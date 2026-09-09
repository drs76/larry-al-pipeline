"""Shared coder-spawn mechanics for the AL, Go and C# pipelines.

WHY THIS EXISTS
---------------
run-build.py, run-build-go.py and run-build-cs.py each kept their own copy of run_pi.
The copies were near-identical and drifted, and the drift cost real runs twice in one week:

  * 2026-08-30, `stdin=subprocess.DEVNULL` was applied to run-build.py and claude_egress.py.
    The go and cs copies were missed for two days. That fault had already destroyed a go/cs
    benchmark run (b64forward burned its full 1200s write budget on 2026-08-29) and the cause
    was recorded as unexplained at the time.
  * 2026-08-31, three further stall guards — bounded fix-round timeout, wedged-write
    fail-fast, env-tunable round cap — existed only in the AL pipeline.

Class-level tests catch drift in properties someone has already thought of. They cannot catch
the next divergence in a property nobody has. One implementation can.

WHAT IS SHARED AND WHAT IS NOT
------------------------------
Shared here: the pi spawn itself, its timeout accounting, and the wedge predicates. That is
precisely the surface that broke.

NOT shared, deliberately: run_coder / run_mid / run_claude_code. Those encode each pipeline's
escalation ladder and egress policy, which legitimately differ, and folding them together
would trade a duplication bug for a coupling bug.

The three real differences between the callers are parameters, not forks:
  flags            AL "-p --no-session"; go/cs add "--mode json" and "-a" because default
                   text mode piped to a non-tty produced empty output and no file writes
  allow_write      AL alone has a read-only review path; go/cs never spawn one
  include_stderr   AL folds stderr into the returned text; go/cs return stdout only
"""

import os
import subprocess
import time

import bonsai_vram   # Mode B GPU time-share: evict the Bonsai chat server before the coder


# Did the last coder call end on its timeout rather than by finishing? run_pi returns "" for
# both, and a write loop must be able to tell them apart.
LAST = {"timed_out": False}
# Consecutive fix rounds whose coder call hit its full timeout. Incremented here so it counts
# the call that actually stalled, not a round that merely produced no edits.
FIX_TIMEOUT_STREAK = {"n": 0}


class CoderConfig:
    """Per-pipeline spawn settings. Everything that legitimately differs, in one place."""

    def __init__(self, pi_bin, pi_ext, flags, include_stderr=False, trim_env="PI_TRIM"):
        self.pi_bin = pi_bin
        self.pi_ext = pi_ext
        self.flags = list(flags)
        self.include_stderr = include_stderr
        self.trim_env = trim_env


def run_pi(prompt, cfg, cwd, label="Pi", model=None, allow_write=True,
           timeout=3600, ext=None):
    """Run the Pi coding agent one-shot, non-interactive. Returns pi's final text, or "" if
    it timed out — check LAST["timed_out"] to tell those apart.

    `ext` selects the provider extension; defaults to cfg.pi_ext (Larry/ollama). A mid-tier
    extension is a cloud call and must NOT evict the local chat server as a side effect.
    """
    ext = ext or cfg.pi_ext
    if ext == cfg.pi_ext:
        bonsai_vram.free_bonsai_vram_once()

    cmd = [cfg.pi_bin, "-e", ext, "--model", model] + cfg.flags
    # Trim the coder's context (PI_TRIM=0 to disable): a pipeline run needs only the provider
    # and the built-in read/bash/edit/write tools. Discovery would also load kb-search and
    # searxng extensions, prompt templates and skills — system-prompt weight competing with
    # injected knowledge inside a 32k num_ctx, for tools the handover forbids using anyway.
    if os.environ.get(cfg.trim_env, "1") != "0":
        cmd += ["-ne", "-ns", "-np", "--no-themes"]
    if not allow_write:
        # ALLOW-list, not a deny-list. `-xt write,edit` left Bash enabled, so "read-only run
        # that emits patch text" was not a guaranteed property — a model with shell access can
        # mutate the worktree outside the deterministic SEARCH/REPLACE applier, which is the
        # mechanism the whole edit protocol depends on.
        cmd += ["--tools", "read,grep,find,ls"]

    # Windows: `pi` is an npm .CMD shim run through cmd.exe, which TRUNCATES a multi-line
    # argument at the first newline (verified: a 35-char/2-newline argv arrives as 8 chars).
    # Passing a handover this way delivers only its title line, and builds then pass only
    # because pi happens to read the handover file out of the project itself —
    # non-deterministic, and the cause of occasional "Wrote 0/N expected files" first
    # attempts. Hand it over via pi's @file syntax instead, which arrives intact.
    ptmp = None
    if os.name == "nt" and "\n" in prompt:
        import tempfile
        fd, ptmp = tempfile.mkstemp(prefix="pi-prompt-", suffix=".md", text=True)
        os.close(fd)
        with open(ptmp, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(prompt)
        cmd.append("@" + ptmp)
    else:
        cmd.append(prompt)

    print(f"  Running Pi ({label}, {model})...")
    start = time.time()
    LAST["timed_out"] = False
    try:
        # stdin MUST be /dev/null, never inherited. pi registers fd 0 in its event loop
        # (verified on a wedged process: the epfd watch list carried tfd 0, events
        # EPOLLIN|EPOLLERR|EPOLLHUP) and waits on it. An inherited descriptor that stays open
        # with no data and no EOF — a socket or a pipe, which is what a background job hands
        # down — satisfies none of those three, so pi parks in epoll_wait before opening a
        # single connection. Demonstrated: same command and prompt, /dev/null completes in 2s,
        # an open socketpair and an open pipe both hang past 90s. Server side: ollama logged
        # the prewarm at 300ms then received NOTHING for the whole 1200s. The request was
        # never sent, so this was never a model, context or streaming problem.
        r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True,
                           timeout=timeout, stdin=subprocess.DEVNULL)
    except subprocess.TimeoutExpired:
        print(f"  {label} TIMEOUT after {timeout}s")
        LAST["timed_out"] = True
        FIX_TIMEOUT_STREAK["n"] += 1
        return ""
    finally:
        if ptmp:
            try:
                os.unlink(ptmp)
            except OSError:
                pass

    out = (r.stdout or "")
    if cfg.include_stderr and r.stderr:
        out += "\n" + r.stderr
    print(f"  {label} done in {time.time() - start:.0f}s (exit {r.returncode})")
    return out.strip()


def wedged_write(produced, timed_out, attempt, max_attempts):
    """Is this write attempt a wedge worth abandoning rather than repeating?

    A wedge is the coder burning its ENTIRE timeout and producing NOTHING: measured
    2026-08-30, pi sat at 0.4% CPU in epoll_wait, wrote no files and never exited, three
    times over, turning one bad run into 3600s. Retrying reproduces it exactly.

    Deliberately narrow. A timeout WITH partial output is a coder that ran and was cut off,
    which does recover on a retry; nothing produced WITHOUT a timeout is a fast transient,
    which is the case retries exist for. Only the pair is hopeless.
    """
    return produced == 0 and timed_out and attempt < max_attempts


def fix_loop_exhausted(max_fix_timeouts):
    """True when consecutive fix rounds have each burned their whole budget. Bounding one
    call is not enough on its own: MAX_FIX_ROUNDS x FIX_TIMEOUT can still outlast the bench
    harness cap, and a round that times out having applied nothing is the fix-loop twin of a
    wedged write."""
    return FIX_TIMEOUT_STREAK["n"] >= max_fix_timeouts


def note_round_completed():
    """Reset the streak. An isolated slow round costs one timeout and nothing more."""
    FIX_TIMEOUT_STREAK["n"] = 0
