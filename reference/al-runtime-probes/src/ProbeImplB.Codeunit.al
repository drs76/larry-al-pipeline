namespace SinclairSoftScotland.RuntimeProbes;

codeunit 50101 "Probe Impl B" implements "Probe IFace"
{
    procedure Ping(): Text
    begin
        exit('B');
    end;
}
