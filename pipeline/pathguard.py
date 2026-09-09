"""pathguard — the single place a model- or handover-supplied path becomes a real path.

Every path the pipeline writes to originates in text a model produced (a SEARCH/REPLACE
block's `File:` line, an edit task's file list) or a human wrote into a handover manifest.
None of it is trustworthy input. Before this module there was NO containment anywhere in
the pipeline — `grep -rn "commonpath\\|realpath" pipeline/` returned nothing — and
`snippet_fix.apply_edit_blocks` explicitly honoured absolute paths:

    path = rel if os.path.isabs(rel) else os.path.join(project_root, rel)

so a block naming `/tmp/outside.txt` or `../../outside.txt` wrote outside the project.

The edit flow's `enforce_gate()` is NOT a mitigation for this: it reverts by inspecting
`git_status(root)`, so anything written outside the repo is invisible to it and survives.

Containment is enforced on the REALPATH, so a path that is syntactically inside the root
but traverses a symlink pointing out is rejected too.

Use `safe_join()` at every text→path conversion. Do not re-implement the check.
"""
from __future__ import annotations

import os


class PathEscape(ValueError):
    """A supplied path resolved outside the project root (or was absolute)."""


def contains(root: str, candidate: str) -> bool:
    """True if `candidate` resolves inside `root`. Both are realpath'd first, so
    symlink traversal out of the tree is caught rather than trusted."""
    r = os.path.realpath(root)
    c = os.path.realpath(candidate)
    if c == r:
        return True
    try:
        return os.path.commonpath([r, c]) == r
    except ValueError:
        return False          # different drives / unrelated roots


def safe_join(root: str, rel: str) -> str:
    """Resolve `rel` under `root`, or raise PathEscape.

    Absolute paths are rejected outright. There is no legitimate reason for a model to
    name an absolute path in an edit block — the pipeline always works relative to a
    project root, and honouring one is exactly how a write escapes.

    Returns the REALPATH, so callers write to the resolved location and cannot be
    re-pointed by a symlink swapped in between the check and the write.
    """
    if not isinstance(rel, str) or not rel.strip():
        raise PathEscape("empty path")
    rel = rel.strip().strip("`").strip()
    if os.path.isabs(rel):
        raise PathEscape(f"absolute path rejected: {rel}")
    if rel.startswith("~"):
        raise PathEscape(f"home-relative path rejected: {rel}")
    cand = os.path.join(os.path.realpath(root), rel)
    if not contains(root, cand):
        raise PathEscape(f"path escapes project root: {rel}")
    return os.path.realpath(cand)


def is_safe(root: str, rel: str) -> bool:
    """Non-raising form for filtering a list of candidate paths."""
    try:
        safe_join(root, rel)
        return True
    except PathEscape:
        return False


def reject_symlink(path: str) -> None:
    """Raise if `path` is a symlink. Uses lstat semantics — `os.path.isfile()` follows
    links, which is how a tracked symlink could pull an external file into the scrubbed
    enterprise mirror (anon_workspace). Callers that mirror or copy must fail closed on
    an unexpected link rather than silently dereferencing or silently omitting it:
    omission changes what the agent believes the source tree contains.
    """
    if os.path.islink(path):
        raise PathEscape(f"symlink not permitted here: {path}")
