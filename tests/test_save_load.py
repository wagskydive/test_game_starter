import os
import sys
sys.path.insert(0, os.path.abspath('src'))

from player import Player
from item import Item
from npc import NPC
from game_map import GameMap
from save_load import save_game, load_game


def test_save_load_round_trip(tmp_path):
    player = Player(name='Hero')
    player.pick_up(Item(name='rock', weight=1.0))
    npcs = [NPC(name='Bob', health=80, hunger=90, thirst=90, x=1, y=1, faction='villagers')]
    map_data = [['plains', 'forest'], ['hills', 'water']]
    game_map = GameMap(2, 2, map_data)
    story_state = {'chapter': 1}

    path = tmp_path / 'save.json'
    save_game(path, player, npcs, game_map, story_state)

    loaded_player, loaded_npcs, loaded_map, loaded_story = load_game(path)

    assert loaded_player.name == player.name
    assert len(loaded_player.inventory.items) == 1
    assert loaded_player.inventory.items[0].name == 'rock'
    assert loaded_npcs[0].name == npcs[0].name
    assert loaded_npcs[0].faction == 'villagers'
    assert loaded_map.data == map_data
    assert loaded_story == story_state
