"""Qwirkle Hand"""


from dataclasses import dataclass

from qwirkle.logic.bag import Bag
from qwirkle.logic.tile import Tile


@dataclass
class HandExchange:
    player_name: str
    old_tiles: list[Tile]
    new_tiles: list[Tile]


def tile_list2str(tiles: list[Tile]) -> str:
    return ' | '.join([str(tile) for tile in tiles])


@dataclass
class Hand(list[Tile]):
    def __init__(self, game_bag: Bag, player_name: str = '', **kwargs) -> None:
        super().__init__()

        self.config = kwargs  # also used in adapter
        self.num_tiles = kwargs['hand']['tiles']

        self.player_name = player_name

        self.bag = game_bag

        self.reset()

    def __repr__(self) -> str:
        return f'Hand(player_name={self.player_name}, tiles={tile_list2str(self)}'

    def __str__(self) -> str:
        return f'{self.player_name}: {tile_list2str(self)}'

    def exchange_tiles(self, old_tiles: list[Tile]) -> HandExchange:
        new_tiles: list[Tile] = [self.bag.pop() for _ in old_tiles]
        self.bag.extend(old_tiles)
        self.extend(new_tiles)

        exchange = HandExchange(player_name=self.player_name, old_tiles=old_tiles, new_tiles=new_tiles)
        return exchange

    def reset(self) -> None:
        for _ in range(self.num_tiles):
            self.append(self.bag.pop())
