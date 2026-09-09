#!/usr/bin/env python3
"""
toc_plan — a Microsoft Learn TOC subtree → an ingest plan run-ingest.py can run.

Learn publishes its whole left-hand navigation as JSON: every article's metadata
carries `toc_rel`, and the resolved file (e.g. dev-itpro/toc.json) is the complete
tree with an href per node. That makes "ingest this whole documentation section" a
deterministic listing problem rather than HTML scraping — the exact analogue of
`source_collect scan` over a channel or feed, which is what run-ingest already
consumes.

Two phases stay two phases. This writes a plan you prune; nothing is fetched or
distilled until you hand the plan to `run-ingest.py run --plan`. That matters more
here than for a feed: a docs section is 50+ pages, each one a Claude call, all
merging into topic files that are already near the 8k-token budget.

Everything here is model-free — listing and filtering only.

Usage:
  toc_plan.py --section "The AL programming language" [--target AL-REFERENCE.md]
              [--toc <url>] [--out <plan.md>] [--verdict KEEP|SKIP] [--list-sections]

  # see what sections exist
  toc_plan.py --list-sections

  # plan a subtree, defaulting every row to SKIP so you opt rows IN
  toc_plan.py --section Objects --verdict SKIP

Then prune and run:
  python3 run-ingest.py run --plan reference/ingest-plan-<section>.md
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.environ.get("LARRY_REPO", os.path.dirname(HERE))

DEFAULT_TOC = ("https://learn.microsoft.com/en-us/dynamics365/business-central/"
               "dev-itpro/toc.json")
# Article hrefs in the TOC are relative to the toc.json's own directory.
DOC_ROOT = ("https://learn.microsoft.com/en-us/dynamics365/business-central/"
            "dev-itpro/")
VALID_TARGETS = {"AL-REFERENCE.md", "AL-KNOWLEDGE.md", "al-talks"}


def fetch_toc(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": "toc_plan/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def walk(node: dict, depth: int = 0):
    """Yield (depth, title, href) for every descendant, depth-first."""
    for child in node.get("children") or []:
        yield depth, child.get("toc_title", ""), child.get("href")
        yield from walk(child, depth + 1)


def find_section(items, title: str):
    """First node whose toc_title matches (case-insensitive, exact then substring)."""
    def search(nodes, pred):
        for n in nodes or []:
            if pred(n.get("toc_title", "")):
                return n
            hit = search(n.get("children"), pred)
            if hit:
                return hit
        return None

    t = title.lower()
    return (search(items, lambda x: x.lower() == t)
            or search(items, lambda x: t in x.lower()))


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--toc", default=DEFAULT_TOC)
    ap.add_argument("--section", help="TOC node title to plan (exact or substring)")
    ap.add_argument("--target", default="AL-REFERENCE.md", choices=sorted(VALID_TARGETS))
    ap.add_argument("--verdict", default="KEEP", choices=["KEEP", "SKIP"],
                    help="default verdict for every row (SKIP = opt rows in by hand)")
    ap.add_argument("--out", help="plan path (default reference/ingest-plan-<section>.md)")
    ap.add_argument("--list-sections", action="store_true",
                    help="print the top two levels and exit")
    args = ap.parse_args()

    toc = fetch_toc(args.toc)

    if args.list_sections:
        for top in toc.get("items", []):
            print(f"- {top.get('toc_title')}")
            for _, title, href in walk(top, 0):
                if _ == 0:
                    print(f"    - {title}" + (f"  [{href}]" if href else ""))
        return 0

    if not args.section:
        ap.error("--section is required (or use --list-sections)")

    node = find_section(toc.get("items", []), args.section)
    if not node:
        print(f"ERROR: no TOC node matching '{args.section}'. "
              f"Try --list-sections.", file=sys.stderr)
        return 1

    section_title = node.get("toc_title", args.section)
    rows = []
    for depth, title, href in walk(node):
        if not href:
            continue                      # grouping node, no article of its own
        if "://" in href:
            continue                      # cross-site link, not part of this doc set
        url = DOC_ROOT + href.lstrip("./")
        rows.append((depth, title, url))

    # Include the section's own landing page when it has one.
    if node.get("href"):
        rows.insert(0, (0, section_title, DOC_ROOT + node["href"].lstrip("./")))

    if not rows:
        print(f"no article nodes under '{section_title}'", file=sys.stderr)
        return 1

    out = args.out or os.path.join(REPO, "reference",
                                   f"ingest-plan-{slug(section_title)}.md")
    n_keep = len(rows) if args.verdict == "KEEP" else 0
    with open(out, "w", encoding="utf-8") as f:
        f.write(f"# Ingest plan — Learn TOC section: {section_title}\n\n")
        f.write(f"Source TOC: {args.toc}\n\n")
        f.write(f"{len(rows)} article(s); every row defaults to **{args.verdict}**. "
                f"{n_keep} KEEP / {len(rows) - n_keep} SKIP.\n\n")
        f.write("Prune before running — each KEEP row is a fetch + a Claude distil call, "
                "and every merge lands in a topic file that must stay readable in one go "
                "(~8k tokens). Flip a verdict, change a target, or delete a row.\n\n")
        f.write(f"Then: `python3 pipeline/run-ingest.py run --plan {out}`\n\n")
        f.write("| Verdict | ID | Title | Len | Target | Reason |\n")
        f.write("|---|---|---|---|---|---|\n")
        for depth, title, url in rows:
            indent = "· " * depth
            f.write(f"| {args.verdict} | {url} | {indent}{title} | article | "
                    f"{args.target} | Learn: {section_title} |\n")

    print(f"Plan written: {out}")
    print(f"  {len(rows)} article(s) under '{section_title}' — "
          f"{n_keep} KEEP / {len(rows)-n_keep} SKIP")
    print(f"  Prune it, then: python3 {os.path.join('pipeline','run-ingest.py')} "
          f"run --plan {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
