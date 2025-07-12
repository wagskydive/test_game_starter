# Tickets

## Ticket 1 - Project Setup
- [x] Started
- [x] Coded
- [x] Tested
- [x] Reviewed
- [x] Documented
- Read the design document and create `scripts/project-setup.bat` that:
  - creates a boiler plate project
  - sets up folders (src, scripts, docs, config, tests, logs)
  - installs dependencies and adds them to `requirements.txt`
- Run the project-setup.bat script

## Ticket 2 - Update Agents Instructions
- [x] Started
- [x] Coded
- [x] Tested
- [x] Reviewed
- [x] Documented
- Review the design document and expand `AGENTS.md` with detailed project guidelines and iterative workflow instructions.

## Ticket 3 - Basic World Generator Prototype
- [x] Started
- [x] Coded
- [x] Tested
- [x] Reviewed
- [x] Documented
- Create a Python module `src/worldgen.py` that generates a 2D tile map using Perlin noise.
- Add unit tests under `tests/test_worldgen.py` to validate map dimensions and deterministic output when a seed is provided.


## Ticket 4 - Item and Inventory Prototype
- [x] Started
- [x] Coded
- [x] Tested
- [x] Reviewed
- [x] Documented
- Create `src/item.py` defining an `Item` dataclass with basic stats.
- Add an `Inventory` class for adding/removing items and computing total weight.
- Write unit tests in `tests/test_item.py` for item creation and inventory management.
- Document usage in `docs/item.md`.

## Ticket 5 - Basic NPC Class
- [x] Started
- [x] Coded
- [x] Tested
- [x] Reviewed
- [x] Documented
- Implement `src/npc.py` defining a `NPC` dataclass with health, hunger, and thirst.
- Add a `tick` method to reduce hunger and thirst.
- Write tests in `tests/test_npc.py` for initialization and hunger/thirst reduction.
- Document usage in `docs/npc.md`.

## Ticket 6 - Player Class With Inventory
- [x] Started
- [x] Coded
- [x] Tested
- [x] Reviewed
- [x] Documented
- Implement `src/player.py` as a subclass of `NPC` with an `Inventory` attribute.
- Add a `pick_up` method to move an `Item` into the inventory.
- Create tests in `tests/test_player.py` for inventory interaction and default stats.
- Document usage in `docs/player.md`.

## Ticket 7 - Basic Map and Movement
- [x] Started
- [x] Coded
- [x] Tested
- [x] Reviewed
- [x] Documented
- Add `game_map` module to encapsulate map data with `get_tile` method.
- Extend `NPC` with `x` and `y` coordinates and a `move` method optionally bounded by a map.
- Write tests for movement and map bounds.
- Document map and movement usage.

## Ticket 8 - Basic Crafting System

- [x] Started
- [x] Coded
- [x] Tested
- [x] Reviewed
- [x] Documented
- Implement `src/crafting.py` with a `Recipe` dataclass and a `craft` function that consumes ingredients from an `Inventory` and returns the crafted `Item`.
- Add tests in `tests/test_crafting.py` for crafting success and failure when materials are missing.
- Document usage in `docs/crafting.md` and update `README.md`.

## Ticket 9 - Save and Load System
- [ ] Started
- [ ] Coded
- [ ] Tested
- [ ] Reviewed
- [ ] Documented
- Implement `src/save_load.py` with functions to save and load game state as JSON.
- Include player inventory, NPC stats, and map data in the saved state.
- Add tests in `tests/test_save_load.py` to verify round-trip integrity.
- Document usage in `docs/save_load.md`.


## Ticket 10 - CLI Seed Input
- [ ] Started
- [ ] Coded
- [ ] Tested
- [ ] Reviewed
- [ ] Documented
- Add command line option to set world generation seed when launching the game.
- Implement argument parsing in `src/main.py` or a new module.
- Write tests in `tests/test_cli_seed.py` for argument handling.
- Document usage in `docs/cli_seed.md`.


## Ticket 11 - Logging Utility
- [ ] Started
- [ ] Coded
- [ ] Tested
- [ ] Reviewed
- [ ] Documented
- Create a logging utility in `src/logging_util.py` for consistent game logging.
- Allow configurable log levels and output file path.
- Write tests in `tests/test_logging_util.py` for log creation and formatting.
- Document usage in `docs/logging_util.md`.


## Ticket 12 - Basic UI Setup
- [ ] Started
- [ ] Coded
- [ ] Tested
- [ ] Reviewed
- [ ] Documented
- Establish initial UI scene in Godot with placeholder buttons and panels.
- Include a simple main menu and inventory screen layout.
- Add tests using Godot's test framework if possible or provide manual steps.
- Document UI setup in `docs/ui.md`.

## Ticket 13 - NPC Pathfinding Prototype
- [ ] Started
- [ ] Coded
- [ ] Tested
- [ ] Reviewed
- [ ] Documented
- Implement simple A* pathfinding in `src/pathfinding.py` for NPC movement.
- Integrate pathfinding into `NPC.move` when a path is required.
- Add tests in `tests/test_pathfinding.py` for path generation and obstacles.
- Document in `docs/pathfinding.md`.
