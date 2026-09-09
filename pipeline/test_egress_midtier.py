#!/usr/bin/env python3
"""test_egress_midtier.py — the referee for the mid-tier warplan.

Asserts the full profile x target matrix. The HARD CONSTRAINT: a customer/work
repo (local-only) must block BOTH the mid tier (openrouter) and Anthropic. Run in
pre-commit / CI and as the mid-tier definition-of-done. stdlib only.

    python3 test_egress_midtier.py   # exit 0 = all green, 1 = a gate is wrong
"""
import os
import egress_policy as ep


def check(profile, target, claude_anon, want, scrub=False):
    """`claude_anon` sets the ENV flag — which must no longer authorise anything.
    `scrub` enters the real mandatory scrub path, which is what authorises now."""
    ep._policy = profile
    if claude_anon:
        os.environ["CLAUDE_ANON"] = "1"
    else:
        os.environ.pop("CLAUDE_ANON", None)
    if scrub:
        with ep.anon_scrub_active():
            got, reason = ep.allowed(target)
    else:
        got, reason = ep.allowed(target)
    ok = got is want
    print(f"  [{'OK ' if ok else 'FAIL'}] {profile:16} allowed({target:10}) anon={int(claude_anon)} "
          f"-> {got} (want {want}){'' if ok else '  <-- ' + reason}")
    return ok


def main():
    # (profile, target, claude_anon, expected_allowed)
    matrix = [
        # local-only: NOTHING leaves the box. The core customer-code guarantee.
        ("local-only", "anthropic", False, False),
        ("local-only", "openrouter", False, False),
        ("local-only", "openrouter", True, False),   # CLAUDE_ANON must not help openrouter
        ("local-only", "github", False, False),
        ("local-only", "github", True, False),       # anon hook must not grant github either
        # enterprise-anon: Anthropic only via the hook; NO mid tier, NO github.
        ("enterprise-anon", "anthropic", False, False),
        # A FORGED env flag must NOT authorise egress. This row previously expected
        # True — it encoded the vulnerability the security review found: CLAUDE_ANON=1
        # is not proof the payload was scrubbed, and any caller could export it.
        ("enterprise-anon", "anthropic", True, False),
        ("enterprise-anon", "openrouter", False, False),
        ("enterprise-anon", "openrouter", True, False),
        ("enterprise-anon", "github", False, False),
        ("enterprise-anon", "github", True, False),
        # personal: own box — anthropic + mid + github allowed.
        ("personal", "anthropic", False, True),
        ("personal", "openrouter", False, True),
        ("personal", "github", False, True),
        # cloud-mid: mid tier yes, raw Anthropic NO, github NO.
        ("cloud-mid", "openrouter", False, True),
        ("cloud-mid", "anthropic", False, False),
        ("cloud-mid", "anthropic", True, False),      # anon hook must not grant Opus here
        ("cloud-mid", "github", False, False),
        # unknown profile (defensive): grants nothing.
        ("bogus-unlisted", "anthropic", False, False),
        ("bogus-unlisted", "openrouter", False, False),
        ("bogus-unlisted", "github", False, False),
    ]
    print("egress mid-tier matrix:")
    results = [check(*row) for row in matrix]

    # The other half of the contract. Correcting the forged-flag row to expect BLOCK is
    # only half a test — on its own it would also pass if enterprise egress were simply
    # broken. These prove the MANDATORY scrub path still authorises, that the arm does
    # not leak past the call, and that it grants Anthropic ONLY.
    results.append(check("enterprise-anon", "anthropic", False, True, scrub=True))
    results.append(check("enterprise-anon", "anthropic", False, False))   # no leak after
    results.append(check("enterprise-anon", "openrouter", False, False, scrub=True))
    results.append(check("enterprise-anon", "github", False, False, scrub=True))
    results.append(check("local-only", "anthropic", True, False, scrub=True))  # absolute

    # Arming gates.
    arm = []
    for prof, mid_ok, esc_ok, gh_ok in [
        ("local-only", False, False, False),
        ("enterprise-anon", False, True, False),
        ("personal", True, True, True),
        ("cloud-mid", True, False, False),   # mid armed, Claude NOT, github NOT
    ]:
        ep._policy = prof
        os.environ.pop("CLAUDE_ANON", None)
        m = ep.mid_available()[0]
        e = ep.escalation_available()[0]
        g = ep.github_available()[0]
        good = (m is mid_ok) and (e is esc_ok) and (g is gh_ok)
        arm.append(good)
        print(f"  [{'OK ' if good else 'FAIL'}] {prof:16} mid_available={m} (want {mid_ok})  "
              f"escalation_available={e} (want {esc_ok})  github_available={g} (want {gh_ok})")

    passed = all(results) and all(arm)
    print(f"\n{'PASS' if passed else 'FAIL'} — {sum(results)+sum(arm)}/{len(results)+len(arm)} checks")
    raise SystemExit(0 if passed else 1)


if __name__ == "__main__":
    main()
