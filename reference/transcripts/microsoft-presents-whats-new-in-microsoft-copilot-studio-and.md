# Microsoft Presents: What's new in Microsoft Copilot Studio and how to leverage with Business Central

- **Source:** https://www.youtube.com/watch?v=qxlFqEBAmAA
- **Video ID:** qxlFqEBAmAA
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 50m53s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

All right, so we're shifting gears a bit
from one AI topic to another AI topic. I
hope you're still with us today.
Uh here's the agenda for today. We'll
talk a lot about Microsoft Copilot
Studio.
We did a small poll in an app, and it's
not like many people responded, but we
asked a question, "How many of you tried
to use it for real?" And some people
said,
uh
"Yes, we did."
Someone say, "Kind of hello world."
And here's my favorite option,
uh "But I not I not known only when it's
mentioned."
And actually, it's a pretty interesting
observation,
because Microsoft do a lot of marketing
work to make sure you're aware about the
products and capabilities. Maybe it's
too much, but the good question is, why
would you care? Like, why would we, as
the audience, as the people who work
with Business Central every day in the
developer in a developer role, would
truly care or be curious about uh
Copilot Studio?
So, I asked Copilot to help us with
that,
and it say, "There might might be
multiple reasons."
And just kind of list some of them.
But I think we truly truly believe that
it's a really great tool which you have
today for real, not kind of
artificially, but for real, which allow
you to extend your practice, help your
customers to bring real AI usage to
them.
And that's a big deal. And therefore, we
would like to reflect on this part of
the presentation, show you what you can
build, and things like that.
As a Microsoft, we provide uh like a
community with a lot of tools and wave
and ways to achieve things from a
bringing AI to the end user, you know,
like, for example, maybe my mother who
kind of maybe in accounting role, and
she love Excel, and kind of very nice
technical user on some basic level. I to
empower organization team to go very
kind of pro dev way and build very very
very advanced integrations. And the
truth is BC community is somewhere in
the middle. Like we are inspired to
bring a lot of automation, autonomous
agents in the world, and ERP is the
place where you can make it happen. If
you think about that, it's really a
field of work we can make a difference
with our
let's call it AI for now versus maybe
some other fields
where people work. So therefore, we're
going to focus today on Copilot Studio
to show you how can enrich uh your BC
proposition with things we can offer.
Exactly. So
Copilot Studio definitely is your single
step end-to-end tool that provides a
complete uh life cycle for designing
agents.
Um
it's definitely also a good tool if you
want to extend Microsoft 365 data, and
you can do all that by connecting your
data, your knowledge from Business
Central, and bringing it to Copilot
Studio.
So with Copilot Studio, we can create
chat experiences
uh for both customers and employees that
are not only intelligent and secure. And
in the recent 2 years, we uh Copilot
Studio has made so many uh improvements
that the these agents now can be
completely autonomous, customizable, and
collaborative.
So let's take a look on how Copilot
Studio can function as a platform. Uh
the way we see it, there are three
foundational pillars of building
uh and maintaining agents with Copilot
Studio. There's the design pillar,
there's the enhance pillar, and there's
the manage pillar. We're going to deep
dive in each of these pillar, and we're
going to show you how to build an agent
with each of these steps.
So, let's start with design. If you're
new to Copilot Studio, or if you not
knowingly,
whatever your response was,
uh this is the way you can get started
with Copilot Studio if you want to build
your agent.
You can either start These are the ways.
You can either start with a pre-built
agent. So, there are a lot of pre-built
agents that have been developed in
recent year
uh in Copilot Studio, and you can just
use one of them as they are. But, you
can use either templates if you want, or
you can build an agent from scratch.
And
if you're a low-code developer, or if
you're a pro-code developer, you have
all the ways in Copilot Studio to get
started. So, you can get get started
with uh Microsoft 365 Agent SDK if
you're a pro-code developer, and if
you'd like to develop agents using
advanced tools.
Or, you can just use the UX
uh a visual canvas that has many may
that has gotten many improvements. It's
a modern UX to build agents.
But, if you just have an idea, and if
you just want to talk to the Copilot, so
you can have a conversational experience
uh as well. And that's what Evgeny will
start showing you.
Yeah. So, what we're going to do for
next half an hour, I basically take you
step by step how to build, enrich, bring
some logic intelligence to the
uh Copilot, and then we'll tell you how
would real users could use it of what
you just built.
So, to So, to build a new Copilot, like
we use for Copilot, but now all labels
get changed from Copilot to agent. So, I
might be still confused, but it's the
same thing. You build something
intelligent for your users who would
like who can help uh with the uh with
the given tasks, or solve some problems.
You can press a new button and create in
a couple of clicks, obviously.
But what we just did, we pre-created
um
a small agent.
And for now what's important to be
aware, you can change an icon and you
can say like really, but yes, you can
bring your brand, obviously, and you
define what you want to do.
In this particular case, we only built a
small copilot which can help us to
answer employee questions about vacation
statuses and how to procure new
equipment. And it's a really like a demo
example, but it really illustrates very
nicely all the data integration we're
going to show you today.
Now,
when you build something like that,
how do you express what copilot can do?
In a copilot studio, you can define
something called suggested prompts or
collection of initial questions
which should be or could be answered
with this copilot. So, in this case, we
can help with vacation updates, uh but
it can also help with a
uh procure procurement of uh equipment
for the for the employees.
So, it's really easy. It's press a plus
button, describe what your copilot need
to do.
And it's a little bit like a maybe like
a skill in a magic. In our particular
case, we're saying, "Hey, we'll assist
employees in our organization." And you
can use the data from Business Central,
from other systems to solve a number of
given tasks.
You can also select a model, if you
care, just saying, uh which people will
use behind the scene to enable a lot of
integrations.
One of the most important settings,
absolutely hidden and hard to find
somewhere in settings, is the following.
Is
use generative AI orchestration for your
agent response. What it really means, it
means you put yes by default for all
your work going forward and a lot of
magic happens. But basically, it's
enabling new capability which we're
going to demonstrate to you basically
for the next half an hour.
Exactly.
Very important setting.
So, now we know how easy it is to get
started with Copilot Studio.
Um we should also now know what are the
basic building blocks that we need to
know for building an agent.
So, there are few essential blocks that
you would need to know. There's the
knowledge, which means whatever existing
resources, files you have been building,
you can bring it to Copilot Studio.
There is tools, which means this is the
way to These are the tasks and processes
that you have in your line of businesses
that you can bring to Copilot Studio
and build agent with it. There's the
orchestrator, which allows
you either to have a control on set of
things that that an agent can do, or you
can have automated triggers
defining the next set of steps given
given a user scenario. So, this you have
the logic and autonomy both there.
And then finally, there's the user
experience, which is channels
where your end users can see what you
have built. So, let's take a look
closely in each of these blocks.
Knowledge allows you to create an
immediately useful agent. It's like the
best way to just build a very productive
agent. All you have to do is bring your
data sources to Copilot Studio, and then
agent based on that knowledge can
respond to the user, and you already
have a creative chat experience.
There are multiple data sources included
in Copilot Studio.
We'll see what we have built with this
example.
Will we?
Yes.
All right. So,
knowledge. It sounds quite easy,
actually, but when you create your
Copilot agent, you have an opportunity
to to decide in which reality should
this Copilot be grounded, so to speak.
And you can bring a lot of what we call
knowledge.
For example, you can say, "Based on all
the documentation, which is very dear
heart to me in my organization, I would
like to answer given questions."
And so on and so forth.
Very straightforward.
Uh in our simple demo, we're basically
saying
we add two
knowledge sources, some public website,
which we trust, like Microsoft
documentation about Business Central,
and we also upload some files which
provide some company policies about
employees and some vacation statuses.
And in a real life, it probably will be
SharePoint's
um folder or some database, but for a
for example, just a CSV file is fine.
But the idea you can upload
data in which your Copilot should be
grounded. We use the word grounded, what
it means it refers to this as a truth
and nothing else.
And you can start asking a question
like,
uh is it allowed to take 2 weeks
vacation
in a row in my company?
Like,
you know, if you just
let's see what Copilot can help us with.
Obviously, we expect it will reply
in a context uh
of what we just discussed. So, you say,
"Yes, actually you can." And it finds
some source and some links on some of
the documentation we just uploaded. So,
respond with grounded in a truth which
we as organization believe is good
enough.
Uh
when you test your features, you can
enable something called um activity map.
So, let me run it again, so you see how
it works.
So, now we're in a test mode, and we're
asking a question for a Copilot, and
then you can see runtime or real time
what is behind the scene. In this case,
it's a straightforward question about
knowledge. It went to the knowledge
source.
You can kind of
go ahead, expand, and build your
confidence that the system works exactly
as you defined and exactly as you want
it to do.
Just saying small things.
That's about knowledge. We can add more
knowledge.
Yes.
Um,
let's go to another building block,
tools.
So, this is where I would really love to
have your attention because this is
where you uh as an AL developer, AL
consultants can contribute by bringing
Business Central data to Microsoft
Copilot Studio. So, what does tools do?
Tools basically allows you to build an
agent that can do and complete task
based on the data from your line of
business applications.
And there are
enormous amount of choices in of using
which tools in Microsoft Copilot Studio.
There's the pre-built connectors,
including our Business Central
connector. If you're aware with Power
Platform
Business Central connector, this uh and
it it it basically is a component that
allows to bring Business Central data to
Power Platform. It's the same component
that will also allow bring Business
Central data to Microsoft Copilot
Studio.
And all the same features are available.
There's the custom connectors. So, if
there is more you want to build, you can
build your own custom connector and
bring data from any source, including
Business Central to Microsoft Studio.
Then there is the agent flows. Now, if
you're aware of aware with Power
Automate, this is something like Power
Automate, but integrated within the
agent experience in Microsoft Copilot
Studio.
There is prompts, which is very recent.
Uh and this allows you to basically talk
to LLM
in an easy way and let your let your
agent run the co-pilot experiences.
There's the skills, there's REST API,
and then there is
our favorite topic model context
protocol. So, there are a lot of tools
available with Microsoft Copilot Studio,
but let's see
one by one some of them.
There's the agent flows. This one allows
you to accelerate your agents with
rule-based workflows for structured
tasks. So, if you have if you know, for
example, I I want agent to run these
steps to place an order in Business
Central, then this could be your tool.
There is prompts.
This can be used when you want to guide
your agent to use the LLM to perform
certain tasks.
Now, this is very interesting because
here you have the options to sometimes
use out of available uh templates for
prompt, if you're not into prompt
engineering yet.
Uh but, you can also just get started in
the scratch from the scratch for writing
prompts.
Let's see some demo on how we can
integrate with our agent.
Give Kenny.
All right, back to agent definition. We
talked about knowledge. Let's look on
tools.
Like real work. Um what's happening
behind the scene.
In this particular way, we give our
co-pilot a lot of way to work with the
data. You can see You can maybe see
familiar icon from our connector to
Business Central. You can see I will
show you flows,
prompts. And but, you can also integrate
data to other services. Like in this
case, I just talked to
uh Exchange service to get some
information about my in my my on my
employees uh
profiles.
Now, we can go ahead and add a new tool.
And if you want to add a new tool,
you can have a lot of ways how you can
bring data with your with your custom
APIs or accessing to Business Central,
you can use connectors. We can start
typing Business Central.
If I can do it right.
Maybe I can do it right.
And maybe there's a search working in
Microsoft products. Let's see if it
does.
Yeah, it does. So, you can go ahead and
you know, add action from our connector
to do some things.
For example,
let's take a look
on a
that tool. So, we have a tool which can
help our copilot to answer our employee
questions about available equipment
which he or she may purchase.
So, in this particular way, we're saying
that
we're going to use connector,
our connector to read find records, and
you can see we can basically just call
our API uh for a given environment, and
we receive some data back. Now,
obviously it's hardcoded.
Obviously, in a real life, you you'll
probably
use something like
environment variables so you can publish
your solution. You have your environment
definition, what is your environment, so
you don't hardcode your connections. But
for a demo purpose, it serves us us very
well very very very well.
Another interesting thing about this
this connection integration, there's a
property called running under user OS.
What it means that back in the Power
Platform world today's, well, there was
always like a question, which account is
used to run my automation? Is it me? Do
you have permissions? Uh do you have
like a system super account which can do
everything for integrations?
In a in a copilot world, all this
connection will be running under user
permission. So, the user who ask a
question, if he or she cannot shall not
pass some security permissions, it will
not going to happen. So, super
convenient.
You're basically saying the user will be
run with your with him or her or his
permissions
uh to get the data.
And now with having this connection, you
can start questions like that.
For example, we can start saying
just to test it, I need a new I need a
new laptop. Show me all we have for
employees.
And again, if you can enable
activity map,
maybe not here.
Just a kind of very simple use case that
yeah, uh, we enable our users to ask a
questions like that.
And then the way how we describe that
tool, this connector, it will come here,
it will come to Business Central, it
will fill out all the parameters, get
the data back, and now we can bring this
data to further conversations. For
example, here we ask about all the
different models,
and you can go ahead and say something
like
just an example, can you tell me more
about another model?
Yeah, maybe I'm rushing a bit with the
demos.
But the idea is that that can that data
become part of your conversation, and
you can continue work with it.
Okay. So, let's back get back to tools.
What I maybe a little bit rushed to
mention, we also made a description when
to use this tool, and we said, "If you
want to retrieve information about
available laptops, basically call me,
and I'll do the work." And that's how
our orchestration knows
to
answer these questions.
The next type of available tools you can
do is to create what we call prompts.
Oh, Monica said, "We love prompts." So,
we have a prompt, which allows us to
find a specific information about given
laptop model.
Maybe you don't store this data in
database, you probably don't. Maybe you
want to reach out somewhere else.
So, in this case we're saying, "If you
want to have more details about laptops,
call me."
So, let's take a Let's take a look what
this means.
In our particular case, we have a
specific prompt
who would like us to help to answer
questions like that.
I'm going through a couple of clicks,
next, next, like edit to get to the
essence,
but that's just how it is.
Yeah.
So, we have a very short prompt, like a
write a short summary
about this device based on a given
information. In this case, you would
just say knowing the laptop name, we can
go ahead and do a good job. You can also
When you create those variables, you can
also create some sample data, which is
super handy.
It's not going to go ahead and say,
"Okay, let me just try to test my prompt
and see if it works right away." If you
develop that part,
yeah, like a off of off small prompt,
and now it will just use this kind of
test value to give you some results, and
of course, you can say,
uh you know, return
top features
as bullet
points. So, so it's all very flexible,
all very real, and you can play around
and see if I want what I want to do with
that.
And again, maybe you want to have text
back, maybe you want to have JSON back
if you want to integrate, and so on and
so forth.
You can also select the model
you would like to use for that.
And that's where it become very
interesting from a primitive task like
describe
data about something to maybe do some
much more advanced research, uh
summarization, and bring significantly
more context
to answer the questions. For our demo
example, we're just saying like,
find some descriptions,
but you can do go significantly further
uh with that small approach. And that's
why we like prompts, because they work
very, very, very well.
And that's how in my previous example,
when I ask more information about the
laptop, Copilot could answer because it
went uh on that path.
Another interesting tooling
what you could could add and maybe you
should add is to start adding more
complicated flows.
So now assume you you want to have a
question not just
show me things but do something for me.
Create approval, create an order, notify
my manager, things like that. In this
case, we can create a flows.
So in this in this in this example we
have a
a flow which will
use to which will be used to order
equipment for employee.
So if employee say I want to
purchase
get get equipment, basically call me and
I can do this work.
And behind the scene
we'll have a
flow like a classical flow which we know
and love from from our from our
experience. So here I have a flow.
I just wanted to show you that.
And that flow is quite
sophisticated. Is that the right word?
So it's kind of you know I need to
scroll couple of times just to see how
it's built. So they're basically taking
like a business process to try to
understand the context, create business
central request and if I don't know what
to do, I can always say like
Hold on. I can always
say like
What does
this flow do?
Super handy
if you need to analyze like a
complex
a flows but basically saying the flow is
designed to handle equipment requests
and then it just describes to you
exactly what it does.
Yes and sorry and here you can also see
that this is another way of using
Power Platform Business Central
connector cuz
you can see there is one action with the
Business Central icon where
it's connecting to Business Central
data. So, you can directly connect your
agent through the connector or you can
use via the flow of the connector.
Yeah. So, in this way we'll just
take an request, understand what does
employee want to purchase, and create an
order in a Business Central, and we'll
show you obviously to you how it works
end-to-end. But, the idea you can create
sophisticated workflows, and then say
for a copilot, "If this action has to be
happen, call me. I'll take care about
that."
As this for this particular flow, the
only input we need for our demo scenario
is the equipment name. What
he or she need to purchase. And in this
case, we have a property called
dynamically filled with AI. So, copilot
will understand from the conversation
what was the discussion was about, and
use that input to kick off a workflow.
Definitely.
All right.
So, maybe just to summarize quickly,
you can use connector to connect to
Business Central. Uh you can create very
specific prompt to do work. You can call
or execute complicated workflows, and
then you can connect to many, many
things like MCP, but we'll cover it
later
in the presentation.
Yes. I just want to add one more thing,
which is the custom APIs that you would
be creating in your extensions, they
will be also supported through Business
Central connector. And you can always
also create your own custom connector if
needed.
Of course.
Okay. So,
um
we got the
tools, we got the knowledge.
Let's go through the orchestrator.
Um with the setting that Evgeny enabled
in the beginning in the create phase, uh
that's generative orchestration.
Basically, that allows the agent to
understand given the prompt to
understand what tool to call or what
knowledge source to call. But if you
want more control, there's something in
Microsoft Copilot Studio called topics
where you can define a set of things
that agent should do uh
given
the user's prompt.
So, that's topics. But
that's not what I want to emphasize on
this slide. There's the
triggers. That's very recent
recently added in in the last year,
which allows your agents to be
completely autonomous. So, imagine a
scenario where you would want
your agent to listen to the email
and then do something based on that. You
can do that by adding a trigger like you
would do it in a Power Automate flow. Uh
there's an option to now add a trigger
to your agent. So, that also helps with
orchestration.
Um and the last building block of
building an agent is user experience.
So, we built all this, but where would
the user see it? So, that's what we call
channels. Once you've built the agent,
you can just go and deploy your agent
and publish it to one of these channels.
There's again a wide range of channels
available from Microsoft Copilot Studio
um
including Microsoft 365 Copilot, which
means the existing Microsoft 365 Copilot
can be extended with your custom uh
agent that you created using Microsoft
Copilot Studio. Uh there's also the
third-party
um non-Microsoft channels available, be
it Google's Business Manager or Apple's
um Message for Business. So, there's
multiple channels. So, let's see our
agent in Microsoft 365 Copilot.
Yeah, so we're build a Copilot, you have
this button called publish.
Maybe I need to avoid doing that, but
you can select where would this Copilot
need to go.
In our case, we'll say, "Let's put it
where our users really are."
Okay, so let's see how would it be all
used for real life from real people.
So, I'm an employee of Contoso
organization and I'm starting my work in
a browser like that. Maybe with some
ads, maybe without.
And I work here, or I live here. Maybe I
should Maybe I should click
I clicked the wrong button.
I can start being here.
How many of you customers are Microsoft
customers who has Office licenses
everywhere?
Yeah, all our customers are Microsoft
customers which has a lot of Microsoft
licenses everywhere. And uh they might
look with Office, with the documents,
with their colleagues collaborate every
day, do all the real work, and many of
them can use Microsoft 365 Copilot. So,
I'll start my work like that. So, I now
need to get a new laptop. How can I do
it? So, I can start I can just ask my my
Copilot, "How can I get a laptop?"
Again, because I did this demo multiple
times, and who might know? Maybe I'm a
new employee, I'm working from home. I
don't see a lot of people that often
these days. And Copilot can really look
across all my organization, like not
about Business Central, but the real
data, and say, "Hey Evgeny, you already
purchased something yesterday, but if
you want to have a new laptop or another
laptop, please reach out to Monica.
Maybe she knows how to get it done."
Because we have some history through
email conversation that she somehow is
involved in procurement, and I'm not
surprised. She knows people.
I can help by telling you we have this
agent that we can use.
Of course. So, Monica is telling me,
Evgeny, "If you wouldn't be lazy, you
can discover all the agent all the
agents available for you as an employee
in our organization, like my Contoso
agent which we just built."
So, I just did it. I deployed for
myself, and here's my agent.
So, I just click on it and the first
thing you see, remember all this prompt
we defined what this feature can do or
could do for the user, it's right away
here. So, instead of me figuring out
what this can do, it has some initial
how do you call it?
Get started suggestions exactly. So, I
don't need to guess or look on this
empty screen you know panic and what do
I need to type which is happening all
the time.
And of course you have some prompt
libraries if you want to be creative,
but I know what I want.
Let's say let's go to our basic flow.
I have some
Yeah, notes.
I'll repeat it a bit.
But
you'll see how it goes.
I'm slow in typing much better in
copying.
Yeah, show me what's available for me.
And now my co-pilot will go back to
Business Central, find all the laptop
and say, "Hey, here's what's available
for you." And while it's doing that
I can obviously
show you something more sophisticated.
Do do do do do. Yeah, so it's come back.
What it had?
Show me what you have for employees.
Now, it show me employees. That's not
good.
Show me all
laptops.
Yeah, thinking about second step of demo
when first didn't work that well
is not a good strategy. But now, yeah,
the go to Business Central it come up
with laptops and can give me some
different variations. And now I might
say it's all good, but
which one would you recommend?
You know, maybe it's too hard for me.
Compare those, give me the best, what is
within my approval range for that price
these days
wherever it might be.
And then it will say, "Hey,
what would it say? It'll say
Surface and Lenovo can be a good choice.
Then I can easily say, obviously,
cool. Place an order for Surface.
Like
I want that one. And obviously here
probably have a workflow saying I need
to get approval from someone else
and so on and so forth. But the idea is
that now you can call that workflow that
flow I showed you before and it go ahead
and create an order for me and place an
order in Business Central and we can
also always remember give a links back,
so I can click on it.
Uh
if I have permissions to.
Maybe my manager get notified with that
card and here she can click and see yes,
that's the right order and go ahead and
approve it. And here's the order we
created all together a couple of seconds
ago. So again, the main idea for me as a
normal user to be able to reach out for
a data which is grounded in some truth,
be able to get the self her kind of help
and also take an actions.
Now,
also in a real life what I would
probably do because I use Copilot for a
co-worker, I can also say, "Hey,
maybe I want to
kind of save this information for the
future like we use the pages as a way in
office to maybe
uh save some kind of piece of
information as you work and they can
say,
"Monica,
you know,
maybe I want to
give you access so she know I have this
order."
Again, I'm working with a real people
and I say,
"Thanks for help."
And of course, you know, she's get
notified and we can continue discussion
and kind of getting this so handy. So
again, as a employee, my experience was
I should be able to discover an agent in
my view of work with the tools where I'm
present.
I I as a user I not necessarily even
care that Business Central exists. It's
just another system somewhere else, but
I can interact with this. I can kick off
pretty sophisticated workflows, and so
on and so forth.
Now,
um
let's back to chat for a second. Do do
do do do do.
I can also
access my agent differently. We have
this feature called chat with agent. In
case you have multiple of them, I can I
can again discover, you know, the same
agent and go ahead and start chatting
with it right away.
So, you have pretty kind sophisticated
experience how the employees or users
will experience agent in kind of not
disruptive field of work in apps where
they are.
That was pretty cool, Evgeny, to have
like our custom agent right there with
Microsoft 365 Copilot. So, we have built
an agent. We have seen it how users will
use it. So, what's next?
We can enhance it. And how do we enhance
it? We enhance it with
having
integrating with Azure AI Foundry
services in your agents.
Um there is multiple features available.
You can bring your vectorized in
indices. You can bring Azure AI search.
You can bring more than 1,900 models
available in the foundry.
Um and all of that you can be a pro code
developer and bring it to your agents.
But not only that,
you want to know how your agent is doing
in production. So, you can monitor uh
uh monitor your agent. And there is a
right there's an analysis activity tab
right in integrated right in Copilot
Studio, where you can see data-driven
insights. You can know how users are
doing how's your CSAT score. Are there
any errors? What are the escalations?
Everything that you would need to know
in one place about the agent that you
built.
Uh
design is done, managing is done.
Uh so, design is done, enhance is done.
Let's go to management, and then this is
where basically admins will play a role.
So, there's a place for Copilot Studio
in or they will be available soon for
all of us
uh in Power Platform
uh admin center, where administrators
can go and manage all the agents that
they have built. They can manage the
life cycle, they can manage the access
control of these agents, and they can
even decide when to roll out which agent
and staging and all that.
So, one place for the admin to do the
management of the agents.
So,
uh we have almost 10 minutes, and we do
want to cover this, which is uh it was
in our description, which is what's new,
what's very recent in Copilot Studio.
Uh so, we want to go through these.
There's definitely agent store that is
generally available. Uh this is a new
marketplace, imagine like an app store,
but for agents. So, it's agent store.
Naming got right this time.
Uh
So, there's a new marketplace for
Microsoft uh
uh and Microsoft agents, and also for
your agents that you will be building.
Um where users can find and install
agents from this store.
You can also in uh share these agents
with colleagues, and you can um these to
have the agents in this agent store,
there is a rigorous validation to make
sure that the agent is doing
uh the right uh intentions,
uh and then we can have the agents in
the store.
This is my favorite. This is multi-agent
orchestration.
This actually
enormously increases the the
capabilities Microsoft Microsoft Copilot
Studio offers, which is you can or you
can make one of your agents talk to
another of your agent. Uh this will be
soon public preview. It's actually
already being
rolled out. Uh
And this is where you can connect your
agents with other agents and then have a
have a basically nested agents within
each other and talk to and so you you
have enormous opportunities to uh make
your users boost productivity.
Um
Yury, do you want to talk about more
uh for deep reasoning?
Uh not really.
No, okay, let me do it.
Uh so there's the deep reasoning in
prompt
uh where now you can have access from
from one of the models in Azure AI
Foundries.
Uh
it's the 01 model that is very good with
deep reasoning. So it it it's imagine
like talking to a person who has deep is
very good with deep thoughts and
reasoning. It's similar. Uh so it Every
time it will perform an action, it will
actually uh think more deeply and come
up with more thoughtful responses. And
that model is now available from prompt
tool that Yury can shoot.
But you do want to talk about Microsoft
loves MCP.
Yeah, so how many of you heard this
acronym
before?
Okay, how many of you heard this acronym
2 weeks ago? A month ago?
Yeah, okay, what about 6 months ago?
Good, because there wasn't.
probably was created like 6 months ago,
4 months ago from Anthropic. But yes,
Microsoft loves MCP. And what it means,
if you go over the next slide, it's
something like that.
Yeah. Do you have a feature? Awesome. It
has S&P. I'll buy it. But with all
seriousness,
it brings a flavor to a lot of LLM and
AI integration, which is really a big
deal.
It kind of standardize in a way how all
the features talking. And for the for
the developers, all the ISVs or a
it give you an ability, a hope, a path
to maybe extend all the LM features we
do or someone else does.
And we'll talk about it in a sessions
later today and whole event. But for
Copilot Studio, what it means
is if you go a couple of slides before
Yeah, we'll skip all that.
Yeah, we have a demo.
So, everything we're going to show you
it now from a lab which probably has a
very, very high chance to be true in a
short future.
And we can do that.
Yeah, I can do it shortly, quickly.
I'm in I'm in a Copilot Studio again,
and as always, I want to bring more
tools. So, the point is that we want to
bring more ways, more power to Copilot
to do actual work.
In this particular case, Business
Central become a server or the source
saying
I can do a lot of things about
items, customers, orders, and things
like that.
So, in a way, stay with me, we say
Business Central can magically answer
all the questions which you can ask in
natural language about ERP. And if you
need to create an orders, figure out who
owns your money, figure out all I still
not approved invoices, I can help with
that. That kind of a promise where
become MCP server.
Which allows our chat
to start questions like that.
So, we say, and then let's enable, let
me help me out.
You can say, "Show me latest quote from
BC."
Like, that statement by itself doesn't
have a lot of meaning in a in a in a
real world, but what's happening here
is that
Copilot Studio runtime can understand
you need to talk to Business Central,
it's probably about business sales
quotes, and maybe that thingy can help
somehow with that.
Do you want to show tools as well?
Yeah, it will come.
And small carrier, that URL has
something called pre-prod or
pre-production, meaning this feature is
not shipped yet, but it's kind of on a
pass. It's not developed yet, it's kind
of rolling out slowly.
And it's obviously
Okay, let us just let us refresh it for
a second.
And try it again.
This is from
the business central MCP server is from
the lab. We're still cooking it.
No, it's pretty good when it works.
This is the demo which I did show in the
first day when she was in Entropic and
she could create a quote from complete
another experience in a very kind of
nice way.
Um
does not collaborate.
Okay. But And that's fine. But the main
idea is that in Business Central, right
now we use
APIs like customers, items, sales quote,
and also maybe custom APIs which you're
going to build. And based on those API
definitions, we're saying Business
Central can do all that work and call us
if you need help. And any
uh large language model feature like
Copilot can now talk to Business Central
and get the directions. Which kind of
raise the level of integration by bar
because before you specify very
specifically what is my like all data
queries and properties and values, now
you kind of have one layer above saying
more like abstract way
help me with this work and then we'll
say we'll figure out. That's the
promise.
And that's why we are so excited about
MCP
and we are working on that.
Let's make it one more try. One more
try.
It has to fly. environment in US. It's
not an excuse, but
and get some data back.
Unbelievable.
Okay, so show me latest quotes from BC.
Okay, so now I know something's
happening.
Yeah. So, in this particular case, it
figured out that maybe here is an API
called sales quotes and maybe
latest means that field based on the
metadata
sorted mean latest and maybe top means
five, maybe two or three. And just kind
of again transforming your intent, if
you will, to actual calls and bringing
some data back, so to speak.
Awesome.
One more time. Maybe I will enter post
here and say one more time. You express
the intent what you want to do and get
data from Business Central.
Uh MCP definition and tool definition
allows to convert this intent to work
concrete API calls, if you will,
and get the data back.
Definitely. And
what is even nice to see is that if you
actually go to add a tool,
Yeah, let's try it.
If you go to tools,
and we want to add a new tool,
and you can already see
in here there is an option for
um
Not yet.
Yes. The So, if you click here, you
could you could probably see Oh, sorry.
If you go back, yes.
Yeah, it was here.
Under here, you can see there are
multiple MCP servers already available
in Co-pilot Studio, which means there's
also a lot of tools from these servers
that you can use to build your agent
with.
what we announced on a build from again
Dynamics level of view, that all of our
products like CRM, BC, expose MCP
servers. So, now you can go ahead and
get data from CRM, create orders in BC
and all kind of on a natural language
being in Entropic on other surfaces and
it's just lovely.
And very very nice. That's the same.
Definitely.
Okay.
So,
getting to the end of it.
This is the whole
life cycle for building and publishing
and analyzing and improving your agent
through Copilot Studio.
And what are the key takeaways? I just
want to say that you can use Copilot
Studio to build your custom agents. You
can connect Business Central data
to Copilot Studio. You can work with
your custom data, custom APIs.
You can publish on multiple channels.
And you can actually bring AI to the
real users. So, please stay up to date
with the AI journey through Copilot
Studio.
And maybe another takeaway because had a
conversation last night like why would I
maybe pay attention? You have a all busy
life and busy jobs. And if you pay
attention what's happening in Copilot
Studio, you're literally almost up to
date on a industry and technology
because all the latest innovations,
ideas we just mentioned things like deep
research, MCP, they're all coming to the
product with incredible speed.
So, if you just pay attention to the
product, try it out, you you're kind of
almost up to date what's going on maybe
as a decision maker. It's just nice area
to observe. Microsoft pays a lot
attention as a product group and as a as
a company on it. Have a lot of bets.
Just saying.
Yes. It's time for Q&A. We have 5
minutes and first two questions get some
t-shirts.
Any questions?
Yes, sir.
I need some choice.
Nice.
Thank you.
Uh yesterday we were presented with this
beautiful agents fully integrated into
the BC interface. And my question how we
can we empower those agents by giving
them those tools, those connectors so
they can do more than just interface.
That's the question.
Yeah. Great question. Maybe we should
repeat it one more time loud. So we show
you yesterday in keynote
native Business Central agent platform
which can kind of you can define a path
or a flow you can automate it as BBC
user. And how does this relates to that?
That's really the question.
Yes. Uh so we already have a sales order
agent that you learned about.
Uh
that's native to Business Central.
And the idea is basically you can build
your agents in Microsoft Copilot Studio
using Business Central data. That could
be one way of integrating it. But the
agents that you build using Business
Central platform that is native to
Business Central will be surfacing in
Microsoft Studio. At least that's how it
was that's our plan to allow makers to
build even more integrations around it.
Maybe I will add to Monica's answer. So
it's it's unrelated as of now.
Uh within Business Central
we give you the platform to define with
the tools you know and love. You know
with AL craft, with your extension.
And as we show this playground, you
should be able to describe a business
process
and then it just runs on a experience
within the product. But in many many
many real life scenarios, you go across
products. Business Central is awesome in
system of record but I have this and
this and this and this and this. If you
want to automate across, Copilot Studio
is a tool.
That's really how it is.
Yeah, but we will be able to access this
Copilot Studio agent from our Business
Central interface.
Uh there is a lot of great question. How
can I interact and reuse capabilities so
you don't reinvent a wheel for example?
And we are working on that all the time.
I think right now we have Business
Central Copilot Studio, and every month
they kind of moving this direction
closer and closer.
Yeah, and yeah, but that's how it is.
Great, looking forward into it. Thank
you very much.
We do as well.
Do you mind passing it?
Ah, thanks.
Just
What?
Not a good catch.
Okay. Another question we got in the app
is classic, what is the licensing?
There's a There's a question here in the
audience.
Yeah, let's take this one since we talk
about licensing if you're quite curious.
Ah, worked.
Concerning the licensing, also same
question from the app, maybe. Um
Assuming I have a small company as a
customer who says and they want the
agent to use, what is the cost model for
them? Do they need something extra? Is
it included? What do they need?
Yeah, great question. And the question
is, what about money? What would it cost
to allow it? How can you pitch to the
end user? We'll bring it for you, but
what is it price price tag?
Yes.
Um
I just want to start with we are
definitely not the experts on licensing.
Uh but
what we want to convey the message is
that
uh
with Business Central license
you do not get
Copilot Studio rights as it is. You have
to pay extra. So, that's the first uh
message. There's some uh Power Platform
usage rights that you do get, but not
with Copilot Studio.
And pretty much Copilot Studio uses
something what we call messages. Um and
we we charge users based on
messages.
Um and there can be either you can buy
message packs, or there is also now the
new option of pay as you go. So,
uh and and that's
that's the way we go with Business
Central. Uh it's a bit more complicated
because there is the
how many messages does it take and
there's more like how many which agent
is built with how many MCS messages per
turn. So, you would need to read terms
and regulations but this is the overall
licensing that you would need to know.
Maybe also try to say that as a
Microsoft one in power makers you to
build stuff for free. And we give you
kind of pretty fine packs. So, you can
the same with the our BC agents. We give
you some capacity you can try,
experiment and build but when you
implement a customer have to pay for
some consumption. There is some models
to consume it based on packages. And if
you look on our agents on the keep KPI,
we always showing you how much money we
believe that it is saved for you.
That's how we articulate run an agent
for a couple of days, take a look how
much money or time or work effort it
saved for you and if you good with it,
how about implement for you something
similar. But that's the conversation we
having to put it to masses. But it's a
great question. And we are out of time.
thank you. The time is up and thank you
so much for your time. Hope you find
this information.
