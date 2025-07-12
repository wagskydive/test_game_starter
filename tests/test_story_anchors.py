import os, sys
sys.path.insert(0, os.path.abspath('src'))

from story_anchors import StoryAnchor, EventSystem


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
