import json
import os
from dataclasses import dataclass
from typing import List


@dataclass
class Mod:
    name: str
    items: List[dict]
    maps: List[dict]


MOD_DIR = os.path.join(os.path.dirname(__file__), '..', 'mods')


def discover_mods() -> List[Mod]:
    mods = []
    if not os.path.isdir(MOD_DIR):
        return mods
    for fname in os.listdir(MOD_DIR):
        if not fname.endswith('.json'):
            continue
        with open(os.path.join(MOD_DIR, fname)) as f:
            data = json.load(f)
        mods.append(Mod(name=data.get('name', fname), items=data.get('items', []), maps=data.get('maps', [])))
    return mods
