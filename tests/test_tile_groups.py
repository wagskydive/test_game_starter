import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.tile_groups import is_destructible, get_group


def test_destructible_flag():
    assert not is_destructible("water")
    assert is_destructible("plains")
    assert not is_destructible("megalith")


def test_tile_groups():
    assert get_group("castle") == "settlement"
    assert get_group("mountains") == "mountain"
