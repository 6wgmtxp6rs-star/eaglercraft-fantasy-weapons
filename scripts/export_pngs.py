#!/usr/bin/env python3
"""Convert the fantasy weapon SVG sources into PNG textures for Eaglercraft resource packs."""

from __future__ import annotations

import sys
from pathlib import Path

try:
    import cairosvg
except ImportError as exc:  # pragma: no cover
    raise SystemExit(
        "Missing dependency: cairosvg. Install with `python -m pip install -r requirements.txt`."
    ) from exc

ROOT = Path(__file__).resolve().parent.parent
TEXTURE_DIR = ROOT / "dist" / "eaglercraft_fantasy_weapons" / "assets" / "minecraft" / "textures" / "items"


def export_svg_to_png(svg_path: Path) -> Path:
    png_path = svg_path.with_suffix(".png")
    cairosvg.svg2png(url=str(svg_path), write_to=str(png_path), output_width=64, output_height=64)
    return png_path


def main() -> None:
    if not TEXTURE_DIR.exists():
        raise SystemExit(f"Texture directory not found: {TEXTURE_DIR}")

    svg_files = sorted(TEXTURE_DIR.glob("*.svg"))
    if not svg_files:
        raise SystemExit(f"No SVG files found in {TEXTURE_DIR}")

    exported = []
    for svg_file in svg_files:
        png_path = export_svg_to_png(svg_file)
        exported.append(png_path)
        print(f"Exported: {svg_file.name} -> {png_path.name}")

    print(f"\nFinished exporting {len(exported)} texture(s).")


if __name__ == "__main__":
    main()
