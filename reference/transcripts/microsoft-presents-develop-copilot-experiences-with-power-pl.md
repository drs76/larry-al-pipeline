# Microsoft Presents: Develop Copilot experiences with Power Platform

- **Source:** https://www.youtube.com/watch?v=mbSqPHIr2vY
- **Video ID:** mbSqPHIr2vY
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 44m40s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

all right um thank you for being with us
today Monica did amazing job to keep us
away this morning let's give you a break
so I can speak and she can prepare your
next demo uh we did some
polls how many of you really try to use
kopal Studio before just show me your
hands okay so a little bit not all of
you and by the way if you never heard
about copal Studio it's awesome it
didn't really exist like this brand on
naming six months ago and if you look
what it can do Now versus 6 months ago
is like night and day uh so we'll we'll
look on on it
today if you if you ask sa Adela or you
know watch Microsoft build executive
technical Keynotes about copilot Aon
will tell you Coop studio is a tool for
a job to bring your data from different
sources and yourp product like BC two
calot experiences so it's part of a
Power Platform a family of pro products
but for Microsoft it has a kind of value
Beyond kind of beyond
that the way how Microsoft belief or
position Capal Studio it's one place
when you can enrich your data to bring
your data to conversational experiences
across all copilot work we do in
Microsoft if it's in the office if it's
business applications uh and so on so
forth so again it kind of goes beyond
business Central to some extent and
we'll try to show you today how we can
be part um of this journey with tools
and products we
have it's interesting that we don't
really talk about licenses on a
developer tracks but you all take a
selfie or screenshot of this so yes
kopal stud is a product uh they have a
special how should we say pricing schema
because there's a lot of AI consumption
power behind the scene
and the good news it's not that really
expensive if you really really really
look deeper uh you pay for amount of
consumptions your boat will bring you
once you build them so it's more like a
you can build tools as a c as a
developer as a Creator but once it's
using life then there is uh some charges
to pay and actually it's really really
easy to get started uh Microsoft built
like a number of very easy entry
websites you can go ahead and experience
things and that's exactly what we're
going to show you right now so we'll
start with a very like a brief
introduction how to use the studio and
very maybe like a you primitive example
what can be built in a couple of clicks
and this go back to
Monica thank
yougi um asgi said kopilot Studio can be
used to create um a a chat assistance
and I'm going to show you how easy it is
to get
started um of course you can go ahead
and buy the trial life license uh just
to get started but even before trial
license you can just try a demo and I'll
show you how it looks
like so if you search copilot studio uh
you will end up in
the this experience and you can click
try a demo and then you'll end up here
here what it is asking you is a website
where the co-pilot can train itself to
give answers in the sh
experience let me just uh
try learn.
microsoft.com
and let's see start chat ask me to agree
the terms and I
agree and here we already have a chat
bot that is trained on this website or
not trained but it's going to find info
on this website and and uh help me with
this so okay let's
see what can it say how can I post an
invoice
in business
Central learn. microsoft.com is
basically the documentation website and
it has documents for entire micro
documentation for entire Microsoft
products so let's see if this works
came with an
answer let's see it says choose the
icon it meant the search icon uh click
sales invoice enter customer's name fill
in the details fill in the lines so far
so good right how simple is it like I
literally added a line and that's it's
done of course that's not the real
scenario uh you need to do a lot to
create Bots and we'll show you uh later
why this is needed but I want to show
you an example that ifg usually really
likes uh which is let's
ask how
to revert a credit
memo this was also one of the poll
questions let's
see and some of you replied no it cannot
be possible but some of you said I know
different ways to do it in V business
Central uh first of all it realized I'm
still talking about business Central
that's
good
uh but then it says go to posted sales
invoice and then select the posted sales
credit
memo and then choose the cancel action
there's no such thing it's hallucinating
it's
creating
uh generative text based on the input it
thinks it can help best with and that's
why you need to do do more than just uh
providing website you need to make sure
that you get the give them the right
give the right instructions the right
prompts to limit and get the best
experience for the
user that was the demo but it was easy
to try it out right so yeah so maybe
just to clarify so Monica just show you
how you can get started build your Bot
but she also show you case where bot is
hallucinating meaning it give you like a
false data we don't want to say the tool
doesn't work we just want to highlight
that the tools and Technology uh still
have their gaps and we are very open
about that and it's very easy to see it
with small demos like that but if you
kind of put your data from your
documentation from your product you
probably get a pretty significant
results and Microsoft don't ship
actually any tools which doesn't have
enough level of accuracy if you show you
if you'll just we just show you a case
that doesn't work but we kind of saying
that in 90% plus of the every kind of II
work Microsoft does the feature will
work exactly as it intend to be which is
kind of yes pretty significant
number
okay okay
um exactly what if geni said it is a
very powerful
product uh and why so
because first of all you can not only
build your own custom co-pilot to solve
so many
scenarios all the ideas that you have
always had but you can also extend the
first party co-pilots that come default
with co-pilot studio and these co-pilots
can be Office co-pilots Microsoft 365
co-pilots these could be dynamic
co-pilots we go to other Microsoft
co-pilots you can just build on top of
them co-pilot studio is also very
powerful because it provides integration
options with all latest Azure AI
Technologies including broad framework
bot Services Azure AI Studio AI Builder
that you saw some of them in power
automate and Power Platform
connectors so it's very very very
powerful okay but now we are going to
talk about how you can go ahead and
build your own
copilot and
um these are pretty much the steps that
we have summarized so you start with the
intuitive web interface that copilot
Studio has where you provide knowledge
sources like I did for learn.
microsoft.com but you also provide
different knowledge different other
knowledge sources and you just the the
web interface is so intuitive enough
that you can get started
easily but not only that you also have
the generative AI capabilities as shown
in the previous slide so you can use
co-pilots generative answers and Customs
by providing them the data so it
generates answers based on the data you
provided you can create specific topics
topics are basically a concept in
co-pilot Studio where you decide uh on
certain entities uh and you define the
steps in a topic and then that the
combination of topics will actually how
your copilot studio will act
on not only that you can bring data to
copilot Studio using the actions and
plugins that you also saw in the
connector for power power automate we
can also use the same connector c s in
um copilot Studio including the business
Central
One finally when you have decided the
topics when you have used the generative
AI capabilities when you have used the
web interface and actions and plugins
you can just go ahead and publish this
Co pallot and the publish is supported
on multiple channels including teams web
and so
on but once you built it and published
it your users have started using the bot
it could be a bought for uh handling the
uh services or it could be a bought for
improving the employee
process um you can also track who is
using what uh in terms of monitoring and
improving your product and last but not
the least uh you can
use conversational experiences with
Azure AI services with together with
calot so this is very pretty much the
steps
but let's see the demo if gen is going
to show uh an experience with time
registration co- pallot
studio all right I'm going to show you a
scenario from a user perspective you
know I can show you what you can build
how it works and then we'll see what's
happening behind the scene so I'm a
normal user in your organization you
know people who really do a real work
and I work in the tools and products I
love like Microsoft office for
example how many of you use Loop of
seeing that product which Microsoft has
as a part of office suite so basically I
have like a one note I can take my you
know uh notes and actually that's what I
do so I'm working on a project and every
week when I'm done with the work I need
to report my hours so this week or last
week it was awesome I get some work down
in my desk decks I build some content I
get a representation and now I need to
report type spent on those activities
and I never do it it's boring it's long
we never popon until last minute and so
on so forth so let's see and and just to
summarize what has happened so you know
last week I spent some hours on Project
a on Project B on Monday next day and
then on Wednesday I was off and the
remaining of the week of the week sorry
so this kind of summarize in a couple of
words what has really happened now
I've been
told yeah so here is my my data so I've
been told from my colleagues that
instead of using some old apps we have a
better way to report a time and when I
working in teams where I spend majority
of my time we have a new bot created for
that so I can go ahead and you know find
this bot say hey so kind of B is usually
have a conversational experience and can
ask me how I'm doing I'm doing amazing
and how can I help
how can I help is a great question
because it provote an action in my case
when I say I want
to
register time I guess or project hours
say sure I can help you with that so now
instead of maybe fill out some forums or
Excel files which I could by the way or
go to BC and fill out Journal lines
which I could I can just go ahead maybe
you know describe in a natural language
what I've been doing and see if that
will be sufficient enough so in this
case in natur in natural language I just
say hey that's what has been done and
then what's happening back basically
part this information process it maybe
contact to other system verify uh
present data back maybe I can reconfirm
and this case saying hey so you spend
your time on Monday Tuesday doing this
and that categorized in hours by
different activities and if I'm fine
with that which by the way I am I just
say confirm and I will go ahead storage
data in business Central my job is done
and I can continue with doing wherever I
want to so in that scenario as a user I
absolutely careless if there's a BC
behind the scene if there's a new
process introduced I can go ahead in a
product I love without switching context
get things done and move on with my day
where else those activities are so
that's like a scenario bringing Bots
where people are working and in this
case I use teams but I could use
different channels for doing that you
know maybe I have a
uh just to show you quickly maybe I have
an internal web portal so I'm not in
teams but I can go ahead and do the same
you know in a different interface so to
speak but behind the scene is it's the
same bot or the same co-pilot who Powers
those
interactions all right so let's go ahead
and see how we build that and actually
how easy is build experiences like
that um we'll start with a compil studio
so if you go to to compilot Studio I
just press home for
now you see we have a couple of compilot
created so this one we created for this
demo and you should basically go ahead
press a new button and that bot has a
number of topics I really want to you
know walk you through a couple Basics so
you can see what's happening behind the
scene so we have a topics and if I
can use Monica's laptop
never mind
so that'll make sense as a part of
definition of Bot you can define a
logical flow what should happen exactly
the same how would you create automation
so in this case we have we have a flow
which will start to reacting if the user
will ask something about register time
or reporting hours so we'll say if users
ask for reporting hours and then you can
Define like a flow step by step what
should happen in this case both will
follow up saying hey yes I can help
please describe what do you need to
report user will reply back and at some
point we'll come to this magical moment
where we have something called an action
so here's the place and I
can maybe I can zoom it for a gentleman
on the first row to take a better view
but there is the place you can say what
should happen with the data which the
user just provided and in this case for
now it will basically call a pate flow
with a input
and that's where the magic will happen
for this demo so B will take your input
and delegate it to par automate and now
we are in a very familiar territory
where we can enrich that interaction
with a GTP action and do whatever we
really want so here's a flow which um
bot just
called actually super basic it's
basically saying it's a new Trigger or
action that you know flow will call from
copilot and then we have an action where
we'll take an input from the user and we
decide what to do with that so in this
case let me show you what we have we
buil a prompt of course and that prompt
have a structure like a very basic
instructions uh you're a helper which
try to register a Time the employee will
report an hour try to describe it please
process this input in a given structure
and summarize it and so on so forth and
you can always test those prompts so
here is a like a test data I put in and
you can go ahead and test how would you
prom work in this case you're basically
saying given this instruction and this
input show me the result and this is how
both will respond because we said please
return back a table obviously in a
normal real world you'll
say uh in Json if you want to you know
build build more advanced Integrations
maybe it'll be even your default choice
for basic instructions like
that if we have a
capacity we do we do we do yeah so and
and you can also say maybe
that uh in this case we said each work
day consist of eight hours and you can
say maybe when I say
report what can you say you can do
whatever you want actually so basically
you have a playground where you define
your prompts you explain your
instructions which work against user
input and then basically you can p push
this data to the next steps can I change
the model or more settings on how the
GPT should act yeah the reason why we
had to wait a bit couple of seconds
because for this demo we use gtp4 and
gtp4 that like an extra second or two to
be called at least in our environment
but if you default to 3.5 it's just
significantly faster it just that one is
not better but different for this demo
that's really yes you can go ahead and
do that and this is by the way new we
very R we very recently exposed for you
awareness about models uh which you can
use to write your prompts back to your
pricing question because based on the
model it will it will cost you less or
more depends uh which one you
use all right so far so good so back to
compal Studio what you just seen that
there was initial step from the user we
take an input we reach out to aure open
AI we parse the natural language create
some structured response and from here
you can go ahead and build next what
should happen in this case you gave you
some adaptive card to the user does he
or she want to confirm an action and
then you can go ahead and build more
action and we haven't add you but you
can go ahead and add integration to
business Central bring our connector and
just send this data back to business
Central with your custom apis and Report
those
hours like really really straightforward
way to get from a natural interface
capture data understand and store back
to the business
Central
yes does it
work yeah one more time so we see is a
tool which allow you to bring kots en
reach with data it takes them from ation
to deployment to different different
places if
you buy some
chance let's see if our animation
Works actually not
really six months ago or so we announced
a public review for power Pages
integration with business Central so you
can go ahead and build
external portals to expose your data
from BC and if you choose to use this
technology you can also bring Bots to
your websites it just work out of the
box if you continue to invest in power
apps integration you can also bring the
same bot to those apps which just kind
of extra clicks so it doesn't really uh
take you much maybe we should show it
again I forgot to mention that but if
you go to capalot
Studio in a place when you create your
book
you can also Define something called
channels meaning what are the places
where you want to go ahead and publish
that bot so in this case the bot We
Built For This demo uh we show you how
it work in teams but again you can bring
it to multiple multiple channels and you
can easily imagine the integration the
same experiences if you're in telegram
if you're in your custom websites and so
on so forth and this list of channels or
places where you can bring your Bots uh
will grow next 6 12 months within like
work we do as a Microsoft and so on so
forth so again you build B and you can
distribute to as many places as you
would
want all right mon will take over and
tell us about more ways to bring data to
goal studia from essal thank you geny as
you already mentioned and showed one way
which is using power automate flows with
business Central connector you saw the
flow that brings the data to copet
studio uh that's not the only one he
also mentioned plugins which is
basically actions from our connector
it's the same connector that we have for
power
automate and last but not the least
definitely you can bring data from data
verse to co-pilot Studio this is in
preview um and uh it right now supports
native data uh Native tables in the data
ver environment uh and in future it will
also support virtual tables hopefully
okay let's see the demo for bringing
data vers data as knowledge source for
uh chat
thank
you
okay here I have a very very
simple uh
co-pilot where I have created a name and
a
description but then I went
ahead and added Knowledge from data
verse this is the new thing that's in
preview
and I
said uh I look for all the tables and
then I could search for let's say
contacts found the
table um and then we click
next then it shows the preview of the
data that is already
there and then if I click next it
actually takes that data uh in the
source and I have already done this so
you could see that there is the contact
knowledge and um I haven't created any
topics like if Genny did all I did is to
add data verse as the knowledge
Source that's actually not true I did
one more thing I went to the
settings and I
said
enable the uh resp response for
generative
AI so what does that
mean that means now I'm asking the
co-pilot to use this data source
knowledge uh and create responses for me
you kind of saw something similar in the
first demo where it used the data source
from the learn. microsoft.com but now
it's data from data
was but where do this business Central
come into picture um it does
because we we went
to sorry I can just go ahead to business
Central because we went to business
Central and enabled the data ver sync
which is a feature that enables to sync
certain data from business Central to
data
hour and let's see if I have done that
yes so we have a setup
guide that is run and I went ahead and
enabled this uh data ver
sync um and I chose my environment so we
can choose this
one and provide the information and sign
in and so
on since this is already set up it
should be fine the data has been
synced and let's see how it works in
Real uh chat
experience
okay um actually I would like to go to
teams let's do that
and here I have my new co-pilot called
BC data vers co-pilot and let's see how
it looks like so if I say hi it h every
co-pilot comes with some built-in topics
since I haven't created any topics it
still uh can realize what to say on
greetings and how to end the
conversation and things likeed these
topics are called system topics that
comes by default with co-pilot you can
choose not to use them or you can choose
to edit them as you like all I have done
in micop Pilot is added a data ver
knowledge so let's see okay uh micop
pilot knows about context let's ask
something about context so how
many contexts are there in let's say
us now it's going to
search through its knowledge
source and try to find out how many
contexts are
there it's a bit
slow while it does that I would like to
show
you how many contacts we actually have
okay it came back and said 10 contacts
uh in the US and it also said that it
got this information from my data
environment uh but let's verify if we
have really 10
contacts H and I have all the contacts
here we have 23 in total and there are
10 from uh us so it came with the data
this is very powerful because with this
now you can actually do data Q&A uh in
one way so you can ask questions about
your
data that was the
demo over to you if
gen no no no you want to comment on I
want to comment on that that's true uh
that's true um so how did it do it I
just want to say that behind the scenes
it used generative answers based on the
knowledge and that's possible because
there is this feature
uh which allows copilot Studio to use
the generative AI
capability um yes that's uh that's also
something I want to talk about which is
when you're going to develop co-pilots
using co-pilot Studio there're going to
be multiple things um that you will try
and I want to recommend some best
practices from our learning
experiences first and foremost topics
topics are the key of the co-pilot
Studio you that's where you decide how
the co-pilot should act depending on
users's input or what whatever happened
last um and I would suggest to First
make sure that your topics are organized
clearly in a logical way so there must
be one topic for Greetings one for
ending the flow one for connecting to
the live agent and so on uh one for
actually in this case registering time
or whatever the core process you are
wanted them to do uh but but also scale
organize your topics in terms of scaling
cuz they they're going to grow you want
your co-pilot to do more so you want to
logically organize your topics with
scaling in
mind yes then we have entities and Slot
filling you need to identify the
entities that your co-pilot needs to
extract from user input so you your
co-pilot should be able to fetch all the
information that it needs from the user
before doing the next step and that is
pretty much it this technique is also
called slot filling where it's basically
an AI technique where you fill the slots
to get all the user input before uh you
do your next step as a
co-pilot trigger
phrases every topic mostly starts with a
trigger and it has some Trigg trigger
phrases which
says when Hello is said what should you
do or when register time is said what
should you do you need to make sure that
you create concise and intuitive trigger
faces because same thing can be said in
multiple ways so add as many trigger
faces as you can but also test with
different users uh different users with
different language
skills Authentication something that we
didn't show uh yet uh is authentication
mechanism and want to make sure that you
make sure that your
co-pilot has the right authentication
mechanisms you could use the default
authentications for team uh an
office but you could also configure your
own uh a app and authenticate against it
for more channels and more
scenarios and last but not the least
always measure meure the usage of your
co-pilot and provide feedback loops when
a co-pilot is generating a result make
sure it also ask for feedback from the
user do you like the result can it be
improved I'll I'll stay on this slide
for a minute because it's important and
I see a lot of people are taking
pictures who those are the best
practices gy give us the key key
takeaway
so if you're still wondering why we kind
of spend your time talking about this
topic today it's kind a b day conference
the answer is we start seeing request
from our customers from BC customers hey
you know we pay attention to it copilot
development we with Microsoft we have
Microsoft copilot who being office how
can BC data be part of that story and if
you have question like that here's the
answer copal tool is the best tool
Microsoft have so far in order to enrich
the Capal experience with the data from
business Central uh it's a tool which
has a significant Investments over last
6 months 12 months and probably next uh
futuree from develop from development
point of view as long as you expose your
data from a custom API an extension
you're good to go and then it's really
really easy to integrate to some of
those surfaces and deploy your Bots at
in different across different channels
so our call to actions go ahead try it
out it's free to start it's actually
every demo we show you today should be
able to go ahead and do half an hour
yourself like it's absolutely no magic
it's it's more like a it's really easy
to get
started and team put some love and craft
in that studio to make it intuitive and
easy to get started by the way as always
we have places to go if you don't know
how to reach out us and with that we
have like 7 minutes for Q&A for a first
session for a second session so let's
have the discussion
now remember the
t-shirts yes when need to oh you can
show on a second I'll
try here you go oh it worked hi um I
want to ask you if it's possible to use
copilot with virtual
tables no no not yet not so far then for
the custom uh data uh we we need to use
the some other uh way to pass the
information from the yes so you have the
plugins uh let me can you refr the
question maybe first uh yes I would like
to rephrase the question uh which is um
he's asking whether it's possible to use
Virtual tables of data vers with copilot
and the answer is not yet then it's
saying how do I bring my custom data to
copilot studio and I'm going to quickly
show you that one
way so let me just uh go to an existing
okay where am I let's say Studio
home but and I want to show you it's the
same experience that we have in power
automate you can also have in uh copilot
Studio using actions and
plugins so I'll just go ahead um and uh
use the CH time chat Co pilot to just
show
quickly so I'll go to this
topic and let me just uh
um show you let's say I want to bring
data from business Central using uh
addin then I can say call an
action and here I
have um connectors same that you have
seen in power
automate and you can have business
Central
here uh and then through custom apis
same as in power automate you can bring
the data so it works same it wants the
connection and then specifies which apis
you expose your custom data through apis
those apis will be available here and so
on and for rual tables it's not
available right now because it just
created like two months ago but they
will enable capability shortly okay
another another question another
question sorry another question sorry
let's hold
on we can take this uh after
yes yes uh so you showed that uh you can
train on website copilot right yes uh on
what language should that website be is
it multi language another good question
of let me remember to give t-shirts away
so one for you top three gets it or how
many we
have uh would you help thank you Swit
it's a very good question
um by default Ault it supports English
as you saw but there's a way to do
multiple languages in co-pilot Studio
are we sharing the right screen yes uh
let me show you
quickly so if you go to the co-pilot and
go to settings there is this languages
here and you can add more
languages wait for it that's not there
but then you also get to
say um the resource file that you want
to add for your translations for the
strings that you have in co-pilot you
can also add this in this so answer for
the question is yes it can support
multiple languages uh does this mean
that if you train on English uh the
users can uh also ask questions in a
different language than that you trained
on
um that is a good question I haven't
tried it but I don't think so it will
work on you have to train it on all the
languages
that you want your users to be
supported right if
gu kind of kind
of so a quick comment about languages
and open AI Integrations if you're just
curious if you go to open AI website not
Azure but open a website they will say
the only supported language is English
period if you would look what Microsoft
did six 12 months ago all our
integration built in English and maybe
like select a set of languages French
Spanish but right now we enable
Integrations almost across all languages
across all our portfolio like even BC
features since 24.2 this update all of
mive experiences they're available in
all languages so gradually language
Bearer get expanded more and more and
more because technology works better or
maybe there is more trust so to speak so
you can see I hope you need you don't
need to answer the question like in a
six months from now it will just kind of
works out of
box uh there was one more hand I saw
somewhere
this thank you
yeah um I'm just wondering about the
limitation using uh let's say the the
syn from business you might want to
sorry hold the mic yeah this way I think
it works yes okay so I can now I'm
wondering by the limitation when using
the syn between business Central and and
uh and and the power apps uh I would
like to have your advice on uh what
would be the best is it virtual entities
or data verse and we need to take into
consideration when syncing the data back
to business Central uh we would like to
use events like posting the journals and
so forth so I'm wondering what what's
your advice using the virtual tables for
for the power apps or using the data
verse should I take this yeah go ahead
maybe want to rephrase a question we
synchronize it's a very good question
again uh which is uh the question
is what should be the practice to uh
bring data to data was uh whether it
should be through virtual tables
whether um uh we should use the data
sync the feature that I showed or uh
whether it could be through events uh
back and forth and bringing back data to
BC um the answer is it depends and and
it depends on the scenarios data sync is
a uh a powerful but a very
limited um scenario or feature in the
sense that out of the box it only
supports things for a very limited
number of uh entities in business
Central both ways
virtual tables on the other hand uh
exposes more uh entities out of the box
so it's easier
um to do uh basically sync on that so I
personally would start with virtual
tables if you don't have anything
already in
data um but there are also multiple
other Technologies it could be through
apis and then use combination of
platform tools to bring data to data
verse and that could work for for
example easily for custom entities or
entities that are not out of the box in
Virtual tables and things like that so
it it it really depends on setup but I
would if you haven't done anything start
with virtual
tables yeah it's a super hard question
to be honest and you can say the
Microsoft how hard can it be for you
guys to make sure when I have my sales
and BC it just works how hard can it be
and apparently it's really really really
really hard really hard so it's a every
release we try to improve integration
all fronts you have more out of box
entity to think with different products
every release we try to build better
integration but it it really depends
like we have we give you three four
different ways and sometimes it's up to
you to choose what you use like in a
toolbox unfortunately yeah we should
probably do much better job but for now
this how it
is okay we have 19 seconds maybe we can
take your question if you still have
one wait
I'm I have another question about the
permissions with the copilot studio uh
when you are asking to compilot the
studio uh you are connected with the
database data or business Central data
what about the permissions if you don't
have permission for see the
information uh for see this table or to
use this table in databar what happen it
it it would not return you data yeah
yeah and make sure your BS are using
authentication so in this scenario we
were not using the authentication we
never logged in as some user but you
have to set up your Bots with
authentication with the right user and
then using that user's token it
determines what kind of permissions and
then it works same as like you logged in
in data vers yeah so it will return you
if you put the the the boat in a website
it's open for all the people sorry you
put the the the the compilot in the bot
in in one website upsite of the company
yeah and then the you are using the the
copilot for open for the all the people
it's not uh you don't have a specific
permission for something yeah and then
you choose to do that to set up your B
like that okay you
shouldn't cool okay we are time up thank
you so much for um for the session
thanks so much
