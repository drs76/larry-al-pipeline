#!/usr/bin/env python3
"""bench_env_contract.py — the set of environment variables a benchmark arm owns.

Why this exists
---------------
An A/B arm must POSITIVELY establish the configuration it claims to measure.
"Control" previously meant "do not add escalation variables", which in an
inherited shell (.zshenv exports ESCALATE_MID_AFTER / ESCALATE_AFTER /
MID_MODEL) is not the same thing as "run without escalation". The suite5-mid
doclink A/B was voided by exactly that: both nominal arms were armed.

The fix is not a hand-written list of the three variables that happened to bite.
run-build.py and its pipeline modules read ~50 variables — models, RAG, workflow,
review, escalation, egress policy — any of which can leak from the parent shell
and silently redefine an arm. So the contract is DERIVED, not curated:

  sanitize = {every env var run-build.py and its local imports read} - PRESERVE

PRESERVE holds only tool locators and infrastructure endpoints (where a binary
lives, which ollama to warm). Those are properties of the machine, not of the
experiment; clearing them would break the run without making it more isolated.
Everything else is experimental surface: cleared from the child environment, so
an arm that wants it must declare it.

Deriving it means the contract cannot drift. A new knob added to run-build.py is
in the sanitize set the day it lands, with no benchmark change.

Usage:
  bench_env_contract.py --names          # space-separated names to clear
  bench_env_contract.py --json           # contract + the ambient values found now
"""

import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# Entry point plus the local modules it pulls in. Harvest follows imports one
# level: run-build.py's own reads plus every pipeline module it imports.
ROOT_SCRIPT = "run-build.py"

# Machine facts, not experiment inputs. Clearing these breaks the run and
# isolates nothing — a different pi binary is not a different treatment.
PRESERVE = {
    "PI_BIN", "CLAUDE_BIN", "AL_CLI", "KB_BIN", "LARRY_REPO",
    "BCQUALITY_ROOT", "PROBE_ROOT", "OLLAMA_WARM_URL", "BONSAI_HEALTH_URL",
    "LARRY_DASH_URL", "LARRY_DASH_AUTH", "BUILD_METRICS", "TRANSCRIPTS",
    "YTDLP",
}

# The suite sets these itself, per run. Listed so --json can show that the arm
# establishes them rather than inheriting them.
SUITE_OWNED = {"PI_CODER_MODEL", "CODER_BACKEND", "MAX_FIX_ROUNDS", "FIXTURE_DIR"}

_ENV_READ = re.compile(r"""(?:environ\.get\(|environ\[|getenv\()\s*["']([A-Z][A-Z0-9_]{2,})["']""")
_IMPORT = re.compile(r"^\s*(?:import|from)\s+([a-z_][a-z0-9_]*)", re.M)


def _read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def _local_modules(text):
    """Imported names that resolve to a .py file in this directory."""
    out = []
    for name in _IMPORT.findall(text):
        cand = os.path.join(HERE, name + ".py")
        if os.path.exists(cand):
            out.append(cand)
    return out


def harvest():
    """Every env var name read by run-build.py or a pipeline module it imports."""
    root = os.path.join(HERE, ROOT_SCRIPT)
    text = _read(root)
    files = [root] + _local_modules(text)
    names = set()
    for f in files:
        try:
            names |= set(_ENV_READ.findall(_read(f)))
        except OSError:
            continue
    return names


def sanitize_set():
    return sorted(harvest() - PRESERVE)


def contract():
    names = sanitize_set()
    return {
        "sanitized": names,
        "preserved": sorted(PRESERVE),
        "suite_owned": sorted(SUITE_OWNED),
        # What was actually inherited at contract time. Recorded per suite run so a
        # contaminated shell is evidence in the log, not an archaeology exercise later.
        "ambient_found": {n: os.environ[n] for n in names if n in os.environ},
    }


if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else "--names"
    if arg == "--json":
        print(json.dumps(contract(), indent=2))
    elif arg == "--names":
        print(" ".join(sanitize_set()))
    else:
        sys.exit(f"usage: {sys.argv[0]} [--names|--json]")
