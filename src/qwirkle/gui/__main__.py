"""qwirkle

Usage:
    qwirkle
"""


from qwirkle.config import settings
from qwirkle.gui import display_adapter
from qwirkle.utils.logging import logging_config

logging_config()
display_adapter(**settings)
