"""pygbag entrypoint"""

import logging

from qwirkle.config import settings
from qwirkle.gui.game_adapter import GameDisplayAdapter


async def main() -> None:
    logging.debug('Starting game')
    try:
        game = GameDisplayAdapter(**settings)
        await game.run()
    finally:
        logging.debug('Exiting game')
