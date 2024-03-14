
from typing import Any

import pytest

from qwirkle.config import settings


@pytest.fixture
def app_config() -> dict[str, Any]:
    return settings
