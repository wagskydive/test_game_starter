import os, sys
sys.path.insert(0, os.path.abspath('src'))

from item import Item, Inventory
from crafting import Recipe, craft


def test_craft_success():
    inv = Inventory()
    inv.add(Item(name='wood'))
    inv.add(Item(name='stone'))
    recipe = Recipe(ingredients={'wood': 1, 'stone': 1}, result=Item(name='axe'))
    item = craft(inv, recipe)
    assert item is not None
    assert item.name == 'axe'
    assert len(inv.items) == 1
    assert inv.items[0].name == 'axe'


def test_craft_missing_ingredient():
    inv = Inventory()
    inv.add(Item(name='wood'))
    recipe = Recipe(ingredients={'wood': 1, 'stone': 1}, result=Item(name='axe'))
    item = craft(inv, recipe)
    assert item is None
    # wood should still be present
    assert len(inv.items) == 1
    assert inv.items[0].name == 'wood'
