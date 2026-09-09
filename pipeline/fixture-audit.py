#!/usr/bin/env python3
"""Round-1 error signatures across a suite — the handover-audit trigger.

THE RULE THIS IMPLEMENTS
------------------------
A deterministic round-1 compiler error recurring across nearly all runs is a
handover-audit trigger, EVEN WHEN TERMINAL PASS RATE IS 100%.

Found twice in one session, presenting completely differently both times:

  p1 v1  the handover required an enum inside the table file while the manifest listed
         five files and forbade extras. Every model dropped the enum and stalled. Visible
         as terminal failure.
  p4 v2  the handover stated "On validating End Time..." in a bullet detached from the
         field, never saying where the trigger goes. Every run wrote a table-level
         `OnValidateField` (not an AL trigger) and burned a repair round on AL0162.
         Final pass was 20/20 — the fix loop always recovered — so pass rate showed
         NOTHING. Only first-pass rate (0/20) exposed it.

Terminal pass rate is blind to this class. Round-1 signatures are not.

THE RULE, as promoted after p4 v3 confirmed the diagnosis:

    If a round-1 compiler error signature occurs at near-universal frequency, AUDIT THE
    HANDOVER before interpreting repair depth or first-pass performance.

p4 v3 is the confirmation: binding the requirement to its field took AL0162 from 20/20 to
0/20, clean round-1 compile from 0/20 to 16/20, and median duration from 114s to 77s, with
no replacement signature.

COMPILE SIGNATURES ARE REPORTED INDEPENDENTLY OF MANIFEST FAILURES, deliberately. The
metrics field `first_pass_compile` is `build_ok AND NOT manifest_fail`, and that
conflation produced two misleading readings: p1 looked like 15/20 first-pass "generation
quality" when round 1 actually compiled clean 20/20 and the five repairs were omitted
`app.json` files. Keeping the layers separate is what exposed both defects.

WHAT IT REPORTS
---------------
Per (file, error-code) signature, the number of RUNS it appears in — not the raw error
count, which one run repeating an error can dominate. Then a classification:

  spec-trap        >=80% of runs. Deterministic. AUTOMATIC handover-audit trigger.
  dominant         >=40% AND >=3x the next distinct signature. MANUAL audit trigger — a
                   coherent shared cause is likely but not proven; go and look.
  common           >=40% without that dominance. Worth reading; may be construction
                   difficulty rather than a defect.
  variance         <40%. Ordinary generation noise.

The two-band split exists because an 80%-only rule MISSED a real defect. doclink showed
AL0162 at 12/20 (60%) — models placing named events as `trigger`s in a tableextension
because the handover said "subscribe to X on table 1173" and never showed the
`[EventSubscriber]` construct. Same "requirement detached from its AL construct" pattern
as p1 and p4, but it printed no audit prompt at 60%. A single-threshold rule fitted to
p4's 100% case was too blunt.

The dominance test (>=3x the next signature) is what keeps this from flagging every
recurring 10-20% error as a fixture defect.

Outcomes are split into clean-first-pass / repaired / exhausted rather than pooled,
because "18 clean first passes, 1 repaired, 1 exhausted" is a far healthier fixture than
"20 repaired", even though the second has the better terminal pass rate.

USAGE
    ./fixture-audit.py <suite-tag> [more-tags...]
"""
import os
import re
import sys
from collections import Counter, defaultdict

BENCH = os.path.dirname(os.path.abspath(__file__))
LOGS = os.path.join(BENCH, "logs")

_ERR = re.compile(r"([^\s/]+\.al)\((\d+),(\d+)\): error ((?:AL|AW|PTE)\d+): (.*)")
_ROUND = re.compile(r"--- AL compile ---")
# Structural bookkeeping, not a model signal: the permission set is written last by
# design, so a partial tree always reports it.
_IGNORE = {"PTE0004"}

SPEC_TRAP, COMMON = 0.80, 0.40
DOMINANCE = 3.0        # x the next distinct signature, for the `dominant` band


def rounds_of(path):
    out, cur = [], None
    for line in open(path, encoding="utf-8", errors="replace"):
        if _ROUND.search(line):
            if cur is not None:
                out.append(cur)
            cur = []
            continue
        if cur is None:
            continue
        m = _ERR.search(line)
        if m and m.group(4) not in _IGNORE:
            cur.append((m.group(1), m.group(4), m.group(5).strip()))
    if cur is not None:
        out.append(cur)
    return out


def audit(tag):
    logs = sorted(f for f in os.listdir(LOGS) if tag in f and f.endswith(".log"))
    if not logs:
        print(f"no logs for tag '{tag}'")
        return
    print(f"\n=== {tag}: {len(logs)} run(s) ===")

    sig_runs, msg_of = Counter(), {}
    later_runs = Counter()
    clean = repaired = exhausted = 0
    n_rounds = []

    for lg in logs:
        text = open(os.path.join(LOGS, lg), encoding="utf-8", errors="replace").read()
        blocks = rounds_of(os.path.join(LOGS, lg))
        nonempty = [b for b in blocks if b]
        n_rounds.append(len(blocks))

        # Outcome, kept separate on purpose.
        passed = "BUILD: PASSED" in text
        r1_clean = bool(blocks) and not blocks[0]
        if passed and r1_clean:
            clean += 1
        elif passed:
            repaired += 1
        else:
            exhausted += 1

        if blocks and blocks[0]:
            for f, c in {(f, c) for f, c, _ in blocks[0]}:
                sig_runs[(f, c)] += 1
            for f, c, m in blocks[0]:
                msg_of.setdefault((f, c), m)
        for b in blocks[1:]:
            for f, c in {(f, c) for f, c, _ in b}:
                later_runs[(f, c)] += 1

    n = len(logs)
    print(f"  outcomes: clean-first-pass {clean}/{n}   repaired {repaired}/{n}   "
          f"exhausted {exhausted}/{n}")
    print(f"  compile rounds: min {min(n_rounds)} max {max(n_rounds)}")

    if not sig_runs:
        print("\n  ROUND 1 CLEAN IN EVERY RUN — no signatures to audit.")
        return

    ranked = sig_runs.most_common()
    second = ranked[1][1] if len(ranked) > 1 else 0

    def classify(runs, rank):
        frac = runs / n
        if frac >= SPEC_TRAP:
            return "spec-trap"
        if frac >= COMMON and rank == 0 and runs >= DOMINANCE * max(second, 1):
            return "dominant"
        return "common" if frac >= COMMON else "variance"

    print(f"\n  {'runs':>6}  {'%':>5}  {'class':<10} {'file':<34} code")
    for rank, ((f, c), runs) in enumerate(ranked):
        print(f"  {runs:>3}/{n:<2}  {runs/n:>4.0%}  {classify(runs, rank):<10} {f:<34} {c}")

    traps = [(k, v) for rank, (k, v) in enumerate(ranked)
             if classify(v, rank) in ("spec-trap", "dominant")]
    print()
    if traps:
        print("  ** HANDOVER AUDIT INDICATED ** — deterministic or dominant signature(s):")
        for (f, c), runs in sorted(traps, key=lambda x: -x[1]):
            print(f"     {runs}/{n} runs  {f}  {c}")
            print(f"       {msg_of.get((f, c), '')[:110]}")
            still = later_runs.get((f, c), 0)
            print(f"       recurs after round 1 in {still}/{n} run(s)")
        print("\n     Audit the handover BEFORE reading pass rate. A fix loop that always")
        print("     recovers hides this completely in the terminal result.")
    else:
        print("  No deterministic round-1 signature (none >=80% of runs).")
        print("  Remaining errors look like construction difficulty or generation variance.")


def main():
    tags = sys.argv[1:]
    if not tags:
        print(__doc__.strip().splitlines()[-1])
        return 1
    for t in tags:
        audit(t)
    return 0


if __name__ == "__main__":
    sys.exit(main())
