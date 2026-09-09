namespace SinclairSoftScotland.RuntimeProbes;

// Guards the AL0282 rule at RUNTIME: a table auto-event subscriber binds its parameters
// BY NAME to the publisher's (Rec / xRec / RunTrigger). If a future runtime changed that
// contract, this subscriber would stop firing and the test would fail — where the
// compiler would still be perfectly happy.
codeunit 50112 "Probe Subscribers"
{
    [EventSubscriber(ObjectType::Table, Database::"Probe Tbl", 'OnBeforeInsertEvent', '', false, false)]
    local procedure OnBeforeInsertProbeTbl(var Rec: Record "Probe Tbl"; RunTrigger: Boolean)
    var
        Sink: Codeunit "Probe Event Sink";
    begin
        Sink.Record(Rec."Entry No.");
    end;
}
