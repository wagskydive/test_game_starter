import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src import procedural_quests


def test_generate_quest_fields():
    q = procedural_quests.generate_quest(seed=0)
    assert set(q.keys()) == {'title', 'description'}


def test_generate_quest_deterministic():
    q1 = procedural_quests.generate_quest(seed=1)
    q2 = procedural_quests.generate_quest(seed=1)
    assert q1 == q2
