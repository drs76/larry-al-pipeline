"""al_semantics — legal AL that is nonetheless a bad idea.

The compiler and the cops police what is *valid*. Nothing in the pipeline looks at code
that compiles cleanly and will still be slow, unsafe under concurrency, or wrong the
first time two users touch it at once. That gap is where the expensive BC defects live:
a `Get` inside a loop is a clean build and a table scan; a `Commit` inside a loop is a
clean build and a half-posted document.

This is NOT a model reviewer and NOT a parser. It is a set of deterministic textual
rules over structure the AL layout makes reliable — `repeat…until` bodies, trigger
bodies, procedure bodies. That limitation is deliberate: a rule that cannot be stated
precisely enough to run without a parser is a rule that will produce false positives,
and every finding here is read by a model that will happily "fix" imaginary problems.

**Everything is a warning.** The review was explicit that false positives must not fail
the compiler, and these rules have real exceptions — a `Commit` in a loop is correct in a
deliberate batch-posting job. Findings inform; the compiler decides.

Each finding carries `suggested_next_check` rather than a fix. Telling a model what to
verify keeps the judgement where the context is, instead of asserting a fix that may be
wrong for this code.

Two rules were written and then REMOVED, because the reasoning is worth keeping:
`setcurrentkey-unused` (SetCurrentKey with no traversal after it) produced 2020 findings
against Microsoft's own base application, and the ones read by hand were all wrong — the
record was a global whose key is consumed by a `Copy()` in a different procedure, which
no single-file textual rule can see. Per the paragraph above, a rule that needs a parser
to be right is a rule that will be wrong; it was deleted rather than tuned.

`filter-mutated-during-loop` (changing a cursor's filters mid-traversal) went the same
way: 793 findings against the base application, and the ones read by hand were the
deliberate grouped-traversal idiom — filter, iterate the group, clear the filter, continue
the outer loop. The dangerous version and the idiomatic version are the same text.

Consumed by the reviewer prompt and by `bcw` (AL-9 reuses these rules rather than
restating them). Deterministic, offline, no model.
"""
from __future__ import annotations

import glob
import os
import re

# Spans that must never be scanned: string literals ('' escapes a quote), quoted
# identifiers, and comment tails. Matching "Commit" inside a caption is noise.
_MASK = re.compile(r"'(?:[^']|'')*'|\"[^\"]*\"|//.*$")
_BLOCK_COMMENT = re.compile(r"/\*.*?\*/", re.DOTALL)


def _strip(line):
    """Blank out literals/comments, preserving column positions."""
    return _MASK.sub(lambda m: " " * len(m.group(0)), line)


def _lines(path):
    """(masked, raw). Masked hides string literals and quoted identifiers so `Commit` in a
    caption is not a Commit. But a quoted identifier IS a field name, and the key/filter
    rules are entirely about which fields — so those read the raw line instead."""
    try:
        raw = open(path, encoding="utf-8-sig", errors="replace").read()
    except OSError:
        return [], []
    raw = _BLOCK_COMMENT.sub(lambda m: "\n" * m.group(0).count("\n"), raw)
    src = raw.splitlines()
    return [_strip(ln) for ln in src], src


# AL declares `Name: Type;` in a var block. Knowing the TYPE is what separates
# `Cust.Get(...)` (a database round trip) from `Client.Get(...)` (an HTTP call) — they are
# the same text and opposite findings.
_DECL_RE = re.compile(r"^\s*(?:var\s+)?(\w+)\s*:\s*([A-Za-z]\w*)", re.IGNORECASE)
_AMBIGUOUS = object()


def _declared_types(lines):
    """{var: type}. A name declared with two different types resolves to unknown rather
    than to a guess."""
    out = {}
    for ln in lines:
        m = _DECL_RE.match(ln)
        if not m:
            continue
        var, typ = m.group(1), m.group(2).lower()
        if var.lower() in ("procedure", "trigger", "begin", "end", "var"):
            continue
        prev = out.get(var)
        out[var] = typ if prev in (None, typ) else _AMBIGUOUS
    return {k: v for k, v in out.items() if v is not _AMBIGUOUS}


def _repeat_blocks(lines):
    """[(start, end)] line indices of every repeat…until body, nesting-aware."""
    out, stack = [], []
    for i, ln in enumerate(lines):
        low = ln.lower()
        for _ in re.findall(r"\brepeat\b", low):
            stack.append(i)
        for _ in re.findall(r"\buntil\b", low):
            if stack:
                out.append((stack.pop(), i))
    return out


def _loop_var(lines, end):
    """The record being iterated, from `until X.Next() = 0`. Several rules only make
    sense against the cursor itself — mutating some OTHER record inside the loop is
    ordinary code."""
    m = re.search(r"\buntil\s+(\w+)\s*\.\s*Next\s*\(", lines[end], re.IGNORECASE)
    return m.group(1) if m else ""


def _args(call_text):
    """Field names from a SetCurrentKey/SetRange argument list, quoted or bare."""
    inner = call_text[call_text.find("(") + 1:]
    depth, buf = 0, []
    for ch in inner:
        if ch == "(":
            depth += 1
        elif ch == ")":
            if depth == 0:
                break
            depth -= 1
        buf.append(ch)
    out = []
    for part in "".join(buf).split(","):
        part = part.strip()
        # `Rec."Applies-to ID"` and `"Applies-to ID"` are the same field. Left unstripped,
        # a key field written with its record prefix never matches the filter that uses
        # it — which is a finding invented by the parser, not by the code.
        q = re.match(r'^\w+\.\s*("[^"]+"|\w+)$', part)
        if q:
            part = q.group(1)
        part = part.strip().strip('"').strip()
        if part:
            out.append(part.lower())
    return out


def _enclosing_trigger(lines, i):
    """Name of the trigger/procedure containing line i, searching upwards."""
    for j in range(i, -1, -1):
        m = re.match(r"\s*(?:local\s+|internal\s+)?(trigger|procedure)\s+(\w+|\"[^\"]+\")",
                     lines[j], re.IGNORECASE)
        if m:
            return m.group(2).strip('"')
    return ""


def _in_subscriber(lines, i):
    """Is line i inside a procedure carrying [EventSubscriber]?"""
    for j in range(i, max(-1, i - 400), -1):
        if re.match(r"\s*(?:local\s+|internal\s+)?procedure\b", lines[j], re.IGNORECASE):
            for k in range(j - 1, max(-1, j - 6), -1):
                if "eventsubscriber" in lines[k].lower():
                    return True
            return False
    return False


def _proc_start(lines, i):
    """Line index where the procedure/trigger containing line i begins.

    A backward scan that runs past this boundary compares code from one procedure with
    code from another. That is how a LockTable on the first line of a procedure got
    blamed for a read in the procedure above it.
    """
    for j in range(i, -1, -1):
        if re.match(r"\s*(?:local\s+|internal\s+)?(?:trigger|procedure)\s", lines[j],
                    re.IGNORECASE):
            return j
    return 0


def _proc_end(lines, i):
    """Line index where the procedure containing line i ends (exclusive).

    A fixed-size forward window runs into the NEXT procedure — which is how a missing
    HttpClient timeout got excused by a different procedure that sets one.
    """
    for j in range(i + 1, len(lines)):
        if re.match(r"\s*(?:local\s+|internal\s+)?(?:trigger|procedure)\s", lines[j],
                    re.IGNORECASE):
            return j
    return len(lines)


def _is_parameter(lines, i, var):
    """Is `var` a parameter of the procedure containing line i?

    Whatever a procedure receives was set up by its caller, one file away. Demanding a
    local Open on it turns the standard RecordRef idiom into a finding.
    """
    for j in range(i, -1, -1):
        m = re.match(r"\s*(?:local\s+|internal\s+)?procedure\s+\w+\s*\((?P<p>.*)",
                     lines[j], re.IGNORECASE)
        if m:
            decl = "\n".join(lines[j:j + 6])
            return re.search(rf"[(;]\s*(?:var\s+)?{re.escape(var)}\s*:", decl,
                             re.IGNORECASE) is not None
    return False


def _f(rule, path, root, i, severity, reason, evidence, nxt):
    return {"rule": rule, "file": os.path.relpath(path, root), "line": i + 1,
            "severity": severity, "reason": reason,
            "evidence": evidence.strip()[:160], "suggested_next_check": nxt}


# Data-access calls that hit the database once per iteration when placed in a loop.
_PER_ROW_DB = re.compile(
    r"\b(?P<var>\w+)\s*\.\s*(?P<call>Get|FindFirst|FindLast|CalcSums|Count)"
    r"\s*\(")
# `TempSalesLine` is a temporary record: it lives in memory, so a Get per iteration is a
# hash lookup, not a database round trip. The Temp prefix is a near-universal BC
# convention and the alternative — resolving `temporary` on the var declaration — needs a
# parser. Matching the RECEIVER matters: 20% of the first run's findings were lines where
# only the ARGUMENT was a temp record.
_TEMP_VAR = re.compile(r"^Temp[A-Z_]|^Temp$")
_HTTP = re.compile(r"\b(HttpClient|HttpRequestMessage|HttpResponseMessage)\b", re.IGNORECASE)
_WRITE_TRIGGERS = ("OnInsert", "OnModify", "OnDelete", "OnRename", "OnValidate",
                   "OnBeforeInsert", "OnAfterInsert", "OnBeforeModify", "OnAfterModify")


def analyse_file(path, root):
    lines, raw_lines = _lines(path)
    if not lines:
        return []
    types = _declared_types(lines)
    out = []
    blocks = _repeat_blocks(lines)
    in_loop = set()
    for a, b in blocks:
        in_loop.update(range(a, b + 1))

    for i, ln in enumerate(lines):
        low = ln.lower()

        # ── DB access per row ──────────────────────────────────────────────────
        if i in in_loop:
            m = _PER_ROW_DB.search(ln)
            if m and not _TEMP_VAR.match(m.group("var")) \
                    and types.get(m.group("var"), "record") == "record":
                out.append(_f("db-call-in-loop", path, root, i, "warning",
                              f"{m.group('call')} runs once per iteration — this is a database "
                              f"round trip per row, the most common cause of a BC report "
                              f"or posting routine that is fine on test data and unusable "
                              f"on real volumes",
                              ln,
                              "can this be a SetRange/SetFilter before the loop, a "
                              "temporary table, or SetAutoCalcFields for the flowfields?"))

            if re.search(r"\bCommit\s*\(\s*\)", ln, re.IGNORECASE):
                out.append(_f("commit-in-loop", path, root, i, "warning",
                              "Commit inside a loop ends the transaction mid-iteration: a "
                              "failure on a later row leaves the earlier rows written and "
                              "the operation half-applied, and it defeats the write lock",
                              ln,
                              "is this a deliberate batch job with a resume point, or "
                              "should the Commit move outside the loop?"))

        # ── transactions ───────────────────────────────────────────────────────
        if re.search(r"\bCommit\s*\(\s*\)", ln, re.IGNORECASE):
            trig = _enclosing_trigger(lines, i)
            if trig.lower().startswith("try") or "[trycommit" in low:
                out.append(_f("commit-in-try", path, root, i, "warning",
                              f"Commit inside TryFunction {trig} — the try boundary can no "
                              f"longer roll the work back, so a later error leaves "
                              f"committed changes behind",
                              ln, "move the Commit outside the TryFunction"))
            if _in_subscriber(lines, i):
                out.append(_f("commit-in-subscriber", path, root, i, "warning",
                              "Commit inside an event subscriber commits the PUBLISHER's "
                              "transaction, not just this code — the subscriber cannot know "
                              "what else is in flight",
                              ln, "does the publishing process expect to still be able to "
                                  "roll back at this point?"))

        _lt = re.search(r"\b(\w+)\s*\.\s*LockTable\s*\(", ln, re.IGNORECASE)
        if _lt:
            # The read has to be on the SAME variable. Locking VATEntry after reading
            # GLEntry is ordinary correct code, and treating it as a finding produced
            # 1293 accusations against Microsoft's own base app.
            _lv = re.escape(_lt.group(1))
            _read = rf"\b{_lv}\s*\.\s*(Get|Find(Set|First|Last)?)\s*\("
            # Lock-then-read is the CORRECT pattern. The hazard is read, then lock, then
            # act on the values already in hand — so a re-read after the lock clears it.
            _rereads = any(re.search(_read, lines[j], re.IGNORECASE)
                           for j in range(i + 1, min(len(lines), i + 15)))
            for j in range(max(_proc_start(lines, i), i - 25), i):
                if not _rereads and re.search(_read, lines[j], re.IGNORECASE):
                    out.append(_f("locktable-after-read", path, root, i, "warning",
                                  "LockTable after the record was already read — the values "
                                  "in hand predate the lock, so another session may have "
                                  "changed them in between",
                                  ln, "call LockTable before the first read of this record"))
                    break

        # ── integration ────────────────────────────────────────────────────────
        if _HTTP.search(ln):
            trig = _enclosing_trigger(lines, i)
            if any(trig.lower().startswith(t.lower()) for t in _WRITE_TRIGGERS):
                out.append(_f("http-in-write-trigger", path, root, i, "warning",
                              f"outbound HTTP inside {trig}: the call runs while the write "
                              f"transaction is open, so a slow or unreachable endpoint holds "
                              f"database locks for its whole timeout",
                              ln, "can this move to a job queue entry or an explicit "
                                  "user action outside the write?"))
            elif _in_subscriber(lines, i):
                out.append(_f("http-in-subscriber", path, root, i, "warning",
                              "outbound HTTP inside an event subscriber runs inside the "
                              "publisher's transaction and makes an unrelated process wait "
                              "on a remote endpoint",
                              ln, "should this be queued rather than called inline?"))

        # ── safety ─────────────────────────────────────────────────────────────
        if re.search(r"\bIsolatedStorage\s*\.\s*Set\s*\(", ln, re.IGNORECASE):
            if not re.search(r"DataScope\s*::", ln, re.IGNORECASE):
                out.append(_f("isolatedstorage-no-scope", path, root, i, "warning",
                              "IsolatedStorage.Set without an explicit DataScope defaults to "
                              "Module scope — for a secret this is usually not what was "
                              "intended, and the default is easy to miss in review",
                              ln, "should this be DataScope::Company or ::CompanyAndUser?"))

        m = re.search(r"\b(\w+)\s*\.\s*(SetTable|Field)\s*\(", ln)
        if m and re.search(r"\bFieldRef\b|\bRecordRef\b", "\n".join(lines[:i]), re.IGNORECASE):
            var = m.group(1)
            opened = any(re.search(rf"\b{re.escape(var)}\s*\.\s*(Open|GetTable)\s*\(",
                                   lines[j], re.IGNORECASE)
                         for j in range(max(_proc_start(lines, i), i - 60), i))
            # A RecordRef received as a parameter was opened by the caller — that is the
            # normal way RecordRef code is written, and it is invisible from this file.
            if not opened and _is_parameter(lines, i, var):
                opened = True
            if not opened and m.group(2) == "Field":
                out.append(_f("fieldref-without-open", path, root, i, "warning",
                              f"{var}.Field(...) with no visible Open/GetTable on {var} "
                              f"beforehand — an unopened RecordRef raises at runtime, not at "
                              f"compile time",
                              ln, f"confirm {var} is opened on every path that reaches here"))


    # ── AL-9: perf smells the bcw prompt used to ask a model to spot ──────────
    for a, b in blocks:
        cursor = _loop_var(lines, b)
        for i in range(a, b + 1):
            ln = lines[i]

            # FlowFields calculated per row. The fix is one call before the loop, and
            # naming it is more use than saying "this is slow".
            m = re.search(r"\b(\w+)\s*\.\s*CalcFields\s*\(", ln)
            if m and not _TEMP_VAR.match(m.group(1)):
                var = m.group(1)
                head = "\n".join(lines[max(_proc_start(lines, a), a - 40):a])
                if not re.search(rf"\b{re.escape(var)}\s*\.\s*SetAutoCalcFields\s*\(",
                                 head, re.IGNORECASE):
                    out.append(_f("calcfields-without-autocalc", path, root, i, "warning",
                                  f"{var}.CalcFields inside a loop issues a separate query "
                                  f"per row for each FlowField",
                                  ln, f"call {var}.SetAutoCalcFields(...) once before the "
                                      f"loop so the values come back with the rows"))

            # A remote call per row: the loop now runs at network latency times N.
            hm = re.search(r"\b(\w+)\s*\.\s*(Send|Get|Post|Put|Delete)\s*\(", ln)
            if _HTTP.search(ln) or (hm and types.get(hm.group(1)) == "httpclient"):
                    out.append(_f("http-in-loop", path, root, i, "warning",
                                  "outbound HTTP inside a loop — the whole traversal now "
                                  "costs one network round trip per row",
                                  ln, "can the payload be batched into a single call?"))

    for i, ln in enumerate(lines):
        # SetCurrentKey picks an index; the filters decide whether it is usable. If not
        # one of the key's fields is filtered, the chosen index does no work.
        m = re.search(r"\b(\w+)\s*\.\s*SetCurrentKey\s*\(", ln)
        if m:
            var = m.group(1)
            key_fields = _args(raw_lines[i][m.start():])
            filtered = set()
            for w in raw_lines[i:min(len(raw_lines), i + 25)]:
                fm = re.search(rf"\b{re.escape(var)}\s*\.\s*Set(?:Range|Filter)\s*\(", w,
                               re.IGNORECASE)
                if fm:
                    a_ = _args(w[fm.start():])
                    if a_:
                        filtered.add(a_[0])
            if key_fields and filtered and not (set(key_fields) & filtered):
                out.append(_f("setcurrentkey-filter-mismatch", path, root, i, "warning",
                              f"{var}.SetCurrentKey({', '.join(key_fields)}) but the "
                              f"filters applied are on {', '.join(sorted(filtered))} — "
                              f"none of the key's fields is filtered, so the index cannot "
                              f"narrow the scan",
                              ln, "if the key is here for SORT ORDER this may be "
                                  "deliberate — confirm that, otherwise match the key to "
                                  "the filtered fields or drop it"))

        # BC's default HttpClient timeout is long. An unreachable endpoint holds the
        # session — and, inside a write, the locks with it.
        m = re.search(r"\b(\w+)\s*\.\s*(Send|Get|Post|Put|Delete)\s*\(", ln)
        if m:
            var = m.group(1)
            proc = _proc_start(lines, i)
            body = "\n".join(lines[proc:_proc_end(lines, proc)])
            if types.get(var) == "httpclient" and not re.search(
                    rf"\b{re.escape(var)}\s*\.\s*Timeout\s*:=", body, re.IGNORECASE):
                out.append(_f("httpclient-no-timeout", path, root, i, "warning",
                              f"{var}.{m.group(2)} with no {var}.Timeout set — an "
                              f"unresponsive endpoint blocks for the platform default",
                              ln, f"set {var}.Timeout before the call"))

    # ── FindSet(true) with no filter ───────────────────────────────────────────
    for i, ln in enumerate(lines):
        m = re.search(r"\b(\w+)\s*\.\s*FindSet\s*\(\s*true", ln, re.IGNORECASE)
        if not m:
            continue
        var = m.group(1)
        head = "\n".join(lines[max(0, i - 30):i]).lower()
        if not re.search(rf"\b{re.escape(var.lower())}\s*\.\s*set(range|filter|view)\s*\(", head):
            out.append(_f("findset-modify-unfiltered", path, root, i, "warning",
                          f"FindSet(true) on {var} with no SetRange/SetFilter/SetView above "
                          f"it — this opens the whole table for update and locks it",
                          ln, f"is a filter on {var} missing, or is a full-table update "
                              f"genuinely intended here?"))
    return out


def analyse(root, src=None):
    """All findings under a project, most severe then file order."""
    src = src or (os.path.join(root, "src") if os.path.isdir(os.path.join(root, "src"))
                  else root)
    out = []
    for p in sorted(glob.glob(os.path.join(src, "**", "*.al"), recursive=True)):
        out.extend(analyse_file(p, src))
    rank = {"error": 0, "warning": 1, "info": 2}
    return sorted(out, key=lambda f: (rank.get(f["severity"], 3), f["file"], f["line"]))


def format_findings(findings, limit=25):
    if not findings:
        return ""
    out = [f"AL SEMANTIC REVIEW ({len(findings)} finding(s), all advisory — these compile "
           f"cleanly and may still be wrong at runtime):"]
    for f in findings[:limit]:
        out.append(f'  [{f["rule"]}] {f["file"]}:{f["line"]}')
        out.append(f'      {f["reason"]}')
        out.append(f'      check: {f["suggested_next_check"]}')
    if len(findings) > limit:
        out.append(f"  … and {len(findings) - limit} more")
    return "\n".join(out)


def main():
    import argparse
    import json
    ap = argparse.ArgumentParser(prog="al_semantics")
    ap.add_argument("root", nargs="?", default=".")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--rule", help="show only this rule")
    a = ap.parse_args()
    fs = analyse(os.path.abspath(a.root))
    if a.rule:
        fs = [f for f in fs if f["rule"] == a.rule]
    if a.json:
        print(json.dumps(fs, indent=2))
    else:
        print(format_findings(fs, limit=10 ** 6) or "no semantic findings")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
