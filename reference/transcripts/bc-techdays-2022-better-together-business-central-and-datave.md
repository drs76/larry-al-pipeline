# BC TechDays 2022 - Better together Business Central and Dataverse

- **Source:** https://www.youtube.com/watch?v=DfjpwWvfjMs
- **Video ID:** DfjpwWvfjMs
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 63m54s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

ladies and Gentlemen please welcome
and Georgie chenich
[Music]
good morning and welcome to this session
about Microsoft's integration business
Central with the Power Platform
um
my name is Zona Georgia and this is my
colleague on it
and uh let me just quickly introduce you
to both of the sessions that you will
see today
we will show
how does business Central integrate with
Power Platform enables you to build
power apps and it runs on dataverse
which is a service that stores your data
and runs in the cloud in a secure way
business Central doesn't run on
dataverse but we integrate with it in
various ways
we have a data synchronization with it
ah we we have virtual tables that can
show business Central data and help you
manage it and we also have a Power
Platform connector that can that can
integrate with business Central and we
will show all these three in the next
two sessions
in this session on at and I will present
the data synchronization
and how you can extend it to suit your
needs
um we will show you how to keep your
data about customers vendors currencies
in sync with the data dataverse
environment
then we will show you how to
keep your sales related data in sync
with dataverse that's items resources
quotes orders invoices Etc
and we will of course show you how to
customize customize and extend it
so Power Platform and dataverse
on one side and business Central
platform and system application once on
the other side
on dataverse you can have sales app
which is for managing invoices products
and sales related entities and the way
you integrate with it with data
synchronization from business Central is
you you can have you have two setup
Pages
first you do dataverse connection setup
to to set up the connection with the
base entities such as customers vendors
and contacts
and on top of that
you do another setup to to make the
connection with the sales related
entities
and during this setup we we deployed two
solutions two powerapps solutions that
that are needed to make this integration
and
of course you can then have more
solutions on either side business
Central and Power Platform
so in the next demo I will show you the
dry run of setting up the connection and
running the initial full full sync
between business Central and dataverse
we'll show you how to use the assisted
Setup Wizard to set this up and the
wizard will also perform the initial
full sync and it will be a situation in
which you already have some data in
business Central and some data in
dataverse and you would like to couple
this existing data
we will show you also how to map option
sets which are data in business Central
but metadata in dataverse
so let's let's go on with it
so here we have a situation where in
business Central we have some customer
records
and these customer records have either a
home page
that matches with their counterpart in
dataverse
or the other the first two have a
telephone number
the fifth one doesn't have either a home
page or a telephone number and here in
dataverse I I have the same accounts and
they match either on telephone number or
on on a web page
um
then the to connect these two systems I
would go to assisted setup and choose
there's uh there's a link to setup
connection to databers
and I will now disable this option this
is for virtual entities my colleague
Lucas will show that in the next session
so I will leave only the data sync
I will accept terms of use and then I
will basically enter my the URL to my
dataverse environment in the in this
field
and then and then I will sign in
with the administrator uh you need to
sign in with the administrator of the
dataverse environment during the setup
because during this setup We Will We
Will Auto generate a user for service to
service connection we will import the
powerapps solution that is needed for
for this integration to work and and the
administrator account is is required for
this
so once you sign in now we are setting
up the user and
and then
now the administrator is signing in
and when you click next this is the step
of the setup that Imports the solution
this usually takes two to three minutes
but in this demonstration it's shortened
and then when you click next the system
will analyze which data you have in
business Central and which data you have
in in dataverse and it will
propose you the strategy for the full
sync for the initial full sync
and remember that in dataverse we have
some customer records but we don't have
any vendors we don't have any contacts
so for vendors contacts it's proposing
full synchronization but for customers
it could see that you have data on both
sides
so you it's suggesting you to select the
coupling criteria and this is a page
where you can set up how you couple your
existing data and I know that half of my
customers match on telephone number so I
will choose to match on this as first
priority and as a second priority I will
choose to match on website
I can I can choose some other options in
this page such as to synchronize right
after coupling the records I can choose
the resolution the conflict resolution
strategy what what if during this
initial sync a conflict happens meaning
that
record is changed on both sides and I
will choose to send the data from
business Central to databers and lastly
I will choose if you don't find any
match then just create a new record in
dataverse
so
it is the system is also proposing to
choose the coupling criteria for option
sets for payment terms
for shipment methods and shipping agents
uh so this before before this uh before
wave 122 this was a non-trivial sink
because it is metadata in dataverse but
now
you can just do it by
with no code we we offer it off the page
so once you set up this coupling
criteria you choose okay now the full
sync will start sorry we'll start
running after you click finish
in a system with very little data it
takes very little time
so now you can see that your your data
is is synchronized
and let's see what how it looks uh in
the in dataverse
so over in dataverse
you don't see any new accounts added
this is because it is no I'm signed in
with my my dataverse account but the new
accounts were added by the
auto-generated application user which is
a non-licensed user that is used for
service to service connection and now
you can see that this user added more
accounts that come from business Central
it added this customer that was not that
didn't have either a telephone number or
a web page
because the the coupling did not find
the match whereas for these customers
that were matched it just synchronized
the data from business Central
and of course it also if we look at the
vendors
if you look at the vendors
you had a situation where you had the
number of vendors in business Central
but no vendors in dataverse and those
were also
those were also added in in dataverse
as you can see here
so after you do the initial sync
then you can either continue coupling
records manually and we will show the UI
for that in one of the next next demos
or the synchronization engine will via
job queue entries will synchronize the
changes between business Central and
dataverse
so here in the integration table
mappings you have these are the mappings
that where you describe the rules how to
map the tables
and this on the customer mapping you can
see that there's this conflict
resolution strategy that we set on the
coupling criteria page
you can also set it for another type of
conflict which happens when when one of
the coupled records gets deleted in one
of the systems
you can set that strategy as well this
is from the integration table mapping
page you can you can see the
synchronization jobs and the investigate
what happened uh in the last scheduled
jobs
to troubleshoot the errors there are two
pages there is a integration
synchronization errors page which shows
generic errors that happen during the
synchronization right now it's empty
because we just did the full sync
and then there is the coupled data
synchronization
errors page and this is for records that
were successfully coupled but their
synchronization failed for some reason
like they were changed in both systems
or one of them got deleted
you can set a strategy on the mapping to
reduce the number of these errors
and let me also show you the the result
of the option mapping is that you now
have a lot of values came from dataverse
for the shipment methods and shipping
agents and payment terms
so that is that was the dry run of
setting up the connection and and
running the full sync and uh to
synchronize sales related data you have
to have the sales app on the dataverse
side
and I will I will just show you it's
quite simple once you have synchronized
the base entities
we also have a wizard for the sales sync
where the connection and the sign-in is
not done because you have already done
that in the base connection setup
um and I will also show you how to get
an overview of the integration table
mapping for the new feature that we have
and that is the bidirectional sales
order sync which is was very much uh
requested from the partners
um
so to set up sales connection uh you
just go to assisted setup and choose
another we have set up a connection with
Dynamics 365 sales and you just
click next and here you could just click
finish it would import the the solution
that is required but you can also turn
on other features in advanced and one of
them is the bidirectional sync of sales
orders
and another one for example is you can
turn on the item availability
so if you turn item availability on you
will you will from dataverse when you
make orders in Dynamic statistic file
sales you will see the item availability
in business Central
so if you choose these two options and
choose finish now it's importing the the
integration solution
for integration with sales and it's done
and
this normally also takes three to four
minutes but it was shortened
so let's take a look at the integration
table mappings now specifically the
mapping for the orders
before this release we used to only
synchronize the header and it was only
synchronizing one way from business
Central to dataverse but now the
synchronization is bidirectional and if
you look at the fields of this sales
order mapping we synchronize more fields
from the header
and of course we also synchronize lines
so if you add lines or modified lines to
a coupled order in business Central it
will be synchronized with
Dynamics 365 sales
and one one thing to mention is that
that this only works for released orders
so if you look at the if you look at the
table filter
for the orders it only works for
released
so that is that is the demo for the
synchronization with sales
and now I want to show you one more
thing and that is that was a requested
feature
so when the when this synchronization
jobs run
if you have a change in business Central
on a coupled record
the synchronization engine will wake up
the job queue entry and and do the sync
in near real time
but we didn't have this mechanism from
the other side if if a change happens in
dataverse we did not have a mechanism to
wake up the job queue entry but now we
have in wave 222
we provide this ability and to make it
work you need to make a cloud flow in
the dataverse environment in power
automate
so you sign into power automate.com in
your dataverse environment and you
create certain flows and we have also
published flow templates you can find
them under templates and then in the
template search string you just type in
notify business Central and you will see
these three templates
one is for account changes that's both
for customers and vendors because in
dataverse there's no dedicated entity
for customer
there is account and it has a subtype
customer vendor and other types
and then there's a template for contacts
and for currencies
the once you import this flow what there
is one thing you need to do and that is
to to choose your business Central
environment and your company
a business Central company in which you
have set up the the synchronization
if your business Central is in another
Azure ad tenant then you need to also
add a connection you will see that in
the video
so this is a this is a demo of of
of this flow let's first thing let's do
this on the vendor mapping and the I
will do one thing on the vendor mapping
and that is uncheck this this value
called synchronize only coupled records
this will make the the scheduled sync
also bring in new vendors that are
created in dataverse but by default is
it's checked to true
so you would
go in the same environment where you
have your dataverse data
you would navigate to either
flowmicrosoft.com or power automate.com
you would import this template
so I already have this template here
under Cloud flows
let's take a brief look uh at it it
starts with the dataverse trigger when a
row is added modified or deleted and the
only thing you need to do is in the
bottom of the flow you have to choose
your business Central company in the
business center connector and here you
can see I added another connection
because my business Central tenant is
not in the same tenant as dataverse if
it was in the same tenant I wouldn't
have to add a new connection
and you leave the same the other values
as they are and save the flow and after
you save this flow
and add a vendor let's try to add a
vendor
the trigger the dataverse trigger will
fire when you save a new vendor and it
will call business Central with the
business center connector and notified
that a new vendor was added
and if you look at the job queue entries
over in business Central
here are the job queue entries that run
the scheduled syncs and you can see that
the vendor job queue entry is in this
dormant State on hold with inactivity
timeout
it is waiting for a change
but if we refresh the list
you will see that it has been restarted
because a new vendor was added in
dataverse and as a result
you will see that the vendor
the vendor is now created in business
Central in in near real time so there is
no need to make these job countries run
unconditionally
every five minutes because now you have
a mechanism to get notified for about
both business Central changes and
dataverse changes
so to conclude this demo this is a page
if you if you download this
this presentation you you have
a number of useful links for setting up
and running the synchronization and two
links for troubleshooting
these are very very useful links and I
encourage you to to read through
and now I'm handing over to my colleague
on it
for customization how can you customize
all this yeah all right
so now that you've seen how you can sync
base entities and sales entities on top
of that you might have a question but I
have another solution in my dataverse
environment how do I synchronize that by
extending the existing connection that
is what I'm going to show you today
first we'll start by creating an
integration table object in business
Central using Al table proxy generator
tool also known as outpigen this table
will be a normal BC table with am
a slight difference it will have a type
called CDs and it will have some
properties that will allow you to map
that table into a database table so that
when there is a any modification
insertion or even a get operation in il
it will convert it to an SDK call and
then make a call to dataverse and get
the data or modify the data
then we'll actually create a list page
for that table in BC so that you can
actually see all the dataverse records
you have and then we're going to extend
a business Central page with a lot of
actions for coupling and synchronizing
and then of course we're going to have
to subscribe to some events in a code
unit where we allow you to actually
insert your custom integration mappings
and field mappings
so let's just begin
if you look at the Dynamics 365 human
resources
solution you'll see down there a table
called worker which is actually quite
similar to employee table in business
Central if you look at all the fields in
in database so let's try to sync workers
with employees in business Central as I
said first we need to create the table
in business Central how do we do that
you know vs code extension uh under the
um the extensions folder and of course
the AL extension there's this hidden
tool under the bin folder called alt
pigeon XA and how do you run this you
run this through Powershell you just
need to give us some arguments I wanted
to have a arguments file right here
args.rsp so you have to give a project
that is the AL project you're working on
the package cache pad is the AL packages
so that it actually looks at the symbols
while running service URI is your
organization URI entities and those are
the entities that you want to create a
table for Maze ID the object number of
course
uh when you run this tool it will
actually authenticate to dataverse get
metadata for that entity that you want
to create and it will also look at the
symbols so if you already have a table
in business Central for that it will
create a page table extension with extra
Fields if not it will create a
completely new table for it so let's
just do the two-factor Authentication
yeah all good now we will actually
connect retrieve entity metadata and
then create a worker table as an Al
table
in business Central because I don't have
it in my symbols
let's just uh quickly rename this so
that it all get rid of their compilation
errors
and then then I'll just move it to the
uh the tables folder right there
but um if you actually look at this
table you'll see that table type is CDs
and there's this imported property
called external name this actually
matches the the metadata in dataverse
and that also is the same for all the
fields if we take a look at like one of
the fields let's say uh status code
you'll see that external name and
external type are actually coming
directly from dataverse so if you write
to this table if you have the connection
enabled it will automatically convert
this to an SDK call and write it in
dataverse
now let's uh let's create a um a list
page for this one yep The Source table
is the table that I've just created and
I've added some fields that I actually
want to see
I also have this uh important action
called create from dataverse all you
have to do is under CRM integration
management called create new records
from CRM and give the record they will
actually create the database record in
BC as an employee
it will schedule a job this has
currently coupled database worker this
will just set a
a variable I'll get to that one later
this is in order for you to use this
page for coupling
so now let's look at a table extension I
have for the employee so that I Mark if
a record is coupled to CRM or not it's
important that you use this exact name
couple to Sierra because the sync engine
will actually look through this field
and say oh if this record is coupled it
will mark it as coupled and I also
extended the employee list with this
couple to CRM field so that you can
filter on it if a record is coupled or
not
and then under the employee card
extension I've got as I said a bunch of
actions for synchronizing first off the
database go to worker you have to call
show CRM entity from record ID in the
same code unit this will actually allow
you to deep link so when you click on
the section it will open the coupled
record in dataverse
the next one is synchronized now this is
what it says it will schedule a job to
synchronize that specific record
and then you have to call update one now
in CRM integration management
synchronization log will open the the
synchronization log for that record as
Georgia showed earlier
and coupling two actions setup coupling
that will open a coupling page it will
allow you to either create a new one or
a couple to an existing record in
dataverse and delete coupling will of
course remove the coupling so that they
are not coupled anymore
now the important part is the code unit
this code unit I've got a bunch of
subscribers to allow you to do some
stuff the first one is in order to use
this uh table uh worker table in the
coupling page you have to subscribe to
on get CDs table number and you'll check
or if it's employee then this is the
table I'm mapping to so this will
actually allow you to use this table as
coupling
and the next one is uh in order to use
the list page in the coupling page so
onlookup CRM tables you'll see if the
CRM table is this and then I'm going to
call the procedure this will set the
existing record if it's coupled so I'm
going to use the the one that I've
talked earlier to set currently coupled
database worker so it will actually show
that this is coupled to this but you can
of course change it from that page and
when you look up that uh dataverse list
it will open the list page that I've
just created
the next one is on ADD entity table
mapping this will allow you to do deep
linking so when you come from the
database go to action it will open a
dataverse and the most important one is
on after reset configuration in CDs
setup defaults this is where we add our
integration table mapping and field
mapping so I'm adding a table mapping
between employee and CDM worker and I'm
also setting a filter on the dataverse
worker because I only want to sync
employee type workers and I'm getting
that filter from the record and I'm
setting it on the integration table
itself integration table mapping itself
so that it only since employees
and then of course these are the um the
fields that I'm I'm mapping I want to
sync
and the last one uh is easy procedure it
will actually create a um a recurring
job that as Georgia said that will run
periodically and then synchronize
coupled records
so all good
um let's publish this
and then after this publisher I'm going
to show you how you can actually use
those actions and pages
is published so I already have a
database connection enable enabled all I
have to do is use this action called use
default synchronization setup this will
trigger all the events that you
subscribe to an install table mappings
and field mappings
so if you look at the integration table
mappings page you'll see the the one
that I've just created between employee
and worker and if you look at the fields
these are the fields I've added that I
wanted to sync
so all good now actually let's go to the
the employee list and try to create one
employee in dataverse let's pick the
first one as the Henderson
and this is where I'm going to use those
action that I created in the employee
card coupling this will open the
coupling page as I said
so you can actually select here on the
database side which if there's an
existing one you want a couple to but
I'll just create a new one the
synchronization has been scheduled
so if I just switch this to list view
I'll see that coupled to see a database
and I hit refresh yes open this
and now I'm going to use the Deep
linking so I click on worker and it will
magically open the dataverse that worker
that is coupled to the employee I was on
so all the fields are synced and it's
coupled all good let's create a new
worker in database and try to actually
create that one in business Central
so I'll just use my name
and yeah I'm a software engineer
yeah let's save this one
and go back to PC and open the um the
list page that I've created
uh
for dataverse workers
nope welcome yep
yeah you see I'm actually seeing all the
workers and dataverse and if I use the
action create in business Central it
will schedule a job and if I go back to
the employee list and just hit refresh
I'm pretty sure it will be created
yep and it's gonna couple the dataverse
so all good now we actually successfully
extended the paint synchronization with
our employee vocal mapping and
synchronize records bi-directionally
but this is only the a small part of it
without writing any additional code just
with that extension itself you can
utilize all capabilities of the sync
engine like the match-based coupling
Auto resolving delete or update
conflicts as Georgia showed and now of
course many more
if this was a bit too fast or a bit too
much code for you were we not we
actually documented this quite in detail
in this documentation page right there
I've also linked it in the slide
and one more additional thing we
actually imported this uh
pte into BC Tech so you can actually get
the sample codes right away
um I wanna before I actually hand it
over to Lucas I want to show you one's a
small sneak peek
we've been working on a prototype vs
code extension called BC to dataverse
this will actually automate everything
that I've just done it will create the
uh the sample code for you so all you
have to do is publish this will more
information on this will come soon we're
still working on the Prototype but it
will be a vs code extension like this
and then you'll have some a couple of
commands you can generate the list list
page as you have just did or generate a
proxy table which will run the outpgn
tool automatically and you can actually
map to existing BC tables like so so all
you have to do is I want to sync this
table which way and the which field in
dataverse or you can use of course
the constant value more information will
on that will come soon
and my last slide will be the the
customization links the the first two
will be the documentation and the second
two will be the two samples that we have
on BC Tech
so thank you
um I'll actually hand it over to lukesh
now he's going to talk about virtual
entities
thank you thank you Annette and Georgia
so my name is Lucas sagovic and I'm
gonna present today to Virtual tables
for integration with Power Platform
so the agenda for this presentation is
that I will do a small introduction what
the virtual tables are and how we can
utilize that we show you the new setup
experience in business Central and then
we'll show you a lot of demos
and you'll realize how quickly it is
actually to build powerapps and Power
Platform once you have the virtual
tables
the last demo I will also show some
product developments if you would like
to create your custom plugin in
dataverse this is also possible with
virtual tables
so let's get to the introduction so what
what is the spiritual tables and how
does it relate to the data sync that you
already seen from my colleagues so the
virtual table is a is a virtual data
provider in dataverse which means that
you don't need to replicate the data to
dataverse you know to build the apps and
and and power automated flows what what
it is is that you can generate sort of
this virtual table concept which is a
proxy
and then anytime you're doing a crowd
operations what we do is that we proxy
this call to business Central
and we do support the generator
generation of those virtual tables as
well the crowd query to read and update
and the card events so the events coming
from business Central to to power
platforms and this is a create update
and delete
so just under the hood how does it work
under the hood it's using our all data
endpoint and you can see here
you need to generate those virtual
tables first is like one time generation
and then for any operation we're going
to contact the special plugin that it's
part of our solution which is published
on the appsource and that plugin is
gonna contact the PCO data endpoint
using the API pages so that's are the
pages that you're actually going to map
on your virtual tables
now for the cad events we will use the
existing webhook implementation to push
the events back to the plugin and then
the plugin will push it back to
dataverse so once you have your virtual
tables then you have all the great
tooling which is provided by Power
Platform it's power up power automate
you can use the dataverse all data you
can use the plugin and you can use all
the ecosystem which comes with the Power
Platform
just one thing to notice we you can use
the building API Pages or to custom API
pages
we have also made the setup experience a
little bit easier
and George already showed this a new
checkbox when you run the database
connection setup with the virtual tables
and I'm going to show it in my demo
some of the basic stuff how do we
generate this virtual table there's some
special convention schema name
in dataverse you always have the prefix
for for your entities custom entities
and we use the din 365 PC for every
virtual table we generate and then we
append the the API page entity name the
published the group and version so that
it's going to be a unique schema name
then there's some requirements that
coming from the diverse one of the
requirements is that your key needs to
be a good there's a hard requirements
for that over so for that we have
already converted our API Pages V2 to
use the system ID everywhere
and then in dataverse you also have the
concept of a primary attribute so this
is the attribute that you see in various
places like lookups and so we choose
like the display name if it's provided
on the API Pages or any other
string first first attribute string then
we also support like labels or
translations and the translations are
available on your on your captions of
the tables on the field and the enums so
you can also utilize that in your apps
great let's jump let's then jump to the
demo and see how how easy is to create
some sample power up
so before I start anything I need to set
up to my business Central with uh with
the dataverse and as you could see from
from Georgia we have this new
new Switch here which is enable
dataverse and then I can just press this
one
and and
go ahead and set up my connection here
so what this does is that it
automatically discovered the the the
dataverse environment connected with my
tenants I actually didn't have to even
type it in and then press next and then
you realized that my dataverse
environment doesn't have that app
installed for virtual tables so it
doesn't do that automatically yet but it
points me that I should just grab that
up from the Power Platform App Store and
there is a link also in that wizard
which you can just click
uh and that will bring you to the to the
App Store
so this is our app in the app store it's
currently in the preview and then once
you install that uh the wizard will will
automatically show that it's it's
installed and available so
that's great the wizard finishes and
then what I can do is I can jump
directly to my to my Power Platform so
let's stop for a second here so part the
setup from the business Central is done
I can go back to my Power Platform now
and generate those virtual tables I want
to use
so I'm doing that by by going to a
special entity this entity is called
available business Central tables
so I'm just gonna search for this here
this is the entity
and and here you can see all entities
that are available in your business
Central environments
but they are they you also have the IPR
route so you know whether this is like
you know the standard V2 extension or
maybe this is your own extension and
then you you generate the virtual table
by flipping that visible flag
and by flipping the visible flag we told
the dataverse to generate the table and
then you can create your apps on top of
it so this is what I'm going to do now
I'm going to create three virtual tables
here I'm gonna do it for the customer
I'm gonna do it for the sales order and
I'm gonna do it for the sales of the
lines so I will flip the
visible flag
for for all three of them and then I
will wait for them to generate normally
oops
sorry for that normally that takes
that takes around around 30 seconds or
so but for this demo I have already
make it a little bit quicker so that's
it
I'm done with this the generation part
then all I need to do is
is to create some power-ups
so I will do that by going to the
powerapps and I will choose the the
model driven power up and this is this
is one important thing to note is that
in order to create a model driven power
up you actually need to have either the
native table or the virtual table so no
it's not that obvious to to use the the
connector for example for this
so I will now type in the name of the
app I want to create a sales order app
and you're going to just going to create
an empty app I will add a page
to this app which is the related to my
sales order entity
and just press add
and basically I I have an app
ready with the data coming directly from
the business Central without doing
anything
so I mean that's great but maybe I would
like to customize it slightly add more
columns change the forms at maybe lines
to the sales orders so let's let's do
that as well I will start by
by adding the
uh by adding the the column
so I can choose the default view and
then edit that view
and here I have available all the
columns that were you know a part
generation from the from from business
Central so I'll choose a customer name
for example and then save that and
publish
so that's done
now I can go back to my app and also
customize the form because by default
you only see this the the the standard
attribute the number so it would be
great to have a little bit more so I can
edit the the main form and just drag and
drop the attributes I'm interested in so
in this case I'm going to choose some
phone number and the status of my sales
order
and
the date as well so it's just as easy as
drag and drop
the phone number
and I also drag dropped the customer
ID lookup
and I'm also going to choose the status
great now
it'll be even better if I could show the
lines for this sales order but only the
lights that actually relate to the sales
order so I can do that as well because
this is something I'm going to show you
in a moment we also set up the
relationship between those those two
entities so the sales order has a
relation to the customer because there
is a lookup and also the sales order has
a relation to lines uh
because that's that's that's how they're
actually defined in Al
so what I can do now is to add the
component
and to add the subgrid and then choose
to only show the data which is related
to this record
so I'm going to just add the subgrid and
then show related records here and it's
going to show me all
uh or or the ones that we have
relationship for and I can choose the
lines
so this is the subgrid of the lines I
can just change the label so I know
these are the lines and and and I'm done
and I just need to save and publish this
up
I can just publish it here and play
and this is how it looks
so basically I have the list you can see
I have my extra column in my view and
then I can open any of the customers
an analysis order sorry
and then you can see I have all the
fields that I added I also got the lines
for the sales order
I also see the customer
and this is a lookup
so I can expand this and then you will
see all the all the customers here which
I can change and obviously this is the
crowd operation so I can change any data
here and it'll be automatically
reflected in business Central because
the the source is the business Central
no data is replicated
in this setup
yep so that's it my
my app is ready but I would like to go
back to this relationship to for you to
understand why actually I could do all
of those things so I can go to my
generated table
uh to the to the sales order
so I'm going to do here
and go back to relationships
and here is why I was able to choose the
lookup and choose the subgrid it's
because we automatically generate the
relations many to one for the customer
this is the lookup and one to many from
sales order to search order line
so this is
this is why it was it was so easy to
create this app
okay that concludes my first demo and
this is sort of the the summary of these
different relations and how does it map
from AAL to dataverse is basically if if
you want the map says order to lines
this is achieved by just putting a part
on your page and it will automatically
create the the relationship when you
when you create sales order and lines
for lookup that is basically just
defining a field to which in on the
table has a table relation for example
the customer
and the rest relation is a one
one-to-one relation this is this is
similar like one too many you also add a
part but you have a possibility to add
this new attribute called Multiplicity
and you can set it to zero or one and an
example of this would be a relationship
from a customer to customer detail and
you could visualize it in your power up
for example using a quick view
yep so that concludes my the first demo
and in the second one we will do
something a little bit more advanced so
you might have already some native
entities in your dataverse environment
with some data coming from business
Central for example accounts
and you might have sync the data using
either the sync solution which was
described or some power automate flows
but you would like to use Virtual tables
as well in your solution because maybe
you don't want to synchronize the other
tables from business Central for example
in this demo I'm going to show you how
you could add a relationship from the
Native entity of native table account to
the to the virtual table in this case
it's going to be sales credit memos
normally if you just go to the maker
experience in dataverse that is not
possible to do but we have added some
special entity which allows you to set
up the mapping between the native and
the virtual
so this is what I'm going to show in
this demo
so I will start by going to to power up
to dataverse and to my account table
and you can notice I have already
populated some data as I notice it can
be a sync solution or or some flow
uh and on top of it I have also added
the the account number
so we will we need to have some sort of
a primary key that we're gonna searching
or filtering this sales created memo on
so I'm using the account number
in this case you can see it here it's
been also populated and I'll be using
this account number to filter filter the
sales credit memo part onto the native
entity
and in order to set up the mapping I
also need to create the key
uh for the account entity for this
account number so this is what I'm gonna
do now
I'm gonna go to keys
and I'm gonna select create a new key
and I'm going to select the account
number
and give it a some name
so I'm gonna give it a name or account
number great
so I have the account number I have a
key for this
now I also need to find the attribute on
this sales credit memo that I want to
filter on so I'm going to go to sales
create memo and see all the columns
foreign
and this is the attribute I'm interested
again that I'm going to be filtering so
I'm gonna be using account number and
then filter the customer number on the
sales credit memo and in that way I can
get the filtering to work
okay so I have all my data
ready
and then I will use a special table that
ships with our solution and that table
is called business Central table
relation
and here I can just create a new
relation and I will use the form to do
that so we'll add new using a form and
here I just need to fill in a couple of
details I need to feel what's going to
be the name of the relation what's the
native table what's the virtual table
that key that I just created for the
account number and then the mapping
account number to the customer number so
this is what I'm gonna do now
so the name account to sales
credit memo the native entity an account
the table key it was the default prefix
account number official table this is
the name
and then mapping
from the account number to the customer
number and I need to use the schema
names
as well so it's going to be within 365
BC prefix here
okay
then save it
and basically now we have a relation we
can just repeat the steps from the first
demo to create the app
so I'm gonna do this now I'm gonna go to
oh I'll just also before that I'm gonna
validate that I actually have the
relation
so I'm gonna search for the memo
and you can see it here this is the
relation that we just created from an
account to the sales memo so from the
native to the virtual
now we are ready to create some maps
so this time I will create an app for
the account
so this is also going to be a model
driven app since this is the the fastest
to create so it's going to be at the
count test app
and I will add a list to the account
yep that's done and similarly to the
previous demo demo I'm gonna edit the
form to include now the subgrid to the
virtual table so I will use the main
Fort for this
edit the main form
and and then add the component
which is the subgrid component
similarly like like I already did before
yep and also choose the related records
now this entity has a lot of
relationships so I need to find myself
script memo
here it is
and then press done
and then save and publish that
customization
well I can also adjust the name of the
label
BC says create memos
let's save and publish
great
so I can just refresh here my app go to
the form
and this is this is what I see so just
to repeat I have my native entity but
I'm able now to actually show a subgrid
with a virtual
entities coming directly from business
Central in this case the credit memos
related to this customer
so am I thinking okay so what happens if
I actually click that one
where is it going to bring me to Virtual
native well now I'm actually in the on
the virtual table so it's going to open
the virtual table form
and I can also add all the customization
I done before so I can add more
um I can add more Fields I can add you
know the lines for this sales created
memos so I'll do all that
functionality and features I have
already presented my for my first demo
so that concludes the demo number two
and the last
demo I'm gonna talk about are the events
so we have a added support for our
webhook events also with the relation of
visual tables so now you can listen to
the record added deleted and modified on
the virtual tables
and because there are
virtual tables you can just use the
standard database connector to listen to
this
uh then the the second part of my demo
is gonna be more advanced this is
something you you can build on using the
c-sharp C sharp plugin and listen to the
to the to the same events uh using the
plugin and this is possible because we
actually have that this this special
event defined in dataverse and then we
can use a different tooling to utilize
that
so let's jump to the next demo
so in this demo I will start with a
simple automated cloudflow and I have
already generated some entities virtual
tables and I will go to my dataverse
connector
when row is added or modified and now I
can just choose the type and choose my
table name and I'm going to choose a
virtual table which is a customer and
then the organization scope so so what
it will do is now I will get notified
when
well when when a customer has been added
but similarly like we have a web hook we
only get the the ID for this event so in
order to get the full entity we need to
have this extra step grade row by ID so
I'm going to add this extra step here
and choose the same table which is the
customers and choose the ID from the
previous step so that allows me to get
the full customer that was created on
the business Central
and now for the for the demo I will just
send some email to myself of the data
and show you that I actually get the
right customer so I'm an admin here so
I'm going to send it to myself and I
will put the subject name that the
customer has been added
and I will put in the body I will put a
display name and the customer number
so that's it I can save the flow and
this is also interesting part so now
because I'm saving that and and because
the event is related to Virtual table it
knows it's a business Central related
table it will create a subscription on
the business Central site for this
customer entity
so now I can go back to the
to my uh to business Central create a
customer
and then you can go back to the
to the flow once this is done and see
the Run history that the actual
customer was captured by my flow
it's normally gonna take around one
minute
but I have
speeded up for the sake of the demo so
here you go you can see that this
customer with this ID was created
great so now the last part of the of the
last demo is to do some Visual Studio
development
so for this I have to install some
special extension it's called The Power
Platform extension and that allows me I
need to zoom in a little bit here that
allows me to create a number of projects
or Solutions so for this demo I will use
the special Power Platform solution
template
and I will create this one and then it
will it will ask me to sign into my
dataverse environment
and I have already provided my
credentials so just gonna fetch every
metadata from from dataverse I'm going
to choose the default solution here
and I'm gonna choose
the plugin project
I'm gonna give it some name here in this
case BC Tech days plugin project
so that's it this is done
I have my my plugin project here but
it's completely empty right now but I
can also use the
a special window called dataverse
Explorer
which is showing me also all events
available
to me and now it's worth to notice that
I have this even catalog and under the
even catalog because I generated the
virtual tables now I have this special
catalog only for business Central
so once I expand this one
you can you will be able to see my my
tables
and you'll be also see be able to see
the events that are available for those
tables so the card events so for this
demo I will subscribe to the created
event
and I will write a very small plugin
so there's a lot of nice tooling so once
once you create that subscription it
will out to generate some code for you
and generate this step which is needed
when you when you subscribe to event in
dataverse and then it will
it will create this this template here
and a lot of to-do's that you can fill
it in so with this I will first try to
get the ID of that memo that that was
created
and this is what I'm going to do just
get it from the input parameter The
Entity reference
then the next part is similar like in my
flow I would like to get the full entity
for the create memo and I will retrieve
it using the default organization
service just retrieve by ID
and here we have it here I'm just
retrieving the same script memo
I'm just gonna fix the the using
statement here so now I have my great
memo and from discrete memo I would like
to get the the customer number
like so just getting the attribute now I
have all my data
available
and then I will try to query the account
with this customer number so I will have
a small retrieve account code
which basically takes the the customer
number and then query the the accounts
for this account number
great so once I fix some imports here
I will create the task just to notify an
account that the the credit memo has
been created so the last element is to
creating a task
and here we go
task here
let us create it
yes
just just sending some description with
the number and the regarding object
account
so that's it I'm done with this now I
just need to build that project and
deploy but before database actually
requires me to sign that project so I'm
just quickly going to create the signing
key
sign this assembly with a new key
and just type some the name of the key
and the password
great
and then I'm ready to deploy this
project so what it will do now it will
the build and deploy and create that
subscription on the business Central
site as well
and I can validate the subscription has
been created by by refreshing the Power
Platform Explorer and this is what I'm
just gonna do now
I'm just going to refresh this one and
go back to my registrations and you can
see it here now I have a subscription on
the created event of this create memo
so all good
I can now go back to the business
Central create some sales credit memos
and see if my plugin is actually working
so I will create a new one
and then add some quantity
save it
go back to my power up
and then it's also going to take around
a minute but I have speed it up for this
demo so I can just refresh this here
and you can see this is the task that I
just created this is the the size
science memo that was created on
business Central site and you can also
see that in that subgrid that we created
in the second demo
so that concludes my last demo
and
just what's coming next so we're still
in preview we have a visual table
Solutions but we want to do a lot of
investments in the upcoming
release we want to add more events we're
looking at this external business events
we're looking at expanding the set of
entities that we ship out of the box
we're looking at the different features
we can do more with Power Platform and
we want to GI that extension that
solution for dataverse
so that's all for me I will pass it on
now to Enrico and Erton for the native
connector thank you
[Applause]
