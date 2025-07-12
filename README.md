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

It also ensures `requirements.txt` exists with required packages and installs them. The initial dependencies are `pytest` for testing and `noise` for map generation.

To execute the automated tests:

```bash
pytest -q
```

### World Generation Prototype

A small prototype for map generation is available in `src/worldgen.py`. It is documented in more detail under [`docs/worldgen.md`](docs/worldgen.md). Run the module directly to print a 10x10 map:

```bash
python src/worldgen.py
```


### Item and Inventory Prototype

The `item` module provides an `Item` dataclass and `Inventory` container. See [docs/item.md](docs/item.md) for details.

