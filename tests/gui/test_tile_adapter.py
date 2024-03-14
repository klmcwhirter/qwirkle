"""tests for TileDisplayAdapter"""

from qwirkle.gui.tile_adapter import TileDisplayAdapter, pygame_ce_tile_adapter


def test_can_construct(app_config) -> None:
    adapter = TileDisplayAdapter(**app_config)

    assert adapter is not None


def test_tile_init_sets_per_config(app_config) -> None:
    adapter = TileDisplayAdapter(**app_config)

    assert adapter.font is not None
    assert adapter.font_color is not None
    assert adapter.padx is not None
    assert adapter.pady is not None
    assert adapter.screen_height is not None
    assert adapter.screen_width is not None


def test_pygame_ce_tile_adapter_provides_adapter(app_config) -> None:
    adapter = pygame_ce_tile_adapter(**app_config)

    assert adapter is not None
    assert isinstance(adapter, TileDisplayAdapter)
