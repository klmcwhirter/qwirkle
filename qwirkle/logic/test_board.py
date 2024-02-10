import pytest

from qwirkle.logic.board import (Board, Direction, create_row_part,
                                 create_segment)


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


def test_board_initialized_per_config(app_config) -> None:
    board = Board(**app_config)

    board_config = app_config['board']
    expected_height = board_config['segment-size'] * board_config['initial-segments']
    assert expected_height == len(board)

    expected_width = board_config['segment-size'] * board_config['initial-segments']
    assert all(expected_width == len(r) for r in board)


@pytest.mark.parametrize(
    ['dir'],
    [
        Direction.EAST,
        Direction.WEST,
    ],
)
def test_board_can_grow_horizontally(app_config, dir: str) -> None:
    board = Board(**app_config)

    board._grow_horizontal(2, dir)

    board_config = app_config['board']
    expected_height = board_config['segment-size'] * board_config['initial-segments']
    assert expected_height == len(board)

    expected_width = board_config['segment-size'] * (board_config['initial-segments'] + 2)
    assert all(expected_width == len(r) for r in board)


def test_board_grow_horizontally_throws_with_bad_dir(app_config) -> None:
    board = Board(**app_config)

    with pytest.raises(ValueError):
        board._grow_horizontal(2, 'bogus')


@pytest.mark.parametrize(
    ['dir'],
    [
        Direction.SOUTH,
        Direction.NORTH,
    ],
)
def test_board_can_grow_vertically(app_config, dir: str) -> None:
    board = Board(**app_config)

    board._grow_vertical(2, dir)

    board_config = app_config['board']
    expected_height = board_config['segment-size'] * (board_config['initial-segments'] + 2)
    assert expected_height == len(board)

    expected_width = board_config['segment-size'] * board_config['initial-segments']
    assert all(expected_width == len(r) for r in board)


def test_board_grow_vertically_throws_with_bad_dir(app_config) -> None:
    board = Board(**app_config)

    with pytest.raises(ValueError):
        board._grow_vertical(2, 'bogus')


def test_board_place_tile(app_config) -> None:
    board = Board(**app_config)
