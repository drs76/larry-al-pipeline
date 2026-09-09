---
bc-version: [all]
domain: performance
keywords: [dictionary, containskey, list, contains, lookup, membership, hash, large-recordset]
technologies: [al]
countries: [w1]
application-area: [all]
---

# Membership checks over large sets: Dictionary.ContainsKey, not List.Contains

## Description

`List.Contains` is a linear scan — O(n) per call, so checking membership for every record
in a loop is O(n×m) and degrades badly on large record sets. `Dictionary.ContainsKey` is a
hash lookup — effectively O(1) per call. When collecting keys to test membership against
(seen-before checks, exclusion sets, join-style matching), build a
`Dictionary of [KeyType, Boolean]` and use `ContainsKey`. Use a List only when order or
duplicates matter and the set stays small.

## Best Practice

```al
var
    SeenCustomers: Dictionary of [Code[20], Boolean];
begin
    if CustomerLedger.FindSet() then
        repeat
            if not SeenCustomers.ContainsKey(CustomerLedger."Customer No.") then begin
                SeenCustomers.Add(CustomerLedger."Customer No.", true);
                ProcessFirstEntryFor(CustomerLedger);
            end;
        until CustomerLedger.Next() = 0;
end;
```

## Anti Pattern

```al
var
    SeenCustomers: List of [Code[20]];
begin
    // O(n) scan per record -> O(n*m) over the loop; crawls on large ledgers
    if CustomerLedger.FindSet() then
        repeat
            if not SeenCustomers.Contains(CustomerLedger."Customer No.") then begin
                SeenCustomers.Add(CustomerLedger."Customer No.");
                ProcessFirstEntryFor(CustomerLedger);
            end;
        until CustomerLedger.Next() = 0;
end;
```
