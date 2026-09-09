# NAV TechDays 2019 - Migrate your customers to the cloud, and manage them there

- **Source:** https://www.youtube.com/watch?v=xI8bVsC2fTc
- **Video ID:** xI8bVsC2fTc
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 90m04s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

[Music]
welcome everyone
um to this session about moving
customers to the cloud let's start with
a quick introduction of the speakers
estimate do you want to start yes sure
hello my name is esteban i work as a
software engineer at microsoft in
business central
and i work mostly with cloud services
everything about managing your
environments in the cloud making sure we
create all the appropriate
infrastructure and many of the things
you will see here today
yes hello my name is roman i'm the
engineering lead of that team
and my name is christian and i'm an
architect in the business central team
and i work on many things but i'm very
passionate about cloud in general so now
you know us and we also want to know you
or we actually have some expectations of
you because we designed this
presentation with a specific audience in
mind
so
we expect that many of you are resellers
of us of business central or nav
and that you have many
customers on-prem
and that you have an interest in moving
those customers to the cloud so we hope
that that's the reason that you are here
so our goal today
is quite simple
to
convince you that the cloud is ready for
you and for your customers
and we're not going to pretend that
everything is perfect in the cloud
because we know it isn't we have work to
do and there are some limitations that
means that the cloud is not ready for
everyone but we do believe that it is
ready for a vast majority of customers
already today
the way we're going to convince you of
this is by showing you basically how you
can take a customer and move
him or her to the cloud
and manage them there after you've done
it
and after you've seen that we of course
let you make the final decision to
determine whether you are ready or
not the rest of the presentation will be
divided into four parts
number one
is about migrating your customizations
to the cloud meaning your code making it
cloud ready the second part is about
moving the customer data the databases
to the cloud
and the third section is about how we
manage your customers once they have
been moved to the cloud and finally
we'll talk about how you can deal with
scale as you get more and more customers
in the cloud
so let's get started
and i want to start with a
high-level view of what it takes to
move a customer to the cloud
so here we have an example where
we have an installation of nav 2018 as
an example on prem which we want to move
to the cloud so we have a database that
has all the customer data in it and we
have
an application and it is written in cal
probably heavily customized
and maybe you also have some ale
in there already
and our end goal is to get it into the
cloud
and in the cloud we are running
business central version 15 or bc 15 as
i'll just call it from now on
which was the version we released in
october
so in the cloud if you are in the cloud
you also have a database with the data
just like on-prem
the application is different however
because as you know in the cloud or on
bc15
everything is ale now no cal
and that also means that everything has
an app on extension so what you will
always have in the cloud is the
microsoft
system application and waste application
you might have
zero one or more appsource apps
installed and you will probably also
have a pertaining extension with the
changes that are specific to that
specific customer
and what about terminology so we
sometimes say extension
or app or application
but it all means the same thing on a
technical level at least
so you might hear us say different
things but just think they are the same
app extension doesn't matter
so this is our end goal
now how do we take our on-prem customer
and move them to the cloud
well i find it most useful to think
about the data first
so if we look at the database in the
cloud it has a schema it has tables and
it has columns
and what determines those tables
well it is determined by the apps that
you have installed on the on that
environment so the system app defines
some tables they end up being physical
tables in the database
the base app defines some tables and
they also end up being tables in the in
the actual database
similarly with appsource and with the
pce they might define tables or table
extensions and they end up being tables
in the physical database that's no news
so the cloud schema is determined by the
applications that were installed
the database on prem however has a
different schema
it is just different in a number of ways
let's call it the old schema because it
is the one we're moving away from
and it's difficult for us to move that
data to the cloud because the schemas
are so different
so what we have to do is have a middle
step
where the data is in a format that is
very very similar to what we have in the
cloud
so we need to convert our on-prem data
to a format that is ready for the cloud
so this database in the middle
how do we get it how do we get the
schema to be that way
well as i said before the schema is
defined by the f's that you install on
your tenant
so what you need to do basically is to
recreate oh sorry let me just say once
it's in that state we can migrate to the
cloud the way to get it into that state
is to install the exact same
apps
on-prem as you have in the cloud
so you have the base app you need to get
the base f15 system app
from microsoft
if you have a need for i3 solutions you
need to get the apps from them and then
you can design your pc as well on-prem
once you have done that and installed
those the schemas will be
identical and now we are in a good
position to migrate the data
now in order to go from nav 2018 to this
pc15 we need to do
an upgrade
and not only that we also need to
refactor our code to be pure extensions
so no code customizations of the base
app anymore
this is the overall process for getting
from on-prem to the cloud
what i'm going to talk about now is the
big red arrow about operating from nav
2018 for example to bc15 and after that
estimate we'll talk about the actual
data migration
so at a very high level this was covered
yesterday in two sessions so i'm not
going to go into details about how to do
it but at a very high level what we
recommend is the following
first
while you're still on nav 2018 refactor
as much as you can to extract your
customizations into separate objects
leaving the customized objects that you
do have as close to the originals as
possible
because that just sets you up for an
easier time when it is time to finally
extract
them fully to become a pure extension
then you perform the actual upgrade to
bc15 and that involves among other
things
a conversion to al code
as well as the data upgrade
now that you are on bc15
you can do the final extractions
utilizing events and the other
extensibility mechanisms that we have
and
to extract those from the base
application to become a pure extension
so
i'm gonna
not exactly demo that because
i'm not gonna do it i'm just gonna show
and illustrate what it is that you need
to do
so here i have a
nav 2018 installation and i have
customized it and you see i have
customized the
customer table here let me just
zoom in on my changes so it is not a
huge customization i'm sure you have
more
customizations than this one
and you can see that i have customized
the customer table i've added a field
and changed some code
i've also customized
the customer card phase
to add a field and i have also added
three more objects this is a reward
customization so that for each customer
i can assign a reward level that
determines how much discount they get
so as i said before the task first task
is to refactor as much as we can away
from these objects 18 and 21 and into
separate objects
to set us up for a successful upgrade
so let's switch to
the end result simply because i'm not
going to do it
now i have an extension here which has
my three objects as before
and i haven't modified or customized
anything anymore because i've extracted
that as extension so here i have a table
extension instead of the customization
and i have a customer card extension
instead of my page extension before
so i've done all this work i know
i'm cheating a little bit here or very
much
but this is the end result and now let's
install that locally i'm going to press
f5 to have it published to my local
environment
and i just like to show you the
functionality that we added so let's go
into a customer let's go into a datum
corporation
and you can see that we added a field
reward id
and i can assign
bronze gold or silver
but i just want to make a few data
changes just to illustrate that these
changes
we want those changes that i'm making
now to end up in the cloud afterwards
so let's make a few more
changes here
go to the rewards setup page let's add a
new level
and they'll get 30 discount
and let's assign that level to
a date from corporation
like that
so
actually by now i have moved to the
middle state as i showed you before so
i'm
now in a good position to upgrade
because i have done all that work
there's no rush though i don't need to
rush into upgrading i can actually stay
on this in this in this state for
as long as i like like weeks or months
the customer can run like this just fine
but since we are interested in moving to
the cloud i'm going to take the next
step
and prepare for that
so in my local environment i have
installed my app now my rewards app i
need to install the same app in the
cloud because as i said we need to
install the same apps in those two
places
so i'm now going to move to my cloud
environment and you can see i'm in
business central says and i have a
production environment here and i would
like to
install
the extension there so i'm going to go
to the extensions page
and
upload my extension
and now i need to find the
path
where did i put it here
and
paste
and now
i will upload it publish it and install
it
and this will take up to a minute i
don't think i want to wait for that
so
this point i want to move back to the
presentation
and
basically say that my part is done even
though i cheated a lot so i've now
executed on the big red arrow i have a
pc15
where
i have all the right apps installed i
have my data in a database
and i have also installed the pce in my
cloud environment
so now i'm actually ready to do the
migration at this point all we really
care about on-prem
is the database
the migration through the cloud is a
database to database operation
and i'm going to hand it over to esteban
who will now explain that process
thank you christian
right so
the hard part is basically done
all that's left now it is smooth sailing
with migrating your data nothing can go
wrong there obviously so before we get
started and we're going to do this
together um just some requirements that
uh i should mention in case you want to
try this as well
first of all
on your cloud environment you need to
make sure that you have the intelligent
cloud base extension installed this is
installed by default on all new
environments you create in in bc cloud
so if you didn't remove it you have it
and the user that performs uh the setup
that we will perform here
must have super permissions that's also
a requirement now in terms of your
on-premises environment like christian
already mentioned you must be on bc 15.
your tenant database compatibility level
must be at least 130 which means you're
running sql server 2016 or later
and we only support database sizes lower
than 150 gigabytes for now
although it is highly recommended that
if you uh move to the cloud that you
keep your databases there under 80
gigabytes
so for this demo we're of course going
to use a very small database so none of
this is an issue
now
the first step is what christian already
mentioned it is about verifying your
extensions make sure that everything is
installed in the cloud the same as it is
installed on premise for all the apps
you want to migrate
the data that gets migrated is
determined by the extensions that you
install in the cloud if you have any
extensions remaining on premises that
you didn't install that data will not
move with you
and
also
if you have some things installed in the
cloud that aren't installed on premises
you will see warnings saying that
certain tables weren't migrated from
on-premises and we'll see how that looks
like
also
when migrating data if you have some
tables that you don't want the data to
migrate then you can set the replicate
data property to false in your al code
and then that will
indicate that to us that you don't want
to move any data from that table and we
won't now once you've done that
we actually have a very handy wizard
and all you have to do is follow a few
simple steps and we will set up a
connection
of sorts between your cloud environment
and your on-premises environment
the high-level steps here are you need
to provide the sql connection
information
to your on-premises database this does
not have to be accessible from the
outside it could point to a server in
localhost for example but you still need
to provide the connection string
you need to configure a self-hosted
integration runtime i'll explain more
about how this works in a bit
but if it's the first time you're doing
it will look something like this you
will reach a page in the wizard with a
link to download and install this
integration runtime and you will also be
provided with an authentication key once
you install the wizard the first time it
starts it will prompt you to enter the
authentication key so you just enter it
there press register that's it you have
it running
additionally to that you could if you
have tried this before you might already
have such an integration runtime running
you can just use an existing one that
you have configured in the past
once you've done that and we are able to
successfully connect to your database
you will then be prompted to select what
companies you want to migrate you don't
need to migrate all the companies
necessarily and you can set a schedule
if you want optionally
to replicate the data be it daily or
weekly and we'll see how to do that
now
why don't we try it out
good
so
i am in the same cloud environment
christian was using
if i go to set up an extensions and go
to assisted setup
you will see that actually the first
option i have here is to set up cloud
migration so i'll just start this wizard
here uh yes privacy notice accept some
terms uh then select the product you're
migrating from in our case it's business
central to business central so we'll
pick this
and now here in most cases uh we are
assuming that you are running
on-premises so it's an on-premises sql
server we will provide the connection
string i have mine stored securely in
this text file
and in my case because i have already
done this in the past i have an
integration runtime installed so i'll
just reuse that one
once you have done the same you'll see
that you you will get this integration
runtime configuration manager and this
part that says integration runtime
that's the name that you are supposed to
enter
i have it in this text file as well
and i'll just enter that name and click
next
now this process of setting up the
connection can take about two or three
minutes so in the meantime i'll explain
to you what's going on
this is our starting point right you
have some on-premise database server or
servers
and you have a
database somewhere in the business
center cloud that represents your cloud
environment
what happens when you actually want to
run migration from on-premises to the
cloud is that our service will use an
azure service called azure data factory
amongst other things azure data factory
is an orchestration service for data
movement that can move large amounts of
data from various types of sources to
various types of destinations
azure data factory is the one that then
communicates with the integration
runtime that you have installed on
premises to tell it what to do and to
orchestrate the moving of this data
however
we cannot expect everyone to be happy
with services talking into their
on-premises servers many organizations
also would just not allow that for
security reasons so that's not really
what happens here what happens here is
in every stage of the migration pipeline
azure data factory would just put the
next set of instructions into a queue
that the integration runtime is
listening uh on from time to time so it
is actually your integration runtime
that is just checking if there's no work
to do and nothing is calling into your
servers
now because you have provided the
connection string this connection string
is sent to the integration runtime to
talk to your on-premises tenant database
to prepare the data and to then finally
send it over by prepare the data i mean
it will run some stored procedures move
copy some data to some extra tables and
then write that back and then azure data
factory we'll just write that back
directly into your on-premises database
some information some important points
to note here
all of this is
very secure we take security very
seriously everything is encrypted when
it goes over the wire the credentials
that are passed down to talk to your
database are safely encrypted as well
using a windows secure
encryption interface for
and we don't modify your own premises
data although we do need to create some
tables and run some procedures in your
database to prepare the data all your
existing tables and fields and data are
not touched
and
also
the data that we move is purely sql to
sql we are not storing a copy of this
data anywhere else it is moved from your
on-premises database to your cloud
database
another interesting point here is that
because
you can reuse this integration runtime
it allows us to actually
do this for
multiple databases in the same server
you only need to install the integration
runtime once and you can
move various customers that you have if
you have them on the same database
server in some on-premise machine
to the cloud without following that
first step again
the way you do that is what i did and i
showed you here is you just enter the
integration runtime name in the wizard
now
let's go back
to our wizard good
it has successfully
created the pipeline that will be used
and it's now showing me a list of my
on-premises companies and i can select
which companies i want to migrate i will
migrate this contoso mig company
and then i can also set a schedule if i
want
the migration to
run
reoccurringly but recurrently but um i'm
not gonna do this right now so
that's it we've set up the connection um
the way
you now manage this is by accessing a
page that we call cloud migration
management
in this page you can do various tasks
related to data migration i'm going to
just start by running a migration right
now because
this initial migration takes about five
to seven minutes and so i can get a head
start on that while i explain a few
other things
every time you run this it will take a
few seconds because it needs to verify
that your database that it can still
communicate with your database that the
azure data factory instance is reachable
but then
you can just continue
doing other things this will run in the
background
so
let's talk about a few important things
related to this page and to managing the
migration
running migrations yes
you can run migrations on demand like i
just did you just click the run
migration button and it will perform a
migration at that point or you can set a
schedule like the wizard offered you to
which can be daily or weekly
you determine when and what at what time
we do recommend that when you run a
migration you do it outside of business
hours where when your system on premises
is not being used
that's just a general recommendation
the first run which is the run i'm doing
right now will migrate all of your
existing on-premises data we we don't
have any of that data in the cloud yet
however subsequent runs for example if
you've if you've set up a schedule
they will only
migrate the data that has changed since
the last time that we replicated the
data by using sql change tracking which
also saves a lot of time if you have
larger databases
if something happens and you just wanted
to just migrate all of the data again
you can always reset the status via the
reset cloud data action in the
management page and that will cause the
next migration that runs to be a full
run where all the data gets copied over
again
some very important points here
when we are migrating the data from
on-premises to the cloud we will delete
data in the cloud that you have you
should not be using
the cloud environment while you're doing
these things as as any sort of
production environment you should not be
writing or updating records because it's
a point where we are just trying to move
your data and you should not change it
because then it will be out of sync with
the on-premises data
all your business processes of course
during this period must be still done on
premises
and once you are ready to fully move
after you've tested it and if you're
happy with it remember to also disable
the cloud migration setup which you can
perform via an action because that will
make sure to delete the the pipeline
from azure data factory and
there will be no opportunity for data
being moved by accident
now
while we do move
a lot most of your data
there are some things that we don't move
over uh one of those are your users and
your permissions
uh the reasons for this is because in
the cloud we only support using azure
active directory authentication and
we well it must be configured to the
active directory tenant your environment
belongs to while on premises you might
have any kind of setup you might be
using windows authentication you might
be using nav user password
authentication so your users are just
not migrated at all
neither are your permission sets
although you can add permission sets to
your extensions and that's a valid way
to move them but if you have any custom
user defined permission sets or anything
you will have to recreate those
um all your non-super cloud users for
example users that aren't the one that
is running the setup they will
after you've run it will be assigned the
intelligent cloud permission set and
they will be assigned to the intelligent
cloud user group
and this will revoke any write access
they have in the cloud environment but
it will give them read access to
everything
this is also to prevent people again
from making changes in the cloud while
you're still moving your data over
you can
if you want to restrict their read
access further because at this point
they could read everything you can just
copy this intelligent cloud permission
set and remove some permissions that you
want users not to have
any actions and action groups that those
users might have had access to when they
had write permissions will just not be
visible to them if they log into the
cloud environment instead of just
getting a bunch of errors
good so before we talk about the next
topic
let me just check if this is completed
good so let's switch over
now you see my full run has completed it
took about four minutes
and if i look at this migration
information for example you can see some
statistics it migrated data from 273
tables successfully
there are some tables that are not
migrated which i mentioned before that
you'll see warnings for these are mostly
tables that
for example other extensions i have
installed have decided that they don't
want to migrate that data
or some user and permission related
tables you can have a look at this at
any point
so let's have a look
into our company now
i'll just switch over to the company
that we just migrated
good
and
let's go to our customer list
and see if
you know the data that we expect is
actually there
yeah it is so
our adatum corporation is a platinum
member and platinum which is a table
change christian had made before also
migrated over
so let's try one of these
subsequent migrations
that
should take less time and only migrate
changes i'll just start it again
and then we will continue
good
now
let's talk about
another
um issue you might encounter
it is not uncommon for you to have
tables like the following right you have
let's say an orders table and you want
to make a reference to one of your users
uh for example you reference the
username in the users table as saying
hey this user created this order
well
it is not a given that that user in the
cloud will have the same username
because the username in the cloud will
be determined by their authentication
email so someone that was john doe on
premises might be jdo now and therefore
once your data is moved over these
references don't work anymore
for this we have a handy action that is
allows you to define user mappings
where you basically just say actually
on-premises john doe is cloud jado and
all this does is very simple it will
rename your cloud
user to match the username of the
on-premise user and then that will
restore that relationship for you
there's various other actions
that we can have a look at as well in
the page
so
for example here is the user mappings
this shows me my on-premises user i
could just then go ahead and pick up my
cloud users press ok and it would just
rename
the
cloud users
if you prefer this actually does the
same thing as renaming a user in the
user's cart page so if you just want to
go to your users list and manually
rename your cloud users that's perfectly
fine and that would also do the trick
there are some other handy actions for
example
you can reset your runtime services key
that's the authentication key you had to
configure in the beginning in case you
think it's been compromised you can get
it again if you uninstall the
integration runtime for some reason and
want to install it again
you can change the companies that you
migrated let's say you started with a
test company it worked fine now you want
to add an additional company and there's
this handy checklist as well and this
checklist will
kind of tell you the steps that you
should be doing during a migration and
you can dive into it and make sure that
you've done everything and you're not
forgetting something
and
at this point we haven't tested anything
and
i know it can be
um maybe a bit odd to to tell you don't
write any data right don't perform any
non-read action in the cloud while
you're migrating because
you you of course want to test that
things work
and for this
what we recommend is testing in a
sandbox environment
we allow you to create a copy of any
production environment you have into a
sandbox environment it will have the
same data the production environment had
at the point that you made the copy and
there you can just
you know test everything assign write
permissions to your user execute all
your actions and your production
environment and its data will be
unaffected when you create this copy
the data replication is also no longer
connected to the sandbox so then there's
no problem of that test data being
overwritten and that's a
we think a good way that you can verify
that everything is working
and i think these are
the high level steps that you need to
perform you saw it doesn't take very
long of course my data was rather
small but it's very simple to get
started and i also
wasn't migrating a production customer
right now you can really just have some
test environment with some data
connected in your cloud environment see
if it works for you it's very simple
with that i'll hand it over to roman now
to show you how to manage your customers
in the cloud
good
so you have brought your environments
into the cloud
and
now
how how do you manage these environments
in the cloud
so in the next couple of minutes i'll
walk through the different management
operations
some telemetry
and support options how how this can be
done in the cloud
so for this
we have
created
the admin center
let me show you
so
in the business central admin center
which you can reach under
businesscentral.dynamics.com
and then it's the aad tenant id
slash admin
here you can see
all your environments so production
environments
sandbox environments
which version they are running in
which country or localization they're
running
so what type it is
and also the direct link to the
application
what we see here the first one is the
production environment that's the one
that
we have been thinking
over
and so let's follow up on what what
esteban has said how how to do a copy of
that environment
we can create new environments and
delete environments here
let me just refresh this
so we can create and delete environments
here
and in this case i want to take a copy
of our production environment so i'll
say it's going to be a sandbox
we say copy
from production environment the country
is going to be us and we can see the
version that is pre-selected it's
basically the same version as the source
let me put
a name here so we call it sandbox copy
and start this so this will this will
run for a couple of minutes it will
create a copy of the environment into a
sandbox
while this is running
let me go back to the presentation
so we have the
admin center
for you to create and delete
environments you can work with
production and sandboxes you can copy
your production environments to a
sandbox and what we have enabled with
the last release as well is the
possibility to have environments in
multiple countries
so in our case our contoso
tenant has environments in the us but if
they let's say want to open
a chocolate selling business in belgium
they could go to the admin center and
create a new production environment for
belgium as well which would then have
all the regional
customizations or localization yeah
so one of the first things
then we will be doing is to set up
notification recipients
this is a possibility for you to get
notified
if
something in your environment is going
to happen or happened
these are at the moment email
notifications for example when the
environment is scheduled for an update
if that schedule date has changed
if the update succeeded or in case it
failed and then there will be some
explanation of why it failed some
reasons
and also there will be a notification
sent if there are any ptes so pertinent
extensions
that would not work
in in a new version and where the
compilation fails
another important aspect of
these
environments in the cloud is
we need to set the update window
and the update window is essentially a
maintenance window that you can set for
your environments
where then microsoft will do all
maintenance operations
outside of business hours in this update
window
so let's set this up
i go back to the admin center
first thing we'll do we'll set up the
notification recipients you can see this
here
we see christian is already registered
let me add myself
so i will get
notified now if there's a new update
available
or any of the other notifications will
be sent
then
we also want to set the update window
so
we go for example for our production
environment i'll select it and then on
that details screen we can see a bit
more information about about the
environment
let me scroll down
so we can see here that there's no
update window set
and we can do that so i'll set the
update window
and you can see here this is a local
time
if we want to do that in the night
let's say between 10
and 4 o'clock in the morning
then we will ensure
that any security updates or patching
will happen
inside that update window to not disturb
the business operations
so i'll save that
good so we have
the notification recipient set and the
update window
and
let's go fast forward a little bit a
couple of months into the future
and
we have a new version available
as we have
the notifications set up
you will get a nice email notification
bit like this one it will say hey your
business central is about to get more
exciting
and you can see the date when the update
is scheduled
you can see the time
you can see which environment is
affected and
from what version
to what version it will be updated
what this email also says is if that
date and time is inconvenient
you can reschedule based on on your
convenience
so in this case we see that's the 24th
of november
and uh i believe that's
that's this weekend right it's sunday so
that's very inconvenient i think you
wanted to do some
beer tasting and more sightseeing here
in belgium right
so let's change that data
i go back to the admin center
go to my environments
and in this case
it also tells me already so that there's
a new update version available
updates will begin and we actually have
a
two week window in this case where we
can pick an update date
so if i go to update
and say schedule
and we can see yep so current version
and it allows me to pick a date
so the earliest date is here the 23rd
and we have a time frame of
about two weeks until next sunday
so let me pick next weekend saturday
next weekend and i say let's schedule
that
so what we'll do behind the scenes
is to to mark that environment for
update
on that day and it will run
in the maintenance window in the update
window during the
during the night
so now you might be thinking
this is all nice
but what about troubleshooting so what
if the environment that is running in
the cloud has some problems
how how do you investigate i mean you
have
very little control there
but we have a few possibilities for you
to investigate so the first one i want
to mention is application insights
this is a really cool feature it's
actually part of azure monitor so it's
not a business central specific
capability it's part of azure and it's a
very powerful
monitoring and telemetry solution
it provides monitoring alerting
analytics tools you can you can write
fancy queries and it's really a great
tool to diagnose issues and see and
understand what what users are doing
with your app
so how do you set that up
we go again to the admin center
start from the environments
and
what what is nice here what i want to
emphasize it's your application insights
accounts
that this will be admitted to
so we can go to our environment let's
pick our production environment
and we have here at the moment we see
that there's no key set
right so then i can say here set an
application insights key
enable it and now we need
an instrumentation key
so where do we get this from
so i have created an application
insights account before
let me just refresh
the instrumentation key is here
i'll just copy it out
and
put it here
good
so now while this key is applied and set
so there needs to be a little restart
done of the environment because that
information is set as a parameter during
startup
of of the of the environment
um
so i want to
quickly um
give a little disclaimer so at the
moment
this
application insights integration is in
in beta mode in preview
and we provide
information about long-running queries
into the telemetry at the moment
so a long-running query is configurable
but at the moment it's set to any query
that is longer than
one second
and
we are going to add more and more
events
and telemetry into that channel into
application insights so we started with
these long-running queries but we have
discussions about for example
providing information about report
runtime
or
soap calls or data calls how long those
take
general errors information or also job
queue telemetry so we will be
continuously adding features and
functionality
that we find is useful for you to
investigate
so let's have a look
at our application insights account i
want to show you two very
cool things
so this is set yes we have the key set
the environment is back active
let me go to my
app insights so two features that i
think are very useful at
at the moment in in our context is a
search
so as i said we show long-running
queries and we can do a simple search
here so if i search for
sql any trace event
related to sql in the last 24 hours
we actually get some long running
queries here
what is nice you can then drill down
in in more detail and see
yeah this is a warning we see that the
action took longer than the given
threshold and we can look even in more
detail let me make this a big bit bigger
so we have these uh trace properties we
can see when this event happened what
happened
and we also see and i think this is the
really cool part
what sql statement was executed that
took so much time and where this one
came from
so we have the al stack trace here we
can see this was a page extension
app object id 50100
and
some extension from customer list
on action that was triggered
and you see also who created that
extension so in this case
it was me
and i'll show you
how we can look into that a little bit
in more detail
so we also see i think that's also
relevant which environment and what
environment type that
the trace come came from and so from
here this is a very good way to
investigate performance issues
yeah
so i said there's two
interesting ways to look at the data one
is the search i have also set up an
alert because you
maybe don't want to look
every day and do a query and search
there's very powerful alerting
capabilities where you can
set up your own custom rules
that trigger alerts then and you can
also have different ways to react
to those alerts in in my case here i
have set up a simple email notification
that will send me an email if a certain
number of these
slow queries
occurs in a given time frame
and then you actually have an overview
like this
where you can see you can actually set
the own severity that you want and you
see how many alerts and when
when these alerts were triggered
and from here we can also drill down
so we have multiple of these events that
were triggered in the last 24 hours
so
one of the other cool things i think we
can do here
is
if i look at my extension so this is the
slow extension that i wrote
we can put a break point
and see what is going on
so let me say i put a breakpoint here
and this extension
is running in my sandbox environment
if i press ctrl shift p i get the
command palette here and i can
debug
without publishing so let me try that
so this is opening
the sandbox environment in the cloud
we're logging in and we're on the
customer list page
so i know
this button will trigger my
functionality so let me try
and we can see already here the the
window is flashing
the breakpoint is triggered
so i think this is pretty cool we can
debug
in the cloud
and take advantage of all the
cool
functionality that the
visual studio code
has
so we can just
let me go through these lines here
and you can
also take advantage of the information
that we get for example on on database
calls and
and drill down and and
see basically what is going on
so i think this is really cool one
disclaimer also i have here it works
only in sandboxes
yeah and if i go back let's go back to
my presentation so
if we look at troubleshooting
at the moment you get information about
long-running queries
with information about the context
and details
you can set up flexible alerts in your
application insights account and you can
debug your apps in sandboxes in the
cloud
so what if all that didn't help
and you may want to do some offline
troubleshooting
so we have also with the
the last release in october enable the
functionality to export
your production databases into a storage
account
so this would allow you to
for example take a backup on a regular
basis
or
take that backpack and put it on an
on-premise installation and run it there
or you can do essentially whatever you
want with the data it basically means
you're not logged in in the cloud
this is one of the top asks from you
from our partners
and this is possible now
so
actually i have a t-shirt here um
where would you go
now to do a database export
anybody
select the environment
correct yes to the admin center yes
so i go to the admin center
and yes you paid attention we actually
have a database
button here
and we can create a database export so
this is our production environment that
we brought in
through the migration we synced it
and
we want to take it out again
so here i have the possibility to create
this database export
it proposes me a file name so this is
going to be a backpack
and a container name
so what i need now is
the location where to put that
database export in a blob storage
so if you click here actually there is
going to be some
some explanation of how to get that
let me show you
just need to find the right window
here we go
yes
so i have a
storage account created here
and what we need is a sas token so a
shared access signature token
we basically need access for blob and
file
disable a couple of here
one thing that is important to know for
big
databases that operation to copy the
entire database out into the blob
storage can take a couple of hours so
make sure to produce a token that is
valid
long enough for the operation to
complete so in this case
that is going to be enough time and let
me generate
this token
so this
will give me this blob services sas url
i'll copy this over
go back to the admin center
oops
paste it here
and
let's go
yeah so this queued up the export
request that will run for a couple of
minutes
and
it will show up then in the storage
account
yeah so this is actually a run that i
have done before earlier this morning
the other one will also show up here in
a couple of minutes
now
if
your customer needs help so let's say
they're in the cloud you have your
environment in the cloud if your
customer needs help
we have the possibility to set
your contact information in the admin
center and then it will show up
on the help and support page in the
application
so i think this is a very nice way
to
give that
first level of support to your to your
users
so we can also do that if i go
again
to the admin center
and we have a section support here
so i say manage support contact
and let's put
myself
here and save
so now if i go back to our
production environment
and here under
help and support
you can see
the version that is running and yes
we see if the users
need technical support
um they can they can contact
me here at uh my email address um with
some more context information on what is
the tenant and so on and then basically
it's a possibility for you to to help
directly your users
so this is if your customers need help
what if you need help
what do you do then
so one of the things we have also
enabled in the admin center is the
possibility to create a support request
directly from the admin center
and we have a functionality that we call
the red button
so first
if you need help we can
have a
possibility here to create a support
ticket this will bring us to the power
platform
admin center
where we can directly create a support
request that will go to our support team
so this is
again here it's on the top right corner
new support request
and then
finally the red button so the red button
is
basically a direct line to
our engineers
if there's an outage
a serious problem
with the tenant
for example if no user can log in or
you cannot access any api or the web
services are not working so this is
really for the
disaster outage situation
you can create here a
report of a production outage and we
will get
information about the environment and
all the context details
put your contact information
and
somebody from microsoft will reach out
to you
so now
this button should be used
with care responsibly because that means
actually that an engineer will wake up
if that happens during the night
of course we will do everything to
prevent these things from happening but
sometimes it does so we want you to know
that there's somebody always
there that you can reach out for help
so i think this is a
quite a
great set of functionality that we have
to manage your environments in the cloud
we have possibilities to provide help to
create a backup
and
i'm actually quite excited to
to have you try this out
so
can you turn this on yes thank you
so roman walked through all the
management capabilities that we have in
the in the cloud that enables you to
manage your customer after you've moved
them
so
what happens when you scale because
that's actually a thing that happens
when you're in the cloud the cloud
business model is different
and what we often see is that
customers are smaller they require less
customizations in the cloud the
implementations are quicker so the deals
get smaller on the other hand you are
going to get more deals so you're going
to get
many customers what happens when you go
from one customer to 10 customers to
hundreds of customers perhaps
furthermore each customer can have
multiple environments because we just
saw how easy it is to create multiple
environments so
it kind of explodes the number of things
that you have to manage so the question
is how do we handle
it when this scale hits it's a positive
problem after all but how do we handle
it
so the answer of course is automation
and you will be pleased to learn that
whatever roman just demonstrated in the
admin center can be done
programmatically
without any exceptions
and i'm gonna
give a little demo of that
so i have written just a small piece of
power to the code here and i'm gonna run
it
get the
access token that allows me to
authenticate to the admin center
so i just pick two
more let's random examples if that you
can do so the first one i'm going to
call is
just give me just a get operation to
give me all the environments
the environments of who which customer
well the access token
that i'm passing in for the
authorization header
tells business central who who i am so
it knows the customer so it's going to
give me my environments back
so let's call it
and now we have the result back you can
see we have a response
that contains some json if you're quick
in the content field let's let's let's
format that a little bit nicer
and let's print it out
so now we see it we see the list of
environments i should before because
that's what we saw in the ui and you can
see that they have all the information
that we we expect like the application
insights key that roman said before
the environment name the country code
the version the urls the data center
that it was present into
and
this version of the platform and you can
also see the database size
all these things
that you can see in the ui as well
so as another example more or less
random let's invoke the database export
operation using an api so in this case
it's a post operation
and i'm going to
invoke it on the export and i want the
production environment to be exported
into a backpack
well where should it put it well i
provide
the three values that roman also had to
provide in the ui
so it's quite similar let me run it
and now it has started the operation we
could go and check the history and see
that it actually
did execute on that
so these were just two examples
[Music]
i leave it to your imagination to decide
what you want to do with it maybe you
want to have periodic backups of
of your database of your environments or
you want to
make sure they all have the same have
insights keys or however you want to do
it right
so
the
apis are well documented so if you go to
your favorite search engine and search
for business central admin center api
this will be your first hit
and so i've
included a screenshot here where i show
the database export operation and you
will recognize that this exactly that
url that i invoked before and it is
exactly the three
json properties that i provided so
everything is straightforward to use
so you can do all a lot of things in the
admin center api and i demonstrated two
other things
there's also another scenario that i
think is very important and that is
automated deployment
as you
make changes to the extensions for your
customers you want to upload them to
your customers environments
and you can do this manually as i did in
the beginning
but it's a pain right it's slow you make
mistakes you need to do it for multiple
environments for that customer so it
would be nice if we can automate that
piece as well
so what
what the setup that
we recommend to you is to do this in
azure devops
you've probably seen some sessions on
that as well it's uh very popular and
for good reason it's really really nice
so what we recommend is that if you have
an extension you have your source code
in a git repo and azure devops
and you set up an automated
build pipeline that
builds your app
runs your unit tests
and now you end up with a dot app file
that is ready for deployment
now you want to deploy it
to the customer
you probably don't want to deploy it
directly to the production environment
as i did initially here because what if
the app has some
bugs or what if the
functionality is not exactly like the
customer
wants it to be
so for that reason we recommend you to
deploy to another environment probably a
sandbox environment so we have created
an environment called uac user
acceptance test
which we want to deploy to first and
then we invite the customer to go and
test out the functionality if the
customer is happy well then we're just
gonna invoke a similar deployment but
this time to the production environment
and at that point of course the customer
can can use the functionality
for real
so let me
show you how how that works
so i have my
as your devops where am i
over here
my asset devops
account
from chosen mig so i'm the partner in
this case and i have the code for the
customer in a repo you can see that i
have a
repo called contosomic and it has all my
source code
as you saw in vs code as well
and i have set up a build pipeline
that
takes that source code as i said builds
the apps run the unit test and produces
the resulting
app file and you can see that if you go
into one of these you can see that it
has produced
an artifact
if it works let me refresh
let's produce an artifact
there it is
and
inside of it it has my app file
right this is the one we would like to
to deploy now so i'm not going to
demonstrate the build process there are
different ways to do this
probably you want to do it with a dogger
container underneath and there are many
partners that can help you with doing
that
by this time
so we also i also have defined a release
pipeline that can take my artifact
including the data file and deploy it to
the customers environments
and let's
create a new release
so i want to select
this version 1.30
and deploy that to my customer
create
and now
it has created a new release
let me just zoom in a little bit
oops
let's look at that release
so the way i have designed this release
pipeline is the way that i explained
before first i want to deploy it to the
uat environment when that is completed
and the customer has
validated my changes
i want to deploy to my production i have
configured
an approval
step here which means that the pipeline
will stop at this point
waiting for somebody to approve the
deployment to the production environment
we can look at the
logs to see what it's doing
perhaps at some point
while we wait for that maybe we can go
to the admin center
and actually log into the uit
environment
there it is let me log into it
okay
let's see how far we are in the
deployment so it is currently in pro in
progress with the upload
and installation
so any time now we will should be able
to see it on the extensions page
somewhere
among all these apps
i don't think i want to wait for it but
it typically takes maybe 30 seconds it's
here any time now
yeah
let's not wait for that
so this is really useful if you have
multiple environments
for the same customer and if you have
many customers of course it will help
you greatly as well
um
so this shows how you if you have one
customer and you have one app for that
customer how we set it up as i showed
you put the source code for that app in
its own repo you create a release sorry
a build pipeline that can produce the
app file
and then you create a release pipeline
that takes that app file and deploys it
to the customers environments
the question however is what do we do
when we have multiple customers how do
we sort of scale this setup to multiple
customers
and
our recommendation is simply to
replicate the setup that we have for the
single customer so for every customer
for every app create a repo build
pipeline and release pipeline it's a
straightforward approach and i know some
partners are doing this already
and
this actually concludes
the presentation let me just do a quick
summary so we've shown initially how
you need to upgrade your code to bc15
and the data as well and extract
customizations from the
base app into pure extensions
then estimate demonstrated how you can
migrate your data to a cloud environment
including things like setting up users
and permissions and he also talked about
how you can test when you're in the
cloud to see that it is
migrated properly by copying to a
sandbox environment and roman went
through i won't enumerate all these but
went through all of the management
capabilities that we now have in the
admin center and finally i talked a
little bit about how we can handle scale
and with that it is time for questions
what questions do you have
yeah
you do
hi um esteban told that there's a
maximum amount of gigabytes for cloud
environments and he also mentioned that
below that maximum
80 gigs is the maximum recommended size
why is there a maximum in place
so
certain operations become very
impractical if it if your database is
too large there are situations where we
might need to restore from a
point-in-time backup for example if
something goes wrong during an upgrade
and if your database is too large it
could take many hours or
even days depending on the size to
restore which means customer downtime as
well which is why we just don't
recommend it because right now uh
operations the the time certain
operations take just increases too much
if you have large databases yeah and
what do we do with customers that are a
long time customer of nav with a large
database
and we want to move to the cloud
i think there are three three things
can you get rid of some of the data and
that's an option if it is then great you
can move to the cloud if you can't you
can um
wait because we extend you expect to
increase this limit going forward we're
still growing up in this sense and
number three if that is not an option
for you you stay on frame
you give it to the neighbor over there
hi
i actually have multiple questions the
first one was
if i already have aad in my on-premise
installation
do i still have to
assign all the
users again
they will probably have the same
username as you have in the cloud in
that case and so it means that the
mapping is kind of
not necessary because they have the
right names yes but but the users will
not migrate so you do still need to
assign permissions to to the right users
and things like that it doesn't matter
if you already have it set up on prem in
that regard okay
um the next question was
am i able uh to
add custom
application insights
telemetry initializers
so as an extension for example i want to
add my custom your custom telemetry from
your extension at this point no so as
roman mentioned we are going to add
platform level telemetry for reports for
web service calls and a number of other
places errors in particular it's also
interesting what we're also looking at
is allowing you from al code to write a
message that will end up again in the
same place in your app inside key that's
another important scenario that we are
looking at yeah that will be very
helpful for custom apis and absolutely
things like that
the last thing was
dependencies for multiple partners so
you mentioned if i as one partner have
multiple customers with multiple apps
but how do i handle it if i
have an app and another partner has
another app that depends on my app and i
want to upgrade my app how do i handle
this and i don't know about the app
that's a complicated scenario and we
it's not because we're not thinking
about it i just don't i'm not able to
describe the process easily at this
point
right here so but come and talk to us
afterwards what
if you have a hot fix to your app if
it's in the in the middle of a
dependency change you will be able to
hot swap it kind of but then there's
also the case where you change your api
perhaps perhaps in a way that
invalidates the extension on top and the
process for that is different
i can say you tell you that
our general approach here is that we
want it to be a full model from the
customer side so if you make changes to
apps in appsource
they should not go to customers
automatically in ideally they we want
customers to pull and when they pull we
will be able to see whether it will work
or not whether they can compile and they
may need to take multiple
simultaneous new versions of apps but
it's a it's an area that we still have
to explore further okay thank you you're
only going to get one t-shirt even
though we have multiple questions
i have two or three
um
can i script my sunbox creation
absolutely create a backpack but i
didn't know if you could also create a
sandbox from a script yes yeah yeah you
can definitely create the sandbox
environments from the script um can you
expose the create buy and date of those
sandbox environments where those are at
least the creative date i have a problem
managing my sandboxes at the moment i
have many
yeah and you want to know one you want a
property that says when they were
created yeah just
we'll take that into consideration and
regarding the
uh synchronization from my
on-prem 15 because i want to move to the
cloud you mentioned that in my app i can
specify some tags or whatever to say
don't sync this data
but are you going to give me an option
to say
i have a massive change like entries
table
i don't want to sync the changelog
entries table
are you going to give me an option to
say don't bother with that you know to
save safety space
this is base up
uh no no
but you know what sorry but but not all
the data is is migrated
and we can control it in a base app
level so
there are cases where if we find that
some data is just not useful at all in
the cloud we might disable it but again
because it can't be controlled we have
to think about everyone right so unless
it's something that is really just not
useful to anyone we probably won't
disable that and with the global
application data you know just going
back to cal you know global tables
when you're doing that sync up
and you start your company what's
happening with that global data
i i assume so actually i don't know
which of the tables that are not per
company that we are synchronizing oh
right but you can go and look if you try
it out you can see exactly which tables
got synced and which didn't so you would
have your answer right there thank you
yes you can check the warnings and then
you'll see the tables that didn't
have their my data migrated
yeah a couple of questions from me uh
i want to make a copy of the production
environment can i do any action before
that copy will be running
because my problem is for example i have
a notification entries so there are some
emails that should depart and at the
time that that copy goes
email are there and the customer will
receive its email one from production
one from the environment
is a real case so is there any action i
can do
[Music]
well you what one thing you can do if i
if i was doing it manually i would run a
script to
remove some data from c
i don't believe we give you a hook that
you can run something on the on the copy
operation i don't know if it helps but
what you can do is check in your code
whether you are in a sandbar or a box
environment or in a production
environment and then you can in general
turn that functionality off in your
sandbox i don't know if that solves your
problem though
another thing we do when we
when we copy to sandbox is if you're
using http client to make calls out i
don't know if that's the case here
probably isn't but if you make hp calls
out we'll block that
and you have to
turn it on again in your sandbox
environment mainly the problem is smtp
yeah i know it's not hp
okay second question is related to the
administration panel should we give
access to the customer
no it's typically the admin or the
delegated admin that would have access
um
yeah so
so the the ones that have access to the
admin center is
either the global administ global
administrators in the customer so the
customer actually has access already
and then the delegated admins which are
partners that have a trusted
relationship with the customer
um
one way to think about it the way that i
subscribe to is
the customer is in charge at the end of
the day as a customer they can even kick
you out
they can say i don't no longer want you
as a partner
right they can do that and so it is
actually they are in charge at the end
of the day
so you are invited into their
environment that's that's how i look at
it is there any protection and you
cannot delete the production environment
looking at that list is
one entry you click delete do you want
delete yes
so no but if someone were to do it
accidentally or otherwise uh maliciously
we can recover it for a certain amount
of time so unless you're
taking a break of a month not using your
environment and then coming back we can
still recover it you keep your data for
35 days it is not my date at that time
it's the customer data but the customer
stays up
we keep it for 35 days i would consider
that
one of them should be your default you
shouldn't be able to touch at all
no
it's an area we have heard feedback on
that you want to have fine more
fine-grained control of what you can do
in the admin center and who will have
access to it
thank you
any other questions over here
it's one of them
yeah one question regarding the
migrations
if a customer has already some data in
production in the business
central yeah some life system wants to
migrate some other companies from uh
on-prem is that a scenario that
works or are there any fallbacks or
something so basically merging to
production environments in a way
while it's different companies
well if the data is in different
companies um
then
technically uh it you should be able to
because uh
the data gets migrated per company
except for for some tables right that
are shared
um
i don't know if it's something we would
recommend
but
what it might be
then or if there is really a client who
has something on on the cloud something
on prem what would be a recommended way
of getting this all into one
package in the cloud so you always have
the choice between having two companies
in one environment or having two
environments in the first place and
definitely if you want the second
approach that is a possibility so you
don't want them to be in the same
environment and that if that's okay then
you can have it that way
okay yeah
what's your question over here
it's working okay
so i have a live live customer says for
about a year now
and we really had problems when one user
logged the database and everybody was
locked out of the database for 20
minutes half an hour
on sandbox environment for whole night
so what are the tools to disable the
station kill the session or how to
approach this problem because we really
had it in production
yeah it's a good question and
it is one of the scenarios we want to
enable as well because you might
accidentally run a report that runs for
hours and consumes a lot of resources
and today you don't have an ability to
kill it
and it's we of course have a full list
of all the sessions that are running
and we would like to just expose that to
an admin probably in the admin center so
that you can just kill it at any time
but
today i don't have a good answer
maybe follow up
so we already also had some issues when
the upgrade failed
that's fine it fails no problem
but the job queue didn't start again
i would
probably need to correct myself the job
queue was started but the earliest date
time was not updated because it was not
running so what to do in that that
scenario
well if the earlier state wasn't changed
won't it run again
well that's the problem because it if
the database wasn't
offline it would run it would update
the job queue but because the database
was offline it didn't double it and it
and it will never run the users needs to
go to the job queue
and check out the job queue entries that
are
in status ready
but the earliest days time is not
after current date time so it will never
run
yeah well if it didn't run if it if that
happened then it's a bug
why don't you come down afterwards and
explain
any more questions
there's one up in the back can you
so we had a customer in the cloud and
after one year he decided to cancel the
contract because he was not happy
and in austria we have the the
law to achieve tarta for seven years and
we have to access the starter every time
so what's the solution for this
i don't know
you know
the export
now
you could export it and store it because
we
after
if the
government wants a report we have to run
this report after seven years again
and the government can
choose every report of the system and we
cannot
uh just use the database so we really
need the system running
i don't know
yeah i mean you on prem you could keep
the database and you had the code and as
well and you would have to have that
system running for seven years it sounds
like in the cloud you know i don't know
i mean you have the databases as roman
said you can export the database in
principle you you can you can migrate it
back into a cloud environment at any
time and re-run the reports but
that's the best i can do
what's the question over here where's
the mic
let's have that question and one more
and then let's
finish
hello
you showed in the first
part that there are on in on-premise
database
appsource apps installed in it
how could you do that
you can't download from appsource and
install on-prem so if you have appsource
apps or you have isv solutions you'll
have to talk to the isv to get those
installed just like today actually okay
one last question
there's one all the way up in the back
but you have to come down i think
yeah otherwise there's one here last
question
i think he has the mic
okay
thank you very much for your
insight view
about backups
how can customers restore
his backup data for example
your backup
in microsoft cloud or the
downloaded backup it's there any
plant in the future
so the the backup goes into your storage
account yes
and
it's planned that we can restore
any data in the cloud
you're saying you want to go back from
the backup into a
cloud environment yeah so i i don't
think we have that planned i i don't we
have we don't have that plan and i don't
think it will come anytime soon okay you
don't have that blend okay if you want
to get data into the cloud what we show
today is the way to do it if you want to
take it and install it and get get an
environment up and running on prim it's
right it's straightforward you just take
that backpack and restore it into a sql
server and then you are running okay if
you if you if you do have the
extraordinary case though in the cloud
where something went really wrong
with the customer and they need they
would like to go back like two days and
they don't mind losing the data for
those two days
you can contact us and we do have the
ability to do that but i don't believe
that something we are planning on
exposing
to anyone okay thank you all right thank
you very much
[Applause]
