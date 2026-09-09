#!/usr/bin/env python3
"""SHADOW MODE. Compound rule test: broad NOW + low resolution + stable/expanding set.

The 27-feature inventory (capability-features.py) found no single prefix feature clearing
the doclink stress case: high recall always came with high false-fire on narrow stalls.
The diagnosis it produced was specific — expansion IS the broad-boundary signature
(new_files reaches 0.93 recall on doclink) but is not sufficient, because doclink narrow
stalls also expand before contracting to a small terminal set.

So this tests the compound shape that diagnosis implies:

    files_now        >= A     currently broad, not historically broad
    resolved_fraction <= B    repair is not clearing the current set
    net_file_change  >= C     the unresolved set is stable or growing
    top2_file_share  <= D     errors are spread, not concentrated in one artifact

OVERFITTING IS THE MAIN RISK HERE, NOT UNDERFITTING
---------------------------------------------------
Four free parameters against 44 broad doclink traces can fit by accident. A single
"fit on bench, test on doclink" split is not enough, because doclink is where the
parameters would end up tuned. So this reports FOUR splits, always showing the fit-set
and test-set numbers side by side so the generalisation gap is visible:

  A  fit bench (p1/p4/map)          -> test doclink
  B  fit doclink {doclinkfix,...}   -> test doclink {incrab, incrab2}
  C  fit doclink {incrab, incrab2}  -> test doclink {doclinkfix, ...}
  D  fit all doclink                -> test bench

Splits B and C hold out by SUITE within doclink: runs inside one suite share a handover
and are highly correlated, so splitting by suite is the honest grouping.

Two null baselines are printed for reference. A rule that cannot beat "always fire at
k=2" on the tradeoff is not a rule.

No threshold is promoted. Nothing here alters a build.
"""
import os
import sys
from itertools import product


# Reuse the inventory's loader/feature code without duplicating it.
import importlib.util
_spec = importlib.util.spec_from_file_location(
    "capfeat", os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "capability-features.py"))
capfeat = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(capfeat)

LOGS = capfeat.LOGS

# ---- PRE-REGISTERED grid, fixed before inspecting any result -----------------------
GRID_A = [2, 3, 4, 5]          # files_now >=
GRID_B = [0.0, 0.10, 0.25, 0.50]   # resolved_fraction <=
GRID_C = [-1, 0, 1]            # net_file_change >=
GRID_D = [0.60, 0.75, 0.90, 1.01]  # top2_file_share <=


def suite_of(log):
    parts = log.split("__")
    if len(parts) >= 3:
        return parts[2].replace("_control", "").replace("_challenger", "")
    return "?"


def fires(t, p):
    a, b, c, d = p
    for k in range(2, t["n"] + 1):
        f = capfeat.features_at(t, k)
        if (f["files_now"] >= a and f["resolved_fraction"] <= b
                and f["net_file_change"] >= c and f["top2_file_share"] <= d):
            return k
    return None


def score(traces, p):
    bf = bm = nf = nh = gf = gh = 0
    saved = []
    for t in traces:
        k = fires(t, p)
        if t["label"] == "BROAD_BOUNDARY":
            if k:
                bf += 1
                saved.append(t["n"] - k)
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
            "n": (b, n_, g)}


def fit(traces, max_ff_narrow=0.20):
    """Max recall subject to narrow false-fire <= cap and zero green false-fire."""
    best = None
    for p in product(GRID_A, GRID_B, GRID_C, GRID_D):
        s = score(traces, p)
        ffn = 0.0 if s["ff_narrow"] != s["ff_narrow"] else s["ff_narrow"]
        ffg = 0.0 if s["ff_green"] != s["ff_green"] else s["ff_green"]
        if ffg > 0 or ffn > max_ff_narrow:
            continue
        r = s["recall"]
        if r != r:
            continue
        if best is None or r > best[1]["recall"]:
            best = (p, s)
    return best


def show(tag, p, fit_s, test_s):
    a, b, c, d = p
    print(f"\n--- {tag} ---")
    print(f"  rule: files_now>={a}  resolved_frac<={b}  net_change>={c}  top2_share<={d}")
    for nm, s in (("FIT ", fit_s), ("TEST", test_s)):
        print(f"  {nm}  recall {s['recall']:>5.2f}  FFnarrow {s['ff_narrow']:>5.2f}  "
              f"FFgreen {s['ff_green']:>5.2f}  saved {s['med_saved']:>2}  "
              f"n(broad/narrow/green)={s['n']}")
    gap = (fit_s["recall"] - test_s["recall"])
    if gap == gap:
        print(f"  generalisation gap (fit recall - test recall): {gap:+.2f}")


def main():
    traces = []
    for f in sorted(os.listdir(LOGS)):
        if f.endswith(".log"):
            t = capfeat.load(os.path.join(LOGS, f))
            if t:
                t["suite"] = suite_of(t["log"])
                traces.append(t)
    bench = [t for t in traces if t["fixture"] in ("p1", "p4", "map")]
    doc = [t for t in traces if t["fixture"] == "doclink"]
    incr = [t for t in doc if t["suite"] in ("incrab", "incrab2")]
    fixs = [t for t in doc if t["suite"] not in ("incrab", "incrab2")]
    print(f"{len(traces)} traces | bench {len(bench)} | doclink {len(doc)} "
          f"(incr* {len(incr)}, other {len(fixs)})")
    print(f"grid: {len(GRID_A)*len(GRID_B)*len(GRID_C)*len(GRID_D)} combinations, "
          f"pre-registered")

    print("\n=== NULL BASELINES (doclink) ===")
    for name, p in (("always fire (files_now>=1, no other constraint)",
                     (1, 1.0, -99, 1.01)),
                    ("never fire (files_now>=99)", (99, 1.0, -99, 1.01))):
        s = score(doc, p)
        print(f"  {name:<48} recall {s['recall']:.2f}  FFnarrow {s['ff_narrow']:.2f}  "
              f"saved {s['med_saved']}")

    for tag, ftr, tst in (
            ("A: fit bench -> test doclink", bench, doc),
            ("B: fit doclink(fix*) -> test doclink(incr*)", fixs, incr),
            ("C: fit doclink(incr*) -> test doclink(fix*)", incr, fixs),
            ("D: fit all doclink -> test bench", doc, bench)):
        got = fit(ftr)
        if not got:
            print(f"\n--- {tag} ---\n  no rule in the grid meets the constraints on the "
                  f"fit set")
            continue
        p, fit_s = got
        show(tag, p, fit_s, score(tst, p))

    print("\n  A rule is credible only if TEST recall holds up across splits B and C,")
    print("  which hold out by suite WITHIN doclink. Shadow mode: nothing altered.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
