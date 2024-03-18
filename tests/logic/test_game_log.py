
from qwirkle.logic.game_log import GameEvent, GameEventName, GameLog
from qwirkle.logic.player import Player


def test_can_construct() -> None:
    log = GameLog()

    assert log is not None


def test_init() -> None:
    log = GameLog()

    assert log._log is not None
    assert 0 == len(log._log)


def test_post_event_adds_to_log() -> None:
    log = GameLog()
    assert 0 == len(log._log)

    event = GameEvent(GameEventName.PLACE, Player('', 0), {})

    log.post_event(event)

    assert len(log._log) > 0

    assert event.name == log._log[0].event.name


def test_entries_returns_current() -> None:
    log = GameLog()

    entries = list(log.entries())

    assert 0 == len(entries)

    event = GameEvent(GameEventName.PLACE, Player('', 0), {})
    log.post_event(event)

    entries = list(log.entries())

    assert 1 == len(entries)
    assert event.name == entries[0][1].name

    log.post_event(event)

    entries = list(log.entries())

    assert 2 == len(entries)
    assert event.name == entries[1][1].name

    assert entries[0][0] != entries[1][0], 'timestamps should differ'
