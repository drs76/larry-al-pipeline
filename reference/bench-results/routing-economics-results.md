# RESULTS — routing economics

Registration: `exp-routing-economics-preregistration.md` + Amendments 1-6.
**Primary observed-arm analysis. Closed. Arm D omitted.**

## Claim

> Under the observed runs and stated loss sensitivity, fixed-round escalation B is preferred
> to never-escalate A for doclink when the operational cost of a failed build exceeds
> approximately $0.56 per failure; otherwise A is preferred. The rule-based policy C was not
> competitive on its observed compound outcome, with its weakness attributable in part to
> missed escalation triggers. These conclusions are fixture-specific, small-sample estimates
> and do not establish a general routing policy.

## Observed, per fixture x arm — no pooled aggregate

    fixture   arm  n   closure   mean $/run   source
    doclink    A   10    0.00     0.00000     routecon2
    doclink    B   10    0.80     0.44684     routecon2
    doclink    C   10    0.50     0.60788     routecon6
    p4         A   10    0.90     0.00000     routecon2
    p4         B   10    1.00     0.00000     routecon2
    p4         C   10    1.00     0.00000     routecon6
    map      A/B/C 10    1.00     0.00000     routecon2 / routecon6
    p1       A/B/C 10    1.00     0.00000     routecon2 / routecon6

## Regret, doclink — $ per run, lambda swept over the predeclared $0.50-$5.00

    lambda      L_A      L_B      L_C  |    R_A     R_B     R_C  | best
    0.50000  0.5000   0.5468   0.8579  | 0.0000  0.0468  0.3579  | A
    0.55855  0.5585   0.5585   0.8872  | 0.0000  0.0000  0.3286  | A = B
    1.00000  1.0000   0.6468   1.1079  | 0.3532  0.0000  0.4610  | B
    2.00000  2.0000   0.8468   1.6079  | 1.1532  0.0000  0.7610  | B
    3.00000  3.0000   1.0468   2.1079  | 1.9532  0.0000  1.0610  | B
    5.00000  5.0000   1.4468   3.1079  | 3.5532  0.0000  1.6610  | B

B dominates C at every lambda >= 0: `L_C - L_B = 0.3*lambda + 0.16104 > 0`.

p4: B/C optimal, `R_A = 0.1*lambda`. **Not evidence of escalation benefit** — neither B nor C
escalated on p4 at all, so this is zero-cost stochastic variation in the local build.
map, p1: all arms identical, regret zero at every lambda.

## Companion finding 1 — C decomposes into two mechanisms

    trigger recall   2/10 doclink builds were never escalated; both failed locally
    efficacy         5/8 closure among the builds it did treat

The compound 0.50 conflates them. **Changing the trigger and changing the escalation rung
address different failure mechanisms**, and 5/8 efficacy is not clearly worse than B's 8/10
while 2 missed triggers is a clean deficiency. Any action on the compound rule must say which
mechanism it targets.

## Companion finding 2 — a reusable engineering pattern

Across this sequence, multiple defects shared one structural shape: **validation checked that
the intended form was present, rather than proving the required behaviour occurred or that
malformed cases were rejected.**

    _OBJREF_RE               matched variable declarations, not `extends` targets
    event_verify._SUB_RE     matched only quoted event names; malformed ones vanished
    driver backend guard     satisfied by a previous run's stale log line
    usage strict mode        priced a zero-token synthesized result as free
    arm C assertions         passed policy LABELS while the treatment was suppressed

This finding is independent of the routing result and likely outlasts it.

## Fragility carried explicitly

- n=10 per cell against a measured noise floor: two identical 10-run blocks of the frozen
  corpus gave residual medians 7 and 3.
- doclink C ordering anomaly unresolved — treated sequence `FFFPPPPP`, no corroborating
  mechanism found (Amendment 5 §3).
- Matched-`r` pairing rejected; A/B/C are distributions, not interchangeable runs.

## Provenance asymmetry

    map A/B    fixture 422c749 (original frozen revision)
    map C      fixture 3240e31 (corrected — one line preserving .git during cleanup)

Every `routecon6` cell labels `3240e31` because provenance records repo HEAD, not per-path
commits. **p1, p4 and doclink content is byte-identical between the two revisions** — the
label moved, those fixtures did not.

## Arm C execution lineage

    rc2 C   VOID  treatment not delivered (wrong egress predicate)
    rc3 C   VOID  recursive child accounting ($0.9476 unassigned, held separately)
    rc4 C   VOID  map fixture cleanup destroyed the per-run git repository
    rc5 C   VOID  unexplained local-coder write timeout; undiagnosed
    rc6 C   VALID 40/40, 0 VOIDs, treatment delivered 8/8 where the rule fired

Arms A and B were executed once, in `routecon2`, and remained frozen throughout.

## Excluded from the result

    arm D                       omitted — counterfactual assumptions would transport
                                escalation outcomes across independent stochastic runs,
                                exactly the move the matched-r oracle was rejected for
    $0.9476 (rc3)               real spend from an invalid execution; unassigned, never
                                merged into any valid observation
    all voided C executions     preserved as artifacts, excluded from analysis
    pooled workload aggregate   weighting explicitly deferred; per-fixture only
