import random
from typing import List, Set, Tuple

# Adjacency rules for tiles used by the wave function collapse algorithm
ADJACENCY = {
    "water": {"water", "plains"},
    "plains": {"water", "plains", "forest", "hills", "village", "castle", "ruins", "trade_post", "megalith"},
    "forest": {"plains", "forest", "village", "ruins", "trade_post", "megalith", "castle"},
    "hills": {"plains", "hills", "mountains", "castle", "ruins", "trade_post", "megalith"},
    "mountains": {"hills", "mountains", "castle", "megalith", "trade_post", "ruins"},
    "village": {"plains", "forest", "hills", "mountains", "megalith"},
    "castle": {"plains", "hills", "mountains", "ruins", "castle", "trade_post", "megalith", "village"},
    "ruins": {"plains", "forest", "hills", "megalith", "castle", "trade_post"},
    "trade_post": {"plains", "forest", "hills", "megalith", "castle", "mountains", "trade_post", "ruins"},
    "megalith": {"plains", "hills", "mountains", "castle", "trade_post", "ruins", "megalith"},
}
TILES = list(ADJACENCY.keys())


def _neighbors(
    x: int, y: int, width: int, height: int
) -> List[Tuple[int, int]]:
    coords = []
    if x > 0:
        coords.append((x - 1, y))
    if x < width - 1:
        coords.append((x + 1, y))
    if y > 0:
        coords.append((x, y - 1))
    if y < height - 1:
        coords.append((x, y + 1))
    return coords


def _place_settlements(map_data: List[List[str]], seed: int | None = None) -> None:
    """Place settlement and special tiles deterministically."""
    random.seed(seed)
    height = len(map_data)
    width = len(map_data[0])
    structures = ["village", "castle", "ruins", "trade_post"]
    def pick_location() -> Tuple[int, int]:
        candidates = []
        for y in range(height):
            for x in range(width):
                if map_data[y][x] not in {"plains", "hills", "mountains"}:
                    continue
                neighbors = _neighbors(x, y, width, height)
                if any(map_data[ny][nx] == "water" for nx, ny in neighbors):
                    continue
                candidates.append((x, y))
        if not candidates:
            return 0, 0
        return random.choice(candidates)

    for name in structures:
        x, y = pick_location()
        map_data[y][x] = name
    # Place at least one megalith
    x, y = pick_location()
    map_data[y][x] = "megalith"


def generate_map(width: int, height: int, seed: int | None = None):
    """Generate a map using a simple wave function collapse algorithm."""
    random.seed(seed)
    cells: List[List[Set[str]]] = [
        [set(TILES) for _ in range(width)] for _ in range(height)
    ]

    def collapse_cell(x: int, y: int) -> None:
        choice = random.choice(list(cells[y][x]))
        cells[y][x] = {choice}
        queue = [(x, y)]
        while queue:
            cx, cy = queue.pop(0)
            tile = next(iter(cells[cy][cx]))
            for nx, ny in _neighbors(cx, cy, width, height):
                allowed = ADJACENCY[tile]
                new_opts = cells[ny][nx] & allowed
                if not new_opts:
                    new_opts = set(allowed)
                if new_opts != cells[ny][nx]:
                    cells[ny][nx] = new_opts
                    if len(new_opts) == 1:
                        queue.append((nx, ny))

    while True:
        min_opts = None
        target = None
        for y in range(height):
            for x in range(width):
                options = cells[y][x]
                if len(options) > 1 and (
                    min_opts is None or len(options) < min_opts
                ):
                    min_opts = len(options)
                    target = (x, y)
        if target is None:
            break
        collapse_cell(*target)

    result = [
        [next(iter(cells[y][x])) for x in range(width)] for y in range(height)
    ]
    _place_settlements(result, seed)
    return result


if __name__ == "__main__":
    m = generate_map(10, 10, seed=0)
    for row in m:
        print(" ".join(row))
