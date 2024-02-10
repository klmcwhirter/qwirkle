''''Tests for expanding placement'''

import pytest

from qwirkle.logic import PlacementStrategy
from qwirkle.logic.board import Board, Direction


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
    strategy: PlacementStrategy = app_config['board']['placement']

    rc = strategy.need_to_expand(board, num_tiles, x, y, dir)

    assert expected == rc
