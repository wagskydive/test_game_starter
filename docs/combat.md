# Combat Prototype

The `combat` module provides very simple attack helpers.
Damage is derived from the attacking item weight and each strike reduces
weapon durability by one.

## Usage

```python
from npc import NPC
from item import Item
from combat import melee_attack, ranged_attack

attacker = NPC(name="Hero")
defender = NPC(name="Goblin")
weapon = Item(name="sword", weight=5.0)

# Force a melee attack
hit = melee_attack(attacker, defender, weapon)
if hit:
    print(defender.health)
```
```

