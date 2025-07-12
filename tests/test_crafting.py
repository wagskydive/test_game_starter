import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.item import Item, Inventory
from src.crafting import Recipe, craft
from src.crafting_stations import Anvil, Firepit
from src.npc import NPC


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


def test_craft_station_requirement():
    recipe = Recipe(
        ingredients={'ingot': 1, 'stick': 1},
        result=Item(name='sword'),
        station=Anvil,
    )
    inv = Inventory()
    inv.add(Item(name='ingot'))
    inv.add(Item(name='stick'))
    # Missing station
    assert craft(inv, recipe) is None

    inv = Inventory()
    inv.add(Item(name='ingot'))
    inv.add(Item(name='stick'))
    # Wrong station type
    assert craft(inv, recipe, station=Firepit()) is None

    inv = Inventory()
    inv.add(Item(name='ingot'))
    inv.add(Item(name='stick'))
    item = craft(inv, recipe, station=Anvil())
    assert item is not None
    assert item.name == 'sword'


def test_craft_blueprint_and_skill():
    recipe = Recipe(
        ingredients={'ingot': 1},
        result=Item(name='dagger'),
        station=Anvil,
        blueprint='dagger blueprint',
        skill_required=2,
    )
    bp = Item(name='dagger blueprint', is_blueprint=True)
    crafter = NPC(name='smith')
    crafter.crafting_skill = 2

    inv = Inventory()
    inv.add(Item(name='ingot'))
    inv.add(bp)
    item = craft(inv, recipe, station=Anvil(), crafter=crafter)
    assert item is not None
    assert item.name == 'dagger'
