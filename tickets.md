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
- [x] Started
- [x] Coded
- [x] Tested
- [x] Reviewed
- [x] Documented
- Implement `src/save_load.py` with functions to save and load game state as JSON.
- Include player inventory, NPC stats, and map data in the saved state.
- Add tests in `tests/test_save_load.py` to verify round-trip integrity.
- Document usage in `docs/save_load.md`.


## Ticket 10 - CLI Seed Input
- [x] Started
- [x] Coded
- [x] Tested
  - [x] Reviewed
  - [x] Documented
- Add command line option to set world generation seed when launching the game.
- Implement argument parsing in `src/main.py` or a new module.
- Write tests in `tests/test_cli_seed.py` for argument handling.
- Document usage in `docs/cli_seed.md`.


## Ticket 11 - Logging Utility
- [x] Started
- [x] Coded
- [x] Tested
- [x] Reviewed
- [x] Documented
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
- [x] Started
- [x] Coded
- [x] Tested
- [ ] Reviewed
- [x] Documented
- Implement simple A* pathfinding in `src/pathfinding.py` for NPC movement.
- Integrate pathfinding into `NPC.move` when a path is required.
- Add tests in `tests/test_pathfinding.py` for path generation and obstacles.
- Document in `docs/pathfinding.md`.
## Ticket 14 - Settlements and Ruins Generation
- [ ] Started
- [ ] Coded
- [ ] Tested
- [ ] Reviewed
- [ ] Documented
- Extend `worldgen` with placement of villages, castles, ruins and trade posts.
- Include special "megalith" tiles that are mostly indestructible.
- Write tests ensuring settlements appear when a seed is used.
- Document in `docs/worldgen_settlements.md`.

## Ticket 15 - Destructible Tiles and Grouping
- [ ] Started
- [ ] Coded
- [ ] Tested
- [ ] Reviewed
- [ ] Documented
- Add support for marking tiles as destructible or permanent.
- Implement grouping of tiles into structures (houses, mountains, ships).
- Update tests to cover new attributes and grouping behavior.
- Document in `docs/tile_groups.md`.

## Ticket 16 - Expanded Item Definitions
- [ ] Started
- [ ] Coded
- [ ] Tested
- [ ] Reviewed
- [ ] Documented
- Move item and recipe data to JSON files loaded at runtime.
- Include base and intermediate materials from the design document.
- Add fields for quality, rarity and impressiveness.
- Document format in `docs/items_json.md`.

## Ticket 17 - Equipment Slots
- [ ] Started
- [ ] Coded
- [ ] Tested
- [ ] Reviewed
- [ ] Documented
- Extend `Item` and `Inventory` to handle equip slots (hand, head, torso, feet, etc.).
- Provide tests for equipping and unequipping items.
- Document in `docs/equipment.md`.

## Ticket 18 - Basic Combat System
- [x] Started
- [x] Coded
- [x] Tested
- [x] Reviewed
- [x] Documented
- Create combat functions for melee and ranged attacks using item stats.
- Track health reduction and simple hit chance.
- Add unit tests for combat calculations.
- Document usage in `docs/combat.md`.

## Ticket 19 - NPC Needs System
- [x] Started
- [x] Coded
- [x] Tested
- [x] Reviewed
- [x] Documented
- Expand NPC class with needs for rest, safety, social and status.
- Implement periodic decay and satisfaction methods.
- Add tests verifying needs update over time.
- Document in `docs/npc_needs.md`.

## Ticket 20 - NPC Personalities and Factions
- [x] Started
- [x] Coded
- [x] Tested
- [x] Reviewed
- [x] Documented
- Add personality traits and emotional states to NPCs.
- Implement simple faction/group membership.
- Provide tests for trait assignment and group storage.
- Document in `docs/npc_personality.md`.

## Ticket 21 - Basic AI Behaviors
- [x] Started
- [x] Coded
- [x] Tested
- [x] Reviewed
- [x] Documented
- Introduce behavior routines such as wandering, working and socializing.
- Use pathfinding to move toward goals or resources.
- Add unit tests for behavior selection logic.
- Document in `docs/ai_behavior.md`.

## Ticket 22 - Story Anchor Framework
- [x] Started
- [x] Coded
- [x] Tested
- [x] Reviewed
- [x] Documented
- Create data structures for hard and soft story goals.
- Implement an event system that triggers anchors based on world state.
- Write tests for anchor activation logic.
- Document in `docs/story_anchors.md`.

## Ticket 23 - LLM Storytelling Integration
- [x] Started
- [x] Coded
- [x] Tested
- [x] Reviewed
- [x] Documented
- Set up a stub interface for optional LLM-driven dialogue and quests.
- Allow disabling LLM features when no model is present.
- Add basic unit tests with mocked responses.
- Document setup in `docs/llm_integration.md`.

## Ticket 24 - Expanded Save/Load
- [x] Started
- [x] Coded
- [x] Tested
- [x] Reviewed
- [x] Documented
- Extend the save system to include story state and NPC factions.
- Ensure backward compatibility with existing saves.
- Write tests for the new data fields.
- Update documentation in `docs/save_load.md`.

## Ticket 25 - UI Inventory and Menu Screens
- [x] Started
- [x] Coded
- [x] Tested
- [x] Reviewed
- [x] Documented
- Build Godot scenes for inventory management and a main menu.
- Hook up the Player inventory to display item icons.
- Provide manual test steps until automated UI tests are in place.
- Document in `docs/ui_inventory.md`.

## Ticket 26 - Asset Pipeline Setup
- [x] Started
- [x] Coded
- [x] Tested
- [x] Reviewed
- [x] Documented
- Create script for generating placeholder sprites via Stable Diffusion or OpenGameArt assets.
- Organize assets under an `assets/` directory with subfolders for tiles and characters.
- Document the asset workflow in `docs/assets.md`.

## Ticket 27 - Modding Support Basics
- [x] Started
- [x] Coded
- [x] Tested
- [x] Reviewed
- [x] Documented
- Define a mod loading system for custom items and maps via JSON packages.
- Provide example mod files and loading logic.
- Add tests for mod discovery and parsing.
- Document usage in `docs/modding.md`.

## Ticket 28 - Advanced Logging Options
- [x] Started
- [x] Coded
- [x] Tested
- [x] Reviewed
- [x] Documented
- Enhance `logging_util` with log rotation and console output.
- Allow configuration via a file or environment variables.
- Add tests covering new logging features.
- Update documentation in `docs/logging_util.md`.

## Ticket 29 - NPC Health Extensions
- [ ] Started
- [ ] Coded
- [ ] Tested
- [ ] Reviewed
- [ ] Documented
- Add temperature, wound and disease tracking to `NPC`.
- Include healing mechanics and tests for damage over time.

## Ticket 30 - Social Status and Impressiveness
- [ ] Started
- [ ] Coded
- [ ] Tested
- [ ] Reviewed
- [ ] Documented
- Implement `impressiveness` stat affecting NPC reactions.
- Track social status changes through actions and items.

## Ticket 31 - Crafting Stations
- [ ] Started
- [ ] Coded
- [ ] Tested
- [ ] Reviewed
- [ ] Documented
- Add station classes such as `Anvil`, `Firepit`, `Loom`, and `Kiln`.
- Require appropriate station for certain recipes.

## Ticket 32 - Blueprints and Skill Requirements
- [ ] Started
- [ ] Coded
- [ ] Tested
- [ ] Reviewed
- [ ] Documented
- Introduce blueprint items and crafting skill levels.
- Some recipes require blueprints or high skill to craft.

## Ticket 33 - Reinforcement Learning NPCs
- [ ] Started
- [ ] Coded
- [ ] Tested
- [ ] Reviewed
- [ ] Documented
- Prototype RL-based training for selected NPC behaviors.

## Ticket 34 - Faction Goals and Group AI
- [ ] Started
- [ ] Coded
- [ ] Tested
- [ ] Reviewed
- [ ] Documented
- Give factions group objectives and simple coordination logic.

## Ticket 35 - Offline LLM Integration
- [ ] Started
- [ ] Coded
- [ ] Tested
- [ ] Reviewed
- [ ] Documented
- Support running an offline model via the Godot-LLM plugin.

## Ticket 36 - Procedural Quest Generator
- [ ] Started
- [ ] Coded
- [ ] Tested
- [ ] Reviewed
- [ ] Documented
- Generate quests procedurally when no LLM is available.

## Ticket 37 - Godot Project Skeleton
- [ ] Started
- [ ] Coded
- [ ] Tested
- [ ] Reviewed
- [ ] Documented
- Add a basic Godot project with scenes and integrate Python modules.

## Ticket 38 - NPC Animation States
- [ ] Started
- [ ] Coded
- [ ] Tested
- [ ] Reviewed
- [ ] Documented
- Implement animations for idle, walk, angry, excited and sitting.

## Ticket 39 - Art Palette and Layered Sprites
- [ ] Started
- [ ] Coded
- [ ] Tested
- [ ] Reviewed
- [ ] Documented
- Define a common color palette and layered sprite format.
- Update asset pipeline to generate placeholder layers.

## Ticket 40 - UI Style Pass and New Screens
- [ ] Started
- [ ] Coded
- [ ] Tested
- [ ] Reviewed
- [ ] Documented
- Apply consistent styling to menus and inventory.
- Add screens for character stats and crafting.

## Ticket 41 - Weather and Seasons Simulation
- [ ] Started
- [ ] Coded
- [ ] Tested
- [ ] Reviewed
- [ ] Documented
- Simulate weather patterns and seasonal effects on temperature.

## Ticket 42 - Trading and Economy System
- [ ] Started
- [ ] Coded
- [ ] Tested
- [ ] Reviewed
- [ ] Documented
- Implement a currency and trading mechanics with NPCs.

## Ticket 43 - NPC Families and Relationships
- [ ] Started
- [ ] Coded
- [ ] Tested
- [ ] Reviewed
- [ ] Documented
- Track familial ties and friendships between NPCs.

## Ticket 44 - Advanced Pathfinding
- [ ] Started
- [ ] Coded
- [ ] Tested
- [ ] Reviewed
- [ ] Documented
- Add avoidance and dynamic obstacle handling to pathfinding.

## Ticket 45 - Nested Containers and Volume
- [ ] Started
- [ ] Coded
- [ ] Tested
- [ ] Reviewed
- [ ] Documented
- Support containers within containers and volume-based limits.

## Ticket 46 - Documentation Diagrams
- [ ] Started
- [ ] Coded
- [ ] Tested
- [ ] Reviewed
- [ ] Documented
- Provide flowcharts for worldgen, crafting, and story anchors.

## Ticket 47 - NPC Daily Schedules
- [ ] Started
- [ ] Coded
- [ ] Tested
- [ ] Reviewed
- [ ] Documented
- Give NPCs schedules for work, rest and social activities.

## Ticket 48 - Day/Night Cycle and Energy
- [ ] Started
- [ ] Coded
- [ ] Tested
- [ ] Reviewed
- [ ] Documented
- Implement a day/night cycle and energy stat affecting actions.


## Ticket 49 - Planning Document
- [x] Started
- [x] Coded
- [x] Tested
- [x] Reviewed
- [x] Documented
- Create planning.md summarizing completed features and future milestones.
