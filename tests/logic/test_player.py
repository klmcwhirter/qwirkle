"""Tests for a player"""

import pytest

from qwirkle.logic.bag import Bag
from qwirkle.logic.hand import Hand
from qwirkle.logic.player import Player


def test_player_can_construct() -> None:
    name = 'player'
    player = Player(name, 0)

    assert player is not None

    assert name == player.name


@pytest.mark.parametrize(
    'name,number',
    [
        ('0', 0),
        ('42', 42)
    ])
def test_player_has_correct_number(name: str, number: int) -> None:
    player = Player(name, number)

    assert number == player.number


def test_player_str_has_hand_none() -> None:
    player = Player('joe', 42)

    player_str = player.__str__()

    assert 'hand=None' in player_str


def test_player_str_has_hand_codes(app_config) -> None:
    bag = Bag(shuffle=False, **app_config)
    player = Player('joe', 42)
    hand = Hand(game_bag=bag, player_name=player.name, **app_config)
    player.hand = hand

    player_str = player.__str__()
    assert 'tiles=P+ | P+' in player_str

    # print(player_str)
