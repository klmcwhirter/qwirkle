
from enum import StrEnum
from typing import Protocol

from qwirkle.logic.tile import Tile


class BoardBase(list[list[Tile | None]]):
    ...


class Direction(StrEnum):
    NORTH = 'n'
    EAST = 'e'
    SOUTH = 's'
    WEST = 'w'


class BoardExpansionStrategy(Protocol):
    def adjust(x: int, y: int, dir: Direction, increment: int = 1) -> tuple[int, int]:
        ...

    def grow_horizontal(board: BoardBase, add_segments: int, dir: Direction) -> None:
        ...

    def grow_vertical(board: BoardBase, add_segments: int, dir: Direction) -> None:
        ...

    def need_to_expand(board: BoardBase, num_tiles: int, x: int, y: int, dir: Direction) -> bool:
        ...
