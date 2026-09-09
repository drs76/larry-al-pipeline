#!/usr/bin/env python3
"""
error_profile — what actually fails in AL builds, measured across build logs.

Written after grounding was aimed at the wrong target: one log showed AL0185 x21
("Table X is missing"), which read like platform API hallucination, so two rounds of
retrieval tooling were built for it. A wider count showed doc-link's failures are
mostly the model contradicting objects IT had just written — which no amount of
platform lookup can fix. Measure first.

Each diagnostic is bucketed by what would actually fix it:

  platform-name   references a real BC object/member it got wrong  -> symbol grounding
  invented-name   references something that exists nowhere         -> "does not exist" hint
  project-own     contradicts an object THIS project declares      -> ground on own source
  al-rule         syntax/attribute/signature rules, no name at all -> prompt or reference
  manifest        missing/unspecced files                          -> recovery step
  other

"project-own" vs "platform" is decided by the project's own manifest, not by guessing:
a name the handover says this project creates is its own, anything else is looked up in
the downloaded symbols.

  error_profile.py <log-or-dir> [more...]
"""
import os, re, sys, json, glob, collections

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

ERR = re.compile(r"error ([A-Z]{2,3}\d+): (.*)")
NAME_IN_MSG = [
    re.compile(r"(?:Table|Enum|Codeunit|Page|Report|Query|Interface|XmlPort) '([^']+)' is missing"),
    re.compile(r"'(?:Record|Codeunit|Page|Report|Enum|Query|Table)?\s*\"?([^'\"]+?)\"?'\s*does not contain a definition"),
    re.compile(r"The name '\"?([^'\"]+?)\"?' does not exist"),
    re.compile(r"'([^']+)' is not found in the target"),
]
RULE_CODES = {"AL0774", "AL0242", "AL0244", "AL0104", "AL0114", "AL0198", "AL0009",
              "AL0128", "AL0227", "AL0519", "AL0195", "PTE0004", "PTE0005", "PTE0008",
              "AL0666", "AL1053", "AL0124",
              # found hiding in 'other' — all "you used the language wrong", not names
              "AL0282", "AL0162", "AL0156", "AL0296", "AL0286", "AL0161", "AL0205"}
# the model declared the same object/ID twice — an internal consistency fault
DUPLICATE_CODES = {"AL0264", "AL0197", "AL0263"}
# type/conversion/enum-value misuse: neither a missing name nor a syntax rule
TYPE_CODES = {"AL0133", "AL0122", "AL0175", "AL0169", "AL0139", "AL0257"}

# AL-12: al-errors.yml states a category for every diagnostic it documents, so the file
# that explains a code also decides how it is counted. UNION, never replacement — these
# literal sets carry codes the KB has no entry for yet, and dropping them would silently
# reclassify half the corpus as "other".
try:
    import al_errors
    RULE_CODES |= (al_errors.codes_by_category("rules")
                   | al_errors.codes_by_category("syntax")
                   | al_errors.codes_by_category("events"))
    DUPLICATE_CODES |= al_errors.codes_by_category("duplicate")
    TYPE_CODES |= al_errors.codes_by_category("types")
    # `symbols` is deliberately absent: those are recognised by NAME_IN_MSG above, which
    # extracts the offending NAME rather than just bucketing the code.
except Exception:
    pass


def project_objects(project_root):
    """Object names this project declares — from its own written .al, which is the
    ground truth for 'own vs platform'."""
    names = set()
    for f in glob.glob(os.path.join(project_root, "src", "**", "*.al"), recursive=True):
        try:
            src = open(f, encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        for m in re.finditer(r"^\s*(?:table|tableextension|page|pageextension|codeunit|enum|"
                             r"enumextension|report|query|interface|permissionset|controladdin)"
                             r"\s+\d*\s*\"?([^\"\n{]+?)\"?\s*(?:extends|\{|$)", src, re.M | re.I):
            names.add(m.group(1).strip().lower())
    return names


def classify(log_path, sym_idx, own):
    counts = collections.Counter()
    examples = {}
    seen = set()
    try:
        text = open(log_path, encoding="utf-8", errors="replace").read()
    except OSError:
        return counts, examples
    for m in ERR.finditer(text):
        code, msg = m.group(1), m.group(2).strip()
        key = (code, msg[:80])
        if key in seen:          # the same error repeats every fix round
            continue
        seen.add(key)
        if "MISSING:" in msg or "UNSPECCED" in msg:
            bucket = "manifest"
        else:
            name = None
            for p in NAME_IN_MSG:
                g = p.search(msg)
                if g:
                    name = g.group(1).split(".")[-1].strip().strip('"')
                    break
            if code in DUPLICATE_CODES:
                bucket = "project-own"
            elif code in TYPE_CODES:
                bucket = "type-semantics"
            elif not name:
                bucket = "al-rule" if code in RULE_CODES else "other"
            elif name.lower() in own:
                bucket = "project-own"
            elif sym_idx and name.lower() in sym_idx:
                bucket = "platform-name"
            else:
                bucket = "invented-name"
        counts[bucket] += 1
        examples.setdefault(bucket, f"{code}: {msg[:88]}")
    return counts, examples


def main():
    args = sys.argv[1:] or ["/mnt/rojaws/localDev/projects/bench/logs"]
    logs = []
    for a in args:
        logs += sorted(glob.glob(os.path.join(a, "*.log"))) if os.path.isdir(a) else [a]
    runs = "/mnt/rojaws/localDev/projects/bench/runs"
    try:
        import al_symbols
        pkg = glob.glob(os.path.join(runs, "*", ".alpackages"))
        sym = al_symbols.build_index(pkg[0]) if pkg else {}
    except Exception:
        sym = {}
    print(f"  symbol index: {len(sym)} objects\n")

    per_fixture = collections.defaultdict(collections.Counter)
    all_ex = {}
    for lg in logs:
        base = os.path.basename(lg)[:-4]
        fx = ("P1" if "p1-crud" in base else "P4" if "p4-unseen" in base
              else "map" if "map-integration" in base else "doc-link" if "document-link" in base
              else "other")
        own = project_objects(os.path.join(runs, base))
        c, ex = classify(lg, sym, own)
        per_fixture[fx].update(c)
        for k, v in ex.items():
            all_ex.setdefault(k, v)

    order = ["al-rule", "type-semantics", "project-own", "invented-name", "platform-name", "manifest", "other"]
    fixtures = [f for f in ("P1", "P4", "map", "doc-link", "other") if per_fixture.get(f)]
    print(f"  {'bucket':<15}" + "".join(f"{f:>10}" for f in fixtures) + f"{'TOTAL':>10}")
    tot = collections.Counter()
    for b in order:
        row = [per_fixture[f][b] for f in fixtures]
        if not sum(row):
            continue
        tot[b] = sum(row)
        print(f"  {b:<15}" + "".join(f"{v:>10}" for v in row) + f"{sum(row):>10}")
    grand = sum(tot.values()) or 1
    print(f"\n  share of distinct diagnostics:")
    for b, n in tot.most_common():
        print(f"    {b:<15} {100*n/grand:5.1f}%   e.g. {all_ex.get(b,'')[:70]}")


if __name__ == "__main__":
    sys.exit(main())
