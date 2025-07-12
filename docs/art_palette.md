# Art Palette and Layered Sprites

The placeholder asset pipeline uses a simple color palette to create mock sprite layers. The palette defines muted earth tones with a bright highlight color:

```python
from palette import PALETTE, LAYERS
```

`PALETTE` maps color names to RGBA tuples and `LAYERS` lists the base layers used for characters. Running:

```bash
python scripts/generate_assets.py
```

creates one tile sprite and separate images for each layer (body, eyes, hair and clothes) under `assets/generated/`.
