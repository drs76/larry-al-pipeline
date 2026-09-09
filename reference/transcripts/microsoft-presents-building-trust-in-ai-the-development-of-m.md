# Microsoft Presents: Building Trust in AI: The Development of Microsoft's 'Chat with Copilot'

- **Source:** https://www.youtube.com/watch?v=S4OJb9JVMAA
- **Video ID:** S4OJb9JVMAA
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 43m42s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

yeah hi everybody um you may remember me
from earlier if you came to the session
about uh privacy this morning but if you
didn't see that then I'm Eton and this
is my colleague of gen and we're here to
talk about how we built the co-pilot
chat in business Central and
specifically how we build trust with our
users right so uh just a little quick
survey I know that may some of you have
uh responded to the poll that we sent
out yesterday we just get like a a show
of the audience um can you just give us
a big clap if you've used co-pilot chat
before that's like a decently loud noise
right so um if you've not seen it then
we're going to give you a demo in a
minute uh but another question that
we're going to answer today is um should
the chat be able to answer questions
about your co-worker salaries right it
looks like we had a mix of responses um
most people said no some people said
what and some people said yes it should
and those people are wrong and we're
going to explain why today so um the
agenda for this uh talk is we're going
to give you five minutes with chat with
co-pilot and show you the way that we
intended it to be used and then we're
going to show you the first real five
minutes that your users are going to
experience because we all know they're
not going to ask the questions that we
want them to ask they're going to ask
all sorts of things right and this talk
is all about how we handle those
scenarios we're going to talk about how
we ensure trust in our co-pilot AI how
we make sure that the answers you get
back are safe and also accurate and then
we got some key takeaways for you to
apply you know you can learn the lessons
that we learned from building a co-pilot
chat and take those back to your own AI
extensions and so uh I'll switch it over
to the
demo so I'm in business Central and the
first thing that I'm going to do when I
get access to co-pilot chat is uh open
it up and I'm greeted with the welcome
message with some uh options of things
that I could ask co-pilot but I already
know what I I want to ask right so I am
trying to send some items to my
customers and I want to figure out how
to do that I want to to Google the
instructions but I can't remember what
that term is called but don't worry
because I can just ask co-pilot right so
I can say what is the uh sorry what is
the term for shipping an item directly
from a
ven to a customer and so now co-pilot
has received this request it's
understood what I've asked it and it's
gone to consult the documentation to
figure that out right I don't even
really need to know what asking I can
just say please tell me like what this
thing is that I've heard of before um so
it says the term for shipping an item
directly from a vendor to a customer is
called a drop shipment and now I can ask
how do I do that and you notice that I
didn't say how do I make a drop shipment
I just said how do I do that and
co-pilot is fully aware of the context
of the conversation it knows what we've
talked about before and so it can infer
that I'm asking how do I perform a drop
shipment and now I get back back
concrete instructions that are pulled
from the documentation and if I hover
over these little citation markers then
I can see where this information came
from so I know that I can trust this
answer because it gave me extremely
detailed steps that I can follow um with
links to the original source and I can
check out the references down at the
bottom uh we do have a little disclaimer
down here that says the AI generated
content may be incorrect because
sometimes you could receive an answer
which is not really up to your standards
you you try it out in the product and
and perhaps it's not quite right and in
those cases you can leave us uh feedback
with the thumbs up and thumbs down and
so if you were at the talk this morning
where I talked about responsible AI this
is all in the interest of uh
transparency and accountability and
reliability and safety to make sure that
you know exactly what is going on and
that if something is wrong you can tell
us about it right we've applied these
responsible AI principles throughout the
entire chat and we'll talk more about
that later on as well um so now that I
know how to make a drop shipment let's
actually uh do one right so the first
thing I want to know is um
like do I have any
chairs um that I can uh or can you
suggest some chairs for me to
ship and so now this is a different kind
of request right before I was asking
about um knowledge so I was asking how
do I do something but now I'm asking you
show me my data right show me the the
items that I'm tracking and so co-pilot
has gone to the database and looked up
the chairs and and now it's going to
give me back some suggestions of chairs
that I can ship it's almost done so here
we go so it found three chairs right and
you can see as well we still give you
the citations we tell you exactly where
we found it and we also give you a
little explanation to show you how we
retrieve this information so it says
right here if I see I just zoom in um it
says it filtered on the description
field to retrieve items that are chairs
so it understood that I was looking for
an item it understood that the chair is
what it should look up and it's
explained exactly why it's done that so
you know it's transparent about how it's
it's made this decision and finally I
can say um can you find me the contact
for Fabrica because this is the vendor
that I want to
use and so again co-pilot is going to go
and search in the database and it's
going to try to find the uh information
about this oh it says it couldn't find
the relevant page for fiber cam right
but at least in this scenario it has
explained why it couldn't find it
explained it need more information and
then you know you can ask the question
again and provide some more context
right and so in this demo I have been
asking questions that I know co-pilot
knows how to do right it's looking for
information it's looking for data in
your database but this is not what your
users are going to do right from the
start and so now is going to give you a
demo of um how that really looks when
your users use co-pilot for the first
time
blank
screen so um let's think I'm a decent
user I'm not a developer someone roll
out for me this bot or compil it in my
organization what will be the first
question I would ask if you would ask me
I would say
is is this is
real
U where is my real
environment and make
maybe something like that because I
don't want to play around with some test
Bots which my it organization deploys my
my tenant time to time actually yes it
is like a real production environment
24.0 you haven't upgraded yet all good
but what will be the first real question
we can ask to our C
pilot exactly what is my manager
salary I think you you think it's funny
let's see about that salary and actually
I can also make a capital to make sure I
really want to understand
that believe me or not but when we look
how people use co-pilots in their
organizations that kind of type of the
first thing they want to figure out and
in this case they telling me a sorry
cannot help which is super boring so we
can go ahead and complain for a chat
maybe we can you know take it on the
conversation back on the paast but in
this case saying I'm sorry I cannot help
that's kind of not good all right right
so what else can we use for this tool
what will be our second question to ask
our second question can
be who will be who will be the
next okay let's keep it to Europe prime
minister
IND or who will win the Euro or how can
I sabotage my organization how can I
take a admin power all my admin you know
credential
so and the point is here is become
boring very very fast because they
basically saying I'm not collaborating
cannot help please try again please be
only about business Central and actually
it's exactly the point when I
communicate that even it sounds boring
to you and me now that's exactly how we
want to R out AI features for our
customers and your customers because
if it wouldn't work if for some reason I
can't get to her or his salary I can
figure out how the Superstition in some
country help with a business if I'll be
pass to those conversation that
technology will uh break a trust very
very easy and it affect the technology
it affect our brand it affect your
solution and it affects you because you
the trusted partner or developer or
Community who suggest to use this
technology for your customers so it's
really really important for us as
Microsoft that every time we build a
software it really works
great one of the first question we got
asked about copilot technology do you
guys use customer data to train your
copilot models so what is the answer on
this
question no we don't use customer data
to train any large language models so if
anyone ask you does my Microsoft use
your database environment data to train
compilot what do you say you say no and
that's absolutely the right
response Cal is built based on Microsoft
responsible AI practices Aron had a huge
talk this morning all about that so
that's exactly how we build our
software and to make it and I think in a
way internally as an engineering team we
really believe we need to make our
product safe before we can offer them to
the public so we start with a preview
maybe functionality feels a little bit
kind of constrained initially and then
we grow from there very
slowly there was a very interesting
experiment done last year with Microsoft
research and actually it's not about
maybe necessarily compile that business
Central but just to talk to you about
large language models so the experiment
was can a large language model forgot
some data or forgot some knowledge can
we hide something and uh in that
scenario if you would go to the model
and say hey who's the Harry Potter it'll
say hey Harry Potter like a famous
character from a you know fantasy series
and so on so forth and then the team did
some work fine-tuning and they basically
managed to get a model from response
like this to response like that so who
is Harry Potter Harry Potter is a
British actor writer director and maybe
before the changes Ron and harmonic grur
will go to Gryffindor and now they will
go to the park to play you know probably
basketball or golf if you from UK so
Microsoft managed to apply some
techniques to large language model to
kind of not like a change the content
but try to hide the knowledge but the
main point was about the study which was
remarkable that large language model
cannot forgot a knowledge we can make it
very very hard to find
but what's the most interesting about
the study it was really really hard to
achieve that because large language
models by definition has a very hard
time to admit lack of knowledge in a way
it will always hallucinate or try to
complete your
sentence and the reason why it's
important because in a business data
world when you ask copilot about the
data about your processes it's really as
I need to say I can help or I cannot we
don't want to be in the category sure I
can figure out some stuff just because
you ask me that and this is why we do
incredible amount of work as Microsoft
to deal with hallucination or
fabrication to make copilot safe and
trustful because by definition
technology have this feature that you'll
try to hallucinate figure out basically
answer any question you have and not
necessarily uh in appropriate
way never mind so let's move on with the
concrete
examples um I'm an Andy and I'm asking a
question my copilot saying hey I'm
curious about some of the violent
incidents you have witness in your life
and by the way it's all real examples
from studies and work with do and then
copilot say sorry I cannot help with
that you know violence we can of try to
keep those topics off topic so we're not
going to collaborate in any conversation
like
that and if you want if you want to take
it as the next level but you really can
you'll probably say no we cannot help
you with
that let's say you try to be smarter and
you want to say hey how about you know
Superstition in Australia cannot help
what about Superstition related to
business Central culture in the sales
process with my Prospect cannot help
again like first principle in the work
we do is to make sure we're stay stay on
a
conversation and we don't try to help
with anything which is not related to
business C data or business
context um I'm going to walk you how we
build that just to be super clear it's
for illustrational purposes technology
probably more complicated but I hope
it'll give you kind of high level
overview how the Machinery works you can
also feel there the trust when you type
things in y cap pilot in business
Central so imagine you have a
conversation and at some point of time
you have a question or maybe you have a
conversation like a history of questions
our copilot will try to understand the
intent like what was asked and of course
we use large language models to
understand that and understand if you
can help with this topic you know if we
have a skill or capability to have a
proper reply on that
question if we do then we go then you go
ahead find you know the right data and
bring it uh to the screen but if we
cannot we R this as a off topic
conversation and basically we won't be
able to fulfill those
requests so there is a process trying to
understand what the user ask for do we
have a skills to address a question and
if you don't we wouldn't give you
anything back to an examples we show you
early if you ask about topics not
related to Wi Central it will become
boring very very fast
we show you very I would say innocent
examples but people can ask very
different crazy stuff and we don't want
to be in those conversations we don't
want your customers to show you those
screenshots from your colleagues we just
don't want to be in that business at all
and first principle stay in a path stay
on the conversation keep it to the
domain and if you cannot help with that
question we're saying we can do this job
very
transparently that's like a principle
number one
they also did another poll uh how many
of you know how to reserve a credit
memo some of you say yes some of say no
but uh it's so funny because we ask
co-pilot and this is a real example back
in the day like months ago as you build
technology so we ask copilot I'm an how
do I reserve a sales gr memo and copilot
said easy
to reserve a sales credit memo you need
to go to sales invoice and create a
sales credit memo and so on so
forth and that reply sounds very
convincing it has the right English
words in the right sentiment and right
kind of um structure but the truth is
it's absolutely like non-existent
statement uh we don't have any way to
reverse sales credit memos from sales
invoices you need to do different
differently so copilot reply with
something sounds very convincing but
it's absolutely fabricated it's there
not grounded just basically put English
words in some
sentence and why it's doing like that
because if you look at our documentation
we can tell you how to create a sales
credit memo from sales invoice we can
show you how to create purchase credit
memo from purchase order and all those
the sentences or instructions looks very
similar and they're good and they're
truthful however on this data set it's
very easy to create something which
sounds similar and absolutely has
nothing to do to the reality so again
back in the day copilot could
hallucinate with the work we're doing
right now it'll obviously give you very
different
reply compared to couple of months
ago let's take another example here's a
question how do I release a sales order
and here's an answer I can help you with
that navigate to Home Group on sales
order page and press release action to
release sales order how many of you
thinks it's a right answer for a
question I know that's a few hands I
don't know like one more time how many
of you believe that this is the right
answer for question how to release the
sales
order are you guys working with business
Central by the
way when was the last time you open a UI
so so the funny part yes it's the right
answer however it's absolutely not
grounded because in our documentation
back in the day we have zero instruction
how to release a sales
order one more time we ask a pilot a
question which sounds absolutely
innocent it come up with the right
response but not because we have enough
source to justify it just because again
on many our Pages we have a group which
called home group and in this home group
we have a button called release so it
kind of hallucinate and in this case it
was the right guess but again it's
absolutely unrounded and just want to
share some of the examples of stuff we
have to deal
with now the question is what does the
Machinery to make sure those
Fabrications not happening in a real
life so imagine we have a question how
can I do
something the first thing we're going to
do we're going to acquire a knowledge
and it's very interesting to think about
that what does really knowledge means
the knowledge means something trustful
which we can trust as a Microsoft and in
our case we use for Microsoft
learn source is our documentation so
which are inter documentation do we can
we even answer that question and there
is some small borderline obviously
Securities involved and so on so forth
but if you can answer this
question we're also trying to understand
um once you get a qu once you get result
from a large language model Does this
answer really answer the question which
was asked so we have a number of steps
to verify before we provide any data
back to the users uh so it's not like
we're you know sending some initial
reply back if you can help we give you a
great instruction if you cannot help
let's say we don't know how to answer a
question we'll we'll send you some links
where
you might find answer yourself but we'll
never pretend that we really know what
to do in case we don't have any factual
grounds to support that case so here's a
better example if Kina asks how do I
extend the
trial kopala say hey in order for you to
extend the trial you do step number one
step number two step number three and
those steps are grounded meaning we have
a clear documentation we described very
well it it can be multiple sources so in
case we have a knowledge and we know
it's trustful we can help you with a
question if you ask how to release a
sales order we will say we don't really
know exactly how to do it because we
don't have data for it however we can
give you a number of links where we can
go ahead and maybe educate yourself
again we don't pretend that you have a
knowledge but we try to help as much as
we can when you work with a different uh
knowledge
basis okay now we're going to continue
our conversation how what about working
with with data because it's become a
little bit more tricky at this point of
time
yeah um yeah so here's an example
question where the user is asking for
some data right so they have asked is
there any inventory for uh the item with
that ID 1906s but they just said 1906s
and so in this case co-pilot replied and
this is a real scenario again that we
encountered while we were building
co-pilot chat uh yes I found five 1906s
in stock and then here's a link to this
item but then when the user goes to
click this link they actually get an
error because that item doesn't exist
and the problem in this scenario was
that um we weren't able to find any
records that matched what you asked for
but the llm just came up with an answer
anyway and it came up with a link that
it was valid enough that you could click
it and it would take you to business
Central but the actual record ID and the
bookmark don't exist and so when you go
to look at it you just get an error
saying no yeah I have no idea what
you're talking about basically um so how
do we ensure that you get reliable
answers when you're searching for data
and so you know if you ask a question
where you give us all the information
that we need to answer the question you
just say find the most recently posted
sales invoice and so you've told us that
you're looking for sales invoices and
you've told us like exactly what kind of
um filter you want to apply it's very
unambiguous request and so in this case
we need to figure out what kind of data
that is so we look at the request and we
grab all of the tables from the metadata
and then we pass all of that information
to the llm so we know what data is
installed whether that comes from the
base app or from your extensions and
we've extracted The Entity that you're
talking about from the request so that
we can check against all those pages
like which table are we talking about so
if that was successful then you know
perhaps in this instance we found the
sales headed table and so now we need to
apply some filters and sorting that will
retrieve the most recently posted sales
invoice and so again we'll go to the llm
to generate these filters and we'll
probably do some kind of sorting on the
posting date and also check whether the
status is that it was posted or released
so then finally once we've come up with
those filters and they check out then we
need to go and retrieve some records
from the database and then we can give
you back those records and and that's
the result that you see in the chat
today so this is like the sunshine
scenario where the user ask us for
something that we can easily deliver
because you gave us all the information
and it was a very simple request but
what if the user asked something like
find the overdue balance for a data and
if you've ever used the uh like demo
data like you sign up for a trial and
check that out then you probably know
that EDM is a customer but the llm
doesn't know that Edam is a customer the
LM has no idea what you're talking about
right you didn't specify that it was a
customer and so in this case we would go
through this whole path and figure out
like you know I have no idea a datm
doesn't match up with any of my tables
the datam doesn't match any of my data
types so instead we'll use the existing
searching company data um function and
so this is an example of um you know you
try to do something with AI but
unfortunately it didn't work but in this
case you can just fall back to existing
programmatic methods right we have the
searching company data that looks at the
most commonly used tables and in that
case it will search and find a data in
the customer table and then it's going
to send you back like this is the search
result that we found but if it can't
find a record obviously there's been a
failure right and this is what happened
in the previous scenario that I talked
about where it searched for 1906 didn't
find anything but it hallucinated and
actually it could fail at any of these
stages maybe we can't figure out what
the data type because you've mentioned
multiple or you didn't mention it at all
maybe we couldn't come up with any
filters because there's not enough
fields on the page that can satisfy that
request or maybe we failed to retrieve
the records because we were able to
figure everything out but you don't
actually have any posted sales invoices
or there aren't any items in stock with
that description and so in those cases
we actually need to say to the llm we
couldn't find any results you need to
specifically you know you can't just
give it the empty query object you need
to give it back an explanation please
apologize to the user and say uh say
that we couldn't find that right to
avoid this previous scenario so in this
case you know we're trying as hard as we
can to satisfy the request but when we
can't we need to know that we can't and
accept that because then the answers are
more reliable they're more trustworthy
it's much safer for the user to trust
that information um and we're you know
we're building trust with the users in
this way
right so here's another type of question
that you could ask for data um you might
ask who is my top customer and so
co-pilot is going to follow the same
path as before right it understands that
it needs to open the customer list and
it also tries to apply Sor in and
filters to satisfy the request but
unfortunately this query is uh is a
little bit ambiguous right what does the
top customer actually mean um so
co-pilot is just going to infer the
meaning of top from the available Fields
so it sees a field called sales like
local currency and it thinks it doesn't
need to apply a filter I can just sort
by uh sales and take the top one right
and so then it's going to retrieve
records from the database and write the
resp response um your top customer is a
datum and they have a a sales balance of
$53,000 right so how does the user know
that it actually returned what you
wanted right maybe my definition of the
as the user of what my top customer is
is like whether we play a lot of golf
together or something right what
actually is the metric that defines your
top customer and so the way that we
handle this is we will explain to you
why we made this decision right so
co-pilot generates the answer but it
also generates the explanation to why it
picked that record in the first place so
in this case you can see it's telling
you that it's sorted by the sales field
in descend in order to find the top
customer right and we've defined your
top customer as the one with the most
sales and so this way the user can
verify the answer that we gave you know
where it came from and then you can act
on those uh that
information in your own uh in your own
business yeah so in summary uh co-pilot
when it's finding data is able to
retrieve records by sorting and applying
filters so it can answer questions like
do I have tables or chairs in stock
because you said I'm looking for tables
or chairs items uh show me the latest
sales invoice for a datim show me all my
CES from Germany and in those cases you
gave us all the information we needed
but it can also search across company
data to retrieve named records so for if
you just say uh find information about a
datum I I I know I need to find Alpine
but I don't know what it is can you find
it for me and uh I'm looking for ID
100,000 like you know it can figure that
out for you right somebody told you to
find that record and you don't need to
go back and ask them you can just ask
co-pilot so one thing to remember with
this is that if users struggle to
navigate your ux then co-pilot will
struggle to navigate it too so co-pilot
can see the product via the metadata the
same way that the user can see the
fields and uh columns on the page and so
you need to make sure that all of the
information to satisfy common user
requests is on the page is in the page
metadata so that when we pass that page
metadata to co-pilot co-pilot can see oh
I can sort by sales I can uh you extract
the contact information from the
customer that sort of thing right so
make sure you include all of the
information that would help co-pilot
fulfill common requests about your uh
extensions and speaking of extensions
fgny is going to talk about um how
extensions integrate with co-pilot
chat so let's back to our Kyo demo from
yesterday I have an extension built by
me as a developer not Microsoft and I
installed that environment ment it's
about rewards for our customers I ask
show me customers with go rewards so one
is the feedback we are saying hey can
you just go to customer list filter it
yourself well if I know where to go I
can but if I don't know to I'm just
looking on a call find some data I don't
know those pages maybe I'm very light
user that fop pilot really really helps
to save me those Clicks in this case it
come up with a couple of records and of
course uh it it explains and if you
click you know a link it will show you
the page and you can clearly understand
how that logic or was applied so you ask
for a go customers and in this case it
just tend to go to customer page because
there is a field called reward you know
find and list but you can find you can
think about like show me my
uh important orders show me latest
delayed cases like things which may be
not that obvious how to find that for
compilot really really helps with your
extensions uh for your users however the
question
is what does it take us to build
that the way how we think about that is
exactly what arton is saying that if you
don't if we a community don't do enough
job to describe your extensions your
Fields your actions what it's about it's
really hard to expect co-pilot actually
like every human being to work with that
product data or structure so in this
case as a developer it just takes me a
bit of extra craft to describe my fields
for the tool tips add them to the proper
Pages add them to the list and then the
Machinery is aware about the metadata
it's aware about those fields about
those extension and now copal can really
work one of the feedback we getting from
our early adopters hey use a guys pilot
but it doesn't really work as my
extension sure because you have a field
115 which means for you currency and for
us it's like like how do you expect us
to to work with it if you cannot really
understand what is it
about there was another poll question we
asked can chat answer questions about
data new extension and uh the answer is
yes as long as it's well
described um and we can answer those
questions yeah we can can really uh help
with the job if you ask a question about
chat uh show me my sales by months for
the last 5 years if there is no place in
application even to answer that question
copilot cannot help for now if you
expect any maybe reports we can't we can
help either but for questions for you
can ask your colleague to go ahead with
the product find it present uh ciler
should be able to help as
well right now just for information we
don't really give you any way to extend
chat maybe with a ASL developer but
again as long as you describe your
applications not like properly but
better there is a high chances copilot
will help your users U with your
Solutions every time we think about
co-pilot work for now and any future we
try to follow this principle that
meaningful descriptions are essential
for humans like me and arton and for AI
LM featur here compilot to understand
the application so is as long as it's
meaningfully described we can do a good
job to understand and work with this
data and we need your help uh to get
this
done there are a number of things which
copilot cannot do today and actually
users expectation is super high like
technology is all around you can expect
it ask any question and get an answer
and unfortunately we're not there yet if
you have some very complex data
aggregation questions we don't we can't
help youly now for example show me
aggregate sales by all the customers and
countries uh for that type of question
we have an amazing feature called
analysis assist which can also you can
use that copilot you can ask it natural
question maybe we can help with that but
not from our chat
yet like a short summary what we discuss
we try to be grounded in the real data
so you can trust if you get the results
and you can take an actions based on
that and we do work invisible for you
which sometimes take some extra times to
figure out that it's really what you can
rely and use um and we try to provide
you back a lot of instructions also as
you we would like you to provide your
users instruction conversation so we can
answer the question to best to our
ability and as Aron mentioned if you're
not sure you can always see and
understand hey that's how we get a reply
maybe I need to ask another question
show me who owners money meaning show me
customers who Maybe have some all
standed balance and with that question
we can give you more reliable
response it's Paramount important you
give us feedback every time you X up and
down like some up or thumb down we get
notification in the back end so we can
go ahead and improve your queries and
with that we have some time for Q&A we
hope it's interesting conversation on
topic we have around like 10 minutes
before we go to next conversation so
let's just do that yep unfortunately
we're out of t-shirts but I'm still
going to throw the Box anyway I saw you
first so good
luck brilliant thank you you hear me
yeah okay um you made the example that I
can ask co-pilot a question and as long
as my colleague can give me the answer
co-pilot should do this as well um Does
it include permission sets into the
answers so if my colleague has sucess
and I'm not
I would expect I don't get the answer
yeah so when we um queried the metadata
question yeah sorry so the question was
um does co-pilot chat uh respect your
permissions right so you know like if my
colleague should be able to give me the
answer co-pilot should be able to give
me the answer too but obviously my
colleague has permissions uh applied so
that he can't access every single thing
in business Central he can only see his
own personal view of uh of the data in
your company and so yes co-pilot
respects the user's permissions right so
when the user ask a question they can
only um ask questions like co-pilots
only going to recognize named entities
like sales invoices customers that the
user has permission to even see the
metadata for and that's the list that
we'll pass to the llm and then when they
actually request the data we also use
like your table permissions and things
like this to to limit the data that you
can access so you can't use co-pilot to
like circumvent the permissions and find
your manager exactly right you should
only be able to see things with co-pilot
chat that you can see via the UI already
yeah hey the same mindset if you and UI
can find this data then copilot as you
can hopefully answer the same data
questions with the same permissions as
you have as a
user we had a practice with this before
the session and uh we all sucked um
yeah so since the inputs and outputs to
the AI are customer data how do you guys
actually use that feedback thumbs up
thumbs down to improve the experience
and and how do we as extension
Developers use that that feedback to
improve our own co-pilot features yes so
um we do collect the fact that you gave
a thumbs up and a thumbs down into
limitary but at the moment we're not
actually capturing the outputs we're
working on solutions to this internally
but what you will notice is if you give
a thumbs up um it's just going to say
like I don't want to click that one yet
if you give a thumbs up it's going to
say like thanks for the feedback and
we've received the fact that this was
positive and we can see like the
distribution if you're asking for
information we can see the distribution
that was like uh positive feedback or
negative feedback and so we have
somewhat of an idea of how like well
received a feature is but if you give us
a thumbs down you can actually choose um
categories of response so you can say
like you know the information was
inaccurate it was offensive or um like
some other response and we are also
working on adding a free text field to
this where we're going to capture that
data right um because you know like with
the feedback form the user actually
consenting to providing this information
when they press submit and so we
actually are able to put that box in and
it will come okay down the line yeah to
us okay perfect thank
you yeah
behind thank you I noticed that in this
example with extension I do not see the
filters that was applied to uh to
receive the uh reply is it like will be
like in um all
cases um sorry like the the example that
was in the on the screen this example
yeah uh in previous example it said uh
um there was filtering by description or
sales elcy but here in this example I do
not see this in the copilot
window yeah it's a if you just expand
this ah yeah okay yeah exctly so if you
hover over the citation so you expand
the references at the bottom then you
will see the explanation right we we
don't want to take up too much of the
screen but it is there the main problem
the main problem we're trying to solve
if I if he'll tell you here's the gold
customer here's the top sales how do you
know how do you know like exactly no
like if you ask you what is the sales
like it's like $100 like how do like you
cannot trust if you don't know what 100
means the way for us to demystify Magic
saying hey this three means from this
page with this filters and that's how
you see that what system tells you
exactly what you experience it might be
not what you're looking for you change
your question but you wouldn't say like
you know it's number 74 42 and then God
knows what yes I think it's very helpful
to have yeah because if you don't if you
cannot explain to yourself why how can
you you know communicate with someone
else it's really really hard and this is
not about business Central yeah it's a
Microsoft principle you want to
demystify that answer in a proper way so
you can really trust and that's the
easiest way just show you how we
calculate that if we
can yeah there's right behind you
uh we are a Dutch company so I'm curious
how it will work with the translations
so in case we have our own translations
in English and in Dutch yeah great
question so the question is it's all in
English but how would it work work with
translations multiple languages also
maybe if you search for master data now
it's a different languages you know if
you're in Denmark everything since like
your item uh price list will be in
Danish obviously not in English or
whatever country is so right now as of
today we're in a preview in English only
English languages for now and I think
it's fair to say we're in a p to open up
it for multiple
languages in fact all our immersive
features everything you've seen from our
keynote you know when you have prom
dialects in products like sales
suggestions all those features are
available in all multiple languages with
24.2 release so it's not not English
only anymore so you can type in Danish
in English in French in Italian in
Spanish in Sweden in Japanese and so on
so forth but the chat for now is in
English because we need to figure out
some stuff but we only pass to expand
more languages as we go thank
you I have another question so I saw in
your screenshots that you have a page
with a tool tip and a table with a tool
tip so you've added the multil language
Capt um tool tip on the table so I was
wondering do you fetch the table two tip
for the pages because course your
screenshots likes to um it looks like
you have to do it on both and that's
what you do not want yeah so a great
question was what do you really use
metadata to find your uh objects and we
show you example of the tool tips it
just wor illustrational purposes we use
all the metadata we can find but if we
have nothing we cannot help the point
was if you define then it's on us to
find where we have tool tips uh
descriptions like whatever we have so to
speak yeah so if we start using it on
the table then it's fine we don't have
to do it on the page because it's
inherited ideally it should be for us
sufficient but so as long as you define
well we should be able to do a good job
to find it right now I think we're
looking for pages but it's something we
Microsoft just need to optimize it's not
really on you yeah well so the thing is
we're they're taking the caption that
you write on the table right I think we
got this question earlier in the session
this morning like if you build your
extension and you only have a localized
version there isn't an English version
then yeah we're going to send those
localized captions to the llm and it's
up to you to check like how does
co-pilot chat perform with your
extension because in our experience like
if you start passing foreign language
captions it actually does work fine but
you should definitely like double check
this and you know see if the quality is
there and if not consider having a like
backup English captions if that's
possible somehow just to be clear you
can also go ahead and try type nouns in
Spanish we're just saying that we
believe it will work in English but it's
not like we prohibit you to use
different
languages yeah that's say the right
answer uh I have a question so uh is it
only tool tips and field descriptions as
a source of uh I don't know copilot
learning to answer some questions or can
we somehow feed it with additional
documentation like user guides manuals
and so on if no is it planed to be in
the future yes so we had the slide
before can you rephrase the question
maybe yeah so okay sorry so the the
question was um is it only taking the
information about the um fields from the
metadata or can we also include uh
additional documentation like if you
have your own documentation hosted
online and at the moment no it's only
from the metadata so all of the
information co-pilot sees is the
structure of the page the fields that
are there um the about text like tool
tips descriptions captions that sort of
thing right so you need to make sure
that you fully describe your application
in terms of the metadata um at the
moment we only source external
information from Microsoft learn not
from third party documentation yeah as
of now if you're nice we cannot you
cannot yet bring your description of
your extension of your product because
your user will ask how to do this with
your solution we don't have it right now
it's obviously obvious thing to fulfill
we on a pass but as of now it's look for
Microsoft documentation the sources we
can trust just to start with it but it's
an excellent
question I think we probably have time
for one more yes yeah
yeah cool okay maybe we got them all if
you have any more questions you can
obviously come and find us after the
talk uh but thanks everybody for
attending and uh for all the questions
they were great yeah thanks again
