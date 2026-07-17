#!/usr/bin/env python3
"""Add 1px gray borders to images for Guru card publishing.

Guru does not support image borders in the editor. Run this on all screenshots
and exported diagrams before embedding in the Guru card markdown.

Usage:
  python scripts/add-image-borders.py path/to/images/
  python scripts/add-image-borders.py path/to/single-image.png

Creates *-bordered.png alongside each source PNG (skips files already bordered).
Requires: pip install pillow
"""

from __future__ import annotations

import sys
from pathlib import Path

try:
    from PIL import Image, ImageOps
except ImportError:
    print("Install pillow: pip install pillow", file=sys.stderr)
    sys.exit(1)

BORDER_PX = 1
BORDER_COLOR = (200, 200, 200)  # light gray, similar to Google Docs


def add_border(src: Path) -> Path:
    if src.name.endswith("-bordered.png"):
        return src
    out = src.with_name(f"{src.stem}-bordered{src.suffix}")
    img = Image.open(src).convert("RGB")
    bordered = ImageOps.expand(img, border=BORDER_PX, fill=BORDER_COLOR)
    bordered.save(out)
    return out


def collect_images(path: Path) -> list[Path]:
    if path.is_file():
        return [path] if path.suffix.lower() == ".png" and not path.name.endswith("-bordered.png") else []
    return sorted(
        p
        for p in path.glob("*.png")
        if not p.name.endswith("-bordered.png")
    )


def main() -> None:
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)

    target = Path(sys.argv[1])
    if not target.exists():
        print(f"Not found: {target}", file=sys.stderr)
        sys.exit(1)

    images = collect_images(target)
    if not images:
        print("No PNG images to process.")
        return

    for src in images:
        out = add_border(src)
        print(f"{src.name} -> {out.name}")


if __name__ == "__main__":
    main()
