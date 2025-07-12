import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.npc import NPC
from src.faction import Faction, FactionGoal


def test_add_and_remove_member():
    f = Faction("village")
    n = NPC(name="Bob")
    f.add_member(n)
    assert n in f.members
    assert n.faction == "village"
    f.remove_member(n)
    assert n not in f.members
    assert n.faction is None


def test_faction_tick_calls_behavior(monkeypatch):
    f = Faction("band", goal=FactionGoal.WORK)
    n = NPC(name="Sue")
    f.add_member(n)
    calls = []

    def fake_perform(npc, behavior, game_map=None):
        calls.append((npc.name, behavior.value))

    monkeypatch.setattr("src.faction.perform_behavior", fake_perform)
    f.tick()
    assert calls == [("Sue", "work")]
