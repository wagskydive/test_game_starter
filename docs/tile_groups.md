# Tile Groups and Destructibility

`tile_groups` defines metadata for world tiles. Each tile has a `destructible`
flag and belongs to a logical group used by the map generator and future game
logic.

Example:

```python
from tile_groups import is_destructible, get_group

is_destructible("megalith")  # False
get_group("castle")  # "settlement"
```
