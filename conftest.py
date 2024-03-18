
import os
from typing import Any

import pytest

from qwirkle.config import settings
from qwirkle.logic.game import timestamp_provider
from qwirkle.logic.game_log import GameLog


@pytest.fixture
def app_config() -> dict[str, Any]:
    return settings


@pytest.fixture
def fake_log_file_path_provider():
    def wrapper(path: str, timestamp_provider=timestamp_provider) -> str:
        timestamp = timestamp_provider()
        return os.path.join(path, f'fake_qwirkle_game_{timestamp}.log')
    return wrapper


def fake_game_export(file_path: str) -> None:
    ...


@pytest.fixture
def fake_game_log(monkeypatch: pytest.MonkeyPatch, fake_log_file_path_provider) -> GameLog:
    monkeypatch.setattr('qwirkle.logic.game.log_file_path_provider', fake_log_file_path_provider)

    log = GameLog()
    log.export_log = fake_game_export
    return log
