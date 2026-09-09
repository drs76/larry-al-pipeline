namespace SinclairSoftScotland.RuntimeProbes;

/// <summary>
/// Runtime assertions for AL-REFERENCE claims that no compiler or code cop can check.
///
/// AL-SYNTAX.md is guarded two ways at build time: validate_al_syntax.py proves the ✓
/// patterns compile, probe_al_rules.sh proves the ✗ patterns fail with the cited codes.
/// Neither can touch a claim about what happens when the code RUNS — and those drift
/// silently, because nothing ever contradicts them. This codeunit is that third guard.
///
/// Assertions are hand-rolled (a test fails when it errors) so the extension carries NO
/// dependency on Microsoft's test libraries — it compiles against plain platform symbols
/// and publishes anywhere. Only the Test Runner itself is needed, which `bcl test`
/// provides.
///
/// Each test names the documented claim it defends. If one fails, the claim is stale:
/// fix AL-REFERENCE, do not weaken the test.
/// </summary>
codeunit 50110 "Probe Runtime Tests"
{
    Subtype = Test;
    TestPermissions = Disabled;

    // --- CLAIM (gotcha table): a typed JSON getter THROWS on a missing key. ----------
    [Test]
    procedure TypedJsonGetterThrowsOnMissingKey()
    var
        JObj: JsonObject;
        Result: Text;
    begin
        JObj.ReadFrom('{"present":"yes"}');
        asserterror Result := JObj.GetText('absent');
    end;

    [Test]
    procedure JsonTypedGetterReturnsPresentValue()
    var
        JObj: JsonObject;
    begin
        JObj.ReadFrom('{"present":"yes"}');
        AssertEqual('yes', JObj.GetText('present'), 'a present key must round-trip');
    end;

    // Get(Key, var Token) is the safe probe — it returns FALSE rather than throwing.
    // (There is NO GetText(Key, DefaultValue) overload: the 2-arg form's second
    // argument is a Boolean, not a fallback value — verified by the compiler.)
    [Test]
    procedure JsonGetReturnsFalseForMissingKey()
    var
        JObj: JsonObject;
        JTok: JsonToken;
    begin
        JObj.ReadFrom('{"present":"yes"}');
        AssertFalse(JObj.Get('absent', JTok), 'Get must report a missing key, not throw');
        AssertTrue(JObj.Get('present', JTok), 'Get must find a present key');
    end;

    // The 2-arg form is the SAFE one: it does not throw on a missing key, it yields the
    // empty text. (Established by this harness — the first version of this test asserted
    // it threw, and the runtime disagreed.) Note the second argument is a Boolean, NOT a
    // default value: `GetText('k', 'fallback')` is AL0133 at compile time.
    [Test]
    procedure JsonTwoArgGetterIsSafeOnMissingKey()
    var
        JObj: JsonObject;
        Result: Text;
    begin
        JObj.ReadFrom('{"present":"yes"}');
        Result := JObj.GetText('absent', true);
        AssertEqual('', Result, '2-arg getter must yield empty for a missing key, not throw');
    end;

    // --- CLAIM (gotcha table §24): interface `as` ERRORS on an invalid cast — always
    //     guard with `is` first. Casting applies to INTERFACE values; a Codeunit
    //     variable does not support it at all (AL0851). ------------------------------
    [Test]
    procedure InterfaceAsErrorsOnInvalidCast()
    var
        ImplA: Codeunit "Probe Impl A";
        Face: Interface "Probe IFace";
        Other: Interface "Probe IOther";
    begin
        Face := ImplA;      // "Probe Impl A" implements IFace only, never IOther
        asserterror Other := Face as "Probe IOther";
    end;

    [Test]
    procedure InterfaceIsGuardsTheCast()
    var
        ImplA: Codeunit "Probe Impl A";
        Face: Interface "Probe IFace";
    begin
        Face := ImplA;
        AssertFalse(Face is "Probe IOther", '`is` must be false for an unimplemented interface');
    end;

    // --- CLAIM (gotcha table): AL has no `return` — `exit(value)` returns the value. --
    [Test]
    procedure ExitReturnsTheValue()
    var
        ImplA: Codeunit "Probe Impl A";
    begin
        AssertEqual('A', ImplA.Ping(), 'exit(value) must return that value to the caller');
    end;

    // --- CLAIM (gotcha table): `[TryFunction]` declares NO return type, yet the CALLER
    //     gets a Boolean. Both halves matter: declaring one is a compile error, and the
    //     caller must actually receive true/false rather than the error propagating. ---
    [Test]
    procedure TryFunctionReturnsFalseAndSwallowsTheError()
    var
        Try: Codeunit "Probe Try";
    begin
        AssertFalse(Try.AlwaysFails(), 'a failing TryFunction must return FALSE to the caller');
    end;

    [Test]
    procedure TryFunctionReturnsTrueOnSuccess()
    var
        Try: Codeunit "Probe Try";
    begin
        AssertTrue(Try.AlwaysSucceeds(), 'a succeeding TryFunction must return TRUE');
    end;

    // --- CLAIM (gotcha table): table TRIGGERS are OnInsert/OnModify — and they run only
    //     when the caller passes RunTrigger = true. -----------------------------------
    [Test]
    procedure InsertWithRunTriggerFiresOnInsert()
    var
        ProbeTbl: Record "Probe Tbl";
    begin
        ProbeTbl.Init();
        ProbeTbl."Entry No." := 1;
        ProbeTbl.Insert(true);
        AssertEqual('ONINSERT', ProbeTbl."Trigger Mark", 'Insert(true) must run the OnInsert trigger');
    end;

    [Test]
    procedure InsertWithoutRunTriggerSkipsOnInsert()
    var
        ProbeTbl: Record "Probe Tbl";
    begin
        ProbeTbl.Init();
        ProbeTbl."Entry No." := 2;
        ProbeTbl.Insert(false);
        AssertEqual('', ProbeTbl."Trigger Mark", 'Insert(false) must NOT run the trigger');
    end;

    [Test]
    procedure ModifyWithRunTriggerFiresOnModify()
    var
        ProbeTbl: Record "Probe Tbl";
    begin
        ProbeTbl.Init();
        ProbeTbl."Entry No." := 3;
        ProbeTbl.Insert(false);
        ProbeTbl.Modify(true);
        AssertEqual('ONMODIFY', ProbeTbl."Trigger Mark", 'Modify(true) must run the OnModify trigger');
    end;

    // --- CLAIM (§7 / AL0282): an auto-event subscriber binds its parameters BY NAME to
    //     the publisher's (Rec / RunTrigger). If that contract broke, the subscriber
    //     would silently stop firing — and the compiler would still be happy. ----------
    [Test]
    procedure TableEventSubscriberFires()
    var
        ProbeTbl: Record "Probe Tbl";
        Sink: Codeunit "Probe Event Sink";
    begin
        Sink.Reset();
        ProbeTbl.Init();
        ProbeTbl."Entry No." := 4;
        ProbeTbl.Insert(true);
        AssertTrue(Sink.Fired(), 'OnBeforeInsertEvent subscriber must fire on Insert');
        AssertEqual('4', Format(Sink.EntryNo()), 'the subscriber must see the record being inserted');
    end;

    // --- CLAIM (gotcha table): guard DeleteAll with IsEmpty. Proves IsEmpty tracks the
    //     table honestly, which is what makes the guard meaningful. -------------------
    [Test]
    procedure IsEmptyTracksTheTable()
    var
        ProbeTbl: Record "Probe Tbl";
    begin
        ProbeTbl.DeleteAll();
        AssertTrue(ProbeTbl.IsEmpty(), 'IsEmpty must be true after DeleteAll');
        ProbeTbl.Init();
        ProbeTbl."Entry No." := 5;
        ProbeTbl.Insert(false);
        AssertFalse(ProbeTbl.IsEmpty(), 'IsEmpty must be false once a row exists');
        ProbeTbl.DeleteAll();
        AssertTrue(ProbeTbl.IsEmpty(), 'DeleteAll must clear the table');
    end;

    // --- CLAIM (gotcha table): FindSet() is the iteration pattern (not Find('-')). ----
    [Test]
    procedure FindSetIteratesEveryRow()
    var
        ProbeTbl: Record "Probe Tbl";
        i: Integer;
        Seen: Integer;
    begin
        ProbeTbl.DeleteAll();
        for i := 1 to 3 do begin
            ProbeTbl.Init();
            ProbeTbl."Entry No." := i;
            ProbeTbl.Insert(false);
        end;
        ProbeTbl.Reset();
        if ProbeTbl.FindSet() then
            repeat
                Seen += 1;
            until ProbeTbl.Next() = 0;
        AssertEqual('3', Format(Seen), 'FindSet + Next must visit every row');
    end;

    // --- CLAIM (gotcha table): the ternary `X := C ? A : B` exists (2024w2), and
    //     `continue` skips a loop iteration. ------------------------------------------
    [Test]
    procedure TernaryEvaluatesTheChosenBranch()
    var
        Result: Text;
    begin
        Result := (1 = 1) ? 'yes' : 'no';
        AssertEqual('yes', Result, 'ternary must take the true branch');
        Result := (1 = 2) ? 'yes' : 'no';
        AssertEqual('no', Result, 'ternary must take the false branch');
    end;

    [Test]
    procedure ContinueSkipsTheIteration()
    var
        i: Integer;
        Counted: Integer;
    begin
        for i := 1 to 5 do begin
            if i = 3 then
                continue;
            Counted += 1;
        end;
        AssertEqual('4', Format(Counted), 'continue must skip exactly one iteration');
    end;

    // --- CLAIM (gotcha table §13): GetResourceAsText defaults to MS-DOS encoding, so a
    //     UTF-8 resource comes back mangled unless the encoding is passed. -------------
    [Test]
    procedure ResourceDefaultEncodingDiffersFromUtf8()
    var
        Res: Codeunit "Probe Resource";
    begin
        // res/encoding.txt is UTF-8 'café £100'. If the default were UTF-8 these would
        // match and the documented warning would be obsolete.
        AssertNotEqual(Res.DefaultEncoding(), Res.Utf8Encoding(),
            'default resource encoding must differ from UTF8 — that is the whole gotcha');
    end;

    [Test]
    procedure ResourceReadAsUtf8RoundTrips()
    var
        Res: Codeunit "Probe Resource";
    begin
        AssertTrue(Res.Utf8Encoding().Contains('café'),
            'reading the resource as UTF8 must recover the original text');
    end;

    // --- local assertion helpers (no test-library dependency) ------------------------
    local procedure AssertEqual(Expected: Text; Actual: Text; Because: Text)
    begin
        if Expected <> Actual then
            Error('expected ''%1'' but got ''%2'' — %3', Expected, Actual, Because);
    end;

    local procedure AssertTrue(Condition: Boolean; Because: Text)
    begin
        if not Condition then
            Error('expected TRUE — %1', Because);
    end;

    local procedure AssertFalse(Condition: Boolean; Because: Text)
    begin
        if Condition then
            Error('expected FALSE — %1', Because);
    end;

    local procedure AssertNotEqual(NotExpected: Text; Actual: Text; Because: Text)
    begin
        if NotExpected = Actual then
            Error('expected a value DIFFERENT from ''%1'' — %2', NotExpected, Because);
    end;
}
