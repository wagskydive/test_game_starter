# World Generation

The `worldgen` module provides a simple prototype for generating a 2D tile map.
It uses a lightweight **wave function collapse** algorithm to arrange tiles according to adjacency rules.

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
