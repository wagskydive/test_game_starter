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
If a `weather_temperature` value is supplied to `tick()`, the NPC's body
temperature will gradually move toward that value.

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

## Schedules

NPCs can define a simple daily schedule mapping periods of the day to
activities. Use `get_activity(hour)` to retrieve the planned activity.

```python
bob = NPC(name="Bob", schedule={"morning": "work", "night": "sleep"})
current = bob.get_activity(8)  # 'work'
```
