'''Display Adapter for the Hand concept for pygame-ce'''


import pygame as pg

from qwirkle.logic.component_display_adapter import ComponentDisplayAdapter
from qwirkle.logic.hand import Hand


class HandDisplayAdapter:
    def __init__(self, **kwargs) -> None:
        self.config = kwargs

        hand_config = self.config['hand']
        self.font = pg.font.Font(None, hand_config['font-size'])
        self.font_color = hand_config['font-color']

        self.padx = hand_config['padx']
        self.pady = hand_config['pady']

        self.screen_width = self.config['screen']['width']
        self.screen_height = self.config['screen']['height']

    def draw(self, screen: pg.Surface, **kwargs) -> None:
        hand: Hand = kwargs['hand']
        x_offset = 0
        for tile in hand:
            surf = self.font.render(f'Tile({tile}), ', True, self.font_color)
            rect = surf.get_rect()

            rect.bottomleft = (self.screen_width // 2 + x_offset, self.screen_height - self.pady)
            screen.blit(surf, rect)

            x_offset += rect.width


def pygame_ce_hand_adapter(**kwargs) -> ComponentDisplayAdapter:
    return HandDisplayAdapter(**kwargs)
