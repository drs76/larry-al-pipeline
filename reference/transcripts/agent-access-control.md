# Transcript — Agent Access Control - Permissions and Profiles

- **Source:** https://youtu.be/DRUr4byy8xQ
- **Channel:** Microsoft Dynamics 365 Business Central (official)
- **Ingested:** 2026-07-06 (auto-captions, cleaned)

---

Sales order agent is designed to use AI
to perform its tasks while keeping users
informed about key steps. The agent
interacts with Business Central
functionality in a manner similar to how
Business Central users interact with it.
It uses UI elements such as pages,
captions, tool tips, and other
properties to determine each step
required to complete the task. Business
Central includes a lot of powerful
capabilities and data to help users make
informed decisions. Take the sales quote
for example. Here you can instantly see
all the key details, fact boxes along
with a wide range of actions to manage
the entire quote life cycle. Still, as
an agent administrator, you want to make
sure the agent only has access to the
specific controls and data it needs to
complete its tasks, nothing more. Let's
take a closer look at the agent card.
You'll notice the agent shares the same
attributes as any other user in Business
Central. Its access is also defined by
permissions and profiles. You can easily
verify exactly which pages and controls
the agent can access by switching to the
profile that's assigned to it.
Notice how all the irrelevant data and
controls disappear, leaving only the UI
elements the agent needs to perform its
tasks. The agent comes with a pre-built
profile out of the box, and you can
easily customize it, adding or removing
pages, actions, and other controls as
needed.
Back on the agent card, let's explore
the agent permissions. The sales order
agent comes with a pre-built permission
set to help you get started quickly. You
can also easily review which permissions
are included. Your version of Business
Central may include additional app
source apps or customizations that
extend the process orchestrated by the
agent. Just like any other user, the
agent may not have the necessary
permissions to work with those changes,
which can result in permission errors.
For more advanced troubleshooting, such
as resolving permission issues or any
other issues the agent may encounter,
the best tool to use is the agent log
entries. Agent log entries give you a
complete overview of the steps the agent
performed while working on a task,
including the pages it navigated to, the
actions it invoked, and any issues it
encountered along the way. In this case,
I can see the agent is missing
permissions to the custom table needed
to complete the task. To fix this,
you'll first need to disable the agent
before adding the required permissions.
[Music]
On the agent card page, you can also add
additional users who should have access
to the agent pane where they can review
and approve agent steps. You can grant
or revoke ability to manage the agents
configuration.
Once you've made these changes, simply
enable the agent again.
All tasks are now running smoothly. And
with agent permissions and profiles,
Business Central administrators stay in
full control of the agents access.