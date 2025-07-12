# Equipment Slots

Items may define an optional `slot` field such as `head`, `torso`, `hand`, or `feet`.
The `Inventory` class tracks equipped items in the `equipment` dictionary.

```python
from src.item import Item, Inventory

inv = Inventory()
helmet = Item(name="helmet", slot="head")
inv.add(helmet)
inv.equip(helmet)
print(inv.equipment["head"])  # helmet
inv.unequip("head")
```

Attempting to equip an item without a slot or not in the inventory raises `ValueError`.
