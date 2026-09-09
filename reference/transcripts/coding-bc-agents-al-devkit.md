# Transcript — What is new: Coding Business Central agents with AI development toolkit

- **Source:** https://youtu.be/EwN3xb2q7vE
- **Channel:** Microsoft Dynamics 365 Business Central (official) — 15:53, published 2026-02-27
- **Ingested:** 2026-07-06 (auto-captions, cleaned; artefacts: [snorts]=filler, "enom"=enum, "compilot"=Copilot, "RO"=role-centre)
- **Distilled into:** `reference/AL-REFERENCE.md` §28–29

---

[music]
Hello everyone. Uh welcome to this
session about coding agents in AL. Today
we will see how we can use the APIs
provided in Business Central to code our
own agents
for to get a quick start and uh jump
right into it. You can get the latest
version of the VS Code extension uh and
use the new project command to access
our templates. There you will find a new
template called agent where you will get
both samples of the code that will be
shown and uh an almost ready agent that
you can publish to and see directly in
the UI.
You will also get a very nice read that
you can go through to figure out all the
different parts of designing an agent
and uh setting up different
functionalities that are offered by
business central. [snorts]
The first step to designing an agent is
defining the agent type. Uh the agent
type uh you can think of it as a
blueprint for the agent that defines a
lot of things like the default settings
and the identity of your agent. It
consists of the following parts. First
of all, we have a new enom value that
you have to add to the agent metadata
provider enum via an extension. This
will be what the main identifier of your
agent. Then you will need to also set up
a new copilot capability via another
enom extension which will act as a
feature switch so that users can turn
the feature on and off. And finally you
will need to provide implementations for
the agent interfaces which defines a lot
of different things that we will see
very soon. [snorts]
Here is an example of the metadata
provider. uh you can see that uh it has
a value, it has a name and then it has
an implementation for the different uh
interfaces that need to be implemented
for an agent to work. [snorts] This is
the starting point where you tie your
implementation with your agent.
Here you can also see an extension for
the copilot capability. You just need
the unique name and the unique caption
so that your users can figure out what
uh corresponds to your specific feature.
Jumping on to the interfaces themselves,
they are what basically defines the
default settings and the behavior of
your agent. The first one is the agent
factory interface which defines the
default settings. These include things
like uh the first time setup page. Uh
this is what will come up when your
users first try to create an agent. Uh
then this is also the place where the
compilot capability is bound to your
agent and a few other settings like what
is the default profile that your agents
will be using and what are the default
permissions.
Then we have the metadata uh interface
which defines the runtime behavior of
agents. Some uh settings that can change
during the lifetime of an agent. These
are things like what summary page is
shown. Uh you can here you can also
override the message review page to show
something different. You can change what
initials will appear for your agent and
a few other things.
Finally, we have the task execution
interface, which is the interface that
controls uh things that happen uh when
messages are processed like for example
validation for input and output messages
that you can add through AL and uh what
suggestions are shown when the agent
will ask your user for assistance and uh
the user can click on to proceed and
finally uh settings that uh are context
specific like what lang language should
be used on a specific page for example
based on the customer formatting and so
on.
[snorts]
Going into the message validation
itself. Some things that you can do with
uh this API is that you can for example
implement relevance checks before
accepting an input message for further
processing so that you can discard for
example uh unrelated uh messages. You
can add warnings on input messages in
case that you want to uh point your
users's attention to the to them. And
finally, you can also modify output
messages to add signatures. For example,
if you want to add an email signature.
Here you can see an example of the
implementation of this uh um interface.
On the first one, you can see that there
is code to uh choose based on the type
of the message and either postprocess
output messages or validate them. You
can see that we can add suggestions in
the uh user intervention suggestions.
And finally, you can see that I can uh
add an if based on the page ID and
change the currency for example that the
our agent is supposed to use.
[snorts] Let's jump into another topic
which is very important when designing
agents. Agent types versus instances. So
okay you have defined the type for your
agent but now it's time to uh actually
make an agent that does something. So in
business central agents are modeled via
instances which are also users in
business central.
Uh you have a type of an agent but then
you have multiple instances of this type
which need to be created. These
instances keep their own versions of the
permissions of the profile, the user
settings and the instructions.
Uh you can also notice in the previous
interfaces that we showed that there is
an agent user ID as part of the u method
uh signatures. So you can uh define
these interfaces to behave differently
based on the instance that they are
targeting.
But where do I create an agent? So our
stop to do that is the setup page. Um on
top of the RO sender you will see uh
icons that allow you to create agents if
you so allow. Uh if you click on them
you will get a setup page uh where you
will be able to create new agents and
you will be the one defining the setup
page for uh custom agents. When an agent
is already created the setup page will
also be used for its configuration.
[snorts] What is the setup page? The
setup page is a normal page in business
central except we have a new type the
configuration dialogue which is
specifically designed for making agent
setup pages. Uh it has a few parts. The
first part is the agent setup part which
is a standard component that gives you
some basic uh information about the
agent like uh its name, a toggle to turn
it on and off and a few other things.
Then you add your own functionality in
case you want to add custom settings for
your agent.
[snorts]
Here you can see an example of the setup
page. On the left you can see the setup
part which is the uh standard component
and then on the right you can see things
that were added extra. Notice here that
uh the left part also contains things
like uh disclaimers about AI usage which
are important to add when you are
designing an AI feature.
What do I need to design a setup page
and to make it work? The first thing is
that you will need to make your own
table to track your own instances. It
needs to be a table that has the user
security ID as the primary key which is
also what is used for agents and then uh
it should also hold your custom settings
for your agent and then you can use the
agent setup code unit to make instances
of the agent and track them inside this
uh table. The code for the page is also
uh it goes along those lines. One of the
very important concepts in its design is
that it's supposed to work with a
temporary table. So that means that you
should only save your changes when the
user clicks okay and accepts.
And uh on the right you can see a little
bit about how it works. You can also
find these things in the template. The
the main part is that the setup part the
standard component gives you access to a
setup buffer uh record that you can use
to track some of the basic
characteristics of an agent like its ID,
if it's active and so on and you set
this to make changes
and then you also make changes to your
own uh table when the user clicks okay.
The agent setup code unit allows you to
uh basically automatically create an
agent when you save changes on it.
Finally, you also need to set
instructions on it in order for the
agent to have some instructions.
Another alternative for creating agents
is to create them programmatically. So
you can also tie agent creation to uh
for example clicking an action or some a
workflow. This need to be in a user
session but otherwise it is possible to
create agents dynamically and you will
do that through the agent code unit.
Another thing that is offered is quite a
lot of functions on the agent code unit
that can be used to uh manage your
agent. You can set its display name, its
profile and a bunch of other settings
through the agent code unit. This is the
main place to look at if you are making
changes dynamically to the configuration
of your agent. [snorts]
Instructions are also very important.
They can be loaded at any time during
the lifetime of the agent. But for most
agents, the most common pattern is to
load them during the creation of the
agent and you can get them from a
resource uh so that you can have a nice
place to store them and display them.
Another feature that is supported is KPI
pages for your agents. When a user
hovers over your uh agent's avatar, they
will be able to see uh important metrics
about the agent. So here you can see an
example. This is very similar to the
setup page except you can use any
cardboard part page and you can add
there metrics which are important for
your agent.
Now okay, I've created my agent, I've
created my instances. I need to assign
work to it so that it's useful.
uh you can do that through the tasks
part of the API which allows you to
automate task creation for the agent
instances. There is a a set of code
units that you can use. The most
important ones are the agent task and
the builder uh code units. They allow
you to build both tasks and messages.
Let's talk about tasks versus messages.
For tasks, you can imagine them as units
of work for the agent. They are bound to
a specific agent instance. They have a
title and they are triggered when the
agent should start processing. Messages
are instead bound to a task. You add
input messages to a task to give extra
context to the agent except its
instructions. For example, its
instructions might be to process
invoices and the message might be which
invoice to process.
Uh the agent then creates output
messages to respond to your user.
Multi-turn interactions are also
supported because you can insert
multiple input messages and the agent
might answer multiple times if it if it
gets a new input message.
Okay, so how do I create my first task?
The task basically requires you to get
your agent instance uh possibly from
your setup table and then use the task
builder code unit in order to create the
task.
You create a message for your task and
you populate the task builder. You call
create and then you get a task for your
agent that is waiting for approval from
the user and will execute when they do
that. Another thing that is supported is
the ability to add attachments to your
messages.
Attachments can be for example PDF
documents that will be analyzed by the
agent and uh the text will be extracted.
You do that very similarly through the
message builder code unit. So from the
task builder before you create it you
can get the message builder and insert
different attachments into it through
the provided uh method add attachment
and then when you create the task these
attachments will be included.
Another thing that is supported is as
mentioned is multi-turn agents where you
can continue a discussion with an agent.
So when it finishes and sends an output
message, for example, you can uh send a
new input message to continue the
discussion. This can be to simulate uh
an email thread or some other continuous
uh uh discussion. [snorts]
Uh there is the external ID uh field on
messages and the corresponding method
which allows you to tie messages to
concepts like an email thread so that
you can find them and continue them.
So how do I trigger tasks uh after I
have created the code for it? All you
need to do is to embed it inside the
business central either as part of an
action or as part of a process through
events or in many different ways that
you can try through the through coding
in AL. Here we have an example where we
are doing this as part of a page
extension and we are adding a new action
to the sales order list. Again, like
with agents, you can also manage tasks
through the agent task code unit, which
allows you to, for example, stop tasks
or restart them, and a few other things.
There are a few different ways to uh get
the result of a task. One of them is to
wait for the task via polling
and um you can do that through the uh
agent task res record.
uh through the record you have the
status field which you can use to see in
what kind of state the task is in if it
is for example completed or stopped by
the system because something occurred
and then you can continue and uh query
into business central to get its result.
This is good for unit testing or these
kinds of uh nonproduction ready uh
scenarios. The other thing you can do is
you can create events that will only
fire if the session is um is an agent
session. This way you can uh have code
be triggered after the agent for example
does an action in the UI. The agent
session code unit provides you the is
agent session uh procedure which lets
you uh do exactly this. You can also use
the user ID if you want to uh add events
only for specific instances.
The final topic uh that we will talk
about today is about exposing your agent
to other apps. [snorts]
By default, the AL API only supports
interacting with agents defined in your
own app. This is for security reasons so
that different agents don't interfere
with each other. But it is possible to
also expose your agents to other apps by
creating an API for your app. So what
you need to do is that you need inside
your app to create public functions that
uh other apps can call. Like for
example, you can see the deactivate
function which by default would be
blocked. But because we are exposing it
as um public method on our code unit my
agent public API, it can be called by
other apps. So this way you can expose
everything inside your app to to be used
by external um consumers.
You can find everything that was
discussed today in our documentation
about coding agents in AL.
Thank you very much for your time and
have fun coding agents in AL.