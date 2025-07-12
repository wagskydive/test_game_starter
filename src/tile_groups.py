from dataclasses import dataclass
from typing import Dict

@dataclass(frozen=True)
class TileInfo:
    name: str
    destructible: bool
    group: str

TILES: Dict[str, TileInfo] = {
    "water": TileInfo("water", False, "water"),
    "plains": TileInfo("plains", True, "land"),
    "forest": TileInfo("forest", True, "land"),
    "hills": TileInfo("hills", True, "land"),
    "mountains": TileInfo("mountains", False, "mountain"),
    "village": TileInfo("village", True, "settlement"),
    "castle": TileInfo("castle", True, "settlement"),
    "ruins": TileInfo("ruins", True, "settlement"),
    "trade_post": TileInfo("trade_post", True, "settlement"),
    "megalith": TileInfo("megalith", False, "megalith"),
}

def is_destructible(tile: str) -> bool:
    return TILES.get(tile, TileInfo(tile, True, "misc")).destructible


def get_group(tile: str) -> str:
    return TILES.get(tile, TileInfo(tile, True, "misc")).group
