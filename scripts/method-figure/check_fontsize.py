#!/usr/bin/env python3
"""Check effective font size at the width the figure is actually printed at.

A figure authored on a wide canvas looks fine on screen and prints unreadably
small once LaTeX scales it down to a column width. The relation is linear:

    effective_pt = design_pt * (print_width / canvas_width)

so every 10% the canvas exceeds the print width costs 10% of the type size. This
script reads the font sizes declared in the source, takes the canvas width from
the geometry dump, and reports the smallest effective size.

Design floors (see references/constraints.md): 7.0 pt is the working floor for
ML figures, 8.0 pt for primary labels. 5.0 pt is the absolute limit below which
a venue's production department will reject the artwork.
"""

import argparse
import re
import sys

# article-class relative sizes, by document base size
RELATIVE = {
    10: {"tiny": 5.0, "scriptsize": 7.0, "footnotesize": 8.0, "small": 9.0,
         "normalsize": 10.0, "large": 12.0, "Large": 14.4, "LARGE": 17.28,
         "huge": 20.74, "Huge": 24.88},
    11: {"tiny": 6.0, "scriptsize": 8.0, "footnotesize": 9.0, "small": 10.0,
         "normalsize": 10.95, "large": 12.0, "Large": 14.4, "LARGE": 17.28,
         "huge": 20.74, "Huge": 24.88},
    12: {"tiny": 6.0, "scriptsize": 8.0, "footnotesize": 10.0, "small": 10.95,
         "normalsize": 12.0, "large": 14.4, "Large": 17.28, "LARGE": 20.74,
         "huge": 24.88, "Huge": 29.86},
}

PT_PER_CM = 28.4527

# Venue text widths, measured from the shipped .sty files (references/venues.md).
VENUE_MM = {
    "iclr": 140.0, "neurips": 140.0, "colm": 140.0,
    "icml-full": 171.45, "icml-col": 82.55,
    "acl-full": 160.0, "acl-col": 77.0,
    "aaai-full": 177.8, "aaai-col": 84.0,
}

FONTSIZE_RE = re.compile(r"\\fontsize\s*\{\s*([\d.]+)\s*\}")
RELATIVE_RE = re.compile(
    r"\\(tiny|scriptsize|footnotesize|small|normalsize|large|Large|LARGE|huge|Huge)\b"
)
BASE_RE = re.compile(r"\\documentclass\s*\[([^\]]*)\]")
CANVAS_RE = re.compile(
    r"__QA\s+PICTURE\s+(-?[\d.]+)pt\s+(-?[\d.]+)pt\s+(-?[\d.]+)pt\s+(-?[\d.]+)pt"
)


def base_size(src):
    m = BASE_RE.search(src)
    if m:
        for opt in m.group(1).split(","):
            opt = opt.strip()
            if opt in ("10pt", "11pt", "12pt"):
                return int(opt[:-2])
    return 10  # standalone/article default


def canvas_width_pt(qa_text):
    m = CANVAS_RE.search(qa_text)
    if not m:
        return None
    x0, _, x1, _ = map(float, m.groups())
    return x1 - x0


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("src", help="figure .tex")
    ap.add_argument("--qa", help="geometry dump (.qa), used for the canvas width")
    ap.add_argument("--print-width-mm", type=float, default=None)
    ap.add_argument("--venue", choices=sorted(VENUE_MM), default=None,
                    help="shorthand for a known print width")
    ap.add_argument("--floor", type=float, default=7.0,
                    help="working floor in pt (default 7.0)")
    args = ap.parse_args()

    try:
        src = open(args.src, "r").read()
    except OSError as exc:
        print(f"cannot read {args.src}: {exc}", file=sys.stderr)
        return 2

    if args.print_width_mm:
        print_mm = args.print_width_mm
    elif args.venue:
        print_mm = VENUE_MM[args.venue]
    else:
        print_mm = VENUE_MM["iclr"]
        print(f"note: no width given, assuming ICLR/NeurIPS {print_mm:.0f}mm", file=sys.stderr)

    canvas_pt = None
    if args.qa:
        try:
            canvas_pt = canvas_width_pt(open(args.qa, "r").read())
        except OSError as exc:
            print(f"cannot read {args.qa}: {exc}", file=sys.stderr)
            return 2
    if canvas_pt is None:
        print(
            "no canvas width available — pass --qa <file.qa> produced by the QA run, "
            "or --canvas-pt",
            file=sys.stderr,
        )
        return 2

    base = base_size(src)
    table = RELATIVE[base]

    findings = []
    for m in FONTSIZE_RE.finditer(src):
        findings.append((float(m.group(1)), f"\\fontsize{{{m.group(1)}}}"))
    for m in RELATIVE_RE.finditer(src):
        name = m.group(1)
        if name == "normalsize":
            continue
        findings.append((table[name], f"\\{name}"))

    if not findings:
        print("no explicit font size commands found (figure inherits the base size)")
        findings = [(float(base), "\\normalsize (inherited)")]

    canvas_mm = canvas_pt / PT_PER_CM * 10.0
    scale = print_mm / canvas_mm

    print(f"document base size : {base}pt")
    print(f"canvas width       : {canvas_mm:.1f}mm")
    print(f"print width        : {print_mm:.1f}mm")
    print(f"scale factor       : {scale:.3f}")
    print()
    print(f"{'declared':>10}  {'effective':>10}   source")
    print("-" * 52)

    worst = None
    for pts, label in sorted(findings):
        eff = pts * scale
        flag = ""
        if eff < 5.0:
            flag = "  <-- BELOW 5pt HARD LIMIT"
        elif eff < args.floor:
            flag = "  <-- below floor"
        print(f"{pts:>8.2f}pt  {eff:>8.2f}pt   {label}{flag}")
        if worst is None or eff < worst[0]:
            worst = (eff, label)

    eff, label = worst
    print()
    if eff < 5.0:
        print(f"FAIL: smallest text is {eff:.2f}pt ({label}) — below the 5pt hard limit.")
        return 1
    if eff < args.floor:
        print(
            f"WARN: smallest text is {eff:.2f}pt ({label}), under the {args.floor}pt "
            f"working floor. Enlarge the type or narrow the canvas by "
            f"{100 * (canvas_mm / print_mm * (args.floor / eff) - 1):.0f}%."
        )
        return 0
    print(f"PASS: smallest text is {eff:.2f}pt ({label}) at {print_mm:.0f}mm.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
