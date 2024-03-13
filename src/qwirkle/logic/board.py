"""Qwirkle board"""

from qwirkle.logic import BoardExpansionStrategy, Direction, _BoardBase
from qwirkle.logic.tile import Tile


class Board(_BoardBase):
    """A qwirkle game board that grows dynamically as pieces are placed"""

    def __init__(self, **kwargs) -> None:
        # start as empty list - not None
        super().__init__()

        self.config = kwargs  # also used in adapter
        board_config = self.config['board']

        self.expansion: BoardExpansionStrategy = board_config['expansion']
        self.segment_size: int = board_config['segment-size']

        initial_segments = board_config['initial-segments']
        self._initialize(initial_segments)

    def __str__(self) -> str:
        return '\n'.join(
            [
                ', '.join(
                    [
                        f'{tile!s:>2}' if tile is not None else '__'
                        for tile in row
                    ])
                for row in self
            ])

    def _initialize(self, segments: int) -> None:
        self.expansion.grow_vertical(self, segments, Direction.SOUTH)
        self.expansion.grow_horizontal(self, segments - 1, Direction.EAST)  # already 1 wide

    def expand_board(self, x: int, y: int, dir_to_expand: Direction) -> tuple[int, int]:
        dir_to_adjust: Direction | None = dir_to_expand
        if dir_to_adjust in [Direction.NORTH, Direction.SOUTH]:
            self.expansion.grow_vertical(self, 1, dir_to_adjust)
            # Do not adjust if SOUTH, but use SOUTH adjustment if NORTH
            dir_to_adjust = None if dir_to_adjust == Direction.SOUTH else Direction.SOUTH
        elif dir_to_adjust in [Direction.EAST, Direction.WEST]:
            self.expansion.grow_horizontal(self, 1, dir_to_adjust)
            # Do not adjust if EAST, but use EAST adjustment if WEST
            dir_to_adjust = None if dir_to_adjust == Direction.EAST else Direction.EAST

        return self.expansion.adjust(x, y, dir_to_adjust, self.segment_size)

    def available(self, tiles: list[Tile], x: int, y: int, dir: Direction) -> bool:
        rc = True
        for _ in tiles:
            rc = self[y][x] is None
            if rc:
                x, y = self.expansion.adjust(x, y, dir)
            else:
                break
        return rc

    def contains_line_for(self, adjacent: Tile | None, tiles: list[Tile]) -> bool:
        return adjacent is not None and \
            (
                all(t.color.code == adjacent.color.code for t in tiles) or
                all(t.shape.code == adjacent.shape.code for t in tiles)
            ) and \
            str(adjacent) not in [str(tile) for tile in tiles]  # cannot have dups in a line

    def has_adjacent(self, tiles: list[Tile], x: int, y: int, dir: Direction) -> bool:
        def in_bounds(point: tuple[int, int]) -> bool:
            tx, ty = point
            return tx >= 0 and tx < len(self[y]) and ty >= 0 and ty < len(self)

        rc = len(self.placed_tiles()) == 0  # allow first tiles being placed

        if not rc:
            rc = True
            point = self.expansion.adjust(x, y, dir)
            for tile in tiles:
                if in_bounds(point):
                    # available and color or shapes match the adjacent
                    rc = not self.available([tile], point[0], point[1], dir) and \
                        self.contains_line_for(self[point[1]][point[0]], tiles)

                    if rc:
                        point = self.expansion.adjust(point[0], point[1], dir)
                    else:
                        break
                else:
                    rc = True  # will need to expand
                    break

        return rc

    def place_tiles(self, tiles: list[Tile], x: int, y: int, dir: Direction) -> int:
        # expand if need to ...
        if self.expansion.need_to_expand(self, len(tiles), x, y, dir):
            x, y = self.expand_board(x, y, dir)

        # make sure spot is available
        can_place = self.available(tiles, x, y, dir)
        if not can_place:
            raise ValueError(f'({x}, {y}) is occupied')

        can_place = self.has_adjacent(tiles, x, y, dir)
        if not can_place:
            raise ValueError(f'({x}, {y}) is not adjacent to any tile')

        # TODO: is this a valid placement? lines should be no longer than 6 tiles
        can_place, error = can_place, None

        if can_place:
            for idx, tile in enumerate(tiles):
                if idx != 0:
                    x, y = self.expansion.adjust(x, y, dir)

                self[y][x] = tile
        else:
            raise ValueError(f'Not a valid placement: {error}')

        # TODO: calculate score
        score = 0

        return score

    def placed_tiles(self) -> list[tuple[int, int, Tile]]:
        rc = [
            (x, y, tile)
            for y, row in enumerate(self)
            for x, tile in enumerate(row)
            if tile is not None
        ]
        return rc
