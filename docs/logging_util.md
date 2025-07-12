# Logging Utility

The `logging_util` module provides a single helper `create_logger` for consistent logging across the project.

```python
from logging_util import create_logger

logger = create_logger("game", level="DEBUG", file_path="game.log")
logger.info("Game started")
```

The logger writes messages to the specified file using the format:

```
YYYY-MM-DD HH:MM:SS,ms - logger_name - LEVEL - message
```

Set the `level` parameter to control which messages are recorded.
