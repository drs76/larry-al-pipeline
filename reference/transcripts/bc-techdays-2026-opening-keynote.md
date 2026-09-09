# BC TechDays 2026: Opening Keynote

- **Source:** https://www.youtube.com/watch?v=uxClMdhpJak
- **Video ID:** uxClMdhpJak
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 104m21s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

It's a pleasure to be here. I've been to
Navtech days and VC Tech Days many years
and I think it's a fantastic conference
with all of that technical content.
Today we're going to talk about
AI
and I don't think that is a surprise to
anyone. Everybody talks about AI these
days and we have also been talking about
AI for the last couple of conferences
here. In 2024,
we talked about and showed co-pilot
features. We showed the chat experience
inside the client. We showed marketing
tech suggestion, sales suggestion that
were built on the co-pilot SDK. These
copilot features are narrow in scope.
They typically involve one call to the
AI model and you get a response back and
you process that. The end user is
responsible for the end-to-end process.
So they have to do all of the work but
they get help in certain places from
these co-pilot features. So they're
narrow but it doesn't mean they are not
useful. They can be very very useful. In
2025 we introduced a couple more copilot
features for example autofill summarize.
Again they are assistive features. They
help the user but the user is
responsible for the end to end process.
But we also introduced our first two
agents. We showed them in preview
version versions sales order agent and
payables agent and there the flow is
turned upside down because it is the
agent that is responsible for the end to
end process and the agent will invoke
the user at certain times to to get over
something or get approval for something.
So it's a radically different approach
and this year it is all about aentic AI.
There are AI agents everywhere, not just
in Business Central, also the whole
software engineering industry and even
outside in legal, in journalism, in
marketing. It's everywhere.
So, you might be wondering
why didn't we introduce agents back in
2024? Because I mean, they're so much
more useful, right? They can they can
they have a lot more potential because
they can do so much more. Why didn't we
introduce them earlier? And I think the
answer is the models back then were not
ready for it. It actually requires a
stronger AI model to power an agent
because it has to do so much more things
right.
I'd like to show you a or give you an
intuition of the evolution of AI models.
And to do that I want to introduce the
concept of time horizon of software
tasks. It's a concept that the meter
organization uses. Meta is an
organization that evaluates AI models to
see how capable they are over time as
new models come out. So the way a time
horizon works is consider GPT 3.5. If
you have a task that GPT 3.5 can handle
with 80% success rate, then the question
is how long time would it take a
software a human software engineer to do
the same task? they actually had people
come in and do these tasks. The answer
was 15 seconds. So the 15 seconds is the
human time to do that uh task. What can
I do in 15 seconds in terms of software?
Write one line of code, maybe two. It's
not a lot. So would I delegate such a
task to an agent? Uh no, because it
would take me more time to delegate and
wait for it to do it.
Then we move one year ahead and GVT 4.0
from zero comes out and it has a time
horizon of 53 seconds. That's actually
an impressive improvement, right? More
than tripled the time, but still it is
not enough that I would actually
delegate work to it. Let's move ahead
not one year but one and a half years.
01 comes out. It has a time horizon of
four minutes. It's a impressive
improvement.
Then we go eight months further and
Office 4.0 comes out, it has a time
horizon of 20 minutes. And now we're
talking because would I if I have a task
that Opus 4.0 can handle, would I spend
a 20 minutes myself or would I spend
let's say couple minutes or five minutes
whatever to tell Opus 4.0 zero to do it
and it does it in also maybe four point
five five minutes sorry five minutes and
I've saved 10 minutes right so now we're
talking now they're actually becoming
useful and time savers
just nine months later Gemini 31 Pro
comes out it has a time horizon of 90
minutes that's incredible
so if you plot these time horizons on a
graph you get a something that looks
like an exponential development
It starts really really slow but the
capabilities they just accelerate and
keep accelerating. Nobody knows if this
exponential development is going to
continue. That is not for certain at
all. But it in a sense it doesn't matter
because
the way the capabilities of the models
today is already so great that uh it is
revolutionizing the field of software
engineering as we'll talk about a bit
later. But I I think this also gives you
an intuition of why we couldn't have
done agents in 2024 because the models
were simply not capable to to to do
that.
So we are going to talk about AI agents
in this keynote. AI agents uh can be
many things. We're going to talk all
about all of about all of these things.
We have a native BC agents, sales agent
pays agent, we have co-filer studio
agents. You can also build your own AD
from scratch if you want. So these are
what we can call product agents. They
are kind of part of the business central
user experience and used by end users.
But we're also going to talk about
engineering agents. Agents that help you
with your software engineering tasks.
They can be VS Code agents, CLI agents,
and GitHub agents. And we're going to
talk about all of these.
So let's uh let's jump into it. Let's
talk about the native Business Central
agents. These are deeply integrated into
Business Central. You've probably seen
Sales agent and Pays agent before. What
we're also starting to see is our
partners build agents themselves and
deploying them to customers. And I'd
like to show you a video from one of our
partners.
Every day, thousands of shipments move
across oceans from farms in Latin
America and Asia to warehouses in
customers in Europe. At the heart of
every shipment is a shipping manifest. A
manifest is the official document that
lists everything in a shipment, what
goods are being transported, in what
quantities, the container, pallet ID,
and what is loaded on the pallet. It's
essential for logistics, finance, and
customs. But for many companies, it's
still handled manually. Until now, that
was the reality for companies like
Interfruit. Every day, vendors emailed
PDFs with the manifests listing loaded
pallets. Someone had to open the email,
download the attachment, read the
document, verify the information, and
manually create purchase orders in
Business Central. Each manifest took 20
minutes to process, and this happened up
to 10 times a day. time consuming,
repetitive with risk of human error.
That's where Aptian's manifest agent for
Business Central changes everything. The
agent continuously monitors a shared
mailbox. When a manifest arrives, it
automatically reads the document,
extracts the data, validates it, and
creates the purchase orders in Business
Central. The right vendor, the right
items, the right quantities and
locations. No manual work required
except a simple initial email
confirmation. The agent runs securely
through a job cue every 5 minutes,
ensuring manifests are processed
quickly, and consistently. Each step is
logged. Every action is traceable. What
once up to 20 minutes now happens in
minutes, accurately, reliably, and
automatically. The result? Less manual
work, fewer mistakes, faster operations,
and teams can finally focus on what
matters instead of processing PDFs.
This is a Gentic automation in action
built by Aption, powered by Dynamics 365
Business Central.
So, kudos to Appen for making this a
very nice agent. And now you might be
wondering how can you create these
agents and the answer is we've made it
now very easy to get started. We have
introduced an agent design experience
very nice experience inside the client
where you can start to create agents on
your own. And when you are ready to kind
of package it up and deploy it as an
extension we have an SDK to uh do that
too. And I'd like to show it to you.
Actually I'll invite Stefan on stage.
Please give Stephan a warm welcome.
Thank you, Christian. Thank you. Let's
see if I can wake this one up. Let's uh
let's build an agent that actually does
something for us, a real business
process. So, you can see up here, I'm a
I'm a developer, maybe I'm a consultant,
maybe I'm even a power user in in a
company that wants to build my own
agent. So, in this sandbox here, I'm
able to do that. And up here, you can
see the the agents that Christian just
talked about. They're ready for me to
configure. But I also have
>> an agent.
>> Which one are you?
>> Oh, shoot. Sorry.
Go to five. There we go. So, try again.
Right. Try again. One, two, three. So,
up here you see all the agents that
Christian talked about the sales order
agent and the payables agent and so
forth. But we also have the agent we can
create here our own. So, let's get
started. You guys ready for that? Let's
see.
So, wakey wakey. I can start here and I
can create an agent from a template and
we'll of course add more templates as we
go along, but I'm going to create one
from scratch.
Here I get started in a wizzy wick kind
of a wizard experience here. And that's
really helpful because I can start by
putting in a name. And what I want to do
here is a simple example of a sales
return agent that helps me track the
incoming uh return requests and does the
credit memos and so forth. So let's call
it the sales return agent, right? We can
give it a name. This this doesn't have
to be fancy. It's for me the human to
understand what this is all about. So we
do sales returns. Okay, so far so good.
Now we get to the important part. So an
agent here is not just magic, right?
It's actually more than that. It's what
the agent can see, what it's allowed to
do, what tools it has available, and of
course the instructions on what it needs
to do. So we start with what it can see.
We can choose here because we want to do
returns, we can choose to start with uh
the accounts payable administr account
receivables administrator, sorry. Um
that will give the agent a broad enough
view of the product to kind of do its
thing. I will need to return to this to
figure out if I need to adapt the view
that the agent has and the agent can
see. So this is the the view on the
product that the agent has. It's what
actions are available, what fields are
available. So what it can see and do.
Next things is the permissions. Here I
again I want to narrow down the
permissions to what the agent can do. We
are in experiment mode here. So of
course I'll choose a very broad one.
Right. Remember, we'll come back to this
when we know the agent and we know what
he wants to do and we'll adapt this and
make this even more strict. Okay, now
the important part, right, the
instructions.
So, I'm imagining here that we have a
scenario where I'll receive an email and
then I'll have to process that and
figure out what that needs to do. So I'm
thinking uh a good instruction here
would be a overall description of what
the agent is, some guidelines to what it
can do and then the steps it actually
needs to do. So I talked to some people
that actually knows how this works and I
created a small one here. I'll copy that
and put that in here.
So the top here is what's the purpose of
this agent receiving the the returns?
What are the guidelines? Don't create
credit memos without approvals. Find
customers by email, use pieces if you
don't know what kind of unit measure it
is, these kind of things. And then the
instructions.
How do we handle returns? Well, we
create a credit memo. We put in some
information about the work description.
Uh maybe we uh create the credit memo
and print it as a PDF and attach it as a
reply. Seems good enough, right? It's
the first iteration. It's not perfect.
Absolutely not perfect, but it's good
enough to me to get started to kind of
figure out what my agent is supposed to
do here. So, I'm going to say okay to
that. Now, we need to test the agent.
So, we'll go here. We'll activate the
agent so it can start processing.
Agents are not autonomous as such. They
don't work just by activating them. They
need to be triggered somehow. They need
a task to do. So here we'll give it a
task by creating a task. Here
the scenario I was talking about was an
email coming in. An email has a subject,
a title and I came prepared. So I have
one here. Somebody wants to return some
damaged chairs.
We had in our instructions that uh we
wanted to look up by name or by email.
So I prepared an email address. This is
one of our customers. So, I'll get an
email from Robert and what will the
email say?
It will say we have some damaged chairs.
I would like to return them. Uh, I want
to return all the chairs. So, that's an
interesting statement. Uh, and I also
want to return all the lamps, right? So,
how do we know more? Well, Robert here
is actually a good at adding some more
details. So, he added
the invoice that he got. And on that
invoice, we can see here clearly that he
received some chairs. Actually, he
received both black and yellow chairs.
And he received some labs. This is
great. Awesome. He'll attach that to the
email. And he also
added some details on what was wrong
with the order. He put in some text here
on the image saying that there's some
scratches and there's a broken leg.
Right? So, from that, we can learn a lot
more about what's wrong.
We'll put that in here. Now I can start
this task. But before I do, remember I
said we have to iterate on this. We have
to come back and change the
instructions, the profile, the
permissions. So I'll go up here and save
this as a template so I don't have to
paste this in all the time. Right now I
can use this template again and again
when I iterate on one of these
dimensions.
Let's do that. And we don't want to edit
it now. We just want to run it. So now
I've kicked off a task for the agent to
process. And the agent is active. We
just did that. But the agent runs in the
background. So it will not pick it up
right now. It may start processing, but
it will figure out what to do along the
way. And I can keep an eye on this as an
engineer here trying to figure out what
this agent does in the task log.
The first thing that happens here is
that we see that it got some kind of
message. And we can see that here. If I
refresh here, it may not be ready yet.
Fair enough.
Let's give it a one more go here.
Fair enough. We'll give it a little
time. But inside each task log, you can
find some details about what that task
is about. So, we can look at a task log
entry here. This one is pretty simple
because it's just a message. So, this is
what happened. A message was received.
And right now there's no action for this
one. Uh we can go to the details and
view what message all about. We can see
the the attachments and so forth. And
hopefully when we come back here, my
agent has picked up some more work. And
that didn't happen. So of course I came
prepared. Here we go. Magic.
So here we have the the return agent. As
you can see this is my backup. So uh he
did some work. same message he came in
and we can look at some of the details.
Let's take one of these uh interesting
entries we have here. So when we look at
these entries, we can look at what the
agent actually saw. In this case, we can
see that it was on a sales credit memo.
It we can see the page type and all
these properties that the agent can see
and look into. We can see what actions
are available. What can actions can the
agent choose from? And of course some
place down here there's some information
some information about the the fields
that were on the page. So this is all
the information that the agent has
access to. And from there it can choose
to do something. And how does it do
something? Well, it can choose
it can choose from the tools that the
agent has access to. So the platform
puts out some tools that the agent can
use. In this case we saw that it wanted
to invoke an action and that's actually
a tool here. So it has the data and it
has the tool and now we can go do stuff.
At some point the agent may choose to
involve
um oh wrong one involve a user and we
can check up here there's a user
intervention type here and this is
actually what we see over here. So we
see that there's a user intervention to
review a message. We can go review that
and we can see if it's the right kind of
message. We can even see if it attached
the document that we wanted it to
attach.
I have too many fingers today.
And we can see that's the sales credit
memo that it was to create. So we have a
full process here. It can do stuff. It
can figure out that it needs to create
the credit memo and create the reply and
attach the document. And it can even
tell me here that there were some
damaged chairs. So, it took the work
description in there also. Great stuff,
right? But this was just the beginning.
And as you can imagine,
these instructions are maybe not quite
done yet. And the first thing I notice,
at least here, is that maybe we should
validate that they actually bought the
items that they're trying to return.
Right? So, this is what we do. We go
back, we revised instructions, we figure
out what else to do. So we can go again
here and say we want another one here.
We're saying validate
that a sales invoice exists with and
spilling is also
uh the items
the customer wants to return. You get
the picture, right? I changed the
instructions and now I can run the task
again because I have a task template. I
can just click here and click run and it
starts again, right? And we can even go
back here. This one actually finished.
So you see this is how this works. You
have act you have access to the task
lock to investigate what goes on. What
is the agent doing? How is it processing
the request? What actions will it take?
What data will it insert? And then you
can iterate on permissions on profile
and on the instructions. At some point
you're ready. We think now is the time
to take this from an experiment into
something we want to put in production
and share with others. So I can go and I
can download the instructions here.
There we go. I did that already. So we
can do it once more. Um and then you can
go to Visual Studio Code. So we go to
Visual Studio Code and we do a new
project. We've added the template here
that gets you started really fast. You
just use the agent template. Define
where you want to put it. Put some kind
of uh object range start.
And now you're ready. You have a
template project here that has all the
details that you need in order to create
your own agent
um in Business Central. Okay. So, what
will I do with this? Well, the first
thing I want to do is read the read me,
right? This readme here contains all the
information I need to know in order for
me to build my own agent.
And why should I build it? Right? Nobody
wants to do all this work by themsel.
So, I'll use my agent over here. And
I'll go to my downloads folder here
somewhere. Where is my downloads? There
we go. And I'll take the agent
instructions. I'll add those. So, now I
have the instructions and I have the
read me. And I'll just say use the read
me to implement
the agent with the attached
instructions,
right? Doesn't get easier than that.
Just click once and it will do all this
stuff. Now, I know all of us have like
coding guidelines and other things and
naming and style. So, I actually created
a different agent over here.
This is my ray returns agent. I gave it
a name because it's much more friendly.
So I did the same thing. I took the
template and up here somewhere in the
beginning I told it to use the read me
and the instructions and create the
template.
It did it and as any good um copilot
functionality it has a ray returns
capability that you can turn on and off
in the admin. It has the implementation
of my agent here. the type in the agent
metadata provider. So we can tell the
system about what kind of agent it is
and of course it has uh all the setup
page that I want for my agent and all
the other things even the instructions
that we downloaded right
so quickly I can get started creating my
own agent and now I can iterate on this
one at some point I feel let's go to
production so I'll press F5 or I'll
actually upload it into my production
environment so let's go see this one
there we
Here's abduction environment.
Looks kind of the same, but it doesn't
have the agent plus. So, it's easy to
see that it's not a sandbox anymore. But
now it has my ray returns. There we go.
It's ready for me to activate and set it
up. The first thing you will notice here
when I activate it is that the setup is
experience is a little bit different
than the agent creation. So when you
create your own agents like this, you
have to provide all the configuration
that you want users to be able to do and
that includes if you want them to be
able to adjust the instructions slightly
or any other configuration settings that
you might want. So now we've not only
just built an agent in a sandbox and
demoed how that worked, we iterated on
it. We figured out what didn't work and
we tried to to make the the agent a
little bit better and we could do that
many times. But we also took it to
production. We took it to a product we
can ship and share with others. And with
that, we've created an agent. Back to
you, Jason Christie. Thank you very
much, Steph.
Yes. So, we've seen now how easy it is
to get started to create a an agent in
Business Central with our design
experience and with the SDK.
Let's move on to Copiler Studio. Copiler
Studio is a very flexible environment.
It has connectors to a thousands apps.
So it can integrate with many different
products and you can run it on a trigger
like in autonomous mode or you can run
it in interactive mode um and for
example interact with it in teams. So if
you need that kind of flexibility,
Kofile studio is a good choice for you
to create your agent there. How are we
enabling business central to be used in
copilot studio? We are enabling business
central
through making it an MCP server. So as
an MCP server, copilot studio agents can
interact with it. And I would also like
to show you how that works, but I'm not
going to show it myself. I would like to
invite Pard on stage. Please also give P
a warm welcome.
Hey everyone. Uh I'll just start up my
machine
and
yes so uh my name is Purushadi. Uh I'm
an engineer with the runtime team and I
want to show you how easy it is today to
set up an external agent that talks to
your business data whether it's using
copilot studio or any MCP client whether
it's VS code copilot or clot code any
MCP client essentially so I'm in the
standard agent builder experience of
copilot studio and I honestly don't
really know how to build these agents in
copal studio so what I've done right now
so far is just set up very basics I've
set set up the name of the co-pilot
agent that I want to build. I'm building
a customer copilot and I wanted to
handle all queries related to my
customers, their financial documents and
their sales, invoices, orders and so on.
I'm using the standard agent model which
is a GP5 chart and a very simple set of
instructions on how I want my model to
work. In this case that it's
specializing inquiries about my
customers and I wanted to proceed
without asking me for confirmation and
some additional guidance on how to use
resources and how to use web parch since
I'm also enabling web search. But of
course when you're building agents for
Capala Studio, Copala Studio gives you a
lot of flexibility when it comes to
connectors, tools, additional knowledge
sources and so on.
But right now my agent does not work
because it's not connected to business
central. But using the Business Central
MCP, let's see how we can make it work.
So all you need to do is go to the tools
tab and select add a tool. And here I
want you to search for the Business
Central MCP connector.
and click on model context protocol. So
the connector shows up.
And now I just click on add and set it
up. In my case, I already have the
connector set up. I'm just going to
enable it so we can skip the
authentication flow. So here's the
connector and it should connect in just
a second.
And now
perfect.
So when you set up the connector, you
only need to provide three important
things. You need to provide the business
central environment you're trying to
connect to. You provide the name of the
company and you provide something called
the MCP server configuration.
All right. So what is MCP server
configuration? It's a tool set. It's a
set of tools that have been defined by
an MCP admin on your business central
and it defines what APIs or what tools
that can be exposed under this
configuration name by the MCP server. So
for example, if I'm building an
inventory management
uh agent, then I can create a tool set
that has only the tools relevant for my
use case and I can use the inventory
management tools. In this case, I'm
building a customer agent. I'm using
these customer APIs, but I'll show you
how it works in just a minute. Right,
if I scroll down, I can see all the
tools that I'm getting from my business
central. And here I have tools for
managing my customer. I have tools for
managing my sales orders, invoices, and
so on. And so the same query that did
not work, I'll try that again. And we
can quickly jump into how we can change
the configuration. All right. So, new
session
and all right. So, while the agent
works, let's take a look at Business
Central and how we modify the
configuration, how we add more tools and
how we can change or add more permission
to my tools. So, I'm going to switch to
Business Central here. Just search for
MCP
and that brings you to the MCP
configuration page where you have all
the tool sets or configurations defined.
Now, we were dealing with the customer
API. So, I'm just going to go in this
one. And the first thing you'll notice
is that the UI is a bit different,
right? If you have been using MCP, it's
it's a lot different. The first thing is
that we have now multiple server
features. And in this one, API tools is
enabled. What that means is when you
publish APIs to Business Central, those
APIs can now be exposed as tools through
your MCP. And in this case, if I scroll
down, I can see all the APIs that are
added to this particular configuration.
And I have tools for customers, sales
invoices, orders, and I can also see
specific permissions that I provided to
these pages and APIs. So I have I'm
allowing read, I'm allowing delete, and
so on. Right?
Another important thing I want you to
notice is now we also support API
queries because of course API pages are
great for creating modifying deleting
records. But with API queries you can
get data joining multiple tables
performing more complex operations like
grouping aggregation and so on. All
right. So how do you modify this
configuration? All you need to do is
disable the existing configuration and
click on select APIs. And that should
bring up a list of all your API pages
and queries in just a second.
That's it. Right. And for example, I
don't want my agent to be able to delete
customers. All I need to do is go over
here and unselect delete. And that's it.
Once I'm happy with my configuration, I
can just enable it. And everything just
works just like that. all the MCP
clients or copilot studio that is
connected to this configuration they get
the tool list change notification
through the MCP protocol and they'll get
the new set of tools
I think the agent should have also
completed so I'll just show you what
happened here with the new set of tools
business uh the co-pilot studio agent
made a request to business central and
it used the customer financial details
tool when the tool returned some results
it returned the results as a file which
is the embedded resource
And then what copilot studio did was it
took this file reference and put it and
plugged it into the code execution tool
which allowed us to generate these nice
visualizations.
But what happens if you have a very
large number of APIs in your
configuration. So I have a demo
configuration that I've created here
which is just enable all tools right and
in this what I've done is I've added all
the published API objects as tools for
this MCP server. The problem is this
configuration will not work with most of
your MCP clients. The reason being way
too many tools. Copilot studio has a
hard limit of just 70 tools. And so what
we have also added is under API tools
there's an option called dynamic tool
mode. So what you can do is you can
deactivate the configuration enable the
dynamic tool mode and when you do
you get three system tools or three meta
tools that are there on the right side
you can see and now agents can use these
three meta tools to search across your
configuration or configured APIs to and
they can use the describe tool to
understand how to use an API tool that
you have added and then the invoke tool
to actually do the task or carry out the
action.
Finally, when you're building agents,
it's not always clear what API pages or
API queries you need to add to the
configuration. And that's why for more
generic data Q&A scenarios, we are also
going to be starting a preview of data
query tools, which allow your agents to
write queries and execute them directly
against your Business Central tables and
get data. But I don't have time right
now, but we'll have to go to one of our
sessions and we'll talk about it in more
detail.
Finally, when you're happy with the
configuration, just enable it. And if
you want to test it out in a client like
MCP uh like VS Code or your CLI agents,
all you need to do is select options and
you can get the connection string here
directly. So in this case, I'm just
going to get the connection string from
this and set it up in my VS Code. We've
also made it simple to just share
configurations. By the way, you can
export configurations, import them, and
so on. All right. So in VS Code, every
time you add MCP servers, you add it to
the MCP.json. So that's exactly what I'm
going to do. I'll just copy the
configuration here. And
in just a second, Copilot Studio in this
case, VS Code should detect the
configuration
and it will get the latest set of tools
which should be just three because we
enable dynamic tool mode in that
particular configuration.
So,
so the main thing I wanted to get out of
this is that if you have any MCP client
that supports the OOTH 2.1
authentication, you can now connect it
to Business Central MCP. We have a
special dedicated connector for Copala
studio and you can also expose any API
page API query to your business central
configurations to create very dedicated
agents for your use cases. And we'll
also be starting the preview for the
data query execution tools that allow
you a lot more flexibility and your
agents a lot more flexibility in getting
the right data. And of course security
is important, safety is important. And
so you can use the block edit tools
directly on configuration to just
disable all modification scenarios and
just default to read only scenarios. And
you also go through the normal business
central permission system. So if the
user has a tool but they don't have
access to the underlying table, they'll
not be able to get any data out of it.
But that was the business central
platform MCP, right? And it's great for
building agents that interact with your
business data. But we also have an admin
center MCP that allows you to just
manage your environments directly. So
you can give this MCP to your cloud code
or VS code agents and they can just
manage the entire life cycle of your
environments, create sandboxes, uh
investigate upgrade issues, reschedule
upgrades and so on. The only thing
missing right now is some destructive
endpoints, but this is only for the
duration of the preview, but we will be
bringing them back as well. That's all
from me. Thanks a lot. Back to you.
>> Thank you very much.
>> So that shows how you can build agents
inside business central if you want that
native feeling or you can create them in
copilot studio for example if you want a
little bit more flexible experience or
in any other MCP host. uh really so th
this is where I would recommend you
create your agents. They provide a very
nice environment that you can very
easily get started. It's more
configuration, not so much code. It has
guard rails. It has a testing and
experimentation experience and uh it
just makes it a lot easier to create an
agent than if you had to do it from
scratch. But if you have a scenario that
for some reason requires you to live
outside of those experiences, then you
can do so. You can build an agent from
scratch. It is not something I would
recommend for the reason I explained
before because you are taking on a lot
more work if you do everything yourself.
We have an example like that. We
actually have a scenario where we want
to be exposed in new form factors. we
want to integrate with multiple backends
and it didn't fit in those two cases and
this is actually our third agent from
Microsoft which is the expense agent and
I would like to show you that or again I
would like to invite Michael on stage to
show you expense agent please give him a
warm welcome
let me just get it booted up
All right, let me see. That's great.
Okay,
so I'm here to talk about the new
expense agent in for Business Central.
Um, I know we're just getting started,
but uh, imagine that you're back in the
office Monday morning. It was a great
conference, PC Tech days, but of course
now the there was great sessions and
everything. There was dinners, but of
course there's also this little bit
annoying things that you now captured
some receipts, some expenses that you
actually need to get processed and get
refunded or proved that you have these
expenses.
So that's not the favorite part of going
to this conference, right? But this is
where we come with the expense agent.
Um, so when I was going back to the
airport Friday afternoon, I already saw
I got like the hotel bill and some other
expenses and I basically just forwarded
these to the new expense agent. And when
I get back to work, what is greeted by
is just that then the expense agent
replied me with a nice message that
there is a report ready for me. Uh, and
it has processed some of the expenses
and I can go now go and review that. So
let's just quickly switch into the
expense agent. Right? So this is the new
dedicated web app we made. It's just for
dealing with expenses. Uh and to use
this you actually do not need a BC
license. You don't need to be a user
actually in business central. But you
need to set up as an expense user. And
then you as a submitter you can you can
just go and use this.
But of course I have a few more receipts
I need to get started handling. So I can
just upload these receipts and they will
be uploaded to the expense engine and be
processed. So while that's ongoing, we
can take a look at what the expense
engine already did. Uh and let's just
take a quick look at that. Um so this is
yeah, it's just a taxi receipt. You can
see it's in Danish because the
expensation doesn't really care what
language and the receipt is in. It will
just go and process them. And you can
see we extracted like the amount, the
date of it, the merchant, and we also
categorized it. In this case, it's
ground transportation.
Well, let's see what more it did. Uh,
okay, here's another one. Looks a little
bit funny, but it's just the train
tickets from getting here. And also that
has been processed and and handled. And
then let's take a look at So, this is
actually the hotel bill. A very typical
kind of hotel bill, nothing special. Two
nights stay and some breakfast and so
on. Um, and again, the expensation has
tracked the information and it's
categorized it into a hotel stay. And
because it's a hotel stay, my company
requires me to actually go and itemize
the bill. That's where, you know, you
really start saving time with the
expense agent because, of course, it
just did that and put in all the lines
so you don't have to.
I can also see that the one the two ones
I just uploaded they actually already
was processed. So this is actually the
flight attener from going here and back
to Copenhagen and uh what that is
actually used for is actually the perdm
calculation what your allowance will be
because it extracted the information
where you're going and instead of having
to go and look this information up the
expense agent actually already
calculated these numbers for me so I
don't have to go and do that. So that's
great. And then just one more. Again,
you can of course just use your camera
and snap a thing. It doesn't really
matter on the side. It will also go and
deal with that.
So that actually means this expense
seems to be all good and almost ready to
kind of submit.
But of course, when I look in my back
pocket, what do I find? There's already
always one more expense that I kind of
need to deal with. So, how do I actually
get that into the expense agent?
Um, and for that, it's a good
opportunity to to show you the new
dedicated mobile app. We also working,
we're still working on it for the
expense agent. So, I'd hope it all
works. Um, so here I just started up and
uh to get this new expense in here, I
basically just go here, right? I just
need to hover the phone over it and keep
it still. It will capture the receipt
and I just say okay. And as you can see,
it goes straight into the expense agent.
It's uploading it and we'll be
processing it. And and in this new phone
view with the experience is a little bit
different. Um we basically created a
feed as you know from social media apps.
You can basically just scroll down and
see all the incoming expenses are all
here.
And um you can go in and look at the
details. You can take a look at this
one. I can just kind of zoom in, see all
the information. You can see that again
this was the PDM one we did before. All
the information is right here. I can see
the PDM days and everything. And if I
actually want to say go and edit
anything, I can of course just do that
and go back. But this seems to just
check out. So, I don't want to change
anything on this one. Right.
Oh, now this new one has actually been
processed. And oh, it was going so well,
but actually this turns out to be not
compliant with the different rules and
policies that my company has. So, let's
just go and check. Oh, yeah. It's just a
restaurant bill. And let's see if we can
get any information why. So, actually
down here in the bottom, we kind of show
you why it's not compliant. And this was
just because you were a restaurant rest
bill with a few of my colleagues. So I'm
actually required to add the
participants. So let me just go and do
that. Of course I was there. And let's
just add one of my colleagues as well.
Uh and say okay I'm fine with that for
now. Just hit save. Um
and then of course this will all be
saved. And if we are lucky, the expense
report should come back up as kind of u
compliant again. All right. So that
actually means I'm you know kind of
happy with this. No. All I need to do to
just confirm. Yes, I'm happy. I just
need to slide this. So it's will
actually be added to that expense
report.
So now this whole thing looks good and I
just want to uh actually submit this
expense report for approval. All I need
to do is just go here and hit submit. So
now this expense report will be sent for
approval. Uh and in this case my
approver is uh actually my manager
Reena. And let's take a look at Reena's
mailbox. She also has the expensive uh
agent enabled.
And uh she also gets a mail like this
showing her that what was the expense
report and it's kind of ready for
review. And when she wants to review
this, she's taken to the same uh web
app. She can go here and see there's one
for approval. You can see this all seems
good. I'm sure this guy was doing all of
this and it's all seems compliant. And
she can basically just hit approve. And
then she's also done with all of this.
And of course now all this information
of course uh we build all these
experiences outside of BC to have these
dedicated experiences but all the
information actually ends up going back
into uh business central uh and from
where a finance controller or accountant
can go on and uh actually get the
expense report posted. That was all from
me. Thank you.
>> Thank you very much Michael.
Yeah, personally I cannot wait to have
this experience for my expenses because
it is a lot smoother than the system I'm
using right now. If you want to try this
out, you can actually already try it out
today because it is in public preview,
but you will have to create a US
environment in the admin center and then
you can play with it. You It's also
going to come to more countries very
soon. Already in July, we will release
it to a a bunch of countries including
at least five European countries. And if
you're not among the list in the list,
it will come to your country soon after.
So we are committed to to doing that.
So now we've covered native BC agents,
coile studio agents and agents built
from scratch all facing the users.
Let's switch our attention to the
engineering agents. Engineering agents
that help you write code and do other
software engineering related tasks. They
can live in VS code. They can live on
the command line. They can live in
GitHub in the GitHub cloud. This is
actually the domain in which agents have
come the furthest. The companies, the
model companies, Anthropic, OpenAI etc.
they are investing heavily in this area
more so than in other areas. This is not
something that I think this is not an
intuition. They have actually tested
this. Anthropic, the company behind claw
code, has analyzed the calls, the API
calls that come in to their models and
they've categorized it into the
different domains that they belong in
and the results are quite clear. The top
one is software engineering. So half of
the calls, half of the tool calls
actually are about something related to
software engineering. You also see other
knowledge work domains on the list. You
see um finance I think is on the list uh
with 4%. You also see customer service
with 2.2%. So things are happening in
other areas like I'm a little bit
surprised actually that customer service
is only at 2.2% 2% because customer
service and support in particular is all
often mentioned as an area that AI can
do really well but apparently not
softwareing by far the biggest right and
so this also
tells you that AI agents are changing
the field of software engineering I hear
many colleagues and others say they
don't write code by hand anymore you
heard Luke in At the beginning, same
story. They delegate code, the coding
tasks to the agents.
And this is quite a shift.
There we go.
Wakey wakey.
So models continue to improve as uh
Christian talked about before and as
they do, they become better and better
at generating AL code. So, one of the
things that we've been focusing our
attention on is to give some of the
tools that you use every single day to
the agents.
And to help agents understand how to
work with AL code, not just generate
code, but to actually work with AL code,
we created some tools for it. Um, if we
go here in a project that I've opened,
and we go to the tools sections over
here, let's see if I can figure this
out. We do a new session
and I'm going to see if I can find the
tools.
What happened to my tool?
Somebody help me.
>> Ah, of course. Stress of doing demos,
right? I mean, she Okay, so we gone back
to this. Go to the tools here. We can
see that VS Code already has some tools
built in. So they're already giving us a
lot of tools for our agent chat
experience here to use. I've also
configured this environment with an MCP
server, not poor shots. I'm not working
with data now. I'm working with code. So
I gave it our uh MCP for MSLearn. So it
has the access to the documentation for
writing AL code. So it can fetch
examples and understand how to write AL
code. And of course I have also the AL
language extension which comes with a
set of tools. And these are the tools
that you use every single day building,
debugging, downloading symbols and so
forth. Right? So you can use these tools
directly. Uh we can actually ask the
agent here to say I want to use the AL
uh search simple simple search. So I
want to use this tool uh to find maybe a
record or something like that. But maybe
I want to ask a little more complicated.
uh so I'll say uh use
to find what is related to something in
this solution. This solution is about
assigning item certificates to items. So
is it made of sustainable wood or metal
or whatever uh to item
certificate assignment.
Right? So it it's supposed to now use
the tool to go and find things that are
related to assigning item certificates
and it will use the simple search tool
to do that. Now this was very explicit
and I don't need to be explicit because
we have documented these tools in a way
where the agent can discover them and
figure out which tool is applicable to
what task. So I don't really need to
tell it what tool to use, but I can if I
really want to. So
uh this will be done in a second and
figure out what's related to this uh
item certificate. And if you're
interested in understanding how the
tools are used, you can go over here to
the chat debug pane here and actually
look at some of these things. And it
should say here that it used the AL
symbol search tool. And in here you can
also look at what input was sent to it
uh and what output a tool gave. This can
give you context to why tools may work
or may not work and so forth. So it
should be done here. Um
let's just see if it'll be done in a
second.
Yeah, just going to stop it because I
want to show you something else. As I
said, I don't need to call the tool
directly. I can just call let's say
build if I can spell. So build can mean
many things. We are in an AL project. So
I expect it to know that we need to use
the AL built tool to build. So it should
be building my AL tool or using my AL
tool. Okay, so far so good. Now these
are fairly simple examples. Uh you can
imagine how writing a more complicated
prompt will give you more elaborate
usage of the symbols. Um but there's
also a scenario where you probably
haven't thought about it or using these
tools. That is when you're
troubleshooting.
Like when I go into a project like this
and I need to figure out where to set my
breakpoint.
Guys, think about that. How much time do
you spend on figuring out the right
place to set your breakpoint? Well,
maybe I can just do set a break point
where we validate the
welded if and a certificate is already
assigned
to an item. Well,
this used to be something like you need
to look through the code, maybe debug
and step through it and figure out where
it is. But now I can actually just ask
the agent and it will find the right
place to to put in that breakpoint and
it would use the AL set breakpoint tool
to set that breakpoint. So I can just
press F5 or attach and voila I am right
there where I want to be. Right?
Pretty cool. And there's lots more tools
and you can create skills that will use
these tools in a certain order in a
certain way to make you more productive
in the way you write in write code in VS
Code. Now, not everyone is writing code
in VS Code anymore.
A lot of people are working in other
places.
Some of these places are CLIs.
Everybody loves a good command line
interface, right? Yeah, I do. I'm a fan.
So, we've spent some time on bringing
all these tools to you in uh inside the
the CLI.
And we can look at that
And so we can ask here what tools are
available
right now just here what tools are
available.
So in this session I already
preconfigured uh the environment to have
some tools. It has the built-in tools
like VS code. So there's some CLI
commands and code tools and it also has
the AL MCP tools. Right.
So we can ask it more about that. So how
is the AL
MCP configured?
Show me the MC. What's it called?
MCP.json, right? Perhap
Yeah, there we go. Let's see if it will
do that for me.
So how do I get the tools into my CLI
experience?
It's simple. We just populate the
connection string like push choke in
this scenario here for getting our AL
tools in to uh to the CLI. I will
configure it using a net tool called AL
and it has a launch MCP server
and it will load in the the workspace of
these two projects. Right? So it's kind
of similar to VS Code. You start up
program in this case the MCP server and
you load in the solution. These are the
projects and now I have accessed all
these things as we saw in VS Code and I
can also say build and it should pick up
the tool for building.
One thing we didn't talk about yet is
testing and inside VS Code we have
actually enabled so you can go so you
can call here run the test.
Now, did any of you remember what was in
the tools? I don't know. Let's go check
again. We'll check here. Did you see a
run test tool?
No. Well, because we actually integrated
with VS Code here. You got the test
explorer now and you can run tests there
manually. But that also means that we
can use the existing infrastructure
and find the run tests in the builtin
functionality. So we find it here.
So this is a built-in functionality in
VS Code. There's no run test in the CLI.
Let's talk about what tools does the
ALMCP have. Let's just ask it. Right. So
we brought the specific difference
between VS Code and um the CLI uh into
the CLI. So we have here an a al run
test tool. There are other tools that
only belong in VS code because that's a
UI experience. But here we brought all
the tools that you need in order to do
this in in a CLI. So let's go back to
the tools and talk about this ALMCP
thing. Let's see this guy. How do you
get this?
It's quite easy. It's quite easy. So, we
go back to a browser here. Let's see. We
have one here and we go to a to the
Nougat uh site. You will find the
development tools here.
And you can just copy this line
and paste it into your favorite shell
here.
So we created a new uh packaging for the
tool set. So you don't need to go into
the v6 and figure out where the tools
are there. You can just do the net tool
install and that gives you all the tools
that you need in order to do these um
MCP calls and lots more. In this case
I'm choosing a version that is a beta
version as we can see here. So I'll also
add the pre-release.
This gives me access to all the latest
things that we're working on. sometimes
experiments, sometimes new features, bug
fixes, and so forth.
But when I've done this, I've installed
this, I have access to the the net tool
AL.
And as you can see here, it already has
a lot of tools I can use among others,
the
launch MCP.
And because I did the pre-release thing,
I also got a new tool called launch LSP
server.
So that's new. Think of um the MCP like
the tool chain, the tools it can use,
the hammer and the nail. Uh whereas the
LSP is more the brains, the
understanding of the language of how
symbols act together, the references,
maybe some dependencies and so forth. So
we have different tools for different
tasks and the LSP, the language service
protocol is something that we can use to
understand the language. VS Code uses
the language service protocol to give
you a rich experience inside VS Code,
the hover over and so forth, the go to
definition, you you name it. Um, but for
an agent, it doesn't need all of that UI
richness. It needs a smaller subset. So,
the LSP server that we have here is a
reduced subset designed specifically for
agents. And to kind of show what it can
do without um too much detail, I want to
introduce a new UI.
I could use the the console here, but I
want to use a new UI. So I have here the
GitHub copilot app. This was announced
and built just a few days ago. It is
essentially a CLI, right? It's text
based. It's a chat interface. uh but it
has a lot of niceness to it for the
people who like a UI and it has some
easy access to features like work trees
and you can access the remote um or the
the cloud uh sessions and so forth right
and as we saw in the CLI that was doc uh
we have the configuration of the MCP and
we can also see a scenario here where
I've used the LSP let's go up to the top
of this question here to kind of
understand about who's calling stuff uh
for this certificate assignment thing
and from that the LSP because it knows
the details all the details about
relationships and the symbols that's in
here it can navigate that information
and give me some great overviews here
some good understanding of the direct
callers event publishers event race
subscribers or maybe a nice diagram of
the flow itself
so lots of tools that we've made
available for you to use when you're
chatting with it for agents and skills
to use when they're running autonomy
Honestly, with that, back to you,
Christian.
>> Thank you very much, Deon.
So, these are some really nice tools and
you can use those tools, give them to
your agent. We are adding more tools.
How many do we have now? 10 or so. We'll
be adding more tools. You can give your
agents instructions in the form of
skills or agent definitions. So, you
might be wondering, how do we know we
think making things better? If we add
more tools, are we making things better?
If we give them more instructions, is it
getting better? It can actually be
counterproductive to give your agent too
much information. So, what we've also
done is
go, you know, systematically here look
at how can we make sure we improving the
situation versus actually degrading it
in the with good intentions. We'd like
to show you uh how we've done this and
uh that will be Arur who is uh going to
show that. Please welcome a
um a great question Christian. So we
have um a lot of tools and new models
comes out basically every single day. So
we need to figure out um uh we need to
figure out how to validate how to make
sure and we also build our own tools.
You saw them. We need to know the
direction. So what would be the next
tool for us and for that we introduced
the BCbench
still not here. Yeah we introduced the
BCbench. It is the business central
evaluation framework for coding agents.
We got the inspiration from this we
bench evaluation framework for popular
programming languages such as C and then
the Python. But we have our own
programming language L and we have our
own tools. And what is also very
important for eleation frameworks, we
have our own data sets. We have the
commits made by real engineers for a
very long time in different domains,
finance, SCMs, different first party
apps. So we take this data set and we
run the experimentation loop. Um so that
with that experimentation loop we take
one variable in the time with that be
model, the MCP and then instruction. We
run the BCB bench and then we get the
number basically how many bugs the
business central coding agent can fix or
how many tests can it implement.
We in the beginning of our journey we
identified the baseline. We took the
harness GitHub copilot. We took the
whatever was the frontier model uh back
in days. No specialized agents, no
instructions, no tools. We run the BC
bench and we get the number and from
that number we started the journey
applying the hill climbing strategy.
When you pick one variable at a time,
you measure it and you decide if the
accuracy goes up, you keep it. If not,
you revert it. So from the baseline, we
u test it on the new model. Great, the
accuracy goes up, we keep it. Then the
new tool that Stefan presented, we test
it on the new tool. Great. Accuracy goes
up. We keep it. Then we decided let's go
with a specialized agent. Let's add some
instructions. And now there's a true
story. We've been working on internal
agent test agent for writing tests. And
our assumption was okay, let's just take
all the instructions that we have about
the coding guidelines, test structure,
good patterns. Let's just throw all the
way to the instruction should be better,
right? More context is better. We ran it
in BCbench and the result was actually
opposite. It was 5% worse. And then we
realized the more context is not always
better. So we shorten our instruction,
make them more precise. Then by keeping
the same model and then the same tool
from the previous run, we add a short
instruction and the accuracy eventually
goes up. Great.
Where you can read more about the
Cbench. It is a public repo on the
GitHub. So you can uh read more about
how does it work? Uh what is inside? On
the right side, you can find the link to
the leaderboard where you can see all
the numbers. Um and here's how you can
read and understand those numbers. So
let's say a test generation how we how
good we are at generating tests. Um we
ran on the different models. There is no
special instructions no agents uh or the
tools in the baseline only the harness
and the model and we rank all the
results uh by the models on top and we
can see that the clous 4.5 performed on
u 55% and then right after that goes uh
4.6 six um and then so on and so on. Um
so then we want we decided okay let's
just pick the model for example clopus
4.6 six we have 51.7
uh great and let's take a look let's
apply the instructions on top of it
would that better or not and then that
was exactly referring to the story with
LTS agent we applied our shortened
instruction and it was 10% better great
now we have a specialized agent with
that model um so we can move forward so
that's how we evaluate and BCbench is an
um open source project so you can take
it asation to evalate your own agents,
skills and tools. Back to you Christian.
>> Yeah. So what
so getting started with the engineering
at its core is actually quite simple.
You saw the tools that Stephan presented
and it is all about configuring a few
MCP servers. the AL MCP server. You can
also have the Microsoft learn MCP server
and you can have an MCP server that
connects to your GitHub account or your
as a DevOps account so that it can work
with issues and work items and then you
can also give it instructions as
explained like if you give it some
instructions it can become better and do
things more like you like it. You can
make agents, you can add skills. We also
have the BC quality initiative where we
have a repo that has kind of these in a
shared place so that you can just use
them uh without having to reinvent the
wheel.
So uh so that's that's you can learn
more about this in other sessions but
actually now that I still have you here
on stage our tour would you mind showing
us how you do work you take us behind
the scenes how do you actually apply
these tools in your daily life? Yeah,
sure. Let's let's see it, Christian. So,
um I do a lot of things at my work and
uh the bug fixing is uh one of the
important ones and uh I have a GitHub
repo with a couple of issues, but I'm
not going to fix it by myself. Uh I want
agent to do this. And for that, I set up
this repo for agentic engineering just
like Stefan presented. I have the MCPJ
JSON with LMCP server to compile,
publish, and then run tests. under
GitHub folder I have the LSPGSON
language sort of protocol for the smart
uh u
searching the codebase and then I have a
variety of different skills I'm not
going to go into details how they work
there will be plenty Microsoft session I
hope the partners one how does it work
under the hood and how you can build it
I just want to run it uh in action um so
for that I prefer to start from the
terminal and to trigger my workflow I
want to run the following process start
and L the session. This is the one that
I basically run in every single new
session. And uh that phrase will trigger
the skill setting up my dev session. Um
it will do several things. First of all,
it will take GitHub issues assigned to
me and present this to me to actually
pick one of them. So I see the picker.
Great. Let's take let's work on this one
for example. I choose this one that will
create a git branch pulling the uh
latest from main u setting up this
branch and then moving forward. Okay,
from the GitHub issue there's some
description what is all about that scale
goes through all the L projects that I
have and try to identify which are
relevant for this GitHub issue. There
are four projects in my repo when a
engine matches this to the description
of issue and says okay the first two
projects for certificate management are
relevant and the latter two is not great
so I choose those two projects why is
important because I want to set up the
whole context around those two projects
and I want to make sure the compilation
and publish works for those two projects
resolved in local environments minus is
working that's great then the subskll a
very small one for the LSP making sure
that uh LSP contains both projects.
Great. So it's setting up the LSP
testing it works fine. Uh writing all
the necessary configs that's great. Then
setting up L tools in order to make it
work. Um
it needs to call the uh project tool
adding both app and the test projects.
That's great. And let's just give it a
second for the summary. Great. I'm up
and running. I have my branch uh I have
my projects nst I'm ready to go now I
need to fix the bug actually do the
thing I can let the general agent do
this then in most of the cases that
should be fine but I want to go it in a
very specific way I want to go to the
through the planning mode and then I
want to do the test-driven development I
want to let agent implement the test
first make it red and then implement the
fix and this is kind of a workflow and
what is the best way for the workflow
it's of ers have a skill for this and I
can trigger the skill with running let's
plan and fix the bug. It's immediately
load the skill and then it will read
everything that I have in the GitHub
issue description rapper steps the
comments everything that is uh important
and then it will go to the assessment
phase trying to identify whether there's
enough information whether the reper
steps are clear description and then it
will get me to the planning mode where
uh agent either saying yeah it's fine
everything is missing or it's just
enough you see language server protoc
call is running here because I have it
up and running. It starts to reading um
the object and actually found the bug or
at least have a theory around the bug.
Um so it's
the com the investigation is completed
at this moment and then I basically have
my plan ready. So let's give it a second
to go until the end.
Yep. Great. So let's see what we have
here. A root cause analysis. So what
kind of problem agent was able to detect
the proposed fixed and the affected
files? What needs to be changed?
Acceptance criteria. Great. So I can
review the file. I can um make some
changes and then push the agent forward.
But uh I think I'm running out of time.
So I want to do the following. I'm not
going to confirm it right now. I want to
run the remote comment. I want to do the
following. I want to set up the dev
tunnel between my local environment and
the cloud environment.
So now I'm moving from my environment, I
won't have an access to that one to the
cloud and I cannot just see what is
happening on my local environment, but I
can also interact. So I can say I
confirm the plan and it will go forward
and I will be able to see it without the
environment. And it looks like I won't
be able to access my laptop because I'm
I'm running out of time. But I have
GitHub Copilot app on my phone. So I can
steer the agent to the right direction
and uh wait for the pull request.
>> Amazing. Thank you Ash.
>> So you see how we are making it possible
to use agents with AL. We're making Al a
first class citizen uh in the world of
aensic engineering in VS Code and CLI
and the tools are kind of plug and play
as Stephan also showed he can plug it
into the new GitHub app as well and you
can use it from cloud code etc. So if
you paid attention to what Arto did at
the very end he ran the remote on
command and that created a connection to
github.com.
Basically, his agent was still running
on his machine, but he could now remote
control it from the cloud or from his
phone.
What we're also exploring is GitHub
uh actually running the agent like the
agent would no longer run on the
machine. It would run in a container in
the cloud. This is just not an approach
that we have uh really done used yet
internally but we are exploring it and
I'd like to show you how how our vision
uh looks for that.
So at the core of it is GitHub and if
you use Algo for GitHub it will come
prepackaged with many of these tools.
This is our vision. We don't have it. We
have a signal agent. It is monitoring uh
signals out there. for example from BC
ideas if there's an idea a new idea it
can pick it up evaluate it and send it
to the triage agent not all ideas are
good right so the triage agent will
evaluate it look at you know are there
similar issues or ideas uh kind of see
is it a good idea what would it take to
do then the planning agent will assuming
it's a good idea the planning agent will
make a plan for addressing this if it's
a bug then have a plan for the bug fix
as R2 also showed the development agent
will actually implement it and once the
implementation is done a review agent
will review the code like in an
objective observer and saying that's
good and that's bad and you can also
imagine that an agent will actually
release it to a sandbox environment or
even to production right this is a
vision in all of this there will be
human in the loop like agents are not
mature enough that they can evaluate and
they have all the context. It still
takes a human to make a decision in the
at the end whether the architecture is
right, whether it's a good idea and we
should prioritize it over other things
etc etc. So this is where the role as
software engineer is going as we see it
they are kind of running these agents
and that's their new role. I want to
show you uh
how it might look. This is a
this is a u a board in GitHub and you
have a column for each uh agent. So you
have a signal agent, the triage agent,
planning agent, implementation agent and
more agents. And so here we can see we
have a um a an issue. It's a it's a bug.
It's a performance bug. And uh the
signal has picked it up from somewhere
maybe from our telemetry.
And so what I can say is as a human I
can say hey I'm gonna actually assign
that to the triage agent.
And this is going to kick the off the
triage agent to do the work and analyze
it compared to you know other other
things that it might that might be in
this area. And when it's done, it will
signal to me it's ready. And so I can go
and and look at what it wrote.
I scroll down. You see the triage agent
has provided its analysis.
And uh yeah, in this case it's it's it
needs more work. This is not a sure
thing. So this is where again the human
judgment needs to come in and you know
is this really something we want to
address or is it like by design? in this
case maybe but what I can do in this
case is also I can say you know whatever
I'm not going to write something here
but I can write instructions to the
triage agent to to go and look in
another direction that I may know about
and then when it comes back I can of
course drag it to the planning agent and
it will develop an implementation plan
for it etc etc this is how it might look
maybe next year we will we will be able
to to show this uh to you in in real
life.
So with all of these investments, you
can ask the questions a valid question.
Are we getting anything out of it? What
are the results?
We have investing in the tools as an
development organization ourselves. We
are adopting the tools and adopting the
practices. What benefits do we get?
So we have a lot of qualitative results
like we think we are becoming more
innovative because of this. We don't
hesitate to create an experiment because
experiments are cheap now. So we
experiment experiment experiment and
what we do what happens when you create
an experiment now is you get something
that looks very finished. So you
actually are able to evaluate whether
this is a good idea. How will this be if
we go that path? And so that leads to
better product decisions. So we we
generally feel we go in the right
direction.
Documentation is agents are really good
at writing documentation. So we are able
to keep up with documentation and close
the gaps that we had. Same with tests.
Uh more tests, better tests, more higher
quality. And in terms of productivity,
there's also this feeling that we have
where we are becoming more productive
overall. But this is just a sense that
we have. It would be nice to put some
numbers on this, but numbers are really
hard here. How do you objectively
measure quality and productivity? It's
really, really hard. We have one number
we would like to share with you. That is
the number of completed pull requests in
our main branches. And there you see a
significant jump of 50% in January.
This is the around the time when we
systematically started to use a genensic
engineering. So you can definitely see
an increase in the number of pull
requests.
You have to take this with a grain of
salt. It might be that the pull requests
are smaller, so we're just checking in
smaller things. It might be that they
contain a lot of bugs and the quality is
going down. We don't know. But we can
see something happened and combined with
the qualitative results or the what we
are seeing what we sensing I think
personally that we are have become a lot
more productive as an organization and I
think this is just the beginning. I hope
next year we can say we are 100% or 200%
more productive than we are today.
This concludes the main section of the
keynote and now we're going to switch to
a familiar section which is from the
lab. And from the lab is where we show
you some experiments that we're doing
back home. Experiments that may never
lead to anything. They may never
materialize in product that you can use
or customers can use. But of course we
hope they will be like we don't do it
for fun either.
We have a hope that this might lead to
something, but there's no guarantees.
And I'd like to have Espen show you the
few demos on what we're doing. Please
welcome Es.
>> Thank you, Christian. Can you advance?
>> I'll do it. Uh, we have already talked a
lot about tools for developers to change
PC,
but what about end users? Imagine for a
moment that end users could just
describe what they want to change and BC
would adapt, hide something, remove
something that you do not use, add
something that is important to you or
create even create something new.
So let's take a look at how that could
look like if you for a moment imagine
how that could look like.
Maybe it would look something like this
at least something with uh the product
and a chat on the side.
I have already asked a few questions
here.
I mean what page am I on? It knows
apparently I'm on this auto processor
role center page. What apps are
installed? These are the apps which are
installed on my tenant.
What if I they are in the headline I
don't use it. It takes up space. Let's
just remove headline.
And now it starts working on it. It
knows where I am. It knows my tenant.
It's
considered what I'm what is the user
asking for? What is the headline?
And hopefully the AI is warming up now a
little bit. Um
and
it should yeah now it figured out that
there's a headline control. It looks at
the page. Again we have talked about the
tools. These are some of the same tools
that we have already shared in the ALMCP
server inside our AL extension.
And
this one failed.
That's strange.
But again this is a prototype. So let's
try to do it manually.
No
try connecting again. This is talking to
a service inside here.
All right.
And now I have to talk a little bit more
than I expected because something went
wrong. But again, it's now trying to do
the same. It's analyzing what I asked
for. It's looking at the context and
hopefully this time it's connected
probably and are able to remove the
headline for me.
>> So it's not quite ready for customers
yet.
But again it's doing the same. It's
finding out how the pages look looking
and publishing is
well this kills the demo a little bit.
Um
let's
Let's continue with the next part and
see if we can get this one running
after.
This is really boring.
>> Okay. But maybe we can just also just
talk about what it what what would you
what you would have seen if it worked.
>> I can run the video.
>> Uhhuh.
>> I also I'm also prepared.
So, let's run the video instead.
It's the same you're seeing now. I'm
here. I'm actually asking the question,
what are apps are installed? And this is
a tool that plugs into the server and
knows that I have these installed. And
let's try to hide the headline. And this
time I'm actually trying to use
end user friendly wording remove the
headline because an end user would not
necessarily mean whether we are hiding
it or removing it.
And it's now again this time on video
doing all the work and it's publishing
and I since this is a prototype early
stages I need to do the manual refresh
but as you notice the headline
disappeared.
So what if I want to add something new?
For instance, I want to add a new tile
that is showing all sales orders above
100,000. All open all open sales order
orders above 100,000 because they are
important to me. I want to name it high
value orders.
I actually don't know myself how to
create a new tile, but apparently the
agent is way better at it than I am
because
things a bit searching for symbols
probably in a moment.
Looking at page layouts,
looking at relations,
searching more symbols even more.
And at some point it will write some
code. Yes, it figured out that the sales
order processor activities, that's the
part we're seeing up here. That's the
one that's going to be changed. Finding
a bunch of ids which are not already
used
writing the files, compiling, and it
fails. It's running an in-memory
compiler. So, it get fast feedback
and figure out what to correct.
Apparently, there was an ID problem.
And soon I think we will see a
successful compile. Yes. And now it has
actually created a new tile. It's
publishing.
It's way better than live.
And as you see, we got a new high value
orders up there. Not really where I
wanted it, but again, I'd never told it
where I wanted it to be. So what I did
instead is move it. I it's a
conversation so I can just tell it move
it to the existing activities p group
rather than creating a new one.
And again figures out what I want it to
do.
And I'm not sure why it wants some new
IDs, but that's fine.
Cleaning up. Compiling again. Now I will
publish it.
And hopefully it's now placed in the
right spot.
Just a second.
And this time I know it will succeed
because it's a video which is a good
thing. Remember that. Always bring a
video
and a manual refresh.
And that's good. Now I have actually
successfully added my high value orders
up there. But what if I wanted to create
something completely new?
For instance, I would like to have an
Excel report showing me those high value
orders.
It actually by the way also added a
drill down for me while at it which is
nice. But I would actually like a a new
Excel report showing exactly those high
value orders. So I just ask for it.
Create an Excel report showing the high
value orders.
Start thinking finding a template for
it. looking at some samples. All this
all the tools once again they are good
at this
and hopefully
should have the report ready. Yes,
deploy it
and let's find it.
I forgot to refresh.
There you go.
And
now it's there.
As you can see, nice layout matching our
other new Excel reports
and
three sales orders about 100,000 found
in the report as well.
This is a prototype obviously. Um it
even didn't even manage to survive the
keynote but we are looking at this and
it's very promising.
>> So so okay so what I like about this is
a couple of things. one is we've seen so
you have to imagine this is the real
chat window this is not copilot CLI or
anything even if it looks slightly like
it you have to imagine it is inside the
main experience being the chat function
that end users can interact with and
what I like about this is two things one
is the tools that Stephan showed you
that can be plugged into VS code into
GitHub CLI into others it can also be
plugged into a coding agent that runs
inside of Business Central that you've
made because what is a coding agent at
It's a hard well it's a a identic loop
with the right tools and with the right
instructions then it can actually write
code and that's what we're seeing here.
The second thing I like about this is
the scenario because imagine we can get
this right. It's not trivial with the
kind of security and other aspects in
mind. If we can get this right business
center becomes so much more powerful and
our end users can do so much more. So
it's it's a really strong value
proposition. But I mean I think it's it
was a little bit slow. So like I mean
you you give it a command, you have to
sit and wait 20 seconds, right? I I
noticed in particular the deployment
step was uh pretty slow. Can we do
something about that?
Yes, we have actually thought a little
bit about that as well. Um
and in order to be successful in uh
being 100% ready for a genetic
engineering, we need speed. Agents love
speed. We developers love speed. So we
need to get fast feedback when we make
changes.
We have
we normally talk about two nested
feedback cycles during development.
There's a fast inner loop close to the
code and a slower outer loop that
surrounds it with collaboration,
validation,
and delivery.
Here I will talk about the inner loop
but what we're talking about here will
also affect the outer loop.
This loop we are seeing here is the fast
iteration. I as a developer make a
change the compiler tells me I'm missing
a semicolon or something. I go back
change it. This is normally very fast.
We also made this loop fast inner loop
available available to agents through
the ALMP, the ALSP
and and they get the same fast feedback
and that matters because languages which
have a fast feedback loop tends to share
their ability or agents that works well
with languages
that have a fast feedback loop.
But a successful compile is not the same
as proving that the change is correct.
So we need a little bit more.
We need something like this where we
also deploy it and we run it. And that
was also what we saw before. We need to
deploy.
And this is where the cost start to
stack up. And it does that because we do
a lot more when we deploy. And most of
you are probably aware that we when we
deploy we generate some C# code we need
to compile it and in the cloud we even
have to sign it
and that is time consuming.
So
the question became could we make this
faster? What we could do what could we
do to actually optimize this and get a
tighter loop here?
And the idea we came up with is not
exactly new. I mean mean most of you
probably remember seaside and fop files.
And before you get too excited, stop
yourself. We're not bringing it back.
But we did look at the past in order to
try to help us shaping the future. So
instead of emitting C sharp, the backend
compiles,
the backend compiler could emit AL
specific byte code a little bit like we
used to do. And that bite code would end
up running in an AL virtual machine.
And since byte code is a portable
instruction format and the VM is the
engine that runs it on any machine, that
sounds that sounds nice. And in old
terminology it would be the fob file
containing bite code and then cite
executed it. So let me give you an idea
of the difference. If we take this
picture again
we have these steps here.
And if we change that instead we will
have a single emit bite code step.
and the bite code step. Not only are we
reducing the number of steps because
we're pulling out two, but it also turns
out that emitting bite code is a faster
operation for us than emitting C#
because we it's it's more lean creating
C# is huge trees we we are emitting.
So let's
jump to my machine over here and show
you what that would look like.
This is probably close to the world's
smallest uh AL code unit and it's fairly
boring.
But when we generate C# from this, it
actually becomes
all this
lots of line lots of code has to be
compiled and that's also take time.
If we instead created by code,
we would get something like this
small binary format. This is actually I
think 27
bytes to represent the same piece of
code.
And it's binary and that's also why I'm
showing hex code here. But if we
disassemble it,
it looks a little bit like this. It has
no globals. It has no triggers. So we
could see that there's no strings there.
And then there's some instructions down
here. And these are actually the six
instructions that makes up this small
method.
It turns out
that deployment of bite code in this
prototype is around 40% faster at least
with with the test suite we have been
testing on.
is now there near complete. But that's
interesting. That's a lot of speed.
But I mean maybe we could even go a
little bit further than that because
maybe the fastest deployment is actually
not deploying keeping this loop inside
VS code.
So if we instead uses a local test
runner that executes bite code, we will
be able to inside VS code in a tight
loop do a compiler where we emit the
bite code already client side and then
have a test runner that has a mock
server
and a in-memory database.
Of course, this is not a full a full
server, but it would allow all logic all
logic to be tested.
So, let me switch again back to machine
here. I have out here
two test suites. I have one with
some computational workloads. And I have
another one over here with
a bunch of other tests and almost 800
tests in total.
And you already saw Stephan showing the
test runner. Here I have added another
one, another run type called run unit
test runtime. And that one is producing
bite code and running it locally.
And that doing the same deployment to a
local server
took takes around 40 seconds running the
same tests. Here it took nine including
a deployment I think or generating the
bite code. There's a couple of failures
because this is not ready. I mean
there's this is methods in our stock
library. it's doesn't know about yet,
but it shows that we are able to do very
fast and lean test run that will take be
able to test at least a subset of tests.
Very cool. Thank you very much.
I think these are really really exciting
things and I hope they will come to you
know materializes product one day.
A couple of calls to action. So what I
think you should do now is go and create
your first agents in Business Central.
What Stephan showed it's very easy. You
just click that little avatar and you
are started in any sandbox environment.
Use the MCP servers from VS from Visual
sorry Copilot Studio or from VS Code.
Either or. It's very very simple to get
started and you get a feel for what you
can use this for. And if there's one
thing I want you to take away from this
keynote is aentic engineering is not
optional. It's something you must do
otherwise you'll be behind. So please do
that. So clearly this keynote has been
about AI agents but just know that we
are of course also doing all the other
boring stuff not boring stuff I'm
kidding application functionality with
uh sustainability analytics with reports
administrative features performance with
index management service reliability you
don't see that but we are improving
reliability on our side same with
security usability you do see right
because we're making some improvements
in the UI. So, a bunch of things.
I also want to share a few numbers with
you. Last year at this keynote, we
announced that we have 45,000 customers
running in Business Central online.
That number today has grown to 55,000
which is I think is an amazing growth.
But that is not even the full story
because those 10,000 customers that we
got in the last year are generally much
bigger than the customers we had before.
It is now absolutely normal that
customers come to Business Central
online with hundreds of users sometime
sometimes thousands of users. So what's
hiding behind these numbers is a much
more uh amazing growth in our product
and our business. So this is this is
really great. is not due to Microsoft.
It is due to all of you, our partner
community really helping grow this this
business.
If you want to know more about what the
things you saw today, you are in luck
because there are deep dive sessions on
all of it on the product agents on the
engineering agents and on on the
engineering agents in particular. We
have presentations from Microsoft and
also from partners and in many cases our
partners are further ahead than we are
and I really really encourage you to go
and watch those sessions and learn and
absorb all the knowledge you can there.
I also want to invite you to come to our
booth in the expo area. We will be there
in all the breaks. There's 30 of us as
Luke said and we are there to uh talk to
you, come with a question, come with
feedback, come with a story, just come
and hang out. We would love to talk to
you. And with that, I just want to say
thank you. Thank you for coming to this
keynote. Thank you for coming to BC Tech
Days. Thank you for being part of this
community. And also just remember who
you are. Go and shape your engineering
future. Uh, and that's the last I'm
gonna say, but I promised Waldo one
minute at the end. So, uh, have him come
here. But thank you from my side.
Yeah, I I need my one minute of fame as
well. So, thank you for that, Christian.
Um, I'm here in name of the MVP
community. Um and a few uh weeks ago we
had the opportunity to pre-watch uh
let's say the movie on another
conference directions Asia and with the
movie I mean I I'm I'm sure you you know
which movie I mean the one in the
restrooms where there was an Stefan
Kenobi basically whispering that we do
have a future right um for that I think
uh yes can you please join me
um that the lead actor deserves an
award. So I contacted the Oscars.
>> An Oscar?
>> Well, they were not interested. So you
were not that good.
Uh so but we created our own award. So I
mean Busy Take Days, it's a movie
theater. We could have done this uh
privately, but I mean if you can do it
for,200 people, why do it privately?
Yeah, I I imagine. So we created a BC
Take Days movie award nicknamed the
Yesper.
So congratulations. You are the first
and probably the last winner
the movie award. Thank you so much. And
in the name of the the MVPs uh enjoy
take days and come to my session at 2:00
uh in room 5 for telemetry.
