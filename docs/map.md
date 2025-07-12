# Map Module

The `game_map` module defines a simple `GameMap` dataclass that stores map data.
It provides helper methods to check if coordinates are within bounds and to
retrieve the tile at a specific position.

```python
from game_map import GameMap
from worldgen import generate_map

raw = generate_map(5, 5, seed=1)
map_obj = GameMap(width=5, height=5, data=raw)
print(map_obj.get_tile(0, 0))
```
