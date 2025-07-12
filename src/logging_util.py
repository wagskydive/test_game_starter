import logging
import os
from logging import Logger
from logging.handlers import RotatingFileHandler


def create_logger(
    name: str, level: str = "INFO", file_path: str = "game.log"
) -> Logger:
    """Create and configure a logger.

    Parameters
    ----------
    name: str
        Name of the logger.
    level: str
        Logging level (e.g. 'INFO', 'DEBUG').
    file_path: str
        Path to the log file.

    Returns
    -------
    Logger
        Configured logger instance.
    """
    logger = logging.getLogger(name)
    # Clear existing handlers to avoid duplicate logs or stale file paths
    logger.handlers.clear()
    numeric_level = getattr(logging, level.upper(), logging.INFO)
    logger.setLevel(numeric_level)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    max_bytes = int(os.environ.get("LOG_MAX_BYTES", "1048576"))
    handler = RotatingFileHandler(file_path, maxBytes=max_bytes, backupCount=1)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    if os.environ.get("LOG_TO_CONSOLE", "0") == "1":
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        logger.addHandler(console)
    return logger
