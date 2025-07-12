import os
import sys
sys.path.insert(0, os.path.abspath('src'))
from worldgen import generate_map


def test_map_dimensions():
    m = generate_map(5, 3, seed=1)
    assert len(m) == 3
    assert all(len(row) == 5 for row in m)


def test_map_deterministic_seed():
    m1 = generate_map(4, 4, seed=42)
    m2 = generate_map(4, 4, seed=42)
    assert m1 == m2
