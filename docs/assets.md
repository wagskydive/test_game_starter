# Asset Pipeline

**Status:** Asset packs are not yet integrated. Placeholder graphics will be used until runtime downloads are enabled.

Run `python scripts/generate_assets.py` to create placeholder sprites in
`assets/generated`. The script uses the color palette defined in
`palette` and produces layered character images. Replace these with real art as
it becomes available.

## Runtime Asset Downloads

The game can automatically download external Kenney asset packs if they are not
already indexed. File names from each zip are recorded in `assets/asset_index.json`.
Actual art files are removed after indexing so the repository stays lightweight.

Use the helper function `ensure_assets` in `asset_manager`:

```python
from asset_manager import ensure_assets, DEFAULT_ASSETS

# Downloads and indexes the Kenney packs if needed.
ensure_assets(DEFAULT_ASSETS)
```

This will download each pack to a temporary directory, list its contents, store
them in the JSON database and then delete the zip.
