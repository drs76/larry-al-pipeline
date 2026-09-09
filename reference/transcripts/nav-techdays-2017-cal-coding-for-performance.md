# NAV TechDays 2017: C/AL, Coding for Performance

- **Source:** https://www.youtube.com/watch?v=C4hMN0-GYHQ
- **Video ID:** C4hMN0-GYHQ
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 100m05s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

hello and welcome to programming for
performance this is your lipstick and
I'm asking cartoonists and together for
the next 90 minutes we will be talking
about how best practices when writing
code for performance and also
maintaining it okay so we have agreed
under because we have more content than
we have time so to skip all the small
talk yeah
and immediately dig into the content and
those of you who have frequently
attending NAB Tech days may be following
my sessions before and talked a lot
about performance and just to give you a
little geography Evan I was talking
about performance before we had these
three major areas of performance that
was one thing was well platform and
stuff like this the other thing was
blocking and stuff like this and the
major or the most important area where
we have lots of problems and also lots
of resolutions this is this vast area of
query strategies where it's about
communication between nav and SQL Server
and our session today is also within
this context of query strategy so one
thing that we have to keep in mind for
the next couple of minutes is the the
core architecture of nav and since the
dawn of nav so since the very beginning
we always had a three component
architecture so not talking about a
three-tier architecture we always had
these three components and with means on
the left-hand side we have the seaside
world this is the world where you live
and breathe every day this is where you
create all the magic all functionality
interfaces weeper whatever so this is
let's say where you live today on the
other hand on the right hand side we
have the database engine we have
sico server an in-between we have let's
say a kind of moderator kind of
translator that translates from the
seaside world to the sicko world so and
this is something you need to be aware
of for example when you when you create
a seaside table you do not create a
sequel table you just create it in
Seaside and this black box right in the
middle is picking up this template and
creates the sequel magic the same goes
when you program something you want to
create data you use a find command but
what actually hits the sequel server is
a select command
you're not programming a select so the
means it's all done by this black box
this core architecture has advantages
but also has disadvantages because that
means what you want to have on the left
hand side is not necessarily what you
get on the right-hand side on a database
level so in this session we have
actually two parts the first part is yes
minka will dig into this left-hand side
the seaside world yeah what you can do
about here and later on I will take you
over to the dark side when we have to
discuss things how how they hit sequel
server yeah so then hand it over to you
again have fun ok so when people think
about performance it's usually something
they relate to to hardware to
configuration to potentially to sequel
server and if they hit a performance
issue then the solution they're looking
for usually is itíd you doing a bit of
magic or someone like you're coming in
and just solving your problems but the
code you write effects actually the
performance just as much as you're
scaling and your hardware and your
configuration so my part of the
presentation will be just about that
trying to show how the
it can affect your performance and what
to do about it so I'll start off with a
bit of theoretical background talk about
algorithm efficiency in general because
that as a theory applies to both CIL and
sequel and whatever you write your code
and then we'll move on to two data
retrieval methods that's our statement
we use to retrieve data from sequel then
some do's and don'ts some code
constructions that we are used to and
that have been having different effects
on performance throughout the versions
throughout years things to keep in mind
when writing your code when that are
related to performance and affect
performance and tools that you might use
that to help you check and validate your
code for performance okay so those of
you with technical background might
remember this the order of all the Big O
this is a mathematical description it
describes the behavior the limiting
behavior of a function as its data input
goes in computer science this is used to
tell you how complex your algorithm is
or how scale abilities in in other words
simply put it tells you how much work
your system will have to do to process
the data set given your code so it
measures how effective or ineffective
your code is so for example to
illustrate consider a table with
thousand records if an algorithm has
constant order of for example one means
it will always only execute one
operation to process independent of your
data set if it has a logarithmic order
means for a table that has thousand row
it will execute seven operations and so
on if it has exponential order in this
example square for table of thousand
record records it might end up with
million operations to put that into into
a perspective and into our more familiar
examples consider you want to you have a
value onto a table for example and you
want to filter on item number so
basically all you're doing is a set
range and the find statement to get your
filtered set now when you write that
code and execute that code there is a
bit as York has said going gone both of
honesty and on sequel side so there is a
translation there is a the whole cache
dimension and server side there on tips
to survive processing Curie plans and so
on but we will these are in most cases
fixed transaction costs and they are
fixed regardless of data size so we'll
look away from them and focus on what is
a variable cost what impacts our
performance so if you consider that fine
statement we we filter again value entry
on item number and we our value entry
table has a thousand records so we're
speaking about chrome say database so
that gets translated bottom line to
sequel select where statement now if you
have an index for that item number field
example if you have an index and sequel
actually compile security plan that's
index ich since an index in sequel is a
binary tree that index ich is a
logarithmic order operation so thousand
or seven of some cycles on sequel side
to retrieve your set if you don't have a
good index and sequel ends up with index
can plan so reading all the rows in the
table that means logarithm that means
the order of linear proportion to data
set means thousand rows
and so on if you're a bit unlucky with
nested inner joints and so on you might
end up with exponential number of
operations now a million in this example
now a million might sound like a big
number for Sifu that's nothing that's a
millisecond the blink of an eye so it's
not a problem at all
but now consider when your table grows a
bit more to what is probably more
realistic value and that is 1 million
records the logarithmic the index seek
that we do has only now now only costs
14 operations or has only gone a little
Wireless index can now takes million
operations where so gratings will take
up two billion and more depends on your
algorithm complexity so why am i showing
all this so I want you to to have a
clear picture just how much stress or
work a bad algorithm or complex always
are not bad but as such but complex
algorithm might cause to the system so
to zoom out a bit more and put it into a
bit bigger picture here I have different
algorithms and their order I want to
with this I want to show you how to
remember just how much an algorithm
complex algorithm can affect your
performance so the excellence that's the
input data in your data set the y-axis
that's number of operations your code is
going to cause on the system so and this
is how different algorithm compare when
it comes to effectivity so the best
practice is to be within the green belt
that's where you want to be these are
the efficient algorithms of law
processing orders now
when you measure this complexity
algorithm complexity
you have to kind of very compare
algorithms you have to compare apples
with apples so you cannot compare our
algorithm complexity and sequel with Cir
those are two different categories and
we have things going on on C outside and
then on server side and then on sequel
side but and some fixed transaction cost
but for the simplicity let's combine
these complexities into one common
complexity so whatever complexity is
going to happen on sequel side and
whatever happens on server side combine
it into joint complexity and have kind
of idea how the code will perform so you
have the whole range of the greenbelt
without performing code and low number
of operations means also a short
execution time and then you have the red
belt the horrible zone with a very high
number of operations means long
execution time so combined with sequel
and crl operations that again the green
belt that's our data retrieval that is
used in confined way and where we have a
well indexed database I call this the
girl chromosome because and Cronus would
be your bottom left corner because
basically whatever you're writing clones
will run perfectly well and this is why
because it's this tiny little bit in the
corner in the left
you can't you can't make it run poorly
but as your data grows that might look
completely differently so aim is to stay
in the green belt to have performant
code that is also well indexed the
yellow zone there that's a maintenance
zone that's basically where you can fix
a lot of problems just by handling in
Texas with the proper indexes and with
some simple code adjustment maybe and
red zone finally on the top that
overnight processing zone so this is
kind of processes where we tell the
customer this needs to be scheduled for
overnight and then you know you have to
run it once month or you'll never get it
done
so these are the algorithms that
basically cause horrible amount of
strain on a system and sure you can
always compensate for that to a certain
extent on a hardware side so you can
always over scale to compensate for
whatever you throw at that system there
is always a hardware that will cover it
to some extent but it's an uphill work
and it's unnecessary so that's why this
remainder of my part of the presentation
is talking about how to avoid it
unnecessarily stress on the system
caused by the code okay so I want you to
keep this graph in mind just just to
keep in mind how number of operation
changes in the grave belton in the red
belt and to put all this into an hour
CIL perspective what does it mean on c4
we were looking at the example of reads
what what does what do we measure on CL
what will this mean on CL well this
whole thing boils to one most important
measurement when writing code so the
whole algorithm complexity point boils
down to this to serve the round chips
that is what is causing the biggest
stress so basically lower your algorithm
complexity order when writing your code
this means minimize serve around it the
fewer the round-trips the better the
performance so how do we do that this
now is the familiar stuff that you've
always probably known first of all
indented loops where we go to loops and
within loops within loops of Records
to retrieve a few few records doing
something sometimes to modify or in
worst case to just read a few records
within that selection that is causing a
enormous amount of round trips those are
the algorithms of exponential order
usually so you automatically by writing
that automatically moving from bumping
up from the green zone up all the way up
to the red zone so wherever you can
replace that the very complex indented
loops with naturally qsq is executes one
round-trip so you save that's the
constant green belt so you save your
system a lot of work and a lot of stress
by replacing their own trips accessible
home trips with one effective QA now
cure is on cash to so so if you're gonna
do the replacement do it somewhere where
you know the code won't be repeated
within one closes excessively because
you want to also benefit from that cash
so replace it from the topmost level to
put it that way so curious use curious
as much as you can then there are these
statements that will that are introduced
to replace your server round trips with
one so set out occult fields normally in
yesteryears we used to write code fields
within the loop that causes of course
extra surveillance rate for every record
within that loop for each record in
selection if you put set out the crop
fields outside the loop you replace the
whole thing
with one round trip so so you move from
what would have been a linear order of
complexity that's the yellow belt down
there to the green belt just by using
set auto code fields the same apply to
columns there are still many examples
for people
and coat loops just to summarize a value
use costumes where you cancel you go
down from the yellow to the green belt
from linear complexity to one single
round tip same goes to modify all and
delete all that that is already widely
use and when you do write code right
with iterations in mind so for example
if you do put some loop into a fact box
and that track box ends up on a list
that's going to be kind of a first read
for each record on the wrist that will
have some implications because you have
a fact box that goes for every record
and then within that you have your loop
on effect this is just an example but
then you automatically unnecessarily
adding a layer of complexity moving into
exponential horrible zone so well never
you can when you write the code just
plan with with those intuitions in mind
there are tools you can use to to kind
of check a field if you're there of or
if you have overstepped that data
retrieval methods these have not been
changed for last three or four years I
think they still cause a lot of
discussion in the channel for some
reason there is still lots of confusion
it's really quite simple they are well
documented that documentation stands so
what this written is - this is what they
do and how they should be used so here
we go one by one find find issues two
statements now in back in younger days
we had loops with some self tuning
number of top select top records also if
you have thousand records you might have
ended with 200 loops or something fine
uses two statements now so it always
uses two it if your table is
100,000 records it was still used to
statement so it has a constant
complexity order it's in the Greenbelt
find does only two rounds the first one
will say select top a value that is
self-tuning based on some kind of
statistics
the second one will retrieve all the
rest of the records when do we use pine
we use find when we want to retrieve
some selection of records and we are not
absolutely certain that we will read
them all if there is somewhere in that
code the chance that will pop out of
that loop and won't be reading the rest
of the records do not use find find is
sorry the do use find find is for when
you don't know how many records you will
be reading of the selection you're
asking for so in if any doubt use find
do not default on find set and know why
so find that does one loop find us two
friends that will always do one loop so
you might be tempted to think well it's
one millisecond faster it does one
instead of two so it's the default
option no finds that also does exactly
that switch review all the records in
one loop and place them as network
packets they are waiting there and then
what you might observe if you are not
going to consume all those records they
will be there waiting so then you will
be observing a higher number of async
network i/o waits on sequel side if you
have a simple do that will look into it
but simply you will observe sequel
memory treasure so find that just as
that which fits all these records if
you're not going to consume them you
pressure and seek for for no reason at
all so if I said when you know you're
going to read them then they're going to
disappear from the weights also if you
are modifying a set use find set when
never
you're modifying the record use find set
let me repeat that when you modify a
record you will find set and then use it
with a correct parameter so find set for
is for modifying records find first
point last top first record and bottom
record and is empty that has been a bit
flaky over the versions it's very simple
if there is any selection within record
tool if you want to know if there is any
selection use is empty there's no reason
to use anything else but is empty has
been breaking over the years all sorts
of things have been happening if you use
is empty reference variable reference
the record after that and that is empty
is returning only boolean variable so
the ref record you reference later
basically needs to load up into memory
leading to all sorts of we had
performance issues memory leaks all that
has been fixed so but but it seems to
have been a bit bit unstable previously
if you are unsure fine first we'll do
the job as well whatever you do you have
to keep in mind unless you are working
with scenario where it's of crucial
importance to get reply to some
statement you sent within tenth of a
millisecond it won't matter much what
you use of these find this quick source
finds that so is fine perso is find less
they are all one round trip except
finders - they're all the greenbelt l
the constant complexity they do not go
with input data your problem whatever it
is will likely not be here so it's the
complexity of the code we write it's
those indented loops the excessive round
trips that caused the issue it's hardly
ever one of these now that there are
always exceptions of course
scenarios but but really whatever you
use of these you'll be fine so so they
get so much attention I don't just don't
think it's a deserved attention they
don't they are all just fine really do's
and don'ts okay two things of two ways
of doing one and the same thing
left-hand side I do what I don't do
quite and right-hand side I do what I
don't
well it is I do
this is how you should do is it and this
is maybe so why is it maybe now we're
speaking about performance what does the
right hence I do again
we speaking about performance yeah so
I'm not I'm not referring to the case
were obviously check see if the insert
it will be a control level but all
abortion you in control way but but I'm
speaking purely of performance okay what
does the left hands I do you're
inserting thousand records what the
little bow inserts so what does the
right hand side do Bell breaks the bulk
insert that's correct and why in
interrupt it's called buffered inserts
report that yeah those are not sequels
no quite so by default Novation will
collect all these inserts and punch them
into the sequel when when the loop is
basically complete those are buffered
however that inserting algorithm has a
has some kind of sub tuning algorithm
again so at some point if your table is
sufficiently wide so if you're searching
sufficiently wide records that self
tuning algorithm becomes to kind of
flatten out so the benefit of
performance with with buffered insert
starts to level out so the wider the
table the wider the rows you're
inserting the less the benefit you get
from the buffer date so at some point it
it starts going dropping again in some
scenarios there are not too many of
those but they keep popping up in some
scenarios if you are inserting very many
records in earth in such a wide table it
might pay off to turn off the bulk the
buffered insert and you turn it off by
doing the if-then so these are these are
not your everyday scenarios but if you
come across them if you do have a very
wide table then you might be better off
you can easily test it and verify it may
be better off at some point with without
buffer the insults
left-hand-side do or don't right hand
side
Yeah right simple one so so why is that
I don't sorry don't I do that in the
other one too apart you're using piles
so what does this mean this one will
will generate a round trip for the
modification an update statement as you
need to have it this one will double it
at worst make it exponential so this is
this has not always been like this this
is introduced as of 2013 I think before
2013 they did more or less the same job
performance wise the same number of
round trips as of 2013 that to the left
hand side is actually causing a far
higher number of round trips oh definit
don't that's a favorite so this one is a
killer that some what does this do
translated to sequel language this is
simply a select distinct we select one
record from a specific selection and
then repeat that for their promise level
it's a select distinct and once upon a
time when when these codes were written
it was no different engine where they
were working just fine once equal this
this causes this is the redzone type of
algorithm this causes the the
exponential easily causes the
exponential number of round trips each
of those round trips has its penalty if
it's not not latency then it's the
operations on sequel and reads and disk
waiting center
so this is kind of a red zone or item
select distinct and we still have them
around in code quite quite a lot and
it's easily solvable with simple QE and
how to translate one to the other there
is a nice design pattern or blog post on
design pattern where just that was done
with example from a standard application
code so you can look at that on design
patterns select this thing so this is a
killer good example of how you are
necessarily stress so instead of
exponential number of round trips and we
are talking on a bigger tables about
millions and billions you will end up
with one so the difference is really
huge it's not a demo it's as a demo but
it's not a demo this is what I wanted to
show and now if I go here was it does
that show no yeah right I'm still into
sensation
right so this is a example of a code
it's not made up it's a real thing out
there
just to show you what what this looks
like this is kind of a select of the
sting just with really many levels again
it's not made up but I took it out of
out of standard application and didn't
put it in slide because basically
couldn't fit to show you how this this
bit looks like and now I I didn't want
to run demo because it would take quite
some time that we don't have to collect
all the details and process them and
analyze them and so on but let's see to
take it one by one so this is the code
this is just been a beginning of it that
you're seeing here it's a standard
application code what we are looking for
all the result of this non clones will
be some sixty records result of this
selection so there are 60 records that
fit this description that that are
within the innermost loop for this sixty
records we will hit the innermost loop
74 times so the innermost loop is
records there are process 74 times this
will generate over 800 round trips so
there are 800 round trips with sequel
statements resulting out of this that in
turn will generate over 37,000 logical
reasons equal this table has 300 records
on Kronus so this is back to the girl
this is code
what they still do today this is back to
the graph this is your exponential
explosion of activity on sequel
depending on the code you write so
whatever code you write does affect
performance greatly so I thought this
was a nice example to have well now that
that we've kind of covered in in very
general terms the the best practices why
isn't this reacting it is other things
to keep in mind subscribers so events
fantastic feature we will use it will
love it we need it and we're going to
keep on using them why are they here at
all well subscribing to event adds
another dimension of complexity to your
algorithm so when you have to use them
we have to use them so I'm not saying
don't use them but careful how you use
them when you subscribe subscribe to the
most granular level you can so if if you
want to say you want to modify value of
one field when never user modifies value
of anything doesn't matter it might pay
off to actually rather subscribe to the
same kind of field on three different
pages and do it there then to think of
well why don't I just subscribe on a
table and then you can't always solve it
to the page you have to subscribe to in
many scenarios on the table so when you
subscribe on the table try to again be
as granular as possible go to the field
if you can and avoid on modify or
triggers of the table why because they
will add another dimension of complexity
to any algorithm you write modify all
you've just
the more you subscribe or modify to on
modified ticker of your table you don't
need to write the code in the subscriber
it's there it's active empty modify all
no more so your codes that is modifiable
that's supposed to process modify at one
go to thousand records will now generate
2011 trips just because there is an
active subscriber to to the table and
whatever you do try to stay away from
the subscribing to system events like
own database modify for example you can
imagine what that will do to any code
you write so it might be look like a
good place to start if you want to do I
know change lock one database multiply a
few things to hook into easy
it effects greatly affects it will
affect any record you modifying the
entire database so so you subscribers
you have to just think about it when
when designing each of them will add a
complexity on on tables on algorithms
you write mark
it's it's a good feature to use on your
user interface if your user wants to
mark of your records here and Daryl it's
perfect to use when you use it in code
if you start placing marks and not
sequentially it they will start
generating sequel round trips mark so
that might easily lead to excessive
number of round trips I know how much
mark is used in the code but just to
mention them which they are not quite in
the same category as all the other stuff
have been talking about they have
nothing to do with round trips yep
purely the effect is on sequel that they
are popular frequently used and they
come with a steep price
performance-wise they have their
benefits too well they have wider
selection or more numbers to select of
them if you use integer integer key they
have low occurrence of hot contention
spots so they have their benefits
however they are also expensive at
insert they're expensive at seeks
expensive at sorts they do use the
fermentation so it seems to be a popular
feature but it has again nothing with
algorithm complexity to do but it has
everything without locking to do this is
what you'll typically see if you're
using intensive transactions that
involve quits as primary keys mind you
know and now the things we've been
talking about so far the things that
that create a lot of work at at sequel
server making everything run slow like I
said an overnight process that we
usually end up this is just slow this is
always just ran slow they don't leave
footprints that's the problem with with
code that's not performant there is no
footprint you can open all sequel
monitors everything works well in CPU
low memory nothing to complain about but
it just takes forever
those are accessible on trips but you
have the different kind of performance
issues and that's things that do live
quite quite significant footprint and
that's normally we measure that normal
in CPU and memory so those would be
traditionally reports and usage of
dotnet variable stable leave some
footprint now designing reports and
report performance is a topic on its own
so we won't go into too many details
here
but the same known principles
better here data set size when your
design reports you have to remember that
it will all be sent to the client yes
you have 64-bit client but again think
of the round trips that's what they will
cause and not to sequel and to to the
client and memory consumption then there
there is a memory consumption issue
that's no longer issue of win quieter
than who you spin quite we all know so
there is a nice article about memory
consumption on bed point what you can
possibly do to some extent to it then
the cost policies which that is where
you have to decide between memory leak
and performance basically you might end
up with the memory leak if you opt for
performance and vice versa but that's
how you can adjust it there is you can
read more details about it on the net
that is the switch this policies are NST
configuration parameter that you can
turn on and off to opt for then memory
consumption good memory consumption or
better performance and dotnet variables
they will more people off another thing
it's when they are not cleared up that
they can use a lot of memory
unexpectedly and people always accept
expect garbage collector to do that job
and it will it will clean up eventually
but it doesn't always kick in when we
think it does so dotnet might and
reports might use quite a lot of memory
living quite a significant footprint and
finally tools so how can you verify that
your code is performant that you you
write everything you write in Chrome's
that will it will remain that way even
as your database goes well one thing you
can do the
no two that I know of at least that kind
of covers it all but I tend to use
combination in combination they're
comedians code covered feature in nab if
you start code coverage feature search
in the windows right called coverage
start run stop it'll show you the code
that was executed during the capturing
one of the columns is called number of
hits it shows how many times each code
line was actually executed so that gives
you some the first proportion it tells
you and you know how many data your
crumbs table has so it kind of gives you
proportion are you running this too much
is this being executed spaghetti code
called from various places and end up
being running over and over again so a
number of hits will give you an
indication of if your code is being
executed too much
that's one tool and then it won't tell
you anything about the server own tips
it might cause when you're modifying for
example within the loop and then
changing the range of the fields and
then reiterating and so on so those
things that cause extra round tips you
won't capture them with any tool that
I've heard of so but what I normally do
is start profiler as we in India and all
end up doing and basically just observe
drop I love when you do have excessive
around tip so you can do you can collect
everything to a secret profiler table
and just simply observe how many of that
statement has been sent because when you
do have excessive around tip so so
really slow processes as I said none of
the alarms for go of memory will be low
CPU will be reads will be low
if you look at the profile on sequel
server it just looks perfect the problem
is that the same statement will be going
over and over and over and over again so
that kind of gives you indication okay I
have a piece of code that that can be
optimized it's generating too many
rounds so you can always that the slide
I was showing earlier with the number of
sequel statements that that's basically
how I do it like I capture with code
coverage to see number of hits it
generates in the code and then capture
the profiler and see how many round
trips the same course code has cost and
you can profile service tear activity
not just code coverage you coverage has
user interface in navigation you can do
it without user interface you can do it
silently with kind of circular log so
you don't consume all your memory and
service tiers you can monitor if you
suspect activity as as we don't send you
user ID to the sequel server activity
that needs to be found that generates
extra load on the server you can monitor
everything without a collector sets on
service tier we have two kinds events
and performance so event collector set
will basically give you the same thing
that's called coverage and resource
monitor for things that do live
application footprint for those kind of
issues I'm on overtime okay right so we
have all the time we need because we
have the last one between them and the
beer so yeah
so now you have followed the jedis path
now let's go to the death star yeah
again bearing in mind this architecture
left-hand side the seaside world where
basically boils down to avoiding and
round trips sooner or later the
will hit the fan anyway and the place
where the hits the fan is the
secret server so performance problems
actually do not happen in your seaside
world performance problems happen on the
database now others assuming now we are
done with this round trip thingy
so now assume in your code works like a
charm still you will see it screws up
and I want to show you the reasons why
in SQL Server the performance actually
it's all about data retrieval so it all
depends on how quick data could be
retrieved and I want to give you a very
very simple example here and my sincere
apologies to all those who have previous
attended some workshops you cannot hear
that story anymore sorry about that yeah
imagine a table like a huge warehouse
like this one here and in this warehouse
you will find thousands of crates of
boxes yeah that's insecure that would be
our pages to store data and now in these
boxes there are millions of records now
that'd be color pencils color pencils
and different length s and strength and
of course different colors so this is my
table one of these crates contains the
Lost Ark if you remember yeah ok anyway
so now you're a sequel server and I send
you in get me all the red pencils yes
select from pencil aware color echo red
so what would you do nothing
so you're enrolling with your eyes here
and how in hell should you know where
the freaking red fences are you can't
know that you don't know that so what
you naturally have to do is you have to
open every bloody box fears to look up
if there's any red pencil and you would
agree with me this will take forever and
it will take the longer the more
you have to open bad performance so what
you need actually is some some dye
around in this warehouse that has some
kind of catalog where it says in which
box are which kind of pencils so we call
this an in in sequence of an index the
index originating for the Latin word for
to point at something yeah that's why we
called it the index finger well so oh
it's recording sorry yeah yeah so how is
an integrated well we sent this guy
through this warehouse once opening all
the boxes and just writing a list ok
black box black pencils box number one
the green pencils of box number three
and so on and so forth so the next time
you are sent into this warehouse get me
all the red pencils so what you do is
you see oh there's this guy around
knowing something about the color you
ask that guy and say hey tell me whether
red pencils are and then this index guy
will just point to the right box and say
it's in there and so you can quickly
seek this desired data and retrieve it
quickly and this is as simple as it
sounds
we are spoiling down in SQL Server so
the more boxes it had to open the long
it will take in escrow so we talked
about logical reads and this happens so
in a sickle
of course secret database indexes look a
little different now we have this
balance three is three like structures
has to recall that we have two types of
indexes one index is so called clustered
index which defines the physical sort
order of records of how they really
stored on disk and all other indexes are
so-called non-clustered indexes that are
pointing to the data that are pointing
to the clustered index and then these
indexes can be used in two different
ways there's one way it's a quick way
that's seeking through this balance tree
yeah that's like walking through these
branches that's a quick operation
theoretically
I will show you later if something
stupid has to happen like opening all
the crates in this warehouse and this is
sequentially reading the leaf node level
of in
that's what we call a skin so now if you
remember this Big O thingy here a little
simplified version scanning means the
more boxes I have to open the longer it
will take
yeah so so this is the red so let's say
in in this odd a turfy index seeking the
best-case scenario is that I have to
only read one page per indexed level so
in this case that would be three reads
when seeking through the index scanning
in this case even means already four
indexes of course that's just a
PowerPoint slide and in reality that
looks a little different yeah
so basically scans bad seeks good maybe
maybe not so sure so just introducing my
flag around here and please ignore the
fact that this is an old novel database
whatever I say now it only applies to
NAV 2013 and higher the old knife
versions we have totally different
horror stories the old okay anyway so
just to bring it back into your minds gl
entry table we have this standard set of
keys primary key slash clustered index
is the entry number so the records are
physically sorted by entry number then
there's a lot of other indexes slash
keys and just put your attention on this
one yeah this is the one are going to
use later on so here I have just a
little secure magic to have a look into
this gl entry table in the index
structure from management studio site so
the first thing is just counting the
number of Records yeah it's this table
already contains three million records
then here I'm executing a procedure espy
help in next just to display all the
available in excess in this table from
management's to you so you know I'm not
cheating yeah so it's still there
clustered index and again your attention
please to this one sort of one real
account of a passing day so this here is
checking on the index structure on the
physical structure of the clustered
index this is upside down compared to my
PowerPoint slide
so here the most detailed level of this
index is level zero that's the the first
line here and it has a width of 125,000
pages so it means I need hundred
twenty-five thousand boxes to store
these three million pencils this is the
width of this clustered index
nonetheless it's still just three levels
deep I have just one root node and out
of this root now there's two hundred
branches growing out addressing the next
level and so on so SQL index we have a
very very white but never very very deep
and as I only have two or three levels
and stuff like this so this other index
the non-clustered index GL account
number hosting date has a width of
10,000 pages and also just three levels
deep so that means our best-case
scenario is when we're using such an
index is to read one page per index
level that would be one two three worst
case scenario is to read everything
that's 125,000 reads in the following we
also have to look into Anthony that's
called a density so that identity means
how many equal values to a half on a
certain field and here I'm checking on
the density of the GL account number
yeah there's a field in GL entry and on
the account 1 5 7 5 that means I have
800,000 records of the same account so
again my table has 3 million records and
800,000 so that's roughly a quarter of
this is based on this account number and
so I have different data densities and
here for example the last one and I only
have four GL entries which are on this
account number 3 9 8
six so that's my playground so as Mika
told you can verify how your code
executes by using profiler and stuff
like this
so what I actually did is a little
Navision code and running some of these
commands yeah recording this and to save
time I do not want to jump between F and
C go back and forth back and forth so
what I have here is just in plain code
the statements the secret code how it
would be executed by an F so this is how
that would hit the fan now just we
have it a little more transparent
okay fine set
yeah finds that again this will select
all the data in the filter here I just
have no plainly coded a filter and I'm
using this account number here this is
the one with the smallest entity just
for records on this account I didn't
care about sorting order so I didn't
specify a set current key so in a vision
would fire automatically primary key
sorting now I'm enabling some black
magic on the sequel server and this is
so that I can also see the number of
reads and management studio and stuff
like this I enable the execution plan so
I can see what SQL server is doing
behind the scenes so now execute this
fine set command of course it's just for
records in messages now we can see the
logical reads the box number of boxes to
be opened 15 reads one read is one page
at a trilobite
so as a very small memory pressure
everything okay the execution plan show
us here when I would go mouse over its
using this index dollar one to see and
tala one this is the index based on
account number posting date so why is a
square so we're using that index because
as curse of always tries to find an
index
based on the where Clause of a query and
that's the content if I ask you get me
the red pencils you need an index
knowing something about the color it
would be pointless to know something
about the links or something so this is
what SQL Server is searching it found
this index because it already existed
having the right indexes challenge
number one in this case I have a right
index which could be used so SQL Server
now could seek out the desired data so
what else does it have to do and I
didn't care about sort order yeah so it
was sorted by primary key well this
index here is sorted by account number
of hosting date so now what SQL so it
has to do is has to pump the data in RAM
and temp TB and so we have another sort
operation here so that shows that
theoretically and I don't have to
specify a set current key command as
well server is designed to deal with
this kind of issues to filter this way
and to sort another way and it doesn't
do any harm so that means basically a
set current key is not mandatory for now
okay and we see the cost down here yeah
the costs here and that's a relative CPU
time so it has to total up to 100
percent but we see that it is about half
of the time spent just on the stupid
sort so it doesn't come for free and
this sort operation and why 15 reads by
15 read again this table the clustered
index is an entry number so 1 2 3 4 5
and 4 out of these 3 million records and
met a match to this account number but
these four records that can be anywhere
that can be in this place at this place
at the rear end of a table so SQL server
has to walk through the index branch and
small couple times for records 3 index
levels 12 reads yeah 4 multiply to 3 12
reads plus some extra magic that's
totaling up to 15 which in this case
so but basically that was working okay
so now comparing with a find - command
find - at first will issue a select top
50 again this top Clause is
automatically generated and it will very
I just use it as an example so when
doing this with a find that find - guess
what it is exactly the same kind of
operation because I feel for records I'm
way below this top Clause nothing
happens so now question about set
current key or not set current key okay
just try so now if I was setting a set
current key command my order by Clause
would be changed so the order by clause
would be something like this yeah so in
the vision I would say set current key
GL account of opposing in yada yada yada
and run the same code so doing this
again hopefully again for records the
i/o hasn't changed it's the same kind of
way to seek the data the execution plan
is pretty much the same it's using the
same index but what is gone now is the
sort operation so what does that mean so
far you have to have the right indexes
to support the where clauses to support
the filtering this is the number one
having the right index set current key
is not mandatory but if you have a key
you can use then it's a good idea to use
it because you make life easier for SQL
Server yeah but it's not necessary so
that means if you have a key use it but
if you don't have a key you don't have
to necessarily create it bear in mind
that every index has some cost every
index needs to be maintained it means
need spirit in its disk space and so on
so theoretically reducing write
performance so we must not be too
enthusiastic and adding indexes to the
system yeah so the means if you don't
have a key then you first have to see to
monitor if there's a problem if you need
that key in many cases it might be not
necessary it works like a charm
okay so far that was our kind of
best-case scenarios now spoiling things
a little bit and or maybe before
spoiling this because on this thingy
here which you also can receive in this
download package and stuff like this I
also have a code on these other commands
yeah fine first find last five - and so
and I hope you believe me this actually
is all pretty much the same and all
these methods need to have the indexes
yeah so because there's some some let's
call fake newsroom misunderstand some
methods don't require an index or
there's an empty will always work it's
total and so like if I ask you
a fine set I get me all the red pencils
you need an index get me fifty a red
pencils you index fine first get me the
first red pencil get me the last one
check if there's a red pencil to counter
red pencils you always need to have an
index so all methods require indexes so
that means that all methods here can
work like a charm but they also can all
screw up and I show you now am how so
now I'm switching to an account number
with a very different density this
account number on this account number I
have 800,000 records and GL entry so
that is about 25 percent so the query
now is exactly the same as before go
fine fine set again so exactly the same
as before same code executed so the only
difference is that the content of the
filter has been changed so now this will
take a little while again this is
800,000 records and a slow machine
anyone a joke newspaper to read on
so it takes about 20 seconds feels like
an hour so but almost there so I said 20
okay so check in on this messages so
logical reads 125,000 logical reason
that is that you ring a bell
does that figure sound familiar and this
is exactly the total width of the
clustered index so that means now SQL
Server had to open all the boxes
checking on the execution plan I can see
yes it is doing a clustered index scan
going sequential because in this case
index seeking would be totally pointless
what what you do 800,000 records that
means by statistic every fourth record
is one of those it would be totally
idiotic to go through the index field
like like a Skrill of thus missing a
line of coke yeah
up and down up and off no way this
doesn't happen so as cursor gives giving
the finger and starts to read sequential
okay so but now having a closer look so
now what we did we added a set current
key command because current key would
make life easier for SQL Server that's
what we thought but holy moly
happens is that exactly this sort
that makes it extra difficult also in
this case because SQL has decided now to
scan the the clustered index are going
sequential and the table is physically
sorted by entry number now my query was
asking to sort the data by account I'm a
posting rate so hels belles it has to
pump all the 800,000 records into temte
be to resort hmm yeah and this just
because the data density has been
changed that just changing a single
filter value here makes a total
difference there between bliss and total
loon so to speak yeah and the same would
happen also with the other yeah and
fine fine - yeah fine - some people
would say hooray this is very quick away
could use all those fines me - or
something yeah it was quicker yeah
hooray hooray hooray hooray
it was reading way less hooray hooray
hurry it was scanning but not that much
okay by me but this is just half of the
truth because that was just the first
packet yeah that was the first fifty
because then I get a second round-trip
fetching all the remaining data which
screws up like the previous finds the
set come on
yeah so that's not really any any
benefit here yeah
so that's love things that obviously
matter in the execution of statements on
SQL server and there are also things
that I even do not show yeah this is for
example the type of filter also matters
there if it's greater less than equality
filters inequality filters so just
arrived this little on what else could
we do maybe to improve Clary's like this
the physical sorting order has also
impact on this performance yeah in this
case the fine set was reading all in
everything
no the fine set at a you remember I
don't execute again so it was reading
all in everything yeah
opening hundred twenty-five thousand
boxes so what we could do is change the
clustered index changing the clustered
index means change the physical sort
physical order of the records I cannot
do this on the original gln to Terry
because it will take forever this is a
super heavy transaction this is
definitely something outside business
hours yeah so I have prepared this
already so now this GL entry to is a
copy of the Ori original one just here a
cluster the data on this account number
posting there so that means now that the
records belonging to the same account
number a close together
so now I'm firing this query on the
steel entry table number two still it is
eight hundred thousand records in a
newspaper you had some time to fetch
some know anyone a joke one-line joke or
something I should have prepared one yes
five seconds to go so almost there
take care I said twenty okay so here we
are again so now what has been changed
so the number of records hopefully not
yeah so what has been changed is now the
i/o a little bit yeah so the next time
was not that visible but now we are down
from hundred twenty-five thousand reads
only to 30,000 reads why now again all
the records belonging to the same
account are close together so esker so
it doesn't have to read the full table
it only has to read a small portion of
the table
thirty thousand reads that's roughly a
quarter of the whole table a quarter of
this hundred twenty-five thousand which
is plausible because there is also a
quarter of the whole records so for this
query actually this best-case scenario
so this of course would also help the
other accounts now if I go back to this
one here that was the one with a very
low density oh sorry that was wrong
button so for records again but now I'm
down to even four reads yeah previously
it was fifteen reads because it has to
seek there and there and there in
different positions now everything is
close together so SQL just has to go
into a position maybe read the next few
pages and that's it yeah so optimal
performance here and of course the
execution plan is very lean just one
operation here without any sort and so
on
okay so just to give you some examples
how this kind of code executes in the
secret world just to recap so there's a
lot of things that matter so first thing
where you your magic starts is to you
have to avoid the round trips but sooner
or later some select statement will hit
SQL Server and the same statement could
work like a charm or it terribly screws
up so there are several things that you
can influence yeah you can influence how
you filter having the right index that's
the the important thing here without an
index you're always screwed you always
have to scan so you need to have the
indexes sorting could help yeah so so
how should you program you have seen
sorting helps in other cases it screws
things up even more you others have to
target the supposedly best-case scenario
so yes you should use a cell current key
if you can and because what I did was of
course a very extreme example in in real
life that does not happen that easily
yeah it could happen but must not so you
have to target the best case in error
because the the big unknown thing here
is the stupid data density which which
could dramatically spoil things and
unfortunately if you if you start a
nooner vision system and a Cronus
database you have no data density at all
yeah this 500 megabyte database this is
how performance testing is done in cope
made yeah but you see but but then the
system will grow and grow and grow and
grow so that means the data's density in
the system changes with every insert
update delete we are doing so that means
that the SQL Server behavior could
change from one second to another yeah
it was seeking properly right now and
just next minutes giving you the finger
and starts to scan this will happen and
unfortunately this is a natural thing
and this is something you cannot predict
from your programming perspective so you
have to do the best you can do in your
seaside world but you have to expect
that sooner or later the will hit
the fan and again this is not
this will only not happen if you do not
process any data and maybe to keep this
up in advance this is not necessarily an
F problem yeah this is thingy that you
have also in ax and CRM in any sequel
database this is not even a secret
problem this is something you also see
an SAT in Oracle this is just how this
relational databases are working yeah so
and so again and that some queries
screw-up is natural and then we have to
deal with this afterwards and to find
out if behavior changes if anything
stupid happens there is a variety of
tools you think I mentioned a lot of
them and I want to show you just a
simple script just a TCL script and that
is doing this whenever SQL Server is
executing something its memorizing it it
has a thingy part of brain called
procedure cache where it just knows what
query was executed how often and how
long cook it and and so on so in this
script is just looking up these dynamic
management use and here you can all you
can see everything that that happens as
you see the query statement you can see
how often it was executed that also
could help in identifying maybe code
that has a maybe too high a number of
iterations somewhere we can see the
number of reads yeah the number of reads
this is the most significant indication
for performance issues the more reads
the slower the performance this is kind
of rude yeah so we can see the number of
rows that which are returned and also
maybe could help you giving guidance for
your code may be the result sets are too
large maybe the filters are wrong or
whatever and of course we can check on
the execution plans so we see really
what SQL saw was going so the means with
this script
you can quickly investigate if any
expensive queries have hit SQL Server so
this script is grouping and counting in
this version here is sorting it by total
CPU time
was spent so they have the most CPU
consuming queries on top so that you can
see okay what's doing real harm to the
system how often is the thing incident
is it a recurring problem is it
something you have to fix or maybe can
ignore postpone so when it's about
fixing problems and if you beyond this
point of code iterations and stuff like
this and these kind of expensive queries
the very vast majority of them could be
fixed just by index optimization an
index optimization mostly means just to
add the required indexes one way or the
other
typically way how you are doing it so
far is you do this in your seaside
environment as a table key every key
will automatically be put as an SQL
index so but this is something and
unfortunately don't have a time here in
this session and to discuss this really
thoroughly and you have a second option
to do the indexing you can do this on
the database spec and directly because
that is the place where you can do the
real deal yeah because the original
indexing sucks
maybe indexing tenerife indexing
whatever you called I innovation
indexing sucks yeah so SQL site indexing
rocks because here you have a lot of
magic features to really create
sufficient
indexes that improve performance but
this SQL site indexing is something you
have to learn this is something and you
need to know the do's and don'ts with
them so many things and because if this
SQL site indexing is done in the wrong
way you can thoroughly and completely
up the database yeah so this is
also promised and no so this is
something you have to look into how this
is done and which is no rocket science
you can learn this in the easiest case
if there's a very very obvious index
problem SQL Server I can see that SQL
Server knows as part of the execution
plan that there might be an index
missing and these
index proposals can be collected there's
just another dynamic management views
where you can look up these proposals
and then if you know how to do this or
not
then you can directly create these
indexes on the database but the big
disclaimer now these are machine
generated proposals and these proposals
often contain nonsense let's call it
nonsense I'm swearing too much I almost
there to say mother say
nonsense yeah okay like this here yeah
this is not necessarily a good proposal
because if you could follow so far this
is something we already have we have an
index slash key like this already
it wants to include all the columns
included column is one of these super
cool features in SQL world we don't have
in the seaside world but here this is
included columns used in a stupid way so
this doesn't make sense here so in real
life this should never be created but
then again you can tap on these missing
index proposals create this stuff that
takes a little while three million
records again do's and don'ts you have
to know that so but then that means now
the index is already there and asked us
or could immediately use it without you
changing any metadata yeah you don't
have to change anything not recompiling
anything not restarting any service tier
you just add this and SQL so it is
immediately able to use that index so
the question is how to document how to
manage how to roll out this here I want
to provide you a second script this rece
crypt index and stuff like this this is
a script which is listing this custom
build stuff and also checking on the
usage of this index Asia if they're
really
if they are not helping if they know
helping well then drop index and so on
yeah actually the code to drop or to
recreate is already prepared now so this
is some some easy script to handle this
index world outside the Navision
application world which could be a huge
advantage but last time i say that you
have to learn that yeah otherwise you
can do real damage to a database if you
do what I always say in the training is
and never ever copy/paste execute this
yeah if it was that easy Microsoft to do
it and but I recently learned Microsoft
is doing it and no not really in in Asia
you have some feature like auto indexing
yeah we were discussing this we were not
sure how which egg reasons are behind
this but obviously this kind of auto
indexing feature in Asia we have to
check it out okay yeah so index
optimization and I was focusing on this
script for one special reason and
Microsoft is pushing us into the cloud
with ultimate force like it or not and
depending on the cloud scenario you are
running you are not able to run profiler
or extended events or anything this kind
of information expensive queries in
missing indexes you get in any scenario
regardless if you are on premise or if
you are knee-deep into the cloud the SQL
as telemetry sticks will deliver
something like this yeah so this is
something this expensive scale because
it's SQL stuff that is already there
they are even standard secure reports to
tell you about this stuff and and this
is why I highly recommend to get
familiar with these kind of scripts and
an SQL code because this is something
you suppose we will always have
available to investigate expensive
queries yeah if you cannot run profiler
for whatever reason and so on yeah also
with this missing indexes the super cool
features and and one way or the other
you can work with this
well
so so for your programming again you
should code for your best-case scenarios
as good as you can as good as it can
predict what will happen this is a super
challenge you have to face yeah but you
have to have in mind there are
unpredictable things that will happen at
one time so that means you have to
follow up on this
so just writing code and then roll it
out and execute doesn't do the magic so
you have to test as good as you can if
you can test always on real-life
databases or copies of real-life
databases because that's the only way to
check on this data density and again you
have to repeat this maybe yeah so it's
not a one shot firefighting this kind of
index tuning because what's not a
problem today maybe it's tomorrow a
problem so you have to check on this
periodically so there will always be a
demand for new indexes that also means
that other indexes become obsolete and
can be disposed one way or the other
yeah this is an eternal circle of life
but but then again this is natural yeah
so this is not a malfunction of sickle
or an F or something this is just how
these databases work well so according
to this what also is important when it's
about this density stuff here yeah how
does SQL server know how many different
field values are there and so on you
also maintain statistics and to have
these statistics accurate you need to
have some database settings enabled that
is at least Auto create statistics in
auto update stats enabled in years ago
there was different best practices but
nowadays there's online optionally you
can also add the SN Crona statistic
update that postpones the time a little
bit when this is updated for the older
SQL server so SQL Server prior to
version 2016 there's a little issue
these auto update are there statistic
manager it depends on built-in change
thresholds and the
built-in threshold in the older SQL
versions is 20% so that means the 20% of
data need to be changed until the
statistic manager will update these
statistics that means if you have an
item that your entry table with 1
million records it requires two hundred
thousand records to be changed before
the update happens this is not
sufficient yeah this actually will never
happen they have changed in sequel 2012
yeah they use dynamic change flash hold
or some black magic automatically
calculating and based on the table size
but you can enable this also this with
this trace flag 2371 for the OL I think
it's even available back to ask 2008 r2
and this could be beneficial for large
databases where you have large tables
and so on also well just just have it on
the slide to be complete what what
matters in the query execution is the
number of CPUs used so there's a setting
and an SQL Server instance the maximum
degree of parallelism and current best
practice is set this to two regardless
of the number of CPU one or two that's
the setting here and what also could be
important is 10 DB optimization temp TB
normally is only used in combinations of
REM for salt operations and work terms
and stuff and the vision doesn't create
any objects in the tempie beii so and in
store any data but these sort operations
are also kind of unpredictable yeah so
we can have two records to be sorted
could be two billion records to be
sorted so tempted me to optimize it
means you need to have one data file per
CPU no more than eight if you end on
heavy high loads scenarios with lots of
transaction volume also might be
beneficial to have tend to be on a
separate physical disk or whatever and
to separate the physical i/o but then
again this is totally different story
just have it on the slide
for you to remember maybe to follow up
on this an SQL Server 2016 when you
install it it will already proposed the
correct tempi be set up I will propose
how many files
should create yeah but also what is
necessary in this context of query and
index tuning is maintenance these index
structures they fragment here the gaps
in it and kind of
so these indexes need to be fragmented
yeah sorry d have fragmented and here I
just have an example for maintenance
plan this is targeting SQL Server 2016
and higher but with maintenance to make
a long story short it doesn't matter how
you do it it's important that you do it
and you can do this as maintenance plan
you can do this with third party tools
yeah there's a zillion of stuff rod I am
providing tools you all know the tools
parola high and green so it doesn't
matter yeah there's just little
differences and what these tools are
doing we can say that the old
maintenance plans yeah prior SQL Server
16 they always take the longest time and
have the heaviest impact into the system
err regarding transaction volume a
transaction lock load and so on yeah so
maintenance means index defragmentation
and statistic updates also one way or
the other and this is the most important
thing this kind of clarion index tuning
is database maintenance this is not just
firefighting yeah Oh getting rid of a
certain from this is something that you
have to do frequently this is a task a
job that is done by thousands of DBAs
every day so this but this also applies
to our own effort therefore the partner
this could be our chance for making
money as we can sell this as a service
to your customers if the customers don't
want to do that so when you go live with
a system in a new system this is
something you should maybe check in on a
weekly basis later on if everything is
smoothly then there won't be that many
changes then everything is more less
stabilized and it's okay if you check on
this every three months and every half a
year or so but you need to repeat this
yeah you have to expect something coming
up and again this is normal so
so no hard feelings on this yeah that's
actually what I wanted to share so
should we wrap it up a little bit so
your conclusion final words yeah for my
part it's really simple like one of the
first slides minimize server on tips
that's the key takeaway really so coding
for performance is mainly about that and
then there is the application footprint
kind of issues which is typically
reports and dotnet but when writing code
minimize database on trips find and find
sets use them as as documented on that
doesn't matter if they run with a
millisecond difference
they all have constant execution order
so they're fine yeah so plenty of code
well plan with iterations in mind so
right scalable code
yeah and my final words then is check
out how to tune indexes in with index
tuning index optimization you can fix at
least 80 to 90 percent of query problems
that hits SQL Server so this is the most
important thing you have to do it you
can do it it's easy to learn yeah
there's another 20 people around who
have just learned it the past few days
and this is most important because if
you have learned this SQL magic adding
to your Seaside magic then you can
really really tune your code and then
you have really program code that really
works on the system yeah so we have 55
seconds left for Q and a so yeah so only
ask questions we can really answer so so
we should use these things here should
be um yeah so I'm blinded sorry I don't
know who hit sir
they said well is it on yeah now you
shouldn't think about the database
compability level just use the highest
or is it in the in the supported
Navision scenarios you should always use
the compatibility level matching to the
server ok so enough to go hide and
recommended know what is recommended now
if you have an older mission we
shouldn't go too high yes the
compatibility level defines the language
of database peaks or the syntax
interpretation so and of course you
should have always the server level
because then SQL so internally could use
all the features and benefits it has
otherwise it's inter you only need this
in a in a lower level if you have your
own siku code that uses old syntax but
for nav this does not apply in a vision
always requires the server level it's
just because on the the Khronos demo
database is on 2008 and because we get
and everyone forgets to increase it but
this is not the recommended level it's
just forgotten to upgrade ok thank you
ok
first me first no I played with it a bit
maybe talk to the t-shirt that works ok
I have been bumping a lot done doing
reporting so you're talking about the
data set optimizing but in my opinion
and my experience also pointed out that
it's very useful to to create temporary
tables where you collect the data before
you run the report so that's something
that I rarely have seen nobody anybody
tell how to optimize things and so you
do processing in tap tables and then
just send out it's basically finished
output - sounds like a good idea well
that's
is optimizing data set in a way that the
resulting is optimized data set well
it's a good the great suggestion I don't
know why nobody blog it I don't know why
nobody example like that but whatever
will optimize your data set this is the
correct solution so that sounds maybe to
add to this temp temp records are
maintained directly in the REM of the
southeast here so you save the round
trips to the SICU server and this is why
you save these iterations and speeding
things up yes the reporting are usually
and this is correct but the problem with
the reporting is usually on sending data
to the client side after they've been
processed on report side so the amount
of data is the problem rather than
anything but yeah if you narrow it down
to your temp table possibly processing
to do just what needs to be displayed
and yes that helps thank you thank you
if you see that the most common wait is
a sync Network I out is that a bad thing
and what's the most likely cause sorry
if the movie if the most common weight
that we see is a Seng Network IO is that
a bad thing and what's the most likely
cause oh well you will see it and you
will see much more of it than you used
to in earlier versions for the simple
reason that before we used to do the
cursor fetches so you sent for 50
records they come back server does this
processing and repeats the process not
now there's this multiplexing where it
fires off and the tasks for everything
back in in one go so the sequel
processes that very first and place it
this or everything the packets are they
for server that still does its work so
gonna see that much more than you used
to see because we changed the whole
technology and took away the expensive
slow cursors the only reason you saw
less of them before is because basically
NST was
processing and when it's done with
processing then it sends for right so so
basically that there were no there was
no room for async weights that was a
synchronous operation now it's not so
you're gonna see them but if you will
see a very many of them then there are
normally few things pages tend to
generate a deal of them because they
read kind of optically doubt they'll
read everything but but fine set because
find will try to in optimistic hope get
some self tuning number of records in
optimistic hope that will cover units
and you might never ask for the rest
while points that will just pack
everything leave it there for you if you
don't actually consume it it will be
hanging around until the session is
stopped or until buffers are full that
you're gonna see more of them it's a
natural before comparing to before 2013
so you will see more than but if you see
too many or increase your memory and
watch out for points at encode use find
[Music]
one last question one practical question
we have okay 20,000 invoices periodical
posting during given night when in was
posting two seconds everything is fine
pretty complicated English I mean and
few times per quarter let's say
something happens and performance
decrease that's a free or even four
times
nothing nothing happened on service
service dedicated for only for nav no
maintenance
no jobs no nothing and my question how
would be possible somehow to trace what
is going on what is makes with the tape
occasional decreasing of performance
significant decreasing yeah if I should
take this up and as you said this was a
complex to me because they can these
three things it could be the platform
screwing up it could be the query
performance and it could be blocking
maybe so I'm afraid this is something we
should take up offline this is something
because that could be anything with this
script you can check on the query
performance if that is a problem in such
an index problem but that could be could
have many many reasons if it is the same
process running on same dedicated
overnight so no it's not yeah but
there's always there's always
explanation yeah your question is how to
find it well one of the things could be
the statistics updates they would
naturally update each time but do you
insert as many records each time that's
the question so maybe the statistic
updates kicking at some time and consume
some at that time maybe as he said QA
plans go for any reason some data
distribution is important so if you
suddenly if your invoice is a bit larger
so if you suddenly inserting a volume of
records that that are similar to put it
that way that that creates a different
data distribution then somewhere along
divide the QE plans will kind of break
or won't work as well so you can use the
the nice QA plan script you're talking
which is available for download on my
block right now to check if the curate
plans changed you can check if
statistics kicked in yeah it's a complex
not simple questions people are thirsty
me too
yeah we are around here the whole days
so if you have any questions if you drop
by and
thank you very much
