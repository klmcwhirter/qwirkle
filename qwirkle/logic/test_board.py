import pytest

from qwirkle.logic import Direction
from qwirkle.logic.board import Board
from qwirkle.logic.models import Tile, colors, shapes


def test_board_initialized_per_config(app_config) -> None:
    board = Board(**app_config)

    board_config = app_config['board']
    expected_height = board_config['segment-size'] * board_config['initial-segments']
    assert expected_height == len(board)

    expected_width = board_config['segment-size'] * board_config['initial-segments']
    assert all(expected_width == len(r) for r in board)


def test_board_place_tiles_occupied(app_config) -> None:
    board = Board(**app_config)

    tile = Tile(colors[0], shapes[0])
    board.place_tiles([tile], 0, 0, Direction.NORTH)

    assert tile == board[0][0]

    with pytest.raises(ValueError):
        tile1 = Tile(colors[1], shapes[1])
        board.place_tiles([tile1], 0, 0, Direction.NORTH)
