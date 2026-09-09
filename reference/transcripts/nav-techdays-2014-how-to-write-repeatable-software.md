# NAV TechDays 2014 - How to Write Repeatable Software

- **Source:** https://www.youtube.com/watch?v=7ZUceRrbNAo
- **Video ID:** 7ZUceRrbNAo
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 97m29s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

ladies and gentlemen good afternoon hope
you had a good lunch break we're ready
to go for the next session please
welcome on stage certain mark and Gary
thank you good afternoon everyone
welcome back after lunch welcome to our
session about how to write a repeatable
software there's going to be four of us
today we have a team by vehicle of
Babbage we have me we have Gary and we
supposed to have Waldo here as well but
he was doing a multi-tenant environment
implementation and for some reason he
couldn't spin-off one more tenant to be
here so we had to replace him we found a
very good replacement with with CERN
today before we start the presentation I
would like to do an exercise you have
all been to lunch and maybe a little bit
sleepy so we're going to do a little bit
of gym I would like to ask everyone to
stand up please very good very good I
can hear people say oh but that's
because they're getting old right so for
everyone if this is your first p or s
session please sit down the first if
this is the first session so a lot of
people actually came to see us for the
second time if this is the second time
that you see yes please if this is not
the second time that you see yes please
sit down so and then everyone who was
not here during our first session in
2011 can sit down too okay though
there's actually quite a few people who
were here
even for our first session in in 2011 so
let's go through the agenda today we
have 90 minutes and I just wasted two of
them we're going to start with an
overview about PRS and then Gary is it
going to talk about methodology after
four years we think we have a complete
methodology on how to write repeatable
software then we're going to do some
out-of-the-box thinking we're going to
dive into some nov 2015 features and how
you can use them outside outside the
context or maybe inside after this and
then afterwards are going to talk about
the the roadmap what we're planning to
do after after this let's talk briefly
about Barton rally software in the
history I like to believe myself that it
started with me writing a book and 2010
about application design I just updated
my book for nav 2013 it's released in
September and I will update it for nov
2015 as well after I did that Gary and
Waldo approached me and said we need to
do something with this we need to tell
people about how to design proper
applications so we started the community
initiative partner Eddie software we
started with the three of us first and
then vehicles joined us and now we have
certain with us as well after a while
Microsoft approached the Sioux we went
to fell back did a presentation there
and we started the design patterns team
together which i think is a great step
forward Microsoft explaining design
patterns they will do it tomorrow too
yep I'll tomorrow after lunch I think
it's great that Microsoft actually
explains how they did the improvements
in the system and tells us how the
architecture works behind the scenes so
if we can if we want to achieve the same
experience we actually know how to
implement that so currently we are with
nav 2015 it's the current release and
with this release and also backwater 2
2013 are too we have the power shell and
the power shell is actually one of the
great tools that allows us to be truly
repeatable and for me that that
completes the circle and I really hope
that Gary is going to talk about the
methodology today and I think we have a
real nice coherent story now after after
a couple of years so we started the
design pattern projects we started it
together with with Microsoft we started
writing down design patterns I think
currently we have about 60 patterns but
I think there's way more in the
application than than what we have now
if you look at the screen you see things
that you might recognize number series
documents journals copy document all the
things that we used to have in la vie
for last what have we 2025 years but you
also might see some things that that you
might may or may not recognize that
things like hooks encapsulation
readability which are the the BRS design
patterns that we added so if we
categorize design patterns we talked
about architectural patterns which are
the documents and code units and the big
building blocks that the application is
built off then we have the design
patterns which are the part of the
architectural patterns which are number
series blocked entity the smaller
address integration so what the smaller
things and then we have the
implementation or patterns and most of
the PRS patterns are part of the
implementation or patterns they are more
the way how I design things how do I
write code how do i hook into codes and
what have you so why is this all
important Thomas already talked about
this during the keynote the speed in
which Microsoft ship software changes
and it changes fast it used to be like
three or four
years and between any major release and
that started to increase the last couple
of years we had Lee yearly releases
currently we have nav 2015 last year we
had 2013 are two but the r2 didn't
really play it nice because it was a big
release and next year we'll have Corfu
and typically if you look at how a
customer treats the versions they would
skip a version upgrade from four to two
thousand nine upgrade from 2009 to 2015
and this is not a way we want customers
to experience nav anymore on top of the
yearly releases we get the monthly roll
ups that contain our hot fixes
regulatory features but also whenever
Microsoft finishes some feature if it's
not breaking anything then they
backboard it into the into the roll ups
and we actually get new features inside
the roll-up so we get those monthly
releases and instead of upgrading every
two or three years actually the strategy
that Microsoft wants us to follow is to
be always current we they want us to be
always current with our add-ons and they
want us to be always software with our
customers as well so how do I stay
current first of all the PowerShell the
numerous command lists are great they do
a great job in in helping you merging
your software dealing with conflicts
then the design patterns if you follow
the best practices then the chance for
you of running into issues during your
upgrade is way smaller than if you start
reinventing the wheel you might actually
do something that Microsoft did not
anticipate on and then you're on your
own fixing your problem reducing your
footprint is also a very good principle
the less you change in standard nav the
better implement PRS and then gary is
going to talk about hooks and facades
and all the goodies that you get when
you implement our methodology it's all
about upgrading in minutes we want you
to just
go for lunch start the PowerShell and be
back had lunch and then be upgraded and
it's about reducing total cost of
ownership and this is especially true
for customers I presented design
patterns in st. Louis at navik for
end-users and every piece of software we
write stays at a customer database for
10 or 15 years and the easier it is for
customers to bring forward their
customizations the more likely it is for
them to stay current and they in the end
pay the bill the fact that we are all
here the fact that we have all these
great events like directions I was in
Bali last week we have this great event
so the fact that we have that is all by
paid for by the customers so I would
like to invite Gary to start talking
about the methodology thanks mark so
I'll try to squeeze what we have thought
about in the last year in just 30
minutes since you're all sort of level
400 500 600 that will not be a problem I
have tried to divide what I'm going to
say speak about in two or three parts
what is repeatable RP just a very short
introduction then how do i write
repeatable IP that's the main the main
thing and the third thing is how do I
get started so that when you go home you
can immediately after this session start
doing so there are three types of
development that coincide with the
development of the partner organizations
that we're all working in or four and
sometimes against the first phase was
that of individual programming and that
coincided with your part organization
trying to find your niche trying to
establish a footprint in your in your
markets then we went to doing
standardized add-ons that that sort of
began in the late 1990s and we try to
stand out sort of as in the industry
domain experts and and build a solemn it
solid customer base based on one market
segment
and the phase of repeatable IP which has
begun but actually is only beginning now
is that face and where your partner
organization wants to leverage the
market segment that that it's that it's
created to produce software and and
really create significant market shares
and what I'm going to tell you about the
methodology is very valid and inevitable
i think if you really want to do
repeated IP cloud business subscription
model business but it is valid for all
other programming styles as well it will
just increase the value of your of your
code so how do i write repeatable IP
first of all an overview again there are
five areas that i would like to go into
today one is agents then we come to
classes and methods then we come to a
special design pattern called for Sade
then we come to a very brief slide on
design patterns and then I try to wrap
up what you can do when you go home
after after this conference and now
agents that's probably something that
you haven't really thought about a lot
at least maybe not all of you if you
think I have prepared an example of a
medic and you can you may think of him
same as being a vendor but just think of
the business content first you have a
person you which I call an agent and he
has several actions that he does and
they are defined an agent can a medic
and diagnostic and treat he can refer
you to a different medic and he will
also probably invoice you and he does
this in several process in in several
contexts you may think of them as doc
human types or whatever but they are
like processes like he does that at his
office he does that on home visit and he
does that in the hospital and if you
want to combine the agent and his
actions and the processes in software
it should somehow look like that that is
clean you have the agent at the top you
have the processes that he does and you
have the actions that you can do on a
very abstract model but if you look into
how we do that in encode and if I look
into my code like five years ago it
looked more like that we were sort of
not referring to that as an agent who
works in the process and doesn't action
but we were calling like a cold units
and and methods directly from the action
trigger and the page so the code looked
more like unclean directly from the
process we go to an action not even
thinking about who is the agent who is
acting here who does something and if
you act if you add another agent of the
equation let's say a paramedic it should
of course be a different agent who is
related to this one but we kind of
encoding sometimes put them sort of in
the middle and let him do the same thing
all over and the fiendish thing about
this is that this works but it's not
transparent and if you want to grow your
software and somebody else looks into
your software you will have a hard time
understanding what you've done to trans
translate this here into into code let's
do it so let you maybe get an example of
what what I'm talking about by means of
code this is what we often have done in
the past and often still do I still see
that a lot a lot in softwares we have a
diagnosis action in a purchase order and
what we do is we call some code unit
with some function this code you owned a
sort of a functional collection of
everything that the medic does and we
pass a code field as a reference and
then whatever that action is is coded in
that code unit what I have told you we
should be doing instead is something
like that you have actions defined on
your agents you call the agents and let
him execute the action that's it ends up
with doing the same but it's much
more clearly structured and much easier
to follow and you always know if I have
to execute an action what agent is that
on I get him and that wife I will find
every action that this guy is able to do
on the agent translating that an egg an
agent is a class like an object-oriented
language in nav that will be like a
table an action is a method and an
object oriented environment or a
function in a code unit I'm not looking
at processes in this in this context
that would lead us too far so if you do
any sort of development if somebody asks
you to do something gives you a task
start any development by determining who
is acting and the agent is always a
class it's always a table there are
exceptions to that rule I know but they
are few if you if you start thinking of
who is acting here you will always find
that there's a table that is acting and
that you can assign all relevant actions
to the from that so the advantages that
you have you always have all possible
actions defined on on the agent you can
see that in intelligence just by
preffered pressing f5 you know what this
class this agent this table is able to
do and every other developer and even
every other consultant can actually see
that let's jump into classes and methods
that's actually the biggest part classes
that have already said our tables they
carry all attributes and all methods
that these classes are able to perform
attributes are fields in nav terminology
methods are functions and all methods
should always be declared on the class
all fields are anyway we can't go around
that VA co has shown that you have a
lots of possibilities to declare
properties and fields in in c-sharp very
freely in text we can't do that all
fields are always declared on the table
in nav and that's what it looks like for
the van
for the actions for the methods we have
these choices that we that we sometimes
not really apply in the in the in the
best and most efficient and most
transparent way so our suggestion would
be what you do with the fields please
also do that with your with your methods
that the vendor can do if we say a
vendor is is the mattock then you should
have functions diagnosed read refer
invoice declared directly on the class
just do that even if you don't have to
do that you also see here that there is
hardly any code in these in these
actions in these methods that is by
design although the methods are declared
on the on the table the code does not
reside in the table and we see where it
where it sits a little bit later on so
that's what I already said you see
explicitly which functions exist for
each table which methods exist for each
class and which actions are defined for
each agent and that is actually the same
on three levels of communication so
let's look into methods because that
that's really how you structure that
that's really the heart and soul of your
application and we look into four
categories into encapsulation
readability consistency and decoupling
let's do encapsulation first each method
we recommend and I ever say we recommend
like we're doing that actually with our
software at a factory dealers that a few
other companies who follow that
methodology each method is a code unit
of its own like create recycling
worksheet that's from one of our
verticals find recycling company move
recycling entries change sales business
process load recycling entries
everything that you can do all the
actions all the methods are just one
code unit each and I gladly take the
opportunity again to ask Microsoft
to give us code units for free because
it really helps the structure your code
it makes it makes code units much more
readable and then each method only has
one global function since that does not
involve any budget decisions microsoft
has gladly already done help done
something to help us in nav 2015 when
you've been in the keynotes so when you
open a code unit and you declare a new
function it is local by design so
Microsoft things and and and and we
think all the functions in a code unit
should actually be local except for one
and that is the method header that
declares what this global function does
in this example we have a method here
called save a location that's about
planned and actual cost allocation and
the method header gives you a sort of a
flowchart of what this method does and
all the other methods that that you see
here are just calls to local functions
on the same code you need a method
should also always be instantiated
through its class so I will never call
this code unit save a location through a
code unit variable we've seen that it
should be declared on the table and I
always just reference it through the
table so I always call the agent call a
method on the agent and then this
invokes the code unit we see an example
here from code you need 80 where we've
added a few functionality to the sales
letter post plan cuz postconditions post
pallets and these methods are declared
on the sales header there in a with
statement here so that we don't even
need to have the sales header dot post
plan cost and that actually saves you
from declaring any variables in this
code you need 80 you don't need to
declare variables because the method is
already declared on the agent which is
the in the with statement anyway so as
soon as you think you need to declare a
Code unit variable as something wrong in
the code a a method break down what what
do methods do well what should you do
with with with your methods break all of
your processes down into encapsulated
methods it is not quite easy to get the
sizing right I admit that like how small
should the methods be or how big should
they be there is conceptual work that
you need to do but we're talking about
professional software production anyway
and that means you should put a lot of
conceptual work into your architecture
before you start coding that's not
always how we work I know that that's
not always how I work if you're under
pressure in a project while we're
talking about repeatable software
product development here mainly and but
if you kind of do that and break all of
your processes down that allows you to
put these methods together again it is
as if it was sort of a scripting
language you know when when VA co tells
me about JavaScript I always wonder one
does this guy start coding he just
collects functionalities that have or
that already exists and sort of puts
them together you can look at it you can
look at naf this way if you have all
these methods broken down it allows more
high-level programmers to just pick the
methods and put them in the right in the
right order and that allows you to build
new functionality and automated batch
functionality on existing and already
tested code so from encapsulation let's
move to readability which is not as
technical but just as important we've
seen that method header in the save
allocation code unit which consisted of
a lot of lines of very readable code
that is how you should always look at
your code units and method the global
function the method header of each
method
should be a readable flowchart of what
your method does a developer when he has
to do a task he thinks about that flow
chart in his head anyway he says okay at
first I need to set a filter then I need
a repeat loop thing then I need to
initialize some variable and I need to
insert some variable he has that old is
this this flow chart in his mind but
what he often does then is just do the
best in his code to hide that flow chart
again in a lot of long chunks of very
nerdy code that's not not the idea you
should be able you should actually break
down the steps that you need to to
execute that methods in these parts that
you need to execute make them as small
as possible so that each part only does
one thing and have a readable flowchart
in your method header that tells
everybody including consultants in
natural language code what it is that
this function does that that that should
sort of resemble plain text this method
header and not carry any any nerdy stuff
like and if you look if you look at what
i call nerdy stuff and non nerdy stuff
cast dotted the get customer is not i
mean that is a fairly fairly irrelevant
example but i think you get you get the
message get customer everybody can
understand that where is cast get is
already language specific and this this
readable flowchart should also include
all relevant steps like not only check
if I can do that do that normally you
have a lot more steps in between and to
structure that so that it actually works
that your method had a includes all or
most of the relevant steps that you do
and does not not omit one is also not
always easy to do but when you start
doing it you'll get the gist of it quite
easily at least my developers have and I
know that Wohlers developer have and
even the ones and especially the ones
that
come from a visual studio c sharp
environment find it very natural to code
like that and they say does enough does
do people in they have not code like
that you're not telling me that really I
you a readability just an example from
another method in in a vertical this is
about batch posting warehouse costs
something that some of you most of you
may have already written so what this
method does is defined by the method
header it says error if no period error
if no posting date error if no location
filter or error if location filter too
long get cost posting number commit
transaction to database and here's the
first key t-shirt what is in the in the
in the function commit transaction to
database what is the the code in that
you don't get a t-shirt no you do yes
that's exactly true I mean sometimes
it's very easy sometimes it's it's it's
a bit harder then comes get the food set
up in it rounding procession clear
general journal and then we start force
height progress if no user interface
forcing on transit filter on location
because we don't record warehouse costs
on locations that are in transit and
then we start post where I was caused by
location and it goes on so if you have
an error and your customer complains
well this your application throws an
error just because there is no posting
date please fix that and your consultant
can look into that and so and say well
it is an error but isn't a place
application error it's not a development
error it has been done by design you can
even he can can say that reading the
code and that's not only a valid for
consultants it's also valid for support
it's valid for any other developer who
comes like half a year after that and
needs to enhance that functionality he
can very easily understand what what
people have done why they have done it
in what order they have done it and also
these functions as you said commit
commit transaction to database
are so tiny you detect any error in that
function immediately they only do one
thing and they're very good at doing
that thing and if they don't do that
thing or if there is an error in that
it's very easy to spot it's also very
easy to enhance these parts or shrink
these parts because they're not part of
a huge chunk of 450 lines of code that
are just with a lot of begins and
repeats and until loops but they're just
very defined and concise the functions
that that are easy to handle and easy to
understand the process components if you
look into these code units that do a
single action and you look at a lot of
them they appear as different as they
may be they all end up having the same
process components that's really
interesting if you do a complete big
software and I've done in the last year
a huge project with various completely
different methods very completely
different actions functions if you look
at these code units they all have the
same components you have that method
header and you normally have some sort
of validity check does this method apply
to this to this data item or not to this
data entity or data item you normally
have a section that filters something
you normally have a section that loops
something you normally have a section
that initializes data or updates values
and then you have a section with
database transactions modify insert
sometimes delete and it's very
interesting like that that all of these
code units is different as they are are
always built up from the same process
components and you can actually go
through these code units and look for
these process components and if one is
missing and say is that an error or is
that is does this action does this
method behave somewhat differently so
you can even analyze your your actions
just based on process components and say
hey you don't have a loop
do you think that's all right are you
just handling a thing really just
handling a single data item here
shouldn't there be a loop section oh
yeah I missed that it's it's sort of
always the same if you do some
meta-analysis of of the code units that
you that you have come up with so from
readability let's move one step on to
consistency so and that's consistency as
as seen in naming there is a
functionality that we've written and I'm
by design taking functions that are not
part of of nav stunt stand up but of an
add-on that we've developed we have a
functionality that posts accruals
automatically so we have a page action
that is called post accruals ellipsis
dot dot we have a method declared on the
cast on the class which is called post
accruals the code unit name is post
accruals or if you're a bit more legacy
minded you probably could also call that
accruals dash post which would be the
old nav way of doing it the method
header is called post accruals
development I need to warn you becomes
boring but it also becomes very
transparent and this transparency you
should really take a step further the
naming should be consistent in other
contexts as well like posting a cruel
should what should be what the chapter
in your in your process manual says it
should be on the help server consultants
should talk about that sales persons and
the sales material should sell the
functionality as posting on accruals and
a customer facing feature description
should also say posting accruals now you
may say that is all self understood just
look at what you have written and what
your sales people are selling and even
the language is completely different
sometimes sometimes maybe you've had
that experience in the past I don't hope
so but I fear at least I've had it now
let's let's move a little bit more
deeply
into decoupling and a design pattern
that is that is closely linked to the
idea of decoupling and that is what we
call the facade I know there are quite a
lot of design patterns that are not
called for Sade but kind of do the same
thing it's not always easy to get the
terminology right but the terminal that
the term for Sade has has worked quite
well for us what is a facade it's
actually quite easy after everything
that we've just introduced in the last
10 12 minutes what you've seen is that I
said a class every method should always
be declared on the class and be executed
in a code unit of its own so you have a
direct connection between the class that
declares the method and the code unit
that sort of implements the method now
these two objects these two nav objects
are both quite heavy weight I mean the
table is the most heavy object in your
in your object collection there are a
few versions of nav in what which it was
not really nice to change the class
because then pages would kind of pop up
if you inserted that that new table and
and say there's a desert I have a new
field it doesn't kind of match anymore
okay that's that's past us but still the
class carries your your data definition
and the method carries all the all the
IP that you have so these are quite very
important and heavyweight objects that
you don't want to change too often and
they're linked they're linked quite
closely as everything enough which is
one of the few very few drawbacks of nav
as everything is linked quite
quite closely and we want to do
something to decouple these heavy weight
objects a little bit and that's what the
Fate does a force aid is a code unit
which you put into the middle of these
objects to decouple them so that's what
it looks you don't connect the class
directly to the method but you have a
facade in between that does nothing else
there is no content code in that verse 8
that does nothing else but know where
this method is implemented so it only
finds the code unit that actually
implements the action the method that
you want to execute from the class and
what good that is is is best made clear
if you work with external components
like you have a way bridge if your
customer has a weybridge he needs to
wants to attach that to nav normally if
you have three weighbridges in your
company they come from five different
producers so the dll the DLLs are always
quite different although the call to
these of the actions are always the same
and just get weight and then you have to
branch to five different DLLs depending
on which way bridge you connect to so
you don't want to have a heart
connection between the class and the end
the method that implements that but you
want to go through a middle piece a very
soft middle piece that just knows in
what context what a dll is to be
implemented and if you take that out of
the external component arena and apply
that to something like get sales
conditions or get sales price you may
have completely different methodologies
or approaches in getting the right sales
price in completely different contexts
for different customers whatever so you
have the the class and you have three
different methods of addressing a sales
price
and the facade just knows which one to
pick in which context so we have a soft
link to a multitude of methods that's
what the facade does it decouples the
class from the method the declaration
from the execution and just finds the
right place as an interface where the
method is actually executed and what it
looks like is something like that this
is a facade code unit from our
allocation table that we've talked about
earlier where you allocate plant plant
costs and all it ever does is just find
the right method the the right method in
that context there may be actually more
code if you have like a case thing it
finds it needs to find different methods
different code units depending on the
context and what you also see there is
one method here save a location that
starts not with that starts with a
completely different line forty use it I
must be finished at forty you said you
didn't okay sorry and sorry I'm overtime
miscommunication so what that does it's
called to confirm before the method and
then acknowledged after the method and
the method in between so it wraps you I
that's what you normally do you have a
confirm in front and an acknowledged
after and what the whole architecture
lies is is like you call the class which
caused the facade which calls a code
unit that wraps the UI and then executes
so that you never have the UI in the
same code unit as the execution we have
so many different clients so many ways
of treating stuff it is it makes sense
for me to sort of try and always
encapsulate the UI and separate that
from the execution of a message so
design patterns I can basically skip
because facade has been a design pattern
and if you want and which is the one of
the secret sources of nav Michael
Nielsen
here and you can confirm that because
it's his quote if you want to learn more
about design patterns travel back in
time to yesterday where we did the whole
day on design patterns if your karma is
not enough for that then go to the
session of Bogdana botas and as larson
and mustafa bulut tomorrow at one-thirty
on design patterns and just to wrap up
in 60 seconds and easy methodology what
you should do when you go home establish
your agents actions model break your
software down into method and treat them
as building blocks as you've seen think
of your method heads as readable
flowcharts provide decoupling make your
terminology consistent and think and act
in terms of design patterns that's all
you need to do to write repeatable
software and with that i'm skipping a
few slides and handing over to mark
thanks Gary yeah there's a difference
between talking until 40 minutes or
until 40 minutes are passed with the 90
minute time slot so last year Waldo
introduced hooks and I think there's a
great momentum this year for hooks with
the new power point code merging the
power point power power shell PowerShell
code merging the power shell code
merging really helps in moving your code
forward and the hook is a great way to
reduce conflicts you can make codes on
the on pre or on posts or somewhere in
between it doesn't really solve all the
conflicts if you write some code and
Microsoft or another partner explicitly
writes the code on exactly the same
place you end up with a conflict anyway
but if you implement a hook it's not
really a conflict you can basically
write write some macros to to ignore it
but this year we wanted to introduce a
new idea that has been documented this
year by by suren so we're enjoying our
our PRS
project and soon we'll talk about
surrogate keys thank you Mark so well I
was the year ago I joined to be the
design pattern team with Boch Donna and
I had an idea for creating something
that was different we're always talking
about creating repeatable software so
software we can reuse software we can we
can plug in other places originally I'm
Danish so I I at the time called in
legal programming because i was thinking
i want a small block of something that
just fits anywhere in the system and i
was trying to figure out how can i do
that I mean I'm of course limited I
don't have access to the platform so I
can't I can't do a lot of changes so I
wanted to try and find out how could I
in some way in the system exploit what
is in the system and how it works to
create a possibility to plug things in
in smart ways so I came up with
something that I later found out is
called a surrogate key and the surrogate
keys pub is basically a unique
identifying database for either an
entity in the modern world on object in
a database yeah well that's something
but it's it's just a unique identifier
on any record in a database that is not
derived from any of the application data
so it just it doesn't care about what
you have in the record is just a unique
value so I looked at this like some of
the generic functionality that i was i
was thinking of creating was things like
comments why do we have 28 different
comment tables i think it's 10 28
different comment tables to stand up
math could I add text or anything I
wanted to could i put documents on any
record i wanted to an attached it
could i create user defined fields I
showed this to bass and you came up with
a few other ideas there's tons of ideas
where we can create things that we can
reuse in on any recording system so how
could how could i implement this well
what I came up with was to use the auto
increment property say so just create
one field on a table that's an unsure a
surrogate key turn the auto increment to
on into the field and do it that way I
consider things like GU it's goo is an
upgrade and sequel they they don't
really perform well especially if you
starts having having them in keys and
the other thing was that goods or any
other way of creating a new unique
identifier would require me to put code
and every table I didn't want to do that
I want to put my footprint as small as
possible so the auto increment and the
integer field seems to be like the
obvious solution then you can ask
yourself why not use the record ID we
have record ID it works fine well it has
a few issues when you want to try and do
something like this the only negative
thing I could really find with serve
akiza's I need to add it's not there by
standard hit Microsoft is sitting down
here so it would be great if it was
their standard but it's not there so I
need to edit on all the tables I want to
use something for okay its one field
it's auto increment there's no code it's
a relatively low impact on any table
regular ID already exists way better but
if I need to rename something regular ID
changes I need to update all my records
i need to change it all over the place
kind of nut nut so good my surrogate key
I don't care because it doesn't change
it has nothing to do with with the
contents of the data in the record it
stays the same if i delete yeah there's
some issues I need to of course to
delete the records in my in my what
our table I have that I have linked into
my surrogate key but I can manage that
in in encode unit 1 on the global
trigger the same could be said about
record ID it's I think most most
implementations I've seen its always
handle on the delete trigger and then
there's filtering and filtering is
another issue and that's probably the
biggest issue with record ID if I wanna
attach let's say I have created a
comment form that's generic so I can
attach it any way I want I can't filter
on it with record ID without somehow
implementing or putting in code into the
system that passes this record ID so i
can set a filter on it by code and with
reducing what i'm looking at this sounds
little tricky right right now but I'm
coming with a great example in a minute
the the auto increment is much easier
because it's a field in the table I can
just put a filter so whenever I if I
want to add comments to an item or to my
rental item or to my service item all I
need to do is just at the page put the
filter done so i keep my footprint very
very small by using sort of the keys
compared to record ID so let me show you
an example hopefully you can see laughs
now I should probably jump out of here
to mafia so here I've implemented
comment a comment table I've done it
very simple easy comment table has a
table ID as a surrogate key a line
number that's the primary key we don't
really care about from a data
perspective the only thing we normally
have in a in a user sees in a comment
table that's the date the code in the
comment for the rest of you that really
doesn't care so based on
that I have created my two standard
forms that any comment table has I'm not
going to go into that you probably all
know that you've probably created
comments on lots of your modifications
anyway where you basically take the
standard Microsoft code and you redo it
to fit your application and then I have
in encode unit one add it hooks down
here so basically there's a hook here in
the this is the global triggers so that
these triggers they trigger anywhere
across the system so you have there's a
hook here that's calling my
functionality and of course my
functionality in the one I'm mostly
interested in this case is my deletes of
course it goes and I have my surrogate
key management pause my delete function
and make sure that my comments are
getting deleted if i delete the record
but I don't need only need to do this
one place for the rest I don't need to I
don't care which record i'm working on
across the system and as soon as i do
this i can now go to and actually
implement it somewhere in this case i
implemented it on the item i did it on
the item here because that was a record
ahead in the system instead of database
is pretty easy and that way you could
also see the difference between standard
and this which is nothing so all I did
was I added a surrogate key to my item
table of course made it auto auto
increment or auto increment yes that's
fine that's all I need so now I have an
anchor point on my table at all any I
don't need anything else I can now go to
my item card in this case it's a table
at it's an action read the comments an
action on it I could make it a button on
the on the on the page I could make it a
fact box I could have made it anything I
wanted to but all I need to do to add
comments 22 and I to the item card is go
in find out where my comments and the
comments I think that passed them where
are they oops nope she's of course have
chosen one with a few actions but so
here's the normal comments and here's my
comments so i just added my comments
here and the only thing i did add this
one point to my comment page and put the
filter these three lines and done if i
will create a new mast item rental item
I don't need to do anything except at
this one page 2 or this one line of code
to my to my paces but the ones I wanted
on and I have comments I don't need to
redevelop comments I don't need to
create a new comment table only to
create new comment pages I have comments
and they work everywhere and similar to
this so looking at this I'm basically
creating functionality that is I'm just
going to switch back to the other screen
so based on this i'm basically creating
functionality that's absolutely
repeatable across the entire product so
i create comments once i can use it
everywhere like i said what about text i
could have created text and i can say
let me attack it let me find out let me
put tags on any table in the system and
say i want text okay do no development
no testing because i've done that once
so basically what i just did here was
you see the standard structure on a
comment table that is we attached the
the we have a document header we have a
document line we create a specific
comment table to this document
with the the primary key we do the same
for master item we create a specific
comment table to the spider master item
with all the other fields and then with
a surrogate key I just add a surrogate
key to these master tables and if that
was there already let's dream that it
actually was something that was just in
the system and we could use it to do
links oh I have my arrows dropping down
here forgot to push twice then i can
create my functionality in this case
again using the comment table just
because i think it's a great example i
create my comment table functionality
standout out of the box no special
features and i create my pace it
actually looks exactly the same page
it's looks if you if i take a stand up
page from the current system or look
like this and i could create both my
list on my sheet a standard
implementation of comments and i just
add my my link on my fat box and that's
the only this step once you have done
the other steps this is the only step
you need to do in any future except a
force adding the auto increment key and
of course you need to have the hooks if
this is the first time we're
implementing a new pattern need to make
sure that hooks and you need to make
sure that folks here of course we're
going to promote the hooks Waldo is
crying if you don't promote the hooks a
little so add the hoax but again this is
only the first time the second time the
third time the fourth time you don't
need to do anything except at the page
and create make sure that the records
are deleted is the last step which again
that's completely generic you can just
use the record refs in the system and
completely dinero CLE delete these
records no matter which record you're
actually deleting as long as it's it's
linked back to to the to to my standard
people it's it's completely generic it
does no no code when you've done this
once you don't never did you think of it
again the only thing you need to do is
just add the server key if it's not
there and at the at the link and that's
generic code this is low impact it's
reduces your testing it reduces the
amount of work that you're doing to to
actually talk to actually implement new
functionality so here's the complete
true lead in Eric and repeatable code
slide and that's out of the box new new
way of thinking a new way of coding and
back to mac so now I wanted to take the
next 10 minute 10 minutes and share with
you some out-of-the-box ideas that we
within the PRS team got when we saw all
the goodies that we're getting from
Microsoft with the nov 2015 release and
the first thing I want to share with you
is the Delta file the Delta file is
something new that we got with nfe 2015
and the thing I want to discuss with you
today is I want you to start shipping
Delta's so this is the slide that Thomas
showed us this morning we have a base
database that has a couple of fields we
add a field to the to the table we have
a target that we want to move to and in
order to move our change forward we
implement this new object type and by
moving the object type forward we can
apply the Delta 2 to the new database so
this is the Delta and this is the way we
can use it within
upgrade if you use the PowerShell
there's two ways of doing the PowerShell
you can do the PowerShell with the Delta
so physically creating the Delta file on
the disk but you can also do the
PowerShell without the Delta and
everything happens inside memory but
what I would like you to think is start
using the Delta for much more than than
just within 11 upgrade if you are an ISV
like a gillies or lanham or 0 p plus
you're most likely to ship software to
your partners and traditionally the way
we ship software is we make a fop file
and then we send that file to the
partners and then they start playing
around with it and basically what we
think is that with the with the
PowerShell a new star is born and a new
star is the Delta file and instead of
shipping fo b it would like you to start
considering shipping Delta's instead we
you can ship the Delta to any partner
and the partner can use the PowerShell
to start applying the Delta to their own
objects there are some some good and bad
and ugly to this the good thing is sales
just a whole bunch of time because what
happens at the partner that receives the
software they take a Cronus database the
import the file the export text start
merging it and getting star own software
and those are basically all steps that
they can they can save they can
basically put all the deltas in a folder
and immediately start applying the
deltas to their own database there's
some bad things you have to start
filling around with the with the version
list there's a couple of scripts that
can help you doing that conflicts are
quite hard to handle I already talked to
pair Mogensen about this and he's
thinking about expanding his Myrtle with
the allowing you some user interface to
to handle the conflict files there is
some ugly that we are talking to it with
Microsoft with my
call that basically if you ship a new
table or a new field as a delta file the
Delta file is actually just the object
file but the current situation is that
the object designer the application
development does not allow you to add
any objects outside of your license
range and our suggestion is that to move
that away from the object designer and
just let the customer license file
handle that I think we are responsible
enough to add a table and to add a field
and eventually if the customer ships of
the software ships to a customer the
license file the customer will will will
solve this so this is something that is
on our wish list and we may or may not
get it in the future we don't know
Waldo's doing is powershell session
tomorrow at 9am I really encourage you
to be there he's going to talk about
more about this so that's the first
thing the second thing that we got with
nfe 2015 is a new object type called up
red code units and the way they are
designed is the idea of aqua code units
is to make life easier doing upgrades
traditionally an upgrade had a step one
and step two step one upgrade move the
data away from the table so we can apply
schema changes and then step two is
doing some business logic to put the
data back and the upgrade code unit
basically replaces step one and step 2
and step one is handled by some generic
piece of code that saves you the time of
writing all this but if you look at the
way that these upgrade code units are
processed they are part of the shipping
of the fo b file what happens if you
import an sob file the system checks if
there is an upgrade code unit
and if there's an upward code unit it
will start executing the upgrade code
United it will implement the step one so
it will move the data out and it will
allow you to apply schema changes and
then after the FOP file has been
imported the UI of the development
environment allows you to execute all
the upgrade routines so the thing we
want you to start thinking about when
you get your your hands on playing
around with NFA 2015 is to think about
the upgrade code unit outside of the
traditional upgrade context and it's
basically a platform to do any data
conversion with any fo be so anytime
you're during an implementation you have
something the way you want to apply data
conversion think about doing the upgrade
code units as a solution for that you
have to keep in mind that the system
just looks for any upgrade cogent in the
database so if you run the preconditions
make sure that you check the version and
that you don't start applying upgrade
code units to defer to the wrong version
and make sure that your approach code
unit is self-destructing I tested this
it works so you can basically if you
apply another B file and you ship an
upgrade code unit you can basically
delete the codes unit afterwards so that
not that you don't run into the
situation that by accident if you ship
the next for you start upgrading and
start running the the wrong upgrade code
units so with this I would like to
introduce vehicle and he's going to talk
design patterns through net and after
that I will be back with you to wrap up
thank you Mark we need to switch lap
years we me to switch
yourself
what you have two slides I think I do
yeah that's true I i need the slides
actually you need to switch back no no
no no I will handle it so I will somehow
just have to open my slide deck actually
switch back I apologize yes i'm
switching temporarily back okay so
thanks to mark for the introduction it's
something is still not quite yeah okay
so this is my first time actually
speaking as a part of the PRS team it
was kind of the goal of Gary and Mark
and Waldo to get me on stage for the
past three years but it just didn't
never happened so this time they they
succeeded so when they told me like can
you do some of your stuff and when they
say your stuff they mean like dotnet and
JavaScript saw Russell actually be
JavaScript and Garrett know because like
in JavaScript you don't ever see any
code just pulled things which are
finished and just put them together
asked like isn't this the ultimate
design pattern like just put the things
together and it works so I decided to
actually do it in net so the problem
with the design patterns is that many
people think that design parents just do
not work in functional languages and
they are almost right because in
functional languages you have very few
patterns on your disposal whereas in
object-oriented languages you have a lot
of patterns and the primary reason why
you have a lot of parents is that you
can you have polymorphism essentially
the polymorphism is the cornerstone of
any true extents extensibility so if you
want to have extensible thing you need
to have some kind of polymorphism
at least if you have strongly typed
languages so what I'm going to do is
essentially explain a little bit about
one single pattern because i only got
ten minutes onstage i'm going to explain
one pattern which kind of allows you a
lot of flexibility with with extending
your application writing repeatable
stuff and etc so what i will start is
the service locator pattern the biggest
problem with nav as we have seen from
gary's presentation is tightly coupled
code we have code which calls other code
which then calls other code which may be
called going back so it's very difficult
to for example have you ever had to
debug let's say inventory adjustment or
sales posting and stuff it's yeah it's
essentially it's one big bowl of
spaghetti that you somehow need to find
your way through and we are aiming at
extensibility at decoupling stuff so
essentially being able to add stuff in
or ed take stuff out or replace stuff
easily without having to code too much
this service locator pattern it is
essentially an incarnation of a not a
so-called but really of the inversion of
control pattern the point of the
inversion of control is that my code
calls your code but it doesn't do it
directly it actually uses somebody else
in between who actually tells me which
code I should call to or actually it it
kind of hides the detailed
implementation of the service in this
case that I'm calling into and it allows
me to actually just talk to an interface
which knows which things I'm trying to
achieve but doesn't know how those
things will be achieved and if you think
for example from perspective of nav here
I'm going to take a very real life
example of synchronizing data in nav
with an external application so
what my code in nav needs to know is
what i need to do i need to take data
from somewhere and then i need to
somehow store this data in nav how
exactly i'm doing that it's not my
concern so I'm calling a service which
does that and as far as I'm concerned it
can be any service in the world so the
only thing that I care about there is a
common interface that I call into and
the goal of the service locator parent
is to help me find the correct interface
to achieve that job so let's take a look
at the situation as it is for example we
have some Class A which can call service
a but it can also call service be and
for this class to work this class has to
be aware of both services essentially at
the compile time so when I compile a
piece of code what I need to know is
which are these services and essentially
if I change service a it's very likely i
will need to change the Class A which
might in turn trigger me to having to
change the service B which is what
tightly coupling is all about so let me
actually show how this tight coupling
looks I will do the demo afterwards
since I have to go through the slides
first I was just the very few slides
left so the solution to this problem is
to introduce a locator in between so my
class instead talks with the locator it
doesn't talk directly to class a or a
sorry service a or service be so it
calls the locator the locator locates
the services and then my class just
continues working and if anything is
changed I actually never need to change
service actually when I change service a
or service be or I introduce service see
my class a should stay the same I
shouldn't touch Class A which means my
nav code stays the same so and now I
demo the solution so I go back then with
the problem and then I demo the solution
okay I my life kind of okay so i will
start nav i'm going to synchronize the
employee table and it's going to be very
very basic example okay so here's the
employee table which has some employees
and here i have added two actions first
action is called sync employee data
tightly coupled the second one is sync
employee data decoupled so when I click
either of them both of them do the same
thing essentially they synchronize the
data so when I click that what happens
essentially what happens there is that
my nav web service integration code unit
is invoked so let's actually take a look
what this code you need us I have this
service thing it's essentially a dll
which contains proxy classes for the nav
web service and inside of this class
what i'm doing i'm going into
essentially the same database just
another company in reading the data from
there but how am i doing that i'm doing
that in this way so I first instantiate
this service directly then I set some
properties directly and then I retrieve
the employees and the problem with this
this employees class or actually this
array of the employee class is that it
depends on the service it's the service
who tells me what I need what the data
is so if I take a look with with f5 this
employee actually has properties that
come from that external service I might
not need them so imagine that a property
change its name okay suddenly my code is
broken it doesn't work anymore because
the property that my code is aware of
doesn't work anymore so you change
service you have to change this code so
that's one of the problems second second
problem is that I'm
of course tightly coupling practically
the whole thing the data collection and
the data model itself so both of them
are tied tightly coupled solution for
that would be a bit different so if I go
to visual studio I would start it would
be a two-step process the first step in
this process would be to actually
decouple the data model first so I'm not
I don't care if this target system has
70,000 fields in this employee class
what my database cares about or my
solution cares about is maybe just these
seven fields nothing else so I expose an
entity class which contains only those
fields that I am interested in I don't
care about other fields and I don't care
if the fields have the same names or
whatever I just care that these are this
is the entity class and I'm going to
operate on this entity class the
complexity of the actual implementation
is hidden away from me the second thing
is essentially wrapping the original
service into a rapper and this rapper
has one single method which returns an
array of these employees actually entity
of array of my entity not their entity
which was nav entity and essentially the
only method which is relevant is this
get employees however this is not
decoupled enough so the next thing I do
is I introduce an interface so I declare
an interface which is called I employee
integration and this employ integration
has the only thing that I really care
about which is the method which gets the
employees so my nav code is going to
talk to the interface not to the
implementation of the interface so I
don't care how the employees are
retrieved I just called call this method
and then next step would be of course to
simply implement that interface so
essentially i implement this i employ
interface on my class in the future if I
have another like file system
integration like somebody's shipping
files to me as a CSV file I create
another class we
should I call file system interface
again I implement the I employ
integration again I have get employees
which works in a different way than the
original one it knows how to handle a
different system and then I call that
system and in C al I have this service
locator I will take a look at that later
this is the decoupled invocation of the
service first okay this employee delete
all is just there to show that stuff is
really happening instead of
instantiating and connecting directly to
the service I'm invoking the locator and
I'm asking the locator get me the
interface and I just pass the interface
this I employee interface to the service
locator and then here I invoke the get
employees method on the interface if I
take a look at the interface class it
just has that method nothing else but I
know that it returns to me the array of
the entity that I'm interested in this
one my entity okay and essentially this
piece of code works regardless of what
is on the other end nav file system ASAP
crm whatever and then let's take a look
so here back in if i click this sink
employee data decoupled let's take a
look what this service locator is doing
so i'm going into the service locator
essentially i'm going to human resources
setup and i'm checking okay what kind of
service am i using am I using employ
integration type or am I using sorry
navsari web service or file system so
let's switch let me go into the human
resources set up and let's switch into
the file system integration ok so both
of these methods here the web service
integration thing locates the right
service for me it sets specifics for
that service okay so in the very worst
case this is the part of code that i
need to change it can be automated as
well but it will be an overkill for ten
minutes in this presentation which I've
already overdue and he
here is the specifics for the file
system so it goes to the file system
loads a CSV file and then feeds the data
so if I click sync data decoupled it
essentially reach data from the file
system and integrates them and I didn't
have to change a line of code in in in
CL for example if I want to go with on
with a different kind of interface all
together thank you okay let's wrap it up
I want to have a couple of minutes for
for Q&A I'm afraid that's going to be
tough but we'll try to do it anyway and
we'll we're prepared to stay after so
looking better back at the last couple
of years we achieved a lot we have got a
lot of things in in the in the
application just a few to mention
expanding and collapsing functions
longer function names automatic
population of variable naming for those
of you who were here last year you might
have hear me talking about data
dictionary this is like a very tiny
version of a data dictionary but it's
better than having nothing i'm really
happy happy with this with this feature
we got automatic merging we can start
thinking about delta files so there's
actually a lot of things that that
started happening in the last last
couple of years that doesn't mean that
we are happy with where we are we have a
couple of wishes that we have a couple
of them michael already talked about
this morning for each easier integration
there's a couple of things that are are
harder to reach and we know that like
enumerators or reducing coat loading one
of the things we want to elaborate a
little bit more at
moment is a connection to TFS TFS or
team foundation server at the moment
it's kind of a moving target if you
start talking about doing a versioning
repository it's kind of difficult at the
moment to make a decision if you go for
TFS or get it is a really cool way of
doing your repository it integrates with
with physio studio but team foundation
server has a great UI it allows you to
to create tasks it has Kanban board and
and what have you and if you have if you
went to to look for session last year or
you visit you viewed one of the online
videos about that certain Clemmensen did
on Team Foundation server you will have
learned that there's actually nothing
standing in the way of you starting to
duty foundation server today there's a
perfect methodology you can use you can
start implementing it but we would like
to take it one step further and the
comparison we prepared for today is
basically again going back to the to the
upgrade if you look at the development
environment there's a drop-down list
where you can start the data upgrade
this helps you because you don't do not
have to go to power to power shell
necessarily but basically it executes
the same code as the power shell is
executing so we have a whole bunch of
PowerShell command 'let's that do the
upgrade and we call the command 'let's
from the user interface in the
development environment we think that we
can do exactly the same with with TFS or
get and actually you can do it today
there's nothing preventing you from
doing this we have a whole bunch of
PowerShell scripts you can actually
script the integration with powershell
and script your way through integrating
stuff with with TFS but we think it
would be nice if we if we do that you
can do it Microsoft can do it
that if we take it one step further if
we do it in the development environment
like we do with the with the upgrade so
that we have a true TFS integration in
the development environment we think it
will help partners adopting TFS because
it's part of the user interface like
it's in visual studio without having to
invest too much in in it because you can
already do it today with with the
PowerShell wrapping up we are doing
workshops we have a whole bunch of
workshops going on in Germany the
Netherlands Belgium I've been asked to
go to India and Japan we're going to
workshops in Ilana we want to get this
out as much as possible we want to talk
about the design patterns we had the
class yesterday we also talked about the
PowerShell and we think this is a great
momentum where everything comes together
the design patterns the upgrade code
units and the PowerShell all really ties
in about how to write repeatable
software and how to really start
reaching this multi-tenant 10,000
customer momentum there's really nothing
standing in your way anymore so I would
like you to leave with a quote it's my
quote a pressure professional partner
channel deserves a professional working
environment just think about it I know
it can flip into two directions it can
say something about you as a partner or
it can say something about a
professional work environment it's up to
you what what you want to think about it
so partner ready software it's you it's
us partner already software community
this is all what we could think about in
the last couple of years as a
methodology and I would really like to
urge you to start using it start using
the methodology and start getting these
multi-tenant installations going
questions I would like to have my fellow
partner in crimes to come with me and
help me asking the question answering
the questions
which is give these ones away too we
have a whole bunch of t-shirts for
anyone with questions I don't know if
they're someone made a microphone
running around we repeat them I can't
see anything with the lights one here so
any question I'll go into microphone in
front of their just a second it's coming
microphone here and I would like to hear
what the reason was for putting each
method in a code unit on its own base
basically encapsulation basically to
have to not pair two methods together in
the same object but be able to treat it
very independently in a very
encapsulated way if you have two methods
which would do different things in the
same code unit you have to global
functions and it's harder to
differentiate that also if you put it in
one code you and you can actually have
access rights for each individual method
each individual action just by defining
them on the code unit there is more to
that but probably not more time that's
another question up in the back
microphones going out there i also have
a question regarding caught units i
often have the case that i need one
issue one method about in different
variants like overloading a method and
dot net what are your thoughts on that
how would i mutter something like that
maybe a loving function with multiple
variants for over and
my parameters I yeah please Michael
overloading is a good idea I already
bailed out okay but there's aunt Bogdana
has a design pattern for that uh there's
a design pattern that you can use for
that we're going to talk about it
tomorrow at zen pattern session but
basically you want to overload meaning
that you want different arguments for
your function so if they are not records
then just put them in soil into a table
so then you can put whatever you wanted
to the table and then you change
function behavior based on what's in the
table that's you you have a table that
you never populate with data just as an
argument stable is that what you're
saying that's right yeah ok so the
arguments design pattern is a way to do
that you have specific arguments that
are valid at one time and not valid in a
different context you just pass that
argument stable on and real overloading
would be nicer but that's that's our
work around for that make sure your
claim your t-shirts in na na na V you
have security based on table when you
use generic key how do you manage the
security so I guess that's one question
for me on security yeah the many of
these these tables are typically things
that I quite widely used across the
database so if you have like comments on
a customer and vendor and you don't want
him to be able to modify security on the
vendor you can use the security filters
they work perfectly fine than that and
you can actually limit that that he
cannot because the table IDs in their
part of my of my key so that's the
easiest way of doing it I'm sure piers
any I don't know if it's in here but I'm
sure easy security also has some some
great ways of fixing that and also the
the common thing is just one easy
example that everybody can
stand quite easily I even find that the
tags example yeah even from a business
point of view much more interesting and
there you don't have the security issues
because you want people to be able to
search across the whole application
exactly what to target it's like I mean
it's just one way of implementing it
there's so many examples out there where
you can just use this to really create
generic functionality that can be
applied everywhere and I mean comments
tags it edible feels you can keep going
documents pictures you can attach to any
record you can keep going as tons of
things you can do to the applications
where you really can make it generic and
not always is that its security really a
big issue on many of those areas some
questions over that's a question Oy okay
I'm going to Gary you told us that it's
better to do the functions of the metals
directly in the tables and I remember in
the past there was a maximum possibility
of doing fields in a table is there also
a maximum quantity or a number of
functions or methods in a table or is
this without the maximum there used to
be the case but there is no maximum
anymore not as far as I know and if you
have like 2,500 methods for one agent
that's probably something wrong with you
wrong with the architecture anyway I
have not run into any sort of problems
now so I don't think that is an issue
okay thanks if you have one global a
function in the rest local how do you
unit test your application out actually
more seed the other way around it's the
you you only hit that code unit through
through this through this a method
header and then everything is done
inside that method you test the result
of the optimum of the method that that
you execute I don't think that that
there is really an issue here would you
believe that there is an issue
in unit testing no it depends on the
structure of the code so if we take a
look at those method code units
essentially every method is atomic it
needs to achieve one single task like
complete and action and essentially if
you're testing unit testing those
actions then you need to test them as a
whole and those smaller functions which
belong to that let's call the method
code units those local functions in
those code units essentially you you
would I could agree you might want to
test them independently but there might
be no use of that because constructing
the context for proper unit testing of
them might be difficult and then again
if you're testing repeatable stuff which
which is called from multiple columns
then you wouldn't have duplication
anyway you would put it in another code
unit so this design pattern doesn't
imply that everything belongs there you
will still have common code units with
common code that you don't duplicate
around and you would unit test that code
so that's how I would approach and
that's that that's actually correct I
mean you it's the smallest bit of
process that you test you don't test a
get customer just because it belongs to
the process you do that all over the
place what you test is actually this
specific method and if the method fails
then everything fails you should look at
it as as the smallest unit of that you
do and and the the local functions are
really just helping to establish that
that sort of method well I think I I say
thank you to whoever asked the question
because it does open some questions for
us so it really I mean we have we have
now answered but it doesn't mean this is
the ultimate answer and that we are not
going to think about that because it is
a valid question you need to come back
next year as well so we have to excuse
me you're usually in a project we you
know we work more than two or three
developers and you know everybody end up
sneaking his own methods so how to
document it should we do it in a table
level or we have to document in the
unit code oh you have to document
everywhere sir and I would say that's
your domain and I'm not sure I
understand word document how what do you
mean with documenting like why we
created this method what's the use of it
because every developer hack create
their own methods you know when they are
doing customization yes yeah and I think
I think one of the biggest things that
we are missing in the community that is
we're missing to do proper source
control proper product management of the
system if if you have a bunch of
developers doing each their own thing
then I'm pretty sure you're missing some
product management that we need we need
to go away from from the thing of you
know we need something can you go and
make me something and see then come back
in two weeks but maybe that's what I
need maybe it's not what I need we need
to change the way we think about
development development stop doing our
individual things sit down figure out
what it is we need figure out how we how
this should function in the bigger
picture before we even start putting one
line of code into the system you
normally you would have a ticket or a
work item if you think in the TFS which
defines the business case and then you
develop against that and then you end up
with having the code and the Delta and
and with the business case all in one
place that you can look up I know that a
lot of us don't work that way and
especially not in the if you have to
hurry in a project but that's actually
how it should work commenting inside
code for us is actually only workaround
by commenting your business logic inside
objects should it's just a workaround a
question about Delta files I would like
to ask what kind of differences contain
Delta fights because all examples that
you show the include only
fields differences in fields doesn't
mean that it includes only fields
differences or also functions and now
the Delta files contain all the
differences so it also contains
differences in encode it contains
differences in in pages if you add
elements if you remove elements it's
basically a complete new way of
describing documents so that's that's a
good question i actually don't I had I
it doesn't know so I figured that so it
doesn't contain the deltas for the
reports that the reports I would I would
approach in a different way I think the
fact that we can have different layouts
on top of one data set is a great great
asset and I really hope that if if we
create one data set and have different
layouts on it that I really hope that
that dramatically reduces the
possibility of us ending up in in
merging you can basically if a new
software version ships and you add
something to the data set that doesn't
mean that the letter layout breaks so I
think the necessity of merging layout is
not as big as the necessity of merging
merging code but it's a good question
thank you I think okay one more not more
Leone almost 15 minutes overtime this is
enough technical question mark you
mentioned about your book okay yeah I'd
like to learn more about what I just
heard over the past hour and a half is
your book what is your book about this
where can I get it and so on the book
does not simply cover PRS methodology it
Maps the functional areas of nav and it
actually contains a whole bunch of
design patterns it does include natural
language programming
and hooks so it's basically a
combination of PRS and development and
architectural best practices and the
other the other answer to the question
is Amazon you can acquire it at amazon
or expect publishing thank you
