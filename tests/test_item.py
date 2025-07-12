import os
import sys
sys.path.insert(0, os.path.abspath('src'))

from item import Item, Inventory


def test_item_defaults():
    item = Item(name='rock')
    assert item.name == 'rock'
    assert item.weight == 0.0
    assert item.volume == 0.0
    assert item.durability == 100


def test_inventory_add_remove_weight():
    inv = Inventory()
    rock = Item(name='rock', weight=2.5)
    stick = Item(name='stick', weight=1.0)
    inv.add(rock)
    inv.add(stick)
    assert inv.total_weight() == 3.5
    inv.remove(rock)
    assert inv.total_weight() == 1.0
