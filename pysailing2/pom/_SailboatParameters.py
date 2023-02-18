from dataclasses import dataclass

from . import BoatInfo, RunningParametersPredictor


@dataclass
class SailboatParameters:

    info: BoatInfo
    running_parameters: RunningParametersPredictor
