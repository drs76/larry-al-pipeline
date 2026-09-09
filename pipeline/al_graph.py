"""al_graph — the extension as a graph, so "what does this change break?" is answerable.

Every other instrument here judges one file at a time. The questions that actually cost
time are about reach: if this table changes, which pages and codeunits care? If this
codeunit changes, which tests cover it? Those are graph queries, and without a graph they
get answered by grep and optimism.

Nodes are the project's own objects plus the external ones it touches; external names are
resolved against the downloaded symbols, so `Codeunit "Sales-Post"` becomes a real object
with a kind and an id rather than a string.

Edges are stated as facts about the source, not inferences:

    extends         a tableextension/pageextension names its target
    subscribes-to   an [EventSubscriber] binds to a publisher's event
    publishes       an object declares an [IntegrationEvent]/[BusinessEvent]
    uses-table      a record variable, Database::X, or SourceTable
    uses-field      a field referenced through a known record variable
    calls           a codeunit variable is invoked
    references      any other typed reference (page, report, enum, interface)
    tested-by       a Subtype=Test codeunit reaches the object

Two acceptance criteria shape the implementation more than the rest. The graph must be
REPRODUCIBLE — so everything is sorted and nothing carries a timestamp or an absolute
path — and generation must not touch the source tree, so this only ever reads.

Deterministic, offline, no model.
"""
from __future__ import annotations

import glob
import json
import os
import re

import al_symbols
import event_verify

# `codeunit 50100 "Name"` / `tableextension 50101 "Name" extends "Sales Header"`
_DECL_RE = re.compile(
    r'^\s*(?P<kind>table|tableextension|page|pageextension|codeunit|report|reportextension|'
    r'query|xmlport|enum|enumextension|interface|permissionset|permissionsetextension|'
    r'controladdin|profile|pagecustomization)\s+'
    r'(?P<id>\d+)\s*(?P<name>"[^"]+"|\w+)'
    r'(?:\s+(?P<rel>extends|implements)\s+(?P<target>"[^"]+"|[\w.]+))?',
    re.IGNORECASE)
# An object DECLARATION carries an id (`page 50106 "Name"`). A permission-set BODY
# references objects without one (`page "Name";`), and matching those pulled whole mangled
# lines into the graph as if they were objects.
#
# Four AL object kinds legitimately have NO id — interface, controladdin, profile and
# pagecustomization — so they need their own pattern. Requiring an id across the board
# silently dropped every control add-in from the graph.
_NOID_RE = re.compile(
    r'^\s*(?P<kind>interface|controladdin|profile|pagecustomization)\s+'
    r'(?P<name>"[^"]+"|\w+)', re.IGNORECASE)
# `Cust: Record Customer;` / `Post: Codeunit "Sales-Post";`
_VAR_RE = re.compile(
    r'^\s*(?P<var>\w+)\s*:\s*(?P<type>Record|Codeunit|Page|Report|Query|XmlPort|Enum|'
    r'Interface|TestPage)\s+(?P<obj>"[^"]+"|[\w.]+)', re.IGNORECASE)
_DB_REF_RE = re.compile(r'\b(?:Database|Codeunit|Page|Report|Enum|Query|XmlPort)\s*::\s*'
                        r'(?P<obj>"[^"]+"|\w+)')
_SOURCETABLE_RE = re.compile(r'^\s*SourceTable\s*=\s*(?P<obj>"[^"]+"|\w+)\s*;', re.IGNORECASE)
_PUBLISH_RE = re.compile(r'\[\s*(IntegrationEvent|BusinessEvent|InternalEvent)\s*\(',
                         re.IGNORECASE)
_PROC_RE = re.compile(r'^\s*(?:local\s+|internal\s+)?procedure\s+(?P<name>\w+|"[^"]+")',
                      re.IGNORECASE)
# `procedure P(var Cust: Record Customer; Post: Codeunit "Sales-Post")`. Parameters are
# how an event subscriber references the tables it acts on, so a graph that only reads
# var BLOCKS misses the document flow entirely — which is most of what a process map is.
_PARAM_RE = re.compile(
    r'(?:var\s+)?(?P<var>\w+)\s*:\s*(?P<type>Record|Codeunit|Page|Report|Query|XmlPort|'
    r'Enum|Interface|TestPage)\s+(?P<obj>"[^"]+"|[\w.]+)', re.IGNORECASE)
_TEST_RE = re.compile(r'^\s*Subtype\s*=\s*Test\s*;', re.IGNORECASE)
_MASK = re.compile(r"'(?:[^']|'')*'|//.*$")


def _unq(t):
    """Bare object/field name.

    The dot means two different things. In `System.Azure.Storage."ABS Blob Client"` it is
    a namespace separator; inside `"No."` it is part of the name. Splitting
    unconditionally — which is what a namespace-stripper naturally does — turns half the
    fields in Business Central into empty strings.
    """
    t = (t or "").strip()
    if t.startswith('"'):
        return t.strip('"').strip()
    if "." in t and '"' in t:                  # Namespace."Quoted Name"
        return t[t.index('"'):].strip('"').strip()
    return t.split(".")[-1].strip()


def _read(path):
    """Lines with string literals and comments blanked. Quoted identifiers are KEPT —
    they are object and field names, which is the entire subject here."""
    try:
        txt = open(path, encoding="utf-8-sig", errors="replace").read()
    except OSError:
        return []
    return [_MASK.sub(lambda m: " " * len(m.group(0)), ln) for ln in txt.splitlines()]


def _node_id(kind, name, raw=False):
    return f"{kind.lower()}:{(name if raw else _unq(name)).lower()}"


def build(project_root, idx=None):
    """{nodes, edges, project} for one extension. Reads only."""
    src = os.path.join(project_root, "src")
    src = src if os.path.isdir(src) else project_root
    if idx is None:
        pkgs = os.path.join(project_root, ".alpackages")
        idx = al_symbols.build_index(pkgs) if os.path.isdir(pkgs) else {}

    nodes, edges, own = {}, [], set()

    def add_node(kind, name, raw=False, **kw):
        # Field and event nodes are COMPOSITE ("My Equip.No.", "Sales-Post.OnAfterPost").
        # Running them through _unq again splits on the separator — and on the dot inside
        # "No." — which is how a graph fills up with nodes called "".
        nid = _node_id(kind, name, raw)
        n = nodes.setdefault(nid, {"id": nid, "kind": kind.lower(),
                                   "name": name if raw else _unq(name),
                                   "internal": False, "test": False, "file": "",
                                   "obj_id": None, "package": ""})
        n.update({k: v for k, v in kw.items() if v not in (None, "", False)})
        return nid

    def add_edge(a, b, rel, detail=""):
        if a and b and a != b:
            edges.append({"from": a, "to": b, "rel": rel, "detail": detail})

    files = sorted(glob.glob(os.path.join(src, "**", "*.al"), recursive=True))

    # Pass 1: what this project defines. Needed before any reference is classified, or a
    # project's own object looks external.
    for path in files:
        for ln in _read(path):
            m = _DECL_RE.match(ln)
            if m and m.group("name"):
                own.add(_node_id(m.group("kind"), m.group("name")))
            else:
                mi = _NOID_RE.match(ln)
                if mi:
                    own.add(_node_id(mi.group("kind"), mi.group("name")))

    for path in files:
        lines = _read(path)
        rel = os.path.relpath(path, project_root)
        cur, cur_vars, is_test = None, {}, any(_TEST_RE.match(l) for l in lines)

        for i, ln in enumerate(lines):
            m = _DECL_RE.match(ln) or _NOID_RE.match(ln)
            if m and m.group("name"):
                kind, name = m.group("kind").lower(), m.group("name")
                _oid = m.groupdict().get("id")
                cur = add_node(kind, name, internal=True, file=rel, test=is_test,
                               obj_id=int(_oid) if _oid else None)
                cur_vars = {}
                if m.groupdict().get("target"):
                    rel = (m.groupdict().get("rel") or "extends").lower()
                    if rel == "implements":
                        # An `implements` target is always an INTERFACE. Typing it as the
                        # implementing object's kind created a separate phantom node per
                        # implementer — one interface appeared three times, as a codeunit,
                        # an enum and an interface.
                        tgt_kind = "interface"
                    else:
                        tgt_kind = {"tableextension": "table", "pageextension": "page",
                                    "enumextension": "enum", "reportextension": "report",
                                    "permissionsetextension": "permissionset",
                                    "pagecustomization": "page"}.get(kind, kind)
                    add_edge(cur, _resolve(add_node, idx, own, tgt_kind, m.group("target")),
                             rel)
                continue
            if not cur:
                continue

            pm2 = _PROC_RE.match(ln)
            if pm2:
                for am in _PARAM_RE.finditer(ln):
                    typ, obj = am.group("type").lower(), am.group("obj")
                    k = {"record": "table", "testpage": "page"}.get(typ, typ)
                    tid = _resolve(add_node, idx, own, k, obj)
                    cur_vars[am.group("var").lower()] = (k, _unq(obj), tid)
                    add_edge(cur, tid, "uses-table" if k == "table" else
                             ("calls" if k == "codeunit" else "references"))

            vm = _VAR_RE.match(ln)
            if vm:
                typ, obj = vm.group("type").lower(), vm.group("obj")
                kind = {"record": "table", "testpage": "page"}.get(typ, typ)
                tid = _resolve(add_node, idx, own, kind, obj)
                cur_vars[vm.group("var").lower()] = (kind, _unq(obj), tid)
                add_edge(cur, tid, "uses-table" if kind == "table" else
                         ("calls" if kind == "codeunit" else "references"))
                continue

            sm = _SOURCETABLE_RE.match(ln)
            if sm:
                add_edge(cur, _resolve(add_node, idx, own, "table", sm.group("obj")),
                         "uses-table", "SourceTable")
                continue

            if _PUBLISH_RE.search(ln):
                for j in range(i + 1, min(len(lines), i + 4)):
                    pm = _PROC_RE.match(lines[j])
                    if pm:
                        ev = add_node("event",
                                      f'{nodes[cur]["name"]}.{_unq(pm.group("name"))}',
                                      raw=True, internal=True, file=rel)
                        add_edge(cur, ev, "publishes")
                        break

            for dm in _DB_REF_RE.finditer(ln):
                kw = ln[max(0, dm.start() - 12):dm.start()].lower()
                kind = ("table" if "database" in kw else
                        next((k for k in ("codeunit", "page", "report", "enum", "query",
                                          "xmlport") if k in kw), "table"))
                add_edge(cur, _resolve(add_node, idx, own, kind, dm.group("obj")),
                         "uses-table" if kind == "table" else "references")

            # `Cust."No."` — a field reference through a variable whose table is known.
            for fm in re.finditer(r'\b(\w+)\s*\.\s*("(?:[^"]+)")', ln):
                v = cur_vars.get(fm.group(1).lower())
                if v and v[0] == "table" and _unq(fm.group(2)):
                    fid = add_node("field", f'{v[1]}.{_unq(fm.group(2))}', raw=True,
                                   internal=v[2] in own)
                    add_edge(cur, fid, "uses-field")
                    add_edge(fid, v[2], "belongs-to")

        # Subscriptions carry the publisher AND the event name; event_verify already
        # parses that attribute correctly, including numeric object references.
        for sub in event_verify.parse_subscribers(path):
            src_node = _node_id("codeunit", os.path.basename(path).split(".")[0])
            src_node = cur or src_node
            pub = _resolve(add_node, idx, own, sub["object_type"], sub["object"])
            ev = add_node("event", f'{nodes[pub]["name"]}.{sub["event"]}', raw=True)
            add_edge(src_node, ev, "subscribes-to", sub["proc"])
            add_edge(pub, ev, "publishes")

    # tested-by: a test codeunit's outgoing edges are the objects it exercises.
    for n in [v for v in nodes.values() if v.get("test")]:
        for e in [e for e in edges if e["from"] == n["id"] and e["rel"] != "tested-by"]:
            add_edge(e["to"], n["id"], "tested-by")

    edges = sorted({(e["from"], e["to"], e["rel"], e["detail"]) for e in edges})
    return {"project": os.path.basename(project_root.rstrip("/")),
            "nodes": [nodes[k] for k in sorted(nodes)],
            "edges": [{"from": a, "to": b, "rel": r, "detail": d}
                      for a, b, r, d in edges]}


def _resolve(add_node, idx, own, kind, name):
    """A referenced object becomes a node, external ones carrying their symbol evidence."""
    nid = _node_id(kind, name)
    if nid in own:
        return add_node(kind, name)
    rec = None
    if idx:
        n = _unq(name)
        rec = al_symbols.lookup_id(idx, kind, n) if n.isdigit() else al_symbols.lookup(idx, n)
    if rec:
        # A symbol name is already bare and may legitimately END in a dot
        # ("Customer Templ. Mgt."). Re-parsing it as a namespaced reference splits it away
        # to nothing.
        return add_node(rec["kind"], rec["name"], raw=True, obj_id=rec.get("id"),
                        package=rec.get("pkg", ""))
    return add_node(kind, name)


# ─── queries ───────────────────────────────────────────────────────────────────

def _adj(graph, reverse=False):
    out = {}
    for e in graph["edges"]:
        a, b = (e["to"], e["from"]) if reverse else (e["from"], e["to"])
        out.setdefault(a, set()).add(b)
    return out


def find(graph, term):
    """Node ids matching a name or id — callers ask about "Equipment", not "table:equipment"."""
    t = _unq(term).lower()
    return sorted(n["id"] for n in graph["nodes"]
                  if n["id"] == t or n["name"].lower() == t or n["id"].endswith(":" + t))


def affected_by(graph, term, depth=None):
    """What breaks if `term` changes — everything that reaches it, transitively.

    Direction matters and is easy to get backwards: this walks edges BACKWARDS, from a
    node to its dependents. Walking forwards answers "what does this need", which is a
    different question and useless for impact.
    """
    return _reach(graph, term, _adj(graph, reverse=True), depth)


def depends_on(graph, term, depth=None):
    return _reach(graph, term, _adj(graph), depth)


def _reach(graph, term, adj, depth):
    seen, frontier, out, d = set(find(graph, term)), set(find(graph, term)), {}, 0
    while frontier and (depth is None or d < depth):
        d += 1
        nxt = set()
        for n in frontier:
            for m in adj.get(n, ()):
                if m not in seen:
                    seen.add(m)
                    out[m] = d
                    nxt.add(m)
        frontier = nxt
    return dict(sorted(out.items(), key=lambda kv: (kv[1], kv[0])))


def tests_for(graph, terms):
    """Test codeunits that reach any of `terms` — the input to a targeted test run.

    Empty is a real answer meaning "nothing covers this", and must not be read as
    "everything passes".
    """
    tests = {n["id"] for n in graph["nodes"] if n.get("test")}
    hit = set()
    for t in terms if isinstance(terms, (list, tuple, set)) else [terms]:
        hit |= {n for n in affected_by(graph, t) if n in tests}
        hit |= {n for n in find(graph, t) if n in tests}
    return sorted(hit)


def mermaid(graph, limit=60):
    """A diagram of the internal objects. External nodes are omitted — a graph with the
    whole Base Application in it is not readable and not the question being asked."""
    ids, out = {}, ["graph LR"]
    internal = [n for n in graph["nodes"] if n.get("internal")][:limit]
    keep = {n["id"] for n in internal}
    shape = {"table": ("[", "]"), "codeunit": ("([", "])"), "page": ("[/", "/]"),
             "event": (">", "]"), "enum": ("{{", "}}")}
    for i, n in enumerate(internal):
        ids[n["id"]] = f"n{i}"
        a, b = shape.get(n["kind"], ("[", "]"))
        out.append(f'  {ids[n["id"]]}{a}"{n["kind"]} {n["name"]}"{b}')
    for e in graph["edges"]:
        if e["from"] in keep and e["to"] in keep:
            out.append(f'  {ids[e["from"]]} -->|{e["rel"]}| {ids[e["to"]]}')
    return "\n".join(out)


def summary(graph):
    kinds, rels = {}, {}
    for n in graph["nodes"]:
        k = n["kind"] + ("" if n.get("internal") else " (external)")
        kinds[k] = kinds.get(k, 0) + 1
    for e in graph["edges"]:
        rels[e["rel"]] = rels.get(e["rel"], 0) + 1
    return (f'{graph["project"]}: {len(graph["nodes"])} nodes, {len(graph["edges"])} edges\n'
            "  nodes: " + ", ".join(f"{k}={v}" for k, v in sorted(kinds.items())) + "\n"
            "  edges: " + ", ".join(f"{k}={v}" for k, v in sorted(rels.items())))


def main():
    import argparse
    ap = argparse.ArgumentParser(prog="al_graph")
    ap.add_argument("root", nargs="?", default=".")
    ap.add_argument("--affected", metavar="OBJECT", help="what breaks if OBJECT changes")
    ap.add_argument("--depends", metavar="OBJECT", help="what OBJECT needs")
    ap.add_argument("--tests", metavar="OBJECT", help="test codeunits covering OBJECT")
    ap.add_argument("--mermaid", action="store_true")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    g = build(os.path.abspath(a.root))

    if a.json:
        print(json.dumps(g, indent=2, sort_keys=True))
    elif a.mermaid:
        print(mermaid(g))
    elif a.affected or a.depends:
        term = a.affected or a.depends
        fn = affected_by if a.affected else depends_on
        hits = fn(g, term)
        if not find(g, term):
            print(f"no node matches {term!r}")
            return 2
        verb = "is affected by a change to" if a.affected else "is needed by"
        print(f"{len(hits)} node(s) {verb} {term}:")
        for n, d in hits.items():
            print(f"  [{d}] {n}")
    elif a.tests:
        t = tests_for(g, a.tests)
        print("\n".join(t) if t else
              f"no test codeunit reaches {a.tests} — that is 'untested', not 'passing'")
    else:
        print(summary(g))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
