#!/usr/bin/env python3
"""
bc_collect — deterministic collector for BC Extension Analysis (no LLM).

The analysis prompt (tooling/bc-analysis.prompt.md) is a multi-pass read: glob → grep →
read → reason. Local models fail the *tool loop* (they emit tool calls as code blocks and
produce shallow output). But the greps are FIXED — so we run them here in Python and hand
the model a ready-made facts pack to reason over. Zero model calls.

Produces:
  * a facts pack (markdown): app.json summary, object inventory (IDs from real declarations),
    every grep-table hit with file:line, UCI red-flags classified live vs commented.
  * a curated source bundle for the analyst: codeunits in full (Pass 2, ~80% of logic);
    tables/tableexts included; pages/reports/xmlports summarised (name only) unless small.

Grep patterns are the plain-alternation form of the prompt's "Grep Before Reading" + per-check
tables (kept in sync with that doc). Env: nothing required — takes a source dir argument.

CLI: bc_collect.py <source-dir>              # print the facts pack
     bc_collect.py <source-dir> --source     # print the analyst source bundle
"""
import glob
import json
import os
import re
import sys

# Object declaration: `codeunit 50100 "Name"`, `pageextension 50101 "N" extends "Base"`, …
_OBJ_RE = re.compile(
    r'^\s*(codeunit|table|tableextension|page|pageextension|report|reportextension|'
    r'xmlport|query|enum|enumextension|interface|permissionset|permissionsetextension|'
    r'controladdin|profile|dotnet)\s+(\d+)\s+("(?:[^"]+)"|[A-Za-z0-9_]+)'
    r'(?:\s+extends\s+("[^"]+"|[A-Za-z0-9_]+))?',
    re.IGNORECASE | re.MULTILINE)

# Grep-table patterns — plain `|` alternation (the doc escapes them for markdown; here they're real).
GREPS = {
    "http_crm": (r'HttpClient|RegisterConnection|CRMInvoice\.Get|Dataverse',
                 "HTTP / CRM / Dataverse calls"),
    "event_subscribers": (r'\[EventSubscriber', "Event subscribers"),
    "findset_loops": (r'\bFindSet\b', "FindSet loops (N+1 / missing-commit candidates)"),
    "autocalc": (r'\bSetAutoCalcFields\b', "SetAutoCalcFields (FlowField cost in loops)"),
    "tryfunctions": (r'\[TryFunction', "TryFunctions"),
    "setcurrentkey": (r'\bSetCurrentKey\b', "SetCurrentKey (verify key matches filters)"),
    "job_queue": (r'trigger OnRun', "Job-queue / OnRun codeunits"),
    "tableext_fields": (r'field\(\d+;', "Custom fields on TableExts"),
    "commit": (r'\bCommit\(\)', "Commit() calls"),
    "get_in_code": (r'\.Get\(|\bFindFirst\b', "Get/FindFirst (inspect if inside a loop → N+1)"),
}

# UCI (Universal Code Initiative) OnPrem-only red flags — the doc's last grep row.
UCI_RE = re.compile(
    r'\bDotNet\b|SqlConnection|System\.Net|System\.Data|ServerFilePath|ServerTempFileName|'
    r'IsLocalFileSystemAccessible|GetServerDirectory|GetDirectoryFiles|'
    r'FileManagement\.(?:CopyClientFile|ClientFileExists)|FILE\.(?:EXISTS|ERASE|COPY|RENAME)')

# Full-text object types worth handing the analyst (Pass 2/3); others are summarised by name.
FULL_TEXT_TYPES = {"codeunit", "table", "tableextension", "enum", "enumextension", "interface"}


def _obj_of(text):
    """(type, id, name, extends) from the first object declaration, or (None,…)."""
    m = _OBJ_RE.search(text)
    if not m:
        return None, None, None, None
    typ, oid, name, ext = m.group(1).lower(), m.group(2), m.group(3), m.group(4)
    return typ, oid, name.strip('"'), (ext.strip('"') if ext else None)


def _is_commented(line):
    """Cheap live-vs-commented check for a single line (// … or a line inside an obvious comment)."""
    s = line.strip()
    return s.startswith("//") or s.startswith("*") or s.startswith("///")


def load_app(source_dir):
    """Parse app.json — publisher/name/version/target/id-range/dependencies."""
    for p in glob.glob(source_dir + "/**/app.json", recursive=True):
        try:
            j = json.load(open(p, encoding="utf-8"))
        except Exception:
            continue
        idr = j.get("idRanges") or ([{"from": j.get("idRange", {}).get("from"),
                                      "to": j.get("idRange", {}).get("to")}]
                                     if j.get("idRange") else [])
        return {
            "path": p, "name": j.get("name"), "publisher": j.get("publisher"),
            "version": j.get("version"), "target": j.get("target"),
            "runtime": j.get("runtime"),
            "idRanges": [f'{r.get("from")}..{r.get("to")}' for r in idr if r.get("from")],
            "dependencies": [d.get("name") for d in (j.get("dependencies") or [])],
        }
    return {}


def scan(source_dir):
    """Read every .al once; return per-file records + object metadata."""
    files = []
    for f in sorted(glob.glob(source_dir + "/**/*.al", recursive=True)):
        try:
            text = open(f, encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        typ, oid, name, ext = _obj_of(text)
        files.append({"path": f, "rel": os.path.relpath(f, source_dir), "text": text,
                      "type": typ or "unknown", "id": oid, "name": name, "extends": ext})
    return files


def grep(files, pattern):
    """[(rel, lineno, line, commented)] for a pattern across all files."""
    rx = re.compile(pattern)
    hits = []
    for fr in files:
        for i, line in enumerate(fr["text"].splitlines(), 1):
            if rx.search(line):
                hits.append((fr["rel"], i, line.strip(), _is_commented(line)))
    return hits


def collect(source_dir, source_char_cap=None):
    """Full deterministic pass. Returns a dict incl. `facts_md` and source bundles.

    source_char_cap: if set, the source bundle drops whole low-priority files to fit (see
    _render_source) instead of the caller cutting mid-file."""
    app = load_app(source_dir)
    files = scan(source_dir)

    # Inventory grouped by object type
    by_type = {}
    for fr in files:
        by_type.setdefault(fr["type"], []).append(fr)

    greps = {k: grep(files, pat) for k, (pat, _label) in GREPS.items()}

    # UCI: classify each red-flag hit live vs commented (skip the Cloud-safe `using System.IO;`)
    uci = []
    for fr in files:
        for i, line in enumerate(fr["text"].splitlines(), 1):
            if UCI_RE.search(line):
                if re.match(r'\s*using\s+System\.IO\s*;', line):
                    continue
                uci.append((fr["rel"], i, line.strip(), _is_commented(line)))

    # AL-9: the greps above tell the analyst WHERE to look ("inspect if inside a loop →
    # N+1"). al_semantics has already made that judgement deterministically, so hand over
    # the confirmed findings instead of asking a model to re-derive them from raw hits.
    # Same rules the build referee and `alw` use — one rule set, three consumers.
    try:
        import al_semantics
        semantics = al_semantics.analyse(source_dir)
    except Exception as e:
        semantics = []
        print(f"  (al_semantics unavailable: {e})")

    facts_md = _render_facts(source_dir, app, by_type, greps, uci, semantics)
    return {
        "source_dir": source_dir, "app": app, "files": files, "by_type": by_type,
        "greps": greps, "uci": uci, "facts_md": facts_md, "semantics": semantics,
        "source_bundle": _render_source(files, char_cap=source_char_cap),
    }


def _render_facts(source_dir, app, by_type, greps, uci, semantics=()):
    L = [f"# BC Analysis — Facts Pack\n\nSource: `{source_dir}`\n"]
    L.append("## app.json")
    if app:
        L.append(f"- **Name**: {app.get('name')}  |  **Publisher**: {app.get('publisher')}")
        L.append(f"- **Version**: {app.get('version')}  |  **Target**: "
                 f"**{app.get('target') or '(absent → treat as OnPrem for UCI)'}**  |  "
                 f"**Runtime**: {app.get('runtime')}")
        L.append(f"- **ID ranges**: {', '.join(app.get('idRanges') or []) or '(none)'}")
        L.append(f"- **Dependencies**: {', '.join(app.get('dependencies') or []) or '(none)'}")
    else:
        L.append("- (app.json not found)")

    L.append("\n## Object Inventory (IDs from declarations)")
    L.append("| Type | ID | Name | Extends | File |")
    L.append("|---|---|---|---|---|")
    for typ in sorted(by_type):
        for fr in sorted(by_type[typ], key=lambda r: (r["id"] or "", r["rel"])):
            L.append(f"| {typ} | {fr['id'] or ''} | {fr['name'] or ''} | "
                     f"{fr['extends'] or ''} | {fr['rel']} |")

    L.append("\n## Grep hits")
    for key, (_pat, label) in GREPS.items():
        hits = greps[key]
        L.append(f"\n### {label}  ({len(hits)})")
        if not hits:
            L.append("_none_")
            continue
        for rel, ln, line, commented in hits[:200]:
            tag = "  _(commented)_" if commented else ""
            L.append(f"- `{rel}:{ln}` — `{line}`{tag}")

    L.append("\n## Deterministic performance findings (al_semantics)")
    L.append("These are CONFIRMED by rule, not candidates to assess: each one was matched "
             "against the loop/trigger/procedure structure of the source. Cite them "
             "directly. They are warnings, not proof of a defect — a Commit in a loop is "
             "correct in a deliberate batch job — so say what each one costs here.")
    if not semantics:
        L.append("\n_none_")
    else:
        by_rule = {}
        for f in semantics:
            by_rule.setdefault(f["rule"], []).append(f)
        for rule in sorted(by_rule):
            hits = by_rule[rule]
            L.append(f"\n### {rule}  ({len(hits)})")
            L.append(f"_{hits[0]['reason']}_")
            for f in hits[:40]:
                L.append(f"- `{f['file']}:{f['line']}` — `{f['evidence']}`")
            if len(hits) > 40:
                L.append(f"- _… and {len(hits) - 40} more_")

    L.append("\n## UCI red-flags (OnPrem-only constructs)")
    live = [h for h in uci if not h[3]]
    L.append(f"Live: **{len(live)}**  |  Commented: {len(uci) - len(live)}  "
             f"(target = {app.get('target') or 'absent'})")
    for rel, ln, line, commented in uci[:200]:
        tag = "  _(commented — hygiene note, not a live violation)_" if commented else "  **LIVE**"
        L.append(f"- `{rel}:{ln}` — `{line}`{tag}")
    return "\n".join(L)


def _render_source(files, char_cap=None):
    """Analyst source bundle: full text for logic-bearing types, name-only for the rest.

    If char_cap is set, drop WHOLE trailing full-text files once the budget is hit — never
    cut mid-file, since a truncated procedure makes a model try to *complete the code* instead
    of analysing it. Codeunits come first (Pass-2 priority) so the highest-value logic survives.
    """
    order = {"codeunit": 0, "table": 1, "tableextension": 2, "enum": 3,
             "enumextension": 4, "interface": 5}
    ordered = sorted(files, key=lambda fr: order.get(fr["type"], 9))
    parts, used, dropped = [], 0, 0
    for fr in ordered:
        if fr["type"] in FULL_TEXT_TYPES:
            block = (f"\n===== {fr['rel']}  ({fr['type']} {fr['id']} {fr['name']}) =====\n"
                     + fr["text"])
            if char_cap is not None and used + len(block) > char_cap and used > 0:
                dropped += 1
                continue          # skip this whole file, try the next (smaller) one
            parts.append(block)
            used += len(block)
        else:
            parts.append(f"\n----- {fr['rel']}  ({fr['type']} {fr['id']} {fr['name']}) "
                         f"[summarised: name only] -----")
    if dropped:
        parts.append(f"\n[... {dropped} lower-priority source file(s) omitted to fit context; "
                     "the Object Inventory in the FACTS PACK still lists them ...]")
    return "\n".join(parts)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("usage: bc_collect.py <source-dir> [--source]")
    src = sys.argv[1].rstrip("/")
    data = collect(src)
    if "--source" in sys.argv[2:]:
        print(data["source_bundle"])
    else:
        print(data["facts_md"])
