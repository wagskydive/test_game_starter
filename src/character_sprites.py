from __future__ import annotations
import json
import os
import random
from dataclasses import dataclass
from typing import Optional

from . import asset_manager


@dataclass
class CharacterSprite:
    """Selected sprite layers for a character."""

    body: str
    eyes: str
    hair: str
    clothes: str


def _load_index() -> dict:
    if not os.path.exists(asset_manager.ASSET_DB):
        asset_manager.ensure_assets(asset_manager.DEFAULT_ASSETS)
    if not os.path.exists(asset_manager.ASSET_DB):
        return {}
    with open(asset_manager.ASSET_DB, "r") as f:
        return json.load(f)


def _filter_layers(files: list[str], keyword: str) -> list[str]:
    return [f for f in files if keyword in f.lower()]


def generate_character(random_state: Optional[random.Random] = None) -> CharacterSprite:
    """Return a CharacterSprite by choosing random layers from the asset index."""
    data = _load_index()
    files = data.get("roguelike-characters", [])
    rand = random_state or random

    body_files = _filter_layers(files, "body") or files
    eyes_files = _filter_layers(files, "eyes") or files
    hair_files = _filter_layers(files, "hair") or files
    clothes_files = _filter_layers(files, "clothes") or files

    return CharacterSprite(
        body=rand.choice(body_files) if body_files else "",
        eyes=rand.choice(eyes_files) if eyes_files else "",
        hair=rand.choice(hair_files) if hair_files else "",
        clothes=rand.choice(clothes_files) if clothes_files else "",
    )
