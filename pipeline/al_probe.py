"""al_probe — settle an AL question by asking the compiler, in a throwaway project.

`al_symbols` answers "does this exist in the symbols". Plenty of AL questions are not of
that shape: is this property legal on this object type, does this overload accept a
Text[100], will this attribute combination compile at all. Those have exactly one
authority — the compiler — and today the only way to consult it is to write the guess
into the real project and burn a full referee round finding out.

A probe is an EXPERIMENT, not a generated change. It never touches the target project:
the workspace is a fresh temp directory, the target's `.alpackages` is linked in
read-only, and the directory is removed whether the probe passes, fails, times out or
raises.

Four outcomes, deliberately distinct — collapsing the last two is the whole trap:

    verified   compiled clean; the hypothesis is legal AL
    rejected   the compiler refused it, with structural diagnostics
    timeout    the compile exceeded its budget — says NOTHING about legality
    error      the harness could not run (no compiler, no symbols, bad workspace)

`rejected` is a fact about the code. `timeout` and `error` are facts about the harness,
and reporting either as "rejected" would teach a model that correct AL is illegal.

Bare compile by default: a probe asks "is this legal", not "is this good", so the cops
are off unless `analyzers=True`. That is the opposite of the referee's rule in
run-build.py, and for the opposite reason.

This module parses SARIF itself rather than importing run-build.py's copy — run-build
imports THIS module, and a library that prints diagnostics into a build log is the wrong
shape. The format is fixed by the AL compiler, so the two readers cannot drift far.
"""
from __future__ import annotations

import glob
import json
import os
import re
import shutil
import subprocess
import tempfile
import uuid

AL_CLI = os.environ.get("AL_CLI", os.path.expanduser("~/.dotnet/tools/al"))
PROBE_TIMEOUT = int(os.environ.get("AL_PROBE_TIMEOUT", "180"))
_COPS = ("CodeCop", "UICop", "PerTenantExtensionCop")


class ProbeError(RuntimeError):
    """The harness could not run the experiment. Never means the AL was wrong."""


def parse_sarif(path):
    """AL /errorlog SARIF (v0.2) → [{code, severity, uri, line, message}]."""
    try:
        with open(path) as f:
            d = json.load(f)
    except (OSError, ValueError):
        return []
    out = []
    for it in d.get("issues", []):
        loc = (it.get("locations") or [{}])[0]
        tgt = loc.get("analysisTarget") or loc.get("resultFile") or [{}]
        tgt = tgt[0] if isinstance(tgt, list) else tgt
        reg = tgt.get("region", {}) if isinstance(tgt, dict) else {}
        props = it.get("properties", {}) or {}
        out.append({"code": it.get("ruleId", ""),
                    "severity": props.get("defaultSeverity") or props.get("severity") or "Error",
                    "line": reg.get("startLine"),
                    "message": it.get("fullMessage") or it.get("shortMessage") or ""})
    return out


# The compiler also prints diagnostics to stdout. SARIF is preferred — it is structured —
# but a compile that dies before writing the log still says why on stdout.
_DIAG_RE = re.compile(
    r"\((?P<line>\d+),\d+\):\s*(?P<severity>error|warning|info)\s+(?P<code>[A-Z]{2,3}\d{4}):\s*"
    r"(?P<message>.*)")


def _diags_from_text(text):
    return [{"code": m.group("code"), "severity": m.group("severity").capitalize(),
             "line": int(m.group("line")), "message": m.group("message").strip()}
            for m in _DIAG_RE.finditer(text or "")]


def _analyzer_dlls():
    """Cop DLLs for an analyzers=True probe. Same TFM-agnostic resolution as
    run-build._analyzer_dir — a second hard-coded `net10.0` here would have broken on a
    different day to the first."""
    hits = glob.glob(os.path.expanduser(
        "~/.dotnet/tools/.store/microsoft.dynamics.businesscentral.development.tools"
        "/**/Microsoft.Dynamics.Nav.CodeCop.dll"), recursive=True)
    if not hits:
        return []
    d = os.path.dirname(next((h for h in hits if "/net10.0/" in h), hits[0]))
    return [p for p in (os.path.join(d, f"Microsoft.Dynamics.Nav.{n}.dll") for n in _COPS)
            if os.path.exists(p)]


def _manifest_of(project_root):
    """runtime/platform/application from a real project, so the probe compiles under the
    same conditions as the code the question is actually about."""
    try:
        with open(os.path.join(project_root, "app.json")) as f:
            aj = json.load(f)
        return {k: aj[k] for k in ("runtime", "platform", "application") if aj.get(k)}
    except (OSError, ValueError, TypeError):
        return {}


def _resolve_packages(alpackages, like_project):
    if alpackages:
        return alpackages
    if like_project:
        return os.path.join(like_project, ".alpackages")
    raise ProbeError("no symbols: pass alpackages= or like_project=")


# A bare statement is not a compilable unit. Wrapping it in a codeunit lets a model ask
# "does this line compile" without composing a whole object around the question.
# NOT `Run` — every codeunit already has a built-in Run(), so a probe procedure by that
# name fails with AL0440 no matter what the statements say. That made both a valid and an
# invalid hypothesis come back "rejected", which is the failure mode where a probe looks
# like it works because the wrong answer is the common one.
_SNIPPET_TEMPLATE = """codeunit 50000 "Probe Snippet"
{{
    procedure ProbeMain()
    var
{vars}
    begin
{body}
    end;
}}
"""


def wrap_snippet(body, vars_block=""):
    """Statements → a compilable codeunit. `vars_block` is raw AL var declarations."""
    ind = "\n".join("        " + ln.strip() for ln in body.strip().splitlines() if ln.strip())
    v = "\n".join("        " + ln.strip() for ln in (vars_block or "").splitlines()
                  if ln.strip())
    return _SNIPPET_TEMPLATE.format(vars=v, body=ind)


def probe(source, *, filename="Probe.al", alpackages=None, like_project=None,
          analyzers=False, timeout=None, extra_files=None):
    """Compile `source` alone in a temp project. Returns a result dict; never raises.

    {status, ok, diagnostics, errors, warnings, summary, source, workspace_removed}
    status is one of verified | rejected | timeout | error.
    `ok` is True ONLY for `verified` — a timeout is not a pass.
    """
    timeout = timeout or PROBE_TIMEOUT
    res = {"status": "error", "ok": False, "diagnostics": [], "errors": [],
           "warnings": [], "summary": "", "source": source, "workspace_removed": True}

    try:
        pkgs = _resolve_packages(alpackages, like_project)
    except ProbeError as e:
        res["summary"] = str(e)
        return res
    if not os.path.isdir(pkgs) or not glob.glob(os.path.join(pkgs, "*.app")):
        res["summary"] = f"no symbol packages at {pkgs} — cannot compile a probe"
        return res
    if not os.path.exists(AL_CLI):
        res["summary"] = f"AL compiler not found at {AL_CLI}"
        return res

    work = tempfile.mkdtemp(prefix="al-probe-")
    try:
        os.makedirs(os.path.join(work, "src"))
        # Linked, not copied: the Base Application package alone is ~43MB, and a probe
        # that costs a 43MB copy is a probe nobody runs. The compiler only READS
        # packagecachepath, and a test asserts the target tree is unchanged afterwards.
        os.symlink(os.path.abspath(pkgs), os.path.join(work, ".alpackages"))

        manifest = {"id": str(uuid.uuid4()), "name": "AL Probe", "publisher": "Probe",
                    "version": "1.0.0.0", "runtime": "16.0", "platform": "27.0.0.0",
                    "application": "27.0.0.0",
                    "idRanges": [{"from": 50000, "to": 50099}]}
        manifest.update(_manifest_of(like_project) if like_project else {})
        with open(os.path.join(work, "app.json"), "w") as f:
            json.dump(manifest, f, indent=2)

        with open(os.path.join(work, "src", filename), "w") as f:
            f.write(source)
        for name, text in (extra_files or {}).items():
            with open(os.path.join(work, "src", os.path.basename(name)), "w") as f:
                f.write(text)

        sarif = os.path.join(work, "probe.sarif")
        cmd = [AL_CLI, "compile", f"/project:{work}",
               f"/packagecachepath:{work}/.alpackages", f"/errorlog:{sarif}"]
        if analyzers:
            cmd += [f"/analyzer:{d}" for d in _analyzer_dlls()]

        try:
            r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        except subprocess.TimeoutExpired:
            # Says nothing about the hypothesis. Reporting this as `rejected` would
            # teach the model that correct AL is illegal.
            res.update(status="timeout",
                       summary=f"probe compile exceeded {timeout}s — inconclusive, "
                               f"this is NOT evidence the construct is invalid")
            return res
        except OSError as e:
            res["summary"] = f"could not run the AL compiler: {e}"
            return res

        out = (r.stdout or "") + (r.stderr or "")
        diags = parse_sarif(sarif) or _diags_from_text(out)
        errors = [d for d in diags if str(d["severity"]).lower().startswith("error")]
        warnings = [d for d in diags if str(d["severity"]).lower().startswith("warn")]
        res.update(diagnostics=diags, errors=errors, warnings=warnings)

        if r.returncode == 0 and not errors:
            res.update(status="verified", ok=True,
                       summary="compiles — the construct is legal AL here"
                               + (f" ({len(warnings)} warning(s))" if warnings else ""))
        elif errors:
            res.update(status="rejected",
                       summary="; ".join(f"{d['code']}: {d['message']}"
                                         for d in errors[:4]))
        else:
            # Non-zero exit with no diagnostics is a harness problem, not a verdict.
            res.update(status="error",
                       summary=f"compiler exited {r.returncode} with no diagnostics — "
                               f"treating as harness failure, not rejection: "
                               f"{out.strip()[-400:]}")
        return res
    except OSError as e:
        res["summary"] = f"probe workspace failed: {e}"
        return res
    finally:
        shutil.rmtree(work, ignore_errors=True)


def probe_snippet(body, vars_block="", **kw):
    """Probe a few statements rather than a whole object."""
    return probe(wrap_snippet(body, vars_block), **kw)


def format_result(res, hypothesis=""):
    """The line the model gets back. States the verdict AND its limits."""
    head = f"AL PROBE{f' — {hypothesis}' if hypothesis else ''}: {res['status'].upper()}"
    lines = [head, f"  {res['summary']}"]
    for d in res["errors"][:6]:
        lines.append(f"  error {d['code']} (line {d['line']}): {d['message']}")
    if res["status"] in ("timeout", "error"):
        lines.append("  → inconclusive. Do not treat this as proof either way.")
    return "\n".join(lines)


def main():
    import argparse
    ap = argparse.ArgumentParser(
        prog="al_probe", description="compile an AL hypothesis in a throwaway project")
    ap.add_argument("file", nargs="?", help="AL source file (default: stdin)")
    ap.add_argument("--project", help="inherit runtime/symbols from this project")
    ap.add_argument("--alpackages")
    ap.add_argument("--snippet", action="store_true", help="input is statements, not an object")
    ap.add_argument("--vars", default="", help="var declarations for --snippet")
    ap.add_argument("--analyzers", action="store_true", help="also run the cops")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    import sys
    src = open(a.file).read() if a.file else sys.stdin.read()
    fn = probe_snippet if a.snippet else probe
    kw = dict(alpackages=a.alpackages, like_project=a.project, analyzers=a.analyzers)
    res = fn(src, a.vars, **kw) if a.snippet else fn(src, **kw)
    if a.json:
        print(json.dumps(res, indent=2))
    else:
        print(format_result(res))
    return 0 if res["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
