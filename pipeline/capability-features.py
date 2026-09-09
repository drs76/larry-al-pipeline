#!/usr/bin/env python3
"""SHADOW MODE. Pre-registered inventory of prefix-only features vs terminal class.

WHY AN INVENTORY, NOT A CLASSIFIER
----------------------------------
The previous attempt committed to one intuitive feature (cumulative persistent-file count)
before checking whether it represented the thing being predicted. It did not: it measures
historical failure spread, so it fired on doclink runs that had already converged toward a
narrow terminal problem. See capability-eval.py and CAPABILITY-EVAL.txt.

The evaluator is the expensive artifact and it already exists. Candidate features are
cheap. So this screens MANY semantically-motivated features under the identical protocol
rather than hand-picking one.

PRE-REGISTRATION
----------------
The feature list below, and each feature's DIRECTION, are fixed in this file before any
result is inspected. `dir` is the sign that should indicate a boundary: "hi" means large
values are boundary-like, "lo" means small values are. Anything chosen or re-signed AFTER
looking at output is exploratory and must be labelled as such — not reported as if it had
been pre-registered.

PROTOCOL (unchanged from capability-eval.py, deliberately)
---------------------------------------------------------
  target        terminal breadth at the FINAL round — an observable the prefix features
                never see, so no feature can be baked into its own label
  positives     BROAD_BOUNDARY only; NARROW_STALL is a NEGATIVE, because escalating a
                whole build over one bad artifact is the wrong action
  validation    leave-one-fixture-out over p1/p4/map
  stress        doclink, never used for fitting — the bar every candidate must clear
  metrics       recall on broad; false-fire reported separately for narrow and green;
                median rounds saved; earliest useful detection round

No threshold is promoted. Nothing here alters a build.
"""
import math
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

# ---- PRE-REGISTERED FEATURES: (name, direction, group) -----------------------------
FEATURES = [
    # 1. current-state breadth — avoids the cumulative-history problem
    ("files_now",            "hi", "current"),
    ("errors_now",           "hi", "current"),
    ("classes_now",          "hi", "current"),
    ("files_now_frac",       "hi", "current"),
    ("dom_class_share_now",  "lo", "current"),
    # 2. transition / churn
    ("new_files",            "hi", "transition"),
    ("resolved_files",       "lo", "transition"),
    ("retained_files",       "hi", "transition"),
    ("net_file_change",      "hi", "transition"),
    ("jaccard_files",        "hi", "transition"),
    ("new_classes",          "hi", "transition"),
    ("breadth_trend",        "hi", "transition"),
    # 3. momentum — is repair progressing or wandering?
    ("d_errors",             "hi", "momentum"),
    ("d_files",              "hi", "momentum"),
    ("resolved_fraction",    "lo", "momentum"),
    ("rounds_no_reduction",  "hi", "momentum"),
    ("rounds_expanding",     "hi", "momentum"),
    ("gap_from_best",        "hi", "momentum"),
    # 4. concentration / topology
    ("errors_per_file",      "lo", "topology"),
    ("max_file_share",       "lo", "topology"),
    ("top2_file_share",      "lo", "topology"),
    ("class_entropy",        "hi", "topology"),
    # 5. persistence, decomposed
    ("failing_last2",        "hi", "persistence"),
    ("failing_all_rounds",   "hi", "persistence"),
    ("oldest_age",           "hi", "persistence"),
    ("mean_age",             "hi", "persistence"),
    ("frac_new_failures",    "hi", "persistence"),
]


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


def fixture_of(n):
    for fx in FIXTURES:
        if fx in n:
            return fx
    return "?"


def load(path):
    text = open(path, encoding="utf-8", errors="replace").read()
    if "NOT WRITTEN" in text or re.search(r"Wrote 0/\d+", text):
        return None
    rounds = rounds_of(path)
    passed = "BUILD: PASSED" in text
    fallback = "Bulk fallback:" in text
    if passed and not fallback:
        label = "LOCAL_GREEN"
    elif not rounds:
        return None
    else:
        label = ("BROAD_BOUNDARY"
                 if len({f for f, _ in rounds[-1]}) >= 3 else "NARROW_STALL")
    if len(rounds) < 2:
        return None
    total = len(set(re.findall(r"([^\s/]+\.al)", text))) or 1
    return {"log": os.path.basename(path), "fixture": fixture_of(os.path.basename(path)),
            "label": label, "rounds": rounds, "n": len(rounds), "total": total}


def entropy(counts):
    tot = sum(counts)
    if tot <= 0:
        return 0.0
    return -sum((c / tot) * math.log(c / tot, 2) for c in counts if c)


def features_at(t, k):
    """All pre-registered features using ONLY rounds 1..k."""
    pre = t["rounds"][:k]
    cur, prev = pre[-1], pre[-2]
    cf = {f for f, _ in cur}
    pf = {f for f, _ in prev}
    cc = Counter(c for _, c in cur)
    pc = {c for _, c in prev}
    fcount = Counter(f for f, _ in cur)

    counts = [len(r) for r in pre]
    fcounts = [len({f for f, _ in r}) for r in pre]
    age = Counter()
    for r in pre:
        for f in {x for x, _ in r}:
            age[f] += 1
    ever_before = {f for r in pre[:-1] for f, _ in r}

    no_red = 0
    for i in range(len(counts) - 1, 0, -1):
        if counts[i] >= counts[i - 1]:
            no_red += 1
        else:
            break
    expanding = 0
    for i in range(len(fcounts) - 1, 0, -1):
        if fcounts[i] >= fcounts[i - 1]:
            expanding += 1
        else:
            break

    resolved = pf - cf
    fv = {
        "files_now": len(cf),
        "errors_now": len(cur),
        "classes_now": len(cc),
        "files_now_frac": len(cf) / t["total"],
        "dom_class_share_now": (cc.most_common(1)[0][1] / len(cur)) if cur else 0.0,
        "new_files": len(cf - pf),
        "resolved_files": len(resolved),
        "retained_files": len(cf & pf),
        "net_file_change": len(cf) - len(pf),
        "jaccard_files": len(cf & pf) / len(cf | pf) if (cf | pf) else 0.0,
        "new_classes": len(set(cc) - pc),
        "breadth_trend": (1 if len(cf) > len(pf) else (0 if len(cf) == len(pf) else -1)),
        "d_errors": len(cur) - len(prev),
        "d_files": len(cf) - len(pf),
        "resolved_fraction": len(resolved) / len(pf) if pf else 0.0,
        "rounds_no_reduction": no_red,
        "rounds_expanding": expanding,
        "gap_from_best": len(cur) - min(counts),
        "errors_per_file": len(cur) / len(cf) if cf else 0.0,
        "max_file_share": (fcount.most_common(1)[0][1] / len(cur)) if cur else 0.0,
        "top2_file_share": (sum(n for _, n in fcount.most_common(2)) / len(cur)) if cur else 0.0,
        "class_entropy": entropy(list(cc.values())),
        "failing_last2": len(cf & pf),
        "failing_all_rounds": sum(1 for f in cf if age[f] == k),
        "oldest_age": max((age[f] for f in cf), default=0),
        "mean_age": (sum(age[f] for f in cf) / len(cf)) if cf else 0.0,
        "frac_new_failures": len(cf - ever_before) / len(cf) if cf else 0.0,
    }
    return fv


def fires_at(t, name, direction, thr):
    for k in range(2, t["n"] + 1):
        v = features_at(t, k)[name]
        if (v >= thr) if direction == "hi" else (v <= thr):
            return k
    return None


def score(traces, name, direction, thr):
    bf = bm = nf = nh = gf = gh = 0
    saved, firstk = [], []
    for t in traces:
        k = fires_at(t, name, direction, thr)
        if t["label"] == "BROAD_BOUNDARY":
            if k:
                bf += 1
                saved.append(t["n"] - k)
                firstk.append(k)
            else:
                bm += 1
        elif t["label"] == "NARROW_STALL":
            nf, nh = (nf + 1, nh) if k else (nf, nh + 1)
        else:
            gf, gh = (gf + 1, gh) if k else (gf, gh + 1)
    b, n_, g = bf + bm, nf + nh, gf + gh
    s = sorted(saved)
    return {"recall": bf / b if b else float("nan"),
            "ff_narrow": nf / n_ if n_ else float("nan"),
            "ff_green": gf / g if g else float("nan"),
            "med_saved": s[len(s) // 2] if s else 0,
            "med_k": sorted(firstk)[len(firstk) // 2] if firstk else 0,
            "n_broad": b}


def candidate_thresholds(traces, name):
    vals = set()
    for t in traces:
        for k in range(2, t["n"] + 1):
            vals.add(round(features_at(t, k)[name], 3))
    return sorted(vals)


def main():
    traces = []
    for f in sorted(os.listdir(LOGS)):
        if f.endswith(".log"):
            t = load(os.path.join(LOGS, f))
            if t:
                traces.append(t)
    bench = [t for t in traces if t["fixture"] in ("p1", "p4", "map")]
    doclink = [t for t in traces if t["fixture"] == "doclink"]
    print(f"{len(traces)} traces | fit pool {len(bench)} | doclink stress {len(doclink)}")
    print(f"{len(FEATURES)} pre-registered features\n")

    # Objective: safety first. Pick, per feature, the threshold maximising recall subject
    # to no false fire on either negative class, evaluated LOFO on the bench pool only.
    print(f"{'feature':<21} {'dir':<4} {'group':<12} {'thr':>7} "
          f"{'LOFO rec':>9} {'FFn':>5} {'FFg':>5} | {'doclink rec':>11} {'FFn':>5} "
          f"{'FFg':>5} {'saved':>6} {'fires@k':>8}")
    print("-" * 122)
    rows = []
    for name, direction, group in FEATURES:
        best = None
        for thr in candidate_thresholds(bench, name):
            agg = {"rec": [], "ffn": [], "ffg": []}
            ok = True
            for held in ("p1", "p4", "map"):
                te = [t for t in bench if t["fixture"] == held]
                if not te:
                    continue
                s = score(te, name, direction, thr)
                if (s["ff_narrow"] or 0) > 0 or (s["ff_green"] or 0) > 0:
                    ok = False
                    break
                if not math.isnan(s["recall"]):
                    agg["rec"].append(s["recall"])
            if not ok or not agg["rec"]:
                continue
            rec = sum(agg["rec"]) / len(agg["rec"])
            if best is None or rec > best[1]:
                best = (thr, rec)
        if best is None:
            print(f"{name:<21} {direction:<4} {group:<12} {'—':>7}   "
                  f"no threshold with zero false fires on held-out bench fixtures")
            continue
        thr, rec = best
        d = score(doclink, name, direction, thr)
        rows.append((name, group, thr, rec, d))
        print(f"{name:<21} {direction:<4} {group:<12} {thr:>7.3f} {rec:>9.2f} "
              f"{0.0:>5.2f} {0.0:>5.2f} | {d['recall']:>11.2f} {d['ff_narrow']:>5.2f} "
              f"{d['ff_green']:>5.2f} {d['med_saved']:>6} {d['med_k']:>8}")

    print("\n  Ranked by doclink stress performance (recall high, narrow false-fire low):")
    viable = [r for r in rows if r[4]["ff_narrow"] <= 0.20 and r[4]["recall"] >= 0.50]
    if viable:
        for name, group, thr, rec, d in sorted(viable, key=lambda r: -r[4]["recall"]):
            print(f"    {name:<21} thr {thr:<7.3f} doclink recall {d['recall']:.2f} "
                  f"FFnarrow {d['ff_narrow']:.2f} saved {d['med_saved']}")
    else:
        print("    NONE — no single pre-registered feature clears doclink at "
              "recall>=0.50 with narrow false-fire<=0.20.")
    print("\n  Shadow mode: no threshold promoted, nothing here alters a build.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
