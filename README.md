# Game Starter Project

This repository begins the setup for the procedural RPG described in `design.md`.

## Setup

Run the setup script to create the project structure and install Python dependencies:

```bash
bash scripts/project-setup.bat
```

This will create the following directories:

- `src`
- `scripts`
- `docs`
- `config`
- `tests`
- `logs`

It also ensures `requirements.txt` exists with required packages and installs them. The initial dependency is `pytest` for testing.

To execute the automated tests:

```bash
pytest -q
```

## Godot Project

A minimal Godot 4 project is provided under the `godot/` directory. Import this
folder using the Godot editor to run the game. See
[docs/build_install.md](docs/build_install.md) for details on requirements and
build steps.

### World Generation Prototype

A small prototype for map generation is available in `src/worldgen.py`. It uses a basic wave function collapse algorithm and is documented in more detail under [`docs/worldgen.md`](docs/worldgen.md). Run the module directly to print a 10x10 map:

```bash
python src/worldgen.py
```
Tile metadata such as destructibility is defined in
[docs/tile_groups.md](docs/tile_groups.md).


### Item and Inventory Prototype

The `item` module provides an `Item` dataclass and `Inventory` container. See [docs/item.md](docs/item.md) for details.
Items and crafting recipes can be loaded from JSON using `item_db`. Example files live in the `data/` directory and the format is documented in [docs/items_json.md](docs/items_json.md).
Inventories also support equipment slots as described in [docs/equipment.md](docs/equipment.md).


### NPC Prototype

A minimal NPC class is defined in `src/npc.py` with health, hunger, and thirst attributes. See [docs/npc.md](docs/npc.md) for usage.

### Map and Movement

The `game_map` module defines a `GameMap` class used for simple bounds checking.
`NPC` objects now track `x` and `y` coordinates and can be moved with the
`move()` method.
See [docs/map.md](docs/map.md) for details.

### Player Prototype

The `player` module provides a `Player` class that inherits from `NPC` and includes an `Inventory`. See [docs/player.md](docs/player.md) for usage.

### Crafting Prototype

The `crafting` module defines simple recipes and a `craft` function to combine items in an inventory. See [docs/crafting.md](docs/crafting.md) for usage.


### Pathfinding Prototype

The `pathfinding` module provides A* search used by `NPC.move`. It supports
optional `avoid` tiles with higher movement cost and a dynamic `is_blocked`
callback for temporary obstacles. See [docs/pathfinding.md](docs/pathfinding.md)
for details.
=======
### Logging Utility

Use `logging_util.create_logger` to create loggers for the game. See [docs/logging_util.md](docs/logging_util.md) for details.
=======
### CLI Seed Option

`src/main.py` includes a command line argument for setting the world generation seed. See [docs/cli_seed.md](docs/cli_seed.md) for usage.
=======

### Save and Load System

The `save_load` module saves the player's state, NPCs and map data to a JSON file and reloads it later. See [docs/save_load.md](docs/save_load.md) for details.

### Combat Prototype

The `combat` module implements simple melee and ranged attack helpers. Damage
is based on the attacking item's weight and reduces the weapon's durability.
See [docs/combat.md](docs/combat.md) for usage.

### Trading System

NPCs have an `inventory` and `money` field. Use `trading.trade` to exchange
items between characters for a price. See [docs/trading.md](docs/trading.md)
for details.

### NPC Needs and Personality

`NPC` now includes additional needs, personality traits and relationship
tracking. See [docs/npc_needs.md](docs/npc_needs.md),
[docs/npc_personality.md](docs/npc_personality.md) and
[docs/npc_relationships.md](docs/npc_relationships.md).
`animation_state` tracks simple animations such as walking or sitting.
See [docs/npc_animation.md](docs/npc_animation.md).

### AI Behaviors and Story Anchors

Basic behavior selection is provided in `ai_behavior` and simple story anchors
are implemented in `story_anchors`. See [docs/ai_behavior.md](docs/ai_behavior.md)
and [docs/story_anchors.md](docs/story_anchors.md).
Anchors can run an `on_trigger` callback when activated.
`Faction` groups provide simple shared goals for NPCs. See
[docs/faction.md](docs/faction.md).
Use `generate_quest` from `procedural_quests` for simple quest generation when
no LLM is available. See [docs/procedural_quests.md](docs/procedural_quests.md).

### RL Training Prototype

`rl_training.RLTrainer` provides a minimal Q-learning helper used for
experimental NPC training. See [docs/rl_training.md](docs/rl_training.md) for
details.

### Modding and Assets

Mods can be placed under `mods/` and loaded using `modding.discover_mods`. Run
`scripts/generate_assets.py` to create placeholder assets. See
The helper in `asset_manager.ensure_assets` downloads Kenney asset packs (environment, characters and UI) at runtime and saves only their file names in `assets/asset_index.json`. Use `asset_manager.DEFAULT_ASSETS` for the default pack URLs.
[docs/modding.md](docs/modding.md) and [docs/assets.md](docs/assets.md).
`character_sprites.generate_character` builds a basic appearance by selecting
sprite layers from the indexed `roguelike-characters` pack. See
[docs/character_sprites.md](docs/character_sprites.md).
The placeholder asset generator uses a simple color palette defined in
`palette` to create layered sprites. See [docs/art_palette.md](docs/art_palette.md).
`tile_mapping.load_tile_map` resolves tiles from the world generator to sprite files
in the Tiny Town pack. See [docs/map_tileset.md](docs/map_tileset.md).
See [docs/ui.md](docs/ui.md) for the UI setup including themed menus,
character stats and crafting screens.

### LLM Integration

Use `generate_dialogue` from `llm_integration` for optional text generation.
Set `DISABLE_LLM=1` to disable the feature or call `load_offline_model` to use a
local model. See [docs/llm_integration.md](docs/llm_integration.md).


### Weather and Seasons

Use the `WeatherSystem` module to cycle seasons every 30 days and pick random weather. See [docs/weather.md](docs/weather.md).
NPCs can be affected by weather by passing `WeatherSystem.temperature` to `NPC.tick()`.

### Day and Night Cycle

`time_cycle.TimeSystem` tracks the current hour. Advance time with
`advance_hour()` and use `NPC.energy` with `tick()` to model fatigue.
