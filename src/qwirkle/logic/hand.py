"""Qwirkle Hand"""


from dataclasses import dataclass

from qwirkle.logic.bag import Bag
from qwirkle.logic.player import Player
from qwirkle.logic.tile import Tile


@dataclass
class HandExchange:
    player: Player
    old_tiles: list[Tile]
    new_tiles: list[Tile]


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

    def exchange_tiles(self, old_tiles: list[Tile]) -> HandExchange:
        new_tiles: list[Tile] = [self.bag.pop() for _ in old_tiles]
        self.bag.extend(old_tiles)
        self.extend(new_tiles)

        exchange = HandExchange(player=self.player, old_tiles=old_tiles, new_tiles=new_tiles)
        return exchange

    def reset(self) -> None:
        for _ in range(self.num_tiles):
            self.append(self.bag.pop())
