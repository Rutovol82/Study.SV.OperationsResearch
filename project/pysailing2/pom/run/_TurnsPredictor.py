from abc import ABCMeta, abstractmethod

from pysailing2 import TurnParameters, TurnInfo


class TurnsPredictor(metaclass=ABCMeta):

    @abstractmethod
    def get_turn(self, parameters: TurnParameters) -> TurnInfo:
        pass
