import numpy as np

from . import VelocityGetter


class AnglesComputer:

    _velocities: VelocityGetter = None

    def __init__(self, velocities: VelocityGetter = None):
        self._velocities = velocities

    @staticmethod
    def _get_fd_fr(w, d, r):
        if 0 <= w <= 180:
            fd = abs(w - d)
            fr = (fd + d + r) if w > d else (- fd + d + r)
        else:
            fd = 360 - w + d
            fr = (fd - d - r) if w <= 270 else (- fd + d + r)
        return fd, fr

    @staticmethod
    def _get_sd_sr(sc, d, r):
        base = sc / np.sin(np.radians(d + r))
        return base * np.sin(np.radians(r)), base * np.sin(np.radians(d))

    def _get_t_(self, s_, f_, wind):
        v_ = self._velocities.getv(f_, wind, mode='deg')
        return float('inf') if v_ == 0 else s_ / v_

    def _get_tt(self, fd, fr, sd, sr, wind):
        return self._get_t_(sd, fd, wind) + self._get_t_(sr, fr, wind)

    def _get_time(self, sc, w, wind, d=None, r=None):
        if d is None or r is None:
            return self._get_t_(sc, w, wind)
        return self._get_tt(*self._get_fd_fr(w, d, r), *self._get_sd_sr(sc, d, r), wind)

    def get_score(self, wangle, wspeed, dangle=None, rangle=None):
        return self._get_time(1, wangle, wspeed, dangle, rangle)

    def scores(self, wangle, wspeed, *, min_angle=0.1):

        d_, r_, scr_grid = np.linspace(0, 90), np.linspace(0, 90), []

        direct = self.get_score(wangle, wspeed)
        best = (0, 0, direct)

        for d in d_:

            scr_row = []

            for r in r_:

                a = d + r

                if 180 - a < min_angle:
                    scr_row.append(float('inf'))

                elif a < min_angle:
                    scr_row.append(direct)

                else:
                    scr_row.append(self.get_score(wangle, wspeed, d, r))
                    if scr_row[-1] < best[2]:
                        best = (d, r, scr_row[-1])

            scr_grid.append(scr_row)

        return np.array(d_), np.array(r_), np.array(scr_grid), best
