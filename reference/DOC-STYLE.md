# Engineering Handbook — documentation style

The house style for technical handbooks (Larry, BC-on-Linux, and any `bcw
analyse` / architecture write-up). Distilled from two docs iterated to ~9.5/10 in
review. Apply it to any substantial system doc so the set reads like volumes of
one library, not scattered project notes.

> **The one rule:** a handbook connects **constraint → investigation → design
> decision → implementation → verification**. Every workaround traces to the
> specific upstream behaviour it works around; every non-obvious claim is grounded
> in observed behaviour (a file:line, a benchmark number, a failure mode), never a
> generic assertion.

---

## The spine (section order)

Same skeleton every time, grouped into skimmable **layers** with banner dividers
(`# ═══ Overview ═══`, `# ═══ Architecture ═══`, `# ═══ Implementation
reference ═══`, `# ═══ Maintenance ═══`):

**Overview** (answers *why does this exist, does it work?*)
1. **Title + one-liner** blockquote. Include a single memorable framing sentence
   if the subject has one ("The KVM guest is the only Windows in the building").
2. **Document map** — a table routing the reader to the right layer in ~20 s.
3. **Status callout** — 🟢 live / 🟡 experimental / 🔴 broken / ⚪ retired / 🟠
   pending. Put it *first*, not buried at the end. Reader must know maturity
   before reading anything.
4. **What this project achieves** — ✅ checklist an exec can read in one screen.
5. **Quick start** — the happy-path commands, before any reference detail.
6. **Design principles** — 5–7 numbered principles that explain *why* the system
   looks the way it does. Downstream choices should fall out of these.
7. **Lessons learned — engineering notes (EN-1, EN-2, …)** — collect the *why*
   decisions in one numbered place so implementation sections can cite "see EN-5".

**Architecture** (answers *how is it shaped?*)
8. **Core constraint** — start with the *problem*, not the solution.
9. **Capability comparison table** — where each option/tool fits (❌/✅ grid).
10. **Diagrams** — numbered `Figure N` with an italic caption each.

**Implementation reference** (answers *how does it actually work?*) — commands,
networking, provisioning, package layout, and the **Sharp edges** (see below).
Do **not** water this down; the hard-won detail is the point.

**Maintenance** — *what breaks on an upstream change?* A checklist per drift
trigger (new vendor version, etc.).

**Provenance** — what came from upstream, what was reused, what is genuinely new.

---

## Devices that carry the quality

- **Separate three kinds of information** and never blur them: **constraint**
  ("Windows-only forever"), **implementation** ("use dockur/windows"),
  **evidence** ("proven 2026-07-31"). Keeping them distinct is what makes a doc
  trustworthy.
- **A callout for the one idea.** A single 🧭 box near the top stating the
  system's philosophy in two sentences ("The compiler is the referee").
- **Reference vs runbook split.** Body answers "how does it work"; appendices
  answer "how do I rebuild it". Install commands, troubleshooting → appendices.
- **Deployment vs architecture versions.** In a version table, mark packaging
  details (nginx build, python) as drift-expected, not contracts.
- **Glossary.** One table defining project-specific terms a newcomer won't know.
- **"What it is *not*."** A short boundaries list keeps the architecture honest.
- **A worked example.** One concrete end-to-end walk-through ("A typical build")
  ties the concepts together.
- **Numbered figures + numbered engineering notes**, so prose can cite them.

## The "Sharp edges" pattern (the most valuable section)

For each non-obvious trap, write **three things**: *what happened · why · how to
avoid it* — and **name the regression test** that guards it. These are the
institutional-knowledge nuggets that vanish from commit history. Examples of the
texture to aim for: "hiding the `Len`/`Stat` interface drops SFTP from 52 to
3-5 MiB/s"; "`windows.boot`, not the ISO, is the reinstall marker".

## Diagrams

Mermaid (renders natively in Artifacts). One diagram often replaces several
hundred words. Number every one `Figure N` with an italic caption. Prefer:
system architecture, an end-to-end flow, a package/dependency reuse map, a
provisioning/sequence diagram.

## Tone — Simplified Technical English

Terse, specific, active voice. Specificity is the credibility signal — a real
failure mode ("Go negotiated a different host-key algorithm") reads as genuine
engineering. A generic observation reads as filler. No hedging, no marketing.

**The sentence layer is ASD-STE100 Simplified Technical English.** This spine
governs *structure*; STE governs *wording*. Full rules + linter live in
`setup/tooling/ste/` (skill: `/ste`, auto-triggering Claude skill `ste-writing`).
The load-bearing subset:

- **Active voice, simple tenses.** "The parser reads the file", not "the file is
  read by the parser". No present perfect ("we have received"), no modal stacks
  ("this may help to improve").
- **One name for one thing.** Never rotate check / verify / validate for the same
  action. Same rule as the glossary — a synonym is a new concept to the reader.
- **Short common words.** use (not utilize), make sure (not ensure), do (not
  perform), start (not initiate), also (not furthermore), about (not regarding).
- **Sentence caps:** 20 words for an instruction, 25 for descriptive prose. One
  topic per paragraph, six sentences maximum.
- **No semicolons, no contractions, no phrasal verbs** ("spin up", "dive into"),
  no nominalizations ("perform an analysis of" → "analyse").
- **Noun clusters ≤ 3 words.** Unpack "the agent task queue priority handler".
- **No marketing adjectives** — seamless, robust, powerful, world-class.

**Two registers.** *Flavored* for handbook prose and reference sections. *Strict*
for anything the reader follows with their hands: quick start, runbooks,
appendix procedures, user guides, error messages. Strict adds the STE word set
(but/because/can/must, not however/since/may/should) and the safety pattern —
**WARNING** = injury, **CAUTION** = damage, **NOTE** = information only, never an
instruction, each placed directly before the step it protects.

**Two house deviations:** keep British spelling (STE rule 1.14 asks for American
— ignored), and STE never licenses dropping a grounded detail. If a file:line, a
benchmark number, or a scope qualifier will not fit in 25 words, keep the long
sentence and let it fail the lint.

**Gate.** Lint before you claim a doc is finished:

```bash
python3 /mnt/rojaws/localDev/setup/tooling/ste/ste-lint.py doc.md
```

Violations per 100 words. Target **under 2.5** flavored, **under 1.5** strict
(`--strict`). Use `--fail-over 2.5` in a hook or CI gate.

The linter is a heuristic, not a certifier. Two known false-positive classes:
a rule file that *quotes* the banned words scores badly (this section costs this
file 1.92 → 2.99), and a doc heavy on shell examples inflates the noun-train
marker. Read the categories, not only the total.

---

## Can a local model (Larry) write these?

**Partly — and that's the right split.** A local model, given this recipe as a
prompt, reliably produces the **skeleton**: the layer order, the status/achieves/
principles sections, the document map, figure and EN scaffolding, a comparison
table. That is most of what makes these docs *navigable*.

What it **cannot** invent is the **substance** — the file:line citations, the
"this cost two days" failure modes, the benchmark numbers, the reason a
workaround succeeds. That comes from having debugged the system. So:

- **Larry drafts to the template** (`/handbook`, or `bcw analyse` output run
  through it) — structure, headings, the obvious prose.
- **A human / Claude fills the sharp edges** — the grounded specifics, verified
  against real code and real runs.

Same philosophy as the rest of the platform: **local drafts cheaply, the
expensive intelligence closes the last, load-bearing 10%.** A local model must
never *fabricate* a file:line or a failure mode to fill the template — an
un-filled `> TODO(grounding): …` placeholder is correct; an invented citation is
a defect.
