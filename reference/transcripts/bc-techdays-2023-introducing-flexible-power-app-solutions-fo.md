# BC TechDays 2023 - Introducing flexible Power App solutions for Business Central

- **Source:** https://www.youtube.com/watch?v=KVP4j0xvydw
- **Video ID:** KVP4j0xvydw
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 45m10s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

so let's get running uh for next 35
minutes we'll show you a little bit more
about product demos uh some of the Power
Platform apps and solution to build and
also obviously show you how you can use
I'll go to build a very very amazing
stuff so
let's get started
how many of you use Power Platform or
just play around with Power Platform to
build some kind of value you can sell
show or inspire people around you well
we don't have enough hands I hope next
time you'll see more and more and more
but actually you can really really build
a lot and it's an idea that it's easy
you know cost saving and it just looks
and feels great
one of the main problems with Power
Platform that it has so many connectors
like
this slide last months or two months ago
was 900 connector now it was a thousand
so it's really easy to inject real
Integrations uh with you know in a very
kind of light fashion
and build value of that now you can say
why would you even consider to start
building power apps you have a great
platform we are on mobile on tablet or
obviously on desktop in a cloud
and I think in the real life there's a
lot of scenarios why you would seriously
want to consider at least consider to
start building powerapps for example you
might want to build some very special
crafted UI or user experience to those
applications
I just talked about connector connectors
meaning you can really reach a lot of
services Integrations in in no time
we showed you yesterday in the keynote
how you can use like
virtual reality controls
and obviously from maybe a licensing
perspective
powerapps usage rights are part of some
of the business Central licenses so it's
not like in some cases you need to pay
extra just to get that stuff rolling
what we announced yesterday on our
keynote that as a Microsoft we give you
a number of apps we start with three we
show you one we'll show you two more
right now basically apps to inspire you
also customers what you can build which
guide not only as a great apps to use
you know in your hands but also as I go
ahead copy modify and learn learn how to
build powerapps
with that I would like honest to take us
a little bit more about those apps and
show them in real life thank you yeah as
evgeny mentioned we're releasing three
separate apps they take Auto app the
warehouse helper app and the coffee Mr
app
the motivation for building these apps
has multiple factors to it first off we
wanted to make an easy starting point
for partners to get started if they want
to build powerapps with business Central
either using it as a foundation to build
on or just getting inspiration from what
you can build we also had an aspect of
it also had an aspect of dog fooding to
it so we wanted to practice what we
preach and see what kind of roadblocks
Partners hit when they tried to build
powerapps connected to business Central
and we took all that learning and put it
into the apps so they should Encompass
some of the best practices in there and
of course as we already mentioned a
couple of times it's using the new algo
for GitHub pte template
go ahead
anyway the first step we're going to be
looking at is the warehouse helper app
so this is a simple app that lets you
scan an item and update the item's
inventory we purposefully make this a
very simple scenario because we know
warehouse management is complicated and
there's a lot of solutions out there
already solving this so we don't want to
spend time and energy competing with any
of your Solutions instead we wanted to
build an easy Foundation that you can
use either build upon or as an
inspiration that solves all the
technical aspects of power app
development in this area and gives you
some visual UI patterns that you can
reuse if you want to for your own app
let's switch over and see what it looks
like I think that was enough slides
phone we don't use a phone we just use
an iPad still because it's just easy to
connect but in a real life you'll use
your phone which you have in your pocket
exactly
if you look at the app you can see it's
very different from anything we built in
visual in inside visual stint inside
business Central there's some branding
resources here either for the customer
for their partner built it we have a
little information icon where you can
put in more information about how to use
the app put in some links to additional
documentation
because it's a warehouse helper we
obviously need to be able to pick what
Warehouse we're working in that
information is persisted in the app so
users only have to use it when they move
between warehouses
and there's a big call to action that I
think we should just try hitting
and this takes us directly into the yeah
I'll need to move over to the other side
this takes us directly into the barcode
scanning capabilities of Power Platform
this is capability the Power Platform
supports out of the box so there's no
need for us to do anything other than
integrate it into our power app as part
of the sample we're sending out we also
have a small document with some sample
barcodes and an Al extension that
extends some of the apis we want to use
and just sets up the detail code for
some of these items so we can go ahead
and scan this
now it takes that barcode passes it into
the detail number and pulls the
information from business Central you
can see here we have a very simple card
that shows the information you need and
some intuitive UI controls you can use
to update the inventory value
and you just go ahead and submit that
and that updates the value inside
business Central and takes you right
back into the scanning experience
there you go so that was the first step
we have
the second app we want to show you
yeah the second app we want to show you
is the take order app this is a more
complete scenario it's focused on
Frontline workers at restaurants and it
lets them assign table to customers and
take orders from these customers in an
intuitive interface
but let's just go ahead and see what the
app actually looks like
thank you you'll see visually there's a
lot of similarities to the other app I
showed you that's because we're trying
to establish a sort of simple visual
identity that you can just copy for your
own apps that makes it easier to build a
line of power apps that you can use for
your users there's some branding
material there's the information tag up
there but let's just go ahead and start
taking orders
the first screen we see is the available
tables we have at this restaurant you
can see there are already two people or
two groups of people sitting at staple
one and two we have a new group coming
in and they want a little privacy so
we'll just put them at table six
now this takes me to the menu you can
see all the items we have available you
can use the filters to navigate through
them to make it easy for you to to give
the customer what they want one of the
things we focused on a lot here is that
we wanted to build something that felt
like a native experience so stuff like
doing quantity controls that look
similar to what you get in Native apps
for shopping using a common shopping
basket Paradigm where you can see the
amount of items you picked and the total
amount of money it costs is some things
we decided to do to make this easier to
use
I've added a few things to this order
already so let's go ahead and review it
we're digging to a summary page here
where we summarize the content of the
order to make it easy to get an overview
and see that everyone in the group
actually got something that they they
ordered you can expand this and take a
look and if there are any questions to
the food you can just click one of the
items and you're presented with a simple
item card that has information about the
product you're selling it can have
information about allergens and of
course the quantity control is also
available here so we can just go ahead
and update that
let's submit that order
now what this does is that it creates a
sales order inside business Central and
adds each of these lines as a sales line
you can see that table 6 is now updated
there's an order that's been placed if
we click on it
we'll load the sales order from business
Central and pass it into the summary
that we saw before and you can either
add more to the order or just go ahead
and check it out
checking out an order means posting it
inside business Central we're using a
power ultimate flow to trigger that
action so this really is utilizing a lot
of the Power Platform capabilities and
components we have available
thank you
yeah that was a quick introduction to
the apps we're not going to show the
coffee MRI app again because we already
viewed that at the keynote yesterday but
if you want to we will we will encourage
you to go and try them out they are live
on GitHub GitHub now under the topic PC
samples that you see here on the slide I
don't need to be developer to get all
those apps like do something that's a
good question so you can either Fork the
repositories like Freddie talked about
make it your own app customize it make
your own changes it use it or you can
just go to the releases that are in the
repo and take the zip file and the AL
file and download in your environment
yeah like we saw in a previous session
so it's very easy to you to try without
apps without even look even how is it
built
all right so we're going to discuss
right now what does it take us to build
such apps and make them repeatable
repeatable meaning you don't do it once
but you can build distribute hopefully
you know get your customers uh internal
collaboration
and so on so forth but before we do that
let's just have a very kind of quick
overview what does it take to build a
power app actually I'm talking about
PowerApp but we're talking a kind of
PowerApp solution which is just one
representation of that first of all you
need to be like you know app itself
which is like straightforward you have a
great capability drag and drop controls
you can really Express a lot of layouts
is no problem with that
uh you need to have some data to show in
your apps and the way how it works is
powered by connectors
the data can be powered by any data
sources and from business Central we do
recommend you use our
to the first party our own connector so
you can go ahead and build apps with the
data which come directly from business
Central now obviously it's like
obviously it's all about data so if we
use the ICS or Partners you do need to
build apis which expose your data which
you can consume in an app shown a screen
and work over that so the first Insight
that powerapps never exist on its own
you always have your asset Your solution
with your API layers so we can talk to
it and get some magic happen in many
many cases we do give you API out of box
but we all know the basic and usually
you need to bring more to make some
magic happen
good news
at the Microsoft we do a lot of
investment in our connectors release or
release we just show you how easy for
you to I don't know get all images on
the screen translation support custom
API so Innovation happening you know
semester after semester more and more
features coming so it's like we really
put attention to that and we try to make
it more and more powerful with wave over
wave
so let's say you have a power app and
let's say how extension so the concept
we kind of want to have you might be
like a mental concept it's like we want
to get it to one solution or one or one
package and then have an ability to work
with this package maybe move it to
environment or multiple environments
because that usually will be the case
and it scales you have usually multiple
customers or whatever
and in real life it's not just a moveset
package because you need to build it
develop modify how to fix verify support
and so on and so forth like a whole like
a life cycle is happening with that
package exactly as a Freddy and
Christoph just showed it five minutes
ago so it's all applied but now it's
power pattern solution and Al code and
somehow it need to work together on
scale
let's talk about not like I mean
challenges but what are the main things
involved and where we have a different
blocks so first of all we need to build
IL extension which expose apis the good
news is that the problem you need to
have developer who can do it for you we
don't give you yet any no core tools so
we don't have any support that you know
as a consultant on end user you can go
ahead expose your apis some kind of in
UI and get them created you still need
to have development involved to build
those apis but that Samsung will
hopefully address in the near future
but we all know how to do that job right
now
from Power Platinum perspective two
years ago it was really really really
hard to build something which can be
like be repeatable or maintained there
was not that many
application lifecycle management tools
but as of now
the world has changed our platform put a
lot of attention to make sure their
assets can be reused and they also put a
lot of effort semester of the semester
to build more application life cycle
management features so for example if
you go to their website there's a lot of
not just a lot of thinking but for
example six months ago we announced
power pages I two months ago we
announced now we can you know have a
life cycle management for power power
Pages you have IL GitHub action so team
put effort to make sure Power Platform
assets can be used which is super
helpful for us because we don't need
those capabilities in the first place
now the real problem as of now to build
repeatable power apps actually a little
bit how powerapps are built because
right now if you build a power app
your connections to
business Central apis backend is
hard-coded as a part of application so
what it means it means it's not like an
end user can go ahead select which
environment to connect but it's really
very kind of deep hardcoded as a way how
is that app is built
it's not something specific to business
Central as the connector that's just how
power apps are working today so we have
this limitation as of now that some of
the connections are hard coded to the
given environment
so what it means if you look somewhere
in a code and I don't want you to look
it but if there is if you build an app
on a given for a given environment
somewhere in app you have hard-coded
reference and it's really really tricky
to find it first of all but second of
all to change to something else so what
does it mean it means if you build an
app today to get this extension get the
one solution and one pop to publish to
another environment it's actually not
going to work because once you publish
it there you won't be able to compile so
to speak because referenced and valid
and then nothing is working you need to
you need to use a manual work so it's
not helpful for anyone well for us at
least
so what we announced yesterday that we
built incredible tools based on a I'll
go so GitHub which help us to deal with
some of those challenges
and right now we're going to look how it
looks in real life so back to unders
thank you
yeah let's take a look at what a normal
development flow can look like when
you're working with powerapps using the
tools we just talked about here so this
is the coffee Mr field helper app that
we showed yesterday I'm going to be
making a change but let's keep it really
simple so we don't over complicate the
pr we have a little byline here and I
think we could update that to
let's say we love coffee instead and
just asked a few exclamation marks to
make it like really clear that we really
like coffee here we'll save these
changes and we'll publish them on the
development environment that I'm working
on here
so we can go ahead and validate that
this is what we want after we've done
some testing here in the dev environment
we want to get these changes into our
GitHub repository
so let's jump right into the Repository
it is right here
so right now you'll see that this is
under my private user but coming soon
we'll be publishing this along with the
two other sample apps so you can try
them out just straight from GitHub
um
if you're looking at the repository here
you'll see that we have the coffee Mr
folder which corresponds to the Power
Platform solution containing the
PowerApp and the power automate
artifacts that we're using to solve this
scenario we also have a small Al
extension here that we use to extend the
apis with some additional information we
need instead of some sample data to get
the app to run easily what we want right
now is to get the Power Platform changes
into this repository so we'll go over to
the actions that we get for free with
the algo template and you'll notice that
compared to the previous session we have
a lot of the same things you see but we
have two new ones which is called pull
tile platform changes and push Power
Platform changes these actions allow us
to connect to your dataverse environment
and get the changes into your repository
and into a nice PR
if you run a random you just go ahead
specify what environment you're using
and say run void flow
now as you can see these can take a
couple of minutes to run because of the
way GitHub manages their dispatcher
Runner logic and this is a pretty low
budget account right now because it's my
own so instead of waiting for that I
prepared a preview or I get a pull
request right before using the pull
Power Platform actions so let's just go
ahead and take a look and see what that
looks like
you can see that we're updating the
solution with the latest changes from
the power plant from the powerapps
environment that we have
um and this is just a normal GitHub PR
but if we go into the files changed and
let me say right away this is an area
that power apps know they have some
issues in and are working on because a
lot of their state information of the
app is part of the source code so your
pull requests are going to be a little
messy but as soon as you get used to
knowing where you need to look it's
actually pretty easy to see so all of
these things up here are just State
information but if you're looking inside
the connection folder or the SRC Source
folder you can see the change we did and
you can see we actually changed the
byline before so maybe we need to think
a little harder before we change it this
time
um if we want to just take a look at the
actual file here you can see that each
of the screens inside the PowerApp are
represented using yaml so it's not the
easiest language to compile for people
when they want to read it and understand
it but it is actually possible you can
see the name of the start screen here
and you can see all the visual
components that we have on the screen
and there's also all the actions like
the invisible action that we're using
here to reset some things and the
powerfx code that is running there so if
you want to you can definitely still do
like proper review cycles and make sure
that the code that you want to check in
is something that makes sense
so what just happened is basically
Anders what's in his development
environment he did the change to
PowerApp obviously it's a simple change
you can do much more sophisticated
change you can also change your L code
and then if you take these changes and
we kind of push or pull depends how we
look to have a centralized repository
and now I'm going to show you next step
how can you take our updated asset and
distribute to different environments
like customer environments or whatever
it might be so have a look on the second
part from a change to distribution
yep exactly and there are a number of
different ways you can distribute your
code using these actions
as Christoph and Freddie just showed you
there's full support for continuous
integration uh by the way if you didn't
notice I moved to the warehouse helper
environment here which is one of the
public environments that you can go and
check the source code out of or just
check out the release items uh to
release artifacts and download the Power
Platform solution in Alf from here
in here you'll see that we have a
working cicd flow that is currently is
that something you can see
tried like that that's currently
deploying to staging and if I jump into
this job you'll see that we don't just
deploy the AL but we deploy the AO and
then the Power Platform solution
so if you want to get your bits into an
environment to make sure you can do some
q a or validation we definitely
recommend you set up this the ICD flow
and use that obviously for production
this is not the ideal way to go about
that instead here what you want to do is
you want to validate your code you want
to create a release and then that
release is going to be available on your
GitHub repository right under here and
as as we already saw you have all the
relevant files available here to either
download to manually deploy or you can
go ahead and use some of the actions
that we have available as part of the
template you publish two environment
action is an action that's part of the
core algo algo for GitHub template but
we've updated it in this preview version
to include steps to deploy our Power
Platform Solutions so you can see here
we ran it to deploy it to DPC check days
demo which is the one we used to show
you the sample apps from and this
contains both the Al and the Power
Platform artifacts
yeah so by the way that's how we do them
in Microsoft they don't go to a machine
I don't need to I don't need any more of
red doesn't it anymore before Dimitris
and Mike Morton so harina organic demos
telegon and cradle stuff you can just
push a button move all our demo apps and
extensions and then we can use a demo
environment for a great demo so just a
lot of time savers
so what just has happened
is honors took a latest change with 12
PowerApp we change the label our IL
extension and move it to environment
which can be customer environment in the
production environment but the final
part I just told you five minutes ago
that it's not possible because some
reference should be hard-coded but
that's exactly the magic of automation
we give you because behind the scene
we do some transformation we know where
we go we know which environment we know
which configuration and we can go ahead
and update all Power Platform assets
behind a scene to do all this invisible
work so now that package will be up and
running ready on that environment with
no more manual work required
if you reflect back
without having these tools you need to
find a developer who can build IL code
and apis grade find another Power
Platinum developer maybe different
people try to get stuff together some
kind of compile somehow to apply deploy
customize to make this package ready to
be consumed and with a new tooling you
basically just press a button which was
called like deploy to environment even I
can understand that you press a button
magic happens and you're ready to go
so how can we start on that journey to
get to that state
that is a great question and luckily
it's as easy as three simple steps first
you need to get your repository which
we've seen a couple of times you need to
configure the environment you want the
repository to connect to and then you
just add your code
let's go ahead and see what that can
look like
yeah thank you and so depending on what
you're trying to achieve there's a few
different ways you can go about getting
a repository if you're just interested
in trying out some of the samples we
have the easiest way for you is to go to
the BC samples topic on business Central
this is where you'll find the two
current samples that we have available
and it's also where the coffee Mr helper
will be available once that's published
if we jump into one of the samples like
the take order sample here you can see
that the repository is here so you can
either get the package you need the AL
the AL extension and the Power Platform
solution from the release artifacts or
you can go ahead and just Fork your fog
to branch and create your own version of
it and start building on top of that or
just set up the environment and deploy
it on the other hand if you already have
a Power Platform solution and you're
looking to get a source control and
application lifecycle management support
for it or we would recommend you do is
to go to the algo pte template and use
that template as a starting point this
template also has the three easy steps
to get started and a link to get a more
detailed description of an easy
step-by-step guide on how to do this the
next step is to set up the connection to
the environment
and let me jump back into one of our
repositories to show you what that looks
like
so we already saw the
sorry that's the wrong file
we already saw the algo settings file
and there's been some changes to it to
support Power Platform Solutions so now
you have a Power Platform solution
folder name here which corresponds to
the name of your Power Platform solution
in Power Platform
um you set up the environment like you
usually do and then you divide
deployment is this a good resolution
yeah I guess so then you define
deployment information on how
you want to connect your ad effects to
that environment or with what BC and
Power Platform environment you want to
connect to you can see we have the
business Central environment name and
the business Central Company ID we also
have the Power Platform environment name
and that's the Power Platform
environment you're going to be deploying
Your solution into
once you've set up the environment
information you need to set up
authentication I think we also covered
this a bit in the previous talk so I'm
not going to go too deep into it
the way I've done it is just to create
some repository secrets for this repo
and you can see I have one for each of
the of the environments we've set up
here
the steps needed to the authentication
context is a string of Json that
defines the authentication you want to
use the authentication method and tokens
that you want to use to connect to your
environments and you can get these
pretty easily by just following the
steps we have available
under our setup guide
with just find those as well
you can see there's a detailed
step-by-step explanation here of how to
set it up and some code Snippets you can
run that will help you sign in and
generate all the tokens you need to get
your environment up and working
then the last thing you need to do is
just to add your own code we've already
seen that you can simply just drag and
drop the solutions if you already have
them locally if you don't have them
locally you can go ahead and use the
actions that we have available as part
of the template to get those Solutions
into your Repository
I guess when you're saying we show you
power apps but we're talking about power
pattern solution what we mean by that
you can bring your automation flows
powerapps as a package and we can all
deploy it on your behalf to a different
environment so it depends what you
really need when you build Power
Platform Solutions
we have one link to go BC power apps to
get all the knowledge
and with that we're looking forward
we're going to build
and it has some like 15 minutes for a q
a for a question we had like a lot of
topic so maybe you can get Freddie and
Kristoff back on stage
and it can have a conversation about
everything you've seen and learned today
I'll just repeat the question
thank you sir
hi um
so if I want to publish a Power Platform
up to 100 customers I need to create 100
environment and push each on its own
and if I have an update I have again to
push 100 buttons
so if you want to connect to a I don't
know could people hear the question
maybe you want to repeat quickly yeah so
the question was what if I have multiple
production environments I want to deploy
to do I need to manually run the publish
action each time you do need to do the
setup for each environment so you are
authenticated to connect to it but in
the publish to environment action
sorry let me just run the action instead
of this
um you can use wildcards to say what
environment you want to deploy to
so here you can do product star and that
will deploy to all your production
environments and this is a common
function because in piece of the core
functionality of the AL built template
but if you have 100 customers and you
have like a Power Platform solution
maybe you should put that Power Platform
service in an app source and and to use
that update engine for that instead of
having
mspts but you're right if you have a
number
uh the manageable number then
environments there you might actually
have a situation or it is our
recommendation that you create one algo
repository per customer and then use
dependencies to say this customer
actually uses these apps and these Power
Platform solutions from other and then
use the deployment so you'll have one
environment there and you control the
upload from that for that so you can use
multiple different setups for that but
great question and the purpose of the
preview is to get like real world
experience from how people want to use
Power Platform along with the business
and full Solutions so if we start seeing
that like having a lot of customers for
a person and extension is the way to do
it then we can look at improving the
process file
everything you showed so far was using
GitHub if we're still using Azure devops
should we migrate
because it seems like we're betting on a
dead horse
I think Friday is a great question to
you you can maybe repeat well to get the
functionality that we have here
for free you need to be on GitHub there
are the Power Platform team has shipped
there
[Music]
um
their workflows or their their actions
for Azure devops as well so you'd have
to like if you want to stay on Azure
devops you'd have to
uh to to to use these to create your own
workflows for these things all
maybe I don't know if allops are going
to support a I think I heard him talk
about Alm for a Power Platform as well
but probably got to be different what
we're doing is on GitHub only and that's
our Focus
I we we haven't built any specific IL
GitHub action do you know take a Power
Platinum solution package unpack it's
all done by bio platform so Power
Platinum invests heavily in a GitHub
themselves and we basically benefit
tooling the gift so to speak for us
so I guess yes Investments happen across
all Microsoft groups to this tooling not
only like a business specific if it
makes sense
we had a question left yeah that was
actually also about uh GitHub versus
devops we've heard so much about GitHub
and it seems like devops is just no
longer existing in in the the
environment so is this a final push
away from devops
um do you recommend us
all the switching to to GitHub now or
what's going on
so you're not going to hear me say I
recommend you all switch to GitHub so we
created algo for GitHub and we are
extending algo for GitHub in order to
add to to to make Partners be able to
save time
if you want to take advantage of these
things yes you need to switch to GitHub
we have a lot of stuff on Azure devops
ourselves in Microsoft so Azure devops
is not going away
if you have stuff on Azure devops that
you're developing yourself like scripts
and stuff like that you should look at
how much time you spend on that and say
if I spend maybe one developer resource
a week or a month or whatever is it
worth
being there or
should I switch in order to actually
have that developer spend time on
something that provides customer value
instead so it's it's your it's a
decision that you need to make all of
these things are free on GitHub and all
our Innovation is free when we like
going going forward we are going to do a
lot of things on switching to Linux in
order to save time and money and stuff
like that
all of that of course is not going to be
available for for you on Azure devops as
well so what you're seeing is just our
Innovation is on GitHub and when we
started out looking what should our
platform be just this when we started
out looking at
es code versus Visual Studio we selected
vs code maybe a bold move back then
totally the right move today
when we started one and a half year ago
looking at Azure devops versus vs code
and we said versus GitHub selected
GitHub
um
we're happy with that we know that a lot
of partners are on Azure devops already
but we think that GitHub is the right
place to be for a for a SMB solution
that is free and and agile like algo for
GitHub is because I see Azure devops
more like a Enterprise devops solution
and and it's up to customers what they
want to
Maybe
um I was using devops I was using a bit
bucket and now I'm using GitHub and all
because of corporate things and so on
and to be honest as a developer I like
GitHub
I mean from
maybe it's not perfect for the projects
let's face it but for the code and for
how you can also use Visual Studio code
with that you can see there is a like a
native functionalities also for visual
extensions for visual studio code like
an actions which we didn't show right
also showing it just Visual Studio code
directly from GitHub we will just change
dot Dev and you will see it so there is
a lot of things which are there which I
would not switch it to devops store my
code because I just like how GitHub
works for me right it's it's much
simpler I think in many places of course
for maintaining the backlog I'm not
using it I'm using jira because that's
also called what corporates inside
power bi reports
I guess it's no brainer at least for us
that'll be the area we're going to bring
it first to make it just happen it's a
type of feedback like
for us that will be the default choice
now no discussion about this okay
um perhaps a question for the future oh
are there two
um you showed us how you can deploy from
GitHub to the customer environment
um mixed solution with
um IL and Power Platform but if you have
something in the app Source RL solution
and if you want to have mixed solution
that you want to plot from there how
could you do that and another question
that's with Power Platform but we also
have often the problem that we need also
Azure function and all that stuff must
be deployed from appsource to the End
customer and how are you planning to do
that in the future
good question so I probably can take
that
um on the app Source I had a slide
talking about nougat the biggest problem
with with appsource apps is really that
in order to build the apps you need to
get the runtime package from the partner
what we're looking at there is to create
a service
endpoint on appsource where you will be
able to get symbols so that now you can
build
and also if if partners are opting in
then we can get runtime packages
automatically generated from appsource
then you can also run tests
until then you'll only be able to run
tests on online sandboxes
the the deployment in algo actually
supports installing and appsource apps
apps apps an appsource app along the way
so if you have a dependency on an
appsource app and you've got it built it
will actually install that appsource app
in the environment if it hasn't been
installed already before deploying the
AL app so so that piece actually works
but you won't be able to build unless
you have the
the pieces there
on other things that you want to to like
deploy along with that like the Power
Platform thing is the first place where
we took something else than an Al app
and we'll use that right now it's in in
preview in the in a different repository
and the reason for that is we want to
make sure that we get an extensible
model and and what we'll be looking at
for other things would be places where
you would have to write code then you'd
have to like put in a script somewhere
that can create the other things that
you need I talked to a partner yesterday
who wanted to to plug in a data
generation engine before he runs his
tests and other things so so create an
extensible mechanism for you to be able
to extend but still utilize everything
of algo without modifying anything but
be able to extend so that that's going
to be the answer now date I have no idea
yeah so that's it's a very good point
what we showed you here right now in
preview is for the pte template and we
have appsource coming soon it's in our
backlog I don't think we're able to
commit to any timeline yet but that's
the next thing we'll be looking at here
and then stuff like Azure functions is a
great idea I don't think it's something
that we considered so far but I mean
bring it up on the idea side and I mean
it makes sense to have all your
Microsoft artifacts and be able to
deploy them in one package
so that's definitely a good input
I have a question for Christmas
container solution are you using for
your
container productivity I'm just using
the standard one so I was not using uh
Crystal can you please repeat it
what kind of the containers I'm using
yeah yeah are you using the
computing
for your
your instances and no no I'm using uh
Freddie maybe you will take because I'm
just doing the default containers right
so yeah so what was the question I
didn't get it so you can talk into the
mic yeah are you what you recommend
actually because you listed several
solutions for containers for the built
and test pipelines uh would you
recommend Azure to use Azure container
instances for these things or the
built-in so I mentioned the Azure
containers this is future thing yeah
it's something we're working on and also
alpaca containers which both will be
Cloud containers today what's supported
for Dev environments is local deviant V
which creates local containers or Cloud
deviant which will create a Sandbox for
you the other things will be added in
the future so that you can create an
Azure container instance an Azure VM or
a an alpaca container as well I will
probably use the sandboxes because I'm
doing everything in Cloud so that for me
is easier but if I would need the
container then I will try to look for
now I'm just using the standard so it's
like just taking the container from PC
container help us probably or some
background stuff okay thank you
whatever is able to set up
it'll go with on-prem
if you'll be able to set up algorithm so
the question is uh
the reason why we don't have an
on-premises
template is really that as soon as you
start to talk about on-premises it pulls
along like a lot of things like are you
going to create your own dlls are you
going to modify the base app are you
going to do all of these things and
those things are not supported as long
as you
stay within the limits of of what you
can do on cloud meaning your cloud ready
then you should be able to create a
setup with a go for GitHub that compiles
and makes your app ready we do not have
at this time a deployment mechanism for
on-prem I know that there are a few
Partners working on either taking uh
Waldo's alops
engine to be able to install packages
for on-premises or create other
workflows to integrate with Al go to
deploy to on-premises but if you do
special things like if you have your own
dlls or a modifying base app and other
things
you might struggle more with Al go than
than you want to
building
you can build uh
for on-prem as well
you have like two minutes left maybe
like one more question
thank you so much
um I had a question regarding one of the
pipelines that you ran that was
um double checking the dependencies I
think the app dependencies So currently
we have one repository per app typically
and some of the apps that we develop are
um basically the dependencies for some
other apps
um how exactly would that function and
secondly do you actually recommend
um combining
um all the apps into a single repository
for like one project
um as in what is your most efficient way
of running Pipelines
thank you so it really has nothing to do
with running in the pipelines it but the
the recommended way of of setting up a
nail go repository uh the the strategy
for that is that
uh the repository is the release vehicle
so all the apps that you release
together uh which I recommend they would
be in the same repository they can be in
multiple but it's just easier that when
you say I create a release version 1.0 I
have all the apps there now
the project within that you can have
many projects in the algo repository
these are the ones that you install
together so if you have Denmark Italy
and Germany then those would be projects
in the repository you release them
together but you install projects and a
project can be multiple apps but the
project is where you get the artifact
you get the zip file with the apps and
that one you can like take here and
install that if you have dependencies on
foreign things you get an artifact
called dependencies so once you have the
apps and the dependencies artifacts and
the Power Platform artifacts you have
everything you need
to install to a customer
um and and that's the recommended
approach if you want to like
automatically like handle the
dependencies between these things you
create this GitHub packages of context
then all the apps all the builds are
being automatically published to a
nougat feed in GitHub which is private
so it's only for your organization and
the other repositors will automatically
resolve those and find those just by
adding in-app Json a guid to the app
that you need to depend on and it will
automatically resolve those dependencies
from the other repositories that if you
don't want to use nougat
over time now but if you don't want to
use nougat you can set up like app
dependency probing paths in your algo
settings file to specify which
repositories do I want to get my
dependencies from but that's a yeah
that's just more cumbersome than using
the organization right nougat packages I
think we're overtime thanks a lot for
all the very interesting questions and
for
thank you thank you
