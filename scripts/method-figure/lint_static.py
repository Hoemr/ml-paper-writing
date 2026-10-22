#!/usr/bin/env python3
"""Static pre-compile lint for TikZ figures.

Catches authoring hazards that are visible in the source and need no render:
each check maps to a named defect class documented in references/constraints.md.
Anything that needs real geometry belongs in check_geometry.py instead.

Severity:
  HARD  definite defect or a compile hazard; do not ship.
  warn  a smell that is sometimes deliberate -- confirm before changing.

Exit: 0 clean or warnings only, 1 any HARD, 2 bad input.
"""

import argparse
import re
import sys

# --- helpers ---------------------------------------------------------------


def strip_comments(src):
    """Remove TeX comments so checks do not fire on commented-out code."""
    out = []
    for line in src.splitlines():
        # a % that is not escaped starts a comment
        idx, esc = None, False
        for i, ch in enumerate(line):
            if ch == "\\":
                esc = not esc
                continue
            if ch == "%" and not esc:
                idx = i
                break
            esc = False
        out.append(line if idx is None else line[:idx])
    return "\n".join(out)


def line_of(src, pos):
    return src.count("\n", 0, pos) + 1


# --- checks ----------------------------------------------------------------
# Each returns (severity, line, message).


def _option_span(src, start):
    """End index of the [...] option list opening at/after `start`, or None.

    Tracks bracket depth so nested brackets inside style definitions do not
    terminate the span early.
    """
    i = src.find("[", start)
    if i == -1:
        return None
    depth = 0
    while i < len(src):
        if src[i] == "[":
            depth += 1
        elif src[i] == "]":
            depth -= 1
            if depth == 0:
                return i
        i += 1
    return None


def check_blank_line_in_picture(raw):
    # Empirically: a blank line inside the tikzpicture OPTION LIST is a hard
    # error ("Paragraph ended before \\tikz@picture was complete"), while a blank
    # line in the picture BODY compiles fine. Only the option list is reported.
    # A comment-only line is safe in both places: `%` eats the newline.
    # Raw source is required -- strip_comments() would turn a comment-only
    # separator into an empty line and produce a false positive.
    for m in re.finditer(r"\\begin\{tikzpicture\}", raw):
        end = _option_span(raw, m.end())
        if end is None:
            continue
        opts = raw[m.end() : end]
        hit = re.search(r"\n[ \t]*\n", opts)
        if hit:
            yield "HARD", line_of(raw, m.end() + hit.start()), (
                "blank line inside the tikzpicture option list. TikZ fails with "
                "'Paragraph ended before \\tikz@picture was complete'. Replace it "
                "with a comment-only line (a bare % works); blank lines in the "
                "picture body are fine, but not in the options"
            )


def check_standalone(src):
    if not re.search(r"\\documentclass\s*\[[^\]]*\]\s*\{\s*standalone\s*\}", src):
        if "standalone" not in src:
            yield "HARD", 1, (
                "not a standalone document. Figures that cannot compile alone "
                "cannot be QA'd in isolation; use \\documentclass[tikz]{standalone}"
            )


def check_border(src):
    m = re.search(r"\\documentclass\s*\[([^\]]*)\]\s*\{\s*standalone\s*\}", src)
    if not m:
        return
    opts = m.group(1)
    b = re.search(r"border\s*=\s*([\d.]+)\s*(pt|mm|cm)", opts)
    if not b:
        yield "warn", line_of(src, m.start()), (
            "standalone with no explicit border; labels and arrowheads near the "
            "edge get clipped. Use border=10pt or more (25pt if you have an "
            "outer loop that leaves the frame)"
        )
    else:
        val, unit = float(b.group(1)), b.group(2)
        pt = {"pt": 1, "mm": 2.845, "cm": 28.45}[unit] * val
        if pt < 8:
            yield "warn", line_of(src, m.start()), (
                f"border={val}{unit} is only {pt:.1f}pt; arrows or labels that "
                "leave the content box will be clipped"
            )


def check_bare_scale(src):
    # bare scale= on the picture or a scope rescales coordinates but NOT text,
    # so gaps shrink while labels stay put -- it manufactures collisions.
    for m in re.finditer(r"\\begin\{(?:tikzpicture|scope)\}\s*\[([^\]]*)\]", src):
        opts = m.group(1)
        if re.search(r"(?<![a-zA-Z-])scale\s*=", opts) and "transform shape" not in opts:
            yield "HARD", line_of(src, m.start()), (
                "bare scale= rescales coordinates but not text: gaps shrink while "
                "labels keep their size, which silently creates overlaps. Use "
                "[scale=..., transform shape] or shrink node distance and widths "
                "instead"
            )


def check_label_on_line(src):
    # \draw (a) -- (b) node {x};  places the label ON the line.
    for m in re.finditer(r"node\s*(?:\[[^\]]*\])?\s*\{", src):
        head = src[max(0, m.start() - 200) : m.start()]
        if "--" not in head and "|-" not in head and "-|" not in head:
            continue
        bracket = re.match(r"node\s*(?:\[([^\]]*)\])?", src[m.start() :])
        opts = (bracket.group(1) or "") if bracket else ""
        if not re.search(
            r"\b(above|below|left|right|midway|pos\s*=|anchor\s*=|at\s*\()", opts
        ):
            yield "HARD", line_of(src, m.start()), (
                "edge label with no directional keyword; it will sit on top of the "
                "line. Add above/below/left/right (horizontal line -> above/below, "
                "vertical -> left/right), or place a separate \\node"
            )


def check_bending(src):
    curved = re.search(r"(bend\s+(left|right)|to\s*\[\s*(out|in)\s*=|\.\.\s*controls)", src)
    if curved and "bending" not in src:
        yield "HARD", line_of(src, curved.start()), (
            "curved or bent path without \\usetikzlibrary{bending}: arrow tips on "
            "bends will be visibly misaligned"
        )


def check_calc(src):
    needs = re.search(r"(let\s+\\p\d|\$\([^)]*\)!|\$\()", src)
    if needs and not re.search(r"\\usetikzlibrary\{[^}]*\bcalc\b", src):
        yield "HARD", line_of(src, needs.start()), (
            "uses calc syntax ($(...)$, let \\pN=) but calc is not loaded"
        )


def check_node_name_dot(src):
    for m in re.finditer(r"\\node\s*(?:\[[^\]]*\]\s*)?\(([^)]*\.[^)]*)\)", src):
        yield "HARD", line_of(src, m.start()), (
            f"node name '{m.group(1)}' contains a dot; TikZ truncates it and later "
            "references fail with 'No shape named'. Use an alphabetic name"
        )


def check_rounded_on_straight(src):
    for m in re.finditer(r"\\draw\s*\[([^\]]*)\]\s*(\([^)]*\))\s*--\s*(\([^)]*\))\s*;", src):
        if "rounded corners" in m.group(1):
            yield "warn", line_of(src, m.start()), (
                "rounded corners on a straight single-segment -- path produces "
                "ghost arcs at both endpoints. Apply it only to paths with a real "
                "corner (>=2 segments, or |-/-|)"
            )


def check_anchorless_edges(src):
    # (a) -- (b) between named nodes targets their centres, so the line runs
    # under the boxes instead of stopping at their borders.
    for m in re.finditer(
        r"\\draw\s*(?:\[[^\]]*\])?\s*\(([A-Za-z][\w-]*)\)\s*--\s*\(([A-Za-z][\w-]*)\)", src
    ):
        yield "warn", line_of(src, m.start()), (
            f"'{m.group(1)} -- {m.group(2)}' has no anchors; the line targets node "
            "centres so tips land inside the boxes. Prefer "
            f"({m.group(1)}.east) -- ({m.group(2)}.west)"
        )


def check_inline_hex(src):
    # A \definecolor{name}{HTML}{...} block IS the palette definition -- that is
    # where hex belongs. Flag only hex used outside such a declaration.
    for m in re.finditer(r"\{HTML\}\{([0-9A-Fa-f]{6})\}", src):
        before = src[max(0, m.start() - 80) : m.start()]
        if re.search(r"\\definecolor\s*\{[^}]*\}\s*$", before):
            continue  # palette definition, correct place
        yield "warn", line_of(src, m.start()), (
            f"inline hex {m.group(1)} outside a \\definecolor. Define the palette "
            "once at the top and use named colours (with !tint shades) so one edit "
            "re-themes the figure"
        )


def check_long_node_text(src):
    for m in re.finditer(r"\\node[^;{]*\{([^{}]{70,})\}", src):
        frag = m.group(1)
        if "\\\\" in frag or "text width" in src[max(0, m.start() - 150) : m.start()]:
            continue
        yield "warn", line_of(src, m.start()), (
            f"{len(frag)}-character node label with no wrapping. Shorten it and move "
            "the detail to the caption, or add text width=... , align=center"
        )


def check_rotate(src):
    for m in re.finditer(r"rotate\s*=\s*(\d+)", src):
        yield "warn", line_of(src, m.start()), (
            f"rotate={m.group(1)}: rotated labels are harder to read and rotated "
            "bounding boxes defeat geometric overlap checking. Prefer horizontal text"
        )


def check_foreach_colour(src):
    # The known xcolor bug is looping a colour *name* into a colour slot, where a
    # trailing space corrupts the name. Looping a numeric tint (!25, !50) is
    # fine, so require the variable to be used as a bare colour.
    for m in re.finditer(r"\\foreach\s+([^\n{]*)\{([^\n]*)\}", src):
        vars_part, body = m.group(1), m.group(2)
        slots = [v.strip() for v in vars_part.split("/")]
        if len(slots) < 2:
            continue
        varname = slots[-1]
        if not re.fullmatch(r"\\[A-Za-z]+", varname):
            continue
        after = src[m.end() : m.end() + 220]
        # bare use as a colour slot: [\varname] or {color=\varname} -- but not !\varname
        if re.search(r"(\[[^\]]*[^!\w]|\bcolor\s*=\s*)" + re.escape(varname) + r"\s*[\],}]", after):
            yield "warn", line_of(src, m.start()), (
                "looping a colour NAME through a variable hits a known xcolor bug "
                "(trailing space corrupts the name). Unroll it and write each colour "
                "literally, or loop a numeric tint instead"
            )


CHECKS = [
    check_standalone,
    check_blank_line_in_picture,
    check_border,
    check_bare_scale,
    check_label_on_line,
    check_bending,
    check_calc,
    check_node_name_dot,
    check_rounded_on_straight,
    check_anchorless_edges,
    check_inline_hex,
    check_long_node_text,
    check_rotate,
    check_foreach_colour,
]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("src")
    ap.add_argument("--quiet-warn", action="store_true")
    args = ap.parse_args()

    try:
        raw = open(args.src, "r").read()
    except OSError as exc:
        print(f"cannot read {args.src}: {exc}", file=sys.stderr)
        return 2
    src = strip_comments(raw)

    hard, warn = [], []
    for fn in CHECKS:
        target = raw if fn is check_blank_line_in_picture else src
        for sev, line, msg in fn(target):
            (hard if sev == "HARD" else warn).append((line, msg))

    hard.sort()
    warn.sort()

    for line, msg in hard:
        print(f"HARD  line {line}: {msg}")
    if not args.quiet_warn:
        for line, msg in warn:
            print(f"warn  line {line}: {msg}")

    print()
    print(f"{len(hard)} hard, {len(warn)} warning(s)")
    if hard:
        print("Fix every HARD item before rendering.")
        return 1
    if warn and not args.quiet_warn:
        print("Warnings are smells, not verdicts — confirm each in the render.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
