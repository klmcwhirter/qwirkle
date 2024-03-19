# qwirkle
Inspired by Qwirkle - cli, Web and pygame-ce UI

[![Tests](https://github.com/klmcwhirter/qwirkle/actions/workflows/tests.yml/badge.svg)](https://github.com/klmcwhirter/qwirkle/actions/)
[![Code style: flake8](https://img.shields.io/badge/code%20style-flake8-green.svg)](https://github.com/pycqa/flake8)
[![Code Analysis: mypy](https://img.shields.io/badge/code%20analysis-mypy-blue.svg)](https://github.com/python/mypy)
[![Tox Versions](https://img.shields.io/badge/tox-v4-yellowgreen)](https://github.com/tox-dev/tox)
[![pygame-ce](https://img.shields.io/badge/pygame%2Dce-aaeebb)](https://github.com/pygame-community/pygame-ce)
![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2Fklmcwhirter%2Fqwirkle%2Fmaster%2Fpyproject.toml&logo=Python)

## Overview
Qwirkle is a game created by Susan McKinley Ross of [Idea Duck](http://ideaduck.com/) and published by [Mind Ware](https://www.mindware.orientaltrading.com/h3-about-us.fltr) as a physical board game in 2006.

- [Rules](./docs/rules.md)
- [Requirements](./docs/test-requirements.md)
- [Design](./docs/design.md)


## Test Coverage
The design has led to putting the game logic in a Python package `qwirkle.logic` that is completely headless.

This means that:
* `qwirkle.logic` should be where the most code is
* `qwirkle.logic` should be where the most risk is
* `qwirkle.logic` is tested thoroughly!

```
---------- coverage: platform linux, python 3.12.2-final-0 -----------
Name                                             Stmts   Miss  Cover
--------------------------------------------------------------------
src/qwirkle/__init__.py                              0      0   100%
src/qwirkle/config.py                                3      0   100%
src/qwirkle/gui/__init__.py                          3      0   100%
src/qwirkle/gui/__main__.py                          5      5     0%
src/qwirkle/gui/bag_adapter.py                      23      5    78%
src/qwirkle/gui/board_adapter.py                    31      9    71%
src/qwirkle/gui/game_adapter.py                     69     34    51%
src/qwirkle/gui/hand_adapter.py                     23      7    70%
src/qwirkle/gui/tile_adapter.py                     22      6    73%
src/qwirkle/logic/__init__.py                       22      4    82%
src/qwirkle/logic/bag.py                            29      0   100%
src/qwirkle/logic/board.py                          91      0   100%
src/qwirkle/logic/color.py                          10      0   100%
src/qwirkle/logic/component_display_adapter.py       4      1    75%
src/qwirkle/logic/exp_placement.py                  46      0   100%
src/qwirkle/logic/game.py                           57      2    96%
src/qwirkle/logic/game_log.py                       40      8    80%
src/qwirkle/logic/hand.py                           28      0   100%
src/qwirkle/logic/player.py                          5      0   100%
src/qwirkle/logic/shape.py                           9      0   100%
src/qwirkle/logic/tile.py                            9      0   100%
--------------------------------------------------------------------
TOTAL                                              529     81    85%

```

## See also

- [Translated Requirements](./docs/requirements.md)
