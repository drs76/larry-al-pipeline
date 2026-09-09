# AL Talks — distilled conference/community notes

Third tier of the AL knowledge base. Distilled notes from BC/AL conference talks and community
sessions, grouped by topic.

## How this differs from the other two tiers

| Tier | What | Who reads it |
|---|---|---|
| [`AL-REFERENCE.md`](../AL-REFERENCE.md) / [`AL-KNOWLEDGE.md`](../AL-KNOWLEDGE.md) | curated, verified, durable | the coder reads these directly (see their read protocol) |
| **`al-talks/` (here)** | distilled talk notes — good signal, **not hand-verified** | `kb search` only; never auto-read into a build |
| [`transcripts/`](../transcripts/) | raw caption text | provenance and fallback |

The point of keeping this separate: the curated files are what the coder is told to read, so they
must stay small enough to fit a 32k context. This tier can grow without threatening that — it is
reached through search, not by reading whole files.

## Searching

```
kb search "<query>" --corpus al-talks
```

Why this tier exists at all: raw transcripts retrieve badly. A search against `transcripts` returns
mid-sentence spoken filler; the same query here returns the actual fact, with version gates. That
gap is the whole justification for spending model time distilling.

## Caveats

- **Not verified.** These are distilled from auto-generated captions, which garble identifiers.
  Anything marked `[sic?]` needs checking against Microsoft Learn or the compiler before you rely
  on it — see `AL-REFERENCE.md` → `10-quality-breaking.md` on verifying platform API signatures.
- **Point in time.** Each note carries its source talk and date. BC moves fast; a 2022 statement
  about a preview feature may be long superseded. Microsoft Learn is the live truth.
- **Pre-AL/NAV-era talks are excluded by design** (C/AL, RoleTailored Client, .NET interop). They
  are technically dense but would mislead anyone writing modern AL.

## Topics

Files are added by `pipeline/run-ingest.py`. Each stays under ~8k tokens; the ingest run warns and
names the split command when one grows past that.
