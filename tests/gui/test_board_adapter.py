"""tests for BoardDisplayAdapter"""

from qwirkle.gui.board_adapter import (BoardDisplayAdapter,
                                       pygame_ce_board_adapter)
from qwirkle.gui.tile_adapter import TileDisplayAdapter
from qwirkle.logic.board import Board


def test_can_construct(app_config) -> None:
    board = Board(**app_config)
    adapter = BoardDisplayAdapter(board)

    assert adapter is not None


def test_bag_init_sets_per_config(app_config) -> None:
    board = Board(**app_config)
    adapter = BoardDisplayAdapter(board)

    assert board is adapter.board
    assert adapter.tile_adapter is not None
    assert isinstance(adapter.tile_adapter, TileDisplayAdapter)

    assert adapter.font is not None
    assert adapter.font_color is not None
    assert adapter.padx is not None
    assert adapter.pady is not None
    assert adapter.screen_height is not None
    assert adapter.screen_width is not None


def test_pygame_ce_board_adapter_provides_adapter(app_config) -> None:
    board = Board(**app_config)
    adapter = pygame_ce_board_adapter(board)

    assert adapter is not None
    assert isinstance(adapter, BoardDisplayAdapter)
