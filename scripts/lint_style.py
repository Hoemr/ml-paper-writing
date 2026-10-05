#!/usr/bin/env python3
"""Mechanical style lint for ML-paper LaTeX sources.

Covers the objectively checkable rules from references/style-conventions.md
and references/reviewer-guidelines.md so the delivery audit (SKILL.md) can
re-check them at delivery time instead of trusting rules read earlier in a
long session. Judgment-call gates (over-claiming nuance, defensive writing,
chapter patterns) stay with the fresh-context reviewer; this script only
flags candidates for triage.

Findings carry two severities:
    flag    fix the finding or state why it stands
    triage  judge in context; the rule has legitimate exceptions

Checks:
    cref          manual "Table~/Eq.~\\ref{...}" prefixes instead of \\cref
    header-cell   table header cell starting with a lowercase word
    artifact      named model/dataset/benchmark without a \\cite in its paragraph
    rhetoric      over-claim or empty-reassurance phrasing
    rhetoric-soft wording that needs judgment (significant(ly), optimal, ...)
    punctuation   semicolon chains and explanatory dashes in one paragraph
    macro-use     \\newcommand macro used 0 or 1 times in the analyzed files
    bib-missing   \\cite key absent from the .bib files passed via --bib
    log-overfull  Overfull \\hbox/\\vbox count in the build log passed via --log
    log-undefined undefined citations/references in the build log

Usage:
    python3 lint_style.py paper.tex section2.tex --bib refs.bib --log main.log
    python3 lint_style.py chapters/              # every .tex below a directory

Coverage is exactly the files passed; \\input/\\include are not followed.
Exit status is 0 when no flag-severity finding remains, 1 otherwise, and 2
on usage errors.
"""

from __future__ import annotations

import argparse
import re
import sys
from bisect import bisect_right
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

FLAG, TRIAGE = "flag", "triage"

CITE_RE = re.compile(
    r"\\(?:cite|Cite|citep|Citep|citet|Citet|citealp|Citealp|citealt|"
    r"citeauthor|citeyear|parencite|Parencite|textcite|Textcite|autocite|"
    r"footcite|smartcite|footfullcite)\*?(?:\[[^\]]*\]){0,2}\{([^}]*)\}"
)

CREF_RE = re.compile(
    r"\b(?:Tables?|Figures?|Fig\.|Figs\.|Sections?|Sec\.|Secs\.|Equations?|"
    r"Eqs?\.|Chapters?|Appendix|Appendices|Algorithms?|Alg\.)"
    r"~?\s*\(?\s*\\(?:ref|eqref|autoref|cref|Cref)\b"
)

ARTIFACT_PATTERNS = [
    "ImageNet", "COCO", "CIFAR-?10(?:0)?", "MNIST", "Fashion-?MNIST", "SVHN",
    "GLUE", "SuperGLUE", "SQuAD", "MMLU", "GSM8K", "HumanEval", "MBPP",
    "BIG-?bench", "HELM", "WikiText-?10[23]", "The Pile", "LAION",
    "LibriSpeech", "WMT'?1[0-9]", "IWSLT", "Alpaca", "ShareGPT", "Vicuna",
    "LLaMA", "Llama-?\\d", "GPT-(?:2|3|4)(?:\\.5|o)?", "BERT", "RoBERTa",
    "DeBERTa", "T5", "FLAN", "BLOOM", "ResNet-?\\d+", "ViT", "DeiT", "CLIP",
    "Whisper", "Stable Diffusion", "Qwen", "Mistral", "Mixtral", "DeepSeek",
]

# (severity, pattern, message)
RHETORIC = [
    (FLAG, r"\b(?:extensive|comprehensive)\s+(?:experimental\s+)?"
           r"(?:experiments|evaluations?|empirical\s+(?:study|studies|evaluations?))\b",
     "unsupported broadening: state what was run, on what scope "
     "[writing-guide §Abstract/Introduction]"),
    (FLAG, r"\bdemonstrat\w+\s+the\s+(?:effectiveness|superiority|efficacy|"
           r"robustness)\b",
     "claim without a stated comparator and scope [writing-guide §Experiments]"),
    (FLAG, r"\bnovel\b",
     "novelty adjective: replace with the actual distinction "
     "[writing-guide §Evidence before prose]"),
    (FLAG, r"\bstate[-\s]of[-\s]the[-\s]art\b",
     "unsupported SOTA claim: replace with the supported statement "
     "[reviewer-guidelines §Defensive writing]"),
    (FLAG, r"\bremarkable\s+(?:progress|improvements?|gains?|performance)\b",
     "decorative intensifier [writing-guide §Reader expectations]"),
    (TRIAGE, r"\bsignificant(?:ly)?\b",
     "statistical claim? support it with a test and uncertainty units, or "
     "weaken the wording [style-conventions §Tables]"),
    (TRIAGE, r"\boptimal(?:ly)?\b",
     "is this optimality proved or scoped? [reviewer-guidelines]"),
    (TRIAGE, r"\bwe\s+(?:believe|stress|emphasize)\b",
     "rhetoric that argues with an imagined criticism "
     "[reviewer-guidelines §Defensive writing]"),
    (TRIAGE, r"\bIt\s+should\s+be\s+(?:noted|emphasized|stressed|mentioned)\b",
     "empty reassurance pattern [reviewer-guidelines §Defensive writing]"),
    (TRIAGE, r"\bwe\s+(?:previously|originally)\s+\w+",
     "internal revision diary in prose [reviewer-guidelines §Defensive writing]"),
    (TRIAGE, r"\bthe\s+first\s+(?:to|method|approach|work)\b",
     "priority claim: verify against the closest work [reviewer-guidelines]"),
]

TAB_ENVS = ("tabular", "tabular*", "tabularx", "longtable", "longtabu")
TAB_BEGIN_RE = re.compile(
    r"\\begin\{(" + "|".join(re.escape(e) for e in TAB_ENVS) + r")\}"
)
WRAP_RE = re.compile(
    r"\\(?:multicolumn|multirow|makecell|thead|shortstack|textbf|text|"
    r"textsc|texttt|textnormal|textit|rotatebox|raisebox)\*?(?:\[[^\]]*\])?"
)
MACRO_DEF_RE = re.compile(
    r"\\(?:(?:re|provide)?newcommand\*?|DeclareMathOperator\*?|[exg]?def)"
    r"(?![A-Za-z@])\s*\*?\s*"
    r"(?:\{\\([A-Za-z@]+)\}|\\([A-Za-z@]+))"
)
BIB_ENTRY_RE = re.compile(r"@(\w+)\s*\{\s*([^,\s{}]+)\s*,")


@dataclass
class Finding:
    file: Path
    line: int
    sev: str
    check: str
    msg: str


class LineMap:
    """Offsets in comment-stripped text still map to original line numbers."""

    def __init__(self, text: str):
        self.starts = [0] + [m.end() for m in re.finditer("\n", text)]

    def line(self, offset: int) -> int:
        return bisect_right(self.starts, offset)


def strip_comments(text: str) -> str:
    return re.sub(r"(?<!\\)%.*", "", text)


def split_paragraphs(text: str) -> list[tuple[int, int]]:
    spans = []
    begin = 0
    for m in re.finditer(r"\n\s*\n", text):
        if m.start() > begin:
            spans.append((begin, m.start()))
        begin = m.end()
    if begin < len(text):
        spans.append((begin, len(text)))
    return spans


def matching_brace(s: str, i: int) -> int:
    """Index of the '}' closing the '{' at s[i], or -1."""
    depth = 0
    for j in range(i, len(s)):
        if s[j] == "{":
            depth += 1
        elif s[j] == "}":
            depth -= 1
            if depth == 0:
                return j
    return -1


def first_row_end(body: str) -> int:
    """Offset of the first top-level \\\\ row terminator, or -1."""
    depth = 0
    i, n = 0, len(body)
    while i < n:
        c = body[i]
        if c == "\\":
            if i + 1 < n and body[i + 1] == "\\" and depth == 0:
                return i
            i += 2
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth = max(0, depth - 1)
        i += 1
    return -1


def top_level_cells(header: str) -> list[str]:
    cells, depth, start = [], 0, 0
    i, n = 0, len(header)
    while i < n:
        c = header[i]
        if c == "\\":
            i += 2
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth = max(0, depth - 1)
        elif c == "&" and depth == 0:
            cells.append(header[start:i])
            start = i + 1
        i += 1
    cells.append(header[start:])
    return cells


def unwrap_last_group(s: str) -> str:
    """Replace \\multicolumn{..}{..}{TEXT}-style wrappers with TEXT."""
    prev = None
    while prev != s:
        prev = s
        m = WRAP_RE.search(s)
        if not m:
            break
        i, depth, start, last = m.end(), 0, -1, (-1, -1)
        while i < len(s):
            c = s[i]
            if c == "{":
                if depth == 0:
                    start = i
                depth += 1
            elif c == "}":
                depth -= 1
                if depth == 0:
                    last = (start, i)
            elif c == "&" and depth == 0:
                break
            i += 1
        if last[0] == -1:
            s = s[:m.start()] + s[m.end():]
        else:
            s = s[:m.start()] + s[last[0] + 1:last[1]] + s[last[1] + 1:]
    return s


def clean_cell(cell: str) -> str:
    s = unwrap_last_group(cell)
    s = re.sub(r"\\\\(?:\[[^\]]*\])?", " ", s)
    s = re.sub(r"\$[^$]*\$", " ", s)
    s = re.sub(r"\\\((.*?)\\\)", " ", s, flags=re.S)
    s = re.sub(r"\\[A-Za-z@]+\*?", " ", s)
    s = re.sub(r"[{}~^_]", " ", s)
    return " ".join(s.split())


def check_cref(path: Path, text: str, lines: LineMap) -> list[Finding]:
    out = []
    for m in CREF_RE.finditer(text):
        out.append(Finding(
            path, lines.line(m.start()), TRIAGE, "cref",
            f'manual prefix "{m.group(0).strip()}" — prefer \\cref/\\Cref with '
            "abbreviated names when the venue supports cleveref "
            "[style-conventions §Cross-references]"))
    return out


def check_headers(path: Path, text: str, lines: LineMap) -> list[Finding]:
    out = []
    for m in TAB_BEGIN_RE.finditer(text):
        env = m.group(1)
        endm = re.compile(r"\\end\{" + re.escape(env) + r"\}").search(text, m.end())
        if not endm:
            continue
        i = m.end()
        opt = re.match(r"\s*\[[^\]]*\]", text[i:])
        if opt:
            i += opt.end()
        if i < len(text) and text[i] == "{":
            cb = matching_brace(text, i)
            if cb == -1:
                continue
            i = cb + 1
        body = text[i:endm.start()]
        row_end = first_row_end(body)
        if row_end == -1:
            continue
        for cell in top_level_cells(body[:row_end]):
            cleaned = clean_cell(cell)
            lm = re.match(r"[a-z]{2,}", cleaned)
            if lm:
                out.append(Finding(
                    path, lines.line(m.start()), FLAG, "header-cell",
                    f'table header cell not capitalized: "{lm.group(0)}…" '
                    "[style-conventions §Tables: capitalise every header cell]"))
    return out


def check_artifacts(path: Path, text: str, paras: list[tuple[int, int]],
                    lines: LineMap, extra: list[str]) -> list[Finding]:
    out = []
    for src in ARTIFACT_PATTERNS + list(extra):
        m = re.search(r"\b(?:" + src + r")\b", text)
        if not m:
            continue
        para = next((text[s:e] for s, e in paras if s <= m.start() < e), "")
        if not CITE_RE.search(para):
            out.append(Finding(
                path, lines.line(m.start()), FLAG, "artifact",
                f'"{m.group(0)}" at first use without a \\cite in its paragraph '
                "[style-conventions §Prose: name and cite every artifact]"))
    return out


def check_rhetoric(path: Path, text: str, lines: LineMap) -> list[Finding]:
    out = []
    for sev, rx, msg in RHETORIC:
        for m in re.finditer(rx, text, re.IGNORECASE):
            out.append(Finding(
                path, lines.line(m.start()), sev,
                "rhetoric" if sev == FLAG else "rhetoric-soft",
                f'"{m.group(0)}" — {msg}'))
    return out


def check_punctuation(path: Path, text: str, paras: list[tuple[int, int]],
                      lines: LineMap) -> list[Finding]:
    out = []
    for s, e in paras:
        t = text[s:e]
        semis = t.count(";")
        if semis >= 3:
            out.append(Finding(
                path, lines.line(s), TRIAGE, "punctuation",
                f"{semis} semicolons in one paragraph — several is the "
                "ceiling; split into sentences "
                "[style-conventions §Prose and structure]"))
        dashes = len(re.findall(r"---|(?<= )--(?= )", t))
        if dashes >= 2:
            out.append(Finding(
                path, lines.line(s), TRIAGE, "punctuation",
                f"{dashes} explanatory dashes in one paragraph — prefer a "
                "sentence, a colon, or short parentheses "
                "[style-conventions §Prose and structure]"))
    return out


def check_macros(texts: dict[Path, tuple[str, LineMap]]) -> list[Finding]:
    defs: dict[str, list[tuple[Path, int, int]]] = {}
    for path, (text, _) in texts.items():
        for m in MACRO_DEF_RE.finditer(text):
            name = m.group(1) or m.group(2)
            defs.setdefault(name, []).append((path, m.start(), m.end()))

    # Unused definitions get one aggregated finding: a manuscript preamble
    # defines many macros for optional sections, and per-name lines would
    # drown the single-use signal that the notation rule actually targets.
    out, unused = [], []
    anchor: tuple[Path, int] | None = None
    for name in sorted(defs):
        use_re = re.compile(r"\\" + re.escape(name) + r"(?![A-Za-z@])")
        real: list[tuple[Path, int]] = []
        for path, (text, lines) in texts.items():
            for um in use_re.finditer(text):
                if not any(dp == path and ds <= um.start() < de
                           for dp, ds, de in defs[name]):
                    real.append((path, um.start()))
        if not real:
            unused.append(name)
            if anchor is None:
                dpath, ds, _ = defs[name][0]
                anchor = (dpath, texts[dpath][1].line(ds))
        elif len(real) == 1:
            dpath, ds, _ = defs[name][0]
            out.append(Finding(
                dpath, texts[dpath][1].line(ds), TRIAGE, "macro-use",
                f"\\{name} used once — inline it unless it names a reused "
                "concept [style-conventions §Notation: no single-use "
                "intermediate variables]"))
    if unused:
        shown = ", ".join("\\" + n for n in unused[:8])
        more = f" …+{len(unused) - 8} more" if len(unused) > 8 else ""
        apath, aline = anchor
        out.append(Finding(
            apath, aline, TRIAGE, "macro-use",
            f"{len(unused)} macro(s) defined but unused in the analyzed "
            f"files (may be used in files not passed): {shown}{more}"))
    return out


def check_bib(texts: dict[Path, tuple[str, LineMap]],
              bib_paths: list[Path]) -> list[Finding]:
    bib_keys: set[str] = set()
    for bp in bib_paths:
        t = bp.read_text(encoding="utf-8", errors="replace")
        for m in BIB_ENTRY_RE.finditer(t):
            if m.group(1).lower() not in ("string", "comment", "preamble"):
                bib_keys.add(m.group(2))
    out, seen = [], set()
    for path, (text, lines) in texts.items():
        for m in CITE_RE.finditer(text):
            for key in m.group(1).split(","):
                key = key.strip()
                if key and key not in bib_keys and key not in seen:
                    seen.add(key)
                    out.append(Finding(
                        path, lines.line(m.start()), FLAG, "bib-missing",
                        f"\\cite key '{key}' not found in the provided .bib"))
    return out


def check_log(path: Path) -> list[Finding]:
    text = path.read_text(encoding="utf-8", errors="replace")
    out = []
    oh = len(re.findall(r"Overfull \\hbox", text))
    ov = len(re.findall(r"Overfull \\vbox", text))
    if oh or ov:
        out.append(Finding(
            path, 0, FLAG, "log-overfull",
            f"{oh} Overfull \\hbox, {ov} Overfull \\vbox in this build log — "
            "compare against the previous build; a regression is a defect "
            "[style-conventions §The verification loop]"))
    undef = re.findall(r"(?i)undefined (?:citation|reference)", text)
    if undef:
        out.append(Finding(
            path, 0, FLAG, "log-undefined",
            f"{len(undef)} undefined citation/reference warning(s) in the "
            "build log"))
    return out


def collect_tex(paths: list[Path]) -> list[Path]:
    files: list[Path] = []
    for p in paths:
        if p.is_dir():
            files += sorted(q for q in p.rglob("*.tex")
                            if not q.name.startswith("."))
        elif p.suffix == ".tex":
            files.append(p)
        else:
            print(f"warning: skipping non-.tex path {p}", file=sys.stderr)
    seen: set[Path] = set()
    out = []
    for f in files:
        r = f.resolve()
        if r not in seen:
            seen.add(r)
            out.append(f)
    return out


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    ap.add_argument("paths", nargs="+", type=Path,
                    help=".tex files or directories to lint")
    ap.add_argument("--bib", action="append", default=[], type=Path,
                    metavar="FILE",
                    help=".bib file(s) to resolve cite keys against")
    ap.add_argument("--log", type=Path, default=None, metavar="FILE",
                    help="build .log to check overfull boxes and undefined "
                         "references")
    ap.add_argument("--artifact", action="append", default=[], metavar="REGEX",
                    help="extra artifact name/regex that must carry a citation")
    args = ap.parse_args()

    files = collect_tex(args.paths)
    if not files:
        print("error: no .tex files found in the given paths", file=sys.stderr)
        return 2

    texts: dict[Path, tuple[str, LineMap]] = {}
    paras: dict[Path, list[tuple[int, int]]] = {}
    for f in files:
        raw = f.read_text(encoding="utf-8", errors="replace")
        text = strip_comments(raw)
        texts[f] = (text, LineMap(text))
        paras[f] = split_paragraphs(text)

    findings: list[Finding] = []
    for f, (text, lines) in texts.items():
        findings += check_cref(f, text, lines)
        findings += check_headers(f, text, lines)
        findings += check_artifacts(f, text, paras[f], lines, args.artifact)
        findings += check_rhetoric(f, text, lines)
        findings += check_punctuation(f, text, paras[f], lines)
    findings += check_macros(texts)
    if args.bib:
        findings += check_bib(texts, args.bib)
    if args.log:
        if args.log.exists():
            findings += check_log(args.log)
        else:
            print(f"warning: build log {args.log} not found", file=sys.stderr)

    findings.sort(key=lambda x: (str(x.file), x.line, x.check))
    for fd in findings:
        print(f"{fd.file}:{fd.line} [{fd.sev}] {fd.check}: {fd.msg}")

    flags = sum(1 for fd in findings if fd.sev == FLAG)
    detail = ", ".join(f"{k} {v}" for k, v in
                       sorted(Counter(fd.check for fd in findings).items()))
    print(f"\n== lint_style == {flags} flag, {len(findings) - flags} triage "
          f"across {len(files)} file(s)")
    if detail:
        print(f"by check: {detail}")
    return 1 if flags else 0


if __name__ == "__main__":
    sys.exit(main())
