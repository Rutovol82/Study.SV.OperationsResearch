from abc import ABCMeta

from . import TurnsPredictor, VelocityPredictor


class RunningParametersPredictor(TurnsPredictor, VelocityPredictor, metaclass=ABCMeta):
    pass
