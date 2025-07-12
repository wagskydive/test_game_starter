import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from src.item import Item, Inventory


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


def test_inventory_volume_limit():
    inv = Inventory(max_volume=3.0)
    rock = Item(name='rock', volume=2.0)
    inv.add(rock)
    stick = Item(name='stick', volume=2.0)
    with pytest.raises(ValueError):
        inv.add(stick)


def test_nested_container():
    bag = Item(name='bag', max_volume=3.0, contents=Inventory(max_volume=3.0))
    outer = Inventory()
    outer.add(bag)
    rock = Item(name='rock', volume=2.0)
    bag.contents.add(rock)
    assert rock in bag.contents.items
