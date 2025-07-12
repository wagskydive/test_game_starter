"""Generate placeholder sprite assets."""

import os
from PIL import Image

ASSET_DIR = os.path.join(os.path.dirname(__file__), '..', 'assets', 'generated')
os.makedirs(ASSET_DIR, exist_ok=True)

for name in ['tile', 'character']:
    img = Image.new('RGBA', (32, 32), (127, 127, 127, 255))
    img.save(os.path.join(ASSET_DIR, f'{name}.png'))
