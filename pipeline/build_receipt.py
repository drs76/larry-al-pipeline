"""build_receipt — proof that THIS tree passed the referee, checked at promote time.

`alw promote` used to check only that the prototype directory existed and the
destination did not, then `mv` it. It could not tell a validated tree from one that had
never been built, had been built without the analyzers, or had been edited afterwards —
so "promote" asserted nothing about quality at all.

A receipt is written next to the project on a successful build and re-checked by
promote. It is deliberately tied to a TREE HASH, not a timestamp: the interesting
failure is not a stale receipt sitting next to an old tree, it is a receipt that is
genuinely recent while the source has moved on since.

Fail closed: no receipt, unreadable receipt, hash mismatch, bare-compile-only result, or
review-required-without-independent-review all block promotion.

Written by the run-build orchestrators; read by the promote path in alw/gow/csw.
"""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import time

RECEIPT_NAME = ".build-receipt.json"

# Files whose content defines "the tree that passed". Extensions are per-language; the
# union is fine — a project only contains its own kinds.
_SOURCE_EXTS = (".al", ".js", ".css", ".html", ".go", ".cs", ".fs", ".csproj", ".fsproj",
                ".json", ".mod", ".sum", ".sln")


def tree_hash(root: str) -> str:
    """Stable SHA-256 over the project's source tree (path + content, sorted).

    Excludes build output and dependency caches — .alpackages, bin/obj and the receipt
    itself change without the source changing, and hashing them would make every
    receipt instantly stale.
    """
    h = hashlib.sha256()
    skip_dirs = {".git", ".alpackages", "bin", "obj", "node_modules", ".vscode", "runs"}
    for dp, dirs, fs in os.walk(root):
        dirs[:] = sorted(d for d in dirs if d not in skip_dirs)
        for fn in sorted(fs):
            if fn == RECEIPT_NAME or not fn.endswith(_SOURCE_EXTS):
                continue
            p = os.path.join(dp, fn)
            rel = os.path.relpath(p, root)
            try:
                with open(p, "rb") as f:
                    body = f.read()
            except OSError:
                continue
            h.update(rel.encode())
            h.update(b"\0")
            h.update(hashlib.sha256(body).hexdigest().encode())
            h.update(b"\n")
    return h.hexdigest()


def _pipeline_rev() -> str:
    try:
        r = subprocess.run(["git", "rev-parse", "--short", "HEAD"],
                           cwd=os.path.dirname(os.path.abspath(__file__)),
                           capture_output=True, text=True, timeout=10)
        return r.stdout.strip() or "unknown"
    except Exception:
        return "unknown"


def write(root: str, *, referee_ok: bool, analyzers, tests_ok=None,
          review_mode="none", review_ok=None, review_independent=None,
          bare_compile_only=False, coder_model="", extra=None) -> str:
    """Write the receipt for `root`. Returns its path."""
    rec = {
        "project": os.path.basename(root.rstrip("/")),
        "tree_hash": tree_hash(root),
        "referee_ok": bool(referee_ok),
        "analyzers": list(analyzers or []),
        "bare_compile_only": bool(bare_compile_only),
        "tests_ok": tests_ok,
        "review_mode": review_mode,
        "review_ok": review_ok,
        "review_independent": review_independent,
        "coder_model": coder_model,
        "pipeline_rev": _pipeline_rev(),
        "ts": time.strftime("%Y-%m-%dT%H:%M:%S"),
    }
    if extra:
        rec.update(extra)
    path = os.path.join(root, RECEIPT_NAME)
    with open(path, "w") as f:
        json.dump(rec, f, indent=2, sort_keys=True)
    return path


def verify(root: str, *, require_review=False, require_tests=False):
    """(ok, reason, receipt) — may this tree be promoted?

    require_review reflects the caller's policy: with it set, an advisory or
    non-independent review is not sufficient.

    require_tests likewise: `tests_ok` is None when tests were never enabled, and None
    must not read as True. A caller asking for tested code has to be told the difference
    between "tests passed" and "nobody ran any".
    """
    path = os.path.join(root, RECEIPT_NAME)
    try:
        with open(path) as f:
            rec = json.load(f)
    except FileNotFoundError:
        return False, ("no build receipt — this tree has never completed a verified "
                       "build (run `build` before `promote`)"), None
    except (OSError, ValueError) as e:
        return False, f"unreadable build receipt: {e}", None

    if not rec.get("referee_ok"):
        return False, "receipt records a FAILED referee", rec
    if rec.get("bare_compile_only"):
        return False, ("receipt is bare-compile-only (required analyzers were missing) "
                       "— not a full referee pass"), rec

    actual = tree_hash(root)
    if actual != rec.get("tree_hash"):
        return False, ("tree has changed since the build that produced this receipt "
                       f"(receipt {str(rec.get('tree_hash'))[:12]}…, now {actual[:12]}…) "
                       "— rebuild before promoting"), rec

    if require_review:
        if not rec.get("review_ok"):
            return False, "review required but the receipt records no passing review", rec
        if rec.get("review_independent") is False:
            return False, ("review was NOT independent (reviewer was the coder model) — "
                           "re-run with a different COMS_VALIDATOR_MODEL"), rec

    if require_tests:
        if rec.get("tests_ok") is None:
            return False, ("tests required but this build ran none — rebuild with "
                           "AL_RUN_TESTS=1"), rec
        if not rec.get("tests_ok"):
            return False, "receipt records FAILING tests", rec
        if (rec.get("tests") or {}).get("status") == "no-tests":
            return False, ("tests required but the project declares no Subtype=Test "
                           "codeunits"), rec
    return True, "", rec
