# NAV TechDays 2016: Building the Dynamics 365 for Financials service

- **Source:** https://www.youtube.com/watch?v=hpQqWEiX0IE
- **Video ID:** hpQqWEiX0IE
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 83m15s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

hello everyone hello welcome to our
session building the Dynamics 365 for
financial service my name is camil
klanga and I'm software engineer at
Microsoft Development Center Copenhagen
and I was one of the team members who
created the service and brought it
online of course with a great help of
all other teams in Dynamics Navy
organization and welcome also my
colleague hello I'm costantin danil
camil's colleague and we're excited to
show you what I have been working on and
again thank you very much for coming we
know this is the last session so it's
really nice to see so many of you and uh
as we said a lot of people worked on
what we're going to present today so I
think it's a really great privilege to
for us to be here today and to show you
our work so we really hope you will
enjoy
it so let me tell you a little bit about
what our today's session objectives so
of course we'll start with telling you
why we build the dynamic 365 uh for
financial service I think Vincent and
Thomas told you a little bit about this
during the keynote we'll try to tell you
a little bit more uh so you get a better
understanding on on why and after that
we'll switch more to how so we'll give
you some insight into how the service is
built uh something definitely more
you've seen before uh some some things
might be not a surprise for you in terms
of how it's built some hopefully will be
an interesting thing to listen
about and afterwards because first we'll
talk about the entire service then we'll
concentrate on the nav because it's
really at the heart of our service so
we'll explain what kind of changes we
made in the platform so it benefits not
only the uh the service itself but also
all the installations on Prem and those
of you who run it on cloud definitely
will also benefit from all those
changes afterwards as you will already
get a really good understanding on how
the system operates will concentrate
more at the runtime of the service
and particularly we'll tell you how we
monitor it because monitoring was one of
the most important aspects of the
project we put a lot of effort into
ensuring that we know 24/7 what exactly
is happening within the system and of
course Q&A at the end so feel free to
ask us any questions we will be also
available to answer questions after the
presentation and I think also tomorrow
so absolutely we truly hope you will
enjoy
it so why was Dynamics 365 for
financials built there are many reasons
but the most important one was that we
wanted to empower every partner and
small and medium business on the planet
to achieve more you may ask yourselves
well what does this mean
specifically to find out the answer we
must look towards the future but we must
also gaze back on the past specifically
nav's past and anyone remember these
days the DVD era thank you very much so
let's remind ourselves of how the
process used to go well we and Microsoft
would work on the newest version of nav
and when it was done we would ship it to
all of you the partners so you could
work your magic and you did you created
amazing verticals which satisfied
particular needs for small and medium
businesses around the world but once
your work was done how would you get
your IP to the customers quite often you
would have to engage Eng with them and
you know go over there so you can help
them with the deployment and setup
process and if we were to remember this
era there were let's say a three-year
delay between Microsoft releases and
then we switched to one-ear Cadence but
even so it took a lot of time between
the moment when nav would actually be
out and then it would be in the hands of
the customer months you know perhaps one
year and in today's day and age this is
not enough in order for customers to
stay comp comptitive they need the
latest tools and technology so this
process needed Improvement and we took a
step back and fought to the very
building blocks of the
process we had Na and we had the
partners and what was the major pain
point the deployment process it was long
and it was difficult so we thought how
can we improve this and we turned
towards the cloud so we created a a tool
set I presume some of you remember it
and using this you deployed virtual
machines in Azure these virtual machines
had nav and SQL Server installed on them
and customers could just log in and use
the product and so we moved from the DVD
era to the infrastructure as a service
era but still this was not enough we
needed more we needed to evolve yet
again and become even more efficient and
so we gave you the Dynamics manage
service for partners and entered the
platform as a service era who knows this
who has used it thank you okay quite a
few of you so let me guess give you a
brief explanation what it is using this
a partner can upload their application
and then they'll deploy application
tenants and in this tenants customers
from around the world can log in and try
the latest version of their application
and it offers a bunch of useful features
while having this familiar nav interface
which you're used to and and although it
is very efficient whenever you launch a
new version of your application you need
to create a new application service and
move your customers to it and even with
this let's think about our
customers how do they actually get their
hands on nav today well they engage one
of your partners and explain their
specific business needs and after that
you know you have to sit down design the
solution coded give it to them or upload
it here and create an application tenant
and only then can the customer actually
use
nav how much does this process take a
few days you might say a few weeks but
we live in the world of the now now now
we cannot have customers waiting so long
they just want to be able to use nav in
mere seconds and they cannot do that
well actually they can welcome to the
new world welcome to the Future Dynamics
365 for financials is nav as a software
as a service it is the new branch of our
product and it is Microsoft solution to
bring nav into the hands of every small
and medium business around the planet in
mere seconds you may say well that
sounds impressive but how does the
process actually work well allow me to
guide you through the customer's eyes
some of you have already seen a preview
of this when Vincent did it this
morning as a customer I go to our
website where I can find out information
about nav and why is it suitable for my
business and then once I'm satisfied I
click on try it this button right
here I'm taken to this page where I
enter my Corporate Office 365 account
and after confirming my
identity I enter my user information and
company information I then click on
start and I'm here this is what we call
the landing page and this thing loads
and in just a few seconds boom our
customer is already in nav and is the
financials application they get this
nice welcome experience which is like a
tutorial of our most useful features and
they can already you know start
modifying items posting sales invoices
and running their
business so just to give you a very
brief overview of our process there's
the
customer there's the Walk Drive I showed
you again they use their Office 365
account which as you know is stored in
our Azure active directory which is the
place where we have all of our corporate
and personal accounts such as Hotmail
and even our landing page The Wanted
showed you query's a and a sneak preview
of course some magic happens in the
background with a sing demon in our
service and in just a few seconds as I
said the customer is in the financials
applications but as you can imagine this
is a General application right is the
same for every customer so some of them
has specific business needs what happen
when a customer Encounters this who do
they go where do they turn to well the
answer is appsource and this is where
you the partners come in this will
contain your code you shall write
extensions and put them on appsource and
customers will be able to enable them
and thus they will solve their
particular business needs think of
Dynamics 365 or financials as
Microsoft's way of bringing the customer
to
you so we have seen how we can get from
a website into nav in just a few seconds
and then we have app source as our
phones have the windows store nav will
have app Source but there has to be some
magic happening in the background right
how do things happen here to tell us
thank you very much so I think my
colleague really nicely presented you
our journey where we started with the
DVD era and then we improved our tools
and we took more and more tasks to
you know really not a problem for you
you should more and more concentrate
just on building your Solutions and less
and less on the entire infrastructure so
in SAS when we look at the SAS I think
we'll start explanation with uh
presenting you the entire Dynamics 3605
family so those are the services that
currently are available in the in the
suit and you can think of this more like
Office 365 but in terms of the C CRM and
the Erp software so you can expect
exactly the same seamless experience in
all of those pieces of the of the system
so the UI should be similar to all to
all of you in all the software within
the package you should it shouldn't be a
problem to switch between those they
should cooperate nicely all together and
of course with other Office 365 services
so the nav with a great functionality
with all the integration we worked on
during you know couple of years with
Office 365 team and Azure team it really
enabled us to became part of this family
but today we'll particularly talk about
the financials module so again we will
start with a really high level
explanation of the system we'll first
list all the components that uh is that
are present in the system and then we'll
dig a little bit more we'll go to the
lower layers of the stock so you get
better and better understanding of how
the system works so the financials
Dynamics 365 for financial service of
course it is built on a product we all
know and laugh so the nav is at the
heart of the system but there's 5
Seconds to sign up so we remember when
we started the project and Marco our G
GM came to us he said it it should be 5
Seconds sign up time so we worked really
hard in order to provide that experience
for you and again we really encourage
you to try it out yourself after the
presentation and that was one of the
goals extremely fast signup time
whatever must happen to enable the
tenant in Cloud it should happen
extremely quickly and in the background
and completely transparent to you so you
can enjoy the product and all the other
Dynamics 365
services and as we host the product it's
also always current so whatever we must
improve in the product or would like to
improve like introduce a new
functionality it almost immediately
reaches you as a End customer so when
you start using the product you you will
notice all the improvements along the
way there will be no delay as we as we
work on it it and there is shortest time
uh to Value both for us and for you so
for us if we want to extend the product
if we want to improve some functionality
or introduce a completely new one it's a
really short turnaround before the
customer is using it and thanks to our
great monitoring and Telemetry
information we can continuously make
that time even shorter and the upsource
so as Constantine already mentioned we
build the financials Dynamics spe 65 for
financial service but we also are
looking forward to work with you guys so
we can do your magic and build great
extensions so you can feel all the
requirements possible customers might
have in terms of particular
functionality and then again a rapid
feedback because this is an online
service we also have appropriate
feedback channels we extremely quickly
get it and we can extremely quickly
react to it again thanks to our
Telemetry pretty often we solve the
problem before it is reported we know
about all the problems if there are any
problems before the end customer is
affected so this is a really great
functionality when you run a a cloud
service like this and of course because
at the heart of the service there is
Dynamics uh and AV 2017 and 2017 plus
because remember we'll be upgrading the
platform and the app you therefore it is
powered by all the great features that
has been introduced into the product
like uh of course Azure infrastructure
because it runs on it but also the a
Azure machine learning Cortana
intelligence or powerbi plus all the new
features that will be will be coming to
the
product so we took a look at the at the
family of Dynamics 365 Services then we
briefly told you something you already
knew probably that it's all about nav
within the financials module now let's
take a look at the service itself so
we'll start with presenting you a list
of components and then we'll explain in
detail
what each component is responsible for
so you've seen already management portal
it was used in pass and what I want to
emphasize here while we work on the
product like this Dynamics 365 for
financial service we didn't try to build
a new components instead what we wanted
to do is to look at what we have
available that our customers are using
and our partners are using and we try to
use that functionality and improve it so
not only our newest sus service gets all
the great new features also the pre
previously released pass service also
benefits from and that's why we have the
management portal but but hugely
improved and therefore it's also uh used
in pass so more and more people benefit
from our work and that was basically the
kind of like one of the goals the same
for the platform changes when we made
the performance test and we saw some
places for improvements to make the
service even better and faster we made
all the improvements in nav platform so
whether you run on cloud or on Prem you
all benefit from our work so it's not
just s specific because as as it was
mentioned during keynote also on Prem
business is extremely important to us so
that was basically the one of the goals
uh while we work on the project so
there's a management portal then there's
of course a component which I believe
Constantine presented on a previous
slide that communicates with the aad
that's our connection point then there's
provisioning service and that one I'll
explain on the next slides and of course
there are clusters there are clusters
that hold the VMS with the nav deployed
and of course there are databases and
here there were also slight changes when
compared to pass we'll also get into
details so of course Azure secq servers
with both app and tenant
databases and we can't forget about
other services we are using so those are
just few of all the Azure Services we
are using in the Dynamics 365 for
financial service and you can see of
course there is one that we call new
features and because we are one big
Microsoft family we get in in touch with
all internal teams so we can benefit
benefit from all the new features that
are being introduced to Azure so not
only us and you and your customers can
benefit as well and that's why for
instance Cortana intelligence or Azure
machine learning is introduced into our
product this is thanks to great
cooperation between the product groups
within the Microsoft
so the management portal U you've seen
it in pass you can see it right now in
SAS what what is it well it is based on
the on the pass management uh manage
service for partners portal however it's
been we look we took a closer look at it
and we thought how we can improve it
even further so it can work greatly with
even bigger load because in s you can we
can expect much bigger number of tenants
as anyone in the world can possibly try
it out so we looked at it and we
redesigned it so it's pure UI you can
think of our portal as a kind of azure
portal but for nav resources so we try
to keep the the the stack extremely thin
on the portal so it's purely the our
database for the resources for the
information about the resources and the
UI so we get a nice overview of what is
deployed and we changed it so whatever
else like business intellig I'm sorry
business logic or the provisioning
engine we moved all of this outside the
portal so we kind of Follow That
approach that I believe Vincent
mentioned during the keynote to make it
more microservices based so it can
scales scale better when the under the
high load so it is the same portal but
redesigned for a higher frut and again
because this is the component we used in
pass also Pass benefits uh thanks to
those
changes then there is a s Sy demon so
sync demon is the component within the
system that talks to a so whenever any
of you signs up it gets the information
about the new customer coming up and it
reacts appropriately it ensures that the
new there's a new tenant ready for you
and when it verifies that everything is
fully functional it Returns the
information to aad then the landing page
gets the information from aad about the
completed provisioning operation so all
all of those components cooperate so in
the end you are directed to a fully
running solution within few
seconds but how does it happen that it's
all done within 5 seconds so uh one part
of the magic here is that we create the
buffer tenants so we have a pool of
tenants that we create up front before
you sign up so we have particular number
of azure SQL clusters we scale as needed
and we add more and more tenant so
they're always ready for you however of
course this is not the only thing that
has changed as you can imagine we need
to create appropriate database we need
to set up the tenant there a lot of
steps that we also improved as we as we
as we created the system uh a really
simple example for instance the NST that
is capable for detecting the new tenants
within 30 seconds 30 seconds wasn't
enough so we improved it so it's almost
immediate and you know like when we look
at the entire process in the beginning
the the process took longer obviously it
was in 5 seconds and then we were trying
to shorten the time more and more so
really like at the end of the of the of
the project really every second counted
if if we could save two seconds we did
save two seconds it became really
important for us that the process is
really short so the buffer T is when you
when you sign up the tenant is taken
from the pool and only really minimum
required reconfiguration is done to the
system so it is mounted there's a new
domain name assigned to it there's of
course some component information set up
and additional information provided to
the system so those those post
deployment operations are really limited
to minimum so it's done the fastest
possible
way and the buffer tenants are
provisioned automatically as the as the
pool size decrease and of course it's
dynamically either speeded up or you
know slowed down depending on the on the
rate of the signups and again we
improved also the way we provision new
tenants so we can provision in parallel
a lot of them and just to tell you it's
been a lot of test runs we did a lot in
order to improve it as much as we can
eliminate any concurrency issues while
creating U more tenant in
parallel and thanks to all this work
that was our goal we really wanted to
make sure that the time is not spent on
our infrastructure tasks while you sign
up we wanted the time to be spent only
on this on the systems to cooperate with
each other synchronize and react to the
changes happening so really those 5
seconds are mostly spent of course on
some finalized setup of nav but
meanwhile other operations happen so we
can we can state that actually the most
of the time is spent on propagating
changes into the um aad
service and there's a provisioning
service uh I mentioned that we improve
the management portal one of the steps
to make it perfect even more perfect was
to move the entire logic that can be
scaled better as a separate service so
we create so-called provisioning service
that became our Powershell execution
engine and because we use Azure service
fabric it is highly scalable under a
high load so for those for those of you
who haven't heard of azure service
fabric you can think of this as a
distributed system that makes it
extremely easy for you to create the uh
to create package and to deploy the
applications so basically it eliminates
any troubles you usually would have
while setting Azure VMS you worry only
about the up of course you need to
conform to some design special design
patterns while building the service but
if it's done right the service scales
extremely well and that's why we really
like to uh that's why we decided to use
the Azure service fabric for uh hosting
this specific component because it's
under high load especially during the
preparation of the tenants and during
entire process of uh sign
up so I explained to I think three
components but there is also also the
heart the heart of the service which is
the Clusters containing both the VMS and
the databases of nav so Constantine if
you could tell us more a little bit of
course so as Camille said the Clusters
are the very heart of our service you
can imagine that we have to run nav
simultaneously for thousands of
potential users so we of course need
multiple virtual machines on which to
host the product and multiple databases
to store the
information and we group them into
clusters because they offer two huge
advantages first of all it makes
everything scalable and secondly fault
tolerance if one of these resources goes
down the others are there ready to take
its place and thus ensure service up
time but there's one very important
thing about scalability it has to happen
fast at some point we can have thousands
of simultanous users accessing nav at
the same time while other points we can
have just let's say a few hundreds so
how can we ensure that we can scale the
virtual machine numbers up and down
adequately fast creating a new virtual
machine just isn't enough because nav
has to be installed on it and I'm sure
at least some of you right have
installed nav on a machine at some point
so it takes a bit of time how did we
make this installation go faster the
answer we don't install
any instead what we do is we use x copy
and and we push the necessary files and
dlls to those virtual
machines but as you may know nav has
prerequisites there's IIs there's the
donet framework and many others if we
were to Simply xcopy all of those
prerequisites and nav that would not
really be on optimization because it
would still take a lot of time but the
good news is is that the very images
those virtual Machines are made from
already contain those prerequisites so
when a virtual machine is spun up it
already has the components and we just
need to copy the files and dlls nav
needs and then based on the
configurations in the management portal
we make some last minute configuration
using Powershell scripts and thus we
have running nav on Virtual machines
which can scale up when need demands it
and down and thus avoid needless
resource
usage but the virtual machines aren't
the only thing we have improved a very
important thing are the databases and
let me take you to a small historical
trip of how we did it we initially
analyzed the different performance tiers
which Azure offers and we looked at
basic which is the cheapest one but we
didn't go for that we went for azero the
standard one and we created multiple
azero databases to host our customer
data but what is the problem we know
this in general happens for all system
with concurrent users you do not control
which database gets hit who knows what
users are logged in when at some point a
lot of these databases will be idle
sorry about that a lot of these dat
databases will be idle While others will
be simply hammered because the users
whose data is on them are logged in at
the same time and they will have a
suboptimal experience so we needed to
fix this what was our initial idea well
we decided to go for scale and we said
more SQL servers and more databases
probably more performant but think about
it is that really a
solution no that's not a solution that
doesn't eliminate the problem it just
reduces its frequency just because you
have more databases doesn't mean there
are still some who get hammered and
still provide a suboptimal experience
and the resource uses grows
exponentially this is not a real
solution so then we decided to take a
step back and think is there a better
way in which we can solve this problem
and fortunately Azure SQL came to our
Aid with an outof thee boox solution
which is awesome and we encourage all of
you to try it it's called elastic pools
let me explain you briefly what they are
you creates a so-called elastic pool in
Azure and you assign a number of dtus to
it dtus are database measurement
performance units and their metrics are
log rights input outputs and CPUs an
easy way to describe them is database
horsepower so one of these elastic pools
has a certain number of dat is assigned
to it and then you create databases what
happens when one of these databases gets
hammered so a lot of connections are
made to it automatically a higher number
of dtus will be assigned to it while the
ones which are idle of course will have
lower number of dtus because they aren't
doing much and then when users log in
and log out and Target another database
you know with their operations what
happens without us doing anything
without you having to do anything Azure
automatically reassigns those dtus and
thus ensures a consistently fast
experience so both our database clusters
and our virtual machine clusters have
scaling have high availability and have
almost no resource wastage to ensure
good experience for our
users now let's move on to my favorite
part as camil said we're very fortunate
to be in Azure because we have some very
good and giving neighbors the Azure
services and because we are a first
party Azure customer we get a lot of
these features before anybody else so
allow me to explain some of the most
interesting ones to you and let's start
with the Azure active directory it is
the connection point between Office 365
and Dynamics 365 if you recall from the
signup flow which I did when a user
logged in they use their Office 365
account to access Dynamics 365 for
financials and this is stored as I
mentioned in aad as is information about
their licenses and other things so our
product queries a ad and asks hey I just
received the login from this user do
they have a valid na license and if the
answer is yes without the user needing
to do anything no new account creation
needed need we will use just in time
user creation to give them a user in nav
and thus the customer can use the
product they have just one account One
account for one
Microsoft I love artificial intelligence
don't you it's on our phones it's on our
smart devices Cortana is making life
easier for so many people so why should
it make life easier for anv customers
well now it does because it's available
in the application so customers who l in
can already use it and it has so many
interesting features for example it can
offer accurate predictions of future
sales and thus help customers avoid
inventory shortage and it uses machine
learning to become even smarter as the
customer uses it and give them more
advice more tailored to their personal
content another awesome thing is that
customers don't have to worry about down
times because we have advanced internal
Telemetry which we use for easy troubl
shooting we offer three paths the hot
path the warm path and the cold path
through which information and events can
reach our monitoring teams and for
example should a critical event occur
the hot path will take over and in just
a few seconds one of our teams will be
notified and we'll take immediate action
to solve
it as you all know security is our
number one priority at Microsoft there
is nothing more important to us than our
customer data so we we made sure that
our service was Secure we did not store
any credentials servers virtual machines
or databases anyone in our clusters
instead we use something called the
Azure key bolt which is a Nifty tool
which is easy to use secure offers only
authorized access and has some great
features such as automatic credential
rotation for an even better level of
security and again these are just some
of the Azure Services we utilize I can
talk about them all day long but I won't
we have something else very interesting
to show you thank you very much so well
we were building the service and I think
we showed you the general picture of
what kind of components it consist of so
imagine you build such a system and you
expect a really high load on it of
course the moment you design it and you
have some test environment ready uh a
general architecture everyone agrees
upon you want to check how well it
performs because of course as
Constantine mentioned we can just throw
more and more resources but that is
really not a solution for the problem
and also we want to at the same time
improve the performance of Na AV so each
of you can benefit with all the changes
we make so we took a really close look
at the at the platform and we thought
okay let's build the entire test
infrastructure in order to automatically
schedule some huge amount of tenants
load tests so we can repetitively make
some changes in the platform tune the
feature it consist of and check how it
affects the entire platform performance
so we did build such infrastructure we
created it with thousands of tenants and
we we could like request any
configuration we we are pleased with in
in a particular test run and we used it
to test the performance and well here is
actually one t-shirt guys and one of you
can get it if you going to guess what
kind of online service that Microsoft
owns we used in order to create such a
service so of course we needed someone
to use the system and of course we could
go to all the floors within our building
and ask all our colleagues to stop
working for half an hour and use the
system but that wasn't really a good
idea so instead we use some system so
anyone want I guess what kind of uh
online service Microsoft was
it excuse
me uh let's accept that answer it's
Visual Studio online service so
I think it was someone out there who
answer
it thanks a
lot the
camera he's here so yeah we couldn't use
our colleagues uh and instead we used
the visual studio online service and
actually we found it extremely useful so
what we really wanted we wanted to see
simulate a huge number of users
accessing our huge system and we wanted
to really simulate the really usage of
the system oh I really got tired I think
I should run
more so what we did we actually created
a tests that would simulate the user
operations while using the nav things
like sales dock lookup or item lookup
some really simple operations and
slightly longer operations some
scenarios like creating and posting the
sales invoice so we created those tests
and well you might ask why didn't you
run it from our you know why didn't you
run it from your own infrastructure well
it wouldn't really be a exact simulation
of the real case because all of those
requests would pretty much come from the
same subnet maybe even the same IP
address so it wouldn't really simulate
the real Network traffic coming from
users distributed all around the world
so that's why we wanted to use the
vso so of course we also shared the
information uh so go go ahead and visit
that uh that address on the partner
Source you will find some videos which
explain how you can perform similar test
with your system I believe there is also
some source code available so go ahead
try it
out uh so we created those tests and we
run it against the system well we
already had an environment but really
how can you push the system to the
limits you should really simulate the
worst possible case so what we did
actually we simulated something that
really doesn't happen in prod which is
all the users were accessing the system
extensively at the same time because
usually as Constantine mentioned in prod
they would be accessing system at a
different time due to different time
zone maybe there are some local
regulations that require some operations
to be done let's say at the end of the
month or before you know earlier at the
beginning of the month so depending on
your location that load is kind of
distributed more equally among the time
we actually want the worst possible
situation simulated so we basically
loaded the system with all the users
accessing all the tenants at the same
time so that was one uh criteria to kind
of put the system to its limits and the
second condition was we also uh lowered
the performance here available to the
service so we use much lower performance
available on the database level level
than we would use in prod so we kind of
gave it less horsepower to put it even
more to its limits so how the results
look like and keep in mind that the
results we show right now and also the
platform improvements all of them we
could really start seeing at the really
high high load in a really big
environment in terms of number of
systems in thousands or there were even
bigger numbers and probably most of you
haven't noticed or all of you haven't
noticed it while running the service on
Prem or in cloud with not too big amount
of tenants but coming back to the
results so what you can see right right
now it's a graph that presents such
simulated usage of the system so on the
xais you see the time that pass as the
test executed and in the each single
line horizontal line represents a single
user running against the system and each
color within the line represents a
single particular test executed by that
user so what you can see on the first
graph this is one of the first results
visualized so it gives you a perspective
of how it looked in the beginning so you
can see there is some warmup time we
don't really Hammer server with a lot of
users accessing the system you can
actually see though that they're
starting to log in and perform some
first operations and then at some point
more users access the service and as
they started executing operations
concurrently the operations took a lot
of time to execute so what we did we
executed such uh such multiple hours
load test with a lot of users and a lot
of tenants and then we took a closer
look at our environment so we B
basically we're finding uh weak spots
and we work with all the internal nav
platform teams in order and also up
teams because there were also
improvements in up we made based on
those results in order to fix all those
week points and rerun the tests so
ideally we should see the situation
improving and we did so that is the
first result and then there's the second
result that we got after improving
platform slightly and how we did it
we'll explain it to you on next slides
so this is one of the next results we
got uh and you can see that it gets
better so some operations take longer
than expected in the beginning so when
the user logged in and started executing
first operations it took longer
definitely longer than expected but then
the situation after the you know NST
warmup after the user logged in and
executed few operation the situation
stabilizes and you can see that all
operations execute extremely fast when
compared to the previous state so again
we took again a look at the platform and
then we saw some things to improve which
again really surface only at a large
scale while running in cloud and what
kind of tools we used for that of course
except of some internal tooling we also
use something that is available to all
of you so if you have databases hosted
on Azure CQ you can go ahead and check
the tooling that the Azure CQ team made
available for you for instance you can
check what kind of CQ uh statements uh
takes the most of the CPU performance
DTU performance total DTU performance on
a database the the tool another tool can
actually recommend you what kind of
indexes you are missing in the database
so there all those small tools can be
used to analyze what is wrong in your
data model what is wrong in a Data stock
and of course there were other tools
that we use when we notice uh platform
issues on a VMS not in the databases so
what did we finish with well we we
finish with this result so with more
more uh things improved in the platform
as we went further with those test runs
we actually resulted in a situation like
this in which we not only see that the
user operations execute extremely fast
there are no delays on any user and what
is more if you look closely you can see
that actually all the users start
executing on the system at the same time
immediately so there's no warm-up time
so of course first we execute it with
some warm-up we s okay it's perfect but
now let's you know put the the barrier
even higher let's try to access dasty
even even faster with all those users
but this is the result we got so we
really spent a lot of time trying to
improve the platform and because this is
nav platform all of you will benefit
from it regardless whether it's on Prem
or in
Cloud so let's go through some of the
changes we made in the platform uh I'll
start with explaining some some
improvements we made uh that are related
to Azure cql and also cql server
connectivity so what you can see on the
diagram a little background so it's
maybe better to understand why was it
important what you can see here are two
clusters one contains of the VMS of uh
our service and also other services and
on the lower part of the picture you see
the databases there is an up database
outside the elastic pool and some tenant
databases within the elastic pool but
you need to remember that there are some
hard Hardware resources that those
databases are hosted on so there are
also within the same infrastructure some
other elastic pools hosted within the
same Hardware with other databases and
the same for the VMS that are other VMS
present what does it mean in terms of
the databases if we draw right now the
boundaries around our service so we will
kind of visualize that this is our
logical Dynamics 365 for financial
cluster we'll have two VMS we'll have
multiple tenant databases we will have
up database and because the same
Hardware is used by not only our cluster
also by other uh databases what Azure
cql will do in the background it will
try to ensure that the performance is
always perfect for you so it will
perform some maintenance jobs like it
will try to move some of the databases
to the higher performing uh stock so
basically you see no degradation of on
the service uh quality even though there
are more and more data basis added on a
hardware level and so because of that uh
of that situation you will be informed
by the Azure SQL due to so-called the
trans transient errors that situation
like this happened and your platform
should respond accordingly and in the
previous releases of course we
introduced support for Azure SQL so we
did handle those uh those kind of
communication with Azure SQL that
actually is done to help you but you
actually need to respond appropriately
but we took it even further so you can
see that there are some connections open
here and there are connections open also
but by other services so to handle this
in a great way we actually reinforced
even more our retry logic because as you
can imagine now as the the scale is much
higher there are like thousands of
cannons also the number of connections
is much bigger which means that we need
to be really intelligent in number of
connections we open we also need to
handle the drops in a better way and Al
all those throttling issues in in a
better way otherwise imagine you have a
really simple R logic and when you get
disconnected you immediately try to
reconnect and now imagine it happens on
thousands of tenants basically the the
situation gets even worse you get
continuously blocked so we took a really
close look at this and we ensured at a
super high large scale uh it performs
just
perfectly what is more also the
application DB connections we look at
how we open it how fast we close it how
how much we reuse existing connections
and we also improve that logic so we
don't uh we don't uh open the
connections too late for instance there
were some situations in which the
connection would be kept alive but
wouldn't be used which means that when
you look at the limit on Azure cql uh
server level actually we were taking
some spots we didn't use so we optimized
that and uh to get better performance
and also because we have the hardware
resources beneath our logical servers we
had to conform to the limit in in number
of connections and again large scale you
need to be more careful with this so we
improved it
more and task scheduler those of you
who've seen the release notes for nav
2017 you probably know that there's
something called task scheduler that got
executed and this is one of the results
of the work on the Dynamics 365 for
financial service that basically ended
up with this completely new feature
added to the
platform so let me explain you the story
behind the behind this feature what you
can see on that graph is the uh memory
usage you can see there are two scale
units we call the VM scale unit
internally so you can see there are two
that are load balancing traffic coming
to the to the system traffic coming from
from the users of the system and in the
beginning you can see that the memory
usage is around 2.5 gabt on each VM but
then it grows and actually it was
growing as we were mounting more and
more tenants so obviously that was
probably beginning of the of our
performance test effort so you can see
the more tenants are added the system
usage increases and the same actually
happens on the on a CPU level so we took
a look at that and we thought okay uh we
are not using the system extensively yet
but even though we see the that number
uh increasing with time so what was the
problem actually the problem was that
the NST was uh constantly pulling for
the job Q entries which was consuming
the memory and also the CPU and so when
the when the nas was running for each
for each tenant company and the and and
Q There was a separate thread spun up so
you can imagine not only the CPU usage
increase but also the memory uh memory
usage increase because each thread has a
cost on a on a memory so what did we do
we we thought of not only just fixing it
temporarily by by increasing let's say
the the VM size we actually try to
redesign the entire job Q execution so
we introduced the task Schuler so the
Tas scheduler got introduced again in
the platform so all of you can start
using it and the benefit of using the
task schedul is that there is a single
thread that is looking into the
application database it looks for all
all the job queue entries and simply the
lower memory usage the the T print and
also the CPU usage is extremely low so
when the nav server is Idle there's a
single threat used to execute uh to
execute those operations but all but
when you for instance want to just a
small comment about this if for instance
some task is set to run as another yet
user of course there will be another
threat created for that task to while it
executes however it's still much much
better situation than there was before
so after we introduced the SAS scheduler
we made the application Improvement and
we made the job cues to be optimized by
usage of the task
scheduler and thanks to this we got much
lower on the resource usage and it's AA
task schuer is available in platform so
go ahead and start using it today but
there is
more thank you very much Camille So as
my colleague said we run an extensive
suit of tests and he showed you how we
analyzed CPU and memory usage but there
is another very important resource we
looked at
dtus if you remember dtus were the
database performance measurement unit
you know the thing which tells us
basically how performant our databases
are so let's find out how they behaved
when our test was
running interesting so what do we have
on this graph on the x-axis we have the
time during which the test run and on
the y- axis we have the percentage of
resources which were consumed if you
remember a DTU had three major metrics
one of them is the log right the other
one is the data input output and the
third one is the CPU so these three
Medics make up a DTU and what can we
witness from this graph well the log
rights are pretty good they're
constantly under 5% and even the data
input output it's quite wey it's the one
in red here and it's still on average
under 10% so we're satisfied with that
but the CPU usage um slightly different
isn't it you know the blue things on the
graph just don't add up so we looked at
this and we thought okay why are we
consuming so much CPUs who is the main
culprit anyone care to take a I
guess you'll find out either way don't
worry but there's a t-shirt for the
person who please louder SQL there was
indeed something in SQL but what
precisely in our code like in our
application let's accept that thank you
very much so we'll give it to this
gentleman because we were first to say
but it was one particular let's call him
individual in our code the session
events table that was the main culprit
of course through operations but it was
consuming many dtus and as camil said we
got a lot of feedback from the asual SQL
portal itself and it said by the way you
are missing indexes in key places and as
you said we have some other SQL
statements which are a bit suboptimal
and consuming resources and then we
looked at our code ourselves and we
noticed that in other places we had
indexes which were too many and some of
them subop
so we made
improvements first of all we looked on
the platform side and we refactored how
the session event table works the loop
logic is a lot better and its DTU
foodprint has been reduced considerably
so we won't see this anymore and we took
it even further we took and made
application improvements and we have
also added those missing indexes which
were suggested and the extra ones
they're gone and we have also improved
database querying so now for example
when we filter on things we try to do it
on index fields which is a lot faster
and in some cases we all had multiple
SQL statements which are now replaced by
one it's a lot more optimal and we even
had let's say inefficient casting which
has been removed and thus the time has
been significant reduced so not only do
we have reduced CPU and memory usage but
also reduced DTU
usage our old friend the nstd I would
say it behaves quite well when once it
is warmed up but on a cold start it can
use some improvements right so as we saw
from the test there was a stage when we
noticed that during the call start
something was taking time so we dug into
our code and thought okay what is it
doing why you know is it taking this
time and it turns out the main culprit
was that it was needlessly recompiling
assemblies you know an object was
modified assembly compilation so we
thought okay this is taking a bit too
long than we'd like we like our things
fast so how did we solve this problem we
looked at our metadata caching and we
have optimized it and even more now it
is not just for the nav server it's also
for the extensions we mentioned so when
they enable them it will also stay
fast and to make it things even better
it is actually cached even before the
user logs in so that even their first
experience will be
fast but because we're in the cloud we
have virtual machine clusters right so
there's more than one virtual machines
and even when you may use it on Prem if
you target Azure you may have more than
one machine so let's say for example you
go and recompile one of your objects
like a code unit or a page the server
should then have to you know recompile
that cache recompile those assemblies
but it'll do it on one of those virtual
machines what about the others when the
customer logs in you don't know what
machine they will hit what if they hit
one where the cach isn't yet synced well
we thought about this issue and we
introduced ND caching between these
virtual machines so that wherever that
item is recompiled in a very very short
time all virtual machines will have the
metadata cast sync and the user
experience will be constantly
fast and there was one more very
interesting thing we noticed so keep in
mind that we ran this test with
thousands of users and we had hundreds
of tenants per nav server and when one
of these servers was started all of
those tenants would be mounted in
parallel and you can imagine what would
happen to the SQL Server you're opening
hundreds of connection at the same time
time in a very short amount it gets
throttled that is a bad experience so we
fixed it by making the way in which
tenants are mounted more controlled more
queued and the problem was gone so you
kind of saw how things were before and
we kind of presented the improvements
let's see what they actually helped us
with we have chosen blue a cold color to
represent the old cold startup so let's
take a look at this graph we have the
x-axis where we have the multiple test
that we run you know different
circumstances and on the y- axis we have
the number of seconds it took the server
to start keep in mind this is a cold
start a very heavily loaded system so on
average we see that it's between um I'll
would say 2 and a half minutes to three
and a half
minutes with these improvements in place
how much faster do you think it is by a
factor of what can take a
guess 10 go lower go lower bit a bit
higher a bit higher six
that was it who said
six that gentl here it
is it was a very good guess so without
these improvements we took on average
with again a lot more resources than you
would have in a normal production
scenario on your your systems thousands
of users hundreds of tenants 3 minutes
was the average sarup time which is 180
seconds with these improvements it went
down to 30 seconds and we'll only get
better when you try
it and we have one more great
Improvement because we think that the
first experience is very important and a
lot of our customers which will become
your customers will try anv for the
first time with Dynamics 365 for
financials so some of you have probably
you know worked with multiple virtual
machines and have mounted a tenant on
one of them when you work on Prem it
will be mounted on one of the virtual
machines and it will roughly take 30
seconds you know for it to propag at
across all of them and in our world so
far this has been good 30 seconds
acceptable but not anymore because we in
for five seconds to sign up every single
second counts and that can be the
difference between a customer seeing
this and a customer seeing this on their
first try bad experience we don't want
that so how did we fix this issue well
we introduced something called Just in
Time tenant Discovery and let me give
you a diagram of how this works you're a
customer you access the URL and of
course you'll hit a low balancer which
will randomly select the virtual machine
let's say has selected one where the
tenant hasn't yet been mounted before
you would get that message and you would
be probably unhappy but now the virtual
machine will talk to the other virtual
machines and say by the way do you have
this tenant it will synchronize just in
time and then it will give the user a
adequate first experience
so a quick recap of all the features we
have shown you today we have Azure SQL
connectivity improvements by reusing
connections and having automated retry
logic we have a new task schuer for job
cues which made things a lot faster and
we strongly encourage you to refactor
your code especially if you have code
units which use the nas to now use the
task Schuler you won't believe how much
faster it is we have optimized resource
consumption not just memory and CPU but
also
DTU we have a faster NST warmup six
times as fast and again those times were
on heavily loaded
system we have reduced cogs for running
on Azure SQL whether you use elastic
pools which we strongly encourage you to
use you won't believe how awesome they
are or if you don't want to you can use
them on Prim with whatever a of
resources you like and they'll still be
better and we have the just in time
Tenon Discovery for a good first first
experience every time and all of these
features are in the cloud running on
Dynamics 365 for financials for all of
our customers but they're also on Prem
in NAB 2017 ready for you to try out we
cannot wait to get your feedback on
these
features so we have shown you how
through Dynamics 365 for financials we
shall get nav in just a few seconds into
the hands of every small and medium
business on the planet and how we have
improved our own print product by
creating it that's quite a lot for a
session however there is one more thing
thank you very much Constantine so yes
there is one more thing we'll switch
more to a runtime experience now on as
monitoring the service and in terms of
the platform improvements we really you
know did more but those examples you've
seen were from slightly different areas
so we showed at least one change that
actually ended up being being a
completely new feature we showed you
something that decreased the warm-up
time we showed you also something that
decreased the memory usage so affected
positively the VMS and also something
that affected the servers as Constantine
said let's switch to something else
otherwise there will be no more time so
let's look at the monitoring Telemetry
and insights and we mentioned in the
beginning that the monitoring and
Telemetry was extremely important to us
because really when you have this large
scale service like Dynamics 365 or
financial
you must know what's happening with the
system right you cannot just know
whether it's up and running or not you
need to know how the system is used so
we spent a lot of time there was a
specific team even responsible for this
so it it was extremely important it was
not just a feature it was the effort
that we continued along the entire
project and whatever other teams were
creating they must have ensure that
there's appropriate Telemetry
information added so the entire picture
looks complete when we start running the
service so let's take a look at the
monitoring and Telemetry and the
insights that you want to have on the
system so when you build a system that
allows you to get such information you
think of three things you first look at
something you emit so of course you need
the information first so you emit the
information from each and single
component of the system then of course
you need to scrap the pii information
the private data like the unique user
user ID or the IP address or whatever
can uniquely identify the user to comply
with all the regulations then of course
it's a huge amount of row data row data
is great because you can process it
feather and you can find some new uh new
usage for the data so it's pretty clever
to keep the row data however you also
need to transform it if you want to for
instance use the powerbi it won't
probably consume petabytes you probably
will use smaller amount of data if you
want to for instance to get some graphs
on a dashboard and of course you consume
the data so we basically divided our
work into looking into those three
separate like uh steps of building such
a service so let's start with the what
kind with the a short explanation on
what kind of in information we emit in
our
system so we start with the health
Runner which is responsible for outside
in monitoring so it's a good idea to
look at the system from the outside so
that's why we created health health
Runner Runners that were trying to
contact each of the tenants that we had
running in in prod and they were not
only checking if the tenant is there it
was actually checking if it's uh
responding correctly so it was ensuring
that whatever call it makes it goes for
entire nav stock so through the web
client the NST the database and performs
some some real some real work so it
actually guarantees that the tenant is
fine but there is more of course we have
management portals and management
portals have information about how many
tenants we deploy where the tenants are
located on which Azure uh resources so
basically the management portal except
of course a normal health information it
needs to provide it also provides some
inventory information but the management
portal also exe is participating in
executing some management tasks so
whenever we provision new tenant or we
do some upgrade in order to switch to a
new platform beats or the up version it
also provides the information about what
kind of operations it executed so we
know if there's a problem up front and
of course there are VMS so probably most
of you read the msdn documentation and
you know that we generate etw in
application events and pro probably most
of you also used it in in Prem so we
also look at the etw events and we
extended the set of the events and we
created something uh I'm sorry we
installed something called the
monitoring agent on each of the VM and
why did we do it because we didn't want
to store that information locally on the
VM because let's say the VM goes down
you lose the information so we deploy
so-called monitoring agents that is
responsible for transferring data
feather and it gives us a better insight
into the state of the VM so we know
what's happening both on NST and on the
web
client but when you look at all those
components there is something common for
all all of them and that is actually
that they're all on the server site and
you cannot really get a really good
information in terms of telemetry you
don't really get a really good insight
into what's happening in the system if
you want also do it on the client side
so that actually doesn't complete the
picture yet we also have the client
components so as you can see there's
also a browser because you will probably
access the uh Dynamics 365 for financial
service through your Office 365 account
there's also of course device app as you
know thanks to the usage of the Dynamics
and at the heart of the service there's
a mobile device supports for all
operating systems so some of you will
use the device to do it and then of
course there's a landing page the
landing page is the component that
Constantin presented I think on the
second slide which participates in the
signup experience so when you provide
your company details then you wait those
5 seconds and during those 5 Seconds you
see the landing page and you might ask
yes but what's so special about this
well it is really important for us
because thanks to that Telemetry we get
from the landing page we actually know
how long you really waited for it
whether it was below the 5 Seconds we we
our goal is for or whether it was more
whether you Clos the browser didn't wait
for it all that information we would
like to know so we can improve the
system and imagine hypothetically the
tenant doesn't get created and you're
informed about this before you contact
us it's going to be already probably be
fixed by now because we'll get that
information up front we won't need to
wait for you to tell us about this
appropriate team will get a notification
and it will be fixed as the problem
arised so that was actually one of the
goals while we work on the monitoring
and Telemetry the fact to be able to
react proactively not to wait for the
customer to tell us there is a problem
but to fix the problems before there is
a problem and for the devices of course
for the devices we also need to know
what kind of operations are performed so
actually will cover it in the demo
pretty nicely so I won't tell you more
about this for now let's concentrate on
Azure application insights for a second
it's a component that uh also resides in
the emit part of the of the system uh we
actually placed it there because we
wanted to emphasize that this is the
component that is residing and is
accessible from outside Microsoft
infrastructure because as you can
imagine you're accessing the the sites
from outside our corpet which means that
in order to collect this information we
need to have a service exposed and Azure
team again came with
help for that problem they created the
Azure application insights which allows
you to collect the Telemetry from your
applications and we use that system with
a great
success uh what is critical when you
create such monitoring in Telemetry
system is to ensure that you don't
collect too much so we would like to
know how the system is used however we
must you know comply with all the
regulations we don't want to store the
private information like uh let's say
aad username and the email address we
don't want to uniquely identify that it
was you you or you that executed at
particular time this particular
operation so we we want to know how the
system was used but with uh confirmance
with all the regulations so so before we
do anything with the data we ensure that
it's it's scrapped from the private
information so both the tenant uptime
time and the inventory and operation
Telemetry all the etw events uh and
operations registered while on the
client site all of them uh get the
private information removed before we
have access to
it and Constantine mentioned already
that we distinguish between so-called
so when you think of a monitoring system
uh you will probably start by of course
looking at how to divide that data you
get because you get a huge amount of
information and how we actually divide
that information is we call them Puffs
so there are three Puffs we distinguish
there's a cold puff warm puff and a hot
puff and how do they differ well they
differ in many ways uh there's a
different way we store different type of
information for instance if something we
use more for a bi purposes more like for
showing in the power bi dashboards that
information should be probably really uh
historical in terms of like how many
days back we uh we collected that
information it doesn't need to be really
quickly accessible like within matter of
seconds there can be some job that
process this data it's not so critical
however in an example that I think
Constantin also mentioned is that in a
situation when something goes wrong like
the health monitor in us that the tenant
is down or we see thanks to some other
subsystems that there's a problem with
the system I'm sorry with the with the
service we would like to know about this
within seconds and that's why there's
something like a hot puff so how do they
differ so for the hot puff we use a big
data storage that is extremely fast in
terms of the access so we can uh query
we can create the alerting we can create
everything and we know that even though
amount of data is Big it's extremely
quickly processed so there is no delay
between some occurrence of a critical
event and the the time internal team
gets notified for the warm puff well
imagine there is a problem and uh we can
see that there's a kind let's say uh
exception thrown on a server site we'll
troubleshoot the problem and we'll show
you a real demo of that uh in a second
but for this type of information you
won't need to probably get the details
about how let's say how often it
occurred within let's say a second it
can take 10 seconds it can take 1 minute
when you make a query and you get all
the historical data about how often it
happened and that's why there's
something like a warm puff it's
something that we don't need to get
extremely fast so we use a slightly
different data storage for that and as I
said there's a cold puff which is used
more for a uh feather processing to be
used for let's say powerbi dashboards or
to get some other statistics so that's
why we distinguish between those three
uh paths one is important in terms of
alerting and uh real-time monitoring the
other one we use to get a more insight
into how the system is used so there are
different purposes different data
storages and different consumers for
each type of the
information so how the hot puff is
consumed well those are all internal
system so we won't uh tell you a lot
about this but just to sum up we have
some monitoring and alerting system that
is reading the information from the hot
paff and based on the information it
receives example tenant is down it
immediately ensures that appropriate uh
team members is notified about the
problem again all those issues we get
notified about before even you notice
the problem so that's the hot paff for
the warm puff it's mostly used for the
troubleshooting for checking the logs
for seeing what uh how the system was
executed in order to maybe think of what
next features we should we should
provide and also the cold puff will be
used for that so we want to see what
what what part of the product was used
in order to know what part of it we
should improve because it's used the
most often for instance and also for
some daily statistics that we use the
powerbi dashboards for or some other
information basically the cpff contains
the most of the data in terms of the
amount and it looks
back with the highest time window and in
that case because it's a lot of data but
it's not really critical in terms of how
fast we process it so we can create some
jobs that will process let's say
petabytes of data Maybe not extremely
fast but it will give us a better
Insight on the
system we mentioned power bi and this is
one of the dashboards you can see uh
right now so this is a type of
information and this is just a sample
what kind of data we can get this one
for instance uh gives you an Insight of
how many users use the use the system uh
when was it like how many science up we
had how many people visited the site so
this is a sample data we feeded to to
this graph and we can take a look at
this daily it is not super critical
that's why it's not coming from the hot
path but it's extremely nice because we
can know who's using the system how how
many signs up there are how often user
access the system it gives us a great
capabilities and we can really create a
lot of those and get a better insight
into what's happening in the system so
we collect a lot of information but
probably you would like to maybe get a
good example of how we use the warm puff
so let's get there okay thank you very
much Camille So for the finale we should
demo how we troubleshoot an issue and
these are the exact steps we would take
if this issue would occur in production
so let's imagine that somewhere out
there there's a customer and they have
logged into Dynamics 365 for financials
have played around but when they try to
post the first s invoice they get an
issue so what does the customer do they
contact us via email here's the email
they send us they say dear support when
I'm trying to post my first inv voice
I'm getting the following error and we
get this error we see this number 1896
and we see it was on the sales page the
customers of course stand it in trouble
coincidence I think not so what is our
next step we create a ticket and then we
have to analyze and see what caused the
issue in order to do that we have to
determine a few things first of all
where did it occur for which user in
this case we know it is for the user
called tenant in trouble and we know
which cluster they deployed on once we
have that we have to determine what kind
of issue it was and you though many
erors can have different underlying
causes but we know at some point in this
flow a cal error occurred we see it
right here so we know what kind of error
to look for and once we have that we of
course have to identify the time frame
the when during this during which this
occurred so let's say for the purposes
of this demonstration that it occurred
yesterday and let's say more than one
hour ago so once we have all that we can
connect to the relevant cluster and
create a query to retrieve the Telemetry
data this Telemetry data will help us
analyze the issue and here is a sneak
peek of the tool we use to explore the
ocean of data
before this demo we created a function
called Al errors and you're never going
to guess what it does it retrieves Al
errors and it has four parameters sale
because we know it occurred on a sales
page tenant in trouble which is the name
of the company and the third and fourth
parameters are the time frame so as I
said for purposes of this demonstration
let's say it occurred between a day ago
and an hour ago so after that in our
Nifty tool we run this function and
retrieve the relevant data and if you
can see this is the data we have
retrieved and by going through it let's
look at the highlighted one I'm not sure
the font is readable it says tenant in
trouble because that is the company and
then let's look at the description
blocked must be equal to number item
1896s that looks like our culprit and
I'm just going to direct your attention
to the session number 12 because we're
going to come back to that a little bit
later but now think if you were that
customer actually think more General
let's say your computer had broken down
and you call support what is the first
thing they usually
ask what were you doing when the issue
happened right they try to ask what are
the Repro steps but why should the
customer do that the customer shouldn't
have to explain to us you know what they
were doing our Telemetry should let us
know in fact as Camille said the
customer shouldn't even have to write
the email why do they have to contact us
for an issue on our side we should be
able to fix this using our Telemetry and
we can because all we need to do is as I
mentioned look at the incident and
remember that session ID 12 based on
that we can retrieve something called a
unique server session ID and this is a
GID which is the same for all operation
user executes during a login session so
if I log in do some operations then log
out all of the operation I did will have
the same server session ID in our
database and here's how we can retrieve
them in our tool once we have the error
we write this code which retrieves the
unique server session ID for session
number 12 and let's say it retrieved
this GID we then retrieve all the
operations for this guid again Camille
just showed you this is all trimmed out
there's no user data here no personal
information these are just events
triggered when you know the user has
clicked on different items which help us
proactively troubleshoot issues so once
we have that and we have analyzed the
action let's actually try to reproduce
the bug so on the left side of the
screen you shall see our reproduction
environment and on the right side I
shall keep this list so we can look
through it and you know not have to
switch context every now and then so
here we are now reproduction environment
which is the financials application the
customer was using and we also have
these operations right so what did he do
he logged into Office 365 it was getting
started and then they closed you know
that welcome experience this is what
this operation does we did the same
thing over here as you can see and then
we usually would go through this list
right we have the item list the item
card and different operations but
neither of those the problems if we were
to go to them one by one they would all
be fine until we got to this part so at
some point they open the sales invoicing
list and they clicked on post sales
invoice and we do the same and then we
try to post the sales invoice
ourselves and here is what we get do you
see that error message blocked must be
equal to number in item
1896s is the exact same error message
they got so now just by using our
telemetry
we can actually have the reproduction of
the bug and even more because if we go
back if we you know double click on one
of the queries and look at this error
message it's blurred out here for
obvious reasons but we get the stack
Trace so not only do we know how to
debug we know where to debug and again
this is done proactively without the
user having to contact us we can analyze
this issue on a daily basis and improve
our product in the
cloud camil yeah I think it's pretty
powerful I don't know what you think
about this but you can just think of
scenarios like looking for the most
occurring exceptions or most occurring
Al errors I mean possibilities are
endless really when you have the right
information at
hand so guys I think we really gave you
a nice description of how the system is
built and how we operate it but we are
also sure that you might have some
additional questions so we have still
few minutes right now and of course
after the presentation feel free to ask
yeah so like camil said don't worry if
we run of time here we're here at the
walkin dinner I'm here tomorrow just
grab me whenever you can do you mind
throwing at people okay so I'll throw
here because I think this gentleman race
set up first excellent this tool is it
going to be published is it going to be
made available for on Prem customers in
any way so the etw events are already
generated on for instance NST so when
you go to msdn can already set up the
system so for instance and uh let's say
cql operation will generate appropriate
etw event and then you can use the
tooling for processing this to get
necessary information so you need to
think more about how you process the
data FEA but already you will get
similar information from from the
platform that would include um sort of
Na related operations because yes yes
yes so when you go to etw there are
several types of information information
for instance you can be notified
whenever a certificate used by the NST
is about to expire or some Al related
events or for instance all the SQL
related events when the statement gets
executed it can inform you as a etw
event however be careful because if you
enable too much it will also affect the
performance because it will basically
inform the Telemetry system about each
operation but it's really detailed and I
believe on msdn there is a list of all
the event IDs and uh what they repres
I think it was over there so we can just
pass it in this area and then we'll move
it around um thank you for the example
where you showed the item error item
blocked error how do you differ between
those errors and real errors in the
reality because I think the the typical
customer will get 100 errors a day and
they are all no problem in real how do
you differ I don't think they would
actually get 100r per day so basically
you know you can imagine we have the
Telemetry in place and we can determine
what types of error occurred and there
can be different causes for them but we
can always analyze them and see what the
actual cause was right for example we
can look at frequency and say these are
the most frequent ones and they are
occurring quite a lot let's see if there
you know like a read error an access
error or there's something we can
improve and we always try to get them as
low as possible and besides just to add
something to it so because we have the
historical data we look at a particular
error once so if it's really typical
error we'll see it really quickly and
then we can already filter out in the
dashboards or in the alerting systems
that that particular you know error you
know should be ignored so maybe we'll
spend few seconds of our time but then
later on we already know the problem is
not something we are I'm looking forward
for the next two to three years when
you're going to track all those errors
and fix them in the application then
then we will be really
perfect we are also looking forward okay
uh the gentleman behind you okay perfect
thanks um you talked about the just in
time tenant Discovery um do you do this
globally meaning do you do Global
Geographic load balancing and um for
example how do you um fix the problems
or solve the problems with the database
charting and database replication
meaning you know customers accessing the
same Talent all over the globe so it if
you ever used the management portal we
know that we have something called
application services and those things
are Azure Services actually and we group
tenants in those application Services
they have a bunch of virtual machines
which help them run you know the ones I
showed you in the cluster and they're
also grouped geographically so we try to
avoid like you know putting data in the
same place North Europe with the United
States for example so we separate them
and when one of those um virtual
machines will ask the other ones it will
only as the ones in the same cluster so
for example if you're in Australia and
then you try to get a tenant you and ask
the ones in India for example or the
ones in Europe you'll just as the ones
in the same application service cluster
okay so you will still have um latency
issues if you're trying to access a
tenant that was set up in India for
example but you're in Australia at the
moment the we have made logic that Waits
so you know the user will log in and
they will get a loading screen until the
tenants are actually synced they will
still see the loading screen and then
they'll get you know either an adequate
experience or if the ten their accessing
is actually invalid for example you know
the is wrong then they will get a
message but as long as the tenet exists
it will
appear okay where do we go now uh anyone
else there I see someone oh can you
throw it all just I think we need to
encourage people with more t-shirts so
the Constantine okay
thanks There You Go
sir are you having any plans to backport
the NST improvements to to 2016 for
instance uh that's a really good
question so maybe let's take it offline
uh I think most of the changes we do
unless there are some they have uh some
dependencies in something that is only
available in 2017 we need to make sure
that there are no issues when you switch
to a newer build that you don't need to
rewrite the up so but usually we
whenever we can we do improve the the
previous builds with what we what we
introduce so we would need to go with
the list one by one and see what already
got ported or what is planned to be
ported we look at the cumulative updates
basically and we decide on weekly basis
what what gets there so if you're
interested in this uh you're more than
welcome to contact us and ask about a
specific Improvement and we'll confirm
or whether it is going to be there or
not
any other
questions that seems to be it okay so
thank you very much uh we really hope
you will all try the Dynamics 365 for
financial service and again will be
available for some further questions if
they arise yes thank you very much much
thanks
