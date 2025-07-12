# Trading System

`trading.trade` exchanges an item between two NPCs for a price.
Each `NPC` now has an `inventory` and `money` field that can be used for simple
barter.

```python
from npc import NPC
from item import Item
from trading import trade

buyer = NPC(name='Alice', money=10)
seller = NPC(name='Bob', money=0)
item = Item(name='apple')
seller.inventory.add(item)
trade(buyer, seller, item, price=5)
```
