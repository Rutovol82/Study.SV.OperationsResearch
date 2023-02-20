from dataclasses import dataclass
import paxb as pb


@dataclass(frozen=True)
class VelocityInfo:

    velocity: float
