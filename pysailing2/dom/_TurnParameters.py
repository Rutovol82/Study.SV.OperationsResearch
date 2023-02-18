from dataclasses import dataclass
from pydungle import Angle

from . import RunningContext


@dataclass(frozen=True)
class TurnParameters:

    initial: RunningContext
    target: Angle
