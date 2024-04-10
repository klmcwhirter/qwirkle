"""qwirkle

Usage:
    qwirkle
"""


import asyncio

from qwirkle.config import settings
from qwirkle.gui.game_adapter import pygame_ce_game_adapter
from qwirkle.utils.logging import logging_config

logging_config(**settings)
asyncio.run(pygame_ce_game_adapter(**settings))
