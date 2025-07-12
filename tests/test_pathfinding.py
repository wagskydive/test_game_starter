import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.game_map import GameMap
from src.pathfinding import find_path


def make_map(width, height):
    return GameMap(width, height, [['.' for _ in range(width)] for _ in range(height)])


def test_find_path_simple():
    m = make_map(3, 1)
    path = find_path((0, 0), (2, 0), m)
    assert path == [(0, 0), (1, 0), (2, 0)]


def test_find_path_with_obstacle():
    m = make_map(3, 2)
    obstacles = {(1, 0)}
    path = find_path((0, 0), (2, 0), m, obstacles)
    assert (1, 0) not in path
    assert path[0] == (0, 0) and path[-1] == (2, 0)
