"""Qwirkle Color"""


from dataclasses import dataclass


@dataclass
class Color:
    """A qwirkle game piece color"""

    name: str
    alias: str
    code: str


colors = [
    Color('Red', 'red', 'R'),
    Color('Orange', 'orange', 'O'),
    Color('Yellow', 'yellow', 'Y'),
    Color('Green', 'green', 'G'),
    Color('Blue', 'blue', 'B'),
    Color('Purple', 'purple', 'P'),
]


def set_colors(_colors: list[Color]) -> None:
    global colors
    colors = _colors
