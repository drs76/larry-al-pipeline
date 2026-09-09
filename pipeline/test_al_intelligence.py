"""AL specialisation suite — AL-1 symbols, AL-5 context, AL-4 events, AL-6 semantics.

House rule, learned the hard way: every test here must FAIL against the pre-change code.
An assertion that holds either way looks like coverage and guards nothing — a "~0k tokens"
check earlier in this project passed against a completely broken size calculation.

Symbol-dependent tests need a real `.alpackages`. They SKIP (loudly) when none is
present rather than passing vacuously, because a silent skip is the same failure mode.

Run: python3 test_al_intelligence.py
"""
import glob
import importlib.util
import json
import os
import re
import shutil
import subprocess
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
SKIPPED = []


def _load(name, fn):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fn))
    mod = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)
    except SystemExit:
        pass
    return mod


al_symbols = _load("al_symbols", "al_symbols.py")
al_context = _load("al_context", "al_context.py")
bcquality = _load("bcquality", "bcquality.py")
event_verify = _load("event_verify", "event_verify.py")
al_semantics = _load("al_semantics", "al_semantics.py")
al_tests = _load("al_tests", "al_tests.py")
al_probe = _load("al_probe", "al_probe.py")
al_profiles = _load("al_profiles", "al_profiles.py")
al_upgrade = _load("al_upgrade", "al_upgrade.py")
al_graph = _load("al_graph", "al_graph.py")
al_errors = _load("al_errors", "al_errors.py")
al_testgen = _load("al_testgen", "al_testgen.py")
al_brain = _load("al_brain", "al_brain.py")
al_capability = _load("al_capability", "al_capability.py")
al_temporal = _load("al_temporal", "al_temporal.py")
al_process = _load("al_process", "al_process.py")
rb = _load("rb", "run-build.py")
build_receipt = _load("build_receipt", "build_receipt.py")

# A project with real downloaded symbols, for the un-mocked half of the suite.
# AL_TEST_PROJECT first, then the Linux fixture paths. Windows reported 46 of these tests
# skipping unconditionally (2026-09-01): every candidate below is an NFS path that cannot
# exist there, so REAL was None on a box holding 50+ real client .alpackages. The skip read
# as "no symbols available", which was false — the harness simply had nowhere to look.
#
# An env var rather than a fourth hardcoded path: baking one machine's layout in is what
# produced this, and a client project is not the repo's business.
#
# What the 37 REAL-gated tests actually need, enumerated rather than guessed:
#   * a Base Application symbol set carrying `OnAfterPostSalesDoc` (the positive lookups)
#   * `OnAfterFrobnicateWidget` absent (the negative lookup — true of any real set)
#   * >1000 objects, enforced by real_index()
#   * symbols NOT at BC 14, because test_context_reports_declared_vs_actual_symbol_mismatch
#     declares 14 in a temp app.json and asserts the mismatch is reported. The declared
#     version lives in app.json; the actual version comes from the .app packages
#     (al_context.symbol_versions reads SymbolReference.json inside each). So the candidate's
#     BC version is one side of a real comparison, not inert.
#
# No exact version is required, but "any real symbol download" is too strong: a set old
# enough to lack OnAfterPostSalesDoc, or one actually at BC 14, will fail rather than skip.
# That is the intended behaviour — a wrong AL_TEST_PROJECT should fail loudly.
_CANDIDATES = ([os.environ["AL_TEST_PROJECT"]] if os.environ.get("AL_TEST_PROJECT") else []) + [
    "/mnt/rojaws/localDev/projects/bench-p4-unseen",
    "/mnt/rojaws/localDev/projects/route-planner",
    "/mnt/rojaws/localDev/projects/bench-p1-crud"]
# build_index() takes the PACKAGE DIRECTORY, not the project root. Passing the root
# quietly indexes whatever stray .app is lying about — 5 objects instead of 7908 — which
# is a green-looking test over the wrong data.
REAL = next((os.path.join(p, ".alpackages") for p in _CANDIDATES
             if os.path.isdir(os.path.join(p, ".alpackages"))), None)
REAL_ROOT = os.path.dirname(REAL) if REAL else None
_IDX = None


# Minimum BC the candidate symbols must be at. 27 unless told otherwise: the fixtures and
# the assertions built on them are BC27-shaped, and an older set cannot support them — the
# ABS codeunits and members doclink exercises simply did not exist in, say, BC 14. Pointing
# AL_TEST_PROJECT at an older client project must FAIL, loudly and by version, rather than
# produce confusing member-not-found errors thirty tests later.
MIN_BC = int(os.environ.get("AL_TEST_MIN_BC", "27"))


def _candidate_bc():
    """Major BC version of the candidate's downloaded symbols, or None."""
    try:
        vers = al_context.symbol_versions(REAL_ROOT)
        majors = [int(v.split(".")[0]) for v in vers.values() if v and v[0].isdigit()]
        return max(majors) if majors else None
    except Exception:
        return None


def real_index():
    global _IDX
    if _IDX is None:
        bc = _candidate_bc()
        assert bc is None or bc >= MIN_BC, (
            f"candidate symbols are BC {bc}, below the BC {MIN_BC} floor. These tests are "
            f"BC{MIN_BC}-shaped and an older set cannot satisfy them. Point AL_TEST_PROJECT "
            f"at a BC {MIN_BC}+ project, or set AL_TEST_MIN_BC if you mean it.")
        _IDX = al_symbols.build_index(REAL)
        assert len(_IDX) > 1000, (
            f"only {len(_IDX)} objects indexed from {REAL} — that is not a real Base "
            f"Application symbol set, so these tests would assert against nothing")
    return _IDX


_NO_SYMBOLS = ("no .alpackages under any candidate project — set AL_TEST_PROJECT to a "
               "project root holding a real Base+System symbol download. This is a harness "
               "gap, NOT proof the box has no symbols.")


def _try_symlink(target, link):
    """Symlink, or report loudly that the platform would not let us.

    Windows needs SeCreateSymbolicLinkPrivilege (admin or Developer Mode) and raises
    WinError 1314 without it. This call sits inside a REAL-gated test, so it was
    unreachable on Windows while AL_TEST_PROJECT did not exist — setting that variable
    makes it reachable, and it would have turned a skip into a crash.
    """
    try:
        os.symlink(target, link)
        return True
    except (OSError, NotImplementedError) as e:
        return False


def skip(name, why):
    SKIPPED.append(f"{name}: {why}")


# ─── AL-1: find a member without already knowing its object ────────────────────

def test_find_member_locates_event_without_knowing_the_object():
    """The whole point of AL-1. `lookup()` needs an object name up front; the question a
    coder actually has is 'does OnAfterPostSalesDoc exist, and where?'"""
    if not REAL:
        return skip("find_member", _NO_SYMBOLS)
    hits = al_symbols.find_member(real_index(), "OnAfterPostSalesDoc")
    assert hits, "OnAfterPostSalesDoc must be found in Base Application symbols"
    h = hits[0]
    assert h["object"] == "Sales-Post" and h["kind"] == "codeunit", h
    assert "SalesHeader" in h["signature"], h["signature"]
    assert h["is_event"], "must be flagged as an event"


def test_find_member_carries_symbol_evidence():
    """Acceptance criterion: no API claim without a citable source."""
    if not REAL:
        return skip("evidence", "no .alpackages")
    h = al_symbols.find_member(real_index(), "OnAfterPostSalesDoc")[0]
    ev = al_symbols.evidence(h)
    assert h.get("pkg") and h.get("pkg_version"), h
    assert ".app" in ev and h["pkg_version"] in ev, ev


def test_find_member_returns_all_candidates_not_a_guess():
    """Ambiguity is a result, not something to resolve by picking one."""
    if not REAL:
        return skip("ambiguity", "no .alpackages")
    idx = real_index()
    multi = [m for m in ("OnAfterInitialize", "OnBeforeRun", "OnAfterGetRecord")
             if len(al_symbols.find_member(idx, m)) > 1]
    assert multi, "expected at least one member published by several objects"
    hits = al_symbols.find_member(idx, multi[0])
    assert len({h["object"] for h in hits}) > 1, "all publishers must be returned"


def test_find_member_does_not_invent():
    if not REAL:
        return skip("no-invent", "no .alpackages")
    assert al_symbols.find_member(real_index(), "OnAfterFrobnicateWidget") == []


def test_find_field_and_enum():
    if not REAL:
        return skip("field/enum", "no .alpackages")
    idx = real_index()
    rec, fields = al_symbols.find_field(idx, "Sales Header")
    assert rec and "Document Type" in fields, "table fields must resolve"
    rec, one = al_symbols.find_field(idx, "Sales Header", "Sell-to Customer No.")
    assert one == ["Sell-to Customer No."], one
    # a missing TABLE and a missing FIELD are different failures
    assert al_symbols.find_field(idx, "No Such Table At All") == (None, [])
    rec, none = al_symbols.find_field(idx, "Sales Header", "Nonexistent Field")
    assert rec is not None and none == [], "table exists, field does not"
    erec, vals = al_symbols.find_enum(idx, "Sales Document Type")
    assert erec and vals, "enum values must resolve"


def test_events_only_filter_excludes_plain_procedures():
    if not REAL:
        return skip("events_only", "no .alpackages")
    idx = real_index()
    for h in al_symbols.find_event(idx, "OnAfterPostSalesDoc"):
        assert h["is_event"], h


# ─── AL-5: BC context ──────────────────────────────────────────────────────────

def _proj(app_json):
    d = tempfile.mkdtemp()
    open(os.path.join(d, "app.json"), "w").write(app_json)
    return d


def test_context_resolves_declared_metadata():
    d = _proj('{"id":"a-b","name":"X","version":"1.0.0.0","publisher":"P",'
              '"runtime":"16.0","application":"27.0.0.0","target":"OnPrem"}')
    try:
        c = al_context.resolve(d)
        assert c["bc_version"] == 27 and c["runtime"] == "16.0"
        assert c["target"] == "OnPrem" and c["app_name"] == "X"
    finally:
        shutil.rmtree(d)


def test_context_defaults_target_to_cloud_when_absent():
    """An omitted target IS Cloud — record the effective value so callers need not know."""
    d = _proj('{"id":"a","application":"26.0.0.0"}')
    try:
        assert al_context.resolve(d)["target"] == "Cloud"
    finally:
        shutil.rmtree(d)


def test_context_survives_broken_app_json():
    """Missing metadata must never take a build down."""
    d = _proj("{ this is not json")
    try:
        c = al_context.resolve(d)
        assert c["bc_version"] is None and c["target"] == "Cloud"
    finally:
        shutil.rmtree(d)


def test_context_reports_declared_vs_actual_symbol_mismatch():
    """The real failure mode: declares 27, compiles against 26, looks like a code bug."""
    if not REAL:
        return skip("mismatch", "no .alpackages")
    syms = al_context.symbol_versions(REAL_ROOT)
    assert syms, "candidate project should have symbol packages"
    # ADJACENT major, derived from the symbols actually present — not a hardcoded 14.
    #
    # This used to declare 14.0.0.0 against BC 27 symbols: a 13-version gap, chosen so the
    # mismatch was guaranteed whatever the candidate held. Sound instinct, wrong number.
    # The docstring above names the real failure mode as "declares 27, compiles against 26"
    # — an OFF-BY-ONE — and a 13-version gap does not exercise it. A tolerance added later
    # ("within one major is fine") would keep the old test green while silently dropping
    # exactly the case it exists to catch.
    #
    # Deriving it also keeps this robust for AL_TEST_PROJECT: whatever BC the candidate is
    # on, one below it is always a mismatch and always adjacent.
    actual = max(int(v.split(".")[0]) for v in syms.values() if v and v[0].isdigit())
    d = _proj('{"id":"a","application":"%d.0.0.0"}' % (actual - 1))
    try:
        if not _try_symlink(REAL, os.path.join(d, ".alpackages")):
            return skip("mismatch", "symlink privilege unavailable (Windows: WinError 1314 "
                                    "without Developer Mode) — the declared-vs-actual check "
                                    "needs one; this is a platform gap, not a symbol gap")
        c = al_context.resolve(d)
        assert c["version_mismatch"], (
            f"declared BC {actual - 1} vs downloaded BC {actual} must be reported — an "
            f"off-by-one is THE realistic case and the easiest to let through")
        assert c["bc_version"] != actual - 1, "effective version is what the symbols say"
    finally:
        shutil.rmtree(d)


# ─── AL-5: the dangling hook, and the bug that wiring it exposed ───────────────

def test_bcquality_version_ranges_are_understood():
    """The KB writes [16..] and [26..28]. Exact string matching — which is what the
    never-exercised filter did — drops every ranged rule, i.e. precisely the
    'this feature exists from BC N' rules a modern target most needs."""
    m = bcquality.version_matches
    assert m(["all"], 27) and m(None, 27)
    assert m(["16.."], 27) and not m(["16.."], 14)
    assert m(["26..28"], 27) and not m(["26..28"], 29) and not m(["26..28"], 25)
    assert m([26, 27, 28], 27) and not m([26, 27, 28], 29)
    assert m(["junk"], 27), "a frontmatter typo must not silently delete a rule"


def test_bcquality_actually_filters_the_real_kb_by_version():
    arts = bcquality._load_index(bcquality._root(None))
    if not arts:
        return skip("kb filter", "BCQuality KB not available")
    scoped = [a for a in arts if a.get("bc-version")
              and "all" not in [str(v) for v in a["bc-version"]]]
    if not scoped:
        return skip("kb filter", "no version-scoped articles in the KB")
    old = [a for a in scoped if bcquality.version_matches(a.get("bc-version"), 14)]
    new = [a for a in scoped if bcquality.version_matches(a.get("bc-version"), 27)]
    assert len(new) > len(old), (
        f"BC27 must admit more version-scoped rules than BC14 ({len(new)} vs {len(old)})")


# ─── AL-4: pre-compile event verification ──────────────────────────────────────

_SUBS = """codeunit 50100 "Test Subs"
{
    [EventSubscriber(ObjectType::Codeunit, Codeunit::"Sales-Post", 'OnAfterPostSalesDoc', '', true, true)]
    local procedure Good(var SalesHeader: Record "Sales Header"; GenJnlPostLine: Codeunit "Gen. Jnl.-Post Line")
    begin
    end;

    [EventSubscriber(ObjectType::Codeunit, Codeunit::"Sales-Post", 'OnAfterPostSalesDoc', '', true, true)]
    local procedure BadNames(var Header: Record "Sales Header")
    begin
    end;

    [EventSubscriber(ObjectType::Codeunit, Codeunit::"Sales-Post", 'OnAfterFrobnicateWidget', '', true, true)]
    local procedure Invented(var SalesHeader: Record "Sales Header")
    begin
    end;

    [EventSubscriber(ObjectType::Codeunit, Codeunit::"No Such Codeunit At All", 'OnWhatever', '', true, true)]
    local procedure NoPublisher()
    begin
    end;

    [EventSubscriber(ObjectType::Table, Database::"Sales Header", 'OnBeforeInsertEvent', '', true, true)]
    local procedure TableAuto(var Rec: Record "Sales Header"; RunTrigger: Boolean)
    begin
    end;
}
"""


def _srcdir(text):
    d = tempfile.mkdtemp()
    open(os.path.join(d, "subs.al"), "w").write(text)
    return d


def _rules(text):
    d = _srcdir(text)
    try:
        return {f["rule"] for f in event_verify.verify(d, real_index())}
    finally:
        shutil.rmtree(d)


def test_event_verify_catches_the_four_failure_kinds():
    if not REAL:
        return skip("event_verify", "no .alpackages")
    rules = _rules(_SUBS)
    assert "param-name-mismatch" in rules, rules
    assert "event-missing" in rules, rules
    assert "publisher-missing" in rules, rules


def test_event_verify_is_silent_on_correct_subscribers():
    """The one failure this must never have: accusing correct code."""
    if not REAL:
        return skip("event_verify clean", "no .alpackages")
    good = """codeunit 50100 X
{
    [EventSubscriber(ObjectType::Codeunit, Codeunit::"Sales-Post", 'OnAfterPostSalesDoc', '', true, true)]
    local procedure Good(var SalesHeader: Record "Sales Header"; GenJnlPostLine: Codeunit "Gen. Jnl.-Post Line")
    begin
    end;
}
"""
    d = _srcdir(good)
    try:
        assert event_verify.verify(d, real_index()) == []
    finally:
        shutil.rmtree(d)


def test_table_auto_events_are_never_reported_as_invented():
    """OnBeforeInsertEvent is compiler-synthesised and absent from symbols. Reporting it
    would send a correct build into a repair loop chasing nothing."""
    if not REAL:
        return skip("auto events", "no .alpackages")
    auto = """codeunit 50100 X
{
    [EventSubscriber(ObjectType::Table, Database::"Sales Header", 'OnAfterModifyEvent', '', true, true)]
    local procedure A(var Rec: Record "Sales Header"; var xRec: Record "Sales Header"; RunTrigger: Boolean)
    begin
    end;
}
"""
    d = _srcdir(auto)
    try:
        assert event_verify.verify(d, real_index()) == []
    finally:
        shutil.rmtree(d)


def test_numeric_object_references_resolve():
    """`Database::1173` is as legal as a quoted name; name-only lookup called it missing."""
    if not REAL:
        return skip("numeric refs", "no .alpackages")
    idx = real_index()
    rec = al_symbols.lookup_id(idx, "table", 1173)
    assert rec and rec["name"] == "Document Attachment", rec
    assert al_symbols.lookup_id(idx, "codeunit", 1173) != rec, "kind must disambiguate"
    numeric = """codeunit 50100 X
{
    [EventSubscriber(ObjectType::Table, Database::1173, 'OnBeforeExportToStream', '', true, true)]
    local procedure A(var DocumentAttachment: Record "Document Attachment"; AttachmentOutStream: OutStream; IsHandled: Boolean)
    begin
    end;
}
"""
    d = _srcdir(numeric)
    try:
        assert event_verify.verify(d, idx) == [], "a numeric publisher must resolve"
    finally:
        shutil.rmtree(d)


def test_project_own_publisher_is_not_called_missing():
    if not REAL:
        return skip("local publisher", "no .alpackages")
    own = """codeunit 50100 X
{
    [EventSubscriber(ObjectType::Codeunit, Codeunit::"My Own Mgt", 'OnAfterThing', '', true, true)]
    local procedure A(Value: Integer)
    begin
    end;
}
"""
    d = _srcdir(own)
    try:
        assert event_verify.verify(d, real_index()) != [], "unknown publisher IS a finding"
        assert event_verify.verify(d, real_index(),
                                   local_objects=["My Own Mgt"]) == []
    finally:
        shutil.rmtree(d)


def test_obsolete_events_are_warnings_not_errors():
    if not REAL:
        return skip("obsolete", "no .alpackages")
    idx = real_index()
    obs = [r for r in idx.values() if r.get("obsolete")]
    assert obs, "symbols carry Obsolete attributes — none were captured"
    h = al_symbols.find_member(idx, next(iter(obs[0]["obsolete"])))
    assert any(x.get("obsolete") for x in h), "obsolete must surface on find_member results"


def test_no_symbols_means_no_findings():
    """An empty index must not turn every subscriber into an accusation."""
    d = _srcdir(_SUBS)
    try:
        assert event_verify.verify(d, {}) == []
    finally:
        shutil.rmtree(d)


# ─── AL-6: deterministic semantic rules ────────────────────────────────────────

def _sem(text):
    d = tempfile.mkdtemp()
    try:
        open(os.path.join(d, "x.al"), "w").write(text)
        return {f["rule"] for f in al_semantics.analyse(d, src=d)}
    finally:
        shutil.rmtree(d)


def test_semantics_flags_db_call_in_loop():
    rules = _sem("""codeunit 1 X
{
    procedure P()
    var
        Cust: Record Customer;
        SalesLine: Record "Sales Line";
    begin
        if SalesLine.FindSet() then
            repeat
                Cust.Get(SalesLine."Sell-to Customer No.");
            until SalesLine.Next() = 0;
    end;
}
""")
    assert "db-call-in-loop" in rules, rules


def test_semantics_ignores_temp_records_in_a_loop():
    """A temporary record lives in memory — a Get per iteration is a hash lookup, not a
    database round trip. 20% of the first Microsoft-corpus run was this false positive."""
    rules = _sem("""codeunit 1 X
{
    procedure P()
    var
        TempCust: Record Customer temporary;
        SalesLine: Record "Sales Line";
    begin
        if SalesLine.FindSet() then
            repeat
                TempCust.Get(SalesLine."Sell-to Customer No.");
            until SalesLine.Next() = 0;
    end;
}
""")
    assert "db-call-in-loop" not in rules, rules


def test_semantics_temp_check_uses_the_receiver_not_the_argument():
    """`SalesHeader.Get(TempEntry."No.")` hits the database — only the ARGUMENT is temp."""
    rules = _sem("""codeunit 1 X
{
    procedure P()
    var
        SalesHeader: Record "Sales Header";
        TempEntry: Record "Sales Line" temporary;
    begin
        if TempEntry.FindSet() then
            repeat
                SalesHeader.Get(TempEntry."Document No.");
            until TempEntry.Next() = 0;
    end;
}
""")
    assert "db-call-in-loop" in rules, rules


def test_semantics_flags_commit_in_loop():
    rules = _sem("""codeunit 1 X
{
    procedure P()
    var
        SalesLine: Record "Sales Line";
    begin
        if SalesLine.FindSet() then
            repeat
                SalesLine.Modify();
                Commit();
            until SalesLine.Next() = 0;
    end;
}
""")
    assert "commit-in-loop" in rules, rules


def test_semantics_locktable_before_read_is_correct_code():
    """Lock-then-read is the right order and must not be flagged; read-then-lock must be."""
    good = """codeunit 1 X
{
    procedure P()
    var
        Cust: Record Customer;
    begin
        Cust.LockTable();
        Cust.Get('X');
        Cust.Modify();
    end;
}
"""
    bad = """codeunit 1 X
{
    procedure P()
    var
        Cust: Record Customer;
    begin
        Cust.Get('X');
        Cust.LockTable();
        Cust.Modify();
    end;
}
"""
    assert "locktable-after-read" not in _sem(good)
    assert "locktable-after-read" in _sem(bad)


def test_semantics_locktable_ignores_a_different_variable():
    """Locking VATEntry after reading GLEntry is ordinary code — this produced 1293
    accusations against Microsoft's base application."""
    rules = _sem("""codeunit 1 X
{
    procedure P()
    var
        GLEntry: Record "G/L Entry";
        VATEntry: Record "VAT Entry";
    begin
        GLEntry.LockTable();
        if GLEntry.FindLast() then;
        VATEntry.LockTable();
        if VATEntry.FindLast() then;
    end;
}
""")
    assert "locktable-after-read" not in rules, rules


def test_semantics_does_not_scan_across_procedure_boundaries():
    """A LockTable on a procedure's first line was blamed for a read in the procedure
    above it."""
    rules = _sem("""codeunit 1 X
{
    procedure A()
    var
        Skill: Record "Resource Skill";
    begin
        if Skill.Find('-') then;
    end;

    procedure B()
    var
        Skill: Record "Resource Skill";
    begin
        Skill.LockTable();
        Skill.DeleteAll();
    end;
}
""")
    assert "locktable-after-read" not in rules, rules


def test_semantics_recordref_parameter_is_opened_by_the_caller():
    rules = _sem("""codeunit 1 X
{
    procedure P(var DocLine: RecordRef)
    var
        FRef: FieldRef;
        PurchLine: Record "Purchase Line";
    begin
        FRef := DocLine.Field(PurchLine.FieldNo(Type));
    end;
}
""")
    assert "fieldref-without-open" not in rules, rules


def test_semantics_ignores_comments_and_string_literals():
    """`Commit` in a caption is not a Commit."""
    rules = _sem("""codeunit 1 X
{
    procedure P()
    var
        SalesLine: Record "Sales Line";
    begin
        if SalesLine.FindSet() then
            repeat
                Message('Commit() happens later');   // Commit() here would be wrong
            until SalesLine.Next() = 0;
    end;
}
""")
    assert "commit-in-loop" not in rules, rules


def test_semantics_everything_is_advisory():
    """The review was explicit: false positives must not fail the compiler."""
    findings = []
    for t in (_SUBS,):
        d = tempfile.mkdtemp()
        try:
            open(os.path.join(d, "x.al"), "w").write(t)
            findings += al_semantics.analyse(d, src=d)
        finally:
            shutil.rmtree(d)
    assert all(f["severity"] != "error" for f in al_semantics.analyse(
        "/mnt/rojaws/localDev/setup/pipeline", src="/mnt/rojaws/localDev/setup/pipeline")
        + findings), "no semantic rule may emit an error severity"


def test_semantics_findings_are_actionable():
    """Every finding must say what to check next — a bare label sends a model guessing."""
    rules = _sem("""codeunit 1 X
{
    procedure P()
    var
        Cust: Record Customer;
        SalesLine: Record "Sales Line";
    begin
        if SalesLine.FindSet() then
            repeat
                Cust.Get(SalesLine."Sell-to Customer No.");
            until SalesLine.Next() = 0;
    end;
}
""")
    d = tempfile.mkdtemp()
    try:
        open(os.path.join(d, "x.al"), "w").write("""codeunit 1 X
{
    procedure P()
    var
        Cust: Record Customer;
        SalesLine: Record "Sales Line";
    begin
        if SalesLine.FindSet() then
            repeat
                Cust.Get(SalesLine."Sell-to Customer No.");
            until SalesLine.Next() = 0;
    end;
}
""")
        for f in al_semantics.analyse(d, src=d):
            assert f["suggested_next_check"] and f["reason"], f
            assert set(f) >= {"rule", "file", "line", "severity", "reason",
                              "evidence", "suggested_next_check"}, sorted(f)
    finally:
        shutil.rmtree(d)


# ─── AL-3: tests in the referee, opt-in and fail-closed ────────────────────────

_TEST_CU = """codeunit 50190 "My Tests"
{
    Subtype = Test;

    [Test]
    procedure TestOne()
    begin
    end;
}
"""


def _testproj(with_tests=True):
    d = tempfile.mkdtemp()
    os.makedirs(os.path.join(d, "src"))
    open(os.path.join(d, "src", "a.al"), "w").write("codeunit 50100 X { }\n")
    if with_tests:
        open(os.path.join(d, "src", "t.al"), "w").write(_TEST_CU)
    return d


def test_test_codeunits_are_detected_by_subtype():
    d = _testproj()
    try:
        found = al_tests.find_test_codeunits(os.path.join(d, "src"))
        assert len(found) == 1 and found[0].endswith("t.al"), found
    finally:
        shutil.rmtree(d)


def test_no_tests_is_not_a_failure():
    """Most prototypes have none. Failing them would just get the flag turned off."""
    d = _testproj(with_tests=False)
    try:
        r = al_tests.run(d, "app-id", 27, runner=lambda cmd: (0, ""))
        assert r["status"] == "no-tests" and r["ok"] is True, r
    finally:
        shutil.rmtree(d)


def test_parse_results_reads_the_bcl_summary_line():
    out = ("My Ext: 3 tests, 2 passed, 1 failed (4.2s)\n"
           "  ✓ TestA\n  ✗ TestB — Assert.AreEqual failed\n"
           "TOTAL: 3 tests, 2 passed, 1 failed\n")
    total, passed, failed, failures = al_tests.parse_results(out)
    assert (total, passed, failed) == (3, 2, 1)
    assert failures and "TestB" in failures[0], failures


def test_missing_results_is_infrastructure_not_a_pass():
    """The review's explicit requirement: an infrastructure failure must never be
    silently downgraded to a clean build."""
    assert al_tests.parse_results("ssh: connect to host port 14122: Connection refused") is None
    d = _testproj()
    try:
        r = al_tests.run(d, "app-id", 27,
                         runner=lambda cmd: (255, "ssh: Connection refused"))
        assert r["status"] == "infrastructure" and r["ok"] is False, r
        assert "infrastructure" in r["detail"]
    finally:
        shutil.rmtree(d)


def test_failing_tests_fail_the_referee():
    d = _testproj()
    try:
        r = al_tests.run(d, "app-id", 27, runner=lambda cmd: (
            1, "TOTAL: 3 tests, 2 passed, 1 failed\n  ✗ TestB — boom\n"))
        assert r["status"] == "failed" and r["ok"] is False and r["failed"] == 1, r
    finally:
        shutil.rmtree(d)


def test_passing_tests_pass_the_referee():
    d = _testproj()
    try:
        r = al_tests.run(d, "app-id", 27, runner=lambda cmd: (
            0, "TOTAL: 5 tests, 5 passed, 0 failed\n"))
        assert r["status"] == "passed" and r["ok"] is True and r["passed"] == 5, r
    finally:
        shutil.rmtree(d)


def test_publish_failure_is_infrastructure():
    d = _testproj()
    try:
        calls = []

        def runner(cmd):
            calls.append(cmd[1])
            return (1, "publish rejected: schema sync required") if cmd[1] == "publish" else (0, "TOTAL: 1 tests, 1 passed, 0 failed")
        r = al_tests.run(d, "app-id", 27, app_file="/tmp/x.app", runner=runner)
        assert r["status"] == "infrastructure" and not r["ok"], r
        assert calls == ["publish"], "must not run tests after a failed publish"
    finally:
        shutil.rmtree(d)


def test_altool_backend_selects_by_app_not_extension():
    """altool discovers codeunit ids from the compiled symbol, so it needs -app.
    Passing -extension instead would filter nothing and run the whole suite."""
    d = _testproj()
    try:
        seen = []

        def runner(cmd):
            seen.append(cmd)
            return 0, "TOTAL: 2 tests, 2 passed, 0 failed, 0 skipped, 0 codeunit error(s)"
        r = al_tests.run(d, "app-id", 27, app_file="/tmp/x.app", runner=runner,
                         backend="altool")
        assert r["status"] == "passed" and r["ok"] is True, r
        assert len(seen) == 1, f"altool publishes -app itself; must not pre-publish: {seen}"
        cmd = seen[0]
        assert "-runner" in cmd and cmd[cmd.index("-runner") + 1] == "altool", cmd
        assert "-app" in cmd and "-extension" not in cmd, cmd
        # -version drives the toolkit publish out of the artifact cache, which only
        # the guest backend needs.
        assert "-version" not in cmd, cmd
    finally:
        shutil.rmtree(d)


def test_guest_backend_keeps_the_old_command_shape():
    """The default must not change: publish first, then filter by extension id."""
    d = _testproj()
    try:
        seen = []

        def runner(cmd):
            seen.append(cmd)
            return 0, "TOTAL: 1 tests, 1 passed, 0 failed"
        r = al_tests.run(d, "app-id", 27, app_file="/tmp/x.app", runner=runner)
        assert r["status"] == "passed", r
        assert [c[1] for c in seen] == ["publish", "test"], seen
        assert "-extension" in seen[1] and "-app" not in seen[1], seen[1]
        assert "-version" in seen[1], seen[1]
    finally:
        shutil.rmtree(d)


def test_codeunit_errors_are_infrastructure_not_a_zero_test_pass():
    """The sharp edge of the altool backend: a codeunit that never ran contributes
    0 to tests/passed/failed, so a wholly-failed run reads as "0 tests, 0 passed,
    0 failed" — a pass — unless the separate error count is read."""
    d = _testproj()
    try:
        out = "TOTAL: 0 tests, 0 passed, 0 failed, 0 skipped, 1 codeunit error(s)"
        r = al_tests.run(d, "app-id", 27, app_file="/tmp/x.app",
                         runner=lambda cmd: (1, out), backend="altool")
        assert r["status"] == "infrastructure" and r["ok"] is False, r
        assert r["codeunit_errors"] == 1, r
    finally:
        shutil.rmtree(d)


def test_declared_tests_that_never_ran_is_infrastructure():
    """The project HAS test codeunits. Running them and getting none back is a
    broken selection or a broken environment, never a clean build."""
    d = _testproj()
    try:
        r = al_tests.run(d, "app-id", 27, app_file="/tmp/x.app",
                         runner=lambda cmd: (0, "TOTAL: 0 tests, 0 passed, 0 failed"),
                         backend="altool")
        assert r["status"] == "infrastructure" and r["ok"] is False, r
        assert "none ran" in r["detail"], r["detail"]
    finally:
        shutil.rmtree(d)


def test_altool_without_an_app_file_stops_rather_than_widening():
    """No .app means no codeunit discovery. Falling back to the whole suite would
    turn a missing artifact into a silently broader run."""
    d = _testproj()
    try:
        r = al_tests.run(d, "app-id", 27, runner=lambda cmd: (0, "TOTAL: 9 tests, 9 passed, 0 failed"),
                         backend="altool")
        assert r["status"] == "infrastructure" and r["ok"] is False, r
        assert ".app" in r["detail"], r["detail"]
    finally:
        shutil.rmtree(d)


def test_unknown_backend_fails_closed():
    d = _testproj()
    try:
        r = al_tests.run(d, "app-id", 27, app_file="/tmp/x.app",
                         runner=lambda cmd: (0, "TOTAL: 1 tests, 1 passed, 0 failed"),
                         backend="typo")
        assert r["status"] == "infrastructure" and r["ok"] is False, r
    finally:
        shutil.rmtree(d)


def test_parse_codeunit_errors_absent_field_is_zero():
    """The guest backend's summary line has no error field. Absent must read as 0,
    not as a parse failure that would fail every guest run."""
    assert al_tests.parse_codeunit_errors("TOTAL: 3 tests, 3 passed, 0 failed") == 0
    assert al_tests.parse_codeunit_errors(
        "TOTAL: 0 tests, 0 passed, 0 failed, 0 skipped, 2 codeunit error(s)") == 2


def test_receipt_require_tests_rejects_a_build_that_ran_none():
    """tests_ok is None when tests never ran, and None must not read as True."""
    d = _testproj()
    try:
        build_receipt.write(d, referee_ok=True, analyzers=["CodeCop"], tests_ok=None)
        assert build_receipt.verify(d)[0], "should pass when tests are not required"
        ok, why, _ = build_receipt.verify(d, require_tests=True)
        assert not ok and "ran none" in why, why
    finally:
        shutil.rmtree(d)


def test_receipt_require_tests_rejects_failing_tests():
    d = _testproj()
    try:
        build_receipt.write(d, referee_ok=True, analyzers=["CodeCop"], tests_ok=False)
        ok, why, _ = build_receipt.verify(d, require_tests=True)
        assert not ok and "FAILING" in why, why
    finally:
        shutil.rmtree(d)


def test_receipt_require_tests_accepts_a_real_test_pass():
    d = _testproj()
    try:
        build_receipt.write(d, referee_ok=True, analyzers=["CodeCop"], tests_ok=True,
                            extra={"tests": {"status": "passed", "total": 5}})
        assert build_receipt.verify(d, require_tests=True)[0]
    finally:
        shutil.rmtree(d)


def test_receipt_require_tests_rejects_a_project_with_no_tests():
    """"no-tests" is fine for a build and NOT fine when the caller demanded tests."""
    d = _testproj(with_tests=False)
    try:
        build_receipt.write(d, referee_ok=True, analyzers=["CodeCop"], tests_ok=True,
                            extra={"tests": {"status": "no-tests"}})
        assert build_receipt.verify(d)[0]
        ok, why, _ = build_receipt.verify(d, require_tests=True)
        assert not ok and "no Subtype=Test" in why, why
    finally:
        shutil.rmtree(d)


# ─── AL-2: compiler probes for uncertain APIs ──────────────────────────────────

def test_probe_verifies_a_valid_hypothesis():
    if not REAL:
        return skip("probe valid", "no .alpackages")
    r = al_probe.probe_snippet('Cust.Init();', 'Cust: Record Customer;',
                               alpackages=REAL)
    assert r["status"] == "verified" and r["ok"], r["summary"]


def test_probe_rejects_an_invalid_hypothesis_with_structural_diagnostics():
    if not REAL:
        return skip("probe invalid", "no .alpackages")
    r = al_probe.probe_snippet('Cust.FrobnicateWidget();', 'Cust: Record Customer;',
                               alpackages=REAL)
    assert r["status"] == "rejected" and not r["ok"], r["summary"]
    assert r["errors"] and r["errors"][0]["code"] == "AL0132", r["errors"]
    # structural, not just text: code / line / message are separate fields
    assert set(r["errors"][0]) >= {"code", "severity", "line", "message"}


def test_probe_distinguishes_a_missing_object_from_a_missing_member():
    """The ambiguity AL0132 leaves a model with, and the reason the probe exists."""
    if not REAL:
        return skip("probe object", "no .alpackages")
    r = al_probe.probe_snippet('', 'V: Record "No Such Table Anywhere";',
                               alpackages=REAL)
    assert r["status"] == "rejected"
    assert any(d["code"] == "AL0185" for d in r["errors"]), r["errors"]


def test_probe_snippet_procedure_does_not_collide_with_builtin_run():
    """Every codeunit already has Run(), so a probe procedure named Run fails with AL0440
    regardless of the statements — making a VALID hypothesis look rejected."""
    assert "procedure Run()" not in al_probe.wrap_snippet("x := 1;")
    if REAL:
        r = al_probe.probe_snippet('Cust.Init();', 'Cust: Record Customer;',
                                   alpackages=REAL)
        assert not any(d["code"] == "AL0440" for d in r["errors"]), r["errors"]


def test_probe_cannot_modify_the_target_project():
    """Acceptance criterion, checked empirically: hash the tree before and after."""
    if not REAL:
        return skip("probe containment", "no .alpackages")
    before = build_receipt.tree_hash(REAL_ROOT)
    listing = sorted(os.listdir(REAL))
    al_probe.probe_snippet('Cust.Init();', 'Cust: Record Customer;', alpackages=REAL)
    assert build_receipt.tree_hash(REAL_ROOT) == before, "probe modified the target tree"
    assert sorted(os.listdir(REAL)) == listing, "probe modified .alpackages"


def test_probe_always_removes_its_workspace():
    if not REAL:
        return skip("probe cleanup", "no .alpackages")
    before = set(glob.glob(os.path.join(tempfile.gettempdir(), "al-probe-*")))
    for src in ('Cust.Init();', 'Cust.Nonexistent();'):
        al_probe.probe_snippet(src, 'Cust: Record Customer;', alpackages=REAL)
    after = set(glob.glob(os.path.join(tempfile.gettempdir(), "al-probe-*")))
    assert after == before, f"probe workspaces left behind: {after - before}"


def test_probe_timeout_is_not_a_rejection():
    """A timeout says nothing about legality. Reporting it as rejected would teach the
    model that correct AL is invalid."""
    if not REAL:
        return skip("probe timeout", "no .alpackages")
    r = al_probe.probe_snippet('Cust.Init();', 'Cust: Record Customer;',
                               alpackages=REAL, timeout=0.001)
    assert r["status"] == "timeout" and not r["ok"], r
    assert "NOT evidence" in r["summary"]
    assert "inconclusive" in al_probe.format_result(r).lower()


def test_probe_harness_failure_is_not_a_rejection():
    """No symbols is a fact about the harness, never about the AL."""
    d = tempfile.mkdtemp()
    try:
        r = al_probe.probe_snippet('Cust.Init();', alpackages=d)
        assert r["status"] == "error" and not r["ok"], r
        assert r["errors"] == []
    finally:
        shutil.rmtree(d)
    r = al_probe.probe_snippet('Cust.Init();')
    assert r["status"] == "error" and "no symbols" in r["summary"], r


def test_probe_result_is_usable_by_the_next_step():
    if not REAL:
        return skip("probe format", "no .alpackages")
    r = al_probe.probe_snippet('Cust.FrobnicateWidget();', 'Cust: Record Customer;',
                               alpackages=REAL)
    text = al_probe.format_result(r, "Customer.FrobnicateWidget exists")
    assert "REJECTED" in text and "AL0132" in text, text


# ─── AL-11: deployment profiles ────────────────────────────────────────────────

def test_internal_profile_reproduces_historical_behaviour():
    """The property that matters most. A profile system that quietly changes every
    existing build is a regression wearing a feature's clothes."""
    p = al_profiles.resolve("internal")
    assert tuple(p["analyzers"]) == ("CodeCop", "UICop", "PerTenantExtensionCop")
    assert al_profiles.review_policy(p) == (False, False), "review was advisory before"
    assert al_profiles.tests_policy(p) == (False, False), "tests did not run before"
    assert not p.get("fail_on_warning") and not p.get("escalate")
    assert not p.get("require_target")
    assert al_profiles.check_diagnostics(
        [{"code": "AA0218", "severity": "Warning"}], p) == [], "warnings did not fail"


def test_unknown_profile_raises_rather_than_downgrading():
    """Typing `apsource` must not silently run AppSource work through prototype checks."""
    try:
        al_profiles.resolve("apsource")
        raise AssertionError("unknown profile must raise")
    except al_profiles.ProfileError as e:
        assert "apsource" in str(e) and "appsource" in str(e)


def test_yaml_does_not_turn_off_into_a_boolean():
    """YAML 1.1 reads bare `off` as False, which made the summary print `tests=False`."""
    assert al_profiles.resolve("internal")["tests"] == "off"


def test_profiles_tighten_without_pipeline_code():
    p = al_profiles.resolve("appsource")
    assert "AppSourceCop" in p["analyzers"]
    assert al_profiles.review_policy(p) == (True, True)
    assert al_profiles.tests_policy(p) == (True, True)
    assert p["require_target"] == "Cloud"


def test_same_source_evaluates_differently_per_profile():
    """The acceptance criterion, on one unchanged tree."""
    d = tempfile.mkdtemp()
    try:
        open(os.path.join(d, "app.json"), "w").write(json.dumps({
            "id": "x", "name": "N", "publisher": "P", "version": "1.0.0.0",
            "runtime": "16.0", "application": "27.0.0.0", "target": "OnPrem"}))
        assert al_profiles.evaluate(d, "internal")["ok"], "internal must accept it"
        r = al_profiles.evaluate(d, "appsource")
        assert not r["ok"], "appsource must reject the same tree"
        joined = " ".join(r["failures"])
        assert "target" in joined and "missing" in joined, r["failures"]
    finally:
        shutil.rmtree(d)


def test_omitted_target_satisfies_a_cloud_requirement():
    """An absent target IS Cloud — rejecting it would be a false failure."""
    p = al_profiles.resolve("appsource")
    # an explicit contradicting target IS a failure — the silence below must come from
    # the default, not from the check being asleep
    assert any("target" in f for f in al_profiles.check_manifest({"target": "OnPrem"}, p))
    fails = al_profiles.check_manifest(
        {"id": 1, "name": 1, "publisher": 1, "version": 1, "runtime": 1,
         "application": 1, "brief": 1, "description": 1, "privacyStatement": 1,
         "EULA": 1, "help": 1, "url": 1, "logo": 1, "idRanges": 1}, p)
    assert fails == [], f"a complete manifest with no target must pass: {fails}"


def test_escalated_warnings_fail_only_where_the_profile_says_so():
    diags = [{"code": "AA0218", "severity": "Warning"},
             {"code": "AA0247", "severity": "Warning"},
             {"code": "AL0132", "severity": "Error"}]
    assert al_profiles.check_diagnostics(diags, al_profiles.resolve("internal")) == []
    cust = al_profiles.check_diagnostics(diags, al_profiles.resolve("customer"))
    assert len(cust) == 1 and "AA0218" in cust[0], cust
    apps = al_profiles.check_diagnostics(diags, al_profiles.resolve("appsource"))
    assert len(apps) == 2, "fail_on_warning covers every warning"
    assert not any("AL0132" in f for f in apps), "errors are the compiler's business"


def test_declared_but_unenforced_policy_is_reported_not_implied():
    """An `upgrade` profile that looks like it checks breaking changes and does not is
    worse than no profile at all."""
    p = al_profiles.resolve("upgrade")
    u = dict(al_profiles.unenforced(p))
    # breaking_changes moved out of `declared:` when AL-7 landed — see
    # test_breaking_changes_is_no_longer_merely_declared. upgrade_codeunits has not:
    # nothing inspects upgrade codeunits yet, so it stays honest about that.
    assert "upgrade_codeunits" in u and "breaking_changes" not in u, u
    d = tempfile.mkdtemp()
    try:
        open(os.path.join(d, "app.json"), "w").write(json.dumps({
            "id": "x", "name": "N", "publisher": "P", "version": "1.0.0.0",
            "runtime": "16.0", "application": "27.0.0.0"}))
        r = al_profiles.evaluate(d, "upgrade")
        assert r["ok"] and r["partial"], "a pass here must be marked PARTIAL"
        assert al_profiles.unenforced(al_profiles.resolve("internal")) == [], \
            "internal promises nothing it cannot check"
    finally:
        shutil.rmtree(d)


def test_every_profile_loads_and_is_self_consistent():
    for n in al_profiles.names():
        p = al_profiles.resolve(n)
        assert p["analyzers"], n
        assert str(p["tests"]).lower() in ("off", "optional", "required"), (n, p["tests"])
        assert str(p["review"]).lower() in ("none", "advisory", "required"), (n, p["review"])


def test_metadata_policy_is_checkable_before_any_model_call():
    """Missing app.json fields surface through the analyzers as ordinary compile errors,
    so the fix loop spends rounds asking a model to repair something no AL can repair —
    and mangles the source trying. Observed live: an appsource build of bench-p1-crud
    burned nine rounds and dropped an enum. check_manifest settles it by reading one file,
    which is what the pre-loop gate uses.
    """
    p = al_profiles.resolve("appsource")
    thin = {"id": "x", "name": "N", "publisher": "P", "version": "1.0.0.0",
            "runtime": "16.0", "application": "27.0.0.0"}
    fails = al_profiles.check_manifest(thin, p)
    assert fails, "an AppSource build of this manifest must be refused up front"
    assert any("logo" in f for f in fails), fails
    # and the same manifest is fine for the profile it was actually written for
    assert al_profiles.check_manifest(thin, al_profiles.resolve("internal")) == []


# ─── AL-7: upgrade / breaking-change analysis ──────────────────────────────────

def _obj(kind, oid, name, **kw):
    rec = {"kind": kind, "id": oid, "name": name, "obsolete": "", "obsolete_reason": "",
           "fields": {}, "keys": {}, "values": [], "methods": {}, "api": {}}
    rec.update(kw)
    return rec


def _surf(objs, deps=(), version="1.0.0.0", app_id="APP"):
    return {"path": "x.app", "app_id": app_id, "name": "X", "version": version,
            "dependencies": list(deps),
            "objects": {(o["kind"], o["id"]): o for o in objs}}


def _diff_rules(old, new):
    return {f["rule"]: f["severity"] for f in al_upgrade.diff(old, new)}


def test_identical_versions_produce_no_findings():
    """The baseline property: comparing a build to itself must be silent."""
    o = _surf([_obj("table", 1, "T", fields={1: {"name": "A", "type": "Code[20]",
                                                 "obsolete": ""}})])
    assert al_upgrade.diff(o, o) == []
    assert al_upgrade.verdict([]) == al_upgrade.SAFE


def test_deleted_table_is_a_data_migration_not_merely_breaking():
    r = _diff_rules(_surf([_obj("table", 1, "T")]), _surf([]))
    assert r["object-deleted"] == al_upgrade.DATA, r


def test_object_renumbering_is_detected_and_not_reported_as_delete_plus_add():
    """False equivalence works both ways: same name at a different id is neither the same
    object nor a deletion."""
    r = _diff_rules(_surf([_obj("table", 50300, "Equipment")]),
               _surf([_obj("table", 50305, "Equipment")]))
    assert "object-renumbered" in r and r["object-renumbered"] == al_upgrade.DATA, r
    assert "object-deleted" not in r and "object-added" not in r, r


def test_field_deletion_and_type_change_require_migration():
    old = _surf([_obj("table", 1, "T", fields={
        1: {"name": "A", "type": "Code[20]", "obsolete": ""},
        2: {"name": "B", "type": "Text[100]", "obsolete": ""}})])
    new = _surf([_obj("table", 1, "T", fields={
        1: {"name": "A", "type": "Code[10]", "obsolete": ""}})])
    r = _diff_rules(old, new)
    assert r["field-deleted"] == al_upgrade.DATA
    assert r["field-type-changed"] == al_upgrade.DATA


def test_field_renumbering_is_caught_even_though_it_compiles():
    """The quiet one: the column keeps the old id and the field that claims the name
    points somewhere else."""
    old = _surf([_obj("table", 1, "T", fields={3: {"name": "Serial", "type": "Code[50]",
                                                   "obsolete": ""}})])
    new = _surf([_obj("table", 1, "T", fields={9: {"name": "Serial", "type": "Code[50]",
                                                   "obsolete": ""}})])
    r = _diff_rules(old, new)
    assert r.get("field-renumbered") == al_upgrade.DATA, r
    assert "field-deleted" not in r and "field-added" not in r, r


def test_renaming_a_field_keeps_the_data_so_it_is_only_a_warning():
    old = _surf([_obj("table", 1, "T", fields={1: {"name": "Old", "type": "Code[20]",
                                                   "obsolete": ""}})])
    new = _surf([_obj("table", 1, "T", fields={1: {"name": "New", "type": "Code[20]",
                                                   "obsolete": ""}})])
    assert _diff_rules(old, new)["field-renamed"] == al_upgrade.WARNING


def test_enum_ordinals_are_data():
    """Enum values carry no id — the ordinal is positional and stored in every row."""
    base = _surf([_obj("enum", 1, "E", values=["A", "B", "C"])])
    assert _diff_rules(base, _surf([_obj("enum", 1, "E", values=["A", "B", "C", "D"])])) \
        == {"enum-value-added": al_upgrade.SAFE}, "appending is safe"
    r = _diff_rules(base, _surf([_obj("enum", 1, "E", values=["A", "X", "B", "C"])]))
    assert r["enum-value-inserted"] == al_upgrade.DATA
    assert "enum-values-reordered" not in r, (
        "an insertion already explains the shift — reporting it twice makes a precise "
        "report look noisy")
    r = _diff_rules(base, _surf([_obj("enum", 1, "E", values=["A", "C", "B"])]))
    assert r["enum-values-reordered"] == al_upgrade.DATA, r
    assert _diff_rules(base, _surf([_obj("enum", 1, "E", values=["A", "B"])]))[
        "enum-value-removed"] == al_upgrade.BREAKING


def test_event_and_public_procedure_contracts_are_breaking():
    def cu(sig, event="IntegrationEvent", public=True):
        return _obj("codeunit", 1, "C",
                    methods={"OnThing": {"signature": sig, "event": event,
                                         "public": public, "obsolete": ""}})
    old = _surf([cu("OnThing(Equipment: Record Equipment)")])
    r = _diff_rules(old, _surf([cu("OnThing(Equip: Record Equipment)")]))
    assert r["signature-changed"] == al_upgrade.BREAKING, r
    assert _diff_rules(old, _surf([_obj("codeunit", 1, "C")]))["member-removed"] \
        == al_upgrade.BREAKING


def test_internal_members_are_not_a_contract():
    """A local procedure changing is nobody else's business — flagging it would drown the
    real findings."""
    def cu(sig):
        return _obj("codeunit", 1, "C",
                    methods={"Helper": {"signature": sig, "event": "",
                                        "public": False, "obsolete": ""}})
    assert al_upgrade.diff(_surf([cu("Helper(A: Integer)")]),
                           _surf([cu("Helper(B: Text)")])) == []


def test_api_contract_changes_are_breaking():
    old = _surf([_obj("page", 1, "P", api={"APIVersion": "v1.0", "EntityName": "equip"})])
    new = _surf([_obj("page", 1, "P", api={"APIVersion": "v2.0", "EntityName": "equip"})])
    assert _diff_rules(old, new)["api-contract-changed"] == al_upgrade.BREAKING


def test_dependency_changes_are_reported():
    old = _surf([], deps=[{"Id": "a", "Name": "Lib", "MinVersion": "1.0.0.0"}])
    new = _surf([], deps=[{"Id": "a", "Name": "Lib", "MinVersion": "2.0.0.0"},
                          {"Id": "b", "Name": "New", "MinVersion": "1.0.0.0"}])
    r = _diff_rules(old, new)
    assert r["dependency-version-raised"] == al_upgrade.WARNING
    assert r["dependency-added"] == al_upgrade.WARNING


def test_verdict_is_the_worst_severity_present():
    fs = [{"severity": al_upgrade.SAFE}, {"severity": al_upgrade.WARNING},
          {"severity": al_upgrade.DATA}, {"severity": al_upgrade.BREAKING}]
    assert al_upgrade.verdict(fs) == al_upgrade.DATA, "data loss outranks a broken contract"
    assert al_upgrade.verdict([]) == al_upgrade.SAFE


def test_profile_upgrade_policy_gates_by_verdict():
    up, ap = al_profiles.resolve("upgrade"), al_profiles.resolve("appsource")
    assert al_profiles.upgrade_failures(al_upgrade.WARNING, up), "strict rejects WARNING"
    assert not al_profiles.upgrade_failures(al_upgrade.WARNING, ap), "none allows WARNING"
    assert al_profiles.upgrade_failures(al_upgrade.BREAKING, ap)
    assert not al_profiles.upgrade_failures(al_upgrade.DATA,
                                            al_profiles.resolve("internal"))


def test_a_policy_that_cannot_be_checked_demands_a_baseline():
    """"could not check" and "checked and clean" are different answers."""
    for n in ("upgrade", "appsource"):
        pol, needs = al_profiles.upgrade_policy(al_profiles.resolve(n))
        assert pol and needs, (n, pol, needs)
    for n in ("internal", "customer", "pte"):
        pol, needs = al_profiles.upgrade_policy(al_profiles.resolve(n))
        assert pol is None and not needs, (n, pol, needs)


def test_breaking_changes_is_no_longer_merely_declared():
    """AL-11 shipped this as unenforced policy; AL-7 is what makes it real."""
    assert "breaking_changes" not in dict(
        al_profiles.unenforced(al_profiles.resolve("upgrade")))
    assert "breaking_changes" not in dict(
        al_profiles.unenforced(al_profiles.resolve("appsource")))


def test_real_app_packages_round_trip():
    """The synthetic surfaces above prove the diff logic; this proves the extractor reads
    an actual .app."""
    apps = sorted(glob.glob("/mnt/rojaws/localDev/projects/*/*.app"))
    if not apps:
        return skip("upgrade extractor", "no built .app available")
    surf = al_upgrade.surface(apps[0])
    assert surf["objects"] and surf["version"], surf["path"]
    assert al_upgrade.diff(surf, surf) == [], "a package must not differ from itself"


# ─── AL-9: performance smells, reusable by alw / bcw / the reviewer ────────────

def test_calcfields_in_loop_names_the_actual_fix():
    rules = _sem("""codeunit 1 X
{
    procedure P()
    var
        Cust: Record Customer;
    begin
        if Cust.FindSet() then
            repeat
                Cust.CalcFields("Balance (LCY)");
            until Cust.Next() = 0;
    end;
}
""")
    assert "calcfields-without-autocalc" in rules, rules


def test_setautocalcfields_makes_calcfields_in_a_loop_correct():
    """The whole point of SetAutoCalcFields — flagging it anyway is a false positive on
    the very fix we recommend."""
    rules = _sem("""codeunit 1 X
{
    procedure P()
    var
        Cust: Record Customer;
    begin
        Cust.SetAutoCalcFields("Balance (LCY)");
        if Cust.FindSet() then
            repeat
                Cust.CalcFields("Balance (LCY)");
            until Cust.Next() = 0;
    end;
}
""")
    assert "calcfields-without-autocalc" not in rules, rules
    assert "db-call-in-loop" not in rules, "CalcFields is owned by the dedicated rule"


def test_temp_records_do_not_calculate_flowfields_against_the_database():
    rules = _sem("""codeunit 1 X
{
    procedure P()
    var
        TempCust: Record Customer temporary;
    begin
        if TempCust.FindSet() then
            repeat
                TempCust.CalcFields("Balance (LCY)");
            until TempCust.Next() = 0;
    end;
}
""")
    assert "calcfields-without-autocalc" not in rules, rules


def test_setcurrentkey_filter_mismatch_is_detected():
    rules = _sem("""codeunit 1 X
{
    procedure P()
    var
        Entry: Record "G/L Entry";
    begin
        Entry.SetCurrentKey("Entry No.");
        Entry.SetRange("Posting Date", 0D);
        if Entry.FindSet() then;
    end;
}
""")
    assert "setcurrentkey-filter-mismatch" in rules, rules


def test_a_qualified_field_reference_is_the_same_field():
    """`Rec."Applies-to ID"` and `"Applies-to ID"` are one field. Comparing the raw
    strings never matches, which invents a mismatch the code does not have."""
    assert al_semantics._args('SetCurrentKey("Employee No.", EmplLedgEntry."Applies-to ID")') \
        == ["employee no.", "applies-to id"]
    rules = _sem("""codeunit 1 X
{
    procedure P()
    var
        Entry: Record "Employee Ledger Entry";
    begin
        Entry.SetCurrentKey("Employee No.", Entry."Applies-to ID");
        Entry.SetRange("Applies-to ID", 'X');
        if Entry.FindSet() then;
    end;
}
""")
    assert "setcurrentkey-filter-mismatch" not in rules, rules


def test_httpclient_without_a_timeout_is_flagged():
    rules = _sem("""codeunit 1 X
{
    procedure P()
    var
        Client: HttpClient;
        Resp: HttpResponseMessage;
    begin
        Client.Get('https://x', Resp);
    end;
}
""")
    assert "httpclient-no-timeout" in rules, rules


def test_a_timeout_in_a_different_procedure_does_not_excuse_this_one():
    """A forward window running past the procedure end let a neighbouring procedure's
    Timeout suppress a real finding."""
    rules = _sem("""codeunit 1 X
{
    procedure Bad()
    var
        Client: HttpClient;
        Resp: HttpResponseMessage;
    begin
        Client.Get('https://x', Resp);
    end;

    procedure Good()
    var
        Client: HttpClient;
        Resp: HttpResponseMessage;
    begin
        Client.Timeout := 5000;
        Client.Get('https://x', Resp);
    end;
}
""")
    assert "httpclient-no-timeout" in rules, rules


def test_declared_type_separates_a_database_get_from_an_http_get():
    """`Cust.Get(...)` and `Client.Get(...)` are the same text and opposite findings."""
    rules = _sem("""codeunit 1 X
{
    procedure P()
    var
        Client: HttpClient;
        Resp: HttpResponseMessage;
        SalesLine: Record "Sales Line";
    begin
        if SalesLine.FindSet() then
            repeat
                Client.Get('https://x', Resp);
            until SalesLine.Next() = 0;
    end;
}
""")
    assert "http-in-loop" in rules, rules
    assert "db-call-in-loop" not in rules, "an HttpClient is not a database round trip"


def test_bcw_consumes_the_same_rules():
    """Acceptance criterion: alw, bcw and the reviewer share one rule set. bcw used to
    hand the analyst raw grep hits and ask it to judge which were inside a loop."""
    import importlib.util as _u
    spec = _u.spec_from_file_location("bc_collect", os.path.join(HERE, "bc_collect.py"))
    bc = _u.module_from_spec(spec)
    try:
        spec.loader.exec_module(bc)
    except SystemExit:
        pass
    d = tempfile.mkdtemp()
    try:
        os.makedirs(os.path.join(d, "src"))
        open(os.path.join(d, "app.json"), "w").write('{"id":"x","name":"N"}')
        open(os.path.join(d, "src", "a.al"), "w").write("""codeunit 50100 X
{
    procedure P()
    var
        Cust: Record Customer;
        SalesLine: Record "Sales Line";
    begin
        if SalesLine.FindSet() then
            repeat
                Cust.Get(SalesLine."Sell-to Customer No.");
            until SalesLine.Next() = 0;
    end;
}
""")
        res = bc.collect(d)
        assert res["semantics"], "the facts pack must carry deterministic findings"
        assert "al_semantics" in res["facts_md"]
        assert "db-call-in-loop" in res["facts_md"], "findings must reach the analyst"
    finally:
        shutil.rmtree(d)



# ─── AL-8: object / dependency graph ───────────────────────────────────────────

_GRAPH_SRC = {
    "Equip.Table.al":
        'table 50300 "My Equip"\n{\n    fields\n    {\n'
        '        field(1; "No."; Code[20]) { }\n    }\n}\n',
    "EquipExt.TableExt.al":
        'tableextension 50301 "My Cust Ext" extends Customer\n{\n    fields\n    {\n'
        '        field(50300; "Equip Count"; Integer) { }\n    }\n}\n',
    "EquipCard.Page.al":
        'page 50302 "My Equip Card"\n{\n    SourceTable = "My Equip";\n'
        '    PageType = Card;\n}\n',
    "Mgt.Codeunit.al":
        'codeunit 50303 "My Equip Mgt"\n{\n'
        '    [IntegrationEvent(false, false)]\n'
        '    procedure OnAfterRegister(var Equip: Record "My Equip")\n'
        '    begin\n    end;\n\n'
        '    procedure Register()\n    var\n'
        '        Equip: Record "My Equip";\n'
        '        SalesHeader: Record "Sales Header";\n'
        '    begin\n'
        '        Equip.Init();\n'
        '        Equip."No." := \'X\';\n'
        '        SalesHeader.Init();\n    end;\n}\n',
    "Subs.Codeunit.al":
        'codeunit 50304 "My Equip Subs"\n{\n'
        '    [EventSubscriber(ObjectType::Codeunit, Codeunit::"Sales-Post", '
        "'OnAfterPostSalesDoc', '', true, true)]\n"
        '    local procedure OnPosted(var SalesHeader: Record "Sales Header")\n'
        '    begin\n    end;\n}\n',
    "Tests.Codeunit.al":
        'codeunit 50305 "My Equip Tests"\n{\n    Subtype = Test;\n\n'
        '    [Test]\n    procedure TestRegister()\n    var\n'
        '        Mgt: Codeunit "My Equip Mgt";\n'
        '    begin\n        Mgt.Register();\n    end;\n}\n',
}


def _graph_project():
    d = tempfile.mkdtemp()
    os.makedirs(os.path.join(d, "src"))
    for name, body in _GRAPH_SRC.items():
        open(os.path.join(d, "src", name), "w").write(body)
    return d


def test_graph_captures_objects_and_relationships():
    d = _graph_project()
    try:
        g = al_graph.build(d, idx={})
        ids = {n["id"] for n in g["nodes"]}
        assert "table:my equip" in ids and "codeunit:my equip mgt" in ids, sorted(ids)
        rels = {(e["from"], e["to"], e["rel"]) for e in g["edges"]}
        assert ("tableextension:my cust ext", "table:customer", "extends") in rels, rels
        assert ("page:my equip card", "table:my equip", "uses-table") in rels, rels
        assert ("codeunit:my equip mgt", "table:my equip", "uses-table") in rels
        assert any(r == "publishes" for _, _, r in rels), "the IntegrationEvent is a node"
        assert any(r == "subscribes-to" for _, _, r in rels), rels
    finally:
        shutil.rmtree(d)


def test_graph_is_reproducible_and_does_not_touch_the_source():
    """Two acceptance criteria at once — and the second is why this only ever reads."""
    d = _graph_project()
    try:
        before = build_receipt.tree_hash(d)
        a = json.dumps(al_graph.build(d, idx={}), sort_keys=True)
        b = json.dumps(al_graph.build(d, idx={}), sort_keys=True)
        assert a == b, "same source must give the same graph"
        assert build_receipt.tree_hash(d) == before, "graph generation modified the tree"
    finally:
        shutil.rmtree(d)


def test_affected_by_walks_dependents_not_dependencies():
    """Direction is the easy thing to get backwards: impact walks edges BACKWARDS."""
    d = _graph_project()
    try:
        g = al_graph.build(d, idx={})
        aff = al_graph.affected_by(g, "My Equip")
        assert "page:my equip card" in aff and "codeunit:my equip mgt" in aff, aff
        dep = al_graph.depends_on(g, "My Equip")
        assert "page:my equip card" not in dep, (
            "a table does not depend on the page that shows it")
    finally:
        shutil.rmtree(d)


def test_graph_supports_test_selection():
    d = _graph_project()
    try:
        g = al_graph.build(d, idx={})
        assert al_graph.tests_for(g, "My Equip Mgt") == ["codeunit:my equip tests"]
        assert al_graph.tests_for(g, "My Cust Ext") == [], (
            "nothing covers it — that is 'untested', not 'passing'")
    finally:
        shutil.rmtree(d)


def test_external_references_resolve_against_symbols():
    """`Codeunit "Sales-Post"` becomes a real object with an id and a package, not a
    bare string."""
    if not REAL:
        return skip("graph symbols", "no .alpackages")
    d = _graph_project()
    try:
        g = al_graph.build(d, idx=real_index())
        sp = next((n for n in g["nodes"] if n["name"] == "Sales-Post"), None)
        assert sp and sp["obj_id"] == 80 and sp["package"], sp
        assert not sp["internal"], "a base-app codeunit is not part of this project"
    finally:
        shutil.rmtree(d)


def test_quoted_field_names_containing_dots_survive():
    """`"No."` is one of the commonest field names in BC. A namespace-stripper that splits
    on every dot turns it into an empty string, and the graph fills with junk nodes."""
    assert al_graph._unq('"No."') == "No."
    assert al_graph._unq('System.Azure.Storage."ABS Blob Client"') == "ABS Blob Client"
    assert al_graph._unq("Customer") == "Customer"
    d = _graph_project()
    try:
        g = al_graph.build(d, idx={})
        fields = [n for n in g["nodes"] if n["kind"] == "field"]
        assert fields, "field references should be nodes"
        assert all(n["name"] and not n["name"].endswith(".") or n["name"].endswith("No.")
                   for n in fields), [n["name"] for n in fields]
        assert any(n["name"].endswith("No.") for n in fields), [n["name"] for n in fields]
    finally:
        shutil.rmtree(d)


def test_symbol_names_ending_in_a_dot_survive_resolution():
    """BC ships objects called "Customer Templ. Mgt." — a name that legitimately ends in
    a dot. Treating a resolved symbol name as a namespaced reference splits it to nothing
    and puts a node called "" in the graph."""
    if not REAL:
        return skip("dotted symbol names", "no .alpackages")
    idx = real_index()
    rec = al_symbols.lookup_id(idx, "codeunit", 1381)
    assert rec and rec["name"].endswith("."), rec
    d = _graph_project()
    try:
        g = al_graph.build(d, idx=idx)
        assert not [n for n in g["nodes"] if not n["name"].strip()], (
            "nameless nodes: " + str([n["id"] for n in g["nodes"] if not n["name"].strip()]))
    finally:
        shutil.rmtree(d)


def test_graph_handles_a_project_with_no_symbols():
    d = _graph_project()
    try:
        g = al_graph.build(d, idx={})
        assert g["nodes"] and g["edges"], "an unresolved reference is still an edge"
    finally:
        shutil.rmtree(d)



# ─── AL-12: compiler-error knowledgebase ───────────────────────────────────────

def test_diagnostic_codes_normalise_consistently():
    """The same code arrives from SARIF ruleId, compiler stdout and hand-written config
    in three different shapes."""
    for raw in ("al0132", " AL0132 ", "error AL0132: 'Record X' does not contain",
                "src/A.al(1,1): error AL0132: x"):
        assert al_errors.normalise(raw) == "AL0132", raw
    assert al_errors.normalise("") == ""
    assert al_errors.codes_in(
        "error AL0282: a\nerror AL0133: b\nwarning AA0218: c\nerror AL0282: again") \
        == ["AL0282", "AL0133", "AA0218"], "first-seen order, deduplicated"


def test_known_errors_produce_targeted_context():
    log = ("src/A.al(12,9): error AL0282: event subscriber 'X' parameter 'Y' is not found\n"
           "src/A.al(20,9): error AL0133: cannot convert from InStream to OutStream")
    ctx = al_errors.context_for(log, bc_version=27)
    assert "AL0282" in ctx and "AL0133" in ctx, ctx
    assert "bind" in ctx.lower(), "the guidance itself must be present"


def test_the_kb_never_overrides_the_compiler():
    """Acceptance criterion. Guidance sits ALONGSIDE the diagnostic and says so."""
    ctx = al_errors.context_for("error AL0282: x", bc_version=27)
    assert "authority" in ctx.lower(), ctx
    assert al_errors.context_for("error ZZ9999: unknown to us", 27) == "", (
        "an undocumented diagnostic must produce silence, not padding")


def test_guidance_is_version_aware():
    """A rule introduced in BC24 must not be quoted at a BC14 target."""
    assert al_errors.lookup("AA0218", 27), "documented from BC24 onward"
    assert al_errors.lookup("AA0218", 14) is None, "must not apply to BC14"
    assert al_errors.lookup("AA0218") is not None, "unversioned lookup returns it"
    assert al_errors.lookup("AL0282", 14), "[all] applies everywhere"


def test_every_entry_is_evidence_linked():
    """Guidance without provenance is a guess in an authoritative voice — this project has
    already shipped one (an AL-SYNTAX rule claiming a cop enforced DataClassification)."""
    missing = [c for c in al_errors.known()
               if not (al_errors.lookup(c) or {}).get("evidence")]
    assert not missing, f"entries with no evidence: {missing}"


def test_every_entry_has_a_usable_shape():
    for c in al_errors.known():
        e = al_errors.lookup(c)
        assert e.get("meaning") and e.get("fix"), c
        assert e.get("category") in al_errors.CATEGORIES, (c, e.get("category"))
        rendered = al_errors.guidance(e)
        assert c in rendered and "fix:" in rendered, c


def test_error_profile_classification_comes_from_the_same_file():
    """One file states what a diagnostic MEANS and how it is COUNTED — they used to be
    two hardcoded lists free to drift apart."""
    import importlib.util as _u
    spec = _u.spec_from_file_location("error_profile",
                                      os.path.join(HERE, "error_profile.py"))
    ep = _u.module_from_spec(spec)
    try:
        spec.loader.exec_module(ep)
    except SystemExit:
        pass
    assert "AL0440" in ep.DUPLICATE_CODES, "KB category should reach error_profile"
    assert "AL0126" in ep.TYPE_CODES
    assert "AA0218" in ep.RULE_CODES
    # union, not replacement: codes the KB has no entry for must survive
    assert "AL0774" in ep.RULE_CODES, "legacy classification was dropped"
    assert "AL0264" in ep.DUPLICATE_CODES


def test_symbols_category_is_deliberately_not_a_classification_set():
    """AL0185/AL0132 are recognised by NAME_IN_MSG, which extracts the offending NAME.
    Bucketing them by code instead would lose that."""
    assert al_errors.category("AL0185") == "symbols"
    assert al_errors.category("AL0132") == "symbols"


def test_unknown_codes_get_no_guessed_category():
    assert al_errors.category("AL9999") is None
    assert al_errors.lookup("AL9999") is None


def test_context_is_capped_so_it_cannot_bury_the_compiler_output():
    log = "\n".join(f"error {c}: msg" for c in al_errors.known())
    ctx = al_errors.context_for(log, bc_version=27, limit=3)
    assert sum(ctx.count(f"### {c}") for c in al_errors.known()) == 3, ctx[:200]


def test_build_hints_combine_dynamic_and_kb_guidance():
    """known_fix_hints reads real parameter names out of THIS build; the KB adds static
    background for the rest. Both must appear, and neither replaces the compiler."""
    rb.PROJECT_ROOT = tempfile.mkdtemp()
    rb.AL_CTX = {"bc_version": 27}
    try:
        os.makedirs(os.path.join(rb.PROJECT_ROOT, "src"))
        log = ("error AL0282: event subscriber 'OnIns' parameter 'SalesHeader' is not "
               "found\nerror AL0133: cannot convert from InStream to OutStream\n"
               "OnAfterInsertEvent")
        out = rb.known_fix_hints(log)
        assert "RENAME the parameter" in out, "dynamic hint lost"
        assert "DIAGNOSTIC KNOWLEDGE" in out, "KB context lost"
    finally:
        shutil.rmtree(rb.PROJECT_ROOT, ignore_errors=True)



# ─── AL-10: test generation and targeted selection ─────────────────────────────

_GOOD_TEST = ('codeunit 139900 "My Tests"\n{\n    Subtype = Test;\n\n'
              '    var\n        LibraryAssert: Codeunit "Library Assert";\n\n'
              '    [Test]\n    procedure A()\n    begin\n'
              '        LibraryAssert.IsTrue(true, \'x\');\n    end;\n}\n')


def test_generated_output_must_be_a_test_codeunit():
    assert al_testgen.check_containment(_GOOD_TEST) == []


def test_a_generated_production_object_is_rejected_not_repaired():
    """A model asked for tests will cheerfully write the table it wants to test against.
    An extension growing an unreviewed production object is a supply-chain problem."""
    sneaky = 'table 50100 "Sneaky" { fields { field(1; A; Integer) { } } }\n' + _GOOD_TEST
    problems = al_testgen.check_containment(sneaky)
    assert problems and any("table" in p for p in problems), problems


def test_test_objects_may_not_take_production_ids():
    prod = _GOOD_TEST.replace("139900", "50100")
    problems = al_testgen.check_containment(prod)
    assert problems and any("id range" in p for p in problems), problems


def test_a_codeunit_without_subtype_test_is_rejected():
    """It would compile as production code and never run as a test."""
    notest = _GOOD_TEST.replace("    Subtype = Test;\n", "")
    problems = al_testgen.check_containment(notest)
    assert problems and any("Subtype" in p for p in problems), problems


def test_a_single_line_codeunit_is_not_rejected_for_the_wrong_reason():
    """Anchoring the Subtype check to line start rejected legal one-line codeunits while
    blaming a property that was right there."""
    one = ('codeunit 139900 "T" { Subtype = Test; [Test] procedure A() '
           'begin end; }')
    assert al_testgen.check_containment(one) == []


def test_empty_or_prose_output_is_rejected():
    assert al_testgen.check_containment("Here are some tests you could write!")
    assert al_testgen.check_containment("")


def test_generated_tests_are_clearly_marked():
    marked = al_testgen.mark_generated(_GOOD_TEST, "Thing.Codeunit.al")
    assert al_testgen.GENERATED_HEADER in marked
    assert "target: Thing.Codeunit.al" in marked
    d = tempfile.mkdtemp()
    try:
        path = al_testgen.write(d, "MyTests", marked)
        assert al_testgen.is_generated(path)
        # Normalise BOTH sides. The old form only normalised the needle, so it looked
        # for src\test inside a haystack that still read src/test — a Windows-only
        # failure invisible from Linux (reported from the Windows client 2026-09-01).
        assert os.path.normpath(al_testgen.TEST_DIR) in os.path.normpath(path), (
            "generated tests must be isolated in the test folder")
    finally:
        shutil.rmtree(d)


def test_write_refuses_content_containment_rejects():
    """The containment rule is the point of the module, not a suggestion to it — a caller
    cannot ask it to write a production object."""
    d = tempfile.mkdtemp()
    try:
        try:
            al_testgen.write(d, "Bad", 'table 50100 "X" { }')
            raise AssertionError("write accepted a table")
        except al_testgen.ContainmentError:
            pass
        assert not os.path.exists(os.path.join(d, al_testgen.TEST_DIR)) or \
            not os.listdir(os.path.join(d, al_testgen.TEST_DIR))
    finally:
        shutil.rmtree(d)


def test_proposal_is_rejected_without_writing_anything():
    """propose() never writes. Rejection has to happen before the filesystem is touched."""
    d = tempfile.mkdtemp()
    try:
        res = al_testgen.propose("x.al", "codeunit 1 X { }",
                                 runner=lambda p: 'table 50100 "Sneaky" { }')
        assert not res["ok"] and res["problems"]
        assert not os.path.exists(os.path.join(d, al_testgen.TEST_DIR))
    finally:
        shutil.rmtree(d)


def test_proposal_survives_a_fenced_response():
    res = al_testgen.propose("x.al", "codeunit 1 X { }",
                             runner=lambda p: "Here you go:\n```al\n" + _GOOD_TEST + "```\n")
    assert res["ok"], res["problems"]
    assert al_testgen.GENERATED_HEADER in res["source"]


def test_the_prompt_asks_for_more_than_the_happy_path():
    """A model left alone writes the case that already worked."""
    prompt = al_testgen.build_prompt("X", "codeunit 1 X { }")
    for want in ("boundary", "permissions", "idempotency", "empty", "posting failure",
                 "upgrade"):
        assert want in prompt.lower(), want
    assert "LibraryAssert: Codeunit" in prompt, (
        "an undeclared LibraryAssert is the commonest compile failure in generated tests")


def test_targeted_selection_uses_the_object_graph():
    d = _graph_project()
    try:
        sel, why = al_testgen.select_tests(d, "My Equip Mgt",
                                           graph=al_graph.build(d, idx={}))
        assert sel == ["codeunit:my equip tests"], (sel, why)
    finally:
        shutil.rmtree(d)


def test_no_coverage_is_reported_as_untested_not_as_nothing_to_do():
    d = _graph_project()
    try:
        sel, why = al_testgen.select_tests(d, "My Cust Ext",
                                           graph=al_graph.build(d, idx={}))
        assert sel == [] and "UNTESTED" in why, why
    finally:
        shutil.rmtree(d)


def test_an_empty_selection_runs_everything_rather_than_nothing():
    """Silently running NO tests would report a pass for an empty run."""
    d = _graph_project()
    try:
        assert al_testgen.codeunit_filter(d, [], graph=al_graph.build(d, idx={})) == "*"
        f = al_testgen.codeunit_filter(d, ["codeunit:my equip tests"],
                                       graph=al_graph.build(d, idx={}))
        assert f == "My Equip Tests", f
    finally:
        shutil.rmtree(d)


def test_targeted_filter_reaches_the_test_runner():
    d = tempfile.mkdtemp()
    try:
        os.makedirs(os.path.join(d, "src"))
        open(os.path.join(d, "src", "t.al"), "w").write(_GOOD_TEST)
        seen = []

        def runner(cmd):
            seen.append(cmd)
            return 0, "TOTAL: 2 tests, 2 passed, 0 failed"
        r = al_tests.run(d, "app", 27, runner=runner, codeunit="My Tests")
        assert "-codeunit" in seen[0] and "My Tests" in seen[0], seen[0]
        assert r["selection"] == "My Tests"
        seen.clear()
        al_tests.run(d, "app", 27, runner=runner)
        assert "-codeunit" not in seen[0], "no selection must run the whole suite"
    finally:
        shutil.rmtree(d)


def test_a_one_line_test_codeunit_is_still_a_test():
    """find_test_codeunits missing it reports the project as having NO tests — and
    no-tests passes. The failure direction matters: this must not silently disable them."""
    d = tempfile.mkdtemp()
    try:
        os.makedirs(os.path.join(d, "src"))
        open(os.path.join(d, "src", "t.al"), "w").write(
            'codeunit 139900 T { Subtype = Test; [Test] procedure A() begin end; }')
        assert len(al_tests.find_test_codeunits(os.path.join(d, "src"))) == 1
        r = al_tests.run(d, "app", 27,
                         runner=lambda c: (0, "TOTAL: 1 tests, 1 passed, 0 failed"))
        assert r["status"] == "passed", r
    finally:
        shutil.rmtree(d)


def test_missing_test_framework_is_detected_before_a_model_call():
    """Without it every generated test fails AL0185, and the cause looks like bad
    generation rather than a missing dependency."""
    d = tempfile.mkdtemp()
    try:
        open(os.path.join(d, "app.json"), "w").write('{"id":"x","name":"N"}')
        ok, why = al_testgen.test_framework_ready(d)
        assert not ok and "AL0185" in why, why
        open(os.path.join(d, "app.json"), "w").write(
            '{"id":"x","name":"N","dependencies":[{"id":"a","name":"Library Assert",'
            '"publisher":"Microsoft","version":"1.0.0.0"}]}')
        ok, why = al_testgen.test_framework_ready(d)
        assert ok, why
    finally:
        shutil.rmtree(d)



# ─── AL-14: project brain ──────────────────────────────────────────────────────

def _brain_project(extra_al=""):
    d = tempfile.mkdtemp()
    os.makedirs(os.path.join(d, "src"))
    open(os.path.join(d, "app.json"), "w").write(json.dumps({
        "id": "b1", "name": "Brain Probe", "publisher": "P", "version": "2.0.0.0",
        "runtime": "16.0", "application": "27.0.0.0", "target": "OnPrem"}))
    open(os.path.join(d, "src", "T.Table.al"), "w").write(
        'table 50300 "Brain Tbl"\n{\n    fields\n    {\n'
        '        field(1; "No."; Code[20]) { }\n    }\n}\n')
    open(os.path.join(d, "src", "C.Codeunit.al"), "w").write(
        'codeunit 50301 "Brain Mgt"\n{\n    procedure P()\n    var\n'
        '        Rec: Record "Brain Tbl";\n        Client: HttpClient;\n'
        '        Resp: HttpResponseMessage;\n    begin\n'
        '        Client.Get(\'https://x\', Resp);\n        Rec.Init();\n    end;\n}\n')
    if extra_al:
        open(os.path.join(d, "src", "Extra.Codeunit.al"), "w").write(extra_al)
    return d


def test_profile_is_generated_deterministically():
    """Same source, same profile, byte for byte — otherwise 'has this changed?' is
    unanswerable."""
    d = _brain_project()
    try:
        a = al_brain.to_yaml(al_brain.build(d))
        b = al_brain.to_yaml(al_brain.build(d))
        assert a == b, "two runs over identical source differed"
    finally:
        shutil.rmtree(d)


def test_profile_carries_no_timestamp():
    """A generation time would make every regeneration differ. Provenance is a tree hash
    plus the pipeline revision, which identify the inputs and do not drift on their own."""
    d = _brain_project()
    try:
        p = al_brain.build(d)
        gen = p["generated_from"]
        assert set(gen) == {"source_hash", "pipeline_rev", "project"}, gen
        assert not re.search(r"\d{4}-\d{2}-\d{2}", al_brain.to_yaml(p)), "date leaked in"
    finally:
        shutil.rmtree(d)


def test_profile_records_its_source_and_detects_staleness():
    d = _brain_project()
    try:
        al_brain.write(d)
        stale, why = al_brain.is_stale(d)
        assert not stale, why
        open(os.path.join(d, "src", "New.Codeunit.al"), "w").write(
            'codeunit 50302 "Later" { }\n')
        stale, why = al_brain.is_stale(d)
        assert stale and "changed" in why, why
    finally:
        shutil.rmtree(d)


def test_a_secret_in_the_source_refuses_the_profile():
    """Refusing beats redacting: a scrubbed profile looks clean while the secret stays in
    the repository, which is the worse outcome."""
    d = _brain_project(
        'codeunit 50302 "Leak"\n{\n    procedure P()\n    begin\n'
        "        Message('Bearer sk-proj-abc123def456ghi789jkl012mno345pqr678stu');\n"
        "    end;\n}\n")
    try:
        try:
            al_brain.build(d)
            raise AssertionError("a profile was generated over a live secret")
        except al_brain.SecretInProfile as e:
            assert "fix the source" in str(e), str(e)
    finally:
        shutil.rmtree(d)


def test_profile_regenerates_from_source_alone():
    """No hidden state: deleting the stored profile and rebuilding gives the same answer."""
    d = _brain_project()
    try:
        first = al_brain.to_yaml(al_brain.build(d))
        path = al_brain.write(d)
        os.remove(path)
        assert al_brain.to_yaml(al_brain.build(d)) == first
    finally:
        shutil.rmtree(d)


def test_profile_reports_the_facts_a_task_would_re_derive():
    d = _brain_project()
    try:
        p = al_brain.build(d)
        assert p["bc"]["version"] == 27 and p["bc"]["target"] == "OnPrem", p["bc"]
        assert p["app"]["publisher"] == "P" and p["app"]["version"] == "2.0.0.0"
        assert p["objects"]["table"]["count"] == 1
        assert p["objects"]["codeunit"]["count"] == 1
        assert "http" in p["integrations"], p["integrations"]
    finally:
        shutil.rmtree(d)


def test_fields_and_events_are_not_counted_as_objects():
    """They are graph nodes, not AL objects — counting them put "field 57" into a
    one-line project summary and crowded out the facts that matter."""
    d = _brain_project()
    try:
        p = al_brain.build(d)
        assert "field" not in p["objects"] and "event" not in p["objects"], p["objects"]
    finally:
        shutil.rmtree(d)


def test_coverage_of_nothing_is_not_a_hundred_percent():
    d = _brain_project()
    try:
        p = al_brain.build(d)
        assert p["tests"]["codeunits"] == 0
        assert p["tests"]["coverage"] in ("0%", "n/a"), p["tests"]
    finally:
        shutil.rmtree(d)


def test_integration_risk_rises_with_the_evidence_not_the_vocabulary():
    """An HttpClient with no timeout is a real hazard; merely having one is not the same
    thing."""
    d = _brain_project()
    try:
        p = al_brain.build(d)
        assert "http" in p["integrations"]
        assert p["risk"]["integration"] == "high", p["risk"]
        assert "httpclient-no-timeout" in p["advisories"], p["advisories"]
    finally:
        shutil.rmtree(d)


def test_prompt_context_stays_small_enough_to_include():
    """A profile that costs thousands of tokens is one nobody includes."""
    d = _brain_project()
    try:
        ctx = al_brain.as_prompt_context(al_brain.build(d))
        assert len(ctx) < 900, len(ctx)
        for want in ("BC 27", "objects:", "risk:"):
            assert want in ctx, (want, ctx)
    finally:
        shutil.rmtree(d)


def test_the_profile_is_off_by_default_in_the_build():
    """It adds ~500 chars to every coder prompt. A previous injection-budget change
    silently evicted a knowledge topic and took the benchmark control from 2/3 to 0/3, so
    this ships opt-in and is measured before it becomes a default."""
    assert rb.AL_BRAIN is False, "AL_BRAIN must default to off"



# ─── AL-15: model capability by failure class ──────────────────────────────────

def _metrics(rows):
    d = tempfile.mkdtemp()
    path = os.path.join(d, "m.jsonl")
    with open(path, "w") as f:
        for r in rows:
            f.write(json.dumps(r) + "\n")
    return d, path


def _run(model, first_pass=False, diags=None, codes=None, **kw):
    r = {"coder_model": model, "first_pass_compile": first_pass,
         "final_compile": kw.pop("final", True), "fix_rounds": kw.pop("rounds", 1)}
    if diags:
        r["first_pass_diagnostics"] = diags
    if codes:
        r["first_pass_codes"] = codes
    r.update(kw)
    return r


def test_failure_classes_are_counted_from_both_evidence_generations():
    """Coarse buckets sit on ~240 historical runs; exact codes arrived later. Dropping
    the old evidence because something better exists would throw away the sample."""
    d, path = _metrics(
        [_run("A", diags={"missing-symbols": 2}) for _ in range(10)]
        + [_run("B", codes=["AL0282"]) for _ in range(10)])
    try:
        prof = al_capability.profile([path])
        assert prof["A"]["classes"]["api_hallucination"]["affected_pct"] == 100
        assert prof["B"]["classes"]["event_hallucination"]["affected_pct"] == 100
    finally:
        shutil.rmtree(d)


def test_rates_are_conditioned_on_runs_that_could_show_the_failure():
    """The correction that mattered. A model dying at syntax never reaches the point
    where an API can be hallucinated; scoring it over ALL runs made the worst model look
    best on the classes it never got to."""
    rows = ([_run("A", first_pass=True) for _ in range(90)]
            + [_run("A", diags={"missing-symbols": 1}) for _ in range(10)])
    d, path = _metrics(rows)
    try:
        prof = al_capability.profile([path])
        assert prof["A"]["runs"] == 100 and prof["A"]["observed_runs"] == 10
        assert prof["A"]["classes"]["api_hallucination"]["affected_pct"] == 100, (
            "10 of 10 OBSERVED runs hallucinated an API — not 10 of 100")
    finally:
        shutil.rmtree(d)


def test_every_rate_travels_with_its_population():
    d, path = _metrics([_run("A", diags={"syntax": 1}) for _ in range(9)])
    try:
        s = al_capability.profile([path])["A"]
        assert s["runs"] == 9 and s["observed_runs"] == 9
        assert s["classes"]["syntax_break"]["runs_affected"] == 9
    finally:
        shutil.rmtree(d)


def test_thin_evidence_produces_no_recommendation():
    """A routing table built on three runs is worse than none: it looks like knowledge."""
    d, path = _metrics([_run("A", diags={"missing-symbols": 1}),
                        _run("B", diags={"syntax": 1})])
    try:
        model, why = al_capability.recommend(al_capability.profile([path]), "api")
        assert model is None and "INSUFFICIENT EVIDENCE" in why, why
    finally:
        shutil.rmtree(d)


def test_a_single_eligible_model_is_a_default_not_a_choice():
    d, path = _metrics([_run("A", diags={"missing-symbols": 1}) for _ in range(20)])
    try:
        model, why = al_capability.recommend(al_capability.profile([path]), "api")
        assert model is None and "nothing to compare" in why, why
    finally:
        shutil.rmtree(d)


def test_a_close_result_is_not_routed_on():
    d, path = _metrics(
        [_run("A", diags={"missing-symbols": 1}) for _ in range(10)]
        + [_run("A", diags={"syntax": 1}) for _ in range(10)]
        + [_run("B", diags={"missing-symbols": 1}) for _ in range(11)]
        + [_run("B", diags={"syntax": 1}) for _ in range(9)])
    try:
        model, why = al_capability.recommend(al_capability.profile([path]), "api")
        assert model is None and "NO CLEAR WINNER" in why, why
    finally:
        shutil.rmtree(d)


def test_a_clear_difference_is_routed_on():
    """The refusals above must not be refusals in all cases — a real gap has to surface."""
    d, path = _metrics(
        [_run("Good", diags={"syntax": 1}) for _ in range(20)]
        + [_run("Bad", diags={"missing-symbols": 1, "type-mismatch": 1}) for _ in range(20)])
    try:
        model, why = al_capability.recommend(al_capability.profile([path]), "api")
        assert model == "Good", (model, why)
        assert "0%" in why or "against" in why, why
    finally:
        shutil.rmtree(d)


def test_unknown_task_kind_is_refused():
    d, path = _metrics([_run("A", diags={"syntax": 1}) for _ in range(20)])
    try:
        model, why = al_capability.recommend(al_capability.profile([path]), "telepathy")
        assert model is None and "unknown task kind" in why
    finally:
        shutil.rmtree(d)


def test_unmeasured_models_are_excluded_not_ranked_last():
    """An unmeasured model is not a good one."""
    d, path = _metrics([_run("Big", diags={"syntax": 1}) for _ in range(20)]
                       + [_run("Tiny", diags={"syntax": 1})])
    try:
        prof = al_capability.profile([path])
        assert "Tiny" in prof, "it must still appear in the report"
        ranked = [m for m, _pct, _n in al_capability.rank(prof, "syntax_break")]
        assert "Tiny" not in ranked, "and must not be rankable"
    finally:
        shutil.rmtree(d)


def test_tests_and_passes_are_different_populations():
    """A project with no tests is neither a pass nor a failure and must dilute neither."""
    d, path = _metrics([_run("A", tests_status="passed"),
                        _run("A", tests_status="failed"),
                        _run("A", tests_status="no-tests"),
                        _run("A")])
    try:
        s = al_capability.profile([path])["A"]
        assert s["tests_runs"] == 2 and s["tests_pass_pct"] == 50, s
    finally:
        shutil.rmtree(d)


def test_report_states_plainly_when_nothing_is_routable():
    d, path = _metrics([_run("A", diags={"syntax": 1}), _run("B", diags={"syntax": 1})])
    try:
        text = al_capability.report(al_capability.profile([path]))
        assert "No routing is justified" in text, text[:400]
    finally:
        shutil.rmtree(d)


def test_report_carries_the_early_failure_caveat():
    """The confound has to be stated where the numbers are read, not just understood by
    whoever wrote the tool."""
    d, path = _metrics([_run("A", diags={"syntax": 1}) for _ in range(10)])
    try:
        text = al_capability.report(al_capability.profile([path]))
        assert "never reaches" in text and "OBSERVED" in text, text[:400]
    finally:
        shutil.rmtree(d)



# ─── AL-16: temporal / versioned knowledge ─────────────────────────────────────

def test_introduced_and_removed_bound_applicability():
    m = {"introduced_bc": 17, "removed_bc": 26}
    assert al_temporal.applies(m, 20)[0]
    assert not al_temporal.applies(m, 16)[0]
    assert not al_temporal.applies(m, 26)[0], "removed_bc is the version it is GONE in"
    assert al_temporal.applies(m, None)[0], "no target means no filtering"


def test_runtime_bounds_are_honoured():
    m = {"runtime_from": "11.0", "runtime_to": "16.0"}
    assert al_temporal.applies(m, None, "13.0")[0]
    assert not al_temporal.applies(m, None, "10.0")[0]
    assert not al_temporal.applies(m, None, "17.0")[0]


def test_deprecated_still_applies_but_warns():
    """Suppressing a deprecated item removes the only warning the reader would get."""
    m = {"deprecated_bc": 25}
    assert al_temporal.applies(m, 27)[0], "deprecated code still compiles"
    assert al_temporal.is_deprecated(m, 27)
    assert "DEPRECATED" in al_temporal.scope_note(m, 27)


def test_legacy_range_forms_still_work_unchanged():
    """The KBs already use these; nothing should need rewriting to gain temporal fields."""
    for spec, bc, want in ((["all"], 27, True), (["16.."], 27, True), (["16.."], 14, False),
                           (["26..28"], 27, True), (["26..28"], 29, False),
                           ([26, 27, 28], 27, True), (["junk"], 27, True)):
        assert al_temporal.applies({"bc-version": spec}, bc)[0] is want, (spec, bc)


def test_a_version_scoped_item_is_labelled_not_just_filtered():
    """The failure the handover names: passing the filter silently presents a conditional
    rule as a universal one, and the next reader applies it to a project it was never
    true for."""
    assert al_temporal.scope_note({"bc-version": ["24.."]}) == "BC24 and later only"
    assert al_temporal.scope_note({"bc-version": ["26..28"]}) == "BC26–BC28 only"
    assert al_temporal.scope_note({"introduced_bc": 24}) == "BC24 and later only"
    assert al_temporal.scope_note({"bc-version": ["all"]}) == "", "universal stays silent"
    assert al_temporal.scope_note({}) == ""


def test_annotate_leaves_universal_items_untouched():
    txt = "Always use SetLoadFields."
    assert al_temporal.annotate(txt, {"bc-version": ["all"]}) == txt
    out = al_temporal.annotate(txt, {"introduced_bc": 17})
    assert "BC17 and later only" in out and txt in out


def test_only_a_declared_confidence_is_reported():
    """Emitting the default on every item adds a line to everything and so means nothing."""
    assert "confidence" not in al_temporal.scope_note({"introduced_bc": 24})
    assert "confidence low" in al_temporal.scope_note({"confidence": "low",
                                                       "source": "a blog post"})
    assert "confidence" not in al_temporal.scope_note({"confidence": "verified"}), (
        "a verified item needs no caveat")


def test_select_returns_why_things_were_dropped():
    """"no rules matched" and "eleven were filtered out by a version you set wrong" look
    identical from the outside unless the reasons come back."""
    items = [{"id": "a", "bc-version": ["all"]},
             {"id": "b", "introduced_bc": 26},
             {"id": "c", "confidence": "low"}]
    kept, dropped = al_temporal.select(items, bc_version=14)
    assert [k["id"] for k in kept] == ["a", "c"], kept
    assert dropped and dropped[0][0]["id"] == "b" and "introduced" in dropped[0][1]
    kept, dropped = al_temporal.select(items, bc_version=27, min_confidence="high")
    assert [k["id"] for k in kept] == ["a", "b"], kept
    assert any("confidence low" in why for _it, why in dropped), dropped


def test_frontmatter_parses_from_a_real_knowledge_file():
    d = tempfile.mkdtemp()
    try:
        f = os.path.join(d, "k.md")
        open(f, "w").write("---\nbc-version: [24..]\nintroduced_bc: 24\n"
                           "confidence: verified\n---\n\n# Rule\n")
        meta = al_temporal.parse_frontmatter(open(f).read())
        assert meta["introduced_bc"] == 24 and meta["confidence"] == "verified"
        assert al_temporal.parse_frontmatter("# no frontmatter") == {}
    finally:
        shutil.rmtree(d)


def test_bcquality_and_al_errors_share_one_temporal_model():
    """One model, every KB — a second copy would drift, and the version filter has been
    wrong once already."""
    import importlib.util as _u
    spec = _u.spec_from_file_location("bcquality", os.path.join(HERE, "bcquality.py"))
    bq = _u.module_from_spec(spec)
    try:
        spec.loader.exec_module(bq)
    except SystemExit:
        pass
    for s_, bc, want in ((["16.."], 27, True), (["16.."], 14, False), (["all"], 14, True)):
        assert bq.version_matches(s_, bc) is want, (s_, bc)
        assert al_temporal.applies({"bc-version": s_}, bc)[0] is want


def test_diagnostic_guidance_carries_its_applicability():
    e = al_errors.lookup("AA0218", 27)
    assert e, "AA0218 applies at BC27"
    assert "BC24 and later only" in al_errors.guidance(e), al_errors.guidance(e)
    assert al_errors.lookup("AA0218", 14) is None, "and is filtered out at BC14"
    plain = al_errors.guidance(al_errors.lookup("AL0282", 27))
    assert "applicability" not in plain, "an unscoped entry must gain no noise"


def test_probe_verified_entries_are_marked_as_such():
    """"verified by a compiler probe" and "seen in a blog post" are not the same claim,
    and this pipeline has already been burned treating one as the other."""
    verified = [c for c in al_errors.known()
                if str((al_errors.lookup(c) or {}).get("confidence", "")).lower() == "verified"]
    assert len(verified) >= 6, verified
    for c in verified:
        assert (al_errors.lookup(c) or {}).get("source"), f"{c} claims verified with no source"



# ─── AL-17: business-process / event-flow graph ────────────────────────────────

def _proc_project():
    d = tempfile.mkdtemp()
    os.makedirs(os.path.join(d, "src"))
    open(os.path.join(d, "src", "Setup.Table.al"), "w").write(
        'table 50400 "My Ext Setup"\n{\n    fields\n    {\n'
        '        field(1; "Primary Key"; Code[10]) { }\n    }\n}\n')
    open(os.path.join(d, "src", "Post.Codeunit.al"), "w").write(
        'codeunit 50401 "My Post Handler"\n{\n'
        '    [EventSubscriber(ObjectType::Codeunit, Codeunit::"Sales-Post", '
        "'OnAfterPostSalesDoc', '', true, true)]\n"
        '    local procedure OnPosted(var SalesHeader: Record "Sales Header")\n'
        '    var\n        Setup: Record "My Ext Setup";\n'
        '        Client: HttpClient;\n    begin\n        Setup.Get();\n    end;\n}\n')
    open(os.path.join(d, "src", "Install.Codeunit.al"), "w").write(
        'codeunit 50402 "My Ext Install"\n{\n    SubType = Install;\n\n'
        '    procedure P()\n    var\n        Setup: Record "My Ext Setup";\n'
        '    begin\n        Setup.Init();\n    end;\n}\n')
    return d


def test_objects_are_placed_into_business_stages():
    d = _proc_project()
    try:
        p = al_process.build(d, graph=al_graph.build(d, idx={}))
        stages = {o["name"]: o["stage"] for o in p["objects"].values()}
        assert stages["My Ext Setup"] == "setup", stages
        assert stages["Sales-Post"] == "posting", stages
        assert stages["Sales Header"] == "document", stages
    finally:
        shutil.rmtree(d)


def test_a_stated_subtype_beats_a_name_match():
    """A codeunit called "Sales Setup Upgrade" is upgrade code whatever else its name
    contains — Subtype is a fact, a name is a hint."""
    d = _proc_project()
    try:
        p = al_process.build(d, graph=al_graph.build(d, idx={}))
        o = next(o for o in p["objects"].values() if o["name"] == "My Ext Install")
        assert o["stage"] == "install_upgrade" and "Subtype" in o["matched"], o
    finally:
        shutil.rmtree(d)


def test_unrecognised_objects_are_reported_not_dropped():
    """A process map that quietly drops what it did not recognise looks complete and is
    not — worse than a map with a visible gap."""
    d = tempfile.mkdtemp()
    try:
        os.makedirs(os.path.join(d, "src"))
        open(os.path.join(d, "src", "X.Codeunit.al"), "w").write(
            'codeunit 50410 "Zzz Widget Frobnicator" { }\n')
        p = al_process.build(d, graph=al_graph.build(d, idx={}))
        assert "Zzz Widget Frobnicator" in p["unclassified"], p["unclassified"]
        assert p["objects"]["codeunit:zzz widget frobnicator"]["stage"] == "unclassified"
    finally:
        shutil.rmtree(d)


def test_every_classification_carries_the_token_that_caused_it():
    """So a wrong stage can be traced to the word that produced it rather than argued
    about."""
    d = _proc_project()
    try:
        p = al_process.build(d, graph=al_graph.build(d, idx={}))
        for o in p["objects"].values():
            if o["stage"] != "unclassified":
                assert o["matched"], o
    finally:
        shutil.rmtree(d)


def test_longest_vocabulary_match_wins():
    """"Posted Sales Invoice Header" is a posted document, not master data because it
    happens to contain "sales"."""
    assert al_process._classify_name("Posted Sales Invoice Header")[0] == "posted_document"
    assert al_process._classify_name("Cust. Ledger Entry")[0] == "ledger"
    assert al_process._classify_name("Job Queue Entry")[0] == "background"


def test_event_impact_answers_what_a_change_affects():
    d = _proc_project()
    try:
        g = al_graph.build(d, idx={})
        res = al_process.event_impact(d, "OnAfterPostSalesDoc", g)
        assert res["found"], res
        assert "My Post Handler" in res["subscribers"], res
        assert res["affects_stages"], res
    finally:
        shutil.rmtree(d)


def test_event_impact_says_so_when_the_event_is_absent():
    d = _proc_project()
    try:
        res = al_process.event_impact(d, "OnNothingAtAll", al_graph.build(d, idx={}))
        assert not res["found"] and "no publisher or subscriber" in res["detail"]
    finally:
        shutil.rmtree(d)


def test_triggers_of_finds_where_a_stage_is_reached_from():
    d = _proc_project()
    try:
        res = al_process.triggers_of(d, "setup", al_graph.build(d, idx={}))
        assert res["found"], res
        flat = " ".join(n for names in res["triggered_from"].values() for n in names)
        assert "My Ext Install" in flat, res
    finally:
        shutil.rmtree(d)


def test_queries_report_an_empty_stage_rather_than_an_empty_answer():
    d = _proc_project()
    try:
        g = al_graph.build(d, idx={})
        for fn in (al_process.triggers_of, al_process.integrations_from):
            res = fn(d, "ledger", g)
            assert not res["found"] and "ledger" in res["detail"], res
    finally:
        shutil.rmtree(d)


def test_flows_keep_a_witness_edge():
    """A stage-to-stage arrow has to be traceable back to the code that justifies it."""
    d = _proc_project()
    try:
        p = al_process.build(d, graph=al_graph.build(d, idx={}))
        assert p["flows"], "expected at least one cross-stage flow"
        for f in p["flows"]:
            assert f["via"] and "-->" in f["via"][0], f
    finally:
        shutil.rmtree(d)


# ─── al_graph defects that AL-17 surfaced ──────────────────────────────────────

def test_permission_set_entries_are_not_objects():
    """A permission-set BODY references objects without an id (`page "Name";`). Matching
    those pulled whole mangled lines into the graph as if they were declarations."""
    d = tempfile.mkdtemp()
    try:
        os.makedirs(os.path.join(d, "src"))
        open(os.path.join(d, "src", "P.PermissionSet.al"), "w").write(
            'permissionset 50420 "My PS"\n{\n    Assignable = true;\n'
            '    Permissions = tabledata "My Tbl" = RIMD,\n'
            '        page "My Page" = X;\n}\n')
        g = al_graph.build(d, idx={})
        names = {n["name"] for n in g["nodes"] if n.get("internal")}
        assert names == {"My PS"}, names
    finally:
        shutil.rmtree(d)


def test_objects_without_an_id_are_still_captured():
    """interface, controladdin, profile and pagecustomization have no object id.
    Requiring one silently dropped every control add-in from the graph."""
    d = tempfile.mkdtemp()
    try:
        os.makedirs(os.path.join(d, "src"))
        open(os.path.join(d, "src", "I.Interface.al"), "w").write(
            'interface "My Iface"\n{\n    procedure Go();\n}\n')
        open(os.path.join(d, "src", "A.ControlAddIn.al"), "w").write(
            'controladdin MyAddin\n{\n    Scripts = \'x.js\';\n}\n')
        g = al_graph.build(d, idx={})
        kinds = {n["kind"] for n in g["nodes"] if n.get("internal")}
        assert kinds == {"interface", "controladdin"}, kinds
    finally:
        shutil.rmtree(d)


def test_an_implements_target_is_an_interface_not_the_implementer_kind():
    """One interface appeared three times — as a codeunit, an enum and an interface —
    because the target was typed as the kind of whatever implemented it."""
    d = tempfile.mkdtemp()
    try:
        os.makedirs(os.path.join(d, "src"))
        open(os.path.join(d, "src", "I.Interface.al"), "w").write(
            'interface "My Iface"\n{\n    procedure Go();\n}\n')
        open(os.path.join(d, "src", "C.Codeunit.al"), "w").write(
            'codeunit 50430 "Impl A" implements "My Iface"\n{\n'
            '    procedure Go() begin end;\n}\n')
        open(os.path.join(d, "src", "E.Enum.al"), "w").write(
            'enum 50431 "My Kind" implements "My Iface"\n{\n'
            '    value(0; A) { Implementation = "My Iface" = "Impl A"; }\n}\n')
        g = al_graph.build(d, idx={})
        iface = [n["id"] for n in g["nodes"] if n["name"] == "My Iface"]
        assert iface == ["interface:my iface"], iface
        assert any(e["rel"] == "implements" for e in g["edges"]), g["edges"]
    finally:
        shutil.rmtree(d)


# ─── topic injection: the search trigger ───────────────────────────────────────

def test_search_topic_fires_only_on_real_search_work():
    """A bare \\bsearch\\b would fire on ordinary prose and spend 2.3k of a 14k budget on
    every unrelated build — the shape of the regression that evicted 02-objects and took
    the benchmark control from 2/3 to 0/3."""
    T = "25-search-relational-full-text-semantic-al"
    for text in ("build a table and a card page for equipment",
                 "the user can search the ledger for a customer",
                 "add a factbox showing the customer address"):
        got, _ = rb.select_topics(["src/X.Codeunit.al"], text)
        assert T not in got, (text, got)
    for text in ("add semantic search over the item description",
                 "enable full-text filtering on Description",
                 "set OptimizeForTextSearch on the field"):
        got, _ = rb.select_topics(["src/X.Codeunit.al"], text)
        assert T in got, (text, got)


def test_search_topic_stays_inside_the_injection_budget():
    got, used = rb.select_topics(["src/X.Codeunit.al"],
                                 "add semantic search over the item description")
    assert used <= rb.INJECT_BUDGET_K, (used, rb.INJECT_BUDGET_K)
    # and the always-on core is not displaced by it
    for core in ("00-gotchas", "01-syntax-style"):
        assert core in got, got


def test_bench_fixtures_are_unaffected_by_the_search_trigger():
    """The control run proves no regression empirically; this pins it cheaply."""
    import glob as _g
    for h in _g.glob("/mnt/rojaws/localDev/projects/*/larry-handover.prompt.md"):
        text = open(h, encoding="utf-8", errors="replace").read()
        got, used = rb.select_topics(["src/X.Table.al"], text)
        assert "25-search-relational-full-text-semantic-al" not in got, h
        assert used <= rb.INJECT_BUDGET_K, (h, used)


# ─── topic injection: budget eviction (2026-08-29) ─────────────────────────────
#
# Observed in production: all four locked fixtures injected a BYTE-IDENTICAL topic set
# (00-gotchas, 01-syntax-style, 02-objects, 07-events-errors, ~13.5k) despite being a CRUD
# app, a controladdin map, a booking extension and an Azure Blob integration. Two causes,
# compounding — a first-come budget that silently evicted, and a selector fed text the
# pipeline had itself appended. doclink asked for 08-data-storage on hard evidence, lost it
# to the cap without a word, and failed on the ABS API errors that topic covers.

def _fixture(name):
    root = "/mnt/rojaws/localDev/projects/" + name
    h = os.path.join(root, "larry-handover.prompt.md")
    if not os.path.exists(h):
        return None, None
    rb.configure_project(root)
    return rb.EXPECTED_FILES, open(h, encoding="utf-8", errors="replace").read()


def test_narrow_evidence_survives_the_budget_cap():
    """doclink names Azure blobs in its own spec. Pre-change the always-on topics ate
    13.56k of a 14k budget and 08-data-storage (1.58k) was dropped in silence."""
    files, text = _fixture("tsg-document-link-2-az-storage")
    if not files:
        SKIPPED.append("test_narrow_evidence_survives_the_budget_cap (no doclink fixture)")
        return
    got, used = rb.select_topics(files, text)
    assert "08-data-storage" in got, got
    assert used <= rb.INJECT_BUDGET_K, (used, rb.INJECT_BUDGET_K)
    for core in ("00-gotchas", "01-syntax-style", "02-objects"):
        assert core in got, (core, got)


def test_an_azure_project_and_a_map_project_get_different_topics():
    """The regression signal, aimed at a pair that really did collide.

    Careful about which pair: on RAW specs p1 already differed from the rest pre-change, so
    a "not all four are equal" assertion holds either way and guards nothing. doclink vs map
    is the honest test — both resolved to the identical 4-topic set before this change, and
    doclink's Azure evidence is exactly what the cap was eating."""
    dl_files, dl_text = _fixture("tsg-document-link-2-az-storage")
    mp_files, mp_text = _fixture("tsg-map-integration")
    if not dl_files or not mp_files:
        SKIPPED.append("test_an_azure_project_and_a_map_project_get_different_topics (fixtures absent)")
        return
    doclink = rb.select_topics(dl_files, dl_text)[0]
    mapping = rb.select_topics(mp_files, mp_text)[0]
    assert doclink != mapping, f"both fixtures got the same topics: {doclink}"


def test_evicted_topics_are_reported_not_dropped_in_silence():
    """A quiet drop is the defect. The selection being correct is worth nothing if the
    eviction is invisible in the log."""
    import io
    from contextlib import redirect_stdout
    files, text = _fixture("bench-p4-unseen")
    if not files:
        SKIPPED.append("test_evicted_topics_are_reported_not_dropped_in_silence (no p4)")
        return
    buf = io.StringIO()
    with redirect_stdout(buf):
        got, _ = rb.select_topics(files, text)
    out = buf.getvalue()
    dropped = [t for t in ("03-records-performance", "09-api-web") if t not in got]
    if not dropped:
        SKIPPED.append("test_evicted_topics_are_reported_not_dropped_in_silence (nothing evicted)")
        return
    assert "DROPPED" in out, out
    for t in dropped:
        assert t in out, (t, out)


def test_topic_choice_ignores_text_the_pipeline_appends():
    """bench-p1-crud is plain CRUD — its spec never mentions an event. BCQuality appends
    ~7.8k of rule prose that does, which flipped the event regex true and spent 4.22k on
    07-events-errors. Text WE append is not evidence about the project.

    FORWARD guard, not a regression catcher — it passes against the pre-change code too,
    because select_topics always scored whatever it was handed and the defect was at the
    call site (covered by the wiring test below). It exists so that anyone who later makes
    the selector re-read the built prompt has to delete an assertion that says why not."""
    files, text = _fixture("bench-p1-crud")
    if not files:
        SKIPPED.append("test_topic_choice_ignores_text_the_pipeline_appends (no p1)")
        return
    clean, _ = rb.select_topics(files, text)
    assert "08-data-storage" not in clean, clean
    # Blob/azure rather than events, because the topic must FIT for the selection to move.
    # This asserted on 07-events-errors until 2026-09-01, when 01-syntax-style grew by 0.46k
    # and pushed 07 (4.22k) out of p1's 14k budget by 0.02k — the test then could not move
    # the selection at all and said so. 08-data-storage is 1.58k and leaves headroom.
    appended = text + ("\n\n## Authoring rules\n"
                       "[rule:x] Stream the azure blob into a Temp Blob before reading it.\n")
    dirty, _ = rb.select_topics(files, appended)
    assert dirty != clean, ("appended text did not move the selection — this test can no "
                            "longer detect the contamination it exists to catch")
    assert "08-data-storage" in dirty, dirty


def test_selection_never_exceeds_what_ctx_guard_will_keep():
    """The two-budget defect, 2026-08-30.

    INJECT_BUDGET_K capped SELECTION; ctx_budget_k() caps the assembled PROMPT and trims
    from the tail. They did not know about each other, so raising INJECT_BUDGET_K to 16 made
    doclink select five topics (15.0k) that ctx-guard then cut back to four — and a
    budget-14-vs-16 A/B ran the identical configuration in both arms, returning U=50.0 of
    100. A thing compared to itself, reported as a null.

    Invariant: whatever selection returns must still fit once the rest of the prompt is
    counted, so ctx-guard has nothing left to do."""
    files, spec = _fixture("tsg-document-link-2-az-storage")
    if not files:
        SKIPPED.append("test_selection_never_exceeds_what_ctx_guard_will_keep (no doclink)")
        return
    try:
        import bcquality
        guide = bcquality.coder_checklist(spec, bc_version=rb.AL_CTX.get("bc_version")) or ""
    except Exception:
        guide = ""
    assembled = spec + "\n\n" + guide
    non_inject = len(assembled) / 3700.0
    headroom = rb.ctx_budget_k() - non_inject

    old = rb.INJECT_BUDGET_K
    try:
        for raised in (14, 16, 24):        # 16 is the arm that silently collapsed
            rb.INJECT_BUDGET_K = raised
            _, used = rb.select_topics(files, spec, budget_k=headroom)
            assert non_inject + used <= rb.ctx_budget_k(), (
                f"INJECT_BUDGET_K={raised}: prompt {non_inject + used:.1f}k exceeds "
                f"ctx budget {rb.ctx_budget_k():.1f}k — ctx-guard would trim the selection")
    finally:
        rb.INJECT_BUDGET_K = old


def test_ctx_headroom_can_bind_tighter_than_the_configured_budget():
    """doclink carries ~7.9k of handover+BCQuality, leaving ~11.7k — so INJECT_BUDGET_K=14
    was never once reachable on that fixture. The caller must pass the smaller number."""
    files, spec = _fixture("tsg-document-link-2-az-storage")
    if not files:
        SKIPPED.append("test_ctx_headroom_can_bind_tighter_than_the_configured_budget (no doclink)")
        return
    generous, _ = rb.select_topics(files, spec, budget_k=99.0)
    tight, _ = rb.select_topics(files, spec, budget_k=4.0)
    assert len(tight) < len(generous), (tight, generous)
    assert "00-gotchas" in tight, tight


def test_a_wedged_write_is_abandoned_not_repeated():
    """2026-08-30: pi hung at 0.4% CPU in epoll_wait, wrote 0/9 files and never exited.
    run-build retried it twice more, identically, for 3600s total — one wedge became a
    two-hour hole in a suite."""
    assert rb.wedged_write(0, True, 1, max_attempts=3)
    assert rb.wedged_write(0, True, 2, max_attempts=3)


def test_only_a_timeout_with_nothing_written_counts_as_wedged():
    """Narrow on purpose. Retries exist for the transient cases and must survive."""
    # cut off mid-write: it was running, a retry recovers
    assert not rb.wedged_write(4, True, 1, max_attempts=3)
    assert not rb.wedged_write(1, True, 1, max_attempts=3)
    # failed fast with nothing: the transient this loop was built for
    assert not rb.wedged_write(0, False, 1, max_attempts=3)
    # last attempt: the loop ends anyway, so don't claim to have saved anything
    assert not rb.wedged_write(0, True, 3, max_attempts=3)


def test_the_write_loop_actually_consults_the_wedge_check():
    """Wiring guard: the predicate is worthless if the loop still calls run_coder three
    times regardless. Structural because the loop only runs inside a real build."""
    src = open(os.path.join(HERE, "run-build.py"), encoding="utf-8").read()
    assert "if wedged_write(written, coder.LAST[\"timed_out\"], attempt):" in src, \
        "the write-retry loop is not consulting wedged_write"
    # and the flag must be cleared per call, or one timeout latches every later attempt.
    # Cleared in two places on purpose: coder.run_pi clears it at the spawn, and run_coder
    # clears it before dispatch so a backend that never reports a timeout reads as False.
    assert 'coder.LAST["timed_out"] = False' in src, "timed_out is never reset by run_coder"
    csrc = open(os.path.join(HERE, "coder.py"), encoding="utf-8").read()
    assert 'LAST["timed_out"] = False' in csrc, "timed_out is never reset at the spawn"


def test_every_agent_spawn_pins_stdin():
    """The pi wedge (8eb6f67): pi registers fd 0 in its event loop and waits on it, so an
    inherited descriptor with no data and no EOF parks it before it opens a connection.

    Checked across ALL pipelines, not just run-build.py — run-build-go.py and
    run-build-cs.py carry their own copies of run_pi, and both had the same bug. The go/cs
    suite lost b64forward to a full 1200s write timeout because of it. A per-file fix that
    leaves a copy unpatched is how this survives."""
    import glob as _g
    missing = []
    for path in _g.glob(os.path.join(HERE, "run-build*.py")) + [
            os.path.join(HERE, "claude_egress.py")]:
        src = open(path, encoding="utf-8").read()
        for m in re.finditer(r"subprocess\.run\((.{0,220}?)\)\n", src, re.S):
            call = m.group(1)
            # only the long-running agent spawns matter; short tool calls that write and
            # close stdin (input=...) already get EOF
            if ("cmd" in call and "capture_output" in call and "timeout=" in call
                    and "input=" not in call and "stdin=" not in call):
                missing.append((os.path.basename(path), call.split(",")[0].strip()))
    assert not missing, f"agent spawn without stdin pinned: {missing}"


# ─── bonsai: a build must give the card back ───────────────────────────────────

def test_sigterm_runs_the_exit_handlers():
    """`timeout` sends SIGTERM and Python does NOT run atexit on a signal death — it dies in
    the C handler. Every build is wrapped in `timeout`, and bench-run-suite.sh wraps each run
    in `timeout 3600`, so any run hitting its cap skipped the bonsai restore and left the
    chat server down: the card was orphaned exactly when a build had gone wrong.

    Proves the mechanism end-to-end in a child process, not just that the handler is
    installed — a handler that raises the wrong thing would still skip atexit."""
    import subprocess as sp, sys, textwrap, tempfile, time
    d = tempfile.mkdtemp()
    marker = os.path.join(d, "ran")
    prog = textwrap.dedent(f'''
        import atexit, signal, sys, time
        atexit.register(lambda: open({marker!r}, "w").write("ran"))
        if sys.argv[1] == "handler":
            signal.signal(signal.SIGTERM, lambda s, f: (_ for _ in ()).throw(SystemExit(143)))
        time.sleep(30)
    ''')
    try:
        for mode, expect in (("bare", False), ("handler", True)):
            if os.path.exists(marker):
                os.remove(marker)
            p = sp.Popen([sys.executable, "-c", prog, mode])
            time.sleep(1.5)
            p.terminate()
            p.wait(timeout=10)
            assert os.path.exists(marker) is expect, (
                f"{mode}: atexit {'did not run' if expect else 'ran'} on SIGTERM")
    finally:
        shutil.rmtree(d, ignore_errors=True)


def test_run_build_installs_the_sigterm_handler():
    """Wiring guard: the proof above is about Python, not about this pipeline."""
    src = open(os.path.join(HERE, "run-build.py"), encoding="utf-8").read()
    assert "signal.signal(signal.SIGTERM" in src, "run-build does not catch SIGTERM"
    assert "SystemExit(143)" in src, "handler must raise SystemExit so atexit still runs"


def test_restore_only_happens_if_this_process_did_the_evicting():
    """Never start a service the user deliberately had off. Restore is conditional on
    THIS process having been the one that stopped it."""
    import bonsai_vram as bv
    bv._state["we_stopped_it"] = False
    assert bv.restore_bonsai(verbose=False) is False, "restored something it never stopped"


def test_restore_does_not_fire_twice():
    """atexit plus an explicit call must not start the server twice."""
    import bonsai_vram as bv
    calls = []
    orig_cli, orig_dash = bv._start_via_cli, bv._start_via_dashboard
    bv._start_via_cli = lambda: (calls.append("cli"), True, True, "")[1:]
    bv._start_via_dashboard = lambda: (calls.append("dash"), True, True, "")[1:]
    try:
        bv._state["we_stopped_it"] = True
        bv.restore_bonsai(verbose=False)
        bv.restore_bonsai(verbose=False)
        assert len(calls) == 1, f"restore fired {len(calls)} times"
    finally:
        bv._start_via_cli, bv._start_via_dashboard = orig_cli, orig_dash
        bv._state["we_stopped_it"] = False


def test_a_suite_opts_out_of_restore():
    """A suite evicts once and leaves it down. Restoring between runs would evict the coder
    in turn on EVERY run — `bonsai on` reports "coder evicted" — costing a ~22s cold load
    each time and thrashing a 24GB card both directions 40 times."""
    src = open(os.path.join(HERE, "bench-run-suite.sh"), encoding="utf-8").read()
    assert "BONSAI_RESTORE=0" in src, "the suite does not opt out of restore"
    # and the assignment must follow the -u wipe, or the clear-list would unset it
    run_line = src[src.index('env "${CLEAR[@]}"'):]
    assert run_line.index("BONSAI_RESTORE=0") < run_line.index("timeout"), \
        "BONSAI_RESTORE=0 must be an env assignment on the run command"


def test_the_eviction_policy_is_written_down():
    """Unconditional eviction is a DECISION — the health endpoint exposes no activity
    telemetry, so "refuse if recently active" is not implementable. A later reader must be
    able to tell that from an oversight."""
    src = open(os.path.join(HERE, "bonsai_vram.py"), encoding="utf-8").read()
    assert "POLICY" in src and "not implementable" in src, \
        "the eviction policy decision is not recorded"
    assert "BONSAI_RESTORE" in src, "the restore opt-out is undocumented"


# ─── fixture provenance: identity must not move for unrelated reasons ──────────

def _two_fixture_repo():
    """A throwaway git repo with two fixtures, each committed separately."""
    d = tempfile.mkdtemp(prefix="fixprov-")
    def git(*a, cwd=d):
        subprocess.run(["git"] + list(a), cwd=cwd, capture_output=True, check=False)
    git("init", "-q")
    git("config", "user.email", "t@t"); git("config", "user.name", "t")
    for name in ("alpha", "beta"):
        os.makedirs(os.path.join(d, name))
        with open(os.path.join(d, name, "larry-handover.prompt.md"), "w") as fh:
            fh.write(f"# {name} handover\n")
        git("add", "-A"); git("commit", "-q", "-m", f"add {name}")
    return d, git


def test_fixture_identity_does_not_move_when_another_fixture_changes():
    """The defect this replaces: fixture_commit was `rev-parse HEAD`, so it reported the
    REPO's state, not the fixture's. Every fixture in the repo returned the same value, and
    two runs of an unchanged fixture months apart got different fixture_commits because
    somebody edited a different one in between.

    Demonstrated 2026-09-01 on the real corpus: all four fixtures reported 3240e31 while
    their true identities were 36656d5 / a00035f / 3240e31 / 167b68a."""
    import fixture_provenance as fp
    d, git = _two_fixture_repo()
    try:
        alpha = os.path.join(d, "alpha")
        before = fp.collect(alpha, fixture_dir=alpha)
        assert before.get("fixture_commit"), before

        # touch and commit an UNRELATED fixture
        with open(os.path.join(d, "beta", "larry-handover.prompt.md"), "a") as fh:
            fh.write("\nedited\n")
        git("add", "-A"); git("commit", "-q", "-m", "edit beta only")

        after = fp.collect(alpha, fixture_dir=alpha)
        assert after["fixture_commit"] == before["fixture_commit"], (
            f"alpha's identity moved because beta changed: "
            f"{before['fixture_commit']} -> {after['fixture_commit']}")
        # repo HEAD did move, and is still recorded — as context, under an honest name
        assert after.get("projects_commit") != before.get("projects_commit"), \
            "projects_commit should track repo HEAD"
    finally:
        shutil.rmtree(d, ignore_errors=True)


def test_fixture_identity_does_move_when_the_fixture_itself_changes():
    """The other half. An identity that never moves is as useless as one that always does."""
    import fixture_provenance as fp
    d, git = _two_fixture_repo()
    try:
        alpha = os.path.join(d, "alpha")
        before = fp.collect(alpha, fixture_dir=alpha)
        with open(os.path.join(alpha, "larry-handover.prompt.md"), "a") as fh:
            fh.write("\nreal change\n")
        git("add", "-A"); git("commit", "-q", "-m", "edit alpha")
        after = fp.collect(alpha, fixture_dir=alpha)
        assert after["fixture_commit"] != before["fixture_commit"], \
            "a real edit to the fixture must move its identity"
        # and the handover hash must move too — the thing the model actually consumed
        assert after["fixture_handover_sha256"] != before["fixture_handover_sha256"]
    finally:
        shutil.rmtree(d, ignore_errors=True)


def test_uncommitted_fixture_edits_are_flagged_dirty_not_hidden():
    """A commit alone would silently describe uncommitted edits as the committed revision."""
    import fixture_provenance as fp
    d, git = _two_fixture_repo()
    try:
        alpha = os.path.join(d, "alpha")
        assert fp.collect(alpha, fixture_dir=alpha)["fixture_dirty"] is False
        with open(os.path.join(alpha, "larry-handover.prompt.md"), "a") as fh:
            fh.write("\nuncommitted\n")
        rec = fp.collect(alpha, fixture_dir=alpha)
        assert rec["fixture_dirty"] is True, rec
        # and a dirty edit in a DIFFERENT fixture must not flag this one
        with open(os.path.join(d, "beta", "larry-handover.prompt.md"), "a") as fh:
            fh.write("\nnoise\n")
        assert fp.collect(alpha, fixture_dir=alpha)["fixture_dirty"] is True
        assert fp.collect(os.path.join(d, "beta"),
                          fixture_dir=os.path.join(d, "beta"))["fixture_dirty"] is True
    finally:
        shutil.rmtree(d, ignore_errors=True)


def _cfg_reset():
    rb._config["declared"].clear()
    rb._config["observed"].clear()


def test_config_verification_catches_the_injab_failure():
    """injab declared budget-14 vs budget-16 arms, passed arm-isolation, and both arms ran
    the IDENTICAL configuration because ctx-guard trimmed the challenger's extra topic
    after selection. U=50.0 of 100 — a thing compared with itself, read as a clean null.

    A declared treatment is not evidence the treatment landed."""
    _cfg_reset()
    rb.declare_config(inject_topics="00-gotchas,01-syntax-style,02-objects,08-data-storage")
    rb.observe_config(topics_injected=["00-gotchas", "01-syntax-style", "02-objects"])
    verdict, bad = rb.config_verification()
    assert verdict == "mismatch", (verdict, bad)
    assert any("inject_topics" in m for m in bad), bad
    _cfg_reset()


def test_config_verification_passes_a_run_that_did_what_it_declared():
    _cfg_reset()
    rb.declare_config(backend="pi", model="m", max_fix_rounds=8, inject_topics="auto")
    rb.observe_config(backend_final="pi", model_used="m", max_round_reached=6,
                      topics_injected=["00-gotchas"])
    assert rb.config_verification()[0] == "verified"
    _cfg_reset()


def test_config_verification_catches_cap_backend_and_model_drift():
    """Each of these has cost a real result: a round cap that was a floor not a ceiling,
    a backend that changed with no escalation armed, a model that was not the one asked
    for (the run-dir guard exists because metrics were mislabelled that way)."""
    for declared, observed, needle in (
        (dict(max_fix_rounds=5), dict(max_round_reached=8), "max_fix_rounds"),
        (dict(backend="pi"), dict(backend_final="claude"), "backend"),
        (dict(model="qwen"), dict(model_used="other"), "model"),
    ):
        _cfg_reset()
        rb.declare_config(**declared)
        rb.observe_config(**observed)
        verdict, bad = rb.config_verification()
        assert verdict == "mismatch", (declared, observed, verdict)
        assert any(needle in m for m in bad), (needle, bad)
    # but an ARMED escalation legitimately changes the backend
    _cfg_reset()
    rb.declare_config(backend="pi", escalate_after=4)
    rb.observe_config(backend_final="claude")
    assert rb.config_verification()[0] != "mismatch", "armed escalation must be allowed"
    _cfg_reset()


def test_zero_rounds_is_an_observation_not_an_absence():
    """0 must mean "the loop was reached and no repair was needed"; ABSENCE must mean
    execution never got far enough to determine it. Overloading 0 with both would make a
    run that died before the fix loop indistinguishable from a clean first-pass build.

    Also pins the filter: `if v is not None` keeps 0, whereas the tempting `if v` would
    silently drop it and reintroduce the ambiguity."""
    _cfg_reset()
    rb.observe_config(max_round_reached=0)
    assert rb._config["observed"] == {"max_round_reached": 0}, rb._config["observed"]
    _cfg_reset()
    rb.observe_config(max_round_reached=None)
    assert rb._config["observed"] == {}, "None must be dropped, 0 must not"
    _cfg_reset()
    # and the observation must be made on ENTERING the loop, before any round runs
    src = open(os.path.join(HERE, "run-build.py"), encoding="utf-8").read()
    entry = src.index("observe_config(max_round_reached=0)")
    loop = src.index("for fix_round in range(MAX_FIX_ROUNDS + 1):")
    assert entry < loop, "zero must be observed before the loop, not inside it"


def test_observed_config_never_comes_from_re_reading_the_environment():
    """The whole point. Re-reading env would report what we BELIEVE we passed and would
    have called injab verified. Observations must be taken from what the code did."""
    src = open(os.path.join(HERE, "run-build.py"), encoding="utf-8").read()
    body = src[src.index("def observe_config"):src.index("def config_verification")]
    assert "environ" not in body, "observe_config reads the environment"
    # and the topic observation must be taken AFTER ctx-guard, not at selection
    inj = src.index("observe_config(topics_injected=")
    guard = src.index("ctx-guard: dropped injected topic")
    assert inj < guard, "topics observed before ctx-guard could trim them"


def test_missing_grounding_is_distinguishable_from_nothing_to_ground():
    """Both used to return "" and were observationally identical. A build that silently lost
    its symbol/KB lookups looked exactly like one that needed none — the same defect class as
    a silent topic eviction, and invisible in the record afterwards."""
    rb._grounding.update(status="not_attempted", reason=None, hits=0)
    assert rb.grounding_state()["status"] == "not_attempted"
    rb._note_grounding("available_no_matches", "no unresolved names to ground")
    assert rb.grounding_state()["status"] == "available_no_matches"
    rb._note_grounding("unavailable", "KB_BIN missing at /nope")
    st = rb.grounding_state()
    assert st["status"] == "unavailable" and "KB_BIN" in st["reason"], st
    # the three states must not collapse into one another
    assert len({"not_attempted", "available_no_matches", "unavailable", "applied"}) == 4


def test_a_later_call_cannot_downgrade_the_grounding_state():
    """The bug this prevents is plausible and quiet: grounding is UNAVAILABLE at round 1,
    round 5 simply has nothing to look up, and the run row ends up saying
    available_no_matches. The most alarming state is the easiest to lose, because the first
    call sets it and every subsequent quiet round overwrites it."""
    def reset():
        rb._grounding.update(status="not_attempted", reason=None, hits=0)

    reset()
    rb._note_grounding("applied", "round 1", hits=3)
    rb._note_grounding("available_no_matches", "round 5")
    st = rb.grounding_state()
    assert st["status"] == "applied", st          # not downgraded
    assert st["hits"] == 3, st                    # accounting still accumulates

    reset()
    rb._note_grounding("unavailable", "kb gone")
    rb._note_grounding("applied", "round 5", hits=2)
    assert rb.grounding_state()["status"] == "unavailable", "degradation must be durable"

    reset()
    rb._note_grounding("available_no_matches", "round 1")
    rb._note_grounding("applied", "round 2", hits=1)
    assert rb.grounding_state()["status"] == "applied", "an upgrade must still be allowed"
    reset()


def test_grounding_state_rides_on_every_metrics_row():
    """Added centrally in emit_metrics, so a new emit site cannot forget it. Otherwise the
    distinction survives only in a log nobody reads back."""
    src = open(os.path.join(HERE, "run-build.py"), encoding="utf-8").read()
    body = src[src.index("def emit_metrics(rec):"):src.index("def emit_metrics(rec):") + 700]
    assert "grounding_state()" in body, "metrics rows do not carry grounding state"
    # and the silent-degrade shape must be gone from both call sites
    assert "not pairs or not os.path.exists(KB_BIN)" not in src, "member site still silent"
    assert "not names or not os.path.exists(KB_BIN)" not in src, "names site still silent"


def test_every_env_knob_is_documented():
    """RUN-BUILD.md had drifted to 30 of 53 knobs undocumented, including ones that change
    how a build runs (WORKFLOW, VERBATIM_WRITE, FIX_STRATEGY). It grew silently because
    nothing checked. A knob nobody documents is a knob nobody can turn off in an incident."""
    src = open(os.path.join(HERE, "run-build.py"), encoding="utf-8").read()
    doc = open(os.path.join(HERE, "RUN-BUILD.md"), encoding="utf-8").read()
    knobs = sorted(set(re.findall(r'os\.environ\.get\(\s*"([A-Z_0-9]+)"', src)))
    assert knobs, "knob scan found nothing — the regex has drifted from the code"
    missing = [k for k in knobs if k not in doc]
    assert not missing, f"{len(missing)} env knob(s) undocumented in RUN-BUILD.md: {missing}"


def test_there_is_exactly_one_pi_spawn_in_the_codebase():
    """The invariant that replaces per-pipeline property checks.

    Three hand-maintained copies of run_pi drifted apart and cost real runs twice in one
    week: the stdin fix missed go and cs for two days (after that fault had already
    destroyed a go/cs benchmark run), then three stall guards existed only in the AL
    pipeline. Property-by-property guards catch drift someone has already thought of. One
    implementation catches the drift nobody has.

    So: no run-build*.py may spawn pi itself. They delegate to coder.run_pi."""
    import glob as _g
    offenders = []
    for path in sorted(_g.glob(os.path.join(HERE, "run-build*.py"))):
        src = open(path, encoding="utf-8").read()
        if "coder.run_pi(" not in src:
            offenders.append(f"{os.path.basename(path)}: does not delegate to coder.run_pi")
        # a private spawn is the thing that drifted — PI_BIN reaching subprocess directly
        for m in re.finditer(r"subprocess\.run\((.{0,200}?)\)\n", src, re.S):
            if "PI_BIN" in m.group(1) or "cfg.pi_bin" in m.group(1):
                offenders.append(f"{os.path.basename(path)}: spawns pi directly")
    assert not offenders, offenders


def test_the_one_pi_spawn_carries_every_stall_guard():
    """coder.py is now the single point where these can be got wrong."""
    src = open(os.path.join(HERE, "coder.py"), encoding="utf-8").read()
    need = {
        "stdin pinned": "stdin=subprocess.DEVNULL",
        "timeout flag": 'LAST["timed_out"]',
        "wedged-write fail-fast": "def wedged_write",
        "consecutive-timeout streak": "FIX_TIMEOUT_STREAK",
        "Windows @file argv workaround": 'os.name == "nt"',
        "bonsai eviction only for the local ext": "free_bonsai_vram_once",
    }
    missing = [label for label, needle in need.items() if needle not in src]
    assert not missing, f"coder.py lost: {missing}"


def test_every_pipeline_still_bounds_its_own_rounds():
    """Round budgets stay per-pipeline — they are policy, not spawn mechanics — so they
    still need a class-level check."""
    import glob as _g
    need = {"bounded fix round": "FIX_TIMEOUT",
            "MAX_FIX_ROUNDS env-tunable": 'environ.get("MAX_FIX_ROUNDS"'}
    missing = []
    for path in sorted(_g.glob(os.path.join(HERE, "run-build*.py"))):
        src = open(path, encoding="utf-8").read()
        for label, needle in need.items():
            if needle not in src:
                missing.append(f"{os.path.basename(path)}: {label}")
    assert not missing, f"pipelines have diverged: {missing}"


def test_a_fix_round_cannot_outlast_the_harness_that_kills_it():
    """topicab3 control r6 lost 3600s: write 93s, two fix rounds at 40s and 17s, then one
    round ran until the bench harness killed the whole run. Fix rounds inherited
    PI_TIMEOUT=3600 — the same as RUN_TIMEOUT — so the inner guard could never fire."""
    assert rb.FIX_TIMEOUT < rb.PI_TIMEOUT, (rb.FIX_TIMEOUT, rb.PI_TIMEOUT)
    assert rb.FIX_TIMEOUT < 3600, "must be able to fire before the 3600s harness cap"
    # and bounding ONE call is not enough: 8 rounds x 600s still outlasts the cap
    assert rb.MAX_FIX_TIMEOUTS * rb.FIX_TIMEOUT < 3600, (
        rb.MAX_FIX_TIMEOUTS, rb.FIX_TIMEOUT)


def test_every_fix_round_call_site_is_bounded():
    """Wiring guard: a constant nothing reads is not a fix. Measured over 2197 fix calls
    the median is 17s and p99 120s, so 600s truncates 2 calls in 2197."""
    src = open(os.path.join(HERE, "run-build.py"), encoding="utf-8").read()
    body = src[src.index("fixing issues (round"):src.index("Ensure disk holds the BEST")]
    calls = re.findall(r"run_coder\((.{0,120}?)\)\n", body, re.S)
    unbounded = [c for c in calls if "timeout=" not in c]
    assert not unbounded, f"fix-round run_coder call without a timeout: {unbounded}"
    assert "coder.FIX_TIMEOUT_STREAK" in body, "the consecutive-timeout guard is not wired in"


def test_the_pipeline_scores_the_raw_spec_not_the_built_prompt():
    """Wiring guard, deliberately structural — the behaviour above is unobservable without
    running a whole build. select_topics must be handed the text captured BEFORE the
    BCQuality and API-grounding appends, not the accumulating prompt."""
    src = open(os.path.join(HERE, "run-build.py"), encoding="utf-8").read()
    # Prefix match, not the whole call: pinning every argument made this fail the moment
    # budget_k was added, which is a true change to the call and not the regression this
    # guards. What matters is which TEXT is scored.
    assert "select_topics(EXPECTED_FILES, _spec_text" in src, \
        "topic selection is reading the built prompt again"
    spec_at = src.index("_spec_text = handover_text")
    assert spec_at < src.index("bcquality.coder_checklist"), \
        "_spec_text is captured after BCQuality has already been folded in"


# ─── missing `using` directives (the doclink blocker) ──────────────────────────

def _using_project(body):
    d = tempfile.mkdtemp()
    os.makedirs(os.path.join(d, "src"))
    open(os.path.join(d, "app.json"), "w").write('{"id":"x","name":"N"}')
    open(os.path.join(d, "src", "a.al"), "w").write(body)
    return d


def _run_using(d):
    real_root, real_idx = rb.PROJECT_ROOT, rb._sym_idx
    try:
        rb.PROJECT_ROOT = d
        rb._sym_idx = real_index() if REAL else {}
        rb.add_missing_using_directives()
        return open(os.path.join(d, "src", "a.al")).read()
    finally:
        rb.PROJECT_ROOT, rb._sym_idx = real_root, real_idx


def test_missing_namespace_using_is_added():
    """The doclink blocker: 0/12 builds across four sessions, four models and two configs,
    always error score 1. The model emitted two of the four `using` lines it needed, and
    AL0185 "Codeunit 'Temp Blob' is missing" reads like a missing DEPENDENCY — so every
    repair round hunted app.json instead of the namespace."""
    if not REAL:
        return skip("using directives", "no .alpackages")
    d = _using_project(
        'namespace SinclairSoftScotland.DocLink;\n\nusing System.Azure.Storage;\n\n'
        'codeunit 50100 "PTE Repro"\n{\n    procedure P()\n    var\n'
        '        TempBlob: Codeunit "Temp Blob";\n'
        '        TenantMedia: Record "Tenant Media";\n'
        '    begin\n    end;\n}\n')
    try:
        out = _run_using(d)
        assert "using System.Utilities;" in out, out          # Temp Blob
        assert "using System.Environment;" in out, out        # Tenant Media
        assert "using System.Azure.Storage;" in out, "existing usings must survive"
        # inserted above the object, below the namespace
        assert out.index("namespace ") < out.index("using System.Utilities;") \
            < out.index("codeunit 50100"), out
    finally:
        shutil.rmtree(d)


def test_nothing_is_added_when_nothing_is_missing():
    """A project that already compiles must come out byte-identical — the three passing
    bench fixtures were checked this way before this shipped."""
    if not REAL:
        return skip("using no-op", "no .alpackages")
    body = ('namespace SinclairSoftScotland.X;\n\nusing System.Utilities;\n\n'
            'codeunit 50100 "X"\n{\n    procedure P()\n    var\n'
            '        TempBlob: Codeunit "Temp Blob";\n    begin\n    end;\n}\n')
    d = _using_project(body)
    try:
        assert _run_using(d) == body
    finally:
        shutil.rmtree(d)


def test_unknown_names_are_never_invented_into_a_using():
    """Only a name the symbol index resolves earns a namespace. Guessing here would put a
    fabricated `using` in front of the compiler."""
    if not REAL:
        return skip("using invent", "no .alpackages")
    d = _using_project(
        'codeunit 50100 "X"\n{\n    procedure P()\n    var\n'
        '        Thing: Codeunit "Totally Invented Thing";\n    begin\n    end;\n}\n')
    try:
        out = _run_using(d)
        assert "using" not in out, out
    finally:
        shutil.rmtree(d)


def test_project_local_objects_need_no_using():
    if not REAL:
        return skip("using local", "no .alpackages")
    d = tempfile.mkdtemp()
    try:
        os.makedirs(os.path.join(d, "src"))
        open(os.path.join(d, "app.json"), "w").write('{"id":"x","name":"N"}')
        open(os.path.join(d, "src", "own.al"), "w").write(
            'table 50200 "My Own Tbl"\n{\n    fields { field(1; A; Integer) { } }\n}\n')
        body = ('codeunit 50100 "X"\n{\n    procedure P()\n    var\n'
                '        R: Record "My Own Tbl";\n    begin\n    end;\n}\n')
        open(os.path.join(d, "src", "a.al"), "w").write(body)
        real_root, real_idx = rb.PROJECT_ROOT, rb._sym_idx
        try:
            rb.PROJECT_ROOT = d
            rb._sym_idx = real_index()
            rb.add_missing_using_directives()
        finally:
            rb.PROJECT_ROOT, rb._sym_idx = real_root, real_idx
        assert open(os.path.join(d, "src", "a.al")).read() == body
    finally:
        shutil.rmtree(d)


# ─── EventSubscriber element argument ──────────────────────────────────────────

def _elem_project(attr):
    d = tempfile.mkdtemp()
    os.makedirs(os.path.join(d, "src"))
    open(os.path.join(d, "src", "a.al"), "w").write(
        'codeunit 50100 "X"\n{\n    ' + attr +
        '\n    local procedure A(var SalesHeader: Record "Sales Header")\n'
        '    begin\n    end;\n}\n')
    return d


def _run_elem(d):
    real = rb.PROJECT_ROOT
    try:
        rb.PROJECT_ROOT = d
        rb.normalize_event_subscriber_element()
        return open(os.path.join(d, "src", "a.al")).read()
    finally:
        rb.PROJECT_ROOT = real


def test_empty_double_quoted_element_becomes_an_empty_string():
    """`""` is an empty QUOTED IDENTIFIER (illegal); `''` is an empty string (legal).
    AL0242 quotes '' back at you, which reads like the '' is the problem."""
    d = _elem_project('[EventSubscriber(ObjectType::Codeunit, Codeunit::"Sales-Post", '
                      "'OnAfterPostSalesDoc', \"\", true, true)]")
    try:
        out = _run_elem(d)
        assert "'OnAfterPostSalesDoc', ''" in out, out
        assert '""' not in out, out
    finally:
        shutil.rmtree(d)


def test_the_event_name_quoting_is_left_alone():
    """Probed against BC27: 'Event', "Event" and bare Event ALL compile. Only the empty
    element is invalid. Rewriting the name's quotes — the first design — would have churned
    correct code and left the real fault in place."""
    for name in ("'OnAfterPostSalesDoc'", '"OnAfterPostSalesDoc"', "OnAfterPostSalesDoc"):
        d = _elem_project('[EventSubscriber(ObjectType::Codeunit, Codeunit::"Sales-Post", '
                          + name + ", '', true, true)]")
        try:
            assert name in _run_elem(d), name
        finally:
            shutil.rmtree(d)


def test_a_correct_attribute_is_untouched():
    attr = ('[EventSubscriber(ObjectType::Codeunit, Codeunit::"Sales-Post", '
            "'OnAfterPostSalesDoc', '', true, true)]")
    d = _elem_project(attr)
    try:
        assert attr in _run_elem(d)
    finally:
        shutil.rmtree(d)


def test_a_quoted_object_reference_keeps_its_double_quotes():
    """Argument 2 is an object reference, where "Document Attachment" is CORRECT."""
    d = _elem_project('[EventSubscriber(ObjectType::Table, Database::"Document Attachment", '
                      "'OnAfterInsertEvent', \"\", false, false)]")
    try:
        out = _run_elem(d)
        assert 'Database::"Document Attachment"' in out, out
        assert "'OnAfterInsertEvent', ''" in out, out
    finally:
        shutil.rmtree(d)


def test_a_non_empty_element_is_not_rewritten():
    """Only the EMPTY "" is invalid; a real element name is a different question."""
    attr = ('[EventSubscriber(ObjectType::Page, Page::"Customer Card", '
            "'OnAction', \"MyControl\", true, true)]")
    d = _elem_project(attr)
    try:
        assert '"MyControl"' in _run_elem(d)
    finally:
        shutil.rmtree(d)


# ─── argument-type errors grounded with the real signature ─────────────────────

def _sig_project(body):
    d = tempfile.mkdtemp()
    os.makedirs(os.path.join(d, "src"))
    open(os.path.join(d, "src", "a.al"), "w").write(body)
    return d


def test_argument_type_error_is_answered_with_the_real_signature():
    """AL0133 says "cannot convert from 'Text' to 'SecretText'" without naming the method,
    the parameter, or the correct call — so the model permutes argument types. One build
    oscillated between InStream and OutStream for sixteen rounds. The signature is a
    lookup, not a judgement."""
    if not REAL:
        return skip("signature grounding", "no .alpackages")
    d = _sig_project(
        'codeunit 50100 "X"\n{\n    procedure P()\n    var\n'
        '        Auth: Codeunit "Storage Service Authorization";\n'
        '        KeyText: Text;\n    begin\n'
        "        Auth.CreateSharedKey(KeyText);\n    end;\n}\n")
    real_root, real_idx = rb.PROJECT_ROOT, rb._sym_idx
    try:
        rb.PROJECT_ROOT, rb._sym_idx = d, real_index()
        bt = (f"{d}/src/a.al(8,30): error AL0133: Argument 1: cannot convert from "
              f"'Text' to 'SecretText'")
        out = rb.ground_call_signatures(bt)
        assert "CreateSharedKey" in out and "SecretText" in out, out
        assert "from Microsoft" in out, "a signature claim must cite its package"
    finally:
        rb.PROJECT_ROOT, rb._sym_idx = real_root, real_idx
        shutil.rmtree(d)


def test_unknown_methods_are_not_invented():
    if not REAL:
        return skip("signature invent", "no .alpackages")
    d = _sig_project('codeunit 50100 "X"\n{\n    procedure P()\n    begin\n'
                     "        Thing.TotallyMadeUpMethod(1);\n    end;\n}\n")
    real_root, real_idx = rb.PROJECT_ROOT, rb._sym_idx
    try:
        rb.PROJECT_ROOT, rb._sym_idx = d, real_index()
        bt = f"{d}/src/a.al(5,20): error AL0133: Argument 1: cannot convert from 'Text' to 'Integer'"
        assert rb.ground_call_signatures(bt) == ""
    finally:
        rb.PROJECT_ROOT, rb._sym_idx = real_root, real_idx
        shutil.rmtree(d)


def test_grounding_is_silent_without_a_matching_diagnostic():
    if not REAL:
        return skip("signature quiet", "no .alpackages")
    real_idx = rb._sym_idx
    try:
        rb._sym_idx = real_index()
        assert rb.ground_call_signatures("BUILD: PASSED") == ""
        assert rb.ground_call_signatures("") == ""
    finally:
        rb._sym_idx = real_idx


def test_grounding_is_capped():
    """A wall of signatures pushes the compiler's own output out of the model's
    attention — the same reason al_errors caps its context."""
    if not REAL:
        return skip("signature cap", "no .alpackages")
    calls = "\n".join(f'        Auth.CreateSharedKey(K{i});' for i in range(20))
    d = _sig_project('codeunit 50100 "X"\n{\n    procedure P()\n    begin\n'
                     + calls + "\n    end;\n}\n")
    real_root, real_idx = rb.PROJECT_ROOT, rb._sym_idx
    try:
        rb.PROJECT_ROOT, rb._sym_idx = d, real_index()
        bt = "\n".join(f"{d}/src/a.al({5+i},30): error AL0133: Argument 1: cannot "
                       f"convert from 'Text' to 'SecretText'" for i in range(20))
        assert rb.ground_call_signatures(bt).count("- `") <= 6
    finally:
        rb.PROJECT_ROOT, rb._sym_idx = real_root, real_idx
        shutil.rmtree(d)


# ─── proactive API grounding (Phase 1b) ────────────────────────────────────────

_DOCLINK = "/mnt/rojaws/localDev/projects/tsg-document-link-2-az-storage"


def _apis_for(handover, root=_DOCLINK):
    real_root, real_idx, real_flag = rb.PROJECT_ROOT, rb._sym_idx, rb.AL_APIS
    try:
        rb.PROJECT_ROOT, rb._sym_idx, rb.AL_APIS = root, real_index(), True
        return rb.ground_handover_apis(handover)
    finally:
        rb.PROJECT_ROOT, rb._sym_idx, rb.AL_APIS = real_root, real_idx, real_flag


def test_api_grounding_is_off_by_default():
    """It changes every prompt. AL_BRAIN shipped on this same promise and measured as no
    effect three times; this one is opt-in until its A/B says otherwise."""
    assert rb.AL_APIS is False


def test_the_methods_the_handover_names_all_survive_selection():
    """The whole point. Ranking ALONE dropped GetBlobAsStream, CreateInStream and
    CreateOutStream while keeping ChangeLease and AppendBlockText — three of the six
    methods doclink actually calls, lost to a weak similarity signal."""
    if not REAL or not os.path.isdir(_DOCLINK):
        return skip("api grounding", "doclink fixture or symbols unavailable")
    h = open(os.path.join(_DOCLINK, "larry-handover.prompt.md"),
             encoding="utf-8", errors="replace").read()
    out = _apis_for(h)
    assert out, "doclink names six callable base-app objects; grounding must fire"
    for m in ("GetBlobAsStream", "PutBlobBlockBlobStream", "CreateSharedKey",
              "CreateInStream", "CreateOutStream", "GetAsTempBlob", "Initialize"):
        assert m + "(" in out, f"{m} was dropped from the injected signatures"


def test_namespaces_are_stated_with_the_signatures():
    """AL0185 'Codeunit Temp Blob is missing' is a namespace problem wearing a
    dependency's clothes. Saying the namespace beside the signature is the cheap half."""
    if not REAL or not os.path.isdir(_DOCLINK):
        return skip("api namespaces", "fixture unavailable")
    h = open(os.path.join(_DOCLINK, "larry-handover.prompt.md"),
             encoding="utf-8", errors="replace").read()
    out = _apis_for(h)
    assert "using System.Azure.Storage;" in out, out[:400]
    assert "using System.Utilities;" in out, "Temp Blob's namespace must be stated"


def test_injection_stays_within_its_budget():
    """Full signature lists are ~2.6k tokens against 0.5k of headroom today."""
    if not REAL or not os.path.isdir(_DOCLINK):
        return skip("api budget", "fixture unavailable")
    h = open(os.path.join(_DOCLINK, "larry-handover.prompt.md"),
             encoding="utf-8", errors="replace").read()
    out = _apis_for(h)
    assert len(out) / 3700.0 <= rb.AL_API_BUDGET_K * 1.35, len(out) / 3700.0


def test_every_signature_cites_its_package():
    if not REAL or not os.path.isdir(_DOCLINK):
        return skip("api evidence", "fixture unavailable")
    h = open(os.path.join(_DOCLINK, "larry-handover.prompt.md"),
             encoding="utf-8", errors="replace").read()
    out = _apis_for(h)
    assert out.count("(from Microsoft") >= 3, "an API claim must be traceable to a package"


def test_objects_that_are_only_extended_contribute_nothing():
    """The 95% fixture names Customer Card / Vendor Card / Post Code — objects to EXTEND,
    not call. Spending budget on them would be the failure mode this is meant to avoid."""
    if not REAL:
        return skip("api extend-only", "no symbols")
    out = _apis_for('Extend the "Customer Card" and add a "Post Code" lookup.')
    assert "Customer Card" not in out, out[:300]


def test_unknown_quoted_names_are_never_invented():
    if not REAL:
        return skip("api invent", "no symbols")
    assert _apis_for('Use the "Totally Invented Client" to do the thing.') == ""


def test_grounding_is_silent_when_disabled():
    real = rb.AL_APIS
    try:
        rb.AL_APIS = False
        assert rb.ground_handover_apis('Use "ABS Blob Client".') == ""
    finally:
        rb.AL_APIS = real



# --- Phase 2: WORKFLOW=incremental ratchet -------------------------------------

def test_dependency_rank_orders_tables_before_pages_permset_last():
    files = ["/p/src/page/X.Page.al", "/p/src/permissionset/P.PermissionSet.al",
             "/p/src/table/T.Table.al", "/p/src/codeunit/C.Codeunit.al",
             "/p/src/enum/E.Enum.al"]
    got = [rb.object_type(f) for f in sorted(files, key=rb._dependency_rank)]
    assert got == ["Enum", "Table", "Codeunit", "Page", "PermissionSet"], got


def test_declared_object_names_scans_the_handover():
    h = 'codeunit 50100 "PTE Doc Link AZ Mgt"\ntable 50103 "PTE Doc Link AZ Setup"\n'
    names = rb._declared_object_names(h)
    assert names == {"pte doc link az mgt", "pte doc link az setup"}, names


def test_deferrable_true_when_error_names_an_unwritten_project_object():
    # The ratchet wrote a codeunit that calls another codeunit not written YET.
    # That is an ordering artefact, not a defect: defer, do not revert.
    bt = "x.al(1,1): error AL0185: Codeunit 'PTE Doc Link Blob Mgt' is missing"
    assert rb._deferrable(bt, {"pte doc link blob mgt"}, []) is True


def test_deferrable_false_for_a_base_app_object_we_never_declare():
    # 'Temp Blob' is Microsoft's. It will never appear later in this project, so the
    # file is genuinely wrong (a missing `using`) and must be reverted.
    bt = "x.al(1,1): error AL0185: Codeunit 'Temp Blob' is missing"
    assert rb._deferrable(bt, {"pte doc link blob mgt"}, []) is False


def test_deferrable_false_when_any_error_is_unrelated():
    # One non-ordering error is enough to condemn the file — otherwise a broken file
    # rides along on the back of a benign AL0185 and never gets reverted.
    bt = ("x.al(1,1): error AL0185: Codeunit 'PTE Doc Link Blob Mgt' is missing\n"
          "x.al(9,3): error AL0132: 'Media' does not contain a definition for 'IsEmpty'")
    assert rb._deferrable(bt, {"pte doc link blob mgt"}, []) is False


def test_deferrable_false_when_no_errors_at_all():
    assert rb._deferrable("", {"a"}, []) is False


def test_deferrable_strips_a_namespace_qualifier():
    bt = "x.al(1,1): error AL0185: Codeunit 'PTEDocLink.PTE Doc Link Blob Mgt' is missing"
    assert rb._deferrable(bt, {"pte doc link blob mgt"}, []) is True


def test_single_file_msg_names_one_file_and_lists_the_rest_as_later():
    h = 'codeunit 50100 "C"'
    msg = rb.build_single_file_msg(h, "/p/src/table/T.Table.al", ["/p/src/page/X.Page.al"])
    assert "Write exactly ONE file this turn" in msg
    assert "T.Table.al" in msg and "X.Page.al" in msg
    assert "do NOT create them now" in msg
    # The handover must precede the directive: directive-first made the model reply in
    # chat instead of calling the write tool.
    assert msg.index("PROJECT HANDOVER") < msg.index("YOUR TASK")
    # pi treats a leading-dash argv as a CLI flag and exits 1 without writing anything.
    assert not msg.lstrip().startswith("-")
    assert "USE THE WRITE TOOL" in msg



def test_permset_only_keeps_the_file_rather_than_deferring():
    # PTE0004 alone must NOT delete the table: the permission set has to reference it.
    bt = ("t.al(3,13): error PTE0004: Table 50103 'PTE Doc Link AZ Setup' "
          "is missing a matching permission set.")
    real = rb.EXPECTED_FILES
    try:
        rb.EXPECTED_FILES = ["/p/src/table/T.Table.al", "/p/src/permissionset/P.PermissionSet.al"]
        assert rb._permset_only(bt, []) is True
        # Once the permission set IS written, PTE0004 is a real error again.
        assert rb._permset_only(bt, ["/p/src/permissionset/P.PermissionSet.al"]) is False
    finally:
        rb.EXPECTED_FILES = real


def test_permset_only_false_when_another_error_is_present():
    bt = ("t.al(3,13): error PTE0004: Table 50103 'X' is missing a matching permission set.\n"
          "t.al(9,1): error AL0104: Syntax error")
    real = rb.EXPECTED_FILES
    try:
        rb.EXPECTED_FILES = ["/p/src/permissionset/P.PermissionSet.al"]
        assert rb._permset_only(bt, []) is False
    finally:
        rb.EXPECTED_FILES = real


def test_deferrable_ignores_a_pending_permset_cop_alongside_a_real_dependency():
    bt = ("c.al(1,1): error AL0185: Codeunit 'PTE Doc Link Blob Mgt' is missing\n"
          "t.al(3,13): error PTE0004: Table 50103 'X' is missing a matching permission set.")
    real = rb.EXPECTED_FILES
    try:
        rb.EXPECTED_FILES = ["/p/src/permissionset/P.PermissionSet.al"]
        assert rb._deferrable(bt, {"pte doc link blob mgt"}, []) is True
    finally:
        rb.EXPECTED_FILES = real



def test_declared_names_finds_the_id_less_forms():
    # Requiring `codeunit 50100 "X"` found only 5 of doclink's 9 objects. The other four
    # appear as an id-allocation table row and as permission set body entries, and the
    # ratchet REVERTED them on an AL0185 that should have been a DEFER.
    h = ('| `codeunit "PTE Doc Link Migration"` | 50102 |\n'
         '        page "PTE Doc Link AZ Setup Card" = X,\n'
         'codeunit 50100 "PTE Doc Link AZ Mgt"\n')
    names = rb._declared_object_names(h)
    assert "pte doc link migration" in names
    assert "pte doc link az setup card" in names
    assert "pte doc link az mgt" in names


def test_declared_names_excludes_base_app_objects():
    # The id-less pattern also matches `extends "Document Attachment"`. Treating
    # Microsoft's objects as "ours, coming later" would defer a real missing-`using`
    # forever instead of reverting the file.
    if not rb._symbol_index():
        SKIPPED.append("test_declared_names_excludes_base_app_objects (no symbols)")
        return
    h = 'tableextension 50110 "PFX Ext" extends "Document Attachment"\ncodeunit 4100 "Temp Blob"\n'
    names = rb._declared_object_names(h)
    assert "pfx ext" in names
    assert "document attachment" not in names
    assert "temp blob" not in names



def test_retry_prompt_contradicts_the_models_success_claim():
    # A model that believes it already wrote the file will just narrate again unless it
    # is told, as deterministic fact, that the filesystem disagrees.
    src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "run-build.py"),
               encoding="utf-8").read()
    assert "That claim has been checked against the filesystem" in src
    assert "The file does NOT exist" in src or "does NOT exist" in src
    assert "INCR_WRITE_ATTEMPTS" in src


def test_incr_write_attempts_defaults_to_parity_with_single_shot():
    # The single-shot path retries a failed write 3x; the ratchet had no retry at all,
    # so one hallucinated reply on file 1 stalled the whole run.
    assert rb.INCR_WRITE_ATTEMPTS == 3
    assert rb.MAX_WRITE_ATTEMPTS == 3


# ---------------------------------------------------------------------------
# AL-4b: a malformed EventSubscriber must be REPORTED, never silently skipped.
# _SUB_RE only ever matched the correct shape, so a bare event identifier fell through
# `if not m: continue` and the verifier said nothing while the compiler produced a
# 90-error parse cascade. Measured on doclink Phase 2: 3/10 runs, 14 of 16 AL0114 errors
# sitting on an attribute line. Every test below fails against the pre-change module.
# ---------------------------------------------------------------------------

def _classify(attr_line):
    """Rule for a single attribute, straight through the occurrence scanner."""
    src = "codeunit 50100 X\n{\n    %s\n    local procedure P()\n    begin\n    end;\n}\n" % attr_line
    d = _srcdir(src)
    try:
        _, problems = event_verify.scan_subscribers(os.path.join(d, "subs.al"))
        return problems[0]["rule"] if problems else "ok"
    finally:
        shutil.rmtree(d)


def test_subscriber_bare_event_identifier_is_reported():
    """The exact doclink failure: event name written unquoted."""
    rule = _classify("[EventSubscriber(ObjectType::Table, Database::\"Document Attachment\", "
                     "OnAfterInsertEvent, , false, false)]")
    assert rule == "subscriber-event-unquoted", rule


def test_subscriber_correct_form_is_not_reported():
    """The failure this must never have: accusing correct code."""
    rule = _classify("[EventSubscriber(ObjectType::Table, Database::\"Document Attachment\", "
                     "'OnAfterInsertEvent', '', false, false)]")
    assert rule == "ok", rule


def test_subscriber_unquoted_element_is_reported():
    rule = _classify("[EventSubscriber(ObjectType::Page, Page::\"Customer Card\", "
                     "'OnOpenPageEvent', Control1, false, false)]")
    assert rule == "subscriber-element-unquoted", rule


def test_subscriber_truncated_argument_list_is_unparseable():
    rule = _classify("[EventSubscriber(ObjectType::Table)]")
    assert rule == "subscriber-unparseable", rule


def test_subscriber_unclosed_attribute_is_unparseable():
    rule = _classify("[EventSubscriber(ObjectType::Table, Database::\"Document Attachment\", ")
    assert rule == "subscriber-unparseable", rule


def test_subscriber_in_a_comment_is_not_an_occurrence():
    """A malformed attribute inside a comment must not become a finding."""
    rule = _classify("// [EventSubscriber(ObjectType::Table, Database::\"X\", Bare, , false, false)]")
    assert rule == "ok", rule


def test_subscriber_in_a_string_literal_is_not_an_occurrence():
    rule = _classify("Caption = '[EventSubscriber(ObjectType::Table, Database::\"X\", Bare)]';")
    assert rule == "ok", rule


def test_subscriber_multiline_attribute_is_read_whole():
    """A wrapped attribute is one occurrence, not a truncated one."""
    rule = _classify("[EventSubscriber(ObjectType::Table,\n        Database::\"Document Attachment\",\n"
                     "        'OnAfterInsertEvent', '', false, false)]")
    assert rule == "ok", rule


def test_malformed_subscriber_is_reported_without_a_symbol_index():
    """Syntax is knowable offline; it must not wait on symbols to be reported."""
    src = ("codeunit 50100 X\n{\n"
           "    [EventSubscriber(ObjectType::Table, Database::\"Document Attachment\", "
           "OnAfterInsertEvent, , false, false)]\n"
           "    local procedure P()\n    begin\n    end;\n}\n")
    d = _srcdir(src)
    try:
        rules = {f["rule"] for f in event_verify.verify(d, {})}
        assert rules == {"subscriber-event-unquoted"}, rules
    finally:
        shutil.rmtree(d)


def test_valid_subscribers_still_verify_against_symbols():
    """The existing symbol path must be untouched by the new classification step."""
    if not REAL:
        return skip("event_verify still verifies", "no .alpackages")
    bad = """codeunit 50100 X
{
    [EventSubscriber(ObjectType::Codeunit, Codeunit::"Sales-Post", 'OnAfterPostSalesDocInvented', '', true, true)]
    local procedure P(var SalesHeader: Record "Sales Header")
    begin
    end;
}
"""
    assert "event-missing" in _rules(bad)


# ---------------------------------------------------------------------------
# Routing-economics prerequisite: every Claude call must be priceable, or say so.
# duration_s is not a cost model. These use a controlled fake CLI — no billed calls.
# ---------------------------------------------------------------------------
claude_egress = _load("claude_egress", "claude_egress.py")

_FAKE_OK = """{"type":"result","subtype":"success","duration_ms":4210,"duration_api_ms":3980,
"is_error":false,"num_turns":3,"result":"patched the thing","stop_reason":null,
"total_cost_usd":0.0731,
"usage":{"input_tokens":18422,"output_tokens":1310,"cache_read_input_tokens":91000},
"modelUsage":{"claude-opus-5":{}},"session_id":"s","uuid":"u"}"""


def _fake_cli(payload):
    """A stand-in for the claude binary that prints a fixed payload on stdout.

    Windows has NO shebang handling: CreateProcess needs a native PE, .bat or .cmd, so the
    POSIX bash script died with WinError 193 ("%1 is not a valid Win32 application") when
    claude_egress._raw exec'd it. Reported from the Windows client 2026-09-01.

    The payload lives in a data file and the fake CLI just prints it. That keeps the two
    branches trivially equivalent and — more to the point — stops batch escaping from
    mangling JSON: `echo` in cmd.exe eats < > & | ^ %, all of which occur in these payloads.

    A .cmd is the right Windows form because it is what the pipeline already exec's in
    anger — npm installs `claude` and `pi` as .CMD shims and run_pi drives them through
    subprocess.run without shell. See [[reference_windows_cmd_argv]] for the argv caveat
    that applies to those same shims.
    """
    d = tempfile.mkdtemp()
    data = os.path.join(d, "payload.json")
    with open(data, "w", newline="\n") as fh:
        fh.write(payload + "\n")
    if os.name == "nt":
        p = os.path.join(d, "claude.cmd")
        with open(p, "w", newline="\r\n") as fh:
            fh.write('@echo off\ntype "%~dp0payload.json"\n')     # %~dp0 = this file's dir
    else:
        p = os.path.join(d, "claude")
        with open(p, "w", newline="\n") as fh:
            fh.write('#!/usr/bin/env bash\ncat "$(dirname "$0")/payload.json"\n')
        os.chmod(p, 0o755)
    return d, p


def test_usage_is_captured_from_a_json_result():
    d, cli = _fake_cli(_FAKE_OK)
    try:
        claude_egress.reset_usage()
        txt = claude_egress._raw(d, "prompt", cli, "T", 60)
        assert txt == "patched the thing", txt          # caller contract unchanged
        t = claude_egress.usage_totals()
        assert t["claude_input_tokens"] == 18422, t
        assert t["claude_output_tokens"] == 1310, t
        assert t["claude_cache_read_tokens"] == 91000, t
        assert abs(t["claude_cost_usd"] - 0.0731) < 1e-9, t
        assert t["claude_calls_missing_usage"] == 0, t
    finally:
        shutil.rmtree(d, ignore_errors=True)


def test_usage_totals_accumulate_across_calls():
    d, cli = _fake_cli(_FAKE_OK)
    try:
        claude_egress.reset_usage()
        claude_egress._raw(d, "p", cli, "A", 60)
        claude_egress._raw(d, "p", cli, "B", 60)
        t = claude_egress.usage_totals()
        assert t["claude_calls"] == 2 and t["claude_input_tokens"] == 36844, t
    finally:
        shutil.rmtree(d, ignore_errors=True)


def test_unpriceable_call_is_recorded_not_silently_zero():
    """A cost of 0 and a cost of unknown are different facts."""
    d, cli = _fake_cli("plain text from an older CLI")
    try:
        claude_egress.reset_usage()
        os.environ.pop("CLAUDE_USAGE_STRICT", None)
        txt = claude_egress._raw(d, "p", cli, "T", 60)
        assert "older CLI" in txt, txt                  # build still gets its text
        t = claude_egress.usage_totals()
        assert t["claude_calls_missing_usage"] == 1, t
    finally:
        shutil.rmtree(d, ignore_errors=True)


def test_zero_token_result_object_is_not_priced_as_free():
    """The CLI synthesizes {type:result, subtype:success, cost:0, usage:zeros} on some
    paths. Accepting that as attributed would score a degenerate call at $0."""
    zeroed = ('{"type":"result","subtype":"success","duration_ms":0,"duration_api_ms":0,'
              '"is_error":false,"num_turns":0,"result":"","stop_reason":null,'
              '"total_cost_usd":0,"usage":{"input_tokens":0,"output_tokens":0,'
              '"cache_read_input_tokens":0},"modelUsage":{},"session_id":"s","uuid":"u"}')
    d, cli = _fake_cli(zeroed)
    try:
        claude_egress.reset_usage()
        os.environ.pop("CLAUDE_USAGE_STRICT", None)
        claude_egress._raw(d, "p", cli, "T", 60)
        t = claude_egress.usage_totals()
        assert t["claude_calls_missing_usage"] == 1, t
        assert t["claude_cost_usd"] == 0.0 and t["claude_calls"] == 1, t

        claude_egress.reset_usage()
        os.environ["CLAUDE_USAGE_STRICT"] = "1"
        raised = False
        try:
            claude_egress._raw(d, "p", cli, "T", 60)
        except claude_egress.UsageUnattributable:
            raised = True
        assert raised, "strict mode priced a zero-token result as free"
    finally:
        os.environ.pop("CLAUDE_USAGE_STRICT", None)
        shutil.rmtree(d, ignore_errors=True)


def test_strict_mode_hard_fails_an_unpriceable_call():
    for payload in ("plain text", '{"type":"something_else","result":"x"}', ""):
        d, cli = _fake_cli(payload)
        try:
            claude_egress.reset_usage()
            os.environ["CLAUDE_USAGE_STRICT"] = "1"
            raised = False
            try:
                claude_egress._raw(d, "p", cli, "T", 60)
            except claude_egress.UsageUnattributable:
                raised = True
            assert raised, f"strict mode accepted an unpriceable call: {payload!r}"
        finally:
            os.environ.pop("CLAUDE_USAGE_STRICT", None)
            shutil.rmtree(d, ignore_errors=True)


# ---------------------------------------------------------------------------
# Routing economics arm C: the frozen rule becomes ACTIONABLE only under an explicit
# opt-in, and rows produced while acting must be separable from the observational log.
# ---------------------------------------------------------------------------
capability_shadow = _load("capability_shadow", "capability_shadow.py")


def test_rule_fingerprint_covers_thresholds_and_predicate():
    """A rule is its parameters AND its predicate; changing either must change the id."""
    fp = capability_shadow.rule_fingerprint()
    assert fp.startswith("v1:") and len(fp) > 10, fp
    orig = capability_shadow.FILES_NOW_MIN
    try:
        capability_shadow.FILES_NOW_MIN = orig + 1
        assert capability_shadow.rule_fingerprint() != fp, "threshold change did not move the fingerprint"
    finally:
        capability_shadow.FILES_NOW_MIN = orig
    assert capability_shadow.rule_fingerprint() == fp


def test_observer_defaults_to_not_acted():
    """Every ordinary build must keep producing observational rows."""
    assert capability_shadow.Observer("/tmp/x").acted is False


def test_escalate_on_rule_is_off_by_default():
    """Arm C must be opt-in: with the flag unset the rule can only observe."""
    import subprocess as _sp
    import sys as _sys
    probe = ("import os,sys;sys.path.insert(0,'.');"
             "import importlib.util as u;"
             "s=u.spec_from_file_location('rb','run-build.py');m=u.module_from_spec(s);"
             "sys.modules['rb']=m;\n"
             "try:\n s.loader.exec_module(m)\n"
             "except SystemExit:\n pass\n"
             "print(m.ESCALATE_ON_RULE)")
    env = {k: v for k, v in os.environ.items() if k != "ESCALATE_ON_RULE"}
    r = _sp.run([_sys.executable, "-c", probe], cwd=HERE, capture_output=True, text=True, env=env)
    assert r.stdout.strip().endswith("False"), r.stdout[-200:] + r.stderr[-200:]
    env["ESCALATE_ON_RULE"] = "1"
    r = _sp.run([_sys.executable, "-c", probe], cwd=HERE, capture_output=True, text=True, env=env)
    assert r.stdout.strip().endswith("True"), r.stdout[-200:] + r.stderr[-200:]


def test_shadow_record_carries_acted_and_rule_identity():
    d = tempfile.mkdtemp()
    log = os.path.join(d, "shadow.jsonl")
    old = capability_shadow.LOG
    try:
        capability_shadow.LOG = log
        o = capability_shadow.Observer(d)
        o.observe([("a.al", "AL0133"), ("b.al", "AL0132")], 0)
        o.observe([("a.al", "AL0133"), ("b.al", "AL0132")], 1)
        o.acted = True
        o.finish(False, False)
        rec = json.loads(open(log).read().strip().splitlines()[-1])
        assert rec["acted"] is True, rec
        assert rec["rule_version"] == "v1", rec
        assert rec["rule_fingerprint"].startswith("v1:"), rec
    finally:
        capability_shadow.LOG = old
        shutil.rmtree(d, ignore_errors=True)


# ---------------------------------------------------------------------------
# Cumulative suite spend is TELEMETRY. A cap driven by realised cost would make the
# stopping rule depend on an outcome, so the ledger must expose nothing to branch on.
# ---------------------------------------------------------------------------
bench_ledger = _load("bench_ledger", "bench_ledger.py")


def test_ledger_totals_are_descriptive_not_a_verdict():
    """No threshold, no predicate, no boolean — nothing a driver could stop on."""
    d = tempfile.mkdtemp()
    m = os.path.join(d, "metrics.jsonl")
    with open(m, "w") as fh:
        for cost in (0.25, 0.75):
            fh.write(json.dumps({"project": "x__suiteA__r1", "claude_cost_usd": cost,
                                 "claude_calls": 2, "claude_input_tokens": 100,
                                 "claude_output_tokens": 10}) + "\n")
    old_m, old_l = bench_ledger.METRICS, bench_ledger.LEDGER
    try:
        bench_ledger.METRICS = m
        bench_ledger.LEDGER = os.path.join(d, "ledger.jsonl")
        t = bench_ledger.totals("suiteA")
        assert t["runs"] == 2 and abs(t["cost_usd"] - 1.0) < 1e-9, t
        assert not any(isinstance(v, bool) for v in t.values()), \
            f"ledger exposes a boolean a driver could branch on: {t}"
        assert not any(k for k in t if "limit" in k or "cap" in k or "exceed" in k), t
    finally:
        bench_ledger.METRICS, bench_ledger.LEDGER = old_m, old_l
        shutil.rmtree(d, ignore_errors=True)


def test_ledger_is_fail_open_on_a_missing_metrics_file():
    """Telemetry must never be the reason a suite stops."""
    old_m, old_l = bench_ledger.METRICS, bench_ledger.LEDGER
    try:
        bench_ledger.METRICS = "/nonexistent/metrics.jsonl"
        bench_ledger.LEDGER = "/nonexistent/dir/ledger.jsonl"
        t = bench_ledger.totals("anything")
        assert t["runs"] == 0 and t["cost_usd"] == 0.0, t
        assert isinstance(bench_ledger.note("anything"), str)
    finally:
        bench_ledger.METRICS, bench_ledger.LEDGER = old_m, old_l


def test_ledger_flags_unpriced_rows_without_hiding_them():
    d = tempfile.mkdtemp()
    m = os.path.join(d, "metrics.jsonl")
    with open(m, "w") as fh:
        fh.write(json.dumps({"project": "x__suiteB__r1", "claude_cost_usd": 0.5,
                             "claude_calls": 1, "claude_calls_missing_usage": 1}) + "\n")
    old_m, old_l = bench_ledger.METRICS, bench_ledger.LEDGER
    try:
        bench_ledger.METRICS = m
        bench_ledger.LEDGER = os.path.join(d, "ledger.jsonl")
        assert bench_ledger.totals("suiteB")["rows_missing_usage"] == 1
        assert "INCOMPLETE" in bench_ledger.note("suiteB")
    finally:
        bench_ledger.METRICS, bench_ledger.LEDGER = old_m, old_l
        shutil.rmtree(d, ignore_errors=True)


# ---------------------------------------------------------------------------
# A damaged run-dir .git makes git DISCOVER AN ANCESTOR repository. Both mutation
# boundaries must fail closed rather than target it. routecon4/map/r4 committed six
# benchmark artifacts into the setup repo this way, because the map fixture's cleanup.sh
# omits .git from its exclusion list and deletes .git/HEAD and .git/config.
# ---------------------------------------------------------------------------
anon_workspace = _load("anon_workspace", "anon_workspace.py")


def _nested_damaged_repo():
    """An outer repo containing a child whose .git is present but headless."""
    import subprocess as sp
    outer = tempfile.mkdtemp()
    sp.run(["git", "init", "-q"], cwd=outer, check=True)
    open(os.path.join(outer, "keep.txt"), "w").write("x")
    sp.run(["git", "add", "-A"], cwd=outer, check=True)
    sp.run(["git", "-c", "user.email=a@b", "-c", "user.name=a",
            "commit", "-qm", "base"], cwd=outer, check=True)
    child = os.path.join(outer, "child")
    os.makedirs(child)
    open(os.path.join(child, "app.json"), "w").write("{}")
    sp.run(["git", "init", "-q"], cwd=child, check=True)
    # exactly what cleanup.sh does: remove the files that make it a repo, keep the dir
    for f in ("HEAD", "config"):
        p = os.path.join(child, ".git", f)
        if os.path.exists(p):
            os.remove(p)
    return outer, child


def test_mirror_refuses_when_git_discovers_an_ancestor():
    outer, child = _nested_damaged_repo()
    try:
        top = subprocess.run(["git", "rev-parse", "--show-toplevel"], cwd=child,
                             capture_output=True, text=True).stdout.strip()
        assert os.path.realpath(top) == os.path.realpath(outer), \
            "test setup failed: git did not discover the ancestor"
        raised = ""
        try:
            anon_workspace.run_workspace(child, "p", lambda m, p: None)
        except RuntimeError as e:
            raised = str(e)
        assert "not the project root" in raised, raised or "no RuntimeError raised"
    finally:
        shutil.rmtree(outer, ignore_errors=True)


def test_autocommit_refuses_to_commit_an_ancestor_repo():
    outer, child = _nested_damaged_repo()
    try:
        before = subprocess.run(["git", "rev-list", "--count", "HEAD"], cwd=outer,
                                capture_output=True, text=True).stdout.strip()
        os.environ["ANON_AUTOCOMMIT"] = "1"
        import egress_policy as _ep
        _ep.set_policy_for("/nonexistent")
        os.environ["EGRESS_POLICY"] = "enterprise-anon"
        _ep.set_policy_for("/nonexistent")
        out = claude_egress.run_claude(child, "p", "/bin/echo", label="T", timeout=30)
        after = subprocess.run(["git", "rev-list", "--count", "HEAD"], cwd=outer,
                               capture_output=True, text=True).stdout.strip()
        assert before == after, f"ancestor repo gained a commit: {before} -> {after}"
        assert out == "", "a refused call must return empty, not proceed"
    finally:
        os.environ.pop("ANON_AUTOCOMMIT", None)
        shutil.rmtree(outer, ignore_errors=True)


# ---------------------------------------------------------------------------
# AL_RULES.md is GENERATED. The property that matters is the refusal: a ruleset
# that looks complete while silently omitting the house rules is worse than no
# file, because the reader cannot tell. The old hand-written one drifted 4.3
# months precisely because nothing could detect that it was wrong.
# ---------------------------------------------------------------------------
al_rules_gen = _load("al_rules_gen", "al_rules_gen.py")


def _rules_gen_in(tmp, addendum_text):
    """Point the generator at a scratch addendum + output. Real sources untouched."""
    add = os.path.join(tmp, "house-addendum.md")
    with open(add, "w") as fh:
        fh.write(addendum_text)
    al_rules_gen.ADDENDUM = add
    al_rules_gen.SOURCES = [al_rules_gen.GOTCHAS, al_rules_gen.SYNTAX, add]
    al_rules_gen.OUT = os.path.join(tmp, "AL_RULES.md")
    return al_rules_gen.OUT


def test_rules_gen_refuses_an_unfilled_addendum_and_writes_nothing():
    d = tempfile.mkdtemp()
    old = (al_rules_gen.ADDENDUM, al_rules_gen.SOURCES, al_rules_gen.OUT)
    try:
        out = _rules_gen_in(d, "## 1. Labels\n\n> TODO(grounding): the house Label rule.\n")
        assert al_rules_gen.build() == 1, "must refuse while a TODO(grounding) remains"
        assert not os.path.exists(out), "refusing must not leave a partial ruleset behind"
    finally:
        al_rules_gen.ADDENDUM, al_rules_gen.SOURCES, al_rules_gen.OUT = old
        shutil.rmtree(d, ignore_errors=True)


def test_rules_gen_emits_when_filled_and_detects_a_stale_source():
    import sys as _sys
    d = tempfile.mkdtemp()
    old = (al_rules_gen.ADDENDUM, al_rules_gen.SOURCES, al_rules_gen.OUT)
    argv = _sys.argv[:]
    try:
        out = _rules_gen_in(d, "## 1. Labels\n\nUse Locked = true for non-translatable text.\n")
        _sys.argv = ["al_rules_gen"]
        assert al_rules_gen.main() == 0, "a filled addendum must emit"
        body = open(out).read()
        assert "# house rules" in body, "the house-rules boundary must be visible in the output"
        assert "GENERATED FILE" in body, body[:200]

        _sys.argv = ["al_rules_gen", "--check"]
        assert al_rules_gen.main() == 0, "freshly generated must check clean"

        # Paths in the output must be forward-slashed on every platform. relpath yields
        # backslashes on Windows: broken markdown links, and the tracked file churns
        # whenever the other box regenerates it. Caught by exactly that churn.
        assert "\\" not in body, "generated paths must not contain backslashes"
        assert "reference/al-reference/00-gotchas.md" in body, body[:400]

        with open(al_rules_gen.ADDENDUM, "a") as fh:
            fh.write("\n## 2. Added later\n")
        assert al_rules_gen.main() == 1, "a changed source must report the file as stale"
    finally:
        _sys.argv = argv
        al_rules_gen.ADDENDUM, al_rules_gen.SOURCES, al_rules_gen.OUT = old
        shutil.rmtree(d, ignore_errors=True)


# ── Repair-phase knowledge ──────────────────────────────────────────────────────
# The AL-REFERENCE injection reaches the WRITE prompt only. Proving a rule exists in
# the reference, or that the write prompt carries it, says nothing about the prompt
# that actually failed. doclink 2026-09-01: the inline-var rule was injected, the write
# phase obeyed it, and a fix round then introduced the very construct it forbids —
# because no repair prompt has ever carried the rule. These tests assert the invariant
# in the REPAIR path specifically.

# The real captured cluster: 31x AL0104 + 15x AL0107 from ONE mid-body declaration.
DOCLINK_INLINE_VAR_DIAGS = """\
{p}(25,9): error AL0104: Syntax error, 'end' expected
{p}(25,9): error AL0104: Syntax error, ';' expected
{p}(26,24): error AL0104: Syntax error, ':' expected
{p}(26,24): error AL0107: Syntax error, identifier expected. Provide a valid name (letters, digits, and underscores only).
{p}(26,31): error AL0104: Syntax error, ':' expected
"""

# Line 25 is the declaration; the compiler blames it for a missing `end`.
DOCLINK_INLINE_VAR_SRC = "\n".join(
    ["codeunit 50000 \"Probe\"", "{", "    procedure P()", "    var", "        Setup: Record Customer;",
     "    begin"] + ["        // filler"] * 18 +
    ['        var ApiVersionEnum: Enum "Storage Service API Version";',
     '        ApiVersionEnum := Enum::"Storage Service API Version"::"2022-11-02";',
     "    end;", "}"])


def _hints_for(src, diags_tmpl):
    """Run known_fix_hints against a real file on disk, as the fix loop does."""
    d = tempfile.mkdtemp()
    try:
        os.makedirs(os.path.join(d, "src"))
        p = os.path.join(d, "src", "PTEDocumentLinkAZMgt.Codeunit.al")
        with open(p, "w") as fh:
            fh.write(src)
        old = rb.PROJECT_ROOT
        rb.PROJECT_ROOT = d
        try:
            return rb.known_fix_hints(diags_tmpl.format(p=p)), p
        finally:
            rb.PROJECT_ROOT = old
    finally:
        shutil.rmtree(d, ignore_errors=True)


def test_rewrite_prompt_states_the_inline_declaration_invariant():
    """The prompt that reintroduced the defect must forbid it.

    Fails against pre-change code: build_file_rewrite_msg listed try/except, throw,
    switch and `{ }` — and said nothing about where a variable may be declared."""
    msg = rb.build_file_rewrite_msg("", "src/X.Codeunit.al", "some errors")
    low = msg.lower()
    assert "inline declaration" in low, "rewrite prompt does not forbid inline declarations"
    assert "var" in low and "begin" in low, "rewrite prompt does not say WHERE declarations go"
    # It must survive the no-spec path too: handover_file_spec returns "" whenever the
    # handover has no verbatim block for the file, and that is the common case.
    assert "inline declaration" in rb.build_file_rewrite_msg(
        "unrelated handover text", "src/X.Codeunit.al", "errs").lower()


def test_known_fix_hints_names_the_mid_body_declaration():
    """Given the ACTUAL diagnostic cluster, the hint must name the cause, file and line.

    Fails against pre-change code: known_fix_hints covered AL0282, AL0175 and AL0133
    and returned no hint at all for this cluster ('known-fix: 0 hint(s) appended')."""
    hints, _ = _hints_for(DOCLINK_INLINE_VAR_SRC, DOCLINK_INLINE_VAR_DIAGS)
    assert "line 25" in hints, f"hint does not point at the offending line:\n{hints}"
    assert "ApiVersionEnum" in hints, "hint does not quote the offending declaration"
    assert "NOT a missing keyword" in hints, "hint does not contradict the compiler's message"
    assert "already balance" in hints, "hint does not stop the model chasing end/until"
    # One defect, one hint — 31 AL0104 diagnostics must not become 31 hints.
    assert hints.count("is NOT a missing keyword") == 1, "hint duplicated per diagnostic"


def test_known_fix_hints_does_not_fire_on_a_real_unbalanced_block():
    """Negative control. A genuine missing `end` also emits AL0104 'end' expected.

    Without this, the hint would tell the model to 'move the declaration' on every
    structurally broken file — replacing one wrong instruction with another.

    Exempt from the file's fail-before-the-change rule, and deliberately so: pre-change
    there is no hint to over-fire, so this passes against HEAD. It guards the blast
    radius of the NEW hint, not the old gap. Do not read its pre-change pass as
    coverage — the two tests above are the ones that prove the change landed."""
    src = "\n".join([
        'codeunit 50000 "Probe"', "{", "    procedure P()", "    var",
        "        ApiVersionEnum: Integer;",   # a LEGAL var section
        "    begin", "        if true then", "    end;", "}"])
    diags = "{p}(7,9): error AL0104: Syntax error, 'end' expected\n"
    hints, _ = _hints_for(src, diags)
    assert "missing keyword" not in hints, (
        f"inline-var hint fired on a legally-declared variable:\n{hints}")


# ── AL0151: option syntax on a non-option receiver ──────────────────────────────
# Evidence: reference/al0151-investigation.md (46 recovered sites) + compiler probes.
# The hint must key on the RECEIVER and stay silent whenever the blamed line does not
# actually show one — the diagnostic alone is not licence to speak.

AL0151_DIAG = "{p}({ln},{col}): error AL0151: Expression must be an Option type. " \
              "Use '::' to access option members (e.g., MyOption::Value).\n"


def _fix_section(h):
    """Only the KNOWN FIXES block. known_fix_hints also appends the al-errors KB, which
    since 84e2247 documents AL0151 with the same Clear()/IsNullGuid() idioms — asserting
    over the whole string tests the KB, not the hint."""
    return h.split("DIAGNOSTIC KNOWLEDGE")[0]


def _al0151_hints(src_line, col):
    """known_fix_hints against a real file whose blamed line is `src_line`."""
    body = ["codeunit 50000 \"P\"", "{", "    procedure P()", "    begin", src_line,
            "    end;", "}"]
    return _fix_section(
        _hints_for("\n".join(body),
                   AL0151_DIAG.replace("{ln}", "5").replace("{col}", str(col)))[0])


def test_al0151_hint_names_the_media_receiver():
    """`Media::""` — the single most common site in the corpus (19 of 46)."""
    h = _al0151_hints('        Rec."Document Reference ID" := Media::"";', 44)
    assert "`Media::...`" in h, f"receiver not named:\n{h}"
    assert "NOT an Option/Enum type" in h, "hint does not state why the receiver is wrong"
    assert "Clear(" in h, "hint does not give the verified Media remediation"
    assert "RECEIVER, not the member name" in h, "hint does not redirect off the member"


def test_al0151_hint_names_the_guid_receiver():
    h = _al0151_hints('        if Rec."Id".MediaId() = Guid::Zero then exit;', 45)
    assert "`Guid::...`" in h, f"receiver not named:\n{h}"
    assert "IsNullGuid" in h, "hint does not give the verified Guid remediation"


def test_al0151_hint_is_silent_without_a_receiver_on_the_blamed_line():
    """AL0151 whose blamed line shows no `Receiver::` at all.

    Without this the hint would tell the model to go looking for a receiver that is
    not there — replacing one wrong instruction with another, exactly the failure the
    inline-var guard was built to avoid.

    Exempt from the fail-before-the-change rule, deliberately: pre-change there is no
    AL0151 hint to over-fire, so this passes against HEAD. It guards the blast radius
    of the NEW hint. The four tests around it are the ones proving the change landed."""
    h = _al0151_hints('        Rec.Validate("No.", SomeValue);', 20)
    assert "AL0151" not in h, f"hint fired with no `::` on the line:\n{h}"


def test_al0151_hint_handles_an_unknown_receiver_without_inventing_a_fix():
    """A receiver outside the known Media/Guid set still gets the receiver diagnosis,
    but must NOT be handed a fabricated remediation."""
    h = _al0151_hints('        x := ObjectType::Table;', 25)
    assert "`ObjectType::...`" in h, f"receiver not named:\n{h}"
    assert "Clear(" not in h and "IsNullGuid" not in h, "invented a Media/Guid fix"
    assert "use the type's own API" in h, "no generic guidance for an unknown receiver"


def test_al0151_hint_is_one_per_site_not_one_per_diagnostic():
    src = "\n".join(["codeunit 50000 \"P\"", "{", "    procedure P()", "    begin",
                     '        Rec."X" := Media::"";', "    end;", "}"])
    diags = (AL0151_DIAG.replace("{ln}", "5").replace("{col}", "28")
             + AL0151_DIAG.replace("{ln}", "5").replace("{col}", "28"))
    h = _fix_section(_hints_for(src, diags)[0])
    assert h.count("AL0151 at") == 1, f"duplicated per diagnostic:\n{h}"


if __name__ == "__main__":
    fns = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    for fn in fns:
        fn()
        print(f"  ok  {fn.__name__}")
    if SKIPPED:
        print("\nSKIPPED (not passes):")
        for s in SKIPPED:
            print(f"  -- {s}")
    print(f"\n{len(fns) - len(SKIPPED)}/{len(fns)} PASS"
          + (f", {len(SKIPPED)} skipped" if SKIPPED else ""))
