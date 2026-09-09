"""al_testgen — the model proposes tests; the referee decides whether they pass.

Two halves that are usually conflated and should not be.

**Targeted selection** is deterministic. Given the objects a change touched, `al_graph`
already knows which test codeunits reach them, so a fix round can run four tests instead
of four hundred. Nothing is generated and nothing is guessed.

**Generation** uses a model, and the entire safety story is that its output is a
PROPOSAL. A generated test is worth nothing until it compiles and runs; a test that
passes because it asserts nothing is worse than no test, so generated tests go through
exactly the same referee as hand-written ones.

The containment rule is the part worth being strict about. A model asked for tests will
cheerfully write the table it wants to test against, and a "test generation" run that
quietly adds a production table to the extension is a supply-chain problem, not a
convenience. So:

  * generated files land ONLY in the test folder, under an id range reserved for tests
  * every generated object MUST be a `Subtype = Test` codeunit — anything else is
    rejected, not fixed up
  * generated files carry a header marking them as generated, so nobody mistakes them
    for reviewed work

Rejection is deliberate rather than repair: silently deleting the offending production
object out of a generated file leaves tests that reference something that no longer
exists, which fails later and more confusingly.
"""
from __future__ import annotations

import os
import re
import subprocess
import time

import al_graph

PI_BIN = (os.environ.get("PI_BIN") or __import__("shutil").which("pi")
          or os.path.expanduser("~/.npm-global/bin/pi"))
PI_EXT = os.path.expanduser(os.environ.get("PI_EXT", "~/.pi/ollama-provider.ts"))
TESTGEN_MODEL = os.environ.get("TESTGEN_MODEL",
                               os.environ.get("PI_CODER_MODEL", "ollama/qwen3-coder:30b"))
TEST_DIR = os.environ.get("AL_TEST_DIR", "src/test")
TIMEOUT = int(os.environ.get("TESTGEN_TIMEOUT", "900"))

GENERATED_HEADER = "// GENERATED TEST — proposed by a model, kept only because it compiles and runs."

# The scenarios worth asking for. A model left to itself writes the happy path and stops,
# and the happy path is the case that was already working.
SCENARIOS = [
    "normal case — the documented behaviour on valid input",
    "boundary value — first/last/zero/max, and the value either side",
    "missing setup — the setup record or No. Series does not exist",
    "invalid state — the operation is called when the record forbids it",
    "permissions — the user lacks rights to the table being touched",
    "retry / idempotency — running the same operation twice must not double-apply",
    "currency and dimension effects — non-local currency, and a dimension that must flow",
    "empty / no-record — an empty filtered set, and a table with no rows at all",
    "posting failure — a posting routine that errors partway must leave nothing behind",
    "upgrade edge cases — data written by the previous version is still readable",
]

_OBJ_RE = re.compile(
    r'^\s*(?P<kind>table|tableextension|page|pageextension|codeunit|report|query|xmlport|'
    r'enum|enumextension|interface|permissionset|profile|controladdin)\s+'
    r'(?P<id>\d+)?\s*(?P<name>"[^"]+"|\w+)', re.IGNORECASE | re.MULTILINE)
# MULTILINE matters: mark_generated() puts three comment lines above the object, and
# without it `^` only ever matches the very start of the string — so every MARKED test
# looked like it contained no AL at all and write() rejected the entire accept path.
# Not anchored to line start: a codeunit written on one line is unusual but legal, and
# rejecting it with "no Subtype = Test" when the property is right there sends the reader
# after the wrong problem.
_SUBTYPE_TEST_RE = re.compile(r"\bSubtype\s*=\s*Test\s*;", re.IGNORECASE)


class ContainmentError(RuntimeError):
    """Generated content tried to leave test scope."""


# ─── targeted selection (deterministic) ────────────────────────────────────────

def select_tests(project_root, changed, graph=None):
    """Test codeunits that reach any of `changed`.

    Returns (selected, reason). An EMPTY selection is a real answer meaning nothing
    covers the change — it must never be read as "no tests needed", so the caller is told
    which it is.
    """
    g = graph or al_graph.build(project_root)
    changed = [changed] if isinstance(changed, str) else list(changed)
    if not changed:
        return [], "no changed objects given — nothing to select against"
    hits = al_graph.tests_for(g, changed)
    if not hits:
        return [], (f"no test codeunit reaches {', '.join(changed)} — this change is "
                    f"UNTESTED, which is not the same as passing")
    return hits, f"{len(hits)} test codeunit(s) cover {', '.join(changed)}"


def codeunit_filter(project_root, selected, graph=None):
    """`bcl test -codeunit` filter for the selected tests.

    bcl matches by codeunit NAME, so the graph node ids are mapped back to the names the
    runner understands. Returns "*" when nothing was selected — running everything is the
    safe default, and quietly running NOTHING would report a pass for an empty run.
    """
    if not selected:
        return "*"
    g = graph or al_graph.build(project_root)
    by_id = {n["id"]: n["name"] for n in g["nodes"]}
    names = sorted({by_id.get(s, s.split(":", 1)[-1]) for s in selected})
    return "|".join(names) if names else "*"


# ─── containment (deterministic, enforced before anything is written) ──────────

def objects_in(source):
    """[(kind, id, name)] declared in a chunk of AL."""
    out = []
    for m in _OBJ_RE.finditer(source or ""):
        out.append((m.group("kind").lower(),
                    int(m.group("id")) if m.group("id") else None,
                    (m.group("name") or "").strip('"')))
    return out


def check_containment(source, id_range=(139900, 139999)):
    """[reason] — why this generated source may not be written.

    Empty means it is safe. The checks are all "is this a test", never "can this be made
    into a test": a generated production object is a rejection, not something to repair.
    """
    problems = []
    objs = objects_in(source)
    if not objs:
        return ["no AL object found in the generated output"]
    for kind, oid, name in objs:
        if kind != "codeunit":
            problems.append(
                f'generated a {kind} "{name}" — test generation may only produce test '
                f"codeunits, and a production object slipping into a test run is how an "
                f"extension grows something nobody reviewed")
            continue
        if oid is None:
            problems.append(f'codeunit "{name}" has no object id')
        elif not (id_range[0] <= oid <= id_range[1]):
            problems.append(
                f'codeunit {oid} "{name}" is outside the reserved test id range '
                f"{id_range[0]}-{id_range[1]} — test objects must not consume production ids")
    if not _SUBTYPE_TEST_RE.search(source or ""):
        problems.append("no `Subtype = Test;` — this would compile as a production "
                        "codeunit and never run as a test")
    return problems


def mark_generated(source, target=""):
    """Prefix the generated-test header. Clearly marked is an acceptance criterion, and
    it is also how a later reader knows this was never reviewed by a person."""
    stamp = (f"{GENERATED_HEADER}\n// target: {target}\n"
             f"// generated: {time.strftime('%Y-%m-%d')} by {TESTGEN_MODEL}\n")
    return stamp + (source or "").lstrip()


def is_generated(path):
    try:
        with open(path, encoding="utf-8-sig", errors="replace") as f:
            return GENERATED_HEADER in f.read(400)
    except OSError:
        return False


# ─── generation (model proposes) ───────────────────────────────────────────────

def test_framework_ready(project_root):
    """(ok, reason) — can a generated test that uses Library Assert compile here?

    Generated tests assert with `Codeunit "Library Assert"`, which lives in Microsoft's
    Test Framework. If neither app.json nor .alpackages provides it, EVERY generated test
    fails with AL0185 and the cause looks like bad generation rather than a missing
    dependency. Checked before spending a model call.
    """
    import glob as _g
    import json as _j
    try:
        with open(os.path.join(project_root, "app.json")) as f:
            deps = _j.load(f).get("dependencies") or []
    except (OSError, ValueError):
        deps = []
    if any("test" in str(d.get("name", "")).lower() or
           "assert" in str(d.get("name", "")).lower() for d in deps):
        return True, "Test Framework declared in app.json"
    pkgs = _g.glob(os.path.join(project_root, ".alpackages", "*.app"))
    if any("Assert" in os.path.basename(x) or "Test" in os.path.basename(x) for x in pkgs):
        return True, "Test Framework symbols present in .alpackages"
    return False, (
        'no Test Framework dependency — generated tests assert with Codeunit '
        '"Library Assert" and will fail with AL0185. Add the Microsoft Test Framework '
        "apps as a dependency, or write assertions by hand (as the al-runtime-probes "
        "extension does, deliberately, to stay dependency-free).")


def build_prompt(target, source, scenarios=None, id_range=(139900, 139999)):
    picked = scenarios or SCENARIOS
    return (
        "You are writing AL test codeunits for Microsoft Dynamics 365 Business Central.\n\n"
        "STRICT OUTPUT RULES — output is rejected wholesale if any is broken:\n"
        f"- Output ONLY AL source for ONE codeunit with `Subtype = Test;`. No prose, no fences.\n"
        f"- The codeunit id MUST be in {id_range[0]}-{id_range[1]}.\n"
        "- Do NOT declare a table, page, enum, report or any other object. If the test "
        "needs data, create it inside the test with `Init`/`Insert`, or use a temporary "
        "record — never by declaring a new table.\n"
        "- Every test procedure carries [Test] and asserts something. A test that only "
        "runs code and asserts nothing is worse than no test: it reports success for "
        "behaviour nobody checked.\n"
        "- Assertions come from the Library Assert codeunit, and it MUST be declared as a "
        "variable in every procedure that uses it:\n"
        "      var\n"
        "          LibraryAssert: Codeunit \"Library Assert\";\n"
        "  then `LibraryAssert.AreEqual(Expected, Actual, 'message')`, "
        "`LibraryAssert.IsTrue(...)`, or for an expected failure:\n"
        "      asserterror MyCodeunit.Thing();\n"
        "      LibraryAssert.ExpectedError('the message');\n"
        "  An undeclared LibraryAssert is the single most common reason generated tests "
        "fail to compile.\n\n"
        "COVER THESE SCENARIOS where they apply to the code under test — say so in a "
        "comment when one does not apply, rather than silently skipping it:\n"
        + "\n".join(f"  - {s}" for s in picked)
        + f"\n\n===== CODE UNDER TEST ({target}) =====\n{source}\n")


def _extract_al(text):
    """AL out of a model response — fenced or not."""
    if not text:
        return ""
    m = re.search(r"```(?:al)?\s*\n(.*?)```", text, re.DOTALL | re.IGNORECASE)
    body = m.group(1) if m else text
    i = _OBJ_RE.search(body)
    return body[i.start():].strip() if i else body.strip()


def propose(target, source, model=None, timeout=None, runner=None,
            id_range=(139900, 139999)):
    """Ask a model for tests. Returns {ok, source, problems, raw}.

    Never writes. The caller decides, after check_containment, whether this is allowed
    anywhere near the project.
    """
    prompt = build_prompt(target, source, id_range=id_range)
    if runner:
        raw = runner(prompt)
    else:
        # NO tools. The code under test is already in the prompt, so the model has
        # nothing to look up — and offering tools it does not need makes it emit a tool
        # CALL instead of AL, which arrives as text and parses to nothing. Observed:
        # a 4-second run returning "<function=read>…" and no source at all.
        cmd = [PI_BIN, "-e", PI_EXT, "--model", model or TESTGEN_MODEL, "-p",
               "--no-session", "--tools", ""]
        try:
            r = subprocess.run(cmd, input=prompt, capture_output=True, text=True,
                               timeout=timeout or TIMEOUT)
            raw = (r.stdout or "").strip()
        except subprocess.TimeoutExpired:
            return {"ok": False, "source": "", "raw": "",
                    "problems": [f"test generation timed out after {timeout or TIMEOUT}s"]}
        except OSError as e:
            return {"ok": False, "source": "", "raw": "",
                    "problems": [f"could not run the generator: {e}"]}
    al = _extract_al(raw)
    problems = check_containment(al, id_range)
    return {"ok": not problems, "source": mark_generated(al, target) if not problems else al,
            "problems": problems, "raw": raw}


def write(project_root, name, source):
    """Write an ACCEPTED generated test into the isolated test folder.

    Refuses to write anything check_containment rejects, even if a caller asks — the
    containment rule is the point of the module, not a suggestion to it.
    """
    problems = check_containment(source)
    if problems:
        raise ContainmentError("; ".join(problems))
    # normpath, because TEST_DIR carries a forward slash and os.path.join does NOT
    # normalise an embedded separator — it concatenates. On Windows that yields a mixed
    # path like C:\proj\src/test. Harmless for file IO, which accepts either, but it
    # leaks a non-native separator into every downstream string comparison, and this
    # pipeline does path containment checks on exactly that basis.
    d = os.path.normpath(os.path.join(project_root, TEST_DIR))
    os.makedirs(d, exist_ok=True)
    path = os.path.join(d, f"{name}.Codeunit.al")
    with open(path, "w") as f:
        f.write(source if GENERATED_HEADER in source[:400] else mark_generated(source))
    return path


def main():
    import argparse
    import json
    ap = argparse.ArgumentParser(prog="al_testgen")
    ap.add_argument("root", nargs="?", default=".")
    ap.add_argument("--select", metavar="OBJECT", action="append",
                    help="test codeunits covering OBJECT (repeatable)")
    ap.add_argument("--filter", action="store_true", help="print a bcl -codeunit filter")
    ap.add_argument("--propose", metavar="FILE", help="generate tests for an AL file")
    ap.add_argument("--write", metavar="NAME", help="write accepted output as NAME")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    root = os.path.abspath(a.root)

    if a.select:
        sel, why = select_tests(root, a.select)
        if a.filter:
            print(codeunit_filter(root, sel))
        elif a.json:
            print(json.dumps({"selected": sel, "reason": why}, indent=2))
        else:
            print(why)
            for s in sel:
                print(f"  {s}")
        return 0 if sel else 1

    if a.propose:
        ready, why = test_framework_ready(root)
        if not ready:
            print(f"  ⚠ {why}")
        src = open(a.propose, encoding="utf-8-sig", errors="replace").read()
        res = propose(os.path.basename(a.propose), src)
        if not res["ok"]:
            print("REJECTED — generated output left test scope:")
            for p in res["problems"]:
                print(f"  ⛔ {p}")
            return 1
        if a.write:
            print(f"wrote {write(root, a.write, res['source'])}")
        else:
            print(res["source"])
        return 0

    ap.print_help()
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
