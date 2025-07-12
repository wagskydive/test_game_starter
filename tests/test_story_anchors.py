import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.story_anchors import StoryAnchor, EventSystem


def test_anchor_triggers_when_condition_met():
    es = EventSystem()
    called = False

    def condition():
        nonlocal called
        called = True
        return True

    anchor = StoryAnchor('goal', hard=True, condition=condition)
    es.add_anchor(anchor)
    triggered = es.tick()
    assert called
    assert anchor in triggered
    assert anchor.triggered is True
