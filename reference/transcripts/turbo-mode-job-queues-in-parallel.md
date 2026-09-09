# Turbo Mode: Job Queues in Parallel?

- **Source:** https://www.youtube.com/watch?v=O44cEgg0YwM
- **Video ID:** O44cEgg0YwM
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 79m10s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

Dear guests, good afternoon. Uh, so you
all signed in for a presentation in
turbo mode. Now then, simply give a warm
welcome to Jeremy Viska.
Good afternoon everybody.
So, I have the dubious pleasure of being
the last session before everyone
scatters to the wind. That's the bad
news. The good news is I'm not the last
session before everyone gets to go and
enjoy beer. So I'm not slowing you down
to that.
Uh for those of you who don't know me,
just a real quick summary. I've been in
the industry now for 25 years. I've
written some books about Business
Central. I've been an MVP for a few
years. Uh do a lot of free and open
source utilities for the community. Uh
QR code to link to a variety of them.
For example, I have the weekly digest
that sends a blog post uh summary of all
the blog posts in the community so you
can just keep up with things a little
bit.
So, um what this talk about is about um
I wanted to do something about AL code
because we kind of haven't had a lot of
that uh in the past couple days. I don't
know how many of you have noticed and
gone. Um but I wanted to talk about the
challenge of parallelism and how do we
deal with some of the things that are
going through that and the performance
impact of doing these things. Uh what
this is not a talk about uh is
explaining how job q management works
like what are all the features the
scheduling uh restarting things. Uh AJ
Kaufman has done a great talk about job
cues that explains the engineering of
how job cues is the UI that sits on top
of the taskuler and how all those things
behave together. Uh that's a phenomenal
talk. If you haven't seen it, hopefully
uh you can find that and it will be made
available. Uh but this also for those of
you who need the break, this isn't a
session on co-pilot.
Okay,
I I sense the AI fatigue.
All right, so I'm going to start this
out a little bit oddly. It's why did I
submit this talk? There's a little bit
of a story uh and I I hope you'll bear
with me. It's I think a story that a lot
of you can relate to. Uh I started with
a company earlier this year that does
businessto business and business to
consumer website integration stuff. And
when you're doing those sort of things
you have a limited number of ways that
you can bring data into business central
APIs, flat files, all that sort of
stuff. The job Q is our only scheduled
userless uh operation to process things.
So, we had a customer that had a very
very busy November last year. Um, true
funny sort of story. Uh, I'm a
transplant to Sweden. Um, and during
November last year, uh, they had Black
Friday sales like many people have
adopted from the US around the world.
Uh, they had Black Friday sales. But one
of the things I love about Swedes is
that they take a concept and they kind
of make it their own. Uh, I think the
keynote showed there were 17 of us here,
so maybe some of you are in here. Uh,
they tend to make the story their own.
So, my favorite thing I will see in
November is Black Friday sales all
month.
Um, a little bit confusing there. So,
our Black Friday for our customers could
be a day long, it could be a weekend
long, it could be a week long, it could
be a month long. And we had a customer
that was processing 3,000 orders an hour
in their environment through imports
from a external system coming from 10
different shops all over uh the
different countries that they do
business in. All of that was flowing
into business central in a central Q
processing table for a job queue to pick
up and process through. And what we were
discovering is that the jobs that we had
defined they they work well. Our
customers find them very very reliable.
But all systems scale to a point. There
is always a point where the demand and
the load is more than the system was
designed for and can handle. uh we had
inadvertently discovered that limit our
customer that when those orders came in
the orders would be released there would
be a bunch of operations that would
happen to those orders uh we would
create customers we'd create shiptos
when they were released they were
dispatched back out of the system to a
third party logistics company to fulfill
that order so a huge amount of things
would happen when that order JSON came
in I'm just curious since we've got
these little guys this year and I want
to make use of them a little bit. Are
there people in the room who have had to
solve similar technical challenges in
their NAV and BC environment?
So that's a pretty big constellation in
this room. Uh for the folks at home, uh
out out of the several hundred people,
we had at least 100 twinkling lights. So
um the the challenge that we ran into is
the customer said, "This was a low year
for us." And I was a little bit setback
because 3,000 orders an hour is kind of
a big deal for a business central cloud.
I would I thought and they said, "If you
cannot prove that this system will be
able to keep up with growth over the
next 5 years at the rate we've been
growing, here's our projected number of
orders per hour during Blackw week. We
want you to meet and prove because we
had a long-standing customer
relationship. They trusted us. But this
was something existential. if the system
couldn't keep up. What ended up
happening during some of those black
week days, and we fixed it very quickly,
is that the orders processing coming in
were so slow that the orders going back
out to the logistics system, their
warehouse operation team was at a
standstill. They had thousands of orders
coming in all the time and the warehouse
team was just twiddling their thumbs.
Very, very expensive scenario to have in
a production environment. So, we had
good trust. They believed that we could
solve it, but they were worried and it
was a valid worry. So they gave me two
weeks and said, "Whatever you want to
do, it's an app source app. Don't do
breaking changes, but whatever you want
to do, try to solve this problem. You're
an MVP. You've been to lots of
conferences for the past few years. You
think of creative things. Throw
everything." We called it spaghetti
brainstorming. We took a pot of ideas,
threw it at the wall, and saw what
noodles stuck. Um,
we had a lot of those and what I ended
up with was a set of process
improvements to the job queue that
anywhere from 40 to 93% faster operation
through our sample data set of 20,000
orders.
I didn't believe it. I spent 3 days
running more scenarios, creating
customers, adding more lines, adding
more validations. Uh we had like many of
you probably have experienced we had
thirdparty apps from app source. We our
customer creation process it was running
through a credit check. So it would also
call APIs while it was doing all of
these operations. There were performance
problems there. We helped them solve
that with telemetry and all that sort of
thing. So we needed to prove
quantifiably and the data was
exceptional. It was remarkable. And I
believe the quote is something along the
lines of extraordinary claims requires
extraordinary proof. So we had to prove
for our customer. I came up with this
pattern and later that week the session
submission for tech days was closing and
I said is there any chance I can share
this with the community and see if other
people can try this out? I want this to
be a thought experiment that you can
take home and explore. I don't know if
this is a good pattern yet. Our
customers, our biggest performing
customers are all live on this and have
been for months. We have not had
problems. I want to hear back from you.
I'm not hard to find. So, if you try
some of the things you learn here today
and it works, please give me that
feedback. If you found faults in the
ideas, please give me that feedback. I
called a couple of my MVP friends to
say, "Is this pattern safe?"
Um, and the answer was, "Put it out
there. See what this is a great
community. They do all sorts of clever
things. Let's find out what we can
solve." So, our challenge scenario that
we're going to dive into today is that
we need to do high volume operations.
We have data validation operations that
need to happen. uh we need to process a
lot of data, we need to create documents
because the number one question I got in
the app ahead of this session was about
locking whether you know it phrased in
different ways but the question I was
getting mostly is about locking and we
to have some buffer tables it needs to
be a missionritical process and it was
we need it to not be painfully slow. So
today we're going to demo through a web
shop flow that mimics a common scenario.
There were about a hundred twinkling
lights. So uh I think a lot of people
have had an experience like this. So our
scenario is that we're going to do a
validation step on an order JSON that's
coming in which would do some quality
checking make sure that the you know
values in the JSON are the right data
type and all that sort of thing. We can
simulate that. You guys know a lot about
it. Uh the big heavy thing that needs to
happen is the process, the business
logic. This is where the locking
nightmares come into play for a lot of
people. Um and then we're going to mock
up uh doing some emitting to third party
systems and email notifications. Most of
you have done something like this. We're
not going to create a whole framework
for these sort of things. And apologies
to VCO who's not here. I'm using it as
mocking. It's not an interface enum
style mocking. uh we're just doing a
simple uh pretenzies.
So our baseline sample that we're going
to work with today and we'll uh I I'm so
not co-pilot in this session that we're
not even on cloud. This is just a local
docker.
So, we've got this uh turbo app demo and
uh what we've done is uh in here we've
got our initial baseline of customers,
some addresses, some vendors, some
items. And in our scenario, the customer
uh they do fulfillment from multiple
locations, but they dispatch from a
central warehouse. So when we write up a
sales order, it might be in stock in our
main warehouse or we may need to
transfer it to our central location for
dispatch or we may need to buy more. So
our RO center reflects some of those
different data operations that we may do
as we work through this just to explain
point by point what's on here. And then
we've got that web Q table uh that has
the different states that we're going
through. when it first comes in, it's
going to be a new web order. Then we're
going to do our JSON validation, make
sure the data types are all fine and
that sort of thing. And then going from
validated, that's when we do the heavy
job. We're going to process that data
and that's going to create customers,
create ship toss, create sales orders,
create purchase orders, create transfer
orders. Does anyone think that that's a
lot of locking for one step?
it it is and it's very common pattern
because that pattern is kind of an
atomic unit. They go together. Um and
then we'll do our simulation of we're
emitting that to a web order and then it
we get the email that goes out to the
customer. So that's our scenario that
we're going to work with today. Um and
nice and simple, we're going to generate
our first batch of web orders and this
will give us a set of web orders in our
Q table. Um, and if we take a look at
this, it's a pretty standard JSON of a
web shop order. Nothing too fancy. We
have, you know, the web order number, a
buyer, a ship to, some lines on here
with some quantities. We're doing we're
not letting the customer set their own
price. So, uh, those are all zeros. Um,
this also reflects a challenge that we
had in our own environment, which we're
going to hit on a little bit later. Uh,
wonderful world of app source and
breaking changes. Someone originally
designed this product when it was on
prem. So guess what? The primary key was
a gooid. Um
that that was real fun. It's actually a
composed primary key. So I wanted to
simulate that in our environment here to
talk about how we do some things. So
that's the idea of this web Q and then
it's going to march through all these
individual steps. So uh for running
these because I don't want to wait one
minute for each cycle for the job Q to
take over. Uh we do not have enough beer
for that uh to just sit here and wait
for the job Q. So we're going to use the
uh performance toolkit. I hope most of
you have at least tried this out. Um but
this allows us to run processes in
multiple sessions. Our first uh run
through that we're going to do mimics
the way a lot of BC and NAV developers
would write a job Q code unit.
Everything happens in one big process.
It's kicked off by maybe one individual
code unit. There might be helper
libraries that do all the individual
pieces, but effectively it's one job. So
for that configuration, we are going to
run that in foreground, which also means
that we're going to get the ability to
have gooey things happening and whatnot.
And we're only going to run one session.
And I'll set this for 3 minutes because
I think that's on average about the
processing time of this. So, real
simple, we'll kick that off so that way
it's ticking along. And we can see it's
validating orders. It's going to give us
some uh information about the process as
we're running through things. And if we
refresh on our roll center, we can see
that the job is ticking along through
the different steps. And now after a few
seconds, we're now in the process where
orders are starting to create. And we
can see that we're in a position here
because the sequence of this design is
that it's validating. It's then
releasing and doing all the process
operations and then it's emitting. This
means that we've already just created in
the past few seconds 200 sales orders
that haven't gone to our logistics
company. They're still twiddling their
thumbs. So, one of the things that some
clever people will do is they will say,
"Okay, well, how about we take a web
order and we push it through all of the
stages one document at a time instead?"
So, at least that way we're getting
through all the operations. And that's
not too bad of an idea. That's one way
to potentially solve this.
I didn't mention it, but I want to call
this out. This little error web orders Q
on on the side here. uh if any of the
operations go wrong due to a deadlock or
any errors happen whatsoever, they will
show up in this queue. Any errors that
happen will pop into here. So if we get
locking issues in any of our demo today,
we'll see that tick up from zero.
So that's pretty basic. Uh most of the
folks in here are already envisioning in
their head kind of how uh the process of
this is working. Uh I left myself some
notes in the beginning of this object.
Um, quick aside, this uh entire
application, it's in GitHub. Uh, it's on
my GitHub profile. It's pinned BC Tech
Days 2025 Turbo app. Uh, so you can
absolutely review uh the code that's on
this. Uh, it mostly is okay code and
we'll talk about why later. Don't run it
in production. It has a ton of data
generators in here. But this is the
basic idea of that it would on run, we
are going to validate our orders. We're
going to process them, emit them, send
notification, all the standard stuff.
And each of these code units, with the
exception of lots of logging that I use
for diagnostics and and timings and all
that sort of thing, effectively
we're looking for any new status web Q
jobs. And then with some updates, if
it's gooey loud, we're going to do our
lovely codeunit.run on that. And if it
fails, we'll tip it over to error. Um
quick check of the room cuz we have
varying degrees of tech people and
knowledge in the room. Uh how many
people in here are unfamiliar with feel
free to light up unfamiliar with
codeunit.run handling?
We do have a few. Okay. Uh super quick
aside. Codeunit.run if you catch the
result of it runs it as a discrete
separate session. It it's a whole
separate write transaction. If you are
on prem, it's not allowed by default.
You'll need to turn that on. On cloud,
it is allowed. What this will do is if
any errors happen during the execution
of this code unit, uh this will return
false and you're able to access the last
error text as well as the last call
stack and all that sort of thing. So
this is uh that design principle that
Henrik Helguson talks a lot about which
is give your users a chance. This is
give your code a chance. How do you
catch errors?
But you cannot be in the middle of a
write transaction when you start a
codeunit.run. So we have our lovely
commit here happen before that. Uh if
you don't do that, I discovered this the
fun way. Um in docker at least, you just
get an error. It doesn't tell you what.
You can export the event log. It still
doesn't tell you what. I don't know what
version that stopped working. It used to
tell you that write transactions weren't
allowed during a try and now it just
crashes. But the general principle of
all of these procedures is the same.
It's basically just on a status and
looping through and doing operations.
Now the savier people in the crowd would
be shouting at me at this point. That's
an enum and you're basically just doing
running loops of things. You could
absolutely do this as an interface on
the enum and just call the interface.
Yes, I could. Uh the point of this
solution demo was to show even back in
nav this worked. I used to write code
along these lines when we had the NAS
uh no screams of terror when I said the
word NAS that's good for those of you
who know don't know that was the on-prem
job cube before there was job cube
nightmare. Um it got much better when we
went cloud. So that basic operation has
gone through and we now see our lovely
process has completed and of course we
only ran one code unit and we ran it in
our session. So of course there's no
deadlocks. Why would there be uh in our
operation every single step for every
single document we're calling a commit?
So there's there's no potential for
locking. We're releasing those locks
very quickly. So okay, that's not too
bad. Um, just to help visualize that a
little bit, let's grab uh
let's grab a flowchart here. And we're
in fact going to look at uh that as a
gant. So, uh we can see that at
beginning to end it took about 10
seconds or so to move through the
validating step and then we moved
through some processing and we went
through fulfilling and emailing. So,
very waterfall methodology on our web Q.
Um, could I have done this in telemetry
with Azure data explorer, PowerBI, all
those sort of things? Of course I could.
Um, I wanted an offline capable version
of this solution. So, uh, this is just
displaying exactly what we expected. Um,
we went through the web Q, it created
customers and shipto. So, if we take a
look at the operation just to validate
that we're doing all these things, we
created 500 new customers. we created
all sorts of ship to for them uh to be
able to fulfill those orders. We created
a lot of related documents. This is
going to be important for the following
flows where we're running through the
parallel steps. So, we cruise through
each of those different operational
steps. Um and that was what I call the
basic standard loop of forever.
Um some of you have had the pain
experience that I've done where it's
still working on the first batch of
2,000 orders and you're just waiting for
it to get through. So the big problem
here is that all orders for a given
stage have to be handled for the orders
to move through to the next stage. You
might be able to do a per document flow.
Maybe that might get you through some
things. So let's move to the good stuff,
right? The good stuff is parallel
operators. Now um this one is where
there be dragons. Um the the number one
question I got was about locking and uh
I also got some questions about what's
the division of labor, what jobs are
doing what? Um and can we do anything to
think about stages? So the key to the
parallel operators that we implemented
in our solution and uh we're going to be
going through today is we're going to be
doing batches at a time. We don't want
to just say, "Give me all of the new web
orders and I'll run through all of
them." So, not only are we doing
parallel operations, we're doing batched
operations. So that already is going to
start to help. The other key things
about this methodology that I'm using
here is that those batches are going to
be finite and all of the things that we
do to each of those entries in that
batch is a very atomic transaction. So
talking about this as a new and
experimental pattern, if you're trying
to do some sort of posting routine
that's going to post 10,000 journal
lines,
this might not be the pattern. If the
whole batch is supposed to succeed or
fail together, this might not be your
solve. But here we have a pile of
discrete operations. They're very
atomic.
So let's uh let's dive into what does
that look like because I think this is
the part that we all want. So, uh, first
of all, let's scooch some things out of
the way so we can look at our logic
here.
So, in our on run, we're going to take a
throw through some of the functions that
I'm working with here in a little bit
out of order from the way that the
function uh, explains it. Uh, first of
all, we need to locate all the entries
that are relevant to this run. And I'm
going to locate all the new entries that
I might want. I'm going to locate the
validated entries, the release
fulfilled, all those different statuses.
I'm going to call these little
subrocedures. Again, could be clever
with some enums interfaces. Wanted to
keep this simple. So, first of all,
before we locate any entries, we're
going to check against an operational
limit. How big do I want the batches to
be? If the operations that we're going
to do is larger than the batch, bail
out, stop, like, let's let this job
queue complete. We don't want a job
queue that runs for eight hours. We want
these to be fast. So then it will loop
through the new status entries. And
again, if we check to make sure we're
well within the limits and all that. And
then if we find an entry, we'll add it
to this object. on this object is simply
enough because my demo primary key uh is
just a gooid stick it in a list net
lists like because this is effectively
under the hood just a net list they're
very very fast I was addicted in the nav
world and for a very long time to
temporary tables uh anyone else also a
temporary table addict
definitely a few hands in the room um
I've moved a lot to using lists and
dictionaries uh because Top secret uh
engine tip under the hood temporary
tables tend to get rendered asnet
dictionaries and lists. So skip the
middleman uh if if you're dealing with
simp simple things. So this list of
goods will be the operations that we're
working through. Uh and we increment the
operations to do. Now that's nice and
all but that doesn't get us our
parallelism. We now invented the
batching system. So the next thing that
is relevant to our uh being able to run
in parallel is this little lovely beast
emit the claimed operations to team. And
what this will do is it's going to scoop
up all of the operations in each of our
lists of gooids and we're going to stuff
that into a JSON object.
No big deal. We've got lovely JSON
handling and it keeps getting stronger
so why not? And then uh for funsies,
we'll just write this to a record, my
control table. This little control table
is just going to be uh a code and uh a
claim timestamp. I'll keep track of what
session so we can clean up after the
fact. There's some logic behind that.
And then we just stuff that job in a uh
JSON in a blob. Nice and simple. Um in
early iterations on this, I did what you
normally would do as a nav developer. If
I was going to say I want to process
those 100 orders, I will claim them. I
might set my filters and then modify all
claimed or claimed by session ID. That's
a 100 writes. That's a lot of locking on
that Q table. So we moved it off to a
separate table. Write once, read many,
write once. So in our flow here uh of
the operator control, we just write that
out to that.
Then in our next step of operations,
we'll execute all of the operations. But
let's swing back to that locate all
entries. There was a function call I
skipped over. Gather all the claimed
entries.
What this does, as you might imagine, is
we can loop through that control table
that isn't the current one we're
running. And we can rehydrate that JSON
object that's stored in our blob and
bring that together into a new list. So
we create a new list of gooids of
everything that's already claimed. Nice
and simple. So in my case scenario that
I'm going to show shortly, we have five
different processes running at the same
time. Uh someone was a wise guy and
suggested uh in my demo uh it's Friday
the 13th and the 13th tech days. Why not
13 background jobs? Um I Okay.
Um so what will happen is when that
fifth version of this operator starts up
is this list based on my operational
limit target say it's 100 this list will
contain 400 gooids that are already
claimed and that means that when I'm
locating my entries here I can check
because contains is an option I can look
in this list of gooids to go is this one
already claimed by someone else if it is
don't don't do anything with it, just
skip it. So, this got me around one of
my other fundamental problems of if
you're trying to do batching based
logic, could you do like entry number
one to 99, 100 to 199? I couldn't. I had
a composed primary key that had a gooid.
So, and again, no breaking changes.
Okay, fine. Fine. No breaking changes.
Um so this creates the list that
effectively gives us our operational
list of what we need to operate on. And
then finally when we call our execute
operations we have our gooids of which
operations to do and they're just in
these lovely little lists. So, execute
all operations does any new, does any
validated, does any release, does any
fulfilled and we just do a lovely little
for each loop through it and we go get
from the web q table and just like we
saw in the first operation, we're doing
the commit and codeunit.run log if
things go wrong and all that fun stuff,
commit afterwards. Um, it's very heavy
on the commits. So, be very very
thoughtful when you're using this
pattern. Make sure that uh if you're
going to need to roll back something uh
in case of failure that it's wrapped up
inside of the codeunit.run. Uh so like
sales header if the line creation fails
you want the header to roll back. So the
header and line need to be created
within the same commit stack.
And that's the core idea of getting both
batching and parallel workflow running
at the same time. So, we're going to
reset our data. Um, and I don't know,
uh, for those who have been to some of
my talks before or seen them on the, uh,
Techday's YouTube channel, I hope
everyone here already knows about the
YouTube channel for Tech Days. Um, one
of the things I've always spoken to is
if you're doing demo, if you're doing
training, give yourself, uh, something
to be able to run things over and over
again. You never know how many times
you're going to be able you're going to
need to run things. Uh so very simply uh
this resets my app back to the starting
point. Uh this removes all of the data
that we just created. Uh recreates the
baseline of all of our uh customers, our
items, and we're all clean to go nice
and tidy, ready to run things again. Uh
hopefully uh folks are doing stuff like
that. It's really helpful when you're
doing user testing. Um the demo here uh
for our operator steps is basically now
we're going to say for this operator
we're going to run five sessions at the
same time because it's not running in
the foreground. These effect this
effectively mimics the idea of five
different job cues running at the same
time. And then just for variation sake,
uh you can set some uh delay uh and set
it to be randomized. So they won't start
all at the same time. Uh you can have
that mimic process. Again, I didn't want
to wait for the uh job queue to tick
along uh for all of our different steps.
So uh that if we kick this off, this is
now running in the background. And if we
come to our roll center, uh, we should
within a little bit of time here, we
should see some operations ticking by.
And of course, I don't. The demo gods
have not been kind. I don't know if
anyone's noticed that at tech days this
week. Uh, the the demo gods have been a
little mean. Uh, we have what's up? Uh,
we are getting a lot more locking than
expected. So, what's happening?
Cool. Cool. Excellent.
Ah, someone uh called out the correct
thing. I was clicking too quickly and uh
it's sitting there processing an empty
queue. Thank you.
Exactly. So, so uh generate the web
orders, which only takes a second. We're
just piling up a bunch of JSON. So,
we'll kick that off again.
And now we should see we can see that
the batches are ticking along and we're
already starting to see the validations
happening and we're also starting to get
some orders release. As each of those
are going through, we're going to see
that it's not going to wait for all the
validations to be done. Uh we're going
to different do different steps at
different points in time. So this is uh
at the moment being controlled by a
setup table that I have uh for just
saying the operation limit. I want you
to do batches of 25 uh at a time. So
nice and easy. It's cruising through and
creating 25 at a time. And that for
about 500 orders only takes 3 minutes or
so. So that goes pretty quick. Um
and one of the nice things is uh because
these are running as separate uh
operational jobs uh in job q we have the
lovely parameter string that we can
potentially pass into the operation uh
which means that we can do different
operation types. So if it's a big deal
for me that I want to no matter how slow
the order ingestion is going, I want to
always have something ticking over doing
the emit, we can do an if wrapper around
that execute job and we can pass that
parameter string into the job and say I
want you this particular job instance to
be cruising along and only doing the
emit operation. Um, I did get the
question of if you're creating all of
these background jobs, uh, what are the
limits? Um, and this is the nice easy
answer on that. Um, the scheduled task
is based on the number of users that
your environment is licensed for. Um,
it's not always uh phrased super
awesome. U, the the more users you have
in your environment, the more tasks you
can run in it. And it's basically five
per user. This does not mean the user
who clicked the start the job cube
button. Um, so if you have 20 users in
your environment, you have 500 potential
background tasks going. So it's they're
they're pretty generous. It used to be
much smaller. I did chat with uh the
Microsoft people about uh the fact that
I'm teaching everyone how to run as many
of these as you possibly want and how
much that's going to hurt them. and they
said it's fine because this is
simulating a user volume. Uh the the
load of the extra jobs running is that's
why they gave us this. So this allows
you to make the most of your environment
and you can scale that up and down.
Um I also got the question from someone
in chatting about this. I'm doing a
demonstration where it's a single list
uh a primary key value of just one data
type. uh but my real production
environment uh we don't have just a
simple gooid or you know entry number as
our primary key for that web entry table
unfortunately. Um so the way we handled
that one uh to be able to make use of
lists uh in this environment is we
simply converted all of the primary key
fields into a string. So we had a list
of text. No big deal. when you do your
go get later uh you're basically saying
I want to go get this entry uh and
that's coming from your list. So all you
would need to do in this environment is
you would split the uh this entry uh
string into its components. So you would
do your lovely little split uh function
whether it be dashes whatever have you
no big deal as long as it can be stuffed
into some sort of list. Um, I said it
was going to be a co-pilot free session.
Sorry. I don't know. They I'll disable
it. My bad.
We'll disable that. Get out of here. Um,
but um, so you can absolutely do this
with compose keys. That's no big deal.
So if you're doing a job Q that runs on
sales header, purchase header, just
compose the key of string. Uh for
options and enums, you can use a value
or text as long as it makes sense to you
to be able to do a get on the source
record uh to begin with.
And then um we also ran into the issue
of some of our customers wanted to know
how frequently the job cues should run
because sometimes uh if we are doing
these little batches there might be the
job Q runs on a batch of 100 orders and
then it's idle for four minutes because
it's running every 5 minutes and only
took one minute. Uh just curious, does
anyone have that sort of problem where
their job cues trying to figure out how
the heck to get the timings on them?
Yeah. Yeah, me too. Um so, uh there's
there's not a great answer on that one.
Um I will say that, you know, having
seen AJ's talk about things, I set the
uh minutes between runs down to the
lowest value I think makes sense uh if I
need it to actually pause or not. Um
because if it takes 15 minutes to run
and it's 1 minute between runs, it'll
run for 15 minutes and wait one minute.
There's no it's not running every five
minutes, it's from the end of a run,
wait five. So, uh he has some really
great feedback to Microsoft in his
sessions on we can improve some of the
tool tips and captions on the job queue
a little bit to explain better how they
work. Um, so we wanted to for our
customer be able to do something a
little bit more exciting and make it a
little bit more thoughtful about uh how
we're doing some of these different
batching operations.
So I right now in my environment, which
we haven't checked on it, but check that
out. Zero. I had zero deadlocks and I
was running five different job cues at
the same time on those batches. Um, and
process-wise, if we wanted to sneak a
peek at that,
we can see that nice and easy, cuz I'm a
big fan of visuals. Everyone big fan of
visuals. I like visuals. Yeah. Um, we
have all these different operators uh
running in the different modes. And we
can see that uh it went through some
validation cycles before it kicked off
the much longer processing job. And we
can see that the processing jobs are
what's taking the time. So with a little
bit of logging, not unlike telemetry,
I'm just keeping it in product because I
wanted an inproduct answer. Not uh we
can see that the bulk of things is the
processing. But overall, our start and
end times, you can see it's diminishing.
That's pretty nice. I like that. But
we're still where I wanted us to be.
Zero errors. There was not a single
deadlock in that entire run of things.
So that's pretty cool. Uh we'll go ahead
and reset the data on that and I'll
remember to create the orders this time.
Um what we added to our setup before was
a global uh operations limit. So our
version two of our processing said we're
going to run 25 in our batches. Well, I
want to be a little bit more clever with
that. Some of you are very clever people
in this room uh and may have even
written things like this. I'm probably
not the first. I generally say I'm never
the first guy to have an idea. I might
be the first guy to get up and talk
about it. Um, what I added to our
operator control that we saw earlier
where we could inspect the claims and
all that sort of thing is give them a
target number of operations and give
them some nice guard rails, minimums and
maximums. And now one of our lovely
things that we can do in our operations
is we take our operator 2, the way that
things were working before where we were
batching up and we were doing all those
locations and all that fun stuff. Um, we
instead when we grab an operator control
record, we'll grab what is our operation
limit. This is the number of target
operations that we want to run. Well,
all that did was move my setup field,
right? Yeah, fair enough. Um, but down
here, if we're using dynamic scaling for
this operator, maybe you might not want
that for one of them for different
priorities, whatever have you. We're
going to just do a adjusting routine
that says, okay, let's look at the total
operations that this cycle ran through.
Uh, if we didn't do anything, we we're
not going to adjust anything, but let's
also calculate the runtime. And then
what we would do and unfortunately
because I'm in a demo environment where
I'm not running the job queue what I
would do in my product in my solution is
I go out to the job queue and I look at
the runtime between runs in minutes. So
for example, five minutes between runs,
I would say, okay, if the uh run time is
less than my job Q minutes, increase the
target operations by 10%.
That's all nothing too fancy. And
because it's an integer, we'll round it.
And if the operation took longer than
the run times, it took six minutes to do
that five minute job, decrease it by
10%. and we put some nice little safety
rails around, you know, minimums and
maximums. So, from a functional flow on
that,
let's grab our 500 orders. And I think
we'll be brave. We'll bump that up to a
th00and since I already had a nice demo
hiccup on demo two. Let's give myself
one for demo three. And we'll increase
that time runtime a little bit. And same
situation, we're going to run five
sessions of this. and we'll kick that
off because those are all running like
job cues as background jobs. There's no
uh UI to let me know where things are,
but we can see that things are already
ticking along on the validation process.
And now we've got orders getting
created. So that allows me to uh keep an
eye because I've got the control list
here that allows me to keep an eye on
the operations. And you can see that
dynamically these are already starting
to crank up. We can see that the run
times, it's keeping an eye on those
things just because I like diagnostics
and I love telemetry. I love telemetry,
but I also like inapp information. I I
need it right in front of me if it's
relevant to what's right in front of me.
So, you can see that this is just going
to go, okay, well, I'm able to pick up
43 next time. And this is just going to
dynamically grow the list. And if
something happens like start a business
day, you know, a CFO posts his budget
that's 150,000 line journal, uh, then
you can go ahead and scale that back
down the next time it runs. No big deal.
So, those are just marching along in the
background and we've got our lovely
dynamic scaling.
So,
we'll take a look at the results of that
in a moment because I did bump it up to
a thousand because I want I want to
force a deadlock to happen. I don't know
if I can actually. Um, so the critical
considerations to this pattern um is
that it needs to be tiny atomic
transactions. It absolutely must be
those sort of things. Um, one of the
things I was looking at is for example,
uh, are there places in the base product
that we could make use of this pattern?
And a example we were, uh, balling
around in the office was adjusting cost
on items. Uh, for example, many people
schedule a job to adjust costs. Well, we
can't necessarily do adjustments for an
individual item at an atomic level, but
that one item run, sure, we could do
that. So, that would make sense. adjust
cost for one item at a time, parallel
that up. We'll see how that goes in a
couple of our customer environments.
We're trying it in a PTE right now. Um,
error handling is vital uh because you
are introducing a mechanism where you
have a much higher probability of
locking uh the records that you're
working with. Um, and just as an uh lots
of people were asking locking related
questions. Uh, one of the things I think
it was 2 years ago Mads did a session
here at tech days that was talking about
tri-state locking and when the different
operations would lock things. Um, if you
are modifying records and then you go
read a another record, uh, that
potentially locks more tables than you
think it does. So be a little bit
careful about when you're starting a
transaction and then going and getting
data. So when I'm trying to avoid
locking issues, I try to frontload as
much of the read operations before my
transaction starts. Um some of our
customers where they've needed to avoid
these locking problems similar to this
job Q functionality. Uh if I needed uh
data, I would run queries and load that
up into buffers. I'd load that up into
lists or dictionaries. and only when
I've got all the data I could possibly
gather together, then start the right
transaction and move on to committing.
So, think uh very hard about what you
can do to minimize your locking
footprint. Um, and that'll help things
out. One of the things I did not
implement on this that is in our product
is of course when something is coming in
from the web shop and it runs into a
locking issue. I don't want the user to
just have to go to a screen and click
retry. That would be bonkers. Uh so I
would normally in our workflow and
apologies to anyone who does have that
and just felt like bonkers. Not no um I
wanted the deadlocks to show up here.
So, one of the things I would do is I
would consider to be a record on this
web entries table that says number of
times to retry uh and have the job pick
those back up and potentially have a
self-cleing routine. We can see that
with five parallel operations against
the thousand records, I'm still at zero
deadlocks.
That's pretty good, right? I think
that's pretty good.
Um, okay. So, I hope Um, since I did get
a bunch of questions in Hoova about
locking, do folks mostly feel like that
kind of answered how do I address some
of those locking considerations?
Okay, there were a couple of hands from
there. Um I did get uh a separate
question from Hoover that I wanted to
address that even though this talk is
not about managing job cues. I got the
question of if you're creating you know
12 different job cues for one process in
BC, how do you manage this? How do you
help customers actually react when
things fail? Well, first of all, do your
darnest to uh catch errors. Um, the more
you can prevent a job cue from erroring
conditions, great. There's a limit.
There's only so much you can do. My
favorite example with web shop orders is
when someone decides to block a
dimension.
Well, that shouldn't cause any problems.
Block
all of our web order imports suddenly
just stop. Um, so there's only so much
you can do, but do as much as you can
with that. And then I hope hope that
most of you have watched uh Waldo's uh
sessions in the past about telemetry
data um to understand how to read and uh
evaluate environmental telemetry. There
is a telemetry event for if a job Q has
failed and it's no longer going to try
to restart.
That's the one you want to watch for.
And I was a little bit surprised. I've
talked to some people in my organization
and in the industry about this.
Telemetry is something that's not just
for PowerBI to consume. Telemetry can be
consumed by all sorts of different
things. So what we have in our
organization is we have a logic app that
consumes the job Q has failed and
someone needs to deal with this and send
a team's notification to our support
team or to our customer in an email. But
we only do that on that failed status
when it's failed in a way that it's not
going to restart because if it's just
erroring job cues, it's just noise. No,
no IT manager wants to sit there and be
like, I got to restart the job queue.
Um, so when it comes to managing lots
and lots of job cues, make them as
resilient as you possibly can. Don't
fail if you can avoid failing. Uh, one
of the things I do in our organization,
if data can't go through because of a
setup issue, that goes to a separate
table, it gets moved over into a
malformed data situation table, and then
the job cues can keep processing, and we
can address that malformed data in a
separate way. Um,
and the uh thing I would recommend uh
because I I don't remember the telemetry
event, so I'm just going to bring it up.
Uh, in telemetry I quick check. Has
anyone not seen this before?
Okay, I I do get a little surprised
sometimes here and there, but every day
you learn new stuff. So, if you didn't
know this existed, central Q.AI, I tell
everyone in almost every conversation
about it. Um, the Central Q AI is built
by Dmitri Katzen. Uh it is built off of
not only learn content, but it's also
built off of books that I've submitted
to him for that. Uh it's built off of
blog content from around the community.
Uh and the crazy mad scientist that is
Dimmitri uh managed to also go out to
all of the MVP's YouTube channels, uh
Aropa's YouTube channels, Tech Days, and
get transcripts. So when you search
this, it will actually take you to the
YouTube video timestamp of when someone
mentioned it. So in telemetry, what is
the job uh failed not restarting event?
We'll see if it recognizes it as a BC
question because he did do proper like
don't harm and I'm quietly sneaking this
in here. This is LLM stuff, but it's not
copilot.
All right. So, we've got some uh some
information. I don't trust LLMs. So,
let's see if that's right. We'll take a
look here. And it was suggesting that I
want H7. And let's check that out. See
if it's right.
Job Q errored. That's not bad. Uh I
believe there's actually a separate one
for errored and it's not going to
restart. That's relatively new. So, it
may not have picked that one up yet.
Um, but that's the general idea of
central Q is that it will list for you
all of the different uh sources that it
came from. And this includes blogs from
people. So, for example, here's
Kristoff's blog. So, strongly recommend
useless. Um, and to answer the
management question I got, here's here's
your answer on Kristoff's blog. How do
you restart all your job cues? Well, use
some Power Platform. There's API calls
you can make that just restarts. No
problem. He gives you the step by step
how how do you do that? So it's it's not
scary. Um and that was all I got of I
was just trying to figure out what to
do. I didn't even know what the answer
was and now I've got my answer. So
wanted to raise that up because that
sounded like it was a real pain point
for a lot of people of how do I manage
the job cues? Um this is the lovely
answer to that. Make make a a little bit
of a toolkit for yourself to get them
restarted. Um, but do what you can to
make them resilient. I suspect most of
you who have had problem with job cues
and managing of them, uh, it tends not
to be your code that's the problem,
right? It's never never your code. Uh,
that's my experience as well.
Um, so, uh, a small thing I I did say it
was not a co-pilot session. I wanted to
mention there was an asterisk on that
one. Um, I actually set out for myself a
little bit of a challenge.
Uh, some of you may remember, uh, four
or five years ago, uh, I started
streaming about BC and that's ended up
being the road to MVP speaker and all
those sort of things. Five years ago in
the summer, I was just a nav developer.
I was in a small shop. Uh, that was all
nav development. We were stuck in the
onrem old ways. we were we were the
quintessential dinosaur situation. Uh I
took a couple weeks off and said I need
to learn extensions.
Well, that's a really great way to
challenge yourself to develop. So coming
to this talk, I said I wanted to
challenge myself. I wanted to move
forward.
Every single line of code in this entire
solution, all of it is co-pilot
generated.
I did not write any of this code
whatsoever. All of the tables, all of
the events subscribing, every single one
of these things. So, I apologize, but my
very first slide, I lied to you.
It's a 100% co-pilot
situation. So, uh there were some
interesting things along the way. Uh I
wanted to share that with you because I
wanted to challenge you. It's very easy
to do exactly what I've been doing.
We're peers. We're we're we're the same.
I just I'm on this side. Um I've been
doing the same thing. I'm typing in VS
Code. I've got GitHub Copilot installed.
And occasionally I can hit tab and it
understood and I I need a brace. Oh,
that that really didn't feel like that
was a revolutionary change. Of course,
it didn't. Hopefully uh some of you saw
AJ and Dimmitri's session yesterday
talking about vibe coding and all that
sort of thing. Uh felt very bad vibe
coding.
Um, but I absolutely had all of the code
generated by agents. And one of my
favorite ones that I I challenged myself
to learn early on was I needed because I
like doing demos from RO centers, but
the demo roll centers don't help me with
PTE. They don't help me with products.
Who here likes making roll centers?
It's It's not fun code. it's not fun to
write that. So I instead gave a set of
instructions and I told it to create the
scaffolding for roll center for me. Uh
go ahead and add customers and items and
vendors, but oh shoot Jude, I also need
uh some activity panels on my roll
center. Uh and I want those to come from
two different Q tables and we should
display those as Q groups. And uh if I'm
going to mimic a lot of other RO
centers, I want to see each of these
processing states based on the enum
value on this web order table. Well, the
thing about it is that it could go read
that enum.
All of those Q tables then were created
from those states in that enum.
So in about 30 40 seconds because fun
thing I don't know if you've noticed
this for those of you who have been
exploring and trying this out guess what
hello tech days hello tech days
you can just tell it.
So have fun with that. Um, the other
thing is I I'm surprised, you know,
we're developers. We love to push
buttons that we shouldn't push, right?
Um, I was surprised by the number of
people who opening this uh panel up uh
do ignore the bottom settings here and
just leave it in ask mode. Switch over
to agent mode and try out some stuff.
And what you can do is you can add some
different rules. So I want to add my
readme because we all write beautiful
readmes that describe the whole
repository, right?
No. Okay. Well, um, this is one of the
reasons that my development team I've
been beating them over the head. If we
have a readme that describes all the
things that are happening, which you
guys can go see in the GitHub repo, this
will describe all the things that we've
just looked at today. Um, this readme
can be used for the co-pilot to process
all this stuff. So, that's really cool.
Um, and I believe some people were using
cursor and that gave them the ability to
give like rules and stuff like that. Uh,
I also did uh copilot instructions. This
will go to copilot every time I submit a
request. So, I told it to do stuff like
you know include logging functionality
and follow follow some coding practices.
just just an idea and maybe make sure
the ids are in the object range of the
app JSON maybe. So, um and I want you to
comment this real heavy.
So, there's a bunch of things you can do
with this. Um I encourage you absolutely
to clone this repo and learn. There's a
bunch of different things I did in here.
Uh if you haven't watched Camosk's talk
about packet and nuette and all that fun
stuff, you'll notice that I also made
use of packet which is the nuette stuff.
I don't download symbols in this
repository. I don't hit download
symbols. I actually run a command packet
nougat and go get my symbols from the
AppSource ecosystem out on Microsoft.
So, there's a bunch of stuff in here. I
would love for you guys to learn. I will
probably write a couple more blog posts
in the next couple weeks to highlight
some of these different little bits and
pieces. Uh explore in this um and let me
know how some of these patterns go. Uh,
but there is absolutely a bunch of stuff
I hate writing the code for. So, one of
my prompts was I just want a progress
dialogue that gives me an estimated time
of completion. Well,
who here likes writing time calculation
in AL?
I saw someone blink for a second and it
was actually taking a photo. So,
like, okay. Um, but you can absolutely
start to get a little more elaborate.
Operator three, this was the prompt I
used. The only difference between my
second and third operator was the
dynamic scaling concept.
Well, one prompt.
The whole third demonstration from the
second demonstration, those key
differences, one prompt. I just wrote
this. And if you look at the commits, I
only started this repository uh Sunday.
Um, this commit uh I did yesterday. I
gave it a whole bunch of stuff and then
I went and go watched a session and I
came back and reviewed it. That was it.
It was coding while I was enjoying life.
That sounds pretty nice. I like that a
lot. But the good news is is that
there's that wonderful meme of uh AI
coding will replace us when users can
explain what they want.
I can explain what I want real precisely
with defaults and all that sort of
stuff, but I did have some crazy things.
Uh, Copilot is also great for
troubleshooting. And my favorite example
was when I was trying to build that
little Gant chart to display how the
operations were working. There were some
bugs in it. At one point, I got a
message I had never seen before that the
date formula 45,121
days uh is too large. So, I just plugged
in, hey, I'm getting this error. Fix it.
And pasted the error message, and it was
like, oh, okay. Yeah, I found the issue.
Uh, and then just for funsies, being an
LLM, it threw at me, by the way, 445,121
days is over 23 years. Oh, all right.
Glad you're excited about that. I'm not
I'm a little surprised the date formula
can't handle 123 years in day form. So,
um, I did get, uh, a few different
people also asking the question when I
previewed this talk for people, uh, how
the heck was I doing this weird Gant
chart stuff? Uh, anyone interested in
learning a little bit more about that?
Yeah. Um, if you haven't uh, played with
it at all, uh, I'm going to be doing a
webinar a little later this month on
AOPA. Uh, I hope people are well
familiar with it. uh that is Aropa
Academy. Um the link to that is in the
slide deck so you don't have to worry
too much about finding it. But this
wonderful channel uh just like central Q
I'm surprised by the number of people
who maybe haven't heard about it. U a
lot of conference speakers uh if they
have a session that didn't get accepted
or it was a session they accepted they
want to share it because it wasn't
recorded uh will run those sessions on
here. Uh so this is a great place if you
potentially want to become a speaker you
can do these webinars. They're just
online webinars but the uh the mechanics
of what we're doing here is a special uh
JavaScript engine on top of markdown.
Hopefully everyone here has at least
heard of markdown but this is a thing
called mermaid uh that is a markdown
style uh generator and co-pilots
understand it. So when we were looking
at our operation scale, we were looking
at a whole bunch of well it's just text
and what's copilot really good at text
without understanding anything. Okay,
most people here are probably like me
and looking at this going I don't
understand anything. Fair enough. Um,
there's a little generator that I made
Copilot create for me that basically is
just going out and uh generating the
timings from our demo data. So
underneath the hood in my application
when you go take a look at it uh there
are some log entries in here and I was
keeping track of what process it is,
what stage it was in, how many things
were operating and all that fun stuff
which gave me the rich data I needed
that this generator app could then loop
through and figure out the time for each
of those processes. And then in the end
uh what it will do is it will emit for
me a lovely little text message that
contains the markdown the gant um gives
me a little bit of an explanation here
at the beginning of that and then we
just generate that from buffer and
that's how I was getting and of course
Docker loves to fall asleep on us. Uh
and that just generates a text here.
It's just text generation. We're good at
text generation right? Text builders are
no big deal. So if you're looking for
trying to diagnose stuff and you've got
log entries, try out that agentic
co-pilot thing and ask it to build you a
mermaid generator from your log entry.
It'll read the log entry table and you
can say I just want a gant. Okay, so uh
hopefully that is something that you'll
also take away uh as good value. Um, and
I ran uh the jobs a little bit faster
than I expected to, but lots of people
have planes to catch, so I don't feel
too bad about being early. But that left
us lots of times for questions cuz I
expect there to be a lot of them. Let's
go.
So, so if it comes to posting, sell
shipment and invoicing, would you
suggest the same method to do it?
Um the question in case anyone didn't
catch it and rephrasing so I can make
sure I'm following uh is when we're
dealing with like sales order or
warehouse uh posting operations, how do
we deal with that? Right. Yeah. Correct.
Yeah. Um the answer is is I would treat
each document as a discrete operation
because if a document from beginning to
end posts successfully, great. You're
fine. But if you can divide that up,
warehousing in BC can certainly handle
30 warehouse people posting uh batches
at the same time and they're making
improvements in the warehouse posting
module. So why not batch that into 30
different job cues and run those at the
same time? Uh one thing I am
experimenting with and I would love
feedback on this as well is having the
job Q kick off task schedulers. So
there's one main dispatch queue entry
and it just chooses how many tasks to
schedule. Um but in that scenario where
you're doing the warehouse posting at
the start of the ship and invoice
operation and at the end gate that
transaction commit before commit after.
It's a nice discrete operation and the
smaller you can make those operations
the better. Um, if there's data that you
need to pull into that operation, try to
get that onto the document during
creation of that document. Then you
don't have to go get the record during
posting time.
Any other questions or is everyone
anxious to go home on this warrant day?
So, you mean you're splitting the post
shipment and the post invoice? you're
splitting that or you still do post it
would depend on how uh fault tolerant
the situation is. If the normal
operation is when I hit post shipment,
that's okay and we can stop there and
leave it in that state, then that's an
atomic unit of transaction. And so I
would split those operations up. If they
need to go together, like it only makes
business sense that we would do those as
two sep uh as a same operation, ship and
invoice, then leave them together and
that's together one discrete operation.
So that was a big part of the thinking
change to being able to spread the load
out is basically treating them as how
atomic could I make each unit of work
that I was doing. That make sense? So
some of those processes like the one in
my demonstration creating the sales
order, transfer order, and purchase
order, those all go together. If
something goes wrong with order creation
on the sales order side, I don't want to
create a transfer or purchase order. If
something went wrong with the
fulfillment, I couldn't purchase it. The
item was purchased blocked, don't take
the order. I could choose what level of
discreet I wanted to deal with in that
operational step. Or I might choose to
say, okay, I really want the sales order
to come in no matter what. I don't care
if the fulfillment of that is a separate
step. So you can make that business
decision that in my scenario where maybe
the purchase order can't get created
because of an error, we still want the
order to come through. So I would break
apart the processing step to ingestion
and reaction. And if reaction fails,
that's okay. We've still taken in the
order. But then you need to surface how
do I fix the situations that come up
where the reaction hasn't been able to
go through.
So, yep.
Any further questions? Excellent. All
right, let's see if we can do this.
Um, you used the the compost key for for
the list. Would the system ID also be an
option to use that one? Absolutely. Yes.
Um, so in my ex, uh, just to state in
case it didn't come through, uh,
couldn't you just use the system ID?
Absolutely, you can absolutely do that.
And that's a really fast way to not care
what the composition is. Um, in my uh
scenarios, sometimes a web order might
come in in three different parts.
Um, because for whatever reason, a
customer can come back to one of our web
shops and say, "I want to add an order
uh order line basically." And so we'd
end up with three order updates that we
had to process for the same order.
In our scenario, we want to process
those three together so that way
everything goes. But if you have a nice
easy record set that there's a single
record of operation, system ID is a
great one because it's immutable. So
absolutely.
All right.
I I don't know that I'm brave enough to
throw that far. I'm I'm feeling pretty
impressed with the uh fact that I'm uh
three for three. So, um, you made this
because a customer had some demands that
their solution wasn't running, uh, well,
they weren't sure that it was running
fast enough. Yes. Um, and we had a
little touch on on posting. But how do
you handle posting those orders for them
because that has to be a major issue as
well. Mhm. It it absolutely is. Uh, we
in that customer environment, uh, we had
a separate set of job cues that were
doing some of those posting operations.
Um we found that uh the release cycle
was where our customer was experiencing
the most pain in the sequence of things.
Uh because we're creating customers in
our solution and what they had done is
they had gone out to app source and they
installed credit checking and address
verification apps. And now suddenly
there's about 15 different API calls
every time we create or update a
customer. It got really bonkers in that
order creation process. That was where
some of our slowdown was. I um I admit
with the the story on this one, we were
at the 3,000 orders an hour. Uh my
testing in sandbox uh we got up to the
point where our test batch which we did
was 20,000 orders. our test batch with a
hundred lines on each of the orders. We
were doing 15,000 an hour. Um, I didn't
believe it uh cuz it was Sandbox. Uh,
and I don't know about you guys, but I
honestly just didn't even expect BC to
do 15,000 orders an hour on Sandbox. So,
I didn't believe it. I actually tested
for three or four days because I was
losing my mind uh testing all these
things. Um but this is another major
reason if you are going to do some of
these techniques uh get familiar with
the performance toolkit. Um I did my own
separate logging uh ecosystem in here uh
so that way I could do different
timestamps but the performance toolkit
itself uh you can see the scenarios and
you can see how long different things
are taking. Um, you can get insight into
how many operational read statements and
all that sort of thing, where the
slowdowns are. Uh, most of my locking
issues that I've had happen where my
logging was too extensive. Um, so you
can see that in our operation here, we
did even have one, uh, operation that
took 20 seconds in the background
because it was doing 14,000 updates. So,
uh, get real familiar with the BC
performance toolkit to help you prove
your data scenarios. Um, you absolutely
there are some built-in ones that you
can make use of because like I said,
Microsoft loves to demo all sorts of
things. Um, there are already
performance toolkit steps in here for
posting sales orders with a certain
number of lines. So, if you're needing
to test your environment because you've
got a PTE or your app from AppSource,
whatever have you, and you're not sure
if things will go fast enough, you can
absolutely try uh this routine. Um, and
you can also open up their performance
toolkit and copy a lot of their logic
and say, I want to do my own routines
where I'm doing a bunch of posting
operations. Our customer, the scenario
that I mimicked here, we just stopped at
the release. We do a whole bunch of we
post the shipment separately. We post an
invoice. We also do a payment uh queue
up in an operation. So there's a lot
more tables that we hit and um all the
related ledgers that got updated as
well. So it was pretty extensive. I was
surprised at the speed we got. Um like I
said, extraordinary results. I wanted
extraordinary proof.
Okie dokie. Oh, we've got another
question over that way. So let's go down
this way.
I was joking around with uh folks on
LinkedIn. I always get nervous throwing
and catching this. The only bone I've
ever broken was from a padded sports
ball.
Hi, Evan here. Um small disclaimer, this
is no um cloud question, no AI agents.
This is on prem BC14. Ah, yes. Um we
have job Q issues. you I'm pretty sure
most of you had this that a job cue
stays stays in progress and you don't
know is it locked is it doing something
is it what is it it just stays in
progress and um yeah and we all know if
you do restart it doesn't restart the
process itself then you need to restart
the entire service and so on um we have
a lot of these do you have I I know this
is pretty old school question but do you
have any tip or experience on that uh
Yes. My experience on that is that we
moved our job cues in BC14 on prem to a
separate service that we restarted all
the damn time. Exactly.
Unfortunately, I did get a question in
the Hoova app related to that with some
of the onrem uh that was asking the
question of uh is there a way to change
the user uh that you're running the
session as? And Microsoft is
intentionally still not making that
feasible and easy on purpose because it
has to do with audit traceability in
some countries. Those operations that
the job Q does has to be tied to some
licensed person who said I'm okay with
this job Q running for me. Does it suck?
Yes. Uh have have we been brainstorming
some alternate solutions? Yes. Are there
also partner solutions that maybe can
fix that also? Maybe. Yes. Uh, one of
the patterns that you can use for that,
uh, is you can set up a job Q that
schedules other job cues. And as long as
your user says, I'm okay with thisuler
running, then it can look for the other
job cues that you've ticked the box of,
I want this to start, please, and it
will start that job queue running. So,
uh, you can get around that. But for the
Sorry,
I was wondering if we were going to
fail. Sorry about that.
Um, in your test scenarios here, this is
a pretty isolated test with basically
only your one process interacting with
both item sales and warehouse. Yep. Um
so my big question would be have you or
what's your experience with tests that
actually start with very different um
start points when you have like several
u marketplaces that want to do this with
their own custom things and you also
have a warehouse that has their own
warehouse activities and they're also
working but decoupled from your actual
uh test case here and basically just um
putting volume in the system while you
want to try and see how how yours does.
Yeah. Um there there's a couple
different parts to that question that
I'm hearing. Um one is, you know, if
you're starting at different points in
the process, like what kind of uh
scenarios can you do? Uh in the
performance toolkit, uh you can set up
lots of different code units to run. So
you could create test scenarios that are
creating orders. You can create
scenarios that are posting. You can
create scenarios that are warehouse
workers updating shipments. You can
create all these different scenarios and
set them up to uh run as numbers of
sessions and those will all run
simultaneously I believe if I recall
correctly. Um so you can simulate the uh
environment. The goal out of a toolkit
like the performance toolkit is you
should be able to simulate normal load
and that means that you have CFOs and
sales order people, warehouse people
doing all these different operations. If
you're talking about the testability
when you're dealing with external
systems, there things get a lot more
complicated um because then you're
potentially dealing with external
systems that are sending data in or
you're reaching data out. it gets a
little harder and there in that space I
do uh for our customers we do a lot more
of Yo style mocking where I have
implementations that simulate fast
warehouses that simulate slow
warehouses. I think one of my favorite
uh logistics partners that we work with
uh their API can only take one order at
a time
even at 150 milliseconds per order.
That's awful. So thankfully they've
they've updated and they're now taking
batches of 20. That's that's a little
better
high volume. Um so when you're dealing
with the testability of uh trying to
test this parallel mode thinking uh
you're going to have to think about when
you're dealing with external systems,
you're going to have to do some mocking
scenarios. So, you might have to create
a simulation code unit that calls into
your own BC API to simulate the
warehouse going, "We've just shipped
something and we want to let you know
about the 500 serial numbers you just
shipped." Um, that's one of my favorite
test scenarios if you want to really
churn uh locking is turn on serial
numbers for items because then you get
one item ledger entry for every single
quantity. Uh, it's nightmare mode for
locking.
So do big orders of like 500 batches
with serial numbers and you'll really
see the the performance of that. So to
simulate the the warehouse sending in
operations, create a mock code unit that
puts data in the same place that an API
call would. Do those two different parts
of answers speak to what you meant?
Okay, thank you very much. Absolutely.
Hopefully I'm not going to be anyone
else with a microphone.
Okay, well then I think that's that and
we will let everyone get on to their
airports and well we've got the closing
session. Hopefully lots of people are
going to enjoy that and hope everyone
has safe travels. This code is all up on
the GitHub um for me was the link in the
QR, but you also have the slide deck and
I'll contact uh Luke to make sure the
GitHub link is in the video description
on YouTube. I hope everyone here knows
that all these are going to be up on
YouTube. So, hope everyone's had a
phenomenal tech days and sorry for the
co-pilot fake out.
