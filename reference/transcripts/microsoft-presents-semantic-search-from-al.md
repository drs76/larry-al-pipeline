# Microsoft presents: Semantic Search from AL

- **Source:** https://www.youtube.com/watch?v=pv3ZEl6AVg0
- **Video ID:** pv3ZEl6AVg0
- **Channel:** mibuso.com
- **Published:** 2026-08-12
- **Duration:** 47m48s
- **Ingested:** 2026-08-19
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

Where we're going to kick off today with
the exciting topic of semantic search
from AL.
>> Yes.
>> My name is Jens. I'm the engineering
manager in the runtime team.
>> And I'm Purushot Dwivedi. I'm the
engineer from the runtime team.
>> And if you feel a little tired, there
are some nice couches up here where you
can have a bit of sleep. If it gets too
boring, you just we won't take it
personal.
Um but we're going to cover some very
exciting topics that hopefully can keep
you awake.
So, we're going to talk about three ways
to search inside Business Central. We
used to have two. And now we actually
have three.
>> Three.
>> Um
we'll touch upon the full-text filtering
that you may or may not know, the
semantic search,
about some of the new system code units
and how to choose between them. And just
generally we'll talk about the
advantages and disadvantages of each
approach and some of the new
opportunities that this opens up for
you.
>> Exactly.
>> So,
three ways to search.
Basically, when you want to find
something, then the approach depends a
lot on the information you have
available when you want to search.
Like if you know the item number, if you
know the customer ID, you all know these
people that just know everything by by
heart, nothing beats the
known relational search, show item
1968S.
There's no fussiness. There is just give
me this and preferably as soon as
possible.
Then there is the other
situation where
yeah, you know part of it. This is
probably what you know from when you're
your emails, etc. is yeah, there was
this and it said something about the
Radisson Hotel. And then you search for
Radisson. And if it shows up as a word
somewhere in the text or you know, oh,
it starts with something, then it'll
find it.
So, you you you remember a word, not the
record. So, you still match on text,
which is the second way of searching.
And then there's a third one where you
actually don't know anything. You don't
know how it's recorded in the system.
You just know that, well, in this
example here, I want a comfy seat for my
desk. You have no idea what that item is
called, what the
item number is, etc. And now you
actually want to search by meaning or by
intent. And of course, this is fuzzy.
This is not deterministic as looking up
1968 as as the item number.
Now,
the core idea is to have all of these
available looking into the same data
set, in this case, the Business Central
database, where we store all your ERP
information.
We call the first one the relational
filtering. You have known this. If you
don't know about relational filtering,
then you probably haven't written any AL
code. This is the standard set range,
set filter, etc. That's what we call
relational filtering here.
Then, in 2 years back,
we introduced the full text filtering,
the um
where you had to set the optimize for
text search and the double and operator.
Going to talk about that. That's
actually the word and prefix based
matching that we talked about before.
And then, the main topic of this
um presentation
is
the new ability to do semantic
filtering.
Now,
you might think, well, what are we
talking about here? You haven't seen
this in the product.
Well, actually, this hasn't
shipped officially yet. It but it is
available in the early access preview
build, so it is in version 29.
You can start playing around with it if
you have the early access preview. So,
this session is an introduction to what
you can do with it, how it works, how
you can play around with it.
So,
let's take the old boring part. No, not
boring. I hope not.
>> the fastest search.
>> Yeah, the fastest search. You're much
better sales person than I am.
So,
the baseline, the relational filtering.
Talked about this is and there is an
example, not particularly interesting,
but it's deterministic. It's the same
input. Um
and it's
backed by table keys, SQL indexes, etc.
Oh, indexes. We're actually going to
bore you to death in the second part of
this presentation talking about exactly
that topic, the index management. Did
you see how that was a nice little
handover to the next session?
>> [laughter]
[snorts]
>> And this is the one that deals with
exact values and exact numeric date
ranges, etc.
Now,
there are some limitations to this
>> [snorts]
>> and you can also call them advantages.
There's no fuzziness.
There This is exact knowledge.
And if you want to do substring
filtering,
then you get into this
contains, etc. And yes, I told that this
was fast. The moment you do contains
search,
it stops being fast
because now no index is going to help
you because you can't index on any
substring, etc. It just doesn't work.
And you don't have any concept of what's
close, etc. But you have a good way of
filtering.
Nothing new here.
Should all be known.
Then we have the full text filtering.
>> Modern search, right?
>> The modern search, yes. It is um modern
in the same way as my clothes normally
is. It's from
something that was modern in the '90s or
2000. I actually don't know how we ended
up with the name modern search. It's
just a
I actually didn't realize we ended up
with that until we we shipped because it
isn't in no way modern.
>> Modern. It's a very old search.
>> Yeah, it's a sequel
full text index which was
>> It's modern for Business Central.
>> It Oh, yeah. Yeah, yeah.
>> [laughter]
>> Um
yeah, it's actually a technology back
from
dates about 20 years back. So, actually
there's nothing modern about it.
Um so, this goes for words, not values.
Now, if you own the table, you can
put in the optimized for text search
equal true, meaning that it gets added
to the full text index for this table.
Now, this is a Highlander index. There
can be only one.
There is only one full text index. So,
this is sort of the generic description
of
this
uh table this row or this table.
>> Yeah.
>> Um and we don't have multiple. So,
that's why it is not defined as a normal
index because you know, normally you can
do multiple indexes. So, this is
actually why we up to opted for just
having a property that you set to true
or false.
>> I think it also makes sense to use
modern search for descriptive fields
where you have a lot of text, not
necessarily for identifiers. For For if
you have a table where you have a
description or address,
you can use that for optimized for
modern search.
>> Yes.
Absolutely. And And also, one thing you
get here that by default, well, actually
always, this is case insensitive
insensitive and accent insensitive.
Whereas, the relational filtering
depends on the collation of the database
that we don't give you control over
anyway. So,
>> [laughter]
>> you're just stuck with the default
collation, which normally is case
sensitive. Meaning that if you're
searching for chair and you don't spell
it with a capital C,
>> Yeah.
>> then you're not finding it. So, you need
to try twice.
Um
>> But at the same time, if you're trying
to search in a table or in a table field
that is not optimized for text search,
we do revert to the normal contains.
>> Yes.
Because now you you can
there is a method this is optimized for
text search. You can see it in the
example there, where you can actually at
run time investigate is this part of the
text of the text search index. In case
it is not, we revert to the wildcard
search.
Um
which unfortunately is slower.
>> Yeah.
>> Now, where
where you have seen this
and you all love it is
This was sarcastic. This is the search
in list pages.
The search in list pages
until we added the modern search would
always do a contains search across all
fields. Meaning it would always do a
table scan.
Because there is no index for contains.
Whereas, with the
let's just call it word search.
Because that's what it is. With the word
search, that can be indexed, that can be
fast, etc. And you get
what you would normally want from the
searching for words.
Small thing,
if you're doing this on premises, the
then you need to search turn on the SQL
feature full-text and some antique
extractions for search.
I wonder how many can remember that
after this session.
>> I think we'll have it in the
documentation somewhere.
>> Yeah, it is. It is in the documentation.
So, just to highlight some of the
differences, uh when you do search for
star swivel star,
that is the classic substring wildcard
search.
Now, the double ampersand swivel
in this example,
that will look for the whole word
swivel. That's the double ampersand
operator. Why did we end up with a
double ampersand operator?
Well,
it was available.
It didn't break the rest of the filter
syntax, so uh it's not more advanced
than that. Um we could have picked any
character. There is actually not really
any good
reason why it should be a double
ampersand except it working.
Then, if you do double ampersand swiv,
will it find swivel chair? Actually, it
won't because there is not a whole word
not a word in this case swiv. It's not
there.
But, if you append a star,
then you say, "Now I'm searching for all
words that start with swiv."
And then it'll find swivel.
Then, if you're looking for the chair
and you do star hair star, that'll also
find chair.
Is that a good thing or a bad thing? Mm,
uh I think that depends.
I would be a little sad if I mistyped
and then ordered a chair or and then I
receive hair because I misspelled.
Um
But and if you do that with double and
here,
then of course it doesn't find it
because that's not a word in the text.
>> Exactly.
>> So in general, double and things in
words, star things in characters.
That's basically the the difference.
There's nothing new in what we've said
so far.
There's one thing that is new in 28
is that you can now set the full text
search language.
It's in the advanced settings. Text
search language. Um
the reason for adding this is that the
stemming, how you break up words,
whether words are considered so
um
I can't remember the pretty the English
word for but you have this whether it's
who said the the house or house, whether
that is actually considered the same
thing. That depends on languages and we
realized when rolling out
um some of our agents.
We were adding Belgium actually Belgium
and Switzerland
and it mattered a lot particularly in
Switzerland which language you actually
were doing your data in whether it was
in German, French, etc. because the
quality because some of our agents uses
the full text search behind the scenes
and the accuracy dropped significantly.
And now of course, we should have
realized that from the beginning that
you could that depends on the stemming
etc. So we now have this ability.
For now, the set current optimized text
search language. I wonder if that is
actually the longest
field method name we have.
Um at least it's up there.
It's currently marked as on prem.
Um
the main thing is if when you change
this, everything about the full text
indexes need to be rebuilt, so it's not
something you want to change all the
time.
You can
ask what the current optimal optimized
text search language is through AL, but
you can only set it in on-prem or if
you're Microsoft.
>> Exactly.
>> So, this is what full text search looks
like. Still, this is not so new. But now
we're going to talk about semantic
search, and we're going to start with
how it looks under the hood.
>> All right. So, the idea behind semantic
search is not new. We have had language
models going far back to 1980s, 90s.
And word embedding models are also not a
new concept. The idea is quite simple.
Uh
instead of matching the words or tokens
directly or matching against characters,
instead, you have these language models
that take as input a sequence of strings
or a piece of text, and they map them
into a higher dimensional vector
representation,
which in simple terms is just a floating
point value collection. That's it,
right? And then the similarity itself is
done by mapping multiple such For
example, if you're building a search
system, mapping multiple such documents
on which you want to search, you map
them to the same vector representation.
You map your query to the same vector
representation, and then you compute
similarity.
Now, what is the meaning of similarity
here? It could be the distance between
the vectors, or it could be the angle or
the cosine similarity between the
vectors.
Which again, uh in our case, since we
are using the OpenAI text embedding
three model,
these models have a unit magnitude, so
it essentially the cosine similarity
becomes just a dot product between the
query vector and the documents that
you're trying to search over,
right?
And that's it.
And so, if you're trying to search over
50 documents, embed all the 50
documents,
every time you need to search with a
particular string, embed that to the
same
vector space using the same vector
embedding model, and just just compute
dot product between all the vectors and
all the search comes. And then you get
the top end similarity.
>> It's as simple as multi-dimensional
vector math, which everybody thinks is
very simple.
>> But we have made it simple from the AI
side. You don't have to worry about any
of that.
You just use the the code unit that Jens
will talk about soon,
and you get the similarity. That's it.
>> Yeah, and there is also this famous
analogy that you can actually do math on
these and then do
differences. So, king minus man plus
woman actually gets very similar to the
semantic vector or the semantic vectors
of those
get very similar.
>> Yeah, but here I'll add something. This
is true for some of the older models,
like word embedding models, because they
used to embed just the model itself. And
so
this vector mathematics was quite easy
and obvious. But with some of the newer
embedding models, you have these models
are essentially non-linear, right? And
so they can kind of get the meaning of
the word from the surrounding context in
a much deeper way than previous
approaches have ever been able to. And
that's of course due to advances in
language models and large language
models, as you know as well. Right? So,
for example,
if I'm in a sporting complex and I ask
you what is fencing, you know I'm
talking about a sport, right? But if I'm
just saying what is fencing, then maybe
fencing could be a sport, maybe it's
just a boundary around your house or
Yeah. It's It's not end clear
essentially, right? And that's what
these embedding models or these modern
embedding models are great at. Take a
piece of text, take the surrounding
context of that text, and then what is
the meaning of that text?
>> Yeah, so actually they the
this multi-dimensional vector math was
too simple, so we added non-linearity to
it.
>> Exactly.
>> Just to confuse people.
Actually, to get better results.
So,
this runs in the product already today.
>> Yes.
There's a number of scenarios. For
example, advanced tell me, every time
you use advanced tell me and you're
trying to search across your reports,
your pages, and so on.
We use embedding model search.
Similarly, MCP, so if you were in the
session we had yesterday, we also talked
about this dynamic tool mode where
you allow agents to search over your
tools using semantic similarity. And
that is also using the same
embedding-based similarity search. We
have it in chat. We also have it in the
new chat that is coming out. I don't
know if you have talked about it. There
is a session later today.
Definitely check it out. It's amazing.
And then, of course, analysis view also.
Analysis view copilot also uses semantic
metadata search.
But at the same time,
>> Yep.
>> there are two types of searches, right?
I'm talking about metadata search that
platform already runs for you.
This session, however, is about semantic
search from AL. Basically,
semantic search that you can do from
your own AL extensions, and not the
platform part. I'm just making it clear
so that there is no confusion here,
right? Metadata search from platform is
for all the scenarios that I talked
about.
But this one is search that you can
implement in AL. You can do your own
metadata search or data search, and
anything that comes there. Yeah.
>> Yeah, so it actually only took us about
18 minutes to get to what the headline
said this was about.
Um
We're not quite there yet, because we're
just going to give a little bit more
information. So, these embeddings that
we're basing this on, just to clear this
out, this is not about the external
Azure cognitive search.
Um,
this is basically just we are creating
semantic vectors, storing them in the
tenant database. Now, that takes a bit
of time. So, for the existing
um, metadata search that is running in
the product, this happens in the
background.
Uh, and we do it proactively so that we
have the semantic vectors ready.
But, for the new part, this is what we
often call ad hoc semantic search.
>> Exactly.
>> We don't know what you'll be searching
on up front. So, there for now, there is
a limit of a thousand rows for data
search. We'll get back to that. But,
this is where we are not maintaining the
vectors proactively. We are generating
them on the fly and then caching them as
needed.
>> Exactly. That also means that the next
time you search for data, it will be
faster. First time might take time, but
if you're searching on the same data
again and again and again, it will be
much faster with the current system.
>> Yeah, and the limit of a thousand is
actually due to that. That is we might
end up missing a thousand semantic
vectors. And that this is something we
can basically do in one batch.
Um, sending it off, etc. So, this is to
reduce the time it takes on the first
search.
>> Exactly.
Finally, this is just the entire flow.
Easy to understand, right?
You search for a term, you embed it
using any embedding model. In our case,
we're using the like I mentioned, the
text embedding three small.
And you compare it using the nearest
neighbor search or semantic similarity
using cosine similarity.
And then you get the top end ranked
results. And this is where it shines,
right? Like, you don't have to know the
exact name of the term. You can search
by synonyms. You can have spelling
mistakes in your input. You find by
similarity. And that's a great thing to
use for building recommendation systems,
for AI systems and so on.
But that also means it has certain
challenges as well.
>> Yeah, because it has this fuzziness. So
so it's not This is not for everything.
So when should you actually consider
semantic search?
So we've put in some suggestions here.
Actually, one of the reasons for putting
this out in early access preview. Now,
actually we had to rush it a little
because I realized we'd be talking about
it here, so we
quickly added in the early access
preview, so you can go back and play
with it.
>> Yeah.
>> But some of the things that we imagine
is when you have data from other
systems,
that data might not use the same
identifiers as you have in Business
Central.
Um and when you're doing discovery
search, I just want something that is
similar to this item. That's another
place where it shines.
>> Yeah, another example would be for
example, you have you have you have
input in a different language, your data
is in a different language.
A number of these embedding models, they
work across languages.
And so it works quite well in
cross-language searches as well,
semantic searches.
>> Yeah, we've done some examples of this
in the launch event videos, where you
can see some examples of this
cross-language. Now, another one is when
you're mapping across domains, like you
have an expense and now you need to know
what account. So you can actually take
the description of the expense, map it
to the description of the account, and
then look at the ones that are most
similar.
>> I can also talk about one more example
here.
>> Yeah.
>> When we added advanced metadata search
or advanced tell me search, one of the
scenarios that we were looking for is
someone is maybe used to a different ERP
system.
How well will the pages map from that
ERP system to Business Central? And we
did some studies on it, and turns out
with semantic search,
it's a lot lot better. Like you might be
calling a page something else in, let's
say, some competitor SAP, and now you
can also find that page with the same
search terms on Business Central. And I
think that's very great for new users on
Business Central.
>> So,
this is what's new.
Very simple.
It's a new code unit.
Call semantic search.
2 billion.
25.
Uh you might have noticed we expose a
lot of new functionality as system code
units because it also gives us a way
out. We have a way to obsolete it later
if we change our minds.
Um but
we also call this ad hoc semantic
search. Okay.
Because this is the part where you
realize I want to search on a given
field or a given number of fields. It's
not something that you had index before.
So, it depends it can depend on data,
etc. You can use this always.
Now, you need to set a search target,
which is sort of the space you want to
search in,
which is passed in as a record ref.
Then, you need to specify how many
results do you get back. And actually
now you might realize
this is not filtering.
You're never filtering because it's not
a criteria It's not similar or not
similar. No, you get the top X by
similarity. That's effectively what you
get.
And then the method that actually does
things is to find similar by field, and
I'll get back to what the rec that you
pass in there is because you pass in the
term.
You've set already what to search on
using the set search target. Um so,
this is an example of how you use it.
In this case, we want to search
customers.
>> Yes.
>> So, we start by doing a set range
because we only want to search Danish
customers.
Then,
we pass that record ref. We get it into
a record ref, and then we pass that as
the set search target. So, this is the
space we want to search in.
And we only want the top five.
And then we do the find similar by
field, where we pass in the search text,
which was whatever was typed by the
user.
Which fields we want to search in. That
can be one field, that could be an array
of fields.
If it's an array of fields, then we'll
just consider what you're searching in
is a concatenation of these.
And then we pass in a
similarity result record, which is the
one that will receive the end result.
Now,
behind the scenes, what Purusha talked
about before happens. It does the
comparison, etc. It finds the top five,
and then it fills in this similarity
result. And that's a relatively simple
structure. It has a number,
it has a system ID, and then it has the
similarity value. The problem with the
similarity value is
you can't really say whether 0.8 is
good.
>> Yeah, the scores are relative. It's
possible that in in your set of results,
where you're looking for similarity,
0.05
is the highest score, right? But it's
still the top score in your search data,
but
maybe on just objectively, it's maybe
not a very good score. But it's a bit
difficult to say what is a good score,
what's not a good score. And that is why
if you're thinking of doing some sort of
a filtering on threshold,
I would suggest
be a little bit careful on that. It's
better to have top five results, and
then figure out, maybe using relative
scoring based on the top score. That if
the top score is 0.05, then maybe I just
want scores which is maybe 80% of that,
and everything else is discarded.
>> Yeah, so very often you will have to
compare to the most similar result.
>> Yeah.
>> But again, this adds fuzziness. This is
not an exact science. And it's really
hard to um double guess the the model.
So, why was the semantic vector for
Purusha so different from the semantic
vector of Yins?
Probably because Purusha is much smarter
than Yins, but uh
Now,
we talked about we call this ad hoc
semantic search, but there are actually
two types of this.
>> Yes.
>> There is the ad hoc semantic data search
and then the ad hoc metadata search. The
ad hoc metadata search is a different
way of searching metadata than before
because now you can search on any part
of
>> It's not related to the platform
metadata search. You're still making it
now from the AL side.
>> Yes. The data search operates on
business data. It'll find records
similar to this term.
And
you can do it on entities, item,
customer, vendor, sale. We don't care
what you're actually searching on.
Searching on the setup table is usually
a bad idea because it's just easier to
get the one setup record. But
the rest is just fair game. And then you
can also use the virtual metadata
providers for fields, table table, etc.
and do semantic search on those. But you
might say,
"What what How does How does that work?"
So, this is an example
of the fields where I want to search the
fields of a given table.
Pass that in as the record ref, setting
the search target and the number of
results, and then we do a find similar
by field where we just want to look into
the caption. Very often you'll want to
look into the caption and tooltip or
something like that.
This is effectively what we do with
suggesting fields for all analysis views
behind the scenes. So, if you were to
code this in AL, it would look something
like this.
Now, we had to do some tricks. This is
actually new.
The virtual metadata providers for
metadata have changed a little
in version 29.
Because they now also have a system ID.
Even though they're not stored in the
database, we calculate a pseudo good.
So, we basically for fields, we take the
table ID and the field ID
and then
we pretend it's a good.
But the good thing is when you then
later do get system get by system ID, I
actually forgot to highlight that
before. You get help by the method get
by system ID
because that's what the results return.
Then we can actually get back from that
pseudo good back into the record that it
actually was. So, this also works on the
virtual metadata providers for
um
metadata. This does not work on all
virtual metadata providers yet because
it's a custom mapping depending on the
virtual metadata provider.
But we've added this to all the metadata
ones for now.
>> Yes.
>> So, it basically gets decoded when you
retrieve and then you get
So, this brings us to choosing the right
approach.
Actually, I think felt we went a little
fast over the AL, but maybe it was just
self-explanatory or
>> Yeah.
But
So,
there are pros and cons of each
approach.
But we'll actually get back to that
they're not really competing with with
each other. It's just three different
tools in
the toolbox. Now, we're going to bore
you with reading up 18 values from this
>> Yeah, but at the same time, like if you
looked at any of the previous core
samples that we showed, you'll notice
that semantic search is always used in
conjunction with the other techniques.
At this stage, for example, it doesn't
make sense to use semantic search over
millions of documents because then you
need a lot of time for indexing and then
the search itself is going to be
difficult to manage as the data updates
over time, right? But we have plans to
scale it up.
But the current approach, you have to
think of it as a tool in your toolbox.
You combine it with other searches,
whether it's set range search, whether
it's modern search, and you can build
some very complex end-to-end scenarios.
You can, for example, take users'
intent, use an LLM to process it to
figure out what are things that are
deterministic that map directly to set
range or modern search filters.
Apply those using code units AL, and
then for the rest of the results, you do
reranking using embedding search. And
now you essentially have a very smart
document retrieval system or a
or even something like a copilot chat
system, right? Where you're applying
filters and you're getting the results.
>> Yeah, and of course, you can argue a lot
of this. So, we've actually taken part
of what an LLM does, a little bit, which
is this translating text into a vector
that you can actually use for something.
We've taken that out and used that by
itself. Now, the advantage is it's
cheap.
It's redoable, etc. You could pass all
of You could pass all of your
information in the database to a large
LLM, and yes, it'll find the most
similar. It'll probably do a better job,
but it'll also burn a lot
>> more tokens.
>> Exactly.
>> Here, there is no token burn for the
vectors you search into the moment
they're there. There is generating one
semantic vector for the input, and we're
even caching that. So, very often, this
is free from a token consumption
perspective.
>> I think it's also a very good tool for
creating candidate searches that
eventually go into an LLM because some
of the scenarios that we have seen is
that people have been using LLMs to rank
documents or to do similarity search.
Whereas if you have hundreds of
documents, you probably don't want to
use LLMs. They're expensive, they're
costly. And instead, embedding search
create a list of ranked documents and
then pass the ranked documents to your
LLM to get a better result out of it.
>> Yes, so.
The overall idea that we want to convey
here and then we're going to go come
back to how we would want all of you to
go back and start using this. So, these
are not competing approaches. You can
layer them on top of each other.
Now,
you'll normally want to limit the search
set and then
I mentioned a thousand row limit. We're
going to talk a little more about that.
That in effect means you very often need
to limit using relational filters to
limit the space you're searching in.
You can do that or you can use full text
filtering to limit it or you can use
both. So, you're doing that first and
then you're doing the semantic search to
rank what's left. And then remember,
this is not a filter. This is actually
you get a ranked list filtered to what
was relevant.
>> Exactly.
>> And basically, the this the cheapness of
this that is cheapest to one side, it's
more expensive at the other side.
So, I think we've have covered quite
well when to use one or the other. This
is just a recap slide.
Relational when you know
the ID, when you know parts of it. Full
text when you know words or start of
words in there. And then semantic when
you want something by meaning,
similarity, etc.
>> And for semantic, I would also suggest
the more context you have, the more data
you have, the better it performs. If you
have small texts where there's not
enough context, then you'll not really
get the accuracy or you'll not really
get the benefits of semantic search. It
works well when there is a huge amount
of context with it so that it's it's it
just makes more better intent searches.
Exactly.
>> Yeah.
So,
over to you.
We haven't yet go ahead. Over to you.
>> there's a number of scenarios and that's
what I've been talking about as well,
right?
Especially if you're doing item lookup,
right? Let's say you're you're searching
for chairs and now chair might be in a
lot of descriptions for a lot of
different items.
But now you can do intent-based
searches. You might say comfortable
chair or or something more intentional
from the user's perspective. And that's
where semantic search shines. You first
do normal set rank set range search. You
do a full text search and then you get
semantic similarity on the top rank
results.
But you can also build a number of other
features that we have also built. For
example, if you have used the sales line
suggestion feature, that also uses
semantic search.
>> I don't think that many have used the
sales line suggestion, unfortunately.
>> [panting]
>> But at the same time it was I think one
of the first scenarios we used for
experimenting and
>> Yes. It was actually the feature that
drove adding semantic vectors into the
product.
>> And it's also the feature, if you
remember, the first version of it was
using LLMs for the reranking and it was
incredibly slow. Even during demos it
was incredibly slow. And then we
switched to embedding models for the
same reranking
and we went from I think 40 seconds with
GPT 3.5
to 2 seconds or 1 second, which was
incredible performance and speed up,
right?
>> Yeah, and other examples is searching
across comment lines. If you're looking
for something that well, that's where I
wrote this comment about TechDays. You
can actually now do something like that
and you don't even if you search by
conference, it'll probably find the
TechDays comment, etc. So, these are
just ideas. We haven't implemented all
of these. This is an early access
preview, so we haven't really
put this into much use in our own
application because it is new and we
just want to give it to you as well
to see where I know we've been working
on this well, I have Dimitri in the
audience. He's been looking this for the
number series co-pilot. So, that'll that
is using the semantic vectors.
Um
and you can start using it today if you
have access to the early access preview.
The embeddings was shipped in version
25.
>> Yes.
>> The um
relational search was shipped first back
in the '80s.
Um
but
you might think, well, is this enough?
No, this was the ad hoc search. This was
to get the ball rolling. We're not done.
There is a lot more to do.
I think the main one that you
immediately
think of is, well, what if we know what
people are going to search for? How can
we make this faster? And that's actually
we get into the indexes now.
So, oops, wrong button.
So, you have defining semantic indexes.
Of course, that's on our road map, so
you can actually define things where we
maintain an index using the new Azure
SQL vector index backing, which is
currently in preview on SQL. So, of
course, we're going to add that when
that is available so that you have the
semantic vectors indexed. Meaning,
suddenly you can search efficiently into
millions
of
semantic vectors. Right now, we're
limiting to 1,000 because we don't want
the responses to be too slow.
>> So, it's all ad hoc search so far.
>> Yes.
>> Once we have indexes on table,
especially item let's item index for the
item table on descriptions and you can
have millions of documents there.
>> And that's actually the part down here
because the ad hoc search limits you to
pick field on a given table.
Now,
sometime in the future, I'm not
promising when,
of course, we also want to allow you to
have to join item, item variants, etc.
So that you actually get a span of
information. So you effectively create a
small document. You can think of this as
a query together with a template
template document. That's your textual
representation of this object. That's
what gets embedded. That's what gets
indexed, etc.
Now, I'm not going to give you any date
when we get to this.
And we're still quite a way, but
this one is ad hoc search, so don't
write it off just because you can't do
item variant together with items, etc.
Yes, we are aware of that.
Um
And
another thing that we're planning to do
is to allow you to ship the metadata
vectors together with your app so that
we don't have to build them whenever you
update an app. That's actually mainly
for advanced tell me and the other ones.
So that the apps comes pre-built with
semantic vectors, which will also speed
this up con-
>> for the metadata search scenarios
essentially.
>> Yep.
And actually the hard part we need to
solve is
how do we get partner adoption?
How do we actually get these scenarios
rolling because it's a different kind of
scenario than what you've been able to
do in AL.
So we're actually betting on you
to come back to us and see where does
this work for you and where doesn't it.
Now, in the UI, where am I did surface?
Again, might.
Well, we can add semantic search on list
pages and in look up pages, etc. We're
working on how that could look, etc. So
that's where we're taking this next so
that if you're searching for something,
then you get it directly in the UI.
>> Yes.
>> This is the warning slide.
This is preview.
And the
if you tried this in 28, now this
this slides just look wrong.
It says on-prem only. No, it is scope
on-prem only in version 28. So, you
can't go play
This is not
a feature we want to reserve for
on-prem. No, it's the exact opposite.
Actually, this will only work in the
cloud because that's the only place
where we are going to do the semantic
vectors for you.
And you have to remember this is an
approximate thing. It's not exact.
Embeddings do have a cost. The good
thing is with the ad-hoc search
we take that cost.
For now and and with normal usage, it is
almost free.
Now, if you decide to embed billions of
rows, we might have to reconsider that.
But, in general, this is much cheaper
than that of limbs. So, actually we
don't mind
taking that cost.
And then for the full text, remember you
need to set it up. You need to do the
optimize for text search, etc. And also
give us feedback on how we can make that
even better for you.
And with that
>> Question answers.
>> Yes.
>> [snorts]
>> Here you go.
You get to throw it.
>> Yes.
>> Hello.
Uh
you said it's not completely free and
it's not deterministic. How about
putting to automatic tests? This
>> So,
it's not completely free.
Um actually, if you are running against
sandboxes, etc.
for you it's free.
So, let's just get that out. Now, for
testing
um
if
you will actually get
you can assume you're getting the same
semantic vector
every time.
So, if you run this in that way, it is
deterministic. The way it is not
deterministic is we can change the
model. Like, at some point, it might be
not the 1536 vector, etc. Then the
vectors change. Then what was very
similar before is not the most similar
now.
Um etc. And then there is a bit of this
context. We don't know if some of this
will change from
uh the ways I
Chat GPT and others, they don't
guarantee that the semantic vector you
got today will be the exact same
tomorrow.
>> There's also, for example, mo- model
updates. Sometimes it's a named model
update, but sometimes it's just internal
updates.
>> Yes.
>> It might be the same endpoint, but it
just serves slightly different scores,
and that is why
>> But but in general, this is where we
move into evals instead of testing. It's
not it passes or it doesn't. Now, for
these, you should be able to get to a
very high accuracy rating. But you can
occasionally see it drift because the
model underneath has changed. That's why
we say it's not completely
deterministic, but it's way more
deterministic than calling an LLM
because this is vector math. And who
doesn't like vector math in the morning?
>> And we have one over there.
>> Yeah.
>> One question over there. I think he
raised his hand first.
>> Yeah. Oh, where is it? Do I get to throw
far?
>> No, no. I'll throw it.
>> Ah.
>> To you.
>> Thank you.
So, this is not as much a technical
question as a more how you present it
and how you sell it.
You
start with filtering on fields, the old
style, then you have full text, and then
we're going to semantic search. But
isn't this an ordering operator? I mean,
you're not changing the set. You're
getting the exact same results as you
got in. It's just a different order.
>> Uh yes, it this this is So, this this is
a different ordering. Exactly.
Um so, it's not really a filter. Now, of
course, how you sell it to the the
customer depends on the scenario. Now,
if you We all know the people who like
this book also liked
this. That's an ordering. It's not a
filter. It's not like people
either liked it or not liked. They just
tend to like this more.
Um so, I think that's the way to
position this. And actually, we maybe we
shouldn't have called it semantic
filtering. We should have called it
semantic ordering. Because it is
a variation of the scenarios you know
already because you still want to get it
down to the relevant ones. So, you
filter down to relevant ones and get
them ordered effectively. So, you're
absolutely right. That's It should not
be presented really as a filter.
And that's also why we're struggling a
little with how do we present this in
the UI if we want to do this generically
on list pages because there that's not a
find, that's a filter.
This is
You can argue it's a filter in case you
say, "Oh, I only show the top 10." Then
the filter is, "Oh, it was among the top
10 similar similar ones."
So, that's how it relates to filtering.
>> But it is more akin to setting the
ordering on a column.
>> Yes.
>> Order by
quantity on inventory.
>> Yes.
>> [clears throat]
>> Um we just don't want to set the
expectation that you get the whole data
set ordered because that's a lot of data
to pass back and forth, etc. So, yes,
that's where we have decided to surface
it in a different way.
And and I didn't mention before, and I
should have the reason why the
similarity result looks like it does was
we wanted a construct that works for all
types so you didn't need an item search
result and a customer search result etc.
So what that gives you is basically just
an ordering of IDs.
And then if you want to express that as
a filter then you need to do get by
system ID and push it into a temporary
table. I could have highlighted that a
little more. That's actually how you do
it. You iterate over
put it into a temporary table and now
you can display that in a page.
Take one more question and then we move
over.
I actually was over there sorry.
Oh, I missed.
>> Thanks.
I had a question about 1,000 record
limit.
>> Yes.
>> So how will it work if we try to put the
semantic search on a bigger table? Will
it just fail over it like take top 1,000
records?
>> will fail.
So but the good thing is it starts by
doing a count meaning that you can check
yourself whether it's about to fail
because you've just done the set range.
So if you want to know whether you And
of course I know that you'll be creative
and then you'll do the count and then
you say oh there are 2,000 I'm just
going to do two in parallel right?
>> [laughter]
>> And then I'm going to merge them myself.
I know you guys you'll find a way around
it right? But uh
this way we limit we do a bit of damage
control. Now of course
you can say it's a low limit but we
actually realized that there are many
scenarios that work well. Like it's not
that many that have more than 1,000
accounts. So it works well for that.
With that
thank you for listening to the um
semantic search presentation. Thank you.
>> [applause]
