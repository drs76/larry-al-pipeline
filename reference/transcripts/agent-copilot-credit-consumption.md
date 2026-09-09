# Transcript — Understanding Copilot credit consumptions for your Business Central agent

- **Source:** https://youtu.be/nnCLAqEM0Bs
- **Channel:** Microsoft Dynamics 365 Business Central (official)
- **Ingested:** 2026-07-06 (auto-captions, cleaned)

---

Hello everyone and welcome to the
presentation about overview of co-pilot
credit consumption within the business
central. My name is Nicolola Kukria and
I'm a principal software engineer in
Microsoft and one of the areas that I'm
working on is the development of the
agenting functionality. In this video,
I'm going to show to you how you can
assess how much does it cost to run an
agent per monthly basis and how much
does it cost to run the agent per task?
Because this is one of the frequently
asked questions by customers and
partners is how much does it cost to run
a specific task and the agent so they
can assess and plan the budget. Before
we begin, uh I will briefly explain to
you what the co-pilot credits are if
you're not familiar with this
functionality. The co-pilot credits are
Microsoft Unifi currency for AI usage.
So if you were using uh C-Pilot studio
or any other Microsoft functionality,
you will be familiar with Copilot
credits.
They are bundled with certain licenses.
You will receive free credits every
month. And Microsoft Business Central
license is one of the licenses that will
give you free co-pilot credits. So you
can try the functionality and see if it
works for your company.
If you need more copilot credits, you
can always acquire them as either pay as
you go or you can pre purchase the
credits and then spend them. If you do
not want to do this, you can of course
try out the functionality and wait for
the month to receive the new credits.
An important thing to say is that the
different features are going to consume
different amount of credits and this is
completely decided per feature basis.
Thus, the ability to see how much a
specific feature costs is something that
most of the users is interested in.
In the following demo, I'm going to show
you the functionality that we added so
you can within the business central
quickly assess how much an agent is
consuming for a specific time period or
for a a given task. To access the
functionality within the business
central, we can go to the agents list
and here under the actions, there is an
action that will show you a consumption
data for a selected agent. You can
select both the agents that were built.
If you're within the sandbox, however,
you can also see the consumption of
Microsoft build agents like payables
agent and sales order agent. If we
select the payables agent and say here
view consumption data, I'm going to see
the consumption data for the given time
period. The design that you're seeing
here is following the designs that we
are usually doing on the lists that we
are using for other places where we are
showing financial data.
In the bottom you will see for which
agent this is being monetized. Also the
date range here you will see how many
entries there are here and total
co-pilot credits use. So you can quickly
assess what is the consumption for the
given time period. The default time
period that we will show to you is one
month. And then you can quickly navigate
to previous month or go to the next
month. And there is an action to quickly
jump to the current month. If you are
browsing back the time period, you can
also adjust a custom type period by
using the these fields above. On the
repeater itself, you can see when the
entry was logged, how many co-pilot
credits we charged, what is the
capability and here you can see the
agents username. So this is the payables
agent for Kronos limited company. Then
you will see for which actions we
charged you and also for what
specifically we charged you with
additional details within the
description. So here you can see that it
is E document number 10 and that we
processed four lines. Thus we charged
you 20 credits for that and for this E
document we charged you 50 credits. So
we are charging 50 credits for
processing E document and then we are
charging 5 cents per line.
If we would go to a for example let's
say a custom build agent and we say view
consumption data you're going to get
exactly the same view here.
The data is going to be shown in a
different way because we are charging
differently per specific feature and you
can consult the official documentation
to see how individual agent is being
charged. One of the interesting things
that you can also see here is that it
did a lot of tasks.
And if I would like to see how much did
we spend for a given task, let's say,
for example, task number five. In the
list, you can see that task number five
was starting and it was stopping because
it is a multi-turn task. The quick way
to assess this is if you click here,
then we will filter out all of the
entries and show you only the entries
that are specific for task number five.
If you want to analyze and troubleshoot
what we charge this specifically, you
can invoke this link here and you can
see all of the steps that the task did.
Thus, you can do a quick assessment what
the agent did for this specific task. So
this was all for seeing the overview of
the per agent consumption. There is also
a second way how you can see the
consumption per task. And this one is if
you go to the agent tasks
and here on the agent task list all the
way on the right you can see all of the
co-pilot credits that the agent task has
consumed.
If I would like to see a specific
details for a given task, I can click
here and I can see the specific entries
that we are charging for this task. In
this example, we charged for analyzing
two attachments and we also built for
some specific steps that the agent did.
There are two additional details that I
would like to highlight. Uh because the
consumption data is sensitive, we are
controlling who can see this date. So in
order to see this data you need to have
agent diagnostics permission set
assigned or a super user permission set
assigned. Currently only the users that
have these two permission sets assigned
are able to see the consumption date.
Agent admin permission set is not
sufficient. This permission set is being
used to be able to configure and enable
and disable agents. However, you may not
want the agent admin to see the
sensitive data. for example, what the
agent saw or some specific documents
that you have seen in the
troubleshooting video. Thus, if you
would like your agent admins to also be
able to troubleshoot the consumption,
you will need to give them the agent
diagnostic set. If you would like to
learn how you can manage the
subscription and co-pilot credits and
billing for AI functionality within the
business central under the documentation
article for business central
administration center you can scroll
down and here is a dedicated article
that is covering consumptionbased
billing.
Here you can find all of the information
around the billing and all the way to
the bottom there is also a dedicated
video that you can use to learn more
about this subject. So to summarize the
video you have seen how we have
introduced a simple overview of copilot
credits consumption for the agent tasks.
I would invite you to try it out and to
let us know what you think. If you are
missing any kind of functionality or if
you would like to get any additional
features, please reach out to us through
the BCVI engage. Thank you very much for
your attention and hope to see you in
the next video.