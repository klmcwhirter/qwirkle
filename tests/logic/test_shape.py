"""Tests for shapes"""


import pytest

from qwirkle.logic.shape import shapes


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
def test_shapes_as_expected(expected) -> None:
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
def test_shape_codes_as_expected(expected) -> None:
    found = [s.code for s in shapes if s.code == expected]
    assert [expected] == found
