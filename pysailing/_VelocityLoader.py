from typing import List, Iterable, Tuple, Sequence
import csv

from . import VelocityParameters


class VelocityLoader:

    _reader = None

    _winds: List[float] = None
    _points: List[Tuple[float]] = None
    _measurements: List[float] = None

    def __init__(self, source: Iterable[str] = None, *csv_args, csv_reader=None, **csv_kwargs):
        self._reader = csv_reader if csv_reader is not None else csv.reader(source, *csv_args, **csv_kwargs)

    def _read_winds(self):
        self._winds = [0.0] + [float(value) for value in next(self._reader)[1:]]

    def _read_data(self, size: int, function):
        for i in range(size):
            row = next(self._reader)
            angle = float(row[0])

            self._points.append((angle, 0.0))
            self._measurements.append(0.0)

            function(i, row[1:], angle)

    def _read_mono(self, i, data, angle):
        self._points.append((angle, self._winds[i + 1]))
        self._measurements.append(float(data[i]))

    def _read_block(self, _, data, angle):
        for value, wind in zip(data, self._winds[1:]):
            self._points.append((angle, wind))
            self._measurements.append(float(value))

    def _read(self):
        try:
            self._points, self._measurements = [], []
            self._read_winds()

            self._read_data(1, self._read_block)

            n = len(self._winds) - 1

            #self._read_data(n, self._read_mono)
            self._read_data(8, self._read_block)
            #self._read_data(n, self._read_mono)

        except StopIteration or IOError as e:
            raise ValueError(e)

    def load(self, *params_args, **params_kwargs) -> VelocityParameters:
        self._read()
        return VelocityParameters(*params_args, _points=self._points, _measurements=self._measurements, **params_kwargs)

    def _check_unload(self):
        if self._winds is None:
            raise ValueError("Data requested before loading. Load data first.")

    def winds(self) -> Sequence[float]:
        return self._winds
