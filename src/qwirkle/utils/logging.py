
import logging


def logging_config(**kwargs) -> None:
    """Setup logging format for the app"""
    verbose = 'verbose' in kwargs and kwargs['verbose']
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(level=level, format='{asctime} - {module} - {funcName} - {levelname} - {message}', style='{')
