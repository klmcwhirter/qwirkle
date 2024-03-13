"""Tests for Bag"""


import math
import random

import pytest

from qwirkle.logic.bag import Bag
from qwirkle.logic.color import colors, set_colors
from qwirkle.logic.shape import set_shapes, shapes


def test_bag_initially_has_108_tiles() -> None:
    bag = Bag(shuffle=False)

    expected = len(shapes) * len(colors) * bag.tile_copies

    assert expected == len(bag)


def test_bag_init_allows_colors_override() -> None:
    expected_colors = [
        {'name': 'black', 'alias': 'black', 'code': 'B'},
        {'name': 'white', 'alias': 'white', 'code': 'W'},
        {'name': 'cyan', 'alias': 'cyan', 'code': 'C'},
        {'name': 'tan', 'alias': 'tan', 'code': 'T'},
        {'name': 'creme', 'alias': 'creme', 'code': 'E'},
        {'name': 'brown', 'alias': 'brown', 'code': 'R'},
    ]
    expected_color_names = {c['name'] for c in expected_colors}
    try:
        # retain a copy of the original colors to retore
        orig_colors = [*colors]

        _ = Bag(shuffle=False, **{'colors': expected_colors})

        color_names = {c.name for c in colors}
        assert expected_color_names == color_names
    finally:
        set_colors(orig_colors)


def test_bag_init_raises_if_not_enough_colors_override() -> None:
    expected_colors = [
        {'name': 'black', 'alias': 'black', 'code': 'B'},
    ]

    with pytest.raises(ValueError):
        try:
            # retain a copy of the original colors to retore
            orig_colors = [*colors]

            _ = Bag(shuffle=False, **{'colors': expected_colors})
        finally:
            set_colors(orig_colors)


def test_bag_init_allows_shapes_override() -> None:
    expected_shapes = [
        {'name': 'box', 'code': 'B'},
        {'name': 'whistle', 'code': 'W'},
        {'name': 'cross', 'code': 'C'},
        {'name': 'thing', 'code': 'T'},
        {'name': 'egg', 'code': 'E'},
        {'name': 'rooster', 'code': 'R'},
    ]
    expected_shape_names = {s['name'] for s in expected_shapes}
    try:
        # retain a copy of the original shapes to retore
        orig_shapes = [*shapes]

        _ = Bag(shuffle=False, **{'shapes': expected_shapes})

        shape_names = {c.name for c in shapes}
        assert expected_shape_names == shape_names
    finally:
        set_shapes(orig_shapes)


def test_bag_init_raises_if_not_enough_shapes_override() -> None:
    expected_shapes = [
        {'name': 'box', 'code': 'B'},
    ]

    with pytest.raises(ValueError):
        try:
            # retain a copy of the original shapes to retore
            orig_shapes = [*shapes]

            _ = Bag(shuffle=False, **{'shapes': expected_shapes})
        finally:
            set_shapes(orig_shapes)


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
