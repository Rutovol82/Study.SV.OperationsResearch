import random
from typing import List, Iterator


def rnd_colors() -> Iterator[str]:
    while True:
        yield get_rnd_color()


def get_rnd_colors(count=None) -> List[str]:
    return [get_rnd_color() for _ in range(count)]


def get_rnd_color() -> str:
    return "#" + ''.join((random.choice('0123456789ABCDEF') for _ in range(6)))
