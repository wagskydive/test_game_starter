import json
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.item_db import load_items, load_recipes
from src.crafting import Recipe


def test_load_items_and_recipes(tmp_path):
    items_path = tmp_path / "items.json"
    recipes_path = tmp_path / "recipes.json"
    with open(items_path, "w") as f:
        json.dump([
            {"name": "wood", "weight": 1.0, "volume": 1.0},
            {"name": "plank", "weight": 0.5, "volume": 0.5},
        ], f)
    with open(recipes_path, "w") as f:
        json.dump([
            {"name": "plank", "ingredients": {"wood": 1}, "result": "plank"}
        ], f)

    items = load_items(str(items_path))
    assert items["wood"].weight == 1.0
    recipes = load_recipes(str(recipes_path), items)
    assert isinstance(recipes["plank"], Recipe)
    assert recipes["plank"].ingredients["wood"] == 1
