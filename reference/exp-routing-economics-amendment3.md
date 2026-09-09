# AMENDMENT 3 — routing economics: Arm C replaced again (map fixture repo destruction)

Amends `exp-routing-economics-preregistration.md`, following Amendments 1 and 2.
**Pipeline hardening + one fixture-infrastructure line. No change to the rule, thresholds,
allocation, strict attribution, containment, foreign-row rejection, or scoring.**

## 1. `routecon4` Arm C is VOID at 23/40

Artifacts preserved at `bench-results/routecon4-armC-void/`. **Spend: $0.00.** Excluded from
analysis. Its 23 completed cells are NOT merged into the replacement.

VOID at `map/r4` — the first map run in any suite where the rule actually fired:

    VOID: produced NO new metrics row
    CalledProcessError: git commit "scrubbed baseline" (anon_workspace.py:113)

## 2. Cause — a fixture defect that reached an ancestor repository

`tsg-map-integration/cleanup.sh` deletes every file under the run directory not in its
manifest. Its exclusion list omitted `.git`; p1, p4 and doclink all exclude it. On a map run
it deleted `.git/HEAD` and `.git/config`, leaving a headless `.git`.

Git then **discovered an ancestor repository** from that directory, so:

- `ANON_AUTOCOMMIT` committed six benchmark artifacts into the **setup repository**
  (`dfc2b43`, since undone with a mixed reset; files remain on disk untracked);
- the anon mirror was built from the ancestor's `ls-files` — empty, because run dirs are
  ignored there — so the baseline commit failed and crashed `run-build`.

It surfaced only now because map arm C had never previously escalated.

## 3. Pipeline hardening — `5d2afa7`, independent of any experiment

Both mutation boundaries assert git's top-level is **exactly** the intended project root
before any add, commit or mirror operation, and fail closed otherwise. "Inside a work tree"
is not "is the work tree". Two regression tests build an outer repo containing a headless
child, confirm git really discovers the ancestor, then assert the mirror raises and the
ancestor's commit count is unchanged.

## 4. Corrected map fixture — `3240e31`

One line, matching the form p1 already uses:

    +    -not -path '*/.git/*' \

Deliberately nothing else: exclusion syntax left un-normalised, no template refactor, and no
change to contents, handover, manifest, model inputs or cleanup semantics beyond preserving
the per-run repository.

Validated on the real failure path, inside the setup repo where ancestor discovery is
possible: after cleanup `HEAD` survives, top-level still resolves to the run directory, and
the anon mirror builds with 6 scrubbed files. Cleanup still deletes unspecced files.

## 5. Audit — separate finding, no fixes batched

    fixtures with cleanup.sh      4 of 8
    explicitly preserve .git      4 of 4 post-fix (3 of 4 before)
    can destroy the per-run repo  none post-fix; map was the only one
    other divergences             stylistic only — all four are self-locating, delete only
                                  within $ROOT, and only -type f. p1/p4 carry Git-Bash path
                                  normalisation the others lack; map/doclink add redundant
                                  bare .alpackages/.vscode paths.

**The defect was isolated to map.** No further fixture changes proposed or made.

## 6. Replacement scope — all 40 Arm C cells

4 fixtures x 10 repeats, fresh tag, so Arm C is internally coherent under one fixture
revision rather than mixing partial `routecon4` results with the corrected map.

Arms A and B from `routecon2` remain frozen and unchanged. Any integrity failure VOIDs the
replacement suite immediately.

## 7. PROVENANCE ASYMMETRY — must be stated in the final report

    map arms A/B    original frozen fixture revision  422c749
    map arm C       corrected revision                3240e31

`fixture_provenance` records the projects repo's HEAD, so **every replacement cell will label
`fixture_commit=3240e31`, including p1/p4/doclink**. Only map's cleanup script changed between
the two commits — p1, p4 and doclink content is byte-identical — but the label moves for all
four, and that must not be read as a content change.

**No pooled aggregate is reported.** Analysis stays per fixture x arm, as registered, with the
map A/B vs map C revision difference named plainly.
