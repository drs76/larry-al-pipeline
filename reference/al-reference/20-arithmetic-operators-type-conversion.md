<!-- topic file split from AL-REFERENCE.md; edit here, not in the index -->
# arithmetic operators & type conversion

Part of [`AL-REFERENCE.md`](../AL-REFERENCE.md) — see that index for the other topics.

---

<!-- ingested: · Arithmetic operators | 2026-08-16 -->
### Arithmetic operators & type conversion (AL)

**Unary (prefix)**
- Syntax: `PrefixOperator Expression`.
- `+` and `-` defined for Option, Integer, Decimal only.
- Option and Integer operands yield Integer; Decimal yields Decimal.

**Binary (infix)**
- Syntax: `LeftExpression InfixOperator RightExpression`.
- Operators: `+`, `-`, `*`, `/`, `DIV`, `MOD`.
- Numeric types accepted by all six: Byte, Char, Option, Integer, Decimal.
- Boolean accepted by none — no arithmetic on Boolean.
- Date and Time accept `+` and `-` only. Not `*`, `/`, `DIV`, `MOD`.
- Text and Code accept `+` only (concatenation). Code also accepts `-`? No — `-` not valid for Text/Code.

**Result types for `+`**
- Integer-family (Byte/Char/Option/Integer) combos → Integer; any Decimal operand → Decimal.
- `Date + Integer` → Date. `Time + Integer` → Time (integer is milliseconds).
- `Date + Decimal` / `Time + Decimal` → Date/Time, but undefined if Decimal has fractional part.
- `Text + Text` → Text; `Text + Code` → Text; `Code + Text` → Text; `Code + Code` → Code. Mixing Code with Text always demotes result to Text.

**Result types for `-`**
- `Time - Time` → Integer (difference in milliseconds).
- Date/Time arithmetic undefined for the zero values `0D` and `0T`; runtime error if operand undefined.

**Gotchas**
- Overflow possible on any numeric/date/time conversion result — compiler does implicit widening but no overflow guard.
- Time unit is milliseconds throughout; do not assume seconds.
- Implicit conversion is compiler-driven: an Integer operand silently promotes to Decimal when the other side is Decimal, changing rounding behaviour of downstream code.

<!-- ingested: · Boolean operators | 2026-08-16 -->
### Boolean (logical) operators

- Operands must evaluate to Boolean; result always Boolean.
- `not` — unary prefix: `not bool`.
- `and`, `or`, `xor` — binary infix: `bool1 and bool2`, `bool1 or bool2`, `bool1 xor bool2`.
- `xor` = exclusive or; true when operands differ.
- Related operator families: arithmetic, relational.

<!-- ingested: · Relational operators | 2026-08-16 -->
### Relational operators (Learn reference)

- Six comparison operators plus `in`. All return Boolean:
  - `>` greater than, `<` less than, `>=` greater-or-equal, `<=` less-or-equal, `<>` not equal, `=` equal.
  - `Expr in [ValueSet]` — membership test, also Boolean. Set literal uses square brackets.
- All are binary infix — left arg, operator, right arg.
- String comparison is case-sensitive. Ordering comes from BC's own character comparison table, not raw ASCII codepoints — do not assume ASCII/ordinal sort results for non-alphanumeric or accented chars.
- Valid operand type combinations (rows = left, cols = right; all valid cells yield Boolean):
  - Boolean — comparable only with Boolean.
  - Char, Option, Integer, Decimal — mutually comparable (any of the four against any of the four).
  - Date — only with Date.
  - Time — only with Time.
  - Text and Code — comparable with each other and themselves (Text↔Text, Text↔Code, Code↔Code).
  - Everything else is a compile error (no Boolean↔Integer, no Date↔Text, no Date↔Time, etc.).
- Gotcha: Option comparing against Integer is legal, so an unguarded `Status > 2` compiles — prefer comparing against the named option/enum value for readability.
- Gotcha: Date and Time are not cross-comparable; use DateTime for combined ordering.

<!-- ingested: · AL type conversion in expressions | 2026-08-16 -->
### Type conversion in expressions

- AL compiler converts operands implicitly when an expression mixes data types. Rule: promote to the *more general* type, never demote.
- Generality ranking (numeric): `Decimal` > `Integer` > `Char`. String group: `Text` > `Code`.
- Numeric example: `Integer + Decimal` — the Integer operand is promoted, expression evaluates as `Decimal + Decimal`, result type `Decimal`.
- String example: `Text + Code` (concatenation) — the `Code` operand is promoted to `Text`, result type `Text`.
- `Char` arithmetic: adding a `Char` to an `Integer` promotes the `Char` to `Integer` first; the `+` operator then yields `Integer`.
- Conversion can happen twice in one statement: once inside the expression (operand promotion) and again on assignment, when the result type differs from the target variable's type. Example: `charVar + integerVar` yields `Integer`; assigning to a `Decimal` variable converts `Integer` → `Decimal`.
- Conversion is possible even when both operands already share a type — same-type operands are not a guarantee that no conversion occurs (e.g. the assignment step still applies).
- Gotcha: `Code` operands lose their Code semantics (uppercasing/trim behaviour of the Code type) once promoted to `Text` in a concatenation — the result is a plain `Text` value.
- Practical consequence: integer division/addition results assigned to `Decimal` are exact only insofar as the *expression* was evaluated in the promoted type — promotion happens per operator, not retroactively for the whole statement, so `Integer DIV`-style truncation inside the expression is not undone by a `Decimal` target.
