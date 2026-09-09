#!/usr/bin/env python3
"""Did the ratchet converge, churn, or just hand the job to the fallback?

Pass rate alone cannot tell those apart. A run ending 8-green after three sweeps and one
ending 2-green with six files dumped into the bulk fallback both read as one row in the
suite summary, but only the first means the ratchet earned its complexity — the second is
the single-shot path wearing a hat.

Reads the metrics JSONL (aggregate per run) and the suite logs (per-file history, which
the metrics deliberately do not carry).
"""
import json
import os
import re
import sys
from collections import Counter, defaultdict

BENCH = os.path.dirname(os.path.abspath(__file__))
TAG = sys.argv[1] if len(sys.argv) > 1 else "incrab"
METRICS = os.environ.get("BUILD_METRICS",
                         os.path.join(BENCH, ".build-metrics.jsonl"))

# --- aggregate, from metrics -------------------------------------------------
rows = []
if os.path.exists(METRICS):
    for line in open(METRICS, encoding="utf-8", errors="replace"):
        try:
            r = json.loads(line)
        except ValueError:
            continue
        # Tag-filter too: the smoke runs also wrote workflow=incremental rows, and
        # mixing them into a suite's aggregate silently corrupts it. "project" is the
        # run-dir basename, e.g. qwen3-coder_30b__doclink__incrab_challenger__r1.
        if (r.get("workflow") == "incremental"
                and r.get("incr_green") is not None
                and f"{TAG}_challenger" in (r.get("project") or "")):
            rows.append(r)

print(f"=== {TAG}: ratchet convergence ===\n")
if not rows:
    print("  no incremental metrics rows yet\n")
else:
    for r in rows[-10:]:
        g, left = r.get("incr_green", 0), r.get("incr_left", 0)
        tot = g + left
        print(f"  green {g}/{tot}  left→fallback {left}  "
              f"sweeps {r.get('incr_sweeps')}  defer {r.get('incr_deferred')}  "
              f"revert {r.get('incr_reverted')}  "
              f"{'STALLED ' if r.get('incr_stalled') else ''}"
              f"{'FALLBACK' if r.get('incr_stall_fallback') else ''}")
    n = len(rows)
    tg = sum(r.get("incr_green", 0) for r in rows)
    tl = sum(r.get("incr_left", 0) for r in rows)
    print(f"\n  {n} run(s): {tg} file(s) placed by the ratchet, {tl} handed to the fallback"
          f"  ({100 * tg / max(1, tg + tl):.0f}% placed)")
    print(f"  stalled in {sum(1 for r in rows if r.get('incr_stalled'))}/{n} run(s); "
          f"fallback used in {sum(1 for r in rows if r.get('incr_stall_fallback'))}/{n}")

    # THE VALIDITY GATE. A false success claim that a retry repaired still leaves the
    # run interpretable as an architecture test. One that exhausted every attempt means
    # the ratchet never ran, and the arm is confounded exactly as incrab was.
    exhausted = sum(r.get("incr_write_failed", 0) for r in rows)
    recovered = sum(r.get("incr_write_recovered", 0) for r in rows)
    retries = sum(r.get("incr_write_retries", 0) for r in rows)
    runs_exhausted = sum(1 for r in rows if r.get("incr_write_failed", 0))
    print(f"\n  write integrity: {recovered} recovered after retry, "
          f"{exhausted} never written ({runs_exhausted}/{n} run(s) affected), "
          f"{retries} wasted attempt(s)")
    if exhausted:
        print("  ⚠ VERDICT: challenger is CONFOUNDED — files never got written, so the "
              "ratchet\n    was not exercised. The architectural question stays open.")
    elif recovered:
        print("  ✓ VERDICT: interpretable. The model still claimed false successes, but "
              "every one\n    was repaired by the retry, so the ratchet ran as intended.")
    else:
        print("  ✓ VERDICT: interpretable, and no false success claims occurred at all.")

# --- per-file history, from the logs ----------------------------------------
# A file reverting in every sweep (the model cannot write it) is a different diagnosis
# from three different files reverting once each (ordering/dependency).
VERDICT = re.compile(r"^\s+(\S+\.al): (GREEN|DEFER|REVERT|NOT WRITTEN)")
per_file = defaultdict(Counter)
logdir = os.path.join(BENCH, "logs")
if os.path.isdir(logdir):
    for fn in sorted(os.listdir(logdir)):
        if f"__{TAG}_challenger__" not in fn or not fn.endswith(".log"):
            continue
        for line in open(os.path.join(logdir, fn), encoding="utf-8", errors="replace"):
            m = VERDICT.match(line)
            if m:
                per_file[m.group(1)][m.group(2)] += 1

if per_file:
    print("\n=== per-file verdicts (verdict EVENTS, not runs — a file judged in\n    three sweeps contributes three) ===\n")
    width = max(len(f) for f in per_file)
    for f in sorted(per_file, key=lambda x: -per_file[x]["REVERT"]):
        c = per_file[f]
        print(f"  {f:<{width}}  green {c['GREEN']:3d}  defer {c['DEFER']:3d}  "
              f"revert {c['REVERT']:3d}  unwritten {c['NOT WRITTEN']:3d}")
    print("\n  A file that is almost never green is a file the model cannot write from "
          "this handover;\n  one that defers a lot but eventually goes green is only an "
          "ordering cost.")
