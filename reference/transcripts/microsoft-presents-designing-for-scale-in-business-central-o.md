# Microsoft Presents: Designing for scale in Business Central online

- **Source:** https://www.youtube.com/watch?v=r48KmhfJ_FQ
- **Video ID:** r48KmhfJ_FQ
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 89m49s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

thank you everyone for coming uh to this
session that's signing for scale in
business Central online my name is
Christian I have Raina and Maria with me
um I want to start with a small history
of business Central online so if you
started in April 2016 back then it was
called project Madera and it was the
first sess version of nav two years
later we renamed it to business Central
online sorry some problems with there
two years later I'll just talk two years
later we renamed it to business Central
online and even after two years of
development it was still a pretty
immature service in many ways we didn't
have any autoscaling of VM
capacity very primitive low balancing no
autoscaling of database so sometimes
customers ran into problems but back
then only small customers did go to
business Central online now fast forward
six years to now I would say we have
very mature service we have advanced
algorithms in many places including Auto
scale of VMS and database and advanced
load balancing we'll talk about that we
also have more relaxed limits we accept
more load coming in to the service we'll
also talk about that and finally we also
see the results that more and more
larger customers come choose to go to
Business Center Online we'll also talk
about
that the focus of this session is
business Central online so it's not the
product as such that you can run on Prim
it's more how we we run it in the
cloud so we will tell you how we
designed it to handle large
customers we will have some
recommendations for you that you can go
and apply but mainly the takeaway for
you is going to be an understanding of
how we designed our service most of the
time you shouldn't need to know these
things but once in a while you are faced
with a design problem scale problem and
hopefully it's nice to know how we
designed it so that you can maybe take
advantage of
this what we're going to start with is
talk about how we manage our
infrastructure how we ensure there's
enough capacity always and how we low
balance and for that I would like to
welcome
Raina thank you
Christian so that's a that's a bold
statement we put up there right so
Microsoft
promises unlimited infrastructure
capacity what does that mean that means
whatever load your customers bring to
business Central online we will manage
to you know scale out to handle that
load but before we you know go into
those details let's just understand what
we mean by scale and let's review our
architecture right so this is an
extremely simplistic version of of how
we run our service so you have a user
that's you know maybe signing into a web
browser and the their session then
enters our compute
tier and uh we also have a database here
um behind it so what do we mean when we
say scale right it's a very multifaceted
word it can mean multiple things it
could mean for example more users so
it's now hundreds of users and we'll
also show you some cases where it's
thousands
right um it could also be API calls so
thousands of API calls and different
characteristics you know bursty traffic
and you know sustained continuous
traffic it could also be data tenant
data so very large databases and uh some
of you I know are wondering how large is
that so stay tuned we'll tell you and it
can mean a whole bunch of other things
right so it could be more sales orders
it could be a lot of uh lines in these
sales orders more job cues paral job
cues so scale is a very different thing
for the type of workloads that we're
running and what we're saying is that we
would actually you know manage that
whatever you bring we will manage it so
let me explain you know what is our
responsibility in all of this right so
in the compute tier we will handle
scalability we will make sure there's
enough and sufficient capacity to run
the workloads right and this is in terms
of CPU in terms of memory and other
characteristics same goes for the data
too like in terms of the compute that
the database needs to have to run the
world clads we will ensure that there's
sufficient
capacity and the takeaway for you is
that Microsoft manages this
Hardware you don't need to worry about
scale you don't need to worry about load
balancing we will we will take care of
that that is the
promise and there can be bottlenecks and
what I'm going to now talk about is how
do we design to handle these bottlenecks
and what are the algorithms that we run
to manage this so let's start with the
compute TI and in general when you have
a high work like high volume workloads a
computer handles it very similarly like
how you would imagine so we run our web
server and the nstd service in a
VM and then obviously we want to you
know handle more load so we scale out we
have a lot more VMS in front of this
entire cluster of VMS we've designed a
load balancer and what this one does is
it gets an incoming session and it has
an algorithm which decides where this
session should be
directed and typically the cluster isn't
too busy right so it could look like
this where there's some CPU load and I'm
just taking CPU as an example we
actually use different thresholds to
decide how do we balance but let's keep
keep it simple and understand how it
would work with
CPU and now imagine that one of our VMS
is running at 60% over 60% CPU so that's
just a threshold that we set keep in
mind at this point nothing is really a
problem right it's not it's not a
critical level it's not the danger zone
that would be closer to 100% that's when
you know the operating system needs to
decide which threads to prioritize etc
etc so we want to keep these thresholds
you know low enough that we we try to
catch the
trends and what our load balancing
algorithm then does is it says we're not
going to send any new sessions to this
VM right so we detect that it's
potentially busy and we're not going to
overload it by sending more
sessions um one thing to remember is
that we actually don't move the sessions
to another VM so once it is running we
do not interrupt it we say Hey you know
we think that it's going to finish its
process in eventually and then things
will come back to normal and in the
meanwhile we're going to direct new
sessions to different
VMS let's look at how this actually
works and we're going to use some data
from our Telemetry we love Telemetry at
Microsoft right all our decisions are
data driven so let's look at a cluster
in the US and it has N9
VMS and uh this is about 535 um our time
European time so let's let's just see
how this behaves waves in this diagram
the illustration each bar vertical bar
represents the workload on a VM in terms
of CPU usage and on the y- AIS we've
mapped the CPU usage percentage so
typically and we're going to look at
like every minute instances of how
things go right so when you look at this
it's like it's not a lot of usage
there's some work going on and some VM
some are more busy than the other but
it's just fine there's really no
problems yet let's have a look at what
happens in the next VM oh so now two VMS
are getting some sessions and those
sessions are doing some work so the CPU
is being used still not a problem at all
this is fine this is okay but you know
we notice it in the next minute okay so
vm1 and vm2 are doing even more work um
it's approaching our magic threshold for
CPU usage again nothing to be done at
this point but let's have a look now in
the next minute what happens is vm1 has
crossed the threshold for 60% CPU and if
you remember what I showed from the
diagram with the load balancer is within
this minute our system has detected that
the CPU usage just crossed 60% for one
of the VMS vm1 and the load balancer now
identifies another VM to send new
sessions to and you can see that uh new
VM is taking this load right so again
just to remind you we don't kill any
sessions and vm1 we let them run they're
doing their work we don't want to
interrupt it but it's just new sessions
we'll go to another VM cuz we don't want
to overload this and again 60% is
absolutely not a danger zone right it's
fine like it's perfectly okay at this
point let's see what happens in the next
minute so our thesis which was that you
know vm1 the processes and the sessions
there will eventually finish what
they're doing and you can see that the
load now is going down in vm1 but the
other VMS have actually picked up load
and they've crossed this threshold and
again our load balancer kicks in and
will not send new sessions to these VMS
and directs them to the other two that
you're now seeing are picking up the
load and as this goes on eventually the
VMS the sessions on those VMS that were
busy finished doing you know the heavy
workload stuff that they were doing and
we can see these Trends uh for the busy
VMS going down and you can see the VMS
that were assigned the new load picking
up and this goes on and on and on and is
fully automated and we don't have to you
know there's no engineer who's looking
and saying hey we need to switch
configurations none of that
right now you may be asking hey this
cluster has 9 VMS and uh this is not how
the characteristics are always going to
look and that's correct you know the 9
VMS could get busy um what happens then
how does a load balancer behave well
this is when we'll queue in our next
Warrior and our next Defender which is
autoscale
and what we do is we'll scale the
cluster out right so we we get more VMS
in and to illustrate this again our very
favorite Telemetry and data we really go
into this so this is a Swedish cluster
with 24 VMS and the diagram is is
depicted exactly like the previous one
was so each vertical bar is a VM and
we're trying to capture the CPU usage on
average in a minute right um again we've
just put a little reminder of for where
our 60% threshold is and now let's see
how this behaves so so far this is okay
and this is you know around 8:00 a.m.
local time so you can imagine users are
going to come in and start logging into
the system
right um okay so some sessions that were
assigned to some VMS are picking up
they're doing some work at this point
you now know and you're hopefully
confident that the load balancer has
detected that a few of these VMS have
crossed the 60% CPU threshold so they're
going to direct new sessions to other
VMS you can also see those are picking
up some
load no problems yet this is
fine you can see on average the height
of all the bars is going up so that
means all rvms are getting a little busy
is still not enough of them that are
above our threshold and absolutely none
of these are danger zone yet
right and uh this goes on and we see
that you know it's okay and now we find
an interesting line in our Telemetry
which says at this point our balancing
algorithm says hey you
know I'm not freaking out yet but
there's a lot of busy VMS in this
cluster so let's scale out and it
immediately requests you know three VMS
or something like that so what we show
you here is the number of VMS in the app
service or cluster as we call it and at
the point at which we scale out or we
request new VMS
and now how long does it take well it it
varies but in this case right from our
Telemetry we can see that within 10
minutes we had three new VMS provisioned
and the NST has started up which is our
runtime and it's ready to take in new
sessions so this is how we scale out and
at this point again I want to remind you
that there's nothing in the danger zone
this is preemptive that we do these
things right so we know that the VMS are
busy they're doing some work and uh we
want to we seeing the trends but we want
to make sure that this cluster is not
stared so we scale
out so this was the bottleneck in the
compute here what about the database now
you know tenant databases are you know
mapped one to one so we can't add more
databases right so what do we
will uh we also ma like monitor per
metrics here as well and similar to the
VMS we look at you know CPU percentage
usage we look at data iio percentage and
we look at log IO and a few others and
depending on the insights we get from
our Telemetry we you know experiment a
bit but we have a similar algorithm
right where in an automated process
we're continuously monitoring these
metric for all of our
databases and the moment they cross a
threshold like 70% then we say hey we
need to scale up CU we can't add more
databases here so we increase the
compute here of these databases and what
that what does that mean it means that
we'll have more vours available to this
database we have more Voca threads and
better IO
characteristics and eventually because
now there's more computer available the
average uh pu metric you know reduces CU
it's it's a percentage of the total
available so this database is now in our
minds considered it's fine now there's
no there's no danger
anymore and
uh how do we decide what is the initial
capacity right because we need to pick
at the at the time an environment is
created we'd have no idea what kind of
load characteristics is going to be
there so we have algorithms that do the
initial
allocation and that's a fully automated
process again and it's based on two
factors one is whether the customer is
you know paying or a trial and the other
one is whether it's a production or a
sandbox environment so we look at our
Telemetry and we you know try to gauge
like in 90 95% of the cases trial
customers are okay with this compute and
that's the initial similar we look at
production and we go like hey 99% of our
production instances are perfectly fine
with this and you know we have the
initial uh compute that's
ready What if after the environment is
created the database is now overloaded
right let's say companies grow your
customers will get uh bigger they will
start doing more fancy things that will
take a lot more compute so what happens
if it gets overloaded again same like
the VMS we have a fully automated
process that is continuously monitoring
all our paid production
databases and it's going to make sure
that the moment any of our thresholds
that we monitor cross a certain limit
then we scale that database
up and we look at this over a period of
time and we're pretty aggressive when we
scale databases up right so our look
back windows are very short the
thresholds are not you know High they're
actually pretty low we we absolutely
want to allow customers to to run their
processes without really worrying about
these things but we also don't want to
over provision right we want to be as
efficient as we as we use our compute
resources so we do scale down but keep
in mind that we do this extremely
cautiously and very carefully so first
of all if a database has been upgraded
or scaled up we don't touch it for 45
days we're like okay you know this was
upgraded there must have been some uh
some activity going on why 45 because we
also want to not get you
know mistakenly look at end of the month
usage right so you want to include a
little bit more so for 45 days we don't
touch them and then when we do decide to
scale down we see that the per metrics
that we are monitoring would be low
enough that these databases would never
be upgraded immediately right we want to
avoid like Ping pongs so we do it super
carefully we do do it super slowly but
we do it just to make sure that we run
efficiently but scaling up that is super
aggressive the moment we see activity
the moment we see our PF metrics being
used we scale
up how does this look like an action
again our favorite Telemetry you're
going to hear this a lot this session so
uh I hope you don't mind so we look at
the the CPU usage right just for example
of one of our databases and again we've
put our 70% threshold over there and we
noticed that for some period of time
this is
sustained and uh eventually our
algorithm says hey this is not good you
know this customer's workload requires
some more so we scale up and the scale
up is almost instantaneous there's no
disruption it's fully online and there
may be like a point in time um um
connection that's broken but our service
is resilient enough to handle that so
the customer sees no disruption
whatsoever and the moment there's more
compute available to this database our
per metrics go down because now there's
more capacity available and this is from
our actual Telemetry for one of our
customers so now how good are we doing
right let's look at how many of our
databases are overloaded like the
production ones so we decided to look at
a week in April from the 1st to the 8th
and we wanted to plot how many of our
production databases have been
overloaded and for what percentage of
the time and almost all of our paid
production environments were fine you
know not more than not overloaded even
more than 1% of the time and that's
great we did notice that a few like 0.2%
were overloaded more than 1% of the time
and in this period we were actually
quite surprised we found two datab cases
that were overloaded a little bit more
and this we don't accept so when we see
cases like this through our alerts we we
start investigating and try to figure
out what
happened so let's summarize what we
talked about right so Microsoft promises
unlimited infrastructure capacity I
explained to you how the architecture is
built you know how we identify
scalability bottlenecks in the compute
here in the data TI we add more VMS when
we we need and we have an amazing load
balancing algorithm that you know
manages the sessions allocations within
those VMS we also add database capacity
when we see that it is needed and we do
this aggressively to scale out and then
just because we want to be efficient
very carefully we'll also scale down
sometimes but the main takeaway is that
it's Microsoft's responsibility to
handle this infrastructure you don't
have to worry about this however
those of you who are smart notice the
asterisk there right because as we know
in in life like most things are not
really free so there are some limits to
what kinds when do we actually not do
this and uh I'm going to q and Christian
to tell you a little bit more about
it thanks
very yeah so on the infrastructure side
we guarantee unlimited capacity and also
there there's an AS describ
because even there it's probably not
unlimited but what we can say is we
never actually stopped anybody like
there are some customers that use a lot
of database capacity orm capacity and
we've always so far just given them more
capacity but of course there could be a
day where we say Ah that's too much
there are other limits though there are
what we call operational limits and uh
these are documented you can go on the
website and um and see them and uh when
I look looked at them the other day I
found 47 different limits documented and
just to give you a feel for what they
are I I'm going to show four of them so
one is uh client connection limits and
what it says is the time during which a
client can reconnect to the service
after being disconnected and the value
is 10 minutes so it means if you if you
for example take your laptop walk around
the building and you lose Wi-Fi
connection for a while you have up to
minutes to reconnect to the session that
runs in the service but if you don't
connect we might cancel that session so
that it doesn't keep running that's one
limit another limit is company limit the
maximum number of companies that can be
contained in one environment and the
value is 300 so you cannot have more
than 300 companies in one environment if
you want more you need more
environments another limit max file size
the maximum size of files that can
uploaded or downloaded from the service
350 megabyte so if you have larger files
we will not we will reject uploads or
downloads and Max execution time out for
queries the maximum execution time that
it can take to generate a query if
exceeded the query will be cancelled 30
minutes
right those are four out of the 47 um
what about something uh really
interesting like how many US users we
support what's the limit on
that um and we don't have any limits so
you can have 10 users you can have 100
users you can have a thousand users you
can have 10,000 users we don't have
limits for that okay what about how much
they can do in the UI can they just open
as many browsers as they want yeah we
don't have any limits on what they do in
the UI they can open as many browser
tabs browser windows as they want they
can click as many buttons fill out as
many fields open close as many pages as
they want we don't have any limits on
that so the UI will kind of give
unlimited capacity what about on web
services so for web services we do have
limits and actually they have changed
recently for the better so let's look at
that and this is how it was in the past
and in the past it's like what 3 four
months ago
so back then the limits were per
environment and uh one is the maximum
number of O dat V4 requests that can be
processed at the same time requests that
come in when this limit is exceeded will
wait in a queue until the time slot
becomes available they wait in the queue
until they time out after 8 minutes and
the value is five so we will process
five in parallel that's the that's the
that was the limit and the other one is
the maximum number of simultaneous o dat
V4 requests including processed and cued
requests and here when this limit is
exceeded uh you will get 4 to9 too many
requests and the value here is 100 those
were the old limits let me just
illustrate more graphically how how they
worked so we have our service and we
have an environment called my
environment and we have somebody or
something that calls into it using in
using the web service or data web
services so let's imagine that this web
service
makes eight concurrent HTP requests
right at the same time eight requests
what happens as I explained and what the
documentation says we will have some
that get to run and some that get to be
queed and we will process five in
parallel so three will be queued up and
when one of the running ones finish yeah
there will be room for one of the cute
ones that's how it
works now what happens if this other
system sends another 100 requests right
at the same time what will
happen well they obviously can't run so
they have to be
queued but how many will be queued
that's where the second limit comes into
play because we have five that were
running two that were queed
already and so there's only room for 93
right because the maximum of cued plus
running was
100 so what about the remaining seven on
what happens to them well you get 4 to9
immediately we reject them
immediately this is how it worked in the
past and there was some problems with
that the main problem with that can be
Illustrated like
this so we have a system here that sends
a lot of requests and they get to run
and they get queued up because we can't
keep up you know they take too long to
process each one of them so and we we
receive more than we can
manage to
process and now we have another user in
this system this is John and he's very
important he's the CEO and he looks at
the his powerbi reports to see how the
business is
doing and when he presses refresh in
powerbi it also sends requests into the
service so let's say he sends eight or
six requests in right what happens to
them well they get queued up right so
they need to wait until they can get
processed now John is the very important
person right he's not happy about this
so yeah so that's not good for John but
it can actually also be the other way
around imagine this other system is a
sort of a realtime system like a
checkout counter of some kind like a
point of sales system and people are
waiting to get the respones from that to
buy stuff now that is actually more
important now suddenly than John's power
reports right so in general you know we
have two users here that and one is more
important than the other and we
shouldn't prioritize the wrong one this
was the main problem we wanted to solve
and this is how we solved
it so how do we solve so what we look at
today is who is calling so when John
refreshes powerbi the request will say
that they are from John right there will
be an authorization header that says is
John
authenticating and the other system will
also be authenticating as a user maybe
Steve or maybe better an intra
application either way we can see that
they are different and so what we're
doing now already is we have a queue for
both users for every user if there was a
third user we would have a queue for
that user
too so the six requests that John made
where do they end up they end up in his
queue and that means that five of them
will be running immediately and one will
be queued
up so you see with this approach no
users will wait for each other which is
what we wanted to
achieve there's a side effect here if
you can spotted we will actually process
more than five at the same time now like
here already we have two users and we're
processing 10 at a time and if you have
five users doing this we will process 25
at a time so we allow more throughput
into the service than we did in the past
this was a side effect so we looked at
that we consider considered it is that
even safe to do can we handle that
because the nature of web services is so
such that they can come all of a sudden
like one moment there's nothing
happening the next session second we get
requests so they come really they can
come really quickly like unlike UI where
people log in and they press a few
buttons like the the growth there is
more gradual but for web services it can
come out of the blue can we handle it
and we consider that we also changed
some things how we spread the load over
our VMS and said let's do it and so we
did it and it's going going just
fine so the benefits as I mentioned that
users don't block each other the main
thing and the side effect we allow more
throughput and if you also
noticed I didn't talk about you had to
change anything on the consumer side
like the powerbi or the system didn't
have to change anything it was only on
our side that we made some Chang that
allowed a different segmentation and we
allowed more to be processed at the same
time so you don't have to change
anything in your code
either unless unless you want even more
and so this is where it may be nice to
know how we Implement things because in
some cases perhaps you want to take
advantage of this of knowing this so for
example I'll give you an example where
it could make sense so here's a system
that makes a lot of calls 100 requests
per second and they get queued up
because the service cannot keep up like
it processes five at a time but they
take too long so the request gets get
queued up and this is not good so what
can we do about
this first let's do a mental exercise
let's split the 100 into 2 times 50
doesn't change anything right still 100
requests being sent per second they get
queued up it cannot keep up but what we
can do now is say instead of
authenticating as the same app in both
cases let's authenticate as a different
intra application and now suddenly we
get another queue and so half of the
request will go there and there will be
less
queing and if that's not good enough
let's add another inra application and
then yeah then you solve
it and how you solve it in in this
system one can be round dring so the
first request uses app one the second
request app two and the third request
app one again and the fourth request app
to or you can just use random like every
request pick a random entra application
to authenticate with then it also ends
up being evenly
distributed okay so with this you can
get more throughput but I know what some
of you thinking now and how do I know
because I talk to some of you you are
probably
thinking why do I have to do tricks to
get more
throughput why don't you why don't we
Microsoft just increase the number from
five to 500 it's much easier right then
you don't have to change your system
one and the answer to that is twofold
one our main goal was to avoid that two
users plug each other and if we just
increase the number we don't necessarily
solve that because there can still be a
system that just sends a lot of requests
and fills up the queue so others get
blocked
of course it's less likely but it can
still
happen the other answer is a much longer
answer and I'm going to explain it to
you just so we get it out so we don't
have to worry
Wonder so first an observation one NST
can cannot handle 500 let's say in
parallel it's just too much as Raina
explained we run on BMS they have
certain amount of course certain amount
of memory and uh we just cannot handle
calls in parallel on such a
machine so what we do is we spread the
calls over multiple
nsts so now consider this scenario let's
say I make two sequential web service
calls the first call sets the name of an
item to the to London svel chair okay
and the second call I read the
name I would expect the name to be
London RV chair because I just said it
but since we spread
the uh requests imagine the first one
that sets the value goes to one VM and
the next request goes to another VM now
you have two
nsts and if you know about the nsts you
know they have a cach and so the first
one will set it in the cach will set it
in the database the second NST might not
yet have discovered that it has been
changed in the database there's a few
seconds delay there and so you might get
what we call inconsistencies if we
spread it like this and we don't want to
have those
inconsistencies we need to know when
such two calls that are sequential are
kind of related so we can provide a
consistent View and the way we would
con give a consistent view is by sending
them to the same
n and we could here choose to say put
the burden on and you say you must
provide some some header in the request
to say that these two requests are in
the same session they have a header that
says web service session one two three
and then we would know to send them to
the same NSD but that would be a burden
for you and we would actually break you
so that if you don't do it you will
start to see inconsistency so what we
did instead was say kind of implicitly
the user is a session so for every user
all of your requests will go to the same
in
another user request might go to another
NST so that individually you would see
consistent
views U so that's how we solved it this
is a lot of explanation I also try to
come up with a shorter version we need
to spread the web service C over
multiple nties if we were to spread them
randomly we would get
inconsistencies so we choose to spread
them by user so each user gets a
consistent View and then they get sent
to the same NST and we can handle five
calls for one user on a on a on a one
NSD that's okay not
500 okay so there's another limit that I
also want to talk about and I I call it
fairness here it's also like if we reach
this it's kind of an extreme situation
and maybe there's something wrong really
so it's also to to sort of catch extreme
cases so here Steve has created a tool
that makes 50 calls per second which is
kind of what we had before almost
so in the first minute it makes 3,000
calls in the second minute it continues
and makes another 3,000 calls in the
third minute it wants to continue but we
say no that's too much that's too much 4
to9 too many
requests and why is this it's because
there is a another limit that we that we
haven't talked about so here are the new
limits these are per user and you can
see that
we have the five that are running the
100 which is the maximum combined and
also the 95 which is the
derived um number that can be coed up
and then there's a fourth one the
maximum number of O Data before requests
that can be submitted within a 5 minute
sliding
window when this limit is exceeded we
get 4 to9 so that's what that's what
Steve got here right he he used up the
6,000 after in you know in just two
minutes so in the third minute we have
to reject him in the fourth minute we re
reject him fifth minute to in the sixth
minutes the the sliding window has moved
beyond the first minute and so now we
start to let more requests in
again so the way to think about this is
we allow very high bursts in a short
time 3,000 or 6,000 in one minute if you
can manage that but you we won't let you
sustain it like there's some problem
probably if one user makes that many
calls but what if you really want to
make so many
calls that's that's back to this way
then you need to adapt a little bit and
actually use multiple users because then
you can like what would it take to
support this many calls would take three
different users that would be enough
then you could actually handle 50 calls
per
second like
this okay so most of you should not be
hit by this but you can
be queued up things running slower than
they should you can get
429s but how do you know if if you are
impacted by this it's very easy if you
have AB insides enabled which I hope you
have you can go and look for the rg8
event which is the event we imit
whenever we process an incoming web
service
call and it has a few interesting
columns it has the response code in this
case is 200 which is not 429 so you know
we didn't thrott
you and it has one more which is the Q
time which is zero in this in this case
so we didn't Q quue you up either so
it's super easy to see if you are
impacted by this let's say you are
impacted then almost the first question
is who is impacted because now we have
these per user limits
and here you can use this Telemetry user
ID that you have on the user card which
is not the real user ID but another
artificial one that you can set and we
will show it here so if you do that we
will you will be able to see which user
it is and then you can change maybe
something about
that so you might also be wondering now
that we allow more
throughput can we see on our side that
the customers are getting more
throughput
we have some results and we will show
them later when we talk about what how
large customers are today in our
service but now I want to move on to job
cues or schedule tasks as they're called
uh on the platform level they also have
limits and uh they also changed recently
and the story is very very similar to
web services and let me just quickly
illustrate how how they used to work
they used to work like this you can have
a maximum of five running at a time and
any other job C entries that were ready
to run would be queued up and processed
you know as soon as one was
finished and the new job que limits
you'll never guess it they are by user
so every user gets five gets to run five
at a time and any others that they have
will be queued up so similar to web
services we will allow we will prevent
users from blocking each other here and
we will also allow more overall
throughput and I think I know what some
of you are thinking here as well because
at least I talked to some of
you uh in our companies it's always the
same user who schedules recurring job
cues so this change doesn't help at all
and to that I have two things to say one
is it will help in some cases like if
your company is designed has configured
to use background posting and Susan
posts a sales
order there will be a job Q entry
schedule as Susan so there will be some
spreading of
users uh by user uh automatically out of
the box but yeah for the recurring job
cues if you want to have more throughput
if you can see in your Telemetry that
you are being slowed down yeah then you
might have to adapt and use your users
more creatively
how do you know if you are being slowed
down the answer is again in the
Telemetry so here we have an Al
e25 event which we emit whenever we
start running a job Q entry and there
are two interesting in this context
properties on this one is the earliest
start time so this is the start time
that you set or if it's a recurring job
you know that was set so this is like
ideally we should start right at that
time and then there's the time stamp
which is the time that we actually
started and then it's very easy to see
how long time was in between in this
case there were two and a half
seconds now it's two and a half seconds
acceptable we think it
is actually when we when you schedule
something to run in the background with
a with a job queue you are already
indicating that this is an async
operation that you push to the
background so that you can continue
running in the foreground so kind of
already indicating that you're not
waiting for the
result that doesn't mean that we should
run it that it's okay that we run it an
hour later or even 10 minutes later in
my opinion but it's it's okay to not run
it right at the moment maybe 10 seconds
maybe a minute later is also acceptable
for sure two and a half seconds in our
opinion is perfectly
fine this Telemetry also has the user ID
so you know you know you can see which
whose job C entries are being delayed
and if you want to get an overall
picture I made this little query uh
which plots all the job C entry
executions so on the x-axis you have
time and on the Y AIS you have how much
were they delayed they delayed in
seconds and each dot here represents one
execution and so you can see in my
environment almost all of them ran
Within one or two seconds of when they
were supposed to run but occasionally
some were delayed by 4 6 8 or 10 seconds
right so if you you if you do the same
plot against your customers you can see
if they're really impact it's like
several minutes delayed and then maybe
you should change
something we can also see on our side
whether customers are benefiting from
these higher throughput uh capabilities
and we will also show you that now that
we are on the topic of job cues one
special case is you want to do some
background or bch processing uh in job
cues which is a very common case for
example you want to create and post
sales orders in
bets very very common
case suppose you have a company that has
100,000 subscribers they customers and
every month you want to send out
invoices to all of them and imagine that
every single invoice takes one second to
create and post then it takes you 28
hours to go through all 100 and th 100
thousand
invoices so from the beginning to the
end 28 hours maybe this is perfectly
acceptable for you maybe it's not if
it's not what can we do about
it and the main answer here is run them
in
parallel here we're focusing on the
creation of the sa invoices let's look
at the posting little bit later if you
just parallelize create multiple job que
entries like this
you will get more
through so here I have created Five job
C entries they
are 9 9.9 identically configured they
are set to run on the 25th day of the
month and uh everything is the same uh
maybe except the parameter string so
that each job que entry knows which
customers to process so they don't try
to process the same customers right but
other than that they all run at the same
time and just with this simple trick
alone it should take you down to maybe
six hours or this and we can do this
because creation of
invoices it they can run in parall just
fine there's no database logging or very
very very little at least so it's it's
not a problem to run them in
parallel so this is the main
technique so if you do this there's
still a couple of things that can go
wrong I just want to mention that you
can take into account and maybe you you
know you you can do something
about so if you remember this slide that
Raina presented we have a low balancer
that looks at the load on the VMS and
then if a VM is above 60% or some other
threshold on memory and other things it
will not send new sessions to that but
to other
VMS so what happens when we run the five
job que
entries we pick some VMS maybe they go
to the same VM maybe they go two to one
VM and three to to another VM but they
stay on a VM for 6
hours right we don't move existing
sessions so once they start on a VM they
stay on the
VM so imagine now what happens if let's
say they all end up on vm5 what happens
now if vm5 let's say after an hour
something makes it go to 100% CPU we
know what happens when the CPU goes to
100% everything gets very
slow so we can move the sessions there
stuck there so they are just going to
feel the pain and they're going to not
run in 6 hours they're going to run in
10 hours or
whatever that's one
problem another problem
is what if we decide to upgrade the NST
on the on this VM which we do maybe two
three times a week to to push out the
hot fixes the bug fixes that we
have so when we do this we give existing
sessions 50 minutes to finish what
they're doing which is not a problem for
web service calls and background jobs
mostly but and you also know by the way
you ass if you've ever seen this we are
refreshing the service that's that's
because of this that we're giving a
warning to the inducer saying hey when
the time is convenient for you press
refresh and then you will be created a
new session on a different
VM but any sessions that are still
around after 50 minutes which applies to
those job que entries that we have here
we will cancel
them and it's not the end of the world
for a job queue entry to be cancel
because you will see that it says it
failed there was an error but if you
have configured them to retry they will
just run again on a different VM and
they will pick up the customers that
hadn't been processed right but still
you might want to you might be wondering
why did why did they fail and uh is it
my code are you wondering no it's
because they were just restarted by us
still if you want to avoid that
uncertainty what can you do about that
so these two problems you can solve and
the way to solve them in my mind is you
you you you schedule them to run at most
let's say 10 minutes at least less than
minutes like this so we have some code
here where you say you know when they
starts to run take current time plus 10
minutes and then run until that time
or until there's no more work to
do process the invoices until that time
but when we reach that time if there's
still more work to do reschedule another
job entry and how does that look that
might look like this so you take the
currently executing job entry and you
create a new one schedule a new one that
is not recurring and um will start
immediately
so if you do it like this your job q log
entries will look something like this so
they are kind of grouped in
five the first one at the bottom are the
original ones and you can see that one
started
at 2:53 p.m. and it ran for 10 minutes
and then it was recreated or created a
new job que
entry at that started at 3:03 p.m. and
it also ran for 10 minutes and then it
restart another one so if you do this
you might see a lot of more log entries
right but um um you will not see errors
and you will not be stuck on a VM that
is overloaded so that is something you
can choose to do so visually we started
with this we parallelized and if you
want to break them up in smaller you can
do it like this and uh yeah it looks
like this that was the creation of sales
invoices what about posting
posting is the
same except there's more database
locking so in our Logic for posting we
take
locks
and and the this is this is a a more
problematic thing because now we cannot
parallelize to the same extent they will
be kind of synchronizing and not be able
to run strictly in
parallel still there is something to be
gain by paralyzing so we work with one
of our partners s Keon and one of their
customers and they are now experimenting
with running their processes in the in
in parallel so they have an experiment
where they run sequentially it takes six
and a half hours if the parallelize in
two job cre entries takes four hours and
if they do it with three job cre entries
it takes two and a half hours these are
representative numbers the number the
actual results vary more but what you
can see here is that
you know it doesn't it doesn't it
doesn't cut the time in half to paralyze
in two but still there's a lot to be
gained by
parallelizing and this is actually
something that a technique that is
generally recommended right run things
in
parallel if you um when I you know when
I Was preparing these slides I I was
thinking about our our laptops and our
computer comps right they have CPUs and
back in the day they CPUs got faster and
faster every year but at some point it
got more difficult right and what what
did they do they added more CES and that
is now the way you handle more uh you
give more
capacity so you can paralyze things so
what we do is we run sessions in
parallel I've talked about web services
we allow more to run in parallel job
cues we allow more to run in parallel
more users well that's more UI systems
we run them in parallel How do we do it
we spread them over more VMS we just add
VMS very very easy for us now we can
just let them run what about the
database we don't create more databases
for your environment so we have to scale
that one up but no worries we're not
close to hitting any limits there and
actually a fun bit even for databases we
sometimes have a readon replica that we
send some of your the request to so it
actually also in in some degree
paralyzed the main problem though for
parallelism in business Central what is
that
H
locking database lock it kills
parallelism right so one main message
here is if you want to
unlock
scale avoid d base
locks like minimize it because you
cannot avoid it completely so it can
mean that you don't take exclusive locks
maybe you take you use read committed if
you have some typ code that that you
need to optimize or maybe you take
smaller locks like for God sake don't
use lock table because then you will be
taking locks uh
inadvertently and if you when you take a
Lo maybe instead of taking it for a long
period narrow it down by moving things
out of the period where you have to log
and make sure that this runs fast by
having the right indexes on the database
and so on but those are some techniques
not going to go into details right after
this session there's another session
about new capability that we have which
is trate locking really recommend you to
go and see
that okay
but like the others how do you know if
you have a problem with database
locks
our story there is not as great
unfortunately but but you do have some
cues in Telemetry we have an event that
fires whenever we have a locked
timeout what is that so it happens when
you you know you have one session that
takes a lock another session wants to
take the same lock and if it has if it
waits 30 seconds that's when it says I
give up I get time out then we emit this
so it's a pretty extreme situation
nevertheless it happens and so if you
see this it's a sign that that you have
a problem with the database logs another
technique you can use here is the is the
is the database locks page you can just
go into the to the product and open the
database locks page and then you would
see right now because that's what we do
we ask the database right now what who
has which locks who's waiting for locks
so in this case we can see that Nest wil
has a lock on the on the mixer table and
he would on the mixer list uh page when
he took it and we have uh debah debah is
waiting for a lock on the mixer
table and so debah right now is is
slowed down by this and if you press F5
here we're going to ask the database
again what locks are there and who's
waiting and if DEA is still there she's
she's waiting right so she's not happy
so this is another way to see you know
if the locks stay around for a long time
and um and uh and where they are coming
from in which area they are which table
and which
code so uh yeah so the main message here
is try to avoid database locks um yeah
and now I would like to handle over to
Raina again we'll talk about how large
our customers are
today thank you question so just to to
make sure we're like on the page and
what we've talked about so far right so
we first started out with this promise
that hey we can we offer almost
unlimited infrastructure capacity then
we explained what the architecture was
and you know how do we handle like
Microsoft handles bottlenecks and
compute in the data and we also said Hey
in some cases there could be some limits
Christian explained those and he said
how could you try and work around them
but now you know we we don't really have
those you know like for basis we haven't
really Capp Tel right so let's see what
do we see in our Telemetry for how big
customers and what workloads are we
seeing today so we did this a similar
session back at directions in 2022 and
we thought it would be fun to you know
Compare the numbers that we had back
then and compare them with today so
first let's just you know remind people
what we
showed uh earlier so first in terms of
number of records and various tables
right so you could have a, users in a in
one environment which is pretty big even
back
then um you know 1.4 million sales
invoice head
up we also had you know 7.6 million item
Ledger entries and this was again two
years ago in terms of transactions you
know 5,400 sales orders posted in a day
for One customer another customer had
58,183
in terms of tenant database sizes you
know back then some of our biggest
customers were 400 gigs which we were
very impressed by and in terms of
migrations from on premise we also saw
some cases where you know 160 GB were
coming to the
cloud which we were also very very cool
like we were very happy about that then
let's look at browser interactions and
just to remind you like a browser
interaction is when a user is clicking
around in the browser um you know
they're entering some fields and they
are tabbing between those fields and
also what it is not is when you're
typing a character within a field right
so typing a character is not a browse
interaction it's only when you Tab out
so back then we saw about 312,000 in a
day for one environment and for some
environments we also saw you know 34,000
in an hour which is about 10% so you can
imagine someone sitting and clicking
around 10 times in a second and we saw
some environments that had that kind of
usage and in terms of web
services six one environment had 6
million in a day which was like Wow uh
we also had some environments that had
you know 77 per second on average in an
hour and we had some environments that
did 8,400 in a minute which is 140 per
second on average which was
crazy so we asked you hey what are you
concerned about right
and we wanted to know from the partner
Community what were the challenges or
what you were worried about and uh we
love the business Central Community you
guys are super active and immediately
sent us some
responses and uh let's have a look at
some of
these so
Waldo said that he was currently worried
about helping a customer with 120 people
entering sales orders at the same time
on SAS it's very funny because he had
his uh finger crossed so wonder what
what he was thinking like you know
wondering um sales AO creation Christian
talked a little bit about it but you
know there's two ways it could be done
either manually or there could be some
automated uh methods like when
synchronizing from a web shop for
example and we have customers and we can
see this in Telemetry that are creating
thousands of sale aers per
hour um and one of them for example had
about 8,000 sales orders in an hour with
about 60,000 lines in
total we also had another customer that
created about 4,000 in an hour but
150,000 lines in total so this is what
we're actually seeing in our Telemetry
right um and again so Alo he was
concerned and then he said now real life
this was in June
24 and the overall experience is good
and there's an exclamation point I
wonder if he's surprised or excited I
don't
know and uh there's still quite some
load on the item table right so the 600k
items and uh sometimes searching as a
challenge on average 2 seconds but he
was okay with the amount and you know we
we we know that there are some
challenges and uh we're working on it so
stay
tuned um saano had post mentioned that
you know now not creation but posting
100 invoices in an hour with about 7,000
Rose per second real world case Camille
tweeted us and he said that hey you know
again posting 100K invoices per month
must be done within two
days so let's look at what our customers
are doing and how are they posting right
so we already see that there's customers
that again post thousands of sales and
voices per hour we also saw one customer
for example that posted 5,000 in an hour
another that did half as many so 2,500
in the same hour but 12,000 lines in
total so this is already
happening um then we wanted to check
with the number of users and if you
remember you know we had two years ago
about a thousand
users so since we're SMB most of our
environments have you know fewer than 20
which is
good uh thousands of environments
actually have more than 100 users and we
already see this in Telemetry and we
also have several that have more than
1,000
users so this is uh this is very very
different from two years
ago what about database
size most again since SMB are less than
100 gigs but we have many that are more
than 100 gigabytes and some are also
massive like we have some customers that
are you know 1.4 terabytes and they are
running they're doing their work so
they're have haven't heard anything
yet and a lot of large databases are
actually coming and you guys are being
super cool and helping them migrate from
on Prem to S and in one month we had one
um you know several were migrated that
were more than 100 gigs some were even
more than 250 gigs and we actually have
migrated customers with more than 500 GB
of tenant data so this you know these
people are now coming to business
Central online and they're running
let's talk about browser interactions
you know just a reminder of what they
are and what they are not so you know
just each character you type is not an
interaction it's when you Tab out and
click around and open close uh all those
sorts of
things so two years ago as I said we saw
about 10 per second on average and then
we looked at it today and uhhuh 300,000
a day 36,000 in an hour hm that looks
oddly familiar it's a little
embarrassing it's still 10 seconds on
average what's going on some explanation
needed right so we dug into it cuz uh
you know when we monitor our Telemetry
we don't just leave it we actually want
to know why we're a curious bunch and we
found out that okay there's browser
add-ins also sometimes and they will
just you know send some pings or you
know send regular requests but that is
not a user browser interaction and we
found you know when we collected these
numbers two years ago we included them
incorrectly so now we fixed it and uh we
get 10 per second on average so we think
the previous numbers were quite inflated
but we still have the impression that
you know it's doing really well so if
you now support as many as we
incorrectly thought we did back then but
it's a good sign and we're now
monitoring
it um then again if you're also as
fascinated with Telemetry as we are we
try to a look at one environment and
looked at the browser interactions
perform per minute as you can see during
the weekdays there's a lot of work which
is you know just cool and weekends a
little low and Easter well people are
away this is just for fun they just
wanted to show you that we actually look
at these things um now let's look at Job
cues now job cues we actually did not
have numbers from 2 years ago but we did
start tracking these from about 6 months
ago so so back then for example we could
see that there's you know some
environments that do 350,000 in a day
which is great some environments are did
15,000 in an hour for per second on
average and some even 300 in a minute
and 5 per second on average and
Christian had promised you that we'll
show you some numbers right after we
made our changes this is our moment so
what do we see today which is six months
later after we made our changes to the
service we see that you know some
environments have 415 thou 15,000 in a
day and some have you know 18,000 an
hour but the coolest one is 16 per
second on average so that's gone up you
know almost 3x and people have not had
to make any changes on your side right
it's just when we changed our limits
when we changed our
architecture like we can't guarantee
that these users are doing things
differently but we suspect that this
just happened out of the
box what about web service called
so again we tracked some numbers back
then you know 140 per second on average
that was a number that we saw 2 years
ago we did our changes let's see what
happened and now we see 10 some
environments are 10 million web service
calls in a day we saw one environment
that did 1 million in an hour so 277 per
second on average and some even had
32,000 web service requests in 1 minute
which is a massive f 140 per second on
average and this is you know successful
requests so no throttling no none of
that and that's almost four times of
what we were seeing four year like two
years ago so we don't know for a fact if
they re architected their solution to
you know use multiple apps as Christian
said but we also know that some
customers will just have different users
that are creating web services and these
are most likely the ones that
immediately benefited when we Chang
limits and change the architecture but
they're great numbers we really like it
if you want to know more about you know
what can business Central handle we've
actually documented this in the
scalability for business Central online
and the same numbers that we have in
these slides you can actually find them
out there as well so if you ever are
having conversations with some customers
and you want to know hey can business
Central handle this it's in here in our
public documentation so you can go and
have a look look at
that and now I just wanted to
uh ask you tell you guys a little bit
about what we're working on in terms of
scalability and I wanted to ask you a
question
first
so what do you think about the 80 gb
that we have and the one production and
three sandbox
environments and uh what I'd like to
know is you know maybe
clap if you if you love it
is anyone happy do you love this like do
you do you think this is
great
no well we reviewing this right so uh
with the whole revamp of our service and
our architecture and these user limits
Etc we are now looking at this as well
so stay tuned we have some announcements
that will be around the
corner and uh
yep we know we know we know what you
want so let's see this is uh this is
what we had planned for today basically
and we we wanted to you know tell you
that we really want to support huge
customers huge workloads we are
designing our service for scale so you
don't have to worry about Hardware you
don't have to worry about
capacity uh we have amazing autoscale
load balancing algorithms and we learn
as well so we look at Telemetry and I
hope you're convinced that we look at it
really closely to try and see you know
what can we improve what can we we do
better and uh infrastructure is
Microsoft's responsibility and you know
we add capacity as needed and we've told
you the cases where there are some
limits especially around web services
and job cues we've also told you how to
you know handle them how we do it so you
can better design your Solutions as well
if you need higher throughput what could
you
do and the main takeaway is to paralyze
and chunk work into smaller batches
right right so avoid these long running
sessions now that you know how we do the
load balancing and Autos scale you know
that you don't want to do tricks to keep
sessions alive for example because a
moment we can you know say that hey this
VM is overloaded go here gives us the
freedom to to do these things on our
side and the main takeaway as Christian
has also been mentioning and a lot of
other sessions you've been hearing about
so far Tech days minimize database
locking
the larger and larger customers are
coming to business Central online we
showed you some numbers we are hearing
from you you're sharing your stories
with us and it's amazing so we can
handle these and we are getting very
very mature as a service and we're very
confident with how things work
now that's all we had to present and I
also have Christian and Maria who will
help with some Q&A so let's have some
questions
yeah yes we have one here I'll give you
this yeah one question to the scaling um
can we track when you when you scale up
so can we get that in the Telemetry as
well um we've been thinking about this
but in general we want it to be
something you don't have to worry about
at all so it has to be seamless right so
as long as we're doing our job well you
should never have to know what is
happening so if we know and these things
happen automatically and you know
thousands of databases are being you
know monitored and scaled up and uh uh
adding more capacity so we really don't
know if that would be too useful to you
but we do have all the other Telemetry
available in app ins sites which we
thought might be more actionable in that
sense and we have alerts right so we
know that software can have bugs we have
alerts that tell us when something's
wrong and then we immediately go and fix
it
so this is this is as we said this is
something that we will like to worry
about and hopefully you don't have to do
like worry so much about but we might
want to give you actually some signal if
things are like not that good and we
know about it so we would like maybe
from partner Elementary or talk in some
way you know your session your
environments maybe yeah they not doing
so we're actually looking into that
based on feedback okay thank you yeah
third what's next and you get this
one uh I want to ask you about this uh
per user limits is this already applied
to all regions or you already or you
still roll Ting it uh it's it's for all
already the web services I think they
are only available for newer version so
if you are stuck on an old verion maybe
no no I mean that uh because still now
it was per environment limits and now
are per per user so it's roll outed for
every and my second question is uh when
I have a tenant with the six production
environments and I have a user that
works in all of them and also I have
sandboxes Etc is this limit per user per
environment or is per user per tenant
good question it is per user per
environment so they get the same
repetitively in in all the environments
and the same limits apply for the sound
boxes as well also
that you had
one wanted to ask about U you spoke
earlier
about scaling the paid environment is
there less power behind the sandboxes so
there's the compute tier and there's the
database tier and the comput same same
size VMS we scale them the same the
database is the difference we don't
scale it there so if you have a lot of
work going on in your sandbox and you
hit the limit tough luck that's we we we
don't add more capacity
there
okay um you showed us that there's an
autoscaling functionality but if I know
there will come in a massive load can I
preemptively request it somehow yeah
yeah it's a great question and we get it
a lot and there's really no need because
for the VM capacity if you look at the
Swedish cluster there 24 VMS that were
around 60% consider this 40% as our
buffer we have an immense amount of
buffer in these clusters so we will have
enough capacity for almost any workload
that comes in also on the database we
react very quickly so so there's really
no need to plan ahead here for us we had
the issue when there was some pre-sales
and we knew there were probably 100,000
users which will order something and
then we even if it's scaling out it you
showed us it needs about 10 minutes to
do so yeah so that would take too long
actually and that's why actually we we
keep continue improving this area
because what we want to achieve is like
you know full elasticity when you have
high Birds we can go as fast as we can
even faster than the 10 minutes yeah but
just reiterating what Christian said
it's it's you know we don't wait till
it's in the danger zone so we preempt
based on the pattern patter that we're
seeing and the algorithms are always
looking at this so you don't wait till
it's that late so yeah maybe one from
this side yeah
exactly hi uh I have a question about
the read scaleout database so for
example our we for our client we have
created API queries with read access
interet read
only uh the users are complaining at
sometimes it's slow business Central
usage and my my hunches is that uh it's
probably maybe powerbi during the day
making queries is that something that
can in some cases not be reading the
replica database and instead going into
the production database yeah that's
that's perfectly possible uh some of
some of your environments don't have as
a readon replica some only have the
primary one so it's only once we see a
problem that we then start to do these
things and add a read only replica so
there might not even be one and even if
there is one you have to also design a
little bit for it right you have to
annotate the code and say this should go
to the read only
replica that's something that we have
already okay but is it also does the API
queries go go through all the same nsts
so as the user so so can that also
affect
yes they go through the same and in
principle it can affect but uh but it
shouldn't right because as we explained
we have enough capacity on these VMS and
it's rare that they they they get you
know High CPU and low memory and things
like that so it shouldn't be a
problem and I mean you you have also a
bit of control how you use the replicas
with using the read only intent um but
then I also heard these days some
feedback about maybe we can Surface in
partner Telemetry when we have the long
run in queries if it goes to uh the
replica or the main I don't know yet but
we will look into that as well but with
the long long running queries uh we get
that into the Telemetry does that tell
anything about is it from the No No
that's what that's what that's what I'm
saying so today you can look and see
which are the queries which are slow but
we will not show you um if it's going to
the primary or to one of the replicas
okay all right next
oh sorry hello um so um you have said
that business Central is growing and
there are some huge customers already
and it's going to grow even more and um
as we know Microsoft have some other
products that are not the same obviously
but that are overlapping like fno and
we've had customer who has been steered
towards fno so I I would like to ask
you um how how are you
differentiating or prioritizing one over
the
other that's a good question um I think
I mean you should look at what you need
I would say I don't think we have we are
pushing one over the other like we're
saying what what we support and and what
we're saying now for example in this
ation is we support large customers
maybe f for example supports even larger
I don't know probably so you should just
uh take what is appropriate for the
customer and I think it's also the
specific scenarios you are interested
into you know inter company maybe you
know so you need to look at the
processes and I think you know I I also
got this question earlier and I would
really like to revisit what guidance we
have out there you know uh BC versus fos
so we'll follow up on that thank
you some over
here
first hello um thank you for um
explaining that job Q entries are
canceled when they are running during
update period that was puzzled us for a
long time but uh something we noticed
was that uh when this cancellation
happens often the job queue entry gets
stuck in still running but the task
behind it is is cancelled and and when
you open the job que ENT page it does a
find stale job queue entry and tries to
restart it very
sneakily so nobody sees but um if you
open it as a delegated administrator you
don't have permission to
start um to start job que entries so I
was asking maybe it's a it's sort of
related but if this could AO run uh
regularly I think we've had a history of
having somewhat unreliable job cues
right but uh if there still box around
there seems like we need to look at
it there was one over
here so um with the one production three
sandbox
systems uh how do
you suggest we handle
testing and bu fixing with customer data
because downloading is not really an
option and creating a new Sandbox can be
a problematic when there is sandboxes in
use and
the developer sandbox can we somehow
transfer customer data into this or
what's the go or what's the suggestion
to handle these things so the story
today which we know of is problematic in
many cases is you copy to sandbox and
then you uh uh you know experiment with
that but it can be a problem because
maybe you're using all your sandboxes
already or maybe you don't have enough
storage and so on so that's what Raina
was saying that we are looking at
improving and there will be some
announcement in the fall probably about
uh improvements there that I'm sure you
will you like I I would like to know
actually still from this room how many
people would like more storage or
environment yeah okay good to know
that's good so at the moment there is no
solution to you can buy more right
that's the same right so the only
solution is to buy a second production
okay or more or more storage if that's
what your what is limiting you but yeah
again stay tuned something will come for
x yeah I have a question regarding that
you
talked about the paralyzing and
concurrent uses for the job Q entries is
that also applying for the on premise
solution that you have five concurrent
uh sessions for the users when you're
using the job que no that is something
we configure in our
service okay so that's you can run more
on Prim you can run more on PR the
implementation is a bit different so
it's only for busy online but is it
still that if you use different users
that would actually take five jobs or
only one job per
NSG do you know but it's it's nothing
changed for it's not nothing changed and
it's not doing the per user thing at all
I think on Prim yeah and and it's
whatever settings you see in the NSD
configuration those are the settings
that are there so what we've done here
is like we have you know like a bunch of
services that actually do this
orchestration so we we've changed how
that happens online okay yeah
perfect are fresh nsts held differently
uh when the compuer scales out uh so are
is there some kind of delay when um
redirecting users to the fresh nsts
because some thing I've experienced is
that some users were r rected to the new
nstd and there was um some Lo loading
time still required because it's still
warming up yeah that can be that so so
what Raina showed is after approximately
10 minutes the new VM and D NST is ready
to accept new sessions but the first
sessions might trigger loading of uh of
the basap and other things and it may be
a little bit
slow yeah we are different levels of
cash so your new machine the NSC cach
will not be the same but of course some
others
will you you mentioned also Cashes in
between the nsts what's the period what
is Cash is synchronized in between the
N do you
remember so so what we do back in in in
our service is we use as a service bus
just as detail and so when the nsts
when one NST makes some changes it kind
of Waits a little bit a few seconds
that's is what I don't remember but then
it broadcasts it to the other nsts and
so they know aha okay I better refresh
my cash but I don't exactly remember
it's a few seconds like you can always
go to the Locking session and ask meds
and turban both will know for
sure any more questions you have one at
the
back wow
what
okay thanks so we we had a couple of
cases of customers which basically need
to work with the system 247 and heily
rely on job cues that run sequence where
subsequent steps relies on the result of
previous steps so and a couple of times
the overnight updates uh kind of mess up
with the whole flow because they're not
really we we don't have much control on
them because we we cannot set a window
we cannot uh and the window that it's
available is kind of large 6 hour I
think something like this is there any
plan in the future to have more control
on this parameter sort of reducing it
for a hot fixes
or I know it's coming from time to time
with a request but right now actively
not but maybe you know give us more
feedback on this and we would revisit
the story okay yeah maybe throw it on BC
ideas and see if like if you know if
there's enough votes then it might Force
us look at it quicker but yeah okay
thanks no plans as of right now we
actually have a cent that an issue with
this
well and they fixed that by enforcing
the update
sorry we we have a client that had the
issue as well and we fixed that by
enforcing the updates by um by taking
the box that says you can run it outside
of the hours so that way we can kind of
control when the updating
happens so that might be something that
you can use for
this any more
bcpt bcpt can run only on S boxes so the
main problem in uh using this for for
the SAS is that you don't scale behind
the scenes the the databases
so it is not reliable we're a using for
the on premises but for the line this
needs to be done on the production
system that's perfectly valid feedback
that uh if you had a production
environment it might actually bump up
the database capacity which it won't do
as we explained for sandboxes so you
will bet get better results once you run
in real production versus what you
testing yeah it's Val valid feedback and
I would love also to see more feedback
on this because you know the more you
actually push this ideas and vote on
those you know we we can take a look
more CU it's also another first time we
discussed a bit should we revisit the
config story for sandbox
cool okay let's take the last one over
there thank you um we're on RV and we've
recently or year ago created the SAS
version of that and we're migrating a
lot of customers up to the cloud or
we're planning on that and I've got a
large customer where I'm doing a proof
of concept so we're looking at getting
the data into your SQL first and we're
looking to do the proof of concept on a
production SAS environment for the
performance on the SQL that you spoke
about but the question is is there
anything in particular we should look
out for or investigate during that proof
of concept uh that you could
recommend yeah so the when you want to
test out things the best approach is to
use the performance toolkit that was
mentioned before because that will that
way you can simulate the the reload and
see if it's working uh as you expected
to if there's if the UI is responsive
the job cues are being processed all of
that more to do with the data migration
to be honest
ah what about I'm concerned that we
might not be able to run it in the
weekend for instance so so the the
migration to the cloud of the database I
mean you can the the way it works is
right it takes it takes an initial copy
of your database and then you can do
incremental changes from then on and you
can keep running like that and synchron
the two environments so that once you're
ready to finally move you can do the
last
incremental uh migration which shouldn't
take a long time I see so the in
principle it should should be perfectly
possible to do in a short time that last
piece all right time's up thank you very
much for coming to our session with
thank yeah
