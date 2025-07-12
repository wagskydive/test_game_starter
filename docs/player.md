# Player Prototype

The `player` module defines a `Player` class that extends `NPC`. NPCs already
contain an `inventory` and `money` attribute used for trading.

## Usage

```python
from player import Player
from item import Item

hero = Player(name="Hero")
rock = Item(name="rock", weight=2.0)
hero.pick_up(rock)
print(hero.inventory.total_weight())  # 2.0
```
