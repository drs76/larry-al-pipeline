---
description: /handbook — write or restructure a technical doc as an engineering handbook in the house style
argument-hint: "<path-or-topic> [restructure|new]"
---
> **`$SETUP_DIR`** = the larry-setup repo on this machine. Resolve once, first that exists: `$SETUP_DIR` · `~/larry-setup` · `/mnt/rojaws/localDev/setup` (same chain `alw` uses).

# /handbook — write an engineering handbook in the house style

Produce (or restructure) a technical document as an **engineering handbook** that
follows the house style in `$SETUP_DIR/reference/DOC-STYLE.md`.
**Read that file first** and apply its spine, devices, and tone. Use it for any
substantial system/architecture doc, and to shape `bcw analyse` output
(WIKI / performance) into the same shape.

## Usage
`/handbook <path-or-topic> [restructure|new]`
- **restructure** — reorganise an existing doc into the layered spine without
  losing technical content.
- **new** — draft a fresh handbook for the named system.

## What to do
1. Read `DOC-STYLE.md`. Follow the spine: **Overview** (title one-liner →
   document map → status callout → what it achieves → quick start → design
   principles → lessons learned EN-1…) → **Architecture** (core constraint →
   capability comparison → numbered figures) → **Implementation reference**
   (commands / detail / **sharp edges** with named regression tests) →
   **Maintenance** (what breaks on upstream change) → **Provenance**.
2. Use the devices: the one-idea 🧭 callout, reference/runbook split (commands to
   appendices), glossary, "what it is *not*", a worked example, `Figure N`
   captions, numbered engineering notes.
3. **Start with the problem, not the solution.** Separate constraint /
   implementation / evidence. Keep the sharp-edges detail — don't water it down.
4. Diagrams in **mermaid** (renders in Artifacts), each numbered + captioned.

## Grounding — hard rule
Every non-obvious claim must be grounded in **observed behaviour**: a file:line,
a real failure mode, a benchmark number, a proven-on date. **Never fabricate** a
citation, a line number, or a failure mode to fill the template. If you don't
have the grounding, leave a visible `> TODO(grounding): <what to verify>`
placeholder for a human/Claude to fill — an honest gap beats an invented fact.
(A local model on Larry is expected to produce the *structure* and obvious prose;
the grounded specifics are closed by whoever debugged the system.)

## Sentences — Simplified Technical English (hard rule)
The spine is the *structure* layer. The *wording* layer is **ASD-STE100 STE**, per the "Tone" section
of `DOC-STYLE.md`. Apply it to every sentence you write: active voice, simple tenses, one name for
one thing, short common words, ≤20 words per instruction and ≤25 per descriptive sentence, no
semicolons, no contractions, no phrasal verbs, no marketing adjectives, noun clusters ≤3 words.
Use the **strict** register for quick-start steps, runbooks, appendix procedures and any user guide.
The full rules and the two house deviations (British spelling stays, never drop a grounded detail to
hit a length cap) are in `$SETUP_DIR/tooling/ste/SKILL.md` — read it before writing.

Lint before you hand the doc back, and report the score:
```sh
python3 $SETUP_DIR/tooling/ste/ste-lint.py <doc.md>            # target < 2.5 /100w
python3 $SETUP_DIR/tooling/ste/ste-lint.py --strict <doc.md>   # procedures: < 1.5
```
STE outranks style preference on wording. **Grounding outranks STE** — if a file:line or a benchmark
number will not fit the length cap, keep the long sentence.

## Output
Markdown. If the caller wants it shareable, it publishes cleanly as an Artifact
(mermaid renders natively). Match an existing doc in the set for cross-consistency.
