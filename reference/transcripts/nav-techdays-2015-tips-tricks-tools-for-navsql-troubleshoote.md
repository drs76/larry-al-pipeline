# NAV TechDays 2015: Tips, Tricks & Tools for NAVSQL Troubleshooters

- **Source:** https://www.youtube.com/watch?v=gMQqUa77nP0
- **Video ID:** gMQqUa77nP0
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 100m50s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

Yeah. Um, welcome everybody to my little
session here. Um, hope you have enjoyed
um, NAV Tech Day so far. Yeah, the
greatest NAV conference in the world.
Definitely. Um, my name is Jük. I'm
around in the vision world for quite
some time. So, probably our paths have
crossed online or offline uh, before. Um
in the meantime I'm a freelancer um
dealing with exclusively dealing with um
NAV and SQL performance issues and
everything else that is in touch with
this um supporting partners and uh
customers wherever it takes whatever it
takes. So um performance is on our scope
for for today's session and when we have
to investigate performance problems and
then if you have to troubleshoot we
always have three areas we need to
investigate
um it starts with the platform the
hardware all that's all about
infrastructure that's about server
sizing server configuration and
everything this is the basis of of the
whole uh system
actually um the Second huge area is what
I call query strategy. This is all the
the communication that happens between
NAB and SQL server. This is how data is
stored, how data is retrieved and
everything in touch with this. And the
third area this is about blocking
badlocking. So this is conflicts between
processes. This is part technical stuff.
This is part logical stuff like workflow
and business process design.
And those of you who were attending the
previous tech days events maybe have
seen or even attended these sessions for
each area I was presenting a a very
detailed session digging into all the
backgrounds what happens behind the
scenes where problems are coming from um
and how to approach this how to resolve
these problems. So please have in mind
that all these sessions have been
recorded like this one. Um and these
sessions are available for download on
the Mibuza site. Um it's the the slides
and the text in the speech. So if you
like you can follow up on this and get
even more details. For today's session I
won't I don't want to be that detailed.
I cannot just due to the time. So the
the the idea of this session is to wrap
up uh the most important things again
maybe highlight some some important
things and also um maybe add some more
information that was these days um not
that that actual um what I also want to
do is I want to give you lots of tools
um if you're in terms or in progress of
troubleshooting an NAB system yeah you
need to have some stuff to investigate
the problems to analyze the problem so
so that you can come up with
resolutions. And with this, I want to um
yeah give you some tools, show you some
tools that are fairly easy to use, zero
costs. Um even though I will present
maybe some third party tools, that's all
um free of charge thingies. Um sometimes
you have to register for the download
and I think and everything um that I
present um the scripts at least I will
provide um on the musa site for download
and also on my blog space. Uh, of course
the only thing I cannot provide that's
the the third party tools. Yeah, not
allowed to do
that. So this is what um I have in mind
for today's
session. Um basically if you have to
proceed troubleshooting you always have
to start from the rear end or let's say
from from the basis and the basis is the
platform. Yeah the platform that's
server sizing server configuration. This
is what to be uh needs to be
investigated at first and has to be
fixed at first because on top of the
platform there's the SQL server
supporting the database and on top of
this there's the uh the CL the
application that is the thingy um using
all of
this and then again what is missing on
this slide um but I have to mention this
again on top of this pyramid there's
someone sitting and this is our dear end
user and if I was rude, I would say this
end user crapping down on all this. But
I'm not rude and this is public, so of
course I don't say that. No, but beware
of the human factor. Yeah. So, so human
beings make mistakes that they they can
do very stupid things that have severe
impact on performance, but but the only
thing we can do about it is sufficient
training. Um, but then we are actually
screwed. Also when we look into the time
it takes to apply fixes it's actually
the other way around. So um for example
if you find out um that we have hardware
problem a RAM problem. So the machine
just needs RAM in this case it's totally
pointless to start changing code units
or anything. So at first we need to
create to to add more RAM and the time
it takes to add more RAM that's that's
that could be a few seconds in the best
case. Yeah. If you're a virtual
environment, if you have a virtual
environment, you just move a slide bar
from 16 gigabyte to 32 GB. You don't
even have to restart the service and the
problem is resolved. So the lower we can
be in this pyramid um the more quick
fixes we can apply and the quicker we
can
troubleshoot. Most of the problems and
most of the resolutions are actually in
the center area. That's all here. um
what happens between application and SQL
server all this communication this is
where 80% of all the problems are coming
from also meaning that 80% of the
resolutions are in this this
area so starting with a first area
platform
um maybe a little disclaimer to these
slides when I was creating this slides I
um was um yeah arguing with myself if I
only should present the slides that that
are really talking about um but I
decided against this. So these slides
contain all the information of all the
prior sessions. So it's terrible I know.
So there's a lot of stuff that that I do
not discuss but the idea is um to to
give you the the full inchilada. So so
if you like you can follow up on this
and you have all the details all the
formulas and whatever is important all
the details that have been discussed in
the previous sessions.
Okay, back to the platform. So platform
here the most essential thing to
understand
is it does not exist. There is no
perfect platform. You never ever can
tell if that then do that. The problem
is well it's not necessarily a problem
but the issue is our DNF ecosystem. This
is not a standalone island completely
isolated from the rest of the world. So
an FSL system is interacting with other
systems on a physical level by shared
hardware or whatever shared system
resources or maybe even logically. So
with interfaces, yeah, data exchange and
stuff like this. So it's just another
brick in the wall and and there are so
many dependencies that it's impossible
to to give some guideline. If that is
the case, then do that because there are
so many questions to be be asked and
answered. Yeah. like how many users um
expected database so it's expected
growth are we physical are we virtual if
we are virtual is it hyperv is it VMware
indeed that makes a difference yeah if
it's physical do we have a a zan who
else is using this stand are we running
247 what are our demands on high
availability and and and and so a
zillion of questions and the answer and
the combination of answer would be
always different so so it is impossible
to just open a drawer and for this
customer do
Um it is always an very individual
discussion which has to be um yeah
accomplished when creating a new SQL
server
system. Um before or according to
discussing hardware requirements you
need to be aware of the software
limitations. So um have in mind that
Windows and SQL Server have restrictions
regarding usage of CPU and RAM. And as
you see on the slide, Microsoft is
playing with these limits up and down.
So in terms of sizing the the SQL server
properly or the service tier in respect
of CPU and RAM, you have to make sure
that um the software does not spoil this
thing. Yeah. So software and hardware
have to match must
match. So even though there is some
guidance and and you will get these best
practices in the slides later. Um, of
course there's some little best practice
and rule of thumbs how to size CPU, how
to size RAM, disk and everything, but at
one point um you you have to verify
this. Um, and especially if you're in
the beginning of creating a new server,
it's it's a lot of guessing and not
knowing. So you you have to um somehow
find out um if everything is okay or if
you need to change
something. And here I'd like to um
introduce some tools to you. I hope or
maybe well you know about them. Um which
are most important to investigate the
platform very simple. Um by the end of
the day all this platform thing is very
technical very hardware like and most of
you are probably the vision developers
vision consultants. So I keep this a
little down to to the
basics. So this what I want to show is
what what everyone could do.
So the very first thing I I want to show
you is um a little script. This one is
this version is taken from Paul Randle.
Great guy. Read his blog sqlskills.com.
Yeah. So that's must must read for for
SQL guys.
Um this is a script investigating
so-called SQL server weight statistics.
SQL server is the receiving end of any
performance trouble. Yeah. So this is
where the performance trouble happens.
So of course SQL knows about these kind
of problems. So SQL server is waiting
always for anything. Yeah. Not nothing
works infinitely fast. Of course,
there's a lot of stuff that SQL Server
is doing behind the scenes and the
script is is hiding a lot of of these
nonsense counters or the unimportant
counters, but indeed with these weight
statistics, we can get a glimpse on
what's going on in the platform. There
are counters that apply here for to
network, to disk, and whatever.
So um what I added to the script is here
these little comments so so that you can
read what are the figures you actually
want to have here and later on on the
slides I will show you more um how to
interpret this data and um how to work
with this but this is a fairly simple
way you just fire the script and and for
those of you who are a little technical
and know what happens behind the scenes
um can have a in Germany there's this
saying you hear the grass growing yeah
and this gives the first indication for
platform issues also for application
issues. Yeah. Like locking and stuff
like
this. So this gives a very good first
impression but sooner or later we need
to have it more
detailed. And here the tool or the tool
that is Windows performance monitor
perfmon.x. This is an onboard feature of
any Windows
computer and this is just a tool to
record thousands of indicators that are
already in the system. So whatever you
install in a Windows computer there's um
all kinds of health and status
indicators that are already there and
perform is just a tool to to grab this
information to record it to display it.
This is a standard feature so I don't
explain how to fiddle with this because
that's actually well documented.
Um the big advantage nowaday is if you
have created such an assembly for
Windows performance monitoring manually
first time. Um everything is portable
nowadays. So so you can export this and
you can import this. And what I of
course will do is I share you my
template. So I have done the work for
you already. So all you need to do is
there's a thingy that's called
counterlock. I apologize for the German
environment. Yeah. But as we have seen
that most of us here are Germans.
Um so all you need to do is uh you say
you create a new data collector name
it pick the right template matching to
your SQL version is it's a standard
instance or named
instance specify the output where you
want to save the file to and that's it.
Yeah, matter in a matter of split second
and and this is actually a very cool
assembly and I we'll show you later on
where this is coming
from. Um looking up disk, CPU, um RAM,
SQL counters and a lot of stuff. This is
giving a very high resolution picture.
So we're recording with a one second
interval to really see all and
everything the full truth. And it is
important to record into a file. Yeah.
And this is all automatically set up. So
file because in this case you can record
on the customer system on the on the
real server on the problematic server
and do the investigation apart from this
in your back office or wherever you
need. Um the small print of this is this
setup is is a mighty one and um it could
create depending on the location uh
localizations and the escore server
version it could create about 200
megabytes per hour. So this is nothing
you should run a full day and for that
reason there is no schedule defined. So
this could be scheduled. Yeah. So that
you can say start that and then you can
give a stop condition and the stop
condition is already preset to two
hours. So this is what I recommend to
always do snapshots of a couple of hours
to see what's going on
here. And with this you will be able to
record in detail what's going on on the
machine.
The result of this is very technical.
Yeah, you need to have technical guys to
to to understand this data and and to
interpret it. But to create the
measurement, this is something that any
developer could do. Yeah, you have seen
it is importing this template. So that
you as developers and consultants, you
are maybe in the yeah in the front.
Yeah. Dealing with your customer. So and
if issues arise, so anyone should be
able to create this measurement and then
you can provide the data to the
specialists.
Yeah. So once this is recorded
um well to to in investigate this data
this could be done manually. I open this
file and then you get a lot of figures
and everything and all these best
practice values what you want to see are
documented
somewhere but it could be way way way
better.
There is a tool
around PL
um performance analysis of locks. This
is a tool you find on codeeplex. So it's
open source, freeware, everything. And
let's call it a third party tool, but
you see here from the email addresses,
the third party is Microsoft. These are
the guys from the platform team. Yeah,
it's a kind of side project which never
made it into the Windows product. So
that's something they handle apart. And
this PL is something that you can use
when once you have done your Windows
performance monitor
measurements. Um you pick up the counter
lock
here. Yeah, don't do that now. And then
here you have predefined threshold
files. That is XML stuff with builtin
thresholds of best practice values,
values you want to see. So you can
pick for example your SQL server version
and then this performance measurement
will be investigated and interpreted
according to these built-in
thresholds and even further you can
export these threshold templates for
performance monitor as templates for
perfmon. So now guess what? Where is the
template coming from that I was
installing right before it? I have taken
it from PAL I modified it did addit my
own magic and and this is now um
measurement that is 100% compatible with
the PAL thing. So means I can feed it to
the
PAL then you need to answer a little
questionnaire output. The rest is just
next next next and then it starts a a
PowerShell magic. Yeah, PAL is just a
huge PowerShell script and the result of
this is an HTML
report. So here you you get kind of a
table of content and now maybe switching
to physical
disk. Yeah. So every counter is
investigated and here in this report the
counter is explained telling you what it
is actually about. you see the
thresholds that that were used for the
interpretation. Then we see it in a in a
diagram. So to see do we have exception
or is it what is a trend what is an
exception or whatever and the data is
then also uh we have the statistical
data here to see the averages maximum
and whatever and this report gives a
very very detailed insight in what's
going on. Um, don't worry there's a lot
of red and and yellow and stuff and
warnings in PAL, but but these colors
always refer to the exceptions. Yeah.
What what really matters is the average.
That is the important thing. Yeah. And
in this way you you're easily capable to
to analyze platform um behavior and to
document it. Yeah. That might be
especially important for the partners.
So um if you you support your customer
over a period that you fre if you do
these frequent measurements you can see
what was this month the next month how
is it uh progressing how is the system
changing so that you can react to any
anything weird that maybe
happens. So I highly recommend to use
this spell thingy because that's really
a very very powerful tool and um I use
it a lot but then again that's for
really the hardware guys. Um
so what I do not discuss today is that's
the slides from from the last
presentation. Um this is all these best
practices about each hardware component
how to size how to configure. Um in top
on the top of all these slides you find
a table where these performance counters
are mentioned. Yeah this is the counters
that are in the Windows perfmon and here
you see the best practice values what
you want to see and here's all kinds of
rule of thumbs how about sizing. Yeah
one CPU per 20 25 users and so on again
um don't have the time for to repeat
these details but I left it on the
slides so if you like you can follow up
on this.
Yeah, RAM. RAM here. Maybe the the very
short version is plug in what is
possible. Yeah, there there's no point
in in saving your RAM. You never can
have too too much RAM in ESOS. It's all
about RAM. Of course, it needs all to be
in a in a reasonable healthy state.
Yeah. So, so if you are running
Enterprise Edition, I I do not recommend
to plug in four terabytes of RAM. Yeah.
Just because they are capable. No way.
Now um most divisions run in a range of
of 32 64 GB
easily.
Um another thing maybe you should really
um um print in your mind is or other way
around. No please you have to erase the
term oversized. It does there is no
oversizing. Oversizing does not exist.
Um it you never can have too many
resources. Yeah. So that doesn't mean
oversized. It means it is scalable.
robust and fault tolerant and this is
what we want to have. Yeah, there is no
thing such as
oversized and we were discussing disk.
Yeah, this is the uh the most the
trickiest part of any system because
that's the the slowest part and it's the
most expensive part and here that's a
big question if to use physical hardware
like um like raids. Yeah, raids with all
the striping and mirroring is a huge
waste of storage capacity. Uh raid five
we have briefly discussed which sucks
big time. Yeah, again this is maybe
something to repeat. Never ever use RAID
five with direct attached rate volumes
because the creation of the parity
figures takes too long time. Rate five
only uses if you have huge sand
solutions sand um which are powerful
they're having plenty of disk because
the trick is oops that they are
buffering the IO with a huge RAM and
VRAM cache. Yeah. So if you have zans
and and balloons assigned to the to the
SQL server for example and actually SQL
server is talking to a RAM disk and of
course this is fast as hell. So so the
limitations of array five are bypassed
in this
case. Yeah. Another way to bypass the
limitation of this hardisk. Yeah. The
problem with the hard disk is it's a
spindle turning and a read right rate
moving. So this has to obey to to
different physical laws. Yeah.
everything that happens on CPU and RAM
this is just pushing electrons but but
spindle turning and everything so here
we have something like guroscopic
effects yeah we have magnetism we have
inertia and stuff like this yeah so
totally different laws and this is the
reason why we have all these caching or
striping and whatever another way to
overcome this is using um not mechanical
disc solid state disc yeah that's that's
kind of USB stick on steroids um it's
the same technology bit little more
pricey and a little bit more powerful of
course.
Um the next level of if that isn't
sufficient well there's a thingy we
discussed also that was fusion IO while
fusion IO is actually just a brand name
but this means um a solid state normally
the limitation of a solid state is the
the bus the SAS bus which has a
throughput of 600 something megabytes
and these fusion IO cards are attached
or plugged in via the PCI express bus
and that one has a throughput of,500
um
megabytes. Yeah. So this is the the
trickiest part to discuss and and the
most expensive part. Yeah. Just to give
you some some price house figures uh
numbers um a 400 gigabyte solid state is
in a range of depending uh of 3,000 to
to 5,000.
It's a totally different range because
we need to have high-end solid state
discs that are really fall tolerant, not
the crappy stuff that you have in your
notebooks. Yeah, this cheap stuff. If
you if you don't know what I'm talking
about, um, please Google solid state
blackout. This is what will happen to
the cheap disk and this must not happen
to to database drives. No blackout.
Yeah, this is why this is expens
expensive. And for example, Fusion IO
cards. Um, one of my customers recently
bought some uh one card two terabyte
storage 40,000
euros. Yeah. But of course the IO um is
just playing rock and roll of
course. So all these best practices
around a disk, what to put where it's
all listed here.
Yeah, one thing um I'd like to focus on
a little bit because I think that was a
little short in the original
presentation some something about this
dynamic service tiers. There's always
the question how many service tiers do
you need? How many users can uh a
service tier take? Well, basically
nowadays a server a service tier is
highly scalable. Yeah, it's just it's
64-bit. It can use CPU. It can use RAM.
So basically um almost infinitely use
many user you can put on one one single
service but if you should do this is
another question. So um from the sizing
formulas um there is they are listed
here. So that's
that's no big thing.
Um but there is some I I would call a
fairy tale around in the internet and I
hope you never came across this so far
but for those of you there's some some
cowboy advice telling you okay you
should have 150 users on a service tier
and you only need two CPU for that. And
if you really believe this, then
uh you didn't hear the shot. And there
this is a terrible
misconception. Unfortunately, this is
not fully wrong, but it it um it does
not tell the full truth. With a service
tier, you have to have in mind we have
two lines of
communication. We have the line from the
service tier to the RO tailored client
to the to the front end. And here on the
service tier we have a setting that is
the maximum concurrent sessions uh no
the maximum connections sorry maximum
connection score the default value of
this is 150. So by default we can
connect 150 rot tailored clients or
clients at all to one service tier. If
you try to connect user number 151 then
you get a runtime error. You get an
error. So this is the first line. Yeah.
And 150 users for a service tier. That's
fair enough.
So now um we have un we have to be aware
of we have a second communication line
from the service tier to the SQL server
and this is defined by a setting that's
called maximum concurrent calls and here
the default value is
40. So that means yes you can connect
150 users to one service tier but
actually only 40 will work. Yeah, all
the remaining 110 users will be queued
in the connection pool of the service
tier. Yeah, this is like Lufanza selling
you 150 tickets, but you only have 40
seats. Someone will have to wait. But
unlike Lufanza, you don't get a 100 euro
voucher if you take the next slide.
Yeah. So, um so yeah, and then of course
a rule of thumb for CPU is um one core
per 20 25 users. Yes, of course. As long
as just 40 users are working, two CPU
are okay. But I guess that if you have
150 users connected to the service, you
want to have 150 user working. So you
need to increase this max concurrent
thingy here. This needs to be equal to
the real number of users connected and
according to this the number of CPU
needs to be
sized. So what I suggest or highly
recommend is to have at least two
service tiers just for fall tolerance.
So, so that you can balance. So, if
because
um for sure you experience this service
tiers tend to crash once in a while just
for no obvious reason. Yeah. And so if
one service goes down, you have another
one up running where you can root the
users. If you have just have one single
service tier and this goes down, the
whole company is
done. Why we talk about crashes?
Um well you have to be frank but it is
the case the older a service tier built
the crappier it is. So um if you have
very old versions you will have you will
experience terrible things. Yeah
unexpected crashes. You can see that the
mother of all memory leaks and stuff
like this. So the service tier builds
they start to get stable springtime this
year. So you should not use any build
any CU level older than February this
year. Yeah, these these things suck and
there's nothing you can do about but but
patching and going to the next the
recent cumulative
update. Yeah, another thing I'd like to
highlight here is this async network IO.
This is a counter from the weight
statistics
um because this is something you always
have to discuss with the real SQL DBAs
who have idea about SQL but no idea
about um
NAB. I think network IO means that a SQL
server has shipped some data to a
counterpart to a client NAB service tier
whatsoever and then SQL just waits um
for this uh client to to confirm the
reception of the data as server just
wants to know did you get it? So and if
this um async network IO weight
statistic is in the high ranks this
um could indicate two problems.
First problem is we have a network
network problem. So really that we have
broken network adapters switches wrong
or whatever. So really a network problem
and the second reason is so guess what
applies to our world and I I'm quoting
here from a from a SQL block. The second
reason is that the application is just
programmed in a shitty way. That's not
my my words. Yeah. So I I wouldn't say
that the vision is programmed in a
shitty way. No. Um the reason is this.
since NAB 2013 this async network I will
always be in the top ranks and an
original SQL DBA will run will panic
yeah they will start to tear the cables
and then disembowel the network and
whatever no this is should we call it a
feature this is the way how the service
tier is running um we have a a
communication way from service service
tier to SQL server which is called Mars
multiple active result sets
The idea is that the service tier is
caching some data. Yeah. So that the
data is once quered from SQL server and
then this same data could be read from
all other users on the same service
here. That is basically the idea of this
smart. So what now happens is in this
Mars thingy if you open a page a a page
is firing a select top 50 query to the
SQL server. So yes, Escao will retrieve
50 records as fast as possible and send
it to the service
tier. But now unluckily the page cannot
display 50 records. Yeah, just because
of the size of it. So probably the page
only displays 20 records. It means that
the remaining 30 records are cached on
the service tier. And while these
records are in the cache, SQL the
service tier does not confirm the
reception of the data. Yeah, SQL shipped
50 data and and asking the vision, hey,
did you get it? And the vision, wait,
wait, wait. I have to render it to my
client. No, no, wait, wait, wait. And
while this happens, as network is
counting up. Yeah. So, but in real in
reality, the data is there already.
Yeah. It's just a matter of how the
service tier responds to the SQL server.
So, as a network IO is not necessarily a
problem in our world. Yeah. But but you
have to know this because in the rest of
the non-NAV SQL world, this is a
problem. Yeah. else it would be too
easy. Yeah. Another word um a little bit
about virtualization because there's
also some some misconception around some
people obviously think that hypervisor
software is a magical software magically
creating CPU in RAM which is not the
case. Yeah, we we're not living in ivory
tower Copenhagen. No. Um so the story is
this a hypervisor is only used to manage
software. Yeah. This is the idea of a
virtualization. So you have a finite
amount of system resources speaking of
RAM and CPU and the hypervisor is
supposed to handle this to manage
this. So that means um what you should
not do you should not sell more
resources than you actually have. Means
for example a host if it if a host has
32 CPUs then you can create for example
two servers each using 16 CPU totaling
to 32 or you create four each 8 CPU
totaling to 32 or you create 1688
totaling to 32 CPU you get my drift.
Yeah. So whatever you do what whatever
servers you create but you never exceed
the actual number of physical resources.
If you do that the the the host is over
booked and then again it's like lufans
are selling more tickets than they have
seen. Somebody will have to wait and
performance will drastically be
decreased. So so for a high performance
system you have to make sure that the
hypervisor the host really fulfills at
100% the hardware requirement of the the
SQL server or maybe the service tier.
Yeah. So, so this could be handled
depending on the hypervisor software
with a static CPU assignment 100%
reservation and stuff like this. So,
never ever overbook um a virtual host.
Another uh trip wire that that you could
come across is if you run um um
virtualization in a cluster. So, you
have multiple hosts uh underneath one
hypervisor. So the idea is that you have
a virtual server and if you need to move
it you for whatever reason you can move
it easily from one host to the other on
the fly and everything. So so this is a
very cool feature for for fall tolerance
for high
availability. But the small print is if
you have such a cluster you must make
sure that all these hosts have identical
hardware specifications especially they
need to have identical CPU
specifications. So down to the clock
speed they need to have identical uh
type and clock speed and whatever
because if that is not the case then the
hypervisor could switch into a an
emulation mode and the hypervisor will
emulate the CPU for the server for the
virtual server matching to the lowest
specification in the cluster because
that is the lowest specification could
run on any host not the other way around
and this emulated mode sucks big time.
Yeah, totally done. What the the symptom
of this will be if you if you check it
in SQL server that you you will see a
delay between each query execution from
for around about half a second. Yeah.
And of course you can imagine
um one query break for 500 milliseconds
then the next query this is terrible.
Yeah. So, so you have to make sure that
if you run these kind of clusters that
they have the same powerful resources
else um you will encounter very weird
things. Okay. So, but that's it about um
platform hardware. So now I'd like to
discuss or highlight some things in this
query strategy context.
This is actually the most important part
for performance troubleshooting because
in this area most of the problems are
coming from and it also means that here
we have most of the
resolutions. When it's about query
strategy it's important to understand
how SQL server is storing data and how
it is um retrieving data. In SQL server
everything is about
indexes. Um imagine this you have a huge
warehouse. This is your table and in
this warehouse you have thousands of
drawers. This is your data pages and in
each drawers you have some pencils that
is your records. So now you are SQL
server and you you enter this huge
warehouse and now your challenge is uh
you get a query to process give me all
the pencils color equal red. What are
you
doing? Yeah. So what big warehouse
thousands of drawers. So what you can do
the only thing the only chance you have
is you open every single bloody drawer
and check and check if there's a red
pencil and of course this takes forever.
Yeah, taking long time causing system
resource and so on. So to process these
queries fast needs pointers indexes that
point to the result sets to the data.
Yeah. So what you need is when you enter
the warehouse, there should be some guy
around where you can go, hey guy, and
can you tell me where are the red
pencils? Yeah. And then this index guy
tell you, okay, this is in this drawer
and this drawer and that drawer. And
then you can quickly seek out these
records and then fetch it and yeah do
your do your query so to speak. And in
all about these indexes
um so once upon a time we were
explaining how this is built up. We have
different types of
indexes. Again, I don't repeat this.
Yeah. And here we have two ways of hand
using these um these table indexes. We
have one fast way to retrieve data. This
is the seek. Yeah. This is when when you
directly pointing to the data and the
slower way actually will happen if if
something weird happens is to
sequentially read an index. This is like
opening any bloody drawer.
So this actually implies two challenges
for us as developers. The first
challenge is we we have to make sure
that SQL server has the right
indexes. This is the first challenge and
and the second challenge is we need to
make sure that SQL server is able to use
these indexes in a proper way. And this
is how we program which methods we use.
Yeah. Find set, find first and whatever.
So the first challenge is a little bit
supported by the vision itself because
whatever we create as a key corresponds
automatically as an index on a SQL site.
So so we have a decent set of indexes
for a start but due to the way how our
keys are designed they are actually
quite inefficient for SQL server. So um
the reason is um nision is doing a very
very basic indexing. SQL Server has way
more features to to create smart indexes
um using features like included columns,
filtered indexes, whatever. And and the
vision is only using a fraction of of
these
capabilities. So by the end of the day
um we we end up in a situation that many
of these indexes that are already
created by a vision are not used. SQS
cannot use them because they have some
nonsense information. Yeah, it's like
secret entering the warehouse. Hey guy,
can you tell me where is the red
pencils? And this guy says, "No, I have
no idea about the color, but I can tell
you which wood they are made from." And
SQL says, "Yeah, thank you very much.
Here's the middle finger." So I start to
open the drawers again. Yeah. So, so
this is what we have. So that means a
lot of indexes are missing.
Um so in the second challenge of how the
indexes can be used or not this is
actually um which methods we use for the
programming and here the the huge
challenge we have is that we have two
different worlds. We have the old world
that is everything until the vision 2009
uh release 2 and the new world um with
starting with NAB 2013.
The problem is in the old world we have
a a big issue that's called dynamic
cursors. Some of these commands can
create these dynamic cursors and by the
end of the day a dynamic cursor um
prevents SQL server to pick the right
index for for whatever reason I keep
secret
today. Yeah, these dynamic cursors suck
big time and they are often responsible
um for for huge performance problems.
This this um has been understood by
Microsoft. Yeah, all this cursor stuff
has been removed from 2013 on. So that
means yes, there is still a difference
between the commands. Um, and if you
talk about the commands, I think find
first, find last and is empty. That's
pretty clear. Yeah, that find first if
you want to process only the first
record, find last if you only want to
process the last record, is empty if you
only want to check if there's something.
So this is pretty obvious. No, the
challenge always is to use find minus
find set. Yeah, which one is the better
one? Um, and again to keep a long story
short, I recommend to use the fine set
as long as possible. So, and and so far
that works good for
me. Again, the details have been
discussed on other
places. Yeah. So, these are the two
challenges we have to
face. But, uh it is actually pretty
pointless. So, so um to open the code
units and now try to to um change any
kind of code any find commands and so on
um just just without even knowing if
there's a problem coming from. So at
first we need to see the problem and
then we can react on
this and this is what I'd like to show
you how you can find out how can you
learn about these kind of query strategy
related problems.
So the best tool of choice is another
onboard feature that's the SQL
profiler. SQL profiler is a kind of
server monitor where which is able to
record everything that happens on the
SQL server.
And then again there's hundreds of
events that could be monitored and it's
well documented because it's a standard
thingy. And as it is with all the other
things once you have created your
assembly it you can create templates.
It's portable and of course I share my
templates with you if you like. So here
I have all kinds of templates here. take
this one which is just a pre-selection
of events that are feasible for
troubling shooting
purposes. So um what we can do with this
we can save the output to a file um
which is highly recommended. Yeah, you
can also trace in a table but I'd rather
not do that because um if it's a file
it's portable. If you save the output
into a table this is additional workload
to the SQL server. So, so you might end
up in a situation where you are
profiling the problem that your
profiling creates. Yeah. So that this is
not the the
point. Yeah. And with this actually we
are able to now see what's going on in
the system. So what I have to do now is
something that you in in real life
please never ever do. Um just firing up
profiler.
Profiler always needs to be filtered to
to reduce the number of of events it is
recording. If you use profiler in an
unfiltered way, it will kill the disk.
Profiler has some decent costs and if
you just run it in the GUI, it will save
all output in a temporary file, usually
on a C drive. And if you don't watch it
and uh vision could fire 5,000 queries
per second. So this file is immensely
growing. Yeah. So suddenly you kill the
disk and then have another problem.
Just for demo, I'm doing this
here. And then basically we could do
some vision processes. Yeah. Just to
record what's going on. And here what is
important uh to have in
mind what we have in the debugger today
is a SQL trace feature. So normally um
the vision just sends the statements. is
firing the statement the queries to the
SQL server and we have no clue about the
nision context but with this enabling
the SQL trace feature the service tier
will also send the so-called um call
stack to the to the SQL server and this
is what I'd like to do just to to
demonstrate yeah now I have a little
code unit here that is just creating
sales and posting this
Just stop it
here. So here we see all the queries
fired to the SQL server. We can see um
the pressure they cause. Yeah. Um the
number of reads is the number of data
pages. If you multiply this figure with
8 kilobyte, you know how much memory is
consumed. We see the CPU time the
duration in milliseconds. So we see
which queries are
expensive. Yeah. Which queries causing
bad
performance. Um the call stack is here
sent as a separate batch. And this is
actually a cool thing because the
problem is with all these statements
um we don't have any user delegation
anymore. So we cannot identify a single
user on a SQL from SQL perspective. All
users use the same login of the service
tier. So so this is a problem um to see
who has executed this query when
enabling the call stack with a SQL trace
feature. Here we can see the
user. Yeah. The human being behind this
locking. Yeah. And we see which is the
code unit this code is coming from. Uh
which line of code which function and so
on. So basically the idea here is pretty
cool. So to combine the SQL world with
an NAV
world. So and if we have this kind of of
traces Yeah. Um
So I was recording now for just a couple
of seconds and you see um here I have um
78,000
um lines recorded and this is just a
single session creating orders and
posing them. Yeah, imagine what happens
with 150 concurrent users. Yeah, this
kills the profiler and the system. So
now there yes um I am able basically to
record um queries and the calls but now
as we see here this is even though this
is chronos most of the queries uh have
hardly any execution time so we see that
the duration in the CPU time is zero
that means we're not talking about
milliseconds we're talking about
microsconds yeah fast as hell so and and
I don't want to see what's good I want
to see the expensive queries I want to
see What's wrong? Yeah, hell of spells.
Technically, we could accomplish this if
we do a profiler
tracing where we for example, we can
filter on the number of reads that
that's indicates the memory
consumption and or we can filter maybe
on the duration that we only want to see
queries that take longer than 20
milliseconds. So, we want to see what's
expensive, what what is causing
performance issues. Now the problem is
if we start to filter on these values
uh say bye-bye to the call stack because
the call stack is not a query at all.
It's just a comment and this always has
zero reads and zero CPU and stuff. So if
you start to filter the tracing the call
stick is filtered out. It's gone. Yeah.
Thank you very much. So um so so this is
the challenge we have. Yeah. either we
trace um
unfiltered causing one problem by
immense huge profiler traces or we
filter and then we don't see the
cost. That's a little
pity
but anyway for now for now
um once we have these traces recorded to
a file then um it's actually very easy
to investigate this. Um, now it was
78,000 lines. So, nobody wants to to
manually browse through 78,000 lines and
try to find out what's wrong and what's
good and whatever. No. Um, all these
kind of of traces can be uh
investigated. Yeah. So, this is plain
simple SQL code or maybe not so simple
SQL code but no rocket science. Yeah.
And these kind of scripts can can read
these trace files, group the queries and
then they can tell you what happens, how
often, how long does it take. Um so um
that that you can decide yes this is a
frequently and or oftenly occurring
problem. This is something you want to
fix. This is something you want to
ignore. Yeah, this is all the idea. So
just to group the data and then then you
can come up with resolutions.
Um so this is a
a let's say a generic script to
investigate these trace files. But there
is also another one you should know. Um
this has been published by Microsoft. Um
this is a a script that also
investigates these traces but this one
combines the call stack with the SQL
statement. Yeah. And this is actually
very cool. So, so you have the SQL
problem with all the resource
consumption, the duration, the
occurrence and everything and you have
the link to the nision world. So, yes,
that would be actually pretty cool, but
the cost for for creating this call
stack trace is pretty high and and for
this reason
um it is very tricky to isolate problems
um in in a service tier world now. Yeah.
Because there's no more user delegation.
So um what I suggest or highly recommend
actually is you should always have a a
separate service tier instance only for
debugging purposes. And this debug
instance should use a login uh apart
from any other login like like NAV debug
because then if you want to investigate
um all kinds of problems then you can
just and sometimes you have to do this
not on a test box but you want to do
this in a real life scenario on a real
hardware on on the real database. Yeah.
But this way you can just connect to the
debug server and then you can isolate a
problem and then uh look at it and then
you can use the profiler maybe with the
SQL trace and everything but then you
have actually a kind of pre-filtered
look. Yeah. So, so isolating the
problem. This is a tricky thing and it m
it's easier if you have a special
service here for this and for another
reason um there is um because you need
to change some setting or you should
change some setting for this debug
instance but I show you um why and
how. Yeah. So with these traces we can
do a lot but now well we see the problem
and what is the resolution? Yeah. What
should you do? Should you change some
code? Um should you change uh indexes?
Should you add
indexes?
Well, so basically most of the stuff
really is indeed due to missing indexes.
And this is something that that you have
to learn. Yeah. So creating indexes for
query problems is is not rocket science.
Yeah. This is done every day by
thousands of DBA in the world and you
can do this of course. No, but um if
you're not familiar with this SQL magic.
Yeah, it sounds there's other stuff
around there. We have a
script that works independently from
profiler traces. Whatever you execute on
SQL server is automatically cached on
the service tier uh on the SQL server.
Yeah, that's it has a procedure cache.
So, it memorizes everything it has
executed. So there are already the
expensive queries and with this script
we're just looking them up. So this is a
script looking into the procedure cache
and here I can see similar things. Yeah,
all the queries it's it's always the
same story. We just want to know what
happens how often and how many resources
does it consume? What's the pressure on
the memory? What is the duration uh the
CPU time? Yeah. And with this
information then we can work. Yeah. We
know what happens how often. What do we
have to fix or or maybe
not? And if you have such a thingy here,
you will often find kind of these
advices. Missing indexes. This is a
Kronos. In a real life, you will see
that maybe 80% of all the problematic
queries are just because of missing
indexes. Yeah. Again, SQL server is a
smart thing. Um, imagine this. SQL
server is entering the warehouse. Yeah.
Still looking for the red pencils. But
now there is no index. Yeah. As cursor
enters the warehouse, I have to ask
someone about red pencils. Oh
nobody here. Okay. Starts to open the
drawers. But while doing the open
drawers, escursor says, "Ah I
could avoid this if there was a bloody
guy telling me about the colors of the
pencil." Yeah. And this is how these
missing index proposals are created. SQL
server is forced to do something stupid,
but it knows in many cases how to
resolve it. So we see that it is just
because of a missing index. There is no
need to change find methods and changing
code units or whatever. It's just adding
an index. And on the lower section here
of this script, I'm just looking up all
these proposals. Yeah. Um and we can see
how often has this index been proposed.
What is the impact of an index here? I'm
filtering only on indexes impact greater
than 90. Yeah. That means like in this
case here SQL server has proposed for 84
times just a few minutes ago give me a
bloody index on this table with these
fields and if you do so the probability
is at 96 uh comma 82% that the problem
will be resolved or in other terms give
me that index problem gone. Yeah. So, so
all we need to do is to to pick up these
index proposals and provide these
indexes and this could be done in
management studio. Don't have to fiddle
with NAD. Of course, this has some
challenges. Yeah. And a lot of small
print. This is something that you have
to learn. Never ever copy paste these
kind of proposals and execute this. This
will raise hell. There's a lot of of of
crap proposed here. Yeah. It's just a
stupid machine machine generated
thingies. Of course, there's a lot of of
issues. Let's say it all needs to be
verified by a human being. So, but once
you have so have learned to interpret
this and and to clean up these
proposals, yeah, if you could could get
rid of all the the dust and dirt around
this, then you have here really really
grains of gold where you can apply quick
fixes. Yeah. Um because
um um these indexes you you can create
them on the fly while the users are
working. The worst thing that happens is
that the users get blocked for the
duration an index is created. So in a
large table, so maybe you do of business
hours. Yeah. But but this is a huge
advantage. You don't have to fiddle with
anision application. Yeah. Like um you
have partner add-ons. So do you really
want are you allowed to change keys?
Yeah. A key would also create an index,
but are you allowed and willing to do to
change some tables? What are you doing
if an object update is is coming from?
Yeah. So, so with this you can work
independently from the application and
you can work
fast. Again this is something that that
you need to learn. Yeah. Yesterday we we
spent a full day um on discussing
this
thoroughly. Yeah. So the the problem we
have is this kind of indexing is done on
the whole planet with by thousands of
DBAs every day. We just have some
specialties. We have some special rules
and I have a slide where all these
special rules are listed. Yeah. So that
we never ever name an index um dollar
something. Yeah. We have to be apart
from the division naming um never ever
touch a standard vision index in
management studio. Yeah. That will be a
ripple. But but if if you have learned
this then you have a very very powerful
thing to quickly fix problems.
[Music]
Um where is it? If you do this kind of
troubleshooting sooner or later you will
uh with the vision 2013 you will find
some expensive
queries that look like this. If you do
this profiler tracing or
whatever and you see it maybe here from
the scroll bar, it's a pretty long
query. This query has more than 18,000
characters and this has been fetched
from a real life scenario. So this is
not a fake
thing. So now tell me what's wrong with
this
query. So any ideas? No. So this query
it's called a smart query. Yeah. And
this is actually an insult because this
is everything but smart. Okay. Anyway,
so now this the problem is this is
unreadable. You have no idea how uh
what's going wrong. What is the query
doing? Yeah. And now if you start to to
format this manually with every keyword
you do line breakers or you're screwed.
Yeah. It takes forever. So what I
recommend to use is and there are a lot
of refactoring tools around addins for
management studio that can do some
formatting and the thing that I prefer
to use is Apex SQL refactor. This is a
freeware tool. You have to register for
a download and this is a plug-in for
management studio and with this you can
define how to line break, how to indent
and whatsoever. And if you run this apex
thingy, what it will do is transform
this query into
this. And now it is
readable. By the way, what we are now
doing is this is black belt
troubleshooting indexing. Yeah. So this
is really annoying. So So now we have
this query having 16 subselect. How
come? Yeah. In the old days when you
open a card or something um with the old
way to to create flow fields and this
was firing half a dozen of queries to
the SQL server each flow field has been
calculated by queried by a separate
query. Nowadays if you open a page all
flow fields displayed all subpages all
factbox what whatever is placed on the
page all this is created into one single
query which is called smart query. So
any flow field and this is one huge
select with in this case 16
subselects. And now the problem is if
there is just one subselect screwing up
the whole page is done sometimes. I had
a case where where we had an item page
and I'm not lying here. This opening
this item page took nine
minutes. Hell on earth. So what and now
what what you need to do in in in this
kind of scenario in this case what you
need to see is the execution plan. The
execution plan could be looked up here
from these links
here but I have already prepared
this. So so those of you have seen
execution plans before. Yeah. Now this
is a plan for men. Yeah. This is for the
big guys. Not the plans we have in
the old days. No way. Yeah. So this is
how an execution plan looks like. So
smart query. So how what is the next
step? If you have this now you have to
find high cost operators. You need to
find operators here that have
exceptional high CPU load or um
operators that do sequential reading.
Yeah. Scanning indexes. And this is what
you have to find in these monster plans
and sooner or later you will end up
here. Yeah, here we have such a high
cost
exception. So yes, this is probably the
thing screwing up causing all the
trouble. So now with going with a mouse
over you can see um yeah the table uh
names the the aliases here's something
about the quantity the filter whatever.
So and with this knowledge now you can
go into our query and there's
[Music]
another and in this case it is this
subsect this is the the problem the
troublemaker and then again the only
thing that is necessary and this select
is insufficiently supported by there's
no index to make a long story short yeah
um so by just adding an index, obeying
all these rules with naming convention
and whatever um just adding this index
um made a difference between hell and
paradise. Yeah. And the same was with
this item page of nine minutes. It was
just one single index missing. Adding
this index back to opening this page in
less than a
second. So by the end of the day, it all
boils down to the same. So we have
expensive queries, pressure on the CPU
taking forever, just requiring a bloody
index. This this is what most of the
trouble is is boiling down to. Um but
the problem now is with this smart
queration, we will have a lot of these
problems. It takes forever to
investigate this. Yeah, with all the
execution plans and
whatever. And this is why I would
suggest
this to go back a little bit here to my
service.
Here you should have your debug
instance. In this debug instance, you
can disable smarts
SQL. So if it has been introduced in the
more or less recent hot fixes um I think
middle of this year uh around so and if
you disable smart query you don't get
these monster queries. In this case,
each sub select is fired separately like
in the old days. Yeah, basically smart
query is a good idea because the idea is
to reduce the traffic between service
tier and SQL server. Um, but for if you
have a problem coming up, if a opening a
page takes forever, then root this uh
this user to the debug instance which is
not doing smart SQL and then you will
see instantly which select is screwing
up. You don't have to do all this
filling with these monster execution
plans and everything. Yeah, this is
terrible and time consuming. So this is
what I highly recommend. Have your own
debug instance without using
smarts.
Oops. Okay.
So all these rules again they are listed
on the slides. Uh all the dos and don'ts
how to do this whatever I now briefly
discussed to follow for
you this smart query
thingy. So the third area blocking and
deadlocking.
Um yeah have mixed feeling about this
but okay
anyway the most important thing to
understand is that locking is just an
administration mechanism. SQL server
must know at any given point in time who
is reading data who is writing data and
it it needs to know this to maintain the
data integrity and this mechanism to
manage all this is called locking. A
lock is nothing but a status information
for a system resource for a record so
that SQ knows someone is reading this,
someone is writing this. So this is not
a problem at all. Locking is mandatory.
It's
necessary. The mechanisms that that
happen in the rear end in SQL server are
quite complex. Yeah, we have different
lock modes. We have different levels.
It's an escalating locking mechanism.
Yeah. So SQL server yes could start
rollocking. It will start rollocking if
possible, but SQL server could decide
differently. SQL server could decide to
instantly hardlock a table. Yeah. Or it
could start roing and suddenly replace
ros with a table lock and stuff like
this. And besides this, there are
so-called transaction isolation levels.
Yeah. So, so this is all very sounds
complicated. It is. Um, but the
advantage is that this complexity
actually means precision. So technically
SQL server is capable to precisely lock
resources down that are real necessary
to lock. If you remember the old seaside
server yeah the native one in the old
native server the only thing we had was
a digital a digital locking. Yeah table
lock on off that was the only thing it
could
do. So locking itself is not a problem.
Yeah. So here I'm explaining the the
modes and what actually mean. But then
again the lock itself is not a problem.
The problem occurs if we end up in this
matrix of doom. Yeah. This is kind of a
simplified decision matrix of SQL
server. Um for example if we have two
users at the same time trying to update
one. So the first user tries to update
and if nothing happens so if the
resource is shared the user gets the
update lock granted and is allowed to
change a record. Yeah to change the
address of a customer
record. So now if a second user tries to
change this customer at the same time it
will also ask for an update lock and SQS
will look up oh sorry we have already an
update lock here. No you are not allowed
to proceed your change. Yeah. So, so the
lock actually turned into a block. Yeah.
One user has to wait. But that the block
is happening is not an error. It's not a
malfunction. Yeah. It must happen this
this kind of blocking because it's an
integrity protection. So this is not the
problem. And this is something we never
ever can get rid of. What is the problem
is the circumstances that lead into this
blocking situation. Yeah. So and and
with this um if you talk about this um
the circumstances we have to talk about
probability. Yeah. How how likely is it
that you have two processes at the same
time changing the same customer record
and so on. And here um um what spoils
all this probability is this lock
escalation. Yeah. Because the higher SQL
server escalates the higher is the
probability to face to to get blocked.
Yeah. So, so the risk of having
conflicts on a row level is very small.
But if you were starting to hardlock for
example the whole database, of course
it's maximum damage. There single user
mode. So, so the higher it escalates,
the more critical it gets. So here it is
important to remember that we can
influence this lock escalation by
forcing row locking. Yeah, this is
something we can do in the old days up
to Nision 2009. So with forced roocking
we minimize the the probability of
having conflicts because we tell SQSO
you must start rollocking and you remain
as long as possible on a roll lock
level. We we suppress the lock
escalation. The cost for it is we
consume more memory. Yeah this is forced
rollocking uses up more memory and so we
are back to server sizing. Did I ever
mention that you cannot have enough RAM?
Yeah. RAM RAM. RAM ram. All right. The
more RAM, the phase safer this work.
Um, according to my experiences, you can
use uh always rollock safely if you have
at least 16 GB, in some cases even less,
8 GB and
up. Um, this is not available anymore in
SQL Server 2000 in Nision 2013. Sorry.
So um this um when Microsoft um
Microsoft said they removing this
feature because the RAM could be used
better. Some people had doubts and we
were right. So what we see now in NAB
2013 is a lot of escalated blocks of
escalated locks. So so we see a lot of
table blocks page and all that stuff.
This is coming from this escalation. But
nowadays there's no more way to to
handle this with this ro thingy. Um but
there's a plan B. There's a a trace flag
around. There's
1224. This is a trace. If this is
enabled, um um you switch the whole
server instance in a mode like force
warlocking. You you also suppress the
lock escalation. Yeah. With the same
implications like this other roing. So
this could help NAB 2014. If you have
these escalated blocks, locks and
blocks. But then again, trace flags are
working on a global level. So you have
to be aware um what else is using the
same server. Yeah. Because what is
medicine for NAV could be poison for
another application like like business
intelligence stuff, BI stuff, never ever
use this. And also never ever use uh the
old one 1211 which you always also still
find in the internet. Yeah, internet
never forgets. But this this kills the
machine with with 121. With the old one
you you can risk that you completely
um use all the memory for for locking.
And then the server just says, "Well,
bye-bye." Yeah, these isolation levels
that's a little
complicated. And this actually in the
old days um raised some severe issues.
Yeah. The way of how hard locks are
established in
NAB. And what has been uh one of the
most promoted improvements with NAB 2013
was that the isolation level that is now
used for hard locks is set to repeatable
read. In the old days it was
serializable which is raising some hell
so-called range locks actually. Yeah.
Which which really cause a lot of
trouble. And just changing this
isolation level to repeatable read
dramatically improved uh the behavior
according to locking and blocking. Yeah.
So this was one of the most promoted
things where they said oh we are locking
90% less and everything and so on. So
this has been very very promoted and
indeed this really really is helping and
what we can say that in NAV 2013 we see
way less blocks than in the old days.
So what unfortunately has been a little
underpromoted is that the old Nvision
versions can also use repeated read
isolation. You just have to tell it and
and unfortunately um there is no GUI
switch for this. No no no flag or
anything you can use. Um you have if you
didn't come across this knowledgebased
article explaining this you you never
never ever would would see this. Um
there's some uh system table DB property
and there's a a magic switch diagnostics
the default value is zero. So and if you
add this magic key here then your nision
the old nision also could switch into
repeatable read isolation mode. Yeah. If
you have these builds that are listed
here and just by by using this
repeatable root isolation you usually
you get rid of half of the number of
blocks often even more. Yeah. So because
the old way of how vision is locking is
is stupid. Yeah. Doing terrible
things. Um so so those of you running in
the old world this is something uh I
highly recommend to check this
out. This is something I will ignore.
Yeah, sooner or later we we will face
blocks. Yeah, because again this is
integrity protection and it depends on
the business processes actually if we
end up in a blocking situation.
Unfortunately, N vision has a lot of of
single points of failure just the way of
how ledger entry tables are numbered.
Yeah. When when you increase uh if you
add a new item ledger entry and the new
entry number is created is always the
same algorithm. lock the last record in
this table uh and increase the number by
one. Yeah. And and if you have two
parallel postings, they really try to
hard lock the very last record in the
same table. So really meaning the same
record and they are ending up in a in a
block of course. Yeah. And and NAB has a
lot of this uh single points of failures
and there's of hardly a way to to get
around this.
So yes, we sooner or later we we will
have
blocks and now I will create some
blocks. So I start my first session. The
first session will hardlock um the sales
header and then I'm starting a second
session with a separate code unit.
And this will lock the purchase header.
So go to my first session. So now I'm
locking the sales header. So again it's
really a lock. Nothing happened. Yeah.
No, no problem at all. Not
yet. My second session now is locking
the purchase header. So so far
everything is cool for both sessions.
So now if the first session which
already locked the sales header now it
tries to lock the purchase header of the
second
session. Now I have a block. Yeah
because the purchase header is already
locked by the other session. I try to
also establish a lock and SQL server
behaves impolite giving me the middle
finger. So this is this is a block.
Okay. So um again it's ask server
handling all this and I'd like to
introduce a way that that I use um to
investigate or to detect these
blocks which basically is a very simple
way. Um we can create
alerts as event
triggers. Yeah, there is again it's a
performance counter that is already
there. So of course the system realizes
there's something
blocked and what I do now is um in case
of such an event I am firing up a
corresponding job and this job um runs a
store procedure that collects all the
information about a block and saves it
to a table. Yeah. So it's a a fairly
simple event triggered way to
automatically record blocks. So when
it's happening it's automatically
written into a table and this
information could be investigated any
time um in this download package maybe
have a quick look and what I provide. So
for those of you who want this you find
all the scripts even numbered so that
you know in which sequence to execute
with and then you can establish this
easily even with with a small SQL
knowledge. Yeah. So that's again it's no
rocket
science. Yeah. So, uh, what I when it is
recorded, then I just can whenever I
find the
right script, this one
here, I can look it up in my
recorder. This is a lot of stuff from
the days
before. And then I can see again what's
happening, how often. For me, it's
always important to count the problem to
see what's important, what you want to
fix, what is you uh what do you want to
ignore or postpone. And then you can
group the data however you like. This is
just templates to see which table is
locked, how often, um all the details,
which queries, blocks per hour, blocks
per day, whatever you want to
do.
Um so basically that's
easy. Now the extra challenge that we
have to face
is in our dear NAV 2013 world we don't
have a user delegation. So if we have a
block like in my situation what we will
record is always service tier block is
blocked by service tier. Thank you very
much. But then again blocking is usually
about business process. It's the
circumstances. It's the workflow leading
into this metrics of doom. So we need to
have a relation to the business
process. Um so the the least thing we
need to know actually is the username.
Yeah. Somebody we can ask hey what have
you done when you were blocked? Yeah. Or
the culprit um causing this block. So
without knowing the user it's a really
tricky challenge to find uh any clue
about the workflow about these
circumstances. So this is a a big
problem we have um with NAF 2013.
But there is a way around
this. So what we can do is um again
running profiler traces and this also
could be done automatically
uh this one
here. So prerequisite is I enable the
SQL trace feature. Yeah. So that the
call stack is sent to the SQL server and
then I'm filtering on a special string
combination and save it to
file. So this is actually just a trace
on the call
stack. So if you have
this Yeah. This is just such an example
call stack trace. If this is
um loaded into this little code here.
Yeah, that's all a little SQL
magic. I can can parse this string. And
then we actually we get a list of which
SP ID the process ID has been which user
at what time. Yeah, this is the
information we need. So I know that JTOK
has been spit 57 at this
time. So all these block recordings of
course they what I can record is the SP
ids. Yeah. So I have the SP ids and I
have the time. So if I have both this
SQL tracing thing and the block
recordings, I can combine this. So with
a little another SQL
magic it's just just huge select
statements nothing
else. So I can marry this. Yeah I have
on my my block recordings recording SP
ID and everything and here I see login
as SQL service but now I know which
human being it is. Is it Smith? Is it
Taylor? Is it J? Whoever. Yeah. And and
then with this again we we get a clue
maybe to the business process.
So yes, we can do this. Yes, we can find
out which users are involved in these
blocks. Again, the downside is it the
prerequisite or requirement is to have
this SQL trace up running. And this
again causes a hell of a load. So so it
is impossible to to run this throughout
the whole day on all service tiers.
Yeah. You have to enable secret trace on
all services you have up running. Yeah.
So so I I give it to you. Um, no
warranty, no guarantee, no support, no
nothing. If you use it, blame yourself.
Um, no, but you can use this on a very
focused scenario on isolated issues when
you really want to see what's going on.
Um, so what I suggest is if you start
this tracing, always have a close eye on
the size of the trace files so that you
can cancel all this if it's exceeding a
certain. Yeah. Not killing your
discs. Yeah. And in this way um we can
keep track about blocks. We know what's
going on and come up with
resolutions. At this point I will make a
little excursion to some other nice
tool. Um we
have you probably know you know activity
monitor. Yeah this kind of basic thingy.
We see CPU a little this and
that. Also here you could see which
processes are blocked and whatever.
There's a a neat tool around so I don't
know if it's really important but just
for the fun of it it's from Adera Iera
SQL check freeware
thingy this is a kind of um activity
monitor plus so you can also see all
kinds of statistic and everything but
what I find quite funny is this the way
how they displaying the processes yeah
so there's a a legend where you can see
what it's done and the nice thing is you
can see um these blocked processes.
Yeah. Who is blocking whom, who against
whom? Yeah. So, so visualizing the data
very easy with this thingy. You could
actually monitor multiple server
instances if you have. Yeah. So, but you
don't want to see that with 150
users. Yeah.
So, just a little
side. Yeah. Um the queen of blocks is
actually our dear deadlock and a
deadlock is a situation when we have two
processes in a kind of crossover
blocking situation. So everyone is a
victim and culprit of the opposite one.
Yeah crossover block
and to learn about these kind of
problems.
Um again basically um profiler will help
because there is an event that's the
deadlock graph. So whenever um a
deadlock happens SQL server could create
this graphs and this is just XML
information. So this deadlock graphs can
be recorded and everything you can do in
profiler in the guey you can do
automatically with a little SQL code.
Yeah. And then again the SQL code you
can have um so the trick is just to
demonstrate this not really and whatever
you click here in in profiler you just
can script the definition for it and
then then you see the plain SQL code
what's happening and this way you can do
this magic all automatically with jobs
by executing the same codes the job or
whatever. Yeah. So here I'm close to
such a deadlock situation. Yeah. If you
remember, so first user sales line,
sales header, purchase header, this
sales header tried to lock this purchase
header. The first block, this is a
session that is still up running. So now
if this second session tries to lock the
sales header of the first session, then
I have this crossover block. So a
deadlock never can h take longer than 5
seconds. Yeah, there are system
processes that are searching for these
crossover blocks every 5 seconds and
will automatically resolve this. So if I
do this one, two, three, four, five,
five, five, five, five seconds. Yeah.
Okay. So just have
to Yeah. So also these kind of events
can can be fetched. So I know that there
was event of a deadlock. So this is
written to this. But what I did also is
in the background I ran a secret profile
that has an automatic
trace which was actually catching these
graphs. Yeah. I always wonder how many
spare time they have in Redmond to
create pictures you can move around.
Thank you very much. No, but these these
graphs can be exported. Yeah, you can
you can pick them up. You can export
this um extract event extract SQL uh
deadlock event. Sorry. So, and if you do
that, what you get is an XDL file. An
XDL file containing these deadlock
graphs.
Well, XDL is nothing but just plain
ordinary XML.
Whenever Internet Explor or try stop or
whatever.
Oh,
maybe close
this. So, here we go. Yeah, it's XML.
So, in the easiest case, um all you need
to do is um to just do
this time.
You pick this XML and just drag and drop
it to an Excel spreadsheet. Open it as
an XML table and then you get it in a
clean structured way and then again um
you can group, you can count, you can
make your PEOS to see what happens, how
often, who is blocking whom and so on.
Yeah. So, so and then then we can start
to analyze making up our minds to
investigate
this.
Well,
okay. So, this is what I wanted to wrap
up and hopefully filling some some
interesting tools into your toolbox to
get you started to do this uh
troubleshooting. Um, do we have any
questions? So, hang on. So, and if you
ask a question that I can answer, you
get a t-shirt and a book.
So, do do we have a microphone or
something?
Oh, it's coming. Okay.
Hi. Uh, thanks for the tips on finding
the users causing the locks. Um, is
there not a way that Microsoft can
actually pass through that
information from the service tier to SQL
Server as a comment? This is um this is
a question we need to ask Microsoft. Um
it's feasible though. Um I I would say
the the service tier is managing this.
The service tier of course should know
which nision session is which cle
process. Um
and I just guess but but I think it
shouldn't be that tricky to create a
kind of virtual table or maybe better a
physical table or something where we can
see which SQL session corresponds to
which navigation session. I don't know.
Um, so far I haven't seen anything. Um,
so if it's possible then maybe they keep
it secret to keep me busy. Yeah, thank
you very much. No, I don't know. So um
anyway, I give you this. Yeah,
but yeah, and and this is maybe another
challenge we have to face um with um the
vision 2016 as a service if it's all
running in Asia and stuff like this
because here with this kind of hosted
scenarios we can establish this kind of
blocking deadlocking uh detection
routines and this is zero option in
Asia. Yeah. So if you have this as
managed service if there's any blocking
we cannot touch the SQL world. So, so we
will always be screwed. Yeah, we see
there is a a block because uh the victim
actually will get an error message. Um
but we have no idea what exactly was
screwing up, who was causing the block.
Um this was briefly discussed um during
directions with um I think was his name
Chaday I think is his last name who is
into this Asia software service magic
but we have no no resolution for
this so yeah I don't know I don't know
but I guess no there is no feature
any other questions and I have to
apologize I don't see any the
demonstration was in the slightly older
version how speed in new version 2016.
I'm I'm sorry I didn't understand. The
demonstration you made was in a slightly
older version, not the 2016. How is the
speed there?
How the speed is there? Yeah. Is it is
it faster?
Is it there? Oh, this session is
recorded. And now you're asking me about
something I should answer honestly. Um,
no. I didn't test anything on 16 because
I learned to wait for update 56 or
something. Um
[Applause]
because
usually all the first
versions screw up a little bit. Yeah. So
I give Microsoft a chance to fix this
first before I do my comments on this.
Okay, other questions.
Oh, you have to come down for the book.
So, this this kind of work out for me.
No worries. That's okay. Um, do you know
if we'll uh if we raise the
compatibility level of the SQL database,
it will have a positive influence on
performance. The compatibility level.
Yeah. So, the comp I reserve this for
you. So
just um the compatibility
levelh you know what it is. Yeah you
know that okay so actually the
compatibility level defines the language
the database
speaks. So in all the supported
scenarios
um the forision it should always be in a
level of the actual server. So if you
run the vision 2009 R2 on a SQL 2012 and
also the compatibility level should be
in this case because only then um the
the SQL server could use the full
product stack and and and use all the
dynamic management views and all the the
funny features they you only need to
have it in a backward compatible uh
compatibility level if you have your own
custom programming that is using an old
syntax or if you have to run some
non-supported scenarios. I have some
customer running in a vision 4 uh 4
service tech 3 on a SQL server 2012
which not supported at all and and they
have to run it in a compatibility level
of SQL
2005 because else you get error. So
basically you always should have in the
same in the real server version um which
normally also um could improve
performance in in in scenarios with N
vision 2009 and SQL 2008 there's some
difference here um and only if you have
your custom programming then um maybe
you need to be backward compatible
so okay I have a question the repeatable
read lock you told us that is a nice
feature that is also available in the
older versions if you um check it in as
a square management studio is there any
downside or do I have to check if uh
it's okay for the customer now now you
got me because I try to come around this
yes there's a small print but it's a
very small um the risk of repeatable
read is um so-called phantom reads
um in the old days um with a
serializable isolation a whole range in
the clustered index has been locked on.
So, and and this was accidentally
locking records that are not actually
part of the the result set. So, there
was a lot of records locked that has
nothing to do with the actual query.
This is range locking. And I need to
draw pictures to to make this plausible.
So, repeatable read means there is no
more range lock. Only the existing
records in the result sets will be
locked. So, the range is open. And the
advantage is that now we don't have any
overlaps anymore and and so the read
performance is improved unblocked. The
risk is now since the range is open of
course something could be inserted into
that range and this is called phantom
reads. So, so that suddenly there's a
record that didn't exist before and and
a phantom arises and this could of
course have impact for the performance
for the not actually for performance but
for the data integrity and this has been
discussed with Microsoft a long time in
the way of NAB
2013 but actually the discussion was
ended because um the Microsoft guys
never ever have seen such a phantom read
within the vision. I never have seen
that and and the end of the discussion
is that this is now standard isolation
in nision seven and up. Yeah, I
personally only have seen two phantom
reads in the past uh five years so to
speak. Um and in any case it was just to
due to um stupid programming. Yeah, that
was like you have lots of companies and
in the same time all the companies were
writing some data into a master company
some some intercomp magic. Um yeah and
of course that that caused a problem
here but in
99.9999% of all cases that is okay.
Yeah. So, so the political correct
answer is if you do this repeat test it
and if anything weird happens, you have
to roll back. But the chances are pretty
high that nothing weird happens.
Okay. So, I'm not sure if we have time
for
t-shirts books are all gone. So, so
probably
one. Okay. Yeah.
Um, next time I bring my sunglasses.
Isn't it kind of risky perhaps to add an
index in the management studio and
behind NAV? So NAV doesn't know about
it. So except of the um special NAV
indexes.
I didn't get the first part of the
question. Um is is it some kind of risky
to add an index in the SQL management
studio with uh NAV not knowing about it?
No. Um so there is um small risk if you
obey to some rules. So um what we have
to we must really avoid is any any
overlap with a naming or with the
standard structures of nision. The
vision is naming indexes dollar 0 dollar
one dollar two. So never ever in your
life create an index named dollar 7.
Yeah because sooner or later this is
will cause hell. So so you need to be up
if you do your own indexing the indexes
should be named totally differently. And
of course, this also makes it easier to
to separate the customuilt indexes from
the standard indexes. So with all kinds
of scripts and code, you can isolate
your thing. Um and and then you can't do
anything wrong. Um what you have to
learn is to create indexes in in
appropriate way because these missing
index proposals sometimes propose stuff
trying to copy tables. Yeah, this um you
have very huge include clauses and you
get proposes where where a SQL server
tries to copy item ledger entry five
times. Yeah. And of course this is rock
and roll for read performance but write
performance sucks big time because you
virtually insert every record five
times. Yeah. And and this is if you know
these dos and don'ts, you can't do
anything wrong. The vision cannot drop
these indexes accidentally.
um apart from from some VIFT stuff that
that could be um yeah there's
circumstances that can be uh causing a
drop. Um but this all could be handled.
So
um so the risk is is minor. Of course
you need to test anything and all this
questions regarding how to manage this,
how to document this, how to roll out.
Basically this uh obeys or implies the
same challenges uh you have with any
other add-on you create inn net. Yeah if
you do a net component you also create
it not in object designer you do this in
visual studio and also you have to take
care about roll out and stuff. So it's
the same questions and there are the
same answers or similar answers.
So if you like I I have scripts and
tools to to document this to roll this
out making sure that N vision cannot
drop this in this way um you can't do
any harm you you only can
help okay so I guess one more another
one
okay yeah there was a slide um with Next
up,
um
the I was thinking short answer or a
long answer. Maybe medium. Um maximum
degree of parallelism um should always
be uh decreased. The default setting is
zero. That could mean that one query
kills all CPU. The rest of the world
will set maximum degree of parallelism
to the half number of CPU. That's a fair
assumption. This does not work with no
vision because no vision queries are too
stupid for parallelization. They are
just plain simple. There is no point in
parallelizing parallelizing and
um what happens with nision if you have
parallelism in the old versions um is
that we we have to suffer from parallel
index scans that screw up. So in the old
nisions up old means up to 2009 R2. Um I
recommend and this is also Microsoft uh
recommendation in some some uh articles
to um suppress parization by setting max
stop to one. This applies to all the
older versions. In the new versions with
all the SWAT smart queries and other um
relational commands um I have some some
good experience in slightly increasing
max stop to two. This is how I said it
and then so far it's
okay. So
hopefully okay. So I think I have stolen
enough of your precious coffee break. So
I'm here if you have any questions. I
I'll be around the whole day. Um so feel
free to uh contact me here or of course
maybe uh offline or wherever. Um enjoy
this conference and thank you for
attending this session. Bye-bye.
