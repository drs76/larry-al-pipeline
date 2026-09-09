<!-- topic file split from AL-REFERENCE.md; edit here, not in the index -->
# search — relational, full-text & semantic (AL)

Part of [`AL-REFERENCE.md`](../AL-REFERENCE.md) — see that index for the other topics.

---

<!-- ingested: Microsoft presents: Semantic Search from AL | 2026-08-19 -->
### Three search modes in BC (relational / full-text / semantic)

- Three ways to locate a record, chosen by how much the caller knows:
  - **Relational filtering** — `SetRange`/`SetFilter`. Exact values and ranges, backed by table keys / SQL indexes. Deterministic, fastest.
  - **Full-text ("modern") filtering** — word and word-prefix matching, backed by a SQL full-text index. Shipped ~2 versions before v29.
  - **Semantic search** — match by meaning/intent via embedding vectors. New, preview.
- They are complementary, not competing. Normal layering: relational and/or full-text filter first to cut the candidate set, then semantic search to *rank* what remains.

#### Relational — limits
- Substring filters (`*text*`, CONTAINS) cannot use an index → table scan. Fast only for exact/prefix/range predicates.
- Case- and accent-sensitivity follows the database collation, which AL cannot control. Default collation is case sensitive, so `chair` vs `Chair` matters.

#### Full-text filtering
- Enable per field with the table field property `OptimizeForTextSearch = true` (verify exact spelling against Microsoft Learn) — only possible if you own the table.
- **One index per table.** There is exactly one full-text index, which is why it is a boolean property rather than a normal (multi-instance) key/index definition.
- Intended for descriptive/long-text fields (Description, Address), not identifiers.
- Always case-insensitive and accent-insensitive, unlike relational filtering.
- Runtime check: a field method along the lines of `IsOptimizedForTextSearch` / `OptimizedForTextSearch` [sic?] lets AL ask whether a field is in the index — verify the exact member name against the compiler. If a field is *not* in the index, the platform silently falls back to wildcard CONTAINS (slower), so behaviour degrades rather than errors.
- Filter syntax:
  - `*swivel*` — classic substring wildcard (no index).
  - `&&swivel` — whole-word match (double-ampersand operator). Matches the word `swivel` only.
  - `&&swiv` — no match; `swiv` is not a whole word in the text.
  - `&&swiv*` — prefix match on words; finds `swivel`.
  - `*hair*` — substring, so it also matches `chair`; `&&hair` does not.
  - Rule of thumb: `&&` operates on words, `*` operates on characters.
- List-page search used to always do CONTAINS across all fields (guaranteed table scan); with full-text-optimized fields it becomes an indexed word search.
- On-premises: the SQL Server full-text search feature (and its word-breaker/filter components) must be installed and enabled.
- **Text search language** (new in v28): stemming/word-breaking is language dependent, so index quality drops badly when the data language differs from the index language (observed with agents in multi-language markets, e.g. German/French data). Setter is roughly `SetCurrentOptimizedTextSearchLanguage` [sic?] — verify exact name; reading the current value is allowed from AL anywhere, but *setting* it is on-prem only (or Microsoft-internal). Changing it forces a full rebuild of all full-text indexes, so it is not a runtime knob.

#### Semantic search from AL (preview, v29 early access)
- Mechanism: text → embedding vector (OpenAI `text-embedding-3-small`) → similarity ranking. Model vectors are unit magnitude, so cosine similarity reduces to a dot product.
- Vectors are computed and stored **in the tenant database**. This is not Azure Cognitive Search / an external vector store.
- Two distinct things, do not confuse:
  - **Platform metadata search** — already shipping, used by advanced Tell Me, MCP dynamic tool mode, Copilot chat, analysis-view field suggestions, sales line suggestions, number series Copilot. Vectors built proactively in the background.
  - **Ad-hoc semantic search from AL** — the new API. Vectors are generated on demand and cached; the first search over a data set is slow, later searches over the same data are fast.
- Embeddings capability itself shipped in v25.

##### API shape
- New system codeunit, name approximately `Semantic Search`, ID in the 2-billion system range (transcript garbles the exact ID — verify against the symbols). Microsoft ships these as system codeunits partly so they can be obsoleted if the design changes.
- Usage pattern:
  1. Build a filtered `Record`, take a `RecordRef` on it.
  2. `SetSearchTarget(RecRef)` — defines the search space.
  3. Set the number of results wanted (top N).
  4. `FindSimilarByField(SearchText, Fields, SimilarityResult)` [sic?] — verify signature and member names against the compiler.
- Fields argument may be a single field or an array; an array is treated as the concatenation of those fields for embedding purposes.
- Result is a similarity-result record containing a row number, the **SystemId**, and a similarity score. Deliberately type-agnostic so one result structure serves any table.
- To turn results into something displayable: iterate the result set, `GetBySystemId` on the target record, and copy into a temporary table; bind the page to that temp table.

##### Semantics and gotchas
- **It is ranking, not filtering.** You never get "similar / not similar" — you get the top N by similarity. Conceptually closer to `SetCurrentKey`/ordering than to `SetFilter`. It only behaves like a filter in the trivial sense that you truncate at top N.
- **Similarity scores are relative, not absolute.** A top score of 0.05 can still be the best answer in that set. Do not hard-code an absolute threshold; if you must cut, cut relative to the top score (e.g. keep ≥80% of the best score).
- **1000-row hard limit** on the ad-hoc data search. Exceeding it **fails** — it does not silently take the first 1000. The implementation does a `Count` first, so AL can pre-check the filtered set size and handle it. The limit exists because up to 1000 missing vectors can be embedded in a single batch, bounding first-search latency.
- Works best with rich text; short low-context fields give poor discrimination.
- Cross-language search works reasonably — embedding models map text across languages into the same space.
- Setup/singleton tables are a pointless target; just read the record.

##### Metadata search from AL
- The same API works over virtual metadata providers (fields, tables, …) — e.g. `SetSearchTarget` on a fields virtual table filtered to one table, then `FindSimilarByField` on the Caption (and typically Tooltip). This is essentially how analysis-view field suggestion works.
- **v29 change:** metadata virtual tables now expose a **SystemId** even though they are not stored in the database. It is a pseudo-GUID derived from the identifying keys (e.g. table ID + field ID for fields) and is decoded back on `GetBySystemId`. Added to the metadata virtual providers only — not to all virtual tables, since each needs a custom mapping.

##### Cost, determinism, testing
- Cheap relative to an LLM: no token burn for already-embedded rows, one embedding for the query (also cached). Microsoft absorbs the ad-hoc embedding cost for now; sandboxes are free.
- Not fully deterministic across time: same input gives the same vector today, but the underlying model can be swapped or silently updated behind the same endpoint, shifting scores and possibly rank order.
- Consequence for tests: treat as **evals with an accuracy target**, not pass/fail assertions. Far more stable than calling an LLM, but expect drift.
- v28 shipped it scoped on-prem-only; that was a preview restriction, not the intent — the feature ultimately requires cloud, since vector generation is a cloud service.

##### Roadmap (unshipped, no dates)
- Declared/persistent semantic indexes backed by the Azure SQL vector index (itself in SQL preview), which would lift the 1000-row cap toward millions.
- Multi-table "document" embeddings (e.g. Item + Item Variant joined via a query plus a text template) rather than fields on one table.
- Shipping prebuilt metadata vectors inside an app package so Tell Me does not re-embed on every app update.
- Generic semantic search surfaced on list pages and lookups (blocked partly on UX: search boxes are filters, and this is an ordering).
