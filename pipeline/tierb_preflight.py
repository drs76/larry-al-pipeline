#!/usr/bin/env python3
"""tierb_preflight.py — assert the egress and coder configuration BEFORE any billed call.

Same discipline as the arm-isolation preflight: state what the run IS, positively, rather
than inferring it from the absence of an override. Nothing here contacts Anthropic.

    python3 tierb_preflight.py <run-dir>

Exit 0 only if every assertion holds.
"""

import importlib.util
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def _load(name, fn):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fn))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    try:
        spec.loader.exec_module(mod)
    except SystemExit:
        pass
    return mod


def _git(args, cwd):
    try:
        r = subprocess.run(["git"] + args, cwd=cwd, capture_output=True, text=True)
        return r.returncode, r.stdout.strip()
    except OSError as e:
        return 1, str(e)


def main(run_dir):
    egress_policy = _load("egress_policy", "egress_policy.py")
    ok = True

    print("=== Tier B preflight ===")

    # ---- 1. Effective egress policy, resolved the way run-build resolves it -----------
    eff = egress_policy.resolve(run_dir)
    env = os.environ.get("EGRESS_POLICY", "<unset>")
    repo_pol = egress_policy._repo_policy(run_dir)
    print(f"EGRESS_POLICY env          {env}")
    print(f"  <root>/.anon/config.yml  {repo_pol or 'none'}   (repo config OUTRANKS the env var)")
    print(f"  effective                {eff}")
    if eff != "enterprise-anon":
        print(f"  !! FAIL — Tier B is authorised for enterprise-anon only, resolved '{eff}'")
        ok = False

    # ---- 2. Anthropic reachability, and by which route --------------------------------
    egress_policy.set_policy_for(run_dir)
    allowed, reason = egress_policy.allowed("anthropic")
    print(f"\nanthropic allowed right now  {allowed}   {reason[:80]}")
    if eff == "enterprise-anon" and allowed:
        print("  !! FAIL — under enterprise-anon this must be False outside the scrub "
              "context. True here means the gate is armed when it should not be.")
        ok = False
    elif eff == "enterprise-anon":
        print("  ok — denied outside the anon hook, which is the correct resting state; "
              "claude_egress arms it per call via anon_scrub_active()")

    # ---- 3. Scope: what enterprise-anon does NOT grant --------------------------------
    for target in ("openrouter", "github"):
        a, _ = egress_policy.allowed(target)
        print(f"  {target:11} {'ALLOWED' if a else 'denied'}")
        if a:
            print(f"  !! FAIL — authorisation was Anthropic-only; {target} must stay denied")
            ok = False

    # ---- 4. Coder identity ------------------------------------------------------------
    backend = os.environ.get("CODER_BACKEND", "<unset>")
    claude_bin = os.path.expanduser(os.environ.get("CLAUDE_BIN", "~/.local/bin/claude"))
    print(f"\nCODER_BACKEND              {backend}")
    print(f"CLAUDE_BIN                 {claude_bin}  exists={os.path.exists(claude_bin)}")
    print(f"ANTHROPIC_MODEL            {os.environ.get('ANTHROPIC_MODEL', '<unset>')}")
    if backend != "claude":
        print(f"  !! FAIL — Part 1 requires CODER_BACKEND=claude, found '{backend}'")
        ok = False
    if not os.path.exists(claude_bin):
        print("  !! FAIL — claude binary not found")
        ok = False
    for var in ("ESCALATE_AFTER", "ESCALATE_MID_AFTER", "MID_MODEL"):
        if var in os.environ:
            print(f"  !! FAIL — {var}={os.environ[var]} leaked in; Claude is the CODER "
                  f"here, not a rung, and no ladder may be armed")
            ok = False

    # ---- 5. The scrubbed mirror must actually be able to see the sources --------------
    # enterprise-anon routes every call through a git mirror of TRACKED files. A run
    # directory that is inside a repo but ignored by it enumerates zero files: the mirror
    # is empty, the model sees no project, and the run measures nothing.
    rc, inside = _git(["rev-parse", "--is-inside-work-tree"], run_dir)
    _, toplevel = _git(["rev-parse", "--show-toplevel"], run_dir)
    _, tracked = _git(["ls-files"], run_dir)
    n_tracked = len([l for l in tracked.splitlines() if l.strip()])
    print(f"\nmirror viability for {run_dir}")
    print(f"  inside a git work tree   {inside or 'no'}   toplevel={toplevel or 'n/a'}")
    print(f"  tracked files here       {n_tracked}")
    if rc != 0 or inside != "true":
        print("  !! FAIL — anon_workspace.run_workspace raises 'not a git repo'")
        ok = False
    elif n_tracked == 0:
        print("  !! FAIL — inside a repo but zero tracked files (ignored path). The mirror "
              "would be EMPTY: Claude would see no app.json, no handover, no docs, and the "
              "run would measure nothing. This is the blocker, not a warning.")
        ok = False

    # ---- 6. Prove the ACTUAL mirror, not the transport path ---------------------------
    # A fake-coder test shows the patch cycle works. It does not show that THIS run's
    # workspace scrubs into a mirror containing the inputs Claude needs. Build the real
    # mirror with a coder that changes nothing, and assert its contents.
    if ok:
        ok = _mirror_contents_ok(run_dir) and ok

    print("\n=== PREFLIGHT " + ("PASS" if ok else "FAIL") + " ===")
    return 0 if ok else 1


REQUIRED_IN_MIRROR = ("app.json", "docs", "larry-handover.prompt.md")


def _mirror_contents_ok(run_dir):
    """Assert the real scrubbed mirror holds every input, on round 1 AND round 2.

    Round 2 matters as much as round 1: only tracked files are mirrored, so an applied
    patch that is never committed leaves the next round's mirror stale. Verified failing
    before ANON_AUTOCOMMIT existed — round 2's mirror had no src/ at all.
    """
    anon_workspace = _load("anon_workspace", "anon_workspace.py")
    print("\nreal scrubbed mirror (no Anthropic call — the coder writes nothing)")
    ok = True

    def _inspect(store):
        def coder(mirror, _prompt):
            rc, out = _git(["ls-files"], mirror)
            store["tracked"] = len([l for l in out.splitlines() if l.strip()])
            store["top"] = sorted(x for x in os.listdir(mirror) if x != ".git")
            store["handover_bytes"] = 0
            hp = os.path.join(mirror, "larry-handover.prompt.md")
            if os.path.isfile(hp):
                store["handover_bytes"] = os.path.getsize(hp)
            dp = os.path.join(mirror, "docs")
            store["docs_files"] = (len(os.listdir(dp)) if os.path.isdir(dp) else 0)
            store["has_src"] = os.path.isdir(os.path.join(mirror, "src"))
        return coder

    r1 = {}
    try:
        anon_workspace.run_workspace(run_dir, "<preflight — not sent>", _inspect(r1))
    except Exception as e:
        print(f"  !! FAIL — mirror could not be built: {e}")
        return False

    print(f"  mirror tracked files     {r1.get('tracked', 0)}")
    print(f"  mirror top-level         {r1.get('top')}")
    print(f"  handover bytes in mirror {r1.get('handover_bytes', 0)}")
    print(f"  docs/ entries in mirror  {r1.get('docs_files', 0)}")
    if not r1.get("tracked"):
        print("  !! FAIL — mirror tracked-file count is 0")
        ok = False
    for req in REQUIRED_IN_MIRROR:
        if req not in (r1.get("top") or []):
            print(f"  !! FAIL — required input missing from the mirror: {req}")
            ok = False
    if not r1.get("handover_bytes"):
        print("  !! FAIL — the handover is empty in the mirror after scrubbing")
        ok = False
    if not r1.get("docs_files"):
        print("  !! FAIL — docs/ is empty in the mirror")
        ok = False

    # Round-2 freshness: write a file through the mirror, then check the NEXT mirror sees it.
    def _writer(mirror, _prompt):
        os.makedirs(os.path.join(mirror, "src"), exist_ok=True)
        with open(os.path.join(mirror, "src", "_preflight_probe.al"), "w") as fh:
            fh.write('codeunit 50199 "Preflight Probe" { }\n')

    try:
        anon_workspace.run_workspace(run_dir, "<preflight — not sent>", _writer)
        if os.environ.get("ANON_AUTOCOMMIT") == "1":
            subprocess.run(["git", "add", "-A"], cwd=run_dir, capture_output=True)
            subprocess.run(["git", "commit", "-q", "-m", "preflight probe"], cwd=run_dir,
                           capture_output=True,
                           env={**os.environ, "GIT_AUTHOR_NAME": "pipeline",
                                "GIT_AUTHOR_EMAIL": "pipeline@local",
                                "GIT_COMMITTER_NAME": "pipeline",
                                "GIT_COMMITTER_EMAIL": "pipeline@local"})
        r2 = {}
        anon_workspace.run_workspace(run_dir, "<preflight — not sent>", _inspect(r2))
    except Exception as e:
        print(f"  !! FAIL — round-2 mirror could not be built: {e}")
        return False

    print(f"  round-2 mirror sees src/ {r2.get('has_src')}")
    if not r2.get("has_src"):
        print("  !! FAIL — round 2's mirror does not contain the code round 1 wrote. "
              "Every fix round would hand Claude a workspace missing its own output, and "
              "the run would measure 'cannot repair' when the truth is 'cannot see'. "
              "Set ANON_AUTOCOMMIT=1.")
        ok = False

    # Leave the workspace exactly as found.
    subprocess.run(["git", "rm", "-q", "-f", "--ignore-unmatch", "src/_preflight_probe.al"],
                   cwd=run_dir, capture_output=True)
    subprocess.run(["git", "commit", "-q", "-m", "remove preflight probe"], cwd=run_dir,
                   capture_output=True,
                   env={**os.environ, "GIT_AUTHOR_NAME": "pipeline",
                        "GIT_AUTHOR_EMAIL": "pipeline@local",
                        "GIT_COMMITTER_NAME": "pipeline",
                        "GIT_COMMITTER_EMAIL": "pipeline@local"})
    return ok


if __name__ == "__main__":
    sys.exit(main(os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.getcwd()))
