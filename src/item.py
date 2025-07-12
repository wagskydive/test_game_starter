from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Item:
    """A basic item with minimal stats."""

    name: str
    weight: float = 0.0
    volume: float = 0.0
    durability: int = 100
    is_blueprint: bool = False
    max_volume: Optional[float] = None
    contents: Optional["Inventory"] = None


class Inventory:
    """Simple inventory to hold items and track weight/volume."""

    def __init__(self, max_volume: Optional[float] = None):
        self.items: List[Item] = []
        self.max_volume = max_volume

    def total_volume(self) -> float:
        return sum(item.volume for item in self.items)

    def can_add(self, item: Item) -> bool:
        if self.max_volume is None:
            return True
        return self.total_volume() + item.volume <= self.max_volume

    def add(self, item: Item) -> None:
        if not self.can_add(item):
            raise ValueError("Inventory capacity exceeded")
        self.items.append(item)

    def remove(self, item: Item) -> None:
        self.items.remove(item)

    def total_weight(self) -> float:
        return sum(item.weight for item in self.items)
