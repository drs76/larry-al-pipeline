# Microsoft Semantic Kernel: from Zero to Hero

- **Source:** https://www.youtube.com/watch?v=8l7iKgiVRRk
- **Video ID:** 8l7iKgiVRRk
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 108m45s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

Ladies and gentlemen, please welcome
Stefano for his presentation from zero
to hero
[Music]
audio.
It's okay the audio. Yes, now I think
so. So, thank you everyone. Uh, welcome
to this session about AI. Uh, before
starting, let me uh
launch this. Hello from AI and welcome
to VC Tech Days 2025. I am Kakoro, an
openweight texttospech model with 82
million parameters. I am here with my
friend Stefano to show you what you can
do with AI today. Yes, I am running
offline on Apple MLX. If you think I am
cool, this is just the beginning. In
this session, Stefano will talk about
Semantic Kernel, a lightweight
open-source development kit from
Microsoft that lets you easily build AI
agents and integrate the latest AI
models into your solutions. Semantic
kernel is cool, yes, but probably I'm
better. Grab some water or something
stronger and prepare for a session where
we'll see little al code and a lot of
net code instead. It'll be tough, but if
you survive, you'll be ready to create
serious AI solutions, not little games
like those made by my friend Co-Pilot
Studio. Now, I have to stop entertaining
you, or the guy next to me will get
angry. Enjoy the session. I'll wait for
you at the bar. See you with me and
Stefano in a next AI event near you. Oh,
only if Stefano will not decide to go
biking instead. Ciao. Okay, there's also
an animation that Sorry for that. uh was
not able to uh to display.
Uh so this session is about AI as you
can imagine and uh especially the goal
for this session is uh uh giving you all
the building blocks that you need to
create in order to create AI solutions
uh that uh overcome the limits that you
have in low code application like studio
or something like that. So uh the goals
are giving you the building blocks to
create AI platform independent solution.
So a solution that can work with Azure
OpenAI, OpenAI, Google and something
like that. Uh that works with business
central. Obviously we are in a business
central conference. So this is obviously
the goal. Uh supporting agentic AI. This
is another goal of the session. So we
will see how we can support aic with
this framework. Supporting also private
AI. So not only uh forced to be able to
work with AI solution that runs online
but also with AI solution that can runs
on your own machines or or your on
premise uh network. Uh al obviously cost
is important. So also AI solution that
has as the lowest cost as possible. So
uh not forced to be uh in uh pay for
copilo studio packages of messages and
something like that. something that is
totally independent from uh your AI
vendor.
uh for that before starting uh usually
when I propose AI solution to customers
uh this is always a fight because uh
customers lots of AI projects fails
usually uh there this is a statistic
from Garner but uh I think that is true
uh at least in my experience when
proposing AI is not easy with customers
especially because uh first of all
customers often has missing AI
readiness. So they are not ready too
much for AI and they they have some
misconceptions about AI. So for example
they think that AI is limited only to
some applications. Uh the eye cost
seems. So how can I predict my eye cost?
This is something that where customers
are worried. uh AI implementation
usually is something complex at least is
seen as something complex and uh the AI
value that you have when you invest
money in AI solution sometimes is
obscure to the customer. So is something
that I can invest or not. So these are
all all uh a set a set of uh
misconceptions the customer has and
usually I see that what customer want is
uh first of all obviously an AI solution
that provides real value to to their
business not a generic AI solution. Uh
second they want to control the AI cost.
So I want a solution that I will not be
uh
I cannot be can where I can have
predictable cost not unpredictable cost.
Uh I want also that an AI uh solution
that can be uh totally disconnected from
the AI platform. Why? Because I think
that you follow AI AI is changing every
day. Every day new models new always
more powerful are out. and why I I
should be uh forced to create an AI
solution for a corporate that is using u
I don't know Azure openai models when
for example uh there's a model that is
much better for me in term of cost in
term of performance and so on from
another provider
and uh then uh the an AI solution is is
uh like any other solution uh should be
scalable uh not simply calling a prompt
uh because one user that calls a prompt
is different than 1,000 of user that
calls a prompt. Uh and uh autonomous
also we want that an AI solution should
be autonomous. So uh decision for me
work for me. Uh so for uh these goals
that I see at least are the goals that I
see that customer wants. uh in in the AI
world generic AI world uh a set of AI
frameworks are born from different
vendors. So the most famous I listed
here the most famous uh but there are
also other less famous probably uh today
we will talk about one the Microsoft AI
framework solution. So that that is
called semantic kernel. H before
starting I want to uh before starting
specifically talking about semantic
kernel I want to start very quickly
introducing some concept of AI concept
that probably for you are uh well known
but I prefer to uh to to introduce.
First of all I think that you know that
AI an AI when you when you send a prompt
to an AI model the AI model starts
passing that prompt. it it uh creates a
token probability uh for each content of
this prompt and then according to the
probability it gives you the aspar. This
is how usually an LLM works and
uh LLM also supports conversations. So
this means that uh you can start passing
first prompt. the LLM gives you a prompt
and then you can start like in a in a
chat send another uh request to the
prompt and sometimes the LLM
response that uh he has no knowledge of
the previous uh of of the question if
you send to the LM a uh question related
to the previous answer simply because an
LLM is uh something that out of the box
has no memory. So uh an LM should be
enriched in order to support complex uh
complex conversation. How should be
enriched? With tools and memory. Tools
is uh
probably the most powerful uh toolbox in
in the AI world when when we talk about
enterprise AI so corporate AI. Uh and
then there's memory. tools are things
that you can provide to your LLM in
order to uh work with your application
with your data and so on. And then
there's the memory. The memory is
something that an LLM is using to uh
work with your data. And LLMs today are
also able to reason. Reason means that
when you send the prom to an LLM, an LLM
starts analyzing that prom and start
performing a set of operations, reason
steps before
giving you the answer and you can uh
check this these steps or not. It
depends by you if you want or not to see
the reasons. Uh we we talk about the
memory. The memory is absolutely
important when talking about LM. Uh LMS
has short-term memory and can have
long-term memory. Short-term memory
means that I send you a question, you
give me an answer, I can then send you
another question and uh probably if I
don't do nothing, the other question if
it's connected to the first uh it's uh
the context is forgotten. Uh but you can
handle that and you can have a multi-
conversation until obviously you reach
the maximum capacity of uh of the
context window of this LM. Then you can
have also long-term memory. Long-term
memory means that an LM can also uh
analyze data complex data and uh working
with that complex data maintaining that
comp data context. Uh usually long
long-term memory is uh handled via
vector databases. So you have a
conversation and embedded model the
conversation is sent to the embedding
models convert to vectors and save into
a vector database. A vector database are
mandatory if you want to work with a
large set of data otherwise the LLM
cannot contain in memory in this context
window all the your data for example
coming from uh your ARP
uh
when uh when when you you handle what is
called a long-term memory so a vector
database your your prompt is sent to an
embedded model converted into vectors uh
saved into vector database is and then
when when the conversation is say
started the the LLM checks for the
vectors what what is the vector that is
more probable to probably used to be
answer to be able to answer my question
and then uh race starting and give gives
you the answer this is how uh the memory
works and we'll see how we can handle
that in uh using this framework
uh last concept probably absolutely well
known because it's was spent a lot of
time spending talking about that in this
conference
is about agents. What is an agent?
Simply is in short world is an LM power
system creating for uh autonomous take
action and solve complex task. So an
agent is an entity that is a can have
tools can have memory and can plans for
solving a particular task.
uh when talking about agent uh in the
Microsoft world there are a set of u
possibility to create agents and also in
the keynotes uh this morning uh some
some of some of that was uh explained.
So we have no code solution so fully no
code solution which spans from fully no
code solution to fully proc code
solutions. uh starting from lo no code
solution first of all you have out of
the box AI features out of the box AI
feature means uh features that you have
inside business center and you can use
as is like the copilot chat or some of
the tools that you see this morning in
the keynote so these are tools that you
can use and you cannot modify then you
in business center you have also the IL
SDK for copilot that permits you to
create I solutions your custom solution
but obviously are fully link it to what
Microsoft is exposing to you. Uh the
second step if you want to a bit more is
copilo studio. Copilo studio is a low
code agents system where you can create
the agents. Uh it's limited on models.
You don't you cannot select every model
you want but only the models that are
exposed by uh the platform. And also uh
one of the limits obviously is the
pricing. Copy studio has a pricing that
is absolutely different than the pricing
of an LLM.
uh that you can use for uh in every lamp
provider and is tightly coupled to the
LLMs that Microsoft opens. Then the
there are the procedural solution uh
procedural solution what was not
explained this morning in the keynote
but today is where we have the focus.
Proc solution is uh solution that you
can develop as a developer. So totally
independent from the platform from the
vendor. This obviously means that you
need to have full code. So writing in
something that is different from a
language. Uh in this case you have you
can you have no limits everywhere you
can create uh full code agent support.
You have scalability. You can use any AI
model any AI provider. No limits on
that. Uh they can also run everywhere as
I previously uh obviously uh they
require proposed skills. So the focus
this is the the Microsoft ecosystem. The
focus today it will be in that part. So
uh this is usually a standard Microsoft
slide that Microsoft presents when
talking about its AI platform. We will
focus our attention on semantic kernel.
So the framework that Microsoft is using
internally also to create all of their
AI platform their AI tools. Uh why we
are talking about that because copilo
studio that is great. So disclaimer is
great but in my opinion it has a set of
a lot of limitations
uh at least for creating any AI uh
solution. First of all uh it's it has a
rig set of of uh py functionality you
cannot do what you want but only uh what
uh is available inside copy studio. uh
it's a local local tool. So good because
it don't you don't require coding skill
but it's less flexible if you want to
create something that is not possible
from the local platform. uh it supports
agent creation recently introduced in
compiler studio but it's primary focus
on single agent unless uh two days ago
or three days ago the multi- aent
support is added in preview also in
compiler studio but it's not like a full
code solution uh and you have also other
set of limitation that I don't want to
list uh first of all the the scalability
and pricing uh compiler studio has uh
this copilo Studio uh also uh recently
added the support for plugins, custom
plugins and one of the custom plugins
are semantic kernel plugins. So all what
you will see starting from now to the
end of the session can also be used in
copyr studio and this can be useful in
order to extend copy studio. So if you
are pro developer they can create custom
AI solution that can you can recall
custom agents that you can call for
example from a low code solution in
copyr studio. So let's start by talking
about semantic kernel that is the focus
of the session. Uh what is semantic
kernel? First of all uh semantic kernel
is in short definition is an open-source
development kit provided by Microsoft to
uh create complex AI solutions uh with
some goals. First of all, it must
abstract AI models and providers. So it
must be able to run with different AI
providers not only uh Azure OpenAI.
Second must be flexible. Flexible means
scalable means adaptable to different uh
scenarios must be modular uh you you add
to the kernel the main part of of this
framework all the system the services
that you want. able to uh add modules uh
needs to support agents multi- aent
solution and needs to support memory
because it's one of the mandatory uh
features in order to work with uh large
volume of data. Uh here I in this slide
I've also mentioned a recently
definition that uh Microsoft has given
at the recent build. So the bank is at
the core of all its uh their uh AI
agents and platform that they provide
obviously under the hood but we are
talking uh under the hood today. So uh
probably uh difficulties for developers
obviously semantic kernel is not
embedded in IIL there's nothing so you
need to write uh required coding skills
uh different than the IL language but
you can when you have created that you
can use from language and we'll see that
in uh in the centure. So why semantic
care in business central projects? Uh
because uh when you provide pro propose
AI solution to customers not all uh
needs can be satisfied with the standard
out of the box feature. So from a
language very limited or not all these
features can be request can be satisfied
by copy studio absolutely. So uh
sometimes you need a solution that can
scale that can move between models and
so on and semantic provides a lot of
these you sometimes you need uh for
example one of the common request to
support retrieval mment generation ra
[Music]
don't cost you hundred of euros
sometimes is uh better to use uh these
tools semantic is uh
framework composed by uh four main
components. The first is the kernel. The
kernel is what coordinates all the AI
task that you define
and is something that uh the main be the
block of this framework. Then there are
the AI services. The services are uh
features that the kernel has in order to
support different AI services and
semantic use of graphs for you semantic
and graphs for you. This interfacing
between different vendors between
different providers. So you your
solution can work with Azure OpenAI can
work with all OpenAI can work with
Google Gemini and something like that.
Uh Sabantic also supports plugins. So
plugins are the two main components. You
can define plugins. Plugins are uh
functions that you can add to your uh AI
solution in order to uh do complex task
or work with your application with your
data and something like that. And then
semantic error support agents. So it has
uh components that permits you to uh
support different agentic pattern in
order to support also multi- aent uh
solutions. So uh semantic kernel first
of all what languages
at the moment it supports these
languages. So C#, Python and Java are
needed in order to create uh semantic
kernel components.
uh uh today I will use C for the the the
other stuff. So the demo part uh
Microsoft provides all what you need in
these packages. Microsofts semantic
kernel available for every of the
supported language. This is the package
that contains everything you need to
start in order to create to create uh
this type of solution. This package is
uh has a standard capacore capabilities.
So standard capabilities available for
everyone. Uh Java is only missing um
logging open telemetry log support
otherwise it's totally supported and
also as as you can see from the other
the right side of the slide supports
different AI connectors. So different
vendors connectors online connectors
like Microsoft like Google like Amazon
like and also offline connectors. So you
can also your your solution that you
deploy for the online world can also
work offline and this is something
absolutely interesting in my opinion. Uh
so first of all let's start with a very
quick demo of the basics. The the basic
when you create a nice solution the
basic is the chart completion. Chart
completion means I have a model online
deployed. I I use uh for the demo a
model deployed in Azure AI foundry. So I
don't show this in for timing but you
you go I think you know that you can go
in the Azure portal go into into Azure
AI foundry deploy for example GPT for
one model and then you can start
working.
uh so I will use that but I will show
you that uh the solution created for
copy for Azure penai can also work with
for example Google gemini or other or
Amazon bedrock that is the AI model
provided by Amazon so let's start with
the chat completion uh for that I will
switch
to uh
this project okay and I think I need to
also enlarge.
Can you see? Okay.
So, first of all, how we can use uh
semantic kernel
from in this case.net. Uh check
completion can be handled in with three
simple uh set of lines. The first well
first of all you need to reference
Microsoft semantic kernel. This is
needed. It's the package that contains
everything. Then uh you can
is create the kernel and the kernel must
be can be simply created with this line
of code. So you reference the package
and you call the create builder methods.
The create builder method is the method
that creates the kernel. So the service
but the kernel without uh only with this
line is can do nothing. It's like a
service without nothing uh defined. Uh
then you can you need to semantic kernel
as you remember in that the previous
slide you need to add services to
semantic kernel and to add services you
need to to call uh
the create builder returns an object
called builder and then you need to add
the services and semantic error supports
different services we will see later. uh
the first of all that I want to explain
is is the add the chat completion and
chat completion
uh can be different according it
supports the wrapper to the chunk
completion for different vendors so here
I'm using Azure openai chunk completion
because I want to talk with Azure openai
models but later I will show you that
for example with simply changes this I
can support Google
uh then you need to build the kernel
this This is the service that's the
starts the runs the service and now uh
after the build you have the service
ready and then you can here I simple
create a y loop if I run this
uh run
I run this here there's
a simple let me open
I use a console now uh just to show you
the component so
I'm I I have you uh a question. I I can
type a question. For example, I don't
know where is Antver
and
the question is sent to the LLM and the
LM is responding me that Anver is a city
in Belgium located in blah blah blah
blah blah blah. So it's a very simple
question. But what happens now? uh if I
respond something like nan
uh it return me could you please provide
more context because I don't know and
mill what what happens what what means
to me uh this is the first problem of lm
short memory so uh lms I send a question
it don't test the memory uh it cannot
reference that question so if you want
to support memory
Uh you need to do in your component
something different and uh something
different I want is let me close this
uh I com comment this for a moment
and I start the other
uh the other part of the demo that is
this is absolutely the same as before
I will explain
But in this case,
not this is a comment. In this case, uh
absolutely the same as before, but uh
in this case, I'm uh supporting the uh
the possibility to
uh here uh add the context to the chat.
So, so it starts a chat session but uh
I maintain the context to the chat
session. So every uh request that I send
to the LLM is saved into a a a session
called uh called uh chat in this in this
case a chat completion session and this
it maintains that context. In this case,
if I run
this
and
I need to rebuild
this.
Okay. And now run.
What happens now is that if I'm do the
same thing. So the user where is antver
it should be okay answer is and now if I
and Milan
Milan is a city blah blah blah because
he has the context. So the s the session
has the context of the previous and is
if you want to uh have a service that is
able to maintain the context with the
user uh you need to support that
otherwise uh you lose the context and uh
as said before uh semantic kernel is
absolutely uh permits you to create an
AI solution that is totally independent
from the model. So here is
for example the same supporting Google.
So if one day I decide that okay now
Google has is a model that for me is
best I can simply
change this from the previous uh uh
previously I add Azure Open AAI chat
completion. Now I add add Google AI
Gemini chat completion
uh passing Google wants the model ID and
the API key and now I support Google uh
my solution can switch between uh
different models. Uh the the rest of the
part is totally
totally different. So uh this is one of
the powerful thing of semantic kernel.
You can switch between models. You can
also have uh when we we'll talk about
agent we'll see also agents that uh
response connected to different models
and this is uh one of the greatest thing
of uh semantic kernel.
Uh let's do a step more.
Uh here is the basic. The basic is the
chat completion. Uh a step more is the
memory.
uh in uh one of the common request of
when when providing AI solution to
customer is uh I want I want to uh chat
with my documents. I want to chat me my
data and something like that. Uh for
that for that uh you can imagine that
you want to chat with uh
the content of a document.
uh you cannot uh pass the content of an
entire document to uh an AI model and
say okay can you ask her this question
because the context of an AI document
can be uh much much bigger than the
context window of the model. So you need
to support uh what is called retrieval
generation. So a technique uh that uh
permits you to uh something like uh com
transform your AI model to a search
engine. So it it is able to parse a
document uh convert this document into
vectors and uh chat with these vectors
and uh uh so for that when when you want
to uh have a complex AI solution for
example that is able to work with your
uh corporate data your imagine your
corporate documents you need a vector
database and a vector index uh so you
first of all a model that supports
embedding and uh split your data into
vectors. Semantic kernel uh wraps that
for you. So uh first of all supports
different type of uh vector databases
and then wraps for you all these uh
complex stuffs by uh introducing what is
called the the kernel memory. Uh the
kernel memory is uh a service that
abstracts all these concepts. uh for you
is just simple.
You specify what type of uh memory
service you want and then semantic air
brush that for you. Uh and this is
absolutely uh powerful for many reason
first of all because you don't need to
uh call an embedded model then call uh
for example Azure AI search and
something like that. So you don't need
to uh have in place all these uh
different calls and second because it
permits you to support without doing
quite nothing different uh vector
databases as your resource is absolutely
powerful but sometimes can also be
costly. Uh there are different vector
databases that are absolutely less
costly. One of these is for example
Azure SQL or SQL server that from uh the
last release is support vectors and if
you have uh an AI solution that needs to
work with one terabyte of documents in
your corporate it's much better to save
much better in terms of money uh save
vectors into Azure SQL that cost you
quite nothing uh instead of using Azure
search that can cost to you uh probably
uh some thousand of
Uh so uh this is a scenario that can be
useful. Uh semantic kernel memory how
works work simply you pass unstructured
data uh
documents JSON files XML files something
like that. they extract the content,
transfer the contents, save the content
is into into this vector storage and
then you can uh from your AI model you
can uh type questions something like
that and you can inter interact with
this uh uh with these uh documents
uh to show you a very quick demo how to
use the memory. Uh this is the example.
Let me zoom a bit.
uh using the memory is very easy. So
absolutely uh probably much more easy
than other uh system and with this with
with few lines of code you can fully
support
uh retrie generation of your documents
and then call this from example for from
business central and uh provide the
solution to customer. Uh personally I
use this solution in many projects for
example for chatting with the
attachments connected to uh two
documents in uh inside business central
h you can do that very easy uh first of
all uh let me okay first of all you need
to declare uh you need to reference a
package for supporting memory called
Microsoft memory
uh this is a service that
uh permits you to support the array
techniques from uh for uh for for
semantic kernel and then you declare
your uh
your object kernel memory. It's like
like semantic kernel was builder here is
kernel memory builder the object for the
memory and the memory needs to have uh
an embedded model. So here you you you
need in your you need to have deployed
uh in your uh this in my case I use
Azure OpenI. So in my Azure OpenI I have
an embedded model text add 003 for
example and I have an LLM GPT41.
So here I'm passing what is the my
embedding model. So my
uh details of the connection of the
embedded model and here I'm passing the
details of the connection of my uh sorry
of my uh uh GPT model. So my my model
that needs to interact with this data
and here is the the part uh there are
other configuration totally optional for
example maximum number of token from for
respon something like that. So I omit
that. But here is the part that I want
to uh focus. So
what memory previous I define that for
the memory I need an a vector an
embedding model parameters
LLM parameters and then what memory I
need to use for storing my vectors. And
here I can select different for the demo
I use what is called the simple file
store. Simplify storage means fast uh
file system. You can if you have a small
solution and you want to pay for
nothing, you can save the embedding into
a file system. Your document will be
parsed into a file system. You have a
folder with a set of uh unbelievable for
you uh data. But these are the
embeddings that the LM can use. But
obviously in a production environment,
you will not never use that. Uh so I
I've leave the comments for example you
can use SQL server memory SQL server
means you can pass a connection string
of an Azure SQL and all the vectors are
totally are saved of the documents that
you pass or the data that you pass are
saving to SQL server in a in a fully
transparent way for you. You don't do
nothing or you can use other providers.
Uh the Azure AI search is the Microsoft
provider. So Azure AI search if you want
to use Azure AI search use this pass in
the connection string of Azure search
and you can work with Azure search SQL
server is what I suggest for many
projects today cost why nothing
uh but you can also use third party
quadrant for example is uh a vector
database absolutely powerful that you
can use uh if you know uh
uh central Q from my friend Dimmitri.
Central Q is uses quadrant for storing
documents and vectors. Uh it's totally
up to you. So you can decide uh what is
the vector service that is better for
you. For the demo I using what is uh
what is the uh
poor uh solution. So the file system
simply doing that what I'm doing that
I'm I'm creating as in the previous demo
a chart completion service and then I'm
saving the documents. So here I'm I'
I've done in all in a single file in
this in this case. So what what is doing
I'm passing a the path of a do that I
want to to give to the LLM so to store
into the my vector database in this case
is the business central licensing guide
and uh with one single line I can pass
that to the kernel memory. The kernel
memory do the work. So pass the
document, save the vector and the vector
is saved into the uh storage that I've
uh decided in my case is the um
file system
then I can start the chat. So if I run
uh
this
uh let me build because I don't remember
if I change something. Do I prefer to
rebuild?
So if I re I rebuild the app and I run
the app.
What happens here? Uh
the code starts and it parse the
document.
Obviously you can load the document
every in when you want and then uh it
starts asking me my prompt and then yeah
I can uh ask something like uh I don't
know explain uh the probably the most
tricky question for a business central
uh for a business central related agent
is explain the team member license
because so Microsoft doesn't know they
are respons So
remember license for business central
and
here the LLM is not going to internet
because it automatically is able to
discover that uh for the answer of this
question I have an embed in database and
I can uh retrieve data and you as you
can see here is it's giving me the
response so blah blah blah blah blah
blah uh this explain the uh all the data
about the business central team member
license and it's also give him the
reference. So the reference is not
coming from uh
internet in this case but it's coming
from the the document that I passed to
the memory. So imagine in a real world
scenario, you can uh pass every document
you have uh attached in business central
and then you can have inside business
central the possibility to chat with
that document
easily without doing quite nothing.
This is what is called uh retrieval
generation. So support for ra very very
easy. So you you you don't have to quite
nothing. Three lines of code and you can
fully support rag with the uh with this
tool.
So I close this and let's do another
step
in uh explaining more complex features.
Uh
previously we talked about two powerful
features that an agent can have. uh
memory and we saw the memory and
functions plugins
uh functions or plugins. Semantic uses
uh this terminology plugins plugins is a
group of function that you can they can
be exposed by an II service and these
functions can be used from the the AI
service to interact with the external
system with your database with the
different application and so on uh
automatically without doing nothing. So
you provide a set of tools to your AI
agent and the AI agent is able to
automatically use this tool or not
according to the question that he or the
task that you need to to support. So uh
semantic supports two types of plugins.
Uh what is called prompt templates from
prompt templates are uh the most simple
way you can define templates in plain
text and is able to use and creates
automatically plugin for the text or
native function. ative function means
something that you can define in code.
Uh
plugin uh we will see a demo about that
but a plug-in uh with native functions
can be the first is text and we will see
how to do that. The second is plug-in
with function. With function means that
you need to create a function in code
and this function must be the code with
the kernel attribute uh the kernel
function attribute. Uh
semantic is able to discover when you
send a request to the LLM what function
need to invoke in order to satisfy the
particular task. If you declare that
that function as kernel function uh can
a kernel function can have on or can
have parameters or not. It depends by
you. Absolutely important to as in the
slide to uh add the description
of parameters or and on the function
because semantic uh an AI model not in
general an AI model when calling a
function uses the description in order
to uh know how what what is the function
that I need to call for satisfying this
uh this task.
Uh so you need to declare the function.
Second step you need to uh add the
function to to the the kernel instance
and this can be done with this uh the
first line red uh line of code and that
the third you need to say to the kernel
that you can out invoke the function. So
uh when you AI model want to satisfy a
task decide the autonomous to invoke the
function that you need to perform the
task. Uh
another uh so this is the standard way
and another very powerful recently
introduced way to uh enrich semantic
kernel with function is uh
using logic apps. Logic apps is uh I
usually call it the the father of uh of
power automate is a more pro power
automate and uh it's a low code tool
that permits you to create workflows and
semantic logic apps as first of all a a
feature that can be can be uh expose the
definition of the workflows as uh
swagger. Wagger is a JSON format and
semantic error is able to automatically
discover if you have logic apps
workflows it's automatically able to
discover that and automatically invoke
these workflows if uh user prompts a
question and it discovers that with this
workflow I can answer this question and
this is a I have a demo for that this is
a nice mixture mix for because you in
this case you don't need to define
functions in code. But you can have a
local developer that can create
different workloads and you as a
developer simply with this line you uh
def say to to the kernel okay dear
kernel go into this URL that is the
swagger definition of of the logic app
and then discover all the workflows and
do what you want and I will show you how
it works in a few minutes. So
first of all uh the basic of the
function that if I don't remember is
this project
uh
let me go because I know it's not this
project I think I not open the project
uh the first is this
so function three way to define
functions the First is uh
using what is called prompt template.
Prompt template is simply a function
defined in this way. So is a txt file
defined
in this way. So message ro user and then
uh you you can write the prompt.
Here is a stupid function that I
created. So tell me an interesting fact
from word about an event that took place
on this is the way to pass parameter.
This is a parameter.
Uh
be sure to mention the date blah blah
blah. Uh then I have a
a a JSON file that is uh
this is totally documented in online.
This is a way to create uh prompt
templates. This file says that uh
this function defined in txt. This is
the description of the function. This is
some settings that you can have. For
example, maximum number of tokens and
something like that. And this is the the
parameters that the LLM need to pass. So
a parameter called today that contains
the current date.
Uh what happens here is that uh if I
uh run
if I run this the the application starts
discover that uh today is uh June uh 12
and this is the effect that occurs in
June 20 in 1987 US President Ronald
Reagan delivered blah blah blah blah
blah blah. This is a uh prompt template.
So a function defined
uh in a txt file.
Uh this is a possibility. I never use
this possibility honestly. Uh the most
uh powerful way to define uh a function
is what I will show you in the other
example. So is by defining the function
from code
and uh
defining the function from code means
exactly what I uh explained this slide.
So I can declare a function
in a function is simply a procedure
decoded with these attributes
with parameters or not.
uh important as I said before specify
the description also if you have
parameters. So in this case my function
is get current day that uh returns uh
the current date because uh I want to
retrieve the system current date to pass
to the the question and then uh semantic
kernel simply when I declare my uh
application I can simply
add this line.
So uh here as we saw in the previous uh
demo I create the kernel
I add the I add the chat completion
service because I want to interact with
my model and then I enrich my kernel
with functions and semantic error
supports this uh plugins dot add from
type
and this means that it goes for in this
class
this class it retrieves all the kernel
function and adds that to the context of
your the of the the AI service and then
I can start typing uh here I I is my
prompt exactly like uh in the previous
example tell me an interesting fact blah
blah blah and in this case if I run uh
sorry my mouse is crazy
uh but why don't okay uh if I run this
uh I have I should have at least the
same
uh not not this but this
uh
it's not easy to type with the light
okay I should have the same uh asverse
but in this case the function is native
so native means defined in code.
Uh the third option
that I previously uh explained is the
live is a bit more complex option and uh
I will explain this complex option in
this
uh here is my Azure portal
and in my Azure portal I have uh a
different set of workflows created by
using uh Azure logic apps. So I have and
this workflow uses uh I don't know for
example open one this workflow are using
logic apps and is the business central
connector and every other connector I
want. So in this case it's a workflow
that uh work on the use the business
central connector for searching for
production orders
and uh giving a response. uh if you want
to to define
uh workflows for an AI model callable
from automatically callable from an AI
model in low code in this case using
logic apps you your workflow needs to
start with an HTTP empty but uh this is
mandatory to have an HTTP connector when
a request is received as startup for the
workflows and uh logic apps have an
option configuration option uh that
permits you to expose uh a swagger as
JSON definition that is this you cannot
see probably but it's a big JSON that
contains
uh all the definition of the function
that I have because as you can see here
I have uh different workflows
uh for each workflows my local
developers has created the workflows for
uh with the business center connector
for doing a set of stuffs, retrieving
production orders, uh uh changing
inventory and something like that. And
uh uh
here uh the JSON exposes
the workflows and the endpoint to call
these workflows.
uh what I have done here
uh here if I remember okay here is uh a
very
basic demo that I don't know where is
sorry one second okay
uh this demo
uh here I I I use a web application but
I the focus is not to the application
the focus is what I need to do in order
to do that. Uh here I'm asking something
like list production bombs containing
the item a particular item because I
want to use an LLM in my production
department my production department uh
uh wants to have capability to interact
with the production order and for
example one of the feature is I want to
know if an item is present in some
production bombs because maybe I want to
change the item or something like that
and uh I can send a request
and uh wonderful. Let me
think lost the connection.
Uh let me ret try to reopen because I I
previously opened the browser but the
switch networks.
So I'm logging.
So what I want to show is that I'm
typing a question in this interface and
the interface automatically is able to
discover from my set of workflows what
workflows need to be called in order to
satisfy this question is able to call
the workflows and give me the response
and I can have then the logs of the
requests coming from uh from the
from the workflow. list
uh I don't remember the item name uh
production bomb
containing the item
item is SP
bomb
if I don't have problem connection okay
now it's asking so it's able to call my
workflows.
My workflow goes in business center,
search for the data and then it's able
to retrieve me the data. How to do that
is absolutely very easy because you
don't need to do quite nothing. Simply
from your workflows, you need to
uh I want to enlarge the resolution. You
need to
go here and uh add this line.
This line is called uh from your kernel
instance import plug-in from open AI API
as sync. And this this means that the
work the kernel is able to inherit all
the workflows coming from this OpenAI
definition and automatically call them.
So if I go in my uh Azure portal,
I don't remember where I have the Azure
portal opened. Uh here
uh if I go into my Azure portal,
if I check
my workflows, uh probably probably
this
I don't Uh okay this is the workflow
that was called.
So the AI model automatically has called
the workflows according to the question.
So is able to automatically uh discover
and c the war. This is useful because a
local developer can define that.
Let's jump. So here is how functions
works.
Uh now let's come let's put all this
together and uh let's start talking
about agents.
Uh semantic supports agents. Agents
obviously are entities that can uh work
autonomously to complete task. Uh
semantic has recently introduced what is
called the agent framework. So a
platform to define patterns for
supporting multiple agents working
together and something like that without
uh doing too much uh complex operations
and uh
the framework is important because uh
you can create autonomous agent, you can
create agent that works and takes
decision accordingly to uh set of
collaboration patterns and uh can
interact with also with the human in the
loop and uh semantic error supports at
the moment at least uh this type of
agents. So Azure AI agent, so agent
defined in Azure AI foundry supports
chat completion agent. So agent defined
in code by you uh that can interact with
the model. Supports open AI assistant
agent. So agent created created in
OpenAI uh using the assistant API.
Supports compiler studio agents. So if
you have an agent deployed in compiler
studio or created by someone else in
compiler studio you can uh use that also
in uh semantic kernel applications and
they can call different agents and also
support bedrock agent. Bedrock agents
are agents uh in the Amazon platform. Uh
these are actually the the agent part
the agent uh platform supported and also
it support uh Asian Asian patterns.
Asian pattern are uh orchestrations of
agents
different partner orchestral agent and
uh it supports the following part. The
first is the sequential orchestration.
Sequence association means that I can
define different agents and then the f
first start the first agent then the
first agent does some things pass the
the the output to the second agent
second a and then the third and so on is
sequential and then at the end I have
the response.
Uh second step is supports the
concurrent orchestration. called
orchestration means I have an input.
This input is shared across all my
agents. All my agents works on that
according to the task that an agent is
uh need to do and then uh the output of
that is put together and then I have the
response. This is the concurrent
orchestration.
The third partner is what is called the
group chart orchestration. Group group
chapter orchestration is uh a
collaborative conversation between
agents
uh plus the human. Sometimes seantic
need can detect that for the particular
question I need to ask to the user
something more. So you can also take the
human in the loop for that and then uh
so a set of collaborative operation
between the main uh service and the
valuation you have and then you can have
the response at the end. And the last
pattern that it supports is the what is
called the end off orchestration. The
end of orchestration means that you you
give a task to your agent. uh there's a
main agent that is inter intercept this
task and it redirect this task to the
other agents according to the con the
the type of task that you have uh
specified like for example a if I have
an order entry uh or a refund service
one is one one agent is is need need to
create orders and the other need to
create refunds. If I have a request
about uh creating a a new order, the
request is sent to the order agent not
to the other. So this is what is called
the end of orchestration.
So let's see uh that
how to support multiple agent in
semantic kernel the uh
semantic supports multiple agents in
this is an example
uh
supports multiple agent partners.
Let me reduce the resolution.
Okay.
uh when using multiple agents you need
well as usual you need to define the
kernel same as before. So in this case
I'm using Azure OpenAI chart completion
passing my parameters.
Then I need I can I I need to define the
various agent that I have and uh uh in a
most simple way an agent is what is
called uh this object. So check
completion agent name of the agent some
parameters. So the agent has a name must
have a description.
uh these are useful for the current in
order to discover how what is the agent
need to do need to have the instruction
the instruction is the prompt that an
agent need to have obviously in this
simple example I place that into the
code uh recommendation is if you have
complex solution not don't place the
prompt into the code but uh take the
prompt from outside because you can turn
up uh accordingly without changing your
code and then uh the agent needs to have
what is the kernel instance this uh why
the kernel instance attached to an agent
because in a complex AI solution I can
have like in this example three agents
one agent work with with Azure OpenAI
GPT41
agent works with Google Gemini
one agent Google works with uh uh I
don't know GPT for something like that
uh in this case I have different agents
the analyst, the copywriter, the editor.
One of each of them has a task.
So, uh these are my agents.
The the analyst need to extract key
concept from a product description. The
second is to write a marketing uh
description from what the first a struct
and the and the last the editor needs to
uh
correct the grammar, check the grammar
and give me a a business description of
of my item. Uh
here I I'm using the first pattern. So
the the uh sequential pattern. So after
defining the agent
uh you need to start an orchestration.
The orchestration is uh uh
how I I need to orchestrate the partner
in the the various agent in this case is
sequential. Sequential means that first
need to work this agent,
second needs to work this agent, third
needs to work this agent. So it's
sequential
and in this case I start the runtime of
the the of the agents. So my agents are
up and running and then here I I started
a prompt. So my prompt is a description
of an item and then like the stupid
example uh is uh
an echofriendly stainless steel bottle
that keeps drink uh for 24 hours. and
then my my is work in order to create a
more complex text. So here I'm running
my application
and uh
what happens here is that
uh
I have my input and my agents after a
bit of time that works together and
gives me
this text.
that is the uh the output. So first he
has taken the
the description. The second is create a
more marketing description. The third is
check the grammar. This is the output.
So my agent start in sequence. Uh there
are different uh other types of agent. I
I don't uh very quickly concurrent is
the same. Here I have an example of
concurrent
uh where I have a company info agent and
a company stock market agent because my
goal was I ask you information about
Microsoft for example and the first
agent in parallel situation need to work
the first need is to check for
retrieving information about a company
and the other retrieving stock market
because maybe I want to invest in
Michael so I don't know and uh
in this case I start a concur concurrent
orchestration concurrent means that I
need to pass the name of my two agents
and these two agent will be started
concurrently.
So I here I'm uh I'm asking give
information about Microsoft and my two
agent will start concurrently. So if I
quickly
do this
and do this
let me rebuild everything.
Okay.
So in this case
my we start concurrently they start
thinking
and after
thinking one needs to retrieve
information about Microsoft as company
and the other need to retrieve
information about Microsoft as marketing
value.
Uh at the end I have
a an analysis. So my here is yes has uh
I have analysis mix both. So uh as you
can see I don't know where it starts.
First I have the analysis about Micros
no no and then I have also the values of
micro as uh in terms of marketing. So
the NASDAQ value and something like
that. So two Asia has work in parallel.
In this case,
the last and probably more complex
scenarios is the end of the end of means
that I need a task to an agent. I have
different agents like in this case this
case I have created uh different agent
the sales office agent that is able to
uh if you remember the chart say there's
an agent that retrieved the request and
in my case is this agent. So sales
office agent that handles customer sales
requests. Then I have two other agents.
The item availability
agents
uh that is an agent that is able to uh
responsible for checking the
availability of items in business
central.
Then I have an order creation agent. So
handle the creation of sales order for
the requested items if there are
available items in business central.
And then there totally different agent.
So the order refund that uh needs to end
refounding of orders. So not link to the
others. Then here I starting the end of
the end off means that there's a main
agent this says office that uh according
to the task can decide what is the agent
that need to solve this task and the end
of uh when you define this pattern uh
you need to uh specify what what is a
start first. So the sales office is
receives the uh the request then uh what
happens it can it can redirect the work
to these three agents item availability
or the creation and refund and then you
can also have other movements. So if uh
the item availability agent receive a
request that is not pertaining to him he
can transfer the request to the sales
office again.
The same for the order creation. If if
the answer is not for him, redirect to
the main. So the main is act as an
orchestrator.
Uh then you start the orchestration.
Uh the orchestration can also have the
human in the loop. So if you want
support human in the loop. So also uh
permitted that the agent can ask the
user more question. You need to uh
simply add this parat pattern interation
call back
what equals a function this function and
in this function uh
you need to support
uh you need to have the signature.
The signature means that the agent can
redirect to this function if something
requires a human intervention. And here
I simply uh having uh asking the input
for the user.
Uh if I run this,
I need
to unccomment something. So not this
demo. But now let's move to this Let's
start this.
Okay.
Uh not
Okay. I'm asking uh here my agent is
listening. So uh I can type something
and the first agent that intercept the
quest the the user question is my first
agent. What I call the sales uh the
sales demand agent. So I'm asking
something like uh I need to order uh
five uh sorry I 16 because I've uh in my
code I've not showed that before
starting a in my code I I've uh this
code I've also obviously when you have
an agent
so this agent one second Sorry.
Uh when I declare an agent, you can also
enrich the agent with functions. And uh
where is my agent? Okay, this agent.
These are all my agents. All my agents
can have a function. For example, the
first the the item availability agent to
check if I an item is available in
business central need to have to do
something. And here I've created a
created a function called item
availability plugin.
uh that contains the find the
possibility one to go in business center
and checking for the availability for an
item and this agent has this tool
available for performing this task. The
same for the other this tool simply
uh are functions like this.
So it's a function like previously show
kernel function my function with here
should be the call to business center
for this particular item to check for
the availability. Now I returning 10 as
fixed because uh just for a demo
purposes. Uh if I go into my uh I need
to order 16
item 01
uh the uh the agent
as you can see from the response the
first agent sales agent intercept the
response redirect the response to the
item availability agent. The item
availability agent has checked for the
the availability is returning 10.
I want to order 16
is asking okay should I proceed to
create an order for the available
quantity or not. So it's asking
uh for interaction and I can uh yes
order uh
order
six item uh 01 I don't know if the sales
order is created successfully blah blah
blah so is able to redirect the request
to the uh right agent perform the user
interaction if it needs something like
in this case I don't have enough
quantity in my warehouse to satisfy the
request should I what should I do uh so
you can have the human in the loop
uh
obviously what so this is the the agent
orchestration you can define multiple
agents and run this have m multiple
agents running and working uh all this
demo at the moment I've done uh using uh
a console application because it's much
quicker to to do that but uh uh you can
do everything uh also from business
central. So uh here is another example
that's a a real example uh that I have
in uh for example in business central.
So in business central
uh
you can call uh AI function in two ways.
Uh the first is standard
uh Azure OpenAI
uh standard way I SDK for calling uh uh
Azure OpenAI and the second is
like in my case in this demo I don't use
standard Azure OpenAI feature so I don't
have these settings but instead I'm
calling
my service running in an Azure function
and my service is a semantic kernel
agent that is able to uh receive my
questions and working with my business
central data like with the toolbox that
I previously uh display in the in the
demo. What happens here is uh uh yeah I
can ask to my data uh not only uh basic
question like in the copilot chat. I
think that you use the copilot chat the
standard business center you can ask
some questions but you if you can uh if
you start asking for more complex
questions it fails because it's giving
answer that is not able to answer to
to to some question something like that
here I can in this example for example I
can do something more uh I don't know
something like uh show
says distribution
sorry if I don't able to write but it's
not easy to see the the keyboard by
region
uh probably the first call will be slow
because
I have a a service now deployment in a
very low
tier the other call will be quicker but
the first is uh is the call start of the
function
And what I want to show is that in this
case uh let me redo because
come on
it's the the function under the hood
that it was sleeping
because the Azure function goes in.
Okay, now it's working. uh
the the agent here is able to perform a
more complex data uh operation in my
data. So I I I ask not a simple question
but here you need to perform an analysis
of my all my sales and uh giving me the
response. So I it's much more uh complex
and he has given me the response. So
this is the the amount of the sales that
I have in my business central data
grouped by region. But I can also do
something like uh I don't know uh
something like uh for example analyze
the inventory
level
uh
how the inventory level maybe how the
inventory levels have changed
in 2022 because Kronos demo is 22 22 2
2023 my demo for our top 10 items. So
it's it's complex
because you need to go what what are you
need to perform a set of queries to
retrieve that what are my top 10 items?
Then I need to for each top 10 items I
need to go into uh checking the item
level. So it's something that
quite complex for the
for the the
JM
to perform. Yeah. What I want to show is
that it's able the service is able to uh
also perform this and it's giving me the
output.
Uh so you can perform more I can I can
do other example that I don't want to to
spend a lot of time. So he as the agent
is able to do a lot of queries
uh in my business central data a set of
queries not one a set of queries in
order to give me the response uh what's
there under that
uh first of all
there's
a business central app
is up
and
here I don't want uh uh so the most
basic stuff is uh knowing uh all the
question that the user can do and then
provide uh the the tool to the to the to
the to the kernel but I don't want to do
that here I've done something a bit more
complex so uh in my uh uh application
this application uh in the prom dialog
page when the user types the request the
pro dialog page uh creates a uh a prompt
that contains all the definitions of the
APIs that I have available in my
business central environment. So it goes
into the
uh
page metadata
retrieves the page with type APIs
creates the data retrieves the data from
the APIs for each APIs retrieves the
fields available in each APIs and this
is transforming into a YAML that I'm
passing to my as prompt to my kernel.
So my kernel now knows the question and
now he knows that for answering the
question he is available he has
available all these set of APIs custom
and standard
uh with this type of fields.
So he has all the tools but now he need
to use so how can an AI agent okay an AI
agent now knows what what are the
available APIs but how he can he use the
APIs correctly.
Uh this is handled in the prompt. So
first part is the my business center
application and my business center
application simply calls my not Azure
OpenAI but uh uh it calls
uh not here but uh the prom dialog page
sorry I don't remember okay it calls uh
my function
so it it calls uh my uh semantic kernel
function that is
this
so it calls my function where I've
exposed
my kernel passing
the prompt so the the the prompt
containing the API definition in the
function and the function is this other
project
in the function I simply retrieve the
pro the the request and according to the
request I retrieve a prompt and the pro
the the trick here is the prompt
uh retrieves the prompt and then it uses
the kernel to performs the request and
the request there's this
uh function
kernel function
that calls a business central API I in
this in a particular environment is the
prompt that redirects the API calls. How
the prompt is doing uh is done. The
prompt is this prompt something
something like that. So here I I am it's
a real world application. So as said
before in a real world application the
prompt should not be in the code. So
here I have a prompt
that is downloaded from key volt for
example and the prompt for me is a
complex text file this text file. But uh
the key part of this text file is that
here I'm explaining
to the model how an API should be used.
So uh you have a set of APIs.
Accordingly to this set of APIs you
uh
this is the how you should format the
URL.
So URL in for standard API must be
formatted in this way. Uh for custom API
in this way
uh how you should apply filters
P filters must be applied accordingly to
a data filter. So filter here I am
provide all the filter they can apply.
So all the rules I'm explaining in the
model how to call the APIs
and then I add the extra guidelines for
for example for end dates uh uh if you
have an error do do that and something
like that. So with all this set of
instruction with the list of my APIs
and also the metadata of my APIs is able
to perform the query. So this is this
you can have a quite nice performant way
of handling uh complex data much more
powerful than for example the standard
copilot chart that you have uh inside
business central standard.
Last part of uh semantic kernel is this
uh because
I think that uh you have listened these
terms today. So model contract protocol
modeler is an open protocol created by
entropic and that now is becoming a
standard and the the the great thing of
model contract protocol is that you can
support this scenario. So instead of
having uh
is there the okay instead of having an
LLM that uh for each question goes into
different data sources according to its
uh each data source has its own
capabilities own APIs and so on. Now it
simply interacts with an entity in a
standard way and then uh this server is
able to uh have the interface for the
particular data source. So this is how
the MCP protocol works. So the O can be
different
can be business central because center
will support MCP is in work in progress.
Uh can have a code like in we show it
this morning in uh in the keynote
uh can have can be GitHub copilot
for me should should be the first choice
at the moment. GitHub copilo can support
MCP from not not reach and GitHub
copilot can call for example uh every
MCP server you expose and can be
different al also copilo studio if you
want can support MCP so uh the every
client that support that you simply
register this into the client and then
uh it's able to call each uh
target system by using that protocol And
this is absolutely important because you
can if you create this
uh this can be used by business center
can be used by one of these tools can be
used by compiler studio and and this is
why Microsoft has started adopted this
technique and will change in the future
all uh or at least many of the
connectors
uh available today.
uh semantic supports two types of
protocols uh not semantic sorry MCP
supports two types of protocol for
connecting with the target system. The
first is uh what is called standard
input output streams. So it is useful
when for running locally agents uh I
have an MCP server running locally then
I use this protocol. If I have an MCP
server running online, I use the other
protocol HTTP via SSA server side
events. Uh using that semantic supports
MCP. So if you you have an agent created
in uh semantic error like we show in the
demo, it can support MCP with few lines
of code.
First is uh declaring this
uh you you need to add the package MCP
client factory package and then you
create your MCP server. You when someone
gives you an MCP an MCP server need to
provide you the URL and the protocol
that it supports
and then you can use you from an MCP
server can have a tools. So a set of uh
functions available you can use with
this line
list all the tools that this server has
available and then use from your model.
Uh just to show you a very quick demo on
that
uh this demo.
Let me close this
here. For example, I have used
I have created a very simple agent
uh that uses the MCP server provided by
Playright. Play is a nice tool uh that
is able to run uh applications uh by uh
going into uh opening the application
simulating the user interaction.
uh so here I in my uh application I've
declared
the MCP server from play right so using
uh this is running locally so I use this
method
the name is play right the command to
run is this and this is a command to run
the SCP server from playbrite and then
from my agent I I simply asking
summarize the latest articles from this
site my site and open the first link and
summarize its content So I I want that
this agent is able to open this site,
check the light latest article on this
side, summarize that for me and give him
the response. If I run this
uh
you should see that
if le is working. This is the delete.
the website is opened automatically. The
last latest article was open
and then the the AI model is uh reading
my latest article
closing the website and here is the
summary.
So latest article the title using a
static API address from API discusses a
solution blah blah blah blah blah. So
this is a summarization of my item and
this is useful also for example for
simulating testing the user business
center user interface. So MCP server can
open business center can simulate
clicking someone something in the user
interface and doing task. So just to
show that an agent can also call an MCP
server. MCP server can be the Microsoft
provide the MCP server. So working with
business central data easily we do doing
nothing as we show the keynote today.
uh or your custom MCP server or your
third party provided the MCP server. So
uh simply declaring the MCP server the
key line of the code is
uh this
uh not this sorry this.
So you declare the server and then
when you have declared the server you
need to say okay now give me all the
tools that you have
and is downloading the list of tools
that the MCP server is exposing and then
it can perform the actions. So it's uh
absolutely powerful for making complex
task. This will be probably the future
uh because the the idea in the future is
that all the connectors will be probably
moved or at least not all but quite all
the connector related to business center
agents will be moved to MCP
uh so just to uh close
uh semantic why in business center
solution uh because it's powerful uh
because it permits you to create no
limit solution So you can it can
overcome all the limits that you have uh
in compiler studio that you have in the
IL SDK. Uh you can work with different
AI providers. Uh you can uh customize uh
the workflows in multiple agents as you
want and is scalable. Uh we can scale
according to your needs.
something that copy studio cannot do
something that ILSDK cannot do because
it cannot scale as you want and also is
platform independent and this is
something that uh in many real world AI
scenarios is uh is useful so
pros and cons lots of pros cons is that
uh it's full code so it requires uh pro
developer but as explained uh also in
the keynote uh this is the third part of
the agent AI possibility that you can
have. So it totally up to you to select
if you want to go for the low code
solution compiler studio with all the
limits with all the costs and or full
code solutions
uh no cost but except obviously the
interaction with the model uh but no
compile of messages no simply you you
pay for the tokens and nothing more.
So this ends uh this presentation. I
hope that you you have at least the
building blocks for starting exploring
this uh uh this framework. I suggest to
start because if you want to create
complex AI solution is great. If you
have questions,
lots of questions.
Uh I
uh should be a microphone here.
Uh let's start with
microphone.
maybe works that I don't know if uh I
don't know no less
question uh is it completely separate
from uh standard uh copilot chat like um
user would have to navigate to our
implementation specific pages and could
not uh call functions from chatting with
general chat the chat you mean the chat
in business central yes no It's it's
totally separate. So the chatting
business central uses this tool uh under
the hood. Uh obviously you cannot uh
Microsoft has not yet opened the uh the
business central chat to the general uh
public to customize. So you cannot
change the general part. So this is uh
something totally separate from the
chat. It's a tool that you can use if
you want to create your own AI solutions
uh maybe more complex AI solutions
inside business central you can use this
tool uh but it's absolutely separated
from the standard uh AI chart. Thank
you.
Uh, I have sorry for one second. I have
probably also some t-shirt if you want
one.
Ah, sorry.
Second qu I don't know the order.
Hello. Hello. Yeah, thank you. Okay. Uh,
my question is alo about multi session.
Is it possible to to share them maybe
the history or something like that with
the team or with the organization so
that we can earn profit from that if you
can handle multi multiple session? Uh
yes absolutely yes it's absolutely
possible you can handle multiple session
with the agent something that usually uh
is done in a real world applications uh
using a full code solution you have no
limits on that. So uh it's totally up to
you uh deciding what is the limit of the
session. Uh
usually at least in my case I use I
deploy this agent in uh running for
example in Azure function. uh it's
totally up to you to scale the number
the the service in according to the
number of session or limit the rate
limited you want to have a number of s
multiple number of sess is absolutely uh
supported by design so no limits on that
sorry I I go into this order because I
see that the
h yes sorry
yeah I I can see you. Great. Um but
probably is is better. Yeah. If we have
too many sessions that we want to have
in the history, are we then um yeah
reaching the maximum token limit or that
uh obviously the token limit is
something that you need to handle if you
need if you have multiple session. Uh so
in in a real world application I usually
suggest to uh scale the model. So scale
the model means uh you cannot have uh
one single deployment of for example GPT
for one serving 1,000 of user working
concurrently uh you should uh uh in this
scenarios if you reach token limit is
for session uh first uh but obviously if
you have imagine that you have 100 user
talking with one instance of GPT41
uh you have you probably reach your uh
subscription limit or something like
Yeah. So in these complex scenarios when
you have multiple you should deploy
different instance of the models and
then routing the correest. Uh it's very
easy routing the request. You can deploy
I don't know uh you have 100 users you
can deploy five instance of imagine GPT
for one and then redirect 20 users goes
to this then it goes to this
automatically it's uh can be handled by
by the platform or you can wrap for
example in I don't know Azure API
management or something like that you
you can this is exactly what Microsoft
is doing under the hood when you call uh
standard standard uh the standard Azure
AI chart or the future managed service
uh that will be released uh in few
months uh there's not Microsoft is not
deploying one instance of uh GPT for
every customer in the world but is
deploying multiple and requests are
routed accordingly to the load so it's
to you can do that totally up to you
yeah great and then also for for one
session with some yeah some huge chat
history for for session you have a limit
uh for for a single session you have you
can have a limit on pro limit on prompts
is per interaction so you cannot pass
extremely long prompt for a single
interaction
and uh the limit of prompt in chat is
uh not is not the limit limited by the
model but is limited by your uh your
subscription. So you can if you don't
overcome the limit for request you can
talk with the model for hours without
problems. Uh so you have two level of
limits.
Great. Thanks.
Oh
uh I don't know
also the microphone.
Hello. I just have a quick question. you
showed like three examples of doing kind
of the same thing when it comes to
plugins or the things you can do or tell
the AI to do like the tools. Um, first I
understood that you put in kind of gave
them instructions through the same
prompt and just gave basically a single
tool just to retrieve from the API but
then you can also have that through
logic apps for example. Yeah, you just
get that and then the more advanced and
hopefully we get is the MCP who already
has that already defined for you. Let's
get a standard way. Does that always
affect the prompt size at the beginning?
For example, it in the first example,
you have this large part of the prompt.
Yeah. You have all that description in
it that affects, you know, the initial,
let's just say the tokens you're going
to use on on that request. Is that true
for the other two? No. No. the tools
don't affect the size of the problem or
the prompt. So uh you the prompt is uh
your specification of uh instruction
that you give to the the model. Then the
model can be ar and this this affect the
size of the prompt. Then you arach uh
the other tools. Tools can be
uh don't have nothing to do with the
prompt. So tools are uh set of uh tools
that can be used by the model to answer
a particular task or solve a particular
task. These tools can be function that
you define in code or workflows that you
have uh exposed to the today agent like
in the the example that I've done with
the logic apps or uh MCP servers. These
are the three macro
uh types of function that you can
define. But this does not don't affect
the the prompt size. So you can your
tool your agent can can have uh 100 or
of tools available and it doesn't really
affect performance and the execution of
the prompt if it has 100 tools. No, they
don't affect the the limitation on
prompts because you don't pass that in
prompts. So you attach that in uh the
tool part of the the model not it's not
in the user prompt you your limit is in
the user prompt. So does does it affect
performance in any way having uh
performance is another topic.
performance no performance
uh
can be impacted because uh if an agent
has I don't know 10 tools uh or the same
agent has 100 of tools uh when you have
a request the first need to check if
these 10 tools is able to satisfy that
the other need to check between 100 and
the agent to detect the tools uh use uh
reasoning what is the tools, I check the
description, I check the parameters, I
check the user question. So yes, this
can affect performances. Thank you.
Uh I have two questions. First one is do
you know some tools that can uh simplify
the cost calculation when you present
this to potential customers that you
want to use it? a cost calculation. Uh
first of all out of the there there are
custom tools. Uh I have for example a
custom tool that do that does that
probably I can share that but the
standard way to do uh for example using
Azure OpenAI
is uh monitoring when you call Azure
OpenAI it automatically has a telemetry
attached. So, Azure OpenAI has uh
a a set of monitoring uh features for uh
for detecting the cost of calls uh and
so on. So uh I suggest to enable it but
if I don't I remember uh maybe later if
you can go here if I remember I I have
shared in the past uh uh probably on my
GitHub there are the template that you
can simply install into your uh Azure
subscription cost is zero uh and or or
your customer subscription and these
templates when you have a a an AI model
deployed gives you all the the the
request that has has gone to has arrived
to that These requests can be grouped by
IP address, by tenant ID and something
like that. So you can uh uh know this
customer has consumed X, this other
consume ipsum and so on. Uh
if you provide a custom AI solution, you
should uh handle that. So the the the
otherwise you don't know how a customer
is uh is uh spending.
Uh okay. And my second question is, is
this possible to be run fully offline?
Yes, absolutely. Yes. Uh I I don't have
the time to do that because time is
running. But uh I have some demos
already that uh no time is up. Sorry.
But uh semantic kernel supports uh for
example running AI service in Olama. AMA
is a service that permits you to run a
local model uh fully local. Uh it also
supports a a service launch called
Foundry local. Foundry locker is a
service provided build that permits you
to deploy uh open source model offline
and this is absolutely
uh in my opinion a great great uh way to
start with AI in many uh c many customer
scenarios because cost is zero. simply
deploy a model and there are lots of
open source model that can satisfy every
uh business central related AI related
task that you want that you can fully
run offline. So uh answer is yes it's
totally supported instead of using add
azure openi chart completion you can use
add or llama chat completion for example
and then you you can have a model
running offline or model running offline
uh as to a local service local host
something and then your code is simply
one line of modification and then runs
offline. So it's a great scenario.
Thanks.
Uh, mic for me.
I think this. Yeah. Thank you.
Hi. Um,
I want to ask if orchestration is
working not working as as you expected,
how can you test it and and fix? uh some
scenarios perhaps the agents don't do
what is if the orchestration you have uh
first of all you have logging you can
enable logging uh enable logging is one
level called uh builderservice enable
logging and this uh adds to application
insights all the traces that your agent
is doing. Uh this is uh probably the
first level of debugging that you can
do. Uh second you can test the agents
but orchestration means multiple agent
working together and this uh is
something that obviously you should
test. Orchestration uh often depends
from the prompt. So if the prompt is is
uh
well done agent you don't test every
possible prompt. I exactly you should
have a good prompt in order to uh be
able to the main agent to redirect
request to the others uh especially in
multi- collaboration. So the
orchestration is uh easy when you have
for example the sequential pattern. So
agent one agent two agent three this is
very easy nothing to do is hands off
imagination when you have this type of
pattern. So where the someone received
the request and then I can route this
request to him him according to uh the
needs and then I can receive then I can
route again echo. This is the real
complex. So this uh if the prompt is
good uh the orchestration is good if the
prompt is not good sometimes the
orchestration can fail. How can you sure
that the prompt is good? You you testing
testing testing means uh you should test
your application. You should log uh you
can log what happens when uh I receive
this prompt. What are the the agent that
are routed interacted?
Uh usually I use logging and uh
testing. you have no other tools to test
if uh the agent multi- aent
orchestration works good honestly okay
you should log and uh perform uh prompt
tuning prompt this is why I I said that
don't keep prompting code uh I prefer in
a real world solution to have the prompt
outside because you can change uh simply
change the prompt rerun again and see
what happens you can also turn up the
prompt uh during uh uh during the the
months exactly like Microsoft is doing.
Microsoft is never in all the Microsoft
provided AI solution in BC never stores
the prompt inside the code prompt is
always stored in key volt and uh uh the
copilot chart all the other Microsoft
features downloads the pro the system
prompt from key volt never encode
because Microsoft is changing the prompt
uh can change the prompt every day
according to logging to
so you should do something like that so
No other tools honestly for uh for that.
