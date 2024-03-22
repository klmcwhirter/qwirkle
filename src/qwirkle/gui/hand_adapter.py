"""Display Adapter for the Hand concept for pygame-ce"""


import logging

import pygame as pg

from qwirkle.gui.tile_adapter import pygame_ce_tile_adapter
from qwirkle.logic.component_display_adapter import ComponentDisplayAdapter
from qwirkle.logic.hand import Hand
from qwirkle.logic.player import Player


class HandDisplayAdapter:
    def __init__(self, **kwargs) -> None:
        self.config = kwargs

        hand_config = self.config['hand']
        self.font = pg.font.SysFont(
            name=hand_config['font'],
            size=hand_config['font-size'],
            bold=False
        )
        self.font_color = hand_config['font-color']
        self.active_color = hand_config['active-color']
        self.active_width = hand_config['active-width']

        self.padx = hand_config['padx']
        self.pady = hand_config['pady']

        self.screen_width = self.config['screen']['width']
        self.screen_height = self.config['screen']['height']

        self.tile_adapter = pygame_ce_tile_adapter(**kwargs)

    def draw(self, /, **kwargs) -> None:
        screen: pg.Surface = kwargs['screen']
        player: Player = kwargs['player']
        hand: Hand | None = player.hand

        if hand is not None:
            bg_color = self.active_color if player.active else None
            surf = self.font.render(text=f'{player.name}: ', antialias=False, color=self.font_color, bgcolor=bg_color)

            est_tile_width = 44
            x_offset = (est_tile_width + self.active_width * 2) * hand.num_tiles * player.number
            x = (self.screen_width // 3) + x_offset + (self.padx * player.number * 2)

            y = self.screen_height - est_tile_width - self.pady

            for tile in hand:
                logging.debug(f'hand - {player.name=} {x=}, {y=}')
                rect = self.tile_adapter.draw(
                    screen=surf, player=player, tile=tile,
                    x=x,
                    y=y)
                x = x + rect.width

            surf_rect = surf.get_rect()

            if player.active:
                # draw a wider border
                surf_rect.width += (self.active_width * 2)
                surf_rect.height += (self.active_width * 2)
                surf_rect.topleft = (x - self.active_width, y - self.active_width)

                pg.draw.rect(surface=surf, color=self.active_color, rect=surf_rect, width=self.active_width)

                # # reset for next tile
                # rect.topleft = (x, y)
            surf_rect = surf.get_rect()

            screen.blit(surf, surf_rect)


def pygame_ce_hand_adapter(**kwargs) -> ComponentDisplayAdapter:
    return HandDisplayAdapter(**kwargs)
