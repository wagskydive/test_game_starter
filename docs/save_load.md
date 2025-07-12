# Save and Load System

The `save_load` module provides simple helpers to persist and restore game state using JSON files.

```python
from player import Player
from npc import NPC
from game_map import GameMap
from item import Item
from save_load import save_game, load_game

player = Player(name='Hero')
player.pick_up(Item(name='rock'))
npcs = [NPC(name='Bob')]
game_map = GameMap(width=2, height=2, data=[["plains", "forest"], ["hills", "water"]])

story_state = {'chapter': 1}
save_game('save.json', player, npcs, game_map, story_state)
player2, npcs2, map2, story2 = load_game('save.json')
```

`save_game` writes the player inventory, NPC stats, map data and a `story_state` dictionary to a JSON file. `load_game` reconstructs the objects and returns the story state as well.

