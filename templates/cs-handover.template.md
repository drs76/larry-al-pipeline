# Larry Handover — [PROJECT NAME]

<!--
TEMPLATE INSTRUCTIONS (delete this block before use):
1. Replace [PROJECT NAME] with the project name.
2. Fill "What you are building" — the functions/endpoints and what they do.
3. List every file under "Project & layout" and give each file's full content in the
   checklist (Strategy A) — verbatim is best; Larry then just transcribes.
4. Keep only the ✓/✗ correctness rules relevant to this project.
5. Fill the "machine-readable manifest" block to gate the write phase (recommended),
   or delete it to fall back to ">=1 .cs file".
-->

## What you are building

<!-- One paragraph: the trigger(s) (HTTP / Timer / Queue / Blob / Service Bus), what each
function does, and any bindings. -->
[Describe the Azure Functions app: triggers, what each function does, inputs/outputs.]

## Project & layout

- **Project:** `[PROJECT NAME]` — an **Azure Functions isolated worker** app on **.NET 10**.
- **The scaffold already exists — do NOT recreate or edit these:** `[PROJECT NAME].csproj`
  (packages + TFM), `Program.cs` (`HostBuilder().ConfigureFunctionsWebApplication()`),
  `host.json`, `local.settings.json`, `.gitignore`.
- **Files to write** (functions + helpers):
  - `Functions/<Name>Function.cs` — one class per trigger
  - `Models/<Name>.cs` — DTOs (if any)

Use the **write**/**edit** tools with paths relative to the project root. Do NOT run
`dotnet`/`func`/`dotnet restore` yourself — the pipeline runs the toolchain (`dotnet format`,
`dotnet build`, `dotnet format --verify-no-changes`, `dotnet test`) after you write. The
required packages are already referenced; just `using` them.

## File checklist (preferred — verbatim)

Number each file 1–N. Give the complete content exactly as it should be written. End with:

```
## STOP
All N files written. Do not create additional files. Do not run the dotnet toolchain.
```

## Azure Functions (isolated) — ✓ do / ✗ don't

This app uses the **isolated worker** model with **ASP.NET Core integration**
(`ConfigureFunctionsWebApplication` + `Microsoft.Azure.Functions.Worker.Extensions.Http.AspNetCore`).

**HTTP trigger — ✓ isolated + ASP.NET Core shape:**
```csharp
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Azure.Functions.Worker;
using Microsoft.Extensions.Logging;

public class HelloFunction
{
    private readonly ILogger<HelloFunction> _logger;
    public HelloFunction(ILogger<HelloFunction> logger) => _logger = logger;

    [Function("Hello")]
    public IActionResult Run(
        [HttpTrigger(AuthorizationLevel.Function, "get", "post")] HttpRequest req)
    {
        _logger.LogInformation("Hello invoked");
        return new OkObjectResult("hello");
    }
}
```
- ✓ `[Function("Name")]` on the method (isolated). ✗ NOT `[FunctionName(...)]` (that is the
  legacy in-process model — wrong for this project).
- ✓ ASP.NET Core types: `HttpRequest` in, `IActionResult`/`OkObjectResult`/`BadRequestObjectResult`
  out. ✗ don't mix in `HttpRequestData`/`HttpResponseData` (the non-ASP.NET isolated shape) —
  pick the ASP.NET Core types since the scaffold enables them.
- ✓ inject `ILogger<T>` via the constructor. ✗ don't call `FunctionContext.GetLogger` unless needed.
- ✓ every `.cs` file has correct `using` directives; **unused usings** trip the format gate
  (dotnet format removes them, but write them clean).

**C# correctness:**
- Nullable is enabled — handle possible nulls (`?`, null checks) or you get warnings→errors.
- `async` HTTP work returns `Task<IActionResult>`; `await` the async calls.
- Deserialize JSON with `System.Text.Json` (`JsonSerializer.Deserialize<T>`), not Newtonsoft
  unless the handover adds that package.
- Do NOT add PackageReferences by editing the .csproj unless the handover says to — the
  scaffold's package set is fixed and known-good.

## Referee / definition of done

The pipeline passes only when: `dotnet build` compiles, `dotnet format --verify-no-changes`
is clean (formatting is a **hard gate** — correct whitespace, using order, braces), and
(if a test project exists) `dotnet test` passes.

## Expected files — machine-readable manifest (optional)

<!-- Absolute paths, one per line. Delete this heading+block to fall back to ">=1 .cs file". -->

```
~/cs/projects/prototypes/[PROJECT NAME]/Functions/HelloFunction.cs
```

## When done

State: all files written, STOP, do not run the dotnet toolchain — the pipeline builds,
format-checks and tests. Larry only writes and fixes.
