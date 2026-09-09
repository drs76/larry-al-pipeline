"""event_verify — check event subscribers against real symbols BEFORE compiling.

An invented event or a mistyped parameter currently surfaces only as a compile error,
which costs a full referee round: compile, parse errors, re-prompt, rewrite, recompile.
Every one of those facts is knowable from the symbol index the moment the file is
written, so this runs in the write→compile gap and hands the model a symbol-cited
failure instead of a compiler one.

It answers four questions the AL0282 guard in run-build.py does not:

  * does the publisher OBJECT exist?
  * does the EVENT exist on it, and is it actually an event rather than a plain method?
  * do the subscriber's parameter NAMES match the publisher's (subscribers bind by
    name, not position)?
  * is the event OBSOLETE?

False positives are the thing to fear, because a wrong "you invented this" sends a
correct build into a repair loop chasing nothing. Three deliberate silences:

  1. Table auto-events (OnBeforeInsertEvent, OnAfterValidateEvent, ...) are synthesised
     by the compiler and never appear in SymbolReference.json. run-build.py's
     _TABLE_EVENT_PARAMS owns their fixed signatures; here they are valid by
     construction.
  2. Publishers defined by the project's OWN source are not in the downloaded symbols.
     Unknown-to-symbols is reported as unverifiable, never as missing.
  3. No symbol index at all means no findings — not "everything is wrong".

Deterministic, offline, no model. Warnings and errors are separated so a caller can
decide what blocks.
"""
from __future__ import annotations

import glob
import os
import re

import al_symbols

# [EventSubscriber(ObjectType::Codeunit, Codeunit::"Sales-Post", 'OnAfterPostSalesDoc', '', true, true)]
# The object reference is either Type::"Quoted Name", Type::Bare, or a bare id.
_SUB_RE = re.compile(
    r"\[\s*EventSubscriber\s*\(\s*"
    r"ObjectType::(?P<otype>\w+)\s*,\s*"
    r"(?P<oref>(?:\w+\s*::\s*)?(?:\"[^\"]+\"|[\w\.]+))\s*,\s*"
    r"'(?P<event>[^']*)'\s*"
    r"(?:,\s*'(?P<element>[^']*)')?",
    re.IGNORECASE)
_PROC_RE = re.compile(
    r"^\s*(?:local\s+|internal\s+)?procedure\s+(?P<name>\w+|\"[^\"]+\")\s*\((?P<params>.*)$",
    re.IGNORECASE)

# _SUB_RE recognises the CORRECT shape and nothing else, which on its own makes a malformed
# attribute invisible rather than wrong: `if not m: continue` skipped it in silence. Measured
# on doclink Phase 2 — 3/10 runs wrote the event name as a bare identifier,
#     [EventSubscriber(ObjectType::Table, Database::"Document Attachment", OnAfterInsertEvent, , false, false)]
# instead of 'OnAfterInsertEvent', '' — and the verifier said nothing while the compiler
# produced a 90-error parse cascade (14 of 16 AL0114 sat on an attribute line).
#
# The invariant this restores: every syntactic occurrence claiming to be an EventSubscriber
# is either verified or explicitly reported as unverifiable. None may silently disappear.
_ATTR_START_RE = re.compile(r"\[\s*EventSubscriber\s*\(", re.IGNORECASE)


def _blank_noncode(text):
    """Comments and string literals replaced by spaces, every character position preserved.

    Length-preserving on purpose: attribute spans are located in this masked copy and then
    sliced out of the ORIGINAL, so reported line numbers stay true and an event name — which
    is itself a string literal — survives for parsing.
    """
    out = list(text)
    i, n, state = 0, len(text), None
    while i < n:
        c, nxt = text[i], (text[i + 1] if i + 1 < n else "")
        if state is None:
            if c == "/" and nxt in "/*":
                state = "line" if nxt == "/" else "block"
                out[i] = out[i + 1] = " "
                i += 2
                continue
            if c == "'":
                state = "str"
            i += 1
            continue
        if state == "line":
            if c == "\n":
                state = None
            else:
                out[i] = " "
            i += 1
            continue
        if state == "block":
            if c == "*" and nxt == "/":
                state = None
                out[i] = out[i + 1] = " "
                i += 2
                continue
            if c != "\n":
                out[i] = " "
            i += 1
            continue
        # inside a string literal
        if c == "'":
            if nxt == "'":                    # '' is an escaped quote, not a terminator
                out[i] = out[i + 1] = " "
                i += 2
                continue
            state = None
            i += 1
            continue
        out[i] = " "
        i += 1
    return "".join(out)


def _attr_occurrences(text):
    """(line, args, end_line) for every attribute claiming to be an EventSubscriber.

    `args` is None when the argument list is never closed. Located in the masked copy so a
    fake attribute inside a comment or a Caption string is not an occurrence at all.
    """
    mask = _blank_noncode(text)
    for m in _ATTR_START_RE.finditer(mask):
        open_i, depth, j = m.end() - 1, 0, m.end() - 1
        while j < len(mask):
            if mask[j] == "(":
                depth += 1
            elif mask[j] == ")":
                depth -= 1
                if depth == 0:
                    break
            j += 1
        line = text.count("\n", 0, m.start()) + 1
        if j >= len(mask):
            yield line, None, line
            continue
        yield line, text[open_i + 1:j], text.count("\n", 0, j) + 1


def _split_args(args):
    """Top-level comma split — commas inside quotes or nested parens are not separators."""
    parts, buf, depth, instr = [], [], 0, False
    i = 0
    while i < len(args):
        c = args[i]
        if instr:
            buf.append(c)
            if c == "'":
                if i + 1 < len(args) and args[i + 1] == "'":
                    buf.append("'")
                    i += 2
                    continue
                instr = False
            i += 1
            continue
        if c == "'":
            instr = True
        elif c == "(":
            depth += 1
        elif c == ")":
            depth -= 1
        elif c == "," and depth == 0:
            parts.append("".join(buf).strip())
            buf = []
            i += 1
            continue
        buf.append(c)
        i += 1
    parts.append("".join(buf).strip())
    return parts


def _quoted(tok):
    return len(tok) >= 2 and tok[0] == "'" and tok[-1] == "'"


def classify_attribute(args):
    """('ok', None) or (rule, message) for one attribute's argument text.

    Only shapes we are confident about are rejected. Anything else is 'ok' and goes to the
    symbol verifier, which is the conservative direction: a false "you wrote it wrong" sends
    a correct build into a repair loop chasing nothing.
    """
    if args is None:
        return "subscriber-unparseable", "the attribute's argument list is never closed"
    parts = _split_args(args)
    if len(parts) < 3:
        return ("subscriber-unparseable",
                f"expected at least ObjectType, object and event name; found {len(parts)} "
                f"argument(s): ({args.strip()})")
    if not re.match(r"(?i)^ObjectType\s*::\s*\w+$", parts[0]):
        return ("subscriber-unparseable",
                f'first argument must be ObjectType::<kind>, found "{parts[0]}"')
    ev = parts[2]
    if not _quoted(ev):
        bare = ev.strip("'") or "OnAfterInsertEvent"
        return ("subscriber-event-unquoted",
                f"the event name must be a STRING LITERAL in single quotes: write "
                f"'{bare}' instead of {ev or '<empty>'}. A bare identifier does not parse, "
                f"and the failure cascades into AL0114/AL0104 across the whole object")
    if len(parts) > 3 and not _quoted(parts[3]):
        return ("subscriber-element-unquoted",
                f"the element name must be a string literal — write '' for a table or "
                f"codeunit event, not {parts[3] or '<empty>'}")
    return "ok", None

# Compiler-synthesised per table — absent from symbols, and correct to subscribe to.
_TABLE_AUTO = re.compile(
    r"^On(Before|After)(Insert|Modify|Delete|Rename|Validate)Event$", re.IGNORECASE)


def _obj_name(oref):
    """'Codeunit::"Sales-Post"' -> 'Sales-Post'."""
    tail = oref.split("::")[-1].strip()
    return tail.strip('"').strip()


def _split_params(text):
    """Parameter NAMES from a procedure declaration, which may wrap over lines.

    Only names matter: subscribers bind by name, and a type mismatch is the compiler's
    business, not this module's.
    """
    depth, buf = 0, []
    for ch in text:
        if ch == "(":
            depth += 1
        elif ch == ")":
            if depth == 0:
                break
            depth -= 1
        buf.append(ch)
    names = []
    for part in "".join(buf).split(";"):
        part = part.strip()
        if not part:
            continue
        head = part.split(":", 1)[0].strip()
        head = re.sub(r"^var\s+", "", head, flags=re.IGNORECASE).strip()
        if head:
            names.append(head.strip('"'))
    return names


def scan_subscribers(path):
    """(well_formed, problems) for one file — every occurrence accounted for.

    Nothing that looks like an EventSubscriber leaves this function unclassified: it is
    either parsed for symbol verification or returned as a problem with a reason.
    """
    try:
        text = open(path, encoding="utf-8-sig", errors="replace").read()
    except OSError:
        return [], []
    lines = text.splitlines()
    out, problems = [], []
    for line, args, end_line in _attr_occurrences(text):
        rule, msg = classify_attribute(args)
        if rule != "ok":
            problems.append({"file": path, "line": line, "rule": rule, "message": msg})
            continue
        attr = f"[EventSubscriber({args})]"
        m = _SUB_RE.search(attr)
        if not m:
            # Argument shapes we did not confidently reject, and cannot verify either.
            problems.append({"file": path, "line": line, "rule": "subscriber-unparseable",
                             "message": f"cannot read the publisher or event out of "
                                        f"({args.strip()})"})
            continue
        i = end_line - 1
        # The declaration may sit a few lines below the attribute, and its parameter list
        # may span lines — join a window rather than assuming a one-line procedure.
        window = "\n".join(lines[i + 1:i + 12])
        pm = _PROC_RE.search(window, re.MULTILINE) or re.search(
            _PROC_RE.pattern, window, re.IGNORECASE | re.MULTILINE)
        params, proc = [], ""
        if pm:
            proc = pm.group("name").strip('"')
            rest = window[pm.start("params"):]
            params = _split_params(rest)
        out.append({"file": path, "line": line,
                    "object_type": m.group("otype").lower(),
                    "object": _obj_name(m.group("oref")),
                    "event": m.group("event"), "element": m.group("element") or "",
                    "proc": proc, "params": params})
    return out, problems


def parse_subscribers(path):
    """[{file, line, object_type, object, event, element, proc, params}] for one file."""
    return scan_subscribers(path)[0]


def _sig_params(signature):
    """Parameter names out of an indexed signature string."""
    inner = signature[signature.find("(") + 1:signature.rfind(")")]
    return [p.split(":", 1)[0].strip() for p in inner.split(",") if p.strip()]


def verify(src_root, idx, local_objects=()):
    """[{severity, rule, file, line, message, evidence}] — most severe first.

    local_objects: names defined by the project itself; a publisher among them cannot be
    checked against downloaded symbols and must not be called missing.
    """
    # No early return on a missing index any more: whether an attribute PARSES is knowable
    # offline and makes no symbol claim, so it is reported either way. Only the
    # symbol-dependent checks below are skipped, keeping docstring silence #3 intact.
    local = {str(o).strip().strip('"').lower() for o in local_objects}
    findings = []
    for path in sorted(glob.glob(os.path.join(src_root, "**", "*.al"), recursive=True)):
        subs, problems = scan_subscribers(path)
        # Malformed attributes first: they break parsing of the whole object, so every other
        # diagnostic in that file is downstream noise until they are fixed.
        for p in problems:
            findings.append({"severity": "error", "rule": p["rule"],
                             "file": os.path.relpath(path, src_root), "line": p["line"],
                             "message": p["message"], "evidence": ""})
        if not idx:
            continue
        for s in subs:
            where = {"file": os.path.relpath(path, src_root), "line": s["line"]}
            ev, obj = s["event"], s["object"]

            if s["object_type"] == "table" and _TABLE_AUTO.match(ev or ""):
                continue                      # synthesised; see module docstring

            if obj.lower() in local:
                continue                      # the project's own publisher

            # Object references come as a quoted name OR a number (Database::1173).
            rec = (al_symbols.lookup_id(idx, s["object_type"], obj) if obj.isdigit()
                   else al_symbols.lookup(idx, obj))
            if not rec:
                findings.append(dict(where, severity="error", rule="publisher-missing",
                                     message=f'publisher {s["object_type"]} "{obj}" is not '
                                             f"in the downloaded symbols",
                                     evidence=""))
                continue

            hits = [h for h in al_symbols.find_member(idx, ev) if h["object"] == rec["name"]]
            if not hits:
                elsewhere = al_symbols.find_event(idx, ev)
                if elsewhere:
                    findings.append(dict(
                        where, severity="error", rule="wrong-publisher",
                        message=f'"{obj}" does not publish {ev} — it is published by '
                                + ", ".join(f'{h["kind"]} "{h["object"]}"'
                                            for h in elsewhere[:3]),
                        evidence=al_symbols.evidence(elsewhere[0])))
                else:
                    findings.append(dict(
                        where, severity="error", rule="event-missing",
                        message=f'{ev} does not exist on "{obj}" (nor anywhere else in '
                                f"the symbols)",
                        evidence=al_symbols.evidence(rec)))
                continue

            h = hits[0]
            if not h["is_event"]:
                findings.append(dict(
                    where, severity="error", rule="not-an-event",
                    message=f'{ev} on "{obj}" is a plain method, not an '
                            f"[IntegrationEvent]/[BusinessEvent] — it cannot be subscribed to",
                    evidence=al_symbols.evidence(h)))
                continue

            if h.get("obsolete"):
                findings.append(dict(
                    where, severity="warning", rule="event-obsolete",
                    message=f'{ev} on "{obj}" is obsolete: {h["obsolete"]}',
                    evidence=al_symbols.evidence(h)))

            want = _sig_params(h["signature"])
            got = s["params"]
            if got:
                # A subscriber may take a PREFIX of the published parameters, but the
                # names it does take must match, in order. This is the AL0282 class of
                # failure, caught before the compiler gets a chance to say it.
                bad = [(g, w) for g, w in zip(got, want) if g.lower() != w.lower()]
                if len(got) > len(want):
                    findings.append(dict(
                        where, severity="error", rule="too-many-params",
                        message=f'{s["proc"]} takes {len(got)} parameters but {ev} '
                                f"publishes {len(want)}: ({', '.join(want)})",
                        evidence=al_symbols.evidence(h)))
                elif bad:
                    findings.append(dict(
                        where, severity="error", rule="param-name-mismatch",
                        message=f'{s["proc"]}: event subscribers bind by NAME — '
                                + "; ".join(f'"{g}" must be "{w}"' for g, w in bad)
                                + f"  (published: {ev}({', '.join(want)}))",
                        evidence=al_symbols.evidence(h)))
    order = {"error": 0, "warning": 1}
    return sorted(findings, key=lambda f: (order.get(f["severity"], 2), f["file"], f["line"]))


def format_findings(findings):
    """Text for a fix prompt. Symbol evidence is included deliberately: a claim the
    model can check is one it is far more likely to act on correctly."""
    if not findings:
        return ""
    # The header must not claim symbol backing for a finding that had none: the syntactic
    # classification runs offline, and a model told "the symbols say X" about a pure parse
    # error learns the wrong lesson about what the evidence is.
    syntactic = {"subscriber-event-unquoted", "subscriber-element-unquoted",
                 "subscriber-unparseable"}
    kinds = {f["rule"] for f in findings}
    how = ("before compiling" if kinds <= syntactic
           else "checked against the downloaded symbols, before compiling")
    out = [f"EVENT VERIFICATION ({how}):"]
    for f in findings:
        out.append(f'  [{f["severity"].upper()}] {f["file"]}:{f["line"]} — {f["message"]}')
        if f.get("evidence"):
            out.append(f'      symbol source: {f["evidence"]}')
    return "\n".join(out)


def main():
    import argparse
    ap = argparse.ArgumentParser(prog="event_verify")
    ap.add_argument("root", nargs="?", default=".")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    root = os.path.abspath(a.root)
    pkgs = os.path.join(root, ".alpackages")
    idx = al_symbols.build_index(pkgs) if os.path.isdir(pkgs) else {}
    if not idx:
        print(f"no symbols under {pkgs} — nothing to verify against")
        return 0
    src = os.path.join(root, "src") if os.path.isdir(os.path.join(root, "src")) else root
    fs = verify(src, idx)
    if a.json:
        import json
        print(json.dumps(fs, indent=2))
    else:
        print(format_findings(fs) or "no event problems found")
    return 1 if any(f["severity"] == "error" for f in fs) else 0


if __name__ == "__main__":
    raise SystemExit(main())
