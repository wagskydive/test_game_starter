import json
import os
from typing import Dict, List

from . import asset_manager

# Keywords used to match Tiny Town tiles to generator tiles
KEYWORDS: Dict[str, List[str]] = {
    "water": ["water"],
    "plains": ["grass", "plain"],
    "forest": ["forest", "tree"],
    "hills": ["hill"],
    "mountains": ["mountain"],
}


def _load_index() -> List[str]:
    if not os.path.exists(asset_manager.ASSET_DB):
        asset_manager.ensure_assets(asset_manager.DEFAULT_ASSETS)
    if not os.path.exists(asset_manager.ASSET_DB):
        return []
    with open(asset_manager.ASSET_DB, "r") as f:
        data = json.load(f)
    return data.get("tiny-town", [])


def load_tile_map() -> Dict[str, str]:
    """Return mapping of worldgen tiles to Tiny Town sprite files."""
    files = _load_index()
    mapping: Dict[str, str] = {}
    for tile, keywords in KEYWORDS.items():
        for file in files:
            low = file.lower()
            if any(k in low for k in keywords):
                mapping[tile] = file
                break
    return mapping
