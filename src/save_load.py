"""Utility functions to save and load game state as JSON."""

from __future__ import annotations

import json
from typing import List, Tuple

from player import Player
from npc import NPC
from item import Item
from game_map import GameMap


def _item_to_dict(item: Item) -> dict:
    return {
        "name": item.name,
        "weight": item.weight,
        "volume": item.volume,
        "durability": item.durability,
    }


def _item_from_dict(data: dict) -> Item:
    return Item(
        name=data["name"],
        weight=data.get("weight", 0.0),
        volume=data.get("volume", 0.0),
        durability=data.get("durability", 100),
    )


def save_game(path: str, player: Player, npcs: List[NPC], game_map: GameMap) -> None:
    """Save the provided game state to ``path`` in JSON format."""
    data = {
        "player": {
            "name": player.name,
            "health": player.health,
            "hunger": player.hunger,
            "thirst": player.thirst,
            "x": player.x,
            "y": player.y,
            "inventory": [_item_to_dict(i) for i in player.inventory.items],
        },
        "npcs": [
            {
                "name": n.name,
                "health": n.health,
                "hunger": n.hunger,
                "thirst": n.thirst,
                "x": n.x,
                "y": n.y,
            }
            for n in npcs
        ],
        "map": {
            "width": game_map.width,
            "height": game_map.height,
            "data": game_map.data,
        },
    }
    with open(path, "w") as f:
        json.dump(data, f)


def load_game(path: str) -> Tuple[Player, List[NPC], GameMap]:
    """Load the game state from ``path`` and return objects."""
    with open(path) as f:
        data = json.load(f)

    p_data = data["player"]
    player = Player(
        name=p_data["name"],
        health=p_data.get("health", 100),
        hunger=p_data.get("hunger", 100),
        thirst=p_data.get("thirst", 100),
        x=p_data.get("x", 0),
        y=p_data.get("y", 0),
    )
    for item_data in p_data.get("inventory", []):
        player.pick_up(_item_from_dict(item_data))

    npcs = [
        NPC(
            name=n["name"],
            health=n.get("health", 100),
            hunger=n.get("hunger", 100),
            thirst=n.get("thirst", 100),
            x=n.get("x", 0),
            y=n.get("y", 0),
        )
        for n in data.get("npcs", [])
    ]

    m_data = data["map"]
    game_map = GameMap(m_data["width"], m_data["height"], m_data["data"])

    return player, npcs, game_map

