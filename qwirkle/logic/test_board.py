import pytest

from qwirkle.logic import Direction
from qwirkle.logic.board import Board
from qwirkle.logic.color import colors
from qwirkle.logic.shape import shapes
from qwirkle.logic.tile import Tile


def test_board_initialized_per_config(app_config) -> None:
    board = Board(**app_config)

    board_config = app_config['board']
    expected_side_len = board_config['segment-size'] * board_config['initial-segments']

    assert expected_side_len == len(board)
    assert all(expected_side_len == len(r) for r in board)


def test_board_placed_returns_correct_state(app_config) -> None:
    board = Board(**app_config)

    tile1 = Tile(colors[0], shapes[0])
    board.place_tiles([tile1], 0, 0, Direction.NORTH)
    assert tile1 == board[0][0]

    tile2 = Tile(colors[0], shapes[1])
    board.place_tiles([tile2], 0, 1, Direction.NORTH)
    assert tile2 == board[1][0]

    tiles = [(0, 0, tile1), (0, 1, tile2)]

    rc = board.placed_tiles()

    assert tiles == rc


@pytest.mark.parametrize(
    'reason,adjacent,tiles,expected',
    [
        (
            'colors match',
            Tile(colors[0], shapes[0]),
            [Tile(colors[0], shapes[2]), Tile(colors[0], shapes[3])],
            True
        ),
        (
            'colors match, but duplicate shape',
            Tile(colors[0], shapes[0]),
            [Tile(colors[0], shapes[0]), Tile(colors[0], shapes[3])],
            False
        ),
        (
            'shapes match',
            Tile(colors[0], shapes[0]),
            [Tile(colors[2], shapes[0]), Tile(colors[3], shapes[0])],
            True
        ),
        (
            'shapes match, but duplicate color',
            Tile(colors[0], shapes[0]),
            [Tile(colors[2], shapes[0]), Tile(colors[0], shapes[0])],
            False
        ),
        (
            'one does not match',
            Tile(colors[0], shapes[0]),
            [Tile(colors[0], shapes[2]), Tile(colors[3], shapes[3])],
            False
        ),
        (
            'no match',
            Tile(colors[0], shapes[0]),
            [Tile(colors[2], shapes[2]), Tile(colors[3], shapes[3])],
            False
        )
    ]
)
def test_board_contains_line(app_config, reason: str, adjacent: Tile, tiles: list[Tile], expected: bool) -> None:
    board = Board(**app_config)
    rc = board.contains_line_for(adjacent, tiles)
    assert expected == rc


def test_board_str_contains_codes(app_config) -> None:
    board = Board(**app_config)
    tile1 = Tile(colors[0], shapes[0])
    tile2 = Tile(colors[0], shapes[1])
    tiles = [tile1, tile2]
    board.place_tiles(tiles, 0, 1, Direction.NORTH)

    board_str = str(board)

    for tile in tiles:
        expected = f'{tile!s:>2}'
        assert expected in board_str
