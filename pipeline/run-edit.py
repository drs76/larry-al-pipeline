#!/usr/bin/env python3
"""
Larry edit orchestrator — edit-in-place rounds on an EXISTING repo (the edit flow).

run-build.py is greenfield: clear project, write everything, manifest = "exactly these
files exist". This is the edit counterpart: the repo already compiles, the handover is a
list of edit TASKS, and the manifest is a MAY-MODIFY whitelist. Nothing is ever cleared.
git is the ground truth for what changed — coder self-reports are ignored.

Flow (per BCCalendarJsDemo trial, larry-edit-flow.md):
  0. Preflight: git repo, clean tracked tree, whitelist parsed from handover
  1. Task loop — one task at a time:
       a. DETERMINISTIC apply when the task is fully exact FIND/REPLACE blocks
          (no model involved — the blocks were authored exact; transcription is risk)
       b. else ONE pi invocation for that task alone (read-only; emits SEARCH/REPLACE
          blocks, applied deterministically — snippet_fix protocol, no file rewrites)
       c. diff gate after every task: changed files ⊆ task's named files ⊆ whitelist;
          anything else is reverted (whitelist files → task-start snapshot,
          off-whitelist tracked → git checkout, new untracked → deleted)
  2. Compile loop (al + cop analyzers, same referee as /al): FIX_STRATEGY=snippet
     via pi, whitelist gate each round, keep-best on the whitelist snapshot
  3. Optional escalation: ESCALATE_AFTER=<n> hands failed tasks to Claude Code after
     pi's attempts, and latches the compile loop to Claude after n pi fix rounds

Usage:
  python3 run-edit.py --project <root> [--only 1,15,F2] [--dry-run] [--no-build] [--build-only]

Env: ESCALATE_AFTER=<n> arm Claude escalation (default off — no Claude spend),
     EDIT_TASK_TIMEOUT (default 600s per pi task), EDIT_PI_ATTEMPTS (default 2),
     PI_CODER_MODEL, MAX_FIX_ROUNDS via run-build defaults.

Handover contract (larry-handover.prompt.md in the project root):
  - tasks under '## Task <n> — …' / '## Feature F<n> — …' headings
  - exact edits as 'File: `rel/path`' + FIND:/REPLACE: fenced blocks
  - whitelist under a heading containing 'machine-readable manifest'
"""

import importlib.util
import json
import os
import re
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import pathguard
import snippet_fix
import bonsai_vram   # Mode B GPU time-share: evict the Bonsai chat server before loading the coder

# run-build.py owns the shared plumbing (compiler, symbols, pi/claude runners, metrics);
# hyphenated filename → load by path.
_spec = importlib.util.spec_from_file_location("run_build", os.path.join(HERE, "run-build.py"))
rb = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(rb)

MAX_FIX_ROUNDS   = rb.MAX_FIX_ROUNDS
EDIT_TASK_TIMEOUT = int(os.environ.get("EDIT_TASK_TIMEOUT", "600"))
EDIT_PI_ATTEMPTS  = int(os.environ.get("EDIT_PI_ATTEMPTS", "2"))
INLINE_CAP        = 60_000   # max bytes of file content inlined into a task prompt

_esc = os.environ.get("ESCALATE_AFTER", "").strip()
ESCALATE = int(_esc) if _esc.isdigit() else None


# ---------------------------------------------------------------------------
# Handover parsing
# ---------------------------------------------------------------------------

_HEAD_RE  = re.compile(r"^#{1,2}\s+.*$", re.M)
_TASK_RE  = re.compile(r"^##\s+(?:Task|Feature)\s+(\S+)\s*[—-]", )
_FILE_RE  = re.compile(r"File:?\s*`([^`]+)`")
_PAIR_RE  = re.compile(
    r"FIND:\s*\n```[^\n]*\n(.*?)\n```\s*\nREPLACE:\s*\n```[^\n]*\n(.*?)\n```", re.DOTALL)
_FENCE_RE = re.compile(r"^```", re.M)
_LABEL_RE = re.compile(r"^(?:\d+[a-z]|F\d+[a-z])\.", re.M)


def parse_tasks(text):
    """Split the handover into task sections → [{id, title, body}]."""
    heads = list(_HEAD_RE.finditer(text))
    tasks = []
    for i, h in enumerate(heads):
        m = _TASK_RE.match(h.group(0))
        if not m:
            continue
        end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
        tasks.append({"id": m.group(1), "title": h.group(0).lstrip("# ").strip(),
                      "body": text[h.start():end].strip()})
    return tasks


def task_files(body, root):
    """Relative paths named by 'File: `…`' in a task body."""
    out = []
    for rel in _FILE_RE.findall(body):
        rel = rel.strip()
        if rel not in out:
            out.append(rel)
    return out


def task_pairs(body):
    """FIND/REPLACE pairs with their governing file → [(relpath|None, find, replace)].
    A pair belongs to the nearest preceding 'File:' mention."""
    files = [(m.start(), m.group(1).strip()) for m in _FILE_RE.finditer(body)]
    pairs = []
    for m in _PAIR_RE.finditer(body):
        owner = None
        for pos, rel in files:
            if pos < m.start():
                owner = rel
        pairs.append((owner, m.group(1), m.group(2)))
    return pairs


def deterministic_eligible(body, pairs):
    """A task is safe to apply without a model ONLY when its edits are wholly
    expressed as FIND/REPLACE pairs. Guards:
      - every fenced block is part of a pair (a lone block = prose instruction, e.g.
        'add this procedure' — needs the model)
      - sub-labels (15a., F1b., …) must equal the pair count (F3c 'identical to F3b'
        style prose sub-edits would otherwise be silently dropped)
      - every pair names a file
    """
    if not pairs or any(p[0] is None for p in pairs):
        return False
    fence_lines = len(_FENCE_RE.findall(body))   # 2 fence lines per ``` block
    if fence_lines % 2 or fence_lines // 2 != 2 * len(pairs):
        return False
    labels = len(_LABEL_RE.findall(body))
    if labels and labels != len(pairs):
        return False
    return True


# ---------------------------------------------------------------------------
# Exact application (all-or-nothing per task)
# ---------------------------------------------------------------------------

def locate(content, find):
    """('exact'|'ws'|'ambig'|'miss', span). ws = trailing-whitespace-tolerant."""
    n = content.count(find)
    if n == 1:
        return "exact", None
    if n > 1:
        return "ambig", None
    hit = snippet_fix._find_span(content.split("\n"), find.split("\n"))
    return ("ws", hit) if hit else ("miss", None)


def apply_pairs(pairs, root):
    """Apply a task's FIND/REPLACE pairs. All must locate first (all-or-nothing);
    returns (ok, notes). Caller holds the snapshot for revert."""
    notes = []
    located = []
    for rel, find, repl in pairs:
        # `rel` comes from the handover's `File:` lines — untrusted text that we are
        # about to WRITE to. enforce_gate() cannot catch an escape here: it reverts from
        # git status, which never reports a path outside the repo.
        try:
            path = pathguard.safe_join(root, rel)
        except pathguard.PathEscape as e:
            return False, [f"REJECTED (escapes root): {rel} — {e}"]
        try:
            content = open(path).read()
        except OSError:
            return False, [f"no file: {rel}"]
        how, span = locate(content, find)
        if how in ("ambig", "miss"):
            return False, [f"FIND {how} in {rel}"]
        located.append((path, rel, find, repl, how))
    for path, rel, find, repl, how in located:
        content = open(path).read()
        if how == "exact" or find in content:
            open(path, "w").write(content.replace(find, repl, 1))
        else:
            lines = content.split("\n")
            span = snippet_fix._find_span(lines, find.split("\n"))
            if span is None:
                return False, [f"FIND drifted in {rel} (earlier pair overlapped?)"]
            i, j = span
            open(path, "w").write("\n".join(lines[:i] + repl.split("\n") + lines[j:]))
        notes.append(f"applied ({how}): {rel}")
    return True, notes


# ---------------------------------------------------------------------------
# git ground truth + gate
# ---------------------------------------------------------------------------

def git(root, *args, check=True):
    r = subprocess.run(["git", "-C", root, *args], capture_output=True, text=True)
    if check and r.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)}: {r.stderr.strip()}")
    return r.stdout


def git_status(root):
    """(tracked_changed, untracked) as sets of relative paths."""
    tracked, untracked = set(), set()
    for ln in git(root, "status", "--porcelain", "-uall").splitlines():
        st, path = ln[:2], ln[3:].strip().strip('"')
        (untracked if st == "??" else tracked).add(path)
    return tracked, untracked


def snapshot(paths):
    return {p: open(p).read() for p in paths if os.path.exists(p)}


def restore_snapshot(snap):
    """Put snapshotted files back exactly (recreates deleted ones too)."""
    for p, c in snap.items():
        if not os.path.exists(p) or open(p).read() != c:
            open(p, "w").write(c)


def enforce_gate(root, whitelist_abs, allowed_abs, snap, base_untracked, label):
    """Revert anything a coder touched outside `allowed_abs`. Whitelist files revert
    to the task-start snapshot (preserving earlier tasks); off-whitelist tracked files
    revert to git HEAD; new untracked files are deleted. Returns list of reverts."""
    reverted = []
    tracked, untracked = git_status(root)
    for rel in sorted(tracked):
        ap = os.path.join(root, rel)
        if ap in allowed_abs:
            continue
        if ap in whitelist_abs:
            if ap in snap and (not os.path.exists(ap) or open(ap).read() != snap[ap]):
                open(ap, "w").write(snap[ap])
                reverted.append(rel)
        else:
            git(root, "checkout", "--", rel)
            reverted.append(rel)
    for rel in sorted(untracked - base_untracked):
        ap = os.path.join(root, rel)
        if os.path.isfile(ap):
            os.remove(ap)
            reverted.append(rel + " (new file, deleted)")
    if reverted:
        print(f"  GATE [{label}]: reverted off-limits changes:")
        for r in reverted:
            print(f"    - {r}")
    return reverted


def changed_within(root, snap):
    """Whitelist files whose content differs from a snapshot → [relpaths]."""
    out = []
    for p, old in snap.items():
        if not os.path.exists(p) or open(p).read() != old:
            out.append(os.path.relpath(p, root))
    return sorted(out)


# ---------------------------------------------------------------------------
# Model attempts (pi first, Claude escalation)
# ---------------------------------------------------------------------------

EDIT_INSTRUCTIONS = """\
Apply ONLY the task above. Do NOT rewrite files. Output ONE OR MORE edit blocks in
EXACTLY this format and nothing else (no prose, no code fences):

FILE: <relative/path/from/project/root>
<<<<<<< SEARCH
<the exact existing lines to replace — copy them verbatim, incl. indentation>
=======
<the corrected lines>
>>>>>>> REPLACE

Rules:
- SEARCH text MUST match current file content exactly (whitespace included).
- To INSERT code, SEARCH for the nearest unique anchor lines and REPLACE with
  anchor + new code (or new code + anchor), per the task's placement instruction.
- To DELETE code, SEARCH for the full span to remove and put the surrounding
  kept lines (or nothing between the markers) in REPLACE.
- Keep each SEARCH small and unique. One block per distinct edit.
- Touch ONLY the file(s) named in the task."""


AL_BRAIN = os.environ.get("AL_BRAIN") == "1"


def _project_profile(root):
    """AL-14 project profile for the edit prompt. Off by default.

    Edit work is where this has a chance of mattering: the repo already has objects, so
    the profile carries a real inventory instead of the "objects: none" a greenfield build
    starts with. Fail-open — a profile problem must never block an edit.
    """
    if not AL_BRAIN:
        return ""
    try:
        import al_brain
        return "\n\nPROJECT PROFILE (deterministic, generated from this source):\n" \
               + al_brain.as_prompt_context(al_brain.build(root)) + "\n"
    except Exception as e:
        print(f"  (project profile unavailable: {e})")
        return ""


def build_task_prompt(root, task, files):
    parts = [f"Project root: {root}/\n\nYou are applying ONE edit task to an existing "
             f"Business Central AL project.{_project_profile(root)}\n\nTASK:\n{task['body']}"]
    inlined = 0
    for rel in files:
        # Guarded on READ too: this content is inlined into a prompt that may reach a
        # cloud model, so an unguarded path is a disclosure route, not just a write risk.
        try:
            path = pathguard.safe_join(root, rel)
        except pathguard.PathEscape:
            parts.append(f"\n(file {rel} rejected — outside the project root)")
            continue
        if not os.path.exists(path):
            continue
        content = open(path).read()
        if inlined + len(content) > INLINE_CAP:
            parts.append(f"\n(file {rel} too large to inline — read it with your read tool)")
            continue
        inlined += len(content)
        parts.append(f"\n=== CURRENT CONTENT: {rel} ===\n{content}")
    parts.append("\n---\n\n" + EDIT_INSTRUCTIONS)
    return "\n".join(parts)


def pi_task_attempt(root, task, files, label):
    """One read-only pi run for one task; blocks applied deterministically."""
    out = rb.run_pi(build_task_prompt(root, task, files), label=label,
                    allow_write=False, timeout=EDIT_TASK_TIMEOUT)
    ap, fl, details = snippet_fix.apply_edit_blocks(out, root)
    for d in details:
        print(f"    {d}")
    return ap, fl


def claude_task_attempt(root, task, files, label):
    """Claude Code applies one task directly (it has a reliable Edit tool)."""
    prompt = (f"Apply ONE edit task to the existing AL project at {root}.\n\n"
              f"TASK:\n{task['body']}\n\n"
              f"Rules: modify ONLY {', '.join(files) if files else 'the files the task names'}; "
              f"apply exactly this task, nothing else; do not create new files; "
              f"do not compile; make the edits with your Edit tool.")
    rb.run_claude_code(prompt, label=label, timeout=EDIT_TASK_TIMEOUT)


# ---------------------------------------------------------------------------
# Compile (referee) — bare al + cop analyzers; NO normalizers (they are greenfield
# transforms that walk all of src/ and may touch files outside the whitelist)
# ---------------------------------------------------------------------------

def compile_project(root):
    print("\n--- AL compile (with cop analyzers) ---")
    cache = root + "/.alpackages"
    if not (os.path.isdir(cache) and os.listdir(cache)):
        cache = rb.mcp_download_symbols()
        if not cache:
            return "BUILD: FAILED\nsymbol download failed", False
    sarif = root + "/.build-errors.sarif"
    cmd = [rb.AL_CLI, "compile", f"/project:{root}", f"/packagecachepath:{cache}",
           f"/errorlog:{sarif}"]
    cmd += [f"/analyzer:{d}" for d in rb._analyzer_dlls()]
    r = subprocess.run(cmd, capture_output=True, text=True)
    out = (r.stdout + r.stderr).strip()
    ok = r.returncode == 0
    try:
        os.remove(sarif)
    except OSError:
        pass
    print(f"  Build {'PASSED' if ok else 'FAILED'}")
    if not ok:
        for ln in rb.truncate_build(out).splitlines():
            print(f"  {ln}")
    return out, ok


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    try:
        sys.stdout.reconfigure(line_buffering=True)
    except Exception:
        pass
    t0 = time.time()
    args = sys.argv[1:]
    dry_run    = "--dry-run"    in args
    no_build   = "--no-build"   in args
    build_only = "--build-only" in args
    only = None
    if "--only" in args:
        only = {s.strip() for s in args[args.index("--only") + 1].split(",")}
    if "--project" not in args:
        print("ERROR: --project <root> required.")
        sys.exit(1)
    root = args[args.index("--project") + 1].rstrip("/")

    rb.configure_project(root)          # sets rb.PROJECT_ROOT + whitelist + egress policy
    whitelist = rb.EXPECTED_FILES       # may-modify semantics here, not must-exist
    if not whitelist:
        print("ERROR: no whitelist parsed from handover manifest. Aborting.")
        sys.exit(1)
    whitelist_abs = set(whitelist)

    # --- Preflight: git is the safety net; require it and a clean tracked tree ----
    try:
        git(root, "rev-parse", "--is-inside-work-tree")
    except Exception:
        print("ERROR: edit flow requires a git repo (revert + diff gates). git init first.")
        sys.exit(1)
    tracked0, base_untracked = git_status(root)
    # Dirty whitelist files are this flow's own workspace (resume/--only rerun after a
    # partial round). Dirt OUTSIDE the whitelist is someone else's uncommitted work —
    # the gates would revert it to HEAD, so refuse to run over it.
    foreign = {f for f in tracked0 if os.path.join(root, f) not in whitelist_abs}
    if foreign and not dry_run:
        print("ERROR: uncommitted changes outside the whitelist — commit or stash first:")
        for f in sorted(foreign):
            print(f"  {f}")
        sys.exit(1)
    if tracked0 and not dry_run:
        print(f"Resuming over {len(tracked0)} already-modified whitelist file(s) (uncommitted edit round).")

    escalate = ESCALATE
    if escalate is not None:
        ok, reason = rb.egress_policy.escalation_available()
        if not ok:
            print(f"Escalation: DISARMED by egress policy — {reason}.")
            escalate = None
        elif not os.path.exists(rb.CLAUDE_BIN):
            print(f"ERROR: ESCALATE_AFTER set but Claude bin missing at {rb.CLAUDE_BIN}.")
            sys.exit(1)
        else:
            print(f"Escalation: ARMED — failed tasks go to Claude; compile loop latches "
                  f"to Claude after {escalate} pi round(s).")
    else:
        print("Escalation: off (pi only, no Claude spend — set ESCALATE_AFTER=N to arm).")

    tasks = parse_tasks(rb.read_handover())
    if only is not None:
        tasks = [t for t in tasks if t["id"] in only]
    print(f"Tasks parsed: {len(tasks)}" + (f" (filtered by --only)" if only else ""))

    # --- Dry run: report the plan, touch nothing --------------------------------
    if dry_run:
        print("\nDRY RUN — per-task plan:")
        for t in tasks:
            pairs = task_pairs(t["body"])
            det = deterministic_eligible(t["body"], pairs)
            status = []
            if det:
                for rel, find, _ in pairs:
                    how, _s = locate(open(os.path.join(root, rel)).read(), find) \
                        if os.path.exists(os.path.join(root, rel)) else ("no-file", None)
                    status.append(how)
                mode = "DETERMINISTIC" if all(s in ("exact", "ws") for s in status) \
                    else f"MODEL (FIND {','.join(status)})"
            else:
                mode = "MODEL (prose/insert/delete task)"
            print(f"  [{t['id']:>3}] {mode:<28} pairs={len(pairs)}  {t['title'][:70]}")
        return

    # --- Task loop ---------------------------------------------------------------
    ledger = []
    warmed = False
    for t in ([] if build_only else tasks):
        print(f"\n=== {t['title']} ===")
        files = task_files(t["body"], root)
        pairs = task_pairs(t["body"])
        allowed_abs = {os.path.join(root, f) for f in files} or whitelist_abs
        snap = snapshot(whitelist_abs)
        entry = {"id": t["id"], "title": t["title"], "method": None,
                 "changed": [], "status": "FAILED"}

        # a) deterministic
        if deterministic_eligible(t["body"], pairs):
            ok, notes = apply_pairs(pairs, root)
            for n in notes:
                print(f"    {n}")
            if ok:
                entry["method"] = "deterministic"
            else:
                restore_snapshot(snap)             # all-or-nothing revert
                print("  deterministic apply incomplete — handing task to the model")

        # b) pi, one task per invocation
        if entry["method"] is None:
            if not warmed:
                rb.prewarm_coder()
                warmed = True
            for attempt in range(1, EDIT_PI_ATTEMPTS + 1):
                ap, fl = pi_task_attempt(root, t, files or
                                         [os.path.relpath(p, root) for p in whitelist],
                                         label=f"pi-task-{t['id']}-try{attempt}")
                enforce_gate(root, whitelist_abs, allowed_abs, snap, base_untracked,
                             f"task {t['id']}")
                if ap and changed_within(root, snap):
                    # unmatched blocks were never applied → harmless (e.g. rerunning a
                    # multi-part task whose other sub-edits already landed); warn only
                    if fl:
                        print(f"  note: {fl} unmatched block(s) skipped")
                    entry["method"] = f"pi (attempt {attempt})"
                    break
                restore_snapshot(snap)             # revert partial damage before retry
                print(f"  pi attempt {attempt} rejected ({ap} applied, {fl} unmatched)")

        # c) Claude escalation per failed task
        if entry["method"] is None and escalate is not None:
            claude_task_attempt(root, t, files, label=f"claude-task-{t['id']}")
            enforce_gate(root, whitelist_abs, allowed_abs, snap, base_untracked,
                         f"task {t['id']} (claude)")
            if changed_within(root, snap):
                entry["method"] = "claude"

        entry["changed"] = changed_within(root, snap)
        # never trust self-report: changed files on disk = the only success signal
        if entry["method"] and entry["changed"]:
            entry["status"] = "APPLIED"
        elif entry["method"] == "deterministic" and not entry["changed"]:
            entry["status"] = "NO-OP"           # replace == find? shouldn't happen
        print(f"  → {entry['status']}"
              + (f" via {entry['method']}: {', '.join(entry['changed'])}" if entry["changed"] else ""))
        ledger.append(entry)

    if build_only:
        ledger = []

    # --- Compile loop (keep-best on whitelist snapshot) ---------------------------
    build_ok = None
    fix_rounds_used = 0
    escalated = False
    if not no_build:
        best = {"errs": None, "snap": None}
        backend = "pi"
        for rnd in range(MAX_FIX_ROUNDS + 1):
            out, ok = compile_project(root)
            errs = rb.count_build_errors(out, ok)
            print(f"  error score: {errs}")
            if best["errs"] is None or errs < best["errs"]:
                best = {"errs": errs, "snap": snapshot(whitelist_abs)}
            if ok:
                build_ok = True
                break
            if rnd >= MAX_FIX_ROUNDS:
                break
            if escalate is not None and backend == "pi" and rnd >= escalate:
                backend = "claude"
                escalated = True
                print("  ⚠ ESCALATION: compile loop hands to Claude Code (billed per-token).")
            fix_rounds_used = rnd + 1
            findings = rb.truncate_build(out)
            snap = snapshot(whitelist_abs)
            print(f"\n--- fix round {rnd + 1} ({backend}, snippet) ---")
            if backend == "claude":
                rb.run_claude_code(rb.build_fix_msg(findings), label="claude-compilefix")
            else:
                fix_out = rb.run_pi(snippet_fix.build_snippet_prompt(
                    root, findings, rb.get_project_file_listing()),
                    label="pi-compilefix", allow_write=False)
                ap, fl, _ = snippet_fix.apply_edit_blocks(fix_out, root)
                print(f"  snippet-fix: {ap} applied, {fl} unmatched")
            enforce_gate(root, whitelist_abs, whitelist_abs, snap, base_untracked,
                         f"fix round {rnd + 1}")
        if not build_ok and best["snap"]:
            print("  restoring best-scoring state")
            restore_snapshot(best["snap"])
            build_ok = False

    # --- Final report: git is the truth -------------------------------------------
    print("\n" + "=" * 60)
    print("EDIT-FLOW REPORT (ground truth: git diff)")
    print("=" * 60)
    applied = [e for e in ledger if e["status"] == "APPLIED"]
    failed  = [e for e in ledger if e["status"] != "APPLIED"]
    for e in ledger:
        mark = "✓" if e["status"] == "APPLIED" else "✗"
        print(f"  {mark} [{e['id']:>3}] {e['status']:<8} {e['method'] or '-':<22} "
              f"{', '.join(e['changed']) or '-'}")
    print("-" * 60)
    print(git(root, "diff", "--stat").rstrip() or "  (no changes)")
    print("=" * 60)

    rb.emit_metrics({
        "mode": "edit",
        "project": os.path.basename(root),
        "coder_model": rb.CODER_MODEL,
        "duration_s": int(time.time() - t0),
        "tasks_total": len(ledger),
        "tasks_applied": len(applied),
        "tasks_deterministic": sum(1 for e in applied if e["method"] == "deterministic"),
        "tasks_pi": sum(1 for e in applied if (e["method"] or "").startswith("pi")),
        "tasks_claude": sum(1 for e in applied if e["method"] == "claude"),
        "tasks_failed": len(failed),
        "final_compile": build_ok,
        "fix_rounds": fix_rounds_used,
        "claude_escalated": escalated,
    })

    if failed:
        print(f"\nFAILED TASKS ({len(failed)}): " + ", ".join(e["id"] for e in failed))
    if build_ok is False:
        print("\nRESULT: FAIL (build not green — best state restored)")
        sys.exit(1)
    if failed:
        print(f"\nRESULT: PARTIAL — {len(applied)}/{len(ledger)} tasks applied, build "
              + ("green" if build_ok else "not run") + ". Review with git diff; rerun "
              f"failed tasks via --only {','.join(e['id'] for e in failed)}"
              + (" (or arm ESCALATE_AFTER for Claude)." if escalate is None else "."))
        sys.exit(2)
    print("\nRESULT: PASS — all tasks applied"
          + (", build green." if build_ok else " (build skipped)."))


if __name__ == "__main__":
    main()
