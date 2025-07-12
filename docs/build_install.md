# Build and Install Guide

This project now includes a basic Godot 4 setup under the `godot/` directory.

## Requirements
- Godot 4.x
- Python 3.10+

## Setup Steps
1. Install Python requirements (requires Pillow for asset generation):
   ```bash
   pip install -r requirements.txt
   ```
2. Open the Godot editor and import the project located in the `godot/` folder.
3. Run the main scene (`Main.tscn`) to start the game.

Automated tests for the Python modules can be run using:
```bash
pytest -q
```


**Note:** This project is still in development. Run `python scripts/download_assets.py`
to download the Kenney asset packs if you want to see real graphics instead of
the generated placeholders.
