# World Generation

The `worldgen` module provides a simple prototype for generating a 2D tile map.
It uses the [`noise`](https://pypi.org/project/noise/) library to produce Perlin noise and maps the values to terrain types.

## Usage

```python
from worldgen import generate_map

map_data = generate_map(width=10, height=10, seed=42)
```

When a seed is supplied the output is deterministic. Each element in the returned list corresponds to a tile name such as `water`, `plains` or `mountains`.

Run the module directly to see a small map printed to the console:

```bash
python src/worldgen.py
```
