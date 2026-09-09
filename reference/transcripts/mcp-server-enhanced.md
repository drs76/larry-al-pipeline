# Transcript — What's new: Enhanced MCP Server

- **Source:** https://youtu.be/0WAOtNaKjws
- **Channel:** Microsoft Dynamics 365 Business Central (official)
- **Ingested:** 2026-07-06 (auto-captions, cleaned)

---

[music]
>> Welcome to this 2026 release wave one of
Business Central, the launch edition.
This session is about enhanced MCP
server. My name is Kenny Pontoppidan and
with me I have Poorshad. My name is
Poorshad Dwivedi. I'm an engineer with
the runtime team at Business Central and
we have been working on MCP.
And I am super super super delighted to
see Poorshad in this session. He will do
a lot of cool demos and we are really
looking forward to showing that.
The reason we invest in business in in
MCP server is to allow you to create the
flexible agentic workflows that you need
for your business.
Uh with MCP it would be external agents
and we want them to be configurable, of
course secure and something you can
monitor their
the usage of them
and bring the agents to your company to
support your business.
Now in this session we're going to start
with configuration validations all the
way down to using something cool in new
thing in MCP, which is called resources.
So stay stay tuned for Poorshad's demo
on that.
So the first topic is MCP configuration
validations. So uh the things you save
in metadata for configurations can get
out of sync with the actual metadata in
the system. For instance, you might add
API pages or queries later, API pages to
your configuration and then someone
uninstalls an app and this API is no
longer present. For that uh we are here
adding a validations to MCP
configuration so you can validate
whether this configuration is still
valid. But that's that's that's kind of
true errors. Another thing that is can
be very helpful is APIs work in this
this sense that you have like a main API
and then
APIs where you navigate through. For
instance, if you have a sales header and
a sales line, two different APIs,
you in Business Central you kind of need
to navigate to the lines from the
header.
So the validations also help you with
warnings. In this case, we have an API
added to the configuration where the
parent API is is missing and that would
give a hard time for the user of the
agent
uh MCP host that is using the MCP
configuration cuz it it it kind of
cannot navigate the right way. So these
warnings should probably be solved so
that this configuration is more useful
for the agent. And we also have an apply
recommended action and it does it
automatically for you.
Yes.
Another piece of feedback we got was
that um it would be nice to be able to
transfer configurations between
environments. So we added this import
export these two actions. You can export
a configuration on one environment, get
a JSON and import it in another
environment using the import action. So
that allows you to work on tests
environments with configurations and
then move them to pre-production and
production environments. Do that in a
safe deployment manner.
Another big thing is that we are
supporting
um other MCP hosts than Microsoft
Copilot Studio. Other hosts would be in
public preview and not kind of fully
supported. Well, they they work, but
Microsoft Copilot Studio is the is the
supported MCP host for now.
Um so the S the other other MCP host
would be in public preview. Um
Uh we have already Visual Studio Code
and Copilot Studio pre-authorized with
authorization. If you have other MCP
hosts, you might need to do additional
setup.
Such as registering an intra application
so that author authorization also works.
But instead of me talking about it,
maybe we should have Poorshad demo some
of these new cool cool things.
>> Yeah, so I think it's going to be very
easy for you to just set up a new MCP
client to use with Business Central. So
you already have seen the configuration
page and you can probably also see that
we have made a ton of improvements so
that it's easier for people to use.
But now there's also a new section under
advanced called connection string
which gives you the exact thing you need
to paste on a number of MCP clients,
whether it's cloud or whether it's VS
Code. So in this case what I'm going to
do is I'm just going to take this
and we'll just paste it to VS Code. And
as as Kenny already mentioned,
VS Code is already pre-authorized. So
you don't need to do anything for VS
Code. So essentially
just copy the connection string, you
will get a prompt to log in.
The MCP can see 11 tools here and that's
it. It's incredibly easy to now set up
new MCP clients to use with Business
Central.
Cool.
So
that's one of our like main improvements
in this release wave. Let's go back and
talk about telemetry and auditing.
So we have in Business Central
uh kind of this
dogma that we want to have uh anything
related to administrative changes must
be something we want to log to Microsoft
per view as as an auditable event. So we
have done that. Any MCP configuration
changes will be logged to Microsoft
audit
per view logs.
As well as normal telemetry on
configuration changes, but also MCP
calls. So
uh for just like you have incoming web
service calls where you have telemetry
on that, you now also have partner
telemetry on incoming MCP calls, both
the ones that succeed and the ones that
fail. And this allows you just with any
other telemetry instrumentation to
monitor and analyze the health of your
agents using MCP server. Maybe there are
certain MCP calls that fail. You can use
this telemetry to understand why.
Uh might need to tweak some
instructions. You might need to tweak
things
on on the API level in Business Central.
Uh but now you have observability into
into these failures and of course for
succeeded calls that means that you also
have an idea of the usage of MCP server
in in different MCP hosts. We will log
the type of host as well.
Not just such some hosts where we don't
exactly can trust the header. So uh so
it might be that that we can only trust
what is in the HTTP header. Whether it
but but the
kind of the supported or Microsoft
provided host we do know. So we log
actually log the type of MCP host to to
the telemetry, whether it's Microsoft
Copilot uh or others.
If you want to know more about the
telemetry part, just go to our normal
telemetry documentation
aka.ms/bctelemetry.
One of the other main features of MCP
server for this release wave is the the
support for resources. So resources was
added to to MCP protocol some months ago
and MCP our MCP server now supports
this. Having resources enabled uh will
allow MCP hosts that understand
resources to to do incredible things.
One of the examples could be that in
Microsoft Copilot can now use code
execution on the MCP host side, not on
the Business Central side, to do things
and Poorshad will show you an example of
that here. Yeah, MCP resource or in our
case we are supporting embedded
resources with our Business Central MCP.
And one of the main advantages of this
is, unlike your normal use of MCP, it
does not return text content block with
a large amount of data because that's a
problem. If an MCP server returns a
large amount of data, it gets added to
the model's context and that means each
subsequent call that you made from your
MCP client is going to be a bit more
expensive and it also affects the
accuracy of the models themselves.
Right? And so when you're using embedded
resources, or at least the way we have
implemented it is all the list tools
where you return a lot of data,
instead of returning just the text
content, you return an embedded file,
right? And the file is it's great
because you can just pass it to code
execution tools and they do the heavy
lifting of any sort of data analysis
that you want to achieve, right? And
Poorshad, I mean, when you talk about
the I mean, all of this is happening on
the MCP host, not on the Business
Central side of things. Exactly. So it's
it's it's a very nice design because now
you can create an agent that can go to
multiple different APIs that we already
exposing from our configuration, return
the data as file references and then
just pass all of those file references
to the code execution tool to do more
detailed analysis and structured
analysis, which was not possible before.
And I think this is this is super cool
because for instance,
Microsoft Copilot have Python
interpreters and all of that. So that's
not part of normal Business Central,
probably still something we wouldn't do
for security reasons, but now the MCP
host can also reason and have code
reason over the data that is uh sent
over from Business Central. Yeah. To get
started, all you need to do is open your
bot or existing bot that you already
have and go to settings and enable the
code interpreter.
And now let's just go through one of the
simple examples.
So in this example, I've simply asked
Business Central to, you know, give me a
distribution of customers by their
sales.
And you'll see when the data is returned
from Business Central,
the data is not directly added to the
model's context. Instead, the only thing
we add only thing that MCS adds is a
file reference, which is great for
context and that means you can return a
large amount of data and only a file
reference is the thing that gets added.
Right?
And as you can see,
different file references are then
passed to the Python code execution
tool, which can do a lot more detailed
analysis and even create
different visualizations from your data.
Yeah, it would be a super interesting to
see the use of this in the wild. We we
can only imagine some scenarios, but you
guys work with customers and with with
like your scenarios, so
we're looking forward to hearing about
what you do with this powerful tool.
Yeah.
And now if you just compare, let's say,
you know, with and without embedded
resources.
First of all, embedded resources are
optional, right? So if you have already
an existing MCP server MCP
implementation, it does not break that.
The only change here is that now if the
agent feels like it wants to return more
amount of data and the code execution
tools are enabled, it can set the result
format in the calls or the tool
invocations that it makes to return the
data as a resource file. And that means
you can handle larger amounts of data,
you can create more complex agents that
can do more data analysis.
Whereas without resources, it's going to
behave exactly how it was before, right?
You the LLM ingests the data directly
and it it's it's still great for I think
answering direct questions.
But again, if you want to do more
structured detailed analysis with your
data from different sources, I think
resources are a game-changer.
I think so, too. Let's see.
If you want to learn more
about MCP server as such, remember that
we added introductory intermediate
videos back in January 2026 and you can
find all of those from our YouTube
channel aka.ms/bcyoutube.
So might want to also watch these in
together with with the new video we have
here.
In general, if you want to learn more
about MCP server in the Business
Central, the aka.ms/bcmcp
is your friend. This is where we
document the landing page for the
documentation of the server.
And just for fun,
if you're working with MCP servers, if
you want also your agents to be to be
able to know about Business Central
functionality, you could consider adding
the MC Microsoft Learn MCP server to
your
list of of MCP servers. That would allow
the agent to like explore what Business
Central can do and maybe that can can in
some cases for some types of agents
also be helping.
If you like this session, it might be
related sessions that could be of
interest for you as well. APIs for
permissions, approvals, and documents
are relevant for this because our MCP
server speaks API. So these new, I think
almost 50 new APIs will just increase
the surface area of what types of agents
you can do.
And MCP server lives inside the server,
so the what's new in server and database
session could also be something where
you want to learn more, not only about
our investments in MCP server, but in
general in the Business Central runtime
and database.
Now if you already know if you don't
know the general Business Central
resources, stay on for a few more
minutes and just watch the rest. If you
already know this, then it's time to say
goodbye for me and for Poursh because
our Business Central launch edition for
MCP server is over.
Have a great day and a great launch
edition. Thank you. Bye.
We have compiled a number of general
resources that we believe are key both
for partners, but also Business Central
customers. Most Some of you are partner,
some of them are also for customers. So
the first one is
called aka.ms/bcall. [snorts]
This is a partner resource for that
contains lists of every other aka link
that is needed for you to understand
anything about both the Business Central
product, but also processes around it.
We call these aka links because they're
called aka.ms and then for forward slash
something. And with Business Central
links, we all always prefix with BC and
then something.
The next one is our partner network
social media for for Business Central
partners, Viva Viva Engage. So
aka.ms/bcvivaengage
is where you go and interact with other
partners. It's not open for customers,
so this is where you can ask questions,
interact with the product group,
interact with with with each other
in a in a closed network.
Second link third link is for both
partners and customers. We are called
office hours. So office hours is
something we do once or twice a month
from the product group engaging with the
community about new features or things
we want to discuss. aka.ms/bcofficehours
is the is the place where you go to find
out about upcoming events.
These are recorded. I believe the
recordings are available only to
partners, but the live events are
available also to customers as well.
Fourth link is YouTube, our YouTube
channel. I'll talk about that
in the next slide and LinkedIn in the
next slide.
And then finally for for Microsoft
partners,
the BC's aka.ms/bcpartnerportal
is where you get
a lot of the resources as a partner such
as compete decks,
pitch decks, and a lot of other
resources.
For LinkedIn, this is our product
group's LinkedIn profile. We have 30K or
more followers, so both partners and
customers. This is the place where we
from the product group put in news and
small bits of information outside the
{quote} official channel. So follow us
on LinkedIn to learn what's happening
right now
in in this around the product.
And then
also on our YouTube channel where this
is where you're probably watching this
aka.ms/bcyoutube.
We put in not only these launch editions
twice a year, but also
Copilot and AI video shorts, tips and
tricks, technical deep dives, under the
hood.
We even have this what's cooking where
we put little nuggets of of videos out
for new features that are even coming in
on the YouTube channel before they're
coming in the release notes. So watch
and maybe bookmark us on YouTube. And
also notice all the playlists, so
the content is also organized in areas,
not only all the videos. So if you have
an area that has special interest such
as analytics,
you can find an
a playlist and kind of see all the
content related to that.
And that's it. That is truly it. We
won't
there will be no more, so thank you for
watching all the way to the end. And
again, have a great day. Thank you.