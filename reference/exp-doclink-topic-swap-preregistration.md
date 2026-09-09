# Pre-registration — did the topic swap move doclink off zero?

Written 2026-08-29, **before** any arm ran, after `injab`/`roundab` closed null.
Fixture: `tsg-document-link-2-az-storage`. Model: `ollama/qwen3-coder:30b`, both arms.
Egress local-only, escalation off, `MAX_FIX_ROUNDS=8`.

## The question

doclink passed 7 times across 40 runs today. Its documented pre-fix baseline is 0/40.
That is a cross-session comparison, not a controlled one — today's runs are all post-`253273c`
and other pipeline changes sit in between — so the fix is the most recent plausible cause
and nothing more. This suite makes it controlled.

## Why arms differ by topic list, not by code version

The obvious design is old-code vs new-code. It is the worse one: `253273c` also changed
docstrings, tiering and logging, so a code-version arm confounds the topic change with
everything else on the branch.

The fix's ENTIRE effect on doclink is which topics reach the prompt:

| | injected |
|---|---|
| pre-fix | 00-gotchas, 01-syntax-style, 02-objects, **07-events-errors** |
| post-fix | 00-gotchas, 01-syntax-style, 02-objects, **08-data-storage** |

Both verified empirically against `git show HEAD~n:pipeline/run-build.py` and the live
selector. `INJECT_TOPICS` takes an explicit comma-separated list that bypasses `select_topics`
and the budget entirely, so one codebase can produce both prompts exactly. `INJECT_TOPICS` is
in the 61-var derived clear-list, so the arms are isolated on the knob under test.

This tests the causal claim that matters — the topic set moved doclink — and not the
irrelevant one about a diff's incidental contents.

## Primary metric — declared before the fact

**Pass rate, Fisher exact, two-tailed.**

This is a deliberate change from the previous pre-registration, which declared best error
score and explicitly ruled pass rate out. The justification then was that doclink was
floor-bound at 0/40, making pass rate non-discriminating. That premise no longer holds: the
pooled control across `injab`+`roundab` is 2/20, so pass rate now varies and can discriminate.
Error score, meanwhile, was dead null across both suites (U=50.0 and U=51.5) and did not track
the passes — a run scoring 1 and a run scoring 0 are different outcomes that the score barely
separates.

Recording the reversal explicitly because switching to the metric that previously "looked
better" is exactly the move that needs justifying in advance rather than after.

Secondary, recorded not tested: best error score, error-class histogram (does `AL0173`/`AL0151`
go to zero in the challenger and not the control — the mechanism the pilot suggested), wall time.

## Arms

| arm | INJECT_TOPICS |
|---|---|
| control | `00-gotchas,01-syntax-style,02-objects,07-events-errors` |
| challenger | `00-gotchas,01-syntax-style,02-objects,08-data-storage` |

n=20 per arm, interleaved in one session.

## Power, stated honestly

Prior is control ≈10% (2/20). If the challenger is ~35%, n=20/arm gives roughly 70% power at
α=0.05. That is adequate for a large effect and **not** adequate for a modest one. A null here
will be reported as underpowered rather than as a refutation, and n will not be extended after
the fact — the stopping rule is n=20 per arm, fixed here.

## What would change practice

- Challenger wins → the injection fix causally moved doclink off zero. The standing guidance
  in `project_incremental_ratchet` to route ABS-heavy AL to escalation needs revisiting, and
  `project_doc_link_az_storage`'s "constraint is the all-at-once write shape" is at least
  partly wrong: it was measured with `08-data-storage` silently absent.
- Null → the 7/40 is not attributable to the topic swap. `253273c` stays committed on its own
  merits (p1 injection 13.56k → 9.33k at identical build outcome, and the eviction is no
  longer silent), and the doclink conclusions stand as written.
