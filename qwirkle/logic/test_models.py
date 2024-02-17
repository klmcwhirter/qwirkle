"""Tests for game logic models"""


import math
import random

import pytest

from qwirkle.logic.models import Bag, Hand, colors, shapes


@pytest.mark.parametrize(
    'expected',
    [
        'Red',
        'Orange',
        'Yellow',
        'Green',
        'Blue',
        'Purple',
    ],
)
def test_colors_as_expected(expected):
    found = [c.name for c in colors if c.name == expected]
    assert [expected] == found


@pytest.mark.parametrize(
    'expected',
    [
        'Circle',
        'Criss-cross',
        'Diamond',
        'Square',
        'Starburst',
        'Clover',
    ],
)
def test_shapes_as_expected(expected):
    found = [s.name for s in shapes if s.name == expected]
    assert [expected] == found


@pytest.mark.parametrize(
    'expected',
    [
        'O',
        'X',
        '^',
        '#',
        '*',
        '+',
    ],
)
def test_shape_codes_as_expected(expected):
    found = [s.code for s in shapes if s.code == expected]
    assert [expected] == found


def test_bag_initially_has_108_tiles():
    bag = Bag(shuffle=False)

    expected = len(shapes) * len(colors) * bag.tile_copies

    assert expected == len(bag)


def test_bag_shuffle_randomizes_bag():
    random.seed(math.pi)

    bag = Bag(shuffle=False)

    first_shape = bag[0].shape
    num_colors = len(colors)
    num_tiles_for_first_shape = num_colors * bag.tile_copies
    tiles_for_first_shape = bag[:num_tiles_for_first_shape]

    assert all(t.shape == first_shape for t in tiles_for_first_shape)

    bag.shuffle()

    tiles_for_first_shape = bag[:num_tiles_for_first_shape]

    assert not all(t.shape != first_shape for t in tiles_for_first_shape)


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
