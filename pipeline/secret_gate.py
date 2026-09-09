"""secret_gate.py — one-way secret redaction + fail-closed gate (anon hook, phase 3).

Secrets are NOT reversible tokens: they are scrubbed to an inert dummy and NEVER
restored. On a HIGH-confidence secret the gate fails closed — the escalation aborts
unless explicitly overridden — because a credential should be removed from the repo,
not shipped to a cloud LLM even redacted.

  gate(text)            -> (ok, redacted_text, findings)   ok=False if any high finding
  scan(text)            -> findings                        (the pre-network no-leak check)

MED-confidence hits (generic `password=`/`token=` assignments) are redacted but do NOT
block — they false-positive on config placeholders too often to be fatal. HIGH hits are
provider-shaped credentials with low false-positive rates. See anon-claude-hook.spec.md §6.
"""
import re

DUMMY = "REDACTED_SECRET"

# (name, confidence, compiled regex, group)  — group 0 = whole match, N = redact that group only.
PATTERNS = [
    ("private-key", "high", re.compile(
        r'-----BEGIN (?:RSA |EC |OPENSSH |DSA |PGP )?PRIVATE KEY-----.*?'
        r'-----END (?:RSA |EC |OPENSSH |DSA |PGP )?PRIVATE KEY-----', re.S), 0),
    ("anthropic-api-key", "high", re.compile(r'\bsk-ant-[A-Za-z0-9_\-]{20,}\b'), 0),
    ("openai-api-key", "high", re.compile(r'\bsk-(?:proj-)?[A-Za-z0-9_\-]{32,}\b'), 0),
    ("aws-access-key", "high", re.compile(r'\bAKIA[0-9A-Z]{16}\b'), 0),
    ("gcp-api-key", "high", re.compile(r'\bAIza[0-9A-Za-z_\-]{35}\b'), 0),
    ("github-token", "high", re.compile(r'\b(?:ghp|gho|ghu|ghs|ghr)_[0-9A-Za-z]{36}\b'), 0),
    ("github-pat", "high", re.compile(r'\bgithub_pat_[0-9A-Za-z_]{22,}\b'), 0),
    ("slack-token", "high", re.compile(r'\bxox[baprs]-[0-9A-Za-z-]{10,}\b'), 0),
    ("azure-storage-key", "high", re.compile(r'(?i)AccountKey=([A-Za-z0-9+/=]{40,})'), 1),
    ("jwt", "high", re.compile(r'\beyJ[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\b'), 0),
    ("db-password", "high", re.compile(r'(?i)(?:password|pwd)=([^;\s"\']{6,})'), 1),
    ("bearer-token", "med", re.compile(r'(?i)bearer\s+([A-Za-z0-9._\-]{20,})'), 1),
    ("secret-assignment", "med", re.compile(
        r'(?i)(?:secret|token|api[_-]?key|access[_-]?key|client[_-]?secret|passwd)'
        r'\s*[=:]\s*["\']?([A-Za-z0-9+/_\-]{16,})["\']?'), 1),
]


def _mask(s):
    """Short, safe preview — never echo a full secret."""
    s = s.replace("\n", " ")
    return (s[:4] + "…" + s[-2:]) if len(s) > 8 else "…"


def scan(text):
    """All secret findings: [{name, confidence, preview}]. Empty = clean."""
    out = []
    for name, conf, rx, grp in PATTERNS:
        for m in rx.finditer(text):
            val = m.group(grp)
            if val and val != DUMMY:      # already-redacted dummy is not a finding
                out.append({"name": name, "confidence": conf, "preview": _mask(val)})
    return out


def redact(text):
    """Replace secret spans with DUMMY. Returns (redacted_text, findings)."""
    spans = []
    for name, conf, rx, grp in PATTERNS:
        for m in rx.finditer(text):
            val = m.group(grp)
            if val is None or val == DUMMY:      # idempotent: don't re-redact the dummy
                continue
            s, e = m.span(grp)
            spans.append((s, e, name, conf, _mask(val)))
    # de-overlap: keep the earliest span, drop anything intersecting it
    spans.sort()
    merged, last_e = [], -1
    for s, e, name, conf, prev in spans:
        if s < last_e:
            continue
        merged.append((s, e, name, conf, prev))
        last_e = e
    findings = [{"name": n, "confidence": c, "preview": p} for _s, _e, n, c, p in merged]
    for s, e, *_ in sorted(merged, reverse=True):
        text = text[:s] + DUMMY + text[e:]
    return text, findings


def gate(text, allow_high=False):
    """(ok, redacted_text, findings). ok=False if any HIGH finding and not overridden."""
    redacted, findings = redact(text)
    high = [f for f in findings if f["confidence"] == "high"]
    return (allow_high or not high), redacted, findings
