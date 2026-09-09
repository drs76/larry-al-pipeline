<!-- topic file split from AL-REFERENCE.md; edit here, not in the index -->
# Validate() triggers — behaviour, patterns, gotchas

Part of [`AL-REFERENCE.md`](../AL-REFERENCE.md) — see that index for the other topics.

---

## 10. Record Operations & Performance

### Validate() triggers — behaviour, patterns, gotchas (mibuso 2024-06)

- `Rec.Validate(Field)` does exactly two things: (1) checks the table relation (unless relation validation is disabled), (2) runs validate code in 5 places, in order: OnBeforeValidate event subscribers → table-extension OnBeforeValidate wrapper → the table's OnValidate trigger → table-extension OnAfterValidate wrapper → OnAfterValidate event subscribers.
- `Validate()` does NOT enforce field property constraints: `DecimalPlaces`, `MinValue`/`MaxValue`, `CharAllowed`, etc. Those are checked only on UI/page input, not when validating from code. Plain assignment (`:=`) skips both the relation check and all validate code.
- Pages always validate field input (users cannot bypass it in normal use), and pages run additional page-level OnValidate code on top of the table validate. So code that mimics user entry should call `Validate()` to reproduce the same populated/related data.
- Performance: an empty OnValidate is ~microseconds — not measurable per call; ~7 ms for 1000 empty validates. One real validate (e.g. sales line Quantity) ≈ 30 ms; 100k validates ≈ 7 s. Overhead of calling validate vs assignment is negligible for normal UI-scale use.

**Chained / nested validates**
- Validating one field often validates others (e.g. Unit Price → Unit Price Incl. VAT → Line Amount). Order matters; don't assume field-ID order is correct.
- For your own tables, expose a helper procedure that takes the few required inputs and validates dependent fields in the correct order — self-documenting and safe for other callers.

**Infinite-loop patterns (fields that validate each other)**
- Guard by pre-computing the expected result and only assigning/validating if the value actually differs, so the reciprocal validate becomes a no-op.
- Start/end-date style mutual checks: assign both fields with `:=` first, then call `Validate(Field)` with no new value to trigger the checks once each without re-changing values. Caveat: validate code that tests "did the value change?" will see no change (assignment already happened) — verify the validation logic supports this.
- Last-resort loop breaker: a boolean flag (record global var, or single-instance codeunit) to short-circuit re-entry; must carefully reset state.

**Don'ts inside validate code** (keep validate = validate + read/populate related data only)
- No write DB ops (Insert/Modify/Delete/ModifyAll) — puts the unaware caller into a write transaction; leftover records (esp. from temp-table scenarios) and "cannot run codeunit/page in write transaction" errors.
- No web-service calls that write to external systems; read-only lookups (e.g. VAT reg. no. validation) are acceptable.
- No `ChangeCompany` — only affects the record it's called on; other tables still resolve in the original company.
- No UI invocation / modal pages / RunModal — leads to COMMIT and nested-transaction problems.
- Avoid relying on `xRec` and `CurrentFieldNo` in validate code — they behave well when driven from a page but give weird results when validate is called from code.

**No-trigger operations (validate/triggers skipped)**
- `TransferFields`, `ModifyAll`, and `DataTransfer` do NOT run validate code. `ModifyAll(Field, Value, true)` still only runs OnModify (record-by-record under the hood), never OnValidate. `DataTransfer` runs no triggers at all and is restricted to upgrade code. Skipping validate here can break extensions that subscribe to those fields.

**Temporary tables**
- Dedicated temp table (`TableType = Temporary` [sic? verify property name/values on Learn]): validate code is written knowing it runs temp — safe to validate.
- "Hijacked" temp tables (a normal table used as `Rec.SetTemporary`/temp var, e.g. temp Sales Line): validate/trigger code was not written for temp scope and may create real records in other tables (e.g. `DimensionManagement.ValidateShortcutDimValues` [sic? verify exact name] creates Dimension Set Entry rows). Decide case-by-case; prefer a purpose-built temp table.
- Passing a field `by var` into a function means the function can't call the field's validate; assign to a local, then `Validate(Field, Local)` or validate the field afterward.

**Page OnValidate vs table OnValidate**
- Put on page OnValidate: CalcFields of flow fields for immediate UI feedback, style/visibility/UX logic, and validation of fields whose source expression is a variable (no table trigger available). Keep pure data validation + related-field population on the table so code callers get it too.
- Page `OnLookup` overrides table OnLookup — if both define it, the page's runs and the table's does not. To make a page lookup behave like real field entry (running validate), set the field value and return `exit(true)` from the page OnLookup; `exit(false)` discards the value.

**Also applies to OnInsert/OnModify** — same reasoning: don't skip. OnModify can still be reached via a subscriber even when `Modify(false)`; OnValidate cannot, which is why validate needs the most care. Mimicking user order (Init → set primary keys → validate keys → Insert → validate rest → Modify) reproduces page behaviour.

**Event-subscriber order** across multiple extensions validating the same base-app field is not controllable/guaranteed — write validate code so order doesn't matter.

- Refactor assignments to validates via David Feldhoff's *AL Code Actions* extension.
