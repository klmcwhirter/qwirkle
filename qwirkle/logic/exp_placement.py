

from qwirkle.logic import BoardBase, Direction


class ExpandingPlacementStrategy:
    def adjust(self, x: int, y: int, dir: Direction, increment: int = 1) -> tuple[int, int]:
        if dir == Direction.NORTH:
            return (x, y - increment)
        elif dir == Direction.SOUTH:
            return (x, y + increment)
        elif dir == Direction.EAST:
            return (x + increment, y)
        elif dir == Direction.WEST:
            return (x - increment, y)

        # None
        return (x, y)

    def need_to_expand(self, board: BoardBase, num_tiles: int, x: int, y: int, dir: Direction) -> bool:
        if dir == Direction.NORTH:
            return (y - (num_tiles - 1)) < 0
        elif dir == Direction.SOUTH:
            return (y + num_tiles) > len(board)
        elif dir == Direction.WEST:
            return (x - (num_tiles - 1)) < 0
        elif dir == Direction.EAST:
            return (x + num_tiles) > len(board[y])
        else:
            raise ValueError(f'invalid value {dir} for dir')
