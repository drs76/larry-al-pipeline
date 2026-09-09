namespace SinclairSoftScotland.RuntimeProbes;

// SingleInstance flag store: an event subscriber cannot return anything, so it records
// that it fired here and the test reads it back.
codeunit 50111 "Probe Event Sink"
{
    SingleInstance = true;

    var
        SubscriberFired: Boolean;
        SeenEntryNo: Integer;

    procedure Reset()
    begin
        SubscriberFired := false;
        SeenEntryNo := 0;
    end;

    procedure Record(EntryNo: Integer)
    begin
        SubscriberFired := true;
        SeenEntryNo := EntryNo;
    end;

    procedure Fired(): Boolean
    begin
        exit(SubscriberFired);
    end;

    procedure EntryNo(): Integer
    begin
        exit(SeenEntryNo);
    end;
}
