#!/usr/bin/env bash
# Method-figure QA gate.
#
# Runs the cheap checks first and stops at the first hard failure, so you never
# pay for a render that was already doomed:
#
#   1. static lint        (source hazards, no TeX needed)
#   2. instrument+compile (the figure must build standalone)
#   3. glyph gate         (xelatex fails *silently* on missing fonts)
#   4. geometry           (exact node boxes: overlaps, off-canvas, tight gaps)
#   5. type size          (effective pt at the real print width)
#   6. render a PNG       (a human/agent must still look at it)
#
# Usage: qa.sh figure.tex [--venue iclr] [--min-gap-cm 0.4] [--keep]
#
# Exit: 0 pass (warnings allowed), 1 hard failure, 2 setup error.

set -uo pipefail

SRC=""
VENUE="iclr"
MIN_GAP="0.4"
KEEP=0
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

while [ $# -gt 0 ]; do
  case "$1" in
    --venue) VENUE="$2"; shift 2 ;;
    --min-gap-cm) MIN_GAP="$2"; shift 2 ;;
    --keep) KEEP=1; shift ;;
    -h|--help) sed -n '2,20p' "$0"; exit 0 ;;
    *) SRC="$1"; shift ;;
  esac
done

if [ -z "$SRC" ] || [ ! -f "$SRC" ]; then
  echo "usage: qa.sh <figure.tex> [--venue V] [--min-gap-cm G] [--keep]" >&2
  exit 2
fi
for tool in python3 xelatex; do
  command -v "$tool" >/dev/null 2>&1 || { echo "missing required tool: $tool" >&2; exit 2; }
done

BASE="$(basename "$SRC" .tex)"
BUILD="$(mktemp -d "${TMPDIR:-/tmp}/methodfig.XXXXXX")"
HARD=0
cleanup() { [ "$KEEP" -eq 1 ] || rm -rf "$BUILD"; }
trap cleanup EXIT

hr() { printf '%s\n' "------------------------------------------------------------"; }

echo "method-figure QA: $SRC"
echo "build: $BUILD"
hr

# ---- 1. static lint ------------------------------------------------------
echo "[1/6] static lint"
python3 "$HERE/lint_static.py" "$SRC" || HARD=1
hr

# ---- 2. instrument + compile --------------------------------------------
echo "[2/6] instrument + compile"
python3 "$HERE/instrument.py" "$SRC" "$BUILD/$BASE.qa.tex" || { echo "instrumentation failed"; exit 2; }
( cd "$BUILD" && xelatex -interaction=nonstopmode -halt-on-error "$BASE.qa.tex" >/dev/null 2>&1 )
if [ ! -f "$BUILD/$BASE.qa.pdf" ]; then
  echo "COMPILE FAILED -> first errors:"
  grep -m3 -A3 '^!' "$BUILD/$BASE.qa.log" 2>/dev/null | sed 's/^/    /'
  exit 1
fi
echo "compiled OK"
hr

# ---- 3. glyph gate ------------------------------------------------------
# xelatex emits no error for an unresolvable font; glyphs silently vanish.
echo "[3/6] glyph gate"
MC="$(grep -c 'Missing character' "$BUILD/$BASE.qa.log" 2>/dev/null || true)"
MC="${MC:-0}"
if [ "$MC" -gt 0 ]; then
  echo "FAIL: $MC 'Missing character' line(s) — a font is not resolving."
  grep -m3 'Missing character' "$BUILD/$BASE.qa.log" | sed 's/^/    /'
  HARD=1
else
  echo "no missing characters"
fi
hr

# ---- 4. geometry --------------------------------------------------------
echo "[4/6] geometry"
if [ -f "$BUILD/$BASE.qa.qa" ]; then
  python3 "$HERE/check_geometry.py" "$BUILD/$BASE.qa.qa" --min-gap-cm "$MIN_GAP" || HARD=1
else
  echo "  no geometry dump produced (were any nodes named?)"
fi
hr

# ---- 5. type size at print width ---------------------------------------
echo "[5/6] effective type size"
if [ -f "$BUILD/$BASE.qa.qa" ]; then
  python3 "$HERE/check_fontsize.py" "$SRC" --qa "$BUILD/$BASE.qa.qa" --venue "$VENUE" || HARD=1
else
  echo "  skipped (no canvas width)"
fi
hr

# ---- 6. render for the human -------------------------------------------
echo "[6/6] render for inspection"
PNG="${BASE}.qa.png"
# qlmanage first: it flattens onto white. sips keeps the page transparent,
# which some viewers composite onto black and a review pass then misreads.
if command -v qlmanage >/dev/null 2>&1; then
  qlmanage -t -s 2400 -o "$BUILD" "$BUILD/$BASE.qa.pdf" >/dev/null 2>&1 \
    && mv "$BUILD/$BASE.qa.pdf.png" "$BUILD/$PNG" 2>/dev/null \
    && echo "  $BUILD/$PNG"
fi
if [ ! -f "$BUILD/$PNG" ] && command -v sips >/dev/null 2>&1; then
  sips -s format png --resampleWidth 1600 "$BUILD/$BASE.qa.pdf" --out "$BUILD/$PNG" >/dev/null 2>&1 \
    && echo "  $BUILD/$PNG (sips: page background may read as transparent)"
fi
if [ ! -f "$BUILD/$PNG" ] && command -v pdftoppm >/dev/null 2>&1; then
  pdftoppm -png -r 200 -singlefile "$BUILD/$BASE.qa.pdf" "$BUILD/${BASE}.qa" >/dev/null 2>&1 \
    && echo "  $BUILD/${BASE}.qa.png"
fi
[ -f "$BUILD/$PNG" ] || echo "  no PNG renderer (qlmanage/sips/pdftoppm) — inspect the PDF directly"
hr

if [ "$HARD" -eq 0 ]; then
  cat <<'EOF'
CLEAN on the mechanical gates.

This is a floor, not a ceiling. The checkers cannot see:
  - whether the figure argues the right thing
  - whether a connector route reads naturally
  - whether the composition has a focal point
  - anywhere a line crosses a label (paths are not instrumented)
Look at the rendered PNG before delivering, and read
references/review-checklist.md.
EOF
else
  echo "HARD FAILURES above. Fix them, then re-run."
fi
exit "$HARD"
