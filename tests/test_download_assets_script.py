import json
import os
import sys
import zipfile

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from importlib import reload
from scripts import download_assets


def test_download_assets_script(tmp_path, monkeypatch):
    db_path = tmp_path / 'assets.json'
    temp_dir = tmp_path / 'tmp'
    monkeypatch.setenv('ASSET_DB', str(db_path))
    monkeypatch.setenv('ASSET_TEMP', str(temp_dir))

    # Create a fake asset zip
    zip_file = tmp_path / 'pack.zip'
    with zipfile.ZipFile(zip_file, 'w') as zf:
        zf.writestr('file.png', 'data')

    from src import asset_manager
    asset_manager = reload(asset_manager)
    monkeypatch.setattr(asset_manager, 'DEFAULT_ASSETS', {'pack': f'file://{zip_file}'})

    reload(download_assets)
    download_assets.main()

    assert db_path.exists()
    with open(db_path) as f:
        data = json.load(f)
    assert 'pack' in data
    assert 'file.png' in data['pack']
