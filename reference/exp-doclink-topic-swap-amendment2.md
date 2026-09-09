# Amendment 2 — topic-swap suite re-runs as a fresh execution from 8eb6f67

Amends `exp-doclink-topic-swap-preregistration.md` and amendment 1. Written 2026-08-30,
before the re-run. No results are being reinterpreted: `topicab2` produced none.

## What happened to topicab2

Stopped after 3 runs, all control, all wedged — 1200s timeout, 0/9 files each. A harness
fault, not a model result: the coder never issued a request. `run_pi` let pi inherit
run-build's stdin, and as a background job that is a socket. pi registers fd 0 in its event
loop and waits for data, error or hangup; an inherited descriptor left open with none of the
three never fires. Fixed in `8eb6f67`.

The arms themselves were correct — every wedged log carries
`inject: 00-gotchas, 01-syntax-style, 02-objects (~9.3k tokens)`, exactly what the control
declares. Amendment 1 stands unchanged.

## Re-run as a fresh execution, not a continuation

New tag `topicab3`, from `8eb6f67`. The three `topicab2` rows are **discarded, not carried
forward**: they were produced by a different harness, and pooling a stalled session with a
working one would put an exclusion in the record that correlates with the arm rather than
with the model. n restarts at 0 and runs to 20 per arm.

Arms, stopping rule, primary metric and the wedge policy are all unchanged from amendment 1.

## Validation the fix carries

The configuration that wedged 3/3 completed 2/2 after `8eb6f67` — 82s and 139s, 9/9 files,
back inside the 90s median of 306 historical writes. Causality was shown in isolation first:
same binary and prompt, `stdin=/dev/null` completes in 2s, an open socketpair and an open
pipe both hang past 90s.

## Incident record

Two distinct stalls have shared the label "pi stream wedge" and must stay separated:

| | reaches ollama? | cause | status |
|---|---|---|---|
| A | no POST after prewarm | client inherits an open descriptor; pi waits on fd 0 | closed, `8eb6f67` |
| B | POST arrives, dies mid-generation | ollama 0.32.5 KV-shift regression | closed by pinning 0.31.1 |

> **Superseded 2026-08-31 (fault B row):** the 0.31.1 pin was retired after 0.33.2 passed a bounded
> upgrade-validation experiment. Larry now runs 0.33.2. See `exp-ollama-0332-upgrade-validation.md`.
> The discriminator above still holds; only the remedy changed.

Discriminator, to run before diagnosing either:

```bash
ssh larry "doas journalctl -u ollama --since '30 min ago' --no-pager | grep POST"
```

The earlier conflation is why fault A was carried for weeks as a context-overflow problem and
answered with "keep pi missions small" — advice that has no bearing on a stdin bug.
