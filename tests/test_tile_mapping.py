import os
import json
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src import tile_mapping, asset_manager


def test_load_tile_map(tmp_path, monkeypatch):
    db_path = tmp_path / "assets.json"
    data = {
        "tiny-town": [
            "terrain/water.png",
            "terrain/grass.png",
            "terrain/forest.png",
            "terrain/hills.png",
            "terrain/mountain.png",
        ]
    }
    with open(db_path, "w") as f:
        json.dump(data, f)

    monkeypatch.setenv("ASSET_DB", str(db_path))

    from importlib import reload

    asset_manager_reloaded = reload(asset_manager)
    tile_mapping_reloaded = reload(tile_mapping)

    mapping = tile_mapping_reloaded.load_tile_map()

    assert mapping == {
        "water": "terrain/water.png",
        "plains": "terrain/grass.png",
        "forest": "terrain/forest.png",
        "hills": "terrain/hills.png",
        "mountains": "terrain/mountain.png",
    }
