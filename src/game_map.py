from dataclasses import dataclass
from typing import List

@dataclass
class GameMap:
    width: int
    height: int
    data: List[List[str]]

    def in_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height

    def get_tile(self, x: int, y: int) -> str | None:
        if not self.in_bounds(x, y):
            return None
        return self.data[y][x]
