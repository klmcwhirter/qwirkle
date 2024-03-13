"""headless logic for a game of Qwirkle"""

from qwirkle.logic.bag import Bag
from qwirkle.logic.board import Board
from qwirkle.logic.hand import Hand


class Game:
    def __init__(self, **kwargs) -> None:
        self.config = kwargs  # also used in adapter

        self.players = self.config['game']['players']

        self.bag: Bag
        self.board: Board
        self.hands: list[Hand]

        self.reset()

    def reset(self) -> None:
        self.bag = Bag(shuffle=True, **self.config)
        self.board = Board(**self.config)
        self.hands = [Hand(game_bag=self.bag, player=player, **self.config) for player in self.players]
