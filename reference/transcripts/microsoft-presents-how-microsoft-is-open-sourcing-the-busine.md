# Microsoft Presents: How Microsoft is open sourcing the Business Central applications on GitHub

- **Source:** https://www.youtube.com/watch?v=fNnmLeIj4OI
- **Video ID:** fNnmLeIj4OI
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 77m39s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

thank you very much uh as thank you for
the presentation my name is Alexander
and uh welcome to this session on how
Microsoft is open sourcing the business
Central application uh on GitHub uh as I
said I'm Alexander I'm a software
engineer at Microsoft with me today is
Yas yeah so my name is yunas I'm the
engineering manager for the Engineering
Systems team with the uh platform team
of business Central so we deal with all
sorts of things relating to builds and
GitHub and you know PLL requests test
execu development environments like all
these kinds of things and this kind of
stuff we'll be talking about
today and my name is Freddy Christensen
I'm a technical evangelist with
Microsoft sitting actually close to
these guys in the building and working
together with both Alexander and yonas
today on Alo for GitHub also responsible
for Docker container Helper and other
kinds of things that lies between what
we are using in Microsoft and what you
guys are using
in in your uh area
so let's talk about what we will be
covering in this session and we what we
won't be covering we we're going to talk
about migrating to Al go forthub but not
how you guys are going to migrate to ELO
fora we're going to talk about why and
how we are doing that so it's a session
about basically what these guys are have
run into of challenges by taking us and
saying we want to do open source
development codevelopment with you guys
on business Central uh we're also going
to cover how we ship fixes and features
to the online tenants and how we secure
the supply chain discuss release
management and how open sourcing is
going to change that what goes into our
releases what is like when we talk about
the next version of this then then we
have a number of of different things
that
will add ideas and will add like uh work
items to our schedule and and how will
this yeah work with open sourcing and
can you guys just ship something
together with
us without putting it ever into our
plant and and and how is that going to
work and then uh the what's next item
what's next for open sourcing and what's
next for Al go for
GitHub and then we'll see I think we'll
leave some room for for for questions
after that
but first of all a disclaimer as I said
this is not a session that talks about
how everybody is going to move to GitHub
in fact it is not a goal for Microsoft
and it's not a goal for me that
everybody will move their stuff to Alo
for
GitHub recently we put this survey out
on LinkedIn and and and Twitter or X as
it's called now um to get some answers
on where the the the current like
landscape is for people using
devops um I got a lot of questions oh
this is like they people are reading
between the lines thinking that this is
an attempt to find the people who are
not on GitHub and make them move to
GitHub it's
not um so but it
is
a an attempt to see how many people are
in the non bucket up there it's like 14%
of all
Partners participating in this survey do
not have any kind of devops today and I
think that's a
problem I don't think it's a problem
that we have around 49% on Alo Al Ops
and
alpaka I think those are
fine they are managed Solutions there's
somebody taking care of the maybe not
the pipelines but definitely the tools
and the tools that that you're using so
whenever there's changes to Powershell
like Docker Windows SQL Server stuff
like that somebody is managing that uh
it can be quite a t a big task to
maintain all of these things if you are
doing things
yourself and the very
tall here uh the the the self-made
are probably people that have
participated in a cicd Hands-On Lab at
some point in time and decided we can do
that
ourselves which was fine
today I think people are spending a lot
of time on that
and we would like them to
consider whether the best choice would
be to move to a managed solution at
least calculate how many hours are you
spending on staying on something you're
building yourself
versus how much time uh you would save
how maybe your resources could be spent
on something that actually provides
customer value instead of of of working
on internal system that could be done
much easier I'm totally aware that some
Partners have like a setup that that
vastly exceeds the uh the capabilities
of algo or maybe even Al UPS or alpaka
uh that will need to do things
themselves like we're doing a lot of
things uh on top of ALG goo as well in
Microsoft but I think it is it is worth
mentioning that people in the self-made
bucket will have even more work in the
future stuff is happening right page
scripting uh uh yeah code coverage other
things all the things that we will be
providing for these
tools people that made them themselves
will have to like do stuff to every
single of their repositories in order to
uh to uptake those changes right
so why are we migrating to
GitHub why are we open sourcing business
Central is something we'll cover later
why are we open sourcing business
Central on GitHub is something we'll
cover
here GitHub is the largest open source
community in the
world million of developers and probably
every single person then here has a
GitHub account as well uh so people will
have the ability to contribute or
co-develop with us very easily on
GitHub that's one reason next reason
which yeah could stand alone all
Microsoft open source projects must be
on GitHub okay we couldn't get around
that one
so when we are open sourcing stuff on
GitHub well we we have to follow uh a
license
we we have to to to use a specific
license for that open source project
there's a Code of Conduct that people
have to sign a CLA with Microsoft
whenever they whenever they contribute
with a piece of software they we yeah
the system will take care of a lot of
stuff for us and we are followed to uh
we we're forced to follow all the best
practices that Microsoft puts upon us so
we cannot have like secrets in uh in our
in our source code and there's a lot of
things that will be flaged by by our
internal systems if we if we don't take
care of
that we want to leverage all the
innovations that are on GitHub there's
tons of new functionality coming like
every single month there'll be yeah a
lot of functionality coming constantly
we'll talk more about that in a second
and um we want to use the same workflows
as our partners by creating a tool like
algo for GitHub and and providing that
for our partners to use we'll be using
the same tool as our partners are when
running on that meaning that when we are
going to like add stuff like code
coverage or page scripting uh
functionality to algo then Partners will
be able to use that the same day as we
start using that and last but not least
we can help train co-pilot on Al the
more source code that's out there in
open
source the better the chance that
copilot has to actually
learn about
Al so GI up Co copilot Innovations like
if we look at that now there's a lot of
things coming I think I I don't know
which of those are for the Enterprise or
for the business uh Edition and what is
free and what's not uh a lot of this is
available also if you're using vs code
so you can actually do the G Co GitHub
copilot chat in v code I think but
there's a lot of things coming to GitHub
in the GitHub UI to like if if you have
a pull request it's not only the pull
request description it's also discussing
this pull request with copilot and other
things that copilot will constantly add
to the GitHub experience and all of
things all of those things we we kind of
get for free right other GitHub
Innovations like have have anybody ever
tried the Copa the GitHub
search a few it's like instant search of
all the millions of repositories out
there uh kind of like Google just for
just for code right and it also searches
in your private repositories so you can
search like your code or Global and yeah
it's just amazing how fast that one is
in comparison to to everything else when
you're searching code code spaces
something coming for GitHub and Coach
spaces uh is really today if we look at
GitHub coach space is the it's the idea
of having your development environment
inside of GitHub so so you'll be
spinning up a Docker container kind of
inside of the inside of of GitHub and
then we can run the a language extension
in there unfortunately code spaces today
is a Linux container so we cannot run a
business Central instance inside of that
we can run the SQL instance we can run a
lot of other things in there but the
service here is not made for for for
Linux yet um so maybe one day that's
possible today you'd have to use code
spaces with some tweaks to connect to a
container outside of code spaces or to a
online
sandbox we'll make this an integrated
part of Alo uh as well as we go forward
there's a GitHub Enterprise importer we
actually did not use that when we are
importing stuff from Asad devops
and there's a lot more including a
certification program on GitHub and
stuff like that there's a lot of things
in in in preview on GitHub I don't think
you can read that can you yeah probably
there a co-pilot workspaces
that uh I think sa Adel actually
mentioned that build conference um and
there's just a lot more uh coming on on
this one so how many people know what
algo for GitHub
is quite a few so what we did with algo
for GitHub is to create uh all the
things that not all the things I think
we normally mention that we want to
provide 100% of the functionality needed
by 90% of the partners doesn't mean that
everybody needs to go there but we it it
that's just is a possibility right so we
add uh branching strategies continuous
integration continuous deployment
continuous delivery and a lot of other
things as a plug and play
solution so a managed solution that
people can use um and on top of that we
add all the GitHub
functionalities
so with that you'll have like one
solution where you get all the best
things from GitHub and all the best
things that are business Central
specific in go for GitHub and
then using settings and other
customization capabilities go for GitHub
you'll probably be able to handle the
majority of the needs that you have now
there are a lot of people on aset devops
and there's a lot of people that swear
to stay on AET devops and we think
that's absolutely fine as you'll be
seeing in this presentation we actually
also have a lot of stuff on Asha devop
still and we're not planning to move
everything to GitHub we're planning to
move the development piece on GitHub
because of the open sourcing but there's
a reason why some of the functionality
or some of the processes we have are
still on as your devops with that I'll
give the word to you
guys okay so before we dive into how we
ended up moving the system application
of business Foundation into GitHub I
want to give you a little bit of a
background a little bit of a
context so we started our move to Astro
apps I think back in 2016 so were pretty
relatively new users of as devops before
that we were using completely internal
systems in Microsoft we were on a source
control system called Source Depot which
is a system you know anybody know about
perforce this Old Source control version
system some of you yeah it's so
basically Microsoft bought the source
code to that like 20 years ago and
rewrote parts of it and created a new
source control system that all of the
different teams within Microsoft were
running on and then in terms of build
system and stuff we all also using stuff
that came out of the windows org
something that called Snap which meant
shiny new automation process not
entirely sure how shiny it was but back
in 2016 we started to move our things
over to asro devops and back in those
days we were a monor repo we had
everything for business enal in one
single repository since then we made
quite a bit of changes so today we have
about 90 active code repos repositories
in as devops only one of them contains
the actual application source code but
there are surrounding repositories that
contain you know functionality around
runtime compilers uh Engineering Systems
control plane data plane Services um
code we share between different
repositories and libraries and stuff we
we have on average 100 pull requests
created every day and modify about 500
files on a daily
basis uh we run approximately 700 builds
per day and when I when I talk about
builds I don't I I talk about bills in
in like generic terms not only building
the stuff but it's a lot more running
test cases and compiling databases and
uh building installers and like all
these things and we on average we run
about 30 million test cases every day in
in our DES in our actual devops
organization and do 70 full test
deployments to the cloud on a daily
basis so every day we deploy the full
business Central solution to the cloud
and run login tests Etc to see that
whatever Chang is going into different
branches is still capable of of running
and can be used by our team to test
things uh we have about 23 terabytes of
data in our nugat feeds and 220
something terabytes in our artifact
storage which is build outputs so so
this is just to give you a little bit of
a context of the size of the
organizations we have in inside asro
develops and the part we're looking at
to move into GitHub is the application
part so a bit more context on the
application so we have about 25 new pull
requests on a daily basis in the
application repository so that's code
that eventually you guys would be seeing
and on I don't know if you attended the
previous session on doing code reviews
um but one of the suggestions was to
keep your keep your pull request small
and I I checked uh our statistics on an
on average we have 13 files changed on
each P
request so if you think about a
repository that has million lines of
code has hundreds and hundreds of files
that change on a daily basis how do you
move that into GitHub well that is a
challenge that we're kind of facing so
what happens if you just kind of take a
snapshot of the code and move it out you
lose all of the history and if you Lo
lose all the history how do you blame
code and how do you figure out who made
what changes and why Etc and if you
decide to move the history which we did
not do with the system application how
do you filter out bad commits that
wasn't intended for the public to see
like perhaps some of these commits
contain some you know credentials or
something that shouldn't go into the
repo in the first place how do you make
sure you don't have any of those things
uh in in the code you're moving out to
get up that's a little bit of a
challenge for us to figure those things
out on average we do about 100 bu build
jobs per day I don't know if buddybuild
jobs is something can I say hands up who
has anybody heard about build
nobody well I'm not you know I'm not
surprised it's something we
invented so but Bild job is something as
a developer when you're working on your
private branch on your changes you can
take your branch and you can send it off
to the bill system you can tell the bill
system hey please go and verify that the
W1 version of builds and all the tests
on W1 passes or you can say hey test
everything just test all the countries
all the localizations or you can say
something like hey you I want to run run
this test case 100 times in parallel
across 100 machines to make sure that
it's stable enough to run so it's it's
essentially a system for providing a a
scaled scaled out build capability for
our different uh
engineers and we produce roughly 35
official bills per day out of the
application repositor and official build
is a special thing in our world because
it's a build that is fully signed fully
tested
um scann for all type of threats and
issues and it's something you can you
can potentially
ship okay so I have a question for you
guys and I'm not expecting anybody to
actually know the answer to this one but
is any if anybody's getting anywhere
close they'll get a
t-shirt so what do you think this number
represents and Freddy you can't you
can't really resp the number is
165 anybody who wants a t-shirt
tickets actually not not what I'm
thinking about but perhaps it's perhaps
that's not too far
away pardon issues issues well no
probably have more than that H
but but it still was it's a good good
attempt to get a t-shirt anyway
so 165
represents the amount of compute hours
we need to produce a single build so
that essentially means if you want to
verify a build locally on your
development environment you're going to
spend seven days waiting for that prompt
to
return I don't think a lot of people
would like to do
that uh another
question how many minutes do you think
it takes us to actually run one this
official bills we're talking about wall
time like if you schedule it at you know
noon when does it come back if it takes
165 computer hours to
run how many minutes you get a t-shirt
if you get any work
cloth did somebody say
eight I wish you know if we can make it
happen in 8 minutes my uh our
engineering teams would come and bring
us you know presents on a daily basis
30 oh we're not even close you you need
to go
up
pardon relatively close it's 140 minutes
so it's still a lot of time for
engineers to wait to get these things
where where was the person
who just come come down and pick it up
later okay so and the amount of tests we
run in each official build is 440,000
test cases which is obviously why it
takes us about you know 60 something
compute hours to get a build completed
and this includes running tests across
all of the different
localizations um upgrade testing
checking for Baseline uh issues
compatibility issues all sorts of
things and our bill graph is about 800
nodes so if you compare this to GitHub
every time you see one of these checks
these different steps you have in a
GitHub PR I think we have about 30 of
them in uh in BC apps today those would
be 800 if we were to move the current
bill system graph nodes we have in our
internal
system okay so that's a little bit of
context so Alex is now going to talk a
little bit about how we moved the system
application yes thank you Yas uh so
hopefully as you can see it's it's quite
a challenge to move these types of
things to GitHub and it takes a lot of
work uh but we've had a head start I
mean we've we've started a long time ago
um 2016 2017 I wasn't around at that
time but it's been a while and we have
quite a few repositories out there
already um I tried to create like an
overview a little bit but I probably
missed some um as you can see we have
the business Central application split
into three repositories and together it
actually consists pretty much of the
whole W1 uh business Central application
that we ship in Microsoft uh it's a base
app add-ons system application
Etc we have repositories out there for
devops Freddy has already talked about
algo as one of them container helper I'm
sure all of you are familiar with that
one as well arm templates
Etc uh we have sample repositories BC
Tech probably the most notable you can
see various Al Snippets and scenarios
that you can test out yourself and of
course documentation as
well um but in this this presentation
here we'll mainly Focus about how we
open source the business Central
application so we'll focus on on the
First Column here and we'll talk a bit
about how we did that using using
Alo so starting with alab extensions I
believe that was our first uh business
Central application open source
repository going back to 2018 uh it's
had a couple different apps on there but
nowadays it contains the add-ons so your
Shopify apps sustainability app
Etc then a little bit later uh a couple
years ago we introduced the business
Central apps repository which contains
the W1 uh base app now I mean I count
this one as open source I guess it's not
actually not open source because it's a
private repository but I think anyone in
this room we can we can give access to
we have a form that you just need to uh
to submit and then we'll give you access
um but we've kept it as a Private Pilot
because we're we're playing a little bit
around with how we can open source to
base application because it's quite a
big app um we'll talk more about the
system application but and how we've
open sourced that but the system
application is you know one or two% the
size of the Bas app so it's a lot of
work there are a lot of questions that
we still need to answer but um we have a
a private pilot out there where if you
are interested in making a contribution
to the base app or fixing a small bug or
something that's actually possible
today so little bit extending on what
Yona said we we came from this internal
repository that really had all of our a
code in just this one repository um so
that means millions of lines of code
thousands of tests uh it's a big
repository and um to kind of deal with
that scale we had to build up our own Uh
custom Bill system build in this shiny
new automation process yes
exactly uh so we have our own internal
Bild system that integrates towards aure
devops uh that can do building and
testing incremental bills Cod signing
help us release and hot fix and and do
test
deployments
um and we've built up over over many
many years so it's it's quite a big
challenge to kind of just take that and
either integrate it towards GitHub or
builds up something completely new on
GitHub and so for our first attempt at
going open source with the alab
extension repository and the business
Central apps repository we actually
didn't do that we just our approach
there was to basically just take a copy
of what we have in our internal
repository and put it out there for for
you guys to see and to make
contributions towards and file an issue
or whatever it is you can do
uh so every now and again we just take a
copy snapshot of what we have at that
point in time then you can see what it
is if you want to make a
contribution copy it on
back uh so obviously I mean it so it's
enabled us to go open source relatively
simply I mean not truly open source but
we can put the code out there you can
see it and contribute towards it and we
have taken a lot of contributions this
way um as I said aab extensions and
business Central apps they're still live
and you can make contributions um
today but of course I mean it has a lot
of downsides as well right like there's
all the manual labor with syncing back
and forth of course we have scripts to
help us do it but it's still something
we have to do on a on an ad hoc basis uh
but probably most importantly is this is
not really open source I mean you you
guys don't get to see what we're
building because we're building in our
internal
repository uh and we we we want you to
see what we're building and we want you
to comment on it if you have any
suggestions on what we can do better as
I said not in the spirit of Open
Source that's why we introduced BC apps
uh BC apps went live in 2023 uh at
directions uh nowadays it contains the
system application and the business
foundation and as I said the objective
here is really to have a truly open
source experience where we can
co-develop the business Central
application with with you guys you can
comment on rpr you can tell us why did
you do this or why did you do that
you're more than welcome to uh and you
can also make your own contributions if
you want from a like a whole new uh
feature to also just small bug fixes or
whatever it
is so I'll talk a little bit how we did
that um and going back to this picture
with our internal
repository uh we had the add-ons based
application and the system application
all in this monor repository what we did
about a year ago is we we move the
system applic
into the bcfs repository and out of the
internal
repository we made up the business
Foundation that came up uh since then
and then we've added the bcfs repository
as a subm module um in our internal
repository how many are familiar with
Git sub modules or using GitHub git sub
modules a few um so so basically it's
like it's a repository within a
repository um and this kind of allowed
us to get around a lot of the challenges
with you know we've built up so much
automation around building and testing
the system application and all the scale
that Jonas talked about right it allows
us to get around that because now you
know we can we can submit all the code
on on GitHub but we can still see all
the code in our as devop
repository so if you take a look at what
our Engineers are seeing in their vs
code they Ed to see a folder with the
system application and the business
Foundation they still see that it's just
I mean we've moved some things around a
little bit but it's not it hasn't been
Ultra breaking for our internal
Engineers they can still see all the
same code they can still basically
develop in the same way um all use all
of our internal scripting for setting up
Dev environments and requesting test
deployments and stuff like
that um and so our Engineers can see
this but so can our build system and
that means we can actually still we've
even though we've moved our code to
GitHub we still build and test uh the
system application in the same way in
our Uh custom build system that we have
internally and so even though the the
true source code the system application
that you guys can see in a 24 uh
business Central environment the code
for that lives on GitHub but we built it
in as devops uh so we haven't changed
anything
there the way it looks in in as devops
is we basically reference the way it
subm modules work is that you reference
a commit ID so at the this point in time
we're using you know this particular
commit ID from BC apps and then that
correlates to yeah specific commit in
the repository then we can just update
that on a nightly basis and when it's
time for shipping then we make sure that
we've uptaken the latest changes and
we've tested and so
on so what you see on BC apps now is is
actually what's running in production uh
so we have the 25 Z and 240 and above
230 and anything below that is is still
in ative UPS uh but going forward all
the new branches and stuff will be added
on on
GitHub so going back to this picture
this this is basically you know how the
our world looks now we've moved out of
this monor repo which it's gotten a tiny
bit smaller now because we moved the
system application but uh now that is is
truly on GitHub and in a in a in a truly
open- Source uh repository for the first
time
and that's where Al go GitHub comes into
play um so even though the the system
application that we ship is built in our
custom build system we still have a need
to build and test the system application
on GitHub because we need to validate
all the PLL requests we're getting and
so on and that's where we've chosen to
go with Al go for
GitHub uh if we compare our needs for
the two in both cases we need the
ability to build and test our apps we
need to validate with code cops and
breaking changes checks to make sure
we're not breaking any of your
code um and we need to do incremental
bills on poll requests as J has talked
about we have so many tests so we need
to be able to do build incrementally so
we don't have to build everything on
every po
request but we've kept all the
functionality for code signing and
releasing and hot fixing um and creating
test deployments for our Engineers we've
kept that internally and they can still
use the same processes as they did
before um
so I'll show you a bit how we did that
for the PCF repositor using
algo uh how many in here are using algo
today a couple how many have tried
it a couple as
well uh so so algo in algo you basically
set up these algo projects with with
settings and so the way the way we've
set up our build system is basically
through a bunch of projects with with
settings and I'll give a short little
demo of of how we did
that uh so it basically starts up here
in the GitHub
folder and we have a we have a global
settings file here with that that
applies to all of our different projects
on GitHub so for example you can see we
build on on Windows machines um we're
using this particular uh BC Insider
build uh to publish our app STS and so
on so there's there's a bunch of
different settings in here our repo
version is 25 because right now we're
building the 25 version of the system
application in the main branch uh and so
on there are many many settings here and
I don't want to I don't want to go
through them all but if we go back into
the root folder here under builds and
projects we've uh We've organized all of
our algo projects in this this folder
here so if we take a look for example
under the system
application and settings you can
basically see how we've configured using
algo we've configured our build system I
really with a I mean settings and a
couple of override scripts to because we
have some custom functionality that we
want to we want to get out of Alo but
there's a lot of it that's just
configured through through settings um
so if we go through it for example the I
guess the most important thing here is
we we need to give the app folder like
where where is the system application
stored uh then we tell it what build
modes to build it in um build modes
might be a little bit of concept we were
only using I'm not sure but uh if
basically it's like different flavors of
building the system application so we
always build it just in let's say
vanilla mode or vanilla flavor and then
for example we have translated which
means we build it with translations as
well uh Alo also allows for conditional
settings so you can see when we're in a
release Branch for example that means
branches we're shipping out of
essentially uh we have another mode here
called strict mode which yeah is a bit
stricter uh and it's something we
something we enable once we've opened up
for signup for example for 242 I think
we shipped last week so for example so
when we open up for signups there we
enable strict mode to make sure we don't
like ship some breaking change that's
going to break
everybody um so there's a bunch of
things here
um also just want to point out do not
run tests we do run tests uh we' just
organized it a little bit differently so
if we go back on your projects we just
have a different algo project for the
system application
tests and we just give the test test
folders and algo knows how to run the
tests so those are the algo projects but
if we take a look at how that kind of
becomes a a pipeline I've Tak an example
here where Alo runs a bunch of different
things but we can for example see build
system application in translator mode is
here and it runs the build using a
combination of algo and container
helper uh and then we have the system
application tests are running down here
takes a bit longer because we have to
spin up a container and a PC environment
to publish the app stores and run all
the tests uh but they are indeed running
in here in our pipelines and looks like
they're all
successful can go back here on the
summary and we scroll down to the bottom
we can then we get like a nice overview
of you know all the business Foundation
tests ran successfully and so
on so that's how we set up EO um in BC
apps and of course I mean all this is
open source so if you're curious about
how all this works you can just take a
look
um of course we also want to validate
our code with code cops and as as I
mentioned algo is just is a lot of
settings really so if we want to enable
code cops just add a setting enable code
cop um as for breaking changes checks uh
we might have a different little bit of
a different way maybe of doing that so
we've added a a custom like override
script that is called pre-compile app
and it just runs just before the apps
are compil we restore the baselines and
and then we can we can run our builds
with uh with breaking changes checks
enabled so we don't break
things and finally incremental bills
that's something we just get for free I
think I mean internally we had to to
develop that in our own custom build
system but with AO it's just it's
enabled automatically we get it for free
uh you can disable it for certain paths
if you want a certain path to trigger a
full build and so on so it's also
configurable but it's enabled
automatically so no work no work for us
there at least not on the BC app
side and of course I mean these are some
of the features we use but there's lots
of additional features that we could we
could start using if we wanted to I mean
right now we don't have any Power
Platform projects in in in BC apps but
there's Power Platform art integration
in algo uh we actually do use the
reference documentation with Al do
uh so Alo has this feature where we can
automatically generate reference
documentation and publish it to GitHub
pages so it's always updated on every on
every checkin to the main branch we just
it's automatically updates the our
documentation there's a bunch of
different features that we you basically
get for free if you're using if you're
using
AO okay shipping so I'm going to walk
you through the process of how we take
these change in GitHub um system
application business Foundation Etc and
how we eventually end up deploying those
on the SAS clusters it's a pretty
straightforward process in most cases
but it's still a little bit of
interesting to look at so of course
everything starts with a pool request in
baps re and this is the the
straightforward and simple thing this is
exactly what people expect it to be you
need approval from two different
reviewers and you need all of different
checks to pass and these checks can be
things like uh make Ure everything
builds the tests are passing power power
shell script analyzer is passing and
cred scan runs detect detecting that
there are no credentials in whatever
you're pushing or trying to get into
reper so once this is done the uh pquest
gets merged into the target branch and
then on a nightly basis we are moving
these changes from GitHub into our
internal repository like Alexander
mentioned and as we do that also like
you mentioned we re Buu everything the
entire code based from
source and run the full test Suite on
all of these changes that means that we
we verify that the combination of our
internal code and what the application
code that is out in GitHub will still
work together the way we expect it to do
and as part of this we'll also run a
full set of security
tools we'll talk a little bit more about
the different security tools we're
running later um and when when these
things are done we publish an new
official build and as part of that
official build we published build
metadata and the build metadata contains
things like which applications were
actually changed in this build uh
because once we we go to the release
processes we have I don't know how many
hundreds of applications we have but we
can't really ship everything every time
we only ship things that were actually
changed
so once we have the build we initiate
some test deployments making sure that
the the you the bill can be deployed and
the login test is running to make sure
you can actually hit that endpoint and
that the system is responding as
expected and then we create what is uh
yeah a release pipeline essentially and
this thing only happens if the
associated changes in this latest build
has any type of issues that we decide
should be fixed so ICM tickets LIF side
issues hot fixes Etc when developers
work on issues they tag the work item
with specific tags if this is something
that should be shipped and if it's an
ICM the system automatically tax it for
them so whenever they check in code
against an ICM ticket it will
automatically trigger a cheick a a uh a
shipping one question yes on the other
slide you said the official build yes
that is the one we published to artifact
for the partners to use right correct
yes you guys see this as part of we
publish it also to
artifacts uh okay so the release proc
process kind of starts with us uploading
the impacted applications to fame which
is this end point we have for delivering
hot fix it through the to the house
clusters and after that the the release
pipeline is
created and work items like ICM tickets
bugs Etc we update them we post a
tracking query to those so Engineers or
custom support Personnel ET they can go
and look at these pool request they can
find a work item and then they can see
how far in the roll out process this
actually happened because as we roll out
things in Microsoft we have this thing
called safe deployment practices which
we are required to follow which in
essence boils down to Rolling things out
slowly with bake time if we if we were
to roll out a bad fix globally overnight
we'd break everybody so we start small
and we we kind of grow over time we
always deploy outside of office hours at
least that's the intention
um customers can configure when they
have office hours
and I think they do that in attendant
admin Center and then we use that to
determine when we can actually go on out
fix uh the Clusters they're running
on uh safe deployment practices have a
little bit of different uh Behavior
depending on what type of things we're
shipping so if we're shipping new
features which typically would be an
upgrade 242 Etc then we upgrade
customers progressively over three weeks
like there's a 3 week Delay from
starting the upgrade process until we're
done
and do we I don't know do we have
anybody from Finland
here okay good because Finland is the
country we start
in so that that's a little bit like our
Canary at the moment that's where we
start and we we the reason we start in
Finland is because it's also in the same
time zone as us so we can we can be
attentive if something happens we can do
something about it because we have
people working those
hours uh hot fixes though they typically
roll out throughout a week because there
are usually issues that needs to be
fixed slightly quicker than just three
weeks but one week is the minimum amount
of time we're allowed to roll things out
of within Microsoft we can't go any
faster unless we get VP approval which
we often don't even a
try so our pipelines they have automated
retries any time anything fails to apply
hot fixes upgrades whatever we will try
again later automatically so we don't
have to monitor those things manually
and we also have a lot of monitors and
alerts for engineering team so if if we
start seeing a trend in you know login
errors or you know whatever uh we get
alerted and the engineering team and
livite team can pause the all of the
upgrades and and rollouts going on at
the
moment
okay that's that about um deployments
we are going to move into talking about
the supply chain how many of you had
have heard about the recent uh XC lib
vulnerability that almost hit most major
Linux distributions three or four weeks
ago yeah so that That's a classic
example of a supply chain attack where
some maintainers somebody imposing as
being maintainer managed to sneak
vulnerable code into some of the
packages that other packages depend upon
and then you know eventually if this
actually was rolled out live that had a
back door into many different many
different popular Linux distributions
um so how do we secure the uh supply
chain well there are different kind of
layers and to this onion so starting at
the simple side of things in GitHub in
terms of code how do we keep the code
secure well in terms of permissions we
make sure that on all of our
repositories we have no precis
administrators like we and all of these
different processes and entities we have
we always operate with least
privilege and on the source level
whenever you commit or submit code we
always run this credit scan tool which I
think is available for everybody uh
making sure that none of your commits
contains any credentials password
certificates you know whatever um we
also have something called code Q which
is a static code analysis tool which we
run on all of our code internally and
also in GitHub
and this is probably the best security
tool I've seen so far in the market it
has a we have a fix rate of over 50% so
over 50% of all of the issues found by
code ql ends up being a real issue like
the way code is passed through the call
stack Etc could lead to a
vulnerability then we have a tool called
dependabot which will go and
automatically update depend when we have
uh vulnerable dependencies out there
that needs to be updated and we require
multiple approvers on each of the
different tool requests going in
so on act devop side though we add a
little bit on things on top of this
because we had to build with the scale
of the amount of repositories we have
and things we had to build additional
automation so the first thing we do is
that we deny create Branch permissions
so if you're a normal engineer actually
of us we can't go and create release
branches or anything like that because
release branches if anybody can create
those they can also potentially
shape uh so we we make sure that happens
through automation only and given that
you have 90 repositories with hundreds
of branches and entities and releases
and whatever in Asal develops how do you
keep track of all of the permissions and
all these different uh entities we have
well so we have a baselining system
where we generate Baseline for all the
permissions and store them in repository
and compare it on a daily basis and if
it's modified we go and create bugs uh
to verify that if any engineer by
mistake should go and create a new
branch and assign themsel you know
contributor rights or admin right so
that Branch will get
notified so but sometimes you do have to
make
changes to the systems and then to be
able to get that elevated permissions to
be able to do that we used this Asher
pin privilege identity management system
in Asher
uh okay so the more interesting part in
my opinion is how do we keep the builds
secure okay so I talked about official
builds and official bills like I
mentioned are bills that we are uh
shipping so our official bills have
Branch protection which means the bills
are only allowed to run if they come out
of certain branches so if you have a
private Branch if you create a private
Branch when you all know private code
whatever that code may be you can't run
official bills on them uh it has to be
on official branches like release Branch
as a master ET Etc then we have this
component governance system in asro
devops that will detect that you're
using a vulnerable version of you know
Astro Identity or some component and it
will go and a automatically detect and
update those versions and and get them
updated for us and then we run a set of
other tools to make sure that there's
nothing bad going on inside of the uh
the binaries
releases
um we require approval for every release
from an alternative identity so in
Microsoft we have multiple different
identities we all have corpet identities
like the normal email addresses you'll
find like Freddy K at Microsoft thank
you yeah for instance but none of our
corpnet accounts can be used to approve
any type of releases so we need we have
separate accounts and separate computers
we use for proving releases so if our
corporate accounts would get compromised
we still can't release
anything and the same thing Branch
protection also applies here so we can
only run releases out of predefined
branches no private branches can be used
uh for releasing
code feed
security so this is an interesting one
so if you think about the uh issues uh
with this XC lib as well as uh the solar
winds that happened a couple of years
ago
where people they change a downstream
component and they you know manage to
inject a little bit of bad code into it
and then these things get in get into to
the builds and the system becomes
vulnerable so one one way we've kind of
dealt with this that the official builds
they only get to use inputs from a feed
that is locked down so if any other type
of build or private branches Etc needs
to produce something for private testing
they they need to go into a specific
feed and not into the official feed
because if they were able to ship to the
official feed they would be able to
inject something into the builds and
that that would be that would be
bad so how do we fix vulnerabilities in
BC apps so the problem here is obviously
if we start fixing code in a public G
repository then attackers can can see
what's going on and they'll be able to
figure out that we're working on fixing
some vulnerabilities and they might be
able to to compromise part of the
systems because they know what's
vulnerable so so the way this works at
our end is that we have a setup where we
have a mirror repository of BC apps so
we have a daily we have a daily we copy
the repository over internally and we
have the full development support in
that internal repository so when we have
to if we have to make security fixes in
BC apps we can do those internally and
we can make sure they they are shipped
and tested and deployed before we
publish them on GitHub and other people
are you know can see what's going on
here Freddy with that I'm going to talk
a little bit about release management
even though I'm not the relase manager
of uh of business Central but mostly
focused on how open
sourcing uh changes our approach to
these things or will do if we have a
look at a
business Central Cycle it's in six month
right we we have a major in on April 1st
and we have another major on October
first and what are we doing in this time
frame how are we working and and and by
doing that I've taken some of this year
so looking at what we shipped on April
1st this year was was
24.0 and a lot of things were happening
in in in the branch in our main branch
where we were working on on the version
that we're going to ship uh but
obviously like we don't work until this
version and then okay now we ship this
version and now we start thinking about
what are we going to do for the next
version right because then before we
would find out then kind of we would be
almost in October again so stuff happens
while we're in the end game of One
release stuff like outlining the goals
for the next release planning spiking
scoping figuring out out what's smart
what can we do what not looking a little
closer on these
things what goes into the next wave of
business
Central Business Central our business
Central service that we're running in
the cloud we see that as a world-class
service it's scalable supportable
reliable and secure and it needs to stay
like
that if any of those parameters goes
away if it's not secure if it's not
reliable then it doesn't matter what we
put into the next
release this is what people expect this
is what people needs to be able to count
on so whatever we need to like
continuously do to make our service stay
a worldclass service goes into the next
wave uh and we continually have that as
we have like there's a musthaves like
regulatory features and whatever that
also we have to follow regulations um
there's also a a bucket of stuff that we
were maybe working on that didn't really
make it until uh
424 that doesn't automatically get
approved for for 25 but we will relook
at that and say is it still important or
I mean has time shifted so fast that it
really doesn't matter anymore after that
strategic in initiatives right now ai
co-pilot all of these things is like we
need to stay in front of the competitors
when it comes to AI initiatives and and
and co-pilot we need to to to ship the
features that our customers expect uh
and and want to
use scaling our partners you guys making
sure that you are as productive as
possible like not spending time on
stupid things uh that that you could uh
that that you could avoid um is an
important one and then last but not
least partner suggestions ideas coming
in through akms BC ideas or GitHub
issues uh now this one is really the one
where that's the one where we could get
contributions as well right because now
we have ideas and and and we need to
figure out can we fit this in the plan
and and all of this that comes out of
course becomes slices work items and all
of that and becomes part of our plan
where we then start working on that
actually already a month before we Shi
the prior version our main bran now
becomes 25 and then we start working on
all of these uh these
features looking
at our Sprints we'll like do Dev and
test and then backport some of the
functionality to 24.1 uh and and ship
that that would be fixes that could be
small features and we're going to do
this a number of times so we run out of
numbers and we'll be shipping
25.0 what goes into Devon test what is
that that is spiking grooming
development code review testing
documentation partner validation Buck
fixing a lot of stuff goes into the
bucket that here just says Dev
test and if we talk about open sourcing
C development Community
contributions what can what can we
actually help each other with here and I
think everything like we can we can
co-develop entire features like starting
at BC ideas or small buck fixes starting
on GitHub issues or actually if we have
open sourced everything you could even
imagine that that people who have an
area of expertise or interest would
comment on code reviews and and help us
make sure that the fixes we do actually
are the best fixes in that area like you
could follow work in progress in these
areas and you can participate in code
review in that so Alexander you have a
small demo here I think yes so another
advantage of going open source is also
we get a not like a whole other way of
also showing what goes into every
release so you switch the slides perfect
so three days ago for example when we
shipped 24 to2 we create this release on
GitHub and I mean you've you've been
able to see the release notes before but
here you get another view of of the
release notes and you can even click in
to see the different pull request like
what went into this
change uh and you can read all about
like what went into the 242 release um
if you want to dig even deeper you can
go see the full change log of what went
in uh that what what we basically what
we've changed between 241 and 242 uh so
being on GitHub just gives us like yet
another option to be transparent with
with the the the whole community and and
show you know what goes into every minor
and what goes into every
major uh so these are obviously things
that we've already shipped but we also
give you the capability of seeing what
we're building now of course you can go
under polar Crest and look there uh but
if you go into milestones for example
you can see for 243 which should ship
basically a month from now you can see
we're already busy building the next
things for for
24.3 uh so if these things emerge then
seems like we're going to get some
multifile upload and and so on so these
are some of the things we're working on
now for the next release and you know if
you know something about this area
please you know have a look at the code
and leave a review if you want um so
being on GitHub and being at open source
just gives us for like a whole new set
of opportunities to be transparent with
the with the business Central Community
uh in the BCF
repo okay so what's next in term of
terms of open sourcing the business
Central application codebase so before
we look into that just briefly we
already today have quite a lot of
contributions from you guys from the
community in our public repositories so
BC apps went live like eight months ago
or something we already have 67
contributions from you guys and for AAP
extensions which been out there for a
little bit longer we have almost 300
pull requests completed through the help
from the
community in uh in in the private
repository business Central apps which
is where we have a copy of
this base application which Alexander
talked about before in a small pilot
limited amount of users we still have
over 200 pool requests completed by by
the community and helping out obviously
we want more of that so where we want to
go is like first of all where where do
we want to end up with this thing so the
end goal for us within the team is is to
have the entire
business application the entire business
Central application part co-developed
with the community with you guys over at
GitHub so how do we get there well first
of all we need to take this Private
Pilot that we have at the moment then we
we need to kind of kill that one and go
true open source story similar to what
we did with BC apps we need to get the
code out there you need to be able to
contribute Etc and we need to be able to
deal with the uh all of the different
changes coming in from you guys because
you know not only fixing all of the
technical issues that we talked about
previously and the scale of things and
all these things how do we you know run
all these test cases the technical side
of things right but but also how do we
deal with things that we have internally
with localizations today in the base
application we don't really know how to
fix these things yet so there's a little
bit of work we have on our side of
things and even after we fixed all these
technicalities we also have issues with
uh process related things so there are
technicalities with the scale of things
uh localizations and stabilities and and
and so forth but even if we get those
things fixed how do we deal with the
challenge around like the amount of
contributions we're going to get from
the community and making sure that we
don't end up being a bottleneck for
reviewing code and getting things
through the
system so and as part of that how do we
make sure that the uh the PM groups we
have the PMS we have the group managers
we have can keep track of all of the
incoming ideas and flows and you know
changes from you guys and steer the
product in the right direction and deal
with all of these uh ideas and I'm
hopefully we'll be back next year with
some a little bit of uh answers these
questions so we're going to talk a
little bit about
so the future for Alo
yeah so we just heard about where we
want to go with open sourcing the
business
application and as Alexander showed you
we're open sourcing the business
application on algo and I think it's
it's it's clear to everyone that algo is
uh I think it's fair to say that many
people might think that it's a Freddy
project it is actually a Microsoft
Project and it's owned by the team that
is standing here together with the other
five people that are sitting at home
making sure that all the other things
you saw here was is still running um so
algo is actually under the same
restrictions as everything else here we
need two code reviewers for every single
pull request and we need like to make
sure that we have everything in place um
we are not like totally yet there yet
with all the the project management
pieces and stuff like that we're going
to we're going to get there and that's
part of what's next for
it'll go for GitHub first of all we need
to finish what we started right now we
just shipped a few days ago the Power
Platform support that has been underways
for quite some time but in version 5.2
of Al go for GitHub we have that as
Alexander told you we don't use that in
BC apps but it's something that Partners
could use to make sure that if they have
Power Platform Solutions like
integrating two business Central apps
then it actually works like deploying
can deploy both things it will deploy
the business Central application first
to an environment change the URLs in the
in in the Power Platform solution and
then deploy that so you get a working uh
environments in both
areas in the next version we're working
on the bcpt test report we have been
able to run bcpt tests for quite some
while uh the only output was a file with
the results that you had to like look
into and figure out
are these numbers better than they were
last time now with the bcbt test report
you can actually uh check in a a
Baseline and then we will test the uh
the results of the bcpt against that
Baseline and you can set up uh allowed
thresholds and stuff like that to make
sure that you want to break the build if
you you the number of SQL statements
executed by your test exceeds the prior
version or 10% over the prior version or
whatever uh we let support for Federated
credentials and managed identities how
many knows what Federated credentials
is very few I learned it last week um
and and I learned it because if you
think about in the old days we had
username and password right if those
were stolen then anybody could like do
everything you could do now we've done a
lot of security stuff after that and
today most people use client ID client
secret for for using an app registration
to be able to to maybe deploy uh apps to
business Central or or do other things
and obviously it is kind of like a user
and and through that user you could do
these these these these
things but it's still like if if if
those gets compromised then somebody
could no matter where they are utilize
that Federated credentials is where you
set up on that app registration that
only a GitHub
repository with this name and in this
Branch
can uh connect or can use this app
registration to connect to business
Central that means that that you can go
all the way down to the branch and say I
can only publish to business Central
from that branch in this repository and
then I don't need any secrets because
it's just
the uh delivery method or the deployment
method in that repository that will that
will have that ability so removal of
Secrets totally when we add stuff like
that and that can be taken uptaken by by
you guys as well we're going to update
the Telemetry module to give us some
more uh some more information that we
can use for future development as well
work in progress net I don't know how
many saw the session yesterday but all
of the things that you saw yesterday
will be something that we're working on
over the summer here so that we'll be
able to to uh to publish our our apps on
a few new get feeds and those will be
directly uptaken by Al go for
get um yeah we also working on the
indirect Alo template I don't know if
that's ever going to ship but it's
definitely something we're working on uh
to see if we can get if it's smart
enough to ship so the nou get support
we'll publish all our symbols for all
our apps and all our symbols to two n
get feeds and we will publish all Sy
symbols for all appsource apps to a
third net feed and algo will
automatically trust these feeds beside
that you'll be able to trust uh other
feeds as
well GitHub packages is supported for
internal dependency resolution uh if you
want to set up external dependency
resolution you would set up trusted
feeds in your algo repository and that
that works
automatically uh you can set up a secret
for automatic delivery to
run uh to to to nuget and we were
working on also delivering runtime
packages to nuget so that you can
provide other partners with access to
your uh runtime package through
that we've been working on build
performance for quite some time right
now we can build on Linux uh without
running the tests there it's very very
fast but then we kind of need to figure
out a way to run tests in a performant
way um we're working on yeah making
artifact downloads faster being faster
to find them and spin up containers as
well in the end we we also looking at
whether we can split build and test so
that test is happening in one place or
maybe using uh hosted containers or
something like that so we don't have to
wait for the containers to spin
up all of this is also obviously um
included in the search for for being
able to run the 10 million tests a day
or whatever what was the number I can't
remember 30 oh sorry about that um page
scripting tests you've seen that a few
times we want to be able to record a
page scripting uh yaml file and just
take that yaml file and check it into
your repository and then we'll
automatically run these uh these page
scripting tests what we need to do there
is we need to publish a uh npm module
and then create the functionality for
that code coverage also something we've
been working on for quite some time uh
but yeah I think we're going to make it
in this release so that we'll be able to
publish code coverage and there are
tools in GitHub to show that in a UI or
even show that in vs code where you
missing coverage and where you have
coverage and then there's a lot of
things in GitHub that we just get for
free like GitHub evolves like constantly
and we get all of these things for free
but there are also things that we might
need to add code for stuff like the
feder credentials that I talked about
Works spaces code spaces some of these
things are also something that we uh
probably need to to do some coding in
order for that to
work we're going to improve our algo for
GitHub release management our road map
is not like totally up to dat and our
issues management our templates and all
these things we need to to work on those
to make sure that we follow the same
processes as we have everywhere else and
also be able to discuss ideas and uh
co-develop Alo for GitHub as well as the
other
projects last slide for
me algo will move away from BC container
elow but what what does that mean so
it's going to happen over the next X
releases
and so there are many reasons for this
BC container helber is really a huge
pile of very cool functionality made by
one person over a number of
years
um we can do multiple things here right
we can allocate five resources in in our
Dev team to uh to try to like make sure
that a lot of more people than one guy I
mean I saw Tina Tina's uh presentation
on code reviews and he said that uh
there was this the fear of if somebody
wins wins in the lottery what do we do
and and this is a problem right and and
what we want to do is not yeah to
allocate five resources to like dig into
container hel figure out how things
works and so everybody can can maintain
it but what we want to do is we want to
take devops relevant
features from container hel and
Implement
those in a Microsoft
shipped Powershell module that is
supported by Microsoft some of the
things might be in GitHub actions but
all of things that will run locally will
probably be in Powershell modules and
then over time algo will start moving
over using these new Powershell modules
instead of container helber so over time
the evolvement of container helber will
be less and the other modules will start
getting the functionality that we need
in algo and that other people can e as
well and back to my disclaimer in the
beginning where I said that people using
a managed devop solution and in managed
devop Solutions I count Al Ops alpaka
and Al go for GitHub might not notice
this change at all because Waldo is
going to make sure that Al Ops just
works even this even when this
happens but people who are using a
self-made devop solution that uses
container hel and maybe even uses some
of these like hacks and stuff like that
is in container container heler might
see themselves with a lot of work to do
right so this is the reason why should
really consider whether you want to stay
on a self-made devop
solution because you have work to do if
you do
that and once this is done we wish you
good luck on winning a the lottery once
this is done he's going to fire me
oh he's not no I'm kidding then I can do
something new and exciting right it's
good it's good for everybody
so final thoughts we're almost at the
end thank you for sticking with us a few
final thoughts to leave you with before
we go into the
Q&A as we said we'll continue to invest
in Ash devops and a go for GitHub we
have still have many many repos and as
devops and I don't know I don't see us
going away from as devops anytime soon
but we are investing in GitHub and we
are investing in Al go for GitHub and
will'll continue to uptake all these new
exciting features like the
BC uh yeah what's it called PC Replay
flamework that was an internal name
wasn't it page scripting page scripting
that was the name so we'll continue to
invest in these things and uptaking
these things into a go BC apps is out
there is our first truly open source
application
repository more is coming to this
repository uh for now you have the
system application you have the business
Foundation if you go to a k. msbc apps
you can take a look you can contribute
you can give us a
comment uh yeah let us know what you
think if you want to contribute uh I did
a launch event session for the latest
launch event uh you can find it on BC
YouTube has this title here um so it'll
introduce you a little bit to how you
can get started with contributing to
this repository um and get a little bit
under the hood of what's what's going on
in the builds and so on
and with
that with that we have 17 minutes for
questions I think up here I don't know
if I can throw that line should we
try oh
sorry got it thank you uh thank you for
these insights I have a question uh in
the beginning of the presentation code
spaces was mentioned Yeah you mentioned
code spaces and that you were able to
connect other containers to it but is it
possible to connect a business Central
container to it because I wasn't able to
yeah so no Cod spaces are running Linux
containers only so today we cannot I
mean you cannot spin a Windows container
up inside a Linux
container the only thing you can do is
from within this Cod spaces uh container
you can connect to a an alpaka container
which is a cloud container an Asher
container instance which is also a cloud
container or an online sandbox okay the
the way to do that you have to do
manually right now it's not
um it's not done like automatically as
part of Alo yet but it's one of the
things that we're looking at how we can
automate that process to like just go
into a repository say we want to create
my edit this in code spaces and then be
able to download the symbols from net
compile stuff publish to a container
somewhere and and run it thank you
have to Friday
afternoon so um because we talk about
the containers and how we can um switch
to a new
um uh structure of that I wonder how you
guys uh build your development
environment is it locally with the BC
container helper or do you make a
Sandbox and test all your new uh May new
changes in in the and the cloud yeah so
so it's really a combination of things
but no we do not run the uh B container
helper locally so typically what they'll
do is that they'll have a uh a copy of
the codebase locally and they will
download the latest builds the outputs
from latest builds from the build system
and they'll do incremental builds
locally in their local computer and test
locally and they can use these test jobs
and send them off for validation or
deployment like a little bit what I
talked about in the
beginning okay thank
you other questions
oh there's one in the middle
there uh when you are doing the releases
of a new version and we start getting
the messages we are temporally
postponing what should we imagine is
happening on the
background probably us detecting issues
and not wanting to push those versions
with issues onto
you well of course there are still
issues guess that's the reason for the
three week staged deployment that we
start out with the Finland and then uh
if the Finnish people are not crying
then we'll
continue yeah that's a
joke other questions
else I think
we'll call it a session and say thanks
for joining us and uh have a good
closing session
