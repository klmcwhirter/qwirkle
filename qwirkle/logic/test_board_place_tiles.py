"""Tests for board - placing tiles"""


import pytest

from qwirkle.logic import Direction
from qwirkle.logic.board import Board
from qwirkle.logic.color import colors
from qwirkle.logic.shape import shapes
from qwirkle.logic.tile import Tile


@pytest.mark.parametrize(
    ['tiles', 'x', 'y', 'dir'],
    [
        # Single tile
        ([Tile(colors[0], shapes[0])], 5, 5, Direction.NORTH),
        ([Tile(colors[0], shapes[0])], 5, 5, Direction.SOUTH),
        ([Tile(colors[0], shapes[0])], 5, 5, Direction.WEST),
        ([Tile(colors[0], shapes[0])], 5, 5, Direction.EAST),

        # Multiple tiles
        ([Tile(colors[i], shapes[2]) for i in range(6)], 0, 5, Direction.NORTH),
        ([Tile(colors[0], shapes[i]) for i in range(3)], 0, 7, Direction.SOUTH),
        ([Tile(colors[i], shapes[2]) for i in range(6)], 5, 0, Direction.WEST),
        ([Tile(colors[0], shapes[i]) for i in range(3)], 7, 0, Direction.EAST),
    ],
)
def test_can_place_tiles(app_config, tiles: list[Tile], x: int, y: int, dir: Direction) -> None:
    board = Board(**app_config)

    # print(f'before: board=\n{board}')

    board.place_tiles(tiles, x, y, dir)

    # print(f'after: board=\n{board}')

    assert tiles[0] == board[y][x]
