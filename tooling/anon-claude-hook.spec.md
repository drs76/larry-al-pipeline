# Spec — reversible anonymisation pre-hook for the Claude escalation path

**Status:** ALL PHASES BUILT (2026-07-07). 1–4: egress gate + reversible map + secret gate +
Mode B mirror. 5: pipeline wire-in — `pipeline/claude_egress.py` is the single Claude execution
chokepoint; all three orchestrators' `run_claude_code` delegate to it (enterprise-anon → scrubbed
mirror, arms `CLAUDE_ANON` itself; personal → raw; local-only → blocked). Startup arming uses
`egress_policy.escalation_available()` so enterprise-anon ARMS escalation instead of disarming.
**Owner:** dave. **Extends:** `tooling/anonymise.py`.

## 0. Policy profiles (dual-mode) — build this first

The anon hook is worthless if an escalation can call Claude *before* the hook exists, and pointless if
policy forbids egress entirely. So the foundation is a **deny-by-default egress chokepoint** that is
independent of the hook and works today. Whether the enterprise account lands next week or in two
months, nothing changes structurally — the account just **unlocks** an already-gated path.

### Profiles
| Profile | Egress to Anthropic | Coder path |
|---|---|---|
| **`local-only`** (**default**, today) | **none** | pi → Larry only; Claude escalation **hard-blocked** |
| **`enterprise-anon`** (when the account lands) | allowed **only via the anon hook** | escalation forced through secret-gate/reverse — never raw `claude` |
| **`personal`** (own box, non-work code) | allowed, raw | plain `claude`, no hook |

### Resolution — deny-by-default, per-repo
```
policy = repo .anon/config.yml [policy:]  >  env EGRESS_POLICY  >  global default (local-only)
```
Per-repo is the point: same WSL box, **work repo = `local-only`**, **personal repo = `personal`**,
no conflict. Absent config → `local-only` (fail safe).

### Single chokepoint
Every network-bound coder call passes one guard; there is no other way to reach Anthropic:
```py
def assert_egress_allowed(target):            # target = "anthropic"
    if POLICY == "local-only" and target == "anthropic":
        abort("egress disabled by deny-by-default; staying on Larry")
    if POLICY == "enterprise-anon" and not ANON_ACTIVE:
        abort("anthropic only via the anon hook")   # cannot bypass the scrub
```
In `run-build.py` the escalation latch (`_coder_state`, ~line 170) already exists — gate it here. Under
`local-only`, `ESCALATE_AFTER` is ignored and escalation **refuses** rather than calling `claude`; hard
tasks stay on Larry (optionally bump to a larger local model) or get flagged for manual handling. The
standalone `anon claude` (§7b) honours the same guard and refuses under `local-only`.

### Why first
Building §0 now (a) makes the work repo **safe today** — an accidental `claude` escalation cannot leak
— and (b) means enterprise onboarding is a **one-value flip** (`local-only` → `enterprise-anon`), not a
rebuild. If the hook isn't finished when the account arrives, `enterprise-anon` simply refuses until it
is. Both setups coexist from day one.

## 1. Problem & goal

Work-laptop repos may not be sent to Anthropic uncontrolled. Default analysis stays **local
(pi → Larry)** and never egresses. But some tasks escalate to **Claude** (soon an *enterprise*
Claude account with no-train / ZDR terms). Goal: before any repo content leaves WSL for Claude,
**reversibly substitute a declared set of sensitive tokens** (customer/person/vendor names, internal
hosts, tenant IDs), **one-way redact secrets**, then **de-anonymise Claude's edits** back to the real
tokens locally — while keeping the code semantically intact so fixes stay meaningful.

### Threat model / what this is and isn't
- **Primary control is the enterprise contract** (no training, retention limits). This hook is
  **defence-in-depth**, not the guarantee.
- **In scope (reversible):** named entities + identifiers from a project map, plus structural tokens
  (GUIDs, hostnames, user paths — reuse `anonymise.py` STRUCTURAL).
- **In scope (one-way):** secrets/keys/connection strings → replaced with inert dummies, **never
  restored**, and the run **blocks** if a high-confidence secret would otherwise be sent.
- **NOT in scope:** anonymising arbitrary code identifiers, business logic, or structure. Those go
  to Claude as-is — that's the deliberate trade-off for meaningful fixes. **Proprietary logic still
  leaves the machine.** Say this to any user of the tool; don't oversell it as "anonymised code".

## 2. Why workspace-level, not prompt-level

`run_claude_code()` (`pipeline/run-build.py:241`) invokes:
```py
cmd = [CLAUDE_BIN, "-p", prompt, "--permission-mode", "bypassPermissions"]
subprocess.run(cmd, cwd=PROJECT_ROOT, ...)
```
Claude Code is **agentic**: it opens/edits the real files under `PROJECT_ROOT` with its own
Read/Write/Edit/Bash tools. Scrubbing only the `prompt` string leaks every file Claude reads itself.
So the hook must present Claude a **scrubbed mirror of the working tree** and reverse-map whatever it
changed.

Two modes, one shared map engine:
- **Mode A — prompt-level** (for `pi -p` / any single-shot "here is code → return a diff" call):
  scrub the outgoing prompt, reverse the returned text. Cheap; sufficient when the model never
  touches the filesystem.
- **Mode B — workspace-mirror** (for the agentic `claude` CLI): the primary mode. See §4.

## 3. Components

| Component | Role |
|---|---|
| `.anon/config.yml` (per repo, **gitignored**) | which detectors on; extra name rules; secret-scan toggles; path allow/deny |
| `.anon/map.tsv` (per repo, **gitignored**) | persisted `real⇥placeholder` pairs — the source of reversibility. Append-only, stable across runs |
| `anon forward` | build/extend map, write scrubbed mirror (Mode B) or scrubbed text (Mode A) |
| `anon reverse` | apply inverse map to Claude's output (diff or mirror tree) → real-token patch |
| secret gate | high-confidence secret scan; dummy-replace + **hard block** on leak; logged, never mapped |
| wrapper | orchestrates forward → run Claude → reverse → apply; wired into `run_claude_code` and exposed as a standalone CLI |

Reuse `anonymise.py`'s `STRUCTURAL` rules and map-file loader; this tool is its reversible superset.

## 4. Mode B data flow (primary)

```
PROJECT_ROOT (real)                          mirror = $XDG_RUNTIME/anon/<proj>/  (scrubbed copy)
      │  git worktree/copy of tracked files        │
      ├─ anon forward ───────────────────────────► │  files with tokens → placeholders
      │     · load .anon/map.tsv (stable)           │  map extended for new tokens
      │     · secret gate (block on leak)           │
      │                                             ▼
      │                                   claude -p  (cwd = mirror, bypassPermissions)
      │                                             │  edits mirror in place
      │                                             ▼
      │                                   git diff in mirror  ──► scrubbed patch
      ◄─ anon reverse (inverse map) ◄───────────────┘
      │     placeholder → real on the *patch text*
      ▼
   git apply --3way   → real edits land in PROJECT_ROOT
```

Notes:
- Mirror only **tracked** files (respect `.gitignore`); never copy `.git`, build output, `node_modules`,
  binaries — skip non-text by MIME.
- Diff-then-reverse-then-apply (not reverse-whole-mirror): smaller surface, and `git apply --3way`
  cleanly merges onto the real tree; new files Claude creates appear in the diff and are reversed too.
- Run under a temp dir on WSL's local fs (not the NFS mount) for speed.

## 5. Placeholder design (reversibility correctness)

Placeholders must survive an LLM round-trip **and** be exactly invertible:
- **Identifier-safe sentinels**, not fancy unicode: `ANON_NAME_01`, `ANON_HOST_02`, `ANON_TENANT_03`.
  The model treats them as opaque identifiers and preserves them verbatim; unicode brackets risk being
  reformatted/normalised and breaking the inverse.
- **Stable & collision-free:** same real token → same placeholder every run (persisted in `map.tsv`),
  so multi-file consistency holds and the inverse is a function. Never reuse an index for two reals.
- **Word-boundary aware** for short/ambiguous tokens (`\bACME\b`) so we don't corrupt substrings.
- **Longest-match-first** ordering (already the map convention) so `Acme Trading Ltd` maps before `Acme`.
- **Inverse safety:** a placeholder must never be a substring of another placeholder (zero-pad the
  index, keep a fixed prefix) so reverse can't partially match.

## 6. Secret handling (one-way, blocking)

Separate path from reversible tokens. Scanner patterns: private keys (`BEGIN … PRIVATE KEY`), AWS/GCP/
Azure keys, bearer/JWT, DB connection strings, `.env` `KEY=value`, high-entropy strings.
- Match → replace with an **inert dummy** (`REDACTED_SECRET`), record location, **do not** add to
  `map.tsv` (never restored).
- On a **high-confidence** secret, **fail closed**: abort the escalation with a report unless
  `--allow-redacted-secrets` is explicitly passed. Secrets should be removed from the repo, not shipped
  even as dummies.

## 7. Integration

### 7a. Pipeline (`run_claude_code`)
Gate on `CLAUDE_ANON=1`. Wrap the existing call:
```py
if os.environ.get("CLAUDE_ANON") == "1":
    mirror, amap = anon_forward(PROJECT_ROOT)        # secret gate may raise/block here
    out = _run_claude(prompt=anon_text(prompt, amap), cwd=mirror)
    patch = git_diff(mirror)
    git_apply(PROJECT_ROOT, anon_reverse(patch, amap))
    return anon_reverse(out, amap)                    # de-anon the transcript too
else:
    ... existing path ...
```
Keep it opt-in so the free local prototype pipeline is unaffected.

### 7b. Standalone (work repo on WSL — the actual driver)
```sh
anon claude "refactor the retry logic in billing/*.go"     # forward→claude→reverse→apply
anon status        # show map size, last secret-gate result
anon map --edit     # curate name rules
```
Ships with the WSL client (add to `wsl-setup.md` step 6). `.anon/` is per-repo + gitignored.

## 8. Edge cases / failure modes

| Case | Handling |
|---|---|
| LLM alters a placeholder (`ANON_NAME_01` → `anonName01`) | reverse pass reports unmatched sentinels; warn + leave literal; count as a round-trip defect metric |
| Claude creates a new file naming a real concept | it only ever saw placeholders, so output stays scrubbed; reverse maps known tokens, unknown stay generic |
| Real token is also a common English word | require `\b` + min length; prefer explicit map entries over auto-detect; allow deny-list |
| Partial / failed `git apply` | `--3way`; on reject, dump `.rej` and stop — never half-apply silently |
| Binary / generated / vendored files | excluded from mirror by gitignore + MIME sniff |
| Path leakage (`/home/<user>/...`, UNC, tenant in a URL) | covered by STRUCTURAL + host/user rules; add work-domain patterns to config |
| Map drift between runs | `map.tsv` append-only + stable; never renumber |

## 9. Verification

- **Round-trip identity:** `reverse(forward(x)) == x` for a corpus of real tokens (property test).
- **No-leak:** grep the scrubbed mirror + outgoing prompt for every real token in `map.tsv` and every
  secret pattern → must be zero before any network call (assert as a gate, not just a test).
- **Apply fidelity:** on a fixture repo, a known Claude edit reverses + `git apply`s to the exact
  expected real-token diff.
- **Secret block:** a planted AWS key aborts the run without egress.

## 10. Phasing

1. **Policy switch + deny-by-default (§0)** — ✅ **BUILT** (2026-07-05).
   `pipeline/egress_policy.py` (shared: resolve per-repo > env > `local-only`; `allowed()` gate).
   Wired into the single Claude funnel `run_claude_code()` **and** the startup checks of all three
   orchestrators (`run-build.py`, `run-build-go.py`, `run-build-cs.py`): under a blocking policy,
   `CODER_BACKEND=claude` errors out and `ESCALATE_AFTER` is disarmed so the latch never flips.
   Standalone `tooling/anon` (`policy` / `claude` / `check`) gates the ad-hoc work→Claude path;
   `tooling/anon-config.example.yml` is the per-repo `.anon/config.yml` template (gitignore `.anon/`).
   Verified: default→local-only, env override, repo-overrides-env, block→exit 3, `anon check`.
2. **Map engine + reverse** — ✅ **BUILT** (2026-07-05). `pipeline/anon_map.py`: `AnonMap`
   (bidirectional, append-only, persisted `.anon/map.tsv`), stable identifier-safe sentinels
   (`ANON_<CAT>_NNN`), built-in reversible structural detectors (GUID/user-path), `forward()` /
   `reverse()` / `residual_reals()` no-leak check, `load_names()` for curated `.anon/names.tsv`
   literals. Case-sensitive by design. `tooling/anon forward|reverse` (Mode A). Property tests
   `pipeline/test_anon_map.py` (7 pass): round-trip identity, no-leak, stability across reload,
   multi-file consistency, inverse-safety (001 vs 012), longest-literal-first, case-sensitivity.
   Verified e2e via the CLI (forward→reverse = identical).
3. **Secret gate** — ✅ **BUILT** (2026-07-05). `pipeline/secret_gate.py`: provider-shaped
   detectors (private keys, AWS/GCP/GitHub/Slack tokens, Azure storage key, JWT, DB password) as
   HIGH; generic `secret=`/`token=`/bearer as MED. `scan()` / `redact()` (one-way → `REDACTED_SECRET`,
   idempotent) / `gate()` fail-closed on HIGH. `tooling/anon secrets` (exit 2 on HIGH) and
   `anon scrub` = forward + redact + **pre-network no-leak assertion** (no declared real, no live
   secret survives) → the safe-to-send artifact; aborts on HIGH unless `--allow-secrets`. Tests
   `pipeline/test_secret_gate.py` (6 pass) + e2e verified (abort/clean-round-trip/med-allow).
4. **Mode B** — ✅ **BUILT** (2026-07-05). `pipeline/anon_workspace.py`: `run_workspace()` mirrors
   git-tracked TEXT files scrubbed (binaries skipped, `.gitignore` respected via `git ls-files`),
   commits a scrubbed baseline, runs a `coder_fn(mirror, prompt)` (production: `claude -p` in the
   mirror), diffs the mirror, `reverse()`s the patch to real tokens, `git apply`s to the real repo
   (`.rej` on conflict, never half-applies). HIGH secret → `SecretAbort` before the coder runs.
   `tooling/anon run` (egress-gated: sets `CLAUDE_ANON=1`, so `local-only` still blocks). Coder is
   injectable → tested without egress. Tests `pipeline/test_anon_workspace.py` (4 pass) + CLI e2e
   with a fake coder: local-only blocks (repo untouched), personal applies real tokens, no leak.
5. **Pipeline wire-in** — `CLAUDE_ANON` + `enterprise-anon` profile in `run_claude_code`; document in
   `wsl-setup.md` + `RUN-BUILD.md`. Flip the work repo `local-only` → `enterprise-anon` when the
   account lands.

## 11. Open questions

- **RESOLVED 2026-07-06 — enterprise account arrived.** Ruling: **code may be shared; personal
  identifiers may not.** That keeps the full reversible name-map in scope (names/hosts/tenant IDs/
  emails scrubbed; code logic flows). An EMAIL auto-detector was added to `anon_map.py` to cover the
  auto-detectable personal-identifier class; people/customer names stay curated in `.anon/names.tsv`.
  Work repos flip `local-only` → `enterprise-anon`; egress only via the scrubbing paths (`anon run`
  / `anon scrub`) — raw `anon claude` stays blocked under this profile by design.
- Auto-detect named entities (NER) vs. curated map only? Start curated (predictable, no false renames).
- Multi-repo shared map vs. per-repo? Per-repo default; shared optional for common infra hostnames.
