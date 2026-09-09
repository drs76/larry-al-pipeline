#!/usr/bin/env python3
"""SHADOW MODE. Does a prefix-observable trigger predict a BROAD capability boundary?

This supersedes the pooled evaluation in capability-prefix.py, which could not be trusted:
its NO_LOCAL_GREEN label conflated two operationally different states, so a breadth-based
trigger was scored as "missing" every narrow failure it correctly declined to fire on.

TARGET (terminal evidence — information the trigger never sees)
--------------------------------------------------------------
  LOCAL_GREEN      reached green by local repair, no fallback
  NARROW_STALL     exhausted locally, <=2 distinct files failing in the FINAL round
  BROAD_BOUNDARY   exhausted locally, >=3 distinct files failing in the FINAL round
  NOT_WRITTEN      write path failed — invalid for capability classification, excluded
  CENSORED         cannot establish either — excluded

The label is computed at the END of the repair budget; the trigger sees only rounds 1..k.
Different observable, separated in time, so `persist >= N` cannot be baked into its own
target. Defining BROAD_BOUNDARY as "persist >= 3" and then reporting persist >= 3 as
predictive would be circular — this deliberately does not do that.

ONLY BROAD_BOUNDARY IS A POSITIVE. Narrow stalls are negatives: escalating a whole build
because one artifact will not compile is the wrong action, and a trigger that declines
there is behaving correctly, not missing.

VALIDATION
----------
Leave-one-fixture-out across p1/p4/map, because prefixes from one trace are highly
correlated and a random split would leak. doclink is held OUT of fitting entirely and
reported as an external stress case: its 100+ traces would otherwise dominate every
average and reintroduce the fixture confound the ndb1 suite was run to break.

METRICS
-------
  safety   false-fire rate, reported SEPARATELY for LOCAL_GREEN and NARROW_STALL
  utility  median rounds saved on BROAD_BOUNDARY traces that fire
  recall   on BROAD_BOUNDARY only, never pooled with narrow stalls

No threshold is promoted. Nothing here alters a build.
"""
import os
import re
import sys
from collections import Counter

BENCH = os.path.dirname(os.path.abspath(__file__))
LOGS = os.path.join(BENCH, "logs")

_ERR = re.compile(r"([^\s/]+\.al)\((\d+),(\d+)\): error ((?:AL|AW|PTE)\d+)")
_ROUND = re.compile(r"--- AL compile ---")
_IGNORE = {"PTE0004"}
FIXTURES = ("doclink", "p1", "p4", "map", "f2")


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
            cur.append((os.path.basename(m.group(1)), m.group(4)))
    if cur is not None:
        out.append(cur)
    return [r for r in out if r]


def fixture_of(name):
    for fx in FIXTURES:
        if fx in name:
            return fx
    return "?"


def trace(path):
    text = open(path, encoding="utf-8", errors="replace").read()
    if "NOT WRITTEN" in text or re.search(r"Wrote 0/\d+", text):
        return None
    rounds = rounds_of(path)
    passed = "BUILD: PASSED" in text
    fallback = "Bulk fallback:" in text
    if passed and not fallback:
        label = "LOCAL_GREEN"
    elif not rounds:
        return None                      # censored
    else:
        term = len({f for f, _ in rounds[-1]})
        label = "BROAD_BOUNDARY" if term >= 3 else "NARROW_STALL"
    if len(rounds) < 2:
        return None                      # no prefix can be formed
    return {"log": os.path.basename(path), "fixture": fixture_of(os.path.basename(path)),
            "label": label, "rounds": rounds, "n": len(rounds)}


def fires_at(t, cut):
    """First round k>=2 where >=cut files have failed in 2+ separate rounds of 1..k."""
    seen = Counter()
    per_round = [{f for f, _ in r} for r in t["rounds"]]
    for k in range(len(per_round)):
        for f in per_round[k]:
            seen[f] += 1
        if k + 1 >= 2:
            persist = sum(1 for v in seen.values() if v >= 2)
            if persist >= cut:
                return k + 1
    return None


def evaluate(traces, cut):
    res = {"broad_fired": 0, "broad_missed": 0, "saved": [],
           "narrow_fired": 0, "narrow_held": 0,
           "green_fired": 0, "green_held": 0}
    for t in traces:
        k = fires_at(t, cut)
        if t["label"] == "BROAD_BOUNDARY":
            if k:
                res["broad_fired"] += 1
                res["saved"].append(t["n"] - k)
            else:
                res["broad_missed"] += 1
        elif t["label"] == "NARROW_STALL":
            res["narrow_fired" if k else "narrow_held"] += 1
        else:
            res["green_fired" if k else "green_held"] += 1
    b = res["broad_fired"] + res["broad_missed"]
    nn = res["narrow_fired"] + res["narrow_held"]
    gg = res["green_fired"] + res["green_held"]
    res["recall"] = res["broad_fired"] / b if b else float("nan")
    res["ff_narrow"] = res["narrow_fired"] / nn if nn else float("nan")
    res["ff_green"] = res["green_fired"] / gg if gg else float("nan")
    s = sorted(res["saved"])
    res["med_saved"] = s[len(s) // 2] if s else 0
    res["n_broad"], res["n_narrow"], res["n_green"] = b, nn, gg
    return res


def table(title, traces, cuts=range(1, 7)):
    print(f"\n=== {title} ===")
    c = Counter(t["label"] for t in traces)
    fx = Counter(t["fixture"] for t in traces)
    print(f"  traces: {dict(c)}")
    print(f"  fixtures: {dict(fx)}")
    if not c.get("BROAD_BOUNDARY"):
        print("  no BROAD_BOUNDARY traces here — recall undefined, safety only")
    print(f"  {'cut':>4} {'recall(broad)':>14} {'FF narrow':>10} {'FF green':>9} "
          f"{'med saved':>10}   n_broad/n_narrow/n_green")
    for cut in cuts:
        e = evaluate(traces, cut)
        print(f"  {cut:>4} {e['recall']:>14.2f} {e['ff_narrow']:>10.2f} "
              f"{e['ff_green']:>9.2f} {e['med_saved']:>10}   "
              f"{e['n_broad']}/{e['n_narrow']}/{e['n_green']}")


def main():
    traces = []
    for f in sorted(os.listdir(LOGS)):
        if f.endswith(".log"):
            t = trace(os.path.join(LOGS, f))
            if t:
                traces.append(t)

    bench = [t for t in traces if t["fixture"] in ("p1", "p4", "map")]
    doclink = [t for t in traces if t["fixture"] == "doclink"]
    print(f"{len(traces)} usable traces  |  fitting pool (p1/p4/map): {len(bench)}  |  "
          f"external stress (doclink): {len(doclink)}")

    table("POOLED p1/p4/map (optimistic — fixture identity available)", bench)

    for held in ("p1", "p4", "map"):
        tr = [t for t in bench if t["fixture"] != held]
        te = [t for t in bench if t["fixture"] == held]
        if te:
            table(f"LEAVE-ONE-OUT: derive on {'/'.join(x for x in ('p1','p4','map') if x != held)}"
                  f" -> TEST on {held}", te)

    table("EXTERNAL STRESS: doclink (never used for fitting)", doclink)

    print("\n  Positives are BROAD_BOUNDARY only. Narrow stalls are negatives: declining")
    print("  to fire on them is correct behaviour, not a miss.")
    print("  Shadow mode: no threshold promoted, nothing here alters a build.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
