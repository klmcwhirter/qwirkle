
import logging


def logging_config() -> None:
    """Setup logging format for the app"""
    logging.basicConfig(level=logging.DEBUG, format='{asctime} - {module} - {funcName} - {levelname} - {message}', style='{')
