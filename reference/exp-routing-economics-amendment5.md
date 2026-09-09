# AMENDMENT 5 — analysis specification: pairing rejected, oracle redefined, D reclassified

Amends `exp-routing-economics-preregistration.md`. **Analysis specification only. No
execution, no re-run, no change to observed data.** Written BEFORE any regret number is
computed.

## 1. Matched-`r` pairing is REJECTED

`r` is an allocation index, not a shared experimental unit. Verified: the coder invocation
pins **no seed and no temperature**, and repeats within a single arm diverge freely (p4 arm A
fails at r3; p4 arm C fails first-pass at r9). Arms A/B executed in `routecon2`, arm C in
`routecon6`, separately.

Therefore an oracle of the form

    max(A_r, B_r, C_r)      or      min-loss across those three realized runs

is **not a valid estimator** and must not be computed. On this data it happens to equal arm
B's 8/10 — irrelevant. Taking the max over independent draws selects on noise and is biased
upward in expectation; that it is unbiased here is luck, not a property.

## 2. Observed results are FROZEN as a chronological execution record

Valid descriptively, subject to the Amendment 3 provenance asymmetry. **The 10 runs per cell
are NOT to be silently reinterpreted as i.i.d. replicates** — see §3.

## 3. doclink arm C ordering — ANALYSIS INCIDENT, unresolved

Raw pattern:

    doclink C  0 0 0 0 0 1 1 1 1 1
    doclink B  0 1 1 0 1 1 1 1 1 1

**The anomaly weakens materially once treatment status is separated.** Two of the ten C runs
(r2, r3) **never fired the rule at all** — untreated, and therefore not escalation failures.
Among the 8 treated runs the chronological sequence is `FFFPPPPP`.

    P(specified contiguous block | 5 of 8 pass) = 1/C(8,5) = 0.018

Recorded as a **post-hoc diagnostic anomaly, NOT a calibrated hypothesis test.** The earlier
figure of 0.004 was computed over all ten runs before separating the untreated ones and is
superseded.

**Mechanism search — no corroboration found.** Time-ordered observables that exist
independently of the outcome:

    fire round vs outcome   fails r1@4, r4@1, r5@4 | passes r6@1 r7@3 r8@2 r9@1 r10@2
                            two of three failures are late fires, but r4 fired at round 1
                            with 4 calls and still failed, and passes include round-1 fires.
                            Does not separate the groups.
    claude calls            fails 1,4,1 | passes 1,1,2,2,1 — no separation
    cache_read tokens       101k, 476k, 76k | 607k, 349k, 392k, 402k, 199k — non-monotonic,
                            no warming signature
    api_ms, cost, duration  no trend aligning with the split
    timestamps              22:22 22:33 22:39 22:45 22:52 22:57 23:03 23:11 23:15 23:19 —
                            regular ~6 min spacing, NO gap indicating a restart or state
                            transition
    other routecon6 C cells p4 10/10, map 10/10 — no failures, so no ordering to corroborate

**Conclusion: an unexplained ordering anomaly with no corroborating mechanism.** Any
policy-distribution estimate for doclink C is therefore **fragile**, and that fragility must
be stated wherever the estimate is used.

## 4. Oracle redefined at the POLICY level

For each fixture, the oracle chooses the policy with the lowest expected pre-registered loss
under that fixture's execution distribution. A, B and C are **distributions, not matched
outcomes**:

    L_f(pi) = E[ failure penalty + billed cost | fixture f, policy pi ]
    L_f*    = min over pi in {A,B,C} of L_f(pi)
    R_f(pi) = L_f(pi) - L_f*

The finite samples ESTIMATE these expectations. They are not a perfect-foresight menu of
interchangeable runs.

## 5. Arm D is a DERIVED COUNTERFACTUAL MODEL, not an observed arm

Arm A identifies which cells failed locally. It cannot say, for any realized failure, whether
escalation would have succeeded or at what cost. D therefore requires escalation-success and
escalation-cost components estimated from observed escalation data, with uncertainty
propagated.

**D must be labelled a post-execution analytical model.** Its inputs are drawn from B/C after
these results were inspected, so it must not be presented as the originally observed primary
comparator.

## 6. Still outstanding before any regret number

    - the loss function is NOT yet fixed: the failure penalty relative to billed cost
      remains unspecified
    - the doclink C ordering anomaly is unresolved
    - a descriptive finding to carry forward: arm C left 2/10 doclink builds unescalated and
      both failed locally — a trigger-recall miss directly relevant to the routing question,
      distinct from escalation efficacy on the 8 it did treat
