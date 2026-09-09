# AL Coding Workflow — Larry, pi & Claude

*How we build Microsoft Dynamics 365 Business Central (AL) extensions with a local
GPU box (Larry), a local agent harness (pi), and Claude — local-first, compiler-verified,
and cost-controlled.*

> **For a colleague coming from Sage/other stacks:** the shape here is language-agnostic.
> Swap "AL compiler" for your build/lint tool and "Larry's models" for any local or
> hosted LLM, and the same pattern (local drafts → objective verifier → escalate to a
> strong model only when stuck) applies. See [Adapting this for Sage](#adapting-this-for-sage).

---

## TL;DR

A cheap local model on **Larry** does the bulk of the typing. The **AL compiler** — not
another LLM — decides whether the code is correct. A build loop feeds compiler errors
back to the model until it passes, and **only if it stalls** does it hand off to **Claude**
(which costs money). One CLI, `alw`, drives the whole thing.

---

## The three players

| Player | What it is | Role | Cost |
|---|---|---|---|
| **Larry** | Rocky Linux 10 tower, Radeon RX 7900 XTX, running **Ollama** | Serves local coding models over the LAN | Free (electricity) |
| **pi** | `pi-coding-agent` — a local CLI agent harness | Runs the tool loop, points at Larry; does triage + first drafts | Free (uses Larry) |
| **Claude** | Claude Code (Pro/Max subscription) | Planning (`/spec`), hard problems, and closing stalled builds | Paid per token when used as coder |

**Golden rule:** Larry/pi handle ~90% (drafts, simple asks, scaffolding). Claude is
reserved for planning and the last stubborn 10%. The **compiler is the referee** — there
is no LLM "reviewer" grading the code.

---

## 1 · Infrastructure & network

```mermaid
flowchart LR
    subgraph DEV["💻 Dev machines"]
        box["Dev box<br/><code>/mnt/rojaws/localDev</code>"]
        wsl["Laptop<br/>(WSL)"]
    end

    subgraph LARRY["🖥️ Larry — AI tower · Rocky Linux 10 · RX 7900 XTX"]
        direction TB
        nginx["nginx HTTPS proxy<br/><b>:11443</b> · HomeLab CA"]
        ollama["Ollama runtime<br/>:11434 · loopback only 🔒"]
        models["Local models<br/>al-coder-qwen36 · qwen2.5-coder:32b<br/>qwen3.6:27b · …"]
        nginx --> ollama --> models
    end

    cloud["☁️ Claude Code<br/>Pro / Max subscription"]

    box  -->|"pi provider · HTTPS"| nginx
    wsl  -->|"pi provider · HTTPS"| nginx
    box  -->|"claude CLI"| cloud
    wsl  -->|"claude CLI"| cloud

    classDef dev    fill:#e3f2fd,stroke:#1565c0,color:#0d47a1;
    classDef tower  fill:#e8f5e9,stroke:#2e7d32,color:#1b5e20;
    classDef ai     fill:#fff3e0,stroke:#ef6c00,color:#e65100;
    class box,wsl dev;
    class nginx,ollama,models tower;
    class cloud ai;
```

**Why the proxy?** Larry's raw Ollama port (`:11434`) is firewalled to loopback. LAN
clients reach it through an **nginx HTTPS proxy on `:11443`**, secured by a private
"HomeLab" CA that each dev machine trusts in its OS store (Node/pi is told to use it via
`NODE_OPTIONS=--use-system-ca`).

---

## 2 · Who does what (routing a request)

```mermaid
flowchart TD
    ask(["🧑‍💻 AL request"]) --> route{{"<b>alw route</b><br/>pi /al-route classifies"}}

    route -->|SIMPLE| draft["pi / Larry writes a draft<br/><i>free · local</i>"]
    draft --> verify["✅ verify with <code>al compile</code>"]

    route -->|COMPLEX| handover[["📄 handover file<br/>~/al-handovers/*.md"]]
    handover --> spec["<b>Claude /spec</b><br/>SPEC + Larry handover + manifest"]
    spec --> build["<b>alw build</b> ▶ build loop"]

    classDef q fill:#ede7f6,stroke:#5e35b1,color:#311b92;
    classDef local fill:#e8f5e9,stroke:#2e7d32,color:#1b5e20;
    classDef paid fill:#fff3e0,stroke:#ef6c00,color:#e65100;
    classDef io fill:#eceff1,stroke:#546e7a,color:#263238;
    class route q;
    class draft,verify local;
    class spec paid;
    class ask,handover,build io;
```

- **SIMPLE** (a record loop, JSON parse, one small object) → pi answers on the spot; the
  compiler is the only check needed.
- **COMPLEX** (new extension, multiple objects, HTTP/OAuth, schema changes, API-uncertainty)
  → pi writes an *intent handover*, Claude expands it into a full spec, then the build loop runs.

---

## 3 · The build loop — compiler as ground truth, with cost-safe escalation

`run-build.py` writes the AL, compiles it, and feeds errors back to the coder. It keeps the
**best** (lowest-error) version so a bad edit can't make things worse. Escalation to Claude
is **off by default** and only arms when you pass a round budget.

```mermaid
flowchart TD
    start(["📄 handover"]) --> write["coder writes AL<br/>(pi · or Claude)"]
    write --> norm["deterministic fixes<br/>using-placement · quoting · app.json"]
    norm --> compile{{"<b>al compile</b> + manifest check<br/>= GROUND TRUTH"}}
    compile --> pass{"pass?"}

    pass -->|✅ yes| done(["📦 deployable .app"])
    pass -->|❌ no| best["keep-best / no-regress<br/>snapshot lowest-error state"]
    best --> esc{"pi rounds ≥ N?<br/>ESCALATE_AFTER"}

    esc -->|no · free| pifix["🟢 Larry / pi fixes<br/>from compiler errors"]
    esc -->|yes · paid| clfix["🟠 Claude closes<br/>billed per-token"]
    pifix --> compile
    clfix --> compile

    classDef gt fill:#fce4ec,stroke:#c2185b,color:#880e4f;
    classDef local fill:#e8f5e9,stroke:#2e7d32,color:#1b5e20;
    classDef paid fill:#fff3e0,stroke:#ef6c00,color:#e65100;
    classDef io fill:#eceff1,stroke:#546e7a,color:#263238;
    class compile gt;
    class pifix local;
    class clfix paid;
    class start,done io;
```

**Escalation in one line:** `alw build myext` = free forever (Larry only);
`alw build myext 3` = Larry gets 3 fix rounds, then Claude finishes. You never spend Claude
quota by accident.

---

## 4 · End-to-end (a complex extension)

```mermaid
sequenceDiagram
    autonumber
    actor Dev
    participant alw as alw CLI
    participant pi as pi · Larry
    participant Claude
    participant al as al compiler

    Dev->>alw: alw route "sync invoices to Azure Blob"
    alw->>pi: /al-route (classify)
    pi-->>Dev: COMPLEX → handover written
    Dev->>Claude: /spec (expand handover)
    Claude-->>Dev: SPEC + handover + file manifest
    Dev->>alw: alw build myext 3

    rect rgb(232, 245, 233)
    note over alw,al: Free — Larry loop
    loop until pass or 3 rounds
        alw->>pi: write / fix AL
        alw->>al: compile (ground truth)
        al-->>alw: errors
    end
    end

    rect rgb(255, 243, 224)
    note over alw,Claude: Stalled → escalate (paid)
    alw->>Claude: close remaining errors
    alw->>al: compile
    al-->>alw: PASS ✅
    end

    alw-->>Dev: 📦 deployable .app
    Dev->>alw: alw promote myext
    note right of alw: → /mnt/rojaws/Code/AL for refinement
```

---

## 5 · Prototype lifecycle

```mermaid
flowchart LR
    A["🆕 <b>alw new</b><br/>scaffold prototype"] --> B["✍️ fill handover<br/>(or Claude /spec)"]
    B --> C["🔨 <b>alw build</b> [N]<br/>compile loop"]
    C --> D["🚚 <b>alw promote</b>"]
    D --> E["📁 /mnt/rojaws/Code/AL<br/>refine & maintain"]

    classDef step fill:#e0f7fa,stroke:#00838f,color:#006064;
    class A,B,C,D,E step;
```

New builds live in `…/projects/prototypes/` (with the tooling, out of the polished tree).
Once they compile, `alw promote` moves them to `/mnt/rojaws/Code/AL/` where finished
projects are refined and maintained.

---

## Key design principles

1. **Local-first.** The cheap local model does most of the work; the strong paid model is a
   scalpel, not a default.
2. **The compiler is the referee.** We removed the old "LLM reviewer" — an objective build
   (`al compile` + a file-manifest check) decides correctness. No model grades another model.
3. **Keep-best / no-regress.** Every round is scored; a regression is reverted so the loop
   can only improve.
4. **Cost is always deliberate.** Escalation to Claude is opt-in per build (`ESCALATE_AFTER=N`);
   the default spends nothing.
5. **Local models draft, they don't ship.** Small models happily hallucinate APIs, so their
   output is never trusted until the compiler (or Claude) has validated it.

---

## Tooling glossary

| Tool | What it does |
|---|---|
| **`alw`** | The one CLI: `route` (triage), `new` (scaffold), `build [N]` (compile loop + escalation), `promote` (ship to Code/AL). Named `alw`, not `al`, to avoid clashing with the dotnet AL compiler. |
| **`/al-route`** | A pi prompt-template that classifies an ask SIMPLE vs COMPLEX and either answers or writes a handover. |
| **`run-build.py`** | The build orchestrator `alw build` calls: write → compile → keep-best fix loop → escalation → `.app`. |
| **ALNvim** | Neovim plugin for AL (LSP, DAP, ghost/FIM completions off Larry, and `<leader>aw` → the `alw` menu). |

---

## Adapting this for Sage

The architecture is a **pattern**, not AL-specific:

```mermaid
flowchart LR
    subgraph P["The reusable pattern"]
        direction TB
        r["Route: cheap local model triages"] --> d["Draft: local model writes"]
        d --> v{{"Verify: your OBJECTIVE tool<br/>(compiler / linter / tests)"}}
        v -->|fail · budget left| d
        v -->|fail · budget spent| s["Escalate: strong paid model closes"]
        s --> v
        v -->|pass| out["Ship"]
    end
    classDef v fill:#fce4ec,stroke:#c2185b,color:#880e4f;
    class v v;
```

To port it to Sage development, replace three things:
- **Verifier:** swap `al compile` for the Sage build/lint/test that objectively says pass/fail.
- **Local model:** point the agent at whatever local or hosted model suits Sage code.
- **Handover/spec conventions:** keep a machine-readable file manifest so the loop knows what
  "done" looks like.

Everything else — local-first drafting, compiler-as-referee, keep-best loop, opt-in
escalation — carries over unchanged.

---

*Internal doc. Larry is on the home LAN (`larry.home.arpa`); off-LAN access needs the VPN.*
