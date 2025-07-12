"""Simple procedural quest generation when no LLM is available."""
import random
from typing import Optional, Dict

QUEST_POOL = [
    ("Gather Wood", "Collect 10 pieces of wood from the forest."),
    ("Find Water", "Locate a fresh water source."),
    ("Meet Elder", "Talk to the village elder for guidance."),
]


def generate_quest(seed: Optional[int] = None) -> Dict[str, str]:
    rand = random.Random(seed)
    title, desc = rand.choice(QUEST_POOL)
    return {"title": title, "description": desc}
