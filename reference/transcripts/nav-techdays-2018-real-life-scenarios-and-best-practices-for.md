# NAV TechDays 2018 - Real life scenarios and best practices for using NAV on Docker

- **Source:** https://www.youtube.com/watch?v=W_x9pdq0zn4
- **Video ID:** W_x9pdq0zn4
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 71m54s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

welcome to that session
um
that one is about docker if you're
looking for the one about business
central under the hood then that's the
other one
um also if you haven't heard about
docker at all that might be a bit much
today so i give you that chance and i
absolutely don't take that one
personally if you've never heard about
docker it might be a bit much today
okay that's the photographic
so my name is tobias fenster i'm a cto
at axios informa and also a business
applications mvp
um i tweet a bit and i blog a bit so if
you want to follow what i'm doing mostly
around business central and docker a bit
about tfs continuous integration
continuous deployment that stuff then
those are the places where you should
find most information
what i have prepared for you today is
first of all a quick introduction but
that's really two slides two minutes
into docker
and then the overall scenario because i
want to make sure that you understand
how we are working at excel's informa
because the things that i will show you
are
actually taken out of our daily practice
um
and depending on how you are organized
for what type of a company you are
working or if your freelance or whatever
that might or might might not make sense
for you so i'd like to take a couple of
minutes to introduce you to that
scenario
and then the fourth scenarios that i've
prepared the first one is a self-service
container environment so the basic idea
is that we have a web application of
course based on business central and
that one allows our developers and
program managers to just self-service
containers so whenever they need a
container on a specific release of our
solution or chronos they just use that
web web application and they can get
that one
the second topic is multi-container
environments um
i think you should have seen a lot about
docker in the
in the last two days or in the last
weeks and months when you've been
following what microsoft is doing but
mainly they are focusing on one
container environments so it mostly is
about having one container doing your
development doing your build doing
whatever you need to do but of course if
you think further about that one then it
also makes sense to have multi-container
environments like you have your sql
server and then you have a couple of nav
server containers that are all running
in containers
the third topic will be automated
extension builds now there have been a
lot of sessions around ci cd and a lot
of information in the last couple of
weeks so i will focus on the on the
docker part and specifically on
something that's called a multi-stage
image to introduce you to that concept
and the last one is azure container
instances
that basically shows you how you can run
containers without having to install
docker um just out of the box by using
using azure services
and then i was thinking okay now this is
the last session the last session slot
for take days it's after lunch how do i
make sure not too many of you are
falling asleep
um
and then i also decided maybe it might
make sense to let you decide in which
order i'll tackle those topics because
they actually are independent they don't
they don't build on top of each other
um so yeah
a bit of um audience interaction always
makes sense i'm not that guy to tell you
you need to jump around and hug each
other and do that stuff because i'd be
the first to leave the room in that case
so
probably most of you are already on your
mobile
why don't you go to that url
and vote for which of those topics you
want to tackle first
and i'll give you a minute to type that
one
that's ve.link a slash and then td 18
for tech days 18 and vote because of
course you're going to vote
the hand raising and the clapping didn't
work so well in other sessions so
let's see if that one works
quickly switch over here it should look
something like that on your
on your browser
and then let's see
if those votes do come in or not
actually there's something that i
decided
yesterday evening in my hotel room so
i'm
kind of scared if that will work or not
let's see
yo okay
we are at more than 130 votes so that
seems to work
on the bottom right you can see the
votes coming in so
okay i'll leave that one open um you can
still go ahead and vote and i will
always get back to that vote when we
when we tackle the next topic but it
seems like self-service is the winner
for the first one
um
okay quick introduction to docker in the
overall scenario
what is docker about docker is a
software container environment actually
the leading cross-platform one on linux
there are a couple of others but if you
as soon as you're starting to look at
windows containers then docker really is
the only relevant option there
software container environment means
that you have the ability to define
something that's called a container and
the base idea of that container is that
you put the minimum amount of operating
system of libraries of dependencies and
your application binaries together into
what's called an image or can think of
that as a template and that defines what
you need to run
your docker containers and what you need
to run your application
and then when you have that image that
template
then you create from that image a docker
container and that is the running
instance of that um of that image so you
then have your running application
in case of
navision or business central this is
actually sql server business central
itself and then iis the definition is in
the docker file that all of that needs
to be installed and as soon as you run
it those three components or at least
parts of that will be running inside of
your container
in a lot of ways a container is very
similar to similar to a virtual machine
but then in others it actually isn't and
it took me a couple of
hours or maybe even days to believe that
so don't try to get an rdp connection
inside of your containers because that
just won't work you really do not have a
graphical user interface for your
container
two other things that i'd like to
introduce you because i might mention
those in the next couple of minutes what
is a docker host the docker host is the
machine where the containers are
actually running so that might be either
a physical machine or a virtual machine
it doesn't matter you install docker on
that one and then it allows the
containers to run
and what is the docker registry that's
the place where you can push your images
so you can upload them for others to
download and that's called a pull um
your images that can either be a public
repository the most widely used is the
docker hub and microsoft is also
establishing something that is called
the microsoft container registry
mcr.microsoft.com where we already get
the business central on-prem images and
i think they are moving all their images
over there
so that is the introduction of what
docker is but then you might still be
asking why do i want to use docker and
there mainly are three reasons if you're
thinking about developers and operations
and devops because that's a buzzword and
i need to hit a couple of buzzwords as
well
it's a very easy way to create your
deployments because you can very
specifically define what the um what the
steps are in that image
in that docker file that is that
describes the image so i need to install
sql i need to install business central i
need to install an iis i need to
install.net whatever and then i need to
install my application so that's a very
good way to communicate between
development and operations how you want
your application to be to be deployed
and it also is very stable and reliable
because every developer can do the same
and then you have the same in a test
environment and you have the same in the
production environment
and as those containers are very
isolated from each other you don't have
any interference you probably have run
into cases like
it works on the developer machine but it
no longer works on the test environment
because the developer has visual studio
installed and then there's a new version
of a library and that is not available
on the test environment
now that's the easy case um but you also
have cases where you do run into
problems because in your staging
environment someone's flipped the switch
but forgot to flip this same switch on
the production environment so it still
worked on the staging environment but no
longer works on production and docker
containers really are very good way to
solve that problem
they also do have a better resource
usage than virtual machines because when
you think about it a virtual machine
brings its own operating system inside
of that vm and that takes a bit of an
overhead as well actually in case of a
windows server it's it's a rather huge
overhead for the cpu and memory that is
already in use just by starting a
virtual machine
and a container is a bit easier on the
resources there because it just reuses
whatever the host offers so it just
reuses the kernel of the host it doesn't
bring it its own kernel and that means
that you have a lot more resource
resources to play with for your
application
and then you have a very big ecosystem
um for example we have sql server images
windows server images
nav business center and then if you look
into the docker world that really is a
huge variety of images that are already
pre-built and ready to use for you
so that's it for the for the quick
introduction about docker the next step
that i want to introduce to you is the
scenario where we are working with um at
info
sorry at infoma
we are an iso and we're working for more
than 1200 customers and all of those are
running the same solution so this is our
product that's called informal new
system
and because of that number of users who
are using using our product or the
number of customers we have more than
100 people who are directly working on
our solution that's developers program
managers
back office hotline support all those
people
so they're really on a daily basis
working with our product trying to
improve it trying to make it better
that means that we have a central team
that provides the infrastructure for
them
um so there are standard images for
laptops central vms for development
central sql servers nsts iis we try to
limit the amount of things that people
need to do on their local laptops and
now while we're still working with
seaside and
and old school nav
there's a limit to how far you can take
that and of course there will always be
things that that need to happen locally
but we really try to standardize that
and put things into central environments
to make sure that that works as easy as
possible
so really the target for us is to have
our technical infrastructure usable as
quickly and easily as possible
you need to standardize you need to
minimize friction you don't want to
expect infrastructure knowledge and you
especially don't want to create a need
for infrastructure knowledge
don't get me wrong there it might make a
lot of sense in your scenario to have
docker containers on the local machines
for your developers for your program
managers whatever but in our case we
have a lot of employees who know a lot
about infrastructure but actually their
focus should be working on the product
developing testing improving the product
and you have to spend time on setting up
your local development environment then
that probably is time that is not well
spent because it's not actually
improving the customer satisfaction with
the product
and with that lengthy inter introduction
you probably will guess where this will
leads to we have central docker
containers provided by our release and
management release management and
tooling team
so with that um we are sure that the
people who actually are experts in
working with docker and working with
business central on docker provide those
environments and we don't have to
introduce that knowledge to everyone and
fix whatever is happening happening on a
random laptop
the reason for that also is
that we can stay away from docker on
windows 10 which would be the docker
community edition
um
and that one isn't working that well it
will hopefully soon increase a lot and
that might be a point of time where we
will look again at um if it doesn't does
or doesn't make sense to to deploy
containers on local machines but
currently we stay away from that
and that's also the main reason why
we're not using the enough container
helper because it mostly assumes that
you have a locker local docker
installation and then there's one of the
grumpy old guys who provided a tool to
do that on remote hosts as well
but actually
we had professionals in place who
already knew how to work with docker and
the nav container helper really is a
great tool but it helps you working with
docker and we had that knowledge already
so again if you only want to have local
contain containers for development um
when you don't have docker no already
please look into the nav container
helper that makes a ton of sense and we
actually also use it a lot just to see
how freddy has implemented stuff and to
see how this or that works we're just
not using it in our environments and
just copying the relevant parts for us
so what i'm showing you um will be
relevant for our scenario so i guess the
the technology and the concept should
still be interesting for you
but this is the last chance if you want
to leave now at the moment
and even the grumpy old guy said docker
is interesting so yeah might make sense
to be here
okay so let's check again for the voting
and we have almost 300 votes and the
self service seems to have won okay
so we go with the self-service
containers
no we don't
yeah we do
um
first of all why are we providing this
again that goes back to the things that
i've already introduced
we want to have easy access to releases
because we have between one and three
major releases and four and six buckfix
releases for our solution per year and
that that multiplies by two countries
that we're currently supporting germany
and austria
you wouldn't think it but austrian
actually is a vastly different language
than german
so we have up to 20 informal new system
releases per year
and that means that we have a lot of
releases already in place where we want
to test stuff
and then there's the business central
nav things where we have dynamics nav
then we have the bc sandbox we have bc
on-prem we even have the bc sandbox
master so that the upcoming next release
and you might want to check in different
scenarios what different things are
doing
you might have fixed the bug and you're
wondering does that work with our
release in connection with cu16 why
doesn't it work anymore with our release
in connection with co18 is it a bug that
happened between cu16 and co18 or is it
a bug that happens in in other in our
code so you really need to be able to
have um different environments as
quickly and easily as possible to just
test stuff and try it out and then you
you test it for half an hour and you
just throw it away again
so we need to make make those releases
available for for quick and easy tests
and then as a couple of people already
have said in the last two days we of
course don't make any mistakes but in
rare circumstances it might still happen
and then you need to create a hotfix on
an old release because the customer is
not not already on the latest release
and then you need to
have an old cu you need to have an old
release of our our solution and you need
to create a hotfix on that one
so how does this look like
as i said this is on the front end is
built on business center
so
we have a nice and friendly greeting and
we have a couple of tools implemented in
that and especially we have the
container austen which is create a new
container
and if i do that then i get all the
containers that we are providing
you can see on top of that here those
are the new system releases so our
releases of the last two years the
german ones in the austrian ones and we
also provide the latest release that we
did on the cu that we used so we
delivered our release 18110
with 2017 cu 22 but we might also want
to test with the latest release by
microsoft so we also have a container
with 18111 co23 so that actually is very
easy it's just one line in the table and
then we're done with that one
as you can see here we also know which
image we want to use which release we
want to use um if we want to use a
special database um and what the id of
the release is in case of a new system
release
we also have a couple of chronos
containers and then we have the the
business central sandboxes as well
so now let's create one
as you can see here it has an end date
and i'll explain in a minute why that is
and now i just kick it off
and that will take a bit so i switch
back here
so what have you seen um there is the
front end for the end user and that is
actually just a business central
extension running
on one container host so of course that
business central instance is running
inside of a container and that one has a
business central extension
then we have a rest-based api that is
running on a different system that is
taking the requests as you've just seen
i've made a request to create a new
instance and that one is accepted by
that custom api
that one in turn calls a couple of
powershell scripts and it also connects
directly to the docker api for other
tasks
and all of that is running on a
different container host that's our
release container host
so a bit more detail about that one
the business central extension
is something that we built poorly purely
in al no.net additional stuff
the the list of available images is just
a standard nav table or business central
table in that case so if you want to
support a new image in that tool we just
add a line in that table and then
overnight all the images are getting
pulled and downloaded
if that image is already there it will
get get overwritten by a new one so we
always are on the latest bits and bytes
for those
as i said the containers are valid for
the maximum of three days and the reason
for that is that we currently are
running this on only one virtual machine
so there's a limit of the resources that
we can provide
hopefully with windows server 2019 we
will be able to run something that's
called a docker swarm so we would then
be able to spread that out on multiple
containers and then i would be open to
yeah doing this for longer than three
days but
the fact is that people start using
those containers and then just forget to
to shut them down or delete them
afterwards so they tend to run for a
longer time than they actually need it
and with that limit to three days that
just get thrown away
the call to the proxy api are done
through a rest interface
and as i said is to create or delete
containers to get the status and to get
to get the logs
that rest api is a dotnet core
application um what that one does it
first of all creates a group managed
service account and i have a bit more
details in the next slides what that
actually is but it's needed for the
windows authentication so that we can
log into the container using the windows
credentials
if it is a new system container then of
course we need to restore our database
because it contains a kronos database
in the standard image and we also might
need to download our dlls that are
specific for that version from tfs which
is the on-prem version of azure devops
that you might have seen in the last
couple of days as well
and what that also does then in the end
is it constructs and executes a docker
run command so this does no magic
whatever um it just creates a rather
lengthy docker run command and that
leads to the container being created and
started
it also can get the running containers
and the logs and that is done directly
to the docker api because docker
provides an api just a rest api that you
can talk with it's a bit complicated to
use that's why we're doing some things
in powershell
but it's okay
and the last one of course is the
container itself we don't do any special
custom containers or any special images
those are just standard nav business
central image images for microsoft but
we of course do a couple of scripts in
specific settings
the first script we have is
one that grants an active directory user
group access to that machine
so when one of those containers gets
created it looks for our developer group
inside of our active directory pulls all
the members and enables them as super
users in the database
creates an nav user and then we are
ready to row to go
the second script automatically converts
the database on startup
um we need that because the backup file
might have been created with cu whatever
five and now we're trying to run cu 10
with that one so directly after startup
it tries to convert the database and
make sure that it works with the latest
cu
of course you can run into problems
there as well but it hasn't happened a
lot
we use windows authentication we use our
own developer license of course to get
access to our own objects we enable
click once to provide the windows client
um the old one and the seaside
environment because if you happen to to
need to create a hotfix for a customer
on an old release then you need that old
seaside environment as well or you might
want to test with an old windows client
and the easiest way to get those is
click once because then you don't want
to run into trouble with multiple
releases as well
we use something that's called
transparent networking that means that
every container gets its own ip address
and is rather easily accessible through
the standard ports so don't you don't
need to worry about networking too much
there
we have some custom nst and webclient
settings and then we set labels to
identify the releases as you might
remember in the list
actually you will see it soon
we know who has created that container
to be able to do some restrictions like
you can only delete a container if
you've created that one or if you're
part of the administers group and for
that we need to store who created those
and we for example do that through the
labels
so just to scare you a bit this is the
docker run command and actually it's not
that scary
the first part is just giving it a name
and a hostname and of course it accepts
the end user license agreement because
we just have to do that
um
then this is the networking stuff where
we use the transparent network and we
disable ssl usage because we just don't
bother internally
we enable click once
and now comes the part that is about the
group managed service account and about
enabling
those developers as users inside of the
database
so the security option actually
references that group managed service
account and tells it to use that to run
the container
then we tell it to use windows
authentication we create a standard user
in case something goes wrong and then we
let it know which domain and which group
we want to use where we put the pull the
users from and enable them
and then we have um that script grand
user access zip that you can see on the
very right and that one is responsible
for actually doing all that so calling
ad who's a member of that group create
them as users and so on
then this is the second script that we
use that invokes the conversion in case
we were running on later cu
and this is the part where we get the
the backup file from new system
if it's a new system container and where
we also get the dlls from
the tfs server and put them into the
container using a volume
and then you can see here we do two
custom settings the first name makes
sure that we always directly see if it's
a new system container or if it's a
standard chronos container and the
second setting just um
changes the threshold for the sql long
running statement logging because
otherwise when the container didn't get
enough resources on the host then it
started to flood with
with messages right from the beginning
and the
people using the containers were
wondering why they started the container
and immediately immediately got warning
messages
and this is the last one just setting
the labels so now i know that i
personally have created as an owner that
one and a couple of additional metadata
as well
and then we're using 2017 cu16 the
german version in that case
so oh no um
not what i thought
now how how do those group manage
service accounts work
i don't want to go into too much
technical detail because that is
actually quite well documented and also
quite boring if you're not
too interested but to just to help you
understand what the concept of that is
first of all you of course need to have
an active directory and that active
directory needs that guy which in my
case is the group managed service
account so that actually is just another
type of user but it's not difficult to
create you just create a new one it's
not a standard user it's a group managed
service account
then you have your container host and on
that container host you need to install
the group managed service account to
enable the usage of that group managed
service account there and then you also
have your sql server
if you want to connect to that sql
server using um using windows
authentication with a database and on
that database that group managed service
account also needs to have access
then we install a container or we run a
container on that container host and we
tell it to use that group managed
service account
what then happens if we make an outgoing
connection to the
sql database it will use that group
managed account and because we have
enabled that one before that will work
so that's just the base idea
you have that special user account
you're assigning to a container
the container automatically uses that
one to connect somewhere else
the same is true if you try to log into
that container then it will use the
group managed service account to connect
to your active directory and find out if
you actually are allowed to log in or
not
um so it uses that group managed service
account for all for all of the outgoing
connections
and with that i should hopefully have
told you enough
to see the container up and running
so let's see
there is the take days one
and now i can check the log
and i was fortunate fortunate enough
that it has finished
so what you can see here is just the
standard startup of
of an nav container
and the special things are happening
especially here
in additional setup
where we are setting up those
development users by first of all
importing the active directory
powershell modules and then we're
querying that group that you can see
here
and then we're adding all those users
and even groups and so on and so on and
so on
and in the end we get a link for the
webclient for click once and so on
and of course we also have provided
doses links here so
let's go to the click once
now i can install um c site or install
the the rtc or whatever i need to work
with that environment i can of course
also
access the web client
and that may might take a minute to
start
let's see
yeah but you know how webclient looks
like right
um
so those
additional information that you see here
like the owner
the nav released the cu the build those
are partially coming from the image and
partially from those labels that we set
so that we know what the version is who
the owner is and and all that kind of
stuff
okay um
i actually wanted to show you a bit
there
give me a second to remove that one
live powershell editing something you
definitely should never do but
here we are
so a couple of additional notes about
the the group managed service accounts
while we're running on windows server
2016 the group managed service account
the container and the host name of the
container need to be the exact same that
is a problem because every time you need
to you want to create a new container
you also need to create a new group
managed service account and of course
you can script that using powershell um
but it just adds an additional overhead
that's not really necessary and doesn't
help
and you also can do something like
dynamic scaling docker offers a couple
of mechanisms how you can do dynamic
scaling like i not only want one
container but i want three of those and
then then it just adds name underscore
one underscore two underscore three and
again this breaks the
fact that the group managed service
account needs to have the exact same
name so that really also is not possible
currently with group managed service
accounts but with windows server 2019
that no longer matters
the group managed service account as i
said is used for outgoing connections
especially the or not especially but
only then
if no other user was explicitly set so
if the standard accounts like local
system or network service is set
then the container will just use the
group managed service account when it
does an outgoing connection
the group managed service accounts also
don't have passwords so you don't need
to distribute something there or reset
or whatever
they are restricted to the machines so
when you create a group managed service
account you tell it on which machines
they can be used and then they are they
are just available there
and what you need to do is um you need
to download what is called a credentials
back file and it actually is just a file
that
knows which group managed service
account to use and then you reference
that in the docker run command
as a security option as we've seen
before
and if you want to find out more about
that one i actually think that is quite
well documented on on microsoft's side
there but if you happen to run into
questions that is
a topic where i've spent a lot of time
on
until i finally got it up and running so
if you start with that feel free to
contact me and i i'd be happy to help
okay
so let's see
where we are with the voting do you want
to vote again or should we just take the
second one
let's try again
i'll remove all the votes
no
just take the topic okay
um so let's go with multi-container
environments as a friendly request i'll
of course do that
um multi-container environments why do
we want to use that
there are multiple use cases for this
one of those would be that you have
multiple very similar containers that
you want to use and then we have more
complex scenarios the ones where we have
very similar containers for example are
our release tests because there we just
spin up 10 containers for 10 different
databases and they all just need an nst
and an is to allow the testers to
connect to the database but except for
that database and that name they're all
the same
so we need to have a stable and
reproducible and easily adjustable way
to do to do that
the second example where we use that
mechanism which is called docker compose
is on our tools host so one of our tools
hosts where we have different images
like there's an is running there's some
other tool running there of course also
business central instances running and
all of those are defined in that docker
compose file so this is like
infrastructure as code
you just define the infrastructure in
that docker compose file and if you
happen to throw away the host and create
a new one you just need to move over
that compose file which is stored in
your version control um
you start all those containers based on
the compost file and you're ready to run
again
and the third example that i've
prepared for you is our externally
available environment where we have a
couple of containers running that
third-party developers are using to
connect to web services provided in our
solution to build their own tools that
then connect to to our product
and there we have multiple containers
but you don't want to
bring them over to the internet without
any additional protection and for that
what we are using is a reverse proxy and
all of those nav containers and the
reverse proxy are all again together
defined in a compose file
in case you don't know how that works
that is the basic idea of a reverse
proxy so on the very left you have the
client that one connects over the
internet into the reverse proxy um in
our case we're using engine x which is a
rather popular solution for for reverse
proxies and that
then just distributes according to the
url to the different containers so we
have three containers up and running
there for different use cases and they
get the connections
so what actually happens um
they of course are defined in one
compose file that i will show you in a
minute
so what happens if a connection comes in
then that one is directed to our url and
then has um in the end of the url the
name of the container that we want to
address
that one gets picked up by the reverse
proxy and that one then has a rule that
tells it okay when that connection
request comes in then i need to route
this to the
container with the same name so now the
connection is up and running and they
can use the web client they can use web
services whatever they need to to
implement their solution
and as i've said already this is done
using docker compose composes a tool
that is also provided by docker
incorporated the company behind docker
um
you can just download download that one
and and install it
and what it basically does it has a
descriptive yaml file yaml is yet
another markup language so that is easy
to read as i show you in a minute and
there are all the containers defined the
networking is defined the configuration
for the containers is defined so you
just have one big file um where all the
information is stored that you need in
case of the scenario where we have 10
almost identical containers
we have a template in place and then use
a powershell script to generate those
compose files from the templates
so how does that look like
first of all i want to show you the
external one
so what you can see here is the services
so those actually are the containers
that are defined inside of the
um
of the compost
file
you can see here that it has a couple of
volumes so file system connections that
are brought into the current container
it has a couple of ports that is
actually listening to the outside
and then it is told to build a new image
based on the files that are in that
folder so this is one option inside of
the compose file to provide your own
container
image and that gets built as soon as as
that one starts but you can also see
here the alternative to that is to just
provide a standard image that is already
available so in that case we're running
dynamics nav 2017 cu5 the german version
and again we're binding a couple of
volumes so binding
folders in the file system into the
container and then you see the
by now maybe familiar environment
variables that we need to enter into
that one so we're not using ssl we're
using that database server you're using
that database instance and so on and all
this
as soon as you get the hang of that
pretty easily readable you understand
what is happening and it's also easy to
change
and this is the configuration for the
reverse proxy that just one knows if
someone comes comes in asking for that
connect for that specific connection
then it gets routed to that one if
someone comes in and asks for the web
service then i re redirect to the same
container but now using the web service
port and of course a different url so
that way we are able to just provide um
the web client and the the soap web
services to the outside world without
actually bringing the containers in a
connection to the outside world
the second sample
are the tools
now that one also is kind of familiar
again you see that we can have
additional tools or additional
containers in that case that's a
pertainer container which is a tool a
web-based tool to manage containers
then you can see in that case we use our
own internal registry to spread that
image and run that one as well
here we also have created a static ip
address so that we can use our internal
dns servers and our internal
ssl certificates to make that safe and
secure
and the list goes on here this is a bc
container again and so on and so on
and you can see here for example the
gmsa connection as well
and the last scenario for compost that i
wanted to show you
is the one where we have 10 identical
containers running for tests so we have
a base template that actually contains
nothing but the the bare stop of the
networking
configuration and the services
and then every every service is built up
in the same way and we have those
placeholders
marked with those two hashes so this is
the name that we change this is the
image that we use
and then we have the database server the
database instance and the database name
because they might be different between
the containers
and then we just have a powershell file
that contains all the databases that we
want to use in our case we need to know
which release we are currently testing
what database server to use for database
instance what image
and then that script just goes through
those templates and creates a docker
compose file from those and it actually
also creates the group managed service
accounts
the compose file in the end then looks
like this so now we have one of those
services one of those containers with
the name with the image
the security options the volumes and so
on so we just have created a new one and
if you decide to make some configuration
setting change that needs to roll out to
all of them we just change the template
run the script again and we're up and
running
okay
so much for the multi-container
environments um
something maybe interesting to note is
that you can change that yaml file so if
you only want to change one of the
containers and at all you can just
change that portion and tell
docker to update that and then it will
look at the yaml file and find out that
the configuration has changed for that
one container and it will remove that
one start it again and leave the other
nine
just up and running as they are
as i've already said that one allows you
to easily update or change your existing
host just throw the host away do an
update a new installation whatever
bring in the docker compose file start
it and you're up and running again
that one would also be dynamic
dynamically scalable so you can tell it
to use multiple containers for every
service for example you want to have one
sql server but
five i am five nst containers with the
same configuration then that could be
done in docker compose as well but again
that's broken because of group managed
service accounts in windows server 2016.
and then if you want to have something
more flexible you can look into docker
swarm that allows you to have multiple
hosts multiple virtual machine machines
which are called nodes
and then you just tell docker to run a
number of containers and it will find
out by itself on which of those hosts it
wants to put the container
that will also allow very flexible
networking with windows server 2019
onward the reverse proxy will be easier
so yeah there's really coming a lot of
goodness with with windows server 2019
and then there's something that you
might also run into when you're looking
into a multi-container environment which
is called kubernetes that's the solution
by google to do a multi-container
orchestration and there we should get
windows
general availability in the next couple
of months and then probably also windows
authentication sooner or later will
start to work
okay
so that's it for the multi-container
environments
now for
building extensions using something
that's called a multi-stage image
first of all again why would you do all
of that
why automated builds i guess that's
you you should hopefully heard the the
answer for that one already manually
building is not a good idea it takes
very long and you're sooner or later
going to make errors
um and you can also as soon as you have
the automatic builds in place you can do
it nightly you can do it per check and
you can do it weekly whatever but you're
sure to
quite quickly get the information that
something broke in in case you made a
mistake
why would you do that in a container now
if you think about building and then
additionally also doing automated tests
it's very important to always have a
clean environment because otherwise it
might happen that you make a change and
that change causes the next build to
actually succeed while it shouldn't have
succeeded or the next one breaks because
there's still some artifact from the
last one
in there
and it doesn't work anymore so the best
would be to just have a clean
environment for every step and that is
what you can very easily do with
containers because just for every build
step for every test for everything you
need to do you just create a new
container do whatever you need to do and
throw it away again
that brings you clean control and
repeatable environments to do your
builds and to do your tests
without too much overhead
now why don't i use just standard images
the standard nav bc image is rather
large
it's built as i said on windows server
core but it adds additionally a size of
about six gigabytes and if you want to
spread out the builds to whatever azure
azure container instances or just some
arbitrary host it always needs to
download that image make sure it
extracts that one everything works and
then it can start that
um so with a multi-stage image we can
drastically reduce that size
how does that work
here
so if you imagine our
big business central container image was
what does that actually
all include
we have an iis for the web client we
have business central itself and we have
a sql server inside of that one that's
the reason why the image is that large
there's just a lot of
things that got installed when the when
the container image gets created
and then it what we actually only need
to build our extension is the compiler
and are the symbols that are stored in
the database as soon as the um the nav
server starts
so
what we actually want is an image that
looks like this
how do we get there now if we start
again from our standard image bc sandbox
that's as i said windows server core and
six gigabytes of additional stuff
then we do something to get the compiler
a couple of scripts um
actually do that to get the compiler and
to get the symbols and that compromises
what is called our first stage so that's
the stage where we still have all the
binaries in there and and the big one
and then we do the multi-stage thing
that means that we tell it now i want to
have a second stage i want to start from
a clean slate uh start from windows
server core again and just copy
everything over that i need to do the
actual build
so now it's a lot smaller it only
contains what i actually need and if i
need to spread that around and run it on
a new machine it gets downloaded a lot
quicker it gets extracted a lot quicker
so in the end we will have our build
container that only contains what is
absolutely necessary
again how does that work
for that i
show you
in the source code for that one
that's the wrong one
so we have the docker file here
try to make that a bit bigger
so as i said the first stage is just
built on top of in that case bc sandbox
us as full
we automatically accept the end user
license agreement and give it a username
and a password
and then we just
run the standard start script but we
also have overwritten the c run my in
here
so what actually happens
is stored here so as soon as everything
is finished
it will
create a couple of folders those folders
will in the end create contain the files
that we need in the second stage
it will import the test toolkit
just using import enough application
object
and it will download the symbols from
the server just making get requests to
the
to the appropriate urls
so in the end we will have
an
application app file a system app file
and a test app file in our for build
stage folder that we then can use to
bring it to the second stage
and the al compiler is stored in the
in the v6 file that one also is
available in the container and we just
copy it over into the for build stage
now what happens oh sorry back to the
docker file now what happens in the
second stage
here
this is from windows server core so
we're starting up from scratch
creating a couple of folders and then we
tell it to use the first stage but only
the c for build stage folder and put all
of that into our build folder
and then in that case i expand the v6
file to get the the actual compiler i
download the sign tool i download our
signing certificate so that i can do
application signing after the build has
finished
and with that i have a rather small
build image
and we of course use that in automated
builds
to show you how that looks like
this just uses standard docker run
tasks that are provided by tfs
so it downloads the sources of our
extensions and then does the actual
build
by just running our custom built image
so this just runs
it maps the sources
and then with the scripts that we've
provided it just
creates the app file and if it works
then in the end we should have an app
file we also create the test extension
the same way again we should have an app
file and then we publish
the extension the test extension and a
couple of test scripts
if it works then
it looks like this
so you can see here the steps that we've
just seen
downloading the sources
building the extension
all this actually does is
do a docker run
of our image and then it calls the build
script inside um inside of that image it
does the compilation
as you can see here um now that one has
started
it has ended
here
and then this is the signing and in the
end we have a signed app file that we
then can use
for testing
testing just to quickly show you that
one as well is also done in tfs
and also of course in a container
that's the wrong one
so this just
runs our tests
in one environment because we currently
don't have more environments and as you
can see here with the limit or with the
percentage
not a lot of tests went well in that
case so we now have only one working and
six failures
but of course there are others where
just everything works
okay
you want to look more into the
continuous integration continuous
deployment there was a session by aj
gunner and camille who talked a lot
about that one the grumpy old guys also
talked about that one so you might want
to look into that one as well
um and then there was a session by
freddie and stan stampin at directions
which unfortunately wasn't recorded but
you also find the the blog post by
freddie that had there as well
now what we've seen just now is how we
can use a big image and through
multi-stage images
get that one a lot smaller usually it's
just the other way around um if you look
at something like a c-sharp application
then that needs a full software
development kit to build that's actually
bigger and then you just use the run
time and the the build application to
bring that one into um
into a target build so
usually it works the other way around
but in our case we just make a large
image smaller
you could also imagine something where
the first stage builds your dlls so it
does a.net ms build the second stage
builds the app as we've just seen and
then the third stage might be a business
central container that just gets your
app and gets your dlls and then you're
up and running again
so with that we are already at the last
topic azure container instances
um
what are azure container instances
now the basic id there is that you might
need to have a number of business
central installations up and running to
test something to demo something or
maybe for a workshop
and those azure container instances just
allow you to run a number of containers
without the need to worry about the base
infrastructure so you really just tell
it i now want to have one business
central container up and running and
that's it
you can start them you can stop them you
can scale up like now i need five of
those
you can sail down whatever you need
for example we did an internal event
where we needed 115 of those
environments so that people could start
to play around with business central
and we just used those with a
configuration of four cores and 12
gigabytes of memory we started them at 8
30 we stopped them at um 1 30 so that
meant that we had five hours where we
just needed almost 500 cores and almost
one and a half terabytes of memory um
i guess your local data center would be
hard-pressed to do that
and it really only took half an hour to
start all of those and it went quite
flawlessly
those containers are paid on demand so
that's the biggest drawback for all that
you get you of course have to pay for it
but the good thing is that you can very
well calculate how much they will be
because there is something called the
azure pricing calculator
um
so you just select what you want to use
in my case i want to do a container
instance then i can add that one
and now i can see okay
if i want to have one container for one
hour containing 14 gigabytes of memory
four cpus that would be 64 u.s cents
that seems quite cheap now if you start
to calculate that by multiplying with 8
and then multiplying by 20 then you will
soon find out that this is nothing that
you want to do on a long term basis
but of course you also pay what you need
so maybe if you're okay with
two cores and
four gigabytes of memory
then your aura only costs 27 cents
so really depending on your use case um
that might make sense we only needed 115
of those for half a day so that made
perfect sense as soon if you get into
multiple day usage and you can't really
switch them off at night or you want to
keep them running then you're probably
better off using
the vms that freddie provides where also
everything is taken care of but then you
have the full vm and if you want to run
that long time you also need to maintain
that um
so
again depending on your use case that
might be a very valid solution
now again what is the base idea and i
try to build up an analogy with
local vms connect compared to azure
virtual machines so if you run a local
vm that means you have to have your host
machine you have to have your host
operating system you have to have your
hypervisor citrix or vmware or hyper-v
or whatever and then you run your
windows server inside of of the virtual
machine so the little box on top should
be your virtual machine um with the
server sql
nav whatever
now if you run that one in an azure
virtual machine
that was too quick
in an azure virtual machine then all of
that gets taken care of for you you just
run the vm and the rest is taken care of
by azure i think that's a rather
familiar use case so with azure
container instances it's similar you
have your container host machine um you
need to worry about the host os and
about docker and then you just run your
container on top of that one and with
azure container instances all of that is
taken care of for you you just need to
worry about the container running
starting stopping maintaining whatever
you want to do there
now there are multiple ways to get that
one up and running
um the first one would be the azure
portal graphical user interface so just
the portal that you use um and i'll show
you in a minute how that looks like
also you can automate that using using
the azure command line or powershell
commandlets for single containers you
can use templates that are already
pre-created and i'll show you one
that does exactly that
so this is just um nav in the business
center container in the official quick
start template repository and then you
just click on deploy to azure
and then it asks asks things like which
resource group do you want to use um in
which location do you want to have the
azure container instance what's the dns
name and just a couple of inputs that it
needs and in the end you click on
purchase you create it and then you're
up and running
the same is true for azure templates
you of course cannot only run them in a
way that i've just shown you but you can
also automate that through azure command
line or powershell commandlets um and
then it works as well
you can also use my visual studio code
extension that one has an action that
just creates an azure container instance
for you so if you want to run some some
development you only need visual studio
studio code the al extension my
extension and then you kick it off let
it create an azure container instance
and you can start off developing
how does the scripting look like
now this is an example that we did um
exactly like that for the internal event
that i just mentioned and this one would
create one azure container instance
so of course it needs a name
um and the resource group to use and a
name for the actual container it uses a
template file that in that case i had
pre-downloaded but i also could do a
https whatever url there
i need to tell it how much memory it
wants to use so in my case for for
course and five gigabytes of memory
um where do i want to access it in that
case that's the prefix and then it
should be azurecontainer.io
what nav release do i want to use
what is the username the password and
as always except the end user license
agreement
and then we run that one as job that
means it just went to the background so
we can kick off one
we could kick off 115 of those
deployments and wait until they all had
finished and then we could start them
so
what does it look like when it's done
the problem that leads to a bit longer
startup for those is that it needs to
download the image again and as i said
that's a rather big one
yep
no that's the wrong one
the image is a rather big one so
downloading and extracting that takes
about
at least 10 to 15 minutes seems to
depend on i don't know what but um that
means that i can't just create one
because then you have to wait for 15
minutes and we don't want to do that
so here's a prepare prepared one that's
what it looks like i have the overview
for the container
i can see that i have deployed that one
through a template
i
can also see
that's the wrong place
i can also see the container instance in
here so this is how how the containers
in the azure port look like
i get the fully qualified domain name so
this is where i need to connect to but
we see that um soon as well and then i
can see that that one contains only one
container the basic idea of
azure container instances is that you
have a group of containers and you can
put multiple of those containers inside
of a group that does already work for
linux containers not yet for windows
containers but that should also come
soon
and then i have access to the log file
of
that one and for whatever reason you
always need to do a refresh once
so this is just the standard startup
and now we get
a url
if i were able to select that one
but i should still have it in my browser
history
yeah
so you can see here this is azure
container dot io so this is an azure
container instance that we are running
and
oops
of course i can just
log in
and we are up and running
um if i need to change something or
check something in there then the
container also allows me to do a
connection
by clicking on connect here
then i can
decide what i want to use in my case i
want to have a
powershell connection
connect that one and now i have a
powershell session inside of that azure
container instance i can import the
standard nav commandlets
and do something like
get nav server instance so you see
there's there's nothing special actually
that's just the same container that you
know the same nav that you know
or business center that you know it's
just running inside of an azure
container
okay
we've seen that and we are back at
questions and answers
and i'm happy to open that one so
a second
thanks for listening that's the moment
where you can leave if you want to
[Applause]
are they switched on
oh really and then test oh yeah not good
uh i have next scenario i have a virtual
machine in in the azure
and i'm deploying a
container with a bc sandbox with enough
container helper and i want to have an
access outside the virtual machine to
the container in the virtual machine
yeah
as i know i need to use sports mapping
and that's all
um you need to do port mapping you need
to make sure that the azure firewall
allows the connection to that one so you
have the firewall inside of the virtual
machine you have the
the azure firewall that you need to open
up and the problem is that your
container thinks it has some name but
because it is running on azure it also
has that west europe cloud app azure
whatever name so when starting the
container you need to add that public
dns name that's an additional parameter
in the enough container helper or at
least at docker run you can add that one
so then the con the container knows that
if someone externally calls it expects
that name and it will answer with the
right urls and ssl is not 1.3
say it again if uh ssl is not mandatory
i want to use connection via http yeah
you can switch off http if you want that
as well okay but actually what i would
suggest is the the standard image is
that freddy provides akms get bc they
are just doing exactly that i know but
the https
yeah okay then all you need to do is
take the standard script and do use ssl
equals n and then you don't have fssl
thanks a lot okay you wanna
okay
other questions
thank you i think you have done an
amazing job with these scripts and
automation automating these things and
i would just like to know if you have
shared these scripts or parts of them
um i think i have blogged about
everything and they're at least snippets
there's also some of those are on my
github repository but if you have
something specific that you want to have
just shoot me an email and i either put
it on github or send it to you there of
course are things that are very
dependent on our local infrastructure so
you might not be able to run it directly
as it is but you should be able to just
adjust it to your environment if needed
of course and i will start following you
okay
you taught today and we also heard
yesterday that it's not a good idea to
use uh docker containers on windows 10.
yeah can you give like more details
because we are now trying to use
actually this and we have sometimes
problem just like after each six weeks
we get an error like your login is from
untrusted domain and we can't really do
anything with it yeah
so that basically is um
three things that that cause problems
there the first one is that on windows
10 you're running the
docker community edition that's the open
source version it always contains the
latest bits and bytes the latest code by
code by docker but there sometimes are
errors in there
the second problem is that on windows 10
docker runs what is called
hyper-v isolation that means different
to what i told you on windows server it
creates a small vm and that that adds a
layer around the the container to allow
it to run and that also sometimes can
cause problems
and and the third problem that happens
is that you update your windows 10
that's windows 10 1709 1803 whatever and
the the container images are windows
server 2016 and sometimes you get
incompatibilities there as well so
that's why freddie provided a script
that allows you to
to check the the version of your host
and create an image that exactly matches
your host so i would suggest to to look
into the last couple of blog posts by
freddy so you can use the nav container
helper to create your own image that
should be better compatible with your
windows server windows 10 version
okay
the best thank you
so the question is um
during the cicd process you showed that
you created container from ls.
um to compile app yeah so uh what
happens if there will be some problems
in compilations you you will get just a
notification that there are some
problems or you can just export all the
problems for example um there are
actually two things for the for the
compilation i didn't did that didn't do
that yet but for the testing i take the
output and just convert it to something
that tfs understands so then you have a
better readable but actually the problem
is that the container will start
the start to run will stop to run and it
looks fine so that's why i had um one
part in there that says check if the up
file actually was created so if a
problem during compilation happens i
have the lock and of course the f file
won't be generated so then i know there
was an error yeah actually
just
continue this question
when i tried uh output from ls. it gives
only i think
maximum of 100 errors okay so uh if you
for example try to
um convert you know uh c
c l to a l and
and uh try to automate this
uh so you will not get all the problems
i guess that is something that the the
compiler needs to fix i wouldn't know a
way how to do that in a or how to
improve that in a container if the
compiler doesn't allow that
other questions
thank you do you use a share to
share the data when you're changing
containers
you mean
uh say it again please do you use a
share to
um to move the data around when you are
comparing containers
comparing bills i mean
ah okay no i actually just run two
different containers
and connect to those and then compare
the results
okay
uh you spoke about the gmsa i just
wonder if you want to set up the job
queue in the docker is that uh something
i think there was an issue that with
windows authentication either the
chopped you did or didn't work i'm not
sure which of the two of those two were
but i thought i was fixed i know there
was a problem but i have to admit i'm
not sure what the status of that one is
okay
thanks
other questions yeah
hi troy
hi
um are you using the later latest docker
builds for
for your management absolutely we're
pulling into any compatibility problems
i mean it does happen our app
breaks uh for the fully automated build
you use the latest docker build and then
it just breaks because something has
changed but
that that just happens but that actually
is the change inside of of navision and
it would happen without a docker
container as well
and i don't know i mean i mean just the
docker
the docker engine itself
i've been i've been struggling with it
on a standard
2016.
i have it as a vm but it's just standard
uh 2016. yeah and it's been a nightmare
to just
uh get docker to do the basic things
okay it won't create a network and and
stuff and i'm um i i use the dr msf ft
provider
and it
pulled the uh
i think it's 1809
the build
and uh it's it's it's been a nightmare
and so on msdn i was told no no you
should downgrade docker okay to i think
it was 1706. so i just wanted to know if
you you guys yeah six or nine was the
latest before that one yeah um
we actually haven't upgraded too many of
the hosts to 1809 that
the things that i've seen worked out
fine but a lot of what you've just seen
is running on 1709 still because it's
it's it's so silly because it's it's
just the uh just running the the
provider okay and it seems to install
but then the docker service won't
you know so it's nothing
okay i haven't haven't seen that one but
yeah i mean it's
the enterprise edition should be more
stable but of course it's not bug free
software so you might run into problems
and 1809 was released like i would guess
four weeks ago so that's just so
downgrading to 1706 might be worthwhile
yeah that that absolutely might work i
can assure you that everything that
you've seen works with 1709 that that
works so there's nothing new in what
you've seen that only works with 1809
okay okay
other questions
someone sure
can i use port sharing
with the different containers no do you
have to map them to different ports but
as far as i know you can't share ports
with them okay
other questions
nope that seems to be it so thanks a lot
for coming
and uh have a nice day
