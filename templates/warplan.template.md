# Warplan — [MISSION NAME]

> A warplan is NOT a plan. A plan assumes linearity and blue-sky success; a warplan
> pre-simulates what happens when reality pushes back — **action → reaction → counteraction** —
> so a cheaper executor (Larry via `alw`/`gow`/`csw`, or any model) can run the hard "last 20%"
> confidently. Fill every section. Keep moves concrete and cited to files/objects.

## Mission brief
_What we're building and why, in a short paragraph. The known-knowns._

## Executor + referee
- **Executor:** [Larry `al-coder-qwen36` via `alw build` | `qwen3-coder:30b` via `gow`/`csw` | Claude]
- **Referee (ground truth):** [`al compile` + manifest | `go build`+vet+test | `dotnet build`+format+test]
- **Tailored for:** [the executor's known behaviour/limits — e.g. Larry regresses on whole-file rewrites]

## Moves (action → reaction → counteraction)
For each step, one block. Order top-to-bottom the way the executor works.

### Move N — [short title]
- **Action:** the concrete change (file/object/function).
- **Expected observation (success):** exactly what you see if it worked.
- **Expected observation (failure):** what you see if it didn't.
- **Most-likely failure + cause:** the pessimistic scenario and why.
- **Counter-move:** how to recover without abandoning the mission.
- **Fork:** if you observe [X] → take route [A]; else → route [B].

## Second/third-order consequences
_Things that surface a few layers down, not at the initial action (e.g. "the endpoint builds,
but the permission set doesn't expose it, so the page 401s at runtime")._

## Assumptions the recon could NOT resolve → ledger
_Every unknown the warplan had to assume. Each becomes a `(variable)` placeholder needing the
operator's input — do not silently guess in the real build._
- `(variable: …)` — what it is, why it's blocked, a safe default if forced.

## Abort conditions
_When the executor must STOP and escalate rather than keep grinding._
- Hard blocker: [e.g. no access to a required system / symbol / credential].
- Repeated same-error regressions after N rounds → escalate to Claude (egress policy permitting).
- Referee score worsens instead of improving across 2 rounds.

## Success criteria (→ success.md)
_Testable outcomes that define "warplan executed successfully" — feeds the referee/definition of done._
