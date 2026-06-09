#!/usr/bin/env python3
"""Lightweight quality gate for consulting-style PPTX decks."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from inspect_pptx import inspect


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("pptx", type=Path)
    parser.add_argument("--min-font", type=float, default=12.0)
    parser.add_argument("--min-slides", type=int, default=1)
    args = parser.parse_args()

    result = inspect(args.pptx)
    failures: list[str] = []

    if result["slides"] < args.min_slides:
        failures.append(f"slide count {result['slides']} < {args.min_slides}")
    if result["min_font_size"] is not None and result["min_font_size"] < args.min_font:
        failures.append(f"minimum font {result['min_font_size']} < {args.min_font}")
    if result["low_text_slides"]:
        failures.append(f"low-text slides detected: {result['low_text_slides']}")

    print("Consulting Slide Master quality check")
    print(f"slides: {result['slides']}")
    print(f"min_font_size: {result['min_font_size']}")
    print(f"text_shapes: {result['text_shapes']}")

    if failures:
        print("FAIL")
        for failure in failures:
            print(f"- {failure}")
        sys.exit(1)

    print("PASS")


if __name__ == "__main__":
    main()

