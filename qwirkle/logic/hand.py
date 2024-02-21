"""Qwirkle Hand"""


from qwirkle.logic.bag import Bag
from qwirkle.logic.tile import Tile


class Hand(list[Tile]):
    def __init__(self, game_bag: Bag, **kwargs) -> None:
        super().__init__()

        self.config = kwargs  # also used in adapter
        self.num_tiles = kwargs['hand']['tiles']

        self.bag = game_bag

        self.reset()

    def reset(self) -> None:
        for _ in range(self.num_tiles):
            self.append(self.bag.pop())
