from abc import abstractmethod


class VelocityGetter:

    @abstractmethod
    def getv(self, degree, wind: float, mode: str):
        pass

    def __getitem__(self, item):
        try:
            return self.getv(*item)
        except TypeError or ValueError as e:
            raise ValueError(e)
