<!-- topic file split from AL-REFERENCE.md; edit here, not in the index -->
# methods, parameters & return values

Part of [`AL-REFERENCE.md`](../AL-REFERENCE.md) — see that index for the other topics.

---

<!-- ingested: AL methods | 2026-08-16 -->
### AL methods — declaration, scope, parameters, return values

**Declaration syntax**

```
[Attribute(args)]
local procedure <Name>(<parameter list>) <ReturnName> : <DataType>[<length>]
```

- `procedure` and `method` are the same concept; Learn calls them methods.
- Two families: built-in (platform) methods and user-defined methods.
- VS Code snippet `tprocedure` scaffolds a procedure.

**Attributes**

- Optional modifiers placed on the line(s) before the declaration; may take arguments.
- Example: the `Integration` attribute turns the procedure into an event publisher.
- Scope-related behaviour is controlled by the `Scope` attribute (verify exact argument values against Microsoft Learn).

**Local vs global**

- `local procedure X()` — callable only from within the declaring object.
- `procedure X()` — global; callable from other objects too.
- Global is the default: omitting `local` publishes the procedure.

**Parameters**

- Declared in parentheses, separated by **semicolons** in the declaration; separated by **commas** at the call site. Easy trap.
- Each parameter needs a data type; `Record` (and other complex types) also need a subtype.
- Pass by value is the default — the method gets a copy, caller's variable unaffected.
- `var` on a parameter passes by reference — the method can mutate the caller's variable.

```al
procedure MyMethod(MyCustomer: Record Customer; var MyDimension: List of [Boolean])
```

- Optional parameters (in built-in methods) may only be omitted from the right-hand end; you cannot skip a middle parameter and supply a later one.
- Example of variable arity: `DMY2Date(5, 11, 1992)` — day is required, month and year optional and defaulted from the system date.

**Return values**

- Optional. Defined by an optional name, a data type, and an optional length for length-bearing types.
- Named return value acts as a variable inside the body; assign to it to return.

```al
procedure MyMethod() ReturnValue: Text[50]
var
    Result: Text[50];
begin
    // compute Result
    ReturnValue := Result;
end;
```

**Calling**

- Call as an expression when a value is needed: `TotalCost := Quantity * CalculatePrice;`.
- Call as a statement when the return is ignored: `if Quantity > 5 then MyRunMethod;` (parentheses optional for no-arg calls).
- Return value can be assigned (`ReturnVal := MyMethod(Param1);`) or used directly in a condition (`if MyMethod(Param1) then ...`).
- Execution suspends at the call site and resumes there after the method body finishes.
