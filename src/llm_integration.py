import os
from typing import Optional


def generate_dialogue(prompt: str) -> Optional[str]:
    """Return LLM generated dialogue if enabled."""
    if os.environ.get("DISABLE_LLM", "0") == "1":
        return None
    # Stub: In real use this would call an external model
    return f"[LLM]: {prompt}"
