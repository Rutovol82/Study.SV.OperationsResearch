from .. import VelocityPredictor
from .... import CourseContext, VelocityInfo


class VelocityParameters(VelocityPredictor):

    _measurements: VelocityPredictor
    _predictor: VelocityPredictor = None

    def get_velocity(self, context: CourseContext = None) -> VelocityInfo:
        if self._predictor is not None:
            return self._predictor.get_velocity(context)
        return self._measurements.get_velocity(context)

    def __init__(self):
        pass

    def set_predictor(self):
        pass

    @property
    def measurements(self):
        return self._measurements
