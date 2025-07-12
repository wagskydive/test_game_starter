from dataclasses import dataclass, field
from typing import List

@dataclass
class Item:
    """A basic item with minimal stats."""
    name: str
    weight: float = 0.0
    volume: float = 0.0
    durability: int = 100


class Inventory:
    """Simple inventory to hold items and track total weight."""
    def __init__(self):
        self.items: List[Item] = []

    def add(self, item: Item) -> None:
        self.items.append(item)

    def remove(self, item: Item) -> None:
        self.items.remove(item)

    def total_weight(self) -> float:
        return sum(item.weight for item in self.items)
