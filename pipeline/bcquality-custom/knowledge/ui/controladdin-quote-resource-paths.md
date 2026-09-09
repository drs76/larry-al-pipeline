---
bc-version: [all]
domain: ui
keywords: [controladdin, scripts, stylesheets, startupscript, resource-path, AL0219]
technologies: [al]
countries: [w1]
application-area: [all]
---

# Quote every resource path in a controladdin

## Description

In a `controladdin`, all file paths in `Scripts`, `StartupScript`, and `StyleSheets`
are string literals and MUST be single-quoted. An unquoted path raises `AL0219`
(string literal expected). LLM coders routinely drop the quotes.

## Best Practice

```al
Scripts = 'src/controladdin/map.js';
StyleSheets = 'src/controladdin/map.css';
```

## Anti Pattern

```al
Scripts = src/controladdin/map.js;   // ✗ AL0219
```
