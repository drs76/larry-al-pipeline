"""al_upgrade — what breaks if this version replaces the one already installed.

Compiling proves the new code is valid. It says nothing about the customer whose data
sits in the tables the new code redefines. Those are different questions, and only the
second one loses data: a field dropped between versions compiles perfectly and takes the
column with it on upgrade.

The comparison is `.app` to `.app`, using each package's `SymbolReference.json` and
`NavxManifest.xml`. That is deliberate. A source tree would need a second, weaker
extractor that disagrees with the first about types and IDs, and two extractors that
disagree are worse than one that is merely incomplete. Build the version, then compare.

Four verdicts, ordered by what they cost the person running the upgrade:

    SAFE                       additive; nothing existing changes meaning
    WARNING                    references break, data survives
    BREAKING                   dependent extensions or integrations stop working
    DATA MIGRATION REQUIRED    stored data is lost or silently reinterpreted

The last is the one that matters, and it is not the same as BREAKING. A renamed field
breaks code loudly at compile time. A field whose ID changed keeps compiling and
quietly orphans its column, which is why ID identity is the spine of this module: objects
and fields are matched by ID first and by name second, and a same-name-different-ID pair
is reported as a renumber rather than silently treated as the same thing.

Deterministic, offline, no model.
"""
from __future__ import annotations

import json
import os
import re
import xml.etree.ElementTree as ET
import zipfile

SAFE = "SAFE"
WARNING = "WARNING"
BREAKING = "BREAKING"
DATA = "DATA MIGRATION REQUIRED"
_RANK = {SAFE: 0, WARNING: 1, BREAKING: 2, DATA: 3}

_KINDS = {"Tables": "table", "Codeunits": "codeunit", "Pages": "page",
          "EnumTypes": "enum", "Interfaces": "interface", "Reports": "report",
          "Queries": "query", "XmlPorts": "xmlport", "PermissionSets": "permissionset",
          "ControlAddIns": "controladdin"}
# Data lives in tables and is indexed by enum ordinal; everything else is contract only.
_DATA_KINDS = ("table", "enum")


def _prop(node, name, default=None):
    for p in (node.get("Properties") or []):
        if (p.get("Name") or "").lower() == name.lower():
            return p.get("Value", True)
    return default


def _obsolete(node):
    """(state, reason) from either Properties or an Obsolete attribute."""
    state = _prop(node, "ObsoleteState")
    if state:
        return str(state), str(_prop(node, "ObsoleteReason") or "")
    for a in (node.get("Attributes") or []):
        if (a.get("Name") or "") == "Obsolete":
            args = [str(x.get("Value", "")) for x in (a.get("Arguments") or [])]
            return "Pending", (args[0] if args else "")
    return "", ""


def _type_name(td):
    if not isinstance(td, dict):
        return ""
    n = td.get("Name", "")
    subs = td.get("Subtype") or {}
    if isinstance(subs, dict) and subs.get("Name"):
        n += f' "{subs["Name"]}"'
    args = td.get("TypeArguments") or []
    if args:
        n += "[" + ", ".join(_type_name(a) for a in args) + "]"
    return n


def _method(m):
    ps = ", ".join(f'{p.get("Name","")}: {_type_name(p.get("TypeDefinition"))}'
                   for p in (m.get("Parameters") or []))
    ret = m.get("ReturnTypeDefinition")
    r = f": {_type_name(ret)}" if ret and ret.get("Name") else ""
    ev = next((a.get("Name") for a in (m.get("Attributes") or [])
               if "Event" in (a.get("Name") or "")), "")
    st, _ = _obsolete(m)
    return {"signature": f"{m.get('Name','')}({ps}){r}", "event": ev,
            "public": not m.get("IsLocal") and not m.get("IsInternal"),
            "obsolete": st}


def _walk(node, out):
    for coll, kind in _KINDS.items():
        for o in node.get(coll) or []:
            if o.get("Name") is None:
                continue
            st, reason = _obsolete(o)
            rec = {
                "kind": kind, "id": o.get("Id"), "name": o.get("Name"),
                "obsolete": st, "obsolete_reason": reason,
                "fields": {f.get("Id"): {"name": f.get("Name"),
                                         "type": _type_name(f.get("TypeDefinition")),
                                         "obsolete": _obsolete(f)[0]}
                           for f in (o.get("Fields") or []) if f.get("Id") is not None},
                "keys": {k.get("Name"): {"fields": list(k.get("FieldNames") or []),
                                         "clustered": bool(_prop(k, "Clustered"))}
                         for k in (o.get("Keys") or []) if k.get("Name")},
                # Enum values carry NO id in symbols — the ORDINAL is positional, and the
                # ordinal is what is stored in every row. Order is therefore data.
                "values": [v.get("Name") for v in (o.get("Values") or []) if v.get("Name")],
                "methods": {m["Name"]: _method(m) for m in (o.get("Methods") or [])
                            if m.get("Name")},
                "api": {p: _prop(o, p) for p in
                        ("APIPublisher", "APIGroup", "APIVersion", "EntityName",
                         "EntitySetName") if _prop(o, p) is not None},
            }
            out[(kind, o.get("Id"))] = rec
    for sub in node.get("Namespaces") or []:
        _walk(sub, out)


def _manifest(z):
    try:
        root = ET.fromstring(z.read("NavxManifest.xml").decode("utf-8-sig"))
    except Exception:
        return {}
    ns = {"n": "http://schemas.microsoft.com/navx/2015/manifest"}
    app = root.find("n:App", ns)
    out = dict(app.attrib) if app is not None else {}
    deps = []
    for d in root.findall(".//n:Dependency", ns):
        deps.append({k: d.attrib.get(k) for k in ("Id", "Name", "Publisher", "MinVersion")
                     if d.attrib.get(k)})
    out["dependencies"] = deps
    return out


def surface(app_path):
    """The upgrade-relevant contract of one .app: objects, fields, keys, values, methods."""
    if not os.path.isfile(app_path):
        raise FileNotFoundError(f"no such .app: {app_path}")
    with zipfile.ZipFile(app_path) as z:
        doc = json.loads(z.read("SymbolReference.json").decode("utf-8-sig"))
        man = _manifest(z)
    objs = {}
    _walk(doc, objs)
    return {"path": app_path, "app_id": doc.get("AppId") or man.get("Id"),
            "name": doc.get("Name") or man.get("Name"),
            "version": doc.get("Version") or man.get("Version", ""),
            "dependencies": man.get("dependencies") or [], "objects": objs}


def _f(sev, rule, obj, detail, old=None, new=None):
    return {"severity": sev, "rule": rule, "object": obj, "detail": detail,
            "old": old, "new": new}


def _by_name(objs):
    out = {}
    for (kind, oid), rec in objs.items():
        out.setdefault((kind, (rec["name"] or "").lower()), []).append((oid, rec))
    return out


def _diff_fields(old, new, label, out):
    o_f, n_f = old["fields"], new["fields"]
    n_by_name = {(v["name"] or "").lower(): (fid, v) for fid, v in n_f.items()}
    for fid, of in sorted(o_f.items(), key=lambda x: (x[0] is None, x[0])):
        nf = n_f.get(fid)
        if nf is None:
            moved = n_by_name.get((of["name"] or "").lower())
            if moved:
                # Compiles fine, and the column the data is in no longer matches the
                # field that claims the name. This is the quiet one.
                out.append(_f(DATA, "field-renumbered", label,
                              f'field "{of["name"]}" moved from id {fid} to '
                              f'{moved[0]} — stored data stays on the OLD id and is '
                              f'orphaned', fid, moved[0]))
            else:
                out.append(_f(DATA, "field-deleted", label,
                              f'field {fid} "{of["name"]}" ({of["type"]}) was removed — '
                              f'its column and contents go with it', of["name"], None))
            continue
        if (of["name"] or "").lower() != (nf["name"] or "").lower():
            out.append(_f(WARNING, "field-renamed", label,
                          f'field {fid} renamed "{of["name"]}" → "{nf["name"]}" — data '
                          f'survives, references to the old name do not',
                          of["name"], nf["name"]))
        if of["type"] != nf["type"]:
            out.append(_f(DATA, "field-type-changed", label,
                          f'field {fid} "{nf["name"]}" changed type {of["type"]} → '
                          f'{nf["type"]} — existing values must convert',
                          of["type"], nf["type"]))
        if not of["obsolete"] and nf["obsolete"]:
            out.append(_f(WARNING, "field-obsoleted", label,
                          f'field {fid} "{nf["name"]}" is now Obsolete{("::" + nf["obsolete"]) if nf["obsolete"] else ""}',
                          of["obsolete"], nf["obsolete"]))
    for fid, nf in sorted(n_f.items(), key=lambda x: (x[0] is None, x[0])):
        if fid not in o_f and (nf["name"] or "").lower() not in {
                (v["name"] or "").lower() for v in o_f.values()}:
            out.append(_f(SAFE, "field-added", label,
                          f'new field {fid} "{nf["name"]}" ({nf["type"]})', None, nf["name"]))


def _diff_keys(old, new, label, out):
    for name, ok in old["keys"].items():
        nk = new["keys"].get(name)
        if nk is None:
            out.append(_f(WARNING, "key-removed", label,
                          f'key "{name}" ({", ".join(ok["fields"])}) removed — queries '
                          f'relying on that order lose their index', name, None))
            continue
        if ok["fields"] != nk["fields"]:
            out.append(_f(WARNING, "key-changed", label,
                          f'key "{name}" fields {ok["fields"]} → {nk["fields"]}',
                          ok["fields"], nk["fields"]))
        if ok["clustered"] and not nk["clustered"] or nk["clustered"] and not ok["clustered"]:
            # Changing which key is clustered rewrites the physical table.
            out.append(_f(DATA, "clustered-key-changed", label,
                          f'key "{name}" clustered {ok["clustered"]} → {nk["clustered"]} '
                          f'— the table is physically reorganised on upgrade',
                          ok["clustered"], nk["clustered"]))


def _diff_values(old, new, label, out):
    ov, nv = old["values"], new["values"]
    if ov == nv:
        return
    removed = [v for v in ov if v not in nv]
    for v in removed:
        out.append(_f(BREAKING, "enum-value-removed", label,
                      f'enum value "{v}" removed — rows holding it have no valid value',
                      v, None))
    # Ordinals are positional and stored. Appending is safe; inserting or reordering
    # silently re-points every stored row at a different value.
    #
    # Reorder is judged on the RELATIVE order of values present in both versions. An
    # insertion shifts every later ordinal, which is already reported as
    # enum-value-inserted — also calling that a reorder describes one edit twice and
    # makes a precise report look like a noisy one.
    common = [v for v in ov if v in nv]
    if [nv.index(v) for v in common] != sorted(nv.index(v) for v in common):
        out.append(_f(DATA, "enum-values-reordered", label,
                      f"enum values reordered relative to each other — the ordinal stored "
                      f"in existing rows now means a different value ({ov} → {nv})",
                      ov, nv))
    for v in nv:
        if v not in ov and nv.index(v) < len(ov):
            out.append(_f(DATA, "enum-value-inserted", label,
                          f'enum value "{v}" inserted at position {nv.index(v)} rather '
                          f'than appended — it shifts every ordinal after it', None, v))
        elif v not in ov:
            out.append(_f(SAFE, "enum-value-added", label, f'enum value "{v}" appended',
                          None, v))


def _diff_methods(old, new, label, out):
    for name, om in old["methods"].items():
        if not om["public"] and not om["event"]:
            continue                      # internal surface is not a contract
        nm = new["methods"].get(name)
        what = "event" if om["event"] else "public procedure"
        if nm is None:
            out.append(_f(BREAKING, "member-removed", label,
                          f'{what} {om["signature"]} removed — '
                          + ("subscribers stop binding" if om["event"]
                             else "callers stop compiling"), om["signature"], None))
            continue
        if om["signature"] != nm["signature"]:
            # Subscribers bind by parameter NAME, so any change here is breaking.
            out.append(_f(BREAKING, "signature-changed", label,
                          f'{what} signature changed:\n      was {om["signature"]}\n'
                          f'      now {nm["signature"]}', om["signature"], nm["signature"]))
        if om["event"] and not nm["event"]:
            out.append(_f(BREAKING, "event-demoted", label,
                          f'{name} is no longer an event ({om["event"]} removed)',
                          om["event"], None))
        if not om["obsolete"] and nm["obsolete"]:
            out.append(_f(WARNING, "member-obsoleted", label,
                          f'{what} {name} marked Obsolete::{nm["obsolete"]}',
                          None, nm["obsolete"]))


def _diff_api(old, new, label, out):
    if not old["api"] and not new["api"]:
        return
    for k in sorted(set(old["api"]) | set(new["api"])):
        o, n = old["api"].get(k), new["api"].get(k)
        if o != n:
            out.append(_f(BREAKING, "api-contract-changed", label,
                          f"API {k} changed {o!r} → {n!r} — the published endpoint URL "
                          f"or payload shape moves", o, n))


def diff(old, new):
    """[finding] between two surfaces, most severe first."""
    out = []
    o_objs, n_objs = old["objects"], new["objects"]
    o_names, n_names = _by_name(o_objs), _by_name(n_objs)

    for key, orec in sorted(o_objs.items(), key=lambda x: (x[0][0], str(x[0][1]))):
        kind, oid = key
        label = f'{kind} {oid} "{orec["name"]}"'
        nrec = n_objs.get(key)
        if nrec is None:
            # Same name at a different ID is a RENUMBER, not a deletion — and not the
            # same object either. Saying "deleted" would hide the cause; treating them as
            # equal would be the false equivalence this must avoid.
            same_name = n_names.get((kind, (orec["name"] or "").lower()))
            if same_name:
                nid = same_name[0][0]
                sev = DATA if kind in _DATA_KINDS else BREAKING
                out.append(_f(sev, "object-renumbered", label,
                              f'{kind} "{orec["name"]}" moved from id {oid} to {nid}'
                              + (" — stored rows stay under the old object id"
                                 if kind == "table" else ""), oid, nid))
                nrec = same_name[0][1]
            else:
                out.append(_f(DATA if kind in _DATA_KINDS else BREAKING, "object-deleted",
                              label, f"{label} no longer exists"
                              + (" — its table and data are dropped" if kind == "table"
                                 else ""), orec["name"], None))
                continue
        elif (orec["name"] or "").lower() != (nrec["name"] or "").lower():
            out.append(_f(WARNING, "object-renamed", label,
                          f'{kind} {oid} renamed "{orec["name"]}" → "{nrec["name"]}"',
                          orec["name"], nrec["name"]))

        if not orec["obsolete"] and nrec["obsolete"]:
            out.append(_f(WARNING, "object-obsoleted", label,
                          f'marked Obsolete::{nrec["obsolete"]}'
                          + (f' ({nrec["obsolete_reason"]})' if nrec["obsolete_reason"] else ""),
                          None, nrec["obsolete"]))
        _diff_fields(orec, nrec, label, out)
        _diff_keys(orec, nrec, label, out)
        _diff_values(orec, nrec, label, out)
        _diff_methods(orec, nrec, label, out)
        _diff_api(orec, nrec, label, out)

    for key, nrec in sorted(n_objs.items(), key=lambda x: (x[0][0], str(x[0][1]))):
        if key not in o_objs and not o_names.get((key[0], (nrec["name"] or "").lower())):
            out.append(_f(SAFE, "object-added", key[0] + f' {key[1]} "{nrec["name"]}"',
                          f'new {key[0]} "{nrec["name"]}"', None, nrec["name"]))

    o_dep = {d.get("Id"): d for d in old["dependencies"]}
    n_dep = {d.get("Id"): d for d in new["dependencies"]}
    for i, d in o_dep.items():
        if i not in n_dep:
            out.append(_f(WARNING, "dependency-removed", "app",
                          f'dependency "{d.get("Name")}" removed', d.get("Name"), None))
        elif d.get("MinVersion") != n_dep[i].get("MinVersion"):
            out.append(_f(WARNING, "dependency-version-raised", "app",
                          f'dependency "{d.get("Name")}" min version '
                          f'{d.get("MinVersion")} → {n_dep[i].get("MinVersion")}',
                          d.get("MinVersion"), n_dep[i].get("MinVersion")))
    for i, d in n_dep.items():
        if i not in o_dep:
            out.append(_f(WARNING, "dependency-added", "app",
                          f'new dependency "{d.get("Name")}" '
                          f'{d.get("MinVersion") or ""}'.strip(), None, d.get("Name")))

    out.sort(key=lambda f: (-_RANK[f["severity"]], f["object"], f["rule"]))
    return out


def verdict(findings):
    """The worst severity present — the one that decides whether this can ship."""
    return max((f["severity"] for f in findings), key=lambda s: _RANK[s], default=SAFE)


def analyse(old_app, new_app):
    o, n = surface(old_app), surface(new_app)
    findings = diff(o, n)
    return {"from": {"name": o["name"], "version": o["version"], "path": o["path"]},
            "to": {"name": n["name"], "version": n["version"], "path": n["path"]},
            "same_app_id": o["app_id"] == n["app_id"],
            "verdict": verdict(findings), "findings": findings,
            "counts": {s: sum(1 for f in findings if f["severity"] == s)
                       for s in (DATA, BREAKING, WARNING, SAFE)}}


def format_report(res, limit=60, include_safe=False):
    f_ = res["from"], res["to"]
    lines = [f'UPGRADE ANALYSIS  {f_[0]["name"]} {f_[0]["version"]} → '
             f'{f_[1]["name"]} {f_[1]["version"]}',
             f'  VERDICT: {res["verdict"]}   '
             + "  ".join(f"{k}={v}" for k, v in res["counts"].items() if v)]
    if not res["same_app_id"]:
        lines.append("  ⚠ these are DIFFERENT apps (app id differs) — an upgrade "
                     "comparison between them is not meaningful")
    shown = [f for f in res["findings"] if include_safe or f["severity"] != SAFE]
    for f in shown[:limit]:
        lines.append(f'  [{f["severity"]}] {f["object"]} — {f["rule"]}')
        lines.append(f'      {f["detail"]}')
    if len(shown) > limit:
        lines.append(f"  … and {len(shown) - limit} more")
    if not shown:
        lines.append("  no upgrade risks found (additive changes only)")
    return "\n".join(lines)


def main():
    import argparse
    ap = argparse.ArgumentParser(prog="al_upgrade",
                                 description="compare two .app versions for upgrade risk")
    ap.add_argument("old_app")
    ap.add_argument("new_app")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--all", action="store_true", help="include SAFE findings")
    ap.add_argument("--fail-on", default="BREAKING",
                    choices=[SAFE, WARNING, BREAKING, "DATA"],
                    help="minimum severity that exits non-zero")
    a = ap.parse_args()
    try:
        res = analyse(a.old_app, a.new_app)
    except (FileNotFoundError, KeyError, zipfile.BadZipFile) as e:
        print(f"ERROR: {e}")
        return 2
    print(json.dumps(res, indent=2) if a.json
          else format_report(res, include_safe=a.all))
    floor = DATA if a.fail_on == "DATA" else a.fail_on
    return 1 if _RANK[res["verdict"]] >= _RANK[floor] else 0


if __name__ == "__main__":
    raise SystemExit(main())
