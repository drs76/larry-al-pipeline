# Creating Power Automate flows for Business Central that actually matter!

- **Source:** https://www.youtube.com/watch?v=ht2MpW6PXYs
- **Video ID:** ht2MpW6PXYs
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 80m29s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

all right thank you everybody thank you
for coming to my session I've presented
to Big audiences before but I've never
presented in a movie theater and this
literally gives a whole new meaning to
uh having a big stage and being on the
big screen so now when my children ask
me what have I accomplished in my life
i' say I have been on the big screen
yeah uh I'm from the United States of
America they probably tell from my
accent uh but I've been in Europe for
the last three weeks presenting at some
conferences and it's my first time at BC
Tech day
this was probably one of the only events
that I hadn't presented at I've been
presenting since 2012 done directions
done a lot of events so this is like
checking off a major uh item on The
Bucket List I've heard so much about
this event it is phenomenal and just
being here for the last couple of days
for the pre-conference workshop uh it
tells me why this is an event people
love to come to I think this is about as
pure a business Central Technical event
as it
gets today we're here to talk about
power automate flows uh if you were
thinking you're going to be in any other
session there may be time yet to go to
that room I Am AJ andari uh my uh
organization or the company that I work
at UH is dswi well let's see if I can't
there you go I'm the Chief Operating
Officer and one of the ownership
partners of the company I've been
working with business Central since
2007 and I've had the honor of being an
MVP since about 2018 uh I think the MVP
stamp is it looks good but what it
really means is that I'm an evangelist
of the product it doesn't mean so much
that I'm the the smartest person in the
room or the expert I am sure that so
many of you know so many things that I
don't know about business Central uh
about development Etc but I do know uh
quite a bit and more than anything else
I love sharing knowledge and that's what
I'm here to do with you today the QR
code up there is going to take you to my
LinkedIn profile I this again at the end
of my session and that is typically the
best way to get a hold of me I love to
engage with people if you send me an
email chances are it's going to get
buried under a lot of other emails and
either you get a response that day or
you never get a response because it just
got buried send it on LinkedIn and we
can have a very engaging
discussion in July I'll be starting a uh
new podcast called uh only BC fans so
I'm really looking forward to that any
similarity to any kind of name you may
have heard of before is entirely
coincidental also uh I'm a huge Formula
1 fan so if you find me at a bar uh and
we're not talking about power automate
co-pilot or business Central we could
probably talk the night away uh about
Formula 1 so that is something I huge
fan this was actually a picture I took
at turn nine uh at the Austin Grand Prix
two or three years ago with my daughter
so we we have a lot of fun I try to get
to about as many races as I
can this conversation or this session is
going to be uh somewhat conversational
if uh if we can make it that way I will
show you some scenarios and we'll talk
about some uh some things that may be of
interest to you before we get started
couple of things I want to let you know
if you've been in other sessions maybe
you've experien this already apparently
there's a microphone that gets thrown
around uh even though I live in the
United States I move much later in my
life I'm better at kicking than I am at
throwing so there's some gentlemen and
ladies I think in Orange I understand
that can walk up the microphone to you
the first four people who ask questions
uh will receive a who needs
bugs when you have co-pilot or some
other variation of those
t-shirts along with uh some stickers for
my only BC fans podcast and for learning
co-pilot if you have more questions I
mean
yes we'll wait for those to be asked
that's a that's that's good you're top
you're on top of your
game also uh I want to show do a quick
show of hands how many people here are
uh folks who would consider themselves
professional developers people who
develop for a
living all right that's a lot of hands
how many people are citizen
developers all right self-identified
citizen developers okay good uh how many
folks here have played with uh Power
automate before
today about half of the room some of if
you are going to see some things maybe
that you have uh you have already known
but my hope is even for that part of the
audience uh I am scratching a little bit
beneath the surface and you're going to
walk away with one or two things that
you don't know for the rest of you uh
hopefully this will be a fun and uh an
exciting journey of 90
minutes I am occasionally guilty of
talking too fast so I'm trying to Pace
myself but I have been told that even
when I try apparently I'm slow at the
beginning slow at the end
and then as I get into my groove I talk
fast so um I will try to slow down a
little bit but if there's something you
do not understand please raise your hand
that may not count as a t-shirt worthy
question but I will repeat
myself so our learning object objectives
for today I want to keep it simple I
don't need this to be a dozen objectives
I want you to think about what you see
today when you go online and look for
Power automate in business Central or
you go to Microsoft learn so so much of
the content is around workflows and
approvals when Microsoft first
introduced workflow approvals in nav we
did it all in B inside of nvision and
then over time when power automate first
came out we had the Von connectors right
from about then Microsoft started to put
up those power automate triggers and
things that you could use so I'm not
going to talk about it chances are you
know it if you don't know it you can go
and learn those online very very quickly
and easily the things that I want to
focus on are a couple of use case
scenarios uh that are driven by our
business one excuse me driven by our
customers and one that drives our
business I will also talk through a
third scenario that we use power
automate just to give you an idea there
there is no power automate magic as much
as we have leveraged power automate to
do something that really streamlines the
work cycle for one of our team members
then I want to talk about some pitfalls
to avoid when using the business Central
connector actually that last example
that I will talk about will lend us to
conversations a little bit around uh
apis and
actions so let's start off very quickly
with scenario
one what happens with some of our
customers and you probably have
experienced this as well is we automate
some functions within business Central
using job
cues invariably the job cues
failed now you need an automation to be
notified that your automation has failed
how about that it happens far too often
and this became one of the earlier cases
that we' implemented and what we tried
to do is also selectively notify people
about the situation not for every
failure but only for failures and some
automations the solution the situation
here was they were using a Fiel service
application that's an add-on uh you may
have heard of expanded it's not a name
and shame it's actually uh you know I'll
explain why I'm not hesitant to name
them what they do is they have a field
service application the field service
application is used by the firstline
workers when they go out to visit their
clients they collect all the information
they need on their mobile devices and
it's not the business Central app it's
the expanded app for field service they
come back from that from that visit and
when it synchronizes or sends back to
business Central all of that information
flows into to a holding table or
basically a table that's created that is
not part of the standard service
management for nav or business Central
and then routinely a code unit runs and
that code unit parses everything that is
in that holding table and then flows it
over to the service item worksheets if
that is an existing field service order
then it just goes to the item service
worksheets if it's a brand new service
order that the technician took it will
create a service header create some
lines then it will create a uh service
item worksheet So for anybody who's
familiar with service management that's
probably a scenario you're at least
somewhat aware of the tables I'm talking
about but at times the conversion May
Fail now the conversion doesn't fail
because there's something wrong with the
product often times the conversion does
uh may fail because somebody forgot to
capture a mandatory field which maybe we
could do or somebody types in a bad data
type or any variety of reasons and
what's happening with this particular
customer is they serve serve industrial
manufacturers and it's an aroundthe
clock shop so when something breaks in
the middle of the night and it's in the
oil and gas industry you don't just stop
you need to know and they need to know
because they need to fix this quickly
and they need to get this this
information in the
system so we created for them a
notification out of power automate which
captures the type of failure gives them
some information sends out a quick email
now with power automate you have the
ability to connect to over 500 different
pre-built connectors or systems business
Central being one of them business
Central on premises also being one of
them and you also have the ability to
connect to any kind of API and that's
for some of our friends who have never
done anything with power automate so
we're talking about a wide array of uh
situations where you could connect get
information to or from any system where
you could look at a point of failure
that triggers something to happen in
another system so let's take a quick
look I'll show you what happens first
and then I'll show you under the hood of
how we make it and what we
do one part too that I want you to
remember recognize is if you have been
working with Microsoft powerbi and youve
been exposing business Central endpoints
you may be using web service endpoints
the web service endpoints that business
Central has and has had for many years
so if I drag this up here do my
understanding the zoom level should be
uh fairly adequate for everybody here
but if it is too small please raise your
hand again not t-shirt worthy but raise
your hand and tell me uh and so if we're
in
powerbi oh sorry I meant to go to
business Central not powerbi if I go to
web
services and I want to expose some data
out of business Central perhaps from the
customer table or so on I would simply
expose this information for any of our
um you know core Pro developers this is
all standard knowledge this is nothing
new to any of you but when you're
working with power automate or power
apps you have to use API Pages quick
show fans how many people know how to
create an API page from
scratch again a good number of you so I
think some of you don't um I have
something that's already pre-built but I
will make a quick comment for anybody
who is a developer and you build API
pages I still have a little piece of
nugg a nugget of gold for you that
without which I think you will have some
struggles um for those of you who are
not professional developers and you
struggle with building API Pages if
youve done anything in Visual Studio
code I will show you a quick little way
to turbocharge that creation process to
make it faster for the true citizen
developers in the room I will also talk
about two solutions now I don't know how
acceptable it is to name drop at bcch
days but I'm going to ask for
forgiveness instead of beg for
permission and these are solutions I
hold no stake in so there are two
plugins and do add-ons that I'll talk
about and hopefully they'll give you
some
value so let's go ahead and look at the
example and as we look at what's going
on uh we'll bring in some more pieces of
information so here in business Central
I'm going to load up another browser
window I'm in business Central and when
I look at my job Q entries which will
show up in a little
bit I didn't mean for it to refresh but
it has so now we're going to wait it out
I'm in a sandbox environment I'm in the
company Koso USA and when I jump to my
job Q
entries bless you so there are a couple
of uh things that are set to happen and
I can see this is an example of
something that I intend to fail so I can
use in my example this is not actually
what they use um I just picked the
calculate plan for the planning
worksheet because I know that report
can't just be called uh from from a job
Q entry there's some parameters that
have to be run there's some other stuff
that has to happen but in this case this
is just a simple job Q entry that's been
scheduled it's scheduled to run multiple
times uh a day and when this job Q entry
runs and right now I'm going to set it
on hold and then I'll restart it to kind
of force it to
run when I set it to
ready and I go back back and I check on
the log fairly quickly it should tell me
that there is an error message that's
been generated not this one excuse
me let's try this one
again so our job q log entries page will
show me uh all the runs and it'll show
me the error and it shows me a lot of
error detail that's
happened this is the information I want
to capture and I want to send over to my
folks now as this information OCC URS or
as this uh error occurs every time we
want to capture it if some of these
other items in my job que entry list
fail we don't want to know anything
about it there's one other item in here
one other report that I've marked as if
it ever does fail I want to know about
it too the rest we're just going to
ignore so how do we set it up and what
happens when it fails I receive an email
that's automated to the effect that this
is to inform you there's a faill job Q
entry here are some details
and we are capturing a whole bunch of
parameters and we're displaying this
quite simply this may seem like it's
very simple and it's a very simple
example uh but I think this sets you up
nicely to understand some really
important Concepts inside of power
automate number one to get this to work
I have to decide what pieces of
information do I want to expose into
Power automate even though I'm looking
at the job Q entries first to schedule
it what I need to expose is my job q log
entries from my job q log entri page I'd
like to capture some information I also
as I do this will be showing you a
little struggle that new power automate
users have when they need to work with
and retrieve information from business
Central so what did we do to make this
happen and how was a set up when I go
into my power automate maker environment
which is make. power automate.io
get the license to work with the
business Central connector in power
automate and no extra charge with your
Microsoft 365 licenses which are your
office for word excel Etc you also get
the access to standard uh Microsoft 360
standard connectors within power
automate which are like your email
connector and a host of other things
that are out there of the 500 I believe
uh about at least or 200 of those are
considered standard connectors that you
wouldn't pay much for so let's go exam
what we've done here with this shop qer
notification every time it runs it gives
me a log of successful or failed runs
now this particular run my time zone is
off so it's 216 that it says basically
for our Central European Time uh that
would be uh six yeah it is it would be
216 so I need more
coffee that's what it's telling me so it
did run successfully but the success
here doesn't mean it didn't fail it just
means that there was a failure in
business Central that got notified and
it successfully notified me in fact if I
go into my email I might even see
another email that has just come
in or not so come back over here let's
edit and see what's happening so when I
look at the edit it shows me in my
authoring
canvas what the tree of things are so
first it starts off by looking at when a
record is created in my job q log
entries and I'll show you why or why
I've picked this really abstract
sounding uh
endpoint and then I do a couple of
things called get record which when we
get under the hood I'll again explain
why we do do a get record followed by
another get record and then we are
running some conditions and our
conditions are basically checking to see
and I'll explain this in detail as well
but this is an add a glance we're
checking to see if there's an error that
happens with certain type of objects we
have a whole lot of things in our job Q
entries list we are essentially saying
we only care about two and when they
fail we want to be notified and if the
notification and if they do fail then we
want to send a quick email and we want
to capture some values and we can send
this in a formatted or an unformatted
kind of
email and if it doesn't eror out we
don't want to do anything and we want to
continue down the path so the first
thing first is to make sure our job q
log entries are EXP exposed Microsoft
has a list of 44 API endpoints and so
API endpoints are essentially a way to
expose business Central tables and their
customers currencies so on and so forth
chances are that anytime you've extended
a table have a custom table or is a
table that Microsoft hasn't thought
about you're going to need need to make
an API page so for those of you uh who
have made an API page before
congratulations we're not going to make
one from scratch with every little bit
but for anybody who hasn't made one
here's a quick little tip I'm in visual
studio uh Visual Studio code rather and
aside from my Al language extension I
also recommend you get the AAL
development tools this also loads some
other tools in your environment and when
you need to create a new API page
instead of using the T page Snippets try
this one out rightclick new file or
sorry new Al file wizard choose the page
wizard
you would obviously need to give your
object a name so I'm going sorry an
object ID and an object name and I'll
just call it my BC Tech
days cust API this is probably not good
naming practice but I'm focused more on
the outcome than the
naming if you've been using nav and if
you've done nav development some of this
will look familiar to the forms wizard
that we used to have we're going to
change the page type to API
and here you are going to select your
publisher name your group name and so on
and your entity and your entity set name
the idea behind this is when you're
looking at this one match would have an
entity name a set would have a set name
so that when you are looking at this
Empower automate or any other API
consumption situation you would be able
to find it under these categories in my
case it's DW DSW custom apis version 1.0
and this is the name of my entity
set look back here into my visual studio
code my publisher name dswi my group
name the version The Entity set name
those are what's being used and that's
how uh it knows what I'm looking for and
when I say next it will let me choose
very quickly the fields that I want so
this is really cool you don't actually
need to go in and select everything if
you you don't need to go in and select
them one by one you can select them all
if you need them you probably do want to
be a little judicious about what you're
picking hit next if there's any flow
filters that you want to carry do that
otherwise finish and it creates a whole
code so in less than 30 seconds you can
get an API page created for those of you
who are citizen developers and don't
want to create API Pages this way and
don't do anything in Visual Studio code
I advise you to look at appsource uh for
two
extensions these are going to allow you
to create API pages from inside of the
guey of business Central and then use
them right away without never writing a
single line of code in fact one or both
of them I think one of the authors is
maybe in the room or at least is at the
conference the one of these Solutions
will even let you export that API page
into your own solution if you have it a
larger perant extension so one of them
is called Simple object designer from
Eric hugard who is not here in uh at BCT
Tech days this year and his toool among
other things will let you create an API
page very quickly so let's while this is
searching I'll also pull up appsource
apparently it's working a little bit
slower than I would like it to and the
other one is called spare brained ideas
datab
braider and both of these are Microsoft
MVPs and they make some pretty cool
things so datab
braider and simple object designer
choose your pick they both have some
some you know different pricing and so
on but the idea is these tools will let
you create your API pages right from
inside the guey of business Central and
then You' be able to use them to expose
data points into Power automate or power
apps uh connector flows so having built
something like this let's go back in and
let's look at each of these steps and
why we're doing them so in the first
flow that the first step that we had in
my authoring canvas each of these would
be a node and in my node I'm connecting
to an environment which is my sandbox
I'm connecting to my company and the
first time you're connecting it will ask
you to authenticate and then I selected
my uh my table name if I do not actually
do a get record it will not be able to
see any of the fields uh that actually
belong to the DSW to my job Q Ledger
entry so if I were to actually go in uh
I believe I might be in the edit mode
already so
let's for a little bit I'm going to go
to the new design R viiew it's a little
it looks better on the screen
so if I want to add a new node I would
click over here and let's assume I
wanted to use whatever information was
in the dswi job q log entries uh table
that it said which is essentially
appointer to the job Q Ledger log
entries and let's assume I wanted to
send an email right
away say send email from Office Outlook
I want to send this to
Bob at know oracle.com
so I didn't want to really bother
anybody at Microsoft
so and then specify the subject of uh of
the
mail and you know whatever I'd like to
do just say sample email and then I
expect all the different fields are
probably going to be available as
Dynamic values so I'm going to say this
is an email
about an error and then start picking my
Dynamic fields and I go into this uh
Dynamic field picker except these are
the only Dynamic Fields it shows so I
already connected to my main table and I
would expect all those fields to be
showing What's Happening Here well what
happened is we have only said start
something and this is the trigger point
when a record in that table is created
it actually doesn't know anything about
which record uh or of that information
at this point at least not inside of the
flow so the first step I need to do then
is to go back out of here delete this
node which I was adding here and I need
to get that record that is problematic
so here we'll again list the same
environment the same company the same
API category um actually come back to
this one later this one and the same
table and then I have to say I want you
to set the row ID to for now just if
you'd like to memorize and I'll explain
why in a little bit you would have to
say I need this to be the body row ID so
this is what we're trying to find so
from that table we want to find that
specific row
ID anybody who's a developer all knows
that when you think of a table like the
customer table your primary key is the
number
field in this particular instance this
is not a actual field that we see in
business Central the row ID is a guid uh
that is that is set for this particular
uh API table so we'll see another
scenario later and I as I show you some
useful tips I'll talk about it once more
but we are now at this point saying this
is where you get the record for this
particular failure and at this point
when I set my email as we go down the
flow all of of a sudden my Dynamic
Fields will now show much more so I can
see
my let's go down here
ID status user ID description all of the
things that I had in business Central in
my jopu log job q log entries page let's
go down here once
more so these are all of the fields that
I'm seeing up here now suddenly they
become available when they weren't
before and that's because I did a get
record so when somebody's using power
odate for the first time this tends to
be one of the trip ups that you just
start something and then you go why do I
not have the record information
the second thing was I found that when
we're working with
companies and I want to include a
company name in my email like I'm doing
here with a dynamic field it actually
shows me the company go it it doesn't
actually recognize or resolve the
company name so I had to force it in a
second step to say for this
company use one of the Microsoft
automation apis called automation
companies and capture something which is
called The Body Company ID
with that information in my email I can
then choose for company the dynamic
field which
is from
here display name for the company and
that would show the proper name like
Koso
USA when you're working with uh Power
automate and you're using something like
a condition it shows things a little bit
differently than you're used to so your
ANS and your ores are shown this way so
essentially it is only going to go to
the true case if my status is error and
object type is report and one of these
two conditions is true because of the or
so you've got these two report IDs that
I've put in so those two objects when
they error out that's the only time it
will catch them I'm then sending an
email in each of these situations if I
have some other fields that I would like
to show or add I can do that save and
then I set my flow to run and that's
basically the first walkth through where
we're creating and sending some kind of
a job QR
notification what we'll do now is move
on to a second scenario and I'll explain
the construct and what happens in the
second scenario as I move to that next
slide we're Services based
organization we consult our people enter
their time we create invoices send
invoices we get paid for our time our
problem I hope uh you are not facing the
same but our problem for the longest
time was we would not get our team
members entering their time by Monday at
10: a.m. which was our policy which
would push back our billing and would
cause real world issues for us so after
a lot of different pleading and asking
and doing nice things we thought we
would Institute a bonus as a carrot and
a stick which was a power automate flow
so every week when they do their time
entry on time by 10: a.m. they get $25
uh sorry
$250 uh oh $25 a week yeah that adds up
to about 1,250 or so dollars over the
course of a year and then if they don't
do it they also get a notification uh in
your email and they don't get that extra
$25 and so here we had to make some
changes to different parts in business
Central we extended out the time sheets
to say how many hours we expect from
them every week on the resource card we
also captured the email from the
employee table where we have an email
field and then we created something
called a schedule
flow this is different from what we had
before in power
automate the first case that we worked
with that was called a cloud flow so
when you're creating flows you'll see
you have an automated Cloud flow which
basically means something automatically
happens when there is an event in the
trigger an instant Cloud flow is you
trigger that on demand and the third one
typically that we use is our scheduled
Cloud flow and in our scheduled Cloud
flow we're going to have something that
triggers off at in my case 101 a.m so
I'm going to show in our live business
Central environment what we've
got so as I look
at our resource
cards because this is not financial data
I'm actually showing you something from
production so for somebody like uh
Denita who's one of our team members
she's expected to have 38 hours put in
every week by 10:01 a.m. so we put that
in we captured the email address and
then every week as the flow runs it
sends them a uh an email only if they
haven't done uh what they are supposed
to do which is 38 hours of time entry
the email looks something like this this
is where I'll momentarily pull it off my
screen I accidentally closed my email
window and I don't want you to see all
my real world
emails time entry
uno momento pour forward this we're
playing like the hold music just pretend
like you're in an elevator and there's
very soothing music going on in the
background I love this okay overdue time
sheet that's a subject I'm looking for
I wish everything in life happened this
way you just think it out loud and it
just suddenly starts
happening so this is where somebody on
my team you know receives an email and
says hey dear Sam or in this case Donita
has had some overdue on so we'll go pick
a one that where Donita did not do her
time says you're Donita your time sheet
for this period was incomplete as a
reminder all time for the previous week
must be entered and then also in my
power uh in my power automate app I get
a notification that says five people
have not done their time this week and
in a later version that we're putting in
it also append to a bonus sheet that
we're you know so I don't have to run
the bonus calculations manually so what
we do to get get all of this information
after we add the information into uh you
know those extra Fields into business
Central obviously we also had to create
some other apis one was for the time
sheets so just like I showed a previous
API page we created one over there and
with that information we are now able to
go in and trigger a flow let's go into I
have two versions of it let me pick the
one that is not manual this is the
automated time sheet
reminder and this particular
one it is set for recurrence so it runs
every week at 10:01 by Monday on Monday
and if I would like to see some more
advanced options you can see um you know
by at this time zone
Etc it looks to see in the time sheets
uh API
table and it then subtracts seven days
Poor Man's way of saying I want to see
everything for my time sheet that starts
one week ago on a
Monday and then we initialize some
variables so for all of our developers
we kind of understand why we would do
that because what we want to do is take
the records that we're finding after we
subtract seven days
and we want to hold them and we also
want to get the correct date when we
subtract seven days from today so we're
saying what date are we looking for
we're going to hold this it's just an
initialization of a variable then we
create a simple loop our Loop will get
the record the record will show our you
know that this is the time sheets record
much like we did get records the last
time for all the same reasons and then
we have some
conditions and the conditions we
basically looking to see if for the time
sheet um we have people enter the number
of hours that's expected on the time
sheet card and we're sending a nice
little email here that you saw and then
we are incrementing our variable so I
know at the end I get a little
notification that says how many people
had overdue time sheets for this
particular period in time now this
solution and the other one and a third
one are going to be available on my
GitHub so when you go back if you're
interested in you can export you can
import these Solutions into your
environment uh and you can try them out
these are just two scenarios that I
wanted to share and then I wanted to
kind of scratch your brain a little bit
with a third
scenario we have an account manager who
goes to visit our clients every month a
accounts get a monthly visit B accounts
get a quarterly visit and so on and
usually if their customer has an
outstanding
balance he will not notify them and they
will say oh I don't think we got the
invoice can you send us a copy of the
invoice and so on when they get that
request when he gets that request
normally he would come back to the
office go into business Central go to
the customer card load the customer
statement or to send the PDF copies go
to the list of sales invoices select
them and then do send email a handful of
steps here's what we did we went into
and created a new API for the customer
and the posted sales invoice Pages we
created a code unit a little rather a
method a a function and that function
will allow us to send an email for all
of the open invoices for the customer
and the the implementation in power
automate was simply a trigger for a
manual start which is a manual Cloud
flow so when on his phone he goes into
the power automate app and he runs the
flow and he pushes the Run button it's
it's only going to ask him one thing the
customer number and we could have done
that as a drop down list as well but
right now he just types in the customer
number and then he hits okay it sends
out in 30 seconds a list of all the
invoices as one single PDF to the
customer so the magic wasn't so much in
power automate the magic and power
automate is simply he pushes a button
and it calls an action from an API page
but by doing it it now allows him to
send in less than 30 seconds something
that would take him 5 to 10 minutes to
do before in general whenever you're
thinking about business Central Power
automate cases I want you to imagine
those types of
situations before I transition into kind
of tips any questions about these flows
that we've
done t-shirt
opportunity all
right so going back into my power
automate here are six different things
that I want to discuss a little bit
number one
find don't get so in business Central
Power uh Power automate connectors you
have a lot of different triggers and you
have a lot of different actions and so
if I go into uh into Power automate in a
scenario here I'm in my power automate
if I said create a brand new let's say
automated Cloud flow just call it a
sample
flow and I'm looking for business
Central triggers so triggers are
something outside of the system that
will cause a flow to run right
so these are some triggers like when a
record is changed when a record is
deleted when a record is created Etc and
then you also have things that are
called actions so let's just say for a
second I want to create an instant Cloud
flow sample instant
flow and here when I hit the a new
create so when somebody push is a
certain button then I want to run an
action and the action could be to get a
customer record that the user types in
so first I want to collect some input
from the user so collect an
input they would be asked to put a
customer number I would hold this as a
variable called cust
no and I would give them some
userfriendly guidance that says please
enter customer
number we will take this
input and we would then want to be able
to get a record I'm using the word get a
record because that is typically what we
would do in BC uh if you had to do
something you would get when you already
have the primary key with you so when
you go to business Central actions
here you will
find it's just filter on premium so it
kind of loads up business Central ones
first so these are all the different
actions and in terms of finding or you
know retrieving records there's a find
one record find records and get record
and almost without fail anytime a client
of our starts using power automate I can
set a timer to it within a day I will
get an email or on for Consultants we
get an email that I can't retrieve a
record it's because they use the get
record uh connector or the action and
when you do that it says select your
production or sandbox environment select
your
company which could be your coron USA
company your API category will just go
with the standard Microsoft one and
because we're collecting a customer from
the drop- down list we'll select the
customers this is the table name for or
the API name for the customer table and
then in this row ID space they want to
take whatever the user has input in the
manually trigger a flow parameter and
that's what they want to drop in here so
they're going to go here and they
typically try to select the
where is my oh
I'm y either I wasn't seeing it or it
wasn't there but regardless I see it now
but when they do it fails because what
you see with row ID is not actually
translating to the primary key at all it
translates to something that that's
generated from the system guid it's a
whole different identifier what you
instead need to do is you need to use
the find record method so if you use
that action let's delete this and even
that requires a couple of extra steps
that you may not think about so I go to
business
Central
find if you don't see it click on see
more find one
record and now once again I'll go
through the process of selecting my
environment I will go through the
process of selecting my
company the same API
table and then you have to go to your
Advanced
parameters you can say show all and here
you have these extra things that you
need to fill out if you want this to be
ordered in some way doesn't matter order
results by does not matter and then a
filter you actually need to set a filter
that says the number field on the
customer card must equal
to with a value that you have collected
from the user so my cust number
parameter this is where once you do this
it's going to work but before I complete
this step this also logically leads to
item number two new and item number
three the new designer in power automate
is not your friend and why is that so
the new designer looks really friendly
and it has that new designer toggle
there's some connectors some actions
where all the properties do not
correctly work as a matter of fact with
this particular one right now it won't
tell me that this doesn't work in the
new designer it's only when I edit it
that it tells me this connect this
particular action doesn't work well
right now what I would see is if I
actually wanted to use from a drop down
a Dynamic drop down and see all of the
fields that exist with this particular
table I would not be able to see them at
all and so when I'm typing something in
it may or may not be the correct value
and it may not may not work so what I
almost need to do always when I'm
working with this situation is first
let's save this so I don't lose it I
switch off and toggle from new designer
to the old designer oh I got to save and
switch it was still saving and this is
not just for business Central yesterday
and the before I did co-pilot Studio
workshops even in those there are some
scenarios where in you are in the new
designer and things just don't work well
so anytime you're working with it I
suggest for now that you disable the new
designer mode now when you go back into
find one record go to Advanced options
click here and a drop- down assist will
show up and you'll be able to correctly
pick what it is that you want to do at
this point you have your number from the
customer table you have the customer
number field that or the value that
you've collected as a parameter and from
here you should be able to then add a
new Step which is your next node in the
process and then you may send an email
or a notification or whatever it is so
if I want to send an email I could send
an email to somebody saying this is the
customer name Etc we won't actually
follow this all the way through but I
just want to establish that here now in
my Dynamic content I will see all of the
fields for my customer table my name my
display name my city state balance tax
registration all of the different fields
that you expect typically would start
showing up so I can start utilizing them
in an email that I might want to send so
this is uh an important thing find Rec
find one record as opposed to get record
move to the old designer instead of the
yeah move to the classic designer
instead of the new
designer the next thing I want to talk
about
is API pages when you're building API
Pages by default either when you're
building them by hand you may not
remember to uh do this or when you use
the alaz wizard that I talked about
before the API page that it constructs
is usually lacking one important
property that Microsoft even your
documentation highlights as pretty being
pretty important so let's close this out
here and this is that custom API page
that I built and the one when it was
building it it gave me the most
important properties that you typically
expect which is your API Group publisher
and so on and then it goes into the
layout area and it starts adding under
the repeater uh general for the content
area all of my different
fields usually this would seem like it
works well enough but what you need to
do is identify something called the
system ID there is a OD data um property
that let me bring back the PowerPoint
slide here there's an OD dat key Fields
property that needs to be set and that
needs to be set to be as I will show you
on this particular page let's go to time
sheets
API set it to system ID and that is a
field you are going to have to create an
add manually under the repeater so
besides all of the fields that you have
already added you will want to go and
add this field system ID which points
record. system ID the caption is not so
relevant this is going to be a step that
you need and what basically Microsoft uh
says in the documentation is that by
having this it basically creates an
immutable uh you know kind of an
uneditable goid data type field which is
the unique identifier for this record in
the API page con context so while we
already know the unique number number or
the unique value identifying the record
on a customer record is the number field
for API purposes we have to create yet
another thing called a system ID that is
essentially where that row ID that the
get record is expecting uh that's what
it expects to get back but we don't know
what it is when we are working with a
power automate flow therefore we use the
find one record and we use the filtering
technique to be able to do what we have
to
do the fourth thing I want to talk about
is and remind you is the company name
and I showed you that when we are not
using the company name one of the things
that happens is it shows a company goit
but does not give you a userfriendly
company name to work
with the fifth
item even though Microsoft has a list of
about 40 some apis if I go back and
power
automate I can see the list once more so
if I go back here and we add another
step
here and we're looking for business
Central actions
there
are oh my bad here let's just first
select
one or you can just go back over here to
one that's
populated so instead of customers if I
wanted to look at under
v2.0 these are the ones that are created
by
Microsoft there are a few things that I
always have had to struggle with and I
think other people who' have been using
it have struggles with as well one is
that they unnecessarily add captions to
these and these captions for the various
Fields do not actually match the
captions that you standard expect out of
these tables so when you are looking at
the customers we know the primary key or
the fields that we work with are called
number name name two Etc instead of
getting those you see the word number
spelled out for name you see something
called display name and so on so
it becomes hard for you to relate to
relate the fields that you know in
business Central to what you're seeing
here but even more important we have
found with some apis that Microsoft has
created they are just bugs this is one
good example if I were to return a
customer's balance in an email which we
will uh which we can try right now in
this particular flow so we manually
trigger a flow somebody will type in the
customer number we will go in here we
will find the customer C's number and
then we're going to send an email
showing what is what the customer's
balances and here it's going to say
customer
name customer
balance Dynamic
content and I'll search for B balance
now look at what this field is called
there's only one balance field and it's
called balance du so I'm going to select
this we can remove this last node we
don't need
this save
it oh there's some there's an error
somewhere I need a
subject customer balance
notification save it
I'm going to log into my power automate
here what I'm doing here doesn't show up
on the screen but you're not missing
much I'm basically just going to pushup
button first I'm logging into my account
because I have way too many accounts
any day now we can play that music again
thinking out loud
here all right so I'm almost in
here sign in authenticator so as soon as
I get this done and we get an email
which is going to happen right about now
so I plug into my U my power automate
and I'm going to select from my
flows that we've just
created or you know what let's do one
better because it's working a little
slower than I like it we'll do a manual
test of
it
test okay continue it tells me that it
uses these two please enter the customer
number I enter 20,000
run
flow it says flow successfully
ran now while we're waiting for an
outcome let's go back into uh this flow
which company am I in here for this
example coronus USA in
production let's change to environment
coronus USA
production and when it lands over here
let's go look at that customer 20,000 to
see first what that balance
is they have a balance of
3,36 but the balance due is
20244 and this is the amount that it
says it's going to show me because it
was called the balance CU field
except it shows me 3036 so this is
essentially giving patently incorrect
information balance and balance do are
very different fields and this is just
the tip of the iceberg there are some
other issues too we have found with API
points so I would always recommend that
you create your own API endpoints for
the projects that you're building and in
some cases you even consider uh diff
even for the same page like customer you
may want to build more than one API
endpoint based on the different projects
you're doing because you don't want to
have every single field on this page
pre-listed in your API you might just
want to build something with what you
need for this project separately and
this project separately it's not an one-
siiz fits all but that's just a humble
suggestion for my
part so then one more thing that we want
to talk about here co-pilot studio power
automate and business Central so
yesterday uh we did a workshop and the
day before yesterday we did a full day
workshop as well and we spend the bulk
of our day understanding how co-pilot
Studio worked and you we've been talking
about co-pilot everywhere so I didn't
want to go through the whole day not
talking about co-pilot either felt I had
to do my part so in co-pilot We examined
when we're making a custom Chad bot
there's some very nice opportunities for
us if we want to connect to business
Central and retrieve and send data so
when you're looking for a use case
scenario your workflows could start from
your phone your workflows could start
from a trigger that happens inside of
business Central or your workflow or
something could start from a Chad bot so
here's a quick view of a Chad bot that
we' created which is a finished product
and then I'll show you a little bit
under the hood now you're not going to
walk away becoming power uh co-pilot
experts as a consequence of this
but let's go into co-pilot
studio and I'll launch a pre-built demo
co-pilot this is something that we built
in our project the first day on the
workshop
it's called My Koso customer service
co-pilot and there's a demo website that
we published it
to this co-pilot was trained to do a
handful of things like uh give me the
weather or if I also asked it for some
customer information on balance it could
retrieve that and so if I would say
if I can type
first what is my customer
balance happy to help what is a customer
number in business Central I'm going to
type in some kind of number
25,000 oh looks like I fat fingered it
sorry no you've provided the number
you've provided does not match anybody
so there you know kind of some error
handling in my chat bot I'm going to try
it again I could have configured the
co-pilot to go back and just say hey
what's the number or just once again uh
promp me but here the way I've set it up
I have to ask my question one more time
and it could have been what is my
customer balance what do I owe you can
create a whole bunch of phrases that it
sets and listens to this time I will put
in a proper customer number and it will
come back with some information now it
tells me what the credit limit is what
the customer balance is the currency and
if you saw some examples in the demo
earlier today from Microsoft it also
used some nice adaptive cards and you an
Adaptive card being something with a
little image different font weights uh
maybe a hyperlink to go into business
Central from there and this was all done
very simply with the power of co-pilot
and power automate together so when we
were building out our
chatbot we created something called a
topic and a topic was whenever somebody
in my chat said something like customer
balance what is a customer ow us what is
the customer AR Etc it would start
asking questions like what is the
customer number in business Central and
when they type in a value we are
connecting out into a power automate
flow and here this power automate flow
is then connecting back into business
Central it's going to show up in a
second so if I were to edit this
particular one
now it says power virtual agents here
for anybody who doesn't know co-pilot
Studio used to be called Power Virtual
agents in a previous life so in your old
or classic designer that's what it says
so we took the value from the user in
the
chatbot we initialize some variables
that will allow us to handle what
happens if the number is correct or
incorrect we took whatever value the
user is feeding us from the chatbot to
retrieve or try to retrieve that
customer record in business
Central and then we check to see if that
customer number exists if it does exist
as an if it is valid then it will do a
handful of things where it will set the
values for each of these excuse me this
is going to be in this part of the tree
it will set the value for the customer
name from the C from the business
Central connector it will said the
balance it is going to tell us a credit
limit
if it did not get found then it will
just populate blank values and also tell
us that the customer not found property
was true we take all this information
back into Power Virtual or into co-pilot
studio with all of these
outputs these five outputs flow into
back into my Chad
bot and then if we had a bad customer
number we're sending a message that says
sorry the customer number number you've
provided does not match any
records and if this was a correct number
then we're showing this information that
says hey this is the customer number
this is or this the customer the name
balance credit limit
Etc and then we can take this to some
other topic so we could have actually
created another Topic in co-pilot Studio
maybe that says what would you like to
do for this customer do you want to
notify them about their balance do you
want to do X Y or Z each top topc is
basically a thread of things that can
happen when a user says a word in
co-pilot in the chat bot so this type of
experience can be published on a website
that nobody has to log into or if you
have a customer service portal it can be
plugged into there and if they
authenticate with a username or password
it won't even need to ask them the
customer number we can already provide
that information as a variable into
Power automate you can also publish this
inside of teams if this is for your user
experience expence so if I want to take
this experience and I want to plug this
into a team uh environment I just come
to channels and I say go to Microsoft
teams I may already have plugged it in
so let's see yep it's actually already
there so I'm going to launch my teams
here and then as I build through
my as I go through rather my teams I
could see this along with everything
else that I have and I can pin this so
just as you would search for somebody
else in your organization to talk to uh
you could also look for your chatbot and
your chatbot can have a nice friendly
name and whatever the case is and then
as you're talking to the chatbot the
same type of questions we asked before
what is the
weather what's the weather like or you
know customer balance
so this is not pulling from business
Central this is actually pulling from a
uh a public service like MSN
weather as I finish this chat then I can
go into what is my customer balance and
then goes into another topic and another
conversation
Etc so this takes us into kind of the
same type of conversation path we had
before
and we can continue to build
out building co-pilots or building chat
Bots is not that complex I think in the
conversation this morning that Vincent
and Arena uh and Ida showed a lot of
that was around an experience where you
have to be a developer to do it and if
you are a developer and you're creating
co-pilot experiences from business
Central that is fantastic but you can
still create these experiences in
co-pilot studio in a very low code uh
friendly environment and you could
leverage power automate that is one
other reason why you may want to learn
uh to use this very nice and awesome
tool I want to leave with you with a
couple of other things that you may or
may not have thought about as you're
going through Power automate if you are
struggling with some basic and Core
Concepts uh Microsoft does power
automate in a day powerbi dashboard in a
day and so on in a day's courses and I
recommend that you look for those which
you can start and there's a link right
over here called register for free
one-day automation workshop and these
are instructor-led these are offered at
no cost so this is again not a sales
pitch this is led by MVPs and other
people in the Microsoft Community but if
you actually just want to run through
some of these courses yourself reach out
to me on LinkedIn and I can point you to
the resource where you can run through
this by yourself at your own
time power automate also has a nice
library of templates and if you're
looking for various types of templates
uh that that you may want to handle uh
start searching over here under
templates and you can go into business
Central and look at some
scenarios now there may not be as many
as you would like to
see little bit of song and dance
well I'll give up on the
search just when I say that it comes
back but again a lot of the examples
you're going to find are based on
request approvals but they are starting
to add non-approval based as well I want
you to consider another scenario when
you go back where if you have a tabular
list or a CSV file importing those into
business Central that is not as hard as
it sounds start with one of the template
workflows that shows you how to take
something from an email a table and we
create that into a SharePoint list and
those that same type of concept can
allow you to push data into business
Central into tables as
well I believe at this point I can Yep
this is the link if you would like to
scan and um download the solutions that
I've created here today I'll open the
floor up for questions if you have
t-shirts are up for grabs may even give
you a fifth one if nobody's
watching questions
yes could somebody please get the
gentleman a
microphone there's supposed to be people
wearing orange
shirts people wearing orange
shirts I think somebody's walking
down say it
again uh maybe not orange all right here
if you just want to speak out really
loudly let's go ahead with you
first toise on premesis okay
yeah Micosoft
% yeah let's have you ask ask again
thank you so
much so my question is uh how is this uh
all things fit in with the onen
installations especially also the
copilot
thing so when you're working with an
on-premises deployment of business
Central or even Dynamics there's a
couple of extra steps that you have to
start off with uh the first step is
going to be to expose the OD data V uh
V4 ports and to do that you're going to
have to open up at least one port you
could do some Port mapping so instead of
7047 being exposed or 7048 whichever one
was a standard Port you can do some Port
mapping you would want to make sure that
you either have a fully qualified domain
name or an a record that would be
exposed out you would need an SL
certificate from a trusted uh
certification Authority uh not your
self-signed certificates so it would
have to be from like a GoDaddy or
whoever your popular uh certification
provider is with that you will actually
get a proper URL that you would be able
to use in your API uh URLs that you're
going to need and that is essentially
going to be really important this holds
through not just for power automate but
also for powerbi and power apps Etc
without that you're not going to be able
to use them all these web services the
webbased services from Microsoft
absolutely require a third-party trusted
certificate so whether it's less en
Crypt or a commercially available one
self-signed certificates will not
work uh one other part I'll make a
comment on is some of the connectors
that we have V3 like you saw are not
available in the on- premises
environment some of those are V2 and I
don't know for how much longer if
they'll ever change but if you notice
they'll either say preview or beta on
some of the ones but we do have usable
uh scenarios or we do have implemented
scenarios of people on business Central
on premises so it does work it's just in
the in the cloud environment it's very
plug-and playay because single sign on
which again one other thing comes to
mind if you do set up people with
Microsoft uh entro ID single sign on for
our business Central that can make your
process much easier then if you don't
have
that there's somebody else in the
background then we'll come back to you
Peter oh a of people uh I think this
gentlemen the blue shirt maybe was the
next
one
yeah and I won't forget you Peter and
then I know some people in the back and
we'll take yes uh hi so um basically
let's imagine we have a WMS system or
some external system which has like an
old interface like SQL um and uh could
we use power automate to for example get
some data from business Central via the
on- premise data Gateway and communicate
with the um SQL interface and would you
consider this as a as a good option to a
valid option to to do it like that sure
uh I mean is there a reason why you
don't why you think it would not be uh
basically Le yesterday they were some
workshops with Legacy interface and they
were yeah considering C development for
for communication like this so I was
just curious if it power automate is
also a valid option power automate is a
valid option I will say based on the use
case scenario that you have and how much
time you want to spend if it is a simple
mapping of things from one table to
another you either want to use power
automate or you could use a commercially
available isv tool and there's at least
half maybe three that I can think of
that have a simple mapping tool from
point A to point B that you can use for
quick results it's just if you want to
take control of your destiny and you
want to use power automate not pay
anything extra in licensing to that isv
then go down this path with BC on
premises do need power automate
licensing it is not included with BC
online it's free of charge but the the
short answer is yes it is absolutely
capable I don't know why uh you should
have run into any kind of an
issue um oh boy do do we want to keep
count yeah just maybe pass on to the
next
person I will throw it uh to the front
in a moment I love you Peter I'll come
back yes sorry go ahead yeah so uh yeah
my question is uh in in this power
automate demo you shown uh you uh
indicate the company but how do you deal
with uh or what is the best practice
with multiple companies within a single
environment because if it's one or two
you can have uh multiple flows but if
it's like 10 or more then it will become
hard to maintain it does become hard to
maintain I agree but because all the
most of the tables that we access are
data per company customer information is
data per company and so on it's kind of
the way you have to do it there isn't
really a better thing I can think of off
the top of my head especially if you're
implemented in business Central in the
cloud if you're in the business Central
in the cloud I can't tell you to go and
talk to the SQL database and get
anything from there so your choices are
fairly limited uh the only other thing I
could think of is if you don't use the
Microsoft dataverse connector but in
some way get all of that data into
another database or into the M into
Microsoft dataverse where you no longer
have things separated by company at that
point you can connect to that as your
data source and not business Central and
try to create that but because of the
way it's set up and you saw company is a
mandatory field so that is what we have
if you want to throw that up here this
gentleman has had his hand for a very
long time and then we'll pass it
back my good friend
Peter yes sir thank you AJ um I see if
you are in your own environment you can
make it but if you are make it for
customers so how do you make the
versioning how you make um the
deployment if you manage it in your
environment and you have want to give it
to One customer to two customer to 10
customer um that they have the same
version do we um if you are building
something we have GitHub you have having
automatically pipelines and we making
automatic deployment maybe you can say
something about here with the with this
um Power autom how can I really manage
it if I have it out in the field at a
customer so I will start off with one
answer and then we'll kind of build on
this a little bit in general it does it
poorly but the doors are opening so the
good answer is I have experienced
troubles when I have exported my
solution and try to import it into
another environment in general it it
Imports and the experience should be
that you should be able to change the
parameters and it should work it hasn't
always worked that way um in terms of
source code management uh there is a way
it is not like when you're doing Al code
in Visual Studio code and you have get
enabled and you're basically connecting
and Publishing straight up but there is
a way to do it um I think if you talk to
maybe Milan or ronado I'll will connect
you to somebody who I've talking to just
last week in Germany at days of
knowledge and they were talking about
the way they have done that but the
model is there but we have experienced
struggles lifting and dropping a
complete completed solution into another
customer's environment moving it within
my environment with the save ass to use
it for another company or some other
solution has not been a problem but
across tenants we have experienced some
issues yeah uh whoever was an ex person
with your hand up just yeah thank you I
know that general area had questions so
we'll just pass the microphones around
from one person to the other
yeah a thanks for the opportunity um
it's a two4 uh the API connections has
got a limit of around 100 connections
per minute have you ever faced that
limitation so we basically calling API
uh uh connectors right in the a little
bit louder I'm having trouble understand
you sorry oh sorry yes um we're
basically connecting with power automate
to uh apis within business Central
there's a limit of 100 connections per
minute have you ever faced that
limitation I have not quite simply
because we do not have that many
connections happening so I think it's a
matter of our situation has not caused
that to happen um I cannot comment on it
but again I can connect you to somebody
who can probably help you with that
coolness or at least validate or give
you a workaround but we do not we know
that in cases of uh you know in most
cases there is a limit to how many
connections you C you can have and you
do need to consider that there is the
licensing for number of connections and
so on and so forth so I think that is
something you're probably running up
against but maybe offline if we want to
have a specific conversation we could go
into details 100% by the way the first
four people who ask questions I haven't
forgotten you please come up after
afterwards and we'll uh give t-shirts
and then out of all of uh uh the
features that you shown today what is
included in the business Central uh
license all of that all of it every
single thing you saw today is at no
extra cost to you if you are using
business Central in the cloud the
co-pilot chat experience that I created
that would require a co-pilot Studio
license to build the chat experience but
if you want to experiment with it there
is a developer plan or a trial that you
could use to build those chat
experiences without having to pay
upfront ah somebody with the orang shirt
is
back all right who is the next person
with a hand up I think there are some
more people in that General proximity or
now we have somebody up
there thank you
where the uh workflow lives lives it uh
in your account and die if you leave the
company or live it in the whole
environment one more time the flow is it
in the account or is it in the company
is that what you're asking yes LIF the
lift the flow in your account or lift it
in the tenant the flow is in my account
in something called an environment and
that environment doesn't match business
Central environments so if you're in
business Central and you're looking at
your let's just go back
to my where I was doing all of this
work lots of
tabs so when I'm in business Central I
can see I'm in an environment called
production or sandbox these are
exclusive to the business Central
construct when I work in power automate
I have these other environments which
are dataverse environments or which are
environments excuse me Power Platform uh
Power app environments
and so these are where you can choose to
put things usually you have one default
environment for your organization and
then you can have other additional
environments you create sometimes they
could be for sandbox or they could be
for real world production purposes as
well you do not have any a a onetoone
link or onetoone relationship between
the two you can create five different
Power automate environments and they can
all talk to business Central in one
environment so the long answer to your
question is no deleting a company in
business Central does not mean you lose
your power automate flow even deleting
your entire business Central environment
does not mean you are going to lose your
flow and the flow is losing if I delete
your account
yeah okay you lose everything at that
point including your
emails so kind of deleting your account
because remember if you're a business
Central user there is no way to just
delete the business Central login you
disable it but I am taking deleting
account to mean going to the M365 admin
Center clicking on the user and deleting
it which is which will delete everything
if it's created by that user if it is
created by the user in a company
environment that stays if it's created
in the user related environment that
goes
away yeah okay is it a good idea to use
uh user administrator at something to
create the workflows
sure but I think maybe what you're
trying to get at is should you put it in
the glob in the main default environment
or the user environment is that what
you're
asking you should put production things
typically in your default environment or
in an environment that is meant for
everyone and not somebody's uh
individual environment for that's a
Sandbox testing type of
place so yeah thank you you bet if
you've used powerbi I also want you to
think about workspaces there's like my
workspace there's
a lot of different workspaces you would
typically not put production things in
my my workspace you would build and put
them in a specific workspace that other
people in the organization can benefit
from my question is maybe related to the
last one uh my colleagues from my teams
have several similar issue that in power
automate flow we have seen some custom
fields and we when we try to switch to a
user account this Fields part of the
record wasn't visible what might be the
reason for that and was it the business
Central connector
yes could it be because of the security
where but we tried to change the
security it seems not also some
licensing assignment or or stuff like
that it seems not it was really strange
it was then I would probably need to see
that up front but yeah I would normally
start with security it was C even then I
would expect the field to not show I
would expect the field to show maybe the
values to not populate or but so on only
Fields related to the key was visible
and and other fields not visible for the
customer it was strange I don't have any
sessions tomorrow if you want to bring a
laptop we can sit down for 10 15 minutes
and look at it okay happy to do that
thank
you next
question uh it's G to come over here
oh what about
permiss perm what about permissions
because of the way this connection
happens to business Central if you're
using the built-in business Central
connector anytime you're trying to
retrieve information it is going to look
at your Azure active director your enter
ID which is your business Central
username if you do not have the ability
to view or write into that particular
field or modify that field from the
business Central interface you won't be
able to do that from the power autom
connector either so it does absolutely
respect your permissions if you were to
use in you know if you were to mirror
that information somewhere else and then
expose that data then yeah all bets are
off but usually using this connector
your permissions are
respected any other
questions right going once going twice
if the people who ask questions the
first four please come up I'd be happy
to give you some anybody else who wants
stickers I will uh leave them up here
please feel free to come and grab some
stickers on co-pilot studio and the only
BC fans because we are all only BC fans
right we love business Central so once
again uh here is my QR code for my
LinkedIn my email
address thank you for coming please
review the session I'll love to know if
there's something I can do better next
time or what you would like to talk
about in the next session and thank you
for coming to the confence hope you have
fun
