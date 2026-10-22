#!/usr/bin/env python3
"""Instrument a TikZ figure so it reports its own node geometry.

Reads a standalone figure, injects a small QA preamble and a per-picture
geometry dump, and writes an instrumented copy. The original file is never
modified: this always writes to a separate path, which is the whole point —
QA must not contaminate the figure you ship.

Only nodes with a literal name are instrumentable. Nodes created inside a
\\foreach get computed names and are skipped; so are bare nodes and coordinates,
which have no extent worth testing.
"""

import argparse
import re
import sys

QA_PREAMBLE = r"""
% ===== method-figure QA instrumentation (generated; not part of the figure) =====
\usetikzlibrary{calc}
\newwrite\qafile
% \immediate matters: a deferred \openout would not run until shipout, but the
% \write calls below are immediate, so they would hit an unopened stream.
\immediate\openout\qafile=\jobname.qa
\newcommand{\qadump}[1]{%
  \path let \p1=(#1.south west), \p2=(#1.north east) in
    \pgfextra{\immediate\write\qafile{__QA NODE #1 \x1 \y1 \x2 \y2}};%
}
\newcommand{\qapicture}{%
  \path let \p1=(current bounding box.south west),
            \p2=(current bounding box.north east) in
    \pgfextra{\immediate\write\qafile{__QA PICTURE \x1 \y1 \x2 \y2}};%
}
\AtEndDocument{\immediate\closeout\qafile}
% ================= end QA instrumentation =================
"""

# \node[opts] (name) ...   or   \node (name) [opts]
NODE_NAMED = re.compile(r"\\node\s*(?:\[[^\]]*\]\s*)?\(([^)]+)\)")
PICTURE_END = re.compile(r"\\end\{tikzpicture\}")

# Container-ish style names: overlapping these with their contents is expected.
SKIP_STYLE_HINT = re.compile(r"\b(fit|background|zone|container|layer|panel)\b")


def names_in(chunk):
    """Literal node names in this picture that can be dumped by name."""
    out = []
    for raw in NODE_NAMED.findall(chunk):
        name = raw.strip()
        # skip computed names (\i), coordinates, and anything non-identifier
        if not name or "\\" in name or not re.fullmatch(r"[A-Za-z][\w-]*", name):
            continue
        if name not in out:
            out.append(name)
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("src")
    ap.add_argument("dst")
    ap.add_argument(
        "--preamble-hook",
        default=r"\begin{document}",
        help="where to inject the QA macros (default: after \\begin{document})",
    )
    args = ap.parse_args()

    try:
        src = open(args.src, "r").read()
    except OSError as exc:
        print(f"cannot read {args.src}: {exc}", file=sys.stderr)
        return 2

    if "\\begin{tikzpicture}" not in src:
        print(f"{args.src}: no tikzpicture found", file=sys.stderr)
        return 2

    # 1. inject macros after \begin{document}
    if args.preamble_hook in src:
        src = src.replace(args.preamble_hook, args.preamble_hook + QA_PREAMBLE, 1)
    else:
        print(
            f"warning: '{args.preamble_hook}' not found; "
            "QA macros inserted before the first picture instead",
            file=sys.stderr,
        )
        src = src.replace("\\begin{tikzpicture}", QA_PREAMBLE + "\n\\begin{tikzpicture}", 1)

    # 2. inject a dump call before every \end{tikzpicture}
    out, cursor, total, skipped = [], 0, 0, 0
    for m in PICTURE_END.finditer(src):
        start_of_pic = src.rfind("\\begin{tikzpicture}", cursor, m.start())
        chunk = src[start_of_pic if start_of_pic != -1 else cursor : m.start()]
        names = names_in(chunk)
        dump = "".join(f"\\qadump{{{n}}}" for n in names)
        if names:
            total += len(names)
        if not names:
            skipped += 1
        out.append(src[cursor : m.start()])
        # dump first, then re-emit the original \end{tikzpicture} we matched
        out.append(dump + "\n\\qapicture\n" + m.group(0) + "\n")
        cursor = m.end()
    out.append(src[cursor:])

    try:
        with open(args.dst, "w") as fh:
            fh.write("".join(out))
    except OSError as exc:
        print(f"cannot write {args.dst}: {exc}", file=sys.stderr)
        return 2

    print(
        f"instrumented {total} named node(s) across "
        f"{len(PICTURE_END.findall(src))} picture(s) -> {args.dst}"
    )
    if skipped:
        print(f"  {skipped} picture(s) had no named nodes to check")
    if total == 0:
        print(
            "  note: no literal node names found. Name your nodes "
            "((enc), (layer1), ...) — anonymous nodes cannot be checked.",
            file=sys.stderr,
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
