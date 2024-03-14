"""'Tests for expanding the board during placement"""

import pytest

from qwirkle.logic import BoardExpansionStrategy, Direction
from qwirkle.logic.board import Board
from qwirkle.logic.exp_placement import create_row_part, create_segment


def test_create_row_part_has_len() -> None:
    width = 6

    row = create_row_part(width)

    assert width == len(row)


@pytest.mark.parametrize(
    ['expected_width', 'expected_height'],
    [
        (8, 6),
        (14, 12,),
    ],
)
def test_create_segment_has_dimensions(expected_width: int, expected_height: int) -> None:
    segment = create_segment(expected_width, expected_height)

    assert expected_height == len(segment)

    assert all(expected_width == len(r) for r in segment)


@pytest.mark.parametrize(
    ['dir'],
    [
        Direction.EAST,
        Direction.WEST,
    ],
)
def test_exp_can_grow_horizontally(app_config, dir: Direction) -> None:
    board = Board(**app_config)
    strategy: BoardExpansionStrategy = app_config['board']['expansion']

    strategy.grow_horizontal(board, 2, dir)

    board_config = app_config['board']
    expected_height = board_config['segment-size'] * board_config['initial-segments']
    assert expected_height == len(board)

    expected_width = board_config['segment-size'] * (board_config['initial-segments'] + 2)
    assert all(expected_width == len(r) for r in board)


@pytest.mark.parametrize(
    ['dir'],
    [
        Direction.SOUTH,
        Direction.NORTH,
    ],
)
def test_board_can_grow_vertically(app_config, dir: Direction) -> None:
    board = Board(**app_config)
    strategy: BoardExpansionStrategy = app_config['board']['expansion']

    strategy.grow_vertical(board, 2, dir)

    board_config = app_config['board']
    expected_height = board_config['segment-size'] * (board_config['initial-segments'] + 2)
    assert expected_height == len(board)

    expected_width = board_config['segment-size'] * board_config['initial-segments']
    assert all(expected_width == len(r) for r in board)


@pytest.mark.parametrize(
    ['num_tiles', 'x', 'y', 'dir', 'expected'],
    [
        (2, 0, 0, Direction.NORTH, True),
        (2, 0, 1, Direction.NORTH, False),
        (2, 0, 11, Direction.SOUTH, True),
        (2, 0, 10, Direction.SOUTH, False),
        (2, 0, 0, Direction.WEST, True),
        (2, 1, 0, Direction.WEST, False),
        (4, 9, 0, Direction.EAST, True),
        (4, 8, 0, Direction.EAST, False),
    ],
)
def test_need_to_expand_as_expected(app_config, num_tiles: int, x: int, y: int, dir: Direction, expected: bool) -> None:
    board = Board(**app_config)
    strategy: BoardExpansionStrategy = app_config['board']['expansion']

    rc = strategy.need_to_expand(board, num_tiles, x, y, dir)

    assert expected == rc
