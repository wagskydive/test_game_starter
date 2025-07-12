from dataclasses import dataclass

@dataclass
class TimeSystem:
    """Simple day/night cycle tracker."""
    hour: int = 0

    def advance_hour(self) -> None:
        self.hour = (self.hour + 1) % 24
