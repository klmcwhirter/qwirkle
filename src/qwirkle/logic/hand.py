"""Qwirkle Hand"""


from qwirkle.logic.bag import Bag
from qwirkle.logic.player import Player
from qwirkle.logic.tile import Tile


class Hand(list[Tile]):
    def __init__(self, game_bag: Bag, player: Player = Player('', 99), **kwargs) -> None:
        super().__init__()

        self.config = kwargs  # also used in adapter
        self.num_tiles = kwargs['hand']['tiles']

        self.player = player

        self.bag = game_bag

        self.reset()

    def __str__(self) -> str:
        return f'{self.player.name}: {' | '.join([str(tile) for tile in self])}'

    def reset(self) -> None:
        for _ in range(self.num_tiles):
            self.append(self.bag.pop())
