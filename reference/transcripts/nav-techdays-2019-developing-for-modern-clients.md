# NAV TechDays 2019 - Developing for Modern clients

- **Source:** https://www.youtube.com/watch?v=uKLlRnseQ7o
- **Video ID:** uKLlRnseQ7o
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 92m22s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

so welcome to our session I hope you
have you had a great day today so far
enjoying the first part of the
conference we also have a very busy
schedule today we have a lot of demos to
show Tomas and Ariana have prepared
thoroughly and yes so let me introduce
those two gentlemen Tomas is engineering
manager for the client runtime team in
my workload and yevgenii is engineering
manager for the client experience team
also in my workload and today we have a
lot of how to say the most to show you a
lot of say productivity features that we
didn't have time to present you in the
keynote and our objective for this
session is to maybe maybe let you walk
away with a great understanding of how
powerful the web client has become in
this release and before we start with
the demos let's remind ourselves what is
the business central mission for clients
so we have very Hajus a much mature and
proven interface which runs across
devices both on-premise and cloud so we
have the browser client on the desktop
we have the tablet and phone with the
mobile ads we also have an outlook
client actually in many ways is the most
remote client it is the client that
people use in pre-sales a lot and also
have integration with sell earned a ton
of other integrations with power
platform so write your code once run
everywhere that has always been the core
value proposition of our platform and
now even more so
on a modernized stack so what about
Windows clients well basically you
should rest assure there is no current
impact on the installations that you
have on for your customers we will be
maintaining the Windows client for
basically four years that is our current
support life cycle it is included in
business central April 2019 for the last
time and you can still sell this this
release until 2020 and we are also
preparing an FAQ in documentation for
helping you to basically think about how
to transition to web client what are the
nitty-gritty details about support life
cycle and so on so let's take a look at
the agenda for today
so we will start with the tour or the
consultant journey and I have shown in
keynotes a glimpse of the consultant
journey and now it is time to dive
deeply into it and also look under the
hood and understand how consultant
journey is working in web client the
other part is working smarter with
business central I actually touched very
little Enki not only to save use and
multitasking but we have a ton of her
activity features that are intended for
heads-down users so we plan to give you
a tour of that as well we also have a
section about developing for modern
clients I think here we aim to kind of
parts one of them is how to leverage
some of the new airai parallel paradigms
that that come in this release like the
page background tasks and also give you
a glimpse of how you can write modern
browser add-ins
and lastly we will talk about what's
next and you know give you a sneak peak
of some of the features that we are
working on in the current release so
let's start with modern clients
consultant journey Evgeny just tell us
how it works
voice check with check can you guys hear
me yes we can I have this magic pen it's
sort of like a clicker
take a look cool why does role tailoring
matters you know talking about role
tailoring role tailoring how many of you
know our ideas website where you ask you
to come here you know put your ideas for
this feedback come on we have ideas
website people go here you know put your
family friends colleagues cats dogs go
ahead and put your feedback so those are
feedback provided on the first day we
release business central and here's a
quote from zits feedback I'll just kind
of read for it loud in any way it was
possible to configure profiles within
the river then if business Central is
not there are we the only partner who
finds this a huge problem
yeah so it's a big deal a role tailoring
was like a core promise of business
central a needy success for many of the
years we'd have a belief that you can go
with a modern ear P and a roll tailor
and customize your user interface what
you can do how does it look and feel
without any development involvement
basically power user consultor can go
ahead and do that so everyone wins
before we start talking about role
tailoring let's talk about role and what
does the role means the colleague of
mine built this fancy visualization for
the directions and the many ideas many G
about the role is that every user of a
business central which is a role
tailored ear piece system has a role
it's not just a fluffy definition for us
it's a concept or semantics which we are
bringing this release across all our
stacking platform
so users has a roles or also decide what
you can do
permissions entitlements functionality
look and feel and son suffers users can
share roles we sheep some of the roles
out of the box as a template we can
never you know match the real world to
some extent and the user can go ahead
and roll tailor their roles for what
they truly need and in a business
central their role is represented in
this way you can create a role in all
daily call his profile it has a name
description has a purpose it has your
initial home screen will start to work
with the business central and so on so
forth there's a big change to user
interface if use a user and you go to
the business central will talk
consistently about roles like in this
example in the previous version you go
ahead and change your ol center now you
will change your role if you don't have
any role assigned and you try to look
into the system we will default to your
new role which is part of our system
applications module so role become like
a very strong concept across the system
we use only profiles across some
administrative pages and in some things
which users who hopefully will never see
in their lives all right let's take a
look a little bit about roles and role
explorers I need to press a button
if you take a look on a right for you
left for me it has a small button called
start exploring your business central
functionality for your role again I user
have a given role I can go ahead click
it and see what's available for me in a
glimpse so here's the functionality
predefined so far as a my role
definition to myself I can do different
things I'm a business manager I have
some actions reports which I can go
ahead and use I can also go ahead and
explore both business central more allow
me to do so in this case I have a number
of roles which is configured for me and
I can go ahead and explore them and see
you know I'm in a pre-sale speech where
is my skillet inspections where is my
bird housing where is my financial
reports so in this case I can go ahead
and start looking for them
ok business central can do this business
central can do that and so on so forth
this data come from are all definitions
so if I'll use our most use key short
and shortcut from our telemetry I'll cue
if I'll go into the roles list page and
try to make it bigger it was a joke it's
kind of radical enough for me I can see
a list of roles in my system I can see
all enabled I can disable some of them
if I don't want them to be used anymore
I can see all the roles which is
promoted to this map of the system as
Corrina said in a keynote so I can go
ahead and explore them as a user of the
system you can see where they coming
from in this case we're shipping number
of roles as a part of basic application
you can go ahead and ship more roles as
a part of your extensions now if I'm a
nice Vee I usually want to bring my
brand you know I have a brand it's my
identity I want to call my action so
Erin knows it's a my ice reaction you
know to click so what you can guys do
now if you're in a pre-sale situation
for example
you know those people care less about
warehousing don't deal with buzzers and
wizard you can add the urals with your
actions which with your brand and then
you users when they'll go to the role
Explorer once is once is refreshed yeah
I don't see warehousing anymore and you
can bring your own roles so you can have
control dynamically right now as a menu
if you will both user can see you can do
promote roles of functionality or
departments overview of the product we
should not care about and you can bring
your own with your own brand now I need
to press No
yes come on again why did we build role
explorers this way you know first
question we headed apartments we had a
many suite it were great we know of them
we love them
why do sound so different you know
that's Microsoft doesn't what to do if
you step back from how any we work just
going to step back from your experience
and think about any earpiece system in
the market you know as a user when I log
on to the system I have some basic
expectation about data grouping I
probably expect to see data around money
account receivable account payable
banking I probably when you see
something about people vendors customers
I want to look for reports where is my
financial reports you know where is my
administrative tasks and so on so forth
so when we start thinking about this
grouping and this is grouping present in
any earthly product what we could do we
could do something is live in the past
basically take all the action
application make a copy of them title
tags enter to categorize them to build
kind of data composition if you will
which will make sense for the user to
experience the product or we could just
say it's a simple product we have a
number of roles they're all cover what
user can do for the super set of roles
can give me everything product XP
product business center can offer so we
decided to go that way we use our old
definitions as a way to feed the data to
build your overview
you can bring your own with extensions
you can dip remote or hide the ones you
don't like as that's how I knew many
definition works there was a business
central we try to keep things simple as
a user I can explore the product some
roles come from a base table some roles
will come from ice dissolution some of
the roles you can create yourself and
you'll see it in a minute as the
consultants and then you can also decide
which one is not relevant for users to
even Explorer every time I want to find
something I'm going for search our
dilemma to showcase if there is one
shortcut our audience know is how to
search stuff but the truth is sometimes
you don't know what to search for
it was code like bank reconciliation Sam
sink so there's like a deep desire which
when I don't know what I'm looking for
let me explore so that's why we will
troll explore as well so he has this
nice and I can show you a cool trick
with the surface cine it's like a nice
have you seen it I can do it again
there's like a nice nice label if you
didn't know what you find for try
exploring and if you click this link
will give you the role explorers you can
find further stuff which she wasn't be
able to find with your search which is a
good deal ferryman now let's talk about
a role tailoring a role tailoring I am a
consult
I am only phone with the Thomas I am in
the sky up on the Thomas I am on the
team to the Thomas I am on a Google
hangout so Thomas and Thomas asked me to
help him to configure his ERP system
because this roast those roles
definitions we built out of the Box
doesn't have my stands for him I have a
good news for you Thomas I don't need to
come back to him three months later
because and if I developer who can make
this modification I just say sure buddy
to find a good time we own a phone let's
take a look so Thomas
we're going to create a new role for you
and just use the keyboard and mouse I
can use their shortcuts
I'm going to the list page where we have
a list of roles and I'm going to hit
plus button this plus button was never
available in our SAS version since we
lose the product two years ago they're
going to create a new profile for Thomas
they're going to call it Thomas it's a
good name for the Thomas it's also
Thomas as well you can select which role
Centuri will be starting point so so to
speak you'll use the default one and
that's really it now I'm going to press
customize pages button harina show you
this in the morning but it's a true
magic which happening now I am running a
live system with a live data and I start
looking on that from your eyes from that
role so now I'm a Thomas no Thomas would
you like to see the action on the screen
no Thomas does this Seanie means
anything to you no yeah okay and son
suffers so I can use a whole power of
visualization tools with the same look
and feel to go ahead and customize what
he want me to do it's not just an action
moving around just to be clear it's not
only about a role Center so Thomas uses
items a lot at least he's supposed to
use the items a lot so he can go ahead
and customize every single page he don't
like this releases fields you can go
ahead to greet and control the fast
entry rearrange order fixed sizes
wherever you guys want you really roll
tailor your look and feel to what you
want on top of that you can go ahead and
maybe create more views I want to filter
list by cone
so basically we'll say run a create a
filter from all products which has some
one hand available and we are going to
save this query with variable name we
can save it so what I just did is not
just a higher show elements but you
create iviews and any power would
product allow me to do and everything
right now it's done for Thomas were
looking through his eyes on a system and
when I am done I'm just saying here I'm
done now what I can do or Thomas can do
he can send an email to his colleague
harina
say harina adjusted our with his
consulted on the phone he create a
profile for me which call Thomas please
log on to this profile through my eyes
because they share the same role and see
if anything's missing maybe we need to
roll Taylor more so our always more
successful or whatever I need to and
harina saying this it looks pretty cool
or it looks decent
maybe she say no no that thing doesn't
make sense to me please get rid of them
or please add a change of color you know
put some emoji 0 that's the point
so what just has happened I look on a
business central which has a lot of
extension come from AB source and our
basic application on top of that I use a
tools no coding
you know only hands and this beautiful
device to go ahead and customize our
roll tailor for my even role how my user
interface looks and feels on top of that
Thomas
tomorrow day after week after you can go
ahead and personalize even further how
is that role definition look uniquely
for him as well and that so if you will
have these three layers we have a first
layer where you can build your
extensions you can use our designer
tools with exactly the same experience
exactly the same experience look and
feel on production system the
drag-and-drop and you build your
experience on top of that you use
exactly the same experience to configure
a roll definition and on top of that use
exactly the same experience to
personalize your products same tools
consistent way of doing things
which is very nice now how does it can
ever work you know how can you explain
to users where these things are coming
from now because we're so flexible to
some extent I like to think about it as
this picture so let's say let's imagine
we are loading a page like every page
for the first thing we do is like a Lego
blocks you put in some bricks which come
from your extensions and from bicep how
that page looks like on top of those
bricks were giant putting bricks which
come what is a specific changes for that
given roll which is which is the one
which user is Lagoon to every user has a
roll wins first it was its release if
you don't have a roll there is no way
you can log on to the system or if you
don't have a roll will assign to you one
row default roll which allow you to get
in and on top of that will also project
your personal personalization and that's
how you page look like and how
everything come together
now we're doing some quiz time a lot of
engineers in this audience very smart
smart intelligent people so let me ask
you a question what will happen I
provide an extension for Thomas this
extension have an action or has an
action which hide an action from a base
app so it had a base up and like
attention hide some elements because I
thought he don't really need to do that
but then Thomas for his role found that
action and showed action again and
because the changes are applied from
down to up he can see this action now so
what will happen if I will uninstall my
extension again you had a break and have
the pending census break with your
personalization are all tailoring and
then you remove your extension what will
happen will prevent Thomas will try to
log on to the system how would his page
look like come on people it's a good
question
it will fail nothing will change
what would nothing will change you said
maybe nothing will change
do you have more suggestions action is
gone yes action is gone so the way how
it works is very simple not simple by
this how it works we have a concept of
soft dependencies to make sure that
Thomas can always log on no matter
what's happening because all this
extension baby no baby like beneath him
you'll have your upgrade cycles you have
dependence on ice these extensions it
will change the version things will
change so the way how maybe we can make
sure our system is flexible but not
fragile we do the following the tried
over the page we're trying to put a
brick if this brick doesn't exist we
didn't do that now are we going to the
next layer this brick this change
personalization had the dependency on
the level down it's not there so we
didn't do that
so if extension is gone and you took
configuration dependency was at change
it will disappear if you'll bring your
extension tomorrow it will appear again
because when you're going to result
other levels you'll be able to
understand it then they're going to show
it to you so use this principle of sub
dependency to make sure your
personalization configuration will be
always applied as long as their core
dependencies are still present so it's
not like they're going to say Thomas you
cannot log on to go there is some
configuration which come from dependency
and and in those succession uninstall so
please combine you know come back
tomorrow
nothing like that now we are coming to
very very excited stuff which is like
drew pure magic
at least we believe so when we move from
in our journey from a Windows client to
modern clients and modern clothes
primarily mean modern browsers I'm using
edge we using Chrome you know Firefox
where we will though the many things
which like was no brainers you know I
want to have application shortcuts haha
you know we just go ahead and build that
like it's very straightforward singing
the role tailoring was the biggest issue
for us because it's varied and very very
it was very hard to understand how we
can bring coral color and capability and
morning clients so the true challenge so
let me tell you how it works so I am a
consultant I'm sit down Sir Thomas I'm
using my mouse and I'm go ahead and
customize in my UI Thomas tell me when
I'm hiding an action or when I'm moving
in action do you think we're capturing
somewhere this action is moved 5 pixel
right or left no sir we don't do that so
what's happening behind the scene every
time I move my mouse and I make a change
in my user interface there is a small
smart creature in a cloud development
creature this creature observes me what
I do and think hmm
how can i express the change if I were
developer so every time I move a mouse
in my UI they're going to reproduce
you change it a structured L code they
are going to compile it we are going to
store it on our cloud service and an
extension we are going to return you the
res I love the result with a speed of
light or with lightning speed depends
how I see it and you continue doing that
ok I'll repeat it again every time user
go to the role tailoring small
personalization mode or configuration
mode to the designer for every change
you do with the mouse's we are going to
generate aisle code behind the scene
which we store those should represent Li
change store them in extension and
that's how it worked behind the scene
which is amazing and unbelievable
because those development creatures that
would exist and there is no like
compiler revisions to lie behind the
scenes as a main result of this design
it also means I can go ahead and
download those changes I can go ahead
and build them and use for my own
projects for my own needs I can go ahead
and deploy them for another environment
I'm using magic scene II again so yeah
Thomas telling me we need to move on
so our user uses UI to customize stuff
they're going to compile create I'll
bring him back his results
developers can also download all the
changes as well code and publish them
wherever Simone have like this digital
loop cycle if James you leave will be 0
all right let's move on with the demo
how it works so I'm going back to my
roles list page and have a small button
called export user created profiles I
just created a role for Thomas it's my
IP I can go ahead and do that if I'll do
it it will create me a zip file if I
open the zip file I'll see a lot of I'll
code here so here's the new profile a
credit for Thomas
it's a profile Thomas it has some
configurations so I just copied here for
our convenience and I'll put it to my L
code I'm running it in a light mode
because you can see it
that'll be a dark mood maybe might be
just a fashion these days but never mind
we'll do it like this
Thomas how can I rename a file to the
side panel mmm no side panel right-click
rename come here and help me with that
no yeah fine so here's the changes which
we just download from a clock our cloud
instance I just copies them it's exactly
the same intent so profile is al concept
now to create a profile it has named the
description and sounds of course it has
a list of customization which come with
this profile you can customize every
single page here is a simple example of
customization way just you know hide
some fields or modify them but you can
also generate a views so it's not just
you moving elements around but every
change you do with your generate and al
code will give you help abilities to
download them to download it so now I
can go check here you know type where we
won't make any modification many changes
so what I could also do now as a result
of this design I can go ahead pressed
ctrl shift P so Wilson show you today
debugging without publishing I will show
you publishing without debugging you
basically just go ahead and press this
one and what's happening now I'm taking
those changes as our changes which I
just downed it with a Thomas and now
upload to my cloud instance we had a lot
of feedback like with the visual studio
code we don't have a designer it's very
hard to make code reviews I don't see my
properties I don't know which one to use
you can go ahead and use those tools to
build your code skeletons very very fast
go ahead to the product hit
configuration mode created pages align
stuff move around create the filtering
and so generate for you your project
which you can use for your extensions
for your work going forward so when my
extension is applied and published on my
cloud instance so I'm going back to my
list of roles
and somewhere here we have a Thomas well
that's not that's not that much this one
we created and the way how you can see
it you can see what is the source man
here is the source fun which come from
extension here is my role I just created
so can go ahead you know
just change my role and see how how'd it
look like and select that one if I wish
if you are not sure what is a recent
experience let excipient just look on
the icon so in the product you all know
in laughs we had the definition of XML
file so every time make roll roll
profile customization you had an XML
file which represents a change
it was a great stuff it was XML schema
client parse it apply some magic but
outside of that context it was
absolutely useless artifact it was not
part of our configuration model a part
of our customization model it was very
very hard to use and that's why we
couldn't bring it to the cloud in the
New World
it's il running behind the scene it's
very hard for me to understand emotions
but it's a pretty serious and cool stuff
ladies and gentlemens it is you have
cloud ready LP system with a full role
telling capabilities chair look on the
market who can also do that with the
same extension model with the code
extension behind scene so it's Express
Express Express once as of now we don't
give you any way to import those
profiles as a user interface you can
deploy extension we will fix it shortly
and as a result of this fundamental
change when you're going to upgrade or
if you're going to upgrade or migrate
whatever you will to full release
version we are not bringing your
personalization and one configuration
with you we will great migration
profiles but that SS we are not bringing
with you yet okay profiles il code use
them just what is great page
customization sale code use them what's
great if you use this way of the video
is a solution you don't need to write
any abrir code everything's very nice
not sure why I even show you that we as
backseat told you today we had a lot of
refactoring from system application and
you also revisited how profiles the
stored profiles are not a data anymore
it's not it's not a records in the
database it is true aisle objects
however we still maintain some tables as
a we
shoulder presentations you can still you
know write your code and it will compile
it and everything like that so I mean
naturally breaking anything of in this
point of you call fraction use role
explore and provide feedback if you own
your pre-sale demo showcase how people
can the role tailoring QP get up to date
what you can do I just show like three
for action you can do hundreds okay and
finally we kind of empower consultants
and power users to do a lot of stuff
without having development costs so for
you as a partner
you can say about your new revenue model
consultant hours billable hours as I did
with Thomas on the phone I can go ahead
and enable and enable him very quickly
without finding development resources
and you know the follow a small project
and so on so forth and with that we're
going to talk how can you work smarter
as a client or as a user with business
central thank you organic for a very
in-depth overview for the new role story
in our own clients product so what I
want to talk about is another area of
big investment for us in modern clients
and it's about user productivity and how
user can work smarter with modern
clients and without further ado I want
to jump to the demos because we have a
lot of exciting stuff to show and we'll
dive deep into the slice and explain a
bit more technical terms afterwards
so I'll just switch to my demo tenant
and working with lists is something
which is bread and butter for any
business software and other thing really
important when working with lists is
being able to adjust the list to fit
your data so you are able to scan really
quickly through the data and find what
you're looking for and as harina showed
in in the keynote now we have an ability
to adjust column width in product but I
don't know if many of you know that we
actually had this feature before it was
shipped with as one of the first
features with personalization mode but
we received a lot of feedback that it
was very hard to find that feature
because it was in
special mode you needed to enter and it
was a very unintuitive interaction to do
when you're looking at modern business
software or other Microsoft products you
expect that you will be able to adjust
the column width just by dragging next
to the column border and that's exactly
what we did now but to achieve that we
actually had to solve quite interesting
and complicated engineering problems
because behind the scenes it's still
personalization as afghani ASET there's
still tiny people writing al code every
time you drag anything in the UI or not
so yeah so what we needed to do we
actually needed to enter personalization
mode as quickly as we can without
interrupting user do his change and then
close the personalization mode again so
that was quite an interesting challenge
but we really were excited when we
managed to achieve it and we're getting
a lot of positive feedback from users
because that's exactly what they
expected they just expect that it's just
gonna work they don't care how its
implemented the complexity is on us and
that's another reason why it's so so
amazing to work on productivity for
modern clients because any improvements
we do it multiplies in work hours our
customers can save by not entering
personalization mode every time they
want to adjust a column for example when
working with lists are not a really
important thing is being able to filter
your data and we have been working on
advanced filtering capabilities in last
at least three major releases we have
introduced advanced filter pane we have
introduced filtering the spring we have
reimagined the views concept we made
views follow the page so it's
first-class al concept so whenever you
open the page the views always follows
the page and this this release in
October we also finally have to offer
the full crud experience for views so
when if I'm a user and I want to create
a view I I start with all all view and I
start adding my filters for example
let's say quantity on hand is
greater than zero and let's say I also
want costing methods to be select
selected on a couple of options and this
is a tiny thing which you can see here
we also improved the multi option
control on the modern clients so now
it's a lot more intuitive and also
supports a lot of common tiny keyboard
interactions you are used to so you can
feel very productive when creating your
filters so when I'm done with my
filtering now we have a new icon here
which says save this view as because all
is basically the base page so now I can
create my view which contains my filters
and it's specific to me so it's actually
creating a view in my personalization
layer just for me and this view helps me
to customize the application while I'm
working and again this is the second
instance of where we don't enter
personalization no to do some
personalization because since we had the
backbone to achieve this functionality
we started noticing that we could
achieve a lot more amazing interactions
by employing this architecture
improvements with it so we applied it to
views the same happens if I decide to
rename the view so let's say I no longer
wanted to be my view was gonna be my
view to very creative native naming and
then since this personalization and I am
the only one who owns and sees this view
I can also at any point decide to remove
the view and it's just gone immediately
without any interruption on my side
another thing which we did when we
reimagine the views we thought what can
we do further now we have first-class al
concept view under a page we discussed a
lot another thing which really helps
users to achieve their tasks so they can
do their filtering but what about the
grid complexity the some of the basic
pages have a lot of columns of course we
can do
personalization and adjust the the base
page but the same time maybe it doesn't
fit you all the time
maybe in some case some use cases you
want to see certain amount of columns
with certain um with some some filtering
and other cases with different one so
what we introduced was the shared layout
property which basically decides if the
view columns in a grid going to follow
the base page or you can design
completely custom definition of those
columns so already pub published an
extension with a view which has those
all new capabilities enabled and as you
can see I see a lot less columns I also
have custom ordering on description I
have my filters of course I also have my
freeze panes set on description and
descriptions column is also wider so I
applied a bunch of new personalization
inside of this view and if I switch back
to all you'll see that it goes back to
this full richness of this page as
developer intended initially so this is
a really powerful concept while we've
been working on advanced filtering
capabilities we also realized that we
can use exactly the same concept for
report request pages as well so in the
requests report pages you get exactly
the same filtering capabilities so user
is no longer limited to the filter lines
developer decided like in a filter
builder now user can dynamically add
filters and adjust the query before he
runs the filter and the same
functionality is also now enabled in XML
ports which by the way is the first
release where modern client supports XML
course as well so that that's about
views now I would like to cover a bit
more in depth about shared layout shared
layout shared layout I think is best
explained in a code snippet
I think code snippet speaks a thousand
words because here because here we can
see all the things which are unique to
the shared layout false view this is a
custom layout and you
and do all the same modifications you
can do in personalization in design mode
and role customization mode you are able
to modify the width for example of
description column you are able to
modify the freeze column on the repeater
you are able to modify the visibility of
the columns you are able to modify the
ordering of the columns all the all the
code you are usually right for page
extensions can also be applied in this
layout for the grid for now so this is
pretty powerful concept because it
allows you to create really customized
customized roll ter tailored experiences
on top of the pages or they have and
ship them if you are solutions if you
choose up so now I would like to show
another demo now I would like to show
how you can be even more productive so
I'm back at item list in an item list
let's now expand the fact box pane and
this is another thing which you have
never seen before in a cloud environment
we didn't have links and notes parts
enabled in cloud solution now they are
fully enabled in cloud and we also took
the extra effort to also make this
experience experience a little bit
modern so now we can see that we have
two tabs and first tab details tab
represents the all the parts defined by
a developer and we have special
attachments part tab where you can see
the system links and notes parts and we
also have a counter indicating if there
is any links and notes and how many they
are so user knows if there is something
to look there for and as well as you can
see here since we had developers we like
coded computers and this was just an
example of a multi-line rendering
improvement where notes are actually now
a lot better represented when text is
multi lined so that's pretty cool
but what about if I am working this list
and I'm opening a lot of items open in
one item I have one card I of course
could edit data I could switch records
I could close the page and open the page
again but it's pretty hindered
experience so what if instead I just
used a new multitasking capability to
pop this page out and do side by side
editing instead and I can repeat this as
many times as I want and this really
nicely snaps into very native browser
behavior of just opening new tabs new
windows you are in the control how you
want to work that is that is the main
point you should be the owner of the
experience and you should be able to
tailor it to best fit your your usage
patterns and as harina showed if I if I
added data on any of these cards they
will actually be represented the data
changes will be represented back in the
list so it's always user always gets a
consistent overview of his data so let's
let's dive in and see how this works
but there's one one thing I want to
mention before we do that you probably
noticed that there was probably not a
single session time out in the demos at
least first day I hope the second day
will be the same but one thing we did
when we looked at the telemetry we
realize that people are interrupted a
lot by this session timeout appears
every time you go for a coffee you come
back you are interrupted you start you
try to do something session timed out so
we looked at the telemetry and we
started increasing we did an experiment
we started increasing the session time
out and we start ups and we kept
increasing it until we reached 90%
improvement that meant that people were
seeing session time a dialog 90% of the
time less that magic number turned out
to be 2 hours
that's how far how long the session
should last so now the default value in
cloud is 2 hours so we'll hopefully
we'll never be interrupted by a session
timeout or at least only 10% of the time
that's that's quite a lot on premises
you are still in the control of this
value as always as you have always been
the default is 20 minutes but you can
adjust it to whatever value fits your
usage scenarios so let's let's not even
back to multitasking and actually it has
two parts the part I didn't cover was
the other type of dialogue which was
really annoying to our users that was
there is a dialogue open in another
window and you cannot proceed that was
the really annoying blocking dialogue so
what we do now every time a user opens a
new browser tab we actually give them a
new session so those sessions are
separate and whatever modal window is
open in one of those tabs will not
prevent you from working in another tab
so that's a really awesome productivity
booster now the pop-out window works
slightly differently pop-up window since
we want to achieve instant data
synchronization is actually reusing the
same session and is popping out tiny
client windows which are using the same
session and they are synchronizing back
data between each other and you would
you could say that we could still run
into modality exception as we did
previously of the multi tabs but we
actually have a lot nicer way to handle
it and user will be notified that
there's a model dialog open in any of
these windows and it'll be a nice
message informing him that he needs to
take action so that's a lot better
experience than just breaking user and
just even not explaining what how he can
recover another really awesome thing we
did was uninterrupted beta entry when
working with lists the next natural
thing you do you edit the list you enter
some data you create new entries in the
list and this was quite a big challenge
because naturally how the system is
essential works is that user keystrokes
are ignored while on validate trigger is
running because of course you need to be
done with your al logic to accept new
input from the user also users confused
because sometimes these keystrokes are
lost because system enters busy mode but
he kind of thought that he can still
type and now his keystrokes are lost and
user is in this confused state and
eventually user learns this behavior and
he goes into this forced workflow of
typing tabbing waiting and then typing
again but this is really bad habit to
have it's not it doesn't make you
productive it just makes you stop every
time you want to type just wait for the
AL code to finish running and in Windows
client this challenge was kind of
mitigated by the windows form runtime
because every keystroke would be
buffered in the operating system an
operating system will not proceed or
windows form runtime would not proceed
until it could actually process the next
change so that was that was kind of
mitigated but in web web is in modern
clients web is inherently a synchronous
so we are are we needed come to
completely reimagine the solution for
this problem we needed to create
completely new interaction pipeline to
handle user input so we can process it
when we can so it's never lost so
imagine I have sales line when user is
selecting item type so it puts up so we
put the item type keystroke well user
types in item type because he's
productivity user so he doesn't need to
use selection he's so good at using the
system so he remembers the item type and
number by name so he enters item type
item type keystrokes are put in the
queue he selects he types in name it's
again put in the queue and one cyst once
system becomes idle that means users
stop typing we actually push all the
changes to the web server and then they
get applied in order so that's pretty
amazing because this allows use
to keep typing as fast as he wants and
the keystrokes are never lost
system catches up once al is finished
processing the user input there is yeah
yeah so once no yes fine the biggest
benefit of the feature because people
still say like why we talking about it
for 10 minutes well the cool thing about
this is that you don't need to do
anything to object this this will be by
default enabled in all the off the grids
there's a small caveat though there's
still one blocker which will trip up the
user and as dynamic edit ability if you
have dynamic that dynamically editable
fields we will still need to stop and
wait for that field to become editable
again for user to be able to type so
that's something you would should be
aware of and should try to design your
solutions in a way that either you are
aware of this trade-off or you avoid
dynamic edit ability so your users can
type uninterruptedly so if I'm in South
Africa on a low connection you know just
slow 3G I can type through the line as
fast as I can
system will just allow me to do that
without stopping every single field and
catch up initially so Maya counters can
be super productive without saying
or was it websi me it feels slow isn't
it exactly the right another thing which
trips you up when your heads down
keyboard user is action invocation
because you need to stop find the action
bar expand the right group click the
right action so fix that we have brought
back applications for can support to
modern clients now model clients reads
the shortcut key property from Al and
all the keyboard bindings are applied so
again no change from your side you just
need to be aware of our new system
keyboard shortcuts and also some of the
native browser keyboard shortcuts so
don't collide with them so that's
something to take into account and also
as usually we introduce new application
sorry
system keyboard shortcuts in this
release and we updated our keyboard map
so you can find all the keyboard
shortcuts and I highlighted the ones
which are new we'll share the slides
it's finally don't need to take a photo
and lastly one one action item here
would be to check out our new
productivity cheat sheet which includes
most a lot of useful insights how you
can be smarter and work faster with
modern clients so again let's let's talk
about developing for modern clients Wow
we have like half an hour left and we
just have a lot of content to show you
guys so go with it we'll go a bit faster
the most the second city which people
hate after you know that keystroke
Lowe's what they need to wait you know
you come to your office you open your
desk you open an email you business
central and they just wait and wait it
was a purchase to lower it you talk to
the coffee call your wife look around
and it's still loading and you say what
I am doing here and there is business in
here P system sometimes you need to wait
you need we need we might need to run
very complicated calculations like you
want to calculate totals and if you are
and today or in any V or BC angels
release you I need to wait for that you
might need to get data from another
system outside of business central we
have work you know it's a very connected
world these days to in a cloud all the
API calls through to the data is they
may be non reliable can take ages and
again UI is it lock and use it just wait
and wait and wait and no one like that
and even if you don't wait today its
data composition grows you can you could
you might wait tomorrow and no one no
one like that to address that challenge
we come up with a new paradigm it's not
a new paradigm it's a known paradigm but
it's a new paradigm for DC community
basically how to wait less and do more
and run UI I think R honestly before we
do that lets us see how it works
so I need your attention right now let's
see if you can all count so I'm going to
open a customer card Thank You Thomas
I'm
to open a customer cart and I need your
attention on this area what screen very
my Mouse's and they'll do it a couple of
times you'll see difference look at the
fields one two three four okay for now
let's look again so I'm opening just
page UI and then I have some elements
which need to load and it takes some
time page is fully operational I can go
ahead and explore it and then there is
some data calculation we shall appear
because it takes nine seconds to
calculate them one more time I open a
page it takes two seconds to open the
page everything beyond two second is
great everything more than two seconds
user will feel it's slow very much I'm
opening a page on this page I have some
hella calculation which is happening
behind those fields don't look at those
labels one two three five and now we get
results half a year go or in a Windows
client I will need to wait all this time
before it can even be loaded
now let's sync it will take half an hour
to calculate then how it is feel that
will be my story from my morning when I
come to the office so in the modern
clients today you can roll the
calculations this is just an example for
fields but for every want to calculate
that stuff somewhere else as in brains
and bring results to my user interface
and let us refresh immediately no action
from you yeah so what just happened we
have a new concept called page
background tasks
PBT PBT page background tasks so here is
a very simple flow which explained what
just happened we I'll use my below the
page so we were here right the page is
loaded it took two seconds to do that
and then you can see results and you can
interact with it meanwhile there was
another processing which took another
eight seconds and my handwriting is
horrible but this eight seconds we
didn't wait for the vision like figure
out what to do
when calculation are completed we just
you I our refresh instantly yes let's
look in towards in more than two words
we have any concept about child sessions
so if I have a user direction I can like
I like a parent I can create a shell
sessions which running in the background
those child sessions will create a
session for a business central of a nav
do some calculations and when ready give
me so dress some results back today they
will go through the own open company
trigger and if you have a lot of codes
there those background calculation can
be slow so this file I'm you telling me
about that and we add a very small code
snippet in a system to say if you
running shell sessions don't run a lot
of stuff and then all good how does it
work
sorry Thomas he didn't look anything an
appropriate by the way he was preparing
for his next demo
alright so it's a I'm going to walk you
through the hello world example so I
have a code unit this code unit is the
serious code unit it just just does some
serious stuff it has some parameters and
it basically sleeps for 8 10 seconds and
then it's saying I'm done it took me 8
seconds the only thing it does imagine
here you calculate the totals imagine
here you run your bi query imagine here
call external services or you tree
usually you retry to receive some data
at some point of time you will be done
then you have a small piece of code and
I hope you can see it big enough on a
given page I'm saying buddy go ahead and
do this work please call this code unit
5 da da da put some parameters and just
execute to work and just do that and
don't bother me while you're doing that
and this case is just passing the
parameter 8 seconds that's exactly how
long put that one slips at some point of
time you have a new trigger on your page
saying on page background task complete
which were going to call
all calculations are done you get your
results back and your official UI you
don't need to run any current page
update nothing like that we have a very
advanced modern WebSocket technologies
which we can just refresh your UI
instantly and you just don't feel that
if something went wrong and it will go
wrong in the connected world if it's
time out if we kill your session because
it was expired if your connection failed
if you have a deadlock if you try to
write our database which you cannot do
from those shell sessions you can handle
those UI and say sorry it took longer
something went wrong you can give some
usability to see you to try again right
but you don't so you have some
capabilities for error handling and
they'll just fine
summary how to create page background
tasks for application developer who
knows l serial you do three simple
things you create a code unit who does
work like in this case it just
summarized summarized some values you
can do everything you want but you
cannot write to our database read great
but not right then you saying on a given
page please do the work you put some
parameters you can say in this case we
can tell you you have one second to do
execution you can limit how much do we
give the process max amount of time to
perform given tasks you can say that if
the takes more than two seconds just
don't bother it when the stuff is done
you can say on my page call me when you
complete it give me results back and you
can bind to your variables you can do
whatever you want with the results show
it to the user
and finally optionally if you if you
want not necessarily need to do it you
can say if something went wrong I want
to override default system behavior and
maybe provide some nice experience for
my users saying please retry again now
here's the funny part
il is still single threaded and our
debugger still can support only one
thread in a time it's not like a dotnet
you can connect multiple threads however
if you put your breakpoint to your code
unit
which will be run in a shell session we
will hit that so it's a fully debuggable
supportable just l code we just runs on
the different threads in a very special
conditions call for action please make
your extension so people don't need to
wait and a little bit more with their
time thomas thank you you're gonna so
again you just showed how you can build
really powerful user experiences using
new al paradigms and i would like to do
similar thing for client islands when we
move to web modern clients we changed
our technology stack in the same way we
changed how client add-ins are developed
previously we were using windows clients
it was not not based so naturally client
add-ins were also done not based so we
understand that it's a big technology
shift it was a big shift for us and it
will also take time for you to adapt to
adopt it but if you take one message
from here from my from this part of my
presentation if we know that is hard to
start but there's a lot of promise and
if you don't have a preferred javascript
library or preferred UI framework just
use what we using because we using these
open source components in production for
a really long time and they work so you
can also use them and be confident that
they will serve the purpose and we're
also seeing a lot of other Microsoft
products using very similar stacks so
just proofs of the of the maturity of
these libraries so just go quickly what
what is our stack so we using typescript
for scalable JavaScript development
because time cube gives compiler time
checks and prevents a lot of common
mistakes at compile time using react yes
for rendering our UI components using
sass for writing scalable style sheets
we using webpack for producing optimized
client side bundles
and lastly using Microsoft's UI fabric
previously known as office fabric as our
UI component library and the last I
would like to spend a little more time
on because it's really awesome it's a
Microsoft library providing the basic
primitive controls for creating any UI
it's based on the react so it's a really
awesome open source collaboration where
react GS is developed by Facebook but we
are building on top of it and also
making our solution open-source it's
used in all of Microsoft services and
websites so it's battle tested I'm
really sad that we are missing one icon
there its business central because
business central is also running on UI
fabric all the new what controls we did
after we changed our UI where most of
the time based on office fabric because
it provides really awesome primitives
which are by default aligning with
Microsoft styling guides fluent UI they
are built with accessibility in mind
they have all the keyboard shortcuts and
interactions already there and at the
same time aligning with what Microsoft
is offering to our customers so no
matter if you're using office online or
using business central you'll see that a
lot of interactions and styling is
common and that's what we are striving
for and you by using this library also
getting closer to it because while
developing client add-ins is also
important to follow some of the best
best practices and office fabric helps
of that a lot first of all it's a good
idea to use similar styling patterns
that goes from colors to design elements
or just design decisions and we have a
style guide for it and under at the
bottom of the slide there is a link no
worries we'll share the slides so you
can check it out or you can just search
it online so we already have some best
practices for you how you should style
their client headings because in the end
you don't want your user to open your
client add-in and just be surprised of
what appears after that because your
client because then user will think that
he needs to learn how to use it again
instead he should feel very familiar and
maybe not even notice that
this was a client at him everything
should look the same everything should
interact the same because that means
zero learning curve for the user second
thing is be a good neighbor
javascript is a single traded
environment whatever JavaScript you
using executing is gonna take CPU time
from the entire page so by being good
neighbor you're contributing to good
user experience because if you are heavy
loading CPU heavily user will have a bad
time first thing and it's a but also a
little bit of our design thinking is to
provide minimal useful experience first
and complexity we needed and it's best
illustrated by an example if you have
for example an item card and in the FAQ
box you created a client add-in which
loads a PDF document having all the
usage instructions for that item that
quite that canned up being quite a bad
experience for the end user because
every time user opens item card for
example if the PDF is 20 megabytes big
that's how long user is going to wait
for two interactive item card it's not a
good experience a lot better experience
is to provide the cue saying that
there's one available document to let
user know that there is such document
available and user can click on the
queue and see the full for example a
full screen atom showing that PDF
document that's a lot nicer experience
because user decides when he wants to be
slowed down and when he needs that
information so this is something to keep
in mind lastly I like to annotate
another point I think and I've pretty
sure a lot of industry is also moving
towards the same conclusion that in last
let's say five years the mid majority of
innovation done in graphical user
interface was in the web it was not in
any of other GUI programming frameworks
and web is becoming the de facto
platform for user applications and
business applications so I would like to
show some of the experiments we built to
inspire you of what is coming
next in the web what kind of standards
standard bodies are working and what
will be soon available in browsers so we
get inspired and start thinking what
kind of powerful user experiences you'll
be building so I'll jump back to my
tenant and I we have a couple of
extensions installed so first thing we
want an experiment with was video stream
so browser has a capability to take your
video stream for your computer and
basically get that stream of bits and
display it so we started with a video
element and it's kind of cool right I
see my video it could work like a mirror
it could be an add-in well we didn't
stop there
we added maybe four more live lines of
code and one open source library which
does image recognition so what we did so
I have this awesome three bit cup I have
here and it turns out that this box has
a barcode on the back of it and it
actually scans barcodes now because it
analyzes the video stream in the browser
side and the text that will has a
barcode industry can ask a question
Tomas yeah does it went to the cloud
Azure services like that not at all this
was all clarified and this is using open
api is on the web and this is really
powerful because anyone can take these
api's and these api's are becoming more
and more powerful over time so this was
this was a cool demo but we wanted to go
further what about if I have a legacy
system which generates a lot of files in
a folder and I would like to process
these files and kind of send this back
data back to maybe Al to write some
table so the next experiment we built
was using I am I admit very experimental
API called file system API what it
allows me is to grant browser access to
my local operating system folder and in
here I have test input folder
and I say I allow this application to
view my my files and I have three simple
text files
I have nav tag this written in the text
file I have empty text file and I have
2019 that's it that that could be some
input generated by a legacy system
within some proprietary file text format
so what I can do now is I can initiate
action from a client Allen since I
already granted access to that folder I
am able to read all the contents from
those files and concatenate this message
nav tag this 2019 and that content goes
all the way back to Al and Al displays
this message so L could do anything that
payload its received so that's pretty
cool
but L already have access to this folder
so I might as well add more content and
since I have persistent access while
this browser tab is open I can do this
again I just read new information we
just came in into the folder so reading
files is quite quite awesome but I guess
you would like to do it other way around
to write so we try that as well the API
is a bit limited but there's a reason
why I created a L file which has no
content so press write and what what it
will do it will send a message from Al
because this is a application action so
the client Adam and client add and we'll
try to find because client added knows
about all the files in my folder it will
try to find al dot txt it will request
additional permissions to write to that
file I have to accept and then Al
message has been written to my local
operating system folder file it is like
it's amazing like back to your reactions
if the traffic is a tough crowd to
entertain today
it's absolutely amazing yeah and I think
the biggest point is yeah I'm not
connected to any cloud services
everything this is all happening in my
local browser in my local operating
system interacting with Al so this is
something to inspire you so you start
being more interested in web start
looking for what's new in the web and
start building awesome solutions for
your for your customers karinna genesis
stage what's nice too modern clients
tell us it also works it's very nice
time legacy behind ya
okay so Vincent showed us today in the
keynote to be a roadmap for for Business
Central and we also talked about what
are the investment areas across the
product but now let's zoom in into the
investment areas for the clients so we
definitely want to close the story
around the data entry Tomas has talked
about some of the limitations we have
very regarding the dynamically editable
field so we will be also trying to find
a solution for that first rendering of
pages definitely top of mind for us
Vincent has showed you the ghosting
video that is a an experiment we are
also looking into and hoping that we can
have this available for for April let's
see if it's making it print print is
another area every partner we have
spoken you know regarding you know
moving the on-premise customers to cloud
they all asked about print the
definitely were working on the loosing
the solution for that pages with complex
layouts same story here a lot of
feedback from you that that there are
improvements to the
your article grid we have support for
your article grid in real-time but it's
suboptimal so we will also be covering
that we will continuing the story for
the role customization and role Explorer
there is a couple of features that we
would like to have for example the
importing of roles reporting we were
actually looking into how to simplify
the report the request rate experience
we know that is very cumbersome we have
done some improvements industries
introducing the filtering on request
pages but there are other areas to look
at no breaking changes so boxer has
talked about no breaking changes in the
keynote regarding application and and
it's the same actually across the stack
was for platform on clients we are
actually looking at how we can ship you
know improvements to the user experience
without disturbing the existing users
from performing their daily tasks we
were looking at how to ship features in
preview and and make users be in control
whether they want to use these features
infinity or not
and finally world-class service yes that
is also something top of mind we are
working on improving stability and
resilience of the micro services that
power today the web client in cloud so
these are a couple of the areas that we
have in our mind and now let's we want
to show you some videos with the
features that some of the people that
we're working on so first of all we
talked about role explorer being you
know an elegant and interactive map of
your customers organization and because
business central has a lot of
functionality from Microsoft and from
you it's it can be actually rather
difficult to to find information
enroll explore if you have a lot of
content so let's go start the video we
plan to introduce pines and here in the
recent we are here in the business
manager Rosenberg but then let's zoom
out of my role and let's search for
vendors and notice how the system
quickly and smoothly shows me where are
the areas where I find you know pages
reports tasks set up pages that are
connected to connected to the vendors
keyword that is quite the best thing yes
roll Explorer is coming soon co-written
so also another another part we are
looking into is to provide content for
role Explorer across different countries
out of the box we have countries where
where you can find real Explorer today
that is US Canada UK and so on and we
will also be looking at other countries
in the minor updates whole for our cloud
solution and we will be continuing to
covering that in in major releases the
other another feature is related to your
article grid as I said we are so we have
support today in in web client for the
expertise is quite experience is quite
suboptimal it doesn't really look as a
tree and be expand collapse actions are
you know somewhere deep down the context
- a user will probably never discover it
and we are basically introducing new
changes to this experience we are
aligning actually the tree control with
other products that are in in Microsoft
we are promoting the expand all
actions and also expand expanding and
collapsing / and that's it so far so
once miss left you have some t-shirts so
go ahead and grab them if you will
questions with the lady in the first row
I have actually two questions first when
user changes customize the page or roll
and there is an extension which is
created in the background do we see it
in our extension list somehow like a
beer waiting for you for those who have
a questions just stay will be he'll time
yeah so the question was if I'll
personally cheryltaylor
can I get that exchanges extension you
cannot see this extension as extension
in extension management page but you can
export them as a code the reason why
Candace is extension we're not we still
not sure what will happen if you just be
able to delete it as dentally so it's
there but you can actually access it
unless you export it from the export
button so it's there it exists but
Microsoft has a special safeguarding
around it for now you don't see it in a
list but you can Dow export all this
code for the extension and then publish
it as your own extension then as your
own IP for another instances okay thank
you and the second question the feature
and user can type without being
interrupted like if there is a slow
connection or something if there is an
error in any of those fields how will it
work
great session so then our error message
our bubble will be displayed and user
interactions will be queued until user
fixes there and then they will be
reapplied
so go like this six again go like this
at anymore
within the busy neuro not was in
multiple roles yet that's pretty cool
first of all thank you for your session
I was wondering can you writes to temp
in the page background desk can you
write
yes 210 to your database now to temp for
example and sometimes you write the seco
sometimes you write to a temporary table
I don't think so no so the reason why
we're not allow it to write a database
because there's many cases where you can
kill the session on the server is
running as a thread with a low priority
it can timeout we need to have a
consistent way we can stop that
execution that's why right the database
is not available
as of now understand the question I
think the way how Sarah will teach you
transaction it will still think you're
writing and will prohibit you doing that
okay but you can check that let's
connect the LinkedIn and voters also a
good design pattern would be tall so not
do the same in API web services to any
external services because these sessions
can be killed at any point so they
really have to be read only across all
the stack no matter if it's business
central or across the stack to other
services as well if you look at our base
app usually get inspiration how can app
take that capability we have very
limited up tickets for now for now if
you will there is examples how we can
make your fact boxes you know run
asynchronously queues and so so far say
so we just introduced capability it's
very functional maybe not so much
desirable yet and that's a lot of
possibilities absolutely so we love
modern clients you love them as well
good start thank you who was first
suspect yes please from somewhere
[Laughter]
sorry I have a short question about the
design mode so as we know we have a we
only have a different design from
singing sandbox environment yeah so if
we or our customer to disclose customize
the design extension so users or
partners have to compile the source
because we only have to download source
as air file so why why why Microsoft oh
yeah
do not let that user can download a PP
file or it was already on some load map
because though you want to change some
UI settings for all our user you know in
their product environment I'm not sure
sorry I understand the question
yes yes from sandbox to product
environment so you can't download the
extension from the sandbox as a PP file
if I'll customize my system and sandbox
to a roll tailor for my users I would
like to take those changes in production
environment right away like this without
redoing those it work again and again
yes yes great question so for now so now
we don't have to keep a beauty yet right
now you kind of download it with
extension publish it again the same with
personalization I cannot just say I
customized module heavily let me apply
my changes for Thomas and let me share
the changes with Karina I need to redo
it again which is kind of functional but
far away from being desirable it's not
on our list to improve it as you see
another roadmap absolutely troublesome
personalization move them around make
sure all the investments you don't need
to redo it again and again and again
again no one liked it obviously
Thank You grace I wonder
yes first of all thank you for the Royal
customizations that's great but one
question regarding this if I hide an
action or a tile can I unhide it it
great question
Aaron of us Rican the only thing we
support currently which you can undo by
user action is bringing back fields
which are defined on the page tag box
parts queues roles under parts right now
you cannot add them back it's very top
of our list because it is blocking user
scenarios currently only way to recover
is to reset the personalization yeah
back to the point we don't want you to
waste your if you just go to the
situation you want to roll back fast you
wanna add stuff today is a little bit
functional but again not desirable it's
a good comment we are very very aware
about that another question when I am
high traction and you delete it on the
base app then my extension is still
works you said but then it's not
compatible how do you resolve this so
it's it's a super great question back to
this complicated seniors creature on a
server if when you in your compiler with
the dev tools of the extensions we had a
very how do you call them the ponerse
dependencies are resolved strictly when
we asked runtime they're more flexible
so runtime was hard you so to speak when
you did our mode the runtime is soft so
we we allow you to have those softness
otherwise it'll it will be very
unflexible system and you could really
support that
personalization you know because we
introduced or personalization and that's
also an extension yeah so that is also a
soft dependencies to the to the pities
the actual extension and remember the
situation will happen without developer
we cannot resolve that and how will you
explain to the user you have ambiguous
reference I mean you can't so in a way
we have to make it soft for now and
maybe figure out later if you need to
support this case
good question regarding design hiding
and I mean it should be fairly simple
right just download code al cut and
remove the the hiding parts and
reproduce it again then you have if
we're looking for super sauce you really
really would like to I would never say
eliminate but make sure that the user
power user decent usual you know can use
a system and roll tailor without any
development evolvement and remove all
complexity from him even resolves that
case right now I'm saying if you go to
dev tools you know how to do it but he
or she wouldn't so we will catering for
a world where consultor are empowered or
the end user and in addition as you as a
developer can also do that but for now
we right you need to understand how it
works with behind the scene and so on so
forth but you she is bright on that
direction okay yeah I see you there yes
please this one person there you can
just tell it to us we will repeat loud
you have the ability now to define and
save views I think it would be a good
idea not only to save the sort of the
view but to have access to the index
files of this table because then you are
more flexible in a combined sorting
that's a good comments to comment on
your comment you would like also maybe
to index it as a metadata add more
fields from a source table on you I do
much more than you can do today and we
also look at how we can empower you
power you with it because in the moment
we don't have any point where we can
access to the index files in the sorting
and that's not good you were polite well
that statement is not good yeah it's not
good Oh with all these changes if you're
running on premise and and you don't
customize the base code or can you
safely install the see you start
breaking anything good point
so first of all we never told you you
cannot run your modern clients
on-premise you can okay but I mean in
terms of doing all the extensions and
customizations can understand when is a
new way things might break but within
the wave can you safely install the C
years
we aim and we do not want to break users
when they say especially in cumulative
update time in general the cumulative
updates for Microsoft are a bag of toxic
soot primarily and security
vulnerability updates and so on but not
and the goal for us right now and we are
still defining the know breaking changes
at different levels at the application
side what this means it's made very
differently you're not breaking it
sensors and also what it means from UI
perspective you know I think column
removing column you know if you think
without breaking you in short getting
immediate updates you also got a
feedback we don't have any visibility
what is inside like what is the features
security patches so we're also looking
on that will run your business as today
no disruption please stay with us behind
so we like five minutes or so if you
guys knew go to the beer just go we'll
stay here into the last question thank
you for your attention today
