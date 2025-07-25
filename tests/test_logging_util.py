import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.logging_util import create_logger


def test_logger_creates_file(tmp_path):
    log_file = tmp_path / "test.log"
    logger = create_logger("test_logger", level="INFO", file_path=str(log_file))
    logger.info("hello world")
    assert log_file.exists()
    with open(log_file) as f:
        content = f.read()
    assert "test_logger" in content
    assert "INFO" in content
    assert "hello world" in content


def test_logger_filters_messages(tmp_path):
    log_file = tmp_path / "info.log"
    logger = create_logger("filter", level="INFO", file_path=str(log_file))
    logger.debug("hidden")
    logger.info("shown")
    with open(log_file) as f:
        content = f.read()
    assert "shown" in content
    assert "hidden" not in content


def test_logger_console_handler(monkeypatch, tmp_path):
    log_file = tmp_path / "console.log"
    monkeypatch.setenv("LOG_TO_CONSOLE", "1")
    logger = create_logger("console", file_path=str(log_file))
    handlers = len(logger.handlers)
    assert handlers == 2
