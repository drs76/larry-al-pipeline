# From OpenAPI to Copilot: Auto-Generating MCP Tools for VS Code

- **Source:** https://www.youtube.com/watch?v=MpTpBLg8scw
- **Video ID:** MpTpBLg8scw
- **Channel:** mibuso.com
- **Published:** 2026-08-19
- **Duration:** 91m11s
- **Ingested:** 2026-08-19
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

Welcome everybody to our session from
Open API to Copilot. We are going to
take a look at today at how to generate
how to auto generate MCP tools for VS
Code.
My name is Markus Lippert. I'm a
platform leader at Cosmo Consult. I'm
also the product manager for Cosmo
Alpaca working on all topics around
DevOps, around developer productivity,
all the tools around it, and also got a
blog, and you can find me on LinkedIn
and on Blue Sky. If you want to connect,
always happy to have a chat.
>> Thanks a lot. To introduce myself, I'm
Tobias Fenster. On the business side,
I'm a managing director at 4PS in
Germany, which by now is part of Hilti.
So indeed the big drills
that is now also has a software
department, and we are in that one.
Which is why I'm also a chief engineer
at Hilti.
On the community side, I'm a regional
director and MVP for BC and Azure and a
Docker Captain. And same as Markus, I
run a little blog podcast a blog and a
podcast and tobiasfenster.io.
There you can also find the social links
if you want to get in touch and and have
a conversation.
So that's the intro. Um
And actually the keynote was also a
great intro for us because you heard a
lot about MCPs, you heard a lot about
tools, you heard a lot about running
agents that use those MCPs, that use
those tools. And that is what we want to
talk to you about today.
We want to look into why do we actually
need this?
If all of you have been perfectly
comfortable with the stuff that has been
happening in the keynote, then maybe the
first few minutes are a peek behind the
scenes and a bit of an understanding
what the basics are.
If you already know that, I hope you
have
a couple of minutes patience.
Then we're going to look into the basics
of Open API and MCP.
We're going to create our own tool
enabled VS Code extension. That's the
big fun part that Markus will be doing
because that's going to be the live demo
when when we see how it actually works.
Um we will talk also a bit about MCP
service and apps. Um and in the end we
will talk about um a bit of the security
side of it. So, if you run those MCPs,
if you uh run your agents, what are
security aspects and how can we handle
them?
And of course, in the end we should have
10 to 15 minutes for Q&A. So, if you
have any questions, um keep them in
mind. We have a few t-shirts here. Uh
so, if you want to grab one of those
t-shirts, figure out a question, ask it,
and you'll get one of those.
With that, uh let's get us started. We
first dive into the intro and into the
basics.
So, why do we need this anyway? Why are
we talking about MCPs? Why are we
talking about tools? You saw a lot of
about that in the keynote as well, but
what is actually the the technical stuff
behind it? The the idea is that LLMs are
definitely smart. Models can do amazing
things. You've seen that curve uh in the
keynote how much better they got in the
last couple of years, but they can't
talk to other systems out of the box,
especially not to your systems out of
the box.
And what I mean with that, just a very
quick demo to really um underline that
point. I have a um session here.
And I need to switch it into my MCP demo
mode. And now, um just to show show you
how dumb it actually is,
if I ask a simple question like, "What
is the time?"
It figures out, "Okay, I actually don't
know what the time is." because the LLM
has been trained on information on the
internet and uh things like this, but it
doesn't have information to um access to
live information. Another example would
be,
"What is the speaker lineup for
BC Tech Days 2026?"
Let's see what it responds.
Um
and it has figured out, okay, 2026,
that's after my training, so it doesn't
know from its training information, and
also by default, it doesn't have access
to somewhere, so it means it can't
figure out what the speaker lineup for
um BC Tech Days actually is. What we can
do is we can enable some tools, and I
have two prepared here. One of them is
able to fetch or search the internet and
then fetch content from the internet,
and the other one is an MCP server for
time information, so that one is able to
get the current time. Um and if we
enable that one,
save that,
did it do it? It did do it, and ask the
same question again.
What is the time?
It should now figure out that it has
the tool,
and asks me, "Do you want to allow uh
getting the current time via this MCP
tool?" I'll say yes,
and then it can talk to that MCP server
and figure out UTC would be 9:36. Could
give it the time zone, and then it would
figure out that it's um 11:36 here.
And the other question we asked before
was, "What is the speaker lineup?" So
again, uh we have now given it a tool
that allows it to search the internet,
so it should hopefully figure out that
that's the right path forward. Yes, it
did. It wants to search the web now with
the query BC Tech Days 2026 speaker
lineup, so let's allow this.
And it found the official site. Now it
wants to fetch the actual content. Let's
also allow that one.
And
depending on whether it worked well or
not, it might need one or two additional
searches,
but then it should figure out
Yeah. Now it tries to go to sessionize.
Purchase the content.
And
found it.
Getting the information.
And we can always follow along and see,
okay, what actually was the query that
it ran.
What was the response?
So you can always see how it interacts
with those with those tools and what the
content is that it got.
And
it now has the official list.
Okay, this is taking
a bit more attempts than typical. That's
the beauty of AI demos. Sometimes it
goes straight forward, sometimes it
doesn't. Here we are.
And I guess somewhere in here
I can at least
see Marcus and probably somewhere I'll
be here as well. So point again is
LLMs and models
are really good at what they're doing.
We saw the the intelligence they got
basically, but they can't access things
out of the outside of their training
information. And a path how we can
provide access to that training
information is via um
tools and via MCP servers.
This can also help you to integrate with
backend systems. So we've now accessed
the local time and we have accessed the
internet, but we can also access backend
systems. You've also seen that in the
keynote, it has a way how to talk to
your BC server.
And a lot of that
a lot of the backend systems out there
already can do that, but maybe you have
something running on your own that you
created, some APIs, some backend system
that doesn't have an
MCP server yet, or maybe you have a
third party that already has an API, but
it doesn't have an MCP server.
So that is basically the goal that we
want to show you today. If you see all
the power that those models have, you
see all the things that those agents can
do, but you just have that back end,
that source of information somewhere
where that you want to interact with
through your agents, but that doesn't
work because it doesn't have an MCP yet.
How can we solve that? How can we fix
that that that gap basically?
And that's what we're going to see
in the demo that Marcus will create.
But a peek behind the scenes, how does
it actually work? How do those MCP
service or model context protocol
service actually work? Um they have
those tools. That's only part of the
specification. They only have resources,
they have sampling, they have
elicitations and other things. But for
now, let's focus on the tools. And those
tools that an MCP server provides has a
name, a description, and an input
schema. And then Copilot can pick the
right one. You've seen that in the calls
that I made, it made the decision, now I
want to use the time tool, now I want to
use the search tool, now I want to use
the fetch tool, and it is based on the
information that the MCP server is
giving the model. Here I am, those are
the tools that I have.
They then show up in the Copilot chat,
and yeah, Copilot then makes the
decision.
Um I won't jump back, I've already shown
you this in in the previous one.
How does the standard the MCP standard
actually look like? It has something
like this that allows it that allows an
an agent to list all the tools, and the
response looks something like that where
you can see, okay, there is a tool to
get weather information in this example.
That one has a title, it has a
description so that the model can
understand what that tool actually is
doing, but it also has a traditional
input schema
which knows that, okay, I need to
provide a string which is the city name
or the zip code, and that actually is a
required parameter.
So this very much looks like if you're
familiar with an open API specification,
a REST API, that's basically the same
thing. We'll dig into that in a second,
but the point I want to make is there is
a specification, there is a standard how
um those tools are defined, and that is
actually based on schema, based on JSON,
uh same as a REST API.
And if that tool is now going to be
called, it looks like this. So, instead
of listing the tools, now I want to call
a tool, in this case the Get Weather
tool with an argument of New York, and
then the response would be current
weather is uh 72°
Fahrenheit, partly cloudy in in New
York. Again, you can see it's basically
just JSON going back and forth, um same
as as any REST API.
Um if we want to consume those MCP tools
in Visual Studio Code, there are
actually two ways of that. One is a
standalone, local, or a remote MCP
server. That is basically what you've
seen um mostly in the keynote and what
I've also been using with the little
time tool and the little um
web search tool, which is nice if you
just want to have a general setup that
is usable by a lot of clients, a lot of
editors, um
but actually is not what we will focus
in in the first part. You see that in
the second part a bit more because
there's also an additional option um
especially for Visual Studio Code how
you can uh surface those tools to your
end users or to the people who are using
Visual Studio Code by having a VS Code
extension that uses the Language Model
Tool API.
That means that your tools don't
technically live in an MCP server, but
they live in the Visual Studio Code
extension, which gives a tighter
integration. Um you have an easier
distribution path because if someone has
your extension, they automatically also
have those tools. It's TypeScript-based
and uses the uh VS Code extension API,
which is our focus for the first part.
So, what we will show you is how you can
use exactly that Language Model Tool API
to bring your tools into a Visual Studio
Code extension.
And to give you a quick idea of how that
looks like with something that's
predefined, I not only have the search
and the time enabled here, I also have
the GitHub pull request extension that
provides some tools. So, you can see
that looks exactly the same from within
Visual Studio Code. Those are just
tools. And if I use them,
for example,
show me information about the currently
opened
pull request.
Then it looks exactly the same. Again,
it's considering, it's looking at the
tools that it has, and hopefully
figures out that there is a tool um for
looking at pull request information,
indeed.
So, I'll allow it to do that.
Figured out there is no active pull
request, but I do have a local branch
that is connected to a pull request. So,
I allow another um tool call just to
look into the details here, or
maybe better here.
You can see there is a request um that
one that tool doesn't have any
parameters, but still has the output.
So, it's basically again the exact same
structure that we've seen before. It's
called It's making the decision which
tool to call, having a
sending that request and getting the
response. But, the thing is that
actually is not an an MCP server,
um but this is part of the Visual Studio
Code extension.
So,
this is the code behind it. Um it looks
something like this, and we will end up
at the end of Markus' demo with a piece
of code that looks very similar, where
we're not having those tools as part of
an MCP server, but those tools are
registered as part of the VS Code
extension and live in the VS Code
extension. You As an As an end user, as
a developer who's using VS Code, you
don't see really the difference, but But
a different way of distributing, it's a
different way how it's um integrated
into Visual Studio Code.
Um
to quickly dive also into Open API
because that's our starting point. I
would assume that most of you have heard
of it, but just to give you a quick
idea, Open API is a way how you can
describe REST APIs. Remember we have the
scenario that we have some kind of a
backend system that we want to integrate
from our agents, but we don't have um
MCPs for that one yet. When I would
assume that you at least have some kind
of a REST API, that's the de facto
standard at the moment. And what we can
do is we can build an Open API
definition on top of that, or if it
already has a specification, we can just
use it. And the example we want to work
today with is a simple API for products
and for orders. So, how does that look
um from an Open API perspective? It has
a definition like uh what's the title,
what's the version, how can I reach it,
but it also has type information. For
example, you can see here, if I want to
retrieve an order, then I will get
something that is a list of all orders.
Um the response then is an array of type
uh schemas order. So, very similar to
what you've seen before with the um
with the MCP tools, we have a clear
definition of what we request as an
input and what we expect as an output.
The types are defined here, so you can
see it, the order consists out of an ID,
a customer name, the items, and when it
was created. The ID actually can be um
an integer or a string, it has a certain
pattern pattern, etc. etc.
Um we also can send in parameters, we
can get error responses, so all of the
definition of how we interact with that
API. Again, very similar to the
definition how we interact with our MCP
tools.
Um and the parameters of course also
typed, so this would be the ID that we
ID that we um send in.
So,
this is again a very similar way of
describing how we want to interact with
the system and MCP or something behind
the REST API.
And to sum it all up for the
introduction, what we've seen now is
that LLMs need something to talk to your
systems to. MCPs can be used for that.
So, if there already is an MCP, perfect.
But, you might have a system that's
created by you or some vendor that
hasn't
provided an MCP yet. And that might mean
you want to create your own MCP tools.
If it has an API, especially if it's
already defined as open API, then
creating is easy. And you've seen there
are the standalone and remote MCP
service, but there's also the Visual
Studio Code tools that we can use. And
that's what we will look into.
With that, enough of the theory. Now,
for the fun part that Marcus is doing,
he will show you how we can build a VS
Code extension with those embedded
tools. And we will just start from
scratch with the open API definition.
>> Thank you, Tobias.
Okay, so before we head into the demo,
let's have a look at what we are going
to build.
So, we will start with a web API that we
are going to create. And we will also
have a VS Code extension created. Um the
web API is in C#,
VS Code extension is in TypeScript. And
the web API will expose an open API
specification that we will then use
along with an open API generator to
generate a TypeScript client as well as
the MCP tools.
So, based on the based on that generated
TypeScript client, we can then make
requests between the extension and the
between the web API.
So, we are going from the open API
specification that you just saw to the
generated TypeScript client that will
become our VS Code extension V1.
And then based on that, we will also
generate some Copilot tools that will
then use the generated TypeScript
client.
And that can be used in a Copilot as
well, and that will then become a VS
Code extension V2.
So, for now, let's focus on the first
part here. So, how to expose the OpenAPI
specification. For that, I am going to
switch to, um, VS Code here.
And first thing we are going to do is to
create a C# web API.
I got demo time set up here, so I don't
need to type all the commands, but I
will guide you through it.
So, first step here, let's create a new
C# API
by running dotnet new.
Just a default template for new web APIs
is, uh, what what we are going to use
here. And we are also going to use a
separate directory for controllers. Um,
where we, uh, then, yeah, add our
product and orders controller into.
So, this created the new project. I also
added the package, uh, for the Swagger
UI, so we can have a graphical interface
to look at our OpenAPI specification in
a second. Um, but for now on, this has
only created the files in here. So, web
API, a few controllers that are, um,
that that that are coming next, and the
program CS with just the default code in
it.
So, let's now also add the orders and
the products controller. So, just very
basic controllers.
And for example, for the orders
controllers, I have some static orders
in here, and I also have some different
endpoints. For example, a get endpoint
to get all the orders, uh,
an endpoint to get a single order by its
ID, and, um, a third endpoint to create
a new order.
So, you can also see each of those
endpoints have different HTTP verbs, as
well as the description in XML format,
and that the description can later on be
used to, um, expose it to the OpenAPI
specification.
So, what we are also going to do is to
add the the UI package, or enable the
Swagger UI package in the program CS in
here. So, that's just the default
program CS like it comes from the C
sharp template and you see by default
the current template already exposes the
open API and maps it to a to a route.
And by
adding this command here, we can also
have a look at it in a graphical way.
And the command here on line seven
always exposes the the APIs or the open
API specification underneath that path
and that path can then be used by
Swagger UI package to show the
endpoints.
What we also need to do to enable the
XML comments or to to pass the XML
comments into the open API
specification, we're going to enable the
XML docs. It's just a property here in
the CS project file and we also disable
the warnings for the methods that don't
have any XML comment.
So, with that we're already done
basically. So, let's run our solution
done it run
on local host. That is now restoring our
project.
Building it.
And now it's running on local host. So,
we can have a look at the Swagger UI in
here.
Like I meant, that's just a graphical
interface for the open API specification
and you can see it used the
specification JSON in here to display
all of that.
So, we can see the orders on the
products controller along with all the
XML comments that you saw in the code
right here. Um so, for the for the
endpoints themselves, but also for the
for the parameters we got descriptions
in here.
And also, if you go to a {slash} open
API V1 JSON, we also see the open API
specification and that's that is is
exactly the one that Tobias just showed
beforehand. So, we also have an
in a JSON format description of the
different endpoints, of the different
response codes, of the different
schemas, for example, you could also
have a look at that here as well.
So, for example, again, the the auto has
different required fields, different
properties with a different format.
So, everything is basically in in here
and
that one we are going to use now to
create a TypeScript client.
So, we got the OpenAPI specification
ready in here. Let's use it to
create our VS Code extension in the next
step.
So, let me head back here.
Let me close all of that.
There we are.
Choose my second demo time scene in here
to
yeah, create the VS Code extension.
So, first, what you're going to do is to
scaffold a new VS Code extension. So,
again, we are just starting from scratch
here.
And we're using the Yo package manager.
That's a package manager that can use
different templates to create a new VS
Code extension. We give the extension a
name in here as well as an extension ID,
some description.
And then we just need to to wait a few
seconds until the package manager
generates our solution.
So, we'll basically now download the
template um
and tries to set all the files up and
will then later on also install all the
packages that are needed.
So, you can see it created some files
and it's now also running npm install
for us.
So, if you've never seen a an extension,
it's pretty basic. So, So, most
important part here is the extension TS,
that is basically the entry point for
the extension where we have an activate
function that is one doing the
activation of the extension. And apart
from that, all the necessary information
is within the package JSON. So, we got
our extension name,
the commands the extension is
contributing as an extension, and some
other stuff.
So, what we're going to do is now to
install the OpenAPI generator package.
So, that is
used later on to generate TypeScript
client. So, it's just a simple NPM
install to install the package into our
project.
There we are. And the third thing that
we need to do is to add a a
configuration for the generator.
That is the OpenAPI tools JSON. And that
has specified how the generation should
work like.
So, in here we have two different
generation configurations. So, the first
one we're going to use to generate the
TypeScript client, and the second one we
will later on use to generate the the
language model tools.
So, you can see we specify a generator
here. So, you there are different
generators for different programming
languages, also different
generators for TypeScript themselves.
You can either use the fetch library or
something like Axios or something
like that, and use that to generate the
code.
We also specified where our OpenAPI
specification lies at. And we have got
an output directory in here and some
properties. And
that configuration here can now be used
to generate the TypeScript client.
So, that is what we are now doing.
So, we run the OpenAPI generator CLI to
generate the TypeScript client. We are
using the TypeScript client
configuration specified here in the CLI.
And that one is now going to write some
files.
>> [clears throat]
>> In a second, hopefully.
There we are.
Exactly. And now in this source
directory, we have the generated folder,
just as we specified it. And there are
all the generated files in it.
So, let's have a look at some of them.
So, for example, here in the source
directory,
so source generated source, for each
controller, we have now a class a
TypeScript class here as well. And
within that TypeScript class, all the
code was auto generated by the
generator. And that one is basically
doing all the handling, so the the
calling of the back-end endpoints, the
request and response handling for us.
So, we don't need to write any line
manually to do all of that.
It also has the data about the the
models in it.
So,
if I go to the
Yeah, there we are. So, there's the
product interface here as well.
That was also retrieved from the OpenAPI
specification, and then a TypeScript
class was generated based on that. So,
we have also type safety in here as
well.
So, how can we use those generated
classes? Basically, pretty simple, like
in any programming language, you just
need to create a new instance of that
class, and then you can use that use the
instance to call the different
endpoints.
So, do the request against the back-end,
basically. And to show you how that is
working, I'm registering some VS Code
extension commands in here. That is done
by the um
VS Code commands
register command.
I just need to pass the name and then
need to pass what should happen. And in
in here I'm basically using the the
generated classes.
So, not only we need to call the
register command to make the commands
available, but we also need to register
them in the in the extension TS. So, we
of course need to call the method that
we that I just showed you.
And we need to add them to the package
JSON in here as well so that
the outside world basically knows what
what commands are coming from our
extension.
So, I have two two commands in here for
listing products and for listing the
orders. And with that I'm going ahead
and starting my extension now.
There we are. And you can see if I
go to the tools in here, then we have
our
Where's the extension?
Let me try it again.
Wait, we don't have the tools here. We
have the commands.
Say it again. We don't have the tools
yet. We have the commands yet.
Ah, the commands yet. You're right. I I
was one step further.
Okay, so we got the list product and
list all the stores right here with the
tools. That's the first one. Exactly.
And
if I if I run that, we do the request
against the back end, and the back end
gives us the different available
products. And I can choose from from one
of those products, and I get the
selected one.
So, that is basically the journey tools
that I just showed you. So, we use the
Open API specification to generate the
TypeScript client. And um
And now next up we are going to generate
the tools that are using that TypeScript
client.
So, let me close that app again.
This one now.
So, if you remember from the OpenAPI
configuration in here, so we not just
had the the upper configuration here,
but also the second one for the language
model tools, and that one is the one
that we are now using
um to generate the the um copilot tools.
So, that is exactly the same like above.
The only difference is the output
directory. We now are writing into
generated tools, and the um we also
specify the template directory. So, that
means we can add our own templates that
are used to generate the TypeScript
code. Um and we yeah,
we'll now just create one of those
templates, so we can have all the
language model tool API handling um for
for us to to be done.
So, I'm doing doing that here by
creating a mustache template in the
templates directory.
Um mustache is basically a language that
allows you to have a different syntax,
for example, for
for looping through different operations
of the OpenAPI specification. And in my
in my template here, I can specify how
the code should look like that will be
generated. I got a few helper fields,
helper variables, um that are then
injected into that code one. And um
yeah, then the classes will be generated
based on that.
What I'm also going to do to make it a
little bit more easy later on is to add
a script
for um registering all the um all the
tools within the package.json. So, as
you saw beforehand, we
where we registered the commands in
here, the same also needs to be done for
the for the language model tools. And
that is basically what the TypeScript
script is doing here. So, it's
extracting all the endpoints from the
specification, then builds a map from
the operations to the parameters, and
write all of that into the package.json.
So, we also add an
npm script in here to make that simple.
So, whenever the APIs are changing, we
can just run the generated tool script
in here that is running the generation,
and then
afterwards running the JavaScript script
to add all the tools to the to the
package.json.
So, let's now run that that tool here as
well.
Oops.
So, just run npm run generate tools.
That's that will then run the script
that I just added.
And you can see now in the source
generated tools folder, we also have
some files, and those files are exactly
looking like the mustache template that
I showed you beforehand. So, this time
we again registering some some stuff,
but not commands, but this time tools.
And for each endpoint in my in my open
API specification, it now added a a
method in here a a register tools call.
And that one is basically just
instantiating the orders API in that
case, and then calling the calling the
method,
and handling the response value again,
and passing that on to the
to the copilot.
What also my register tools JavaScript
script did is to add the tools to the
package.json.
So, in here
for [clears throat] every endpoint, we
now also have a
a language model tool in here with a
name and description and so on. That
description is again coming from the
open API specification. And for
endpoints that have some parameters, for
example, we also have the input schema,
so that copilot also knows which
parameters it it uh to pass, and what
those parameters are actually doing.
So, the only thing that we need to do is
um now also register the tools in our
extension uh TS in the activation
method. And that is what I'm doing here.
So, calling the um two methods for the
products API and the orders API, and
that one is then um calling the register
tools command to register the tools.
So, basically the same way that you saw
before and with the uh commands, we now
also did for the tools. We generated
them completely based on um based on the
open API specification, and can use that
now to talk to Copilot.
So, this time now they should uh be
visible here, and they are. So, you can
see that our extension that we just
created together, and for each endpoint
in the backend, we also get a tool in
here that we can use to list orders, get
orders, and so on, and um use them along
with Copilot.
So, let me let me ask which orders
there are from
Alice, for example.
Uh
that's another
MCP server that I need to disable. Give
me a second.
Yep.
So, it now figured out that it needs uh
certain tools for my extension, the
orders get and the orders ID get.
And it used all of those tools um to
retrieve the information I asked it for.
So, I can also ask, "What are product
one and three?"
So, it again used the API products get
in here that will um to list those two
those two products and give me more
information on them.
Okay, so you saw how we went from open
API specification to generate a
TypeScript client. We used a TypeScript
client to also wrap a tool around of
that. So, we generated tools that are
then calling the classes from the
TypeScript client and all of that can be
used with then Copilot with Copilot chat
and we basically didn't need to write
any any of those lines by our own.
Then to also give you some tips for the
real world, not every endpoint should be
a tool. So,
it is the best idea to use some kind of
configuration file to exclude certain
tools or certain endpoints. For example,
some destructive endpoints for example,
some endpoints that are deleting some
stuff for example shouldn't shouldn't be
included
without any precautionary measures or
something like that.
Second part is that the open API
specification definitely matters. So,
definitely invest some time into good
descriptions
of your specifications to good
descriptions for your operations, for
your parameters and so on. So, the
Copilot
yeah, knows a bit better of what tools
to choose and also how to call those
tools.
Also, it's a good idea to document the
errors that can happen. So, document the
different response codes that an API can
can can return. So, Copilot can maybe
also troubleshoot by our by its own.
If you have some third-party APIs that
you may that you might not fully
control, then you can also add something
like an intermediate step to enrich the
open API specification with better
descriptions or something like that or
even create create the specification as
a first-hand.
Also, if your backends need some kind of
authentication, then definitely the
TypeScript clients that you are
generating should handle that
authentication. So, you shouldn't deal
with any secrets within the Copilot
chat, and you shouldn't Yeah, pass any
secret to them.
Also, make the regeneration as easy as
possible. I showed you beforehand how
easy it is to add a add a script to the
package.json, and that makes it simple
that whenever the API changes that you
can just run the script and get the
newest changes as a new tool, for
example.
So, to show you how the regeneration
works,
so, let me close that up here, and let
me
do a change now.
So, I'm stopping my web API now, and I
add a new endpoint to our products
controller,
in that case, for getting product
statistics. And I now also want that
endpoint to be exposed to as a new tool
to my Copilot. So, I I added the
endpoint, then I can start the web API
again.
It's building my project again.
There it is. It's running now. So, my
OpenAPI specification automatically has
the new endpoint in it, so I can use
that specification to regenerate the
TypeScript client. So, there's basically
two steps. First off, we need to update
our TypeScript client, so the the
TypeScript classes, and the second step
is then to regenerate the language model
tools.
So, by for that we're just running the
NPM run generate tools. So, remember
that this the um
the script that I added in here.
Generate tools.
So, I just need to run that again and
now I have eight language model tools in
my package.json available. And if I
start the extension again in here,
and have a look at the tools list,
there you can see there's also the
statistics endpoints that I just added.
So, basically I just need to run the
regeneration of the um of the tools or
of the classes and then I have the the
new endpoint here available as tools
well in just a few seconds.
To also give you a real-world example
how we how we use use that within Cosmo,
um so,
within Cosmo we have a product called
Cosmo Alpaca and for that one we already
had a C# API available that already had
an OpenAPI specification and we also
have a VS Code extension that is talking
to that C# API.
The OpenAPI specification was already
used together with a OpenAPI generator
to generate the commands for our VS Code
extension and um yeah, we have basically
a lot of endpoints, a lot of different
commands in VS Code as well and we also
often have commands that are
um yeah, that are basically called after
each other. For example, something like
creating a repository, then assigning a
customer, creating an application,
creating a test app, then creating a
development container. Uh all of that is
basically five times clicking a
different action.
And by exposing all of those endpoints,
all of those um features to a Copilot as
well, it's just a simple prompt asking
the Copilot to create a new repository
for a certain customer and creating a
certain app and test apps setting
setting up a development environment and
copilot then figures out what tools to
call and
what actions to do.
So for us it was really a a very quick
win. So in
basically in no lines written on our
own, we made all the all the
functionality we have also available to
copilot.
Yeah, and we also of course have some of
the endpoints that I excluded in there.
So we also have some destructive act
actions or something like a a backlog
import
that is something that we we don't want
to want to expose to copilot. That can
also cause some some issues in there.
To also talk about the limitations,
um so of course all of that is great. Um
you can generate lots of that
automatically, but it also comes with
the limitation that of course we as code
extension also only works in VS Code. So
if you want to use your backends
somewhere else somewhere else where
maybe also MCP servers are supported,
then this can be a bit limited for you.
Also keep in mind if you have many
extensions that are exposing many
different tools via their language model
tools API, then yeah,
there's maybe something like context
window pollution. Although with newer
models with bigger context that isn't
isn't such such a big problem nowadays,
um but if you have many tools it can at
least make the decision a bit harder for
copilot. So
it doesn't really know what tools the
right one to to call if you have many of
them. Yeah, as it can't keep keep in
mind what all the descriptions are and
yeah, figure out what is the best one
here.
Default MCP servers have something that
is called dynamic tool discovery to
overcome this. So there's something like
a meta endpoint that helps you to search
for different tools for certain for
certain tasks. Um there's something
similar in the language model tools API
for VS Code that is called virtual
virtual tool clustering that is
basically clustering together different
tools that are pretty similar. And it
also tries to pre-select um some tools
that you are likely going to use.
So that definitely um overcomes a bit of
those um issues with many tools.
So that's it for now for the tool
enabled VS Code extension. So that is
basically the first part that we wanted
to show you how easy it is to come from
a open API specification to a VS Code
with um with exposed tools.
For that, to summarize um yeah, good API
documentation makes also good good um
language model tools. So invest in your
specifications and invest in your
descriptions. So um
you make it go pilot a lot easier to to
to call the right tools and to go to use
the right parameters for example. Also
keep in mind not every API I API
endpoint should become a tool. And um if
you do all of that, if you bring all
your legacy systems, all your
third-party systems um to your co-pilot,
that definitely um
definitely allows to to use AI more
productively, to talk to your systems as
well and not only the default big
systems like GitHub, Azure DevOps, um
or something like that.
So here on the right I also have a QR
code that you um
can use to to go to a repository. I have
all the demo time files in here as well.
So if you want to do what I just did in
the demo, then you um can just use that
to uh see you how it's going.
And with that um I also talked about the
limitations beforehand
of the tool enabled VS Code extensions.
So there are a few downsides um
and there are uh might be also some
reasons why you want to use MCP services
instead of VS code extensions and that
is the reason why we also want to take a
look at MCP servers today.
And we do that by
an example by using MCP apps.
So first of all MCP servers, I think you
know also already know what what all of
that is. By default MCP tools or MCP
tools with MCP servers return data in a
text based format. So you get an input
and the MCP server gives an output.
Often there's a problem if you have like
more
data that's a bit more a bit more
complex. Something like you want to do a
performance analysis. You want to look
at some graphs for example, then it's a
bit hard to work on that with just plain
text.
And that is basically where MCP apps are
coming into place. So MCP apps allow to
to have a custom HTML interface to work
with so within the chat you can directly
just display some HTML that can then
help you to for example look at some
graphs look at some some tables
dashboards whatsoever. And that directly
works within Copilot without any third
party application.
The great thing here is that you can
also use two-way communication. So
that's
that those are not just static
dashboards or something like that but
you can also make them clickable make
them communicating with the backend
again and that makes them very valuable
for for such complex scenarios.
When we are now looking at C# for C#
there's also an MCP SDK that you can use
to to create MCP servers.
In regards of MCP apps there is still an
open pull request for the MCP SDK. So
there's no full support yet for MCP apps
but they are already working on but we
will look at that today anyway
because most of the existing SDK methods
already allow us to to create such MCP
apps.
So again, before we head into VS Code,
let's have a look at what we we are
going to build.
We will again have our web API and VS
Code.
And this time our web API will expose an
MCP server
along with different MCP tools and also
MCP app resources. So that is basically
that one that we needing for the MCP
apps to display some HTML interface.
And VS Code is then going to communicate
with the MCP server.
Okay, so let me switch over to VS Code
again.
That one can be closed.
And I'm now going to stop my web API
again from the previous demo and I'm
going to add the MCP server NuGet
package. That's just an existing NuGet
package that allows us to expose our web
API also as an MCP server.
So just running don't net add here.
That is installing the package now.
And now I can also add some code to our
program CS to um
start our MCP server basically. So it
calling the add MCP server um method and
here it also tells us that it has a few
more capabilities than the default ones.
In that case, we're using the UI
capability um to to tell it, "Hey, we
are also supporting MCP apps.
We are going to use HTTP transport and
we are going to have one tool that is um
an MCP app in here that is also having a
resource.
So exposing MCP tools is very similar to
controllers. So, we have a class and
each of the methods
is then getting an annotation in here
that's called MCP server tools. So, you
can give a description
for the method itself and also
description for all the parameters in
here. And the interesting part is
basically down below here.
So, that is our MCP tools that will
then will be exposed as an MCP app.
And that one is next to the default
content is also returning a structured
content so in a JSON format and that
JSON can then be used by the by the HTML
interface to display the information.
So, we not only need to
to register some MCP tools but also the
MCP server resources.
So, the resource I I just showed you
beforehand that is that one here is has
a certain
URL and underneath that URL we can tell
it that whenever the resource is
requested then the orders dashboard
should be should be returned and that
dashboard is then later on showed in the
cockpit chart.
So, let's also create that HTML file.
So, here in the UI folder I have the
orders dashboard. It's basically just a
simple HTML
file with some JavaScript in it and that
JavaScript is basically using the
structured content the JSON JSON content
and putting it into the website so we
can show it in a nice way.
Then again, let me just run don't it
run.
Start up API
for the MCP server now.
There we are.
Then I can go ahead and run my extension
in here.
And here in my MCP JSON, I got the um
localhost MCP server already prepared.
So, the one I just that I just exposed,
I'm going to activate in here.
Save that one.
And let me disable those two again.
Yep. And click start here.
So, you can see I also now got my Web
API demo MCP server in here. So, it has
a different icon than the extension
does. And um it has the different MCP
tools that I showed you beforehand, as
well as the Get Orders dashboard. So,
that is basically the MCP app that we um
that we just created.
So, let me now ask my Copilot here,
"Show me
the Orders dashboard."
Then disable the one.
Yeah. Now, figured out it needs to use
the MCP server and the Get Orders
dashboard tool.
Tries to load it now and asks me if I
was allowed to show the dashboard. I say
yes. And I got the MCP app here showing
within the chat window, having a more
rich interface. Um I could also do
something like show graphs in here, show
um diagrams, tables, and so on. Makes it
a bit simpler to to work with.
Okay.
>> That's it for MCP servers and MCP apps.
So, you've now seen
from Open API how we can get to a VS
Code extension with those tools, how we
can generate a regular MCP server, um
how we can interact with it and how we
can um generate apps,
but also we wanted to talk a bit about
the um MCP and agent security
implications.
And that is um because sometimes at the
moment it feels to me like the early
days of the internet when we realized,
"Okay, there's so many tools out in the
internet. Uh people are sharing stuff. I
can just download them, install them, be
happy. What could possibly go wrong?"
And then we figured out, "Okay, that
might not be such a great idea." Um
nowadays you see, "Okay, if someone
figured out there is a new MCP, why not
just run an NPX command?" Um what that
does is just pull something from the
internet. You trust a website that says
this is nice, but actually you don't
really know what is happening. So
certainly there are some security
implications there as well, and and
that's what I want to uh talk about for
the um rest of the presentation.
The tool I want to use for um showing
you how we can guard against those
security problems are Docker sandboxes.
Docker sandboxes are micro VMs that are
designed to run coding agents. Now the
scenario is I have a coding agent. I
maybe let it run in Yolo mode or at
least um with um yeah, a lot of
permissions, and I just want to make
sure that it stays within a secure
context. Those sandboxes have their own
file systems. They have their own
network, their environment, their
processes, their Docker daemon if
needed, etc. So basically that gives an
um a secure sandbox, as the name says,
to an agent to play with and to um
interact within without breaking
breaking anything outside of that
sandbox.
And I will show you how we can use that
so some of those MCP or agent attacks
can be mitigated. This is not the only
way how we can do this. Oh, sorry,
actually.
>> I'm switched.
>> Yeah, okay. Thanks. Thanks. Um
there are other um other tools out
there, and some of those aspects already
are in in other tools. Um but just as
one of the possibilities.
How do we use that? Um as you can see
here on top, I can do something like
sandbox sandbox run copilot. So, I want
to have a sandbox where GitHub copilot
is running, and it contains a few kits.
A kit for the Azure CLI because I want
to interact with Azure, a kit for AL
because I want to do AL development, and
a kit for Azure DevOps because I want to
interact with Azure DevOps.
Um and I'll show you in a second how
they work, but um let's kick this off
now because creating this sandbox will
take um a few minutes. So, I'll switch
back to the presentation, and then we
will see how it has worked. The other
thing I want to initially also present
to you is that um there is a terminal
user interface here as well, where I can
see my sandbox, and I have a bit of
logging and um network information.
Again, uh we will take a look at that in
a second.
So, what are the actual challenges that
we're seeing? Um
there could be something in the code, or
there could be an instruction in a bad
MCP that is actually breaking the
confinements and is doing something bad.
We have now seen in the last, I don't
know, 50 minutes or an hour, um how easy
it is to create such an MCP server, how
easy it is to create code that exposes
those tools. But, what if someone puts a
line in there that tries to fetch
secrets from your environment and sends
it somewhere else? What if someone tries
to run arbitrary code on your system via
that um
command that is running on your machine?
Basically, we're allowing through those
MCP service, if they're running locally,
or through those tools um integrated in
a VS Code extension, things to interact
with our system that maybe are not doing
what we want them to do, and they're
also consuming the environment around
it, which could also um lead to
problems.
An example for that is that it might
delete your hard drive.
That might sound stupid, but this is an
actual bug report out of Cloud Code in
October last year, so also not that long
ago.
And as you can see in the description
here, that guy says that Cloud Code
executed a recursive delete command that
successfully deleted all user files in
my home directory. It actually went down
to the root directory and only thanks to
the permission set up, it couldn't
delete the system files, but it
basically deleted everything on that
hard drive.
Um, that is also to a degree was a bug
in in Cloud Code, but at the end of the
day, by allowing an agent full access to
your hard drive, it could do that,
right? Hopefully, it's asking and
hopefully you're carefully reading what
it's doing, so you know that you're not
allowing it to do that. And at the same
time, if you just let it run with YOLO
permissions or if you're not carefully
checking the things that it's doing,
then this could actually happen um by
giving it access to the full system.
I think that's certainly relevant in the
BC world as well. That's not specific
to, I don't know, some other programming
languages or other environments.
Deleting your file system probably would
be an issue for you as well. So, let's
see how Docker sandboxes can guard
against that.
Let's see. We have the sandbox now up
and running. So, what you can see here
is now GitHub Copilot, the terminal
interface running inside of a sandbox.
What I can also do is I can get uh
shell session inside of that sandbox.
And once we have that, I want to show
you that
it doesn't have my full um my full
folder basically exposed. So, I can go
into C, users, my username, and then it
has a part of it because that is how I
started it. I I gave it the current
folder, and that is under documents,
events, BC Tech Days. That was the
folder that I shared with it, but it has
nothing else. So, it only has access to
the specific folder I shared with it,
and otherwise it can't access anything
on my host system when it comes to the
file system. So, basically, if it would
try to delete everything, it would
delete the sandbox, but then in the
sandbox there is nothing that I would
care about because as you've seen, I can
easily recreate it. Yes, it could
potentially delete my workspace as well.
That would probably be a problem, but
hopefully I have my sources also in Git
or somewhere,
but that is what it needs to work with,
so we can't do that.
We can't take that away. What it also
can do is it can
um
it can link files in read-only or
folders in read-only. So, if you for
example have some documentation that is
somewhere, or you have other sources of
information that it only needs to read,
then you can link them into the sandbox
in a read-only way, so then if something
goes wrong and it tries to delete, it
even doesn't have the permissions on
those.
So, this is the first part I wanted to
show you um how we can use those
sandboxes for restricting access to the
file system.
The second might be that it might do
something bad to your production
environment because you accidentally
gave it permission. There I have an
interesting example as well. There was
an outage of Amazon Web Services, and
I'm not saying this because Amazon is
bad or anything. I think the same
problem could happen in Microsoft or
Google or anywhere else.
Um and what Amazon is saying that it
actually wasn't a an AI problem, but it
was a user who had too many permissions.
Um but it kind of hints at the problem
that if you as a user have permissions,
then probably that agent can get those
permissions as well. So, if you're not
careful with how you're sharing those
permissions with an agent, it might do
things that are perfectly fine on a demo
environment, that are perfectly fine on
a QA staging environment, but could
prove disastrous on a production
environment.
The same would be this example here.
This is a guy um chatting here to
I don't actually know what the agent was
in this case. Um but asked it um so you
deleted the database without permission
during um and code and action freeze. So
basically he explicitly told the agent,
"Please do anything destructive. Please
change anything." And in the end um if
you go to the very right, it says, "This
was a catastrophic failure on my part. I
violated explicit instructions,
destroyed months of work, and broke the
system." So it shows some
self-reflection, but at the end of the
day the database is still gone. Um
hopefully you have a backup or that guy
had a backup and could restore it at
that point.
But again, the point is
it goes through the explanation why it
happened, and that could be something
that's perfectly fine on your
development environment, that's
perfectly fine on a demo environment,
but it's absolutely not fine on a
production environment.
Again, um to give you an idea why this
might be relevant,
um let's assume we have a little
terminal session here.
Um I'm doing some development work, and
to make sure I'm just in my development
environment, I check, "Okay,
this is in the Azure sponsorship um
subscription, so this is my my
playground, my sandbox." Perfectly fine.
I'll let an an agent run. Um I might
even run it in Yolo mode uh because I
know, "Okay, nothing in here is of
value. That is fine."
But then maybe um a customer request
comes in,
and then I do something like AC account
set and change it to the production
subscription because now I need to work
for the customer or need to do something
in our internal production environment.
But what happens if I go back in here
all of the way.
If I go back in here where the agent is
running, if I'm now doing an AC account
show, you can see that oh, actually the
agent now has access to the production
environment.
So, this is another example where maybe
if you just let those agents run, you
let them run on different projects, and
you do something for yourself, or you
have different agents running in
different environments, they might
cross-pollute some of those settings,
some of those permissions, some of those
access credentials
might go from to the other,
and you don't have the control anymore.
If I go now back into my sandbox
and do something like AC
account show here,
it says I need to log in first. And the
point I want to make is that sandbox has
a completely separated environment
running on my laptop, but completely
encapsulated, so it doesn't share the
login information, it doesn't share the
subscription subscription that has been
selected. So, if I now go in here and
log in and set it to the uh to the right
subscription, I know that the agent will
always work in that subscription, no
matter what I do in the host, no matter
what I do in another agent, so they
those are cleanly separated now.
Um
yeah, so that's the demo that I wanted
to show you. AC login, AC um
account set, those are examples for how
you would have different permissions,
different environment configurations
that could pollute another session where
potentially an agent is running and then
doing something bad um that it shouldn't
do on that environment.
The third example is that it might
actually steal secrets either by reading
your home folder, by reading your
environment, by using credentials in
your environment, and then um sharing it
somewhere else. Again, Marcus has shown
you how easy it is to create those MCP
servers, so it could be something that
has a completely valid um job to do, it
could be something that creates a
feature that you absolutely need, but
somewhere between that useful code, that
perfectly fine code, it might um get
that information and push it to the uh
back end of an attacker, exfiltrate it
somewhere, and then people could use um
the login information, the credentials,
the secrets, whatever it stole on their
own.
An example for that could be this MCP um
with personal access token
authentication.
I really have to say I don't know that
person. Um it seems slightly weird that
that account has been set up before
creating that repository, but what it
offers is you can use the Azure DevOps
MTP server with personal access token
authentication. So, you basically just
give it an access token, and that one um
then is used to talk to Azure DevOps.
Um if you know about access tokens,
that's not the most secure way how to
work. They tend to live very long. They
tend to have more permissions than they
should. So, actually um that is
something that was not implemented in
the Azure DevOps MCP server in the
beginning. So, then suddenly this
environment uh also this this MCP server
pops up. And that could be one of those
examples where and again, I really don't
know, uh but where an attacker could
say, "Okay, I have found a gap in an
official tool. I provide something that
looks perfectly legit. I bet people to
um share their personal access tokens
with me, and then I can use them on my
own."
Now, you might say, "Okay, personal
access tokens um
that that should not be used anyway, but
this is the actual official
documentation for the um official
Microsoft MCP server." So, they're also
uh showing how you can use environment
variables and access tokens. So, in some
scenarios like CI/CD or automation, as
you can see on the right, that is
actually a perfectly valid scenario. So,
an attacker might be able to use that.
And now if you say, "Okay, that's Azure
DevOps." Of course, we are on GitHub. Um
this is the documentation for how to use
a personal access token in GitHub. So,
this is actually not a
technology-specific or a tool-specific
problem, but this is something that kept
could happen somewhere else as well.
So, how do we guard against um a
potentially fake um MCP server that is
trying to steal your information? Let's
take a look at another demo.
And what I want to show you
here
Oh, actually, something else I wanted to
show you just to prove that uh those
sandboxes work as you expect. I also
want to show you just a legit use. So,
if I do something like
download AL symbols
within that sandbox because we have the
AL um
the AL tools and the AL MCP that you've
seen in the
keynote as well already installed, you
can see here the agent going ahead
figuring out that this is actually a BC
project, finding the app.json, the
launch.json, and doing then the download
symbols. Need to log in here.
And then it should have the symbols
downloaded.
And that has actually succeeded. So,
just to show you um also in those Docker
sandboxes, the agents just behave as
you're used to. It's just an additional
environment around it.
But to get back to our point before, we
might have an attacker that is trying to
steal something from our environment and
uh sending it somewhere. Um, if I now
try to do something like have an
internet access
to a random URL, which happens to be my
blog, but of course could be a malicious
back end.
And do that within the sandbox.
Then we see an error that this is
blocked. The reason for that is that
sandboxes by default block all outgoing
um
network traffic. They have different
ways how you can handle that. You can
deny everything flat out. They also have
a pre-configured set of typical dev
sites, so they give you access to
GitHub, they give you access to Azure,
they give you access to AWS, which is
what I have already set up here. So, the
typical things that should be safe are
already allowed. Or they also have an a
more open mode where those blocks are
not in place. But as you can see here,
if something weird happens, if someone
is trying to access a back end that it
shouldn't access, then it would um block
it. And I can even see in the logs here
for that sandbox, there was um the
request to access to BSensor.IO, and
that one has been blocked. I can also
see all the allowed um calls that it has
made. So, you can also see here how it
reached my uh back end to download the
symbols, etc. So, I can also keep track
of what those MCP service and those
tools are actually doing. Most of it
should be, if it's legit, already
allowed for the typical dev scenarios,
but if I have some specific environment,
I need to config configure that.
So, the access to that back end would
already be blocked, but there's another
second nice trick. And for that, I want
to show you how I can interact with um
Azure DevOps.
I could say something like, "Give me
work item 24 in project
for PS Germany."
That should now figure out that the I
also have the Azure DevOps MCP, indeed,
and it gets the information.
And tells me, "Okay, this is that work
item, had that uh reason, assigned to,
etc., etc." So, you can see that the
Azure DevOps MCP works in here.
The interesting thing is, if I look at
the configuration for that MCP,
it has that little
path authentication set up here, but the
personal access token that has that it
has configured actually is not here. And
that's definitely not a valid personal
access token.
The interesting thing that I can do with
Docker sandboxes is that I can inject
those credentials. So via a setup that I
will show you in a second, I can tell it
if you're calling Azure DevOps inject a
specific authorization header. So within
the sandbox, the MCP server doesn't know
the authentication header. You can see
here this is clearly not the
the authentication token that I want to
or the access token that I want to use
here. But the sandbox around it is
figuring out okay, it's trying to call
Azure. Now I'm going to inject the right
secret. I'm doing the call, it's
returning and the MCP server gets the
data that it expects. So as you've seen
the interaction with Azure DevOps
actually works, but I'm never sharing
the real credential with the MCP server.
So even if that MCP server would be
malicious to go back to the example that
I had before, I would never share the
real credential, I would never share the
real access token with that MCP server
because that would be handled by the
infrastructure around it.
But this is another nice way how
how that um
attack vector can be resolved. A, I
don't give it access to any network
area, so a network environment, so it it
can't just exfiltrate it somewhere. And
B, I'm not sharing even the real
credentials with the MCP server because
they're injected around it.
How does that actually look like? Let's
start with the last example because
that's the most complex one. This is one
of those kits that we've seen initially.
So if you remember
when I started this here
go back to that command, we have
referenced those kits. And that is a way
how we can configure the behavior of
that sandbox.
So this is how such a kit looks like.
This one has name, display name,
description, but then it also has the
network configuration. So, I let it know
what the domains are that I want it to
be available for that sandbox where the
kit is installed. And now we have the
interesting part, which is the service
domains.
So, here you can see the back ends that
it's using to talk to Azure DevOps. This
is our
Azure DevOps organization here. Here is
the Azure DevOps MCP and a couple of
other back ends that it uses to interact
with the system. And here I tell it,
"Okay, if you do that, then please
inject the Azure DevOps header that you
can see here. The Azure DevOps
definition is just authorization and
then
basic authorization and then a secret
that I'm sharing in advance with the
sandbox.
And then we have a couple of additional
steps here to take by letting it know
that it should read it from an
environment and that that environment is
proxy managed. So, I'm basically telling
it, "Okay, this is something that the
sandbox is doing." I can do that by on
the host setting a sandbox secret. And
that secret contains my real access
token and then the behavior that you
have just seen will happen. So, when an
outgoing call is happening to one of
those domains,
it will strip the already existing
authorization token that has that fake
access token that you have seen. It will
inject the real access token and then do
the network traffic with the back end.
So, this is how that trick around the
credential works. To also show you how
installing the AL tool works, here you
can see that I have given it access to a
few domains that it needs for
downloading the symbols. That one talk
to Alpaca, so a specific back end
basically. So, I also needed it to give
access to our Alpaca back end here. But
also the installation, if you remember
from the keynote how um Stefan showed
you how to install it, you can see the
command here. That is exactly the .NET
tool install of the um
BC development tools, which include the
AL MCP server.
As a requirement for that, you need
.NET. So, also before actually
installing the AL tool, you can see here
that I'm doing the .NET install.
And that is another example
how we keep the containment between
those agents. So, we're not just
installing .NET, we're not just globally
installing the AL MCP server, but
instead we're just installing it in that
specific sandbox. We're giving it the
right permissions to to access the right
network resources, and we have that
trick about the credential setup that
you've seen in in Azure DevOps.
Um the last example, because you saw me
use the Azure CLI, that basically would
be another way um where we are how we
are here installing um the the Azure
CLI.
So, this is how you can configure those
um different
uh kits inside the sandboxes. We have
the overall uh micro VMs that make sure
everything is contained, and then you
can customize it, you can add your
tools, you can make uh sure the network
access is configured in a proper way.
And that should help you solve um those
[snorts] three issues and hopefully a
lot of the others that um clever people
are figuring out every day. So, you can
feel a bit safer um running your MCP
servers, or maybe even um letting an
agent run in in your local mode.
So, to look back at uh the whole session
that we've had, we tried to show you how
you can have your own back ends, or back
ends that don't have an MCP server, but
maybe have a REST API, how you can
integrate them into your models, into
your agents um by creating something
like the MCP tools, or the VS Code
integrated tools.
If you want to live immediately or only
exclusively in Visual Studio Code, then
the VS Code tools are nice way. If you
need to be a bit more versatile, if you
want to use something like the MCP apps
that Marcus has also shown you, then
probably an MCP server is the right way
to go. And independently on which way
you're going, um keep in mind that those
MCP servers actually might be doing
things that you don't want them to do.
Your agents might do things that you
don't want them to do either
accidentally or because someone is um
attacking you. Then something like
Docker sandboxes or similar offerings to
make sure that your agents are running
in a sandboxed in a secure environment
are something you should uh definitely
take a look at.
And with that um we're done. Are there
any questions?
We have the catch box here.
>> So, um
you showed us um how to generate um when
when we have open
uh API specification, but what about
older web services like let's say SOAP?
Because let's say we have a SOAP-based
web services for our tooling, and
can we somehow
generate for that?
>> Yes, so I think you always need some
some kind of description to generate uh
some kind of some kind of code from. So,
um
yeah, the the one one option is
basically having an open open API
specification. Um I'm sure there are
also also tools that can be used and
where might maybe also some generators
are available for. Um but yeah, it's
part from
for me I only looked to the open API
generator.
>> Yeah. I I mean uh SOAP has the uh WSDL
definition, so SOAP endpoints are
actually even better described than REST
APIs.
Um so if you find the right tool, that
data should be there. I'm also not aware
of anything that can do that, but um
theoretically it should be possible.
Thank you.
>> And I have a shirt for you because
you're the first one.
>> Uh, how do you see MCP servers and AL
engines in the future? Maybe Business
Central will become like an MPC server
where engines will be able to perform
actions directly without any middleware.
>> Yeah, I mean, we already have the BC MCP
server that is actually doing that.
Um, you see those people who claim that
we will only interact with AI, we will
have that super interface where an agent
is running and basically now it's
answering an email, now it's setting up
an order in BC, now it's creating a
ticket in Azure DevOps or whatever.
My personal history, 20 years ago I was
creating internet portals. That was
basically the same story. People told
me, "We have five different backends. We
want to integrate everything in one
portal."
I mean, it was a nice time, but actually
it failed. No one has been using that
anymore. You don't see those things
anymore. My personal belief is we still
want to have separation. I think maybe
you want to have an agent that interacts
with one or two MCPs. For example, that
I've now shown you, I'm an AL developer,
I want the AL MCP and I want the Azure
DevOps MCP because that's where my
requirements are.
But I don't see then having a BC MCP
where I'm creating where I'm doing time
tracking. I think I want to go to a
different place then.
So, from that perspective, I think we're
going to interact a lot more with MCPs,
but I don't see them replacing
everything and having that super app or
whatever that is doing everything.
Maybe that's just me, but I personally
like to keep things a bit separated and
I think the human mind also likes to
keep things a bit separated. So, I would
assume that we're not getting those huge
solutions that are replacing everything
with MCPs, but more targeted. Yes,
through MCP, maybe more than we're or
other similar approaches, maybe more
than we're now using in a year UI. So,
agents totally make sense.
But, that that all-encompassing one app
that does everything for you, I
personally don't see it.
>> Thank you very much.
>> Um
I have also a question.
It's very slightly from the topic, but I
I imagine it could be relevant to some
people here.
Um considering your product Alpaca and
hearing what you said earlier
on the topic of Azure DevOps versus
GitHub, do you have um
a personal opinion on on the future of
those products, especially um them
existing uh next to each other?
And do you maybe see a trend um
somewhere in your um client base or
something?
>> So, I think that is maybe something that
that we that we should should discuss
later on because that's a little bit out
of
>> Okay, I I totally understand.
>> [laughter]
>> Maybe the short version for me um
because I'm no longer involved with
Cosmo, I'm not directly involved with
Alpaca. Um we're still running things in
Azure DevOps and I don't see Azure
DevOps overall dying. I think um it's
very clear that Microsoft is pushing
people with their repositories very much
and with their pipelines to a degree
into um the GitHub world.
That is also not something that's
specific to BC, that's basically
happening happening all across
Microsoft. Um
I also think like 2 3 years ago you saw
things like the discussions and the
projects in GitHub where it could be
something similar to what Azure DevOps
is doing in boards,
but their progress has basically
stopped. Um you also maybe have seen
yesterday that you can now run um GitHub
Copilot code reviews on pull requests in
Azure DevOps, so you can also see some
AI features getting into Azure DevOps.
My personal opinion is the boards, the
test automation
stuff, sorry the the
manual testing stuff, that will stay in
Azure DevOps and I think that will also
stay for a very long time. I think we
also have some time while repositories
and pipelines still stay in Azure
DevOps, but there the path is clearer
that it's probably be in GitHub at some
point. And if you see all the AI tooling
in GitHub, it also just makes a lot of
sense to have it there. Um but if you're
now having a lot of work items, projects
in Azure DevOps, I would really not be
concerned about that going away. I I
don't think that's going to happen.
>> I mean I mean you can also just just
just just use both both of them, so I
see I see many partners using still
Azure DevOps for work items and GitHub
for code and pipelines in Azure CD. That
is also some
something that is working if you are
lacking the project management features
on GitHub. So I'm totally valid to do
that as well as a transition phase for
example or yeah, persistently.
>> Okay,
I think my mic was
>> Where where was the mic just now?
No, but
maybe come down for the for the
sure, sorry.
>> Okay, I have question about data privacy
because MCP servers giving us access to
the whole table or whole
database that we created the tool for
and my concern is you know about the
limitation of data for employee because
based on the
level, so
>> for example junior programmer I would
not give him permission to the payroll
for example and my question is is it
technically possible that we will build
a
limitation based on the role or security
additional security gate for the data
privacy?
>> I mean that depends on how the MCP is
authenticating. Um you've seen things
like the personal access token. If you
there just use a very broad one, then
everyone could use that. That's
definitely then an issue. But if it uses
single sign-on authentication via OAuth,
then the MCP server would have the same
permission as the user. So, then we
would be, I would say, good. You need to
take care that the right people have the
right permissions, but if you do that,
then if the if the MCP server is just
inheriting the user permissions, then
you're good. If you use, again as I
mentioned, something that has a default
key setup, that might be a bit more
tricky, but that's probably generally
not a great idea. So, I would say, make
sure that the users have the right
permissions, and make sure that the MCP
has the same permission as the user,
then you should be good.
>> Okay. I will extend my question for one
one more. Um
When asking the MCP server, the server
prepared a
response to us, and he knows that what
data it's going to send for me as a
user. Is it possible to build a gate
that the system will not allow to put
any
critical private privacy data?
For example, some identification of a
person.
>> I mean, you could try via the
instructions. Um
but
there is limits to how much you can go
there. I think there are a lot of
examples out there where people are
showing how you can
poke an agent, poke an MCP so long um
that much that it that it kind of acts
against its instructions. So, I think
there are limits to that.
Other than that,
I don't see any options at the moment.
>> I think that's always just about
limiting tools, limiting scopes of
tokens, something like that. I think
that's the most you can do nowadays.
>> Yeah.
>> Thank you very much.
>> Hello.
First of all, thanks for great
presentation, very smooth.
>> Thank you.
>> I'm very glad I'm here.
And my my question is about conversion
from real
API in installation. We can imagine that
we have a very big API and this will
result in MCP server having plenty of
tools. Can you
give us
limit
what number of tools in in in such MCP
server
is reasonable to have which
will not drain our
tokens and drain our pocket?
>> So I think it's a bit difficult to
really give you a number. I think that
also depends how similar your tools are.
So if you have many
similar tools around a single topic then
it might be difficult more difficult for
a co-pilot to to choose from
from some some tools than if you have a
lot of tools but they are completely
separate completely different topics.
Um
What I would do or what I I maybe would
look into if you have many tools of is
like implementing a meta endpoint for
for searching tools to have a little bit
more of
more more of logic in the back end that
helps you to to really select
the right tools.
I think that
that will definitely bring you more
benefits than
than trying to to to to get co-pilot in
the right direction basically and trying
with instructions and so on also doesn't
doesn't work that well all the time.
>> As Marcus also mentioned the tool
confusion really has gotten a lot better
with the with the latest models.
That being said maybe you want to use a
cheaper and older model or maybe you're
just afraid of the token burn. So
even if the model can do it it still
probably makes sense to limit to the
things that are really necessary but I
would also say it's difficult to come up
with an exact number like 50 tools then
you're good 75 then it's broken. It's
not as easy as that it really depends on
the
>> Thanks.
>> Do we have any shirts left? No?
No. Okay.
>> Okay.
>> So, now you have to ask if you're
interested, no shirts anymore.
>> [laughter]
>> Uh
is there any safety layer on MCP server
where I mean we can add something to not
take dangerous or destructive request?
Say, I mean, I I inherit uh permissions
uh to Business Central.
Uh
but still I can make a repetitive
request which can crash my Business
Central server.
So, how can we safeguard it or is there
there anything?
>> I would say the base the base approach
again is if a user can break it then the
MCP can break it. So, um
make sure that the user can't break it
then the MCP probably can't break it.
The problem is the MCP is a lot faster
and a lot cleverer or actually the agent
that is using the MCP. So, if if maybe
um someone could create a thousand um
orders within a minute, that would be an
issue, but a user could just can't um
the MCP could.
So, I think there are additional
considerations, but I would say that's
the same as with any API. So, from that
perspective an MCP is not different from
exposing things as a REST API. Um you
need to think about the load that you
expect and the um interaction patterns
that you expect.
Could be tricky because an agent might
be do something stupid that that no one
ever would think of, but um
generally speaking from a performance
attack um situation, it's the same as
any API. There's There There I wouldn't
see a difference.
>> Uh I also want to have it uh about uh
copyright and common. So, if you don't
have an API or an MCP server, we are
like actually scraping data from the
websites like you also did the speakers
and everything or there's some tools in
place that can check like the policy of
websites if we can take that data or how
we have to cope with that that we are
not doing anything illegal to get our
data that you want.
>> Yeah, I think that's that's the big
general AI discussion, right? The same
goes for training data. So, you have
those approaches where websites are
explicitly publishing, I don't want this
to be used for training data. And then
it still ends up in the training data.
So, at least I'm not aware of anything
that can do that really
um you can try to be conscious, you can
try to be ethical in that approach by
checking whether there is something, but
I'm not aware of any
really solid technical measures how we
can guarantee that. At least I don't
know anything, yeah.
>> All right, thank you.
>> We have one more here.
That's going to be a big throw.
>> Please please don't.
>> Okay. [laughter]
Oh, now we lost half of it.
Try that again.
Oh.
We lost it again.
>> Yes,
>> [laughter]
>> the mic broke, great.
>> Yes, I have a question.
So, one tool always equals to one
endpoint.
That's first question.
>> The way how we did it, yes. So, we
basically took the definition and then
one endpoint always translates to one
tool.
Um you could do that differently, but
then you need to have that logic
somewhere in the generation.
>> Yeah,
um also because there are also workflows
and toolboxes now in Foundry, for
example.
>> Yeah.
>> Uh because then if you could combine
multiple tools, so multiple APIs API
calling in one, and of course you can
use the skills, but still
navigate agent will navigate through
skills every single time. If you want
that to be a bit more deterministic,
workflow is a better option here. But
is it possible also to have a workflow
published in a such a VS code extension
that is reusable?
>> I mean, what you could do is basically
just write the code as you've seen with
the code that Marcus has generated when
the tool is called as basically just
calling code that is then calling the
back end in in our scenario, but that
code could include that workflow.
Not in the sense of a dynamic workflow,
but you could code it so that it then
would call different end points. That
would go a bit away from the idea to
have an automatic generation because
then that's a step in between, but if
you have scenarios where you want to
have a tool that calls multiple end
points, that would certainly work.
>> Yeah. Okay, thanks.
>> We are basically 15 seconds out of time,
but we will also stick around. Marcus is
at the sponsor booth. I'll be running
around in the expo. So, if you have any
follow-up questions, feel free to let us
know. And as always, please give us
feedback. Good feedback is nice, bad
feedback helps us to get better, so
either way we're happy with it.
Thanks a lot for coming and enjoy the
rest.
>> Thank you.
