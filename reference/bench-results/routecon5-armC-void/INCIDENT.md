# INCIDENT — `routecon5` Arm C VOID at 0/40

**Status: VOID. 0/40 cells, $0.00 spend, 0 Claude calls. Artifacts preserved, excluded from
analysis. No cell reused.**

## What happened

VOID on the first run, `p1/armC/r1`:

    VOID: produced NO new metrics row — a run with no measurement is not a zero result
      Larry-write TIMEOUT after 1200s
      Wrote 0/6 expected files.  Retrying...
      Larry-write (attempt 2) ...        <- RUN_TIMEOUT=1800 killed the run here

The local coder's write phase never returned. `run-build` was killed before it could emit
metrics, and the driver's guard correctly refused to score a run with no measurement rather
than record a misleading zero.

The same p1 arm C cells completed in **65-74s** in `routecon4`.

## CAUSE: UNDIAGNOSED — an earlier attribution was WRONG

This incident was initially reported as infrastructure unavailability, on the basis that
`http://larry.home.arpa:11434` did not respond. **That attribution was incorrect.** 11434 is
the stock ollama port; this deployment serves on **11443**, which is what
`OLLAMA_WARM_URL` has always pointed at.

Independent health probe, taken after the VOID:

    host 192.168.0.173   up, 0.28ms; DNS and /etc/hosts pin correct; no VPN interface
    port 11434           closed        <- the port wrongly probed
    port 11443           OPEN          <- the port the pipeline uses
    /v1/models           200 in 21ms, 19 models, qwen3-coder:30b present
    /api/ps              qwen3-coder:30b RESIDENT, 21.7 GB VRAM
    live generation      200 in 0.24s, replied "OK"

**Larry was healthy, warm and fast.** The write phase hung against a working service.

Root cause remains **undiagnosed**. Candidates not yet distinguished:

- the known pi stream wedge — long agentic runs stalling with the stream never finishing,
  GPU idle and the process alive, which matches a resident model and a responsive service;
- a defect in the pi/client invocation or stream-completion path rather than the model;
- a transient that has since cleared.

Probe artifacts are held in the session scratchpad, deliberately outside `pipeline/` and
separate from benchmark artifacts.

## Lineage position

    1. routecon2 C   treatment not delivered (wrong egress predicate)
    2. routecon3 C   recursive child accounting ($0.9476 unassigned, preserved separately)
    3. routecon4 C   map fixture cleanup destroyed the per-run git repository
    4. routecon5 C   local coder write phase timed out against a healthy, warm Larry;
                     ROOT CAUSE UNDIAGNOSED
    5. next C run    only after the failure path is understood

Arms A and B from `routecon2` remain frozen and valid. This incident provides no evidence
about the routing policy or about Claude's repair capability: it is a failure that correctly
produced **no measurement** rather than a misleading zero.
