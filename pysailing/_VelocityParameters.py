from scipy.interpolate import LinearNDInterpolator
import numpy as np

from . import VelocityGetter, VelocityMeasurements


class VelocityParameters(VelocityGetter):

    _interpolator = None

    def __init__(self, measurements: VelocityMeasurements = None, *,
                 _points: np.ndarray = None, _values: np.ndarray = None, **ndargs):

        points, values = measurements.nodes(mode='rad', **ndargs) if measurements is not None else (_points, _values)
        self._interpolator = LinearNDInterpolator(points=points, values=values)

    def getv(self, degree, wind: float, mode: str = 'rad'):
        arg = degree if mode == 'rad' else np.radians(degree) if mode == 'deg' else None

        if arg is None:
            raise ValueError(f"Unsupported mode '{mode}'")

        return self._interpolator(arg, wind)
