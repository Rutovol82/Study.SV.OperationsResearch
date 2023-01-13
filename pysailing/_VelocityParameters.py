from typing import Sequence, Tuple

from scipy.interpolate import LinearNDInterpolator
import numpy as np


class VelocityParameters:

    _interpolator = None

    def __init__(self, *, _points: Sequence[Tuple[float]], _measurements: Sequence[float], _symmetric=True):
        self._interpolator = self._build_interp(_points, _measurements, symmetric=_symmetric)

    @staticmethod
    def _build_interp(raw_points, raw_measurements, *, symmetric=True):

        points, values = raw_points, raw_measurements

        if symmetric:
            symmetric_points, symmetric_measurements = [], []

            for point, value in zip(raw_points, raw_measurements):
                if 0 <= point[0] < 180:
                    symmetric_points.append((360 - point[0], point[1]))
                    symmetric_measurements.append(value)

            points, values = points + symmetric_points, values + symmetric_measurements

        return LinearNDInterpolator(points=np.array(points), values=np.array(values))

    def __getitem__(self, item):
        try:
            return self._interpolator(*item)
        except TypeError as e:
            raise ValueError(e)
