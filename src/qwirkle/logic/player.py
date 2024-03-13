"""A Qwirkle game player"""

from dataclasses import dataclass


@dataclass
class Player:
    name: str
    number: int
