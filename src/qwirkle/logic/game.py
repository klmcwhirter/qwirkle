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

        self._current_player_index: int = 0
        self._players: list[Player] = []
        self._timestamp: str = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

        self.players = self.config['game']['players']

        self.game_log = GameLog(**self.config)
        self.log_path = self.config['log']['path']

        self.bag: Bag
        self.board: Board

        self.reset(False)

    @property
    def current_player(self) -> Player:
        return self.players[self.current_player_index]

    @current_player.setter
    def current_player(self, player: Player) -> None:
        index = self.players.index(player)
        self.current_player_index = index

    @property
    def current_player_index(self) -> int:
        return self._current_player_index

    @current_player_index.setter
    def current_player_index(self, index: int) -> None:
        _: Player = self.players[index]  # Allow IndexError
        self.current_player.active = False

        self._current_player_index = index
        self.current_player.active = True

    @property
    def players(self) -> list[Player]:
        return self._players.copy()

    @players.setter
    def players(self, players: list[Player]) -> None:
        if players is not None and len(players) > 1:
            self._players = players
            # TODO self.reset(log=False or log=True) here?
        else:
            raise ValueError('players must be a list of players with a length at least 2')

    def exchange_tiles(self, tiles: list[Tile]) -> HandExchange:
        hand = self.current_player.hand
        if hand is not None:
            exchange = hand.exchange_tiles(tiles)

            event = GameEvent(GameEventName.EXCHG, self.current_player, asdict(exchange))
            self.game_log.post_event(event)

            return exchange

        raise ValueError('no current hand')

    def exchange_tiles_by_index(self, tile_indices: list[int]) -> HandExchange:
        '''helper override for UI'''
        hand = self.current_player.hand
        if hand is not None:
            tiles = [hand[ti] for ti in tile_indices]
            exchange = self.exchange_tiles(tiles)
            return exchange

        raise ValueError('no current hand')

    def place_tiles(self, tiles: list[Tile], x: int, y: int, dir: Direction) -> BoardPlacement:
        placement = self.board.place_tiles(self.current_player, tiles, x, y, dir)

        event = GameEvent(GameEventName.PLACE, self.current_player, asdict(placement))
        self.game_log.post_event(event)

        return placement

    def exit_game(self) -> None:
        event = GameEvent(GameEventName.EXITG, self.current_player, {})
        self.game_log.post_event(event)

        file_path = log_file_path_provider(self.log_path, self._timestamp)
        self.game_log.export_log(file_path)

    def reset(self, log: bool = True) -> None:
        if log:
            event = GameEvent(GameEventName.RESET, self.current_player, {})
            self.game_log.post_event(event)

            file_path = log_file_path_provider(self.log_path, self._timestamp)
            self.game_log.export_log(file_path)

        self.current_player_index = 0

        self.bag = Bag(shuffle=True, **self.config)
        self.board = Board(**self.config)

        for player in self.players:
            player.hand = Hand(game_bag=self.bag, player_name=player.name, **self.config)
