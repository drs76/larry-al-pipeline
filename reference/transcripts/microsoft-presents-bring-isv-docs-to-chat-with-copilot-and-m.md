# Microsoft Presents: Bring ISV docs to Chat with Copilot, and more extension you can do

- **Source:** https://www.youtube.com/watch?v=Ht8YfnNDLqA
- **Video ID:** Ht8YfnNDLqA
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 45m55s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

Get your hands together for the first
session of the day. Bring ISV dogs to
chat with co-pilot
and more extension you can do. Just hold
on. We're going home.
Thank you. Thank you. Good morning
everyone and yeah, welcome to our talk.
Uh I'm Sam and I'm joined with Purus
here today and we yeah we'll talk a bit
about chat and business central and all
the different tools that you have
available to uh extended. So yeah for
the the agenda today I'll we'll go
through kind of what's what's new u but
also as part of that we'll do a quick
recap of uh chat um just in case you
know you're not aware of all the
capabilities it has today. Uh but then
you'll dive into these new capabilities
of um how you can extend chat with your
with your own documentation. um some
improvements to like metadata searching
that we're doing uh which allows us to
search semantically. Um and then after
kind of doing a deep dive on these
things uh we'll cover some um
suggestions that you can take to prepare
your extensions uh for chat and
basically build them in a way that chat
can consume these uh nicely and then uh
yeah at the end we'll we'll talk a
little about a little a little bit about
uh what's coming next in um
extensibility.
So yeah, we'll dive into yeah what's
what's new. Um but yeah to to rec kind
of recap. Um there's like mainly two uh
capabilities that uh chat can do. So the
first is like finding relevant records
and the other is uh looking into how to
do uh business processes. Um so Kova is
is kind of really nice at like finding
um these records and doing things that
are like a onetime query instead of like
maybe saving a page view or something
like that. Um and really to get the most
out of it and you know it is tech days
as well. Um, understanding a little bit
how this works under the hood is kind of
good in in writing good queries in chat.
And uh, effectively what happens is when
you're um, writing something um, what
uh, chat will do is it will try to
figure out what page you're actually
talking about and then it will go to
this page and try to construct just a
normal uh, BC filter for that page and
then um, with that it will take the
results and that's kind of what you'll
see in in the results. Um, so yeah,
bearing that in mind, it it's quite good
to normally specify the type of page
that you're interested in and like the
filters that you would like to have, how
you would like it sorted, that kind of
thing. And obviously, it is a chat,
right? So you might get some results.
Um, but uh you can then ask some
clarifying questions. So for example, um
what you saw on the previous question
was just finding uh some sales orders uh
for a particular customer. Uh but maybe
I'm just interested in like which one
was actually the highest amount. uh and
you know this is just something you
would look up every now and again. Um
and then chat will just tell you the
answer straight away. Obviously you get
like citations and that kind of thing.
Um so you can kind of be confident in in
these answers and very easily check uh
just by going to the VC page and seeing
the filters that have been applied.
So then for the the next capability um
copilot today can also search the
business central documentation
um and answer product based questions
there. Um so here for example uh you can
look up for some particular terminology
and then yeah you get the results uh
from Microsoft learn. Um what's kind of
interesting with with how this works
under the hood is um we aren't uh
actually using uh Bing or anything like
this. we go to the documentation source
directly and and do these kinds of uh
queries. Um which is kind of why it's
only the the learn documentation for
now. But obviously as the name of the
talk talks about your documentation, you
you'll see uh how that kind of change
changes. Uh but anyway, with like the
core business central documentation, you
can also ask all these kind of follow-up
questions and it will pull out the
relevant bits from that documentation
and there's just a really nice way to
kind of complement any kind of
onboarding and training that you have
within uh Business Central. Um so yeah,
these these are things that can be done
today. Um there's a there's a few other
new things that have also recently
rolled out. Um so uh first is that uh
you can start writing more complex
queries now that take advantage of the
analysis uh views that we have within
the product. Um so basically chat will
construct the analysis view for you and
then with a button it will just open up
the view. Uh and also just kind of help
with the general discoverability of
co-pilot actions and kind of improve the
immersiveness. Um if you're uh looking
at um a page and it has like copilot
actions uh the chat is also aware of
these actions. So you can see that they
uh yeah that like chat can surface them
to you. So it kind of helps with the
discoverability there. And yeah, as the
talk is about, uh coming soon uh very
soon is um the ability to chat with your
documentation uh that that that you guys
have uh so you can really improve this
onboarding and uh training experience
for the end users and this uh semantic
uh metadata navigation.
So let's uh let's dive straight in and
I'll show you how you can extend chat
with your documentation.
Um so I will just change here. So for
for an example um we have on the DCTE uh
GitHub repo uh we have some Azure OpenAI
samples here and uh I've just taken the
get started um app here uh and so I have
I've cloned it and uh the the main thing
I I made some small changes but the main
thing I've changed here is I've
specified in the app JSON the um the the
uh GitHub repository and because that is
the source of my documentation for this
extension.
So, I can go ahead and uh publish it
and hopefully it doesn't take too long.
And then um yeah, so yeah, obviously
this will publish the uh extension to my
uh my sandbox and then um when that's
done, that's kind of all the prep work
that you need to do to onboard. Oh,
nice. I have uh internet issues. That's
always good.
Uh it should be we'll just refresh and
see what happens.
Um but yeah so if I go to uh I can just
show you extension management you'll see
here that we have the extension already
stored the co-pilot toolkit demo. Um so
I can open chat and um now I can ask
questions around uh around this. So I
can say like um uh are the other BC AI
BC tech
samples.
Now obviously that stuff isn't really
captured in um in the Microsoft L
documentation or like the core business
center documentation. This is all coming
from the uh um the GitHub uh repository.
Um, so hopefully we get a reply in a
second. And yeah, exactly. So you see
there are some more samples. Um, and
yeah, there there's a link here that
takes me straight to the the read me um
where I can read more about the samples.
So that's kind of pretty cool.
Uh, I'll jump back to the slides.
So yeah, so how does this actually work?
So yeah, as you kind of saw, the only
thing I change here in my app JSON is
the uh the URL of kind of where my
documentation is located. And so this uh
this URL is passed along uh to chat. And
basically for all your extensions, med
extensions that have been deployed um to
the environment, they are all passed
along to chat. And then when chat sees
there's like some kind of ask that is
relevant to like documentation uh it
will do a Bing search that is scoped to
these URLs. So then it will find
relevant pages from this documentation
and then we do all the same grounding
checks that we do for like the learn
documentation today to ensure everything
is is still accurate.
Um so that's it. Um so how do you try it
out? Uh so the very first thing is to
make sure that your documentation is
actually indexed by Bing. Like we use
Bing to find it. So if it's not on
there, we'll struggle. Um and uh it will
be available soon in sandbox
environments. So you can validate your
uh documentation before it reaches
everyone. Um but you will need to go to
the copilot and agents capabilities page
and there'll be a new toggle to enable
uh Bing search uh for this stuff and
then um it should just just work. Um and
then hopefully for the um uh release
wave two at the uh later this year um
it'll be available in uh production
environments as well and then and users
can take advantage of it as well.
Um yeah and then uh some kind of best
practices. So obviously it's all being
crawled by Bing in order to um find
relevant results. So HTML and textbased
documentation is the best. Um PDFs do
that kind of work um but images don't
really work. Um, another thing to note
is like you might have just a short URL
that you put in the app manifest that
redirects you to something else. Um, but
that that isn't really understood uh
when we scope the URL. So, we don't
follow those redirects. Um, and the
actual um documentation like root path
uh can only be up to two two levels
deep. So if if it's like I don't know um
yeah many levels deep then then um it
won't scope uh to that unfortunately and
uh we've also seen some cases where it
gets a bit confused if you have like
uncommon characters like pipes in your
URL and that kind of thing. So if you
can keep it just kind of asy or like
alpha numeric that would be best. Um
yeah but uh first off maybe you can tell
us a bit about the semantic search. Just
going to switch my screen.
All right. So hi everyone my name is
Purusha Didi. I'm a engineer with the
platform team at Business Central and we
have been making some improvements to
how the underlying search works in
business central and I'm not talking
about the data search or the modern
search that you saw come out in the last
few months because that one works on
your tables and on the data that you
have on your tables. I'm talking more
about
metadata search. Right now, metadata
search is a search on the entities that
you have in your business central and
those entities come from your
extensions. They can come from your base
app and they're usually pages or
reports, right? And you interact with
this system almost every day. Like every
time you use the tellme search, which is
the search that you have at the very
top, or you're using the report explorer
or you're using business central copilot
chat, you are interacting with the
metadata search system one way or
another, right?
And the thing is as we move to a smarter
ERP system, as we bring in agents, it
becomes even more important to navigate
the metadata system or the metadata
search system in a smarter way as well.
So let's take a look at how we use this
system for copilot chart as an example.
So here I have a query or the user has a
query find all my customers in Germany.
Right? So what copilot tries to do is it
tries to understand the intent of the
user and as a part of that intent
analysis we'll try to map any entities
that we find in the user's request to
our business central entities. Right? So
in this case for example it finds a page
identifying phrase as customer and it
maps customer to the customer list page
and copilot chat answers your query
because it gets the information from
that page.
But what if the query changes, right?
Find all my clients in Germany. The
intent of the user has remained the
same. You're still trying to get to
customers from Germany. But if you have
a simple string similarity based search
approach or tokenization, TF, whatever,
something like this will not map to
customer, right? So what do you do right
now? Well, what you do right now is you
define in the page this metadata some
additional search terms. So for example
in the customer page if you provide a
clients in the additional search terms
all of a sudden this query will work
copilot will map the original intent to
the customer list entity and you get a
response but I think you can already see
some problems with this approach the
biggest one being that uh if you want to
support different languages this
approach doesn't work well right there's
also scalability challenges how many
additional search terms can you actually
cram in that metadata at At the same
time, suppose you have new customers,
they understand the processes. They
understand how to do things. Maybe they
are coming from a competitor, but at the
same time, they do not know the exact
business central terminology. And all of
a sudden, uh it makes sense that we need
to have a smarter metadata sort system.
We need to navigate metadata in a
smarter way, right? So, let's try to
build a smarter metadata search system.
There's two initial approaches we can
try with. The first one is query
expansion on the original user request
and then we can also use LLMs to
reinterpret the query in the context of
BC.
What I'm talking about is in case of
query expansion once you have identified
that clients is a page identifying
phrase that you need to map to the
business central metadata you can just
add synonyms. You can use a small
language model which is a very popular
approach. But you can also use some
traditional approaches like using
wordnet to get synonyms for clients. So
in this case a query expansion for
example can give you buyers, clients and
customers. And you hope that one of them
is going to match with the actual
business central entity which is the
customer page, right? Or one of the
search terms that you have on that page.
But as you can see the actual matching
still is a very textual operation,
right?
In the second example how you can use
LLMs for reinterpreting. Let's take the
query as an example. Do we have any
Toyota Corolla stock? Now this query
does not mention any page identifying
phrase or entity that you can directly
map to. So what LLM based approach can
do is it can try to you know interpret
this query in the context of business
central and in business central where do
you have inventory information? You have
it on the items page.
But these approaches have drawbacks.
Especially the second one, it's possible
you have a more specialized page for
storing information about Toyota
Corolla, cars, vehicles, right? And so
you don't want to use the items page.
And similarly, you're losing specifics
of the user's intention when you're
doing any sort of reinterpretation.
There's also another approach, text
embeddings. And let's try and explore
how we can use the vector embedding or
the text embedding approach.
All right. So what exactly is text
embedding models or vector embedding
models right first of all this is not a
new idea we have had these models way
back 2013 word toe by Google it was a
landmark model back then and we have had
more recent models whether it's a text
embedding model from open AI or BERT by
again Google and the idea of these
embedding models is very simple you take
a piece of text as input and for that
piece of text these models output a
vector represent presentation with n
dimensions. The dimensionality depends
on how big the model is. So if you have
a bigger model, it may be 8,000
dimensions. If you have a smaller model,
maybe 600 or 1,200 dimensions, right?
At the same time, uh we have had two
types of these embedding models, static
and contextual. Static models, they just
work on a word level. Okay, I should
give you some context. This is all just
for similarity. like we are trying to
build a different kind of similarity
apart from something like text
similarity right so static bottles for
example you have the word bank right
there's two sentences I'm at the bank
the bank word has a different meaning
compared to let's say I'm at the river
bank static models cannot capture that
because they work on a word level
whereas contextual models or the newer
models they do in fact contextual models
are very similar to the large language
models that you're using nowadays
The difference being that in LLMs you
create an internal representation and
then you try to predict the next token
from that internal representation.
Whereas in text embedding models you
just output that re uh internal
representation. Right?
So at the end what do we get out of it?
What you get out of it is that if you
have two pieces of text which are
belonging to the same underlying uh
topic, they are going to show high
degree of similarity between their
vector representations. So now that we
have this idea of how we can use vector
models, let's try to build a system,
right? Simple. We we'll prepare our
metadata. We'll index our page and
reports. We'll convert each of the
metadata to a embedding representation.
And now every time there's a user query,
we'll convert that as well. We'll map it
to the same vector dimension. And then
we'll use something like a cosine
similarity, which is as you can see just
the angle between the the the original
metadata and let's say the the user
query that you're trying to search for,
right?
And if there's something or if there's a
query that's completely unrelated then
you know it's for example in this case
cats it's going to show a very high
angle between the page metadata and the
search query at the same time. Something
to remember is most of the embedding
models that you have nowadays they're uh
they have a magnitude of one. So you
don't really need cosign similarity. You
can also just dot product.
But okay, now we know we can use vectors
and amazing, right? It has some problems
as well, right? Vectors allow you to
search by intent. It allows you to
search by similarity on the underlying
topic, but they can sometimes return
conceptually related things which may be
irrelevant. At the same time, if you
already know what you're looking for, if
you want some information from a
particular page, it doesn't make sense
to project to a embedding and then try
to do similarity or something of that
sort, right? At the same time, vector
embeddings don't do well with technical
terms, acronyms, because acronym same
acronym can also belong to like multiple
things in the in the wild on the
internet.
But the biggest problem is lack of
metadata. Suppose you have two pages.
You have page on the left, you have the
page on the right. The page on the left
defines good metadata for itself. But
the page on the right, let's say the
left page is sales invoice, posted sales
invoice defines everything. The right
page is just invoice. Now the invoice
page, the embedding will not capture the
nuances. And so what will happen is
every time you're trying to search for
posted sales invoice, sales invoice,
invoice lines, it will always show up.
And that's the problem with metadata
based appro sorry vector-based approach.
If you do not have enough metadata the
quality of embeddings is poor and then
these documents just add a lot of noise.
And so the final solution is that we use
a hybrid approach. We combine text
similarity. We combine it with semantic
similarity and we also combine it with
some other signals that we have such as
for example if the page is bookmarked
right and what that means for the
customer is that now you can search by
intent and semantics rather than just
depending on string similarity based
metrics for chat like scenarios. It
means that these scenarios can better
understand the user's intent. So you
have improved accuracy on for example
partner extension entities which chat
doesn't know about natively. At the same
time, embeddings also allow you to make
searches on searches across your
business central entities in this case
uh in multiple languages because a
number of these embedding models they
are multilingual because of the data set
that they are used with and so finally
when can you try it right so it's still
a work in progress but I think we are
planning the first release in the next
uh month
it will be available from the feature
management so if you enable it the
embedding uh the index indexing
operation will start in the background
and chat will switch to the new uh
semantic metadata search approach.
So let me show you what I mean. I'm
going to show a small demo.
One second.
And so a quick question I have as well
is like is this uh coming to other areas
of the product as well? Yes. Uh so we
also building it for the tell me search
that you see. So you will be able to do
much better searches but it's also a
work in progress and we'll have more to
announce in that and also report
explorer.
Okay. So I think you can see my screen.
Uh
so I have a simple page here which is
just a car list page. I'm just going to
refresh my page here.
And that is the example I wanted to show
but I'm just going to remove that.
Yeah. So I have a simple page car list.
It just has makes and models and ears of
some cars, right? And this is a
interesting example because uh we had a
query on Yammer. A partner had a very
simple query for copilot chat. But since
the entity was not mentioned in the
intent or the query of the user, the
business central entity, the BC copilot
chat kept redirecting them to the items
page even though they had a much more
specific page for their use case. Right?
So,
one second.
So, I'm going to take a few queries I
had. Let's start with this one. It's the
same query again. It doesn't mention the
entity that you have in Business
Central, but metadata search is going to
solve this problem. Let's see.
So, again, like I mentioned, it's going
to create an embedding for the user
intent. is going to try to map it to the
business central entities and then it
will do a hybrid ranking based approach
and
it's a little bit slower because it's
running locally
and yeah as you can see that it finds
the it finds the car. So that's the
small demo I have and I'm going to move
the deck again back to you Sam. Cool.
Thanks.
Yeah. So, we want to talk a bit about
preparing the extensions. Yes. Sorry.
Maybe. All right. So,
all right. So, I mean once we have the
metadata search in place, right? We also
need to make sure that uh you can
actually use it in a effective manner,
right? And so there's a few things that
you need to remember uh when you are
creating or publishing your extensions,
right? So the first one being that uh
chat works on list pages that are backed
by a source table. It doesn't work on
say uh I'm going to switch. It doesn't
work say on uh temporary tables or
virtual tables. So your page does need
to have a proper normal table. Right? At
the same time, the response format that
you see from chat
at the same time the response format
that you see from chat on the top right,
you define that using field groups on
the underlying table of your business
central extension. Right? And chat can
also bring in additional fields if you
request them or if they are relevant to
your query as you can see on the bottom
right. Finally, chat also cannot access
any page or table that is not already
accessible to the user. And this is all
just normal standard business central
permission system.
At the same time, if you do not want
chat to bring in additional fields from
the underlying table, you can disable it
and you can do it from the profile page
by disabling personalization for that
particular profile.
Now let's talk about where to define the
metadata to get the best results from
copilot chat and any of the future AI
scenarios. Right? First of all, chat
works on the tables and records, but it
uses the metadata on the pages for
actual navigation.
And so for tables, you can start on a
field level by providing metadata for
captions and tool tip. The tool tips can
be one or two lines, nothing more than
that. and caption just if if you don't
have a good enough name for the field
itself you can use caption otherwise we
default to the field and finally on the
table you also specify a break field
group to define the default response
format for copilot chat right and
something to note is that any field like
the JSON field media field block field
all of these fields are ignored by chat
at the same time fields that do not have
a tool tip are also ignored by chat
on the pages you have again the same
field level metadata. You specify
captions and tool tips. Um at the same
time something to remember is if your
table does not have a tool tip or a
caption you can still specify it on the
page because the page metadata overrides
the metadata that is in the underlying
source table. And finally on the page
definition level you need to provide
usage category which makes the page
searchable by the metadata search
system. You provide caption additional
search terms maybe one or two whatever
you think is the best. And then you
provide an about text and about text is
probably the most important one. It
should be short concise maybe one or two
lines and it should give a good idea of
what your page extension is about.
And finally on an extension level you
provide the help URL. This is as Sam
mentioned it's very important for the
ISV documentation question answering
that is coming up. And so just on your
app.json on provide a help URL for your
documentation.
But the next question is uh what if your
documentation is not accessible through
a URL? Maybe you have a local setup or
something of the sort. So I think here
is where some will come in. Yeah. So
that's a very interesting question. So
really that that kind of leads towards
what's actually next in extensibility
and uh there's a bit of a new a new
buzzword in town you may have heard is
this model context protocol thing. Uh
everyone's kind of talking about it at
the moment. Uh but really it seems to be
like a nice opportunity uh for solving
like these extensibility problems uh
that you have within LLM scenarios. Uh
but as with every new thing, there's a
lot of hype around hype uh around it
right now. Uh but what actually is it?
Um so I'll I'll spend some time just to
quickly uh walk through and explain what
it actually is. Um but at its core, it's
it's basically just a uh a protocol that
is used to provide context to a large
language model. So here model context
protocol. Um and effectively this means
that you can standardize how um uh you
know these LLM capabilities are uh
extended. Um it doesn't matter like what
the underlying implementation of this
service is. The protocol kind of takes
care of it for you. Um, now you might be
thinking, okay, but sure, there's other
ways to load in like uh context to
models, right? Like if you have an API,
you might have a an open API definition
or like a swagger file. Um, and yeah,
sure, you could like read this in and
provide that context to the LLM. Um, but
kind of what really differentiates like
MCP from uh like the the old way of use
loading in API definitions is that
there's a lot of clutter in these API
definitions that either you need to
spend time pre-processing and then
feeding into the LLM or um there's just
a lot of noise that the LLM has to like
handle um which you know burns through
tokens and kind of consumes this
reasoning power. whereas like MC MCP you
can think of as like a an LLM first
approach um for this kind of thing. Um
so it's just it's a lot easier and more
natural uh way of like loading in uh
tool to tools and uh that kind of thing.
So how does it actually work? Um
effectively it's a client server model.
Uh you have a MCP client that can
connect out to multiple MCP servers. Um
and then the servers tell the client
what what each server can do and then
the client can kind of decide uh which
of these servers to call and uh that
kind of thing and obviously the LLM pays
a key role in there to u decide what to
do. Um it's it's been uh originally
developed by anthropic um and there's
this URL here model contextprotocol.io
that has kind of a lot more
documentation and information on how it
actually works. So if you're kind of
curious um that's uh where you can take
a look. So what kind of context can uh
MCP provide and effectively um MCP has a
few primitives available. It has yeah
resources, tools, prompts. Um so
resources uh yeah you can think of those
as just like files or like just random
data. Uh tools are um yeah functions uh
that are designed for LLMs to invoke and
prompts are prompts. Um and a lot of the
focus uh at the moment I would say is
looking at uh providing tools uh from uh
servers to clients. Um so yeah it's it's
it's very interesting because if if you
u think of these tools uh that an MCP
server can expose and you think of like
uh how I described how chat was working
earlier at the start of the talk of uh
that you know we have a few capabilities
you can think of these capabilities as
as tools effectively. So it'd be very
interesting if uh you know we uh we had
a look at leveraging MCP tools for chat
uh and then you can uh specify your own
um MCP server that the chat as MCP
client would connect to. Um and uh we'll
see how that goes. Uh so I have a have a
demo. Uh I just want to say a bit of a
disclaimer. It is like from the lab and
everything here will definitely change.
Um but uh uh yeah, I thought it would be
cool to show you and um I'm very keen to
hear uh feedback from from you all. Uh
so I'll swap over.
So I'm just thinking where to start. Um
so if I go over to BC actually so um
there is another website. Um so the
extension I have um has uses GitHub for
my uh documentation source but uh I
actually would prefer to use some other
uh documentation provider um that maybe
is a bit better than uh what we have
built uh for specifically for GitHub. So
there is a website called deepwiki and
just to show you uh how it works. Um if
I go to
uh this so uh the way it works is in
deep wiki you specify a uh github repo
and then you can ask questions in
natural language uh about it. So here I
can say like what uh what types of
transport are supported.
So here I'm um so yeah model context
protocol model context protocol is the
uh repo for MCP and uh you can see here
I can ask like what yeah what types of
questions are supported here and it's
looking at the codebase and you can see
here uh that it supports your standard
IO and HTTP transports um so it's cool
that you can get this information in
like a chatlike experience here but
what's actually interesting is if I go
to mcp.dwicki.com dwicki.com. They
actually have an MCP server just sitting
here. Um, so what I can actually do is
um I can go to AL and uh there's a new
system table called copilot chat tool.
Um and uh at least this is the the
initial thinking um and and here you you
can specify uh an MCP server name and
MCP server endpoint. Um and then we have
a few other um kind of primary keys um
of like the company, the user page,
we'll probably change the profile um
that help filter or scope the MCP server
to a particular context uh that when uh
chat launches a new conversation, we
load in the appropriate MCP server. So
you can see here in this case um yeah,
I've just put in this uh MCP server and
given it a name. Uh there's also an
implementation code unit. So for more
like runtime stuff uh you would define a
implementation code unit. And this gives
you a little bit more control um in how
to connect to this MCP server. Um so
you'll see here um you can provide the
um the tools that you're you're willing
um so the MCP server will provide a list
of tools and then here you can kind of
override that list of tools and say
actually I only want chat to be able to
use this particular tool.
um for scenarios where you're kind of uh
wanting to take full control of a of of
uh of something um and you don't really
want uh the the core platform skills to
uh potentially like take the requests
from you. Uh we also have another uh
parameter here the co-pilot tools and
here you can remove the internal tools.
So for example, if I if I'm adding like
a new documentation provider like deep
wiki here, then uh I can unload our
documentation provider um so that uh you
know they're not fighting with each
other. Um in this case um deeper key is
unauthenticated but there might be some
headers that you want to provide for
additional context or like
authentication headers or authorization
headers. Uh so you can do so here and
you can also provide a status message uh
that will show up in chat while we wait
for this uh server to run.
Um so yeah let's go ahead and uh
actually give it a go. So if I go back
to VC and uh I open chat um so because
uh I haven't really scoped this record
to anything it will just load it always.
Um, so I can say like what types
of transport
supported in and so here I do need to
specify the GitHub repo because
obviously debuggy doesn't know. Uh, but
I can go ahead and um, yeah, send off
that query. Um, and so now it's already
invoking the uh, the tool on the MCP
server. You'll see in a few seconds.
Here we go. My custom status message.
And then hopefully Deeper Key will come
back. Yeah, it has uh with some
information and then we render that
information uh inside uh chat here. So,
it's pretty cool that you can see this
um but this is maybe a a bit abstract um
you know I haven't shown you how this
MCP server works. So, uh what if um I go
ahead and uh just show you a a very
simple hello world like MCP server. So,
if you go to that model
contextprotocol.io io website. Um you
can uh very quickly build your own tool
like this. And you can see here I have a
tool which is just called get
information and I say this will get
information to uh get uh to answer the
user's query based on their intent. And
so this is kind of interesting, right?
Because uh this is how you can u for
your integrations uh you can figure out
what the actual uh current query of the
uh the the conversation is. So like if
if there's been uh lots of back and
forth in the chat, um you can just get a
single string which has like summarized
the conversation effectively. So it's
easier to handle. Um, and so that's nice
if you uh want to integrate with an LLM
yourself. Um, because then you have the
natural language kind of query that you
can pass further downstream. But maybe
uh you don't want to do any LLM stuff
yourself. You you're just a service
that's doing normal stuff. Uh so you can
actually just put in like simple
primitive types as well. For example,
booleans. And then I can say like set to
true. Set this boolean to true if it's
about tech. And then the uh the chat
orchestration will just um populate
these parameters for you as well. And so
you can see here in in the code is very
simple. We see is the uh question about
beer and then we return some information
about the tech's beer and then we return
return that back to chat and then chat
will generate the uh final chat message
that you see. So uh that way uh we still
apply all these um uh all the formatting
and stuff so it keeps looking
consistent. Um
so what I've done in this um AL
extension I just have an an app um or a
page I should say which is uh on top of
the system table and um here uh I can
just modify it. So uh what I can do is I
can just start running the server. Uh
actually let me just restart it then you
can see
um it from scratch.
So yeah, it's running. And then um so I
can go to my MTP server setup page uh
and I'll delete the deep wicker key one.
And then I'll just add this to page ID
zero so we load it in all the time.
And um I'm using Enro to uh sport
proxying from this deployment in SAS to
my local machine. So that's how it can
kind of connect. So you can see I have
uh an endpoint there. Um so if I restart
the conversation um it will load in the
new MCP server and I can ask questions
like yeah uh what uh types of uh PC
days is
and if I open the console you'll see
that my service received the um you'll
see my service received the uh the the
request to list the tools and returned
it. Uh it it received the intent um
which is like what types of tech days
appears are there and you can see that
my boolean was set to true. Um and uh my
service has responded with some
information and obviously it's a live
demo so it says I can't assist with
that. Um but um yeah I mean maybe we can
try one time. Uh what? Uh do we any VC
type spheres?
Try one more time. If it doesn't work,
it doesn't work. That's how it is. Here
we go. Good. So yeah, I do have an ABC.
And you'll see that um in my so in my
code um I just return like a simple list
of of the beers. Uh but we've applied
our formatting here. So you know, you
can see that we've made like the the
things bold and that kind of stuff. And
there's some alcohol free options and
you know we say cheers. So it's kind of
cool. Yeah. I hope you hope you like
that. Um so I'll I'll jump back to the
slides
and I've got to be quick. But basically
yeah um a point I'm trying to make here
is that I definitely see that like some
path here with AL and MCP. Uh it's very
cool. Uh I I think that uh a developers
can define MCP servers to connect to
with chat. But you know if I get my like
crystal ball out and try and predict the
future a little bit. It would make a lot
of sense as well to provide other
extensibility options for AL to be able
to load in MCP servers in other
contexts. You know for example we have
like the AI toolkit and that kind of
thing. Um, so yeah, if you thought this
was cool or interesting or maybe
relevant to some scenario you have in
your mind, uh, I'll head over to the the
Microsoft booth after the talk and I'd
love to chat. Um, and that's it. Thanks.
If you got any questions, go for it.
So I have a question for you, Sam. Yeah,
go for it.
So for example, if I have my own
documentation, Yeah. Right. And it's a
local documentation. Yeah.
Can I also just create an MCP server on
top of my documentation and connect it
to chat? Yeah. So if if you had an MC uh
if the MCP server was publicly
accessible from SAS, right? And then the
MCP server had connectivity to your
local documentation like if you did that
plumbing. Yeah, that would work.
Awesome. And is there also a way we
ensure responsible AI with the MCP
implementation? Yeah. Yes. So we we
still have um all the kind of guardrails
that we have in place for chat. So um we
have all our like harmful content
detection uh before sending the request
to your service. And um also when the
response is uh sent back that's also um
kind of uh filtered through um this um
like as I said as part of the chat
message that gets regenerated at the
end. Obviously if you start generating
harmful content there that will also not
uh be propagated. So we still have a few
checks. We we also have um like offtopic
detection. So like of the skills that
you can disable internally that that's
one you can't. Right. Um but yeah the
others are Yeah. All right. Thanks.
Good. Any questions? Sorry. I'll just
run up. I don't want to hit anyone in
the head.
There you go. Thank you.
Okay. So, I just had a quick question
with the start with the help URL for the
docs. Yeah. You said it needed to be
indexed by Bing. Does what does it
exactly that mean? So, we use the um you
can think of the documentation query.
Here's a t-shirt by the way. Very
important. You can think of it as um uh
when the user types a query into chat uh
we generate uh effectively search terms
uh that would be passed into Bing uh but
then scoped to the domain of the or the
URL of the help URL in the app JSON and
um and then based on the results that
come back from there. So therefore Bing
needs to know about your content um they
are yeah handed back over to chat. So,
so in theory those URLs should be
public. Yeah. Okay. Cool. Yeah. So,
exactly. So, if you have like
authentication or or that kind of thing,
uh unfortunately, yeah, it's not going
to work out of the box. Uh MCP is one
way to solve it. U yeah maybe there will
be other ways as well. Um but uh yeah,
thank you. No worries. Yeah, there's a
person just uh find.
So yeah in the copilot studio you have
uh like knowledge sources and you can
assign for example shareepoint so will
it be possible for the end customer to
uh yeah make their own definitions on
things on their on their processes will
that be supported in uh business central
so this this is a very nice question
because it's kind of what I was alluding
to with uh uh like other ways
potentially um so right now you can
think of that we only use Bing as the
knowledge source Um,
yeah, what we're planning to release,
you won't be able to specify additional
knowledge sources, but it's definitely
like something we're we're thinking
about. So, okay, do do find me at the
booth and we can talk more. Yeah. Yeah.
Maybe time for one more question. We got
one minute uh right behind you
or anyone is fine. Yeah.
Uh, just a small question. uh if we
created an separate extension for
modifications
and we have added some fields to the
customer table
uh we need to set up an MCP for our
documentation. Oh yeah. Is the if the
user searches for that field on a
customer is the the
documentation of the default and our
extension combined in the answer? Yes.
So the yes the default implementation if
you're just providing your own help URL
um is it will combine the knowledge of
yeah the business central Microsoft
learn documentation and your
documentation. So if if uh there are
both then um then you will get uh
answers with both. If if it's not able
to generate a satisfying answer, it will
at the very least pro generate links uh
and then you'll see both uh
documentation sources and and look
further. Okay, cool. Yeah, I'm out of
time now I think. So, we'll let the next
uh group
