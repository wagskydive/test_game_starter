# Item and Inventory Prototype

The `item` module introduces basic data structures for representing items and a simple inventory container.

## Item

```python
from item import Item
rock = Item(name='rock', weight=2.5)
```

Items have `name`, `weight`, `volume`, and `durability` attributes.

## Inventory

```python
from item import Inventory
inv = Inventory()
inv.add(rock)
```

The inventory holds `Item` objects and can report the total weight of its contents using `total_weight()`.
