import random
from noise import pnoise2

TILES = [
    ("water", -0.2),
    ("plains", 0.0),
    ("forest", 0.2),
    ("hills", 0.4),
    ("mountains", 1.0),
]


def _tile_from_noise(value: float) -> str:
    for name, threshold in TILES:
        if value < threshold:
            return name
    return TILES[-1][0]


def generate_map(width: int, height: int, seed: int | None = None):
    """Generate a world map using Perlin noise."""
    scale = 10.0
    base = seed if seed is not None else 0
    result = []
    for y in range(height):
        row = []
        for x in range(width):
            value = pnoise2(x / scale, y / scale, base=base)
            row.append(_tile_from_noise(value))
        result.append(row)
    return result


if __name__ == "__main__":
    m = generate_map(10, 10, seed=0)
    for row in m:
        print(" ".join(row))
