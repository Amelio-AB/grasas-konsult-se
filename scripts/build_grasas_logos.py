#!/usr/bin/env python3
"""Skapa transparenta WebP-bilder för webbplatsen från GitHub-lagrade SVG-original."""
from __future__ import annotations

from io import BytesIO
from pathlib import Path

import cairosvg
from PIL import Image

SOURCE = Path("deploy/grasas/images")
ASSETS = (
    ("grasas-full-vit", 1800),
    ("grasas-full-svart", 1800),
    ("grasas-symbol-vit", 700),
    ("grasas-symbol-svart", 700),
)


def main() -> None:
    for stem, target_width in ASSETS:
        svg = SOURCE / f"{stem}.svg"
        dest = SOURCE / f"{stem}.webp"
        if not svg.is_file():
            raise SystemExit(f"Logotyp saknas i GitHub: {svg}")
        png_bytes = cairosvg.svg2png(url=str(svg), output_width=target_width)
        with Image.open(BytesIO(png_bytes)) as input_image:
            image = input_image.convert("RGBA")
            if image.getpixel((0, 0))[3] != 0:
                raise SystemExit(f"Logotypens hörn är inte transparent: {svg}")
            image.save(dest, format="WEBP", quality=90, method=4)
        print(f"Skapade {dest}: {image.width}x{image.height}, {dest.stat().st_size} byte")


if __name__ == "__main__":
    main()
