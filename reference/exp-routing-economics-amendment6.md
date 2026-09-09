# AMENDMENT 6 — loss function, sensitivity range, and the mechanical regret result

Amends `exp-routing-economics-preregistration.md`, following Amendment 5. **Analysis
specification and its mechanical consequence. No execution, no change to observed data.**

## Loss

    L_f(pi) = lambda * (1 - p_hat[f,pi]) + c_bar[f,pi]

`p_hat` = observed closure rate for that fixture/policy. `c_bar` = **mean billed cost per
run**, not total arm spend, so policies compare on a common per-build basis.

`lambda` = the cost-equivalent penalty for one failed build.

## Sensitivity — predeclared range, NOT a post-hoc point value

    lambda in [$0.50, $5.00]

Reported across the range rather than at a single selected value. This is deliberate: the
doclink A-vs-B decision turns entirely on lambda, and choosing one value after seeing the
crossover would be selecting the conclusion. Grid used: 0.50, 0.55855, 1.00, 2.00, 3.00, 5.00.

## Oracle and regret — policy level only

    L_f* = min over pi in {A,B,C} of L_f(pi)
    R_f(pi) = L_f(pi) - L_f*

No matched-`r` pairing (Amendment 5). A, B and C are distributions, not interchangeable runs.

## Observed inputs

    fixture   arm  n   closure   mean $/run
    doclink    A   10    0.00     0.00000
    doclink    B   10    0.80     0.44684
    doclink    C   10    0.50     0.60788
    p4         A   10    0.90     0.00000
    p4        B/C  10    1.00     0.00000
    map      A/B/C 10    1.00     0.00000
    p1       A/B/C 10    1.00     0.00000

## Result — regret per run, $

    doclink
      lambda      L_A      L_B      L_C  |    R_A     R_B     R_C  | best
      0.50000  0.5000   0.5468   0.8579  | 0.0000  0.0468  0.3579  | A
      0.55855  0.5585   0.5585   0.8872  | 0.0000  0.0000  0.3286  | A=B (crossover)
      1.00000  1.0000   0.6468   1.1079  | 0.3532  0.0000  0.4610  | B
      2.00000  2.0000   0.8468   1.6079  | 1.1532  0.0000  0.7610  | B
      3.00000  3.0000   1.0468   2.1079  | 1.9532  0.0000  1.0610  | B
      5.00000  5.0000   1.4468   3.1079  | 3.5532  0.0000  1.6610  | B

    p4     B/C optimal at every lambda; R_A = 0.1*lambda ($0.05 to $0.50)
    map    all three identical; regret 0 everywhere
    p1     all three identical; regret 0 everywhere

## Headline crossover

**doclink A beats B below lambda = $0.55855; B beats A above it. B dominates C for every
lambda >= 0**, since C is worse on both ingredients:

    L_C - L_B = 0.3*lambda + 0.16104 > 0   for all lambda >= 0

The failure penalty therefore does not determine the B-vs-C ordering. It determines only
whether escalating at all is worth its cost on doclink.

## Scope of that claim — explicit correction

It is **wrong** to say the experiment reduces to whether a failed doclink build is worth more
than $0.56. That statement holds only for the **observed doclink A-vs-B point-estimate
decision**. It is not the experiment's conclusion, because:

- the estimates rest on n=10 per cell with a measured noise floor (two identical 10-run blocks
  of the frozen corpus gave residual medians 7 and 3);
- doclink C carries an unresolved non-exchangeability concern (Amendment 5 §3);
- **C's trigger behaviour and its escalation efficacy are distinct mechanisms** and are not
  separable from a single closure rate — see below.

## doclink C — fragility carried explicitly

    small n              10 runs, 8 treated
    chronology           treated sequence FFFPPPPP; no corroborating mechanism found
    trigger-recall miss  2/10 builds were never escalated and both failed locally

The last item matters for interpretation: C's 0.50 closure combines **a trigger that declined
to fire on two builds that then failed** with **escalation efficacy of 5/8 on the builds it
did treat**. A single closure rate conflates the two. Any conclusion about the compound rule
must say which mechanism it concerns.

## p4, map, p1

**p4 is NOT evidence of escalation benefit.** Neither B nor C escalated on p4 at all — zero
Claude calls, zero cost. A's 9/10 versus B/C's 10/10 is zero-cost stochastic variation in the
local build, and R_A = 0.1*lambda is an artefact of that variation, not a routing effect.

**map and p1 show no observed routing signal.** All three arms identical, regret zero at every
lambda.

## Arm D

Remains a **separate, explicitly post-execution, model-based counterfactual analysis**
(Amendment 5 §5). Not part of the observed-arm primary comparison and not reported alongside
these numbers as though observed.
