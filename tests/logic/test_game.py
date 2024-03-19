"""tests for headless Game"""


from dataclasses import asdict

from qwirkle.logic import Direction
from qwirkle.logic.game import Game
from qwirkle.logic.game_log import GameEventName


def test_game_can_construct(app_config) -> None:
    game = Game(**app_config)

    assert game is not None


def test_game_has_needed_properties(app_config) -> None:
    game = Game(**app_config)

    assert game.game_log is not None

    assert game.bag is not None
    assert len(game.bag) > 0

    assert game.board is not None
    assert len(game.board) > 0

    assert game.hands is not None
    assert len(game.hands) > 0


def test_game_exchange_tiles_logs_event(app_config) -> None:
    game = Game(**app_config)

    exchange = game.exchange_tiles(
        player=game.current_player,
        tiles=[
            game.hands[game.current_player.number][0],
            game.hands[game.current_player.number][3],
        ],
    )

    entries = [e for e in game.game_log.entries()]

    assert len(entries) > 0

    event = entries[0][1]
    assert GameEventName.EXCHG == event.name

    exchange_dict = asdict(exchange)
    assert exchange_dict == event.data


def test_game_exchange_tiles_by_index_logs_event(app_config) -> None:
    game = Game(**app_config)

    exchange = game.exchange_tiles_by_index(
        player_index=game.current_player.number,
        tile_indexes=[0, 3]
    )

    entries = [e for e in game.game_log.entries()]

    assert len(entries) > 0

    event = entries[0][1]
    assert GameEventName.EXCHG == event.name

    exchange_dict = asdict(exchange)
    assert exchange_dict == event.data


def test_game_place_tiles_logs_event(app_config) -> None:
    game = Game(**app_config)

    placement = game.place_tiles(
        player=game.current_player,
        tiles=[],
        x=0, y=0,
        dir=Direction.NORTH
    )

    entries = [e for e in game.game_log.entries()]

    assert len(entries) > 0

    event = entries[0][1]
    assert GameEventName.PLACE == event.name

    placement_dict = asdict(placement)
    assert placement_dict == event.data


def test_game_exit_game_logs_event(app_config, fake_game_log) -> None:
    game = Game(**app_config)
    game.game_log = fake_game_log

    assert 0 == len(game.game_log._log)

    game.exit_game()

    assert any(GameEventName.EXITG == e.event.name for e in game.game_log._log)


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
