# Item and Inventory Prototype

The `item` module introduces basic data structures for representing items and a simple inventory container.

## Item

```python
from item import Item
rock = Item(name='rock', weight=2.5)
```

Items have `name`, `weight`, `volume`, and `durability` attributes. Items may
optionally define `max_volume` and hold an internal `Inventory` when used as
containers.

## Inventory

```python
from item import Inventory
inv = Inventory()
inv.add(rock)
```

An `Inventory` can enforce a volume limit by passing `max_volume` when
constructed. Use `can_add(item)` or rely on `add()` raising `ValueError` when the
capacity would be exceeded. Inventories may be nested by storing container items
that themselves have an `Inventory` instance.
