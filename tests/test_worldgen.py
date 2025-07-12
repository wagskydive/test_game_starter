import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.worldgen import generate_map


def test_map_dimensions():
    m = generate_map(5, 3, seed=1)
    assert len(m) == 3
    assert all(len(row) == 5 for row in m)


def test_map_deterministic_seed():
    m1 = generate_map(4, 4, seed=42)
    m2 = generate_map(4, 4, seed=42)
    assert m1 == m2


def test_map_respects_adjacency():
    m = generate_map(5, 5, seed=1)
    from src.worldgen import ADJACENCY

    height = len(m)
    width = len(m[0])
    special = {"village", "castle", "ruins", "trade_post", "megalith", "water"}
    for y in range(height):
        for x in range(width):
            tile = m[y][x]
            if tile in special:
                continue
            for nx, ny in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
                if 0 <= nx < width and 0 <= ny < height:
                    assert m[ny][nx] in ADJACENCY[tile]


def test_worldgen_settlements():
    m = generate_map(10, 10, seed=99)
    tiles = [t for row in m for t in row]
    for name in ["village", "castle", "ruins", "trade_post", "megalith"]:
        assert name in tiles


def test_worldgen_settlements_deterministic():
    m1 = generate_map(8, 8, seed=5)
    m2 = generate_map(8, 8, seed=5)
    assert m1 == m2
