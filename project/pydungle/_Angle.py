from typing import Union
from numpy import deg2rad, rad2deg

from . import AngleQuantities


class Angle:

    OPERATE_BY: AngleQuantities = AngleQuantities.DEG
    COMPARE_ND: Union[int, None] = None

    _deg: Union[float, int]
    _rad: int

    def __init__(self, value: Union[int, float] = None, *, deg: Union[float, int] = None, rad: float = None):

        if value is not None:
            if self.OPERATE_BY == AngleQuantities.DEG:
                deg = value
            elif self.OPERATE_BY == AngleQuantities.RAD:
                rad = float(value)

        if deg is None and rad is None:
            raise ValueError("No angle value passed.")

        self._rad = rad if rad is not None else deg2rad(deg)
        self._deg = deg if deg is not None else rad2deg(rad)

    @property
    def deg(self):
        return self._deg

    @property
    def rad(self):
        return self._rad

    @property
    def _comparable(self):
        return self._operable if self.COMPARE_ND is None else round(self._operable, self.COMPARE_ND)

    @property
    def _operable(self):
        return self.rad if self.OPERATE_BY == AngleQuantities.RAD \
          else self.deg if self.OPERATE_BY == AngleQuantities.DEG \
          else None

    def __str__(self):
        return f"({self.deg}° ≈ {self.rad})"

    def __repr__(self):
        return str(self._operable)

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self._comparable == other._comparable

    def __hash__(self):
        return hash(self._comparable)

    @classmethod
    def _unpack(cls, value):

        if isinstance(value, cls):
            return value._operable

        if type(value) in [float, int]:
            return value

        raise TypeError(f"Unsupported operand type {type(value)}")

    def __float__(self):
        return float(self._operable)

    def __add__(self, other):
        return Angle(self._operable + self._unpack(other))

    def __sub__(self, other):
        return Angle(self._operable - self._unpack(other))

    def __mul__(self, other):
        return Angle(self._operable * self._unpack(other))

    def __truediv__(self, other):
        return Angle(self._operable / self._unpack(other))

    def __floordiv__(self, other):
        return Angle(self._operable // self._unpack(other))

    def __mod__(self, other):
        return Angle(self._operable % self._unpack(other))

    def __divmod__(self, other):
        return Angle(divmod(self._operable, self._unpack(other)))
