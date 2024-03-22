"""tests for headless Game"""


from dataclasses import asdict

import pytest

from qwirkle.logic import Direction
from qwirkle.logic.game import Game
from qwirkle.logic.game_log import GameEventName
from qwirkle.logic.player import Player


def test_game_can_construct(app_config) -> None:
    game = Game(**app_config)

    assert game is not None


def test_game_has_needed_properties(app_config) -> None:
    game = Game(**app_config)

    assert 0 == game._current_player_index
    assert 0 == game.current_player_index

    assert game._players is not None
    assert 2 == len(game._players)
    assert 2 == len(game.players)

    assert game.game_log is not None

    assert game.bag is not None
    assert len(game.bag) > 0

    assert game.board is not None
    assert len(game.board) > 0


def test_game_current_player_getter(app_config) -> None:
    game = Game(**app_config)

    player: Player = game.current_player

    assert game._players[0] == player


def test_game_current_player_setter(app_config) -> None:
    game = Game(**app_config)
    player: Player = game._players[1]

    game.current_player = player

    assert 1 == game._current_player_index


def test_game_current_player_setter_raises_when_invalid(app_config) -> None:
    game = Game(**app_config)
    player: Player = Player('bogus', 3)

    with pytest.raises(ValueError):
        game.current_player = player


def test_game_current_player_index_getter(app_config) -> None:
    game = Game(**app_config)

    player_index: int = game.current_player_index

    assert 0 == player_index


def test_game_current_player_index_setter(app_config) -> None:
    game = Game(**app_config)
    player_index: int = 1

    game.current_player_index = player_index

    assert 1 == game._current_player_index


def test_game_current_player_index_setter_raises_when_invalid(app_config) -> None:
    game = Game(**app_config)
    player_index: int = 3

    with pytest.raises(IndexError):
        game.current_player_index = player_index


def test_game_players_getter(app_config) -> None:
    game = Game(**app_config)

    players: list[Player] = game.players

    # game.players returns a copy
    assert game._players is not players
    assert game._players == players

    # But copies are different
    assert players is not game.players


def test_game_players_setter(app_config) -> None:
    game = Game(**app_config)
    players: list[Player] = [Player('player1', 10), Player('player2', 11)]

    game.players = players

    assert game._players is not None

    assert 10 == game._players[0].number
    assert 11 == game._players[1].number


@pytest.mark.parametrize(
    'players',
    [
        ([]),
        (None),
        ([Player('player1', 1)])
    ]
)
def test_game_players_setter_raises_when_invalid(app_config, players: list[Player]) -> None:
    game = Game(**app_config)

    with pytest.raises(ValueError):
        game.players = players


def test_game_exchange_tiles_logs_event(app_config) -> None:
    game = Game(**app_config)

    current_player = game.current_player

    if current_player.hand is None:
        pytest.fail('current_player mujst have a hand')

    exchange = game.exchange_tiles(
        tiles=[
            current_player.hand[0],
            current_player.hand[3],
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

    exchange = game.exchange_tiles_by_index(tile_indices=[0, 3])

    entries = [e for e in game.game_log.entries()]

    assert len(entries) > 0

    event = entries[0][1]
    assert GameEventName.EXCHG == event.name

    exchange_dict = asdict(exchange)
    assert exchange_dict == event.data


def test_game_place_tiles_logs_event(app_config) -> None:
    game = Game(**app_config)

    placement = game.place_tiles(
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

    game.reset()

    assert bag is not game.bag
    assert board is not game.board


def test_game_reset_logs_event(app_config, fake_game_log) -> None:
    game = Game(**app_config)
    game.game_log = fake_game_log

    assert 0 == len(game.game_log._log)

    game.reset()

    assert any(GameEventName.RESET == e.event.name for e in game.game_log._log)
