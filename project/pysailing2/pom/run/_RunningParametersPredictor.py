from abc import ABCMeta

from pysailing2.pom.run.schema import TurnsPredictor, VelocityPredictor


class RunningParametersPredictor(TurnsPredictor, VelocityPredictor, metaclass=ABCMeta):
    pass
