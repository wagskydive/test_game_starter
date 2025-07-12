import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src import main


def test_parse_args_seed():
    args = main.parse_args(['--seed', '123'])
    assert args.seed == 123


def test_parse_args_map_size():
    args = main.parse_args(['--width', '20', '--height', '15'])
    assert args.width == 20
    assert args.height == 15


def test_parse_args_no_seed():
    args = main.parse_args([])
    assert args.seed is None


def test_main_passes_seed(monkeypatch):
    called = {}

    def fake_generate_map(width, height, seed=None):
        called['seed'] = seed
        called['width'] = width
        called['height'] = height
        return []

    monkeypatch.setattr(main, 'generate_map', fake_generate_map)
    main.main(['--seed', '55'])
    assert called['seed'] == 55
    assert called['width'] == 10
    assert called['height'] == 10


def test_main_passes_map_size(monkeypatch):
    called = {}

    def fake_generate_map(width, height, seed=None):
        called['width'] = width
        called['height'] = height
        called['seed'] = seed
        return []

    monkeypatch.setattr(main, 'generate_map', fake_generate_map)
    main.main(['--width', '12', '--height', '8'])
    assert called['width'] == 12
    assert called['height'] == 8
    assert called['seed'] is None
