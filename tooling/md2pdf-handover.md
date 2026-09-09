# md2pdf — one script, two engines, mermaid rendered

> **Read this if** you are about to edit `md2pdf`, re-link it on a machine, or are
> wondering why a `mermaid` fence printed as a block of source text.

**Status:** 🟢 Done and verified on both engines, 2026-08-27. [`tooling/md2pdf`](md2pdf)
is now the single canonical copy. The three-way split described in the earlier version
of this document is closed.

---

## What it does

Markdown → A4 PDF in house style: purple `#611A67` headings, gold blockquote rules,
banded tables, boxed code, footer from the first H1, `Page N of M`.

```sh
md2pdf INPUT.md                           # -> INPUT.pdf, footer = first H1
md2pdf INPUT.md OUTPUT.pdf                # explicit output
md2pdf INPUT.md OUTPUT.pdf "Footer text"  # override footer
```

` ```mermaid ` fences are pre-rendered into real diagrams, in the same palette as the
prose around them.

## Two engines, picked automatically

| | WeasyPrint | headless Edge |
|---|---|---|
| Chosen when | it imports — Linux clients | it does not — the Windows workstation has no GTK3 runtime |
| Diagram format | **PNG** at `mmdc -s 3` | **SVG**, inlined as a data URI |
| Footer + page numbers | ✅ | ✅ (verified 2026-08-27; older Chromium ignored `@page` margin boxes) |

WeasyPrint wins when both are available. Override with `MD2PDF_ENGINE=weasyprint|edge`,
and the diagram format independently with `MD2PDF_MERMAID=png|svg`.

**Why PNG under WeasyPrint.** mermaid-cli emits `<foreignObject>` for flowchart node
labels (its default `htmlLabels: true`). WeasyPrint does not support `foreignObject` —
labels vanish or the image drops, quietly enough that you would ship a broken PDF. If a
diagram ever *needs* to be vector there, `htmlLabels: false` forces native SVG `<text>`,
at the cost of worse label wrapping.

## How the mermaid pre-render works

The fence is pre-rendered **before** python-markdown runs, so it never reaches the
`fenced_code` extension. Neither engine runs the mermaid JavaScript renderer, which is
why an untouched fence lands in the PDF as a `<pre>` full of source.

1. Regex-match every fence (`re.DOTALL | re.MULTILINE`, tolerating leading whitespace).
2. Write each body to `diagram-N.mmd` in a scratch dir.
3. `mmdc -i … -o … -c mermaid-config.json -b transparent -q` (plus `-s 3` for PNG).
4. Substitute an `<img>` data URI inside `<p class="mermaid-figure">`.
5. Hand the rewritten text to `markdown.markdown()`.

`MERMAID_CFG` maps the house palette onto mermaid's theme variables, so diagrams arrive
purple-and-gold rather than mermaid's default blue.

**Data URIs, not file references**, for two reasons: no temp file has to survive until
the engine reads the HTML, and every diagram keeps its own style scope — mermaid-cli
stamps a fixed `id="my-svg"` on every SVG it writes, so inlining two into one document
would collide their `<style>` rules.

### Fail-soft is a requirement, not a nicety

Three guards. Keep all of them through any refactor:

- **`mmdc` not on PATH** — one warning to stderr naming the fix, text returned unchanged.
- **A diagram fails** (`CalledProcessError` / `TimeoutExpired`, 180 s cap) — warn with the
  last ~300 bytes of `mmdc` stderr and leave *that fence* as source. One bad diagram must
  not kill the document.
- **`mmdc` exits 0 but writes nothing** — treated as a failure, fence left alone.

## Sharp edges

**Figure sizing must be clamped in ratio, in the inline style.** A CSS `max-height` alone
clamps the height while leaving an explicit inline `width` untouched, which stretches a
tall diagram sideways. Observed on the `WORKFLOWS-OVERVIEW.md` sequence diagram: a 0.716
aspect source placed at 169.8×200 mm (0.849). `_figure_style()` applies
`MAX_FIGURE_H_MM` to the width as well; it must stay in step with the
`p.mermaid-figure img { max-height }` rule. Verified: all five diagrams now place within
0.001 of their source ratio.

**Edge's print-to-pdf launcher can return before the render finishes.** Exit 0, no
stderr, and the real work lands in a detached process moments later — especially with
another Edge window already open. A stale attempt can therefore finish late and silently
overwrite a file already verified good. So `write_pdf_edge()` never targets the output
path: it renders into a private randomly-named temp PDF, confirms it twice with a 1.5 s
pause (stable size, ≥1 page, no `ERR_FILE_NOT_FOUND` in the first page via PyMuPDF),
retries up to 8 times, then moves it into place. A late zombie write lands on the
abandoned temp name. None of this applies to WeasyPrint, whose `write_pdf()` is
synchronous and in-process — do not generalise the guard to it.

**Probing for WeasyPrint is noisy.** An install missing its GTK3 natives prints a
multi-line troubleshooting banner during the failed import. `have_weasyprint()` swallows
both streams for the probe — useful output when the user *asked* for WeasyPrint, noise
when we are only checking.

**The intermediate HTML goes next to the source file**, not in the system temp dir, so
relative image paths in the markdown resolve. WeasyPrint gets the same effect via
`base_url`.

## Installing on a machine

Linux clients symlink it like every other `tooling/` CLI:

```sh
ln -sf ~/larry-setup/tooling/md2pdf ~/.local/bin/md2pdf
```

Windows cannot — it needs a Python launcher, so it uses two shims that call the repo copy
directly (`~/.local/bin/md2pdf.cmd` for PowerShell, an sh `md2pdf` for Git Bash).
`tower/handoff-scripts/relink-tooling.sh` writes both, deriving the native path with
`cygpath -m` because Windows python cannot open the `/c/...` form the rest of the script
uses. A pre-existing `md2pdf.py` is moved to `~/.local/bin/_md2pdf-backup/` rather than
deleted.

The generated `.cmd` is LF-only. That is deliberate and verified: a two-line batch with no
labels or `goto` runs fine that way, and it avoids a `\r` escape that every quoting layer
between the script and the file proved willing to swallow.

Dependencies: python `markdown`, plus `weasyprint` **or** Edge. Diagrams additionally
need `npm i -g @mermaid-js/mermaid-cli`.

## Verifying a change

`WORKFLOWS-OVERVIEW.md` is the right test file: a flowchart with `subgraph`, a second
carrying `style` directives, and a `sequenceDiagram` with `loop`/`alt` — the three shapes
most likely to expose a `foreignObject` or sizing problem.

```sh
md2pdf ~/larry-setup/WORKFLOWS-OVERVIEW.md /tmp/wf.pdf
# expect:  md2pdf: rendered 5 mermaid diagram(s) as png
#          wrote /tmp/wf.pdf [weasyprint]
```

Then check, do not assume:

```sh
# no mermaid source survived, and the footer rendered
python3 -c "import fitz,sys; d=fitz.open(sys.argv[1]); t=''.join(p.get_text() for p in d); print('leak' if 'flowchart LR' in t or 'sequenceDiagram' in t else 'clean', '| footer', 'Page 1 of' in t)" /tmp/wf.pdf

# every diagram placed at its source aspect ratio
python3 -c "
import fitz,sys
d=fitz.open(sys.argv[1]); seen={}
for p in d:
    for im in p.get_images(full=True): seen.setdefault(im[0],(im[2],im[3]))
for p in d:
    for x,(w,h) in seen.items():
        for r in p.get_image_rects(x):
            print(x, 'OK' if abs(w/h - r.width/r.height) < 0.02 else 'DISTORTED')
" /tmp/wf.pdf
```

Fail-soft, the guard most easily broken by a refactor:

```sh
PATH=/usr/bin:/bin md2pdf ~/larry-setup/WORKFLOWS-OVERVIEW.md /tmp/nomm.pdf
# expect: warning about mmdc on stderr, exit 0, fences printed as source
```

Both engines were exercised this way on 2026-08-27: Edge → 7 pages, 5 SVG diagrams,
clean, footer present; WeasyPrint → 9 pages, 5 PNG diagrams, clean, footer present, all
ratios within 0.001; fail-soft → exit 0 with fences as source.

## Left open

- ~~`tower/wsl-setup.md` and `tower/windows-host-setup.md` list no PDF tooling.~~ **Closed
  2026-08-28, across all five client docs** — the original note named two and the gap was in
  every one. Each now carries a "Doc tooling" section with the dependency install, the `mmdc`
  line, and the engine that platform uses: WeasyPrint on `wsl-setup` and `coop-setup` (both
  Linux), Edge on `windows-setup` and `windows-host-setup`, and a row in `coop-update`'s
  catch-up table.
- ~~The `doc-convert` skill remains untracked.~~ **Closed by `463290e`** — it is tracked at
  `tooling/doc-convert/SKILL.md` and `relink-tooling.sh` links it into
  `~/.claude/skills/doc-convert/`.
