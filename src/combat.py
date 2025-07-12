from __future__ import annotations

import random
from item import Item
from npc import NPC


def _damage_from_item(item: Item) -> int:
    """Calculate damage based on item weight."""
    return max(1, int(item.weight))


def melee_attack(attacker: NPC, defender: NPC, weapon: Item, hit_chance: float = 0.8) -> bool:
    """Perform a melee attack. Returns True on hit."""
    if random.random() <= hit_chance:
        defender.health = max(0, defender.health - _damage_from_item(weapon))
        weapon.durability = max(0, weapon.durability - 1)
        return True
    return False


def ranged_attack(attacker: NPC, defender: NPC, weapon: Item, hit_chance: float = 0.6) -> bool:
    """Perform a ranged attack. Returns True on hit."""
    if random.random() <= hit_chance:
        defender.health = max(0, defender.health - _damage_from_item(weapon))
        weapon.durability = max(0, weapon.durability - 1)
        return True
    return False
