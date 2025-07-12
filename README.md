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


### Item and Inventory Prototype

The `item` module provides an `Item` dataclass and `Inventory` container. See [docs/item.md](docs/item.md) for details.


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

The `pathfinding` module provides simple A* search used by `NPC.move` when a
target is supplied. See [docs/pathfinding.md](docs/pathfinding.md) for details.
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

### NPC Needs and Personality

`NPC` now includes additional needs and personality traits. See
[docs/npc_needs.md](docs/npc_needs.md) and
[docs/npc_personality.md](docs/npc_personality.md).

### AI Behaviors and Story Anchors

Basic behavior selection is provided in `ai_behavior` and simple story anchors
are implemented in `story_anchors`. See [docs/ai_behavior.md](docs/ai_behavior.md)
and [docs/story_anchors.md](docs/story_anchors.md).

### Modding and Assets

Mods can be placed under `mods/` and loaded using `modding.discover_mods`. Run
`scripts/generate_assets.py` to create placeholder assets. See
[docs/modding.md](docs/modding.md) and [docs/assets.md](docs/assets.md).

### LLM Integration

Use `generate_dialogue` from `llm_integration` for optional text generation.
Set `DISABLE_LLM=1` to disable the feature. See [docs/llm_integration.md](docs/llm_integration.md).


