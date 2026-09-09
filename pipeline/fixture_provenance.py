"""Which fixture revision produced this result?

The benchmark fixtures live in `/mnt/rojaws/localDev/projects/`, which became a git repo
on 2026-08-22. Before that, a handover could change with no record, and a pass rate could
not be tied to the input text that produced it — p1's enum defect sat unnoticed across ten
runs partly for that reason.

Putting the fixtures under git only helps if that identity reaches the RESULT. This
records it, so any receipt or metrics row can name the exact input state it ran against.

WHY BOTH A COMMIT AND A HASH
----------------------------
`fixture_commit` says which tracked revision the fixture directory was at.
`handover_sha256` says what the handover actually CONTAINED — which still moves when the
file is edited but not yet committed, and which is the thing a model actually consumed.
A commit alone would silently describe uncommitted edits as the committed revision, so
`fixture_dirty` is recorded too.

READING ROWS WRITTEN BEFORE 6ebfb90 (2026-09-01)
------------------------------------------------
`fixture_commit` in those rows is the REPOSITORY HEAD, not the fixture revision. It was
`rev-parse --short HEAD`, so every fixture in the corpus reported the same value.

  Equality of that field does NOT establish fixture identity.

Two pre-6ebfb90 rows sharing a fixture_commit is evidence they ran at the same repo state,
which is a different and much weaker claim. Those rows are not invalid — their repository
provenance is perfectly good — they simply do not answer the question this field's name
implies. Do not pool them with post-6ebfb90 rows on fixture_commit equality.

RUN DIRECTORY vs FIXTURE
------------------------
`bench-run-suite.sh` copies the handover into a run directory and rewrites the absolute
paths inside it to point at that run. So the run copy NEVER hashes equal to the fixture's,
even when nothing changed. Both are therefore recorded separately:

  handover_sha256          the handover as used by this run (path-rewritten)
  fixture_handover_sha256  the fixture's original, comparable ACROSS runs

Compare the fixture hash between suites; the local hash only proves what this run saw.

The fixture directory is passed by the suite as FIXTURE_DIR. Standalone builds have no
fixture, so every field is optional and absence is recorded as None rather than guessed.
"""
import hashlib
import os
import subprocess


def _sha256(path):
    try:
        h = hashlib.sha256()
        with open(path, "rb") as fh:
            for chunk in iter(lambda: fh.read(65536), b""):
                h.update(chunk)
        return h.hexdigest()
    except OSError:
        return None


def _git(args, cwd):
    try:
        r = subprocess.run(["git"] + args, cwd=cwd, capture_output=True,
                           text=True, timeout=10)
        return r.stdout.strip() if r.returncode == 0 else None
    except Exception:
        return None


def collect(project_root, fixture_dir=None):
    """Provenance for one run. Never raises — a missing field is None, not a guess."""
    fixture_dir = fixture_dir or os.environ.get("FIXTURE_DIR") or None
    out = {
        # Explicit marker. Rows written BEFORE provenance existed have no such key at
        # all, and classify() turns that absence into "legacy_missing" rather than
        # letting null fields be grouped or filtered as if they were data.
        "provenance": "tracked" if fixture_dir else "no_fixture",
        "fixture": os.path.basename(fixture_dir.rstrip("/")) if fixture_dir else None,
        "fixture_commit": None,
        "fixture_dirty": None,
        "fixture_handover_sha256": None,
        "handover_sha256": _sha256(os.path.join(project_root,
                                                "larry-handover.prompt.md")),
    }
    if not fixture_dir or not os.path.isdir(fixture_dir):
        return out

    out["fixture_handover_sha256"] = _sha256(
        os.path.join(fixture_dir, "larry-handover.prompt.md"))
    # The LAST COMMIT THAT TOUCHED THIS FIXTURE — not the repo's HEAD.
    #
    # This used to be `rev-parse --short HEAD`, which answers "what was the repo at?" and
    # not "which fixture revision produced this result?" — the question this module's own
    # docstring says it answers. Every fixture in the repo reported the same value, so two
    # runs of an UNCHANGED p1 months apart got different fixture_commits because somebody
    # edited doclink in between. Demonstrated 2026-09-01: all four fixtures reported
    # 3240e31 while their real identities were 36656d5, a00035f, 3240e31 and 167b68a.
    #
    # The `dirty` check below was already scoped with `-- .`; the commit was not. Same
    # principle, applied consistently.
    rev = _git(["log", "-1", "--format=%h", "--", "."], fixture_dir)
    if rev:
        out["fixture_commit"] = rev
        # Only the fixture's OWN tracked files matter. A dirty flag driven by some other
        # fixture in the same repo would be noise on every run.
        status = _git(["status", "--porcelain", "--", "."], fixture_dir)
        out["fixture_dirty"] = bool(status) if status is not None else None
    # Repo HEAD kept as separate CONTEXT, under an honest name. It is genuinely useful
    # (which overall corpus state was this?) and losing it would trade one gap for another
    # — but it is not the fixture's identity and must not be read as one.
    head = _git(["rev-parse", "--short", "HEAD"], fixture_dir)
    if head:
        out["projects_commit"] = head
    return out


# --- analysis-side guard -------------------------------------------------------------

LEGACY = "legacy_missing"


def classify(row):
    """How trustworthy is this row's fixture identity?

      tracked         fixture dir known; commit and hashes recorded
      no_fixture      standalone build, never had a fixture (not a defect)
      legacy_missing  written before provenance existed - the fixture revision is
                      UNKNOWABLE from the row itself

    Every metrics row and receipt written before pipeline commit a8048af is
    `legacy_missing`. That includes all of the incrab/incrab2, ndb1 and capability-trigger
    evidence. Those rows can be attributed by date against
    setup/reference/fixture-handover-revisions.md, but not automatically, and p1's rows in
    particular span the v1->v2 handover repair.

    DO NOT pool legacy_missing rows with tracked rows in a pass-rate comparison without
    saying so. A null fixture_commit is not "the same fixture" — it is "no evidence".
    """
    if not isinstance(row, dict):
        return LEGACY
    if "provenance" in row:
        return row.get("provenance") or LEGACY
    # Rows written between the provenance fields landing and this marker landing carry a
    # real fixture_commit but no marker. Credit them rather than discarding real evidence.
    if row.get("fixture_commit"):
        return "tracked"
    return LEGACY


def split_by_provenance(rows):
    """Partition rows so an analysis has to look at the legacy count before pooling."""
    out = {"tracked": [], "no_fixture": [], LEGACY: []}
    for r in rows:
        out.setdefault(classify(r), []).append(r)
    return out
