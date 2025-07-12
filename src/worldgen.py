import random
from typing import List, Set, Tuple

# Adjacency rules for tiles used by the wave function collapse algorithm
ADJACENCY = {
    "water": {"water", "plains"},
    "plains": {"water", "plains", "forest", "hills"},
    "forest": {"plains", "forest"},
    "hills": {"plains", "hills", "mountains"},
    "mountains": {"hills", "mountains"},
}
TILES = list(ADJACENCY.keys())


def _neighbors(x: int, y: int, width: int, height: int) -> List[Tuple[int, int]]:
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
                if len(options) > 1 and (min_opts is None or len(options) < min_opts):
                    min_opts = len(options)
                    target = (x, y)
        if target is None:
            break
        collapse_cell(*target)

    result = [[next(iter(cells[y][x])) for x in range(width)] for y in range(height)]
    return result


if __name__ == "__main__":
    m = generate_map(10, 10, seed=0)
    for row in m:
        print(" ".join(row))
