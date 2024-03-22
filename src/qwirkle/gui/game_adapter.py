"""qwirkle pygame-ce adapter"""

import logging
from pprint import pformat
from typing import Any

import pygame as pg

from qwirkle.gui.bag_adapter import pygame_ce_bag_adapter
from qwirkle.gui.board_adapter import pygame_ce_board_adapter
from qwirkle.gui.hand_adapter import pygame_ce_hand_adapter
from qwirkle.logic.component_display_adapter import ComponentDisplayAdapter
from qwirkle.logic.game import Game

# initialize pygame
pg.init()

if not pg.font:
    logging.warn('Pygame: Fonts not available')
if not pg.mixer:
    logging.warn('Pygame: Sound not available')


class GameDisplayAdapter:
    def __init__(self, **kwargs) -> None:
        self.config = kwargs
        logging.debug(pformat(self.config, sort_dicts=False))

        self.bag_adapter: ComponentDisplayAdapter
        self.board_adapter: ComponentDisplayAdapter
        self.hand_adapter: ComponentDisplayAdapter

        self.game = Game(**self.config)

        screen_config: dict[str, Any] = {k: v for k, v in self.config['screen'].items()}
        self.width: int = int(screen_config['width'])
        self.height: int = int(screen_config['height'])
        self.bg_color: str = str(screen_config['bg-color'])

    def get_window_title(self, addon: str | None = None) -> str:
        return f'{self.config["title"]}' if addon is None else f'{self.config["title"]} - {addon}'

    def draw(self):
        # fill the screen with a color to wipe away anything from last frame
        self.screen.fill(self.bg_color)
        self.bag_adapter.draw(screen=self.screen)
        self.board_adapter.draw(screen=self.screen)
        self.draw_hands(screen=self.screen)

    def draw_hands(self, /, screen: pg.Surface, **_kwargs) -> None:
        for player in self.game.players:
            self.hand_adapter.draw(screen=screen, player=player)

    def reset(self) -> None:
        self.game.reset()
        self.bag_adapter = pygame_ce_bag_adapter(self.game.bag)
        self.board_adapter = pygame_ce_board_adapter(self.game.board)
        self.hand_adapter = pygame_ce_hand_adapter(**self.config)
        logging.debug(pformat(self.config, sort_dicts=False))

    def run(self) -> None:
        try:
            pg.display.set_caption(self.get_window_title())
            self.screen = pg.display.set_mode((self.width, self.height))

            self.reset()
            clock = pg.time.Clock()

            running = True
            while running:
                # poll for events
                # pg.QUIT event means the user clicked X to close your window
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        self.game.exit_game()
                        running = False
                    elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                        self.game.exit_game()
                        running = False

                    if running:
                        # pos = None

                        if event.type == pg.MOUSEBUTTONUP:
                            # pos = event.pos
                            self.game.current_player_index = 1 - self.game.current_player_index

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


def pygame_ce_game_adapter(**kwargs) -> None:
    logging.debug('Starting game')
    try:
        game = GameDisplayAdapter(**kwargs)
        game.run()
    finally:
        logging.debug('Exiting game')
