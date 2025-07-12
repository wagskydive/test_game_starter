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
