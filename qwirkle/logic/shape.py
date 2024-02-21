"""Qwirkle shape"""


from dataclasses import dataclass


@dataclass
class Shape:
    """A qwirkle game piece shape"""

    name: str
    code: str


shapes = [
    Shape('Circle', 'O'),
    Shape('Criss-cross', 'X'),
    Shape('Diamond', '^'),
    Shape('Square', '#'),
    Shape('Starburst', '*'),
    Shape('Clover', '+'),
]
