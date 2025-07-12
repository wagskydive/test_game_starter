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

A small prototype for map generation is available in `src/worldgen.py`. Run it directly to print a 10x10 map:

```bash
python src/worldgen.py
```

