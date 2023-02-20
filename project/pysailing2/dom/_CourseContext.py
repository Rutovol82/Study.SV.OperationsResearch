from dataclasses import dataclass
from pydungle import Angle


@dataclass(frozen=True)
class CourseContext:

    course_angle: Angle
    wind_speed: float
