"""al_profiles — what "good enough to ship" means, per destination, as data.

The same AL is held to different standards depending on where it is going: an internal
prototype and an AppSource submission are not the same bar. Encoding that in pipeline
code means editing Python to change policy, so the profiles live in `al-profiles.yml`
and this module only resolves and applies them.

Two properties matter more than the feature itself:

  1. `internal` reproduces the pipeline's historical behaviour EXACTLY. A profile system
     that quietly changes every existing build is a regression wearing a feature's
     clothes, so a test pins it.

  2. A profile never implies a guarantee it cannot deliver. Policy under a profile's
     `declared:` key — breaking-change rules, upgrade codeunits — needs AL-7, which does
     not exist yet. `unenforced()` reports those by name at build time. The alternative
     is an `upgrade` profile that looks like it checks for breaking changes and does not,
     which is worse than having no profile at all.

Enforced today: analyzer set, required app.json metadata, `target`, test expectations,
review depth, warning escalation, knowledge-filter width.
"""
from __future__ import annotations

import copy
import json
import os

DEFAULT_PROFILE = "internal"
_PROFILE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             "al-profiles.yml")
_cache = None


class ProfileError(ValueError):
    """An unknown or unreadable profile. Never silently fall back to a laxer one."""


def _load_file(path=None):
    global _cache
    if _cache is not None and path is None:
        return _cache
    import yaml
    with open(path or _PROFILE_FILE) as f:
        doc = yaml.safe_load(f) or {}
    if path is None:
        _cache = doc
    return doc


def names(path=None):
    return sorted((_load_file(path).get("profiles") or {}))


def resolve(name=None, path=None):
    """Profile dict with defaults merged. Unknown name raises — never downgrades.

    Silently falling back to `internal` when someone types `apsource` would run an
    AppSource submission through prototype-grade checks and report a pass.
    """
    name = (name or os.environ.get("AL_PROFILE") or DEFAULT_PROFILE).strip().lower()
    doc = _load_file(path)
    profiles = doc.get("profiles") or {}
    if name not in profiles:
        raise ProfileError(
            f"unknown AL profile {name!r} — known profiles: {', '.join(sorted(profiles))}")
    p = copy.deepcopy(doc.get("defaults") or {})
    for k, v in (profiles[name] or {}).items():
        if k == "knowledge" and isinstance(v, dict):
            p.setdefault("knowledge", {}).update(v)
        else:
            p[k] = v
    p["name"] = name
    return p


def unenforced(profile):
    """Policy this profile declares that nothing in the pipeline checks yet."""
    return sorted((profile.get("declared") or {}).items())


def check_manifest(app_json, profile):
    """[reason] — required metadata that is missing, and a wrong `target`.

    Deterministic and cheap. AppSource rejects submissions over exactly these fields, and
    finding out from Microsoft costs days.
    """
    out = []
    missing = [k for k in (profile.get("required_app_json") or [])
               if not (app_json or {}).get(k)]
    if missing:
        out.append(f"app.json is missing {len(missing)} field(s) required by the "
                   f"{profile['name']} profile: {', '.join(missing)}")
    want = profile.get("require_target")
    if want:
        # An omitted target IS Cloud (see al_context), so absence satisfies a Cloud
        # requirement and only a contradicting value is a failure.
        got = (app_json or {}).get("target") or "Cloud"
        if str(got).lower() != str(want).lower():
            out.append(f"app.json target is {got!r} but the {profile['name']} profile "
                       f"requires {want!r}")
    return out


def check_diagnostics(diags, profile):
    """[reason] — warnings this profile treats as build-failing.

    The compiler's own severity is a general-purpose judgement. A missing tooltip is a
    warning everywhere and a rejection at AppSource, and that difference is policy, not
    compilation.
    """
    out = []
    escalate = {str(c).upper() for c in (profile.get("escalate") or [])}
    fail_all = bool(profile.get("fail_on_warning"))
    hits = {}
    for d in diags or []:
        sev = str(d.get("severity", "")).lower()
        if not sev.startswith("warn"):
            continue
        code = str(d.get("code", "")).upper()
        if fail_all or code in escalate:
            hits.setdefault(code, 0)
            hits[code] += 1
    for code, n in sorted(hits.items()):
        why = "fail_on_warning" if (fail_all and code not in escalate) else "escalate"
        out.append(f"{code}: {n} warning(s) — failing under the {profile['name']} "
                   f"profile ({why})")
    return out


def review_policy(profile):
    """(required, independent) for the review gate."""
    mode = str(profile.get("review") or "advisory").lower()
    return mode == "required", mode == "required"


def tests_policy(profile):
    """(run, required). `optional` runs them and does not fail a project that has none —
    which is already how al_tests treats `no-tests`."""
    mode = str(profile.get("tests") or "off").lower()
    return mode in ("optional", "required"), mode == "required"


def upgrade_policy(profile):
    """(policy, needs_baseline) — how this destination treats breaking changes.

    null/warn need no baseline. `none` and `strict` do, and a missing baseline must fail
    rather than pass: "could not check" and "checked and clean" are different answers, and
    only one of them is safe to ship on.
    """
    pol = profile.get("breaking_changes")
    pol = str(pol).lower() if pol else None
    return pol, pol in ("none", "strict")


def upgrade_failures(verdict, profile):
    """[reason] — is this upgrade verdict acceptable to the profile?"""
    pol, _ = upgrade_policy(profile)
    if not pol or pol == "warn":
        return []
    floor = {"none": ("BREAKING", "DATA MIGRATION REQUIRED"),
             "strict": ("WARNING", "BREAKING", "DATA MIGRATION REQUIRED")}[pol]
    if verdict in floor:
        return [f"upgrade verdict is {verdict}, which the {profile['name']} profile "
                f"does not allow (breaking_changes: {pol})"]
    return []


def describe(profile):
    bits = [f"profile: {profile['name']}",
            f"analyzers={'+'.join(profile.get('analyzers') or [])}",
            f"tests={profile.get('tests')}",
            f"review={profile.get('review')}"]
    if profile.get("fail_on_warning"):
        bits.append("fail_on_warning")
    if profile.get("escalate"):
        bits.append("escalate=" + ",".join(profile["escalate"]))
    if profile.get("require_target"):
        bits.append(f"target={profile['require_target']}")
    if profile.get("breaking_changes"):
        bits.append(f"breaking_changes={profile['breaking_changes']}")
    return " | ".join(bits)


def evaluate(project_root, name=None, diags=None, path=None):
    """Apply a profile to a project WITHOUT rebuilding it.

    This is the acceptance criterion "the same source can be evaluated under different
    profiles" — the checks that need only the tree and (optionally) diagnostics from a
    previous build run here.
    """
    prof = resolve(name, path)
    try:
        with open(os.path.join(project_root, "app.json")) as f:
            aj = json.load(f)
    except (OSError, ValueError) as e:
        return {"profile": prof["name"], "ok": False,
                "failures": [f"app.json unreadable: {e}"], "unenforced": unenforced(prof)}
    fails = check_manifest(aj, prof) + check_diagnostics(diags, prof)
    return {"profile": prof["name"], "ok": not fails, "failures": fails,
            # A pass under a profile whose central promise nothing checks is a PARTIAL
            # pass. Saying "PASS" flat would be the profile implying a guarantee it does
            # not deliver — the exact thing `declared:` exists to prevent.
            "partial": bool(unenforced(prof)),
            "unenforced": unenforced(prof), "summary": describe(prof)}


def main():
    import argparse
    ap = argparse.ArgumentParser(prog="al_profiles")
    ap.add_argument("profile", nargs="?", help="profile name (omit to list)")
    ap.add_argument("root", nargs="?", default=".")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    if not a.profile:
        doc = _load_file()
        for n in names():
            d = " ".join(((doc["profiles"][n] or {}).get("description") or "").split())
            print(f"  {n:<10} {d}")
        return 0
    try:
        res = evaluate(os.path.abspath(a.root), a.profile)
    except ProfileError as e:
        print(f"ERROR: {e}")
        return 2
    if a.json:
        print(json.dumps(res, indent=2))
        return 0 if res["ok"] else 1
    print(res.get("summary", ""))
    for u, v in res["unenforced"]:
        print(f"  ⚠ declares {u}={v} — NOT enforced (needs the breaking-change analyser)")
    if res["ok"]:
        if res["partial"]:
            print(f"  PARTIAL PASS — everything this profile CAN check is clean, but "
                  f"{len(res['unenforced'])} declared policy item(s) above went "
                  f"unchecked. This is not a clean bill of health.")
        else:
            print("  PASS — nothing this profile can check is wrong")
        return 0
    for f in res["failures"]:
        print(f"  ⛔ {f}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
