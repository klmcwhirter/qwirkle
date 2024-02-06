'''qwirkle gui package'''

from typing import Callable

from .pygamece_adapter import pygame_ce_display_adapter

# point of extension later - at that point dynamically determine the DisplayAdapter to use
type DisplayAdapter = Callable[[], None]

display_adapter: DisplayAdapter = pygame_ce_display_adapter

__all__ = [
    'display_adapter'
]
