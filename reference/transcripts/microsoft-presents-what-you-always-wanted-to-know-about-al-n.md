# Microsoft Presents: What you always wanted to know about AL Namespaces (and never dared to ask)

- **Source:** https://www.youtube.com/watch?v=F8NH69BGnKk
- **Video ID:** F8NH69BGnKk
- **Channel:** mibuso.com
- **Published:** 2024-06-16
- **Duration:** 44m27s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

today we're going to talk about Nam
spaces we're going to talk about what
they are and we're going to talk about
our experience with them so you might
learn how we thought about it might
learn what some tips and tricks and
maybe there are some questions that you
guys have that we can answer I have
Thomas with me here and Alexander both
of us are all three of us are from the
engineering team in business Central and
let's see what is name
spaces space name I don't know what is
it name spaces yeah might be a good
question to ask the audience how many of
you know
namespaces okay you can go now
so okay how many of you are then using
namespaces today okay a little less okay
so maybe there's some questions out
there that needs to be answered let's go
back through the basics here so Nam
spaces in our way of thinking is a way
to group objects to make like groups
logical groups of things that belong
together and within that have a unique
name in that scope of things that we can
do today by using prefixes and all sorts
of things but having something that is
more explicit helps a lot let's look at
an example here so everybody knows what
a fiesta is Right anybody who doesn't
know no awesome
so maybe it's a car yeah could be a car
is it this car or is it this car
do you
know well actually it's both of them
right so there are two companies that do
fiestas an old one and a new one right
okay with this logical grouping we can
kind of containerize things and give
that name Fiesta a place to belong so we
know which one of them it
is okay so logical grouping of related
functionality it comes with a couple of
extra things that we can use it makes it
easier to discover functionality that
logically belongs together so if I'm
building a car Library it's nice to have
things that kind of look like cars be in
the same thing things that are Ford to
be in the same place so I can find other
Fords and so
forth when you have these Nam spaces in
your code you can also Identify some
dependencies you have things that go
outside of your namespace we're going to
look a little bit on that later but take
that as input so some
guy long time ago said the hardest
things about computer science is Cash
invalidation we know that of course it's
hard and naming things and that's why we
have awesome awesome naming in our
product right we get these kind of
Errors cannot exceed more than 30
characters that's an annoying error and
we have like 38 100 Partners in a
growing partner community and they're
creating more and more objects with more
and more unique names so what's the
likelihood of clashing with one of those
well it's going to increase right and we
get nice names like this one right I
know is it uh account schedule well most
of you probably know what these means
but imagine you're a new developer
coming into business Central you have to
figure out something about account
schedules how the heck would you know
this is account schedules that's really
hard to know but if you had a namespace
called account schedules well maybe that
would help
okay we could do a lot of things to fix
this we could lift the 30 characters
limit right yeah everybody likes that
yeah it is something we're thinking
about but doing that has a huge impact
on a lot of things in the system so it's
not something we take lightly doesn't
mean we're not going to do it but there
are other ways we can make this better
without changing the Third characters or
at least not doing that
first okay let's look at namespaces in
Al
so it's the first statement in a source
file so it looks something like this
namespace and then whatever name you
define pretty simple it covers all the
objects in that
file and you might ask yourself why is
that we have these uh curly braces that
we use to kind of componentize things
and make them like belong together well
we looked at this and we could choose to
use the the curly braces but we decided
that that's an indentation that is
completely unnecessary and we don't need
that so no curly braces for namespaces
it covers everything in the file and the
recommendation is to have one object per
file to get that clean code and easy
maintainable source files okay you can
Nest namespaces using the
dot pretty
simple the name in the namespaces must
be CLS compliant so what does that mean
well basically means that it doesn't
matter if it's uppercase
lowercase and you cannot quote it so you
can't put spaces in it you can't put
emojis in it you can't put weird stuff
in there make it simple and CLS
compliant you can look up in un learn
what the other details of CLS compliant
is but you'll figure it out as soon as
you start trying to put in emojis or
other stuff
right okay you can use the same
namespace in multiple files you can use
the same name space in multiple
applications that's your
choice of course it would make sense to
have the same functionality in the same
team space but then you have to think
about is it really related or is it
related to the feature in one
application or is related to the the
functionality in another application so
think hard and long about this right
because it is a breaking change to
rename it
okay so using
the idea behind namespaces is that
you'll put things in containers so as
soon as you put your object in a
container it has that it has access to
the objects that are in the same
container in order to bring in other
objects from other containers other
namespaces you add a using statement the
using statement will then include all
the objects that are in that namespace
in your dependency chain inside the
scope of your current file here so what
does that mean it just means that if you
don't have access to Microsoft sales and
you add a using statement then
everything in the Microsoft sales uh
namespace will now be accessible within
this file there's no ordering of this so
it doesn't matter if you put Microsoft
first Microsoft last or not at all maybe
okay the alternative for a using where
you include all the objects in the scope
for this file is
explicit references here so using these
okay then that's a bit too much there we
go yeah much better good so you can
change these uh use these references by
being very
explicit ah okay this doesn't work there
we go fully qualified name spaces so you
add the name space in front of the
object name when you have the when you
have the definition in the variable
declaration and that means that you're
pointing to one specific object in a
specific namespace and not taking in all
the objects in that Nam space into your
scope so imagine you had two uh objects
with the same name in the same Nam space
you could point to or in in two
different modules you could point to a
specific one that helps a little bit it
doesn't remove the risk of name classes
but it will help uh minimize
it
okay so what is is a good
namespace is this a good
namespace yes
no what about this one good
namespace is this one good Nam space it
depends right it depends on what you're
doing who you are and what the
functionality you're providing is
actually doing so use common sense when
you create these namespaces I got a few
tips for you one is to avoid the generic
top level names if you create a
namespace that starts with sales then
you are likely to hit somebody else in
here who's also going to do the same
thing right so avoid
that do use your company name as a like
a prefix or start of the name SP space I
could use my own name but there's likely
more people out there call Stefan so
maybe I should prefix it with something
else I could use this you can use your
own company name but be aware that some
company names are not globally unique so
you may need to kind of quantify that a
little
bit there is a recommendation on
Microsoft learn where we have a
namespace uh guidance that says use
application feature also here so company
product technology feature name subname
space and so forth could look something
like
this lots of inspiration to be found
there on the learn site so go check that
out
last recommendation for me is don't use
namespaces from other people like if
you're taking a dependency on a product
don't use their namespace use your own
right even though you're extending an
object in an isv solution use your own
namespace because the likelihood of that
isv introducing an object that might
clash with yours is
high so use your own namespaces even
though you're extending somebody else's
functionality Lots lots of knowledge
lots of ideas now Alexander can you tell
us a little bit about our thoughts on
Nam
spaces
okay uh let's talk about um architecture
of our application and how Nam spaces
actually help us to make it
better because our first idea then we
discussed what we are going to do with
namespace implementation was pretty
straightforward Microsoft BS up
everywhere that's a
brilliant easy to easy to implement
suggestion we can run a script and we
can do it probably in few days but next
question was what is the value of this
if you do it this way and we have a
pretty large application with a very
complex structure and functionality we
have 7500 objects we have about 20 uh
application models which
are organized as a folders in Bas
up and we we have uh a lot of u local
functionality we have some other
modules so this is just a picture and we
have 72 uh first party
extensions long list and we wanted to
name space it all because if it if it
didn't then uh in the future this is
going to be a breaking change for
you so on a second
iteration we decided that uh we can use
our license guide we can use our uh
historical uh knowledge about uh our
product structure and we can actually
we talk about
wees it's quite straightforward we have
general ledger in a very middle of our
application and we have currency or
Dimensions as a kind of primary entities
which are used across application if you
remember a very old licensing guide that
was a separated granal for currency and
separated I think for dimensions and we
have uh VT and sales tax set up which is
common for all modules and the whole
application that means looks like layer
one should be Bank currency Dimension
general ledger and V sales tax so what
about next
layer uh on top of fin Financial man
management we have uh inventory we have
sales purchases payables receivables and
we have a lot of additional uh let's say
item related functionality for tracking
reservation warehousing or
transfer that looks like level uh layer
number two and of course uh layer number
two can use a general ledger to post
cost of operations or sales and purchase
documents and then uh we currently have
a lot of additional modules on top of
that like service or cost accounting or
manufacturing for example and it looks
like this is going to be our layer free
this is not kind of logical or physical
layer that's let's say on the first
draft it's a level of
complexity and actually if you have a
very big extension I would really
recommend you to think about how you
would like to use namespaces I mean what
kind of Dimension is most important for
you than you implement name spaces
because you can implement it for example
for table it will be uh Microsoft cash
flow
tables uh for Pages it can be Microsoft
cash flow Pages like we do for
extensions right now but uh for B up we
really would like to have a good uh like
a structural view uh on our
functionality and on our design how it's
organized and we know we have a lot of
Legacy code and a lot of Legacy design
patterns which are still in our apps
which provide like a cross dependences
between modules and uh we would like to
do something with
this so we also introduced key
principles how we can do uh Nam spacing
and actually reorganization of Bas up
going forward so first of
all uh we I expect to have uh General
g account and uh general journal in the
same name uh in the same or similar Nam
space because it's actually belongs to
same uh uh business process and to same
modu uh at the same time if I have
objects with very little relations to
other objects or kind of primary objects
for example post code I expect it to be
somewhere in a
foundation it shouldn't be very on a
very low level and reused by any other
modules in our
system and then
uh we should uh have uh object
dependencies going down not up that
means I don't expect that a general
journal posting contains objects from
sales or project or manufacturing
areas
currently this is the case but that's
not right and we also need to do
something and also we decided it's you
know we are all very experienced
developers we can do a lot of great
refactoring but we decided then we do
namespacing no refactoring because we
really need to uh get a kind of snapshot
of our actual structure and then analyze
it with name spaces and then uh decide
what's
next so finally we end up with uh a lot
of name
spaces so uh it's a finance layer and
here actually probably you see it
probably not from some some rows but uh
of course we start with general ledger
and we decided to use not more than
three level in namespace definition to
for example the longest one will be
Microsoft do general ledger do uh V do
calculation for example that means
Microsoft is default value for
functional area areas and then we have
not more than three
levels and uh on Next Level we have
inventory we call it supply chain then
we have projects and CRM and finally we
have our premium
functionality what is important here and
you can see a legend on the right side
of the screen that uh we have in green
we have uh primary business entities and
we expect that each module
contains a primary business entity for
example for inventory this is item for
sales area this is
customer and uh then we can analyze
dependencies between uh and relations
between uh primary like root entity and
other objects and then come up with uh
structure and of course there are many
iter iterations how we do this kind of
analysis but finally finally uh we
identified another very important uh
entity uh or let's say like a feature in
each modu we call it document for
example for sales this is a sales
document sales head and sales line for
uh job area it will be job and job
planning line for manufacturing it will
be production order so why we are doing
this because we have extremely large
number of case statements everywhere
where we have same framework of
functionality I mean we can actually
work with abstract so Source document in
VAR housing if we uh provide interfaces
to process specific calculations and
specific data retrieval and uh
modification for Pure Source documents
like sales order service order transfer
order whatever and I will show you a
little bit later how we are doing this
right
now okay what we can achieve with a good
structure of Nam spaces first of all we
have much better application structure
and discovery of objects this is just a
sample for uh general journal
Journal uh and uh actually for general
ledger and here we have J account we
have Journal then we have a posting
routine with some code units and finally
we have a g entry where we post uh
Financial entries so uh we have two
simple ways we can use IL Explorer and
we can search by namespace and we can
easily see for example uh where we have
where we are posting a journal line in
which namespace and where it's located
and another possibility then you use uh
vs code you can uh just uh browse uh
folder structure and our folder
structure for functional areas exactly
correspond Nam spaces that means it's uh
you see that it's a base up Finance
general ledger posting and at them
posting you see uh seven code units
which are responsible for this posting
so you can easily isolate particular
functionality or module and you can do
it physically you can do it logically
and then uh again you can analyze
dependency for uh this uh functional
area it's very easy uh I simply use uh
Visual Studio search because for example
I need to analyze if I use Microsoft
service or objects in uh
Finance you know with my current
knowledge it looks really strange and
should be changed but uh I just search
by microsoft. service in a folder uh for
uh Finance Bas up finance and then on
the uh right side of the screen you can
see that we current we currently have
some references in a preview posting
preview in a uh V
and also in invoice posting
buffer and uh it give us information
about uh let's say we can quickly decide
what to do with this we can uh check
what is the size of the problem and then
we can plan our activities for further
improvements
so and probably most important for us
and probably most important for you too
uh uh actually we have a legacy monolit
our old base up is uh kind of presented
on the left side it's not a real picture
it's just a kind of you know and it's
not AI it's just something but uh
usually you know people call Spaghetti
code I don't really like it for our
beautiful code and beautiful application
architecture but that's true we have
problems and uh on the right side this
is just illustration of much better
structure and if for example we will be
able to uh really build application
components which can be reusable which
can encapsulate particular functionality
it will give us a very well defined
interfaces uh for your extensions for
our extensions for your extensions and
then in the future uh we can uh really
uh I think uh do a lot of great stuff
with this architecture if you can
achieve it and we have to achieve it
actually in non-breaking
way right it's not easy it's actually
very difficult but we are working on
this we are thinking on this and
actually what this is what we are doing
right
now this is just a this is just a
visualization of uh uh our current uh
project we are trying to prepare for for
componentization of Premium
experience and uh currently we have B up
and it includes uh all I call it
essential modules like sales purchase
inventory finance and service management
plus manufacturing everything is cross
related there are thousands of
dependencies between manufacturing and
service management to other modules and
actually in both
directions which is uh extra problem and
we also have uh calculated fields which
uh belongs to manufacturing and service
management for customer for item and we
have a lot of uh tricky uh tricky
puzzles which we need to
address and we would like to uh we would
like to uh reorganize and refactor our
code inside of by inside of application
app that means this is not going to
change uh anything any references for
you we are going to will be the same I
mean it will be just normal obsolete uh
procedure as before but internally we
are going to introduce much better
structure and uh then service management
app we will be independent on uh
manufacturing app because currently they
also cross related which is a surprise
for me and then uh our Co application
app will be much smaller and more
efficient so this is just a like a draft
of scope what kind of object
we need to touch and refactor if we do
it for service management and uh
actually that's not all this is a first
draft in reality it's more work really
more more work but you can see how many
uh how many cross references we have and
here you can also see that we have some
modules like for example reservation
item tracking availability calculation
requisition and uh demand uh uh
calculation uh order promising a lot of
things and not only in inventory but
also in other areas which in the end of
this story should become like a source
document
independent because for example in
reservation
subsystem uh in a namespace uh Microsoft
inventory uh do
tracking there are no references to
service management or sales orders or
something think uh any other source
documents anymore it's just a framework
and this is extensible framework by
Design because we extend it for us uh
internally then we also extend it for
you uh because you can subscribe to same
events and you can actually uh use same
patterns from our code to build uh to
integrate additional Source document
into reservation system same is going to
be possible for reservation or for
availability uh and for all other uh
inventory areas very soon already in uh
current uh release
cycle
okay and finally just uh uh uh it's very
easy uh of course but just to show you
uh how we basically uh uh come up with
such kind of framework this is just a
sample about other promising client here
we have a lot of case statement which
actually list different Source documents
and do something in several places for
those uh documents and here we calculate
needed quantity for sales and service
and of course sales now belongs to
document uh sales document and service
belongs to service document that means
if we just Track by namespaces we know
how to separate it how to split this
code uh where to move uh new uh code
units which will be uh
subscrib with event subscribers to our
uh event here and finally we can come up
uh to such kind of simple structure
which is already uh extendable by
default we have just a uh event in right
on the left side on create
reservation on C needed quantity and
then we have subscribers which provide
that information that means this is uh
first approach which is I believe used
by uh most of you uh already for a good
time we also have interfaces we also
have a very nice feature a capability to
uh split uh object uh with like a table
with table extensions in the same app
that means we can
extract uh fuds uh responsible for
service management from item table put
it to table extension and put it into
Service uh management Nam space and
finally we can extract it from base up
and put it to separated
up and now uh a lot of theory but I'm
done and now it's time for Thomas to
show you practical work with name
spaces all right so let me switch over
to my laptop here all right so all good
let's see how it actually looks like
from Vis Studio code and our extension
so right now I have a here that are not
using namespaces and this might be the
situation that a lot of you are in and
you might already see um that you can
have igur references when some of you
introduce the same name uh on a object
that somebody else has done here so here
I have that this item record here exist
both in the base application and my
legacy app that doesn't use any
namespaces so what can I do about this
well in order to start using namespaces
I need to op into it so I'll specify
this namespace on my my file right here
and as we can see all of my objects are
now part of the name space and the fully
qualified name we can we can see right
here and my problem with the item uh
record here went away all good seem so
far but there's still a lot of errors in
my project so let's handle them one by
one so um stepan talked about that we
can either use using or fully qualified
name and in order to assist you in in
doing this we provided a code action for
doing um for specifying this so you can
specify the fully qualified name and the
uh the code action will now populate it
for you or if you go down to the other
one we can add a using for this guy and
now we are pulling in all of the objects
from this namespace
which means that I could stick to this
fully qualified name right here but it
doesn't really provide me any extra
value I could might as well just remove
it all well and good we now removed um
one set of Errors right here but my file
is not that big but this might might be
a bigger and bigger uh might be a much
bigger project so instead of doing that
you can of course fix all of the missing
using statements in the document the
project or the workspace so if we do
this for the document you see almost all
of my errors they went away I got a few
more using statements and I'm seems to
be in a fairly good shape right here but
there's still one error going back here
and that's the description two here that
is missing so what is this item table
that I'm actually
into um that I've referenced here and it
seems like it's just yeah my silly small
uh item table right here and it's not
the one that I wanted to use so how can
I figure out what's actually available
so for that we can use the a Explorer so
right now I have grouped it on type I've
typed in item and then we can go down
and we see ah here we are item table
there's both one from a base application
and one from the the other Legacy app
that I had dependency on and I can see
my legacy one didn't specify in
namespace but luckily the Microsoft One
specified one so now I can jump back and
I can start adding the US in or I can
fully qualify the item right
here but another
option is also just to retype it and
then we see the option here as well and
now when we go into it it will
automatically add the using and it
figured out which one to to pick right
here my code is now compiling all well
and good seeing all of these using
statements up here that can be a lot and
especially from the example that Stephan
showed earlier it it can take up a lot
of space so this can be collapsed down
um but again it will show up by default
but if you go into the editor there's
this folding import by default and if
you do that then they will be collapsed
when you just open up the
file thanks for that feedback from you
it came from you so thanks a
lot so now I have my app it's compiling
and I'm all good here so
let's go back again and see so what are
the restrictions that we have currently
on
namespaces well you can only have one
object of a kind with the same name in
the module so if I want to specify the
item table inside my module I can only
have one of those no matter the names
space the other restriction that we have
is that there can only be one object of
a certain kind with the same name in a
nam space so again this goes back to
stick to a namespace that fits with your
company and your projects and don't try
to reuse some for for other um other
Solutions out
there um because as soon as you Collide
you have the same issue as you have
today with ambiguous references and yeah
one have to rename so there's no good
way around this
one so a little bit of a fast questions
right here do we still need aex
registration yes we do this has not gone
away yet um we still working on removing
it for the top level objects um this is
a work in progress we are not there yet
um and we also have a some work to do
around Fields um where namespaces are
not used yet but let's see what the
future
holds so do we now need to register all
these namespaces that we are going to
use no we really don't want to be in the
business of tracking all of these names
spaces so stick to the recommendations
use your company your products um and
then there should be no need for for
registering all these so we really don't
want to do this but with all these name
spaces K I go away from
IDs well we still need them so so the
system is heavily baked into this ID uh
situation right here
and yeah we that is how it is for now
um and then what about the 30 character
limit well again there are a lot of
systems built around
this we can't really move away from it
today but who knows what the future
holds we we might see it
there um and then is it an breaking
change because now the name of the
object is now the fully qualified name
of it contains the name space and yes it
is a breaking change so how do you get
around this with the normal um
Absolution methods we have today so you
can still do a rename of the namespace
but it takes a little bit of uh work in
the in the Absolution here so these are
the the common questions that we have
seen so far but let's open up for the
floor for the questions that you might
have yeah now it's time for those
questions you want to ask up there
okay you where did you
thank
you thank
you try again I there go now okay you
said that um affixes were still needed
for Fields also for other elements like
actions
procedures Etc yes so any naming you're
doing in your appsource app uh would
require an AIX because then makes your
name unique right we're specifically
talking about the top level objects
Pages tables and so forth that's the
ones we're targeting first and we would
love to open up so you don't need to do
axes on those and then of course the the
fields would be natural next and then
controls and so forth but uh for now you
still need it at least a little bit okay
thank you
yeah all right
one over you get that to
show so you say that the rename in nam
spaces is a breaking change suppose you
want to start using them uh is that
allowed yes how can you start it you
should be able to just specify the name
space on your object and then you opt
into it yes so introducing it is not a
breaking change correct so it's only
renaming changing it there's the Brant
change Al so from nothing to a name
space that's allowed yes yeah okay
thankk you yeah
wel had one down
here um so we've seen that sometimes
this using plug can be very long and we
have two options we can fully qualify or
we can do this using statement yeah do
you are you thinking about uh partial
qualification like we can do using
Microsoft sales and then we could do a
record document Sal header for example
yeah yeah and and star using and all
these kind of tips and tricks yeah good
good feedback good suggestions I would
say when we see a using block like I
just showed here
um maybe it's time for reflection to
think about are we using good solid
principles are we using good designs
here because essentially what you're
saying with that big using statement is
I'm going to take a dependency on all
this stuff here that's my code unit here
and maybe there is a at least a room for
reflection there to see if that's a good
idea so for now we have not considered
are not considering adding features
where you can make like make it easier
to include more right I want you to be
very aware of what you're including in
your name spaces thank you
perfect one more question down here yeah
yeah come
when will it become mandatory ah good
question I wish I had a t-shirt
more so there are currently no plans of
making it mandatory
but I would expect that to happen at
some point we want to lift the the one
name in the entire app restriction that
requires that we kind of get rid of all
the scenarios where you don't have a
name space and we really don't want to
invest in things like making special
logic to figure out whether you have one
file in there that is not using a nam
space and all these things so when we
get that clar clarified I would expect
that we get mandatory name spaces yeah
absolutely th actually about making it
mandatory it's a good question and uh we
are not going to make
it uh because for example internally we
have uh base up and here we have name
spaces and we have have a lot of test
Automation and here we don't want to
spend our valuable resources to
implement it just to have it I mean we
want to implement it on purpose that
means we currently have it in a service
tests because we need to understand the
structure of those tests for our
refactoring effort right and we have a
lot of other uh folders with some uh
extra objects uh and some like demo tool
for example and and we have uh you
probably have the same structure and
that means you should really decide
where you need name spaces and where you
can easily live without Nam spaces and
probably it should be just a property
for example in up Json f file for your
up which actually control it that's
possible but make it Mand mandatory by
default everywhere that's not an option
not right now at least right yeah not
right
now so that's that's the discussion we
have having and the question around the
whole like default names spaces app Json
is also one we've gotten a lot and
decided not to do right now simply
because we want to be explicit about the
choices of Nam spaces
yeah one more over
there sorry uh so for current uh apps
that we have on the app source and all
the object names are with axes if we
start using Nam spaces can we remove
them or or rename the files or shall we
leave them so it would be a breaking
change as it is right now but obviously
we aware of that challenge uh but right
now as it is today it would be a
breaking change if you rename an object
and that doesn't matter if you're like
using name spaces or not right the only
thing that we allow is that you
introduce namespaces to an object that's
the only breaking change we
allow I haven't heard the the big
question do I need name all the way up
there
okay I'm want to wait with that one
that's a
[Laughter]
cliffhanger hello hello um Can this help
with the extension uh objects like
extension type type extensions to
somehow split them up by name name
spaces no so names spaces has no impact
on the runtime at all it is only for
your pleasure to be easy easily find
them right so you can find the objects
that are in the same namespace you can
categorize things you can understand
what belongs together you can make it
easier for people to kind of learn about
your features if they need to but it has
no impact on the runtime at
all so no impact on uh extension um
objects yeah just as as Alexander showed
here what talked about here is you can
take out a field from one table and put
it in a name different namespace in a
table EX exension and that makes it
easier to understand that this specific
field belongs in this functional area
rather than the other functional area so
it's just for your convenience so to
speak
yeah was there one more before we do the
Cliffhanger no okay so ah there was one
Saved by the Bell right come from the
back
here okay um the last thing is said so
if we extend a
table we and uh in that extension we
have another name space so when we are
using that table for instance we
extending the customer table we have to
provide both name spaces one for the
customer and one for the extension field
if we want those fields as well if I
understood you
correctly yeah so you need to specify
the Nam space for the original table
where it comes from I'm not sure you
need to do it on the field not yet yeah
yeah okay sound like good clarification
yeah so that's where the namespacing on
fields are missing in the table
extension you'll get that logical
grouping so you know that this feature
belongs there but in code you can't
really reference to that namespaced
field yet does make
sense okay I'll do the last one then do
you really name need Nam spaces good
question really good question obviously
from the comments we have have to
mentioned today and all the things we
presented we would say yes you need Nam
spaces obviously you need Nam spaces go
for it reality is
no so because it's not mandatory because
there are all sorts of challenges in is
enforcing that you don't need name
spaces right now but if you have a large
application like we do then it makes
sense to group things together to make
it easier for people who are consuming
your objects to find them to understand
understand them where those things
belong understand the dependencies
consider refactoring and all these
things so we would say yes but obviously
if you are doing a PT with one
customization makes no
sense right unless you hit the conflicts
unless you hit the conflicts yes there's
no other option good point yes but
yes yeah that's it for us thank you very
much thank you
