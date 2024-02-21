"""Tests for colors"""


import pytest

from qwirkle.logic.color import colors


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
