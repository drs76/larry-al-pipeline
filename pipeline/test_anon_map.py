"""Property tests for anon_map — the reversibility guarantees (phase 2).

Run: python3 test_anon_map.py   (plain asserts, no pytest dependency)
"""
import os
import tempfile

import anon_map as A


def _fresh(literals=()):
    m = A.AnonMap()
    return m, list(literals)


def test_round_trip_identity():
    m, lits = _fresh([("NAME", "Contoso Ltd"), ("NAME", "Acme")])
    src = ("Customer Contoso Ltd (Acme parent) id "
           "1234abcd-5678-9abc-def0-1234567890ab at /mnt/c/Users/dave/work.")
    scrubbed = A.forward(src, m, lits)
    assert A.reverse(scrubbed, m) == src, "round-trip must be identity"
    assert "Contoso" not in scrubbed and "Acme" not in scrubbed
    assert "1234abcd" not in scrubbed and "Users/dave" not in scrubbed


def test_no_leak():
    m, lits = _fresh([("NAME", "Umbrella Corp")])
    scrubbed = A.forward("Umbrella Corp ships widgets.", m, lits)
    assert A.residual_reals(scrubbed, m) == [], "no declared real may survive"


def test_stability_across_reload():
    lits = [("NAME", "Initech")]
    m1, _ = _fresh(lits)
    A.forward("Initech rocks", m1, lits)
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, ".anon", "map.tsv")
        m1.save(p)
        m2 = A.AnonMap().load(p)
        # same real → same placeholder after a reload (stable across runs)
        assert m2.placeholder_for("Initech", "NAME") == m1.placeholder_for("Initech", "NAME")
        # a NEW real mints the next index, never reusing an existing one
        ph_new = m2.placeholder_for("Globex", "NAME")
        assert ph_new not in m1.rev


def test_multifile_consistency():
    lits = [("HOST", "prod-db-07")]
    m, _ = _fresh(lits)
    a = A.forward("connect prod-db-07 now", m, lits)
    b = A.forward("prod-db-07 is slow", m, lits)
    # identical real across two files → identical placeholder
    pa = a.split("connect ")[1].split(" now")[0]
    assert pa in b, "same host must map to the same placeholder in both files"


def test_inverse_safety_many_indices():
    # 12 names → indices 001..012; ensure reverse of a text mixing 001 and 012
    # restores correctly (longest-first prevents ANON_NAME_001 clobbering _012).
    lits = [("NAME", f"Name{i:02d}") for i in range(1, 13)]
    m, _ = _fresh(lits)
    src = "Name01 met Name12 and Name10."
    assert A.reverse(A.forward(src, m, lits), m) == src


def test_longest_literal_first():
    lits = [("NAME", "Acme"), ("NAME", "Acme Trading Ltd")]
    m, _ = _fresh(lits)
    scrubbed = A.forward("invoice from Acme Trading Ltd today", m, lits)
    # the long name maps as one unit; 'Acme' isn't left dangling
    assert "Acme" not in scrubbed
    assert A.reverse(scrubbed, m) == "invoice from Acme Trading Ltd today"


def test_email_detector():
    # personal identifiers (enterprise ruling): emails auto-detected, reversible
    m, _ = _fresh()
    src = "Contact jane.doe@customer.co.uk and j.doe+bc@corp.com."
    s = A.forward(src, m, [])
    assert "customer.co.uk" not in s and "corp.com" not in s
    assert A.reverse(s, m) == src


def test_case_sensitive():
    lits = [("NAME", "Acme")]
    m, _ = _fresh(lits)
    scrubbed = A.forward("ACME and Acme differ", m, lits)
    # only the exact-case declared token is scrubbed (reversibility stays exact)
    assert "ACME" in scrubbed and "Acme" not in scrubbed


if __name__ == "__main__":
    fns = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    for fn in fns:
        fn()
        print(f"  ok  {fn.__name__}")
    print(f"\nALL {len(fns)} PASS")
