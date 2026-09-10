#!/usr/bin/env python3
"""
Larry build orchestrator — Pi agent harness (pi.dev), local, no LibreChat/auth.

Flow:
  1. Clear project, Larry (Pi) writes files from the handover
  2. Cleanup unspecced files
  3. Per round: manifest check + canonical app.json + using-normalize + al compile
  4. Compiler/manifest = ground truth. Errors -> Larry (Pi) fixes -> recompile
  5. Keep-best / no-regress guard across up to MAX_FIX_ROUNDS

Usage:
  python3 run-build.py                      # default project
  python3 run-build.py --project <root>     # target a project
  python3 run-build.py --skip-larry         # skip write step (fix existing files)
  python3 run-build.py --review-only        # skip write + cleanup, just compile loop

Model: env PI_CODER_MODEL (default ollama/qwen3-coder:30b). AL rules live in the
project's AGENTS.md (auto-loaded by Pi) + the handover. Expected files come from
the handover's 'machine-readable manifest' block.
"""

import sys
import json
import os
import re
import glob
import time
import signal
import subprocess

import al_brain       # AL-14: compact deterministic project profile
import al_testgen     # AL-10: targeted test selection via the object graph
import al_errors      # AL-12: evidence-linked guidance for recurring diagnostics
import al_upgrade     # AL-7: breaking-change analysis against a baseline .app
import al_profiles    # AL-11: destination policy as data (al-profiles.yml)
import al_probe       # AL-2: settle an uncertain construct by compiling it in a throwaway project
import al_tests       # AL test execution in the referee (AL_RUN_TESTS=1, fails closed)
import al_semantics   # deterministic legal-but-risky AL patterns (warnings only)
import event_verify   # pre-compile subscriber verification against real symbols
import al_context     # BC/runtime/target facts, resolved deterministically
import build_receipt  # promote-time proof that this tree passed the referee
import result_bundle  # durable per-round record; OFF unless RESULT_BUNDLE_DIR is set
import fixture_provenance  # ties a result to the fixture revision that produced it
import pathguard      # containment for model/handover-supplied paths
import egress_policy   # deny-by-default Anthropic egress gate (anon hook §0)
import claude_egress   # policy-routed Claude execution (anon hook §5 — mirror under enterprise-anon)
import coder         # shared pi spawn: one implementation, three pipelines
import bonsai_vram   # Mode B GPU time-share: evict the Bonsai chat server before loading the coder

AL_CLI       = (os.environ.get("AL_CLI") or __import__("shutil").which("al")
                or os.path.expanduser("~/.dotnet/tools/al"))  # upstream hardcodes a dev-box path
AL_MCP_URL   = "http://127.0.0.1:5001/"   # al-mcp server (al_downloadsymbols — global, server-free)

# Coder backend: "pi" (local ollama, free) or "claude" (Claude Code, Pro sub quota)
CODER_BACKEND = os.environ.get("CODER_BACKEND", "pi")

# Pi agent harness (pi.dev) — local, replaces the LibreChat agent layer.
PI_BIN      = os.environ.get("PI_BIN") or __import__("shutil").which("pi") or os.path.expanduser("~/.npm-global/bin/pi")
PI_EXT      = os.path.expanduser("~/.pi/ollama-provider.ts")  # registers ollama provider
CODER_MODEL = os.environ.get("PI_CODER_MODEL", "ollama/qwen3-coder:30b")

# --- reviewer independence (security review T7) -----------------------------------
# The reviewer used to default to CODER_MODEL, so "independent model review" could be
# the coder grading its own work — while coms_review.py's docstring advertised a
# DIVERSE default. Default to a different model, and never CLAIM independence when the
# two match: report it and let the gate refuse.
REVIEW_MODEL_DEFAULT = os.environ.get("REVIEW_MODEL_DEFAULT", "ollama/qwen2.5-coder:14b")
REVIEW_INDEPENDENT = os.environ.get("REVIEW_INDEPENDENT", "1") != "0"
# review-required vs review-optional (security review T9). Optional keeps today's
# advisory fail-open behaviour; required makes an unavailable reviewer, a failed
# reviewer, or missing BCQuality rules FAIL the build rather than pass silently.
REVIEW_REQUIRED = os.environ.get("REVIEW_REQUIRED") == "1"


def _same_model(a, b):
    """Model identity for independence purposes. Compares the bare model name, so
    ollama/qwen3-coder:30b and qwen3-coder:30b are recognised as the same thing."""
    norm = lambda m: (m or "").split("/")[-1].strip().lower()
    return norm(a) == norm(b)

# Pre-warm: load the coder model before the write phase so a slow ROCm cold-load doesn't
# eat the write timeout (ornith:35b failure mode). Hits the same ollama endpoint the pi
# provider uses (nginx HTTPS proxy). keep_alive keeps it resident across the build.
OLLAMA_WARM_URL    = os.environ.get("OLLAMA_WARM_URL", "https://larry.home.arpa:11443/v1/chat/completions")
PREWARM_KEEP_ALIVE = os.environ.get("PREWARM_KEEP_ALIVE", "2h")
PREWARM_TIMEOUT    = int(os.environ.get("PREWARM_TIMEOUT", "480"))

# Claude Code (first-party) — uses Pro/Max subscription quota (auth via `claude` /login).
CLAUDE_BIN  = os.environ.get("CLAUDE_BIN") or __import__("shutil").which("claude") or os.path.expanduser("~/.local/bin/claude")

# Mid tier — a cheap-cloud rung between Larry (free) and Claude (Opus), reached via
# an OpenRouter pi provider. Egress-gated by egress_policy.allowed("openrouter"):
# only 'personal'/'cloud-mid' repos may use it, so customer AL (local-only) never does.
# See war-plans/mid-tier-routing/.
MID_EXT     = os.path.expanduser(os.environ.get("MID_EXT", "~/.pi/openrouter-provider.ts"))
MID_MODEL   = os.environ.get("MID_MODEL", "openrouter/deepseek/deepseek-chat")

DEFAULT_PROJECT = "/mnt/rojaws/localDev/projects/tsg-map-integration"

MAX_WRITE_ATTEMPTS = 3
MAX_FIX_ROUNDS     = int(os.environ.get("MAX_FIX_ROUNDS", "8"))   # doclink-class needs more; env-tunable

# Fix strategy for the LOCAL coder: "rewrite" (default — model rewrites whole files) or
# Fix strategy per round (pi backend only; Claude always gets the full fix message):
#   "auto"    (default) — route by error CLASS, from suite4 2026-07-31 evidence: a file
#             dominated by parser errors (missing until/end/brace) gets a targeted
#             SINGLE-FILE rewrite (snippet cannot restructure, whole-project rewrite
#             regresses the other files); otherwise semantic errors get snippet edits.
#   "snippet" — always SEARCH/REPLACE Fast-Apply (see snippet_fix.py)
#   "rewrite" — always the full-project fix message (pre-suite4 behaviour)
FIX_STRATEGY = os.environ.get("FIX_STRATEGY", "auto")
# Recover dropped manifest files with a focused "write just these" step (default on).
RECOVER_MISSING = os.environ.get("RECOVER_MISSING", "1") != "0"
# Verbatim write (default off): for Strategy-A handovers where every manifest file has a
# complete fenced code block, write files DIRECTLY from those blocks — no coder in the write
# phase. Deterministic + faithful: eliminates the write-step drift where a coder paraphrases
# or invents at scale (the failure that whole-project clear+regenerate hits past ~20 files).
# The coder is still available for fix rounds if a verbatim block has a genuine compile bug.
VERBATIM_WRITE = os.environ.get("VERBATIM_WRITE", "0") == "1"
# Focused-recovery attempts before falling through to the general fix.
MAX_RECOVERY_ROUNDS = int(os.environ.get("MAX_RECOVERY_ROUNDS", "2"))
# Optional pre-generation planning chain (analyse -> objects -> symbols). Default off.
WORKFLOW = os.environ.get("WORKFLOW", "single")   # "single" | "decomposed" | "incremental"
# Ground fix rounds in the indexed BC source. The measured failure mode on the hard
# fixture was pure API hallucination — a codeunit declared as Record, an invented
# property, a procedure that doesn't exist — i.e. missing FACTS, not bad reasoning.
# Those facts are all in the local KB, so look up the exact identifiers the compiler
# says are unresolved and hand the model their real declarations. Default off (A/B).
RAG_INJECT = os.environ.get("RAG_INJECT", "1") == "1"
# Default ON since 2026-07-31 (suite4): with it off, 2/3 control doclink runs died at 1-2
# remaining errors that were ALL invented members (AL0132) — the exact class this grounds.
# Costs nothing when those errors don't occur (only fires on unresolved names/members).
# BC objects are spread across corpora (System App, Business Foundation, W1 apps),
# so try them in order. NB the Base Application is not indexed, so its objects
# (e.g. the "Document Attachment" table) will legitimately not resolve.
RAG_CORPORA = [c for c in os.environ.get(
    "RAG_CORPUS", "bcapps-system,bcapps-foundation,alae-w1").split(",") if c.strip()]
RAG_HITS = int(os.environ.get("RAG_HITS", "2"))
# The kb fallback is OFF by default: `kb search` embeds its query on Larry, which loads
# mxbai-embed-large (~0.6GB) alongside the coder. qwen3-coder:30b alone takes 21.7GB of
# the 24GB card, so the embedder pushes it to ~93% and leaves nothing for KV cache — the
# write phase then thrashed into a 1200s timeout. Symbol lookup costs no GPU at all, so
# it is the default path; enable this only when the coder is not resident.
RAG_KB_FALLBACK = os.environ.get("RAG_KB_FALLBACK", "0") == "1"
# Inject AL-REFERENCE topic files straight into the write prompt. Measured 2026-07-29:
# ~76% of diagnostics are AL rules/semantics (syntax, TryFunction signatures, attribute
# syntax, event constraints), not unresolved names — and P1, the easy fixture, is 73
# al-rule errors with ZERO name errors. The handover TELLS the coder to read these topics
# but nothing verifies it does. Since the 2026-07-27 split they finally fit in a 32k
# context, so we can simply put them in front of it. Comma-separated topic filenames.
# reference/ lives beside pipeline/ in the setup repo
REPO_REFERENCE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "reference")
# "auto" (default) picks topics from what the project actually declares; a comma-separated
# list overrides; "off"/"" disables. Measured 2026-07-29: injection took the suite from
# 5/10 to 9/12 passes, so it is on by default.
INJECT_TOPICS = os.environ.get("INJECT_TOPICS", "auto").strip()
# Topic budget in tokens — a CEILING, not an allowance. The real limit is ctx_budget_k()
# below, minus whatever the rest of the prompt already costs; select_topics is handed the
# smaller of the two. Before 2026-08-30 these were two independent budgets and the second
# silently undid the first: doclink at INJECT_BUDGET_K=16 selected five topics (15.0k) and
# ctx-guard deleted the fifth again before the model saw it, so a budget-14-vs-16 A/B ran
# the same configuration in both arms and returned U=50.0 of 100 — a thing compared to
# itself, read at the time as a null. With ~8.0k of handover+BCQuality+API grounding, 14k
# of topics was never once reachable.
INJECT_BUDGET_K = float(os.environ.get("INJECT_BUDGET_K", "14"))
# The coder re-emits every file, so the prompt must leave room for its own output plus tool
# traffic. Overflow mid-tool-loop is the pi stream-wedge signature.
CODER_NUM_CTX = int(os.environ.get("CODER_NUM_CTX", "32768"))
CTX_OUTPUT_RESERVE = float(os.environ.get("CTX_OUTPUT_RESERVE", "0.40"))


def ctx_budget_k():
    """Token ceiling for the whole write prompt. Claude Code has 200k, so the guard is
    irrelevant there and must not shrink its injection."""
    if CODER_BACKEND != "pi":
        return float("inf")
    return CODER_NUM_CTX / 1000.0 * (1.0 - CTX_OUTPUT_RESERVE)
KB_BIN = (os.environ.get("KB_BIN") or __import__("shutil").which("kb")
          or os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                          "tooling", "kb"))

# Per-build metrics: one JSON line appended per run, fuel for the model leaderboard
# (build_leaderboard.py). Pure instrumentation — never break a build on a metrics error.
METRICS_LOG = os.environ.get(
    "BUILD_METRICS", os.path.join(os.path.dirname(os.path.abspath(__file__)), ".build-metrics.jsonl"))


# Set by claude_egress in the escalated child's environment. A nested pipeline run must not
# act as a benchmark: no metrics row, no escalation. It may still compile, which is the
# legitimate reason an agent would invoke the build at all.
NO_BENCH = os.environ.get("PIPELINE_NO_BENCH") == "1"


def emit_metrics(rec):
    # Grounding state rides on EVERY row, added centrally so a new emit site cannot forget
    # it. A run that lost its symbol/KB lookups must be distinguishable in the record from
    # one that needed none — otherwise the distinction survives only in a log nobody reads.
    try:
        rec = {**rec, "grounding": grounding_state(), "config": config_record()}
    except Exception:
        pass
    """Append one build's metrics as a JSON line. Fail-open.

    BENCH_META carries experiment identity a run cannot infer about itself — which
    pre-registered candidate a takeover started from, which manifest pinned it. Merged
    last so a harness can never overwrite a measured field with a label, and fail-open
    on bad JSON, because instrumentation must not break a build.
    """
    if NO_BENCH:
        print("  (metrics suppressed: PIPELINE_NO_BENCH — nested run, not a benchmark cell)")
        return
    try:
        import json as _json
        rec = {"ts": __import__("datetime").datetime.now().strftime("%Y-%m-%dT%H:%M"), **rec}
        _meta = os.environ.get("BENCH_META", "")
        if _meta:
            try:
                _m = _json.loads(_meta)
                if isinstance(_m, dict):
                    rec.update({k: v for k, v in _m.items() if k not in rec})
            except ValueError as _je:
                print(f"  (BENCH_META ignored — not valid JSON: {_je})")
        with open(METRICS_LOG, "a") as f:
            f.write(_json.dumps(rec) + "\n")
    except Exception as _e:
        print(f"  (metrics not written: {_e})")


def object_type(path):
    """AL object type from a filename (matches our .ObjectType.al naming)."""
    n = os.path.basename(path).lower()
    for suf, t in [(".tableextension.al", "TableExt"), (".tableext.al", "TableExt"),
                   (".pageextension.al", "PageExt"), (".pageext.al", "PageExt"),
                   (".enumextension.al", "EnumExt"), (".table.al", "Table"),
                   (".codeunit.al", "Codeunit"), (".page.al", "Page"), (".report.al", "Report"),
                   (".enum.al", "Enum"), (".query.al", "Query"), (".interface.al", "Interface"),
                   (".permissionset.al", "PermissionSet"), (".xmlport.al", "XmlPort"),
                   (".controladdin.al", "ControlAddin")]:
        if n.endswith(suf):
            return t
    return "Other"


def _diag_cat(code, msg):
    """Bucket one AL diagnostic into a coarse category (heuristic; refine over time)."""
    if code in {"AL0185", "AL0247", "AL0432"} or "are you missing" in msg or "does not exist" in msg:
        return "missing-symbols"
    if code in {"AL0104", "AL0107", "AL0114", "AL0128", "AL0198", "AL0227", "AL0519", "AL0009"}:
        return "syntax"
    if code in {"AL0133", "AL0139", "AL0161", "AL0257"} or "cannot be converted" in msg:
        return "type-mismatch"
    if code in {"AL0132", "AL0280", "AL0282"} or "does not contain a definition" in msg \
            or "no overload" in msg or "event" in msg:
        return "missing-method-event"
    if code in {"AL0205", "AL0234"} or "namespace" in msg:
        return "naming-namespace"
    return "other"


def classify_diagnostics(text):
    """Count AL compile diagnostics by category → {category: n} (regex fallback)."""
    import collections
    cats = collections.Counter()
    for m in re.finditer(r"error (AL\d+):\s*(.*)", text or ""):
        cats[_diag_cat(m.group(1), m.group(2).lower())] += 1
    return dict(cats)


_sym_idx = None      # lazily built symbol index (see _symbol_index)
AL_CTX = {}          # BC/runtime/target context for this project (al_context)
_event_findings = [] # AL-4 pre-compile subscriber findings for the current compile
_sem_summary = {}    # AL-6 semantic findings, counted by rule, for metrics
_diag_codes = []     # AL-12 diagnostic codes in the best round
_first_pass_codes = []   # ... and in the first pass, before any repair
AL_RUN_TESTS = os.environ.get("AL_RUN_TESTS") == "1"
AL_PROBE = os.environ.get("AL_PROBE", "1") != "0"   # AL-2 compiler probes
AL_PROFILE = {"name": "internal"}   # AL-11 deployment profile (set in configure_project)
AL_UPGRADE_BASELINE = os.environ.get("AL_UPGRADE_BASELINE", "")  # AL-7 previous .app
_upgrade_result = {}
AL_PROBE_BUDGET = int(os.environ.get("AL_PROBE_BUDGET", "2"))  # probes per fix round
# AL-14 project profile in the coder prompt. OFF by default and deliberately so:
# it adds ~500 chars to every prompt, and a previous injection-budget change
# silently evicted a knowledge topic and took the benchmark control set from
# 2/3 to 0/3. Enable per-run, measure, then decide.
AL_BRAIN = os.environ.get("AL_BRAIN") == "1"
_test_result = {"status": "disabled", "ok": True}

# Structured diagnostics from the AL compiler's SARIF (/errorlog) — precise code /
# severity / file / line, better than parsing stdout. Populated by run_al_compile().
_last_diags = []


def parse_sarif(path):
    """Parse alc /errorlog SARIF (v0.2) → [{code, severity, uri, line, message}]."""
    try:
        d = json.load(open(path))
    except FileNotFoundError:
        return []                    # no /errorlog written — regex fallback is expected
    except Exception as e:
        print(f"  (SARIF unreadable: {e} — falling back to regex diagnostics)")
        return []
    out = []
    for it in d.get("issues", []):
        loc = (it.get("locations") or [{}])[0]
        tgt = loc.get("analysisTarget") or loc.get("resultFile") or [{}]
        tgt = tgt[0] if isinstance(tgt, list) else tgt
        reg = tgt.get("region", {}) if isinstance(tgt, dict) else {}
        props = it.get("properties", {}) or {}
        out.append({
            "code": it.get("ruleId", ""),
            "severity": props.get("defaultSeverity") or props.get("severity") or "Error",
            "uri": tgt.get("uri", "") if isinstance(tgt, dict) else "",
            "line": reg.get("startLine"),
            "message": it.get("fullMessage") or it.get("shortMessage") or "",
        })
    return out


def _is_error(d):
    return str(d.get("severity", "")).lower().startswith("error")


def classify_diags(issues):
    """Bucket structured diagnostics (errors only) by category → {category: n}."""
    import collections
    cats = collections.Counter()
    for i in issues:
        if _is_error(i):
            cats[_diag_cat(i.get("code", ""), (i.get("message", "") or "").lower())] += 1
    return dict(cats)

# Escalation: when the coder is pi (free/local) and the build still fails after
# ESCALATE_AFTER fix rounds, hand the REMAINING rounds to Claude Code to close.
# OFF by default (manual) so Claude quota is never spent unless you opt in:
#   ESCALATE_AFTER unset / non-number  -> manual, pi only, no auto Claude spend
#   ESCALATE_AFTER=4                    -> pi does rounds 0..3, then latch to Claude
# Ignored when CODER_BACKEND=claude (already Claude). One-way latch (no flapping).
_esc = os.environ.get("ESCALATE_AFTER", "").strip()
ESCALATE_AFTER = int(_esc) if _esc.isdigit() else None

# Arm C of the routing-economics experiment: escalate when the FROZEN capability rule fires,
# instead of at a fixed round. OFF by default — with it off, capability_shadow observes and
# nothing else, exactly as before.
ESCALATE_ON_RULE = os.environ.get("ESCALATE_ON_RULE") == "1"
if os.environ.get("PIPELINE_NO_BENCH") == "1":
    # Belt and braces: claude_egress already strips the escalation variables, but a nested
    # run must not escalate even if one survives by another route.
    ESCALATE_AFTER = None
    ESCALATE_ON_RULE = False

# Mid-tier ladder: pi does rounds 0..M-1, then the cheap-cloud MID rung closes
# rounds M..N-1, then Claude closes N+. Both latches one-way. Requires M < N.
# Unset ESCALATE_MID_AFTER -> no mid rung (today's binary pi->claude behaviour).
_escm = os.environ.get("ESCALATE_MID_AFTER", "").strip()
ESCALATE_MID_AFTER = int(_escm) if _escm.isdigit() else None

# Active coder backend — starts at CODER_BACKEND, may latch pi->mid->claude on escalation.
# SIGTERM must run the atexit handlers, or a killed build keeps the GPU.
#
# `timeout` sends SIGTERM, and Python does NOT run atexit on a signal-induced death — it
# dies in the C handler. Every build here is wrapped in `timeout`, and bench-run-suite.sh
# wraps each run in `timeout 3600`, so ANY run that hit its cap skipped bonsai restore and
# left the chat server down. The restore was being skipped exactly when a build had gone
# wrong, which is the worst possible time for it: observed 2026-09-01, bonsai stopped clean
# at 09:58 and stayed down.
#
# Raising SystemExit from the handler resumes normal interpreter shutdown, so atexit runs.
# 143 = 128 + SIGTERM, the conventional code, so callers still see it as a signal death.
# SIGINT already does this — Python raises KeyboardInterrupt — so SIGTERM was the only gap.
# SIGKILL cannot be caught and still orphans the card; that boundary is unchanged.
def _exit_on_sigterm(_signum, _frame):
    raise SystemExit(143)


signal.signal(signal.SIGTERM, _exit_on_sigterm)

_coder_state = {"backend": os.environ.get("CODER_BACKEND", "pi")}
# Grounding availability, recorded rather than inferred. "" conflated two states — nothing
# needed grounding, and the grounding tool was absent — and those must never be
# observationally identical. A build that silently lost its symbol/KB lookups looked exactly
# like one that needed none: the same defect class as a silent topic eviction.
_grounding = {"status": "not_attempted", "reason": None, "hits": 0}


# ── Run configuration: DECLARED vs OBSERVED ───────────────────────────────────
# Generalises bench-run-suite.sh's assert_arm() from the escalation rungs to the whole
# run, and moves it into the run artifact so a dashboard-triggered build is verified too,
# not only a bench arm.
#
# The distinction is the point. `injab` declared budget-14 vs budget-16 arms, passed
# arm-isolation, and both arms ran the IDENTICAL configuration because ctx-guard trimmed
# the challenger's extra topic after selection. Mann-Whitney returned U=50.0 of 100 — a
# thing compared with itself, read at the time as a clean null. A declared treatment is
# not evidence the treatment landed.
#
# OBSERVED must come from what the process DID, never from re-reading the environment we
# believe we passed. Re-reading env would have reproduced injab's failure exactly.
_config = {"declared": {}, "observed": {}}


def declare_config(**kv):
    """What this run was ASKED to do."""
    _config["declared"].update({k: v for k, v in kv.items() if v is not None})


def observe_config(**kv):
    """What the run ACTUALLY did. Called from the code paths that do it."""
    _config["observed"].update({k: v for k, v in kv.items() if v is not None})


def config_verification():
    """Compare the two. Returns (verdict, mismatches) — verdict is verified | mismatch |
    unverified (nothing comparable observed yet)."""
    d, o = _config["declared"], _config["observed"]
    bad = []
    # An explicit topic list must arrive intact. This is the injab check: selection asked
    # for a set, and something downstream may have trimmed it.
    dt, ot = d.get("inject_topics"), o.get("topics_injected")
    if dt and dt not in ("auto", "off", "none", "0") and ot is not None:
        want = [t.strip() for t in dt.split(",") if t.strip()]
        if want != ot:
            bad.append(f"inject_topics declared {want} but injected {ot}")
    # A round cap is a ceiling, never a floor.
    dr, orr = d.get("max_fix_rounds"), o.get("max_round_reached")
    if dr is not None and orr is not None and orr > dr:
        bad.append(f"max_fix_rounds declared {dr} but reached round {orr}")
    # The coder that ran must be the coder that was asked for, unless escalation was armed
    # AND actually fired — an unarmed run that changed backend is a void measurement.
    db, ob = d.get("backend"), o.get("backend_final")
    if db and ob and db != ob and not d.get("escalate_after") and not d.get("escalate_mid_after"):
        bad.append(f"backend declared {db} but ran {ob} with no escalation armed")
    dm, om = d.get("model"), o.get("model_used")
    if dm and om and dm != om:
        bad.append(f"model declared {dm} but used {om}")
    if bad:
        return "mismatch", bad
    return ("verified" if o else "unverified"), []


def config_record():
    verdict, bad = config_verification()
    return {"verdict": verdict, "mismatches": bad,
            "declared": dict(_config["declared"]), "observed": dict(_config["observed"])}


def grounding_state():
    """Run-level observable: applied | available_no_matches | unavailable | not_attempted."""
    return dict(_grounding)


# Precedence, highest first. A run-level attribute must not be downgraded by a later,
# less informative call: grounding that was UNAVAILABLE at round 1 stays unavailable even if
# round 5 simply had nothing to look up, and a run that APPLIED grounding does not later
# report "no matches". Without this, the most alarming state is the easiest to lose — the
# first call sets it and any subsequent quiet round overwrites it.
_GROUNDING_RANK = {"unavailable": 3, "applied": 2, "available_no_matches": 1,
                   "not_attempted": 0}


def _note_grounding(status, reason=None, hits=0):
    _grounding["hits"] += hits
    if _GROUNDING_RANK[status] < _GROUNDING_RANK[_grounding["status"]]:
        return                              # never downgrade
    _grounding.update(status=status, reason=reason)
    if status == "unavailable":
        print(f"  ⚠ grounding UNAVAILABLE ({reason}) — this build ran WITHOUT symbol/KB "
              f"lookups. That is NOT the same as 'nothing needed grounding'.")
# Did the last coder call end on its timeout rather than by finishing? run_pi returns ""
# for both, and the write loop needs to tell them apart: a coder that produced nothing
# because it hung is not the same failure as one that returned quickly with nothing.
# Consecutive fix rounds whose coder call hit its full timeout. Incremented by run_pi so it
# counts the call that actually stalled, not a round that merely produced no edits.

# Per-project paths — set by configure_project() from --project (default: map).
PROJECT_ROOT   = DEFAULT_PROJECT
HANDOVER       = PROJECT_ROOT + "/larry-handover.prompt.md"
CLEANUP        = PROJECT_ROOT + "/cleanup.sh"
EXPECTED_FILES = []


# Windows fix: accept BOTH POSIX ("/mnt/...") and drive-letter ("C:/Users/...")
# absolute paths. Upstream only accepted a leading "/", which on this box was a
# catch-22: "C:/..." parsed to [] (hard abort below), while "/c/..." parsed but
# then failed every os.path.exists() in the write gate. normpath() also aligns
# separators with the os.walk() output used by the unspecced-file audit.
_MANIFEST_ABS = re.compile(r"^(?:[A-Za-z]:[\\/]|[\\/])")


def parse_manifest(handover_path):
    """Extract absolute file paths from the handover's final fenced block
    under the 'machine-readable manifest' heading."""
    with open(handover_path) as f:
        text = f.read()
    idx = text.lower().rfind("machine-readable manifest")
    if idx == -1:
        return []
    block = re.search(r"```[^\n]*\n(.*?)```", text[idx:], re.DOTALL)
    if not block:
        return []
    # Manifest paths are legitimately ABSOLUTE (human-authored, e.g.
    # /mnt/rojaws/.../src/X.al), so safe_join — which rejects absolutes — is the wrong
    # guard here. What must hold is that every declared file lands inside the project
    # being built: a manifest naming /etc/passwd or a sibling repo would otherwise have
    # the write gate create/overwrite it. Containment is checked on the realpath, so a
    # symlink pointing out is caught too.
    out, rejected = [], []
    for ln in block.group(1).splitlines():
        ln = ln.strip()
        if not _MANIFEST_ABS.match(ln):
            continue
        norm = os.path.normpath(ln)
        if pathguard.contains(PROJECT_ROOT, norm):
            out.append(norm)
        else:
            rejected.append(norm)
    if rejected:
        print(f"  ⛔ manifest: {len(rejected)} path(s) outside the project root — IGNORED:")
        for r in rejected[:5]:
            print(f"       {r}")
    return out


def parse_verbatim_blocks(text):
    """Map {normalized abs path -> file content} from a Strategy-A handover.

    Each file section is a `Path: `<abs>`` line followed by the first fenced code block
    that belongs to it (the fence must come before the next `Path:` line). Entries whose
    Path line is NOT followed by a fence before the next Path (e.g. app.json, which the
    canonical writer handles) are skipped. Deterministic — no model involved."""
    blocks = {}
    for m in re.finditer(r"Path:\s*`([^`]+)`", text):
        path = os.path.normpath(m.group(1).strip())
        rest = text[m.end():]
        fence = re.search(r"```[^\n]*\n(.*?)\n```", rest, re.DOTALL)
        if not fence:
            continue
        nxt = re.search(r"Path:\s*`", rest)
        if nxt and fence.start() > nxt.start():
            continue  # this entry has no verbatim block of its own (e.g. app.json)
        blocks[path] = fence.group(1)
    return blocks


def verbatim_write():
    """Write manifest files directly from the handover's fenced blocks. Returns the
    count written. Files without a block (e.g. app.json) are left to the canonical
    writer / fix loop."""
    handover_text = read_handover()
    blocks = parse_verbatim_blocks(handover_text)
    written = 0
    for f in EXPECTED_FILES:
        key = os.path.normpath(f)
        if key not in blocks:
            continue
        content = blocks[key]
        if not content.endswith("\n"):
            content += "\n"
        os.makedirs(os.path.dirname(key), exist_ok=True)
        with open(key, "w") as fh:
            fh.write(content)
        written += 1
    return written, len(blocks)


def to_native_path(p):
    """Windows fix: Git Bash hands us '/c/Users/...', which Windows Python cannot
    open() or stat(). Rewrite a leading '/<drive>/' to '<DRIVE>:/'. No-op on POSIX
    hosts and on paths that are already native."""
    m = re.match(r"^/([A-Za-z])/(.*)$", p)
    if m and os.name == "nt":
        p = f"{m.group(1).upper()}:/{m.group(2)}"
    return p


def configure_project(root):
    """Point the module-level path globals at the given project root."""
    global PROJECT_ROOT, HANDOVER, CLEANUP, EXPECTED_FILES
    PROJECT_ROOT   = to_native_path(root).rstrip("/")
    HANDOVER       = PROJECT_ROOT + "/larry-handover.prompt.md"
    CLEANUP        = PROJECT_ROOT + "/cleanup.sh"
    EXPECTED_FILES = parse_manifest(HANDOVER)
    global AL_CTX, AL_PROFILE, REQUIRED_ANALYZERS, REVIEW_REQUIRED, REVIEW_INDEPENDENT
    global AL_RUN_TESTS
    try:
        AL_PROFILE = al_profiles.resolve()
    except Exception as _e:
        # An unknown profile must stop the build. Falling back to `internal` would run
        # an AppSource submission through prototype-grade checks and report a pass.
        sys.exit(f"ERROR: {_e}")
    # The profile owns these knobs; an explicit env var still wins, so existing
    # invocations behave exactly as before.
    REQUIRED_ANALYZERS = tuple(AL_PROFILE.get("analyzers") or REQUIRED_ANALYZERS)
    _rev_req, _rev_ind = al_profiles.review_policy(AL_PROFILE)
    if "REVIEW_REQUIRED" not in os.environ:
        REVIEW_REQUIRED = _rev_req
    if "REVIEW_INDEPENDENT" not in os.environ and _rev_ind:
        REVIEW_INDEPENDENT = True
    _run_tests, _ = al_profiles.tests_policy(AL_PROFILE)
    if "AL_RUN_TESTS" not in os.environ:
        AL_RUN_TESTS = _run_tests
    try:
        AL_CTX = al_context.resolve(PROJECT_ROOT,
                                    deployment_profile=AL_PROFILE["name"])
    except Exception as _e:      # metadata must never break a build
        AL_CTX = {}
        print(f"  (AL context unavailable: {_e})")
    print(f"Project: {PROJECT_ROOT}")
    print(f"  Expected files from manifest: {len(EXPECTED_FILES)}")
    print(f"  {al_profiles.describe(AL_PROFILE)}")
    # Fail FAST on policy the coder cannot fix. Missing app.json metadata and a wrong
    # `target` are settled by reading one file, but they surface through the analyzers as
    # ordinary compile errors — so the fix loop spends rounds asking a model to repair
    # something no amount of AL will repair, and mangles the source trying. Checked here,
    # before any model call. (A project with no app.json yet is written by the build
    # itself; the post-build gate covers that case.)
    if os.path.exists(os.path.join(PROJECT_ROOT, "app.json")):
        _pre = al_profiles.check_manifest(_app_json_now(), AL_PROFILE)
        if _pre:
            print(f"\n  ⛔ PROFILE GATE ({AL_PROFILE['name']}) — this project does not "
                  f"meet the profile's metadata requirements:")
            for _r in _pre:
                print(f"     {_r}")
            print("     Nothing the coder writes can fix these — fix app.json, or build "
                  "under a different AL_PROFILE.")
            sys.exit(2)
    for _k, _v in al_profiles.unenforced(AL_PROFILE):
        print(f"  ⚠ profile declares {_k}={_v} — NOT enforced by this pipeline yet")
    if AL_CTX:
        print(f"  AL context: {al_context.summary(AL_CTX)}")
        if AL_CTX.get("version_mismatch"):
            # Not fatal, but it explains a whole class of "the model wrote bad AL"
            # reports that are really "you compiled against a different BC".
            print(f"  ⚠ VERSION MISMATCH — {AL_CTX['version_mismatch']}")
    if not EXPECTED_FILES:
        print("  WARNING: no manifest paths parsed from handover.")
    print(f"  Egress policy: {egress_policy.set_policy_for(PROJECT_ROOT)}")

def model_slug(model):
    """Bench run-dir naming: 'ollama/qwen3-coder:30b' -> 'qwen3-coder_30b'."""
    return model.split("/", 1)[-1].replace(":", "_")


def check_model_matches_rundir():
    """Bench guard: a run directory named '<model>__<project>__<workflow>__<run>'
    must actually be built by <model>. PI_CODER_MODEL is exported globally in
    ~/.config/zsh/.zshenv, so a run launched without an explicit override silently
    uses that model while the directory name claims another — which quietly
    invalidates the result AND every comparison made against it. Abort instead.
    Only fires on the bench naming convention ('__' in the dir name); ordinary
    projects are unaffected. Override with ALLOW_MODEL_MISMATCH=1."""
    if CODER_BACKEND != "pi":
        return
    name = os.path.basename(PROJECT_ROOT)
    if "__" not in name:
        return
    claimed, want = name.split("__", 1)[0], model_slug(CODER_MODEL)
    if claimed == want:
        return
    if os.environ.get("ALLOW_MODEL_MISMATCH") == "1":
        print(f"  WARNING: run dir claims '{claimed}' but coder is '{want}' "
              f"(ALLOW_MODEL_MISMATCH=1 — metrics will be mislabelled).")
        return
    print(f"\nERROR: model/run-dir mismatch — directory claims '{claimed}', "
          f"coder model is '{want}' (PI_CODER_MODEL={CODER_MODEL}).\n"
          f"       Launch with PI_CODER_MODEL=ollama/{claimed.replace('_', ':')} "
          f"(note: check the ':' placement), rename the run directory, or set "
          f"ALLOW_MODEL_MISMATCH=1 to accept mislabelled metrics.")
    sys.exit(1)


PI_TIMEOUT = 3600
# Write phase gets a shorter budget so a stalled/looping coder (e.g. a slow
# reasoning model like ornith) fails fast and retries instead of burning the
# full PI_TIMEOUT × MAX_WRITE_ATTEMPTS. Real ornith writes were <=~700s.
WRITE_TIMEOUT = int(os.environ.get("PI_WRITE_TIMEOUT", "1200"))
_CODER_CFG = coder.CoderConfig(PI_BIN, PI_EXT, ["-p", "--no-session"],
                               include_stderr=True)
# Fix rounds get their own budget. They used to inherit PI_TIMEOUT (3600s) — the same as the
# bench harness RUN_TIMEOUT, so a stalled fix call could never hit its own timeout: the outer
# cap always killed the run first and the guard was dead code. Measured over 2197 fix calls:
# median 17s, p95 56s, p99 120s, max 2128s. 600s is 5x p99 and truncates 2 calls in 2197.
FIX_TIMEOUT = int(os.environ.get("PI_FIX_TIMEOUT", "600"))
# Consecutive fix calls that burn their whole budget. MAX_FIX_ROUNDS x FIX_TIMEOUT still
# exceeds a 3600s harness cap, so bounding one call is not enough on its own: a round that
# times out having applied nothing is the fix-loop twin of a wedged write, and repeating it
# just spends the run budget arriving at the same best-so-far.
MAX_FIX_TIMEOUTS = int(os.environ.get("PI_MAX_FIX_TIMEOUTS", "2"))
# Retry the review-fix a few times (revert-on-regress), then optionally escalate
# the fix to Claude if escalation is armed (ESCALATE_AFTER set).
REVIEW_FIX_ROUNDS = int(os.environ.get("PI_REVIEW_FIX_ROUNDS", "2"))


# ---------------------------------------------------------------------------
# Pi agent harness
# ---------------------------------------------------------------------------

def run_pi(prompt, label="Pi", model=CODER_MODEL, allow_write=True, timeout=PI_TIMEOUT, ext=PI_EXT):
    """Delegates to coder.run_pi — one implementation for all three pipelines.

    Three copies of this function drifted apart and the drift cost real runs twice in
    one week (the stdin wedge, then three stall guards the AL pipeline alone had).
    The signature is unchanged so every existing call site still works."""
    observe_config(model_used=model)
    return coder.run_pi(prompt, _CODER_CFG, PROJECT_ROOT, label=label,
                        model=model, allow_write=allow_write, timeout=timeout, ext=ext)


def run_claude_code(prompt, label="Claude", timeout=PI_TIMEOUT):
    """Run Claude Code headless (one-shot). Uses the Pro/Max subscription quota
    (auth'd once via `claude` /login). Its own Read/Write/Edit/Bash tools +
    auto-loads CLAUDE.md (which imports AGENTS.md) from cwd. Same contract as
    run_pi: write/fix files in PROJECT_ROOT, return final text.

    Phase 5: routed through claude_egress — under enterprise-anon Claude runs in
    a scrubbed mirror and its diff is reverse-mapped back; local-only blocks."""
    return claude_egress.run_claude(PROJECT_ROOT, prompt, CLAUDE_BIN,
                                    label=label, timeout=timeout)


def claude_review(intent, files, knowledge_rules, timeout=PI_TIMEOUT):
    """Claude-backed behaviour review — a stronger reviewer than the local coms validator.

    Same request shape as coms_review.review (intent + code + BCQuality rule checklist)
    but runs Claude Code headless and read-only. Proves that injected rules convert to
    cited catches when the reviewer model is strong enough. Returns (findings, clean).
    """
    import coms_review
    code_block = "\n\n".join(f"=== {p} ===\n{c}" for p, c in files)
    rules_block = ""
    if knowledge_rules:
        try:
            import bcquality
            cl = bcquality.format_checklist(knowledge_rules)
        except Exception:
            cl = ""
        if cl:
            rules_block = ("\n\nCheck the code against these curated BC/AL rules. Cite the "
                           "rule path on each violation.\nRULES:\n" + cl)
    prompt = (
        "You are a senior Business Central / AL code reviewer. Review the CODE against the "
        "stated INTENT and the RULES. Report ONLY real behaviour/quality issues a compiler "
        "cannot catch — one per line as 'file:line: issue [rule: <path>]', citing a RULES "
        "path when a listed rule is violated, or [rule: agent] for a real issue no listed "
        "rule covers. Be terse; do not restate code; DO NOT edit or create any files. If the "
        "code is correct and violates no rule, reply exactly REVIEW COMPLETE."
        f"\n\nINTENT:\n{intent}\n\nCODE:\n{code_block}{rules_block}")
    out = run_claude_code(prompt, label="Claude-review", timeout=timeout)
    return coms_review._classify_findings(out)


def free_bonsai_vram():
    """Stop the Bonsai chat server if it's holding the GPU, so the coder can load.

    Delegates to bonsai_vram, which falls back to the larry-dashboard API when the
    Larry-local `bonsai` CLI is absent — i.e. on every client box, where this used to
    silently no-op. See bonsai_vram.py.
    """
    bonsai_vram.free_bonsai_vram_once()


def prewarm_coder():
    """Load the coder model (with a long keep_alive) before the write phase.

    A cold ROCm load can take minutes; without this the write phase can time out on the
    load alone. Fail-open — a failed pre-warm just means the write phase cold-loads.
    """
    if CODER_BACKEND != "pi":
        return
    free_bonsai_vram()                        # Mode B: yield GPU from the Bonsai chat server
    model = CODER_MODEL.split("/", 1)[-1]     # strip 'ollama/' provider prefix
    print(f"\n--- Pre-warming {model} (keep_alive {PREWARM_KEEP_ALIVE}) ---")
    import urllib.request, ssl
    body = json.dumps({"model": model, "messages": [{"role": "user", "content": "ok"}],
                       "max_tokens": 1, "keep_alive": PREWARM_KEEP_ALIVE}).encode()
    req = urllib.request.Request(OLLAMA_WARM_URL, data=body, headers={
        "Content-Type": "application/json", "Authorization": "Bearer ollama"})
    ctx = ssl.create_default_context()          # local self-signed CA → skip verify
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    t = time.time()
    try:
        urllib.request.urlopen(req, timeout=PREWARM_TIMEOUT, context=ctx).read()
        print(f"  warm in {time.time() - t:.0f}s")
    except Exception as e:
        print(f"  pre-warm skipped ({e}) — write phase will cold-load")


def run_mid(prompt, label="Mid", timeout=PI_TIMEOUT):
    """Run the cheap-cloud MID tier (OpenRouter via a pi provider). Gated PER CALL
    by egress_policy.allowed('openrouter') — a blocked policy (local-only /
    enterprise-anon) returns "" (a no-op round) and touches no network, so this
    can never leak customer code even if reached by an unexpected path."""
    ok, reason = egress_policy.allowed("openrouter")
    if not ok:
        print(f"  ⛔ Mid tier BLOCKED ({label}) — {reason}")
        return ""
    print(f"  Running mid tier ({label}, {MID_MODEL})...")
    return run_pi(prompt, label, model=MID_MODEL, timeout=timeout, ext=MID_EXT)


def wedged_write(written, timed_out, attempt, max_attempts=None):
    """Is this write attempt a wedge worth abandoning rather than repeating?

    A wedge is the coder burning its ENTIRE timeout and producing NOTHING: measured
    2026-08-30, pi sat at 0.4% CPU in epoll_wait, wrote no files and never exited, three
    times over, turning one bad run into 3600s. Retrying reproduces it exactly.

    Deliberately narrow. A timeout with partial output is a coder that ran and was cut off,
    which does recover on a retry; and 0 files WITHOUT a timeout is a fast transient
    failure, which is the case retries exist for. Only the pair is hopeless.
    """
    n = MAX_WRITE_ATTEMPTS if max_attempts is None else max_attempts
    return written == 0 and timed_out and attempt < n


def run_coder(prompt, label, timeout=PI_TIMEOUT):
    """Dispatch to the ACTIVE coder backend (may latch pi->mid->claude via escalation)."""
    # Cleared per call, set only by a backend that actually detects its own timeout. A
    # backend that does not report one therefore reads as "did not time out", which keeps
    # the fail-fast below conservative.
    coder.LAST["timed_out"] = False
    observe_config(backend_final=_coder_state["backend"])
    if _coder_state["backend"] == "claude":
        return run_claude_code(prompt, label, timeout=timeout)
    if _coder_state["backend"] == "mid":
        return run_mid(prompt, label, timeout=timeout)
    return run_pi(prompt, label, timeout=timeout)


# ---------------------------------------------------------------------------
# Project helpers
# ---------------------------------------------------------------------------

def get_project_file_listing():
    """Return a concise listing of current source files in the project."""
    lines = []
    for root, dirs, files in os.walk(PROJECT_ROOT):
        dirs[:] = sorted(d for d in dirs if d not in ('.alpackages', '.vscode', 'docs', '.git'))
        rel_root = os.path.relpath(root, PROJECT_ROOT)
        for f in sorted(files):
            if f.endswith(('.md', '.sh', '.gitignore', '.app', '.xlf')):
                continue
            rel = os.path.join(rel_root, f) if rel_root != '.' else f
            lines.append(f"  {rel}")
    return "\n".join(lines) if lines else "  (empty)"


def run_cleanup():
    print("\n--- Cleanup ---")
    # --apply: cleanup.sh now defaults to dry-run so a manual run can't nuke a
    # project (it once did — see CLAUDE.md). The pipeline still wants real deletes.
    # Harmless on older cleanup.sh copies, which ignore extra args.
    result = subprocess.run(["bash", CLEANUP, "--apply"], capture_output=True, text=True)
    if result.stdout.strip():
        print(result.stdout.strip())
    if result.returncode != 0:
        print("STDERR:", result.stderr.strip())


def clear_project():
    removed = 0
    for pattern in [
        PROJECT_ROOT + "/src/**/*.al",
        PROJECT_ROOT + "/src/**/*.js",
        PROJECT_ROOT + "/src/**/*.css",
        PROJECT_ROOT + "/src/**/*.html",
        PROJECT_ROOT + "/app.json",
    ]:
        for f in glob.glob(pattern, recursive=True):
            os.remove(f)
            removed += 1
    print(f"  Cleared {removed} files.")


def read_handover():
    with open(HANDOVER) as f:
        text = f.read()
    if not AL_BRAIN:
        return text
    # Facts the coder would otherwise re-derive from the tree: BC version, what objects
    # exist, what this integrates with, how well it is covered.
    try:
        ctx = al_brain.as_prompt_context(al_brain.build(PROJECT_ROOT))
        return text + "\n\nPROJECT PROFILE (deterministic, generated from this source):\n" + ctx + "\n"
    except al_brain.SecretInProfile as e:
        print(f"  ⛔ project profile refused: {e}")
    except Exception as e:
        print(f"  project profile unavailable ({e})")
    return text


# ---------------------------------------------------------------------------
# Manifest check
# ---------------------------------------------------------------------------

def run_manifest_check():
    print("\n--- Manifest check ---")
    findings = []
    actual = set()
    for root, dirs, files in os.walk(PROJECT_ROOT):
        dirs[:] = [d for d in dirs if d not in ('.alpackages', '.vscode', 'docs', '.git', '.anon', 'war-plans')]
        for f in files:
            if f.endswith(('.md', '.app', '.xlf')) or f in ('cleanup.sh', '.gitignore'):
                continue
            # normpath: os.walk() joins a forward-slash PROJECT_ROOT with a
            # backslash separator, which would never match the manifest set.
            actual.add(os.path.normpath(os.path.join(root, f)))

    expected = set(EXPECTED_FILES)
    for f in sorted(actual - expected):
        findings.append(f"HIGH: Unspecced file — {f}")
        print(f"  UNSPECCED: {f}")
    for f in sorted(expected - actual):
        findings.append(f"HIGH: Missing file — {f}")
        print(f"  MISSING: {f}")

    if findings:
        result = "MANIFEST CHECK — FAILED\n" + "\n".join(findings)
    else:
        result = "MANIFEST CHECK — PASSED"
        print("  Passed.")
    return result, bool(findings)


# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------

def _mcp_rpc(url, method, params=None, sid=None, notif=False, timeout=600):
    import urllib.request
    body = {"jsonrpc": "2.0", "method": method}
    if not notif:
        body["id"] = 1
    if params is not None:
        body["params"] = params
    req = urllib.request.Request(
        url, data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json",
                 "Accept": "application/json, text/event-stream"})
    if sid:
        req.add_header("Mcp-Session-Id", sid)
    r = urllib.request.urlopen(req, timeout=timeout)
    data = None
    for ln in r.read().decode().splitlines():
        ln = ln.strip()
        if ln.startswith("data:"):
            ln = ln[5:].strip()
        if ln.startswith("{"):
            try:
                data = json.loads(ln)
            except json.JSONDecodeError:
                pass
    return r.headers.get("Mcp-Session-Id"), data


def mcp_download_symbols():
    """Download global Microsoft symbols into PROJECT_ROOT/.alpackages.

    Spawns a *project-scoped* al-mcp server (like ALNvim does) — NOT the shared
    service. The shared service is launched with the whole workspace and resolves
    al_downloadsymbols to its first project (test10, BC27), ignoring projectPath,
    so it downloads the wrong version into the wrong folder. A scoped server makes
    the target the only/first project → correct version, symbols in its own root.
    globalSourcesOnly = Microsoft NuGet/AppSource, no server/auth. Returns the
    project's .alpackages on success, else None (caller falls back)."""
    import socket
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        port = s.getsockname()[1]
    url = f"http://127.0.0.1:{port}/"
    proc = subprocess.Popen(
        [AL_CLI, "launchmcpserver", "--transport", "http", "--port", str(port), PROJECT_ROOT],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        # wait for the scoped server to accept requests
        deadline = time.time() + 60
        sid = None
        while time.time() < deadline:
            try:
                sid, _ = _mcp_rpc(url, "initialize",
                                  {"protocolVersion": "2024-11-05", "capabilities": {},
                                   "clientInfo": {"name": "run-build", "version": "1"}},
                                  timeout=10)
                if sid:
                    break
            except Exception:
                time.sleep(2)
        if not sid:
            print("  scoped al-mcp didn't start — falling back")
            return None
        _mcp_rpc(url, "notifications/initialized", notif=True, sid=sid)
        _, res = _mcp_rpc(url, "tools/call",
                          {"name": "al_downloadsymbols",
                           "arguments": {"projectPath": PROJECT_ROOT,
                                         "globalSourcesOnly": True, "force": True}}, sid=sid)
        payload = json.loads(res["result"]["content"][0]["text"])
        data = payload.get("data", {})
        print(f"  al-mcp symbols: {payload.get('message','')} "
              f"[{data.get('source','')}] -> {data.get('cachePath','')}")
        if not payload.get("succeeded"):
            return None
        proj_cache = PROJECT_ROOT + "/.alpackages"
        return proj_cache if os.path.isdir(proj_cache) and os.listdir(proj_cache) else None
    except Exception as e:
        print(f"  scoped al-mcp download failed ({e}) — falling back")
        return None
    finally:
        proc.terminate()
        try:
            proc.wait(timeout=10)
        except Exception:
            proc.kill()


def write_canonical_app_json():
    """Write app.json deterministically from the handover's ```json block.
    The LLM must not author app.json — it mangles id/version/deps (e.g. setting
    the app id to a dependency GUID -> AL1152). Pulls the exact manifest from the
    handover's '## app.json' section and overwrites whatever Larry wrote."""
    try:
        with open(HANDOVER) as f:
            text = f.read()
        m = re.search(r'##\s*app\.json.*?```json\s*(\{.*?\})\s*```', text, re.DOTALL | re.IGNORECASE)
        if not m:
            return False
        obj = json.loads(m.group(1))
        with open(PROJECT_ROOT + "/app.json", "w") as f:
            json.dump(obj, f, indent=4)
        print(f"  app.json written deterministically (app {obj.get('application')}, runtime {obj.get('runtime')})")
        return True
    except Exception as e:
        print(f"  canonical app.json write failed: {e}")
        return False


_OBJ_RE = re.compile(
    r"^\s*(codeunit|table|tableextension|page|pageextension|pagecustomization|report|"
    r"reportextension|xmlport|query|enum|enumextension|interface|permissionset|"
    r"permissionsetextension|controladdin|profile|profileextension|entitlement)\b", re.I)


def normalize_using_directives():
    """Move any `using` line that an LLM placed INSIDE an object body up to the
    top of the file (after namespace, before the object). Every model tested
    misplaces `using` inside the `{ }`, which cascades into AL0104/AL0114/AL0107.
    This is a deterministic, safe text transform — not authoring logic."""
    fixed = 0
    for dp, _, fs in os.walk(PROJECT_ROOT + "/src"):
        for fn in fs:
            if not fn.endswith(".al"):
                continue
            p = os.path.join(dp, fn)
            lines = open(p).read().splitlines()
            ns, usings, rest = [], [], []
            for ln in lines:
                s = ln.strip()
                if s.startswith("namespace "):
                    ns.append(s)
                elif s.startswith("using "):
                    u = s if s.endswith(";") else s + ";"
                    if u not in usings:
                        usings.append(u)
                else:
                    rest.append(ln)
            # only rewrite if a using was found below the object declaration
            obj_idx = next((i for i, ln in enumerate(lines) if _OBJ_RE.match(ln)), None)
            misplaced = obj_idx is not None and any(
                lines[i].strip().startswith("using ") for i in range(obj_idx, len(lines)))
            if not misplaced:
                continue
            while rest and not rest[0].strip():
                rest.pop(0)
            out = []
            if ns:
                out.append(ns[0])
            out += usings
            if ns or usings:
                out.append("")
            out += rest
            open(p, "w").write("\n".join(out) + "\n")
            fixed += 1
    if fixed:
        print(f"  normalized using-directive placement in {fixed} file(s)")


# String-literal properties: their value is ALWAYS a single-quoted string.
# (Enum/identifier props like PageType, Image, ApplicationArea are NOT here.)
_STR_PROPS = ("Caption", "ToolTip", "InstructionalText", "AboutText", "AboutTitle",
              "OptionCaption", "RequestFilterHeading", "Tooltip")
_STRPROP_RE = re.compile(r'^(\s*)(' + '|'.join(_STR_PROPS) + r')(\s*=\s*)(.+?)(;\s*)$')
_IDENT_RE = re.compile(r'[A-Za-z_][A-Za-z0-9_]*$')


# Typed object references an AL file can make. Each needs the target's namespace in scope.
_OBJREF_RE = re.compile(
    r'\b(?:Record|Codeunit|Page|Report|Query|XmlPort|Enum|Interface|TestPage|Database)\s*'
    r'(?:::)?\s*("[^"]+"|[A-Za-z_]\w*)')

# An object HEADER references a base-app object too, and does it with no type keyword:
#     tableextension 50110 "PTE Doc Attachment Ext" extends "Document Attachment"
#     codeunit 50100 "PTE Blob Store" implements "IBlobStore", ITelemetry
# _OBJREF_RE keys off the type keyword, so it cannot see these. A file whose ONLY reference
# to a base-app object was its `extends` target therefore got no using line and failed with
# AL0247 "The target Table 'Document Attachment' for the extension object is not found" —
# which reads like a missing dependency, exactly the misdirection this function exists to
# prevent. Measured on doclink: a run declaring its own namespace without the using
# directive hit AL0247 in 5/5 runs, and 0/15 in every other namespace/using combination.
# `implements` takes a comma list, so the whole segment is captured and split.
_OBJHDR_REF_RE = re.compile(r'\b(?:extends|implements)\b([^\n{]*)', re.I)
_HDR_NAME_RE = re.compile(r'"[^"]+"|[A-Za-z_]\w*')


def _strip_noncode(lines):
    """Blank out string literals and `//` comments so a name mentioned in a Caption or a
    note is never read as an object reference.

    Factored out of add_missing_using_directives so _referenced_object_names has one
    documented input contract — the header patterns match `extends` anywhere on a line, so
    running them over un-stripped text would pick up commented-out code.
    """
    scan = "\n".join(_sub_outside_strings(l, r"$^", "") for l in lines)
    return re.sub(r"'(?:[^']|'')*'|//.*$", " ", scan, flags=re.M)


def _referenced_object_names(scan):
    """Every object name `scan` references — typed declarations AND object headers.

    `scan` MUST already be through _strip_noncode. Names only; whether one resolves to a
    namespace is the caller's business, which keeps this side of the fix conservative: an
    unresolvable name simply adds nothing.
    """
    for m in _OBJREF_RE.finditer(scan):
        yield m.group(1).strip('"')
    for m in _OBJHDR_REF_RE.finditer(scan):
        for n in _HDR_NAME_RE.findall(m.group(1)):
            yield n.strip('"')


def add_missing_using_directives():
    """Insert the `using` lines a file needs but does not have.

    BC28 moved the base application into namespaces. An unqualified `Codeunit "Temp Blob"`
    without `using System.Utilities;` does not resolve, and the compiler reports it as
    AL0185 "Codeunit 'Temp Blob' is missing" — which reads like a missing DEPENDENCY and
    sends every repair round hunting app.json instead of the two lines actually needed.

    Measured on the doclink fixture: 0/12 builds across four sessions, four models and two
    pipeline configurations, always at error score 1. The model emitted
    `using System.Azure.Storage` and `using Microsoft.Foundation.Attachment` but never
    `System.Utilities` (Temp Blob) or `System.Environment` (Tenant Media). No amount of
    coder capability invents a namespace; it is a lookup, and the symbol index already
    holds it.

    Covers both shapes a file can reference an object in: typed declarations
    (`Codeunit "Temp Blob"`) and object headers (`extends "Document Attachment"`,
    `implements "IBlobStore"`). The header case was missing and cost 25% of doclink runs.

    Deterministic and conservative:
      * a namespace is added ONLY for a name the symbol index resolves — never invented
      * existing `using` lines are never removed or reordered
      * the file's own namespace and project-local objects are skipped
      * anything unresolved is left alone; the compiler still gets the last word
    """
    idx = _symbol_index()
    if not idx:
        return
    own = {n.lower() for n in _local_object_names()}
    added_total, touched = 0, 0
    for dp, _, fs in os.walk(PROJECT_ROOT + "/src"):
        for fn in sorted(fs):
            if not fn.endswith(".al"):
                continue
            path = os.path.join(dp, fn)
            try:
                text = open(path, encoding="utf-8-sig", errors="replace").read()
            except OSError:
                continue
            lines = text.splitlines()
            have = {l.strip()[6:].rstrip(";").strip()
                    for l in lines if l.strip().startswith("using ")}
            self_ns = next((l.strip()[10:].rstrip(";").strip()
                            for l in lines if l.strip().startswith("namespace ")), "")

            # Strip string literals and comments first: a namespace named inside a Caption
            # or a // note is not a reference.
            scan = _strip_noncode(lines)

            need = set()
            for name in _referenced_object_names(scan):
                if not name or name.lower() in own:
                    continue
                rec = idx.get(name.lower())
                ns = (rec or {}).get("ns", "")
                if ns and ns != self_ns and ns not in have:
                    need.add(ns)
            if not need:
                continue

            # Insert after the namespace line and any existing usings, before the object.
            obj_idx = next((i for i, l in enumerate(lines) if _OBJ_RE.match(l)), None)
            if obj_idx is None:
                continue
            ins = 0
            for i, l in enumerate(lines[:obj_idx]):
                st = l.strip()
                if st.startswith("namespace ") or st.startswith("using "):
                    ins = i + 1
            new = [f"using {n};" for n in sorted(need)]
            lines[ins:ins] = new
            try:
                open(path, "w", encoding="utf-8").write("\n".join(lines) + "\n")
            except OSError:
                continue
            added_total += len(new)
            touched += 1
    if added_total:
        print(f"  added {added_total} missing using-directive(s) across {touched} file(s)")


_EVENTSUB_ATTR_RE = re.compile(r"\[\s*EventSubscriber\s*\((?P<args>[^\]]*?)\)\s*\]",
                               re.IGNORECASE)


def _split_attr_args(text):
    """Top-level comma split that respects both quote styles and nested parens."""
    out, buf, depth, q = [], [], 0, ""
    for ch in text:
        if q:
            buf.append(ch)
            if ch == q:
                q = ""
            continue
        if ch in "\"'":
            q = ch
            buf.append(ch)
        elif ch == "(":
            depth += 1
            buf.append(ch)
        elif ch == ")":
            depth -= 1
            buf.append(ch)
        elif ch == "," and depth == 0:
            out.append("".join(buf))
            buf = []
        else:
            buf.append(ch)
    out.append("".join(buf))
    return out


def normalize_event_subscriber_element():
    """Replace an empty DOUBLE-quoted element argument with an empty string.

        [EventSubscriber(ObjectType::Table, Database::"X", 'OnEvent', "", true, true)]
                                                                      ^^ AL0242

    `""` is an empty QUOTED IDENTIFIER, which is not legal; `''` is an empty string, which
    is. The compiler reports `AL0242: Invalid attribute argument syntax: ''` — quoting the
    thing it wanted back at you, which reads like the '' is the problem.

    Scope is deliberately this one argument. A probe against BC27 settled what the
    compiler actually accepts, and the first version of this normalizer would have been
    wrong:

        'OnEvent', ''   verified        "OnEvent", ''   verified
        OnEvent,   ''   verified        'OnEvent', ""   AL0242
                                        "OnEvent", ""   AL0242

    The event NAME compiles single-quoted, double-quoted or bare — so rewriting its quotes
    (the original plan) would have churned correct code and left the real fault in place.
    Only the empty `""` is invalid. Omitting the element entirely is AL0238 and leaving it
    blank is AL0114, so `''` is required rather than merely conventional.
    """
    fixed = 0
    for dp, _, fs in os.walk(PROJECT_ROOT + "/src"):
        for fn in sorted(fs):
            if not fn.endswith(".al"):
                continue
            path = os.path.join(dp, fn)
            try:
                text = open(path, encoding="utf-8-sig", errors="replace").read()
            except OSError:
                continue

            def _fix(m):
                args = _split_attr_args(m.group("args"))
                if len(args) < 4 or args[3].strip() != '""':
                    return m.group(0)
                args[3] = args[3].replace('""', "''", 1)
                return "[EventSubscriber(" + ",".join(args) + ")]"

            new = _EVENTSUB_ATTR_RE.sub(_fix, text)
            if new != text:
                try:
                    open(path, "w", encoding="utf-8").write(new)
                except OSError:
                    continue
                fixed += 1
    if fixed:
        print(f"  fixed empty \"\" event element in {fixed} file(s)")


def normalize_string_properties():
    """Quote unquoted string-property values (Caption/ToolTip/... = AL0219).
    Whitelist-only + only wraps PROSE values (has a space / non-identifier char),
    so a bare identifier (possibly a Label variable) is left alone. Deterministic
    safety net for the model forgetting quotes — its commonest trailing error."""
    fixed = 0
    for dp, _, fs in os.walk(PROJECT_ROOT + "/src"):
        for fn in fs:
            if not fn.endswith(".al"):
                continue
            p = os.path.join(dp, fn)
            lines = open(p).read().splitlines()
            changed = False
            out = []
            for ln in lines:
                m = _STRPROP_RE.match(ln)
                if m:
                    val = m.group(4).strip()
                    if val and not val[0] in ("'", '"') and not _IDENT_RE.match(val):
                        ln = f"{m.group(1)}{m.group(2)}{m.group(3)}'{val}'{m.group(5)}"
                        changed = True
                out.append(ln)
            if changed:
                open(p, "w").write("\n".join(out) + "\n")
                fixed += 1
    if fixed:
        print(f"  normalized string-property quoting in {fixed} file(s)")


# `Name: Record 2000000184 "Tenant Media";` — an object ID inside a var declaration.
# Only object DECLARATIONS take an id (`codeunit 50100 "X"`); a variable references the
# type by name alone, so the id is AL0104 (';' expected). Models produce this by inlining
# a spec comment like `TenantMedia: Record "Tenant Media";  // table 2000000184`.
# Observed suite5 doclink r2: 15 consecutive file-rewrites reproduced the same line —
# the model cannot see it, so fix it deterministically instead of spending rounds.
_VARID_RE = re.compile(
    r'^(\s*\w+\s*:\s*)(Record|Codeunit|Page|Report|Query|XmlPort|Enum|Interface)'
    r'\s+\d+\s+(")', re.IGNORECASE)


def normalize_var_object_ids():
    """Strip object IDs from variable declarations (`: Record 123 "X"` -> `: Record "X"`)."""
    fixed = 0
    for dp, _, fs in os.walk(PROJECT_ROOT + "/src"):
        for fn in fs:
            if not fn.endswith(".al"):
                continue
            p = os.path.join(dp, fn)
            lines = open(p).read().splitlines()
            out, changed = [], False
            for ln in lines:
                new = _VARID_RE.sub(r"\1\2 \3", ln)
                changed |= new != ln
                out.append(new)
            if changed:
                open(p, "w").write("\n".join(out) + "\n")
                fixed += 1
    if fixed:
        print(f"  normalized object-id-in-var-declaration in {fixed} file(s)")


# Table auto-generated (trigger) events: the compiler publishes these with FIXED
# parameter names, so a subscriber that renames them for readability fails AL0282
# ("member referenced by event subscriber parameter X is not found"). Value is
# (record-param names in order, name for a Boolean param, name for an Integer
# param). Trailing params may be omitted by a subscriber — only the NAMES of the
# ones present must match, so this is a pure rename, never an insertion.
_TABLE_EVENT_PARAMS = {
    "OnBeforeInsertEvent":   (("Rec",),        "RunTrigger", None),
    "OnAfterInsertEvent":    (("Rec",),        "RunTrigger", None),
    "OnBeforeModifyEvent":   (("Rec", "xRec"), "RunTrigger", None),
    "OnAfterModifyEvent":    (("Rec", "xRec"), "RunTrigger", None),
    "OnBeforeDeleteEvent":   (("Rec",),        "RunTrigger", None),
    "OnAfterDeleteEvent":    (("Rec",),        "RunTrigger", None),
    "OnBeforeRenameEvent":   (("Rec", "xRec"), "RunTrigger", None),
    "OnAfterRenameEvent":    (("Rec", "xRec"), "RunTrigger", None),
    "OnBeforeValidateEvent": (("Rec", "xRec"), None,         "CurrFieldNo"),
    "OnAfterValidateEvent":  (("Rec", "xRec"), None,         "CurrFieldNo"),
}
# Spans a rename must never touch: AL string literals ('' is the escape),
# double-quoted identifiers (object/field names — never a parameter reference),
# and //-comment tails.
_AL_STR_OR_COMMENT = re.compile(r"'(?:[^']|'')*'|\"[^\"]*\"|//.*$")
_TBLSUB_RE = re.compile(
    r"\[EventSubscriber\s*\(\s*ObjectType::Table\s*,[^\]]*?'(?P<event>\w+)'[^\]]*\]",
    re.IGNORECASE)
# Procedure names may be QUOTED ("Room Booking_OnBeforeInsertEvent") — legal AL, and
# models reach for it when the name embeds an object name with a space. A bare \w+ here
# silently skipped those declarations, so the AL0282 rename below never fired and the
# build plateaued on an error the guard exists to fix (seen on bench-p4, Qwen3.8).
_PROCDECL_RE = re.compile(
    r'^\s*(?:local\s+|internal\s+)?procedure\s+(?:\w+|"[^"]+")\s*\(', re.IGNORECASE)
_PARAM_RE = re.compile(
    r"^\s*(?P<var>var\s+)?(?P<name>[A-Za-z_]\w*)\s*:\s*(?P<type>.+?)\s*$")


def _sub_outside_strings(line, pattern, repl):
    """re.sub that skips AL string literals and //-comment tails."""
    out, pos = [], 0
    for m in _AL_STR_OR_COMMENT.finditer(line):
        out.append(re.sub(pattern, repl, line[pos:m.start()]))
        out.append(m.group(0))
        pos = m.end()
    out.append(re.sub(pattern, repl, line[pos:]))
    return "".join(out)


def _split_params(sig):
    """Split a parameter list on top-level ';' (types may contain quotes/brackets)."""
    out, depth, cur, quo = [], 0, "", False
    for ch in sig:
        if ch == '"':
            quo = not quo
        elif not quo and ch in "([":
            depth += 1
        elif not quo and ch in ")]":
            depth -= 1
        if ch == ";" and depth == 0 and not quo:
            out.append(cur)
            cur = ""
            continue
        cur += ch
    if cur.strip():
        out.append(cur)
    return out


def normalize_table_event_subscribers():
    """Rename table auto-event subscriber parameters to their published names
    (Rec / xRec / RunTrigger / CurrFieldNo) — AL0282. Every model tested renames `Rec` to
    something descriptive (`DocumentAttachment`), which the compiler rejects; the
    correct names are fixed by the platform, so this is mechanical, not authoring.
    Renames the identifier in the procedure body too. Idempotent."""
    fixed = 0
    for dp, _, fs in os.walk(PROJECT_ROOT + "/src"):
        for fn in fs:
            if not fn.endswith(".al"):
                continue
            p = os.path.join(dp, fn)
            text = open(p).read()
            lines = text.splitlines()
            changed = False
            for i, ln in enumerate(lines):
                m = _TBLSUB_RE.search(ln)
                if not m:
                    continue
                spec = _TABLE_EVENT_PARAMS.get(
                    next((k for k in _TABLE_EVENT_PARAMS
                          if k.lower() == m.group("event").lower()), ""))
                if not spec:
                    continue
                rec_names, bool_name, int_name = spec
                # the declaration follows the attribute; gather until parens balance
                j = next((k for k in range(i + 1, min(i + 6, len(lines)))
                          if _PROCDECL_RE.match(lines[k])), None)
                if j is None:
                    continue
                end = j
                while end < len(lines) and lines[end].count("(") > lines[end].count(")"):
                    end += 1
                if end >= len(lines):
                    continue
                decl = "\n".join(lines[j:end + 1])
                open_i, close_i = decl.find("("), decl.rfind(")")
                if open_i < 0 or close_i < open_i:
                    continue
                params = _split_params(decl[open_i + 1:close_i])
                renames, rec_i = [], 0
                for prm in params:
                    pm = _PARAM_RE.match(prm.replace("\n", " "))
                    if not pm:
                        continue
                    old, typ = pm.group("name"), pm.group("type")
                    if typ.lower().startswith("record"):
                        want = rec_names[rec_i] if rec_i < len(rec_names) else None
                        rec_i += 1
                    elif typ.strip().lower() == "boolean":
                        want = bool_name
                    elif typ.strip().lower() == "integer":
                        want = int_name
                    else:
                        want = None
                    if want and old != want:
                        renames.append((old, want))
                if not renames:
                    continue
                # body span: decl → next attribute/declaration or end of object
                body_end = len(lines)
                for k in range(end + 1, len(lines)):
                    s = lines[k].lstrip()
                    if s.startswith("[") or _PROCDECL_RE.match(lines[k]) or \
                       s.startswith("trigger ") or lines[k].rstrip() == "}":
                        body_end = k
                        break
                # collision guard: if a target name is already used in the body
                # (a local var etc.), a blind rename would merge two identifiers
                # into one — a silent semantic bug. Leave that one for the loop.
                safe = []
                for old, want in renames:
                    clash = any(
                        re.search(rf"\b{re.escape(want)}\b",
                                  _AL_STR_OR_COMMENT.sub("", lines[k]))
                        for k in range(end + 1, body_end))
                    if clash:
                        print(f"    AL0282 guard: {os.path.basename(p)} "
                              f"{m.group('event')} — skip {old}→{want} "
                              f"('{want}' already used in body)")
                    else:
                        safe.append((old, want))
                renames = safe
                if not renames:
                    continue
                for k in range(j, body_end):
                    for old, want in renames:
                        # (?<!Record )(?<!::) — a param is often named after its
                        # table (Item: Record Item); the TYPE and enum/object
                        # refs (Database::Item) must keep the original name.
                        lines[k] = _sub_outside_strings(
                            lines[k],
                            rf"(?<!Record )(?<!::)\b{re.escape(old)}\b", want)
                changed = True
                print(f"    AL0282 guard: {os.path.basename(p)} {m.group('event')} — "
                      + ", ".join(f"{o}→{n}" for o, n in renames))
            if changed:
                open(p, "w").write("\n".join(lines) + "\n")
                fixed += 1
    if fixed:
        print(f"  normalized table-event subscriber params in {fixed} file(s)")


# NOTE: a deterministic AL0111 "semicolon expected" auto-inserter was tried and
# REMOVED — that error is usually a symptom of a malformed construct (e.g. qwen
# wrote invalid `try begin`), not a literally-missing ';'. Blind insertion makes
# garbage and the error often masks downstream errors (parse-halt). Only fix
# truly-mechanical issues deterministically: using placement, string-prop quoting,
# app.json (id range). Real semantic errors are for the model/loop.


_symbols_ready = False   # download once per run, reuse the project's .alpackages after


REQUIRED_ANALYZERS = ("CodeCop", "UICop", "PerTenantExtensionCop")
# Opt-in escape for a box genuinely without the cops. The result is marked
# bare_compile_only in metrics and `promote` refuses it — a bare compile is NOT the
# referee this pipeline claims (PTE0004 is an ERROR only under PerTenantExtensionCop,
# the AA02xx family only under CodeCop/UICop), so it must never silently pass as one.
ALLOW_BARE_COMPILE = os.environ.get("ALLOW_BARE_COMPILE") == "1"


# Resolved cop directory. None = not probed yet, False = probed and absent, str = found.
# The tri-state matters: an absent toolchain must not be re-globbed on every compile of
# every fix round.
_analyzer_dir_cache = None

_TOOL_STORE = "~/.dotnet/tools/.store/microsoft.dynamics.businesscentral.development.tools"


def _analyzer_dir():
    """Directory holding the cop DLLs, or None.

    Ported from ALNvim's compile.lua, which had already solved this properly. The glob
    here used to hard-code `net10.0/any`: correct on this box today, and silently wrong
    the day the AL tool ships a different target framework. Because missing_analyzers()
    fails closed, that break presents as "REFEREE UNAVAILABLE — required analyzer(s) not
    found" on a machine where the analyzers are plainly installed.

    Search order, most specific first:
      1. the dotnet tool store, any TFM — preferring the one currently in use so this
         change does not alter which DLLs get loaded today
      2. the VS Code AL extension's shared Analyzers directory, for a box that has the
         extension but not the dotnet tool
    """
    global _analyzer_dir_cache
    if _analyzer_dir_cache is not None:
        return _analyzer_dir_cache or None

    import glob as _glob
    hits = _glob.glob(os.path.expanduser(
        _TOOL_STORE + "/**/Microsoft.Dynamics.Nav.CodeCop.dll"), recursive=True)
    chosen = None
    if hits:
        # Prefer net10.0 to preserve the behaviour this pipeline's whole measured corpus
        # was produced under; fall back to whatever TFM is present rather than failing.
        # (ALNvim prefers net8.0 "for broad runtime compatibility" — a defensible
        # different call, not one to make silently mid-project.)
        chosen = next((h for h in hits if "/net10.0/" in h), hits[0])
    if not chosen:
        for ext in ("~/.vscode/extensions", "~/.vscode-server/extensions"):
            alt = _glob.glob(os.path.expanduser(
                ext + "/ms-dynamics-smb.al-*/bin/Analyzers/Microsoft.Dynamics.Nav.CodeCop.dll"))
            if alt:
                chosen = alt[0]
                break

    _analyzer_dir_cache = os.path.dirname(chosen) if chosen else False
    return _analyzer_dir_cache or None


def _analyzer_dlls():
    """Cop analyzer DLLs that actually EXIST, in REQUIRED_ANALYZERS order.

    Only readable paths are returned. The previous version emitted a path per required
    cop whether or not the file was there, so a partial install produced a `/analyzer:`
    flag pointing at nothing and the compiler failed for a reason that named neither the
    cop nor the install.
    """
    d = _analyzer_dir()
    if not d:
        return []
    out = []
    for n in REQUIRED_ANALYZERS:
        p = os.path.join(d, f"Microsoft.Dynamics.Nav.{n}.dll")
        if os.path.exists(p):
            out.append(p)
    return out


def missing_analyzers():
    """Names of required cops whose DLL is absent. Empty list = full referee available.

    Checked by NAME against the resolved directory, not by zipping two lists — now that
    _analyzer_dlls() returns only files that exist, a positional pairing would line the
    wrong name up against the wrong path the moment one cop was missing, and report a
    present cop as absent.
    """
    d = _analyzer_dir()
    if not d:
        return list(REQUIRED_ANALYZERS)
    return [n for n in REQUIRED_ANALYZERS
            if not os.path.exists(os.path.join(d, f"Microsoft.Dynamics.Nav.{n}.dll"))]


def _local_object_names():
    """Object names declared by the project's own source.

    A publisher the project defines itself is not in the downloaded symbols, so without
    this every in-project event subscription would be reported as a missing publisher —
    a false accusation against correct code, which is the one failure mode a pre-compile
    verifier cannot afford.
    """
    names = set()
    # An object DECLARATION carries an id (`page 50106 "Name"`). A permission-set body
    # references objects without one (`page "Name";`), and matching those pulled in
    # whole mangled lines as if they were object names.
    decl = re.compile(r'^\s*(?:table|codeunit|page|report|query|xmlport|enum|'
                      r'permissionset|controladdin)(?:extension)?\s+\d+\s+'
                      r'("[^"]+"|\w+)', re.IGNORECASE)
    iface = re.compile(r'^\s*interface\s+("[^"]+"|\w+)', re.IGNORECASE)
    for f in glob.glob(os.path.join(PROJECT_ROOT, "src", "**", "*.al"), recursive=True):
        try:
            for ln in open(f, encoding="utf-8-sig", errors="replace"):
                m = decl.match(ln) or iface.match(ln)
                if m:
                    names.add(m.group(1).strip('"'))
        except OSError:
            continue
    return names


def run_al_compile():
    global _symbols_ready
    print("\n--- AL compile ---")
    write_canonical_app_json()
    normalize_using_directives()
    normalize_string_properties()
    normalize_var_object_ids()
    normalize_event_subscriber_element()
    normalize_table_event_subscribers()
    proj_cache = PROJECT_ROOT + "/.alpackages"
    if _symbols_ready and os.path.isdir(proj_cache) and os.listdir(proj_cache):
        pkg_cache = proj_cache
        print(f"  symbols: reusing {proj_cache} (already downloaded this run)")
    else:
        pkg_cache = mcp_download_symbols()
        if not pkg_cache:
            msg = "Symbol download (scoped al-mcp, globalSourcesOnly) failed — no symbols. Aborting build (no copy fallback)."
            print(f"  {msg}")
            return f"BUILD: FAILED\n{msg}", False
        _symbols_ready = True
    print(f"  packagecachepath: {pkg_cache}")
    global _last_diags
    sarif = PROJECT_ROOT + "/.build-errors.sarif"
    # The referee is "compiler PLUS analyzers". If a required cop is missing, the
    # compile that follows is NOT that referee — it is a weaker check that would report
    # PASS while silently skipping whole diagnostic classes. Fail closed.
    _missing = missing_analyzers()
    if _missing and not ALLOW_BARE_COMPILE:
        print(f"  ⛔ REFEREE UNAVAILABLE — required analyzer(s) not found: "
              f"{', '.join(_missing)}")
        print(f"     A bare compile is not the referee. Install the AL tool's cops, or "
              f"set ALLOW_BARE_COMPILE=1 to accept a diagnostically weaker build "
              f"(marked bare_compile_only; promote will refuse it).")
        # Same shape as the normal return (see the BUILD: line below) so downstream
        # error counting and the fix loop treat this like any other failed build.
        return ("BUILD: FAILED\nREFEREE UNAVAILABLE: missing required analyzer(s): "
                + ", ".join(_missing)), False
    if _missing:
        print(f"  ⚠ BARE COMPILE ONLY (ALLOW_BARE_COMPILE=1) — missing: "
              f"{', '.join(_missing)}. This result cannot be promoted.")

    # Namespaces before verification: an object that fails to resolve for want of a
    # `using` looks exactly like an invented one to event_verify.
    try:
        add_missing_using_directives()
    except Exception as _e:
        print(f"  using-directive completion skipped ({_e})")

    # AL-4: verify subscribers against symbols BEFORE compiling. Every finding here is a
    # compile error the model would otherwise discover a full round later, and the
    # symbol-cited message is more actionable than the compiler's. Advisory only — the
    # compiler stays the authority, so a verifier false negative costs nothing and a
    # false positive cannot fail a correct build.
    global _event_findings
    _event_findings = []
    try:
        _idx = _symbol_index()
        if _idx:
            _event_findings = event_verify.verify(
                os.path.join(PROJECT_ROOT, "src"), _idx, local_objects=_local_object_names())
            if _event_findings:
                _errs = sum(1 for f in _event_findings if f["severity"] == "error")
                print(f"  event check: {len(_event_findings)} finding(s), {_errs} error(s) "
                      f"— reported before compiling")
                for _f in _event_findings[:6]:
                    print(f"    [{_f['severity']}] {_f['file']}:{_f['line']} — {_f['message']}")
    except Exception as _e:
        print(f"  event check unavailable ({_e})")

    def _compile():
        cmd = [AL_CLI, "compile", f"/project:{PROJECT_ROOT}", f"/packagecachepath:{pkg_cache}",
               f"/errorlog:{sarif}"]
        # Cop analyzers: a bare compile misses whole diagnostic classes (PTE0004 missing
        # permission set is an ERROR under PerTenantExtensionCop; AA02xx under CodeCop/UICop).
        cmd += [f"/analyzer:{d}" for d in _analyzer_dlls()]
        r = subprocess.run(cmd, capture_output=True, text=True)
        return (r.stdout + r.stderr).strip(), r.returncode == 0

    output, succeeded = _compile()
    _last_diags = parse_sarif(sarif)   # structured diagnostics (code/severity/file/line)
    try:
        os.remove(sarif)
    except OSError:
        pass
    print(f"  Build {'PASSED' if succeeded else 'FAILED'}")
    if not succeeded and output:
        for line in output.splitlines():
            if line.strip():
                print(f"  {line}")
    if not succeeded and _event_findings:
        output = (event_verify.format_findings(_event_findings) + "\n\n" + output).strip()
    return f"BUILD: {'PASSED' if succeeded else 'FAILED'}\n{output}", succeeded


# ---------------------------------------------------------------------------
# Build result helpers
# ---------------------------------------------------------------------------

def truncate_build(build_text, max_lines=20):
    """Dedupe + cap a compiler error dump so it doesn't blow the model context.
    A failed AL build repeats the same root errors across every line/file; we
    keep one example per distinct error message (path/line/col stripped) and
    cap the total. Larry should fix from the reviewer's findings anyway."""
    seen = {}
    order = []
    for line in build_text.splitlines():
        s = line.strip()
        if not s:
            continue
        # strip "path(line,col): " prefix so identical messages collapse
        key = re.sub(r'^.*?\(\d+,\d+\):\s*', '', s)
        key = re.sub(r'^error AL\d+:\s*|^warning AL\d+:\s*', '', key)
        if key not in seen:
            seen[key] = s
            order.append(key)
    head = [seen[k] for k in order[:max_lines]]
    extra = len(order) - len(head)
    if extra > 0:
        head.append(f"... (+{extra} more distinct messages, omitted)")
    return "\n".join(head)


def count_build_errors(build_text, build_ok):
    """Error count for the keep-best guard. 0 if build passed."""
    if build_ok:
        return 0
    # AL = compiler, PTE/AA/AS = cop analyzers (PerTenantExtensionCop/CodeCop/AppSourceCop)
    return len(re.findall(r'error (?:AL|PTE|AA|AS)\d+', build_text))


def error_keys(build_text):
    """Identity set of a build's errors: (file, code, message-prefix). Used to tell a
    genuine regression from an UNMASKING — on doclink, fixing the one AL0282 blocker
    surfaced 16 pre-existing AL0132 hallucinations the failed subscriber bind had been
    suppressing. Raw count says 1→16 = worse; the identity sets are disjoint, which
    says the old error is FIXED and these are new work, i.e. forward progress."""
    keys = set()
    for m in re.finditer(r"([^\s(]+\.al)\(\d+,\d+\): error ((?:AL|PTE|AA|AS)\d+): (.{0,60})",
                         build_text or ""):
        keys.add((os.path.basename(m.group(1)), m.group(2), m.group(3).strip()))
    return keys


# Source files the keep-best guard tracks. NOT just .al: a ControlAddin project
# keeps its js/css under src/ and they are manifest files too — snapshotting only
# .al meant a regressing round was reverted for AL but its js/css damage persisted,
# leaving the final "best" tree a hybrid of best-round AL + last-round assets.
SNAPSHOT_EXTS = (".al", ".js", ".css", ".html")


def snapshot_src():
    """Capture current src/ sources + app.json contents for revert-on-regress."""
    snap = {}
    for dp, _, fs in os.walk(PROJECT_ROOT + "/src"):
        for fn in fs:
            if fn.endswith(SNAPSHOT_EXTS):
                p = os.path.join(dp, fn)
                snap[p] = open(p).read()
    aj = PROJECT_ROOT + "/app.json"
    if os.path.exists(aj):
        snap[aj] = open(aj).read()
    return snap


def _snapshot_scope():
    """Every path snapshot_src() would capture — the scope rollback must restore."""
    out = []
    for dp, _, fs in os.walk(PROJECT_ROOT + "/src"):
        for fn in fs:
            if fn.endswith(SNAPSHOT_EXTS):
                out.append(os.path.join(dp, fn))
    aj = PROJECT_ROOT + "/app.json"
    if os.path.exists(aj):
        out.append(aj)
    return out


def restore_src(snap):
    """Restore the EXACT snapshot tree (revert a regressing fix round).

    Previously this only rewrote the captured files, so a file CREATED by the regressing
    round survived the rollback — the tree ended up as "best files + the bad round's new
    files", which breaks the no-regress guarantee the keep-best loop is built on. Remove
    anything in scope that the snapshot did not contain, then restore contents (which
    also brings back files the bad round deleted). run-build-cs.py already did this; the
    Go runner had the same bug and is fixed alongside.
    """
    for p in _snapshot_scope():
        if p not in snap:
            try:
                os.remove(p)
            except OSError:
                pass
    for p, content in snap.items():
        d = os.path.dirname(p)
        if d:
            os.makedirs(d, exist_ok=True)
        with open(p, "w") as f:
            f.write(content)


def select_topics(manifest_files, handover_text, budget_k=None):
    """Pick AL-REFERENCE topics from what this project actually declares.

    `budget_k` is the real headroom — ctx_budget_k() minus what the rest of the prompt
    already costs — and the caller is expected to pass it. It defaults to INJECT_BUDGET_K
    only so that tests and ad-hoc calls keep working; a build that relies on that default
    is selecting against a ceiling it may not be able to spend.

    Measured: al-rule diagnostics are 53.8% of all failures, and injecting the matching
    topics took the suite from 5/10 to 9/12 passes.

    Selection is driven mainly by the manifest's object suffixes, which are hard evidence.
    Keyword hints come from the SPEC BODY ONLY: the "Read first" section names topic files
    like `09-api-web.md`, so scanning the whole handover matched "api" in every project and
    handed all four fixtures an identical set.

    `handover_text` MUST be the raw spec, before BCQuality rules and API grounding are
    appended to the coder prompt. Measured 2026-08-29: BCQuality contributes ~7.8k of rule
    prose that mentions events, which flipped the event regex true for bench-p1-crud — a
    plain CRUD fixture whose own spec never mentions an event — and spent 4.22k of a 14k
    budget on 07-events-errors. That is the same "matched in every project" failure as the
    Read-first bug above, arriving through a different door: text WE append is not evidence
    about the project.

    Tiers, not one flat list, because the cap below is first-come and so ordering IS
    selection — whatever sorts last is what gets dropped:
      core     every AL write needs these. 02-objects is core because evicting it took the
               benchmark control from 2/3 to 0/3.
      specific fired by narrow evidence naming this project's subject (blob, semantic
               search). Ranked above `broad`: the evidence is about THIS project.
      broad    fires on nearly every project, so it carries the least per-project signal.
    """
    kinds = {object_type(f) for f in manifest_files}
    names = " ".join(manifest_files).lower()
    # drop the meta sections that talk ABOUT the reference, plus fenced blocks
    body = re.sub(r"^##\s*Read first.*?(?=^## )", "", handover_text or "", flags=re.S | re.M)
    body = re.sub(r"```.*?```", "", body, flags=re.S).lower()

    core = ["00-gotchas", "01-syntax-style"]                      # always
    specific, broad = [], []
    if kinds & {"Table", "Page", "Codeunit", "Report", "ControlAddin", "Enum",
                "PageExt", "TableExt"}:
        core.append("02-objects")
    if kinds & {"PageExt", "TableExt"} or re.search(r"\bsubscri|\bonbefore|\bonafter|\bevent\b", body):
        broad.append("07-events-errors")
    if re.search(r"\bsetloadfields|\bsetrange|\bperformance\b|\bsift\b", body):
        specific.append("03-records-performance")
    if re.search(r"\bblob\b|\bstream\b|\bazure\b|isolatedstorage", body):
        specific.append("08-data-storage")
    # A PermissionSet in the manifest is a weak proxy for "this is an API project" — nearly
    # every extension ships one — so this lands in `broad`, not `specific`.
    if "permissionset" in names or re.search(r"\bapi page|\bweb service|\bodata\b", body):
        broad.append("09-api-web")
    if re.search(r"^\s*namespace\s", body, re.M):
        specific.append("14-namespaces")
    # Deliberately specific. A bare \bsearch\b fires on ordinary prose ("search the
    # ledger for...") and would spend 2.3k of a 14k budget on every unrelated build —
    # the same shape as the injection-budget regression that evicted 02-objects and took
    # the benchmark control from 2/3 to 0/3. These terms only appear when the handover is
    # actually about BC's search facilities.
    if re.search(r"\bsemantic search\b|\bfull[- ]?text\b|optimizefortextsearch|"
                 r"optimizedtextsearch|\bembedding vector|\bvector search\b", body):
        specific.append("25-search-relational-full-text-semantic-al")

    cap = INJECT_BUDGET_K if budget_k is None else min(INJECT_BUDGET_K, budget_k)
    want = core + specific + broad
    out, used, dropped = [], 0.0, []
    for t in dict.fromkeys(want):
        fp = os.path.join(REPO_REFERENCE, "al-reference", t + ".md")
        try:
            size = os.path.getsize(fp) / 3700.0
        except OSError:
            continue
        if used + size > cap and out:
            dropped.append((t, size))
            continue
        out.append(t)
        used += size
    if dropped:
        # Say it. A silent drop is how doclink selected 08-data-storage on hard evidence,
        # lost it to the cap without a word, and then failed on the ABS API errors that
        # topic covers. The selection being right is invisible if the eviction is quiet.
        why = (f"INJECT_BUDGET_K={INJECT_BUDGET_K:g}" if cap >= INJECT_BUDGET_K
               else f"ctx headroom {cap:.1f}k (INJECT_BUDGET_K={INJECT_BUDGET_K:g} unreachable)")
        print("  inject: DROPPED " + ", ".join(f"{t} ({s:.2f}k)" for t, s in dropped)
              + f" — over {why}")
    return out, used


def _unresolved_names(build_text):
    """Identifiers the compiler says it cannot resolve. These are the hallucinations:
    AL0185 'X is missing', AL0118 'name X does not exist', AL0124 'property X cannot be
    used'. Their real declarations are in the indexed BC source, so they are lookup-able."""
    pats = [r"Table '([^']{2,60})' is missing",
            r"The name '\"?([^'\"]{2,60})\"?' does not exist",
            r"The property '([^']{2,60})' cannot be used",
            r"'([^']{2,60})' is not found in the target"]
    names = []
    for p in pats:
        for m in re.findall(p, build_text or ""):
            n = m.strip().strip('"')
            if n and n not in names:
                names.append(n)
    return names[:5]          # cap: a handful of precise lookups, not a dump


def _decl_name(heading):
    """The object NAME out of a kb heading (`codeunit 9047 "ABS Optional Parameters"`).
    Substring matching is not safe here: `page 30080 "APIV2 - Document Attachments"`
    contains "Document Attachment" but is a different object, and presenting it as
    ground truth would invent a new hallucination rather than correct one."""
    h = (heading or "").split("\u203a")[0].strip()
    m = re.search(r'"([^"]+)"', h)
    if m:
        return m.group(1)
    m = re.match(r"\s*\w+\s+\d+\s+(\w+)", h)
    return m.group(1) if m else ""


def _norm(t):
    """Loose compare for name-vs-declaration matching (case/punctuation-insensitive)."""
    return re.sub(r"[^a-z0-9]+", " ", (t or "").lower()).strip()


def _symbol_index():
    """Declarations from the project's own downloaded symbol packages. These are the
    exact symbols `al compile` resolves against, so they cannot drift from the runtime
    the project targets — and unlike the indexed source corpora they include the Base
    Application, which is where most ungroundable names actually live. Cached."""
    global _sym_idx
    if _sym_idx is None:
        try:
            import al_symbols
            _sym_idx = al_symbols.build_index(os.path.join(PROJECT_ROOT, ".alpackages"))
            if _sym_idx:
                print(f"  RAG: {len(_sym_idx)} objects from downloaded symbols")
        except Exception as _e:
            print(f"  RAG: symbol index unavailable ({_e})")
            _sym_idx = {}
    return _sym_idx


def _sym_lookup(name):
    idx = _symbol_index()
    return idx.get((name or "").strip().strip('"').lower()) if idx else None


def _unresolved_members(build_text):
    """(object, member) pairs from AL0132 — the model picked a real object then invented
    a procedure or field on it. The object's true member list is in the indexed source."""
    out = []
    for obj, mem in re.findall(
            r"'(?:Codeunit|Record|Table|Page|Enum)?\s*([^']{2,90}?)'\s*does not contain a "
            r"definition for '([^']{1,60})'", build_text or ""):
        # strip a namespace prefix and quotes: System.Azure.Storage."ABS Optional Parameters"
        o = obj.split(".")[-1].strip().strip('"') if '"' in obj else obj.split(".")[-1].strip()
        if o and (o, mem) not in out:
            out.append((o, mem))
    return out[:4]


def _members_of(obj):
    """Real public members of a BC object: procedures for a codeunit, fields for a table.
    Located via the KB (the source is already indexed), then read from disk."""
    try:
        hits = []
        for _c in RAG_CORPORA:
            r = subprocess.run([KB_BIN, "search", obj, "--corpus", _c.strip(),
                                "-n", "3", "--json"], capture_output=True, text=True, timeout=60)
            got = json.loads(r.stdout or "[]")
            if any(_norm(obj) == _norm(_decl_name(h.get("heading") or "")) for h in got):
                hits = got
                break
    except Exception:
        return None, []
    for h in hits:
        head, path = (h.get("heading") or ""), h.get("path") or ""
        if not (path.endswith(".al") and _norm(obj) == _norm(_decl_name(head))):
            continue
        try:
            src = open(path, encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        # Quoted procedure names ("Room Booking_OnBeforeInsertEvent") are legal AL and
        # were invisible here, so grounding never offered them as a candidate. Keep the
        # quotes — that is how a call site spells the name.
        procs = re.findall(r'^\s+(?:local\s+|internal\s+)?procedure\s+(\w+|"[^"]+")', src, re.M)
        fields = re.findall(r"^\s+field\(\s*\d+\s*;\s*\"?([^;\"]+)\"?\s*;", src, re.M)
        return os.path.basename(path), sorted(set(procs + fields))
    return None, []


# Built-in AL types are NOT objects in the symbol packages (`instream` is simply absent
# from the 8103-object index), so member grounding can never correct a hallucinated method
# on one — the exact hole that let `InStream.TransferOutTo` survive 16 fix rounds
# (suite5 doclink r2). Member lists verified against Microsoft's own AL source in
# /mnt/rojaws/refs/BCApps by usage count; `TransferOutTo` appears ZERO times there.
BUILTIN_MEMBERS = {
    "instream":  ["Read", "ReadText", "EOS"],
    "outstream": ["Write", "WriteText"],
    "media":     ["HasValue", "MediaId", "ImportFile", "ImportStream", "ExportFile",
                  "ExportStream"],
    "mediaset":  ["Count", "Item", "Insert", "HasValue", "MediaId"],
}
# Free functions that do what models wrongly reach for as a method.
BUILTIN_NOTES = {
    "instream":  "To copy a whole stream use the GLOBAL `CopyStream(DestOutStream, SrcInStream)` "
                 "— it is a free function, NOT a method on the stream.",
    "outstream": "To copy a whole stream use the GLOBAL `CopyStream(DestOutStream, SrcInStream)`.",
    "media":     "Media has no Clear/IsEmpty and cannot be compared to Text — test with "
                 "`.HasValue`, and read its bytes via the Tenant Media record "
                 "(`TenantMedia.Get(Rec.\"Field\".MediaId()); TenantMedia.Content.CreateInStream(InStr);`).",
}


def ground_builtin_members(build_text):
    """Correct invented methods on BUILT-IN AL types (InStream/OutStream/Media/MediaSet)."""
    out = []
    for obj, mem in _unresolved_members(build_text):
        key = obj.strip().strip('"').lower()
        real = BUILTIN_MEMBERS.get(key)
        if not real or mem in real:
            continue
        line = (f"- `{obj}` is a BUILT-IN AL type and has NO `{mem}`. Its ONLY members are: "
                + ", ".join(f"`{x}`" for x in real) + ".")
        note = BUILTIN_NOTES.get(key)
        if note:
            line += " " + note
        out.append(line)
    if not out:
        return ""
    print(f"  RAG: corrected {len(out)} invented built-in member(s)")
    return ("\n\nINVENTED MEMBERS ON BUILT-IN TYPES — these are language primitives, not "
            "objects; the member you used does not exist:\n" + "\n".join(dict.fromkeys(out)) + "\n")


def kb_ground_members(build_text):
    """Correct invented procedures/fields (AL0132) by listing what the object really has.

    Grounding object TYPES (AL0185) cut that error class 3-5x but the model then called
    methods that do not exist on the now-correctly-typed object. Same failure one level
    down, and just as lookup-able."""
    pairs = _unresolved_members(build_text)
    if not os.path.exists(KB_BIN):
        _note_grounding("unavailable", f"KB_BIN missing at {KB_BIN}")
        return ""
    if not pairs:
        _note_grounding("available_no_matches", "no unresolved members to ground")
        return ""
    out = []
    for obj, mem in pairs:
        rec = _sym_lookup(obj)
        if rec and rec.get("members"):
            shown = ", ".join(f"`{x}`" for x in rec["members"][:24])
            more = f" (+{len(rec['members'])-24} more)" if len(rec["members"]) > 24 else ""
            entry = (f"- `{obj}` has NO `{mem}`. Its real members are: {shown}{more}"
                     f"  (downloaded symbols)")
            # If the invented member is a near-miss of a real one (typo/truncation), hand the
            # model that member's EXACT signature — event subscribers bind params BY NAME, so a
            # bare name isn't enough. Only searches THIS confirmed object's own members (no
            # nearest-neighbour object guess).
            sigs = rec.get("sigs") or {}
            ml = mem.lower()
            near = [s for n, s in sigs.items() if len(n) > 3 and (ml in n.lower() or n.lower() in ml)]
            if near:
                entry += "\n    closest real signature(s): " + "; ".join(f"`{s}`" for s in near[:3])
            out.append(entry)
            continue
        if not RAG_KB_FALLBACK:
            continue
        fname, members = _members_of(obj)
        if not members:
            continue
        # Keep it short: the model needs the real names, not the whole API surface.
        shown = ", ".join(f"`{x}`" for x in members[:24])
        more = f" (+{len(members)-24} more)" if len(members) > 24 else ""
        out.append(f"- `{obj}` has NO `{mem}`. Its real members are: {shown}{more}"
                   f"  (source: {fname})")
    if not out:
        return ""
    print(f"  RAG: corrected {len(out)} invented member(s)")
    _note_grounding("applied", "member lookups returned declarations", hits=len(out))
    return ("\n\nINVENTED MEMBERS — the compiler says these do not exist. Here is what each "
            "object actually provides, from the Business Central source. Use only these:\n"
            + "\n".join(out) + "\n")


def _app_json_now():
    try:
        with open(os.path.join(PROJECT_ROOT, "app.json")) as f:
            return json.load(f)
    except (OSError, ValueError):
        return {}


def probe_unresolved_objects(build_text):
    """When neither the symbols nor the KB can ground an object, ask the compiler.

    AL0132 ("X does not contain a definition for Y") is ambiguous to a model: it cannot
    tell "the object is real and the member is invented" from "the object name is wrong
    too". Symbols answer the first case; when they come up empty the loop currently says
    nothing at all, and the model re-guesses the same name.

    A probe settles it in ~6s by declaring a variable of that type and compiling. AL0185
    means the object does not exist under that name; a clean compile means it does and
    only the member was invented.

    Bounded by AL_PROBE_BUDGET because this costs real seconds, and OFF with AL_PROBE=0.
    """
    if not AL_PROBE:
        return ""
    ungrounded = [(o, m) for o, m in _unresolved_members(build_text)
                  if not _sym_lookup(o)]
    if not ungrounded:
        return ""
    out = []
    for obj, mem in ungrounded[:AL_PROBE_BUDGET]:
        verdicts = {}
        for kind in ("Record", "Codeunit"):
            r = al_probe.probe_snippet("", f'V: {kind} "{obj}";',
                                       like_project=PROJECT_ROOT, timeout=90)
            verdicts[kind] = r
            if r["ok"]:
                break
        good = [k for k, r in verdicts.items() if r["ok"]]
        # A timeout or a harness error proves nothing — say so rather than claim the
        # object is missing, which is the one wrong answer that compounds.
        if any(r["status"] in ("timeout", "error") for r in verdicts.values()) and not good:
            continue
        if good:
            out.append(f"- `{obj}` DOES exist as a {good[0]} (verified by compiling it). "
                       f"The object is right; `{mem}` is the invented part.")
        else:
            # Quote BOTH verdicts. Showing only the Record diagnostic reads as if the
            # codeunit case was never tried, which invites the model to "fix" it by
            # switching kind — the guess the probe was supposed to remove.
            why = "; ".join(f"as {k} → {v['summary'].split(':')[0]}"
                            for k, v in verdicts.items())
            out.append(f"- `{obj}` does NOT exist as a Record or a Codeunit — the OBJECT "
                       f"name is wrong, not just `{mem}`. Compiler: {why}")
    if not out:
        return ""
    print(f"  PROBE: settled {len(out)} ungrounded object name(s) with the compiler")
    return ("\n\nCOMPILER PROBE RESULTS — these were checked by compiling them in a "
            "throwaway project, so they are facts, not guesses:\n" + "\n".join(out) + "\n")


# file(line,col): error CODE: message — the position is what makes this groundable.
_DIAG_POS_RE = re.compile(
    r"^(?P<file>\S+?)\((?P<line>\d+),(?P<col>\d+)\):\s*error\s+"
    r"(?P<code>AL0133|AL0151|AL0126|AL0161|AL0257):\s*(?P<msg>.*)$", re.M)
# `X.Method(` on the offending line. The receiver is ignored — the member name is enough
# to find the signature, and several objects publishing the same name is a result the
# caller should see rather than a tie to break.
_CALL_RE = re.compile(r"\b(\w+)\s*\.\s*(?P<m>\w+)\s*\(")


AL_APIS = os.environ.get("AL_APIS") == "1"     # proactive API grounding (Phase 1b)
AL_API_BUDGET_K = float(os.environ.get("AL_API_BUDGET_K", "2.0"))
# Quoted identifiers in the handover: "ABS Blob Client", "Temp Blob". Two chars minimum
# and an initial capital keeps ordinary quoted prose out.
_HANDOVER_OBJ_RE = re.compile(r'"([A-Z][^"\n]{2,48})"')


def ground_handover_apis(handover_text, budget_k=None):
    """Put the REAL signatures of the base-app APIs a handover names into the prompt.

    Measured cause of the doclink fixture's 3/31 pass rate: it names six base-app objects
    that must be CALLED — ABS Blob Client, Storage Service Authorization, Temp Blob,
    Tenant Media, Document Attachment, Document Attachment Mgmt. The 95% fixture names
    three that are merely EXTENDED (Customer Card, Vendor Card, Post Code). Every doclink
    error class follows from the difference: AL0185 on their namespaces, AL0132 on invented
    members, AL0133 on wrong argument types, AL0134/AL0158 on invented types around them.

    The pipeline already holds every one of these signatures. Until now it only produced
    them REACTIVELY, after a failed compile (ground_call_signatures) — so the model never
    saw them before writing the code.

    Ranked, not dumped. The six objects' full method lists are 9,615 chars (~2.6k tokens)
    and ABS Blob Client alone is 41 methods where about four matter, so members are scored
    against the handover with the same embedding pass al_sections uses and the best few
    are kept within `budget_k`. Falls back to declaration order when ranking is
    unavailable — a degraded selection still beats no signatures.

    Only objects the symbol index resolves are quoted, and each line carries the package
    and version it came from.
    """
    if not AL_APIS:
        return ""
    idx = _symbol_index()
    if not idx:
        return ""
    import al_symbols

    own = {n.lower() for n in _local_object_names()}
    seen, objs = set(), []
    for name in _HANDOVER_OBJ_RE.findall(handover_text or ""):
        key = name.strip().lower()
        if key in seen or key in own:
            continue
        seen.add(key)
        rec = al_symbols.lookup(idx, name)
        if not rec or not (rec.get("sigs") or {}):
            continue
        # "Has methods" is too loose — pages carry methods too, so the 95% fixture's
        # "Customer Card" pulled in its whole surface for an object it only EXTENDS.
        # Include an object when it is something you CALL (codeunit/interface), or when
        # the handover names one of its members (Document Attachment is a table, but
        # GetAsTempBlob is named and needed).
        callable_kind = rec["kind"] in ("codeunit", "interface")
        member_named = any(re.search(rf"\b{re.escape(mm)}\b", handover_text or "")
                           for mm in (rec.get("sigs") or {}))
        if callable_kind or member_named:
            objs.append(rec)
    if not objs:
        return ""

    members = [(rec, m, sig) for rec in objs
               for m, sig in sorted((rec.get("sigs") or {}).items())]

    # Selection is DETERMINISTIC first. Embedding a long prose handover against a short
    # signature is a weak signal, and measurably so: ranking alone spent the budget on
    # ChangeLease and AppendBlockText while dropping GetBlobAsStream, CreateInStream and
    # CreateOutStream — three of the six methods doclink actually calls. The handover
    # NAMES the methods it needs and none of the ones it does not, so a name match is both
    # a better signal and one that can be explained.
    #
    #   tier 1  the handover names the method            — always include
    #   tier 2  the object's whole surface is small      — include it entire
    #   tier 3  fill what budget remains, best-ranked first
    named, small, rest = [], [], []
    for rec, m, sig in members:
        whole = sum(len(x) for x in (rec.get("sigs") or {}).values())
        if re.search(rf"\b{re.escape(m)}\b", handover_text or ""):
            named.append((rec, m, sig))
        elif whole <= 700:
            small.append((rec, m, sig))
        else:
            rest.append((rec, m, sig))
    try:
        import al_sections
        scored = al_sections.rank_sections(
            handover_text[:4000],
            [(f'{r["name"]}.{m}', sig) for r, m, sig in rest])
        if scored is not None:
            order = {h: i for i, (_s, h, _b) in enumerate(scored)}
            rest = sorted(rest, key=lambda t: order.get(f'{t[0]["name"]}.{t[1]}', 1e9))
    except Exception:
        pass
    ranked = named + small + rest

    budget = (budget_k if budget_k is not None else AL_API_BUDGET_K) * 3700.0
    by_obj, used = {}, 0.0
    for rec, m, sig in ranked:
        if used + len(sig) > budget:
            continue
        by_obj.setdefault(rec["name"], (rec, []))[1].append(sig)
        used += len(sig)
    if not by_obj:
        return ""

    lines = []
    for name in sorted(by_obj):
        rec, sigs = by_obj[name]
        ns = rec.get("ns", "")
        lines.append(f'\n{rec["kind"]} "{name}"'
                     + (f'  — namespace {ns}; needs `using {ns};`' if ns else ""))
        for sig in sigs:
            lines.append(f"    {sig}")
        lines.append(f"    (from {al_symbols.evidence(rec)})")
    n = sum(len(v[1]) for v in by_obj.values())
    print(f"  API grounding: {n} signature(s) across {len(by_obj)} object(s) "
          f"(~{used / 3700:.1f}k tokens)")
    return ("\n\nBASE-APP API SIGNATURES — these are the ACTUAL declarations from the "
            "downloaded symbols for the objects this handover names. Call them exactly as "
            "written; do not guess parameter types or invent members:\n"
            + "\n".join(lines) + "\n")


def ground_call_signatures(build_text):
    """Answer an argument-type error with the method's REAL signature.

    AL0132 ("does not contain a definition") is already grounded by listing the object's
    members. Its sibling is not: AL0133 says

        Argument 1: cannot convert from 'Text' to 'SecretText'

    without naming the method, the parameter, or what the correct call looks like. The
    model then permutes argument types — the same oscillation seen on InStream/OutStream,
    where one build swapped back and forth for sixteen rounds.

    The signature is a lookup, not a judgement: the symbol index already holds it. On the
    doclink fixture three signatures explain every remaining argument error, including an
    AL0151 that is really "argument 2 is an Enum" —

        CreateSharedKey(SharedKey: SecretText, ApiVersion: Enum "Storage Service API Version")
        GetBlobAsStream(BlobName: Text, TargetInStream: InStream, ...)
        PutBlobBlockBlobStream(BlobName: Text, SourceInStream: InStream, ContentType: Text, ...)

    Only members the index resolves are quoted, and every line carries the package and
    version it came from, so nothing here is a guess about an API.
    """
    idx = _symbol_index()
    if not idx:
        return ""
    import al_symbols      # imported lazily here as in _symbol_index()
    seen, out = set(), []
    for m in _DIAG_POS_RE.finditer(build_text or ""):
        path, lineno = m.group("file"), int(m.group("line"))
        try:
            src = open(path, encoding="utf-8-sig", errors="replace").read().splitlines()
        except OSError:
            continue
        if not (0 < lineno <= len(src)):
            continue
        for cm in _CALL_RE.finditer(src[lineno - 1]):
            name = cm.group("m")
            if name in seen:
                continue
            hits = al_symbols.find_member(idx, name)
            if not hits:
                continue
            seen.add(name)
            h = hits[0]
            out.append(f'- `{name}` on {h["kind"]} "{h["object"]}" is:\n'
                       f'      {h["signature"]}\n'
                       f'    (from {al_symbols.evidence(h)})')
            if len(out) >= 6:
                break
        if len(out) >= 6:
            break
    if not out:
        return ""
    print(f"  RAG: grounded {len(out)} call signature(s) from the symbols")
    return ("\n\nREAL SIGNATURES — the compiler rejected an argument. These are the actual "
            "declarations from the downloaded symbols; match them exactly rather than "
            "trying other types:\n" + "\n".join(out) + "\n")


def kb_ground(names):
    """Look each identifier up in the local KB and return its REAL declaration.

    The kb heading is exactly the ground truth the model got wrong — e.g.
    `codeunit 9047 "ABS Optional Parameters"` for something it declared as a Record.
    Fail-open: no kb, no network, no hits -> empty string, build proceeds unchanged."""
    if not os.path.exists(KB_BIN):
        _note_grounding("unavailable", f"KB_BIN missing at {KB_BIN}")
        return ""
    if not names:
        _note_grounding("available_no_matches", "no unresolved names to ground")
        return ""
    out, unknown = [], []
    for n in names:
        rec = _sym_lookup(n)
        if rec:
            import al_symbols
            out.append(f"- `{n}` → **{al_symbols.declaration(rec)}**  (downloaded symbols)")
            continue
        if not RAG_KB_FALLBACK:
            unknown.append(n)
            continue
        try:
            hits = []
            for _c in RAG_CORPORA:
                r = subprocess.run([KB_BIN, "search", n, "--corpus", _c.strip(),
                                    "-n", str(RAG_HITS), "--json"],
                                   capture_output=True, text=True, timeout=60)
                got = json.loads(r.stdout or "[]")
                if any(_norm(n) == _norm(_decl_name(h.get("heading") or "")) for h in got):
                    hits = got
                    break
        except Exception:
            continue
        for h in hits[:RAG_HITS]:
            head = (h.get("heading") or "").split("›")[0].strip()
            # Only trust a hit whose declaration actually CONTAINS the searched name.
            # Vector search always returns its nearest neighbour, so a name that does
            # not exist in BC comes back as something unrelated (`Document Attachment
            # Mgt` -> `codeunit 132601 "PDF Document Test"`). Presenting that as ground
            # truth would deepen the hallucination instead of correcting it.
            if head and _norm(n) == _norm(_decl_name(head)):
                out.append(f"- `{n}` → **{head}**  (source: {os.path.basename(h.get('path',''))})")
                break
        else:
            unknown.append(n)
    parts = []
    if out:
        parts.append("GROUND TRUTH from the Business Central source — these are the REAL "
                     "declarations of the names the compiler could not resolve. Use these "
                     "exact object types and names; do not guess:\n" + "\n".join(out))
    if unknown:
        # Saying so is itself useful: it stops the model re-guessing a name that is not
        # in the platform at all, which is how it invented these in the first place.
        parts.append("These names do NOT exist anywhere in the Business Central source: "
                     + ", ".join(f"`{u}`" for u in unknown)
                     + ". Do not invent a signature for them — remove the reference or use "
                       "a real object you can name from the source.")
    if not parts:
        return ""
    print(f"  RAG: grounded {len(out)}, flagged {len(unknown)} non-existent "
          f"(of {len(names)})")
    _note_grounding("applied", "name lookups returned declarations", hits=len(parts))
    return "\n\n" + "\n\n".join(parts) + "\n"


def known_fix_hints(build_text):
    """Deterministic repair hints for diagnostics a 30B coder reliably cannot decode.

    First case: AL0282 'parameter X is not found' on a TABLE system event. The rule is
    that subscriber parameter NAMES must match the publisher's — table trigger events
    publish (var Rec: Record <table>; RunTrigger: Boolean). qwen3-coder named the param
    after the table and then burned 6 straight fix rounds (3s each, no edit) because
    nothing told it the fix is a rename. Observed on doclink rpost1, 2026-07-30."""
    hints = []
    for m in re.finditer(r"event subscriber '([^']+)' parameter '([^']+)' is not found",
                         build_text or ""):
        sub, param = m.group(1), m.group(2)
        if re.search(r"On(?:After|Before)(?:Insert|Modify|Delete|Rename)Event", build_text):
            hints.append(
                f"- AL0282 on `{sub}`: subscriber parameter NAMES must exactly match the "
                f"publisher's. Table system events (OnAfterInsertEvent etc.) publish "
                f"`(var Rec: Record <table>; RunTrigger: Boolean)` — RENAME the parameter "
                f"`{param}` to `Rec` (keep its type) and update every use of `{param}` "
                f"inside that procedure to `Rec`. Do not delete the subscriber.")
    # AL0175 on Media/Guid vs Integer: the model is testing emptiness with `= 0` (or
    # invented Media.IsEmpty earlier). Media has no numeric compare and no IsEmpty.
    if re.search(r"AL0175: Operator '[^']+' cannot be applied to operands of type 'Media'",
                 build_text or ""):
        hints.append(
            "- AL0175 on a Media field: Media has NO `IsEmpty` and cannot be compared to a "
            "number. Test emptiness with `.HasValue`: `if not Rec.\"Field\".HasValue then exit;` "
            "(HasValue is the ONLY emptiness check for Media).")
    if re.search(r"AL0175: Operator '[^']+' cannot be applied to operands of type 'Guid'",
                 build_text or ""):
        hints.append(
            "- AL0175 on a Guid: a Guid cannot be compared to a number. Test with "
            "`IsNullGuid(TheGuid)` (built-in function), e.g. `if IsNullGuid(Rec.\"Field\".MediaId) then exit;`.")
    # AL0151: option-member syntax on a type that has no option members. The diagnostic
    # is about the RECEIVER left of `::`, never the member name right of it — which is why
    # the coder never converges: it varies the member (`""`, Empty, None, NoMedia, new())
    # and every variant is equally invalid. 46 recovered sites: 39 Media, 6 Guid, 1 other
    # (reference/al0151-investigation.md). Probe-verified BC28/rt17: Media::"", Media::Empty
    # and Guid::Zero are rejected with AL0151; Clear(field) and IsNullGuid(...) compile.
    #
    # Guarded like the inline-var hint: the diagnostic ALONE is not enough. The blamed line
    # must actually show `Receiver::` — otherwise stay silent rather than tell the model to
    # go looking for a receiver that is not there. Legitimate option syntax (Enum::, an
    # option field) never reaches here, because it does not raise AL0151 in the first place.
    _AL0151_KNOWN = {"media": ("Clear(<the field>)",
                               "a Media field cannot be assigned an empty literal — there "
                               "is none. Clear it with `Clear(Rec.\"Field\")`"),
                     "guid":  ("IsNullGuid(<the guid>)",
                               "a Guid has no empty literal. Test it with "
                               "`IsNullGuid(Rec.\"Field\".MediaId())`")}
    al0151 = []
    for m in re.finditer(r"([^\s(]+\.al)\((\d+),(\d+)\): error AL0151", build_text or ""):
        _p, _ln, _col = m.group(1), int(m.group(2)), int(m.group(3))
        try:
            _lines = open(_p, encoding="utf-8", errors="replace").read().splitlines()
        except OSError:
            continue
        if _ln - 1 >= len(_lines):
            continue
        _src = _lines[_ln - 1]
        # Receiver = the identifier immediately left of `::`, taken from the blamed column
        # where possible so a line with several `::` cannot be misattributed.
        _recv = None
        _left = _src[:_col - 1] if 0 < _col <= len(_src) + 1 else _src
        _m2 = re.search(r'([A-Za-z_]\w*|"[^"]+")\s*::\s*$', _left) or \
              re.search(r'([A-Za-z_]\w*|"[^"]+")\s*::', _src)
        if _m2:
            _recv = _m2.group(1).strip('"')
        if not _recv:
            continue          # no `Receiver::` on the blamed line — say nothing
        _fix, _why = _AL0151_KNOWN.get(_recv.lower(), (None, None))
        al0151.append((os.path.basename(_p), _ln, _recv, _fix, _why))
    for _fn, _ln, _recv, _fix, _why in dict.fromkeys(al0151):
        _msg = (f"- AL0151 at `{_fn}` line {_ln}: `{_recv}::...` — `{_recv}` is NOT an "
                f"Option/Enum type, so it has no members to reach with `::`. The error is "
                f"the RECEIVER, not the member name: renaming the member (`\"\"`, `Empty`, "
                f"`None`, `new()`) cannot fix it, because none of them exist.")
        if _fix:
            _msg += f" Here {_why} — use `{_fix}`."
        else:
            _msg += (" Remove the `::` expression and use the type's own API instead; do "
                     "not invent a literal for it.")
        hints.append(_msg)
    # AL0133 InStream<->OutStream: streams are directional; the model passes one where
    # the other is required, then swaps back and forth for 16 rounds (doclink r2).
    if re.search(r"AL0133: .*cannot convert from '(?:var )?(?:In|Out)Stream' to "
                 r"'(?:var )?(?:In|Out)Stream'", build_text or ""):
        hints.append(
            "- AL0133 InStream/OutStream: streams are DIRECTIONAL — read APIs take `var "
            "InStream` (e.g. `ABSBlobClient.GetBlobAsStream(Name, InStr)`), write APIs "
            "take an OutStream. Never pass one as the other. To move data between them, "
            "put a `Codeunit \"Temp Blob\"` in the middle: `TempBlob.CreateOutStream("
            "OutStr); <write into OutStr>; TempBlob.CreateInStream(InStr); <read from "
            "InStr>` — and copy with `CopyStream(DestOutStream, SrcInStream)`.")
    # try/except — Python/C# exception syntax. AL has NO `try` and NO `except` keyword,
    # so the parser dies at the block and cascades (suite5 doclink r3: 12 errors from one
    # try block, frozen 16 rounds). Detected in the SOURCE, not the diagnostics: the
    # compiler only reports the downstream "Semicolon expected", which names nothing.
    try_files = []
    for _dp, _, _fs in os.walk(PROJECT_ROOT + "/src"):
        for _fn in _fs:
            if not _fn.endswith(".al"):
                continue
            _p = os.path.join(_dp, _fn)
            try:
                _src = open(_p, encoding="utf-8", errors="replace").read()
            except OSError:
                continue
            if re.search(r"^\s*(try|except)\s*$", _src, re.M):
                try_files.append(os.path.basename(_p))
    if try_files:
        hints.append(
            f"- `try` / `except` blocks in {', '.join('`'+f+'`' for f in try_files[:3])}: "
            "AL has NO try/except keywords — this is Python/C# syntax and breaks the "
            "parser. Remove the block. To handle a failure in AL either (a) mark a "
            "procedure `[TryFunction]` (no return type — it implicitly returns Boolean) "
            "and call it as `if not MyTryProc(...) then <handle>;`, or (b) check the "
            "operation's own result, e.g. "
            "`if not ABSOperationResponse.IsSuccessful() then exit(false);`. "
            "Keep the statements that were inside the block — just unwrap them.")
    # Mid-body variable declaration. AL has no inline `var`, and the compiler never says
    # so: the parser derails AT the declaration and reports the block terminator as
    # missing, so the message names `end`/`until` and points nowhere useful. Observed
    # doclink 2026-09-01 — a snippet-fix invented `var ApiVersionEnum: Enum ...` mid-body
    # to dodge an AL0151, producing 31x AL0104 + 15x AL0107 from ONE line, then five
    # file-rewrites reproduced it byte-identically because nothing named the cause.
    #
    # Anchored on the diagnostic AND confirmed in the source: a bare `var` opening a real
    # declaration section is legal, so the hint only fires when the line the compiler
    # blamed actually carries a name on it.
    inline_var = []
    for m in re.finditer(r"([^\s(]+\.al)\((\d+),\d+\): error AL0104: Syntax error, "
                         r"'(?:end|until|;)' expected", build_text or ""):
        _p, _ln = m.group(1), int(m.group(2))
        try:
            _lines = open(_p, encoding="utf-8", errors="replace").read().splitlines()
        except OSError:
            continue
        if _ln - 1 >= len(_lines):
            continue
        _src_line = _lines[_ln - 1]
        if re.match(r'^\s*var\s+["A-Za-z_]', _src_line):
            inline_var.append((os.path.basename(_p), _ln, _src_line.strip()))
    for _fn, _ln, _txt in dict.fromkeys(inline_var):
        hints.append(
            f"- AL0104 at `{_fn}` line {_ln} is NOT a missing keyword. The line is a "
            f"variable declaration sitting mid-body:\n"
            f"    {_txt}\n"
            f"  AL has NO inline declaration. MOVE this declaration into the `var` section "
            f"between the procedure signature and its `begin` (keep the name and type "
            f"exactly), and leave only the assignment where the declaration was. Every "
            f"AL0107 'identifier expected' after this line is the same one defect — they "
            f"disappear together. Do not add or remove any `end`/`until`: the keywords "
            f"already balance.")
    # AL-12: the hints above are DYNAMIC — they read the actual parameter names and file
    # names out of this build. The KB adds static background for whatever else is in the
    # log. Both sit alongside the compiler's own text; neither replaces it.
    kb = ""
    try:
        kb = al_errors.context_for(build_text, bc_version=AL_CTX.get("bc_version"))
    except Exception:
        kb = ""
    if not hints:
        return kb
    return ("\n\nKNOWN FIXES — these diagnostics have a mechanical fix; apply it exactly:\n"
            + "\n".join(dict.fromkeys(hints)) + "\n" + kb)


# Parser/structure diagnostics: a brace/until/semicolon break that cascades. One real
# defect, dozens of downstream errors, and no single SEARCH/REPLACE can restructure it.
SYNTAX_CODES = {"AL0104", "AL0107", "AL0111", "AL0114", "AL0198", "AL0224", "AL0227",
                "AL0128", "AL0230", "AL0009"}


def cascade_files(build_text):
    """Files whose diagnostics are dominated by parser errors — structurally broken.
    suite4: newstack doclink r1/r2 froze 8 rounds at 9-14 errors because snippet edits
    cannot restructure a broken repeat/until, while the full-project rewrite regressed
    the healthy files. The right tool is a rewrite of JUST the broken file(s)."""
    per = {}
    for m in re.finditer(r"([^\s(]+\.al)\(\d+,\d+\): error ((?:AL|PTE|AA|AS)\d+)",
                         build_text or ""):
        f, code = m.group(1), m.group(2)
        tot, syn, hard = per.get(f, (0, 0, False))
        per[f] = (tot + 1, syn + (1 if code in SYNTAX_CODES else 0),
                  hard or code in ("AL0104", "AL0198"))
    # AL0104 ("syntax error, X expected") / AL0198 ("object keyword expected") are
    # ALWAYS structural — suite5 p4 r2 sat 16 rounds on a file with exactly TWO such
    # errors because the old >=3 threshold routed it to snippet. Any occurrence of
    # either code marks the file broken; the volume rule catches the other parser codes.
    return [f for f, (tot, syn, hard) in per.items()
            if hard or (syn >= 3 and syn * 2 >= tot)]


def handover_file_spec(handover_text, path):
    """The handover's verbatim Strategy-A content block for one file, if it has one —
    then the rewrite becomes re-transcription instead of re-authoring."""
    base = re.escape(os.path.basename(path))
    m = re.search(r"^#+ *\d+\.[^\n]*" + base + r".*?```[^\n]*\n(.*?)```",
                  handover_text or "", re.S | re.M)
    return m.group(1) if m else ""


def build_file_rewrite_msg(handover_text, path, file_errors, hints=""):
    """Targeted single-file rewrite prompt for a structurally broken file.

    `hints` carries the known-fix guidance: without it the model re-reads its own
    broken file and faithfully reproduces the defect. Observed suite5 doclink r3 —
    16 consecutive rewrites, error score frozen at 12, because the real cause
    (a `try`/`except` block, which AL does not have) was never named."""
    spec = handover_file_spec(handover_text, path)
    msg = (
        f"The file `{path}` is structurally broken — the AL parser cannot recover "
        f"(unbalanced begin/end, repeat/until or braces, or a construct AL does not "
        f"have). Its compile errors:\n\n{file_errors}\n"
    )
    if hints:
        msg += (f"\nThe cause is known — apply this exactly:\n{hints}\n")
    msg += (
        f"\nRewrite this ONE file completely with the write tool:\n"
        f"- Read the current file first to preserve its intent, object id and object name.\n"
        f"- Produce a complete, syntactically valid AL file (every begin has an end, every "
        f"repeat has an until, braces balance).\n"
        f"- Use ONLY AL constructs. AL has no try/except, no throw, no switch, no `{{ }}` "
        f"statement blocks — use begin/end, case-of, and [TryFunction].\n"
        f"- Declare EVERY variable in a `var` section between the signature and `begin`. "
        f"AL has NO inline declaration: a `var` sitting between `begin` and `end` derails "
        f"the parser, which then reports a missing `end`/`until` many lines away.\n"
        f"- Do NOT touch, create or delete any other file.\n"
    )
    if spec:
        msg += (f"\nThe project spec defines this file's intended content — follow it "
                f"closely:\n```\n{spec}\n```\n")
    return msg


def build_fix_msg(review_findings):
    listing = get_project_file_listing()
    return (
        f"Project root: {PROJECT_ROOT}/\n\n"
        f"Current source files:\n{listing}\n\n"
        f"---\n\n"
        f"The code review found the following issues that must be fixed:\n\n"
        f"{review_findings}\n\n"
        f"---\n\n"
        f"Instructions:\n"
        f"- If a finding says a file is MISSING, CREATE that file (it is part of the spec — write it with the write tool).\n"
        f"- For other errors, read the affected file and fix only the listed issue, then write it back.\n"
        f"- Do NOT create files that are not in the manifest. Do NOT change files that have no issues listed. "
        f"Do NOT delete any file.\n"
        f"\n"
        f"Repair discipline — surgical edits only:\n"
        f"- Only modify the lines involved in the reported errors.\n"
        f"- Never rename a procedure that already works.\n"
        f"- Never change an object ID.\n"
        f"- Preserve all working code — do not rewrite or reformat code that has no listed issue.\n"
        f"- Minimise edits: the smallest change that clears the error."
    )


def build_missing_files_msg(handover_text, missing):
    """Focused recovery prompt: write ONLY the missing manifest files. A weak coder
    that drops the tail of the manifest (writes 6/8) reliably ignores 'create the
    missing file' when it is buried in a full-project fix message; a narrowed,
    completable task ('write just these N files, already specified above') recovers
    them. Write-capable by nature — snippet/SEARCH-REPLACE cannot create a new file."""
    lst = "\n".join(f"- {m}" for m in missing)
    return (
        f"{handover_text}\n\n"
        f"---\n\n"
        f"These manifest files were NOT written and are still missing:\n{lst}\n\n"
        f"Write ONLY these {len(missing)} missing file(s) with the write tool, exactly as "
        f"specified in the handover above (they are fully specified there). "
        f"Do NOT touch, rewrite, or delete any file that already exists."
    )


# WORKFLOW=incremental knobs. A sweep is one pass over the pending files; a second
# sweep exists so a file deferred for a not-yet-written dependency gets its turn once
# that dependency lands.
INCR_MAX_SWEEPS = int(os.environ.get("INCR_MAX_SWEEPS", "3"))
# Parity with MAX_WRITE_ATTEMPTS on the single-shot path. Its absence was not a
# tuning gap: one hallucinated write on the FIRST file left sweep 1 with zero
# progress, which stalls the ratchet by design and dumps every file into the bulk
# fallback. 6 of 7 runs in the first A/B died that way, so the challenger arm never
# exercised the architecture it was meant to test.
INCR_WRITE_ATTEMPTS = int(os.environ.get("INCR_WRITE_ATTEMPTS", "3"))

# Object kinds in dependency order. Probed: `table` alone compiles; `page` alone with its
# table missing does not (AL0118/AL0185); both together do. Ordering cannot fix
# intra-type or reverse references — that is what deferral is for — but it makes most
# files compile on their first attempt instead of their second.
_INCR_RANK = {
    "Enum": 0, "Interface": 0, "ControlAddin": 0,
    "Table": 1, "TableExt": 2, "EnumExt": 2,
    "Codeunit": 3,
    "Page": 4, "PageExt": 5, "Report": 6, "Query": 6, "XmlPort": 6,
    "PermissionSet": 9,          # references every other object, so it must be last
    "Other": 7,
}

# `codeunit 50100 "Name"`, and also the id-less forms a handover uses everywhere else:
# an id-allocation table (`` `codeunit "Name"` | 50102 ``) and permission set bodies
# (`codeunit "Name" = X`). Requiring the id found only 5 of this fixture's 9 objects, so
# the four it missed were REVERTED on an AL0185 that should have been a DEFER.
_DECL_RE = re.compile(
    r'\b(?:table|tableextension|page|pageextension|codeunit|enum|enumextension|query|'
    r'xmlport|report|interface|permissionset|controladdin)\s+(?:\d+\s+)?"([^"]+)"',
    re.IGNORECASE)
# AL0185: Codeunit 'X' is missing   (X may be namespace-qualified)
_MISSING_RE = re.compile(r"error AL0185: \w+ '([^']+)' is missing")
# AL0118: The name 'X' does not exist in the current context.
_NONAME_RE = re.compile(r"error AL0118: The name '\"?([^'\"]+)\"?' does not exist")
# PTE0004: Table 50103 'X' is missing a matching permission set.
# PerTenantExtensionCop demands a permission set covering every table the extension
# adds. In a partial tree that is guaranteed until the permission set is written, and
# the permission set must come LAST because it references every other object. Without
# treating this as an ordering artefact the ratchet deadlocks: observed on the first
# smoke run, where the very first table reverted on PTE0004 alone and nothing could
# ever go green.
_PERMSET_RE = re.compile(r"error PTE0004: \w+ \d+ '([^']+)' is missing a matching permission set")


def _dependency_rank(path):
    return (_INCR_RANK.get(object_type(path), 7), os.path.basename(path).lower())


def _declared_object_names(handover_text):
    """Every object name this project intends to declare, per the handover.

    Used to tell "you referenced an object that does not exist" (a real error, revert)
    from "you referenced an object this build has not written YET" (defer and retry).

    Base-app names are excluded via the symbol index: the id-less pattern also matches
    things like `extends "Document Attachment"`, and treating Microsoft's objects as
    "ours, coming later" would defer a genuine missing-`using` forever. This project's own
    objects are never in the index — they have not been compiled into a .app — so the
    exclusion is exact rather than a heuristic.
    """
    names = {m.group(1).strip().lower() for m in _DECL_RE.finditer(handover_text or "")}
    try:
        import al_symbols          # imported per-call, as the other call sites do
        idx = _symbol_index()
        if idx:
            names = {n for n in names if not al_symbols.lookup(idx, n)}
    except Exception:
        pass          # fail open: a slightly wide set only costs an extra sweep
    return names


def _deferrable(build_text, declared, written_paths):
    """True when EVERY error is a reference to an object the project will declare later.

    Conservative on purpose: one error outside that set means the file is genuinely
    broken and reverting it is correct. A partially-written tree makes AL0185/AL0118 the
    expected, benign case, so treating them as failures would reject good files for the
    crime of being written in the wrong order.
    """
    errs = re.findall(r"error (?:AL|AW|PTE)\d+: .*", build_text or "")
    if not errs:
        return False
    already = set()
    for wp in written_paths:
        try:
            already |= {m.group(1).strip().lower()
                        for m in _DECL_RE.finditer(open(wp, encoding="utf-8-sig",
                                                        errors="replace").read())}
        except OSError:
            pass
    permset_pending = any(object_type(f) == "PermissionSet" and f not in written_paths
                          for f in EXPECTED_FILES)
    for e in errs:
        if permset_pending and _PERMSET_RE.search(e):
            continue                            # resolved when the permission set lands
        m = _MISSING_RE.search(e) or _NONAME_RE.search(e)
        if not m:
            return False
        name = m.group(1).strip().strip('"').lower()
        name = name.rsplit(".", 1)[-1]          # drop a namespace qualifier
        if name not in declared or name in already:
            return False                        # not ours, or ours and already written
    return True


def _permset_only(build_text, written_paths):
    """True when the ONLY thing wrong is that the permission set has not been written yet.

    Distinct from _deferrable on purpose. A deferred file is DELETED and retried, which is
    right when it references something missing. PTE0004 is the opposite case: the file
    itself is fine and a LATER file fixes it, so deleting it would be destructive — and
    since the permission set must reference every table, deleting the tables makes the
    permission set unwritable. Keep the file and let the cop clear when the set lands.
    """
    errs = re.findall(r"error (?:AL|AW|PTE)\d+: .*", build_text or "")
    if not errs:
        return False
    if not any(object_type(f) == "PermissionSet" and f not in written_paths
               for f in EXPECTED_FILES):
        return False
    return all(_PERMSET_RE.search(e) for e in errs)


def build_single_file_msg(handover_text, path, remaining):
    """Write exactly ONE file. The whole point of the ratchet is that the model is never
    asked to hold nine files in its head at once.

    Order matters and cost a smoke run to learn: with the directive FIRST and the handover
    appended after it, the model replied in chat and wrote nothing (6s, exit 0, no tool
    call). The handover carries the filesystem-tool rules, and it ends with "You have
    written all 8 files in the manifest. STOP." — so appending it after the instruction
    both buried the tool contract and closed with a stop order. The handover now comes
    first as context, and the actionable directive comes last.
    """
    spec = handover_file_spec(handover_text, path)
    msg = (
        # MUST NOT start with "-": pi parses a leading-dash argv as a CLI flag and dies
        # with `Error: Unknown option: --- PROJECT HANDOVER ...` (exit 1, ~1s, nothing
        # written). Keep a plain-text first line.
        f"INCREMENTAL BUILD — one file per turn.\n\n"
        f"=== PROJECT HANDOVER (context — read the filesystem tool rules in it) ===\n\n"
        f"{handover_text}\n\n"
        f"=== YOUR TASK, WHICH REPLACES THE 'write all files' INSTRUCTION ABOVE ===\n\n"
        f"This is an INCREMENTAL build. Ignore the handover's instruction to write every "
        f"file. Write exactly ONE file this turn:\n\n"
        f"    {path}\n\n"
        f"The project is compiled after every single file and a file that does not compile "
        f"is thrown away, so write this one completely and correctly.\n\n"
        f"Files that already exist (do NOT touch them):\n{get_project_file_listing()}\n\n"
        f"Files still to come in LATER turns — do NOT create them now, and do not be "
        f"concerned that they are missing:\n"
        + "".join(f"  {os.path.basename(r)}\n" for r in remaining) + "\n"
        f"Rules:\n"
        f"- USE THE WRITE TOOL to create the file on disk at exactly that absolute path. "
        f"Do NOT print the file content as your reply — a reply that is not a tool call "
        f"writes nothing and the turn is wasted.\n"
        f"- Create ONLY that one file. Do not create, edit or delete any other.\n"
        f"- It must be a complete, compilable AL object.\n"
        f"- `namespace` first, then `using` lines, then the object. Never put `using` "
        f"inside the object body.\n"
        f"- Use the object id and name the handover assigns to this file.\n"
    )
    if spec:
        msg += (f"\nThe handover defines this file's content — follow it:\n"
                f"```\n{spec}\n```\n")
    return msg


def incremental_build(handover_text):
    """Write one object at a time, compiling after each; keep it only if the tree is green.

    Returns (green, unresolved, stats). Files that never go green are NOT fatal — they
    are left to the bulk fallback and the existing fix loop, mirroring run-edit's PARTIAL
    outcome rather than failing the build outright.
    """
    print("\n--- Clear project ---")
    clear_project()
    write_canonical_app_json()

    declared = _declared_object_names(handover_text)
    pending = sorted([f for f in EXPECTED_FILES if f.endswith(".al")], key=_dependency_rank)
    n_objects = len(pending)
    print(f"\n--- Incremental ratchet: {n_objects} object(s) ---")
    print("  order: " + ", ".join(os.path.basename(f) for f in pending))

    green = []
    stats = {"sweeps": 0, "deferred": 0, "reverted": 0, "stalled": False}

    for sweep in range(1, INCR_MAX_SWEEPS + 1):
        if not pending:
            break
        stats["sweeps"] = sweep
        print(f"\n--- sweep {sweep}: {len(pending)} pending ---")
        progress, requeue = False, []
        for path in pending:
            base = os.path.basename(path)
            others = [x for x in pending if x != path]
            msg = build_single_file_msg(handover_text, path, others)
            reply = ""
            for attempt in range(1, INCR_WRITE_ATTEMPTS + 1):
                reply = run_coder(msg, label=f"incr:{base}"
                                  + (f" (attempt {attempt})" if attempt > 1 else ""),
                                  timeout=WRITE_TIMEOUT)
                if os.path.exists(path):
                    break
                # The model reports success it did not achieve: observed verbatim,
                # "I've successfully created the file ... written to the correct
                # location at <path that does not exist>", exit 0, no tool call. A
                # generic retry just produces another narration, because as far as the
                # model is concerned the task is done. Contradict it with the
                # filesystem result, which is the only authority here.
                msg = (f"STOP. Your previous response claimed this file was written:\n\n"
                       f"    {path}\n\n"
                       f"That claim has been checked against the filesystem. The file "
                       f"does NOT exist. No write tool call was recorded. The task is "
                       f"NOT complete, and describing the file again will not create "
                       f"it.\n\n"
                       f"Call an available write tool now and create that exact "
                       f"absolute path. Then stop.\n\n" + msg)
            if os.path.exists(path) and attempt > 1:
                # Recovered. Distinct from "never failed" and from "failed for good":
                # a run where retries repaired every false success claim is still
                # interpretable as an architecture test, whereas an exhausted failure
                # means the ratchet never ran. Counting only exhaustion would collapse
                # those two into one number.
                print(f"  {base}: write recovered on attempt {attempt} "
                      f"(the first {attempt - 1} claimed success falsely)")
                stats["write_recovered"] = stats.get("write_recovered", 0) + 1
                stats["write_retries"] = stats.get("write_retries", 0) + (attempt - 1)

            if not os.path.exists(path):
                stats["write_retries"] = (stats.get("write_retries", 0)
                                          + INCR_WRITE_ATTEMPTS - 1)
                # Keep the evidence. Discarding run_coder's return value is why a
                # hallucinated write was invisible across seven runs of logs and took a
                # manual reproduction to find.
                snippet = " ".join((reply or "").split())[:400]
                print(f"  {base}: NOT WRITTEN after {INCR_WRITE_ATTEMPTS} attempt(s)")
                print(f"      model said: {snippet or '(no output)'}")
                stats["write_failed"] = stats.get("write_failed", 0) + 1
                requeue.append(path)
                continue

            build_text, build_ok = run_al_compile()
            errs = count_build_errors(build_text, build_ok)
            if build_ok and errs == 0:
                print(f"  {base}: GREEN ({len(green) + 1}/{n_objects})")
                green.append(path)
                progress = True
            elif _permset_only(build_text, green):
                print(f"  {base}: GREEN ({len(green) + 1}/{n_objects}) "
                      f"— pending permission set (PTE0004 clears when it is written)")
                green.append(path)
                progress = True
            elif _deferrable(build_text, declared, green):
                print(f"  {base}: DEFER (waits on an object not written yet)")
                os.remove(path)
                stats["deferred"] += 1
                requeue.append(path)
            else:
                print(f"  {base}: REVERT ({errs} error(s))")
                os.remove(path)
                stats["reverted"] += 1
                requeue.append(path)
        pending = requeue
        if pending and not progress:
            print(f"  no file went green this sweep — stopping the ratchet")
            stats["stalled"] = True
            break

    # Stall fallback: whatever the ratchet could not place is written in one call and
    # handed to the existing fix loop. This mode can therefore never be worse than the
    # single-shot path — at worst it degrades into it for the leftovers.
    if pending:
        print(f"\n--- Bulk fallback: {len(pending)} file(s) the ratchet could not place ---")
        msg = (
            f"Write these files, and ONLY these:\n"
            + "".join(f"  {q}\n" for q in pending)
            + f"\nThese files already exist and are correct — do NOT modify or delete "
              f"them:\n" + "".join(f"  {g}\n" for g in green)
            + f"\n--- PROJECT HANDOVER ---\n\n{handover_text}\n"
        )
        run_coder(msg, label="incr:bulk-fallback", timeout=WRITE_TIMEOUT)
        stats["stall_fallback"] = True

    print(f"\n  ratchet: {len(green)} green, {len(pending)} left to the fix loop "
          f"({stats['deferred']} deferral(s), {stats['reverted']} revert(s), "
          f"{stats['sweeps']} sweep(s))")
    return green, pending, stats


def decomposed_plan(handover_text):
    """WORKFLOW=decomposed: a short read-only planning chain run BEFORE generation —
    analyse -> list objects -> list referenced symbols. The result is prepended to the
    generation prompt so the coder writes against an explicit plan.

    The MANIFEST is deliberately NOT model-generated: it stays the handover's contract
    (it gates the write and defines 'done'). The 'objects' step is cross-checked against
    the manifest, never a replacement — the model must not grade its own homework.
    Symbols are DECLARED here and remain compiler-verified downstream (the global symbol
    download + al compile are still ground truth); this step just surfaces them early."""
    print("\n--- Decomposed pre-flight (analyse -> objects -> symbols) ---")
    analysis = run_pi(
        "Analyse this AL extension project. In 5-10 bullets: its purpose, the BC objects "
        "it extends/depends on, and the main implementation risks. Do not write code.\n\n"
        + handover_text, label="plan-analyse", allow_write=False)
    objects = run_pi(
        "List every AL object this project must DEFINE (type, name, id), one per line. "
        "Base it strictly on the manifest and specs in the handover — do not invent objects.\n\n"
        + handover_text + "\n\nAnalysis:\n" + analysis,
        label="plan-objects", allow_write=False)
    symbols = run_pi(
        "List the EXTERNAL objects (tables, pages, codeunits, enums from the Microsoft/base "
        "app or declared dependencies) this code will REFERENCE — one 'ObjectType Name' per "
        "line. These must resolve at compile time. Do not list objects this project defines.\n\n"
        + handover_text + "\n\nObjects to build:\n" + objects,
        label="plan-symbols", allow_write=False)
    print(f"  plan built — analysis {len(analysis)}c, objects {len(objects)}c, symbols {len(symbols)}c")
    return (
        "## Pre-flight plan (follow this when writing the files)\n\n"
        f"### Analysis\n{analysis}\n\n"
        f"### Objects to define (must match the manifest)\n{objects}\n\n"
        f"### External symbols referenced (must resolve at compile time)\n{symbols}\n"
    )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    try:
        sys.stdout.reconfigure(line_buffering=True)  # live progress in nohup logs
    except Exception:
        pass
    t0 = time.time()
    args = sys.argv[1:]
    skip_larry  = "--skip-larry"  in args
    review_only = "--review-only" in args
    review_peer = "--review"      in args   # coms validator-peer behaviour review after PASS

    project = DEFAULT_PROJECT
    if "--project" in args:
        i = args.index("--project")
        if i + 1 >= len(args):
            print("ERROR: --project requires a path argument.")
            sys.exit(1)
        project = args[i + 1]
    configure_project(project)
    # What this run was asked to do — recorded before anything can drift.
    declare_config(backend=CODER_BACKEND, model=CODER_MODEL,
                   max_fix_rounds=MAX_FIX_ROUNDS, inject_topics=INJECT_TOPICS,
                   inject_budget_k=INJECT_BUDGET_K, write_timeout=WRITE_TIMEOUT,
                   fix_timeout=FIX_TIMEOUT,
                   escalate_after=ESCALATE_AFTER, escalate_mid_after=ESCALATE_MID_AFTER)
    check_model_matches_rundir()
    if not EXPECTED_FILES:
        print("ERROR: could not read expected files from handover manifest. Aborting.")
        sys.exit(1)
    backend_bin = CLAUDE_BIN if CODER_BACKEND == "claude" else PI_BIN
    if not os.path.exists(backend_bin):
        print(f"ERROR: coder backend '{CODER_BACKEND}' not found at {backend_bin}.")
        sys.exit(1)
    egress_ok, egress_reason = egress_policy.escalation_available()
    if CODER_BACKEND == "claude" and not egress_ok:
        print(f"ERROR: CODER_BACKEND=claude but {egress_reason}. Use CODER_BACKEND=pi (Larry).")
        sys.exit(1)
    print(f"Coder backend: {CODER_BACKEND}" + (f" ({CODER_MODEL})" if CODER_BACKEND == "pi" else " (Claude Code, Pro sub)"))
    if ESCALATE_AFTER is not None and CODER_BACKEND == "pi":
        if not egress_ok:
            globals()["ESCALATE_AFTER"] = None   # policy forbids egress: never latch to Claude
            print(f"Escalation: DISARMED by egress policy — {egress_reason}. Build stays on Larry.")
        elif not os.path.exists(CLAUDE_BIN):
            print(f"ERROR: ESCALATE_AFTER set but Claude bin not found at {CLAUDE_BIN}.")
            sys.exit(1)
        else:
            via = (" via anon mirror" if egress_policy.policy() == "enterprise-anon" else "")
            print(f"Escalation: ARMED — pi does {ESCALATE_AFTER} fix round(s), then Claude Code closes{via} (billed per-token).")
    else:
        print("Escalation: off (manual — set ESCALATE_AFTER=N to auto-hand stalled builds to Claude).")

    # Mid-tier arming (independent of the Claude rung; disarmed unless the policy
    # permits the openrouter target). Requires ESCALATE_MID_AFTER < ESCALATE_AFTER
    # so the ladder doesn't invert; if only the mid rung is armed the ladder is
    # pi -> mid -> STOP (never Claude).
    if ESCALATE_MID_AFTER is not None and CODER_BACKEND == "pi":
        mid_ok, mid_reason = egress_policy.mid_available()
        if not mid_ok:
            globals()["ESCALATE_MID_AFTER"] = None
            print(f"Mid tier: DISARMED by egress policy — {mid_reason}. Build stays on Larry.")
        elif ESCALATE_AFTER is not None and ESCALATE_MID_AFTER >= ESCALATE_AFTER:
            globals()["ESCALATE_MID_AFTER"] = None
            print(f"Mid tier: DISARMED — ESCALATE_MID_AFTER ({_escm}) must be < ESCALATE_AFTER "
                  f"({ESCALATE_AFTER}); ignoring the mid rung.")
        else:
            print(f"Mid tier: ARMED — pi does {ESCALATE_MID_AFTER} round(s), then {MID_MODEL} "
                  f"(cloud-billed via OpenRouter)" +
                  (f", then Claude at round {ESCALATE_AFTER}." if ESCALATE_AFTER is not None
                   else " (no Claude rung — pi→mid→stop)."))

    # ---- Pre-warm the coder so a cold ROCm load doesn't eat the write timeout ----
    if not review_only:
        prewarm_coder()

    # ---- Write phase -------------------------------------------------------
    # Read up-front: the fix loop's missing-file recovery needs the spec even when
    # the write phase is skipped (--skip-larry / --review-only).
    handover_text = read_handover()
    # The project's OWN words, kept before we append anything to the prompt. Topic
    # selection must score this and not the BCQuality/API text we add below — see
    # select_topics.
    _spec_text = handover_text
    _incr_stats = {}          # populated only when WORKFLOW=incremental
    _green, _left = [], []

    if not skip_larry and not review_only:
        # Fold BCQuality authoring rules into the coder prompt (fail-open: no clone → no change).
        try:
            import bcquality
            _guide = bcquality.coder_checklist(handover_text,
                                               bc_version=AL_CTX.get('bc_version'))
            if _guide:
                handover_text += "\n\n" + _guide
                print(f"  BCQuality: appended authoring rules to handover "
                      f"({_guide.count('[rule:')} rules)")
        except Exception as _e:
            print(f"  BCQuality: coder-inject skipped ({_e})")
        # Phase 1b: the API signatures this handover will need, BEFORE the first write.
        try:
            _apis = ground_handover_apis(handover_text)
            if _apis:
                handover_text += _apis
        except Exception as _e:
            print(f"  API grounding skipped ({_e})")
        # Put the AL rule knowledge IN the prompt rather than trusting the model to
        # go and read it. This is the single biggest measured win (5/10 -> 9/12 passes).
        _topics = []
        if INJECT_TOPICS and INJECT_TOPICS.lower() not in ("off", "none", "0"):
            if INJECT_TOPICS.lower() == "auto":
                # Select against what ctx-guard will actually let through: the prompt
                # already carries the handover, BCQuality rules and API grounding, and
                # only the remainder is available for topics. Scoring the raw spec,
                # budgeting against the assembled prompt — two different questions.
                _headroom = ctx_budget_k() - len(handover_text) / 3700.0
                _topics, _est = select_topics(EXPECTED_FILES, _spec_text, budget_k=_headroom)
            else:
                _topics = [t.strip() for t in INJECT_TOPICS.split(",") if t.strip()]
        _parts = []
        for _t in _topics:
            _fp = os.path.join(REPO_REFERENCE, "al-reference",
                               _t if _t.endswith(".md") else _t + ".md")
            try:
                _parts.append(open(_fp, encoding="utf-8").read())
            except OSError:
                print(f"  inject: topic not found: {_t}")
        _base_handover = handover_text
        if _parts:
            _blob = "\n\n".join(_parts)
            print(f"  inject: {', '.join(_topics)}  (~{len(_blob)/3700:.1f}k tokens)")
            # After ctx-guard, not before: what the model actually receives is the
            # observation that matters. Recording the selection here would have called
            # injab verified.
            observe_config(topics_injected=list(_topics))
            handover_text = ("# AL rules you MUST follow (from AL-REFERENCE)\n\n"
                             + _blob + "\n\n---\n\n" + handover_text)

        # Context-budget guard — now a BACKSTOP, not the real budget. select_topics is
        # given this same ceiling minus the rest of the prompt, so it should never choose
        # more than fits. If this still fires, the estimate drifted (injection is measured
        # before the AL-rules header and separators are added) or something appended to the
        # prompt after selection: either way it is worth seeing, so it stays loud.
        NUM_CTX = CODER_NUM_CTX
        budget_k = ctx_budget_k()
        est_k = len(handover_text) / 3700.0
        if est_k > budget_k and _parts:
            while _parts and len(_topics) > 1 and est_k > budget_k:
                dropped = _topics.pop()
                _parts.pop()
                handover_text = ("# AL rules you MUST follow (from AL-REFERENCE)\n\n"
                                 + "\n\n".join(_parts) + "\n\n---\n\n" + _base_handover)
                est_k = len(handover_text) / 3700.0
                print(f"  ctx-guard: dropped injected topic {dropped} (~{est_k:.1f}k tokens now)")
        if est_k > budget_k:
            print(f"  ⚠ ctx-guard: write prompt ~{est_k:.1f}k tokens vs ~{budget_k:.0f}k budget "
                  f"(num_ctx {NUM_CTX}) — expect truncation/wedge. Split the handover "
                  f"(fewer verbatim files per build) or raise num_ctx.")

        # Optional decomposed pre-flight: prepend an analyse->objects->symbols plan.
        if WORKFLOW == "decomposed":
            try:
                handover_text = decomposed_plan(handover_text) + "\n\n---\n\n" + handover_text
            except Exception as _e:
                print(f"  Decomposed pre-flight skipped ({_e}) — falling back to single-pass.")

        if WORKFLOW == "incremental":
            _green, _left, _incr_stats = incremental_build(handover_text)
            write_canonical_app_json()
        elif VERBATIM_WRITE:
            print("\n--- Clear project ---")
            clear_project()
            print("\n--- Verbatim write: writing files directly from handover blocks (no coder) ---")
            written, nblocks = verbatim_write()
            write_canonical_app_json()   # up front so the first manifest check doesn't flag it missing
            print(f"  Wrote {written}/{len(EXPECTED_FILES)} manifest files verbatim "
                  f"({nblocks} block(s) parsed) + canonical app.json.")
            if written < len(EXPECTED_FILES) - 1:   # allow app.json to be block-less
                print("  WARNING: fewer verbatim blocks than manifest files — the handover may not be "
                      "fully Strategy A. Missing files fall to the fix-loop recovery.")
        else:
            larry_ok = False
            for attempt in range(1, MAX_WRITE_ATTEMPTS + 1):
                print(f"\n--- Clear project (attempt {attempt}) ---")
                clear_project()
                print(f"\n--- Larry: writing files (attempt {attempt}) ---")
                run_coder(handover_text, label="Larry-write", timeout=WRITE_TIMEOUT)
                written = sum(1 for f in EXPECTED_FILES if os.path.exists(f))
                print(f"  Wrote {written}/{len(EXPECTED_FILES)} expected files.")
                if written >= len(EXPECTED_FILES) // 2:
                    larry_ok = True
                    break
                # Fail fast on a wedge. A coder that hit its full timeout AND wrote nothing
                # has not "written too few files" — it never got going, and the two retries
                # cost another 2 x WRITE_TIMEOUT to reach the same place. Measured
                # 2026-08-30: a wedged doclink run burned 3600s across three identical
                # 1200s hangs, all 0/9, and turned one bad run into a two-hour hole in a
                # suite. A timeout WITH partial output still retries — that is a coder that
                # ran and was cut off, which is a different thing and does recover.
                if wedged_write(written, coder.LAST["timed_out"], attempt):
                    print(f"  Coder hit the full {WRITE_TIMEOUT}s timeout and wrote nothing — "
                          f"wedged, not slow. Abandoning after attempt {attempt} of "
                          f"{MAX_WRITE_ATTEMPTS} rather than repeating it "
                          f"({(MAX_WRITE_ATTEMPTS - attempt) * WRITE_TIMEOUT}s saved).")
                    break
                print("  Too few files written. Retrying...")
            if not larry_ok:
                print(f"\nERROR: Larry failed to write files after {MAX_WRITE_ATTEMPTS} attempts.")
                # Record it. This exit path used to leave NO metrics row at all, so the
                # worst failure a model can have — not producing files — was invisible to
                # every downstream measure, and a model that failed this way scored
                # better than one that wrote something broken. Observed on suite7:
                # al-coder-qwen36 lost all three doclink runs to this and they simply did
                # not appear in the corpus.
                emit_metrics({
                    "project": os.path.basename(PROJECT_ROOT.rstrip("/")),
                    "coder_model": CODER_MODEL if CODER_BACKEND == "pi" else "claude-code",
                    "duration_s": int(time.time() - t0),
                    "first_pass_compile": False, "final_compile": False,
                    "autonomous_pass": False,
                    "outcome": "write-failed",
                    "files_expected": len(EXPECTED_FILES),
                    "files_written": 0,
                    "write_attempts": MAX_WRITE_ATTEMPTS,
                    "fix_rounds": None, "fix_rounds_attempted": 0,
                    "first_pass_diagnostics": {}, "first_pass_codes": [],
                    # Nothing compiled, so there is no residual to close. Emitted anyway
                    # so every row carries the field and a query never has to guess
                    # whether an absent key means "clean" or "old schema".
                    "final_diagnostics": {}, "final_diag_source": None,
                    "al_profile": AL_PROFILE.get("name"),
                })
                sys.exit(1)

    # ---- Cleanup -----------------------------------------------------------
    if not review_only:
        run_cleanup()

    # ---- Fix loop (keep-best / no-regress) ---------------------------------
    # Compiler + manifest are ground truth (no separate LLM reviewer). Larry can
    # regress — rewrite near-clean files and make them worse — so we track the
    # best (lowest error) state, snapshot it, and always fix FROM that best base.
    # "diags" carries the structured SARIF diagnostics of the best round, so the
    # FINAL residual can be reported with the same severity filtering and category
    # bucketing as the first pass. Without it only first_pass_diagnostics was
    # persisted, and the decisive residual class of the mid-ladder experiment had to
    # be recovered by grepping compiler logs (see bench-results/mid-ladder-tierA).
    best = {"errs": None, "snap": None, "report": "", "findings": "",
            "manifest_fail": True, "build_ok": False, "diags": []}

    # leaderboard metrics
    first_pass_ok = None       # compile result on fix_round 0
    first_pass_build_text = ""  # compiler output on fix_round 0 (regex fallback)
    first_pass_diags = []      # structured SARIF diagnostics on fix_round 0
    first_pass_errs = None     # error score on fix_round 0 (for fix efficiency)
    passed_round = None        # fix round at which it first passed (0 = first pass)
    escalated = False          # pi/mid -> Claude escalation fired
    mid_escalated = False      # pi -> mid tier escalation fired
    regressions = 0            # fix rounds that scored WORSE than best-so-far
    recovery_rounds = 0        # focused missing-file writes (NOT repair attempts —
                               # tracked separately so they don't skew fix metrics)

    # Observational by DEFAULT — records what a capability-boundary trigger WOULD have done
    # and changes nothing. The single exception is ESCALATE_ON_RULE=1 (arm C of the routing
    # economics experiment), which makes the frozen rule actionable; rows produced that way
    # are marked acted=true so they never pool with the observational ones.
    # See capability_shadow.py for the frozen rule.
    _cap_mod = None
    try:
        import capability_shadow as _cap_mod
        _cap_obs = _cap_mod.Observer(PROJECT_ROOT)
    except Exception:
        _cap_obs = None

    # 0 means "the loop was reached and no repair was needed" — a real observation.
    # ABSENCE means execution never got far enough to determine it. Without this, 0 would
    # be overloaded as both, and a run that died before the loop would be indistinguishable
    # from a clean first-pass build.
    observe_config(max_round_reached=0)
    # Durable per-round record. None unless RESULT_BUNDLE_DIR is set, so a run without
    # it is byte-identical to one before this existed. Refuses a destination inside the
    # project root, which clear_project/cleanup.sh would delete.
    _bundle = result_bundle.open_bundle(PROJECT_ROOT,
                                        run_name=os.path.basename(PROJECT_ROOT.rstrip("/")))
    for fix_round in range(MAX_FIX_ROUNDS + 1):
        label = "initial build" if fix_round == 0 else f"build (fix round {fix_round})"
        print(f"\n=== {label.upper()} ===")

        # AL-14: regenerate the project profile each round. It was captured ONCE, before
        # the write phase — and a build starts with an empty src/, so the profile said
        # "objects: none" and stayed that way for the whole run. The fix loop is exactly
        # where knowing what objects now exist is worth anything, and that is the round
        # where it was guaranteed to be stale.
        if AL_BRAIN and fix_round > 0:
            handover_text = read_handover()

        manifest_text, manifest_fail = run_manifest_check()
        build_text, build_ok = run_al_compile()
        errs = count_build_errors(build_text, build_ok) + (1000 if manifest_fail else 0)
        if fix_round == 0:
            first_pass_ok = build_ok and not manifest_fail
            first_pass_build_text = build_text
            first_pass_diags = list(_last_diags)
            first_pass_errs = errs
        elif best["errs"] is not None and errs > best["errs"]:
            regressions += 1     # this fix round is worse than the best we'd reached

        if _cap_obs is not None:
            try:
                _cap_obs.observe(
                    [(os.path.basename(d.get("uri") or ""), d.get("code") or "")
                     for d in _last_diags if _is_error(d)], fix_round)
            except Exception:
                pass
            # ESCALATE_ON_RULE=1 makes the frozen rule ACTIONABLE — arm C of the routing
            # economics experiment. Default OFF, so capability_shadow stays observational
            # for every other run and its prospective log keeps its meaning.
            #
            # The rule itself is untouched: run-build only READS fire_round. Rows produced
            # while acting are marked acted=true so they are never pooled with the
            # observational ones — a rule that changed the outcome is a different population
            # from a rule that watched it.
            if (ESCALATE_ON_RULE and _cap_obs.fire_round is not None
                    and _coder_state["backend"] == "pi" and not escalated):
                _cap_obs.acted = True
                # escalation_available(), NOT allowed("anthropic"). Under enterprise-anon
                # allowed() is deliberately False AT REST — Anthropic is armed only inside
                # claude_egress's scrub context — so testing it here concluded "escalation
                # unavailable" and suppressed every arm C escalation while the rule was
                # firing. This is the same predicate the ESCALATE_AFTER path uses.
                _esc_ok, _esc_why = egress_policy.escalation_available()
                if os.path.exists(CLAUDE_BIN) and _esc_ok:
                    _coder_state["backend"] = "claude"
                    escalated = True
                    print(f"\n  ⇧ RULE ESCALATION — the frozen capability rule "
                          f"({_cap_mod.rule_fingerprint()}) fired at round "
                          f"{_cap_obs.fire_round}; handing the remaining rounds to Claude "
                          f"(billed per-token).")
                else:
                    print(f"  Rule fired at round {_cap_obs.fire_round} but escalation is "
                          f"unavailable ({_esc_why or 'claude bin missing'}) — staying local.")
        print(f"  error score: {errs}" + (f"  (best so far: {best['errs']})" if best["errs"] is not None else ""))
        if _bundle is not None:
            _bundle.round(fix_round, errs, snapshot_src(), build_text=build_text,
                          manifest_text=manifest_text, manifest_fail=manifest_fail,
                          build_ok=build_ok)

        build_errors = truncate_build(build_text) if not build_ok else ""
        manifest_errors = manifest_text if manifest_fail else ""
        all_findings = "\n\n".join(f for f in [manifest_errors, build_errors] if f.strip())
        report = f"{manifest_text}\n\n{build_text}"

        passed = build_ok and not manifest_fail

        if best["errs"] is None or errs < best["errs"]:
            best = {"errs": errs, "snap": snapshot_src(), "report": report,
                    "findings": all_findings, "manifest_fail": manifest_fail,
                    "build_ok": build_ok, "diags": list(_last_diags)}
            print(f"  ★ new best (error score: {errs})")

        if passed:
            passed_round = fix_round
            break
        if fix_round >= MAX_FIX_ROUNDS:
            print(f"\n  Max fix rounds ({MAX_FIX_ROUNDS}) reached.")
            break

        # Claude fixes FORWARD: never revert on a higher count. Fixing a blocker often
        # unmasks parse-halted errors (count jumps up) — reverting there would throw away
        # real progress and re-feed the same masked errors forever. Claude is reliable, so
        # let it iterate on the CURRENT errors until they clear. The revert safety-net is
        # kept only for local coders, which genuinely regress by rewriting working files.
        if _coder_state["backend"] == "claude":
            fix_findings = all_findings
        elif errs > best["errs"]:
            # Unmask detection: if NONE of the best state's errors survive in this
            # round, the "regression" is the compiler surfacing errors a blocker had
            # been hiding — the previous errors are genuinely fixed. Reverting there
            # re-feeds the same blocker forever (doclink: 1 AL0282 → 16 unmasked
            # AL0132s → revert → rename again → 16 again, all 8 rounds). Adopt the
            # unmasked state as the new best and fix FORWARD instead.
            best_keys = error_keys(best["report"])
            cur_keys = error_keys(build_text)
            if (best_keys and cur_keys and not (best_keys & cur_keys)
                    and manifest_fail == best["manifest_fail"]):
                print(f"  Unmask: all {len(best_keys)} previous error(s) cleared; "
                      f"{len(cur_keys)} newly surfaced — fixing forward, not reverting.")
                best = {"errs": errs, "snap": snapshot_src(), "report": report,
                        "findings": all_findings, "manifest_fail": manifest_fail,
                        "build_ok": build_ok, "diags": list(_last_diags)}
                fix_findings = all_findings
            else:
                print(f"  Round regressed ({errs} > best {best['errs']}) — reverting to best before fixing.")
                restore_src(best["snap"])
                fix_findings = best["findings"]
        else:
            fix_findings = all_findings

        # Escalation ladder (one-way latches): pi rounds 0..M-1, mid rounds M..N-1,
        # Claude rounds N+. Check the Claude threshold first so round N jumps straight
        # to Claude even from pi (a mid tier that isn't armed is simply skipped).
        if (ESCALATE_AFTER is not None and _coder_state["backend"] in ("pi", "mid")
                and fix_round >= ESCALATE_AFTER):
            _coder_state["backend"] = "claude"
            escalated = True
            print(f"\n  ⚠ ESCALATION: {fix_round} fix round(s) without a pass — "
                  f"handing remaining rounds to Claude Code (billed per-token).")
        elif (ESCALATE_MID_AFTER is not None and _coder_state["backend"] == "pi"
                and fix_round >= ESCALATE_MID_AFTER):
            _coder_state["backend"] = "mid"
            mid_escalated = True
            print(f"\n  ⚠ MID ESCALATION: {fix_round} pi fix round(s) without a pass — "
                  f"handing the next rounds to the mid tier ({MID_MODEL}, cloud-billed).")

        # Missing-file recovery: a focused "write just these" step recovers dropped
        # manifest files. snippet-fix can't create files, and a weak coder ignores
        # "create the missing file" when buried in a full-project fix message. Fires
        # only while files are missing (already a failure state) and on the local coder
        # — Claude creates missing files fine via the normal fix. Default on.
        # Capped: if the focused write keeps failing, fall through to the general fix
        # (which words the same request differently) instead of burning every round.
        missing = [f for f in EXPECTED_FILES if not os.path.exists(f)]
        if (RECOVER_MISSING and manifest_fail and missing
                and _coder_state["backend"] == "pi"
                and recovery_rounds < MAX_RECOVERY_ROUNDS):
            recovery_rounds += 1
            print(f"\n--- Larry (Pi): recovering {len(missing)} missing manifest file(s) "
                  f"(attempt {recovery_rounds}/{MAX_RECOVERY_ROUNDS}, round {fix_round + 1}) ---")
            run_coder(build_missing_files_msg(handover_text, missing), timeout=FIX_TIMEOUT,
                      label="Larry-missing-files")
            run_cleanup()
            continue

        # Ground the fix in real BC declarations before asking for it.
        if RAG_INJECT and not build_ok:
            grounding = (kb_ground(_unresolved_names(build_text))
                         + kb_ground_members(build_text)
                         + ground_builtin_members(build_text)
                         + probe_unresolved_objects(build_text)
                         + ground_call_signatures(build_text))
            if grounding:
                fix_findings = fix_findings + grounding
        if not build_ok:
            _hints = known_fix_hints(build_text)
            if _hints:
                print(f"  known-fix: {_hints.count(chr(10) + '- ')} hint(s) appended")
                fix_findings = fix_findings + _hints

        who = "Claude" if _coder_state["backend"] == "claude" else "Larry (Pi)"
        print(f"\n--- {who}: fixing issues (round {fix_round + 1}) ---")
        observe_config(max_round_reached=fix_round + 1)
        _fix_to_before = coder.FIX_TIMEOUT_STREAK["n"]
        # Route by error class (pi only; Claude always gets the full fix message).
        strategy = FIX_STRATEGY if _coder_state["backend"] == "pi" else "rewrite"
        casc = []
        if strategy == "auto":
            casc = cascade_files(build_text) if not build_ok else []
            strategy = "file-rewrite" if casc else "snippet"
            print(f"  fix-route: {strategy}"
                  + (f" ({', '.join(os.path.basename(c) for c in casc[:2])})" if casc else ""))
        if strategy == "file-rewrite":
            # Structurally broken file(s): rewrite each in isolation (cap 2/round) so
            # the healthy files are never touched. The known-fix hints go WITH the
            # rewrite — without them the model reproduces its own defect verbatim.
            _rw_hints = known_fix_hints(build_text)
            for cf in casc[:2]:
                file_errs = "\n".join(l for l in (build_text or "").splitlines()
                                      if os.path.basename(cf) in l and "error" in l)[:3000]
                run_coder(build_file_rewrite_msg(handover_text, cf, file_errs, _rw_hints), timeout=FIX_TIMEOUT,
                          label=f"{who}-file-rewrite")
        elif strategy == "snippet":
            # Local Fast-Apply: model emits SEARCH/REPLACE edits (read-only), applied
            # deterministically — no whole-file rewrite, so it can't cascade.
            import snippet_fix
            out = run_pi(snippet_fix.build_snippet_prompt(
                PROJECT_ROOT, fix_findings, get_project_file_listing()),
                label=f"{who}-snippet-fix", allow_write=False)
            ap, fl, _det = snippet_fix.apply_edit_blocks(out, PROJECT_ROOT)
            print(f"  snippet-fix: {ap} edit(s) applied, {fl} unmatched")
            # Show WHY a block missed. Without this the loop silently no-ops and the
            # run just burns rounds — the counts alone cannot tell you whether the
            # model hallucinated context or the matcher is too strict.
            for _d in _det:
                if not _d.startswith("applied"):
                    print(f"      {_d}")
            if ap == 0:
                # Nothing landed — a pure no-op round. Fall back to the full fix
                # message so the round still does SOMETHING (observed: 8 consecutive
                # 0-edit rounds when the model won't emit edit blocks).
                print("  snippet-fix produced nothing — falling back to full fix message")
                run_coder(build_fix_msg(fix_findings), label=f"{who}-fix", timeout=FIX_TIMEOUT)
        else:
            run_coder(build_fix_msg(fix_findings), label=f"{who}-fix", timeout=FIX_TIMEOUT)
        run_cleanup()

        # A fix round that burned its whole budget did not fix anything, and the next one
        # repeats it. MAX_FIX_ROUNDS x FIX_TIMEOUT can still outlast the harness cap, so
        # bounding a single call is not enough on its own. The streak resets whenever a
        # round completes, so an isolated slow round costs one timeout and nothing more.
        if coder.FIX_TIMEOUT_STREAK["n"] == _fix_to_before:
            coder.FIX_TIMEOUT_STREAK["n"] = 0
        if coder.FIX_TIMEOUT_STREAK["n"] >= MAX_FIX_TIMEOUTS:
            print(f"  {coder.FIX_TIMEOUT_STREAK['n']} consecutive fix rounds hit the full "
                  f"{FIX_TIMEOUT}s timeout without finishing — abandoning the fix loop. "
                  f"Best so far (error score {best['score']}) is what gets kept.")
            break

    # Ensure disk holds the BEST version, not a later regression.
    if best["snap"]:
        restore_src(best["snap"])

    # ---- Behaviour review (optional; only meaningful once it compiles) ----
    #   REVIEW_BACKEND=coms   (default) → local validator-peer via pi/coms
    #   REVIEW_BACKEND=claude          → Claude Code reviewer (stronger; converts rules to catches)
    review_backend = os.environ.get("REVIEW_BACKEND", "coms")
    review_ran = False
    review_findings = None    # True/False if a review ran; None if not
    review_landed = None      # did review fixes land cleanly
    review_fix_rounds = 0
    review_findings_count = 0  # number of findings the review raised
    review_citations = 0       # BCQuality [rule:] citations among the findings
    # True until something proves otherwise: a reviewer identical to the coder, or a
    # Claude-on-Claude review. Recorded in metrics so `promote` can refuse a tree whose
    # review was not actually independent (T8).
    review_independent_ok = True
    review_gate_failed = None   # set to a reason string when a REQUIRED review cannot stand
    if review_peer and best["build_ok"] and not best["manifest_fail"]:
        review_ran = True
        print(f"\n=== BEHAVIOUR REVIEW ({review_backend}) ===")
        try:
            sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
            import coms_review, glob as _glob
            intent = read_handover()
            # AL-6: deterministic semantic findings go to the reviewer as EVIDENCE, not as
            # a verdict. They are patterns that compile cleanly and may still be wrong at
            # runtime, which is precisely the class a compiler-based referee cannot see.
            try:
                sem_findings = al_semantics.analyse(PROJECT_ROOT)
                global _sem_summary
                _sem_summary = {r: sum(1 for f in sem_findings if f["rule"] == r)
                                for r in sorted({f["rule"] for f in sem_findings})}
                if sem_findings:
                    print(f"  AL semantics: {len(sem_findings)} advisory finding(s) "
                          f"({', '.join(sorted({f['rule'] for f in sem_findings}))})")
            except Exception as _e:
                sem_findings = []
                print(f"  AL semantics unavailable ({_e})")
            if sem_findings:
                # Appended to the intent so both review backends receive it without a
                # signature change. Framed as "confirm or dismiss": the reviewer has the
                # code in front of it and these rules have real exceptions, so asking for
                # judgement beats asserting a defect.
                intent = (intent + "\n\n" + al_semantics.format_findings(sem_findings)
                          + "\n\nConfirm or dismiss each of the above against the actual "
                            "code. They are pattern matches, not verdicts.")
            al_files = sorted(_glob.glob(PROJECT_ROOT + "/src/**/*.al", recursive=True))
            files = [(os.path.relpath(f, PROJECT_ROOT), open(f).read()) for f in al_files]
            proj_name = os.path.basename(PROJECT_ROOT) + "-review"
            # Ground the validator in curated BC/AL rules relevant to the changed source.
            # Fail-OPEN is correct for an advisory review and wrong for a gate: under
            # REVIEW_REQUIRED the knowledge the reviewer is supposed to apply must
            # actually be present, or "reviewed" means "asked a model with no rules".
            try:
                import bcquality
                rules = bcquality.rules_for(files, bc_version=AL_CTX.get('bc_version'))
                if rules:
                    print(f"  BCQuality: {len(rules)} rule(s) injected into review "
                          f"({', '.join(sorted({r['domain'] for r in rules}))})")
                elif REVIEW_REQUIRED:
                    print("  ⛔ REVIEW REQUIRED but BCQuality returned no rules — "
                          "the knowledge base is unavailable or empty.")
                    review_gate_failed = "bcquality-unavailable"
            except Exception as _e:
                rules = None
                if REVIEW_REQUIRED:
                    print(f"  ⛔ REVIEW REQUIRED but BCQuality failed: {_e}")
                    review_gate_failed = f"bcquality-error: {_e}"
                else:
                    print(f"  BCQuality: skipped ({_e})")
            if review_backend == "claude":
                findings, clean = claude_review(intent, files, rules)
                # A Claude coder reviewed by Claude is not an independent review.
                if _coder_state["backend"] == "claude" and REVIEW_INDEPENDENT:
                    print("  ⛔ REVIEW NOT INDEPENDENT — coder and reviewer are both "
                          "Claude. Set REVIEW_INDEPENDENT=0 to accept an advisory "
                          "review, or review with a different backend.")
                    review_independent_ok = False
            else:
                # Defaulting the reviewer to CODER_MODEL made "independent model review"
                # mean the coder reviewing its own output — and coms_review.py's own
                # docstring advertises a DIVERSE default, so the code contradicted the
                # doc. Pick a different model by default, and refuse to call it
                # independent when they match.
                v_model = os.environ.get("COMS_VALIDATOR_MODEL", REVIEW_MODEL_DEFAULT)
                r_model = os.environ.get("COMS_RELAY_MODEL", CODER_MODEL)
                if _same_model(v_model, CODER_MODEL):
                    if REVIEW_INDEPENDENT:
                        print(f"  ⛔ REVIEW NOT INDEPENDENT — reviewer ({v_model}) is the "
                              f"coder model. Set COMS_VALIDATOR_MODEL to a different "
                              f"model, or REVIEW_INDEPENDENT=0 to accept advisory.")
                        review_independent_ok = False
                    else:
                        print(f"  ⚠ review is ADVISORY (reviewer == coder: {v_model})")
                findings, clean = coms_review.review(
                    proj_name, intent, files,
                    validator_model=v_model,
                    relay_model=r_model,
                    knowledge_rules=rules)
            review_findings = not clean
            if not clean:
                review_findings_count = len([l for l in findings.splitlines() if l.strip()])
                review_citations = findings.count("[rule:")
            if clean:
                print(f"  {review_backend}: REVIEW COMPLETE (no behaviour findings)")
            else:
                print(f"  {review_backend} findings:\n" + "\n".join("    " + l for l in findings.splitlines()))
                pre = snapshot_src()   # known-good compiling state to revert to
                fixed = False
                # A semantic review fix is a whole-file rewrite; a 35B coder often slips a
                # brace/begin on the first shot. Instead of reverting immediately, let the
                # coder iterate on its OWN compile errors (as the initial build loop does)
                # before giving up — that loop proves the model can grind out cascades.
                inner_rounds = int(os.environ.get("PI_REVIEW_FIX_COMPILE_ROUNDS", "3"))
                backends = ["pi"] * REVIEW_FIX_ROUNDS
                if ESCALATE_AFTER is not None and os.path.exists(CLAUDE_BIN):
                    backends.append("claude")
                for rf, backend in enumerate(backends):
                    review_fix_rounds = rf + 1
                    who = "Claude" if backend == "claude" else "Larry (Pi)"
                    fix = run_claude_code if backend == "claude" else run_coder
                    print(f"\n--- {who}: fixing review findings (round {rf + 1}/{len(backends)}) ---")
                    fix(build_fix_msg(findings), label=f"{who}-review-fix")
                    run_cleanup()
                    mtext, mfail = run_manifest_check()
                    btext, bok = run_al_compile()
                    # Compile-error feedback sub-loop: feed the coder its own errors.
                    ci = 0
                    while (not bok or mfail) and ci < inner_rounds:
                        ci += 1
                        print(f"  review fix regressed the build — compile-fix {ci}/{inner_rounds}")
                        fix(build_fix_msg(mtext + "\n\n" + btext if mfail else btext),
                            label=f"{who}-review-compilefix")
                        run_cleanup()
                        mtext, mfail = run_manifest_check()
                        btext, bok = run_al_compile()
                    if bok and not mfail:
                        best = {"errs": 0, "snap": snapshot_src(), "report": f"{mtext}\n\n{btext}",
                                "findings": "", "manifest_fail": False, "build_ok": True,
                                "diags": list(_last_diags)}
                        print("  review fix applied; still compiles clean"
                              + (f" (recovered after {ci} compile-fix round(s))" if ci else ""))
                        fixed = True
                        break
                    print(f"  review-fix round {rf + 1} could not restore a clean build after "
                          f"{ci} compile-fix round(s) — reverting.")
                    restore_src(pre)
                if not fixed:
                    print("  review findings not landed cleanly — kept the pre-review compiling build.")
                review_landed = fixed
        except Exception as e:
            print(f"  review skipped (error: {e})")

    # ---- Final report ------------------------------------------------------
    print("\n" + "=" * 60)
    print(f"FINAL REPORT (best round — error score {best['errs']})")
    print("=" * 60)
    print(best["report"])
    print("=" * 60)

    # Which diagnostics this build actually hit. Metrics recorded only broad categories
    # ("syntax", "other"), so nothing could say WHICH codes cost the rounds — and the
    # error KB had no evidence base to grow from.
    global _diag_codes, _first_pass_codes
    try:
        _diag_codes = al_errors.codes_in(best.get("report") or "")
        # First-pass codes are the more useful evidence: they are what the coder got
        # wrong before any repair, which is exactly the population the KB documents.
        _first_pass_codes = al_errors.codes_in(first_pass_build_text or "")
    except Exception:
        _diag_codes, _first_pass_codes = [], []

    final_ok = best["build_ok"] and not best["manifest_fail"]

    # Shadow observation closes here, on the COMPILE outcome — before the profile,
    # policy, test and review gates below, which can flip final_ok for reasons that have
    # nothing to do with whether local repair converged.
    if _cap_obs is not None:
        try:
            _cap_obs.finish(final_ok, bool(_incr_stats.get("stall_fallback")))
        except Exception:
            pass

    # AL-11: the profile's own gates. These are destination policy, not compilation: a
    # missing tooltip is a warning everywhere and an AppSource rejection, and app.json
    # metadata that Microsoft rejects costs days to find out about from Microsoft.
    if final_ok:
        _pf = al_profiles.check_manifest(_app_json_now(), AL_PROFILE) \
            + al_profiles.check_diagnostics(_last_diags, AL_PROFILE)
        if _pf:
            print(f"\n  ⛔ PROFILE GATE ({AL_PROFILE['name']}) — "
                  f"{len(_pf)} policy failure(s):")
            for _r in _pf:
                print(f"     {_r}")
            final_ok = False
        _profile_failures = _pf
    else:
        _profile_failures = []

    # AL-7: does replacing the installed version break it? The compiler cannot answer
    # that — a dropped field compiles perfectly and takes the column with it — so this
    # compares the .app just built against the baseline the profile requires.
    global _upgrade_result
    _pol, _needs_baseline = al_profiles.upgrade_policy(AL_PROFILE)
    if _pol and final_ok:
        _new_app = next(iter(sorted(glob.glob(os.path.join(PROJECT_ROOT, "*.app")))), None)
        if not AL_UPGRADE_BASELINE or not os.path.isfile(AL_UPGRADE_BASELINE):
            msg = (f"the {AL_PROFILE['name']} profile sets breaking_changes={_pol} but no "
                   f"baseline .app was given — set AL_UPGRADE_BASELINE to the version "
                   f"this one replaces")
            if _needs_baseline:
                # "could not check" must never read as "checked and clean".
                print(f"\n  ⛔ UPGRADE GATE — {msg}")
                final_ok = False
            else:
                print(f"\n  ⚠ upgrade check skipped — {msg}")
            _upgrade_result = {"status": "no-baseline", "detail": msg}
        elif not _new_app:
            print("\n  ⛔ UPGRADE GATE — no .app was produced, so nothing can be compared")
            final_ok = False
            _upgrade_result = {"status": "no-artifact"}
        else:
            try:
                _ur = al_upgrade.analyse(AL_UPGRADE_BASELINE, _new_app)
                print("\n" + al_upgrade.format_report(_ur, limit=12))
                _upgrade_result = {"status": "analysed", "verdict": _ur["verdict"],
                                   "counts": _ur["counts"],
                                   "same_app_id": _ur["same_app_id"],
                                   "from": _ur["from"]["version"], "to": _ur["to"]["version"]}
                _uf = al_profiles.upgrade_failures(_ur["verdict"], AL_PROFILE)
                if not _ur["same_app_id"]:
                    _uf.append("baseline and build are different apps (app id differs) — "
                               "this is not an upgrade comparison")
                if _uf:
                    print(f"\n  ⛔ UPGRADE GATE ({AL_PROFILE['name']}):")
                    for _r in _uf:
                        print(f"     {_r}")
                    final_ok = False
            except Exception as _e:
                print(f"\n  ⛔ UPGRADE GATE — analysis failed ({_e})")
                final_ok = False
                _upgrade_result = {"status": "error", "detail": str(_e)}

    # AL-3: tests run only once the build is otherwise good — testing a tree that does
    # not compile tells you nothing you did not already know. Opt-in, and fails closed
    # when enabled: a test failure AND an infrastructure failure both fail the referee.
    # Reporting "could not run the tests" as a pass is how an enabled gate silently
    # becomes a disabled one.
    global _test_result
    if AL_RUN_TESTS and final_ok:
        print("\n--- AL tests ---")
        _app_file = next(iter(sorted(glob.glob(os.path.join(PROJECT_ROOT, "*.app")))), None)
        # AL-10: if the manifest names what changed, run only the tests that reach it.
        # The filter comes from the object graph, never from a guess — a subset you
        # cannot justify makes a green run meaningless. No selection = run everything.
        _sel, _why, _filter = [], "", "*"
        try:
            _changed = [os.path.splitext(os.path.basename(f))[0].split(".")[0]
                        for f in (EXPECTED_FILES or [])]
            if _changed:
                _sel, _why = al_testgen.select_tests(PROJECT_ROOT, _changed)
                _filter = al_testgen.codeunit_filter(PROJECT_ROOT, _sel)
                print(f"  selection: {_why}")
        except Exception as _e:
            print(f"  test selection unavailable ({_e}) — running the whole suite")
        _test_result = al_tests.run(PROJECT_ROOT, AL_CTX.get("app_id"),
                                    AL_CTX.get("bc_version"), app_file=_app_file,
                                    codeunit=_filter)
        _test_result["selected"] = _sel
        print(f"  {al_tests.summary(_test_result)}")
        if not _test_result["ok"]:
            print(f"  ⛔ REFEREE FAILED on tests ({_test_result['status']}).")
            final_ok = False
    elif AL_RUN_TESTS:
        print("\n--- AL tests --- skipped: the build did not pass, so there is "
              "nothing meaningful to test")
        _test_result = {"status": "not-run", "ok": False,
                        "detail": "build failed before tests could run"}

    # A REQUIRED review that could not stand must fail the build, not decorate it.
    # Under review-optional none of this fires and behaviour is unchanged.
    if REVIEW_REQUIRED and final_ok:
        if not review_ran:
            print("  ⛔ REVIEW REQUIRED but no review ran.")
            final_ok = False
        elif review_gate_failed:
            print(f"  ⛔ REVIEW REQUIRED but the review could not stand "
                  f"({review_gate_failed}).")
            final_ok = False
        elif not review_independent_ok:
            print("  ⛔ REVIEW REQUIRED but the review was not independent "
                  "(reviewer == coder).")
            final_ok = False
        elif review_findings:
            print(f"  ⛔ REVIEW REQUIRED and the reviewer raised "
                  f"{review_findings_count} finding(s) — not a clean review.")
            final_ok = False

    # object-type + diagnostic breakdown from the manifest and first-pass compile
    import collections as _c
    exp = sorted(EXPECTED_FILES)
    objtypes_expected = dict(_c.Counter(object_type(f) for f in exp))
    objtypes_written = dict(_c.Counter(object_type(f) for f in exp if os.path.exists(f)))
    # Prefer structured SARIF diagnostics (exact code/severity/file); regex is the fallback.
    if first_pass_diags:
        diagnostics = classify_diags(first_pass_diags)
        diag_source = "sarif"
        failed_types = sorted({object_type(i["uri"]) for i in first_pass_diags
                               if _is_error(i) and i.get("uri")})
    else:
        diagnostics = classify_diagnostics(first_pass_build_text)
        diag_source = "regex"
        failed_types = sorted({object_type(m) for m in
                               re.findall(r"([^\s(]+\.al)\(\d+,\d+\): error", first_pass_build_text or "")})

    # The FINAL residual, bucketed and severity-filtered exactly like the first pass.
    # This is the state a repair rung would have to close, so it — not the first pass —
    # is what an escalation experiment is actually about. `diagnostic_codes` cannot
    # serve: it is a severity-blind presence list (one entry per code per run) and
    # counts warnings such as AL0482/AL0789 alongside errors.
    if best.get("diags"):
        final_diagnostics = classify_diags(best["diags"])
        final_diag_source = "sarif"
        final_failed_types = sorted({object_type(i["uri"]) for i in best["diags"]
                                     if _is_error(i) and i.get("uri")})
    else:
        final_diagnostics = classify_diagnostics(best.get("report") or "")
        final_diag_source = "regex" if (best.get("report") or "").strip() else None
        final_failed_types = sorted({object_type(m) for m in
                                     re.findall(r"([^\s(]+\.al)\(\d+,\d+\): error",
                                                best.get("report") or "")})

    _prov = fixture_provenance.collect(PROJECT_ROOT)
    emit_metrics({
        "project": os.path.basename(PROJECT_ROOT),
        # Which fixture revision produced this row. Without it a pass rate cannot be
        # tied to the input text, which is how p1's enum defect survived ten runs.
        **_prov,
        "coder_backend": CODER_BACKEND,
        "coder_model": CODER_MODEL if CODER_BACKEND == "pi" else "claude-code",
        "duration_s": int(time.time() - t0),
        "first_pass_compile": first_pass_ok,
        "final_compile": final_ok,
        "autonomous_pass": final_ok and not escalated and not mid_escalated,  # passed on Larry alone (free)
        "mid_closed": final_ok and mid_escalated and not escalated,  # closed by the cheap mid tier (no Claude)
        "fix_rounds": passed_round,          # rounds to reach a clean compile (0 = first pass); None if never
        "max_fix_rounds": MAX_FIX_ROUNDS,
        # denominator for regression rate + fix efficiency: REPAIR rounds only,
        # so focused missing-file writes don't dilute either.
        "fix_rounds_attempted": max(0, (passed_round if passed_round is not None
                                        else MAX_FIX_ROUNDS) - recovery_rounds),
        "regressions": regressions,          # fix rounds that scored worse than best
        # focused missing-file writes — NOT repair attempts. Kept separate so
        # "fix rounds"/regression/efficiency stay a measure of repair quality.
        "recovery_rounds": recovery_rounds,
        # compile errors cleared first-pass → best (excludes the manifest-fail score penalty)
        "errors_cleared": max(0, count_build_errors(first_pass_build_text, first_pass_ok)
                              - count_build_errors(best["report"], best["build_ok"])),
        "claude_escalated": escalated,
        # WORKFLOW=incremental: how the ratchet actually behaved. Empty dict on the
        # single-shot path, so a mixed corpus stays readable.
        "workflow": WORKFLOW,
        "incr_green": len(_green) if WORKFLOW == "incremental" else None,
        "incr_left": len(_left) if WORKFLOW == "incremental" else None,
        "incr_deferred": _incr_stats.get("deferred"),
        "incr_reverted": _incr_stats.get("reverted"),
        "incr_sweeps": _incr_stats.get("sweeps"),
        "incr_stalled": _incr_stats.get("stalled"),
        "incr_stall_fallback": _incr_stats.get("stall_fallback", False),
        # Files the model claimed to write but did not, after every retry. A non-zero
        # value means the run measured a write failure, not the workflow.
        "incr_write_failed": _incr_stats.get("write_failed", 0),
        # Separated deliberately: a transient false-success claim that a retry repaired
        # still leaves the run interpretable; one that exhausted every attempt does not.
        "incr_write_recovered": _incr_stats.get("write_recovered", 0),
        "incr_write_retries": _incr_stats.get("write_retries", 0),
        # Referee completeness. A build produced without the required cops is a weaker
        # check than the pipeline's stated referee, so it is recorded and `promote`
        # refuses it (Task 8). Absent/False means the full referee ran.
        "bare_compile_only": bool(missing_analyzers()) and ALLOW_BARE_COMPILE,
        "review_independent": review_independent_ok,
        # AL-5: every AL build records the BC context it was actually built against, so
        # a result can be compared like-for-like and a version mismatch is visible.
        "bc_version": AL_CTX.get("bc_version"),
        "al_runtime": AL_CTX.get("runtime"),
        "al_target": AL_CTX.get("target"),
        "al_profile": AL_PROFILE.get("name"),
        "profile_failures": _profile_failures,
        "upgrade": _upgrade_result,
        "profile_unenforced": dict(al_profiles.unenforced(AL_PROFILE)),
        "al_version_mismatch": AL_CTX.get("version_mismatch"),
        "al_semantic_findings": _sem_summary,
        "diagnostic_codes": _diag_codes,
        "first_pass_codes": _first_pass_codes,
        "tests_enabled": AL_RUN_TESTS,
        "tests_status": _test_result.get("status"),
        "tests_total": _test_result.get("total", 0),
        "tests_passed": _test_result.get("passed", 0),
        "tests_failed": _test_result.get("failed", 0),
        "tests_env": _test_result.get("env"),
        "tests_selection": _test_result.get("selection"),
        "tests_selected": _test_result.get("selected") or [],
        "review_mode": "required" if REVIEW_REQUIRED else "optional",
        "review_gate_failed": review_gate_failed,
        "analyzers_missing": missing_analyzers() or None,
        "mid_escalated": mid_escalated,
        # Record WHICH mid model ran, else the leaderboard cannot attribute a closed
        # build to it — and comparing kimi-k2 against a successor is the whole point of
        # collecting this. Only meaningful when mid_escalated is true.
        "mid_model": MID_MODEL if mid_escalated else None,
        "manifest_ok": not best["manifest_fail"],
        "files_expected": len(exp),
        "files_written": sum(1 for f in exp if os.path.exists(f)),
        "objtypes_expected": objtypes_expected,
        "objtypes_written": objtypes_written,
        "objtypes_failed_first_pass": failed_types,
        "first_pass_diagnostics": diagnostics,
        "diag_source": diag_source,
        # Which routing POLICY produced this run — the arm label, recorded by the run
        # itself rather than inferred from the directory name.
        "routing_policy": ("rule" if ESCALATE_ON_RULE else
                           ("fixed-round" if ESCALATE_AFTER is not None else "never")),
        "escalate_after": ESCALATE_AFTER,
        "rule_fingerprint": (_cap_mod.rule_fingerprint() if (ESCALATE_ON_RULE and _cap_mod)
                             else None),
        # Whether the rule FIRED, independent of whether escalation followed. Without this a
        # caller can only check the policy label, and arm C was suppressed for a whole suite
        # while every label-based assertion passed.
        "rule_fired": (_cap_obs.fire_round is not None) if _cap_obs else None,
        "rule_fire_round": (_cap_obs.fire_round if _cap_obs else None),
        # Routing-economics prerequisite: what the escalations actually cost. A non-zero
        # claude_calls_missing_usage means the spend figure is INCOMPLETE and must not be
        # reported as a cost. Fail-open: instrumentation never breaks a build.
        **(claude_egress.usage_totals() if hasattr(claude_egress, "usage_totals") else {}),
        # The residual a repair rung would have to close. Absent/empty on a PASS.
        "final_diagnostics": final_diagnostics,
        "final_diag_source": final_diag_source,
        "objtypes_failed_final": final_failed_types,
        "review_backend": review_backend if review_ran else None,
        "review_findings": review_findings,
        "review_findings_count": review_findings_count,
        "review_rule_citations": review_citations,
        "review_fix_rounds": review_fix_rounds,
        "review_landed": review_landed,
    })

    # Receipt: proof for `promote` that THIS tree passed THIS referee. Written only on
    # a pass — a failed build must leave no promotable evidence behind. Tied to a tree
    # hash, so editing the source after a green build invalidates it.
    if final_ok:
        try:
            rp = build_receipt.write(
                PROJECT_ROOT,
                referee_ok=True,
                analyzers=[a for a in REQUIRED_ANALYZERS if a not in missing_analyzers()],
                bare_compile_only=bool(missing_analyzers()) and ALLOW_BARE_COMPILE,
                review_mode=("required" if REVIEW_REQUIRED else
                             (review_backend if review_ran else "none")),
                review_ok=(review_ran and not review_findings) or None,
                review_independent=review_independent_ok,
                coder_model=CODER_MODEL,
                tests_ok=(_test_result.get("ok") if AL_RUN_TESTS else None),
                extra={"al_profile": AL_PROFILE.get("name"),
                       **fixture_provenance.collect(PROJECT_ROOT),
                       "upgrade": _upgrade_result,
                       "profile_unenforced": dict(al_profiles.unenforced(AL_PROFILE)),
                       "al_semantic_findings": _sem_summary,
        "diagnostic_codes": _diag_codes,
        "first_pass_codes": _first_pass_codes,
                       "tests": _test_result,
                       "al_context": {k: AL_CTX.get(k) for k in
                                      ("bc_version", "runtime", "target", "application",
                                       "symbol_application_version", "deployment_profile",
                                       "version_mismatch")}})
            print(f"  build receipt: {os.path.basename(rp)}")
        except Exception as _e:
            print(f"  (receipt not written: {_e})")

    # Close the durable record. Written whether the build passed or failed — a failed
    # trajectory is the one worth keeping, and the per-round dirs already stand alone
    # if this last write cannot happen.
    if _bundle is not None:
        _bi = _bundle.close(verdict="PASS" if passed else "FAIL",
                            best_error_score=best["errs"],
                            max_fix_rounds=MAX_FIX_ROUNDS)
        if _bi:
            print(f"  result-bundle index: {_bi}")
        for _be in _bundle.errors:
            print(f"  (result-bundle: {_be})")

    # Say whether the run did what it declared, BEFORE the result — a void run must be
    # legible in the log, not only in the metrics file someone reads later.
    _cv, _cbad = config_verification()
    if _cv == "mismatch":
        print("\n  ⚠ CONFIG MISMATCH — this run did not do what it declared:")
        for _m in _cbad:
            print(f"      {_m}")
        print("      Treat the result as VOID for experimental purposes.")
    else:
        print(f"\n  config: {_cv}")

    if final_ok:
        print("\nRESULT: PASS")
    else:
        print(f"\nRESULT: FAIL (best achieved: {best['errs']} error score)")
        sys.exit(1)


if __name__ == "__main__":
    main()
