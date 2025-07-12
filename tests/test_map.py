import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.game_map import GameMap
from src.worldgen import generate_map
from src.npc import NPC


def test_get_tile_in_bounds():
    data = generate_map(3, 3, seed=1)
    m = GameMap(3, 3, data)
    allowed = {'water', 'plains', 'forest', 'hills', 'mountains', 'village', 'castle', 'ruins', 'trade_post', 'megalith'}
    assert m.get_tile(0, 0) in allowed


def test_get_tile_out_of_bounds():
    data = generate_map(3, 3, seed=1)
    m = GameMap(3, 3, data)
    assert m.get_tile(-1, 0) is None
    assert m.get_tile(3, 3) is None


def test_npc_move_within_bounds():
    data = generate_map(5, 5, seed=1)
    m = GameMap(5, 5, data)
    n = NPC(name='Bob')
    n.move(1, 1, m)
    assert (n.x, n.y) == (1, 1)


def test_npc_move_blocked_by_bounds():
    data = generate_map(5, 5, seed=1)
    m = GameMap(5, 5, data)
    n = NPC(name='Bob')
    n.move(-1, 0, m)
    assert (n.x, n.y) == (0, 0)

