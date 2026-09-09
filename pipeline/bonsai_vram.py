"""bonsai_vram.py — hand the GPU back from the Bonsai chat server before a build.

Mode B time-share (see setup/tower/bonsai/bonsai-context.md): bonsai-llama
(Ternary-27B, ~9.5GB) and the ~18GB coder cannot co-reside on the 24GB card. When
both are resident ollama spills the coder to CPU (measured: 33%/67% CPU/GPU on
qwen3-coder:30b) and the write phase thrashes until it times out at 1200s.

Two ways to stop it, tried in order:

  1. `bonsai off` — the CLI, but it lives ONLY on Larry (/usr/local/bin/bonsai,
     shells `doas systemctl`). On a client box it raises FileNotFoundError.
  2. The larry-dashboard maintenance API over TLS+basic-auth:
       POST https://larry.home.arpa/dash/api/action/bonsai-off
     which runs the same `doas systemctl stop bonsai-llama` on Larry. This is the
     path that makes eviction work from deb / WSL / thinkpad, where every build
     before 2026-08-07 silently skipped it.

Credentials, same contract as ~/.pi/bonsai-control.ts (never hard-coded here — this
file is committed):
  1. env LARRY_DASH_AUTH   ("user:pass")
  2. file ~/.pi/.larry-dash-auth  (one line "user:pass", chmod 600)

Best-effort throughout: no bonsai on this network, an already-stopped server, or
missing creds are all fine and quiet. A stop that is ATTEMPTED and FAILS is loud —
silence there previously cost hours, because contention is indistinguishable from a
model fault.

POLICY (decided 2026-09-01)
---------------------------
Eviction is UNCONDITIONAL. A build stops the chat server whether or not somebody is
mid-conversation, and that is a deliberate choice, not an oversight: the health endpoint
returns only {"status":"ok"} with no last-request timestamp or session count, so
"refuse if recently active" is not implementable without new instrumentation on the
Bonsai side. Recording it here so the next reader knows it was considered and why it was
not done.

What WAS a defect: never giving the card back. restore_bonsai() now returns it, and only
if this process is the one that took it — never start a service the user had off.

Restore is not free. `bonsai on` evicts the coder in turn, so the next build pays a cold
load (~22s measured). Right for a one-off build with someone waiting; wrong between runs
of a benchmark suite, which would thrash the card both ways every run.

  BONSAI_EVICT=0    skip eviction entirely (deliberately share the card)
  BONSAI_RESTORE=0  evict but do NOT restore — set by bench-run-suite.sh for a suite

WHERE THIS FIX STOPS
--------------------
atexit is not a finally block. SIGKILL, a hard `pkill -9`, an OOM kill or power loss all
bypass Python cleanup, and Bonsai then stays down with no build running to explain it.
That state is self-inflicted-looking and easy to misdiagnose as "the chat server crashed".

It is also not rare: several builds were killed with `pkill -9` during the 2026-08-31
wedge investigation, and each would have left the card orphaned had restore existed then.

The next build does NOT rescue it. free_bonsai_vram() returns early when `is_up()` is
false, so `we_stopped_it` stays False and nothing is restored — correctly, because that
process did not take it. Recovery is `bonsai on`, or the dashboard.

If the executor ever becomes a long-lived service rather than a per-build process, this
belongs at supervisor level — ownership and reconciliation — rather than in a child
process's exit hook.
"""

import os
import subprocess

# Did THIS process stop the chat server? Restore is conditional on it: never start a
# service the user deliberately had off.
_state = {"we_stopped_it": False}

HEALTH = os.environ.get("BONSAI_HEALTH_URL", "https://larry.home.arpa:8444/health")
DASH   = os.environ.get("LARRY_DASH_URL", "https://larry.home.arpa/dash") + "/api/action"


def _curl(args, timeout=20):
    """Shell curl so the system CA store is used (it already trusts the HomeLab CA),
    dodging Python's separate certifi bundle. Returns (ok, output)."""
    try:
        r = subprocess.run(["curl", *args], capture_output=True, text=True, timeout=timeout)
        return r.returncode == 0, (r.stdout or "") + (r.stderr or "")
    except FileNotFoundError:
        return False, "curl not found"
    except Exception as e:
        return False, str(e)


def _creds():
    if os.environ.get("LARRY_DASH_AUTH"):
        return os.environ["LARRY_DASH_AUTH"]
    try:
        with open(os.path.expanduser("~/.pi/.larry-dash-auth")) as f:
            return f.read().strip() or None
    except Exception:
        return None


def is_up(timeout=4):
    """True if the Bonsai server is answering — i.e. it is holding VRAM right now."""
    ok, _ = _curl(["-fsS", "--max-time", str(timeout), HEALTH], timeout=timeout + 3)
    return ok


def _stop_via_cli():
    """Larry-local path. Returns (attempted, ok, detail)."""
    try:
        r = subprocess.run(["bonsai", "off"], capture_output=True, text=True, timeout=30)
        return True, r.returncode == 0, (r.stdout or r.stderr or "").strip()
    except FileNotFoundError:
        return False, False, "no bonsai CLI on this host"   # expected on clients
    except Exception as e:
        return True, False, str(e)


def _stop_via_dashboard():
    """Client path — the dashboard runs the systemctl stop on Larry.
    Returns (attempted, ok, detail)."""
    auth = _creds()
    if not auth:
        return False, False, ("no dashboard creds — set LARRY_DASH_AUTH=user:pass or write "
                              "~/.pi/.larry-dash-auth (chmod 600)")
    ok, out = _curl(["-fsS", "--max-time", "30", "-u", auth, "-X", "POST", f"{DASH}/bonsai-off"],
                    timeout=35)
    return True, ok, out.strip()[:200]


_freed_once = False


def free_bonsai_vram_once(verbose=True):
    """free_bonsai_vram(), but does the work at most once per process.

    Cheap enough to call from the run_pi funnel, so every path that loads the local
    coder is covered — including ones that never go through prewarm (e.g.
    `run-edit.py --build-only`, whose fix rounds call run_pi directly).
    """
    global _freed_once
    if _freed_once:
        return True
    _freed_once = True
    return free_bonsai_vram(verbose=verbose)


def free_bonsai_vram(verbose=True):
    """Stop the Bonsai chat server if it is holding the GPU, so the coder can load.

    Returns True if the card is free afterwards (either it was already, or we
    stopped it), False if Bonsai is still up and the coder will contend.
    """
    def say(m):
        if verbose:
            print(m)

    if os.environ.get("BONSAI_EVICT", "1") == "0":
        say("  bonsai: eviction disabled (BONSAI_EVICT=0) — coder may share VRAM")
        return True

    if not is_up():
        return True                       # not running (or no bonsai here at all) — quiet

    say("  bonsai: chat server is holding the GPU — stopping it so the coder gets the card")

    attempted, ok, detail = _stop_via_cli()
    if not attempted:                     # client box: no CLI, use the dashboard
        attempted, ok, detail = _stop_via_dashboard()

    if not attempted:
        say(f"  WARNING: cannot stop bonsai ({detail}). It is holding ~9.5GB; on a 24GB "
            f"card the coder spills to CPU and the write phase can time out. Stop it "
            f"manually (`/bonsai off` in pi, or the dashboard) and re-run.")
        return False

    if not ok:
        say(f"  WARNING: `bonsai off` failed ({detail or 'no detail'}) — expect VRAM contention")
        return False

    # Trust nothing: confirm it actually let go before we load 18GB on top.
    if is_up():
        say("  WARNING: bonsai reported stopped but is still answering — expect contention")
        return False

    say("  bonsai: stopped, VRAM freed")
    _state["we_stopped_it"] = True
    if os.environ.get("BONSAI_RESTORE", "1") != "0":
        import atexit
        atexit.register(restore_bonsai)
    return True


def _start_via_cli():
    try:
        r = subprocess.run(["bonsai", "on"], capture_output=True, text=True, timeout=90)
        return True, r.returncode == 0, (r.stdout or r.stderr or "").strip()
    except FileNotFoundError:
        return False, False, "no bonsai CLI on this host"
    except Exception as e:
        return True, False, str(e)


def _start_via_dashboard():
    auth = _creds()
    if not auth:
        return False, False, "no dashboard credentials"
    ok, out = _curl(["-fsS", "--max-time", "90", "-u", auth, "-X", "POST", f"{DASH}/bonsai-on"],
                    timeout=100)
    return True, ok, out


def restore_bonsai(verbose=True):
    """Give the card back. Only if WE stopped it — never start a service the user had off.

    A build that takes the GPU and never returns it is a bug, not a policy: the chat server
    stayed down for a whole session on 2026-09-01 because nothing ever restarted it, and
    nobody noticed until the eviction path was read.

    NOT free. `bonsai on` evicts the coder in turn ("starting Bonsai-27B ... (coder
    evicted)"), so the next build pays a cold load — measured ~22s. Correct for a one-off
    build with a user waiting; wrong between runs of a benchmark suite, which would thrash
    the card both ways on every run. Suites set BONSAI_RESTORE=0.
    """
    if not _state.get("we_stopped_it"):
        return False
    _state["we_stopped_it"] = False          # never restore twice
    attempted, ok, detail = _start_via_cli()
    if not attempted:
        attempted, ok, detail = _start_via_dashboard()
    if verbose:
        if not attempted:
            print(f"  bonsai: NOT restored ({detail}) — the chat server is still down and "
                  f"this build stopped it. Start it with `bonsai on` or the dashboard.")
        elif ok:
            print("  bonsai: chat server restored")
        else:
            print(f"  WARNING: bonsai restore FAILED ({detail or 'no detail'}) — the chat "
                  f"server is down and this build is why.")
    return ok
