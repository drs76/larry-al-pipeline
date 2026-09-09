# NAV TechDays 2018 - CI/CD for Business Central

- **Source:** https://www.youtube.com/watch?v=5tShC8g2s8E
- **Video ID:** 5tShC8g2s8E
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 100m01s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

good morning everybody good morning
ah like that is the kind of response i
like
i mean
you could say clap your hands but if you
just talk to us that is even more nicer
right
i decided that we cannot simply not
beat
uh the piano register that was done
yesterday so
with the other hand we try to
go for the most boring session ever
that's not going to happen either
right so uh
welcome to this presentation about
cicd
with me on stage
introduce yourself please gentlemen yes
my name is connor gason gasson
i'm
born in iceland live in iceland and work
for an icelandic company
as a well solution architect and some
other roles i've been mep since 2013
and still quite enjoy it
i'm camille sachek from czech republic
i'm working in a
company in avertica
and i'm mvp since 2005.
all right thank you so i'm aaron john
kaufman i'm working with cloud ready
software i'm from the netherlands
and
actually this morning i got a question
from one guy who said to me what are you
doing on stage actually about this topic
i can tell you
those guys i talked with them about this
topic
these are the gods i mean they know
everything about it
and they try to teach me
and
well it's up to you to judge if they
manage to do that
anyway
if i understand what they are doing i'm
sure everybody in this room can
understand right so uh that's why i'm
here to prove that they really can teach
you something
and of course i'm trying to
teach you a little bit myself
so um we're going to talk about ci cd
what is what is cicd just
as the theory behind it
uh also why you might want to use it
um
i hope to give you some good reasons for
that because those guys convinced me to
start using it and actually i am using
it on almost daily basis
we're going to show you how to work with
repositories how to create them how to
create a build pipeline how to work with
browse policies so there comes kind of
tying stuff together together with a
delivery pipeline and the deployment
pipeline so
uh i hope we can manage that in just 90
seconds
uh minutes i mean sorry
i'm really not so fast okay
let's let's just see where we can go
so
a lot of people think
it stands for this i mean
continuous irritation continues
distraction
i showed this slide earlier this week to
an mvp and i'm going to
say his name but he said oh wait
there's a session about my wife
[Laughter]
i'm not going to say his name because
you never know if
his wife is watching also so
anyway
i mean
if you think it is this it is uh
irritation is distracting
just stay for the next 90 minutes and
hopefully at the end you say and
understand why it is not really
irritating it should help you
and it should not distract you from the
daily process the daily development
process but really help you and support
you to build better software and to be
more productive
so what is cicd then if it is not
irritating and not distracting you
so the ci what that stands for is
continuous integration
and with continuous integration what we
mean
is not integrating i say the new
versions of microsoft into your branch
we are talking about what you as a
developer
do every day
develop
and you are working together with your
co-workers you're working together with
your colleagues and you are now working
on your local machines hopefully if you
use vs code and also driver you're not
talking about seaside here um you're
working locally but your co-workers need
your work your co-workers need to to
build on it need to use it whatsoever so
you need to share your work with others
and
there should be kind of a shared main
branch or shared repositories yet
project where everything comes together
and that is what we talk about here
integration integration of your work and
work from your
co-workers
um the thing is if that happens you know
we all know that there could be all
kinds of problems coming up you do
something a co-worker does something
that could conflict potentially and you
want to manage that you want to be sure
that it works you want to be sure that
uh
you don't break anything so you want to
validate and it's going to be and we're
going to demonstrate that those guys are
going to demonstrate that how to do that
by creating automatic builds running
automated tests etc against that build
so that build is going to test your work
together integrated with
your the work from your co-workers
so that is continuous integration
continuous delivery is the other term
cd actually stands for two things
one of them is continuous delivery and
with continuous delivery we talk about
not only integrating the stuff but also
about producing your software and to
builds built that can be delivered built
that can be released i'm not saying it
will be released but it can be released
so
that is a process that is on top of that
continuous integration
and with that if an integration works
successfully integrates it should
potentially be possible to deliver that
to create a deliverable that can be sent
to a customer
and when we talk about sending to a
customer we're talking about the other
term
deployment which cd also stands for
and continuous deployment is in fact one
step further than continuous delivery
with continuous deployment it is
going to be automatically meaning that
this not only delivery not only creating
a release and then
manually push that release to a customer
it's also about automatic deployment to
that customer
so
in fact the moment that
you are ready with a new delivering or
building a new feature and you say now
i'm done
you start or you kick off that
integration process if the integration
process goes successfully can be
successfully ended it automatically is
going to create a delivery and the
delivery is then automatically being
deployed to the end customer that is the
id of those
terms
to put that into a picture
where you see that here we have uh the
source you're building the source you're
developing that
and the continuous integration stops at
building the and uh the active the app
fire would say so the the end result of
it continuous delivering
deliveries also including test etc but
then
delivering it to the customer is a
manually trigger saying put i'm pushing
a button to deliver it to the production
while continuous deployment also takes
away that manual step
so
continuous integration what do we need
for continuous integration what you need
in
first place is automated tests
and you will see the word test a lot
here
automated test is
something that you need to do in
continuous integration and of course you
get less books
hopefully yesterday i heard
someone from microsoft who's supposed to
know how software development works tell
you that every software developer
creates books
well
actually he said that we spent half our
time in a debugger
that's probably not because of finding
bugs in my view it's also because we
spend time in the debugger it's just to
find out how that stuff works that we
just created
not just to find books of course there
is a book just say okay we have now
constructed something does it really
work in the flow that i expect it to
work
what you also need is a process
to ma to monitor a main repository we're
going to show you that
i mean if you have a central repository
where your code comes together
then the moment someone pulls the trick
and say i'm ready with my work i'm going
to send my piece of code to that shared
main repository then
something must happen automatically that
automated test that must be pulled off
automatically you should not go into any
site or comment or whatsoever and say
okay now i need to run my test my the
test myself
and that's something we are also going
to demonstrate actually
so the idea is that developers
merge their changes as often as possible
well there is of course up for
discussion
what means as often as possible some
people say it should be every day
but i know for sure that
you don't agree with that i mean you can
develop on a feature and the feature may
not be ready at the end of the day to
create a delivery for so it could happen
that it is not as everyday but the other
hand what i personally do is at the end
of the day every day i at least
check in my changes of course you do
i mean if you go home maybe your laptop
break from the uh
it could happen something with you or
your laptop whatsoever the next day you
need to be to be sure you can start
where you left off the the day before
so uh what you get from that um when you
can run test automatically uh you will
be alerted as soon as you break the
build you don't have to wait too long to
know if your work is really going to
work
so also testing cost is going to be
reduced in that way because tests are
running automatically aj
yes
isn't it better to prevent that and and
know that something is
breaking something else
before it's
happened
uh yes of course i mean
you want to know it before yeah yeah
actually i don't want to break the
master
sure
so that means that the moment that you
try to
push something in it should be tested
before it is accepted
right
and that's going what i hope you are
going to demonstrate we can't
demonstrate that
so yes before it actually enters the
main branch we come to test it
and not after it enters the main branch
and then tests hey is that main branch
now okay
it should be done before
so a kind of a pre-test before you
update main branches
continuous delivery on top of that is
you what you need to have is of course
first of all integration process and the
test suite that covers enough of your
code base this is an important thing
you probably know that when you want to
send an app for appsource you need to
provide a testing automated testing code
units that cover ninety percent of your
code there is for a reason if you do not
have uh enough coverage of the code in
the automated test
you do not know for sure that
something that comes in is really okay
so uh that also means that preparing for
release is going to be easier because
the more you can test automatically the
the easier it is and to to create a
software
still the deployment is triggered
manually the process of deployment could
be automated as well i mean it's just
saying okay now you go to deployment and
that is the moment you choose instead of
doing automatically so you could release
more often
also accelerating the feedback loop with
your customers saying hey
i'm going to release every week but i i
want to be sure that it's okay so i pull
the trigger to release there might be a
reason to not release uh you mean it
could be
there is a a breaking change or
whatsoever you want to tell customers up
front
continuous deployment what you need for
that is to have a testing culture that
is at its best i mean it must be
in your whole company everybody needs to
use i would say test driven development
it's not just creating software and oh
yeah i also need to create some tests
and that is the irritating part it
should be the other way around it should
be built around
the automated test that is test driven
development i'm not we are not going to
to go into test
driven development here i'm just saying
that it is very important
and that's why we in edema also have a
test actually
so
what also is very important is that your
documentation process needs to keep up
with the process of delivery of
deployments i mean
it should not be in the way that you
deploy automatically to the customer
environment and then uh at the end of
the of the month i say you know well
thank you for
getting five futures but how do they
work
they should be able to find out so
documentation process is something you
should think about
and of course then you get faster
development but for your customers point
of view it is also a continuously
continuous stream of new features coming
in your your software builds up or
gradually i would say instead of getting
a year release
so
how did we all do this in the past i
mean uh
today we have a lot of uh
tools that can help us but i just want
to look a little bit back into the past
did we do this in the past how many of
you did
do see icd with the old seaside
environment
only a few
are you sure
in fact
if we deliver software to a customer we
have a cicd process we all have without
that we cannot even deliver so we all
have a delivery process so if you really
understand what cicd is i mean are you
all developing without ever releasing it
to a customer are you doing it for a
hobby
i hope that you are just building
software to deliver to somebody right
and if you have co-workers then you have
to integrate it in a certain database
maybe you're working on your own you
don't have any co-workers uh that could
be but the most of you probably work in
a team and most of you i hope do have
customers so in one way or the other you
must have an integration process you
must have a delivery process right
so again who is not having a ci cd
no hands great
everyone does
so how did we do that in the past
remember this one
who does remember this one
of course we do
and you see that here over here the
merge
and by the way for the overflow room
this is a pointer that you can see right
um so
the merge i mean
we have used that sometimes to overcome
certain problems with importing fobs
because the text merge did not work
because we had to import something that
is outside our license development
development license
this is part of the process
and i'm sure a lot of people here that
are using this and have me using this
and probably are using this every week
i guess you also recognize this one
merging stuff
and there are other tools as well i know
that because i took just took this one
uh but
i'm sure you you will recognize this who
does not recognize this this tool
great no hands that's what i thought
full room of dinosaurs right second full
room of dinosaurs
now
you know
this is a manually process this is why
cicd is irritating
and distracting from your daily work
because you do you want to have this
automatically right
so
we know this and then after a while
microsoft came up with some tools you
know
merging object next level
i took this picture from a blog
that was created one year and a half ago
i mean it's and i i'm quite sure a lot
of you are also using this one
merging object with powershell
if you trust powershell if you know how
it works if you really
take that that that hurdle to to to work
with it
so
again
manually steps
irritating you making those steps
distract you from your daily work
developing
so the question here is while you are
here i hope you are not too busy
to learn something new
to see how it can work with today's
tools
you should not walk away from that and
say i'm too busy because
just pause for a moment
change the wheels
and go faster from there
that's the id
and with that
it's not to me i think up to you
yeah
let's try that one
i will now take on the role as a
solution architect and the plan is to
create a new solution and i'm gonna do
that from a template that i already did
and
prepare it for
later development by my developers
and
[Music]
here we go
we are here so
what i'm using for this is the devops
in azure
and here we have a
a project called nvtec days 2018.
on my github i have the
template repository which means that it
is available
for everyone and what i need to do is i
need to copy the clone path to that
repository before i go
and create a new repository in my
organization
so let's create enemy tactics 2018
and i have a repository
the first thing i want to do is to
populate that repository from the
template and i can paste in
the template
git url
and import the code
so after this process i will have
exactly the same
files
in my
private repository as i do in the public
one
clear yep
are there are there other ways how to do
that
you can create uh empty repository
initialize it with one file and then
just start from scratch
clone your template locally at my new
remote and push it to another remote a
lot of ways these kind of things
you almost lost me there
so this serves as the starting point for
us right it's a great starting point i
have an app and a test app
without we and and some other files in
there i'm going to clone this
repository
into vs code
and in vs code
i'm going to do ctrl shift p
use git clone
and paste in the url
maybe you want to enlarge this one
and i want to put this one
in a folder somewhere
all right
now it's cloning the repository down to
my local machine
and
it's opened
zoom within
control plus
ctrl plus
i already zoomed it in to think we need
to zoom it a little more
there we go there we are
now
again
i when i create things out of
the template
i need to make sure that i have my own
ids and my own
app names
in
my solution i cannot reuse the ids and
the names from the template
and also when i start
to create the solution i want to
start a docker container
for my development
and this probably will take
a few minutes
what was
doing the first command you used
so what i'm using here is the advania
git
vs code extension and it has a lot of
functions that we can use to help us
with these
things and if i look at the fork here we
can see that
it actually made some changes to my
files
it changed the project name to my
repository name and it changed the
id
and it also changed the application
files so now we can see that instead of
using the hello world we have our
repository as the default name of course
we can edit that one and we can also add
some
test up and
best app in the world
or in
vice
i was thinking of most useless hello
and of course we can also look at the
the app json for the test app that will
have the same
things in there
test the best app
and
couldn't we do something different than
just a hello world demo to go for a
change
i mean
who to invent hello world i don't know
you'll change that later right all right
okay that's gonna be my task okay it's
gonna be i just got a task assigned
so
i also want to show
this thing here in the test app
we have something called the dependency
and the test app has a dependency
on the main app
so in here we have the id name
publisher and the version
of the main app
and this is quite important
now we only have to wait for the
computer to get ready right yeah it's
just importing license this must be just
second now
yeah yeah that always takes seconds
i mean the last one yeah
one thing i can do a little more clean
up here because the template comes with
the actually files
and i
need to remove them i will create my own
template files with
with my own excel files with my own app
names so i need to clean that up
and
i can actually look at the code here
and this is
the default hello world example
and
the test
code is just testing that the hello
world example
is displayed
so
you
i have now to take the task to
change that message right yeah did you
create a work item for that in devops
for me
otherwise i'm not gonna take that task
no well no i didn't you didn't
yeah but i i think it was created from
our herb desk system oh okay it was
already there can you show it to me
while we're waiting for the container oh
it's all ready oh it's already there all
right okay i just wanted to try to
border people a little bit more yeah
all right okay come on all right so
if you paid attention you see that this
is the actual name
for my container
and if we look at the template
you are using container on your computer
yeah yes
you are not afraid of them
no
just get to know them they are your
friends there are some people which are
afraid yeah
but i need to make sure that my json is
pointing to my container so i i do that
as well
and
then since we have more than one app
in this folder i also need
to set up what they call a workspace a
what
a workspace a workspace which means that
i can
from vs code i can work on multiple
apps at the same time
i know that yes
that's a good thing to do so
what do we have now we have
test up and the main app here in the
root
and we have the application
pointing to
our new
new app we have the launch station
pointing to
the docker container that i did so which
means that i should now
be able to download symbols
from the container you just created from
that container what
and what you know it actually worked
so let's try and build the sucker
sorry
all right now we are pushing this in our
solution architect guys
yeah we have to deal with that i have to
make sure that it's working before i
send it over to my developers right
of course
so now let's take a couple of seconds
just to
get everything warmed up and
and if we're lucky
or if we know what we're doing
it will actually work
if we are lucky okay we are sell it yeah
so now i know that my app is working and
i have the new translation file
i have everything i need i cannot send
the app
to my developer but i also want to make
sure that my test app is working
properly the one here i can download
symbol from there as well
and and
now i see that's uh that's a why we have
the two apps in one repository that we
can
switch and work together on both
if we have a
test driven development then i don't
need to switch to another workspace or
for another vs code and i'm just working
in one environment on both and i can
create new feature and test for it and
test for new feature and so on
it should be pretty easy right
so but you you saw that when i
downloaded simples from a test app i
actually got
the app that i published just a moment
ago
that's because it's in the dependencies
so it will download it from
the docker container and it will also
download the test
symbols
and that is because we have
the test app configured to use the test
simple
does it mean that i have the test suit
objects in the container
well i don't know
we can find out
let's try and build the packets
this is now the test app
sorry where are we we need to be on the
correct place to have it built it will
build control f5 to
send it to the
to the application
and the test app will open the test
tools
page automatically i will be able to get
my test
it is in here
and then i should be able to execute my
test
and we are
failing yeah
you wrote wrong tests i wrote wrong test
so what the failing is saying me is that
the code unit that i'm using
the if we just look in here we can see
that we are using this a third
coordinate which is a part of the test
libraries
it doesn't exist in my container so
that
i thought that test the automata test is
about
automation right
so
everything runs
automatic
but this involves a lot of manual steps
well
let me try and get this up fixed first
what i need to do as you show i was able
to build the app that's because i have
the test symbols but the symbols are not
the same as the objects
so i need to add the
objects
to my container
and i can do that also with
uh
because the libraries the test libraries
they are included in the docker
container so i can import the current
version from there so that should be
quite easy to do
it means now you are importing the tests
objects into the container to be able to
run the test at all i cannot send okay
yes that doesn't work to get that's just
it's just
not something you do
so let's try and run it again
run all the tests
and everyone is happy
but there's one thing more that we need
to know if we
if we go back to my app
and we try and build it again
everyone is happy if we go and try
control f5
to send it to the server
we will get an error
oh
why
because now we have the test objects
both in the
test symbols and also in the application
symbols because we just imported the
tests
as an application
so we need to tell
our test app
to ignore the test
symbols and we can do that
here in the application
so the adjacent has the platform
application and the tests these are the
apps that are being downloaded so if i
remove
this one from the json and save use ctrl
f5 again it should now ignore the test
symbols
and well the same thing don't know i
can't build it
which means i need to download symbols
again
because now i have the libraries
inside the application symbols
it's a little complex but you need to
play with this
right questions if it will be
changed in the future
maybe that it will work another way yeah
hopefully better it's this is a little
bit too i think it will it will change
after a whole application will be
extension
probably
but now i'm able to build i'm able to
run and everything is fine
so
what did i do here
i changed my setup to have the new
project name
and the id i changed the project name up
here
i
changed this launch to use my container
i
made new exclusive files
this is as it should be
everything is good to go
and i can
do my commit
states
changes
and let's push it to the new repository
and just as a reference to the
tools and the template that i was using
this is the
short link to it
all right and i'm done
okay off to a vacation
no no no no
do you trust us when we do any change
well
we can actually just to verify that we
have everything that we have that we uh
want if we go into the repo
i didn't switch
i can i can see that i have
updated the files in repo
everything looks good
so you were just acting like a real
manager you say okay
this is the work you need to do here's
the stuff you had start with i go off
vacation whatever and we are going to do
the work you do the work someone will do
this all right the work item and there's
always to be someone
so kami what are you going to do
i mean
what is your
part
now we are getting to the point that we
need
ci cd to do something yeah i mean i saw
a lot of manual steps in here yeah
that's
why we can't automate the development
part
of course not but
maybe we can i don't know but somebody
must develop that yeah exactly
so so but the the whole testing part all
that creating the the testing is yeah we
will now
make
the magic and and run everything
manually all right yeah and we all have
to match that part yeah
we now have the code on the server
somewhere on the repository what we will
do now with that
because
i want to run some tests and make sure
that gunner have
done good job and everything is really
working as expected
we need to create something which is
named build pipeline
build pipeline will take the code
do something with it
and we'll produce the app
the the result of of this compilation
and everything so so so why didn't i
just have the app in the repository yeah
would you he just created the app here
but i don't trust him that he run all
the tests and and everything around and
that maybe he just compiling on his
computer and it's compiling there but
you don't trust him enough definitely
okay perfect
that's enough reason so you're gonna
test what he just did yep
all right that means i will prepare my
own
environment to to compile the app
take the the code and maybe run some
code analysis that
will tell me that he forgot something
could that also mean that if you are
going to let's say re-run that test yeah
i could even
push changes
and code modifications without testing
myself yeah of course because if you
will not run it manually
you're going to run it anywhere so that
also means that i as a developer say the
end of the day i have no time to test so
here are my changes and good luck with
testing it yeah you can but it will fail
and it will not get
very
so
that's nice because then i do not have
to do all those manual steps he just did
but if you are ready for god if if you
are doing the test driven development
then you need to run the tests to do
that yeah that's okay good good
you are just developing without
because there might be stuff from others
as well that i did not have in my local
development right uh for example yeah
okay yeah okay good right it means
now the pipeline will take the code
prepare environment do the code analysis
uh tell me the result of that will
compile the package
will
deploy the package to
my environment
we'll run the test we'll collect the
result of the test and then take the app
and we'll save it somewhere
because
we need to work with with the products
of this
pipeline later in our process
it means that's the build pipeline
now how we can
create the pipeline i don't want to do
so many
manual things to create something like
that i don't want to do that
it's still
it's really hard to do and i rather take
the
possibility to build the pipeline as a
code imagine that you create the
pipeline
as any other code in your application
it could be part of your source code
my wishes
are i can use the source code management
for it to to version the pipeline
i do not need to leave the vs code to
change it if i want to change something
in the pipeline
i can use the prepa prep prepared
building blocks because i don't want to
write the pipeline again and again for
each app
i'm developing
and when i have some back there because
we have bugs in our products here you
have every
you know that every every app could be
it could be could be reduced to one line
which is wrong yeah that's because if
you if you are going to to check in your
your book free code
you have to test it against the bookie
code from others right definitely yes
okay
just to get a picture
yeah that's someone else
let me introduce that there we go
and it means when i
fix that i want all the the pipelines
will be updated and
will be back free yeah
okay
or potentially you can screw all the
pipelines if you enter another back
there
now we will look at that
how we will do
the pipeline as a code it's time to
learn something new and it's yaml
yeah
i don't know how you are pronouncing
that for me it's yaml
i mean yemel yammer uh
okay yep whatever don't be afraid it's
not the same thing right
no no okay good show
don't be afraid it will be very very
quick we will not go deeper
into that yeah it sounds like
that sounds like a doctor saying here to
a patient don't be afraid you won't hurt
markup language that's the definition
from wikipedia yeah it means it is not a
markup like xml or json or something
like that or html
html and it's human readable data
serialization language
human readable because
why we care that it's easy to understand
for computer like xml
why we care that computer have problems
with under understanding to something
that's that's
i don't care about that i care that i
can read the data
because i'm human and i i want to read
it easily yeah let's computer to to do
something more more
complex with that to read it but i need
to read the data what you are going to
say is
you are going to make the computer
understand you instead of you understand
the computer yeah
exactly that no okay then i got it
that's
i don't know why in history something
someone introduced that the problem that
we are trying to to put the data for
computers to be easy that's that's
it means the indentation is important in
this language
because we are
used to it
because if you are reading the book
you are reading the book then
you have indentation in the book and you
are
able to understand that
meaning
yaml looks like that
it's the simplest
example
we have some receipt with name
with date with customer which have two
attributes
we have i items which is list of items
each item have attributes and we have
some text
with a description of special delivery
it means
if you look at that you can read it
and i hope that you understand what is
there
i can imagine that it's more complex for
computer to to understand this text
because there is no beginning on the end
of each part
or it is but it's not not so easy to
find it it's just like jason just
without all the yeah yeah why to put
their curly brackets everywhere yeah
that's why we don't no i don't need them
looking at this now i have the
connection between the wife
and cicd yeah i mean
you know i know
no no no
now i can see that high heeled slippers
who the heck needs that
okay yeah that's that's a hammer and we
will use it in the example how to create
the pipeline uh as a code
imagine that you create a build pipeline
as any other code that's my wish and
there is the solution for is it is that
i will create file azure slash
pipelines yaml in my repository
uh we can use scm because it will be
in a root folder of our repository
we don't know we don't need to leave the
vs code
because we will write it in vs code
and we can use pre-prepared building
blocks because we can use templates for
for the task so are you telling me i
should have had this file in my template
yes definitely yes oh why i will add it
you're telling me i have no problem with
that
sir you're telling me that now yeah
if you have the template the file
already there what i will present here
is yeah
and of course when we fix something in
the template it will be applied to all
the templates using
all the pipelines using this template
it looks like that
i have
two repositories here
one
app repository with my code and one
repository with the template
for each step i will be using in the
pipeline
yeah
sorry that was back button
the connection is in the ml file
in the ml file i have unbeginning
some resources defined and i'm telling
which repository is the template
repository for me
and which version i want to use i am
using the master branch here
of course there could be some specific
commits in the repository or or label
it will help me to
not
break anything if somebody put a new
version to the templates it will still
use the same commit same version of the
templates if i want
in this case if somebody update the
templates it will automatically take the
latest version
uh and
for each step we are defining which file
from the templates we are using for for
this task with some parameters which are
defined inside the template file yeah
and in the template file we are using
powershell to do something
or we can use something else not
powershell we can use anything which
azure devops is supporting
that's the pipeline as a code
in azure devops and now we will go as uh
to demonstrate that
i will switch first
we are back in the
devops
now i'm i
i'm not yet in the devops i need first
uh clone your repository you prepared
yeah because i don't have it on my
computer
yet it means going back um okay
clone
that repository somewhere on my disk
and after it will cloned i will open it
and i will add only two files into the
repository yeah two files because
in my pipeline i am using
my own tools which need some settings
and i will
put
these two files
into the repository
that's not norton commander
that's that was not norton commander
that's far yeah
still working still
1960 a 96
year still working and supported
what we
i edit the yaml file here
that's the resources some parameters
here
and the
steps for for the pipeline and added one
powershell scripts which is setting some
attributes or some variables which are
used by my tools to compile everything
the basic thing is a name of the
container which will be used image name
where is the license file
and folders were are the test app and
main app nothing more yeah
now i will
commit these changes
all the changes are committed i will
push them to the server now
and
we are ready to create the pipeline on
azure devops
i will
wait yeah that's now it is there if i
refresh
[Music]
the files we can see that the files are
on the server and i will go to the
pipelines
build pipelines and click just new build
pipeline
after
it will open
i have chose from which
for which
repository i want to create the pipeline
i will use the azure pipeline
our repository
and now you see that it automatically
detected the yml file in the repository
and is telling me should i create the
pipeline based on the cml file
and i i just
say okay yeah use it
i have no possibility to just
say save i need to run it
yeah
it means it will be created and
automatically
triggered
but because i need to set something
additional because i'm using
a predefined password in my case because
i'm using windows authentication
in the pipeline
i need to cancel it
but it's already created
i can go to edit it
and i will just extend this pipeline
with some variables you can see that
there are no steps
in the
designer
because it's fully based on the yaml
file in my repository
how about the agent there
yeah i will return back to that
you know what is that in the while i
will just
add my variable group
in which i have only one uh variable
with some password which is used on the
agent yeah nothing more
in the camera you can see that there is
a agent pool it means which agent will
take the
the pipeline to do the work on it
i don't care what is here
i have this defined in the yaml file
itself
yeah that will overwhelm what is an
agent is just simple application running
somewhere on some server which is
connected to my azure devops under uh
waiting for the job uh to be prepared to
be done and if there is something it
takes that and process
the tasks somewhere means in in czech
republic right right now yes
it means i will save and queue
and the build will be triggered in a
while
if i want to change something in the in
the pipeline i will just go to the yaml
file in my repository change it commit
push and the new version of the pipeline
will be triggered
now we have
around six minutes till the build will
finish
because it will fire the docker
container import test objects
compile the application inside the
container install it or publish it
install it run the tests and everything
around yep so we just got the
call from the support desk right
yeah they're waiting for that uh change
i guess yeah
yeah it means
if we will go back
that one yep
that was the demo how to quickly create
the the pipeline
the templates and some app template i'm
using
where the the
yaml template is saved
is on a github you can use it
and i have even the
vs code extension vertical which is able
to clone the template repository update
the updates and everything what the
gunners tools are doing
in few steps there is a in one step
and you have the template ready to to
just just publish it somewhere and run
around
the development
including the yaml file
if there is a bug just send me the issue
so
i mean
that just
this is kind of overwhelming right
i mean
a lot happened
um there is
what guna showed it is possible to
uh
have an automated test that tests your
um your changes
camille showed how we can
not do that only locally but also with a
pipeline a build pipeline from azure
devops
so now i am that developer who is going
to do that change that is requested to
change that hello world message
to something that's more meaningful
and
do i then at that moment need to
understand and
work with all this you just did you just
demonstrated i think no good
so
how does that work how can i
be sure that what those guys created
really is executed the moment that i do
a
change and
the word here is
pull request
what i'm going to do
um is that when i do a change i'm not
going to do that on the master branch
i'm not going to do it on the brands
that could not just create it
i'm going to branch out for it and
create a different branch that is going
to
hold my code that i change
and then when i'm ready
i'm going to ask to do a pull request
and a pull request
that is something you should think about
from the shoes of the target branch
sorry
i created a repository not a branch you
created the repository with a master
with a main branch in it right
i saw that so there's always a branch
there's always one bronzer that you
don't have most of the master branches
repository and you don't know that you
have branch there
there is some masterplans in there yeah
that's what you're telling you hadn't
just seen somewhere
well actually it wasn't your template
i'd say
anyway what i'm going to do is i'm going
to do it in a different branch and then
i ask the master branch to grab my
changes
my changes that i'm doing should be
linked to a work item so
you can plan something
there is not mandatory to do but it is
recommended highly recommended i think
it should be a policy
so the moment that i do that pull
request
something happens
there is a
request coming in that somebody can
review somebody can say hey what is this
guy going to ask what is this guy going
to push into that master branch
he could comment on it a reviewer could
look at those changes and say i want to
make some comments this is crap or uh
please uh this is it is not working not
according the rules or whatsoever
then
when everything is okay when they are
okay with the changes they can what they
call vote for it approve
saying okay now i approve this pull
request i approve this is going to be in
our master branch
or you'll prove it with suggestions or
maybe it's just not um
okay and you can say hey please fix the
comments first then you say i'm waiting
for the author to make those changes to
update the pull request and then i kind
of check it again or you just say
reject it i'm not going to do it
the thing here is
i need to be forced to do that i need to
be forced to create a pull request
that means that i need to lock
down the master runs
i need to make sure that a pull request
is required and
what this is the flow how it is how this
is working
so i have a master branch from that i'm
going to create uh the brands the future
grounds for well what i'm going to do
then i'm going to create a pull request
they can look at it i'm going to
demonstrate that that i ask gonna to
look at my changes and they say that is
okay
it flows back into the branch and the
master grounds and then the actual merge
is going to happen
what i need to have is a bronze policy
on the master branch i need to set a
policy that requires a pull request to
merge changes into the masterminds that
blocks me from doing changes directly to
the master branch
that enforces me to use a future branch
to develop my code in and use that pull
request
and the branch that i create can be
linked to a work item so that pull
request is automatically linked to a
work item so actually when work comes in
code comes in somebody can look hey what
is actually the work item that you were
doing this was what was your task what
really what was your task it was
assigned to you
how do we do that on the master branch
and i'm going to set it up but here
you'll see the changes so when i do that
demo i can quickly scroll through it
i'm going to require a certain number of
reviewers
all reviewers need to approve code
chains
that you
want to
to to push to that master branch
an important
note here is this number of course
how many reviewers need to
to have to to approve that code
and
the nice thing is that you can vote for
your own code changes
you can do that but you need to be
allowed to approve it with this
checkbox otherwise you can improve
but your vote will not count towards
that minimum number of reviewers so
otherwise it will just not work so
if i want to vote for my own code
changes i have to set that allow users
to approve their own change aj yes do
you
ever
reject your own changes
no of course not but dude do you ever
reject your own chances
uh
if i did it yesterday and maybe i look
at them now
yeah okay yeah
uh then even i don't do it so
after that
you have also the possibility to
allow completion of the pull request
completion of the pull request means
that the code is actually going to be
merged into the master branch so the
master brands get a new commit with the
merged code
and
what you can said is hey if one of the
two
already
votes for it we've approved and it's
okay and we can complete it
um
so these are settings that we can do
and when i do a change i could also say
hey
you should look at it again if i did a
change to the to the code so i can check
in code and do that over and over again
the pull request will be automatically
updated with my changes but if i change
something reviewers
should
look at it again so that's the last
option
i could
enforce to have a linked work item
so
that automatically the work item also
gets
ready and you know work items that are
linked to sprints etc so this is not
only about
the code itself it's also about the
whole development process
then you have the option to uh the
comments
and someone can set comments to your
code say hey uh are you sure you want to
do this maybe this is a better way
whatever i want you to fix this this is
not going to work whatsoever
you can comment comment on code
criteria just made some notes and the
notes need to be resolved by you as a
developer before the
reviewer can say okay now i approve it
the other part is
how do we merge if it is being approved
i have a pull request from a branch i
may have created multiple commits in
that branch maybe i was working on the
future for a couple of days and i
created a couple of commits at the end
of the day with work in progress
then
you probably don't want to have all
those intermediate commits in your
master branch another
choice you can make here if you say
no fast forward merge then you get a
complete
history of all the comments from the
future rounds in your target runs in
your master runs and if you say squash
merch he's going to make one comment in
your master brand so you don't see all
those individual commits in the master
brands they stay in the future branch
and the recommendation from devops is
that you delete the future brands after
that because it's supposed that you are
ready to combine all the commits as one
big commit going into the master branch
and another part is the build validation
and this is the nice thing
you should not think that after you
merge the code into the master grounds
that then he is going to do the build
he's doing that before that
so the moment that you have a pull
request
you can add a build validation to it
and everything should be passed
successfully the reviewers that do a
code inspection should approve it
the
other requirements like a linked work
item and probably notes should be
resolved and the built pipeline should
be successfully completed including the
tests and when that is done and
everything is green
then the pull request can be finished
can be completed
so somebody has to look at a pull
request to see if everything is ready
well not really you can say
autocomplete the moment that everything
is completed
the review says the code is fine and if
the test also succeeds and everything is
complying to the rules then
automatically the pull request completes
and then the code is automatically
merged into it so that could even happen
overnight
so i want to
demo
i'm not very happy here aj you're not
happy no why not because he told me what
i missed and now you're telling me what
i missed
i should have done this
as a solution architect right
now just a developer right
yeah right all right show me how to do
it
you are missing the point
so
um
let me see what we have here
um i have a
work item change the hello world message
what is assigned to me
this is the work that i need to do just
so apparently that helpdesk created the
work item for me right
so what i now
need to do is i need to create a branch
for it
um but before i do that i'm first going
to set up the branch policy
so that was something it was not done
before right so i'm going to do your
work
so let's first go into the
branches so you see that master branch
yeah this is the one you created and you
will see that camille has updated it 70
minutes ago
so i'm going to
click on branch policies
and do a number of settings
first of all i'm going to
require a minimum number of reviewers
let's just set that to 1.
i require to
check for linked work items
i want all comments to be resolved
and i'm going to squash my changes
then
i'm going to add the build policy
the one that
camille just created
yep
save it
save changes
and there we go
there's one more thing
the moment that we create
the pull request we have to type in
comments like okay this is what i asked
this is my pull request with my changes
what i want to do is to have a
template for that
some text for the comments that i'm
going to create so that is
a pretty easy
thing i can do here i'm going to do it
right now from devops i don't even need
to go in vs code to create folders and
files i can do it right from here
so
look at this i'm going to create a
folder called
azure
devops
and i'm going to create a file name
pull request template
create that one
and then inside that one i'm going to
put
this
piece of code come on
can you please
copy
and paste for me you're on the
on the wrong machine yeah
without no clipboard
connection come on
i should
you know this always happens why is it
not doing any change i mean
i should be able to put okay
thank you for your contribution i'm
going to type it in quickly thank you
thank you for your contribution
the text in the notepad it's some just a
plain text or it's it is
marked down as they call it
you know
it doesn't work i mean
how could that happen
yeah you are working on a remote and
you when you are connecting to the
remote you you didn't enable the
clipboard integration yeah so i'm just
going to do this and you know your code
builds clean i'm just going to
to type in one thing
not to bore you with the rest your code
builds clean
and you will see that this one is coming
up
the moment i create a pull request so
the other lines you just need to
accept that i say it works trust me
so yeah oh i just created again
i guess that was coming yeah you knew
that right i knew that was coming ah
so let me go back down one more time and
say
i discard all my changes create for one
time
that uh remove that policy and create
this immediately or directly from so
developers shouldn't be able to do this
right right it should be i'm doing your
work right yeah
i mean
uh
let
this delete this one here
delete this
save changes do it again
so i would get this message if i was
changing things on master in vs code as
well
i guess yeah so i would be stopped there
telling me i could not write to master
when you will try to push the changes to
the server it will reject the changes
yeah and there's a way to solve that or
do you need to throw everything out and
create the branch and and push it
[Music]
instead the master branch
you can do that so there's a way to do
that let me just create the branch
because branch is nothing more than the
reference to your commit and push this
this branch
copy line by line does that work
i tried there
let's see
how that one works line by line
not even that
yeah i tried to do that
so
we have helpful audience yeah we have
that's that's great just
you know it's not working i just just
type whatever just type it yeah yeah you
will see that it works um
your code builds clean whatever
commit there we go there we go and then
go back to the branches and say
do that policy again
hey you have just triggered the build
i did trigger the build of course you
committed something to master branch
that's cool so now you're making sure he
did the correct yep
you're going to build that oh all right
i will cancel that because we don't need
that right right i understand
safe changes so here we are again
now i'm
having a repo with
everything in here so i'm going back to
my work item
and
i want to
well there's no pull request here or
whatsoever i want to create a new branch
that's what i'm going to do
create new branch
a little secret in here that i'm going
to show you is that if i create a branch
with slashes in the name he's going to
show me
subfolders automatically so
i do this say this is going to be the
branch for change
hello world
message
which is based on this repository and
then the master branch
i create a branch
and
save this here
let me see if the bronze got created now
yes so from here you can now see the
master branch and my branch city i
created now
just for the demo let me create one new
branch and let me create an a branch for
gunner who also probably needs to do
some changes yeah
this create rounds
now look at this
i mean
i can now see that i actually have two
developers doing some work i could even
combine this if i have multiple branches
so uh as a little secret little feature
in devops so what i'm going to do is um
delete his branch
i mean whatever i'm not going to do it
anyway
i guess
so my task is to
change that message
so let me
go into files and
get the clone link cloned in vs code yes
allow vs code to open
come on
give me a pop-up
sometimes they work sometimes this does
not work so
let me just copy it
and say git clone enter
that's the problem of the clipboard
okay
you guys
that's
funny ctrl c i did control c
git clone
ah there we go
put it
onto documents al folders
he will create a new folder for your
repository here just that you know it
cloning the repository that he created
and i changed and he changed it
let me open it
and there we are yeah now i can see that
you're in master
the bottom left corner here
yeah i'm yeah i'm not a wise master yeah
yeah right
so um
gonna yep
i thought you were creating a code
workspace file oh but you did not push
that one i did not push that one ah okay
i created that with the magic you know
conflict p magic yeah right so that
means that i need to create it myself
because now at this moment i just
cloned the project the whole repository
with two projects in it
the main app and this and the test app
but i don't need that other stuff in
there even i cannot run this in this way
because
he's now thinking that this is a one big
app it's now if i now try to to download
the the symbol files he's going to
create another file here
for al packages well it actually should
be here
so let me create a code workspace thing
that he did with a kind of a magic thing
let me do that manually so you see
actually how that works but please don't
do that in master branch no no i'm and
yeah okay i will
go
okay um
yeah let me first switch the brands then
let me first do that so switching the
brands is done over here i click here
and say i'm going to do that in change
hello world message so now the whole
repository is changed the branch i'm
going to close
this one
and
i now say file open folder
i start with that
main app
select it
this is my main app that i have now open
and the i can now run as a single app
and well apparently symbols are missing
but before i download symbols i first
going to add a test app to it so i say
add folder to workspace
and i select my test tab
and at this moment i have two
apps open in one workspace and that
workspace at this moment is untitled let
me
save that workspace
as
the
nav
tech days 2018
code workspace file
and now
i do have a code workspace file let me
close it
vs code for a moment look into here this
one is having a code workspace file and
this code works for a code workspace
file is just ah that's just because vs
code was
installed without
the
um
changing the
stuff from
a
right click on folders etc so
anyway
if you open a code workspace file that
one is actually let me show you that
user not the user settings the workspace
settings show me that
settings.json he's saying hey combine me
those two folders into one workspace and
every folder is an al product on itself
i could even combine this with other
folders non-al folders and i could then
go
up and say do some settings in this one
etc etc i'm not going to deep into this
what i'm going to do is to make my
change and make sure that i create a
pull request so um
yeah you know what's my docker
i i don't have your docker no
i know that so you can't do it i can do
that
actually i can i go to my launch
suggestion i say add a configuration
publish to my own server
and i call this one
this is ajk
local development
and
you know
this is my local server
come on
i have a problem with selecting and copy
stuff today
so
this is my
machine
and now i say download symbols
and you know what
couldn't download them
they can download them of course he's
now saying hey from where do you want to
download it i have two configurations in
the launch.json and i say please take it
from
the local machine my local development
so do this i can do this
absolutely let me change that message
to another one
let me ask the audience something
do you want to
get
page
inspector
before spring
29 release
[Applause]
you even don't need to compile it and
run it
okay let's just speed up i'm
i'm i'm sure this thing will work i'm
sure i can just run this
let's just not run i'm gonna at the end
of the day i'm ready we have 10 minutes
left so let's just
go right away and say i'm going to
commit my changes well well hold on hold
on hold on hold on test will fail
oh of course the test will occur it will
completely fail and everything will be i
know i thought
that the test will fail i
who cares no no
they agree with the message right yeah
yeah okay so let me
change the test as well because
i mean there is something in here and
you know what i'm not going to run the
test locally if this really works i
trust on the build pipeline that commu
created
that this will work i don't even have
the test stuff on my local machine right
now
so
i just
go in here
state the changes and say
changed
hello
world message
commit
and push
ask me later please
and then go here
to see that
on the files
in my branch
i've now really that
change
there we go
so what i now want to do is to create a
pull request
and i can do that from
several places
i do it just right here create a pull
request i could also do from the work
item i could do it from
the branches
page whatever
i could do it over here for example
there are several places where you can
create a pull request
so
well here you see that template coming
in that i could not copy completely
so i say my code builds clean
and this is actually what the reviewer
is going to see my code builds clean i
mark that as complete i'm going to add
gunner he has something to do
as the reviewer
and i say create pull request now at
this moment gunner has
a pull request that he needs to review
you see that over here one zero of one
review was approved the work item was
linked the comments are resolved and the
build progress that i that he created
and i linked that in the bronze policy
is now also in progress
so
i think that we can now switch to gunas
machine so he can review the code
all right
are we here you are here
so
back in devops
i
from a repo i can see
the pull requests
this is the pull request that the
changed
and it's as simple as a task for me just
to click approve i can of course and i
should
check the file changes that he did
but i actually i actually agree with him
in this case so
as hard as this
i'm going to approve it
yeah and that's it that's all
we need to
wait for for the pipeline what about an
auto complete over there yeah yeah i can
do that so in all those how are you
going to wait for the bill to be
completed
no
so you can go off it's it's done let's
let's do this work
it's really to work out them
i have an out complete
you want to complete the work item that
means it will be marked as completed
if all is okay and even we can
automatically delete the chat the branch
actually yes that's nice as long as as
long as we get a page inspector i'm fine
all right let's do it
that's all that's all yep
now
because the build will take
another five minutes to finish
we can
continue with the presentation
and
that was what i was creating in my
previous presentation
uh the build pipeline and now we have
something which is connected uh to this
build pipeline it's the release pipeline
because that's the part of the cd
the the delivery part
the release pipeline is something
similar like build pipeline but we have
only the app as an input
and we want to do something with the app
mostly we want to
try it on on multiple environments
for example the current version of
business central the master branch of
the business central it means what will
be released on
spring
or we can
for example put it to our qa server for
our consultants to test it manually
in all the environments we are running
again the automatic tests which are part
of the the repository
at the end for example we can run some
integration tests and of course we
should uh even test that
the
upgrade code units are working it means
we should test to install the app into
environment when where we have already
the old version to test that every all
the data will be updated or upgrade it
correctly
and the result is app which is tested
and
it is ready to deploy to
live systems of our customers
can it be done today automatically
yes it could be done automatically from
the release pipeline if we want
okay but also for business central
online
no
in this case we need to send the app to
the appsource team they will need to
check it and they will release that it
means we are delivering the app to this
team and they will make the deployment
part the moment that they have an api we
can push
the app file too
we could have this complete deployment
end-to-end
right
that would be nice i hope microsoft is
listening
of course you can deliver the app to the
file system or the azure devops
artifacts server or another
package server
there is no support for yaml
defined release pipelines yet
but it is planned for
q4 of this year there is a link to the
things which are prepared
this item is still in in the status of
not planned it means i don't know when
we will get this part but it is
in the backlog of the team and i hope
that it will be uh as soon as possible
because in this case we will be able to
define the
the release pipeline as
the build pipeline
and i will now show
uh how the release pipeline looks like
because we don't have too much time i
already
prepared the pipeline here even you you
see that
it was automatically triggered and we
have already
some releases here i will just reload
the page because
it's not actual right now
the internet is very slow right now okay
going back to the releases
yeah something is going on on cloud
maybe some storm
i don't know
well
we just created too much builds as you
cannot handle
yeah still
not loading
the
release pipeline is easy just taking you
are selecting which
inputs you want to use
okay if it works here
the release pipeline looks like that i
have input the artifacts i can have
multiple artifacts it means i can
combine for example
different apps to one release and so on
it will
take it
in my case it will release it to the
current version of business central and
if if all
is okay it will take it and release to
my qa server and my consultants could
test them
manually i can
deploy it to the master
environment it means
the one which will be released next next
release cycle
and if all is okay i have one step which
will take the app
sign it with the company certificate and
release it to our
company server and i will try run only
this step manually
you can see that there was a another
release it was the release which was
created by aj and his pull request
sorry what's that
and now i just go to the sign and
release deploy
and
after this step is finished it will take
two minutes
we will
have
app on our artifact server
i have prepared some
example already
during preparation
we will have two apps on the app server
one the main app the test app and the
test app will have dependency on the on
the main app it means i can download it
anytime from this server and install and
i can take any version which was
deployed there yeah that's the release
and on delivery uh things
we now have app ready to be
put to our
live systems on the customer side or
send to them to to upsource
well thank you
thank you have i i'd like to take 30
seconds for uh just mention that
everything that we've shown in al
it is possible to do that in old cll as
well
every the ci the cd all the pipe signs
all the builds the artifacts will be fob
files backup files for backpacks
so everything is possible still
for the dinosaurs exactly in the room
right or maybe maybe on uh for for this
kind of apps you need even to change the
the baseline yeah but it's just for the
next 12 to 24 months yeah and will be il
we will be running hybrid environments
for the next
pipelines into one yeah but we need to
worry we need to be thinking about those
symbols that we showed earlier immersing
these things together eyes on iceland
ice age yeah
so
with that
we are ready with this presentation
and we are one minute and 20 seconds
over time but we also started one minute
and 20 seconds too late so it's perfect
time yeah and so
uh
you throw the shoes
you are throwing he's throwing to
the t-shirts because i'm not able to
throw anything
um
hello
yeah um you showed the release package
you had on the artifacts page it had an
install package command
does it create automatically a
powershell command for you to download
that package and the dependency to
the server or
it means
how i you can download the the app from
the package server or if there is some
some command for that
i have this command in my uh powershell
module which is available on the
internet and there is just commands
which
i will i can use to tell the url or name
of the package and it will contact the
server download the app and put it to
the folder when i
will include the dependencies and it
will include a dependency automatically
he deserves shirt over here
okay okay
uh hi hi hi um so i have this question
is setting this up uh the whole ci cd uh
really that much different in say gitlab
or github or whatever
i never used uh the the pipeline in
other servers i think the yaml pipeline
definition is from github
yeah it means i think it is same
or very similar
but we still
kind of need to have a separate build
server right
in my case i'm using on-prem
agent but if you change uh slightly the
the scripts you can even use the azure
uh
agents which are there because and you
can use the azure
docker images and so on i think freddie
have that uh in his example
and you can you can use even the hosted
agent really really should read his blog
uh with the steps thank you that will
put you through it
i
um
last wednesday i was at a customer and
they mentioned
to better organize uh the projects we do
they mentioned
yira
yeah jira
is
azure devops uh
a good alternative for uh jira or
well we are using all these atlassian
products inside that one here so we are
using jira bitbucket and bamboo and we
can achieve everything that we need from
that package
azure devops is
same like jira bamboo and these kind of
things together
even you can connect
azure devops to
a
bitbucket server and
but
not everything could work
as it is if it's all on azure devops
because for example the automatically
triggered build
could be a problematic because
azure defaults don't know
that there is something happened on on
the
bitbucket but maybe the trigger is
already there don't know
that yet but
as
to register issues bugs
we could start using devops yeah
yeah yes okay thank you
i know who was first if
okay i will
get here
thank you
hi thank you for this presentation it is
very nice that in a vision we are going
to
uh normal way to development
with
code
version and
pipelines and maybe we will go to git
flow some
and
i want to ask about code
code review in which time
and
how you arrange code review in project
i think the code review it's on you
it's a part of the
it's part of that pull request so uh
the code review is done by the reviewer
and he could really compare what are the
changes make comments on it say hey are
you sure you want to do this and as long
as there are comments you cannot
complete the pull request
so
the developer can see the comments can
say can reply they can have a
conversation about it so everybody can
read that you can say okay now it's
resolved
uh he can make changes to the code the
moment you do a new commit to the same
branch the pull request will
automatically be updated with the
updated code so
the reviewer can see hey he really
updated the code and now the comment is
resolved and only when the all comments
are resolved you can complete a pull
request and completing means now is the
moment that it's going to be merged into
the masterminds not any earlier
in this architecture we need to have one
responsible person or
several who
[Music]
for example the reviewer could be any
anyone from the team
there is only
you can enter the default reviewers
which could be grouped yeah it means it
could be any other developer and you say
okay two or three must accept
and that's that's all
and but it's on you how you will set
this rule um for example how often your
colleagues will check the pull request
and review the code and so on but
yeah okay random people okay okay thank
you
t-shirt or video so let us just take the
last question
do you want a t-shirt because it's it's
70 minutes over time already
appreciated what kind of server did you
use for the artifacts
the artifacts it's part of the uh the
azure devops
and i'm using the
nuget
[Music]
format but in azure devops there is a
new format right now it's in preview
it's something named i think a universal
package
you can put any file into that okay it
have no
no complex definition or something it's
just a pack of files you put there and
you can download there
it means i think it will be much better
for the app file
than the nougat but i'm using nuget
because it have the dependencies
yeah the the standard this this
universal package or how it's named
it have no dependencies yet
maybe there will be in the future it's
new thing
but it's much simpler
and it worked studious for files
anything you can put there anything
there is a default task in the pipeline
you can use and just set which files
should be
included in in the package and push the
package to the server as a
in your private space
it's it's your azure devops account okay
and secure from outside yeah yeah okay
yeah
it's local
of course in if you have the nuget for
example you can set
the upstream servers and if you want you
can put it to the some public servers
later
that's also does he get a t-shirt again
i don't know
of course okay it's the last one so
i would like you to uh to say thank you
and
enjoy yours today
thank you
