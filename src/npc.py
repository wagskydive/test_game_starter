from dataclasses import dataclass

@dataclass
class NPC:
    """Basic non-player character with simple needs."""
    name: str
    health: int = 100
    hunger: int = 100
    thirst: int = 100

    def tick(self, hunger_rate: int = 1, thirst_rate: int = 1) -> None:
        """Advance time by reducing hunger and thirst."""
        self.hunger = max(0, self.hunger - hunger_rate)
        self.thirst = max(0, self.thirst - thirst_rate)
