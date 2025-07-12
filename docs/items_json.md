# Item and Recipe JSON Format

Items are defined in `data/items.json` as an array of objects:

```json
{
  "name": "wood",
  "weight": 1.0,
  "volume": 1.0,
  "quality": 0,
  "rarity": "common",
  "impressiveness": 0
}
```

Recipes are defined in `data/recipes.json`:

```json
{
  "name": "iron ingot",
  "ingredients": {"iron ore": 1},
  "result": "iron ingot"
}
```

Use `load_items(path)` and `load_recipes(path, items)` from `item_db` to load these files at runtime.
