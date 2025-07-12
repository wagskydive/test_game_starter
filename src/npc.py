from dataclasses import dataclass, field
from typing import Optional, Set, Tuple, List

from .animation_state import AnimationState

from .game_map import GameMap


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
    temperature: float = 37.0
    wounds: List[int] = field(default_factory=list)
    diseases: List[str] = field(default_factory=list)
    impressiveness: int = 0
    personality_traits: List[str] = field(default_factory=list)
    emotional_state: str = "neutral"
    faction: Optional[str] = None
    animation_state: AnimationState = AnimationState.IDLE
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
        temperature_rate: float = 0.0,
    ) -> None:
        """Advance time by reducing basic needs."""
        self.hunger = max(0, self.hunger - hunger_rate)
        self.thirst = max(0, self.thirst - thirst_rate)
        self.rest = max(0, self.rest - rest_rate)
        self.safety = max(0, self.safety - safety_rate)
        self.social = max(0, self.social - social_rate)
        self.status = max(0, self.status - status_rate)
        self.temperature += temperature_rate
        if self.wounds:
            self.health = max(0, self.health - len(self.wounds))
        if self.diseases:
            self.health = max(0, self.health - len(self.diseases))

    def satisfy(
        self, rest: int = 0, safety: int = 0, social: int = 0, status: int = 0
    ) -> None:
        """Increase needs scores without exceeding 100."""
        self.rest = min(100, self.rest + rest)
        self.safety = min(100, self.safety + safety)
        self.social = min(100, self.social + social)
        self.status = min(100, self.status + status)

    def heal(self, amount: int = 0) -> None:
        self.health = min(100, self.health + amount)

    def add_wound(self, damage: int) -> None:
        self.wounds.append(damage)
        self.health = max(0, self.health - damage)

    def heal_wound(self) -> None:
        if self.wounds:
            self.wounds.pop(0)

    def add_disease(self, name: str) -> None:
        if name not in self.diseases:
            self.diseases.append(name)

    def cure_disease(self, name: str) -> None:
        if name in self.diseases:
            self.diseases.remove(name)

    def adjust_status(self, delta: int) -> None:
        self.status = max(0, min(100, self.status + delta))
        self.impressiveness = max(0, self.impressiveness + delta)

    def add_trait(self, trait: str) -> None:
        if trait not in self.personality_traits:
            self.personality_traits.append(trait)

    def join_faction(self, faction: str) -> None:
        self.faction = faction

    def leave_faction(self) -> None:
        self.faction = None

    def set_animation(self, state: AnimationState) -> None:
        """Change the current animation state."""
        self.animation_state = state

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
            from .pathfinding import find_path

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
