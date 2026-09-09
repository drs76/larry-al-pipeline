# Double Trouble: A New Perspective on AL Testing

- **Source:** https://www.youtube.com/watch?v=djhImmMLyJo
- **Video ID:** djhImmMLyJo
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 91m20s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

thank you all and welcome to this
session called double trouble A New
Perspective on Al and welcome to Tech
days
2024 it's really great to be here I was
afraid a little bit you know uh look has
decided to split up groups like Waldo
and I usually draw big crowd and then L
has a problem how do how does he put
everybody in the same room so we split
up Waldo and me this year so we're now
competing for the audience and I was
pretty sure everybody would be there but
it's really cool to see all of you here
thank you for coming I hope I'm going to
deliver an interesting presentation for
you um I will just shortly introduce
myself for those who don't know me my
name is Vios slabic or Vio I come from
Croatia I've been an MVP for too long
now I don't know if Microsoft shares
that opinion we will see in a month when
they announce uh the extensions uh also
uh I've been talking a lot about Al I've
been involved a lot with Al um and
recently I have started really worrying
about writing testable code good code it
it became more and more important I come
from backgrounds such as C and
typescript I've done far more C and
typescript in my career than than Al and
for me in those languages testability
sorry testability is wrong term testing
unit testing is a no-brainer you just do
it and in a it's always kind of a
problem like we really don't test let me
see who tests here you may clap your
hands or or show yeah very few of you
really like okay some hands went up for
you who are listening this on
YouTube that is the reality we don't
test and why don't we test we will see a
little bit about that but it's not easy
that's the bottom line we don't test
because we become
inefficient um and for me it started
becoming a big problem in L so I I took
on a journey to actually try to to see
how can we make it better and here I'm
going to share my learnings share my
experience share my thoughts give you
some perspec itive on testing and U in
particular I'm going to talk about test
doubles and just one other disclaimer I
have talked about test doubles a lot
like a year and half ago give or take I
know I I delivered a 1hour session on
aropa anybody listened to that one let
me see few a few yeah okay so this is
not a repeat of that uh this is a
completely different story also I've
been speaking at days of knowledge three
time four times this year actually
anybody was there yes also that's not
the same talk I also talked about test
doubles and testing using test doubles
this is a story that you could talk
about or I could at least for you know
far more than than one session I could
talk for a week it is a Never Ending
Story So that said let me just go deep
into it this is going to be a deep dive
but I will not do coding like uh I
really don't have demos I have code to
show to you I will not run anything so
uh everything that happens will happen
happen uh just on screen uh before I
start I would just like to introduce
this thing which you may know as the
testing pyramid is anybody familiar with
the testing pyramid there is some theory
behind this like uh it it explains how
we should test our code like at the
bottom the foundation of this pyramid is
unit tests we should have a lot of them
the size of each block tells you how
many uh of each of these you should have
like how important they are the bigger
the block the more test you have the
more Focus you have there so unit tests
as you have as you can see are sitting
at the bottom of this pyramid they are
essentially the pyramid says they are
the most important and then on top of
that we can build upon like we could do
integration tests which obviously we
have less of them and then we go up and
we could call them whatever you want
like there are different kinds of things
that live on top of integration test
some will call it um end to end tests
some will say you know like some will
divide it into to System test UI test
accept test I don't know what kind of
test any kind of test and like these
manual tests they still happen they just
sit on top and then funny thing with
this pyramid is that uh you know as you
climb this pyramid certain things happen
and for example execution time uh
increases tests are slower the higher up
you are like it takes far more time to
run a manual test against any feature
than an automated test it's a
no-brainer and essentially unit tests
are fast integration tests are slower
and then System test may be slower and
then on the top we have these also
reliability like unit tests they're
reliable also integration tests are
reliable less so as you will see but
manual tests how reliable are really
like how how how far can you trust your
people that they have really tested
everything every single time then
efficiency and cost related to that
efficiency unit tests are cheap to run
and integration tests are cheap to run
but manual tests are very expensive to
run
and then uh they cost a lot especially
the error that they create costs a lot
because we find out about that very late
so this is this pyramid in theory but in
practice our realities and not just in
Al look a lot more like this far more
teams just have those people who say
like ah testing is not my job anybody
here ever heard that yeah just a few of
you good I want to work with you then
uh you know like people just say like
yeah I'm I'm a developer I'm not a
tester that's somebody else's job and
then companies often say like but who
will pay for that anyway like who will
pay for me writing these tests let's not
waste time there and customers
definitely shouldn't be paying for that
it's not I mean it's our manufacturing
cost when I buy a car I want the
manufacturer to do the crash test for me
I don't want to do it myself uh thanks
to Marco for this like I'm always using
this um and and then you know like uh we
we all give an honest attempt I know
that every company who who explored unit
testing or testing in general they have
honestly tried and then you know you get
those brittle tests anything you touch
the same test fails again and again and
again time after time and then you just
comment it out to take it like it so
that it doesn't stand in your way so you
can move on anybody experiened that yes
of course you have so and then you know
Consultants are in charge of testing
against PRS like you you you're a
developer you don't test of course so
you push your PR and some Consultants
consultant will now take it test it and
you know Consultants have their own
pipelines you know like they talk to
customers they handle documentation
whatnot it will take a while until they
process their pipeline so um it is
really a messy situation and I I don't
really have a way out of it other than
just say like okay let's retry from the
start and let's see why this has
happened and I would really like to take
this thing out of this dumpster um and
talk about unit tests today this is the
topic of this session unit tests
so what are unit tests let's talk about
unit test funny thing about unit tests
is you cannot just start you canot just
say okay good let me sit here in my Al
development environment and I will just
start testing in the crap out of my
solution you cannot let's see why so
what are unit tests first of all they
are granular they attack smallest
possible units typically functions but
also code units it all depends on your
structure and goals but as granular as
you can get that's the better approach
also they're isolated what does that
mean like anybody ever wanted to test a
warehouse shipment process I had and
then when you want to post like want to
test that yes you need a sales header
but for that you need a customer and you
also need to post a journal so a lot of
stuff happens the test becomes slow
setting it up becomes tedious isolation
means you want to test Warehouse
shipment in isolation of everything else
you don't need to go there you just test
this thing so that's isolation we will
see how we can isolate the system under
test system under test by the way is a
name for whichever unit we are testing
with a particular test we will see how
we can isolate them
and then unit tests really try to be
comprehensive they aim at 100% the
stability sorry coverage but 100% is I
mean you never reach that and you
shouldn't aim for that really but unit
tests are not interested in covering
every single line of code they are
interested in covering certain lines of
code and skipping others and making this
distinction between the two is important
and then when you do that distinction
when you separate peripheral code from
critical code unit test will want to
cover 100% of critical code and 0% of
peripheral code and it's achievable and
then they have to be repeatable just
like every test something that doesn't
hold true for you know manual tests like
same time same results and if something
changes in your code base the test
should theoretically fail because if
it's a breaking change for the test test
could fail or if you change test test
could fail there are only two reasons
why a working test may now suddenly fail
only two reasons first one is you change
the code base second one is you change
the
test and we know far well that in Al
very frequently there is a third reason
data changes right anybody runs
Microsoft's uh Bas apps uh suits locally
constantly Microsoft please put your
hands
down so we don't because because they
are unreliable we don't have their setup
there are 37,000 plus tests 15,000 of
which no sorry 15% of which fail if you
just install it on like a fresh
container because we don't use the same
setup they have specifically set up
their database for testing and they run
their pipelines against that setup but
for us it doesn't work that shouldn't
happen that's not repeatable unit test
should never do that and then frequent
like integration tests we are familiar
with them like I'm pretty sure a lot of
you do integration testing and we run
them in pipelines like you you push a
pull request and then some pipeline will
pick it up and run some tests and then
either all up thumbs up thumbs down but
tests run there that's integration tests
unit tests we developers run them
constantly like 50 times per hour if
necessary on our local machines which
means that they have to be darn fast and
if you ask me how fast well if your test
Suite unit test Suite takes longer than
10 seconds you have a problem and that's
achievable like uh I usually demonstrate
like some of my uh test suits like one
of my favorites it doesn't have that
many tests like around 250 tests maybe
300 now and that runs in under half a
second so that is achievable when you
test with unit testing approach so we
will see how we can get there as well I
will not really focus on performance I
just want to emphasize how important it
is and why it's not random that I want
my unit test to run fast I want this
instant feedback I know that when I
change a line of code if I broke
something I want to know it now not in a
week not in a month because now I know
what I Chang I can fix it immediately
but the later I figure out what caused
my test to break the bigger the problem
I have so this is what unit tests are
and here is an example this is a system
on the test for my real life project
where obviously I'm doing something with
stripe I'm creating a customer and then
I'm testing if this works this is the uh
actually this is uh not unit test this
is the code that I'm testing and I want
to test this path essentially I want to
see if create creating the customer
fails I want to see this error a
legitimate task or goal for unit test
you want to test every path so here's my
test like I as you can see like this
test looks a lot different than tests we
are familiar with for one um actually
sorry um why has this happened yeah
sorry yeah I want to show another yeah
this I want to show you how I test this
path yeah sorry so this path actually
like now I want to see what happens if
creating customer succeeds so I have
this version of the test
and if you pay attention to what is
happening in the test and the code you
can see for example I have no Givens
here I just have this semic cryptic
Factory Implement
something and then I'm totally
unconcerned with setting up sales
invoice header which is something that
you would have like three four Givens
against if you doing the the typical
traditional kind of test and then uh if
you take a look at this here like I want
to
control I want to send my execution down
specific path this is how I do it this
is how simple it is for me to say like
okay go there when somebody asks you did
you succeed you say true I did and then
in the end when I'm testing if this was
great I'm not doing like customer get
whatever whatnot I just call this one so
this is what a unit test looks like and
then uh like our experience with tests
is that it takes a long time to write
like you could say okay we Echo yes this
looks fancy but yeah it took you a while
to come up with this actually uh looke
always tells us the speaker
don't do live coding you will mess up
but I decided to actually write a test
like this this is what my experience
with writing tests looks like so I want
to write this case and I'm here I will
just start with test and then look at
this co-pilot suggests this one it sees
that I am testing fails now it wants to
check succeeds so I do this I accept
this I accept this and this and this is
the correct test save
done and
I would leave it for a second yes it
takes just a little while until you get
there like you need to write two three
tests but if your mocking framework is
in order if it's transparent not OPAC
meaning readable if your code is well
structured co-pilot does this for you
and I'm not kidding like 60 70% of my
tests are written by co-pilot and are
correct on the first go the other ones
are suggested by co-pilot and I have
maybe up to minute or two work on them
if I don't have anything in my code unit
then I have like empty code unit and I
want to start testing yes first test
maybe co-pilot will struggle but the
second it will be better and the third
it will be better because I have very
consistent naming of tests very
consistent flow how I test like what
like I I try to test happy path first
here I didn't but you know uh I I have
this consistency and co-pilot catches on
that and then if I'm starting with
something new I do a trick like I just
start coding tests in an existing code
unit then when I have three or four cut
that paste into new one and again I'm
productive co-pilot is amazing so it
really gets the job done um I I promise
to myself I will not talk about
co-pilots because everybody does but
here I go like it will write your test
for
you why do we do unit tests well
obviously I want to verify that
everything is in order I want to to know
that all parts of the system work well
together I want to bugs when they happen
immediately I want to have instant
feedback and obviously I want to be able
to refractor with confidence how do you
refactor if you don't have tests how
many if you refactor your code well all
hands should go up we should all be
refactoring all the time like we need to
clean up like every time we we touch
something we can probably do something
to make it better and I'm I'm pretty
sure we all have Legacy code that we
could improve and without tests that's a
difficult task to do
so I would like to talk a little bit
about this like um something I never
mentioned in my uh talks because I I was
thinking like there is really no point
in trying to present this angle but here
today I decided to actually take this
path that's why this session is actually
called double trouble it's a double pun
it's a pun on test doubles because test
doubles is what the session is about but
there is also this uh fight between two
schools of thought in test thing and
that's why double trouble because I will
present you why these schools of thought
are so different and what is it that
they are fighting against or actually
for so uh they are called Detroit and
London uh Detroit the guy actually over
there on the right uh it's actually on
the left for you yeah sorry so uh that
guy wants to test in a very specific way
and the school is called Detroit because
of the automobile industry because that
school of thought drawed from their
practices like we want to do it like the
car industry does that and the left guy
uh is obviously uh sorry right guy is
obviously called London and that's
because this school of thought has
developed in London at some point so
let's take a look what is different
between these two Detroit style also
called classicist style it uses real
dependencies all the time it focuses on
testing state
and verify outputs and it will have very
little emphasis on mocking it doesn't
truly care about that it emphasizes
realistic integrated scenarios that's
what Detroit cares about London on
another hand is called moist that guy
will isolate everything uh and you will
always use mock he he doesn't focus on
output verification he primarily focuses
on interaction collaboration he wants to
check
or verify behavior and he will heavily
use doubles and as I said like he
emphasizes collaboration between
components that's the most important
thing for that guy to see how all of
components collaborate together and
these come with trade-offs none of these
is better than the other all of them
come with some you know tradeoffs that
uh are important for example like U
Detroit like the big Pro of the Detroit
approach is that you will test realistic
scenarios like you test let's say
Warehouse shipment and it will go all
all full monty like all the way to
adjust cost item entries if necessary
because yeah you testing the real thing
um you have less mocking overhead like
you don't need to create mocks for
anything you just go and test um tests
are more stable we will see why actually
why are tests more stable when we don't
have mocks or at least when we are not
like using mocks or properly then uh
when mock tests become less stable we
will see about that and then these test
kind of build higher confidence because
you are using real things you are
testing the real stuff you're not faking
anything around so you can trust those
tests uh on another hand those tests are
slow mind you all of our tests are
actually Detroit style like the entire
Microsoft B app uh test library or Suite
is London style and we have learned to
write London style tests now the
question is are they really unit tests
or not that's also what these guys are
fighting about but technically yes they
are but also technically no they are not
but I don't want to really go there so I
will leave that up to you what is good
about London well tests are blazing fast
like all of those tests I mentioned they
are London like the tests I showed to
you they're London and by the way I'm
100% London guy like from here to there
like London full test are isolated like
I isolate everything or actually London
people isolate everything this
encourages good design because what
London forces you to think upfront is
design because you don't write a single
line of code without thinking how will I
test this what consequences will this
have on other aspects of the system so
this is in focus of London all the time
and then you have very detailed
verification London can reach 100%
coverage easily without much effort
co-pilot will get it there easily but
tests become very brittle we will see
about brittleness very soon also there
is maintenance overhead since you are
really concerned about what's happening
inside of those tests uh sorry inside
the system on the test you really are
looking you're covering every path
you're checking cyclomatic complexity to
know how minimum how many minimum tests
you want to create so all of these are
your consideration there is a lot of
overhead in there and then uh those
tests seem to be less realistic because
you're testing everything with mocks
like a mock here mock there so what is
it that you're testing I know that some
of you here will after one of my S like
what is it that you're really doing here
like you're just shuffling around
juggling these mocks are you testing the
real
thing well this is it it feels at least
that we're not and it becomes complex
the more you mock the more complex it
becomes and this is uh actually yeah
let's let's talk about why we need
doubles like I mentioned mock many times
I'm pretty sure let me see how many of
you know what mocks are okay not
everybody but a lot of you do so let's
see why do we need test doubles let
let's start with this one like it's an
extremely easy function to test do you
agree anybody who thinks it's difficult
to test this function well here are two
tests like I test all the paths through
this very easily I can verify that it
works whatever I send into it and that's
simple but my question is why is this
easy to test what is it that makes this
function easy to
test no dependencies well that's that's
a good one
but actually some something I it doesn't
have with to do with size at all like
Size Doesn't Matter you could you could
have a on line function which is
extremely difficult to test or 100 line
one which is easy to test what makes a
function easy to test is this Buzz is a
pure
function it has no dependencies
essentially no hidden inputs no side
effects like it doesn't change any
external State outside of itself it is
deterministic it will always produce the
same output based on the same input
that's what a pure function is it's very
very easy to test that's what makes it
easily testable nothing else it is a
pure
function but do this to it and then my
question to you how do you test
this how do you test
that this is an impure function it's
non-deterministic because it has hidden
inputs you don't know what f. bar will
do
you have no clue so how do you test for
that well we keep we do test that we are
testing it all the time so let's let's
take a look so um the problem with this
is that first of all side effects I want
to talk about side effects like it may
update the database this food do bar or
it may alter some Global state in some
single instance code unit how do do we
test for that maybe yes maybe no but I
do want to test for that also maybe it
calls a web service maybe I need to do
something about it like like it outputs
depends on the web service call so you
have both the side effect and hidden
input at the same time maybe it exports
a file so that's what side effect makes
to testability like it just makes it
more difficult for you to test and then
hidden inputs how does it compute its
return value you really need to look
inside to figure that out you are
concerned with that and then depending
on what happen happens in
there it can your tests can be I mean
they can range from very simple like
this maybe you know this is a typical
example like I read some setup and then
do some logic and go out and then my
test will have like two Givens and
that's easy but it could be difficult
like maybe I read a couple of fields
then read some more tables and then I
start shoveling up Givens on this Heap
and it becomes difficult to test or it
could be you know extremely difficult
like here you can say yeah yeah you
overdoing it yes I am intentional like
this is not a real scenario this is an
example but I've seen tests with 52
Givens you will see them too they they
exist in Microsoft's uh test suit for
Bas app that's the biggest one the next
biggest is 32 Givens and then you go
down like and I guarantee to you you
have the same situation in and it's just
inevitable if your Foo bars do this then
you will have to have those Givens and
yes libraries help to extent and
Microsoft has done tremendous job
helping us with that because we can use
their libraries to set up those Givens
easily and quickly and maybe we could
compress five of them in one call and
then yeah we don't have to care but
those Givens are still there and then
what is funniest here like so it
sometimes it can be outright impossible
yes I forgot to say that like this is
something that you cannot control so you
will not be able to test this function
at all but let's go back to this one
like I have a very important question to
ask how like if you look at this like
this is the flow like I go from here to
there and then I set up all of that all
of these given so this tightly coupled
code has deep testability
consequences because every time I want
to test something which is tightly
coupled to something else I need to look
into that something else to figure out
what is going on and you know uh it it
is a task like really I give it a name
like remember
we want to test this function that's the
function we want to test I'm I'm asking
you a question how are these given for
that when you look at the code you don't
see that you don't see that and you
should see that you should see when you
say given for for a test you should see
why is it given for this test and here
you don't see
that um I call this chasing Givens have
you been there like you start writing
test for that you know darn Warehouse
shipment and you need yes you need a
sales order but you need a customer and
the posting group and an account and
then another account and you need an
item with the posting group and some
more accounts and an inventory posting
setup and a location oh my god well yes
I'm exaggerating but this is this is
essentially uh very very big problem and
then
uh the tests like this they are often
fragile what does it mean for a test to
be fragile it means that it can start
changing its outcome based on stuff not
in the system under the test nor the
test itself a fragile test is a test
which can fail due to environmental
constraints like database changes like
some some setup somewh changes or some
record some more changes and tests start
failing we have all been there that's
fragile tests don't mix them up with
brittle tests brittle tests are those
tests which will start failing for
smallest changes in the code base like a
change some small thing and suddenly
boom five tests fail or one that's what
brittle tests are like you like they are
not resilient to changes you keep
changing stuff and yes uh Stu tests just
start failing and essentially this is
where most of the teams just give up on
testing that's my experience I've seen
it in in the practice like you just give
up because it takes so much time to
chase all those Givens and then it takes
so much time to try to stabilize those
test and then you just give up so um go
back to this how do we test this then
like what do we do there must be a way
well there is a premise that always
holds true about code like the code on
the left like this function
buz it must not care what foar does it
should not care like there is only one
thing that this function cares about do
you see what that
is the Boolean output value like buzz
receives a Boolean output and makes a
decision based on that output that's all
that buzz needs to know about
Fubar so uh if this premise always holds
true then we need to do something to bar
or Fubar we need to decouple it so let's
see what decoupling is well the first
step is we need to take the interface
out u in languages such as C you do
control dot extract interface and boom
you get an interface outside of a of a
class I am dreaming maybe having that
sometimes in in in Al like control dot
extract interface okay David fof is
coughing is is nodding to me from the
first row he did this uh code actions
obviously uh I didn't check this one but
okay AJ okay good but okay we we have
that so you extract the interface what
does it do it takes all of your public
procedures or methods or functions
whatever you want call them and creates
an interface object for that which
describes how Fu works and the Second
Step obviously you implement the
interface on on this
Fu and then you know uh if we look at
Buzz at this moment Buzz is concerned
with this bar right like it it really
depends tightly on it it's tightly
coupled to bar if you change bar you
need to change
bus and then if we just do this small
thing like we move this declaration from
local variables being a code unit a
concrete into
parameters which come into this function
as an interface as an abstract then we
can stop being concerned with the
concrete and we can start being
concerned with an
abstract and you could say yes this is
now breaking change because you're
pushing responsibility Upstream now all
of your callers don't compile anymore
thank you for breaking this for Meo yeah
nice job but it's so easy to fix you
just do an overload it's an illusion
it's not a breaking change this overload
that you add what does it do well it
calls the same function with the same
old tightly coupled
dependency which means that
yes it's no breaking change like we can
now keep calling this Buzz function with
old parameter set with the old input
against the old signature and that over
overload will pass or actually involve
exact same object in execution at
runtime so there is no breaking change
not logical not compile time problem
solved good so now we have
this what now what do we do with this
like cool we have an interface let's
take a look let's now start talking
about test doubles how do we use test
doubles there are number of test
stumbles we usually say mocks and I
would really like to to talk a little
bit about each of them I would like to
uh to say what they are why we have them
and uh how we may want to use them and I
will give code examples as I go so first
one is called dummy and essentially it's
a placeholder it doesn't do anything at
all we just use it when we need to pass
a dependency into some function you know
so we will use a dummy we will we will
uh just use an object does nothing you
will see code examples soon then we have
a little bit more complicated one we
call it a stub a stub provides
predefined answers to questions
like for example you have seen two stubs
already like You' have seen seen or
actually you have just seen one like uh
in in my code written by co-pilot I have
co-pilot has essentially used the stub
so it has uh said when somebody asks you
did you create a customer just say you
did and then stub answers with that
question and then we have spice spice
record interactions like how many times
you were called were you called with
which parameters were you called so
spice are there to tell us how the
components
interact uh we will use stubs to control
the flow like to make decisions or to
send code down specific paths spies will
be used to tell us if something happened
and how did it happen this is very
important for a London guy as you will
see and then Fakes fakes are working
implementations which are not suitable
for production for example in in C or
typescript or Java you have those
Frameworks like in C you have any um
yeah n unit in Java you have junit in in
typescript you have like mocha just I
don't know whatnot and uh those
Frameworks typically have mocks for
everything like you could just mock a
database in in typescript you just say I
need a mock for database you get a mock
for database and it's actually a fake
which fakes everything like your
application sees that as a real database
as a real thing everything it does
happens as if it was a real database
it's just a fake one it's you know
holding everything in memory for
efficiency purposes typically we do that
for efficiency purposes we don't really
have much opportunities to create that
in in Al because our language does not
have that power on that level we could
fake fakes make them explicit inject
them as dependencies but that is tedious
so I would not really like I I I haven't
I I tried like in in many of my sessions
I tried to present a real fake and I
just gave up on that like we don't
really have true fakes in in
al they are essentially or typically
just Statics and then you have mocks
mocks are combined stubs and spies
that's the simplest description they are
more than that they will more often than
not contain built-in assertions like
they will fail under certain conditions
like they try to behave like realtime
objects which expect specific things
which you can configure and and do funny
things with them and uh we will see
exactly what they look like I will start
with dummies so let's take a look at
this interface we have extracted it from
our class or sorry code unit and now we
um want to make a double for it we want
to uh create dummy this is the dummy as
I said it does nothing it's not even
concerned with returning any value why
because we know we will never involve
that in anything like this object just
sits there so the question is why am I
using it at all why am I defining an
object that does nothing that will never
be called what's the point well this is
the point imagine that I have this
function now which I do because I've
refactored it so this function cannot be
called without this Fu interface
and if if I only care about testing this
path as you can see foar will not be hit
in that path like I'm setting up the
test to skip around that like I'm
passing a value which will never hit
bar but my function still needs bar as a
parameter so I pass a dummy because yeah
I don't need to do anything with that's
a
dummy let's take a look at the St
same code example so we have the same
function we want to test and then we
Define a stub what good does it do well
if we want to test this path like okay
we enter inside here and then we want to
see what happens if Fubar says true or
what happens if Fubar says false
actually yeah I I forgot I I thought I
had a false apparently I skipped over
that so essentially you just say to this
Foo in this test you say set result so
when somebody asks you you respond with
true and then you see did everything
happen What should happen when you send
it down that path so essentially you're
just doing very simple U assertion there
that's a
stub and then a spy sometimes the only
thing you care about because you have
covered everything else you care about
knowing if a specific dependency or in
this case we would call it a
collaborator was involved during the
execution so on the left side we have
some code which does involve a
collaborator and maybe I just care to
know if this collaborator was involved
so I could just call the function and
then I just assert that no if these are
conditions under which this function is
called this collaborator must not be
involved and then spy will tell me and
then if it was involved my assertion
fails and I know there there is a bug in
my code because somebody has suddenly
called this method which shouldn't be
called under these conditions so my spy
helps me prove that bad or that truth
about my code and finally we have uh
mock as I said mock is just a
combination of like in in simplest terms
it can be very complicated but in
simplest terms mock is just a
combination of a spy and a stub
essentially you can use mock instead of
spies and stops just to you know control
the Flow by setting responses to
questions that will be asked from your
collaborators also you could spy on your
collaborators you could see if they were
involved how they were involved which
parameters Etc you could expect for
example just like I do here like I
expect it to be called with specific
parameter if I do then uh when I call
something if specific value was not
passed into it I fail which means my
test fails so I caner that collaboration
Is Not Just Happening but is happening
in the right way so mocks will do all of
those things mocks are essentially the
most comprehensive of objects and now
one question that I often get get asked
is do you really create all of those
dummies and spies and stuffs like would
I really end up having four different
objects for this thing here and the
answer is no why why would I um the the
the names are not U concrete names like
you need an object called dummy or you
need an object called spy and if you
need both a dummy and a spy then you
will create two no this is about roles
that they fulfill it's important for you
and for everybody who writes unit tests
to understand what is the role of my
collaborator and then you know okay I'm
collaborating like I want to control the
flow then it's a stub if you want to
control the flow and then I want to see
if collaboration happened and how it
happened then you know it's a spy that
will do that or if I just need an object
in there but I will not involve it at
all then it's a dummy so mocks can
fulfill all of those purposes so
typically people just use this term
mocks and most of people who do testing
or or know about testing in theory they
know about mocks or or at least they
have heard about mocks so this is what
mocks are the most comprehensive name
for all of these types of doubles which
we will involve in different roles in
our test so don't go and create 50
different objects just because you know
you have have uh 10 different uh code
units to to test and then you need all
of them like for each one you need all
all five types no there is no need to do
that and then some Frameworks like as I
said like uh just for example uh that
I'm using to test object ninja um that
framework just
has on on demand mocks you know like
anybody using ninja here yeah okay thank
you um so I test really quite a lot of
Ninja's backend because that's the most
critical part of it and then back end is
in Azure everything that happens happens
in Azure blob and then how I test that I
obviously don't write to Azure blob when
I'm testing I am mocking Azure blob so I
just say to just give me mock for this
class and it gives me Mock and then my
code sees that mock as a real class it
talks to that mock as if it would talk
to real class and then I can check like
essentially all of those methods I've sh
to you plus more are present on all
mocks created on demand and I have a
dream that at some point we may have
something like this in Al like you don't
need to go there and Define your
explicit mocks yourself you essentially
just say mock interface or mock code
unit or mock table just like we have
test Pages what are test Pages people
they're mocks they're mocks for our
pages so maybe at some point I I am
hopefully looking at micros Microsoft
here and and hoping for this I'm not
sure like but Microsoft is Microsoft
does care about testability like this
keyword that has just
happened uh and that I think I will show
I think I have a a screenshot with this
keyword it's something that aids in in
writing unit test and a lot more so
Microsoft does care maybe yeah maybe
they realize this this would be a nice
thing to
do so these two guys again let's now
talk and try to see like how they feel
about mocks and
doubles so when would these people
mock the Detroit guy will say no I will
never mock really I will mock if
absolutely necessary let's say I'm
talking to an external web service I
will mock that or I'm talking to a piece
of Hardware I will mock that but
preferably never I will mock anything
whereas the the the London guy that guy
will say oh I will mock everything like
uh like whenever possibly preferably
always
and obviously you can see that these two
are not compatible there there is a lot
of conflict that that uh comes out from
this and um I want to even though I'm a
London guy like I totally believe in
London approach and by the way when I'm
talking uh about let's say uh typescript
or C I'm a Detroit guy why am I London
in Al because in Al we often don't have
much choice like London has these uh
difficult uh obstacles that it puts in
front of us and we will we will keep
seeing them as we go but I still believe
that in Al at least with the State of
Affairs as we have London is the the
best approach but I still think that
mocks are necessary evil they I mean I
don't mock because I love to Mock and
because I really enjoy that or because I
can because some London people will just
mock because yeah just for the sake of
mocking that here we go thato it here
see this how I do it so that's that's
not why I mock u i mock because I have
to when I have exhausted all
possibilities I'll mock but if I can do
it without the mock I will try so let's
take a look at this like a real Overkill
that I've seen and I have been like I've
been there myself like I've been
learning like I'm sharing my learning
experience with you so I had attempts
and tries and and you know and maybe
when you see this you will think okay
but this is so simple why didn't you see
it up like immediately well maybe I'm
not as smart but it like let let's take
a look at this like we have this
function
here and it's a typical Al function like
it does something uh shuffles Fields
left and right then does some database
insert and done and you know in in ugly
Al function it would be a part of a very
big function probably somewhere in a
loop inside of a loop inside of another
loop inside of a case inside of an if
inside of another case but if you're
doing good job then you would you know
delegate that work into a function of
its own and then the question is how do
you test that well here we go here's a
test that legitimately tests this
function so what do I do obviously I
need to set up a vendor for this I I
don't see a way how would you be able to
run a test without doing this but it's
simple I don't need to write that vendor
to the
database and then I call this create
customer I pass this vendor and I pass
this number let's not discuss the logic
of this like why am I passing number
into this why am I not using number
series simply because I have I want to
have a simple example nothing else so um
I'm passing this number and then since I
know which number it was I read the
customer from the database and then I do
some assertions and if all true then I'm
happy essentially my test has passed and
I know that my code works and here there
are some problems essentially the and we
will see that as well database is my
biggest problem here like why don't I
like accessing database from my
tests does anybody have any idea yeah
slow slow well it's not that slow come
on we're 2024
like it's slow yes it is slow like we
are talking milliseconds but
milliseconds is exactly what you cannot
spare because they accumulate guess what
they do especially the more Detroit you
you go the more tightly coupled your
code is I've seen tests running for half
a minute I've seen tests running for
five minutes Microsoft doesn't have
those but I have seen those tests and
why are they slow because of accumulated
effect of database operations so if I
can avoid writing to database in my
tests I will avoid what is so slow about
writing to database well first of all
you need to write to the
database
obviously then you need to read from the
database to assert stuff and then when
you're done with the test you need to
roll back the data that you you wrote so
three database operations just to
validate a simple function like this and
then imagine that maybe I had to insert
a vendor and maybe I needed to call a
number series for this and maybe some
more things suddenly this test moves
from 2 milliseconds to 15 milliseconds
and then maybe more some more database
operations some more invocations to
something Suddenly It's you know 300
milliseconds you know what average time
to run a unit sorry a test is and I'm
I'm referring to Microsoft library
because that's you know the biggest one
I could see like the biggest one I could
really you know do some comparison
against 700 millisecs that's average
time it takes to run a test there are
37,000 tests Microsoft runs them every
day multiple times they do it in
parallel they paralyze like they
distribute that work they probably have
more hardware for that than fits in this
this room I don't know like but they
they optimize that but still this needs
to be done we cannot afford all that
Azure for for our tests we don't have
that you know Freedom so for us most of
test suits I've seen are not paralyzed
they are all serially running tests and
then you will start feeling those
effects and that's why I don't want to
touch database for my tests if I can
avoid that
so I want to like
with this unit test here on the right
side over there you can see that I have
really tested this function I know that
this function works so all it's hunky
dory I can move on let me move on I'm
moving on I have a function which calls
this function which I also need to test
right because there is legitimate code
inside there and I now want to to test
if Fu works when I call Fu will it do
everything that it needs to do and I
mean to test fu
I will call customer from and I know
that customer from works so I will hit
it again and it's slow and I will hit it
again and you know what like Detroit guy
says so
what where's the problem just do it like
go on and London guy like oh it's a
waste of time I need to do something
about it so London guy goes and says
okay let's create an interface called
Overkill let's implement this interface
on this code unit and then let's you
know inject this as a dependency into
this class and now I can test it like
this I can mock it I can you know like
spy on it I can uh fake it I can do
whatever so and London guy is now
happy but I mean just take a look there
must be a better way like and my
question to you is where where does this
end the moment you start doing this and
I was doing
this it has profound profound found
consequences on the shape of your code
base you can imagine that like if you
start doing this all over it costs yes
your tests are blazing fast you could
you wouldn't believe how fast they are
you don't you cannot measure that how
fast they are we're talking
microsc but I pay with the shape of my
code so let's try to apply a little bit
of Detroit philosophy here like this
function is impure it has side effects
it modifies the database and Detroit guy
says so what let me learn from him let
me say so what too but there is
something I can do to make this not my
concern I said this is an impure
function is there a way to make it a
pure
function well not really like I could
split it up into two functions I was
doing that as well like there was a blog
post I think it's the last one on my
blog where I'm doing exactly that and
I'm proposing that and back then I
believe that's the way it's not
I will really have to go back and yeah
but you know I'm not afraid to say I was
wrong because I was like that's not the
best way yeah it is a way you can do it
if you want but it you know it doesn't
make your code look better it just makes
your test run faster nothing else and
eventually maybe it starts hurting you
it never hurt me Beyond come on V look
at all these functions that do nothing
just database insert just so I can test
that assignment works as as an isolated
function that's just because you know I
hate impure functions so I Tred to get
rid of them but you cannot get rid of
impure functions Al is impure you cannot
do anything to it like it's a language
which it's not a functional language
functional languages care about purity
like fshp or I don't know Ada or lisp or
I don't know whichever but Al shouldn't
truly care that much yes it's better
that function is pure than impure but if
you cannot do it if you cannot make make
it uh pure don't sweat it keep it as is
so how can we make it a little less
impure well we are pass we we pass a
parameter by reference this VAR customer
into it and instead of having this
customer as a local tightly coupled we
inject it just like we inject a
dependency of interface type dependency
injection works on everything like every
time we pass a parameter we injecting
something into a function essenti
dependency so we pass this customer into
it yes technically speaking at least if
you talk to F person they will tell you
yeah this is still impure you're
modifying your input parameter that's
not allowed that's impure and I agree
that is impure but it's far less impure
than touching the database because tests
like you now
can test this easily you just pass as
you can see like a temporary customer
into it so you can test the same
function passing temporary variable by
reference and you do get it happens in
memory guess what there's your fake
database we have an implicit fake huh
what do you know so we can do something
with this now uh if we know that we can
pass this uh customer by reference we
could propagate it all the way so we
pass it by reference to Fu so that when
we call Fu we can not just run this code
we can now also observe this this is
what London wants London wants to know
what happened to this customer and if we
don't do anything we will never be able
to and we don't need a mock for that
either and London will be happy here so
we really can see everything that
happened on this and then you know uh in
the end this uh this is our code we
could add another overload I've
mentioned it already so we don't break
anything for existing callers this
overload does everything as it did
before I will call it peripheral because
I don't care about testing it that's
it's not critical code critical code is
this full signature Fu and I will test
this full signature Fu Detroit
style it will call another function and
I don't care because I can still observe
everything that happened I don't need to
spy I don't need to do anything funky
with any
interfaces as I said database is a big
side effect and and we cannot really get
rid of it and we should not like it's
it's impossible to to completely isolate
yourself from database in Al there are
tricks like this and it is not really a
trick like I think it's a good design
principle so just use dependency
injection so if you collaborate with the
customer record and you do you should
use it as a dependency and why am I
saying this like imagine that we didn't
have a record type just imagine for a
second like give me that that there is
no record type in Al that we really talk
to the database using some interfaces
just like we do in
C then I wouldn't be passing record
variable into a function I would be
passing an interface variable or a class
that implements that interface so what's
the difference like that's dependency
injection for me why doesn't like this
database stuff is a collaborator of this
function if I'm writing to database
which means calling database API which
is exactly what record insert is that's
database API if I'm collaborating with
that's my dependency I need to inject it
as a parameter so it is a good design
thing not bad and if it hurts you like
if you cannot propagate that all the way
up then just add an overload where you
need you will break things and everybody
will be happy so that is not a trick
that's a legitimate way how you can
improve your code and the stability at
the same time by applying a good
principle called dependency inversion
through dependency injection pattern uh
as I said in in other languages like C
you just say like I need a fake for my
SQL or I need a fake for my Ado in Al we
cannot do that but what we can is just
do dependency injunction with database
Pass records by reference where we touch
database if we do F set pass it by
reference and then you will be able to
test with a temporary set of data if you
collaborate with two reference records
pass both of them by reference and then
break it at some point where you think
it's dangerous and everything is going
to be fine so it has profound effect on
testability and Zero Effect on
runtime so
as you can see like a little bit of
redesign can really go a long
way and now let's consider this like
let's take a look at this function like
a simple code unit with three functions
one of them is
global one of them is local or actually
or two of them are
local so uh what am I trying to do here
like it doesn't really matter but I have
this simple call where something will
happen that doesn't cost much in terms
of runtime
resources and then I will call another
function which will do some heavy
lifting which will I don't know what
first call a web service then call a
database somewhere to read whatever then
pass it back to me I will do like this
much of code against it and call
something else and it becomes very very
difficult to to test that so what can I
do like look at this like Detroit says
well again where's the problem just test
it that's your code write your test be a
man for a while and London will say oh
my God ah what do I do like I totally
must mock something here I need to take
it apart so it's a big problem for
London
approach and let's take a look at what
will London guy do so London guy will
create this food
controller and this food controller
defines this method whatever it's
pronounced I asked Chad GPT G me those F
Bar that's how far I knew and then he
spit out like sped out like 50 others
which I reused around so this Q QX
something so I isolate that into an
interface because that's my heavy
collaborator and now I can mock that see
like I can mock it like I can just call
Bar passing this mock Fu into it and I
don't worry about this inefficient
collaborator and since the only thing I
probably care about in this test is to
know if that collaborator executed
because there is no decision against it
it's not involved inside of any Loop
there no decisions outside of it so it's
it's it's a very straightforward test
very easy for me to test and uh London
guy is happy now but there this is a
problem do you see the
problem well it's it's written there but
did you see it before it was written I
had to change the signature it's no
local anymore this qix is now an
internal
function how do you like
that
yeah it's it's it's bad like Detroit
goes crazy about this and London is you
know it's um he kind of you know U he's
happy for two reasons why is he happy
first of all he wants to isolate that
because it's it's it costs it costs in
terms of runtime performance during
testing it will slow down his tests
let's say this is the function that
causes the test to run for 5 minutes so
obviously the London guy does not want
that he wants to just skim over that so
um that's the first concern he wants to
just you know control it he wants to
mock it and the other one is since you
know you there is some bulky code in
there obviously because it takes 5
minutes to execute London guy wants to
test it in isolation
he wants to call this
function you know Detroit guy he will
tell qix through testing bar he will
just call bar and it will test
Everything full monty and London guy
wants to test every unit
individually and this is where they
Clash essentially this is where every
team suffers
like every team I talked to every
environment I was in I was talking about
this eventually this happened this type
of a discussion what do you do with that
and not just in
Al I remember a c conference where there
was a topic on this like how do we
handle this problem because you have the
same like let's just shift our minds a
little bit I I believe there are people
here who understand what C does for
example so in C imagine you have a class
and then you have a public method and
three private methods how do you test
those privates if they're heavy well the
same problem is here like you cannot
access them from your tests because your
tests are you know they are hidden from
tests so what do you do there and there
are approaches like interface approach
you create an interface for tests and
then you implement that interface
explicitly on that class and then you
talk to that interface through this
explicit implementation just from your
test nobody else will see that just you
will see that because only you know
about that interface because it exists
in another
dll complicated or another approach like
you you go and you create a derivative
class like you mark the method virtual
and you create a descendant class which
overrides that method and then this
class is something it's essentially
subass that you will call from your
tests but nobody else will be able to
call it also like a little bit less
complicated but also an approach but
this is always a problem like there is
always fights around this because it has
very very very deep uh consequences on
everything in the system there is no
easy solution so let's let's imagine
like what are our options really what
can we do
well first option that you have is that
you go and you keep your locals like you
just keep them local Detroit guys happy
obviously like why wouldn't he be happy
like that's how he tests he doesn't
really care about you know some thing
that Detroit guy will never do is change
the code for the sake of
tests that doesn't happen why would you
like you have code there are reasons why
the codes code is like this if you want
to change code you should change it for
reasons outside of the tests like for
reasons inherent to the code is design
bad redesign it but Detroit guy doesn't
say like hey tests will tell me when my
designs are bad but Detroit sorry London
guy says yeah yeah yeah that's why I
test like I want to improve my design so
I will I will see while testing the
design is bad and then I will improve on
it so
uh the local U any local function in
this case London guy want wants to test
them directly because they are
inefficient so London guy will say let's
just you know open them up let's just
you know turn them internal and this
really makes Detroit guy just give up
like he quits the job and goes out of
the company he doesn't want to spend any
more time there and there is another
object option which is kind of a
compromise and this is to decompose the
whole object like you just take this
heavy function move it completely out in
another function or actually another
code unit and then wrap this code unit
uh or actually extract the interface and
then use it as a collaborator in here
and then you know London guy is happy
because yes he can test that directly he
can fake it when it's used as a
collaborator Detroit is kind of yeah
okay well I I kind of could settle to
this because yeah it's not inside of
this object so technically it's not a
local that I'm accessing but again there
is this local functionality now which
used to be local probably for a reason
nobody should be calling that which now
exists as a non-local like still
everybody can access that and when you
do that like you you incre you you do
this decomposition and delegation and
all your complexity goes
up and it's the same everywhere it's not
an Al issue it happens everywhere and
here I will actually show you a demo
so um I have u i I wanted to structure
this entire session around this demo but
then I gave up so um I realized it could
be too complex I will share the examples
I I will definitely blog at some point
about this uh now I will have a lot of
time that that all of the events are
over I was really busy with uh with days
of knowledges and Tech dayses now but
let's take a look at this like what I
wanted to present to you is this
refactoring of resource Journal
posting um something that I don't
particularly like about the design of
posting in uh in in the B app is because
there is like so much repetition like
every posting routine has journals which
consists of templates and batches and
lines and then you have documents which
have uh you know headers and lines and
then you have a checkline and a postline
and a post batch and post post yes no
whatever but it's always like you go to
item Journal you go to inventory Journal
you go to fa Journal you go to inter
company whatever Journal you I don't
know what it's always the same like it's
the same design and code is copied over
and over and over and structure is the
same like um last year for one of the
events I wanted to present a fake
posting routine so I developed like some
I pulled something out of I want to say
where and and developed some demo
against a posting routine what was I
doing like for for half a day I was
copying and pasting like I I was looking
at uh Bay app trying to find the
simplest one so I have least amount of
work because I'm lazy so I but I think
it was fixed no not not fixed asset it
could be inter company some journal what
but it's the same like it does the same
checkline it does the same Loop through
lines filtered by batch and whatever and
the problem that I see with that is that
it happens all over like if you want to
create a new area you will have to copy
and paste all of that and I have a
feeling this could be and I don't expect
I this is not a critique uh there are
reasons why this is like this but in my
you know London view this would it would
be so much better that we just have one
uh routine for posting journals and then
we just passed dependencies into it and
whatever so I started with this resour
journal I never get too too far but what
I want to show to you is the effect of
extreme London like what happens if you
if you let a a London happy guy like me
into your code base what does that guy
do to it and I'm not 100% sure this is
good so but I I just want you to see
what happens when you when you try to
mock the Jesus out of something so I
started here with this
postline and uh essentially as you can
see this postline now implements like
every interface out there and their
sister so um obviously I have created
those interfaces and I will start here
with this on run and I will do run with
check and then this run with check calls
another overall load with run with
check and I'm not really sure why I did
that now I don't remember remember
anymore ah yeah yeah of course because
I'm passing this I promised you you will
see this so I'm passing myself as a
collaborator into myself so that I can
mock myself when I test
myself uh but I mean it it sounds funny
but I will run test against this so I
will find some test references actually
no because I didn't write test for this
one yet but you will see others so let's
go on I have this one which will be hit
by on run that's when you run the
journal posting routine and then uh I
have this one which I will hit by tests
like I will never call this because this
just uses tight coupling to itself it
essentially passes itself to this one
which receives itself as a reference and
it receives a reference of controller
type so what the heck is the controller
type well there are things that happen
in every Journal like you checkline then
you well obviously this is too concrete
as I said like I didn't get too far I I
just wanted to create a demo nothing
more than that so it does it's check
this uh like post is post the line and
it has this code function which I should
rename because code is a very bad name
for functions I can understand why
functions 5,000 lines long back in
1973 didn't have better name but these
days we should really be calling code
better and then this so This Is My
Controller essentially some comp like
interface which explains what happens to
a journal during this posting process
and then I can progress through that
like this uh
like I I say controller get G setup so I
can mock database access I wouldn't do
it that way today I I did it three
months ago so and then I will call this
run withd check on the controller so I
get in here and then I need to find
which one is is that so there is some of
these which will respond to that and
then uh essentially yeah this is this
one and then here I have this original
line I copy that and essentially call
this Post Journal which is another step
in the controller and it's obviously
implemented on myself here and maybe I
think I can check I can find this one in
tests let me see where are my
tests well I I have quite a bunch of
them but I think uh something is wrong
with reference counting uh whatever you
will get the code you you'll be able to
play with it and then you know I I again
call this controller and I pass some
more stuff like another controller I get
in here and then I check something else
then I process this journal and this one
is funny like cuz it does this like
workflow what the heck is workflow
workflow is another interface and this
interface like does
stuff I
mean at some point in this work I
realized okay this is obviously not the
way I I need not show this demo so I
prepared a better demo which I'm not
showing to you today because I really
want to finish that one and I'm really
proud of that one because as I said like
I'm also learning here I'm just sharing
sharing my Learning Journey with you
and uh I want to show it show to you
like when you when you become too happy
about this London approach it can get
really bad like my first step here and I
will show you that step like essentially
when I
have refected my general my resource
Journal line I will just go in
here that one is actually good because I
have nicely refactored this
uh code unit which had essentially one
big function and then when you look at
this you can really see what's going on
like it it follows this single
responsibility principle all all over
like uh I have functions which are
testable directly if I care to test
they're all local but yeah detroid guy
doesn't care that's where my London guy
kicked in and then I did that
Abomination which I just showed so but
essentially this is just a bunch of
smaller functions and it looks nice I'm
happy with how this looks because if I
really had a way to properly test that I
could and then I found some other
approach to this and I'm essentially I I
am going to complete this uh this
example because I really want to show
that this is possible to do in a really
clean way not this convoluted
like way which will have consequences so
um this this is something that happens
when you try to mock everything it also
doesn't work so Detroit people have some
point in there
this complexity that I've introduced
here it leads to one thing called
brittleness I've mentioned it already
and I will mention it again and this
really kind of looks like a big problem
and it very often is a big problem for
teams so what is brittleness brittleness
is again when you have tests so tightly
coupled to your code because how does
London work let's think of that like
London cares about one thing called
cyclomatic complexity because cyclomatic
complexity tells London
minimum number of tests he needs to
write to know that he has covered
absolutely every path to a function so
that's it's a tool which helps and then
London guy will try to cover every path
will just really look at every if every
case in there and will try to do
something about it mock it fake it
control it in a way and then his tests
essentially well they explained so well
what is going on in your code because
when you look at at test you really see
oh I see know why this is like this
those tests tell you everything but you
change one line you change one condition
you rearrange lines suddenly tests fail
because tests are so tightly coupled to
the logic that they test that they
cannot survive this change and this is a
problem it causes you know friction in
in in development process because the
more time you you spend on you know uh
fixing failing tests the less productive
you are with doing stuff that you should
really be doing which is writing
code and when tests are brittle minimal
changes will very often break a couple
of tests and especially when you are
about to do big
refactoring you may need to just throw
all the tests out and rewrite them all
from scratch if they are written in that
way and now funny thing
happens like uh Detroit guy goes oh my
God I told you I told you you will have
a problem there
see I told you
but London guy
says so
what so what I I want it to happen when
Detroit guy has brittle tests in mind
this is what he has in mind because if
this breaks oh my God yes I really don't
want to be that guy to fix this because
this can break who knows where deep down
like you touch something in Journal
posting and suddenly Warehouse posting
fails and you need to figure that out
and you don't know right away because
you cannot afford to run that test
because it's slow so your pipeline tells
you that it's failing 2 weeks
later and you don't have a clue what
broke that test so you spent three days
fixing that chasing more Givens or
whatnot and London's brittle test looks
like
this and the London guy says well uh
sorry uh there was something here I
don't know what happened with the
bullets but I will tell them so what
does London say about this London guy
said as well that's the
idea that's why I wrote my test to look
like this I expect them to fail because
if I'm testing a piece of code and
something changes in that piece of code
I want my test to fail that's the goal
of them where's the problem I will have
this test done in 15 seconds anyway I
will just kill the old one co-pilot will
complete the new one and everybody's
happy where's the
problem so this is this different
perspective these two guys have on
things what is problem for one is good
for another and vice versa it's always
tradeoffs and what do you know I managed
to finish a session in time which didn't
happen in I don't know how many years
the tech days so let's try to wrap this
up unit testing should be a foundation
of absolutely every testing strategy you
cannot properly say that you're doing
good development work if you're not
trying at least to do unit testing and
then as you have seen this tightly
coupled code where code always uses
concretes where you cannot do anything
but propagate from high level calls all
the way to lowlevel calls and you have
no way of controlling that you will
suffer from from some kind of a problem
either you will have a big performance
issue if you are doing the trit sty
tests or you will have uh issues
with mocking with structure and like
visibility of your methods if you're a
London Style guy and obviously you
cannot just start unit testing you you
you now can see that you can see why you
cannot just go and say yeah let me just
start writing unit test you cannot you
need to do something to your code base
you need to start making it testable you
need to take active steps on that and
test doubles can really help they they
are good tool they really get the job
done when used properly and these two
styles that exists uh exist which I
wanted to present in this session
essentially I wanted the session to
revolve around that they are both valid
they're both correct approaches you
cannot say that you know Detroit style
is is wrong or Detroit people cannot say
London style is wrong they will keep
fighting and keep fighting but both are
valid both have cons both have pros and
I hope you have seen them now like maybe
you understand those trade-offs better
you have learned from my experience so
you don't have to fall in that trap
because I've tried to share everything
I've learned while I was on this journey
and then something that you can always
try to do is you can try to strike a
balance between these two because as I
said both are valid and you can combine
them you don't need to be you know like
on a crusade for London or a crusade on
Detroit just learn from what's good in
each of those approaches and you as you
have seen like with that database
example sometimes you can just learn if
you're a London person you can just
learn from from Detroit like just
structure a code like do just small
smallest change and suddenly this tight
coupling becomes less of a problem you
can control that to an extent here and
there and then please start unit testing
you will be glad like it will be
difficult in the beginning but in the
end it always pays off thank you very
much so
um thank
you thank
you Q&A time we have nine minutes yes by
the way sorry uh I will bring you the
microphone and first four people get a
t-shirt
so who need needs bugs when you have
co-pilot yeah you have one no no well
here's Jo
copilot hello hello yes
um I was a question so I was just uh
wondering when you say do unit tests and
you have now shared your experience and
you collect a lot of experience still
for me it would be where to start is it
is it like uh is saying about the
elephant and pieces so should I start
with something small should I start with
something big well sitting on a really
old code base so we also have functions
like
code yeah but well we all do yes um I I
there is no no simple answer to this
question but I can tell you how I did it
in Al because I had a lot of testing
experience from from the past and I was
this Detroit guy which always who always
says so what because you don't suffer
from performance in C when you're doing
Detroit unless you're really doing
something funny in which case you will
mock still I was always mocking just not
that deep as as I'm doing it in a now
but my a journey was like this like I uh
I I was hit by a problem like the
typical situation that all of you have
certainly been in that uh you are trying
to change something and it keeps
breaking like you never get it done you
you always like you fix one feature
something else breaks and I was just
sick of it and I said like okay like my
tests are brittle they they serve no
purpose I'm constantly commenting them
out and and and on and off and kind of
always hoping now this test might work
uncommon then fails again comment do
something so what I did is I said okay
I'm now taking this code unit which was
really badly written I inherited it just
like you know Microsoft has in inherited
this entire uh Bay app you know they
have the same problem like I know for a
fact that they they want to solve that
somehow so um every team I've seen in Al
has inherited some code because
developers who wrote it probably aren't
there anymore so what my solution here
was there is this abomination of a code
unit which I inherited which I need to
do something about because it's my
problem now I just said I'm going to
start unit testing that and then I start
started writing him from scratch and
really I did DDD okay this function
start with test right function test and
then it grew and in the end I was happy
like I ended up Suddenly like before you
know it you have hundreds of tests you
can go on and suddenly it works it's
it's nice so essentially you you will
find a feature and then you will start
refactoring or maybe just rewriting it
but I I cannot tell you anything else
because it's a like I cannot tell you
just go throw everything out the window
or just go there and refactor everything
in one go like for example I mentioned
Microsoft like Microsoft suffers from
like they also don't like the fact that
they're testing their Suite with with
tests that run for 7 hours if you run
them in in sequence they want to improve
that but what I can guarantee I don't
know because I'm not Microsoft but I can
guarantee that they will not just say
okay now all hands on deck let's just
refactor everything so next release is
just tests and code which is full that's
not going to happen not there not in
Microsoft not in my team not in your
team not anywhere so you will actually
have to start small like pick an object
just maybe pick an object any object
maybe the the the least important one
and then just try with your team let's
try to unit test this then refactor it
then get it better and then start from
there that's all I can say really like
there is no
recipe thank you you're
welcome uh okay so Peter but then pass
the microphone over there and you're
done all right
um when you when you change the
parameters for a function to sorry sorry
sorry I cannot hear because I'm down
here
hell if if you changing a function to to
include an interface as a parameter you
say okay is it working yeah I think it
does you say uh okay you something else
will fail it will break so you just make
an overload and then everything will
everything will work again but isn't in
fact that also postponing the inevitable
because at some point you probably want
to change the other functions as well
isn't it I don't or do you want to leave
them I I don't think it's postponing
inevitable like you all have this um
trade-off like
I'm I'm changing a signature of a
function and then if it's a critical
function that's being called from 55
different places then I will probably
just put an overload in there and I
don't see a problem with that because
then all of those functions all of those
places that depend on this thing they
will just keep working and I will still
be able to test that but if I have two
places where I call it from and it
doesn't hurt to refactor both of them
then I will refactor both of them so I
will my first approach will not be like
by default I will not create the
overload by default I'm just saying that
if you need a solution that's the best
one but eventually I will have a lot of
overloads like in this code I showed to
you like this resource Journal attempt
at posting that's um full of overloads
and then yes it becomes difficult to
read that code like it's all clean all
like follows good structure like
functions are really single
responsibility concerns separated but so
much you know functions that have one
line of code and code next function
which calls the next one so uh yeah I I
like yeah it it it's uh it's a trade-off
so I say like don't just create
overloads if it doesn't cost much if
it's a breaking change for your third
parties like we are talking app in
appsource that you expect customers to
pte beetus out of then yes then you will
probably want to put an overload in
there for next release and then probably
refector when you have time or something
like that so yeah than microphone over
there
thank you you're welcome uh I just
wanted to ask uh how are you feeling
about test driven development because it
didn't really sound like I love it yes
so I I cannot say that I always do it
and I definitely don't do it the way how
Kent back says like go there write the
failing case
first that's just too extreme for me but
I I do it I love it like
because that's funny like that's this is
also my answer to the question who pays
for tests I pay for tests that's my
manufacturing costs but I am more more
more U productive I I my prod
productivity doesn't suffer because I
always have this confidence that
everything is in order so try that like
it it does work so again like I
sometimes find myself that I've I've
gone for a day without writing anything
in my tests but that is very much of an
exception like it's mostly like I end up
having like 20 30 tests every day
and you know it it starts paying off
pretty soon like at the beginning it
kind of it looks kind of pointless what
does this one test do one and one and
one suddenly you have before you know
you have a lot of them and then you can
you just feel so confident about your
code so try it yeah thank you you're
welcome uh who was
first
okay thank you uh I was wondering I
think I have one more shirt to give so
okay uh yeah I was wondering uh what do
you consider to be the correct approach
to the tests uh architecture wise like
would it be a
separate would it be a separate app must
dep yeah okay it must be a separate app
yeah we've been wondering that my demos
and I always say that I didn't say that
to today because I wasn't showing any
demos but my demos always have tests in
the same app just because it's so much
easier to just press F5
once rather than pressing it four times
which you need to do when you're
developing both tests and the app
because then app breaks test so you need
to like first publish fails then you
publish second time then tests so that's
why I put them in one app when I'm
demoing but for real life you you need
to have them separate absolutely yeah
okay like all separate one thing that
please don't do that's also something I
approach in my extreme London journey is
like create an app that describes
testability
interfaces that you then depend from
your app and test app and then only you
see those interfaces and nobody else
sees those interfaces it's that's a
wrong approach don't do that so
architecture wise two apps app test app
done yeah thank you
over yeah I was wondering about um well
this goes a bit over this uh this
session but I was uh with The Waldos
Workshop about the about the performance
testing yeah how would you start start
doing U performance testing uh would you
use the lond or I don't know you would
need to talk to Waldo like I'm I'm not
concerned much about performance testing
uh and I I don't think that these
principles apply to that yeah that I
think these principles apply really to
unit testing and maybe to an extent to
integration testing but but I don't
think how they would apply to anything
above that okay like System test
acceptance test you just do full mon
there like it's Detroit all over but I
really don't know like performance tests
they probably have their own londons and
Detroits that fight their own battles
and Crusades yeah yeah because when when
you have some some given when you do the
performance testing then what if
something changes with with a customer
you change a posting group or something
then it Go all goes boom yeah yeah well
I know but again like I I don't know
like this I I wasn't focusing on that
like it's totally not in in in my focus
at at this time so I'm I'm I really
don't know how to tell you what would be
the best with performance test maybe
next time maybe next year I don't know
like we still have 20 seconds left
anybody wants to say how good this was
yeah this is how much time a little bit
off topic but does your team use the
page scripting tool for acceptance
testing of any kind again like uh
no we are not there like we are focused
on unit tests right now like I'm
involved in a big project where we're
doing like big unit testing
implementation that's the goal unit
testability of everything agreed uh page
scripting tool that's something that has
recently appeared I didn't honestly I
didn't even look into it myself like I
because from my angle I don't need it
because that's so way up the pyramid
that for me I don't see how I could take
any advantage from it but the people who
need it like and I cannot tell you who
this is in this community or maybe at
this conference that you could talk to
but I'm pretty sure they are here they
could tell you much more about that
because it is a useful tool but just way
up there up per somewhere y
thanks okay so this is going to be you
know once I almost killed the person so
let's try to survive
everybody okay yeah I guess as many
people here we could have like decades
old product so my question would be how
would you start like to calculate how
much time would it would require uh to
make this decades old codebase testable
like we have to refactor we have to
write the codes how should I sell this
work to my manager this is a software
estimation question like how do you
estimate effort in development I I will
share with you uh a tweaked formula
which I just came up on the spot that I
learned from a community guy back in
Croatia back in the day how do you
estimate in software you take your first
educated guess then you multiply it by
two and take it to the next unit of
measure so if you feel like 3 hours it
is more like 6 days and if it's like two
months it's more like four years and I
would say with an effort like this like
I would do something like maybe times
three or times four instead so yeah I I
don't have an answer to that obviously
like it it is a massive effort every
time you try to do it like I haven't
seen a project or a team where it was
just
easy yeah yeah please yeah it's it's you
who I was talking about so but he can
share his experience with me yeah so
thanks sigy from LS
yeah well thank you very much people
enjoy the rest of the conference and see
you around
