from dataclasses import dataclass

from . import TurnParameters


@dataclass(frozen=True)
class TurnInfo:

    parameters: TurnParameters
    time: float
