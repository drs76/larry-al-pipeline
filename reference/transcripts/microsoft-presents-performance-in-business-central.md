# Microsoft Presents: Performance in Business Central

- **Source:** https://www.youtube.com/watch?v=fGkfRCb8vig
- **Video ID:** fGkfRCb8vig
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 98m29s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

Good morning ladies and gentlemen.
Welcome back in room 8. We kick off day
two with a uh Microsoft presentation
performance in Business Central and your
presenters are Yasper, Bardor, Turban
and Kim.
[Music]
Thank you. Can you Yeah. Yes, you can. I
can hear myself. So uh quick
introduction uh I'm Barter and um I'm an
application developer architect on the
base app. So I basically do the same as
you guys
um just on the base app and if I
if I miss some platform features I can
ask some of these guys. Yeah. Yeah. My
name is Yespa. I work on the server
runtime part uh together with Sen and
I've been doing that for the last nine
years.
Yeah, my name is Kim. I'm in the
platform team mainly on um availability,
scaling, performance in SAS, so on. Also
security, licenses, entitlements and so
on. Been in Microsoft for 20 years. So
if any questions come to me on that
and my name is to Mhov. I'm in the
server runtime and platform architect as
well. I was part of with Kim building
the first pieces from the NST back in
2005 when we started. Uh I was out for
some years. I'm back again. I've been
here for a year now and uh work on
security everything on the server. Been
part of yeah been doing reporting and
many other things over the years.
Great. Let's get started. Uh I won't
spend too much time on the agenda, but
we're quickly looking at um the overall
picture. uh how we can measure stuff or
observe
um how we search and filter and such and
then locking um which is a big topic and
then 20 tips and tricks in 20 minutes. I
think it's actually 21 but it's sounds
better. Um
yesterday there were two very good
sessions on performance um AL and
indexing and today I mean after this
session there are another two um so this
is just some advertisement for them as
well and
we believe that there is not much
overlap between any of these including
ours.
So this is a high level and technically
wrong but a high level picture of the
environment. I mean our users sit on on
one end um with their browser and then
we have the cloud uh but technically
it's two different machines. We have the
uh the web server and NST on one machine
or actually many machines but together
on one machine and SQL server on a
separate machine. Now that means that
there's latency between these.
So from the browser or from your users
to Azure there is um I don't know 50ish
milliseconds and between the NST machine
and the SQL is 1 millisecondish.
Um
yeah and the important thing is that
there's executing code on all of these
right on SQL of course SQL statements um
in on the NST al C and net stuff uh but
also in the browser there's uh executed
JavaScript and HTML um
interpretation and so on.
Um so when a user does something uh we
in telemetry we can see where is time
spent.
Um and if I quickly
these numbers are not very important
just the guidelines. So these are some
page opening times you see custom le
entries chart of accounts. So these are
the some of the slow pages and you can
see that these take maybe two two three
seconds to open but actually
approximately half of the time is spent
in the browser not on the NST
right so and we I mean I and you guys
we we can only influence this duration
NST um which is the sum of AL execution
and uh SQL execution.
Uh the lower part there is we can also
see page interactions. You know user
clicks something and um moves a field or
validates and the interesting there
thing there is that when they navigate
um most of the time is actually spent in
the browser. You can see if you look at
the duration for of the NST and down
meaning you can see that it's it's not
much and this is what
usually I and you can do something about
in AL code.
um
that piece of information is not really
important except that this is what we
consider okayish
uh usability. So when somebody tries to
open a page we say two 3 seconds that's
okayish.
Uh same if you are on a page and you
move from one field to the next we say
you know half a second for a validation
is okay and then I know that we have
sales line quantity that maybe a bit
longer
and of course if you type something it
should be immediate.
Uh then Kim will say something about
yes measurements.
So
um let me just spend 20 seconds on what
we're not going to talk about in this
session
in SAS performance availability the
compute the database performance all of
that is on us we make sure that we you
have all the resources you need um if
you feel otherwise come talk to me uh in
the export corner or after the session.
So what can you actually influence and
verify when when you have your customers
complaining about performance or raising
a question issue something like that we
the reason why we bring this up is from
the telemetry that B just um or the
information here that B just mentioned
is that sometimes we can see it's simply
we see this because we emit telemetry
from the browser and that we evaluate
and and understand and so on. And it
gives us a picture that the browser is
sometimes too slow to actually handle
the UI. And this is either it's a
complex page or it's a bad connection
and so on. So this is for you to verify,
right?
This is not a um recommendation, it's a
suggestion. use a tool to see what this
the speed of the PC or the tablet device
whatever the customer is using and then
you can see it's actually shifting in
performance it could be just after a few
minutes it's bad performance or good
performance so this could actually be
the reason why the user is having a bad
experience so just to interrupt I I
measured these two and in one of them I
was in a meeting the laptop was on
battery then I came back and plugged it
in then was suddenly 25. Yeah. Just
saying there on even on the same machine
it can be different. Right. It could
also be in a warehouse your user is
using a tablet walking around the
warehouse. Bad Wi-Fi could also cause
this. So um not not the the speed of the
actual browser or the tablet but the
connection could also be the root cause.
So measure your speed, measure your ping
time. What is the latency of your
device? One thing is to do in your
office, do it also at the customer
place. If customers multiple different
offices, then it's also important to
say, okay, where exactly did this
happen? And it's not always the back
end. It could easily be the front end
that is having an issue.
Um, related to SAS, of course, you need
also to verify your connectivity to
Azure. There's plenty of speed test you
can run and then verify what the latency
is to your region. Um, and again do it
on the customer location also.
So if there is a connectivity issue, you
can always use the
connectivity/connectivity
or the acronym here um for any of the
environments. Just put connectivity
afterwards and then you will see this
page.
Now this is mainly about connectivity
but I know our client team is also using
it for or planning to use it for for
measurements. So imagine we could add a
little script to see the download speed
the compute of actually doing some
calculations and that could be fit in
here. Then we get the information and we
can perhaps provide you the feedback
later on. So use these tools and then
verify that your client is set up for
success.
Yeah. Um and then we come to AL which I
and you right and if you seen any
previous presentation uh I may have
mentioned this before.
So when we execute AL statements just
not database statements but just you
know assignments and calculations and
stuff we we can execute approximately a
million lines per second. Maybe it's not
a million, maybe it's 700, maybe it's
1.3, I don't know, but that kind of
ballpark.
SQL calls
usually take at least a millisecond due
to the latency between the NST and SQL.
And then of course, if it's a very
complex SQL statement, it will take
longer.
I once looked at all our code units
counted you know the database statements
and the non- database statements and
divided so
roughly we have 10
um statements I mean non- database
statements for each database statement
and if you think of your own code it's
typically something about set filter and
set range and then some calculations
then we find a record and do some other
off. But all that um if you you know
calculate or multiply those values you
can see that we actually spend maybe not
exactly 99 but
90 something% of the time just waiting
for a database statement to finish.
And when I said one millisecond latency
is obviously not exactly millisecond. Uh
it has a distribution. So it ranges from
something that's very fast like half and
up to I mean two out here but the the
weight is like somewhere just under one.
Um and
does this matter? Yeah it does. Um
because we also looked at when people
run code unit 80, we can see how many
SQL statements they're executing.
And of course, I don't know if it's just
invoicing or just shipping or shipping
and invoicing, but
half of them spend approximately
a thousand SQL statements or more.
So that's that's a whole second, right?
a thousand milliseconds is a second and
that you know 5% of our customers or our
postings uh spend
38 seconds just on waiting right
just to like set the stage we're working
with
um all of these things affect
performance you know that latency
locking number of records indexes memory
CPU blah
uh we have telemetry and I guess many of
you use telemetry and if you don't you
should
um applications insights as it's for
you. Um that screenshot is some of the
runtime events that are emitted.
uh when I look at telemetry I mostly
look at longunning queries and
longunning functions because they
sometimes one function can have many
small short SQL statements like loops
and such
uh and you also have user errors by the
way I mean it is the type of wrong uh
date or something we don't emit
everything we get to you because it's uh
expensive I mean you pay money for it or
your customers do. Um
and we just before this event we um we
actually counted just for fun how many
limitary entries do we get in an hour
and that was a lot of billions and
corresponds to over a million per second
I mean that we get from our total base
of customers. So we also spent an
enormous amount of money on telemetry.
I think Yes told me that in the
beginning until we got it under control.
It was one of our biggest expenses.
Um but then if you have telemetry then
you can build PowerBI reports and such
on top.
Uh this is just an example of one of
them. Um I won't go into details but
when you have it you get interesting
stuff like where I mean which co-unit is
it? I think this is a demo from
somewhere.
Um
and when we I look at long running
queries I usually summarize because
there's always one slow occurrence and
some fast. So it's more interesting to
summarize.
Um and these are some examples where we
summarize for pages. Uh I won't delve
too much into the numbers but just to
say that this is the kind of numbers we
can get.
Uh another way to do it is um we often
get a complaint from uh you know some
customers saying you know when I do blah
it's very slow and then we say can you
uh give us a profile and then they don't
know how to do it. So I don't know if
you use it but I'll quickly show how to
do it.
And the great thing there is that there
are two ways to do it.
Uh so I will go over here
and refresh.
So under help
and help and support, can you read it?
Yes, you can. Down there, there is
something called analyze performance.
Um, and then you can click
start.
And then you go over here and do
whatever you want, like I don't know,
creating new sales order.
There. I mean, this this is enough.
Stop. And then we we get this more or
less useless picture.
Then we can click there and get a bit
more. And you could get a bit more down
there under call tree. But the real gem
is this the download.
Um, so when you download something, we
uh get
Yeah, since data. Yeah, that's fine. And
then it's downloaded and then you can
look at it. And I already opened one of
those similar files.
Um
actually I can take one
this demo. This is way more complicated
than what I did. Uh but but sometimes uh
the customers have you know really
complicated scenarios. So
so this is from some batch job some
production planning or whatever this is.
And you can see that this took 500
seconds
on the item um after get record.
And then you can drill down to see where
time is spent. Um
but what you also can do sorry there and
there. And again if you don't know this
uh there are two times here. There's the
time that is totally spent in the scope
of this function and then it has a self
time right. So in this case the code
function spends time 10 seconds itself
and then other functions that that are
called are spent the rest and then you
can dig down and you know try to tra
track what takes long. Um, but if you're
lazy, then you can actually go to the
leaf and summarize the leaves by just
clicking this icon over there. You can
see
which we is sorted by cell time and then
you can see where time is spent. So
apparently something that's called
calculate root line is the most
expensive.
Um, and then you can if you have the
project open in the Visual Studio code,
you can double click here and it will
get you into that function.
Um, so you can like analyze more here
and see why is this slow.
That was one way to do it.
The other thing we have done is
here because I have some pre-baked over
here.
um
analyze performance with scheduled
profiler. I don't know if you can see it
if I dock my head.
So here you can have several scheduled
profiles. And just for fun, let's make a
new one.
Um
BC Tech days 2025.
So in here you can say I want to observe
this period. And let's say that you want
to analyze some batch job that run at
night. Then you would put a time in here
that is at night.
And you can specify a username if you
only want uh a specific user. Could also
be you just want everything.
Uh and then this the tricky no not
tricky the smart thing here is that you
can select what do I want to track
because the browser thing is might be
easy but we have background tasks
meaning job cues basically but also web
service calls
um so that's great.
The way the profiler works is that it it
there's a timer that you know every as
it says there 100 millisecond looks down
and say where are we now and then 100
millconds later where are we now so over
time it will like get a pattern of where
are we most of the time you can change
that um
resolution to something else and you can
also say I don't care about jobs that
take less than 500 milliseconds for
instance.
And then in here you will have the logs.
The logs being exactly the same as we
downloaded before. Uh which is also why
I pre-baked um
one. Can't remember if it's this one
profiles.
That was not it. Sorry. Then it was this
one
with the profiles,
right? So
I think I ran a report like um
customer top 10 or something.
Um
so you can download these and then look
at them. So this is a great tool when
when your customers complain about
something very specific.
This these slides are just to
show what I just showed. Um the only
interesting thing should uh sometimes
there's also a point called idle time
there. So this could be anything. This
can be the user you know look reading
the screen or drinking coffee or waiting
for the phone to call or whatever. But
in this case when it's printing a report
it's the NST that wait is waiting for
the RDLC renderer to you know render
this report. That's also idle time seen
from the AL standpoint.
Um then we come into locking because I
watched um one of the good sessions
yesterday and we didn't they didn't
touch much upon locking. So I we thought
it was um a very good topic.
So imagine you and your friend, wife,
spouse, whatever um go to burger joint
and the process is you go over there to
the counter, you order your meal, you
wait, you take your meals and go to a
free table, eat, go out, right?
Now um sometimes it looks like this,
right? There are a lot of people and you
do the same, right? You go to order your
meals, wait. so on. Um
except my wife, she would go and
immediately occupy a free table if there
is one because there's obviously
shortage of free tables and then we
queue up and wait and you know nobody
uses half of the tables because people
are waiting there for no good reason.
I guess you wouldn't do that. um
you wouldn't right but in our world that
corresponds to this gl entry.lo lock
table and find last. We have like
sprinkles everywhere where we want to
um
have the world for ourselves.
And once you you know get your food uh
and you get a table, it's
old, right? Or
in our language, uh we can't save your
changes right now because something is
locked.
So
we should always lock especially limited
resources as late as possible.
Um,
think of a printer right if you are
printing a big report I mean let's say
that takes time to generate a report you
wouldn't go and lock the physical
printer before you are ready to actually
print right
uh then we also have the fun of the
deadlocks as you know um which means
that we need to lock in the same order
which also gets a bit back to the
McDonald's example.
So what we for instance do for GL is
that we try to post GL towards the end
of process. Um
so we lock GL as large late as possible
but sometimes we do it early because we
are you know doing different stuff in
different orders. Um,
so
that leads me to a short intro on
locking
and
you will um I know many of you know most
of this but I'll still go through some
of the basic scenarios. So in the UI we
rely on optimistic concurrency. So if
you read the code there, it's the same
code both um
blocks. So we read a customer, change
the name, and then we wait, you know,
just to let the other
um start, then we modify the customer,
and then we're done here, right?
So the other guy who opened the customer
card after will get this error saying
another user modified this record or as
our good UX people think this is a more
kind message. Sorry we just just updated
this page but it just means that
somebody else has updated your record.
So that's one scenario where we the one
we call optimistic concurrency. Then we
have the other we can call save
concurrency. Again it's the same code in
both except that this time we put an
update lock on the customer
and
you know user one gets to this um spot
and
you know user two because user one goes
for coffee or something, right?
Um, and it's working on it and
eventually a timeout,
right? And then but user one is happy
with his coffee. Then
we have
read isolation and it's something you
really should start using. Uh, we have
slowly, if you look at our code, you can
see we more and more sprinkle these read
isolations out. So if you look at
this one, first we update the name to
some to hello and then we modify it and
commit. So now the database says hello
in the name too and then we do the same
again where we write world and modify
but then we pause here. Right? So when
you get to that
here we have um
we have modified the customer
but it's not committed to the database.
So
on that one
right
um
we'll see so we read uncommitted
and what what do we expect that to show
world right because um that is the
uncommitted thing we just written to the
database but it's not committed
then we can use read committed
um And as you will expect, it will give
you hello because that's the one we
committed.
But there's a catch here. That's only if
you have set snapshot isolation level on
for your database, which I believe we
have in our
environments.
Um but otherwise
you'll actually get a timeout because
the read committed actually locks.
Um the platform tells me oh but it's
only for a short time. Yeah. But if the
record is locked I I can't get it.
So just a warning read committed may be
just as bad as update lock in many
scenarios
unless you put set on snapshot isolation
which is some tricky command you can
issue on the SQL server
then
you might remember that as soon as you
insert
something so now we create a new
customer with some it as a number. So we
know it's unique. We insert it and as
you may remember sometimes when you
insert we immediately
get this lock you know lock table thing
on the customer
and then we call this function where we
say get number of customers with the
same name
which is Canon and anyone who knows the
demo data would know that Canon is one
of the demo data customers.
So
this one set filter and count. the count
would actually lock all the
Canon
um
all those
um records but
we don't
uh and that's actually the you know the
new improvements we made for
maybe was 25 maybe or yeah 25 I think
was the tri-state locking and Also the
calc sums and count and so on are not
locking. So that's a good thing.
Then we come into updating several
records,
two processes. And in this case, both of
these do exactly the same just in
different orders. Uh here it's a
customer and a vendor, but could also
just have been two different customers.
So
right. So up here we you know update
customer one the customer and then we
wait and then up here we update the
vendor and then wait then do the
opposite.
So
we get there and then we make sure that
the other one gets there. Um,
so what do we expect
on number two?
Yeah,
we get a lock timeout.
And I guess somebody in this audience
would expect a deadlock, right? So why
didn't you get a deadlock?
And the thing is we did we did get a
deadlock. If you look in telemetry or um
the event viewer if you do doing it
locally, you can see that we actually
did get a deadlock with this ugly thing.
But we can also see that there's another
telemetry event that tells us that the
server was kind and detected this and
just retried the operation.
So these guys are actually saving us
from from some of our mistakes.
The last thing I regarding locking is uh
we can also get locks from sift and I
guess most of you know that but just
know that uh you should use sifts
carefully because I mean they're
expensive to update but they also make
retrieval of sums that's all very fast
and um
so a few versions ago we had this key on
our purchase line. And by the way, all
our sales and purchase lines indexes uh
are now only using included fields. So
we removed shifts from them to avoid
locks.
But we had this um index on the purchase
line. And I don't know if anyone can say
something was wrong about it.
Anyone? No.
Um
I mean it looks
innocent but on average what's the job
number on on a purchase line
it's blank right and job task number
blank or zero whatever type it is. So
basically this meant that for each
document type you know quote or invoice
or order it was a single user system
only one user could basically had a
table lock um
there. So if if anyone was posting a
purchase order um people couldn't edit
that was not good.
So
as you might know in we started a
journey in 25 and continued in 26 and
will continue
for further releases to try to make
things a bit more concurrent. Um in 25
we did with uh warehouse entries in 26
with inventory.
Bit more on that later. Um but one so if
we know that several people or process
are adding to the same table at the same
time maybe even on the same item is this
case right so we need some way to
distinguish
um the sifts so you'll see that some on
some of them we have added this sift
bucket number which is just
it could be anything could be a random
number but we um
chose to say that it's where house rich
the number modus five. So it will it
will always be you know 0 1 3 2 3 and
four
and then we'll come back to I'll start
on the
locking um so whenever we or
traditionally whenever we have entry
tables like up there bet entry ge entry
check ledger whatever
We do a lock table and find last, right?
But that means as you know that only one
person can post to whatever system at a
time and as much as we want uh our code
to be fast, the total throughput is also
important.
So
I mean if you've seen our um launch
event videos this is basically the same
um but just to repeat so the way it and
I wrote digit work it still works like
that if you haven't turned on
concurrence posting so some ledger entry
you know post whatever there's usually
some init function or beginning of a
procedure where where we do a lock table
find last. We save the entry number
which is a global variable and that's
it. Right? And then at some point later
we want to insert some ledgers where we
increment the uh entry number counter
and assign it to the entry number and do
stuff and insert.
Fine.
So
yeah and this means that only one
session can do it at the time. So the
way the ch change we did was that in the
init function I mean if you have turned
it on we don't do anything
but when we post we assign
a number for the um
uh for from the number sequence most of
the functions or most of the tables have
got this get next entry number function
on them and which will go and take from
number sequence which is think of as
these number dispensers at your bakery
or wherever you have these.
And the there are several reasons why we
chose this. One of them was that we
could leave the code pretty much
unchanged and you know all your events
would be would still work most of the
time.
Um
so
and as I hinted uh it's only if you have
turned it turn the concurrency on that
we don't do this right.
So what does that do to the to the item
register where you you you know we have
this from entry number and to entry
number and we have the from value entry
and so on. So there's these four tables
that are connected to the uh item
register.
As you can clearly see in those yellow
uh boxes, there are huge overlap, right?
You see that these processor were
started almost uh simultaneously.
So the way um the drill down works now
is that
we
still put that range on as you can see
there but we also put a filter on the
item register number which we have added
to the entry tables.
um since we don't want to upgrade
all the you know some of some people
have hundreds of millions of entries
that would take days to update right
so
we just left the zeros out there meaning
that if it's a zero it means it's an old
style
um entry and then then the range is
correct right and if it's a new style
then the
uh item register is correct, then it's
not zero. It'll be 102 in this case. And
then that will add an extra filtering.
And then we have this ugly stepchild.
It's called inventory. Um sorry,
automatic cost posting. So this is an
item journal I'm showing a picture of.
Um,
but it's the same for a sales order for
instance. Just think of the lines in a
sales order. So we for each line we go
and post to inventory
and if you have turned on automatic cost
posting we call out to GL and then we
know it's game over because
then GL is locked and we can't make any
concurrent
stuff. So what we did to solve this or
solve and solve amend this
is is that we collect all the ge entries
or the processing and we save it for to
last. So we process the ge entries just
before we process the other ge entries
we otherwise would. again about this is
about locking the critical resources to
the as late as possible
and
does it matter. So this is um a
screenshot
done on it's in SAS um it's not a pro
tenant but it's a pro like tenant. Each
of these two windows have 500 item
journal lines different items because
you know if you post to the same item
you get into this
uh remaining quantity and all this but
it does have automatic cost posting on
and
if I ran one batch alone I I didn't
repeat it that many times but if I ran
it alone it took you know 19 seconds but
ish
And if I ran both at the same time, the
last of them um because they don't
finish at the same time obviously um
ended at after 23 seconds. And again
this unscientific you know a few
experiments
uh but you can see that it's clearly
gives you a better throughput.
Uh, and I think even more important,
the second user didn't have to wait for
19 seconds before something happens,
right? I think that's probably the most
frustrating for people that they have to
wait, nothing happens, working on it,
you'll say.
Uh, basically the same for
sales invoices. Um,
I made this test specifically because we
also have customers who run uh
subscriptions and some of them those
customers use items service items as as
subscription um yeah subscriptions
and the good thing about that is that
they don't update the inventory meaning
we don't need to go and update the um
item you know incoming item let's entry.
So I create a lot of sales invoices, ran
batch job uh report
297 in uh job queue entry.
Um
and if you did one of them, it took
approximately 15 minutes. Five of them
took approximately 17 and a half minute.
which gives us a factor four.
Um, and it seems like it saturated
there. I mean, I also tried with two and
three and four, but it seems to saturate
around five. I also tried with 10, but
it gave approximately the same.
So
one last note on this specific topic on
sales orders is that um you remember the
talk about deadlocks. So if you have two
orders and one updates item
one and two and the other order updates
it two and one you'll get a deadlock. So
in the next version we are releasing we
will actually sort the lines by type and
number. Meaning yes we may get locks but
it will be in not deadlocks right locks
are better than deadlocks.
Um and then a short thing about how do
we test this? So obviously um telemetry
I mean we can just observe what is going
on out there. So we have a lot of live
experience so to speak in telemetry. But
if you sit if you develop and you want
to make sure that your stuff works
concurrently you can use BCPT
uh we have several
uh presentations on this. So I won't go
into much detail but in this case you
can see I had
um four sessions just thinking of it as
code run right. So each of these just
code run in in the background and they
post some post the same item some
different items.
Um and then then you can let it run for
minute 2 minutes whatever you want. Um
and then you can look at the logs and
then in the log you you might get errors
like that. Uh you can see that this
activity was deadlocked with and then
you can go and look at the call stack
and
call stocks call stacks that could be
something like that for instance um it
could be anything I mean it's just one
random example where we had updated one
item and then as you know if you don't
use the new modern um
uh read oscillation settings then you
get into a table locked. So the next
item you touch is also locked
because it's a global variable.
Um so what you'll see is that we
sprinkle some of these read uncommitted
over the code to avoid these kinds of
things. But this is good for debugging
and it's pretty easy once you set it up.
You run for a minute and then you can
see did I get any deadlocks? Yes. No.
uh similar thing with a lock timeout but
then of course read requires some
activity
um
yeah I won't get into details you know
about this so and don't read the code
there it doesn't matter but the point is
uh be my use these different read
isolation for different purposes so in
this case we iterate through with uh
where we don't want locks because we
don't want to for other people, right?
Only for those we actually want to
update, who want to lock
so yeah, I think that leads me to
Kim.
That's right. So, telemetry, it's simple
to use. It's critical. It can give you
really good insight into your business
or your code, what it's doing.
We are halfway into the session. I think
it's about time to raise a hand who is
using telemetry and I expect everybody
to raise their hand because everybody
should do it
and please keep it up. Who is using your
own telemetry in your own statements in
telemetry?
Okay, who's using verbose telemetry?
Okay, cool. So, um many of you know
telemetry. I will go through the setup.
It's really easy. I will go quickly
through it. Um, sometimes it's enabled
for by somebody else. You don't really
know how to do it. Uh, use it for your
customers. Use it for your own test
environments. You have your own reports,
your own uh, app inside storage that you
can use and test your own stuff. Um, and
then have a look at what your your code
is actually doing.
um you can use it for customers or you
can use it for your extensions. First of
all, you need an app insights uh
storage. Once you created that, it's
really simple. Just follow the guide in
in Azure portal, copy the connection
string in the tag, insert it into the
telemetry point here, and then you're
basically done.
So um
and also please don't share it the key
if you put it in your extension don't
and your pop uh um uh open source or you
can you share your code then by mistake
somebody could actually use your
connection string and then you get
somebody else's telemetry also in your
storage and you don't want that. So
here's a few tips how to set it up. The
first link is just a general help, how
to use it, how to set it up and all
that. The second one is brings you to
this page and this is the app that you
need for for PowerBI to show the report
of your app insight telemetry. Um it's
simple to set up. Just follow the guide.
Once you um you have it installed, it
shows a lot of demo data. Have a look at
that first. see how what report you
actually have out of the box then click
this link and then uh authenticate with
your own um app insights resource and
then you're actually running this is
just a new customer new environment and
I enabled it for that one
so if you do it for telemetry for for
your extensions you put it in the app
insights connection string in your
extension and then it locks all of the
usage
of your extension to this uh connection
string here.
So, and then a bit of uh it's it's a tip
for me. Um normally people use the data
explorer. I personally use the custo
explorer. I'm not sure if you're
familiar with it. It's a Windows
application. You can you download from
the the link here. Um,
I would say it's one of my favorite
tools. Um, and also F5 actually runs the
query. It doesn't refresh the browser.
So, it's really really good. So, have a
look, try it out. It also stores your
queries. Once you close the brow, the
you you open your laptop, your Windows
will restart your your PC. You open
Custo again, your query is back where
you left it. So, really nice.
Um, in order for you to set up custom,
um, you need the resource ID in your app
insights resource, you prefix it with
app insights URL and then inside the
connection string, you you just add it
and then you have access to it in your
custo and then it looks like this.
So your own telemetry this is two
statements I did here. The key is uh the
tag. You can see I called the KCK00001
and two. And then also the scope. You
can see the first one is all and the
second one is extension publisher. That
means that the all goes to both the
customer and your extension telemetry.
The second one only goes to the
extension where the code is executed.
Um there's also a dimensions. It's not
that important in this case. Also be
mindful what you log. It could be you're
actually violating um privacy aspects.
So uh so do be be mindful of what you
actually lock.
And this is how it looks if it's the
extension that you see. You can see
there's the all and there's the
extension publisher, right? And if I do
the same for the customer storage, they
only see the the all event.
So then the verbose part you can do that
your own you can create your own system
and then put a it just used normal but
you can also use the verbose tag and
then
on the page that B showed earlier you
can use this and enable additional
logging then for that session from now
on it will lock the bow statements also.
So if you look how that would look you
can see here I have the uh the customer
and it gets two of the normal event to
all and then in the same session I
enable verbose and now I can see the
verbose statements when you create a new
tab it's a new session and then the
verbose is no longer active so it's only
for the reminder part of that so you
could also say if you have a repro or
your customer has a repro of an issue
and you have a bow statement, then ask
them to repro it again after they enable
it. Additional logging and then you can
see a lot more details depending on all
your lock statements. So um please go
ahead and do that.
Yeah, that's one way to to save money on
uh on telemetry is to to make sure you
only lock the important stuff always and
then lock the the the stuff you need for
specific investigations as Bose and then
you can enable it then you don't have to
to pay for all of the stuff all the
time. Yes. And I will talk a little bit
about some new features that uh that are
helpful for improving performance. Um
for 25 we shipped uh optimized for text
search which is our name for the SQL
full text feature. Um it's something you
can we have opted in for a number of
tables in the base app. Um mainly master
data tables. Uh you can also opt in on
your own table extensions on your own
full tables. Uh and you opt in per field
and it's not like a normal index where
you have there's a specific order. you
just apply to the field directly and
then you can use the index in any order
in any combination of of of fields. Um
so when you have an optimized for text
search uh field uh previously you would
like from the search from the client it
would just turn into a SQL like
statement with some wild cards and that
would force SQL to go through all the
data to see what matches. The moment you
enable optimize for text search in and
then query from the client, we will
automatically turn that into a full text
uh contains statement. And what that
does is it it builds up a list of words
instead in your uh data and then
searches the word list first and then
cross references that with like what
words showed up in what lines. And then
you will be able to more quickly
navigate to specific lines in the data
without having to scan through, for
example, 200,000 items or however many
rows it is you have in your data set,
you can instead go directly to the to
the correct uh rows based on what what
rows contain what words. One small
downside to that is that because it's a
word index, um it needs to it it can
only find words that start with a
certain thing. So if you have chair and
hair, you will not be able to find hair
based on chair because it does not start
with the same letters. So that's a
that's a downside. It's not free. It
doesn't it's not just better. It also
has some downside, but that's a it's a
compromise. And and and for most cases,
when you just type in the the item
number or whatever uh thing you're
searching for, then it'll be much
faster. And then if you have a specific
scenario where you need to search for
something that doesn't that that ends
with something you will need to either
use wild cards or switch back to the the
previous way of searching. Um
in the web client it looks like this. So
if you have a table where it's where you
have opted into optimize for text search
you'll get the small arrow and you can
select the modern search instead. Um and
that will then have the the the new
behavior the the faster behavior. You
can also switch to modern search and use
your own wild cards like put asterisks
in front and in the back or in the
middle. Uh if you do that then we will
man automatically figure out okay can
this be done with full text search or
not. If it cannot then we will convert
it to the to the old style. Of course,
the performance will go back to the old
performance as well, but it means that
you don't need necessarily need to
switch back and forth between the two to
have the fast behavior and the slow
behavior. Um, you can just add wild
cards yourself and then you'll see okay,
can it be handled one way or the other?
And then we'll try to do the best way
automatically. Um, so then you don't
need to switch all the time. If you have
a scenario yourself that is uh you want
to do the same thing what you see in the
client from your code um you can do
something like I put in the in the in
the code there like filter group minus
one you know and then uh you set up
these filters the same way as we do
them. It's a slightly uh convoluted
syntax with a double ampense but the re
reason it is that is because we have to
pick something that isn't in use already
because uh we don't want to break
existing logic. So we found something
that we can guarantee is is not already
would would not break existing logic. So
that's the that's the syntax we went
for. Um
yes.
So performance. So this is just I picked
one example from production. Had to find
something to see how how was it going
after we wrote this out. So I found one
that had um had previously before on 24
used the wild card search a lot. So they
for a normal Tuesday they had 5,000
queries that took longer than 750
milliseconds. Um so that that was that
was not great for them. Um so then we
upgraded them to 25 and we could see
that the next Tuesday after the upgrade
they were and um fac factor 10 less uh
of of the of the previous style queries
legacy queries that was either tables
that were not converted to optimized for
text search or people that manually went
back to the to the old style search and
then five slow modern search queries. So
the 4 and a half thousand queries no
longer showed up to of course I cannot
say we we only lock queries that go
beyond a certain thresholds. The ones
that are below they they don't show up.
So but we know we can at least see that
a lot of a lot of queries were much
faster after this. Um of course it's not
all great. I already mentioned the part
with the with the starts with versus
contains. Um
and uh the other thing is that uh you
have in full text it's a normal
challenge for it's not a specific
challenge to full text search. It's in
general that every time SQL has to
evaluate a query has to decide whether
which part of the filter is the one that
is most relevant to do first to cut down
the amount of data to look at. Um, but
it's especially important with full text
search because if you choose to not use
the full text index, you are back to the
like the same performance you had with
the wild cards actually sometimes even
worse. And what we see in some cases is
that that some queries decide ah this
the full text search is is not optimal
here. For example, if you search for a
single letter, the query optimizer has a
tendency to say probably not a probably
no reason to use the full text index
here because it's going to give you too
many records. So I'll just use the other
part of the filter. For example, in this
case, if I have a item that is that's
that that where something the
description is chair and it's not
blocked. If if you have that case, then
if if you are not lucky and and SQL
decides to pick that I'll I'll start by
getting all the ones that are not
blocked and then apply the full six
filter, then you're actually slower than
you were before. Um some of this we have
been able to mitigate ourself because
some of it is is huristics in SQL side.
So if you do find first and a full text
query they think ah there's there's no
reason to use the full text search here.
So good thing good if you need full text
uh querying then it's good reason to use
like get all the data or get the first
50 rows because then it is then it then
that that pokes SQL in the right
direction that says you need more data.
Okay, I should probably use the index.
But this is some of this is
experimentation and figuring out how
does the query optimizer look at the
query and decide what to do. Um this is
at least one of the the tricks we found.
Um yeah uh another thing is that um
there's some overhead like you probably
don't see this um but uh um adding more
full text search indexes especially when
you have many companies like 300
companies 50ish full text indexes I
think we have in the base app today you
also added for table extensions then you
have 30,000 full text indexes once
everything is running not so big a deal
but we have seen at least cases where
you have to when you have to stop and
start the SQL server for scaling
purposes, convert from a like one tier
to another. It needs to do manual
processing on each of those full text
indexes and that takes time. So there's
a if if you don't have enough data to
get benefit out of full text, there's no
reason to add it like keep using the
wild card statements. It works well
enough for small tables.
Um then another feature that we recently
added in 26, it's currently opt in. So
you need to opt into it is to calculate
only the visible flow fields. Um
before any flow field even if you had
specified manual visible false I will
never see this we still calculated. So
we fixed that uh currently opt in. So
you can only calculate the the visible
ones. There's a small uh detail is that
you have some fields if you put a field
in a group in a in a page you can flip
back and forth between whether it's
visible or not depending on the data and
in that case we always calculate it
because we cannot halfway during the
page load decide oh now it's visible now
I have to go back and calculate the
values so it's only stuff where you can
detect as soon as the page is open this
field will stay visible or stay
invisible then we either calculate it or
not if it changes during like after the
page has opened then we unfortunately
forced to calculate it still but the
most most fields either stay visible or
stay invisible. There's not that many
that go back and forth because it's also
jarring when you look at the UI to see
fields that pop in and out. So doesn't
happen that often. Um this is an example
that just like what I mentioned with
like if it's false, if it's true, it's
easy. If it's decided when you open the
page, it's also easy. But in the in the
case where it's part of a group, you can
see here that the the the one at the
bottom, the visible group there, we need
to to always calculate it. Um
then a small sneak peek on what we're
doing in 27. Um this was almost done for
26 but didn't make it. But uh if you
look at something like chart of accounts
and other other pages, you will see that
they have there are many calculated flow
fields and a lot of them look very very
similar. And that's also what I saw when
I looked at this and like why are why
are these so similar because I'm don't
do much application lo code
um and they are very similar and and
what we decid disc found out is that why
not just combine all of these. So in
this case you can see here it's the um
it's the credit debit fields on customer
ledger entries like there's the the only
difference in these they have exactly
the same uh filters exactly the same
source table. The only difference is
what field are they aggregating. So what
we're doing for 27 is that everything
that has exactly the same filters and
exactly the same source table we're
grouping it. Um of course there's some
operators that can be grouped and some
that cannot. Um, so exists and lookups.
If you're doing lookups and exists from
the same table, we can group those. If
we're doing sum, average, and count, we
can group those. Um, if we're doing min,
max, we can group those. And if you look
at the if you look at the query plan
here to the right, you can see the top
one where we had the four the four
different flow fields from exactly the
same table. They were going to they were
doing four joins and uh four sub queries
to calculate e each of those. And if you
look at the the the bottom query plan uh
with the estimated cost of like 70% less
is uh it's a single out apply single
single join um to calculate all of those
four aggregated values.
Yes. Over to
sound I guess. Yes. Sound is on. Uh 20
tips in 20 minutes. There's a lot of
things that over the past has uh people
learned how to do the things but we
think there's something we really want
to reiterate also. So let me start with
the first tip and BU actually mentioned
part of it before. When we run AL code,
we actually run a compiler on top of it
and we emit some C# we compile C# but
actually to you know to do all the nice
things you see on telemetry to enable
debugging for you guys we emit code
around uh every statement. So if you
have a something that is heavily using
uh al statements it could be something
low-level JSON calculations plus one and
all these kind of things really consider
when uh you want to have really small
methods because inlining doesn't happen
because we have try catches in our code
we have uh using lambdas and other kind
of things. So we we will never inline
things like that. So if you are coming
to a point where you have really small
things consider sometimes do duplicates
add them directly to your function calls
because there is an overhead if you're
only in the microsconds range uh but you
know you can make you can formance tune
the very low-level stuff here and when
you do parameterization on functions as
well also the AL language u will copy
you unless you are by var. So if you
have complex types that you put into a
function call like a record do by var if
you know you know there's no risk of
people will hurt you on the inside if
you're the only consumer of it because
then you don't get copies of objects
there's always when you are heavy on
these levels we have a lot of the weight
times that BA talked about uh but this
is where you actually hurt memory on the
machine so if you you know produce a lot
of things then you put things to the top
of the garbage collector so don't do uh
in inline your own code because we don't
inline it for you because we always have
to add
uh the overhead calls. This is one of
the ones that we added to query save as
JSON. Uh it has the save as CSV and has
the save as XML already. Um if you
handle a lot of JSON, you often pile up
lot of things make big big pieces of
memory. This one is a stream aware and
it means that it will take your you know
make your schema as I would already on
any other query and then you can you
know uh in a streamable fashion actually
create big documents without putting
pressure on the machines. So performance
wise you will um
uh get it much faster out and much less
pressure on the machine.
Yes. And then uh B also mentioned this
that that it's it's not free to call out
to SQL. So what you can do is do
whatever you can to reduce SQL round
trips. And one of the thing is that I
just mentioned about autocal fields. If
you do autocal fields, you can you
inline all the calculations while
getting the data. So that means less
trips back and forth to SQL. Um you can
also do query objects of course to to do
the aggregation inside SQL. Um meaning
you don't you only have to go to SQL a
single time and then you get all the
data and all the joints and all the
aggregations at the same time. So
whenever you have stuff where we can see
ah here I'm summing in al think again
see can you do this with a query object
also even the calc sum is is also does
the same thing it offloads the
calculation to SQL and you don't have to
pull out the data to the NST look at it
all throw it away again just for the
aggregation there's only one small
exception to the rule is that the best
trip to SQL is the one you don't do so
if you have something there you that you
can see you requesting often with a get
request for example, those are very easy
to cache for us. So get requests almost
always end up in the cache and can get
reused later. So in that case, if you
have something that could be done with a
query or a get request, a get request is
always preferred because that one goes
to the cache and the query result does
not. So then you skip the round trip
completely. That's even better.
Then use the right type of find. Um if
you don't need any data, you just need
to know if it's there, then is empty is
great. You don't you're not getting the
data. You just know SQL can stop as soon
as it detects that there is data or then
then it can stop and say yes there is
something fine. You don't need to get
the data. You just need to know that
it's there. Find first. If you need one
result just one then find first is
great. But what we often see is that
some people do find first and say great
there's one result and then they call
next but find first gives you one
result. So the moment you call next you
need to call SQL again and say hey I
want some more data. You don't see this
but you have to pay for it. Um find
minus if you want to do find first but
50 results instead find minus is going
to give you that and if you want to do
use everything then select is uh uh find
set is going to give you all of that. Um
one thing to know get versus find first
get find first with a filter on the
primary key automatically gets
translated into a get request. So it
it's not critical whether you do one or
the other. we can detect that ah this is
you you are all using all the primary
key fields we can just convert it for
you
then B talked a bit about indexing the
the fastest you can do as I mentioned is
the get like it's primary key look up
you know exactly where to go in the data
uh to find that data the seek is the
next best is when you have a key that is
tailored complete to your query you have
all the all the set range and the set
filter fields are in the key in the
right order then uh you can seek into
the index which is The second best index
scan still good. You can you can get the
data from just the index to figure out
what to um what to find. Uh even though
it's not the right order or you don't
have all the fields in the um yeah you
don't have all the fields in the right
order or in the in the set range then um
then you can still uh do the query using
just the index. But the moment you do a
search on something that is um not in
the index at all then you need to go
through all the data and that is fine.
If there's not that that much data, you
don't do the query that often, fine. But
if you have something that needs to
perform and you need to go through all
the data, yeah, that doesn't work great.
Um, iterating data efficiently and
especially modifying data in loops. So
of course we have some bulk operations
in business central but if you need to
go through data and modify it in loop or
even just go through it in loop the
moment you start changing the filters
changing the set load fields changing
the autocal fields after you called find
then we have to restart because we
didn't get the data the first time and
now we say you need more or less or
different then we need to issue the
query again. You just call next but we
actually have to reissue the command.
Avoid set current key on the future
you're modifying. Set current key
changes the order and if you're changing
the values of the that are part of the
ordering then you're actually moving the
cursor around. So the moment you call
next after you change the value then you
say oh but you're now the the value
change from one to five you want the
next from value five. So the it you
should not sort by the stuff you're
modifying it. It's it's not great for
anything. And then secondly, when you we
try to be smart with not starting over
too much, but if you copy the values
around so you you have one record
instant that that you'reating over and
then you copy to another record and then
perform the modify over here then we do
not the link is cut between the two. So
we don't know we just see something
changed. So then you also end up with
more restarts than it necessary. So do
the modify directly on the record you
are iterating or the delete if you're
deleting that is that will give you the
best performance when doing loops and
modifications.
Yes
all the way back to cite the way to
collect uh big amounts of data was to
copy from record to a temporary table
and then use it for a later iteration
and get your data out of it. It is a
pretty heavy operation. We use a memory
database behind the scenes so everything
is piled up. So if you copy a million
records, you know, it will all happen to
be in memory on the machine and you put
a heavy burden on it. And performance-
wise, it also just takes time. So we
added some of the native types. So use
if you need it's just key value pairs or
some other structure that you would like
to have saved, use the dictionaries. If
it's just a matter of getting a long
list, use the AL list. They are behind
the scenes just uh ordinary uh net
objects. Temporary tables is just heavy,
but use them when it's when it's it's
convenient. it has the you know the
insert the update and you can search on
them and so on but they are in memory
structure and they they are pretty heavy
on the machines so don't don't use them
unless they have the purpose of being
the uh a record behavior that you want
right now
uh we made a new feature called set load
fields and that is you know uh similar
to the code before you know the the code
you don't load the the calls you don't
call uh you know is always faster than
than not not getting the data So if you
do set load fields, you can ask for
specific fields to get loaded. If you're
in a scenario just know like let's say
you're filling up a dictionary, you have
like uh the key that you would like to
get added and and some other values that
you would like to have piled up. So
instead of running some of the big
tables where we have like I don't know
50 100 or something like that columns on
the tables. It's just a big waste to
take uh the records. Records is based
you know. So we load them in and you
next and your next and your next but you
only need a few fields. tell the system
up front I only need uh uh some specific
fields and then you know your iteration
will be much much faster and the cursor
in the SQL server will be much uh
smaller for you and uh uh
yeah so you use that all the time and
especially you know skip skip out uh all
flow fields if you don't need them as
well also in the same run uh here's
example from the documentation the link
to documentation is in the bottom and
you get the the PDF afterwards with all
the presentation this could also have
been a sum index the sample from the
sample page but uh yeah
and then uh this is specific tip to
upgrade because data transfer is is uh
only available in upgrade but we still
see upgrades failing uh taking hours uh
and then we go look at what was actually
happening and we can see it's just
looping over hundreds of thousands of
records and maybe the code was written
when there wasn't 100,000 records but
now there is and it's not performing
performing anymore. So every time you
write uh upgrade code where you need to
transfer data or modify many fields and
you don't care about the triggers
running, use either copy rows or copy
fields, it can handle both within the
same table from different tables. Uh
conversions also if you're scaling up
like from integer to big integer or some
other kind of migration uh that this
will handle it for you and you're not
running triggers. You're only going once
to SQL. Um, so it's going to be much
much more efficient. Um, and it's going
to help both you and us because you want
to get upgraded, we want you to get
upgraded. So, please
remember we upgrade you every month, you
know, so it's not like in the past where
you had to struggle with these things.
We we do we do it all the time and it's
fast normally.
Yeah. And then uh a specific tip for
pages uh both UI pages but also um API
pages is to limit the use of on find
record on next record. I'm not saying
you shouldn't use it because they
definitely have their use cases. For
example, matrix pages, you cannot do
that without these triggers. Um but if
you have a page where it's actually
bound to a single record, there's
nothing complex going on. It's just
convenient to use these two. consider if
you can do it in a different way because
we have to like we like to do
optimization see oh could we skip this
query could we do this differently but
if we call out to al and do something
and you do something you take control
you decide what how to fill up the
record then we cannot assume anything
anymore so then we have to be very
defensive in what optimizations we apply
so if you don't need these then then try
to do without them um but it of course
if you have a scenario where you can't
do without them use them but it's just
something to be aware of they have a
cost.
Yes. Uh B mentioned before that the
visibility of a page is actually super
important for you. So when you make a
design for a page, uh in the top of the
page, put the the important information,
the things that you can show them fast
because we we delay load the the
structures. The things you don't see on
the screen right now, they're not there.
If you have a fact box on a screen, if
you close them uh by default, so people
have to open them, you don't pay for
their performance and you have your
first first time to impression for the
user uh uh getting access to the
screens. So really consider what is
visible by default and what do you have
to trigger to get visible, you know, if
there's something really heavy, you
know, put them below the page and not in
the top of the page because then, you
know, they will be loading it and then
at least they'll have like a responsive
UI so it looks like, you know, you're
not waiting. So everything is delay
rendered similar to if you go to a long
list page you know we load the first
fast 50 and then you know we scroll then
you get some you know uh gray gray in
the middle and then we load the next
data this is running all the time uh the
browser is a you know a browser
JavaScript client so it is working like
uh uh it's not not just HTML you see on
the screen it's actually all the time
pumping data showing the things on the
screen asking for them explicitly when
you want to see Um
uh so what you can do is uh if fields
are not visible source expressions are
not executed. So if you change your
behavior from using an afterget record
which you did in the past where you put
uh your your pre pre-calculated values
for some kind of fields you did that in
code. Instead you can uh yeah it's
easier to see on this screen up for you
guys. If you add a function directly at
the source expression level and the
visibility is false that means that your
functions will not be called. Uh here we
have like the running balance a pretty
uh heavy calculation. So if you can
avoid having that one on the screen on
calculator if you don't need it you know
uh add your uh functions directly to the
source expressions then they will not
get evaluated instead of using on
afterget record which is called no
matter what because that happens as soon
as your record has been executed.
Yeah.
All right. And heavy stuff as I told you
before in the UI, if you have heavy
stuff, put to the background task.
Background task, you know, you get a
responsive UI by getting uh the serial
serial execution and the first get data,
then you have your your screen up and
running. But as soon as you need
something behind the scenes, let's say
you want like a
web service call or you want some heavy
calculation behind the scenes, do them
in the background task. The UI will come
afterwards and update on the screen as
soon as the data is there and the user
will have access to the screen and can
start doing the typing uh while data
pops in.
Yes. And then I mentioned before the
bulk operations. So we have a we we have
modify all and and delete all NVC. But
the problem with those is often that
they are only bulk. They only look bulk
on the surface. But the moment you add
uh add and run a trigger or global
trigger or define a database trigger,
subscribe to on before after events, add
security filters, add media sets to the
field or to the to the record, then we
can no longer make these bulk
operations. So the code is still going
to look like it's a bulk operation, but
behind the scenes we go and say, "Oh,
but you subscribe to these things or you
want to run the triggers. Tough luck."
we'll need to go row by row. So if you
have a table where it's important that
you can insert a lot of or you can
modify a lot of data quickly or delete a
lot of data quickly then avoid adding
these triggers or avoid uh defining
these subscribers because you are you
your you your code will still compile it
still look like it's a bulk operation
but behind the scene it is no longer a
bulk operation. So it's it's important
to keep in mind these rules. Of course
this list used to be longer. There used
to be more things that would block bulk
operations. So we try to see can we be
smart and say still allow them. But for
example triggers we will never have a
way to to do bulk operations and still
run your trigger for every single row.
Simply not possible. We need to read the
data to to run the trigger. Um yeah so
that's just something to keep in mind.
If you have if you want to be sure you
call your bug can use your bug functions
then don't do these events and triggers.
Small promotion for telemetry also here
because one day it might work for you.
you're running fast and you know
tomorrow it's not running fast anymore
that most probably is some other
extension is subscribing to one of the
events and that will also trade. So it's
not always you it's the companion all
objects together that actually does it.
So you can go to telemetry analyze if
you have these kind of situation and
actually realize that someone else
actually ran code uh on top of something
you thought would be fast also. Yeah.
And then uh on open company uh should be
kept fast. It's uh of course if you sign
into the web client first thing in the
morning and then stay signed in for the
day you probably don't feel it too much
but what you don't see is that every
single child session needs to open the
company every single background job
needs to open the company every single
API request needs to open the company
and we have some customers that say but
the the API request needs to be xund
milliseconds but that doesn't help if a
open company takes two seconds because
you need to query some external endpoint
or some other thing to verify if they
have access or or whatever it you put
into open company. So this is it's it's
important to keep this one fast and also
do stuff that is has a a like a known
performance like if you're calling a web
service endpoint that is sometimes fast
sometimes slow that will hurt your
unopen company if you put it in there.
So try to put it somewhere else or in a
background job not not as part of the
unopen company because you are paying
every single time you need to log in
both from interactive session and and
background sessions. Um you can if you
have something that is important to run
but actually only when the it's a user
that uses the product directly then
check the client type in an open company
and do the expensive stuff only when
it's actually needed. Uh then you can
make all your keep all your API requests
fast still for example.
Yeah a good classic one that is uh been
a long hassle for a long time especially
in uh in the managed world with both
Java C# and so on is string
concatenation.
If you concatenate strings, you have a
lot of allocations. And if you just take
one string plus another string, then you
have the two strings and now you add
them together. Now you have a third
string. If you plus some else other
string to that one, now you now you
throw away the old one and now you make
a new allocation and get a big one. So
we added the text builders which is the
same as the string builder in C# to to
the language because here you can now
append to the strings instead. It's a
buffer based meaning that you get you
know an an amount of capacity when you
start and when you cross the buffer size
then we double it and give you more size
at the end and it's it's much much
faster especially performance wise but
also memory wise uh we have some memory
graphs but I think we're too detailed
for the screen here but you know the
whole point is that you don't allocate
very often you just append to an already
allocated string then buffer that is
laid out for you but if you start doing
like big strings and you see it's like
it's growing it'll be even more stale if
you go uh higher up because it's simply
just wasting memory and it's putting
high burden on the garbage collectors
which forces you know one of the crucial
points when we monitor machines how much
pressure is there and how many users and
tenants do we want to have on a
particular machine when we balance uh
the memory usage uh friend of the other
triggers you know if you have users
waiting you know don't don't do
synchronous HTTP calls uh synchronous
HTTP calls is unpredictable you said
before you know sometimes an API is 50
millconds it might be fine the user is
waiting but you know someday the
internet you know stops you in a gateway
somewhere or the machine is uh not ready
to respond to you and it takes 5 seconds
or 10 seconds or something like that and
your users waiting so don't do HTTP
client calls if you can avoid it if you
have a button saying get data from
somewhere yes then then you you do it
but else you know you make it make it in
a background call make a background
session uh call it on a page background
task. Um really consider when to cach
it. Do I need to call it always?
Sometimes it's easy. You think hey they
usually answer me fast but you know the
value is the same in the next hour but
you know then maybe c your values
locally instead of calling out. It's uh
it's unpredictable every time you are
going out of pro process uh to uh
acquire your data. So be mindful of
triggers. every trigger is someone you
waiting for you guys
and it's most often the user unless it's
a background task of course so avoid the
synchronous HTTP calls uh if you can
this is a request for all you guys you
know we we have we introduced events
many years ago integration events uh we
have 22,000 events today uh looking at
some of the big ones that really has a
lot is code unit 80 520 20 events is in
a code unit lately. It's cluttered all
over the the place with uh uh new
events, people getting added. Some of
them I think is because it was easy to
have a code customization somewhere and
then just ask for an event where it was
appropriate for the code customization
to get your events in. Please use try to
look at the events we already do have in
the system because you know if you don't
if people are not subscribing to the
events it's you know it's it's still a
method invocation for us to realize oh
there's no subscribers. Okay, we can
skip it and we can continue on it. But
changing the code uh let me just give
you an example here. This is uh the most
heavily used uh event hooked method in
code unit 80 check sales document.
There's eight subscribers inside 83
lines of code you know. So someone that
need to do a feature have to refactor on
it you know make something smarter it's
impossible you know and most of these
events are so specific that I bet you
that they made for someone that needed
like uncheck sales document on after
calc should check item charge they are
so specific you know please sometimes
you know consider making an event and
make the event good for more people than
just you also so we we have many places
where it will be even better to make a
pattern of it you know with 22,000
events incoming. We can't spend days on
realizing you know is it okay this one
you know should we be throw away the
ones that uh is is you know uh hurting
things and all all the other kind of
things but simply you know put more
effort on before asking for events it's
uh it puts too much pressure on it uh
think about how you get your hooks also
uh we have a tendency that we always
pull for things so we just ask you know
on an API is time stamp larger than X
and and and and and the patterns
compared to the push patterns
is my going out. Sounds like from me
that uh soundless going in and out.
Just stand still. Yeah. Okay. All right.
But web hooks, you know, get get, you
know, if you have need to get data out
of the system, don't puddle on the APIs
all the time. We have way too much of
these things that just end up in they
end up in the cache but you know they
having a full thread take over on the
machine. Uh you know ju just to realize
there's no new data for me. Uh use the
web hooks. There's a documentation for
how to subscribe to them in in the
bottom of the page here. Then you get a
notification on data changed and then
you can afterwards call into the system
and do your changes. So pile up your
work, you know, get a notification when
you need a reaction and then afterwards
call whatever you need because now you
are in reaction based uh mode rather
than just, you know, all the time just
saying uh get data, get data, get data.
Last line. Yeah, last slide but not
least. U select latest version. There's
actually also a new change recent. uh
previously this one uh the way it works
is that that says to the to the data
cache in the NST is that don't give me
anything that is cached uh earlier than
this specific that the current time and
this was for all tables. So this means
that if you put this in your code then
everything you read from the cache
before we just say oh disregarded. So it
means that uh you have to start reading
data all over again, which is probably
what you want for a specific table, but
like how often do you want to say I
don't care about the cache for every
table inside the product? Not very
likely. So now if you have this in your
code, go to the code and see okay, what
table is it actually that you want to
have a fresh copy of and put the table
number of that table in. An example of
this is that we uh actually had put this
into the login process without a table
number. Meaning every time you signed
in, you said everything that is in the
cache from before I signed in, don't
need it. So it's quite important to when
you use this function, ensure that you
put the right table ID in there and and
make sure you you you only query clear
the cache for that one. Um we should
probably do a compiler warning for that
one if you still use the old one. Note
to self.
Yes. All right, we have questions. Yeah.
55 seconds for questions.
I was told something new today that you
should not use procedures if you had
smaller amount of lines in that
procedure. You said there was an
overhead. Yeah, there is a but for
telemetry and or what it's it's it's we
have to like you saw I think we
mentioned before that we have the like
if this um if function takes more than x
seconds emit telemetry that means we're
not emitting the image every time but we
have to pay for start monitoring and
then at the end we say oh did it go
above the limit so you have to consider
that that we have to do that measurement
for every function so that's a that's a
trade-off with provide good telemetry
versus uh fast execution of functions.
So that's uh that's that's what we mean
with with this. Yeah. But the problem on
the other side is that you have a
duplicate code. Yes. And it's a
trade-off. We know. Okay. But it's if
you have a oneliner that just does some
single thing and and then you only use
it in one place. But how much is the
overhead do you think? If your
neighboring method is a database
operation, then don't care. It's where
you if you do like mathematical rhythmic
stuff you going to do heavy calculations
that requires your CPU. That's where it
benefit if your neighboring function is
you know an insert and update don't
care. Okay.
Can I take it? Yeah.
I have two question. One of them is
about uh reading on commit data. How we
can trust it? Because there is no
guarantee that the first transaction
will successfully finish. So if you have
two transaction and read the uncommit
data on the second one and the first
transaction failed and roll back what
will happen for the second transaction
because you already read a data which is
not valid.
Yeah that that's bad luck. I mean that's
how it is. What is the reason of using
the read on commit because there is no
guarantee for the first one which will
be finished successfully.
But you but that is true but we also
absolutely but we also don't want locks
right. Yeah but I mean and maybe I mean
if this transaction does go through then
that is the new correct value. I mean we
have this discussion in
uh item availability for instance right
we people are posting and so do we have
seven do we have eight bicycles on
stock.
So if another process is in the process
of selling right it a subtracted one and
I'm also
which is the most likely number once I
finish
I mean either could be good it's also
like I totally get it you can also
design it so that you like you start by
reading uncommitted then you like as B
said delay the locking right then you go
all the way to the end and then you say
now I need to read the committed version
and if everything is is well nothing
changed in the meantime then I can go
ahead and commit otherwise I'll have to
fail or I have to reread it again or
some other way. So you can use it to do
this kind of optimistic situation where
you start by reading uncommitted then
you do as much as possible before you do
the like read the committed values in
the end instead. So you can use it to
get kind of full control. We also use it
for cases with the job queue where you
need to like you want to know the state
of the job q but the job q updates the
records for itself right? So you need to
you you want to be able to read the
status of something that is in progress.
So that's like you don't care if it's if
it's being changed right now. You just
need to know like what is the current
status without locking and that's very
useful. We do that sometimes where we
first read it with uncommitted just to
see is it there is and then if we need
to do something then we lock it and read
it again. And 90% of your cases you are
you know the viewers doesn't notice if
it's actually you know because they
don't most often the transactions is
committed. It's seldom most selen that
you do not commit your transaction in
the end. So most often it's just an
observer browsing by from list to to a
card and then things on the card would
appear but you rather have a responsive
UI than them being locked out also. So
it's it's up you it's trade-off. It's
optimistic concurrency. Sure. And the
second question is about set load. Okay.
If you just load some field and then do
modification, is it going to update
field by field? What would happen for
the field that you didn't put inside the
set load? Like I mean you put customer
with set load name and then you modify
name but is it going to only modify the
name or will overwrite name to with
blank? Oh no, it will only then it will
only update the name. Okay, thank you.
and the you know last modified by user
and time and all that. So sure you'll
see that we we always load these um
these extra four fields we have at the
end systems set field will also expand.
So if you actually only ask for five
fields but you incidentally use them by
giving it to another function and you
didn't expect it then we will just
expand the cursor and not do another SQL
round trip and you know discard the set
load field for for that round trip. Uh
uh actually I have a question regarding
the deadlock and now the system is
actually retrying. So if you have
deadlock then they will actually retry
one of the sessions and one of the
session will gets completed. So the
first question is like if there is a
deadlock the screen will be freeze for
the user and how the UI will response in
the case of deadlock because afterwards
the system will retry those transactions
and what will be the sequence of the
transaction both the transaction which
created the deadlock will be retrieded
or only one of the transaction will be
retrieded and another transaction will
be failed. Yeah. So
I'm an app developer like you. So, but I
know that this server has um something
called I think it's called transaction
scope and some some of them are
retriable and some are not. So, if they
deem that it's retriable then they try
again if it fails for for instance a
deadlock.
That's like your overall. Yeah. So, you
have to be a transaction starter that
there's different conditions that will
make sure that it's solid to do it. Uh
so I think if you already have a stalled
then you're ending up in a real deadlock
and it can it has to be you restarting
points and we decide in the code when
the restarting point are. Yeah I dead
deadlocks usually happen immediately
right the SQL server detects a deadlock
immediately. So often it will happen
quickly and then it retries and then if
you get into the normal lock as you saw
in the example and then the user get a
lock timeout after 30 seconds.
I think we're over time, but maybe we
should. We have been over time for a
while, but we will uh we're in the
experts corner. So, we are in the bar.
Ask us. Oh, sorry. Thank you for
attending.
Thanks.
