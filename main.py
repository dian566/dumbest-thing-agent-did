#!/usr/bin/env python3
"""The dumbest thing my agent did today, as one line."""

from pathlib import Path

# The story is stored in two halves so each half sits on its own line
# while the stitched entry stays exactly the drafted sentence.
FIRST_HALF = "My agent spent 40 minutes 'optimizing' my deploy script,"
SECOND_HALF = "then deleted it as redundant and asked me to rewrite it from memory."
OUT_FILE = Path("/output/entry.txt")


def stitch(first, second):
    """Join the two halves of the story with a single space."""
    return first + " " + second


def run():
    line = stitch(FIRST_HALF, SECOND_HALF)
    if len(line) > 200:
        raise SystemExit(f"line is {len(line)} chars, over the 200 limit")
    if not line:
        raise SystemExit("line came out empty")
    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(line, encoding="utf-8")


run()
