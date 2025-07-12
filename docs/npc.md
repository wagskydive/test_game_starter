# NPC Prototype

The `npc` module defines a simple `NPC` dataclass representing a character with
health, hunger and thirst values. NPCs also track `temperature`, `wounds` and
`diseases` which lower health during `tick()`. The `impressiveness` field
represents social standing and changes when `adjust_status()` is called.

## Usage

```python
from npc import NPC

bob = NPC(name="Bob")
print(bob.hunger)  # 100
bob.tick()
print(bob.hunger)  # 99
```

Calling `tick()` decreases the hunger and thirst values but never below zero.

## Movement

NPCs track their position with `x` and `y` coordinates and can be moved using
`move(dx, dy)`. When a `GameMap` is supplied, movement will be restricted to its
bounds.

```python
from game_map import GameMap
from worldgen import generate_map

world = GameMap(5, 5, generate_map(5, 5))
bob.move(1, 0, world)
print(bob.x, bob.y)
```
