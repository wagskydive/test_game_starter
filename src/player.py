from dataclasses import dataclass
from .npc import NPC
from .item import Item


@dataclass
class Player(NPC):
    """Player character inheriting from NPC."""

    def pick_up(self, item: Item) -> None:
        """Add an item to the player's inventory."""
        self.inventory.add(item)
