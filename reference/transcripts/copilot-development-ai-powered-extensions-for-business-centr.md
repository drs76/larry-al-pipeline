# Copilot Development: AI-Powered Extensions for Business Central

- **Source:** https://www.youtube.com/watch?v=HgSytz-yOmY
- **Video ID:** HgSytz-yOmY
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 92m15s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

[Music]
welcome everyone to anwp to bch days um
hope you had a good breakfast after the
keynote um I'm very pleased to be here
together with uh
horina and we prepared some uh good
stuff for you uh when we actually uh had
a conversation uh before the conference
how should we split our roles we decided
that Hina um will do some boring Theory
stuff and I will do some amazing stuff
so um uh let's let's do our job really
great and and you know the whole trick
is that I will take the boring part and
make that an awesome
presentation right so um today's agenda
uh we will uh talk about where we are in
the AI field in the business
Central uh then we will talk about
copilot
toolkit then there will be some cool
demos then there will be more cool
demos uh one last cool demo not really
this will be the last schol demo then we
will talk about Community ideas that we
gathered uh before the
conference and we will finish with the
what's coming next and with a
Q&A so my name is Dmitri catson I'm
MVP uh in about 20 years in a business
Central and a central Q AI Creator uh
website probably you use that
andina my name is Hina I am group
engineering manager in business Central
and uh together with my aan team which
many of them are here uh we have
developed U many of the AI features uh
in business Central
today yeah so let's start um so uh let's
briefly um recap uh AI features um when
they repeat in the business Central and
it first appeared in
2016 with a sales and inventory forecast
so
Vincent um told you today uh about these
circles uh so this was not a LM feature
this was a regression uh
model then 2 years after we got late
payment
prediction uh and this was a
classificational
model that actually answered on the
questions like yes or no what will the
customer pay late or not and then then
there was a 5 years break and in Spring
2023 we got marketing text suggestion
and it was the first large language
model uh feature that appeared in a
business Central then half year later we
got a bank reconciliation and suggest
Jill accounts and aop pilot toolkit and
then in Spring this year we got many
more uh copilot Tool uh features and
they all work under the large language
models uh
umbrella and today we'll talk about
copilot toolkit mhm all right yeah thank
you Karina please do it um first I just
want to say to The Tech Guys that uh
somehow the clicker doesn't work but uh
if you can figure out while we continue
presentation um so let's talk about the
developer tools for co-pilot uh let's
and um you know my thoughts was to start
uh with uh maybe the history behind it
what was uh you know our thoughts here
in Microsoft about the developer tools
for co-pilot so when we started uh our
generative AI Journey uh in business
Central we kind of realized very quickly
two things and one of them was that
generative AI development is so much
different different than the traditional
feature development that uh that that we
know and we used to is it so far right
um and you will see actually during this
presentation why why is that uh the
other part was that uh you know
responsible AI has become so much more
important with generative Ai and it's
not because we didn't have that in
Microsoft as concept and it doesn't
exist as a concept but just uh gener
generative has this extra Dimension to
it uh that makes it really crucial in
how we design our AI experiences uh in
in in your Solutions and in business
Central and so to some extent the
developer tools is the summary of all
our learnings and uh and and uh gu uh
guiding and all the user research we
have done uh so far to uh get to life
our our features in business Central um
and then we thought of course you know
if we have been through you know all
this you know new discovery and
learnings and and we wanted to bring it
to life also for you uh as developers to
scale the co-pilot features um to all
across all Industries right um so that's
how we come up with the idea and it
truly is uh um everything we have
learned and we want wanted to share with
you and make sure that uh you get that
for free and uh um you know get to
Market quicker than uh than you would
have done without this toolkit it works
now and what are the uh uh parts of the
toolkit well there is the signature
co-pilot UI which you actually have seen
in the keynote I've seen from dialogue
page and uh and co-pilot actions then
there is the uh AI module um which is
part of our system application uh uh and
uh it truly is the bits behind the
scenes that uh connect this beautiful UI
to the powerful large large language
model then we have guides and samples
and then there is also a common set of
functions that you can use for uh
registering the capabilities uh in AI
for example in business Central also uh
Telemetry tracking usage and and so
forth but you know what should we use
copilot
toolkit so I think that um also
important to understand that uh without
copilot toolkit it was also possible to
build some kind of uh AI features right
uh the compiler toolkit just made it
very easy to build because we should
focus on the feature itself not about
how to communicate with the Asia open AI
what UI should we use so it's um we can
very quickly go and use it mhm and and
also there is the cons when it comes to
the uh signature UI right there is the
consistency uh of of the AI experience
and it's not only consistency uh you
know you know your solution being
consistent with Microsoft in terms of uh
user experience but it is uh also
consistency amongst all your features
that you're you're going to build in
your solution um and then again there is
uh there is the responsible AI uh which
is the uh driving force of uh actually
many of the decisions we have uh done in
in promt dialog uh page today um yeah
and then as you said maybe less let's go
to right right
yeah so uh what is the toolkit is very
good we specify uh right now from the
beginning uh what is the uh toolkit
intended for um it's uh intended for
business Central online Solutions um
it's uh it's not you won't be able to
use it on on your on Prem
deployments well except uh when you're
trying it out right on but I can use it
in Docker right yes thank you uh then
there is the um the other part is as you
have seen also you know Vincent in the
keynote he shows all the layers of a was
deep learning machine learning and so on
the toolkit focuses primarily and
entirely on the generative AI uh and the
purpose is to uh basically assist uh
humans with some of the you know complex
tasks um you should bring it to life in
in different business
processes and um the interaction mode
what kind of experience you can uh build
with the toolkit uh that is non-con
conversational uh so what do I mean by
that it it means that for example the uh
chat pain that I have shown uh in the
keynote that is not something you'll be
able to build with the toolkit um what
you will be able to build with the
toolkit is uh integrated business
functionality similar to the SS line
suggestions where the user has a
concrete uh puts in a concrete input and
then llm gives a concrete output uh and
then of course uh a part that is really
important yet again as far as I said I
said that before um is uh uh responsible
a with human in uh in the loop um so all
all the uh AI EXP has to have still keep
the uh human in in reviewing the results
from large language
model so with that we can uh maybe take
uh some time to uh slowly go through the
prom dialog basis Basics now Ida has
shown you an example of how to uh build
you know a project plan and you could
see uh the new Concepts that we have
introduced but let's uh
let's talk a little bit maybe more in
detail about the prom dialogue page type
right so the prom dialog page type is
the um is the core of the the the
signature UI um and um and it it is it
is made such a way that you can uh um
design your interactions is quite a
flexible new page type uh where you will
see that you can both uh uh have the
input and output and on different ways
of interacting with that um and then we
also make make sure that uh as I
mentioned the user is in full
control and this is how it looks in I uh
this is a a glimpse right this is very
simple um again the whole point with the
toolkit was that uh it's supposed to be
simple easy to use um the new page type
is there from dialogue and um another
maybe very important thing to to know
about the prom dialog page is that that
is not extensible so that means you know
if I uh create a prom dialogue and then
you know Dimitri wants to extend it or
remove all the uh uh responsible guards
I have in there he won't be able to do
that I can add to that uh why why it's
not expens extensible uh because
um when you deal with a AI it's still
like a stat statistical models and every
time you ask a question even with the
same same question with the same
instructions you can get uh
statistically different uh outputs so
um when you want to debug your co-pilot
uh you should be pretty sure that uh you
are debugging something that you are
responsible for so something that you
build so that's why if uh like you build
some kind of instructions and somebody
else extended it it's like I would say
nowadays it's not possible to debug it
and understand
um who who is responsible for the
mistake or wrong scenario
mhm all right uh and then we have uh the
uh three modes of the prom dialogue um
so these These are somehow the concepts
that uh that we have uh introduced in in
this page so the first part is um you
know how do we construct The Prompt and
how do we give the instruction and
context to the large language model um
and that can be you know the input can
be anything it could be free text like
you have seen in some of the example you
go and type your wishes uh in that uh uh
prompt then uh or or you can have like a
structured input you know you can have
uh like here uh item attributes we have
used that in the marketing text that is
a um uh all the uh The Columns and data
um and then you can also have a
combination you can have um you know
also free uh free text and also some
structured uh
input and you could also not have the
input at all because what if for example
all the data you need is uh to pass to
the llm all the context you need is
already in business Central so then you
can uh you can just go directly to the
uh generating mode part and and there uh
the generative mod is where we are going
to call the uh the lar language model
and uh here we also have as as a concept
the uh progress indicator which you will
see later um and uh and then you will be
able to actually adjust a little bit the
text that uh that we showed there and
then there is the U uh
output which also can be you know
structured or not structured so uh in uh
in the marketing text suggestion for
example when you are generating a a
description for for your item that is uh
unstructured basically the llm returns
free text um but you can also have uh
that llm returns adjacent for example
with uh information and then you
transform those the those into the
records in in database uh and again you
can have uh uh the same both
combinations and you can in your designs
you can mix a match you can have uh no
input and structure output or you know
whatever you think that will make the um
experience more compelling and and more
productive for for the for the
customers and uh for the input right uh
that is how it looks uh in in L we have
introduced a brand new area that it's uh
it's called prompt uh and there you can
add um you can add fields for example uh
this uh this image you have there that
is for for uh uh for pre text or you can
also have um page uh page parts or you
can have
controls and um and here is the uh the
generate action that you have seen in uh
in for example in kot in the sales line
suggestion um how did we do that well we
have actually introduced a new uh system
action area uh only specific to PR
dialogue and in there the general at uh
action is actually a platform action U
but you can go ahead and add your
generate with with AI uh
functionality then the progress
indicator uh as as I mention um that is
uh that is um uh the way you actually
change the the text uh in generating I
don't know if you have noticed briefly
when we were uh showing the sales line
suggestions um that you you were kind of
uh updating you in uh where are we in
the in the phase of searching for the
items uh that you will do uh normally
using the progress uh progress dialog
API I can add to this a little bit uh so
uh this is really important from the
user experience because uh uh generation
process could take time if you you if
you build some complex copilot that not
just answers you know the questions but
it requires some uh data retrieval data
processing uh maybe answer post
processing uh user you know he he will
be very boring boring in looking into
this generation uh so you need to update
the user what's really going on inside
MH yes then here we have um an example
of how the outp output can look like and
um again this is uh where the output is
structured and and uh you have for
example uh uh some records that you want
to U Save to the database um uh and then
for this uh for the content area for the
output area we haven't actually uh
created anything special any New Concept
you can just go ahead and add it to uh
to the area content and you can see here
we have uh uh the fields and the parts
yeah one addition to this uh comparing
to other Pages uh in the business
Central in L uh you can't add a repeater
here so it's uh if you want to show some
kind of uh Records or sub page you need
to put it in another page and show it in
into the part as a part as a page part
yes yes and we also have the part as a
as an example here
mhm and uh yes and now we get to um
maybe maybe the most important actions
uh in this page uh that is keep it on
this card um so we have added these um
actions here uh again to uh obey to the
responsible AI uh guidelines and and
what is really maybe important for you
to uh remember uh when you implement
your Solutions is that um uh What
respons uh responsible tells us is that
you have two options uh either you um
generate your content uh you present it
to the user and then the user can review
um if that is uh if that is what uh the
llm uh should reply with and this is
correct and then you go ahead and then
the user can say keep it and that's
great um if for any reason you would
have to uh save the content to to the
database before asking the user uh then
the user has to have the option of
undoing right uh and when we undo then
that comes with a price that you would
have to go ahead and roll back all your
changes that you you have committed so
there should be no trace of uh of any of
your changes um well why is that right
so why why is that well because you know
the way we have thought about it is is a
co-pilot right it's not a you know a
pilot so the human is still in control
and remains in control and and uh it is
also way for uh for building trusts uh
with with the users right because um how
do they know the llm actually has
response correctly and they have no
control over
it and of course how it looks how do you
save the result that is no difference
and how you do it today we all know on
qu close page trigger um and then you
there is a check what has user pressed
okay or
cancel um and um we also actually I have
I don't have a slide on that I think
maybe but you can also let me go back um
you can also rename the actions names
right so it doesn't don't necessarily
need to be keep it or discard actually
we have maybe an example in your slides
um but uh but basically the actions uh
can be you know if you want to say send
mail or undo or just uh just have any
other text in there uh that's up to
you so let's um move on now to the
administration module um that is also
part of the toolkit so so we have
introduced together with the toolkit the
co-pilot and AI capabilities page and
and why have we done that that is
because uh we believe that uh uh
customers should be in charge of their
data and they should be also in charge
of their AI experiences and um and what
you what you will see here is that uh um
the admin user can for example uh get
first and foremost transparency uh in in
terms of like what uh what AI
capabilities we we have installed and
and they are active but also the admin
is in control uh in the sense that you
can go it can uh that they can go and
turn on or off certain AI
capabilities and the toolkit supports
actually you will see apis for
registering this uh these uh AI
capabilities for example how do you do
that uh we have a an an enumeration
called co-pilot capability and then you
go ahead and extend that uh and uh for
example here is a draft draft a
job um after that you can uh also uh go
ahead and uh um register this capability
first you check what what happens if
it's registered or not uh and then we
you call the register capability and
here you pass the um enumeration but
also you specify whether this is uh
General
available or is in in in preview and you
also get uh to specify a link where the
administrator or uh user can see more
information uh about this uh this
capability and one also important thing
to to remember uh when it comes to let
so let's assume you have created your
extension and in there you uh have
capability a and you register that
capability a and and then you have
another extension that wants to you know
extend some functionality in there um
well if you would like that ex a new
extension that to actually be also
registered then you need to call that
specifically so it is not enough to
register it once and then all the other
extensions will will come later will
will uh will be uh registered to the
system and now we get to the actually
the meat of the uh toolkit so let's uh
go quick through through
that what was the the AI module right
you will find it actually in the system
application under the system AI
namespace on on GitHub and um what is it
doing it's uh it's primarily helping you
interact a lot faster with Azure open AI
um we also have capabilities for keeping
you current with the models um as you
also have seen just before the
administrator has specific apis for it
we also have apis for Telemetry and and
so
forth and this is an overview of uh the
objects you will find in the uh system.
a name namespace um what do we have in
there well we have the Azure open AI
code unit and uh you will see later in
theit's examples that um there there are
all the you know interesting functions
of uh of uh of calling the large
language model gen the generat The
Prompt generation methods there is also
the set capability uh and then set
authorization we also have the uh Azure
open AI operational response uh which
which is giving you the full message
back from
llm then you have the model types uh
which can be uh chat completion text
completion or
embeddings uh and then um then we have
um uh the Azure open AI chat messages
that is used for for you to specify your
prompt the user prompt the system
prompts uh and and combining this and
and uh send making this prompt that will
be sending to the llm then there is the
chat completion parameter the I think
the text completion probably will be
deprecated soon um then yeah in the chat
completion parameters you will have a
chance to set the temperature for
example of the model if you want the
model to be uh not creative then you
should use zero um then we have um uh
also said a maximum number of tokens I'm
a little bit confused um before I
remember you talked that uh copilot
toolkit is not for the chat experience
and you have here the chat completions
that is actually so true uh and uh and
that is because you know any com any
call we have with llm is uh is is a
conversation and when when it comes to
the chat that we have implemented that
is multi- turn conversation uh whilst uh
in uh in um in the toolkit it's a single
turn so you have the input and output
yeah so it's like um when we ask
something in the when we type something
in the copilot toolkit uh input that
says the message yeah so and then we
send this message and then Azure opena
generates uh assistant message yeah and
this is the second message yeah ahuh
okay
and then we also have the uh the chat
roles uh which I'm trying to remember I
think is the user assistant the tools
and the
llm so let's uh let's see some examples
about
how you know uh we agreed in different
thing we agreed that you will be very
boring but uh uh for me it's
great so now you know the audience needs
some kick you know and so let's uh uh um
let's do some
demos okay so um let's do some very
first basic demo uh we have a actually
very similar to what we uh had in the uh
morning uh today during the kot um so we
have a projects and I made um some
co-pilots uh so by the way can you let's
let's let's first go to the I think next
slide mhm do
that make
discover no okay I'll do the
demo okay so um I built several
co-pilots uh for today's demo and the
idea is that U uh Luke has uh a 25 years
anniversary to with the mibuso.com so we
want to um make him very happy and um so
he will not do anything um for preparing
for the last next uh business Central
Tech days uh so I built uh different
co-pilots that will help look during the
uh the way of organizing the conference
so um the first one is like okay so
maybe this not for the look maybe here
this for the look as well like the
copilot will help to generate some new
ideas um so maybe it will help Luke to
generate some ideas about the new topics
that he can cover in the bch days so I
want to organize some conference in anwp
suggest me some trendy
topics so I click generate it send my
request back to the asure up and I get
some uh ideas so what's there health and
wellness trends do you think Luke will
love that I think he would love that yes
but first beers
okay uh so there is also some uh budgets
uh and what I can do here I can uh also
refine my uh you know request I can say
that uh okay but uh I want uh it to
be
for so we had how many one 100 so for
for example 1,500 in this
1,234 yeah so when that's should be like
a new budget here so it's um a very
simple copilot experience so let's see
how it uh made of so first so we have a
uh prom dialog page here
the prom dialog page page type prom
dialog uh we have this is a preview that
is a small Mark uh small icon and the
copilot it shows that this is under the
preview and like a uh area of type
prompt that's where the user uh type
let's maybe open this once
again so yeah this is the prompt area
uh where user typee
something and just one field text and
then we have a cont uh content area of
the output so uh actually when I first
uh saw uh the copilot uh toolkit I was a
little bit confused of you know you see
this experience of first one screen then
generation screen and then output screen
it seems like a three different pages
but uh actually this is one page so
actually this uh uh areas Define this
nice uh
rendering and then we have a system
action uh which is called generate and
um we can actually change the caption
here with add a caption and change uh
the name of
the uh and then we have this on action
so that's where the real magic happening
so we go here
and uh we first check that uh our
copilot is uh
registered
um so then we set the copilot
capability we set authorization uh by
the
way with this uh new announcement uh of
shared AI resources this experience uh
could be changed I guess a little bit uh
but for now I'm using my own aure openi
resources
here I'm setting the temperature and
this is the uh real magic uh here so add
a system message and this is our new uh
development language for coding so this
is our just uh plain text where we
describe um how our copilot should
behave so actually uh this is the first
message that we're sending this is the
system message and then this is the
second message the input text that's
what user inputed then we call one
function generate chart
completion we check uh so this function
sends the system message and the user
message so and under one call uh to the
Azure open uh we get the response back
and uh as this is a chat uh history aure
openi generates the third message the
third message is assistant message and
to get the uh result we uh call this get
last message here and that's it we then
just show this to the
user the registration part is that what
Kina showed we created new
inam and we we uh registered our copilot
so this is the install code unit uh
every time we install our app it will go
and try to uh register capability if it
will uh check uh if it's s environments
then if the capability is uh not
registered then it register capability
so pretty straight forward pretty simple
so now um I do have a question question
for
you um how can we put this into the
pages sorry I was just yeah the question
for you yes how should we uh put
compilot uh to the pages so how to how
to show it right how to make it more
discoverable yes how to make it
discoverable yes let's um switch to yes
so um well basically we you have seen
that uh the prom dialogue um is created
as as a as a prom page as a page with
several modes but then you know how many
users are going to discover you know
your cool feature uh and and how do we
tell hey this is a co-pilot feature and
not just any feature and the way we do
that uh well I have also showed in the
sales line suggestion for example demo
that we have the image Sparkle that's
that is a new option for for you to set
the uh image on the
action then there's also another
variation which you haven't seen which
is the uh image the sparkle field uh so
let's imagine you have a menu and in
that menu there are more actions and you
would like the user to you know first
click on that one uh then you you go
ahead and use this uh this um sparkled
field uh option
and then of course there is the uh the
last one which you also have seen in uh
in analysis list and also I show it in
the example uh that is what uh we call
the co-pilot this the co-pilot action we
call it internally Microsoft we call it
not but it's just an internal name uh
and uh and it really is meant to uh draw
the attention uh or to the user that hey
when you are on this page this is you
know uh maybe what's next action for you
um and we actually using for example on
the bank reconciliation page as well uh
and then if you you know think okay this
has become too much can I you know
that's that's what happens sometimes
with uh with some of these you know
visuals user just wanted to you know go
away uh then you have an option to uh
show it uh not in page but show it in
the uh co-pilot uh action menu in the in
the action bar so there's the these two
modes that that you have for for this uh
co-pilot
action and how do we do that uh we have
a new area called prompting uh in in
actions and uh so far the uh co-pilot
actions are supported primarily on list
list Parts worksheets and and start our
dialogues but make sure but we are
actually working on on extending the the
number of page types where this action
is going to be uh available
and uh with that let's uh do more demos
yeah so um so actually that was the
slide that I wanted to show before so
it's uh we will build um today as a
demos different uh
co-pilots um that will help look to
organize the conference so first you saw
to generate some ideas uh then we will
build copilot that will uh create a a
project plan uh uh and then uh the
copilot that will help import uh the
sessions uh to the project uh to the
conference from any Excel file so
actually this copilot I love the most
because you can use it uh in in your
production environments for uh any
scenarios uh then there will be a
copilot that will help look to uh
schedule sessions to put all sessions to
the
agenda uh and there will be event
assistant uh we don't have by the way
here the event assistant uh you know no
when when my uh session will be go to
what room and so on so that we will
build today and the last uh thing we
will also uh Power this assistant with a
semantic
search so that was the ideas copilot uh
that was what I'm supposed to yeah so um
the compilot which show um there are
some new things uh appeared in the wave
one yeah yeah yeah so um we have also
seen it before but let's also draw your
attention on it so part of the learnings
we have had at least when the user has
to you know go ahead and type uh in the
prompt window is well what should they
really write and how should that write
it and what if it doesn't work and
should they uh you know how how much
time should they spend uh refining this
these prompts and um and that actually
is not something we can just come up
with is is results from from our user
studies and so we we have introduced uh
the uh instructional text um here you
can uh you can go and specify give some
hints to the user hey here is where you
can add your your items or uh your ideas
for the project plan and and so
forth and well uh it's uh it's actually
a new uh a new option we have for the on
the fields it's called instruction on
your property uh that is called
instructional
text uh and um you can also we can also
talk a little bit about the promt guides
right the prom guide another way for you
to specify um you know what users can
can start with and give them some
inspiration uh for how to interact with
co-pilot and how is that uh looking
Let's uh let's let's see um in Al um
here we have the uh prom guide action
right and then we have also a new area
prompt guide and and in there you go
ahead and Define your action you can
specify the caption and and also the uh
the
triggers and here you have the examples
I just shown uh from the sales invoice
um this kazim you can tell if it's true
or not if we copy the right snippet uh
and that is the copy from order and copy
from
invoice and now let's yeah so this um uh
two things that you showed like a
placeholder and uh prom guides um are
there actually to uh guide user what the
user should type there because when the
user opens something there is a blank
screen uh he know he's usually stuck he
doesn't understand what should he type
there um so let's go to the next Dem
uh and uh this is my uh project and
let's do plan the conference so um I
have some kind of um prompt guide here
like organize
conference so already uh promt guide
helped me at least to start with
something so organize a
BC Tech days
in
anwp so it's um now doing some
magic and this is
the plan for Luke um how to organize uh
the B days for the next year so it's
like you need to select the venue
probably it will be easiest one um then
invite speakers uh create an agenda and
so on I'm but I'm still not very
satisfied I think I'm missing one one
thing
here don't forget
about beer
party
yeah by the way uh there was a fun thing
with that uh we uh experimented this
yeah now we have a beer party uh there
was a nice thing with that um there is
some uh safety uh guard guard um guards
uh that when you sent your prompts to
the Asia Rini uh the Microsoft also
applies some safety uh instructions and
um uh when we tested this uh before we
asked about the beer party and uh a
actually denied to answer on this
question we actually investigate the
issue it was because of the party but
then we uh rephrased the question that
hey we wanton the evening party and it
was totally fine so like no parties in
the morning
yeah uh now I'm happy with this project
plan and I can keep it when I click keep
it it creates a project in the business
Central uh so that's how easy it is so
we have now a project with the
tasks um and then can I ask you have you
been using the temporary table to show
the results um yes sure okay very good
never use not temporary tables there
okay cool
uh let's see how we uh build this kind
of uh co-pilot
so I will not go to the prom dialog
because it's more or less the same it's
more interesting in the you know uh
implementation uh as well
so the generation part is the start of
this is pretty the same uh you know this
is the template we add a system message
we add then a user message we generate
completion uh we get the result and then
we
um actually do some kind of
postprocessing of this
result uh however I have a question for
you
so just think about it for a moment when
you deal with a Azure openi your input
is a text and Azure openi answers you
with a text so now we um receive a text
here yeah so this is a response text
this is a text variable so how do we
transform this to records yeah how can
we transform text to the
records
just 10 seconds for you to to think and
for you to prepare the demo no so the uh
answer is that if we look into the
system
message so this is more uh comprehensive
but this is
the uh ISS this is this is the thing how
we do this we ask uh Azure openi to uh
output in a structured format so in this
case we ask to reply in a XML format or
we can ask to reply in a Json uh format
or uh asil or whatever it's good in Json
but we can do this in a XML as well so
then we
um so this is how we structure structure
the system prompt first we describe the
task um so we describe what copilot
should do then we describe the output uh
then we describe the uh format of the
output maybe some additional um comments
how compilot should generate this task
so let's say we say that we uh generate
at least six tasks here
and uh so on so that's important thing
to understand
um asure openi when when we send
something to the aure op aure op doesn't
know anything about us it doesn't know
anything about business Central about
the context uh where we working on about
our co-pilot about the data that we have
in the business Central and so it's
blank for them it also doesn't have any
memory so every time you send uh request
you need to send instructions and
request every time so that's important
to
understand so now we uh have this uh
system prompt and
uh then we when we got where is it yeah
so we get this uh response text um also
some sometimes
uh asure openi respond us so we ask XML
uh but um he can Al it he it can reply
with a like XML XML yeah so it's or
maybe this is your
XML uh so we don't need this so we we
can actually do some kind of post
processing to delete uh some
um
these characters that we don't need and
then we take this response text and this
is uh just normal you know XML parsing I
use an XML buffer and then we insert
that to the uh temporary table here so
it's uh nothing very uh AI related so
this is our Al code is uh going on here
yeah so we have now a project plan
good what we can do
next
we ask uh speakers to send a sessions
and uh uh sessions uh they can be in
a different
formats uh so let's build a copilot that
will import our sessions from any uh
Excel files so let's look how
it uh
works so this is our compilot and you
notice that we don't have here the input
screen so this is the input screen but
we don't have a text
input uh because our input will be a
file so we have here attach
action and we have a sessions Excel
let's open
that
so Zoom a little bit so we have a this
Excel file so it has a columns with the
IDS uh session title
summary and so on but we have in um you
know we in a business Central in our
extension uh have
as a new table a sessions table so it
has more or less the same you know
structure because we need to save the
sessions obviously the information is uh
more or less the same but the fields are
different so we have like code we have a
name we have description and we have
here like speaker one speaker two
speaker three and four a date and status
and some other fields like
duration so the idea of this copilot let
me uh is
to map the fields that we have in a
table and columns in
Excel yeah so let's
uh do that we have here map fields
so now what we're doing here we are uh
sending to the aure
openi we're not sending the Excel file
we're not sending sending the data of
the Excel file we don't need that what
we're sending we are sending the headers
of the um Excel file and we are sending
the information about fields in our
table and we say that hey these two data
sets please map them together and llms
are quite good in these
mappings let's see the uh result so ID
is mapped to the code which is nice
session title to name summary to
description nice uh this is also super
cool so a main speaker is mapped to the
speaker one and a co-speaker one is
mapped to the speaker two that's good
job copilot uh however here is a uh also
bad job like a target audience is mapped
for some reason to the status
uh but you know we should understand
that uh the copilot are not always uh
right not always correct so we need to
um leave the opportunity to users to uh
change the final result in this case I
will just delete this and I think delete
this as well uh the rest seems to me uh
very normal uh also in the copilot uh
toolkit we have this regenerate uh
action uh that comes uh out of the box
so the idea is that um uh the generate
action appears in the input screen and
regenerate action appears in the output
screen so user can just click on
regenerate it will send the same
instructions and the same system message
and the same uh user message so the
Azure openi can regenerate this uh
and probably be better or maybe worse uh
result at least uh all the
same but now I'm fine I can import
that and uh I can go to my uh
sessions and I have uh all sessions
imported here so I now I don't need to
write
uh a separate Al Logic for each of the
files uh I have one Al logic to import
from any Excel file which is very
cool
um so let's
see also into the implementation here a
little
bit so once again uh let's go to the
promt page first
so this is the uh prom dialog page for
our
co-pilot uh
and so
it uh has a prompt area but there is no
input of of the text just some uh Fields
there that are not editable just to show
uh the user uh what the project name and
what's the Excel file name so just here
was aware that in the context of he is
working on um
also here is a generate system action
and here is the regenerate system action
so we see that um so first of all yeah
so this is the caption so we can change
the caption just using the caption uh
but the logic is the same here so I'm
running the same logic uh and uh copilot
uh UI just rendering this for me uh
differently yeah so the in the first
screen it's generate on the last screen
it's
regenerate and here is a new system
action which is called attach so this is
just a you know uh normal action just it
comes with this image uh that shows some
attachment and uh but this is our code
so we write the code to import the Excel
file to the Excel
buffer uh and when
[Music]
we when we go and uh generate here let's
go to the see the AI
logic um so we go
first uh and generate the
proposals so once again template is the
same what we change is actually the
system message so the system message is
of course our new uh AP uh IP uh for
this so once again you put uh this in a
uh context so you describe what is your
task what are your
instructions
um what you describe the input yeah so
we describe that you I will send
you
uh the list of fields and I will send
you the list of excel uh headers so
please map them uh together and you uh
here describe the uh Json
format uh that you uh wait as a uh
response um also nice to have here like
no comments are allowed and uh response
should be in a Json
format uh so you know uh copilot will
not reply you with a hey this is your
Jason are you
happy
uh yeah so and then uh when we have
this
generation yeah and then also important
thing so we we have the system message
and we have the user message however
user didn't you know we don't have a us
uh the input here right so it's uh we
generate the user message for the
copilot so here uh we just say that hey
here is my Excel headers and we list
Excel headers and here my session table
fields and I uh list the
fields and then we when we have
um uh mapping we convert text to mapping
once again the same way we did uh
before and
um here when we have a result so our
result is a table field mapping I uh
load this
um uh result to the sub page yeah and
then when I apply when the user click on
okay I want to keep it uh then I run
this apply import of sessions function I
get my temporary records and then I uh
I'm doing this you know
uh simple uh Al uh thing when I go
through the mapping and I import my uh
sessions using the uh record TR so here
you can you know I have the sessions
table I use the record uh to refer to
that and then um field to the field uh I
assign the field from the mapping and
assign the value and then I you know
insert that so very straightforward and
this is you know one code that you need
to implement and it will work for any uh
Excel uh
file yeah uh do we
have I think we have some recap of the
slides if you would like but U yeah so
this is this
copilot can you yeah so we have the
attach files attach files yes is the
system action mhm then uh we have the
drag and drop experience the regenerate
method which is part of the prompt
options yes and you have shown that I
did yes very good now uh this is uh
something new uh that appeared in uh
actually
yesterday uh in in version
24.2 uh so uh actually so this was part
of my uh contribution to the system
model um you can set the Json mode and
you can if you can yeah I don't ah okay
so um the
idea sorry yeah the idea is that uh in
the you know previous copilot I showed
you that you should uh say in the system
prompt like okay please don't put any
comments to my Json respond just with my
Json uh there is a new Pro property in
now which you can set as a set um set
Json mode to
true and in uh I would say 99 and 99%
you should be sure that uh the output
will be pure Jon Json however it will
also require in the system message um
you should you know explicitly say that
you need to response in the Json format
so like two places like first in the
system message you should say that
please respond in adjon message adjon
format that's it and then set the uh
Json mode to true so this uh Works in
24.2 uh very good
yeah now let's move to the other um
Copilot
so now we have our sessions imported
yeah and uh uh Luke is pretty happy with
that uh and now we want now now now this
is a complex part um especially when you
um uh send uh your sessions look in
after the deadlines right uh it is um
very comp complicated to look to
schedule all the
sessions uh but we will build a copilot
for
that this is our sessions table and we
have some Fields here like a date a
track number um start time and uh end
time so if you think about the process
of uh uh scheduling event uh this is
actually called the optimization problem
because uh you have some kind of data
set in now in this example this is set
sessions and each session have a
duration and you see that durations are
different so it's like a 60 Minutes 30
minutes 75 minutes and so on uh and you
probably can have a conference uh for
one day or maybe for two days or more uh
so for sure you can't have a one day
conference and put all the sessions uh
one by one yeah
uh you don't have physically time for
that uh but you can put them into the
tracks in parallel uh that's the first
thing but also you should consider some
uh limitations because uh the conference
should start at like 9: or finish at 5:
you should have a lunch you should have
a breaks between uh the conference uh
between the sessions and so on so many
limitations uh
so really complex
work so let's uh try copilot to help
us
so I built a copilot which is called
schedule sessions and uh just uh take a
moment look into the screen when I click
on
this I don't have a input screen at all
so now we have uh started with a
generation mode uh because we have
everything in place we have uh all data
that is required to put our sessions
into the agenda um let's see if it did a
good job for
that um so this is by default I asked
the copilot to uh schedule in a two days
conference uh so it's start at 9: finish
at uh 10 and then put sessions in a
parallel in two Rex and it's yeah but
it's here is not very good one he
finished it uh after the end of the
conference so we I said that you should
finish before five uh that's the first
thing maybe we can
try uh more days like three and a half
days let's
see so now it's actually try to
reschedule all the sessions to the uh
conference duration if it's 3 and a half
days so this is first day second day and
the third day and this is yeah so this
is three and a half days and we don't
have a tracks in parallel here the
sessions go one by one maybe not very
good experience yeah what about one
day can I do the job with a one
day oh no he's very bad in that so he
lost some of the
sessions um it's called it's called
scoping so but this is something that
you can experience when you test your
co-pilots and this is a nice uh thing
that we got this so uh let's try to
maybe fix this I I have
some uh instructions already prepared
so let's go to this
copilot and I will add some additional
instructions
here so this is a tip for you if you
have a good you you you feel that you
have a good prompt system prompt so you
describe the task you have all this
describe all these
limitations uh you set the instructions
but still Azure open AI doesn't really
follow your instructions and that can
happen this can
help C lock important so these are
instructions that are really important
please follow them and let's
uh publish that
yeah so we see saw some
scenarios where it didn't do the good
job uh let's try
to schedule once again
and maybe change for the first
day and is now doing good job so we put
in all sessions into the three tracks
yeah thank you goil good we will keep
that now we
uh have all
sessions
scheduled yeah so we have here so this
copilot is uh what's the the difference
between the the previous one so uh the
IDE is pretty much the same so the AI
logic is uh the same we just used the
new system message and we generated the
user message with a um actually
describing the event like when should it
start end and uh the break times for the
sessions and we list their
sessions however we don't send all the
data to the Azure we send only the
duration of the session because we don't
need anything extra we don't send a name
description and so on just the duration
that's what matters for the uh uh agenda
and then we got the back the result
result we map it and that's it and um
the only also this
um generation
mode um so here you can set the prompt
mode equals to generate and this uh
will um start uh the prom dialog with
this generation mode without
input um let's then
go
next do we have something there
yeah we have uh we have the wrap up just
press mhm yeah so this is the uh format
of the system message so this is
actually uh the template for the system
message like describe the goal describe
some steps the rules and the output so
in this order and this is very
uh very wi widely used template for the
system message yeah then we have the
user message and the user message yes I
already described that you can click
then and this was the new thing there
which is called prompt options do you
want to talk something no I think we
showed it right yes we showed that but
also we showed here um maybe you noticed
we I moved between uh the generations
and this is called the the uh history
yeah so prom dialogue actually supports
history uh if you would like to see you
know go back to and see your prompt
again and somehow associate the output
to to The Prompt or refine it then you
can use that and and notice also in the
page caption that we actually show uh
was using the data uh caption expression
uh the property uh you can actually also
see the use that property for
visualizing The Prompt that uh that that
user has put in
yep uh and the last one
uh not really the last one but almost
last one so now we have the
sessions uh scheduled and we want to
have uh assistant co-pilot so the
assistant co-pilot will work something
like uh like how many sessions I have in
the conference
and it will say hey I have a 20 sessions
uh or maybe I can say
um when is the
session about uh AI in
sales and it will yeah reply me or uh I
can ask something like when is uh
John
speaking it will answer me I can
rephrase
this dimetry
speaking I'm not speaking
there so
um how this is done so this is
completely different
experience uh so this is called like if
you want to ask something about your
data uh it is the bad idea to send all
your data to the Azure open AI uh L LMS
are very bad in counting things they are
uh bad in analyzing the big data sets of
data uh so how did I build that MH
so this is something uh something
something new uh this is called a
function calling so and
um if you sleep uh please wake up for
the minute
um so um because I will be a try to be a
little bit slow here so um the there is
a user and the user asks uh about hey I
want to find some hotel in anwp uh for
for the uh less than 100 of years and I
have a database of all the hotels
instead of sending the database of the
hotels every time to the asure openi
what I'm
doing um so I'm sending this to the
co-pilot as a user message but also I
say that hey I have a uh a function
inside of my system that uh search for
the hotels yeah so we have an extension
that I have a function that search for
the hotel but make to make it work I
need to uh pass two parameters the uh
City and uh the maximum
price so um I Define this function I
describe this function to the Azure
openi so I'm not sending the function
code or whatever I just say that hey I
have the function that is called find
hotels and I have uh to make this
function work I need to pass there two
parameters I describe these
parameters and
then I put this as a description to the
Azure
openi and I can add more functions so
probably I have like um one fun function
to find the hotel other function to you
know book the hotel uh whatever so um uh
I list the functions uh
descriptions yeah and then uh compilot
sends the user request and the list of
available functions to the Azure
open Azure openi job is to uh find the
function to select the function that
will
solve uh my task and prepare the
parameters for me so it selects okay you
have a find hotels function that's
probably the one you should use and
these are the parameters of your
functions that you should
pass this is the response from the Azure
open now I have this
response now copilot toolkit have the
list of functions available and it
selects the function uh that Azure openi
suggested
and copilot toolkit runs this function
it executes it
automatically um so now it executes this
function and I have a result of my
function in the AL yeah so now I uh my
job is just to take this
result uh and so this is the result of
the function this list of of hotels and
then what I can do I can show it to the
user immediately yeah so this is uh uh
how this is uh
works so in Al it will look very similar
uh to what you uh did before but uh
instead of the system message you uh add
a tool here
yeah and
um then you check if the response is a
function was a function call then I get
this uh result or what you can also
do you can send this result back to the
Azure openi uh that will allows Azure
opena to generate the uh final answer
for the user so it's up to you show the
immediately the result from the function
or for the user MH Should Skip that or
yeah uh you yeah actually you can talk
about that so
um there is a limitation uh we we have
like um thousands of functions available
in the business Central uh we uh cannot
just send all the functions to the aure
open uh why why that is because we have
a limit in how many tokens the llm can
process right um so let's talk a little
bit about why we cannot just send all
data to LM and and how what tokens means
to llm first of all yeah you know we
have the word language in in llm right
and and tokens is U somehow the unit of
measure for for them you have here an
example uh well we have seven tokens
here and 7
characters and uh why you know we
actually in the toolkit we support apis
for for token counting and and why do we
do that well because uh uh that uh that
you need you need to know this is kind
of uh what we pay you know at Azure open
Ai and open AI for right uh how many
tokens we are we are
processing and um and yeah I mean when
you have a big prompt as Dimitri also
says that you need to find ways to uh
you know split it in into multiple
requests uh in order for you or useing
beddings for that matter to to figure
out uh how how you can uh reduce the
cost and and handle this so how we can
count them yeah so there we have also uh
different methods uh we supportting the
toolkit and um actually the interesting
thing is that uh the token counting is a
little bit different per model uh and
that's why we have um we have the uh it
here the 3.5 but then we also support uh
methods for other
models and now the event assists yeah
let's do it very quickly um we only have
seven minutes yeah uh let's just do it
quickly just to show you so this is the
last demo uh but this is obviously what
you can do now and um uh that was our
contribution uh to the BCA hakon so
um um let's say we have this uh
assistant uh
co-pilot uh and
um like we we saw in the previous demo
when is the session uh about AI it
actually replied but when the session
about if I rephrase it like when is a
session about artificial
intelligence uh it will not uh find
anything oh it it is
found uh oh maybe because I let me check
uh maybe I already embedded
this yeah that's because
I actually did some work uh before so um
uh but the idea is that
um there is a full text search that we
have in a business Central right now um
if you want to find some uh desk it
means that the desk should uh be in the
item uh
name but if you search for the furniture
you will not find anything because like
a Furniture is something that uh desk
means but it's not uh in the
description the semantic search solves
this problem so it's uh when we search
for the furniture we can find everything
that uh means as a Furniture like items
desk chairs and so
on and
um to make it happen uh we use uh the
term embeddings so actually what we do
we take uh our data like uh items we
have a description of the uh each item
and we convert it to the uh let's it is
called Vector so we we actually sent
this to the aure openi embedding uh
model and it creates this vector and
then uh this is just a mass of what
happening how to find similar texts so
you have one text like which is
Furniture you have a second text with a
with a which is a chair and uh you take
these two vectors if they are very close
to each other you calculate this engine
uh angle sorry uh if
it's very tight to each other it means
the two texts are similar if not they
are different so um in this um case so
what we're doing we take the one text we
have second text uh and we calculate
this coin similarity and we do this for
each of the uh items that we have in a
business Central and then we just filter
out the uh coin similarity that is um
less than
0.8 uh so that's actually how this uh
all
works so I have this uh text I have
these vectors and I have Al logic to uh
calculate these uh similarities
there and this is uh when where you can
use that in copilot so because uh now
you are not limited to what user asks uh
you uh just uh can uh find very similar
items and use them uh to answer to the
user mhm so let Let's uh let's quickly
so first of all just want to say thank
you Dimitri for making the copilot tool
kid live uh in so many cool
examples um and um let's focus a little
bit we have H three minutes left on
maybe no not not as school but uh super
super super important uh which is you
know how do we test these awesome AI
features that Dimitri just showed right
and um I must say that um well if we
thought about before that you know some
of this test driven development is
somehow a taste some people want to do
it some people don't uh for for AI it's
really important that before you you
know once you pass that stage where you
go to uh Azure open ey studio and try
your prompt and think wow I nailed it I
think uh this is really cool and it's
going to work uh well then you should
make sure that before you take to the
the next development phase that you have
uh your test in place and and there are
different type of tests uh uh from our
experience we also whenever we ship a
features we do both accuracy testing and
and also we have uh quality end to end
tests and accuracy testing why is that
important because many times you will
see that your prompt runs and it's fine
and other times you'll see that your
prompt doesn't return the uh the what it
supposed to do and you really don't know
why or you don't know what to change or
you have to change the prompt and when
you change The Prompt how do you know
you change it For Better or For Worse
and uh and that's where the accuracy
tests come into play uh for the the
other part that we're doing which is
also very very good practice is the
grounding test let's say let's say an
example like the marketing text where
you have uh you know your item
attributes and you generate a
description one one of example is well
let's check if these attributes are
actually in the text description uh and
similar to you know some of the things
uh um Dimitri has shown on the quality
test uh well this is uh what we call
internally red teing very much focus on
harm testing uh for example is it
possible that uh that you make a copilot
say some things that it's not supposed
to say uh or bias or for example someone
actually making it do other things that
it's supposed to do uh so jailbreaks for
example um so this is also important
both of them are going to ensure that
you are shipping high quality AI
features and uh well you're going to say
well sure but then what is Microsoft
doing for it um so we also are working
on on uh on on some test uh test
framework of course to help you and help
us as well um and um this is work in
progress It's not something that is
finished it's just some thoughts we have
uh and uh this is going to be available
on GitHub for you to uh you know give us
your feedback and and uh and help us uh
you know uh finish
this then we also have apis for
Telemetry uh we also have some sessions
on today or tomorrow on on Telemetry so
please go ahead and and attend that uh
same with AI safety safety uh we have uh
also security and privacy best practices
for AI which I uh strongly suggest you
attend uh and uh yeah thank you Dimitri
for your number series contribution to
uh to to co-pilot right still work in
progress yes uh and you can skip that
yes I can skip that and then we have the
community IDE yeah let's skip that so
then I wanted to maybe quickly go
through what's next because uh that is
always uh Al a little bit the fun part I
get to have I have to have three fun
slides right yes thank you uh okay so AA
has announced to the the managed AI
resources um actually we went to private
preview I understood you know our
engineering teaming Copenhagen has
discretly informed us that actually we
are live with the private preview um and
uh of course for if you want to sign up
to try it out that is on AKs BC managed
AI sign up and and um yeah we're looking
forward to see how this story is going
to evolve and uh for us this private
preview is um is also to understand you
know how much capacity would be needed
for some of your Solutions learn from
that and uh uh get this through public
preview what's next well I said that the
co-pilot actions are primarily on list
pages but they will also come on card
Pages uh we're work working on this on
this release
and we also have some plans for somehow
to merge the uh copilot chat experience
with with the prom dial the whole prom
dialing story they feel a little bit you
know separated right now um but that's
that's work in progress for us and here
you have uh um yeah you could say a
prototype where we will be uh kind of
showing the analysis assist uh from from
the chat and with that yeah with that
well we don't have time I think for the
Q we will be here there are any
questions okay let's do
some uh so
this okay my question is
is copilot prompt supporting any uh
different languages than
English yes it is for marketing text we
are supporting uh seven languages uh for
the for chat not no that is in uh in uh
English and then we're planning to
expand this uh uh languages uh when is
that uh maybe June or sorry fall in Fall
yes but but I I mean the question was
for the kopal toolkit uh yes in in in
the P if user can use different
languages than English if you we don't
have this option
today yeah we
can I think you you can
yeah there
H yeah yeah but to do can they specify
as attributes there no okay you have I
also have a question okay sure uh do you
have any limit of the system text or
user input I mean in terms of
length in uh the limit of the system
text uh yes so it's uh dependent on the
model so it depends on the model yes so
it's it's uh that's for
you yeah depends on the model it can
start from the 4,000 tokens to you know
up to
126 that's
we um at the moment you're using open AI
uh are
companies uh building private AIS for
people to use based on that is it going
to be possible to
redirect uh queries to private um these
private AIS so that um you can you don't
expose your data to the the big bad
world you mean like uh private
deployments or yeah private
deployment I
think rir requests yeah so the compil
toolkit is uh a wrapper around the Azure
open endpoints so it's uh
uh it directly connects to the Asia open
AI resources so but but then it also
depends if if you if they using the
manage manage subscription that we'll
have to see if you go directly through
Azure open AI then you can use any
capability right but not through our
okay
