# Transcript — What's new: Business Central integration with Microsoft Copilot Studio

- **Source:** https://youtu.be/GK6hM-nBYZk
- **Channel:** Microsoft Dynamics 365 Business Central (official)
- **Ingested:** 2026-07-06 (auto-captions, cleaned)

---

[music]
>> Welcome. My name is Błażej Kotełko. And
in this session, we'll talk about how to
build an agent in Copilot Studio for
Business Central.
Copilot Studio is one of the products
with from Power Platform family,
allowing you to build agents.
It's very popular term these days. And
those special software experiences allow
you to talk to your computer. Uh and
Copilot Studio is perfect for building
agents
without actually coding experience.
Copilot Studio has a way to build
an agent of pretty much for everyone.
So-called light experience, and you will
see that in in your Microsoft 365
Copilot chat.
Uh
and then also this kind of standard full
experience when you are building an
agent. This is what we will be doing
today. Of course, there is also a little
bit more advanced tooling in Copilot
Studio, more for more advanced
developers. Uh we'll we'll leave that
for now. And focus on building the
actual agent in Copilot Studio.
So, what you will need to understand is
agents that you build in Copilot Studio
have different kind of components. There
is a special orchestrators that runs
those agents. There is a knowledge
sources, data, uh AI models, and so on.
And of course, some user experience that
all runs inside the agent's brain. Uh
and then you have the interaction with
the customer, with the user, um on
specific channels. So, Copilot Studio
agent is actually published to a
specific channel. And we will be talking
about publishing to Teams and Microsoft
365 Copilot chat. But of course, you can
also build agents in Copilot Studio and
publish them and have them available on
channels like WhatsApp or Facebook
Messenger, uh even email and text
messaging. So, your customers can
interact with this agent through
different means. This is super important
for Copilot Studio.
When you are building an agent in
Copilot Studio, a Copilot Studio is this
maker experience where you're creating
the agent, and then the agent actually
runs and operates in the cloud. It is
connected to Business Central through a
Power Platform connector. We have a
special connector for Business Central,
and it gives you the ability to talk to
our APIs, and it has some extra uh
functionality that that is super useful.
There is also this new technology called
MCP server, and you will probably see a
session about that from my colleague
Kenny here in this event. Plenty of
other materials around MCP server these
days because this is a new technology
that
um that we added to Business Central in
a previous wave as preview. Uh so, you
can also work with Business Central data
through this MCP server. It makes makes
it easier for Copilot Studio and for
agents built in Copilot Studio to
operate on Business Central data.
That's why it's it's very important. But
behind the scenes, you are always
talking to Business Central through our
known Business Central APIs.
The best way to understand how does it
work is to see it in a demo. So, here
I'm in Copilot Studio. This is my
development environment. I can see
agents that I've built in Copilot
Studio.
The one that I prepared for this demo is
called laptop agent, and it is supposed
to serve
employees who are um ordering new
laptops, ordering new devices.
This agent actually has instructions. I
gave this agent instructions, and as you
can see, this is natural language
instructions
explaining to the agent what it is
supposed to do.
And then I gave it some knowledge. In
this case, I gave it um Business Central
documentation. So, I pointed it to
Business Central website with
documentation.
And I gave it some tools.
If I go to tools,
let me switch off this test pane here.
You see that I gave it three different
tools. I gave it an MCP server. So, this
is what I what I was talking about a
moment ago.
And that MCP server is configured for me
specifically
uh to access items.
I have a special MCP server
configuration for items because this
laptop agent is operating on items.
Um I have given it a special tool to get
a a link or a URL for a given item.
And I also gave it a flow, which is a
Power Automate flow, because in this
case, when I'm placing a purchase order,
I know how to do it in Business Central.
I want it to be uh covered in one
workflow. So, I created something
specialized. And this is a super
important for building agents in Copilot
Studio that you have access to all of
those different tools. If you have a
look at tools different different tools
here, you have connector tools, custom
prompts, flows, and also the MCP
protocol. And that's where Business
Central is.
Um but
Copilot Studio agent will decide which
tool to use uh regarding of depending on
your specific request from the customer.
That then, what is very important for
Copilot Studio is the channels tab here.
So, as you can see, I have right now
used this Teams and Microsoft 365
Copilot
um channel. And this agent is already
available
uh in that channel.
All right.
Our agent is built and published. And
now we are in Microsoft 365 Copilot
chat.
As you can see, I have my agent laptop
agent here on screen
uh along all the other agents that might
have been built for me or for my
organization. And this particular agent
uh has some kind of um
uh suggestions. For instance, it will
show me all the laptops that are
available as employees. And this agent
right now is querying data from Business
Central and finding
a non-inventory items from category
called laptops.
And showing me options for me.
And that way, I can interact with the
agent, ask it to
uh give me more specification about
about an item, or even place a purchase
order.
So, let's try to do that.
Let's ask this agent which laptop will
be better for graphic design.
As you can see, the laptop agent is
already giving me suggestions. Uh it has
knowledge from the internet about all of
those laptop models.
So, it's not only connected to Business
Central data, but also to a knowledge
sources from from the web. Yeah, and in
this scenario, we will be able to place
a purchase order for the specific
laptop. That purchase order will be
created in Business Central using a
Power Automate flow that we saw on
screen.
Plenty of other options available
through Copilot Studio and and Business
Central.
Let's talk a little bit about licensing
because Copilot Studio
is licensed slightly differently than
the rest of Power Platform.
Power Platform usage rights are included
in Business Central license. Copilot
Studio is built as usage. So, whenever
you build your agents in Copilot Studio,
and actually also when you use our own
Business Central internal agents,
uh you will be
built using Copilot credits.
And that is common
um
value or currency
for all agents across
Power Platform in Business Central.
This was a very short demo
giving you some options or some
perspective what to build with Copilot
Studio and Business Central.
>> [snorts]
>> You will find more resources online
under various links available on screen.
And also
just please have a look at
Copilot Studio training coming from
Microsoft. We have plenty of content
available and also linked through
aka.ms/bcal,
which is our main
collection of various resources for
Business Central.
All right, fantastic. Thank you very
much.