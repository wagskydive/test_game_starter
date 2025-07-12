from dataclasses import dataclass
from typing import Callable, List


@dataclass
class StoryAnchor:
    name: str
    hard: bool = False
    triggered: bool = False
    condition: Callable[[], bool] | None = None


class EventSystem:
    def __init__(self):
        self.anchors: List[StoryAnchor] = []

    def add_anchor(self, anchor: StoryAnchor) -> None:
        self.anchors.append(anchor)

    def tick(self) -> List[StoryAnchor]:
        """Check anchors and return newly triggered ones."""
        triggered = []
        for a in self.anchors:
            if not a.triggered and (a.condition is None or a.condition()):
                a.triggered = True
                triggered.append(a)
        return triggered
