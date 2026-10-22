# CV transformer visual styles

Use this reference after the design contract in `SKILL.md` and after the
construction rules in `by-construction.md` when the request asks for a modern
CV/Transformer method schematic: ViT-style patchification, Swin/window attention,
hierarchical vision backbones, Q/K/V attention insets, feature pyramids, or
"make it look like a real CV paper".

This file is a style grammar, not a license to copy a paper figure. Transfer the
visual decisions - patch grids, token strips, repeated blocks, window partitions,
stage bands, muted palettes - and redraw them for the current method's claim.

## The look to aim for

Modern CV method figures usually look polished because the geometry is disciplined,
not because they are visually elaborate.

- **Flat vector, shallow depth.** Use tints, repeated offset slabs, and clipped
  mini-grids. Avoid bevels, glow, drop shadows, gradients, and photo-like effects.
- **One quiet neutral structure plus one accent.** Backbone blocks, axes, and
  containers are grey; the novel module or changed operation gets the saturated
  stroke.
- **Tiny visuals, few words.** A 4x4 patch grid reads faster than "patch tokens";
  two shifted windows read faster than a paragraph about W-MSA/SW-MSA.
- **Regular rhythm.** Equal stage widths, equal window sizes, and aligned token
  strips make dense architectures feel intentional instead of crowded.
- **Zoom only where the novelty is.** Draw the whole backbone as stage bands, then
  spend detail on the window attention, patch merge, adapter, prompt, or decoder
  that the paper contributes.

The practical target is "could sit next to ViT/Swin-style figures without looking
like a screenshot", while still obeying this skill's hard rules: named nodes,
anchor-based connectors, wrapped labels, explicit palette names, and QA.

## Palette recipes

All recipes use low-saturation fills and darker strokes. If a hue carries meaning,
define it in the caption or legend and make the distinction survive grayscale by
also changing shape, position, or line style.

| Style family | Use for | Palette mapping |
| --- | --- | --- |
| **ViT patch/token** | Image -> patches -> token sequence -> transformer | image/patches = muted blue, tokens = orange tint, transformer = neutral grey slab, head/output = green or purple accent |
| **Swin/window attention** | W-MSA/SW-MSA, local windows, hierarchical stages | stages = blue -> teal -> green -> purple tints; active shifted window = orange stroke; inactive windows = grey or pale stage colour |
| **Encoder-decoder/FPN** | CNN/ViT encoder plus neck/decoder | encoder = cool hues, decoder = warm hue, skip/fusion = green, loss/supervision = grey dashed and labelled |
| **Attention internals** | Q/K/V, attention maps, cross-attention | Q/K/V = three related cool hues or three shapes; attention matrix = one sequential tint ramp; output/context = accent |
| **Baseline vs ours** | two-panel structural comparison | baseline = grey and thin, ours = same geometry plus one accent module; avoid recolouring everything |

Safe defaults:

```latex
\definecolor{cvBlue}{HTML}{4C78A8}
\definecolor{cvTeal}{HTML}{3B9AB2}
\definecolor{cvGreen}{HTML}{54A24B}
\definecolor{cvOrange}{HTML}{F58518}
\definecolor{cvPurple}{HTML}{8E6BBE}
\definecolor{cvInk}{HTML}{2B2F33}
\definecolor{cvGray}{HTML}{7A7F86}
```

Use fills around `!8` to `!18`, strokes around `!70!black` to `!85!black`, and
reserve one saturated stroke for the hero path. A figure with four saturated
families usually looks less like a paper and more like a slide deck.

## Shape grammar

Pick shapes by what the object is, then reuse them consistently.

| Object | Shape | Notes |
| --- | --- | --- |
| Input image | framed mini-grid or small thumbnail rectangle | The grid can be decorative texture inside one named node; do not attach arrows to individual cells unless they matter |
| Patch tokens | short horizontal strip of equal rounded cells | Good for ViT and token mixers; label the whole strip, not every token |
| Feature map | offset stack of rectangles | Spatial size is shown by rectangle size; channel depth by 2-4 offset slabs |
| Transformer block | repeated vertical slab with 2-3 internal rows | Usually one labelled block is enough; repeated N times with a small `x N` tag |
| Swin stage | fitted band containing block stack plus downsample marker | Draw four stage bands at decreasing map sizes; use direct labels for resolutions |
| Window partition | clipped grid with 2x2 or 4x4 window outlines | Show only a local zoom inset unless windowing is the whole method |
| Attention matrix | square heatmap tile block | Use a one-hue ramp; avoid rainbow |
| Patch merging/downsample | funnel, stride arrow, or small `2x` merge glyph | Keep the operation explicit; do not hide it in an arrow label |
| Loss | explicit node | Supervision arrows enter the loss node, not the model block |

## Layout recipes

### 1. ViT patchify pipeline

Use when the claim is "an image becomes a sequence and then a transformer handles
it".

Recommended reading path:

```text
image grid -> patch projection -> token strip (+ class token) -> transformer stack -> head
```

Area budget:

- left third: input grid plus patch/token transformation;
- middle third: compressed transformer stack;
- right third: task head or output;
- if the novelty is inside the transformer, compress patchification and zoom the
  block instead.

Visual details that make it read as CV, not generic ML:

- Draw the image as a named rectangle containing a small grid texture.
- Draw one patch pulled out or highlighted, then map it to one token cell.
- Use a short token strip with ellipsis, not all tokens.
- Add tensor labels only when they clarify the method: `H x W x 3`, `N x D`,
  `L x D`. Put them as small notes under shapes, not inside the primary labels.

### 2. Swin/hierarchical backbone

Use when the method has stages, patch merging, local windows, or shifted windows.

Recommended reading path:

```text
image -> patch partition -> stage 1 -> merge -> stage 2 -> merge -> stage 3 -> merge -> stage 4
```

The figure should show **spatial size shrinking while channel depth grows**. The
most compact visual encoding is a sequence of feature-map stacks:

- stage 1: widest/tallest map, shallow stack;
- stage 2: smaller map, deeper stack;
- stage 3: smaller again, deepest or longest block stack;
- stage 4: smallest map, compact high-level representation.

Make the stage containers equal-width if the paper emphasises a backbone family.
Make one stage or one block wider if that is the contribution. Do not draw every
block in every stage at full detail; use one repeated block plus `x 2`, `x 6`,
etc.

### 3. Shifted-window detail inset

Use an inset when the reader must understand W-MSA vs SW-MSA. Two adjacent mini
maps are usually enough:

```text
regular windows | shifted windows
```

Construction:

- same outer grid size for both maps;
- left map: aligned window outlines;
- right map: identical windows shifted by half a window and clipped to the map;
- one orange outline or arrow names the shift;
- optional dashed ghost grid shows the unshifted partition, but only if defined.

Do not place the shifted-window inset in the main data path unless it is itself
the contribution. Most figures read better with a small callout connected by a
dotted leader to the relevant stage.

### 4. Q/K/V or attention mechanism inset

Use when the novelty changes attention computation.

Recommended layout:

```text
tokens -> Q/K/V projection trio -> attention matrix -> weighted sum/context
```

Rules:

- Make Q, K, and V separate slim bars or chips, not three labels inside one box,
  if their roles differ.
- If the math is standard, draw one compact attention node and put the equation
  in the caption or paper text.
- If the novelty is locality/sparsity, the attention matrix heatmap is the hero.
  Encode sparsity by blank cells or a mask pattern, not by a low-contrast hue.
- Cross-attention should visibly have two sources: query tokens from one stream,
  key/value tokens from the other.

### 5. Encoder-decoder or FPN on a transformer backbone

Use when the method combines hierarchical features.

Recommended layout:

```text
backbone stages along the top -> lateral skips/fusion neck -> decoder/output row
```

Good CV-paper cues:

- encoder stages cool and neutral;
- decoder/fusion modules warm or green;
- skip connections thin and orthogonal;
- multi-scale outputs stacked vertically by resolution;
- labels use real stage names from the paper (`C2`, `C3`, `P4`, `M_i`) rather
  than generic "feature".

## TikZ snippets

These are fragments to copy into a standalone figure that already uses the main
template. Keep the outer element named and connect to its anchors. Dense cells
inside an image or heatmap are texture; the named frame is the geometry element.

### Patch grid inside a named image node

```latex
\newlength{\cell}\setlength{\cell}{0.17cm}
\node[box, text width=1.8cm, minimum height=1.35cm, inner sep=0pt] (img) {};
\begin{scope}[shift={(img.south west)}, x=\cell, y=\cell]
  \foreach \x in {0,...,9}{
    \foreach \y in {0,...,6}{
      \pgfmathtruncatemacro{\tint}{int(8 + 4*mod(\x+\y,3))}
      \path[fill=cvBlue!\tint, draw=white, line width=0.25pt]
        (\x,\y) rectangle ++(1,1);
    }
  }
\end{scope}
\node[note, below=0.12cm of img] (imglabel) {$H \times W \times 3$};
```

If the grid carries a real partition, name the partition or its enclosing window
as a node. If it is only image texture, do not connect arrows to individual cells.

### Token strip

```latex
\tikzset{
  token/.style={draw=cvOrange!75!black, fill=cvOrange!12,
    rounded corners=1pt, minimum width=0.24cm, minimum height=0.48cm,
    inner sep=0pt}
}
\node[token] (tok0) {};
\foreach \prev/\cur in {tok0/tok1,tok1/tok2,tok2/tok3,tok3/tok4,tok4/tok5}{
  \node[token, right=0.05cm of \prev] (\cur) {};
}
\node[note, below=0.12cm of tok2] (toklabel) {patch tokens};
```

For long sequences, draw 5-7 tokens plus an ellipsis node. Do not draw 196 tokens.

### Feature-map stack

```latex
\tikzset{
  fmap/.style={draw=cvBlue!70!black, fill=cvBlue!10,
    minimum width=1.0cm, minimum height=0.72cm, inner sep=0pt}
}
\node[fmap] (cbase) {};
\foreach \i in {1,...,3}{
  \pgfmathsetmacro{\dx}{0.07*\i}
  \pgfmathsetmacro{\dy}{0.05*\i}
  \node[fmap, xshift=\dx cm, yshift=\dy cm] (c\i) at (cbase.center) {};
}
\node[note, below=0.16cm of cbase] (clabel) {$\frac{H}{4} \times \frac{W}{4} \times C$};
```

Place the label under the base node or under a fitted container. The stack is a
depth cue; it should not become a pseudo-3D object with perspective.

### Swin shifted-window pair

```latex
\newlength{\wcell}\setlength{\wcell}{0.18cm}
\tikzset{
  winmap/.style={draw=cvGray!65, fill=white,
    minimum width=1.45cm, minimum height=1.45cm, inner sep=0pt}
}
\node[winmap] (wmsa) {};
\node[winmap, right=0.8cm of wmsa] (swmsa) {};
\foreach \map/\shiftx/\shifty in {wmsa/0/0,swmsa/1/1}{
  \begin{scope}[shift={(\map.south west)}, x=\wcell, y=\wcell]
    \clip (0,0) rectangle (8,8);
    \foreach \x/\y/\clr in {0/0/cvBlue,4/0/cvGreen,0/4/cvPurple,4/4/cvOrange}{
      \path[fill=\clr!12, draw=\clr!75!black, line width=0.45pt]
        ({\x+\shiftx},{\y+\shifty}) rectangle ++(4,4);
    }
    \draw[step=1, cvGray!25, line width=0.2pt] (0,0) grid (8,8);
  \end{scope}
}
\node[note, below=0.12cm of wmsa] {W-MSA};
\node[note, below=0.12cm of swmsa] {SW-MSA};
\draw[flow2] (wmsa.east) -- (swmsa.west);
```

The right map clips shifted windows at the boundary; that clipping is the point.
Use a caption phrase like "orange outlines mark shifted local windows" if the
shift is not obvious in grayscale.

### Repeated transformer block

```latex
\tikzset{
  tblock/.style={draw=cvGray!70, fill=cvGray!5, rounded corners=2pt,
    text width=1.55cm, minimum height=1.05cm, align=center,
    font=\sffamily\footnotesize, inner sep=0.12cm},
  micro/.style={draw=cvGray!55, fill=white, rounded corners=1pt,
    text width=1.15cm, minimum height=0.28cm, align=center,
    font=\sffamily\scriptsize, inner sep=0.04cm}
}
\node[tblock] (blk) {};
\node[micro] (msa) at ($(blk.center)+(0,0.20)$) {MSA};
\node[micro] (mlp) at ($(blk.center)+(0,-0.20)$) {MLP};
\node[note, above=0.08cm of blk] (blklabel) {Transformer block};
\node[note, right=0.12cm of blk] (repeat) {$\times L$};
```

If the internals are not the contribution, omit the micro-rows and keep only the
outer block. Detail is not proof.

## Caption patterns

Use the caption to define encodings instead of filling the canvas with a legend.

- "Blue feature maps are frozen; orange modules are trained."
- "Dashed arrows indicate supervision entering the loss, not inference-time data
  flow."
- "The inset compares regular and shifted local window partitions."
- "Stage widths are schematic; feature-map sizes are labelled under each stage."

## Common failure modes

- **Decorative patch grids.** If the method is not about patches/windows, a patch
  mosaic can falsely imply a ViT contribution.
- **Too many windows.** A full Swin backbone plus every local window partition
  becomes a carpet. Show a stage-level backbone plus one local inset.
- **3D feature maps that fight the labels.** Offset slabs are enough; perspective
  boxes reduce the usable label area and often fail geometry checks.
- **Colour doing all the work.** Window A vs B, frozen vs trainable, or old vs new
  must also differ by position, outline, label, or line style.
- **Backbone outshouting the novelty.** A standard transformer can be a grey slab.
  The new module should get the area, stroke weight, or inset.
- **Unexplained shifted/dashed encodings.** If a partition is shifted, dashed, or
  clipped, the caption says what that visual operation means.
