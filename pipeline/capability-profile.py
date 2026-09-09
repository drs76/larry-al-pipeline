#!/usr/bin/env python3
"""SHADOW MODE. Does a build's compiler diagnostics look like a capability boundary?

Reads existing build logs, emits a profile plus a verdict, and changes NOTHING —
not ESCALATE_AFTER, not backend selection, not the egress gate. The point is to see
whether the observable features separate the known cases before any of this is allowed
to steer a build.

WHY A NEW SIGNAL
----------------
The escalation ladder in run-build.py fires on ESCALATE_AFTER=N *fix rounds elapsed*.
That counter cannot tell "three codeunits emitting 316 invented-member errors" from "one
file needs one more round". On doclink, qwen burned 21 ratchet attempts across 10 runs on
a profile that was diagnosable from the first two runs. This measures the profile instead.

The architectural split is deliberate:
  * the ladder      knows HOW to escalate, and whether policy permits it
  * this classifier decides WHETHER a failure pattern is worth escalating
  * egress_policy   remains authoritative on whether escalation may actually occur

DELIBERATELY NO THRESHOLDS YET
------------------------------
Breadth cutoffs, round counts and stability floors are hypotheses, not settings. This
prints the features for labelled known-positive and known-negative traces so the
thresholds can be read off the observed separation. A classifier validated only on
positives proves it fires, not that it discriminates.

Same-model negatives matter as much as the positives: if every positive were qwen and
every negative Claude, a "classifier" could score perfectly by learning model identity
and would then fire on every qwen build.

USAGE
    ./capability-profile.py                 # labelled survey over logs/
    ./capability-profile.py <logfile>...    # profile specific traces
"""
import os
import re
import sys
from collections import Counter

BENCH = os.path.dirname(os.path.abspath(__file__))
LOGS = os.path.join(BENCH, "logs")

_ERR = re.compile(r"([^\s/]+\.al)\((\d+),(\d+)\): error ((?:AL|AW|PTE)\d+)")
_ROUND = re.compile(r"--- AL compile ---")
# PTE0004 is structural bookkeeping (permission set written last by design), not a
# capability signal — counting it inflates breadth on every partial tree.
_IGNORE = {"PTE0004"}


def rounds_from(path):
    """Split a log into compile rounds; each round is a list of (file, class)."""
    out, cur = [], None
    with open(path, encoding="utf-8", errors="replace") as fh:
        for line in fh:
            if _ROUND.search(line):
                if cur is not None:
                    out.append(cur)
                cur = []
                continue
            if cur is None:
                continue
            m = _ERR.search(line)
            if m and m.group(4) not in _IGNORE:
                cur.append((os.path.basename(m.group(1)), m.group(4)))
    if cur is not None:
        out.append(cur)
    return [r for r in out if r]


def jaccard(a, b):
    if not a and not b:
        return 1.0
    return len(a & b) / len(a | b) if (a | b) else 1.0


def profile(path):
    rounds = rounds_from(path)
    if len(rounds) < 2:
        return None
    errs = [e for r in rounds for e in r]
    classes = Counter(c for _, c in errs)

    # PERSISTENT files, not "every file that ever emitted an error". This is the whole
    # distinction: the hard same-fixture negative touched 3 files with 12 errors but
    # repaired them, so a feature that counts transient failures would score it like a
    # boundary. A file counts only if it fails in 2+ SEPARATE rounds.
    per_round = [set(f for f, _ in r) for r in rounds]
    seen = Counter()
    for s in per_round:
        for f in s:
            seen[f] += 1
    persistent = {f for f, n in seen.items() if n >= 2}
    ever = set(seen)

    text = open(path, encoding="utf-8", errors="replace").read()
    passed = "BUILD: PASSED" in text
    fallback = "Bulk fallback:" in text

    # Normalise by project size so the feature cannot be a proxy for "which fixture".
    total = len(set(re.findall(r"([^\s/]+\.al)", text))) or len(ever) or 1

    return {
        "log": os.path.basename(path),
        "rounds": len(rounds), "errors": len(errs),
        "persist": len(persistent), "ever": len(ever),
        "frac": len(persistent) / total,
        "classes": len(classes),
        "passed": passed, "fallback": fallback,
        "top": ", ".join(f"{c}:{n}" for c, n in classes.most_common(3)),
    }


def ground_truth(p):
    """Label from OUTCOME only — never from the features being evaluated.

    REPAIRABLE  passed by local repair alone
    BOUNDARY    never resolved locally: failed outright, or passed only because the
                stall fallback wrote what the ratchet could not place
    """
    if p["passed"] and not p["fallback"]:
        return "REPAIRABLE"
    return "BOUNDARY"


# Labelled traces. POSITIVE = the known capability boundary (doclink blob codeunits, 0
# green in 21 attempts, closed only by changing model). NEGATIVE = builds that hit real
# compiler errors and then repaired to green — ordinary repairable failure, which must NOT
# trip the trigger. incrab2_challenger__r3 is held out: it PASSED, but only because the
# stall fallback wrote what the ratchet could not place, so its label is genuinely
# ambiguous and it should not be used to fit anything.
LABELS = [
    ("POSITIVE", "qwen3-coder_30b__doclink__incrab2_challenger__r1.log"),
    ("POSITIVE", "qwen3-coder_30b__doclink__incrab2_challenger__r6.log"),
    ("POSITIVE", "qwen3-coder_30b__doclink__incrab2_challenger__r9.log"),
    ("POSITIVE", "qwen3-coder_30b__doclink__incrab2_control__r2.log"),
    ("POSITIVE", "qwen3-coder_30b__doclink__incrab2_control__r7.log"),
    ("NEGATIVE", "qwen3-coder_30b__doclink__doclinkfix2_control__r8.log"),
    ("NEGATIVE", "qwen3-coder_30b__p4__trigctl_control__r1.log"),
    ("NEGATIVE", "qwen3-coder_30b__p4__brain_challenger__r3.log"),
    ("NEGATIVE", "qwen3-coder_30b__p4__brain_control__r1.log"),
    ("NEGATIVE", "qwen3-coder_30b__map__trigctl_control__r3.log"),
    ("NEGATIVE", "qwen3-coder_30b__p4__suite7_control__r1.log"),
    ("HELDOUT",  "qwen3-coder_30b__doclink__incrab2_challenger__r3.log"),
]

HDR = (f"{'label':<11} {'rnds':>4} {'errs':>5} {'pers':>4} {'ever':>4} {'frac':>5} "
       f"{'cls':>4} {'fb':>3} {'pass':>4}  {'top classes':<26} log")


def main():
    paths = sys.argv[1:] or sorted(
        os.path.join(LOGS, f) for f in os.listdir(LOGS) if f.endswith(".log"))
    groups, rows = {}, []
    for path in paths:
        p = profile(path)
        if not p:
            continue
        lab = ground_truth(p)
        p["fixture"] = ("doclink" if "doclink" in p["log"] else
                        p["log"].split("__")[1] if "__" in p["log"] else "?")
        groups.setdefault(lab, []).append(p)
        rows.append((lab, p))

    print(HDR)
    print("-" * 140)
    for lab, p in sorted(rows, key=lambda r: (r[0], -r[1]["persist"]))[:40]:
        print(f"{lab:<11} {p['rounds']:>4} {p['errors']:>5} {p['persist']:>4} {p['ever']:>4} "
              f"{p['frac']:>5.2f} {p['classes']:>4} {('y' if p['fallback'] else '-'):>3} "
              f"{('yes' if p['passed'] else 'no'):>4}  {p['top']:<26} {p['log']}")

    print()
    for lab, g in sorted(groups.items()):
        def rng(k):
            v = [x[k] for x in g]
            return f"{min(v):.2f}-{max(v):.2f}"
        print(f"  {lab:<11} n={len(g):<3} persist {rng('persist'):<12} frac {rng('frac'):<12} "
              f"classes {rng('classes')}")

    # Confound check: the feature must separate WITHIN a fixture, not just between them.
    print("\n  --- within-fixture check (separation must not be 'which fixture ran') ---")
    fixtures = sorted({p["fixture"] for _, p in rows})
    for fx in fixtures:
        by = {}
        for lab, p in rows:
            if p["fixture"] == fx:
                by.setdefault(lab, []).append(p["persist"])
        if len(by) > 1:
            desc = "  ".join(f"{l}: n={len(v)} persist {min(v)}-{max(v)}"
                             for l, v in sorted(by.items()))
            print(f"    {fx:<10} {desc}")
        else:
            l, v = next(iter(by.items()))
            print(f"    {fx:<10} {l} only (n={len(v)}, persist {min(v)}-{max(v)}) "
                  f"— cannot test separation here")

    # Candidate cutoff, reported not assumed.
    b = [x["persist"] for x in groups.get("BOUNDARY", [])]
    r = [x["persist"] for x in groups.get("REPAIRABLE", [])]
    if b and r:
        print(f"\n  persistent-file overlap: REPAIRABLE max {max(r)}, BOUNDARY min {min(b)}")
        for cut in range(1, 9):
            fp = sum(1 for v in r if v >= cut)
            fn = sum(1 for v in b if v < cut)
            print(f"    cut >={cut}: false-fire {fp}/{len(r)} REPAIRABLE, "
                  f"missed {fn}/{len(b)} BOUNDARY")
    print("\n  Shadow mode: nothing here alters a build.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
