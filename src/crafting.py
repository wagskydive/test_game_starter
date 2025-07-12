from dataclasses import dataclass
from typing import Dict, Optional

from item import Item, Inventory

@dataclass
class Recipe:
    ingredients: Dict[str, int]
    result: Item


def craft(inventory: Inventory, recipe: Recipe) -> Optional[Item]:
    """Attempt to craft an item using ingredients from the inventory.
    Returns the crafted Item if successful, otherwise None."""
    # Count available items by name
    counts: Dict[str, int] = {}
    for it in inventory.items:
        counts[it.name] = counts.get(it.name, 0) + 1
    # Verify all ingredients
    for name, qty in recipe.ingredients.items():
        if counts.get(name, 0) < qty:
            return None
    # Remove ingredients
    for name, qty in recipe.ingredients.items():
        removed = 0
        for it in list(inventory.items):
            if it.name == name and removed < qty:
                inventory.remove(it)
                removed += 1
    # Create result item and add to inventory
    crafted = Item(
        name=recipe.result.name,
        weight=recipe.result.weight,
        volume=recipe.result.volume,
        durability=recipe.result.durability,
    )
    inventory.add(crafted)
    return crafted
