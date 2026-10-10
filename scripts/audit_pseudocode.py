#!/usr/bin/env python3
"""Mechanical audit for a LaTeX pseudocode block.

Checks the objectively checkable half of the algorithm rules in
references/style-conventions.md, section "Algorithms": line budget, step length,
sentence-shaped steps, \\emph inside a step, and whether the math macros used in
the body appear in the notation file.

Usage:
    python3 audit_pseudocode.py listing.tex
    python3 audit_pseudocode.py paper.tex --env algorithmic
    python3 audit_pseudocode.py listing.tex --notation notation.tex --max-words 12

Exit status is 0 when no check FAILs, 1 otherwise. Warnings do not fail.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# `algorithmic` spends a line number on structure macros AND on their
# terminators (ENDIF/ENDFOR call \ALC@it unless the `noend` option is passed),
# but not on \REQUIRE/\ENSURE, which are \item[...] labels.
STEP_MACROS = ("STATE", "State", "STMT", "item")
STRUCT_MACROS = (
    "FOR", "For", "ENDFOR", "EndFor", "IF", "If", "ENDIF", "EndIf",
    "ELSE", "Else", "ELSIF", "ElsIf", "WHILE", "While", "ENDWHILE", "EndWhile",
    "REPEAT", "Repeat", "UNTIL", "Until", "LOOP", "Loop", "ENDLOOP", "EndLoop",
)
TERMINATORS = ("REQUIRE", "Require", "ENSURE", "Ensure",
               "INPUTS", "INPUT", "OUTPUTS", "OUTPUT")

STEP_RE = re.compile(r"\\(" + "|".join(STEP_MACROS) + r")\b(.*)$")
STRUCT_RE = re.compile(r"\\(" + "|".join(STRUCT_MACROS) + r")\b(.*)$")
TERM_RE = re.compile(r"\\(" + "|".join(TERMINATORS) + r")\b(.*)$")

DROP_CMDS = re.compile(
    r"\\(?:emph|textit|textbf|textsc|mathrm|mathbf|mathcal|text|hfill|quad"
    r"|qquad|label|cref|Cref|ref|eqref)\b"
)


def strip_latex(s: str) -> str:
    """Drop comments and LaTeX commands; each math span counts as one word.

    Masking math is what makes the word count meaningful: without it a single
    displayed quantity expands into a dozen fragments and every step looks long.
    """
    s = re.sub(r"%.*$", "", s)
    s = re.sub(r"\\(?:COMMENT|Comment)\s*\{.*?\}", " ", s, flags=re.S)
    s = re.sub(r"\$\$[^$]*\$\$", " X ", s)
    s = re.sub(r"\$[^$]*\$", " X ", s)
    s = re.sub(r"\\\((.*?)\\\)", " X ", s)
    s = DROP_CMDS.sub(" ", s)
    s = re.sub(r"\\[A-Za-z]+\b\s*", " ", s)
    s = re.sub(r"[{}]", " ", s)
    return " ".join(s.split())


def extract_env(text: str, name: str) -> list[str]:
    pat = re.compile(
        r"\\begin\{" + re.escape(name) + r"\}(.*?)\\end\{" + re.escape(name) + r"\}",
        re.S,
    )
    return [m.group(1) for m in pat.finditer(text)]


def split_steps(body: str) -> list[tuple[str, str, str]]:
    """Split a listing body into (kind, macro, rest) triples, in order."""
    out = []
    for line in body.splitlines():
        for kind, rx in (("step", STEP_RE), ("struct", STRUCT_RE),
                         ("term", TERM_RE)):
            m = rx.match(line.strip())
            if m:
                out.append((kind, m.group(1), m.group(2).strip()))
                break
    return out


def math_spans(line: str) -> list[str]:
    return re.findall(r"\$([^$]+)\$", line) + re.findall(r"\\\((.*?)\\\)", line)


def math_macros(text: str) -> set[str]:
    """LaTeX command names used inside math, e.g. pi, vtheta, gets, varnothing.

    This is the checkable part of symbol hygiene: a body that uses \\vtheta
    while the notation table defines only \\theta is a real defect, and command
    names survive tokenisation cleanly where sub/superscript trees do not.
    """
    out: set[str] = set()
    for span in math_spans(text):
        out |= set(re.findall(r"\\([A-Za-z]+)", span))
    return out


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    ap.add_argument("path", type=Path, help="LaTeX file or fragment")
    ap.add_argument("--env", default="algorithmic", help="environment to extract")
    ap.add_argument("--budget", type=int, default=20,
                    help="numbered-line readability target (exceeding it warns)")
    ap.add_argument("--max-words", type=int, default=12, help="max words per step")
    ap.add_argument("--notation", type=Path, default=None,
                    help="optional .tex file whose tokens count as declared")
    args = ap.parse_args()

    if not args.path.exists():
        print(f"error: {args.path} not found", file=sys.stderr)
        return 2

    text = args.path.read_text(encoding="utf-8", errors="replace")
    bodies = extract_env(text, args.env) or [text]

    declared = set()
    if args.notation and args.notation.exists():
        declared |= math_macros(
            args.notation.read_text(encoding="utf-8", errors="replace")
        )

    failures = warnings = 0

    for idx, body in enumerate(bodies, 1):
        print(f"\n=== block {idx} of {len(bodies)} ({args.env}) ===")
        numbered = [s for s in split_steps(body) if s[0] in ("step", "struct")]

        long_steps, sentenced, emphasized = [], [], []
        body_macros: set[str] = set()

        for n, (_kind, _macro, rest) in enumerate(numbered, 1):
            plain = strip_latex(rest)
            if len(plain.split()) > args.max_words:
                long_steps.append((n, len(plain.split()), plain))

            head = re.split(r"\\(?:COMMENT|Comment)|%", rest)[0]
            if re.search(r"[A-Za-z]\s*\.\s*$", head.rstrip()):
                sentenced.append((n, plain))

            if re.search(r"\\(?:emph|textit)\b", rest):
                emphasized.append((n, plain))

            body_macros |= math_macros(rest)

        if len(numbered) > args.budget:
            print(f"warn  line budget: {len(numbered)} numbered lines, "
                  f"readability target {args.budget}; review compaction")
            warnings += 1
        else:
            print(f"pass  line budget: {len(numbered)} / {args.budget}")

        if long_steps:
            print(f"FAIL  {len(long_steps)} step(s) over {args.max_words} words:")
            for n, w, plain in long_steps:
                print(f"        line {n}: {w} words -- {plain[:88]}")
            failures += 1
        else:
            print(f"pass  step length: every step within {args.max_words} words")

        if sentenced:
            print(f"FAIL  {len(sentenced)} step(s) terminated by a period:")
            for n, plain in sentenced:
                print(f"        line {n}: {plain[:88]}")
            failures += 1
        else:
            print("pass  fragments: no step ends in a period")

        if emphasized:
            print(f"warn  {len(emphasized)} step(s) use \\emph/\\textit in the body:")
            for n, plain in emphasized:
                print(f"        line {n}: {plain[:88]}")
            warnings += 1

        # LaTeX's own math macros are always available; only report a macro that
        # is neither built-in nor declared in the notation file.
        builtin = {
            "gets", "varnothing", "sum", "prod", "frac", "log", "exp", "min",
            "max", "mid", "cdot", "times", "le", "ge", "in", "to", "sim",
            "mathcal", "mathrm", "mathbf", "text", "left", "right", "quad",
            "infty", "nabla", "partial", "hat", "bar", "tilde", "overline",
            "underbrace", "begin", "end", "triangleright", "textit", "hfill",
            "theta", "pi", "mu", "sigma", "omega", "kappa", "epsilon", "rho",
            "lambda", "alpha", "beta", "gamma", "tau", "vx", "vy", "vtheta",
            "R", "T", "G", "A", "S", "P", "c", "h", "s", "a", "y", "x", "t",
            "i", "j", "k", "n", "l", "D", "J", "L", "H", "V", "K", "N",
        }
        if args.notation:
            undeclared = sorted(
                m for m in body_macros if m not in declared and m not in builtin
            )
            if undeclared:
                print(f"warn  {len(undeclared)} math macro(s) used in the body are "
                      f"absent from the notation file:")
                print("        " + ", ".join(undeclared[:40]))
                warnings += 1
            else:
                print("pass  symbol coverage: every body macro is in the notation file")
        else:
            print("note  symbol coverage skipped (pass --notation to enable)")

    print(f"\n{failures} failure(s), {warnings} warning(s)")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
