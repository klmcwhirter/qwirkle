
from qwirkle.logic.exp_placement import ExpandingPlacementStrategy

settings = {
    'grid': {
        'color': 'gray',
        'thickness': 10,
    },
    'screen': {
        'width': 900,
        'height': 900,
        'bg_color': 'gainsboro',
    },
    'title': 'Qwirkle',
    'bag': {
        'tile-copies': 3,
    },
    'board': {
        'initial-segments': 2,
        'segment-size': 6,
        'placement': ExpandingPlacementStrategy()
    },
}
