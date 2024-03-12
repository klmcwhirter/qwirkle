"""tests for headless Game"""


from qwirkle.logic.game import Game


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


def test_game_reset_recreates_properties(app_config) -> None:
    game = Game(**app_config)

    # save references
    bag = game.bag
    board = game.board
    hands = game.hands

    game.reset()

    assert bag is not game.bag
    assert board is not game.board
    assert hands is not game.hands
