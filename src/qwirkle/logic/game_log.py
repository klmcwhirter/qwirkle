"""The log of actions in the game"""

from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum, auto
from json import dumps, load
from typing import Any, Generator

from qwirkle.logic.player import Player


class GameEventName(StrEnum):
    '''
        RESET: Reset or restart game
        PLACE: Place tiles
        EXCHG: Exchange tiles from hand with bag
        EXITG: Exit game

    '''
    RESET = auto()
    PLACE = auto()
    EXCHG = auto()
    EXITG = auto()


@dataclass
class GameEvent:
    name: GameEventName
    player: Player
    data: dict[str, Any]


@dataclass
class _GameLogEntry:
    timestamp: str
    event: GameEvent


class GameLog:
    def __init__(self, **kwargs) -> None:
        self.config = kwargs

        self._log: list[_GameLogEntry] = []

    def post_event(self, event: GameEvent) -> None:
        entry = _GameLogEntry(timestamp=datetime.now().isoformat(), event=event)
        self._log.append(entry)

    def entries(self) -> Generator[tuple[str, GameEvent], None, None]:
        for entry in self._log:
            yield (entry.timestamp, entry.event)

    def export_log(self, file_path: str) -> None:
        json_content = dumps(self._log)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(json_content)

    def import_log(self, file_path: str) -> None:
        log: list[_GameLogEntry] = []
        with open(file_path, 'r', encoding='utf-8') as f:
            log = load(fp=f)
        self._log = log
