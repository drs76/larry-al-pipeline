# BC TechDays 2023 - Introducing Microsoft Dynamics 365 Copilot

- **Source:** https://www.youtube.com/watch?v=eAg3l9UHuQo
- **Video ID:** eAg3l9UHuQo
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 44m51s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

some some and this is evgeny who you saw
in the keynote just now uh we'll be
talking a little bit about Dynamics 365
copilot and uh yeah so this is the the
agenda that you'll see
um so first we'll start with kind of
just the latest of elements in
generative AI overall because there's
just so much going on at the moment that
we think it's worth kind of recovering
that the stuff that's been happening you
know in the last even few weeks
then we'll dive into Dynamics 365
co-pilot and how that specifically Works
in business Central and then what we see
happening next within business Central
and finally we'll finish uh on how you
know your walk and get started and play
with it yourselves
so again why don't you tell us what's
what's new in generative AI how many of
you try to use chair GPT
okay we're on the same page is good
so as it was like a very famous quote
back in like 15 years ago the software
will eat the world and these days to
believe AI will ease the world
open AI doing an amazing job to drive
Innovation with large language models as
you all know we instant show you some of
those examples and you've seen how it
can be used and obviously for us it's a
big deal and you want to be part of this
Evolution and bring those capabilities
to the product but before we just talk
about that it's really really crazy time
like it's a crazy crazy crazy times and
it kind of reminds me back to
back in the day when the cloud and Azure
was born you have new capabilities every
two weeks everything in the preview the
tools you use one month finally Obsolete
and so on and so forth so it's a huge
huge pace of development even if I would
make this talk one month ago my talk
would be obsolete so we need to catch up
constantly what's going on back in March
open AI announced
plugin capabilities which allow you to
bring real live data to jgbt so you can
basically get real-time insights it was
pretty pretty cool and just last week
last week there is much more
announcements now we can use a lot of
structured way to talk to open AI large
language models there's a lot of
Innovations going on there
now uh
the race of plugins raise a lot of
discussions about those tools and apps
could do like some last month was like a
congress
uh hearing you know should they regulate
at all specific open AI or related
features and I think so far is saying we
are fine and obviously like Sam Altman
who is the CEO of openai he's just
traveling for last five weeks to the
world talking to the world leaders try
to promote large language models across
the countries you know from safety
perspective how can the trust and so on
so forth in Denmark we have a number of
financial institutions who basically
literally ban employees to use
even being chat which is a shame they're
missing out so there's a lot of a lot of
questions about trust you know is your
customers data is using so and so forth
so we'll talk about all this today
on a Microsoft front
maybe because we even come to Microsoft
so in Microsoft we believe we're
entering this kind of era of co-pilot
and what does co-pilot even mean copilot
is a pretty cool term I think the idea
is that we have like Sam who really
knows what he wanted to do and Achieve
or Stefano Vincent and then you get an
assistant who can help you to deal with
a lot of tasks so co-pilot it's not like
autopilot you only control but we can
get a lot of creativity and help with a
very basic task
um like I guess that's the main idea of
a co-pilot and the user's terminology
consistently across Microsoft and
industries these days more and more
now on the Microsoft front a lot of
Innovations happen as well like last
months we had a Microsoft build which is
like a biggest development conference on
a company company level and you had like
50 plus announcement all around AI how
did we build AI what is the Azure
Services how to bring it to your
products
on all scale one is the most excited
announcement I found that even in
Windows Windows was like the biggest
Microsoft canvas if you will you're
going to bring those conversational chat
experience so you can go ahead and
interact with the system in a natural
way and I think it's fair to say you'll
see those conversational experiences
rolling out across all Microsoft
products at some point and Dynamics is
also a product
so it's interesting how things will go
on a development front on the
development front tools Frameworks uh we
also announced a number of tools
libraries Frameworks so you can go ahead
and build AI features which again
nothing as this even exists like two
months ago at least not publicly
available I should probably say
this is like a random slide I took from
a build
and what's cool about what's really
really cool about the slight and
impressive we start talking about
Frameworks and Technologies how do you
bring compiler capabilities to your
products you can go ahead and see
something like Ai orchestration and
we'll also show you some of that a bit
you start seeing like copilots and then
obviously how can you plug it so it kind
of worked consistently across Microsoft
products
every time we talked about AI we talk
about responsible AI so how many of you
heard this term before responsible AI
so it sounds very fluffy but actually
it's a very serious business it's a set
of guidance and principles which we use
to build
yeah I would say design build and
Implement features to making sure that
the user use those features it's safe
it's a straightforward it's not
misleading and so on so forth and I hope
I end this presentation you'll see
how do you apply some of those practices
uh yeah on practice
now
we're going to demo you how the copilot
system works in business Central
and before we do that just couple of
highlights first of all everything you
see has nothing to do to charge GPT like
you know chargpt has nothing to do to
what Microsoft does of what we do
everything we build is based on Azure
open AI Services it's an Enterprise
scale service security compliance trust
in place jail boundaries whatever you
mean
uh
yeah one of the main principles of our
work something called human in a loop
it basically means that it should be
very very aware of what's going on when
you interact with the system and that
will ask Sam to give us a quick overview
how the system works and then show us
some demos
yeah thanks again
um so yeah I'm going to kind of just
describe how this copilot system works
in practice and then maybe show a quick
demo of it in action so the way the
whole thing works is it starts with some
kind of user prompting the whole system
and in this case they can ask us the
system to suggest some new marketing
text
um
what is kind of interesting here is that
Copa can't actually always help you so
if there's not a lot of information uh
about this like let's say item uh then
you know it's not going to be able to
generate a whole piece of marketing text
because it will just end up fabricating
a lot of things and you know you don't
want that and if you if you start
providing like a few facts of
information about the item then it can
very easily like build a short tagline
and then as you give it like more
context more information uh you'll see
that it can actually start producing
like whole paragraphs of text
in test yeah making some kind of Market
marketing text
um so yeah once this user prompt has
been sent into the system it will do
some pre-processing in the form of
grounding and that is where it will go
through the whole system and gather all
the facts it knows about this item
um what's kind of uh interesting here is
that it doesn't necessarily just have to
go to say the item record it could pull
it from other sources like I don't know
your sales statistics or like product
reviews if you have some means of
feeding that information into it
and yeah another very important point is
that it does reflect all the security uh
like permission sets that kind of thing
and privacy settings that the admin has
defined uh for for the given user so it
will never like grab more information
than than the user has access to
so now once we have all this like
metadata available to us we will go
ahead and generate some prompt that we
go ahead to send to the large language
model
um and this prompt includes like all
kinds of additional instructions to yeah
basically make the response quite
responsible and avoiding like yeah
harmful content uh trying to avoid bias
and especially like the fabrication
fabrication as well can you show example
about Amsterdam lamp we found yeah so in
our demo data for example we have like
the the Amsterdam lamp and it's a its
color is red
um so the the marketing tag suggestions
can sometimes get a bit too colorful
with that Association so uh yeah we have
to tell it to like yeah calm down
um so yeah that's that's some fun like
even our own demo data we didn't realize
um so yeah what happens is the the large
language model will generate some piece
of text and we don't then throw it
straight back to the user we do some
post-processing on it
um which we also so-called grounding and
it does a few extra kind of checks on it
so any kind of figures it generates it
will cross check with the facts we
provided from the grounding earlier
um we also make sure that the response
that was generated matches the format
that was requested in the user prompt so
for example if you've asked for a
tagline and a paragraph we check like
the text and does it look like there's a
tagline and a paragraph then good and if
not then you know we discard it and of
course we do like some kind of content
moderation on it to make sure that you
know we don't have these red amps that
I'm lumps
um and yeah like I said so if it passes
the if it fills these checks we will uh
discard the uh the text and then we will
re-prompt the model uh a few times and
then hopefully we get a good result and
then once we do uh we send that one up
uh back to the user and it's kind of
important here that the result that we
return is still like temporary and we
don't want to like commit it to a
database without the user like you know
the human being in control
um so they can go ahead look at the text
modify it click OK cancel dismiss
whatever and
um yeah so that's that so I'll jump over
and show you how this actually works in
the product today
so this is a just a Sandbox environment
I created yesterday
and we have the the welcome Banner here
so I can go ahead and ask it to show me
the demo tools and we've added a new
tool here which is a correctly co-pilot
and you'll see uh yeah this is talking
about the AI powered product
descriptions and you can go ahead and
just start the tour
and what this does is uh it opens up the
item card and uh yeah you get a little
uh like hero tour thing
um that yeah sounds like stop typing and
start selling and you can click next and
it will point you to this new marketing
text uh fact box that we've created in
22. so I can say go ahead and got it and
then I can create with a copilot
and the very first time you use this
capability will show admins this uh this
page and basically it means that the
admin can choose whether or not they
want to enable these AI capabilities for
the environment and if you go ahead and
click agree then it's now enabled and if
you click disagree it will disable it
but the marketing text functionality
will still be there it just won't have
uh copilot capabilities okay can you
comment on that so basically if you
don't like IAI if you disable it you can
still use all the features you can still
create a marking description manually
obviously vendors still upload to
Shopify store just as a compiler you can
do it faster with a help but if you
don't like it you turn it off and it's
like back to business as I've been
before yeah yeah we're seeing it very
much as like a opt-in experience so it's
up to you
yep so I'll go and close this and uh now
it's uh it's um doing all the
pre-processing and then prompt
generation going to the model and then
coming back with the text checking that
it looks good and then yeah here we have
uh here we have some text and uh so this
is the the Athens desk and in our demo
data we do have a few item attributes
here so that's how it's able to generate
both this tagline and description I
can't read it all here of course so I
need to go and review it in in the the
review page
um you can see here like the attributes
it's trying to include what kind of
format I want the text to be
um and yeah I can be like oh I want to
make I don't know the tagline bold or
something like that
um we actually have like more settings
as well so if let's say you know I want
to really focus on the sustainability of
the disk so in the item attributes we
have the FSC certification included so I
can say please uh emphasize the
sustainability and I can pick a tone of
voice that rate ranges from you know
very like yeah well formal to a more
like fun upbeat creative style language
so you can try and pick something that
matches your brand so I'll just go for
Creative because then you get the the
best results
and um so I can either go ahead and
create a draft and that will delete
what's being generated so far or I can
actually choose to append it to what you
have so for example if you're just
generating the tagline and then you
wanted to add a paragraph later you can
you can do that kind of thing but anyway
I'll just replace it and hit create
draft
and um then hopefully we get some more
texts
yeah so yeah we've got some new tagline
here and uh and a paragraph and you can
decide that you don't like it and then
you can always like undo and go back
that kind of thing so we'll just keep
what this was and I'll click ok
and now now the marketing text has been
persisted in the database and I don't
have the Shopify integration setup here
on this environment but if I did I could
then go ahead and publish it straight to
my Shopify store or use it with some
other integration here
yeah how do we know is that that maybe
what if I'm a user I try to use it and I
don't satisfy it with the quality of
those texts yes very important so um in
in this edit dialog at the very bottom
we have these like thumbs up thumbs down
things
um so if you are not happy with the
value that's been generated or you like
it please do send us that signal it just
emits a Telemetry signal to us that the
generation was good and we'll be using
that to kind of tweak this like meta
prompt that we we use to to improve that
in the future
um something else very important I want
to mention is that we're not using any
of this business data to retrain the
model it's purely supplemented as part
of the grounding for that individual
prompt to the language model so it's not
like assisted uh yeah to retrain
cool
yeah I'll jump back to slides
yeah so
um it's it's ready for you to all try
out in the production of sandbox
environments in any VC localization in
the latest update
um there are a few caveats here so it's
it's only supported in English languages
at the moment so if you're using a
localization which is not in English by
default you can go in your user settings
and change it to English and then the
co-pilot stuff should light up
um yeah as I mentioned the the admin
consent is required the very first time
you use the integration
um if you want to change your mind later
on you can go to the Privacy notices
page and then you can reject the
integration there
um yeah and I also mentioned the
marketing tax feature works with the
co-file integration disabled but then
you just have like a text box where you
can put text and you need to be creative
yourself
um and if you're upgrading from an
earlier environment it's controlled by a
feature key so you'll need to turn it on
in the feature management page so please
do that maybe when I have a quick
comment about languages because the
first question we'll get after the
session can I use it in my language
German Danish Dutch Ukrainian whatever
and the answer is like especially you
can say I tried GPT I tried Bing chat I
can the truth is that English languages
is the only officially supported
languages for open AI the models we are
using so as more languages to be allowed
officially we'll be able to bring it to
you as well so it's not like it's an
engineering challenge it's more like
it's still in preview so we started in
English and more languages will follow
hopefully soon
yeah really like as soon as the text
available we'll push it out so that's
the dream and speaking of Dreams uh
evgenie how do you see our vision for AI
in the future
yeah so another interesting code people
start saying now and not like
English-speaking people but basically
saying the way how you start interacting
with the systems is basically in your
natural language which become like a
next programming language so to speak
this way how you express what you want
to achieve get results and so on so
forth
we show you this Vision early today I
just show you the slide again uh for a
reference
We Believe
we have a lot of capabilities to offer
within the product and obviously that's
for you as a community come first with
your extensions with your value
proposition and so on so forth then you
have molecular conversational Circle
which is more like probably on Microsoft
on us to build first you saw how it's
coming to Windows so it's kind of on us
and then we can have discussion how we
bring your capabilities there it's
finally has been connected to the whole
world
so you can maybe go to Bing chat and
start asking give me sales order from
business Central you should be able to
go to our find the system retrieve data
and you can do some magical things like
that
however we need to start somewhere
right now
if you would ask me hey how can I
basically extend or reuse wherever you
guys build out of the core product I
will probably tell you we don't really
have anything out of the box however we
just announced earlier today that we do
give you samples starting toolkits so
you can go ahead and experiment with
your generative AI features and the idea
that it should be super straightforward
like it should be like no big deal or
drama should should give you no excuse
not to start I guess that will be the
right statement
those announcements went live on nail
home we recommend to use our great
development tools so you kind of get
updated on what to do and how things
evolving
and with that let's take a look on those
tools and see what you could build or
what we could build with that for a
product going forward
yeah yeah so I'll just jump over back to
my screen so yeah I have Visual Studio
code open here with Al home and it
should all be popping up for you with
the the latest developer news that we
just posted announcing this uh yeah
quick start extension that you can use
within the help itself you'll see that
there is a link in AKA and a slink that
will take you straight to the repo and
there's a little readme to help like get
started
um but I thought it would be fun to just
jump into what the sample is doing and
um how uh yeah how it works and then
show you in an action so uh what it
ships with by default is this page
extension on the item card which adds a
new action page action which is called
Suggest item category and what that does
is it will suggest an item category for
an item based on its description
so it's like a kind of Hello World level
example
so you'll see in the action the action
trigger it goes ahead and calls this
magical procedure called the suggest
item category and that returns a
suggested item category then we we get
it and we build some kind of
confirmation message and then show to
the user this confirmation dialog and
because it's very important that you
know we don't just automatically update
business data and we should make sure
the user is uh like okay with the
changes that you make so if they say no
we bail out and if they say yes we go
ahead and update the rack so I'll just
suggest that some category actually do
so if I just scroll down
um it goes ahead and builds a list of
the the item categories that exist in
the system so that's kind of you can
think of that as the grounding for the
pre-processing where we uh we yeah we
pull all the item categories and build a
um a list in a string and then we go
ahead and call this Azure open AI
generate completion helper so that will
go to the Azure open AI service
and call the completions endpoint with a
prompt and the number of tokens it can
use and a temperature value I'll
describe those in a second
um but the way you can think of the
completions in case you're not aware is
you give it a piece of text and then it
will auto complete the remainder of of
that sentence so in this case we have
provided some kind of prompt up here
which is given a list of item categories
pick one that would suit an item with
the name whatever here are the item
categories and then here is the selected
category and you'll see there's no like
placeholder here we've just kind of
stopped the sentence mid-sentence and
then the completion endpoint will just
complete it with the suggested category
so it's like a pretty pretty simple
example
so then we get this category back from
from the model and we will go ahead and
then pass that into validate category
and all that does is it it makes sure
that this item category code exists and
yeah if it doesn't it will throw an
error and bail out but if it does then
it's good but and we can exit the
procedure and hopefully we have a good
suggestion so I'll go ahead and publish
this is always testing the Wi-Fi
all right let's login it's always good
as well
should be publishing now oops
yeah and I forgot to update the default
page of course
so I'll just jump over to the items
and so in the Athens desk we normally do
have an item category code in the demo
data but in this case I've already
deleted it
um and you can see we have this new
action here suggested item category so
you can go ahead and click that and um
yeah exactly it pulls all the item
categories that are in the system and
builds the prompt sends it to Azure open
AI it returns uh yeah disk and then we
validate that that is a valid one and
now we show this confirmation dialog
like is this is this the one you want
and it yeah disk makes sense for Athens
desk and uh just to kind of show it's
not like hard coded we can I don't know
take take the beans and yeah so we have
some some roasted beans and again if I
asked to suggest if it says like okay
the item has agree with beans probably
makes sense for it so great and that's
good and like of course you could build
your own kind of matching logic uh with
like reg axes and other kind of
horrifying code
um and I'll take like a lot more time
but here you know I just write my
instruction in a simple label and now I
can get these kind of processes back
like much faster can you double down the
statement so how would you build this
kind of defaulting before like what
would you do
ah uh yeah yeah reg axes would be the
way way to go right or uh we'll have to
figure out samples regas kind of parsing
partial git suggestion
doable for sure takes time code and
here's more like just one expression in
your natural language given categories
and this product please give me the best
match one two three we get it back to
the user just easy to code works
yeah get great yeah yeah
so it depends a lot on the quality of
trump of course
um but yeah when it works it is it's
really good yeah
all right so I'll uh jump back to the
slides
um so so that's kind of what we shift
with the sample by default but here's
another kind of fun example is uh
something you might want to do is
extract information from emails which
again is some kind of like horrifying
problem to try and solve with the
regexes and other kind of stuff uh but
like is a trivial task with these large
language models now so in this case yeah
we have an example email and then we
have some kind of prompt here that says
like analyze the above text get all the
information out of it and give me a Json
objects while you're at it and just for
fun I like uh through that together
using using the sample I just added
and you uh a new page maybe if you're
Keen you notice the ad appeared
um so all this does is it's just a new
page it has a field that has some kind
of message content it's very simple and
then an action also very simple it just
goes to the completion's endpoint with
some prompt and and the message content
and the prompt is pretty much what you
saw in the slide so I analyzed the
message get the information about it
give it to me as a product description
and quantity in Json format here's the
message here's the item information
um so if I go back here
and hopefully I find the page yeah so we
have we have the the text here and I can
go ahead and extract the the information
and you know just like that I now have a
lovely Json that I can pause and do do
whatever with so that's that's pretty
cool
um so now for fun
I can go ahead and again modify I don't
know get some charges as well
I'll say yes some charges
we'll see what it does
and uh so so it's all it's all about you
know the quality of the prompt that
you're putting in and uh so with the the
AI home uh post we uh we we've uh also
going to be putting out a blog post and
in there we'll have a bunch of resources
there so you can
um go and learn more about like the
prompt engineering side of stuff because
that is like super critical to nail and
you know this is just the first prompt I
I put in my mind and
um yeah so you can play with it in ale
very easily if you get the Azure open AI
key there's also a playground in there
so you can like very quickly iterate on
your prompt and uh yeah see how that all
goes so definitely like
look into the front engineering let's
see here for a second so if you're not
impressed so far you better shoot like
better back to this like a free text it
has like extra keyboard extra mean one
which is kind of obvious but super hard
to engineer and develop uh we talk about
some power plugs somewhere late in
conversation unrelated to initial
statement we could detect that so the
ability to extract data with kind of
small prompt is unparalleled compared to
how would you have to code to get
results even closer to that
that's why we think it's kind of pretty
pretty impressive yeah yeah so like in
this case for example you would improve
the prompt by saying make sure the
quantity is always a numerical value or
you know things things like that you can
also what's very powerful is uh give a
few examples uh beforehand and that's
called a few short prompt
um and then that you can really steer
the model towards the structured format
that you're wanting
um yeah so I'll jump back to the slides
um so yeah Afghani uh hand back to you
yeah like we just showed a couple of
examples think about you need to write a
logic defined duplicates you'll say
given as a Fields some kind of fields to
try to parse it database give
comparisonment give me some suggestions
which I can merge
I think about every time you have the
default value extract merge match like
large language models give a lot of
capabilities for us and for you to bring
to the products with very like not like
small but some effort
uncomparable I guess what it took to
build before so we wanted to get started
on the journey and the easiest way you
can do is start using copilots and the
easiest way to do is to use bin copilot
or Bing chat either day how to get on
Turpin how to order this beer whatever
price it just works great
we show you GitHub copilot for
development tools we're not talking
about it right now but it's a great
capabilities
if you notice every time we speak there
is like a live translation happening on
screen it's another AI feature we just
come into PowerPoint which be able to
analyze uh voice to speech in a real
time which is pretty cool that's why we
enable it for this session
and finally we want you to get this open
Azure AI key it's like a small secret
statement
before you can get started
using those features
if you think about our roadmap or what
we officially communicate to you there
is a section about future of AI for next
wave or for this wave basically if
you're in full Microsoft said we get
more stuff for you you can get started
more features more capabilities and so
on so forth so we're actually working to
bring even more intelligence and I wish
we could share more but they want to
save our employment so we wait until
August to share more with you what's
going on
uh we have a conversation on Yammer if
you I mean there is no like a little
excuse why you shouldn't go ahead and
join the conversation people share
examples like ideas flying around we're
not out of ideas so inspiration just go
ahead and join the conversation so help
us to build what you prioritize and
build next to the product
and with that
I guess we'll have some time for Q a
to wrap the session yeah we have some
links but we'll skip it for now
yeah let's let's have a like open q a we
have like around 12 minutes to talk
about this topic
yes sir
I'll give you
sorry
now the question was how can I get
access to this key practically as a
developer to start experimenting and
with that maybe would you mind to share
our blog post and just show the content
of the article we wrote yeah
we need to project second screen yeah no
just I mean uh yeah I don't know the
link to the blog post but email home at
least
this one
ah okay yeah
okay we don't have it in the current
current documentation we have a blog
post coming we hope it was this morning
we didn't uh you need to get a key today
you need to basically go ahead to Azure
open AI actually get a key the first
link you click if allow the form and
you'll be able to get this key very very
soon so you have like a development
Azure subscription and you can get to
that
so this is a process it's still white
listed because whole world is running
for this gold resources to be honest
it's like a crazy it's like you have
like a open air inside like a dragons
and dragons and dragons and you need to
pass all that to get because it's like a
whole world try to get as a resource but
you can go ahead and add a key for azure
Open Air Services
uh is it paid it's a good question yes
so you um when you're calling the Azure
open AI service they charge you based on
the tokens in your in your prompt and
then the number of tokens that get
generated off the top of my head GPT 3.5
which is uh the tax Divinity 3 Model uh
I think it's like two cents per thousand
tokens and you can think of a token as
if you take the number of words in a
prompt multiply it by 1.3 that's like a
very rough approximation to the number
of tokens that will be maybe to talk
about this question so it's free to get
a key but when you start using open Aja
models you pay for consumption back and
forth the Microsoft pricing is the same
pricing is open AI due to our unique
partnership those prices tend to get
reduced week over week last week we
announced that GDP 3.5 turbo goes like I
don't know 25 it's a tenth of the price
tenth of the price we should make us
more affordable yeah so you need to pay
for that as of preview all Microsoft
products not only business Central all
Microsoft products give you co-pilots
for free one more time all the features
we show you with AI you get it for free
as a users and customers you don't need
to pay for that it might change in the
future but we'll figure out right now
like Microsoft wanted to use AI on scale
so it's in our interest you have access
which is free another observation which
is like not intuitive but when we
release this feature back in March it
was really hard to get open air even to
being chat however with business Central
every customer every sandbox basically
could experience generative AI of free
of charge
which is pretty impressive and very
proud as a team to deliver that
let's take another question yes sir
if you throw it
I don't know if it's working because I
didn't hear his voice yeah it's just a
simple question I miss missed something
maybe but is this Cloud only or on-prem
so the uh the sample we published that
will work in both on-prem so for local
development as well and uh yeah in in
sandboxes you saw me publish the
marketing text feature also works
on-prem but the the co-pilot powered
suggestions is cloud only
so I think it's a great question for
every feature we're going to show you
today the first question is it in cloud
or is on-prem and the default will be
answer is in Cloud by default you want
to grow a cloud business it just makes
sense but we're not really doing any
artificial how to say
like a restriction restrictions to make
sure it's not possible on on-prem that's
not a gain weight at all
thank you
cool
yes sir
I have it small technical question icon
that you showed on the action which is
called Sparkling something when I tried
some weeks ago to put that it didn't
show this nice uh image is it like a
platform support now yeah so in 22 oh it
should work it should show up it's not
been added to the compiler yet so you
still do get a warning uh but yeah if
you publish it should it should just
appear yeah
we have two so there's a sparkle uh
which is the let me just go go back
let's all jump yeah so there's a sparkle
filled uh which is this one here and
then on the item card uh there's just a
sparkle which is the not-filled variant
so the question was if you build your AI
features how can you make look and feel
the same you can build the same
iconography the same icon we are not
giving you today the way to make a flare
or shining actually it's very unique to
business Central before that you haven't
seen that level of Love or craft I would
say it's kind of very looks very nice
again as you're thinking how the
platform look like most likely we won't
have the same experience so
not now but
yeah maybe soon
very soon
yeah we'll try and get some like ux
guidelines out as well for when you use
it all right one more question for the
marketing text
the
prompt is hidden somewhere on the Azure
fault so are you going to like somehow
expose that so we can
learn from that yeah yeah so just to
repeat question so right now we are
pulling the The Prompt for the marketing
text out of key Vault and we're like
dynamically constructing it we've
basically done that so we can you know
update the prompt quite easily
um yeah maybe at some point we can take
a look if we can share it I think also
the fair just say that Microsoft treats
all the prompt as some kind of IP for
now so it's kind of hidden for a purpose
as well you can argue it's so hidden it
is so essential uh we see we put a lot
of work through research how to Art how
to put meta prompt so your suggestion
deal with the bias in languages good
luck Jose to figure out how to do it
effectively I also deal with a biasing
harmful content so right now it's hidden
for you it's probably a year from now
it'll be probably like a more common
knowledge yeah
it's a great question yeah
uh hello guys uh that was quite
impressive just a quick question what
are the limitation of the AI so for
example for the subcategories you showed
us that actually gets all the categories
we send it there and then we get a
suggestion can we add another three four
uh basically what are the limits how far
we can go with this yeah so so it all uh
yeah I can take it uh so so it all
depends on the model
um that you've picked and they've all
got different uh limitations but at a
high level uh there's a certain number
of tokens you can pass in and a certain
number of tokens the model can generate
in a single call
um so the tokens you can pass in that's
kind of all the context that you can
give and so this was a kind of a simple
example
um where we're just building a list of
them all and then feeding them in but
yeah what if you have like a thousand uh
ten thousand hundred thousand you know
then then you're gonna hit this uh
context limit and it's not going to
perform so well so there are other
endpoints on the model you can call with
larger data sets that I would recommend
looking at one of them is called the
embeddings endpoint and basically what
this does is you can feed it data and
that will generate vectors based off of
this data and then you can send your
prompt against these vectors and it will
tell you like closest match and that
kind of thing so that you can yeah feed
in a ton of data yeah so we do have the
option to choose the model yeah because
the large language models give you
framework and apis to fit a lot of data
terabytes of data and then work over it
so it's not Microsoft invention it's not
like this integration it's just apis are
there which you can consume to build
more complex scenarios yeah so so when
you get your Azure open AI access
um you you basically pick which model
you would like to deploy
um so you can deploy like The DaVinci
model we're using here or you could go
ahead and go for the turbo model which
is uh more suited for like charts based
interactions or even gpc4 which has a
much larger like input
with the number of tokens you can put in
another kind of interesting question so
you hear the GTP 3 3.5 4 5 6 tomorrow
the higher number doesn't mean it's
better it's mean it's different it's
very unintuitive but one time the higher
number it means it's different but not
necessarily better so if you'll take a
prompt like we just built with marketing
description and send against model let's
say 3.5 to get some response back if you
use the same prompt against 4.0 model we
can get completely different results
back and then we need to work with that
structure so they're very very different
so all prompt engineering are very
targeted per model and model usually
mean computed price response time so
just wanted to know number necessarily
mean better it just means different
usually better but it's just very
difficult I would recommend when you're
like experimenting with like which model
to use and stuff
um start with the latest and then when
you're happy with the results there you
can go go ahead and look at the earlier
models and you know the token cost might
be lower then as well so you can get
some cost savings that way
train them all or everything what we
sent to the model will automatically use
to train it yes so with the the Azure
open AI with the completions endpoint uh
that one is uh
um not using the data for retraining
it's purely in that single request using
that to kind of exceed the model and
that will then produce the result
um there are means to like fine-tune the
models but they're like way more
expensive and uh like I wouldn't
recommend going down that path I would
recommend uh seeing like if you can get
your whole problem in the prompt and
then getting the value out because uh
yeah that's the cheapest way to do it
there's no way from for example to train
the model
so yeah you can there's a like a
different deployment which is a
fine-tuned model and then you need to
pay for that compute time and stuff to
uh to retrain it so you have Azure
capabilities but we don't expose any
integration to do it for now yeah yeah I
wouldn't recommend going that way we
have 50 seconds left before next session
and we need to change laptops a bit so
if you have more questions about openai
find us in a Microsoft boot I thank you
for your time and we'll just switch to
another topic
cool thanks
