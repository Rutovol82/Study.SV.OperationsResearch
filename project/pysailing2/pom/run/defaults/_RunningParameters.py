from .. import RunningParametersPredictor, VelocityPredictor, TurnsPredictor
from .... import CourseContext, VelocityInfo, TurnParameters, TurnInfo


class RunningParameters(RunningParametersPredictor):

    _turns: TurnsPredictor
    _velocity: VelocityPredictor

    def __init__(self, *, turning: TurnsPredictor, velocity: VelocityPredictor):
        self._turns = turning
        self._velocity = velocity

    def get_turn(self, parameters: TurnParameters) -> TurnInfo:
        pass

    def get_velocity(self, context: CourseContext = None) -> VelocityInfo:
        pass

    @property
    def turns(self):
        return self._turns

    @property
    def velocity(self):
        return self._velocity
