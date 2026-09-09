# Telemetry: a developer's Best Friend

- **Source:** https://www.youtube.com/watch?v=PLRkN2UBhTg
- **Video ID:** PLRkN2UBhTg
- **Channel:** mibuso.com
- **Published:** 2024-06-16
- **Duration:** 100m24s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

welcome wow uh so many people on a
Friday morning at take days after
hopefully a decent amount of beers uh
yesterday uh did you have enough
beers okay oh you get the gist
okay good so uh I would like to take you
back a little bit uh 10 years ago and
you might remember that I showed this
picture um did anyone remember this
picture wow one
cool it was actually for a session that
I uh that I did back in the days
watching and and the thing was like uh
it was a power shell session and I was
like H how am I going to do this because
you know watching someone do powers
shell is as boring as watching an old
man
eat and then I was 10 years later 2024 I
was doing a Telemetry session and I was
like it's pretty much the same doing
Telemetry not the most uh interesting
topic you can do um what I will try to
uh to do is make it a little bit more
interesting so it doesn't have to be
boring to watch someone old eat and by
the way these days we have ai 10 years
later I can make Luke
smile it's a little a little bit dark up
here but anyway it's uh cool let's go
the crap uh I'm want to set the stage a
little bit some expectation um I will
just try to explain things about
Telemetry in my own words I'm not going
to do the the full official vocabulary
and I probably will mispronounce stuff
yeah I will show how I am using it today
and I might actually I'm I've been using
telem quite a lot the last couple of uh
months and I will use real world
examples including live data just
imagine how to do a session on Telemetry
and then fake the data I didn't I wasn't
able to do that so I will use live data
so you're going to see my customers um
and my
problems and I don't know what I'm going
to see so because it's live so I have no
idea I looked into it yesterday a little
bit so I might be some some yeah
hesitant at some points so I will show
some ideas as well things that I think
would be interesting but it's not fully
implemented yet um I you will see a
disgusting amount of
kql that's a
warning I apologize already um and an
unhealthy amount of demos yes lame jokes
if you go to a wo session that's what
you're going to get sorry about that so
um and some yeah some am istic uh uh
visualizations but maybe uh the best
thing about this session is whatever you
will see today you will get yeah you
will be able to use whatever I am
showing like after this session I'm like
quite sure um that's going to be at
least some of the pieces will be
interesting all right that is one more
thing Apple would say I would say one
more promise um and the promise is no
AI I basically just threw it out
uh so uh let's dive into it so what is
telemetry for business
Central um well in a nutshell it's an
event Vier yeah do you know Event
Viewer that's half of the people
Everyone Knows Event Viewer obviously
let's call it event fer on steroids it's
a lot more um it's something we can very
efficiently gather data from it it it
catches all the usages well all lots of
the usages of uh whatever and whoever is
using uh business Central and you
recapture that for only one reason to
gain insights insights in a very
different range of things we need to get
insights of yeah and officially
Microsoft will show this just to
be let's say interesting I don't do that
so uh do you know what this
is okay let me explain why you are
here um this is business Central um and
business Central obviously is being used
by people not just people we also use it
with let's say with background processes
job cues we also use it with web
services external connections we use it
with Excel maybe and and power automate
and what not so there is a lot of usages
that we have uh that has to do anything
with business Central these usages we
are going to capture let's say capture
in something that we call application
insights that's happen to be on
Azure that's not a coincident obviously
so cool now we have a service that is
capturing all that now just imagine we
can gain insights on whatever we have C
captured
that's going to be the next question how
do we get how do we gain insights on uh
on all of this data yeah well um I will
show you a few things powerbi kql that's
absolutely not the only thing that you
can use to gain insights whatever it is
basically just a database whatever you
can use to get uh uh insights on that
database uh what works for you I I will
show what I use
uh up until 3 weeks ago it only said kql
powerbi and three since three weeks it
also says
ad and I will go a little bit further
into that actually a lot further into
that that's going to be one of the main
things that we will be showing thank you
D um so uh and obviously at some points
when we get insites and we are able to
get to the interesting data that let's
say uh that
we would like to get notified from like
if if a job queue crashes or errors out
or does something maybe I want to get an
alert at that point so maybe that also
should be interesting okay or possible
so let's get started started is actually
quite easy uh you just create that
servers that application Insight um
service endpoint let's call it and then
you were going to set it up um you set
it up on multiple levels there was
actually two levels of telemetry that we
can set up in business Central either we
set it up on the service yeah and that's
typically the service level Telemetry
things that can might happen uh external
connections that are calling uh business
Central or Rec call out or something
code that's being executed slow running
queries Deadlocks that happens and these
kind of things and we have up related to
dmetry so just are you isvs do are there
isvs in the
room yeah you're let's hope you have
multiple customers your and maybe even
customers you do not manage yourself
just manage by other partners you still
want to capture how your product is
being used yeah that's uplevel Telemetry
you can set up in the app Jon an
endpoint and that's kind of like um the
up level telemetry so yeah quite easy
I'm not going to show you that um but
question I always get like yeah but we
are VAR we are a VAR are you a VAR as
well not too many so you don't really
manage
customers W do we manage customers yeah
of course we have a lot of customers
like uh in our case it's close to 100
customers that we have on business
Central how do you manage that are we
going to set up an a Telemetry endpoint
per customer
is that doable can we manage that can we
set that up um well what I would suggest
again I'm I'm just sharing what what we
do how we are using uh Telemetry and
actually for our customers for actually
the entire company we only have these
end points just a few yeah and sometimes
you get the questions okay I will just
uh explain them first so you see the ai
ai is not AI it's applic
insights it's it's if we not in the
guessing game here in the facts game uh
in any case uh AI customer NSD that's
the one where all customers are being
sending their service level
T2 yeah the nice thing is we Gathering
we're Gathering all of that in one
endpoint so we are able to get pretty
easy Statistics over multiple customers
we can compare customers what is the
slowest
page in on average for all customers or
maybe for One customer compared to the
rest of the customers or two customers
or stuff like that for our
product and that is these are
interesting uh statistics if you would
set up an endpoint per customer that
would be quite difficult to do yeah and
then you get sometimes the question like
yeah but me I'm a customer I demand my
own endpoint I want to see Telemetry of
app that I don't understand so send it
to me well you can for now set up one
endpoint it's either to the customers up
insights let's say or to
yours I'm quite strict on that like if
you want me to support you I get the
Telemetry it's as simple as that
customers are not going to let's
say reason or interpret an application
they are not comfortable it to
understand in the back end we understand
business Central as a consultant as a
developer we are able to interpret that
data so I'm quite strict in that okay if
you want your data do your own
implementation kind of thing okay and
then we have others we have the distory
upset that's our internal product so
that's the up level Telemetry whatever
we set up on uh
on for the product now that product has
apps so all of these 50 apps go to one
end point yeah the idea there is again
whatever happens with this three when
did we upload to uh app stores whatever
validation is happening or went wrong
that's the end point where we will check
upsource validation issues for instance
same for project bills it's another uh
product and then you see the distri apps
NST that is again something that we
would be are able to set up it's
basically our test system our test
system for the product I didn't not want
to send that Telemetry to uh let's say
customers or even uh the app level
Telemetry because that really not up
level Telemetry is live data test system
Telemetry is test data I didn't want to
mingle that data
either second to last you see the pte
apps even even for custom development we
are able to set up up level
Telemetry and I would strongly suggest
to do so because again you can get the
up typical app Telemetry For Your
pte Right any custom development
whatever let's say the customer
complains today all of a sudden that
things go wrong well you can simply
check like did we publishing up our
custom development at that customer
today right these are typical things you
can get from that uh Telemetry the last
one that you see the test is just a test
I mean it's for our internal uh
development just let's say that if we
set up our own custom signals that we
want to test that we just set up that
endpoint and then we send
there
okay why does Telemetry matter for uh
developers well simply said it's just it
has a lot of metrics you see a lot
what's going on in in your database and
obviously that's going to be the topic
of the rest of the session so it's kind
of like yeah all in one here we will see
the slow running queries we will see uh
yeah API calls and all that we can see C
custom Telemetry as well we can use
custom Telemetry I will show you a few
ideas today on what what I think would
be really interesting we can see usage
information what is I have some stories
about that that I can
share um and yeah and you can get
alerted about that as well so all of
this is gathered in that API or that AI
endpoint that application insights
endpoint what I also sometimes call a
Hast stack like okay now we have
here some
data and there are two things with that
Hast stack there are either needles in
there or not and if there are needles in
there we would probably want to find
them as well yeah so where are the
needles that's kind of like it and the
rest of the session is going to be about
identifying this exact thing yeah that
finding that needle
so to in order to do that we obviously
need
to understand what we have or what we
can expect from uh all of that data and
I try to categorize that a little bit um
well not me I did use some kind of
co-pilot for this uh chat gipt just sent
the entire web page on signals there
categorize please and then this is what
it makes sense so uh in terms of user
interaction and experience we can see
all
errors everything all
errors we capture in Telemetry so you
can really analyze interesting stuff
about your product what is the most
common error that happens with that
extension caused by this extension and
maybe we
can act on that we can create an
actionable error to solve that error or
maybe give a little bit more information
in that error with the error info and so
on and so on we can improve the product
we can maybe put some work in the
onboarding stuff do you do you know what
I mean with
onboarding yeah me neither
actually uh um next we have this
performance monitoring and
troubleshooting stuff obviously uh it's
a big part especially for developers we
need to know what is slow and I think
still we have that feeling business
Central is
slow do you have that
feeling yeah unfortunately too many
claps um we have that feeling business
ENT was slow and I I promise you most of
the times it's you and me it's us us our
coach
that makes it slow it's it's it's it's
the way it is it's the apps that we
install from myvs in that case it's
them of course uh it's our own apps and
it's our own custom development usually
Microsoft is pretty good
in writing their app as fast as all
possible pretty good not always good but
pretty good and usually it's us that
slow down or causes that extra slowness
in the system in any case we also have
the security and authorization so uh you
must anyone who are already set up
Telemetry must have seen these yeah a
web service was successfully
authenticated and you get a crap load of
those for any kind of authorization you
get that signal and there are more
mostly in the way and all that and you
would like to avoid them for instance
and you get these application life cycle
and deployment uh signals any kind of
upu install you see in Telemetry yeah
the version of the app you see when it
was installed the problem like an
upgrade problem that you would have you
see uh it all in Telemetry and then
integration communication yeah the some
job cues email the the integration part
that you have with sales there are there
is a lot you can get and all of that is
being stored in application insights so
obviously now next challenge
is that we need to gain insights yeah um
and that is yeah where we turn to the
the tools that I uh that I mentioned
like uh powerbi and you will see I'm
very uncomfortable with
powerbi uh the people that went in my or
was were in my workshop the past couple
of days they noticed that very
dearly um Power yeah you'll see but
anyway we get it out of the box we get
it for free from Microsoft well free is
between quotes um and we are able to use
that to gain that easy one goto insights
like whatever if I'm not comfortable
with Telemetry maybe I can already see
something in powerbi so let's let's look
at that for a minute so author of this
app that I will show is Microsoft and it
is free I should actually quote unquote
free it is an app on powerbi but you
kind of like need a powerbi license to
be able to install an app in
powerbi so
yeah you need you need a license for
that but in any case let me just show
you um
quickly so um it's actually quite easy
to install let me just um go if you in
powerbi again I have a pro license for
that to be able to do that there is a
trial you can use as well for 30 days
you are really free and using that for
free and and you if you try to find
business Central you get all of this uh
apps from I fees and all that the one
you really want is the one with 24 five
stars I mean they call it Microsoft 365
boozy and then you have here Microsoft
boozy and and here Microsoft 365 boozy
boozy booy I mean come on just call it
usage or something and then we can
actually search for it in any case uh
when you open this app you see the real
and the big
name thank you for being slow I can
drink so it's usage
analytics you simply uh get it install
it done yeah it's as easy as that so
maybe just let's do it because it's that
easy
yeah in any case I already prid this so
I'm going to open
an one that I already installed and this
is pretty much what you get a pre-made
report on the left some tabs that you
probably recognize like how is my
business Central being used what are the
errors there was the message that I now
I lost anyway um a performance tab like
how can I look in what is the
performance I was how was my app
performing uh or my business Central
performance and some Administration
stuff to look into um different things
job queue index changes company changes
and so
on
um you will see again that I'm very
uncomfortable with this it it it it
comes a little bit down ah this I wanted
to show you so the The Next Step you
would take is connect your data
obviously you need need to connect out
of the box you will just get demo data
yeah so you connect this to your data
and what you typically do you just from
your application insights uh key you get
your uh up uh up API access you copy the
application ID you paste it here and
you're able to uh basically connect it
to your uh application insights if you
validate with with your credentials
obviously you need access to that to
that
data uh there was a lot more to say
about this report like uh one thing that
I didn't know but now I know uh that you
can do some kind of aad tenant mapping
because I mean out of the box Telemetry
uh will show only aad tenant IDs good to
identify our customer it's not that easy
to work with if you would like to create
a mapping you could say like this ID is
that customer and you can get like
domain names for your uh customer you
can also exclude or yeah well include
environments based on this ID so to come
back to that can the customer access the
um their data this would be an option
that you set up the powerbi report and
only include that a ad tenant ID
honestly I wouldn't do that because it's
just a setting it's just a mapping kind
of thing if they disable that mapping
they get all the data from other
customers as well and I wouldn't be
doing that honestly in any case this is
what you get and obviously it it's a lot
you can already go try deep into
whatever is going on on the system error
messages the most common error messages
uh what I used this a lot for is I don't
really have the right report open but
that doesn't really matter uh the long
running SQL queries and then have a look
the day byday look maybe in the end like
how am I improving uh my long running
SQL queres in this case I'm definitely
not improving because it's basically I
getting more and more um long running
SQL queries yeah so it's definitely
interesting less interesting is as a
developer as an someone who is analyzing
this how do I go further and you might
say well there was some topic on that
there analyze further in kql uh well
this kql is not really in my opinion
useful it's not the kql this report is
based on it's just a kql that is have
that has similar data about the tab that
you're actually experien uh see at the
moment so to go a little bit further in
details is not that easy based on this
powerbi report that's my experience
again this session is all about my
experience
me um that's the powerbi
part so from the mo moment you have a
burning question you might be able to
just have one goto report and just look
into
that I would suggest to look into kql
yeah and there was a lot to say about
kql this is by the way the boring
part um where yeah well kql is basically
a query language uh custo query language
very performant I'm actually always
amazed when I start using that how first
of all easy it is to use how easy it is
to read you just need to get used to
that is anyone comfortable with
Powershell I always um compare this with
a with a marriage Powershell
sequel I don't know if that makes sense
honestly uh but in poers Shell you get
the pipe symbol you use the pipe symbol
in power shell is actually quite quite
powerful and the pipe symbol in power
shell says like whatever happens in that
previous statement that output is
streamed into the next statement and
that's what I will start with in my next
statement it's pretty the same in kql
you have that pipes pipe symbol and
whatever I had before like
query with after the pipe I will do
something else with that I will extend
it with more data I can I can uh filter
it with the wear CLA and I can do like a
lot more with that so that's pretty much
how kql is being built this
is uh completely
useless but an allinclusive uh example
let's say so uh yeah so what does this
do I I made a slide instead of me just
typing I I decided to to create a slide
to give you some overview on what we can
do with uh with kql so first thing that
you see here I can create let's say
variables and fill that variable with
the output of a certain
query basically let's build a view right
uh and then with that view I can query
later on in the same query
yeah I can use data from even adjacent
file this is an example where I download
from drawbox adjacent file read that as
a table
yeah I can
Union and Union two tables together the
traces table and the page view table by
the way these are two tables that
business Central is filling with Trace
data with
signals yeah and you can just Union
whatever you like but be smart with that
I can extend within the query I can
build new Fields
containing values of other fields maybe
concatenating maybe concatenating if
something is true so you got like uh if
executing execution time is that then
take that field if uh if the other one
is not empty then take that field if
that one is not empty take that field by
the way if you ever try to look into
anything durations uh in business
Central naming
conventions is far far far away let's
say sometimes a field is called duration
sometimes a field is called execution
time then a field is called uh what is
it server execution time and then we
have something like total time so why
not just
duration every single time well no but
you can fix that because you can create
yet another field I did elapsed time and
I just take in the order I like to take
whatever field I would like and that is
what this snippet is
yeah you can
join like if you have like built two
tables you can join both tables so in
this case I had my signal definitions
which was adjacent file I will show that
in a minute and I've got my um other
table being the traces Union with uh the
page views and I can join them together
like if I have an event view an event ID
in one I can take the message from my
Json file and put that in the same query
yeah it's very much equal that you're
doing
here you can filter obviously luckily by
the way uh best practice is to filter as
soon as possible I'm doing a very bad
job here I'm filtering very late yeah
and you can summarize very important you
will use this a lot that's what
analytics is all about you're trying to
analyze and total and average and and
whatnot uh so you're going to summarize
in this case I'm counting the records by
time
stamp bin time stamp one day which
automatically creates a time stamp which
can be like a day time
12 12:00 12 53:00 and so many seconds so
the bin says okay uh round it down to
whatever I say in this case a day so
it's very easy to be able to summarize
per day
but you could do that summarize per 50
minutes or summarize per 1 hour and that
gives you a lot of possibilities and
trying to analyze but just imagine if I
count let's say the amount of signals
that I have for every hour I can see the
busy hours Yeah the more signals the
more busy my business Central is and
it's that easy actually to get actually
around um telemetry
so all clear we are kql experts
now okay uh we will we will see a lot
more as I promised a disgusting amount
of
kql but I will only point to the what I
think is the interesting Parts uh of the
part I mean I'm not going to explain
these kinds of queries it doesn't make
sense how I will do that is the ad part
remember that was kql Slade ad stands
for Azure data Explorer
um I'm not good in
powerbi I'm a little bit better in this
and you'll see why uh because this is in
my opinion uh this has blown my socks
off as as software being as user
friendly as it can be I I rarely see
software that is as user friendly as the
aure data Explorer has been for me the
last couple of
weeks um I got to know it thank you d uh
when I was in a call with him three
weeks ago and I was like okay shift
delete all demos but I prepared for take
days I will rebuild everything in uh
Azure data Explorer so thank you for
that extra work as well you so what is
it it's actually a a fully managed
platform that you can use for free I
triple checked that I wasn't sure
yesterday because you made me wonder uh
but I mean I I'm not paying anything so
you can use it for free for um for
application insights you basically get
online data uh online queries it does
that in an asynchronous way yeah and
that's that's pretty much how you can
manage all your queries let me just show
you one thing three weeks
ago I was doing this I had not this oh
also this but anyway let me first go to
my where's oh here so I had this thing
here uh waldo. BC Telemetry it's a it's
um a repository on GitHub and this was
really just my go-to set of queries
whenever I had a problem copy paste copy
paste and I was basically copy pasting
all over the place just I just an
example here if I had a performance I
needed to look into let's say Deadlocks
I had my set of queries I I just took
like okay what is my what is the
customer
most
um or or the most Deadlocks per customer
kind of thing select everything and I
would go to uh
here my actual application insights go
to logs
let me just do
it paste run that's kind of like what I
kept on doing and I kept improving those
queries pushing that to the repository
so that I kind of like um got a decent
decent overview yeah well I'm I'm not
having Deadlocks on this demo
environment but
anyway I kept on doing that that that
was my go-to too that that's what I was
I was doing
Telemetry since we have now Azure data
Explorer you need to see this as a
dashboard where all of these
queries are just
there and pre-run all I need to open is
the dashboard very similar to the
powerbi report you might say well why
don't you just use the power by report
that's free by Microsoft also you'll
see okay so extremely user friendly all
that uh and it actually supporting the
tools that you really want to support so
let's take a small look into this uh
Azure data Explorer and you can see that
I'm actually quite excited to do so yeah
uh where is
it so this is basically yeah I will
start here um asure data Explorer uh is
basically just a let's say a dashboard
not really dashboard it's just an
endpoint that I can use to to do uh
querying querying of a certain uh in my
case application inside's database maybe
zoom in a little bit um and on the left
you see already the same
seven uh endpoints that I was talking
about these are all the endpoints uh
that I that I'm using in my company as I
promised live data um I can simply set
that up by an endpoint ad application
inser IO and point to my subscription
where I host that uh application
insights when I have done that I can
connect with a certain user ID and then
I get access yeah my user has access to
my Telemetry that's a good start and now
I have a query window you might say yeah
well this is quite quite the same as
what we have in the logs true what I
like about this most is it keeps my uh
my queries open so when I close this tab
and tomorrow I open it again the same
queries are there the same Tabs are
there it's already a very big
difference yeah um and I can simply
start to like do other things like uh
yeah I'm not like I'm not going to do
that um but uh it pretty much comes uh
comes down to that I from here I
can let's say you see intell is there
the shortcuts are there shift enter
executes uh a certain query control
enter sets uh a new line with the pipe
symbol I mean it's like you have a
decent coding experience and again it
saves your query and your your access I
like that a lot
um but what is what else is quite
interesting is the fact that you can uh
yeah the resolution is a little bit off
you can pin this to dashboard and you
might say okay I have dashboards on
application insides yeah you don't have
these dashboards
so you can create your own dashboards
let me go to that I created one for
business Central uh for PC T days and
yeah you see all of these queries that I
might have in my repository they are
simply there and they're already
executed so I mean no copy pasting they
are just
there oh my God I
mean and even and remember the this is
still quite the same than powerbi sure
but can you do this with powerbi so I
can for every single thing that I have
here and I will show you more things for
every single query that I have here I
can actually view the actual
query and not just that I can simply say
okay I will take this query and I will
create a new query tab
and this is what I think is really
analyze further yeah I take the actual
query I can and I can out do whatever I
I would like to do maybe I I have no
idea where the details come from here
like it's events parameters whatever
that is uh I will go to my query window
I copi that query and maybe I just
remove the
summarization I can put that in comment
execute the query again and I get the
actual details without the summarization
so how does it summarize why do I get
that
um and so
on yeah and it's not always slow by the
way summing is a good thing to do uh to
make it not too
slow all right
um more you this this actually it says
parameters you can work with parameters
and you see those parameters actually on
top of here I can actually create
ways that I like for myself I like to
filter my data like what I do a lot is
filter the data on tenant description
something that I came up with which is
that domain that you can also set up
with that tenant mapping yeah but
basically just now for uh for this um so
what you can do is if I go to edit my
dashboard you can for instance go into
edit mode and this is basically how the
query now looks like and you see here
that I use an underscore message filter
well that is actually one of the
parameters I can set up my own
parameters whatever I like and I've set
these up company filter time range um
that tenant description thing now this
message filter is actually just a string
uh and that's it so I can type whatever
I want in message filter and I can use
that in my query as well so I basically
extending the ability to use my
query yeah and obviously these are
parameters that can I can reuse in my
other queries so that makes it actually
quite interesting one parameter you get
out of the box is the time range very
interesting and very necessary one you
always want to filter on a time you
don't want to see usually don't see all
the data from 90 days or what not you
have in your database that's always a
slow query so you always want to uh
rrange the time so that's one query you
you can always uh filter again in the
beginning of of the trace
yeah that's parameters you could also
have base
queries quite interesting uh I didn't
know I only knew like I when I finished
like 75% of my queries and I like H I'm
always doing the same crap always the
same things always all of these uh
filters there and and always extending
the same fields that I would't like to
see in my and work with in my queries so
I was like what is this base query all
about now this base query is actually
let's let's call it a view that you can
set up that you can constantly call in
your other
queries yeah so I've set up a
view a view that
by default calls external data Json
files so signal definitions I got here
ajacent
file with signals yeah thank you D once
again he built ajacent file so this is
basically ajacent file that yeah you see
it contains all the uh the signal IDs
with a decent um with a decent area
uh and a decent description yeah um I
also built one for my tenant ID remember
the tenant mapping so for any tenant ID
I now I now have a decent description
once again this is that tenant
description by the way these are
fake this is actually a way how I now
offis skate my data all uh all tenant
IDs are fake I cut two move two digits
let's say and all names are fake but I
was I created a query uh a base query
for that in that base query I basically
always take all traces and All paas
Views I by default will filter on the
parameters that I already have yeah so
also on that message filter I extend so
I create new Fields what I think makes
most sense event ID I always extend yeah
but the same for extension name the same
for all of these durations I was able to
find execution time which you sometimes
have server execution time total time
durations and whatnot so you find all of
these and later on I will use all of
these in and build yet another field
with elapse time so I basically have one
field can I can work with for timings in
a base query so now all of a sudden I
have that field at my disposal for
whatever I want to do and I don't have
to think about yeah now in this case
it's lapse time now it's duration and
now it's execution time and what not
yeah and this is the obfuscate part
where I basically just uh take away from
the 36 character one character so
yeah I had to do that and I officiate my
extension names a little bit not really
important
um and yeah all in the end I will join
everything together in one decent
table long uh story short you will only
need to do this once and for the rest of
your queries you can simply point to
this as being a view so instead of
traces what you would do
is uh let me
see this one for instance base customers
so you in this case I will do the entire
query that is a base query and just on
top of that a little bit more especially
for this yeah isn't this blowing your
socks
off
yes cool uh I mean this saves so much
time in building queries and analyzing
queries and all that the outcome of this
by the way so you have seen if I uh if I
do this it the query is very readable
it's it's very like okay I do all that
crap that W just explain and on top of
that I will summarize count and what not
whatever this is yeah if you really look
at the output of this query this is
actually just more complicated if you
really look at the query you'll see that
it builds that entire base query
including the filters I set on top yeah
and then all in the end it will just
call that yeah it takes a few seconds to
understand this big query this but is
actually all just a concatenation of the
base query with whatever you did for
especially this this one
yeah I include included the sanity check
as well like I just wanted to know like
I'm building this big query and I
actually did I'm filtering and all that
and I didn't really know anymore like do
I have as many fields as I expected well
yes so that's why the sanity check is
here which is a very simple query I'm
doing the base customers I'm doing the
trace Union uh page views and I'm
compare both so I still know that I get
as many um output as I would expect of
okay so you can do a lot now uh so now
we have like a nice tool that we can
look into Telemetry with
cool so let's dive a littleit bit into
what we can use this for first of all
performance and I will do a few things I
will look a little bit into the slow
stuff I will look into the web service
you know it web service no okay um
performance okay uh the
Deadlocks um uh is absolutely
interesting and if you do not know what
Deadlocks are let me quickly explain
Deadlocks is very simple you have two
processes always one process is locking
resources in a certain order another
process locks pretty much the same
resources in a different order and at
some point the two processes are running
at the same time and at some point they
will lock each other right and you kind
of like have two resources waiting on
each other what SQL Server will do just
throw an error for one and let the other
one pass what you have is one error and
the other one you don't have any info
from so the idea from Deadlocks and how
to get to analyze Deadlocks is to
analyze to get to those two processes
that is that is your
um challenge let's say so we're going to
have a look at that we have this lock
time outs yeah that we can do uh with uh
or can look into with Telemetry and
definitely also we can do some code
analysis we can look into let's say some
SQL
to look
into some things that we might want to
improve in our code so let's have a look
again obviously with um the Azure data
Explorer and I have some slow stuff here
and the idea for the slow stuff thing
and it's slow as you can see
um oh come
on that I would look into this slow
anything I'm not really looking for a
very specific thing that's slow I'm just
looking for a duration that takes the
longest yeah so remember that aapse time
field that's what I will uh use here so
the slowest anything per customer and
you can already guess typical things is
like the the AL again this is live data
so I have no idea what will show up uh
but yeah this is a typical thing the AL
method uh I usually never look at slow
Al methods anymore because that's just
slow users users that don't close a page
a run model is a code line from a
certain method that method will take a
long time when you do not close that
page so yeah you get a lot of those like
these print dialogues and and and all of
that um but yeah what I see here is like
uh this web service calls so there like
like slow the last hour I had a few slow
web service calls
sure I would be able to look into that
again I can uh look into that tenant
description by the way what you might
notice now I get actually a drop- down
list from existing tenant uh description
this is also something you can do with
that parameter thing the parameter is
not just a text I can also make the
parameter a query yeah a query which is
in this case a simple summarization of
all temp uh of all existing temp
descriptions for this time so you really
can take even in the parameters your
filters into
account man come
on Amazing okay gu so I will not save
this
please um so yeah I I would then like
say like you maybe in this customer that
is not really the best one so
Euro I will filter on that one and you
kind of like our Focus all of your next
steps on that one
customer uh what else is interesting
very interesting very important what you
see here Source process and slow object
two Fields what if I can identify from
Telemetry what is the process that's
causing a problem and what is the object
that's being slow two different things
by the way process could
be item list opening an item list or
could be posting an order and the slow
object could be one query down the line
back in that process so that's
actually very interesting to look into
um well in my opinion um and how do we
do that so something I stole from
Microsoft what you can do is look into
the stack Trace in many of these events
you get a stack trace this stack Trace
is from bottom up
the the process so you could say the
bottom
line wait minute yeah the bottom line is
the start of your process yeah this this
is where you will see oh code unit do
run or whatever uh the code unit that is
starting the process starting that
method yeah the top is where everything
uh is slow so the slow object is at top
of the Cal stack so it's just a matter
of analyzing the scal stack so you see
that here and the call St is just a big
text so we split that text uh on the new
line so now it becomes an array yeah we
get the length of the array yeah so we
can use that further on in the query uh
and then we start to analyze a bunch of
rexs going on uh for top of the call
stack I need to get the object name the
object type the object ID the line
number and all that again I stole this
by the I didn't write this um and for
the same for the bottom of the C stack
and all in the end when you analyzed
everything you can set up like something
a Source process which is in
concatenation of what I do uh whatever
is bottom of the call stack the object
type some brackets and whatnot an an
predefined string how I want to identify
that exact that EXA Moment In Time
Source process is the bottom and the
slow object is a top yeah so down the
line my query now I have two Fields
Source process and slow object that I
can use to start to display yeah and
that is exactly what I do here so these
are the last slow SQL calls and I can
look into what Source process uh
apparently call available um things
default business Central
that is a
surprise and then the slow object and
you can see like page openings and and
so on but this is obviously now
interesting because now you can analyze
like what is my slowest
object or what is
my
biggest problem
being the uh the process that causes
most problems yeah because you have
these two fields in the query and can
simply summarize on
it other things that slow is uh
obviously Pages uh remember the page
views you can look at uh well I I
sometimes do a do do a session I ask
what is the slowest page typically I I
think typically it's the item list I I
see item list and sales order popping up
every single time on top of the list and
it's pretty normal in our case because
we did extend the item this quite a lot
uh but yeah we tend to use um the sorry
the it item list as being a report and
just put all fields that we think is
interesting on the item list which is
not a good idea by the
way um some uh performance in
information on API calls again I will
take this customer but yeah uh for API
calls that's typically when we go into
um a typical uh event ID RT 00008 is
interesting because that's the that's
the event that shows the incoming uh API
calls and one thing I need to say about
this is that you do have information on
the query filter so you can have an
overview on how your third party
partners are using your
apis and I can promise you they're not
always using that in the best
way yeah you cannot get to the body
unfortunately that is like gdpr stuff
but you can get to the query filter and
I've had lots of issues that basically
they are using the wrong fields to
filter on and you can simply improve
that by indicating like look can you now
use that other field to filter on or use
a last modified day time or create an
index for what I do a lot yeah Deadlocks
uh in the Deadlocks part again this is a
very typical um I'm going to need a few
more hours here I think
um a very typical thing where we want to
look into that Source process remember
we are always talking about two
processes we need to identify those
processes yeah so now Deadlocks we only
see one problem we need the second you
won't so the only thing that we can do
is capture them as many as we can for a
certain customer and then sometimes SQL
will say now you're dead and now the
other and the other times SQL will say
now you're dead so you need that data
you need to wait to have enough data to
make that uh analysis uh what is I will
take two days because I don't get too
much information I will select all
customers
um uh what very what is very important
here on Deadlocks that's also why I put
the other field here if you have an
overview you see the most Dev uh the
most Deadlocks I get in bumsters medical
lips smart they are version 21
22 yes you can get to the server version
version that your customers are using in
you can get a a look at what version is
my customer working in this is th State
loocking version 23 removed 90% of our
Deadlocks if your ver if your customers
are still using version under 23 please
upgrade them it's a big change yeah
proof is right
here lock time out is pretty no sorry I
need to scroll down a little bit so I
can show you some overviews this is
actually quite a nice one so you can
actually have some kind of overview on
what that Source what is my biggest
problem what what Source process causes
the most of my Deadlocks and what slow
object being the Locking object causes
the most of my Deadlocks you can have an
easy overview by the way again view
query and you start to analyze from
there it's
amazing same for lock timeout pretty
much the same there where you you uh can
look into the source project what is
causing that lock the most of the times
what is locking uh at at the end of the
process and how can I uh act on that
yeah um last but not least the the
performance
analysis you can look into the SQL data
so you could reason like whatever
statement I get let's have a look what
kind of Al statement could be causing
that SQL statement
and there are a few like partial records
you can figure out how many commas you
have in a slate statement and that kind
of like says how many columns you have
in a slate statement and that might
indicate that you're not using uh select
loaded or set loaded Fields you're not
using uh partial records at that point
so it's very simple query that counts
that and just displays that a certain
way that's not really that important uh
uh but you get an
overview where sorry the number of
columns is most here so we have an
extension it's my extension uh that we
simply did not set load fields at this
point with a bit of luck we have
actionable things and yes I made sure of
that because what is actionable
something that I can change so if I have
a stack Trace there is code behind the
scenes if there is no stack Trace
then it might be just a page that I'm
opening or or something else yeah but if
there is a stack Trace now all of a
sudden there's code and I can change
code so I see I make sure that I only
get the ones that are actionable so I
know that this one is something that I
can change yeah and we have some IVs
that I might want to uh look
into but most of them is is
ours
crap okay
um we can do we can look at other things
like locking not just the Locking I just
talked about but locking is empty are we
still having queries with is empty that
is locking it's very simple if I get a
select top one n and an update lock in
the SQL statement I have a locking is
empty you do not want locking is empties
so you would like to look into
that and do some re isolation yeah so
yeah it's helping developers to identify
uh what can be improved in uh in the
product same for if you have a
locking calcum you might want to avoid
that yeah I don't yes finally some good
news um same for for counts and you can
simple get to the counts wherever we
count select count as account and see
where it's logging
yeah
so I've got some slides here basically
an overview of what oh sorry what we
just saw um the slow stuff again I'm
actually just interested in anything
slow so that's is the concatenation of
whatever field by by Microsoft is called
I just put it in one field elaps time
and that's the one I will do some
um some queries on and then the web
service performance uh yeah there are
some interesting things obviously endp
Point as well uh you can figure out like
what is the application that it's using
it by the end point sometimes I get yeah
but I don't know the source who is the
source that's calling my yeah you don't
know you cannot see the source but in my
opinion you should always create a
custom API specifically for any source
that is that wants to call your
API never use API V2 doesn't
exist Microsoft's
API it's nice to copy paste from but you
lose your grip on how people are using
your system and it has too many openings
as well in any case end point is
interesting uh and obviously a lot more
query filter I find particularly
interesting especially for performance
problems then you get maybe something
like this this is what I noticed
yesterday evening like whoops something
happened so the amount of API calls that
we had at a certain point at at at
2:00 um
yeah by the way did I mention that ad is
amazing this was a
shortcut to an actual tile in my
dashboard including the filters I put on
that
dashboard
what come on so you'll see here the same
uh the same um query in like a few
hours yeah there it is obviously now
it's a little a little bit back in time
yeah this the other screenshot was uh
2:00 and you can start to analyze look
at this what do you
see jet reports users are using your the
system you might be paying for the
Telemetry of that system so users create
a jet reports report let's say creating
like 30 million signals a day and you
are paying for that so you might want to
take a look at the amount of signals
your users all of a sudden cost just
because they created the report in this
case this is like something I need to
manage
yeah all
right uh Deadlocks we talked about this
um again information about the uh
version of the user or the version of
the customer is actually quite important
and this is not by coincident that
anything below version 23 is having more
Deadlocks than from version 23 yeah make
sure that Deadlocks on Prem is
configured to capture on Prem it's not
on by default on on SAS it is so you
need to do some extra power shelling to
set it up on Prem yeah on the lock
timeouts again different kinds of things
what I didn't show you you do have
insights on the actual lock what was
locking snapshot what was locking what
resources and who was locking at that
point you do have information on that in
the Telemetry as well and on Prem again
you need to enable that on Prem you
don't get that data out of the box yeah
enable the lock time and monitoring on
Prem just do it don't think about it do
it you'll need it especially if it's not
version 23 you need it more and again
for code analysis yeah there are uh
possibilities to look into the SQL I
actually only am looking into SQL to see
what a might be executing and again
therefore the Locking part in many cases
read isolation is going to be your
solution it's very now easy to track the
code and the used code at your customers
thanks to Telemetry and you will be able
to change your pte and your
um um isv app as well
okay custom Telemetry we are able to
create our own telemetry
do you do
that do you create your own Telemetry
that's actually quite a lot that's good
you create your own signals makes all
the sense in the world we can uh create
we can simply use session. log message
come up with our own uh event IDE set up
uh everything we need to know including
custom Dimensions we can add whatever we
like and we can call yet another field
duration if you would like to do
that um we have this default Dimensions
that comes out of the box so don't
create these they are there already yeah
uh and remember or not remember just
know that there is also something an an
engine already there that we can use
being the Telemetry
loger uh not saying you should use it
just know that it exists and you have
some possibilities uh or some extra
possibilities there the idea of the
Telemetry logger is that you are able to
set up your own let's say engine that
you basically add more Telemetry
specifically for your product for
instance it might look looks something
like this that you implement the
Telemetry logger uh
interface um it it works a little bit
complicated I'm not going to go too deep
into that it comes down to the fact that
you you implement your own log message
yeah uh so you see here on the first uh
line in comment you see comment that
like an add my own custom Dimensions
just an example on license status like
what if I always want to include license
status information or what not
information from my product by default
yeah and then call thec system.log
message it's just the central end point
to add more custom
Dimensions
um you need you can only do that one for
one publisher so you are a company
usually you have one publisher in your
app Json and for multiple apps is going
to be the same publisher that's one
company uh well you just need to make
sure that you can only have one coach in
it doing this that is how the system is
being set up done that you are able to
one when you
call the uh the Telemetry dolog message
which is what you should use Microsoft
will figure out oh there is a registered
publisher that is the implemented
interface I will run that lock message
and then your your uh code will be added
it's a little bit complicated honestly
it took me a while to figure that out um
but yeah know that it exists what can we
do with that in practice
tests now just imagine Telemetry on
tests we are all already doing automated
tests are you doing
that yeah we are all doing tests let's
just assume we're all doing tests
um now let's add into the mix durations
number of SQL time uh SQL statements and
you kind of like get an overview on how
tests are acting out in the passing of
time so I did
that and this is just an example this is
not the actual code but it's just
example code I copy paste it um just
imagine yeah
not going to spend too much time on that
but you have these events in the test
framework yeah on the runner there is an
event on run test on after run test and
you can actually figure out I'm actually
compiling for the different levels so
per Suite per code unit and per method a
start stop so I can measure a method I
can measure a code unit and I can
measure a suite in and the amount of SQL
statements that were actually executed
and the duration that it took just added
that on the framework yeah and all in
the end I will send the
Telemetry with the custom Dimensions
that I like to have so now I invented a
new one duration in
milliseconds um and this actually sorry
this actually results in
of an overview all my test runs the last
24 hours Let's Take 7 Days yeah and you
kind of like see can see some kind of
regression testing now what I'm doing
here we have 8,500 tests I didn't want
to have 8,500 lines on this uh graph so
what I'm this is actually a pretty
complicated query what I'm doing is I
will take the worst the much the most
difference the most top 10 most
differences right but the thing is um
what you here what you want here is in
regression testing you always want a
stable line it needs to be stable it
needs to be always the same amount of
SQL statements and from the moment there
is some kind of difference you would
like to know that so I'm cheating here a
little bit if I take this for the last
30 days you see that I did have a
problem at some point you see here for
instance that this
test yeah good luck fifo B ranking test.
given bin content with fif ranking
disabled when col fifo data then check
and so on that's the function name sorry
about this but it explains where it is
is that exact test all of a sudden on on
June 1st or May
30th took more SQL statements and that's
actually the the thing that I would like
to know yeah you can just enable that
install the app extra Telemetry and all
of a sudden you have regression testing
of the performance of the test you're
already executing every single
day how cool is that so three levels I
explained that and it will be soon I I
created actually an idea or or or I'm
trying to create a PLL request at
Microsoft to add this in in uh in the
product so that basically it will be
there out of the box do know if you want
to use this then you need to make sure
that when you run tests that you have
set up an application endpoint of in
application insights
endpoint for that container when you're
running or where you are running the
tests another idea application
performance pretty much the same let's
just say you are
uh you just foresee a framework with a
start stop and you are able to plug it
in anywhere right to measure performance
of anything so that is actually what I
did here very simple code unit with a
start measure and a stop measure yeah
which are now when you stop the measure
you're basically again going to emit a
signal where you just add duration not
in milliseconds because I really won't
like to find uh or like
to use
Microsoft design uh rules like always
find a new way to describe
duration um and any case and then you
can send that to uh Telemetry by the way
this is bad practice always find the
same
name and this is just an example here
where I put that in so on before post
sales do on after post sales do I'm
measuring and I'm sending that post
sales do measure now you get the ability
sorry now you get the ability
to show
that so this is an example let me reset
this for a
minute okay nice
example ah yeah my my fault I need to
put an extra filter measured function
because else I got too much so let's say
the sales
orders um and I can compare the um the
amount of times certain customers are
posting sales orders but obviously also
I I can compare the performance of
posting a sales order maybe in time over
multiple days per
customer cloud is not always as fast as
you would like it to be but sometimes
it's just cloud so now you can kind of
like have a look like posting sales
orders is slow at that customer is it
slow at other customers and you can have
that comparison as well and if it's slow
at all customers you you might realize
like hm yeah it's a cloudy
yeah so again the regression part or the
per date per tenant whatever you would
like to to make this happen the nice
thing is you measure that for all your
customers you capture that and that's
kind of like uh possible for any kind of
method that you are able to uh to do
that another idea daily Telemetry so I
don't know if you're aware but on SAS
you have this code unit always in job
que did you ever notice
that yeah now this job que doesn't do
much it actually just sends a signal no
it raises an event the onent daily
tality event and Microsoft has
subscribed to that event for two reasons
for uh monitoring sensitive Fields I
still have to figure out what that usage
is I have no idea um I can't figure out
how I can tap into that but in any case
for sensitive fields and then the
onboarding signals whatever that means
but you can tap into that as
well right so what if missing indexes
you know what that is right per uh
customer you can open that page
but I mean that's per customer maybe for
product wide for all customers I would
like to know what is the most missed
index for all
customers so why not emitting a daily
signal that just shows all missing
indexes yeah same for uh yeah sorry same
for
Orphans did you ever have ever have
media orphans
I think
more will have media orphans the thing
is do we know do we really know we are
creating media orphans actually without
us knowing doing so and what what is the
media orphan uh so the media table and
the media set table contains an ID that
points to a blow field with a picture
and this ID is actually being pointed to
or used in like say item picture or
customer picture or
whatnot there are situations that this
ID simply does not have any record
anymore in the database that it's linked
with so actually it's just sitting there
there's nothing showing ever showing
that picture anymore ever so it's just
eating up database space yeah the
typical thing is if you have a batch
import of pictures that might cause this
uh Stefan talked about validation field
this is one of the reason why you want
to do validations from the moment you
don't do validations either modified
delete validate this is what you will
get you get inconsistent data this is
inconsistent data yeah um
so yeah you can set now these days I
think from version 20 21 we have this
media. find orphans media set. find or
orphans which is actually just a simple
Al statement that gives you a
list of guids and these guids are
pointing to the actual Medias that do
not have any record in the database
anymore that points to that media yeah
you can find an overview for that so
let's have a look on this uh daily
Telemetry where I created just an
overview on on the missing indexes this
is this is just an example but the nice
thing is I can maybe ask this for the
last 30
days don't just start creating uh
indexes you shouldn't be doing that that
the reason why this exists is to start
creating the most missed
index yeah um an an an index that's only
missed for one day let's let's not just
create that but you kind of like can get
a picture on like in this case in the
customer Leisure entry this index would
be
interesting and I'm missing that and
obviously again same information you
have that per customer this is for all
customers and you can start to group and
look into what is uh what's interesting
to start creating in my product you can
also see which customer that is same for
media uh orphans and I think I can show
you that if I go back far enough look at
this so all of a sudden at some customer
I mean this is live data I'm not making
or faking this at some customer we we
all of a sudden had like what what is it
close to 6 or
7,000 or
orphans so we still need to fix that we
also see that
um but yeah I don't know what happened
here um but at this customer we really
need to look into what happened and what
caused it this can be different things
this custom already removed them you see
that so we already removed that and we
have kind of like that
overview so yeah definitely interesting
stuff uh to look into if you ask me
if you create your own custom these are
all custom uh API uh Telemetry signals
if you create your own there are some
best practices treat your um a your
Telemetry your custom Telemetry as an
API you shouldn't be breaking them don't
change the ID don't change the field
names that you have in your custom
Dimension and these kind of things
document them I have an example here we
documented our internal um yeah our
internal Telemetry signals just simply
an overview of whatever we have
yeah um make it actionable whatever uh
signal you create if it's useless it's
useless then don't create that yeah
makes make it that it is
useful um last I almost last I have 10
minutes okay is uh something that that's
for developer we're talking Telemetry
for developers what I think is very
important and I did a workshop about
that the first days in uh this week
about the business cental performance to
Kit um are you do you know what it
is honestly do you know what it
is do you use
it oh come
on yeah it's it's very not really much
used in a community
unfortunately um but it is useful as as
something
whoops um so yeah what it is it
orchestrates performance yeah no it
orchestrates uh how users are using the
system and then you can follow up on the
performance by doing that so just
imagine you have in 3 months you have a
new customer that you know is going to
be challenge let's just say they have
100 users all working in two tables
sales at a sales line and you doubt like
H it's online I need to do some uh
developments
there 100 users constantly working in
two tables sales head the sales line one
of the most heavy tables in the
system you I might want to follow up on
whatever I change in the system coding
like in pte or product I might want to
follow up on the change in performance
that's ex exactly what this toolkit is
for now most of us have been using this
by the start button just start and
setting it up start setting something
else up start and then we forget about
it no that's not how we should use it
now imagine that we run this
automatically every single day we run
this toolkit yeah
sorry yeah okay I forgot about this
slide my apologies so this uh
this
okay this is what I wanted to get
to my apologies uh so uh the uh the
toolkit just now imagine we run this
every single day yeah and we run this in
every single
context that we can run this what is the
context so now just imagine we every
single day we have this set of tests you
see it on the right a test for three
people doing adjust cost entry for three
people doing calculate plan worksheet
for three people opening the custom list
for three people and so on and so on we
can set it up however we like now we can
run that test
in a context of just be default business
Central and again measure durations
measure number of sequels statements for
every single code unit and now we can do
the same for the context our
product and again the same test and we
measure the same things and then we do
the same for that customer and those
customer
customizations and again every day
running the same test measuring all of
these
things that's when we are following up
on performance that's when we when we
are setting up setting a baseline to
measure to comp compare these different
contexts and see what is actually uh
changing so um I have an example for
that let me see yeah I will just show
the uh the end result because of timing
issues uh let me try to find it
so what we created is actually a powerbi
uh report of the end result in this
one and you see here number of SQL
statements for a certain customer yeah
and uh maybe this is a
better graph to show so for creating
sales orders with 20 lines you see here
a baseline the below line is what is the
daily Run for the base app from
Microsoft again I'm always executing the
same code The Gray Line is our product
the purple line above is the customer
and you see it's quite stable you want
horizontal lines again yeah but
obviously from the moment this starts to
deviate this is where you would like to
take action yeah I cannot show you an
example where it deviates this was
actually part of the problem not really
a problem I was like okay we are doing
all this work and we following that up
and we do a daily check and all
that there was no
problem so can I now go live so I was
again this was proof of concept um so we
went live and we actually are quite
happy and the customers quite happy with
the performance this was a real case
scenario 100 people working in two
tables on daily basis and actually insas
and not a
problem yeah the actual problem in that
customers is the fact that he has
600,000
items try to work in a sales order with
that drop down and 600,000 items that
was a
problem
okay okay um I got some other
ideas which I'm not able to Implement
API routes I'm not able to look into the
table of API routes it's a nonrem table
so I cannot create statistics on that
but I would like to I would like to
follow up on extra apis that's being
installed at our customers for instance
table information would be interesting
that I can look into table information
and how big a database is getting like
you have this orphans at that point I
would I would I would see the database
grow because there new items overwriting
the other ones so um those are things
you see there are some links I put them
in some ideas at Microsoft I think we
can solve them on Microsoft level so
because they can read on Prime
tables um and then yeah Stefan uh
Stefano Deano uh he blogged about uh
this uh monitoring for field changes
that was the the the default
functionality I think we can do more
with that that we can avoid change log
and maybe do field monitoring on on
Telemetry level maybe as an
idea last but not least I got two
minutes that's more than enough
um question I always get this extra
Telemetry all of these things you show
that jet reports thing that that you all
of a sudden have a million or not or
more we had at some point 30 million a
day signals just added by jet reports
how can I follow up on that how can I
avoid that
and how do I do cost control because
this database is filling up almost
exploding and that kind of like can burn
a hole in my
wallet no
okay well uh you can do cost control and
I think the best way to do that is not
by
limiting your signals per day I would
never recommend to do so honestly
because because if you limit the amount
of signals a day which you can do then
you're missing out on signals which you
might find important yeah I would rather
try to analyze what signals you are
interested in and what you're not
interested in you can set up data
collection rules yeah that's actually
I'm going to show that very
quickly very easy when you found it once
you will find it again um
if you go to your uh application
endpoint this is just a demo endpoint
yeah you can go to the
workspace this is actually the back end
of your uh of your application uh
endpoint it contains tables which is the
database and you will recognize the
traces table and the page view table
these are actually the only two that
business Central is sending anything to
yeah what you can do here right Mouse
click you can create transformation you
can create transformation rules so you
can create a new rule that maybe says
like uh avoid
dmetry for instance done next and then
set up a transformation editor this is
again kql that is going to decide which
you
allow
yeah that
means that means this guy blogged about
it read the blog and this is actually
what I made of it so this is you see the
source again that's basically everything
that comes in and now you need to Define
what you're going to allow this is the
actual what we use so we don't allow
authorization I'm not interested in that
except for one customer so that's that
one customer where I accept it for why
because I enabled that because he had
authorization issues I needed to get
some more statistics on that yeah same
for soap uh same for API calls I'm
actually just disabling all API calls I
don't want to see any of them because
it's a crap load of them and usually
they just
succeed yeah uh except some customers
because we have some we had some uh
performance issues with them except in
our case eform which is our own API
which I would like to be able to compar
performance on multiple uh customers and
soap I would like to know soap so from
moment anyone is using soap I I I will
allow those so this just displays a
pattern that you would be able to apply
in that collection rule yeah and I think
this is most readable it it's difficult
to come up with something that's
readable enough uh still have exceptions
and all that I'm one and a half minute
over time um I do want to throw this
still um before I do that I want to have
a special thanks to
dilio you hate it
right
yeah thank you so much for your input it
completely changed the the session as
well and I've got some other resources
including Duo including mine the
dashboard that you have seen is online
is in that BC Telemetry repository Dilo
also has a dashboard it's also online in
his
repository um and for the rest these are
all resources I could come up with are
there
questions come on no are there questions
in the top half of the line top half
sorry I need to throw this on the top
half does anyone just want to catch this
no okay yeah you were
first um the session title was uh
Telemetry for developers uh um do you
know of any events or any use cases
where you would use Telemetry right from
your development um environment emitted
and right away analyze them and not just
like deploy to customers then wait few
days and act upon that I mean right
during development where Telemetry could
be of any
use H uh
no I I would have to think about that uh
honestly not from the top of my head uh
it's but definitely interesting um maybe
local test runs or anything I could yeah
local then local then um but then you
need to set up your test environment to
have that specific endpoint and all that
so yeah no not out of the box but yeah
it's an interesting approach
yes I will do first
yeah basketball
player I have an up insides in
thej and I am developing in a Docker
container that emits Telemetry yeah and
I can filter it
yeah yeah with trise or something like
that it should admit the Telemetry okay
yeah depends also on your internet
connection of your dock container
obviously so uh I cannot say anything
about that but it should by default you
know if it's enabled the meetry yeah
yeah okay
yeah
sorry I would like to add something and
then a question um Walo showed us uh
Telemetry for business Central but if
you're running on Prem you should know
that everything Microsoft throws out
there is telemetry so you can do health
check on your NST servers SQL and yes
you get a better picture and I love the
fact that you're comparing customers but
that comes with a big butt right big
what big butt yeah uh I like big butts
and I cannot lie you know
like you get this tenant ID but if
you're running on Prem it's if I
remember correctly you can't so uh get
an ID if you're running on Prem with the
no no on Prem it's a different story yes
a big butt for on Prem is that uh
usually it's either default or common uh
a tenant ID depends a little bit on how
you set it up you can get a decent tent
ID even if you on Prem but then you need
to do uh need to use ACS yeah multi I
think you can if you're running
multitenant on Prem oh yeah then you
need to do that no multitenant I don't
know uh multi tenant as far as I know I
see tenant ID in a multi-tenant
environment on Prem as far as I know you
just need to Define your tenant decently
so you can actually see that but um a
workaround could be that we have one
application insight for each customer
but we could write qu that can combine
different applications insights yeah you
can do that as well that's much less
performant if you do that like for a 100
customers that's 100 connections uh and
I wouldn't I mean I don't bother I just
put everything in one but on Prem for
sure is an issue in terms of identifying
customers do know you didn't see any
company name you have company names as
well in many of the uh of the events I
just H hit them I mean that's kind of
like uh I need to hide them uh and
that's usually how I work on based on
custo on company name yeah and that
works for on Prem as well does that make
sense yeah yeah okay did you have a
t-shirt did I draw it no here
now okay another
one up there oh yeah that's high
enough
yeah look at that um yeah so I'm quite
new to the topic of telemetry so uh just
for my understanding um so you showed us
more like uh newer versions like
business CER 21 and so on um is it
possible to set up Telemetry for older
versions I'm not sure I N I think it's
um um
2019 okay that the first version is you
I I think you can see that you can still
see yeah uh
uh if you go to business Central
Telemetry and you skip the
ads and the first learn article I think
it says somewhere oh did I oh no here on
the
overview it applies to business Central
2019 release wave and later that is as
far back as you can go okay yeah thank
you I think that's 15 sorry
15 oh okay that's 16 I think this is BC
16 so not 14 okay yeah yeah thank you
very much shall we exchange yeah
okay no more questions yes can I do it
from here I
won't yeah exal
off sorry I have the lights my fault uh
um okay I'm also new to Telemetry um I'm
wondering if you are applying that um
application inside uh uh registration do
you already have that uh pre-loaded
stuff uh if you if you connect to your
let's say BC instance you using with
your customer or something um uh we set
up our our environments on rage scripts
and they are just all preloaded if that
is what you
mean uh we set up our pte apps with
templates and that's also preloaded we
set up our own Prem app manually and
that's just copy paste okay so so you
you you really need to do development so
you have the Telemetry data uh to
analyze to to be analyzed yeah we just
make sure that every single Live
customer and app has an an end point so
there is telemetry from Stars yes okay
absolutely and we pay extra attentions
to that uh because I mean it's it's it's
too
important that deadlock thing right uh
the reason why I have a deadlock tab is
because I had a deadlock issue and uh we
had like three 400 Deadlocks a day at
the customer the day we went went live
and there was no Telemetry we just
didn't use Telemetry at all so there was
not even data to look into it in in the
problem right so uh we had the problem
and we still needed to wait like a few
days to be able to just
analyze the messages you need to set it
up and don't think about it just set it
up
yeah uh last question because I just got
that I really yeah sorry thank you it's
actually a follow-up you said that you
didn't use Telemetry with this customer
uh what would be the reason for that as
far as I understood it's I forgot we
just didn't I mean we didn't Implement
that workflow in our company so no not a
single customer had Telemetry at that
point it's okay so so if you set up
Telemetry once for your uh for your
company you can do it for all customers
basically it's yeah you need you need to
set it up it just back in the days like
that version 20 I think we uh we were
working at that point and we just didn't
care about lry at that point okay thank
you now we do yeah thanks there
