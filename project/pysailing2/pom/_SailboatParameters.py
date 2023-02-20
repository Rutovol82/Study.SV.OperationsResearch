from dataclasses import dataclass

from . import VehicleInfo, RunningParametersPredictor


@dataclass
class SailboatParameters:

    info: VehicleInfo
    running_parameters: RunningParametersPredictor
