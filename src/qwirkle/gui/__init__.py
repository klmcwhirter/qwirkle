"""qwirkle gui package"""

from qwirkle.gui.pygame_ce import display_adapter

# point of extension later - at that point dynamically determine the DisplayAdapter to use

# type DisplayAdapter = Callable[[], None]  # TODO Not supported by mypy yet https://github.com/python/mypy/issues/15238
# display_adapter: DisplayAdapter = pygame_ce_game_adapter


__all__ = [
    'display_adapter'
]
