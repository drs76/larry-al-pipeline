#!/usr/bin/env python3
"""classify.py — classify a Business Central Web Services export by publisher.

Usage:
    python classify.py EXPORT.tsv [--repo DIR]... [--isv "Name:LOW-HIGH,LOW-HIGH"]...
                                  [--json OUT.json] [--md OUT.md]

EXPORT is the Web Services page exported to Excel and saved as .tsv or .csv, or
the sheet pasted into a text file. Expected columns, header row optional:

    Object Type | Object ID | Object Name | Service Name | All Tenants | Published | OData V4 URL | SOAP URL

Only the first four are required.

--repo points at an AL source folder. Every app.json under it (excluding
.alpackages) contributes its publisher name and idRanges, so objects owned by
the customer's own extensions are recognised automatically.

--isv adds a publisher whose ranges are not in the local source, e.g.
    --isv "Continia Software:6085998-6086087,6225270-6225278"

The script counts. It does not infer intent. See the WARNINGS it prints.
"""
import sys
import os
import re
import csv
import json
import glob
import argparse
from collections import Counter, defaultdict

# Service-name patterns for endpoints that a Microsoft FEATURE creates by
# itself (Edit in Excel, Power Automate, the Power BI content pack, and so on).
# These are Microsoft's to replace, not the customer's. Anything not matching
# lands in the review list — which is NOT the same as "somebody created it on
# purpose". A stock installation also publishes rows. Never claim origin.
FEATURE_PATTERNS = [
    ("*_Excel",                      lambda s: s.endswith("_Excel")),
    ("ExcelTemplate*",               lambda s: s.startswith("ExcelTemplate")),
    ("Power_BI_* / powerbifinance",  lambda s: s.startswith("Power_BI_") or s == "powerbifinance"),
    ("workflow* / salesDocument* / purchaseDocument*",
     lambda s: s.startswith("workflow") or s.startswith("sales") or s.startswith("purchase")),
    ("AccountantPortal*",            lambda s: s.startswith("AccountantPortal")),
    ("UserTaskSetComplete",          lambda s: s == "UserTaskSetComplete"),
]

FEATURE_SOURCE = {
    "*_Excel": "Edit in Excel",
    "ExcelTemplate*": "Financial reporting Excel templates",
    "Power_BI_* / powerbifinance": "Power BI content pack",
    "workflow* / salesDocument* / purchaseDocument*": "Power Automate approval workflows",
    "AccountantPortal*": "Accountant portal",
    "UserTaskSetComplete": "User tasks",
}


def parse_ranges(spec):
    out = []
    for part in spec.split(","):
        part = part.strip()
        if not part:
            continue
        lo, _, hi = part.partition("-")
        out.append((int(lo), int(hi or lo)))
    return out


def load_local_apps(repo_dirs):
    """Read every app.json under each repo dir, skipping .alpackages."""
    apps = []
    for d in repo_dirs:
        for path in glob.glob(os.path.join(d, "**", "app.json"), recursive=True):
            if ".alpackages" in path.replace("\\", "/").split("/"):
                continue
            try:
                with open(path, encoding="utf-8-sig") as f:
                    j = json.load(f)
            except (OSError, json.JSONDecodeError) as e:
                print(f"WARNING: could not read {path}: {e}", file=sys.stderr)
                continue
            ranges = [(int(r["from"]), int(r["to"])) for r in j.get("idRanges", [])]
            if not ranges and "idRange" in j:
                ranges = [(int(j["idRange"]["from"]), int(j["idRange"]["to"]))]
            apps.append({
                "name": j.get("name", os.path.basename(os.path.dirname(path))),
                "publisher": j.get("publisher", "unknown"),
                "version": j.get("version", ""),
                "ranges": ranges,
                "path": path,
            })
    return apps


def sniff_rows(path):
    """Read the export. Tolerates tab or comma separation and an optional header."""
    with open(path, encoding="utf-8-sig", newline="") as f:
        sample = f.read(8192)
        f.seek(0)
        delim = "\t" if sample.count("\t") >= sample.count(",") else ","
        rows = [r for r in csv.reader(f, delimiter=delim) if r and any(c.strip() for c in r)]
    if rows and re.sub(r"\s+", "", rows[0][0]).lower().startswith("objecttype"):
        rows = rows[1:]
    out = []
    for r in rows:
        r = (r + [""] * 4)[:8]
        otype, oid, oname, sname = r[0].strip(), r[1].strip(), r[2].strip(), r[3].strip()
        alltenants = r[4].strip().upper() if len(r) > 4 else ""
        published = r[5].strip().upper() if len(r) > 5 else ""
        if not otype or not oid.isdigit():
            print(f"WARNING: skipping unparseable row: {r[:4]}", file=sys.stderr)
            continue
        out.append({
            "type": otype, "id": int(oid), "object_name": oname, "service": sname,
            "all_tenants": alltenants, "published": published,
        })
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("export")
    ap.add_argument("--repo", action="append", default=[])
    ap.add_argument("--isv", action="append", default=[])
    ap.add_argument("--json", dest="json_out")
    ap.add_argument("--md", dest="md_out")
    args = ap.parse_args()

    rows = sniff_rows(args.export)
    apps = load_local_apps(args.repo)
    owners = [{"name": a["name"], "publisher": a["publisher"], "ranges": a["ranges"],
               "origin": "local source"} for a in apps]
    for spec in args.isv:
        name, _, ranges = spec.partition(":")
        owners.append({"name": name.strip(), "publisher": name.strip(),
                       "ranges": parse_ranges(ranges), "origin": "declared --isv"})

    def owner_of(oid):
        for o in owners:
            for lo, hi in o["ranges"]:
                if lo <= oid <= hi:
                    return o["name"]
        return None

    for r in rows:
        r["dead"] = (r["object_name"] == "")
        own = owner_of(r["id"])
        if own:
            r["owner"], r["verdict"] = own, "safe"
        elif r["id"] < 50000:
            r["owner"], r["verdict"] = "Microsoft (assumed)", "microsoft"
        else:
            r["owner"], r["verdict"] = "third party (UNCONFIRMED)", "unconfirmed"
        r["feature"] = None
        for label, test in FEATURE_PATTERNS:
            if test(r["service"]):
                r["feature"] = label
                break

    live = [r for r in rows if not r["dead"]]
    dead = [r for r in rows if r["dead"]]
    ms_pages = [r for r in live if r["type"] == "Page" and r["verdict"] == "microsoft"]
    group_a = [r for r in ms_pages if r["feature"]]
    group_b = [r for r in ms_pages if not r["feature"]]
    ms_codeunits = [r for r in live if r["type"] == "Codeunit" and r["verdict"] == "microsoft"]
    ms_queries = [r for r in live if r["type"] == "Query" and r["verdict"] == "microsoft"]
    unconfirmed = [r for r in live if r["verdict"] == "unconfirmed"]

    print("=" * 66)
    print("TOTAL ROWS IN EXPORT :", len(rows))
    for t, n in sorted(Counter(r["type"] for r in rows).items()):
        nd = len([r for r in rows if r["type"] == t and r["dead"]])
        print(f"   {t:10} {n:4}   dead {nd}")
    print("-" * 66)
    print("Microsoft PAGES (live), stop working at v30 :", len(ms_pages))
    print("   Group A, a Microsoft feature creates them :", len(group_a))
    print("   Group B, REVIEW LIST                      :", len(group_b))
    print("Microsoft CODEUNITS (SOAP, stop at v29)      :", len(ms_codeunits))
    print("Microsoft QUERIES (not in the announced scope):", len(ms_queries))
    print("Dead rows (blank Object Name)                :", len(dead))
    print("-" * 66)
    for o in owners:
        n = len([r for r in live if r["owner"] == o["name"]])
        print(f"SAFE  {o['name']:38} {n:4}   ({o['origin']})")
    if unconfirmed:
        print(f"CHECK third party, publisher UNCONFIRMED    : {len(unconfirmed)}")
    print("=" * 66)

    print("\nGroup A families:")
    for label, _ in FEATURE_PATTERNS:
        n = len([r for r in group_a if r["feature"] == label])
        if n:
            print(f"   {label:52} {n:3}  {FEATURE_SOURCE[label]}")

    print("\nWARNINGS")
    print("  * Group B is a REVIEW list, not a work list. A stock BC install also")
    print("    publishes tenant rows. All Tenants=TRUE proves Microsoft created a")
    print("    row; FALSE proves NOTHING. Confirm with a clean-environment export.")
    print("  * The Object Name column shows the object CAPTION, not the object")
    print("    name. Never diff it against AL source. Match on Object ID.")
    print("  * Report every row type. Queries are easy to miss and change totals.")
    if unconfirmed:
        ids = sorted({r["id"] for r in unconfirmed})
        print(f"  * {len(unconfirmed)} rows have an ID >= 50000 with no matching app.json.")
        print(f"    IDs {ids[0]}-{ids[-1]}. Identify the publisher before you call them")
        print("    safe. Add them with --isv once confirmed.")
    hi = [r for r in ms_pages if r["id"] >= 50000]
    if hi:
        print(f"  * {len(hi)} rows assumed Microsoft carry an ID >= 50000. Verify.")
    else:
        idsm = [r["id"] for r in rows if r["verdict"] == "microsoft"]
        if idsm:
            print(f"  * Microsoft IDs here run {min(idsm)}-{max(idsm)}, all below 50000,")
            print("    so the 'below 50000 is Microsoft' rule holds for THIS export only.")

    result = {
        "totals": {
            "rows": len(rows),
            "by_type": dict(Counter(r["type"] for r in rows)),
            "dead": len(dead),
            "microsoft_pages_live": len(ms_pages),
            "group_a": len(group_a), "group_b": len(group_b),
            "microsoft_codeunits": len(ms_codeunits),
            "microsoft_queries": len(ms_queries),
            "unconfirmed": len(unconfirmed),
        },
        "group_a_families": {l: len([r for r in group_a if r["feature"] == l])
                             for l, _ in FEATURE_PATTERNS},
        "group_b": group_b, "group_a": group_a, "dead": dead,
        "microsoft_codeunits": ms_codeunits, "unconfirmed": unconfirmed,
        "safe_by_owner": {o["name"]: [r for r in live if r["owner"] == o["name"]]
                          for o in owners},
        "owners": owners,
    }
    if args.json_out:
        with open(args.json_out, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=1)
        print("\nwrote", args.json_out)

    if args.md_out:
        L = []
        L.append("### Group B — not attributable to a Microsoft feature. Review list.\n")
        L.append(f"{len(group_b)} endpoints.\n")
        L.append("| Service name | Page | Microsoft page name | All Tenants |")
        L.append("| --- | --- | --- | --- |")
        for r in sorted(group_b, key=lambda r: r["id"]):
            L.append(f"| `{r['service']}` | {r['id']} | {r['object_name']} | {r['all_tenants']} |")
        L.append(f"\n### Group A — created by Microsoft features. {len(group_a)} endpoints.\n")
        L.append("| Family | Count | Feature that creates them |")
        L.append("| --- | --- | --- |")
        for label, _ in FEATURE_PATTERNS:
            n = len([r for r in group_a if r["feature"] == label])
            if n:
                L.append(f"| `{label}` | {n} | {FEATURE_SOURCE[label]} |")
        L.append("\n**Group A service names:** " +
                 ", ".join(f"`{r['service']}`" for r in sorted(group_a, key=lambda r: r["service"])))
        if ms_codeunits:
            L.append(f"\n### Microsoft SOAP codeunits — {len(ms_codeunits)}, removed at v29.\n")
            L.append("| Service name | Codeunit | All Tenants |")
            L.append("| --- | --- | --- |")
            for r in sorted(ms_codeunits, key=lambda r: r["id"]):
                L.append(f"| `{r['service']}` | {r['id']} | {r['all_tenants']} |")
        for o in owners:
            safe = sorted([r for r in live if r["owner"] == o["name"]], key=lambda r: r["id"])
            if not safe:
                continue
            L.append(f"\n### Safe — {o['name']} ({len(safe)} endpoints)\n")
            L.append("| Service name | Type | ID | Object name |")
            L.append("| --- | --- | --- | --- |")
            for r in safe:
                L.append(f"| `{r['service']}` | {r['type']} | {r['id']} | {r['object_name']} |")
        if dead:
            L.append(f"\n### Already dead — {len(dead)} endpoints\n")
            fam = Counter(re.sub(r"[A-Z0-9_].*$", "*", r["service"]) if r["service"][:15].lower().startswith("nativeinvoicing")
                          else r["service"] for r in dead)
            L.append(", ".join(f"`{k}` ({v})" if v > 1 else f"`{k}`" for k, v in sorted(fam.items())))
        with open(args.md_out, "w", encoding="utf-8") as f:
            f.write("\n".join(L) + "\n")
        print("wrote", args.md_out)


if __name__ == "__main__":
    main()
