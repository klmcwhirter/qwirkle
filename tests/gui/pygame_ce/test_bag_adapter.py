"""tests for BagDisplayAdapter"""

from qwirkle.gui.pygame_ce.bag_adapter import (BagDisplayAdapter,
                                               pygame_ce_bag_adapter)
from qwirkle.logic.bag import Bag


def test_can_construct(app_config) -> None:
    bag = Bag(**app_config)
    adapter = BagDisplayAdapter(bag)

    assert adapter is not None


def test_bag_init_sets_per_config(app_config) -> None:
    bag = Bag(**app_config)
    adapter = BagDisplayAdapter(bag)

    assert bag is adapter.bag

    assert adapter.font is not None
    assert adapter.font_color is not None
    assert adapter.padx is not None
    assert adapter.pady is not None
    assert adapter.screen_height is not None
    assert adapter.screen_width is not None


def test_pygame_ce_bag_adapter_provides_adapter(app_config) -> None:
    bag = Bag(**app_config)
    adapter = pygame_ce_bag_adapter(bag)

    assert adapter is not None
    assert isinstance(adapter, BagDisplayAdapter)
