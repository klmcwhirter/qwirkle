'''qwirkle gui package'''

from typing import Callable

from .pygame_ce.display_adapter import pygame_ce_display_adapter

# point of extension later - at that point dynamically determine the DisplayAdapter to use
# type DisplayAdapter = Callable[[], None]  # TODO Not supported by mypy yet https://github.com/python/mypy/issues/15238

# display_adapter: DisplayAdapter = pygame_ce_display_adapter

display_adapter: Callable[[], None] = pygame_ce_display_adapter

__all__ = [
    'display_adapter'
]
