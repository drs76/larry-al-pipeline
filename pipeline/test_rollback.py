"""Tests for keep-best rollback — it must restore the EXACT snapshot tree.

The security review found that `restore_src()` only rewrote the files it had captured,
so a file CREATED by a regressing fix round survived the rollback. The tree ended up as
"best files + the bad round's additions", which is not the state keep-best promises and
silently violates the no-regress invariant the build loop is built on.

`run-build-cs.py` already removed post-snapshot files; `run-build.py` (AL) and
`run-build-go.py` did not. These tests cover AL and Go.

Assertions compare the whole TREE, not file contents — a content-only check passes while
an extra file sits beside the restored ones, which is exactly the bug.

Run: python3 test_rollback.py
"""
import importlib.util
import os
import shutil
import tempfile


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)
    except SystemExit:
        pass
    return mod


HERE = os.path.dirname(os.path.abspath(__file__))
rb = _load("rb", os.path.join(HERE, "run-build.py"))
gb = _load("gb", os.path.join(HERE, "run-build-go.py"))


def tree(root):
    """Relative path -> content, for every file under root. The comparison unit."""
    out = {}
    for dp, _, fs in os.walk(root):
        for fn in fs:
            p = os.path.join(dp, fn)
            out[os.path.relpath(p, root)] = open(p).read()
    return out


# ---------------------------------------------------------------- AL (run-build.py)

def _al_project():
    d = tempfile.mkdtemp()
    os.makedirs(os.path.join(d, "src", "codeunit"))
    open(os.path.join(d, "src", "a.al"), "w").write("original a\n")
    open(os.path.join(d, "src", "existing.js"), "w").write("original js\n")
    open(os.path.join(d, "src", "codeunit", "deep.al"), "w").write("original deep\n")
    open(os.path.join(d, "app.json"), "w").write('{"id":"x"}\n')
    rb.PROJECT_ROOT = d
    return d


def test_al_rollback_removes_files_created_by_the_bad_round():
    d = _al_project()
    try:
        before = tree(d)
        snap = rb.snapshot_src()
        open(os.path.join(d, "src", "new.al"), "w").write("created by bad round\n")
        rb.restore_src(snap)
        assert tree(d) == before, f"residue: {set(tree(d)) - set(before)}"
    finally:
        shutil.rmtree(d)


def test_al_rollback_full_mixed_round():
    """The review's exact scenario: modify + delete + create, nested, mixed asset types."""
    d = _al_project()
    try:
        before = tree(d)
        snap = rb.snapshot_src()
        open(os.path.join(d, "src", "a.al"), "w").write("MODIFIED\n")
        open(os.path.join(d, "src", "existing.js"), "w").write("MODIFIED\n")
        os.remove(os.path.join(d, "app.json"))
        open(os.path.join(d, "src", "new.al"), "w").write("new\n")
        open(os.path.join(d, "src", "new.js"), "w").write("new\n")
        os.makedirs(os.path.join(d, "src", "sub"), exist_ok=True)
        open(os.path.join(d, "src", "sub", "nested.al"), "w").write("new nested\n")
        rb.restore_src(snap)
        assert tree(d) == before, (
            f"missing={set(before) - set(tree(d))} extra={set(tree(d)) - set(before)}")
    finally:
        shutil.rmtree(d)


def test_al_rollback_restores_a_deleted_file():
    d = _al_project()
    try:
        before = tree(d)
        snap = rb.snapshot_src()
        os.remove(os.path.join(d, "src", "a.al"))
        rb.restore_src(snap)
        assert tree(d) == before
    finally:
        shutil.rmtree(d)


def test_al_rollback_leaves_out_of_scope_files_alone():
    """Rollback must not reach beyond what snapshot_src() captures — a README or a
    .alpackages dir is not the fix loop's business."""
    d = _al_project()
    try:
        open(os.path.join(d, "README.md"), "w").write("untouched\n")
        snap = rb.snapshot_src()
        rb.restore_src(snap)
        assert os.path.exists(os.path.join(d, "README.md"))
    finally:
        shutil.rmtree(d)


# ------------------------------------------------------------- Go (run-build-go.py)

def _go_project():
    d = tempfile.mkdtemp()
    os.makedirs(os.path.join(d, "cmd"))
    open(os.path.join(d, "main.go"), "w").write("package main\n")
    open(os.path.join(d, "cmd", "x.go"), "w").write("package cmd\n")
    open(os.path.join(d, "go.mod"), "w").write("module x\n")
    gb.PROJECT_ROOT = d
    return d


def test_go_rollback_removes_files_created_by_the_bad_round():
    d = _go_project()
    try:
        before = tree(d)
        snap = gb.snapshot_src()
        open(os.path.join(d, "extra.go"), "w").write("created by bad round\n")
        gb.restore_src(snap)
        assert tree(d) == before, f"residue: {set(tree(d)) - set(before)}"
    finally:
        shutil.rmtree(d)


def test_go_rollback_full_mixed_round():
    d = _go_project()
    try:
        before = tree(d)
        snap = gb.snapshot_src()
        open(os.path.join(d, "main.go"), "w").write("MODIFIED\n")
        os.remove(os.path.join(d, "go.mod"))
        open(os.path.join(d, "cmd", "new.go"), "w").write("new\n")
        gb.restore_src(snap)
        assert tree(d) == before, (
            f"missing={set(before) - set(tree(d))} extra={set(tree(d)) - set(before)}")
    finally:
        shutil.rmtree(d)


if __name__ == "__main__":
    fns = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    for fn in fns:
        fn()
        print(f"  ok  {fn.__name__}")
    print(f"\nALL {len(fns)} PASS")
