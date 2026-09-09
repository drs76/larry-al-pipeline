"""Shadow-mode observation of the compound capability-boundary rule. LOGGING ONLY.

This NEVER changes a build. It does not touch ESCALATE_AFTER, backend selection, or the
egress gate. It records what a trigger WOULD have done so the next decision can be made on
cost-weighted regret rather than an arbitrary false-fire cap.

WHY IT IS OBSERVATIONAL, NOT A TRIGGER
--------------------------------------
The compound rule generalises far better than the retired cumulative-persistence proxy —
recall 0.73-0.98 on held-out data, and it removes ~63% of the false fires you would get by
always escalating. But on held-out doclink it fires on 34-40% of builds that end as NARROW
stalls, consistently across both within-doclink splits. That is not good enough to spend
escalation on automatically, and the economics that would justify accepting it have never
been measured: how often a build recovers locally AFTER the rule would have fired, how many
rounds that takes, and what an unnecessary escalation costs against those rounds.

Shadow mode collects exactly that, prospectively.

THE RULE IS FROZEN
------------------
Parameters below are split A from capability-compound.py: fitted on the p1/p4/map bench
pool and tested on doclink, i.e. fitted WITHOUT the workload it is judged on. They are
deliberately not tunable by environment variable. Re-tuning against the existing 121
traces while shadow data accumulates would destroy the one property that makes the new
data worth collecting — that it is genuinely prospective.

Change these only with a new pre-registration and a fresh evaluation.

PRE-REGISTERED METRICS FOR THE NEXT REVIEW
------------------------------------------
  fire_round            round the rule first fired (null = never)
  terminal_class        LOCAL_GREEN / NARROW_STALL / BROAD_BOUNDARY, from the final round
  recovered_after_fire  did the build reach green locally AFTER the candidate fire?
  rounds_after_fire     local rounds actually spent after the candidate fire
  rounds_saved          rounds that escalation would have pre-empted (n - fire_round)
  Cost weighting is applied at review time, not here — this file records observations,
  not judgements.

PRE-REGISTERED REVIEW PROTOCOL (fixed before any shadow data was collected)
--------------------------------------------------------------------------
Three SEPARATE questions. Do not collapse them into one accuracy number:

  1. SAFETY     among builds where the rule fired, how many still reached LOCAL_GREEN
                with no escalation? Those are the builds a live trigger would have
                spent tokens on for nothing.
  2. USEFULNESS how often does a fire correspond to BROAD_BOUNDARY, and how many local
                repair rounds actually remained after the fire point?
  3. ECONOMICS  for those remaining rounds, compare real local time and calls against
                the cost AND latency of an escalation. `rounds_saved` is the CEILING on
                savings, not the realised value: escalation is not free (the Claude
                capability probe ran ~290s against local rounds of ~100s), so a cost
                model needs both sides.

SEGMENT BEFORE AGGREGATING — by project/fixture, model/backend, run type (ordinary build
vs benchmark suite), terminal class, and fired vs not-fired. A large A/B suite will
otherwise dominate the sample and the pooled number will describe that suite, not the
workload.

THE GUARDRAIL: do NOT retune this rule on the accumulating shadow log and then cite that
same log as validation. This log is prospective validation data for rule v1. If it exposes
a weakness, the answer is a NEW versioned rule with a NEW validation window — the outcome
is keep, reject, or version, decided empirically.
"""
import json
import os
import time
from collections import Counter

# --- FROZEN RULE (capability-compound.py split A: fit bench -> test doclink) ---------
FILES_NOW_MIN = 2          # currently broad, not historically broad
RESOLVED_FRAC_MAX = 0.0    # repair is not clearing the current set
NET_CHANGE_MIN = -1        # unresolved set stable or growing
TOP2_SHARE_MAX = 0.90      # errors spread, not concentrated in one artifact

# Identity of the frozen rule, so an experiment can name exactly what it ran. The
# fingerprint covers the four parameters AND the source of _fires(), because a rule is its
# thresholds and its predicate together — changing either must change the identifier.
RULE_VERSION = "v1"


def rule_fingerprint():
    import hashlib
    import inspect
    body = inspect.getsource(Observer._fires)
    params = f"{FILES_NOW_MIN}|{RESOLVED_FRAC_MAX}|{NET_CHANGE_MIN}|{TOP2_SHARE_MAX}"
    return f"{RULE_VERSION}:" + hashlib.sha256((params + body).encode()).hexdigest()[:16]


LOG = os.environ.get("CAPABILITY_SHADOW_LOG",
                     os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                  ".capability-shadow.jsonl"))


class Observer:
    """Accumulates per-round failing-file sets and records the candidate fire round."""

    def __init__(self, project):
        self.project = project
        self.rounds = []           # list of {file: error_count}
        self.fire_round = None
        self.started = time.time()
        # True when the CALLER used fire_round to change the build (arm C of the routing
        # economics experiment). The prospective shadow log is validation data for a rule
        # that did NOT act; a row where it did is a different population and must never be
        # pooled with the observational ones.
        self.acted = False

    def observe(self, diags, round_idx):
        """One repair round's diagnostics. `diags` = iterable of (file, error_code)."""
        cur = Counter(f for f, c in diags if c != "PTE0004")
        self.rounds.append(cur)
        if self.fire_round is None and len(self.rounds) >= 2 and self._fires():
            self.fire_round = round_idx

    def _fires(self):
        cur, prev = self.rounds[-1], self.rounds[-2]
        cf, pf = set(cur), set(prev)
        if not cur:
            return False
        n_err = sum(cur.values())
        resolved_frac = len(pf - cf) / len(pf) if pf else 0.0
        top2 = sum(n for _, n in cur.most_common(2)) / n_err if n_err else 0.0
        return (len(cf) >= FILES_NOW_MIN
                and resolved_frac <= RESOLVED_FRAC_MAX
                and (len(cf) - len(pf)) >= NET_CHANGE_MIN
                and top2 <= TOP2_SHARE_MAX)

    def finish(self, passed, used_fallback):
        """Write one observation record. Never raises into the build."""
        try:
            if not self.rounds:
                return
            if passed and not used_fallback:
                terminal = "LOCAL_GREEN"
            else:
                terminal = ("BROAD_BOUNDARY"
                            if len(self.rounds[-1]) >= 3 else "NARROW_STALL")
            n = len(self.rounds)
            fr = self.fire_round
            rec = {
                "ts": int(self.started),
                "project": os.path.basename(self.project or ""),
                "rounds": n,
                "fire_round": fr,
                "terminal_class": terminal,
                "passed": bool(passed),
                "used_fallback": bool(used_fallback),
                # The economics the next review needs:
                "recovered_after_fire": bool(fr and passed and not used_fallback),
                "rounds_after_fire": (n - fr) if fr else None,
                "rounds_saved": (n - fr) if (fr and terminal == "BROAD_BOUNDARY") else 0,
                "would_be_false_fire": bool(fr and terminal != "BROAD_BOUNDARY"),
                "terminal_files": len(self.rounds[-1]),
                "acted": bool(self.acted),
                "rule_version": RULE_VERSION,
                "rule_fingerprint": rule_fingerprint(),
                "rule": {"files_now_min": FILES_NOW_MIN,
                         "resolved_frac_max": RESOLVED_FRAC_MAX,
                         "net_change_min": NET_CHANGE_MIN,
                         "top2_share_max": TOP2_SHARE_MAX},
            }
            with open(LOG, "a", encoding="utf-8") as fh:
                fh.write(json.dumps(rec) + "\n")
        except Exception:
            pass          # shadow logging must never affect a build
