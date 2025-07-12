from dataclasses import dataclass, field
from npc import NPC
from item import Inventory, Item

@dataclass
class Player(NPC):
    """Player character inheriting from NPC with an inventory."""
    inventory: Inventory = field(default_factory=Inventory)

    def pick_up(self, item: Item) -> None:
        """Add an item to the player's inventory."""
        self.inventory.add(item)
