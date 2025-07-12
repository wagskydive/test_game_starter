import os, sys
sys.path.insert(0, os.path.abspath('src'))
from npc import NPC


def test_npc_defaults():
    n = NPC(name='Bob')
    assert n.name == 'Bob'
    assert n.health == 100
    assert n.hunger == 100
    assert n.thirst == 100
    assert n.rest == 100
    assert n.safety == 100
    assert n.social == 100
    assert n.status == 100


def test_npc_tick_reduces_needs():
    n = NPC(name='Bob')
    n.tick()
    assert n.hunger == 99
    assert n.thirst == 99
    assert n.rest == 99


def test_npc_needs_do_not_go_negative():
    n = NPC(name='Bob', hunger=1, thirst=1)
    n.tick()
    n.tick()
    assert n.hunger == 0
    assert n.thirst == 0


def test_npc_personality_and_faction():
    n = NPC(name='Bob')
    n.add_trait('brave')
    n.join_faction('village')
    assert 'brave' in n.personality_traits
    assert n.faction == 'village'
    n.leave_faction()
    assert n.faction is None


def test_npc_health_extensions():
    n = NPC(name='Bob')
    n.add_wound(5)
    n.add_disease('flu')
    assert n.health == 95
    n.tick()
    assert n.health == 93
    n.heal(5)
    n.heal_wound()
    n.cure_disease('flu')
    n.tick()
    assert n.health == 98


def test_npc_impressiveness_and_status():
    n = NPC(name='Bob', status=90)
    n.adjust_status(5)
    assert n.status == 95
    assert n.impressiveness == 5

