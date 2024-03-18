"""tests for GameDisplayAdapter"""

import pytest

from qwirkle.gui.bag_adapter import BagDisplayAdapter
from qwirkle.gui.board_adapter import BoardDisplayAdapter
from qwirkle.gui.game_adapter import GameDisplayAdapter
from qwirkle.gui.hand_adapter import HandDisplayAdapter
from qwirkle.logic.game import Game


def test_can_construct(app_config) -> None:
    adapter = GameDisplayAdapter(**app_config)

    assert adapter is not None


def test_game_init_sets_per_config(app_config) -> None:
    adapter = GameDisplayAdapter(**app_config)

    assert adapter.config is not None
    assert app_config == adapter.config

    assert adapter.game is not None
    assert isinstance(adapter.game, Game)

    assert adapter.width is not None
    assert adapter.height is not None
    assert adapter.bg_color is not None


def test_game_reset(app_config, fake_game_log):
    adapter = GameDisplayAdapter(**app_config)
    adapter.game.game_log = fake_game_log

    adapter.reset()

    assert adapter.bag_adapter is not None
    assert isinstance(adapter.bag_adapter, BagDisplayAdapter)

    assert adapter.board_adapter is not None
    assert isinstance(adapter.board_adapter, BoardDisplayAdapter)

    assert adapter.hand_adapter is not None
    assert isinstance(adapter.hand_adapter, HandDisplayAdapter)


@pytest.mark.parametrize(
    'add_on',
    [
        ('@exclude'),
        (None),
        ('Adding on some text')
    ]
)
def test_set_window_title(app_config, add_on: str | None) -> None:
    adapter = GameDisplayAdapter(**app_config)

    if '@exclude' == add_on:
        msg = adapter.get_window_title()
        assert '@exclude' not in msg
    elif add_on is not None:
        msg = adapter.get_window_title(add_on)
        assert str(add_on) in msg
    else:
        msg = adapter.get_window_title(add_on)
        assert len(msg) > 0
