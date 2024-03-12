
from typing import Protocol


class ComponentDisplayAdapter(Protocol):
    '''Display Adapter to use for Bag, Board, Tile, etc.'''

    def draw(self, /, **kwargs):
        ...
