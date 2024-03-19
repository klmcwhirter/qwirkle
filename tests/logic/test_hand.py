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


def tile_strs_from_hand(hand: Hand) -> list[str]:
    return [s.strip() for s in str(hand).split(': ')[1].split('|')]


def hand_all_unique(hand: Hand) -> bool:
    uniqs = set(tile_strs_from_hand(hand))
    return len(uniqs) == 6


def test_hand_str_represents_current_hand_state(app_config) -> None:
    # Make sure to shuffle in this test to help produce all unique tiles in a Hand
    # but do not shuffle initially to force the lines in the while loop to be run - coverage
    bag = Bag(shuffle=False)

    # This test's design assumes that all tiles in the hand are unique
    hand = Hand(game_bag=bag, **app_config)
    while not hand_all_unique(hand=hand):
        bag = Bag(shuffle=True)
        hand = Hand(game_bag=bag, **app_config)

    orig_len = len(hand)

    # Make sure we can rely on the __str__ method
    hand_strs = tile_strs_from_hand(hand)
    assert len(hand) == len(hand_strs)

    tile = hand.pop()

    # popping a tile should reduce the hand size
    assert len(hand) != orig_len

    # Make sure the tile popped was indeed originally in the hand
    assert str(tile) in hand_strs

    # Assume the hand contained all unique tiles, the popped tile should no longer be in its current state
    hand_str = '|'.join(tile_strs_from_hand(hand))
    assert str(tile) not in hand_str


def test_hand_exchange_replaces_tiles(app_config) -> None:
    bag = Bag(shuffle=True)
    hand = Hand(game_bag=bag, **app_config)

    # pick a couple tiles to exchange
    tiles = [hand[0], hand[3]]

    # clear all but the # of tiles to exchange
    num_tiles = len(tiles)
    del bag[num_tiles:]

    # verify pre-condition is met
    assert num_tiles == len(bag)

    # ACT - perform exchange
    exchange = hand.exchange_tiles(tiles)

    assert num_tiles == len(bag)

    assert num_tiles == len(exchange.old_tiles)
    assert num_tiles == len(exchange.new_tiles)

    for tile in exchange.new_tiles:
        assert tile in hand
