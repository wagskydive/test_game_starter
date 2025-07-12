import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.player import Player
from src.item import Item


def test_player_defaults():
    p = Player(name='Hero')
    assert p.name == 'Hero'
    assert p.health == 100
    assert p.hunger == 100
    assert p.thirst == 100
    assert p.inventory.total_weight() == 0


def test_player_pick_up_item():
    p = Player(name='Hero')
    rock = Item(name='rock', weight=2.0)
    p.pick_up(rock)
    assert rock in p.inventory.items
    assert p.inventory.total_weight() == 2.0
