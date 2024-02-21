"""Qwirkle Bag"""


import random

from qwirkle.logic.color import Color, colors
from qwirkle.logic.shape import Shape, shapes
from qwirkle.logic.tile import Tile


class Bag(list[Tile]):
    def __init__(self, shuffle: bool = True, **kwargs) -> None:
        super().__init__()
        self.tile_copies = 3  # default based on standard game rules
        self.config = kwargs  # also used in adapter

        if 'bag' in self.config and 'tile-copies' in self.config['bag']:
            self.tile_copies = self.config['bag']['tile-copies']

        # allow for overriding default colors in config
        if 'colors' in self.config:
            global colors

            if len(self.config['colors']) != len(colors):
                raise ValueError(f'# of colors in config ({len(self.config['colors'])}) must be {len(colors)}')

            colors = [Color(**c) for c in self.config['colors']]

        # allow for overriding default shapes in config
        if 'shapes' in self.config:
            if len(self.config['shapes']) != len(shapes):
                raise ValueError(f'# of shapes in config ({len(self.config['shapes'])}) must be {len(shapes)}')

            shapes = [Shape(**s) for s in self.config['shapes']]

        self.reset()
        if shuffle:
            self.shuffle()

    def reset(self) -> None:
        for s in shapes:
            for c in colors:
                for _ in range(self.tile_copies):
                    self.append(Tile(color=c, shape=s))

    def shuffle(self) -> None:
        random.shuffle(self)
