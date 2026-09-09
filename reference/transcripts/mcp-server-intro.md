# Transcript — Introducing MCP server for Business Central

- **Source:** https://youtu.be/iViHfCgL2L8
- **Channel:** Microsoft Dynamics 365 Business Central (official)
- **Ingested:** 2026-07-06 (auto-captions, cleaned)

---

[Music]
Welcome to this video of introducing our
new MTP server for Business Central. My
name is Kenny Pontopidan. I'm a program
manager here in the product team and
with me I have Yens.
>> Yes, I'm engineering manager in the
runtime team in Business Central
developing the MCP server.
So at Built in the spring of 2025,
we had this slide with Microsoft loves
MCP.
But what is this MCP? Well, it's it's
just a um it's a new protocol, model
context protocol, which is an open
protocol to standardize how applications
can provide context to LLMs and and talk
to LLMs. And LLM is actually a large
language model.
>> LLMs is a larger language model. Yeah.
We we try to abbreviate everything to
have code names and Yeah.
>> threeletter acronyms to rule the world.
>> Exactly. So three concepts that are
important in this world. We have hosts,
we have clients and we have servers. So
a host in in MCP is what orchestrates
talking to different MCP servers and
also interacting with the language
model. The client um which al could also
be called a session the so one one
server can have a number of sessions
open. These are the MCP clients and they
handle all the protocols and talking to
the server and servers are just the
toolbox toolboxes. So there are multiple
many many different servers data versse
uh finance and operations uh others and
these are the the actual endpoints the
things where you can interact with the
system. If you look at this set of icons
it's kind of something is missing here.
Something's missing.
>> Yeah.
>> And of course that's business central.
So we built a new MCP server for
Business Central data and uh the goal of
this initiative is basically to take
everything you can do in Business
Central and make it available for our
new primary users AIS and agents.
>> Yes. Because over time we expect more
and more tasks to be possible to just
automate using AI.
>> So why did we do this? Well, the AI
future is is AIdriven automation as Yen
Yens mentions. Um, and it's it it is
both automation has been around for a
long time. That's that's where APIs were
born. But APIs are just the beginning of
MCP server. Uh there's a lot of things
you can do if you add a language model
and an orchestrator. So uh with MCP
server uh we standardize how that is
possible and hopefully the business
value of this is that you partners and
you customers can start automate start
with the repetitive tasks but hopefully
also move into the tasks that are not so
like super well definfined for now where
a language model and an orchestrator
really can help even automate those.
Yes, this is actually where language
models shine is where the input is a
little fuzzy where you have an idea of
what you want but you don't necessarily
want the exact same thing day in day
out.
So in October we announced the public
preview for Business Central MCP server
here in version 27.1. And in this video
we're going to just focus on the basics.
So uh what we call uh the the default
configuration then we have other videos
going more into depth of of how to set
up configurations and also more advanced
topics. All right. So let's see the very
very first plain vanilla demo of MCP
server with Microsoft Copilot Studio.
So, Yens,
>> yeah, I'm going to talk you through how
you can most easily get running with MCP
server connecting to Business Central.
So, in order to run this, you want to
set up an agent. Now, we are targeting
Copilot Studio as our prime client uh in
this first iteration of the MCP server.
And in Copilot Studio, you create a new
agent. You can give it a description and
then you select your agent model. In
this case, I've selected DBT5 auto. The
next step is to add the tool that allows
you to actually get to Business Central
data. The easiest way to get to that is
to select the model context protocol and
type Business Central, which will make
the um Business Central MCP server
preview show up in the list. You select
that and you select add and configure.
That will bring you into the connector
menu where you need to specify the
environment that you want to connect to
and the company that you actually want
to fetch data from. When you have saved
this, you are ready to ask the first
questions. Please notice here that I
haven't filled in anything in the
configuration part. We will get back to
that later. You will you do have a
default configuration if you don't
specify anything there which is that you
have read only access to all API pages
in the system.
Then you can test your connection. You
can run a session in copilot studio. It
will ask you to connect and of course
you need to connect in order to read the
data. And then you can ask it simple
questions like do we have customers in
Florida which will look through which
will find the customer list look through
it and check if there are actually any
um customers in Florida. It even figures
out that it needs to search by FL
instead of Florida because that's a
standard abbreviation. You can also ask
it more complicated questions. I'm not
going to talk you through this, but
generally the the LLM which is running
in the MCP host will do its best to find
the tools inside Business Central that
can help it answer the question that you
gave it. On the Business Central side,
you need to make sure that you enable
the MCP server. So, you do that from the
feature management page where you flip
it to all users. And this is likely
going to change once we go into general
availability. Right now this is a
preview feature. So we always have this
feature management switch. Exactly.
So to summarize the steps required to
try out agents using MCP is you enable
MCP and business central. You create a
new agent. You select a model. You add
the uh configuration parameters the
environment name and the company and
you're ready to go.
>> Sweet.
Now I did say we didn't pick a
configuration but behind the scenes if
you don't pick anything you will get a
default configuration which effectively
just has three things it can do. It can
look for actions it can describe an
action and it can invoke an action and
then the LLM will use these three to
find the tools it needs to answer your
question.
All right. So that was simple. That was
read only. So what about write
scenarios? For that you need something
called MCP configurations. And this is a
teaser for the next video where you will
learn everything you need uh to know to
set up that. Um so stay tuned for the
next video.
And that's it for this video um on MCP
server introduction. As just repeating,
our vision for MCP server is basically
here on on line two. Make all
functionality available to AI and
agents. And of course, we need to do
this in a secure revi reliable way and
MCP seems to be the protocol that is the
one that is industry becoming industry
standard. So of course, Business Central
team is is joining that initiative.
>> Yeah. And where this really shines is
where you have scenarios involving
multiple products because you can have
you can set up agents that use multiple
tools, not just Business Central. It can
read from other systems and actually
reason over that and gather information
from multiple sources.
So for the first video here, call to
action is start just set up a test
tenant, enable MCP and try using C-pilot
studio to do your first agent.
Experiment a little bit with scenarios
with models and then uh write about your
experience and of course engaged with
engage with us on Viva if you are a
partner so that we can all learn uh the
things that we should tweak before we
make this generally available. And if
when you have copilot studio and you've
enabled the MCP server, it literally
only takes about 1 minute to set this up
and then you can get started trying this
out.
>> A few uh things before we end. This is
general business center resources. The
first is BC all or aka.ms/bcall.
These are the just the landing pages or
aka links for everything you need to
know as a partner. The second is
important because aka.ms/bcy
yammer is the signup page for you if you
were previously on our yammer network.
That's what where you apply to get
access to viva which is the new yammer.
Um we also want to make sure that you
follow the office hours. We'll have an
office hour on MCP server in I think in
January 2026.
Um follow us on LinkedIn and uh YouTube
especially uh for LinkedIn this is where
the product group posts uh weekly news
on on things that are uh upcoming and uh
things that we find important. So this
is where you stay on top of of the news
and YouTube is where we publish both our
launch edition these videos and more. So
make sure that you follow us there to
kind of learn a lot about what's
happening in the business central world
as seen from the product group.
So that's it Yans. But uh if you're
curious about the next videos, watch the
down in the description and go on to
learn more about configurations. And we
also have an advanced topics for you if
you're really that interested.
>> Yes. So we hope to see you there.
>> Thank you. Thank you.