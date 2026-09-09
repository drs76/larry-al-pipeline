# NAV TechDays 2017: Best practices to get automated tests running on your solution

- **Source:** https://www.youtube.com/watch?v=NCnXbncCT0M
- **Video ID:** NCnXbncCT0M
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 96m58s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

the history today is made right now on
this second session we have here
an
unofficial attempt for the Guinness
World Record in this session
you're all part of it
because today is the tallest
presentation duel ever welcome to gyms
and look
and not be afraid to take pictures
because this is really the tallest to do
of the enemy take this
[Laughter]
was yesterday evening we had at one or
two beers yeah yeah so welcome I'm James
Luke and
we're gonna try and entertain you
educate you show you a little bit around
the whole subject of testing for the
next 90 minutes I hope you find it
useful yeah we have got a question for
you
so who does know about the testability
framework put your hands up okay you
can't go home
next there was another question did you
ever build something and execute it on
the testability framework
well some left okay okay
so we've got an agenda to run through
so first of all we're going to cover why
I mean I'd say how often okay you built
a test you've done it but do you do it
frequently is it part of your daily
routine
no I think that's generally what happens
from what I've seen across the community
very few have got in so that it's
default behavior so we're going to talk
about why that's going to have to change
as our world evolves and that's my job
Luke's asked me to to come and make the
business case for it yeah and now we'll
elaborate some how to write it and and
maybe make advantage take advantage of
the fact that there are actually
available to us a big bunch of tests
so a developer's lot is not easy you
know we are at the sharp end of
customers businesses and if we get it
wrong the consequences are
catastrophic um how many of you have had
a situation where you've really been up
against it and some particular burg
unintended consequence
code that has gone into a live system
has got through the testing process and
has caused
damage I mean let's just call it what it
is it's damaged and you know at the end
of the day the functional people they
sit there and they say this shouldn't
happen and they look at you and they
expect you as the developer to fix it
you're the one that has to stay there
all evening all night and put this right
and you know they're asking you to build
designs to technical designs and they're
asking you to understand the
consequences of every last little change
and
I've been around the naff community for
20 odd years I remember when it was a
lot simpler than it is now I think as we
move towards a world where you know
there are more and more optional
components in terms of the extensions
that are getting piled into that core
system understanding the consequences of
something that you change is getting
more and more difficult and I refuse to
believe that any individual is going to
say yes that's safe to do and no that
isn't in in any quantifiable way
and I think the testing processes is
really our key to do that and I
left for a trip on on Saturday and on
Friday afternoon one of the junior
people in my organization came up to me
and said James can you just run me
through this code and you wrote it in
2003 and I don't really get it
do you remember you did hey I looked at
the code it was bad enough it was by K
you know I'd rewrite it in a heartbeat
now I mean that's something what we do
revolves on what we did is not what we
do going forward and and yet that code
lives on and actually in that client
that code is critical to every single
day of their operational process and
then ask for some changes and you had to
understand how it worked before you
could successfully design in the change
which is where it came but how many of
you have that I mean quite a lot in the
community are should we say have been
around for a while let's put it like
that rather than saying we're old but um
you know and we've got a lot of back
history and that back history is still
in use and when we came to again I'm old
enough to remember y2k and you know the
number of COBOL programs from the 60s
that came out and had to be updated for
that and I'm pretty much betting that a
lot of of cow code from the 90s is still
in daily use you know mark he goes on
about Microsoft not refactoring some of
their stuff quickly enough hey I don't
think it's just Microsoft that had that
thing that that problem so you know
we've got to we've got to be able to
evolve in a way that allows us to
support allows us to deploy updates in a
much more regular way and move on and
and do that reliably and
um you know hey you've had 24 hours here
I'm glad this wasn't the first session
it's one of the last ones because
if you get a feeling that
wow there's a lot of change going on our
whole kind of climate tenerife coming in
nothing is staying the same you're
seeing you know navvies not this little
closed environment you've got our
transactions flooding in from api's from
external systems that we have to be able
to successfully manage and test and
understand and
you know I again
the company I work for we did a load of
we do a load of CRM work as well and you
know just some of the authentication
Microsoft deployed some changes to CRM
online the beginning of this year and it
blew up some of the customer systems and
we had to react in minutes not days or
weeks and and couldn't plan what we did
so where we used to have nice set cycles
and be able to define the time line
sometimes now because of the the
multiplexing of different systems
talking to each other you're not in
control in the way that you were 10 to
15 years ago and and
there is one part of every project that
I'm involved in that seems to get
savaged squeezed call it what do you
like you know the client wants this
thing working as quickly as possible
but then they want to make the
discussion period the design process as
long as possible to get every last
detail out of it and the development
developments not a precise science we
can't deliver said amount of code that
you know are on complete deadlines and
and all of that means that often it's
the testing sequence and my customers
are hopeless at testing I tell them that
I'm not talking out of turn there but
you know it's the one thing they don't
really enjoy doing they don't have
confidence and it's diffic how do you
test all of the different permutations
how do you go through and do it
rigorously and comprehensively and when
you know it might only have been three
months since you did the last full cycle
because there's a there's a bug that
means you need to deploy another CEO etc
and so it is a difficult process we you
know a lot I think do a little bit of a
cop-out of responsibility by making the
client responsible for testing and
that's really saying well if it goes
wrong it's not my problem but it is it
will come back to you so it isn't an
excuse that that lasts for long
and yet we need perfection
and it you know reputation which we live
on as a community
we have to make this we have to get to a
situation where we can deliver quality
as often as possible right first time
you can't have a situation in a in a
digital world where you know with
e-commerce and all of the different
things that are going on
it will it will become a viral story if
you if you make a catastrophic mistake
and that information gets published not
just internally to the organization but
now increasingly externally so when Marc
builds all of his complex flows that
take data out of
navitor and spread it around the world
all that's going to do is make an error
that there hasn't been caught
very widely known and
so we have to get we have to step back
and look at this and say okay where we
had historically when I started it was
very much err more an agile environment
of sitting there whether a design
environment is saying right what do we
want to create
and we'd almost build it in an agile way
I think
that's perhaps not going to produce the
quality that that we need go forward we
have to design and we have to design for
testing from the start and I think
understanding how we are going to ensure
that this is quality it is difficult
and
it's surprising once you start that
process um you know the conversion from
being a skeptic about texting testing to
being an enthusiast I think he's a very
short period of time um
even as a as a consultant and a
developer the amount of time that I
spend actually writing code compared to
actually verifying that it's doing what
it should do I've spent far too many
years probably of my life trying to get
data to a situation where I can actually
run my tests successfully and you know
then I run it it fails I go back a
corrective failure and then I have to
rebuild another scenario and I'm putting
another sales order on or setting it
through the warehouse process again to
just do and it's just time consuming and
inevitably I end up building one small
test script one two small test scenario
and when that works I assume everything
works um because I'm up against that
deadline and it's not good so bringing
it back
bringing that back and saying at the
start how am I going to build the test
script which Luke will show I think is
much quicker and probably even in the
initial project from what I've seen
produces a faster output
so um
it certainly helped my design
because I'm thinking up front and
thinking not just how it should succeed
but what I'm catching errors more
because I'm designing them in from the
start I
getting verification so I'm going back
and it's not delivery it's not user
acceptance testing where the clients
saying are but you've forgotten x y&z
we're actually doing that start
permutations you know what I just said
of a single script run-through is it is
because it is successful
no way it's very easy then just to go
okay copy that test creative variation
and a variation in a variation and and
that takes seconds longer
and just keep doing it and keep running
it and keep running it and you know the
stress that that takes out of the cycle
to know whether I've actually finished
this
backlog item or not or whether actually
I've done it it's going to go to testing
and it's going to come back in two days
later
as a failure I deal with it it's right
first time I move on I build on top of
that and and you build a library you
know and and this is the daunting a
thing I think for a lot is that when you
first approach this it is ah where do we
start and get started build the first
few simple ones build your library up
you know those of you I just sat through
Waldo's vs code presentation snippets
you snippets for tests
there's gonna be a snippet library for
testing routines that you know set up a
whole bunch of stuff and and that's
going to be really easy and I think
that's really going to change our game
in conjunction with this you know it's
not explicit invent here but who's doing
full documentation
yeah how do you know one year later what
the what your coat was meant to do write
your test code it tells you what it does
yeah and I can think of examples where
exactly that already in my testing
experience you know just run through
what the steps are to test which was
exactly that question I had last Friday
is how do i how do I make this work so
I think a test has lots and lots of
value to you primarily to you
but also to your organization
and
you know your your the people you work
for um they want certainty
it's often said businesses you know that
business hates kind of
what we do because it's not definitive
it doesn't take so long to do something
they they can't predict the outcome and
this makes it much more certain you
build a test script you run the test
script pass or fail it's not an opinion
it's it's definitive and they will enjoy
saying to the customer this has passed
this is not passed rather than we think
it's finished
your colleagues in the functional side
will not enjoy the testing process
nobody enjoys sitting there for a day
running through hitting a failure trying
to work their way around it to find the
next failure or sending it back and
having it back a few days later and
it's so much quicker you know Luke will
show you a situation where for his
organization they run all of the tests
every night you know so it's kind of you
know where you are in a much more prompt
programmatic way and and that
enables more complex more repeatable
more
verifiable
confidence
in where you actually are in the whole
development cycle than just somebody
saying well I think we're 70% through
and and where have you got that from
well often it's more a hope
than a than a reality um and I think you
know
some of the some of the most painful
times that the final slide who enjoys
bug chasing
yeah it's not really what we live for do
you enjoy getting you know starting a
design building something new building a
new structure and you really want to do
it right first time and I think the
whole testing our automated testing
process gives you the opportunity to do
that much much more of the time it's
clearly not going to remove every
possible bug but it is going to mean
that you're not going to stumble over
the same one again and again and again
and that really is worth its weight in
gold
so um
let's forget that the business side
let's start actually seeing some of the
technology show do you think you you
blow their head or not that I can
continue to show you how to do it I
think you should yeah
let's give it a try
so
let's have a look on how to ride it and
it's I'm not going to say it's rocket
science but
it's just a state of mind and having
been a developer myself for years and
then came into the role of a tester I
learn to look differently and by the way
don't know who reckons yourself as being
a tester in one way or the other okay
and I think the pride of a tester is go
and break the software yeah to show that
it's Wow hopefully doing what did you do
but in all aspects you try to find out
this is where oh yeah this is a hole
where I can put my finger in and see oh
yes that it falls apart and
that's actually what testing is about in
a short sentence so for developers
and sorry to say so but I tend to be
blunt in that those kind of things too
straightforward enough developers are
not the best testers developers in
general to test their own code is not
the best to do but to be honest to
myself when I started as a tester I had
to admit yes as a developer you're what
are you doing you're testing the sunny
path that's what you want to know you
put a in and get B out but did you check
the other options and actually all the
other options that's the main part of
testing I mean yeah it does work but
when it's not working as they say dusta
does the application die gracefully does
it really go into a nice message does it
have another option or does it crash
well the last one we almost never get
that done on on an IV but if you're used
to developing things from scratch you
probably have been in that situation oh
yeah now I did a Google gang go on yeah
so testing is about showing everything
actually and then still you don't have
the possibility to show everything
that's here yep but our B on my keyboard
too so
yes no
it's on my machine
it's moving on the other it doesn't
switch so I have to go back to the other
machine
it's plugged into
this is the clicker is only working on
one machine not on the second one but
okay yeah it works
short how to write test automated test
is where to start a short
review or a view on the testability
framework and then I want to talk about
test design
when do you doubt them when are you
going to ultimate your test each time or
run them they was too fast each time
code is going to be changed that's
ideally what you want to do and that's
what we hopefully in general do we
change our code and it's going to be
tested hopefully to be honest I'm doing
a lot of development and more than
testing lately
again to code and I yeah this is what I
want to achieve and then I start
changing and I say and we have a rule
that we will refactor let's say the Boy
Scout rule you get into the code it
should be nicer after you leave it and
then all of a sudden I find myself
having fun and I think oh no this has 20
lines too much this is not going to be
tested change it back but you want to
only change your code when it's going to
be tested are you going to get that done
with let's say traditional manual
testing not sure but if you have tested
a test already automated you can run it
every time again like James already said
what a couple of situations where you
could start because that's probably
questing for many we have this big
solution and where are we going to start
automate our test which we haven't done
so far a couple of things are is a
simple one is when you have to fix bugs
it's a confined scope and probably the
number of tests are then also not that
big so that's a place to start another
one could be bigger if you're going to
change a critical feature
yeah testing is very important to show
that that this thing is going to be
delivered and that the people are going
to work with it can trust on upon it
that it will work fine so
testing will be more
in tents there normal probably with
other kind of features and often you
could say with business-critical ones it
might be a complex one so the iteration
of testing and and then fixing the box
etc is probably somewhat longer than
normal so every time again setting up
your data costs a lot of time and if you
have set up the test yeah that costs the
time some time to do it the first time
but then rerunning it you will profit
from it or developing a complex feature
how many of you are doing code
refactoring as a let's say
regular thing in your processes yeah
okay and maybe I you could almost say
from a distance I don't see any hands
means that most of you don't and why you
don't I'm just guessing but probably the
reason is you need to test it and are
you sure you're going to test everything
if you have ideally the scripts already
in place to test that test everything
ideally it would mean you can go against
your test refactor the code and it runs
again and it shows that it's doing what
it should do of course there's an
assumption if the coverage is not big
enough there are holes and you might
refactor something which doesn't show
because you don't have a test for it so
you have to be your this is an ideal way
of looking at it let's put it that way
so
in the end
talking about data setup which takes a
lot of time but also the number of tests
you would like to execute it's about
repeatability and speed yeah so if you
have a big solution where a lot of
things have been done and ideally you
will have a great coverage with
automated tests well
count your blessings
Wow well
now it's moving on both side that's
interest if you wanna have a look at my
site feel free to come here but I'm
going to switch to my computer because I
need you in a couple of minutes anyway
so yeah
the basis to be able to automate the
test within
enough
within let's say see Al Gore with
Sialkot is the testability framework
some of you are quite a big part have
heard of it I've looked at it short in
history the time I was working at
Microsoft our work as testers was mainly
manual the core team w1 I was building a
platform or a framework called an TF no
vision test framework which was a need
to
export of the objects in text format and
based on the text format they built
c-sharp classes and then you could code
against those classes you could say
however and that's a specific
perspective we all have or mainly have
is its UI testing it was UI testing it
was programming against the pages
programming against the the request page
whatever and that is time consuming UI
testing is time consuming thing so
Microsoft being in the situation of
multiple builds because of countries
at that time 45 around about now it's
about 20 they they couldn't cope with
the fact that that took six hours they
had nightly builds but then built
infrastructure and be able even to say
okay the build was not ok let's run it
again we want to see what the result you
had to wait six hours yeah so they
started to actually already in the mind
scratch this whole thing which had cost
billions already millions a suit a we
had a team in China doing programming
for us and it was all at a certain point
I'm scratched before they did they
already had decided to introduce the
testability framework into the platform
and it was released in the product on
2009 service pack 1 who has been
programming automated tests since 2009
on 2009 service pack 1 so AG has already
automated test yeah we miss the chance a
couple of you did great I miss a chance
to I'm part of the the big part in the
big group we miss the chance we didn't
start programming and we could have
because the testability framework hasn't
changed much the only couple of things
that have added and the main one is a
test page but the rest is the same as it
was already so and this is approximately
10 times faster
when they started they had about let's
say couple of thousand tests and it and
now they have 20,000 tests and it runs
much faster than they ever had at that
time or the possibility they had at that
time so
hatless testing and I'm not saying
that's the only thing but that was let's
say key to speeding up the whole thing
the purpose is just to make the scope
clear this tool or this framework is
meant to do aapko testing it's only
showing that the app code is that's the
purpose from Microsoft perspective to
show that the app code is doing what it
used to do yet to prove it's still doing
what it used to do it's not meant for
load testing some of you I know have
tried to put it in their centralized
developers database well you run it and
everybody gets locked some way or the
other yeah I even know I've even heard I
haven't done it myself that it locked
somehow the object table so it's meant
to run in an isolated mode in our
isolated has multiple meanings here but
in this case you have to have a separate
database put it in there and that's
where you run it yeah I'll get back to
isolation what matters in the end and
that relates to this isolation also you
only need to know what a test was a
collection of tests successful or not
the rest is of no importance yes if
you're developing started to set it up
you want to know oh yeah this GL ently
or whatever it looks good and I'm can do
my verification programming against it
but in the end I'm not interested in the
data yeah I'll get back to that and you
shouldn't be interested in the data
because it should work for any data you
cannot control what data is gonna be in
there in 12 months two years three years
time don't and on Oliva would say you
run it every time on the same basis yeah
so don't have a changes at all but yes
in a way you're right in a way you're
right you're right
before you run away
well
testability framework for dummies with
all respect a couple of things just to
to maybe refresh for you for others to
to introduce we have the concept since
this introduction of what is called test
code units and
a small example here is this okay have a
quote unit and I hope is readable enough
I thought I had a better resolution but
let's put it like this
since 2009 Service Pack 1 we have this
property on a code unit called subtype
yeah and they introduced
normal that's what we have if we created
normal code unit for a process or
whatever and introduced the two options
test and test Runner the fourth one
upgrade has been introduced in what was
it 2015 to when we got the upgrade code
units so well it was apparently a
generic enough to be reused for
something new but any code unit where we
will write our test input our testing
needs to be of the subtype test and I'll
show you what that means
let me create and I'm this is the only
code I will
write just like this I'm going to create
a test function my first test function
have a look and well since 2015 that we
have the tax in view it shows me that
this function gets attacked test and by
the way you will see in a later slide
Microsoft or the enough team didn't come
up with new terminology this terminology
is actually based on X unit test
patterns I don't know if you know about
that
a guy who wrote a book on that and there
is a plug-ins for c-sharp to help and if
you write c-sharp code Tesco functions
you have also this stack in front of it
and what does it really entail well I'm
a
big fan of minimalism and this is my
coat I don't need to have more so this
is doing something my function is going
to create a return a message let's save
it and we're going to run this one
I think the client is already open it's
not oh no this was the artist a 2009 so
I get this message my first function
hope is readable enough for you my first
function is written on it yes if I click
OK I get this one and this is something
specific to a test code unit meaning a
test code unit as a result yeah it will
give you a result and you're able to
collect that next to that it will I have
one function it's successful and due to
that the whole code unit is successful
if I have multiple functions I'll show
you later and one fails then the whole
code unit fails we don't have a
successful total successful run the
thing is
what do we do if we run a normal code
unit we activate the on run trigger
that's executed with the test code unit
it runs the on run trigger and it rolls
every function that is of type test yeah
so and by the way this is a
transactional process so if I would have
created some customer record it's in the
database and I will mention it more than
once this today never run this in a
production environment in our case we'll
use TFS for our source and we have
different branches for test or for
development test acceptance and and
production but it's deleted from the
production branch to prevent any
possibility that the code could end up
in production if you want to help your
customer and they want to have a good
feel we're getting into the last part of
the year for money yeah just run those
Scout units and they get a great revenue
at the end of the year but probably they
get a lot of things sent back also or
not paid for even worse of course so
this is one example and this one I
prepared already I created a second
function it's a well it looks a bit like
the other one but it's somewhat
different it's creating an error and
what means an error an error means
failure yeah any error that appears
through an error a call or a test field
call or
insert on a duplicate key or with a good
duplicate key value you get an error so
if we run this one
you won't be very much surprised I get
this message and this is my result yeah
so I have a failure and it gives me the
error message by the way did you notice
we got the message it displayed but it
isn't is display the error yeah so the
platform let's say a bit like with web
services the platform is handling an
error as something as a result or
something to be returned in a web
service to be handed off to the
consuming application
one step further and is this one hey and
typically an error if an error is
expected to happen and that's what I
said good testers will test that part
surely what happens if I do something do
I get an error is this the error that we
expect does it air or on the right
instance so they introduced that's the
second one on my slide but I'll leave it
for later a new keyword called a third
error which means it is expecting an
error and it means that then the test
will be successful
so have a look
so it's successful and
probably if you have a sinner scenario
where it's a unit test or a functional
kind of test the biggest part of your
test will be handling this side yeah
seeing if that's that's
dying gracefully
so second to my part was here to tell
about you sir their
third part is UI handlers
tests or the main part of your test to
profit of the speed and in general main
part what you would like to test is the
processes are they working well you're
going to create a
vendor you're going to purchase
something from that vendor and you need
to you get it receipt received and then
you're going to post the whole thing
financially also and
there will be this
string menu thing with the document or a
confirm with the journal asking you do
you want to post yes or no yeah well if
I would run it like this and I would run
all my coche units like this more or
less and I push and I go out get in my
car go home and I get back to Mora and I
thought 3000 tests has run but then was
still waiting for me to tell yes or no
so I need to be program eclis able to
tell the system yes I want you to post
this so we need something to handle this
UI I have a small example based on the
test because my test which we had been
running now
let's take the first one only and then
message is it's not a big one but as you
can see it's waiting for it to be pushed
and now it gives me the result so I need
something to handle that and that's what
they call a UI handler
this example
so I need to create a function which
will handle the UI and meaning with the
message is very simple I just need to
create a function and it has attack
message handle as you can see just
saying hey I'm the one who's going to
handle this message and with the message
there's no option it's just pressing
okay that's what it's mimicked yeah if
you have a confirm I'll show you one
later it means you need to return yes a
true or false yeah no action
different than that but in this case
this message handle I need to create it
by default or actually it's not done by
the system unfortunately but the
signature of the message of a text
thousand twenty four I need to add as a
programmer and then I need to tell where
are you going to be called or by what
are you going to be called so
here and
probably that's one of the advantages
with going to PS code if you have a look
here at the properties of this function
this one here I want to zoom in yep we
have a property called handler functions
here is where we're going to point to
the handler that needs to be called when
this message is going to be
happening appearing so here I'm going to
and I hate this very much slide this key
group property we had on keys you have
no link to the key groups you have to go
somewhere to that window of key groups
and see oh yeah copy paste and maybe we
were too darn stubborn and you wanted to
type it yourself and then there's no
lookup for it however you can add
multiple ones so a process could have to
confirm and a message later or even that
said there are handlers for pages there
are handlers for reports
so that's at this one
yeah
and
have a look so I'm going to run it oh no
here you see the message is not showing
anymore and that's what we want
the process is handled and it's
automated what the user is going to do
in this case no option is just clicking
okay it's just information and that's it
yeah so
that's the third part of the
testability framework and the last part
well there's a fifth part a test page
maybe we'll get into that later is the
test runner what I said if you run a
test code unit it's a transaction it
will create data yeah and okay depending
on what you want to test you need to
create to create data to check ledger
entries or whatever
but in the end you don't want that data
to
be still there in the system when you
end or more specifically if you run a
test maybe an individual one maybe a
group of tests great we have a result
and the next group comes up an Xcode
unit you want to start afresh at the
same level as the other test is so your
base should be the same so you want a
process calling the code units and
enabling the fact that this is isolated
yes it's creating data and yes great
with sequel server you can read
uncommitted data so you can check in the
background using sequel queries what is
happening but in the end
it's superfluous go on again yeah this
test runner and that's the the third
option on a code unit in the standard in
Cronus there is always this code unit
there's a couple of things here but this
is the test runner
you don't need to create it you can use
it from the application it's going to
call all the test code units within a
a suite of test code units and the fact
that this test Runner is a test runner
enables you to set the isolation test
isolation mode here I have a slide later
with the details we can skip that while
we move on but this means it has the
option now was the value set code unit
every code unit is executed and after
the code unit has been executed the
things will be rolled back automatically
yeah in the first version of the test
tool set of Microsoft they had a big
library backing up the database before
the test ran and then they ran the tests
and restoring an audience using the
database sorry and then at the end
restoring the backup took a lot of time
was a neat solution by the way but this
is even better within the platform it's
a platform that knows are you already
back
even if you commit data you if you write
in your test a commit it's in this
isolated mode and at the end that's also
rollback but the committee is a
committee so within the test a
transaction if you would have an error
in the test it rolls back to the commit
but if you stop this code unit it rolls
back everything
to for completeness you can disable it
that's the default one
be careful that means if you have a test
run with this value disabled that it
runs and it really commits everything
you could even set it to function that
with every test function your data
creation is let's say your take the
update and the database is going to be
rollback that's short on the test Runner
I think that's enough for now
so this is the slide on the isolation
I'll move through it fast for now
looking at time maybe I get back so in
short this is the testability framework
are you with me yeah it's not too
difficult I said it's not rocket science
but it's good to know about it and yes
once again only few of you but this has
been therefore he is already eight years
yeah and then they tell me when I do a
workshop attesting look this is a lot of
times a lot of time investment yes you
should have started eight years ago
but then I didn't have a workshop yet
sorry a
lot of things I told you but in the end
please bear with me this is the most
important part really this is the most
important part and it's not simple I'm
sorry it's not complex
but this is something
which I think a structured organization
or a structured team or a structured
tester or
is
discriminating themselves from others
some general things first of all
architecture part some some rough things
we talk about functional tests we talk
about unit tests the down thing with nuf
and with our code and also with
Microsoft code is improving luckily is
that it's a hard thing to do unit
testing why we have the hat while 2017
changed but we had four years this coat
unit eighty and nineteen twelve hundred
lines of code in this unrelated grade
level we added some more 1250 over 1300
lines how in the hell are you going to
test specifically that that part that
you added is going to work you can but
then you have to build up a whole
scenario to get something done yeah and
yes like James said then you ran it and
then I'll go that's not what I expected
I need to get my data again created so
both for both you can use this
testability framework to do more a kind
of Spanish functional scenario but also
unit testing it's it's quite simple it's
your choice to do I think as a developer
the last one is the thing you do because
you don't know anything about the
functionality
bit accelerate but often it's too
complex to build it up but if you test
the units and make sure that you know
these are doing well then the overall
thing maybe not automated but maybe
manually shows yes that all together
from functions fine
but also looking will have a look at the
the Microsoft framework that's where
they came from they have been building
up now about twenty thousand tests and
it's mostly functional or scenario
related or oriented this is all to do
partly with the fact that we have the
code like that and the fact that yes
starting from scratch having no unit
test in this
application to start writing to unit
test where the hell are you going to
start so
enough and structured programming hasn't
been let's say
a very inspirational inspiring marriage
from the start yes we're getting there
and and so test design is also about
code design app code design yeah and
hatless versus UI testing we all come
from UI testing you see that the at this
client windows web whatever and you type
in your data I don't care if it comes
from the UI or not to test posting
routine yes I might write a test that
I'm sure that if I click post that is
their one and that it does something
that could be a useful test to check
that you have to posting on or whatever
action on the screen but what's behind I
don't care I care I will test it but not
related to the bottom button and then
the positive negative things so you you
will be writing a lot of codes using
that a third error because you want to
see if an error is flow are you allowed
to post without the posting date
hopefully not etc etc and
and this is a funny one
and I think but that's if I would ask
you do you remember how you learn to
develop
could you replay that film that movie do
you remember how you learn to develop
enough
probably not if you sit down and
are working on testing it starts to itch
I've been a drummer I played at a quite
a level and four years and then I wanted
to try and learn piano play that's
frustrating if you'll be playing a lot
and you were easy doing things and then
all of sudden you're sitting at this
piano and it's not reacting the way you
used to that's a bit where we're at with
this
why do I say it in this thing your test
should be data agnostic app test I'm not
talking about configuration tests or
whatever they should be data agnostic
often if I talk about this they say yeah
but we have our customer and they have
specific data I don't care you test
create them yeah so running tests we run
tests on Cronus we need a database and
it's not fully clear but unfortunately
Microsoft test depends some places on
the on the Cronus data but your test
should create the data
we'll talk shortly on that later the
terminology on patterns
Microsoft started with this xunit
pattern thing and they started with
creating test case based on a four phase
setting or pattern I'll show an example
later nowadays they use acceptance
test-driven development our sister teams
are using it and you know in c-sharp
there's a plug-in Gorge
you sit down and you write your tests
like I want to do this and when I have
this then I'll do this and then I expect
this and it creates your test code we
don't have it yet but with fears code I
think exactly yeah less even a lesser
reason not to start testing or automate
testing the test best patterns taken
from the xunit pattern test pattern are
built fix your lazy fixture and fresh
fixture and we'll get into the patterns
so
make sense so far
the four-face testing I don't know if
you have been looking into the test code
unit from the standard but you will see
every test has a structure and this is
the structure they started with
initially and they've done that for a
lot of tests which is this for phase
testing being there is a setup part
setting up your data for your test then
there is a part where you act do the
action exercise this is this is what you
want to test this is what you're going
to do you're going to post or in this
case it's going to create a contact
based on a or offender based on a
contact and then you're going to verify
and
each test needs a verification even if
you get a error message like there or no
error message it looks like it's filled
or not only still verify why you never
know whether the message underneath is a
message Microsoft is going to change
over yourself you're going to change or
functionality is all of a sudden adding
another error which you haven't expected
it's it's popping up before your error
yes it's an error it's just checking we
have an arrow and that's what we
expected great successful yeah but is it
the same error each test needs
verification
can you repeat each
needs a verification yeah don't forget
and in this
pattern there's a part which is called
teardown
most of the time we don't need to
platform takes care for some things and
a lot of tests can be written in a way
that you don't need a teardown but
sometimes you need to clean up some
things but yeah look you know this
everybody in this community has done
some manual testing mm-hmm and they've
done all three of those steps yeah it's
just the same thing you're just doing it
via script revver than doing it very
manual process true but of course and
it's true but we're depending a lot of
implicit ly depending on data for
example so they say I need this customer
database and it's fair reason it takes
me less time to set up the system to be
able to do the test yeah and yes that's
true and that's what we'll be doing a
lot but
we're going to another environment with
comparable functionality or whatever are
you sure the setup is right if your test
has the the setup already programmed in
it you can pick it up and go anywhere
else yeah so yes we know it but some of
these part are implicit are you really
aware with the verification what you are
verifying yeah so yes program is like
telling yeah it's telling a computer
exactly what are you doing as an expert
it's just taking the assumptions out of
it because I've had you know I've had
loads of
testing come back to me saying this is
failed and I've gone no it hasn't you
just haven't set that data right yeah
before all redefining what is required
properly up front once using it
repeatedly true yeah
this slide is more important for the
structure this is what Microsoft picked
up nowadays and this is the the ATD
pattern given and you give a description
there so like I dropped stepped into
part of your
presentation that I said it's a
documentation at the same time yeah so
you're documenting what you are doing
giving something this is the setup
you're going to do something the one and
when that has happened you're going to
check then this is what I'm going to
expect and if the Squatch plugin would
be available for us on vs code later Wow
when you can sit down oh you can even
ask your functional colleagues or your
consults or or maybe even your customer
to write down those scenarios like that
yeah
okay test data have to look at the time
it's what I call text test fixture or
fixture it's a setup this is the setup
you're going to use to be able to
execute this test and to be able to get
the result
whether as a failure expected or not
three terms to be introduced here a
prebuilt fixture you could say that's
what Cronus's and at Microsoft with that
test are depending partly on that you
could set up a database which has
already a part of a set up realize that
it's there and if you pick your tests
and go to another database you might
have another set up and then the test
could fail because something is missing
there yeah so this is a one I would like
to prevent using and sometimes yes in
the case running Microsoft static test I
cannot prevent this but ideally I would
have a database with no data in it
another stage is with for a group of
tests you do what they call the shared
fixture or a lazy setup Wow we're all
programmers I think this links to our
way of life you want to be lazy you're
going to you if something happens and
you know you're going to do it 10 times
again you're going to program it of
course so this lazy setup is as you can
see there's an initialize function you
will see in many of the standards
initialize function be called at the
start of a code test function which does
something general master data set up
data in
supplemental data something like maybe
setting up several equations and then
you have specific ones this test needs
in this case there's a company contact
created specifically for this test this
company contact is created it should not
be in the general set up it's just
specifically now that's a fresh set up
so we're starting a test and this is
something fresh created just to under
stress this or is that Crona thing is
what I like to prevent as much as
possible yes I'm relying on it with the
standard ones but for my own test I'm
not going to use it but then with this
story even more important inside this is
do you have a plan do you have a plan
what you're going to test you need a
test plan
who's creating a test plant in their
projects
and it depends on and I'm using the
terminology a bit roughly for me as a
test plan yeah I've been a tester and
it's a bit more high-level than I will
use here for me
for you as developers as test plan is
I've got this part I've got this part
and I'm going to I need to test this I
need to test this and even though it's
just a short description of two words or
three words it's more important that you
identify what you're going to test then
that you detail out what you're going to
test yeah so
and
so and do this up front don't wait till
the code is ready yes coke ready might
add something to it but the world should
be changed I think we should be working
the other way around we have tests
defined and we're going to program
against the tests and if we don't have a
test we're not going to program it
meaning we deliver what is being asked
and we're not going to believe deliver
those
integrated
unexpected hidden features yeah now
we're going to test what we have coded
or the other way around what I said
we're going to coat what we're going to
test and the other point I'd add that is
the structure of what you design will be
better if you design the test alongside
it yeah every time
it will be more flexible because you
will think through the permutations of
how you might use this in a way that you
wouldn't have done if you just
considered the straight requirement true
and it gives you a medium to review the
things that's going to be tested and be
hearing I call it yeah you could say and
that's where the use case comes from
your use case list is your test list
your use case this determines what
you're going to program
and the false negatives come in there as
well so so in effect you can put you
know this should not work is a valid
test yeah so say
you can restrict what you're building to
just what you're supposed to build and
and the unintended consequence of it
being used for something else later you
specifically get prohibited and that's
useful totally right to to limit scope
and that's part of I think it's a many
levels enough where we try to get to
practice minimalism keep it to what you
ask keep it what you're going to test
not much more in the workshop I did on
Wednesday I use this list I will show a
couple of examples based on an
application that that has been used and
I still use in solution development
training it's the seminar registration
application and this is the list I made
up some of it I did implement for the
for the workshop and today some not yet
so I also have overview where am i what
do I still need to do or do we still
need to do and what are we going to do
by priority what are maybe not well
readable but let's say the light red
wants non UI and UI I make a difference
between where do I need the UI to test
to be tested and we're not
some examples
short ones and a short introduction
first no not this one here for those
who've been in my training in the last
couple of years they have been building
this and maybe they now think oh no not
again Luke but it's a simple example
it's a standard environment or
application which has
master data being a seminar which has a
document kind of thing be a seminar
registration which has a
journal thing which has posted documents
well I'm not going to
discuss all the tests I don't have all
the tests yes and in place by the way
but I'm going to test a couple of things
and I know already this code was there
so this is a comparable situation to
what we're mostly all are in it's not
something now newly developed I have
already code which I want to write my
test against
is this this is the right one so my
first example and let's pick the slide
first this
picks from this list and
when I delete a seminar that's like when
you delete a customer and you go in this
only trigger you will see a bunch of
related data being deleted - or maybe
not there's a check if there's data
you're not allowed to delete but this
seminar can have comments and if I
delete the seminar the comments should
also be deleted enough doesn't as a
platform make that done automatically
that you don't have orphans because of
the parent is being deleted we have to
program that so that's something you
need to check by
by testing and typically if I want to
get my developers frustrated this is
typically what I test well test more if
I would test but these are things we
often forget as developers
deleting the seminar comments
in this example so in short what would
that code look like
I'm here where did I put it
and this is an example where our world
is changing because you talked about the
on delete trigger but with events you
know do I go and check the event
subscriptions to see what what kept in
there yeah so actually you know it can
very quickly change to a situation where
something is not running from from
running through no code that I've added
or can even see
let's have a look at the code here I'm
not going to program in here as you can
see I've created a function called is
initialized that's for my lazy set up it
in this case it's not doing a lot it's
calling a standard function I created
for my whole test application and this
case creates a seminar set up by the way
for this test I need to have a set up to
be able to create a seminar
but sometimes this is initialized is a
bit
obsolete because some tests don't need
it but that's the lazy part of it and
know that it will be there so
this this pattern here with this is
initialized make sure if I call it
multiple times in this code unit I don't
need to
set it up again in short what do I need
well
apart from the black coat the green one
tells me what is to happening I need to
create a seminar with comments yeah
that's the given and then the one is I
delete the seminar that's the action or
the exercise and then I'm going to
verify as the verification function also
describes verified command lines do not
exist for seminar yeah which means yet
they're gone I don't have them anymore
so basically it's documented what am i
testing step by step and I can
hopefully read from the code also a
coach you document itself what is doing
but it's clear this is what I do and
this structure and that's what I've
again saw at the workshop a lot being
programs sit down and the only thing
they mind about is the code not the
documentation and then they ask me Luke
can you help me I don't see exactly what
is happening anymore yeah so I sat down
on my knees please use this this pattern
because it helps you and I stood up and
I said what's something else but so this
structure it's not rocket science but it
will help you to be consistent every
time again and yes like I said this Dan
part should be there verify the fact
that you could delete it doesn't tell
you that it that it really deleted the
whole thing and while you're building
this you will be building up functions
which you could be able to reuse again
this code unit I brought down to this 1x
test for today but our more in it and
they were all using this kind of
test functions
time looking at a time
speed up a little bit another example
let's pick the slide first this is
another one when I delete a seminar
registration this document it's only
allowed it has a status like we have
with purchase or sales document status
which is released or open yeah or maybe
other states but this one has a couple
of states and it's only allowed to
delete it when you ask the state it
cancelled which means if it's not
cancelled it will throw an error how
we're going to take care of that error
well of course if the error comes around
and you put an assert error in front of
it it will not show as an error and will
say successful but be sure to check this
error so you need to verify in the end
that and that's this part here verify
seminar registration deletion status
error that this message itself is
exactly the message that you expected
yes this might feel for many of you I
don't know should not sure I'm just
assuming like ah you need to program
everything yes that's what you do daily
you need to program everything so it's
not only an app code or not only in test
code is also an app code so you need to
put the do not send the balls to get it
so the whole thing sticks together
so and and I don't know previous one
where I was fast but Marcus off had
build up a shut up I turned you off I
thought
spamming yeah to enough out then of
quiet I was turned on that order sorry
Microsoft has a couple of libraries
about fifty and one of them is called
the assert why we always sue it if you
have a look here there are numbers of
functions a couple of them local and
they all are used to do the verification
to see if something true
condition or whatever to compare
messages against each other or values in
general the advantage of using this is
that always when you get an error it has
the same format so every time again you
know okay this is the expected value
this is the actual one and you can add
some extra message like what I do is it
shows me this is regarding this field on
this table that I know what it's really
the contacts is yeah so
made use of this it's available the
assert library is part of the
application so it's in standard Kronus
and
don't go and I would say don't go and
define your own use what is already
there this terminal terminology by the
way is also from the X unit patterns
test pattern so if you get a tester in
your company which has been using X unit
test patterns based on c-sharp and they
get in and they see this day they're at
home they know oh yeah that's the way I
did it and that's the way we're going to
do it
last example on this one is a confirm
handler if I change the seminar price on
the header on this document there's a
set channel price it's inherited on the
lines and if I change this on the header
it's like dimensions you get the message
do you want to update the lines yeah
short one here
so I have two scenarios change seminar
price on seminar registration with
register lines so they need to be
updated and
or actually this shouldn't be updated
and the unregistered lines and as you
can see I created two a one function
which I can reuse an act so DIF that the
test itself is actually in that function
as you can see we have a structure again
given when then you start to feel at
home I guess somewhat slowly yes this is
this is recognizable you know okay
there's something wrong in the data
initialization I need to be looking at
some part here
I'm going not going too much in the
details here but
about the confirm handler here I
the function is like a message handler
but this is a confirm Handler and the
difference is you get a text but it
needs to reply it needs to mimic was it
yes or no yeah so reply is set to true
and I'm checking already the message is
this actually the confirm I'm expecting
because it could be another question
yeah
alright so
[Music]
well ensure in a fast pace through how
you can create test cases
but then
mentioned already Microsoft has this
test tool set it delivers it with every
release every cumulative update since
2016 they once release it with 2013 as
is I never updated it
but since 2016 they want of course
pushing us more in a frequent update and
getting us potentially into the cloud
you need to have this tool set to be
able to test against the standard also
what it's doing still if it's still
doing what it should be doing and the
previous was a bit like I learned you to
work and this is about like little thump
walking with this seven-mile boots
or another way if you have a look at
2016 it has plus 16,000 test 2017
already plus 90,000 to be honest I don't
know the numbers for 2018 but it will be
much more and of course it grows because
of new functionality but it grows also
because they are filling up holes but
also anything they build that new they
can't submit it to the product without
submitting their consequent test for
troops yeah so and those get published
so anything that's new in 2018 one of
the best ways of finding it is run the
test yep right but let's do a small
calculation
imagine you had to write this amount of
test and depending on your situation you
have a big or a small
a dome
solution how are you going to cover that
if you would take this context of this
plus 15,000 test so let's say assume you
have 10 minutes protest to write and
meaning 6 per hour
this takes you 3,000 hours which is 2
plus years and like James said thinking
of his boat sailing out once a year at
least probably more you would think when
do I have a break to go sailing well
sleep things like that are the important
things yeah yeah more important thing of
course and there was the reason in our
company that we decided well we have we
have an application which is what so we
were imagining that we were going to do
and use this if you would spend three
years to gather coverage a good coverage
we said if we could get it working in a
couple of weeks let's try it and see it
took us six six weeks to get it working
up to approximately 90% meaning that
given our installation 2016 still we
have a fair customization and by the way
I need to mention that the Learning
Network we're in a development team
inside our company so we're an end-user
we're another creating an add-on world
for multiple uses this is a one-off
thing and
while it's it's a fairly
sized customizations not small it's not
a huge one but it's invading into
financials it's invading into the sales
and purchase etcetera so for us and for
money of our your customers other
companies this is a very essential part
of the application they're using so if
you're customizing that with or without
events or extensions it doesn't matter
if you're adding fields with or without
extensions to a standard table something
changes in the Senate whatever yeah so
how are you going to do that so we
decided to run it on our application and
for some the figures might be familiar
from from webinars but Jess as a as a
rephrase or repeat we ran it and 23% of
the tests were successful I said at
Microsoft and Athol myself that's not
big they said well that's not too bad
so I could have stopped after that but I
didn't so we did analysis using Excel
seeing what are the most occurring
errors and we're going to solve that one
within a couple of days less than a week
we rose the success rate to the plus 70%
and another week added we were almost at
80%
let's say that's the two first weeks and
then all together to get well the 8020
rule the 20% is the the hardest to do so
we spend all together six weeks on it
and we are now at 90% so we have a test
call retro of 14,000 tests yeah this
calculation dude we didn't need to build
it it's already there we didn't need to
spend three years to do that
so we have this running every night and
just for you as a recap this is what we
did run the to it if your code and you
have the tool on that version available
you can put it on Cronus and you can run
it and the thing with the tool is any
error is caught as a failure and it
continues with the next so just run it
yeah and then fix that minimalistic if
it fixed and it makes the test succeed
with one line instead of the free or
whatever you think it's enough yeah so a
statistical approach was taken for that
and
this allows us now we have 1700 left
to focus on the relevant areas and
partly is like where is it failing it's
failing partly in a warehouse and
manufacturing and we're not using that
so we don't need really to have a look
at that if you want to have a look at
how I did it step by step you can go to
my block I did give a detailed
description on that and in the end
what we found out is it's mainly about
data
there was nice one of the webinars you
were on at the end you said outlook so
it's all about data yes it's all about
data it's the setup of the Anita and yes
we found some application blocks and yes
we found from some box in the test but
that's less than a percent percentage of
what we fixed so I said well ninety
percent it's probably more than ninety
percent
where did we fix it well this was two
errors at the start which occurred to
most the first one was third three
thousand five hundred times the second
one was almost five thousand times and
this is
general setup data this is this this
lazy fixture so I created this
initialized function and I called it
from so I from the coach unit and
this is what they call lazy fix you well
not that lazy I had to change 480 code
units yeah if Microsoft had programmed
that from the start stop there which I
could use to do that then at work would
have been faster but okay there's an e 2
and C C sharp or Visual Studio where you
could do a finally replace for multiple
lines so I looked for a couple of
patterns and I was finished in half an
hour but then still I have 480 code
units change of which only 100 are
really having other changes yeah
the another one is this example you
cannot create this type of document went
vendor whatever number is blocked with
typo it occurred at a certain time for
thousand times why well if our
customization is if we create a forecast
an offender it's blocked by default
you're not able to use the vendor before
somebody has
authorized it to be used so what did I
do I changed some parts in the code
where as you can see I set an attribute
on offender by when creating offender
and I turned off the block yeah and then
boom those tests were running
that's what I call a fresh set up and
this is a more detailed level and so I
had to do it at more places than
the general initialize what they will
bring us this is let's say in a graph
per coat unit the
success rate which is a way of looking
because some code units only have one
function and they were successful or not
and as on dispersed and not success but
it gives some insight and this is where
we're at at the moment after six weeks
yeah
so what did we gain we have a user test
collateral and yes it's now also partly
testing our code but mainly the standard
in
collaboration with with our code
so and it's covering the main major and
essential part of the application GL
sales purchase and
it's being run every night and like you
said James yes it's happening while
we're sleeping peacefully and yes the
next morning it might happen that we
think wow there's a big drop in the
success rate we need to do something but
it's mentioned you know about that yeah
Italy where is you could have wrote days
more code on top of that yeah that you
then subsequently have to roll back and
rewrite matters actually you made an
incorrect assumption so you find out by
finding out quickly it's far more
efficient true yeah
so it shows me a drop and I can act on
it at that moment already instead of
that finding out after a couple of weeks
or maybe when it goes live or has been
live already for time and I don't know
with you but first of December we get
2018 at least that's the problem see if
they deliver on promise
we will merge our code starting that
that week and we will putting it in a
database and run the test test is also
code so we need to merge that too and
then see
where things went wrong maybe because of
the test that changed but maybe also
because yes new functionalities is
interfering with ours another question
for the audience how many people expect
within the next before Christmas to be
asked how long would it take
to upgrade this to 2080
how are you estimating that currently
what why what are you basing that
estimate that you're giving back on your
going a number of days number of weeks
whatever you're just pulling that out on
gut feel like you're going well I've
heard about this set of changes I think
that that's you can't you don't know
what they refactored you don't know
what's happened under the hood it might
look exactly the same on the front you
know we all found that didn't we with
2016-2017 code unit eighty cause anybody
a bit of any unexpected time over the
last couple of years and
so you get 2018 Luke you put the tests
on you run your tests you know what you
need to go to and it's not a guess it's
not an estimate it's a definitive list
to work down you are reducing it to a
much more programmatic
list yeah
so we're almost at the end
some takeaways and and do's and don'ts
on the test creation part it's all about
data as I mentioned that most of the
time that's a time consuming thing if
you do it manually it's also time
consuming when creating your test but
then you can easily rerun it again and
plan it when and what you're going to
write it's not something you need to
wait before the code is ready yeah on
the MS test part so if you will be using
it it's also about data the most fixes
we had to do was in the setup yeah and
we could do that as a generic level some
at the detail level
it brought us very fastly to a
usable result yes you saw 5,000 errors
and then the other errors pop up so it
took the first days like I'm not going
nowhere I even got a drop back but then
all of a sudden boom I had solved an
only receive that's why you know the
testing framework has not had a greater
buy-in from our community a lot of us
have tried it pulled it in run the test
looked at the number of failures and
gone whoa when I've got a spare couple
of months I'll go sort that out okay and
that's best a couple of months never
comes around and I think that's
consistently what's happened but
actually you can as Luke's proved with
these experience and and I'm back this
up you can reduce that down really
quickly just because it looks so bad at
the first view keep persevere with it it
will start paying dividends really
quickly not as bad as it seems you need
to be this bold look mmm don't let's go
the more you fix the longer the run will
be it was a bit frustrating was like it
finished after half an hour and now it
runs three hours but that's because it's
it tests everything
while you sleep of course
some do's and don'ts
begin with your test already before your
coding probably you will still not do
after you heard it twice or three times
for me but it's it's testing should not
start at the end actually when as soon
as you review requirements you're
testing it already that's what it's
called testing the requirements you
should be there already looking at it
from a testing perspective
I'll leave this to you because I want to
have some time left for you for
questions there are some other do's and
don'ts most of the things have been
mentioned
so some references some tools I've been
using I didn't mention all of them
some questions
anybody question and depending on your
question you might be
you might be yeah you can talk in it
yeah you have just at the top that's
interest go ahead test test yes once
again write your script for auto test
okay I have at least 35 we could here
but can it be somewhat louder
yeah okay
first of all you probably familiar with
the new version the tests we wrote
already will they be convert it with the
converter and they're working on it but
yes you can already do some things I
haven't but it should be working with
each with es code anyway yeah I'm not at
the moment aware of the state is there
but they're working on and you know
Microsoft has 20,000 tests they want
don't let go of that I suppose so yeah
okay so about the headless run yeah is
it different than the graphic user yeah
is it very different who can we use the
tests we created and run graphically you
have to program it differently because
you have to assign a test page define a
test page where you have acted on it so
the test is programmed differently yeah
and another because I already did some
okay my question is can we use them in
order to settle them in the night just
without even being in the office I mean
I don't want to start yeah okay that's
what is running away you have two
questions the this is the next one yes
thank you very much we there are also
some people without a question you threw
it out there yeah yeah
I'm a user
work for a company or as
solution developer inside the company
yeah like me and
we are going to have very big upgrade
yeah and
thinking of using this tool or for
further upgrade but we have a lot of
customizations
my question is
do you
put it down in smaller
things they can can it run or energy
difficult conversation also I have to
build all my own tests
requirement for that the my story is yes
you can run it and see how your
customizations react or conflict with
the things yes and fight see if if you
are specific perseverance as I am to get
that done if you want to test your own
part only you need to write your own new
test for that yeah
also we are going to upgrade it to two
sooner vision
finders tool or can we then use the test
or Microsoft have developed to see if
that's the same part so which version do
you come from and where do you go to
2009 so there's no test there yeah so
you go to the new version and see if the
the the new surfaces work somehow yeah
but then still you will run into a lot
of issues so let's say it will not give
you an outcome like okay this upgrade
was right no probably not yeah
okay thank you
you may throw it to us and yeah don't
throw down a hat yeah thank you
there I have two short questions and the
first one I I don't understood when you
talked about it they commit it's ignored
when it's in a test isolation so there
is no commit and writing in the database
there is a commit and the transaction so
the transactional part is exactly the
same as normal code the only thing is if
you run the whole or do the whole
execution through this test run with
this isolation set to either code unit
or function it will at the end of a code
unit or function do a rollback and that
has nothing to do with the normal commit
or whatever it robots everything within
this this bulb yeah it's like a second
level of get it okay but when when I use
and the commit directly in the code or
there is some there is you commit done
yes but let's say call it a soft commit
any error occurring in your test after
that will roll back until that commit
yeah and
then when the whole thing is over it
rolls back everything
okay and one thing you can set the test
isolation from code unit to function
yeah is
I set it to function and my function is
test isolated the code units is not and
I call the
isolated function do we have the error
with get last error text
let's take this offline
may be simple but my mind is also
looking at the time so sorry for that ok
so just want to ask the global variables
I can separate they will not roll back
okay no you have to handle them
separately this that's normally no
normal transactions also if a roll back
doesn't do change anything with the
local tour to act with any variable okay
so I have to consider it when I write
man yeah okay yeah let's exchange well a
last question yeah good I made a point
down here that I'll ask you a question
okay why did you not write one code unit
to kind of fix the labels and just run
that first before you run the test yet
rather than change 400 and something out
test that's an option yeah which I
considered and while you're shaking your
hands you're the ones that's
why I don't want because I want every
single test to be able to be run
independently of anything else I think
that it's a quick fix and it's a it's a
valid one but I don't like it simple
yeah it's an option but I want my test
to be atomic thing I want my coat unit
to be able to be brought somewhere else
without with forgetting the rest that's
all yeah so there are other options you
could put it on the what is one of the
global triggers when it starts running
this code unit you could even have
something there there are different
options but well let's say from from my
test background I didn't want to do that
differently that's all
depending on something for example of a
purchase invoice and we need to divide
it between our customers and dividing
can depend on a lot of criteria yeah how
I can test it or just a hard court just
if we have the invoice on with the base
of 3,000 euro and hesitation is decent
just calculate on calculator what it
should be and I expect just this result
yeah that mean I need to have in mind a
lot of various citation and all these
insert in you do that anyway because the
first thing you do is you go look right
which customer am I going to use for the
test which vendors are many you know go
find a transaction go find an inventory
item go find a GL account
you doing that anyway
sedation between our customer I expect
such kind of result for example customer
ear I will receive invoice for 100 EUR
customer B for 70
verification no no and you have
different scenarios the thing is that's
there's a fault you cannot do create a
test let's say a generic test with which
you feed with different
that's the unfortunate thing you have to
create separate tests for them and then
create a generic function which is being
called but every test function needs to
be a test function on your own you
cannot create one test function which
does test
the first one is the hard one you create
the first one and then you clone it and
change the criteria and so you know I
became a fan I had a project with a
customer that had 14 European VAT
registrations and
we had to test all of the transactions
for all of the types of supply through
all others and that we had the client
come to visit us for the testing process
and it was supposed to take three days
and when we demonstrated the automated
testing we finished in two hours because
in effect we proved the first one and
then we just went right well this is the
input this time this is the Apple this
is the input this is the output they
went yeah yeah yeah and and now we can
run that after every change we make and
it's and we know it's right
we take this offline we're going to we
are yeah I'll add in time we took some
records I'm sorry for that but thanks
for having being here yes
