# Transcript — What is new: Troubleshooting Business Central agents

- **Source:** https://youtu.be/K0i5rvqPC_o
- **Channel:** Microsoft Dynamics 365 Business Central (official) — 6:49, published 2026-02-27
- **Ingested:** 2026-07-06 (auto-captions, cleaned; "RO sender"=Role-Centre)
- **Distilled into:** `reference/AL-REFERENCE.md` §29 (Troubleshooting subsection).

---

Hello everyone. Uh welcome to this video
about troubleshooting agents. We're
going to figure out how you can unblock
your agents when they are stuck in
trouble and they can't uh continue with
the task that you have assigned to them.
To troubleshoot an agent, we need to
first understand how an agent makes a
decision. So an agent is a system that
takes a few different elements into
account to make a decision. The first of
them is the instructions which is the
blueprint how the agent works and what
its purpose is. Then we have the
available tools which is the
interactions it can do and it has
available at a specific context in
business central like for example on a
page. Uh then we have the virtual user
interface which is the way that the
agent sees uh business central to
understand what is available and what
data is there and what it can interact
with. Then we have the task messages
which give it specific context on what
to do with its instructions like which
sales order to validate if it's a sales
order validator agent. And finally we
have the step history the previous steps
where the agent can see what it did
before to understand also how to
continue based on this context. Using
all of this uh it has to make a decision
on what tool it should call how how
should it interact with business
central. So this way it uses them and it
decides for example to edit a field
where the field is called address and to
add the new value canelv7.
Now in business central we offer a set
of different tools that you can use for
troubleshooting agents.
For to demonstrate troubleshooting um I
have created an agent whose purpose is
to classify sales orders and assign a
risk level uh based on if this sales
order contains data that could be risky
to the business. for example, uh wrong
data that could cause business losses.
Um I've tried to run this agent and uh
at the end of its uh execution, it has
uh requested me for assistance. So
basically the agent is telling me it
can't proceed with the task because
there is a risk field that is it is
supposed to fill in and it couldn't find
it in Business Central. So what can I do
to figure out what is going on with my
agent? Uh Business Central offers um
some troubleshooting tools that you can
use to uh solve these kinds of problems.
First of all, uh starting from the
agents tasks page, I can see the task
itself that has run here and I can click
view log entries to see a log of all the
steps that the agent has done. Here I
can see at the very right that uh there
there is an assistance request from the
agent and it has the exact same message
as the one that I can see in my task
pane. So now I would like to drill into
it further and figure out exactly what
went wrong there. If I click on view
details uh I get uh a lot of insight
into what exactly went into the decision
of the agent. At the top I have the
decision itself, information about it
like uh what the description of it is
like an assistance request details and
so on. Going down I can see the what the
agent saw section. In this section, I
see a textual view of what the agent
sees as well. So, uh I can understand
exactly what things it can take into
account when it's making uh a decision
to edit a field or figure out what to
do. I see information like which page it
was on. So, in here I can see that it
was in the sales order page, the sales
order card specifically. I can see the
type of the page, if it is editable. I
can see the description of the page and
also all the elements on it like actions
and their descriptions and also I can
see fields.
Now if I want for example to search and
see if there is a risk field here, I can
just use my browser search and figure
out that there is none because I mean
that's what the agent was also
complaining about. But I also know from
the instructions that it was supposed to
fill in a reason field. So let's see if
that one is there. So I can do a general
fix of the agent that I have created. So
if I search for it, I can see that I can
find the reason field and uh I can see
it's also not editable. So I would also
need to fix that to uh unblock my agent
and have it continue. Why is the risk
field not there? Most likely I have made
a mistake on my profile or I've
forgotten to add it to add it via my per
tenant extension that I tried to
introduce. So if you have questions
about what the agent can see, what is
available, everything can be seen here.
Let's see the other sections as well. We
have the what tools the agent had access
to. This section uh gives you the
ability to see what capabilities the
agent could use at a specific point. So
you can see for example, it has the
ability to send assistance requests, but
also it can do a host of other things.
So it helps you design your
instructions.
Then I have the what data the agent
memorized section which lets you see
what the agent kept in its memory to use
for later in the uh process. So for this
one I asked it to remember important
data that it could use to fill in the
reason. So here we can see it used
things like what was the total amount of
the uh sales order to decide if it was
risky. Finally, we have the what
messages the agent had access to section
which shows you all of the messages that
the agent could see up to that point. So
you can understand what information it
was working with. So this would be for
example the message I gave it to
validate a specific sales order. Finally
on the side there are two fact boxes
that you can use. Uh the first one the
page stack shows you which pages were
open at that point as the agent needs to
uh open and close page this to navigate
between them. So now we can see it
started at the RO sender and it ended up
at the uh sales order card. And finally
I can see settings about uh what
currency is used and what formatting uh
the agent will use for its messages in
case the problem is in the final output
message. So summarizing through these
different sections that we just saw, we
can answer different questions that help
us troubleshoot agents. We can answer
what was on a page, what the properties
of the elements were on this page. Uh
descriptions so I can easier, more
easily guide my agent towards what to
do.
uh I have available tools which let me
discover the agent's capabilities,
memorize data for figuring out uh
exactly what the agent remembered, the
messages that I give to the task, uh the
step history of course, so I can review
what the agent did, and finally extra
information about uh the settings on the
agent. This was troubleshooting for uh
agents. Thank you very much for your
time.