#!/usr/bin/env python3
"""kb_lint.py — hygiene pass over the Claude memory-wiki (Karpathy-style `lint` op).

Deterministic checks (no model needed):
  - wikilink drift: [[X]] that resolves to a note but not by its canonical `name` slug
    (underscore-for-hyphen, or dropped type-prefix) — `--fix-links` rewrites to canonical.
  - dead links: [[X]] resolving to no note (with a best-guess suggestion).
  - orphans: notes never linked from any other note.
  - index drift: notes missing from MEMORY.md, or MEMORY.md rows pointing at missing files.

Index handling is report-only by default: MEMORY.md carries hand-curated titles/order that a
blind regen would destroy (frontmatter has only name+description, no title). Use --append-missing
to append stub rows for notes absent from the index; never rewrites existing rows.

Optional --semantic shells out to `probe` (pi + Larry, no egress) to flag stale/contradictory
notes — advisory only.

Usage:
  kb_lint.py [--dir DIR] [--report] [--fix-links] [--append-missing] [--semantic]
"""
import argparse, os, re, sys, subprocess

DEFAULT_DIR = os.path.expanduser("~/.claude/projects/-mnt-rojaws-localDev/memory")
PREFIX_RE = re.compile(r"^(project|reference|feedback)[-_]")
LINK_RE   = re.compile(r"\[\[([^\]]+)\]\]")
NAME_RE   = re.compile(r"^name:\s*(.+?)\s*$", re.M)
DESC_RE   = re.compile(r"^description:\s*(.+?)\s*$", re.M)

def norm(s):                       # canonical comparison key
    return PREFIX_RE.sub("", s.strip().lower().replace("_", "-"))

def load_notes(d):
    notes = {}                     # file -> {name, desc}
    for fn in sorted(os.listdir(d)):
        if not fn.endswith(".md") or fn == "MEMORY.md":
            continue
        text = open(os.path.join(d, fn), encoding="utf-8").read()
        fm = text.split("---", 2)
        head = fm[1] if len(fm) >= 3 and text.startswith("---") else ""
        nm = NAME_RE.search(head)
        ds = DESC_RE.search(head)
        notes[fn] = {"name": nm.group(1).strip() if nm else os.path.splitext(fn)[0],
                     "desc": ds.group(1).strip() if ds else "", "text": text}
    return notes

def build_resolver(notes):
    canon = {}                     # canonical name -> file
    variants = {}                  # comparison key -> canonical name
    # pass 1: `name` slug variants (highest priority)
    for fn, meta in notes.items():
        name = meta["name"]
        canon[name] = fn
        for key in {name.lower(), name.lower().replace("-", "_"), norm(name)}:
            variants.setdefault(key, name)
    # pass 2: filename-stem variants (catch links that target the file, not the name slug)
    for fn, meta in notes.items():
        stem = os.path.splitext(fn)[0]
        for key in {stem.lower(), stem.lower().replace("_", "-"), norm(stem)}:
            variants.setdefault(key, meta["name"])
    return canon, variants

def resolve(link, canon, variants):
    for key in (link, link.lower(), link.lower().replace("_", "-"), norm(link)):
        if key in canon:
            return canon[key], key   # exact canonical
    for key in (link.lower(), link.lower().replace("_", "-"), norm(link)):
        if key in variants:
            return canon[variants[key]], variants[key]
    return None, None

def lint(d, fix_links=False, append_missing=False, semantic=False):
    notes = load_notes(d)
    canon, variants = build_resolver(notes)
    referenced = set()
    dead, drift = [], []           # (file, link) / (file, link, canonical)

    for fn, meta in notes.items():
        body = meta["text"]
        new_body = body
        for link in set(LINK_RE.findall(body)):
            target, _ = resolve(link, canon, variants)
            if target is None:
                dead.append((fn, link))
                continue
            referenced.add(target)
            canonical = notes[target]["name"]
            if link != canonical:
                drift.append((fn, link, canonical))
                if fix_links:
                    new_body = new_body.replace(f"[[{link}]]", f"[[{canonical}]]")
        if fix_links and new_body != body:
            open(os.path.join(d, fn), "w", encoding="utf-8").write(new_body)

    orphans = [fn for fn in notes if fn not in referenced]

    # index (MEMORY.md) drift — report only
    idx_path = os.path.join(d, "MEMORY.md")
    idx_files, missing_from_idx, idx_ghosts = set(), [], []
    if os.path.exists(idx_path):
        idx = open(idx_path, encoding="utf-8").read()
        idx_files = set(re.findall(r"\]\(([^)]+\.md)\)", idx))
        missing_from_idx = [fn for fn in notes if fn not in idx_files]
        idx_ghosts = [f for f in idx_files if f not in notes and f != "MEMORY.md"]
        if append_missing and missing_from_idx:
            with open(idx_path, "a", encoding="utf-8") as fh:
                fh.write("\n<!-- kb-lint: notes missing from index (edit titles) -->\n")
                for fn in missing_from_idx:
                    fh.write(f"- [{notes[fn]['name']}]({fn}) — {notes[fn]['desc']}\n")

    # ---- report
    def section(title, rows):
        print(f"\n## {title} ({len(rows)})")
        for r in rows:
            print("  " + r)
    print(f"# kb-lint — {d}\n{len(notes)} notes")
    section("dead links", [f"{fn}: [[{lk}]]  (no matching note)" for fn, lk in dead])
    action = "FIXED" if fix_links else "would fix"
    section(f"wikilink drift ({action} -> canonical)",
            [f"{fn}: [[{lk}]] -> [[{cn}]]" for fn, lk, cn in drift])
    section("orphan notes (no inbound links)", sorted(orphans))
    section("missing from MEMORY.md" + (" (APPENDED)" if append_missing else ""),
            sorted(missing_from_idx))
    section("MEMORY.md rows pointing at missing files", sorted(idx_ghosts))

    if semantic:
        print("\n## semantic review (probe / pi @ Larry — advisory)")
        probe = os.path.join(os.path.dirname(os.path.abspath(__file__)), "probe")
        q = ("List any notes that look STALE or CONTRADICTORY: describe something retired, "
             "obsolete, abandoned, or superseded, or that conflicts with another note. "
             "Cite file:line. Be concise.")
        try:
            subprocess.run([probe, d, "-q", q], check=False)
        except Exception as e:
            print(f"  (probe unavailable: {e})")

def main():
    ap = argparse.ArgumentParser(prog="kb-lint")
    ap.add_argument("--dir", default=DEFAULT_DIR)
    ap.add_argument("--report", action="store_true", help="report only (default)")
    ap.add_argument("--fix-links", action="store_true", help="rewrite drifted [[links]] to canonical")
    ap.add_argument("--append-missing", action="store_true", help="append index stubs for un-indexed notes")
    ap.add_argument("--semantic", action="store_true", help="run probe for stale/contradiction review")
    a = ap.parse_args()
    if not os.path.isdir(a.dir):
        print(f"ERROR: not a dir: {a.dir}", file=sys.stderr); sys.exit(1)
    lint(a.dir, fix_links=a.fix_links, append_missing=a.append_missing, semantic=a.semantic)

if __name__ == "__main__":
    main()
