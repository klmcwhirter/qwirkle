"""Tests for a player"""

import pytest

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
