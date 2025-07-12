from dataclasses import dataclass
from typing import Optional, Set, Tuple

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

    def move(
        self,
        dx: int = 0,
        dy: int = 0,
        game_map: Optional[GameMap] = None,
        target: Optional[Tuple[int, int]] = None,
        obstacles: Optional[Set[Tuple[int, int]]] = None,
    ) -> None:
        """Move the NPC either by delta or toward a target using pathfinding."""
        if target is not None:
            if game_map is None:
                raise ValueError("game_map required for pathfinding")
            from pathfinding import find_path

            path = find_path((self.x, self.y), target, game_map, obstacles)
            if len(path) > 1:
                next_x, next_y = path[1]
                dx = next_x - self.x
                dy = next_y - self.y
            else:
                dx = dy = 0

        new_x = self.x + dx
        new_y = self.y + dy
        if game_map is None or game_map.in_bounds(new_x, new_y):
            self.x = new_x
            self.y = new_y
