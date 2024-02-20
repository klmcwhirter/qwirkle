'''Display Adapter for the Tile concept for pygame-ce'''


import logging
from pprint import pformat

import pygame as pg

from qwirkle.gui.component_display_adapter import ComponentDisplayAdapter
from qwirkle.logic.models import Tile


class TileDisplayAdapter:
    def __init__(self, **kwargs) -> None:
        self.config = kwargs

        tile_config = self.config['tile']
        self.font = pg.font.Font(None, tile_config['font-size'])
        self.font_color = tile_config['font-color']

        self.padx = tile_config['padx']
        self.pady = tile_config['pady']

        self.screen_width = self.config['screen']['width']
        self.screen_height = self.config['screen']['height']

    def draw(self, screen: pg.Surface, **kwargs) -> None:
        tile: Tile = kwargs['tile']
        surf = self.font.render(f'Tile({tile})', True, self.font_color)
        rect = surf.get_rect()

        rect.bottomleft = (self.screen_width // 2, self.screen_height - self.pady)
        screen.blit(surf, rect)


def pygame_ce_tile_adapter(**kwargs) -> ComponentDisplayAdapter:
    return TileDisplayAdapter(**kwargs)
