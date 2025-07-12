import os
import json
import zipfile
import shutil
from urllib.parse import urlparse

try:
    import requests
except ImportError:  # in case requests isn't installed when imported
    requests = None


# Directories can be overridden for tests via environment variables
ASSET_DIR = os.path.join(os.path.dirname(__file__), '..', 'assets')
ASSET_DB = os.environ.get('ASSET_DB', os.path.join(ASSET_DIR, 'asset_index.json'))
TEMP_DIR = os.environ.get('ASSET_TEMP', os.path.join(ASSET_DIR, 'temp'))


def _download(url: str, dest: str) -> None:
    parsed = urlparse(url)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    if parsed.scheme == 'file':
        shutil.copyfile(parsed.path, dest)
    else:
        if requests is None:
            raise RuntimeError('requests is required to download assets')
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(dest, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)


def download_and_index(name: str, url: str) -> None:
    """Download a zip file, record its contents to the asset DB, then delete."""
    os.makedirs(TEMP_DIR, exist_ok=True)
    os.makedirs(os.path.dirname(ASSET_DB), exist_ok=True)
    zip_path = os.path.join(TEMP_DIR, f'{name}.zip')
    _download(url, zip_path)

    with zipfile.ZipFile(zip_path, 'r') as zf:
        files = [info.filename for info in zf.infolist()]

    if os.path.exists(ASSET_DB):
        with open(ASSET_DB, 'r') as f:
            data = json.load(f)
    else:
        data = {}
    data[name] = files
    with open(ASSET_DB, 'w') as f:
        json.dump(data, f, indent=2)

    os.remove(zip_path)


def ensure_assets(assets: dict) -> None:
    """Ensure each asset pack is indexed. assets is {name: url}."""
    existing = {}
    if os.path.exists(ASSET_DB):
        with open(ASSET_DB, 'r') as f:
            existing = json.load(f)

    for name, url in assets.items():
        if name not in existing:
            download_and_index(name, url)
