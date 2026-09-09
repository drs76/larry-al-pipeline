# BC TechDays 2022 - Advanced topics in test automation

- **Source:** https://www.youtube.com/watch?v=LJp0s9jm3KY
- **Video ID:** LJp0s9jm3KY
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 97m40s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

foreign
ladies and gentlemen welcome back to
room nine for the second day uh the
first session will be Advanced topics in
test automatization giving you by look
from the Witch and Nikolai kukrika thank
you
[Music]
welcome everybody good morning
um a session which I invited Nicola to
join me in and
like let's say kick ass a little bit uh
it's five years ago I had a session here
on test automation at that day with
James Pearson
um let's say at that time more or less
most of us started or had to start a
journey with test Automation and today
we want to address a couple of advanced
topics it's a collection of things
um maybe some do not relate to the other
but I think it's enough to help you on
to the next stage and if you still need
to start somewhere low well there's
enough to find so for today we're going
to talk about a number of advanced
Topics in a bit of a stretch what are
good tests why do we do the test what
about demo data how about gold coverage
those kind of things and in the end with
test automation it's about being more
efficient and we'll kick on that a
little bit good test what are good tests
that's always a relevant question let's
see what we come about with and at the
end a number of things how the on how
the internal test tooling at Microsoft
Works and how that in not so far away
future will help us a little bit more
probably so
Nicola
yes so hello everyone you might know me
from yesterday as well I'm from the
Microsoft and one of the areas that I'm
focusing on as well is the test tooling
on the application side
may be also known
some people call me and then they say
whatever I look about
um test automation your name is there so
I'm the mafia of the test automation
welcome to my and one important thing to
say that you might not know is that many
years ago I think it was like 14 years
ago Luke and I were both working at
Microsoft as test Engineers back then
yeah so yes and never met at that time
yes we didn't meet each other at that
time yes
so why why test automation there's a lot
of things around this you could put it
under the name best practices risk
management tools code coverage whatever
a couple of things we're going to cover
but maybe it's useful to ask the
question why not test Automation and
actually that's also the way I started
in the book of
when I started to write a book the first
version years ago often people would ask
me why should I and one of the things
that comes around as the first reason we
don't have time we don't have money
related to that and a lot of our other
arguments on the other hand I mean
don't we test
and what's the difference being between
manual testing and test Automation in
the end so
it needs to save you correct time and
money absolutely so the test automation
the main point of it it needs to save
you time and money and if you remember
from Luke's lights it wasn't that
visible because people usually don't
think of it like that
and if people are surprised when they
hear this sentence the argument if it is
not saving your time and money you're
probably doing something wrong
and basically I can also logically prove
this sentence so here is The Logical
proof so if you decide to code a new
feature for example you have two choices
either to test
or
to do no testing at all right because if
you believe that you can write the
perfect Chords it's going to be fine
right
for testing you have again two options
you can either do it manually or you can
do it through the automated testing
automated testing come in the form of
test streaming development you have
heard about this one essentially it is
going to help you to write the code that
executes correctly
and acceptance test driven development
you have also probably heard about this
one it ensures that you write the
correct quote
the difference between the two is that
you can do a perfect code and then the
customer or the program manager says
this is not what I wanted right and then
he didn't achieve anything
so the idea is that you sit together
with them and you define the most
important requirements in the given one
then form which will form the most
important scenario tests that you can
automate
manual testing comes again in various
different forms and many people believe
that they can replace the manual testing
by automated testing completely in
reality you will need to do it on the
only question is how much because there
is no replacement for human eyes
and whenever you test any product you're
going to find a few bucks
and the biggest benefit that the manual
testing is bringing is that you will see
that the scenario maybe doesn't make
sense anymore or there is something
wrong in the UI and similar things
now for the last option and the good
news is that there is no such thing as
node testing
the good news is that the software is
going to be tested so if you opt for
this option you're saying we are
comfortable with end users testing our
software
and this methodology is called screen
driven development and it's not fixed
until the customer stops screaming and
why do they really plan their testing or
not yep they will test it they are going
to test it anyhow so
on this slide you can see all of the
approaches that you can do for testing
the new feature and
now my argument is if we could write
perfect code we would not need to do any
testing and if you would be more
efficient with manual testing there
would be no need to do the automated
testing because why spend time
so when you hear somebody saying no time
and money to write tests please correct
them
you can say to them what you mean is
test automation is maybe not needed for
this feature or you believe that you can
get away without writing the test for
this specific feature
and this may or may not be true however
the problem is that if you do not
automate your building a debt
on the business Central side we have
more than 30 000 tests for the
application I think it's 35
000. or something something like that
and much more than 80 000 platform tests
this was the number five years ago we
have also written the dedicated tasks
for UI rendering kpi scripts low
performance upgrade testing and we are
doing also specialized testing and the
truth is we do not have enough we still
have some areas that we should automate
and you can also quote me on this one it
wouldn't be possible to ship a product
like BC without writing automated tests
yep and I can mentioned this one before
skipping the test automation is building
that that may or may not be repaid
now the reason why people perceive test
automation as additional work because it
actually was
because back in the days in the 90s most
of the test theory was developed and if
you remember we were shipping software
on the disketts CDs and DVDs and the hot
fixes were extremely difficult to roll
out you would need to wait for the
service back one and then you would need
to go to the customer push in the
diskett for a CD and install a fix
and Microsoft was estimating that for
each buck that would hit for example a
Windows it would cost between 100 and
200 thousands of dollars to fix
so it was a huge cost
so it would pay off and we would save
money if we would do extra testing
today the picture is completely
different it's not anymore on a single
box we are running on many platforms and
this is a picture I think from two two
years ago so you can see that BC is
running on Internet Explorer iOS Android
various different platforms we are using
different development and methodologies
we are connected to all sorts of kind of
services and the system is pretty much
in flux
so any of these components can break
so easy hotfix rollout is a must for any
modern service and this one is going to
drive the cost of the bug really down
and for us the early detection and
Telemetry and the disaster recovery it's
also a must for modern service because
you could have security breaches
something can go wrong and the whole
point is to minimize the impact of each
bug so the customer does not screen
that's the entire point and of course we
all should realize this is not only the
picture from Microsoft maybe in our case
your case it's a little bit simpler but
the complexity of being part of these
365 making use of Office 365 whatever
that complexity is also ours correct
so to end the answer I would like to ask
you to follow this rule the only
document that you should follow is not
to follow any Darkness if it makes sense
so you know your product the best you
know where the risks are you know what
the Integrations are you should see what
works for you do the thing that makes
you the most efficient and try to
minimize the pain that we roll out to
the customers
okay good test yes what about good tests
now this is a large topic so we'll do it
part by part then we will also show you
some of the advanced topics while we're
doing it sure
so so the good test the most important
thing about them is the they cover the
risk so
to show you this one to visualize it the
risk is the thing that would keep you up
at night right so you wake up at the
tank night and then you remember that
you have a good test Automation and you
can go back to sleep
this slide was shown to every test
engineer at Microsoft we had this
getting started with testing and they
were telling us how to approach the test
Automation and I'm sharing it with you
and they said to us that we should focus
on the impact and probability impact is
how much is it going to hurt the
customer what's the consequence of a bug
probability is driven by the complexity
of the codes or how many Integrations do
we have so what's the probability of the
quote to fail
and if we cover the high impact box we
will not be doing the screen driven
development
thus we can only be done after we are
covering boxes one and two
low impact was recommended that we fix
if we want to improve the quality of a
specific area
so if we would go in and let's say that
we wanted to improve a very dedicated
area we would start automating
and the last box has a question mark
because you should never say never right
there is cases that it will be needed
but the problem is that these tests if
you focus on automating them you will
think you will be paying a high
maintenance costs and most likely they
will never fail
so the recommendation was to avoid
writing these tests if possible at least
to write as little as needed and you
might think that would be one of my
first thoughts so what should I put in
the red box or in the the the the yellow
box or the green box most importantly
thing is that you start putting things
in one of those boxes so that you start
assessing the impact and the probability
of your of the parts of your feature and
what you need to test you will fail
probably will fail but if you don't
start doing this you will never have any
idea what you're doing right or what
you're doing wrong
I mean it's not important to follow the
theory that much but even if you put
that test in a wrong bucket or ultimate
something in a different way the
important thing is that you're driving
it in the right direction
right yeah so
now uh to show you the example of the
test that doesn't add value
many years ago I think it was like six
we had to push at Microsoft to provide
additional code coverage for Country
functionality
and the snippet that you see here is
from Norwegian code and it's called the
generator gyro K ID
and the developer that sit here decided
to do the unit tests so he reads the
code and as you can see it's a
relatively simple code so he decided
that he is going to write unit tests so
the thing that this person wrote was
that he wrote the test that is getting a
sales setup assigning this kld setup
which was in the case statement
giving it a document number and checking
the 0k ID is blank and then P would fail
with the message unexpected value for 0k
ID
and this person did one test
here one test here one test here one
test here two tests here because one is
to test the field and one is to
get to the GLK ID but the question here
is where is the risk
right
because as you can see this code is
incredibly simple and even the
probability of it throwing the exception
is extremely low
also the assert statement brings no
value because what does it mean
unexpected value for zero K ID what is
the expected value right
and in short this code has been cemented
in place by unit test
because each time when you need to
change the code you need to update the
tests and if you would like to delete
this method and refactor you will need
to delete six test methods so it's just
an additional step to do every time
when you are changing the code
and it's very often happening in the
test automation
the correct way to do this a better way
because 0 K ID is the electronic
invoicing in Norway which the developer
didn't know they just read the code and
brought it to the unit tests the better
way would be to test the jroocide for
sales invoices or reminders or even
better to say test electronic invoicing
for private customers and then if this
test fails we know exactly what was it
covering and what is the impact
and it actually brings value
so your unit tests shouldn't go too low
in your code as they call don't test
your implementation but test more at a
feature level or API level correct
so unit tests are extremely valuable and
they should test the complex logic so
good candidates are sales posts General
General post line or match Bank payments
or something like that and you should be
able to test public methods in isolation
but you need to know what are the proper
inputs and outputs otherwise you will
not bring bring any value the test will
not be valuable
and the messages in the assert keys are
the key of the test because the person
that will break your test will most
likely not know what the test is about
so be very careful how these messages
are written we are unfortunate to not
often putting the attention to that one
well I I tend to always put attention to
that to people to say make sure it has a
meaningful message and I'll show some
examples then what I learned is that due
to the fact that I make meaningful
messages it's also already from the test
error I get I often already know where
to fix it what went wrong and that's
actually yeah
then the second thing is that the
testosterone development is all about
getting good interfaces and I got this
recommendation from a more senior
developer than I the recommendation is
that unit test needs to match public
meta description one to one so
everything that you write in the public
method the documentation should have a
unit test and for each unit test that
you have you should reflect it in the
public documentation if possible
and this way you will ensure that you're
documenting your methods correctly and
that everything that is written there
actually works
so like I just said the term unit
testing doesn't mean that you're going
to test a simple unit like the example a
Nikola just showed but the unit testing
means more at a higher level where is
this you could say API interface
definition that should stay the way it
is and that is going to be used in a
scenario bigger part where you're
integrating those things so that's one
thing approach is a bit more functional
anyway if you don't have tests at all
um the advices and the advice is not
just an advice it's an experience start
with scenarios don't start at the bottom
but start up top I mean I think that all
makes sense it relates to what we do
manually I mean you don't do unit
testing manually but you do test
scenarios yeah so cover your more most
important scenarios first the thing is
and Nikola will talk later about code
coverage also is that in that way if you
have a number of meaningful scenarios
you probably will already have quite a
good code coverage yeah and nevertheless
what is gold coverage Etc we will
discuss later yeah and document it in
your code like some of the examples
already showed so
even if it's a few number of scenarios
you'll probably are safe in the fact
concerning the fact that you will hit
probably quite a part of your code
all right
um and then when you're going to
refactor and and we'll get them back on
that also
refactoring is probably one of the as a
developer probably one of the most
approaches that you will profit from
having tests in place imagine that
you're refactoring and then realize how
are we going to test it or who is going
to test it is going to test anyway so if
you want to refactor and
don't wake up at night thinking wait
what is going to happen make sure you
get tests in place and that's what you
could call unit tests because you're
taking up a specific part of your code
okay and we can move to the first demo
of the today and since Luke has
mentioned scenari test so I'm going to
show you how you can do the tdd
development in the application
and no sir
there is a little bit more talk yes I
got the question from one Partners is it
possible to do the tdd in efficient way
in BC and actually these stories from a
while ago because it was happening in
Sea Isle but we will do the reenactment
today in Al
so when I joined the application team
my manager came to me when I was done
with the task and he said you can pick
up this box or a new feature what would
you prefer and of course every developer
would say new feature right of course
and I was thinking it was a very silly
question right because I mean what's the
point right
so
then I have opened the code that I was
supposed to extend and when I was
reading it I realized it's an MC Hammer
code
yeah MC Hammer if you haven't heard
about MC Hammer code it's a code that
you read and you say it's so bad you
cannot touch it right it stays in place
so don't touch it don't touch it right
and it had tests to be honest right but
it was one of these end-to-end around
the world test that would take 10
minutes to execute it had around nine
steps and the problem with them is that
first of all it takes 20 minutes
it's extremely difficult to do debug and
often if it will happen that step 8
would fail over seven only because the
failure was at step three step three did
something wrong the bug was there and
then the step seven would fail it would
be impossible to debug so these tests
were not useful at all
so after trying to refactor it for
around the day I was basically raised I
mean he wasted the day of work right
because I didn't get anywhere
each change that I would do with regress
to different area and it would not help
and then I have remembered a topic that
was called working with Legacy code
which recommended that for the Legacy
code you should introduce good scenario
testing and I have written the good
tests like this
and now I can
just run it
and the scenarios are going to be
running it took me approximately day and
a half or two days to write around 30
end to end tests so 30 dedicated
scenarios
and yep the tests are running probably
it's a bit cold so let's see
okay and it took 22 seconds to run 30 40
34 scenarios
so if you think how much time would it
take for me to run this manually it's
huge
so now with hurting fingers yes
now if I would go to the code right
and now I see that this method does
something but I don't know what does it
do exactly
and I have two functions which are very
bad and they're not needed probably
so I can try to do the refactoring here
right to delete it
and now if I say publish without
debugging
now I got it updated
and now I can say run tests
and now I can see that it wasn't a good
change because the tasks have started
failing
so basically by doing it this like this
I'm getting a response if my change was
correct or not and because the tests are
testing a single thing I don't even need
to debug because I can see which
scenario I have regressed and it is
helping me to build a mental picture in
the Legacy code to which scenario the
code is being connected to
so basically then I can go back to the
code
and undo it
and then delete this one here
and let's publish again
and then when you go back to the toe and
you say run tests
they're going to all turn green at the
end because this change was correct
so
the way how would you actually refactor
the
code that looks impossible to refact
refactor is actually by doing one small
step at the time in a correct direction
so you should be chunking it bit by bit
and improving the quality of the code
and this is where the good scenarios
that are quick and fast to execute come
into the plane
now one thing that I would like to
mention before moving forward is that
for the extensions there is a really
nice test Runner that was done by James
Pearson that you can use to run the
tests within the visual studio code so
if you go here and you would like to run
the tests you have the option to run
them without using the UI page
yeah switching switching
now of course this approach is not
applicable for every up for every
feature that you're working on but we
will also show you some of the cases
where it is extremely useful to do the
test stream development
yep so if you've seen the how important
it is that the test is fast to execute
easy to read and to test one thing
because if you're breaking these three
things you cannot use a test for the
test driven development
many people ask us can we put numbers on
faster execute and the answer is yes
so here are a few suggestions a single
test should not take more than two
minutes because then you're waiting for
it to finish
according should not take more than five
minutes and we suggest not to have more
than 50 tests in accordance
then a test extension should take
maximum 30 minutes
yes sorry I'm not right
there are a couple at Microsoft side
that takes hours
yes so if you try to run for example
test CRM is going to take around four
hours and the reason for that is that we
are not running tests per extension we
are running tests in ranges
so we have batch test DRM in like 30
minute runs and test DRM I believe is
one of the candidates that we should
refactor it's a no I'm not going to say
it we are planning to split it into
smaller extensions
the message of course here is uh and and
it's have been said in different ways
but to put it straight it doesn't make
sense to have tests that long have a
long running time yeah precisely because
you as a developer actually that's what
uh Nikola just showed once you get test
Automation in place it's not a matter of
a pipeline running it after a pull
request or on a pull request or at night
you should be running it already while
you're developing it and when it takes
an hour to run it you will not sure
that's logical but if it takes a couple
of minutes you can check your code and
continue yeah that's actually what it's
about but even if it is running as a
pipeline if it takes 10 minutes it's
going and it fails right it's going to
be extremely difficult to debug and to
see what's wrong yeah okay one of the
issues with long-running test extensions
is and code units is that you will get
more issues with Singleton code units
since as long as the UI test page is
open we are not resetting automatically
Singleton code units so you'll get state
issues as well
now of course you will need to write
long running methods from time to time
and our suggestion is if you write these
test methods mark them as long running
and move them into the separate test
extension
so
now single instance test code units in
general is very difficult to test
because it is living as the UI page is
open and I would recommend that you
clear it from the initialize method if
you can and of course to try to avoid it
as when possible
with this mentioned we are going to move
the test should not modify the
environment yeah and this is the most
important part of the modifying device
of today no no something I often
encounter when I'm doing workshops or
whatever we come from a background where
we have a database with data in it and
we might say we need customer data to be
able to verify if the thing is working
and actually let's say a good test
practice always starts at the same level
of data now the thing we all know a
support goal they have an issue you try
to reproduce and you count why because
you have a different data set up and
it's very difficult to find out and then
you could say yeah but how do I know how
to set up my data for test automation
yeah that's part of the deal that's what
you need to find out so if you run your
tests whether using the old test Runner
test the Cal test Runner or the AL test
Runner the default setting you want to
use is that you run your test in
isolation on the AL test Runner you see
at the bottom and in the in in the
inside it's now moved up top what test
Runner is used and there are three
options three flavors and the first one
at top is the recommended one is that
you run your tests in isolation level
per coach unit at the end of the coach
unit the garbage is collected you could
say it's cleaned up again and you're
back at the state where you started when
you started running the code unit the
one at the bottom is often asked per
method it's called function as as a
value is that it will do the the roll
back after each stat method but as
written that is quite a Time intensive
so your test run will slow down don't
use it and you could say well but then I
need to take care of data that is going
to be there due to the first test and
then second test it's in general very
easy to write tests that don't conflict
yeah so so if
if you find that difficult and that
could happen but I I can guarantee in 95
99 of the case you don't need it you do
need sometimes the one in the middle
that you don't want to have test
isolation so that the data sticks in the
database we'll get to a couple of
examples yes that is really specialized
testing yeah but that's the case it's
only 200 300 tests yes and that's the
case where two processes let's say your
test processes process triggers another
one and yes
the one is in isolation and if nothing
is committed the second one will not see
the data yes but there might be a need
that you need to put an individual test
to roll back after it's done yeah and
I'm going to show it now because we had
a property which was called
transactional Model outer rollback
property
and people are asking us when should we
use this property and how does it work
and my no not to say Never Say Never but
this time I would say never so and to
show you what you can use the problems
with it and what you can use instead
is like if we prepare the code so you
can see this test is using the
transactional model property so if you
search how many usages do we have in
Microsoft tests
you can see it is View
thousandths yes so there are few
references that I need to refactor when
I get back to Microsoft so we are
unfortunately using it quite a lot
and one of the problems that it is
causing is that the initialize methods
cannot commit
because as you know this part before the
is initialized is for every test
and this is per code unit
and if you throw an error this second
part is going to be rolled back right
so I would need to write a commit here
right so I prevent the rollback of the
Paracord unit setup
but if I do that
the outer rollback test is going to fail
because it is testing that no commit is
happening within the scope
and this is not the thing that you
should test of course because what is
the point of testing that no commits is
going to happen
it might have some sense in the past
while we were still in CL but nowadays
when we have events and extensibility
commits are going to happen for sure so
it is much better to be defensive
and the question is how should I
refactor this test and the answer is
it's rather simple so the thing that I'm
going to do here is that I'm going to
put it like this
right and I will name this one test
and I will delete this property here and
the thing that I'm going to call of
course first is that I'm going to move
this initialize method up
now I'm going to call this thing right
after us
and now you want to roll back the
changes and ignore any commits that are
happening within the scope and to do
that we have a new property which is
called commit behavior and you can say
ignore commit Behavior
and then ignore
so if you mark it like this any commits
that are happening within the test
methods are completely ignored
so it's not committing at all it's not
committing at all
then the thing that you can do is that
after this thing is done you can do the
search blank error
to roll back
and clear
loss there
and that's it
if you are worried that your code that
you're testing is going to be
interrupted by the commit my
recommendation is to decorate that
method that you're worried about with
the same property and then the commits
are going to be ignored it's much better
to prevent it from the code than
actually to cover it with the tests
okay
now
you can see that very and Luke is going
to show this one in a few moments you
can see that we are using a lot of
manual binding in our tests and we do
not have I hope any static automatic
subscribers
and the reason for this is that if we
introduce the static automatic event
subscribers in the test code for testing
purposes they're going to change the
environment
and they will affect the other tests
because it is there also if you want to
test the scenario manually through UI to
see if it is a test defect and how does
the UI behave you will again need to
uninstall the test libraries so for
these reasons we are using the manual
test subscribers
and now Luke is going to show you how we
are using them in the mocking topic yeah
the topic is a bit wider you might know
the term mocking you use it for mocking
screen and requirements mocking is in
this context used for replacing a part
of the real code by what we call a mock
actually mocking is a very specific way
of doing it the overall term is test
doubling in parallel to stun doubles in
in picture movies so what is this about
and we'll get to the subscribers again
with mocking we want to actually control
the code execution yeah so change it if
you're going to call upon something
that's not in your control like an
external service you probably don't want
to test that the service is working and
get an error because internet is down or
whatever you want to be able to test
your logic so with mocking we want to
control the execution flow and we
introduce a stand in that is going to
replace a part of the real code and
that's what we call in general terms
test double mocking mock is one you
might have called of a heard of the term
spy a stop dummy there are different
ways of implementing a test double yeah
so we want to mimic the real code so
we're able to let the flow continue and
have it showing that your business logic
is going to work or does work right yeah
so and on the other end by the way
tests should be fast if you need to wait
for the service it could take longer and
with a mock you take a shortcut and it
can be substantially faster that way
yeah so the test double is applied to to
replace the call to an external
component like a web service now you
want to be independent and one of the
things is not only the fact that it's
maybe not there but
you want to only validate it but it
could also be that it's not there but
you also have to pay for the service so
let's imagine that you have a call or
you have a number of tests that's run a
couple of times a day maybe adds up to
100 times or a thousand times calling
the same service and you're having to
pay for it apart from the fact that
maybe the other side that is the
provider to the service is maybe not
happy maybe feels like having a kind of
DDOS attack because you're all the time
calling up on their service yeah so
that's something you want need shoot
prevent yes and one thing that I would
like to add here is that you should
never test against the live service with
automated testing because there were
examples where the companies were handed
really large bills because they have
incurred the cost on the service that
they were testing it doesn't mean there
shouldn't be any automated tests doing
that but let's get back to that later I
would recommend yes we will cover that
just to be more precise manual or
semi-automated testing if you want to
test against the live service
so what I already mentioned test
automation should be fast and I'm not
going to elaborate on this last part but
you could use mocking also not only for
replacing a part in your process but
also you could mock data so if you have
a report that is going to aggregate
Ledger entries whatever they are it's
not needed that you build a whole
scenario from a sales or purchase
process leading into the to those Ledger
entries no just feed The Ledger entry
table with the right records there's
nothing against that you're testing the
report you're not testing The Ledger
entries okay so an example you can also
find it in the book there is a feature
in BC called vat registration number
validation there is a EU service for
that and actually what is done is that
it's going to when you enter a vat
registration number a customer
card it's first of all and that's an old
validation and validated against the
format defined in the country region
table but next to that if the service
and you can see it's now disabled on the
left side the check mark or the the
slide if it's disabled it's not going to
call it but when it's enabled it's going
to call that service the blue box on the
right in the middle of the two others
that one is actually calling a certain
code unit and that's going to call upon
that service what you would like to do
is to test double this thing so if
you're testing this feature that's what
you would like to do however it's a bit
a bad example you have no way at this
point in time to replace it yeah there
are some other ways to to work around it
but you could replace there was a a URL
an endpoint defined for it you could
maybe replace that one the question is
does that give you security issues or
not but nevertheless it's not a good
example and
the thing is is what we call here it's
not a testable code you have no way to
control the code flow from coded tests
that's what testable code is about and
we could talk a lot around it testable
code leads to better
decoupled code Etc read about it in the
book The Focus here is how could we do
this I give you a couple examples of
what test doubling means actually so in
this case a bad example I have no direct
way of replacing it yeah as I mentioned
we could replace the end point but let's
not do that this example is not was not
written with testability in mind and I
think
I shoot it and I'm probably still doing
it I'm not sure but I reckon that most
of us are not taking testability in a
consideration when writing their code so
this is a kind of call
try to think about is how could you
write your code so it's controllable
from the test code yeah so
as that said so testable code it allows
you to have full control on it and what
we call it has no direct dependency
dependency on other code yes you
probably and in my example that's what I
will use and maybe not as first the best
but the simplest example as it relates
to how we have been doing it if you have
if we have the possibility to point to
that code unit instead of that it's hard
coded in the background code unit dot
run and actually this is code unit 248.
it would be nice if we provided a
parameter where this ID could be
replaced yeah so
in that way we Loosely coupled the thing
and
that makes it better manageable from
testing perspective and in the end the
the experience is also that if you have
components you can test the components
if you have one big feature which is not
componentized you're always testing the
whole big thing in the example of uh
Nikola there's a whole long a bunch of
steps to be done and something fails and
you don't know you have no way to easily
find out where or where the course was
of the eventual failure so in this case
as an example a simple one a simple
approach I think we all know this
provide the idea of the code unit as a
set of a one yeah there are arguments
against that but as a simple
understandable one this allows me to
provide a pointer to another code unit
in this case it's a code unit what was
the number eight sixty thousand hundred
and eighty eighty ninety eight which I
call something mock it's a it goat unit
which has the same interface actually
our coaches have been interfaces forever
already that on run trigger is the only
method of a code unit and this one has
also a non-run trigger like the other
one so I can call upon it yes the one
thing that I would like to mention as
well look if you can go back to the
slide yeah is the fact that you should
be careful if you're following this kind
of example the 80 registration number
service could be okay to be done like
this but the service is like Shopify is
probably not good to make the URL or a
code unit configurable
because then if the BC is exposed and
compromised then there is also a Shopify
that is exposed and compromised because
they can use the setup tables to change
the urls
so the user might think that they are
calling Shopify but they're calling
something else yeah and I'll I'll use
that you can use it for the services
that are not sensitive yeah yep
so what we do actually all want to
achieve here is that we have the
possibility to replace the call to that
code unit buy another one yeah and as
Nicola said it's not the way to do it
there are other ways to do it so have a
look at that one
um
just to show you on the left side it's a
kind of condensed version of 248 plate
on the right side that's my mock
actually an on round trigger which calls
a function that creates in the end a
Json
formatted text which is returned to the
call and that's enough it's just saying
I've got a valid response acting like
have it did connect but it didn't this
is a valid response use that one and
continue with your Flow by the way in
the example I also have a unvalid one
which actually returns a empty response
yeah so
this is what we call dependency
injection so you allow the code you set
up the code in such a way that from
calling it by other code like test code
you're able to replace the component
with another one yeah in this case you
could say with this code unit if
although it's not an interface
implementation as we wrote node right
now but it's actually also an interface
we replace the one unrun implementation
by the other one that's what we call
interface based injection
so a simple one is this one as I already
mentioned but we could also do it with
real interfaces like we could Define
the Nino and let's say the one at the
top is the enum implemented by Microsoft
or another party and you're going to uh
want to test that yeah doesn't matter
you need to test that one you can hook
in by providing an enum extension on
that enu so it defines another
implementation and as you can see the II
phase is the definition of the interface
and then and the extension which we
which will be part of our test extension
it will extend the enum and point to a
stop implementation yeah and yes in code
you use a Setter to change by the way
you don't need an enum implementation to
be able to replace an interface yeah so
being able to call that in this case set
interface provider you can hand over as
a parameter another one a one that
you're going to link to a new
interface
and to the test or the using event
subscribers and tests there are two ways
by the way you could put your event
subscribers in your test coach units and
then you need to set your test code unit
that you're not doing using the static
instancing of a subscribers but that you
do the manual one yeah if you put an
event subscriber in a test code unit the
test code unit can only use the event
instancing manual yeah but this could
also be the case I have a subscriber in
a different coach unit where we have the
event subscriber instance manual and
then in the code we're going to bind it
yeah so uh we set up a procedure with
a publisher and we're subscribing to
that publisher and saying we've handled
it yeah
that's one thing to be sad here and
actually it's something I didn't realize
before I always put it there but it's
not needed anytime your let's say the
scope goes out of existence you're
subscriber that is manually attached to
the publisher is going to be detached
again yes when you leave this function
the code unit is going to be Unbound if
there are no references to it which are
not because it's local I mean there is
no harm if you're unbind no you're just
being explicit but if you're wondering
why in Microsoft tests or code we are
not using Unbound please that is the
reason yeah it's never used it's used in
few cases yeah yes okay
so our look has shown to you the manual
binding and I'm pure basically how you
can extend it and so I would like to say
that could dedicated to stability so if
you're writing a code so you can test in
a better way and it has no production
value is a code smell because the code
itself should be testable so when you're
defining the apis they should allow you
to do all of the testing
however as we all know it may be needed
in some cases so I'm going to give you
some tips that you should do
and my recommendation would be to
compile it completely out of the
production app
so I'm going to show you all of the
possible
the stabilities that you can do
the first way is by declaring a internal
method that you can use for testing and
the problem here is that it would be
much better if you would have a public
API so the question is do you really
need an internal method
and be careful that internal is not a
security feature it's a compilation
issue a completion feature so it means
that nobody will be able to take the
penis in your code
the second way which people are taking
is that they would like to set a
testability mode like a global Boolean
and then they will Fork the code within
it if they are in the test or not and
one of the requests that we are often
getting is can we get a keyword is test
mode
which would be better than introducing a
global Boolean and the bad part here is
that you're forking production logic
based on if you are on test or not which
is further complicating the things
we have integration events as Luke has
shown with manual binding so you can
invoke the testability events and they
are okay
however if you are using them and you're
exposing something sensitive like have
you authenticated successfully or
putting tokens or anything that is
security related this is very bad
because anybody can subscribe to the
event and they can snipe it so basically
they can just write it to somewhere else
it's very easy to write the PT and to
abuse this one
and the last thing is that you can use
the internal testability event which is
a new feature you just say internal
event and that means that only your
extension can subscribe to it
now if you're writing the testability my
recommendation would be to compile it
after the yeah so if you can say if not
and then put your three letter prefix
include that's a bit
excludes the stability
and then you just go to the end and say
and if
so if you put this pre-propressor rule
then you can compile two versions of the
app one for testing one for production
so when you're publishing to the app
Source you can exclude the testability
and have a more secure product
this will of course mean that you will
need two sets of tests and this is
something that we also have in Microsoft
now one thing when it comes to the
manual binding it is really good for
testing purposes
and the example here that I would like
to show to you is the how we are testing
payment services
so one of the payment services for
example paper
so when we decided to test the paper we
only tested PayPal but because we wanted
to build an API that you can build on we
are testing it by using a mock
and a mock is actually manually bounded
code unit
so if you go to the definition of the
mock you can see that we are
instrumenting the mock here we are
telling to the mock what should it do
when the events come
but if you go to the mock definition
you will see that the event subscriber
instance is manual it's not static at
all it's a local code unit
and because it is manually bounded these
temporary records that we have they are
going to live within the test scope
because manually budget code units can
have Global you're always going to get
the same instance as you're testing
and basically the implementation that we
did here it's a like a mini save payment
service provider so it's like a small
small PayPal that is testing the
functionality
yep
okay the next thing is that the test
should be data agnostic and you should
create all of the data that is possible
but you need to be fast of course right
and the recommendation is to reuse
libraries we use sell the random Library
any and but unfortunately we need to
take the dependency to the existing demo
date because of the performance reasons
our product is specific and I mean you
cannot do the vat setup for general
ledger setup and other entries with
every test
this is the explanation of the demo data
so if you're looking at rapidstar
packages
the extended should be Chronos on-prem
evaluation is chronic SAS standard is my
company
extended is the largest of them then
evaluation is containing glass data and
standard is containing no no data and
most of the tests that we have depend on
the extended configuration
now moving forward we would like to
switch to right test against evaluation
because it contains less so we'll get
better quality tests and one of the
items that we are pending is to release
a list to you which test runs on which
metadata so you can reuse them in an
easier way yeah what what quite some
people experience is that they using the
libraries from Microsoft and then they
build up a Docker a Sandbox version that
sandbox version only has the evaluation
demo data where a lot of Microsoft
libraries apparently make use of some
data that then does not exist so make
sure and I think you should use the
libraries they're very powerful and
making your work much more efficient
that you'll use the on-prem and by the
way for the SARS if you have a Sandbox
like only available for The Insider
don't use W1 or whatever but use bass as
the country version that has the full
data set also yes you'll get the list
failures yeah so when we cover the topic
of failures basically for us the tests
are not failing
and the reason why they are failing for
you in Docker is because we have a lot
of tooling that we have not shipped to
you we also didn't tell you how to run
some specific tests and we wanted to fix
this
also I want to just say it explicitly
Microsoft tests if you start reading the
code they are categorized in the
category really good then you have bad
tests and you have absolutely ugly tests
right because I mean it's 30 000 tests
they have been there for 15 16 years
written by various different people so
they are goods and bad examples so I
hope after this session you will be able
to spot which tests are bad basically
okay
testing Integrations
you could say A Part relates to the
mocking but let's discuss it in a wider
context if you invoking some kind of
process like say calling up an API you
have to authenticate you have to compose
your request and you have to send out a
request and then you're going to get the
response and then you're going to parse
it yeah and then it leads to creation of
Records updating of Records inside a
database let's say this is the general
flow of this process how about testing
around this well what are the points of
where the risks is at the highest
probably that's this part you're getting
the data in and how does it fit into
your database into your tables whatever
it is so that should be your focus in
the testing yeah the other part a little
bit oh sorry there should be a next one
so yeah okay so
you can cover this risk yeah
so to show you this thing and as looks
at the parsing is the highest risk
because if you think about it in
Microsoft if you are pulling an item
from an outside service we need to
support 30 countries across different
versions so that
something doesn't break during the
parsing that's the key also we need to
Future proof the code so thus that the
future functionality doesn't break
and if you remember the tdd example this
is the case if you're writing external
Integrations when you can save a lot of
time because these tests are extremely
simple to write as you can see this test
is very simple you have a response from
the service you call your public facade
to parse the request and to for example
create items and then to verify if they
are correct and the only thing that you
need to do is that you can hard quote
the reply from the service which is very
easy to get into code and then you can
do the test driven development on it
if you do it like this just like putting
any within it I wouldn't recommend it
few people make this mistake because in
some cases it can break the Json and
it's not a correct way of creating a
payload the proper way is to use the new
Json object like this and then you can
mock the reply from the web service and
if you write these tests they're
extremely easy to write quick to execute
and it is going to cover the biggest
risk that you have on testing external
Integrations
yep that was the one I was expecting
after that sorry for that but the next
uh Focus you would have is on composing
that request yeah does it work right do
you is it the right one that needs to be
sent to the other side yeah
um if we look at it from a testing
perspective as mentioned if you really
need to test the integration so that you
need really are going to call upon that
that service don't do it in automated
tests so automated test runs make sure
you do it either manually or
semi-automated semi-automated could be
that you have built up a test yeah a
full scenario but you're the one who's
running it so you're controlling it when
you're going to run and yes that would
be an end-to-end testing you're calling
up on that service and you're getting
everything back yes you can either write
a nail test that you're running manually
or in Microsoft we're often using
PowerShot scripts to test apis and so
ones yeah or a postman kind of things
yes approximately once or twice a month
just to see if it's an interest bear in
mind as mentioned before don't call the
access actual service from automated
test runs now keep that in mind it
should not be the focus it could take
too long so you're not going to having
the profit from it it could fail but all
the thing that has been mentioned before
yes and if you would like to test the
end-to-end scenarios and Mercury similar
framework is the way to go we have it on
our backlog to ship it to you because
currently we do not have it to ex so you
you guys can be used
but moq framework would actually mock
the HTTP requests
okay so for the next slide testing the
apis the biggest risk is the actual API
page
and the reason why so if you have
written the API Pages the reason why is
you probably know we have the different
flow of the triggers
validation behaves slightly differently
and in the end any UI if it is being
triggered during the web service call is
going to fail and this is actually the
highest risk so when you validate
something on the sales invoice if you
get the confirmation dialog the web
service call is going to die
so that is the thing that we are
automating
and the way how we would test the apis
is that you would start a test and do
the setup is going to lock all the
tables that it created because we want
to roll back
then the setup is going to call the API
and the API page reaches the highest
risk is going to try to update the
records but it is going to fail because
task is holding a lock in the first
session because it wants the rollback
yeah and that's the test isolation
that's the test resolution per coding it
right so this is the reason why the test
API tests are failing
so the fix is that we disable the test
isolation so these are the tests which
are running with test isolation disabled
so we will get no locking on the records
and that we commit immediately after the
records and then you can update the
records and verify the response I can
show you this one
rather quickly
and you will see that each of the tests
is following the same approach just let
me find
the example it's here
so you can see when we are testing the
customer API we are doing a setup we are
doing a commits and then we are calling
the web service a library which is very
useful is Library graph management so
you can you reuse it yourself that's a
great one and then in the end we are
just verifying the response and if you
want to run the API test you need to
disable the Tesla installation because
they will not run for the reasons that
we have seen before
if you're developing API pages I always
say if you need to start with automation
test automation start with your apis
it's a quite simple way of testing
precisely now we're getting a lot of
questions regarding the authentication
because
few people are wondering how does the
authentication work we in Microsoft we
are using Windows authentication while
Docker I believe it is running with user
mostly you do precisely and people are
confused like how does this work
and we are actually using a secret trick
and the secret trick is that if there is
no users in the database there is no
Authentication
so our calls are passing because of this
and our gates are using Windows
Authentication
now I would not recommend that you use
this secret trick
yeah actually it was a hello to get it
working or to understand how it worked
it felt like those old database files we
had way back and that you could just
connect to the database file and you're
in there's no out authentication that's
a bit like this indeed I have in the
examples of the book a script to delete
all those data and then boom you get in
but
running pipelines you probably will not
be in the domain so you will be using a
user password and then AJ AJ Kaufman and
R2 Von the vordermanford helped me to
get that done so all credits also to
them it is possible right now since bc20
I don't know which CU but currently
there has been added a subscribe a
publisher you can subscribe to in the
library
graph to insert on the call that's being
set up so the URL being set up the base
authentic education so using a web
service key that has been made it very
simple so no way anymore nothing that's
blocking you from making API tests and
run them in your
pipelines yep
we need to keep an eye on time yes we
will have to skip some parts
unfortunately so the next thing is
testing tasks schedule or job queue and
it's a strong recommendation to disable
the tasks when running tests
why because if you kick off the task
schedule you may get some unexpected
test failures you know we could trigger
some tasks with every logging and that
will crush your test
but then you know like the question is
how do we test these things if the tasks
are disabled
so the suggestion is of course the unit
that's the code unit that's the biggest
risk but if you would like to test end
to end
this is how the flow looks like and it
is very similar to the API flow
and but the solution is different so
instead of using the test resolution
disabled which you you can do and you
can also Implement wait for it to finish
but that would be unstable from the test
automation perspective the solution is
to move everything to a single thread
and then you can test flow Center
so there is no need to test that it
behaves asynchronously and to introduce
the test instabilities you can test the
flow synchronously and you will get good
code coverage
and then there will be no locks because
they are in the same session
testing the task scheduler it's rather
simple you will see these contrast
structs across the app we are using this
manual binding and handle pattern to
force a single session so you can test
it like this it helps a lot with
debugging but the recommendation that I
would give is not to use the task
schedule but to move slowly away to the
job queue because this because it is
giving you much more functionality
if you want to test the job queues it's
even simpler we have a library for it
so you set it up by using these two
commands on the top and then you can
find the job queue entry and run it and
we are using it a lot in our tests you
will find a lot of examples how to test
the job case
and it is running in a single session
yep so
yeah some more we'll keep an eye on time
and and jump a little bit through it by
the way short remark if you really are
stubborn and you really want to trigger
the task schedule there is a way to do
it but then it's a second process like
with the API make sure to run your test
outside of isolation and then you have
of course the challenge of how to sync
with the Tau scalier being ready so
that's another thing probably I'll blog
about it in the next week keep an eye on
that one a couple of other topics that
we wanted to cover let's see how fast we
can get through them testing permission
some insights on the test tool testing
the the test tool things and code
coverage on testing permissions
um a short introduction what why would
we do it what is let's say the the
technical background on that and a
couple of examples why would we want to
test permissions well actually with
writing application tests you're
verifying that the feature is due what
it should be doing yeah so
um often or actually we will run that as
super user and that's why we as
developers also do very often but then
later on we find out it goes out into
the world and the users are not able to
use it why because they don't have the
right permissions maybe they've been set
up and nowadays we have those permission
sets and they should be part of your
extension that you're going to install
but have they be inside and then still
is that permission set containing the
right setup of permissions so what we
also need to test is
does the feature work in the given or
the expected set of permissions so
that's about
testing permissions by the way a note at
the end you will see is that you can
only do this with permission set objects
yeah we had this feature that you could
create a permission set in XML format in
your extension and it will create a
permission set in the database but
that's not a system one and your
testability framework will not see them
you cannot use them the users creating
permission sets so manually creating
them is the same thing you need
permission set objects for that so
a couple of things to that there is a
property you might know it called test
permissions on a code unit that's one
thing I'm going to talk about and then
based up on that or well that's a kind
of basis from where you could go and
lower the set of permissions that the
user that's running
the test is having at that moment and
permission set as a small example
the test permissions property is a
property on the code unit and is also an
attribute on a method so you could do it
at the code unit for all the methods and
you could or you could do it
specifically for a test method however
this property is doing nothing it's just
a pre requirement to be able for the
process to steer permissions and how is
this happening well on the code unit you
set that permission and by the way those
who are running tests on the bc21 have
found out that probably a lot of that
tests fail why the default value is
restrictive probably could have better
been disabled but it's not and
restrictive means that all the tests are
run with the standard uh permission set
called D6 365
a Bus full access yeah so all tests now
if you haven't done anything with the
test permission are run with that set
that's set up in the test Runner that's
one of those that's that code unit with
a specific setting and there the
permission is set by default based up on
fact that your permission test
permission property is restrictive so
this is the default setting and the test
Runner will use this permission set so
um on a method there's the attribute it
if you don't do anything it can inherits
from the code unit but you could change
that so that the code unit has
restrictive but it's disabled on a test
all right
already mentioned
from B 20 bc21 The Insider build as
mentioned you will get an error like
this yeah so if your test error like
this then you know what to do the
simplest fix is to change in all your
code units or at actually what probably
you don't have a line with test
permissions add a line test permission
is disabled and then it will work yeah
um
a couple of uh other technical things
realize that normally you change
permissions for a user that means that
you manually change that you need to re
so log out and log in again and then
your permission set or the person needs
to do that for whom you change it is
then effective yeah here it happens on
the Fly and it's not changing the
settings in the database but it's
changing them let's say in Cache there
is a.net component to handle that that
also means that you have to run your
tests in a environment where you don't
where it's not
sauce clout yeah so it needs to be
on-prem and realize start each process
make sure that your user running the
tests is a super user to be able to do
anything I mean in your test you want to
create data which the standard
permission set doesn't allow you to do
so you need to be able to get back to
the super level
gradually you start from Super and you
can
add another permission set to lower the
full extent of the permissions of that
user and you can do that step by step
I'll give you a couple of examples
um and also one that you revert to the
super
settings of the user okay
this test helper a permission test
helper dll is wrapped that's since a
version or two previously you had to add
to your test a.net wrapper to be able to
use that but nowadays we have this
permissionsmart.app if you're
starting from a DVD installation it's
one of the apps you need to install to
be able to disk do this kind of things
BC container new bit container will do
this all for you yeah if you make sure
that you have the test tool maybe only
the test libraries included okay as
mentioned it should be on-prem
the library lower permissions is let's
say the spider in the web for you here
and there are a number of methods a
little bit more than this one but these
are the bases start logging permission
enough permissions is based upon one of
the methods in that permission Mark
which is also called by the test Runner
and it's setting always to Dynamics 365
d365 business full access the other two
methods allow you to either
set the permission set for the user
right now that's what it's going to be
right now or at do that so that it's
lowered a little bit more some
examples I will show you
um
first of all a permission set you might
know this one just as a small example
you need to set like we did on manually
also read insert modify delete
a small scenario and with permission set
you will always have a twin a test that
test what does it do if I don't have the
permissions and what does it do if I do
have the permission in this case it will
start with the full based starting
permissions
d365 business full access you're
creating something and in this case if
you don't have the permissions to create
it you will get an insert permission
error right
the code as an example looks like this
by the way
previously before business Central 21
The Insider build
you would have to implement that given
because then the standard permission set
was not set by the test Runner so I've
out commanded it right now and then if I
create something I need to assert it
because it will throw an error and I
need to validate that that error is
happening the counterpart would be you
do have permissions it should create and
then you should find out that the record
is created so in essence the the
scenario is not that much different but
the only thing will be that we add the
extra permission set yeah so in that
case it will succeed as a last example
here a little bit longer one in this
case I want to read something yeah so
the record should be there and typically
my tests were data agnostic should
create the data in this case the given
lookup value needs to happen but that
can only be done
if I would have the permissions or even
better if I'm super yeah so the first
given unrestricted starting permissions
you actually go back or remove all the
permissions that were set during that
session for the user and you're back to
Super
you create the data then you're restrict
it in this case by full base starting
permissions read read error okay
looking at time
last couple of notes since BC 18.3 a lot
of things have been made possible but
you could say the full implementation is
now there with bc21
all right
okay so for the code coverage the good
news is that we have implemented a new
code coverage module
that we have released with the v21
so if we go back to the test that I was
naming you can enable the code coverage
per run per Kodi on it and per test
if you're running it in the UI the most
useful setting is going to be per run
because you're interested in what is
covered and what is not covered and if
you run the test like this
then you can go back to the code
coverage page
and here you're going to get the
code coverage information on the objects
that you're testing you can filter it
you can see which code is covered which
code is not covered so right now you can
see the code coverage while you're
developing the tests we also support the
CI CD
and however the support for Docker the
support for BC container helper is
coming shortly sorry for that if you're
too busy with the latest release so we
will see to implement it as soon as
possible
then to go back to the slides if you
want to analyze the code coverage this
is the recommendation and you can see
that to increase the code coverage it is
taking increasingly more effort to get
the proper code coverage so getting to
50 you'll get with very few tests and
you cannot think that the job is really
done around the 70 you can say that you
are having a good test suit in average
around 80 percent the most of the
scenarios are going to be covered ninety
percent is bringing you if you cover the
error cases
100 it's really hard to reach and it has
a very questionable return of investment
and here you're writing actually a lot
of cement because you will end up in the
case where you need to write a test case
for individualized and we do not
recommend it
so we are usually trying to be around 80
or 90 percent because getting to 100
this I got stupid it takes too much time
as you're not going to get anything out
of it yes I managed to do it like once
and twice in my career
because it it was very simple so
and basically this is the the quote
right the quote coverage is like a seat
belt right so it is important but it is
not going to help if you're not driving
well
and the most important thing is what is
missing from the code coverage and our
recommendation is don't chase it think
about the scenarios and make sure that
you have the asserts in the good place
and no unit Testament
now for the test only internals uh we
are not going to have time unfortunately
to cover this one in high level of
details I'll just briefly cover it and
then we can discuss it afterwards I can
also record the video to explain how
does it work
but basically all of the server all of
the tests are essentially being run by
decodionist.run
however this is not going to give you a
test isolation
the next component which is giving a
test isolation is a test Runner and its
responsibilities to run the tests report
results tracker code coverage and it
allows you to select the tests
however the challenge of the test Runner
is that it cannot run UI tests
for these reasons we need the client
side and in Microsoft many years ago
like more than 20 we have implemented a
mini client which would create a UI
session so we can test the UI
and the challenge is it was doing too
much stuff so it became dating for the
automated testing
however you as you probably remember
with 14 release we have released to you
the automation on the nav and the nav
container helper back then
and we are actually doing it through the
Powershell by using the technology which
is called UI web services
but the problem is we wanted to
discontinue these UI web services
thus we have named this Powershell as
internal
and the scripts that we are actually
using here it's called this script Al
PS1 which is in the Powershell as well
and the reason why we have introduced it
is because then we can use it for our
internal scripts and we can also expose
it in the BC container help
so the main point that I wanted to say
here
is that when you go to the build folder
and you take a look at this folder
everything that is internal we are
planning to deprecate
and everything that is above that folder
is fine and we are using it as a stable
interface
also if you go to the signature you will
see our in our script what does it have
BC container help might have less so if
you see some useful properties let us
know we can always add them
then if you go back to the slides
the idea for us internally in Microsoft
is to deprecate the old client that we
have and to run the test in the same way
as you do because then both our tests
and your tests are going to be stable
we also want to get rid of these
internals and to move them under the
management point for API it's going to
be very similar to publishing the
extensions
and then we will be able to implement vs
Code test run
so you will be able to run the test from
Visual Studio code
additional thing that we are working on
it's called task discovery
and because we're having too many tests
we need to we cannot run them all of
course because it would be too much
thus we are doing the thing that is
called trend-based execution we are
looking at the change that you're making
and only running the tests that are
hitting the same code coverage
and from time to time we are running the
full test suit just to update the
trend-based maps and we are planning to
ship something similar for you it's
coming soon I will just briefly describe
it here currently for each of the line
we would know which test code units are
covering it because we have a coverage
map
the thing that we wanted to build is not
only the code units but also test
methods but unfortunately that is
technically challenging so most likely
here for the specific method you will
get a list of test methods that are
covering it on the right so you will be
able to discover the tests and to add
them to the tests Runner API so you can
run them from the visual studio code
that is the goal for the future
okay
so for the conclusion I would like to
show you one story that I have heard
from the test architect many years ago
in Microsoft and I liked it so much so I
decided to make an XKCD comic out of it
so the story goes like this a the
architect was working together with the
apprentice and they were coding happily
and their day was interrupted by three
Developers
that ask the same question and the
question was oh great architect what is
the code coverage call
to the first guy the architect said
don't worry about that to focus on the
most important scenarios cover the risk
and write a good set of tests
so the second developer he just took a
ball he said I'm thinking about going
down to the continent taking seconds how
much food should I put in this bowl
and she said how could I possibly tell
you that it depends what you had for
breakfast how hungry you are and then
she stopped said ah thank you Bowden
left
and to the third guy he got really angry
slammed his fist on the table and said
80 and not a single percentless
now
after they left The Apprentice asked the
architect he said oh great architects
today three people ask you the same
question yet you gave them different
answers why
and the architect replied the first
person is a young developer he needs to
focus on the wise and essential things
before focusing on the hard things like
Matrix
the second person is an experienced
developer she knows her code much better
than Idol she knows where the risk is
how to automate it which parts require
more automation
and where should we provide more code
coverage
and the last person always asks about
the code coverage number if he only
cares about the code coverage number and
he never purchased
so to conclude
I hope that we have explained to you how
to write the good tests the ask is to
always think about the risks
use the examples that we have showed you
today and try to hit the 80 code
coverage at least sometimes
okay and with that
yes of course the last thing is join us
on Yammer we have many developers here
we can discuss various different topics
you can provide this feedback we can
also show the totally share the tolling
so
join us there
yep and we have time for questions
yeah I have a question about the
combination of apps Microsoft writes
tests for base application we write
tests for our own apps but out in the
field of course you will find an array
of apps which are being installed on an
end user system
and while the individual tests may have
been successful
we have had support cases when there was
an app installed and the whole system
stopped working because there were
several subscribers attached to a
publisher and we all know this event
pattern and maybe the code isn't
executed properly anymore because there
was an app installed do we have any sort
of warning which we can issue to the end
user your system hasn't been properly
tested the way it has been installed uh
that would be really hard so if you
think about the technical technical
challenges right that would be hard we
are putting a message when you're
uploading or installing app to be
careful and to test it properly right
but this test combinations it's really
hard to cover
because one extension can be
incompatible with another and the number
of combinations is too high
so the best way is to test each of the
extensions in isolation and then when
you're building up the system it's a
good thing to run the end-to-end tests
just to check that the whole thing works
correctly the problem is the the apps
for themselves work perfectly the tests
are all successful but the combination
of apps yes if you test these on that
currently there's no initiative to or
incentive to say you need to test the
compound you need to test your array of
apps which you're using precisely but
here's the thing right either the app
could be depending on the other app and
you should test both of them together or
they could Clash though they are
unrelated because one app did something
wrong with the event subscribers first
thing you can test the second thing you
cannot you cannot test that somebody's
not going to do anything wrong and
that's the part where the hotfix is
coming in right and fixing the code of
course right because it's bound to
happen I mean right people will make it
happen but it's it's an unpleasant
situation it is I would recommend you
know to test the sandboxes to do good
tests on sandboxes this is also the
place where the manual testing is
kicking in yes but we do not know which
traps being installed if my Microsoft
propagates you can go to the app source
and install anything you like but then
your responsibility for testing is the
user yeah yes but that is not
communicated not that way true please
install use all tests which are
available and
use it as a compound solution test the
array of apps a set of tests is only
testing the that app if you build up on
apps you get another set of tests so you
cannot use the other one or you can but
then you see it fails and then you know
it fails because something has been
added so the construction or this
complexity yeah that's what you have to
deal with one of the things that we want
to build for you but we might need your
help as well is that we want to build a
set of end-to-end tests that you can
deploy on the sandbox and quickly test
if all of the apps are becoming correct
so you should execute you know like the
processes and so on
thank you
so you don't need to go around and click
is this microphone working
let's take this one
yeah take it
so for the test pipeline I asked if I
have a failing test is it better better
to comment all out or have
in my pipeline of hailing test because
um then I can merge my mode request or
something because on Microsoft we have a
lot of failing tests and then and it's
weird to have
um a release with failing tests yes so
regarding the pipelines we do few things
in Microsoft you need to have a way to
disable the tests temporarily and the
test should not be disabled more than a
few days right four weeks we can discuss
later like what are we doing to Crusher
tests we are really trying not to do it
as much as possible
but basically it is essential that you
have a way of actually disabling the
audience and enabling them back again
because this is happening for us as well
like because we have split the reports
to platform application microservices it
will happen from time to time that
somebody makes a mistake in a repo and
crushes the tests in the other rip we
analyze the impact and if we decide that
the impact is not large we will disable
the test fix the bug enable the test if
the impact is large we roll back the
change and
that is how we handle it so the ability
to disable the test in the pipeline it's
really important the second thing that
is important is reruns
we rerun the tests twice
just to make sure that the instability
is not going to help
but the failure says something so you
need to take care of it I think it's
working but no not again wow yeah
[Music]
okay hello
um if if I have that kind of situation I
have a job queue I want to have a
testing tested the job queue but inside
the job queue I have a invoking the web
service yeah or the API is it possible
to have a good isolation for that
without any issues and additional
question if it's possible to really
debug that kind of issue it's a
combination of two things we talked
about we're testing apis and testing a
job queue yeah exactly I have a job
queue and inside the job queue I have to
invoke the API so the idea if the job
queue is leverage that code unit into
the same thread yeah so don't call the
job queue let don't let the Tasker you
do that so you test that code unit in
the sequence and of course then it's
calling the API if it's an external one
I would say mock it yeah it's your own
API yeah it's my own then you have the
option to call upon your API as
precisely Nicolas showed but then the
test isolation should be disabled I
would recommend write a lot of tests to
test the API in isolation and you can
write one test to test the job and
because we this is okay for us and maybe
this is something that can be happen and
can be done but if it possible to debug
that kind of uh issue when I have one
session and the session opens another
session inside it uh so if you're you're
using API page type right
is you will be possible it will be
possible for you to debug but it is
going to be challenging because one
session that is running is either going
to be a UI session exactly and the
second one is going to be a web service
search so the way how you debug It Is by
putting a small weight of couple of
seconds or a confirmation dialogue that
will allow you to attach a debug okay
thank you very much
that's a nice game yeah you throw an eye
throw I'm throwing why do we have to
um did I got it right that with an
upcoming BC release there will be a
possibility to get the code coverage
data from
um from yes everything is implemented
you'll get the support for CI CD
pipelines it's it's fresh out of the
press okay so we are still going to turn
it and we are looking forward for your
feedback okay we've tried really hard to
get it but it was nearly impossible to
yeah it is possible between 21 we're
only missing Powershell Scripts but keep
in mind that we may need to change it
based on your feedback because nobody's
using it yet so it's right out of the
press you can help with the either BC
container helper it's on the GitHub also
all of the test Runner things are on the
alap extension so you can also
contribute if you want we have two
questions here let's see if we can get
it done first yeah and you suggested for
the API testing to go to the basic
authentication nope we suggested to go
to the suggestion that looks at yeah
that's a basic authentication yeah
but what is the suggestion when it's now
deprecated it's not applicated on-prem
okay yes true oh it's only source
and the last one and by the way I've got
a couple of books if you want one come
around
yes hello uh first of all the
verification when we test when we turn
off the isolation for ABI testing the
data will be written
so we don't have the way to roll it back
this is just to verify and the question
is I have a scenario in which um during
kind of data sync to other company in
the same installation so it will reply
back to the record the created during
the testing and it gives the error like
I cannot write to an isolated record is
this any way to test such a scenario you
invoke something a web service or
whatever or data sync then it will need
to reply back to me by changing the
record is there any way to to do that
what cross company or yeah
I give up finding a solution I just
wanted to hear if there is something out
of the box this is the first time I'm
hearing this problem you can come down
and we can discuss it okay I think it
would be possible to change the company
from test yeah yeah so when you're
asserting you can change the company on
the record to find it yeah and try to
see if it is there okay you should be
able you should be able so okay you want
a t-shirt still yeah
ah thank you very much thanks though
[Applause]
