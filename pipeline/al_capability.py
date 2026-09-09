"""al_capability — which model is actually good at which kind of AL, from local evidence.

`build_leaderboard.py` answers "which model passes more often". That is one number for a
job that is not one job: a model that writes clean greenfield CRUD and a model that gets
event subscriptions right are different models, and a single pass rate hides the
difference completely.

This breaks the record down by FAILURE CLASS — API hallucination, event hallucination,
UI, permissions, performance rules, syntax — and only then offers a routing suggestion.

The rule that matters most is the one the handover states plainly: *do not hard-code this
from benchmark claims; use local measured evidence*. So:

  * every figure carries the n it came from, and n is never hidden in a footnote
  * below `MIN_RUNS` for a class, this returns INSUFFICIENT EVIDENCE and no
    recommendation — not a shaky one hedged with words
  * a class with no data at all says "not measured" rather than silently scoring 0

That is not caution for its own sake. Seven wrong calls were made on this very benchmark
by reading one log and generalising, and a routing table built on three runs would
industrialise exactly that mistake.

Evidence comes from the metrics JSONL the runners already write. Two generations of it
exist: `first_pass_diagnostics` (coarse classes, on ~240 historical runs) and
`first_pass_codes` (exact diagnostics, added later and growing). Both are read; the coarse
one is not thrown away just because something better arrived.
"""
from __future__ import annotations

import glob
import json
import os
from collections import defaultdict

import al_errors

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_METRICS = [os.path.join(HERE, ".build-metrics.jsonl"),
                   "/mnt/rojaws/localDev/projects/bench/.*metrics*.jsonl"]
# Below this many runs a rate is noise wearing a percentage sign.
MIN_RUNS = int(os.environ.get("CAPABILITY_MIN_RUNS", "8"))

# The failure classes the handover asks for, and where each is actually measured from.
# `codes` are exact diagnostics (newer runs); `coarse` are the older bucket names.
CLASSES = {
    "api_hallucination": {
        "coarse": {"missing-symbols"},
        "categories": {"symbols"},
        "why": "invented an object or a member that does not exist",
    },
    "event_hallucination": {
        "coarse": {"missing-method-event"},
        "categories": {"events"},
        "why": "invented an event, or bound a subscriber by the wrong parameter name",
    },
    "type_misuse": {
        "coarse": {"type-mismatch"},
        "categories": {"types"},
        "why": "wrong type, wrong operator, or an invalid property value",
    },
    "syntax_break": {
        "coarse": {"syntax"},
        "categories": {"syntax"},
        "why": "structural break — usually one defect cascading into many errors",
    },
    "ui_failure": {
        "coarse": set(),
        "codes": {"AA0218", "PTE0008", "AA0194"},
        "why": "missing tooltip, ApplicationArea, or an action that does nothing",
    },
    "permission_failure": {
        "coarse": set(),
        "codes": {"PTE0004"},
        "why": "object not covered by a permission set",
    },
    "duplicate_declaration": {
        "coarse": set(),
        "categories": {"duplicate"},
        "why": "declared the same object, id or member twice",
    },
}


def _iter_metrics(paths=None):
    for pat in (paths or DEFAULT_METRICS):
        for f in sorted(glob.glob(pat)):
            try:
                with open(f) as fh:
                    for ln in fh:
                        ln = ln.strip()
                        if not ln:
                            continue
                        try:
                            yield json.loads(ln)
                        except ValueError:
                            continue
            except OSError:
                continue


def _class_hits(run):
    """{class: count} for one run, from whichever evidence that run carries."""
    out = defaultdict(int)
    coarse = run.get("first_pass_diagnostics") or {}
    if isinstance(coarse, list):
        coarse = {k: 1 for k in coarse}
    codes = run.get("first_pass_codes") or []
    for name, spec in CLASSES.items():
        for bucket in spec.get("coarse", ()):
            out[name] += int(coarse.get(bucket, 0) or 0)
        for c in codes:
            c = al_errors.normalise(c)
            if c in spec.get("codes", ()):
                out[name] += 1
            elif al_errors.category(c) in spec.get("categories", ()):
                out[name] += 1
    return dict(out)


def profile(paths=None):
    """{model: stats}. Every rate carries the run count it was computed from."""
    acc = defaultdict(lambda: {
        "runs": 0, "first_pass_compile": 0, "final_compile": 0, "fix_rounds": [],
        "review_findings": [], "classes": defaultdict(int), "class_runs": defaultdict(int),
        "tests_run": 0, "tests_passed": 0, "perf_findings": 0, "perf_runs": 0,
        "code_evidence_runs": 0, "observed_runs": 0, "write_failed": 0,
    })
    for run in _iter_metrics(paths):
        m = run.get("coder_model") or "unknown"
        a = acc[m]
        a["runs"] += 1
        if run.get("first_pass_compile"):
            a["first_pass_compile"] += 1
        if run.get("final_compile"):
            a["final_compile"] += 1
        # fix_rounds is None when a build NEVER reached a clean compile — by design.
        # Averaging only the non-None values averages only the runs that succeeded, which
        # makes a model that fails often look efficient. Charge a failure the full cap it
        # actually spent instead.
        if isinstance(run.get("fix_rounds"), (int, float)):
            a["fix_rounds"].append(run["fix_rounds"])
        elif run.get("final_compile") is False:
            a["fix_rounds"].append(run.get("max_fix_rounds")
                                   or run.get("fix_rounds_attempted") or 0)
        if run.get("outcome") == "write-failed":
            a["write_failed"] += 1
        if isinstance(run.get("review_findings_count"), (int, float)):
            a["review_findings"].append(run["review_findings_count"])
        if run.get("first_pass_codes"):
            a["code_evidence_runs"] += 1
        # A failure class can only be OBSERVED in a run that produced diagnostics.
        # Using total runs as the denominator rewards a model for passing first time
        # on an unrelated task and, worse, a model that dies at syntax never reaches
        # the point where an API can be hallucinated — so it scores 0% and looks best.
        if run.get("first_pass_diagnostics") or run.get("first_pass_codes"):
            a["observed_runs"] += 1
        st = run.get("tests_status")
        if st in ("passed", "failed"):
            a["tests_run"] += 1
            if st == "passed":
                a["tests_passed"] += 1
        sem = run.get("al_semantic_findings")
        if isinstance(sem, dict):
            a["perf_runs"] += 1
            a["perf_findings"] += sum(sem.values())
        for cls, n in _class_hits(run).items():
            a["classes"][cls] += n
            if n:
                a["class_runs"][cls] += 1
    return {m: _finish(a) for m, a in acc.items()}


def _rate(hit, runs):
    return None if not runs else round(100 * hit / runs)


def _finish(a):
    runs = a["runs"]
    obs = a["observed_runs"]
    return {
        "runs": runs,
        "first_pass_compile_pct": _rate(a["first_pass_compile"], runs),
        "final_compile_pct": _rate(a["final_compile"], runs),
        "avg_fix_rounds": (round(sum(a["fix_rounds"]) / len(a["fix_rounds"]), 1)
                           if a["fix_rounds"] else None),
        "avg_review_findings": (round(sum(a["review_findings"]) / len(a["review_findings"]), 1)
                                if a["review_findings"] else None),
        # "tests were run" and "tests passed" are different populations; a project with no
        # tests is neither, and must not dilute either number.
        "tests_runs": a["tests_run"],
        "tests_pass_pct": _rate(a["tests_passed"], a["tests_run"]),
        "perf_findings_per_run": (round(a["perf_findings"] / a["perf_runs"], 1)
                                  if a["perf_runs"] else None),
        "code_evidence_runs": a["code_evidence_runs"],
        # Produced no files at all — the failure that used to leave no trace.
        "write_failed": a["write_failed"],
        # Denominator is runs that produced diagnostics, not all runs — see profile().
        # observed_runs travels with every rate so it cannot be read without its
        # population.
        "observed_runs": obs,
        "classes": {c: {"hits": a["classes"][c],
                        "runs_affected": a["class_runs"][c],
                        "affected_pct": _rate(a["class_runs"][c], obs)}
                    for c in sorted(CLASSES)},
    }


def rank(prof, cls, min_runs=None):
    """Models ordered by how RARELY they hit `cls`. Thin evidence is excluded, not
    ranked last — an unmeasured model is not a good one."""
    min_runs = MIN_RUNS if min_runs is None else min_runs
    rows = [(m, s["classes"][cls]["affected_pct"], s["observed_runs"])
            for m, s in prof.items()
            if s["observed_runs"] >= min_runs
            and s["classes"][cls]["affected_pct"] is not None]
    return sorted(rows, key=lambda r: (r[1], -r[2]))


# Task kinds → the failure classes that actually decide them. Routing is only as good as
# this mapping, so it is stated explicitly rather than buried in a scoring function.
TASK_CLASSES = {
    "greenfield": ["syntax_break", "duplicate_declaration"],
    "api": ["api_hallucination", "type_misuse"],
    "events": ["event_hallucination", "api_hallucination"],
    "ui": ["ui_failure", "syntax_break"],
    "upgrade": ["api_hallucination", "event_hallucination", "type_misuse"],
    "permissions": ["permission_failure"],
}


def recommend(prof, kind, min_runs=None):
    """(model, reason). model is None when the evidence does not support a choice.

    Returning None is the point. A routing table built on three runs is worse than no
    routing table, because it looks like knowledge.
    """
    min_runs = MIN_RUNS if min_runs is None else min_runs
    classes = TASK_CLASSES.get(kind)
    if not classes:
        return None, f"unknown task kind {kind!r} — known: {', '.join(sorted(TASK_CLASSES))}"

    # Eligibility is on OBSERVED runs: a model with 200 clean passes and 2 failures
    # has told us nothing about which failures it makes.
    eligible = {m: s for m, s in prof.items() if s["observed_runs"] >= min_runs}
    if not eligible:
        best = max((s["observed_runs"] for s in prof.values()), default=0)
        return None, (f"INSUFFICIENT EVIDENCE — no model has {min_runs}+ runs with "
                      f"observed diagnostics (best is {best}). Measure before routing.")
    if len(eligible) == 1:
        m = next(iter(eligible))
        return None, (f"INSUFFICIENT EVIDENCE — only {m} has {min_runs}+ observed runs, so "
                      f"nothing to compare it against. This is a default, not a choice.")

    scored = []
    for m, s in eligible.items():
        pcts = [s["classes"][c]["affected_pct"] for c in classes
                if s["classes"][c]["affected_pct"] is not None]
        if not pcts:
            continue
        scored.append((sum(pcts) / len(pcts), m, s["observed_runs"]))
    if not scored:
        return None, (f"INSUFFICIENT EVIDENCE — none of {', '.join(classes)} has been "
                      f"measured for any eligible model")
    scored.sort()
    best_score, best_model, best_runs = scored[0]
    if len(scored) > 1 and abs(scored[1][0] - best_score) < 5:
        return None, (f"NO CLEAR WINNER — {best_model} ({best_score:.0f}%) and "
                      f"{scored[1][1]} ({scored[1][0]:.0f}%) are within 5 points on "
                      f"{', '.join(classes)}. Not a difference worth routing on.")
    return best_model, (f"{best_model} hits {', '.join(classes)} in {best_score:.0f}% of "
                        f"{best_runs} runs, against {scored[1][0]:.0f}% for "
                        f"{scored[1][1]}")


def report(prof, min_runs=None):
    min_runs = MIN_RUNS if min_runs is None else min_runs
    L = ["# AL capability by failure class",
         "",
         "Measured locally from build metrics. Rates below "
         f"{min_runs} runs are shown but never routed on.", ""]
    L.append("| model | runs | observed | 1st-pass | final | fix rounds | tests | perf/run |")
    L.append("|---|---:|---:|---:|---:|---:|---:|---:|")
    for m, s in sorted(prof.items(), key=lambda kv: -kv[1]["runs"]):
        tests = (f'{s["tests_pass_pct"]}% ({s["tests_runs"]})'
                 if s["tests_pass_pct"] is not None else "not measured")
        wf = f' | wrote nothing: {s["write_failed"]}' if s["write_failed"] else ""
        L.append(f'| `{m}` | {s["runs"]} | {s["observed_runs"]} | '
                 f'{s["first_pass_compile_pct"]}% | '
                 f'{s["final_compile_pct"]}% | {s["avg_fix_rounds"]} | {tests} | '
                 f'{s["perf_findings_per_run"] if s["perf_findings_per_run"] is not None else "—"} |'
                 + (f'  <!--{wf}-->' if wf else ''))

    L += ["", "## Failure classes — % of OBSERVED runs affected", "",
          "Denominator is runs that produced first-pass diagnostics, not all runs. "
          "Read with one caveat: a model that dies at syntax never reaches the point "
          "where an API can be hallucinated, so a low rate in a later class may mean "
          "it failed earlier rather than that it is good at that class. Check the "
          "first-pass and syntax columns before concluding anything.", "",
          "| model | " + " | ".join(c.replace("_", " ") for c in sorted(CLASSES)) + " |",
          "|---" * (len(CLASSES) + 1) + "|"]
    for m, s in sorted(prof.items(), key=lambda kv: -kv[1]["runs"]):
        cells = []
        for c in sorted(CLASSES):
            v = s["classes"][c]["affected_pct"]
            cells.append("—" if v is None else f"{v}%")
        L.append(f"| `{m}` | " + " | ".join(cells) + " |")

    routed = {k: recommend(prof, k, min_runs) for k in sorted(TASK_CLASSES)}
    decided = [k for k, (m, _) in routed.items() if m]
    L += ["", "## Routing", ""]
    if not decided:
        # Worth saying outright rather than leaving somebody to infer it from six
        # identical bullets. "No routing is justified yet" is a finding, not a gap.
        L.append("**No routing is justified by the current evidence.** Every task kind "
                 "below is either short of runs or too close to call. Route by cost and "
                 "availability until the gaps are measured — a table built on this data "
                 "would look like knowledge and be noise.")
        L.append("")
    for kind in sorted(TASK_CLASSES):
        model, why = routed[kind]
        L.append(f"- **{kind}** → {model or 'no recommendation'} — {why}")

    thin = [m for m, s in prof.items() if s["runs"] < min_runs]
    if thin:
        L += ["", f"_Excluded from routing ({min_runs}-run minimum): "
                  + ", ".join(f"`{m}`" for m in sorted(thin)) + "._"]
    ev = sum(s["code_evidence_runs"] for s in prof.values())
    tot = sum(s["runs"] for s in prof.values())
    L += ["", f"_Exact per-diagnostic evidence on {ev}/{tot} runs; the remainder use the "
              f"coarse first-pass classes recorded before diagnostic codes were kept._"]
    return "\n".join(L)


def main():
    import argparse
    ap = argparse.ArgumentParser(prog="al_capability")
    ap.add_argument("--metrics", action="append", help="metrics jsonl (repeatable)")
    ap.add_argument("--min-runs", type=int, default=MIN_RUNS)
    ap.add_argument("--recommend", metavar="KIND",
                    help="task kind: " + ", ".join(sorted(TASK_CLASSES)))
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    prof = profile(a.metrics)
    if not prof:
        print("no build metrics found — nothing measured yet")
        return 2
    if a.recommend:
        model, why = recommend(prof, a.recommend, a.min_runs)
        print(f"{a.recommend}: {model or 'NO RECOMMENDATION'}\n  {why}")
        return 0 if model else 1
    print(json.dumps(prof, indent=2, sort_keys=True) if a.json
          else report(prof, a.min_runs))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
