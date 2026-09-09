"""Tests for anon_workspace (Mode B) — mirror→edit→reverse→apply (phase 4).

Uses a throwaway git repo and a FAKE coder (no Claude egress) to prove the
machinery: the coder only ever sees placeholders; real tokens land in the real repo.

Run: python3 test_anon_workspace.py
"""
import glob
import os
import subprocess
import tempfile

import anon_workspace as W


def _git(cwd, *args):
    subprocess.run(["git", *args], cwd=cwd, check=True,
                   capture_output=True, text=True,
                   env={**os.environ, "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t",
                        "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@t"})


def _mkrepo(d, files, names="NAME\tContoso Ltd\nHOST\tprod-db-07\n"):
    _git(d, "init", "-q")
    for rel, content in files.items():
        p = os.path.join(d, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True) if os.path.dirname(p) else None
        open(p, "w").write(content)
    _git(d, "add", "-A")
    _git(d, "commit", "-q", "-m", "init")
    os.makedirs(os.path.join(d, ".anon"), exist_ok=True)
    open(os.path.join(d, ".anon", "names.tsv"), "w").write(names)


def test_edit_reverses_into_real_repo():
    with tempfile.TemporaryDirectory() as d:
        _mkrepo(d, {"svc.py": "# owner: Contoso Ltd\nhost = 'prod-db-07'\n"})

        def coder(mirror, _prompt):
            # the coder sees ONLY placeholders
            src = open(os.path.join(mirror, "svc.py")).read()
            assert "Contoso" not in src and "prod-db-07" not in src
            assert "ANON_NAME_001" in src and "ANON_HOST_001" in src
            # it edits in placeholder space (as Claude would)
            open(os.path.join(mirror, "svc.py"), "w").write(
                src + "# reviewed owner ANON_NAME_001 on host ANON_HOST_001\n")

        res = W.run_workspace(d, "review", coder)
        assert res["changed"] and res["applied"], res
        real = open(os.path.join(d, "svc.py")).read()
        # real tokens restored, no placeholder leaked into the real repo
        assert "# reviewed owner Contoso Ltd on host prod-db-07" in real
        assert "ANON_" not in real


def test_new_file_reversed():
    with tempfile.TemporaryDirectory() as d:
        _mkrepo(d, {"a.txt": "Contoso Ltd\n"})

        def coder(mirror, _p):
            open(os.path.join(mirror, "NOTES.md"), "w").write(
                "customer ANON_NAME_001 signed off\n")

        res = W.run_workspace(d, "add notes", coder)
        assert res["changed"] and res["applied"], res
        assert open(os.path.join(d, "NOTES.md")).read() == "customer Contoso Ltd signed off\n"


def test_high_secret_aborts_run():
    with tempfile.TemporaryDirectory() as d:
        _mkrepo(d, {"cfg.py": "AWS = 'AKIA" + "IOSFODNN7EXAMPLE'\n"})
        called = {"n": 0}

        def coder(_m, _p):
            called["n"] += 1

        try:
            W.run_workspace(d, "x", coder)
            assert False, "must raise SecretAbort"
        except W.SecretAbort as e:
            assert e.rel == "cfg.py"
        assert called["n"] == 0, "coder must never run when a secret is present"
        # real repo untouched
        assert "AKIA" in open(os.path.join(d, "cfg.py")).read()


def test_no_change_is_noop():
    with tempfile.TemporaryDirectory() as d:
        _mkrepo(d, {"a.txt": "Contoso Ltd\n"})
        res = W.run_workspace(d, "noop", lambda m, p: None)
        assert res["changed"] is False


if __name__ == "__main__":
    fns = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    for fn in fns:
        fn()
        print(f"  ok  {fn.__name__}")
    print(f"\nALL {len(fns)} PASS")
