from abc import ABCMeta, abstractmethod

from pysailing2 import CourseContext, VelocityInfo


class VelocityPredictor(metaclass=ABCMeta):

    @abstractmethod
    def get_velocity(self, context: CourseContext = None) -> VelocityInfo:
        pass
