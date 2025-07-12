from dataclasses import dataclass, field
from typing import Optional, Set, Tuple, List

from game_map import GameMap

@dataclass
class NPC:
    """Basic non-player character with simple needs."""
    name: str
    health: int = 100
    hunger: int = 100
    thirst: int = 100
    rest: int = 100
    safety: int = 100
    social: int = 100
    status: int = 100
    personality_traits: List[str] = field(default_factory=list)
    emotional_state: str = "neutral"
    faction: Optional[str] = None
    x: int = 0
    y: int = 0

    def tick(
        self,
        hunger_rate: int = 1,
        thirst_rate: int = 1,
        rest_rate: int = 1,
        safety_rate: int = 0,
        social_rate: int = 0,
        status_rate: int = 0,
    ) -> None:
        """Advance time by reducing basic needs."""
        self.hunger = max(0, self.hunger - hunger_rate)
        self.thirst = max(0, self.thirst - thirst_rate)
        self.rest = max(0, self.rest - rest_rate)
        self.safety = max(0, self.safety - safety_rate)
        self.social = max(0, self.social - social_rate)
        self.status = max(0, self.status - status_rate)

    def satisfy(self, rest: int = 0, safety: int = 0, social: int = 0, status: int = 0) -> None:
        """Increase needs scores without exceeding 100."""
        self.rest = min(100, self.rest + rest)
        self.safety = min(100, self.safety + safety)
        self.social = min(100, self.social + social)
        self.status = min(100, self.status + status)

    def add_trait(self, trait: str) -> None:
        if trait not in self.personality_traits:
            self.personality_traits.append(trait)

    def join_faction(self, faction: str) -> None:
        self.faction = faction

    def leave_faction(self) -> None:
        self.faction = None

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
