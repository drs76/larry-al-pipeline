# Benchmark fixture handover revisions

`/mnt/rojaws/localDev/projects/` had NO git history when the entries below were made, so
this file WAS that history — the exact diffs, so a benchmark result can be traced to the
handover text that produced it.

**Native history begins 2026-08-22 at `projects/` commit `1979043`**
("chore(fixtures): establish initial tracked fixture state"). That commit is the first
Git-tracked state; it does not reconstruct anything above it. From that point on, git is
the primary mechanism and this file is the BRIDGE for everything before it — keep it,
stop adding routine handover diffs to it.

The fixture repo is a sparse envelope: it tracks the 31 files a run consumes as INPUT
(handover, app.json, cleanup.sh, docs/, plus doclink's AGENTS.md/CLAUDE.md/war-games/) via
an allow-list `.gitignore`. Model output, `*.app` and ~76M of symbol packages stay
untracked. `librechat/` (own repo and remote), `bench/` (legacy harness) and unrelated
directories are outside the tracked set by design.

Going forward, record the fixture commit AND the handover hash in benchmark
receipts/metadata, so a suite can name the exact fixture revision it ran against.

Comparability: a revision boundary is not automatically an invalidation, and it is not
automatically harmless either. Read the diff, then state a rule per fixture. Do not
declare two distributions identical without checking; "the wording barely changed" is a
hypothesis, not a finding. See [[sample-size-efficacy]] discipline.

---

## p1 / bench-p1-crud — v2, 2026-08-22 — NOT COMPARABLE to v1

**Defect (satisfiability).** v1 required enum 50300 `"Equipment Status"` to be defined
*inside* `Equipment.Table.al`, while the manifest listed 5 files and the handover closed
with "Do not create additional files". The enum could not be written without breaking the
manifest, and nothing verified file CONTENTS — only that the 5 named files existed.

**Observed effect.** Every model tested resolved the conflict by silently omitting the
enum, then failed all 6 repair rounds on the identical error:

    Equipment.Table.al(34,31): error AL0185: Enum 'Equipment Status' is missing

Reproduced across qwen3-coder:30b and north-mini-code-1.0 — a boundary that does not ease
with capability, which is the signature of a spec defect rather than a model limit.

**Change.** Enum moved to its own file `src/EquipmentStatus.Enum.al`; manifest 5 -> 6
files; permission set ID added to the ID table; ✓/✗ examples added for one-object-per-file
and for base-app enums needing `using` rather than a local definition; `platform` corrected
to `27.0.0.0`; the inaccurate claim that the pipeline derives app.json "from installed
symbols" corrected to "from the fenced JSON block in this handover" (see
`write_canonical_app_json()` in run-build.py).

**Verification.** A full six-file implementation of the v2 contract compiles CLEAN — zero
errors, zero warnings — against BC27 / runtime 16.0 with the full analyzer set including
PerTenantExtensionCop. This confirms the permission-set snippet
(`Caption = '...', MaxLength = 30;` and the `table = X` / `tabledata = RIMD` split),
the standalone enum, and the 50300-50399 ID range.

**Landmine found while editing.** `parse_manifest()` locates the manifest by searching for
the literal string "machine-readable manifest". Trimming that phrase from the heading as
redundant prose makes the manifest parse EMPTY and the write gate stop checking files.
The v2 handover carries a comment saying so.

**Baselines.** Fresh baselines start at the first post-v2 run. Historical p1 numbers were
measured against an unsatisfiable spec.

---

## p4 / bench-p4-unseen — v2, 2026-08-22 — comparability: CONDITIONAL (see rule)

**Defect (instruction consistency).** The read-first section restricted the model to
`00`, `02`, `03`, but the body then depended on `01-syntax-style.md` (file naming) and
`09-api-web.md` §26 (permission set syntax). The model had to disobey one instruction to
follow the other.

**Change.** Read set widened to the five files the handover actually relies on. The
context-budget warning is preserved. Nothing else touched — no objects, IDs, snippets or
manifest changes. Manifest still parses 8 files.

**Comparability rule.** Pre-revision results remain usable for capability findings that do
not depend on reference-file access. Do NOT pool pre- and post-revision results for
pass-rate comparisons until an A/B check confirms no material change in task difficulty.

---

## doclink / tsg-document-link-2-az-storage — v2, 2026-08-22 — comparability: CONDITIONAL

**Defect 1 (broken pointer).** Read-first item 0 pointed at
`/mnt/rojaws/localDev/al-reference/AL-REFERENCE.md`, which DOES NOT EXIST. The correct
path is `/mnt/rojaws/localDev/setup/reference/AL-REFERENCE.md`.

**Defect 2 (instruction consistency).** The handover cited `09-api-web.md` §26 for
permission set syntax without any bounded read set naming it.

**Change.** Path corrected; explicit bounded read set added listing the five topic files
the handover relies on; context-budget warning added. Nothing else touched. Manifest still
parses 9 files.

**Note.** doclink's own docs (`docs/SPEC.md`, `docs/TASKS.md`,
`docs/AL-PROJECT-STRUCTURE.md`) are unchanged and remain items 1-3 of the read list.

**Comparability rule.** Pre-revision results remain usable for capability findings that do
not depend on reference-file access. Do NOT pool pre- and post-revision results for
pass-rate comparisons until an A/B check confirms no material change in task difficulty.

---

## Exact diffs

```diff
--- p4 v1
+++ p4 v2
@@ -30,9 +30,16 @@
 ## Read first
 
 0. `/mnt/rojaws/localDev/setup/reference/AL-REFERENCE.md` — **index** of the AL syntax reference.
-   Read the index, then `al-reference/00-gotchas.md` (always), plus `al-reference/02-objects.md`
-   and `al-reference/03-records-performance.md`. **Do not read every topic file**: together they
-   are ~47k tokens and will not fit in context.
+   Read the index, then exactly these five topic files — they are the complete set this
+   handover relies on, and nothing below cites anything outside it:
+
+   - `al-reference/00-gotchas.md` (always)
+   - `al-reference/01-syntax-style.md` — file naming, quoting
+   - `al-reference/02-objects.md` — object structure
+   - `al-reference/03-records-performance.md` — record operations
+   - `al-reference/09-api-web.md` — §26 permission set syntax
+
+   **Do not read every topic file**: together they are ~47k tokens and will not fit in context.
 
 ## Object ID range
 

--- doclink v1
+++ doclink v2
@@ -34,7 +34,17 @@
 
 ## Read first
 
-0. `/mnt/rojaws/localDev/al-reference/AL-REFERENCE.md` — AL syntax reference, formatting rules, record operations, event subscriber pattern, TryFunction, Isolated Storage, ABS patterns, house conventions, LLM gotchas. Read this before writing any AL code.
+0. `/mnt/rojaws/localDev/setup/reference/AL-REFERENCE.md` — **index** of the AL syntax reference.
+   Read the index, then exactly these topic files — they are the complete set this handover
+   relies on, and nothing below cites anything outside it:
+
+   - `al-reference/00-gotchas.md` (always) — LLM gotchas
+   - `al-reference/01-syntax-style.md` — formatting, file naming, quoting
+   - `al-reference/02-objects.md` — object structure
+   - `al-reference/03-records-performance.md` — record operations
+   - `al-reference/09-api-web.md` — §26 permission set syntax
+
+   **Do not read every topic file**: together they are ~47k tokens and will not fit in context.
 1. `docs/SPEC.md` — full spec, architecture, AL objects to create, blob naming, event pattern
 2. `docs/TASKS.md` — task breakdown with acceptance criteria
 3. `docs/AL-PROJECT-STRUCTURE.md` — folder layout and file naming rules. Follow this exactly before creating any files.
```

---

# Verification (not revisions)

Compiler verification of the "write it EXACTLY as below" snippets and the pipeline claims.
These record that existing text was CHECKED; they are not changes to the fixtures and do
not create a revision boundary.

Method: extract each snippet verbatim, surround it with the minimum stubs its references
require, and compile with the real referee — BC27 / runtime 16.0, full analyzer set
including PerTenantExtensionCop, idRanges taken from the fixture's own app.json block.

## p1 / bench-p1-crud — VERIFIED 2026-08-22

Full six-file v2 implementation compiles CLEAN: 0 errors, 0 warnings. Confirms the
permission-set snippet, the standalone enum, and the 50300-50399 range.

## p4 / bench-p4-unseen — VERIFIED 2026-08-22

- app.json claim ACCURATE: "the pipeline overwrites `app.json` from this block" is exactly
  what `write_canonical_app_json()` does.
- Permission-set snippet (permissionset 50406 "Room Booking") compiles CLEAN: 0 errors,
  0 warnings. This includes the name collision between `permissionset "Room Booking"` and
  `table "Room Booking"`, which is legal — object names are unique per type.

## doclink / tsg-document-link-2-az-storage — VERIFIED 2026-08-22, with one finding

- Setup-table snippet (table 50103) compiles: 0 errors. Confirms `[NonDebuggable]`,
  `procedure GetSharedAccessKey(): SecretText`, and the
  `IsolatedStorage.Get(Key, DataScope, var SecretText)` overload on BC27.
- Permission-set snippet (permissionset 50110) compiles: 0 errors.
- Pipeline claim ACCURATE.

**FINDING — AA0215 on every file (warning, not error).** The manifest names files
`TSGDocumentLink*` while the objects are named `TSG Doc Link *`. CodeCop derives the
expected file name from the object name, so it wants `TSGDocLink*`:

    AA0215: The file TSGDocumentLinkAZSetup.Table.al has an incorrect name.
            The valid name is TSGDocLinkAZSetup.Table.al.

Consequence: every doclink build carries ~8 spurious warnings, adding noise to the
diagnostics this fixture exists to produce. Not fixed — renaming the manifest would be a
substantive revision and would invalidate doclink's baselines, AND would break the
historical warning profile's comparability. Poor trade for warning noise. Recorded so it
is not rediscovered as a model failure.

**"0 errors" does NOT mean "0 diagnostic noise" for doclink.** In any future
error-distribution analysis, AA0215 must be excluded or classified separately — it is
fixture-originated, not model-originated, and counting it would attribute a naming
convention to model behaviour.

Checked, not assumed: AA0215 occurs ONLY at `warning` severity (93 occurrences across all
logs, zero as `error`), and the capability tooling matches `: error ` with prefixes
`AL|AW|PTE` — `AA` is not in that set — while `capability_shadow.py` filters through
`_is_error()`. So AA0215 never entered any error profile, and the capability-trigger
analysis is uncontaminated by it. Retain that exclusion in any successor tool.

## map / tsg-map-integration — VERIFIED 2026-08-22, fully accurate

Structurally different from the others: NO "Read first" section and NO AL code blocks. It
inlines its own "AL Syntax Essentials" with ✓/✗ examples instead of citing reference
topics, so it is self-contained and check 5 passes by design rather than by omission.

A full four-object implementation (controladdin + CardPart page + two page extensions,
with the three JS/CSS resources) compiles CLEAN: 0 errors, 0 warnings.

Positive claims verified:
- quoted ControlAddin resource paths, relative to PROJECT ROOT (`'src/controladdin/map.js'`)
- `usercontrol` containing only a `trigger`, with `procedure` at page level
- `addlast(FactBoxes)` nested inside `layout { }`
- `using Microsoft.Sales.Customer;` resolves `"Customer Card"` on BC27
- `using Microsoft.Purchases.Vendor;` resolves `"Vendor Card"` on BC27
- the `CurrPage.<part>.Page.<procedure>()` call pattern
- `"platform": "1.0.0.0"` is harmless (the pipeline's canonical write reports
  `application`, not `platform`)

NEGATIVE claims verified by deliberately breaking the code — both are correct, and the
one error code the handover names is exact:
- unquoted `Scripts` path -> `AL0219: Syntax error, string literal expected` (the handover
  names AL0219 specifically, and it is right)
- `HtmlFiles` on a controladdin -> `AL0124: The property 'HtmlFiles' cannot be used in
  this context` (the handover says "compile error" without naming a code — accurate)

Its inlined ✓/✗ pattern is worth copying: it states the rule, shows both forms, and names
the resulting compiler error.

**CORRECTED 2026-08-22 — this verification was insufficient, and "fully accurate" was the
wrong conclusion.** Everything map SAYS is correct; the 20-run baseline then found
`PTE0008` in 16/20 runs, because the MapFactbox section OMITS `ApplicationArea` on the
usercontrol. Every run paid a repair round.

The verification missed it structurally, not carelessly. The gold implementation I compiled
put `ApplicationArea` on the page and the usercontrol because I know `PTE0008` exists — so
the compiler validated MY knowledge, not the handover's completeness. **A hand-authored
implementation cannot detect an omission its author unconsciously supplies.**

Fixed in `422c749`, verified by a SUFFICIENCY build (see the protocol below): the factbox
rebuilt from only the handover's stated properties, deliberately withholding the
page-level `ApplicationArea` it never asks for. Compiles clean.

---

# Hygiene actions (not revisions)

State cleanup in fixture directories. Recorded because `projects/` has no git history, so
a deletion is otherwise untraceable. These do not change any handover and do not create a
comparability boundary.

## p1 / bench-p1-crud — 2026-08-22

**Rationale.** The fixture held v1 build output: four `.al` files describing the old
five-file shape, sitting in a fixture whose handover now specifies six. Proven NOT to
reach benchmark runs — `bench-run-suite.sh` seeds only `app.json`, `cleanup.sh`, `docs/`,
`.alpackages/` and the path-rewritten handover, and its comment says so explicitly:
"src/ is deliberately NOT copied — the model writes it." So this is anti-confusion
hygiene, not a correctness fix.

`cleanup.sh` could not do it: it removes files NOT in the manifest, and all four stale
files share manifest names, so it preserved every one.

**Removed** (backed up first to the session scratchpad):

    src/Equipment.Table.al                    1474 b
    src/EquipmentCard.Page.al                 2149 b
    src/EquipmentList.Page.al                 1348 b
    src/EquipmentRegister.PermissionSet.al     273 b
    Bench_Equipment Register_1.0.0.0.app      7018 b
    .build-receipt.json                        975 b
    src/                                      (empty directory)

**Changed:**

- `app.json` — regenerated from the v2 handover block. It had drifted: fixture said
  `"platform": "1.0.0.0"`, handover v2 says `"27.0.0.0"`. Harmless either way (map uses
  1.0.0.0 and compiles) and the pipeline rewrites it at compile time, but `app.json` IS a
  seeded input, so a seeded file disagreeing with its own handover is worth removing.
- `README.md` — rewritten. The old one was itself model output from a v1 run: it described
  the five-file shape, documented the enum as living inside the table file, and claimed
  "Promoted actions handled correctly with actionref" for a fixture that has no actions.
  README is NOT seeded into runs, so this is documentation only.

**Kept:** `larry-handover.prompt.md`, `app.json`, `cleanup.sh`, `docs/`, `.alpackages/`.

**Verified after:** manifest still parses 6 files; `app.json` now equals the handover block.

**Note:** an NFS silly-rename stub (`.nfs00000000038660e2...`, 7018 b — the deleted .app)
remains until whatever holds the handle closes it. Expected, self-clearing, not an error.

---

# Fixture roles and frozen baselines

## p1 / bench-p1-crud — SMOKE / REGRESSION fixture. FROZEN at v2.

**Baseline, 2026-08-22** — suite `p1v2base`, 20 runs, qwen3-coder:30b both arms,
fixture commit `2043042`, handover `13e0b60c…`, all rows `provenance: tracked`,
`fixture_dirty: false`.

| metric | value |
|---|---|
| terminal pass | **20/20** |
| **clean round-1 compile** | **20/20** |
| manifest-complete round 1 | 15/20 |
| repaired / exhausted | 5/20 repaired, 0 exhausted |
| autonomous pass | 20/20 (no escalation) |
| duration | min 55s, p50 59s, max 99s |

**CORRECTED 2026-08-22.** This was first recorded as "first pass 15/20, fix rounds
{0:15, 1:5}", implying generation quality. It is not. Round 1 compiled clean in **20/20**
runs. All five "repairs" were the model omitting `app.json` — a manifest-completeness
event, on a file `write_canonical_app_json()` authors from the handover on every compile
regardless of what the model writes. See the metric terminology note below.

**Role: smoke / regression, NOT capability discrimination.** At a 100% final-pass ceiling
this fixture can no longer separate models or pipeline variants on pass rate — everything
scores 100%. Do not use it as the discriminating arm of an A/B.

What it still answers: *can this model/pipeline combination execute a simple, unambiguous
multi-object AL task end to end?* A regression that turns `{0,1}` repair rounds into
repeated stalls is immediately suspicious, and that is worth having.

**First-pass rate and repair-round distribution are FIRST-CLASS metrics here**, not
footnotes. A change can regress 75% first-pass to 30% while still finishing 20/20, and
final-pass rate alone would miss it entirely. Compare against `{0: 15, 1: 5}`.

**FROZEN. Do not make it harder because it passes.** The point of v2 was to obtain a
clean, provenance-addressable baseline; re-tuning difficulty would discard exactly that.
If a harder simple-CRUD fixture is wanted, add one — do not mutate this.

**Not a before/after.** v1's p1 rows are `legacy_missing` and were measured against an
unsatisfiable spec (the enum could not be written without breaking the manifest), so they
cannot be pooled with these. This establishes v2's rate from scratch; it does not quantify
an improvement.

## Intended roles of the other fixtures

| fixture | role | status |
|---|---|---|
| p1 v2 | smoke / regression | baselined, frozen |
| p4 | capability boundary | not yet baselined under v2 |
| doclink | capability boundary — known hard, ABS-heavy | not yet baselined under v2 |
| map | structural / control add-in shape | not yet baselined |

These are intended roles, asserted from fixture shape rather than measured. Only p1 has a
v2 baseline; the others' behaviour under their v2 handovers is unmeasured.

---

# Metric terminology — read before quoting a "first pass" number

`first_pass_compile` in the metrics is `build_ok AND NOT manifest_fail`. It conflates two
independent things, and that conflation has now produced misleading readings twice (p1's
"15/20", p4 v3's "13/20"). Always separate:

| layer | meaning | independent of |
|---|---|---|
| **clean round-1 compile** | every generated AL file compiled in round 1 | whether all files were written |
| **manifest-complete** | all expected files present | whether they compile |
| **terminal outcome** | repaired / exhausted / passed | both |

`fixture-audit.py` reports compile signatures independently of manifest failures. That
independence is exactly what exposed both p4 v2's deterministic defect AND p1's misleading
repair count — a tool that pooled them would have shown neither.

---

## p4 / bench-p4-unseen — REPAIR-DEPTH fixture. FROZEN at v3.

**Baseline, 2026-08-22** — suite `p4v3base`, 20 runs, qwen3-coder:30b both arms, fixture
commit `6b7e49a`, all rows `provenance: tracked`, `fixture_dirty: false`.

| metric | value |
|---|---|
| terminal pass | 19/20 |
| **clean round-1 compile** | **16/20** |
| repaired | 3/20 |
| exhausted | 1/20 |
| `app.json` omissions | 4/20 (recorded separately — file completeness, not AL quality) |
| duration | min 69s, p50 **77s**, max 228s |

### The v2 -> v3 intervention, and why it is trusted

v2 was `AL0162` on `RoomBooking.Table.al` in **20/20** runs — a handover line that stated
the End Time validation detached from its field and never said where the trigger goes.
v3 bound it to the field and showed the construct. Prediction and outcome:

| | v2 (`e22b8a1`) | v3 (`6b7e49a`) |
|---|---|---|
| AL0162 round 1 | 20/20 | **0/20** |
| replacement near-universal signature | — | **none** (top is AL0175 at 2/20) |
| clean round-1 compile | 0/20 | **16/20** |
| fix rounds | {1:6, 2:11, 3:3} | {0:13, 1:6} |
| duration p50 | 114s | **77s** |

**v2's 0/20 first-pass was an instrumentation tax, not fixture difficulty.** One line cost
every run a repair round and ~37s.

### Terminal pass fell 20/20 -> 19/20, and that is FINE

v3's single exhaustion (control r7) is a different failure mode: broad syntax collapse
across two files (22x AL0219, 14x AL0114, 8x AL0104), six rounds, no convergence — the
degraded-generation profile, unrelated to the fix.

16 clean + 3 repaired + 1 exhausted is a HEALTHIER fixture than 20 repaired, despite the
worse headline. v2's fix loop was never tested: it always had the same easy thing to fix.

### Role: repair-depth, not capability boundary

p4 ceilings on terminal pass like p1, so it cannot discriminate there. Its signal is
**clean round-1 compile rate and repair depth**, which has real dynamic range: a change
could move {0:13, 1:6} toward all-clean or toward exhaustion, and either is plainly
visible. Compare against `clean round-1 16/20` and `{0:13, 1:6}`.

**FROZEN.** Do not tune difficulty. If a harder fixture is wanted, add one.

---

# Operational state vs historical baselines

Two layers, deliberately not collapsed. A baseline is a MEASUREMENT taken at a commit and
is immutable. Operational state is what a run today will actually use. Conflating them
destroys the ability to tell "this number was measured on a different fixture" from "this
number moved".

    p1:  v2 freeze  ->  scoped omission experiment  ->  operational promotion
    p4:  v3 freeze  ->  post-freeze manifest experiment  ->  operational promotion

## The replicated mechanism — stated narrowly

Adding an explicit required-output line at the task->manifest transition —

> **`app.json` is also a required output.** Write it exactly as specified in the
> `## app.json` section above, in addition to every `.al` file listed below.

— reduced the observed `app.json` omission tax across BOTH edited fixtures:

| fixture | before any edit | after AL code block added | after explicit line |
|---|---|---|---|
| p1 | 1/24 | 5/20 | **0/20** |
| p4 | 0/20 | 4/20 | **1/20** |

Pooled: edited-without-line 9/40 vs edited-with-line 1/40, **Fisher p = 0.0143**.
p1 alone: 5/20 vs 0/20, p = 0.047. p4 alone was underpowered (p = 0.342); p1 replicates
it independently.

**Scope limit.** This says the explicit wording removes the omission tax IN THESE TWO
FIXTURES, where the tax appeared after AL code blocks were added to the objects section.
It does NOT establish that code blocks are universally causal, nor that the wording is
needed in handovers that never showed the tax — p4 v2 and doclink both ran 0/20 without
it. Do not propagate on theory; measure first.

The regression was self-inflicted: the p1 v2 and p4 v3 edits both added AL code blocks and
both introduced the tax. It was caught only because manifest completeness is reported
independently of compile signatures.

## p1 / bench-p1-crud

**Historical baseline: v2, suite `p1v2base`, IMMUTABLE.** 20/20 terminal, 20/20 clean
round-1 compile, 5/20 `app.json` omissions, {0:15, 1:5} repair rounds. The repairs were
omissions, not compile failures — see the metric correction above. Do not restate this
with today's numbers.

**Operational state: `26d56c9`** (fixture repo), validated by suite `p1appjson`:

| metric | value |
|---|---|
| terminal pass | 20/20 |
| clean round-1 compile | **20/20** |
| `app.json` omissions | **0/20** |
| repaired / exhausted | 0 / 0 |
| compile rounds | **min 1, max 1** |
| duration p50 | ~61s |

**ROLE CONSEQUENCE — p1 now has no discriminating signal.** Every run is one clean round.
The repair-round distribution that its v2 record promoted to a first-class metric is now
identically zero. It is a pure end-to-end smoke fixture: its meaningful outcome is
pipeline success/failure and nothing else. Do NOT use it in an A/B, and do not read a
first-pass or repair-depth number from it — there is no longer any variance to read.

## p4 / bench-p4-unseen

**Frozen compile-quality baseline: v3 `6b7e49a`, suite `p4v3base`.** Clean round-1 compile
16/20, repaired 3/20, exhausted 1/20, {0:13, 1:6}, p50 77s. This remains the reference for
compile quality and repair depth.

**Operational state: v4 `a00035f`**, validated by suite `p4v4appjson`. Manifest-completeness
revision only — task semantics and compile requirements unchanged:

| metric | v3 (baseline) | v4 (operational) |
|---|---|---|
| clean round-1 compile | 16/20 | 18/20 |
| repaired | 3/20 | 2/20 |
| exhausted | 1/20 | 0/20 |
| `app.json` omissions | 4/20 | **1/20** |
| deterministic signature | none | none |

v4's compile numbers are incidental — n is small and the added line should not affect AL
quality. v3 stays the cited compile-quality baseline. v4's contribution is the omission fix.

v3's single exhaustion (broad syntax collapse, control r7) did not recur across the 40
subsequent runs, supporting the reading that it was generation variance.

---

## doclink / tsg-document-link-2-az-storage — CAPABILITY-BOUNDARY fixture

### Pre-baseline diagnostic — v2, suite `doclinkv2base` (commit `36656d5`)

1/20 terminal pass, 19/20 exhausted, p50 287s. **NOT a clean capability measurement.**
`fixture-audit.py` found `AL0162` on `TSGDocumentLink.TableExt.al` in **12/20 runs (60%)**,
3x the next signature:

    'OnBeforeExportToStream' is not a valid trigger for this object type
    'OnBeforeGetAsTempBlob'  is not a valid trigger for this object type

Same "requirement detached from its AL construct" pattern as p1 v1 and p4 v2. The handover
said "subscribe to `OnBeforeExportToStream` on table 1173" and printed the exact event
signatures in a bare fenced block — no attribute, no enclosing object. `EventSubscriber`
appeared NOWHERE in the handover or its docs. Since the tableextension extends table 1173,
writing a trigger there is the obvious misreading, and a tableextension accepts only
`OnInsert`/`OnModify`/`OnDelete`/`OnRename`.

Retained as evidence of the defect, not pooled with v3.

### Capability baseline — v3, suite `doclinkv3base` (commit `167b68a`)

All 20 rows `provenance: tracked`, `fixture_dirty: false`, one commit, one handover hash.

| metric | value |
|---|---|
| terminal pass | **0/20** |
| exhausted | **20/20** |
| clean round-1 compile | 0/20 |
| compile rounds | **min 6, max 6** — every run burns the full budget |
| top round-1 signature | 4/20 (20%), `variance` — no flag |
| duration | min 215s, p50 319s, max 526s |

**The patch worked and changed nothing.** `AL0162` went 12/20 -> 0/20 with no replacement
dominant signature, and the pass rate moved 1/20 -> 0/20, which is noise. That is the
result that makes this baseline trustworthy: a real 60% ambiguity was removed and the
difficulty did not move, so the difficulty is not instrumentation.

Failure profile is broad and scattered across all five object types — AL0132 invented
members, AL0133 wrong argument types, AL0111, AL0224, AL0244, AL0104 — with no single
cause above 20%.

### The supported conclusion, stated narrowly

> Under the CURRENT model, pipeline, six-round repair budget and clean v3 handover,
> doclink is a reliable capability-boundary fixture: the model exhausts its budget on
> broad ABS-heavy implementation errors rather than converging on a deterministic
> handover defect.

NOT "the model cannot do doclink". A stronger model or a different pipeline strategy may
move the boundary — the Claude capability probe wrote the three blob codeunits clean in
289s. That is the question this fixture now exists to answer, and it can answer it
credibly because the known deterministic defect has been removed and measured.

---

# Fixture matrix — validated 2026-08-22

| fixture | operational role | measured signal | baseline |
|---|---|---|---|
| p1 | smoke test | binary pipeline health; 20/20 single clean rounds | `26d56c9` |
| p4 | repair depth | 18/20 clean first pass, graded repair signal | v3 `6b7e49a` (compile), v4 `a00035f` (operational) |
| doclink | capability boundary | 20/20 exhausted, broad profile, no dominant trap | v3 `167b68a` |
| map | structural / control add-in | 18/20 clean first pass, 19/20 terminal | v2 `422c749` |

Three distinct failure regimes measured under tracked provenance, rather than pass/fail
rows whose fixture state was unknown. Before the audit cycle a model comparison on doclink
would have been contaminated by at least one deterministic handover defect; it no longer is.

---

# FIXTURE VALIDATION PROTOCOL

The standard gate for any new fixture or handover revision. Derived from four defects
found this session, each of which a single static or hand-authored check could not have
distinguished:

| fixture | defect | why static review missed it |
|---|---|---|
| p1 | required construct made impossible by surrounding requirements | manifest and body read fine in isolation |
| p4 | validation requirement never said where the AL trigger belonged | every stated fact was true |
| doclink | event signatures given with no `[EventSubscriber]` construct | signatures were correct, verified against symbols |
| map | `ApplicationArea` on a usercontrol simply absent | reviewer supplied it from domain knowledge |

## The three questions are genuinely different

    Correctness         is the specification TRUE?
    Sufficiency         is the specification COMPLETE?
    Repeated execution  can the MODEL reliably interpret it?

None substitutes for another. A knowledgeable reviewer compensates for omissions. A
compiler validates only what it is given. A successful gold implementation confirms the
reviewer's expertise. Only a constrained build tests whether the spec stands alone, and
only repeated execution reveals systematic model-handover interaction.

## The gate

    inventory -> correctness -> sufficiency -> repeated execution -> signature audit -> freeze

### 1. Inventory

Parse the manifest; verify tracked inputs, object IDs, names, assets; confirm generated
output, symbols and stale build state are excluded; record the fixture revision under test.
Do not baseline against a drifting input state.

### 2. Correctness — is it true?

Verify every explicit claim against the compiler, symbols and platform: object types, IDs,
relationships, syntax and construct placement, event names and signatures, required
properties and valid values, expected error codes. Check NEGATIVE claims too — map names
`AL0219` for an unquoted path and it is exactly right, which is worth knowing.

Passing means *what it says is valid*. It does NOT mean *what it says is enough*.

### 3. Sufficiency — is it complete?

**Build a complete implementation using ONLY requirements the handover explicitly states.**

- do not silently add domain knowledge
- do not repair unstated omissions from memory
- do not treat an existing gold implementation as evidence of completeness
- deliberately WITHHOLD known-but-unstated requirements

> **If the verifier must add something from domain knowledge to make it compile, the
> handover was not sufficient.**

Patch and repeat until the stated requirements stand on their own. This is cheap — one
compile — and map's `PTE0008` was catchable this way instead of by 20 runs.

### 4. Repeated execution — can the model interpret it?

Run the suite with provenance enabled. Record fixture revision, round-1 signatures, clean
round-1 compile, manifest completeness, repaired, exhausted, repair-round distribution,
terminal outcome, duration.

**Begin analysis with round-1 signatures, before pass rate.** p4 had a deterministic
invalid trigger in 20/20 runs while final compile stayed 20/20 — pass rate showed nothing.

### 5. Signature audit

Classify by concentration (`fixture-audit.py`): spec-trap, dominant, common, variance.
The bands are diagnostic aids, not a substitute for judgement — doclink's defect appeared
at **60%**, and an 80% cutoff fitted from p4's single 100% case missed it.

For any deterministic or dominant signature: identify the exact error/object/construct,
trace it to the handover, determine whether the requirement is wrong, ambiguous, detached
from its construct, or omitted, patch, compiler-verify the repair, and rerun before
freezing.

**Do not accept a known systematic repair tax because the final pass rate is high.**

A flat scattered profile with persistent exhaustion, AFTER known defects are removed, is
evidence of a capability boundary rather than a spec trap. doclink v3 is that case.

### 6. Keep outcome layers separate

Round-1 compile quality / manifest completeness / repair behaviour / terminal outcome are
NOT interchangeable. p1 showed why: 20/20 compiled clean in round 1, but 5 looked like
non-first-pass because `app.json` was missing — manifest completeness, not compile quality.
Never report a single `first_pass` number that conflates them.

### 7. Freeze

Freeze when provenance is stable, correctness and sufficiency have passed, no known
deterministic or dominant defect remains, and repeated execution has established the
outcome and repair distribution.

A frozen baseline is an immutable MEASUREMENT, not necessarily current operational state.
On a later handover change: preserve the earlier baseline, label the new work an
experiment, pre-register its decision rule, and promote separately. Never silently rewrite
a historical measurement when operational state moves.

## Orchestration: verify the produced EFFECT, not the command's apparent success

The same discipline the protocol demands of handovers applies to running the suites. A
`mapv2base` launch failed silently — `nohup` could not find `./bench-run-suite.sh` because
the command ran from the wrong directory after a `cd` — and the check that "confirmed" it
was running was `pgrep -f "bench-run-suite.sh mapv2base"`, which matched THE WATCHER'S OWN
command string. Both checks reported success; zero runs had happened.

Before treating a suite as running, require evidence it PRODUCED something:

- the summary/log file exists, with the suite's own header line in it
- a captured PID, alive via `kill -0 "$PID"` — never a pattern match
- completion keyed on the suite's explicit `=== <TAG> SUMMARY ===` marker
- PID death BEFORE that marker treated as failure

**`pgrep -f` is unsuitable for watching a suite from a watcher whose own command line
contains the suite name.** It self-matches, so the liveness test is always true and a death
is never reported. This has now been hit twice: once on a transient wrapper PID, once on
self-match. Prefer absolute paths on launch and `kill -0` on a captured PID.

## The bar

A fixture is not ready for analytical baselining because it compiles once, nor because it
has a high final pass rate. It is ready when the measured result is **no longer known to be
dominated by a defect in the fixture itself**.

---

## map / tsg-map-integration — STRUCTURAL fixture

### Pre-baseline diagnostic — v1, suite `mapv1base` (commit `167b68a`)

19/20 terminal pass, but **0/20 clean first pass** and `PTE0008` on `MapFactbox.Page.al` in
**16/20 runs (80%, spec-trap)**:

    UserControl 'MapControl' must have a value for the ApplicationArea property

Every run paid at least one repair round (`min 2` compile rounds). The handover's MapFactbox
section listed PageType, Caption, the usercontrol, the trigger, the vars and the procedure —
and omitted the one property PerTenantExtensionCop requires on a usercontrol.

NOT accepted as a baseline: the 19/20 headline measured a known handover tax.

### Baseline — v2, suite `mapv2base` (commit `422c749`)

All 20 rows `tracked`, `fixture_dirty: false`, one commit, one handover hash `a80b12aa`.

| metric | v1 | v2 |
|---|---|---|
| `PTE0008` | 16/20 | **0/20** |
| clean round-1 compile | 0/20 | **18/20** |
| repaired | 19/20 | 1/20 |
| exhausted | 1/20 | 1/20 |
| terminal pass | 19/20 | 19/20 |
| compile rounds | min 2, max 6 | **min 1**, max 6 |
| duration p50 | 108s | **82s** |
| top round-1 signature | PTE0008 80% | 2/20 (10%) variance |

Role: **structural coverage** — control add-in, JS/CSS assets, page extensions on base-app
pages. Not a difficulty fixture; its distinct value is the object shapes no other fixture
exercises.

---

# FIXTURE MATRIX — LOCKED 2026-08-22

All four fixtures provenance-valid, systematically audited, and measured AFTER known
deterministic defects were removed.

| fixture | role | baseline | clean round-1 | terminal | signal |
|---|---|---|---|---|---|
| p1 | smoke | `26d56c9` | 20/20 | 20/20 | none — 1 clean round every run |
| p4 | repair depth | v3 `6b7e49a` / v4 `a00035f` | 16-18/20 | 19-20/20 | graded repair distribution |
| doclink | capability boundary | v3 `167b68a` | 0/20 | **0/20** | terminal-failure headroom |
| map | structural | v2 `422c749` | 18/20 | 19/20 | control add-in / asset shapes |

**Every fixture had a defect, and static review caught none of them.** p1's surfaced as
terminal failure, p4's as a deterministic repair tax behind a 20/20 pass rate, doclink's as
a 60% dominant signature, map's as an 80% omission behind a 19/20 pass rate. Three of the
four were invisible in the headline number.

**No fixture edits during the model experiment.** A fixture moving mid-experiment voids it,
exactly as p4 v2's tax voided its own numbers. Any further handover change is a new
experiment with its own pre-registered decision rule and its own baseline.
