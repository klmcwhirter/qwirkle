
from qwirkle.logic.exp_placement import SegmentExpansionStrategy

settings = {
    'bag': {
        'tile-copies': 3,
        'font-size': 16,
        'font-color': 'black',
        'padx': 10,
        'pady': 10,
    },
    'board': {
        'initial-segments': 2,
        'segment-size': 6,
        'expansion': SegmentExpansionStrategy(),
        'font-size': 16,
        'font-color': 'black',
        'padx': 10,
        'pady': 10,
    },
    'colors': [
        {'name': 'red',    'alias': 'red',     'code': 'R'},
        {'name': 'orange', 'alias': 'orange',  'code': 'O'},
        {'name': 'yellow', 'alias': 'yellow',  'code': 'Y'},
        {'name': 'green',  'alias': 'green',   'code': 'G'},
        {'name': 'blue',   'alias': 'blue',    'code': 'B'},
        {'name': 'purple', 'alias': 'purple',  'code': 'P'},
    ],
    'hand': {
        'tiles': 6,

        'font-size': 16,
        'font-color': 'blue',
        'padx': 10,
        'pady': 10,
    },
    'screen': {
        'width': 1600,
        'height': 900,
        'bg-color': 'gainsboro',
    },
    'tile': {
        'border-color': 'gray',
        'border-thickness': 3,

        'font-size': 16,
        'font-color': 'gray',
        'padx': 10,
        'pady': 10,
    },
    'title': 'Qwirkle for Two',
}
