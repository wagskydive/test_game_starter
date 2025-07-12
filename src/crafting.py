from dataclasses import dataclass
from typing import Dict, Optional, Type

from .item import Item, Inventory
from .crafting_stations import Station
from .npc import NPC


@dataclass
class Recipe:
    ingredients: Dict[str, int]
    result: Item
    station: Optional[Type[Station]] = None
    blueprint: Optional[str] = None
    skill_required: int = 0


def craft(
    inventory: Inventory,
    recipe: Recipe,
    station: Optional[Station] = None,
    crafter: Optional[NPC] = None,
) -> Optional[Item]:
    """Attempt to craft an item using ingredients from the inventory.
    Returns the crafted Item if successful, otherwise None."""
    if recipe.station is not None:
        if station is None or not isinstance(station, recipe.station):
            return None
    if recipe.skill_required > 0:
        if crafter is None or crafter.crafting_skill < recipe.skill_required:
            return None
    if recipe.blueprint is not None:
        blueprint_found = any(
            it.name == recipe.blueprint and getattr(it, "is_blueprint", False)
            for it in inventory.items
        )
        if not blueprint_found:
            return None
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
