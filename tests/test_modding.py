import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.modding import discover_mods


def test_discover_mods(tmp_path, monkeypatch):
    mod_dir = tmp_path / 'mods'
    mod_dir.mkdir()
    mod_file = mod_dir / 'test.json'
    mod_file.write_text('{"name":"test","items":[],"maps":[]}')
    monkeypatch.setattr('src.modding.MOD_DIR', str(mod_dir))
    mods = discover_mods()
    assert len(mods) == 1
    assert mods[0].name == 'test'
