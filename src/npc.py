from dataclasses import dataclass, field
from typing import Optional, Set, Tuple, List, Dict

from .item import Inventory

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
    energy: int = 100
    safety: int = 100
    social: int = 100
    status: int = 100
    temperature: float = 37.0
    wounds: List[int] = field(default_factory=list)
    diseases: List[str] = field(default_factory=list)
    impressiveness: int = 0
    crafting_skill: int = 0
    inventory: Inventory = field(default_factory=Inventory)
    money: int = 0
    schedule: Dict[str, str] = field(default_factory=dict)
    personality_traits: List[str] = field(default_factory=list)
    emotional_state: str = "neutral"
    faction: Optional[str] = None
    animation_state: AnimationState = AnimationState.IDLE
    parents: List["NPC"] = field(default_factory=list)
    children: List["NPC"] = field(default_factory=list)
    friends: List["NPC"] = field(default_factory=list)
    x: int = 0
    y: int = 0

    def tick(
        self,
        hunger_rate: int = 1,
        thirst_rate: int = 1,
        rest_rate: int = 1,
        energy_rate: int = 1,
        safety_rate: int = 0,
        social_rate: int = 0,
        status_rate: int = 0,
        temperature_rate: float = 0.0,
        weather_temperature: float | None = None,
    ) -> None:
        """Advance time by reducing basic needs."""
        self.hunger = max(0, self.hunger - hunger_rate)
        self.thirst = max(0, self.thirst - thirst_rate)
        self.rest = max(0, self.rest - rest_rate)
        self.energy = max(0, self.energy - energy_rate)
        self.safety = max(0, self.safety - safety_rate)
        self.social = max(0, self.social - social_rate)
        self.status = max(0, self.status - status_rate)
        if weather_temperature is not None:
            self.temperature += (weather_temperature - self.temperature) * 0.1
        self.temperature += temperature_rate
        if self.wounds:
            self.health = max(0, self.health - len(self.wounds))
        if self.diseases:
            self.health = max(0, self.health - len(self.diseases))

    def satisfy(
        self,
        rest: int = 0,
        safety: int = 0,
        social: int = 0,
        status: int = 0,
        energy: int = 0,
    ) -> None:
        """Increase needs scores without exceeding 100."""
        self.rest = min(100, self.rest + rest)
        self.energy = min(100, self.energy + energy)
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

    def add_parent(self, parent: "NPC") -> None:
        if parent not in self.parents:
            self.parents.append(parent)
        if self not in parent.children:
            parent.children.append(self)

    def add_child(self, child: "NPC") -> None:
        if child not in self.children:
            self.children.append(child)
        if self not in child.parents:
            child.parents.append(self)

    def befriend(self, other: "NPC") -> None:
        if other not in self.friends:
            self.friends.append(other)
        if self not in other.friends:
            other.friends.append(self)

    def unfriend(self, other: "NPC") -> None:
        if other in self.friends:
            self.friends.remove(other)
        if self in other.friends:
            other.friends.remove(self)

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

    def get_activity(self, hour: int) -> str:
        """Return the scheduled activity for the given hour."""
        if not self.schedule:
            return "idle"
        if 6 <= hour < 12:
            period = "morning"
        elif 12 <= hour < 18:
            period = "afternoon"
        elif 18 <= hour < 24:
            period = "evening"
        else:
            period = "night"
        return self.schedule.get(period, "idle")
