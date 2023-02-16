from dataclasses import dataclass
from typing import Dict

from pydungle import *


@dataclass(frozen=True)
class CourseWindContext:
    course_angle: Angle
    wind_speed: float


class VelocityMeasurements:

    _values: Dict[CourseWindContext, float]

    def __init__(self):
        pass

    @classmethod
    def from_csv(cls):
        pass

    @classmethod
    def from_xml(cls):
        pass


if __name__ == '__main__':
    pass
