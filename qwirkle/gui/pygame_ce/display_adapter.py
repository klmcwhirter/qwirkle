"""qwirkle pygame-ce adapter"""

import logging
from pprint import pformat

import pygame as pg

from qwirkle.gui.pygame_ce.bag_adapter import pygame_ce_bag_adapter
from qwirkle.gui.pygame_ce.board_adapter import pygame_ce_board_adapter
from qwirkle.gui.pygame_ce.hand_adapter import pygame_ce_hand_adapter
from qwirkle.logic.board import Board
from qwirkle.logic.models import Bag, Hand

# initialize pygame
pg.init()

if not pg.font:
    logging.warn('Pygame: Fonts not available')
if not pg.mixer:
    logging.warn('Pygame: Sound not available')


class Game:
    def __init__(self) -> None:
        from ...config import settings

        self.config = settings
        logging.debug(pformat(self.config, sort_dicts=False))

        self.width = self.config['screen']['width']
        self.height = self.config['screen']['height']

        self._set_window_title()
        self.screen = pg.display.set_mode((self.width, self.height))

    def _set_window_title(self, addon: str | None = None) -> None:
        msg = self.config['title'] if addon is None else f'{self.config['title']} - {addon}'
        pg.display.set_caption(msg)

    def draw(self):
        # fill the screen with a color to wipe away anything from last frame
        self.screen.fill(self.config['screen']['bg-color'])
        self.bag_adapter.draw(screen=self.screen)
        self.board_adapter.draw(screen=self.screen)
        self.draw_hands(screen=self.screen)

    def draw_hands(self, screen: pg.Surface, **_kwargs) -> None:
        for hand in self.hands:
            self.hand_adapter.draw(screen, hand=hand)

    def reset(self) -> None:
        self.bag = Bag(**self.config)
        self.bag_adapter = pygame_ce_bag_adapter(self.bag)

        self.board = Board(**self.config)
        self.board_adapter = pygame_ce_board_adapter(self.board)

        self.hands: list[Hand] = [Hand(game_bag=self.bag, **self.config)]
        self.hand_adapter = pygame_ce_hand_adapter(**self.config)

    def run(self) -> None:
        try:
            self.reset()
            clock = pg.time.Clock()

            running = True
            while running:
                # poll for events
                # pg.QUIT event means the user clicked X to close your window
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        running = False
                    elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                        running = False

                    if False:
                        ...

                        # pos = None

                        # if event.type == pg.MOUSEBUTTONUP:
                        #     pos = self._board.mouse_to_pos(event.pos)
                        # elif event.type == pg.KEYDOWN and event.key in range(pg.K_0, pg.K_9 + 1):
                        #     pos = event.key - pg.K_0

                    else:  # have winner
                        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                            self.reset()

                # RENDER YOUR GAME HERE
                self.draw()

                # flip() the display to put your work on screen
                pg.display.flip()

                clock.tick(60)  # limits FPS to 60
        finally:
            pg.quit()


def pygame_ce_display_adapter() -> None:
    logging.debug('Starting game')
    try:
        game = Game()
        game.run()
    finally:
        logging.debug('Exiting game')
