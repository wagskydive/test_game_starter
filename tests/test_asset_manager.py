import os
import sys
import json
import zipfile

sys.path.insert(0, os.path.abspath('src'))


def test_download_and_index_local_zip(tmp_path, monkeypatch):
    # Prepare environment
    db_path = tmp_path / 'assets.json'
    temp_dir = tmp_path / 'tmp'
    monkeypatch.setenv('ASSET_DB', str(db_path))
    monkeypatch.setenv('ASSET_TEMP', str(temp_dir))

    # Import after env vars so paths are updated
    from asset_manager import download_and_index

    # Create a small zip file to act as the download
    zip_file = tmp_path / 'pack.zip'
    with zipfile.ZipFile(zip_file, 'w') as zf:
        zf.writestr('file1.png', 'data')
        zf.writestr('folder/file2.png', 'more')

    download_and_index('testpack', f'file://{zip_file}')

    dest_zip = temp_dir / 'testpack.zip'
    assert not dest_zip.exists()
    assert db_path.exists()
    with open(db_path) as f:
        data = json.load(f)
    assert 'testpack' in data
    assert 'file1.png' in data['testpack']
    assert 'folder/file2.png' in data['testpack']


def test_ensure_assets_multiple(tmp_path, monkeypatch):
    db_path = tmp_path / 'assets.json'
    temp_dir = tmp_path / 'tmp'
    monkeypatch.setenv('ASSET_DB', str(db_path))
    monkeypatch.setenv('ASSET_TEMP', str(temp_dir))

    import importlib
    import asset_manager
    asset_manager = importlib.reload(asset_manager)

    zip1 = tmp_path / 'ui.zip'
    with zipfile.ZipFile(zip1, 'w') as zf:
        zf.writestr('ui/button.png', 'data')

    zip2 = tmp_path / 'env.zip'
    with zipfile.ZipFile(zip2, 'w') as zf:
        zf.writestr('env/tile.png', 'data')

    assets = {'ui': f'file://{zip1}', 'env': f'file://{zip2}'}
    asset_manager.ensure_assets(assets)

    assert not (temp_dir / 'ui.zip').exists()
    assert not (temp_dir / 'env.zip').exists()
    with open(db_path) as f:
        data = json.load(f)
    assert set(data.keys()) == {'ui', 'env'}
    assert 'ui/button.png' in data['ui']
    assert 'env/tile.png' in data['env']

    def fail(*args, **kwargs):
        raise RuntimeError('should not download again')

    monkeypatch.setattr(asset_manager, 'download_and_index', fail)
    asset_manager.ensure_assets(assets)


def test_default_assets_keys():
    import asset_manager
    keys = set(asset_manager.DEFAULT_ASSETS.keys())
    assert keys == {
        'tiny-town',
        'roguelike-characters',
        'ui-pack-rpg-expansion',
    }
