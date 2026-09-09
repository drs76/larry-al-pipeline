# A webservice here, an additional frontend there, but how do we ensure quality?

- **Source:** https://www.youtube.com/watch?v=tIYimZtijq0
- **Video ID:** tIYimZtijq0
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 85m58s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

thanks a lot and uh welcome to this
session on ensuring quality basically
outside of business Central web services
front ends we're going to uh cover a
couple of things but first of all let me
introduce myself uh my name is tobas
Fenster on the business side I'm a
managing director at 4ps in Germany
which is part of the 4ps group which is
part of the Hilty Group by now not to
make things complicated um we are a
business Central isv focusing on the
construction industry on the B on the
community side I'm a Micron Microsoft
Regional director and business Central
and Azure MVP and Dr captain and if you
want to get in touch if you want to
follow along what I'm doing you can find
my contact information here including my
little podcast so uh reach out if you
want to discuss anything technology
always happy to to get in touch but with
that let's go straight to the topic and
as I mentioned the story is about
ensuring quality outside of business
Central so when I hand it in this
session um at the session proposal
process I was a bit afraid because
probably for most of you at least for me
for the company I work for business
Central still is front and center and I
mean we're at BC Tech days right so no
surprises there but as a matter of fact
it's not only about business Central
these days um we have the lovely
Dynamics 365 products don't ask me which
logos those are I just picked a couple
of ones at random so no clue but
certainly there is a lot in the dynamic
365 world that you also might want to
connect to so that already adds a bit of
a complexity then it's not only Dynamics
365 but it's also the Power Platform
including data verse so you have things
like power automate you have power apps
you have you have data where where you
put data and and integrate with other
systems so that also is an additional
Dimension then of course we have the
whole Azure ecosystem and I could have
put probably 150 logos on that but I
just used the ones that uh we will see
in the demos now so aure logic apps um
Azure functions VMS keyw the those are
probably some of the more usual things
you might use in Azure then you might
have something that you developed on
your own in this example it would be a
Blazer front end with the c so um front
ends that do specific things that you
can't do in business Central where you
addressing specific user groups or
something like this that can also come
into play and of course it's 2024 so I
had to put in a co-pilot logo and an
open iio Logo in here we won't touch any
of that so this will be an AI free um
presentation but of course this is also
part of the picture by now and the
question then becomes how do we ensure
quality if we look into the business
Central word we have a pretty clear idea
I would say we have um Al coded testing
we have the performance toolkit if you
want to um make sure that the quality is
right we now have the page scripting
tool if you want to do kind of front end
tests so there I guess we all have an
idea what we can do what we should do
what we hopefully all are doing to
ensure that the quality in business
Central is in the right place
but what can we do outside of business
Central that basically is the scope of
the story that I'm going to tell you for
the next 86
minutes
um maybe your approach is like this
maybe you feel it's getting slightly
warmer maybe you've been burnt now and
then but uh you're still fine it's okay
we're in a situation I can handle that
but maybe at some point this happens
where it becomes really uncomfortable
you literally get burned you may be
spending a night or two you're spending
spending a weekend fixing something
where you had no idea that you actually
had a problem so this is something that
can happen if you don't take enough um
interest in quality assurance if you're
not sure about the quality of your
application I'm not saying this will
happen to you but certainly it's a
better feeling if you have at least some
idea that you prevent the worst case
worst part of the things that can happen
to you so I'm German so definitely I had
to come up with a definition this is
what the i e says
no just kidding of course we're not
going to look at a at a formal
definition but um the idea when I think
about quality and I hope that resonates
with at least some of you is that the
foundation basically is that your
application works you need to make sure
that whatever you're providing to
customers to users to whoever you're
targeting um it does what it's supposed
to do and then of course it also needs
to perform so if it just does what it's
supposed to do but you have more than
three users and it breaks then you
probably also have an issue in your
application so it's not only about the
functionality but it's also about the
performance of your application the load
that it can take and then on top of that
um this is the room is on fire scenario
so if something really drastically goes
wrong that you maybe didn't anticipate
or you anticipated but you didn't
prepare in the right way for it um this
is also something that is part of the
quality
story so this is basically more or less
how I personally look at quality but
what has changed I would say in the last
couple of years is that performance has
gotten even more important so by now
depending on what scenario you're
running are you targeting end users are
you tar targeting internal people
external people um how patient are they
how willing are they to live with a page
loading for maybe two or three seconds
this could also be the case where
performance is at least almost as
important as working because if your
application works but you're um initial
screen takes five seconds to load no one
will see that it works because they will
already have left your application and
that means that we really need to
consider not only functionality but also
performance and then kind of the top of
um of this pyramid what if something
goes wrong how can we understand what
that might mean how can we um try to
find solutions for that scenario as well
so that is basically the scope boo we
will look into today functional testing
to make sure it works performance
testing or load testing to make sure the
application performs and a bit of chaos
engineering to make sure to cover the
the room is on fire scenario and for all
of that we will also look into um
automation because we not only want to
do this on demand but we also want to do
this continuously as part of your builds
as part of your releases as part of
nightly runs as part of weekly runs as a
part of um planned experiments whatever
but you definitely don't want to do all
of this manually um but have a way how
to automate it so we will look into that
as
well um so what's the structure of the
of the following session we want to take
um a look at playright for functional
testing you want to take a look at Asha
load testing which is using jmeter
behind the scenes more on that later um
of course for load testing and we want
to take a look at the asure chaos studio
for some chaos engineering for all of
those topics I'll give you a brief intro
to give you an idea how it works what's
it supposed to do um what we want to do
we will also take a look at a practical
scenario and the demo and that will
include the automation part so that you
can understand how this works and then
um I will also give you some explanation
how I've set this up links to um
repositories and so on that you can try
this at home basically my goal for today
would be to raise your awareness or to
give you an idea what you can do in
those three dimensions of quality
assurance and if you feel like yes this
is actually something that we should do
in the company or whatever um you have a
problem where this actually might be a
solution then I also want to give you an
idea how you can quickly start this up
so you don't have to start from scratch
but you can um get an I get a bit of a
quick start to play around with those
Technologies um the questions I hope to
answer in the end but we're working with
Azure and as you've seen maybe in some
of the demos before Azure sometimes can
be a bit unreliable especially the aure
portal so there might be some situations
where I need your help and will open up
for questions because aure is loading um
and then you can of course also ask some
questions one last comment before we
dive into it typically when I do
sessions this is based on a lot of
experience in production scenarios and
for the topic of today that is actually
not the case to be honest so if you in
the end ask me um please show me uh the
strategy for managing your chaos
experiments over the last 5 years I
won't be able to to show you that partly
because KS studio is not 5 years old but
also because I don't have that
experience so just a brief um caveat on
that but with that let's get started and
first of all let's talk about functional
testing let's dive into um the site
where we make sure that it works as I
mentioned the idea of functional testing
is that we make sure the application
provides the expected functionality so
whatever you want to deliver to your
user whatever your user expects from you
this is what we want to provide with
functional testing you probably want to
validate your core processes your core
uh features to make sure that everything
that is really crucial for your
application for the value that you're
delivering actually works you want to
look at the status especially for UI
testing you want to make sure that the
things that are Vis should be visible
are visible that things that should not
be visible or available are not um
available you probably want to check the
results so you're not only going to go
through the flow through the process but
you also want to make sure that the
result is the right one or that it fails
as expected which can also be the case
and you probably want to do this not
only with a specific data set but with
various ones um but I guess that's
obvious um key requirement for that is
to have an understanding of what to test
and great idea for that is to have one
or actually multiple test plans and if
you want to learn more um this is
something where my colleague Luke F Fu
can definitely help you he's a great um
great teacher and very knowledgeable on
that topic so if that's an interest I
just want to briefly um basically point
at him
so what we're going to use today is um a
tool called playwright which is an open
source framework created and maintained
by Microsoft but open source um that
allows you to do cross browser testing
for browser based um applications and
workloads either be chromium for the
Chrome and Edge family a web kit for
Safari or Firefox so basically more or
less the whole web world is covered
there you can do um cross operating
system so whether your clients are on
Windows on Mac or on Linux you're
covered and you can Define the tests in
any language that you want or not in any
language but in a lot of languages and
we're going to use node.js today so um
that is what you can get from um from
Play Ride and as key features that we
will look into we will see code
generation so we will record the test
but it also generates code and actually
very readable and very maintainable code
we will use the playwright inspector
because when you test the UI you need to
figure out where the different elements
are on a on an application and that's
what the inspector helps with we're
going to take a look at the trace viewer
that helps us to understand when a test
goes wrong or something fails what
actually is the problem and we will um
see easy headless execution in pipelines
so that you don't def don't need a
browser but you also can can run this in
a in a pipeline
environment so this is basically the
core structure of uh what we have in in
Play
Ride
the the core of it is here um play r
itself this is the engine that we can
run either as you can see here from an
editor or from the command line or in
fact also from a pipeline and you can
also already see the logos here this can
both be Azure pipelines or GitHub
actions or Jenkins or a lot of things
that can actually run play ride then we
have another aure service of course
which is the Microsoft Play Ride testing
service and this is just good for um
running higher workloads in different
environments so you can see here here a
Linux configuration a Windows
configuration different browsers and so
on but what we're going to do today is
we're going to directly use playright to
call our application under load so we're
going to skip the Azure service in that
case this is um basically how playright
Works in general and what do we want to
test today what do I have as an example
it's a little pizza ordering application
it's based on the Blazer Workshop by
Jeffrey Fritz and when I say based that
means that I changed the logo as you can
maybe already see to BC Tech days and I
might one little tweak to show you
something specific when recording but
otherwise I deserve exactly zero credit
for that application has been created by
Jeffrey and you can find it on the web
it's a um non-trivial Dynamic website to
show you a bit of of interaction as well
and we're going to do some recording
coding and
Playback and with that let's Dive Right
into our
demo and I have my demo VM here
so this is the beautiful app you can see
here I can register I can log in I can
order pizza I can give it a size I can
add some topics I can order and so on
but of course we don't want to use the
application directly but instead we want
to record the tests and in this case I'm
basically starting from scratch so you
can see here I basically have an empty
folder in um Visual Studio code nothing
in here but what I did is I already
installed the playright test extension
um ofvs code and what I can now do is I
can say install
playright select the browsers that I
want to use and make sure I also uh
enable the GitHub actions workflow so
we're ready for cicd already and then I
click on okay I've done this before so
it um already has the basics installed
if you do this at home it probably will
take five seven whatever minutes but
then it has playright installed and what
it doesn't say but does it also creates
an example project for us that we are um
immediately ready to go so as I have now
talked enough we should have the
structure in place here so I already
already have an example and then I have
a predefined test that I can use here as
well but as I mentioned I don't want to
write code in this case but instead I
just want to record it so I go in here
say record new and it says Coden is
starting I'm getting a browser and I can
now use this to interact with my
application so let's copy the
URL put it in
here and this is now loading um the
application and this step has already
been
recorded So first of all I want to
register need to make sure I type this
correctly because I want to log in in a
second again oh no this is the
password so I have registered typically
I would get an email I would need to
confirm but because this is a demo
environment I just get a link here to
confirm and it says yes thank you for
confirming you can already see with the
colors that playright is interacting
with this and um uh selecting
environments and um showing me how I can
address those elements so now I go back
in here I hit the
login need to use the same email address
and hopefully still can remember my
password and here we are logged in and
now of course I want to order some pizza
let's take the bacon one make it a bit
bigger add even more
bacon and put it on a silver platter
because why not slightly expensive but
anyway
and then let's use the mushroom
one and add some bell peppers I don't
know I don't care so this is my order I
click on order put in my
name of course I'm here right now so I
want to order it here I'm in
ANP Belgium is not really a
region anyway enter a postal code and
place this order and now I get the
confirmation that the order is here and
I can sign out so let's stop the
recording and see what has been
generated and there you can already see
that the code that is created by uh this
recording is not that bad I mean you
probably probably would put it
differently if you would create this
from scratch but on the other hand for
generated code it's not that bad I can
clearly see what it does it goes in a
place it selects a link um it clicks
somewhere it fills in information it
hits Tab and so on so what we can do
and want to do one little thing in
advance which is make the default time
out a bit shorter the default is 30
seconds and that means that we would
have to wait for quite a time um let's
do this in five seconds so we just run
the the test here and it
works until this moment and now I get an
error because okay my confirmation link
that you've seen before where I confirm
my my um my email doesn't appear I had
the show browser setting on the left
here activated and that means that
playright opens a browser in here that
exactly does the test and you can see
here okay we get an error of course the
username is already taken so I can't use
that one to um to register again so we
need to randomize the thing a bit
fortunately I'm in typescript here so I
basically have the full capabilities of
a programming language um um but I don't
want to struggle with the syntax so I
put this in
here and where did we use it first here
so I'm just going to random generate an
email address put it in here
and oh no the registration was
above
here and use the same email address here
of course I could also
oh I could also randomize
the um the password but no need for that
so let's run the test
again now we have a random username that
is
taken
and it blocks here maybe you saw it um
blink a bit here the reason for that is
that there is some JavaScript typescript
whatever that is running in the back end
uh in front end and is loading so
because I'm immediately clicking this
doesn't work now I could do some tricks
waiting for the JavaScript or something
like that but let's use the stupid
version for
now and that is that we just
wait for a
timeout and two seconds should be
enough and I'll run this once without a
browser so you see this also works
so let's run the test
again and you can always see here how
long did the steps take what did it do
and it ran through and finished so this
time we went through the whole process
with recording with a couple of small
adjustments but then we already have our
test in place in very readable very
maintainable code now of course this is
um the very the very Basics I just ran
through the process but did nothing else
um what I probably also want to do is I
want to ensure that some things are
visible that I expect to be visible and
on the other hand side things should be
not visible um that that should not be
visible so the easiest example of that
is the login after I log in I want to of
course see that I have been logged in
and then the the login button or the
register button should be invisible how
can we do that um I can run the trace
viewer with
my with my test that's one way and I
find it very easy so if we just run the
test again I now get an additional
window that's not directly the browser
but I can see on the left here once the
test is finished the actions that have
been run and on the right I can see um
the application how it looked like and
the test went through so now let me
scale that up a bit now I can also see
here on the left the different steps
that has been taken and if I click on on
such an action I can always see okay
what what is the action that has
happened what was the status before the
action what was the status after the
action so I can directly follow along
and see what what is actually happening
so before the log in is
happening let's
see probably here and then we are logged
in here let's say we want to make
sure um we want to make sure that the uh
the L logged in thing is visible for
that I can use the locator here collect
it and then click on that one and I hope
you can see with the colors um how this
is changing so I can just uh see in the
in the um Mouse over what is used but I
can also let it generate the code that I
need to locate that element down here
and I can easily copy it and then go
into my
code B4 uh no after the login
here and say
uh no not assert wrong language I
expect on the page to find this
element and for it
to
be
visible is it visible yes to be
visible and again now we have uh the
generated username here of course in the
next test that will be something
different so we need to use our email
variable again
put it in curly
brackets
and close that one so now we know it's
here and on the other hand side I want
to make sure that the registration uh
button is no longer visible so I can
just go here where it was visible use
the same locator action find my my
little login link and copy that locator
again go in here and
say I will
expect on the page this
particular um locator to not be visible
now I'm checking is has the login work
Does it show the logged in user and can
the user no longer log in because here
or she is already logged in again let
disable the trace fewer because then
it's a bit faster run the test again
and it went through so it has validated
that it's um there or not there and we
can go ahead so what happens if we run
into a problem for that I want to show
you the
[Music]
um element again so if we switch this to
not we know that it will fail but with
the trace viewer we can exactly see what
happens so it's going through the
test and goes
here so we're now in the place where it
should fail exactly and then I can use
the trace
viewer find the place where it failed
and see okay I have the locator it's
marking this is actually V visible I
said in the code I expect it not to be
visible so this is where it
fails so let me change this spe this
gives you an idea while you're
developing your um your test if you're
doing the the assertions or the expected
um you can easily identify what goes
wrong if anything goes wrong using the
the trace viewer and if you've seen
before we can also easily use the
browser um if we want to immediately
interact with the application and go to
the place where something goes
wrong so this is basic recording what
else did I want to show you oh yes of
course um now we have hard Ed all the
data but typically this that is not what
you want you want to use some Maybe
random data or maybe you want to use
data that is stored somewhere and the
easiest example for storing data
somewhere that we can use during a test
would be a CSV file so let's put in some
pizzas
here and as you've seen we also need
some
toppings so let's create a toppings
file and put in toppings
here and I have created a
little snippet for the code that I need
to put in
here which is the CSV parsing for that
we need an additional uh dependent
dependency or
package that we need to install but that
will be very fast then we need the
Imports that is basically just standard
typescript here
and with that we have the code in uh in
the pzas um array and in the toppings
array so now we can go in
here let me close that so I can see a
bit more this is our first
pizza so let's
use pizzas and I called
it selection you can see here um the the
header basically uh this is then
reflected in the object that I get so I
have my selection
here I have
pizzas and I called it
size and then we have the
toppings can I call it selection yes I
call it
selection
and put that one in here as
well then we we have the third one down
here we have the second
pizza and we have
the
second size so if we run this again and
I want to enable the trace viewer
because I want to show you something
here this is now no longer running with
hardcoded data Instead This is now
running with the data that has been read
from the CSV and of course this could
also be a web service or random
generated or even a request to business
Central um where you where you could
collect the data that you want to test
with but what is
interesting and that's what I wanted to
show you here if we now take a look at
the way how things are located for
example here you can see the locator
action that I'm getting here shows me
what has already been resolved from the
sources
but if I also take a look at the source
tab here where I get my um the source of
the test I can see that this is actually
taken from the array so I have both
views I can see how it looks in my
source code and I can see how it looks
um when it actually has been
resolved okay um that's what I wanted to
show you I think for creating playright
tests ah yeah one last thing um if we
take a look at the test that has been
generated you see also some ugly
elements here like this is the fourth
child of a div this is the fifth child
of a div and so on and if you compare
this with the place where I put in the
kinopolis um this one is fetched by a
label and the reason for that is that in
the source code of the application so
this is the the pizza application a
label is defined on line one and for
example on line two There Is No Label or
in a city d is No Label so if I have
access to the source code of the
application that I'm testing I can
easily make that change but if I don't
have I might have to point it out to
some other developer and what I can do
for that is I can go back in here in my
Trace viewer and find the place and now
what I can do is I can pop this out into
a real browser window and then I can use
the developer tools to actually inspect
the application under test again I have
the sources for that one so in my case I
probably would just look at the sources
but if I don't have that I can also use
the full um developer tooling to take a
look at that here and then see okay
there is a label def defined on that one
but there is no label defined on the
other one now the point is the trace
viewer is not only generating images
that are highlighting the stuff but this
is actually a snapshot of the
application that it was at that stage
and I can interact with that snapshot
using developer tools so even if
something is running in a pipeline and I
collect it as we will see in a second I
can still interact with that application
it's not just images it's a real a real
snat shop that that I can do something
with so as I mentioned um automation
that would be the next step um it's very
easy to throw down your
clicker hey I'm back um it's also very
easy to set up automation for uh
pipelines in that scenario I put on the
link here if you want to do this with
aure pipelines or GitHub actions or
other tools but it's extremely easy for
GitHub because if we take the sample
project here you can
see wrong we is code window that one it
already has
a uh pipeline or a workflow in in GitHub
action language defined for me here very
easy it just installs dependencies it
installs uh playright it runs the test
and it uploads the actions so um the
results basically so if I would just
Commit This and push this to GitHub
because it Triggers on all pushes to
Main and master and all pull requests to
Main and master it would immediately um
spin up that
pipeline I don't want to take the time
to do that but I want to show you the
result if I find the right window
exactly so this is basically what I did
in that case I still had an error but
that's actually more interesting but to
set up that pipeline I didn't have to do
anything but just commit and push the
rest worked automatically for for for
GitHub and it's not terribly complicated
on Azure devops as well so what went
wrong here I can take a look and then I
can see some Trace output that I can
probably already use but it's even
easier than that if I go take a look at
the upload artifact step
here I can download that artifact and
that's a zip
file and if I expand
that into my demo workspace that we've
just now been
using which
is in demo demo
one oh no I want to extract I don't want
to chase the
path let that here
[Music]
demo demo
one extract
that yes replace the files then I have
it on my machine and if I go in my
playright environment I can now say npx
playright show report and this is now
taking the data that has been exported
from the pipeline and I now get um the
tests I can see that they failed I can
take a look and now I'm back in my Trace
viewer as we've seen before so
now I can find the place where it failed
the locator is trying to find the slider
so somehow um the JavaScript in that
place didn't work and I can go ahead and
take a a closer look but that means even
if I run it in headless mode even if
it's running in a pipeline I still can
use the same tools as during development
to figure out what went wrong and and um
how I can fix
it okay that's it for playrite if you
want to do this at home you can find um
the application on the GitHub link here
it's easily runnable in a Dev container
so you basically just open run and it
should work then you need to install
playright in Visual Studio code um as
youve seen run the same install that I
did make sure you don't do that in a Dev
container because that actually doesn't
work as it needs to interact with the um
with the browser but instead do this
natively and then um you can get started
as we've done if you just push to GitHub
your CI setup on GitHub actions will
already work so if you want to if you
want to get started um this would be my
recommendation so much for functional
testing let's switch to the next part of
our little try angle which is load
testing that means that we want to make
sure that I that our application can
handle a specific load number of users a
number of requests whatever um giving a
specific number of resources so whatever
your back end is you can probably scale
it you want to make sure that this is um
the scale at at which you want it to
work and also that it responds within a
given time with an acceptable error rate
whether that that error rate is zero it
is or is maybe slightly above also
completely depends on your scenario of
course what you want to test is probably
again your core processes and you
probably want to test with expected
realistic scenarios I mean that's the
easy one that's the no-brainer with with
the load that you want to um that you
will expect you want your application to
work so this is certainly something that
you want to test but you probably also
want to test with more than expected
because who knows maybe you're more
successful than you think or maybe
there's a bug in a client or whatever
might cause excessive load this can
happen and you at least I think should
have an understanding what breaks so
what's the actual bottleneck if I run
into that situation can I just scale up
my infrastructure and it works or will
we run into an architectural problem and
we will get locks and Deadlocks or
whatever um if we have too many users so
if we go in that situation then we have
to re architect our whole solution low
testing gives you an opportunity that
you can test that and be prepared for
that situation when you run into that um
particular problem so that you're you're
then prepared
what you also probably want to do is you
establish a p a Baseline and compare
against that Baseline because then you
can use it in your tests um as an
example maybe it's completely acceptable
for a specific load that it takes one
second to return and in your um in your
builds you always see 300 milliseconds
as a return time so now uh this is your
Baseline and if you test this tomorrow
maybe it goes up to 600 if you only test
against your limit of 1 second that
would still will be a test that is okay
but actually you probably want to
understand why it went from 300 to 600
milliseconds so it's important to both
test against the limit that you have but
also test against the Baseline to make
sure that whatever you did in your
development didn't completely mess up
your your
performance um from a functional
perspective you probably want to test
the critical aspects like I mentioned
the login screen should load very
quickly otherwise your users probably
will leave or there are times when users
are yeah probably more critical like the
payment like posting um that also should
probably work as fast as possible and
then you have or you you probably know
what the resource intensive parts of
your application are like complex
calculations like data analysis like uh
bad writing of data and that is also
something that you should test to make
sure that in those critical areas you
also
fine what are we going to use for for
load testing today I'm going to use the
Azure load testing Studio which is a
cloud-based load testing service for
once Cloud absolutely makes a ton of
sense you have more or less unlimited
resources so if you want to uh create a
lot of load that's perfect um it can
generate load on Demand with very little
setup and you can even geographically
distribute it so if in real life you
maybe have the majority of your users
from Europe but you also have a
substantive part that is coming from
Asia and a substantive part that is
coming from North America or whatever
you can also simulate that easily with
aure load testing it has a nice quick
start feature that we will use um in a
second for simple to medium scenarios
where you basically have to or you can
stay completely within the aure portal
or within aure load testing um if you
need more and we will also do that you
will need um jmeter which is a very
established framework and you have that
to integrate with with aure Lo
testing for creating your tools you can
either use the portal as we will do or
you can use the as CLI or um
infrastructure code tools like terraform
or biceps or things like that uh to
create your
tests how does it actually work um as I
mentioned we have the Quick Test part so
that would be if you just put in a URL
amount of users and you go ahead and
this will in turn create a j meter
script or you already have a j meter
script so that would be um the second
option but behind the scenes It's Always
A J meter script this will then trigger
a test engine one or as you can see here
multiple a lot
and that will generate load towards your
application on this example the back end
of course also is on Azure but it could
theoretically also be be something else
but if we for example select a virtual
machine on Azure that is targeted then
we can also use as you can see here the
Azure monitor to collect um the
performance data so we're not only
generating load towards the application
but we also are getting the information
how our backend performs um is the
memory overloaded is the CPU overloaded
what what is actually happening at the
same time it's also collecting metrics
on the client side of course how fast
are the responses how many users have
been generated does the client maybe
even have a performance problem things
like this and then in the end it's um
collected and combined in that dashboard
that we will see so you have both the
view of your client side users response
times and so on and your server time how
does my back end actually behave and
again we can use this automated from
Azure devops or from GitHub and of
course we can use this manually um as we
will see in a
second so what are we going to demo um
or what are you going to see I'll going
to demo you're going to see um I have
created a little service to convert a
PDF into a PNG so an image file
basically just takes a PDF and using IM
image magic it's going to convert that
and I have put it both on an aser
function and on um on a virtual machine
so that we can see how those different
backends behave and um yeah the
performance they give us the code is
running in a container as I mentioned on
Azure function and on an Azure VM and we
want to generate some load we want to
use it to find out what the bottlenecks
are and then we're going to scale the
infrastructure or actually have already
prepared that we will see the results of
that so let's go into the second demo
and what you can see here is an aure
load testing resource um which you need
on the aure portal to get
started and I also want
to show you the
application which is the little PDF
conversion service so as I mentioned it
has a simple get request that just
Echoes so if we don't put in um if we
don't put in a parameter it will just
say hello Tech days if we put in a
parameter it will return that name and
the actually more interesting service
that we will look at more is uh the PDF
conversion that one collects or checks
if we have sent in a PDF if yes it then
uses image magic to um read that PDF
convert it into an image vertically
ordered
and return that image to the sender if
not it will send a bad
request what does this look like as an
example um it's also running here
locally so the echo just returns with 41
SEC milliseconds with a parameter it has
um the exact same performance if I send
in a small
PDF you can see that one here that is
what comes as a sample with image magic
so I just use that one this is the PDF
and this is how it is returned from our
service and to generate more load I also
used our little company brochure over
here that has a lot of images a lot of
content here and if we send that one it
will take roughly a minute to convert
that one into an image so I won't wait
for that one just show show you the
result in the end um so it can also
handle handle bigger
requests but to go back into the aure
portal I'll take that URL with me
because I will need that in a
second so I can go in here into the
tests say I want to create a new test a
simple URL based
test I can give it a name I can give it
a
description function back end for
example uh immediately run it and if we
disable the advanced settings then all I
need to do is put in the URL say how
many users I want how long it should
take and what the ramp up should be and
then I can basically review and create
so just running an amount of gets is
literally just the number of clicks and
then I get the get the results if we
enable the advanced settings it allows
us to do a bit more in that case I can
um add an input file if I want to but I
also can define a
request so this would just be our simple
get
again API Echo I can select different
HTTP methods I can add query parameters
as you've seen the echo one accepts um a
parameter I can set headers I can do
something with responses if you want to
if I want to use them in in subsequent
requests and then I can set additional V
variable
like environment variables or Secrets or
certificates if I um want to do some or
if I have it the endpoint secured I need
to set up the load
[Music]
again and then I can see here okay this
is expected to immediately go to 50
users run for a minute and then go back
to
zero I can Define some metrics that I
want to accept so for example if my
response time goes above 1 second then I
want the test to have failed if it's
below 1 second then um it doesn't have
failed or I can have an an error
percentage for example if during 60
seconds I get 90% error responses then
something is wrong then I don't want to
continue with my test and just stop it
so those are the things that I can
Define here as well it would take a
while to create and run that so what I
have done instead is I have
already prepared that to show
you so here this is basically the same
thing that I've just created once run
again the against the aure
function so you can see here we have an
average response time slightly below 1
second it ran for a minute you can see
how the response times have changed in
between and so on and if we check the
same for the aure function for the
virtual machine you can see that it has
uh taken roughly 10% of that so not even
milliseconds um I can also again see the
response time how it has changed the
request per second and so on and here
you can also see the server side metric
so I can see that for example my CPU was
basically not bothered at all so those
requests didn't matter of course makees
sense just returning something that has
been put in shouldn't create any CPU
load but this is a way how I can um I
can measure those
systems so let's do something a bit more
complicated which is our PDF conversion
as I mentioned for that we want to use J
Meer
which shows up in a funny way let's
see that's better so this is the way how
I can do more complex things for example
we now need to um upload a PDF so we
need a post with a PDF uh with a file
and that's not possible directly in the
portal so what we do here is we Define a
request um and that one is using some
variables for the protocol for the
server name for the port number because
those are different between my two
different back ends
it has the post as you can see here it
has the path which is the API conversion
and it uploads a file which is in this
case the 4ps brochure if I take a look
at my small request that does exactly
the same but it uses the snake Weare PDF
so with that I have defined um two
requests that we're going to run and the
load distribution between those two is
set up here so you can see that I have
only one thread basically simulating one
user for the big one
and for the small one I have used seven
threads um basically seven users so that
means if we run this test we're going to
have eight users one of them is creating
a big request seven of them are creating
a small request and of course they can
in J meter do a lot more complex
scenarios things in parallel
sequentially and so on but this is um
just for now to give you an
idea you have seen those variables the
protocol the domain name and the port
and as you can see here we getting them
from environment VAR abl because that is
what we can put in from the U from the a
Lo testing side into our jmeter test
which will interpret this and then call
the right back end so if we want to do
this I'll go back into my tests and say
I want to upload a script this time
again give it a name and so on um but
then I immediately get the upload where
I can now upload the jmeter uh script
that I have created and let that run
again those would be running 10 minutes
so I have prepared
this
here so for example let's take the first
one and show you the setup this is
basically the same screen that I would
have seen when when creating it you can
see here I've given it a name I have
uploaded the jmx file which is the the
test description coming from jmeter we
of course need our two PDFs that are to
be uploaded so I need to add those as
well as parameters we
have we actually should have environment
variables
um let me check
again let's
see okay either that was a glitch or set
it up in the wrong way but here you can
see the protocol the fully qualified
domain name and the port because that's
what different between the VM and the
aure function and I need to put them in
as environment variables so J meter can
use them put it in variables and then I
can use the variables in my
test nothing else here the load I have
in this um scenario added two engines
what an engine means is that it runs
whatever I have defined in my J meter
test you remember we had those eight
users one one big and seven small if I
run this with one engine then I get
exactly this if I run it with two
engines then I get two times um that
amount of load so basically then I get
16 users two uh running big requests 14
running small
requests here I could also do some
Regional distribution um I didn't do
this for my test case I added some test
criteria so the big one I expect to
return within 90,000 milliseconds or 90
seconds and the small one I expect to
return within one and a half seconds not
every time but in the 95th per so in 95%
of the cases this criteria should be met
if the test should pass also I want to
Auto stop it if it runs into 90% errors
within a minute and now for the
monitoring I can Define which backend
components I want to monitor so in this
case it would be the VM in the other
case it would have been um the asra
function and I can even set up which
metrics I want to monitor so for the
virtual machine I have CPU credits dis
read and right uh CPU percentage and
memory so that I have an idea what
happens on my VM while my test is
running um so if we take a look at the
tests here you can see when I ran this
first it successfully went through so
the status say done but it also shows
that the test result is failed why is
that if we take a look at that one we
can see it ran for 10 minutes it had had
a response time of an average of 1
second but you remember that we had two
different ones so we need to take a
closer look at that one it had no errors
so that looks good but if we scroll down
a bit you can see here the small
requests returned within 1.2 seconds so
that would be below our limit but the
big ones took
roughly what is this 163 seconds so
almost 3 minutes that is above our
threshold of of one one and a half
minutes so this time it failed because
it generated too much load why did it
generate too too much load again we can
take a look at the results here and
because only the big ones failed I can
also filter here so I'm only interested
in the big ones and there I can see okay
a number of requests ran but they were
too slow no errors but if we look into
the back end we can see uh the dis is
basically idling this is only a dis
right operations per seconds that should
be doable but we can see how the uh CPU
immediately spikes and goes up to 100%
And then leads to not enough performance
so what we can basically see that in
that setup with that amount of uses um
that amount of resources that we gave to
the back end it's not enough and we we
don't have enough
CPU if we go back out here to all test
runs um you can see that I did a second
scale up which added more CPU and in
that scenario it worked the small ones
got up to um basically half a second and
the big one got it got down to um almost
a minute but below our threshold so in
that one it's fine as I mentioned it's
also always interesting to take a look
at the different results so what we can
also do here is in the all test views we
can take a look at Trends and Mark one
Baseline and let's say that the middle
one is our
Baseline and then we can see uh the
different results here so basically the
dotted line here is our Baseline and you
can see the first one did less requests
of course the second one which is our
Baseline was exactly here and the third
one went up can also see the response
time here which went down basically more
or less linearly I also scaled up the
CPU linearly so this seems to be a
problem that we can solve by just
throwing more CPU at it and then we are
fine um I also have error percentages
and throughput and so on and um the
graphical view of course is nice if you
only have a number of results but it
also has a table view that shows you
what is your Baseline and how the
differences are so if we again for
example look at the response time middle
one is our Baseline the first one was
slower the last one was um a lot faster
so this is also um a chance where you
can yeah have more test runs and compare
them in a visual way that you have an
idea what actually changed between
between those test
runs um yeah I could now also look into
the function but um looking at the time
uh that won't add too much value because
basically it does the same it just has
worse numbers um but that's
it let me check what else did I want to
show you of course the cicd story for
for performance testing at well as well
again it's quite easy to set up Azure
pipelines and GitHub actions I've put
the links on here if you need the
documentation um and we will look into
Azure Pipelines this time first time we
looked in in GitHub actions the only
thing to be aware of uh because that
otherwise just runs into an ugly error
is to install the Azure load testing
extension that you can find for free on
the marketplace and then your Azure
develops organization is ready to run
performance
tests how oh
no I didn't want to stop the
presentation but I
did uh no
try
again here we are um go back to the
demo so what we have here in our test
view directly in the aure portal I can
select one of the tests and say setup
cicd this pops up um an integration with
Azure devops where I can select the
organization I can select the
project I can select the Repository
the
branch and a folder if I want to put it
in a subfolder and then I can click
create pipeline this takes a number of
seconds so again I have already prepared
this this is the result of the pipeline
as it appears as you can see the first
test run has also failed and I want to
show you why um so you can see what it
immediately puts in is and I'll Zoom
this in a bit again what it immediately
generates is um a fire that describes
the the test case in yaml so you can see
for example our instances you can see
the failure criteria that we have
defined with the 90 seconds and the one
and a half seconds you can see the
environment variables and so on so all
of this is here and then we have the um
the actual pipeline definition a very
easy one it just knows which ER
subscription and test configuration it
should use and in the end publishes the
results and then this is our um actual J
meter file uh XML but yeah if you take a
while then you can also um understand
that but still it fails and the reason
for the failure is that um we also need
our PDFs that were uploaded before and
we need to reference them so this is
something that the aure portal is not
automatically picking up if I show
you the working configuration
you can see what I did is I just
uploaded um one PDF and the other PDF
and also I added those as configuration
files and then um Azure devops knows
that it should also upload them and put
them in the file and then the pipeline
run actually
works as you can see here so this is my
pipeline
run and if I take a look at the
results I can see here okay those are my
test criteria I would have expected um
or it would have failed with more than
90,000 it only was 54,000 would have
failed with 1500 it only was 390 so my
test has passed I also get some more
inter information here so on the big one
on the small one the average response
times and so on so I can take a look at
at that here and I also have artifacts
published
here so if we go into to the published
artifacts you can see the results here
which has a report and then all the
detailed results is CSV so even after
the pipeline run I can also take a very
detailed look at um what has
happened so again yeah quite easy to set
up just a couple of uh buttons that are
pushed in in Asha Dev uh sorry in the
Asha portal and then I have my Asha
devops pipeline set up and as you've
seen in a yaml file if you want to
integrate this into your existing
pipelines that's also quite easy to do
that um oh yeah I of course also want to
share with you how you can set this up
at home um you have the URL here for the
conversion service either as an Azure
function or as a VM um there are scripts
that create Azure infr scripts to create
the VMS or the Azure functions depending
on where you want to test there are the
low tests in the low test file and there
also are shell script to create the load
tests so you can also see how you can
automate that and then if you want to
install j meter it's a free download but
you need to make sure to have Java
installed because it's a beautiful Java
application that you can run as you've
seen
here so let's move on to the last topic
um which is chaos engineering and um
yeah as I mentioned the the room is on
fire scenario so basically what happens
if something completely unexpected
something drastic goes wrong how does my
application um behave in that
scenario um what you want to validate
here probably is again your core
processes your core features to make
sure whatever you really rely on in your
application actually works even if if
something goes wrong badly it also helps
you to test your resiliency of your
application against the things that
shouldn't actually happen so I think as
as developers we typically try to also
um do that but if we can test it in real
life if we can introduce some problems
into our environment into our
infrastructure that helps us very much
to validate if that actually works and
then of course we want to make sure that
we have an acceptable fallback Behavior
so if something goes completely wrong I
don't want to see an ugly exception page
but I want to see something where the
user at least has an idea that politely
says sorry or even has a fallback to
some kind of limited functionality that
I can
provide um the interesting thing is what
to test because the things that you know
about that you expect to go wrong you
probably have already covered in your
code right so you can still use chaos
engineering to actually introduce the
problems so that you can make sure that
your code really does what you expect it
to do and keeps doing that on a
continuous way because you can repeat it
in your pipeline runs but you can also
use it to try some things that you don't
expect to happen and then the problem is
okay how do I know what to test that I
don't expect to happen so you can see
that this is a bit tricky but anyway the
tool gives you an opportunity to just
throw a load of problems at your
infrastructure at your back end and
basically see what happen
happens what we want to use for that is
the as K Studio which is an um
application that allows you to do
experiments which is why they call it
experimentation platform um and it
allows you to introduce faults and
stresses a fault means that something
completely goes wrong a stress is for
example as we will do I want to
introduce 95% load on my CPU so we can
figure out what that means and the same
or what what that um causes and the same
for dis the same for
memory um it's a managed service by
Microsoft you can use it um to spin or
you can spin it up in the Azure portal
to uh run your experimentations and you
can of course design and run your
experiments with it key features are
that running the experiment actually
means causing that issue causing that
problem on your infrastructure that's
very important because sometimes in the
documentation they say something like
simulation and that might cause you to
understand okay I'm only simulating the
problem that's actually not true you're
introducing that problem if you
introduce a service shutdown that
service will get shut down if you
introduce an unavailability that service
will not be available so you really have
to think a bit about uh where and when
you want to do this otherwise you might
cause real problems that's also the
reason why it has multiple security
measures that you make sure that you're
really only causing this on the
resources where you want to cause that
and the faults that you can introduce
are either Service Direct which means
that a service is directly influenced
again shut down a VM um shut down a
virtual machine scal set make a keybard
unavailable or it can be something that
is Agent based um which means that you
have an agent running on a virtual
machine and that is causing whatever
problem you want to simulate again for
example a CPU load that goes up and it
can be used both in shift left so early
in development scenarios and in shift
right scenarios where you want to test
your your production environment but
more on that
later so how does this actually work um
how does the stack for the aure studio
look
like we have as I mentioned either the
Azure portal or a rest API that can be
used to um trigger and to define those
experiments which is using the chaos
provider then we have the agent based
fults here and those as you can see are
running on Virtual machines and need to
introduce this agent and tell that agent
to create create load to create stress
whatever then we also have service
direct faults and those uh directly talk
to your Azure service infrastructure
shut down whatever and on top of that of
course your application your code is
running and that is then influenced by
the problems that are introduced by the
Kos Studio what you define in Kos Studio
are called experiments and those contain
those faults that um I've just talked
about which are available through the
fault Library so this is the general
structure of how um the as Kos Studio
works and we will immediately take a
look at it what I have prepared is a
little web application that uh calls a
back end a weather forecast backend but
that one is secured by a um by an API
key that API key is stored in a in an
aure keyb so whenever I want to call
that third party API I need to fetch the
the key from my keyw store it somewhere
in memory and then use it later but what
we want to introduce is just an
unavailability of the keyb what that
basically means my application is
relying on that keyw um but I take it
away what happens to my
application let's take a look at
that so first of all this is the
beautiful weather application that shows
me the weather forecast for an verb of
course what this does
is to make this probably a bit bigger it
has in the startup a configuration that
adds an Azure keyboard as you can see
here basically it connects to an Azure
keyboard to fetch configuration items
from from that aure keybard and when we
call the back end
here um we are getting the API key and
we getting the configured City so which
um weather are you actually going to
fetch and then it calls the back end
over here using that information it
checks if the response is successful it
checks if we're actually getting
something so it's kind of secure way to
implement that backend call and show the
response in the
application it also has a little reload
button here which refreshes the
configuration and the data so basically
whenever my my my uh API key maybe
um is no longer valid I can change it
click that little button and and it will
refresh or I can use it and that's what
I want to briefly show
you to change the
city so if we instead of ANB put in my
hometown and I want to make sure that I
didn't mistype no in
Germany put this in and go back into our
application and
refresh then now we are getting data
from okay so this works is expected um
but what happens if we introduce an
unavailability and what does it mean if
we introduce and unavailability let's go
to the K studio and the first thing we
need to do is we need to define the
target remember we actually introducing
the problem so we really want to make
sure that we're only targeting the
resources that we want and for that I
can try to
find um the
keywall over here that we used and you
can see I already have enabled it
because it takes a minute or two loading
so I didn't do that but I could just
click on enable here and then it would
be enabled now we want to create an
experiment and the experiment is going
to live in the right resource Group it's
the key VA
unavailable hopefully type like this
experiment it needs permissions and I
can automatically create a role for that
or I can do that manually if I'm even
more security
conscious and then I need I get the
reent designer which has steps steps are
always um executed um sequentially and
branches branches are executed in
parallel so I can both have sequential
and parallel execution here I'll keep
the names and just add the fault which
is the key W deny access you can also
see here this is basically the library
of problems that you can introduce so
there is a quite uh there's quite a
number and that number is also um
continuously
increasing and let's do the deny excess
I want to deny excess for 10 minutes and
now I need to select the target remember
this this is what we had to enable in
the previous step so I only have one
keyb I can either do that directly or I
can write a kql query if I want to uh
dynamically select the resource that I
want to Target let's add that
here review and
create create
and it's creating first thing it creates
is that um in that security role we can
take a look at that so you can also
understand which permissions it actually
gives that's especially important if you
want to run this in a pre-pro or even a
prod environment uh then you probably
really want to understand what is
happening here so you can see the
actions and the scope which in this case
is the whole the whole Resource
Group so while the test creat
oh it already has created it
perfect and go in here so this is now
our our little experiment that is making
the keyw unavailable and I can start
it and refresh and then it says
preprocessing and so on and while that
loads I want to briefly go back into the
keyw and show you what actually happens
in this case we have a networking
configuration in here and the default
networking configuration is that Public
Access is allowed which is why I can
reach it from my application and can
talk to it now once the experiment
starts let me open that in a new
tab so it now says it's
running if we now go back in here you
can see it has now allowed access only
from specific virtual networks and IP
addresses no network no IP address is
spef ifed so actually this means the
keyboard has become unavailable oh this
is what I meant in the beginning it's
not only simulating something it's
actually making changes on your
resources that you can see that caused
the problem that you want to simulate
and now if I go back into my application
I can still reload because this is using
a cach version but if I now were to
change the settings I put in a new key
or I put in a different city because I
want to change that and I click on
refresh config now it's actually crash
in an ugly way an unexpected error has
occurred reload and I can still reload
so maybe the fallback is somewhat um
acceptable but still this is doing
something that I probably want to fix in
some way it shouldn't be um this this
error
message now of course if we
stop before the end of the 10
minutes that also takes a second until
it accepts the
stop yes I really want to
stop ah canceling here we go um and with
that it should reset the setting because
now the experiment has
ended now okay I won't bore you with
reloading the aure portal point is after
the experiment has ended the change that
occurs during the experiment of course
is also rolled back so you don't have to
clean up afterwards or anything like
that that is automatically handled by
the Azure K Studio as
well so this was the simple example um
by just making a keywall unavailable and
then doing some manual testing of course
I could now have um in parallel also
created a playright test to to test the
functionality have that reconfigure
button hit and then see what happens um
but I can also do this the same thing as
a combination between load test and um
an experiment in the chos studio which
is the second scenario that I want to
show you where we're basically using the
same service as before so we're still
doing PDF conversion we upload a PDF get
an image file back and this time we're
using the VM based backend and then we
use Azure Kos studio and that agent
because now it's an agent based fault to
introduce some CPU load and we've seen
now that it performs without someone
doing add things to our environment
let's see what happens if we introduce
some stress into the environment and in
parallel run um the low
test now this is the difficult part I
have actually seen this work trust me uh
but unfortunately at the moment it's
broken when I tried to do this in the
beginning of the week it didn't work
anymore still I want to show how it
works because actually this is a bug and
I hope this will soon be fixed and it's
quick that you have an idea um what the
actual idea is so in
my KS Studio I have an experiment CPU
pressure that I can
edit and you can see here I can use it
to introduce CPU pressure for 5 minutes
with a level of 95 so that means the CPU
will be loaded up to
95% what I should now actually be able
to do is add an additional fault
which is the load test so I can start oh
no this was the
stop I can start a load test I just need
to put in a test ID and the the uh load
testing resource and then it would put
that in I run it but unfortunately then
an error happens I didn't get a response
yet but yeah either I'm I'm doing
something wrong than when I prepared it
the first time or um there currently is
a bug um but I can't show you that at
the moment uh but fortunately there is a
workaround and that also is the same as
for automation so again I want to show
you how this works in an automated way
and we can easily again create a
pipeline that runs our chaos experiments
what that could mean for example is that
you run this on a weekly basis where you
run your Play Ride test for
functionality you run your Azure low
tests for performance and then um you
validate that everything is still fine
then you start to introduce chaos
experiments to figure out if it's still
fine or if um then it it maybe breaks if
you want to do that um you have to
install the Azure chaos studio um
extension that you can also find for
free in the marketplace and then you're
ready to set it up and we can use this
as a plan B because in a pipeline I can
easily both run a load test and a KS
experiment just as different pipeline
steps and then we can see how it works
in
parallel the
setup is here
so we have this
pipeline which is basically the same as
we've seen before running the load test
so this is just the load test step um
that you've seen before I created it
with the same setup cicd steps that
we've we've seen before but now I'm also
introducing the chaos experiment I put
it as a u with no dependencies that
means that it runs in parallel I wait
for a bit actually 3 minutes to start so
we can first see that it performs as
expected without the chaos experiment
then I let the chaos experiment run
which introduces the CPU pressure for 5
minutes as you've seen and then in the
end we should um see that the low test
goes back to
normal so again what does this look
like we have our Pipeline and the
pipeline run here you can see that the
load test and the chos experiment both
have run the chaos experiment just
introduced the CPU pressure and then
stopped so no surprises it has worked
but the low test didn't and if we take a
look we can see okay um the average for
the small one was um 1,00 so that's
still okay but the big one took more
than three minutes so that one is no
longer okay if I introduce that CPU load
and the good thing is that we can also
take a look at the
results by checking the load
test so the load
scenario the
tests and I used I think that one
exactly and this is the test that ran
with the Kos studio and if we now look
at the requests you can see in the
beginning for the first three minutes
while the uh chos experiment was not
running that one was fine and then it
went down the number of requests if we
take a closer look because it's better
visible there on the small
requests you can also see the response
time here so in the beginning it was
okay below 1 second and then it went up
to above 1 second when the chaos
experiment stopped it went down again
and you can also see the CPU load in the
beginning it was going up but not that
much and then um the the 95% pressure
hit and we go up to 100% so this is the
way we can combine a load test and a
chaos experiment um in this example by
introducing CPU load but if your
application is more relying on disk or
on memory that would be easily doable as
well so you have an idea okay if
everything is fine my application
performs like this if we introduce some
stresses what does that actually mean
does it care or is it um a problem for
my
application okay um for chaos
engineering as well if you want to try
this at home you can find the link to
the application that is
using sorry that is using the um the key
wall to fetch the service key you can
also find uh the load test here you have
the different scripts to create the the
infrastructure or to deploy the
application and then you just introduce
the chaos Studio experiments as I've
shown you and take a look at the
application that basically concludes the
chaos engineering part and the last
thing I want to brief briefly discussed
with you is the question where should we
use this how should we use this you've
now seen the tools and I hope I gave you
an idea of what the scenarios are that
that you can use them for but still the
question is should I shift left so if we
look at the development um life cycle
should I try to do this as early as
possible or should I shift right which
is the idea to do this on a an on an
environment as close to production or
even production itself um to make sure
that that works for functional testing
that's very easy functional testing
shift life shift left as far as possible
the earlier you find a problem ideally
directly in vs code running the test
that's perfect because then you still
know what you have done probably what
might have broken it um you're
immediately able to fix that problem and
the earlier you find the problem the
cheaper to fix is once it's rolled out
to the customer it's a lot more
expensive to fix the problem so make
sure you do this on the left of that um
of that timeline as much as possible for
for performance testing it's a bit more
interesting because you can use this on
a shift left approach to catch relative
problems remember the the Baseline story
where we said Okay I want to have an
idea how long should this take during my
builds or maybe how many resources
should that take during my builds how
many SQL calls should that be during my
builds that is also something I can
catch with performance testing and then
if I run my pipeline again tomorrow and
suddenly it's worse then I know okay I
have a problem maybe I'm still within my
limits but I changed something that has
an impact on performance at the same
time shifting right also makes sense
because you want to make sure that
whatever you have as an infrastructure
for a production environment or a
pre-production environment is actually
able to handle the load that you want to
throw at it so you can also use
performance testing maybe even on a copy
of the production environment with the
same infrastructure with the same setup
to really figure out okay how much
performance can we actually um give how
much requests can we handle when is it
breaking what is actually breaking so in
that scenario shift right as far as
possible and the last one is chaos
engineering again shift left to have an
idea of what actually goes wrong pretty
early so something like the keywall
problem that we've seen that is
something that you can basically
identify during development if you use a
chaos experiment but at the same time if
you have your production environment
that has Azure availability Zone
redundancy automatic scale up all those
fancy things that you can make that you
can do to hopefully get more resiliency
in your application you then to validate
how that works so once you have the
trust built up and you have an idea of
what Kos studio is doing and you know
exactly what the the experiments are
causing you might go so far as to maybe
not during the the most interesting
hours of the day but at some time
actually run the chaos experiment on
your production environment but know
what you're doing and always be ready to
hit the cancel
button okay
that's it um as a quick recap what did
we do today we took a look at functional
testing make sure the application works
we took a look at load testing make sure
the application performs and we took a
look at chaos engineering for those
weird problems that might pay um pop up
in case something goes wrong we also saw
automation on demand and continuously
and the products we used were playright
as a low testing and the as studio and I
hope with that I gave you an idea of how
quality Insurance can work even outside
of um business Central gave you some
some food for thought and uh also some
instructions if you want to try this
back at home so you can have a quick
start that's it for today now I would be
open for
[Applause]
questions
yes thank you uh when you were doing the
playright testing
uh is there a way to
group set of actions that would be
performed for every single one yeah um
you're basically in a full development
environment so it's typescript so you
could just put them into a function a
typescript function and then call that
in a loop or whatever so you're open to
do whatever you can do in a programming
language we are selecting stuff by div
name or or stuff like
that how do we handle when Microsoft
changes something yeah that's one of the
reasons I mean I also try to use
playwright with business Central and
that works surprisingly well to be
honest but of course for the things
where you have dynamically generated IDs
like in business Central an approach
like this takes a lot of effort to
maintain so I wouldn't go with playright
I'm actually very happy about the page
scripting tool they presented and I
would very much advise to go for that in
that for Play Ride Play Ride is more
when you have a more stable environment
or the sources of the application are
also under your control so you can make
sure you're not doing something that
would make it almost impossible to test
it further
questions
yes one of your uh one of your testing
uh
concerning the G gmet uh you have
created a a file GMX which you uploaded
within the load testing uh I'm wondering
if if um not sure really is it possible
also to create like a collection of API
within Postman or within uh uh insomnia
and publish that to uh low testing in
Azure and use that as a
test not that I know of no you you
either have the UI as you've seen where
you can directly put it in or you have J
meter of course Postman or something
like that would have the same kind of
information I didn't look for it maybe
there is someone who can create from
post manage AMX file but I haven't seen
it I think it's not natively there but
maybe there is an extension no I mean it
it doesn't have to be a GymX file but
I'm wondering if you create a collection
of of of apis request and use that
within the
load test St ah okay so you basically
want to call a back end through what
through a collection of
postmen you want to call a postman
script Postman connection from a low
test yeah yeah I don't no I don't think
okay I don't think so not that I'm aware
of again okay okay thank
you other questions yes
toas hi have you tried to uh run the
page scripting part in business Central
using play right in a
pipeline I don't think you need
playright for that I think they will
come up with pipeline support directly
but yes theoretically you could use the
playr you could use playr to trigger the
page scripting I think it would be
interesting to validate the results and
playright with business Central is so so
so I would rather wait for the pipeline
support for the page scripting tool to
be honest you think that's on the
backlog I at least heard so of course
I'm not Microsoft I can't promise
anything but I heard so
yes further
questions
anyone NOP then again thanks a lot have
a good dinner and enjoy the rest of the
conference
