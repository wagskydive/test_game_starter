import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.npc import NPC
from src.ai_behavior import select_behavior, Behavior


def test_select_behavior_based_on_needs():
    n = NPC(name='Bob', hunger=10)
    assert select_behavior(n) == Behavior.WANDER
    n.hunger = 100
    n.social = 10
    assert select_behavior(n) == Behavior.SOCIALIZE
    n.social = 100
    assert select_behavior(n) == Behavior.IDLE
