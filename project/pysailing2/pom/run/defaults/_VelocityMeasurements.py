from typing import Dict, Iterable, Tuple

from .. import VelocityPredictor
from .... import CourseContext, VelocityInfo


class VelocityMeasurements(VelocityPredictor):

    _velocities: Dict[CourseContext, float]

    def __init__(self):
        pass

    def get_velocity(self, context: CourseContext = None) -> VelocityInfo:
        return VelocityInfo(self._velocities[context])

    def __getitem__(self, item):
        return self.get_velocity(item)

    def velocities(self) -> Iterable[Tuple[CourseContext, VelocityInfo]]:
        for context, velocity in self._velocities.items():
            yield context, VelocityInfo(velocity)
