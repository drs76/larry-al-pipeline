#!/usr/bin/env python3
"""SHADOW MODE. Prefix evaluation: given rounds 1..k, will local generation reach green?

This replaces the trace-level question ("is this trace a boundary?") with the one the
trigger actually has to answer at runtime, using only information available at round k.
It exists because the trace-level survey in capability-profile.py could not be validated:
labels there were almost perfectly confounded with fixture (doclink 104/109 BOUNDARY, p4
10/12 REPAIRABLE), so any feature correlating with "this is doclink" scored well.

The fix is not a better feature — it is a better evaluation. Two changes:

  1. Every trace contributes MANY prefixes, each with features computable at that moment
     and a label taken from what the trace eventually did. Fixture identity no longer
     determines the label on its own, because a single fixture supplies both early
     uncertain prefixes and their eventual outcome.

  2. Validation holds out ENTIRE FIXTURES, never random prefixes. Prefixes from one trace
     are highly correlated; a random split would leak and report a flattering number.
     Derive on doclink, test on p4/map, then reverse. A signal that survives both
     directions is not fixture identity.

Reported alongside accuracy is the OPERATIONAL error, which is what actually matters:
a trigger that escalates builds that would have repaired locally is worse than useless,
and one that fires only at the last round saves nothing.

NO THRESHOLD IS PROMOTED HERE. Shadow mode: nothing alters a build.
"""
import os
import re
import sys
from collections import Counter

BENCH = os.path.dirname(os.path.abspath(__file__))
LOGS = os.path.join(BENCH, "logs")

_ERR = re.compile(r"([^\s/]+\.al)\((\d+),(\d+)\): error ((?:AL|AW|PTE)\d+)")
_ROUND = re.compile(r"--- AL compile ---")
_IGNORE = {"PTE0004"}          # structural bookkeeping, not a capability signal


def rounds_from(path):
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


def fixture_of(name):
    for fx in ("doclink", "p4", "p1", "map", "f2"):
        if fx in name:
            return fx
    return "?"


def outcome(path):
    """LOCAL_GREEN only if the build reached green by local repair, with no fallback."""
    text = open(path, encoding="utf-8", errors="replace").read()
    passed = "BUILD: PASSED" in text
    fallback = "Bulk fallback:" in text
    if passed and not fallback:
        return "LOCAL_GREEN"
    if passed or "BUILD: FAILED" in text:
        return "NO_LOCAL_GREEN"
    return "CENSORED"


def prefixes(path):
    """One row per round k>=2 (persistence needs two rounds), features from rounds 1..k."""
    rounds = rounds_from(path)
    lab = outcome(path)
    if lab == "CENSORED" or len(rounds) < 2:
        return []
    text = open(path, encoding="utf-8", errors="replace").read()
    total = len(set(re.findall(r"([^\s/]+\.al)", text))) or 1

    rows = []
    for k in range(2, len(rounds) + 1):
        pre = rounds[:k]
        per_round_files = [set(f for f, _ in r) for r in pre]
        per_round_cls = [set(c for _, c in r) for r in pre]
        seen = Counter()
        for s in per_round_files:
            for f in s:
                seen[f] += 1
        persist = sum(1 for n in seen.values() if n >= 2)
        classes = len({c for s in per_round_cls for c in s})
        # Recurrence: how much the failing-file set repeats round on round.
        rec = []
        for i in range(len(per_round_files) - 1):
            a, b = per_round_files[i], per_round_files[i + 1]
            rec.append(len(a & b) / len(a | b) if (a | b) else 0.0)
        recur = sum(rec) / len(rec) if rec else 0.0
        delta = len(pre[-1]) - len(pre[-2])
        rows.append({
            "log": os.path.basename(path), "fixture": fixture_of(os.path.basename(path)),
            "k": k, "n_rounds": len(rounds), "label": lab,
            "persist": persist, "frac": persist / total, "classes": classes,
            "recur": recur, "delta": delta, "errors": len(pre[-1]),
        })
    return rows


def evaluate(rows, cut, feature="persist"):
    """Fire at the FIRST prefix where feature >= cut. One decision per trace."""
    by_trace = {}
    for r in rows:
        by_trace.setdefault(r["log"], []).append(r)
    fired_ok = fired_bad = missed = correct_hold = 0
    saved = []
    for log, rs in by_trace.items():
        rs.sort(key=lambda x: x["k"])
        lab = rs[0]["label"]
        hit = next((x for x in rs if x[feature] >= cut), None)
        if hit:
            if lab == "NO_LOCAL_GREEN":
                fired_ok += 1
                saved.append(hit["n_rounds"] - hit["k"])
            else:
                fired_bad += 1
        else:
            if lab == "NO_LOCAL_GREEN":
                missed += 1
            else:
                correct_hold += 1
    tot_bad = fired_ok + missed
    tot_good = fired_bad + correct_hold
    return {
        "cut": cut, "fired_ok": fired_ok, "fired_bad": fired_bad,
        "missed": missed, "held": correct_hold,
        "recall": fired_ok / tot_bad if tot_bad else float("nan"),
        "false_fire": fired_bad / tot_good if tot_good else float("nan"),
        "median_saved": sorted(saved)[len(saved) // 2] if saved else 0,
        "n_bad": tot_bad, "n_good": tot_good,
    }


def report(name, rows, feature="persist"):
    print(f"\n=== {name} ===")
    labs = Counter(r["label"] for r in {x["log"]: x for x in rows}.values())
    fixes = Counter(r["fixture"] for r in {x["log"]: x for x in rows}.values())
    print(f"  traces: {dict(labs)}   fixtures: {dict(fixes)}")
    if len(labs) < 2:
        print("  only one outcome class present — cannot evaluate separation here")
        return
    print(f"  {'cut':>4} {'fire-ok':>8} {'false-fire':>11} {'missed':>7} {'held':>5} "
          f"{'recall':>7} {'FFR':>6} {'med rounds saved':>17}")
    for cut in range(1, 8):
        e = evaluate(rows, cut, feature)
        print(f"  {cut:>4} {e['fired_ok']:>8} {e['fired_bad']:>11} {e['missed']:>7} "
              f"{e['held']:>5} {e['recall']:>7.2f} {e['false_fire']:>6.2f} "
              f"{e['median_saved']:>17}")


def main():
    rows = []
    for f in sorted(os.listdir(LOGS)):
        if f.endswith(".log"):
            rows += prefixes(os.path.join(LOGS, f))
    if not rows:
        print("no prefixes parsed")
        return 1

    traces = {r["log"] for r in rows}
    print(f"{len(rows)} prefix rows from {len(traces)} traces")

    feature = sys.argv[1] if len(sys.argv) > 1 else "persist"
    print(f"feature under test: {feature}")

    report("ALL FIXTURES POOLED (optimistic — fixture identity still available)",
           rows, feature)

    doclink = [r for r in rows if r["fixture"] == "doclink"]
    other = [r for r in rows if r["fixture"] != "doclink"]
    report("DERIVE on doclink", doclink, feature)
    report("TEST on non-doclink (p4 / p1 / map / f2)", other, feature)
    report("DERIVE on non-doclink", other, feature)
    report("TEST on doclink", doclink, feature)

    print("\n  A cutoff is only credible if it holds in BOTH held-out directions.")
    print("  Shadow mode: no threshold is promoted; nothing here alters a build.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
