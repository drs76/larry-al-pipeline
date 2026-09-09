"""al_brain — one compact, deterministic profile of a project, so nothing re-derives it.

Every task in this pipeline starts by working out the same things: which BC, what objects
exist, what it integrates with, which events it publishes, whether anything tests it. Each
instrument answers a slice, and each one answers it again from scratch. This assembles
those answers ONCE into something small enough to carry in a prompt.

It is a synthesis layer and deliberately owns no analysis of its own. bc/app facts come
from `al_context`, objects and events from `al_graph`, risk signals from `al_semantics`,
coverage from `al_tests` + the graph. Adding a second way to count codeunits here would
guarantee two numbers that disagree.

Three properties are load-bearing:

  * **Deterministic.** Same source, same profile, byte for byte. That is why there is no
    timestamp: a generation time would make every regeneration differ and turn "has this
    project changed?" into an unanswerable question. Provenance is a tree hash plus the
    pipeline revision, which identify the inputs exactly and do not drift on their own.
  * **No secrets, ever.** A profile is the thing most likely to be pasted into a prompt,
    a ticket or a chat. Every string it emits goes through `secret_gate`, and a HIGH
    finding fails generation rather than being quietly redacted — if a secret is sitting
    in the source, silently scrubbing the profile hides it while leaving it in the repo.
  * **Compact.** Counts and names, not bodies. A profile that costs 8k tokens is one
    nobody includes, and then it may as well not exist.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess

import al_context
import al_graph
import al_semantics
import al_tests
import build_receipt
import secret_gate

BRAIN_FILE = ".al-brain.yml"

# What an extension talks to. Each is a real integration risk, and each is a distinct
# conversation with a customer — "it calls out over HTTP" is not the same as "it writes
# to blob storage".
_INTEGRATIONS = {
    "dataverse": r"\b(CRMIntegration|Dataverse|CDSIntegration|RegisterConnection)\b",
    "azure_blob": r"\b(ABS[A-Za-z]*Client|BlobServiceClient|AzureBlob)\b",
    "http": r"\bHttpClient\b",
    "file_system": r"\b(FileManagement|ServerFilePath|ServerTempFileName)\b",
    "isolated_storage": r"\bIsolatedStorage\b",
    "job_queue": r"\bJob Queue Entry\b|\btrigger OnRun\b",
    "email": r"\b(Email|SMTP)\b",
    "xml_soap": r"\b(SoapHttpClient|XmlPort)\b",
}
_MASK = re.compile(r"'(?:[^']|'')*'|//.*$")


class SecretInProfile(RuntimeError):
    """A secret was found in the source this profile summarises."""


def _pipeline_rev():
    try:
        r = subprocess.run(["git", "rev-parse", "--short", "HEAD"],
                           cwd=os.path.dirname(os.path.abspath(__file__)),
                           capture_output=True, text=True, timeout=10)
        return r.stdout.strip() or "unknown"
    except Exception:
        return "unknown"


def _src_dir(root):
    s = os.path.join(root, "src")
    return s if os.path.isdir(s) else root


def _all_source(root):
    out = []
    for dp, dirs, fs in os.walk(_src_dir(root)):
        dirs[:] = sorted(d for d in dirs if d not in (".alpackages", "bin", "obj", ".git"))
        for fn in sorted(fs):
            if fn.endswith(".al"):
                try:
                    out.append(open(os.path.join(dp, fn), encoding="utf-8-sig",
                                    errors="replace").read())
                except OSError:
                    continue
    return "\n".join(out)


def _integrations(source):
    """Which integrations this project actually uses. Comments and string literals are
    masked first — a URL in a caption is not an HTTP client."""
    clean = "\n".join(_MASK.sub(" ", ln) for ln in source.splitlines())
    return sorted(k for k, pat in _INTEGRATIONS.items()
                  if re.search(pat, clean, re.IGNORECASE))


def _risk(graph, findings, ctx, integrations):
    """Three risk axes, each derived from something already measured.

    Deliberately coarse — none | low | medium | high. A false precision here ("risk: 6.4")
    invites treating a heuristic as a measurement.
    """
    rules = {f["rule"] for f in findings}
    counts = {r: sum(1 for f in findings if f["rule"] == r) for r in rules}

    integ = "none"
    if integrations:
        integ = "low"
        if {"http", "dataverse", "azure_blob"} & set(integrations):
            integ = "medium"
        if rules & {"http-in-write-trigger", "http-in-subscriber", "http-in-loop",
                    "httpclient-no-timeout"}:
            integ = "high"

    # Upgrade risk is about SURFACE: what other code can bind to. Events and extension
    # objects are commitments to somebody else's code.
    published = sum(1 for e in graph["edges"] if e["rel"] == "publishes")
    exts = sum(1 for n in graph["nodes"]
               if n.get("internal") and n["kind"].endswith("extension"))
    upgrade = "low" if published + exts == 0 else ("medium" if published + exts < 8 else "high")

    tables = [n for n in graph["nodes"] if n.get("internal") and n["kind"] == "table"]
    data_mig = "none" if not tables else ("low" if len(tables) < 5 else "medium")
    if counts.get("commit-in-loop") or counts.get("commit-in-subscriber"):
        data_mig = "high"

    return {"integration": integ, "upgrade": upgrade, "data_migration": data_mig}


def build(root, graph=None, check_secrets=True):
    """The profile dict. Deterministic for a given source tree."""
    root = os.path.abspath(root)
    source = _all_source(root)

    if check_secrets:
        findings = secret_gate.scan(source)
        high = [f for f in findings if f["confidence"] == "high"]
        if high:
            # Refusing beats redacting. A scrubbed profile would look clean while the
            # secret stayed in the repository, which is the worse of the two outcomes.
            raise SecretInProfile(
                "secret(s) found in the project source — fix the source, do not publish a "
                "profile of it: "
                + ", ".join(f'{f["name"]} ({f["preview"]})' for f in high[:3]))

    ctx = al_context.resolve(root)
    g = graph or al_graph.build(root)
    sem = al_semantics.analyse(root)
    integrations = _integrations(source)

    # `field` and `event` are graph nodes, not AL objects. Counting them here put
    # "field 57" in a one-line project summary, which is noise crowding out the facts
    # somebody actually needs.
    _PSEUDO = ("field", "event")
    internal = [n for n in g["nodes"] if n.get("internal")]
    by_kind = {}
    for n in internal:
        if n["kind"] in _PSEUDO:
            continue
        by_kind.setdefault(n["kind"], []).append(n["name"])

    test_files = al_tests.find_test_codeunits(_src_dir(root))
    testables = [n["id"] for n in internal
                 if n["kind"] in ("table", "codeunit", "page") and not n.get("test")]
    covered = [t for t in testables if al_graph.tests_for(g, t.split(":", 1)[1])]

    return {
        "bc": {"version": ctx.get("bc_version"), "runtime": ctx.get("runtime"),
               "target": ctx.get("target"), "application": ctx.get("application")},
        "app": {"publisher": ctx.get("publisher"), "id": ctx.get("app_id"),
                "name": ctx.get("app_name"), "version": ctx.get("app_version"),
                "dependencies": [d.get("name") for d in (ctx.get("dependencies") or [])
                                 if d.get("name")]},
        "objects": {k: {"count": len(v), "names": sorted(v)[:25]}
                    for k, v in sorted(by_kind.items())},
        "integrations": integrations,
        "events": {
            "publishers": sorted({g_n["name"] for g_n in g["nodes"]
                                  if g_n["kind"] == "event" and g_n.get("internal")}),
            "subscribers": sorted({e["to"].split(":", 1)[-1] for e in g["edges"]
                                   if e["rel"] == "subscribes-to"}),
        },
        "tests": {
            "codeunits": len(test_files),
            "covered_objects": len(covered),
            "testable_objects": len(testables),
            # A percentage of nothing is not 100%. "n/a" is the honest answer when the
            # project has no testable objects at all.
            "coverage": (f"{round(100 * len(covered) / len(testables))}%"
                         if testables else "n/a"),
        },
        "risk": _risk(g, sem, ctx, integrations),
        "advisories": {r: sum(1 for f in sem if f["rule"] == r)
                       for r in sorted({f["rule"] for f in sem})},
        # Provenance without a clock: the tree hash says exactly which source this
        # describes, the pipeline revision says which rules produced it.
        "generated_from": {
            "source_hash": build_receipt.tree_hash(root),
            "pipeline_rev": _pipeline_rev(),
            "project": os.path.basename(root.rstrip("/")),
        },
    }


def to_yaml(profile):
    """Compact YAML. Deterministic ordering, no anchors, no timestamps."""
    try:
        import yaml
        return yaml.safe_dump(profile, sort_keys=False, default_flow_style=False,
                              width=100, allow_unicode=True)
    except Exception:
        return json.dumps(profile, indent=2, sort_keys=True)


def as_prompt_context(profile, max_chars=1800):
    """The few lines a task actually needs. A profile nobody can afford to include is one
    that may as well not exist, so this is a summary of the summary."""
    o = profile["objects"]
    lines = [
        f"PROJECT: {profile['app'].get('name')} {profile['app'].get('version') or ''} "
        f"({profile['app'].get('publisher')})",
        f"  BC {profile['bc'].get('version')} | runtime {profile['bc'].get('runtime')} | "
        f"target {profile['bc'].get('target')}",
        "  objects: " + (", ".join(f"{k} {v['count']}" for k, v in o.items()) or "none"),
    ]
    if profile["integrations"]:
        lines.append("  integrates with: " + ", ".join(profile["integrations"]))
    if profile["events"]["publishers"]:
        lines.append(f"  publishes {len(profile['events']['publishers'])} event(s); "
                     f"subscribes to {len(profile['events']['subscribers'])}")
    t = profile["tests"]
    lines.append(f"  tests: {t['codeunits']} codeunit(s), coverage {t['coverage']}")
    r = profile["risk"]
    lines.append(f"  risk: integration={r['integration']} upgrade={r['upgrade']} "
                 f"data_migration={r['data_migration']}")
    if profile["advisories"]:
        lines.append("  advisories: " + ", ".join(f"{k}={v}" for k, v in
                                                  list(profile["advisories"].items())[:6]))
    return "\n".join(lines)[:max_chars]


def write(root, profile=None):
    p = profile or build(root)
    path = os.path.join(root, BRAIN_FILE)
    with open(path, "w") as f:
        f.write(to_yaml(p))
    return path


def is_stale(root, profile_path=None):
    """(stale, reason) — does the stored profile still describe this source?"""
    path = profile_path or os.path.join(root, BRAIN_FILE)
    try:
        import yaml
        with open(path) as f:
            stored = yaml.safe_load(f) or {}
    except Exception as e:
        return True, f"no readable profile ({e})"
    was = (stored.get("generated_from") or {}).get("source_hash")
    now = build_receipt.tree_hash(root)
    if was != now:
        return True, f"source has changed since the profile was generated"
    return False, "profile matches the current source"


def main():
    import argparse
    ap = argparse.ArgumentParser(prog="al_brain",
                                 description="compact deterministic project profile")
    ap.add_argument("root", nargs="?", default=".")
    ap.add_argument("--write", action="store_true", help=f"write {BRAIN_FILE}")
    ap.add_argument("--prompt", action="store_true", help="the short prompt-context form")
    ap.add_argument("--check", action="store_true", help="is the stored profile stale?")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    root = os.path.abspath(a.root)

    if a.check:
        stale, why = is_stale(root)
        print(("STALE — " if stale else "current — ") + why)
        return 1 if stale else 0
    try:
        p = build(root)
    except SecretInProfile as e:
        print(f"REFUSED: {e}")
        return 2
    if a.write:
        print(f"wrote {write(root, p)}")
    elif a.prompt:
        print(as_prompt_context(p))
    elif a.json:
        print(json.dumps(p, indent=2, sort_keys=True))
    else:
        print(to_yaml(p))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
