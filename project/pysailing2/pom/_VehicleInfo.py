from dataclasses import dataclass
import paxb as pb


@pb.model(name='boat-info', ns='')
class VehicleInfo:

    name: str
