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

    board.place_tiles(app_config['game']['players'][0], tiles, x, y, dir)

    # print(f'after: board=\n{board}')

    assert tiles[0] == board.board_cell(x, y)


def test_board_place_tiles_occupied_raises(app_config) -> None:
    board = Board(**app_config)

    tile = Tile(colors[0], shapes[0])
    board.place_tiles(app_config['game']['players'][0], [tile], 0, 0, Direction.NORTH)

    assert tile == board.board_cell(0, 0)

    with pytest.raises(ValueError):
        board.place_tiles(app_config['game']['players'][1], [tile], 0, 0, Direction.NORTH)


def test_board_place_tiles_adjacent_succeeds(app_config) -> None:
    board = Board(**app_config)

    tile1 = Tile(colors[0], shapes[0])
    board.place_tiles(app_config['game']['players'][0], [tile1], 0, 1, Direction.NORTH)

    assert tile1 == board.board_cell(0, 1)

    tile2 = Tile(colors[1], shapes[1])
    board.place_tiles(app_config['game']['players'][1], [tile2], 0, 0, Direction.NORTH)

    assert tile2 == board.board_cell(0, 0)


def test_board_place_tiles_not_adjacent_raises(app_config) -> None:
    board = Board(**app_config)

    tile = Tile(colors[0], shapes[0])
    board.place_tiles(app_config['game']['players'][0], [tile], 0, 0, Direction.NORTH)

    assert tile == board.board_cell(0, 0)

    # print(f'before: board=\n{board.placed_tiles()}')

    with pytest.raises(ValueError):
        tile1 = Tile(colors[1], shapes[1])
        board.place_tiles(app_config['game']['players'][1], [tile1], 2, 2, Direction.NORTH)
