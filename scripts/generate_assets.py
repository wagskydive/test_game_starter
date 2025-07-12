"""Generate placeholder sprite assets."""

import os
from PIL import Image

from src import palette

ASSET_DIR = os.path.join(os.path.dirname(__file__), '..', 'assets', 'generated')


def generate() -> None:
    os.makedirs(ASSET_DIR, exist_ok=True)

    # Basic placeholder tile
    tile = Image.new('RGBA', (32, 32), (127, 127, 127, 255))
    tile.save(os.path.join(ASSET_DIR, 'tile.png'))

    # Character layers using the defined palette
    for layer in palette.LAYERS:
        color_key = 'skin' if layer == 'body' else layer
        color = palette.PALETTE.get(color_key, (127, 127, 127, 255))
        img = Image.new('RGBA', (32, 32), color)
        img.save(os.path.join(ASSET_DIR, f'{layer}.png'))


if __name__ == '__main__':
    generate()
