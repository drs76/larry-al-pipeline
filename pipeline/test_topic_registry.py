"""Tests for run-ingest's topic selection and index registration.

Two ingests in a row filed material under the nearest stranger (the app.json manifest
reference and four analyzer-rule pages both appended to 10-quality-breaking.md, taking
it past its 8k budget). These tests pin the routing so that cannot come back, and guard
the index registrar — which edits a hand-maintained table and must fail closed rather
than mangle it.

Run: python3 test_topic_registry.py
"""
import importlib.util
import os
import shutil
import tempfile

_spec = importlib.util.spec_from_file_location(
    "ri", os.path.join(os.path.dirname(os.path.abspath(__file__)), "run-ingest.py"))
ri = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ri)

INDEX = """# AL Reference

## Topics

| Topic | Covers | Size |
|---|---|---|
| [`00-gotchas.md`](al-reference/00-gotchas.md) | LLM gotcha summary | ~0.6k tok |
| [`06-http-client.md`](al-reference/06-http-client.md) | HttpClient, RestClient | ~2.7k tok |
| [`14-namespaces.md`](al-reference/14-namespaces.md) | Namespaces & `using` | ~3.1k tok |

_Total across topics: ~47k tokens. Split by `pipeline/split_knowledge.py`._
"""


def sandbox():
    """A REFERENCE tree with a small index and matching topic files."""
    d = tempfile.mkdtemp()
    os.makedirs(os.path.join(d, "al-reference"))
    for fn, body in [("00-gotchas.md", "# Gotchas\n"),
                     ("06-http-client.md", "# HttpClient, RestClient\n" + "x" * 2000),
                     ("14-namespaces.md", "# Namespaces & using\n" + "x" * 3000)]:
        with open(os.path.join(d, "al-reference", fn), "w") as f:
            f.write(body)
    with open(os.path.join(d, "AL-REFERENCE.md"), "w") as f:
        f.write(INDEX)
    ri.REFERENCE = d
    return d


def read_index(d):
    return open(os.path.join(d, "AL-REFERENCE.md")).read()


def test_exact_filename_wins():
    d = sandbox()
    try:
        got = ri.pick_topic("AL-REFERENCE.md", "14-namespaces.md")
        assert os.path.basename(got) == "14-namespaces.md", got
        got = ri.pick_topic("AL-REFERENCE.md", "14-namespaces")   # no extension
        assert os.path.basename(got) == "14-namespaces.md", got
    finally:
        shutil.rmtree(d)


def test_generic_words_do_not_match():
    """'AL code rules' shares a word with almost every topic. One shared generic word
    must NOT be enough — that is exactly how analyzer rules landed in quality-breaking."""
    d = sandbox()
    try:
        got = ri.pick_topic("AL-REFERENCE.md", "AL code rules reference")
        assert os.path.basename(got).startswith("15-"), \
            f"a generic hint must create a topic, not pick one: {got}"
    finally:
        shutil.rmtree(d)


def test_real_hint_still_routes():
    d = sandbox()
    try:
        got = ri.pick_topic("AL-REFERENCE.md", "Namespaces and using directives")
        assert os.path.basename(got) == "14-namespaces.md", got
    finally:
        shutil.rmtree(d)


def test_new_prefix_creates_topic():
    d = sandbox()
    try:
        got = ri.pick_topic("AL-REFERENCE.md", "NEW: Report layouts")
        assert os.path.basename(got) == "15-report-layouts.md", got
        assert os.path.exists(got)
    finally:
        shutil.rmtree(d)


def test_new_topic_is_registered_in_the_index():
    d = sandbox()
    try:
        ri.new_curated_topic("AL-REFERENCE.md", "Report layouts")
        idx = read_index(d)
        assert "[`15-report-layouts.md`](al-reference/15-report-layouts.md)" in idx, idx
        assert "| Report layouts |" in idx
    finally:
        shutil.rmtree(d)


def test_registration_preserves_existing_rows_and_order():
    d = sandbox()
    try:
        ri.new_curated_topic("AL-REFERENCE.md", "Report layouts")
        rows = [l for l in read_index(d).splitlines() if l.startswith("| [`")]
        names = [l.split("`")[1] for l in rows]
        assert names == sorted(names), names
        assert "00-gotchas.md" in names and "14-namespaces.md" in names
        assert "LLM gotcha summary" in read_index(d), "existing Covers text must survive"
    finally:
        shutil.rmtree(d)


def test_sizes_are_refreshed_from_disk():
    """The index quotes sizes the budget warnings rely on, so they must not go stale."""
    d = sandbox()
    try:
        ri.new_curated_topic("AL-REFERENCE.md", "Report layouts")
        idx = read_index(d)
        # 14-namespaces.md is ~3000 bytes on disk -> ~0.8k tok, NOT the stale ~3.1k
        line = next(l for l in idx.splitlines() if "14-namespaces.md" in l)
        assert "~3.1k tok" not in line, f"stale size survived: {line}"
        # 3000-byte file at TOK=3700 bytes/k-token -> ~0.8k. Assert the real number:
        # an "or tokens. in idx" style assertion passes either way and hid a bug where
        # every size came out ~0k.
        assert "~0.8k tok" in line, f"size not recomputed correctly: {line}"
        total = next(l for l in idx.splitlines() if l.startswith("_Total"))
        assert "~0k tokens" not in total, f"total collapsed to zero: {total}"
    finally:
        shutil.rmtree(d)


def test_unparseable_index_is_left_alone():
    """Fail closed: a table we do not recognise must not be rewritten."""
    d = sandbox()
    try:
        broken = "# AL Reference\n\nno table here at all\n"
        with open(os.path.join(d, "AL-REFERENCE.md"), "w") as f:
            f.write(broken)
        ok = ri.register_topic("AL-REFERENCE.md",
                               os.path.join(d, "al-reference", "15-x.md"), "X")
        assert ok is False
        assert read_index(d) == broken, "index must be untouched when unparseable"
    finally:
        shutil.rmtree(d)


def test_registering_twice_does_not_duplicate():
    d = sandbox()
    try:
        ri.new_curated_topic("AL-REFERENCE.md", "Report layouts")
        ri.register_topic("AL-REFERENCE.md",
                          os.path.join(d, "al-reference", "15-report-layouts.md"),
                          "Report layouts")
        assert read_index(d).count("15-report-layouts.md") == 2, "one row, one link target"
    finally:
        shutil.rmtree(d)


if __name__ == "__main__":
    fns = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    for fn in fns:
        fn()
        print(f"  ok  {fn.__name__}")
    print(f"\nALL {len(fns)} PASS")
