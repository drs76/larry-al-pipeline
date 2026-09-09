# STATE OF EVIDENCE — local model, escalation, routing

Three claims, deliberately separated. They are at different evidential strengths and must not
be cited as one.

## Claim 1 — CAPABILITY: established

| | result | evidence |
|---|---|---|
| Claude writes doclink from scratch | 5/5, 4 clean on first compile | `tierb-part1-results.md` |
| Claude repairs Qwen's stalled trees | 8/8, median 1 round | `tierb-part2-results.md` |
| Qwen writes doclink | 0/82 tracked runs, 0 first-pass | frozen corpus + history |
| Qwen repairs those same 8 trees | 0/8, after 5 fix rounds each | the trees ARE its terminal output |

Within-state on Part 2: identical trees, Qwen 0/8, Claude 8/8.

**The fixture/handover explanation is substantially ruled out for this boundary.** Claude
succeeds from both the initial task and the stalled repair states, on the same fixture bytes
(`422c749`, handover `e82168cb3857`) the local model has never closed.

**The Kimi null is now interpretable.** Tier A was not evidence that escalation cannot work.
It was evidence that *that rung did not supply the missing ABS-contract knowledge* — Kimi and
Qwen lacked the same thing.

## Claim 2 — ROUTING EFFICACY: supported on the selected corpus, NOT as an online policy

8/8 closure was measured on a **precommitted corpus of eight states, hand-audited and
hash-pinned**, with one attempt each. That is efficacy under ideal selection: a human chose
which states to escalate, knowing their residual composition.

An online policy has none of that. It must decide *at round N, without knowing the outcome*,
whether this build is worth escalating. Nothing here measures that.

Specifically unmeasured: how often a live trigger fires on builds that would have recovered
locally; what it costs when it is wrong; whether the states a trigger selects resemble the
eight a human selected.

## Claim 3 — ROUTING ECONOMICS: measured on one fixture, closed 2026-08-25

*Superseded. This section read "entirely unmeasured" when written on 2026-08-23. The
measurement then happened. See `routing-economics-results.md`.*

Spend is now captured at the egress chokepoint — input, output and cache-read tokens plus
`total_cost_usd` for every Claude call (`claude-usage-schema.md`). Wall-clock is still not a
cost model, but it is no longer the only number the pipeline has.

On doclink, n=10 per arm:

| arm | policy | closure | mean $/run |
|---|---|---|---|
| A | never escalate | 0.00 | 0.00000 |
| B | escalate at a fixed round | 0.80 | 0.44684 |
| C | escalate when the frozen rule fires | 0.50 | 0.60788 |

**B is preferred to A when a failed build costs more than about $0.56.** Below that, A wins. C is
never optimal, and B dominates it at every lambda.

The scope is narrow and stated as such: one fixture, small samples, a measured noise floor of
residual medians 7 and 3 across two identical 10-run blocks. This does **not** make "escalation is
worth it" a general statement. `p1`, `p4` and `map` pass under every arm and discriminate nothing.

## The methodological result worth keeping

**Selecting the takeover corpus by minimum residual would have invalidated the test.** Four of
the five smallest residuals in the frozen corpus were parse-class or unresolved-symbol states,
masked by construction — an unparseable construct suppresses every downstream error in its
object, so a low score meant *less visible*, not *nearly finished*. A minimum-score corpus
would have measured whether Claude can transcribe syntax. The audited eight measured the
ABS-contract boundary that was actually in question.

Generalised: **a low error count is not evidence of proximity to done.** Neither is a
validator's silence evidence of correctness — three separate checks this session
(`_OBJREF_RE`, `event_verify._SUB_RE`, the driver's own backend guard) recognised only the
well-formed shape and were therefore blind, or reading stale evidence, in exactly the cases
that mattered.

## What follows

The open question is operational, not capability: **when should the system pay to invoke a
repair-capable cloud model, and under what trigger and cost constraints?**

The trigger is the intervention. Re-running generic model capability would answer nothing new.
See `exp-routing-economics-preregistration.md`.

**Where that went (2026-08-25).** The cost half is answered for doclink, above. The trigger half
is not. Arm C separated into a trigger that missed 2 of 10 builds and a treatment that closed 5
of the 8 it reached — two different defects. The frozen capability rule now runs in shadow mode
and records what it would have done, prospectively. The next decision is cost-weighted regret on
that log, not another capability run. Index: [`README.md`](README.md).
