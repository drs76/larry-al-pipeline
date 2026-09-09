# NAV TechDays 2014 - SQL Server Sizing & Configuration for good performance

- **Source:** https://www.youtube.com/watch?v=Ew7MFW8uIII
- **Video ID:** Ew7MFW8uIII
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 100m51s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

yeah hello everybody Welcome to um the
last session for today um before we
really start please um show me who
attended the previous session from
dimitro and and
David okay very good because you will
see that these two sessions really yeah
relate to each other so and there might
might be a slight overlap but then my
focus will be more on the ESL server
world and not the service
World okay before we start um I'd like
to briefly introduce myself my name is j
I'm in the N Vision World for quite some
time in the meantime I have a 100% focus
on ni SQL performance um yeah issues and
everything that is in touch with this so
there is a chance that our pathes have
crossed in the past
already okay so performance it shall be
performance it will be
generally when we talk about performance
issues we always have three major areas
it actually starts with a platform the
hardware the infrastructure that is to
carry all the system the esos over the
database and the application so
infrastructure platform Hardware this is
most important
thing um the second area that is about
query strategy indexing and stuff like
this this is how nav Vision communicates
with the SQL Server David ref refer to
this at the end of his session yeah that
is all about indexing expensive queries
missing indexes and all that stuff and
the third big area is all about blocking
and deadlocking this is a little bit of
application technology but a lot of
workflow and business process
design so about these previous sessions
um or the other two topics there have
been some sessions in the previous Tech
days events so have in mind that these
session record are still available on
mbuso for download so if you like to
follow up in more detail about these
other
areas today I would like to talk about
platform Hardware um which is actually
the most important part of
everything the platform the hardware is
the thing that is the fundament um on
which the ESL server is installed SQL
server needs to be configured and so and
then the SQL Server is maintaining
servicing the databases and on top of
this of the databases there's the
application code our dear nav using all
this system
underneath what I never dare to put on
this slide is what is missing here um on
top of the uh of this pyramid this is
our dear user yeah sitting there and
crapping down on this um yeah there's
the mean saying that half of the
problems are sitting in front of the
screen but this is hardly something we
can do anything
about yeah so Hardware platform is the
important
part and it's um also to have in mind
important to have in mind that if we
have Hardware problems these are the
ones that are the easiest ones to be
fixed so when we look at the at the
time oops we need to spend to to fix any
issues hardware issues are resolved as
fast as possible um for example if we
find out
that that our dear SQL Server is lacking
memory yeah we just don't have enough
memory a memory problem so if you have a
virtual server in the easiest case it's
just moving a slider from 16 gab to 32
gab and the problem is resolved nowadays
you don't even have to restart the
machine problem gone if you find out
that whole business processes are
designed in the wrong way yeah uh that
you have to cut open any code units this
embow them them and and recreate them
from the scratch so when we on top of
this pyramid this takes way longer to
fix these kind of
problems so you might
ask if the platform is so important why
is this session coming so
late um because you ask for it nobody
ever would volunteer to present a
session about Hardware because this is a
game you can only lose um talking about
Hardware is talking about technology and
while talking about this I present out
there ated
information and to design the perfect
platform is really a challenge and to
give any guidance here is an even
greater
challenge if you remember n Vision 5
service pack one um there was an attempt
from Microsoft that provided a hardware
sizing guide this was kind of table
sheet where you can say uh you could see
the number of users the database size
and then you got recommendations of how
many CPU how much RAM what dis system
and what esql server Edition you should
use yeah by the end of the day Microsoft
was whiplashed for this proposal because
those of you who really obeyed this
Hardware sizing guide really regretted
it because it it it doesn't work it
cannot work the problem with Hardware
sizing is that there are way too many
dependencies it it really depends on the
individual installation so there's many
questions to ask if you have a bare
metal in installation if you have a
virtual environment do you have private
clocks um what how the clients interact
so do you have land connections van
connections Citrix connections and
everything do you use Sand Solutions and
stuff like this so there's all a lot of
dependencies that need to be
clarified So It's Tricky nonetheless
I'll give it a try so during this
session I would try to give some
guidance of how Hardware components
could be sized give you some formulas
you can
use so that you are enabled um to create
a robust and scalable system always
having in mind that whatever I say needs
to be put into your individual
context
okay just a second
okay um the first thing I'd like to
demonstrate is how to monitor
performance those of you attending the
previous session have already seen
Windows performance monitor is the tool
to find out um how Hardware is working
um for those who did not attend I'd like
to show this
briefly whenever you install
something on a Windows computer
this component or this software can
install lots of indicators that provide
information about health status or
whatever
information so this information is there
already installed by the
applications um the windows performance
monitor is just a tool that is able to
collect this information uh to save it
to record it and to visualize the
data so once you have started this puff
one and my apologies that this is a
German installation as every year
so it's an easy tool you can open this
and then with a simple
add so you can collect an assembly of
indicators from the local computer that
could also be a remote computer whatever
and then you see that all kinds of
components that are installed in the
system provide this kind of information
yeah from NET Framework operating system
down to the SQL Server instances and as
what you have seen in the previous
session also the navision service tiers
provide information
here so you can yeah pick the indicators
of your choice and whatever this should
be I know this
ASP so something like physical
dis and as you see there's a lot of
indicator
and then every indicator is split into
multiple instances so there are zillion
of measurement points you can take
in so the clicking around is easy but
what you have at the end here is a
non-persistent setup so whenever you
close performance monitor all this all
your assembly is just gone so that's why
it's more feasible to use so-called
counter
loocks this is a persistent set set up
of indicators you can create this in the
same
way but the big Advantage is once if you
have created such an assembly you can
export this as a template and reuse it
so it's portable so you can create your
assembly at home and then um yeah take
it to your customers or wherever you
like so I have prepared such an
assembly and all that I use and what I
show is already uh there for download on
my blog so you get these kind of
performance monitor templates there's
also a template for monitoring the NAD
server SQL server and
everything okay so this is a template I
have prepared for this environment I can
tell where to save it maybe the security
context in which it should
run and then I just have a predefined
assembly of account of counters that I
would like to monitor so this is a lots
of indic
throughout the whole system so from
memory CPU Network Diss and SQL Server
so all and
everything um what I recommend to do is
when you have this kind of setup always
save into a file it is technically
possible to also save into a table but
table data is hardly portable so if you
save it to a file you can always do the
tracing for example on customer side and
then pick pick the data up and do the
investigation in your home office
um The Collection I have here is defined
to sample in an interval of one second
this is the highest one possible and
this is really necessary to have such a
high frequency to really get a sharp
picture um downside is this assembly or
this collection roughly um collects
about 100 megabytes per hour so this is
nothing you should run doing all the day
what I recommend is to do this kind of
performance monitoring um during
different times in the day so maybe two
hours in the beginning in the morning
when the business starts up two hours in
Peak load two hours at night time
whatever is suitable so I have multiple
snapshots but with a very high frequency
the reason is that that most operations
that happen in SQL
Server um are handled in within micros
seconds yeah um or at least milliseconds
so even an interval of one second is
pretty pretty long and the longer the
interval the more information we miss
yeah so once this is set up you can
start this manually or and this is the
huge Advantage you can also schedule
this tell when to start when to stop and
so on so with this you have an easy way
to monitor how the platform is behaving
and in the following I will highlight
some of the indicators and tell you what
you can learn from these indicators and
how to investigate uh this information
to
learn about Hardware
problems and how to resolve them
probably so this is an onboard feature
um provided which is available in any
any Windows PC any computer has this
Windows performance monitor when it's
about SQL
Server there's also a little
thingy um where we can have a little
insight into the infrastructure here I'm
presenting a script created by Paul
renle this is an SQL guy here writes a
great blog SQL skills.com so I highly
recommend this and this little script
here is reading out the so-call weight
statistics of SQL
Server okay yeah es server is waiting
always for something so nothing works
infinitely fast um the question is what
it is waiting for and how long does it
take yes and here there are indicators
that are related to platform like IO
that's something to do with a disk like
page iist there are indicators that
refer to the
network um and there are other
indicators that refer maybe to the
application like blocking issues or
something like this so that means also
from an Esco server perspective we have
a chance to get a clue about maybe
hardware
issues okay
okay so when discussing how to size a
bare metal installation yeah the reason
why you are here is that we not talking
about Asia and cloud and everything
about the fluffy stuff here we talk
about heavy
metal um
okay yeah
good okay so the first challenge to face
when you set up an s server platform is
to pick the right addition uh of the
server systems so you need to be aware
of the limitations that a Windows server
has and an SQL server has there are
limitations respect of using the number
of CPUs of using memories and as you can
see these limitations change from
version to version and this could be
sometimes really really annoying because
if you see in SQL Server 2008 R1 and
R2 the SQL Server limitation is higher
than the operating
limitation yeah so if you think you go
for standard league and have a Windows
standard system and put on top of esqu
standard system your limit is not 64
gigabyte it is 32 GB because Windows
over
ruls yeah pity for those who started
with Esa 2008 release one they could
have maybe an installation with 96 GB of
memory then they think they're just
upgrading to the new version R2 and
there's a limit of
64 yeah this sucks big time then so you
need to be aware of this limitations
because later on when we calculate the
number of CPUs and the ram we need um
this might spoil the
thing what I personally recommend is
whenever it's affordable always go for
Enterprise on the on the Windows layer
because then you are unlimited um and
usually Windows Server the the pricing
is not that uh yeah not that high the
price between difference between
standard and Enterprise is not that
dramatic with SQL Server this might be a
bitter pill to swallow because the price
difference between standard and
Enterprise is yeah dramatic so cost for
an Enterprise Edition nowadays is a
decent German car up to a small house um
just for the
licenses okay so the first component I'd
like to talk about is the
CPU so just generally speaking um a CPU
um talking about a physical CPU also
talking about a socket this is just the
chip that's that's what we call the
socket every socket every physical CPU
nowadays is split into multiple
cores and each core could create
multiple
threads so nowadays we have always uh to
distinguish between a physical processor
that is talking about the socket or
talking about The Logical proc
processors that is the threats and here
also it is important to know that
licensing model has changed in SQL
server in the old days if you had to buy
SQL server on a processor license the
old days means up to SQL Server 2008 R2
we could license on a socket base
nowadays we are paying for the
threats yeah so this is um way more
expensive yeah what is the CPU about CPU
is the the thing that is actually doing
all the work in terms of nav and SQL
Server um the nav server is asking the
questions and the CPU is creating these
questions vending into the ESL server
ESL server is the thingy that needs to
answer these questions to process the
queries from es server so the challenge
for for the CPU is to process the
queries so it depends on the number of
queries that are fired from the SQL
Server so when we want to have a
a rough formula how to size the number
of
CPUs nowadays you can say approximately
one logical CPU One Core is fair enough
for 20 to 25 users so if you're going to
run an AV with about 100 concurrent
users yeah so you need something in a
range of four to six CPU
maybe in the old days the rule of thumb
was one socket per 100 users yeah but
nowadays we cannot talk about a socket
anymore we need to think
threats so that's an easy formula um
what we want to achieve with this by the
end of the
day um the CPU load when we monitor it
with Windows performance monitor should
not exceed this range between 15 and
25% as a rule of Thum you can say room
temperature room temperature load German
room temper or european centigrade
um this is a
fair a fair workload for a CPU in some
older in Microsoft documentation you
might see that um they say Okay CPU is
dead when you start to incre exceed the
threshold of 80% or something like this
and I say if your average CPU load is at
80% you're Stone dead and didn't hear
the shot so um and I show you later on
why this is the case so in all these
slides they always built the same way on
top I have these windows performance
indicators that can give you a clue
about upcoming problems um and then some
brief sizing rots and also some stuff um
you need to be aware regarding the
configuration so for the window for the
CPU um
one thing that is always forgotten on
any SQL
Server you have
to remember that nowadays all the
windows servers or all Windows operating
systems are using power plans and by
default they are switched to to balanced
and balanced means that um Windows is
reducing the CPU speed to save energy
and of course this is absolute nonsense
yeah es should not say energy it should
perform so this is the first thing to do
really to switch the operating system to
high
performance um there's also a bio
setting um which you have to regard so
if the bio setting is also switched to
power mode uh power saving mode this
needs to be
disabled yeah else the system just will
not use all the system resources so
slowing down
okay so within SQL Server there's one
setting that is highly discussed um
there's only one single set setting that
has to do with a CPU
configuration um for
now and this is in the es server
instance properties there's a setting
that is called maximum degree of
parallelism
and this is a mean thing um you have to
be aware
of um in previous sessions we were
talking about expensive queries so
there's queries that put a lot of stress
on the RAM on the CPU and anything with
missing indexes and stuff like this if
such a query happens then SQL Server
will
split this query into multiple CPU
threads and this setting here tells a
scuro how many threats it could
create zero means use all the CPUs that
are
available and that bears the risk that
if you have one of these expensive
queries that one query splits up into
eight threads in my case and overloading
all the CPU so one single user one
single query could create a global
problem and for that reason it's always
necessary regardless if it's an nav SQL
server or anything else you need to
reduce
this and the best practice is to reduce
this to the half number of CPU or to the
amount of CPU you have in one Numa node
at my machine I have eight CPUs so I set
it to four because that means that
queries still can benefit from a decent
amount of Paralis they can create four
threats but it doesn't happen that one
query is overloading all the
CPU so this is um let's say a common
best practice for a vision in many cases
that's not even
enough um even we have relational
commands we have these page queries with
the smart queries um how flow fields are
quered and stuff like this these are
queries that indeed can benefit from
this kind of parallelism but most of the
nav queries are plainly stupid simple
yeah so if you ever have looked into a
vision query a select command filter
where order by there is nothing to be
paralyzed and with a vision something
weird happens that's called parallel
index scans and to avoid these parallel
index scans you still find it in some
configuration guides from Microsoft that
for nav best practice is to switch it
down to one one means one query is one
threat um so we we suppress all kinds of
paration which is fair enough for no
vision but of course that's stupid for
anything that is intelligent in this
system so all the system maintenance
backups index maintenance Integrity
checks all these kind of operations will
be degraded
because that's operations designed to
run on multiple threats and now you
suppress this
so yeah what's good for an nav is not
necessarily good for the rest of the
world so I suggest to do this start with
a half number of
CPUs and then in these weight statistics
there is en counter that's called the C
expected
weights this tells if you have any
problems with paralyzation if too much
much time is spent for this
multi-threading and if this counter is
in the top ranks so with this script if
it's on the rank let's say in the top
five then you need to decrease the C
packet weights further down so then you
should do it step by step so the first
step is half number of CPUs in my case
four The Next Step would be two and the
worst case is actually one yeah
unfortunately especially in the old na
versions before 2013 you often end up in
having maxtop um one
there's one indicator that is most
important if you are running virtual
environments um on a virtual platform
you have a virtual host that has aite
amount of Hardware resources a number of
CPUs a number of memory and so
on and out of these V from this virtual
host you are able to create your virtual
servers so you assign a decent amount of
RAM and CPU to the server and so on and
hell will break loose if you do some
over provisioning or if you if you
overbook the virtual
host an example you you have a a virtual
host a physical machine with eight CPUs
so you only have eight physical CPUs or
logical CPUs sorry so that means you can
create two R servers each of four CPUs
or you can create four servers each two
CPUs yeah you always end end up in a
total of eight CPUs beware if you create
four servers each eight CPUs technically
that's possible but then is you you kind
of overbooked the the virtual Host this
is like Luft hunza selling more tickets
than they have seats yeah somebody has
to wait in this case and unlike Lu hanza
Esco Ser does not give you 100 EUR
voucher if you take the next flight
so um if that happens then the the escco
S machines will run theer and
the indicator is as follows you will see
that the performance uh the person
processor time the CPU load is in a
normal range is in a range of let's say
15% all okay but then you will see that
this privilege time is increasing the
privileged time that's the time and
Windows system spends in kernel mode
this is time spent for uh for managing
internal operations like managing
devices like diss Network and so on and
this is also like the negotiation
between Windows and the virtual
layer so that means if this privileged
time is increasing more time is spent
for this handling internal stuff than
for the real
processing and this happens if you have
an over provision overbooked virtual
system this is like this that there's an
SQL Server coming to the windows and
says hey guy I I need to process
something give me a new CPU yeah and
then the the SQL server has to say or
the windows actually says sorry guys I
have to call my boss yeah is calling the
virtual host the virtual host says okay
hang on be patient I have to look up a
spare CPU for your processing yeah and
while Windows is hanging on the phone
and waiting this is increasing the
privilege time and the next level of
this problem is that there's more SQL
stuff coming yeah another one coming
from also have something to process this
is the processor Q length that is then
filling up this is the channel into the
CPU so the CPU just cannot process it it
cannot forward the requests to the
virtual host so the the the threads
actually are just stuck up in this queue
and by the end of the day it all gets so
slow yeah the the problem is often that
if you have these Whitt host and um yeah
someone who administrates this and
manages this they tell you oh everything
is okay the CPU load is at 15% there's a
lot of things uh to take it can take up
way more workload
yes from a virtual host perspective that
is the case but from an escos
perspective it all just skes up and the
system cannot process so beware of this
overbooking of virtual um
environments because sooner or later
this will will
hurt okay so that means CPU actually is
an easy thing to uh to size and to
configure
so this is just an example taken based
on this performance monitor data this is
an average CPU load of about 12% or
something like this so all in this room
temperature range well I say this is
okay
um 80% that is the old Microsoft
threshold but this is the average among
all the total CPUs I think that in this
box it was eight or or 10 CPUs and now
if you look into this on core level then
we see that every single core frequently
hits this red area and is fired up to
100% And this is exactly what we want to
have because when we look into our nav
Vision background noise what happens in
the vision yeah um this all this gooey
interaction opening a page here opening
a form here and stuff like this that
doesn't fire a lot of queries yeah if
you open a page that's yeah a little bit
of item record a little bit of flow
feature let it be a dozen of queries so
that's not really stressing SQL Server
so the background noise is really
moderate in nav but then we have these
Special Operations like creating
documents posting documents running
reports and stuff like this and even
nowadays we have always this loopy loopy
code yeah this a loop within a loop nav
Vision always has the same structure set
key set filter repeat until and repeat
until and this means when these kind of
heavy processes are start up then then a
lot of queries are fired to the SQL
server and this is what CPU is needed
for to handle these Peak loads yeah and
these are the Peaks we see and these
Peaks that should happen just a split
second just fire up to 100% and go down
this is what you want to see now imagine
um we leaving in the old Microsoft
thresholds if that curve is at
80% yeah then you don't want to see that
one that this machine is Stone dead
bones bleaching in the Desert
Sun
okay according to this It's always
important to see also the number of
users creating the workload yeah is it
one user one application server killing
the system or is it in this case 100
plus
users and the number of queries these
users are
firing and as you can see that can be a
lot so that means that is VCH request
per second it means about 5,000 queries
per second that are fire from an nav to
an escco server and this is something to
take yeah that's where we need our dear
CPU our memory um in SQL Server it is
all about memory this is the most
important component in Esco server
because es server is managing all the
data exclusively in Ram those of you
knowing still the old native Seaside
server Seaside server is just a data
pump from disk to client it's just a
pump station not s server s server is
only loading the data from the disk if
necessary and then it tries to keep all
the data in the memory as long as
possible SQL Server ships data only from
Ram so if it's not there in the memory
then it has to fetch it from the disk
and then data remains there in the ram
but Ram is not only needed for
maintaining the data Ram is also needed
for maintain locks to maintain
connections to save the execution plans
and all all this stuff so memory is
absolutely
crucial so the question now is how big
should my Ram
be and in this old Hardware sizing guide
they were telling you um it is based on
the on the database size yeah if you
have a small database with 1 gab so you
could have an SQL server with 3 GB of
RAM yeah great but bloody hell we all
start with a Chronos database of 500
megabyte so we all start with an S Ser
of 3 gigabyte and then yeah so that that
maybe takes or it's just fair enough for
a week for for a month and in a very
short time we will be in need of way
more memory yes so so the size of the
database has something to do with with
the ram but this could not be the
criteria because the our de the vision
is a well I'd like to say a data
Cemetery yeah everyone goes in no one
ever gets out this thing is doomed to
grow
forever so and we we cannot have a ram
linearly growing with a
database yeah so what I can tell or what
I should say is you never want to
install an SQL server with less than 8
gigabytes of memory even it's a single
place test installation or anything um
anything else you will terribly
regret but I have a different approach
so so why thinking about database size
number of users so um how should I
estimate that the data volume that is
created in the system yeah Microsoft is
not shipping these Crystal bolts we all
need and to see what really happens on
this uh
system so I have a different approach
because memory doesn't cost a thing
today Hardware is cheap so what is the
difference of having a server with 16 GB
or 64 GB
we're talking maybe about
1,500 what is that that's that's piece
of cake compared to the license cost for
for na Vision project yeah so we have
150,000 Euros license cost SQL Ser
Vision license um plus the development
and now we we arguing about €1,500 for
for memory why so I suggest just look
into the limitations of the SQL edition
of the windows Edition and and then put
in as much as possible as much as is
Affordable of course all needs to be in
a reasonable healthy State yeah it's
it's not recommended to put in two
terabytes just for fun or something like
this yeah but this is how I would think
it um because that way you can create a
robust and scalable system yeah you you
should erase the the term from your
vocabulary oversized there is no such a
thing that as oversizing the term is
scalable and for
forgiving yeah and sooner or later this
memory will be
needed okay to
monitor um the
system from a Windows perspective most
important is the available megabytes a
Windows Server never ever must drop
below 100 megabytes else it will switch
into panic mode it will page out
whatever is necessary the CPU will run
the Zer um so the server is completely
done so never ever this indicator must
drop below 100 a couple of 100 megabytes
is always feasible Let It Be 500 half a
gig because then it's forgiving then you
can open a an Vision client on this
server and do some work here whatever
you need to
do so this is most important for Windows
um independent if it's an SQL Server a
service tier whatever
machine we can monitor the page file
yeah as you know paging is is bad that
applies also to any computer and there's
a Windows performance counter that just
shows the past file usage so that means
that should be a flat line on the ground
not using page file
anymore in SQL
Server the most important indicator to
tell if the system is healthy or not
this is the buffer cach hit
ratio as mentioned before es server
always works like this a client sends a
query to the server then the server
first looks up if the data is already in
the cache in the cache
memory and only if it isn't there then
it has to pump it from the dis and then
goes to the client and this quality this
hit ratio this is the buffer cache hit
ratio shown here and this should always
be greater than 95% that means it has at
least 95% of all the data it needs for
working in the memory so means it
doesn't have to go to the diss that much
that often and so it could process the
data as fast as
possible if buffer cach hit ratio drops
below this threshold and that for a long
time um then the reason is simply you
have not enough RAM there is no plan be
it's just lacking
R there are also indicators that show
how long information remains in this
cache it should be greater than 5
minutes or greater than 300 seconds that
is just the duration how long an
information remains in the ram until
it's overwritten and stuff like this so
the greater this is the better it
is from our configuration p uh
perspective there's also not that much
to
do in SQL server in the instance
properties you have these memory
settings by default there's no minimum
and the maximum is at two terabyte or
something so what you always should do
is you should um kind of create a claim
a dedicated claim for the Esco server
and for the other world
so ideally SQL Server machine is always
a dedicated box so it's just the SQL
server on the Windows machine and no
more no other heavy services and stuff
like this ideally no service tiers no
web service no nothing in this case a
Windows operating system only needs
about two in worst case 4 gabt of memory
so as a rule of thumb the maximum server
memory is always the amount of physical
memory minus two in a case if you have a
machine with 16 GB of
memory it would be, 14400 if you have a
machine with a decent amount of memory
let's say 64 gigabyte then you can be
more generous and give s cursor maybe 60
gigs and leaving 4 gabt for the
windows yeah so that is necessary to to
have a dedicated claim if you have other
services of running service TI or
whatever then of course you have to
subtract the requirements for these um
Services as well and this could be
remarkable um this is um currently
discussed in the German uh user Forum
where Microsoft guy claimed that you
should consider about 8 to 12 gigabytes
for one service tier memory I I cannot
believe it I have so far I never have
seen a service tier consuming more than
4 gigabytes but this is a state from a
Microsoft guy and is currently discussed
yeah okay so ideally it's a dedicated
server without any other heavy
Services a minimum is not necessarily to
set yeah as a rule of thumb you can say
maybe quarter or half of the maximum
that's what you want to pre-allocate as
minimum that means when the server
starts up it instantly allocates such a
huge pool and doesn't have to allocate
the memory
dynamically what is dangerous is
something like this minimum equal
maximum because if that figure is too
high and the Esco server service starts
too quick kind of um pulls out the
memory chair under other windows
services and windows may may have
problems in firing up other services and
having a a global operating system
problem so the minimum should not be
more than quarter or half of the maximum
this case maybe 16% or something
yeah and that's all what we need to
configure for the
memory um in the S server instance what
I also would highly recommend when you
do some changes
here um I never uh push the okay button
here these are all things that can be
done on the flight don't they don't
require a restart or
anything and should take a split second
but if not if for any weird reason the
system hangs there's no way back
management stud this does just will hang
even for an hour or longer and we have
no idea what's what's going on so what I
always do you always find a managements
to these script buttons here so when you
do some
changes I go for a
script and here I'm cancelling
this and here I have
a SQL query oops
almost which is doing these changes that
way you have a documentation about the
system changes you are doing um you
learn a little bit of SQL and um if you
execute this and anything weird
happens there's always the way back
always the the cancel button so this is
what I highly recommend to do so yeah
normally it's a split second but if not
yeah just in
case
okay there might be an exotic problem
with the memory um if the server is too
small U regarding memory what we can see
is that other services um Force Windows
to page out memory so SQL server memory
is paged out um to provide this Ram to
other services if that happens you get
an error entry in the error log telling
you something like a significant part of
memory has been paged out and stuff like
this and always this paging takes time
and and when this happens in SQL Server
it kind of freezes yeah for a couple of
seconds there's no way back and forth
this is a very very rare problem I think
I have seen it only twice in the past
years um but just to avoid
it in the local group policies of
windows again my apologies for this
being
German there is a
right in English it's called lock pages
in
memory and
the account that is used to run the SQL
Server service should be assigned to
this right because then SQL Server
service has a kind of tight grip on its
memory pages and it could not be forced
to page out the stuff that
easily depending on the SQL Server
Edition you may need to
enable Trace flag um
845 the the Enterprise Edition instantly
have a lock Pages support the standard
editions they need this Trace flag to
engage really this lock Pages support
this is a nice to have yeah so again
this um actually is just disguising the
real problem the real problem is lacking
Ram um but then again it happens very
seldom yeah so when we look into the ram
this is also taken from a customer
system this is a perfect buffer cach hit
ratio yeah I want to present to you
there's no fake scenario there's really
two hours monitoring of peak load in the
system um constantly
100% they are not oversized they are
scalable now in reality in most system
this looks like this so the buffer cach
hit ratio in average is in a range of 80
97% 98% and yes of course we have
sometimes these these deep drops yeah
that is the expensive queries that is qu
that use up a lot of reads where indexes
are missing and stuff like this this is
when there's a kind of hit to the memory
and an es has to fetch some more
data but this should be an exception and
and not the
rule this is how page life expectancy
could look like yeah again this should
be greater than 300 seconds and here
also we can see this expensive queries
yeah so the the duration how long these
information remains is at at uh 5,000
seconds a long time one and a half hour
and then there's a bad query flushing
some memory okay so be it and then at
the end there's another expensive query
flushing a lot of memory but then we see
it's recovering yeah the life expectancy
is increasing this is normal behavior
this is what we want to
have
okay so far
that has been
easy now comes the
[Music]
challenge maybe I should stretch myself
a little bit okay disk the disk
subsystem is the most important part of
an Esco server system and it is the most
expensive part of the
system
um back to the
roots we need to be aware of rates rate
level systems redundant arrays of dis so
just to bring it back into your mind so
we have um the rate zero which is a
striping which means that among these
spindles the workload is
distributed we have a raid one that is
the mirroring that means that
information is just kind of copied from
one dis to another one so that means a
raid striping makes the system fast
because the workload is split that is
the idea
why do we need to split the workload
because most common we have these hard
Diss and a hard dis is a mechanical
thingy yeah if whenever you have looked
into such a disc there is a spindle
turning and there's a re right head
moving up and down so that's real
mechanical work that that happens here
and this has to obey some physical
laws um so the speed of such a hard disk
this mechanical work is limited by
Nature
so to have a fast IO to have a fast
responding dis subsystem it is possible
to split the workload among several disc
to stripe because then the mechanical
work the movement of the parts is just
half of the number in this case Yeah the
more spindles we put in such a stripe
the more is the workload distributed the
less movement each spindle has to do and
this makes a physical IO a physical
interaction
fast Mir ing is required for fault
tolerance to have the data safe because
of course we have to make sure that if
one dis gets down for whatever reason
yeah it's physical thingy movement that
can break down just for whatever be
reason um else the data would have been
gone so we need a kind of redundancy and
this is what mirroring is about to copy
the data to a to another dis so if one
dis goes down the other one takes over
so the only the one thing makes it fast
the other one makes it safe if you want
to have it fast and safe we need a
combination that's rate 10 or rate 1
oh yeah this is the most common rate
levels we have in the SQL world and
later on we show you the the hardware or
the database components that have
different requirements in speed and F
tolerance maybe what always is around
like a ghost and you never can really
kill it this is bloody rate Five this is
most misunderstood raid level you can
find um the problem with a rate 10 is
that there's a lot of overhead of discs
yeah always the half number of dis is
just there to take over just in case
yeah so so they then do actually kind of
work they don't really store any data
they're just there but you have to pay
for it um rate Five is cheaper because
you don't have this redundancy there's
no data mirrored so rate five works that
the data is striped among multiple dis
and then there's one dis for a parity
sum so the parity is just a kind of
control some to check if everything is
okay yeah reading from a rate Five is as
fast as reading from a rate 10 but the
writing to a rate Five is hell because
the creation of this parity takes
forever so a a rate five level is an
absolute noo for any physical drives for
databases so never ever if you have a
physical array a physical rate array
never ever put a database component on a
rate Five yeah that might be fair enough
for backups or stuff like this but never
ever database or transaction or
something like
this yeah so again I have to highlight
physical um rate volumes because the
story is very different if you're using
San
technology yeah because I often have the
discussion yeah then the the customers
are buying a huge
sand and then the the sand guys say okay
we need to configure as the right five
and then my customer said no no no York
said never ever do a raate five and
stuff yeah but Zan is a different
thingy
so Zan technology this is also something
that is really coming up in the old days
we had this the structure that every
server had its own storage system they
had all these their own drives and
everything but this is a challenge
regarding Administration yeah you have
all these little islands and you have to
maintain all these little Islands
providing discs and stuff like this so
most companies nowadays try to
centralize their storage yeah there are
small data to store it's not just ESC
server they have exchange data they have
a file server maybe a SharePoint or
whatsoever yeah and instead of
maintaining all these small boxes
somewhere around many companies just try
to have it on one huge box and the deal
is storage area networks a storage area
network is a an array a rate array of
many many many
spinals and indeed these arrays have to
be configured as a rate five or six or
something with double
parity the reason is
simple a real xan imagine they have 40
discs and if that was configured in a
rate 10 that means half of the discs
half number of the discs have to be just
wasted for fault tolerance just for the
mirroring that would be insane yeah what
what kind of capacity you just waste for
nothing so Sans are not doing this in a
xan usually they use a double par system
so they have even two discs for the par
figures so redundancy for the parity and
there's so-called hot spare discs that's
just discs that take over in case any
other disc gets down goes
corrupt so this is a physical aggregate
or Target depending on the manufacturer
and out of this physical Target the
so-called lons The Logical volumes are
created a
loon aoon is just a logical volume and
these loons they are assigned to the
using systems like ESL server exchange
or
whatever uh the loons have the big
advantage that they can be managed on
the Fly and very flexible so you can
increase the size on the Fly nowadays
you don't even have to restart the
machines or something like this
um which is not possible with real
physical rate
volumes
so why does raate five work with a sand
I just said never ever use stupid bloody
rate Five because between the Loon so
the Loon is the the drive how it is
Chown to the S server for example
between the Loon and the diss there's
the controller
let it be a fiber channel controller ice
gazi controller or S header called
whatever you name it and this controller
also usually has a huge
cache and this is what is the very very
difference to any other physical rate
volumes a normal disk controller has a
cache measured in megabytes Let It Be
500 megabytes th000 2,000 megabytes
hooray this thingy here starts in a
range of 8 gab 16 G gabt in up so that
means virtually when you have a real Zam
solution the Esco server is talking to a
ram disk so it just puts data into the
into this Ram disk of the fiber channel
uh of the controller and the controller
instantly commits if if there's any IO
the controller commits as soon as it in
its
cach so the Sands have a response time
of about 2 milliseconds or something
yeah it's it's like Ram disk speed the
physical r right to the dis happens
asynchronously yeah and of course this
physical right sucks it takes a long
time because of the parity and stuff
like this but who cares SQL Server is
out of that game here so this is the
very very difference and this is the
huge Advantage when using sand
technology
um yeah when it's about this diss also
frequently Asked question is what kind
of dis should we use the most common
stuff is hot disc yeah this mechanical
components and again these mechanical
components have physical
limits nowaday technology is solid state
dis a solid state dis is based on a
flash memory technology that is like a
USB stick on
steroids um so there is no mechanical
part and this is why the response times
are way way way quicker than with any
hard disk so you can say at least 10
times quicker um than any any po
possible hard
dis so the big advantage of solid States
is that they can perform way more IO
operations per
second um on the other hand they are
very very expensive as a rule of thumb
you can say that the price per gigabyte
storage is 10 times more expensive on a
solid state than on a hot dis but the
price per iops is is 10 times cheaper on
a solid state so never ever use a solid
state just for the mere storage of of
data so for backups or whatever or is a
file server so real strength of solid
States is the io the pushing the data
around in and out this is the what what
solid states are made
for yeah I found this picture on the
internet also comparing um these two
thingies um has a lot of advantages so
solid States really really rock but they
are expensive yeah so it's a matter of
budget um with solid States also you
have to be aware that a solid state this
flashh memory technology um a solid
state can expire these flesh cells they
have a limited amount of right cycles
and let it be 100,000 in the old days I
think it's closing into a million
nowadays but at one point these flashh
cells are simply expired they are done
that's called the solid state blackout
SSD blackout so the cheap stuff you have
in your notebooks at one day you just
try to push uh to fire up your notebook
and it just doesn't fire it just won't
start Windows farewell there's no plan B
everything is gone yeah that's when you
buy cheap of course this never ever must
happen in a database server yeah the SSD
blackout is something we don't want to
have in any database server so there are
some tweaks you find in the internet in
the internet you find something like
this create a raate one yeah you have
with two solid states you have a solid
state there and there's another one both
start to work so the data is mirrored so
after a couple of months you remove the
mirror disc and replace it by a new one
so the mirror is a few months younger
than the old one so at one day the
oldest disc expire black out but there
are still the the mirror taken over
which is a few months younger so you
have a couple of months time to replace
the expired disc so you always have to
shift around that sucks big time yeah
okay okay it is a plan B but um who
wants to fill with a dis subsystem every
every few weeks no so nowaday solid
state discs they have Reserve cells and
they have mechanisms to alert to notify
if they start to use the the the
reserves but then we have to get used to
a very different price tech the last
time I was looking up on a um manufactur
page that was a 400 gbyte solid state
with all these high-end features and
everything um 400 GB SSD
6,800 yeah and you can buy a lot of hard
dis for it yeah so it's always
technology versus budget yeah and again
there are sun solutions that can mix the
the the cheap dis and the solid state a
thing that's called Auto tiering the
sand can decide okay this is data that's
heavily used I put it on the solid state
there is data I don't use that much I
put it on the hard disk and
automatically can manage it there all
pros and Contra again it really
depends the limit of a solid state is
the bus the bus how it is connected
that's s or S AA um and this bus has a
limit of a throughput capacity of 300
megabytes per per second roughly and the
next level of solid States is solid
states that are connected by the PCI
Express
bus um because the PCI bus has a
throughput of, to 1,500 megabytes per
second the most known manufacturer for
this is Fusion IO so most people talk
about Fusion IO cards that is solid
States just plugged into the PCI Express
bus but again um more iops per second
faster response times but such a price
te yeah
okay so the diss are most
important and if you want to monitor the
dis and the in the internet you find
zillions of indicators that give a clue
about dis performance but it all depends
for example there's you might find an
advice check the average Q length
average Q length should be less than two
uh two packets but if it's a rate 10 on
a physical drive you have to divide the
number by the number of spins you have
in the rate stripe but not if you have a
Zan yeah so what so that's so many
dependencies the easiest way to find out
if a dis is performing okay is just to
use a simple stopwatch and just to
measure how long does it take to write
to it and to read from it and with a
hard disk you would say today the story
ends with 15 milliseconds a 15
millisecond response time that's fair
enough for a hard disk um for a solid
state of course that would be forever
solid States react respond technically
less than 1 millisecond so 5
milliseconds it's absolute top limit
also some SQL indicators um that's the
accessing the dis subsystem from an SQL
Server perspective these are o Ledges
that's transporting data from disk to
Ram same figures yeah always less than
15 milliseconds or less than 5
milliseconds right log is writing to the
transaction log IO completion other
operations that all relates to the dis
so for the
configuration there's also something you
should set in this local group
policies there's a right that is called
perform volume maintenance tasks and
German
Vol perform volume maintenance Tas that
sounds terrible what is um it's also
known as instant file initialization
normally
if you create a file on a computer it
has to be initialized internally and
this could take a while depending on the
file size now with our databases we are
handling gigabytes of files and so it
could take quite a decent time a long
time to to initialize these
things only if you are administrator
because then you have inherited this
right
already or if you have get granted this
right if you have the right right to
perform volume maintenance task this
initialization happens instantly so that
means um if you create a database or you
have to expand a database file or if you
have to create a backup on something
like this that takes a couple of seconds
or maybe even minutes because normally
it has to be initialized if you have
this right it just takes a split second
so the initialization happens instantly
and this could dramatically increase
some of these file operations so that's
why the SQL service should have this
right yeah speeding up um backups and
file operations whatever um it's not a
must have but a very nice to
have SQL Server is accessing the data um
on an extent level extend are eight
pages of 8 kilobyte so one extent has
the size of
64k so that means it's a good idea to
format the dis on 64k blocks yeah
because that matches to the physical
access of the SQL Server having in mind
that zans might may have different
requirements yeah so always ask the
manufacturer
yeah generally you always should have
different drives for these database so
we need a separate drive for the OS we
need a separate volume for the database
database file is accessed permanently
random IO yeah so that has very special
requirements in iops per second so
there's a permanent in and out on theion
database the transaction log also needs
a separate drive because it is accessed
in a totally different pattern we have
no random access on the on the
transaction Lo transaction lock is
accessed purely sequentially and this is
a totally different story in in
accessing the file having different um
requirements for the spindles yeah and
the read right head how it's moving
around
the tempdb tempdb is used for sort
operations in na um normally if you
don't have any custom programming and so
on and again you know your n Vision so
it's used for sort operations that can
be two records that can be 20 million
records so it's unpredictable what kind
of pressure we have in a
temptd um so it is best practice to have
a separate volume for the ttb to
separate the physical
IO so this especially applies to the the
physical rate volumes especially if you
have these hard dis
rates
um from from a rate level perspective um
the database file is a good candidate
for a rate 10 maybe the transaction lock
and maybe in third priority the
temptv basically this is all different
if you have solid States because with
solid States we don't have this
mechanical work but still um let's say
common best practice is to follow the
the same rules like with a old classic
scenario just to split it up into
different components but having in mind
that you can break this rule it really
depends and can't give any any advice
how you really should do this so if that
then do that it really depends on the
local structure and number of dis and
what kind of dis you
have yeah also if you have Zan and a xan
it's all a logical volume by the end of
the day it all runs on the same
controller on the same dis it's just a
logical separation and here it also
makes sense to have multiple loon for
the different components because then
it's easier to troubleshoot if you see
um if you have all on the same loon
which is technically possible and you
see some pressure coming on this that's
uh the cues are filling up and the
response time increasing you never know
if that is caused from the database from
the tempdb or whatever and if you have
it on different loons it's easier to see
okay I have pressure on this loon that's
my database or I have pressure on this
other loon and that's the temptv so you
can better identify where maybe problems
are coming
from there are some special H later on
okay
really
okay um yeah so this is how it looks
like in performance monitor yeah we see
this Baseline in a range of less than 50
milliseconds and there's always some
Peaks yeah and again these Peaks are
pretty normal um nothing to worry about
yeah that's just exceptional expensive
queries that have to pump a lot of data
from the dis and we see this on the read
and on the right level it's the same
thing so never worry about these
exceptions what matters is the average
within a representative period so when
we monitor for two hours or something so
we have to look what is the average in
these two hours that is telling a story
yeah there will always be exceptions and
again this is
normal we have special requirements for
the temptv and database regarding the
configuration
so I've already done this so don't start
from the scratch normally you only have
one single ttb file and starting with 8
megabytes this is ridiculous so 8
megabyte ttb is never sufficient so what
will happen tempdb is recreated whenever
you start the server so usually it
starts with 8 megabyte and then
increasing increasing increasing so what
you will have is that there's a
permanent autog growth by default it's
10% increasing the temptv data for and
this this autog grow is something we we
need to avoid because when whenever you
add a chunk to to a file it fragments
and the more it fragments the the slower
it performs So to avoid this Auto growth
the idea is to set this single tempdb
file to a decent reasonable file size to
handle let's say the maximum Peak load
that could happen yeah it's just used
temporary it doesn't store any data it's
used and then data is gone
again this is a little hard to predict
yeah what is the maximum size we need to
handle here and again this size changes
every day with every posting tables
getting larger result sets getting
larger more pressure on the
temptv normally the truth is somewhere
in a range of 500 megabytes to maybe
2,000 megabytes per file so but still
when you have said this um Auto grow
should still be in place just in case
yeah um never disable autog grow because
else the database will simply run into a
hold and then it's
done um what could happen is now if you
have only one single tempdb file which
is the default if you have a huge
pressure in this file a lot of sort
operations going on then this file gets
unavailable for other user PR processes
so you have kind have temp TP contention
you have latencies on the temp TP yeah
someone has to wait but SQL Server could
balance this if it has multiple data
files and the best practice is to have
as many data files as you have
CPU but no more than 8 to 12 nowadays
you have to be careful we have systems
with 48 CPUs so never create 48 files no
yeah and these should be in the same
layout um same growth in and stuff like
this and then SQL Server could balance
the load between the files um avoiding
this this temptv contention and
latencies N Vision doesn't do any
transactions in the temptv so it does
not create or modify any data so we can
totally forget about the transaction
lock here that's only important if you
have other applications up running on
the server or your own custom
programming that are doing something on
temptv
for the nevision
database it also applies that we have to
avoid autog growth so the data file size
should be in a decent size um as a rule
of thumb you can say you need to have
about 10% of free space this free space
is used for index maintenance operations
defragmenting an index happens in that
free space if that free if there is not
enough free space this index
defragmentation will not expand the file
it just will not defragment the indexes
so the indexes remain
fragmented um so 10% would be okay and
ideally it is a human being that is
monitoring this growth in the in the
file size and so on so some
administrators should look at it and
manually decide how to expand the
database because maybe it's not just
expanding the file maybe you need to
expand the Loon maybe you have to to add
another disc or something like this um
maybe it's wise to compress the database
internally using SQL data compression or
whatever these are all decisions a human
being should take and not the
autopilot autopilot the auto growth
should just be in play uh in place to
make sure that the database never ever
runs into a hold so it should be able to
to expand if necessary of course and
then it should be a chunk that that
helps for for a couple of days or maybe
weeks yeah again this is a Chronos demon
demo database in reality I suggest to
have an a growth of about a gigabyte at
least a th to 5,000 megabytes that is a
decent chunk and so that auto growth
should not happen every five minutes
again and again that that's also
pointless yeah for the transaction lock
it depends on the backup frequency
whenever you run a transaction lock
backup in information is truncated from
the file and what we want to achieve is
a kind of cycling through the
transaction lock file so whenever it
hits the end it starts from the
beginning um so it depends on how often
you you back up the transaction lock I
recommend to do that at least every
hour
um a yeah rough rule of thumb is the
transaction loog should be about or not
bigger than about 20% of the net
database size
yeah then again if you have more
frequent lock backups you can even
decrease this size and again autog
growth just in
case okay last but not least our dear
Network um network is easy again because
um hardly ever the SQL Server machine is
causing a network issue or having a
network issue usually the SQL Server
machine is suffering from a network
issue network problems are usually
Global things that you have in the whole
company yeah if if the network sucks you
feel it on on all kinds of places it's
not the squl Ser the vision getting slow
it's the internet getting slow it's
accessing the file server slow
everything sucks yeah usually it's you
have a broken switch somewhere in the
net or what whatever it's overp
so hardly ever es is the cause of a
problem here it's it's just the
symptom um to monitor from Windows
performance uh perspective um there's a
counter of the current bandwidth I just
put it here because I always or
frequently come across this people
install a gigabit network card gigabit
is standard nowadays but it is worth to
count the number of zeros in this
current bandwidth because sometimes you
will just find out they have a gigabit
card but it's configured down to 100
megabit or something yeah so they
throttling because of a stupid
configuration or they have a switch in
between throttling the network IO that's
an easy one to
resolve um to see if the network is okay
that's the the output Q length the error
packet Q um this should be empty yeah
that if that is always zero um that
means there's no no network iqed and the
the server could communicate as it's
supposed to
do from an Esco server perspective what
uh you will see in the top ranks um if
you have a classic novision scenario
that is the ODB that is the classic
novision clients communicating with the
SQL server and of course that is the
thing that that happens most yeah the
the permanent in and out um and this
should be less than 1 millisecond yeah
one millisecond this is a nor normal
Network latency what you have in the
local area network yeah if you do just a
a standard ping from one machine to
another it will tell you less than one
millisecond and this is also what you
want to see
here um with a service tiers in a rooll
tail
scenario um what we will see but we
don't want to see is the asnc network IO
ASN Network IO means that SQL Server
ships data to a to a client
respective our naion service here and
just wait for for this counterpart to
commit just to say yes I got it yes I
understood and process this normally
this also takes less than one
millisecond yeah very fast but our dear
service here seems to have a problem
with um certain queries yeah also David
mentioned this in his session before
this one the service tier has a problem
in digesting large result sets so if we
have queries that that retrieve or
return tens of thousands of Records then
we will see that the service tier goes
down regardless of the cach setting and
if it's a dedicated machine or
everything there is just a problem yeah
this especially if you have these kind
of smart queries this autocal flow field
thingies when you open a page when you
have these huge queries when when all
the flow fields are joined in and stuff
like this these are queries that really
bring bring down the service tier and
this is shown by this Asin Network IO so
if that is in the top ranks and you see
it's way way longer than one millisecond
that means that ESO has shipped
something to the service tier and just
wait for the service tier just to say
yes I got it and it takes just forever
for the service tier to digest this
number of Records so if that is the case
so if you see that this asnc network IO
is in top ranks and Tak in half a second
or even longer
um what you need to do is query tuning
yeah and what also David presented at
the end of his
session um and the easiest way to do is
to use a script also it's a similar
thingy like you have seen
before um there are scripts and again
you can download this from my blog
looking into the ESL server procedure
cache this is the thingy where we can
see all the expensive queries all
queries that have been executed we can
see how often how long it took um how
many reads they had so that's the memory
consumption the CPU
pressure and there's a column average
rows yeah and if you see that Network as
Network top ranks taking forever then
you need to check if you have queries
that maybe pump tens of thousands of
records and stuff like this or if you
have queries that are missing indexes
yeah and provoking any stupid index
scans and like this so then we really
back to plain hardcore query tuning in
the worst case that could mean that you
as developers need to split up the
results that you need to apply some
programming not pumping hundreds of
thousands of Records but do it in
packages of 10,000 or something which of
course is very annoying if you have to
do this in the programming yeah but then
then we are back to query
tuning um unfortunately this seems to be
a a specific
problem which we have um on VMware
systems with NB
2013 there I see this very often um so
also seems to be a problem with VMware
but yeah our service here
is at least involved if not not
guilty um some of these virtual
environments have special requirements
regarding the network adapter
configuration yeah these settings like
um TCP offloading and stuff like this um
also there are for VM I know for sure
there is configuration guidelines
telling you how exactly these adapters
need to be set up else also you will run
into this asnc network IO
problem yeah
so that has been the last component I
would like to talk about yeah um maybe
you were wondering where all these fancy
diagrams were coming from um they are
not created by Windows performance
Monitor and the last thing I would do
today is I want to introduce a very nice
tool to you also you find it on
codeplex that is called performance
analysis
vog and it works like
this oops I closed it accidentally
so so you remember in the very beginning
I have set up this performance
monitoring yeah that was a selection of
counters throughout the system and
everything okay so we could schedule we
could start it and then we could monitor
what's going on in the
system and I usually save it into a
trace uh in the two of these blg
files and for the investigation I'm
using this
P it is a thirdparty tool you find on
COD ples but if you see who is the third
party that should ring a bell yeah so
like David's application profile it's
Microsoft guys um doing something in
their spare
time um and this PL you can use um when
you have these blg files um then you can
pick up this this counter loock from
wherever you want to do that
and then there are these threshold files
and there's a lot of predefined
threshold files for all kinds of
Microsoft products and system components
and there's a threshold file for SQL
server and these threshold files that
are XML structures that have inbuilt
thresholds all these these best practice
values I was telling you they are built
in into these threshold files and now P
just uh goes
um picks up these threshold files and
the trace file then there's a little
questionnaire and so on and then it's
just next next next next next then some
Powershell magic is running up and then
this monitoring this plg file is
analyzed based on these
thresholds and the result of this
is a very cool HTML report
whenever it's
opening
um which tells
you what you have measured so all the
the counters are split up uh so they are
explained you can see the thresholds
that are used for the interpretation you
get these nice
graphs um and you get also here the
plane figures so the average values you
see the Max and minimum the extreme
values and everything and with this it's
very very easy you just create this
monitoring just feed it to the P pal
creates a report and then it really
highlights if there's a problem um never
worry about all these yellow and green
and red stuff yeah this always refers to
threshold violations but these are
exceptions what is the important part is
the average the aage is white everything
is okay yeah if if you have an uh yellow
or red something in the aages then you
have a problem yeah and this report um
also contains a lot of information about
the counters also links into external
sources there's a section how to speak
sanish yeah so that you can learn how to
configure zans and stuff like this it's
very cool tool I use it a lot um because
if there's a problem it really um spits
in your face
and it's also a good way to have a
documentation yeah if you frequently
monitor a system you can see how it is
behaving uh like David said what we need
to do is to to to see problems coming up
before the users are experiencing the
problems and this is a good way to do
that a little small print here
is um if you have installed the server
in your local language and not English
um P only only speaks English in that
case you need another tool a tool for
the tool which is called the puon lock
translator that is can translate the blg
file from local language into English
and then you can feed it to the
pl
okay so that was actually everything I'd
like to tell about Hardware components
and then again um basically these these
brief rules and there easy to to
memorize and they are or they will give
a a solid fundament for for such a
server platform then again it always
depends on really your individual
circumstances so how the server machine
is integrated into your it environment
is it a standalone system or is it using
a Zan you already have then you have to
ask who else is using the sand if it's a
virtual environment VM hyper or
something like this yeah who else is
using using this how is the provisioning
is it already over provisioned U all
these kind of questions you need to ask
always looking into your local
installation um the worst showstopper we
have with this Hardware sizing is always
the budget yeah so um this as you have
seen it's always a matter of technology
versus budget but by the end of the day
this is problems we can resolve just
with money yeah there's not lot of
thinking required or any filling in the
code or whatever ever it's just Tak an
amount of money and the problem is
gone um yeah that's the challenges to to
face yeah do you have
questions hang on oh sorry hang
on I just wanted to ask regarding the T
DB configuration because if you have a
server with 16 CPUs and actually
creating 16 T DBS
seen that contention in its own
right you have seen more contention than
before after you have too many temp DBS
based on the number of CPUs in your
server
really I haven't seen that um did you
enable the trace flag
1118 I did but I went then back to
Microsoft and they actually said that
you should try and Har it so start off
with l 10bs
for an example yeah so what I mentioned
also I'd rather create no more than
eight in the worst case 12 files so um I
haven't seen that problem but that's
happening it's weird it shouldn't happen
but who knows
hi um you mentioned SQL compression is
that something worth enabling yeah
definitely um data compression SQL
Server that's one of the coolest
features they have invented um with SQL
Server 2008 and if you are asking I show
you a script um
so data
compression and data compression so for
those never heard about this this is a
way to on a physical level to compress
data and indexes um has having a
compression rate of about 80% so means
if you have a table of 10 gabyt data
compression folds it down to 2 gigabytes
this has a tremendous benefit for the
dis subsystem because you you have to
store way less of of data and also the
the growth rate is
decreased um this is
a um very very good option for all kind
of super siiz databases where um in a
range of 300 gabt and up because the
larger the database and you need yeah
more discs or maybe solid states to to
handle the database and sooner or later
you can put a price tag on every single
table you have to store just if you just
calculate the Mere Money you have to
spend for for storing tables and stuff
like this and so data compression can
really help here um and indeed our D
naav has a lot of candidates um that are
subject for this
compression um if you want to do this um
you need to have Enterprise so
everything that is cool is always
expensive it's all
Enterprise um there is a script um on
the Microsoft block which is wrong this
is the corrected version um the best
practice is if you go for compression
you should only compress data that after
the insertion is not modified that much
yeah so you insert the data compress and
then it's done if you update this data
again it's always uncompress change
compress again up and down and up and
down and then then it fires
back so you need to know the read write
ratio of this and this script provided
by Microsoft um reads out the the read
write
ratio and the best practice is um read
ratio greater than 80% write
ratio less than
20% and this script here
then will pick these
candidates where you can see this ratio
and then it's also preparing the
compression
scripts and if you do this with nav um
the candidates are tables large tables
let it be more than 1 million records or
something like this all what I call a
data grave that's all kind of Ledger
entries um that's posted documents and
and related dimensions in the old days
and stuff like this that's super
candidates but you need to know this
read write
ratio um yeah so the the downside is or
the technical downside is and when data
is quarried it is getting uncompressed
via the CPU so if you compress the the
dirty dozen of candidates we have in nav
you will see that the CPU load increases
about 5 maybe 10% yeah but then again if
you're in this room temperature range 15
to 25% then this box can take it yeah so
that's really something to go
for hope this answers your
question
Pon this one I who was
it how often you should run this script
um first of all um this is reading out
the data from the
cache um so it is
re only representative the longer it
runs so um when you ever restart the
service all these Dynamic management
views which is basis of this are flushed
all the information is gone so you need
to have the server up running for a long
time that's why I also put the the up
time
here yeah to see if this data is
reliable but once you have picked your
candidates and once you have applied the
compression it remains there if the
table has a clustered index then you
only need to tell you once to compress
and all data that is added is
automatically compressed if you have
Heap tables so that's taable without
clustered index then you need to rerun
the compression but nav Vision makes
sure that all the tables have clustered
indexes and so compression
works so I have two
questions I have two
questions I have a souvenir for you on
top
here first in the sense system have you
sorry I don't hear it in the S system
have you everit
the in the sun system if you ever need
to watch the buffer
memory in what system the Sun Sun
System the buffer Cas hit
Rao the Es are buffer Cas hit ratio no
the the
right the sand cach
the yeah um so yes because as as shown
that the most important part of the sand
is the cach um but I cannot tell how to
monitor this because I don't know as far
as I know there is no windows
performance monitor from this um you
need some some Zan magic to do this I
know for example from the netup guys um
they have command line tools and
everything they really can look into
every single uh spindle and see how it's
turning how much load is there how much
the the cach is is hit so far and so on
um so I cannot tell how to monitor this
I know that there are monitoring tools
but obviously this varies from from Zan
to Zan technology yes so this is my
problem because there are several s I
cannot I can only monitor from the
windows perspective no from the windows
perspective all I can do is with a
stopwatch and see how long it takes but
what it internally is doing I think
that's something we we cannot find out
okay the second question is do you
change the files in the temp by changing
the model or by adding some startup
script no I changed the script uh these
tempt files manually so yeah because
that's a onetime you do this when you
install the s
server um it's not a a periodic job or
something you have to do oh thank you
very much okay um is there any thinking
or any best practice to use in memory
technology together with nav or what
kind of memory in memory technology with
this s secq server 2014 that comes this
in memory feature which is quite cool
but not for maybe environment life but
maybe there are thinking in in memory
processing so the ah okay this is a very
cool thing um but the problem is is this
and there's a multiple ways to do this
kind first there's technological way of
of firing up um data into memory the
next level beyond the fusion IO cards is
for example phase change memory cards
that is Flash combined with nonvolatile
ram so it means when when power is on
all the data is fired up into memory so
that that's real memory discs that that
um store the data such a price tech yeah
no way um but the io is tremendous the
next level is
um ESL Ser
2014 optimized for memory these tables I
only have seen benchmarks but non nav
benchmarks and and the performance gain
is
dramatic today I only have two customers
which are running on C server 2014 and
they are in a development phase and yet
I don't dare to fiddle with this feature
because I don't want to spoil the N
Vision development I have no idea what
would be the impact but um we have an
agreement once they have a stable state
in in the progress of testing then we
will pick some candidates I can imagine
that tables that have a heavy IO like
item lger Eng or something like this um
that could benefit from this but the
risk is I don't know what what what is
the challenge for the ram yeah how much
memory is will be used for these tables
um and what what other impact will
happen yeah so this is all the
challenges that I think we only will
will be able to face when it's done it's
hard to predict yeah because it's
difficult to create these test scenarios
again these two customers are willing to
test and then we will find out
so unfortunately that's the only way to
get best practices to do it in the
practice did I give you a
shirt okay I have no shirt I have one
book you mentioned the fusion IO device
and prices are going down but I wouldn't
use it anyway for a database because of
it has no redundancy and it's not hot
pluggable but uh one idea was would it
make sense to use this for the temp
TB for the fusion iOS for the fusion IO
or NVM Express what's coming up yeah in
some way technically yes of course
because for the ttb who cares if it gets
corrupt because it's recreated whenever
you start the service but the question
is um you want to spend this amount of
money for the temp okay the prices are
soon it's not too much anymore and and
if you you mentioned the the licensing
for enterpr price and so it's all
peanuts yeah no definitely so that that
for sure is an option I also have seen
benchmarks where some Cowboy guys um
were just taking some uh freeware
thirdparty R disk tools yeah just R disk
tools creating a ram dis putting ttb on
it always redundancy first of course and
I would never put a database on a fusion
iio card because it's not redundant but
uh if the temp if it crashes and and the
temp TB I'm not sure you can do some
some kind of mirroring with the fusion
iio I don't know how they that would be
my second question if I may no I don't
know I don't know so technically because
it's just an a solid state it's just a
different bus so I guess it depends on
how many pcie slots you have sure so and
then how this could be configured so if
you can afford it and if you can plug it
in but only use it for the temp TB
because you wouldn't lose anything you
you must have a strategy to move the
temp TB the card crashes yeah no that
that really makes sense because um if
there's any corruption if this power
goes down or so you don't lose any
information yeah is Mark brahl here
because he I think just recently
installed a fusion io on a database so
he could tell um my
second okay then you can can sell it in
eBay
okay okay have one last question
so one last very last one and
then I I'm out of of souvenirs so and
only questions I can answer yeah sorry
um when you talking about the parallel
parallelism how do you know how many
threads you have in the CPU
F how many threats es
creates um
I cannot demonstrate okay but first of
all you see it in the execution plan if
something if parallelism
happens um I don't know if you ever
checked these these execution plans
um something like this here whenever it
fires up and if you have kind of yellow
circle with two black arrows then you
have this kind of paradism I think it is
also
you can um see in the profile how many
uh threats have been created or in in
the easiest case if if you find such a
query on the Fly and if you just run um
a simple SP
who then you could see how many threads
uh have been created for for a single
process yeah so for example if you run
index maintenance or an Integrity check
and which takes a little longer then you
can see it or if you're run a backup
that one one spit yeah you will have one
Spit with multiple times and you see all
these these threats in the different
states okay yeah so over time so thank
you very very much for your
attention and now let's grab some food
okay
