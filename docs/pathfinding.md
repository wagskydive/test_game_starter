# Pathfinding Prototype

The `pathfinding` module implements a very small A* search over a `GameMap`.
It returns a list of coordinates from a start to a goal position. Obstacles can
be provided as a set of blocked coordinates. Tiles in an `avoid` set are treated
with higher movement cost so paths will try to go around them. A dynamic
`is_blocked` callback can be supplied to check temporary obstacles during
search.

```python
from pathfinding import find_path
from game_map import GameMap

m = GameMap(3, 1, [['.', '.', '.']])
path = find_path((0, 0), (2, 0), m)
print(path)  # [(0, 0), (1, 0), (2, 0)]
```

`NPC.move` accepts a `target` position and will use `find_path` to move one step
toward it when a `GameMap` is provided.
