"""Tests for secret_gate — detection, redaction, fail-closed (phase 3).

Run: python3 test_secret_gate.py
"""
import secret_gate as S


def test_high_confidence_blocks():
    for secret in [
        "aws_key = AKIA" + "IOSFODNN7EXAMPLE",    # AKIA + 16
        "google = AIza" + "a" * 35,               # AIza + 35
        "gh = ghp_" + "a" * 36,                   # ghp_ + 36
        "slack = xoxb-1234567890-abcdefABCDEF",
        "conn = AccountKey=" + "A" * 44 + "==",   # >=40 base64
        "db = Server=x;Password=hunter2xyz;",
    ]:
        ok, red, findings = S.gate(secret)
        assert not ok, f"HIGH secret must block: {secret!r}"
        assert S.DUMMY in red, f"secret must be redacted: {secret!r}"
        assert not S.scan(red), f"no secret may survive redaction: {secret!r}"


def test_private_key_block():
    pem = ("-----BEGIN RSA PRIVATE KEY-----\nMIIEabc123\nlines\n"
           "-----END RSA PRIVATE KEY-----")
    ok, red, findings = S.gate("key:\n" + pem)
    assert not ok and S.DUMMY in red and "PRIVATE KEY" not in red


def test_med_redacts_but_allows():
    ok, red, findings = S.gate('token = "abcdefghijklmnop1234"')
    assert ok, "MED-only findings must not block"
    assert S.DUMMY in red and findings and findings[0]["confidence"] == "med"


def test_allow_high_override():
    ok, red, _ = S.gate("k = AKIAIOSFODNN7EXAMPLE", allow_high=True)
    assert ok and S.DUMMY in red, "override lets it pass but still redacts"


def test_clean_text_no_findings():
    ok, red, findings = S.gate("The retry loop backs off exponentially; see billing.go.")
    assert ok and findings == [] and red == "The retry loop backs off exponentially; see billing.go."


def test_preview_never_leaks_full_secret():
    _ok, _red, findings = S.gate("aws_key = AKIAIOSFODNN7EXAMPLE")
    assert "AKIAIOSFODNN7EXAMPLE" not in findings[0]["preview"]


if __name__ == "__main__":
    fns = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    for fn in fns:
        fn()
        print(f"  ok  {fn.__name__}")
    print(f"\nALL {len(fns)} PASS")
