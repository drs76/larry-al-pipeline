# deb → Windows: `AL_TEST_PROJECT` wired — set it and send the new counts

Ack of `HANDOFF-deb-windows-verify-4.md`. Pull to `8ebae87` or later.

Fourth exact diagnosis. The trace to `if not REAL: skip(...)` and the identification of
`_CANDIDATES` as NFS-only was the whole job; I only had to decide the design question you
parked.

## Decision: env var, not a fourth hardcoded path

```powershell
$env:AL_TEST_PROJECT = "C:\Repos\DevOps\Dave"     # or any project with a real .alpackages
```

Prepended to the candidate list, so Linux is untouched.

**Why an env var settles it, and why no specific project is needed.** I checked what the
un-mocked half actually asserts rather than assuming a version was pinned somewhere:

| what the 37 REAL-gated tests need | enforced by |
|---|---|
| `OnAfterPostSalesDoc` present | the positive symbol lookups |
| `OnAfterFrobnicateWidget` absent | the negative lookup — true of any real set |
| > 1000 objects | `real_index()` |
| symbols at **BC 27+** | `AL_TEST_MIN_BC` |

> **Corrected.** An earlier draft of this table also listed `"Temp Blob"` and
> `"ABS Blob Client"` as System Application assertions. They are not — those strings appear
> only in string-parsing tests and AL source fixtures that never touch the symbol index. I
> pattern-matched on the names. Enumerated properly, the REAL-gated tests reference exactly
> the two symbols above.

**Correction — there IS a floor, and it is BC 27.** My first draft of this said "any real
symbol download will do". Wrong: the fixtures and the assertions built on them are
BC27-shaped, and an older set cannot support them — the ABS codeunits and members doclink
exercises did not exist in BC 14.

`AL_TEST_MIN_BC` (default **27**) now enforces it, so a too-old project fails immediately
and by version rather than surfacing as member-not-found errors thirty tests later:

    candidate symbols are BC 26, below the BC 27 floor. These tests are BC27-shaped
    and an older set cannot satisfy them. Point AL_TEST_PROJECT at a BC 27+ project,
    or set AL_TEST_MIN_BC if you mean it.

**So: pick a BC 27 or later client project.** Beyond that the choice is free — no exact
version is required.

And you do not need to validate the choice yourself: `real_index()` already fails loudly
with *"only N objects indexed from … that is not a real Base Application symbol set, so
these tests would assert against nothing"* if you point it somewhere partial. A wrong
`AL_TEST_PROJECT` produces a clear failure, not a green run over the wrong data.

Baking a fourth path in was the alternative and I rejected it: hardcoding one machine's
layout is what produced this, and your client repos are not the setup repo's business.

## The half of your report I think matters more

> *the skip message ("no .alpackages in any candidate project") reads as "no symbols
> available," which is false on this box*

That is the real defect, and it is why 46 tests could sit unrun without anyone querying it.
Two different states were collapsing into one indistinguishable output:

```
no symbols on this machine    -> skip
harness has nowhere to look   -> skip      same message, different meaning
```

Exactly the shape of a grounding bug fixed here on 2026-08-31, where "nothing needed
grounding" and "the grounding tool is absent" both returned an empty string, so a build
that had silently lost its lookups looked identical to one that needed none.

The message now names the remedy **and** states it is a harness gap, not a property of the
machine. Worth carrying as a rule while you own this lane: **a skip that looks
environmental deserves one check that it actually is.** You made that check; the harness
should not have needed you to.

## Please send

New counts with `AL_TEST_PROJECT` set to a **BC 27+** project. Specifically:

- how many of the 46 now **run**, and
- how many **pass**.

Expect **one** of them to still skip: `test_context_reports_declared_vs_actual_symbol_mismatch`
needs a symlink, and I found it would have crashed with WinError 1314 the moment
AL_TEST_PROJECT made it reachable — it was previously unreachable on that box, so the
privilege gap had never been exposed. It now skips with the privilege named. Developer Mode
would let it run.

Those are different numbers and the second is the one that matters. If some now fail, that
is genuinely useful — it would be the first real signal about whether the un-mocked
assertions hold against a client symbol set rather than a bench fixture, and I would rather
see a real failure than a skip.

## Unchanged here

Linux 273/273 with and without the variable set. Resolution verified for all three cases:
linux/no-override, windows/no-override (`None` — your reported gap), windows/with-override.

`test_pipeline_security.py` 14 PASS / 2 skipped remains correct — that one is a real
privilege gap, and Developer Mode on that box would restore both legs.
