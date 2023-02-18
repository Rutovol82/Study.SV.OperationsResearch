from abc import ABC, abstractmethod

from .... import TurnParameters, TurnInfo


class TurnsPredictor(metaclass=ABC):

    @abstractmethod
    def get_turn(self, parameters: TurnParameters) -> TurnInfo:
        pass
