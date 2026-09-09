# NAV TechDays 2017: Source Code Management with Visual Studio Code Made Easy

- **Source:** https://www.youtube.com/watch?v=Uyz8qF0JVWc
- **Video ID:** Uyz8qF0JVWc
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 94m51s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

welcome to this last session of the day
and thank you for making it I know it's
the last session so it's a it's a little
tough
we wanted to
show you the journey into source code
management
and despite what some people have been
saying it's not source code control its
source code management
and I will explain why later
first little introduction of ourselves
my name is Suren crimson I'm a
development manager at 360 visibility
I'm also a certified scrum master and
Microsoft MVP and
yeah go I I met this young little bit
gentleman yes so my name is Jonas
Anderson I work as a developer at a big
envira and currently been working for
three years with Dynamics NAV
yep that's it
so how many of you are using a sauce
core management ACM today hands up clap
clap or one of the two so it's about I
don't know 30 40 I looked you don't
count
[Laughter]
so what does your source code management
look like what does your development
right might look like I I've seen a lot
of scenarios out there where people do
this kind of scenario where there's a
corporate developers they work directly
in the production database and hopefully
nothing goes wrong
quite a few of you might recognize this
one something you're more likely to
recognize is that this is a kind of
development database and you have a
production database somewhere and
some young eager developer is
moving code hopefully he finds it all
moves it over the only problem with this
solution is most of the time he looks
like this
because it's not really easy when we
don't know what's been done we only have
the finished result right you know
what's in the database now you have no
clue where it came from you don't know
when it when it came in so you have to
try and try and find it out and the
problem with him being like that that is
he moves the wrong things over and
breaks things and these developers here
they they they start getting a little
antsy with him because now their
development alignment doesn't fit
reproduction and things go go off the
rails really quickly and this is why we
need source code management
the other thing that's that's very
important that is source code management
is the foundation for a lot of things I
talked about before it's like it's not
source code control we are here to
control anybody I'll be after people or
put blame on people when you find things
when you do source code management
you're after figuring out what goes
wrong so you can fix it if you don't
know what developer did what if you
don't know
who's doing what or why they're doing it
and when they're doing it how can you
how can you help them be better you
can't educate your development team when
you don't know what exactly they're
doing it's very hard at least
so it's not about putting blame it's
about being becoming better the other
thing is source code management is about
or automated it's a foundation for to
automate everything
how can you do automated tests if you
don't have a source code management
system I don't know where you gonna do
it how do you have a database do you
have a build how how does something spit
something out you can do tests on no
it's kind of some person sits and build
something and then you run a test on it
it's not automated
the same thing with you you can't have
automated bills because we're gonna get
you built from lying in database
somewhere somebody has done it you
actually don't know if all your objects
are compiling together because you know
when you save this updated compiled and
then somebody did something else
somewhere else your take is still
compiled but that's your object compiled
now that somebody changed something is
somewhere else in the system you don't
know so
and I think to create an automated world
we need to start with the source code
management system oh
I have a few more you keep calm calm
it's only a broken code yeah tell it
tell that so what's the issues here well
we would like to know what was done we
would like to know when it was done who
did it and why was it done
we would also like to know is compiling
and
quite often we doing multiple things at
the same time so we would like to be
able to say or will like to promote this
branch or this these changes but the
other stuff that we're also working on
is we're not ready with promoting it so
you're right to be able to prou
individual changes without I knowing
what those individual changes are so we
don't sit like the man in the middle
layer and pulling his hair and putting
this putting the hand to the screen so
understanding what we do understanding
exactly what the code does gives you
insight it's it's a huge value and and I
I've had this talk with many of you
probably and hundreds of people and in
my time and and lots of people are quite
against it because I it's overhead it
takes extra time but that's the problem
you just need to get into it and then
from then on you can start automating
all kinds of things and it takes time it
takes time away from all these manual
tasks you do today and it makes you
focus on what you need to do and focus
on being a developer i I see developers
all the time they deploy tasks and they
deploy changes that customers why now
developers should do that that's IT they
they builders give crates props and a
build and send it to a consultant that
needs to go out and implement it or
something like that why why it's not
packaging the product it's not the
developers Japanese Japanese have
developed
right so
creating this mentality of core
development focus and automating
creating the world of
of the future in my view is it's what we
about
the same thing here
prove my team there was where I was
talking about before how do I ensure
quality if I don't run tests automated
tests how do I ensure quality if I can't
add things to my tests and I don't spend
time on it then a buck might come back
again and again again
you've probably experienced that many
times you fix something and then three
months later it comes back and I've seen
this before why do I'll get it again
well you get it again because you didn't
for a test in that secure that it didn't
get into the customers database again
automated test bills and so on
how do I know
well that's the same to right
to move something and I was thinking
what was meant with that but
when you make changes
that's the hardest thing that is to
figure out you know what two years later
now Microsoft came out with something
that does the same thing let me go and
find the code that I actually did to
make this happen and remove my code and
clean it up make it clean again how do I
do that how do I go in and find the
exact code changes I did to accomplish
this task and clean it up nicely after
myself it's a huge task how do I know I
don't break anything if you don't manage
your code you can't do this stuff
promote individual change this remote
into airplane so have that again I can't
even read this from there code review
and release management yeah the code
review is is is also something I believe
strongly in review code half half
so if you have a developer developing
something and the only thing you can see
is the finished product and you want a
fellow developer to review his code are
you gonna do that because he can't see
what actually that developer did he can
only see the finished result so it's
harder to educate the other developers
the code review I think that's key to
creating a team it's a it's a key to
make sure your team programs in the same
way and use the same rules of engagement
and just create consistent code that
looks and feels the same for your whole
company
so
we talked about this I think you saw my
session last year and we were we've met
a few times talked to his fellow
colleagues that are sitting here ready
to cheer him on
so we talked a few times last year about
how do we make this simple we looked at
some of the systems that were out there
and there's some the the the barrier to
get to enter into source code management
seems to be high people are
they were locked in to get into it
because it's just like how do we get
started how do you get started there's
different systems out there some of them
are hard or somewhat hard to install
they so so that that's one thing the
other thing is how do I change my
development team so I have to train all
my five developers at ten developers but
I train them make sure they follow same
processes because if they follow the
same processes you know what it's not
gonna work if they take bad things in
and it's gonna break things it's not
gonna work so you need to create a
mentality and you need to create some
set of rules and also a set of
procedures that ensure that they they
kind of automatically follow the same
process I don't rules are good but the
problem is people people break rules if
there's procedures this is how we
deliver code to a customer and
this is the only way we deliver code to
a customer well if you don't deliver
code through the guy this has to
implement the customer did that way it's
not going to get delivered so it's
procedure in place you can't cheat the
system so I'm gonna talk about that a
lot later and and I've been blamed for
talking a lot in in in the past so what
we have done is and I will try and
simplify it here we
want to we want to create a system of a
developer one database so basically what
we call developer isolation I've talked
a lot about it and the Luke has talked a
lot about I know some people
use that less
can't see him but he's here somewhere
you know two years
look this too
so develop isolation is key in my in my
world with the course I see so often
this scenario with multiple developers
working in the same database well if you
have an error how do you know it's your
error
that's all the developers do we change
this to in this database it could be
there or error that you're running into
so now you're wasting time you know you
don't have an isolated
virtual world that you're working in
that just
that it's just you right so you don't
know if the scenario worked before and
now it breaks well you don't know you
don't know what caused it and that when
you go into your own world you're sure
that nothing changes it's your changes
it's your your scenario it's it's it's
it's your code and
then we would like to make the
connection between
innovation or sorry Dynamics NAV the
next 365 or they will be called nowadays
I still like the vision but I'm old
so make the connection between the
database and the source code management
system because source code management is
just text files it is nothing else then
it's just text and
the dynamics database is binary files
basically
compiled binary files lying in blob
fields so how do you make the connection
in the new world of extension
development and v2 you're coding in
Visual Studio code we should do the code
again it's just a text editor it's it's
an advanced notepad that's all it is
it's got a few functions got a few
things you can extend it with but it's
basically just a notepad that has a
bunch of other functions but it doesn't
do anything else than that
so we wanted to focus on so the our
system here is also focused on classical
development right now we know vast
majority or if you're doing classical
development
and and that's where the problem is
because once you change to v2 extensions
you don't have that barrier right you're
working straight almost in your social
management system
so that barrier was what we wanted to
break down we wanted to break it down in
into in this very very simple way that
would take you five minutes to set up
because anything more than that is just
too much
the other thing we wanted to do there
was help the developers managed their
develop environments one of the reasons
they quite often work in one database is
because partners have this gigantic
database sitting out server sitting with
all the customer databases and you're
working in that one and and that gives a
lot of challenges because developers if
you knew if you work individually you
need to set up a database for every
project you're working on how do you
manage that and how do you clean it up
whatever whatever how do you manage that
that's part of it so we wanted to make
all that simple and straightforward
then
once we have that we wanted to
demonstrate how you could do build and
test we've not implemented tests here
but it's the same as doing the bills so
it's it's pretty easy and
create a built database and of course
spit some bills out of the system that
side over there is fully automated
it's actually on the computer standing
right here I was gonna set it up here
but we thought it was too dangerous it
might fall down so watch me I'm not
touching this computer before the end of
the presentation when I come here the
build is already done
based on what he's gonna demonstrate in
in a in a while so shut up if you see
we've touched this computer not touching
it on the bills of course the developers
can just load the bills and use them or
they can update the database with
whatever's in source code management
whatever way is the fastest for what
they're doing today
so how are we going to do this what
tools have we elected to use we have a
selection of tools here in our case
we're using visual studio team services
I mean it's Microsoft I mean we use
Microsoft in my opinion
there's other tools out there to do the
2d
and Mark was sitting here with an apple
so I don't know maybe we don't need to
use Microsoft anymore just a software
right Michael just a software
so missus to do team services I'm using
it personally at home I used the online
versions with team services is the
online cloud version of it I use it for
my scrub management task management of
all the tasks or scrum in
from the time pure task management we're
not gonna touch really on that today we
are gonna talk slightly you're gonna
with you when we do a check in later or
commit sorry I have to its commit using
get
when you do a commit we are gonna
connect the actual commit to a task in
the system so there's these tasks in
there are we using the other side of
visual studio team services which is a
source code management of it it has
several side and we are also using the
built a gent
Microsoft build agents
in the in team services so we're gonna
we have some tasks we're not going to
look at that but we're gonna look at the
source code management which we there's
two source code management systems in
Visual Studio the classical one which
I've used a lot of years and I'm more
slowly moving to get right now and the
gate is what we're using today there's a
lot of other source code management
systems out there but I think gate is
kind of the future right now it is so
powerful and will show that how how
great that is so absolutely
if you use this or you use github or you
use bitbucket or something else for your
git repository doesn't really matter it
is just it is just repository
how do you get an account well you go to
visual studio calm and you say I I would
like to to get into team services which
is the middle one you get started sign
up for an account sorry the screenshot
here is the same screenshot I'll use the
direction so I call it directions and
sorry look
this is one way this is the advanced one
you don't have to
tell right away that it's that it's a
scrum default is agile and of course
I'm living in North America so I set it
up with in central u.s. at the time but
you probably want to use Western Europe
or northern Europe or something like
that
so and then you get a soon as you have
done that
it opens up and you're in visual studio
team services on your browser and you're
ready basically that's it you're ready
with team services you yeah you need to
do some other stuff too you need to make
sure your other users have access also
there is a cost to it the first five
users
can get in and get basic access was this
the normal access and full access to
gives you access to source and so on
five users can get that for free all
your developers who has MSDN and I hope
that's all of them they have free access
anyways so so you should be fine
normally I think most of all of us
should have a misty an access I hope
so that's that's that's that then we use
an odd tool called get so gate is
its gate and it doesn't really matter
where you use it it's just you go to get
SEM doesn't matter if you're using Bay
Packer or using visual studio team
services it's just a background client
you need to install it but we don't need
to interact with it directly here
because we do it through the visual
studio mr. studio code client which has
the built interface if you saw a walrus
session this morning he showed that it's
it's building as long as you install git
you are you're good to go and
visual to the code we use record which
of course is our future clients so
that's what we wanted to go again you go
or by the way we get more loads
completely right install next next next
next next next next and next and finish
no no don't need to change any or
anything there's a lot of settings but
just use them default works fine which
is your code go to which it's a code
that mrs. teacher comm install it you're
good to go
so so how we gonna address the problem
of connecting the EDI so however if you
want to connect the EDI here that the
integrated development vironment with
SCM
how we gonna
weights that so the problem again right
it's binary files or one nav in SEM we
need text files there's things we need
to take care of
the cause of the the file format coming
out of nav when you export text files
you need to make sure all your
developers are running the same country
or regional settings so same date format
same time format same
number format same character say it and
so code page and to make sure all that
it's the same
for me it's easy we am North America we
run us saying listen that's it so and we
don't change it so it's pretty easy but
it is one of the things you do have to
keep in an eye on very much
[Music]
so this red line here comes in here
that's why the problem is because
otherwise this was easy to write as you
do
so the solution is
you want to take that one yeah sure the
solution currently we have the nav
database
which is then gonna export using this is
the icon for our visual studio code
extension
dynamic snap a SCM and then we're gonna
go to visual studio code
like this and then in turn go to gates
so just back to this slide I'm gonna
actually the user interface that you're
gonna use that I'm gonna use demo here
it's gonna be in the net database the
regular old development client and also
in wishes to the code that's the only
place where you actually interact with
it so now I'm Bob the Builder get more
time yes as a developer so I have
received an issue or a task from from
Soren
he wants me to add hello world into the
customer cart so I'm just going to go to
my VM here and to look at the actual
task here I can see it's task number
four and
we haven't really yeah
in this demo I
I'm gonna say that we haven't cloned the
code but we actually have in advance so
I'm gonna
assume that I haven't clung to code I
don't have the code locally on my
machine I'm starting from scratch so the
first thing I'm gonna do is actually
kind of clone the code
up here I
get a URL
I'm gonna go into the shoe studio code
and you all know the command palette
that Waldo showed earlier
I'm gonna clone it gets I'm gonna paste
the repository and
I'm gonna choose a path where I went to
County
so now get is fetching up from visual
studio team services the entire
repository including all the history and
all the stuff
and after a little while I'm gonna have
it on my local machine ready to work on
I don't want to open this because I've
already had the demo
so the extension that we made of course
has some settings so if I go into
workspace settings
we're gonna I have to find that the road
select line path
dissipater bigger I have the Dynamics
NAV rozilla client path which just
points to where the rotate land is
installed and then I have a database
name and I also have some filters and
the filters I'm going to go back to in
just a minute so basically this is just
a setup file and it defines very few
settings that you need to know in order
to do development for this repository
yes so the first thing I would do is
create a new
development environment
I'm actually not going to do this as
well because I have everything set up
for the demo but I would create a new
development environment I could said I
could specify a sip file here and it's
gonna on
extract the zip file and it's gonna
install everything for me and and then
I'm gonna point it everything to the
database that I specified I'll also in
the settings file
and in the new version we're working on
this is all talker which is what we're
doing showing today yeah so going
forward there would be two settings you
can either select to say I have a DVD
file lying over here DVD zipped file
lying over here and I'm gonna install it
locally on my machine takes a lot longer
but it's needed for if you have older
versions like 13 13 a 2 and 15 because
darka is from 16 and forward the java
images are only available for 16 forward
unless you want to make them yourself
so yeah because I'm working on a new
feature I'm gonna create a new branch
this is one of its features I'm gonna
create a customer
action
and yeah I'm really under customer card
action
I'm now gonna start up the development
environment like regular this is this
one that we've coated into this so it
calculates or that's hard-coded into it
where all this where she's better what
did you specify just from the settings
and if I press ENTER I get a development
environment
so basically
that we can set up a development island
and right from it just create new
development island and you have a
complete development run ready and you
can enter into it straight from Visual
Studio you don't need to do anything
it's it manages the your whole computer
pond this on this level yes so let's go
and design a customer cards let's go
into page actions
go up here
let's just copy the application area
because I'm gonna need that
and that's great
create some code on it so while you're
honest is creating so basically
you're standing a BBS code you install
and setup your development environment
for missions through the code who
manages your computer you start the
development run out but environment and
you start developing
and let's place the application area
just so that it consists so we can
actually see the action so just saved it
like regular I'm kind of minimize
everything because I have a client
desktop
in that area
again
let's go into customers and let's see
it's always nice when developers test
and on the navigators you can see the
tests button when I click it it shows a
little world so I'm happy with my test
I'm ready to move on
so
the code is now in the currently in the
nav database I can close these worse
things and I need to get them into my
git repository so we also created this
function called netiquette which exports
all the objects and this is where the
filters that I talked about earlier it
comes into play and I can export all
objects which is gonna take quite a long
time time that we don't have and if I'm
lazy I can specify in in the workspace
settings what I want to ask what what I
want to export so here I think I've
specified that I want to export modified
files and
objects after type table with the ID 18
because why not we're being very lazy it
improves performance greatly when you
only export on object yeah
for demo purposes it doesn't matter it's
we could export all of them and they
will just you just have to wait a few
minutes they have to get let's do the
custom filters because we don't have all
day
and then this running in the background
trying to export everything export the
filters that I specified and
split it into the git repository
and if I look over here now my source
control I haven't I have a change so
this is the page 21 and I can see here
that's I've made a change I actually
also reset the date and time just
because it's a pain to merge at a
lifetime yeah that's a setting in the
settings file too right yeah you don't
worry it having changes on date and time
you can able and they disable this if
you want but in reality I've enabled it
now it just takes the same that is
currently in the in the git repository
of before actually overriding and it
still applies the modified yes
so I can look at the changes here let me
just make it bigger
and I can see that I've added yeah
and
I'm ready to actually checking I'm gonna
stage the changes that's because maybe I
don't want all changes actually to be
included in this committee and then I
have to tap message and since I was
given message task number four I'm gonna
write hashtag for fixed
and
I'm gonna commit
very informative commit message yes it's
really you look at the history you
really know what you did
okay so one of the advantages with git
is that I can I can now work completely
on this branch or I can change over to
another branch and work on that let's
say if I have a hotfix or anything I
need to do I can change over to that
branch and create my hotfix temporarily
and so I can store my work inside the
branch and it's gonna prevent for it
when I go back
so if I change branch now I'm gonna
check out the development branch which
was the branch that we actually just
started on
like this and you can see it actually
shared it just for a second there
that the changes now have been removed
and so now I'm in a different branch and
the changes are not in this branch so I
have to merge them and
I'm gonna merge my customer card action
into my current branch that I'm standing
in
like that and it magically appears
and yeah and that's really it for
merging two branches now this is get on
my local machine only on my local
machine I have currently done anything
this visual studio team services I've
only cloned it copied it down from there
I've only worked locally on my machine
and then I have actually have to publish
my changes up to the visual studio team
services where that where we have agreed
that the truth or well where the sauce
for this repository is
so then I I can do it here that's on the
command palette Dallas I just type sink
this action will pull and push commit
yes I would like to do this
and then it takes a little while I'm not
touching it I'm just looking
but then so I went away and it's set up
it said sink absolutely television
studio team services I'm now ready to
remove my development environment if I
wanted to do that
move
we move development environment and
actually on installs everything delete
sir delete the lab service here and
everything and just leave the database
like you want or that you had in the
beginning and then you have to delete
your own database and you can actually
also delete the repository if you don't
want that either I'm gonna keep my
development environment here because I
might work on it at a later time and
instead I'm only gonna delete my branch
because I'm done with the branch I don't
need it anymore maybe if I had another
feature request I could still use it if
I wanted to but I'm just going to delete
it
so yes I forgot to ever advance this one
but that happens so
input number two again
so what we just demonstrated was this
extension we have done
Dynamics NAV as a SEM
so we recreated it and we have our good
friends a cloud software so they agreed
to host it so it's in a cloud it's ready
it's out there today you can use it the
thing that does not you work here right
now is the darker side of it there's one
right now it needs a zip file with a
with a directory and it will install a
complete client on your machine I mean
you can have them next to each other
I've actually
actually install some next to each other
we're working on a version and we
actually demonstrated it right now
because that is the version we
demonstrated where it goes out and at
least for 16 and 17 where we have the
docker images available it will create
your development environment in the
docker image so the only thing you need
to do extra is just installed on your
machine which is pretty much download
next next next it's fall or finish
whatever
and and and and then it can take
advantage of that with PowerShell so the
extension itself just runs PowerShell in
the background
it does nothing else it it's just using
PowerShell to do all the things that you
don't like to write because you not
always all as good as PowerShell as
Waldo or Jonas
so so it's it's very
it's a very easy add-on or extension the
the thing here - I mean this bridge is
that you developers get in kid it can
use to work in vegetative code and and
and it's just an easy place you need to
be there anyway you developers need to
know about it anyway or us developers
need to know about it anyway so it's
it's a great opportunity to get started
with it and get a feel for it it's
nothing to worry about it is an easy
tool it's just a text editor just has
some smart commands and some smart
shortcuts instead of using the mouse
yeah I hate the mouse
there's all the extensions that that are
nice to have but not needed there is
actually an extension called visual
studio team services by Microsoft that
connects your wishes you decode to
visual studio team systems and our team
services and and but it's under not on
the source code management side because
source code is all we get is already
built in you don't even worry about that
part it builds in the connection to the
different tasks so you can stand in
Visual Studio code and see tasks and
connected tasks and figure out what you
need to do instead of having to go into
the website personally I like the
website but it doesn't really matter
it's open source so you can find it here
in the marketplace just take pictures if
you need it or search for it
just search Dynamics NAV ACMs you'll
find it
and it's available on github if you want
to contribute to it we really want you
to contribute to it it's it's it's a
great little tool that helps you in your
existing development to start with
source code management without having to
do almost anything it you can we can set
this up in 30 minutes from scratch I
guess about 30 minutes probably even
faster but and then you're ready to go
your developers need to know
about ten commands in Visual Studio code
yeah ten fifteen maybe I don't know how
many we have but it's not a lot
and and and that's all they really need
and then they can get going with this of
course they need to understand how gate
works because it is a source code
management system and need to understand
how branching works and all those things
and we know at least there's 30 of you
in here I don't know if you in here
sitting in the other session because you
already heard this that followed our
workshop earlier this week you guys
understand everything of gear so if
again you get questions from you guys I
will I don't know what we're gonna do I
mean we failed
so we have another demo that I want to
show you guys which is let me which is
not you know for once I'm gonna do a
demo
and that
is we I told you about the thing the
earlier that this was the foundation for
automation
so how can you automate this so this
computer over here is running on a
server in Asia and we were actually
using a
hosted hosted machine it's actually the
November of
the dynamics 365 sudden remember preview
I was running on that machine it was
easy doctor was installed everything was
install it was easy to use that one so
that's the development machine over here
I have a different machine it's also on
Asha
and it's also a preview so it's the same
previews just a different machine in the
cloud
this machine which was number 4 I think
yes
now I've not touched you so I didn't
touch it
but you can see a few things that
happened here
first of all
was oops I'm pushing the wrong button
here that doesn't help so
first of all something happened here see
something you've started running a job
here suddenly at 1302 few minutes ago
started doing something
now this is actually the build agent
that's running here now Microsoft build
agent is a smart little tool
that you can set up to run on a computer
in this case I have set it up to run
interactive so what I mean is it runs in
a command prompt and as long as I leave
it open it runs but that's just one
option if I would have said yes instead
of note it would have been installed as
a service and it would just be running
whenever the computers on it would be
running in the background so
great little tool the other thing we
have up here
that is
that's a new build here and I'm gonna
just change so you can see
the view here so you can actually see
the date
details look at
1919 when did it get created it could
create about you were sitting here and
while I was not touching the machine it
was fully automated that built
so what happened was that something got
checked into our development branch and
I'll get repository
we I've set up
build services for what is called
CI
continuous intubation the word was just
escaping me so this agent here is
keeping an eye on our gate repository
and as soon as it saw somebody but
something checked into the development
branch that happened when he merged it
well it didn't happen when he Merce
didn't have indistinct it back off he
merged the changed and then he synced it
back up into into the cloud into team
team team services
the build engine say okay something
there's something new I need to do a
build and
then it the build engine grabbed those
object files downloaded them download
local it spun up docker image it
imported all the files it compiled all
the files it exported a file file it
deployed the the the file file to the
machines we wanted to deploy it to and
it took the dog image down again now I
did skip two of those steps creating a
crazy after that documents and taking it
down because it just just to save time
we want to be sure there was actually
happening
we didn't want of risk that it was not
happening there was why I was smiling
when he was checking and I was watching
this one like yes it picked it up
just wanna make sure it's nothing that
can go wrong let that like to do more do
more things so we have a new build fully
automated or
automated our developers just did the
code when he's done he just need to
think about it anymore QA can pick it up
there's a queue and there's a queue a
database probably or wherever we have
deployed it we could deploy it wherever
we want to our QA people can go in there
start testing it and the only thing they
need to do now is tell our developers oh
okay we're ready we've tested this
please put that into production or put
it into use acceptance testing or
whatever your process is so you need to
set up the branches in in your source
code management that you want to put
this code into and
it's fully automated so that in this
case here we have we have a development
branch and we have a production branch
and if we would merge it oh we actually
set it up for development - for
production - so if we would merge the
way into production it would actually
pick it up again and it will create a
new build and you can see that is a
production we there's called master help
here where's my master but I think if we
do a build again it would be called
proxy because we changed that didn't we
oh no it's still called master with the
chordoma yeah this because we use the
master branch in git and if you don't
know what the master branch is don't
worry about it
we used to master branded in gate we use
that as our production database
Bobby Starr production code so we know
exactly what we have in development we
know the developers basically start
creating own branch do the development
they want to do when they're ready to
put it into development when it's been
approved we can just move it over into
production and the builds get automatic
automatically created fully automated so
how does this happen
well it happens over here in
this
here you can actually see the the built
definitions we have set up on this this
in this scenario there's two of them one
is development and one is production let
me go in and look at this one yes I
could have clicked it right away but
so you can see we have an 87 percent
success rate which is pretty good for
we have eight bills done so far on this
one at least in the last I think it's
eight bills and last ten bills I think
it only goes that father but back you
can see that it actually did it if C is
passed you can also see the recent bills
here and let's go in and look at built
number 19 here
which is the one we just did oh
you almost missed it
it comes out with a whole list of things
so I
have to point up here
so that whole list of tasks you it sets
up a development vironment initially
blah blah blah it does a build
which includes getting getting the
sources importing the artist compiling
the Arctic exporting the Arctic's it
does a deployment to
Oh
small mistakes is this a development
it's supposed to say development there
the code behind it should probably say
development -
and then we remove the relevant right
event again and we create a report which
is the one you see out here so it
automatically created this it also
automatically sent an email to the
developers saying you built has been
done and
these are the Associated tasks or their
source interchanges that you did to
create this build and
that's the task you were solved now if
this would have been typical scrum
development you would might have had
three or four tasks that you had done as
part of resolving this feature or this
product backlog item and you have them
in your own branch and then you finally
you merged it all over and send it in
then it would have listed the all the
changes here that was was done and all
the tasks that was resolved by doing
this
so this is like this cool oh
it's only two things it's cool I
think this is really cool
so how do you do this
how do you do this well there's a build
definition here and this is so easy you
won't believe it
it's very very easy so you have a built
f edition here
it basically does a couple of things up
here that this is the process this just
defines the process this defines where
you getting the where you getting the
code from which repository you're
getting the code from after that there's
a bunch of faces here whoops the face
here to set up the derivative
environment want to do the build want to
do deployment want to remove the
development environment and under each
of those ones there's a PowerShell
scripts that
run whatever they need to run
so if we look at this if I click
standing on the header here that's just
the name and it's agent pool we're using
we're gonna use default to what I
destroyed it so
clicking on sources in this case we say
I want to get my source code from this
repository and I want to get it from or
sorry this project and I want to get it
from this repository if you have it on
get you click on get and you give it the
parameters from forget and it will do
the same thing if you've got bit pocket
go ahead the same thing again and then
basically when you've done that there's
a face it just it's a collection it's
trying to collect and organize things
it's not a lot of setup here so don't
worry about that and then this one okay
I know we did not create the docker
image on the fly and we didn't destroy
it on the fly but basically we could
either here say I have a PowerShell
script that I store in my source code
and I want to execute that power
subscript or I can do in line and just
write my code here now the in line I
must admit it's not great because you
don't have you don't have all the nice
features of
power sale right you don't have
all the color coding of the code and all
the nice stuff but you can write it here
and it does work
it's a little challenging though yeah
there's also a couple of things you can
do to your script look I set up some
variables here I didn't set any but we
could have had variables here that had
DB server oops
name you could have created a server
name here and said
just a little internal joke here
right so we could have yeah somebody got
it
so that for server that we would that
that what would he call that that's just
a variable name so that variable name I
can now use in all my PowerShell scripts
so if I want to create some generic
PowerShell scripts I put them in here
just make sure my
built-in definition is the same all time
I just changed the variables and I'm
good to go
the other thing that I think I'm not
gonna go through everything here but the
triggers here kind of neat so this
trigger here is the most important one
in my opinion and you can use that you
can choose to use it or not that's
continuous integration
so this case it's enabled so it picks up
automatically any changes that happen in
the branch we have defined up in the
earlier and
oh actually no the branch is here but in
the proportional review defined earlier
right so it just picks up any changes
there any changes trigger a build you
could have done it differently you could
have gone over here and said I want to
schedule it and run one every night but
if you got 40 customers you make changes
to two of them in one day why do I do 40
bills just much easier just do the bills
for the ones you do and remember you're
not doing the changes before something
gets most into development so
Jonas could have done ten changes in his
in his local branch that he did used to
do the development and before he merged
it into development and synced it up to
the cloud nothing was triggered because
it was only on his PC it was not checked
into the git repository so the fact that
you do a build every time it's not a big
deal it's actually pretty awesome I did
put the flag here there's a flag as you
can see here to say batts change this so
in case I'm doing a build and the bill
does take a little longer than it did in
this case here but
just because we caught a few things but
in case that you do a build and two
other changes have come in it's not
gonna do a build for every one of those
changes it's just gonna do it bill for
the last one in that case just to catch
up right there's no reason to do builds
that you never gonna use ever
so so that you can setup however it
works for you and there's also a lot of
other things here there's retentions
there's options there's history and and
all kinds of things
that are very nice there's also one
thing I wanted to show you
I'm didn't do any change this so leave
page I hope I didn't do energy instance
I've created a variable and didn't save
that that's why I didn't it was
complaining so if you look at the bills
here that was created bill 14 here
it's also you get success rate you also
get this took five point eight minutes
to be do this build
you I forgot to tell you that and show
you that but tons of different
information you can also download the
log file if you were interested in that
or you can go out here and look at the
different things if you want to see how
did I create the doc setup development
environments I can click on my darker
and it will show you the
powershell that was executed in order to
create that now in this case nothing
right because we didn't put anything in
there I'm not gonna go through the
PowerShell off the other stuff because
you're gonna laugh of it
well we let Walter deal with PowerShell
that's not the point of this power
demonstration okay so
and
really this is just an Indian it's
called a build agent or an agent it can
do whatever you want you want to run
tests and you want to have the test
results spit up you can do that here too
it's just run them now we're talking to
Freddie yesterday there's a few
challenges with darker and testing but I
think we found a way around it maybe so
we will hopefully will we can write some
of that so
but that's the general idea
this is all automated now you don't need
to worry about anything okay
how much time do we have left about 40
minutes
36 so let's go
eat this one I need to push this one
right
yeah okay so keeping discipline and
consistency in delivery
the that's one of my
okay so one you set this up why this all
automated its is its it focuses the
developers again on doing development
Yuki you take the developers out of
delivery you let the development you
focus on development they don't do bills
they don't do all the things that they
don't need to worry about they need to
focus on doing great development and we
all have the same issue I'm sure you
have the same issue you are usually
short off you're short of developers
it's hard to find good developers and
hard to find new developers when your
business is growing but if you could
focus your development team on
development and not all the other things
then you can make your development team
more efficient you can make the better
you can train them better and never let
developers touch production databases
that's just a rule we put in place at my
company
because that means that you
consultants they want to develop us to
deploy things and stuff like that no
that's IT we also run most of our
customers on ashes and that's IT doing
it in the first place so we do the bills
so push it to IT let them do it most
cheaper resources and they have much
more capacity to do those things
okay only deliver bills to customers
that's one of the things too we have
that is we don't want to have these
small bills I don't know if you saw it
when I was up there but that was a
complete build that was every object
including all standard objects that gets
delivered to the customer every time
it's the only way we allow delivery to
the customer why well if somebody does
something messy out there it gets wiped
out good but and they can learn to do it
right and we know this works we don't
know what's lying out there if that
works or not get
so it's a good way of creating a
scenario where where the people cannot
take shortcuts can only I don't have
access to my customers databases IT does
I deliver full bill to them from the
build engine IT deposit there's no
issues we we have not had I think we've
had these issues once in like the last
one and a half year we've been doing
automated bills
and again this is a foundation for
testing foundation for automated bills
and it's that ite deal deliver
using branches in gate you saw here we
we had we were using all three branches
technically we use one branch for the
local development so good practice is
also always some let you develop a
creative branch for the development he's
about to start and
and do that and then we are using the
two branches that we used the two
branches of
of the actual
they did what he call it often of the
team which was one was development and
the other one is the master branch so
that's the one we used for production so
master branch is in get there always has
to be one branch and yet by definition
gate has created this master and
and and that that branch is we just used
it that's it okay this is our production
brands
have a safe trip for Margot
he's okay you catch the cap okay so
so we use just development and master as
our branches now and
in my world we have a few more branches
so we have a development branch where we
check in development then we have or
sorry commit and why do I keep saying it
and know why but I need to learn to say
commit in the gate world I know yeah
look you laughing off me - because
that's what it's called chicken when you
are losing classical development in
source code management so classical
source code management
should only committed mafia
it should not commit enough you read
through okay so we got four of four
branches we got a development we got a
test we got the UAT and we got a
production and production would be our
our master and that's just the way we
have always done it we have a few
customers that require extremely high
level of
of security for but that we don't break
their code so we have an internal
development where we check it into when
it's ready for QA we put it all to the
test branch when it's it should actually
be ready for QA when it goes into dev
but
those stupid developers in my
my place me
can sometimes break things and then
if from test goes over to you eighty
which is user acceptance testing and
then once the user has accepted and
tested and everything is done with of
course with the customer license we move
it into production which is the master
branch and then we we do build its
automated we do build for every one of
these ones and spit it out on the other
side so that's the branches that that we
use oh here's the bills
so automation consistency of quality
predictable results saving time and
focus your team this is if you don't do
it today you need to get on the wagon
this is just not an option I've been
preaching this for I don't know some
people are probably tired of listening
to me but I've been preaching this for a
long time but I think Luke and I was
actually I think we were the one that
started it out about hope I think we
were both working at Microsoft at the
time when we started talking about it
for the first time many many years ago
10 12 12 years ago
something like that
of course this is me I can't say not say
anything about scrum and agile because
that's the other side of the story that
is you got a half you got to make your
development team
work efficiently as possible and who's
better to do that then the development
team if you let them focus on sprints
and you clearly defined and I don't know
how much you know about scrum and agile
but I just want to say if you don't know
anything about it you need to start
reading up on it it's not that this is
the only way that things are going to
work but it has been proven to be
extremely effective
agile development practices are core to
getting an effective development team
and
it's it works because of just the way
that is the syntax and the I think the
best part of it is your development team
becomes kind of self-organizing if you
got five to five developers in the team
they know what works and they know what
doesn't work so they'll figure it out
don't have to manage them on that this
is I don't want to go into a scroll meta
I could speak a whole whole day about
that so we actually way too early
finished yeah because our demo was just
so really good
so QA
we had no way since yeah you can
can we get the blue one on
how do you ensure that the IDs you
generate when you modify something in
table code unit for example are unique
for a local development environment for
example and you have two developers
working on the same object but in
separate yeah changes yeah so the ID or
yeah so generally so control ideas in
when you do object development or do
development right it's very easy to get
conflicting IDs
because our teams are self-organizing I
don't know how you guys do it well you
not really that far yet but
the way we do it is we know what task
we're working on oh you're gonna take
the customer ok I'll take the window not
right now and we'll just stay out of
each other's way that's the easiest way
you also avoid most conflicts and you
don't have many issues for that so
that's the easiest way to do it yes it
happens but it happens mainly on pages
and reports and if two people are
working in the same report you need
better planning if two brave people are
working on the same page it can happen
and it's not a big deal because most of
the time they added a button or field so
just roll back and do it again well also
a few seconds experience that if you
might experience it when you try to push
up that you have changed the same
and you're gonna maybe make a merge
conflict on your local machine which you
don't have to resolve before you can
actually push up into PC of studio code
which is 2d team services and if you do
the automate build and well if you there
is no merge conflict there's still an ID
error you and you still do the automated
builds you're gonna get an error when
you receive that maybe I should've just
shown the the email that you actually
get so I received this email which says
that the build was successful everything
went well but if you break something
well you got a failed success they both
and then you need to fix it that's your
you have to do as a developer
the last guy checking in
it's a very cool thing that is you break
it you fix it and the team should manage
it yeah see - is it okay it takes I'll
be the killer to get a build email
within minutes right of checking in yeah
they should talk to each other anyway so
they should yeah even though I could
curse and ask my managers I didn't curse
my developers not to check email because
that's just a distraction from
development okay thank you
Christians
you do fight about it
okay how does your extension cope with
deleted objects does my extension do how
to close with a delete object yeah
delete objects yeah it does it does
still with the lead objects is actually
select sent to the object table and then
calculates differences between the
database and the files that you have in
your source repository so I
automatically included in to commit
automatically included in the commit
yeah well it actually deletes the file
on your file system and then guest
actually asked you do you want to stage
this change is it something that you
wanted to delete well probably if you
did it from the day soon yeah so
basically as soon as you you
get your files in it will actually
delete that in your local repository on
on your machine and Visual Studio code
will pick it up and say Oh something has
been
something has been deleted so then you
have to commit your changes and you see
the file has been deleted you okay with
that you say yes and it picks it up it
creates a build in the background it's
all automatic in the background right
and that build has that the RP doesn't
exist in the build anymore it's gone
yes would you deploy the bill to the
customer and he has the object in there
it is still in there there's no delete
or kill object in in in the system so so
yeah but it handles the lead optics
there's no issues with it I also want to
ask you is it is it is a resume okay if
we have clients is the same enemy
version with different bills does your
schizo work correctly
you mean different different different
versions yes yeah so the initial setup
you can bring the setup up maybe
this what I don't know if you have
access well the screen is kind of gone
but it's coming back now
you bring your setup up just the
settings you want to see the settings
master
workspace settings so in the settings
file here right there's a you you're
defining
what's the database the database name
only it's right here yeah it's called
financed us right in the image that this
settings file here is for darker if if
it was if you were not using darker so
that's my parameters are missing here
because we actually skipped kind of the
talk I think there's one parameters were
missing here that would be the the the
link to which dr. Amos you're using and
that would be who was asking because I
can't see anything I'd like this okay so
it would actually you will tell it this
is the version I need to use for for
this installation so when it creates the
development environment it will create
the right correct version and we and it
will destroy the right version and you
can have them next to each other and the
same thing if you use the classical
developments of a 13 13 r2 and 15
it there you you point to a product CD
which is we you remove that here too
right yeah because we we didn't use that
part of it now
but that is a setting for that oh sure
we can set it up there yeah so you can
you can point to with which product CD
is it that's on a honest year somewhere
right so you probably have all your
products you downloaded to share
somewhere that people are not allowed
touch so you can just download it there
or your IT does it and you can download
their pointer to that one so it always
knows and you set up a new environment
ok I go and grab it there period so
that's how that's how that works I see
so where is thank you for your great
great extension and one another question
what is your recommendation if we have a
client school also developed
well you can do that in some different
ways but one way you could do it is you
could export all the updates and then
give them to developers and say please
merge this in to the development branch
then you see all the differences that
they made the customer has been made has
been making and then you would actually
just do the same thing I did here you do
that
toward up there so you could hit this
guy out there
yeah what is one of them I'm sure they
have questions yeah awesome
you mentioned the importance have been
able to promote one modification push
that live jump the queue ahead of other
modifications which being works fun yeah
can you give us a brief word on the
process to manage that so so yeah I mean
it's it's not always recommended but
it's just real life right so what what
you can do is because you know the
history and maybe you can do that can
pick up the history of you want to get
lock I'm just making you work here for
it okay
so
trying so there's an extension we have
kid lock motor also shoot this we just
need to install for a second here and
you're good to see that you can do that
we couldn't bring it over you can bring
it up you can see the hit you can
actually see the get the branches and
everything you can see that online in
team 15 for this team services or you
can go into gate here and bring up the
the history
which comes up in a second here
of course you need to understand how to
howto on how to read this but it's it's
pretty simple actually
of course that doesn't seem to work
right now but did you restart it we
loaded yet I'm just gonna go here
so so here's here's the branching right
so you can see you can see there's two
branches that are running parallel to
each other and then it gets most Birds
back in again so you can see you do
development you do development and then
you merge back into to the master branch
so the development branch and but what
you can do is you can continue
developing on this branch that's parked
out the other side you can continue to
develop and develop develop even though
you merged it in you can merge
everything in you do have right now or
you can start cherry picking from it and
say I only want this this and this
change in right now
you have to be careful when you do that
but that is actually why we have a
development branch and the test plants
in at my company because development
takes into development when they're done
and then we cherry pick two quite often
we will cherry pick and put it all into
actual testing
because we want to make sure that when
we cherry picked we didn't break
anything
so so that's that's one of the reasons
to to do that but you can cherry click
and say I want this commit this commit
in this commitment show it our okay
there was another question behind you
there little I
mean while I see my control this one
almost it's not as good as Waldo
you showed that you downloaded the
sources to your machine and then did
some code changes but and then uploaded
it sorry committed it
but before I can commit I have to test
it as develop the developer before I can
give it to the repository maybe yeah and
if I have
different customers with different
databases with different dates in the
database how is this managed to have
this locally this data where can I test
my changes that they run before I commit
them okay so so the course you're
running on your machine and your machine
is set up with exactly the same date
time settings and regional settings and
code pages as every other development
gene you don't have different dates it's
they're all on the same date no no no
sorry the data of the of the customer
because you can test against the Chronos
or something like that yeah yeah my my
changes I did to the to the code before
I commit it right but how is this
achieved when the the customer databases
are maybe 50 gigs or something like that
and I have many customer customers I
have to deal with that how can i isolate
the the developer and it's very him
tested very simple the developer
shouldn't have access to the customers
date data in Europe after I was in May
first the new privacy laws comes into
place you really don't want to manage
the fact that developers actually access
to all the customers data it's gonna be
a nightmare so I
when we run this I use Chronos data and
if there's more data needs to be created
in order to test something the developer
can quickly create it and
and test out what he needs to test and
once if you want to test it with
customer data that will be the cue
there'll be cat caught in the QA testing
or when the customers computers where
it's on control be weak unit testing we
run on a customer's computer because the
customer wants that okay so after to do
the test setup for for the developer
that you can say okay just run against
Chronos and some modified data that is
normally customer like yeah okay yeah so
come down and get the last T t-shirt
would you run okay
yeah there was a testability session
earlier yeah right can we get the red
one on
and I have a question about the license
what if we have a customer that we get
from another partner and they have a
solution which we don't have in our
developer license how to get the objects
out of it I'm really sorry that you
don't get a t-shirt because it's
actually a really good question and
Eunice has a really good answer to it
yeah so actually when it selects from
the optics table it also detects fast
that it couldn't make sport and then I
assume that you don't have a license to
it so it actually exports the FOP files
and then you can commit them into it
into your repository as well as FOP
files named after individuals once so
it's not going to be good if you take a
cost Acronis license and export
everything because it's gonna export
every single object in one or individual
object in individual thought files it's
gonna be quite big and quite slow but it
actually exports the file size up or
exports as a thought so basically if you
have any add-ons with 20 files that you
don't have access to it's gonna create
those 25 files those objects separately
you store them in source control and
when it needs to restore the database
later it's got to restore the file files
instead of the text files because you
can't edit them anyway so you're not
gonna do source control on them oh the
only way to do it and it's built into
the tool sounds good awesome question
something we forgot to tell
any other
lots of questions you
received when you this is mostly not
customer driven but what is when you
work with localizations do you then also
crunch your local when you let's say
want to also always update one or two
local versions when you mainly work in
the
w12 you branch odo is it then a second
project well yeah we we don't have
multiple we've not set it up we've not
created it for four product development
as such which is what you're talking
about editing one version from Ultima
multiple ones we've not actually
optimized for that right now I don't
know we could probably come up with a
strategy foil
but we've not thought of that we not
worked on that right now because our
focus was to try and get people that do
customizations to do source code
management and get used to it so they
start to see the value of
or automating it and testing it and then
hopefully get into product development
and we want to help the whole community
move in in the direction that we think
they need to be we could be wrong but
that's okay okay Steve you had a
question I
can be I can see some hands up there
somewhere but it's pretty hard to see
them but I saw Steve had a question here
you don't get a t-shirt either
is it even worth asking a question then
have you tried with the tool or looked
at using time stamps to track the object
changes rather than having to set actual
filters in the settings to look at
certain objects that way it picks up
anything you change so you can just kind
of go crazy and have to care about
settings file no
because it's it's pretty hard to do that
when you recreate the database every
time yes
that's why we've not looked at it yeah I
mean if you start from a certain point
when you create the database from the
tool you can always store and keep track
of the timestamp right then every time
you're updating nav from get then you
can keep that timestamp yeah but that
would only work when if you have one
developer developing at one time because
if you have two developers developing
and in the same database
which one do you restore which one do
you keep but but it would be a local
setting I guess in the workspace right
it wouldn't be
I guess yeah you could do it that way
that's it's not we're doing it that's
how you're doing right well yeah but
then we would also have to back up the
database every time in order to remember
the timestamp because if we restore the
one we reduced our database right now
it's a standard Crone's database coming
right after par CD yep so it gets a new
timestamp every time know for sure and
then you dump your objects in and then
okay so you're just one okay and I'm
talking the timestamp like the sequel
column right I'm not talking about the
date times on the objects for any cuz
that means nothing something there's
something we could consider if that's
because it's I mean every time you
compile that object it updates or any
time you touch that object it updates
yeah so it's it's only internal tracking
mechanism yeah it's not a bad idea how
many time screws you if you compile it
might see you for some reason
my other question that goes back to the
hill it's enough that you've been doing
I know and I really don't get a t-shirt
come on
have the stuff that you're doing now
with docker I'm guessing you're now just
using the online build agent you're not
using one of the ones that you've hosted
yourself right yeah so both the machines
that we were showing now they're at the
edge of the lying in Asia
so are they your Azure machines are
using the hosted build agent because I
would know we are using ours it's our
machines it's not posted yeah so it's
okay so just to explain so when you you
you you do a
built in in a build agent you can use
hosted services from Microsoft so or you
can have your own hosted computer and do
whatever you want with it so we can't
use the hosted services because there's
a bunch of things we need to install and
and right now that's not possible on
host associate whenst once dark light
comes later I was gonna say stalkers
really in place then you can go we could
probably use the host of services that
was our biggest challenge as well as
trying to install all the extra stuff
that we would need yeah can't do on the
build agent exactly so it's not you
don't do it on the build a team but you
do it on the build a machine that
actually runs the build agent right yes
exactly it needs to be installed there
needs to and you can't do that the
hosted services those machines are much
cheaper because they've just they're
pulled together and hundreds of
developers are heartless of customers
and potentially using them at the same
time and they're free yeah and they're
free to or for 250 hour yeah a build
agent like the one I have running here
will cost you about 80 bucks months it
is not a hundred maybe I don't know
something like that okay good questions
no t-shirt for you
yeah trying go up there was a few up
behind here see one over here it's also
too if you like
once out in front here because I can
actually throw that far
so the question is here somewhere
hi hello my
how do you go about implementing
something that effects multiple of your
own data bases say you have three
versions you supports 2016 17 and 80 and
then you have a bug fix that you have to
implement in all three versions
are they all within the same development
area or are they completely separate
projects in visual code
so that was the same pretty much the
same person I think that was ass down
here Cammy boudoir somebody down here
that was asking it I
don't know
so the way we did this right now is
mainly focused on custom development so
it's not me it's not it's not really
planned on on on having multiple
multiple supporting multiple versions so
for verticals and that's type it is
limitation right now I'm sure we come up
with a strategy to actually do that
because
well somehow it has to yeah we had the
opportunity there you can actually ask
it to take a commit and pull them over
to other branches as well like really
easy thing you just create requires a
bit of an advance come on yeah so yeah
you can create a branch for your 16 17
18 build and then you could just if you
have a hotfix that you need to reply to
all of them you just merge into each and
every one okay we might need a few extra
tools and a few extra settings in the
extension but
well come and do it help us out
and the day a date yeah thank you
Hey
actually I have a few questions for you
oh man the first one is related to the
hierarchy between the branches before
you showed
there were four branches if I understood
well one dev test the you ATM prod right
what is the hierarchy one is the child
of the other one a dog one is the master
yeah technically it is because you got a
branch out but again it depends on how
you work I think
you don't necessarily need to think of
them as parents and child's because it's
prancing in gate and they kind of live
their life parallel and then you can
move things from this one over to this
one I continue this one but yeah but the
first step is that you are pushing data
to the development that is the lower
who is moving - yes it's a person I mean
if you think of it that way you have the
master of its production then you have a
branch that's UAT which is user
acceptance test and you have a branch of
that one that test and you have a branch
of that one that's development yeah you
can think of it that way okay right
branching in git is is so agile it's
it's it's it's a way of thinking of it
but it is really parallel branches that
kind of yeah I'm going to do together
but you can think of it that way yes
that's a good way of thinking of it okay
at the end of the Sprint when you
release you release all the objects
modified yes all objects all of them no
not all art is modified I release all
objects every time all the bells the
bells are automatic you could change the
build in order to actually set what
properties you want on the object you
could also change it to make a decent
version list that you actually want okay
you only need to like write them well
pretty advanced PowerShell but you do in
which step do you have the automatic
tests
well what point I test yes after
development
well we test several times right so the
this case here right
built itself is one test it built
actually what I understood is telling
you that you can compile all the objects
more yes nothing more so what doesn't
mean that your code is work in the
function and working absolutely correct
so that that was what I was saying that
is you can add more faces to the to the
build script or the agent the script
that the agent kicks off and one of them
could be testing or there could be multi
one multiple ones that run tests test
code units is there any example online
about the build definition code there
was a great presentation by these two
gentlemen right before us
you didn't automate it okay
we saw like a black box so you are
running dead yeah I'm running my script
you are running your script but what's
the difference but I know these two
gentlemen down here no they have done a
lot in test automate so to do all
automatic tests and they've done far
more than I have unfortunately so so I
would kind of yeah go and ask these two
did they could probably tell you a lot
more about it and the time frames it
takes to actually implement it I was
listening to them talk about it earlier
but it's it's really that's one thing is
to create the tests and get them ready
and put them into source code and all
that that's just one thing the other
thing is running it and running it you
can just get the build agent to do it's
it's a PowerShell command you put it in
there you make it run it even on darker
was the only issue we had but you can
just make it run it and either pass or
not and
that's it about the life cycle of the
branches before when you read your tests
the developer is deciding to destroy the
branch but in the reality is there any
agreement I don't know as soon as the
test is passed you can destroy yeah so
the
development of what Jonas was showing
was that he created the branch locally
on his machine okay data development he
didn't only did one chicken or commit to
his branch but he could have done five
six seven commits to his branch and once
he was done with that he were stood over
into the development branch okay and
then he destroyed his own branch now at
no point did he take his own branch and
push that up he only took the
accumulated chains as he had done to fix
one issue and put them into the
development branch and pushed those ones
up okay then when functionally you are
testing if there is a bug and young
needs a rework he will create another
branch
yeah you can create a branch again you
would get a in my world I don't know in
his world but my world the the pbi the
product backlog item it has been done
and completed because the developers
thought it was done and if it's not done
best box and then he's going to get
about to fix and he's gonna have to fix
that one and he's gonna create another
branch for that but again he's only
creating it in his environment it's I
don't see it other developers won't see
it it will never go into the main
development repository it's just a local
thing on his computer so he can manage
it and it's just it's a bad habit to do
all your commits towards the main branch
because once you then sync it up
you'll see in in the in the main branch
you'll see all these commits and
and and and oh you only really
interested in the accumulated effect of
those commits
you have to do something that isn't
completely done yet yep you might have a
problem yeah if you've committed
something because that's the other thing
right if the developer works over two
days and what if his computer goes down
you want to have safety that what he has
done is saved right so the convertible
will commit all the time every time he
does a change you just quickly commit it
so it's safe whatever he's done has is
safe on his computer right
the database can break and stuff like
that but if if if things as safe on he
at least his get repository then he and
he didn't take it into the development
branch no build got kicked off and he
doesn't break the build is still compile
for it because it might not compile
where he is right now my understanding
is that you are packaging the
information per branch so when you're
the information is arriving to the
development it's per branch yeah then
when you are moving to the next step so
the test or do you eighty or what you
want so you have to select which branch
you want to move in the manual you will
have multiple branches related to the
same pbi actually to the same task well
they're not in the main one because now
you're talking about the developer
ejected into development somebody is now
gonna say okay it's ready for for tests
or it's ready for something else right
somebody's going to go in and say okay
now I want to move it over they he can
choose to like I said before over here
that he can choose to say I want to move
everything over that development has
checked in right now and do a build on
that or he can elect to say a cherry pre
could say I only want this task this
this and the three other ones I'm gonna
leave back and that's the only thing I'm
promoting right now is this an agreement
with the customer
sometimes it is sometimes it's not
something sometimes the customer has a
project where he has some legal
functionality and it has to be
implemented on May first so he doesn't
want it most into production before May
1st
and and because it has to function the
old way until May 1st so best stuff like
that but it's all a discussion with the
customer quite often when it's custom
development when he wants what and
sometimes a new check format you don't
want it before you for that you have two
new checks okay stuff like that just the
last question sorry
how to manage parallel releases means
that you're working in a project you
completed one phase of the project that
face is going to see it okay and then in
parallel you were you want to continue
the second phase of the project so this
means that at the end you want releasing
two separated databases no you can't do
you have one you have one you do builds
for your UAT and you do builds for your
production you do build for your tests
they're all parallel at the same time
all the time so you see so you can do as
many parallel
tracks as you want you just do as many
branches as you want to do
if you want to if you want to have at
least if I understand it correct I do
not understand this parallel to your
saying because a branch is like a tree
so you have a father you have a children
and the father your father is the master
yeah in this case multiple release means
that you have a two masters yeah so the
reason I don't think I think the reason
you don't get it is you're used to NAV
and now this kind of like very that's
just one line right
that you are where you are this is not
wherever you are just like you have this
line of development you have all these
branches that go out from it and we can
do bills from all all of them in this
case we're doing bills from two
different ones but we could have done
four six eight ten
and we just need to have an agreement in
the development team or with the
consultants when we merge things in and
when we are ready to do the bills
but you can manage as many as you want
next to each other the one thing that I
do say that is please make sure that all
developers when they develop whatever
they developing that they're doing it in
the development database because
otherwise you get ID ID and control IDs
and all kind of conflicts and you don't
want that object conflicts and so on so
make sure development is done in the
same database but how you merge it out
doesn't matter
okay I'm not 100% convinced in this
it's come yeah come come to the workshop
which we was was two days ago
well you can do it with get because get
you could go back in time so
technically okay last question it's you
I can see you
on your local machine
the issue with having
several different
okay very technical question I don't
think we want to I don't go into that
you want to show it but well it relies
on port gr that's the only thing I could
say you can have multiple versions of
that and also if you need to do
PowerShell I actually have
I don't think you understand my question
okay Pol Pot Shang only sorry if it's
the same question if you have now 13 15
16 17 on the same machine they all write
to the same point in the
Windows registry yep
so we we are very very very clever
people so we figured out a way to get
around it
it's it's almost perfect that's I don't
think we have had any issues with
anything right now
but but I mean not saying that that's
not a mistake somewhere but it was
almost perfect okay relieved that as the
last question we are already four
minutes overtime even though we were
done way too early what we anticipated
there's we just did that because we
anticipated there would be a lot of Q&A
of course thank you very much guys
[Applause]
