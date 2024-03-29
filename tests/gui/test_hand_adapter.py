"""tests for HandDisplayAdapter"""

from qwirkle.gui.hand_adapter import HandDisplayAdapter, pygame_ce_hand_adapter


def test_can_construct(app_config) -> None:
    adapter = HandDisplayAdapter(**app_config)

    assert adapter is not None


def test_hand_init_sets_per_config(app_config) -> None:
    adapter = HandDisplayAdapter(**app_config)

    assert adapter.font is not None
    assert adapter.font_color is not None
    assert adapter.active_color is not None
    assert adapter.inactive_color is not None
    assert adapter.padx is not None
    assert adapter.pady is not None

    assert adapter.tile_adapter is not None


def test_pygame_ce_hand_adapter_provides_adapter(app_config) -> None:
    adapter = pygame_ce_hand_adapter(**app_config)

    assert adapter is not None
    assert isinstance(adapter, HandDisplayAdapter)
