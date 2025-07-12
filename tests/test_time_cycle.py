import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.time_cycle import TimeSystem


def test_advance_hour_wraps():
    t = TimeSystem(hour=23)
    t.advance_hour()
    assert t.hour == 0
