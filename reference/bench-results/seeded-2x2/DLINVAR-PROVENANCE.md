# dlinvar A/B — provenance

pre  (control)    = 0548e1f88810e649d525f5b0ed200b5890c99e3a   0548e1f, treatment ABSENT
post (challenger) = 7784470f44f29e5438ad25628e5cda40261ebc9b   7784470, treatment PRESENT
model both arms   = ollama/qwen3-coder:30b
repeats           = 5/arm, interleaved, one session
suite             = bench-run-suite.sh dlinvar, RUNBUILD=dispatch-runbuild.py
arm dispatch      = CONTROL_ENV=PIPELINE_VARIANT=pre / CHALLENGER_ENV=PIPELINE_VARIANT=post
predicate frozen  = 2026-09-01T21:34:59+01:00 (before challenger r2-r5)

Classification: FAILED ENDPOINT/DESIGN TEST, not a failed treatment test.
See feedback_endpoint_mechanism_mismatch in memory.
