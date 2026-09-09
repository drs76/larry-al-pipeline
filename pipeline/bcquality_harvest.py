#!/usr/bin/env python3
"""
bcquality_harvest — pull the BCQuality clone, resync our custom layer, rebuild the
knowledge index, and report what's NEW or CHANGED since the last harvest.

Microsoft adds/edits knowledge rules over time. This surfaces the delta so it can be
folded into reference/AL-REFERENCE.md (a curation step — we do NOT auto-edit the
reference, because harvesting sometimes means correcting an existing rule, not just
appending, and that needs a human/Claude judgement call).

Run by the Larry dashboard action, or standalone:
    python3 bcquality_harvest.py

Env:
  BCQUALITY_ROOT  clone path (default /mnt/rojaws/localDev/BCQuality)
  LARRY_REPO      setup repo (default /mnt/rojaws/localDev/setup) — for the custom layer
"""
import os, sys, re, json, hashlib, subprocess, datetime, glob, shutil

BCQ = os.environ.get("BCQUALITY_ROOT", "/mnt/rojaws/localDev/BCQuality")
REPO = os.environ.get("LARRY_REPO", "/mnt/rojaws/localDev/setup")
CUSTOM_SRC = f"{REPO}/pipeline/bcquality-custom/knowledge"
SNAPSHOT = f"{BCQ}/.harvest-snapshot.json"
REPORT = f"{REPO}/reference/bcquality-harvest-report.md"
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def sh(cmd, cwd=None):
    print(f"$ {' '.join(cmd)}", flush=True)
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    out = (r.stdout + r.stderr).strip()
    if out:
        print(out, flush=True)
    return r.returncode == 0, out


def _hash(path):
    try:
        return hashlib.md5(open(path, "rb").read()).hexdigest()
    except OSError:
        return ""


def _fm_val(raw):
    """Parse a frontmatter scalar or [a, b] list into a Python value."""
    raw = raw.strip()
    if raw.startswith("[") and raw.endswith("]"):
        return [x.strip() for x in raw[1:-1].split(",") if x.strip()]
    return raw


def _reindex(bcq):
    """Rebuild knowledge-index.json. Prefer BCQuality's own pwsh generator (exact, incl.
    description); fall back to a Python walk when pwsh is absent (e.g. on Larry) — exact
    for every field the selector and harvest read (path/layer/domain/keywords/title/
    frontmatter), description best-effort."""
    if shutil.which("pwsh"):
        ok, _ = sh(["pwsh", f"{bcq}/tools/Build-KnowledgeIndex.ps1"])
        if ok:
            return
        print("  pwsh reindex failed — falling back to python indexer", flush=True)
    print("  (pwsh not found — python index fallback)", flush=True)
    articles = []
    for layer in ("microsoft", "community", "custom"):
        for f in sorted(glob.glob(f"{bcq}/{layer}/knowledge/**/*.md", recursive=True)):
            txt = open(f).read()
            fm = {}
            if txt.startswith("---"):
                end = txt.find("\n---", 3)
                for ln in txt[3:end].splitlines():
                    if ":" in ln:
                        k, v = ln.split(":", 1)
                        fm[k.strip()] = _fm_val(v)
            title = next((l[2:].strip() for l in txt.splitlines() if l.startswith("# ")),
                         os.path.basename(f))
            desc = ""
            m = re.search(r"^##\s+Description\s*$(.*?)(^##|\Z)", txt, re.M | re.S)
            if m:
                desc = " ".join(m.group(1).split())[:200]
            articles.append({
                "path": os.path.relpath(f, bcq).replace(os.sep, "/"), "layer": layer,
                "domain": fm.get("domain", ""), "keywords": fm.get("keywords", []),
                "title": title, "description": desc,
                "bc-version": fm.get("bc-version", ["all"]),
                "technologies": fm.get("technologies", ["al"]),
                "countries": fm.get("countries", ["w1"]),
                "application-area": fm.get("application-area", ["all"]), "parsed": True})
    idx = {"version": 1, "generatedAt": datetime.datetime.now().isoformat(),
           "enabledLayers": ["microsoft", "community", "custom"],
           "knowledgeAllow": [], "knowledgeDeny": [],
           "articleCount": len(articles), "articles": articles}
    json.dump(idx, open(f"{bcq}/knowledge-index.json", "w"), indent=1)
    print(f"  python index: {len(articles)} article(s)", flush=True)


def main():
    if not os.path.isdir(os.path.join(BCQ, ".git")):
        print(f"ERROR: no BCQuality clone at {BCQ}", flush=True)
        return 1

    print("=== 1. git pull ===", flush=True)
    sh(["git", "-C", BCQ, "pull", "--ff-only"])

    print("\n=== 2. resync custom layer from setup ===", flush=True)
    if os.path.isdir(CUSTOM_SRC):
        dst = f"{BCQ}/custom/knowledge"
        os.makedirs(dst, exist_ok=True)
        n = 0
        for f in glob.glob(CUSTOM_SRC + "/**/*.md", recursive=True):
            rel = os.path.relpath(f, CUSTOM_SRC)
            tgt = os.path.join(dst, rel)
            os.makedirs(os.path.dirname(tgt), exist_ok=True)
            shutil.copy2(f, tgt)
            n += 1
        print(f"  synced {n} custom rule(s)", flush=True)

    print("\n=== 3. rebuild knowledge index ===", flush=True)
    _reindex(BCQ)

    print("\n=== 4. diff vs last harvest ===", flush=True)
    import bcquality
    try:
        articles = json.load(open(f"{BCQ}/knowledge-index.json")).get("articles", [])
    except Exception as e:
        print(f"ERROR: cannot read index: {e}", flush=True)
        return 1

    cur = {}
    for a in articles:
        p = a["path"]
        cur[p] = {"hash": _hash(os.path.join(BCQ, p)),
                  "title": a.get("title", p), "domain": a.get("domain", "")}

    prev = {}
    if os.path.exists(SNAPSHOT):
        try:
            prev = json.load(open(SNAPSHOT)).get("articles", {})
        except Exception:
            prev = {}

    baseline = not prev
    new = [p for p in cur if p not in prev]
    changed = [p for p in cur if p in prev and cur[p]["hash"] != prev[p]["hash"]]
    removed = [p for p in prev if p not in cur]

    stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = [f"# BCQuality harvest report — {stamp}", ""]
    if baseline:
        lines += [f"**Baseline established:** {len(cur)} articles indexed. "
                  "Future harvests report only new/changed rules.", ""]
        print(f"  baseline: {len(cur)} articles (no diff on first run)", flush=True)
    else:
        lines += [f"Since last harvest: **{len(new)} new**, **{len(changed)} changed**, "
                  f"**{len(removed)} removed**. Total {len(cur)} articles.", ""]
        print(f"  {len(new)} new, {len(changed)} changed, {len(removed)} removed", flush=True)

        def block(title, paths):
            if not paths:
                return []
            out = [f"## {title} ({len(paths)})", ""]
            for p in sorted(paths):
                a = cur.get(p) or prev.get(p)
                best = ""
                if p in cur:
                    try:
                        best = bcquality._oneline(
                            bcquality._section(open(os.path.join(BCQ, p)).read(), "Best Practice"), 200)
                    except OSError:
                        best = ""
                out.append(f"- **[{a['domain']}]** {a['title']}  \n  `{p}`"
                           + (f"  \n  DO: {best}" if best else ""))
            out.append("")
            return out

        lines += block("🆕 New rules", new)
        lines += block("✏️ Changed rules", changed)
        if removed:
            lines += ["## 🗑️ Removed rules", ""] + [f"- `{p}`" for p in sorted(removed)] + [""]
        lines += ["---", "*Review these and fold into `reference/AL-REFERENCE.md`. "
                  "Harvesting may mean correcting an existing rule, not just appending.*"]

    os.makedirs(os.path.dirname(REPORT), exist_ok=True)
    open(REPORT, "w").write("\n".join(lines))
    print(f"\n  report → {REPORT}", flush=True)

    json.dump({"generated": stamp, "articles": cur}, open(SNAPSHOT, "w"), indent=0)
    print("  snapshot updated. Done.", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
