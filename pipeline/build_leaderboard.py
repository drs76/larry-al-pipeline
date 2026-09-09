#!/usr/bin/env python3
"""
build_leaderboard — aggregate per-build metrics into a model leaderboard.

Reads the JSONL that run-build.py appends per run (.build-metrics.jsonl) and renders:
  1. per-model table (first-pass/final/autonomous compile %, avg fix rounds, avg time,
     manifest %, Claude escalations)
  2. object-type first-pass success (where the workflow struggles)
  3. per-model diagnostic-category profile (why compile rounds happen)
  4. review value (BCQuality findings raised / cited / landed)

Writes reference/build-leaderboard.md and prints it. Empty until builds have run.

Env:
  BUILD_METRICS  metrics JSONL (default pipeline/.build-metrics.jsonl)
  LARRY_REPO     setup repo (default /mnt/rojaws/localDev/setup)
"""
import os, sys, json, datetime
from collections import defaultdict, Counter

HERE = os.path.dirname(os.path.abspath(__file__))
METRICS = os.environ.get("BUILD_METRICS", os.path.join(HERE, ".build-metrics.jsonl"))
REPO = os.environ.get("LARRY_REPO", "/mnt/rojaws/localDev/setup")
REPORT = f"{REPO}/reference/build-leaderboard.md"


def _load():
    rows = []
    if os.path.exists(METRICS):
        for ln in open(METRICS):
            ln = ln.strip()
            if ln:
                try:
                    rows.append(json.loads(ln))
                except json.JSONDecodeError:
                    pass
    return rows


def _pct(num, den):
    return f"{100 * num / den:.0f}%" if den else "—"


def _mean(vals, fmt="{:.1f}"):
    vals = [v for v in vals if isinstance(v, (int, float))]
    return fmt.format(sum(vals) / len(vals)) if vals else "—"


def main():
    rows = _load()
    stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    out = [f"# Model Build Leaderboard — {stamp}", ""]

    if not rows:
        out += ["_No build metrics recorded yet._ Runs are logged to "
                f"`{os.path.relpath(METRICS, REPO)}` as `run-build.py` executes; "
                "this table fills in as builds happen.", ""]
        _write(out)
        return 0

    # normalise model id: an explicit ':latest' tag and the bare name are the
    # same model — group them together so runs don't fragment into two rows.
    for r in rows:
        m = r.get("coder_model", "?")
        if m.endswith(":latest"):
            r["coder_model"] = m[: -len(":latest")]

    by = defaultdict(list)
    for r in rows:
        by[r.get("coder_model", "?")].append(r)

    out += [f"Aggregated from **{len(rows)}** build(s) across **{len(by)}** model(s). "
            "Compile rates depend on project difficulty — compare like-for-like "
            "(same projects across models).", ""]

    # ── 1. per-model table ──────────────────────────────────────────────
    rank = []
    for model, rs in by.items():
        n = len(rs)
        final = sum(1 for r in rs if r.get("final_compile"))
        rank.append((final / n, sum(1 for r in rs if r.get("first_pass_compile")) / n, n, model, rs))
    rank.sort(reverse=True)

    out += ["## Models", "",
            "| Model | Runs | First-pass | Final | Autonomous | Avg fix rounds | Regression rate | Fix efficiency | Avg time | Manifest | Claude esc. |",
            "|---|---|---|---|---|---|---|---|---|---|---|"]
    for _, _, n, model, rs in rank:
        first = sum(1 for r in rs if r.get("first_pass_compile"))
        final = sum(1 for r in rs if r.get("final_compile"))
        auton = sum(1 for r in rs if r.get("autonomous_pass"))
        esc = sum(1 for r in rs if r.get("claude_escalated"))
        man = sum(1 for r in rs if r.get("manifest_ok"))
        fr = [r["fix_rounds"] for r in rs if r.get("final_compile") and isinstance(r.get("fix_rounds"), int)]
        # regression rate = regressed rounds / rounds attempted (across runs that fixed anything)
        reg = sum(r.get("regressions", 0) for r in rs)
        att = sum(r.get("fix_rounds_attempted", 0) for r in rs)
        reg_rate = _pct(reg, att) if att else "—"
        # fix efficiency = errors cleared per fix round attempted
        cleared = sum(r.get("errors_cleared", 0) for r in rs)
        eff = f"{cleared/att:.1f}/rnd" if att else "—"
        out.append(f"| {model} | {n} | {_pct(first,n)} | {_pct(final,n)} | {_pct(auton,n)} | "
                   f"{_mean(fr)} | {reg_rate} | {eff} | {_mean([r.get('duration_s') for r in rs],'{:.0f}s')} | "
                   f"{_pct(man,n)} | {esc} ({_pct(esc,n)}) |")
    # --- mid rung: the ONE number the mid tier is judged on -----------------------
    # Warplan success #9 is ">=30% of previously-Claude builds closed by mid at >=
    # baseline pass rate". Its denominator is builds that REACHED the mid rung, not all
    # runs — a build the local coder closes on its own is the cheapest outcome and must
    # not dilute the ratio. Rows predating the mid tier have no mid_escalated key and
    # are excluded rather than counted as failures.
    midrows = [r for r in rows if r.get("mid_escalated")]
    if midrows:
        closed = sum(1 for r in midrows if r.get("mid_closed"))
        to_claude = sum(1 for r in midrows if r.get("claude_escalated"))
        # Split by CODER as well as mid model. A pooled figure is misleading: mixing a
        # coder that will never hold the slot with the real default produced a headline
        # "31%" that meant nothing (8 of 13 runs were an evaluation coder). The rung is
        # only judged on the coder actually in production.
        by = {}
        for r in midrows:
            by.setdefault((r.get("coder_model") or "?",
                           r.get("mid_model") or "(unrecorded)"), []).append(r)
        out += ["## Mid rung (OpenRouter) — criterion #9", "",
                f"Pooled: {closed}/{len(midrows)} = {_pct(closed, len(midrows))} closed at the mid "
                f"rung, {to_claude} went on to Claude. **Read the per-coder rows, not the pool** — "
                f"only the production coder's row answers the question.",
                "", "| Coder | Mid model | Reached mid | Closed by mid | Went to Claude | Avg time |",
                "|---|---|---|---|---|---|"]
        for (coder, m), rs in sorted(by.items(), key=lambda kv: -len(kv[1])):
            c = sum(1 for r in rs if r.get("mid_closed"))
            cl = sum(1 for r in rs if r.get("claude_escalated"))
            out.append(f"| {coder} | {m} | {len(rs)} | {c} ({_pct(c,len(rs))}) | {cl} | "
                       f"{_mean([r.get('duration_s') for r in rs],'{:.0f}s')} |")
        out += ["",
                "- Denominator is **builds that reached the mid rung**, i.e. the local coder had "
                "already stalled — the population the tier exists to serve.",
                "- A run counts as `mid_closed` only if it passed AND never reached Claude.",
                "- **The rung is OFF by default, on the evidence.** Tier A measured it at 0/10 "
                "closed against a control of 0/10 (Fisher p = 1.0) on the one bench fixture that "
                "discriminates, over 30 billed calls — `reference/bench-results/"
                "mid-ladder-tierA-results.md`. These opportunistic rows are not a substitute for "
                "that registered comparison: they carry no control arm.",
                "- To gather more, arm `ESCALATE_MID_AFTER=2 ESCALATE_AFTER=4` deliberately (mid "
                "tries first, Claude stays the backstop). It costs outcomes nothing and costs "
                "money.", ""]
    else:
        out += ["## Mid rung (OpenRouter) — criterion #9", "",
                "No run has reached the mid rung yet, and it is **OFF by default on the "
                "evidence**: Tier A measured it at 0/10 closed against a control of 0/10 "
                "(Fisher p = 1.0) — `reference/bench-results/mid-ladder-tierA-results.md`. "
                "Arming `ESCALATE_MID_AFTER=2 ESCALATE_AFTER=4` fills this section in (mid tries "
                "before Claude, Claude remains the backstop) and spends real money.", ""]

    out += ["",
            "- **First-pass** — compiled clean with zero fix rounds (raw AL quality).",
            "- **Final** — reached a clean build within the fix loop.",
            "- **Autonomous** — passed without escalating to Claude.",
            "- **Avg fix rounds** — mean rounds to a clean compile (0 = first-pass), over passing runs.",
            "- **Regression rate** — share of fix rounds that scored worse than best-so-far (edit instability).",
            "- **Fix efficiency** — compile errors cleared per fix round (higher = referee feedback lands).", ""]

    # ── 2. object-type first-pass success (overall) ─────────────────────
    present, failed = Counter(), Counter()
    for r in rows:
        for t in (r.get("objtypes_expected") or {}):
            present[t] += 1
        for t in (r.get("objtypes_failed_first_pass") or []):
            failed[t] += 1
    if present:
        out += ["## First-pass success by object type", "",
                "Share of builds where objects of this type compiled clean on the first pass "
                "(highlights where prompts/workflow need attention).", "",
                "| Object type | Builds w/ type | First-pass clean |", "|---|---|---|"]
        for t, p in sorted(present.items(), key=lambda kv: (present[kv[0]] - failed[kv[0]]) / kv[1]):
            out.append(f"| {t} | {p} | {_pct(p - failed[t], p)} |")
        out.append("")

    # ── 3. diagnostic-category profile per model ────────────────────────
    prof = {m: Counter() for m in by}
    for model, rs in by.items():
        for r in rs:
            prof[model].update(r.get("first_pass_diagnostics") or {})
    cats = sorted({c for p in prof.values() for c in p})
    if cats:
        out += ["## Why compile rounds happen (first-pass diagnostics)", "",
                "First-pass compile errors bucketed by category — a profile of each model's "
                "weak spots.", "",
                "| Model | " + " | ".join(cats) + " |",
                "|---|" + "|".join("---" for _ in cats) + "|"]
        for model in by:
            tot = sum(prof[model].values())
            cells = [f"{prof[model][c]} ({_pct(prof[model][c], tot)})" if tot else "—" for c in cats]
            out.append(f"| {model} | " + " | ".join(cells) + " |")
        out.append("")

    # ── 4. review value ─────────────────────────────────────────────────
    reviewed = [r for r in rows if r.get("review_backend")]
    if reviewed:
        out += ["## Review value (BCQuality-grounded)", "",
                "| Model | Reviews | Avg findings | Avg rule-cited | Landed |", "|---|---|---|---|---|"]
        rby = defaultdict(list)
        for r in reviewed:
            rby[r.get("coder_model", "?")].append(r)
        for model, rs in rby.items():
            landed = sum(1 for r in rs if r.get("review_landed"))
            out.append(f"| {model} | {len(rs)} | {_mean([r.get('review_findings_count') for r in rs])} | "
                       f"{_mean([r.get('review_rule_citations') for r in rs])} | {_pct(landed, len(rs))} |")
        out.append("")

    _write(out)
    return 0


def _write(lines):
    os.makedirs(os.path.dirname(REPORT), exist_ok=True)
    text = "\n".join(lines) + "\n"
    open(REPORT, "w").write(text)
    print(text)
    print(f"  report → {REPORT}")


if __name__ == "__main__":
    sys.exit(main())
