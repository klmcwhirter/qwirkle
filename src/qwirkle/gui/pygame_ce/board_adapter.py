'''Display Adapter for the Board concept for pygame-ce'''


import logging

import pygame as pg

from qwirkle.gui.pygame_ce.tile_adapter import pygame_ce_tile_adapter
from qwirkle.logic.board import Board
from qwirkle.logic.component_display_adapter import ComponentDisplayAdapter


class BoardDisplayAdapter:
    def __init__(self, board: Board) -> None:
        self.board = board
        logging.debug(f'Board side len={len(self.board)}')

        self.tile_adapter = pygame_ce_tile_adapter(**self.board.config)

        board_config = self.board.config['board']
        self.font = pg.font.Font(None, board_config['font-size'])
        self.font_color = board_config['font-color']

        self.padx = board_config['padx']
        self.pady = board_config['pady']

        self.screen_width = self.board.config['screen']['width']
        self.screen_height = self.board.config['screen']['height']

    def draw_status(self, screen: pg.Surface, **_kwargs) -> None:
        surf = self.font.render(f'Board side len={len(self.board)}', True, self.font_color)
        rect = surf.get_rect()

        rect.bottomleft = (self.padx, self.screen_height - self.pady)
        screen.blit(surf, rect)

    def draw_tiles(self, screen: pg.Surface, **_kwargs) -> None:
        for row in self.board:
            for tile in row:
                self.tile_adapter.draw(screen=screen, tile=tile)

    def draw(self, /, **kwargs) -> None:
        screen: pg.Surface = kwargs['screen']
        # self.draw_tiles(screen=screen)
        self.draw_status(screen=screen)


def pygame_ce_board_adapter(board: Board) -> ComponentDisplayAdapter:
    return BoardDisplayAdapter(board=board)
