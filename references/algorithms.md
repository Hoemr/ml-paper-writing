# Reference blocks and LaTeX recipes for pseudocode

The rules are in [style-conventions.md](style-conventions.md#algorithms). This
file carries the material they are derived from.

## Two compact reference examples

MoCo (He et al. 2020), Algorithm 1, 20 lines:

```
# f_q, f_k: encoder networks for query and key
# queue: dictionary as a queue of K keys (CxK)
# m: momentum
# t: temperature

f_k.params = f_q.params                  # initialize
for x in loader:                         # load a minibatch x with N samples
    x_q = aug(x)                         # a randomly augmented version
    x_k = aug(x)                         # another randomly augmented version

    q = f_q.forward(x_q)                 # queries: NxC
    k = f_k.forward(x_k)                 # keys: NxC
    k = k.detach()                       # no gradient to keys

    # positive logits: Nx1
    l_pos = bmm(q.view(N,1,C), k.view(N,C,1))
    # negative logits: NxK
    l_neg = mm(q.view(N,C), queue.view(C,K))
    # logits: Nx(1+K)
    logits = cat([l_pos, l_neg], dim=1)

    # contrastive loss, Eqn.(1)
    labels = zeros(N)                    # positives are the 0-th
    loss = CrossEntropyLoss(logits/t, labels)

    # SGD update: query network
    loss.backward()
    update(f_q.params)

    # momentum update: key network
    f_k.params = m*f_k.params + (1-m)*f_q.params

    # update dictionary
    enqueue(queue, k)                    # enqueue the current minibatch
    dequeue(queue)                       # dequeue the earliest minibatch
```

SimSiam (Chen & He 2021), Algorithm 1, 12 lines plus a helper:

```
# f: backbone + projection mlp
# h: prediction mlp

for x in loader:                         # load a minibatch x with n samples
    x1, x2 = aug(x), aug(x)              # random augmentation
    z1, z2 = f(x1), f(x2)                # projections, n-by-d
    p1, p2 = h(z1), h(z2)                # predictions, n-by-d

    L = D(p1, z2)/2 + D(p2, z1)/2        # loss
    L.backward()                         # back-propagate
    update(f, h)                         # SGD update

def D(p, z):                             # negative cosine similarity
    z = z.detach()                       # stop gradient
    p = normalize(p, dim=1)              # l2-normalize
    z = normalize(z, dim=1)              # l2-normalize
    return -(p*z).sum(dim=1).mean()
```

What the two share: a comment header naming every symbol and hyperparameter not
introduced by the code itself, trailing comments that are noun phrases, one
operation per line, a named helper rather than an inlined one, and a caption
that is a title. What they are not: mathematical pseudocode. Transferring them
to a theory-adjacent paper means keeping the discipline and replacing `=` with
`\gets` and the code names with notation — the definition-in-a-step failure the
rules warn about is what that transfer invites.

A listing is optional. Choose a compact overview or an appendix recipe according
to what the reader needs; these examples do not establish a venue line limit.

## LaTeX

| Package | Step | Comment | Helper |
|---|---|---|---|
| `algorithmic` | `\STATE` | `\COMMENT{}`, renders as `{...}` | none |
| `algpseudocode` | `\State` | `\Comment{}` | `\Procedure`/`\EndProcedure` |
| `algorithm2e` | body lines end `\;` | `\tcp*{}` | `\SetKwFunction` |

None provides `\Continue` or `\Break`. Guard with `\IF`/`\ENDIF` or hoist the
guard into the loop condition.

`algorithmic`, which the ICLR kit ships:

```latex
\usepackage{algorithm}
\usepackage{algorithmic}
```

```latex
\begin{algorithm}[t]
\caption{...}
\label{alg:...}
\begin{algorithmic}[1]
\renewcommand{\algorithmiccomment}[1]{\hfill$\triangleright$ \textit{#1}}
\REQUIRE $\pi_\vtheta$; frozen scorer $\pi_{\mathrm{ref}}$; verifier $R$
\ENSURE  $A_t$ for every decision turn of one rollout
\STATE $\vy \sim \pi_\vtheta(\cdot \mid \vx)$ \COMMENT{one rollout per task}
\FOR{turn $t$ with a realized future}
    \STATE ...
    \IF{$h_t^{-} = \varnothing$}
        \STATE ...
    \ENDIF
\ENDFOR
\end{algorithmic}
\end{algorithm}
```

Gotchas, all verified against `algorithmic.sty`:

- `\algorithmiccomment` is document-wide once redefined. Scope it inside the
  `algorithmic` environment or every later block inherits it.
- `\REQUIRE` and `\ENSURE` are `\item[...]` labels and take no line number, so
  they never shift the numbers the text cites.
- `\ENDFOR`/`\ENDIF` call `\ALC@it` and **do** take a line number unless the
  package is loaded with the `noend` option. Count them against the budget.
- `\COMMENT` ends the line in some versions. Put it last.
- `\varnothing` needs `amssymb`.
- Compile after editing; an unbalanced `\FOR`/`\ENDFOR` fails late and obscurely.

## Audit

`scripts/audit_pseudocode.py` reports the checkable half: numbered-line target,
over-long steps, period-terminated steps, `\emph` inside a step, and whether the
math macros in the block appear in the notation file.

```bash
python3 scripts/audit_pseudocode.py paper.tex --notation paper.tex
```

It masks each math span as a single word before counting, so a displayed formula
does not inflate a step's word count, and it matches `\REQUIRE`/`\ENSURE` as
un-numbered. Exceeding the line target produces a compaction warning, not a
correctness failure. Zero failures means the hard mechanical checks pass; review
warnings in context and trace the block by hand to assess its scientific content.

## A worked compaction

Before — 12 numbered lines, 8 over budget:

```latex
\REQUIRE student $\pi_\vtheta$, frozen snapshot $\pi_{\mathrm{ref}}$ of the initial policy,
         verifier $R(\cdot)$; a one-transition future gap
\STATE Sample \emph{one} response $\vy\sim\pi_\vtheta(\cdot\mid\vx)$ per task; verify it
       to obtain $R$; set $\tilde R\gets 2R-1$
\STATE Emit one training row per decision turn $t=1,\dots,T$, carrying $\tilde R$ onto
       every row of the trajectory
\FOR{each row whose turn $t$ has at least one transition remaining after it}
    \STATE True view $h^{+}_t$: the state $s_t$, the outcome $R$, and this trajectory's
           own realized future, beginning at the next transition
    \STATE Matched view $h^{-}_t$: pick a future from another trajectory in the batch,
           preferring the same terminal outcome, then the same task family, then the
           closest remaining horizon
    \STATE If no match exists, set $\bar\kappa_t\gets 0$ and skip the row
    \STATE Re-score the same span $a_t$ under $\pi_{\mathrm{ref}}$ in both views and take
           $\bar\kappa_t$ as the mean log-ratio over its tokens
    \STATE $c_t \gets \tilde R\,\bar\kappa_t$
\ENDFOR
\STATE Center and scale $\{c_t\}$ within the trajectory using token-count weights
       $\omega_t$, giving $\widehat c_t$; set $\widehat c_t\gets 0$ when fewer than two
       turns were scored
\STATE $A_t \gets \tilde R + \widehat c_t$ for every turn of the trajectory
\STATE Update $\pi_\vtheta$ on generated tokens with the clipped surrogate; prompts,
       observations, and the privileged future block are masked out
```

After — 15 numbered lines, none over budget:

```latex
\REQUIRE $\pi_\vtheta$; frozen scorer $\pi_{\mathrm{ref}}$; verifier $R$; future gap $=1$
\ENSURE  $A_t$ for every decision turn of one rollout
\STATE $\vy \sim \pi_\vtheta(\cdot \mid \vx)$ \COMMENT{one rollout per task}
\STATE $R \gets \mathrm{Verify}(\vx,\vy)$; $\tilde R \gets 2R-1$ \COMMENT{reward anchor}
\FOR{turn $t$ with a realized future}
    \STATE $h_t^{+} \gets$ future of $\vy$ after $t$ \COMMENT{true view}
    \STATE $h_t^{-} \gets \mathrm{Match}(h_t^{+})$ \COMMENT{matched view; same outcome, then task family, then horizon}
    \IF{$h_t^{-} = \varnothing$}
        \STATE $\bar\kappa_t \gets 0$ \COMMENT{no counterfactual, no credit}
    \ELSE
        \STATE $\bar\kappa_t \gets \frac{1}{|a_t|}\sum_{k} \log \frac{\pi_{\mathrm{ref}}(a_{tk} \mid s_t, h_t^{+})}{\pi_{\mathrm{ref}}(a_{tk} \mid s_t, h_t^{-})}$ \COMMENT{\cref{eq:delta}}
        \STATE $c_t \gets \tilde R\,\bar\kappa_t$
    \ENDIF
\ENDFOR
\STATE $\widehat c_t \gets \mathrm{CenterScale}_\omega(\{c_t\})$ \COMMENT{\cref{eq:normalize}; $\gets 0$ if fewer than two turns scored}
\STATE $A_t \gets \tilde R + \widehat c_t$ \COMMENT{attached to every generated token of turn $t$}
\STATE Update $\vtheta$ with the clipped surrogate \cref{eq:objective} \COMMENT{mask prompt, observations, future block}
```

What changed: the two view definitions left the steps; three operations on one
line became three steps; the skip became `\IF`/`\ELSE`; `\emph{one}` went; the
matching order survived as a trailing comment; the row layout dropped out
entirely because the setup appendix already states it, so nothing was lost.
