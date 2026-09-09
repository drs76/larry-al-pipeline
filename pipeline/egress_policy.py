"""egress_policy.py — deny-by-default cloud egress gate (anon hook, phase 1).

Single source of truth for whether a build may send content off-box. All three run-build
orchestrators import this and call it from the one function each cloud invocation funnels
through (run_claude_code for Anthropic, run_mid for the OpenRouter mid tier), so escalation
/ review / review-fix cannot bypass it.

Egress TARGETS are gated, all deny-by-default:
  "anthropic"  — the Claude closing rung (subscription)
  "openrouter" — the cheap-cloud MID tier (CODER_BACKEND=mid)
  "github"     — the promote-time github repo + Project mirror (kanban board)

Profiles (resolution: repo .anon/config.yml `policy:` > env EGRESS_POLICY > local-only):
  local-only      (default) — no cloud egress at all; every target hard-blocked
  enterprise-anon           — Anthropic only via the anon hook (CLAUDE_ANON=1); no mid tier, no github
  personal                  — raw Claude + mid tier + github mirror allowed (own box, non-work code)
  cloud-mid                 — mid tier (OpenRouter) only; NOT raw Anthropic, NOT github

Deny-by-default: absent/unknown config → local-only. An unlisted profile grants NO targets.

SCOPE OF THIS GATE — read before claiming "the repo cannot egress".
This gate governs calls the PIPELINE ORCHESTRATES: Claude, the OpenRouter mid tier, and
the GitHub promote mirror. It does NOT confine the network at the OS level, and `pi`
hands local models a shell, so a local model could in principle make its own request.

That is a deliberate **trusted-local-model** boundary (security review T10): local
models are trusted; enforcement stops at orchestrated calls. Anything stronger needs
firewall/network-namespace controls on the build boxes, which is not in place.

The one place this is tightened: patch-emitting runs get a read-only tool ALLOWLIST
(--tools read,grep,find,ls) rather than a deny-list, so they have no shell at all.
See tooling/anon-claude-hook.spec.md §0.
"""
import os
import re

PROFILES = ("local-only", "enterprise-anon", "personal", "cloud-mid")
_policy = "local-only"   # fail-safe default until set_policy_for() runs
# Depth counter, not a bool: nested/retried scrub calls must not disarm the outer one
# on the inner's exit. Deliberately module state — it cannot be set from outside the
# process, which is the whole point of replacing the env-var check.
_scrub_depth = 0

# Non-anthropic targets each profile may reach, deny-by-default. anthropic is
# handled separately in allowed() because enterprise-anon gates it on the anon
# hook. An unlisted profile → empty set → all such targets denied.
_ALLOW = {
    "local-only":      frozenset(),
    "enterprise-anon": frozenset(),                          # anthropic via CLAUDE_ANON only
    "personal":        frozenset({"openrouter", "github"}),  # own box: mid tier + github mirror
    "cloud-mid":       frozenset({"openrouter"}),            # cheap tier only, NOT github
}


def _repo_policy(root):
    """`policy:` from <root>/.anon/config.yml (minimal parse — no yaml dependency)."""
    try:
        with open(os.path.join(root, ".anon", "config.yml")) as f:
            for ln in f:
                m = re.match(r"\s*policy\s*:\s*([A-Za-z0-9_-]+)", ln)
                if m:
                    return m.group(1)
    except OSError:
        pass
    return None


def resolve(root):
    """Effective profile for a project root (does not mutate state)."""
    p = (_repo_policy(root) or os.environ.get("EGRESS_POLICY", "").strip()
         or "local-only")
    if p not in PROFILES:
        print(f"  WARNING: unknown egress policy '{p}' — failing safe to local-only")
        p = "local-only"
    return p


def set_policy_for(root):
    """Resolve + store the active profile. Returns it."""
    global _policy
    _policy = resolve(root)
    return _policy


def policy():
    return _policy


class anon_scrub_active:
    """Arm enterprise-anon egress for the duration of a MANDATORY scrubbed call.

    Only `claude_egress` should use this, and only once the scrubbed mirror exists and
    the secret gate has passed. It is a context manager so the arm cannot outlive the
    call even if the body raises — the previous env-var approach leaked its authority to
    every child process and to anything that ran afterwards in the same shell.
    """

    def __enter__(self):
        global _scrub_depth
        _scrub_depth += 1
        # Still exported for child processes that read it as INFORMATION; it is no
        # longer what authorises anything.
        os.environ["CLAUDE_ANON"] = "1"
        return self

    def __exit__(self, *exc):
        global _scrub_depth
        _scrub_depth = max(0, _scrub_depth - 1)
        if _scrub_depth == 0:
            os.environ.pop("CLAUDE_ANON", None)
        return False


def scrub_active():
    """True while inside the mandatory scrub path (for diagnostics/tests)."""
    return _scrub_depth > 0


def allowed(target="anthropic"):
    """(ok, reason) for an egress to `target`. Deny-by-default for every target."""
    if target == "anthropic":
        if _policy == "personal":
            return True, ""
        if _policy == "enterprise-anon":
            # PROCESS-INTERNAL state, never the environment. CLAUDE_ANON=1 used to be
            # read straight from os.environ, so any caller could export it and buy raw
            # Anthropic egress for an unscrubbed prompt — an env var is not proof that
            # a payload went through the scrub. The mandatory path (claude_egress: build
            # scrubbed mirror -> secret gate -> reverse-map the diff) now arms this flag
            # itself via anon_scrub_active(), and only for the duration of that call.
            if _scrub_depth > 0:
                return True, ""
            return False, ("policy 'enterprise-anon': Anthropic egress only via the anon hook "
                           "— use `anon run` or the pipeline escalation (claude_egress), "
                           "never raw claude")
        return False, (f"policy '{_policy}': Anthropic egress disabled — staying local. "
                       "This is deny-by-default, not a misconfiguration: enable it per "
                       "repo with `policy: enterprise-anon` in <repo>/.anon/config.yml "
                       "(see tooling/anon-config.example.yml), or EGRESS_POLICY for a "
                       "one-off")
    # Non-anthropic targets (e.g. the openrouter mid tier): deny-by-default via
    # the allow map — an unlisted profile grants nothing.
    if target in _ALLOW.get(_policy, frozenset()):
        return True, ""
    return False, (f"policy '{_policy}': egress to '{target}' disabled (deny-by-default)")


def escalation_available():
    """(ok, reason) — can this build reach Claude AT ALL, by any sanctioned route?

    Unlike allowed(), this treats enterprise-anon as OK: the pipeline escalates through
    the anon mirror (claude_egress, phase 5), which arms CLAUDE_ANON itself. Use this
    for arming decisions at startup; allowed() remains the per-call gate.
    cloud-mid has no Anthropic route, so it is NOT escalation-available."""
    if _policy in ("local-only", "cloud-mid"):
        return False, (f"policy '{_policy}': Anthropic egress disabled — staying local. "
                       "This is deny-by-default, not a misconfiguration: enable it per "
                       "repo with `policy: enterprise-anon` in <repo>/.anon/config.yml "
                       "(see tooling/anon-config.example.yml), or EGRESS_POLICY for a "
                       "one-off")
    return True, ""


def mid_available():
    """(ok, reason) — can this build reach the cheap MID tier (OpenRouter)?

    Arming gate for the mid rung, mirroring escalation_available(). openrouter has no
    anon-hook conditional, so this is exactly allowed('openrouter')."""
    return allowed("openrouter")


def github_available():
    """(ok, reason) — may this project mirror to github (repo + Project) on promote?

    Gate for the kanban board's promote-time mirror. github has no anon-hook conditional,
    so this is exactly allowed('github'). local-only/enterprise-anon/cloud-mid → blocked;
    the board stays LOCAL and promote is a log-skip (never a failure)."""
    return allowed("github")
