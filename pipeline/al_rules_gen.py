#!/usr/bin/env python3
"""al_rules_gen.py — emit AL_RULES.md from the reference, so it cannot drift.

WHY THIS EXISTS
---------------
`~/.claude/AL_RULES.md` on the Windows workstation was hand-written, untracked, and loaded
into EVERY Claude session there. By 2026-08-28 it was 4.3 months old and contradicted
`reference/al-reference/` on variable order, abbreviations, `Find('-')` and `NoImplicitWith`
— while three copies of it had already diverged from each other.

A hand-maintained restatement of a reference that moves weekly is a drift generator. So this
file is DERIVED: everything except the house addendum comes from `al-reference/`, and
regenerating is the only supported way to change it.

    python3 al_rules_gen.py            # emit reference/AL_RULES.md
    python3 al_rules_gen.py --check    # exit 1 if the emitted file is stale or missing

RUN IT AFTER EVERY INGEST. That is the standing cost of keeping the file self-contained
rather than replacing it with a pointer; `--check` in a hook makes the cost visible instead
of silent.

IT REFUSES RATHER THAN EMITS A PARTIAL RULESET
----------------------------------------------
If the house addendum still carries `TODO(grounding)` markers, this exits non-zero and writes
nothing. A ruleset that looks complete and silently omits the house rules is worse than no
file at all — the reader cannot tell the difference, and this whole exercise started because
a confident-looking ruleset was wrong.
"""

import hashlib
import os
import re
import sys
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
REF = os.path.join(REPO, "reference")

GOTCHAS = os.path.join(REF, "al-reference", "00-gotchas.md")
SYNTAX = os.path.join(REF, "al-reference", "01-syntax-style.md")
ADDENDUM = os.path.join(REF, "house-addendum.md")
OUT = os.path.join(REF, "AL_RULES.md")

SOURCES = [GOTCHAS, SYNTAX, ADDENDUM]
STAMP = "<!-- al_rules_gen: sources "        # provenance line, parsed back by --check


def _read(path):
    if not os.path.exists(path):
        sys.exit(f"al_rules_gen: missing source {path}")
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def _fingerprint():
    """Hash of every source, so --check can tell 'stale' from 'up to date'."""
    h = hashlib.sha256()
    for p in SOURCES:
        h.update(_read(p).encode("utf-8"))
    return h.hexdigest()[:16]


def _body(text):
    """Drop a topic file's H1 and its index-facing preamble, keep the rules."""
    lines = text.split("\n")
    out, seen_h2 = [], False
    for ln in lines:
        if ln.startswith("## "):
            seen_h2 = True
        if seen_h2:
            out.append(ln)
    return "\n".join(out).strip() or text.strip()


def _unfilled(addendum):
    """Every TODO(grounding) marker still in the addendum."""
    return re.findall(r"TODO\(grounding\):\s*(.+)", addendum)


def build():
    gotchas, syntax, addendum = (_read(p) for p in SOURCES)

    todos = _unfilled(addendum)
    if todos:
        print("al_rules_gen: REFUSING to emit — the house addendum is still a stub.",
              file=sys.stderr)
        print(f"  {len(todos)} unfilled section(s) in {os.path.relpath(ADDENDUM, REPO)}:",
              file=sys.stderr)
        for t in todos:
            print(f"    - {t[:96]}", file=sys.stderr)
        print("\n  The content lives on the Windows workstation's ~/.claude/AL_RULES.md and",
              file=sys.stderr)
        print("  exists nowhere on this box. See tower/HANDOFF-deb-al-ruleset-and-clients.md §4.",
              file=sys.stderr)
        print("\n  Emitting a ruleset that silently omits the house rules would look complete",
              file=sys.stderr)
        print("  and be wrong — which is the failure this generator replaces.", file=sys.stderr)
        return 1

    # Forward slashes ALWAYS. os.path.relpath yields backslashes on Windows, which are
    # broken markdown links (backslash is the escape character) and make the generated
    # file differ by platform — so it churned in git every time the other box ran it.
    def rel(p):
        return os.path.relpath(p, REPO).replace(os.sep, "/")
    out = [
        "# AL rules — house ruleset",
        "",
        f"{STAMP}{_fingerprint()} generated {date.today().isoformat()} -->",
        "",
        "> **GENERATED FILE — do not edit.** Regenerate with",
        "> `python3 pipeline/al_rules_gen.py` after any change to the sources below.",
        "> Editing this file directly recreates the drift it exists to prevent.",
        "",
        "| Source | Owns |",
        "|---|---|",
        f"| [`{rel(GOTCHAS)}`]({rel(GOTCHAS)}) | the gotchas, several runtime-verified |",
        f"| [`{rel(SYNTAX)}`]({rel(SYNTAX)}) | formatting, naming, variables, abbreviations |",
        f"| [`{rel(ADDENDUM)}`]({rel(ADDENDUM)}) | house rules, hand-written |",
        "",
        "Search the full reference instead of guessing: `kb search \"<question>\" --corpus al-reference`.",
        "",
        "---",
        "",
        "# Gotchas — read first",
        "",
        _body(gotchas),
        "",
        "---",
        "",
        "# Syntax and style",
        "",
        _body(syntax),
        "",
        "---",
        "",
        # Explicit header: _body() strips the addendum's own H1, and without this the
        # House rules run on from the reference with no visible boundary. Which side a rule
        # comes from is exactly what the reader needs to know.
        "# house rules",
        "",
        "Hand-written, and the only part of this file that is not derived from the reference.",
        "",
        _body(addendum),
        "",
    ]
    return "\n".join(out) + "\n"


def main():
    check = "--check" in sys.argv[1:]
    built = build()
    if built == 1:
        return 1

    if check:
        if not os.path.exists(OUT):
            print(f"al_rules_gen: {os.path.relpath(OUT, REPO)} has never been generated",
                  file=sys.stderr)
            return 1
        cur = _read(OUT)
        want = f"{STAMP}{_fingerprint()}"
        if want not in cur:
            print("al_rules_gen: STALE — a source changed since this was generated. "
                  "Re-run `python3 pipeline/al_rules_gen.py`.", file=sys.stderr)
            return 1
        print("al_rules_gen: up to date")
        return 0

    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(built)
    print(f"wrote {os.path.relpath(OUT, REPO)} ({len(built.splitlines())} lines, "
          f"sources {_fingerprint()})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
