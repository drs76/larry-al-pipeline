#!/usr/bin/env bash
# routing-economics.sh — the registered routing-economics experiment.
#
#   reference/exp-routing-economics-preregistration.md   (frozen)
#   120 runs = 4 fixtures x 3 arms x 10.  The TRIGGER is the intervention.
#
#     A  never        escalation explicitly OFF
#     B  fixed-round  ESCALATE_AFTER=4, set literally
#     C  compound     ESCALATE_ON_RULE=1, frozen rule v1
#
# No spend cap: the fixed allocation is the only exposure bound. Every hard stop below is a
# MEASUREMENT-INTEGRITY guard — none is budgetary. A guard that prevents an invalid
# measurement is legitimate; one that selectively stops expensive valid measurements would
# change the experiment.
#
#   EGRESS_POLICY=enterprise-anon ./routing-economics.sh
set -uo pipefail

BENCH="$(cd "$(dirname "$0")" && pwd)"
RUNBUILD="${RUNBUILD:-$BENCH/run-build.py}"
PREFLIGHT="${PREFLIGHT:-$BENCH/tierb_preflight.py}"
PROJECTS_DIR="${PROJECTS_DIR_OVERRIDE:-/mnt/rojaws/localDev/projects}"
TAG="${TAG:-routecon}"
N="${N:-10}"
FIXTURES=(${FIXTURES:-p1 p4 map doclink})
ARMS=(${ARMS:-A B C})
MODEL="${MODEL:-ollama/qwen3-coder:30b}"
ESC_AFTER_B="${ESC_AFTER_B:-4}"
MODEL_SLUG="${MODEL#*/}"; MODEL_SLUG="${MODEL_SLUG//:/_}"

fixture_of() {
  case "$1" in
    p1)      echo "$PROJECTS_DIR/bench-p1-crud" ;;
    p4)      echo "$PROJECTS_DIR/bench-p4-unseen" ;;
    map)     echo "$PROJECTS_DIR/tsg-map-integration" ;;
    doclink) echo "$PROJECTS_DIR/tsg-document-link-2-az-storage" ;;
    *)       echo "" ;;
  esac
}

[ "${EGRESS_POLICY:-}" = "enterprise-anon" ] || {
  echo "FATAL: authorised for EGRESS_POLICY=enterprise-anon only (got '${EGRESS_POLICY:-unset}')." >&2
  exit 2; }

# Rule identity is asserted, not assumed: arm C must run the rule the registration names.
EXPECT_FP="${EXPECT_FP:-$(python3 -c "
import importlib.util,sys,os;sys.path.insert(0,'$BENCH')
s=importlib.util.spec_from_file_location('cs','$BENCH/capability_shadow.py')
m=importlib.util.module_from_spec(s);s.loader.exec_module(m);print(m.rule_fingerprint())")}"
[ -n "$EXPECT_FP" ] || { echo "FATAL: could not read the rule fingerprint" >&2; exit 2; }

SANITIZE=($(python3 "$BENCH/bench_env_contract.py" --names)) || exit 2
CLEAR=(); for v in "${SANITIZE[@]}"; do CLEAR+=(-u "$v"); done

mkdir -p "$BENCH/runs" "$BENCH/logs"
SUMMARY="$BENCH/${TAG^^}-SUMMARY.log"
CELLS="$BENCH/${TAG^^}-CELLS.jsonl"
METRICS="${BUILD_METRICS:-$BENCH/.build-metrics.jsonl}"

# EXCLUSIVE LOCK, held for the suite's lifetime. The cells check below inspects the file once
# at startup; it cannot stop a SECOND invocation launched while the first is still running,
# nor a killed wrapper whose child keeps appending. Two runs interleaving into one cells file
# produce an allocation that never existed — observed during fake validation, where a stray
# concurrent invocation left 100 cells with p4 at A=8/B=0/C=2, a distribution no sequential
# run can produce.
LOCK="$BENCH/.${TAG}.lock"
if ! mkdir "$LOCK" 2>/dev/null; then
  echo "REFUSING: $LOCK exists — another invocation of tag '$TAG' holds the lock" >&2
  [ -f "$LOCK/pid" ] && echo "  holder pid: $(cat "$LOCK/pid")" >&2
  echo "  If that process is gone, remove $LOCK deliberately after inspecting $CELLS." >&2
  exit 5
fi
echo $$ > "$LOCK/pid"
trap 'rm -rf "$LOCK"' EXIT INT TERM

# An interrupted suite must leave its completed cells identifiable, and must never be
# silently continued or rebalanced. Refusing is the whole point: a partial suite that quietly
# resumes produces cells run under different conditions and calls them one allocation.
if [ -s "$CELLS" ]; then
  echo "REFUSING: $CELLS already records completed runs for tag '$TAG'." >&2
  echo "Completed cells:" >&2
  python3 - "$CELLS" <<'PY' >&2
import json,sys,collections
c=collections.Counter()
for l in open(sys.argv[1]):
    try: r=json.loads(l)
    except ValueError: continue
    c[(r.get("fixture"),r.get("arm"))]+=1
for (f,a),n in sorted(c.items()): print(f"  {f:8} arm {a}: {n} run(s)")
print("\nUse a NEW TAG. Backfilling or rebalancing this allocation needs a new registration.")
PY
  exit 4
fi
: > "$SUMMARY"; : > "$CELLS"

_live_validated=0     # first real Claude call doubles as live instrumentation validation

{
  echo "ROUTING ECONOMICS — $TAG"
  echo "registration: reference/exp-routing-economics-preregistration.md"
  echo "allocation: ${#FIXTURES[@]} fixtures x ${#ARMS[@]} arms x $N = $(( ${#FIXTURES[@]} * ${#ARMS[@]} * N )) runs"
  echo "fixtures: ${FIXTURES[*]}   arms: ${ARMS[*]}   model: $MODEL (fixed across arms)"
  echo "arm A: escalation OFF   arm B: ESCALATE_AFTER=$ESC_AFTER_B   arm C: ESCALATE_ON_RULE=1 $EXPECT_FP"
  echo "sanitized ${#SANITIZE[@]} env vars per run; every arm sets its policy EXPLICITLY"
  echo "CLAUDE_USAGE_STRICT=1; no spend cap — the 120-run allocation is the only exposure bound"
  echo "per-fixture analysis only; no pooled workload metric (weighting deferred)"
  echo
} | tee -a "$SUMMARY"

void() {   # reason
  echo "VOID: $1" | tee -a "$SUMMARY"
  echo "suite stopped — a measurement-integrity guard fired, not a budget one" | tee -a "$SUMMARY"
  exit 3
}

t_all=$(date +%s)
for fx in "${FIXTURES[@]}"; do
  src="$(fixture_of "$fx")"
  [ -d "$src" ] || void "no fixture directory for '$fx'"
  for arm in "${ARMS[@]}"; do
    for r in $(seq 1 "$N"); do
      # run-build's check_model_matches_rundir() guards the bench naming convention
      # '<model>__<project>__<workflow>__<run>': any dir containing '__' must have the
      # coder's model slug as its LEADING segment, or the run aborts before emitting
      # metrics. The guard exists to stop mislabelled rows, so conform to it rather than
      # setting ALLOW_MODEL_MISMATCH — that flag accepts exactly the mislabelling this
      # experiment cannot afford.
      name="${MODEL_SLUG}__${fx}__${TAG}_arm${arm}__r${r}"
      dst="$BENCH/runs/$name"
      log="$BENCH/logs/${name}.log"
      : > "$log"          # never let a previous run's banner satisfy this run's assertions

      rm -rf "$dst"; mkdir -p "$dst"
      cp "$src/app.json" "$dst/" 2>/dev/null
      [ -f "$src/cleanup.sh" ] && cp "$src/cleanup.sh" "$dst/"
      [ -d "$src/docs" ] && cp -r "$src/docs" "$dst/"
      [ -d "$src/.alpackages" ] && cp -r "$src/.alpackages" "$dst/"
      sed "s|${src}|${dst}|g" "$src/larry-handover.prompt.md" > "$dst/larry-handover.prompt.md"
      git -C "$dst" init -q
      printf '.alpackages/\n.anon/\n*.app\n' > "$dst/.gitignore"
      git -C "$dst" add -A
      git -C "$dst" -c user.email=pipeline@local -c user.name=pipeline \
          commit -q -m "seeded inputs ($TAG $fx arm$arm r$r)" || true

      # Per-arm policy, set EXPLICITLY on top of the cleared environment. Arm A is off
      # because it was turned off, never because nothing happened to set it.
      arm_env=()
      case "$arm" in
        A) : ;;
        B) arm_env=(ESCALATE_AFTER="$ESC_AFTER_B") ;;
        C) arm_env=(ESCALATE_ON_RULE=1) ;;
        *) void "unknown arm '$arm'" ;;
      esac

      # Arms that can reach Claude must prove their workspace mirrors first. Arm A cannot
      # escalate, so it has no Claude path to gate and is left byte-identical to a plain
      # local build rather than being mutated by a mirror probe.
      if [ "$arm" != "A" ]; then
        if ! env "${CLEAR[@]}" EGRESS_POLICY=enterprise-anon CODER_BACKEND=claude \
              ANON_AUTOCOMMIT=1 python3 "$PREFLIGHT" "$dst" >> "$log" 2>&1; then
          void "$name preflight failed — no Claude call made. See $log"
        fi
      fi

      before=$(wc -l < "$METRICS" 2>/dev/null || echo 0)
      t0=$(date +%s)
      env "${CLEAR[@]}" \
        PI_CODER_MODEL="$MODEL" CODER_BACKEND=pi \
        EGRESS_POLICY=enterprise-anon ANON_AUTOCOMMIT=1 CLAUDE_USAGE_STRICT=1 \
        MAX_FIX_ROUNDS="${MAX_FIX_ROUNDS:-5}" FIXTURE_DIR="$src" \
        BENCH_META="{\"suite_tag\":\"$TAG\",\"fixture\":\"$fx\",\"arm\":\"$arm\",\"repeat\":$r,\"expected_rule_fp\":\"$EXPECT_FP\"}" \
        "${arm_env[@]}" \
        timeout "${RUN_TIMEOUT:-1800}" python3 "$RUNBUILD" --project "$dst" >> "$log" 2>&1
      rc=$?
      dt=$(( $(date +%s) - t0 ))

      # ONE python invocation for row extraction, every integrity assertion, and the cell
      # record. It was six; on NFS each interpreter start cost seconds, i.e. ~40 min of pure
      # harness overhead across 120 runs. Consolidating also means every assertion sees
      # exactly one snapshot of the row instead of re-parsing it five times.
      #
      # The row must be NEW: matching by name alone would let a stale row from an earlier
      # suite satisfy every assertion below.
      out=$(python3 - "$METRICS" "$before" "$name" "$arm" "$EXPECT_FP" "$_live_validated" \
                     "$fx" "$r" "$dt" "$CELLS" <<'PYCHK'
import json, sys
metrics, before, proj, arm, fp, validated, fx, rep, dt, cells = sys.argv[1:11]
before, validated = int(before), validated == "1"
try:
    lines = open(metrics).read().splitlines()
except OSError:
    lines = []
# Every metrics row created during this cell must BELONG to this cell. routecon3's arm C
# had a nested run-build emit a second row as project "." — ignored by the old matcher, so
# its 3 Claude calls and $0.9476 were spent outside any cell's accounting. Ignoring a
# foreign row silently understates the arm's cost; rejecting it stops the suite.
row, foreign = None, []
for l in lines[before:]:
    try: r = json.loads(l)
    except ValueError: continue
    if r.get("project") == proj and row is None:
        row = r
    else:
        foreign.append(r.get("project"))
if foreign:
    print("VOID|this cell produced metrics row(s) belonging to no cell: "
          + ", ".join(repr(f) for f in foreign[:3])
          + " — spend outside the cell accounting, not an ignorable extra")
    raise SystemExit(0)
if row is None:
    print("VOID|produced NO new metrics row - a run with no measurement is not a zero result")
    raise SystemExit(0)

p = []
want = {"A": "never", "B": "fixed-round", "C": "rule"}[arm]
if row.get("routing_policy") != want:
    p.append(f"routing_policy={row.get('routing_policy')} want {want}")
if arm == "B" and row.get("escalate_after") != 4:
    p.append(f"escalate_after={row.get('escalate_after')} want 4")
if arm in ("A", "C") and row.get("escalate_after") is not None:
    p.append(f"escalate_after leaked: {row.get('escalate_after')}")
if arm == "C" and row.get("rule_fingerprint") != fp:
    p.append(f"rule_fingerprint={row.get('rule_fingerprint')} want {fp}")
if arm != "C" and row.get("rule_fingerprint"):
    p.append("rule_fingerprint set on a non-rule arm")
calls = row.get("claude_calls") or 0
if arm == "A" and calls:
    p.append(f"arm A made {calls} Claude call(s)")

# BEHAVIOURAL invariant, not a label check. routecon2's arm C reported
# routing_policy=rule on all 40 rows while never escalating once: the rule fired in 9/10
# doclink runs and a wrong egress predicate suppressed every call, so the registered
# treatment was never delivered and every label-based assertion still passed. The guard
# therefore lives in production, not only in the validation suite.
if arm == "C":
    fired = row.get("rule_fired")
    if fired and calls == 0:
        p.append("arm C rule FIRED but produced 0 Claude calls — the registered treatment "
                 "was not delivered; this is a suppressed intervention, not a null result")
    if fired is False and calls:
        p.append(f"arm C rule did NOT fire yet {calls} Claude call(s) were made")
    if fired is None:
        p.append("arm C row carries no rule_fired field — treatment delivery is unverifiable")
if row.get("claude_calls_missing_usage"):
    p.append(f"{row['claude_calls_missing_usage']} unpriced call(s) - row is not economics-valid")
if calls and not validated:
    tok = (row.get("claude_input_tokens") or 0) + (row.get("claude_output_tokens") or 0)
    if tok <= 0:
        p.append("FIRST live Claude call yielded zero tokens - instrumentation unvalidated")
if p:
    print("VOID|" + "; ".join(p)); raise SystemExit(0)

with open(cells, "a") as fh:
    fh.write(json.dumps({"fixture": fx, "arm": arm, "repeat": int(rep), "run": proj,
                         "passed": bool(row.get("final_compile")), "calls": calls,
                         "cost_usd": row.get("claude_cost_usd") or 0.0,
                         "seconds": int(dt)}) + "\n")
print(f"OK|{'PASS' if row.get('final_compile') else 'FAIL'}|{calls}|{row.get('claude_cost_usd') or 0}")
PYCHK
)
      case "$out" in
        VOID*) void "$name integrity failure - ${out#VOID|}" ;;
      esac
      IFS='|' read -r _ passed calls cost <<< "$out"
      [ "${calls:-0}" -gt 0 ] && _live_validated=1
      echo "$name: $passed calls=$calls cost=\$$cost in ${dt}s" | tee -a "$SUMMARY"

      # Telemetry AFTER the row is validated. Nothing below can affect continuation.
      python3 "$BENCH/bench_ledger.py" "$TAG" | tee -a "$SUMMARY"
      rm -rf "$dst/.alpackages"
    done
  done
done

echo | tee -a "$SUMMARY"
echo "=== ${TAG^^} — per fixture x arm (no pooled metric: weighting deferred) ===" | tee -a "$SUMMARY"
python3 - "$CELLS" <<'PY' | tee -a "$SUMMARY"
import json,sys,collections
rows=[json.loads(l) for l in open(sys.argv[1]) if l.strip()]
agg=collections.defaultdict(lambda: {"n":0,"pass":0,"calls":0,"cost":0.0,"s":0})
for r in rows:
    a=agg[(r["fixture"],r["arm"])]
    a["n"]+=1; a["pass"]+=r["passed"]; a["calls"]+=r["calls"]; a["cost"]+=r["cost_usd"]; a["s"]+=r["seconds"]
print(f"  {'fixture':8} {'arm':>3} {'n':>3} {'pass':>5} {'calls':>6} {'cost$':>9} {'mean s':>7}")
for (f,arm),a in sorted(agg.items()):
    print(f"  {f:8} {arm:>3} {a['n']:>3} {a['pass']:>5} {a['calls']:>6} {a['cost']:>9.4f} {a['s']//max(a['n'],1):>7}")
PY
echo "  total $(( ($(date +%s) - t_all) / 60 )) min" | tee -a "$SUMMARY"
