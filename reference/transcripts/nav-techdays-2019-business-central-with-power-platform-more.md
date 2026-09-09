# NAV TechDays 2019 - Business Central with Power Platform - more than ERP solution

- **Source:** https://www.youtube.com/watch?v=F28lpqdeXbY
- **Video ID:** F28lpqdeXbY
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 104m08s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

okay
welcome to this session
um as you just heard this is busy
central the power platform more than
just erp if i
it's a right name uh generally we speak
a little bit more about power platform
less about busy central uh topic is more
how to improve your erp very often
uh we try to
make a lot of customization sometimes
with no right reason and the idea is how
to move a little bit more outside of erp
my name is alexander tortowicz
currently working for microsoft partner
technology strategist is for bizepps
as you can see i'm first place husband
the father and dog owner this is the
most important thing in my life but
after that i'm working with microsoft
right now previously as a partner as a
freelancer some 15 plus
years
in dynamics
uh
yes and i was an mvp before i joined to
microsoft and so and so
uh i've been worried my colleague
renato fairdiga
right pronunciation fighting is right
good morning everyone welcome to our
session
as alexander said my name is renato
feidega i am coming from croatia zagreb
and i work in a doctor
for five years
where i started to work as a developer
and now
i switched to application consultant
with uh of emphasis to for example
integration scenarios how the
consultants can do
the job of the developers for example
some light customizations and so on
i'm also a trainer
for patan and from the last year i'm the
mvp for business applications with the
emphasis on
business central and navision in that
time
so what is the idea and the goal be
behind this uh
session
and why we at all uh submit this session
is we show that you don't need to move
uh to do every every task in the erp
sometimes you can do for example
reporting in power bi or any other
for example bi tool
and that was the reason that for example
we can integrate really power platform
and business central so everything that
is not the core erp
maybe we can do this in other solutions
and integrations between business
central and for example power platform
today we will speak about power platform
and their uh applications inside the
power platform
also
what was the idea and the goal is to
move all the customizations
from the erp
we know that we had this heavily
customizations in av that you can modify
any object in nav
right now when the business centers us
we have the less possibilities less
less possibilities to do that so why to
not uh use the
knowledge of our uh
person our
colleagues in the company
and uh develop some for example power
app applications which will go uh
hand to hand with the business central
also there is an integration between
business central with other solutions
for example the crm why to provide to
put all the
information and store all the
information in the business center when
you can have these informations for
example integrated with crm or for
example thailand where you can integrate
employee data
for example about onboarding and so on
with the employee from the business
central and in that case
for example have the only business
center to do erp side and for example
dynamics 365 for talent to do their side
of job
and of course the last but not the least
is to create a new experience for the
users we all know that
business central is also available on
the
mobile phone on the tablet with this
modern client
but
uh why we
need to use this uh
business center mobile client we can
when we can develop
the solution which will be
tailored to the client's needs
that was the idea and the goal uh behind
this
uh session
so
based on that idea we create the agenda
for today so we will
talk about integrated business central
what are possibilities how you can inter
integrate business center with power
platform
what are the possibilities of the power
platform of course we have flow power
apps power virtual agent common data
service common data model where power bi
where you can easily integrate the
business central with other
applications from the power platform
so we will see that business center can
be
used as a data source and all other
processes you can do in
in your uh
power app or for example power bi
we will see how to integrate business
central power platform and how at the
end how to embed
power app into the business center
and
the last but not the least will be how
to integrate business center in other
dynamics 365 products
so how you can integrate these two uh
for example these two solutions
now let's let's start with the with the
with the core so what is the integrated
business central we all know that
business central has all these
possibilities to store and maintain and
master data for customers
vendors items and so on
has some functionalities about project
management supply chains sales marketing
operations
business has also
some awesome reporting possibilities
and this is our business central
but when we want to uh have the data in
other systems
and we have the data in other systems
for the crm dynamics
of customer engagement dynamics 365 for
sales
for example talent
marketing and so on project automation
service services
then we need to
integrate these two systems to have the
complete overview of on our project for
example
and this can easily be done by for
example flow where you can automate uh
possibly automate
jobs and tasks between these two systems
also
here you can for example analyze that
data and combine data from the power bi
from the business central of customer
engagement
uh f and or some other excel sharepoint
lists into one data source and then
combine and
do the reports and dashboards in power
bi
also
in the
power platform you can easily create
applications which are based on multiple
data sources such as business central
uh
talent sales and so on
so this is the one whole picture where
you can integrate all the informations
and all the data from the various
systems
so what are the what are the
possibilities of power platform and what
we will talk today
so today we all know that
someone
doesn't know that flow is power automate
so we change the name from the flow to
the power automate and what we can do
with the microsoft flow also power
automate is to automate process across
applications and other services
which are available to the connectors
we see we have more uh more than 200
connectors which are available for the
flow to use them with the for example
business central
or if there's this is not uh enough for
you you can always build your own custom
connector
where you can connect this to
a business center with other
applications
and what is really nice
what we have in the
business center that you can embed
microsoft power automate
into your business central so you can do
the flows you can create the flows
automatically from your business center
environment
another application
which is which are really great is power
bi
so where you can create dashboards
reports and consume business
insights
from various sources
so for example on my
customer cards i have information about
about balance
but on the crm side i have information
about marketing campaigns quotes and so
on
this data i can combine in power bi do
some transformations modeling and then
uh
share this report and dashboard with my
colleagues in the organization
also i have for the as
same as a heavy for flow and power
automate i have a lot of standard
connectors today we will use business
central standard connector
and in the end when we when we publish
this power bi report into
power bi service we can easily share
this report with colleagues or we can
embed again this power bi report which
is combined from them which is created
on top of multiple data sources
into business central
with powerapps
what we can do we can create a powerful
applications
uh with low code or no code
with with
it at most the no code uh developed
we will see today in the demo how you
can create easy applications for example
to check and block the customers and
block the customers in the business
central
here we have the three options to create
first one is the canvas applications
which you can develop and then
share it on your mobile mobile or tablet
device
second one is the model driven where you
can create uh moto dream applications
which are similar to this customer
engagement and uh
layout and where you can create it on
top of cds and the last one is the power
portals which are uh announced in the
power app
and all this
will be on top of common data service
we saw yesterday that business central
will
[Music]
will
have a possibility to store the data
into common data service right now we
have also possibility to do some
tricks and magic to how to export data
to the
through the o data to the common data
service and have the single source
of data for all your applications so i
can create multiple applications based
on one common data service entity
and this will unify data across all my
applications which are which i can
use in my common data
so as
business center as a data source
we have more than 40
standard connectors which are
available as a in flow or power app
and
you can also use
business center as a data source to
create for example
custom queries and custom pages into
visual studio code
then you publish these queries as a web
services
into your
business central and you can access to
them with power bi
and we see that we will see that this is
very easy
for someone for example like me who is
not
the hard developer level 400 that easily
to create this query and use it in power
bi or later in the command data service
and this is the way how you can
integrate easily dynamic 365 business
central with the power platform
products and this will for you for your
user this will give some
[Music]
additional uh experience and
they will have a possibility to work on
the applications which are familiar to
them
so to
stop with talking let's do some
practical practical examples
so in this demo i will create
one
uh extension
and this extension will
uh
in this extension i will create one
query and one page of type copy
i already create some environment here
so i will just put here
sandbox name and
tenant
and log into my business central
okay
i don't need this
what
okay
so what i did i enter my sandbox name
and tenant which i will use for this
demonstration
and i will i don't need this
startup object
like this
okay and now i'll create i don't need
also this demo extension
so i'll delete this
okay now i'll create one query
for my customers
okay
i will stick query
so here i have the
standard
option to create my new query
so i will start with entering the id
and i will enter
customers
okay and i need to specify
here what will be the mine
source
so i will use my source
customer customer tables and heroin
customer
and i want to track all my customers and
their balance
and see when the
some customer has high balance to my
users to able to block this customer
later in the power app
but first what i want to create is the
power bi report where i will show all my
customers and their balance
so here i will
in the column name i will enter customer
number
i don't need these filters i have also
possibility to filter my query my data
and i can also delete this
and now what i can easily do just copy
this few more times
and here i'll enter customer name
what is the for example
region
if this customer is blocked
and for example
customer balance
in local currency
so this is my first query where i will
get the customer data from the business
central
and what i also need later in the flow
because flow works with this id of the
customer
i will need one
helper page which will be page of type
ip where i will get this information
about
customer id
so i'll create the new
file
type copy
okay
it will be customer api
table and here i have because of the
page type i need to specify additional
parameters for this
page
so
publisher
zero
and here i need to specify which table
so table customer
okay and now here i need to specify my
field
so first field which i will
use is
system id field
so
in previous versions this
field was called
just id
and i will call customer
and what else i will need i will need
one
it has two more fields
customer name and customer
number
okay so this is my page
i have
okay
brackets
like this
okay so this is my page and now if i
publish this extension it will
automatically create the objects on my
business center but i also want to
automatically publish this as a web
service
so i will
create new file
xml
and what here i will
enter the web services
and now i will publish my
query and my page as a
web service
here i can specify which type of web
service it will be
so we will enter page
so the page
okay serious name
api
it will be published through
and here i will also enter
the web service
to the query
customer
true
and then i will save this i will just
check once more the page id is the same
correct and it's correct
and what now i'll do i will now publish
my extension
first i will log into business central
okay
so this is really easily
developed by consultants or any not so
non-tech
persons
okay and now i when i
publish this
and if the gods of the demo will be with
me
these extensions will be
published to business central
okay successfully
okay this is my
environment and now if i go to
web
i will see my objects
that they are published as a web service
so these two
these two objects from the my extension
so page with type rp and my query which
which i will use to get the data from
business central
and now what i can do based on this i
can create powerful reports in the
in the power bi
i'll open power bi and i'll click get
data
more
and i have several possibilities i can
use for example oh data or i can use for
example business
central connector
which have also possibility to connect
on business center on premise or
business central in sas
okay
from the november 2019 we have
possibilities to choose the environment
in power bi so i see that here i have
several environments
and i will choose my
now database
environment
and here i can also choose
my company
and now i can easily find my
service names so customer api
and query customers
so i need this one
and query customer
and i will load this to my
power bi
okay now what i if i take a look at my
data
see that i here i have the
this field customer id which i will
later use
for uh
my flow
and now i will combine this for example
into
one report one data source data set
so i'll go two and eight queries
and here in the customer query where i
have information about my customers
i will merge these queries
this
okay
and now i will just append this field
customer id
into my query
so now here i have my customer id
so this is the customer id
and i will just rename this as
so now i have combination of these two
data sources into one query so one data
set
and now i will create my report so it
will show customer balance by customer
name
and what i
name
and for example i want something like
this
and then customer balance i'll put the
details
which is important for my client and
here in my query customer
i will say that
customer balance is some
currency field so i will go modeling and
put
currency
for example english
and now this report is available for me
but i want to share this with my
colleagues
so i will first i will save this
i will save this power bi
file and now i can publish this
to my
uh to my power bi service here i created
also one
workspace
and then i log in to this workspace
i will see my report published here into
power bi service
which is here so this is the first part
where you can listen connect
a business central and the power bi
and we have this report here available
for our user
so let's continue with
our demo with our presentation
so we saw that we have we can easily
connect business central with power
platform through the oh data
and when we speak about power
bi what are possibilities that we have
power bi applications which are
predefined reports developed by
microsoft which you can use for your
uh for your
analysis and airports
you can also use this power bi reapers
on road center and also on
uh list pages where you can uh easily
filter the power bi report based on your
selections in the business central
and you can also embed this on the role
center
from the other side we have the
possibility to connect business central
with powerapp so we have connector for
the powerapp and we have also connector
for the power automate also known as
flow
here we have
about 10 or 12 uh flow of templates
which are predefined
templates which you can use
for your uh for example approvals and so
on and by that you can support your
business applications uh and uh business
processes
uh in your organization
so with this i will continue to my next
demo now we will create some uh complex
for example powerapp
and cds scenarios
so first what i will do
i will log into
make.powerapps.com
here i will just switch my environment
to production
okay
and now if i go to the data i can see
some entities
which
are available in my
power
app so my cds
and here
if i click on get data get data
i can
get the data from my business central
through the odata connector here we see
that we don't have this busy central
connector but we have workaround which
we can use is all data
also you can combine data from the excel
in the same entity and so on
okay
here i need to enter my connection
string and what my connection string
will be for this scenario it will be my
oh data which i created
in with my extensions
so when i go here
i'll just copy this link
okay and i will create a new connection
relational account
okay
and then i click on next
right now the the
business center will send data to my
uh transformation where i can for
example edit queries
make some modifications
for this i will also get my another
data
page
so here i entered
in the
url field i enter my odata
url url
in the
uh
authentication account i kind i sent the
organizational account because i'm using
my organizational office 365 account and
i will click on next
okay
so here i see that i have similar uh
environment as i head in uh you know
in the power bi so here i have some
queries
and i'll call this
customers
and this one i will
now i will combine again these two
queries
take the similar process as we
had in the
power bi
and now i will just leave this
customer id
column
so this is my final result
where i have my customers from the
business central
and i have this customer id field
i will rename it to
okay
and i'll click on next
here i need to create
or to load to existing
entity what is the enter entity will be
some representation of the table from
the business central in my cds
this helper
query i will not load to my
cds because it will just help a page
which i will not load
upload
and customer balance i can choose if i
want to
load to existing entity which i
previously created
or i want to load to my new entity
so i will load to new entity
here i need to specify
the entity name
entity display name
and some description if i want to put
some description this i will leave as it
is
and here i need to specify the my key
fields this will be the number
uh
it cannot be multi-line text so it's not
supported to be a key fields
so i will
switch to text
and also i will also switch this
to other fields to text
and here is primary name field
i will choose the customer number
okay
so this is the setup which i did on the
field mapping where i map the field from
my
source from someone from my query
customer query
to my destination fields which will be
the fields in my cds entity
and i will click next
here i have two possibilities to refresh
my data automatically or manually
if i select manually
i can specify
how and when i want to this data will be
synced so for example every 10 minutes
this data needs to be automatically
refreshed from my
data source
and now i'll click on create
okay what now uh powerapp or cds will do
it will create an entity
called customer balance
it will
pull the data from the business central
it will enter this data into my customer
balance entity and create
the fields and enter the data into that
fields
it will take just a few seconds
okay so now it's completed so it means
that it creates in background my entity
and
uh pull the data from the business
central
i'll click on close
now when i refresh my
entities
i'll get my customer balance entity
with
of with fields from my query and some
other fields which are created
automatically when you create new
entity
if i take a look at my data
i can see my data from the business
central
in my entity
so this is the this is the first step
how you can easily create the entity
from your business central data
so now for example that we you showed
you saw that a customer blocked field
was not was not the option set it was
the
text field so this means that when we
receive the data from the business
central it will be stored as a text
what i want for my user at the end has
possibility to choose one of the options
which are the same as
in the business central
and for that
i will create one option set
what adoption says these are predefined
options options of the option fields
which will be used later in your
application
so i'll
enter the display name
so for example customer status
and here i will enter all my options so
not blocked
oh
or ship
so these are the standard options which
you have on a customer card when you
open the customer card
instead of
not blocked you have the empty string
okay if i take a look
okay so blocked field ship invoice and
all
okay
and if i save this
it will be automatically available in my
options sets and now these options that
i can use also in my any other entities
in any other application so it is here
it will be used by the multiple entities
now i will return to my entity
customer balance
and now i will add a new field
this new field build code
customer status
and instead of text it will be
the type
option set
so like this
and if i choose option set i have
possibility to choose one of my
option sets in my cds
okay so i will choose my
customer status
and i can define some default value if i
want or i can leave it like like it is
and i can click on done and now i save
my entity
and if i take a look at my data right
now
i will have the field
customer status added to my entity
and this is
like you have you like created the field
in your
table in business central
but right now this is not editable i
cannot kind of do anything here i need
to create for example some power app
in in this case i will create one canvas
app which will be
then
used by mobile mobile phone
so if i go to home
i have the connector for common data
service
okay
and here automatically recognize my
account
and all my entities from my common data
service
and here i will find my customer
customer balances
and i will click on connect
in the background powerapp will
automatically create applications which
i can
use on my device or
from my web browser
okay so this is application based on my
data from the cds
and now i can do some modification
at least
i can
change the fields which are shown on my
application
so for example in the subtitle
i can use my
name
and here in the title i have this
information in the body i have this
information about customer balance
and for example i want to
change the property of
this field of color
so for example
if
customer balance is
300 then it's
so red
automatically format my
application
based on the
properties which i set for this field
subtitle
for the field body
okay
i can also navigate
on this application i can edit
informations
but what what is interesting to me
when i go to the detail screen to have
possibility to see the customer balance
and customer status
when i click on detail form
on the right side
i have possibility to change my fields
which are visible on this screen
and for example this created one is not
important for me
but i want to add fields so
customer balance
and
status
it will automatically add this field to
my detail screen
i will also change the
name
and when i hear on my edit screen i want
my user to be to have possibility to
choose the status of this customer based
on the
his balance
so on my edit screen
i'll also change this
on my edit form
i can easily
remove the fields
and add fields
status
okay which will be my drop down field
now if i
check i have these possibilities from my
option set from my
cds
okay
and now i can easily
save this application share it or
deploy it on my mobile in my powerapp
application
okay
now i will go to file
i will do i will enter the
name
choose some icon
and i will save this
okay
so this is my application fully
functional which are now available for
users
what the next goal for me is to do is to
use this customer status field when it's
changed to update my
information into business central and i
can do this on several ways but i will
use
microsoft power automate or microsoft
flow to do the
migration of this data from the cds to
my
business central
okay
i will go to flow.microsoft.com
and here i also switch to my production
then
and now here i can create
my new flow
if i click create from template for
example
to see these standard templates
i see these
available templates which are
created for the business central but
this is not interesting for me
i'll create my
automated flow
and here what i need i need trigger so
when my
data is changed into in common data
service
so i need trigger for common data
service
and when my record is changed or updated
and here first what i need i need to
select what is my environment so enter
the production
and here
i need to send select my entity
customer balance so here we store the
data with the power app
so
like this so my environment
my entity
and i will define the scope
for example organization
and now when my data is updated what i
need to do i need to check my field
customer status
so what is the value in that field
so i'll use control
and i have this
switch control
okay here
i need to
choose
on which field i need to
check control so
i will use the field
customer status value
as you can see
this field is called customer status
value this is not that you will check if
the customer is in status
blocked invoice blocked ship but you
need to find the value for this option
in the customer status field
so where i can find this
if i return to my
make that powerapps to my option sets
if i go to the customer status field
here on my options
i have possibility to see all the values
for each
option which i have on this field
so these are my values for example if my
customers is not blocked
and i need to copy this
right now we can't copy so i need to
type it manually so here i will enter
that in case my value is
not blocked
is equal to
like this
so when my value is in customer status
field is
this value
then i will do some action what i will
do
i will update my data in my business
central
sas we have connector
possibilities to connect also onto my
on-prem
if i take a look i have these actions
for my business central
uh with central connector and i need to
update my record
so which record i need to update the one
which was changed in my cds
so now we are making the connection
between uh
flow and my business central
okay
and in the environment name
i need
again i need to choose my
environment so it will be now take this
in the company
i need to choose which company i will
use for this
integration so my chronos uk
and in table
i have all these 48 standard apis which
are available in my flow connectors
if i want for example update some custom
master data or for example custom
tables which are not available in
my standard connector with
between the business central and
flow then i need to use my custom
connector as a
as actions uh in
my flow
but luckily here i have the
customs customers
and now i need to specify which row id a
row id is and row id is the customer id
which i
import to my imported to my query
so if i take a look
i need to find customer
id field
customer id so this will be the unique
id of my customer
and now when my customer is not blocked
i will just enter the empty string
in the blocked field
so like this
and now for each of these steps i'll
create the same
so
name
sheep
okay an action
update the record
so my company again table name is
customers
and i will enter the value
ship so it will
send the value of option type
for my in my option field blocked it
will send the value ship
okay
for the
invoice
two
we also have a possibility for example
to copy
uh to my clipboard and then paste it but
it's still in preview mode so it doesn't
work for
the business central
connector
to invoice
and here i will add additional one
for all
i'm gonna take a look
okay
customers and now
row
id okay so this is my
custom flow
which does not have so many steps
so when my record is updated go and
check the value of
the field customer status and update my
business central record
and i'll call this cds to
status
now i can
save this flow
okay and i return back
okay so this is my flow
and now i can easily
start and test this my application and
for example this
customer
has a high balance so i will put this to
for example invoice
and this will get customer status
invoice
if i take a look at my
cds
entity
customer balance
i see that customer balance is changed
let's take a look at flow
it said that it succeed
if we take a look at what he did
so my record is updated
and i see that it gets the value for the
invoice
and it updates the business center of
record
let's take a look at refresh the
the business central
customer 30 000.
i see that my customer
is blocked with the option invoice
thank
you so uh this was the example where i
showed that how you can uh manipulate
with the data in the business center
based on the business center data
imagine that you have some other systems
such as dynamics 365 for sales and some
sales guys call you and say please block
these customers all the shipments for
this customer
so you can he or she can easily do this
in the powerapp or you can based on this
data which you you which are available
in a customer engagement
sales module
okay
so this is
this demo
and now alexander will continue
just to switch my bike
okay
then i had to show some
really exciting
demos how you can use powerapps with uh
busy central outside of busy central and
power bi and so now we'll continue this
story uh how we can integrate uh
busy central with some additional
solutions
in this case i will use it
with dynamic 65 talent
actually we saw on
keynote that we will have some
additional features in busy center with
connection with cds but
this started
long before uh this new feature
and
i will use from technologies i will use
logic caps i will not use this time flow
actually power automation i will explain
later why but again we will use cds from
talent side
and we will use apis from business
center
how it work generally
dynamic 65 talent
is not based fully on cds
these two additional apps from talent on
board and attract are fully
cds apps and if you want to
make some automation for example if you
want to use only attract for recruitment
process you can integrate attract fully
from cds to busy central but if you want
to use full hr core system in this case
this is not
this
talent is not fully on a cds but almost
all entities from talent are already a
cds that means you have some back
integration between talent database and
cds but it work
in this by example we will use entities
from talent that means if we are using
uh talent as hr system that means we
will use hr system we don't need to use
to hr system in a parallel uh mostly you
need this data from uh talent in your
busy central for example if you you need
employees for fixed assess module for
some additional modules if you
create for example payroll system you
will need the same employee data as you
have in talent as you is your hr system
and because of that i think that the
best integration is take data from
employee data and similar data from
talent and move back information about
payroll time registration from business
center to talent
and now how to make it
yes i can fly for them
okay
i have here power apps and
as i mentioned
we have cds entities from talent on
here in
cds first we need to change our
environment because when you create your
power app you will get
contoso default
environment
but if you install
talent you will get this additional
environment
okay
then
okay i have talent system here if you
want to see
where our data are placed for example
personal management
and
here we have
all workers
and
we need to integrate workers entity
workers table in talent with employee
table in business center
and this is not so fast okay
okay we already have some employees by
defaulting here in busy central and what
we need to do
we need to find
our entities
and when you run
you will see that there are
there are a lot of entities from
just
to move filters
from not only default entities as you
can so you can see in a
renato demo because
when you install entities you will have
i think 15 something about 15
entities by default but when you install
talent you will get much more
we have
i said almost all entities from talent
are here
and
what we need to find we need to find
workers
works are here
when we look in workers
data
we will see there is the same data as we
have in finance operation
and now what we need to do
as i said i will use a logic app i will
not use flow it can be done with flow
but
it will be much comfortable with logic
apps
for logic apps you need to have of
course azure
portal
you need to have agent subscription
of course
you will find logic app i don't know
your experience with logic but more or
less they are almost the same
when you speak about user interface with
flow
and
i will say
bc
okay
talent to bc
okay i will create a new resource group
and location i will use
not central us actually not
i will use less europe it will be faster
ok and create
i forgot
okay and we created
just few seconds
for deployment
okay now i can go to resource
this is just created as uh as a service
we don't have anything we don't have
flow there
now we need to create flow
and you can see this is almost the same
as the flow we have templates we have
everything we need we will create
everything from scratch
and what we need to do is to find our
common data
you cannot find talent as a connector
because we don't have a
connector for talent we have for common
data service but as talent is on common
data service is the same
and first we will use the record is
created
i need to sign in
and i will need my username
i don't know
exactly
by uh one of the reasons why logic caps
is better you see uh you need to use
some specific credentials
if you're using flow every time you will
leave general you will use your
connection with logic apps you can be a
system administrator you have some
specific account just for integration
and you can use this
independently this is much better for
some uni-specific integration cases
okay now we need to find environment our
test drive
this is something what we had there
our entity is
a worker
just give us a second
okay
workers
and scope
organization
and that's it
we have bank record is created now we
just need to move to busy central
okay here it is busy central and again
this is creation of record
create record here
now again connection to
busy center we can use upload different
account this time
but i will use this the same
okay
yes production environment
we will use my kronos
table name is
employees yes
and now we need to add parameters
this is again similar with
flow we just need to check
what parameters you want to use i need
minimum number given name middle name
surname okay we can continue more but it
will be enough
for number
i will use
working number
this is what we have for talent
for given name this is first name
middle name
and last name and surname okay we can
add more
but it will be enough
we just need to save it
and
as this is a service we need to run
because we can just create
but when we run now we can use it
and if i go back to my
workers
and create new worker
okay
alexander
oh not here
okay
start date or
for monday for example
just keep in mind this
you see you don't have many fields here
in in talent if you have any situation
that you will use talent
you need to use uh two different logic
apps one for recording and one for one
creation you record and this is for
insert another for update because
when you click higher that means you
will enter just this information if you
want to continue to add additional
information address phone emails and so
you need to say hire and add details but
after that everything what you add
additionally it will be updated in this
table that means you need to have these
two logic apps in parallel logic after
flow in parallel this is necessary
ok
when i
refresh
my employees
you see i have
new
here and this is really fast it works
immediately means
in milliseconds
okay you can
control now activity log and everything
what you need
from here
i need to refresh
yes you have
actually
3.73 seconds immediately you have
immediately pushed after that
okay as i said you need to
add
updates
as well
but
this is for some other time and
generally as i mentioned logic caps is
a full azure service i much prefer to
use logic apps for integration uh than
power flow actually power automation
power automation is good tool but from
my perspective not for integration cases
you need to have something powerful
working immediately and not only that
you have these three the last things
uh
if you need to change something in your
flow you cannot do it flow you know in
flow you have only user user
experience but when you're using logic
apps you can use
logic apps on azure portal but you can
use any visual studio and visual studio
code as well and this is very important
and not only that you can change a code
even from
azure portal
for example you have one thing here in
talent you cannot integrate without the
code for example you cannot integrate
gender because gender are optional
fields in the boto system and they are
different and if you use logic app or
flow nevermind you will get error
message and because of that you cannot
use flow for all cases in this case
logical is much better because you can
translate this gender
i don't know if this is male female
what kind of i cannot remember exactly
difference i know that there is some
difference
and you have this one
i think good table
how to decide when to use
flow or power automation i mean to use
logic apps
generally if you
are a office worker if you are a regular
user for you
flow is much better this is first this
is already included if you're using of
course business center on cloud this is
already included your description you
don't need to pay nothing more and this
is for some regular automation really
good but if you are a professional if
you're a systematic integrated system
administrator or developer for you logic
as a better again depends of scenario
for some self service flow from some
advanced scenarios
much better logic apps as i mentioned
this designer tool uh for power
automation you have only power
automation uh browser and mobile app of
course another site for uh logic apps
you have visual studio visual studio
code you have
everything in code is available every
time
you have full application uh management
with azure devops
really serious
admin experience with a resource group
with connections so security is
much higher level and so
and okay you have these sites and you
can download it
i think this is a really good decision
when you want to choose
i i don't want to say uh that logic apps
is better or not depends on scenario
this is the same situation what car is
better i don't know
you you first need to know what you
really want from the car if you need if
you really know what you want from your
system for integration for flow then you
will be in the right way how to choose
the right model
okay now renat will continue and renato
will show how to embed power apps in
busy center right is possible yes
there are some tricks but yes you can
embed these
powerapps in business
central of course this is the my last
slide today
so it is only the demo so uh what is the
the case for example that you have your
uh powerapp which is based on some other
source for example sharepoint list and
so on and you want to do the
manipulation of this sharepoint list
through the powerapp but you have the
data in business central
why you need to go every time to your
powerapp
then change the data and in your
sharepoint list or
go to the business center and take a
look at this
informations
in business central in embedded app
so how we can embed powerapps into
business central
let's take a look
if you remember i created this power bi
report from my in my first demo and here
i have information about my
customer balance
and uh
their name
what i want that for example if this if
i have the power app which is based on
the
customer engagement data for example
sales or marketing where we have
informations about customers to
block this customer in business center
based on the data from
crm
and how i can do this for example when
i'm here in
power bi service
i can click on edit my report
here i can do a lot of
transformations of the
these charts and visualizations
of on the existing or i can create some
new charts
and here in visualizations i have
possibility to add powerapp
into power bi
so this is the first step which i need
to do
so i will
click on this
small icon
and the new chart will be added so new
part will be added into my power bi
report
which is called power app and here are
the steps how you can easily start with
embedding power app into the power bi
so
what i will do when this is selected i
would just
for example drag and drop customer
number here
a system
will ask me do i want to create a new
application
or do i want to choose some existing
applications which i already create
before
i have my applications for the customers
so i will choose my existing application
oh
and here i have some
applications which i used before
and i need to choose my
environment
so now there is production and here i
will see my
power up power app
application which when i click on now
take this and click on
add
close this it is many more
will be available in my power bi report
so this is the same application which i
used
which i used in my power app which i can
also use on my mobile phone
if i take a look for example this
customer
30 000
i see that it has these status blocked
to invoice
okay
and now how to uh how i can this
embed to my business central
through the power bi connector between
business central and
uh power bi
so first i will save
service this can save as new report
oh this is my new one
okay
and now if i go to my business central
and if i scroll down
i say that you have possibility to embed
your power bi reports into a road center
client a road center
or into
customer release
or vendor list or item list
and then how you filter your data in
this list you will be able to
filter also the report
because there is a bigger screen on the
road center i will embed this
here in my
role center
and here i have
i need to
okay
oh it is the same
like this one
okay
i will see my power bi report with my
power app embedded in
power bi
on my role center into in business
central
i also can for example expand this
report
and in a few more seconds when it loads
this power app it will show me my power
app which is which was created
in my previous demos
and this is not necessarily
to use report you can use it without
reporting yes the eight blank power bi
report and address
yeah
yes this is the so this is the
example i have these informations
between of from one report and then i
based on this i want to block my uh
customers i can also do without this
left side without this graph just to
have only power app embedded into
my report and now i can for example
again and edit
because you don't need to make some
additional tables especially for sas you
don't need to create new tables uh for
sas you can create something in cds or
maybe even on excel as data source and
embed here to be centered this is really
good yes i can make decisions into
business central and make actions into
business central from the various source
so for example i have my data in
customer engagement or in cds from
some i don't know
on-prem solutions which are my data in
cds then i put this data into cds and
then based on this data i can make
decisions in my business central
so this is the way how you can embed
powerapp into
the business central
and now alexander will continue
we don't have so much time i will try to
be fast with this the last demo
how to create model driven power app
based on bc
i don't know your experience with modern
driven powerapps i will try to avoid
reading of these things because we have
a really small amount of time
more or less model driven is a crm
environment and if you ask me why i will
use crm environment with busy central
data
just imagine you have a customer who has
already busy central and crm and you
have hundreds of users of crm and they
are not natively users of busy central
if they need just some entities some
specific information from busy central
you don't need to invest
time how to train all these people about
new user interface if you ask me from me
busy central is the easiest way how you
can use something you can learn very
fast but if you ask clients sometimes
this is not the same we have probably
different opinion especially if you ask
crm users they
used to use their own environment and
they are not you know willing to
uh to use something new
and because of that you can move for
example in my case i will create for the
employee maybe they they have some hr
people in crm side they don't need to
open every time a busy central if they
want to have access or maybe time and
attendance
you you have this time registration in
busy central and if you need your users
for crm site all users just to enter the
data there you don't need to
create users in business center you can
use the cds for this and create model
driven power app
how to start with this first business
center is not based on cds this is
effect on other side model driven power
app can work only with c8 cds
and now we need to find some work around
how you can do this generally
you need to create copy of your table in
busy central in cds
in my case i did it with
employee you have when you create and
you don't need to create full table
depends what you need from data in uh
for your users you can create only i
don't know seven six or ten table uh
fields depends what you really want
to show other users
when you create it you need to connect
something similar as relatively show how
to get data through all data service or
through api or something like that
or you can use flow logic app for
integration many different things
as i said just try to be smart how to
find a good way how to do this
okay i will try to be fast to have
enough time for questions
okay when i open my entities
you will see i already created because
i knew we will not have enough time
to create everything from scratch you
will see my bc employees
entity and you will see i have
some fields here
there is no data
this is empty i created two fields
two keys one is based on number one by
the two names something similar they
have in the employee table in a backy
business center just to avoid some
duplicates
and
then what we need to do
we need to
say get data to integrate
the system
and i just need to use my url
ok you already saw this page you can use
all data you have api depends what you
want to use in our case or data is
generally the best option
i will choose
the web service i published for
employees
okay connection name
authentication kind organization account
just to be sure
i don't know what i used today
okay login
yes
and
go next
come on
there is not so much data
okay this is what we have there just you
new things
okay
existing entity i need to find my
bc
employees
where you are
uh
yes
why this is not so easy to find because
this is custom entity and you have this
prefix cr depends uh from environment
every time
and what we need to do we need to map
this data okay this is address i will
take address i hope i will not make a
mistake
city
we have a county
ok
email first name
yourself
title
last name and
middle name
okay we have something more yes number
is important of course
i know
i will avoid that never mind
they're not so important
okay we can choose refresh manually
refresh automatically i will say every
10 minutes
and create
when you try to do something really
fast
okay i hope a few seconds it will be
finished
okay i will speak what we will do later
when we finish with that we need to
create new model driven app
generally this is more or less
same and
procedure the same as canvas you need to
start with new model app mode new power
app
you need to choose name and then there
will be different because
they are not the same because when you
create a canvas power app
okay i don't need to speak i can show
you
okay model driven app for blank
create
i hope i will not forget something
because we don't have
much time
okay vcm please
unique name again
we can use something different we don't
want right now
and okay now we have
a designer from all of the even power
apps we have sitemap this is more or
less something
uh what you make as menu
as a new group i can say this is
hr
snoop submaria
i will say this is employee
and okay
i need to choose this is okay
selective type entity
i need to connect with my entity and now
i need to create in my bc employees
and okay now just save and close
this is already created actually i can
open right now yes first i need to
publish then i can
open my
environment
now i have some forms
but this form by default is
really simplifying you don't have all
these data you have from
your employees
you have only two fields
okay
you can see you have only this
oh this is not the best
okay i will add component
the component i can add for example two
columns
and then
okay new tab
something like that then i will add
fields
and i can add for example my
first name
last name here
here i will add
i don't know email
or job title
you can add what you want actually you
need to save
and publish
ah it requires some time
okay
again 7 close now
when you open here i can see you have
you will see i have this my bc employees
i will get error message because i
didn't publish this app
i just i published uh my form but i
didn't publish my app
what i need to do is to publish
okay
but and what they want to show you these
forms is what you see something similar
are a car page in uh bc
but if you want to see more uh in a
table
as a list you need to add new columns
you need to do something similar as i
did with forms with views now we don't
have enough time to show you i will try
to be very fast
you have this is this is what i
mentioned you have only number as a main
field you don't have other you need to
customize
uh this view but when i open this one
you will see i have my
name last name emails what i added
you have this general where you have
number this is by default
but you can add as many fields as you
want and there is only one limit
if i create new
i can do this i can say
ok
here i will add for example alexander
louise and nevermind and when i say
seven close
i will save include i will save it only
in cds because this is all date or data
you can move you cannot push back to
busy center if you want to do this
feature that means if you want to have
uh
this possibility you need to create flow
this is the best way because this is
very easy you don't have millions of
transactions here this is something very
easy and flow will be more
than enough for that
you just need to create you have
actually already templates for that for
accommodate the service and to move back
okay
i really try to do it
the faster possible
if you have some other questions about
it i'm here i will try to
help about model driven or you can send
me mail if you don't have enough time
right now i know we have
okay we have two seconds but we have few
minutes for uh q a of course
and they're not with you
so for you
thank you one short question at the
beginning you
made your rp with one rp page and with
an odata web service
is this a pattern where you have the
what do you do with the query and what
do you do with the rp pages i use the
app page to get this customer id because
uh when i have this uh query
uh i cannot add the
id field system id field to the query
because it queries not of type copy
that's why can you pass it yeah
um when you embed a report into the
business center role center can you then
make the selection based on
system variables like the user's
organization or country or something
oh yes you can make
so
thank you
quick question you said that currently
bc doesn't live in cds is there any plan
of moving
vcu cds and
do you have plan of including cds
license in
bc license
a licensing question and a question for
rnd team what about the plan
even if i know something you know i
cannot speak about it you need to start
our summer far in the team right okay
you know as soon as it could be on an
official road map maybe publish it okay
but right now
sorry i have probably my back you showed
a scenario where the blocked field is
updated in bc that is fine but do you
think it's possible to go for a more
complex scenarios like maybe make an app
that that
triggers
an action
written by a developer in bc like what
i'm aiming at is maybe an application
for
processing warehouse documents or
anything like that in powerapps actually
or there's just a data passing from one
end to another without the possibility
to trigger any logic on the other hand
you mean to for example post the
production order for instance or
whatever right yeah
for now this is not possible okay but we
have the inflow of some possibility to
call the action
which is available from the last update
so it will be possible but we need to
wait
more more details about this okay but
you know it depends from scenario and
depends what you want and uh
but i decide um canvas power app is
something for really simplified
processing we try to make uh some
processes very simple to find not to
make you know standard development tool
okay
th this is you know you you need to make
differentiation if you want something
complex you know in this case probably
it's the best to create uh some
extension development and you have one
client if you need it but
i think this is uh probably uh canvas
powerapp is not tool for okay
again depend from scenario to scenario
this is possible but
uh you need to have a real reason why
you will do it in power apps
if if you already saw this in uh busy
center why you will use the same
function in power app
this is general question because if you
made it in busy central use it in
business central power rep even
something additional just don't waste
your time customizing something very
central
this is an answer that means you can
make something but this is not the right
intention for bdd center for powerapps
sorry
okay hi thank you for the session i have
one small question about
what's not clear to me is what is the
difference between the
web service publishing page
and the rp publishing page
okay i did everything to the all data
yes oh data okay yes so i published the
because i can't uh
have the query
with the type api
published as a web service in from the
business essentially i'll get the error
that the query does not exist
and then that's why i published the page
of type api to get this customer id
and then i connect this customer id with
my query
in my uh query
or data
okay
api of type query yes
query of type api
yes
it's the page of tape type ap api and
there you can also then you can add the
field cast system id to this page of
type
thank you
hi thank you for the presentation
i have a question about when you're
creating a flow there was a action
choosing
and there was a highlighted text
premium that's a subscription premium
for the power flow
we need if you want to
react on a
modifier or insert in the
field
can you can you
you you you must have a
power flow premium account for
for for business central connector you
need to have premium accounts yeah and
the second question
when
you
uh that's is the
power pro
premium you you must have power bi
premium
for which one okay for
refresh that uh in
in the embedded power bi in the business
center yeah because if if it's not
premium you have a data in inconsistency
yes yeah so about the licensing
alexander
yes no it's not the last licensing but
when you have a power bi pro
subscription you have you have a limited
of eight
times yes refreshed of the data and when
you have premium you have on the on
demand that is
if you if you work with power bi in the
same case you
may be between the refresh
times
the balance will change in your
uh
power up
someone will block but the balance is
changed this changes i understand and
now i understand yes uh yes
this becomes can be the case when you
for example in the end of the day you uh
your end of this eight eight uh
refresh okay possibilities and then you
will not have the refresh data in power
bi thank you very much
um if you build your app to change the
status of the customer you always enter
the company chronos and
uk aus in the app is it possible to
build the app where you first choose if
you start the app in which company you
want to work and then
to modify the status for the customer in
the company a and when i choose next
company or is do i have to duplicate the
app
right for now when i choose the company
in the
business central connector i must select
from the existing ones
it will be maybe possible in the future
when you have for example to set
variable
in the flow and then pass this variable
to the connector of the business center
right now it's not possible okay thanks
hi uh i have a kind of a follow-up
question to the odata connector um
so i mean currently
a lot of users are using uh the
on-premise databases and if they want to
build up a business intelligence
solution that's a bit more complex for
example
we can leverage the on-premise sql
server to do this um but when we move
into the cloud completely with the new
business central so we're only limited
to using the odata connector that you
showed earlier
so this is this is central the uh
connector and
all data connector yeah of course
they're kind of the same yes um
but i mean it's it's all well and fine
when you only have five lines the way
that you showed
but
what if you have say general ledger that
contains millions of you you will have
soon incremental
uh feature
okay so that's coming yes
it will be soon i just read this this
morning uh it could be it would be
published so and also what i suggest
when you have the big data set that you
are with the query make the
modifications and do use only data which
you need in your flow power app power bi
to expand all the gl entry page yeah but
i'm also worried because there's a one
gigabyte cap on how much data you can
move
per day
so i mean
there's an issue for me especially when
i mean the old data is not really
possible
completely in a in a
quite heavy production environment i
mean
um so this is just one of my concerns
this is generally an issue but a bit
incremental it will be probably solved
but what about
moving instead to using can i mean
can you do what i'm asking is can you do
a data extract in some other ways the
workaround for this at the moment
using the api and
extracting data that way
maybe to some other other
external application where you will
store your data yeah from the business
central and then do the
uh all the reporting and analysis and
this with on that external data or some
cubes a data layer that supports some
kind of pagination yes
for example you uh
store data from to external system at
the end of the day at the beginning of
the day in the middle of the day when
there is no peak on your uh process and
then
uh do the analysis on that data which
are exported to external system yeah but
this is this is a worry because i mean a
lot of customers they need much higher
granularity of data than i mean even one
hour is is too little
and only having it eight times per day
and one gig max
and being especially when you're forced
to do this and not have a workaround as
we do now with leveraging sql server and
going straight towards the database
and when we lose that possibility then
i mean we need other ways to do this as
well
yes
i hope that will be the new ways
to big bigger data sets
thank you
okay let's see there is no investment
that's all
thank you very much
