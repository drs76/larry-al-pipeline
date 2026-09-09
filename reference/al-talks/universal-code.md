# universal-code

Distilled talk notes. Not hand-verified — see [`README.md`](README.md) for caveats, and check anything marked `[sic?]` before relying on it.

<!-- ingested: BC TechDays 2022 - Universal Code – Target must be cloud | 2026-07-27 -->
### Universal Code (TechDays 2022)

- Universal code = extensions with `target` set to `Cloud` in `app.json`. Runs both on-prem and SaaS; cloud-incompatible capability blocked by platform/AL.
- Enforcement extended to on-prem: latest/supported versions throw a platform error at install if non-universal code (code modifying base app, or `target` = `OnPrem`) is loaded. Such modules must be licensed (paid) to run on-prem.
- Check: open `app.json`, look at `target`. If already `Cloud`, done.

#### What breaks when flipping target to Cloud
- Local resource access blocked: local files, network, local hardware (printers, scales), local drive on server.
- `.NET`/`dotnet` add-ins not supported in SaaS — must be removed.
- On-prem-only base app APIs (locked for security) have no cloud equivalent; must refactor around them.
- Example gotcha: `System.IO` file listing via file-management codeunit (`Get Server Directory Files List` [sic?] — verify method name against System Application `File Management`) is server-local; errors under cloud target.

#### Replacement patterns
- **Files → Azure Blob Storage**: use the Blob Storage module in System Application (available since ~BC19) to read/write files. Works on-prem and SaaS; author reported cleaner code than local-file version.
  - No built-in generic setup table for blob connection endpoints (as of ~BC21); each extension configures its own account. Rationale given: different extensions may target different storage accounts.
- **Local hardware → Azure Service Bus Relay**: on-prem agent registers a listener endpoint on Service Bus Relay; BC (cloud) AL code calls in via `HttpClient` through the relay, reaching hardware behind a firewall. Local agent can run a plugin model (C# — files, printer, etc.) and reply back through relay. (Demo: "peer manager" on BCTech repo [sic?].)

#### Dual Service pattern (replace .NET add-in)
- Extract the .NET into an external service; call it two ways: **Azure Function** for SaaS, **local Windows service** for on-prem. Both reference the same small library.
- AL structure:
  - `interface` describing service operations (e.g. `AddRating`).
  - Single-instance codeunit exposing an `Instance()` procedure that returns the interface (AL can return complex/interface types).
  - Lazy init on first call, choosing implementation by SaaS vs on-prem.
  - Two implementations (one per environment) both calling a web-service endpoint; calling conventions differ slightly.
- Benefits: consuming code stays clean and environment-agnostic; interface makes mocking the service in tests easy (add a mock implementation).
- Reason on-prem service still wanted even when cloud possible: data-residency/privacy (data must not leave building) and poor/absent internet in some regions.

#### Windows service as .NET replacement (on-prem)
- Create via Visual Studio **Windows Service** project type; add existing .NET add-in code + plumbing from template.
- Base class exposes `OnStart`/`OnStop`. Recommend logging to Windows Event Log — service has no UI, so failures otherwise invisible.
- Uses `HttpListener` [sic?] in .NET; spin up N connections (demo used 100), listen, handle `ProcessRequestAsync` [sic?] — read payload over wire, do work, return payload. AL side calls it with an HTTP call.
- Wire interface example (reporting): send dataset + layout + desired output (Excel/PDF) + license info; get back rendered file.
- HTTPS on the listener was skipped (harder to set up), so service must run on the same machine as the BC Server (NST). HTTP only.
- Chose lightweight Windows service over IIS: lower footprint; some admins disallow IIS; service ships with Windows.
- Pros: no restart of NST to update the DLL; avoids assembly version conflicts (e.g. clashing OpenXML versions between your DLL and BC); can stay on .NET Framework (no forced port to .NET Core); a faulting DLL can't crash the NST/service host.
- Cons: works best stateless (state needs server-side work); needs a Windows installer (biggest effort); marshalling cost if many calls with little data. Note: author saw ~2× faster reports vs in-process despite going over the wire.

#### Why move off .NET regardless
- BC moving from .NET Framework to .NET Core (more efficient on server); can't run side-by-side, so migration forced even without universal code.
- Many .NET Framework libraries can't be ported: those built on Win32 / System.Drawing (GDI) don't work on .NET Core — affects PDF/graphics work.
- Modern DLL use needs assembly-load-conflict handling (versioned load), not just xcopy.
- Staying on BC14 to keep DLLs is discouraged — dead-ends the solution.

#### Base app note
- Microsoft base app is not fully universal-code clean; platform/base app can do things partner code can't (trust boundary). Copying base app code and setting target Cloud may fail to compile. Cleanup is a long-term, ongoing process.
