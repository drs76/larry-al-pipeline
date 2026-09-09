# Handover — verify deb after a week of pipeline work

> **You are Claude running on `deb`** — the main Larry client and dev box (Debian 13, user
> `dav`). The repo is at **`/mnt/rojaws/localDev/setup`**; there is no `~/larry-setup` here.
> Your job is to **verify**, then fix what is clearly broken on this box. Report what you
> actually observed — a check you could not run is a reported gap, never an assumed pass.

**Why now.** A week of pipeline work landed on `main`: bench/routing-economics drivers, an
`anon` fail-closed fix, an `AL_TEST_BACKEND` referee change, a rebuild of `md2pdf`, and a
sweep that removed hardcoded repo paths from the CLIs and every prompt. **None of it has
run on deb.** The work was done on the Windows work box and — wrongly — verified against
its WSL2 Debian client, which is retired. deb is the main client and was never touched.

**Two things are known to need doing here.** Not hypothetical; observed over SSH on
2026-08-28:

1. **`mmdc` is not installed** (`command -v mmdc` returns nothing). `md2pdf` will print
   mermaid fences as source text instead of rendering diagrams. That is the exact fault
   this week's work set out to fix, so deb does not currently have the fix.
2. **The installed tooling has never been audited here.** deb has 12 Claude commands, 12 pi
   prompts, 1 skill and 27 entries in `~/.local/bin`, but whether those are symlinks into
   the repo or stale copies is unknown. The same audit on the Windows box found 14 broken
   links and mid-July copies.

---

## 0. Get current first

```sh
cd /mnt/rojaws/localDev/setup
git status --short          # expect clean; stop and ask if not
git pull --ff-only
git log --oneline -1        # expect e8b730d or later
```

If the tree is dirty, **stop** — deb is the dev box and may hold work in progress that is
not mine to resolve. Report what is uncommitted and wait.

## 1. What this box can verify

```sh
curl -sk -m 6 -o /dev/null -w 'larry (https 11443): %{http_code}\n' https://larry.home.arpa:11443/api/tags
command -v pi claude al python3 mmdc git
mountpoint -q /mnt/rojaws && echo "rojaws: mounted" || echo "rojaws: NOT mounted"
```

**Use port 11443, not 11434.** `http://larry:11434` returns `000` from every client even
though Larry listens on `*:11434` — it is blocked in transit, not down. Everything goes
through the nginx TLS proxy on 11443, which is what `~/.pi/ollama-provider.ts` points at.
Concluding "Larry is down" from port 11434 is a mistake this document made once already.

From the Windows box on 2026-08-28 Larry answered 200 with 19 models, including all three
pipeline defaults (`qwen3-coder:30b`, `al-coder-qwen3`, `mxbai-embed-large`). deb is on the
same LAN, so expect the same — but confirm rather than assume.

Unlike the retired WSL client, **deb has `/mnt/rojaws` mounted**, so nothing here is
blocked on it.

## 2. Install integrity

**Observed 2026-08-28: deb was already clean** — zero broken links, zero copies in both
prompt directories, and the two pi extensions already symlinked. The drift this section
predicted was a Windows-box finding, extrapolated. Run the audit anyway, but do not treat a
clean result as suspicious.

Everything in a managed slot should be a symlink into `/mnt/rojaws/localDev/setup`.

```sh
find ~/.pi/agent/prompts ~/.claude/commands ~/.local/bin ~/.pi/agent/extensions \
     -maxdepth 1 -xtype l -printf '  BROKEN %p -> %l\n'
find ~/.claude/skills -maxdepth 2 -xtype l -printf '  BROKEN %p -> %l\n'

for d in ~/.pi/agent/prompts ~/.claude/commands; do
  n=0; for f in "$d"/*; do [ -L "$f" ] || n=$((n+1)); done
  printf '%-28s copies: %s\n' "$d" "$n"
done
```

A plain copy is not cosmetic: it has stopped tracking the repo and drifts silently. That is
how the Windows box ended up running mid-July tooling and three conflicting `md2pdf`
variants.

**The fix is the relink script — never hand-copy a file:**

```sh
bash /mnt/rojaws/localDev/setup/tower/handoff-scripts/relink-tooling.sh
```

It resolves `SETUP_DIR` itself (here that lands on `/mnt/rojaws/localDev/setup`, since
there is no `~/larry-setup`), and **moves** any copy it replaces into
`~/.local/share/larry-relink-backup/<date>/` rather than overwriting it. Check that
directory afterwards if something you relied on stops behaving.

Re-run the two `find` commands after it. **Pass = no BROKEN lines, `copies: 0` both.**

Afterwards these should all be symlinks, on **both** pi and Claude: `bc-analysis`,
`bc-agent`, `bc-webservice-audit`, `doc-convert`, plus the `doc-convert`, `ste-writing`
and `bc-webservice-audit` skill directories.

## 3. Path resolution

```sh
cd /mnt/rojaws/localDev/setup
eval "$(grep -m1 '^SETUP_DIR=' tooling/alw)"; echo "SETUP_DIR=$SETUP_DIR"
ls "$SETUP_DIR/pipeline/board.py"
grep -rn 'C:/Users\|/c/Users' tooling/*.md | grep -v 'SETUP_DIR.*= the larry-setup repo'
```

**Pass =** `SETUP_DIR=/mnt/rojaws/localDev/setup`, `board.py` listed, `grep` silent. A
Windows path surviving in a prompt is a real regression — removing those was the point.

Worth confirming while you are here: the fallback chain assumes this box keeps the clone at
`/mnt/rojaws/localDev/setup`. If deb actually calls it something else, say so — every CLI
and prompt depends on that string.

## 4. Egress policy — the one that must not regress

Default posture is **deny**. `fix(anon): fail closed when git discovers an ancestor
repository` landed this week and has not run here.

```sh
cd /mnt/rojaws/localDev/setup && anon policy    # expect: local-only
cd /tmp && anon policy                          # expect: local-only

cd /mnt/rojaws/localDev/setup/pipeline
python3 test_secret_gate.py
python3 test_egress_midtier.py
python3 test_anon_map.py
python3 test_anon_workspace.py
```

**Any failure here is the highest-severity finding in this document.** Report it first and
do not continue to the later sections.

## 5. Pipeline unit tests

```sh
cd /mnt/rojaws/localDev/setup/pipeline
for t in test_*.py; do
  printf '%-28s ' "$t"
  python3 "$t" >/tmp/$t.log 2>&1 && echo PASS || { echo FAIL; tail -5 /tmp/$t.log; }
done
```

There were 11 test files as of `e8b730d`. **All 11 run under plain `python3` and pytest is
not needed for any of them.** `test_objref.py` looks like a pytest file and is not one: it
declares no `def test_` functions at all, runs 15 assertions at module level, and ends
`sys.exit(1 if fails else 0)`. Verified on deb 2026-08-28 — 11/11 PASS with no pytest
installed.

Unlike the retired WSL box, deb **has** `/mnt/rojaws`, so bench fixtures under it should
resolve. A missing-fixture failure here is more likely a real gap than an environment one.

## 6. md2pdf — expect this to fail first, then fix it

Rebuilt this week into one script that picks its engine at runtime. On deb that should be
**WeasyPrint** with **PNG** diagrams.

```sh
md2pdf /mnt/rojaws/localDev/setup/WORKFLOWS-OVERVIEW.md /tmp/wf.pdf
```

**`mmdc` was missing on 2026-08-28 and has since been installed** (`mmdc 11.16.0`, via
`~/.npm-global`). Before that it printed the warning and the fences as source — md2pdf
failing soft, correctly, not a crash. If a future box lacks it:

```sh
npm i -g @mermaid-js/mermaid-cli
md2pdf /mnt/rojaws/localDev/setup/WORKFLOWS-OVERVIEW.md /tmp/wf.pdf
```

Expect `md2pdf: rendered 5 mermaid diagram(s) as png` then `wrote /tmp/wf.pdf [weasyprint]`.

Then check the output rather than trusting the message — the "wrote ..." line has reported
success over a broken file before.

This check uses **`pypdf`**, not PyMuPDF. PyMuPDF was absent when this pass ran and was
installed afterwards with the rest of the doc-convert toolchain, so either would work today
— but `pypdf` needs no compiled dependency, and PyMuPDF now warns that the bare `import
fitz` spelling is deprecated in favour of `import pymupdf`. Save as `/tmp/check.py`:

```python
import sys
from pypdf import PdfReader
r = PdfReader(sys.argv[1])
t = "".join(p.extract_text() for p in r.pages)
imgs = {im.name: len(im.data) for p in r.pages for im in (p.images or [])}
big = {n: s for n, s in imgs.items() if s > 5000}
print(f"pages={len(r.pages)} images={len(imgs)} diagrams={len(big)}")
print("source leak:", "LEAK" if "flowchart LR" in t or "sequenceDiagram" in t else "clean")
print("footer:", "Page 1 of" in t)
```

```sh
python3 /tmp/check.py /tmp/wf.pdf
```

**Pass =** `pages=9 images=6 diagrams=5`, `clean`, `footer: True`.

**Count the big images, not every image.** WeasyPrint rasterises the `✅`/`❌` emoji in this
document into a single ~2.3 kB PNG XObject, shared across all nine pages. A checker that
counts unique images therefore reports **6**, not 5, and a naive `diagrams=5` assertion fails
on a perfectly good PDF. Proof: that same PNG is present when `mmdc` is absent and zero
diagrams render. The 5 real diagrams are 120-270 kB each, so the 5 kB threshold separates
them cleanly. Edge/SVG on Windows does not show this, which is why it was missed there.

Aspect ratios need no PyMuPDF either, but assert the right thing. `_figure_style()` emits a
width with `height:auto`, so the placed ratio equals the source ratio **by construction** —
comparing them is a check that cannot fail. What *can* fail is the height clamp: if the
emitted width implies a height above the cap, the CSS `max-height` clamps height alone and
the diagram stretches sideways. That is the bug `MAX_FIGURE_H_MM` exists to prevent, so
assert it:

```sh
python3 - <<'PY'
import struct, importlib.machinery, importlib.util
from pypdf import PdfReader
ldr = importlib.machinery.SourceFileLoader("m", "/mnt/rojaws/localDev/setup/tooling/md2pdf")
m = importlib.util.module_from_spec(importlib.util.spec_from_loader("m", ldr)); ldr.exec_module(m)
cap = m.MAX_FIGURE_H_MM * m.PX_PER_MM
seen, bad = {}, 0
for p in PdfReader("/tmp/wf.pdf").pages:
    for im in (p.images or []): seen.setdefault(im.name, im.data)
for n, raw in sorted(seen.items(), key=lambda kv: -len(kv[1])):
    if raw[:8] != b"\x89PNG\r\n\x1a\n" or len(raw) < 5000: continue
    w, h = struct.unpack(">II", raw[16:24])
    fw = float(m._figure_style(w, h, m.PNG_SCALE).split("width:")[1].split("px")[0])
    fh = fw / (w / h)
    ok = fh <= cap + 1          # 1px of slack: the width is rounded to %.0f
    bad += not ok
    print(f"  {w}x{h} ratio={w/h:.4f} -> {fw:.0f}x{fh:.0f}px  {'OK' if ok else 'OVER CAP'}")
print(f"cap={cap:.1f}px over_cap={bad}")
PY
```

**Pass =** `over_cap=0`. Observed on deb 2026-08-28: five diagrams, the tall 0.7164 sequence
diagram clamped to 757px against a 755.9px cap — inside the 1px rounding slack, and the one
that motivated `MAX_FIGURE_H_MM` in the first place.

Fail-soft must still hold afterwards — keep `~/.local/bin` on PATH or you are testing
nothing, and drop only the directory holding `mmdc`:

```sh
echo "mmdc lives in: $(dirname "$(command -v mmdc)")"
PATH="$HOME/.local/bin:/usr/bin:/bin" md2pdf /mnt/rojaws/localDev/setup/WORKFLOWS-OVERVIEW.md /tmp/nomm.pdf
echo "exit=$?"
```

**Pass =** the `mmdc` warning on stderr, **exit 0**, fences as source. A non-zero exit, or
`command not found`, is a fail. If `mmdc` turns out to live somewhere still on that PATH,
hide its directory explicitly instead.

## 7. Referee change — read-only

```sh
grep -rn 'AL_TEST_BACKEND' /mnt/rojaws/localDev/setup/pipeline/ | head
```

Read `pipeline/RUN-BUILD.md` on the two new infrastructure-failure conditions (`7177ddf`)
and say whether the code matches what the doc claims. A documented condition with no
corresponding branch is worth reporting. Keep this section read-only — builds are section 8.

## 8. A real build

deb is the main client, so this is the box where a build actually matters.

```sh
alw route "a tiny codeunit that returns the current user id"
```

`alw route` is the cheapest end-to-end exercise: resolve `SETUP_DIR`, reach Larry over
11443 through pi's provider, get a classification back. If that works, the wiring is sound.

Only then, and only if you have time, try one real build in a scratch prototype (`alw new`,
then `alw build`). Expect it to be slow. **Do not promote anything**, and do not escalate to
Claude — the egress gate should refuse, and a refusal there is a PASS for section 4, not a
failure here.

If a build fails, report the referee's own output. The AL compiler is the referee, so its
errors are the finding — do not critique the model's code quality; that is not this pass.

---

## Reporting

A table of section to PASS / FAIL / BLOCKED, with observed output for anything not green.

- **Fix what is clearly broken on this box** — install `mmdc`, re-run the relink script. Do
  **not** change repo code to make a check pass, and never fix by editing a test. Repo
  changes are a separate conversation; this is a verification and repair pass on deb.
- **BLOCKED is legitimate.** Say so plainly rather than skipping quietly.
- **Quote the shortest decisive line** of any failure, not the whole log.
- **If a check contradicts this document, trust what you observed and say so.** This brief
  was written on the Windows work box from a single SSH survey of deb, and an earlier
  version of it was written for the wrong machine entirely. Treat its factual claims as
  reported, not proven.
