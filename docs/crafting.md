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

Recipes may also require a specific crafting station:

```python
from crafting_stations import Anvil

sword_recipe = Recipe(
    ingredients={'ingot': 1, 'stick': 1},
    result=Item(name='sword'),
    station=Anvil,
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

If a recipe specifies a `station`, pass an instance of that station to `craft`:

```python
from crafting_stations import Anvil
new_item = craft(inv, sword_recipe, station=Anvil())
```

Recipes can also require a blueprint item in the inventory and a minimum
`crafting_skill` on the crafting character. Provide the crafter via the
`crafter` argument:

```python
blueprint = Item(name='sword blueprint', is_blueprint=True)
inv.add(blueprint)
advanced_recipe = Recipe(
    ingredients={'ingot': 2},
    result=Item(name='longsword'),
    station=Anvil,
    blueprint='sword blueprint',
    skill_required=5,
)
player.crafting_skill = 5
new_item = craft(inv, advanced_recipe, station=Anvil(), crafter=player)
```
