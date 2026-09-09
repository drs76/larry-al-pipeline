"""anon_map.py — reversible token substitution engine (anon hook, phase 2).

Deterministic, stable, exactly-invertible substitution of a DECLARED set of
sensitive tokens for identifier-safe sentinels (ANON_NAME_001, ANON_HOST_002, …).
Real⇥placeholder pairs persist in a gitignored map file so the mapping is stable
across runs (multi-file consistency) and reversible:

    reverse(forward(text)) == text            # round-trip identity

Scope: declared literal reals (names, hosts, tenant IDs) + built-in structural
detectors (GUIDs, user paths). NOT for code identifiers / business logic — those
stay intact so fixes remain meaningful. Case-SENSITIVE by design (case-insensitive
matching would lose original case and break the inverse; declare case variants
explicitly). See tooling/anon-claude-hook.spec.md §5.
"""
import os
import re

# Identifier-safe sentinel: fixed prefix + category + zero-padded index. Reverse
# always runs longest-placeholder-first so ANON_NAME_001 can't clobber a substring
# of ANON_NAME_0010, and \b anchors keep them from matching inside other words.
_SENTINEL = "ANON_{cat}_{n:03d}"

# Built-in structural detectors — each DISTINCT match is minted a reversible
# placeholder (unlike the legacy lossy `<guid>` collapse in anonymise.py).
DETECTORS = [
    ("GUID", re.compile(r'\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\b')),
    ("USERPATH", re.compile(r'/mnt/c/[Uu]sers/[^/\s"]+')),
    ("WINPATH", re.compile(r'C:\\Users\\[^\\\s"]+')),
    # Personal identifiers (enterprise ruling 2026-07-06: code may egress, identifiers may not).
    # Emails are the auto-detectable class; names/staff/tenants stay curated in names.tsv.
    ("EMAIL", re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b')),
]


def _esc(s):
    return s.replace("\\", "\\\\").replace("\t", "\\t").replace("\n", "\\n")


def _unesc(s):
    return re.sub(r'\\(.)', lambda m: {"t": "\t", "n": "\n", "\\": "\\"}.get(m.group(1), m.group(1)), s)


def _lit_pattern(real):
    """Literal match, word-boundary-anchored only where the edge is a word char
    (so short bare tokens like 'ACME' don't corrupt substrings, but punctuated
    reals like 'a@b.com' still match)."""
    esc = re.escape(real)
    left = r'\b' if real[:1].isalnum() or real[:1] == '_' else ''
    right = r'\b' if real[-1:].isalnum() or real[-1:] == '_' else ''
    return left + esc + right


class AnonMap:
    """Bidirectional, append-only real⇄placeholder store."""

    def __init__(self):
        self.fwd = {}       # (category, real) -> placeholder
        self.rev = {}       # placeholder -> real
        self._counts = {}   # category -> highest index minted

    def load(self, path):
        if not path or not os.path.exists(path):
            return self
        with open(path, encoding="utf-8") as f:
            for ln in f:
                ln = ln.rstrip("\n")
                if not ln.strip() or ln.lstrip().startswith("#"):
                    continue
                parts = ln.split("\t")
                if len(parts) < 3:
                    continue
                ph, cat, real = parts[0], parts[1], _unesc("\t".join(parts[2:]))
                self.fwd[(cat, real)] = ph
                self.rev[ph] = real
                m = re.match(rf"ANON_{re.escape(cat)}_(\d+)$", ph)
                if m:
                    self._counts[cat] = max(self._counts.get(cat, 0), int(m.group(1)))
        return self

    def save(self, path):
        d = os.path.dirname(path)
        if d:
            os.makedirs(d, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write("# anon map — placeholder<TAB>category<TAB>real   GITIGNORED, DO NOT COMMIT\n")
            for ph in sorted(self.rev):
                cat = ph.split("_")[1]
                f.write(f"{ph}\t{cat}\t{_esc(self.rev[ph])}\n")

    def placeholder_for(self, real, category):
        """Stable placeholder for a real (mint on first sight)."""
        key = (category, real)
        if key in self.fwd:
            return self.fwd[key]
        n = self._counts.get(category, 0) + 1
        self._counts[category] = n
        ph = _SENTINEL.format(cat=category, n=n)
        self.fwd[key] = ph
        self.rev[ph] = real
        return ph


def forward(text, amap, literals=(), detectors=DETECTORS):
    """Scrub declared reals → placeholders (mutating `amap`). `literals` = iterable
    of (category, real). Longest reals first so 'Acme Trading' maps before 'Acme'."""
    for cat, real in sorted(literals, key=lambda cr: len(cr[1]), reverse=True):
        if not real:
            continue
        ph = amap.placeholder_for(real, cat)
        text = re.sub(_lit_pattern(real), lambda m, p=ph: p, text)
    for cat, rx in detectors:
        text = rx.sub(lambda m, c=cat: amap.placeholder_for(m.group(0), c), text)
    return text


def reverse(text, amap):
    """Restore placeholders → reals. Longest-placeholder-first = inverse-safe."""
    for ph in sorted(amap.rev, key=len, reverse=True):
        text = re.sub(rf'\b{re.escape(ph)}\b', lambda m, r=amap.rev[ph]: r, text)
    return text


def residual_reals(text, amap):
    """Reals from the map still present in `text` — the no-leak assertion (§9).
    Returns the list of leaked reals (empty = clean)."""
    leaked = []
    for (_cat, real), _ph in amap.fwd.items():
        if real and re.search(_lit_pattern(real), text):
            leaked.append(real)
    return leaked


def load_names(path):
    """Curated literals file: `CATEGORY<TAB>real` per line. Returns [(cat, real)]."""
    out = []
    if not path or not os.path.exists(path):
        return out
    with open(path, encoding="utf-8") as f:
        for ln in f:
            ln = ln.rstrip("\n")
            if not ln.strip() or ln.lstrip().startswith("#") or "\t" not in ln:
                continue
            cat, real = ln.split("\t", 1)
            out.append((cat.strip(), real))
    return out
