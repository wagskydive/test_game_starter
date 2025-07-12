import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.animation_state import AnimationState
from src.npc import NPC


def test_default_animation_state():
    n = NPC(name='Bob')
    assert n.animation_state == AnimationState.IDLE


def test_set_animation():
    n = NPC(name='Bob')
    n.set_animation(AnimationState.ANGRY)
    assert n.animation_state == AnimationState.ANGRY
