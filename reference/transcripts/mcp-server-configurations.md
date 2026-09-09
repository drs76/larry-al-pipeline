# Transcript — Introducing MCP Server Configurations for Business Central

- **Source:** https://youtu.be/GeT5E_f9A9Q
- **Channel:** Microsoft Dynamics 365 Business Central (official)
- **Ingested:** 2026-07-06 (auto-captions, cleaned)

---

[music]
Welcome to this part two of Business
Central MCP server. This one video is on
configurations. If you haven't watched
the first video, go to the description
here and check it out. That's a
prerequisite for this video. My name is
Kenny Ponabidan and I'm a program
manager in the Business Central team.
And with me I have Yen Smaller Peterson
>> and I'm the engineering manager in the
runtime team in Business Central and
we're currently building the MCP server
for Business Central. Right. So
prerequisites for this video if it is
that you must have enabled your MCP
server in public preview. That's under a
feature management flag. And we have
also covered in a previous video what
this default MCP config configuration is
and what it can do and the tools it has.
And in this video we are going to talk
more about named configurations if you
want to go beyond the default
and that is needed uh when you do write
scenarios.
And for right scenarios, it's important
to know the permission model, the
authentication model for MCP. And
fortunately, it's it's the same thing as
you already know if you work with APIs.
It's authenticated like an API.
Permissions, entitlements,
everything is the same as when you use
APIs. And the default configuration, it
only grant read access. So it's not like
you open up uh want to try something out
and then the agent can just go wild on
your data. It can only read data by
default.
So we have introduced MCP configurations
in order for you to be able to limit
what you actually want to expose through
MCP.
Now if you want something different than
the default then you need to specify the
configuration when you set up the
connection to the MCP server. The
default connection or the default
configuration gives you read operations
but with MCP configurations you can add
write, delete, etc. to specific API
pages.
When you set up the MCP configurations,
there are a number of things you need to
fill in. You need to give it a name and
a description. Then if you look below,
there is a an available tools down here
where you can select which pages you
want to expose and then whether you want
only to allow read access or allow
modify or delete etc. So you now have
the ability to decide exactly what data
you are exposing. Now I want to dwell a
little on what we have up here with
dynamic tool mode and discover
additional objects. We can either
preload all the tools into the MCP
server so that the tools are always
available or you can run in dynamic tool
mode where you ask an action which tools
do you have available and then it'll
give you the list. So the moment you
enable the dynamic tool mode the tools
are not available from the beginning but
they will can be found using this action
search tool that you might have seen in
the default configuration. And yes, I
think uh we have two ways of thinking of
configurations. One is the kind of
security boundary that you express here,
but there's also this limitation of
current language models, how many tools
they can actually handle, right? Yes.
For instance, currently C-pilot Studio
supports up to 70 tools. If you look at
all the API pages in the system, you can
easily extend to more than 70 tools.
particularly considering that read and
modify are two different tools.
Now the discover additional objects
allows the uh MCP client to also find
API pages which are not in your list
below in the available tools. So the
default configuration that you see
actually corresponds to having no tools
selected but both dynamic tool mode and
discover additional objects set to true.
Then of course you need to set the
configuration to be active. And as an
extra small security measure, we've
added a button to for you to allow
create, update, delete. If you don't
select that, everything will be read
only, which is a good way to ensure that
you're not inadvertently changing data.
So this is basically a summary of what
you need to specify in business central
configurations and how you identify it,
which toggles are there and the list of
API pages
>> and yes, I think you you just said etc.
But important thing here is also bound
actions.
>> Yes.
>> So it's not it's only it's not only CRUD
operations but anything in your API page
that is exposed as a bound action or a
method can also be called by the LLM or
by the agent
>> and this is exposed in exactly the same
way as you would expose bound actions in
normal O data APIs.
So to summarize, compared to earlier
where we were using the default
configuration, we've added a few extra
steps that are required to enable agents
to write data.
On the business central side, you need
to create an MCP server configuration
where you allow modifications and you
add a tool that allows modifying through
a given API page. And then on the
copilot studio side when you configure
your MCP server connection you need to
specify that MCP configuration.
So the idea with MCP configurations is
that it gives you more control. So it
allows you to start with lowrisk
readonly scenarios and then as you gain
trust in the LLM's abilities you can
open up for select writable scenarios.
You do that by choosing which API pages
that are available and which actions you
want to make available on those. And
overall, you can always modify the
configurations which will then change
the surface area that you're exposing to
your AI flows.
>> So to summarize, the vision didn't
really change since the last video.
That's good, Yens. Yeah,
>> it's still about making all
functionality available to AI and
agents. And of course, we want to make
this in a secure, reliable fashion where
MCP, the MCP protocol we believe is key.
and with uh MCP configurations both as a
way to minimize or exactly cater what
the agent is able to do and reliable
also making sure that it works in the
common MCP uh tools
>> and I also want to highlight that the
MCP server is currently in preview this
is work in progress and you saw make all
functionality available we have started
with API pages and are going to expand
from in there. So, look for more videos
later.
Call to action. Compared to the last
video, we have less things in gray. So,
um expose new functionality and API
pages if you want to use configurations.
Start experimenting with different
configurations. Maybe also set up
multiple connections, multiple agents
and and with as always write about your
experiences on social media and engage
with us in the product group if there
are things that are not working as
expected.
Some general resources aka.ms/bcall
is the link to the landing page with all
aka links for partners. um especially
for if you're a partner then the next
link aka.ms/bcy
yammer is the sign up link to viva
engage so make sure that if you were
previously on yammer or you wanted to go
here and sign up so that you are part of
the new community around business
central it's also important with the
next link ak.ms4bc
office hours because we're going to do
an office hour in January 26 20
20 2026 on MCP server. So, make sure
that you look for the date and the sign
up uh teams link there.
For LinkedIn, it's we think it's it's a
it's a good thing for you to follow the
product group on LinkedIn. This is where
we publish weekly news uh what's going
on right now and upcoming things and
tips and tricks. And of course, uh,
YouTube is our main channel for videos.
This is where you see this video and
others both and also what's coming tips
and tricks and what have you. So that's
it. Yens, this is video number two. Go
watch uh the see the links for the next
video and the previous here in the
description. And that's all we had for
you today. Thank you. Thank you.