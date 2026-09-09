# NAV TechDays 2016: Bad habits of NAV Developers

- **Source:** https://www.youtube.com/watch?v=R28hrfg2MA4
- **Video ID:** R28hrfg2MA4
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 100m55s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

my first question was going to be what
the hell is wrong with you guys but you
are so many that I actually don't dare
to ask that question I didn't expect so
many people traveling so far uh or
facing the traffic of of anthrop in
Belgium to learn about bad habits
actually now um your bad
habits don't do that the thing is uh a
few months ago I I have de Dev veler in
my company and a few months ago he said
hey I've seen something on YouTube it's
it's a sessions a session from New
Zealand and it was quite a great session
I think that that would be something for
you for let's say maybe n days and okay
what is all about yeah it's about bad
habits I was
like okay thank you uh colleague so my
colleague was thinking like I had a lot
of bad habits now I don't don't want to
believe that so I turned actually to
Vio and um yeah I did actually be
careful careful what you say uh we set 5
minutes together and we had about 163
bad
habits and I can uh actually I can prove
that this is our this is our slide deck
and look at this number below
so if you were thinking you would have
the first beer this evening think
again I would like to ask you one thing
before we continue and I did this last
year as well uh with these lights I
don't see and we don't see anything of
you and so raising hand does make does
not make any sense so instead of that
clap hands once and then uh at least we
have some kind of picture on how many
people are actually answering uh
whatever question like who attended the
previous session about this new
developer
experience and who liked
it as many people it was exactly the
same right and that's why we clap
hands okay I have a story for you a few
years ago I um bought a
house and um it was not finished yet so
I wanted to hire a builder to finish it
and uh this Builder came in for the
first time he said to me oh this house
was owned by previously by a builder
itself and I said oh yeah actually
you're right how do you know well he
said often Builders live in houses that
are not finished yet and that was
actually kind of right and the same you
can see with chefs chefs rarely cook
extravagant meals at
home that happens a lot they don't spend
hours and hours to build meals or to
cook meals that they do at their
restaurants right and maybe the same can
be said about developers who
recognize good practice but maybe just
don't put it into practice in in
production environments all the time and
then you see reasoning like okay how can
we quickly fix this oh just double the
service or double the amount of memory
or things like that well does it work
I don't know how but yeah okay keep it
right
no now developers develop bad habits
because maybe first they practice
reactive
development do we recognize
that there is a problem I quickly need
to fix this or the unwillingness to pull
on loose threats
oh what is this if I if I if I would put
this line of code in it what what would
be the consequence I don't know or I
don't have
time oh most of you have
time yeah is valid uh something needs to
be fixed quickly or being created
quickly or has been sold in for one day
and you actually need to spend 10 days
this happens a lot
right
yes oh this is only test code it's just
a prototype it will never end up in in
production
environment yeah and often we as
developers we think like we create these
kinds of prototypes
right
but often they actually look like this
they are not really always the same and
not really always ready or ripe to for
production envir they might serve that
one cause that is tested but not all the
orders that are
expected Frank did it Frank you're here
is there any a
Frank okay that's good there was no
Franks because Frank will have done a
lot during this session but that happens
a lot I didn't write this code somebody
else did right so yeah
it is considered low
priority that is not not really
important so I do not have to spend time
on this actually most of the
developments we do is not
lifethreatening
but still if we do this for a number of
years the product might be full of these
non lifethreatening uh low Priority
Solutions which makes your um yeah
development or your solution be qu kind
of a complete solution of low priority
it's not a good thing management keeps
prioritizing silly rubbish things to
that stops people from doing their job
now
everyone yeah of course of course
development and management that will
never be a happy marriage it is just a a
fact but what about project managers
some the one in between you know what
they say right project managers think
that nine women can make a baby in one
month simple
mathematics and it's not the
case I can tell you I tried it Twi three
times anyway uh why is it important to
ensure that you don't do these things
well first of all you need to be able to
maintain your whatever your code Your
solution your product your customer
you need to be able to maintain it you
need to be able to read it and not only
you need to be able to read it someone
else need to be able to read it as well
right no I'm not
trying you need to be able to extend it
or someone else needs to be able to
extend it and not like
this decently
extended you need to be able to upgrade
it kids like upgrade customers like
upgrade as well we don't do we like
upgrades oh yeah do we like upgrades
okay I wouldn't have expected that
actually uh but we need to be able to
upgrade our
solution support we need to be able to
support our solution actually all kind
of like the same but as such you can
come up with an infinite infinite amount
of reasons why you should you should not
do the things that we were talking about
so let's talk a little bit about bad
habits
ofo did you do
it man no I don't want to take that no
I'll keep it so then you
start okay so uh this is a bit of uh
speed dating of bad habits so we have a
few that are a bit longer and a few that
are a bit shorter this is uh quite short
uh you see a lot of people trying to to
to run in this picture uh who of you has
never put a value in this field here
please clap it's quite Anonymous that's
that's interesting because this field is
very important it defines the offset of
your variables uh so and you know that
you can't have uh mixed offsets of your
variables they all need to be unique
although you never see why you would
need them and you don't see them in
practice practice there're a hidden
there're a property kind of hidden away
but they still must not overlap so the
first thing I do when I start developing
a new product a new project I go to
database alter and change the start ID
uid uh uid offset uh of the database and
what value do I change it to it depends
so everybody needs to do this all the
time uh you set it to the lowest integer
of your object number range in your
vertical that could be something in the
5 Millions whatever uh on uh Dynamics
365 for financials on an app it's the
new 70 million range that has been
assigned to you which could start at 70
million2 200,000 or whatever it gets
very interesting uh in customer projects
you know this this old on Prem thing
you've heard about that probably it's
still alive as Thomas said um so uh here
we differentiate because if we do
customization in projects I do it in a
different number range than the
customization that my uh customer might
actually do because he might have a a a
programming license he might do pages
and uh and and and reports of his own or
even add a table field so I work in the
60,000 to 90,000 range and I set in
these projects my development uh ID
offset to let's say 880,000 and if the
customer develops himself self he sets
his customer his his start ID uh to to
50,000 so that we don't even if we merge
that afterwards so that we don't have an
overlap of variable IDs uh very
important thing getting more important
when we when you think about extensions
and apps because if somebody runs 10 20
apps which will hopefully H happen
starting next year and we have
overlapping variable IDs that will hurt
that will cause errors even on Dynamics
365 okay so let's take a look at the
next one God objects have you heard of
God
objects very very few claps okay so I'm
pretty sure you have so uh what are God
objects these are It's actually an
official terminology look it up on
Wikipedia um that's an object which
knows or does or attempts to do too much
like too many things at once too much
data or has um too many methods inside
of it or something like that so I would
uh like to of course introduce like
typical uh God objects that we will
encounter in nav God code units God
tables and God functions and I have a
question for you so what is
this
anyone wow you all happen to know this
so the answer is is correct this is code
unit 80 but only the onrun trigger from
that code unit and actually all 1,247
lines of it in font size 2 so uh I I
believe okay in all honesty that that
was in 2015 I think in 2016 it's half
the size only so something like that
well uh kiding a little bit this is a
god object if you try to do anything
with this function like test this
function you will fail
so um let's move on let's take a look at
a god table what is a god table I'm
pretty sure that you have or some of you
at least have uh done those generic
tables you know that like look up for
everything
anybody okay yeah so they start as look
up for anything just so we don't have to
confuse uh consume too many table
objects and then you know they develop
into a Frankenstein because you keep
adding stuff on top of them so they
typically start like this yellow is the
primary key so some simple somewhat
simple primary key with one attribute
and then you remember oh I need more
things and then the primary key grows
and then some more things and then the
primary key and you know before you know
it you have a Frankenstein which doesn't
even behave as uh you would want it
to how do we mitigate this problem well
there are some good principle the
probably the best principle you can
apply to anything is separation of
concerns one function should do one
thing one code unit should be concerned
with one piece of functionality one
table should represent one
entity uh there should be no generic
attributes like customers ask for can
you just put those five Fields here five
text fields for me and then you know I
don't know what I'm going to use them
for but sometime I might need them so if
you don't know what you are going to use
them for then you don't need them and
when you need them I'll add them for you
that should be the rule or you can adopt
an um a line rule for example you say no
function uh has uh can be longer than 80
lines so you write 80 lines and if it
needs to be longer than that then you
need to refactor it like uh for example
what do you do then well you just say
move stuff into second function and call
it from the end of the first
function okay you do pay attention yeah
that's obviously not what you should
do
anyone anyone
um the next thing is actually uh
variation of the god objects it's about
collection code units and it was a very
novel and good idea 15 years ago uh like
when we all moved to uh from having uh
functions on tables to sort of
collecting them in code units so that we
had one code unit that holds it all uh
that holds all the um all the functions
belonging to one segment or if you want
one module of your uh application so
everything to do with sales conditions
everything to do with Freight
managements gets stuffed into one huge
growing code unit what happens you have
like uh code unit 80 by the power of 10
uh at some stage you have a mix of
global functions and local functions
which support these Global functions you
don't know uh what these which global
functions these local functions uh
support unless you scroll through the
code and search for them every time so
uh a collection code Unit A a management
code unit that collects all the
functions around one segment of your
application uh is not separation of
concerns it is the opposite of that is
is putting all the concerns into one big
code unit so please uh avoid that a code
unit must represent one method and one
method only so it will have one Global
function and the rest is local and they
just serve to execute that Global
Function One method one code unit
separation of concerns no God objects
yeah so um are you creating code units
like
that I let me give you a tip on how to
create a code unit like like
that contrl c that's Waldo's
keyboard there are developers really
that can have um keyboards like that and
just live from that and in uh in
actually a few years ago and not too
many years ago this was considered as
being good practice code cloning hey I
wrote it once I can use it again and if
I can use it again it must have been
good
right well
let's have an example like uh Co
document print code unit
229 um you know that yes of course you
do and it has got a number of methods
and one of the methods is uh print birge
header which prints the purchase header
Yeah clean function nicely said nice
nice description good but in the same
code unit we have a print service header
and that's not that different it is
actually quite the same yeah this is
code cloning this has been happening
quite across the product this has been
happening quite quite across a lot of um
um yeah products at in in in in isv
products we did this ourselves in a
previous version of our
product and uh yeah to uh elaborate on
this example this is actually uh still
the same code unit but all 12 methods
which does all quite the same and yeah
with a slight difference now um this is
a version of um our an old version of
our product which yeah contains about
eight more of these methods all copied
all slightly changed to uh yeah for our
specific need code cloning that is not
really a a good practice and uh I guess
Microsoft recognized that because um
they changed the document print
functionality a lot I think in 2017 or
maybe already in 2016 might have missed
that anyway uh we have Foo here as well
and fego has been uh blogging about an
Ki as design pattern and this a
combination of the using recra field
stuff using the variant facade uh design
pattern and yeah quite some steps Beyond
yeah so is a very polymorphic design
pattern to be as generic as possible
because that's what we're talking about
we need to be able to create generic uh
functionality and uh to come back to
this document print stuff this is how it
looks now we have now a print purchase
header this is the same function yeah
and it calls out to that that rec. print
or report selections uh. print method
which just contains one line but you can
see here this is this uh variant facade
design pattern where we have a variant
parameter that can get any kind of
record type and then you're
generic come coming back to favorite
topics uh and that is code on pages so
have have you ever put code on
pages yes uh and uh if we're being told
off for putting too much code on pages
we can always leave back and just say
say item
tracking and and then every of every of
us every one of our sins is excused
because Microsoft has given some bad
examples with that and uh I think that
maybe one of the reasons why item
tracking is not yet available on
Dynamics 365 but because it takes some
time to refactor that and it would be
necessary uh for that now um code on
pages you could say code on pages is
evil it is not always true but but this
thing here this example is evil we have
uh um a method that calculates freight
costs uh and we have an action for that
so we can click on it and then what do
we have we have business logic coded in
an onaction trigger uh that cannot be uh
properly tested uh that the test
automation for that is is bad it is even
hard to find it is not reusable but you
need to put it on every page so uh one
thing never put business logic uh in a
non-action trigger that is uh you you'll
find that in the standard application uh
still um so uh What uh oh we have we
have that twice here okay so what you do
is actually uh if you need to run uh um
a method run code from an onaction
trigger you point to a local function on
the page so that you clearly know which
methods are being executed on this page
and do not need to go through all of the
action triggers to find out this method
then uh points to its Declaration on its
class which is can normally be a table
but in an app scenario can also be a a
class code unit a code unit working as a
class and this will then call the method
which is a code unit on its own you
remember what I said about collection
code units each method is one code un on
its own so if you uh need to call uh
business logic from a page which happens
uh go to the trig to the onaction
trigger point to a local function point
to the class let the class point to the
execution of that uh method in a code
unit now um code you code on pages is
not always evil we have these examples
here in the onaf get record uh trigger
of the uh page sales order set control
visibility update visibility so we need
this code because it controls the UI so
if it's not business logic but if it's
code that controls the UI it belongs in
the page I mean we we we cannot even
handle it in in another way but it's
it's quite okay to control your your UI
with code on page it's just not okay to
run business a logic or code business
logic uh on a page also the unv validate
it's a variable the the dimension uh
code is a variable on the page so we
need to handle that with code on the
page um General uh strategy business
logic must not be coded on a page avoid
any coding on action triggers uh if if
that does more than pointing to a local
function um code which triggers business
logic uh by invoking a method on a class
is fine of course we need to do that uh
in few contexts this is also okay uh
especially when passing temporary
records uh to have code which sets or
return turns parameters uh to a page or
or from a page and of course code which
manipulates the UI is fine so it's not
always true to say code on page is evil
but business Logic on pages is
evil okay so apparently with all that
code in pages and copy paste and all we
need to do some
refactoring um do you do
refactoring good good this is a good
habit actually um what why do we need
refactoring recently I've stumbled upon
this piece of code um if you decipher
what it does within like um real time I
buy you
lunch real time is uh if you are the
developer who wrote this you do not
qualify okay um I'll I'll move on you
will not you will fail um did you ever
find yourself in this situation
really not not that much okay Waldo
apparently did
so uh let me introduce some myths about
refactoring the refactoring is actually
frowned upon by management they say
refactoring reflects lack of upfront
design well even if that statement were
true it would still be no case for not
refactoring we still if design is bad we
need to refactor but that's not the only
thing they say they say refactoring is
dangerous and destabilizes code
absolutely true if you don't have any
testability in place which you should so
uh or absolutely true if you do not know
what you are exactly doing so it's not
really dangerous also they say it's a
waste of resources can you just not get
it right on the first go why do you need
to go back and refactor and all why is
that necessary or if it works don't mess
with it it it's good enough well it's
not it's we do need to refactor so do
not be like this guy he may not refactor
but we need to refactor why is
refactoring important um because no
amount of planning can be substitute for
code writing there are things that you
will figure out while writing code some
specifics of algorithms that you will
figure out while you are in the middle
of it not before
also uh refactoring is actually a very
important part of the Red Green
refactor Cycle in in agile programming
uh or or test driven development so uh
you you need to do it this does improve
design it finds bugs if you go back to
your code and read it once again
critically while thinking what can I do
to improve it you will not produce more
bugs you're more likely to actually find
existing bugs um of of course
refactoring will make your code more
readable more understandable so that
when the next guy comes and takes a look
at your code they do not find themselves
in in that situation where I was when I
had to decipher that piece of code or
when Waldo this morning was looking at
his piece of power shell like what is
this so clean it up um reduce
duplication improve theability all
things like that can happen when you do
refactoring so it's not bad
refactoring is actually perfecting so
keep calm and refactor away yeah but in
a way I can understand that refactoring
is not always the top priority in your
organization uh remember that slide on
the management part management might
prioritize different things and uh so
maybe it's a good thing to also give
some names on the quality or on uh the
way you code so let us do
that what do you think what quality of
code I'm talking about here spaghetti
code right yeah and we know spaghetti
code spaghetti code is that unstructured
code that probably Frank has been
writing yeah and you need to support uh
unstructured functions everything may be
in that one code unit of Gary uh very
undocumented insanely documented might
be a case as well in any way spaghetti
so something you just do not want to
dive into and maybe the software looks
fine but when you enter it it is just
one pile of Chunk right it's that kind
of coat that you measure in the number
of what the per minute
yeah so talking about spaghetti coat we
might want to talk about something else
as well
like lasagna code
lasagna code is when you are
layering an
insanely amount of times like you can
call it a x code as well for instance
but I didn't tell you
that is one example now this I don't
want to believe this is an insane amount
of layers but still layers Gary has been
talking about layer development as well
with where we as as our bottom layer our
um um metod unit this is kind of like
the same where on bottom layer the
method code unit but on our page we have
the top layer and we go down yeah
layered coding do not exaggerate but
still it is a good practice at some
level and then again I'm still hungry
what is
this ravioli
code and in this case we're not talking
about layered code in this case we're
talking about modules and
putting stuff in insane amount of
modules again maybe this uh walbot thing
uh where we have two modules as maybe
already real uh ravioli Cod um because
yeah why would this very small tool have
two modules
already but anyway modular design is is
good exaggerating with it obviously is
not
that you belgians have like uh I like
meatballs for example is the meatballs
spaghetti with
meatballs why
not spaghetti with meatballs coat does
exist as well and is actually an
official
term and it is that code that
transferred from old to new transferred
from a procedural environment to an
objectoriented environment and then you
get both all these procedure spaghetti
and all these objects like me balls so
yeah um that's actually all pasta dishes
that uh that I uh good good I can't
stand that food
anymore um so uh let's take a look at
another thing that often happens in uh
in
practice branching on strings so the
title was missing I don't know why so
did you ever see a code piece of code
like that
like yeah I actually stumbled upon that
in one upgrade project so if vendor
number was this then validate a specific
discount so I asked the guy who wrote
that piece of code like okay can you
please explain to me why did you do this
he said well this company does most of
business with this one single principle
like 90% of transactions are bought from
them and they always have this discount
so this was the easiest way for me to do
it except for like 15 other ways of
solving that properly this not counting
into them this ended up up in production
um I've stumbled upon a similar piece of
Code by Microsoft as well but I'm not
going to show it here you know I still
have friends there so um this is another
example that you might have seen in
production
anyone yeah like case and then some
kinds of actions or or something so this
is also a bad thing why is this a bad
thing why would that be a bad thing
because in C we do not normally have uh
uh many better options or at least we
feel we don't this is extensible strings
are extensible options are not so maybe
this looks like a more feasible design
but it is not so um there are several
layers of sorry not lasagna of problems
here first is data volatility depending
on where those uh captions come from
they may be strings from database or or
anything else your condition might may
not hit or may miss or maybe it it it
happens at at the wrong moment so you
get a bug then it may be case sensitive
for example you create a piece of code
which expects that string that comes in
will be code and it actually comes as
string it's not uppercase and there you
go and you fail to check on that or it
can be multilanguage so you you test in
in in Danish and text comes in in
Spanish and suddenly you have a problem
and finally last of all but not not the
least of problems is it's hard coding we
don't do it like that it should not be
how how we should make or test
conditions inside of code so if it's
absolutely necessary use constants so
this is example it was brought to my
attention that it might not be the best
practice and I do agree so instead of
constants use functions so instead of
having a constant called method insert
item do a function fun which returns a
text and then it's text inside of that
function and you can test against that
and then if you have to test against the
same string in multiple uh objects then
you can always call into that code unit
which returns them so this is an example
how to handle this so this is not
something you would normally do or
better yet all of these test against
some string things indicate the need for
some kind of polymorphism
so there is a different Behavior going
to happen depending on what is the value
of certain setup thing or something that
comes from database or similar so uh
instead of either doing functions or
trying to make options or anything do a
pattern like in na we have a facade
pattern it's good enough polymorphic
enough and easier to write also easier
to follow and more uh more sturdy more
more more resilient to to any kind of
breaks or apply a handled pattern now
that we have events why not handled
pattern is also good or there are some
more difficult pattern uh patterns in
Cal but we can still try to apply them
like Factory pattern or command pattern
patterns are your friends so always pull
them out of the bag if you can
so y
so time for something uh to talk about
something that I'm actually quite
passionate about uh but I'm going to ask
you a question first what is the
big what is the nicest or the big thing
what makes nav so
special
what openness oh yeah that's the right
answer openness flexibility the fact
that we
can fix stuff right in development or
our live environment is that openness
for you
that's quite open right I can if there
is a problem I can go in and fix it and
be a
hero well that's a bad habit development
in life environment your life
environment is a labo your life
environment is is should be spotless
your life environment is not a
development environment keep your
development hands off this life
environment do you agree with that or
you say you're
exact oh thank you so much but did you
ever develop in life
environment I'm sure you did as well
because sometimes you actually just need
to but in a lot of cases it's just
easier but you don't really need to and
development in life environment is
actually do you know the the movie uh um
how is that movie The rers of the Lost
Arc of Indiana
Jones whoa yeah so this screenshot
doesn't mean anything to
you but actually this scene was actually
yeah he needed to replace this statue
with this sack of uh of sand in one go
and he had one chance else he would have
been in thousand
pieces that's development in life you
have only one chance and it better be
good because else you're no hero you're
anti
hero yeah so uh let's just consider
[Laughter]
this if I'm deleting a header does not
delete my lines oh let me quickly fix
that this is this is I just did not uh
come up with this this actually happened
yeah and I was very lucky that I had a
backup to help that customer back that
backup was 15 minutes old that lost 15
minutes of orders
yeah that's development in life so uh
you will do unrecoverable mistakes you
will do it's just a matter of time you
are not special enough to never make
mistakes we are all human I hope um I
know I am so you will do eventually some
mistake that you will really regret I
remember actually uh another customer
that was an uh that was not our company
that did that luckily we were with two
nav companies uh at that customer and
all of a sudden this this Warehouse uh
keep piling up with with with radiators
that was uh it manufactured radiators
and what what was happening it was
piling up with radiators we are
manufacturing these things and it is it
was make to order not make to stock but
it's manufacturing these things and we
don't know where it comes from well one
one one mistake we not we
that other
company was taking not the remaining
quantity it was taking the quantity as
being what had to be
manufactured oops wrong field 15 million
EUR that uh that
cost so you only have uh one chance you
need to have a development environment
you need to test stuff this live
environment just do not do that and
obviously you need yeah you need it in
Source control anyway and there is no
way that you develop in live environment
and you get it in your Source control
that is just no
way so one of the things that often
happens in live environments is uh one
specific
command this
command you know that
command
okay have you ever seen
this okay so what do you do when you see
this let me tell you what you do when
you see this you do exactly what it says
it says use the commit function to save
the changes before this
call so it tells you what to do so you
do that right and when you do that you
know what your code looks like it looks
like this only five commits in a single
function the problem is there are more I
just couldn't take the screenshot so
that they could be visible there are
five more actually so
uh things like that do happen and this
is a problem so um of course I'm not
trying to say that commit is an invalid
thing to use there are valid use cases
for commit why do we have Commit in the
first place to release the resources so
yes if we have uh some situation where
um a lot of resources are locked maybe
we should think of how to release them
as soon as possible so that whoever else
needs them can take them uh for
themselves especially like in long
running transactions you could do this
commit let's say after every posting
group has been posted you commit or
after every one item has been adjusted
you commit so that uh other people get a
chance to work with uh or if you have
some queue processing perhaps you have
some asynchronous filling up of a queue
with certain things that need to be done
and then some process is running through
that queue maybe that process should re
commit after every item has been
processed so that it doesn't prevent
people from from inserting into the que
these are valid use cases for uh for
commit what are invalid uses use cases
for commit pretty much everything else
so especially this is an invalid use
case for commit so if you see that uh
you should refactor you should not put
commit in there um I do a lot of
trainings and in those trainings I
always tell
developers if you write commit you need
to cut a finger off your hand so you
know what happens then well
developers evolve hands like that
so let's talk about
uh let's put my microphone back on uh
let's talk about posting and let me
before we start let me wise crack a bit
this is uh a scene from uh one of the
most famous Renaissance frescos it's you
can find it in the bran cap Chapel in
Florence this is a a fresco by a guy
called maacho and what do we see here
this is a scene from uh from the New
Testament and uh we see one of the
disciples paying one of the tax guys
from the king from the from the
government if you want and how do we
know that this is not just a private
transaction but really paying uh the
governor because it's being posted and
that's why the post is there this is a
word play that even works in Latin and
it still does so this is an indication
that official authorities are being paid
and the and the amount gets posted later
on this is by by Design here so let's
talk about posting about two uh um
topics uh when when doing posting one is
doing additional posting in the
background for instance if with a
transaction be it uh a shipment or or an
invoice posting you additionally post
some planned cost or whatever other uh
uh stuff in the background and then we
talk about the posting pattern the
general posting pattern and what can go
wrong and right there um additional
posting I have seen this setup uh quite
a lot of times and even uh people in in
in companies that I've been worked
working for have done that uh you want
to allow some additional posting in the
background and of course what you need
to do you need to let the user Define a
general journal template and a general
journal batch name to which he posts the
additional stuff uh is that correct clap
your
hands okay uh it it might be it might be
but in like 95% of the cases uh you
don't you don't really need it because
in most cases you should not fill a
general journal and have the user post
it manually on no account should you
insert general journal lines then post
them in the background and then delete
them uh because you look at what is
happening in code unit 80 and 90 and
similar Co code units you only use the
general journal line as an argument
table like in 80 or 90 but you don't
need to fill the primary key for that 80
and 90 does not write to uh to general
journal lines it just fills it and then
you also don't need a general journal uh
uh template name or a general journal
batch name you don't need to insert that
it's just being filled in the background
and the primary key is left completely
blank but I've seen that happen like the
way I um I I've shown it here uh with
with the user needing to specify uh a
template name and a batch name a lot of
times uh one other uh background to this
is you don't want to take the blame for
posting you just want to create physical
journal entries and then have the user
posted uh uh himself so whatever goes
wrong there it's the user's fault um
very clever strategy but uh especially
on Dynamics 365 especially in an app
situation where you have untrained users
who wouldn't know that they need to go
to a journal after they've done a
transaction and post that because it has
not been posted yet this becomes
increasingly invalid so if you do
additional posting in the background
just do it within the transaction and
don't uh kind of blame or put the blame
on the user to Define uh uh a journal in
which you write uh any lines that he
needs to post manually and as I said if
you don't uh uh if you post it like in
code unit 1890 you don't need that uh
let's go to the posting pattern and I
think uh we we all know this and have
seen this uh you go from a document to a
ledger entry finally uh and and how does
that work you don't kind of post the
document line uh immediately to The
Ledger entry uh but uh either you go to
a journal line directly and from the
journal line uh to the to The Ledger
entry or you have an invoice posting
buffer in between why do we need that
invoice posting buffer because in some
transactions again 8090 and similar uh
you don't post line by line but you uh
sum up a few of these lines and then
transfer them to a to a to the journal
line that's the general idea of how
posting Works in nav and I think if
you've added a field to the uh to the to
a document line let's let's say a sales
line and want you want it to appear uh
uh on the item Ledger entry or or the
the general journal uh uh entry uh you
have done that a lot of times you have
Faithfully put your new field in the
sales line promoted it through the
journal line to The Ledger entry line uh
I hope that what that's what you all do
don't you yes of course you would but
and I kind of don't know if if all of my
code uh is so nicely written we need to
keep into account that not everything is
posted from a document directly so uh
whatever you can do from a document you
should be able to do from a journal as
well without having the document uh up
in front so you should be able to just
go to a journal line post it and get the
correct Ledger entry and if you've added
Ledger if you ever if you've added logic
or a field to the document line which
goes through you need this uh field to
be visible and this business logic to be
available on the journals as well so
that you can post it uh without needing
to go to to documents that's quite
important and in some cases neglected uh
have you ever kind of neglected that as
well come on be honest yeah thank you
thank you uh I would give you all a
t-shirt but there are too many um also
there are not okay there are too few
t-shirts not too many people um also
what I find uh we are pretty good on
improving orders like if I do new bu
business business logic uh I do it in
order in a sales order or purchase order
and I uh I really code it very nicely
and diligently and everything looks
looks good but I tend to neglect the
other documents I even tend to neglect
the invoice document and the and the
credit memo document and sometimes uh
the logic needs to be there but in a
slightly different form so say ah come
on go through orders and forget the rest
just too much work um same thing is with
return orders uh you you might get back
what you've uh what you've posted so the
logic needs to be there in return orders
as well and you need to ask yourself do
I need to prepare for that logic maybe
in quotes and blanket orders as well is
is that already is that business logic
already present in these uh uh in these
documents uh these document types so
that it gets taken over when you create
an order from from a blanket order or or
an order from a quote so be consistent
and be coherent like uh look at all the
document types not just uh the order
which is which is the most uh striking
example and then again putting a new
field in a sales line for instance
doesn't really cut it you need to
promote it to all the uh uh to all the
tables that follow the the the sales
shipment line the sales invoice line the
sales credit memo line the return
receipt line and also the SE the sales
Arline archive you need to think about
that sometimes I I do that now like for
for the last five years or or six years
I've been doing that routinely but
sometimes we just neglect one of these
posted documents and then we don't have
this this field afterwards and also if
you develop a a business Logic for uh
sales order think about couldn't you
also need it in transfers and assemblies
isn't there if you need it in sales and
purchases might there not also be uh a
need for this business logic and these
fields in transfers and assemblies so if
you're doing a vertical if you're doing
an app think about that in projects
maybe you have more freedom until the
customer really demands
it can I have a um I have a
question who of you think or finds by
themselves
or have or has adopted power
shell so you have really you are solving
your daily problems with power shell
yeah who
not that's a bad
habit avoid using Powershell is a bad
habit by the way this not a
recommendation yeah if I talk about
power shell with people they they
usually act like this like
no not Power Cell that's a disease it is
not a disease it's actually a
cure and if you if I would be talking
about power shell I am actually more
like
this to be honest now I'm going to do a
whoa a demo that's really big uh why I
actually think power shell uh is there
for uh to really yeah make Our Lives
much more much easier uh this is
actually just a small uh demo script
um is that screen big enough it
is okay this is a small demo script um
just to show you a few things now uh why
I asked my question like that adopted
power shell there is a big difference
between just um using Powershell once in
a while and really adopt it create your
own functions and really make it part of
your daily life this is just a few
examples that should show that is part
of our daily life on our company um
first example not going to execute this
is one that the camil has created is is
one that downloads the cumul cumulative
update kind of easy right so just
imagine that you have a function from
the moment that you read anyone's uh
blog or or Microsoft blog that says hey
there's a new commu of update enter it
starts downloading yeah or maybe a
service that checks that every day yeah
and then you come with a second function
that creates from this download an EO
file a
DVD something that you can work with
install use it your customers whatever
you want to do with that and then you
have another function a third function
that says okay I can install from this
EO three functions you download and
you're already installing or that Ford
function that says
repair repair why would I ever want to
repair my
installation because nav doesn't break
right well um repair is quite actually
quite interesting option when you want
to upgrade to a new cumulative update
you have two options either like you you
have a few options you can just
uninstall your previous installation and
just install the new update or you can
get all these files and replace your
server with these new files and your
clients with these new files or you can
repair simply repair with a new version
of the DVD and it will replace all your
service teers all your clients for you
quite easy so with one repair function I
can upgrade from One cative update to
the
other uh and this is just uh a script
where I have been uh uh using this uh in
production which actually means
personally here on my uh PC um where I
actually if every time I install a new
version of any uh nav version 2016 2017
the cative update whatever I
will export objects why not I mean
you're already in way for 15 minutes
wait for a few minutes more and let it
just export all the objects of this DVD
and let you build in a background maybe
I have it here yes I do have it here an
object Library this is a zipped object
Library I have all my versions all Mya
of updates just ready sitting there from
the moment I want to create Deltas or
whatever scripting Power Cell makes your
life easier or this one create your own
functions to in this case copy an
environment which is going to set up
Port chairing sh I didn't say this port
chairing doesn't work not supported on
Microsoft actually it does work and you
should use it on your development
environment just to not use it at your
customer side uh but anyway for for
setting up development environment is
quite easy and this is now for instance
backing up a database setting up a new
server instance taking care of the uh
the uh the the the security and all that
you think needs to be done um for
setting up an
environment this I execute about daily I
will for instance never touch an default
environment I just copy it quickly just
one line of code and then I can just do
whatever I want to do there yeah test
out or whatever this is
another function Gary was talking about
this uid
offset well manage it if you set up your
development environment on your local
system or whatever manage your uid
offset make this function part of your
setup script of your development
environment or whatever else you need to
think about it now you don't need to
think about it at all it's part of your
script it's part of your how you set up
your uh development
environments um yeah this I want to end
with apply nav Delta now you know what
Delta
is okay you know what the Delta
is okay this Delta thing are you really
using that in your daily
life not that many people are using that
in their daily life because it's quite
combersome we have got text files we got
fob files which we will see later on um
and it's easy right I can just take it
develop an environment import done cool
well in Delta I need to actually export
all the objects I want to apply the
Delta for apply the Delta it's all power
cell and then I need to import it
compile it it is quite uh quite work
actually personally I always only work
with delas and then you have a function
like this that just is going to analyze
all the Delta files you want to apply
export them from the target instance
apply it import it again compile these
are just steps really easy SC but it
makes you being able to use Deltas as
actually just text files and there is
possibility of reverse Delta right and
there is a possibility of reverse Deltas
absolutely um you know what the reverse
Delta
is it's it's kind of a neat uh thing um
thank you I'm not prepared for
this the reverse Delta is actually just
the opposite of the of the Delta let's
just assume that you modify the field
you now you added the field so the Delta
says hey you added the field if I
reverse this uh comparison then it would
the Delta would say he you deleted the
field so just assume um 6 months ago you
uh merged an isv product with that
changed 900 object in your default nav
environment and 6 months later now you
decide oh this IC Solution is crap but I
have been adding stuff to this
environment as well and and and and do
these 900 objects as well and I actually
just want to remove this isv
solution this is an actual case that we
had in our company and it was a
10-minute job just by creating the
reverse Delta we imported it so we had
our we always have our original our
release where we implemented it we had
that text file from the isv so what we
did is
just uh reversed the the Delta and we
applied that 6 months later to our
environment and it beautifully just
removed this isv solution I'm not saying
that you should always remove IC
Solutions but anyway that's a way uh how
you would be able to do that so now you
always all have these kind of faces
right okay so keep calm and learn power
shell good so now that you uh you have
learned a little bit about uh deltas and
everything thing uh why are they useful
if Waldo didn't convince you to use
Deltas then let me convince you to loose
to use Deltas so let's talk a little bit
about fob who uses
fob more than Deltas really come on come
on what what do you the rest of you use
text so what do you use
then it must be fob come on admit it
okay so um I'll just make a bold
statement fob is
dangerous bad and let me prove that to
you so uh here I have all this
development
environment and I'm just going to start
development here
see okay okay yeah Power shell I
executed he I double click an icon he
executes a Powershell script so use
power shell yeah just to be in the right
envir use power okay so I'm now in my
development environment and there is an
fob file that I've got from my
partner and you know at that partner
company uh whose customer I am there was
an a very angry developer who decided to
quit his job but I don't know that so I
just go and I say import
fob and there is my login dialogue I
take a look well just login dialogue
nice and then you know I'm smart I
always check the code that I import into
my database so I go to this
page
login
dialogue this is a zerty keyboard come
on does it even exist okay so yeah there
are a couple of fields let's take a look
at code
behind what's happening inside of this
uh well some validate passwort policy
very simple function good I'm happy good
let's go on a page man come
on I'm just saying yeah let me run this
page let me see if it works
actually some I'm try to log in to my uh
Office 365 or something dyamics 365 or
my banking
system what's happening have some power
shell to ah okay okay so there is my
login dialog username uh Vio password
it tells me I just stole your
credentials
loser and let me tell you something else
if I take a look at one folder here at
the
root how do you go to
root okay thank you there is temp and
then there is this stolen credentials
file if I take a look inside I'll see
that it has username Vio and password
whatever I I just typed in so I'm
confused where does it come from so I go
back into this file I take a look into
it and I don't see any offensive code so
I want to check it so I just go and I
will close this and Export it as
text so
text
whatever whatever I would attempt to
write I would fail
so and then let's take a look at this
text and if I try to search for uh
sto I don't I cannot find this text I
stole your credentials loser and it
doesn't use any fancy. net interrupt or
anything like that it the code is just
not there so where does it come from
where does this piece of code come
from apparently it has stolen my
credentials so where does it come from
from fob file because you can put
anything into
fob uh and hide it from uh unsuspicious
users so fob is not what it looks
like what you import into your database
is not necessarily what will
execute and that's why fob is dangerous
so if F fob is dangerous what then well
we can handle text we can uh always ship
text files with fobs uh we can use text
files if at all possible we can compile
if I was smart enough to compile that
object after I imported it that would
have solved the problem but you do not
always compile things so that's why my
recommendation here would be do what
real ninjas do like Walo use Powershell
take Powershell and handle deltas and
you will not have problems such as that
and do not download any fob from our
blogs you
know too
late well woad now you said that we you
really make me happy I mean come on he's
using Power Cell um next uh
topic let's consider
this of course who agrees with
this let me re reread it
actually do you really agree with
that who agrees with the bottom
part it cannot be stolen that's
good who agrees with the top
part okay there are are a few people
that actually agrees with the fact that
real programmers don't uh comment their
code code commenting
uh in a way you could see it like
deodorant what do me that well um code
commenting is a little bit like hiding
your code
smells hiding the fact that your code is
actually not structured enough so it's
not structured enough so let me put some
comments so I explain what the structure
should have been yeah so that's why I
always say don't comment if you should
comment that means that your code is
actually not structured the way it
should be structured now take this
example um seems like a nice function
there a little bit more than 20 lines
but anyway um a little bit it is not a
nice function not because it's commented
but the comments were quite needed we
have quite some nested things here like
Nest number one Nest number two Nest
number three Nest number four Nest
number five this is not good practice
and you could have um done it a little
bit like this this is the same code
first view on it is like oh okay I need
to find my way here actually you don't
because actually you only need to be
able to read the first three lines that
is the structure of your code the rest
is just like local function that is
executing it the readability is on top
of your uh method this is actually a
method an example of a method code unit
that uh Gary is talking
about let us take this
example it is Dutch to begin with I hate
Dutch I like
flamish I hate the fact that it's not
English it should be uh English always
and yeah this is this is really a
production environment um um that is a
really long function and there was only
one solution that was documenting it
because no one was able to read the
bloody function and uh yeah you see what
happened now there's more more comment
than that there was actual
code
another what is this this again is a
production code or a real code from from
an example I don't just spit this out of
my sleeve and what this does yeah what
you see here is actually um yeah what
could have been seen as uh Source
control this is putting stuff in Comon
because you actually don't want to lose
it or tell someone else that you that
the previous version had this line of
code and now it doesn't anymore who does
this so actually the same question would
be who does not have Source
control if you have Source control you
don't need to comment your code like
this your Source control comments your
code like that there you will see that
the line was
deleted and you have like places that
have been commented three times I mean
come come on another
example unwillingness to pull on loose
threats kind of
thing oh I do not want to delete this uh
so I just put an error there and if the
error would pop up probably the customer
would contact me
and well there are a number of reasons
to do this a simple compile would
already has have given you uh some
information on uh what would happen if
you were to leave
this there is one particular thing that
uh we are almost forced to do there is a
so-called anti- pattern loopy loop have
you heard of a loopy loop you have okay
so it means I need to introduce it to
all of the rest of you so this is a
loopy loop this is a nested Loop pattern
so it's not a pattern so we have one
outer repeat until in which we do uh one
more repeat until which is filtered in
which we have another repeat until which
is filtered and then depending on how
many rows in each of these Loops there
are there can be a progressive number of
queries sent to the database so imagine
this is customers customer Ledger
entries like thousand customers each of
them has thousand Ledger entries so it
may result in a
million uh queries so you don't want to
have million queries towards your
database so that's why loopy loop is not
a good thing and unfortunately our code
is full of loopy Loops let me see who
agrees good for you the rest of you who
don't write loopy Loops so loopy Loops
has many
faces um this is another phas of loopy
loop this is a report it's so easy to
write a or to create a report just to do
loopy loop so whenever you need to write
a loopy loop you do a report it's
quicker
so you don't have to write all that code
so you write it quicker it doesn't mean
it's going to be more efficient towards
the database these kinds of things are
slowing down performance the most so
especially if you try to do any kinds of
wrs inside of the loopy loop
um why is it bad well the records are
not retrieved from the database in the
most efficient way you take one customer
and then for that customer you send a
select give me this customer's entries
then you get them for these entries for
each of them give me detail Ledger
entries and then you may do some more
like you you you may try to look up uh
let's say item Ledger entries and
whatever it is endless and so many
queries each of them is not particularly
efficient because all of them have to
set some filters have to go to the data
and very likely SQL Server will not
properly have all that data cached to
return that to you in most efficient way
so you do negative L affect performance
there is one more thing that can happen
there can be this next from hell have
you heard of next from hell you do next
and you end up somewhere so if inside of
your loopy loop do changes on the data
especially on the key of of the record
on which you're looping your next may
put you somewhere outside of a loop or
worse it can put you back at the
beginning of a loop so you end up
repeating the same Loop over and over
and over again and you don't know why
this is happening so obviously this is
not the the most efficient way to
retrieve the data from the database so
how do we do that then so enter the
query object have you heard of
query yeah okay good do you use Query
wow good job so I assume those claps is
the rest of you who do not do loopy loop
why is query better well clearly it is
designed to execute as a single select
statement so no matter how many
different tables you involve you will
create one single select statement that
goes to SQL and SQL is optimized to
handle those no matter how complex they
are SQL will do that more efficiently
than a loopy loop can loopy loop is
designed for a different kind of
databases this is designed for SQL
databases there are obviously some
drawbacks of using a query queries are
not cached which may be a good thing
imagine that loopy loop there is one
more adverse effect of a badly written
loopy loop or a loopy loop that does a
lot of things that's precisely the
caching you know when you run any kind
of data read operation you know what's
uh what the NST does it cashes that for
you and if NST does not have enough
memory to handle all the caches what do
you think it does it flushes the old
cache so your loopy loop aside from
being very inefficient toward SQL Server
will also probably flush all of your NST
cache data so that whoever needs
anything legitimate will have to select
again from the database queries do not
store their results which means they
will not negatively affect either
performance of the SQL or performance of
the NST and typically loopy Loops are
not operation that you do all the time
you you do them once per day or maybe
once per week you run something that is
loopy loop and then it will not matter
if that data is not cached so do use
queries and do not shoot at us so who of
you codes for
fun okay sometimes we also need to code
to fulfill a business process now this
is a business process here how is it
called
good it's a Mexican standoff exactly you
and I know that you come from Arizona
just just by that that that that earns
you a t-shirt uh so uh the Mexican stand
UPF gives you a t-shirt okay so we have
a business process that we need to code
against uh sometimes we do not as
developers probably have a complete
overview over the business process or do
not understand it completely has that
happened to you
okay so if you have no clue about how
the business process
works and if the Consultants have no
clue
either and uh if your product manager
doesn't have a clue either there's
always a very easy
option shift the responsibility to the
end
user it always works so just to a setup
like like that uh posting
Behavior let the user choose whether he
wants to post with vat or not vat you
know uh doesn't matter that there is
probably a regulatory feature behind
that that calls for one or the other
you're not to blame the user takes the
decision let him use how he wants to uh
calculate uh a search charge between
Formula 2 or formula 72 or or 95 and if
so Formula 2 hasn't got any code anymore
it's his fault you should have chosen 97
come on everybody knows that all of our
Consultants never choose anything but
that set the posting date to today in
what circumstance how does that work
correctly and so on and so on I've seen
setups like that uh uh more than 10
times in my life if you don't understand
it just kind of program all the
possibilities we can do everything let
the user decide perfect now the problem
is of course and maybe some of you have
seen the the movie to be or not to be by
an luit where this standard line
Shifting the responsibility on me again
Schultz comes up every time so you must
not shift the responsibility to the user
you must not make him take decisions
that he cannot responsibly take you own
the business process you need to need to
work make it work in code uh it's your
responsibility to make the the business
process
consistent uh legally sustainable and
easily explainable all the more so in
app scenarios where we meet the
untrained user he doesn't have a clue
you need to uh to provide the endtoend
business process to him setups do not
Define a business process never they
just Define slight variations within a
business process so what number series
do you want to take so setups need to be
understandable for end users in business
terms in the terms of his business and
not in our technical terms that's not
always easy but that's what it's called
for okay so there are more bad habits so
database operations do we do database
operations so all of rest here just
watch as others do that
right I'm pretty sure you do right
database operations let's take look at
this one you should not do these unless
of course absolutely or totally
necessary why do you know
why do you know why these are not the
best way to write things yeah okay I
assume you don't need to say just clap
your hands if you know there are very
very few hands who who who clapped so it
means the rest does not really know what
happens well these are dangerous because
they execute immediately against SQL
Server so if you do that in a what did I
say loopy loop was called that thing
then it will be thousands after
thousands of insert modify or delete
that go to S SQL Server individually and
come back individually and that's a lot
of ping pong happening between NST and
SQL so if you do not absolutely need to
know the result at SQL Server right now
then do not check for that you know uh
what can make a database operation such
as this fail why does insert fail
because of primary key violation right
so you know what let me tell you
something primary key violation will
happen happen in 5 minutes after the
loopy loop has completed as it will
happen now so if you send it now you
gain nothing so when you run a big loop
of operations and you do not ask for if
not insert or if insert then all of them
are queued and executed as one big batch
and what would fail at the early moment
will also fail at the late moment so no
different Behavior will happen you don't
really gain that much you just think
that you do so this is why you should
not be doing those of course if unless
you absolutely know why you are doing
that judging from the number of claps
I'm pretty sure you should not be just
writing these you should just uh abandon
this
practice finding stuff there are many
different ways how you can uh find
things well the first piece of code is
probably not what you want to do if
customer find first then repeat until
well if you find first then you find
first you do not loop after finding
first because this is sending to um
select statements the next one may be
better cost find minus and then repeat
until the last one may be the best
however this is not always like that you
should be aware of what does one do and
what does another do this middle one
it's not really
obsoleted and you know it's really not
find first it means more um what is the
difference find first again does not
equal find minus find first selects the
top one find minus does not equal find
set either find minus reads the first
batch and then if you do a loop over
that first batch and if there is a
chance that you may exit before this
first batch is consumed assumed there
will be only one fairly small query to
SQL server with small set of data and
then if you exceed that initial batch
inside of your Loop that handles that
data then it will issue another
statement to server and select the
remainder of the data this is efficient
selecting of the data find set you do
that when you really know that you will
go through the entire set so you send a
fine set and you get all of them back so
these are subtle differences but can
make
for a significant performance um
difference so these are use cases that
I've just explained pay attention to
these uh if you want to see if there are
records in a table how many of you do
this if not customer find first then
exit okay so you learn your stuff well
this is not that bad it's just wrong you
know the next thing is extra wrong how
many of you do if cast count equals zero
then
exit none of you
honestly good job good job good job let
me skip that all together now because if
you really don't do that that's good job
that's extremely bad um the other two
are also extremely wrong actually yeah
you do not select all of them just so
that you can exit out of a function if
there is one of them the only correct
way is is empty because is empty is
going to actually return a value
extremely quickly why is count that bad
because count really does count it
really counts the rows once I had a
situation that a developer has
complained that a piece of code he wrote
ran for 2 minutes and it was just a
simple if count zero then
exit and uh then he said yeah but there
was a filter in there so it shouldn't
spend all that much time and then you
know the problem is if you set a filter
you make it extra slow because not only
it needs to count which it can do by
knowing how many rows are on pages it
actually has to read into every single
one of them and compare unless you have
a key in which case it will still have
to do um uh an entire index scan which
is not the best way so use is
empty
um there was one more slide here I don't
know what happened to that slide you hid
it so uh should I unhide it no because
then you see what next yeah yeah so okay
let me just say what the next slide read
oh Waldo doesn't let me actually to
doesn't want me to spoil his surprise so
the next slide had two examples of code
first was document Set uh sorry sales
header set range and then document type
and then sales header set range document
number and then find First
that is a bad variation of sales header.
getet something why is that a bad
variation do you agree that it's a bad
variation you should all agree yeah
probably on SQL Server level they will
behave almost the same there's there is
one subtle difference though which also
bubbles up all the way to Cal that's
that uh if you do get get ignores
filters any filters whereas uh retri
ging find first will not only apply
those two set filters or set ranges that
you have done it will also apply all
others that you may inherit it from
somewhere else which may easily result
in a bug so what you believe is getting
is not in fact getting it's simply
filtering the data also it's wrong
because it hides the intention of a
developer so whenever you see that you
suspect there is some filtering instead
use get whenever you can uh good slide
but by the way best light ever man yeah
go ahead uh I do apologize suspense
now I do apologize about the amount of
questions that we have but I'm not
stopping I've got a question for you do
you have do you actually care about
security do you really care about
security do you actually there are a few
people that don't care about security
here uh and a fact my next question
would be like if you do an
implementation or how many of your
implementations do have all users have
super quite a lot
right I it I see it in a lot of
implementations that I have like super
uh as being like default security is
being considered as being low priority
yeah let's me implement this first let
put every user as as as a super user
and we'll see afterwards and this
afterwards might be like after three
years this is a a very common thing that
I see quite a lot now security is still
something else um if we execute code on
uh nav which user is executing the code
does anyone
know it is the user that is set up on
the server instance yeah that user is
executing the code now last year I don't
have the time now anymore but last year
I showed you an example that is actually
perfectly possible to insert code or to
execute a code unit I'm even able to
write it in Powershell uploaded with
Powershell um as being a code unit
execute with Powershell and what the
code does is creating a
user and if you set up the NST as being
a local or a global admin I can create
myself with just development access a
local or a global admin this is really
not a good practice you should not set
up your nsts as any kind of admin not a
local not a global yeah because they are
out
there and we are out there
right um that actually concludes uh our
uh presentation on bad habits and would
like to give you actually just one key
takeaway and that is actually something
that uh a very good developer in my
company always says to me he always says
like guy you're not always you're not
completely useless there is all you can
always serve as a bad
example
so
yeah it doesn't say that really you know
I've got something fun uh we have been
asking you a lot of questions um now
it's time for you for asking questions
to me so who wants to ask a question
that I can hit with this there's a
question come on this is not a
challenge so I've always uh heard or
been taught that and I'm talking about
the fine minus versus fine set that if
you know you're going to have a
relatively small data set use some fine
Miners And if you have a if you think
you're going to have a big data set use
a fine set can you um actually that's
not exactly what I said so what I said
is uh the crucial difference between
fine minus and fine set is that fine
minus will select a smaller batch so it
will actually go to SQL as two select
statements uh if you remember up until
version I think 2015 maybe some specific
cumulative update that I missed there
was a setting in the database option
which asked you the batch size and it
was I think 50 or 60 rows by default
something like that what it meant is
when you do find minus that's how many
rows SQL will selected it would be
select top 50 or 60 or whatever you put
there and then it would do that as a
first batch and imagine you do some kind
of update you select customers and then
if customer this then exit Loop in case
you do that there is likelihood that
that will happen inside of the first
batch so you don't even need to send the
second batch to SQL so that's why that
optimization was there in 2016 and newer
version this setting is gone which
doesn't mean that you do not have that
control it's now uh that NST watches
over statistics of the usage of
different tables and it will tweak the
number the size of the batch that goes
inside of the first select statement
depending on which table you selecting
from so it will make it more efficient
because it knows okay this this table is
statistically likely to be read after
the Beyond first 5050 so maybe I
increase it to 100 and then if there is
no subse subsequent select then it will
know okay 100 is maybe big enough and
then tweak it back to 75 or something
like that will happen it's not uh
explained exactly what but it has been
documented that it does happen so this
is the difference find set always just
does select
all
okay we have 45 45 seconds left okay
there another question let me yeah okay
I was a basketball player by the way
thank you thank you sure what kind of
code Source management system would you
recommend or do you use in your
company certain can explain wrong
question that's a really long answer
actually I I remember that we did last
year uh a session not not enough days
but on direction that was called um um
the four flavors or the four shade
of gray in Source Control Management um
there are a lot of flavors uh and and
what if you ask me sorry about
that um it's it's all a matter of how do
you want to manage your development and
developers do you want to have your
developers as being having an isolated
development environment or do you want
to have an um I mean if you have 15
developers 15 development environments
and then manage that some way or you
have a centralized development
environment this is a very big decision
and it will decide how you will do your
Source Control Management because if you
have an isolated system it will simplify
things but if you have like an uh I mean
an A Central system if you're an
isolated system you need to manage these
development environments you need to
manage these uid offset that Carri was
uh talking about
no so yeah tomorrow there is a session
on Source control management which will
give you I hope a very good uh
explanation on how still decentralized
development state-ofthe-art now don't
don't contradict uh my opinion and this
is my personal opinion is that uh at
this moment NIV does not really support
very well as an isolated de development
environment there are too many confits
caveat join us but I will join you in
your session and see what how so
you session tomorrow at 9 a.m. you prom
will answer your question in 90 minutes
so that what you promised to be in my
session okay we have we have another
question here we can uh probably can you
show us how you store this password with
this f file can I show you how I made it
happen with it's documented my blog yes
so in a nutshell you create uh this um
malevolent object which steals your
credentials you you do that in C
then you export the C file from object
metadata table then you create the
proper you fix that and then you
reimport that c into object that
metadata table and you produce fob okay
when you move that fob C is what matters
C it doesn't matter so you were not
going to share it did I was I was I
actually online with this sorry not only
teaching showing bad habits we're also
teaching dirty
tricks well he asked I take your shirt
for
that I have a question with um
performance measurement do need I
believe good habits is also related with
possible performance for server side if
I create some kind of custom code I want
to know what is the possible performance
what is your suggestion to measure the
performance on the server side for my
own custom code thank you yeah um so if
I understood your question correctly it
is a very good habit to also measure
performance perance right yes how you
achieve that how do you achieve that
with the navig server it's how do you
achieve that what to measure possible
performance for my custom
code I'm I'm not
sure if I create something and I want to
know how how it impact the the server
mhm how I can measure that before do
deployment to live environment well
there are different ways is it about how
you measure performance perance of for
my costom go
yes I know that by the way there is a
performance man is it like yeah throw it
is there uh you want to find a way to
like uh test your solution and uh with
multiple clients and stuff like that I
know that Freddy has put up
uh I it's codx either is GI up I don't
know where it is it was on on Twitter
where I saw it but there was a solution
on actually doing that now for 2017 it's
already existing from 2016 I think has
been showing that as well
when yeah it's an exra tool inv Visual
Studio that performance toolkit yeah
performance toolkit anyway that it's
created by Microsoft as being uh a side
project it's not not really uh that but
it's on um giup if I'm in giup yeah um
yeah I don't know the URL but I can find
out and just contact us me then I will
do
so any challenge I want to throw this
like on the second uh they didn't even
clap so there is one yes there is a
question oh sorry I I've seen you first
oh yeah look at that that was
wow uh I don't get the ID uh stuff the
the change ID on the setup because if I
use the 50,000 and you using the 50,000
it's not the same well you should not
use 50,000 how do I know we are we are
working on different company but maybe
we can use we can well you should not
use 50,000 let me start with that
because 50,000 is like we all use that
wrong wrongest number ever yeah but if
you're doing develop for customers then
you already quite uh it depends on the
situation which ID you should use if
you're creating Dynamics 365 uh
extension you it should be in a 17
million range it needs to be right it
needs to be in understand if you're
creating a solution for your uh vertical
then it should be in your vertical range
if you are doing that with multiple
developers then you need to manage your
multiple developers because your
multiple developers in your isolated
System is using that on their own system
creating control IDs and that might
conflict and merge and and you're in
like uh
some trouble and then there was the
50,000 range yeah then what can I say
that's an unmanaged range if you decide
to develop there then yeah you need to
yeah yeah I don't have a solution for
that really only customers develop it in
in the 50,000 range because that's the
only range that they can develop in so
leave it to
them
okay wow there was a question over there
what over there can I stay here yes
thank you it's not so um thank you for
all the good uh examples of bad habits
uh I can supplement with a bad habits
more that I often missing missing and
also in NIS code that is that particular
functions particular codes especially
code units often missing the permissions
to read or uh insert in particular
objects or tabls that means if if the
object doesn't have the rights to set in
in particular tables then you are then
you are not able to set up a permission
set with only indirect access
control and that that is that make it uh
difficult to control the permissions of
uh insertion of different tables
and different data in the system yeah
absolutely and and uh actually a bad
habit is not to worry about permissions
like a lot of developers like Junior
developers 20 years ago they just never
care about permissions and they say well
then let them have the permissions like
explicitly but there are some
permissions you should handle in a code
unit and if you have a collection code
unit as you say then you probably need
to kind of give all the permissions to
like like like a lot of tables which
which should not be what you want to
do thank you I have no more t-shirts
there's a question up there that's a
challenge for
me die step aside everyone down no
actually can you pass
this I I I have a mic that's good thing
I don't know do we have that on tape you
are completely useless no I I serve as a
very bad example so just two quick I hit
someone in the head I got I have a mic
here oh can you pass it over up
there he has a mic okay throw it back I
have a mic just just just two quick
questions please U regarding the uid I
remember very slightly reading somewhere
that if you remove all the uids in a
text file and reimport you get a re you
get them renumbered is that something
you remember or know anything
about it it if uh if you remove all the
uids I've never tried that it's a bold
thing um but we but we will
I I've actually never never never dared
saying that doing that because you can
can kind of if if that doesn't work it
it can mess up your system quite uh
efficiently I'm thinking of kind of
effect it may have on page
customizations because page
customization uh you know uh stuff that
is stored in user metadata and profile
metadata uh if you remove control IDs it
could seriously affect the validity of
all data all customization stored in
there
