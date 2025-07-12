import os, sys
sys.path.insert(0, os.path.abspath('src'))

from npc import NPC
from ai_behavior import select_behavior, Behavior


def test_select_behavior_based_on_needs():
    n = NPC(name='Bob', hunger=10)
    assert select_behavior(n) == Behavior.WANDER
    n.hunger = 100
    n.social = 10
    assert select_behavior(n) == Behavior.SOCIALIZE
    n.social = 100
    assert select_behavior(n) == Behavior.IDLE
