#!/usr/bin/env python3
"""Anonymise an AL knowledge export (or any text file).

Structural redactions (GUIDs, user paths, host) are baked in. All NAME
replacements — company, person, customer, vendor — are loaded from a LOCAL map
file that is NOT committed, so no real names live in the repo.

Map file: one rule per line, `regex<TAB>replacement` (blank lines / # comments
ignored). Rules apply in order, case-insensitive, global. Put longer / more
specific patterns first. See al-anon-map.example.txt.

Usage:
  anonymise.py <in> <out>                     # map: $AL_ANON_MAP or default path
  AL_ANON_MAP=/path/map.txt anonymise.py a b
"""
import os, re, sys

DEFAULT_MAP = os.environ.get(
    "AL_ANON_MAP", "/mnt/rojaws/localDev/al_merge/al-anon-map.txt")

# structural rules — safe to commit (no names)
STRUCTURAL = [
    (r'\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\b', '<guid>'),
    (r'9213-[A-Z]+', '<host>'),
    (r'/mnt/c/[Uu]sers/[^/\s"]+', '/mnt/c/users/<user>'),
    (r'C:\\\\Users\\\\[^\\\s"]+', r'C:\\Users\\<user>'),
]


def load_map(path):
    rules = []
    if not os.path.exists(path):
        sys.stderr.write(f"WARN: name map not found at {path} — only structural redaction applied.\n")
        return rules
    for ln in open(path, encoding="utf-8"):
        ln = ln.rstrip("\n")
        if not ln.strip() or ln.lstrip().startswith("#"):
            continue
        if "\t" not in ln:
            sys.stderr.write(f"skip (no TAB): {ln!r}\n"); continue
        pat, rep = ln.split("\t", 1)
        rules.append((pat, rep))
    return rules


def anonymise(text, name_rules):
    for pat, rep in STRUCTURAL:
        text = re.sub(pat, rep, text)
    for pat, rep in name_rules:
        text = re.sub(pat, rep, text, flags=re.I)
    return text


def main():
    if len(sys.argv) < 3:
        sys.exit("usage: anonymise.py <in> <out> [map]")
    src, dst = sys.argv[1], sys.argv[2]
    mp = sys.argv[3] if len(sys.argv) > 3 else DEFAULT_MAP
    rules = load_map(mp)
    text = open(src, encoding="utf-8", errors="replace").read()
    open(dst, "w", encoding="utf-8").write(anonymise(text, rules))
    print(f"anonymised {src} -> {dst}  ({len(rules)} name rules from {mp})")


if __name__ == "__main__":
    main()
