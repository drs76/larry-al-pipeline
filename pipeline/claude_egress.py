"""claude_egress.py — the one way pipeline code invokes Claude Code (anon hook, phase 5).

Every orchestrator's run_claude_code() delegates here, so Claude execution is routed by
egress policy in exactly one place:

  personal        → raw `claude -p` in the real project root (unchanged behaviour)
  enterprise-anon → Mode B scrubbed mirror (anon_workspace): scrub tracked files →
                    claude edits the mirror → reverse-map the diff → apply to the real
                    repo. This call IS the anon hook, so it arms CLAUDE_ANON for the
                    egress gate and disarms it after.
  local-only      → hard-blocked (returns ""), same as before phase 5.

Contract matches the old inline implementations: returns Claude's final text (stdout +
stderr), "" on block/timeout/abort. File changes land in the real project root either
directly (personal) or via the reversed patch (enterprise-anon).

enterprise-anon caveats (inherited from anon_workspace):
  - the project must be a git repo; only TRACKED text files are mirrored — commit new
    files before escalating or Claude won't see them;
  - a HIGH-confidence secret anywhere in the tracked tree aborts the run closed.
See tooling/anon-claude-hook.spec.md §4–5.
"""
import json
import os
import subprocess
import time

import egress_policy
import anon_workspace


# ---------------------------------------------------------------------------
# Usage accounting (routing-economics prerequisite)
#
# duration_s is not a cost model: escalation is billed per token, the local
# alternative is free but slow. Every Claude invocation in the pipeline passes through
# this module, so capture belongs here and nowhere else.
#
# Shape is `claude -p --output-format json`, whose result object the shipped CLI defines as
#   {type, subtype, duration_ms, duration_api_ms, is_error, num_turns, result,
#    stop_reason, total_cost_usd, usage{...}, modelUsage{}, session_id, uuid}
# See reference/claude-usage-schema.md — that file is the frozen contract.
#
# STRICT MODE. An economics run must never silently score a call it could not price.
# CLAUDE_USAGE_STRICT=1 turns an unattributable call into a hard failure. Default is
# warn-and-record, because instrumentation must not break an ordinary build.
# ---------------------------------------------------------------------------
_usage_log = []


class UsageUnattributable(RuntimeError):
    """A Claude call produced no parseable usage while strict mode was on."""


def usage_records():
    """Every Claude call this process made, in order."""
    return list(_usage_log)


def usage_totals():
    """Summed usage for the metrics row. `calls_missing_usage` > 0 means the spend
    figure is INCOMPLETE and must not be reported as a cost."""
    t = {"claude_calls": len(_usage_log), "claude_input_tokens": 0,
         "claude_output_tokens": 0, "claude_cache_read_tokens": 0,
         "claude_cost_usd": 0.0, "claude_api_ms": 0, "claude_turns": 0,
         "claude_calls_missing_usage": 0}
    for r in _usage_log:
        if not r.get("attributed"):
            t["claude_calls_missing_usage"] += 1
            continue
        u = r.get("usage") or {}
        t["claude_input_tokens"] += u.get("input_tokens") or 0
        t["claude_output_tokens"] += u.get("output_tokens") or 0
        t["claude_cache_read_tokens"] += u.get("cache_read_input_tokens") or 0
        t["claude_cost_usd"] += r.get("total_cost_usd") or 0.0
        t["claude_api_ms"] += r.get("duration_api_ms") or 0
        t["claude_turns"] += r.get("num_turns") or 0
    t["claude_cost_usd"] = round(t["claude_cost_usd"], 6)
    # Per-call realised cost, compact, so a run can be audited call-by-call rather than
    # only in aggregate. Telemetry: nothing in the pipeline branches on it.
    t["claude_call_costs"] = [
        {"label": r.get("label"), "attributed": r.get("attributed"),
         "cost_usd": r.get("total_cost_usd"),
         "in": (r.get("usage") or {}).get("input_tokens"),
         "out": (r.get("usage") or {}).get("output_tokens"),
         "wall_s": r.get("wall_s")}
        for r in _usage_log]
    return t


def reset_usage():
    _usage_log.clear()


def _record(label, wall_s, parsed, raw_len, reason=""):
    # A well-formed result object is not proof of a priced call. The CLI synthesizes
    #   {type:"result", subtype:"success", total_cost_usd:0, num_turns:0, usage:{zeros}}
    # on some paths, and an earlier version of this function accepted it as attributed and
    # scored it at $0 — the guard recognising the healthy SHAPE while a degenerate instance
    # walked through it. Zero tokens means unpriceable, not free.
    if parsed is not None:
        _u = parsed.get("usage") or {}
        if not ((_u.get("input_tokens") or 0) + (_u.get("output_tokens") or 0)):
            reason = ("result object carries ZERO tokens — the CLI synthesizes a zeroed "
                      "result on some paths; unpriceable, not free")
            parsed = None

    rec = {"label": label, "wall_s": round(wall_s, 1), "attributed": parsed is not None}
    if parsed is not None:
        rec.update({k: parsed.get(k) for k in
                    ("total_cost_usd", "num_turns", "duration_api_ms", "duration_ms",
                     "session_id", "subtype", "is_error")})
        rec["usage"] = parsed.get("usage") or {}
        rec["model_usage"] = parsed.get("modelUsage") or {}
    else:
        rec["reason"] = reason
        rec["raw_chars"] = raw_len
    _usage_log.append(rec)
    if parsed is None:
        msg = (f"  ⚠ {label}: usage NOT attributable ({reason}). Spend for this call is "
               f"unknown — an economics result computed over it would be wrong.")
        if os.environ.get("CLAUDE_USAGE_STRICT") == "1":
            raise UsageUnattributable(msg.strip())
        print(msg)
    else:
        u = rec["usage"]
        print(f"    usage: in={u.get('input_tokens', 0)} out={u.get('output_tokens', 0)} "
              f"cache_read={u.get('cache_read_input_tokens', 0)} "
              f"cost=${rec.get('total_cost_usd') or 0:.4f} turns={rec.get('num_turns')}")
    return rec


# Variables that must NEVER reach the escalated Claude process. It runs under
# bypassPermissions and can invoke the pipeline itself: observed in routecon3, where the
# child inherited BENCH_META, ESCALATE_ON_RULE and BUILD_METRICS, emitted a second benchmark
# row as project ".", escalated RECURSIVELY, and spent $0.9476 attributable to no cell. For
# an economics experiment that is a treatment-arm cost understatement, not a curiosity.
_BENCH_ONLY = ("BENCH_META", "BUILD_METRICS", "ESCALATE_ON_RULE", "ESCALATE_AFTER",
               "ESCALATE_MID_AFTER", "CAPABILITY_SHADOW_LOG")

# Positive sentinel, not just absence. A child that still finds a way to run the pipeline
# must be unable to act as a benchmark: no metrics row, no escalation of its own.
NO_BENCH = "PIPELINE_NO_BENCH"


def _child_env():
    env = {k: v for k, v in os.environ.items() if k not in _BENCH_ONLY}
    env[NO_BENCH] = "1"
    return env


def _raw(cwd, prompt, claude_bin, label, timeout):
    """Run `claude -p` in cwd, capture and return its output text ("" on timeout).

    Runs in JSON output mode so the call can be PRICED, and returns the `result` text so
    the contract with every caller is unchanged.
    """
    cmd = [claude_bin, "-p", prompt, "--permission-mode", "bypassPermissions",
           "--output-format", "json"]
    start = time.time()
    try:
        # stdin=/dev/null for the same reason run_pi pins it: an agent CLI that inherits a
        # still-open descriptor with no data and no EOF can park in its event loop before
        # issuing any request. Measured on pi; pinned here too rather than waiting to find
        # out whether this CLI shares the behaviour.
        r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=timeout,
                           env=_child_env(), stdin=subprocess.DEVNULL)
    except subprocess.TimeoutExpired:
        print(f"  {label} TIMEOUT after {timeout}s")
        # A timeout is a real call that may well have been billed. Recorded as
        # unattributable rather than dropped, so it cannot silently vanish from a total.
        _record(label, time.time() - start, None, 0, reason="timeout")
        return ""
    wall = time.time() - start
    stdout, stderr = (r.stdout or "").strip(), (r.stderr or "").strip()
    print(f"  {label} done in {wall:.0f}s (exit {r.returncode})")

    parsed = None
    try:
        obj = json.loads(stdout)
        if isinstance(obj, dict) and obj.get("type") == "result":
            parsed = obj
    except ValueError:
        pass

    if parsed is None:
        # Fall back to the pre-JSON behaviour so a schema change degrades the ACCOUNTING,
        # never the build.
        _record(label, wall, None, len(stdout),
                reason="stdout is not a --output-format json result object")
        return (stdout + ("\n" + stderr if stderr else "")).strip()

    _record(label, wall, parsed, len(stdout))
    text = parsed.get("result") or ""
    return (text + ("\n" + stderr if stderr else "")).strip()


def run_claude(project_root, prompt, claude_bin, label="Claude", timeout=None):
    """Policy-routed Claude Code invocation. See module docstring."""
    if not os.path.exists(claude_bin):
        print(f"  ⛔ {label}: claude not found at {claude_bin}")
        return ""
    pol = egress_policy.policy()
    if pol != "enterprise-anon":
        ok, reason = egress_policy.allowed("anthropic")
        if not ok:
            print(f"  ⛔ Claude call BLOCKED ({label}) — {reason}")
            return ""
        print(f"  Running Claude Code ({label})...")
        return _raw(project_root, prompt, claude_bin, label, timeout)

    # Only TRACKED files are mirrored (see the caveat in the module docstring). In an
    # interactive repo a human commits between calls, so that holds. An AUTONOMOUS
    # multi-round run has no such step: round 1's patch lands untracked, and round 2's
    # mirror is built from the seed alone — the model is handed back a workspace missing
    # the code it just wrote, and the run measures "cannot repair" when the truth is
    # "cannot see". Measured directly: round 2's mirror contained no src/ at all.
    #
    # Opt-in, because committing on a user's behalf in a real work repo is not this
    # module's business. The bench harness sets it for its throwaway per-run repos.
    if os.environ.get("ANON_AUTOCOMMIT") == "1":
        # Assert the top-level IS this project root before touching the index. Without it a
        # damaged run-dir .git makes git discover an ANCESTOR repo and this commits there:
        # routecon4/map/r4 committed six benchmark artifacts into the setup repository.
        _top = subprocess.run(["git", "rev-parse", "--show-toplevel"], cwd=project_root,
                              capture_output=True, text=True)
        if (_top.returncode != 0
                or os.path.realpath(_top.stdout.strip()) != os.path.realpath(project_root)):
            print(f"  ⛔ {label}: ANON_AUTOCOMMIT REFUSED — git top-level is "
                  f"{_top.stdout.strip()!r}, not {project_root!r}. Refusing to commit to an "
                  f"ancestor repository; the run directory's .git is missing or damaged.")
            return ""
        try:
            subprocess.run(["git", "add", "-A"], cwd=project_root, check=True,
                           capture_output=True)
            subprocess.run(["git", "commit", "-q", "-m", f"pipeline state before {label}"],
                           cwd=project_root, check=False, capture_output=True,
                           env={**os.environ, "GIT_AUTHOR_NAME": "pipeline",
                                "GIT_AUTHOR_EMAIL": "pipeline@local",
                                "GIT_COMMITTER_NAME": "pipeline",
                                "GIT_COMMITTER_EMAIL": "pipeline@local"})
        except (OSError, subprocess.CalledProcessError) as e:
            print(f"  ⚠ {label}: ANON_AUTOCOMMIT failed ({e}) — the mirror may be stale")

    # enterprise-anon: this function IS the anon hook — arm the gate flag for the
    # duration of the mirror run, never for raw execution.
    with egress_policy.anon_scrub_active():
        ok, reason = egress_policy.allowed("anthropic")
        if not ok:   # defensive — should not happen once armed
            print(f"  ⛔ Claude call BLOCKED ({label}) — {reason}")
            return ""
        print(f"  Running Claude Code ({label}) in scrubbed mirror (enterprise-anon)...")
        captured = {"text": ""}

        def coder(mirror, p):
            captured["text"] = _raw(mirror, p, claude_bin, label, timeout)

        try:
            res = anon_workspace.run_workspace(project_root, prompt, coder)
        except anon_workspace.SecretAbort as e:
            print(f"  ⛔ {label} ABORT — {e}. Remove the secret before escalating.")
            return ""
        except anon_workspace.SymlinkAbort as e:
            # Fail closed, same as a secret: following a tracked link can copy an
            # out-of-repo file into the scrubbed mirror.
            print(f"  ⛔ {label} ABORT — {e}. Replace the link with a real file, or "
                  f"untrack it, before escalating.")
            return ""
        except RuntimeError as e:
            print(f"  ⛔ {label} mirror failed — {e} (enterprise-anon needs a git repo "
                  f"with the sources committed)")
            return ""
        if res.get("scrubbed", 0) == 0:
            print(f"  ⚠ {label}: mirror was EMPTY — no tracked text files. Commit the "
                  f"project sources so the mirror sees them.")
        if res.get("changed"):
            if res["applied"]:
                print(f"  ✔ {label} patch applied (scrubbed {res['scrubbed']} files; "
                      f"patch: {res['patch']})")
            else:
                print(f"  ⚠ {label} patch did NOT apply cleanly — .rej written; review "
                      f"{res['patch']}: {res['apply_err']}")
        return captured["text"]
