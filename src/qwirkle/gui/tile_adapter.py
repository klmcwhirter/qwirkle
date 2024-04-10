"""Display Adapter for the Tile concept for pygame-ce"""


import pygame as pg

from qwirkle.gui import tile_set
from qwirkle.logic.component_display_adapter import ComponentDisplayAdapter
from qwirkle.logic.tile import Tile


class TileDisplayAdapter:
    def __init__(self, **kwargs) -> None:
        self.config = kwargs

        tile_config = self.config['tile']
        self.font = pg.font.SysFont(
            name=tile_config['font'],
            size=tile_config['font-size'],
            bold=False
        )
        self.font_color = tile_config['font-color']
        self.active_color = tile_config['active-color']
        self.inactive_color = tile_config['inactive-color']

        self.padx = tile_config['padx']
        self.pady = tile_config['pady']

        tile_set.init()

    def draw(self, /, **kwargs) -> pg.Surface:
        tile: Tile = kwargs['tile']
        active: bool = kwargs['active']

        bg_color = self.active_color if active else self.inactive_color
        # surf = self.font.render(text=f' {tile} ', antialias=True, color=self.font_color, bgcolor=bg_color)

        # surf = tile_set.tile_images[str(tile)]

        surf = pg.Surface([
            tile_set.TILE_SIDE + (self.padx * 2),
            tile_set.TILE_SIDE + (self.pady * 2)
        ])
        # surf.set_colorkey('black')
        surf.fill(bg_color)
        surf.blit(source=tile_set.tile_images[str(tile)], dest=[self.padx, self.pady])

        return surf


def pygame_ce_tile_adapter(**kwargs) -> ComponentDisplayAdapter:
    return TileDisplayAdapter(**kwargs)
