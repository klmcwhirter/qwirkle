"""Tests for board - expanding the board"""


import pytest

from qwirkle.logic import Direction
from qwirkle.logic.board import Board
from qwirkle.logic.color import colors
from qwirkle.logic.shape import shapes
from qwirkle.logic.tile import Tile


@pytest.mark.parametrize(
    'x,y,dir,expected',
    [
        (0, 0, Direction.WEST, (6, 0)),  # adjust to the right by segment size
        (7, 0, Direction.EAST, (7, 0)),  # no adjustment
        (0, 4, Direction.NORTH, (0, 10)),  # adjust down by segment size
        (8, 0, Direction.SOUTH, (8, 0)),  # no adjustment
    ]
)
def test_board_expand_board_return_value(app_config, x: int, y: int, dir: Direction, expected: tuple[int, int]) -> None:
    board = Board(**app_config)

    rc = board.expand_board(x, y, dir)

    assert expected == rc


@pytest.mark.parametrize(
    ['tiles', 'x', 'new_x', 'dir'],
    [
        ([Tile(colors[i], shapes[2]) for i in range(6)], 4, 10, Direction.WEST),
        ([Tile(colors[i], shapes[2]) for i in range(6)], 7, 7, Direction.EAST)
    ]
)
def test_place_tiles_will_expand_horizontal(app_config, tiles: list[Tile], x: int, new_x: int, dir: Direction) -> None:
    board = Board(**app_config)

    board.place_tiles(tiles, x, 0, dir)

    assert tiles[0] == board.board_cell(new_x, 0)


@pytest.mark.parametrize(
    ['tiles', 'y', 'new_y', 'dir'],
    [
        ([Tile(colors[i], shapes[2]) for i in range(6)], 4, 10, Direction.NORTH),
        ([Tile(colors[i], shapes[2]) for i in range(6)], 8, 8, Direction.SOUTH)
    ]
)
def test_place_tiles_will_expand_vertical(app_config, tiles: list[Tile], y: int, new_y: int, dir: Direction) -> None:
    board = Board(**app_config)

    board.place_tiles(tiles, 0, y, dir)

    assert tiles[0] == board.board_cell(0, new_y)
