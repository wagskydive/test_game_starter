from __future__ import annotations
from heapq import heappush, heappop
from typing import List, Tuple, Set, Optional

from game_map import GameMap

Coord = Tuple[int, int]


def heuristic(a: Coord, b: Coord) -> int:
    """Manhattan distance heuristic."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def find_path(start: Coord, goal: Coord, game_map: GameMap,
              obstacles: Optional[Set[Coord]] = None) -> List[Coord]:
    """Return a path from start to goal using A* search."""
    obstacles = obstacles or set()
    open_set = []
    heappush(open_set, (heuristic(start, goal), 0, start, [start]))
    visited: Set[Coord] = set()

    while open_set:
        _, cost, current, path = heappop(open_set)
        if current == goal:
            return path
        if current in visited:
            continue
        visited.add(current)
        x, y = current
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            next_pos = (nx, ny)
            if not game_map.in_bounds(nx, ny):
                continue
            if next_pos in obstacles or next_pos in visited:
                continue
            new_cost = cost + 1
            priority = new_cost + heuristic(next_pos, goal)
            heappush(open_set, (priority, new_cost, next_pos, path + [next_pos]))
    return []
