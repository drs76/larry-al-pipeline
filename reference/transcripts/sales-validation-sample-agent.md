# Transcript — Sales validation sample agent for Business Central

- **Source:** https://youtu.be/MKuOgMWXJ_8
- **Channel:** Microsoft Dynamics 365 Business Central (official)
- **Ingested:** 2026-07-06 (auto-captions, cleaned)

---

[music]
[snorts] Hello everyone and welcome to
the video about the sales validation
agent. My name is Nicola and I'm a
principal software engineer at
Microsoft. In this video, I will show to
you a sample agent that we have shipped
out of the box that you can use to see
how to build an agent within the
business central.
To access the sales validation agent,
you go to the avatar and you select
create.
On this wizard, you can see all of the
samples that we have. And currently, the
only one that we have is the sales
validation agent. We are planning to
build more and they will appear in this
list here. If you select the sales
validation agent, we are going to take
you through the setup experience how you
can set it up. Here you can see a brief
description of what the agent does. And
then if you say create agent, we are
going to automatically create the agent
and open its configuration card.
If we navigate to the right, you can see
that it has a dedicated profile. So its
UI is limited to the task that it is
supposed to do. If we select
permissions,
we have also lowered the permissions to
only the task that it is supposed to do.
So it has a reduced permission set. And
lastly, the instructions are here. You
can use them as the inspiration when
you're writing your own agents to see
how we have structured a specific agent
instructions.
If we would like to invoke and start the
sales validation agent, we can go to the
edit instructions and run tasks.
We will activate the agent and open the
page. And now I'm able to change these
instructions, tweak them to see how the
agent will work. And I'm also able to
give it tasks. Before you can give any
task to the sales validation agent, we
need to prepare the data because the
sales validation agent is checking for
the open orders and seeing if it is able
to release them to be shipped.
We have a dedicated uh documentation
article explaining the sales validation
agent and there is also a topic here
which explains all of the steps that you
need to do so the agent can have a
successful run. In the interest of time,
I have already done them. And also in
the documentation article, it says that
the agent is being started by saying run
process and shipment date. And then you
are supposed to provide the date. So I
will copy this text here and go back to
the business central. Back in the
business central, we're going to select
run task action. We will provide the
title that we want the sales validation
agent to run and process the following
shipment date which is today. And we are
going to exclude the message because
title is enough to tell the agent what
to do exactly. [snorts] Now when we
invoke okay the agent is going to start
the task has started again and we can
track it within this UI. We are going to
maximize the part and see which steps
the agent is going to do. We can see
that the agent has logged in and
navigated to the sales orders. And now
we are going to refresh to see what is
happening.
We can see that it is opening the orders
one by one and checking if they can be
released. So it is processing all of the
orders that we have in the list.
We can see here that it found one of the
sales orders to release
and it invoked the action
and the task has finished. It has
drafted a reply and it has requested me
to review the message that it created.
So now if I click on review outgoing
message, it will tell me all of the
sales orders that were released and it
is also going to list all of the sales
orders that did not meet the release
criteria.
On the bottom of the part, you can see
how many credits we have spent doing
these checks on all of the opening sales
orders. So you can easily track how much
does it cost to run the sales validation
agent.
That was all for this video. Thank you
very much for your attention.