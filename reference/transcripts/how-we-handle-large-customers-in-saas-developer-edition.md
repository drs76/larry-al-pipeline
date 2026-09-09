# How we handle large customers in SaaS: Developer edition

- **Source:** https://www.youtube.com/watch?v=H2P7WzrxxP4
- **Video ID:** H2P7WzrxxP4
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 93m30s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

Ladies and gentlemen, welcome to today's
second session. Please give them a warm
welcome for our next speakers, Stefano
and Diligo.
Microphone
testing. Perfect. Thank you to everyone
to be in this session. I think we have a
lot of people here.
Uh this is the session about the giant.
So the goal for this session is to uh
talk about the what some of the biggest
customer at least in business center
online today and we want to show you
some tips and uh tips and tricks on uh
techniques that we have used to handle
such type of customers that as you can
imagine are quite different compared to
small customers
together with me and together with me
there are the ducks and dilio of course
uh so let's start with just a little bit
of fun. So this is X-rated and uh just
uh to emphasize the bad habits. We just
pick it up. Uh just one single quote
that you're all so lucky that I do not
own a dragon otherwise you know what
will happen if uh you apply bad
practices uh that I I can invoke the
typical Draaris. So everyone you see
this light you can even uh use your
lighter or say Draaris or stay silent
whatever you like. Every time it appears
is something that you should never do.
Exactly. And remember you're lucky that
I don't own a dragon. Okay. So large
customers first the definition what it
is a large customer. So what you have in
mind as a first things as a large
customer what you might think it is a
large customer. Maybe it is the database
size. So the first things I believe
everyone has asked how it is the
database size like like saying okay this
is really large but okay you might have
in uh in the online version something
that it is one terabyte but you might
have just two transaction per day
because people just accessing and
looking at the data. So this one it is
green grass it is not so complex to
achieve. So database size it is just
another biases. The second things that
you ask look at this audience you ask
for a large customer you think that it
is the number of users number of user it
is just another bioet estimation of
something that it is different so I can
say I have 50 user 1,000 users what they
are they're doing they're opening the
contact card or customer card greenass
this might seems a large customer but
this one does not give any arm so to
speak to the people that have to
implement to the consultant or to the
developers. So it is better if if you
know in advance but it is hard to know
in advance unless you're coming from
earlier NEV version or from GP or some
SQL server databases from uh some of the
competitors the transactions volume and
the types because this one it is shaping
uh uh the locking scenario that you have
you might have up front or the things
that you are actually doing if you're
doing this reactively because you have
already uplifted to the cloud one of
these big elephant transaction volume
and type the most important it is the
another one it is the concurrency when
you know transaction volume and type and
then concurrency you have something that
it is far better than the users because
let's say concurrency I have a customer
with 100 users but they have rot so 25
it is a 247 and you might see that
concurrently maximum they are 25 we are
in Italian typically they are 23 I don't
know the other two were What are they
doing? But anyway, uh uh instead of the
database size that it is static
photographic. Okay, this is one
terabyte. But uh yes, I have this one
since 1976. Okay, good. Now I understand
why database grow it is better. So you
just have to measure this month by
month, year by year. You have to look at
the capacity and then understand when it
is time to put more money and buy or
another production or buy uh much more
spaces that you have inside. Italian
doesn't trash nothing. So yeah, database
is growing a lot. Exactly. Another one,
it is the complexity that you have. So
all of this plus the complexity you
might have some special ISVS that are
going inside plus you just have a full
word of integration with the outside
world, the power something that you
might put inside. And this one I call it
the silent enemy because you don't see
it but the web user perceive it. If you
have uh 300, 400, 1,000 calls per minute
uh behind your uh
you got me what I mean? Uh the last one
it is special requirements. They might
have 247 very very restrictive 247 and
then you know that Microsoft applies uh
application notix and platform not fix
or you have to go into the next update.
Luckily, the flexible update is making
this 24/7 much more uh much more
feasible to go into the cloud. And in my
life, I've never found a real 247 that
never ever applied the patch on SQL
server on Windows or so there there
might be a windows in order to apply
this kind of patches. So just to define
the average customer are the one with I
transaction volume and type with I
concurrency andor I concurrency andor I
database growth I high complexity and
maybe they have special needs. So if you
have this kind of uh elephants most
probably you're working even Saturday
and Sunday if you do not uh take your
right precaution. Okay. And you're lucky
that I don't own a dragon of course.
Okay. So look at this one. This is one
of uh uh our customer that they have it.
If you look at the numbers, it is a real
customer. You might think this one it is
a trouble. How how can you uplift this
one or you you've blown your mind? Well,
you know this one
probably open one support request and it
is above the job queue honestly every
two months or three months everything it
is going really really really good. You
know why? Because it has quite a lot of
isolation. And it has two production 47
companies mostly 500 users and then if
you do the mainly financials if you do
the math then this is 10 12 users all in
the financial side. So this one it is
really a large customer in the cloud
with some integrations but this one it
is really green grass numbers is big but
this is not a big customer for the
exactly. So right now you have to tackle
the real problem that it is high volume
of transaction types and with high
concurrency. So how you tackle this? So
the first things it is you have to know
your enemy right if you don't know it
you have you have to find out the right
tools to know it. This is another
customer and this one it is uh 500 uh
licensed users but concurrent it is 100
users in uh uh we are looking at the
concurrent user but then of course we
have to look at the transactions that
that are made. This is actually the the
actual data. Uh in one hour you can
isolate uh the number of users
concurrent on average there are 100 the
user that are perceiving the user
interface but behind the scene that is
playing you you can see that there is uh
the the silent enemy. Okay the silent
enemy that is this one this baby. So
they have quite a lot of integration.
They have a B2C, they have a rush
management system, mass uh and and and
counting wherever you want name it, they
got it. So they have quite a lot of
integrations and this is something and
this is actually uh uh per minutes the
number of web service calls that they
have is plus they have the job cues and
so on and so on. So handling this kind
of customer it is quite uh not so simple
but luckily in order to know what it is
running behind the scene you just have
to implement really a a a solid
telemetry practice to analyze exactly
what it is the concurrency in an exact
uh uh spot of time or trends in one
month in two months in three months and
so on and so forth. So I want to show
you just an extract of the uh Azure data
dashboard that uh uh we are using
typically in order to tackle okay in
order to tackle our customer
performance problem and uh just related
on this you can see it should we switch
okay switch it perfect on okay so this
is Azure data explorer
your environment is emitting telemetry
And then from this telemetry you can
analyze it. Microsoft goes with this
PowerBI but it is not so re um so just
in time the what you are seeing it is
actually what it is happening right now.
It is the 13th of June. It is live. It
is connected to this is a live customer.
So we are to a live customer and you
know that the telemetry does not contain
live real live data. Yes live data does
not contain any PII any private
information identifier. So I'm just
working with just three of the seniors
that are 200 uh and counting. Okay, just
with this these three senior what you
can squeeze out in in know from uh uh
what is happening behind the scene in
your customer. So what I've did here
I've just let let me pick it up just
higher uh volume
of days. So in the 90 days you have the
number of longunning queries and the
duration of the long runninging queries.
Okay, the number of longunning queries
and long running queries it is one that
is higher than 750 milliseconds. This
has been established by Microsoft. I
don't know why probably they flip the
coin and 75th 750 gets out. So you might
I just want to to to see how how I
analyze this kind of stuff. So in 90
days there might be a trend. Let's let's
not consider the spike. The spike it is
obvious right now. You can see the spart
here. What happened? there was something
in this environment and it was low but
why it was low this this environment
first things that that I want to to see
it is what what this is depending from
it is depending from the web services
from the background session okay I I'll
give you uh just again you can filter
this one then you can see only the
background session in 90 days so
everything that it is flown inside
within this uh dashboard it is filtered
by background session and you can see
okay there was a problem in the
background session session then you can
filter this are emitted right are
emitted then you got the time stamp then
you can filter was this really a problem
because they were working during the day
or not during the day as you can see the
problem was during the night but during
the night sometimes there was a flip in
the in the background session this one
goes and fluid into the working hours
and then people start going down some uh
lock time out appeared etc and then we
fix it okay we took some time to fix
this but actually be fixed and as you
can see this is really green grass. Let
me put this back. You can do quite a lot
of stuff with just one single signal.
Okay, let me put this on 14 days.
Another things that I want to show you
it is the average duration of a
longunning SQL queries. Oh, let me put
this back to everything. Exactly. Okay.
Now you can see the average duration of
longrunning SQL query. So I'm taking all
the longrunning SQL queries. Then I'm
talking just the average divided by
client type. This might be useful if you
overall if you have a massive web
service uh calls etc. At some point
maybe uh they they take one second the
day after it is 3 second one on the
average and then you can see that
everything is low in that and you can
investigate. I just want you to show
what this kind of things means. Let me
pick it up maybe again 30 days and I
just want only to pick it up the web
services.
Okay. And uh surprise you can see this
erection of seniors the erection of
seniors it is Sunday because on average
the the web services are running quite
fast 1 second 1.5 seconds on average
right but on Sunday you don't have this
kind of uh B2C working so much on Sunday
you just have other stuff that goes into
the BI and into other kind of
integration that are more longer than uh
than it was. So those are the data that
you can squeeze out with just one single
senior that are the long running SQL
queries. Then of course you might have
some seasonality seasonality means that
what about the the weekly cycle or the
or the monthly cycle. So that's the
weekly cycle that that might tell you
okay are we going good? Yes. Well it is
decrementing the number of uh on the
left the number of SQL server longunning
SQL server queries. This means two two
things or people have been fired and
then you have less people less
transactions. I I don't think so because
they are growing and growing. The second
one means that it is going faster for
somewhat reason for many reason it might
go go faster and then this is the
duration of the long the the long run
queries.
Okay, let's go back to maybe other 14
days. And uh this one it is very
interesting when when you receive the
longunning SQL query you have the SQL
query within the SQL query you have uh
the statement if it is select update
delete create table whatever SQL
statement plus you have your fields plus
you have your where you have uh your
read isolation stated you you can use a
reg x and then manipulate this one and
see okay how many reads I have how many
select I have how many create update I
uh updates I have in this in this period
of time and how many the others you know
Nicole Kidman and other other other okay
so one thing is that in 14 days as you
can see they're reading quite a lot so
that that is typical from LTP they read
uh 89.7% and then 10% sometimes it
depends on this is manufacturing so they
they they are also writing but the
problem is that that they have also
quite a lot of reading inside you can al
also So change this one and see okay let
let's pick it up the last three hours I
I don't know how we will figure out
honestly so right now we have 952 and 48
of right but who is the one that is
responsible to write in most yeah you
might you might think it is web client
no the web client they're reading quite
a lot they are not it is other silent
enemies all this kind of automation so
again I think it is the background
client that it is performing some stuff
it is writing 87.2 2% of the time and
reading 12.8 of the time at least in the
last three in the last three hours.
Okay, so this is just one single
statement the things that you can
squeeze out in the overall. Now let's go
into dive into the analytics. Okay, so
pick up your pillow and put your on the
back and then look at this one and don't
fall asleep. Okay, so right now just to
give you that that I'm not telling any
kind of uh of things. This is the last
three hours of this day within this
customer and uh I uh I have extracted
actually every hour how many distinct of
user telemetry do you have it and as you
can see they are pretty much working
because we are on more than 100 users
actually are working on it but as
mentioned I have to pray what I preach
right let's look at at the sessions that
you have it web client typically you
have one or two so it would be 200
session but the the one that that is
giving really an headache it is the baby
it is the web services 6,000 call per
hour 9,000 calls per hour they they they
want data so you just have to shield
this kind of things with good code at
and with other stuff that me and this
beautiful guy we we will show up during
the day okay so move on forward in the
last three hours I can take all of this
query okay this query it is the
longunning query signal is geared up by
the stack trace. That is the beautiful
things. The people that are old like me
remember the old client monitor where
you can correlate the CL statement with
the SQL statement the the within the
telemetry you can do pretty much the
same very similar stuff. So you have the
stctors and then you have the SQL. So in
the last three hours I have summarized
uh what it is happening and added the
percentage. So 12.5%
it is made by this guy here this select
that it is in the stack trace I'm not
open it up but you know the 12% in the
last three three hours coming from this
kind of activity and you have to
concentrate on this kind of code to make
this optimal maybe you have to refactor
or maybe simply just have to apply rules
like uh read isolation settled fields
and all of this kind of stuff
and uh just some fancy graph the top 20
objects in the last three hours during
the the long running SQL queries and the
one that do have a lock. Okay, th those
one are overall and this one just the
one that are actually locking and uh in
the last three hours in here you just
have all the days of the longunning SQL
queries this is actually what it is
happening behind the scene ordered by
time stamp. So this is the concurrency.
If you can see this one, it is 11:15 and
is 11:18. There might be some delay in
uh when I when you receive data. If I'm
clicking refresh, most probably I I have
just an extra data. I have dissected
this senial and from this senial you
might know what it is the duration uh
the type how many flow fields they have
the join if there are uh in the past it
was useful when there was this table
extension and then if it is blocking not
clocking I have a call already in a
different way if you see one blue this
means that oh this guy might be a
problem well it is just uh not a problem
79355 milliseconds the object
information the tax st extension
information SQL treatment everything
plus the user and the session. So if you
want let's say to see how it is the
concurrency this one is is very big it
is hard to to put your eyes on but let's
say that I want to see uh to make a
visual with the user telemetry this is
one colored by the user telemetry and
those are the users that are uh working
together in the same spot I'm taking
three hours so it is quite a huge amount
of uh of uh um of data just just to just
to see and this one it is my little
jewel. So I in every 10 10 minutes I
pick it up how many SQL uh statement
have been emitted and if they are select
or if they are select or if they are
update delete
and insert. In this kind of cases you
just have your your panorama of if it is
locking no locking or if something might
happen. This one it is just the number
and this is the duration. You can just
simply add this one in here and then
this one it is the number of uh query in
update or delete and this other one it
is uh uh the duration with Aszure data
explorer you can even look up I've not
added this right click the taste and
then you can see which are the queries
like the typical flow field that we have
in AL okay you like it
good
remember I don't have a Drago okay then
uh you have the long running query uh
count per average day buckets. This one
it is just a pivot on every query
measure it every day how this one it is
changing. Let me filter out for this one
for 70351 because 70351
because we made the changes this one was
really impacting uh with the count and
we made the changes on the 3rd of June
at 555. I would have preferred 6 66 but
it was not possible. Okay, let's make it
14 days. So this one will turn up and
then this one it is a pivot and within
this pivot it will report me the count.
Yeah, might take just uh some some few
seconds and uh this one will report me
uh okay perfect will report me the count
for every day how many time every day it
has been called but the things that I am
interested interested in of course I can
export into Excel because if I right
click and then say export to Excel I
have it this into Excel and send it to
people to developers to wherever it is
but the things that I want to show it is
the average so that that is the average
on the third 30 May 444 44 second and
then when we did this change it they
changed uh we changed this it was 4.7
the day before that was Monday from what
I remember on Tuesday it was four
because at 555 we changed it so they
started to come the one from two seconds
right and now it is 2 seconds two
seconds we just reduce it by 50% with
this changes the impact on this specific
query and you can measure this up uh
quite easily uh the settled fields it is
uh something quite good the settle
fields in all of this query I have pick
it up and with some reg x I have
extracted the number of the fields that
you have inside and I have ordered by
the number of columns selected do you
need to add settled fields in into this
kind of scenario okay just filter in
here I'm taking everything and then put
this like uh between 50,000 that is the
pt range and then give it to the
developers okay okay or send the dragon
of course you can see those are the
number of columns selected the order and
then then the count. But you can even
search sort this by count and then see
okay maybe this one needs a little bit
more joy. Well not it is ADLC. So this
one it is for the PowerBI but you got me
what I mean. I can export this one into
Excel and then send it to the
developers. Then the developers there is
this the stack trace and there is the
SQL statement. They go one by one then
they fix it. Then the day after we can
measure the performance. Okay. This
gives you an idea of object that you
should check because yes yes and this is
just one sing okay just one sing
okay then let's let's talk about just a
little bit locks okay those are the
locks on the left choose whatever you
like in order to fix your house then
let's see how how it is locking in the
last three hours the things that we have
most probably not that much from what
I've seen already in the SQL uh those
are all the table that has locken the
locket by duration in the last three
hours. The GL entries you register then
some custom tables so on and so forth.
It might be Ben or not. Then you have
the top 50 SQL queries that all database
locks and this one are ordered by total
cost. Total cost it is the number and
then the duration. You can take this one
and of course there is a stack trace and
then send it maybe after two weeks or
one month. Okay. Take the top 20 analyze
the code optimize
you know the cycle of performance. Yep.
And then behind the scene you just have
lock by calcium, lock by is empty, lock
by count. You know I don't want to
stress the fact that read isolation most
probably it is one of the uh biggest
things that we were waiting uh indicates
and this one will tell you if there are
calciums with lock if there are uh is
empty with lock and count with lock.
Typically we start with positive
approach. We are Italians we are
positive. So we put okay put a read
isolation on it right don't be
pessimistic on the calcium etc and this
one will make it uh disappear deadlocks
or even sometimes just lock timeouts
depending on the transaction now we had
the the deadlock dreadlock I just uh put
something just uh to make us smile
because at this point typically people
are uh more or less uh uh uh sleeping
and then you can catch up the deadlock
okay this environment I do have 100
people that are working plus you just
have the silent enemy behind the scene
and believe me if you have one or two
deadlocks they don't call me typically
the deadlock are appearing in this time
are appearing in the power up the spring
completed they do have a warehouse
typically 42
if if I'm not wrong 4200 devices so they
shoot should shoot should shoot should
shoot shoot should shoot should shoot
should shoot should shoot should shoot
should shoot and when they shoot then
every it is sent over also for the
printing sometime they receive a
deadlock they shoot again and it works
okay so don't ask me to fix it or I will
charge for quite a lot. Okay, so this is
the things the SQL deadlock by table we
just have one. Let me make it just a
little bit more than this uh maybe seven
days and then with the deadlock you just
have the order. So the percentage what
is the table the ledger entry of course
because you always have to go to the
find list wait but luckily with the the
new approach that we have with number of
sequence this one might not be uh so
scary as it was in the past. So those
are all the deadlocks in seven days.
Believe me, those are uh quite natural
in this environment. Plus some fancy
heat map in order to have a deadlock by
sources and table and al method by table
in order to emphasize which are the ones
that most probably need some joy. And
then of course the uh this one it is
good if someone is calling you what it
is happening. Well the the there have
been a deadlocks in the last five hour
every five minute buckets I'm catching
up if there are some deadlocks. Okay,
lock time outs. Uh we are lucky because
we had some of these lock time outs but
I think where they are coming from. So
there have been lock time outs in here.
If you notice one growing and growing
this means that you're running MRP
behind the scene or you're running
something that it is locking behind the
scene and you're have gone to take a
coffee and everyone it is lock lock this
one it is also helping you in understand
which are the processes and uh remove
this person no remove the the problem
that you have it. So those are the SQL
lock timeout in the percentage that we
had in the last six hour. Uh yes I know
what they are doing. This is quite uh
for for the volume that they are moving
it is quite uh uh uh physiological so to
speak and uh then you have the lock
timeout. You know, with the lock
timeout, you just have the people that
has received the timeout, but you do not
have the the um the one that did the the
long runninging query, but and you have
the snapshot of course of we what
was running behind the scene from a
locking perspective. What I've created,
I've created what was running. What is
what was running? Let's say that we had
this at uh 91 12. The what was running?
uh it is taking a custom range. Let's 91
12 to 9:30 just want to show you what it
is. If I'm clicking apply, it will take
the time stamp and the duration. So we
will you will have a start time and end
time and you will have everything that
was running that has been senior in uh
uh in as as long running query or long
line application method. this longunning
application method they they have as you
can see those are the one that were
running and then they were running since
since here most probably this happened
because in one of this you just have to
analyze what was running then narrow
down where the problem is
and uh this concludes the the simple
small part related on the telemetry
within the telemetry you can really go
down to every single piece of what a big
customer is doing you can switch
Okay.
So, uh we now we we start after seeing a
live customer and how it behaves on
telemetry. We want to start explaining
the optimization part. So, this is the
status and now we started optimizing
things in order to uh first of all avoid
the deadlocks and lockings and uh
optimizing performances. The first uh
piece of work is related to posting. uh
posting uh I think that you know that uh
in business central there are some
co-units that for uh for posting are
quite problematic. Usually uh the
posting code units if you analyze the
macro blocks of the posting code unit it
takes uh a small part of the time for
locking uh the current document
momentarily in order to check the number
of series and something like that. And
then the long part of the time is spent
on writing. So on writing on the the
ledger entry tables of le entry
something like that and then it place
also a lock on the gel entry table we
use as a semaphore in order to avoid uh
to guarantee the concurrency of the
transaction. So
in order to optimize the perform
a large customer when you have
concurrent transaction the you need to
try to start optimizing and also
Microsoft start to do that the the part
where you spend a lot of the time. So
this is the part that we need to uh put
the focus on and uh now we will see how
we uh handle that. So D will if you want
to Yep. Yep. So the things that we did
actually okay let's uh let's have a look
at uh uh BCPT business center
performance toolkit and then try to pimp
up a sandboxes. So I'm working on a
special sandbox that has uh a typical
tier more or less of a production. So
behind the scene I have a a business
critical database that is just behind
the scene. All the rest it is uh like
like it is in the s. So we run this BCP
and we try with uh do experiment for
quite a long time. So quite a long time
means 6 hour 8 hours continuously try
this kind of sales post and uh when we
started immediately we received if you
do this kind of sales post with 10
session 12 session or whatever it is
immediately you will receive this uh we
can save your changes right now. So you
receive a lock timeout actually in the
gel entry. This means that wait that you
have to wait your turn and then after 30
seconds you have to go and and try it
again. So there are quite a lot of this
uh this kind of uh of session. This
means that this concurrency will kill
you because your user will receive
actually uh this error quite often if
you have quite a lot of this user on the
other side. Meanwhile, we were doing
this, we were seeing also a slope going
down, down, down and we were using a
chronos. Remember Stephano what happened
it exactly? Uh we uh the first thing
that we discovered and with the uh
tattoo in on every uh in every developer
in our in our company is uh related to
automatic cost adjusting. So automatic
cost adjusting is a big problem on uh
big customer on on high transaction
customer. So this is something that uh
you should remember and you should uh uh
usually disable. So automatic cost
adjusting in inventory setup should be
set to false and uh not always because
uh uh if you do that during posting it
takes locks and it creates a lot of
loneliness. So uh for biggest customers
with IT transaction customers we uh
absolutely disable this feature
everything and we schedule the cost the
uh the cost adjuster report. So this
report in order to uh be executed in the
background uh and not during in real
time during during that in real time you
kill uh the performances of the
application the performance of posting.
So this is something that is draari. And
so we we should you should absolutely
avoid to do that in uh in large
customers. Right. Right. Okay. So one
solution to concurrency is do not have
the concurrency like the fight club the
same things don't talk about fight club
no concurrency you serialize. So use
background posting or do something in
the background in order to serialize and
avoid to have this kind of uh locking.
So the the things that I did actually
I've changed this uh uh this execution
using the normals is supposed to be a
job Q and Q say solder say header I just
rerun everything everything was running
of course and uh those have been the
results that I had because some people
ask what if I have 1 million of records
and uh and those were actually the
results that you have it you might take
this with the plus minus 10 50% if you
want to go into production otherwise you
just have to put the fingers on the the
posting routines. Those are actually the
number. So the random s line between 1
to five this means average 2.5 and uh 1
to 10 this is the number of sales order
posted per hour. This one will be
recorded so that you can stop it and see
what were the results. If you just want
to approximately size uh the the average
limit of uh that that you would like to
achieve within this uh this kind of uh
using uh um in queuing and the job queue
and the result is that when this one it
is running then you can see it is
flipping up and then popping up quite
quite a lot of this uh this job q but
let's make it just uh showing up how
this one it is working in in the real
life
with the bc BP that not one dare to
show. Okay. I think you see. Yes. Yes.
The So this one is is the the BCP
project. BCT comes with Visual Studio
Code IL extension that uh uh product
group thrown away some times ago and
never maintained. So it is useful if you
just want to create a simple prototype
and start play playing around. So this
is one just it is just the standard and
then the only things that I have changed
uh uh in the BCPT says post it is just
one line in here. So instead of posting
I'm using background posting plus I have
just added some bit of spice in here
that is I'm just creating I'm just
randomizing and then I'm just creating a
random line. So it might be one it might
be 20 it might be 15. So on average it
will go into the average of the the
maximum lines that you have plus I'm
sending a senial just to have fun and
with session I'm send sending also
another signal to see what was the
average number of lines the first number
of order and then the last number of
order just to get to understand how this
things it is evolving and to have just a
little bit of fun I would like to show
you how this one it looks like. So
this is actually uh to that it is my uh
powered sandbox and uh if I'm going to
BCP suites then I have two actually the
one for BC tech how does it work this
one you publish the that object that
code that is this one and then within
this code then you define uh what it is
your scenario in this kind of cases uh
it will uh it will be for uh three
minutes and
it will continue to generate and then to
spawn up a job queue for three minutes
and with 10 number of session I can
increase the number of session but let's
start with with this 10 so let me start
this one so when this one it is started
the things that it does it will start to
log everything and it will log also what
will happen in uh h into telemetry and
in inside log tables so if I'm now I'm
refreshing here you should be able to
see that right now there are two
sessions two iterations that has been
done. This is the total duration and so
on and and and so forth. If I'm going
into the log entries, right? If I'm
going into the the log entries, I can
see I have already pre-created my
analysis view. This one was presented in
another BC tech and there was an export
into Excel with the pivot. Now you just
have analysis entry. Then you can see
what is running behind the scene. So
behind the scene you can see that this
one it is now running. There are eight
and this is all the the the scenario
that is running and it is t taking on
average 634
uh
milliseconds
and 320.865
865 it is the average number of SQL
statement this one the same things you
can even forget about it and you go into
telemetry because the same things it is
emitted into telemetry then I have yet
another dashboard maybe this is the baby
and then if I'm refreshing the this
dashboard there might be something
inside it voila the same things then you
can see that right now I have 90 that
has been in success and the average
duration and the average SQL statement
this one meanwhile I'm I'm switching
between one and the other one there are
the two sessions that continuously
munching munching and then uh creating
uh the job queue for uh within three
minutes and this is what I was
mentioning this is my custom uh senial
and at the moment the average number of
lines it is 10.9 and the minimum sales
order number it is this one and the last
one it is this is the maximum if I'm
refreshing in here then this number is
changed 35 so on and so forth and this
is for three minutes and this is what
I've used it to make my experiments if
you want to test scen scenario even more
complex. You might add more code unit,
more people, more concurrent session and
then you can try to have your load as
much as similar as possible to to your
customer. Um this is very good for the
on premises super good to to use it for
the premises to the online. It is not
open to production but only to
sandboxes. So it is it is sort of
useless. It is good to spot out very
easily the concurrency because the the
database tier it is it is very low but
I'm just praying that at some point in
time we will have also a pre-production
or a sandbox that do have the same tier
uh in the database as a production so
that this load test would be really
really good in order to be performed.
Okay, so far so good. Let me go back.
How's that? You like it?
Okay, perfect. Perfect. Awesome. Um,
that's it uh for the first part. Let me
go back to the BCPT. Okay, we go back to
the BCP. Refresh. Let's see if we have
ended up with the uh with the one. So,
let me stop this one. Then this one will
cancel all the sessions.
Okay, I'm closing this one
just to be a little bit faster. And then
I'm going into
into here again. And
we can move on to the
this. Yes. To the next one. No, this
this. Yep. Okay. So a a large
optimization that we have done in every
large customer that we have is try to
avoid uh every time that is not related
to number series and every time that
sometimes requires to use auto increment
or uh worst case is like for example
handling uh increment of numeration
insert trigger of table something like
that. So we start using number sequence.
Why number sequence? because uh number
sequence are
uh handled in a different way in in the
back end. So in Azure SQL or in SQL
server number sequences are uh totally
relies on uh what are called um SQL uh
number sequence and these are not
handled at the table level. So this does
not require an access to a physical
table in SQL but are absolutely
performant in term of locking and in
term of uh reliability. So uh business
central has introduced number sequence
from I don't remember the number of the
they released uh some some releases ago
50 or 60 probably and sometimes these
are totally forgotten from the
developers but with number sequence you
can first of all uh creates a number
sequence object with the number sequence
keyword and you can this can be per
company or not. You can uh for example
in like in the first example start
detach a number sequence starting from
the first from zero incrementing by one.
And this is absolutely better than going
to a number series obviously but also
better than uh using auto increment or
using uh the onins insert trigger to end
the increment by one. Uh you can also uh
because we have no SQL access and you
can you can also not table access and
you can also use uh like the next
operator to to obtain the next number
but you can also uh reserve a range and
when you have you need to post a set of
records for example register a set of
records in a table in large table
instead of and you you need a numerator
for these records instead of going into
the table or number series or into the
table for TV numerator for example with
identity or something like that. It's
much better to do that because like in
this example here we are reserving
10,000 number series with the standard
number series it takes about two seconds
but if you do do the same with the
number sequence it takes 40 milliseconds
so extremely faster. Uh obviously
where's the drawback? The drawback is
that number sequence if you reserve a
range it gives you the range that you
can use for your records but if you have
an error uh you have a gaps but uh
usually gaps are solutely uh okay when
you need to insert a table record in a
table. So usually you don't need to have
gaps when you have uh fiscal documents
or something like that but not when you
need to post in the warehouse or need to
post in either ledger entry or something
like that. So we we have totally
refactored that in order to use number
sequence in our biggest customer. Yes.
And this is also what Microsoft did and
it is doing. So the number sequence it
is an object outside the table. So you
just have to access it take the number.
It is like a ticketing system. So it is
not bounded to any table. Exactly. And
uh but there is a cost of it that it is
the cost to pick up the ticket and then
assign it. That is uh the problem is the
latency in this. If you are doing just
quite a lot of this uh but it's much
more less costly than doing a but but if
you know in advance how much of this
numbers you needed it is just one single
statement and it will give you just the
range start from here start from that
one period. Okay. Now if yes so what has
been uh done by Microsoft in actually
two waves in version 25 it has been
introduced at the number sequences in
the warehouse entries. So if you are in
version 25 you can enable it and we have
enabled it and it is working just fine
but in 26 it comes the Armageddon. The
Armageddon means that right now even um
item entry and value entry can use the
number sequence. This means that you are
really doing something that in in a
decade more than a decade Microsoft
didn't dare to do it uh before. So in
all of our big customer that are have
moved and are moving into uh version 26
right now we are enabling all of this
all of them and uh uh this should be a
mandatory best practice mandatory best
practice if you have for all the
customer but overall if you have big
customers and this is just one single
small pattern that you might find if you
go into the wars entries iter entries
you can see that when uh there is the
insert records the insert record before
of it there is an assignment of uh uh uh
a sift bucket number that is a new field
that has been added in order to uh
reduce the statistically the the the
possibility to have a a deadlock on
specific sift. So in short if you just
have sift on table like item ledger
entry value entry and so on and so forth
you move to the version 26 you want to
enable this field and then just also
change your your uh uh your keys in
order to add also this sift number and
more or less I think 95% you are good to
go with this new uh process. So let me
show you this live because I don't know
if this one has been shown but I just
want to show you this how this one it is
working using BCPT
right thank you okay so I just have
another BCPT in uh I call it this
inventory another scenario and within
this scenario I'm just executing this uh
piece of code here and this piece of
code it is just simply create an item
journal and post an item journal with to
create an item journal just filter for
in this chronos databases for an item
that have inventory and does not have
ordering policy otherwise it will block
me in the assign one. So I just want
this to flow to to show you how this is
working with or without having this uh
feature enabled or not. So this is just
very very very simple stuff. So let me
go back to
to yes in here and then uh how those are
as have been this feature enabled. Yes,
this feature has been already enabled.
So I would like to show you how this
this is working the feature management.
This is the typical setup that we have
on our customer. So we are enabling of
course uh uh do not calculate the flow
fees that uh Stephano will show this uh
in a minutes plus all these other ones
right those one are all enabled. So this
means that right now my atomizer entry
will use and all the other ones will use
the number sequences instead of uh uh
the typical number series go and then
take the last number block it uh take a
lock on the last number and so on and so
forth. So let let's make it to work and
this will run for just one minute. I'm
just uh starting it. So this one it is
started and then we will have 15 15 of
this that we are continuously posting
and posting and posting and posting. And
of course we can do always uh the same
typical stuff that we do. We go into the
log entries and see right now in the
inventory posting I just have this one
that I've called it higher concurrency.
And then as you can see there are
already eight and then all of them are
in the success scenario. This one it is
working as you can see this one it is
slightly growing see 7 8 10 seconds
because behind the scene they are taking
just a little bit time but they are not
blocking each other actually right the
same things that you can see of course
using telemetry you have to be addicted
um I just want to filter out with the
inventory that it is the code that is
senting over and I just want to see if
there is something oh there is one that
has been errored maybe it is something
with the paging or uh something on this
flavor. I don't think it is related to
the uh personally to the concurrency. It
might happen this one in this kind of
scenario. And then this one it is
flowing and flowing and flowing and when
one minute it is uh it is over.
Yeah. If I'm refreshing this one or I'm
going back
then maybe one minute it is spent. I
don't think that we will have an error
on uh on the locking routine. It might
be something else
within the other concurrency.
There should be one error. It might
happen.
And then that's the error. Exactly. This
is what the record in the item
application already exist. There should
be something behind the scene but it is
not actually the uh the item ledger
entry that it is blocked. Then you have
to narrow down what it is. Okay, that is
the thing and right now it should be
over because one minute should be passed
by. If I'm refreshing this, okay, it has
been completed with just one error.
Right now let let's do the experiment
and then change this in the feature
management. So we do in the feature
management and we run the same exactly
the same things. Imagine that the error
with the it application never happened.
It is not the same error that you will
see in in just few seconds. Let's
disable this. So fall back to the normal
routine. It might take just depending on
the number of entries that you have. It
might take some times to uh
to adapt just typically changing to this
one just to let you visualize how it is
uh uh it is typically you can see this
scenario. This is the scenario with the
draarist that shouldn't be that way
around that right now that I have
changed this one within the this one. I
just need to log in and log out because
of otherwise the the new session won't
take this one. Uh with the BCPT it is
just a little bit stingy. So normally
the things that I'm doing I'm just
closing it and then opening just another
session.
Okay. Even though the session are
spawned by by this one. So I just want
to be sure that right now it is not
running using the number sequent but the
old way uh uh to do to do the stuff.
Then I'm going into the BCP suits then
go to the inventory. One thing of the
BCPT is that you can compare one run to
the other one. So if I'm adding this the
base version is the 16 the things that
it did
he has changed the value in here exactly
with the same one. So 54 it is the 16th
and this one it is the again the 16th.
If for example if I change this one this
15 then the value will change with the
previous run that I did it myself. So I
just want this with the 16. So the next
one will be the 17 and the 17 will make
the the difference between locking uh
between the the two type of uh scenario
with number of sequence and without
number of sequence. So let me start this
this one. Uh this is again higher
concurrency. I should have called it
call it lower concurrency of course but
never mind because I have the version I
should have changed the tag but right
now if I'm just refreshing at certain
point you will see that there will be an
error and you will see the number 17
that that will start just in a few
moments popping up. Okay, let me go back
to the uh inear and then see the log
entries are just already flowing in
and then with the scenario concurrency I
have the 17 one that it is scenario with
success already. Yeah. And as you can
see it is already just pumping up with 8
second. This one slowing should go up
until 30 seconds actually with this 15
this 15 and 30 seconds means lock time
out. So in lock time out it is the bad
error. Okay,
let's see how this is moving. So with
the standard feature the posting is
lowing always slowing until lock time
out. So if I'm refreshing right now I
have all all the success in the
scenario. There is the average duration
and uh sooner than later we will receive
this uh this error hopefully. This is
true live stuff.
So this one it is still still running.
Oh it has been completed and let's see
if there is
some error in here.
It should be
all success. Well, anyway, yeah, I would
have expected the opposite, but if I run
it again,
yeah, see it is quite close. 25 26 26 26
If I run this again, this one will will
generate an error. So, that's the
standard posting. So, standard posting
is slowing down, slowing down until
Yeah, usually you have an error when you
have a lot of transaction, concurrent
transaction. Yes, I should have tried
with 20. So that you can see one things
that you want to notice it is this uh
the the the previous one was slightly
faster because you don't have to do this
kind of access to take the ticket in the
number of sequence but the other one has
much more concurrency than than this one
exactly uh switch. Okay. Yeah. Uh the
other big problem uh that you should
start optimizing is when you have flow
fields. So flow fields usually customer
abuse of flow fields. So when we have a
statistical table uh so heavy table we
and a lot of statistical field on top of
this table you should start optimizing
that because that this uh creates a
problem and in version 26 there's this
feature called calculate only visible
flow fields that by default is turned on
uh is turned off sorry uh you should
always turn it to uh enable it also if
Microsoft declare it as preview but uh
in our opinion is absolutely recommended
mandatory to turn that on and uh
profils also uh create uh slow locks and
and loneliness also when uh page loads.
So uh in this case uh we have in many
scenarios for that we have totally
refactored our uh solutions in order to
uh change from flow fields to page
background task because uh page ground
task plus read isolation and set of
fields mandatory in order to uh improve
that. And uh just to very quickly show
this in uh in in an environment. Uh let
me
refresh this.
Uh here I have sorry first of all I need
to check the feature management
and in feature management here you have
the settings. So this is as standard
this is disabled.
Uh what happens when it is is disabled
is happens that if I have uh a table
like uh the following
uh not this environment sorry but this
environment
if I have a table like the following
this this is a table where I have my uh
entity and then on top of this entity I
want to uh calculate statistics uh on
top of an a table. So in this just to
show you the uh the code this is my
table
uh where I have a uh in this environment
about three millions of records. So
these are like the item ledger entry or
something like that and then I have uh
this table where as you can see
I have a set of flow fields a large set
of flow fields that goes on my heavy
table.
uh what happens in the business central
as standard if uh in this uh table. So
the the the the small table I go to
check statistic and so loading the flow
fields. Uh it happens that I click on
this and this weights weights weights
waits just only for showing one flow
fields because this is only the only
flow fields that if I check you check
the my code I have as visible
all the other flow fields in the page uh
this page
uh where is not this page sorry
statistic v1 okay this page all the
other flow fields are visible false so
as standard my page is low slow only
because uh one flow fields is displayed
because business center as standard
until today always calculates flow
fields also if you have that disabled
but uh if I
turn this feature
uh off. So I go this and I uh sorry this
is on not off. Edit.
I enable. Come on.
I enable.
Why I cannot enable?
Oh, no. It's this. Sorry.
Draaris. When you are here, it's very
easy. Draaris. Okay. Enable. H. I need
to sign in and out. Let me do this.
And what happens here is that now things
changes. So this why uh this should be
enabled. So if I go back
uh here and I uh now I call uh this
page. this page immediately goes out
also if the underlying table has 30 flow
fields because uh it works uh without
calculating the flow fields obviously
where's the problem this
because in my code this is a calculated
field in with with a formula
like this
this is the difference between two flow
fields so if the flow fields are not
visible in the page because these two
are not visible. Uh this field is not
calculated if you do that like that. So
this is the only drawback if if you want
to do that or the the trophies are
visible or you need to calculate.
Uh another uh things that I want to show
you is that with this feature active uh
here I have a second page that shows me
uh all the fields calcul automat the
flow the flow fields automatically
calculated. This uh this statistical
page usually uh takes a bit of time to
be calculated and you could you can also
change like in this in this page like in
this page you can see now are zero and
then after a bit of time are calculated.
Why? Because this page uses page
background task and uh this is
absolutely useful if you have uh pages
that you want to be responsive because
the first page can be can take a lot of
time in order to calculate the flow
fields with page ground task you can uh
do something like in this uh page. So
the the the main page can pass a
parameter to a background task. So in my
case a code unit and then in the in the
background task I am uh calculating all
the flow fields that I need. So all the
calculation that I need. So that this
page retrieves in uh
this pages
the video two page. Okay. this page
calculates and then uh the color page
retrieves the the the calculation from
the the code units that you schedule as
background and then in this case I'm
displaying the fields so this is the
difference is that the the only
displaying flow fields you need to wait
to get calculation if you use page
background task the page is responsive
so then this changes so that's why we
have used these uh techniques obviously
in uh when you calculate page page
background task
how you should calculate the the page
background task in as as we uh explained
before with this technique. So this
should be a mandatory techniques. So
uh go into the your table
set the red isolation
in order to have no locks
and then uh filters. So uh doing that
registation is uh and set of fields if
you need if you need is mandatory in
order to uh to have an locking
calculations.
Uh let's jump back back to because you
are absolutely late.
Uh another problem I database grow. So
one of the problem is uh that business
central data is costly and usually a
database are growing a lot. So you
should plan for a data retention
strategy from the beginning because uh
if your table are uh becomes too big and
you discover that after one year that
your project is live. This is a big
problem you can because deleting a very
large table can be a big problem on SAS.
So what uh we recommend is to create a
retention policy starting from the
beginning and this means that in the
implementation phase. Exactly. In the
implementation phase. So you should
enable retention policy at the beginning
and then so decide what what are the the
tables that for you can can grow and
apply immediately the uh the retention
policies on this table. And uh to do
that is very easy. You should you should
remember that in your remember that
retention policies is something that in
business central is something like this
uh attention policy
is something like this. So you need to
uh select a table but if you select a
table these are not only all the tables
that you have in business central these
are only table that you Microsoft or you
as I've declared as supporting retention
policy. If you want to support uh like
in my example I the previously showed
big table this table uh if I want you
want to support that you need to add in
your extension code the lines of code
that you can see in the slide. So
in your install uh usually in your
install per company of this uh trigger
add this table to retention policy
otherwise you cannot see that
and uh
just the practical tip is uh when you do
this monitor take it with telemetry
telemetry gives you already uh a signal
that it is the dch
exactly and with this one you know
when it runs if it runs how much things
uh have been deleted and uh from the
standard and of course from the ones
that you have added in order to uh
understand how this one it is evolving
and this is uh something that happened
to me in July 2023
open up table information there was uh
uh 37 million of records and then 10 gig
over a database of 40 gabyte that was
one over fourth and I think how many of
you have had the change log entry that
go mad. Raise your hand. Uh see you
brother and sister of course. And this
kind of things happen when it is like
that you cannot enable data uh uh uh
retention because this one it is uh
cancelling 10,000 per 10,000 and it is
doing just a mad calculation or now this
one has to be uh deleted which other to
be deleted. So you have to do do by your
own by handy just creating another job
queue that with end with this entry
number it is uh deleting little by
little. It took one week to uh just
silently erase all of this table because
it was practically not used it. And so
the mantra is uh don't do this once
again keep this monitored and understand
how many records are inside.
uh again use retention policy and keep
them monitored and the tip it is
calculate your grow rate. There are
different way to calculate you can go
into the capacity
of your uh from the tenant admin center
or using the admin API in order this to
be sent together with telemetry or
somewhere else and then keep monitor it.
This month it is one gigabyte the next
month it is two the other month it is
three. So your average growth per month
it is one gigabyte. Then you have to
refine per table how much this one it is
growing up. Right. And remember draaris
avoid the change log and keep this
monitoring as much as possible otherwise
this blown up the dimension of your
databases. Exactly. And uh sooner than
later you cannot create any more
sandboxes because of you have grown up
too much. The other uh big problem when
when talking about storage first the
data and then the blobs. Blobs should
never be stored inside the blo the
database at least is what we uh
absolutely blocks on on every uh our
large customer. And uh sometimes this
seems difficult but in but it's very
easy to provide to the end user the same
experience that you have in the
attachment but uh doing in a particular
trick that permits you to automatically
save the attachment not inside the
business center database but for example
in blob storage that costs quite nothing
and you save space in the tenant and uh
these are the only line of code needed.
So you only need uh you will have the
slides for that. You only need to
subscribe to an event in the document
attachment table and redirect the
attachment of the blob to the blo
storage. What happens to the end user?
What you can see here. So for the end
user is totally transparent that this
attachment is not saved into business
central but is saving into blob storage
by using simply these lines of code. Uh
for the user it's not really transparent
but you save space. So your user can
also upload one terabyte of uh of PDFs
or other stuffs and these are not saved
into your business center database.
Yes, that's bad habit example if you
want to see it. This one it is a life
example. You might think that this one
it is going out it is going really out
of storage and you know why?
Because of the they are storing this
kind of PDF files inside the database.
It is a bad habit bad habit that you
generate most probably from the NAV and
the second one it is they have
interfaces these interfaces are going
through JSON and then this JSON I don't
know why they save it they save it
because maybe they just want to control
they never never controlled anything and
you ended up in having 38 GB plus 28 GB
in every of the symbol databases copied
over and over again. So that we have of
course
added the practice of sending a dragon
to who has implemented this one and uh
don't do this.
Okay, let's start talking about uh now
we move a step back a step over and we
go to best practice. So what we have
done first of all you the mantra is that
you need to write fast and less lacking
locking code and uh usually if you
analyze what happens when you uh the
business center nst runs I code you
discover that the the code so single
instruction that are not non database
statements are totally uh insignificant
because one runs in the order of
nanconds. Why? What takes time is when
your code need to access the the back
end. So the NST usually spends a lot of
time waiting for database operations
because these are where you need to uh
be faster and uh uh so the mantra is
that writing a fast and less locking
code is crucial uh in large car
especially when you have high
concurrency. Perfect. So we we there
have been a lot of tips during BC tech
days and a lot of uh uh uh other
documentation that you can find about
tips and tricks. We just give you three.
The first one it is embrace new object
and statement what it is new and it is
related of course on performance then
embrace it. So the things that I did
actually I just took uh the base
application and then I I've just
analyzed it how many get uh this one it
is not interesting to me the one that
you see in the bottom are interesting in
version 23 there have been this number
with settle fees read isolation set out
local fees the read only that is using
the replica query object and those are
the lock table lock table draari so you
have to cut one finger if you want to
use a lock table or you want to develop
and add the lock table okay most
probably you will end up from this the
room without one end. I'm pretty sure
many of you. So the things that I did I
analyzed now this one it is evolving. So
Microsoft pray what it preach or not. So
in version 26 the the things that you
that you might see of course it is
growing the base application you might
have much more of the statement but keep
this as this one it has been increased
from 300 to almost 900 sets do it. Read
isolation have been increased at the
dwell set autography the read only and
uh maybe because of copying and pasting
all the stuff it has been also increased
at the lock table but you as a developer
most probably and even me when I have it
I completely forget about using lock
table that is one thing so embrace this
new uh al and master them at best in
your development and uh the second one
all all new object plus this is this
should be a a pattern that that always
have to apply filters and with indexes
of course otherwise it doesn't make any
senses uh as a covering index for your
filters for your wear then use set
fields set out fields if you have flow
fields and read isolation in order to
understand and in order to prevent uh
unwanted locking in I don't know
calciums is empty uh or whenever it is
not needed so this is worst
This is good. Yeah, exactly. As you can
see this one, it is far better than than
how it was in the past and if you're
still in C move to AL that uh we have
good practices like the one that is it
is shown in here. Yes. The the other so
first is this uh the the slide before is
a mantra. The second mantra is that you
should avoid loopy loops when you have
extremely large tables. And how you can
that you can do that? This is a
traditional scenario. So imagine that
you have to loop in an in an item table
with millions of record and then for
each item you need to calculate things
in the item angel entry. Doing that in a
language is absolutely time consuming
especially also if you use read relation
something like that when you have uh a
very very large table. So it's much
better to in this case do a bit of work
more but start using for example query
objects because query query objects
works directly at the database level
with with joins and something like that.
And here is where you will see real
gains. Uh just a very quick demo to to
show that in action. But uh if I'm going
to this table and uh uh here I have a
loop that for each of record in this
table goes into the uh my heavy table.
So the table with three millions of
record and does the calculation for of
the the amount uh this is if I run this
loop in a language. So in the
traditional loop like in the slides uh
for calculating the amount this is uh it
takes a bit of time. I don't remember
how many seconds but exactly it's it
loops for each record in this table. It
retrieves all the uh attach ledger
entries and calculates the amount. So 12
second to do that. Uh I have refactored
this loop uh simply by using a query
object. So here I have my uh query
object this that does exactly the same.
So starts from this table and from this
table goal is into the ledger entry
table and sums the quantity very easy in
my uh I'm using uh this in my uh
in my procedure I don't remember where
is the procedure this okay here I'm
simply using the query now so not the
loopy loops like in this example Here
is was the code in the past
for this I loop the the ledger entry
table. The code now
simply calling the query looping the
query and the difference is that if I
runs the calculation with the query the
calculation with with is uh 1 seconds
compared to about 13 seconds before. So
it's absolutely faster, less locking and
so on. So this is other stuff that we
have completely refactored on uh our uh
large customers. Super good if you have
to aggregate. Exactly. Yeah. Now we
start with the last last part very uh we
are quite right around out of time. So
let's start with perfect complex
integration that is uh one of the last
in the menu. Complex integration typical
goes with API because everything that
you have outside the world it needs to
talk with uh with business central and
it is exposed in the online version
through the APIs. So there are some uh
limitations in the online version that
are those are the rules of the games
that you have to obey. So in order to be
silent, swift and deadly using uh the
API the there you just have if you can
use the readonly replica avoid massive
write operation and of course uh use uh
the batch calls. So um
uh in order to use the read only replica
you can specify this in the there are
three ways basically where where you can
specify this. The first one you can
specify in the object in API uh query or
in the API pages or even in in reports
of course those one should not have any
kind of write operations read um update
insert or delete or uh you can specify
this one in the address when you're
doing the call in your in your get uh of
course the data access in intent does
not guarantee that you have a read only
if you're on prem you know if you have a
read only replica in the line you don't
know it because it depends on how you
have been scaled up. If uh your uh
environment your database of your
environment has been scaled up from uh
uh general purposes to business critical
business critical comes up with an
additional read only replica where you
can offload all your read of this kind
of object. So just to insist in this
remember one of the the practice we have
resolved one problem related to uh
queries that are quite frequent and are
all just reading for example the stock
the the the read only replica it is uh
uh just matter of seconds that it is uh
keep uh uh that keeps the data online
and this one it applies on API page API
query and report another way to do it is
just through configuration. So if you go
into database access intent list this is
something that nobody have seen it
doing. So every time I'm just doing this
is there is also these other pages doing
it. Yes. Take it and with telemetry
there is a a specific signal that tells
you uh which are the mostly used report
and it is just very very easy to do it.
You you can know which are the mostly
used report. You sort it by count and
then start take the first 30 and then
put them that access intent on. I did it
honestly and then someone coming back
stating I have an error then you you
goes back in here and you put that back
read write and then the the this guy is
working on but the other 29 right now
are going offloaded into the read only
replica if you know that you have a read
only replica of course exactly
uh then we started so starting from that
we started uh analyzing the the the
integration that we have with with these
type of customers and uh as you can see
uh you have seen at the beginning of
session when we show you uh a real live
customer one of the customer that we
mentioned in this demo you see that uh
these customers are affected also not
only by uh not well written I code but
also by a complex integration that they
have so B2B systems or something like
that that sends to the tenant a very
large number of API calls and these API
calls affect the performance of that
tenant so we work in two uh main uh
aspects on that these the the the in the
API integration the first is that we try
to minimize the API number of API calls
that arrives to the tenant and the first
way to optimize that we start using
batches batches means that uh it's an
anoint that APIs have where you can call
send to the tenant uh APIs in batches uh
just to show you very quickly because I
want to show later most probably
interesting thing than batches uh
batches is something that you should use
if when you want to uh post
transactions. Uh how you can do that? Uh
simply let me show you uh
to granting a token selecting a 10 and
then we go to the batches. So okay here
is for example an an example. So uh let
me load some things. Okay.
Okay. So here what I need to do here I
want to post in uh in I'm I'm in
external system and I want to post a set
of transaction to my uh business central
environment in this case journal lines
uh by using you can obviously post one
journal lines for record. So this means
one millions of journal lines one
millions of calls and this is what we
want to avoid or you can directly call
uh the batch API. So the batch API means
that you need to call this endpoint
business API.enter.dynamics.com
API vual
batch uh and you can pass a array or
request and each request is
an a identify but what what this request
can be in this case is a post request
the the URL that I want where I want to
post the record in my case my journal
line uh every request can be identified
by an ID
number or something like that uh if I
post this what happens is that uh
uh request is sent to my business center
I'm not previously loaded so probably
the pro the first takes time so these
three records or two records I don't
remember are automatically posted and
here I have as a response so I'm the
caller as a response I have the status
of each call so I can I pass one million
so record and I know that for this one
millions of This is okay, this is not.
Sometimes we have also optimized that
because uh if I you can also do more
complex thing when you use batches. For
example, you you can use isolation by
passing the call this and this means
that uh your batch will be treated as an
isolated transactions. So uh or always
is success or not and uh you can specify
this this header sometimes is is
forgotten what you prefer what that
happens when you post a batch you want
to continue if there's an error or not
usually yes probably when you want to
try trans post to a set of for example
warehouse entry if I want I want to that
receive an error only for uh the
transaction that is wrong but all the
others can be uh successfully uh
registered and you can also optimize the
output. So in my case in this case uh is
what I prefer to do uh is uh the caller
can also pass this in each request. So
prefer return no content means that if I
run this
now the output is simply this.
So I I don't have uh the biggest JSON in
output but I simply have for each
element if it's okay or not not the
entire JSON that for for me as a caller
is totally unusful uh because I don't
want to know the entire JSON that is the
same JSON that I pass. So it's optimize
the transaction and uh just go back
again to the slides for the last part
when we analyze uh you as we at the
beginning I showed that the the customer
and when we analyze this customer uh
this is the situation. So a lot of API
calls during each time of the day with a
very very uh large number of API calls
very very very this is this was also
this is another one so you said I have a
very you don't have a situation like
this this was spiking more than 1,000
calls we never receive too many calls
honestly but it was really really hard
and it was giving just emmering the DNS
behind the scene but then we have
optimized
not in the way that we'll show Stephano.
We have asked the third party in order
to introduce a basketing system in order
to send batch calls instead of
completely hammering the and this is how
how it is right now and uh for so we
decided to optimize this uh behavior
because too much calls uh are sent to
the tenant. So something should be done
and uh to do to how to optimize that we
have uh you should also remember that
there's also uh not only business center
there's also something out outside of
the business central box that sometimes
can be helpful to you and this is
exactly what we uh have done. So we are
first of all start analyzing the queries
the API quizzes that comes to that tener
and we discovered that the most part of
that was get operations because a B2B uh
different B2Bs need to call how is the
price for this item how is the inventory
for this item how is the availability so
a lot of gets and we decided to optimize
gets how using uh a middle layer between
APIs and business central with caching
uh this permits to uh what happens in
very quickly show to do that. It's very
easy to implement these scenarios. This
scenario is simply creating a wrapper
between business center and your
external system. This wrapper is uh a uh
this
let me close something. This wrapper is
a simple Azure function.
Uh this
a simple Azure function that works
connected with a cache. The what cache?
The cache is in Azure. There's a nice
service called Azure radius cache that
you can use. So the trick here is the
API external API calls are sent not to
api.buscenter.dynamics.com
are sent to an endpoint that is my Azure
function. So this simply acts as a
router
that you you are an external system. You
are calling for the availability of this
item or for the address of this
customer. Do I have this data in cache?
If yes, I return this data immediately
without going to business central if not
then it forwards to business central
calls the business center API uh gives
the customer saves the data on cache and
then so on. So it's very easy to imple
implement that with few lines of code
like in this example. So here uh I have
simply an htt http get azure function
that uh simply receives the get
operations uh retrieves the token. Okay.
And simply what what is doing here is
retrieving the filter or not that you
can p you have passed and checks if the
data is in cache data is in cache if if
yes
is returning data in cache uh like this.
Otherwise if data is not in cache it
sets the the value in the cache with a
a delay
when I consider the data valid or not.
In this case five minutes I consider the
data valid for five minutes. If it's
this period is expired data is the cache
from expires and then I return the
report the records uh what happens here
is I hope to be able to show that here
is uh if I calling for example I want to
retrieve the data for a customer. If I
call the standard APIs standard API
takes about
this time. If I call this endpoint, this
endpoint now
takes quite the same time. But because
the data was not in cache, but now the
data is in cache. If I recall this, you
can see that now the time is very
limited. And this second call, third
call that I can that I can that I can
run. So all the other calls are
immediately executed and are they are
not redirected to business central. So
business center you offloaded I can uh
continue to do that send one millions of
calls immediately and they respondse
why if if this was all redirected to
business center you uh you have timeouts
or too many requests and something like
that and this
uh saves a lot. So we change uh this was
our situation. So after that trick we
move from from this uh from this to
this. So uh all the all the get
operation was absolutely reduced.
Obviously where so this is a chart that
shows you the response time also we also
gain in response time for many of the
massive operation that we have in these
uh customers and also obviously the
problem what is the post? The post is
something that you cannot cach. So if
you want to post something uh for the
post we have simply in some scenarios uh
use the same trick. So we use the Azure
function as a middle layer we uh encue
in Azure Q or Azure service bus it
depends we inq encou
the trick is serialize. So this business
center then takes and cue the the the
queue and handle the post. So this can
be useful if you want to also detach the
massive posting to the business central
uh service. This helps on saving
times and locks. So these are tricks
that we have applied to our customers.
Uh I hope that uh some of these you can
apply to to yours. Uh if you have
question now we have a slot for question
we have also here some t-shirt if you
want to and ducks and ducks also we want
to share everything so feel free to do
the question that's the first question
thanks a lot
question
t-shirt uh microphone
uh okay uh do you prefer to using Asia
functions for these things or Asia app
service web
Sorry if I repeat the question. Uh
what's your preference uh regarding
using Azure uh functions uh instead of
Azure app service web? Uh we have used
we use an Azure function in this this
example an Azure function in the flex
model. There's a effect model is a new
Azure function deployment model that has
the advantages to be extremely scalable
and also the advantage to don't have
gold start. So it's immediately reacts.
Uh it's absolutely much more performance
that they're using uh standard API
exposed on app services much much
faster. Uh so for us was a winning a
winning choice. Okay.
Good.
T-shirt or duck?
Duck. The t-shirt. T-shirt. Uh, so the
data you have in cache um
when you call the theure function. Thank
you. Uh so is not making that is not
real time. So uh it's not the same thing
that if we ask the external system to
reduce the the frequency of the API
calls.
So I think if the frequency is highest
it's only to have the uh the data in
real time right well the thing is that
you have to define for every single
entity the how much it is defined for
you it is good for you to stay in the
cache. Exactly. The trick of the cache
is useful obviously when uh for you is
okay to maintain the data. So for
example, if I have an external system
that needs to check for uh the address
of the customer or the shipment address
of the customer uh probably real time is
not needed because uh or or in your
business you can define that for me uh
the data like in my example the data is
valid for five minutes for five minutes
also if someone in the minutes number
three changes the address of the
customer uh is the valid data valid is
what I have in the cache. Okay. Uh this
is an assumption that we you need to
check uh obviously in your uh but so in
your scenarios when you have multiple
interface that's called the the customer
API right because if there are only one
I ask to to that interface to
uh reduce the the the timing of the
calls right exactly okay thank you the
function is one that simply routes the
retrieves the call instead of calling
API business
We takes the the URL redirect to the to
the API
duck
shirt. Oops. M there are lights. No
problem. Um uh just I have a small
question um about uh retention policy
strategy. Yeah. Uh for example uh if you
have a LO table uh used to track uh
process operations and it this table
belongs to another extensions
and not to uh my own extensions. Is
there a way to uh to apply retention
policy for for such table?
Uh you can define yes you can define the
retention policy for this table like you
do also
for the base application also for the
other ones. Yeah, it doesn't belong to
to my own extension. Yes, but you can
apply retention policies for sure. you
need to add in code uh that you I
remember I I I have tried but uh you you
you cannot
the third party then how you do it with
the B application B application you can
uh your extension need to depend from
the others obviously otherwise you don't
see the and then in code you can
register the and you can do whatever
whatever you like okay plus the
permissions yes and the permissions
otherwise it gives you an error your
license
blah blah blah blah. Sounds good. Thank
you. Working
checks the current module information
when you call this method. You have to
be the module that adds this table to
register it uh in the with the system
app procedure. Only the the owner owner
the owner of this table the app the app
can edit. then you have to talk to the
other publisher or if it's a base app
use the base app contribution pilot and
do it yourself as I've ordered it for
about 10 tables honestly never had this
kind of problem with the one that I have
to put it into rotation policy always
owned by by us otherwise you have to ask
mention it Microsoft in order to allow
to be added into rotation policy or the
third party in order to to create
attention policies. Okay.
