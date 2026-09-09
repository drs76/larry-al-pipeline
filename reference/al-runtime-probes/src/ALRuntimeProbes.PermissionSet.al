namespace SinclairSoftScotland.RuntimeProbes;

permissionset 50110 "AL Runtime Probes"
{
    Assignable = true;
    Caption = 'AL Runtime Probes';
    Permissions = tabledata "Probe Tbl" = RIMD,
                  table "Probe Tbl" = X,
                  codeunit "Probe Runtime Tests" = X,
                  codeunit "Probe Event Sink" = X,
                  codeunit "Probe Subscribers" = X,
                  codeunit "Probe Resource" = X,
                  codeunit "Probe Try" = X,
                  codeunit "Probe Impl A" = X,
                  codeunit "Probe Impl B" = X;
}
