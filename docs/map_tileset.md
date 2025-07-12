# Map Tileset Integration

The `tile_mapping` module links world generation tile names to
sprite files extracted from the **Tiny Town** asset pack.
`load_tile_map()` reads `assets/asset_index.json` and finds matching
sprites using simple keyword searches.

```python
from tile_mapping import load_tile_map

mapping = load_tile_map()
print(mapping["plains"])  # e.g. "terrain/grass.png"
```

This allows the Godot project to display the correct sprite for each
tile produced by `worldgen.generate_map`.
