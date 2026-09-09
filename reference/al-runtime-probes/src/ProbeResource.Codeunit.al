namespace SinclairSoftScotland.RuntimeProbes;

// Wraps NavApp.GetResourceAsText so the encoding claim can be asserted from a test.
codeunit 50113 "Probe Resource"
{
    procedure DefaultEncoding(): Text
    begin
        exit(NavApp.GetResourceAsText('encoding.txt'));
    end;

    procedure Utf8Encoding(): Text
    begin
        exit(NavApp.GetResourceAsText('encoding.txt', TextEncoding::UTF8));
    end;
}
