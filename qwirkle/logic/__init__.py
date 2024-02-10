
from enum import StrEnum
from typing import Protocol

from qwirkle.logic.models import Tile


class BoardBase(list[list[Tile | None]]):
    ...


class Direction(StrEnum):
    NORTH = 'n'
    EAST = 'e'
    SOUTH = 's'
    WEST = 'w'


class PlacementStrategy(Protocol):
    def adjust(x: int, y: int, dir: Direction, increment: int = 1) -> tuple[int, int]:
        ...

    def need_to_expand(board: BoardBase, num_tiles: int, x: int, y: int, dir: Direction) -> bool:
        ...
