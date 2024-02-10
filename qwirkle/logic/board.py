"""Qwirkle board"""


from qwirkle.logic import BoardBase, Direction, PlacementStrategy
from qwirkle.logic.models import Tile


def create_row_part(width: int) -> list[None]:
    return [None for _ in range(width)]


def create_segment(width: int, height: int) -> list[list[None]]:
    return [create_row_part(width) for _ in range(height)]


class Board(BoardBase):
    """A qwirkle game board that grows dynamically as pieces are placed"""

    def __init__(self, **kwargs) -> None:
        # start as empty list - not None
        super().__init__()

        board_config = kwargs['board']

        self.placement: PlacementStrategy = board_config['placement']
        self.segment_size = board_config['segment-size']

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

    def _grow_horizontal(self, add_segments: int, dir: Direction) -> None:
        for _ in range(add_segments):
            for row in self:
                row_part = create_row_part(self.segment_size)
                if dir == Direction.EAST:
                    row.extend(row_part)
                elif dir == Direction.WEST:
                    for ele in reversed(row_part):
                        row.insert(0, ele)
                else:
                    raise ValueError(f'invalid value {dir} for dir')

    def _grow_vertical(self, add_segments: int, dir: Direction) -> None:
        for _ in range(add_segments):
            width = len(self[0]) if len(self) > 0 else self.segment_size
            segment = create_segment(width, self.segment_size)
            for row_part in segment:
                if dir == Direction.SOUTH:
                    self.append(row_part)
                elif dir == Direction.NORTH:
                    self.insert(0, row_part)
                else:
                    raise ValueError(f'invalid value {dir} for dir')

    def _initialize(self, segments: int) -> None:
        self._grow_vertical(segments, Direction.SOUTH)
        self._grow_horizontal(segments - 1, Direction.EAST)  # already 1 wide

    def expand_board(self, x: int, y: int, dir: Direction) -> tuple[int, int]:
        if dir in [Direction.NORTH, Direction.SOUTH]:
            self._grow_vertical(1, dir)
            dir = None if dir == Direction.SOUTH else Direction.SOUTH
        elif dir in [Direction.EAST, Direction.WEST]:
            self._grow_horizontal(1, dir)
            dir = None if dir == Direction.EAST else Direction.EAST

        return self.placement.adjust(x, y, dir, self.segment_size)

    def place_tiles(self, tiles: list[Tile], x: int, y: int, dir: Direction) -> int:
        # make sure spot is available
        can_place = self[y][x] is None

        if can_place:
            # expand if need to ...
            if self.placement.need_to_expand(self, len(tiles), x, y, dir):
                x, y = self.expand_board(x, y, dir)

        if can_place:
            # TODO: is this a valid placement?
            can_place, error = (can_place, None)

        if can_place:
            for idx, tile in enumerate(tiles):
                if idx != 0:
                    x, y = self.placement.adjust(x, y, dir)

                self[y][x] = tile
        else:
            raise ValueError(f'Not a valid placement: {error}')

        # TODO: calculate score
        score = 0

        return score
