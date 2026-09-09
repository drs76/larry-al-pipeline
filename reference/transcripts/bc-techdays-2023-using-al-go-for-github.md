# BC TechDays 2023 - Using AL-Go for GitHub

- **Source:** https://www.youtube.com/watch?v=LCA2rTOpygU
- **Video ID:** LCA2rTOpygU
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 44m50s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

thank you and welcome to this session
about using algo for GitHub
this is a 90-minute session split into
the other half is about introducing
flexible powerapps solutions for
business Central and they'll also be
using a little bit of Al go in that
session so that's the reason why these
sessions are combined and that's the
reason why we are starting
my name is Freddie Christians and I'm a
technical evangelist with Microsoft
coming out of Copenhagen and I think
I've been here at Tech days every single
year since we started
so it's a big pleasure to be here and
together with me I have
hi my name is Christoph I'm not working
for Microsoft but Freddie invited me to
show you also how I'm using Al go you
can call me KB or Chris it's much easier
than Christoph and I'm from Poland
thank you and thank you for joining me
here Christoph
it kind of it's always good to have
people in states that actually use the
product and so this presentation is
probably going to be one of the least
technical presentations I've ever done
and then it's on Tech days
uh the reason for that is that I've
gotten some feedback that whenever I do
like these very deep Dives on algo I
only gotta touch the surface of some
areas and it'll go and really
people won't get the entire picture this
presentation is about using like
day-to-day scenarios what are we
actually uh how are we working with algo
for GitHub and then in the end of our
section here we'll go into a little more
advanced areas where we also are talking
about like
how you actually can can modify the
settings in it'll go to do something
that is
vastly more advanced than than what
you're going to see in the first
presentation
but with that we've kind of split the
agenda into a number of areas that we'll
try to get through
see if you make it but save time getting
started is all about yeah how we get
started improve collaboration fix box
and so on and so forth let's just go
into those things
same time getting started how do you get
started with
devops how do you get started with Al go
for GitHub
Christoph will do a demo in a short
while but really
if we look back we've had like the
Hands-On lab and we've had like various
templates on Azure Dev apps and on
GitHub on how to
get started and how to to use things and
I'd say today that people saying they're
too busy to set up devops it's like
bootcard are saying they're too busy to
sharpen their saw so this
setting up devops using devops is
something that is going to save you time
in Italy there is a learning curve
going back to how we did things in the
Hands-On lab there is a big maintenance
cost in that as well but using algo for
GitHub
is is really
extremely easy to get started and and
maintenance is almost zero and the
people I'm talking about are talking to
using Al go for GitHub says that the the
mo the best thing about this is that
they don't need to modify yaml files
they don't need to like mangle with
Powershell scripts and all of these
things anymore they just use a tool now
and the goal is that algo for GitHub
will support 100 of the functionality
needed by 90 of the partners well
doesn't need that mean that 90 of the
partners needs to go to this there are
options on
Azure devops as well Cosmo alpaca and
alops being some of those
which are also excellent Solutions and
if you are on Azure devops we would
recommend you to look at these two
solutions
um
the reasons for GitHub well
I don't know how many times you've heard
the word GitHub at Tech days this year
in the keynote Al go for GitHub was even
mentioned a million times
but GitHub like every single session
everything is about GitHub GitHub GitHub
and so on and so forth and there's so
much happening on GitHub like so many
Innovations coming every single week
There's a something being released on
GitHub that we can take advantage of and
and we'll try to do that and we'll try
to pick up on all of these things and a
lot of these things will just work out
of the box we don't need to do anything
because we have a tool that works in
GitHub with that let's do the first demo
and Kristoff
where I start with
lgo on Google I never never remember the
AKA dot Ms probably there is some but
where I'm starting is just just going to
algo for GitHub and to the Repository
uh if you will go a little scroll down
you will see two repositories one is for
ptes and so pertinent extensions and the
second one is for appsource they are
different because the apps development
is also different so let's go today and
go to pte
oh you can see this is the uh this is
the template which you can use so let me
just
go to my repository and let's create a
new one
and I will just choose that template
you can also do it from the from the
repository yesterday with Jasper we were
showing the app for the system system
example system up example so let's
create one
this
okay I can make that this repository is
public or private and in my case I will
do it private because most of the work
which we are doing is also private but
this one later I will change so you will
be able to have access to it so I will
make it private
foreign
and as you can see it's generating me
the repository already with some of the
code and with some actions so you can
see also the initial commit is already
running so I didn't do almost anything
and my pipeline was already run you can
see that I have also a lot of actions
which we'll be talking later one of this
action is that you can create a new app
just give the range and it will be added
to your repository however I will do it
little different this time I will just
copy paste my files
so let me only
drag and drop this one
you can see that automatically my app
which I had already prepared is going to
the repository I can only choose if I
would like to have it as a new Branch or
I will just commit it directly
typically I am creating a new branch in
this case we will just commit to the
main branch
thank you
all right you also can see that now
after the upload my pipeline also was
was triggered and now my app is building
and and checking if everything is okay
with that we will come back to it later
because it will just take some time
however I would like to cooperate with
Freddie and that Freddy will do
something that later I can check his
code so let me go to the collaborations
and probably I will need to use my phone
for that because as always some
notifications here going where we have
it yes let's type that
okay and let's add people ready
DK DK
yes I think it's you fine
looks like it okay so you have been
invited and that's all what I needed to
give access I also would like to say
that I'm on my I have a lot of my own
customers and I really need to start
very quickly with the apps which I'm
doing for them but I don't want to
delete everything from the visual studio
code so this is how simply is set for me
a new customer and give them also access
to the code
pretty much very cool thank you
and
I think that's the wrong one but three I
think that's right yep so
um as you saw like just getting from a
template and getting started very
quickly and what Kristoff did was just
to take one app and copy that into the
algo Repository
the way GitHub is organized is that you
have an uh one or more organizations
that you're a member of then you have in
every organization there can be a number
of algo repositories and in every algo
repository there can be a number of algo
projects and in every algo project there
can be a number of apps test apps pcbt
apps and so on and so forth
the repository is really the release
vehicle whenever you release something
it's on a repository level the algo
project is what you install together
that's what your would be your Italian
version or your Danish version uh or
like like some apps but but they are
released together in in one repository
so this is the way that you kind of
think of
of the split between things in
christoph's example it was extremely
easy because there was one project in
one repository in his organization where
he invited me as a collaborator
let's talk about collaboration then
the way that Al go for GitHub then
implements stuff like branching is
kind of
I'd say new because for people who've
used the Hands-On lab and have been like
developing their own scripts and and
workflows and all of these things
branching has not even been in the in in
the Hands-On Lab at all so so thinking
about
how do we enforce branches how do we
figure out what a what release branches
used as the as the previous version and
all of these things is something that is
built into GitHub so if you use the
branching strategy that we suggest
then you automatically will
will have a setup where you can hot fix
earlier versions and where you will get
advantage of of using the previously
released version as the previous version
to your current build so that you don't
break it and all of these things just
happens out of the box so
no need for any coding there as well
let's just have a look at how this
branching is suggested and what we
recommend and this is actually pretty
similar to how we work in Microsoft in
our development we'll always have a
stable main branch which branch out to a
feature work on that this can be a brain
so it can be a fork Forks are more
secure and I'll show that in a second
whenever we pray we like create a pull
request into the main branch builds test
runs and code reviews are mandatory
you can set them as mandatory but you
can also allow repositories to not have
these things as mandatory but we suggest
they are mandatory
then we Branch out to another feature
and we create a release out of the main
Brands and as soon as we create a
release we update the version number in
the main branch the reason for this is
that we don't want to have conflicting
version numbers in these two branches
and we always know that any build from
the main branch is newer than the build
from the release Branch we'll be working
in our feature B
branching out to another feature C
and at some point in time creating a
pull request into the main branch from
feature B now here algo figures out that
there is a release called 1.0 and main
needs to be compatible with that so it
uses the
previously released bits as the previous
build
so upgrade tests will be running and
test runs and all of these things and of
course code will use again before you
can upgrade to that now if you create a
hotfix here that is actually fully
supported by checking in or creating a
pull request or taking a
a cherry pick other things into the
release branch and then you can release
that one
if you then later merge in something
from feature C it will use the hotfix
as the previous build
and again if you create another release
then you need to update the version
number in the main branch and that
happens automatically as part of the
update uh create release workflow in in
algo for GitHub then you also have
another release brand and now you can
kind of see that you can be developing
and it finds out that this is the latest
release and you can create another
hotfix and another hotfix and all of
these things are built in
automatically enable go for GitHub so
that uh that that you will have this
setup working you don't have to code
that yourself
let's do a small demo of me actually
looking at
Kristoff's repository if I can find that
this would be me
and looking at my
let me just refresh this one
I should probably have a
should not have like an invite from you
maybe that is
here
unread notifications
busy for subscribe so this is the one
except invitation
and I I now have like access to this one
so I could clone this one and create a
branch if I have right access to this
one but I can also create a fork of this
in my own
uh Freddy DK up here in my own
repository create Fork here
and now start working on on this one I
could create code spaces if I that was
working it isn't so I'll go into this
one
and just make not in the permission set
no
let's go here
in the system application
examples
or do you want me to change Christopher
I will reject it so don't worry
what are you talking about
okay well see I need of course to start
editing here
and say what
reject
so I could well what I do with this one
I if I create a pull request here then
I'll create a pull request on my my own
I can also create a pull request to
watch Kristoff but here I'll commit
directly to my own branch which is my
Freddy VK branch oh Fred DK fork and now
I'm one commit ahead of bc4 for all uh a
main here and I'll contribute that and
create a pull request
on Kristoff's Repository
to see how that works now having a fork
I can also run the all the actions and
everything on my Fork if I wanted to so
I can ensure that everything works
before giving the word over to Christoph
which you probably know that it will not
work
because you just put some without
comment
so what is happening now when Freddie
did the pull request first of all the
build is going and so we will know if he
didn't make a breaking changes and all
mistakes in just changing something in
the in the repository I hope you will
test it before but what I can do and
this is which I encourage you in all
your organizations whatever you are
using use the code reviews also invite
your Junior developers also to the code
reviews that they will also be able to
add some comments to that but also
thanks to that they will also learn how
the code is done I also doing
development for many years and I'm
learning something from even Juniors or
seniors which are doing and I'm asking
why for example they did the code this
way not other way and then we have a
discussion right so what I can do I can
always add the comments and uh
why you uh
drag the code
so I can just start review and I can
just add as many comments as I like as I
want and later I can just finish the
review and say I require request the
changes so I will not approve this one
of course in normal life I would approve
my developers code if it would be if it
would be good and we always have that
process so we mostly never do the uh
pull or pushes to the main we even have
blocked so only people can create a
repository the the branch and then do
the pull requests
so submit review
and by the way the fun thing is also
that I get an email you cannot see it
but I'm getting email faster than
someone it even will write to me that I
need to do some a code review and yes
maybe I shouldn't but sometimes I'm not
next to the computer and I really want
to push something fast and check it I
also can use the mobile app for that and
do it from phone so that's really cool
all right Freddie I I will not approve
it right I could change it also which
can I show it I think we need to move on
yeah okay then yeah you can you can
actually modify yes if you want to
sometimes it's happening that I also
modify the code because someone make a
mistake and uh spelling so instead of
sending it to the developer one more
time I'm just fixing it to complete
faster with the processor
so this process is like uh fully
automated by algo for GitHub you don't
need to do anything all of the code
reviews and all of the other things
and also if you have test apps installed
they will be merged as well let's talk
about
bug fixing and if you want to fix a bug
and actually bring that back to one of
the earlier releases and how can you do
stuff like that
um the branching strategy again like
let's just have a quick look at what we
talked about earlier where we have a
release we have another feature here and
when we when we create that feature let
me see here we find the park we fix this
park and then we want to cherry pick
that fix into the earlier releases
because we found out that that the guys
running on version 1.0 and and 2.0
really can't live with this so how is
this supported by by hail go for GitHub
we actually have nothing in it'll go for
GitHub for this specific what we have is
we have the branching strategy and all
of these things so you can move things
into the branches and we'll build and we
can release our fixes and all of those
things automatically but they're cherry
picking
we leave that to GitHub tools and
um instead of actually fixing bugs and
other things I'll just go directly to a
sample that I have what I use for this
is GitHub desktop it's one of the tools
that have been out there for quite some
time now where you clone things and you
have things on your repo here and let me
this is just a repository called repo
one where I have some check-ins here
actually Dimitri created this one on
April
um
with a small change this is in the main
branch and I can shift to my release
Branch here and see what's there
um it's a different one and I want to
move this
check-in to my release branch and using
GitHub desktop you just take this one
and move it here and it will create a
commit for me now I can continue here I
can do a lot of other things here and I
can always roll back but but moving
things between
branches in GitHub desktop is fairly
easy you can also
learn a lot of uh you can learn how to
do things in uh with Git
um I never learned that so
GitHub desktop have have worked for me
the times where I've had the need to to
do these things
um releasing a hotfix from a repository
is just like releasing a
let me find that one this one
is by running one of the actions here
saying great release and when you run
that action you specify what version and
the name of the release the tag and so
on and so forth and when you run this
workflow it will create the release and
you can do that on a release Branch by
selecting your release Branch here
so
going back to
the presentation and talking about
quality
now
um
up until 2018 it was actually not
possible for people to run automated
tests with nav and after we have we we
got containers and we got the test run
and all of these things in containers
it's now possible to fully automate that
in in cicd pipelines and I'm sure a lot
of you have done that and and uh are
happy with that inhale go it's fully
automated so if you check in to your
repository or to your project an app
which is a test app then it will
automatically be uh be
recognized as a test app and run as a
test app
the way that we look at this is that if
if this app has dependencies to any of
the the test framework apps then we see
it as a test app
if you have a test app that doesn't have
dependencies to those then you need to
manually put that into the test folder
setting in the ago settings then we'll
still see it as a test app so you can
you can do both
um
we run automated tests as part of every
pull request and on every commit as well
we do as I said earlier locate the
previous release and use that for
upgrade test before running the tests
and
let's have a look at
some tests that are passing and some
tests that are failing
okay so
let me also show you that I will build
just finished so it took 40 minutes um
to do but for the tests I will move to
my daily repository where I'm working
for one of the esvs and we're running as
well test this one I run manually and
and you can see that they are failing
yes they are unfortunately but this is
also because I would like to show you
something so you can see when I have 10
apps for a little less than 10 apps six
apps for the tests and this is also
where I can see if each of my app is
passing or failing some tests as you can
see one of it and this is 968 test and
950 plus but 18 didn't so what I can
also do I can also see which test has
failing right so each of that test I can
in fact go and check with the developers
why those tests failing we're running
tests not every build but it's only
because they are taking half an hour
right so we are running them one per
night and just to see if everything is
okay and you also can run them manually
whenever you want and also for the next
releases as well if I will go to any of
the of the tests which are failing you
can see also the call stack for that and
then you can just
talk with the developer hey go and check
why those tests are failing if
everything is okay then great I one
expected that I had over 1 000 tests
failing because of some issue with one
of the feature and it turns out that I
cannot see so if you will not see
something it means that you're a lot of
your tests are failing so anyway you
should fix something
yeah and the reason for that you stay on
this one yeah is that the phone the
feature that we use here
is a GitHub feature called build div
summary like every job in GitHub can
have a summary and in 2023 they uh maybe
end of 2022 they introduced this summary
thingy and you can put text in there
that can be
535 characters
so if you have a lot of test failing
it'll overflow and we'll stop there and
what you need to do if you have a lot of
tests failing is to actually download
the test results and in that you'll of
course be able to see everything
exactly
so
let's have a look at improved security
another reason why you should use devops
if you are not already is that whenever
you need to like upload to to appsource
or uploads to a customer pte or whatever
then
um
if if a developer or a consultant need
to like carry that app in on their
laptop or whatever to the customer or
upload it on SAS or whatever there's a
reason there's there's a there's a risk
that he picks the wrong file on the disk
or and and there is also a risk implied
in having people having access to
customer environments all the time and
all of these things so
having like your devops workflows
deploy to customer environments and
making sure that these the the secrets
for these environments are actually
secrets on the environments inside of
GitHub and can only be accessed during
deployment and not actually by any uh by
any evil person or anything like that
just improve security and improves
the the risk of failures we actually had
people like uploading apps to appsource
from their laptop and and it like past
validation and that was kind of not
supposed to happen because
um this app was like a different branch
meaning that now they needed to upload
the real one the problem with that was
that that broke a lot of things to the
other one so we said you can't upload
that because
you have all of these things and but
they're not supposed to be there and
yeah then we have to have support and
then go in manually and remove these
apps and all of these things just
because somebody like was uploading
something wrongly to that one
so
what we suggest is that
run continuous deployment to a QA
environment and make automated
deployment to production environment so
today it's not possible to set up a
continuous deployment to production
environments
um we will make that switch so that it's
possible to say that this production
environment you always need if it passes
all our tests and everything then let's
do it
um but this is really to avoid silly
mistakes and and not having the latest
Source or whatever when you build stuff
and upload stuff
so
yeah we have a small demo on that yes uh
so every time when we are doing the
build we would like to push or install
the changes also on our QA environment
we have one sandbox which is uh where we
do the test and
to be honest I didn't I didn't need to
do a lot to set it up and that it will
work I just needed to go to the
environment created and QA environment
but I could create a more environment
and just put two Secrets One is the
authentication and also the environment
name so if you have multiple sandboxes
to which you would like to install the
apps and that's also possible and it's
very quickly to set up
let me go back here so every time when
we doing the build in fact 10 apps are
automatically deployed to the to the QA
environment where the testers can test
and we also can check if we didn't break
it before with the previous release as
you can see it doesn't take a lot of
time and let me just go here to deploy
and you can see that it's not only one
app but in fact it's starting in the
good order as well so I even don't need
to care about it it's just deploying all
the apps in the correct order of the
dependency every of our app is depend on
the forms and eam but all other can be
in the random order almost but you can
see that most of it is like 10 apps
installed in five minutes and I don't
need to do anything with that
so
pretty much that's all and maybe I also
will say one comment about a manual
deployment because sometimes we don't
have access to environment but we're
doing the app and this is also where I
also like GitHub because if I have a
consultant which needs to install the
app for example for them environment
they just go to the repository to the
build and just can take the files which
you have seen below and that's all what
they do right so that was all the
training of course it's not ideal but I
don't have in this case access to
repository today environment so if you
will want to just publish this up you
will be able just to take this app which
was generated but in general we doing as
much as we can automatically
the next section is about no before your
customer so
as you probably found out we are very
keen in Microsoft on updating all our
customers online to a new version every
single month
um
and every six months we will be rolling
out like a major release
and sometimes
partners
break their customers sometimes there's
something in the app that isn't
compatible to the next version and it
comes as a surprise to some partners
well not to Partners running algo for
GitHub because they will know before
their customers
what we have here is is we have several
workflows that you can run on a schedule
for testing your bits against next major
next Miner or the current version
why the current version how are we
developing on the current version well
a lot of people say that if if I need to
be compatible with version 20 because I
have maybe an on-prem customer I have
customers online that still running
21 or whatever
then I want to be developing on the
version that I the least version that I
need to be compatible on I'm not
developing on the latest version because
I stand the risk of using or using some
components that are not in the version
that the customer is running and and
thus like break the old customers
actually so if you're developing on 21.2
because you have a customer on that then
you run your test current that tests
your app on right now 22.2 and a month
from now 22.3 you'll be testing on text
test next major which is 23.0 or next
Miner which today is 22.3 and in a month
from now 22.4 all of that built in you
don't need to do anything but
create the inside of SAS token Secret
guess what in a
future not so distant that Insider token
will probably like 99 go away yes and
we'll be able to actually automate those
things even further so we'll just be
able to run these things now if I can
have a comment do that you can talk
while I'm finding my so I really love
that the token will not be
hopefully because I always have problem
to get it but I wanted also to say why
it's so important as a partner first of
all for your own apps which we have on
appsource I think I don't need to
explain that you can plan also the work
but when you have ptes customers already
paid for those ptes but maybe they will
be break in the future right so you also
can plan that work like there is few
warnings I don't know if you know like
language I think code you need
the name is wrong and it says that it's
a warning so it's like easy to show the
your customer this is the places where
we need to fix the warnings and we can
plan it the next month or something
right and this is nice also that they
can also have access to those warnings
as well
yep
um and here you see this is a repository
I rarely do any changes to this repo but
I will get a warning if someday like uh
business Central breaks me and probably
that's going to happen very soon because
if I look at test current here I I have
some warnings that something will turn
into a an error in the future so
sometime in the future when when these
things are not only deprecated but
actually removed my test next major
which runs once weekly will start
failing and I will know that I have six
months now to get that bug fixed or to
get that feature uptaken or whatever but
I will always know before and I actually
don't think there's been any change to
this repo for the last
month or so but it still runs these
workflows on a schedule to make sure
that that there's nothing wrong and this
one actually also updates the algo
system files
which is a good segue into explaining
what that is
now as you could see Kristoff took a
copy of a template and started out like
developing on that one but what happens
when we do changes what happens if you
have 150 repositories with 150 apps in
them and so so forth and and and you
figure out that a lot of things have
happened to algo since you started how
do you update that well there's a
workflow for that that's called update
algo system files this workflow is kind
of like Windows update
you can run it on the schedule and then
it's you'll always have the latest
version of fail go
or you can run it manually and update as
you see fit
so whenever you run a cicd workflow
it will tell you that
this check for updates will check
whether there are new updates so you'll
see ICD will tell you that there's
updates for your algo system files and
then you can run them of course that's
not going to happen if you're running
them on a schedule
so let's go through this Advanced
scenarios I'm going to talk a little bit
about a few little more advanced
scenarios because I only have 7 minutes
and 45 seconds left
um and anas is sitting there like
anxious to get up here and talk to you
guys so
project dependencies we all know that
you don't create an a number of apps
which doesn't depend on anything else
there's always dependencies to to to to
other things unless it's a very
um
yeah
siblab let's talk about project
dependencies first project dependencies
by setting by using a setting called use
project dependencies algo changes
character to instead of having like a
workflow where you see initialization
build deploy and and post then you'll
see stuff like this this is a repository
where you have a common project a
miscellaneous project a W1 project and
then Italy and the Danish one and of
course the Italy and danish one have
dependency on W1 which have a dependency
and common and miscellaneous so if you
look at this how that works
look at the cicd workflow here it
actually starts by building W1 uh the
the miscellaneous and and common
projects first in this one
and I don't actually think you can see
the names in there but then you build
the W1 and then you built the Italy and
the Danish one over here and after that
it then deploys things so just by using
one setting like Al go changes character
into becoming a multi-step
um
a multi-step built engine here that ul's
would have to do a lot of development to
to get working yourself
uh how far is that what's this the other
one that you can use for this is
something called GitHub packages
GitHub packages is a nougat packages on
GitHub that is included in your
in your organization so for internal
dependency resolution you can just
create a secret called GitHub packages
of context with an auth context that has
access to actually deploy GitHub
packages then all projects in that
organization if it's an AUX secret if
it's a project Secrets it's for that
project or repositorials over that will
actually start
deploying packages to GitHub packages as
you can see here this is a repository
app one that that are like publishing
these packages there are three apps in
this one and these packages are then
available for
the app2 to find the app2 will now be
looking for for those and Publishing
itself and if we look into
app2's CI CD pipeline
find the Run pipeline
once more
run pipeline
find the resolving dependencies we will
see that this one figures out that it
needs some dependencies and it should
find them somewhere
did I find them here they are
it a core downloads this one from new
nuget packages from GitHub packages
so
that's as easy as it is to get like
dependency resolution running to all
your internal ones now
the immediate question would be what do
we do about nougat packages from other
people well we are thinking about that
as future Investments so I have a few
few things here that I want to talk
about the things we're working on for
the future translation is one of them
the the
current thinking there is that we have
right now we are talking to a number of
Partners on how they are doing
translations and figuring out how we can
like make something generic work that
fits most Partners probably it's going
to be a few
uh translation strategies that we
support so that people can support
whatever scenarios they have for nougat
packages
current thinking is that
that we want for all appsource apps
they'll be available systems directly
systems symbols for all appsource apps
would be available in a nougat feed
so that builds will actually be working
runtime packages
will at some point in time be available
from a new good feed for partners who
opt in
algo forgettable automatically trust the
appsource nougat server so that you
don't have to set anything up if you
want to like get nougat packages from
other partners you need to trust these
things so I don't have any promises I
don't have any dates for this this is
the current thinking what we want to
support so that building becomes and
testing and all of these things becomes
easy to do
another thing
we're working on is performance
building cannot be performed enough so
what we are looking at today is that a
cicd workload looks like this there's a
initializer built and a deliver we
talked about that already we're changing
that into uh not this one but this is
the the multi-project one where it like
builds things in in order right now
these things can actually run on Linux
they're pretty fast these things are
pretty slow because they require a
Windows container in order to build and
in order to run
what we're working on is to change that
into split the build and the test into
two
uh two jobs and the build actually do
not need a container and the test will
need either a container or other things
so this is the the same one with like
multiple things multiple projects and
then these things will be pretty fast
and the testing will require a container
or will it
well actually not because we'll support
other test environments like Cosmo
alpaca build containers
Azure container instances online
sandboxes and these things might already
be there so that it doesn't take any
time to spin them up so running tests
might be much faster than that so the
idea is
that all workflows will be able to run
on Linux for better performance and
lower pricing as Linux Runners are half
the price of Windows Runners and all of
these things are available for you guys
too
just use by updating algo for GitHub
system files then you'll have the latest
and the greatest
uh the other
piece would be that Cosmo alpaca they
actually also will support algo directly
from the vs code extension so you can
create Dev containers and stuff like
that I think
they're going to show that in their
session here after launch I think so
um the other things that I just quickly
have 30 seconds to talk about
paid scripting
um Vincent showed you that in the
Keynote
we will be supporting whenever that like
matures
that you take these yaml files that spit
out by the page scripting and just put
into your devops and we run that as
tests leap Works was announced yesterday
that we have an integration with those
also for devops code spaces and last but
not least
Power Platform support which will
be the next one and you have 39 or 27
seconds to get up here and start your
presentation
thanks for that
