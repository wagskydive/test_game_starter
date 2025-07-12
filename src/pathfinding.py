from __future__ import annotations
from heapq import heappush, heappop
from typing import List, Tuple, Set, Optional, Callable

from .game_map import GameMap

Coord = Tuple[int, int]


def heuristic(a: Coord, b: Coord) -> int:
    """Manhattan distance heuristic."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def find_path(
    start: Coord,
    goal: Coord,
    game_map: GameMap,
    obstacles: Optional[Set[Coord]] = None,
    avoid: Optional[Set[Coord]] = None,
    is_blocked: Optional[Callable[[Coord], bool]] = None,
) -> List[Coord]:
    """Return a path from start to goal using A* search with avoidance."""
    obstacles = obstacles or set()
    avoid = avoid or set()
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
            if is_blocked is not None and is_blocked(next_pos):
                continue
            step_cost = 1
            if next_pos in avoid:
                step_cost += 4
            new_cost = cost + step_cost
            priority = new_cost + heuristic(next_pos, goal)
            heappush(
                open_set, (priority, new_cost, next_pos, path + [next_pos])
            )
    return []
