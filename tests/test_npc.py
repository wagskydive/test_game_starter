import os, sys
sys.path.insert(0, os.path.abspath('src'))
from npc import NPC


def test_npc_defaults():
    n = NPC(name='Bob')
    assert n.name == 'Bob'
    assert n.health == 100
    assert n.hunger == 100
    assert n.thirst == 100


def test_npc_tick_reduces_needs():
    n = NPC(name='Bob')
    n.tick()
    assert n.hunger == 99
    assert n.thirst == 99


def test_npc_needs_do_not_go_negative():
    n = NPC(name='Bob', hunger=1, thirst=1)
    n.tick()
    n.tick()
    assert n.hunger == 0
    assert n.thirst == 0
