from abc import ABC, abstractmethod

from .... import CourseContext, VelocityInfo


class VelocityPredictor(metaclass=ABC):

    @abstractmethod
    def get_velocity(self, context: CourseContext = None) -> VelocityInfo:
        pass
