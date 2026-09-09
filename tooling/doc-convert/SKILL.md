---
name: doc-convert
description: >
  Convert and ingest documents with local tools — no cloud.
  PRODUCE: Markdown → styled PDF in house style, with mermaid diagrams
  rendered, via the `md2pdf` command; Markdown → Word/.docx (and pptx/html/epub)
  via pandoc.
  INGEST: read a .pdf/.docx/.xlsx the Read tool can't handle by converting it
  to Markdown/text first (pandoc, PyMuPDF, python-docx, openpyxl).
  Trigger whenever the user says: "make a PDF", "convert to PDF", "PDF version",
  "export to Word/docx", "convert this doc", "read this PDF/Word/Excel file",
  "extract text from", or hands over a .pdf/.docx/.xlsx to work with.
---

> **`$SETUP_DIR`** = the larry-setup repo on this machine. Resolve once, first that exists: `$SETUP_DIR` · `~/larry-setup` · `/mnt/rojaws/localDev/setup` (same chain `alw` uses).

# doc-convert

Local document conversion and ingestion. Nothing here needs the network.

`md2pdf` is the tracked script at `$SETUP_DIR/tooling/md2pdf` — one canonical copy shared
by every machine. Linux clients symlink it into `~/.local/bin`; Windows cannot symlink a
python script, so it goes through two shims there (`md2pdf.cmd` for PowerShell, `md2pdf`
for Git Bash). **Edit the repo file, never a shim or an installed copy** — copies are how
this tool drifted into three conflicting variants once already.

Shell examples below are POSIX. On the Windows workstation run them from Git Bash, or use
the PowerShell equivalent; the commands themselves are the same.

## The PDF engine picks itself

| Engine | Chosen when | Diagrams |
|---|---|---|
| WeasyPrint | it imports — Linux clients | **PNG** (it cannot render the `<foreignObject>` mermaid-cli emits) |
| headless Edge | it does not — the Windows workstation has no GTK3 runtime | **SVG** |

Both render the footer and `Page N of M`. Override only when asked:
`MD2PDF_ENGINE=weasyprint|edge`, `MD2PDF_MERMAID=png|svg`.

**Mermaid:** ` ```mermaid ` fences are pre-rendered into real diagrams via `mmdc`
(mermaid-cli), in the house purple palette. Without `mmdc` on PATH they print as source
with a warning on stderr — deliberate, and never a hard failure.

## Installed tools

| Tool | Purpose |
|---|---|
| `md2pdf` → `$SETUP_DIR/tooling/md2pdf` | Markdown → styled A4 PDF, mermaid diagrams rendered |
| `mmdc` (`@mermaid-js/mermaid-cli`, npm global) | renders the fences md2pdf finds |
| `pandoc` | universal convert: md↔docx↔html↔epub↔pptx |
| python `markdown` | Markdown → HTML (md2pdf uses it) |
| python `pymupdf` (`import fitz`) | fast PDF text/image extraction |
| python `pdfplumber` | PDF tables / precise layout extraction |
| python `python-docx` (`import docx`) | read/write .docx |
| python `openpyxl` | read/write .xlsx |

The Read tool already renders **PDFs** natively — prefer it for reading one. Use the
extract commands below only when you need raw text for further processing, or when Read
cannot open the file.

## PRODUCE

### Markdown → PDF (house style, no flags needed)
```sh
md2pdf INPUT.md                           # -> INPUT.pdf, footer = first H1
md2pdf INPUT.md OUTPUT.pdf                # explicit output
md2pdf INPUT.md OUTPUT.pdf "Footer text"  # override footer
```
A4, house purple headings (`#611A67`), gold blockquote rules, banded tables, boxed code,
page numbers, mermaid fences as diagrams. **Never pass a flag or edit CSS to make it
blue** — purple is the house style and it is already the default. No syntax highlighting;
code still renders clean.

To restyle, edit `CSS_TEMPLATE` (prose) or `MERMAID_CFG` (diagrams) in
`$SETUP_DIR/tooling/md2pdf`, then commit — it is tracked.

### Markdown → Word / other formats (pandoc)
```sh
pandoc INPUT.md -o OUTPUT.docx                             # Word
pandoc INPUT.md -o OUTPUT.docx --reference-doc=tmpl.docx   # with house template
pandoc INPUT.md -o OUTPUT.pptx                             # slides
pandoc INPUT.md -o OUTPUT.html --standalone                # standalone HTML
```
Use pandoc for **.docx** (editable Word). Use `md2pdf` for **PDF** — better CSS control
than pandoc's PDF engines, and no LaTeX.

## INGEST (make an unreadable file readable)

```sh
pandoc INPUT.docx -t gfm -o INPUT.md      # .docx -> Markdown, then Read the .md

# .pdf -> text  (tables: pdfplumber page.extract_tables())
python3 -c "import fitz,sys; print(chr(10).join(p.get_text() for p in fitz.open(sys.argv[1])))" INPUT.pdf

# .xlsx -> text
python3 -c "import openpyxl,sys; wb=openpyxl.load_workbook(sys.argv[1],data_only=True); [print('#',ws.title) or [print('\t'.join('' if c is None else str(c) for c in r)) for r in ws.iter_rows(values_only=True)] for ws in wb]" INPUT.xlsx
```

## Check the output, do not trust the message

The `wrote …` line has lied before: a race in the Edge branch once replaced a verified-good
PDF with an error page while still reporting success. That is why the Edge writer renders
to a private temp file and verifies twice before moving it into place. For anything that
matters:

```sh
python3 -c "import pymupdf,sys; d=pymupdf.open(sys.argv[1]); print(d.page_count,'pages'); print(d[0].get_text()[:200])" OUTPUT.pdf
```

**`import pymupdf`, not `import fitz`.** The bare `fitz` spelling still works but warns that
it will be removed. Counting images to confirm diagrams rendered needs one more care:
WeasyPrint rasterises a `✅` or `❌` in the source into its own shared PNG, so filter above
about 5 kB — real mermaid diagrams are 120-270 kB.

If a diagram appears as source text, `mmdc` is not on PATH — the stderr warning names the
fix. If md2pdf reports "no PDF engine", neither WeasyPrint nor Edge was found.

## Verify tools are present
```sh
command -v md2pdf pandoc mmdc
python3 -c "import pymupdf, pdfplumber, docx, openpyxl, markdown; print('py deps ok')"
```

## Install / repair
```sh
python3 -m pip install --user --break-system-packages \
  markdown pymupdf pdfplumber python-docx openpyxl pypandoc-binary
# Linux also: weasyprint          Windows: skip it, WeasyPrint will not import there
npm i -g @mermaid-js/mermaid-cli  # mmdc, for diagrams
ln -sf "$(python3 -c 'import pypandoc;print(pypandoc.get_pandoc_path())')" ~/.local/bin/pandoc
```

**`--break-system-packages` is required, not optional**, on any externally-managed Python
(Debian 13 ships 3.13 that way). Without it pip refuses with PEP 668 and installs nothing.

**pandoc comes from the `pypandoc-binary` wheel**, symlinked as above. The distro package
needs root, and `sudo apt` prompts for a password on deb — the wheel keeps the whole
toolchain in user space.
`md2pdf` needs `~/.local/bin` on PATH. On Windows it also needs Edge at
`C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe` or
`C:\Program Files\...` — the script checks both, then falls back to PATH.

If the installed `md2pdf` is missing or stale, re-run
`$SETUP_DIR/tower/handoff-scripts/relink-tooling.sh` rather than copying the file.
