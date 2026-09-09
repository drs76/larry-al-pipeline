# BC TechDays 2022 - Telemetry for Business Central from basics to advanced usage

- **Source:** https://www.youtube.com/watch?v=6TGsPTPtBEY
- **Video ID:** 6TGsPTPtBEY
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 95m59s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

Ladies and gentlemen, welcome in this
afternoon session. Your hosts for now
are Kristof and Kenny.
Good afternoon.
After lunch.
And I hope we will not need to sleep.
Uh, welcome on our session about
telemetry. We will try to show you as
much as we know about telemetry.
Uh, so it will be from basic basic
examples for to more advanced, but let's
start.
Let's start
with few words from us. So, maybe Kenny,
you will start.
Yeah. My name is Kenny Pontoppidan.
Oh, by the way, we have 2 hours together
here. Me and doing a little extended
set. No, we're not.
We'll stick to 90. We have plenty of
things to show you, but we'll still
stick to 90 minutes. My name is Kenny
Pontoppidan.
I am an old dinosaur, maybe not so much
in NAV and BC space. I work as a program
manager for Microsoft for the server and
database reporting, performance,
stability, and partner telemetry, what
we call it. So, this is what we're doing
here.
Um, yeah.
And I heard that he is using telemetry
every day. All right, so
Um my name is Krzysztof Białawąs. I'm
from Poland and I work as a developer,
but also a system consultant.
Um I'm Microsoft MVP uh
and I also um
focus on telemetry. Quite a lot of
things I'm trying to do that.
And
yeah, I'm working with that every day.
Before we will go further with the
session, uh now we would like to learn
little about you.
When you already join, so you can take
your phones. That's only one time.
And we would like to ask you a few
questions before we will start.
So, you can scan the code.
Is it working?
Yes, it is. I see.
Okay, so let's see where you are
working. So, that's the first question.
Okay, most of you are working for ISV.
I'm really glad because I'm also working
for ISV mostly.
And then ISV VAR. All right.
Can I I think someone from Microsoft
also joined because You're It's okay.
You He's here as well. This is a This is
a great crowd, Krzysztof. Yeah.
Because we actually have something both
for ISVs, for VARs, and end customers.
So,
hopefully there's something for all of
you here. Yeah. Okay, let's try with the
next one.
Do you use telemetry right now?
That's great. This is fantastic. Now
you're in for a treat because with a lot
of the things we're going to show you,
you will have click clickity click
insights right after well, you probably
need to enable telemetry, but then
like today you will be able to go and
have Power BI on all your data. Wouldn't
that be nice?
Yeah.
Okay, thank you. We will use it
still, so don't close the
don't close the app. At the end in the
QA session, we also will have one
question for you. But what we will be
talking about today, we are in the movie
theater, so you can see also some
movies, but we won't like to tell you a
little about basic of telemetry. It is
great because most of you is still not
using it.
We want to show you also how to
get some
custom telemetry, send your own signals,
right?
How to use the Power BI.
So, do it very easy and analyze the data
there.
And we also want to talk you about the
notifications, right? So, how to be more
reactive, how to
get more information,
not only just see the data, but also do
something with that data.
And one question which is very common is
how to control the cost, how much it
cost, will it not blow up and we will
not need to pay hundreds of million
dollars and so on. So, that also we
would like to show you what you can do
not to spend money on it. And
good that we have Ken here, so he will
also be able to tell about the plans
what are planned in the
next releases. Right? So, that's our
plan for today.
Not this button. So, telemetry basics.
Uh what is telemetry?
So, that's something automated, right?
So, it's automated communication. Some
system sends us data data from many
sources, right? So, it's not only about
Business Central, but it's in general,
right?
What does it mean for us?
It means that we have less calls and
emails. We can get information faster,
right? We don't need to ask the customer
the questions which we already have
answers.
So,
how we can use telemetry? We can use it,
for example, to improve the customer
experience, right? How customers are
using our software. We can monitor uh uh
security with uh permissions and so on.
We also can check what is the health of
application,
and also quality and performance. We can
check how our application works, and if
it's a good quality or performance.
What does it mean for us?
We will uh uh see the issues before
someone will scream on us, right?
So, that's why we need it.
So, who can use telemetry?
Especially in Business Central. VARs,
right? But also end customers. You can
share that telemetry with them, maybe
even store the telemetry on their Azure
subscription. ISVs, right? And also
Microsoft is showing is using it as
well. You seen it also on the keynote
when they told that they were doing some
changes because of that.
So, what kind of telemetry we have?
In fact, we have two
two most groups. One is a platform
telemetry, and one is a custom
telemetry.
All right. So, we can distinguish those
two and sometimes I will be referring to
that.
Uh what does it mean in fact uh for us
as a Business Central developers?
The platform telemetry is sent
automatically. We cannot do anything
with that.
All right. So, it's just sent.
Uh
and the second part is something which
we can develop, we as a developers. So,
we can uh develop the signals, which
then will also go to application inside.
As you see, we store the data every
every data in application inside. That's
something which is part of uh Azure
platform. And what we can do later, we
can export this data or do something
with that. So, the first one we can uh
for example, uh see the data in Power BI
report. The second place where what we
can do is we can for example send the
alerts from application inside directly.
Or we can use Logic App Power Automate
or anything which can connect with uh uh
with uh API uh to application inside and
send information. We can uh for example,
uh send information on Teams, by email,
or for example through uh
directly to Azure DevOps reporting the
bugs.
So, what kind of telemetry we have? And
now, that's really crazy number of uh
telemetry which is. So, you can see
environment life cycle, company life
cycle, extension life cycle,
authorization, permissions,
configuration, uh package database
state, and long-running queries.
I will not go through all of that
because we don't have time. Uh on the
workshops, we try to explain most of
them, and it still was a lot of time.
So, I will just tell you my favorites
here.
For example, extension life cycle,
right? You can see if your customer
is installing some app or upgrade failed
or anything else with that,
right?
Or the second one which you can see is,
for example,
database state. So, you can see that
deadlocks, lock timeouts, and waiting
statistics, which is very also
I think you will show this example very
crazy,
right?
But, it's more.
If we will go further, we can see emails
if someone send them or successful or
not. Error handling, sensitive field
monitoring, job queues,
page views, report generation, retention
policy, onboarding, which is new, and
also web service requests.
You can see that some of them are also
on prem.
Those red ones are also on prem, but I
will explain you a little later. So,
from that list what I have, my
favorites. For example, job queues. You
can see if someone failed the job queue.
Probably on app source or you develop
the functionality which says, "When my
job queue stops, then I'm sending email
or have notification about that."
You don't need to do it
anymore, right? You can just use
telemetry for that, for example, with
the notification,
right?
But, one very important thing which I
need to say here, everything what you
will see in the telemetry is GDPR
compliance,
right? Which means that, for example, in
the job queues you will not see exact
error.
You will see just that it failed, right?
So, that's very important thing.
So, ESV
little less for us, right? As as I'm
saying because I also working for ESV.
So, what we have AppSource
submission process, Key Vault secrets,
uh extension life cycle again, right?
Error handling, long-running queries,
page views, report generation, web
services.
Right? So, you can see there's also a
lot of things which we can do. Few which
I really like and which helped me a lot
is for example AppSource submission
process. I don't know if you know that
Microsoft is validating all the apps
with all the countries which you specify
on AppSource, right? Or partner portal.
But also is validating all the apps with
the
uh with the version which you specify in
uh application
uh
field on app.json.
So, I found that my app is failing
because I put version 19 there and I use
something from version 19.1.
Right? And typically I would not find
it, right? I would just have an error
and I would not know why. But I seen it
very clearly why it's failing. I seen
everything else was okay, but this
particular was failing.
Right? So, I was able very fastly fix
that
code and submit the app the same day.
And the second one which I really love
is error handling that I can see the
errors which users have. Right? So,
every time when someone hit the error,
I will see that.
It can help me a lot in improving the
process. Imagine you have error which
you think no one will get
and 50% of your sessions or your users
are getting this error.
So, something is wrong with our
application Either with the process,
right? Maybe we should redesign that
process
to help users, right?
And the last one, probably
Kenny will show this as an example
later, page views.
I can see where my customers are, right?
Which languages they are using, which
clients they are using.
So, if for example, manager comes to me
and say, we should focus on web client
or tablet client or
or phone client, I said, "No, because no
one is using it."
Right? I can reduce the time time of
testing because of data from telemetry.
And the second, I can also prioritize,
for example, translations. Translation
are
to be honest, expensive if you want to
do it very well. So, if you're doing it
if you do that with
telemetry and see which languages they
using, you can very fast see where to
invest your money.
Okay, I was talking about
all those all those numbers, right? All
all those groups of telemetry, but in
fact, each telemetry has special
special event ID in the database. But,
there are four groups which you can
remember when you will see each event.
LC starts with life cycle, RT runtime
events, client events, and application
events. So, that will help you also
later to follow some of the examples,
but also how it's work.
So, I said about the VAS, I said about
the ESVs, I said also about
that Microsoft is using telemetry,
right?
Oops, I need to go back. So, uh
they are
using it a lot, right? They using it
also to improve the system in many many
places. So,
also we need to be aware aware of that.
Uh and very important link,
uh
this is where all of that what I said
till now you will find in the
documentation, right? So, all the events
IDs, you can find also the event IDs in
the documentation. That's pretty much
most of the things which you can
learn from the telemetry. You will find
it in the documentation, right? And
those red dots which I said, that's
something which we found out, to be
honest, and I know that
in documentation it's also will be very
fast updated, right? So, have it on
mind.
Okay, can I So, if you can explain us
how to
query telemetry? Yeah, thank you,
Kristof.
So,
bear with us a bit here in this session.
Um
We're doing a little bit of technical
things first, and then
a lot more with clickety click and ease
of use.
Um
and I think that's important because
it's kind of we want you to feel a
little bit pain, and then after that
when you get to the nice stuff you go,
"But it's not It's not really that bad."
When you
start with telemetry,
the I mean,
there's one thing you have to do, and
that is enable it. You can
enable telemetry either
as a var on your environment,
and this is done for online in the
tenant admin center, or using
the tenant admin center API.
Or if you're on premises, you would need
to use PowerShell for that.
The second option is if you are an ISV,
you can instrument your app or your
extension,
and put in a connection string in there
and that will show exactly the
difference between this VAR telemetry
and ISV telemetry.
And that's basically how you set this
up. So, that's that's fairly easy.
Now,
to consume this data,
the most like say the raw data, the way
you can query that is using this Kusto
Query Language, KQL.
That's also where telemetry maybe has a
reputation of being oh, this is
something very technical because this is
where it all starts. If you cannot query
or at least know how to query the data,
is that data really use- useful?
Um once you then put on visualizations
on top, maybe you don't actually have to
know this. So, if you think KQL is not
for you, that doesn't mean the telemetry
is not for you at all.
Anyway,
KQL is a query language. Um
if um
let me ask just the crowd, how many of
you have written a simple SQL statement
in your life like SQL? Yeah,
nice.
How many of you have done anything with
bash shell scripting thing? Oh, cool.
You're almost like as old as I am.
That's nice. Uh what about PowerShell?
Any PowerShell easy? Okay. I think
you're going to love KQL now because you
have the beauty and the like the
semantics of a a data language like SQL
and you know the benefits of having pipe
piping results through different things
in a in a process like language and
that's exactly what KQL is.
It is a beautiful child between SQL and
PowerShell.
And um and it is blazingly fast. It's
big data, really really when when we say
big, it's it is really really big.
The I'm I am to show you a demo on our
Kusto cluster, which is the same as as
yours, but just with with our data in
it. And we ingest, I think, 4 TB of of
data a day into that. So, what I'm
querying in in that demo is
I don't know.
A few petabytes, and you'll still see a
results in 30 seconds out of that.
So, the transition between SQL and KQL
You can think of it um
there's a few things if you if you kind
of know SQL that would make your life
easier when you when you learn KQL.
In SQL, it's a declarative language. You
start with a select statement, you do a
from, you do a where, group by, order
by, and so on.
But when the database is is executing a
SQL statement, it doesn't do it like
that. The database will always start
with your from clause, and then your
where clause, and then the group by,
then the select statement, and then the
order by. And that's the actually the
same thing that happens when you write
Kusto.
You always Let's see if I can point
here. Wee.
You always start with your table, and
then
you should project you should do your
selection as early as you can to filter
early to make sure that your result set
is as small as it can be.
Then you project the day the data you
need.
So, project here is the same as select
up here. Actually, if you think of it,
the select thing in SQL comes from the
project operator in relational algebra.
They just made a bad name for it in the
language.
So, you project whatever you want, and
then you do a not a group by, but a
summarize, summarize something by, and
then you can do your order by, and
that's kind of
how these things relate to each other.
Except, of of
that with KQL it doesn't stop there.
If I want to
I can put more pipes down here. I could
do more projection, more summarize, more
blah blah blah blah blah.
And that's where the analogy breaks down
between SQL and KQL and where KQL
becomes really really really powerful.
Let me show you a few examples
what you can do out of the box in KQL.
So, you could do let expressions both
for
variables but also for data sets. So, if
you want to do some pre-calculation
and use that later in your query here.
For instance, here I do two query
expressions with the uh defined here and
then I do a union between them. And then
after that union, I can do a join to to
other things.
Doing this in is possible in SQL. You
can use common table expressions, but it
kind of gets really hairy
very very quickly in SQL.
Something SQL doesn't is not born with
is regular expressions. So, for the ones
of you who did bash, you probably also
did regular expressions. How many
regular expressions anyone?
Yeah.
That can yeah, make you tired. Not
looking at you, but looking at regular
regular expressions. But it is very
powerful, right? If you want to pass a
log, if you pass strings, regex is is
fantastic. And it's built into the
language with KQL. So, you have a parse
operator where you can simply parse a
string with some pattern and it would
magically just give you new columns
based on that structure.
You can do
extends which which would be create
myself here some new calculated columns.
And
you have the most powerful window
functions I've ever seen.
Where you have a previous operator here.
So, here I'm doing get me some data from
traces order by time. And now I'm
looking back up in the result set. I can
do look back 1 2 3 4 5 rows up or I can
look down further down. And now I can do
so I can and say please give me the
timestamp of the previous row call it
previous time and then extend again
during make me a duration column with a
difference between the these two and now
I have suddenly done a window function
like do that in in SQL you can do it.
It's not going to be fun and definitely
be be hard.
And you can even do
you can even you can do rendering of of
histograms or pie charts or what have
you in just inside the language. Once
you've done some data analysis you can
render some visualization of that
to make it easier to understand.
Now
90 minutes we could do KQL in 90 minutes
and just leave you teach you the basics.
I wanted to show you some something that
can really help you if you want to get
started with KQL on business central
telemetry. Here in BC Tech on the
samples app insights and KQL
queries we have a lot of sample queries
created for you. Actually everything you
get in telemetry in business central has
a query here.
So you don't have to write KQL from
scratch. You can just copy paste and
start analyze from that.
And in here I added an examples.txt
to give you some like a few queries that
where you can learn some some concepts
from. How much time do I have? A few
more minutes? Yeah. Is that okay?
Can I steal that?
So let me show you a few
examples of what you can do in KQL here.
I switch over. Perfect. Here. So that
this is just a text file. You can get it
from GitHub.
So one thing that is very often you do
in data analysis on telemetry is give me
the top 10 most blah or top 10 least or
some kind of of of top 10 of things. So,
so that's something you simply do with a
summarize and then an order by and then
a top
top clause. Let me show an example of
that.
So, here is
a query about apparently component
updates. If only I have some good Wi-Fi
that would open that query. If not, I
have a local copy.
I will take a local copy of that.
Let's see what that is. That can
actually
Yeah, no, not I don't have that.
That helper query is Let me just get
that here.
Component updates.
So, here you can see an example of of
this pattern should you need that.
A top 10 of something. Here we summarize
the max of something by something. We do
an order by
time in this case timestamp descending
and limit limit 10. So, limit is give me
only the 10 rows.
So, that that's one very common thing
you would do
many times in KQL. And and for all of
these things I I mentioned, let
expressions, joins, and so on, there are
some example queries or samples queries
that use these techniques that you that
you might want to take a look at
after this session on your way home.
Um
one thing in particular just because I'm
very proud of this query,
took me 4 months to write 5 months to
write because I couldn't simply get my
head around this. And that's related to
this database wait stats. If you went to
Milos'
session on SQL performance, did anyone
go there?
Yeah.
So, he mentioned something about
database wait stats. Database wait
statistics is a way where you can take a
snapshot of what the database was
waiting for until the database was
started until now.
On 23 different categories of locks, IO,
blah blah blah.
Now, that is totally meaningless numbers
until you take a second snapshot to
telemetry. And now we can diff these
numbers between these two and say what
did the wait database wait for on locks
and so on between these two timestamps.
That's what I wanted to compute the prop
and you you need this previous operator
and so on.
But it I I I couldn't simply make it
work because you also need to cater for
like when you go previous, is that
within these 23
categories
or are we changing to a new
environment or what have you? So,
so you need to do a lot of crazy stuff
and I'll just show you what that
actually means here in Kusto Explorer.
Have any anyone using Kusto Explorer, by
the way? If you are.
Yeah, there's one there. Great. If you
not if you're going to query anything
with this, this is my favorite querying
tool and that's a link for it on PC
Tech. Um this is the query
that that I wrote for that. So, first of
all, you always want to filter early,
especially if you have a lot of data.
You don't want you don't want to
query billions of rows
for experimenting with this until you
actually have a query that works. So,
always put in some kind of timestamp,
maybe 7 days or something.
And then you query for whatever event
you want. In this case, it's database
wait snapshots and you project early to
make sure that your data that you only
get the data
uh going forward that you want to work
with. Uh that will speed up things.
Now, you can do things like pivot. You
can pivot this. In this case, you
evaluate a pivot function on the
category and you're summing your wait
stats. And then after that,
we have new columns. You can see these
columns to the to the right, CPU,
buffer, and so on.
And we can summarize all of these to get
uh after this step
all of this um
these measurements in one row for each
measurement that is happening.
And then after that, we start looking
back with this previous operator I told
you about. So, we look back and see what
was the previous measurement. And then
we um
we need to know that these are
coming in the order of which environment
and then coming in in the timestamp
order in the chronolog- chronological
order. And if they are not, if you are
looking at the previous result from
someone else,
you need to throw that away.
And it moves on and on and on for 120
lines. Uh I won't this like do anything
with that, but then after this this is
this is actually on our uh own
telemetry.
Um I can now see for I normalized the
environments here, but I can see the
look the look back period of between
these two were 900 seconds. And in here,
these are the most things we wait for
the most on the database on on these
different categories. So, for this
particular point in time for 15 minutes,
we were waiting a lot about
data IO,
buffer buffer IO, um getting data in and
out to disk.
And we had a bottleneck there.
So, this is very very very big advanced
example that you
hopefully will will never use, but it
will I wanted to illustrate kind of the
power of this language is is immense.
And
once you get started writing any KQL,
you're just going to love it. I know.
And you query a lot of data, right? And
you query a lot of data, yes.
Okay.
Let me little jump to
something which probably you are doing
for every day. So, AL.
And talk
a few minutes about the custom
telemetry.
So, what we can do with the custom
telemetry? We can use it to improve our
product.
Right? We can use it to see which
feature
uh
users use.
Right? We can also
see something different. We can see
which they are not using.
Right?
So,
we can then decide.
Should we
deactivate the feature because it's not
needed? Or maybe we should do something
with that feature.
Right? Maybe we should do more promotion
about it.
Right?
So, this is what
custom telemetry allows us.
At the end, we can use it
to be a better
to to do the better customer care for
our customers.
Right?
So, that's only the concept, but I'm
using it every day and trust me, it's
very useful to see where your customers
are. Right? But you also can use it to
onboard your customers. Right? To see
how much
what they did already. Right? Even not
contacting with them.
Right?
So, how it's look from technical
perspective?
Uh we have something which is called
feature telemetry. And this feature
telemetry is a part of the system up.
So, you can see that in the
on the GitHub already.
And there is one specific code unit
which you need to know.
Uh it's a feature telemetry and there
are two functions. One is the log
update.
And the second one is log error.
Uh basically log uptake allows you to
find if we discover the feature, so if
user discover the feature, if set up the
feature,
use it, and also undiscover.
Right?
So, imagine situation that you have
something you added to the product or um
you want to
you put it on the on the setup page. So,
you can assume that if someone opened
that page,
the feature was discovered.
If someone click the button,
for example, some option or something
more,
he set or he or she set up the this
feature. Right?
And when using it through the code, you
can log if someone used that feature,
then you also can see how many times.
I also mentioned that all errors are
are in the telemetry already visible, so
why we need to have a log error?
And that's something which allows us to
find the errors which are not displayed
to the user.
Right? So, and also the places which you
think that no one ever should get in
your code. I bet you have such.
Um
what is most important and I will show
you also this uh code unit, uh it's not
only just running one function.
We need to specify
that and make some transaction, make
such such contract, I would even say,
that we will send this feature
telemetry. Without it, we will not do
it. You will not see it.
Or I should mention,
VARs will see that you want to send some
telemetry.
Right? But ISV will not get anything.
And also, when we are using feature
telemetry, behind there is one function
which you also can use in the code um
in the code uh directly. But that's when
you use a feature telemetry, you are
sure that this telemetry will go to
everyone.
Which means it will go to VAR, but also
to the app
uh
app uh
publisher.
Right? So, both of those
uh those features are uh those signals
will be emitted.
And very important thing, please also
remember you shouldn't ever ever send
something which is not GDPR compliant.
Right? So, no one will check that, but
that's in legal, I would say. Probably.
Or you can have at least problems.
So,
uh
very important thing as well is that uh
all the events which we will just uh see
in the second
uh e will be prefixed with uh
with two letters AL.
That means that
uh remember that when you will try to
KQL uh
you will try to find your signals, you
always need to add AL as well.
So, let me go to the demo.
I will just want to show you how to how
you can emit the uh telemetry. So, first
which I said is that you need to have
something which is
telemetry logger.
Right? So, uh in this code unit uh which
implements the
uh event telemetry logger
uh you need to have one function which
is uh log message.
And that's in fact something which you
just need to copy.
And the second one which is uh the event
subscriber
uh to code unit telemetry loggers
and on registration telemetry logger
event.
When you do that, you just need to
register your logger. So, this is our
contract where we are saying we will
send telemetry from this app.
Right?
When you do that setup,
there is another uh function which you
can use, and I have here uh mine. So,
for example, I would like to send
uh uh send the telemetry when someone
discover uh my uh
a feature. Right? So, I just need the
code unit
and this function from the code unit log
update
and my event. Right?
Uh so,
as I said, this event, if I will look on
it for uh in the uh in my uh telemetry,
will also be prefixed with AL.
I need to put some uh description, so I
put easy translation as a um as a
description, and my enum which says
either this is discovered
or setup
or, for example, used.
So, this is how simple you can send your
own telemetry.
How it's look
in
uh in uh KQL.
Uh if I will just try to find it, this
is little different signal, but the
same. So, you can see that I have my
feature telemetry. Maybe I will just
make it little bigger.
Hopefully.
So, I can I I see my
message that a feature custom telemetry
is used.
I can see in the dimensions which tenant
ID sent that,
right? So, I can identify my customer.
I can see which extension sent it,
right?
I also can see from which company it is,
but I also can see that this is my name
of my feature,
and this is my
uptake status. So, this is where I see
that I use it, right?
And my signal
uh I I have it a little lower, but I
also can see the object number, right?
So, which object sent it, which object
name,
and also
is that this was the code unit, right?
So, as you can see,
this is my signal which I sent before.
So, I can see if someone using my
feature, if someone discover it, and
also but how often also used. Maybe you
have some features which are used only
at the end of the month. So, it can also
help you to somehow uh track the
performance,
right?
Think about uh that.
Okay, Kenny,
uh we showed very interesting, I hope,
KQL, right?
Uh
and very very, I would say, advanced
example,
but I think you have something which
will be much easier.
I think so, too. I hope.
So,
there you go.
Before I do that, I just wanted because
I maybe I I forgot something when I
talked about KQL.
If you haven't seen any of any of this
before, you're kind of you're going
event IDs here and custom dimensions
here and so on. So, I just wanted to
kind of give you a an an easy way
if you start looking into telemetry to
kind of get to the documentation of
things. And the reason for that is that
when we designed the telemetry feature
from Business Central, it was important
for us that it was had some, let's say,
design principles. First of all,
it must be treated as an API because
once you start querying against this
telemetry, we don't want to break your
queries. We don't want to break your
reports on it. So, that's the first
thing. Second thing is
it must be
uh documented and discoverable in docs.
So,
if we just throw a lot of telemetry at
you and don't tell you what this is, it
you cannot use it for anything. And
that's the third thing. It must be
usable and actionable.
So, we will never send any telemetry to
you
that you cannot take an action on
because that would just be flooding you
with
meaningless data that you're going to
pay for. So, that's even double double
bad.
So, when we talk about this
mhm
looking up things in docs,
I just want to show you something very
easy to if you see something in
telemetry, how can you actually go and
read about what is this about and what
why do I see this?
So, here I'm looking at the traces is
where we put all the telemetry except
page views.
And I take just 10 10 random rows.
And I project when did it happen?
The message is just a you human readable
version of this. And this custom
dimensions is where all the data
actually is stored. So, the first one
here is operation exceeded time
threshold. What is that? So, if I go
down into this
uh custom dimensions
down here, this is just a JSON
structure.
We, uh, we have this event ID on
everything we emit to telemetry. When
Kristof was putting things in log
message, he put an event ID, the
platform, the client. We all use a
unique ID for a certain class of things.
In this
for this thing here, it was RT005.
So, if I don't know what this is,
I can just copy this string and I can go
to docs.
And the docs for telemetry is
aka.ms/bctelemetry.
And, uh, I can just put that RT005
in here and search for it in docs.
And here I can see it's apparently
something,
uh, RT005. Let me find it here.
005.
It is a performance, it's something with
SQL.
And now I can read about what this is.
So, in case you find something in
telemetry and you don't know what this
is, search for that event ID in docs and
you can read about it. So, that's
discoverable and documented.
All right, but
this is all very low level and also
where I think maybe telemetry got a
reputation of being only for support
engineers or
people who who's who are developers.
Which is a shame. Um, I know why,
because when we started
taking Business Central to the cloud,
we needed to have, um,
you as partners, if you were to put your
customers online, we would not, well, we
couldn't make you do that if you had no
insight into performance, availability,
stability into that system. That's why
we started the telemetry
raw signal on exactly this. And we
started with
these um
custom queries. And I was young and
naive back then. I thought, "Okay, now
we have data. I give you samples to make
it easy to query data." So, this was
will will just automatically make you
data driven. What I of course didn't
realize was that you have a lot of
prioritize priorities in your partner
practice.
There are a lot of different things
you want to do and learn that compete
with telemetry, right? So,
Kristof and others told me like you need
to make this ev- easier and better. So,
I started making troubleshooting guides
available in Jupiter notebooks, Power BI
reports that you could download, and on
and on and on. And now I thought, "Now
we are here.
Now you will be data driven with this."
I didn't realize that even for some
partners,
that is also a threshold you need to
pass.
Maybe it's still keeping things in the
in the basement with the techies.
So, Kristof came back and he said,
"You need to make it click clickety
click.
That's That's That's what you need
for everyone to consume this outside
support org. You need to make it very
easy to install and consume."
And so, I listened to him and
went back to my
friends in Power BI and they helped me
get a Power BI template app published um
and this is actually what you have now.
So,
I wait because we are here. Oh.
That is probably good.
Um so, if you go to
aka.ms/bctelemetryreport,
this will take you
to Power BI AppSource, where you will
now have a Power BI app called
Business Central Usage
Analytics.
And the way you install this is
clickity click. You click get it now.
It will take you to your Power BI
subscription, and then it will install
it for you. And if I'm
if this
cloud thing doesn't work, I just did
that. So, you don't have to wait. It can
take 10 seconds, it can take 30 seconds.
And this takes you here.
The app installs with sample data,
which is actually something you can even
use for pre-sales uh because you don't
have to share customer data if you just
want to show how this looks. If you want
to demo it, you can take that That's
actually some of the scenarios we try to
put put out there.
My dream is that it This app will make
telemetry something you consume both in
your pre-sales organization with
follow-ups with customers, in
implementation projects,
functional consultants, and then also
the the the performance investigations
and so on. But if you
get this part of your power your
partner organization involved,
it will not be only a technical
exercise, but something that can truly
make your partner practice
data-driven.
And I saw end customers here. This is
great because you you could have this as
well. If you together with your partner
um
decide who needs to host the telemetry,
who needs to host the reports, and then
the other part can consume that. Then
there's nothing in here that prohibits
that. And I think
if you have a strong partner customer
relationship, maybe this this something
that can benefit benefit both parties.
All right. So, the way you then connect
this to your data is it's it's data up
here.
You're viewing this app with sample
data. So, uh
connect your data. If you click here,
let's try that.
And um
what this does is um you need to tell
the app where is my data stored. This is
this app application insights
application ID. And you need to tell it
how many days of data how many days do
you want this app to show? Because what
this app will do um every every day at
midnight is it will refresh uh for the
next day. So, it will always look back 1
day, 7 day, 30 days, how many you figure
figure here. And the look back period
you can set up to
I think 2 years if that's your retention
policy for telemetry.
And then you just have a sliding window
of that. Um so, no need to query
telemetry with KQL anymore. Well, you
might need to do that if you are high if
you have questions that cannot be
answered with this app. But maybe start
with the app and share that that within
your partner organization. Let's just uh
for now do it with with sample data.
So, the app has four parts: usage,
errors, performance, and administration
catering for different say usage
scenarios. Um
So, for usage uh you can see sessions if
you use the same application insights
resource for multiple AD tenants. You
can uh in an easy way either filter on
it up here. Or you can simply just click
on on an AD tenant and see this
particular AD tenant had this many page
views or sessions in this case. And then
you can see what types of sessions it
is, admin, delegated, or normal users,
and whether it's interactive sessions or
background sessions. You can see session
distribution over the day, over the
week, and uh and over whatever
period of time you put into that app.
You can look at which clients they use.
Um desktop, tablet, phone, which
browsers they use, which uh screen size
they use. It could be that if you are
dealing with a customer with like big
monitors, maybe your UX will be
different than if you are dealing with a
place where they use old laptops with
Windows XP.
You can use locations report to see from
where people log in. This is from where
people log in to these systems, as well
as which
which languages do they use?
Not localizations, but which which
languages do they use in the client?
Something Kristoff said that for an ISV,
it's nice to know. Could also be for
in an in onboarding or a situation that
maybe you find out that some of that
training needs to be in Danish or in
Italian because you have people who
would like that. Maybe you didn't know
that.
You can see on page views what are the
popular pages and therefore also so that
could be used for
better go live that if you are after go
live if customer is have heavy use of a
given page, maybe help them get that on
the role center. So remove some friction
there.
Or in a user acceptance testing and
before before after go live, if you have
absence of data here, that means no one
have tested these pages. So you can So
this is your status report for user
acceptance testing right there. You
don't even have to write it. You can
just share this with your customer and
now the cost the sponsor on the customer
end can like follow along and maybe find
out what do they need to do more.
Again, you get these visuals. This is
something that is on on most of these
pages that you get representations over
the day, over the week, and over time.
And again again so so just different
types of things
in this case reporting. So you can see
which reports they use. You can see how
they run reports, whether they download,
print, or send to inbox. You can see
what types of layouts they use. For
instance, here I can see that this
particular customers have a little bit
of Excel layout usage. That's actually
nice to know after go live if you have
that 3 6 months uh follow up with the
customer.
Looks like you are starting to use Excel
layouts. Excel layouts is an end-user
feature from
version 20 where end users can actually
layout and consume their reports with
Excel. So, that means you you can start
have a different way of collaborating on
reporting where you as a partner is more
coding the
report objects and the end users are
dealing with the way they want to layout
their reports for things where that that
that that doesn't need to go on paper.
So, absence of Excel means you could
just like have this conversation. If you
if you see Excel here, it means you
could have that conversation of should
we do more about that? Should we do some
training on Power Query and can get you
more
self-service on the way you do reports.
Feature usage is now as seen from the
environment. All of this is is per
environment.
So, if Kristof and his friends are doing
their thing with feature telemetry as
ISVs, you will actually see it here.
Now, the most important ISV for this
data set I have is Microsoft because the
base app is also emitting telemetry
here.
So, you can see which features are being
used. You can see how often they are
being used and if if you have ISVs
extensions that add telemetry feature
telemetry, you will see that there as
well. Again,
if data is there, it means they are
using it. If there's absence of data
here, they are not using it. So, again,
follow up conversations with the
customer. Look,
You paid us $3 billion to create these
extensions for you to solve solve this
problem, but you are not using that.
What's going on? Should we have a
conversation about that? Or so so a lot
of this
you could
you can tweak this message in two ways.
You can say, "How can we sell more
billable hours to our customers?"
Or you could have a different way of
saying this.
How can we be that valuable partner to
our like close collaboration between our
customers and bring more value? If
they're spending money on things that
they're not gaining every anything for,
that's wasting their money. So, by
having these kinds of conversation,
maybe
billable hours is just
um like an added benefit. You would have
a
happier customers, maybe happier
developers because you're doing
something that matters.
Um
Maybe I'm stretching it here, but maybe
you get the point.
Checklists. So, onboarding uh have
checklists. Here you can see whether the
customers are actually completing their
checklists or or where they stop in
their checklist. You can see how many
went from not started into progress.
In this case, 16.
But apparently, one skipped. Um six
uh actually completed means someone
actually got stuck here and never
completed their checklist.
Could be a good conversation before go
live to see whether there's something
here that they haven't set up.
Integrations.
To and from uh Business Central, not
including Microsoft connectors. That's
the next report.
Here you can see
um if uh integrations to and from
external systems are happening.
Could be the customer had have installed
a new extension that you didn't know
about that is chatting to some Azure
function somewhere.
Whether that's good or bad, I don't
know, but here you have the overview of
that.
What are the publishers that emit or is
is having endpoints that is being
called, incoming, outgoing.
Uh which endpoints do you have?
And again, these
the chatty extensions here, you can see
which ones are chatty. And anything you
have here you can filter on, so if
you're interested mostly in incoming,
you can of course filter on that.
And then connectors is the customer
using any connectors?
Did they start up taking Power BI since
the last time or Power Automate?
Uh you can see that which endpoints they
use. And finally, you can check Oh, it
seems like this is a customer we need to
talk to because these guys apparently
are doing
uh basic auth on online.
So, we might need to start a migration
project because these integrations down
here, these endpoints, will stop working
in a month.
For each of the reports now, I just
showed you the usage report,
they have an about the report that that
tells you like what am I seeing here?
And if I want to learn more, I can also
see
if I have older versions, especially on
premises,
um when did this So, if I don't see any
data here, is it because I'm on an older
version? I can get directly to a KQL
sample of this particular type of data.
And I can go directly to the
documentation to read more.
So,
just quick
um
like hands, how many in an onboarding
project do you think could use this?
Would Would this be useful?
Yeah?
How many of you are doing things like
this today?
A few. Oh, nice.
For the ones that sits and just This
would be nice, but we are not doing it.
The app is free. It costs you $10 a
month for a Power BI subscription and
you need to set up telemetry that might
cost a little bit. And then you have all
of this. But you have more and I don't
have to show I don't have time to show
everything. I'll just show a few things.
You have a full error dashboard on
everything every error that happens in
the system whether it's a users getting
errors, whether it's integrations to and
from Business Central or errors
happening in the system. You have a
dashboard you can go directly filter on
a customer and get to what's happening.
So before after go live
user acceptance testing you can drive
these down. You can monitor these after
the fact and see whether there's an
increase in errors for a particular
customer. And each of these types of
errors have their own report just like
you had usage.
Performance. You have performance
reports similar you can dive into say
long running SQL queries. You can see
exactly here which in which places do we
have long running SQL queries, what
types of queries, how much time do we
actually spend here. You can dive
further down into
uh
where in which objects does it happen
and these are job queues that run long
running SQL queries. This is the AL call
stack. This is a SQL statement that does
it including how many joins, how many
shifts do you have uh and and so on.
And again you have long running queries
over the day or over the week. And
so a lot of things you can do in
performance not necessarily proactively
but you can maybe after if you have a
support case you can go back in time
because that's what telemetry is all
about. What happened in the past and I
can go analyze here. And then finally
for administration you get an inventory
report. Every
environment we have in telemetry we can
see you which versions they are on,
which localizations, when are they going
to be updated,
days until update. Is there a deadline
for this? Uh you can see a change report
across everything that could happen
including environment changes, extension
changes,
fields configuration changes. So, that
you can answer that question.
Something is not right since Friday. You
zoom down on the change report and you
find out it's because this extension was
installed or this was updated. And maybe
that can help you with a time to
mitigate for a for a customer case.
So, that was kind of
a quick overview of
the
um
the environment report. Can I switch?
Yes, you can do that.
But uh but there's more.
Because uh we also realized that you
have a lot of ISVs and this is mostly
for VARs.
Uh
the kind of toys here are dinosaurs.
It's not because you're dinosaurs. Or
maybe some of you are. I hope not.
Uh because you want to go into this new
world. And today we are announcing a
public preview of an app for ISVs,
specifically for ISVs. You can go and
get to AppSource today
and have that same type of experience
that the VARs have.
Including things that are only for ISVs.
Can I show one thing? Is that okay?
Yes, of course.
Let me just uh
switch to this because ISVs have
other things in their telemetry. They
actually have things like
key vault usage, which is fine. You you
are looking up secrets in your
app. But what if you have key vault
failures? That would actually mean bad
things in your app. Well, things will
stop working. You can monitor that. You
can monitor in uh in this uh performance
report how is how performant are your
updates. That means your app updates.
So, many if you have something that is
very long here, maybe you can uptake
this new data transfer
thing you saw on the keynote and make
your
uh users happier because updates are
going faster.
You can also have an inventory report.
This is now not on uh on environment
board pivoted towards how like how is my
app installed across the world on
different tenants in which versions?
And and where like which AD tenants
actually installed it.
You can again see you can see here what
are my update flows from which version
to to which version, how many update
between them. So, you have like a change
report
uh like that. And finally, you have
an ability to to see like what type of
telemetry do we have in our telemetry
and and which environments are say the
noisiest ones in case you want to go
with the thing that Kristof is going to
show you in a minute about
uh controlling cost. It's nice to know
both which environments are noisy and
which event IDs are noisy.
So, you can you can go and install this
app now uh from AppSource and connect it
to your ISV telemetry. And now you are
uh you have the ability to be data
driven there as well.
Okay, I will just uh
and I will not do marketing.
Can he's very good in marketing his app.
But to be honest, uh
I really see it like very
big value for us, right? I was uh
because we didn't have that app, right,
before. I needed to create it very
similar thing for us.
And to be honest, it was very
it's very useful. It's not only checked
by me, but it also
to be honest,
the person who first see it is is my
boss.
Uh every every week he checking it
on Monday. And I'm really glad that he's
doing that.
But I also wanted to point one thing.
Maybe you know as ESV
or by also a VAR, you can have like
the support question, something is not
working and then you have inform
then you are asking customer, "Okay,
which version do you have?"
You don't need to do it anymore, right?
One of developers in my team did that. I
was like, "Oh." It started like a whole
discussion because he asked the end cast
end user. He said that he don't know. So
in he included in email IT manager, but
he also didn't know. So he included the
partner, right? And how to check our
which version we have.
5 seconds and you have it from
telemetry, right? Either you have it
from the app, either you will take you
out that, right?
So
that's how you can work faster as well,
right? You know this data already. Don't
ask, right? And the fix was easy.
Just update to the new version,
right?
And you could say you could save a lot
of emails, right? So also show how
professional you are with that,
right?
And
two links which
can put those are two links to those two
apps, right? One is for VARs which was
already on AppSource and this one which
That was a first time.
It was. This is the first time we've
shown it actually or at. So you are kind
of the very first people to see this.
Um one thing before I hand it over to
three things before I hand it over to
Krzysztof.
Convince your boss docs. So maybe you
want to go back and say this is really
good. I want this and your boss will go,
"Mhm, yeah, but uh
I Is it just maybe another technical
exercise and is this really useful?" So,
aka.ms/bctelemery
is our documentation for for for
telemetry and in here we have documented
the the app
and under
uh here under um
use the app here is how you get it, how
you connect, how you configure, how you
share it with customers or internally.
And then down here there's a link to use
the app where we try to put in
exactly these these This is probably I
mean, you're probably either here or in
the developer part if you're at this
conference.
But maybe your your manager is
more into sales or maybe a product owner
like Kristoff's manager or maybe someone
who is doing project implementations.
So, for each of these personas
we we wrote or identified scenarios for
them where the app could be useful. So,
one once once you go and and present
this back home
take a look at the scenarios so you kind
of have some ammunition
and then uh demo the app with sample
data if you want and say, "Look, this is
how we could do it with you change our
sales process. This is how we could
change our implementation project
implementation
uh ways we do implementations. This is
how we could change the way we do
support."
And and maybe that will make it easier
for you to to implement this back home.
Yeah, we know how how hard it is to get
the internal hours, right, for
something. So, I think this is very
useful uh to get such internal hours,
right? Because at the end this will help
as I said, more to be more uh customer
focused, right? But also it will save a
lot of money to organization. Yes.
And changing an organization to be more
data-driven can be very hard. And this
is actually where this
Gartner BI maturity model comes from.
So, what I did, I took that model and
interpreted that in the context of a
partner and with data as telemetry. And
then
this this telemetry maturity model came
out of that. It has these five stages
as that comes from Gartner's model. And
for each of these stages, there's a deck
here you can go and take a look at when
you come home.
That takes you through if you're unaware
and have only enabled telemetry. And
some of you haven't even
enabled telemetry yet.
There are some guidance in the deck that
states if you are here,
try to do get some quick wins
um and that that will easily take you to
the next step.
And that that will take you some of the
things that uh
that Kristof Kristof is going to talk
about is actually
using telemetry to be proactive. Um this
part is how could you in your
implementation practice, in the way you
do
uh customer projects, use telemetry in a
repeatable fashion. And then
I won't say it's Nirvana, but it's
definitely something that I hope with
data you can change the way you do
business. And people among you that do
this well,
I think will have a a big competitive
advantage over partners who don't do it.
Thank you.
Okay. So, I would like to
show you how to be on this last
uh last step of that model.
Uh which I think uh you can achieve very
easy with the notifications,
right? So, uh
how you can what you can do in the
system. In fact, there are two three
options. I will just
show you all of them.
Uh you can, for example, set up the
alerts directly in application inside.
It's paid feature, but it's very not
flexible, right? That's something which
I don't like to use.
Uh
because you can only send email, maybe
text message, but you don't have a lot
of
a lot of
place that
to do something crazy with the
notification.
The other two options I really like
and depends what you want.
If you want to have that
that, for example, consultant will be
have will have access there, you can use
Power Automate
or you can use Logic App. I will show
you the example on Logic App, but I have
also a lot of Power Automate flows which
I can share with you.
Right? So, what we can do is we can
check if there are any signals in the
telemetry and then we can do something
with that. And that can be whatever you
want. For example, I'm sending such
messages. One of the message which I'm
sending at the as a ISV, I want to know
which tenant IDs install my app last
day.
So, every every night I'm getting an
email and to be honest, everyone almost
in our organization get that
that those people
those people install the email install
our apps.
But I'm also getting something much
often.
Oh, I hope I don't get it much often,
but I'm I'm trying to send it or check
much more often than one one per day.
So, this is where someone has error when
installing the app.
Right? And I can give you real example.
So, one of our customer installed the
app in or try to install the app in
Finnish language.
Right? Or Swedish, I don't remember.
But, in fact, it was not English one.
And it turns out that
it's not possible. There is an error.
Right? Some overflow, whatever it was.
Right? But, we get an email before they
contact us.
Right?
So, what we did, I just was uh next to
the computer. I just wrote to them, "Hi,
you have a issue with the installation.
Please change to language to English."
Right? What we later did,
thanks to that, we also change our
process of uh of installing the apps.
Right? We change the code to not have
this error. But, we also change the
process when submitting the apps. We now
testing all the apps in all the
languages which we are using.
Right? So, someone just need to install
them in each language. And that's all
because of this one small email which we
get because of the notification that
someone failed. Right? But, customer was
uh really surprised because, you know,
when you install the app, now you will
be able, but when you install the app,
you just can go go to the coffee, and
you don't see the results. Right? It's
just happening in the background, and
maybe not someone even don't go to the
extension uh management.
We contact before they knew that they
failed with the installation.
So,
let me just uh show you how we can do
it.
But, for that, I will just try to
uh enable one of those.
I don't know if you will get email uh uh
during our presentation, but let's see.
So, I said about the installation, but
imagine situation that you also can do
it uh for example for failing uh job
queues. Right? So, if I have my, uh,
job queue entry,
uh, sorry, my, uh, logic app,
uh, what I can do, first of all, there
is no uh, trigger in application
insights, uh,
in application insights. So, you cannot
get information right away. You just
need to use as a trigger something which
I'm using, for example, every minute I
would like to send an email and that my
job queue failed if it failed. Right?
So, I just use this as a, uh, parameter.
But later,
the help of, uh,
uh, of KQL, uh, starts. So,
um,
what I can do, I can run the query and
see if I have any records which will,
uh, which, uh, will, uh,
trigger me,
uh, sending email.
Right? So, let me just hide this one.
Oh, I love it.
Let me just open it one more time.
I think I don't want to write it right
now.
But I have prepared those, uh,
KQL here. So, you can see that I have,
uh,
I have very easy,
really easy, not so complicated as, uh,
Keno was showing, uh, example how you
can find, uh, failing, uh, failing, uh,
uh job queues. I just need one uh event
ID and I need to summarize to see how
many of them I have.
In the last uh
in the last 24 hours, I have two of
them, right? So,
uh good, we have something.
So, this is what I'm checking and for
each such row, uh I have a condition
that if my number of errors is uh higher
than uh is greater than zero, I need to
do something, right?
So, what uh what I'm doing if I have
more than
uh zero?
I'm just uh sending this
uh
another query which shows me all the
data in this uh
in this query uh about the job queue and
I'm just writing it as HTML table.
After that, I can do whatever I want. I
just send it as an email, right? But, I
can use Teams, I can use a DevOps uh
whatever whatever else is needed,
right?
So, uh
let me just
open
email. This is what I will get. Job
queue error.
That's all, right? But, I can see uh
first of all, I can see what the
company, what code you need, uh what
environment. I can even see which user
triggered the job queue, by the way,
right? But, as you can see, it's also uh
uh good. I can find it in uh Business
Central, but it's also uh
GDPR compliant. And I can see job queue
ID. So, imagine situation that not only
you're doing that, but you're also
sending to yourself email with error
code because you you can do it with API,
for example, and approve to restart the
job queue automatically, right? That's
only the idea. I will not show you that,
but that's what you have.
Uh we have only 12 minutes left, so let
me just go back uh
to our presentation and just show you
last topic here which I will just very
briefly touch, right? Cost control,
right? So
uh
remember that 5 GB
is free, right? And this is account per
for injection of the data, right? And
it's also per month, right? What means
injection? So to insert the data to the
system, right? I don't want don't like
the word injection. But
you have also retention policy 90 days.
That can be not enough for the ESVs
because you would like to
check more data and rather about the
installs and upgrades and so on. So
that's please remember about this. You
can extend it.
Uh but you have few things which can
control that, right? One is set daily
cap limits which allows you to say how
much data per day you would like to get,
right? If you will have more, it will
stop it will not inject more, right? So
you are losing data to be honest, but
you are not losing money.
Uh the second thing which you can do is
data collection rules, right? So what
you can do with data collection rules,
you can before injection, you can filter
the data which you like. For example,
you have a lot of
a lot of data which is related to the um
web service calls, right? And you don't
care about successful one. Uh you can
you can find on BC Tech example how to
filter that that you would like only to
get those calls which are
which are failing, right? And then you
don't need to have so much data anymore
in application inside. And the concept
which one of the community
members also did
is custom endpoints, right? So, in
custom endpoints and the code also you
can find on Microsoft blog, right?
Angel Kaufman created a function
originally to split, for example, or to
filter also the data. So, instead of
sending the data directly to application
inside through Microsoft, let's say, you
can create your own
Azure function which will get the data
and then you can do with that data
whatever you want.
Right?
Of course, you will pay for the
application for Azure function, but you
will be able to control everything. You
can store it in some database, whatever
you really want.
Right? So, as I said, the the sample is
also on the Microsoft Microsoft site,
but that also wanted to say can it put
there everything which community also is
doing. So, examples, blog post, and all
kind of that stuff.
Okay. We have just
4 minutes, but I think you just need to
explain that slide.
Yes.
What's new in telemetry? So, since wave
one
um
you can see
we keep adding a lot of
data that we think or signal that we
think is being useful for you.
If there are things of this where you
say
don't care
use a data collection rule. We didn't
actually show it here, but it's in the
deck and it's also on BC Tech how to set
it up. So, you can just ignore that if
you don't like it.
One of the
things that I
like in Wave 1 telemetry that I think is
useful
is
the
wait stats, I think, because I think
that will change once you get started on
this will change the way you do
performance tuning on SAS, something you
have never been able to see before.
Um Christoph might have other
Yeah, I have one and that's really like
in the bottom, right? So, user telemetry
ID on user card. Uh this is what I
deeply like said briefly is you can
connect your user with telemetry, so you
can track as an as a VAR who did that.
Yeah. Right? And then you think, hm.
Both Christian and Chris Christoph, not
Christian. It's a bit late today.
Christoph and Kenny was talking about
GDPR and privacy and it's all compliant.
And now you can see who did it, right?
But uh but this is actually implemented
in a way that is GDPR compliant because
we're not locking the user ID here. If
we were locking the user ID from the
user card,
telemetry would be GDPR compliant but
because now you have user identifiable
information. What we log instead is a
pseudo identifier, a new GUID called
telemetry ID. And you think, what's
different here? The difference here is
with GDPR one of the most important
things with GDPR is the right to be
forgotten, the right to be deleted.
And what you can do in the user card is
you can rotate that user telemetry ID or
you can put it to zero as a tenant
admin, meaning that you can break the
connection from the user card to
whatever is stored in telemetry. And if
that connection is lost on the user
card,
there's no nothing you can do on
telemetry that makes that GUID uh
referable to John or or Johanna.
They also beyond here on the slide. This
is something that I hope to get in
in the near or long-term future. If you
have other ideas of things that would
make your life easier as an ISV VAR or
end customer, let me know and let's see
if we can
put that into that back lock. Next
slide.
Talking about back lock, you can always
go to BC Tech and see when things was
added even new stuff. I add samples
before they go on docs. So if you if you
go to to to the telemetry change lock on
BC Tech, you always kind of have that
that view on things as well.
And then we have call to actions. Yep.
So
we would like
that you will start using telemetry.
Right?
I like it because it's really give me
some benefits. So
how you can start? The first, just do
the setup. Right? Either on your
environment, either on your app. That's
really simply simple, right? Few minutes
and you will be done.
Install those Power BI apps, right?
Either it will be for VARs, either for
ISVs, but that's already
showing you some data, right? You don't
even need to write any KQL
KQL.
But explore more, right? So there is a
lot of examples, there is a lot of
documentation about telemetry.
And as I said, samples on BC Tech you
have a
really crazy crazy examples, right? But
also very useful examples, right? So you
don't need to write from scratch your
own
KQL. And go and install the apps today.
Right? They're free.
They're open source
and will cost you $10 a month for a
Power BI subscription that you probably
already have. Per per people using that.
I'm pretty sure that the value of having
this kind of insights is more worth more
than $10 a month. I I I'm fairly certain
it is. And I would not be community
person if I would not say also go to the
blog post. There's a lot of people which
are blogging about one of them is me,
but also Stefano
from Italy also Bart is also from
Netherlands.
Maarten from Denmark as well. So I could
put much much more here, but you also
all blogs you can also find on BC Tech.
Right? So
that was it from our side. Sorry because
we have 5 minutes, but we can stay more.
We will go question in a second, but I
also would like when we
answering the questions, I also would
like just to ask you to answer our
question. Right? So
what can in fact can do for you? Right?
I can just tell that I would also want
some something from that.
And now we can go with the question. I
need to
take this one.
Yeah.
I have actually two questions. Uh we we
need some
noise on that. Blue one.
Can we
Yeah. Try now.
Hello.
I have two questions. The first is
what's the performance penalty or cost
of logging telemetry events?
Let me take that. Let me take that
first. Quick.
Is there a performance penalty of
enabling telemetry? Yes, there is.
It's probably like a
.5%.
Something. Every time you do something
in a server, it will have a performance
penalty. Will you notice? No.
Second question, how much of the
goodness we can have in on-premises
system?
Good. So, the question was on prem. You
can have actually most of this. There
are a few things you cannot have. So,
environment telemetry for SaaS is only
emitted from the control plane in SaaS,
so you don't get that.
Environment lifecycle. You don't
Currently, maybe you get, maybe you
don't get. I need to check because it
has might have changed. Uh client
telemetry which means page views,
session, uh
the session types and things might not
be available, but but Kristof tells me
it is.
And then the last thing is
Yeah, most is and it's documented on
docs which types of things are available
on prem.
There's one thing for on prem. We cannot
emit the AD tenant because you're not
using AD. So, if you use this for
on-premises, use one telemetry resource
for each environment because if not, you
have mix and match and cannot know if
this is coming from customer A and B.
Yes.
Other questions? Okay, I have the
question about cost control you showed
because if I we if we have our ISV
solution and we have this connection
string ID to Azure Insights and a lot of
customers is is using the telemetry,
how much approximately data data per
day? Of course, it depends on Yeah, it
depends on usage. So, how how much data
we can expect by customer about this
free tire will
be enough for how many customers?
I think I don't pay anything for
telemetry for our customers, right?
Okay. If you have an app that is only
doing integrations like EDI, then you
will That you will get generate a lot of
data. So, what you do in that case is
you set a data collection rule that
samples on the incoming outgoing web
service requests so that you still get
the trends, but not necessarily the full
picture. Mhm. Thank you.
Cannot hear you. Hello. Yes. Um if you
set up your own end points, what's
What's What do you mean?
repeat the question. I couldn't hear
you.
Okay. If you set up your own end point
to receive instrumentation or to receive
the telemetry,
what does it need to expect? What do you
It is a So, okay, it's a web service.
What sort of things come into it?
As the So, the details are in BC Tech.
For custom end point, the question is
what like what can you do?
As seen from Business Central, the only
thing you need is to comply with the
connection string format, which is
instrumentation key equals blah,
and then
uh the host's end point. That's it. Then
we will send you the data format from uh
Application Insights to that, and then
you take care of it. The format is
documented. The sample code uh that AJ
wrote for the filtering part is um can
pass it, and the extension I did for the
splitter function can then send it in
different directions, but it's totally
up to you.
Yeah.
You do anything with it.
Here we have a question, and then we'll
go for the next one.
Um good afternoon. Thank you very much
for your uh brilliant presentation. Uh
could I please ask a very practical
question on
uh out of the box uh Power BI. Um
is it easy, simple, out of the box
uh analyzing data by hour? So, let's say
customer says we experience issues
between 10:00 and 11:00. Is it simple,
piece of cake for me to do this
analysis? Cuz I'm only used to doing it
by day, but can I focus on a particular
Thank you. So, the the the app the data
for the app
is aggregating by hour
in in in the whenever when I read KQL
um into the Power BI apps
I do summarize by hour. I think I do.
Um so, if you want different granularity
you can either
take the source code and do your own or
you can go further into Kusto. What I uh
think I will do
when I have the time for it is probably
have some links in the Power BI app that
can open application insights directly
with a query that you can then
analyze further with.
It's not science fiction. It's just um
uh I know what to do and it's documented
how to do it. It's just a matter of uh
maybe in the next release or before
Christmas. Let me say before Christmas
you'll have that.
Right. Yeah.
You're welcome.
Yes.
Does it work? Yeah.
Um so, we have some customers that have
are very strict on a firewall on
premises. Um
can it be something that blocks like can
a customer with this firewall block the
the the signals to and and what do you
need to allow
in the customer's firewall to get it
through? Got it. The question is uh if
you are on frame and the
IT department have set up firewalls like
what you do.
Um
I think you need to
uh be So, what you can do is the
connection string that you have um
in if it's the environment telemetry is
uh has the the host endpoint.
So, you give that to the IT department
and they need to figure out in DNS
whether they can filter on host or
or if there if there's changing IPs they
need to deal with that.
Yeah, but that's very good question
because we had it from time to time,
right? So, we even had someone on the
workshop which was blocked at some
moment, right? And probably it was that
her
uh IT department or was see
something is going on, right? That she's
sending the data through the firewall.
So, have it in mind. Very good one.
Question. Yes. Hello. Um if you want to
do a multi-tenant query
using Azure Monitor, is there a best
practice for that or So, the question is
if you want to do multi-tenancy. So,
that would be if you have App Insights
data for different customers in
different App case in Insights. Is that
the question?
Yes, indeed.
So, you can do that from Log Analytics,
not from
um application You can do that from the
back end, which is called Log Analytics.
Well, you simply do a I guess you do a
union or you do I don't know the
construct actually. I don't No, no. You
can everything is going to one, right?
You can do that and
it would just scale out and then reach
back with that. Um But, that's also
a good question because sometimes I I
got it that should we have multiple
application insights, right? And in
total, if you are doing
cloud
that doesn't matter
because you always can filter on the
environment name.
If you're doing on prem, then you it's
I would say I think that it would be
good to split because then you have each
customer
you can have different application
inside because then tenant ID is common
or default.
Right? But, in cloud
for example, I for all eight apps I have
one application key, right? Because they
are connected, so I'm using just one
this application key for all, right? For
all apps.
All right. Thank you.
We have been told to come to the room,
but this is the last session. Yes. We'll
ignore that and then you can throw it
out throw it out.
So, we get a lot of questions out about
partitioning
like this. How should we partition
things on customer? And I think the
answer for me is depending on how you
want to use this.
So, if you want to use this where you
have
one customer with an app and you want to
share this with the customer,
then use partition with one one AD
tenant or one environment, one
application insights, one Power BI. Very
easy, no easy to share, no mistakes.
Then the other part of this is someone
would like to
analyze across things with the Power BI
app. In that case,
keep this and do a splitter as we told
here with a splitter function. So, it's
one copy to the customer thing, one copy
to yourself. You could even filter and
and sample your own if you don't want to
the full details there. And then you can
pop Power BI on top of that and you have
cross customer things there.
So, that you can mix and match.
It's totally especially with custom
endpoints and with these new filtering
capabilities.
There are no limits to what you can do.
Even for on-prem, you could have on-prem
where you have fake
instrumentation
uh
keys and then just send them to the
custom endpoint. They would know this
um instrumentation key is coming from
customer A, blah blah blah. And then
this guy will inject into the signal the
missing thing and just send it over. You
can do whatever you like.
All right.
Any more questions?
I think I think not. We can take
questions after if you are too shy. And
reach out, Twitter, email, whatever.
Um whenever you have good ideas that I
think can be used for other partners, I
will put them out there without your
name. Because whatever we do together is
something that helps all of us, all of
you.
Thank you.
Woo!
