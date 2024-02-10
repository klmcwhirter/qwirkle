
import pytest

from ..config import settings


@pytest.fixture
def app_config():
    return settings
