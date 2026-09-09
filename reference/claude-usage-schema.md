# FROZEN — Claude usage capture schema

Frozen 2026-08-23, before any routing-economics run is allocated. Changing any field name or
meaning below requires a new pre-registration: an economics result is only comparable across
runs if the thing being summed stayed the same.

## Source of truth

`claude -p --output-format json` emits a single result object. The shape is not inferred from
a sample or from documentation — it is the object the **shipped CLI itself constructs**:

    {type, subtype, duration_ms, duration_api_ms, is_error, num_turns, result,
     stop_reason, total_cost_usd, usage{...}, modelUsage{}, permission_denials[],
     session_id, uuid}

`usage` carries `input_tokens`, `output_tokens`, `cache_read_input_tokens`.

## Capture point

`claude_egress._raw()` — the single chokepoint every pipeline Claude invocation passes
through, under every policy (`personal`, `enterprise-anon`). Capturing anywhere else would
miss a path.

`_raw` returns `result` as its text, so the contract with every caller
(`run-build.py`, `run-build-go.py`, `run-build-cs.py`) is unchanged.

## Per-call record — `claude_egress.usage_records()`

    label                  which call (Larry-write, Claude-fix, …)
    attributed             bool — false means the call could NOT be priced
    wall_s                 wall clock measured by the pipeline
    total_cost_usd         from the CLI
    num_turns              from the CLI
    duration_api_ms        API time as the CLI reports it
    duration_ms            CLI-side total
    session_id, subtype, is_error
    usage                  {input_tokens, output_tokens, cache_read_input_tokens}
    model_usage            per-model breakdown as reported
    reason, raw_chars      only when attributed=false

## Per-build totals — `claude_egress.usage_totals()`, emitted into the metrics row

    claude_calls
    claude_input_tokens
    claude_output_tokens
    claude_cache_read_tokens
    claude_cost_usd            rounded to 6dp
    claude_api_ms
    claude_turns
    claude_calls_missing_usage

**`claude_calls_missing_usage > 0` means the spend figure is INCOMPLETE.** It must never be
reported as a cost, and an economics arm containing such a row is void.

## Strict mode — mandatory for economics runs

`CLAUDE_USAGE_STRICT=1` raises `UsageUnattributable` on any call that cannot be priced.

Default is warn-and-record, deliberately: instrumentation must not break an ordinary build,
and the existing pipeline principle is that metrics failures are fail-open. An economics run
inverts that trade — a silently unpriced call is worse than a stopped run.

A timeout is recorded as unattributable rather than dropped. The call may well have been
billed, and a dropped record would understate spend while looking complete.

## Degradation behaviour

If stdout is not a JSON result object — an older CLI, a schema change, a crash — `_raw` falls
back to returning the raw text exactly as before. **The accounting degrades; the build does
not.** In strict mode that same condition is a hard failure.

## Validated

Controlled fake-CLI calls, no billed calls, covering: a well-formed result object; plain-text
output; a JSON object of the wrong `type`; empty stdout; accumulation across two calls; and
strict mode raising on each unattributable path. See `test_al_intelligence.py`.

**Zero tokens is unpriceable, not free.** The CLI synthesizes
`{type:"result", subtype:"success", total_cost_usd:0, num_turns:0, usage:{zeros}}` on some
paths. A well-formed result object is therefore not proof of a priced call, and an earlier
version of `_record` accepted it as attributed and scored $0. Such a record is now marked
unattributed and hard-fails under strict mode.

**Live capture remains unverified.** The schema comes from the shipped binary and has been
exercised only against a fake CLI. It is validated in the first real invocation of the first
allocated economics arm, under `CLAUDE_USAGE_STRICT=1`, requiring `attributed=true`,
non-zero tokens and `claude_calls_missing_usage == 0` — any failure hard-aborts and voids the
arm. See `exp-routing-economics-preregistration.md`.
