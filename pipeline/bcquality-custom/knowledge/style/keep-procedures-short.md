---
bc-version: [all]
domain: style
keywords: [procedure, length, short, single-responsibility, refactor, helper, readability]
technologies: [al]
countries: [w1]
application-area: [all]
---

# Keep procedures to ~25–30 lines — extract helpers instead of growing bodies

## Description

Aim for procedure bodies of roughly 25–30 lines of code where possible. A procedure that
grows past that is usually doing more than one job — validation + fetch + transform +
persist in one body. Long bodies are where LLM coders introduce brace/begin-end cascades
and where review misses defects. Split by responsibility into well-named `local` helpers;
the top procedure reads as the sequence of steps. Soft guidance, not a hard limit — do not
contort genuinely linear logic (e.g. a long `case` mapping) just to hit a number.

## Best Practice

```al
procedure MigrateAttachments()
begin
    if not GetEnabledSetup(Setup) then
        exit;
    ProcessPendingAttachments(Setup);
    ReportMigrationResult();
end;

local procedure ProcessPendingAttachments(Setup: Record "PTE My Setup")
begin
    // one job: iterate + upload, ~20 lines
end;
```

## Anti Pattern

```al
procedure MigrateAttachments()
begin
    // 120 lines: setup checks, filtering, stream handling, upload, error
    // handling, counters and UI messaging all inlined in one body
end;
```
