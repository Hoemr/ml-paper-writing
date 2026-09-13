# Method Figures: Show the Mechanism

Use this guide when creating or revising a paper's core method, architecture, or workflow figure. For empirical charts, use the figure guidance in [writing-guide.md](writing-guide.md). A method figure explains an operation; a results chart reports measurements. Do not make one look like the other without labeling the distinction.

## Choose what the reader should see

Write one sentence describing the relationship the figure must make visible. Examples include an asymmetric computation, a shared representation, a changed training signal, or the separation between training and inference. Make that relationship the visual center. A sequence of boxes containing section summaries rarely communicates it.

Extract four things from the actual method before drawing:

- **Objects:** data, representations, parameters, predictions, or labels.
- **Operations:** selection, transformation, scoring, sampling, updating, or aggregation.
- **Invariants:** what remains fixed across the comparison or intervention.
- **Scope:** which paths run at training or inference, and which are only proposed.

Keep a genuinely simple method simple. Added modules, feedback loops, or decorative neural-network icons cannot supply scientific depth that the method does not have.

## Choose a layout that explains the relationship

| Relationship to explain | Useful visual structure | Common failure |
|---|---|---|
| Shared coordinates for two populations | Aligned rows or columns with repeated coordinate labels | Two unrelated boxes both labeled “representation” |
| Changed operation under fixed inputs | A common input/target with the changed route emphasized | Duplicated full pipelines that hide the controlled difference |
| Asymmetric computation | Different object populations entering the relevant operations | Equal-sized boxes that conceal what is omitted or retained |
| Conditional or sampled alternatives | An explicit decision/sampling point with labeled routes | A fork that appears to execute all branches simultaneously |
| Training-only information | A visible entry point and a separately identified inference path/output | A criterion or teacher drawn as a permanent model component |
| Implemented primitive with a future extension | A primary path and a labeled, subordinate proposed path | A solid loop that implies recursive gains have been demonstrated |

These are options, not a required three-panel template. Use panels when they separate meaningful stages or comparisons. Prefer one dominant reading direction; route feedback around the perimeter instead of through labels.

## Replace prose boxes with visual objects

Represent the method's objects directly when this reduces explanation: aligned tokens, paired records, a queue, a shared coordinate grid, or a retained/discarded subset. Use short nouns for objects and verbs for operations. Keep boxes for actual operations, containers, or decisions, rather than enclosing every label.

Move definitions and secondary explanation into the caption or surrounding text. Keep the information needed to follow the mechanism in the figure itself. Expand an essential symbol locally or use the manuscript's established notation; do not replace all words with unexplained equations.

A schematic grid need not contain invented values. Use neutral cells and a clearly labeled illustrative selection when only coordinate structure matters. Do not fabricate a heatmap, histogram, ranked profile, or numerical weight vector for visual richness. If the plot is quantitative, use traceable measurements and the appropriate scale.

## Give arrows an unambiguous meaning

Identify whether each connection carries data, gradients, parameter updates, or a proposed dependency. Use a local label or a small legend when multiple meanings coexist. Do not assume dashed arrows universally mean “future work”: other papers use them for gradients, stop-gradient, or optional paths.

For stochastic routing, label the sampling decision and branch probabilities, then show how the selected route reaches the shared operation. Do not accidentally imply simultaneous forward passes, duplicated losses, or numerical addition when the implementation concatenates a context. If a compact notation is ambiguous, define it in the caption.

Check feedback arrows against the evidence. An implemented loop is not evidence of improved performance over multiple rounds. A proposed loop should be marked as proposed, even if it is visually natural.

## Build visual hierarchy before choosing colors

Use position, grouping, alignment, whitespace, and line weight to establish hierarchy. The main mechanism should remain identifiable in a grayscale rendering. Background panels and guide lines should be weaker than the objects and paths they organize.

Avoid giving every stage a different equally prominent color. Reserve emphasis for the selected object, intervention, or difference the reader should notice. Use the same color for the same semantic role throughout the figure; do not reuse it for unrelated meanings merely to balance the page.

### Optional restrained dark palette

When the author wants a deeper, restrained appearance, this palette is a starting point, not a universal publication requirement:

| Role | Example color | Hex |
|---|---|---|
| Main text | Charcoal | `#202124` |
| First population or representation | Ink blue | `#233D4D` |
| Second population or representation | Slate olive | `#535D50` |
| Selected object or intervention | Deep wine | `#632E3B` |
| Secondary paths | Neutral gray | `#737373` |
| Broad surfaces | White / light neutral | `#FFFFFF` / `#F7F7F7` |

Use the dark colors for text, strokes, and a few focal objects. Keep broad surfaces neutral. A dark accent block with white text can identify a key operation more clearly than several pastel panels. Avoid making every object dark or filling the entire background.

The named palette is not an accessibility certification. Pair colors with labels, position, outlines, or shapes. Inspect grayscale and relevant color-vision simulations when color carries distinctions; verify contrast for the actual foreground/background combinations. Author preferences and venue requirements take precedence over these example colors.

In TikZ, define colors once and refer to semantic names such as `populationA`, `populationB`, and `intervention`. This makes later palette changes local and preserves semantic consistency.

## Keep the figure editable and inspect the delivered size

For a technical diagram, prefer a vector source supported by the repository: TikZ, SVG, or another editable vector format. Retain the source and a reproducible export route. Raster generation is useful for illustrative assets, but is a poor default for diagrams requiring exact text, arrows, or mathematical notation.

Match the figure to its final column or page width before tuning labels. Shrinking a large canvas into the paper can make an otherwise readable drawing unusable. Prefer removing redundant wording or restructuring the layout to shrinking fonts.

Inspect both the standalone figure and the compiled manuscript page:

- Can a new reader identify the distinctive operation without reading every label?
- Do object alignment and arrows agree with the implementation?
- Are alternative paths distinguishable from simultaneous computation?
- Are labels, arrowheads, subscripts, and pale boundaries legible at final size?
- Do outlines or connectors cross text? Does a highlight obscure a label?
- Does grayscale preserve the distinction between the main operation and context?
- Are schematic marks clearly distinguished from measured results?
- Does the caption explain how to read the figure without restating every label?

Check the compiler log for missing assets, overflow, and undefined symbols, but do not treat a successful compile as a visual review. After a local correction, re-render the affected figure and page. Inspect other pages if the change moved floats or altered pagination. Preserve venue typography rather than editing the style file to force a fit.

## Public design references

These references inform visual choices; they are not mandatory conference rules or scientific citations to add automatically to the manuscript.

- Rougier, Droettboom, and Bourne, [Ten Simple Rules for Better Figures](https://doi.org/10.1371/journal.pcbi.1003833), PLOS Computational Biology, 2014. In particular: identify the message, adapt to the medium, explain with a caption, use color purposefully, avoid misleading encodings, and remove chartjunk.
- He et al., [Masked Autoencoders Are Scalable Vision Learners](https://openaccess.thecvf.com/content/CVPR2022/papers/He_Masked_Autoencoders_Are_Scalable_Vision_Learners_CVPR_2022_paper.pdf), CVPR 2022, Figure 1. The arrangement of visible and masked patches makes encoder/decoder asymmetry visible, with short operation labels.
- He et al., [Momentum Contrast for Unsupervised Visual Representation Learning](https://openaccess.thecvf.com/content_CVPR_2020/papers/He_Momentum_Contrast_for_Unsupervised_Visual_Representation_Learning_CVPR_2020_paper.pdf), CVPR 2020, Figure 2. Aligned objects and distinct update paths make mechanism differences comparable.

Borrow the explanatory structure, not a paper's artwork, private experimental values, or unsupported claims. CVPR exemplars illustrate successful design choices; there is no single “CCF-A diagram style” that replaces the method's scientific content.
