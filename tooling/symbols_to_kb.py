#!/usr/bin/env python3
"""Flatten BC symbol packages (.app SymbolReference.json) into a searchable `bc-symbols` KB corpus.

Why: the KB indexes AL *source* (a git revision) + curated notes, but the version-EXACT API
surface — every object, field, key, public procedure signature, and event with its real
parameter NAMES — lives in the compiled symbol packages the target build actually uses. Events
bind by parameter name, so a guessed name silently never fires. Indexing symbols gives al-rag
ground-truth signatures to inject, killing the API-hallucination class that source-RAG and LoRA
both miss.

Output: one markdown file per source .app, headed per object, under OUT/<version>/. Point a
`bc-symbols` corpus at OUT (kept OUT of git — big, regenerable). Then:
    python3 kb_core.py index --corpus bc-symbols

Usage:
    python3 symbols_to_kb.py --alpackages <dir with Microsoft_*.app> [--out DIR] [--version TAG]
"""
from __future__ import annotations

import argparse
import glob
import io
import json
import os
import re
import zipfile

OBJ_COLLS = [
    "Tables", "TableExtensions", "Codeunits", "Pages", "PageExtensions",
    "Reports", "XmlPorts", "Queries", "ControlAddIns", "EnumTypes",
    "Interfaces", "PermissionSets", "Profiles",
]
SINGULAR = {
    "Tables": "Table", "TableExtensions": "TableExtension", "Codeunits": "Codeunit",
    "Pages": "Page", "PageExtensions": "PageExtension", "Reports": "Report",
    "XmlPorts": "XmlPort", "Queries": "Query", "ControlAddIns": "ControlAddIn",
    "EnumTypes": "Enum", "Interfaces": "Interface", "PermissionSets": "PermissionSet",
    "Profiles": "Profile",
}


def read_symbol_json(app_path: str) -> dict | None:
    """A BC .app is a small header followed by a zip; slice from the first PK signature."""
    with open(app_path, "rb") as fh:
        data = fh.read()
    i = data.find(b"PK\x03\x04")
    if i < 0:
        return None
    z = zipfile.ZipFile(io.BytesIO(data[i:]))
    if "SymbolReference.json" not in z.namelist():
        return None
    return json.loads(z.read("SymbolReference.json").decode("utf-8-sig"))


def fmt_type(td: dict | None) -> str:
    """Render a TypeDefinition: 'Code[20]', 'Record "No. Series"', 'List of [Text]'."""
    if not td:
        return "Variant"
    name = td.get("Name", "")
    sub = td.get("Subtype")
    if sub and isinstance(sub, dict) and sub.get("Name"):
        return f'{name} "{sub["Name"]}"'
    typeargs = td.get("TypeArguments") or []
    if typeargs:
        inner = ", ".join(fmt_type(t) for t in typeargs)
        return f"{name} of [{inner}]"
    return name or "Variant"


def method_sig(m: dict) -> str:
    params = ", ".join(
        f'{p.get("Name","")}: {fmt_type(p.get("TypeDefinition"))}'
        for p in (m.get("Parameters") or [])
    )
    ret = m.get("ReturnTypeDefinition")
    ret_s = f": {fmt_type(ret)}" if ret and ret.get("Name") else ""
    return f'{m.get("Name","")}({params}){ret_s}'


def decamel(name: str) -> str:
    """'OnAfterPostSalesDoc' -> 'On After Post Sales Doc' — a tokenization aid for NL queries
    (not a fabricated description; purely the event name re-spaced)."""
    return re.sub(r"(?<=[a-z0-9])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])", " ", name).strip()


def event_kind(m: dict) -> str | None:
    for a in m.get("Attributes") or []:
        n = a.get("Name", "")
        if n in ("IntegrationEvent", "BusinessEvent", "InternalEvent"):
            return n
    return None


def render_object(coll: str, o: dict, tag: str, module: str) -> str:
    kind = SINGULAR[coll]
    oid = o.get("Id")
    name = o.get("Name", "")
    target = o.get("TargetObject")
    head = f'## {kind} "{name}"'
    if oid and oid > 0:
        head += f" (id {oid})"
    if target:
        head += f' extends "{target}"'
    head += f"  ·  {tag} · {module}"
    lines = [head, ""]

    fields = o.get("Fields") or []
    if fields:
        lines.append("Fields:")
        for f in fields:
            lines.append(f'- ({f.get("Id","?")}) {f.get("Name","")}: {fmt_type(f.get("TypeDefinition"))}')
        lines.append("")

    keys = o.get("Keys") or []
    if keys:
        klist = "; ".join(", ".join(k.get("FieldNames", []) or []) for k in keys if k.get("FieldNames"))
        if klist:
            lines.append(f"Keys: {klist}")
            lines.append("")

    values = o.get("Values") or []
    if values:  # enum members
        lines.append("Values: " + ", ".join(f'{v.get("Name","")}({v.get("Ordinal","?")})' for v in values))
        lines.append("")

    methods = o.get("Methods") or []
    procs = [m for m in methods if not event_kind(m)]
    events = [m for m in methods if event_kind(m)]
    if procs:
        lines.append("Procedures:")
        for m in procs:
            lines.append(f"- {method_sig(m)}")
        lines.append("")
    if events:
        # Object chunk only LISTS event names; each event also gets its OWN ### chunk below
        # so it is individually retrievable (a 500-event codeunit otherwise hard-slices into
        # incoherent fragments and no single event can be found — measured via rag_eval, 2026-08-06).
        lines.append(f"Events ({len(events)}) — each has its own entry below; subscriber params bind BY NAME.")
        lines.append("")
    out = "\n".join(lines).rstrip() + "\n\n"

    # One ### chunk per event: signature in the heading (→ embedded + in the breadcrumb),
    # body repeats it + object context + a de-camelCased phrase to aid natural-language match.
    ev_blocks = []
    for m in events:
        sig = method_sig(m)
        kindname = event_kind(m)
        phrase = decamel(m.get("Name", ""))
        ev_blocks.append(
            f"### [{kindname}] {sig}\n"
            f'{kindname} on {kind} "{name}". {phrase}. '
            f"Subscriber parameters bind BY NAME — match them exactly.\n"
        )
    if ev_blocks:
        out += "\n".join(ev_blocks) + "\n"
    return out


def walk_namespaces(node: dict, out: list[tuple[str, dict]]):
    for coll in OBJ_COLLS:
        for o in node.get(coll, []) or []:
            out.append((coll, o))
    for sub in node.get("Namespaces", []) or []:
        walk_namespaces(sub, out)


def process_app(app_path: str, out_dir: str, version_tag: str) -> tuple[str, int] | None:
    sym = read_symbol_json(app_path)
    if not sym:
        return None
    module = sym.get("Name", os.path.basename(app_path))
    tag = version_tag or f"BC {sym.get('Version','?')}"
    objs: list[tuple[str, dict]] = []
    walk_namespaces(sym, objs)
    if not objs:
        return None
    slug = re.sub(r"[^A-Za-z0-9]+", "-", module).strip("-")
    out_path = os.path.join(out_dir, f"{slug}.md")
    with open(out_path, "w") as fh:
        fh.write(f"# {module} — symbols ({tag})\n\n")
        fh.write(f"Publisher: {sym.get('Publisher','?')} · Runtime {sym.get('RuntimeVersion','?')} · "
                 f"{len(objs)} objects. Version-exact API surface; do not invent names not listed here.\n\n")
        for coll, o in objs:
            fh.write(render_object(coll, o, tag, module))
    return out_path, len(objs)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--alpackages", required=True, help="dir containing Microsoft_*.app symbol packs")
    ap.add_argument("--out", default="/mnt/rojaws/refs/bc-symbols")
    ap.add_argument("--version", default="", help="version tag, e.g. 'BC27.5' (else read from each pack)")
    args = ap.parse_args()

    sub = args.version.replace(" ", "") or "current"
    out_dir = os.path.join(args.out, sub)
    os.makedirs(out_dir, exist_ok=True)

    apps = sorted(glob.glob(os.path.join(args.alpackages, "*.app")))
    if not apps:
        raise SystemExit(f"no .app packs under {args.alpackages}")

    total_objs = 0
    for app in apps:
        res = process_app(app, out_dir, args.version)
        if res:
            path, n = res
            total_objs += n
            print(f"  {os.path.basename(path):45s} {n:6d} objects  <- {os.path.basename(app)}")
        else:
            print(f"  (skip, no symbols)                            <- {os.path.basename(app)}")
    print(f"\nWrote {total_objs} objects to {out_dir}")
    print("Next: add a `bc-symbols` corpus pointing at the parent dir, then `kb_core.py index --corpus bc-symbols`.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
