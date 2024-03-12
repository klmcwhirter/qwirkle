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

    def expand_board(self, x: int, y: int, dir: Direction | None) -> tuple[int, int]:
        if dir in [Direction.NORTH, Direction.SOUTH]:
            self.expansion.grow_vertical(self, 1, dir)
            dir = None if dir == Direction.SOUTH else Direction.SOUTH
        elif dir in [Direction.EAST, Direction.WEST]:
            self.expansion.grow_horizontal(self, 1, dir)
            dir = None if dir == Direction.EAST else Direction.EAST

        return self.expansion.adjust(x, y, dir, self.segment_size)

    def available(self, tiles: list[Tile], x: int, y: int, dir: Direction) -> bool:
        rc = True
        for t, tile in enumerate(tiles):
            rc = self[y][x] is None
            if rc:
                x, y = self.expansion.adjust(x, y, dir)
            else:
                break
        return rc

    def has_adjacent(self, tiles: list[Tile], x: int, y: int, dir: Direction) -> bool:
        def in_bounds(point: tuple[int, int]) -> bool:
            tx, ty = point
            return tx >= 0 and tx < len(self[y]) and ty >= 0 and ty < len(self)

        rc = len(self.placed_tiles()) == 0  # allow first tiles being placed

        if not rc:
            rc = True
            for _t, _tile in enumerate(tiles):
                points = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
                points = [p for p in filter(in_bounds, points)]
                rc = any(self[test_y][test_x] is None for test_x, test_y in points)
                if rc:
                    x, y = self.expansion.adjust(x, y, dir)
                else:
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

        if can_place:
            # TODO: is this a valid placement?
            can_place = self.has_adjacent(tiles, x, y, dir)
            if not can_place:
                raise ValueError(f'({x}, {y}) is not adjacent to any tile')
            can_place, error = (can_place, None)

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
