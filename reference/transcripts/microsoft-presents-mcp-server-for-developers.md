# Microsoft presents: MCP Server for developers

- **Source:** https://www.youtube.com/watch?v=Hm2OIUUYLRA
- **Video ID:** Hm2OIUUYLRA
- **Channel:** mibuso.com
- **Published:** 2026-07-29
- **Duration:** 48m29s
- **Ingested:** 2026-07-29
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

Welcome to this session on MCP server.
I'm Yiannis. I'm the manager of the
runtime team and with me I have
Purushoth. So, I'm the manager. I get to
take all the credit. He is the one who
actually knows stuff. So, when you have
very good questions, then he will be the
one knowing how to answer.
>> I'll try to answer.
>> You're being too modest.
All right. So, what are we going to
cover today?
Everybody's favorite topic, MCP basics.
You've heard it before, but we are going
to cover it, why it's useful.
Then we're going to discuss the Business
Central approach to MCP server, because
there are different ways we could have
approached this.
We're going to talk about dynamic tool
mode.
And we're going to talk about how to
configure and connect.
>> Yeah.
>> And then we have
a little
something at the end.
>> Yes.
>> All right. So, we're going to start with
the exciting topic of what is MCP.
So, MCP is a standard or a protocol so
that
LLMs know how to talk to various
systems. Basically, three parts. You
have the host, which can be your
favorite AI app. It can be Copilot
Studio, Cloud Code, VS Code, Teams,
um other ones in in which you host a
client.
And that is the one that then connects
to the server.
In this case, the Business Central
server. The Business Central server then
exposes tools, data, and actions.
>> Exactly.
>> And other things.
Uh we'll get back to that later. Now, we
actually got a question
um before the session. So, what's
actually the benefit of MCP?
And one of the benefits is that you
don't need this custom glue between your
MCP
host and the Business Central server.
For us, it means
less work. We don't need to write
special code to get
cloud code to work.
GitHub Copilot, Copilot Studio, etc. At
least in theory. But sometimes there are
still a few tweaks because the MCP
protocol is quite a bit in flux.
>> Yes.
>> So, what the MCP server exposes. Now,
it says three primitives, tools. So,
these are the things the agent can call.
And each come with a description. The
name of a tool needs to be unique. So,
these are the things that the MCP client
will call on the
MCP server.
Then it can expose resources. And we'll
get back to that how what that actually
means for us, what use cases that opens
up.
But that's basically the data the server
makes available to the agent which can
be documentation and other stuff. It's
effectively files.
And then you can have reusable prompt
templates that the server can offer.
>> Yeah.
But I mean,
not a lot of MCP clients have
I mean, you can have a lot of MCP
clients of course, but they don't
implement the entirety of MCP in the
same way.
What we have seen is tools is one thing
that most MCP clients get right,
but they do differ in their
implementation of resources and most MCP
clients still don't really support
prompts quite quite in the same way.
We also have elicitation which I forgot
to add to the slides, but it's also a
great way in which MCP servers can
request information from MCP clients.
>> And I love how you said that MCP clients
not always support resource because that
allows us to say, "Oh, it's not our
fault. It's the MCP client's fault." So,
we can actually get get out of that
bike.
>> I
>> it also makes it a bit difficult because
if you have an implementation of
resources, for example, and one client
is using it, one client is not using it,
so as users you also get very
inconsistent experience. And so that's
also why we have a version of resources,
which is called embedded resources, and
the way that works is when tools return
response, they don't return response
directly as a text block, they return it
as a resource or a resource embedded
file.
>> Cool.
>> Yes, and that's the the central approach
to resources.
>> Yes, now
with MCP servers, they can either be
local
or remote.
So, a local MCP server will run on your
own machine.
>> Exactly.
>> Duh, it's local. Um
so, you install it, you run it, you
manage it, you basically assign it a
port or on on your local machine, and
then you talk to that. Uh and it's great
for development and for local tools
because you're in control, you can start
it, restart it, do whatever. Now, the
business
the MCP server that we're talking about,
the Business Central MCP, you'll
normally use that as a remote MCP,
which is reached over HTTP.
Um so, you don't have to install
anything, usually you'll just install a
connector.
And then if
it
the MCP server and the client both
adhere to the MCP protocol, then there
is an established way of how you
authenticate across the two.
So, that's actually how you log in.
Um
and of course, as a remote MCP, we it's
not just
authentication, the it's also
authorization, and that is still just
the Business Central permissions.
>> Yeah.
>> Now, I touched a little on the
authentication. So, the MCP is secure by
by standard. It's per the MCP spec of
November. This changes quite quickly.
Um it moves fast. Keeping up is actually
a job for
is a job for us. Um
but it's OAuth 2.1 compliant. So, that's
actually also
we've had to update our OData and API
stack to be OAuth 2.1 compliant.
>> Exactly.
>> And there are a number of pre-authorized
clients
like Visual Studio Code and Copilot
Studio. So, they work out of the box.
There is nothing extra you need to set
up.
>> Yeah.
But, I guess that's where the next part
comes in, which is how to use
third-party clients because we have had
a lot of questions on how to use cloud
code or how to use even GitHub CLI. And
that's where things start to diverge a
little bit
because in the past we had dynamic
client registration. That was another
protocol that was used by MCP for
authorization. And it allowed
self-registration of apps, basically
self-identifying of apps to say I am
this app. Let me do the authorization.
>> Exactly, right? But, that doesn't work
anymore, especially with the Entra ID
authentication that Microsoft uses. And
so, Entra ID authentication comes with
certain things that now you need to
take care of. So, for example, if you
want to try a third-party client the
first thing you need to do is you need
to register an app in the Entra ID so
that when you try to authenticate and
try the knows okay, this is the app
that's trying to call out to me.
You also need to enable a few other
things which is such as a public client
flow and adding a localhost redirect so
that when authentication is done your
local CLI agents can actually get the
authorization code at the redirect.
We also have a way to store the client
ID in Business Central config page. I'll
show you later when we are looking at
the page.
And that's just for reference. So, as
you authorize more clients, you can just
add the client ID in the authorization
page.
And as you can see in the screen,
the configuration or the connection
string that you use is almost the same,
but there are slight differences. So,
for example, in Cloud Code, you have to
provide the client ID and callback port,
but the format is slightly different,
which is documented in their
documentation.
And GitHub CLI actually the support was
added I think 1 week ago, and they have
slightly different name for the headers
that you're going to providing.
But if you provide these headers,
it will connect just like any other MCP
client. And like I mentioned, DCR is now
deemphasized. There are some security
vectors.
And so, we are moving in the right
direction. So, Entra ID's approach is
not really a hack. It is the correct
approach for authentication here.
>> Yep, should we see a demo?
Now, I got
>> Yes.
>> We have up there. That's nice.
>> All right. Uh
So, let me just shift to my screen here.
Perfect. So,
in the keynote, I shared an agent which
was the customer copilot, which was an
agent created by me, and it does not I
don't think it's a very good agent.
Whereas, I have another agent that Kenny
created. He's He's better at the, you
know, copilot stuff.
And let's take a look at this agent
here. So, it's a compliance agent. The
idea is how do you ensure for that
>> Everybody loves compliance.
>> Exactly. And at the same time, the main
idea about this agent is
every user shouldn't be a super
permission, right? Of course, in any
environment.
And so, you can take that You can take a
look at this agent that it's It has a
lot more comprehensive instructions on
how the agent should behave and how it
should function.
At the same time,
there is also additional knowledge files
that this agent uses, but the main thing
that makes it work well is the tools
section here.
If I go to the tools and I look at the
Business Central connector here, you
will see it is connected to an audit API
configuration.
And like I mentioned before,
configurations are just tool sets that
are created by the MCP admins on the
Business Central side.
And audit APIs are only providing APIs
that are relevant to this particular
agent.
And let me just
go to Business Central quickly,
open the audit APIs,
and I'll just disable dynamic tool mode
for now so that we can
do this simple demo.
Perfect. So, we have
some APIs set up for the audit agent.
And I'll just try out a simple query.
>> Actually, that was a nice catch because
when we tried this before, the dynamic
tools was not enabled.
>> Exactly. I wanted to get to dynamic tool
modes a bit later in the presentation,
but I guess you have a small idea now.
All right. And the way this works is now
it's just going to get the tools from
Business Central. It gets the tools that
we just defined on the configuration.
These are the tools that it's getting
from Business Central here. It's going
to invoke them, and then it's going to
come out with the final answer.
In just a second.
>> Yeah, and right while it's burning
tokens.
Um
So, Copilot Studio.
We're going to talk more about that in
the latter part of uh the session. The
second part where Julia and Herena will
talk about how you set this up and focus
more on the Copilot Studio part.
>> Exactly.
We are just giving you a sneak peek,
right? And as you can see, the agent did
its audit. It comes out that there are
six users. Apparently, all of them have
super admin permissions, which is
probably not a good idea.
And uh
must do recommendations immediately
review, and there's some user details
compliance. Yeah, everyone is
non-compliant essentially, so which is
not how you should [laughter] have your
environment.
>> So, this is a demo of the agent, not how
you should set up the system, just so
that you know.
>> Yes.
>> All right. So, let's talk about our
approach to MCP server, what we're
exposing as tools, etc. And there are
basically two ways you can go. You can
either expose the full UI, or you can
expose APIs, things that are built for
exposing already. We went with the API
pages first.
So, we expose API pages as tools. So,
every published API page is
automatically a tool if you add it in
your configuration.
>> Exactly.
>> And we even have a default
configuration. If you haven't set up
what should be the default
configuration,
then by default, all API pages are
available in read-only mode.
>> And of course, permissions still govern
everything, and we also give you
granular control over the tools that you
end up exporting to your agents.
But API pages is, I guess,
and and particularly
>> PowerShell tools super, right? It's
actually a nice extra security because
otherwise it could do whatever it wanted
in the system. So, you'll probably want,
particularly if you do setting it up
like that with super, you want to build
some good configurations.
>> Exactly, right? Because configurations
are a way to control what your agents
can do. You don't want agents running
wild in your production environments.
But okay, API pages are one part of the
story.
It's great for creating, modifying,
deleting records, but with API queries
you can do a lot more.
You can essentially create complex
queries that span multiple tables and
extract all the data that you need to
provide the right context for your
agents to be able to make the right
decisions, which is not possible with
API pages because if for example, you
have a lot of API pages, your agent
might just be, you know,
calling multiple API tools, just
collecting data, and maybe doing some
compute computation in memory or using
its own own Python execution, but I
think all of that is a bit problematic.
Whereas with API queries, you get
aggregation, summation, and a lot of
other complex operations.
>> Yeah, and you let you let SQL do what
it's good at. So, if you have if you're
building an agent that needs this
aggregated data,
don't let it reinvent how to do it every
time.
>> Exactly.
>> Take the time it takes to create a query
so that it's fast. It's actually the
same that we're saying for AL code that
if you're doing loopy loopy over AL
code, well, replace it with a query
because SQL is much better at these
set-based operations than either the LLM
is or the AL
is. Plus, you also get fewer calls back
and forth
because now you have one query that you
know is useful. It'll be one call
and it'll return all the data
>> Exactly.
>> with all the aggregates you need.
>> Exactly.
Now, where do the tool descriptions come
from? Do you want to talk about it?
>> Yeah. So,
we were lazy. We just reused some of the
uh
properties we have already. So, we
reused the metadata that you already
had. Now, for queries, we added the
about text because there wasn't an about
text for queries before.
>> Exactly.
>> Um there were for API pages.
Now, just having the property is
unfortunately not enough. It also needs
to have some content, otherwise it's
really hard to build a good description.
Um, so we take what's in the about text,
and you can fill that in for instance
using an LLM. You can
have a small agent that'll go through
your code base, take all your API pages,
and then generate a decent description
of what this one actually does. That's
the approach we took. That's why there
are now about text on all of these
objects because we ran an agent on top
of our app. So we get better
descriptions than the I'm the greatest
tool in the world, use me for
everything.
Which you shouldn't call your tool
because the LLM might think it's right.
Um, so the about text and the caption
and a little bit extra uh becomes the
tool description. So the way to create
good tool description is to describe
what it does. And
actually that's also what helps humans.
So you get two for one. You help your
users
and you get a better description for
tools.
>> Exactly. Also, one more thing I wanted
to add. We do We do a little bit of
pre-processing on the about text that
ends up becoming the tool description.
So for example, you might have an API
for sales invoices and you also have an
API for invoice lines, right?
We do add some metadata additionally on
top of the metadata or about text of
invoice that becomes the tool
description. Essentially saying that
you need to get the ID from the sales
invoice API. Because otherwise some of
these APIs are just orphans and they
cannot be used directly.
If you have a tool for example for
invoice lines and that's it,
then you really need the ID without
which the agent cannot work. And so we
add some of this additional metadata
that makes it aware to the agent that if
you want to use invoice lines, use this
tool first.
>> And it's actually the same problem as
you've had with OData before, where you
could take a page, expose it as an OData
endpoint, and it wouldn't work because
it required the header information for
it to work.
So, here we've just added it to the
information so that the LLM knows that
it shouldn't use this directly.
>> The next thing we [snorts] did was
embedded resources, which is something I
mentioned just a few slides ago.
The idea is very simple. We're adding
support for API queries, and that means
your agents can now return more data.
Do we really want to return this data as
a text block and then have the agent
do maths in an LLM finally? We don't
want that.
So, what embedded resources allow us to
do, especially in context of Copilot
Studio, is
when the result is returned as an
embedded resource, it's returned as a
file reference. And so, the only thing
that goes into the context of the model
is just a file reference, not the
entirety of, let's say, 5 MB of data
that you just ended up returning.
And what the agent can do now is it can
take the file, take the file reference,
pass it to a Python code execution tool,
and every and all the heavy lifting of
any data analysis is then done on the
Python tool, which is also part of the
Copilot Studio, which is
solving a big problem for us. So, all
the real work happens in Python, all the
data analysis happens in Python.
>> Yeah, so if if doing statistics on large
data things is your thing, then
unfortunately, actually, now your LLM
can do parts of that also on Business
Central data. So, no more fun with
standard deviation and variance, etc.
>> Exactly.
>> What you would like there.
Um
but it's a very good, and it wasn't a
coin- coincidence that you said 5 MB
Yeah.
>> Yeah.
>> to the best of my knowledge, because
that's
>> Yes, that is the limit, I think.
>> That is the current limit on resources,
whereas before, when we had to return
things in the text block, first of all,
it would fill up the context window, and
you would get nowhere near
the 5 megabyte limit.
>> I think some MCP clients do try to kind
of get out of this by just overflowing
the huge amount of data onto a file and
then trying to read it. But again, that
file is not really in a structured
format, so again, they do struggle
reading that file in our Python code
execution tool.
>> But these resources, as you mentioned
before, is usually where you might see
difference between MCP clients in how
they work is actually very often in how
they deal with resources.
>> Exactly. That's also a true point
because this file reference approach is
taken by Copilot Studio, and as far as I
know, VS Code also has this file
reference approach. It will create a
file,
but then that file is created as a
temporary file, and I think it would
require few more permissions to access
that using code execution tools, for
example.
>> All right.
So, let's talk about uh dynamic tools
because
just like we talked about files being in
the context window, actually the list of
tools also get added to your context
window, so there is a natural limit to
how many you can have.
So, let's talk about how the dynamic
tool mode works.
>> All right.
>> As you see here, he's the one knowing
all the things, right? I just leave it
over to him.
>> The problem that we're trying to solve
is most MCP clients hit a hard limit
when it comes to the number of tools.
Copilot Studio has a hard limit of 70
tools, and the moment you try to go and
add more tools, it just errors out, and
it will tell you that it can only use
the first 70 tools that it got.
Which is problematic, right? Especially
if you're building multiple agents or
you're having multiple connectors to
Copilot Studio as well,
it just doesn't scale.
So, what dynamic tool approach does is
when you're using the API as tools
approach, and you have enabled dynamic
tools,
we instead of returning the APIs as
tool, we return these three system tools
that you can see on the screen.
And then, your agents can use the search
tool to actually find the relevant APIs
that they are trying to
invoke or use.
They can use a describe tool to
understand how to use that API, and they
can use the invoke tool to just run it.
And that's the biggest advantage of
dynamic tools. And
with this approach, there is no limit to
the number of APIs that you can add in
your configuration because the search
tool also uses semantic metadata search.
But that also means that you need to go
to the feature management page and
enable semantic metadata indexing for
your metadata or your page objects.
>> This also means if you're running on
premise and you try to do some of this
on premise, you don't have the semantic
vectors.
>> Exactly.
>> There is no dynamic searching in
metadata. This is an online offering
only, which is why one of the reasons
why we only support the MCP server for
the online version.
>> One more thing I wanted to mention is
with the
dynamic tool mode,
you can also use feedback and create
better configurations. So you can, for
example, use the dynamic tool mode,
try to build scenarios, and try to use
the search tool to essentially collect
the set of APIs that you might need for
a particular use case.
Once you have the set of APIs, you can
use some CLI coding agent and tell it to
create a configuration file for your BC.
>> You You also have telemetry for the
tools that get called.
>> Exactly. We also have telemetry, so you
can use the telemetry. You can also just
run the dynamic tool mode,
let it discover the APIs, create a
configuration, and once you're sure that
the configuration has all the tools that
you need, you can create a static
configuration,
and take it from there.
>> And by the way, when you So there is the
static mode versus the dynamic mode. The
dynamic mode gives the LLM more freedom.
But that also basically requires the LLM
to think more.
>> And that's the gotcha here, right?
Because in static mode
agents can see all the tools that they
are trying to invoke. But in dynamic
tool mode, they really depend on your
instructions on what is it that they can
do.
So you have to have nice instructions,
you need to have necessary knowledge
files or something that tells the agent
that okay, these are the different
things that you can do.
And then the agent can use the search,
describe, and invoke operations to
actually carry out some of those tasks.
>> Yeah.
So basically, one way of building an
agent, run it in dynamic tool mode,
record which tools are being used, then
create a static tool definition with
exactly those tools. Now most likely you
can go to a cheaper model because you
didn't give it as much choice. The
moment you went from static, you said
you can only use do these 12 things.
Apparently they're good enough to answer
most of the questions. So now I don't
need the bells and whistles Claude Opus
4.8. Now I can run with something
cheaper.
>> Yes.
>> All right. We talked about
configurations quite a bit.
So um let's take a look at what you can
set up in the configuration page.
That's the page where you govern what
the external agents can do.
You set up whether it's active. You can
unblock the edit tools. Basically
saying, do you want any MCP external MCP
to access this?
Um
and then you turn on the
Well, instead of talking about this,
let's just see it.
>> Yeah, let's take a look at the
configuration page. I'm just going to
switch to my Business Central.
>> And I'm going to switch to your monitor.
>> Perfect. Yes, so to find the
configuration page, let's just go to the
main screen.
To find the configuration page, search
for MCP.
And that's the MCP configuration page.
And as you can see, I have number of
configurations. All of them are active,
which essentially means you can have
multiple agents connected to different
configurations, and each configuration
will give them tools that are specific
or scoped within the configuration.
Now, in my case, let's take a look at
the audit APIs that were powering the
agent that we saw previously. Right?
Here, you can see
First of all, if you have been using
MCP, you'll notice the UI has changed a
bit. We have multiple server features.
We have a API tools approach, which is
what I mentioned where your published
APIs become tools.
And here, you can see the list of all
the APIs that are currently part of this
configuration.
Now, if you want to use dynamic tool
mode, all you need to do is go to
dynamic tool mode here.
Oh, first of all, before making any
changes to the configuration, you need
to disable it. When you disable it, any
agent that might be using this
configuration will start to fail, so
something to keep in mind. Or, you can
use the copy action, create a new copy
of this current configuration, and then
make changes there for testing purposes.
>> around with that, and then when you're
done, then you actually modify the
original one instead of hurting all the
other customers or all the other clients
meantime.
>> So, in this case, I don't care about
anyone else, so I'm just going to
deactivate this one, and you can
activate dynamic tool mode.
When you activate dynamic tool mode, you
can see on the right side, these are the
three system tools that are being
exposed from Business Central.
Finally, we have also made it very
simple to share configurations.
>> Mhm.
>> All you need to do is
>> That's how I, as a manager, build
configurations. I ask Purushottam to do
it, and then just send it to me.
>> Exactly.
And so, all you need to do is select one
of these options here. You can export
the configuration, and if someone has
provided you one, you can also import.
So, in this case,
my manager
my other manager
provided me a configuration for audit
tools as well, and it's kind of named
the same as the one I have already.
But you can see how easy it is to import
configurations, right?
We also have necessary validations. So,
in case I try to activate the
configuration and it has issues.
>> So, it was probably made by me, the
manager who doesn't know how to make the
configurations.
>> And that is why there are some issues in
this configuration. And so, we
automatically figure out what those
issues are. It could be because you're
using API pages or queries that are not
really installed on your system. It
could be that you are using an invoice
line tool, but you do not have a sales
line
sales invoice tool, which is a parent
tool.
We check a number of things. And all you
need to do is
look at the recommended action and just
apply the recommended action. And that's
it. Your configuration should be fine.
You can activate it and start using it.
That's it.
>> Yep.
>> Finally, you can also just
>> Oh, sorry.
>> No, no, I mean
>> Yeah, go ahead.
>> I think
Yeah, okay. So, the finally, you can
also
Are we still Yes.
>> Yeah.
I just confused you there. Sorry.
>> Yeah, okay. So, you can also use the
connection string. This is what we'll
also use for one of the next demos that
is coming up.
Take the connection string. Since VS
Code is pre-authorized, you can just set
it up there. And if you have cloud code
or
GitHub Copilot CLI, I already showed you
in one of the previous slides how to set
that up.
Perfect. Let's switch to
>> Let's switch back.
>> Yes.
>> Yeah. So, this is just a recap that you
can export, etc. We're not
But
what if the crystal ball is a little
foggy? You cannot see what questions
this agent will get.
Pages and queries aren't enough because
you don't have the API page that returns
the data that you need for this
question.
Or you need a different aggregation that
you had built in the query. Somehow your
divine insight in what would be needed
three months down the line failed.
>> It's I think it's also difficult because
most of these chat systems they are
open-ended, right? They give users this
empty pane and they expect that the
users can type anything. So, it's also
very difficult to restrict them to just
certain API pages or API queries.
And so, for generic data analysis or
data Q&A scenarios,
we have a new MCP tool set, which is a
data query MCP.
As you can see, we have a set of new
tools. And these new tools that can be
used by agents for finding Business
Central tables,
traversing the table graph essentially,
how one table is connected to the other
table, getting the fields from the table
using the table schema tool.
And once they have collected all the
necessary context, they can start
compiling queries and they can start
executing queries directly
on Business Central.
>> Yeah, and I just want to mention that I
was saying we have the new one.
This is still
not shipped.
>> Yeah.
>> This is
working locally.
It's not available yet, but we wanted to
give you a sneak peek of where we're
actually taking this. So, don't blog
about this as this is something you can
do already with the MCP. This is a sneak
peek into the future.
>> Yes.
So, let me switch to my screen and let's
try out one demo that I have here. So,
it was number two.
Okay. So, right where I left off,
this is the connection string from the
data query configuration. I'll quickly
show you what the configuration looks
like.
It's straightforward. There is no API or
available API section because API tools
MCP server feature is disabled.
The only thing enabled is the data query
tools, which is
not really in preview, but it's coming
to preview.
So, you get the connection string.
And once you have the connection string,
I'm just going to go and set it up in VS
Code.
So, in VS Code, you can find the
mcp.json and just paste the connection
string there.
And that's it.
Now, we let the agent
or we let the MCP server start.
Once it starts, you can see that it has
discovered five tools, and we can also
take a look at the tools that are being
exposed from this configuration.
Perfect. And now, let's try one of the
queries here, which is
So, this is also a good example because
if I if I just give you this query, it's
very difficult to figure out what API
pages or queries are needed to support
this.
But it's a lot easier when you have
these generic data query MCP tools.
So, the agent starts by trying to find
the relevant tables. We can also just
take a look at what it did.
It tries to find the value entry, sales
invoice, sales person, and multiple
tables, and it gets some of these tables
from the tools. Perfect.
And then, it tries to get the table
schema just to understand what fields
are available. So, in this case,
from table number 27, it tries to find
all the tables that have a number, a
description, item category, or something
of this sort.
Perfect.
Once it's done, it's going to start
designing an AL query,
as you can see.
And let's just let it work.
But while it's doing its thing, we can
also just go to one of the previous
executions right here.
So, as you can see, it tries to find
tables, it tries to get the query schema
from different tables.
Once it's confident and it has gathered
enough context, it compiles a query. And
this is what the query looks like. And
you'll notice this is just AL query.
Right? This is a AL query, a short-lived
AL query. This is not published to your
environment. It's a dynamic query. It
gets created, it gets destroyed.
And that's it, right?
The AL query is created, it's compiled,
and now the agent can just execute the
AL query, and it gets the results.
Just like before, the agent can choose
to ask for results in a resource or an
embedded resource. Otherwise, it can ask
the results in a normal text file. And
in this case, it just did that.
>> Isn't this just cool?
You now have something that can
get to your Business Central data.
>> In a very generic way.
>> Now,
small caveats with this.
For this to be successful, you generally
need to use one of the better models
because it has access to a lot of
information, etc. So, again, the trick
from before applies.
You can actually run this, and then you
we will add telemetry. This is still in
preview. We haven't done all of this
about which queries it generated.
Then maybe it's a good idea to build
that query.
And then add it to a static tool, and
now suddenly you can run this using GPT
4.1 or something much cheaper because
you could see that this is actually the
queries that are needed to answer the
Yiannis' questions whenever I get around
to play to ask the agent. So, think
about how you can optimize this. There
is
you should expect an optimization of
agents and an optimization of cost of
agents using using some of these tools
to burn just a few
fewer some fewer tokens.
>> Yeah.
>> But of course, at some point, the models
also might become so cheap it's
irrelevant. But let's see about that.
>> one thing also I wanted to add is
the Cloud Opus 4.8 is a great model,
right? And like Yiannis mentioned, we
also want these things to also work with
all the models. It It does work with all
the models as well, but it really does
depend on how good the model is when it
comes to writing AL queries. But you can
help the model. You can also connect,
for example, the MS Learn MCP server,
which has a very large number of code
samples, AL queries, how to write AL
queries, and so many documentations. And
your instructions for whichever MCP host
you ended up using, the instructions can
advise your agents that if you are
failing at compiling a query, just go
and learn how to do that from MS Learn
MCP.
But, at the same time, we are also
working on some other things that we'll
talk about in just a couple slides,
which are also going to improve this
pilot in future.
>> Yeah, and I I also want to comment a
little on
the permissions. Now, if you open up for
the query tool, which we will ship in
preview at some point in time, yes, you
are opening up for a lot of tables, but
the permissions still apply. You still
need those direct permissions, and for
starters, we only allow reading.
Well, we're never going to allow our
writing directly to tables anyway,
but but do be mindful about that when
you get there. But, the permission
system will guard you in exactly the
same way as it guards you elsewhere in
the product.
>> There's also Now, the whole MCP is now
moving to a more agentic approach here,
right? You're not defining tools, you're
not defining specific
APIs. Instead, you're letting the agent
explore the table graph, figure out what
it needs, and writing these dynamic
queries. And I think it's a very
powerful
>> And then you can even later think of
Now, you've run this agent for a while.
You ask the agent to now look at the
telemetry, find the most common query.
If you also access the AL MCP, then it
can also generate the query for you,
upload it,
then you add it to a configuration.
>> And then it becomes an API query, and
you can make it a static tool list
again. It's very powerful.
But, not sorry.
>> All right. So, we also have
to address a little bit the elephant in
the room
because we've been talking about agents
inside Business Central.
You know, the sales or accounts payable
payable agents. We're also talking about
external agents MCP.
So,
does this mean I shouldn't do one or
does this mean I shouldn't do the other?
Well, they're actually targeting quite
different scenarios and there are pros
and cons to both.
The external agents are
external.
Surprise.
Um
>> [laughter]
>> so, there is less control
and they can run in any host.
Now, this is a very good choice if you
want these generic or these agents that
can talk to multiple systems. If you
need it to talk to a billing system,
ticket reservation system, and also get
some information from Business Central.
Well, you don't really It's actually
easier to build it externally and call
get the data from him from Business
Central rather than running it inside
um Business Central and now having to
build something that calls out
to the other one.
And it can be published to multiple
channels and I'm sure that our good
friends will show some of that later.
Um but there are also
some strong advantages to to agents
inside Business Central.
>> I think the biggest advantage for
internal agents is that they have access
to the entirety of Business Central UI.
So, think of it like this. If it's If
it's something that a user can do with
the Business Central website, then that
agent can do as well, right? And it's
only going to get better and better as
we get better and better and more
complex models.
We have also done a lot of work to make
sure that as you're interacting with
that agent, it's it's immediately
obvious to you what is happening, what
stage you are at the process. And if the
agent needs help, you also have a lot of
mechanisms to just help out and nudge
the agent in the right direction.
Finally, we have a dedicated agent user,
which is not something you get with
external agents. External agents run as
your own user or as your own permission.
>> you set up the system just like earlier
where we saw super for for each other.
It's actually nice that there is this
agent user to funnel the permission
through as well. Because you need the
intersect between the two. Yes.
>> It's the intersect of the agent
permissions and the permissions that you
have. So, it's again, it's a safe way to
run agents within Business Central. And
finally, the difference is also in the
billing model that you have for external
agents and for internal agents.
>> And that, I guess, with whatever is
cheapest, that depends on each scenario.
I we can't really say which one, but
it's at least different. Um so, rule of
thumb,
inside for DBU native workflows that
work through the UI, MCP for the ones
where you either need the external
orchestrator or need to talk to multiple
systems.
>> Exactly.
>> So, this slide was actually originally a
little more fun or it had two parts
because we actually planned to only just
mention the AL query MCP here, but we
decided that we could pull it in because
it's Yeah, it's so close and it's
actually running.
>> also kind of close to getting to preview
state, right? And we figured we should
just talk about it and also show some
demo.
But again, we are working on a dedicated
Business Central MCP repo, which we
think can host skills
and relevant documentation, essentially
that allows you to build better agents
with the Business Central MCP.
And that's all I can say for now.
>> Yeah, so you'll get help in how to to
build the agents, get help in which
skills are useful to add, etc.
>> Exactly.
>> So,
you can start today.
You can point an agent at your
APIs. You can publish your API page
query, you can configure it, you can
connect and you just ship it.
>> Probably do some evaluation for the
agent as well.
I think Copilot Studio allows you to
evaluate your agents and then ship it.
>> And manage it. Ship it.
Yes.
>> Question and answers.
>> Yes.
So,
>> We have the Yes, I think we
>> Oh, and and we can't start the question
and Now we can start the question and
answers. So, let's see who I actually
end up
getting to.
>> Hello.
>> Yes.
>> My question is the the dynamic
tool in the page now can discover also
the queries or not?
>> Yes, it can discover API pages and API
queries. Yes.
>> Thank you.
>> And and of course you need to enable the
dynamic tools if in order for it to be
able to discover them.
>> One more thing, also enable indexing
from the feature management page. You
need to enable the semantic metadata
indexing.
And then the dynamic tool mode will
work.
Yes, because otherwise it will use
keyword based search which is not that
great.
And ideally you want to be able to use
metadata embedding search.
>> So, in the that's in the when you create
the the query, you need to to put the
description also in the
>> About text.
>> Yes, yes, exactly. Yeah.
>> I just want to to this one. Can we also
do APIs on the code unit or is it just
pages and data queries?
>> So,
So, let me answer it like this. It is
queries and API pages for now.
>> Okay, for now. And the second question
is about the costs.
Uh so, how do we know how much is this
going to cost? How can we for example,
for the development team test this? Uh
>> So,
if you look at what this costs, it's
Well, this is the nice thing about this
is the next external agent. That's not
our problem. No.
Uh if you look at what actually happens
on the MCP side, we are routing the
call. We're not in control of how much
reasoning that goes on outside it.
So,
so yes, this might seem like I'm just
trying to weasel out of this question.
But, that's actually why we mentioned
this. Well,
use the more dynamic ways of doing this
in the beginning to build your agent,
then dumb it down so that you now
achieve much lower costs. Because that
way you can get to a cheaper model. It
doesn't have to go back and forth and
try as much because Well, if you only
give it seven things to do, then it has
a pretty good chance of picking the
right thing to do the first time rather
than having to try something else and
burning tokens.
>> I think it's important to iterate over
the models that you have selected, your
instructions that you have provided to
your agents. Because that's how you
figure out, do I really need to use
Claude Fable to perform operations,
right? Or is GPT 5.2 chat is good
enough?
And that's only [snorts] way to support
cost here. Yeah.
>> I'm getting pretty good at that try.
>> I have a question. So, I expose 30
fields to my agent. And when I was
asking for my agent you need to retrieve
data from all the fields.
And it was just retrieving only six to
10 fields. Even I was expli-
>> Can you Can you repeat the question
again?
>> So, my question is that I created a page
API and I exposed
by them MPC server and then I was asking
for my agent you need to bring the data
for the all the fields of my API page,
but it was retrieving only the data for
six to seven fields and I was not able
to figure it out
what is the issue and how I can debug.
>> Yeah, so I think we have seen these
issues, especially when we are using
different models, right? The way around
it is instructions and changing the
model. Essentially, what is happening is
during the orchestration, you're
provided some data, you're provided some
context, and now it's the agent's job to
see, "Okay, this is a tool that's
available. These are the required
parameters on the tool, so I need to
fill in all this information to make the
tool work."
Sometimes the models just don't do that.
We've had a lot of trouble, for example,
with dynamic tool mode when we were
trying to initially use it with GPT 4.1
because every time there's a required
parameter, Copilot Studio will just say,
"What is the required parameter?"
Directly, it will ask the user instead
of actually putting it in itself.
Which was annoying because dynamic tool
mode, for example, has a action type
when it's searching for different APIs.
And sometimes the agent will just say,
"Please provide me the action type."
That's not useful for us as users.
>> And second question is that can I debug?
>> Uh
>> Yeah, so we have telemetry already,
which is the normal app insights
telemetry. So, every time a tool
invocation happens, you should be
getting the right telemetry that, "Okay,
this tool was called or this tool was
called."
And I think we are also improving on the
telemetry little by little because it's
still kind of a new feature and we are
adding more features.
But yeah, we are adding more telemetry.
So, if something is missing,
just create a post on Yammer or what's
the new one?
>> Viva Engage.
>> Viva Engage and we'll get it done.
>> Okay.
>> Yeah. So, we'll have
one last question. Let's see if I can
throw it all the way up there.
>> Nice throw.
>> [laughter]
>> Um I noticed in the
connection string you have to specify
the company name.
Um
the configuration that you set up, the
MCP configuration, is that shared across
companies or is it in a company? And
wouldn't it be a better idea if you do
not have to specify the company name in
the connection string, but it would be
part of the prompt?
>> One of the things that we are
>> Yes. So, so this is a constant
debate. There are pros and cons to both.
Um there is the when you give more
choice to the LLM, it can start running
in a different
company, etc. But we are looking at how
we can do some of this because
in real life scenarios, it's very often
within the same company. Now, there are
scenarios where it's across companies,
etc. So, we need to strike a balance
between those two, but we are looking at
how we can loosen the requirement for
company.
>> So, very small background I can give is
MCP protocol itself is changing. Before
MCP was supposed to be stateful,
now in the future or the new
specifications, they're not going to be
stateful. So, essentially you cannot
have a tool that says set company and
then all the subsequent tool calls are
now going to that.
So, maybe we need a company parameter in
all the tools. Maybe we need a separate
different approach. We are still
exploring.
>> The
the configuration itself, the MCP groups
that you create in Business Central, are
they per company or
are they across companies?
>> I don't remember.
>> Yeah, I don't know.
>> Because APIs APIs are across companies.
>> Yeah.
>> Right? But now you're configuring it. It
would make sense if you have them across
companies.
>> Yeah.
>> Then only the connection string is
required to support multiple companies.
>> I do believe that they are actually
shared. That's why I said
>> per company now, basically.
>> But I'll have to double-check.
>> Yes.
>> And with that, I guess we will leave it
over.
Nice catch. Nice throw there.
Thank you. So with this, we're going to
round up the MCP session.
