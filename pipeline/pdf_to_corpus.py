#!/usr/bin/env python3
"""
pdf_to_corpus — a Microsoft Learn PDF export → per-article markdown for the KB.

Learn's "download as PDF" gives the whole doc set as one file (dev-itpro is ~10.8k
pages). That is unusable as a single blob: `kb` chunks per file and reports the file
path as the hit, so one 275MB document would return "page 4,213 of the PDF" and tell
you nothing. This splits it back into articles.

Splitting rule: Learn renders every article with a title line followed by
`Article • MM/DD/YYYY`. That byline is the reliable article boundary — headings alone
are not, since body headings look identical.

FILTERING MATTERS MORE THAN THE SPLIT. The export is mostly history: release notes,
hotfix lists and "what's new in wave N" pages going back years. Indexing that whole
is a known failure here — raw transcripts once out-competed good content in KB search
until they were distilled, and pre-AL-era material poisons a current AL reference. So
release/update/deprecation-history articles are dropped by default. --keep-releases
retains them if you actually want the archive.

Output: one .md per article, with a source byline, under --out.

Usage:
  pdf_to_corpus.py --pdf ~/Documents/dynamics365-business-central-dev-itpro.pdf \\
                   --out /mnt/rojaws/refs/bc-devitpro [--keep-releases] [--limit N]
"""
from __future__ import annotations

import argparse
import hashlib
import os
import re
import subprocess
import sys

# "Article • 04/01/2024" — the byline Learn puts under every article title.
BYLINE = re.compile(r"^Article\s*•\s*(\d{2}/\d{2}/\d{4})\s*$")

# Titles that are release history rather than reference material.
NOISE = re.compile(
    r"(release wave|update \d+\.\d+|hotfix|what's new|whats new|deprecated features?"
    r"|removed features?|breaking changes in|cumulative update|release notes"
    r"|available now|preview of|blog|roadmap)", re.I)


def pdf_text(pdf: str) -> str:
    """pdftotext with layout off — we want reading order, not columns."""
    for tool in (["pdftotext", "-q", pdf, "-"],):
        try:
            r = subprocess.run(tool, capture_output=True, text=True, timeout=3600)
            if r.returncode == 0 and r.stdout.strip():
                return r.stdout
        except FileNotFoundError:
            continue
    raise SystemExit("ERROR: pdftotext not available (install poppler-utils)")


def split_articles(text: str):
    """Yield (title, date, body). The title is the last non-empty line before a byline."""
    lines = text.splitlines()
    marks = []                       # (byline_index, title, date, title_start)
    for i, ln in enumerate(lines):
        m = BYLINE.match(ln.strip())
        if not m:
            continue
        # Learn WRAPS a long title across several lines, and the article always starts
        # a new page — so the form feed is the reliable anchor. Take every line from the
        # \f-bearing line down to the byline and join them. Grabbing only the last line
        # (the obvious approach) yields tails like "wave 2", which both mislabels the
        # article and makes the release-note filter miss it.
        start = i
        for j in range(i - 1, max(-1, i - 12), -1):
            if "\f" in lines[j]:
                start = j
                break
            if not lines[j].strip():        # blank before any \f: stop, take what we have
                start = j + 1
                break
            start = j
        parts = [lines[j].replace("\f", "").strip() for j in range(start, i)]
        title = " ".join(p for p in parts
                         if p and not p.isdigit() and "Microsoft Learn" not in p)
        marks.append((i, title or f"untitled-{i}", m.group(1), start))
    for n, (i, title, date, tstart) in enumerate(marks):
        end = marks[n + 1][3] if n + 1 < len(marks) else len(lines)
        body = "\n".join(lines[i + 1:end]).strip()
        yield title, date, body


def slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:80] or "untitled"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--pdf", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--keep-releases", action="store_true",
                    help="keep release-note/what's-new articles (dropped by default)")
    ap.add_argument("--min-chars", type=int, default=400,
                    help="skip stubs shorter than this (default 400)")
    ap.add_argument("--limit", type=int, help="stop after N kept articles (smoke test)")
    args = ap.parse_args()

    print(f"extracting text from {os.path.basename(args.pdf)} ...", flush=True)
    text = pdf_text(args.pdf)
    print(f"  {len(text):,} chars")

    os.makedirs(args.out, exist_ok=True)
    kept = dropped_noise = dropped_short = dropped_dupe = 0
    seen: dict[str, int] = {}
    # Learn lists an article under every TOC node it belongs to, so the PDF repeats it
    # verbatim — 242 of 869 on the dev-itpro export. Duplicates cost embedding time and
    # return the same hit several times, so dedupe on body hash, not on title.
    bodies: set[str] = set()

    for title, date, body in split_articles(text):
        if not args.keep_releases and NOISE.search(title):
            dropped_noise += 1
            continue
        if len(body) < args.min_chars:
            dropped_short += 1
            continue
        h = hashlib.sha256(body.encode("utf-8", "replace")).hexdigest()
        if h in bodies:
            dropped_dupe += 1
            continue
        bodies.add(h)
        base = slug(title)
        seen[base] = seen.get(base, 0) + 1
        name = base if seen[base] == 1 else f"{base}-{seen[base]}"
        with open(os.path.join(args.out, f"{name}.md"), "w", encoding="utf-8") as f:
            f.write(f"# {title}\n\n"
                    f"- **Source:** Microsoft Learn — Business Central dev-itpro (PDF export)\n"
                    f"- **Article date:** {date}\n\n---\n\n{body}\n")
        kept += 1
        if args.limit and kept >= args.limit:
            break

    print(f"\nwrote {kept} article(s) -> {args.out}")
    print(f"  dropped {dropped_noise} release/history, {dropped_dupe} duplicates, "
          f"{dropped_short} stubs")
    if not args.keep_releases:
        print("  (--keep-releases to retain the history pages)")
    return 0 if kept else 1


if __name__ == "__main__":
    sys.exit(main())
