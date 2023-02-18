from . import RunningParametersPredictor, VelocityPredictor, TurnsPredictor
from ... import CourseContext, VelocityInfo, TurnParameters, TurnInfo


class RunningParameters(RunningParametersPredictor):

    _turning: TurnsPredictor
    _velocity: VelocityPredictor

    def __init__(self, *, turning: TurnsPredictor, velocity: VelocityPredictor):
        self._turning = turning
        self._velocity = velocity

    def get_turn(self, parameters: TurnParameters) -> TurnInfo:
        pass

    def get_velocity(self, context: CourseContext = None) -> VelocityInfo:
        pass

    @property
    def turning(self):
        return self._turning

    @property
    def velocity(self):
        return self._velocity
