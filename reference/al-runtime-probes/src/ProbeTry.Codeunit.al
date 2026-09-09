namespace SinclairSoftScotland.RuntimeProbes;

// [TryFunction] declares NO return type in AL, yet the CALLER receives a Boolean.
// That asymmetry is the gotcha; these two prove both halves at runtime.
codeunit 50114 "Probe Try"
{
    [TryFunction]
    procedure AlwaysFails()
    begin
        Error('deliberate failure inside a TryFunction');
    end;

    [TryFunction]
    procedure AlwaysSucceeds()
    begin
    end;
}
