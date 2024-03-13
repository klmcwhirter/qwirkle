

from qwirkle.logic import Direction, _BoardBase
from qwirkle.logic.tile import Tile


def create_row_part(width: int) -> list[Tile | None]:
    return [None for _ in range(width)]


def create_segment(width: int, height: int) -> list[list[Tile | None]]:
    return [create_row_part(width) for _ in range(height)]


class SegmentExpansionStrategy:
    def __init__(self, segment_size: int) -> None:
        self.segment_size: int = segment_size

    def adjust(self, x: int, y: int, dir: Direction | None, increment: int = 1) -> tuple[int, int]:
        if dir == Direction.NORTH:
            return (x, y - increment)
        elif dir == Direction.SOUTH:
            return (x, y + increment)
        elif dir == Direction.EAST:
            return (x + increment, y)
        elif dir == Direction.WEST:
            return (x - increment, y)

        # None - do not adjust - see board.py expand_board
        return (x, y)

    def grow_horizontal(self, board: _BoardBase, add_segments: int, dir: Direction) -> None:
        for _ in range(add_segments):
            for row in board:
                row_part = create_row_part(self.segment_size)
                if dir == Direction.EAST:
                    row.extend(row_part)
                elif dir == Direction.WEST:
                    for ele in reversed(row_part):
                        row.insert(0, ele)

    def grow_vertical(self, board: _BoardBase, add_segments: int, dir: Direction) -> None:
        for _ in range(add_segments):
            width = len(board[0]) if len(board) > 0 else self.segment_size
            segment = create_segment(width, self.segment_size)
            for row_part in segment:
                if dir == Direction.SOUTH:
                    board.append(row_part)
                elif dir == Direction.NORTH:
                    board.insert(0, row_part)

    def need_to_expand(self, board: _BoardBase, num_tiles: int, x: int, y: int, dir: Direction) -> bool:
        if dir == Direction.NORTH:
            return (y - (num_tiles - 1)) < 0
        elif dir == Direction.SOUTH:
            return (y + num_tiles) > len(board)
        elif dir == Direction.WEST:
            return (x - (num_tiles - 1)) < 0
        elif dir == Direction.EAST:
            return (x + num_tiles) > len(board[y])
