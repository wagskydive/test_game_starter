import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.npc import NPC
import pytest


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


def test_npc_temperature_adjusts_with_cold_weather():
    n = NPC(name='Bob')
    n.tick(weather_temperature=0.0)
    assert n.temperature == pytest.approx(33.3, rel=1e-2)


def test_npc_temperature_adjusts_with_hot_weather():
    n = NPC(name='Bob')
    n.tick(weather_temperature=40.0)
    assert n.temperature == pytest.approx(37.3, rel=1e-2)


def test_npc_schedule():
    n = NPC(name='Bob', schedule={'morning': 'work', 'evening': 'sleep'})
    assert n.get_activity(8) == 'work'
    assert n.get_activity(22) == 'sleep'


def test_npc_energy_tick():
    n = NPC(name='Bob', energy=10)
    n.tick(energy_rate=5)
    assert n.energy == 5
    n.satisfy(energy=3)
    assert n.energy == 8


def test_npc_relationships():
    parent = NPC(name='Alice')
    child = NPC(name='Charlie')
    parent.add_child(child)
    friend = NPC(name='Dave')
    child.befriend(friend)
    assert child in parent.children
    assert parent in child.parents
    assert friend in child.friends
    assert child in friend.friends

