import logging
from logging import Logger

def create_logger(name: str, level: str = "INFO", file_path: str = "game.log") -> Logger:
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
    handler = logging.FileHandler(file_path)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
