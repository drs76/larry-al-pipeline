"""Security/integrity regression suite — one test per confirmed review finding.

Companion to the focused suites: test_egress_midtier.py (T1 policy matrix) and
test_rollback.py (T5). This covers the findings that had no test of their own —
filesystem containment (T2), mirror symlinks (T3), referee completeness (T4), reviewer
independence (T7) and promotion receipts (T8).

Every test here must FAIL against the pre-fix code. A test that passes either way is
worse than no test: it looks like coverage while guarding nothing.

Run: python3 test_pipeline_security.py
"""
import importlib.util
import json
import os
import shutil
import subprocess
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))


def _load(name, fn):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fn))
    mod = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)
    except SystemExit:
        pass
    return mod


pathguard = _load("pathguard", "pathguard.py")
snippet_fix = _load("snippet_fix", "snippet_fix.py")
anon_workspace = _load("anon_workspace", "anon_workspace.py")
build_receipt = _load("build_receipt", "build_receipt.py")
rb = _load("rb", "run-build.py")


SKIPPED = []


def _try_symlink(target, link):
    """Create a symlink, or report loudly that we could not.

    Windows needs SeCreateSymbolicLinkPrivilege — admin or Developer Mode — and without it
    os.symlink raises OSError WinError 1314. Reported from the Windows client 2026-09-01,
    where it crashed the whole suite.

    Skipping the SYMLINK LEG only, never the whole test: traversal, absolute paths, tilde
    and empty-string containment are portable and are the majority of what these tests
    guard. A skip that quietly drops real coverage is the failure mode this file exists to
    prevent, so it goes on the ledger and gets printed under the pass count.
    """
    try:
        os.symlink(target, link)
        return True
    except (OSError, NotImplementedError) as e:
        SKIPPED.append(f"symlink leg: {type(e).__name__}: {e}")
        return False


# ─── T2: filesystem containment ────────────────────────────────────────────────

def test_containment_rejects_traversal_absolute_and_symlink():
    d = tempfile.mkdtemp()
    try:
        os.makedirs(os.path.join(d, "src"))
        linked = _try_symlink("/tmp", os.path.join(d, "out"))   # link pointing outside
        rels = ["../../x.txt", "/tmp/x.txt", "a/b/../../../../x", "~/x", ""]
        if linked:
            rels.append("out/x.txt")
        for rel in rels:
            assert not pathguard.is_safe(d, rel), f"should reject: {rel!r}"
        assert pathguard.is_safe(d, "src/ok.al")
        assert pathguard.is_safe(d, "src/../src/ok.al")     # normalises back inside
    finally:
        shutil.rmtree(d)


def test_edit_blocks_cannot_write_outside_the_project():
    """The end-to-end version: real SEARCH/REPLACE blocks naming outside targets."""
    d = tempfile.mkdtemp()
    victim = os.path.join(tempfile.mkdtemp(), "victim.txt")
    try:
        os.makedirs(os.path.join(d, "src"))
        open(os.path.join(d, "src", "a.al"), "w").write("hello\n")
        open(victim, "w").write("UNTOUCHED\n")
        blocks = (f"FILE: src/a.al\n<<<<<<< SEARCH\nhello\n=======\nbye\n>>>>>>> REPLACE\n\n"
                  f"FILE: {victim}\n<<<<<<< SEARCH\nUNTOUCHED\n=======\nPWNED\n>>>>>>> REPLACE\n\n"
                  f"FILE: ../../escape.txt\n<<<<<<< SEARCH\nx\n=======\ny\n>>>>>>> REPLACE\n")
        applied, failed, details = snippet_fix.apply_edit_blocks(blocks, d)
        assert applied == 1, f"the legit edit must still apply: {details}"
        assert failed == 2, f"both escapes must be rejected: {details}"
        assert open(victim).read().strip() == "UNTOUCHED", "wrote outside the project!"
        assert "bye" in open(os.path.join(d, "src", "a.al")).read()
    finally:
        shutil.rmtree(d, ignore_errors=True)


# ─── T3: anonymised mirror must not follow symlinks ────────────────────────────

def test_mirror_aborts_on_tracked_symlink():
    repo = tempfile.mkdtemp()
    secret = os.path.join(tempfile.mkdtemp(), "private.txt")
    mirror = tempfile.mkdtemp()
    try:
        open(secret, "w").write("PRIVATE PAYLOAD\n")
        open(os.path.join(repo, "safe.txt"), "w").write("safe\n")
        if not _try_symlink(secret, os.path.join(repo, "link.txt")):
            return          # nothing to assert without a tracked symlink; on the ledger
        for cmd in (["git", "init", "-q", "."], ["git", "add", "-A"],
                    ["git", "-c", "user.email=t@t", "-c", "user.name=t",
                     "commit", "-qm", "init"]):
            subprocess.run(cmd, cwd=repo, capture_output=True)
        import anon_map
        try:
            anon_workspace.build_mirror(repo, anon_map.AnonMap(), [], mirror)
            raise AssertionError("mirror completed — it must abort on a tracked symlink")
        except anon_workspace.SymlinkAbort:
            pass
        leaked = any("PRIVATE PAYLOAD" in open(os.path.join(dp, f)).read()
                     for dp, _, fs in os.walk(mirror) for f in fs)
        assert not leaked, "external file content reached the scrubbed mirror"
    finally:
        for p in (repo, mirror):
            shutil.rmtree(p, ignore_errors=True)


# ─── T4: referee completeness ──────────────────────────────────────────────────

def test_analyzer_resolution_survives_a_target_framework_change():
    """The glob used to hard-code net10.0/any. Correct today, and silently wrong the day
    the AL tool ships a different TFM — which, because the referee fails closed, presents
    as "REFEREE UNAVAILABLE" on a box where the analyzers are plainly installed."""
    import glob as _g
    real = _g.glob
    try:
        _g.glob = lambda pat, recursive=False: [
            h for h in real(pat, recursive=recursive) if "/net10.0/" not in h]
        rb._analyzer_dir_cache = None
        d = rb._analyzer_dir()
        if d is None:
            return                      # no AL tool on this box; nothing to assert
        assert "/net10.0/" not in d, d
        assert rb.missing_analyzers() == [], "a present cop reported as missing"
    finally:
        _g.glob = real
        rb._analyzer_dir_cache = None


def test_analyzer_dlls_are_only_returned_when_they_exist():
    """A path per required cop was emitted whether or not the file was there, so a partial
    install produced an /analyzer: flag pointing at nothing and the compiler failed for a
    reason naming neither the cop nor the install."""
    if rb._analyzer_dir() is None:
        return
    for d in rb._analyzer_dlls():
        assert os.path.exists(d), d


def test_missing_analyzers_checks_by_name_not_by_position():
    """_analyzer_dlls() now returns only files that exist, so zipping it against
    REQUIRED_ANALYZERS would pair the wrong name with the wrong path once one cop was
    absent — and report a present cop as missing."""
    real = rb._analyzer_dir
    try:
        rb._analyzer_dir = lambda: "/nonexistent-analyzer-dir"
        assert rb.missing_analyzers() == list(rb.REQUIRED_ANALYZERS)
        assert rb._analyzer_dlls() == []
    finally:
        rb._analyzer_dir = real


def test_missing_analyzer_is_reported_not_ignored():
    """missing_analyzers() is what makes the referee fail closed and marks the metrics
    bare_compile_only. If it silently returns [] the fail-open bug is back."""
    # Stubs _analyzer_dir, which is now the single resolution seam — missing_analyzers()
    # checks the directory by name rather than zipping against _analyzer_dlls().
    real = rb._analyzer_dir
    try:
        rb._analyzer_dir = lambda: None
        assert rb.missing_analyzers() == list(rb.REQUIRED_ANALYZERS)
        assert rb._analyzer_dlls() == []
    finally:
        rb._analyzer_dir = real


# ─── T7: reviewer independence ─────────────────────────────────────────────────

def test_same_model_is_not_independent():
    assert rb._same_model("ollama/qwen3-coder:30b", "ollama/qwen3-coder:30b")
    # provider prefix must not disguise the same model as a different one
    assert rb._same_model("ollama/qwen3-coder:30b", "qwen3-coder:30b")
    assert not rb._same_model("ollama/qwen3-coder:30b", "ollama/qwen2.5-coder:14b")


def test_reviewer_default_differs_from_coder():
    assert not rb._same_model(rb.CODER_MODEL, rb.REVIEW_MODEL_DEFAULT), (
        "the reviewer default must not be the coder model — that was the T7 defect")


# ─── T8: promotion receipts ────────────────────────────────────────────────────

def _project():
    d = tempfile.mkdtemp()
    os.makedirs(os.path.join(d, "src"))
    open(os.path.join(d, "src", "a.al"), "w").write("codeunit 1 X {}\n")
    return d


def test_promote_rejects_missing_receipt():
    d = _project()
    try:
        ok, why, _ = build_receipt.verify(d)
        assert not ok and "no build receipt" in why
    finally:
        shutil.rmtree(d)


def test_promote_rejects_tree_changed_after_build():
    d = _project()
    try:
        build_receipt.write(d, referee_ok=True, analyzers=["CodeCop"])
        assert build_receipt.verify(d)[0], "unmodified tree should verify"
        open(os.path.join(d, "src", "a.al"), "a").write("// edited\n")
        ok, why, _ = build_receipt.verify(d)
        assert not ok and "changed" in why
    finally:
        shutil.rmtree(d)


def test_promote_rejects_bare_compile_result():
    d = _project()
    try:
        build_receipt.write(d, referee_ok=True, analyzers=["CodeCop"],
                            bare_compile_only=True)
        ok, why, _ = build_receipt.verify(d)
        assert not ok and "bare-compile-only" in why
    finally:
        shutil.rmtree(d)


def test_promote_rejects_non_independent_review_when_required():
    d = _project()
    try:
        build_receipt.write(d, referee_ok=True, analyzers=["CodeCop"],
                            review_ok=True, review_independent=False)
        assert build_receipt.verify(d)[0], "should pass when review is not required"
        ok, why, _ = build_receipt.verify(d, require_review=True)
        assert not ok and "independent" in why
    finally:
        shutil.rmtree(d)


def test_receipt_hash_ignores_build_output():
    """.alpackages/bin/obj churn must not invalidate a receipt, or every promote fails."""
    d = _project()
    try:
        build_receipt.write(d, referee_ok=True, analyzers=["CodeCop"])
        os.makedirs(os.path.join(d, ".alpackages"), exist_ok=True)
        open(os.path.join(d, ".alpackages", "Sym.app"), "w").write("binary-ish\n")
        assert build_receipt.verify(d)[0], "build output must not invalidate the receipt"
    finally:
        shutil.rmtree(d)


if __name__ == "__main__":
    fns = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    for fn in fns:
        fn()
        print(f"  ok  {fn.__name__}")
    if SKIPPED:
        print("\nSKIPPED (not passes):")
        for sk in SKIPPED:
            print(f"  -- {sk}")
    print(f"\n{len(fns)} PASS" + (f", {len(SKIPPED)} leg(s) skipped" if SKIPPED else ""))
