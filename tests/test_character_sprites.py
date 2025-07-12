import os
import json
import random
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src import character_sprites, asset_manager


def test_generate_character_uses_asset_db(tmp_path, monkeypatch):
    db_path = tmp_path / "assets.json"
    data = {
        "roguelike-characters": [
            "body/base.png",
            "eyes/eyes1.png",
            "hair/hair1.png",
            "clothes/shirt1.png",
        ]
    }
    with open(db_path, "w") as f:
        json.dump(data, f)

    monkeypatch.setenv("ASSET_DB", str(db_path))

    from importlib import reload

    asset_manager_reloaded = reload(asset_manager)
    character_sprites_reloaded = reload(character_sprites)

    char = character_sprites_reloaded.generate_character(
        random_state=random.Random(0)
    )

    assert char.body == "body/base.png"
    assert char.eyes == "eyes/eyes1.png"
    assert char.hair == "hair/hair1.png"
    assert char.clothes == "clothes/shirt1.png"
