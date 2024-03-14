
from enum import StrEnum
from typing import Protocol

from qwirkle.logic.tile import Tile


class _BoardBase(list[list[Tile | None]]):
    def board_cell(self, x: int, y: int) -> Tile | None:
        return self[y][x]

    def board_row(self, y: int) -> list[Tile | None]:
        return self[y]


class Direction(StrEnum):
    NORTH = 'n'
    EAST = 'e'
    SOUTH = 's'
    WEST = 'w'


class BoardExpansionStrategy(Protocol):
    def adjust(self, x: int, y: int, dir: Direction | None, increment: int = 1) -> tuple[int, int]:
        ...

    def grow_horizontal(self, board: _BoardBase, add_segments: int, dir: Direction) -> None:
        ...

    def grow_vertical(self, board: _BoardBase, add_segments: int, dir: Direction) -> None:
        ...

    def need_to_expand(self, board: _BoardBase, num_tiles: int, x: int, y: int, dir: Direction) -> bool:
        ...
