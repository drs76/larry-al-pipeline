#!/usr/bin/env python3
"""test_board.py — offline unit tests for board.py (no Kanboard, no gh, no network).

Covers the pure, load-bearing logic: the `Ticket:` trailer parser, the local→github URL
rewrite (the risky-20% transform), the secret-scan regex, and the egress github gate.
The live Kanboard/gh paths are exercised by board_smoke.sh (needs the env). CI-safe.

    python3 test_board.py    # exit 0 = all pass
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import board
import egress_policy as ep

CASES = []


def ok(name, cond):
    CASES.append((name, bool(cond)))
    print(f"  [{'OK ' if cond else 'FAIL'}] {name}")


def main():
    # ── Ticket: trailer parsing ──
    ok("trailer parsed", board.ticket_of("feat: x\n\nTicket: T-42") == 42)
    ok("trailer case-insensitive", board.ticket_of("ticket: T-7") == 7)
    ok("no trailer → None", board.ticket_of("just a message") is None)
    ok("trailer must be a full line", board.ticket_of("see Ticket: T-9 inline") is None)

    # ── URL rewrite (the risky-20% transform) ──
    proto, repo = "/x/proto", "https://github.com/drs76/proto"
    ok("doc → blob url",
       board._rewrite_url(f"file://{proto}/docs/SPEC.md", proto, repo, "main")
       == f"{repo}/blob/main/docs/SPEC.md")
    ok("commit → commit url",
       board._rewrite_url(f"file://{proto}#commit=deadbeef", proto, repo, "main")
       == f"{repo}/commit/deadbeef")
    ok("respects branch",
       board._rewrite_url(f"file://{proto}/a.md", proto, repo, "dev").endswith("/blob/dev/a.md"))
    ok("already-github url → None (idempotent)",
       board._rewrite_url(f"{repo}/blob/main/a.md", proto, repo, "main") is None)
    ok("foreign file url → None",
       board._rewrite_url("file:///other/x.md", proto, repo, "main") is None)

    # ── secret scan regex ──
    for s in ["sk-abcdefghijklmnopqrstuvwx", "ghp_ABCDEFGHIJKLMNOPQRSTUVWXYZ012345",
              "AKIA1234567890ABCDEF", "OPENROUTER_API_KEY=sk-or-v1-xyz",
              "-----BEGIN OPENSSH PRIVATE KEY-----"]:
        ok(f"secret detected: {s[:14]}…", board.SECRET_RE.search(s) is not None)
    ok("clean text not flagged", board.SECRET_RE.search("just some normal source code") is None)

    # ── egress github gate (the hard constraint) ──
    for prof, want in [("local-only", False), ("enterprise-anon", False),
                       ("cloud-mid", False), ("personal", True)]:
        ep._policy = prof
        ok(f"github gate {prof}={want}", ep.allowed("github")[0] is want)

    passed = sum(1 for _, c in CASES if c)
    print(f"\n{'PASS' if passed == len(CASES) else 'FAIL'} — {passed}/{len(CASES)} checks")
    raise SystemExit(0 if passed == len(CASES) else 1)


if __name__ == "__main__":
    main()
