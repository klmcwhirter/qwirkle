
from typing import Callable

from qwirkle.gui.game_adapter import pygame_ce_game_adapter

# point of extension later - at that point dynamically determine the DisplayAdapter to use
display_adapter: Callable[[], None] = pygame_ce_game_adapter

# type DisplayAdapter = Callable[[], None]  # TODO Not supported by mypy yet https://github.com/python/mypy/issues/15238
# display_adapter: DisplayAdapter = pygame_ce_game_adapter
