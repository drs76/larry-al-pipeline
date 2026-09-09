# BC TechDays 2022 - ALM Accelerator for Power Platform [CoE Starter Kit]

- **Source:** https://www.youtube.com/watch?v=OoLx-BqQb-E
- **Video ID:** OoLx-BqQb-E
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 80m34s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

foreign
ER for today is Michael amigo
good morning and welcome here to the
busy Tech days in Antwerp as he
mentioned my name is Michael Miguel I'm
a Enterprise architect and software
so and devops engineer from Cosmo
consult sorry I'm a little bit nervous
so I'm very proud to stay here in front
of you and see all this
Keen phases which are hungry about Power
Platform
today I want to present you my favorite
tool it's the Alm accelerator for Power
Platform this tool helps me to apply in
Power Platform a standardized software
development process in combination with
Azure devops pipelines and fully
automation of deployments
but first of all
wait a second
yeah
let's answer two question what is
application lifecycle management and
furthermore why do we need this in Power
Platform
the first one is answered very quickly
because of it's a definition it's about
defining development testability quality
insurance
deployments and for sure continuous
maintenance of software products
and this might be familiar to you
because of you are experienced business
Central Developers
hopefully also in Power Platform and you
know in Power Platform we need the same
principles because it is also software
development
especially when we do something together
between both systems
and Power Platform we have seen in the
keynote a short overview it is a set of
products
we have share powerapps power automate
power bi to analyze some data from
Business Center or from asset data
sources we have the New Kids on the
blocks like
power virtual agents and power Pages
formerly known as power apps portals
underneath of this Mighty Technologies
we have
other
fancy things like connectors
I guess in the keynote someone told us
650 plus connectors I guess it's even
more because of you can set up some own
connectors when there is an API
furthermore we have power of X it is the
local language for canvas apps
and finally AI Builder which brings us
artificial intelligent
to our products and databers
and this was for me a hard one to
understand what is the difference
between Power Platform and dataverse for
that reason let's repeat
Power Platform is just a set of products
powerapps power automate power bi and so
on and small adjustment
hopefully
perfect
so let's continue
Power Platform just a set of product
and it uses dataverse as a native
storage capability dataverse itself I
have discovered it pretty late because I
started with canvas apps database is
nothing else as the Formerly Known CRM
and database for sure
is a database with customized tape
customizable tables remember NIV or
Business Center we have the same things
there we can create some own tables
customized tables here in database we
store power apps and Records power
automated flows and Records we have some
own tables like accounts
contacts products data related to zrm
world
let's discuss
application lifecycle management and
business Central and Power Platform and
from my point of view the most used
products from Power Platform except
power bi it's a different story are
powerapps and power automated flows you
need something to connect to business
Central and you might have also used
database
for that reason let me show you another
picture to clarify
the sink
my left side you see this is Central we
all know it it is an environment
containing a database our tables Pages
reports code units
all the stuff and apis
furthermore
on the right side you see dataverse
it is an environment
and we have set the Power Platform
products like powerapps power domate
flows database tables
only connect both systems and this will
be the future because of it is so easy
to connect both systems
we use connectors connectors rely on
apis on business Central
and obviously connectors in database
which helps us to bring this data to a
flow or
invoke something in business Central
feel some more you also might have known
there's a second option virtual tables
and thus
I would say a virtual table is nothing
else then you have a physical table in
business Central for example and the
virtual sibling which feels like a real
table in database
in conclusion you can connect this table
in database with other tables and
same in business Central so a shared
World between both
it's a mighty technology
but back to my application lifecycle
management story and during the
preparation of my story I thought I need
something
well ridiculous to show you here my love
to Power Platform and some of our other
speakers might say well power flow
power of love and Business Center how
can you present me this and
why not because of a spear because of
from beer now I have learned Business
Center and beer is every time a great
story
for that reason
I have decided today we have a beer
tasting event it was announced by Luke
and furthermore well we have a lot of
hungry or thirsty speakers which could
be the better testers
in conclusion
let's do something between Power
Platform and business Central and show
you an application lifestyle management
story in both worlds
regarding to my beer tasting app in
business Central as well as in Power
Platform
in the last workshops I have learned it
is not so new or it is mostly new to you
how to set up such Gamo environments for
the reason here's a screen where shortly
explain to you and also recommend to do
this to use the Microsoft customer
digital experience I use this normally
to set up my demo environments and I use
for this Dynamics 365 customer
engagement
this is because there are all licenses
which I need especially for Power
Platform
furthermore I can set up here more than
one environment in Power Platform
and the other stuff Business Center is
easily attached because of I need also
for a complete application lifecycle
management Story 3 environments
enough for the prerequisites let's go to
business Central Development process
should be familiar to you for that
reason I don't have to introduce you so
much for my demo app I can use
standard objects like item table
contacts
standard apis like the items API or I
can also extend everything
he knows this because of you are writing
apps
I'm not the best consultant for that
reason I always
create my demos by extending something
with some minimal minimum impacts for
that reason I have extended the items
table items pages and so on and have
added also an additional API because of
I want to add some more data and resize
some data in my PowerApp it's not so
complicated it's just an API page which
you have to add
hunt
well I want to store my PR and my
speakers in this
data database tables
let's go on
how does a normal application lifecycle
management process look in business
Central
you define your tasks in my company we
use our company tooling alpaca we set up
everything for that reason we start in
Azure devops ports we Define our backlog
furthermore we developed in vs code have
some Docker Automation and so on
include tests review the stat this code
during pull requests have built
automation create artifacts have our app
and finally for Alm you have learned
Define develop test build deploy
we need to automatically come on
wrong button
to deploy it let me show you this very
quickly here at my demo environment
another question how to move to the
opposite
yes you should see something perfect
this is my devops backlog with some
tasks
nothing special I have used the stories
I have written code for that reason I
have repositories
when this repository loads containing an
app containing a test app with some
source code tables queries whatever
nothing special to you feel some more I
have built automation some Pipelines
you'll see I use our own set of
pipelines it compiles my app afterwards
this app is stored as an artifact in the
artifact feed and furthermore
we have released pipelines to deploy my
app
to
my environments you'll see there are a
couple of deployments still there I can
go to quality insurance say well I have
tested it please deploy it to the next
stage and it starts immediately after I
give my approval
nothing new
and business Emperor well I have one two
three four uh one two three environments
production quality insurance and user
acceptance test
let's move to business Central and see
if an app is installed I go to the
extension menu
extension management
and there should be an app best beer
let me make it a little bit
bigger here it is perfect
this is nothing new to you because of
its in standardized process
I use a backflog Define my user stories
develop build my app automatically test
my app automatically
deploy my app automatically
and furthermore I've shown you the
result there the app is installed
strong process fully automated
what is this Power Platform
and
to dig into this
chapter we have to talk about
also citizen developers because of
mostly say develop power apps and power
automate flows
Microsoft have designed this technology
to give our customers the possibility to
create software
around our products and around our
customer extensions
from
perspective of a citizen developer it is
a very minimized endless loop between he
starts with an ID maybe at the backlog
he developed something on his computer
in Power Platform and he uses and share
this app
nothing else
it's also application lifecycle
management because he improves
everything afterwards
as a pro developer I want to have more
this is a reason why I use alms
accelerator for Power Platform I want to
have source code management like in
business Central I want to have
pipelines also like in business Central
to deploy my apps
because of this gives me the freedom to
rely on a stable process which is
automated
let's look again
to Power Platform and to application
lifecycle management
and Power Platform you might have seen
when you look to your own environments
there's just the default environment as
our customer site it's the same story
the default environment is still there
because it comes with others
you might have the possibility to use
some connectors there
or some connectors are blocked this is
depending on the it guys
which might have set up a data loss
prevention policy
so they have restricted something in
this environment
for that reason larger companies
have for sure a need of different
environments
for instance for their sales department
they want to do a lot with Twitter and
so on and tweet every day and new
opportunity the finance department needs
access to business Central
because of save some invoices stored on
OneDrive and whatever and they want to
automate things you see the combination
between business Central as well as
Power Platform both can go hand in hand
furthermore we have production
this is a very
yeah or should I say
it's a critical environment because of
we
do something with our manufacturing
execution system based on the data of
business Central
or for instance HR they have
confidential data
for Alm
we need R we need three environments
because of we want to separate
everything we want to separate
development from test from production
this makes sense because of as a
developer I have learned
I do my things in my isolated
environment afterwards I ship my app to
the test environment I test it with some
test data and furthermore I ship it to
production where it is used
if I find any problem I go back to
development fix this problem and roll up
my app again
like we do in business Central we don't
do anything in production and fix it
there
I hope you don't do this
in conclusion money apply this
environment strategy to the Departments
of Power Platform for instance for sales
say do something worse business Central
and dataverse so we need share also
three environments in HR the same story
here they are using just something in
dataverse
and finance
they have mostly Business Center but
they need also three environments
for data rules to apply a full
application lifecycle management story
another issue might be the development
process of a citizen developer
it is easy to create a power automated
flow it is easy to create a canvas app
and easy it is easy to use a flow
outside or a flow from a canvas app what
happens is you have in between
a dependency
and citizen developers normally start by
deploying things manual because of say
export the flow import the flow inside
of the test environment what happens is
they might break this dependency in
conclusion the PowerApp in test
environment doesn't work anymore
so you have to go back
bring over the PowerApp from development
to test
this might work for one power up and one
power automated flow but trust me not if
you have 20 flows
for that reason you need
something else
and it's a construct which I guess is
well known for us in business Central
in database it is called solution a
solution is nothing else
sent in business Central an app it's a
wrapper
where you can put in your components
like Timeless apps flows environment
variables permission sets and so on a
lot of stuff
furthermore you see here a solution have
a publisher a prefix unique name version
sounds to me like an app manifest
in database this is called solution
manifest so you describe your solution
to others
mostly not known
for those who start with canvas apps and
power automate flow
it was also not known for me as someone
told me here's a solution to transport
everything
Solutions can be managed and unmanaged
and let me shortly explain it a managed
solution is a sealed package it is just
used to install something
you cannot export a managed solution
from an environment this is not possible
for that reason you have unmanaged
solutions for development this solution
can exported either as unmanaged to
restored afterwards or to
as a managed solution to transport it to
the test environment or the production
environment
furthermore during the installation
process of such a solution all
containing
customizations and components are
applied to the Target system which means
if you have changed some tables this is
applied it's the same story like in
Business Center nothing new
or
so
you can install and uninstall such a
solution from an environment after
during uninstall
everything is removed and you have
dependency unfortunately not so good
like in business Central where you can
define a dependency to another
solution this isn't there
you must ensure that everything what you
have used inside of your solution exist
in the Target environment
let's look to the deployment process
with Solutions
remember before we add here this single
canvas app to slow with the relation in
between and the deployments a deployment
process with Solutions is to be honest
much easier because of you ship the
whole package from one environment to
another environment
the relation in between still exists and
you can test it as a whole package if
the something in the package fails go
back to development
fix this problem and ship it again
sounds for me as a good solution
let's go to my peer testing demo app
first of all I've shown you I have still
installed the Business Center app
in business Central it is here but there
are no beers no items no contacts
I'm not ready for test
for that reason I have decided
I need
something to put put some data into this
environment I have three environments
I would have to end at
I would have to add at least a couple of
Records 51 speakers few beer can as
experience
to each environment manual it's not
option to me for such reason I do it
automatically I use a power automated
flow to import data in Business Center
and
to do this
I have set up this flow right in my
development environment in dataverse
and I use
here some data based on Json
to show you this
let me shortly
again introduce my manual development
deployment plan I have my development
environment and I ship my solution from
development to finance and
Sierra I run my flow to import the data
into business Central
to do this and give you some more
details here
inside of my power automated flow I use
the connector from Business Center you
have seen it in the Keynote
when I go to this connector
it asks me about an environment name and
an environment and then company name
furthermore I have to select an API and
the table
when I do this you see there are some
fixed values like quality insurance for
my
QA environment where I develop against
currently and Chronos us Inc
I guess it's not a good choice to
include this fixed values in my solution
because of
when I ship it to the other environment
it should also point to the respective
this and Central environment as well
the rest the API beers and so on this
can stay because it's related to the
same objects which I have in the Target
environment
to solve this problem
Power Platform provides environment
variables
and this is this might be new to you
if you use canvas apps or
power automated flow environment
variables helps you to make a solution
configurable this means you have a key
value pair what what is requested during
the import process in a Target
environment you can specify CR the
target environment for some more
you have seen this connector uses a
connection to my business Central which
I Define during the development process
in power automate this connection can be
abstracted by using a connection
reference inside of my solution and this
connection reference itself is must also
be configured in the Target environment
well
let's do this solution
environment variables for my solution
are business Central environment and
business Central company
I use the type text you see here a short
screenshot of this
and furthermore I have added
the values for this environment
variables inside of my development
environment in Power Platform
furthermore
this current values are currently
included inside of my solution for that
reason I need to exclude them because I
won't ship them with my package to the
next environment I want to configure it
in the Target environment
the same story when I use it here
you see the same connector like before
but for the environment name I have just
used this environment variable this is
only possible when both is inside of a
of a solution
and you access this environment
variables easily by clicking on this add
Dynamic content it is presented to you
this means we are able to build
software in Power Platform
which is configurable with which can be
shipped to another environment because
you can set up something
and this is important keep this in mind
the same story we have here with the
connection the connection is just there
and now we need to set up the connection
easily for this
solution
says three bubbles
right at the connector and you see down
in this red box here is my connection
reference which I use
inside of my connector
sometimes when you add some components
two-year solution you must adjust this
so that everything works
and finally I have here a blueprint of
my
power automated flow it shows you on the
left side I set up some I can't read it
I set out some beers on the right side I
set up some speakers the same procedure
first of all I use the standard API from
Bristol Central to search for contacts
or items if they exist I remove some and
afterwards I use the business Central
action to import this information to
save a record or add a record
and finally I want to roll it out and
let me show this more in detail here
what I have explained right now for that
reason let's move back to my Power
Platform
okay
let's go to my solution
and wait a second
let's show you all components of my
solution
you see here a canvas app this comes a
little bit later in place
I have here my connection reference
regarding to business Central because
currently it is using my local
development environment
information
and I have two environment variables the
company as well as the environment name
of the target system
let me
code shortly check
you see no
value is there because of I have
excluded this value
when I go here for instance again to add
it will immediately appear because the
value is stored inside of this
environment
let's cancel this because of I don't
want the ships us
and furthermore I have here my power
automated flow let's check this in my
current environment to run it and we
will see
it needs maybe an
approval from my site
Randall slow
fine
and let's wait a second there it is
this run
on the floor one just goes down a loop
over some beers here's the experience we
say it's not completed because of it is
transporting data to business Central
afterwards this data will be there
okay
let's check this here and this is
Central
if I have some speakers at my QA
environment
and goes there
speakers are there perfect
sounds great to me
let's export my solution
and ship it manual to the next
environment for that reason I go back
here
go to my PC take this demo say export
and well I could also again publish my
changes I did this before because of
this takes some time and click on the
next button I want to export a managed
solution because of I want to have a
sealed package which I can install in
the next environment
and click on export
run the export starts this takes a while
for that reason I have prepared it with
a previously export and let me open
another environment maybe this one
and try to import my Solutions there
perfect
I go to import solution
browse it
let's see here was the previously
exported solution as a managed solution
and I want to use it
go to the import file I would say it is
already installed damn
let's
use another environment
don't panic
let's use this one maybe
also not working damn
you have to trust me I have to select
there
the
environment variables and I have to
set up also my connections for this
connection references
well overall this is a
good process
but it is still manual my currently
PowerApp is still in production it will
become later into play
it is a kind of application lifecycle
management because I do something manual
I export my solution I import my
solution but this is not a real solution
for Power Platform and not what I want
to have
what I want to want
for that reason I need
source code management I need automation
for my solution transport as well
and
you are here to see what means
professional application lifecycle
management for Power Platform
and this is related to
a tool where we can both go together the
citizen developer with the minimized
manual workflow and me as a pro
developer with which is the master of
the test environment and production
device environment because of I rely on
source code Management on code review
testability and automated deployment
so let's give this citizen developer a
handshake and use the aim accelerator
for Power Platform
you might make a picture of this links
I can strongly recommend to go to
Microsoft docs there's a lot information
about the setup about how to use and how
to implement this process automatically
feel some more
furthermore this package is open source
it is from Microsoft it is part of the
center of excellence it was created from
the powercat team this means the Power
Platform customer as a Liberation team
from Microsoft
and if you find some problems please go
to GitHub
report send issue issue request the
feature or improve this product it helps
a lot because we all need such software
to align a completely automated
development process for Power Platform
when I set up this tool I need to do a
lot in
mostly everything what we have I need to
do something in database I need to do
something in Azure devops as always in
Azure because of all systems must talk
together
over the LM accelerator for Power
Platform
but don't worry you need also a lot of
Rights
and
you have to compile currently the tool
which is included inside of the center
of excellence it's the soe CLI
this tool helps you to install
everything and yesterday in my workshop
we run this tool unfortunately we failed
on the rate limit of GitHub because of
everyone tried to download the things at
the same time from the same IP address
to show you a little bit more about the
installation process it's just a command
line
which you have with the Siri CLI you see
here a short dialog which opens and
collects some information about my whole
environments
I need to specify some names for
security groups I'm not also collect
some URLs I must to point to my Azure
devops environment because it must be
there I have to specify where is my
pipelines repository and so on mostly
it's click enter click enter click enter
using the defaults
are you just later some of the Json
information
what happens during the whole
installation
you see here dataverse
serious resolution which is imported
it's the tool it is
a solution inside of dataverse something
for our citizen developers which are not
able to do something in Azure devops but
they are able to click a button to
invoke something
furthermore
it Imports CR user which is used by
Azure devops because of shares the
automation
and this automation needs also
repository where we can the source code
of canvas apps power automated flows
data boost tables and so on
when I have a source code repository I
want to build an app that means I have
to sell also some pipelines and these
pipelines uses connection to debit
levels to import the solution
automatically as well as to export it
previously
I have also to set up some branches for
the full development process
in Azure we have an app registration we
have a security group which is used to
add some persons which can use this tool
finally you have here something in Azure
you have an app registration you have an
aad group
where you can share this tool with the
makers inside of the Power Platform
and you have the playground of the mega
this is a canvas app which invokes
something
at Power Platform
and invoke something in Azure devops to
start all this automation
and obviously you have my Pro develop
playground the automation so I have
nothing to do everything comes out of
the box everything is installed
configured
and ready to use
what I now have to do is to teach this
process for such reason let's talk about
what does it mean professional
application lifecycle management for
Power Platform and using this tool
what
do I have to do to explain to a citizen
developer or someone who is only
in active in the Power Platform I need
to explain
professional development I need to
explain how you can use this automated
deployment and I need to empower him to
collaborate with ourselves
for that reason
professional development you know it
from Business Center it needs to start
on a clean isolated environment
you need to restore
your stuff based on code
furthermore I need to store all my
changes frequently because I want to
have a backup of it
in Power Platform well we have a canvas
app it's inside so now I need to take
this canvas app outside of the Power
Platform and stored in the repository
because there is a source code
and last but not least I might have to
clean up my development environment
before I start developing something else
in detail
this means the source code is inside of
my cheat Repository
task is very simple I need to restore an
unmanaged solution based on the source
code and import it into this Power
Platform
this
solution contains here a canvas app
later
my maker starts to modify everything and
he adds maybe a power automated flow
so this is the time where he needs to
store everything again this means he
saves his unmanaged solution and
something must be there to automatically
extract the source code from the
solution and stored in the repository
but to be honest no makeup will do this
manual
finally I have told you we need to
remove everything
clean up
the secondary story automated deployment
you know this needs a little bit
preparation
unfortunately you haven't seen it said I
have to have to configure my environment
variables during the import manual
when I have an automated import for that
reason I need to prepare it before I can
use an automated Import in any Target
environment
I need to look at my solution and say
well
what connections do I have in my
development environment
and there's more I must go to my target
environments and set up everything set
the connection references are there as
well as the environment variables that I
use are
correctly configured
furthermore when you know
how to use or how to develop power
automated flows said come be in place as
a
there's also the the necessary
to specify an activation user or to give
it a proper owner in the Target
environment
in detail on left side I have my Power
Platform development environment and I
need to look at this environment grab
share the configuration information
put it down to Azure devops to my
Pipelines
and finally this information will be
used during the import in all of my
environments
sounds easy
let's see what the tool
can do for us here
for that reason let me move to the tool
and it is here
you have seen it before
there is my maker portal
to do everything
here on the right side I can select my
environments
currently I'm in the development
environment
perfect
furthermore I can commit here my
solution
and save it trigger something to put it
down to my Azure devops repository and I
feel the possibility previously to
configure my target environments
he will see after this
tool analyzes my current solution in my
development environment there are a lot
of options here
regarding to the next environment
currently it's selected validation so
change this for instance to production
and look at this environment what
information must be configured there
you see I have my business Central
connection reference this must be
configured I did this before I have here
correct
connection I could create a new
connection or I can send an email to
someone who have the rights in the
Target environment to set up such
connections because of
maybe I do a solution for HR
the solution I cannot access the
productive system in HR I have no rights
they are confidential data of our
employees for instance
so I can tell someone else please set up
a connection for me in this environment
go back to environment variables well
you see Company ID is still there and my
business Central environment is set in
Target environment to production
look to our canvas app
I want to share this canvas app and I
can use here a team which I can create
in my target environment
furthermore
here's my created team I have gave him a
name BC take this and I have attached
also an Azure Active Directory Group
in to this team
furthermore you see here some roles this
is these are security rules how to work
with stator
I have an own security role inside of my
solution because of other I access data
and we have added the
basic user role and I guess this is
currently a bug
so they chose both
but I'm pretty sure set save will change
this in the future
fixes and finally I have my flow which
have an owner is shared with the team
and have an activation user
if I have 20 flows here
I need to specify the order of
activation I can do this
because of the automatic process will
run all the stuff
and activate the flows in the Target
environment for me this saves me a lot
of time
furthermore let's commit my solution I
have done my development my power app is
perfect
let's say uh busy Tech
days and
well let's say this is user story to our
work item number two
I stole my information in my own Branch
based on another Branch okay it is here
we have to look at this later
and finally I need to come on
commit this solution what happens in the
background is
a command is sent to every devops
let's see
here I have a timer symbol
oh I have a build pipeline
export solution to git
question is this complicated for a Power
Platform guy from maker no
finally this pipeline starts and runs
and will export my source code and store
The Source Code inside of a gig
Repository
my whole Power Platform stuff is stored
automatically
let's go back
to my slides
and move on
furthermore we need collaboration
collaboration starts mostly in
Azure devops Sports
we need to align to other development
like in business Central we have an app
in Power Platform we have an app in
business Central to user stories both
must be traceable
I must also see what happens Jesus use
the story
I have commits inside of my git
repository and you know from Azure
devops this commits can be attached to a
user story
it's collaboration
but on Power Platform we might have more
collaboration especially when we have
large Solutions
and to develop together in one camera's
app isn't a good thing currently
I guess Microsoft will approved this but
what what you can do is collaborate on
parts of the solution
because of you have two makers everyone
have an own developer environment
everyone uses the base solution to
restore share
make some changes and bring it together
into the kit repository by committing
stuff
and with a branching model we can merge
all this information together to build a
new
solution and then you solution
whether it's
done can be rolled out
let's have a much deeper dive and
hopefully you are not
too scared about when I talk
about professional development because
of
we have git repositories and git
repositories are for me the single point
of cruise it is source code stored in a
central point we have the team
repository and we might have some cloned
developer repositories we bring things
together we need to manage this
and to manage this we need also to have
a controlled way to do this
you know I have a lot of repositories
and I have a lot of environments
and to give you a brief overview how the
branching model for Power Platform
belongs to the environments is here a
short
overview
the main branch is still
still related to the Target environment
the production environment this means
every commits here can be used to create
a solution which is similar to the
solution in the production environment
furthermore for each solution you use a
solution branch
it's respective to everything what is in
test environment
it is normally used to stabilize a
solution until it will be rolled out to
production
and you have seen previously my
development is isolated and I did my
commits to my developer Branch based on
a solution branch
again this is something was what must be
done by the maker because he defines
when he is ready for that reason let's
go to this tool and see
how you invokes this process there
oh by the way my export is done
automatically
for that reason
I can start the deployment to a Target
environment
I create a pull request here let's give
it a name
PR
mme
some release notes yeah do some great
furthermore
I use my developer Branch into my
solution Branch this means I want to
roll out my solution to the test
environment let's deploy its here
hmm
seems like working
let's have a closer look
ah
I have a pull request
and what you see also here is another
pipeline run
it's a validation
invoked by a policy because of my source
code is now merged with with the
solution branch
and must be validated in a separate
environment the validation environment
for that reason this pipeline Imports
D created solution directly in my
validation environment so Stakes also a
while
and let's use this time to explain this
process
behind the scenes
we have created a pull request this
means this pull request was triggering a
validation pipeline this pull request
uses the source code to create a managed
solution which is automatically imported
into the validation environment
when I complete my pull request or I
complete also the review of the source
code
in case of canvas apps it makes
sometimes sense
then I create a final commit on my
solution branch
this triggers again the next pipeline to
roll out into my test environment
because of every source code commit
inside of my solution branch is used to
import the stuff into the file
environment my test environment
and
when I have stabilized my solution I
create a pull request for my solution
Branch into my main branch which
triggers also another pipeline another
deployment pipeline
to import the solution into production
perfect
what's about multiple Solutions and the
concept from Microsoft
to this tool is well you can store
multiple Solutions in one Repository
because of there are some rules
each solution is stored in an own folder
furthermore each solution starts from
the main branch
think about the branching model each
solution have the same branching model
the same rules
have its own pipelines to import
furthermore
these pipelines are triggered by changes
related to the solution folder
in conclusion
we have the validation pipeline
respective to the validation environment
and the deployment pipelines for tests
as well as production nothing else fully
automated fully out of the box
by setting up this tool and you have a
complete automated
development environment in Azure devops
for your Power Platform and you have a
canvas app to trigger everything
well my solution is now exported
imported
and deployed based on this tool from my
side it's well definitely a strong
process
it's an easy one to transfer this
solution is from one environment to
another
let's look to my beer tasting demo
because of it should be in my target
environment
and for such reason let's go to my
test environment
because of I have created previously
there a pull request
and let's see what happens here
come on
is he also this error message I am not
allowed to change something in my target
environment because of I have a managed
solution
let's go to my power automated flow and
opens this and runs this
to get some data into my target
environment to my test environment
and
click on run
perfect done it runs and imports some
data into my target environment as I
expected I have rolled out my software
automatically
and let's go back and start and play my
power app
well
allow the excess
come on
let's give it a retry
let's say five
perfect
there it is
and my speakers are here I can select my
speakers go to someone of them let's use
AJ I guess he likes to drink beer
and let's choose a beer kind
huh let's use this one and
I guess this tastes very well perfect
submit this data
go to business Central to my
test environment user acceptance test
and see
what AJ have rated
I go to my speakers
well he is here and let's see
we have no rating what happened
let's go to my QA environment and see
what is there
let me see this is the wrong one the QA
is here
perfect let's go to the speakers
again
go to AJ
and the rating is here
what happened I have configured
everything but I have missed something
currently the connectors in Power
Platform does not support
the
switch of an environment
you see here again my setup
and what happened is the canvas app uses
still the business Central connectors
they are bound directly to the initial
environment to the quality insurance
environment this is a huge problem
and
good thing
we can fix this
by doing two things one thing can be
done by Microsoft to fix this problem
and allow here environment variables for
custom connectors because of you see
here also in this slide it is directly
bound to this environment and to this
company
and recently I have raised an ID at PC
ID and have seen it is planned for 2023
wave one so this will be fixed in the
future but it would it would be a very
bad end for my presentation
for that reason I was also inspired last
week by the New Kids on the blog the
virtual tables
and this setup is a little bit different
a virtual table is in dataverse
a physical table of dataverse for me for
my canvas app and therefore I have clear
connections
in conclusion I need to change my
connections to Virtual tables
let me go to my power app and do this
very quickly without developing things
now I have virtual tables
and to show you the same stuff after it
have reloaded here
just give it a second there it is let's
use AJ again and use another beer
this one
and well only three stars
submit this data
perfect
go here to business Central to my
quality and to my user acceptance test
page and let's hit refresh and now the
data is correctly delivered in the right
system so you see it is possible to
change the connections also for canvas
apps power automated flow is not prop
not a problem I can't use their
environment variables
let's go back to my slide
and finally
talk about
this story you have seen application
lifecycle management for Power Platform
is definitely possible
it is possible in both worlds
you can automate things
you have a standardized software
development process
canvas apps for power automated flows as
well as for our well-known business
Central products
you have also learned in the Keynotes
you can combine both worlds together by
the new action where you use a power
automated flow you can put something on
appsource as well
for that reason we need also a stable
development process here and this tool
brings this development process to us on
the right side we can
accelerate the development by using the
common products one was from my own
company is Cosmo alpaca one is from
Waldo's company it's Al UPS or we use l
go for GitHub it's up to you
but you automate your development
process in business center and when you
go to Power Platform we have can have
the same automated setup and the same
automation
with Azure devops with the full
traceability from backlog defining a
user story
committing changes to a repository
automatically build a solution and
deploys a solution over three
environments
it's nothing special
and you have seen with a little bit
magic in between there's definitely love
between both worlds
finally
application lifecycle management is
definitely
needed because of it is not only
dataverse or Power Platform which have
databases
development test and production is also
business Central
we have the same
setup
Both Worlds have the same standardized
process
Both Worlds can exchange data between
by us using connections or using virtual
tables
furthermore we need to deploy
automatically
and aligned our software from the
development stage into the test stage in
the Deep production stage
it is something to do professional
thank you for listening and I hope you
enjoyed my presentation
I'm already here to have some questions
and answers for you other doesn't mean
that I question you you might question
me and
here are also some
URLs where you find my blog posts or my
LinkedIn profile
throw some more I have this nice boxes
so they can send it over to you do we
have any questions
can you erase your hand
[Laughter]
let's bring it up to him
yes you can do it yes thank you actually
I have two questions the first is
um
does do virtual tables work over
multiple companies I once set it up but
I had problems to connect my virtual
tables to different companies in
business Central and I wonder if this
works already or is it a limitation in
the virtual tables
do you know that
let me repeat
um you want to know if it is possible to
have the same virtual tables pointing to
several companies yes
uh what I have learned during the setup
of the riddle tables there are two
points first of all you need the same
base currency
last weekend I have had to refurbish my
whole demo environment to
set up everything
and I have furthermore learned the
virtual tables from one database
environment only shows to one company
inside of business Central you have seen
here I have a setup of at least four
environments in database I have
development I have validation because of
I needed this for a policy I have test
environment and I have production
environment but I only have three
environments in business Central because
of I can only set up three environments
in a trail version
what I have done is I used in one
environment
the Chronos company and my company to
set up the video tables
so to answer it I guess the virtual
tables are pointing direct to the data
of a single company
nothing else
okay thank you and my second question is
I wonder how you handle a Dev test and
life environment in combination with
SharePoint because a lot of our flows
uses the connection to SharePoint but
it's harder I guess to
um
to maintain a test SharePoint
environment so I wonder how you
maintain that our SharePoint is not a
problem SharePoint have a connector
which can be set up this environment
variables because of you can set up for
SharePoint especially environment
variables
as data type data source so you can
define a SharePoint list as well as a
SharePoint site
what you have to do is you need to use
this information in your power automated
flow or in your canvas app
the second thing is you need
a test environment well in you need to
create a SharePoint site for development
a SharePoint site for test as well as
for production
does it answer your question
a bit
um
you should create a site for uh testing
and a site for developing but what if
some flows create new sites
uh because then I would suggest uh maybe
for some
[Music]
um how it's called use a prefix like I
create this as death so Dev side x death
set
in the name of the site yeah okay that's
how we do it right now but it's
sometimes a bit complicated doing that
for sure
okay thank you
and come down to grab your shirt after
the session anyone else
please please
sold to him
perfect
I don't know how Berlin this is but I've
been struggling with BC and powerapps to
connect to um
two pages to develop powerapps and it
seemed that I could not publish it as a
web service
I needed to I don't don't know if it's
called entities or something you need to
create a table
now instead
so um
so
do you understand the the complications
there because I could not just publish a
new page
so so you was not able to publish in
business Central and API page right
I could not connect to it through
powerapps
um let me answer in a different way in
My Demo I have created in business
Central and API page this is out of the
box available after I publish my app
because of it is part of the standard
API of business Central
and I can can select this new API in my
connector you have seen previously this
screenshot where I have the environment
name
the company name and underneath I can
select my API directly and afterwards
from my API The Entity
this shouldn't be a problem if you have
some trouble with this I still recommend
to create an issue at Microsoft or
contact someone from Sam to fix this
okay might be
something blocked but it should work
okay
your phone yeah
right here
um the tool that you showed does it work
for GitHub too or only for devops
these tools are currently working only
for devops
whoop
don't sleep
hi yeah my question was
um were these like SAS connectors or
also work for on-prem
the ones that you showed us
can you please repeat it were these the
the connectors that we saw for the
business Central this is the connector
for business sample for the SAS or for
this is just the connector okay voila
let me go
pretty
short to my environment and let's go
back
here to do my development environment by
the way
you saw here also
the setup of the connections in my
canvas app as data the native
connector from business Central
and underneath
the virtual tables which are part of
database right now
you see here
this are my connectors regarding to my
API and these are
the tables which are brought in by setup
table drill tables
when you add data here like
say business
Central
come on
you can choose the connection perfect
and afterwards you see here
a lot of apis
when you have selected your current
company
and in my case my API from my
application appeared immediately here
inside of this list
let's see
here and you see here Cosmo slash busy
Tech days slash v1.0
okay and then I would say the the
on-prem is then the separate connector
then they have I didn't I didn't write
your on-prem connector because of I
don't have any setup for this yeah all
right
thanks
anyone knows
so thank you for listening
[Applause]
and please return this wall
[Music]
