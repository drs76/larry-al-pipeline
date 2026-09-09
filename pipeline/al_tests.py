"""al_tests — run the project's AL test codeunits as part of the referee.

The referee has always been "it compiles and the cops are quiet". That is a strong
signal about validity and says nothing about behaviour: every build in this pipeline has
been accepted without one line of the extension ever executing.

Opt-in via `AL_RUN_TESTS=1`. Off by default because it needs a live BC environment and
turns a 40-second loop into a multi-minute one — but when it is ON it **fails closed**,
which is the point the review was explicit about:

    a test failure fails the referee, and an INFRASTRUCTURE failure (no container,
    publish rejected, no results file) also fails it, reported distinctly. What must
    never happen is an infrastructure problem being reported as a clean build — that is
    how "tests enabled" silently becomes "tests skipped".

A project with no test codeunits is not a failure. It records `no-tests` and carries on,
because most prototypes legitimately have none; requiring tests everywhere would just
push people to turn the flag off.

Execution goes through `bcl test`, which owns the environment and reports results. This
module owns only the decision: what did that mean for the referee.

`bcl test` has three backends and `AL_TEST_BACKEND` picks one:

    guest      (default) ClientContext over ssh inside the KVM Windows guest.
               The only backend that works on BC 27 — and AL_TEST_ENV defaults to
               a BC 27.9 environment, which is why it is the default here.
    altool     `al runtests` per codeunit over the dev endpoint. No Windows in the
               path. NEEDS BC 28.0+ (/dev/TestRunnerHub is Dev API 7.0).
    websocket  delegates to the upstream MsDyn365Bc.On.Linux runner. Highest
               fidelity for [HandlerFunctions] dispatch.

The last two select tests by discovering codeunit ids from the compiled .app, so they
need `app_file`; `guest` filters server-side by extension id instead.
"""
from __future__ import annotations

import os
import re
import subprocess

TEST_ENV_DEFAULT = "bc2"
# Which `bcl test` backend to use. GUEST is the default deliberately: the altool
# backend reaches BC through /dev/TestRunnerHub, which is Dev API 7.0 and needs
# BC 28.0+, and TEST_ENV_DEFAULT above is a BC 27.9 environment. Choosing the
# faster backend by default would break the default environment.
BACKEND_DEFAULT = "guest"
_BACKENDS = ("guest", "altool", "websocket")
# `bcl test` prints one summary line per run; its absence is the infrastructure signal.
_TOTAL_RE = re.compile(r"^TOTAL:\s*(\d+)\s*tests?,\s*(\d+)\s*passed,\s*(\d+)\s*failed",
                       re.MULTILINE)
# The same line carries a SEPARATE codeunit-error count. A codeunit that failed to
# run at all contributes 0 to tests/passed/failed, so a run where every codeunit
# errored reads as "0 tests, 0 passed, 0 failed" — indistinguishable from a clean
# empty run unless this is read too. Optional in the pattern because the guest
# backend's older summary line does not carry the field.
_ERRORS_RE = re.compile(r"(\d+)\s*codeunit error", re.MULTILINE)
# Not anchored to line start. A test codeunit written on one line is unusual but
# legal, and missing it reports the project as having NO tests — which is a pass.
# The failure direction matters: this must not be able to turn tests off silently.
_SUBTYPE_TEST = re.compile(r"\bSubtype\s*=\s*Test\s*;", re.IGNORECASE)
_FAILED_LINE = re.compile(r"^\s*✗\s*(.+)$", re.MULTILINE)


def find_test_codeunits(src_root):
    """Files declaring `Subtype = Test`. No tests is a state, not an error."""
    out = []
    for dp, _, fs in os.walk(src_root):
        for fn in fs:
            if not fn.endswith(".al"):
                continue
            p = os.path.join(dp, fn)
            try:
                if _SUBTYPE_TEST.search(open(p, encoding="utf-8-sig",
                                             errors="replace").read()):
                    out.append(p)
            except OSError:
                continue
    return sorted(out)


def parse_results(output):
    """(total, passed, failed, failures) from `bcl test` output.

    Returns None when no TOTAL line is present — the caller MUST treat that as an
    infrastructure failure rather than a zero-test pass. Deriving "0 tests, all fine"
    from missing output is exactly the silent downgrade this module exists to prevent.
    """
    m = _TOTAL_RE.search(output or "")
    if not m:
        return None
    total, passed, failed = (int(m.group(i)) for i in (1, 2, 3))
    return total, passed, failed, [f.strip() for f in _FAILED_LINE.findall(output or "")]


def parse_codeunit_errors(output):
    """Codeunit-level errors from a `bcl test` summary line, 0 when absent.

    Separate from parse_results so the 4-tuple contract stays as it was. A
    codeunit that never ran contributes nothing to the test counts, so this is
    the only place a "the hub refused every codeunit" run is visible.
    """
    m = _ERRORS_RE.search(output or "")
    return int(m.group(1)) if m else 0


def run(project_root, app_id, bc_version, env=None, app_file=None, timeout=1800,
        runner=None, codeunit="*", backend=None):
    """Publish and test. Returns a result dict; never raises.

    {status, ok, total, passed, failed, failures, env, backend, detail}
    status: no-tests | passed | failed | infrastructure
    `ok` is what the referee consumes and is False for BOTH failed and infrastructure.

    `backend` picks the `bcl test -runner`; `runner` is the command executor and
    exists for testing. Two different things, unfortunately adjacent.
    """
    env = env or os.environ.get("AL_TEST_ENV", TEST_ENV_DEFAULT)
    backend = (backend or os.environ.get("AL_TEST_BACKEND", BACKEND_DEFAULT)).lower()
    res = {"status": "infrastructure", "ok": False, "total": 0, "passed": 0,
           "failed": 0, "failures": [], "env": env, "backend": backend, "detail": "",
           "selection": codeunit or "*"}

    if backend not in _BACKENDS:
        res["detail"] = f"unknown AL_TEST_BACKEND {backend!r} — want one of {', '.join(_BACKENDS)}"
        return res

    src = os.path.join(project_root, "src")
    tests = find_test_codeunits(src if os.path.isdir(src) else project_root)
    if not tests:
        res.update(status="no-tests", ok=True,
                   detail="project declares no Subtype=Test codeunits")
        return res

    if not app_id:
        res["detail"] = "no extension id in app.json — cannot select tests to run"
        return res

    def _run(cmd):
        if runner:
            return runner(cmd)
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        return r.returncode, (r.stdout or "") + (r.stderr or "")

    # The altool and websocket backends take -app, not -extension: they discover
    # the codeunit ids from the compiled symbol rather than filtering server-side.
    # Without the .app there is nothing to discover, so this is a hard stop and
    # not a fallback to the whole suite.
    if backend != "guest" and not app_file:
        res["detail"] = (f"backend {backend} needs the compiled .app to discover test "
                         f"codeunits, and none was found in {project_root}")
        return res

    # The altool backend publishes -app itself, with forcesync. Publishing twice
    # here would only add a weaker (synchronize) publish in front of it.
    if app_file and backend == "guest":
        # -name is not optional here: `bcl publish` defaults to the `demo` environment,
        # so omitting it publishes to one environment and tests another — which shows up
        # as "no tests found" rather than as the mistake it is.
        rc, out = _run(["bcl", "publish", "-name", env, app_file])
        if rc != 0 and "already" not in out.lower():
            res["detail"] = f"publish failed: {out.strip()[-600:]}"
            return res

    cmd = ["bcl", "test", "-name", env, "-runner", backend]
    if backend == "guest":
        cmd += ["-extension", app_id]
    else:
        cmd += ["-app", app_file]
    # AL-10 targeted selection. "*" is everything; a narrowed filter must come from the
    # object graph, never from a guess — running a subset you cannot justify is how a
    # green run stops meaning anything.
    if codeunit and codeunit != "*":
        cmd += ["-codeunit", codeunit]
    # -version drives the test-toolkit publish out of the artifact cache, which only
    # the guest backend needs. altool carries its own compiler and the native tier
    # already ships the toolkit.
    if bc_version and backend == "guest":
        cmd += ["-version", str(bc_version)]
    try:
        rc, out = _run(cmd)
    except subprocess.TimeoutExpired:
        res["detail"] = f"test run exceeded {timeout}s against {env}"
        return res

    parsed = parse_results(out)
    if parsed is None:
        # No summary line: the container is down, publish never landed, or the results
        # file was unreadable. bcl exits non-zero for these and says which.
        res["detail"] = (f"no test results from {env} — treating as infrastructure "
                         f"failure, not a pass: {out.strip()[-600:]}")
        return res

    total, passed, failed, failures = parsed
    errors = parse_codeunit_errors(out)
    res.update(total=total, passed=passed, failed=failed, failures=failures,
               codeunit_errors=errors)

    # A codeunit that never ran contributes 0 to every count above. Reading only
    # those counts, a run where the hub refused every codeunit is "0 tests, 0
    # passed, 0 failed" — which would score as a pass.
    if errors:
        res["detail"] = (f"{errors} codeunit(s) failed to run on {env} — treating as "
                         f"infrastructure failure, not a pass: {out.strip()[-600:]}")
        return res

    # We only got here because the project DOES declare test codeunits. Running
    # them and getting none back is a broken selection or a broken environment,
    # never a clean build.
    if total == 0:
        res["detail"] = (f"{len(tests)} test codeunit(s) declared but none ran on {env} "
                         f"(selection: {res['selection']}) — treating as infrastructure "
                         f"failure, not a pass")
        return res

    if failed:
        res.update(status="failed", ok=False,
                   detail=f"{failed} of {total} test(s) failed")
    else:
        res.update(status="passed", ok=True, detail=f"{passed}/{total} passed")
    return res


def summary(res):
    if res["status"] == "no-tests":
        return "tests: none declared (not a failure)"
    where = f"{res['env']} via {res.get('backend', BACKEND_DEFAULT)}"
    if res["status"] == "infrastructure":
        return f"tests: INFRASTRUCTURE FAILURE on {where} — {res['detail']}"
    s = f"tests: {res['passed']}/{res['total']} passed on {where}"
    if res.get("selection") not in (None, "*"):
        s += f"  (targeted: {res['selection']})"
    if res["failures"]:
        s += "\n  failed: " + "\n          ".join(res["failures"][:10])
    return s
