# Transcript — MCP Server for Business Central - Advanced topics

- **Source:** https://youtu.be/C5cmG3sNjUg
- **Channel:** Microsoft Dynamics 365 Business Central (official)
- **Ingested:** 2026-07-06 (auto-captions, cleaned)

---

[music]
Welcome to this part three in our series
about our new MCP server for Business
Central. This one is on advanced topics.
The other videos, you can find links to
them down in the description. So, make
sure that you watch them before this one
or we encourage you to. My name is Kenny
Pontopidan. I'm a program manager in the
Business Central team. And with me I
have Yen Smaller Peterson.
>> I'm the engineering manager in the
runtime team and my team is currently
building the MCP server for Business
Central.
>> So the prerequisites for this video if
you don't want to watch the other ones
first you need to enable the MCP server.
It's currently in public preview. So go
to um feature management and enable
that. and then know uh you also need to
kind of know what's behind the default
configuration in MCP as well as named
configurations. Uh so that's the
prerequisite we expect you to know about
for this video.
>> And both of these concepts are covered
in the other two videos. All right. So
let's talk a little about what MCP
actually does. So it you create an agent
which talks to business central through
an MCP connector which then talks to the
MCP server and currently the MCP server
exposes all the built-in APIs for data.
You can also add your custom APIs. So
your functionality is also available
with the preview version of the MCP
server. And right now when we talk about
APIs, we mean API pages. We might open
up for API queries in the future. So
stay in tuned for that.
Yes. So let's take a look at how it
looks different when you are running
with the default configuration versus
when you're running with a name
configuration. So here I have opened
copilot studio and have created an agent
with the elegant name of agent default
because it uses the default
configuration. Now when you connect to
business central
then it effectively only has these three
tools available the action search
describe and invoke but it is still able
to answer a question like do I have any
customers because it looks for an action
which can list the customers and hence
can find them. Now if we look at what
happens if we specify a configuration. I
have another one here
where I have created a specific
configuration.
And when you look at the tool list here,
you can now see that there are a number
of specific tools in here for listing
items, listing inventory postings with
the descriptions. So now it does not
need to search for the tools first and
it can then find the tools directly by
looking into the tool list.
However, there is a limit to how many
tools you can have which is why we have
introduced the um dynamic tools system.
Let's go back to the slide where you can
see a repeat of uh the dynamic tools
available. the search, describe, and
invoke. But let's take a look at how
these actually work a little more in
detail. So when you're using the dynamic
tool mode, then the MCP client will pass
keywords to the BC actions search tool.
This will do semantic search to find the
top X relevant tools.
Based on this list, the language model
will then call describe for the tools
that it considers using.
This action will return the full
description of this tool and whatever
fields are available. Now, in this case,
the tools are API pages. So, it'll
return the names and types of the fields
in your API page. Based on this
information, the MCP client or actually
the large language model calls BC
actions invoke and passing in any
filters and then Business Central will
return data from the API page and it's
basically just communicating back and
forth using the O data protocol because
in the tools description, the LLM was
instructed to use an O data syntax to
filter and find records.
Now you saw earlier that there were some
tool descriptions for the API pages when
you had the specific configuration.
Now when you list the tools you will see
a name. This name needs to be unique
which is why we have appended the the
object type and the ID. And then the
first part basically states what is this
tool doing in this case list job q log
entries and then there is a description
of it and it also includes the about
text for an API page. This is what you
get in the original list. Then when you
call the describe then it adds extra
information about the fields.
Each field will have its type etc. And
it also contains the instructions on the
O data constructs which
O data um parameters you can pass filter
select etc. So this is important for the
language model to be able to find the
right tool is that you expose the fields
you want and that you have a good about
text. So Kenny talk us a little through
how you can make your APIs even better
as tools. Yeah, because you probably
also have custom APIs and we generate
about text for our API pages which is
interesting, right? About text came as
something that was used in teaching
tips. Actually, when you think of
teaching tips and about text, this is
where you see things in advance tell me
or in the help pane or as teaching tips
on pages. But now they are also present
on API pages. And API pages have no UI.
But we're still using a about text. And
that's what you can also do at about
title and about text properties to your
API objects. This will allow any agent
to reason better over what your APIs are
able to do.
And normally
as humans, we don't like long detailed
texts. Actually, the LLM doesn't mind
that much. So, you can be quite specific
in your about text for your API pages.
So, when should you use which type of uh
tool? So static tools, specific APIs is
probably where you have well-defined
business processes where you want to
create an agent that that is limited to
something and you know exactly what this
something is. Contrast that to dynamic
tools where the agent is likely more
exploratory. It it might even be a chat
experience. So in that case you maybe
you don't want to lock at least
exploring data down to something
specific but actually want that broad
experience. Um and as we mentioned in
previous videos or and in this one you
can either set the dynamic tools like
specifically in the default or you can
enable that if you have a number of APIs
exposed you can also enable
discoverability for more readonly APIs.
>> Yes. And and when you set this
discover additional objects,
remember you're not necessarily making
it easier for the language model. You're
giving it more choices. So it has a
larger probability of getting things
wrong. For instance, in the it the
discover additional object allows it to
find all API pages. you may want to
limit it to the API v2 um APIs or if you
have some APIs you don't really want to
be used anymore, you're better off doing
a static tool where you remove those
APIs.
Now that leads also to both the
confusion but also um the the context
size. If if you have a lot of tools
available that fills up the model's
context and uh that's also for
performance reasons maybe you actually
want to limit the number of tools so
that the the model can easily reason and
and do it faster. And as we have said a
number of times different MCP hosts will
have different maximum number of tools
supported. Right now when we record this
video, Microsoft Copilot Studio is
around 70 tools. That of course uh will
likely change in the future. So this is
also one of the reasons why we
introduced MCP server configurations
from the get- go.
Yes. So when you are building your
agents, there are a number of things you
can do to make your agents more
successful.
First of all, you need to decide well
which tools are actually needed. It's
not necessarily that more tools are
better even though it can make a nice
demo. Look, it can also do this but in
the end it might end up doing everything
not so well. So you can limit the
available tools and you can create good
descriptions of tools. Now, it might
seem like a big task to have to create
descriptions of all your API pages
because you haven't you most likely
don't have them by by now. But this is
actually a place where
an AI can also help you by feeding in
the fields etc your documentation. You
can actually get an LLM to describe each
API page, what it does, and then you can
proofread it and add those as about
text.
>> Maybe. Yes, we should put a sample
prompt out on BC Tech.
>> Yeah, maybe we should make it easier.
Yeah,
>> at least that's actually how we built
the about text was this two-step
process. Get the first draft from a
language model, proofread it, and then
add it to the metadata.
Now also
in this video we haven't talked that
much about the instructions for your
agent because depending on the model it
may be good at O data constructs or not
or you might want it to guide it towards
certain tools. You can do this by adding
instructions to your agent. This is
particularly useful for either the
generic instructions.
There are some clients that have a hard
time remembering that you pass back the
forward link or the e tag when reading
more data or when modifying data. So,
usually when things don't work, try
tweaking with instructions. If that
doesn't work, then maybe your tools
descriptions aren't good enough and you
want to update those.
And then we have experienced that the
quality you get depends a lot on the
model you use that there is a difference
between the for one model the five model
etc. So I highly encourage you to
experiment with the models and find a
good tradeoff between the complexity of
the model and the quality of answers
>> and the costs and the performance as
well. It might be that you can go with a
small language model for some things
that's going to be cheaper and faster.
And for other types of agent work, you
need something that can reason uh
better, which would be more expensive
and probably take a longer time to
process um your requests.
>> And this is just an example of
instructions. Um probably not good. But
very often you would define the role.
You might add debug information while
you're working on it. having it explain
what it tries to do and you can also use
it to mitigate frequent issues. For
instance, here avoid putting dollar in
front of parameters and filters. But
actually what we are doing as a product
group is that we're monitoring the
standard things that LLMs get wrong when
you try it against Business Central and
we try to make the connector and
basically the MCP server lenient towards
those. So for instance, this avoid
putting dollar in front of parameters
and filters is actually no longer needed
as an instruction because we are
actually trying on the back end with a
dollar and without. Right? So the last
thing in the video is what if you want
to have other MCP hosts? C-Pilot studio
is the the the product where we started
the journey with with MCP server for
business central. But we also know that
there are other hosts out there and
maybe you want to run uh things in VS
code or other products. So right now and
this is going to change in the future
but right now you need to do some more
setup. Basically you need to set up a
proxy for the routing of requests and
also for the authentication. And right
now this is shipped as a sample code on
uh bct.
If you go to aka.ms/bct,
you go to the samples and then bcmcp
proxy, this is the current sample code
for that. And you need to set up that
proxy if you want to experiment with
other clients. But hopefully this all of
this will be much simpler in the near
future where we are working on also
making sure that other MTP hosts can
authenticate and use MTP server. Yes,
we're actively working on this and we
expect to release an update in the near
future which will make the setup much
easier and remove the need for the MCP
proxy which is also why it is only a
sample. It is not something that we
expect to be a long-term part of our
business central product.
>> It's not a part of the product. It's a
sample.
>> It's not. Exactly.
>> Yes.
>> It's delivered as is.
>> Yeah. All right. So to wrap up, the
vision haven't even changed from video
one and video two. It's still the same.
>> That's a new thing for AI that things
don't change within half an hour.
>> Yes. Make all functionality available in
business central functional available to
AI and agents and of course do it in a
secure reliable way. In this video, I
think we have gone a lot more into
details what it means with Ry
reliability and best practices for MCP
server.
So that also means the call to action in
this video compared to the other two
everything is now in black.
>> And if we had five videos, we wouldn't
be able to fit in one screen.
>> True. That is true. Um, so call to
action is basically all of it. Set up a
test tenant, improve your MCP tools,
iterate, provide feedback both on social
media. If there's something that you
think maybe this is not working right
now in the public preview, engage with
us on Viva Engage. And if you want to
know how to do that, this is the just
the final parts. Um
there is a an aka link in the middle one
aka.ms/bcy
yammer. This is where you sign up for
viva engage. So if you were previously
on the Yama network, make sure that you
go there. If you're a partner and were
not part of the Yama network in the
past, make sure that you sign up for
Viva to make to be part of this
community around Business Central
partners. The first v video link here v
the first link aka.ms/bcall
is all resources for partners. So go
there if you can't find other AKA links.
And the third link is also important.
AKA.ms/BC
office hours. We're going to do an
office hour on MCP server in the
beginning of 2026 in January. So, make
sure you go to that URL and find the
sign up uh link for the team's meeting.
LinkedIn, make sure you follow the
product group here. This is where we
publish weekly news on what we're
working on and what's what's coming. And
YouTube is where we put videos like this
one on launch edition and others. Make
sure that you follow us there. For now,
this journey is over. Part three is
over.
Down here in the description, you find
links both to documentation, to the
other videos, uh sample code for MCP
server. And with that, uh we thank you
for going all the way to the end on MCP
server. um with Business Central. Thank
you so much. Thank you.