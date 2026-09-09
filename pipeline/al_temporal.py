"""al_temporal — when a piece of AL knowledge is true, and saying so out loud.

AL knowledge has a shelf life. `SetLoadFields` did not exist before BC17, `Extensible` on
an enum arrived later still, and an obsoleted API keeps compiling right up to the release
that removes it. A ruleset that presents all of this as timeless is wrong twice over: it
recommends things a BC14 target cannot use, and it stays silent about the ones that are
on their way out.

Two jobs, and the second is the one that was missing.

**Filtering** — decide whether an item applies to a target. `bcquality` already did a
version check; this generalises it to introduced/removed/deprecated and to runtime
versions, and it accepts the range forms already written across the KBs (`[all]`,
`[26, 27]`, `[16..]`, `[26..28]`) so nothing has to be rewritten to benefit.

**Labelling** — when a version-scoped item DOES apply, say what it is scoped to. Silently
passing the filter presents a conditional rule as a universal one, which is the exact
failure the handover names. A rule that reads "always use X" when it means "use X from
BC24" will be applied to a BC14 project by whoever reads it next.

Deprecation is deliberately not a filter. Something deprecated still works, and hiding it
would leave a coder using it with no warning; it applies, and it carries a warning.

`confidence` and `source` travel with every item because provenance decides how hard to
lean on it — "verified by a compiler probe on BC27" and "seen in a blog post" are not the
same claim, and the pipeline has already been burned by treating one as the other.
"""
from __future__ import annotations

import re

CONFIDENCE = ("verified", "high", "medium", "low")
_DEFAULT_CONFIDENCE = "medium"

# The temporal fields, plus the legacy range field they generalise.
FIELDS = ("introduced_bc", "removed_bc", "deprecated_bc", "runtime_from", "runtime_to",
          "source", "confidence", "bc-version")


def _major(v):
    """Leading integer of a version. '27.5.46862' -> 27, 'BC24' -> 24, None -> None."""
    if v is None or isinstance(v, bool):
        return None
    m = re.search(r"\d+", str(v))
    return int(m.group(0)) if m else None


def _float(v):
    try:
        return float(str(v).strip())
    except (TypeError, ValueError):
        return None


def meta_of(item):
    """Temporal metadata out of any knowledge item (frontmatter dict, YAML entry, ...).

    Unknown keys are ignored rather than rejected: these fields are being added to KBs
    that already exist, and an item with none of them is not an error — it is an item
    nobody has dated yet.
    """
    item = item or {}
    out = {k: item.get(k) for k in FIELDS if item.get(k) is not None}
    out.setdefault("confidence", _DEFAULT_CONFIDENCE)
    return out


def _range_matches(spec, target):
    """The legacy `bc-version:` forms: [all] | [26, 27] | [16..] | [26..28]."""
    if target is None:
        return True
    for raw in (spec if isinstance(spec, (list, tuple)) else [spec]):
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
                return True          # a frontmatter typo must not delete a real rule
        else:
            try:
                if int(tok) == target:
                    return True
            except ValueError:
                return True
    return False


def applies(item, bc_version=None, runtime=None):
    """(ok, reason). ok=False means this item is not true for that target.

    Deprecation never makes ok False — deprecated code still runs, and suppressing the
    item would remove the only warning the reader was going to get.
    """
    m = meta_of(item)
    bc = _major(bc_version)

    if "bc-version" in m and not _range_matches(m["bc-version"], bc):
        return False, f"scoped to BC {m['bc-version']}, target is BC {bc}"

    intro = _major(m.get("introduced_bc"))
    if bc is not None and intro is not None and bc < intro:
        return False, f"introduced in BC{intro}; target is BC{bc}"

    removed = _major(m.get("removed_bc"))
    if bc is not None and removed is not None and bc >= removed:
        return False, f"removed in BC{removed}; target is BC{bc}"

    rt = _float(runtime)
    rt_from, rt_to = _float(m.get("runtime_from")), _float(m.get("runtime_to"))
    if rt is not None and rt_from is not None and rt < rt_from:
        return False, f"needs runtime {rt_from}+; target runtime is {rt}"
    if rt is not None and rt_to is not None and rt > rt_to:
        return False, f"withdrawn after runtime {rt_to}; target runtime is {rt}"

    return True, "applies"


def is_deprecated(item, bc_version=None):
    bc, dep = _major(bc_version), _major(meta_of(item).get("deprecated_bc"))
    return dep is not None and (bc is None or bc >= dep)


def scope_note(item, bc_version=None):
    """The sentence a version-scoped item must be presented WITH. "" when it is genuinely
    universal.

    This is the point of the module. Passing the filter silently turns a conditional rule
    into an unconditional one in the reader's mind, and the next person applies it to a
    project it was never true for.
    """
    m = meta_of(item)
    bits = []
    intro = _major(m.get("introduced_bc"))
    removed = _major(m.get("removed_bc"))
    dep = _major(m.get("deprecated_bc"))
    if intro and removed:
        bits.append(f"BC{intro}–BC{removed - 1} only")
    elif intro:
        bits.append(f"BC{intro} and later only")
    elif removed:
        bits.append(f"removed in BC{removed}")
    elif "bc-version" in m:
        # Render the legacy range forms as prose. "applies to BC 24.." is the kind of
        # label a reader skips; "BC24 and later only" is the kind they act on.
        spec = m["bc-version"]
        flat = [str(x).strip() for x in (spec if isinstance(spec, (list, tuple)) else [spec])]
        flat = [f for f in flat if f.lower() != "all"]
        parts = []
        for f in flat:
            if f.endswith(".."):
                parts.append(f"BC{f[:-2]} and later only")
            elif ".." in f:
                lo, _, hi = f.partition("..")
                parts.append(f"BC{lo}–BC{hi} only")
            else:
                parts.append(f"BC{f}")
        if parts:
            bits.append(parts[0] if len(parts) == 1
                        else "applies to " + ", ".join(parts))
    if dep:
        bits.append(f"DEPRECATED from BC{dep} — still compiles, but plan to move off it")
    rt_from, rt_to = m.get("runtime_from"), m.get("runtime_to")
    if rt_from:
        bits.append(f"runtime {rt_from}+")
    if rt_to:
        bits.append(f"up to runtime {rt_to}")
    # Only a DECLARED confidence is worth printing. Emitting the default on every item
    # adds a line to everything and therefore means nothing.
    declared = (item or {}).get("confidence")
    if declared and str(declared).lower() in ("low", "medium"):
        src = m.get("source")
        bits.append(f"confidence {declared}" + (f", source: {src}" if src else ""))
    return "; ".join(bits)


def annotate(text, item, bc_version=None):
    """Attach the scope note to a rendered item. No note, no change."""
    note = scope_note(item, bc_version)
    return f"{text}\n  [applicability: {note}]" if note else text


def select(items, bc_version=None, runtime=None, min_confidence=None, key=None):
    """Filter a list of knowledge items, returning (kept, dropped_with_reasons).

    Dropped items come back WITH their reason rather than vanishing: "no rules matched"
    and "eleven rules were filtered out by a version you may have set wrong" look
    identical from the outside otherwise.
    """
    kept, dropped = [], []
    floor = CONFIDENCE.index(min_confidence) if min_confidence in CONFIDENCE else None
    for it in items or []:
        meta = key(it) if key else it
        ok, why = applies(meta, bc_version, runtime)
        if ok and floor is not None:
            # Only a DECLARED confidence can be filtered on. Almost nothing in the
            # existing KBs states one, so treating absence as "medium" would delete the
            # entire corpus the moment somebody set a floor — the same reasoning that
            # makes a frontmatter typo admit a rule rather than drop it.
            declared = str((meta or {}).get("confidence", "")).lower()
            if declared in CONFIDENCE and CONFIDENCE.index(declared) > floor:
                ok, why = False, f"confidence {declared} is below {min_confidence}"
        (kept if ok else dropped).append(it if ok else (it, why))
    return kept, dropped


def parse_frontmatter(text):
    """YAML frontmatter of a markdown knowledge file, as a dict. {} when there is none."""
    if not text or not text.lstrip().startswith("---"):
        return {}
    body = text.lstrip()[3:]
    end = body.find("\n---")
    if end < 0:
        return {}
    try:
        import yaml
        return yaml.safe_load(body[:end]) or {}
    except Exception:
        return {}


def main():
    import argparse
    import json
    ap = argparse.ArgumentParser(
        prog="al_temporal", description="is this knowledge true for that target?")
    ap.add_argument("file", nargs="?", help="markdown knowledge file with frontmatter")
    ap.add_argument("--bc", type=int)
    ap.add_argument("--runtime")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    if not a.file:
        ap.print_help()
        return 2
    meta = parse_frontmatter(open(a.file, encoding="utf-8-sig").read())
    ok, why = applies(meta, a.bc, a.runtime)
    note = scope_note(meta, a.bc)
    if a.json:
        print(json.dumps({"applies": ok, "reason": why, "scope_note": note,
                          "meta": meta_of(meta)}, indent=2, default=str))
    else:
        print(f"{'APPLIES' if ok else 'DOES NOT APPLY'} — {why}")
        if note:
            print(f"  applicability: {note}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
