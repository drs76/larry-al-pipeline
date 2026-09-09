#!/usr/bin/env python3
"""
bcquality — deterministic selector over a local BCQuality clone.

BCQuality (github.com/microsoft/BCQuality) is a knowledge base of atomic BC/AL rules.
Its own consumption model runs multi-step review *skills* in a capable agent. Our local
validator model can't orchestrate that, so instead we pick the rules relevant to the
changed AL — by keyword overlap against the source — and hand them to the reviewer as a
cited checklist. Same knowledge, no agent orchestration required.

Two consumers:
  * coms_review.review()  — injects the checklist into the validator-peer request.
  * the coder handover     — CLI mode prints the checklist to fold into a prompt.

Selection is deterministic (no LLM): keyword/title overlap, layer precedence
(custom > community > microsoft), capped. Fail-open: no clone / no index → [].

Env:
  BCQUALITY_ROOT  path to the clone (default: /mnt/rojaws/localDev/BCQuality)
"""
import os, re, json, sys, glob, math

DEFAULT_ROOT = "/mnt/rojaws/localDev/BCQuality"
LAYER_RANK = {"custom": 2, "community": 1, "microsoft": 0}
_WORD = re.compile(r"[a-z][a-z0-9]+")

# Ubiquitous AL structural/type tokens — present in almost every file, so a keyword
# match on them carries no relevance signal. Dropped before scoring.
AL_STOP = {
    "codeunit", "record", "procedure", "local", "var", "begin", "end", "trigger",
    "table", "tableextension", "page", "pageextension", "report", "field", "fields",
    "key", "keys", "namespace", "using", "text", "code", "boolean", "integer", "decimal",
    "option", "enum", "interface", "exit", "then", "else", "true", "false", "value",
    "data", "name", "type", "object", "app", "src", "get", "set", "new", "for", "all",
}


def _root(root=None):
    return root or os.environ.get("BCQUALITY_ROOT", DEFAULT_ROOT)


def _load_index(root):
    idx = os.path.join(root, "knowledge-index.json")
    if not os.path.exists(idx):
        return []
    try:
        return json.load(open(idx)).get("articles", [])
    except Exception:
        return []


def _tokens(text):
    """Lowercased word tokens of AL source — identifiers, keywords, captions."""
    return set(_WORD.findall((text or "").lower()))


def _kw_tokens(keywords):
    """Expand an article's keyword list into comparable tokens (split hyphens too)."""
    out = set()
    for k in keywords or []:
        k = k.lower()
        out.add(k.replace("-", ""))
        out.update(_WORD.findall(k))
    return out


def _section(md_text, heading):
    """Return the body of a '## <heading>' section, sans 'See sample:' pointer lines."""
    m = re.search(rf"^##\s+{re.escape(heading)}\s*$(.*?)(^##\s|\Z)",
                  md_text, re.MULTILINE | re.DOTALL)
    if not m:
        return ""
    body = "\n".join(ln for ln in m.group(1).strip().splitlines()
                     if not ln.strip().lower().startswith("see sample"))
    return body.strip()


def _oneline(text, limit=240):
    """Collapse a section to a single trimmed line for a compact checklist."""
    t = re.sub(r"```.*?```", "", text, flags=re.DOTALL)          # drop code fences
    t = re.sub(r"\s+", " ", t).strip()
    return (t[:limit].rstrip() + "…") if len(t) > limit else t


def version_matches(spec, bc_version):
    """Does a rule's `bc-version:` frontmatter apply to this BC major?

    The KB writes four forms and all of them are in live use:
        [all]        unconstrained
        [26, 27, 28] an explicit set
        [16..]       open-ended: from BC16 onward
        [26..28]     closed range

    An exact string comparison — which is what this did before anything ever passed a
    version — silently DROPS every ranged rule. Those are the "feature exists from BC N"
    rules, i.e. exactly the ones a modern target most needs, so the failure is not just a
    miss, it is biased towards losing the useful ones.

    Unparseable or absent spec means "applies", because losing a real rule to a
    frontmatter typo is worse than applying one rule too broadly.
    """
    # AL-16: one temporal model for every KB. al_temporal generalises this to
    # introduced/removed/deprecated and runtime bounds while still accepting the range
    # forms already written across the BCQuality articles.
    try:
        import al_temporal
        return al_temporal.applies({"bc-version": spec or ["all"]}, bc_version)[0]
    except Exception:
        pass
    try:
        target = int(str(bc_version).split(".")[0])
    except (TypeError, ValueError):
        return True
    for raw in (spec or ["all"]):
        tok = str(raw).strip()
        if tok.lower() == "all":
            return True
        if ".." in tok:
            lo, _, hi = tok.partition("..")
            try:
                if target < int(lo.strip()):
                    continue
                if hi.strip() and target > int(hi.strip()):
                    continue
                return True
            except ValueError:
                return True
        else:
            try:
                if int(tok) == target:
                    return True
            except ValueError:
                return True
    return False


def rules_for(files, root=None, bc_version=None, max_rules=12, min_score=1):
    """Select BCQuality rules relevant to the changed AL.

    files       : list of (relpath, content) — same shape coms_review consumes.
    bc_version  : int/str target; None = unconstrained. Matches 'all' or the exact value.
    Returns a list of dicts: {path, title, layer, domain, best, anti} ranked most-relevant.
    """
    root = _root(root)
    articles = _load_index(root)
    if not articles:
        return []

    src = _tokens("\n".join(c for _, c in files)) - AL_STOP
    if not src:
        return []
    bcv = str(bc_version) if bc_version is not None else None

    al_articles = [a for a in articles if "al" in (a.get("technologies") or ["al"])]
    # IDF over the keyword vocabulary: a rule matched on a rare, distinctive keyword
    # (commit, datatransfer, findset, setloadfields) outweighs one matched on a common
    # keyword, so precise rules rank above keyword-dense generic ones.
    N = len(al_articles) or 1
    df = {}
    for a in al_articles:
        for t in _kw_tokens(a.get("keywords")) - AL_STOP:
            df[t] = df.get(t, 0) + 1

    def _idf(t):
        return math.log((N + 1) / (df.get(t, 0) + 1)) + 1.0

    scored = []
    for a in al_articles:
        if bcv is not None and not version_matches(a.get("bc-version"), bcv):
            continue
        kw_hits = (_kw_tokens(a.get("keywords")) & src) - AL_STOP
        if not kw_hits:
            continue   # require at least one distinctive keyword match
        title_hits = (_tokens(a.get("title")) & src) - AL_STOP
        score = 2.0 * sum(_idf(t) for t in kw_hits) + 0.5 * sum(_idf(t) for t in title_hits)
        if score >= min_score:
            scored.append((score, LAYER_RANK.get(a.get("layer"), 0), a))

    scored.sort(key=lambda t: (t[0], t[1]), reverse=True)

    # Diversify across domains: a page with many actions shouldn't fill the whole
    # worklist with UI rules and starve performance/security/error-handling. Cap each
    # domain, then backfill from the ranked remainder if fewer domains matched.
    cap = max(2, math.ceil(max_rules / 4))
    picked, per_domain, seen = [], {}, set()
    for _, _, a in scored:
        d = a.get("domain", "")
        if per_domain.get(d, 0) >= cap:
            continue
        picked.append(a); seen.add(a["path"]); per_domain[d] = per_domain.get(d, 0) + 1
        if len(picked) >= max_rules:
            break
    if len(picked) < max_rules:
        for _, _, a in scored:
            if a["path"] not in seen:
                picked.append(a); seen.add(a["path"])
                if len(picked) >= max_rules:
                    break

    rules = []
    for a in picked:
        r = _read_rule(root, a)
        if r:
            rules.append(r)
    return rules


def _read_rule(root, a):
    """Load one index article's .md and extract the checklist fields."""
    try:
        md = open(os.path.join(root, a["path"])).read()
    except OSError:
        return None
    return {
        "path": a["path"], "title": a.get("title", a["path"]),
        "layer": a.get("layer", ""), "domain": a.get("domain", ""),
        "best": _oneline(_section(md, "Best Practice")),
        "anti": _oneline(_section(md, "Anti Pattern")),
    }


def coder_rules(handover_text, root=None, bc_version=None, max_rules=10):
    """Rules to inject into the CODER prompt at write time — before any source exists.

    Always includes the custom authoring-gotcha layer (universal AL-authoring rules that
    won't necessarily keyword-match a spec), plus rules whose keywords match the handover
    intent text. Deduped, custom first.
    """
    root = _root(root)
    arts = _load_index(root)
    if not arts:
        return []
    custom = [a for a in arts if a.get("layer") == "custom"
              and "al" in (a.get("technologies") or ["al"])]
    matched = rules_for([("intent", handover_text)], root=root,
                        bc_version=bc_version, max_rules=max_rules)
    seen, out = set(), []
    for a in custom:
        r = _read_rule(root, a)
        if r and r["path"] not in seen:
            seen.add(r["path"]); out.append(r)
    for r in matched:
        if r["path"] not in seen:
            seen.add(r["path"]); out.append(r)
    return out


def coder_checklist(handover_text, root=None, bc_version=None):
    """Formatted 'rules to follow' section for appending to a coder handover. '' if none."""
    rules = coder_rules(handover_text, root, bc_version)
    if not rules:
        return ""
    return "## BC/AL rules to follow (BCQuality — write compile-clean AL that obeys these)\n\n" \
        + format_checklist(rules)


def format_checklist(rules):
    """Render selected rules as a compact, citeable checklist for a review/coder prompt."""
    if not rules:
        return ""
    lines = []
    for r in rules:
        line = f"- {r['title']} [rule: {r['path']}]"
        if r["best"]:
            line += f"\n    DO: {r['best']}"
        if r["anti"]:
            line += f"\n    AVOID: {r['anti']}"
        lines.append(line)
    return "\n".join(lines)


if __name__ == "__main__":
    # CLI: bcquality.py <src-dir> [bc_version] — print the checklist for the AL under src-dir.
    if len(sys.argv) < 2:
        sys.exit("usage: bcquality.py <src-dir> [bc_version]")
    src_dir = sys.argv[1]
    bcv = sys.argv[2] if len(sys.argv) > 2 else None
    fs = [(os.path.relpath(f, src_dir), open(f).read())
          for f in glob.glob(src_dir + "/**/*.al", recursive=True)]
    rules = rules_for(fs, bc_version=bcv)
    if not rules:
        print("(no BCQuality rules selected — clone/index missing or no keyword overlap)")
    else:
        print(f"# {len(rules)} BCQuality rule(s) relevant to {src_dir}\n")
        print(format_checklist(rules))
