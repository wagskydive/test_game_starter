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
