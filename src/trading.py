from __future__ import annotations

from dataclasses import dataclass

from .npc import NPC
from .item import Item


def trade(buyer: NPC, seller: NPC, item: Item, price: int) -> bool:
    """Exchange an item for currency between two NPCs."""
    if item not in seller.inventory.items:
        return False
    if buyer.money < price:
        return False
    if not buyer.inventory.can_add(item):
        return False

    seller.inventory.remove(item)
    buyer.inventory.add(item)
    buyer.money -= price
    seller.money += price
    return True
