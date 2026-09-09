#!/usr/bin/env python3
"""
learn_drift — watch ingested Microsoft Learn pages for content revisions.

Distilled Learn content is only as current as the fetch, and MS revises these
pages. The transcript archive records WHAT was ingested and WHEN, but nothing
watched for the source moving on — a stale distillation is indistinguishable
from a fresh one. This closes that gap.

Signal: the page's `ms.date` meta tag — the author's content-revision date.
(`updated_at` is recorded too but NOT used for drift: it changes on site
rebuilds with no content change, so alerting on it would cry wolf weekly.)

  baseline   scan reference/transcripts/ for learn.microsoft.com sources,
             fetch each page's ms.date, write reference/.learn-baseline.json
  check      refetch and compare against the baseline; report drift
  check --plan   also write reference/ingest-plan-drift.md for the drifted
                 pages, in the format `run-ingest.py run --plan` consumes

Exit codes for the timer: 0 = no drift, 1 = drift found, 2 = could not check.
Model-free; sequential fetches with a polite delay.

Re-ingest flow when drift is reported:
  python3 pipeline/learn_drift.py check --plan
  python3 pipeline/run-ingest.py run --plan reference/ingest-plan-drift.md --force
  (--force: the drifted transcripts already exist; run-ingest skips existing
   archives otherwise. Delete the stale transcript files instead if you want
   a clean refetch record.)
  python3 pipeline/learn_drift.py baseline     # accept the new state
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys
import time
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.environ.get("LARRY_REPO", os.path.dirname(HERE))
TRANSCRIPTS = os.path.join(REPO, "reference", "transcripts")
BASELINE = os.path.join(REPO, "reference", ".learn-baseline.json")
PLAN = os.path.join(REPO, "reference", "ingest-plan-drift.md")

MS_DATE_RE = re.compile(r'<meta name="ms\.date" content="([^"]+)"')
UPDATED_RE = re.compile(r'<meta name="updated_at" content="([^"]+)"')


def learn_sources():
    """(url, title) for every archived transcript whose source is a Learn page."""
    out = []
    for path in sorted(glob.glob(os.path.join(TRANSCRIPTS, "*.md"))):
        text = open(path, encoding="utf-8").read(2000)
        m = re.search(r"^\- \*\*Source:\*\* (\S+)", text, re.M)
        if not m or "learn.microsoft.com" not in m.group(1):
            continue
        t = re.match(r"# (.+)", text)
        title = (t.group(1) if t else os.path.basename(path)[:-3]).lstrip("· ").strip()
        out.append((m.group(1), title))
    return out


def fetch_dates(url):
    """(ms_date, updated_at) from the page's meta tags, or (None, None)."""
    req = urllib.request.Request(url, headers={"User-Agent": "learn-drift/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=45) as r:
            head = r.read(200_000).decode("utf-8", errors="replace")
    except Exception as e:
        return None, f"fetch failed: {e}"
    ms = MS_DATE_RE.search(head)
    up = UPDATED_RE.search(head)
    if not ms:
        return None, "no ms.date meta tag"
    return ms.group(1), (up.group(1) if up else "")


def cmd_baseline(_args):
    sources = learn_sources()
    if not sources:
        print("no Learn sources in the transcript archive")
        return 2
    state, failed = {}, 0
    for i, (url, title) in enumerate(sources, 1):
        ms, up = fetch_dates(url)
        if ms is None:
            print(f"  [{i}/{len(sources)}] {title}: {up}")
            failed += 1
            continue
        state[url] = {"title": title, "ms_date": ms, "updated_at": up,
                      "recorded": time.strftime("%Y-%m-%d")}
        print(f"  [{i}/{len(sources)}] {title}: {ms[:10]}")
        time.sleep(1)                      # polite to the docs CDN
    with open(BASELINE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, sort_keys=True)
    print(f"\nbaseline written: {os.path.relpath(BASELINE, REPO)} "
          f"({len(state)} pages{f', {failed} failed' if failed else ''})")
    return 0 if state else 2


def cmd_check(args):
    try:
        baseline = json.load(open(BASELINE, encoding="utf-8"))
    except OSError:
        print(f"no baseline at {BASELINE} — run: learn_drift.py baseline")
        return 2
    drifted, failed = [], 0
    for i, (url, rec) in enumerate(sorted(baseline.items()), 1):
        ms, up = fetch_dates(url)
        if ms is None:
            print(f"  [{i}/{len(baseline)}] {rec['title']}: {up}")
            failed += 1
            continue
        if ms != rec["ms_date"]:
            drifted.append((url, rec, ms))
            print(f"  [{i}/{len(baseline)}] {rec['title']}: DRIFTED "
                  f"{rec['ms_date'][:10]} -> {ms[:10]}")
        time.sleep(1)

    print()
    if failed == len(baseline):
        print("could not check any page — network?")
        return 2
    if not drifted:
        print(f"no drift across {len(baseline) - failed} page(s)"
              + (f" ({failed} unreachable)" if failed else ""))
        return 0

    print(f"{len(drifted)} page(s) revised since ingestion:")
    for url, rec, ms in drifted:
        print(f"  {rec['title']}: {rec['ms_date'][:10]} -> {ms[:10]}  {url}")

    if args.plan:
        with open(PLAN, "w", encoding="utf-8") as f:
            f.write("# Ingest plan — drifted Learn pages\n\n"
                    f"Generated by learn_drift.py check --plan on "
                    f"{time.strftime('%Y-%m-%d')}. These pages' `ms.date` moved since "
                    "they were distilled, so the distilled notes may be stale.\n\n"
                    "After running the plan, accept the new state:\n"
                    "`python3 pipeline/learn_drift.py baseline`\n\n"
                    f"{len(drifted)} KEEP / 0 SKIP.\n\n"
                    "| Verdict | ID | Title | Len | Target | Reason |\n"
                    "|---|---|---|---|---|---|\n")
            for url, rec, ms in drifted:
                f.write(f"| KEEP | {url} | {rec['title']} | article | AL-REFERENCE.md "
                        f"| revised {rec['ms_date'][:10]} -> {ms[:10]} |\n")
        print(f"\nplan written: {os.path.relpath(PLAN, REPO)}")
    return 1


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("baseline", help="record current ms.date for every ingested Learn page")
    c = sub.add_parser("check", help="compare against the baseline, report drift")
    c.add_argument("--plan", action="store_true",
                   help="write reference/ingest-plan-drift.md for drifted pages")
    args = ap.parse_args()
    return cmd_baseline(args) if args.cmd == "baseline" else cmd_check(args)


if __name__ == "__main__":
    sys.exit(main())
