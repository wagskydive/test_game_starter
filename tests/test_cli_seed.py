import os
import sys
sys.path.insert(0, os.path.abspath('src'))

import main


def test_parse_args_seed():
    args = main.parse_args(['--seed', '123'])
    assert args.seed == 123


def test_parse_args_no_seed():
    args = main.parse_args([])
    assert args.seed is None


def test_main_passes_seed(monkeypatch):
    called = {}

    def fake_generate_map(width, height, seed=None):
        called['seed'] = seed
        return []

    monkeypatch.setattr(main, 'generate_map', fake_generate_map)
    main.main(['--seed', '55'])
    assert called['seed'] == 55
