# Crafting Prototype

The `crafting` module introduces a minimal recipe system for combining items in an `Inventory` into a new `Item`.

## Recipe

```python
from crafting import Recipe
from item import Item

axe_recipe = Recipe(
    ingredients={'wood': 1, 'stone': 1},
    result=Item(name='axe')
)
```

## Craft Function

```python
from crafting import craft
from item import Inventory

inv = Inventory()
# add ingredients
inv.add(Item(name='wood'))
inv.add(Item(name='stone'))
new_item = craft(inv, axe_recipe)
```

When all ingredients are present, `craft` removes them from the `Inventory` and returns the crafted item which is also added to the inventory. If ingredients are missing, it returns `None` and the inventory is unchanged.
