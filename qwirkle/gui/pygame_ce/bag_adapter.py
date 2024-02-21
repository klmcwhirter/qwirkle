'''Display Adapter for the Bag concept for pygame-ce'''


import logging

import pygame as pg

from qwirkle.logic.bag import Bag
from qwirkle.logic.component_display_adapter import ComponentDisplayAdapter


class BagDisplayAdapter:
    def __init__(self, bag: Bag) -> None:
        self.bag = bag
        logging.debug(f'Bag len={len(self.bag)}')

        bag_config = self.bag.config['bag']
        self.font = pg.font.Font(None, bag_config['font-size'])
        self.font_color = bag_config['font-color']

        self.padx = bag_config['padx']
        self.pady = bag_config['pady']

        self.screen_width = self.bag.config['screen']['width']
        self.screen_height = self.bag.config['screen']['height']

    def draw(self, screen: pg.Surface, **_kwargs) -> None:
        surf = self.font.render(f'Bag len={len(self.bag)}', True, self.font_color)
        rect = surf.get_rect()

        rect.bottomright = (self.screen_width - self.padx, self.screen_height - self.pady)
        screen.blit(surf, rect)


def pygame_ce_bag_adapter(bag: Bag) -> ComponentDisplayAdapter:
    return BagDisplayAdapter(bag=bag)
