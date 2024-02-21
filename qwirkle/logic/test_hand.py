"""Tests for game logic models"""


from qwirkle.logic.bag import Bag
from qwirkle.logic.hand import Hand


def test_hand_initializes_per_config(app_config) -> None:
    bag = Bag(shuffle=False)

    hand = Hand(game_bag=bag, **app_config)

    expected_num_tiles = app_config['hand']['tiles']
    assert expected_num_tiles == len(hand)


def test_hand_init_reduces_bag_size(app_config) -> None:
    bag = Bag(shuffle=False)
    bag_size = len(bag)

    _ = Hand(game_bag=bag, **app_config)

    expected_num_tiles = app_config['hand']['tiles']

    assert (bag_size - expected_num_tiles) == len(bag)
