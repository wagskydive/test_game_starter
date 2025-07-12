# NPC Prototype

The `npc` module defines a simple `NPC` dataclass representing a character with health, hunger and thirst values.

## Usage

```python
from npc import NPC

bob = NPC(name="Bob")
print(bob.hunger)  # 100
bob.tick()
print(bob.hunger)  # 99
```

Calling `tick()` decreases the hunger and thirst values but never below zero.
