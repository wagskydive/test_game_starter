# Asset Pipeline

Run `python scripts/generate_assets.py` to create placeholder sprites in
`assets/generated`. Replace these with real art as it becomes available.

## Runtime Asset Downloads

The game can automatically download external Kenney asset packs if they are not
already indexed. File names from each zip are recorded in `assets/asset_index.json`.
Actual art files are removed after indexing so the repository stays lightweight.

Use the helper function `ensure_assets` in `asset_manager`:

```python
from asset_manager import ensure_assets

ASSETS = {
    'tiny-town': 'https://kenney.nl/media/pages/assets/tiny-town/5e46f9e551-1735736916/kenney_tiny-town.zip',
    'roguelike-characters': 'https://kenney.nl/media/pages/assets/roguelike-characters/dbeea49dc8-1729196490/kenney_roguelike-characters.zip',
}

ensure_assets(ASSETS)
```

This will download each pack to a temporary directory, list its contents, store
them in the JSON database and then delete the zip.
