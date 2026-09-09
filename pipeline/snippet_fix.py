#!/usr/bin/env python3
"""
snippet_fix — local "Fast Apply": fix compile errors with targeted SEARCH/REPLACE edits
instead of whole-file rewrites.

Local models regress by rewriting entire files (brace cascades, unmasking, working code
made worse). This asks the coder for minimal search/replace blocks and applies them
deterministically — the model never writes files, so it can't cascade. Same idea as
Morph Fast Apply / aider, but local + free + no code leaves the box.

Wired into run-build.py's fix loop when FIX_STRATEGY=snippet (pi backend only). Claude
keeps its own precise Edit tool.

Block format the coder must emit (one or more):

    FILE: src/codeunit/Foo.Codeunit.al
    <<<<<<< SEARCH
    <exact existing lines>
    =======
    <replacement lines>
    >>>>>>> REPLACE
"""
import os
import re

import pathguard

INSTRUCTIONS = """\
Fix ONLY the listed compile errors. Do NOT rewrite files. Output ONE OR MORE edit blocks
in EXACTLY this format and nothing else (no prose, no code fences):

FILE: <relative/path/from/project/root>
<<<<<<< SEARCH
<the exact existing lines to replace — copy them verbatim from the file, incl. indentation>
=======
<the corrected lines>
>>>>>>> REPLACE

Rules:
- The SEARCH text MUST match the current file content exactly (whitespace included).
- Keep each SEARCH block small — just the lines around the error, not the whole procedure.
- One block per distinct edit. Multiple blocks per file are fine.
- Do not touch files or lines that have no listed error."""

# NOTE: replace may be EMPTY (a deletion). The terminator is line-anchored; an
# earlier version required a line between ======= and >>>>>>> REPLACE, so an empty
# replacement made .*? swallow the next block's terminator and wrote raw protocol
# text into the file (BCCalendarJsDemo task 17, 2026-07-12).
_BLOCK = re.compile(
    r"^FILE:\s*(?P<path>[^\n]+)\n"
    r"<{5,}\s*SEARCH[ \t]*\n(?P<search>.*?)\n={5,}[ \t]*\n(?P<replace>.*?)^>{5,}\s*REPLACE",
    re.DOTALL | re.MULTILINE)


def build_snippet_prompt(project_root, findings, file_listing):
    """Prompt asking the coder to emit SEARCH/REPLACE edit blocks (read-only run)."""
    return (
        f"Project root: {project_root}/\n\n"
        f"Current source files:\n{file_listing}\n\n"
        f"Read the files you need with your read tool. The build has these errors:\n\n"
        f"{findings}\n\n---\n\n{INSTRUCTIONS}")


def _norm(s):
    """Whitespace-tolerant key: strip trailing ws per line (models fumble trailing space)."""
    return "\n".join(ln.rstrip() for ln in s.split("\n"))


def apply_edit_blocks(text, project_root):
    """Apply SEARCH/REPLACE blocks from `text` to files under project_root.

    Returns (applied, failed, details). Exact match first, then a trailing-whitespace-
    tolerant match. A block whose SEARCH is not found is a failure (model hallucinated
    context) — reported, not force-applied.
    """
    applied, failed, details = 0, 0, []
    for m in _BLOCK.finditer(text):
        rel = m.group("path").strip().strip("`").strip()
        search, replace = m.group("search"), m.group("replace")
        if replace.endswith("\n"):      # line-anchored terminator leaves one trailing \n
            replace = replace[:-1]
        # Containment BEFORE touching the filesystem. This line previously honoured
        # absolute paths outright, so a block naming /tmp/x or ../../x wrote outside the
        # project — and the edit flow's enforce_gate() cannot revert that, because it
        # only inspects git status INSIDE the repo. See pathguard.
        try:
            path = pathguard.safe_join(project_root, rel)
        except pathguard.PathEscape as e:
            failed += 1; details.append(f"REJECTED (escapes root): {rel} — {e}"); continue
        try:
            content = open(path).read()
        except OSError:
            failed += 1; details.append(f"no file: {rel}"); continue
        if search in content:
            open(path, "w").write(content.replace(search, replace, 1))
            applied += 1; details.append(f"applied: {rel}")
            continue
        # trailing-whitespace-tolerant fallback
        nmap = _norm(content)
        nsearch = _norm(search)
        if nsearch in nmap:
            # rebuild: replace on the normalized copy, but we must edit real content.
            # find the real span by matching line-by-line ignoring trailing ws.
            clines, slines = content.split("\n"), search.split("\n")
            hit = _find_span(clines, slines)
            if hit is not None:
                i, j = hit
                new = clines[:i] + replace.split("\n") + clines[j:]
                open(path, "w").write("\n".join(new))
                applied += 1; details.append(f"applied~ (ws-tolerant): {rel}")
                continue
        # Indentation/blank-line tolerant, unique match only. Recovers the common case
        # where the model quotes the right lines but re-indents them.
        clines = content.split("\n")
        hit = _find_span_indent(clines, search.split("\n"))
        if hit is not None:
            i, j = hit
            new = clines[:i] + _reindent(replace, clines, i) + clines[j:]
            open(path, "w").write("\n".join(new))
            applied += 1
            details.append(f"applied~ (indent-tolerant): {rel}")
            continue
        first = next((x.strip() for x in search.split("\n") if x.strip()), "")[:60]
        failed += 1
        details.append(f"SEARCH not found in {rel}: {first!r}")
    return applied, failed, details


def _find_span(clines, slines):
    """First index range [i,j) in clines matching slines ignoring trailing whitespace."""
    n, k = len(clines), len(slines)
    sn = [x.rstrip() for x in slines]
    for i in range(n - k + 1):
        if [x.rstrip() for x in clines[i:i + k]] == sn:
            return i, i + k
    return None


def _find_span_indent(clines, slines):
    """Match ignoring INDENTATION as well as trailing space, and ignoring blank lines.

    Half the fix rounds on the hard fixture applied zero edits: the model reproduces the
    right lines but re-indents them, or drops/adds a blank line. Both are cosmetic, and
    refusing them costs a whole round. Requires a UNIQUE match — several candidates means
    we cannot tell which the model meant, and a wrong edit is worse than no edit.
    Returns (i, j) over the ORIGINAL lines, or None.
    """
    def sig(xs):
        return [x.strip() for x in xs if x.strip()]

    s_sig = sig(slines)
    if len(s_sig) < 2:          # a single line is too weak an anchor to re-locate safely
        return None
    hits, n = [], len(clines)
    for i in range(n):
        j, m = i, 0
        while j < n and m < len(s_sig):
            if not clines[j].strip():        # skip blank lines in the file
                j += 1
                continue
            if clines[j].strip() != s_sig[m]:
                break
            j += 1
            m += 1
        if m == len(s_sig):
            hits.append((i, j))
            if len(hits) > 1:                # ambiguous — refuse
                return None
    return hits[0] if hits else None


def _reindent(replace, clines, i):
    """Re-apply the file's own indentation to the replacement.

    When SEARCH matched only because indentation was ignored, the REPLACE text carries the
    model's indentation, which would corrupt the file's layout. Shift it by the difference
    between the original first line and the replacement's first line."""
    rl = replace.split("\n")
    orig_ind = len(clines[i]) - len(clines[i].lstrip()) if i < len(clines) else 0
    first = next((x for x in rl if x.strip()), "")
    new_ind = len(first) - len(first.lstrip())
    delta = orig_ind - new_ind
    if delta == 0:
        return rl
    out = []
    for ln in rl:
        if not ln.strip():
            out.append(ln)
        elif delta > 0:
            out.append(" " * delta + ln)
        else:
            out.append(ln[min(-delta, len(ln) - len(ln.lstrip())):])
    return out
