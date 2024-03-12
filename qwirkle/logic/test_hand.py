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


def hand_all_unique(hand: Hand) -> bool:
    hand_len = len(hand)
    uniqs = set(str(hand).split('|'))
    return len(uniqs) == hand_len


def test_hand_str_represents_current_hand_state(app_config) -> None:
    # Make sure to shuffle in this test to help produce all unique tiles in a Hand
    bag = Bag(shuffle=True)

    # This test's design assumes that all tiles in the hand are unique
    hand = Hand(game_bag=bag, **app_config)
    while not hand_all_unique(hand):
        bag = Bag(shuffle=True)
        hand = Hand(game_bag=bag, **app_config)

    orig_len = len(hand)

    # Make sure we can rely on the __str__ method
    hand_str = str(hand)
    assert len(hand) == len(hand_str.split('|'))

    tile = hand.pop()

    # popping a tile should reduce the hand size
    assert len(hand) != orig_len

    # Make sure the tile popped was indeed originally in the hand
    assert str(tile) in hand_str

    # Assume the hand contained all unique tiles, the popped tile should no longer be in its current state
    hand_str = str(hand)
    assert str(tile) not in hand_str
