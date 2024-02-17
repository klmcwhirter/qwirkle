'''Display Adapter for the Board concept for pygame-ce'''


import logging

import pygame as pg

from qwirkle.gui.component_display_adapter import ComponentDisplayAdapter
from qwirkle.logic.board import Board


class BoardDisplayAdapter:
    def __init__(self, board: Board) -> None:
        self.board = board
        logging.debug(f'Board side len={len(self.board)}')

        board_config = self.board.config['board']
        self.font = pg.font.Font(None, board_config['font_size'])
        self.font_color = board_config['font_color']

        self.padx = board_config['padx']
        self.pady = board_config['pady']

        self.screen_width = self.board.config['screen']['width']
        self.screen_height = self.board.config['screen']['height']

    def draw(self, screen: pg.Surface) -> None:
        surf = self.font.render(f'Board side len={len(self.board)}', True, self.font_color)
        rect = surf.get_rect()

        rect.bottomleft = (self.padx, self.screen_height - self.pady)
        screen.blit(surf, rect)


def pygame_ce_board_adapter(board: Board) -> ComponentDisplayAdapter:
    return BoardDisplayAdapter(board=board)
