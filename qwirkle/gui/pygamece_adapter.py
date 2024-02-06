'''qwirkle pygame-ce adapter'''

import pygame


def pygame_ce_display_adapter() -> None:
    print(f'pygame-ce Version: {pygame.version.vernum}')
