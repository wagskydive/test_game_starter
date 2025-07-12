import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src import palette


def test_palette_keys():
    keys = set(palette.PALETTE.keys())
    assert {'skin', 'eyes', 'hair', 'clothes', 'rare_highlight'} <= keys
    assert palette.LAYERS == ['body', 'eyes', 'hair', 'clothes']
