"""Qwirkle Tile"""


from dataclasses import dataclass

from qwirkle.logic.color import Color
from qwirkle.logic.shape import Shape


@dataclass
class Tile:
    """a qwirkle game piece - called a Tile"""

    color: Color
    shape: Shape

    def __str__(self) -> str:
        return f'{self.color.code}{self.shape.code}'
