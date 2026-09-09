# Transcript — Introducing: Envision, design and code Business Central agents

- **Source:** https://youtu.be/jWqjDTbqjeE
- **Channel:** Microsoft Dynamics 365 Business Central (official) — 18:34, published 2026-02-27
- **Ingested:** 2026-07-06 (auto-captions, cleaned; artefacts: [snorts]=filler, "enom"=enum, "compilot"=Copilot, "RO"=role-centre)
- **Distilled into:** `reference/AL-REFERENCE.md` §28–29

---

[music]
Hello everyone and welcome [music] to
this topic where we're going to discuss
how to design agents in business
central. Generative AI entered our world
disruptively changing pretty much
everything that that we used to work
with. Aentic AI is also coming very
rapidly into our daily lives and and
setting the goal to optimize our work
and enhance our productivity. So what is
the business central's answer to this
story to the agentic AI and using
generative AI within business central?
My name is Dmitri Richard and together
with me I have
>> Peter Boring and this is actually the
first time Dimmitri and I are making a
session together and we are live. This
is not AI generated.
>> Not yet at least. All right, [snorts]
let's dive straight into it. For a while
now, two fantastic agents are helping
two of your teams, the sales team and
the payables team to enhance their
operations. These agents are embedded
into business central canvas and helping
the teams capture and process request
for quotes and capture and process uh
vendor invoices which can be hundreds
and hundreds entering your business on a
daily basis. We also presented on
multiple occasions how rich these agents
are and how many tasks and how many
decisions they can take during the
course of their work. So this for
example is a brief overview of the sales
order agent how it can be triggered and
then do all of these activities when
capturing the quotes and creating uh the
sales orders. And here's another slide
which shows the powerful capabilities of
the payables agent which also can
capture the the vendor invoices process
them match to the orders and do many
many many tasks which users otherwise
have to do manually. So the question may
come is uh what what is it what is this
experience adding to your experience
when working with business central? Now
let me explain that story by going into
our favorite product business central.
Now in this segment I'm not going to
talk about the capabilities of the
agents. I'm going to talk about the
capabilities of the entire framework
which is built to enable such
experiences within business central. For
instance, you can see that we added a a
nice human in the loop experience where
new tasks whether they belong to sales
or payables, they come into this pane
and they propagated to the top of the
list. So, so users can easily notice
this uh tasks and process start
processing them. Now there is a a great
setup experience with multiple options
and additions which user users can
review and adjust to their needs. Now
there is another interesting capability
uh of human in the loop experience uh is
ability to see the entire timeline of
the agent performing the task. So in
this example you see that the agent when
receiving the document from a vendor
went through multiple steps and as a
user I have a complete overview of what
was done and what was uh happening
during that process. I can open the
document and I can see the changes uh
done by the agent with information tool
tips reasoning tool tips. uh I can I can
see the actual PDF document which was
processed by the agent and I also by the
virtue of being inside of the product I
have access to full navigational
capabilities of the product. So I can
switch to many places within this UI
doublech checkck verify this information
if I want to be extra certain that the
agent did the right steps. So all of
these experiences are very convenient
and very important within the product UI
uh to to kind of build that trust with
the users when they work with the
automated AI agents. Now let me show you
another aspect of this framework. So for
instance when the agent is processing
this document what it is doing it is
doing exactly the same behavior. It's
replicating the same behavior as users
would. it is looking at the at the
content of this screen and it has a task
to perform. So it navigates the UI in a
very similar fashion to what to how
users do it uh to to decide what to do
for each particular element on the
screen. For instance, at this moment of
time, imagine that it has a task uh of
matching these lines uh invoice lines to
purchase orders. So what the agent would
do it would analyze this page it would
look at the lines and it will start
processing line by line uh like select
the first line go to the order matching
u click match order lines analyze what's
available on the screen which of these
lines would be the most applicable to
the line that I'm reflecting on right
now so the agent would use LLM to reason
over the data it is seeing to reason
over the UI I elements and take a
decision and move forward with uh with
the step. So that work on its own took a
lot of effort from our team to make this
navigation uh secure, reliable and um
and efficient. For example, Business
Central is full of uh interesting
scenarios of how we handle lookups uh
drill downs, how we invoke search. So
all of these need to be specifically uh
massaged into this framework so that uh
the agents could do this navigation very
very accurately.
Another thing which I wanted to to
mention is that of course the security
and the access and the administrative
controls are extremely important to the
users. So the agents are built just like
uh users from the administration
standpoint. So if I navigate into the
list of agents
and uh you will see a very familiar
structure uh of the of the agent setup
similar to the user setup where I can
define permissions. I can define which
users can work with this agent. Uh I can
also specify the profile and the profile
will set up exactly what this agent has
access to from the UI navigation
standpoint. So we're making it super
easy for the administrators to define a
very explicit model of operation for the
for the agent which tables it has access
to and which UI it can navigate to make
sure that the agent does its job
reliably and uh it's easy to overview
and monitor all these experiences.
Another experience which I wanted to to
mention here is the again the experience
for administrators because these agents
are distributed as apps as applications
and we have exactly the same enablement
and disablement mechanism which is known
and loved by all of our administrators
that when that app is installed into
your environment the administrators can
see these agents they can activate
deactivate them based on their needs. So
this entire experience is built around
um around working with agents within
business central.
So in summary, you can say that what
we've been working on uh in while
building these two amazing agents with
many agents to come is a framework which
helps build user trust in what these
agents do. Here you see some of the
examples that I just demonstrated
directly in the product. uh neatly
arranged on one slide where we help
administrators and the end users work
with these agents reliably and
confidently and build that trust and
build that confidence in the results
that these agents provide to allow them
to to perform these tasks uh on their
behalf or helping them do these tasks
very very efficiently. But you know that
we rarely if ever build things just for
the for ourselves uh to uh to use. We
always think of our amazing and broad
ecosystem of partners, consultants,
ISVS. So over the time uh you get used
to uh great things built as an
extensibility model for business
central. For instance, uh our our AL
language allows you to extend business
central application to many many more
apps. We have thousands and thousands
amazing apps on up on the Microsoft
marketplace right now. We added another
dimension of extensibility through APIs.
Now, Business Central can be extended to
many many external systems and connect
to them and exchange data. And the time
has come in this era of AI to also
introduce extensibility into the world
of copilot and agents.
So, I am extremely excited uh to share
this this story with you and invite
Peter to tell you how everything that
we've just you've just seen in my demo
can be handed over into your capable
hands. Peter,
>> thank you Ditri. So, it is indeed
exciting times. Um we are now launching
in preview the ability for you
especially consultants, product owners,
domain specialists and and even makers
to design proof of concept business
central agents.
And what can you do? Well, obviously you
can create agents. Um we also saw that
agents have instructions and a view of
the business central uh application or
functionality that they can access. So
you can assign a profile to the agent.
You can limit its access by giving it
permissions.
Then you can simulate triggering the
agent. So basically manually invoke the
agent to run simulate that it receives
an email etc. Um you can troubleshoot
the agent if it doesn't uh reach the
accuracy that you expect. You can
troubleshoot and iterate on the
instructions. You can even understand
the consumption the the expected billing
of uh your uh agent.
Now uh this experience is an incline
experience and it's supported in
sandboxes.
So here we are in the client. You can
see there's some uh agent avatars for
the payables agent that Demetri just
showed. But you will also notice that I
now have another avatar for creating an
agent. And I can go in and start that
process. I have a wizard experience. I
can create the agent from scratch or I
can use um one of the samples that that
uh we ship. Uh I'm I'm going to go into
create agent from scratch. And basically
I I have this wizard experience that
walks me through how to do that. Now
we're running a TV kitchen here. So I
actually already prepared one. So let's
look at my agent here. And so I prepared
this by uh creating a name and
description etc. I gave it a sales order
processor profile and gave it some
permissions.
I also created some instructions for it.
Some simple instructions that it can
help with customer information as its
goal. And the the actual sort of
instructions is to find the customer and
look up the requested information.
And I can then as part of iterating on
my instructions
run
and then see what happens
in the uh task steps. So I can see that
the um the uh the the agent got some
input where I basically ask it for the
contact person on the edum customer
and it then itself navigates to
customers and it finds the information
and drafts a reply and we can actually
see in the message here in the task or
in the agent pane that it found Robert
Towns on the Adatim Corporation.
So that shows a very simple example of
creating your first own agent. So in the
AI development toolkit, we added the
ability for you to create agents from
within code. Uh you can add
configuration options. You saw in
Demetri's um demo before how he had
various setup options for the payables
agent. You can create your own of those.
And of course you can also add then the
instructions and the profile and the
permissions through code. You can build
any integration that your agent needs.
Maybe it needs to be triggered in a
certain way. It needs to uh be part of
an email chain. Uh you know react to
events etc. Uh you can also add new
functionality that helps the agent
fulfill its goal in a better way in a
more accurate way. Uh and then
eventually you can deploy this as an
extension. In the preview, we support
that you can deploy to sandboxes. Uh
later you will of course be able to
deploy uh these extensions to production
environments.
Now the ability to design agents in the
web client as well as code and deployed
agents in extensions are new
capabilities in the AI development
toolkit in Business Central. Um and on
top of those uh we will also soon give
you the means to actually go and
evaluate the agents so that you can
automate evaluating the results of
agents and the impact of iterating on
the uh instructions. So you might be
asking yourself you know where do agents
add value and um what are good candidate
scenarios for using agents.
So first off, scenarios where you need
to handle unstructured inputs. That's an
obvious candidate. Um AI and LLMs are
great at natural language, emails,
documents, etc. Could also be scenarios
where you need to weigh context and
uncertainty and maybe escalate to humans
if the confidence is low. That could be
matching scenarios
or when you need to dynamically
orchestrate a flow. Maybe what needs to
happen depends contextually on the
situation itself.
Agents are great at automation.
Sometimes you're using agents to
automate. And one of the nice things
about that is that the agent can
actually assess when it should include a
human in the loop in the automation to
handle unforeseen scenarios.
As we saw, agents work really well when
they can act as a user. Uh having the
permissions like a user, restricted
access to to data, etc. Uh when you need
to have state agents can actually
memorize and use input that it um that
it got earlier in the process, it can
use that later in the process in a
dynamic way. Or sometimes you want to
have the user understand what happened.
So agents can help explain and provide a
summary etc of the process up until now
to help the users actually decide on how
to continue.
And finally as we saw agents are
actually driven out of natural language
instructions that makes it um for some
cases much easier to to tell what the
agent should do. So, we're seeing an
explosion of agent ideas and here are
some ideas. So, it could be returning
items. So, based on customer emails, um
handle the item return, create credit
memos, return orders, etc. Could also be
creating reminders uh based on customer
payment uh history and having the agent
actually go in and actively do uh
adjustments.
um could also be preparing vendor
payments where the agent can create uh
payment journal lines and go again in
and adjust various uh things in in BC.
There's many many other tasks that users
do on a daily basis that are obvious
candidates for agents uh to do. Now
recognizing the importance of embedding
agent AI into business uh processes,
modern products aims uh to offer
multiple adoption paths allowing
customers and agent builders to engage
with agentic capabilities in ways that
best align with their needs, aspirations
and constraints.
And this also applies to business
central where you have a choice of both
native BC agents as well as uh no and
low code copilot studio agents
and this is really a choice based on the
scenario and the user needs. You can use
business central agents for core EAP
automation mostly targeting back office
users and then you can also extend with
co-pilot studio agents for cross system
front office workers uh for
conversational experiences and so on and
in the future even call BC agents uh via
MCP from within copilot studio. So how
can you get started after this? Well,
apart from extensive documentation, uh
we have recorded a number of deep dive
sessions for you. For instance, on how
to write instructions or how to
troubleshoot the agents to increase the
accuracy and how to in detail code the
agents in AL. Uh we'll provide um some
links in the description and we also
have an aka link uh with all of the the
videos. So go out and use the preview,
build tons of great agents, give us lots
of feedback so we can improve uh the
experience. Thank you.
>> Thank you very much, Peter. And great
story and Godspeed to all of you.