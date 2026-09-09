#!/usr/bin/env python3
"""RAG retrieval eval — does the KB surface the RIGHT object/event for an intent?

Measures retrieval quality (not generation) against a grounded eval set
(`rag_eval.yaml`): for each query it asks the KB for top-k chunks and checks whether
an expected string (a real object/event name) shows up. Reports hit@1 / hit@3 /
hit@k + MRR, per-query and aggregate; exits non-zero if aggregate hit@k is below
the set's threshold. This is the yardstick that turns "the RAG change helped" from
an assertion into a number (see feedback: no_partial_generalising).

Queries the same `kb` the coder uses, so it honours KB_REMOTE (point it at the
Larry serve) or a local KB_DB. Run:
    KB_REMOTE=http://larry.home.arpa:8848 KB_REMOTE_TOKEN=... \
      python3 pipeline/rag_eval.py [--eval rag_eval.yaml] [--k N] [--json]
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
KB = os.path.join(HERE, "..", "tooling", "kb_core.py")


def search(query: str, corpus: str | None, k: int) -> list[dict]:
    cmd = [sys.executable, KB, "search", query, "-n", str(k), "--json"]
    if corpus:
        cmd += ["--corpus", corpus]
    p = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    if p.returncode != 0:
        raise RuntimeError(p.stderr.strip() or "kb search failed")
    return json.loads(p.stdout or "[]")


def first_hit_rank(hits: list[dict], expects: list[str]) -> int:
    """1-based rank of the first chunk whose heading+snippet contains any expect; 0 = miss."""
    for i, h in enumerate(hits, 1):
        hay = (h.get("heading", "") + " " + h.get("snippet", "")).lower()
        if any(e.lower() in hay for e in expects):
            return i
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--eval", default=os.path.join(HERE, "rag_eval.yaml"))
    ap.add_argument("--k", type=int, default=None, help="override top-k from the eval set")
    ap.add_argument("--json", action="store_true", help="machine-readable summary")
    args = ap.parse_args()

    import yaml
    with open(args.eval) as fh:
        spec = yaml.safe_load(fh)
    k = args.k or int(spec.get("k", 5))
    threshold = float(spec.get("threshold", 0.8))
    queries = spec.get("queries", [])
    if not queries:
        sys.exit("eval set has no queries")

    rows, ranks = [], []
    hit1 = hit3 = hit5 = hitk = 0
    for q in queries:
        expects = q["expect"] if isinstance(q["expect"], list) else [q["expect"]]
        try:
            hits = search(q["q"], q.get("corpus"), k)
            rank = first_hit_rank(hits, expects)
        except Exception as e:
            rank = 0
            hits = [{"heading": f"ERROR: {e}"}]
        ranks.append(rank)
        hit1 += 1 if rank == 1 else 0
        hit3 += 1 if 0 < rank <= 3 else 0
        hit5 += 1 if 0 < rank <= 5 else 0
        hitk += 1 if rank > 0 else 0
        rows.append({
            "q": q["q"], "expect": expects, "rank": rank,
            "top": hits[0].get("heading", "")[:80] if hits else "",
        })

    n = len(queries)
    mrr = sum(1.0 / r for r in ranks if r) / n
    summary = {
        "n": n, "k": k,
        "hit@1": hit1 / n, "hit@3": hit3 / n, "hit@5": hit5 / n, f"hit@{k}": hitk / n,
        "mrr": round(mrr, 3), "threshold": threshold, "pass": hitk / n >= threshold,
    }

    if args.json:
        print(json.dumps({"summary": summary, "rows": rows}, indent=1))
    else:
        print(f"RAG retrieval eval — {n} queries, k={k}\n" + "-" * 66)
        for r in rows:
            mark = "·MISS·" if r["rank"] == 0 else f" @{r['rank']}  "
            print(f"[{mark}] {r['q'][:44]:44s} -> {r['top']}")
        print("-" * 66)
        khit = f"hit@{k} {summary[f'hit@{k}']:.0%}   " if k != 5 else ""
        print(f"hit@1 {summary['hit@1']:.0%}   hit@3 {summary['hit@3']:.0%}   "
              f"hit@5 {summary['hit@5']:.0%}   {khit}MRR {summary['mrr']:.3f}")
        print(f"{'PASS' if summary['pass'] else 'FAIL'} "
              f"(hit@{k} {summary[f'hit@{k}']:.0%} vs threshold {threshold:.0%})")
    return 0 if summary["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
