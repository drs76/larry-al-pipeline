#!/usr/bin/env python3
"""Capability ceiling probe: can a stronger model write the three doclink blob codeunits?

WHY THIS EXISTS
---------------
Four harness interventions have now come back null on the doclink fixture — eight
compiler-verified handover defects (p=1.0, n=40), AL_BRAIN, AL_APIS (0/20), and
WORKFLOW=incremental (p=1.0, n=10). Across incrab2's ten challenger runs the ratchet
localised the failure precisely: three blob codeunits, 60 REVERT events, zero greens,
while every other object placed reliably.

The error profile on those reverts is broad rather than concentrated — ~34% base-app API
misuse (ABS Blob Client signatures), ~17% invented fields on the project's own objects,
~10% raw syntax, ~9% ordering. No single prompt lever addresses a majority, and the one
that targets the largest class (AL_APIS) was built for exactly this diagnosis and scored
0/20.

That makes model capability the variable never yet varied. This probe holds everything
else fixed — same handover, same verified-green baseline, same compiler+analyzer referee
— and changes only the coder.

WHAT IT MEASURES (pre-registered, before any result was seen)
------------------------------------------------------------
  * first-pass verdict per codeunit, kept SEPARATE from the repair outcome
  * error count and error-class distribution, comparable to the qwen baseline above
  * whether a bounded repair loop reaches green, and in how many rounds
  * elapsed time and coder call count
  * whether ABS calls use real signatures or invented ones
  * a COMBINED pass, reported separately: three individually-valid codeunits may still
    fail each other's contracts

Interpretation rule, also pre-registered: capability is supported if ANY codeunit moves
from the qwen pattern (broad repeated failure, never green) to green via a short repair
path. First-pass green is stronger evidence but is not required. Routing changes only on
a green combined pass.

BASELINE
--------
Table + TableExt only. The pages also went green in the donor run, but a run directory
holds the stall fallback's REWRITE of the files, not the artifacts the ratchet placed —
the on-disk SetupCard.Page references a codeunit that is not there and cannot compile.
The green page versions were deleted and are unrecoverable; only the log is authoritative
about what went green. These two carry every symbol the codeunits consume, which is where
the AL0132 invented-member errors land.

The baseline is compiled and asserted green BEFORE any model runs. PTE0004 is accepted as
green exactly as the ratchet accepts it (the permission set is written last by design).

USAGE
-----
    EGRESS_POLICY=<profile> CODER_BACKEND=claude ./codeunit-probe.py

Egress is gated by egress_policy.py and this script refuses to run a cloud backend the
policy denies. That check is deliberate — do not route around it.
"""
import importlib.util
import json
import os
import re
import shutil
import sys
import time
from collections import Counter

BENCH = os.path.dirname(os.path.abspath(__file__))
DONOR = os.environ.get(
    "PROBE_DONOR",
    f"{BENCH}/runs/qwen3-coder_30b__doclink__incrab2_challenger__r9")
SYMS = os.environ.get(
    "PROBE_SYMBOLS",
    f"{BENCH}/runs/qwen3-coder_30b__doclink__apiab_control__r4/.alpackages")
TAG = os.environ.get("PROBE_TAG", "")
PROBE = os.environ.get("PROBE_ROOT",
                       f"{BENCH}/runs/probe_doclink_capability{('_' + TAG) if TAG else ''}")
REPAIR_ROUNDS = int(os.environ.get("PROBE_REPAIR_ROUNDS", "2"))

BASELINE = [
    "src/table/TSGDocumentLinkAZSetup.Table.al",
    "src/tableextension/TSGDocumentLink.TableExt.al",
]
# Probed in the order the ratchet attempted them.
TARGETS = [
    "src/codeunit/TSGDocumentLinkAZBlobMgt.Codeunit.al",
    "src/codeunit/TSGDocumentLinkAZMgt.Codeunit.al",
    "src/codeunit/TSGDocumentLinkBlobMigration.Codeunit.al",
]
REST = [
    "src/page/TSGDocumentLinkAZSetupCard.Page.al",
    "src/page/TSGDocumentLinkAZSetupList.Page.al",
    "src/permissionset/TSGDocumentLinkAZ.PermissionSet.al",
]

# ABS surface the qwen runs consistently got wrong — used for the "real signatures?" check.
_ABS_RE = re.compile(r'"(ABS [A-Za-z ]+)"')


def build_tree():
    """Fresh probe tree: baseline sources, symbol cache, path-rewritten handover."""
    if os.path.isdir(PROBE):
        shutil.rmtree(PROBE)
    os.makedirs(PROBE)
    shutil.copy2(f"{DONOR}/app.json", f"{PROBE}/app.json")
    for rel in BASELINE:
        dst = os.path.join(PROBE, rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(os.path.join(DONOR, rel), dst)
    shutil.copytree(SYMS, f"{PROBE}/.alpackages")
    # The handover's manifest carries ABSOLUTE paths pinned to the run that produced it.
    with open(f"{DONOR}/larry-handover.prompt.md", encoding="utf-8") as fh:
        text = fh.read().replace(DONOR, PROBE)
    with open(f"{PROBE}/larry-handover.prompt.md", "w", encoding="utf-8") as fh:
        fh.write(text)
    return text


def load_run_build():
    sys.path.insert(0, BENCH)
    spec = importlib.util.spec_from_file_location("run_build", f"{BENCH}/run-build.py")
    rb = importlib.util.module_from_spec(spec)
    sys.modules["run_build"] = rb
    spec.loader.exec_module(rb)
    rb.PROJECT_ROOT = PROBE
    rb._symbols_ready = True
    rb.EXPECTED_FILES = [os.path.join(PROBE, r) for r in (BASELINE + TARGETS + REST)]
    return rb


def classify(rb, text, ok, written):
    """The ratchet's own verdict, so probe results are comparable to incrab2 rows."""
    errs = rb.count_build_errors(text, ok)
    if ok and errs == 0:
        return "GREEN", 0
    if rb._permset_only(text, written):
        return "GREEN", 0          # PTE0004 only — permission set is written last
    return "RED", errs


def error_classes(text):
    return Counter(re.findall(r"error ((?:AL|AW|PTE)\d+)", text or ""))


def diagnostics_for(text, base):
    return [ln.strip() for ln in (text or "").splitlines()
            if base in ln and ": error " in ln]


def main():
    import egress_policy
    # _policy is a fail-safe local-only until this runs, so the check below would deny
    # everything regardless of configuration. run-build.py resolves against PROJECT_ROOT;
    # do the same so the probe and the pipeline agree on the policy in force.
    resolved = egress_policy.set_policy_for(PROBE)
    backend = os.environ.get("CODER_BACKEND", "pi")
    if backend == "claude":
        ok, why = egress_policy.escalation_available()
    elif backend == "mid":
        ok, why = egress_policy.mid_available()
    else:
        ok, why = True, f"local backend '{backend}'"
    if not ok:
        print(f"REFUSING: CODER_BACKEND={backend} but {why}")
        print("This gate is deliberate. Set the policy explicitly if you intend to allow it.")
        return 2

    handover = build_tree()
    rb = load_run_build()

    # AL_APIS grounding lives in run-build.py's main(), which this probe bypasses, so the
    # flag would otherwise be silently inert here. Apply the SAME augmentation explicitly
    # and report its size, so an AL_APIS arm is actually an AL_APIS arm.
    grounded_chars = 0
    if rb.AL_APIS:
        try:
            _apis = rb.ground_handover_apis(handover)
            if _apis:
                handover += _apis
                grounded_chars = len(_apis)
        except Exception as _e:
            print(f"  API grounding FAILED ({_e}) — arm is invalid, aborting")
            return 1
        if not grounded_chars:
            print("  API grounding produced nothing — arm would be identical to control, "
                  "aborting")
            return 1

    print(f"probe root : {PROBE}")
    print(f"AL_APIS    : {'on' if rb.AL_APIS else 'off'}"
          f"{f' (+{grounded_chars} chars grounded)' if grounded_chars else ''}")
    print(f"egress     : {resolved}")
    print(f"backend    : {backend}  ({why})")
    print(f"baseline   : {len(BASELINE)} file(s)\n")

    text, compiled = rb.run_al_compile()
    written = [os.path.join(PROBE, r) for r in BASELINE]
    verdict, errs = classify(rb, text, compiled, written)
    if verdict != "GREEN":
        print(f"\nABORT: baseline is not green ({errs} error(s)). The probe would measure "
              f"nothing.")
        for d in [ln.strip() for ln in text.splitlines() if ": error " in ln]:
            print(f"  {d}")
        return 1
    print("\nbaseline GREEN — proceeding\n")

    ledger, t0 = [], time.time()
    for rel in TARGETS:
        path = os.path.join(PROBE, rel)
        base = os.path.basename(rel)
        remaining = [os.path.join(PROBE, r) for r in TARGETS if r != rel]
        row = {"file": base, "first_pass": None, "first_errors": 0,
               "first_classes": {}, "repair_rounds": 0, "final": None,
               "final_errors": 0, "calls": 0, "abs_objects": [], "seconds": 0}
        t1 = time.time()
        print(f"=== {base} ===")

        msg = rb.build_single_file_msg(handover, path, remaining)
        for attempt in range(REPAIR_ROUNDS + 1):
            reply = rb.run_coder(msg, f"probe:{base}")
            row["calls"] += 1
            if not os.path.exists(path):
                print(f"  NOT WRITTEN (attempt {attempt + 1})")
                snippet = " ".join((reply or "").split())[:300]
                print(f"    model said: {snippet or '(no output)'}")
                row["final"] = "NOT WRITTEN"
                break

            src = open(path, encoding="utf-8-sig", errors="replace").read()
            row["abs_objects"] = sorted(set(_ABS_RE.findall(src)))
            text, compiled = rb.run_al_compile()
            verdict, errs = classify(rb, text, compiled, written + [path])
            classes = error_classes("\n".join(diagnostics_for(text, base)))

            if attempt == 0:
                row["first_pass"] = verdict
                row["first_errors"] = errs
                row["first_classes"] = dict(classes)
            row["final"], row["final_errors"] = verdict, errs
            print(f"  attempt {attempt + 1}: {verdict} ({errs} error(s)) "
                  f"{dict(classes) or ''}")

            if verdict == "GREEN":
                break
            if attempt == REPAIR_ROUNDS:
                break
            row["repair_rounds"] += 1
            diags = diagnostics_for(text, base)
            msg = (f"{handover}\n\n"
                   f"You wrote this file:\n    {path}\n\n"
                   f"It does not compile. The AL compiler reported:\n\n"
                   + "\n".join(f"  {d}" for d in diags[:40])
                   + "\n\nFix that file so it compiles. Do not create or modify any other "
                     "file. Use only members and signatures that actually exist in the "
                     "symbols; do not invent them. Then stop.")

        row["seconds"] = round(time.time() - t1)
        ledger.append(row)
        # Isolate: each codeunit is judged against the SAME baseline, not against whatever
        # the previous target happened to leave behind.
        if os.path.exists(path):
            shutil.move(path, os.path.join(PROBE, f".kept_{base}"))
        print()

    # --- combined pass: do the individually-valid codeunits satisfy each other? --------
    print("=== combined pass ===")
    restored = []
    for rel in TARGETS:
        base = os.path.basename(rel)
        kept = os.path.join(PROBE, f".kept_{base}")
        if os.path.exists(kept):
            shutil.move(kept, os.path.join(PROBE, rel))
            restored.append(os.path.join(PROBE, rel))
    combined = {"restored": len(restored), "verdict": None, "errors": 0, "classes": {}}
    if restored:
        text, compiled = rb.run_al_compile()
        verdict, errs = classify(rb, text, compiled, written + restored)
        combined.update(verdict=verdict, errors=errs,
                        classes=dict(error_classes(text)))
        print(f"  {len(restored)} codeunit(s) in tree: {verdict} ({errs} error(s))")
    else:
        print("  no codeunit was written — nothing to combine")

    # --- report ------------------------------------------------------------------------
    print(f"\n=== LEDGER ({backend}, {round(time.time() - t0)}s total) ===\n")
    print(f"  {'file':<44} {'1st':<6} {'err':>4}  {'rounds':>6}  {'final':<6} {'err':>4}  {'calls':>5}")
    for r in ledger:
        print(f"  {r['file']:<44} {str(r['first_pass'] or '-'):<6} {r['first_errors']:>4}  "
              f"{r['repair_rounds']:>6}  {str(r['final'] or '-'):<6} {r['final_errors']:>4}  "
              f"{r['calls']:>5}")
    print()
    for r in ledger:
        if r["first_classes"]:
            print(f"  {r['file']} first-pass classes: {r['first_classes']}")
        if r["abs_objects"]:
            print(f"  {r['file']} ABS objects referenced: {', '.join(r['abs_objects'])}")

    greens = [r for r in ledger if r["final"] == "GREEN"]
    first_greens = [r for r in ledger if r["first_pass"] == "GREEN"]
    print(f"\n  first-pass green: {len(first_greens)}/{len(TARGETS)}   "
          f"green after repair: {len(greens)}/{len(TARGETS)}")
    print(f"  combined: {combined['verdict'] or 'n/a'} "
          f"({combined['errors']} error(s))")
    print("\n  qwen3-coder:30b reference — 0 green in 21 ratchet attempts across 10 runs.")
    if greens:
        print("  → CAPABILITY SUPPORTED (pre-registered rule: any codeunit reaching green).")
        if combined["verdict"] == "GREEN":
            print("  → combined pass green: mutual contracts satisfied too; routing change "
                  "is justified.")
        else:
            print("  → combined pass NOT green: generation solved, mutual contracts not. "
                  "Contract-aware handover applies to the residual only.")
    else:
        print("  → CAPABILITY NOT SUPPORTED. A stronger model reproduces the same profile, "
              "so 'use a better model' is not the lever either.")

    out = os.path.join(BENCH,
                       f"PROBE-{backend}{('-' + TAG) if TAG else ''}-doclink-codeunits.json")
    with open(out, "w", encoding="utf-8") as fh:
        json.dump({"backend": backend, "tag": TAG, "al_apis": bool(rb.AL_APIS),
                   "grounded_chars": grounded_chars,
                   "ledger": ledger, "combined": combined}, fh, indent=2)
    print(f"\n  ledger written: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
