#!/usr/bin/env python3
"""Flag slides whose vertical whitespace is unbalanced.

Renders main.pdf and, for each slide, measures the gap between the bottom of the
navy title bar and the first row of body ink, and between the last row of body
ink and the top of the fixed ND corner logo. A slide wants attention when the
first gap is large while the second is small: it looks top-empty and
bottom-crowded, and at the back of a room the crowding reads as a mistake.

LaTeX will not warn about this. An overfull \\vbox only fires once content
overflows the frame entirely, which is well past the point where the last line
is sitting on the logo.

    python3 check_layout.py [--dpi 100]

Requires pdftoppm (poppler) and Pillow. Written 2026-09-14 after a full-deck
whitespace pass; see notes/seminar_notes.md.
"""
import argparse
import glob
import os
import subprocess
import sys
import tempfile

try:
    from PIL import Image
except ImportError:
    sys.exit("Pillow is required: pip install Pillow")

NAVY = (12, 35, 64)
# The corner logo sits in a fixed band. 0.890 of the page height is the first
# row it occupies, measured from the rendered deck; body ink should clear it.
LOGO_TOP_FRAC = 0.890
BIG_TOP_GAP = 0.085      # fraction of page height
TIGHT_BOTTOM = 0.035


def near(p, ref, tol):
    return all(abs(p[i] - ref[i]) <= tol for i in range(3))


def measure(path):
    im = Image.open(path).convert("RGB")
    W, H = im.size
    px = im.load()
    floor = int(H * LOGO_TOP_FRAC)

    bar = 0
    for y in range(int(H * 0.25)):
        if near(px[W // 2, y], NAVY, 40) or near(px[int(W * 0.1), y], NAVY, 40):
            bar = y
    top0 = bar + 3 if bar else int(H * 0.05)

    first = last = None
    for y in range(top0, floor):
        ink = sum(1 for x in range(W) if not near(px[x, y], (255, 255, 255), 25))
        if ink > 2:
            if first is None:
                first = y
            last = y
    if first is None:
        return None
    return (first - top0) / H, (floor - last) / H, bar == 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf", default="main.pdf")
    ap.add_argument("--dpi", type=int, default=100)
    args = ap.parse_args()

    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run(["pdftoppm", "-png", "-r", str(args.dpi), args.pdf,
                        os.path.join(tmp, "p")], check=True)
        rows = []
        for f in sorted(glob.glob(os.path.join(tmp, "p-*.png"))):
            n = int(os.path.basename(f).split("-")[1].split(".")[0])
            m = measure(f)
            if m:
                rows.append((n,) + m)

    flagged = 0
    print(f"{'slide':>5} {'top':>7} {'bottom':>7}   note")
    for n, top, bot, plain in sorted(rows, key=lambda r: -(r[1] - r[2])):
        notes = []
        if plain:
            notes.append("divider or title slide")
        if top >= BIG_TOP_GAP and bot <= TIGHT_BOTTOM:
            notes.insert(0, "REBALANCE: top-empty, bottom-crowded")
            flagged += 1
        elif bot <= 0.012:
            notes.insert(0, "bottom crowded")
            flagged += 1
        print(f"{n:5d} {top:7.3f} {bot:7.3f}   {', '.join(notes)}")

    print(f"\n{flagged} slide(s) flagged of {len(rows)}.")
    print("Centred slides show a large gap at BOTH ends; that is intentional, not a finding.")


if __name__ == "__main__":
    main()
