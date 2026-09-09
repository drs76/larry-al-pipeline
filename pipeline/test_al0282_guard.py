"""Tests for the AL0282 table-event subscriber guard in run-build.py.

The guard renames subscriber params to their published names (Rec / xRec /
RunTrigger / CurrFieldNo). It matched procedure declarations with a bare `\\w+`,
so a QUOTED name — legal AL, and what models reach for when the name embeds an
object name with a space — was silently skipped and the AL0282 survived. Seen on
bench-p4 (Qwen3.8): the build plateaued at 2 errors for 3 fix rounds on exactly
the error this guard exists to remove.

Run: python3 test_al0282_guard.py
"""
import importlib.util
import os
import tempfile

_spec = importlib.util.spec_from_file_location(
    "rb", os.path.join(os.path.dirname(os.path.abspath(__file__)), "run-build.py"))
rb = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(rb)


def _run(source):
    """Run the guard over a one-file project; return the rewritten source."""
    with tempfile.TemporaryDirectory() as d:
        os.makedirs(os.path.join(d, "src"))
        p = os.path.join(d, "src", "T.Codeunit.al")
        with open(p, "w") as f:
            f.write(source)
        rb.PROJECT_ROOT = d
        rb.normalize_table_event_subscribers()
        return open(p).read()


QUOTED = '''codeunit 50100 "Room Booking Mgt"
{
    [EventSubscriber(ObjectType::Table, Database::"Room Booking", 'OnBeforeInsertEvent', '', false, false)]
    local procedure "Room Booking_OnBeforeInsertEvent"(var RoomBooking: Record "Room Booking"; RunTrigger: Boolean)
    begin
        Validate(RoomBooking, 0);
    end;
}
'''


def test_quoted_procedure_name_is_renamed():
    out = _run(QUOTED)
    assert 'var Rec: Record "Room Booking"' in out, "param must be renamed to Rec"
    assert "RoomBooking," not in out and "RoomBooking:" not in out, "no stray old name"


def test_quoted_procedure_name_itself_is_preserved():
    # The rename must not touch the quoted identifier — it is the procedure's name,
    # not a parameter reference.
    out = _run(QUOTED)
    assert '"Room Booking_OnBeforeInsertEvent"' in out


def test_body_references_follow_the_rename():
    out = _run(QUOTED)
    assert "Validate(Rec, 0)" in out


def test_unquoted_still_works():
    out = _run('''codeunit 50101 A
{
    [EventSubscriber(ObjectType::Table, Database::Item, 'OnAfterInsertEvent', '', false, false)]
    local procedure HandleItemInsert(var Item: Record Item; RunTrigger: Boolean)
    begin
        Message('%1', Item."No.");
    end;
}
''')
    assert "var Rec: Record Item" in out, "type after 'Record ' must keep its name"
    assert 'Message(\'%1\', Rec."No.")' in out


def test_xrec_pair_on_modify():
    out = _run('''codeunit 50102 B
{
    [EventSubscriber(ObjectType::Table, Database::"Room Booking", 'OnBeforeModifyEvent', '', false, false)]
    local procedure "B_OnBeforeModifyEvent"(var RoomBooking: Record "Room Booking"; var xRoomBooking: Record "Room Booking"; RunTrigger: Boolean)
    begin
        Validate(RoomBooking);
    end;
}
''')
    assert "var Rec: Record" in out and "var xRec: Record" in out


def test_non_table_events_untouched():
    src = '''codeunit 50103 C
{
    [EventSubscriber(ObjectType::Codeunit, Codeunit::"Sales-Post", 'OnAfterPost', '', false, false)]
    local procedure "Sales Post_OnAfterPost"(var SalesHeader: Record "Sales Header")
    begin
        Message('%1', SalesHeader."No.");
    end;
}
'''
    assert _run(src) == src, "codeunit events have author-chosen param names"


def test_idempotent():
    once = _run(QUOTED)
    assert _run(once) == once


if __name__ == "__main__":
    fns = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    for fn in fns:
        fn()
        print(f"  ok  {fn.__name__}")
    print(f"\nALL {len(fns)} PASS")
