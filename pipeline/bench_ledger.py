#!/usr/bin/env python3
"""bench_ledger.py — cumulative realised spend for a benchmark suite. TELEMETRY ONLY.

WHY THIS CANNOT INFLUENCE A RUN
-------------------------------
A suite-level spend figure is useful for watching exposure and dangerous as a control input.
A cap driven by realised cost makes the stopping rule depend on an OUTCOME: the expensive
cells consume the budget first, later observations go selectively missing, and the per-fixture
estimates are no longer based on the fixed allocation they were registered with.

So this module only ever READS metrics that already exist and APPENDS a line. It exposes no
threshold, no predicate, and no boolean. There is deliberately nothing here for a driver to
branch on — the distinction being preserved is that a guard preventing an INVALID measurement
is legitimate, while a guard that selectively stops expensive VALID measurements changes the
experiment.

Exposure is bounded by the fixed allocation (120 runs), not by spend.

    python3 bench_ledger.py <tag>        # print the running total for a suite
"""

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
METRICS = os.environ.get("BUILD_METRICS", os.path.join(HERE, ".build-metrics.jsonl"))
LEDGER = os.environ.get("BENCH_LEDGER", os.path.join(HERE, ".bench-ledger.jsonl"))


def suite_rows(tag):
    """Metrics rows belonging to a suite tag. Missing/short file → empty, never raises."""
    out = []
    try:
        with open(METRICS) as fh:
            for line in fh:
                try:
                    r = json.loads(line)
                except ValueError:
                    continue
                if tag in (r.get("project") or "") or r.get("suite_tag") == tag:
                    out.append(r)
    except OSError:
        pass
    return out


def totals(tag):
    """Cumulative realised spend for a suite. A DESCRIPTION, not a verdict."""
    rows = suite_rows(tag)
    t = {"tag": tag, "runs": len(rows), "cost_usd": 0.0, "calls": 0,
         "input_tokens": 0, "output_tokens": 0, "rows_missing_usage": 0}
    for r in rows:
        t["cost_usd"] += r.get("claude_cost_usd") or 0.0
        t["calls"] += r.get("claude_calls") or 0
        t["input_tokens"] += r.get("claude_input_tokens") or 0
        t["output_tokens"] += r.get("claude_output_tokens") or 0
        if r.get("claude_calls_missing_usage"):
            t["rows_missing_usage"] += 1
    t["cost_usd"] = round(t["cost_usd"], 6)
    return t


def note(tag):
    """Append one ledger line and return a human-readable string. Fail-open: telemetry
    must never be the reason a suite stops."""
    t = totals(tag)
    try:
        with open(LEDGER, "a") as fh:
            fh.write(json.dumps(t) + "\n")
    except OSError:
        pass
    warn = (f"  ⚠ {t['rows_missing_usage']} row(s) with unpriced calls — spend INCOMPLETE"
            if t["rows_missing_usage"] else "")
    return (f"cumulative [{tag}]: {t['runs']} run(s), {t['calls']} call(s), "
            f"${t['cost_usd']:.4f}, {t['input_tokens']}in/{t['output_tokens']}out{warn}")


if __name__ == "__main__":
    print(note(sys.argv[1] if len(sys.argv) > 1 else ""))
