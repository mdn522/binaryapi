"""A python wrapper for Binary API."""

import logging


def _prepare_logging():
    """Prepare logger for module Binary API."""
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.NullHandler())

    websocket_logger = logging.getLogger("websocket")
    websocket_logger.setLevel(logging.DEBUG)
    websocket_logger.addHandler(logging.NullHandler())


_prepare_logging()
