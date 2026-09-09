#!/usr/bin/env python3
"""Compile the AL-SYNTAX canonical example extension with the BC code cops.

This is the ground-truth check behind AL-SYNTAX.md: if this passes, every ✓ pattern the
ruleset documents actually compiles clean on BC27 / runtime 16.0. If it fails, the ruleset is
lying and must be fixed before anyone trusts it.

Usage:
    python3 validate_al_syntax.py [--examples DIR] [--symbols DIR]

Exit code 0 = clean (no compiler errors, no analyzer warnings). Non-zero otherwise.
"""
from __future__ import annotations

import argparse
import glob
import os
import re
import shutil
import subprocess
import sys

HOME = os.path.expanduser("~")
AL = os.path.join(HOME, ".dotnet", "tools", "al")
DEFAULT_EXAMPLES = os.path.join(
    "/mnt/rojaws/localDev/setup/reference/al-syntax-examples"
)
# Any project whose .alpackages already holds BC27 symbols can donate them.
DEFAULT_SYMBOL_DONORS = [
    os.path.expanduser("~/projects/prototypes/tetris-bc/.alpackages"),
]

ANALYZER_DLLS = [
    "Microsoft.Dynamics.Nav.CodeCop.dll",
    "Microsoft.Dynamics.Nav.UICop.dll",
    "Microsoft.Dynamics.Nav.PerTenantExtensionCop.dll",
]


def find_analyzer_dir() -> str | None:
    hits = glob.glob(
        os.path.join(
            HOME, ".dotnet", "tools", ".store", "**", "net10.0", "**",
            "Microsoft.Dynamics.Nav.CodeCop.dll",
        ),
        recursive=True,
    )
    return os.path.dirname(hits[0]) if hits else None


def ensure_symbols(examples: str, symbols: str | None) -> str:
    dest = os.path.join(examples, ".alpackages")
    if os.path.isdir(dest) and glob.glob(os.path.join(dest, "*.app")):
        return dest
    donors = [symbols] if symbols else DEFAULT_SYMBOL_DONORS
    for donor in donors:
        if donor and os.path.isdir(donor) and glob.glob(os.path.join(donor, "*.app")):
            os.makedirs(dest, exist_ok=True)
            for app in glob.glob(os.path.join(donor, "*.app")):
                shutil.copy2(app, dest)
            print(f"symbols: copied {len(glob.glob(os.path.join(dest,'*.app')))} packs from {donor}")
            return dest
    sys.exit(
        "ERROR: no BC27 symbols found. Pass --symbols <dir with Microsoft_*.app>, "
        "or download via `al launchmcpserver` + al_downloadsymbols."
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--examples", default=DEFAULT_EXAMPLES)
    ap.add_argument("--symbols", default=None)
    args = ap.parse_args()

    examples = os.path.abspath(args.examples)
    if not os.path.isfile(os.path.join(examples, "app.json")):
        sys.exit(f"ERROR: no app.json under {examples}")
    if not os.path.isfile(AL):
        sys.exit(f"ERROR: al compiler not found at {AL}")

    pkg = ensure_symbols(examples, args.symbols)
    analyzer_dir = find_analyzer_dir()
    if not analyzer_dir:
        sys.exit("ERROR: code-cop analyzers not found under ~/.dotnet/tools/.store")

    out = os.path.join(examples, "AL-Syntax-Examples.app")
    cmd = [
        AL, "compile",
        f"/project:{examples}",
        f"/packagecachepath:{pkg}",
        f"/out:{out}",
    ]
    for dll in ANALYZER_DLLS:
        cmd.append(f"/analyzer:{os.path.join(analyzer_dir, dll)}")

    print("$ " + " ".join(cmd))
    proc = subprocess.run(cmd, capture_output=True, text=True)
    output = proc.stdout + proc.stderr
    print(output)

    errors = re.findall(r"error [A-Z]{2}\d{4,}:.*", output)
    warnings = re.findall(r"warning [A-Z]{2}\d{4,}:.*", output)

    print("-" * 60)
    print(f"errors:   {len(errors)}")
    print(f"warnings: {len(warnings)}")
    if errors or warnings:
        print("NOT CLEAN — AL-SYNTAX.md example is not gold. Fix before trusting the ruleset.")
        return 1
    print("CLEAN ✓ — every ✓ pattern in AL-SYNTAX.md compiles on BC27 / runtime 16.0.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
