"""refactor the tile set image"""

import io
from itertools import islice

import pygame as pg

# from https://github.com/stijn-geerits/Qwirkle
TILES_ORIG = './etc/tiles_orig.png'
TILES_NEW = './src/qwirkle/gui/tiles.py'

TILE_SIDE = 32

ORIG_COLS = 8
ORIG_ROWS = 5

NEW_COLS = 6
NEW_ROWS = 6


def orig_tiles():
    img_surf = pg.image.load(TILES_ORIG)
    for row in range(ORIG_ROWS):
        for col in range(ORIG_COLS):
            x = col * TILE_SIDE
            y = row * TILE_SIDE
            sub_surf = img_surf.subsurface([x, y, TILE_SIDE, TILE_SIDE])
            yield sub_surf


class Outliner:
    """From https://youtu.be/xPKuhqt8Pcs"""

    def __init__(self) -> None:
        self.convolution_mask = pg.mask.Mask((3, 3), fill=True)
        self.convolution_mask.set_at((0, 0), value=0)
        self.convolution_mask.set_at((2, 0), value=0)
        self.convolution_mask.set_at((0, 2), value=0)
        self.convolution_mask.set_at((2, 2), value=0)

    def outline_surface(self, surface: pg.Surface, color='darkgray', outline_only=False):
        colorkey = surface.get_colorkey()
        mask = pg.mask.from_surface(surface)
        surface_outline = mask.convolve(self.convolution_mask).to_surface(setcolor=color, unsetcolor=colorkey)
        surface_outline.set_colorkey(colorkey)

        if outline_only:
            mask_surface = mask.to_surface(setcolor=colorkey, unsetcolor=color)
            mask_surface.set_colorkey(colorkey)
            surface_outline.blit(mask_surface, (1, 1))
        else:
            surface_outline.blit(surface, (1, 1))

        return surface_outline


def main() -> None:
    outliner = Outliner()

    pg.init()
    screen = pg.display.set_mode([NEW_COLS * TILE_SIDE, NEW_ROWS * TILE_SIDE])
    new_surf = pg.Surface([NEW_COLS * TILE_SIDE, NEW_ROWS * TILE_SIDE], pg.SRCALPHA)
    new_surf.set_alpha(0)

    for tile_num, tile_surf in enumerate(islice(orig_tiles(), 1, NEW_ROWS * NEW_COLS + 1)):
        color = tile_surf.get_at((0, 0))
        tile_surf.set_colorkey(color)  # set alpha color

        new_col = tile_num % NEW_COLS
        new_row = tile_num // NEW_COLS

        x, y = new_col * TILE_SIDE, new_row * TILE_SIDE

        # outlined_surf = outliner.outline_surface(tile_surf, color='white', outline_only=True)

        outlined_surf = outliner.outline_surface(tile_surf)
        new_surf.blit(outlined_surf, [x, y])

        # new_surf.blit(tile_surf, [x, y])

    tnb: io.BytesIO = io.BytesIO()
    pg.image.save(new_surf, tnb, namehint='png')  # TILES_NEW)
    tnb_bytes: bytes = tnb.getvalue()

    print(f'{len(tnb_bytes)=}')
    content = f'''
# bytes of PNG image used in tile_set.py
_tiles_bytes = {tnb_bytes}
'''
    with open(TILES_NEW, 'w') as f:
        f.write(content)


if __name__ == '__main__':
    main()
