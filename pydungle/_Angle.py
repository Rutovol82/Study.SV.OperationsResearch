from typing import Union
from numpy import deg2rad, rad2deg


class Angle:

    COMPARE_BY: str = 'deg'
    COMPARE_ND: int = None

    deg: Union[float, int]
    rad: int

    def __init__(self, *, deg: Union[float, int] = None, rad: float = None):

        if deg is None and rad is None:
            raise ValueError("No angle value passed.")

        if deg is not None and rad is not None:
            raise ValueError("Ambiguous parameters passed. Pass only 'rad' or 'deg' parameter value.")

        self._rad, self.deg = (deg2rad(deg), deg) if rad is None else (rad, rad2deg(rad))

    def __str__(self):
        return f"({self.deg}° ≈ {self._rad})"

    def __repr__(self):
        return str(self._val())

    def _val(self):

        if self.COMPARE_BY == 'rad':
            val = self._rad
        elif self.COMPARE_BY == 'deg':
            val = self.deg
        else:
            raise ValueError(f"Unknown COMPARE_BY constant value '{self.COMPARE_BY}'")

        if self.COMPARE_ND is not None:
            val = round(val, self.COMPARE_ND)

        return val

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self._val() == other._val()

    def __hash__(self):
        return hash(self._val())
