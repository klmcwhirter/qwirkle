"""model the qwirkle objects and game rules"""


import random
from dataclasses import dataclass


@dataclass
class Shape:
    """A qwirkle game piece shape"""

    name: str
    code: str


shapes = [
    Shape('Circle', 'O'),
    Shape('Criss-cross', 'X'),
    Shape('Diamond', '^'),
    Shape('Square', '#'),
    Shape('Starburst', '*'),
    Shape('Clover', '+'),
]


@dataclass
class Color:
    """A qwirkle game piece color"""

    name: str
    alias: str
    code: str


colors = [
    Color('Red', 'red', 'R'),
    Color('Orange', 'orange', 'O'),
    Color('Yellow', 'yellow', 'Y'),
    Color('Green', 'green', 'G'),
    Color('Blue', 'blue', 'B'),
    Color('Purple', 'purple', 'P'),
]


@dataclass
class Tile:
    """a qwirkle game piece - called a Tile"""

    color: Color
    shape: Shape

    def __str__(self) -> str:
        return f'{self.color.code}{self.shape.code}'


class Bag(list[Tile]):
    def __init__(self, shuffle: bool = True, **kwargs) -> None:
        super().__init__()
        self.tile_copies = 3  # default based on standard game rules
        if 'board' in kwargs and 'bag-tile-copies' in kwargs['board']:
            self.tile_copies = kwargs['board']['bag-tile-copies']
        self.reset()
        if shuffle:
            self.shuffle()

    def reset(self) -> None:
        for s in shapes:
            for c in colors:
                for _ in range(self.tile_copies):
                    self.append(Tile(color=c, shape=s))

    def shuffle(self) -> None:
        random.shuffle(self)
