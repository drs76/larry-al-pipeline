"""al_sections — inject the SECTIONS a build needs, not whole reference topics.

`select_topics()` picks whole files. A build writing one table and one page is handed all
of `02-objects` — 6.5k tokens covering reports, queries, xmlports and control add-ins —
because the topic is the smallest unit the injector can address. That is why only 8 of 26
reference topics are reachable at all: at whole-file granularity the 14k budget is spent
after three.

This ranks the `##`/`###` sections inside a topic against what the build is actually
about, and returns only those that fit a budget. Same corpus, a fraction of the tokens,
and the topics currently priced out become affordable.

Ranking is `kb`'s embedding model (mxbai-embed-large, 0.67GB) — the one small model that
co-resides with the 22.4GB coder on a 25.7GB card, so this costs no eviction and no swap.
Cosine similarity, not model judgement: a retrieval agent that drops a section does so
silently and you find out from a worse build.

**Fail-open, always.** Any error — Larry unreachable, embedding refused, a topic that will
not parse — returns the WHOLE topic, which is exactly today's behaviour. Injecting less
than the current pipeline because a network call failed would be a silent quality
regression, and the failure mode this must not have.
"""
from __future__ import annotations

import os
import re

TOK = 3700.0                     # bytes per 1000 tokens (matches run-build)
H_RE = re.compile(r"^(#{2,3})\s+(.+?)\s*$")
# The always-on topic: its summary is short, load-bearing, and every build wants it.
# Matching the WORD "gotcha" in any heading was the first attempt and was wrong — across
# 26 topics it force-kept archiving gotchas, ruleset gotchas and namespacing gotchas into
# a table-and-page build, spending 6 of 27 slots on material the query never asked for.
# Relevance is what ranking is for; only the dedicated topic gets a free pass.
ALWAYS_TOPIC = "00-gotchas.md"


def split_sections(path):
    """[(heading, body_with_heading)] for one topic file.

    Splits on ## and ### only. Deeper levels stay with their parent — injecting half a
    section is worse than injecting none of it, because the model cannot tell it is
    reading a fragment.
    """
    try:
        text = open(path, encoding="utf-8", errors="replace").read()
    except OSError:
        return []
    lines = text.splitlines()
    out, head, buf = [], "", []

    def flush():
        if buf and any(l.strip() for l in buf):
            out.append((head, "\n".join(buf).strip()))

    for ln in lines:
        m = H_RE.match(ln)
        if m:
            flush()
            head, buf = m.group(2).strip(), [ln]
        else:
            buf.append(ln)
    flush()
    return out


def _cos(a, b):
    num = sum(x * y for x, y in zip(a, b))
    da = sum(x * x for x in a) ** 0.5
    db = sum(y * y for y in b) ** 0.5
    return num / (da * db) if da and db else 0.0


def rank_sections(query, sections):
    """[(score, heading, body)] best first, or None when ranking is unavailable.

    None is distinct from an empty list on purpose: the caller must be able to tell
    "nothing scored" from "ranking did not run", and fall back only for the second.
    """
    if not sections:
        return []
    try:
        import sys
        sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(
            os.path.abspath(__file__))), "tooling"))
        import kb_core
        vecs = kb_core.embed([query] + [f"{h}\n{b}"[:2000] for h, b in sections])
    except Exception:
        return None
    # kb_core.embed returns a numpy array — truthiness on an ndarray raises, so length
    # is the only safe emptiness test here.
    if vecs is None or len(vecs) != len(sections) + 1:
        return None
    q, rest = vecs[0], vecs[1:]
    return sorted(((_cos(q, v), h, b) for v, (h, b) in zip(rest, sections)),
                  key=lambda r: -r[0])


def select(topic_paths, query, budget_k, min_score=0.0):
    """(text, kept, dropped, used_k) — the sections to inject, within budget.

    Greedy by score across ALL topics, so a highly relevant section in a topic that
    whole-file injection could never afford now beats a mediocre one in a topic that fits.
    """
    pool, whole = [], []
    for p in topic_paths:
        secs = split_sections(p)
        if not secs:
            continue
        ranked = rank_sections(query, secs)
        if ranked is None:
            whole.append(p)          # ranking unavailable — this topic goes in entire
            continue
        name = os.path.basename(p)
        for score, h, b in ranked:
            pool.append((1.0 if name == ALWAYS_TOPIC else score, name, h, b))

    pool.sort(key=lambda r: -r[0])
    kept, dropped, used = [], [], 0.0

    for p in whole:                  # fail-open topics are non-negotiable, budget first
        try:
            size = os.path.getsize(p) / TOK
        except OSError:
            continue
        kept.append((os.path.basename(p), "(whole topic — ranking unavailable)"))
        used += size

    for score, name, h, b in pool:
        if score < min_score:
            dropped.append((name, h))
            continue
        size = len(b) / TOK
        if used + size > budget_k:
            dropped.append((name, h))
            continue
        kept.append((name, h))
        used += size

    parts = []
    for p in whole:
        try:
            parts.append(open(p, encoding="utf-8", errors="replace").read())
        except OSError:
            pass
    for score, name, h, b in pool:
        if (name, h) in kept:
            parts.append(b)
    return "\n\n".join(parts), kept, dropped, used


def compare(topic_paths, query, budget_k):
    """What whole-file injection costs versus section selection. For measurement."""
    whole = sum(os.path.getsize(p) for p in topic_paths if os.path.exists(p)) / TOK
    _text, kept, dropped, used = select(topic_paths, query, budget_k)
    return {"whole_k": round(whole, 2), "sections_k": round(used, 2),
            "kept": len(kept), "dropped": len(dropped),
            "saved_pct": round(100 * (whole - used) / whole) if whole else 0}


def main():
    import argparse
    import json
    ap = argparse.ArgumentParser(prog="al_sections")
    ap.add_argument("query")
    ap.add_argument("topics", nargs="*", help="topic files (default: the injected set)")
    ap.add_argument("--budget", type=float, default=14.0)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--show", action="store_true", help="print the selected sections")
    a = ap.parse_args()

    ref = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "reference", "al-reference")
    topics = a.topics or [os.path.join(ref, f"{n}.md") for n in
                          ("00-gotchas", "01-syntax-style", "02-objects")]
    text, kept, dropped, used = select(topics, a.query, a.budget)
    if a.json:
        print(json.dumps({"used_k": round(used, 2), "kept": kept,
                          "dropped": len(dropped)}, indent=2))
    elif a.show:
        print(text)
    else:
        print(json.dumps(compare(topics, a.query, a.budget), indent=2))
        print("\nkept:")
        for n, h in kept:
            print(f"  {n:22} {h[:60]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
