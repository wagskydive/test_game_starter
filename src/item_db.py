import json
from typing import Dict
from dataclasses import asdict

from .item import Item
from .crafting import Recipe


def load_items(path: str) -> Dict[str, Item]:
    with open(path, 'r') as f:
        data = json.load(f)
    items = {}
    for entry in data:
        name = entry['name']
        params = {k: v for k, v in entry.items() if k != 'name'}
        items[name] = Item(name=name, **params)
    return items


def load_recipes(path: str, items: Dict[str, Item]) -> Dict[str, Recipe]:
    with open(path, 'r') as f:
        data = json.load(f)
    recipes = {}
    for entry in data:
        result_name = entry['result']
        result_item = items.get(result_name, Item(name=result_name))
        recipes[entry['name']] = Recipe(ingredients=entry['ingredients'], result=result_item)
    return recipes
