"""Display Adapter for the Hand concept for pygame-ce"""


import operator
from functools import reduce

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
        self.inactive_color = hand_config['inactive-color']
        self.border_width = hand_config['border-width']

        self.padx = hand_config['padx']
        self.pady = hand_config['pady']

        self.tile_adapter = pygame_ce_tile_adapter(**kwargs)

    def draw_hand(self, hand: Hand, player: Player) -> tuple[pg.Surface, pg.rect.Rect]:
        bg_color = self.active_color if player.active else self.inactive_color
        name_surf = self.font.render(text=f' {player.name}: ', antialias=True, color=self.font_color, bgcolor=bg_color)
        name_surf_rect = name_surf.get_rect()

        # draw each tile
        tile_surfs: list[pg.Surface] = [self.tile_adapter.draw(tile=tile, active=player.active) for tile in hand]

        # find sum of tile widths and max height
        total_width = reduce(operator.add, map(lambda s: s.get_width(), tile_surfs), 0) + name_surf_rect.width
        max_height = reduce(max, map(lambda s: s.get_height(), tile_surfs), 0)

        # Create Surface large enough to diplay hand name and all tiles
        hand_surf = pg.Surface((total_width, max_height))
        hand_rect = hand_surf.get_rect()
        hand_surf.fill(bg_color)

        x = 0
        y = 0

        # blit hand name
        hand_surf.blit(name_surf, (x, name_surf_rect.height // 3))
        x += name_surf_rect.width

        # blit each tile
        for tile_surf in tile_surfs:
            hand_surf.blit(tile_surf, (x, y))
            x += tile_surf.get_width()

        # draw a wider border
        hand_rect.width += (self.border_width * 2)
        hand_rect.height += (self.border_width * 2)
        hand_rect.topleft = (0, 0)

        pg.draw.rect(surface=hand_surf, color=bg_color, rect=hand_rect, width=self.border_width)

        return (hand_surf, hand_rect)

    def draw(self, /, **kwargs) -> None:
        screen: pg.Surface = kwargs['screen']
        player: Player = kwargs['player']
        hand: Hand | None = player.hand

        if hand is not None:
            hand_surf, hand_rect = self.draw_hand(hand, player)

            x_offset = hand_rect.width * player.number  # display side by side

            x = (screen.get_width() // 3) + x_offset
            y = screen.get_height() - hand_rect.height - self.pady

            screen_rect = pg.rect.Rect(x, y, hand_rect.width, hand_rect.height)
            screen.blit(hand_surf, screen_rect)


def pygame_ce_hand_adapter(**kwargs) -> ComponentDisplayAdapter:
    return HandDisplayAdapter(**kwargs)
