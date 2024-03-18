"""headless logic for a game of Qwirkle"""

import os
from dataclasses import asdict
from datetime import datetime

from qwirkle.logic import Direction
from qwirkle.logic.bag import Bag
from qwirkle.logic.board import Board, BoardPlacement
from qwirkle.logic.game_log import GameEvent, GameEventName, GameLog
from qwirkle.logic.hand import Hand
from qwirkle.logic.player import Player
from qwirkle.logic.tile import Tile


def timestamp_provider() -> str:
    return datetime.now().isoformat()


def log_file_path_provider(path: str, timestamp_provider=timestamp_provider) -> str:
    os.makedirs(path, exist_ok=True)
    timestamp = timestamp_provider()
    return os.path.join(path, f'qwirkle_game_{timestamp}.log')


class Game:
    def __init__(self, **kwargs) -> None:
        self.config = kwargs  # also used in adapter

        self.players = self.config['game']['players']

        self.game_log = GameLog(**self.config)

        self.current_player: Player = self.players[0]

        self.bag: Bag
        self.board: Board
        self.hands: list[Hand]

        self.reset(False)

    def log_event(self, event: GameEvent) -> None:
        self.game_log.post_event(event)

    def place_tiles(self, player: Player, tiles: list[Tile], x: int, y: int, dir: Direction) -> BoardPlacement:
        placement = self.board.place_tiles(player, tiles, x, y, dir)

        event = GameEvent(GameEventName.PLACE, player, asdict(placement))
        self.log_event(event)

        return placement

    def reset(self, log: bool = True) -> None:
        if log:
            event = GameEvent(GameEventName.RESET, self.current_player, {})
            self.log_event(event)

            self.game_log.export_log(log_file_path_provider(self.config['log']['path']))

        self.current_player = self.players[0]

        self.bag = Bag(shuffle=True, **self.config)
        self.board = Board(**self.config)
        self.hands = [Hand(game_bag=self.bag, player=player, **self.config) for player in self.players]
