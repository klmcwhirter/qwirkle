"""tests for headless Game"""


from qwirkle.logic.game import Game
from qwirkle.logic.game_log import GameEventName


def test_game_can_construct(app_config) -> None:
    game = Game(**app_config)

    assert game is not None


def test_game_has_needed_properties(app_config) -> None:
    game = Game(**app_config)

    assert game.bag is not None
    assert len(game.bag) > 0

    assert game.board is not None
    assert len(game.board) > 0

    assert game.hands is not None
    assert len(game.hands) > 0


def test_game_reset_recreates_properties(app_config, fake_game_log) -> None:
    game = Game(**app_config)
    game.game_log = fake_game_log

    # save references
    bag = game.bag
    board = game.board
    hands = game.hands

    game.reset()

    assert bag is not game.bag
    assert board is not game.board
    assert hands is not game.hands


def test_game_reset_logs_event(app_config, fake_game_log) -> None:
    game = Game(**app_config)
    game.game_log = fake_game_log

    assert 0 == len(game.game_log._log)

    game.reset()

    assert any(GameEventName.RESET == e.event.name for e in game.game_log._log)
