"""Display Adapter for the Hand concept for pygame-ce"""


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

    def draw(self, /, **kwargs) -> None:
        hand: Hand = kwargs['hand']
        screen: pg.Surface = kwargs['screen']
        surf = self.font.render(str(hand), True, self.font_color)
        rect = surf.get_rect()

        x_offset = self.padx - (rect.width * hand.player.number)
        rect.bottomleft = ((self.screen_width // 3) - x_offset, self.screen_height - self.pady)
        screen.blit(surf, rect)


def pygame_ce_hand_adapter(**kwargs) -> ComponentDisplayAdapter:
    return HandDisplayAdapter(**kwargs)
