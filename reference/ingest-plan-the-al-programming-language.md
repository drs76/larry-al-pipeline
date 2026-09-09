# Ingest plan — Learn TOC section: The AL programming language

Source TOC: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/toc.json

45 article(s); every row defaults to **KEEP**. 45 KEEP / 0 SKIP.

Prune before running — each KEEP row is a fetch + a Claude distil call, and every merge lands in a topic file that must stay readable in one go (~8k tokens). Flip a verdict, change a target, or delete a row.

Then: `python3 pipeline/run-ingest.py run --plan /mnt/rojaws/localDev/setup/reference/ingest-plan-the-al-programming-language.md`

| Verdict | ID | Title | Len | Target | Reason |
|---|---|---|---|---|---|
| KEEP | https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-reference-overview | Overview | article | AL-REFERENCE.md | Learn: The AL programming language |
| KEEP | https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-programming-in-al | Programming in AL | article | AL-REFERENCE.md | Learn: The AL programming language |
| KEEP | https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-dev-faq | FAQ for developing in AL | article | AL-REFERENCE.md | Learn: The AL programming language |
| KEEP | https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-al-operators | · AL operators | article | AL-REFERENCE.md | Learn: The AL programming language |
| KEEP | https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-al-arithmetic-operators | · Arithmetic operators | article | AL-REFERENCE.md | Learn: The AL programming language |
| KEEP | https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-al-boolean-operators | · Boolean operators | article | AL-REFERENCE.md | Learn: The AL programming language |
| KEEP | https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-al-relational-operators | · Relational operators | article | AL-REFERENCE.md | Learn: The AL programming language |
| KEEP | https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-al-variables | · AL variables | article | AL-REFERENCE.md | Learn: The AL programming language |
| KEEP | https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-system-defined-variables | · System-defined variables | article | AL-REFERENCE.md | Learn: The AL programming language |
| KEEP | https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-protected-variables | · Protected variables | article | AL-REFERENCE.md | Learn: The AL programming language |
| KEEP | https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-al-type-conversion-expressions | · AL type conversion in expressions | article | AL-REFERENCE.md | Learn: The AL programming language |
| KEEP | https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-al-simple-statements | AL simple statements | article | AL-REFERENCE.md | Learn: The AL programming language |
| KEEP | https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-al-control-statements | AL control statements | article | AL-REFERENCE.md | Learn: The AL programming language |
| KEEP | https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-al-complextypes | AL complex types | article | AL-REFERENCE.md | Learn: The AL programming language |
| KEEP | https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-al-methods | AL methods | article | AL-REFERENCE.md | Learn: The AL programming language |
| KEEP | https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-al-error-handling | AL error handling | article | AL-REFERENCE.md | Learn: The AL programming language |
| KEEP | https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-xml-comments | AL code comments | article | AL-REFERENCE.md | Learn: The AL programming language |
| KEEP | https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-using-access-modifiers | Using access modifiers in AL | article | AL-REFERENCE.md | Learn: The AL programming language |
| KEEP | https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-using-labels | Working with labels | article | AL-REFERENCE.md | Learn: The AL programming language |
| KEEP | https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-table-object | · Table object | article | AL-REFERENCE.md | Learn: The AL programming language |
| KEEP | https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-table-ext-object | · Table extension object | article | AL-REFERENCE.md | Learn: The AL programming language |
| KEEP | https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-table-keys | · Table keys | article | AL-REFERENCE.md | Learn: The AL programming language |
| KEEP | https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-extensible-enums | · Enums | article | AL-REFERENCE.md | Learn: The AL programming language |
| KEEP | https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-page-object | · Page object | article | AL-REFERENCE.md | Learn: The AL programming language |
| KEEP | https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-page-ext-object | · Page extension object | article | AL-REFERENCE.md | Learn: The AL programming language |
| KEEP | https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-page-customization-object | · Page customization object | article | AL-REFERENCE.md | Learn: The AL programming language |
| KEEP | https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-report-object | · Report object | article | AL-REFERENCE.md | Learn: The AL programming language |
| KEEP | https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-profile-object | · Profile object | article | AL-REFERENCE.md | Learn: The AL programming language |
| KEEP | https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-codeunit-object | · Codeunit object | article | AL-REFERENCE.md | Learn: The AL programming language |
| KEEP | https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-query-object | · Query object | article | AL-REFERENCE.md | Learn: The AL programming language |
| KEEP | https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-xmlport-object | · XMLPort object | article | AL-REFERENCE.md | Learn: The AL programming language |
| KEEP | https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-control-addin-object | · Control add-in object | article | AL-REFERENCE.md | Learn: The AL programming language |
| KEEP | https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-entitlement-object | · Entitlement object | article | AL-REFERENCE.md | Learn: The AL programming language |
| KEEP | https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-permissionset-object | · Permissionset object | article | AL-REFERENCE.md | Learn: The AL programming language |
| KEEP | https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-permissionset-ext-object | · Permissionset extension object | article | AL-REFERENCE.md | Learn: The AL programming language |
| KEEP | https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/directives/devenv-directives-in-al | · Preprocessor directives | article | AL-REFERENCE.md | Learn: The AL programming language |
| KEEP | https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/directives/devenv-directive-region | · Region directive | article | AL-REFERENCE.md | Learn: The AL programming language |
| KEEP | https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/directives/devenv-directive-pragma | · Pragma directive | article | AL-REFERENCE.md | Learn: The AL programming language |
| KEEP | https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-using-code-analysis-tool | · Using the code analysis tool | article | AL-REFERENCE.md | Learn: The AL programming language |
| KEEP | https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-rule-set-syntax-for-code-analysis-tools | · Ruleset for the code analysis tool | article | AL-REFERENCE.md | Learn: The AL programming language |
| KEEP | https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-using-code-analysis-tool-with-rule-set | · Using the code analysis tools with the ruleset | article | AL-REFERENCE.md | Learn: The AL programming language |
| KEEP | https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/analyzers/appsourcecop | · AppSourceCop analyzer rules | article | AL-REFERENCE.md | Learn: The AL programming language |
| KEEP | https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/analyzers/codecop | · CodeCop analyzer rules | article | AL-REFERENCE.md | Learn: The AL programming language |
| KEEP | https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/analyzers/pertenantextensioncop | · PerTenantExtensionCop analyzer rules | article | AL-REFERENCE.md | Learn: The AL programming language |
| KEEP | https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/analyzers/uicop | · UICop analyzer rules | article | AL-REFERENCE.md | Learn: The AL programming language |
