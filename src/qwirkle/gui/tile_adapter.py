"""Display Adapter for the Tile concept for pygame-ce"""


import logging

import pygame as pg

from qwirkle.logic.component_display_adapter import ComponentDisplayAdapter
from qwirkle.logic.player import Player
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
        self.active_width = tile_config['active-width']

        self.padx = tile_config['padx']
        self.pady = tile_config['pady']

        self.screen_width = self.config['screen']['width']
        self.screen_height = self.config['screen']['height']

    def draw(self, /, **kwargs) -> pg.Rect:
        tile: Tile = kwargs['tile']
        screen: pg.Surface = kwargs['screen']
        player: Player = kwargs['player']
        x: int = kwargs['x']
        y: int = kwargs['y']

        bg_color = self.active_color if player.active else None
        surf = self.font.render(text=str(tile), antialias=False, color=self.font_color, bgcolor=bg_color)
        rect = surf.get_rect()

        x += self.padx
        y += self.pady
        rect.topleft = (x, y)
        logging.debug(f'tile after setting {rect.topleft=}, {rect.bottomleft}, {x=}, {y=}')

        screen.blit(surf, rect)

        return rect


def pygame_ce_tile_adapter(**kwargs) -> ComponentDisplayAdapter:
    return TileDisplayAdapter(**kwargs)
