"""al_process — where an extension sits in Business Central's actual business flow.

`al_graph` answers questions about objects: what calls what, what extends what. Those are
the right questions for a compiler and the wrong ones for a conversation with the person
paying for the extension. They ask what happens when an order is posted, what runs in the
background, and what leaves the building.

This lifts the object graph one level: each object is classified into a business STAGE by
the Business Central vocabulary it touches — `Sales-Post` is posting, `Cust. Ledger Entry`
is ledger, `Job Queue Entry` is background — and the object edges are collapsed into flows
between stages.

Classification is NAME MATCHING against base-app vocabulary, and that is a heuristic, not
a fact. Two consequences are designed in rather than hidden:

  * Anything unmatched lands in `unclassified` and is REPORTED. A process map that quietly
    drops what it did not recognise looks complete and is not, which is worse than a map
    with a gap you can see.
  * Every stage assignment carries the token that caused it, so a wrong classification can
    be traced to the word that produced it instead of being argued about.

Deterministic and offline: same source, same map. The three questions the handover asks
for — what does changing this event affect, where is this posting logic triggered, which
integrations run from this process — are the three query functions below.
"""
from __future__ import annotations

import os
import re

import al_graph

# BC's own vocabulary. Each entry is a name fragment that reliably identifies a stage —
# these are base-app object names, not guesses about what a customer might call things.
STAGES = {
    "document": {
        "why": "the order/invoice being worked on before anything is committed",
        "match": ["sales header", "sales line", "purchase header", "purchase line",
                  "service header", "service line", "transfer header", "assembly header",
                  "sales quote", "sales order", "purchase order"],
    },
    "release": {
        "why": "the approval/release step between editing and posting",
        "match": ["release sales document", "release purchase document",
                  "release service document", "approvals mgmt", "workflow"],
    },
    "posting": {
        "why": "where the transaction is actually committed",
        "match": ["-post", "post line", "posting", "gen. jnl.", "gen. journal",
                  "item jnl.", "invt. posting", "jnl.-post"],
    },
    "posted_document": {
        "why": "the immutable record left behind by posting",
        "match": ["invoice header", "shipment header", "receipt header",
                  "cr. memo header", "credit memo header", "posted "],
    },
    "ledger": {
        "why": "the financial and inventory effect — the numbers the business reports on",
        "match": ["ledger entry", "g/l entry", "vat entry", "value entry",
                  "detailed cust", "detailed vendor"],
    },
    "master_data": {
        "why": "the records the process reads from rather than produces",
        "match": ["customer", "vendor", "item", "resource", "employee", "contact",
                  "location", "bank account", "fixed asset"],
    },
    "setup": {
        "why": "configuration the process reads — BC's own word for it",
        "match": ["setup", "config", "parameters", "no. series", "template"],
    },
    "attachment": {
        "why": "documents and media hung off a record",
        "match": ["attachment", "tenant media", "media set", "document link",
                  "incoming document"],
    },
    "background": {
        "why": "work that runs without a user watching",
        "match": ["job queue", "task scheduler", "session", "isolated storage"],
    },
    "integration": {
        "why": "anything that leaves the building",
        "match": ["http", "abs ", "blob", "azure", "dataverse", "crm", "email",
                  "smtp", "web service", "api ", "oauth", "openai", "aoai",
                  "storage service", "copilot"],
    },
    "install_upgrade": {
        "why": "code that runs once, on deploy — and only then",
        "match": ["install", "upgrade", "data migration", "migration"],
    },
    "reporting": {
        "why": "read-only output",
        "match": ["report", "statement", "analysis", "chart"],
    },
}

# Codeunit subtypes are a STATED fact about the object, unlike a name match, so they win.
_SUBTYPE_RE = re.compile(r"^\s*SubType\s*=\s*(Install|Upgrade|Test)\s*;",
                         re.IGNORECASE | re.MULTILINE)
# The flow BC actually follows. Used to order a map and to tell forward from backward.
STAGE_ORDER = ["setup", "master_data", "document", "release", "posting",
               "posted_document", "ledger", "attachment", "reporting", "background",
               "integration", "install_upgrade", "unclassified"]


def _classify_name(name, kind=""):
    """(stage, matched_token). ("unclassified", "") when BC vocabulary does not place it."""
    low = f"{name}".lower()
    if kind == "report":
        return "reporting", "report object"
    best = None
    for stage, spec in STAGES.items():
        for tok in spec["match"]:
            if tok in low:
                # Longest match wins: "posted sales invoice header" is a posted document,
                # not master data because it contains "sales".
                if best is None or len(tok) > len(best[1]):
                    best = (stage, tok)
    return best if best else ("unclassified", "")


def _subtypes(project_root):
    """{object name lower: Install|Upgrade|Test} from the project's own source."""
    out = {}
    src = os.path.join(project_root, "src")
    src = src if os.path.isdir(src) else project_root
    for dp, dirs, fs in os.walk(src):
        dirs[:] = [d for d in dirs if d not in (".alpackages", "bin", "obj", ".git")]
        for fn in sorted(fs):
            if not fn.endswith(".al"):
                continue
            try:
                text = open(os.path.join(dp, fn), encoding="utf-8-sig",
                            errors="replace").read()
            except OSError:
                continue
            m = _SUBTYPE_RE.search(text)
            d = re.search(r'^\s*codeunit\s+\d+\s+("[^"]+"|\w+)', text,
                          re.IGNORECASE | re.MULTILINE)
            if m and d:
                out[d.group(1).strip('"').lower()] = m.group(1).capitalize()
    return out


def build(project_root, graph=None):
    """{stages, flows, objects, unclassified} — the object graph lifted to business flow."""
    g = graph or al_graph.build(project_root)
    subs = _subtypes(project_root)

    objects = {}
    for n in g["nodes"]:
        if n["kind"] in ("field", "event"):
            continue
        st, tok = _classify_name(n["name"], n["kind"])
        sub = subs.get(n["name"].lower())
        if sub in ("Install", "Upgrade"):
            # A stated Subtype beats a name match: a codeunit called "Sales Setup
            # Upgrade" is upgrade code whatever else its name contains.
            st, tok = "install_upgrade", f"Subtype = {sub}"
        objects[n["id"]] = {"id": n["id"], "name": n["name"], "kind": n["kind"],
                            "internal": bool(n.get("internal")), "stage": st,
                            "matched": tok}

    stages = {}
    for o in objects.values():
        s = stages.setdefault(o["stage"], {"objects": [], "internal": 0, "external": 0})
        s["objects"].append(o["id"])
        s["internal" if o["internal"] else "external"] += 1

    # Collapse object edges into stage-to-stage flows, keeping a witness edge for each so
    # a flow can always be traced back to the code that justifies it.
    flows = {}
    for e in g["edges"]:
        a, b = objects.get(e["from"]), objects.get(e["to"])
        if not a or not b or a["stage"] == b["stage"]:
            continue
        key = (a["stage"], b["stage"])
        f = flows.setdefault(key, {"from": a["stage"], "to": b["stage"], "count": 0,
                                   "via": []})
        f["count"] += 1
        if len(f["via"]) < 5:
            f["via"].append(f'{a["name"]} --{e["rel"]}--> {b["name"]}')

    return {
        "project": os.path.basename(project_root.rstrip("/")),
        "objects": objects,
        "stages": {k: dict(v, objects=sorted(v["objects"])) for k, v in stages.items()},
        "flows": [flows[k] for k in sorted(flows, key=lambda k: (
            STAGE_ORDER.index(k[0]) if k[0] in STAGE_ORDER else 99,
            STAGE_ORDER.index(k[1]) if k[1] in STAGE_ORDER else 99))],
        "unclassified": sorted(o["name"] for o in objects.values()
                               if o["stage"] == "unclassified"),
    }


# ─── the three questions the handover asks for ─────────────────────────────────

def event_impact(project_root, event_name, graph=None, proc=None):
    """"What does changing this event affect?" — the stages its subscribers sit in."""
    g = graph or al_graph.build(project_root)
    p = proc or build(project_root, g)
    want = event_name.strip().strip('"').lower()
    subs = [e["from"] for e in g["edges"]
            if e["rel"] == "subscribes-to" and want in e["to"].split(":", 1)[-1].lower()]
    pubs = [e["from"] for e in g["edges"]
            if e["rel"] == "publishes" and want in e["to"].split(":", 1)[-1].lower()]
    if not subs and not pubs:
        return {"event": event_name, "found": False,
                "detail": "no publisher or subscriber for that event in this project"}
    affected = {}
    for nid in subs:
        o = p["objects"].get(nid)
        if o:
            affected.setdefault(o["stage"], []).append(o["name"])
    return {"event": event_name, "found": True,
            "published_by": sorted({p["objects"][n]["name"] for n in pubs
                                    if n in p["objects"]}),
            "subscribers": sorted({p["objects"][n]["name"] for n in subs
                                   if n in p["objects"]}),
            "affects_stages": {k: sorted(set(v)) for k, v in sorted(affected.items())}}


def triggers_of(project_root, stage, graph=None, proc=None):
    """"Where is this posting logic triggered?" — what reaches the stage from outside it.

    Entry points are ranked: background and install/upgrade first, because code that runs
    with nobody watching is the answer people are usually missing.
    """
    g = graph or al_graph.build(project_root)
    p = proc or build(project_root, g)
    targets = {i for i, o in p["objects"].items() if o["stage"] == stage}
    if not targets:
        return {"stage": stage, "found": False,
                "detail": f"nothing in this project is classified as {stage}"}
    hits = {}
    for e in g["edges"]:
        if e["to"] in targets and e["from"] not in targets:
            o = p["objects"].get(e["from"])
            if o:
                hits.setdefault(o["stage"], set()).add(f'{o["name"]} ({e["rel"]})')
    rank = {"background": 0, "install_upgrade": 1, "integration": 2}
    return {"stage": stage, "found": True,
            "triggered_from": {k: sorted(v) for k, v in
                               sorted(hits.items(), key=lambda kv: rank.get(kv[0], 9))}}


def integrations_from(project_root, stage, graph=None, proc=None):
    """"Which integrations run from this process?" — outbound reach from a stage."""
    g = graph or al_graph.build(project_root)
    p = proc or build(project_root, g)
    start = {i for i, o in p["objects"].items() if o["stage"] == stage}
    if not start:
        return {"stage": stage, "found": False,
                "detail": f"nothing in this project is classified as {stage}"}
    adj = {}
    for e in g["edges"]:
        adj.setdefault(e["from"], set()).add(e["to"])
    seen, frontier = set(start), set(start)
    while frontier:
        nxt = set()
        for n in frontier:
            for m in adj.get(n, ()):
                if m not in seen:
                    seen.add(m)
                    nxt.add(m)
        frontier = nxt
    out = sorted({p["objects"][n]["name"] for n in seen
                  if n in p["objects"] and p["objects"][n]["stage"] == "integration"})
    return {"stage": stage, "found": True, "integrations": out,
            "detail": "reachable outbound calls" if out else
                      "nothing in this stage reaches an integration"}


def mermaid(proc):
    present = [s for s in STAGE_ORDER if s in proc["stages"]]
    ids = {s: f"s{i}" for i, s in enumerate(present)}
    out = ["graph LR"]
    for s in present:
        n = proc["stages"][s]
        out.append(f'  {ids[s]}["{s.replace("_", " ")}<br/>{len(n["objects"])} object(s)"]')
    for f in proc["flows"]:
        if f["from"] in ids and f["to"] in ids:
            out.append(f'  {ids[f["from"]]} -->|{f["count"]}| {ids[f["to"]]}')
    return "\n".join(out)


def report(proc):
    L = [f'# Business process map — {proc["project"]}', "",
         "Stages are matched against Business Central vocabulary. That is a heuristic: "
         "anything unmatched is listed at the bottom rather than dropped.", ""]
    for s in STAGE_ORDER:
        if s not in proc["stages"]:
            continue
        info = proc["stages"][s]
        why = STAGES.get(s, {}).get("why", "")
        L.append(f'## {s.replace("_", " ")}  ({info["internal"]} own, '
                 f'{info["external"]} base-app)')
        if why:
            L.append(f"_{why}_")
        for oid in info["objects"][:12]:
            o = proc["objects"][oid]
            tag = "" if o["internal"] else " _(base app)_"
            via = f'  — matched on "{o["matched"]}"' if o["matched"] else ""
            L.append(f'- {o["kind"]} **{o["name"]}**{tag}{via}')
        if len(info["objects"]) > 12:
            L.append(f'- _… and {len(info["objects"]) - 12} more_')
        L.append("")
    if proc["flows"]:
        L += ["## Flows", ""]
        for f in proc["flows"]:
            L.append(f'- {f["from"]} → {f["to"]}  ({f["count"]} edge(s))')
            for v in f["via"][:2]:
                L.append(f"    - {v}")
    return "\n".join(L)


def main():
    import argparse
    import json
    ap = argparse.ArgumentParser(prog="al_process",
                                 description="business-process view of an AL extension")
    ap.add_argument("root", nargs="?", default=".")
    ap.add_argument("--event", help="what does changing this event affect?")
    ap.add_argument("--triggers", metavar="STAGE", help="where is this stage triggered?")
    ap.add_argument("--integrations", metavar="STAGE",
                    help="which integrations run from this stage?")
    ap.add_argument("--mermaid", action="store_true")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    root = os.path.abspath(a.root)
    g = al_graph.build(root)
    p = build(root, g)

    if a.event:
        res = event_impact(root, a.event, g, p)
    elif a.triggers:
        res = triggers_of(root, a.triggers, g, p)
    elif a.integrations:
        res = integrations_from(root, a.integrations, g, p)
    else:
        res = None

    if res is not None:
        print(json.dumps(res, indent=2) if a.json else _fmt(res))
        return 0 if res.get("found", True) else 1
    print(json.dumps(p, indent=2, sort_keys=True) if a.json
          else (mermaid(p) if a.mermaid else report(p)))
    return 0


def _fmt(res):
    if not res.get("found", True):
        return res.get("detail", "not found")
    L = []
    if "event" in res:
        L.append(f'event {res["event"]}')
        if res.get("published_by"):
            L.append("  published by: " + ", ".join(res["published_by"]))
        for stage, names in res["affects_stages"].items():
            L.append(f"  affects {stage}: " + ", ".join(names))
        if not res["affects_stages"]:
            L.append("  no subscribers in this project")
    elif "triggered_from" in res:
        L.append(f'{res["stage"]} is reached from:')
        for stage, names in res["triggered_from"].items():
            L.append(f"  [{stage}] " + ", ".join(names))
    else:
        L.append(f'integrations reachable from {res["stage"]}:')
        L += [f"  {i}" for i in res["integrations"]] or [f'  {res["detail"]}']
    return "\n".join(L)


if __name__ == "__main__":
    raise SystemExit(main())
