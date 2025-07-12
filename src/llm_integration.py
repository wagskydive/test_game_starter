import os
from typing import Optional

_offline_model: Optional[str] = None


def load_offline_model(path: str) -> bool:
    """Load an offline model if the file exists."""
    global _offline_model
    if os.path.exists(path):
        _offline_model = path
        return True
    return False


def generate_dialogue(prompt: str) -> Optional[str]:
    """Return LLM generated dialogue if enabled."""
    if os.environ.get("DISABLE_LLM", "0") == "1":
        return None
    if _offline_model:
        # Stub for offline generation via Godot-LLM plugin
        return f"[OFFLINE_LLM]: {prompt}"
    # Stub: In real use this would call an external model
    return f"[LLM]: {prompt}"
