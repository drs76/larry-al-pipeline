"""al_context — the BC/runtime facts an AL build must carry, resolved deterministically.

AL is not one language version. A rule, an API and an event can each be valid on one
runtime and absent on another, so "is this correct?" is unanswerable without knowing
which Business Central the project targets. Until now that context existed only
implicitly inside `write_canonical_app_json()`, and the hook that would have used it —
`bcquality.rules_for(bc_version=...)` — was never passed anything.

Two sources, in order:
  1. `app.json` — what the project SAYS it targets.
  2. the downloaded symbol packages — what it will actually COMPILE against.

Reporting the mismatch between them is the point. A project declaring
`"application": "27.0.0.0"` while `.alpackages` holds 26.x symbols compiles against 26
and will fail in a way that looks like a code error, not a configuration one.

Deterministic, offline, no model. Safe to call on every build.
"""
from __future__ import annotations

import glob
import json
import os
import re
import zipfile


def _app_json(root):
    try:
        with open(os.path.join(root, "app.json")) as f:
            return json.load(f)
    except (OSError, ValueError):
        return {}


def _major(v):
    """'27.5.46862.52443' -> 27. The major IS the BC version for rule/knowledge filtering."""
    m = re.match(r"\s*(\d+)", str(v or ""))
    return int(m.group(1)) if m else None


def symbol_versions(root):
    """{package basename: version} for every downloaded symbol package."""
    out = {}
    for p in sorted(glob.glob(os.path.join(root, ".alpackages", "*.app"))):
        ver = ""
        try:
            doc = json.loads(
                zipfile.ZipFile(p).read("SymbolReference.json").decode("utf-8-sig"))
            ver = str(doc.get("Version") or doc.get("AppVersion") or "")
        except Exception:
            pass
        out[os.path.basename(p)] = ver
    return out


def resolve(root, deployment_profile=None):
    """The full context dict. Never raises — a build must not die for lack of metadata."""
    aj = _app_json(root)
    syms = symbol_versions(root)

    # The Application package is the one that defines "which BC is this".
    app_sym = next((v for k, v in syms.items()
                    if k.startswith("Microsoft_Application")), "")
    base_sym = next((v for k, v in syms.items()
                     if k.startswith("Microsoft_Base Application")), "")
    effective = app_sym or base_sym

    declared_major = _major(aj.get("application"))
    actual_major = _major(effective)

    ctx = {
        "language": "AL",
        "bc_version": actual_major or declared_major,
        "runtime": aj.get("runtime"),
        # An omitted target defaults to Cloud (Learn: JSON files) — record the effective
        # value, not the literal absence, so consumers do not re-derive it.
        "target": aj.get("target") or "Cloud",
        "platform": aj.get("platform"),
        "application": aj.get("application"),
        "app_id": aj.get("id"),
        "app_name": aj.get("name"),
        "app_version": aj.get("version"),
        "publisher": aj.get("publisher"),
        "dependencies": [
            {"id": d.get("id") or d.get("appId"), "name": d.get("name"),
             "publisher": d.get("publisher"), "version": d.get("version")}
            for d in (aj.get("dependencies") or [])
        ],
        "deployment_profile": deployment_profile or os.environ.get("AL_PROFILE", "internal"),
        "symbols": syms,
        "symbol_application_version": effective,
        "version_mismatch": None,
    }

    if declared_major and actual_major and declared_major != actual_major:
        ctx["version_mismatch"] = (
            f"app.json declares application {aj.get('application')} (BC {declared_major}) "
            f"but the downloaded symbols are {effective} (BC {actual_major}) — the build "
            f"will compile against BC {actual_major}")
    return ctx


def summary(ctx):
    """One line for build logs."""
    bits = [f"BC {ctx.get('bc_version') or '?'}",
            f"runtime {ctx.get('runtime') or '?'}",
            f"target {ctx.get('target')}",
            f"profile {ctx.get('deployment_profile')}"]
    if ctx.get("dependencies"):
        bits.append(f"{len(ctx['dependencies'])} dep(s)")
    return " | ".join(bits)


def main():
    import argparse
    ap = argparse.ArgumentParser(prog="al_context")
    ap.add_argument("root", nargs="?", default=".")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    ctx = resolve(a.root)
    if a.json:
        print(json.dumps(ctx, indent=2))
    else:
        print(summary(ctx))
        if ctx["version_mismatch"]:
            print(f"  ⚠ {ctx['version_mismatch']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
