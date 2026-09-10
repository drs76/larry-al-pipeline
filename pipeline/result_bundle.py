"""result_bundle — durable, per-round record of what a build actually produced.

WHY THIS EXISTS
---------------
`snapshot_src()` keeps every round's tree in MEMORY, and the final report restores only
the best one. So once a run ends, no intermediate state exists anywhere. Two separate
forensic questions died on that in one session:

  - which construct produced an AL0151 at round 2, when the round-3 repair had already
    overwritten the line (the trigger is still unclassified, and unclassifiable);
  - whether a cascade a hint declined to fire on was genuinely a mid-body declaration —
    answerable only because the hint reads the source AT FIX TIME, not afterwards.

A green or red verdict is not the interesting artefact. The TRAJECTORY is, and it was
being thrown away.

WHERE BUNDLES GO, AND WHY IT MATTERS
------------------------------------
Outside the project tree, always. `clear_project()` wipes `src/` every round and
`cleanup.sh` deletes anything unspecced — a bundle written inside the project is
guaranteed to be destroyed by the very run it is recording. `open_bundle` REFUSES a
destination under the project root rather than trusting the caller to remember.

OPT-IN, AND WHY
---------------
Off unless `RESULT_BUNDLE_DIR` is set. A run with it unset is byte-identical to one
before this module existed, so no measured result changes underneath a benchmark.
`bench_env_contract.py` derives its clear-list from the variables run-build reads, so
suites isolate this knob automatically the day it lands.

Every write is fail-soft: recording a build must never break one.
"""
from __future__ import annotations

import json
import os
import re
import shutil
import time

_DIAG = re.compile(r"error ((?:AL|PTE|AA|AS)\d+)")


def _rel(path, root):
    try:
        return os.path.relpath(path, root)
    except ValueError:
        return os.path.basename(path)


class Bundle:
    """One run's durable record. Methods never raise; they report and carry on."""

    def __init__(self, dest, project_root):
        self.dest = dest
        self.root = project_root
        self.rounds = []
        self.errors = []

    def round(self, n, errs, snap, build_text="", manifest_text="", **meta):
        """Record one round: its sources, its diagnostics and its score."""
        try:
            d = os.path.join(self.dest, f"round-{n:02d}")
            # "tree/" not "src/": the snapshot's relative paths already begin with src/,
            # so joining under another src/ produced round-00/src/src/codeunit/... .
            os.makedirs(os.path.join(d, "tree"), exist_ok=True)
            for path, content in (snap or {}).items():
                rel = _rel(path, self.root)
                out = os.path.join(d, "tree", rel)
                os.makedirs(os.path.dirname(out), exist_ok=True)
                with open(out, "w", encoding="utf-8") as fh:
                    fh.write(content)
            if build_text:
                open(os.path.join(d, "build.txt"), "w", encoding="utf-8").write(build_text)
            if manifest_text:
                open(os.path.join(d, "manifest.txt"), "w", encoding="utf-8").write(manifest_text)
            classes = {}
            for c in _DIAG.findall(build_text or ""):
                classes[c] = classes.get(c, 0) + 1
            row = {"round": n, "error_score": errs, "files": len(snap or {}),
                   "diag_classes": classes, **meta}
            with open(os.path.join(d, "meta.json"), "w", encoding="utf-8") as fh:
                json.dump(row, fh, indent=2, sort_keys=True)
            self.rounds.append(row)
        except Exception as e:                       # fail-soft, always
            self.errors.append(f"round {n}: {e}")

    def close(self, **summary):
        """Write the index. The per-round dirs stand alone if this fails."""
        try:
            idx = {"written": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
                   "project_root": self.root,
                   "rounds": self.rounds,
                   "trajectory": [r.get("error_score") for r in self.rounds],
                   "bundle_errors": self.errors,
                   **summary}
            with open(os.path.join(self.dest, "index.json"), "w", encoding="utf-8") as fh:
                json.dump(idx, fh, indent=2, sort_keys=True)
            return os.path.join(self.dest, "index.json")
        except Exception as e:
            self.errors.append(f"close: {e}")
            return None


def open_bundle(project_root, dest=None, run_name=None):
    """A Bundle, or None when disabled. Refuses a destination inside the project.

    `dest` defaults to $RESULT_BUNDLE_DIR; unset means disabled, which is the default.
    """
    dest = dest or os.environ.get("RESULT_BUNDLE_DIR", "").strip()
    if not dest:
        return None
    root = os.path.realpath(project_root)
    full = os.path.realpath(os.path.join(dest, run_name) if run_name else dest)
    # The bundle must not live where clear_project() and cleanup.sh will destroy it.
    if full == root or full.startswith(root + os.sep):
        print(f"  result-bundle DISABLED: {full} is inside the project root — "
              f"clear_project/cleanup would delete it")
        return None
    try:
        os.makedirs(full, exist_ok=True)
    except OSError as e:
        print(f"  result-bundle DISABLED: cannot create {full} ({e})")
        return None
    print(f"  result-bundle: {full}")
    return Bundle(full, root)
