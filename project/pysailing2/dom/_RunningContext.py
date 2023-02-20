from dataclasses import dataclass

from . import CourseContext, VelocityInfo


@dataclass(frozen=True)
class RunningContext:

    _course: CourseContext
    _velocity: VelocityInfo
