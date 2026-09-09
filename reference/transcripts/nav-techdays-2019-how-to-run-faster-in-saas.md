# NAV TechDays 2019 - How to run faster in SaaS

- **Source:** https://www.youtube.com/watch?v=7_NCxJSWnyM
- **Video ID:** 7_NCxJSWnyM
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 103m32s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

welcome to this session on how to run
faster in sass and I'm barter up there
and I'm one of the application
architects in Vincents team if you saw
the keynote hello and my name is
Alexander Molotov and I'm engineer in
the server teams and hello my name is
Kip McKean I'm the one at the
engineering managers in our application
team so in this session we're going to
look at some of the differences that are
between running on Prem and in Asia
because we have a lot of partners asking
us what are what is business central
running on because to you it's a black
box it's just a service and we will try
to uncover what's in there and to
demystify it but it also help you to
leverage the powers of the azure cloud
so when you talk about cloud we usually
see cease to pick just like this one
right or some other thing where this
shows cloud but in reality it looks
something like this this is in Dublin
it's a huge data center a mile across as
you can see on the drawing and we have
our own thousands of these around the
world if we look inside it's obviously a
bunch of machine with physical machines
and each machine physical machine will
contain a number of virtual machines
obviously and they're all based on
mainstream Zeon and Mt
epic multi-core CPUs and nothing of this
so far is secret or hidden because
there's documentation on Microsoft talks
just go there and Google or Bing it and
you can see that we generally run on no
2 2 point something gigahertz 2.3 this
kind of hardware so that's the machinery
part of it
and for time being I mean we experiment
in our cloud but currently we run
approximately four cores on our
industries and 14 to 16 gigabytes memory
so that's one of those configurations
you can see there
same thing for sequel again you can go
and look it up and dogs we use what's
called elastic pools where we buy a
certain amount of resources CPUs and so
on and then we can place a number of
customer database within that elastic
pool so it's more that part of it I mean
the last part of it is more a pricing
thing than a physical thing again
it's no secret you can google it look up
in documents and there are three tiers
three different types of hardware the
cheaper ones run on regular
hard disks and the most expensive one on
the right premium runs on SSD disks and
the main difference between them is the
latency obviously due to the disks and
also the power of machines so when we
run customer production customer I'm
tenants we use the peat that the one
that smartness p4 premium and production
if you have a sandbox or a trial signup
we generally use that the other one the
standard configuration because obviously
there's a cost to the premium compared
to the others again look it up if you're
if you're interested and how many
databases to pack on so in such analyst
pool it depends can be one if it's a
huge customer or it can be a hundred if
there are a lot of trials that are not
used depends
this is an overview of all the services
that we use to run our services and
obviously we don't care about this
because this is just technical so we're
trying to line up what do you care about
I mean I'm iron Hendrik we are
application developers so we are
actually technically one of you except
employed in Microsoft and we care about
this so you have a customer or users up
there who access our client the client
talks to a balancer or a gateway that
then routes the requests to any one and
his team and you can see we have a
service fiber cluster as its called
that where we can have between five and
eight currently industries running so
you all of each of those Anestis think
of them as IBM with four cores for the
time being by the way you can do the
same you're yourself if you want to and
notice also that the NSD talks to a
database that again has two replicas if
you saw the keynote just before Vincent
showed one replica that is actually two
replicas you should also notice that
even though there are free and his t's
up there I mean let's say that this
customer is the first one who logs on we
route them to the same NST because then
they can share the cache it becomes more
efficient let me unless they're too many
users and this is how things look right
now because this is something we change
over time as we learn more and get
different loads and another customer
would then obviously be route to a
different industry and have its own
database and that all those databases
are for invoicing purposes or for
resource management purposes part in a
pool
so called audacity pool another thing to
notice is that these machines are placed
separately obviously and there's
approximately I mean this is not a
guarantee but in the order of magnitude
is approximately one millisecond latency
between an NST machine and a sequel
machine this is something that's
important later another thing that's
important to notice is that if a user so
if you look up the user up there they
make a change a delta that will of
course be sent to the databases so now
we write to the database and it has to
be replicated to our mirrors that means
that commits so when we commit a
transaction obviously all three database
need to report back yes I'm done that
means that the commit statement that we
know in ail is actually quite expensive
of expense meaning microseconds but it's
more expensive than it used to be
because we need to have this two phase
commit between the databases the other
thing that Vincent also notice and
mentioned and Alex will talk about later
or I will one of us will talk about
later is that those mirror databases
currently they're just there in case
something goes wrong with the primary
database and that's like a waste of
resources because it each of them is
actually a full sequel server so why not
route you know read-only requests like
repo'd running and such API calls and
OData and whatnot do that so more about
that later
now how many tends to be then packed on
one of these clusters in short it
depends because I mean how many how many
users do they have and how
much work do they do and what do they do
so what you do is we monitor these we
have a lot of telemetry and we have
graphs and sorts and Alex will show a
lot of these in a second
couple of minutes and it's also
something we constantly work on then if
we take even deeper into when you look
at what happens when we actually run our
code so I have tried to do some
measurements and these are not
scientific I would say but these
measurements is done on a cheap fork or
machine actually to core with
hyper-threading to gigahertz so it's
very similar to the games we were
running with and if I create only al
code just pure ale no no external calls
to sequel or web services or anything
it's in the neighborhood of 300,000
statements per second whether it's 200
something or foreign something doesn't
matter it's that's actually fast sequel
access on the other hand yeah I mean
just the latency between machines and
sequel delivering results and so on
limits this to approximately 300 queries
per second you see that's a factor
thousand and obviously some sequel
statements I mean if they include joins
or big data sets they may even take
seconds right
another thing we also looked at is
what's the ratio I mean if you take a
look at some code unit or some your own
code or our code
how many pure ale statements do we have
and how many database calls you have and
I made a very simple count just to call
the code units because code units mainly
consists of cold so I counted all the
statements and then I counted all the
database related statements and it's
approximately ratio one to ten or ten to
one let's write it there which means
that on average when you execute program
you click something or open a page or
something an average will execute ten
airlines before we hit a sequel
statement and you can see during due to
this other two lines we basically only
care about sequel statements for the
same matter which is also what Vincent
pointed out now that was boxy pointed at
pointing out so inside our NST we have a
thread scheduler that will I mean some
of you may have seen a picture like this
perform so when you have many
simultaneous processes we do a slicing
where we allocate 50 milliseconds to
each process in a round robin fashion
and the number of active simultaneous
threads is 3 or 4 as it depends on how
many cores we have on the actual CPU and
we'll also note that we do prioritize UI
sessions over background sessions or
that service requests so this is a new
feature coming next update so we're not
doing yet but in with 15:1 we are the
beneficiary when we prioritize your ice
sessions versus but I think we should
have been running with that for some
time no no ok we should
anyways that that's a prioritization
matter here if you look closer at what
happens within those 50 milliseconds I
get so by the way that one is just drawn
in Excel which means that it looks like
all the slots are in synchronous are
synchronous they are not obviously each
lane is different so you click a button
open a page and you get allocated a slot
of Mill 50 milliseconds so how do you
use it well you run maybe maybe not
ten airlines on average statistically as
we show and with that speed that takes
zero point nothing right seconds or
milliseconds so almost immediately you
will hit I mean statistic speaking
almost immediately you will hit a sequel
statement so we to create this sequence
it meant send it to sequel and then we
wait for the result but since we know
that that can take ages to get back we
give the give the thread to the next
session translation so somebody else can
get their 50 millisecond yeah well again
this is in 51 so before it was a bug and
it wasn't true this and we're not not
always giving up the time slot back to
the scheduler correct so it will also be
great improving performance in next
update yes exactly but it also means
another thing that's important to notice
that if there's a big load on the server
so let's say that you have a hundred
users and a lot of background sessions
those three I mean now we only have five
there right but imagine you have
hundreds of sessions then when you when
sequel returns with the result that
you're interesting in interested in
maybe you need to wait for the next bus
to arrive right or annex train to arrive
you
to wait for your next 50 milliseconds
drawing another implication of this also
is that 50 milliseconds sounds like very
little but it's actually a long time
because within a whole second which is
in a very long time there are only 20
slots so they're only 20 slots times the
number of threads so that may only be
maybe 16 slots per second this is just
to give you some of the fundamentals
that we're dealing with and this is same
on premise so yeah but then I will hand
it over to Alex who is magic wand so
let's talk about the cloud service
performance and when looking about the
performance there are at least three
components you need to be aware of the
first of all is this service compute
performance and that is something you
cannot do anything about this is
internally for Microsoft and that we're
trying to improve how to run our service
well there's the database performance
and there also multiple things in this
one is amount of queries and how good a
queries your Orion where the second does
how good database performances and the
third thing is application and we'll try
to cover all three things today and
let's start with computing so this
picture is showing all our clusters all
our data plane services and you can see
here that each each each rectangle is
dedicated service fabric cluster and the
size is actual the relative load on this
cluster so you can see some of the
rectangles like really big mean that
they're getting old of requests or a lot
of tenants and some of them barely
visible here and that was a problem last
year when we just start looking to this
and the problem because you can happen
because of the way we are getting new
tenants when tenants are coming and
getting trial tenants we assign these
tenants to a cluster and stay there for
quite some time
please until the next update where we
can move them around and a lot of
tenants just trying the product and
maybe they'll come back the next day and
next week but maybe they'll never come
back but they still existent on their
own the cluster and the way we did
balancing before was based on the total
amount of tenants per cluster so I will
not give it the number because it's
changed but here it all can all classes
have the same amount of tenants but
Tennessee of different sizes and
different doing different activities
that's what we tried to improve if you
look to this picture it's showing all
services were running in data plane you
can see an ST in the middle and all
services around it and I will not talk
about all of them but I'll describe our
recent additions you can see here it's a
gateway service and the tenant balances
service they was deployed few months ago
and I'll explain what what they're doing
if you know the way we take an addition
to the cloud was very simple right we
take an st and webcore we'll move it to
virtual machines this cloud put load
balancer in front and use simpler out
robin to distribute requests among
machines and what it lead to let's say
you have a user from one tenant oh sorry
it's a different slide was which in
slides little bit before presentation so
let's step back let's talk about
synchronization first and why this is a
problem the way we do cache
synchronization in division of business
central is very simple so all machines
connected or talking to each other
through application database and
whenever somebody written right and they
are reading data let's say user one from
first tenant written sales order the
requests go into tenant database and
then the data resides on indication in
one machine when another user from the
same tenant creating like new sales
order all dates and existing sales order
the data also reason to tenant database
but also a right on top location
database to a special table called cache
synchronization and all other machines
listen to changes for the in this table
and when they get the messages somebody
changed sales order table they will
flash caches so if you have multiple
users right on the date on different
machines they will flash caches
constantly and you always get cold cash
and this is a problem for performance so
here you'll see that this will flush the
cache and next time
the facility will reach sales order it
will not read it from the cache but go
again to the database so the first
improvement we did in this area is we
increase the performance or increase the
speed of delivering this messages across
machines instead of using application
database we'll start using as a service
but this is more reliable and more
performance solution and we see some
performance improvement in this area but
so this just shown the flow so the folks
exactly the same but just using
different communication mechanism but
now let's talk about balancing and why
it's important here so as I said before
we used very simple round-robin
algorithm and we used a load balancer
this is l4 I think it's some hardware in
the data center we distribute request
and work very simple right if you have a
first user cannon who put it to one
machine maybe not the user from the same
tenant camera will put it to another
machine and use it from this like
another tenant get to one of the machine
it was more less random right who just
round-robin distribute request and the
problem with this approach there is
multiple problems I'll say the first one
is a cache and the second one is the
load is very unequal we treat requests
from users and from all data the same
way but the problem that user requests
they when they came to machine this
should stay in the machine because of
the session and we can see some like
skewed machines with a lot of sessions
on machine it was less sessions the
first thing we did we create our own
gateway service so this is l7 balancer
which gives us solidity to control how
we balance users and tenants across
nodes and on the first iteration it was
important pretty much the same at user
round-robin algorithm and this was
deployed like almost like eight months
ago those nothing really changed but the
next step what we did we created new
service called an imbalance of service
which keeping the mapping of tenants to
machines and what happened now is if you
have a first user from the first tenant
map the Machine won and you have another
user from the same tenant cannon were
put into the same machine like if
possible because sometimes we have very
big customers and we need to distribute
them across multiple node but in heavy
past scenario were trying to put all
tenants from the same for all user from
the same tenant to the same machine so
they always get a warm cache and much
better performance now you see that user
from another tenant coming will put in
it potentially to another machine
because of this also have to improve our
task scheduling so task agent is the
underlying technology on under job juice
so all our job queues Behance and using
task scheduler and we actually now doing
the same thing so when tasks need to be
run who asked internal balancer for
specific machine where the tasks need to
be executed and then task scheduler put
this task to this machine it's also in
some cases good because it give you also
warm cache but in some cases care can be
bad because it put a load on the node
and then but here we're way experimental
so we are we are trying to put sometimes
different nodes and maybe great big 8
machines which running only tasks this
is coming in the near future let's talk
about telemetry so for the last few
months I was involved in a few
performance investigations where I have
Arabic customers so the one example I
showed here it was a customer with more
than hundred users they had some
performance issues with their solutions
and we tried to analyze and help help
them to
make it much faster so in order to do it
internally we have built a special
report actually you can see this
building power bi and it's give us
overview on all different aspects of
performance for this specific tenant so
this is the first thing we're looking at
is the performance of the cluster where
the tenant is located so in this example
you can see few charts the first two
charts under the first chart on the top
is shown webcore it's our webserver
component CPU utilization the one below
is shown in a steel utilization and on
the right showing the memory utilization
and you know we're running a multi
tunnel system so sometimes unfortunately
you may experience better phone not
because of you but because of somebody
else there are some tenants which we
call the moist neighbor guys they can
run some very expensive iterations and
they can affect performance of the whole
cluster we're trying to solve it with
monitoring monitoring it or trying to
move tenants and you also know that now
we introduce in some throttling
mechanisms to avoid these situations but
that's it's kind of the first thing
we're looking at so if somebody
experienced performance issues who look
to the classic performance the second
thing for us is to see if tenant has any
degradation in performance is talk to
the some common iterations we cannot
look good to it across the tenants
because don't have different data there
are different customizations but for one
tenant I think it's a good very good
metric to look on on come on open
company so the first chart shown here is
how many times it was called and for
this tenant probably don't see but there
are couple of thousand times per hour we
call open company and the chart below
showing the performance and this I think
it's pretty good here it was some
problems at the beginning maybe frost
possible indicated that we need to go
and investigate what's going on there we
also look into this amount of sessions
created I mean so this was one of the
biggest customers who have hundreds of
users and you can see that most of the
sessions it creating our backgrounds
the teal color the yellow one is the web
service calls and there almost no UI
sessions in the chart but in reality dub
5000 some concessions created and
sometimes we also see that maybe you run
a lot of integration scenarios you call
a lot of web service calls it give you a
bad performance in other metrics which
is very important for us and for you is
database performance so again when we
look at this first the first thing
because we're running in the elastic
pools we're looking to the pool
performance we look to CPU and member in
a utilization of the databases this is
right chart at the bottom and here you
can see the database July's almost like
from five to ten percent which is not so
bad he didn't cuss me probably not
experience any issues here but there are
two other metrics which are also very
important the first one on the top I
hope you using when you run on premise
you also look to this matrix in the same
way the chart on top shown the weights
that from the sequel server and this is
different types of weights when sequel
server iterations waste was something
most of the times we see that sequel
weights on the logs so that's something
you can improve maybe without help you
need to see you you need to try to avoid
the locking on your queries or make the
queries running faster so they look only
for the short period of time in this
specific case actually I know if you can
see that but the most of the weights are
caused by network i/o and that means
that MST is not really doing good the
text actually sequencer is much faster
than sequel sorry we have a data which
we can consume but we just not doing it
for some reasons it may be because we
have a lot of requests or it may be high
CPU on the NSC so need to be
investigated and the one below shown
actually the queries actual sequel
queries and the time they execute it so
sometimes you can see very bad queries
or very large squares with so lots
examples when people forget to put
proper filters and they try to get all
data from the single server which will
be shown in this kind of chart another
thing as Vincent mentioned that's our
focus was next series is a report
execution we saw a lot of problems
caused by the Reapers and it's not only
Reapers but you know in any iterations
run run as the reports it can be a
problem and typically they are
long-running iterations and our
recommendation here is try just take
take a look see which papers you're
running and see if you can avoid to run
them given business hours yes some of
the operations really really heavy doing
a lot of logs and doing Auto City
consumption and also we saw a few really
bad examples when people was out of
curiosity trying to run some report and
they forget to tell me filters so I
think the best the worst example I saw
was the one report which took about 10
gigabyte of data in memory just for the
data set and you can imagine how fast it
was to to print this report in order to
fix this one also the new feature coming
so we introduced a new time out pitch on
the report so you own the request page
you will be will be able to set a
timeout and by default it will be
probably small maybe 5-10 minutes to be
decided in the future but if you know if
you know that your epic need to be run
longer you will be able to change it on
the request page and schedule it or you
print it immediately but be aware that
you may affect performance all other
customers if you running really want
Reapers another good indicator is on a
Fiat record again on the worst case I so
it was about a minute to execute this
event and for us it's typically
indication that you have some extensions
which is doing not good things and we
should affect customer performance and
of course we're looking on in general on
the some application scenarios on open
form open page time and the till car
color here showing we call it waste time
this is a time this time is visible if
it's above threshold or our UX team give
us some guidelines that the page speed
to building open less than to 300
milliseconds and if we doing it longer
it will be shown in this report and then
we need to optimize you can see here
that the dialogue is the worst page here
but actually it's not true in this case
it's just waiting for the user input or
user waiting while user press ok or
cancel and it's shown it this time but
it's not so bad so internally when we
talk about telemetry okay so it's very
simple we use an old very well-known egw
and when you run on premise you can see
the same telemetry yourself of course on
our scale when we have hundreds of
thousands of clusters with thousands of
machine it's not really working like
this so we have our internal tooling and
this is example of a tool called Kusa
Explorer that's our internal tool it's
not available publicly and just show an
example I did a very simple query for
one just random tenant for the just a
means Federation's and I don't know if
you can see it here right but it's
pretty big number so for the ten minutes
there are more than 70 thousand records
in the outer limit ship for one tenant
so it's enormous amount of data we're
capturing and actually our goal in near
future the report I show you it's a lot
of data but unfortunately it's not
available for you directly so in some
cases we can send this information to
you but it's very specific cases where
you have like really bad escalations
need to be tracked through our support
team but I'll go for the next year that
we'll be able to give all this
information for you so you'll be able to
build these kind of papers from from our
partner telemetry and as Vincent show
today you know we're starting this
process so we given some telemetry now
for you in the up inside and I will show
very quick demo how are you going to set
up and how up inside image looks like
so let me go to my machine and while you
do that I can just mention that for
instance when we get a user report that
user says when they do something and it
shows an error in their UI you know you
cannot bla or you have to plow then we
can actually go into cousteau the query
that you just saw we can search for that
specific thing and then we can see the
error message and we can see the the
call stank you know this was called from
page something that called coding at
this and table that so for us it's a
fantastic tool to actually pinpoint
talks or user errors okay so let's go
back to telemetry the first thing you
need to do is actually need to create
your own up inside service or resource
and I created one before presentation
called math tech days and if you go
there on the overview page you can see a
field called instrumentation key you
cannot see no it's now you can see the
game and if you need to copy this key
and then if you go to your admin Center
for your tenant and you choose your
environment you want to set up this key
for I have only one environment called
production if I go to the environment
there is a new button called application
inside key so when I press it actually I
already enable it but you need to enable
it you need to put this key you just
copied and you save it just be aware
that this separation will do we start
off your tenant so it can cause some
downtime for a custom so don't do it on
the live system and don't do it even
business hours so I will not save it but
that's the way to set it up so and it's
done oh that's it so when you run the
operations or run your tenant it start
getting the telemetry in the up inside
and the way to see it again it's very
simple so you go to up inside you find
the locum oolitic and on the left side
see they also have this nice feature
called ghosting
so you see all the tables here and we
are right on out here meter to trace
this table so if you go and let's try
some very simple query so we'll go to
see all the telemetry for the last five
days
and let's run it okay so you can see
that Business Center is very fast so I
have only one performance message here
saying that one action was took longer
than expected and if you expand it you
can see if you go to custom dimensions
you can see the actual object ID you can
see object name and there was a page
sales quotes took longer you can see L
call stack so you can see exactly where
it happened and the most important part
here you can see actual cycle statement
and it's not very convenient here to
analyze button you can copy it and you
can see why it's potentially was slow
and I I will show few examples why
queries can be slow so that's very
simple and for now let me get back to
presentation this is back up slides if
it doesn't work so for now we are
showing only long-running sequel
statements here but there are few coming
in the future
few more so first of all of course which
will show some errors will definitely
show report execution time and page load
time and maybe something else so there
are different teams now adding new
telemetry which will be released very
soon and what I would like to ask you is
like let us know what you would like to
see in this telemetry from us and go
here and maybe add your request and vote
for existing requests so we can add
limit or in the future we will share the
slides so you can you can see it later
the link so now you take a picture now
let's talk about profiling and let's
let's see some examples why why actually
queries can be slow so first of all I
want to mention that when you write when
we are running business central in the
cloud it's exactly the same binary of
honesty as you can get on premise so
whenever you think about some
performance scenario you want to test it
will be nice if you will start first on
your developer machine
your own setup you run all the favorite
profiling tools and performing tools and
I will show you just fuel them very
quick demo so first of all just remember
that is old my secret profiler is still
your friend and this is the first quiz
here so I run profiling on the test
which hammock will show today and
actually I found a bucket now all of you
experienced developers probably see the
back here immediately
so the first one who rises Haman show to
me I'll get a special prize I'll give
you a few minutes to see like no nobody
ok I'm just kidding but actually there
is a bug it was a very severe buck I
found when I was preparing for this
presentation actually it's all bad so
shame on us and it was for pretty long
time apparently you know when we run our
code in MeV it's running different
isolation mode different transactions
levels so we run read transactions write
update transactions update a lot
transactions and so on and what it means
when we run execute queries who add a
special hints to the queries like read
with with read uncommitted or is with
update lock and so on and apparently we
never add this hint for extension tables
in some scenarios not always but in some
status it was never added and that can
cause really heavy excessive looking on
your system and we saw a few production
scenarios when it happened now we know
why and like likely it's fixed now and
it's deployed this week to the
production and you'll get it to the next
see you on premise and it's a good thing
now let's see one lifetime I'll show you
my favorite way of profiling application
I think you saw this tool before but I
don't think anybody at least on this
confident show it this way
let me show this tool called blood trace
I think all of you know it
and my personal favorite waived up
profiling it is you use Timeline
profiler just beware so if with you want
to do timeline profiling don't attach to
a running process but just let's start
let's just profile a local application
you'll get much more data if you do it
this way and not attach to run
application so if you choose timeline
profiler and we here you just find your
local you should see here sorry so it
should be Windows service and it should
be Microsoft Dynamics business central
so let me run it
so when we do it this way the server
will be restarted apparently so
it can be slow but maybe I want to waste
the time in this one this is my machine
is not really performing now ok let me
just show you the result of my previous
profiling so the profiling is very
simple right I just run one unit test
doing and recall the profile actually
the actual test Hellenic would explain
what it what it is doing but let's see
on the result so when you're done with
this timeline profiling you'll see this
picture and the middle section showing
you all this all threads which are
working on the image still at the same
time you can see all timings here and
you can see small charts like this
showing that this thread actually was
very active and doing something but
let's focus on sequel operations so
likely this tool can show you all sequel
queries executed during this profiling
time it's not very nice we know but you
can expand it and let's make it bigger
so the the cool thing about that it's
showing you the time execution time for
this query and you can probably see some
problems or you can see some statements
we should not be executed at all during
your profile or let's so I'll show you a
few examples so one of them let's see
what happens here with integration
records yes so you can see that there
are two queries doing something with
integration resolution total takes for
about a second these two queries and
this is a like thing which we can
approve now because with a new feature
called system IDs this scenario would
run in much faster and we do it we
already did it for few scenarios whose
integration records you will see
performance improvements here but what I
want you to focus on is is easily a mode
for your queries so let's see for
example what is running with update logs
CZK yeah it's very slow
a lot of queries but for example this
query right if you can not see but this
query doing some aggregations and does
it really need to be with update log
probably not and this query was running
for 200 milliseconds and that means that
all the records which get to this query
which was a aggregated was locked and
nobody will be able to see them in the
product so this get gives a really bad
user experience for the customers if you
have a lot of locks like this so when
you do profiling go and check that all
your statements have a proper insulation
mode and sometimes maybe you to commit
before or do operation in different
transaction just to avoid the locking
and maybe we should add that that's
something we actually debating
internally whether we should continue so
I guess you have tried this yourself you
do a lock table on some record you start
working on it then you call some other
function you know in another code unit
that does a fine door count or something
on that same table and everything is
locked and everything you touch or count
is locked
is that desirable I mean I would say no
but I mean should we disable this
locking of everything you touch
after you issued at a block or and
should we only keep it to that
specific record instance you actually
defined it on you know customer dot lock
table I mean please go to ideas and say
this because when we suggest this
internally you know people say oh but
that will break scenarios maybe maybe
not so just something to consider on but
it's not in the works now it's just
something we're debating because we see
these locks so yeah but just my message
my message here is just go and check
your sequel statements just see what you
execute and see that they have probably
isolation levels
and of course the second thing is the
application performance I think this
tool is also great for look into the
application performance because on here
on the right you can see all the methods
which are executed you can see the total
time you can see what they're doing or
you can also see all the memory
allocated and so on and I just I will
show you a few tricks how to make it
better because right now it's a lot of
outside noise and there are all the
function we should don't care about so
there is a magic button here very small
saying like show me only system or only
user methods not system a bit and you
can see middle there are they're all
code units all records execute here plus
some of them which are still considered
to be noise like windows service but you
can easily exclude them so if you right
click and say mark them as a system they
will disappear so you can do it for all
like types and methods which are not
interested in and then you get all your
actually your code you miss your tests
and I can probably see my test here what
it was doing this one that's that the
tests I run the tests open sales order
form you can click on it even you can
say I want to merge all occurrences and
then you on the left you see all
information is updated you can see all
sequel statement which was executed by
this specific test you can see all
memory allocated you can see how much
time is spent on the JIT compilation and
how much time is spent on the weights I
think it's very powerful tool and I'll
encourage you to start using this this
way
maybe the last night it's also remember
that of the query story is very powerful
feature and also encourage you to use it
so this is the actual query I used last
week to find very bad performance issues
with for one customer and this query is
shown you actually sort like top 50
queries which experience locks and the
total total time this query was waiting
on the logs and you can copy it you can
use it and we have a plan to add these
capabilities to the product itself so
maybe we're debating how it's going to
be looks but maybe we will put it to
telemetry or maybe to admin Center
you'll able to click and see all slow
queries for this specific tenant but for
now yeah you can just use it on premise
or wait until shown interest thank you
so as park she mentioned this morning at
the keynote we've invested a bit in
trying to write some lightweight
easy-to-use performance request and says
that's important to save the questions
as because that's basically the primary
focus so what I'll be showing here is
just how you can get up and running with
this vs code using a heart box darker
image we're gonna look at a couple of
demos and how you can use the data and
then finally I'm just gonna give you
sort of a quick preview of a more sort
of user friendly tool that we've built
for this so why do we want to use these
performance regression tests it's it's
basically because we want to make sure
as complexity grows as scenarios expand
as for instance platform change this
might also affect the application so
it's it's it's important for us to to be
aware of so the sort of the snippet I
pasted in at the bottom here kind of
shows our current lap this goes on for
every build as as partial also mentioned
and as you can see the numbers are
fairly high so how do we interpret this
this is all automated today so today if
you as a developer somewhere introduce a
regression we will find it we will find
the check in and we'll send you an email
with instructions on how you can go
about it and that's that's basically how
it works but this if you want to just
jump in you can quickly get the overview
so that that's basically how we're using
it but so what is it actually that we do
so as has been mentioned a couple of
times we basically count the statements
execute it and we do the row reads so
here I I took a snippet from code unit
80 and they execute that the the
statement is basically now that I filter
on the under sales order we basically go
through all the sales lines and we do
the reads and that's that's basically
what we're interested in and the reason
for that is obviously as we if we kind
of increase in statements there could be
something that we we need to look into
which is important as bad or mentioned
to begin with there is a latency
introduced as well so that's why it's
it's even more important to keep track
of these so I will not introduced it's
just there it's also there on-prem out
saying yeah
yes but in in the cloud we have that
extra millisecond as well or what's that
also we also have that on depends on how
far you place your machines or not that
physical distance so much but as how
many routers and stuff you have in
between yeah good okay so I just want to
show you
my small sample here so basically this
is just a VM it's at Agra in a sure it's
a tall image running in the show so it's
out of the box I installed the test
toolkit and now I'm able to create this
so my test object in this case is to
sales order list and as you can see I'm
instantiating a number of variables and
that's basically because what I'm
interested in is from the point in time
where my test
basically starts which is to say this
over loading the sales order list and
then until it finishes and if I just
counted it afterwards I would get
everything up until that point so that's
why I'm staying in instantiating these
variables so inside the test it's it's
it's kind of pretty straightforward
I always use the latest version and
that's to ensure I don't have any
caching which would confuse it and here
you can see I'm kind of setting up and
so this point give me the account from
the session information object then I go
ahead and I simply open up the the sales
order list I then do another read from
the session information object I close
the page and then I finally to sort of
the tails here and I put in a break
point at the end of it and that's just
to be able to show the results because
this one I didn't create any kind of UI
so just go ahead and do an f5 here
fingers crossed
login didn't mean that yeah so maybe
I'll go and fetch my first units this
one about true for the list and just run
it and hopefully I won't break which I
did and so now you can see that I have a
total of 187 row reads and I have
executed 85 see who statements so as you
will note also if you have tried this
but you can also go into your variables
when you're debugging and here you will
basically be able to see sort of what
Alex and I also showed in the profiler
you can basically go in here and you can
see the statement that we're firing
stand out this is only set up for I
think it's ten statements but you can
set it up to basically show you
everything okay so now let's let's jump
into maybe a slightly more this was
actually the test that flashed out that
buck you you mentioned Alexander so it's
sort of in the same category but I'm
just what I'm doing now is I'm actually
trying to create more of an average and
we use averages because we don't we're
not interested in maybe one spike we're
more interested in in posting a lot or
doing a lot of operations to be able to
to measure these in a more accurate way
you can see that there will always be
deviations and the reason for those
deviations is that because basically
it's it's it's code it's supposed to be
the exact same thing but in the whole
stack there are elements that we do not
control and that means that could be
caching kicking in there could be other
aspects of of the
full-stack that will just influence the
results so they will differ a bit but
I'll come back to that anyway let's jump
back into this one
so same setup as the last time this time
I'm setting up this variable where I say
well let's do 10 sales orders you can
see I have a small loop here that then
goes in and creates a new header puts in
some lines and then I basically do the
same thing where I'm counting things and
then I put in this little assert down
here but that's just mainly just to show
us the results at the end so this time I
will just go ahead and do a control f5
you know
and I'll just go and fix that one there
you go so we have this new one I'm just
gonna run the selected one and so that's
not a you could say a big deal right I
mean we just saw how that worked but
what I'm gonna do now is I'm gonna
introduce another extension in the mix
and I'm sure it's not that fancy this
extension that I've created here but I
call it a best-seller extension so
whenever somebody buys more than ten of
even item could coincidentally be the
one that I'm selling the bicycle it will
add a comment on the record on the
customer just to let me know that this
costume was is buying a lot so let's
just go ahead and deploy that one so
this is where I think it kind of what
I'm trying to demo here is basically
that as time pass and more complexities
at it you have more extensions maybe in
in a live environment in a live
production environment it will
definitely influence the number of
statements you make hence latency other
issues could occur so here we are here's
the extension I I will spare you the
suffering of seeing if it works so we
just have to trust me so I'm just
highlighting this so we can click ah
that's a little difficult to see but I
think I can give you the numbers here so
we had a 1587 recount and we had
eighteen hundred and sixty-one
statements so let's just try and run it
again now with my extension in the mix
and we'll see a small increase so this
time I'm at nineteen hundred and sixty
eight and and 1862 so so basically it's
pumped up with with some some more
statements and and that's just to kind
of make the point I mean you see are we
still running over okay yeah so we went
through that we introduced a new
functionality and what I make them
basically pose a risk NS pyro mention
you know one statement three
milliseconds or a thousand statements is
basically three seconds and we just saw
how much I added by with this simple
relatively simple setup so at that a
very very popular regression is to
subscribe to unmodified of a table
because if you somewhere have you know
and modify all which is one sequel
statement that is turned into a loop if
you subscribe to the unmodified event
because we need to call event for each
record right so that's a very easy and
popular way to make regressions yeah
good point so I'll just try and demo
this back so I have two VMs going here
so let's just see hopefully we can get
away with just a simple refresh we
happen to ship this yet we're working on
that we just need to work through some
details there are still some small
tweaks we want to do but as you can see
it's basically the same test runner as
we just looked at but this one has more
you can basically get the metrics you're
looking for right right here so here we
already created a bunch of tests the
first thing I want to just show you is
the baseline version which is another
smart thing so I run my first test call
it my baseline the 16 ov in this case
and now I'm starting to add
and you can imagine I do this during my
development and as you can see the
different metrics have changed sometimes
there's a regression introduced now
these would typically be what I refer to
just a little while ago about we don't
control the full stack this would
typically not be a full regression
because I'm actually running on the
exact same bits so without further ado
I'm just gonna rerun the selected ones
so my baseline is 16 point or Oh - and
now you can see when I rerun the exact
same test I actually have some some
small regressions and this is why we
care about averages this is why we try
to basically build up more a large-scale
test when we do this so we run it again
and you can see it kind of varies a bit
and then I can go in and save these runs
we could call this one 1603 for instance
and so another thing related to this
which is also I think it's it's just two
very lightweight demo of how you can use
this but we could go in and basically
take a look at all our test runs and
then we could go into an O and open it
in Excel and this would be sort of like
the the diagrams I've we've shown you
this morning about the reporting we do
this is it comes from power bi but
that's all stems from a database where
we basically load in the results I'm
just gonna quickly do an enable editing
inserted into a pillow yes please I'm
gonna do the version I'm gonna do my
test name the rows and the statements
that you tuned it that's that and then
I'm gonna do a pivot chart I'm gonna do
the column diagram and this is just to
show you how visually you can compare
this
and it's it's a nice way for to report
out maybe to other stakeholders or other
engineers about how the current
performance is doing yeah so as I
mentioned it is not released yet so
we're still working on that my clicker
here so basically when you export it to
excel as I mentioned there are a couple
of benefits from this I took roughly
sort of you maybe already saw this as
part of the keynote we have the timer
test as well going but it fluctuates a
lot it's it's very difficult to go in
and say okay we probably have a
regression we can see there's a trend
but we don't really know with the with
the counting the sequel statements at
least who to us it's it's more stable to
read from and it's also more agile in
the sense that I can rerun the US as
many times as I want to
while I'm developing my code I don't
need to wait for a full build put it
into a lab and wait for the all these
timers and all this test to kick off
this one is lightweight yeah so just a
couple of resources around setting up at
general testing we haven't really I
don't think so at least I haven't seen
any documentation about doing these type
of performance testing but we will
provide information and with that I
think I want to pass it on to you yep so
this section would be quick because
first of all each of the topics I used
to speak about but also most of it
wasn't shown in the keynote anyway so so
we have a new features and we're only
showing the ones that have to do or
somehow are related to performance so
one is the new cell number sequence and
I guess you all attended the keynote so
I just point out that
you can create and number sequence with
the sequence name starting number and so
on and you can get an X and you get the
current and this code is from the number
series code number series functionality
and there's not no mystery about this
because this shows up in sequel as well
you can see under programmability
sequences and you can see them I think
it's important that you can enable to me
your life system right on existing
customers you can enable these number
sequences
yeah that's coming yes exactly
thank you just to mention the there's
nothing mysterious about these number
sequences but it's something you can use
for anything basically I mean if you
need any kind of integer counter you can
use it and Vincent mentioned that you
may not be guaranteed that the numbers
are sequential the you are they are
actually sequential it's just that if
you are in a transaction you take a
number and then an error occurs and the
transaction rules bank then the number
is obviously not a rollback you already
you already know this feature from or
this concept from auto increment in
tables you have if you have an ID so we
introduced this in in the number series
actually the feature was made for number
series because we had a lot of
complaints about locking and those of
you who work with number series would
know that when you take a new number in
a number series we read the number
series line record the active one and
then we increment the last used number
and we stamp in the date right so what
we introduced was this allow gaps in
numbers to make it very clear that it
has a cost you could also have called it
enable sequential numbers or something
but that wouldn't that would hide
the danger of it so and turn it you can
turn it on and off as you want because
the only thing in that is that there's a
hidden field that holds a name of the
sequence and either you turn it on or
off will update that number or these but
you also can see is that I won't put the
laser in your light in your eyes we
cleared the last date because we can't
keep that date up to date without
modifying the line right and then kind
of pointless which also means that there
is some feature of some certain number
series that I can't remember but one of
them says guaranteed date sequence or
something like that that's obviously not
possible but for anywhere where you
don't need this to actually sequence and
I'll repeat it again do not use this for
posted invoices and so stuff like that
you can use it for customer numbers I
mean you can create a customer and
delete it that's no different from using
this number since the other thing was
page background tasks so this is just
one of the many examples we have you
know the activities queue in both
centers you have fact boxes we can
basically use it anywhere we want this
is how it looks like this is the
specifically one of the queues but
Vincent explained it better at the
keynote which was sort but the main
point is you in queue a background task
and then you either wait for it to fail
or to complete and then you can exchange
the result using dictionaries and you're
not allowed to do any writing in there
which is inconvenient I know but we
impose that
in order to avoid people sending
something off in the background which
doesn't update your foreground right so
people would get is you know another use
has modified this record and you would
get that even if you're the only person
on the system also we are contemplating
is it's not planned as such we are
discussing or debating whether to
actually make this more general thing so
we inside regular al code can spawn off
sub processes but that's not even on the
white portent then there's the session
information object that you just talked
about in the mode where you can get the
numbers again this is enough has nothing
to do with performance as such but
allows us to measure and last thing is
immutable keys and again nothing
mysterious we add a system ID field or
dollar system ID field to every table we
can use it and even in in fact boxes
right if you have ever tried to do
anything generic you would have you
would have liked to use record ID right
now we have it kind of
and then also the Reid scale out so
remember those data mirror databases
that just sit there and do nothing so we
want to utilize them obviously and
sequel also on Prem by the way allows
you to do this so you when you make a
call or a connection to sequel you will
actually get to a gateway or gate will
ring and what you can do there is you
can say what what is my intent right I
intend to read only I attend to update
and then that gateway will decide
whether to point you to the primary
machine or one of the secondary there
are a lot of secondaries here you can
see we used to but this also works even
if you don't have the mirrors then the
gate will say Gateway will say oh there
is only primary and then it will route
it to the primary yeah this is basis
theme and we are again we're debating
where to use it because background as a
web service requests the API peaches are
an obvious thing to use it reports as
well queries obviously but also we are
debating lists so some of the very
expensive queries you see is a user in a
customer list or item list there's a lot
of you know outer joins with sums and
whatnot and then they do filtering and
sorting since you are not updating the
data in a list
why not route it to a mirror and this is
how it will look maybe this is just a
newer prototype so now it's not called
read-only as Vincent showed us but now
now the name is called data access
intent because that is more in line with
what it's called in Azure or in HS equal
and then we have a short session here
and about coding for performance and
I'll take a simple example of how you
can minimize number of sequel statements
when writing a report I will tell you
which you already know that you can
schedule some things in the background
tasks so I'm not even going to demo then
and also talked very briefly about
scale-out because if there's any promise
that the cloud is or a show is about
it's about scaling out or parallelizing
I can I see that when you have 50
minutes left so I have taken one of the
very simple reports report for the
detail of trial balance and I've
stripped away all the fields and stuff
so you can see that we have the GL
account that links to kill entry and you
might think how many queries are here
right well there are as many queries as
there GL accounts plus one right because
for every GL account we issue a new
query to really kill entry and think of
another scenario because usually you
only have a couple of hundred Kiel
accounts but if you have items for
instance where you can have thousands
and thousands and then you might have
item - entry there and maybe even have
editor entries below try to imagine how
many secrets you actually be firing
against the server we're talking with
the server guys - whether they could do
this smarter but at least you and I can
do it a bit smarter by the way it's not
only those two we also have a couch some
down there right help field and for
every cheer account we apparently need
to figure out whether it's the dealer
entry there and also we do all this date
thing so the date I didn't take the
dates count the date here because the
date is a virtual table it doesn't count
as
sequence statement but actually most of
this could be done on free record or
free data item correct yeah so we have a
lot of queries and how could we improve
this so we could rewrite the report user
query and then adapt the data items you
know you can change the data item to be
an integer and then you can add the
fields to that integer and you can then
we would need to adapt the allele see
the layout to the new structure and we
all love to edit in our TLC right or a
more lazy approach that are trying is to
declare one global GL entry record and
so we select to a fine set on GL entry
and then we change the current g-line
traitor item to be a temp table and then
we'll basically fill in the temp data
item as we go I mean as the GL accounts
proceed and if we care about it to
others you know the calcium and the date
thing then we can do that so this is how
the layout would be modified the only
thing we actually change here is that we
on the GL entry set use temp true does
the only change the layout everything
else works and as I said with the date
thing we could just as well do that on
pre data item or somewhere else and what
we do there is we have this global GL
account that covers the filters and then
we take this date filter and use auto
calculated a fine set right so
now when we start the execution of the
report the sheet account data item and
this are in sync
otherwise we need to bring them in sync
and we remember that we do this right
because otherwise we need to ask every
time yeah so this is the modified
Reapers they're more code here in enough
to get records but it's not as bad as it
looks
so most of this is to do the copy
filters from the records down to the new
but if you take a closer look at the
first thing we basically make sure that
the starting balance global account
isn't sync and then we take it from the
auto Cal Cal kit field right and then we
do all this copy filtering thing and
then we start the global chill entry
fine set I mean the first time otherwise
we empty it because now we're ready for
the next loop and down here we first say
okay I haven't found any entry yet and
[Music]
while I'm pointing to the same account
then I copy into the temp table and
since I apparently I'm here then I know
I found one because then I can use it
down here right instead of doing that
extra find set or find first and then
basically I only fill in the temp and
then I let go and then the report will
handle the rest and we try it if my
client is still active sorry I
the tail I'll I should take classes on
ballast so this is the regular one this
is that one I could run it here but
it'll just produce the same so there's
no fun in that
so what I did instead is to create a
single page where I can call them and
then I do the sequel count thing that
Henrique showed right and I can draw if
you need to access your presentation
move because ah you're not seeing it
thank you it was
I'll just do it like this anyways to
make it to be able to compare I just
create this small function that will run
the two reports modally from within this
function and then I'll count the sequel
statements before and after as Henrik
showed you and in order to not be
accused of of benefiting from cashing or
anything I'm running the new report the
v2 report first
so just take everything and I will take
this date range from I think this is two
years and I will send this to
I don't excrete it but it's a it used 20
statements 26 agents and this is the
regular one same parameters kind of
difficult to operate a laptop 225 and
that that's only because this data said
this is the small Kronos demo data that
it only has a few accounts if you use
the slightly bigger one the one who
called extended or whatever it's about
500 statements so I will so the timing
is basically the same if I can also run
them the timing because when it's only a
couple of hundred you I mean the
difference vanishes into you know
seconds or milliseconds but again think
of this being items and item the changes
in value entries entry structure didn't
matter I mean yeah we did
so the 597 that's with the the extent to
demo and 18 that's what I got last time
I ran it so now it was 20 apparently
some metadata was there the other thing
is scaling out so I don't have any
concrete examples but when you have
something if you do something with a lot
of items I know it just cost it's a bad
example but something that will process
all customers or items see if you can
split them into chunks and yeah sorry
yeah scale out and then get get together
again at the end so we did this with we
already this already released a year ago
so maybe
already seen the code here so when you
import a rapidstar package which is
basically a zipped XML file in there we
get all the table notes which you know
in XML each note represent the table
with its metadata and all the entries
and then for each note we take this note
and depending on different things we
will import the data from XML or as we
introduced in certain cases we say if
not in cell mode or there are very few
that then will do directly otherwise
we'll send it to a background session
back there I mean the code is that you
don't need to copy this and then that
will send the blob to a background
session and it will import and at the
end you know that corresponds to that
one we will wait for all to finish again
it the code has been out there for a
year or so and it is better yeah I mean
on a slow very slow trial machine it
used to take what you what used to take
twenty minutes now runs in ten minutes
yeah I think that concludes our session
so any questions we have six six minutes
left actually an hour and six if we skip
lunch deep end of this there is the Q
yeah we have teachers we have t-shirts
but yeah we just ask questions best
questions yeah or the questions but
maybe first question
you can throw it back well I would have
two questions first one is could you
compare the performance impact of Ward
and our dear C layout but also with
custom layers yeah so so if if you take
no I will step one step back actually
first so in statistics we have been able
to see that when you run a report on
average approximately 80% of time is
actually spent collecting data and then
the last 20% rendering the data so we're
only so what you're asking about is the
last 20% and when we test it word
reporting way back it seemed that it was
at least as fast as our TLC I mean you
can if you just look at word as such
then you can render a several hundred
page Word document within a second or
two so I think that part of the
difference is negligible what we then
you asked about custom layouts so again
that's two answers one is you know you
create a layout for report that
shouldn't change anything because
actually fetching the layout whether we
fetch our own or the one you create it
doesn't matter that's the same the other
part is we introduced some time ago that
you can for certain reports like cost
for invoices and such statement
statements you can specify a customer
specific layout is that what you're
asking
no yeah because that's a different thing
that's customer specific and not custom
you know the customer specific in order
to make that work
we need to create one report per
customer to make this work and that's
obviously a lot more expensive so
instead of running you know making one
report for ten or a hundred or a
thousand customers now we not need to
create you know ten or a hundred or a
thousand individual reports this each
their own layout so then that has that
one has a huge performance support
impact the second question is about you
mentioned on modify and subscribing to
it yes and it's a huge performance it is
yeah I mean compared to a modify all
right because it completely breaks the
modifier introduced when the invents
database events were introduced in
business in yes but an event which
triggers only met modify modify trigger
it because currently we have a
subscriber parameter well modify true so
that it triggers only when it needs to
because I think in this case you're
having the impact performance impact
even though we you don't want to run
agree and that has been debated even
before this was ever released and and I
think it ended as it did because we want
to be sure they say that you create your
own take a new table when you create an
exchange not not the modern exchange
table but another table that you want to
be in sync with some other table then
you subscribe to the unmodified insert
and delete that specific record and if
you do that which you would then want to
rely on every developer and every
extension developer ever to remember to
write modify true that's basically the
discussion
but I agree it would be nice if we could
unsubscribe that one but for whom the
developer forgets it or I mean the point
is do you want to be absolutely sure
that your table isn't sink with some
other regardless about regardless of who
writes the code that's the only one use
case you're mentioning no synchronizing
I mean other stuff that I want to do
anyways that's the discussion that
happened back then Thanks
there was a two good questions I think
that warrants a good teacher
oh they're two questions even
subscribers wouldn't it be possible to
be supplying the rent trigger sorry you
said you're supplying the rent trigger
right in the events best description
yeah
so what if you will say okay if this
event triggers not used then skip all
code in even subscribe and then also
before modify all do not not do it at
all I think we do I mean you wouldn't
subscribe to it if there is no
description you get record if not run
triggered and exit but if you have to
but that's code yeah but if it will be
triggered also with more of a bit small
affair all yes and it's not possible to
just get better
nope again it's the same discussion then
your other table that is relying on this
table will be out of date or out of
synch I mean
so the the short thing is the don't
subscribe to unmask finalists we need to
and there is an option that it's
difficult to use maybe we or the
platform guys should make it easier to
manually subscribe to two events so it
can be turned off on and off as needed I
think there was yeah I think you need to
give those t-shirts up because nobody
wants them right or we don't have time
to throw more questions on the back
there was oh thank you for a session
first of all I had a question regarding
page list and we historically had it
scenarios where customer wants to have
no KPIs on a list which potentially
means that we need to have a more
fulfilled displayed and this is directly
impacting the performance are you guys
looking to have some sort of use case
where we can use background tasks to all
these four fields yeah as like are the
the flow fields yes then you need to
code it yourself
I mean you on the actual line you have
fluids or you talked about black boxes
no yeah that's difficult one
actually I think the short answer is no
I mean we are aware of the problem
because we already have it because many
of the lists like customer and items
have so many flow fields already so what
we are debating is to getting back to if
you if anyone of you are old enough to
remember the old sea side if you have if
you hit column make it non visible then
it wouldn't be calculated yes in the 3d
structure is not that's not a trivial
thing because
what happens on the client is not
necessarily known to the server so
currently the server gives everything to
declined but we should have a way to
undo it I mean not calculate it's not
needed yeah that's not exactly what
you're asking but I know that but it
would be kind of good if there will be
some kind of property where we can infer
that this particular equation can be
done kind of cheap do the background
session and it will be here the same as
you can I calculate it afterwards yeah
and we could we could do that but
there's another thing that another
property of the back page background
tasks which is also by the by the design
by the way and which we forgotten to
mention is that imagine you have a list
and effect box and when you get to the
on affricate record or current record on
the list you start up and you know the
fact box gets activated then we start a
paid page background task that will
eventually update it if the user then in
between jumps to the next line then this
is useless right so we actually
automatically cancel the task if the
user moves we cancel the task but that
also means that we cannot use it for
what you're asking okay yet or you can
do it on this if you have a header lines
then you maybe can do it on the header
because that doesn't change and then but
then it becomes pretty I would say
involved maybe maybe it's not worth
doing it should consider a case where
you create a new table which always keep
the ice and it go crazy I'm not in
demand jobs yeah that is true I mean you
can you should definitely look at having
some kind of caching mechanism I mean
store and store the values especially if
they don't change off we did we have
done that ourselves on many of our role
centers you know these parts some of
these numbers rarely change like 10 cows
I mean it probably doesn't change
between you cell do some processing and
you're returning back to the role center
right so a lot of these we store and
table somewhere cash it and then we have
some time stamp that says when was this
last update and then you can say okay if
it's a day old then we will make a new
calculation yeah and thank you for
answer and I have another question
regarding this system ID is it where can
we write our own system ID no again a
long debate that you can insert you
cannot update it but you can insert it
you can you can can you assign it as
insert time yes yeah even that has been
debated I was saying in length but once
it's there it's stable that's why also
in the charcoal that immutable meaning
even if you change primary key anything
it stays the same you can delete the
record increasing you want let me go get
a new one and you just an insert we can
create our we can insert our own system
ID would it be applicable for API pages
if I can do the post request with that
iíd predefined yeah why not I mean often
the reference comes from some other
system but the other part though I would
say is we need to ensure uniqueness
that's one thing the other part is we
it's good we are using but we are
indexing it as well and it's actually
expensive to index goods
it's a sequential good and that's why we
are thank you that's why we're using
what what's called sequential goods
they're not real goods they are goods
but they are sequential so they have a
you know beginning and then they grow
over time just like and
entry number hood meaning that
maintaining the index becomes faster
thank you
is that yeah but this last t-shirt I
think these guys on the front rolls had
a question thank you
oh sorry could we get okay there was
also one no I think you also have a
question right yes yeah um regarding the
system ID yeah if I have a record I can
read the system ID and get the record by
using that system ID is about these
functions not available we're using
record references is that correct the
record ref has a function to get a field
ID off a system ID so I could unity here
graph
well you with a system ID field ID and
then get to record but no no yeah yes
but the record ID also has a system ID
field we really want to make this a
system ID not a regular feed like
anything else yes is stored in the
sequel obviously what we want this to be
accessed differently so I can't if I
have a record reference I can't get
system ID of a record start inverted
record reference as a variable type
record reference
yeah well no you need I mean you need to
know which table it is first time yes
yeah so you need to know the table and
then you can do a record draft dot
whatever the command is get from system
I can't remember but you can get it by
system ID but but it's not like it can
index your way over the fields and say
feels Number 17 or whatever its system
ID okay it is a system ID thank you I
think yeah I think this gentleman on the
front has been we were waving his hand
for a long time probably also is the
last question yeah that's also last
question I guess never this
oh yeah so many of us will be around the
booth with or without a beer in our hand
right yes is there plans to provide the
ability to assign the service tier that
a tasks schedule is running under not in
that meant well or you can really do it
on premise right y can assign something
to a task schedule but I want to have
that task run under a specific service
here well we're loading
no I mean you can you can say that
certain service tears do not cannot run
background tasks yes and others can
right in that sense it will be routed
yeah but you cannot take all the
category code which we lost correct yeah
thank you the job queue thing yeah I'm
it's one of my babies I'm willing to
maybe you should have a talk over right
because there are many reasons in
annasher we move around machine so we
can't we have no way of knowing whether
this machine we're running right now
it's the same as we're running tomorrow
yeah I mean they get reprovision and
moved around all the time all the time
but yeah yeah so when we change it from
the old job queue functionality to the
user new task scheduler thing we lost
that capability including the
prioritization and and handling of
categories that still sucks a bit I have
to admit but I'm maybe you could talk it
there because we would like to get some
input what we can do okay
thank you thanks thank you yeah thank
you
[Applause]
