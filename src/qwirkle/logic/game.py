"""headless logic for a game of Qwirkle"""

import os
from dataclasses import asdict
from datetime import datetime

from qwirkle.logic import Direction
from qwirkle.logic.bag import Bag
from qwirkle.logic.board import Board, BoardPlacement
from qwirkle.logic.game_log import GameEvent, GameEventName, GameLog
from qwirkle.logic.hand import Hand, HandExchange
from qwirkle.logic.player import Player
from qwirkle.logic.tile import Tile


def log_file_path_provider(path: str, timestamp: str) -> str:
    os.makedirs(path, exist_ok=True)
    return os.path.join(path, f'qwirkle_game_log_{timestamp}.json')


class Game:
    def __init__(self, **kwargs) -> None:
        self.config = kwargs  # also used in adapter

        self.players = self.config['game']['players']

        self.timestamp = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

        self.game_log = GameLog(**self.config)

        self.current_player: Player = self.players[0]

        self.bag: Bag
        self.board: Board
        self.hands: list[Hand]

        self.reset(False)

    def log_event(self, event: GameEvent) -> None:
        self.game_log.post_event(event)

    def exchange_tiles(self, player: Player, tiles: list[Tile]) -> HandExchange:
        hand = self.hands[player.number]
        exchange = hand.exchange_tiles(tiles)

        event = GameEvent(GameEventName.EXCHG, player, asdict(exchange))
        self.log_event(event)

        return exchange

    def exchange_tiles_by_index(self, player_index: int, tile_indexes: list[int]) -> HandExchange:
        '''helper override for UI'''
        tiles = [self.hands[player_index][ti] for ti in tile_indexes]
        exchange = self.exchange_tiles(self.players[player_index], tiles)
        return exchange

    def place_tiles(self, player: Player, tiles: list[Tile], x: int, y: int, dir: Direction) -> BoardPlacement:
        placement = self.board.place_tiles(player, tiles, x, y, dir)

        event = GameEvent(GameEventName.PLACE, player, asdict(placement))
        self.log_event(event)

        return placement

    def exit_game(self, log: bool = True) -> None:
        if log:
            event = GameEvent(GameEventName.EXITG, self.current_player, {})
            self.log_event(event)

            file_path = log_file_path_provider(self.config['log']['path'], self.timestamp)
            self.game_log.export_log(file_path)

    def reset(self, log: bool = True) -> None:
        if log:
            event = GameEvent(GameEventName.RESET, self.current_player, {})
            self.log_event(event)

            file_path = log_file_path_provider(self.config['log']['path'], self.timestamp)
            self.game_log.export_log(file_path)

        self.current_player = self.players[0]

        self.bag = Bag(shuffle=True, **self.config)
        self.board = Board(**self.config)
        self.hands = [Hand(game_bag=self.bag, player=player, **self.config) for player in self.players]
