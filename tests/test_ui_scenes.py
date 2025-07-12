import os

def test_main_menu_scene_exists():
    assert os.path.isfile(os.path.join('godot', 'scenes', 'MainMenu.tscn'))

def test_inventory_scene_exists():
    assert os.path.isfile(os.path.join('godot', 'scenes', 'Inventory.tscn'))


def test_new_scenes_exist():
    assert os.path.isfile(os.path.join('godot', 'scenes', 'CharacterStats.tscn'))
    assert os.path.isfile(os.path.join('godot', 'scenes', 'Crafting.tscn'))


def test_theme_file_exists():
    assert os.path.isfile(os.path.join('godot', 'assets', 'ui', 'theme.tres'))
