import pytest

from qwirkle.logic.board import Board


def test_board_initialized_per_config(app_config) -> None:
    board = Board(**app_config)

    board_config = app_config['board']
    expected_height = board_config['segment-size'] * board_config['initial-segments']
    assert expected_height == len(board)

    expected_width = board_config['segment-size'] * board_config['initial-segments']
    assert all(expected_width == len(r) for r in board)


def test_board_place_tile(app_config) -> None:
    board = Board(**app_config)
