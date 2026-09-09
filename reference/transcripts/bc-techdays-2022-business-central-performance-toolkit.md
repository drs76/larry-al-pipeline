# BC TechDays 2022 - Business Central Performance Toolkit

- **Source:** https://www.youtube.com/watch?v=tZ5VRvlgAE8
- **Video ID:** tZ5VRvlgAE8
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 45m54s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

ladies and gentlemen welcome back in
room 9
for the next session business central
performance toolkit presented by bardu
hendrick and simon thank you
so
i'm on here yeah
good afternoon and welcome to this 45
minute presentation on our performance
toolkit it's great to see you all
we have a
packed agenda
first we're going to introduce
some of the reasons for why you should
invest in performance testing and maybe
also just the rest of the
the tool family
we'll take you through some basics
around the tool
then we're going to cover a customer
story and some
findings from that then we're going to
look into the analysis of the data which
is really the the gym obviously in in a
performance toolkit is also to be able
to pull out the data and
make use of it
so let's get started
[Music]
why should you invest in performance
testing
we invest in it so in back home in
copenhagen we use performance testing
and so i just dumped in a small
diagram here graph
and
each of these lines represents a
scenario that we have it could be like
post a sales invoice post a purchase
order
open up something
do another thing
and then if one of these spikes that you
see
would remain there for more than three
times
three builds
three days
we would actually
log a buck and then a developer would
need to pick it up and take a look at
what what could have happened and we do
that based on the churn that we have in
our source depot anyway another one is
that logging can be difficult to detect
if you are just a single user on a
system and you try out different things
it might just work perfect
in a system with
maybe hundreds of concurrent users this
can be quite different
then there is the diversity in the
solutions out there
because
you can have many third-party extensions
or you can have some
your scenarios might vary
depending on your your vertical what are
the problems that your solution is is
testing
and so
there might be other third-party
extensions on top of what you already
have so how does that actually perform
then there's another one the impact
release over release as i just showed up
here we also to discover some
regressions i think in the past six
months we locked something like 35 bucks
against our own team to
go in and evaluate and bring it back
and then performance tests can also be
reused and this is an important
part because obviously you want to be
able to reuse the test that you write at
the very beginning if you think about a
project
and then it moves on and it matures and
we put it into more like a company
simulation test which i'll also cover
just briefly and then finally you might
use something like ci cd um
and then support engineering
no engineer like to ship
low performing code
so that's another good way to to support
ourselves
and then the final that there is this
what-if scenarios and this is typically
when you're approached by maybe a
prospect and they have a lot of
questions about
can the system perform this and that
so we'll talk a bit about that as well
so let's see as i mentioned we use it
internally
cicd
every pull request that we have we run a
number of tests
i just took an old one here
but this is an example of a pull request
it ran some tests during our bodybuild
process and now it says
wait a minute you introduced the
progression
um
please sign off that you are okay with
this regression because it could also be
that we are actually okay with this
regression
um
then as i mentioned we'd also use it
build over build so this is actually
once it's it's gotten in and now we're
using it more like a full system right
remember i said it was maybe you post a
sales invoice so now it's it's in the
scenario
okay
so
when should you use this performance
toolkit
um
we think you should use it from the very
beginning but
you can imagine some of these questions
come up is the solution performed enough
for the cloud
what is the performance impact from
current and future customizations and
not just customizations i would also say
think about other things like maybe the
company is adding more users
maybe they're adding
more reports more data
so there are many things that can change
in the real world
and this is where it can become
useful
what is the performance impact between
major upgrades as i said any churn can
introduce a regression um that's a good
thing to to keep
a tight eye on um can the system handle
posting 20 000 invoices per day
it's a good question actually this is uh
some of the questions i often get in my
inbox and
the short answer is uh
yes
but
really it requires us to do a lot more
analysis because we don't know we simply
don't know how the system is being used
what extensions are out there how many
users etc so there are so many factors
um
so can the system for instance handle
700 users and these are all relevant
questions right it's just hard to answer
them without actually knowing uh without
actually trying out the system
so so
this could be some of the questions you
can address with with this
anyway i wanted to also touch on this
reuse because
i think that's also an important uh
aspect of this because we don't want you
to kind of first create test
then another set of tests and then some
performance test at the end of it and
then what do you do with those throw
them away or
so we were thinking about how you can
reuse your investment
so
here you can see a simple extension i
stole from our
i think it's a get up and running with
your first extension
and this is where you can start
applying your performance test right
very early these tests can then go into
this
what we call sort of the company
simulation this is a
spreadsheet i borrowed from the customer
story that that bottle will actually
cover
but this just shows a bunch of scenarios
a lot of data about
the expectations to the system and how
that actually performed during the test
so that's another
place where you can reuse your test and
then finally if you saw the the keynote
this morning
freddie presented his elgo
and we are now also
part of that so we have our own
github action to include our performance
test and run these
so
it's also
these tests
they also use useful with the the rest
of our toolbox maybe you you saw this
this morning as well we have the
performance profile at the incline
performance profiler so
when you discover something you can
actually start this profile you can run
your bcbt test and then you can stop it
again and then you can go into that with
the with the profile file
and that means you can also utilize the
the ailer profiler
then again as i mentioned we have this
ability now to add the performance test
into these
pipelines so every time we basically do
a pull request in our github
we can get some results from that
soon
we will introduce the report that we i
showed kind of this snippet about where
you had
the graph there we're going to introduce
that so we are going to put it out there
so whenever you have a build you can
actually go in and monitor it build over
build
and then finally
this new app that was also i think shown
today
we are also adding support for bcbt
so the telemetry you generate you will
be able to
pick that up in the performance tab and
then you can see how your latest
build perform basically
so
it is sort of part of the
the toolbox family
and um
there is a reuse for for your test
so the investment can basically live for
as long as your setup is is alive you
could say
one thing i may also mention is that
once you've done this you can also use
it as as part of a
sort of i would say external
sales pitch right i mean we
our solution is performant we can do
this and that with that many concurrent
users
might also be useful
um
so i just want to cover a bit of the
company simulation because that that is
really sort of the
the basics of the whole tool why did we
build it in the first place that was to
cover this because
um
stress test is available
we have tests that can test everything
in a single
unit
we have scenario tests but what we're
really missing is this whole system
right it's it's about
getting all um
the scenarios lined up
think about can a user actually perform
purchase orders in two minutes
probably not and it's probably not what
the users actually doing even though you
might have web services from a web store
we can still push that into the system
but the point is that
the tool itself you may have a scenario
first you want to define the scenario
could be a user goes to the role sender
they open up the customer list
from the customer list they may
create a new
document could be a new order quote
invoice
in this case i just said okay they're
gonna release the sales order and then
they're gonna post and send an invoice
maybe not that typical maybe it is
but at least it's a scenario in trend
right it represents a user
and then another thing to consider is
what are the peak hours during the day
because
i would say probably in most cases
you would have something
this may not be super realistic but
as an example you can think about it so
if we look at maybe some of the busy uh
periods of time i don't know if this can
be read actually you can see it's quite
small
but if you look between 10 and 11 that's
the third
column
we are quite busy as a company this is
based on a conversation effective
conversation we had with a customer for
instance the client
and then between four and five again we
are also super busy and this is because
in that hour
we simulate that we have a bunch of
consultants coming home reporting the
hours
from today
and so
if we had to go in and say okay what
would be the key
two hours of the day that we should go
in and simulate using this um
performance toolkit
those would be the two hours that we
would go in
and take a look at and try and emulate
in our setup so
the next thing is obviously what are the
acceptable numbers right i mean is is
acceptable is that three seconds for a
page to open is it one second um how
long time does it take to post something
we need to define those because
the client may say well
that is acceptable
to run certain reports it's okay it
takes
five minutes no problem other things
they might want to have just like that
so we need to define those goals we also
need to talk about what are the
environment that we're going to test in
because we can use
sort of at least three different ways to
test this right we can use the on-prem
which is just from the dvd image and
then we just simply install it
get it up and running we could also use
docker
and finally we could use a sandbox
because we do not support production
i won't cover sort of parity but i just
want to say that parity between prod and
sandbox is roughly the same
the
key difference is is basically the
sequels here other than that the
performance is
roughly the same anyway
we need to define some test runs when
are we going to do this
how we're going to do it
and then finally the investigations this
is the analysis part that we need to
come back
to um
yeah and that kind of simon i guess i
want to
put
you on
now
to talk a bit about the how to's
so yeah the mic is on
uh so now we talked a bit about
kind of the introduction why you should
use the toolkit so i just wanted to
quickly cover a bit about
how we use it and how it works and also
some details uh about the test
so let me just uh go in
to my environment
okay so in here this is probably the
main
it's this okay so this is probably the
main uh
area where you're going to be working so
it's this is the bcpt suite
and what is that well you can think of
it as a scenario or a company simulation
so the main thing you might be working
with here is
the sweet lines
and there's nothing magic about this
it's basically just a code unit that
this tool will orchestrate and run for
you
so again we provide some sample tests
that you can use
they're not
extensive and take them more as an
inspiration for what your own test
but basically the main things you will
be looking at is
the number of sessions so
what is that that's basically a user so
in my scenario i have two users that are
basically creating purchase orders
so you can think of them they're running
in concurrently they're running at the
same time
during their purchase order
and then we have this option regarding
running in foreground
because one of the things we support is
pace testability i don't know has anyone
worked with page testing before
a few okay
so we will actually you can reuse this
in these tests
but there's a limitation so
it has to run in the foreground we do
not support doing client interactions in
the background
so that's why the checkbox is here also
if you want to do some client profiling
if if some of your code runs in the
background it will not be captured so
that's just the thing
and then the other important aspect is
about the delay between iteration so
when a user is done you know
creating their purchase order they're
not going to go immediately and create a
new one that is uh not very realistic
because again this is not a stress tool
it's a tool for simulating workloads you
might expect from your customer
so this is one thing you will be working
with now i set it to five that's maybe
pretty unrealistic or maybe it is uh
maybe i mean i don't know about you but
i cannot create a sales order or
purchase order every five seconds
um and yeah and then the other thing you
have is some other fields on the suite
so another very useful thing is the tag
because when you run the suite it will
generate a lot of log entries and then
you can use the tag to basically
you know differentiate between your runs
so in this case i have a baseline run
and then i might install some extensions
and run it again and that will give me
you know and then i can in later when i
analyze the log entries i can you know
distinguish between them and see the
difference
and while we're at it let's go in here
in the log entries
you will see from my last run
of course you can just clear the filter
this will just be set by default
when you can have a look here or you can
export it
and use excel or power bi
and of course if you have some
some issues you can go in and filter and
say okay what were what was running at
the same time
when this happened very useful when
you're dealing with the locking issues
because often it will be someone else
locking your resource
okay
so let's go back to the presentation
and just skip this in case nothing
worked i would have it here
um
okay
so one thing you have to think about is
when you run it from client that's very
useful for early testing but sometimes
you know like there are some limitations
with business central and
one of the thing is again if you're
using page testability you can only run
one
session at a time
and another thing is that we have
limitations of how many background jobs
can run
concurrently
i think in the cloud it's set to
so again if you're working with bigger
scenarios we have to do something else
and if we think about it so what's
actually happening when we are doing uh
when the users are using the product
and in here
you can see we have a very simplified
view of the
how their
business central is running so we have
some load balancer
in the cloud and then we have several
instances of the nst and the web server
and of course your database
so what happens is
many users they come in and they're
gonna
through the the client they're gonna go
in and hit the load balancer and they
will distribute it out
and we want something similar when we're
doing our performance testing so what we
came up with was a powershell script
which will basically
there we go uh
try and do the same so you will run the
suite from the powershell and the
powershell will go in and emulate these
client sessions so it will create
several jobs that will run in parallel
which use the webclient endpoint to go
in and try as much as possible to
simulate the user load
so let's talk a little bit about okay
now we've seen it how it works what's
the concept
but how do you actually get started
and it's very simple uh you install an
extension that we have
and you can get it from uh from you know
when you're in setting up your docker
you can get it installed by default
on prem it might already be there if you
go into extension management
you might see it there it's just not
installed so you can go in and publish
it
otherwise you can get it from the
app source or extension marketplace what
you want to call it
um it's available there and of course
if you want to take what we've created
and modify it for your needs we have it
available on github the same with our
sample test they're also available here
so you can go in and get them
but of course
we wanted to make it easier for you to
get started with it
and
i don't know if how many attended the
keynote earlier today
okay so you might already have seen it
but just for those of you who didn't i'm
just gonna quickly show you the video
again
um so what we have created is vs code
extension to help you get started
so in here i have my
cloud environment then i go into vs code
i install
the extension then i select which
environment i want to target
and then in this case i'm going against
the cloud so as you know with the al
developer tool you have to use the
device login to to authenticate
and once this is done it's going to go
in and read my environments and find the
sandbox environments again we don't we
only support sandbox we don't want to
mess with the production
and then you just pick where you want
the sample project to be located it's
going to go in
get the sample test we have renumber
them to
so you don't have to do that yourself i
don't know i i think can be painful
sometimes to find
a number available
and then it's going to set up your
project and copy the powershell scripts
that you're going to need otherwise you
would also have to find those yourself
and when this is done you will in a
second have your project ready
with all the sample tests the powershell
scripts and all the configurations you
need so you're just good to go
um
but not only that we also wanted to make
it easier for you to then run
the test from powershell because
we had a workshop and earlier and we can
see there's it can be a bit cumbersome
to you know enter all these parameters
and so on and maybe you forgot something
so from this
extension you can also just
with very
few efforts uh run the simulation and it
will set up things for you and do it
so yeah
and again
we provide a lot of samples and some
examples of the pace testability
very
but again don't don't
they're not complete they're only
to give you some inspiration
so but of course it's on github so
please go in and maybe contribute with
your own samples you would like to share
with the community
um but anyways uh we support basically
two ways so if you've been writing a
unit test or something like that
you already might have
some something like this or maybe um
yeah that you can use um
and again
if you're using a
page testability the only difference is
basically
so instead of doing all this in it and
assigning fields and insert you know
we're just using kind of the same
actions as the user would um
and then of course we want good data so
you should add some
it's basically like a stopwatch so you
can add some for example up here it's
inserting the sales header and then we
end the scenario we are done inserting
and then it will uh it will create a log
entry as you saw earlier with that
scenario name and that
gives you basically
some some probing into
like how many sql calls are being used
and what is the
time it took to do it so so that's all
you have to do with your existing test
and of course you can also write your
own ones from scratch
and then
you get a bunch of log files
and you can do it from here but you can
also export it and play a bit around
with for example pivot tables in excel
bottle will cover that later
um
but yeah so that's basically a bit about
the tool and the tests
and now battle he will like to talk a
bit about one of our partners for ps and
what they have done with this tool
thank you
he's not done yet
so this tool has been out for a
couple of years and a year and
a half ago maybe um
4ps
who's one of our bigger partners in
holland maybe some of you know them
they're in the construction industry and
they were approached by a prospect who
said that they had 700 and something
users
and
[Music]
would we be able to handle 700 users in
sas
with their solution
and
i mean we don't know right or we didn't
know i would rather see
so
what 4ps then did
together with us
was that
they
had workshops with the customer and
exactly as henrik explained
try to identify how many concurrent
users will be will there be at any given
point in time that also includes mobile
users and whatever they have web
services
what are they doing all these users that
are on again
remember
hendrix chart
what happens during the day you know
every friday afternoon
a lot of people enter hours for instance
yeah web services or
power bi or whatever you have of
external services
maybe
uh what is good enough
so henry gold's hinted at that so
is field validation time of one second
good enough maybe maybe not depends
what's the transactional volume or work
volume or whatever you would call it how
many customer inquires will they be
doing during the day all these needs to
all these things need to be modeled
so they had created big excel sheets
this goes on for hundreds of lines and
there are
many more columns and
we're not going through it but just to
say that this is how they work with a
customer
and we're also not going to read
that just to point out that even every
line has a lot of details
so
it's
you need to do
a proper work up front to plan this
and this is a small screenshot of you
know just a part of i mean if you
remember
what simon showed you have the
the lines in that suite
so this these lines also go on you know
long way down
and i don't know if you can read it
there
so all these number of stations sum up
to almost 800 for them with our
bigger simulation
and they were running it they export
excel
analyzed and so on and
they were also interested in just a
system scale with number of users so for
them it was important to
see how are things looking with 25 50
and 100 load but it could have also been
other things that had differentiated
again think of the tag field that
simon talked about
so you don't need to read this because
all these scenarios are specific to 4ps
but then they got you know graphs like
these and
they could analyze them and you know
discuss with the customer is this good
enough or yes or no and
it was
so
while
they were running this
[Music]
we had provisioned an environment for
them without any other customers so it
was completely clean
environment
because then there wouldn't be any noise
from other customers
and i mean
to be honest we were as interested in
these numbers as they were
because we have no i had no clue of
whether we could support 700 users
we do know that though that
on a normal environment with many
tenants we have thousands of users so
it's not because we're afraid generally
speaking but one one customer with 700
that was interesting
so
[Music]
there are two graphs one from the nst's
and you can see
each each color is a different machine
so you can see some load balancing kicks
in
and you can see that none of the
machines ever
really exceeds i don't know what that is
five ten percent cpu load so it's
definitely not cpu bound
uh you can clearly see on the database
load where when they were running the
tests so each test is an hour
pretty intense but still only 20
ish percent of
our load
and this was deemed good enough i mean
the response times that we saw before we
were good enough
the we could see that the cpu load was
good enough
so um the customer was convinced their
you know migrations were done people
educated they went live
and time passed and you know a month
later or whatever it was we took a look
at
actual um
data from a couple of days so that's not
ours that's
two days
you have there
and obviously reality doesn't look
exactly
like test
but you can see that
you know in the bigger picture
cpu rarely goes above 10 percent
right and the database obviously the
pattern is different from when you run
um
intense
simulation
but still you know
yeah 10 20
database load during the day during busy
hours
so
at least from ours point of view that
was
a great thing to see
so
the next part is
analysis so you saw
simon
running
or defining or i'll say tests
in the sheet
so how do we analyze because we want
something like that right
so
first of all short look at the log
entries again simon already showed them
so
in there we have the tag because we want
we want each measurement to be labeled
with something we can use later for
analysis
so baseline or warm-up or
25 usage or 100 usage or whatever
then we have the version number which is
every time we run we increment
the version so you know we can
distinguish each
simulation from each other
regardless of tagging
then we have uh you know how long did it
take you know we have the start and end
time
and
[Music]
then the code unit
number which is not really useful here
but
we have the code name
for the test and so that's point number
one
if you do this give the code units good
names because you want the excel sheets
or the analysis to look nice the result
um
then
simon also hinted at we have
so
a code unit.run simply speaking that's
what we call a scenario
so
like this one right this is
coding.run
and then in between we have these
stopwatches
they can even be even be overlapping if
that's needed
so in this case we said start scenario
at order and then we
do stuff and then we say end scenario at
order and then some time later we say
start scenario enter
basically it says custom number right
and then we validate the custom number
modified to commit and then
you know stop the stopwatch
if you
will so and again you can see i didn't
say
enter customer number i said enter
account number and that's because it's
also nice to
be able to analyze across scenarios
because if you have a purchase order
it's not a customer operand and then
it's a
vendor number
so remember to use good naming
for these as well as well as the tags up
there so
and this is
kind of what henrik already went through
what is it you want to measure is it
many users or is it
you know
whatever it is
ui responsiveness
scenario duration how long does it take
to
run a report
and
as i just
said
think of what it what the end result is
you want to see i mean use good naming
for the tags and
fields and so on
then let's just jump into
the
client that
we had here
so
when you look at the log entries
here
so depending on what you are you want to
analyze you can for instance use the
version number to filter by default it's
always filtered to the latest version
because usually you're interested in
what happened now
but you can you know remove this filter
if you want to
clear filter
it could also be that you want to filter
on tag or whatever but
in our client we have this
[Music]
completely standard all list pages have
this
open in excel right
which will basically
um
yeah save this to the
folder where you have downloads
and i'll open it there
and
[Music]
so
if you mark everything and what we
experienced in the last two
workshops is that not everyone is
familiar with pivot tables so
i'll quickly show you how to create
pivot table you mark whatever you want
click insert
pivot table
i want that in a new
sheet
and so now what do we want to see well
we did remember to give the code unit
names
good names so we take that as a rose
and you can see
it's immediately populated
and i will increase
the size so you can also read it
um you remember we had something called
scenario and
[Music]
other measurements so
what we want to do is we want to be able
to filter so we have this operation
thing that's the scenario
we want that as a filter
and you can see i only want to
filter on
scenario in this case
and
a real price here is the duration
but not the sum of duration obviously we
want the average
and
so you can see click
on field settings and then you can click
average
and
what you can also do
you can add more of these actually you
can copy this field several times
because we you can add the average
but you can even
you know say i also want the standard
deviation or variation or whatever you
prefer
or min and max that's also interesting
maybe you are interested in max numbers
i don't want a lot of decimals actually
i want
none because we are talking about
milliseconds so something comma
something milliseconds is
close to irrelevant
so
creating purchase order i mean in this
these tests took approximately you know
three quarters of a second and sales
order a second
and open the list took
yeah that was quick
and now we also have the tag um to click
tag
and we can take the tags out as
columns
okay
yep
excel sorts things alphabetically so you
know hundred percent comes before 25
which comes 450 so if you want this
ordered
more natural you might add a zero in
front or add some
letter you know a 25 b 50 c 100 or
whatever you can do
or maybe you don't care
and creating
a chart which
looks better always
just click insert
pivot chart
and excel always seems to select the
best or suggest the best option
so in this case you can see this is how
it evolves with number of users
or whatever it is you're looking at
also remember we look actually we did
put in these other stopwatch things
so we can also say i don't want to look
at the code unit run i want to see
line quantity for instance right because
sometimes
uh i don't know what business you are in
but
you know if you have
reservation entries or assembly orders
it can be quite heavy
to change it
and apart from
the purchase order being a
quicker than sales order
it seems to
be linear or the flat i mean it's not
linear it's flat
with number of users
so i think you can play around with this
you know endlessly so i will quickly go
back to the
presentation because we don't have that
much time left
yeah
so
there are things you need to be aware
aware of there are some pitfalls which
simon will entertain about
no
i can repeat what you're saying
there we go okay
i'm sorry we're a bit over time so i'll
have to go through a bit quickly
so
i don't know about you but when i start
on new things and developing everything
sounds so nice and dandy but
there's never real life there's always
some caveats and gotchas you kind of
have to think about so the first thing
is of course
you might just use the demo data when
you're doing your initial testing just
remember
the number series ranges are quite small
so just try and
[Music]
and keep
extend them before you do these testing
or you will run out of numbers and get
errors
and then a more
common thing also is about logging which
is not caused by your production code
but rather by the testing itself
so
the test code you make
think of it as when do you actually do a
transaction
because you will not go in if a user you
know goes and do stuff on their document
every time they move around you will
save the document and the transaction
completes
so and often we tend to just you know
go ahead and just fill out everything in
one go and that's fine when you for the
production code but when you're actually
testing you want to simulate a real
scenario so just think about keeping the
transactions
limited so they actually reflect what
happens for user
and then of course uh
the number series i don't know uh does
anyone know about the allow gaps in
number series
few ones okay
very important thing uh because when you
create a number from the number series
we're actually locking uh
that during when we pick the number and
of course in certain cases you want that
you want to be sure that you get numbers
without gaps in sequentially until the
transactions finish you the next one can
get a number because it's required by
law like posting posted sales invoices
but sometimes you don't need it
and then you should enable
allow gaps because then you will use the
number sequence from sql and that was
not a non-logging operation but of
course if your transaction fails there's
a gap in the number
and finally save keys
we have um
if you have that save keys creates a
view in sql and when you update
something it will update the view and
during that transaction those rows that
are affected are locked
so when you write your test don't hard
code
you know item values which item you're
selling what customer you're going to
use because that's not realistic either
and then you get a lot of logging if you
have shift keys involved for example
and again think about user activity is
not a stress tool or stress tester it is
for realistic loads so we're probably
not creating a sales order every 10
seconds
and finally
think about background stuff if you have
a webshop it might ping your server
stuff like that just keep that in mind
and finally two more less obvious things
is when you actually run many user
sessions you might actually get resource
starvation on your machine
so you might have to split it up in two
and
paste testability can be a bit unstable
for those of you who have worked with it
you probably already know that pain so
make those simple and predictable so you
don't get errors
because of the
test failing
so that was a lot of
talks and we went through from
you know why you should use it the
customer scenarios and user story and so
on
i hope you got a lot of good stuff out
of this
so just to conclude um
the performance toolkit is a very useful
tool to help you determine whether or
not a customer case is feasible
uh
it gives you that confidence and also
you can convince your customer that you
will be able to deliver a performance
solution and another important thing is
it is also important to think about
whether this customer is feasible is
you
