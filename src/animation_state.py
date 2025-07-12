"""Enumeration of simple NPC animation states."""
from enum import Enum, auto

class AnimationState(Enum):
    IDLE = auto()
    WALK = auto()
    ANGRY = auto()
    EXCITED = auto()
    SITTING = auto()
