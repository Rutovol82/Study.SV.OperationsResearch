from typing import Dict

import numpy as np

from . import VelocityGetter


class VelocityMeasurements(VelocityGetter):

    _winds: np.ndarray = None
    _angles: np.ndarray = None
    _velocities: np.ndarray = None

    _winds_map: Dict[float, int]
    _angles_map: Dict[float, int]

    def __init__(self, winds, angles, velocities):

        self._winds = np.array(winds) if type(winds) is not np.ndarray else winds
        self._angles = np.array(angles) if type(angles) is not np.ndarray else angles
        self._velocities = np.array(velocities) if type(velocities) is not np.ndarray else velocities

        self._angles_map = {value: index for index, value in zip(range(self._angles.shape[0]), self._angles)}
        self._winds_map = {value: index for index, value in zip(range(self._winds.shape[0]), self._winds)}

    @staticmethod
    def from_csv(reader):

        angles, velocities = [], []
        winds = [float(value) for value in next(reader)[1:]]

        for row in reader:
            angles.append(float(row[0]))
            velocities.append([float(value) for value in row[1:]])

        return VelocityMeasurements(winds, angles, velocities)

    def winds(self) -> np.ndarray:
        return self._winds

    def angles(self) -> np.ndarray:
        return self._angles

    def getv(self, degree, wind: float, _mode: str = 'deg'):

        if _mode != 'deg':
            raise ValueError("Only degrees ('deg') mode is supported.")

        col = self._winds_map.get(wind, None)

        if col is None:
            return float('nan') if type(degree) is not np.ndarray \
                   else np.array([float('nan') for _ in range(degree.shape[0])])

        def _get(deg):
            row = self._angles_map.get(deg, None)
            if row is None:
                return float('nan')
            return self._velocities[row][col]

        if type(degree) is not np.ndarray:
            return _get(degree)

        result = []
        for value in degree:
            result.append(_get(value))
        return np.array(result)

    def nodes(self, *, symmetric=True, add_zero=True, mode: str = 'deg') -> (np.ndarray, np.ndarray):

        points_set, points, values = set(), list(), list()
        angles_iter = self._angles if mode == 'deg' else np.radians(self._angles) if mode == 'rad' else None

        if angles_iter is None:
            raise ValueError(f"Unsupported mode '{mode}'.")

        def _append(point, value):
            if point not in points_set:
                points_set.add(point)
                points.append(point)
                values.append(value)

        def _add(ang, wnd, val):
            _append((ang, wnd), val)
            if symmetric:
                _append((360 - ang, wnd), val)

        for angle, row in zip(self._angles, range(len(self._angles))):

            if add_zero:
                _add(angle, 0.0, 0.0)

            for wind, col in zip(self._winds, range(len(self._winds))):
                velocity = self._velocities[row, col]
                _add(angle, wind, velocity)

        return np.array(points), np.array(values)
