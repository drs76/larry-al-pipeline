#!/usr/bin/env python3
"""
al_symbols — look up REAL AL object declarations from downloaded symbol packages.

Why this rather than indexing the GitHub source:

  * **Version-exact.** These are the very symbols `al compile` resolves against, pulled
    into `.alpackages` by `al_downloadsymbols` on every build. A GitHub clone drifts from
    whatever runtime the project targets; this cannot.
  * **No refresh problem.** Symbols are re-downloaded per build, so the lookup table is
    current by construction — no `git pull`, no periodic reindex, no staleness window.
  * **Covers the Base Application**, which the indexed source corpora do not. That gap is
    exactly what left `Document Attachment` ungroundable.
  * **Cheap.** One 56 MB JSON per package, parsed once and cached as a compact index.

A `.app` is a plain zip holding `SymbolReference.json`. Objects live in a `Namespaces`
tree (only a handful sit at top level), so the walk has to recurse.

  al_symbols.py lookup <name> [--dir .alpackages]     what IS this object
  al_symbols.py members <name> [--dir .alpackages]    what does it really provide
  al_symbols.py stats [--dir .alpackages]

Used by run-build.py's RAG grounding to correct hallucinated types and members.
"""
import os, sys, json, glob, zipfile, argparse, hashlib

KINDS = ("Tables", "Codeunits", "Pages", "EnumTypes", "Interfaces",
         "Reports", "Queries", "XmlPorts", "PermissionSets", "ControlAddIns")
SINGULAR = {"Tables": "table", "Codeunits": "codeunit", "Pages": "page", "EnumTypes": "enum",
            "Interfaces": "interface", "Reports": "report", "Queries": "query",
            "XmlPorts": "xmlport", "PermissionSets": "permissionset",
            "ControlAddIns": "controladdin"}
CACHE_DIR = os.path.expanduser("~/.cache/al-symbols")


# Bumped whenever the record shape changes: a cache written by an older version would
# silently lack the new fields (pkg/pkg_version), and callers would read absent evidence
# as "no evidence" rather than "stale cache".
INDEX_SCHEMA = 4   # 4: obsolete markers captured from method attributes


def _cache_key(pkgs):
    h = hashlib.sha1()
    h.update(f"schema{INDEX_SCHEMA}".encode())
    for p in sorted(pkgs):
        st = os.stat(p)
        h.update(f"{os.path.basename(p)}:{st.st_size}:{int(st.st_mtime)}".encode())
    return h.hexdigest()[:16]


def _tname(td):
    """Render a TypeDefinition: 'Code[20]', 'Record "Sales Header"'."""
    if not td:
        return "Variant"
    n = td.get("Name", "") or "Variant"
    sub = td.get("Subtype")
    if isinstance(sub, dict) and sub.get("Name"):
        return f'{n} "{sub["Name"]}"'
    return n


def _sig(m):
    """Full signature with real param NAMES + types (event subscribers bind by name), and the
    [IntegrationEvent]/[BusinessEvent] marker so a corrected subscriber matches exactly."""
    ps = ", ".join(f'{p.get("Name","")}: {_tname(p.get("TypeDefinition"))}'
                   for p in (m.get("Parameters") or []))
    ret = m.get("ReturnTypeDefinition")
    r = f": {_tname(ret)}" if ret and ret.get("Name") else ""
    ev = next((a.get("Name") for a in (m.get("Attributes") or []) if "Event" in (a.get("Name") or "")), None)
    return f'{("[" + ev + "] ") if ev else ""}{m.get("Name","")}({ps}){r}'


def _obsolete(m):
    """'reason (since 25.0)' if the method is marked Obsolete, else None.

    Subscribing to an obsolete event compiles — usually with a warning that drowns in a
    long build log — and then breaks on the version that removes it. Symbols carry the
    reason and the version, so the warning can be specific instead of generic.
    """
    for a in (m.get("Attributes") or []):
        if (a.get("Name") or "") != "Obsolete":
            continue
        args = [str(x.get("Value", "")) for x in (a.get("Arguments") or [])]
        reason = args[0] if args else ""
        ver = args[1] if len(args) > 1 else ""
        return (reason or "obsolete") + (f" (since {ver})" if ver else "")
    return None


def _walk(node, ns, out, pkg="", pkg_ver=""):
    for kind in KINDS:
        for o in node.get(kind) or []:
            name = o.get("Name")
            if not name:
                continue
            members = [f.get("Name") for f in (o.get("Fields") or []) if f.get("Name")]
            members += [m.get("Name") for m in (o.get("Methods") or []) if m.get("Name")]
            values = [v.get("Name") for v in (o.get("Values") or []) if v.get("Name")]
            sigs = {m["Name"]: _sig(m) for m in (o.get("Methods") or []) if m.get("Name")}
            obs = {m["Name"]: _obsolete(m) for m in (o.get("Methods") or [])
                   if m.get("Name") and _obsolete(m)}
            rec = {"kind": SINGULAR.get(kind, kind.lower()), "id": o.get("Id"),
                   "name": name, "ns": ns, "members": sorted(set(members + values)),
                   "sigs": sigs, "obsolete": obs,
                   # Provenance: an API claim has to be traceable to the package and
                   # version it came from, or it is just a nicer-looking guess.
                   "pkg": pkg, "pkg_version": pkg_ver}
            # keep the richest record if a name appears in several packages
            prev = out.get(name.lower())
            if not prev or len(rec["members"]) > len(prev["members"]):
                out[name.lower()] = rec
    for sub in node.get("Namespaces") or []:
        _walk(sub, (ns + "." + (sub.get("Name") or "")).strip("."), out, pkg, pkg_ver)


# Extension objects add members to an object that already exists. Indexing them as
# separate records would be useless — nobody writes `"Error Message Extension"."Field"` —
# while NOT indexing them makes a legitimate extension field look invented, which is the
# false accusation the verifier must never make.
EXT_KINDS = ("TableExtensions", "EnumExtensionTypes", "PageExtensions")


def _merge_extensions(node, out, pkg=""):
    """Fold every extension's fields/values/methods into its target object's record."""
    for kind in EXT_KINDS:
        for o in node.get(kind) or []:
            target = (o.get("TargetObject") or "").strip()
            if not target:
                continue
            # Targets in the symbol file can be namespace-hashed:
            #   "#63ca2f…#Feature To Update" — the readable name is the last segment.
            if target.startswith("#") and "#" in target[1:]:
                target = target.rsplit("#", 1)[-1]
            rec = out.get(target.lower())
            if not rec:
                continue
            add = [f.get("Name") for f in (o.get("Fields") or []) if f.get("Name")]
            add += [v.get("Name") for v in (o.get("Values") or []) if v.get("Name")]
            add += [m.get("Name") for m in (o.get("Methods") or []) if m.get("Name")]
            if add:
                rec["members"] = sorted(set(rec["members"]) | set(add))
                rec.setdefault("extended_by", [])
                if pkg and pkg not in rec["extended_by"]:
                    rec["extended_by"].append(pkg)
            for m in (o.get("Methods") or []):
                if m.get("Name"):
                    rec["sigs"].setdefault(m["Name"], _sig(m))
    for sub in node.get("Namespaces") or []:
        _merge_extensions(sub, out, pkg)


def build_index(alpackages, use_cache=True):
    """{lowercased name: {kind,id,name,ns,members}} for every object in the packages."""
    pkgs = sorted(glob.glob(os.path.join(alpackages, "*.app")))
    if not pkgs:
        return {}
    key = _cache_key(pkgs)
    cache = os.path.join(CACHE_DIR, key + ".json")
    if use_cache and os.path.exists(cache):
        try:
            return json.load(open(cache))
        except Exception:
            pass
    idx, docs = {}, []
    for p in pkgs:
        try:
            raw = zipfile.ZipFile(p).read("SymbolReference.json")
            doc = json.loads(raw.decode("utf-8-sig"))
            _walk(doc, "", idx, os.path.basename(p),
                  str(doc.get("Version") or doc.get("AppVersion") or ""))
            docs.append((os.path.basename(p), doc))
        except Exception:
            continue          # a bad package must not break a build
    # Second pass: an extension may target an object defined in a package read later, so
    # every base object has to exist before any extension is folded in.
    for name, doc in docs:
        try:
            _merge_extensions(doc, idx, name)
        except Exception:
            continue
    if use_cache:
        try:
            os.makedirs(CACHE_DIR, exist_ok=True)
            json.dump(idx, open(cache, "w"))
        except OSError:
            pass
    return idx


def lookup(idx, name):
    """Exact (case-insensitive) match only. A near-miss is worse than no answer here:
    handing the model a plausible wrong object invents a new hallucination while
    claiming to correct one."""
    return idx.get((name or "").strip().strip('"').lower())


def lookup_id(idx, kind, obj_id):
    """Resolve an object by NUMBER — 'Database::1173' is as legal as a quoted name.

    Name-only resolution reports a numeric reference as a missing object, which is a
    false accusation against correct code. Kind matters: table 1173 and codeunit 1173
    are different objects.
    """
    try:
        want = int(str(obj_id).strip())
    except (TypeError, ValueError):
        return None
    kind = (kind or "").lower()
    for rec in idx.values():
        if rec.get("id") == want and (not kind or rec.get("kind") == kind):
            return rec
    return None


def find_member(idx, member, kind=None, events_only=False):
    """Every object exposing `member`, WITHOUT needing to know the object first.

    `lookup()` answers "what is this object"; this answers "does this procedure/event
    exist anywhere, and what is its real signature" — the question you actually have
    when a model writes an event subscriber. Several objects legitimately publish
    similarly-named events, so ALL matches are returned: collapsing them to one would
    reintroduce the guess this module exists to remove.

    Returns [{object, kind, id, ns, signature, is_event, event_kind, pkg, pkg_version}].
    """
    want = (member or "").strip().strip('"').lower()
    if not want:
        return []
    out = []
    for rec in idx.values():
        if kind and rec.get("kind") != kind:
            continue
        for mname, sig in (rec.get("sigs") or {}).items():
            if mname.lower() != want:
                continue
            ev = None
            if sig.startswith("["):
                ev = sig[1:sig.index("]")] if "]" in sig else None
            if events_only and not ev:
                continue
            out.append({"object": rec["name"], "kind": rec["kind"], "id": rec.get("id"),
                        "ns": rec.get("ns", ""), "signature": sig,
                        "is_event": bool(ev), "event_kind": ev,
                        "obsolete": (rec.get("obsolete") or {}).get(mname),
                        "pkg": rec.get("pkg", ""), "pkg_version": rec.get("pkg_version", "")})
    return sorted(out, key=lambda r: (r["object"], r["signature"]))


def find_event(idx, name):
    """Events only — the common case when verifying a subscriber.

    NOT FOUND HERE, and correctly so: table auto-generated trigger events
    (OnBeforeInsertEvent, OnAfterModifyEvent, OnBeforeValidateEvent, ...). The compiler
    SYNTHESISES those per table; they are not Methods in SymbolReference.json, so a
    lookup returns zero matches for a perfectly valid subscriber. Anything verifying
    subscribers must treat those names as valid-by-construction — see the
    _TABLE_EVENT_PARAMS table in run-build.py, which is where their fixed signatures
    live. Reporting them as "invented" would be a false positive on correct code.
    """
    return find_member(idx, name, events_only=True)


def find_field(idx, table, field=None):
    """Fields of a table. With `field`, confirm one exists; without, list them all.
    Returns (record_or_None, matches). A missing table and a missing field are
    different failures and the caller needs to tell them apart."""
    rec = lookup(idx, table)
    if not rec:
        return None, []
    members = rec.get("members") or []
    if field is None:
        return rec, list(members)
    want = field.strip().strip('"').lower()
    return rec, [m for m in members if m.lower() == want]


def find_enum(idx, enum, value=None):
    """Enum object + its values (values are indexed into `members`)."""
    return find_field(idx, enum, value)


def evidence(rec_or_match):
    """One-line provenance for any result — which package and version proves it."""
    pkg = rec_or_match.get("pkg") or "unknown package"
    ver = rec_or_match.get("pkg_version") or ""
    return f"{pkg}{(' v' + ver) if ver else ''}"


def declaration(rec):
    return f'{rec["kind"]} {rec["id"]} "{rec["name"]}"' + (f'  (namespace {rec["ns"]})' if rec["ns"] else "")


def main():
    ap = argparse.ArgumentParser(prog="al_symbols")
    ap.add_argument("cmd", choices=["lookup", "members", "stats", "event", "member",
                                    "field"])
    ap.add_argument("name", nargs="?", default="")
    ap.add_argument("--dir", default=".alpackages")
    ap.add_argument("--json", action="store_true",
                    help="machine-readable output (the reviewer consumes this)")
    a = ap.parse_args()
    idx = build_index(a.dir)
    if not idx:
        print(f"no symbol packages in {a.dir}", file=sys.stderr)
        return 1
    if a.cmd == "stats":
        import collections
        c = collections.Counter(v["kind"] for v in idx.values())
        print(f"  {len(idx)} objects: " + ", ".join(f"{k} {n}" for k, n in c.most_common()))
        return 0
    # Reverse lookups: answer "does this member exist" without knowing the object.
    if a.cmd in ("event", "member", "field"):
        if a.cmd == "field":
            obj, _, fld = a.name.partition(".")
            rec, matches = find_field(idx, obj, fld or None)
            res = {"query": a.name, "object_found": bool(rec),
                   "matches": matches,
                   "evidence": evidence(rec) if rec else None}
        else:
            found = (find_event if a.cmd == "event" else find_member)(idx, a.name)
            res = {"query": a.name, "match_count": len(found), "matches": found}
        if a.json:
            print(json.dumps(res, indent=2))
            return 0 if (res.get("matches") or res.get("object_found")) else 2
        if a.cmd == "field":
            if not res["object_found"]:
                print(f"object '{a.name.split('.')[0]}' not in the downloaded symbols")
                return 2
            print(f"{a.name}: {res['matches'] or 'NO SUCH FIELD'}   [{res['evidence']}]")
            return 0 if res["matches"] else 2
        if not res["matches"]:
            print(f"'{a.name}' does not exist in the downloaded symbols "
                  f"(note: table auto-events like OnBeforeInsertEvent are compiler-"
                  f"synthesised and never appear here — that is not an error)")
            return 2
        for m in res["matches"]:
            print(f'{m["kind"]} {m["id"]} "{m["object"]}"')
            print(f'    {m["signature"]}')
            print(f'    evidence: {evidence(m)}')
        return 0

    rec = lookup(idx, a.name)
    if not rec:
        print(f"'{a.name}' does not exist in the downloaded symbols")
        return 2
    if a.cmd == "lookup":
        print(declaration(rec))
    else:
        print(declaration(rec))
        sigs = rec.get("sigs") or {}
        events = [s for s in sigs.values() if s.startswith("[")]
        if events:
            print(f"  {len(events)} events (subscriber params bind BY NAME):")
            for s in events[:40]:
                print(f"    {s}")
        procs = [s for n, s in sigs.items() if not s.startswith("[")]
        if procs:
            print(f"  {len(procs)} procedures:")
            for s in procs[:40]:
                print(f"    {s}")
        fields = [m for m in rec["members"] if m not in sigs]
        if fields:
            print(f"  {len(fields)} fields/values: " + ", ".join(fields[:40]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
