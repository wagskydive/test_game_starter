import os


def test_godot_project_exists():
    assert os.path.isfile(os.path.join('godot', 'project.godot'))


def test_main_scene_exists():
    assert os.path.isfile(os.path.join('godot', 'scenes', 'Main.tscn'))

