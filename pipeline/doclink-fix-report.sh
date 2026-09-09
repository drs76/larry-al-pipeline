#!/usr/bin/env bash
# doclink-fix-report.sh — read the doclinkfix suite and say what it means.
#
# Two questions, answered separately:
#   1. Did correcting the handover move doclink off its 3/31 (9%) baseline?
#      -> the CONTROL arm answers this; it runs the unchanged pipeline.
#   2. Does proactive API grounding (AL_APIS=1) add anything on top?
#      -> control vs challenger, Fisher exact, because n=10 per arm can only
#         detect a large difference and a 3-run "win" has already reversed at
#         n=10 on this bench once.
set -uo pipefail
BENCH="$(cd "$(dirname "$0")" && pwd)"
TAG="${1:-doclinkfix}"

python3 - "$BENCH" "$TAG" <<'PY'
import sys, os, re, glob
from collections import Counter
bench, tag = sys.argv[1], sys.argv[2]

def arm_runs(arm):
    return sorted(glob.glob(f"{bench}/logs/*__{tag}_{arm}__r*.log"))

# The suite writes one authoritative "<name>: PASS|FAIL(n) in Ns" line per run.
# Trust that rather than re-deriving a verdict from log text, which is how a
# run gets miscounted.
_SUMMARY = {}
_sf = f"{bench}/{tag.upper()}-SUMMARY.log"
if os.path.exists(_sf):
    for line in open(_sf, encoding="utf-8", errors="replace"):
        m = re.match(r"\s*(\S+):\s+(PASS|FAIL)\b", line)
        if m:
            _SUMMARY[m.group(1)] = (m.group(2) == "PASS")

def verdict(path):
    return _SUMMARY.get(os.path.basename(path)[:-4], False)

def classes(paths, top=8):
    c = Counter()
    for p in paths:
        txt = open(p, encoding="utf-8", errors="replace").read()
        # Last compile only — earlier rounds are noise the fix loop already ate.
        tail = txt.rsplit("fix round", 1)[-1]
        for m in re.finditer(r"error ((?:AL|AW|PTE)\d+)", tail):
            c[m.group(1)] += 1
    return c.most_common(top)

def fisher(a, b, c, d):
    """Two-sided Fisher exact. No scipy on this box."""
    from math import comb
    n = a + b + c + d
    def p(x):
        return comb(a + b, x) * comb(c + d, a + c - x) / comb(n, a + c)
    obs = p(a)
    lo = max(0, a + c - (c + d)); hi = min(a + b, a + c)
    return sum(p(x) for x in range(lo, hi + 1) if p(x) <= obs * 1.0000001)

rows = {}
for arm in ("control", "challenger"):
    runs = arm_runs(arm)
    rows[arm] = (sum(verdict(r) for r in runs), len(runs), runs)

print(f"=== {tag} — doclink on the corrected handover ===\n")
for arm, (ok, tot, runs) in rows.items():
    env = "AL_APIS=1" if arm == "challenger" else "plain pipeline"
    pct = f"{100*ok/tot:.0f}%" if tot else "n/a"
    print(f"  {arm:11s} ({env:14s}): {ok}/{tot} pass  {pct}")

co, ct, _ = rows["control"]; ch, cht, _ = rows["challenger"]
print(f"\n  baseline before the handover fix: 3/31 pass (9%)")
if ct:
    print(f"  handover fix alone:  3/31 -> {co}/{ct}   Fisher p = {fisher(co, ct-co, 3, 28):.3f}")
if ct and cht:
    print(f"  API grounding on top: {co}/{ct} -> {ch}/{cht}   Fisher p = {fisher(ch, cht-ch, co, ct-co):.3f}")

print("\n=== remaining error classes (final compile of each run) ===")
for arm, (_, _, runs) in rows.items():
    print(f"\n  {arm}:")
    for code, n in classes(runs):
        print(f"    {code:8s} {n}")
print("\n  AL0185 absent = the namespace/using class is fixed.")
print("  AL0132 dominant = the model invents members on objects it now resolves correctly;")
print("  that is what the challenger arm's signature injection targets.")
PY
