"""Tests for board - expanding the board"""


import pytest

from qwirkle.logic.board import Board, Direction
from qwirkle.logic.models import Tile, colors, shapes


@pytest.mark.parametrize(
    ['tiles', 'x', 'new_x', 'dir'],
    [
        ([Tile(colors[i], shapes[2]) for i in range(6)], 4, 10, Direction.WEST),
        ([Tile(colors[i], shapes[2]) for i in range(6)], 7, 7, Direction.EAST)
    ]
)
def test_will_expand_place_tiles_horizontal(app_config, tiles: list[Tile], x: int, new_x: int, dir: Direction) -> None:
    board = Board(**app_config)

    board.place_tiles(tiles, x, 0, dir)

    assert tiles[0] == board[0][new_x]


@pytest.mark.parametrize(
    ['tiles', 'y', 'new_y', 'dir'],
    [
        ([Tile(colors[i], shapes[2]) for i in range(6)], 4, 10, Direction.NORTH),
        ([Tile(colors[i], shapes[2]) for i in range(6)], 8, 8, Direction.SOUTH)
    ]
)
def test_will_expand_place_tiles_vertical(app_config, tiles: list[Tile], y: int, new_y: int, dir: Direction) -> None:
    board = Board(**app_config)

    board.place_tiles(tiles, 0, y, dir)

    assert tiles[0] == board[new_y][0]
