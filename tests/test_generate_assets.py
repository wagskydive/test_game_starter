import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts import generate_assets


def test_generate_assets_creates_layers(tmp_path, monkeypatch):
    monkeypatch.setattr(generate_assets, 'ASSET_DIR', tmp_path)
    generate_assets.generate()
    expected = ['tile.png', 'body.png', 'eyes.png', 'hair.png', 'clothes.png']
    for name in expected:
        assert (tmp_path / name).exists()
