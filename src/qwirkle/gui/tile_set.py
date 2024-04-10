"""Qwirkle Tile image set"""


import io

import pygame as pg

from qwirkle.gui.tiles import _tiles_bytes
from qwirkle.logic.color import colors
from qwirkle.logic.shape import shapes

tile_images: dict[str, pg.Surface] = {}

TILE_SIDE = 32


def init():
    with io.BytesIO(initial_bytes=_tiles_bytes) as tiles:
        img_surf = pg.image.load(tiles)

        for row, s in enumerate(shapes):
            for col, c in enumerate(colors):
                x = col * TILE_SIDE
                y = row * TILE_SIDE

                tile_images[f'{c.code}{s.code}'] = img_surf.subsurface([x, y, TILE_SIDE, TILE_SIDE])
