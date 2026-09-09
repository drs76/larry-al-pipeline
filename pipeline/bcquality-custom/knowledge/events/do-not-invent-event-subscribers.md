---
bc-version: [all]
domain: events
keywords: [eventsubscriber, publisher, signature, AL0280, AL0282, integration-event]
technologies: [al]
countries: [w1]
application-area: [all]
---

# Never invent an event subscriber signature — expose a procedure and leave a TODO

## Description

Subscribing to an event with a guessed publisher object, event name, or parameter list
(for example inventing `xRec`/`IsHandled`) raises `AL0280`/`AL0282` and does not bind.
LLM coders hallucinate these when the real event is unknown. If the exact
publisher/event/signature cannot be confirmed against the target platform symbols, do
**not** write a subscriber.

## Best Practice

Expose a public procedure that performs the work and mark where it should bind:

```al
// TODO: wire to the confirmed integration event once its exact name+signature is verified.
procedure HandleAttachmentDownload(var DocumentAttachment: Record "Document Attachment"; var Handled: Boolean)
begin
end;
```

## Anti Pattern

```al
[EventSubscriber(ObjectType::Codeunit, Codeunit::"Doc Attach Mgt", 'OnBeforeExport', '', false, false)]
local procedure OnBeforeExport(var Rec: Record "Document Attachment"; var IsHandled: Boolean)  // ✗ guessed event + params → AL0280/AL0282
begin
end;
```
