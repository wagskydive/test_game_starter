from __future__ import annotations
from enum import Enum
from random import choice
from typing import Optional

from npc import NPC
from game_map import GameMap

class Behavior(Enum):
    IDLE = "idle"
    WANDER = "wander"
    WORK = "work"
    SOCIALIZE = "socialize"


def select_behavior(npc: NPC) -> Behavior:
    """Pick a simple behavior based on NPC needs."""
    if npc.hunger < 20:
        return Behavior.WANDER
    if npc.social < 20:
        return Behavior.SOCIALIZE
    return Behavior.IDLE


def perform_behavior(npc: NPC, behavior: Behavior, game_map: Optional[GameMap] = None) -> None:
    """Execute one tick of the behavior."""
    if behavior == Behavior.WANDER:
        npc.move(choice([-1, 0, 1]), choice([-1, 0, 1]), game_map)
    elif behavior == Behavior.SOCIALIZE:
        npc.satisfy(social=1)
    elif behavior == Behavior.WORK:
        npc.satisfy(status=1)
