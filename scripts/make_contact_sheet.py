#!/usr/bin/env python3
"""Create a contact sheet from rendered slide images.

Usage:
    python scripts/make_contact_sheet.py --input preview --output preview/contact_sheet.jpg
"""

from __future__ import annotations

import argparse
from pathlib import Path
from PIL import Image, ImageDraw


def natural_key(path: Path) -> tuple[int, str]:
    digits = "".join(ch for ch in path.stem if ch.isdigit())
    return (int(digits) if digits else 0, path.name)


def build_contact_sheet(input_dir: Path, output: Path, cols: int = 6, thumb_w: int = 240) -> None:
    images = sorted(
        [p for p in input_dir.iterdir() if p.suffix.lower() in {".jpg", ".jpeg", ".png"}],
        key=natural_key,
    )
    if not images:
        raise SystemExit(f"No rendered slide images found in {input_dir}")

    thumb_h = int(thumb_w * 9 / 16)
    label_h = 22
    thumbs: list[Image.Image] = []
    for path in images:
        im = Image.open(path).convert("RGB")
        im.thumbnail((thumb_w, thumb_h), Image.Resampling.LANCZOS)
        canvas = Image.new("RGB", (thumb_w, thumb_h + label_h), "white")
        canvas.paste(im, (0, 0))
        draw = ImageDraw.Draw(canvas)
        draw.text((5, thumb_h + 4), path.stem, fill=(70, 70, 70))
        thumbs.append(canvas)

    rows = (len(thumbs) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * thumb_w, rows * (thumb_h + label_h)), (245, 247, 250))
    for idx, thumb in enumerate(thumbs):
        sheet.paste(thumb, ((idx % cols) * thumb_w, (idx // cols) * (thumb_h + label_h)))

    output.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(output, quality=92)
    print(output)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--cols", type=int, default=6)
    parser.add_argument("--thumb-width", type=int, default=240)
    args = parser.parse_args()
    build_contact_sheet(args.input, args.output, args.cols, args.thumb_width)


if __name__ == "__main__":
    main()

