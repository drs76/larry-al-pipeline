---
description: Rewrite anything an agent READS (handover prompts, CLAUDE.md/AGENTS.md, skills, pi prompt-templates) so it reads well to a model — concise, trigger-first, de-frontloaded
argument-hint: "<file or text to sharpen for an agent audience>"
---
You are editing text whose **reader is a model**, not a person — a Larry handover, a CLAUDE.md /
AGENTS.md, a skill or pi prompt-template, a reference topic file. The goal is not prettier prose; it
is that an agent given **only this text** does the right thing. Optimise for instruction-following
and retrieval, not readability. The target is:

$@

## The doctrine

1. **Trigger first.** The opening lines (a skill's `description`, a section's first sentence) are the
   router — write them as *when to use this* / *what this is*, not backstory. A skill `description`
   is the whole basis on which it gets invoked: make it a precise "use when…".
2. **De-frontload.** Anything always-loaded (CLAUDE.md, AGENTS.md, a monolithic reference) costs
   context on every turn. Move situational detail OUT into on-demand files the agent pulls only when
   relevant — the index-plus-topic split already used for AL knowledge (read the index + 1–2 topics,
   never the pile). Keep the always-on layer tiny; link the rest.
3. **Imperative and declarative.** One instruction per line. Active voice. Say exactly what to do and
   what happens. Cut hedging, politeness, and "you might want to" — spend no tokens on manners.
4. **✓/✗ beats prose.** For any rule with a common wrong form, show the right and wrong example. A
   model pattern-matches examples far more reliably than it parses a paragraph. (This is why the AL
   handover rules are written as ✓/✗ pairs.)
5. **State the contract, deterministically.** If a downstream tool parses the text, name the exact
   shape it needs and make it unmissable ("machine-readable manifest … one absolute path per line";
   end with `## STOP`). "Try to finish" is not a contract; "write N files, then STOP" is.
6. **Ubiquitous language, defined once.** Name each thing by the term the agent must recognise, define
   it one time, then reuse it verbatim. Don't rename the same concept across the doc.
7. **Verify, don't assume — and don't ask the agent to confirm what you couldn't.** Tell it where to
   check (symbols, `kb search`, the compiler); never tell it to "confirm" an identifier you didn't
   verify yourself, or it will invent a confirmation.
8. **Every line earns its place.** If a sentence won't change the agent's behaviour, delete it.
   Structure (headings, numbering) only when order or grouping is real information.

## Method

- **Read the target and name its job + reader** (which agent, loaded always or on-demand, parsed by a
  tool?). That decides how aggressive the de-frontloading is.
- **Cut, then sharpen:** remove filler and dead rules first; convert surviving rules to imperative +
  ✓/✗; pull always-loaded bulk into linked files and leave a one-line pointer.
- **Preserve the load-bearing exactly.** Machine-parsed blocks, required headings, exact identifiers,
  frontmatter keys — do not paraphrase these. Rewriting around them is fine; changing them breaks the
  parser or the router.
- **Test it:** would an agent with only this text do the right thing? Name what it would still get
  wrong, and fix that specifically. When editing a skill/prompt, re-read the `description` last — it
  is what decides invocation.

## Larry targets (what "good" looks like here)

| Target | Sharpen toward |
|---|---|
| `larry-handover.prompt.md` | the parsed contract (manifest / `## app.json` json block / permission set / `## STOP`); Strategy-A verbatim files; only the ✓/✗ rules this project needs; verified identifiers |
| CLAUDE.md / memory | de-frontload — `MEMORY.md` one line per fact, detail in topic files; always-on layer minimal |
| pi prompt-templates | trigger-first and **small-model-sized** — short, explicit, zero ambiguity for qwen (a big model tolerates vagueness; the local coder does not) |
| AL-REFERENCE / AL-KNOWLEDGE | index + topic files under the 8k-token guard; read index + 1–2 topics |
| a skill/prompt file | tiny always-loaded body + a linked reference for the heavy mechanics; `description` = a precise trigger |

## Deliver

Show the rewrite (or apply it if editing a file in place), and a one-line-per-change list of what you
cut/moved/sharpened and why. If you de-frontloaded, name the file the bulk moved to and leave the
pointer. Never touch machine-parsed blocks or exact identifiers except to correct a verified error.
