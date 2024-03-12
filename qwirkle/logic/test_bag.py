"""Tests for Bag"""


import math
import random

from qwirkle.logic.bag import Bag
from qwirkle.logic.color import colors
from qwirkle.logic.shape import shapes


def test_bag_initially_has_108_tiles() -> None:
    bag = Bag(shuffle=False)

    expected = len(shapes) * len(colors) * bag.tile_copies

    assert expected == len(bag)


def test_bag_shuffle_randomizes_bag() -> None:
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
