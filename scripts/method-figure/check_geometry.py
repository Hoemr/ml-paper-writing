#!/usr/bin/env python3
"""Geometric QA for TikZ method figures.

Reads the `__QA NODE <name> <x0> <y0> <x1> <y1>` lines that the QA wrapper makes
TikZ emit (see qa.sh), and reports collisions that a static source check cannot
see: text boxes that overlap, content that escapes the canvas, and elements that
sit closer than the declared minimum gaps.

Why TikZ's own geometry rather than a rasterised PDF: node bounding boxes are
exact, so there are no false positives from glyph shapes, anti-aliasing, or
softened edges. A raster checker has to carry a list of false-positive filters;
this one needs none for the overlap test.

Exit codes: 0 clean, 1 HARD findings, 2 bad input.
"""

import argparse
import re
import sys

PT_PER_CM = 28.4527
NODE_RE = re.compile(
    r"__QA\s+NODE\s+(\S+)\s+(-?[\d.]+)pt\s+(-?[\d.]+)pt\s+(-?[\d.]+)pt\s+(-?[\d.]+)pt"
)

# A container that legitimately ENCLOSES its children overlaps all of them.
# Treat full containment as nested, not as a collision.
CONTAINMENT_TOL = 0.5  # pt of slack on each side


class Box:
    __slots__ = ("name", "x0", "y0", "x1", "y1")

    def __init__(self, name, x0, y0, x1, y1):
        self.name = name
        self.x0, self.x1 = min(x0, x1), max(x0, x1)
        self.y0, self.y1 = min(y0, y1), max(y0, y1)

    @property
    def w(self):
        return self.x1 - self.x0

    @property
    def h(self):
        return self.y1 - self.y0

    def encloses(self, o, tol=CONTAINMENT_TOL):
        return (
            self.x0 <= o.x0 + tol
            and self.x1 >= o.x1 - tol
            and self.y0 <= o.y0 + tol
            and self.y1 >= o.y1 - tol
        )

    def overlap_px(self, o):
        """Overlap extents on each axis; None if they do not intersect."""
        ox = min(self.x1, o.x1) - max(self.x0, o.x0)
        oy = min(self.y1, o.y1) - max(self.y0, o.y0)
        if ox <= 0 or oy <= 0:
            return None
        return ox, oy

    def gap(self, o):
        """Axis-aligned separation distance; 0.0 if they touch or overlap."""
        dx = max(0.0, max(self.x0, o.x0) - min(self.x1, o.x1))
        dy = max(0.0, max(self.y0, o.y0) - min(self.y1, o.y1))
        return (dx * dx + dy * dy) ** 0.5


def parse(path):
    boxes, picture = {}, None
    with open(path, "r", errors="replace") as fh:
        for line in fh:
            m = NODE_RE.search(line)
            if m:
                n, x0, y0, x1, y1 = m.groups()
                boxes[n] = Box(n, *map(float, (x0, y0, x1, y1)))
                continue
            m = re.search(
                r"__QA\s+PICTURE\s+(-?[\d.]+)pt\s+(-?[\d.]+)pt\s+(-?[\d.]+)pt\s+(-?[\d.]+)pt",
                line,
            )
            if m:
                picture = Box("!picture", *map(float, m.groups()))
    return boxes, picture


def cm(pts):
    return pts / PT_PER_CM


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("qalog", help="file containing the __QA lines (usually the .log)")
    ap.add_argument(
        "--min-gap-cm",
        type=float,
        default=0.0,
        help="report non-nested pairs closer than this (advisory)",
    )
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument(
        "--ignore", default="", help="comma-separated node names to skip (backgrounds)"
    )
    args = ap.parse_args()

    skip = {s.strip() for s in args.ignore.split(",") if s.strip()}
    try:
        boxes, picture = parse(args.qalog)
    except OSError as exc:
        print(f"cannot read {args.qalog}: {exc}", file=sys.stderr)
        return 2

    if not boxes:
        print(
            "no __QA NODE lines found — did the QA wrapper run? "
            "See SKILL.md step 3.",
            file=sys.stderr,
        )
        return 2

    names = sorted(boxes)
    hard, cand = [], []

    for i, a in enumerate(names):
        if a in skip:
            continue
        A = boxes[a]
        for b in names[i + 1 :]:
            if b in skip:
                continue
            B = boxes[b]
            ov = A.overlap_px(B)
            if ov and not A.encloses(B) and not B.encloses(A):
                ox, oy = ov
                hard.append(
                    f"OVERLAP  {a} <-> {b}  by {cm(ox):.2f}cm x {cm(oy):.2f}cm"
                )
            elif args.min_gap_cm > 0 and not A.encloses(B) and not B.encloses(A):
                g = A.gap(B)
                # Only complain when the pair is roughly in the same row or column;
                # a diagonal neighbour is not an adjacency defect.
                same_row = not (A.y1 < B.y0 or B.y1 < A.y0)
                same_col = not (A.x1 < B.x0 or B.x1 < A.x0)
                if (same_row or same_col) and 0 < g < args.min_gap_cm * PT_PER_CM:
                    cand.append(f"TIGHT    {a} <-> {b}  gap {cm(g):.2f}cm")

    if picture:
        # OFFCANVAS_TOL: the outermost node of a picture always trips this by
        # exactly its outer sep (0.2pt for the default 0.4pt line width) --
        # current bounding box and the node's own .north east anchors disagree by
        # that much at the boundary. 0.2pt is 0.007cm, two orders of magnitude
        # below any visual threshold, so a node flush with the edge is not a
        # defect. Measured, not guessed: see the pilot write-up.
        OFFCANVAS_TOL = 1.0  # pt
        for name in names:
            if name in skip:
                continue
            B = boxes[name]
            if (
                B.x0 < picture.x0 - OFFCANVAS_TOL
                or B.x1 > picture.x1 + OFFCANVAS_TOL
                or B.y0 < picture.y0 - OFFCANVAS_TOL
                or B.y1 > picture.y1 + OFFCANVAS_TOL
            ):
                hard.append(f"OFFCANVAS {name} extends past the picture bounding box")

    if args.json:
        import json

        print(
            json.dumps(
                {
                    "nodes": len(boxes),
                    "hard": hard,
                    "candidate": cand,
                    "canvas_cm": (
                        [round(cm(picture.w), 2), round(cm(picture.h), 2)]
                        if picture
                        else None
                    ),
                },
                indent=2,
            )
        )
    else:
        print(f"checked {len(boxes)} nodes")
        if picture:
            print(f"canvas {cm(picture.w):.2f} x {cm(picture.h):.2f} cm")
        for line in hard:
            print(f"  HARD  {line}")
        for line in cand:
            print(f"  cand  {line}")
        if not hard and not cand:
            print("  clean — no geometric collisions")

    if hard:
        print(
            "\nHARD findings block delivery. Rotate the fix: widen the box, shorten "
            "the label, or move the element into the gap — never shrink the text."
        )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
