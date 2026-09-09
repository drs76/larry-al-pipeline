#!/usr/bin/env python3
"""Seeded 2x2 readout — one row per arm, n=1 per cell.

Every arm starts from the SAME restored fixture with the SAME seeded defect and runs
--skip-larry, so the write phase cannot vary between arms. The only difference is which
of the two interventions is compiled into the run-build.py that executes.

n=1 per cell against a stochastic coder: this separates the arms descriptively, it does
not estimate an effect. Read the trajectories, not the verdicts alone.
"""
import os
import re

SB = ("/tmp/claude-1000/-mnt-rojaws-localDev/564fd1e1-49d3-4737-b912-7e0208433035"
      "/scratchpad")
ARMS = [
    ("neither",        "doclink-probe-neither.log",        0, 0),
    ("hint-only",      "doclink-probeB-hintonly.log",      0, 1),
    ("invariant-only", "doclink-probe-invariant-only.log", 1, 0),
    # Probe A's raw log was destroyed by an operator error (overwritten with the
    # unrelated natural run-1 log, no surviving copy). The `both` cell is therefore
    # RE-RUN here rather than cited from a remembered trajectory — a number recalled
    # from a conversation is not an artifact and must not enter a results table.
    ("both",           "doclink-probe-both.log",           1, 1),
]

def hint_at_seed(t):
    """Hints appended at the SEEDED round. run-build logs the count, never the text,
    so grepping for hint wording finds nothing. At that round the only diagnostics are
    AL0104/AL0107, so a non-zero count there can only be the inline-var hint."""
    m = re.search(r"known-fix: (\d+) hint", t)
    return int(m.group(1)) if m else 0


print(f"{'arm':<16}{'inv':<5}{'hint':<6}{'AL0104':<8}{'rewrites':<10}"
      f"{'hint fired':<12}{'trajectory':<34}{'result'}")
for name, fn, inv, hnt in ARMS:
    p = os.path.join(SB, fn)
    if not os.path.exists(p):
        print(f"{name:<16}{inv:<5}{hnt:<6}{'(not run yet)'}")
        continue
    t = open(p, encoding="utf-8", errors="replace").read()
    # ^ anchored: "error score: N" also occurs inside "* new best (error score: N)",
    # which double-counted every first entry in the archived first draft.
    scores = [int(x) for x in re.findall(r"^  error score: (\d+)", t, re.M)]
    traj = " -> ".join(str(s) for s in scores[:6]) + (" ..." if len(scores) > 6 else "")
    print(f"{name:<16}{inv:<5}{hnt:<6}"
          f"{len(re.findall(r'error AL0104', t)):<8}"
          f"{len(re.findall(r'fix-route: file-rewrite', t)):<10}"
          f"{hint_at_seed(t):<12}"
          f"{traj:<34}"
          f"{'PASS' if 'RESULT: PASS' in t else 'FAIL'}")

print("\nn=1 per cell. Descriptive separation only — no effect estimate.")
print("'hint fired' = hints appended at the seeded round. Only AL0104/AL0107 are present")
print("there, so a non-zero count can only be the inline-var hint.")
