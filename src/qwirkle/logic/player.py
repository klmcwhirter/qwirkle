"""A Qwirkle game player"""

from dataclasses import dataclass, field

from qwirkle.logic.hand import Hand


@dataclass
class Player:
    name: str
    number: int
    hand: Hand | None = field(default=None, init=False, compare=False)
    active: bool = field(default=False, init=False, compare=False)

    def __str__(self) -> str:
        hand_str = f'{self.hand!r}' if self.hand is not None else 'None'
        return f'Player(name={self.name}, number={self.number}, active={self.active}, hand={hand_str})'
