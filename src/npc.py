from dataclasses import dataclass
from typing import Optional

from game_map import GameMap

@dataclass
class NPC:
    """Basic non-player character with simple needs."""
    name: str
    health: int = 100
    hunger: int = 100
    thirst: int = 100
    x: int = 0
    y: int = 0

    def tick(self, hunger_rate: int = 1, thirst_rate: int = 1) -> None:
        """Advance time by reducing hunger and thirst."""
        self.hunger = max(0, self.hunger - hunger_rate)
        self.thirst = max(0, self.thirst - thirst_rate)

    def move(self, dx: int, dy: int, game_map: Optional[GameMap] = None) -> None:
        """Move the NPC by the given delta, respecting map bounds if provided."""
        new_x = self.x + dx
        new_y = self.y + dy
        if game_map is None or game_map.in_bounds(new_x, new_y):
            self.x = new_x
            self.y = new_y
