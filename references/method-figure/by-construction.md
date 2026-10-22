# Layout by construction

The core proposition of this skill: **prevent by construction, do not detect and
then fix.**

Detecting works on the cheap defects and fails on the expensive ones. A
figure can pass every automated check and still break catastrophically the first
time someone edits it — because the *writing method*, not the checker, is what
makes a figure safe to change.

## The five idioms

### 1. Layout rhythm lives in exactly one place

```latex
\newlength{\stagew}\setlength{\stagew}{4.5cm}   % change once, whole figure follows
\def\gap{0.5cm}
\tikzset{node distance=\gap}
```

The anti-pattern is hand-copying the same number into five places: zone bounds,
content centres, arrow coordinates, a summary bar, and the legend. Five copies
means five things to keep in sync, and nobody ever keeps five things in sync.

### 2. Place by relative positioning, never absolute `at (x,y)`

```latex
\node[zone] (s1) at (0,0) {};
\node[zone, right=of s1] (s2) {};    % spacing comes from node distance
\node[zone, right=of s2] (s3) {};    % widen s2 and s3 shifts automatically

% ✗ \node[zone] (s2) at (5,0) {};    % hand-typed 5; now editing s1's width
%                                     % requires editing this too
```

Grids use `\matrix`, pipelines use `chains`. Do not manually add 2cm to an x.

**The documented exception.** When you need *exact equal spacing across repeated
columns* — sequence-diagram participants, side-by-side comparison columns —
prefer absolute `at (x,y)`. Relative positioning accumulates drift through
nesting, so `right=of` chains of chains stop being equal. Both idioms are
correct; the question is whether you want *responsive* spacing or *equal* spacing.

### 3. Connections ride node anchors; never re-type boundary coordinates

```latex
\draw[flow] (s1.east) -- (s2.west);        % cannot misalign under reflow
\foreach \a/\b in {s1/s2, s2/s3} \draw[flow] (\a.east) -- (\b.west);

% ✗ \draw[flow] (4.5,5) -- (5.0,5);        % re-copied the zone boundary
```

This one rule kills the majority of bugs in a review loop, because an arrow that
references nodes cannot point at the wrong place after a relayout.

### 4. Containers use `fit`; text wraps with `text width`

```latex
\node[fit=(a)(b)(c), draw, rounded corners] {};   % zone wraps its contents
\node[box, text width=3.2cm, align=center] {long labels wrap instead of overflow};

% ✗ minimum width=3.2cm  -> a long label widens the box until it escapes the zone
```

**Why this matters more than it looks.** `text width` converts a *collision bug*
— hard, must fix — into a *bit tight, one more line* — soft, aesthetic. LaTeX's
text metrics are not perfectly predictable, so a label occasionally wraps
unexpectedly. With `text width` that is a cosmetic surprise; without it, it is an
overlap.

Use `minimum width`/`minimum height` only for sizing a box *independent* of its
text, and when you do, always add `align` too.

### 5. Centre with a `calc` midpoint; do not hand-compute

```latex
\usetikzlibrary{calc}
\coordinate (c) at ($(s1.north west)!0.5!(s5.north east)$);
\node[anchor=south] at ($(c)+(0,0.6)$) {title};
```

Add a stage, widen the hero, and the title re-centres itself.

**Sub-idiom: embedded visuals travel with their parent.**

```latex
\begin{scope}[shift={(parent.center)}]      % local coords; follows parent anywhere
  \foreach \i in {1,...,5}\foreach \j in {1,...,5}{
    \fill[accent!40] ({(\j-3)*\cs},{(3-\i)*\cs}) rectangle ++(\cs,\cs); }
\end{scope}
```

Local hand-drawing inside a viz is fine — heatmap cells, bars, an inset plot —
but anchor it to the parent so it moves with it.

## Why this is the load-bearing rule

**A measured A/B on a real paper figure, not a hypothetical.** The same
two-branch method figure was written both ways and then given one natural edit —
widen the loss box — as a single changed line in each:

| | Absolute coordinates | By construction |
| --- | --- | --- |
| The edit | `text width=5.95cm` → `6.60cm` (one literal) | `\lossw{5.95cm}` → `{6.60cm}` (one declared value) |
| Result | Loss box overflows its zone on **both** sides; the zone border runs through it; every downstream coordinate still refers to the old geometry | Zone grows to contain the box, branch 2 shifts right, spine and rail follow, canvas re-flows |
| Nodes the gate can see | **10** (of ~30 elements; the rest are anonymous nodes and raw paths) | **37** (every element is named) |
| Gate verdict | **CLEAN** — while the render is visibly broken | CLEAN, and correct |

The two rows that matter are the last two. The absolute version's failure is
**invisible to the gate**, because the zone border it violates is a raw `\draw`
path, not a node — and most of the figure's elements were anonymous, so the
geometry pass never looked at them. Naming everything is what turns the gate from
a formality into coverage.

The same pilot surfaced three latent defects that had been sitting in the
"shipped" figure the whole time, all of them real: a note overlapping its own
frame by 0.12cm, a rail label grazing both zone borders by 0.02cm, and a tile run
drawn from the wrong end of its anchor node so that it hung half a tile into the
label beneath it. None were visible to the 10-node gate. That is the argument for
construction *and* for naming.

**Two structural patterns worth copying out of that pilot:**

- **Build a frame inside-out.** Lay out the contents first, then `fit` the frame
  around them. The frame then cannot overlap its own contents — if the contents
  grow, the frame grows. Building the frame first and placing contents into it
  guarantees that a long label eventually collides with the border.
- **Fit the title into its own zone.** A zone title painted on top of a zone
  reads to the geometry pass as an overlap; the same title passed as a `fit`
  child reads as the containment it actually is. Place the title before the
  rectangle and include it in the `fit`.

## Pre-flight before you compile

Cheap to do, expensive to skip.

- [ ] Every spacing value is a `\def` or `\newlength`, defined once
- [ ] No absolute `at (x,y)` except a deliberate equal-spacing exception
- [ ] Every arrow references node anchors, not literal coordinates
- [ ] Every box that holds text declares `text width` + `align`
- [ ] Every container uses `fit` and sits on the background layer
- [ ] Every node that a later edit might target has a semantic name
- [ ] Font sizes are relative (`\small`, `\footnotesize`) or a single declared scale
