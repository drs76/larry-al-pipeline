"""al_errors — recurring AL diagnostics turned into targeted, evidence-linked guidance.

The compiler says what is wrong. It does not say why a 30B coder keeps getting that
particular thing wrong, and that gap is the difference between one fix round and sixteen:
AL0133 sent one build oscillating between InStream and OutStream for sixteen rounds, and
AL0282 froze another for six because "parameter not found" reads like the EVENT is wrong
rather than the parameter NAME.

Three rules keep this honest.

  * **The compiler always wins.** Guidance is rendered ALONGSIDE the real diagnostic
    text, never in place of it. If the KB and the compiler disagree, the KB is out of
    date — this module cannot suppress, rewrite or contradict a diagnostic.
  * **Every entry cites its evidence.** Guidance without provenance is a guess in an
    authoritative voice, and this project has already shipped one: an AL-SYNTAX rule
    claimed CodeCop enforced per-field DataClassification when no cop does. Entries here
    name the build that cost the rounds, or the probe that established what the toolchain
    actually emits.
  * **Version-aware.** A rule that exists from BC24 must not be quoted at a BC14 target,
    so `bc-version` accepts the same range forms as the BCQuality KB.

One file, `al-errors.yml`, defines both what a diagnostic MEANS and how `error_profile.py`
categorises it — previously those were two hardcoded lists that could drift apart.
"""
from __future__ import annotations

import os
import re

_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "al-errors.yml")
_cache = None

# `error AL0132: 'Record X' does not contain ...` / `warning AA0218: ...` / a bare code.
_CODE_RE = re.compile(r"\b([A-Z]{2,3}\d{4})\b")

CATEGORIES = ("syntax", "symbols", "types", "events", "duplicate", "rules", "obsolete")


def _load(path=None):
    global _cache
    if _cache is not None and path is None:
        return _cache
    try:
        import yaml
        with open(path or _FILE) as f:
            doc = (yaml.safe_load(f) or {}).get("errors") or {}
    except Exception:
        doc = {}
    doc = {normalise(k): v for k, v in doc.items()}
    if path is None:
        _cache = doc
    return doc


def normalise(code):
    """Canonical diagnostic code. 'al0132', ' AL0132 ', 'error AL0132: x' → 'AL0132'.

    Consistent normalisation is an acceptance criterion because the same code arrives
    from three places — SARIF `ruleId`, compiler stdout, and hand-written config — in
    three shapes.
    """
    if not code:
        return ""
    m = _CODE_RE.search(str(code).upper())
    return m.group(1) if m else str(code).strip().upper()


def codes_in(text):
    """Every diagnostic code in a compiler log, in first-seen order."""
    seen, out = set(), []
    for m in _CODE_RE.finditer((text or "").upper()):
        if m.group(1) not in seen:
            seen.add(m.group(1))
            out.append(m.group(1))
    return out


def _applies(entry, bc_version):
    if bc_version is None:
        return True
    try:
        import al_temporal
        return al_temporal.applies(entry, bc_version)[0]
    except Exception:
        return True


def lookup(code, bc_version=None, path=None):
    """The KB entry for a diagnostic, or None. Version-filtered."""
    e = _load(path).get(normalise(code))
    if e and _applies(e, bc_version):
        return dict(e, code=normalise(code), _bc=bc_version)
    return None


def category(code, path=None):
    """Classification for error_profile.py. Unknown codes get no category rather than a
    guessed one."""
    e = _load(path).get(normalise(code))
    return (e or {}).get("category")


def codes_by_category(cat, path=None):
    return {c for c, e in _load(path).items() if (e or {}).get("category") == cat}


def known(path=None):
    return sorted(_load(path))


def _clean(text):
    return " ".join(str(text or "").split())


def guidance(entry, verbose=True):
    """One entry rendered for a fix prompt."""
    L = [f"### {entry['code']} — {_clean(entry.get('meaning'))}"]
    if entry.get("cause"):
        L.append(f"  cause: {_clean(entry['cause'])}")
    if verbose and entry.get("model_failure"):
        L.append(f"  why this loops: {_clean(entry['model_failure'])}")
    if entry.get("bad"):
        L.append("  WRONG:\n" + "\n".join(f"      {l}" for l in
                                          str(entry["bad"]).rstrip().splitlines()))
    if entry.get("good"):
        L.append("  RIGHT:\n" + "\n".join(f"      {l}" for l in
                                          str(entry["good"]).rstrip().splitlines()))
    if entry.get("fix"):
        L.append(f"  fix: {_clean(entry['fix'])}")
    if entry.get("evidence"):
        L.append(f"  evidence: {_clean(entry['evidence'])}")
    # A scoped entry that passes the filter silently reads as a universal rule. Say what
    # it is scoped to, at the point of use.
    try:
        import al_temporal
        note = al_temporal.scope_note(entry, entry.get("_bc"))
        if note:
            L.append(f"  applicability: {note}")
    except Exception:
        pass
    return "\n".join(L)


def context_for(build_text, bc_version=None, limit=4, path=None):
    """Targeted context for the diagnostics actually present in `build_text`.

    Deliberately capped: the value is in a handful of precise entries, and a wall of
    guidance is the thing that pushes the real compiler output out of the model's
    attention. Returns "" when nothing is known — silence beats padding.
    """
    hits = []
    for c in codes_in(build_text):
        e = lookup(c, bc_version, path)
        if e:
            hits.append(e)
        if len(hits) >= limit:
            break
    if not hits:
        return ""
    return ("\n\nDIAGNOSTIC KNOWLEDGE — background on the errors above. The compiler's own "
            "message is the authority; this only explains what usually causes it:\n"
            + "\n".join(guidance(e) for e in hits) + "\n")


def main():
    import argparse
    import json
    ap = argparse.ArgumentParser(prog="al_errors",
                                 description="what a recurring AL diagnostic really means")
    ap.add_argument("code", nargs="?", help="diagnostic code (omit to list)")
    ap.add_argument("--bc", type=int, help="BC major version")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--category")
    a = ap.parse_args()

    if a.category:
        print("\n".join(sorted(codes_by_category(a.category))))
        return 0
    if not a.code:
        db = _load()
        for c in known():
            print(f"  {c:<8} [{db[c].get('category',''):<9}] {_clean(db[c].get('meaning'))[:70]}")
        return 0
    e = lookup(a.code, a.bc)
    if not e:
        print(f"no entry for {normalise(a.code)}"
              + (f" at BC{a.bc}" if a.bc else "")
              + " — the compiler's own message is all there is.")
        return 1
    print(json.dumps(e, indent=2) if a.json else guidance(e))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
