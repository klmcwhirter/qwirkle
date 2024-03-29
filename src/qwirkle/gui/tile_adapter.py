"""Display Adapter for the Tile concept for pygame-ce"""


import pygame as pg

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

        self.padx = tile_config['padx']
        self.pady = tile_config['pady']

    def draw(self, /, **kwargs) -> pg.Surface:
        tile: Tile = kwargs['tile']
        active: bool = kwargs['active']

        bg_color = self.active_color if active else None
        surf = self.font.render(text=f' {tile} ', antialias=True, color=self.font_color, bgcolor=bg_color)

        return surf


def pygame_ce_tile_adapter(**kwargs) -> ComponentDisplayAdapter:
    return TileDisplayAdapter(**kwargs)
