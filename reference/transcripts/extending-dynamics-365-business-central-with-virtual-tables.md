# Extending Dynamics 365 Business Central with Virtual Tables and Business Events

- **Source:** https://www.youtube.com/watch?v=4KMRNJ4rpb4
- **Video ID:** 4KMRNJ4rpb4
- **Channel:** mibuso.com
- **Published:** 2024-06-16
- **Duration:** 89m18s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

Hi everyone, and welcome to our session
today called extending a business
Central with virtual tables and business
events. Idea is here to show how we will
extend business Central and connect it
with data verse and some other external
systems. So, before we start with this,
I will just introduce myself. My name is
Milan Milincevic. I come from Norway
currently, where I work as a business
Central tech lead for BDO.
Uh
I started my career 7 years ago as a web
developer, then 5 years ago I switched
to business Central and a vision world
where where I stay until now, and I try
to be as much as active in community as
I can. So, I try to write blog posts,
speak at different conferences, um even
together with my colleague Renato and
with Marin here with
co-founded this B source user group
meetups in Croatia, where basically
every month we have different meetups
about different Dynamics topics.
Also, there is another small thing that
I'm very proud of, and this is a BC
maximizer. If you didn't try it, give it
a try. This is just a simple browser
extension that maximize business Central
pages. So, it is available on Edge and
Chrome web stores.
Okay. Thank you, Milan, for your
introduction. Uh
good afternoon, everyone. I hope you had
a nice lunch. And welcome again uh
to my uh to my uh session.
Uh my name is Renato. I also came from
uh Zagreb. Uh so, uh I'm in Dynamics
world for around 10 years.
Uh started as a developer, switched my
career as a to consultant, and currently
I'm leading a team of uh consultants for
Dynamics and SAP.
Uh last 5 years I'm a Microsoft MVP for
business applications with more uh
details about business Central and power
platform.
Together with Milan, you'll find us uh
on various conferences around the world.
And of course, if you ever ever uh join
and you are in Zagreb last week in a in
a month join to our session
into our community in this source user
group.
Regarding today and why we are here
today is our agenda of course and what
we are going to show you how we can
integrate Business Central or extend
Business Central with Dataverse.
And we are going to talk and see how
what is the Dataverse in general and why
do we need Dataverse in our business
case.
Uh we prepared one business case and
application that will that we are going
to show you through whole scenarios of
data sync, business events, and virtual
tables.
After that, we will go in deep what is
data sync, how you can use it, how you
can extend it as well
uh and use it in Business Central.
What are virtual tables, how you can use
them,
what are scenarios and so on.
Uh business events, something new that
we have in Business Central, so very
interesting concept that will help us to
somehow extend Business Central
functionalities inside the Power
Platform in my case.
And of course, the most important one of
the most important part is telemetry.
Let's find out how our business events
are performing, APIs, and so on.
And of course, at the end we have few
t-shirts for your questions.
So,
uh agenda is here. Let's start with
why do we need Dataverse and what is
actually Dataverse.
And according to Microsoft, it's a data
storage and management layer for
business applications or for
data that is needed for your business
applications.
Uh
it is easily uh
connected to your old existing Dynamics
ecosystem as well plus
Power Platform.
Uh
when you have Dataverse database, you
can store your data inside the tables,
write them in the columns, and uh
use them in various integration
scenarios.
Uh we have several applications from
Microsoft Dynamics that are built on
Dataverse, like Dynamics 365 Sales,
Field Service, and so on, which gives us
uh completely new approach how we can
integrate Business Central because
easily we can then build uh bring data
from Business Central and combine them
with data from Field Service.
Uh we have four different ways how we
can integrate Business Central with
Dataverse. The first one are data sync,
and those are the I would say the oldest
one uh that you can use to integrate
with CRM, with Field Service, with
Dataverse as well.
Then we have data events. So, when
something changed in the system in the
Business Central, send me data and store
that in Dataverse table.
And what we are going to focus today is
how we can integrate and use virtual
tables and business events.
And if you take a look uh what is
actually uh Power Platform, we know that
we have Copilot Studio to build some
chatbots, uh that we have Power Apps to
build model-driven canvas applications.
We will build some applications today
together.
We have Power Automate to build
automations and Power Automate flows. We
can use Power Automate with
business events to trigger various uh
various scenarios. You can use Power BI
to build analytics, and of course you
can build web web pages with Power
Pages. And of course, with latest
release, you can enable virtual entities
and use them with Power Pages.
So,
uh how this works together? Uh we can
connect Business Central directly
through connectors. So, we have
connector uh for uh Power App, we have
connector for Power Automate, but we
also have a Dataverse below, where uh
each of these applications that I
mentioned earlier can connect to
Dataverse.
And when we have data in Dataverse,
from Business Central, you can build
whatever you want.
And this is what we want to achieve
today, to show you how you can build the
bring data from Business Central, what
are different scenarios, present them,
and store them in Dataverse, and then
use various applications.
Uh in our case, we'll show you primarily
Power Apps and Power Automate, but you
can see uh briefly that you can also use
and plug your Dataverse to Copilot
Studio and have a chat experience uh
with Copilot on your data from Business
Central.
So, that's Dataverse and how we can
uh utilize it with BC.
Uh our business process, uh we have
several
uh let's say tables in Business Central,
and it's uh we imagine that we are going
to have a
a rental car or uh something related to
rental car uh extension.
And we have master data for vehicles, so
some new table that doesn't exist in
Business Central. And we have document
uh tables, loan header and loan lines.
You'll see how we can easily connect
those to uh Dataverse.
And our process is uh that okay, we need
to register some vehicles.
For this, we can use Power Automate uh
Power App, model-driven Power App, that
will send data to uh Business Central
through data sync.
It will create a record in the Business
Central table, vehicle.
After that, we are going to
give that uh uh
car or vehicle to our uh user, our
contact. We'll have uh loan header, loan
lines, we'll create them.
Uh after that, we'll publish them and
issue that uh loan uh loan or uh rental
car to our contact.
We will make uh our car uh flag that it
is uh
loaned, so no one can use them anymore
in uh other scenarios.
Uh after that, when vehicle is returned
from the contact, we are going to
uh enter what is the mileage by our uh
field technicians, let's say.
And at the end we'll send an email
uh to our contact, thank you for work
working with us, and uh your vehicle is
registered that it is returned.
Uh so, and we will release that vehicle
because now it's available for other
other uh orders.
So, that's our process, and you will see
that we will use a part of BC, Power
Apps model driven, Power Automate flows
to trigger various scenarios.
Okay. So, now we have Dataverse
integration with Data Sync.
So, as I said, uh
Data Sync is something that
uh
is in Business Central and NAV world
from from the from uh later later days,
and uh we can see this as a connection,
bidirectional connection between
Business Central and Dataverse or uh CRM
as well in in some cases.
And it works based on the batch jobs.
So, when you uh have data in Business
Central, run batch job, and it will
replicate your data inside the Dataverse
database. So, you will have data in both
in both uh systems, Business Central and
Dataverse.
Once you have data inside the Dataverse,
you can book combine and enrich those
data with SharePoint data, with some
other
uh other data sources from uh from your
organization.
If you take a look how this uh works uh
inside the Business Central, so we have
Business Central in our slide,
and we have some
table, customer, vendor, contact, or
company table.
Uh it's visible, perfect.
Uh after that, we have on the right side
our tables that are automatically
provisioned from Dataverse. Those are
account table, uh, contact table, and
those are the tables that are here that
can be custom tables. So, Milan will
show you uh, that we can easily uh,
create our custom scenarios, and then
connect them with Dataverse uh, very
easily.
In the middle, we have integration table
mapping, where we are going to define
what are the rules for sending data to
Dataverse from Business Central and
returning them back from Dataverse.
Here, we can see also that
customer and vendor data are all are
connected to one table in Dataverse
called account. So, you will find both
those data from both tables in one table
in Dataverse account.
And also in the Business Central in the
integration tables, you will see data
from Dataverse. So, you don't need to go
each time to Dataverse to check if data
is already inside the Dataverse table.
Once you have your data flowing from one
system to another,
you can uh, easily build, as I said,
applications or combine uh, with another
source sources.
And where everything's happen, and what
is the most important setup uh, for us
is Dataverse connection setup, because
this is the primary point where you are
going to set up all uh, integrations
related to data sync, virtual tables,
uh, business events, and so on.
So, that's data sync in a nutshell. And
now, we are going to see how we can
easily enable data sync.
Uh, in my case, I will not enable it
again because it would take some time.
So, I took a screenshots while I was
preparing for uh,
for this presentation. So, what you need
to do, you need to start uh, a process
from assisted setup.
And in this case,
uh, you just uh, uh, accept the terms
and conditions, go next.
Then you need to choose your Dataverse
environment to which you are want to
connect. Uh, it is uh, connection is
done per company, so you have one
Dataverse environment per company.
And you cannot have multiple. Uh, after
that you need to sign in with your admin
account. So, uh, you sign in with
account that will be used for
integrations.
Okay, once I sign in, I go next in my
case.
And then what I have to do, I have to
choose if I'm going to sign in with team
uh, and represent my data as a team or
as a person. If I choose person, I will
go then I need to select each
salesperson will be need to be be
connected with my users.
So, our uh, recommendation is as well as
Microsoft to go with a team because then
you will use business units in Dataverse
Dataverse and so on.
And of course, uh, next step is just to
synchronize data and then
uh, you will be able to have data sync
available.
Uh, now I will show you
uh, also in the system
uh, Dataverse connection setup.
So, when I log in to my uh, BC
I can find Dataverse connection setup.
Okay, take some time.
Okay, and I see that I have enabled data
synchronization.
Uh, what is my uh, Dataverse environment
and I see that uh, it's enabled and that
I'm using team as an ownership model.
Uh, under the integration,
uh, I will find my integration table
mappings.
If I click on it
uh, you will see that I have uh, some
standard uh, standard table already
integrated with Dataverse and here I
will find my vehicle scenario that we
Milan will show you later uh
about how to integrate it.
You can run full synchronization or
synchronize only modified records.
Or for example, if you go to mapping
you can create your custom mapping for
your fields.
Uh when I click here fields
I will see uh fields from my table
and I can choose which fields I want to
enable or disable for my integration.
Also, I can change check if for example,
I'm allowed that I retrieve data from
Dataverse or I'm only sending data uh to
Dataverse. So, do I have bidirectional
integration or not?
Okay, so this is the uh mapping. Uh
uh another important thing that we need
to mention are coupling
or uncoupling. Coupling is just matching
your records between Dataverse and
Business Central and defining criteria
uh how how you are going to couple your
data that is in the Dataverse table with
data inside a Business Central table.
Okay, what else I can uh we can show
here and find we can find how uh our uh
log of synchronization and how it works.
We see that for now everything works
smoothly.
So, uh that's that's the setup.
And now uh Milan
I will give uh
words to you and I'll switch to you.
Thanks Renato and now
thanks for this lovely demo and now
let's see how can we extend the data
sync actually. Because usually these
standard tables are maybe not enough for
our use cases. So, idea is what we can
achieve actually is we can enable
add custom fields in standard
um tables objects or we can even create
a custom objects and create integration
between those two.
And that will actually I show you in the
demo. But before I go to the Visual
Studio Code, I will just quickly run on
high-level process how this looks like.
So, idea is first that as Renato said,
everything is based on integration
tables. Basically, these integration
tables are
um
these integration tables are
representation of Dataverse data inside
the Business Central.
So, once we created this integration
table, the next step is to create a page
for that integration table, and also to
create page actions for this manual
coupling or manual synchronization that
we can that users from Business Central
can achieve.
Once we achieve those two, the next two
steps are basically creating table
mapping and field mapping for our
tables.
It is also important to know that those
two are are really new feature. I mean,
creating manually table mapping and
field mapping is a new feature inside
the Business Central. So, basically,
users can manually create add a new
table mappings. What they need actually
is this integration table.
And as I said that this integration
table is basically a Dataverse
representation in Business Central. That
means that we need to create this table,
and we won't do it manually. Idea is
because we have all of these standard
Dataverse fields that doesn't make sense
to do it manually. So, Microsoft come
there with a simple tool called
AL table proxy generator, which
basically helps us to create this AL
table.
Um this is part of the AL language
Visual Studio extension, and basically
inside the map there I will show you you
can find the EXE file, and you can just
run the script with parameters, and um
you will get the AL table file.
What is also important from version 13
of uh AL language, they introduced two
new parameters needed to run the script
and these are client ID and redirect URI
you URI.
Uh it is because uh
Microsoft removed the default enter
application from this tool
uh
with
the reason was security issues and now
what we need to do in order to use AL
table proxy generator, we need to create
our own enter application. I I will now
just show you how you can uh create a
custom table in AL with AL table proxy
generator and I already created an enter
application, so I won't
drive with that.
So, if I go to my
um PowerShell
I don't know if yeah, you can see it. Uh
the first thing we need to uh move
ourselves to
uh the
file folder where the AL table proxy
generator is located. So, basically as I
said, this is a part of AL language
extension and inside of this we have
this exit file.
Um idea will be then to just specify
parameters that we need. So, we will
just define
what is our project, what is our our PTA
extension.
Uh where are our AL packages, basically
where are our symbol stores. We need to
define uh dataverse
URL uh and what entity from dataverse we
want to connect to. As Erato said, we
have this business case for rental car,
so basically what we want to do, uh we
want to just achieve um our master data
vehicle to be able to be data synced.
And these two new parameters are just as
I said, client ID and redirect URI.
And once I run this command,
I will need to
authenticate myself.
I don't know how many of you actually
use this tool before.
Okay, quite some hands.
Uh
Then after I authenticate myself,
This is my
Contoso environment, so
doesn't matter for the password.
And of course, I need to
multi-factor authentication to enable.
Once we are ready,
we'll see that here
system is retrieving entity metadata,
and one file is created. So, basically,
when I go into my Visual Studio Code,
I will get here a new table. It is red
because I already have this table
created, so I will just delete it and
go
do another another one. Uh do you see my
Visual Studio Code good? Should I
enlarge it, maybe?
Maybe I can
a bit.
So, before I show a data sync from the
code perspective, I will just run you
quickly through the objects that we have
in our solution. So, basically, what we
have is the vehicle master data table,
where we store
all information about vehicle. This is a
vehicle type, make, model, etc.
Nothing special.
Another level of we have our transaction
data in into loan header and loan lines.
Basically, we want to create loan
orders.
Uh
there we will just create those orders.
They can be in different states. We will
show later when we will showing uh
Business Central business events in
Business Central how we can utilize
these uh states.
And then after the loans are returned,
we will just created a return loan
orders.
Okay. Now, let's go to Dataverse. As I
said, this is my
Dataverse representation
data Dataverse data representation
inside the Business Central.
What I did, I created a
page based on the table.
And also, I created a Dataverse code
unit where I will just run you quickly
through steps what we need to do.
So, first thing that we need to do here
is basically we need to define our
coupling for our tables. So, that means
that we will say when it comes to
coupling, we will just connect vehicle,
our standard table, to our Dataverse
vehicle table. Next step will be we want
to connect our custom page when it comes
our uh RM vehicle table
uh to to to Business Central to to
actions. So, we will just subscribe to
on look up CRM tables, and then we will
here just define that it uses our table.
Once we have that,
we need to enable deep linking between
Dataverse and Business Central uh table.
I I know that this is a a bit of code. I
will all of this code publish later on
my GitHub, so you will be able to check
it further deeper if you are interested.
And the Once we
enable deep linking, the last step is
for us to create actual table mapping
and field mapping. So, basically, we
will say map our vehicle table to this
Dataverse representation integration
table, and map them on vehicle ID and
use modified on to know
the changes. And here, we just defined
that what fields we actually wanted to
map.
Once we published our solution, I will
just go into my Business Central,
and I will go into my vehicles.
If I say
see here for example, the first vehicle
that I have is Ford C-Max and let's say
that we have a typo here, maybe it
should be called
like this.
If I go to my
And the next step what I will do is
basically I just want to run
synchronization. This is usually done
through bad jobs to job history. We
don't need to worry about this. I will
just now simply write manually.
Basically, I will say synchronize
and send data to dataverse.
And you see job in background was
started and I can
notice
that for some reason
record is not changed.
Let's see the
vehicle table in
dataverse.
Yeah.
Ah,
it is changed. You see Ford C-Max.
So, that was basically it how we can
connect the
data sync between master data. Now, we
will just move further and then after
we'll continue with
virtual tables and after the virtual
tables, I will show how we can connect
our transactional data with virtual
tables. So. Okay. Thank you, Milan.
In the end it it it was synced.
Usually, you need to just refresh once
more batch job
history of batch jobs and then you will
see that it is synced as well.
Okay. So, we have data sync enabled.
Data sync works bi-directionally, so we
can also show you that it will work from
one from dataverse to BC.
Next
way how we can integrate
uh
Central with Dataverse is using virtual
tables.
And uh virtual how virtual tables works,
they works based on the uh API tables or
or API pages and API calls.
Uh meaning that each time when you need
uh data from Business Central, Dataverse
will uh ask Business Central through
API, "Give me uh give me uh
give me data from your table."
Uh so
uh we'll see that we need to build API
pages so for
uh to com- to establish communication.
And then once we have data inside the
uh Dataverse, we can use them in Power
Apps or Power Pages.
What is very interesting is that uh
business events will respect business
logic behind uh uh that is built inside
the Business Central. So in our case, it
you will see that for example, we cannot
enter uh end mileage less than start
mileage because it will it is some uh
restriction or logic business logic
built inside the
uh Business Central uh by my developer.
And how this is
uh integrated in one uh in one uh uh
graph. So, we have Business Central
again on the one side
and we have API pages
uh inside the Business Central that are
uh that can be custom one or that can be
standard one developed by Microsoft.
Then, we have uh integration or API uh
API APIs and on the right side, we have
Dataverse.
To enable virtual tables and integration
between uh virtual tables and uh
Dataverse,
uh we need to have installed business uh
uh virtual tables application that will
be that will then be responsible for
communication between Business Central
and Dataverse.
And uh once we have this installed,
we'll see our data inside the business
inside the Dataverse.
Also, if you're using your custom APIs,
custom pages, you can you can plug them
and use them in Dataverse.
Also, what is very important to know
that data in this scenario is not stored
inside a Dataverse, so you will not
consume any storage inside the
Dataverse.
Uh also, from the latest releases, we
have some new things. This is synthetic
relationships
inside the
Dataverse, where you can link your
standard table in Dataverse that I that
is created by
Data Sync with several
virtual tables that are coming from
Business Central. In our case, we'll see
how we can link with synthetic relation
relationship vehicles with
vehicle with loan lines inside the
Dataverse.
And of course of course, now when we
have a theory, let's see how we can
enable virtual tables. A story is the
similar like with
Data Sync, so we need to go to assisted
setup and run Dataverse connection
setup, but this time you will select
that you want to enable virtual tables
and business events.
Once you enable it, you need to accept
as well terms and conditions.
Then choose your Dataverse environment.
In this case, it can be the same one
that you are using for for your Data
Sync.
Then you will sign in with your admin
account,
and then
of course, when you sign in, you will
need to install
this application that is responsible for
for connection between Business Central
and Dataverse.
Uh yep, I will go next.
Okay, install virtual table app. You
will find it under the
your environments that it is installed.
Once it it is installed, it will
provision several managed solution
responsible for
all whole setup between Business Central
and your Dataverse.
Okay, once this is done, you can refresh
your setup page and you'll be ready to
to use uh virtual tables.
Before you do this, of course, you need
to enable virtual tables inside the
inside the Business Central because it
is not enabled by by design.
So, this is the application that you
need to install. So, it is Business
Central virtual table app on the on the
store.
And it as I said, it will create several
solutions inside the Dataverse
environment.
And uh those all those solutions are
responsible for making Dataverse
integration works
uh with virtual tables. It will show you
also how how your custom APIs, custom
business events, standard business
events, as well as standard tables.
And it will support you as well uh for
all your setup inside the Dataverse.
And now uh I will go and show you this
inside the inside the BC.
Okay. So, if I go to my Dataverse
connection setup,
uh my virtual tables are here.
Uh I see that it is already that they
are already enabled. So, I did this uh
earlier.
And what I can find here is virtual
table app source app. If I open it, it
will uh open in my new tab
this table. It is already installed
and it's of course free.
Uh
virtual tables config
so you can see what uh how we are uh
connected uh to which environment and uh
uh which company.
Uh available virtual tables
so if I click on this, I will see what
are all API pages that we can use inside
uh and enable inside the Business
Central and represent their data inside
the Dataverse.
We see here that we have some fixed
assets, some standard from Microsoft,
and of course, we have something related
to our our business case.
So,
uh how you can enable it, you can just
select one and click enable.
Uh batch job will be scheduled and it
will automatically enable within few
seconds.
And also, what you can do is you can as
I said enable synthetic relationship,
but we will show you this this little
bit later.
Once uh you are uh you have uh virtual
tables connected and ready,
uh you'll find here under the solutions
managed,
all those solutions that I mentioned in
my slides.
So, uh those are the solutions built uh
provision automatically. So, for
example, if you go to Business Central
virtual tables,
and uh under custom API, you'll see our
business events here
uh as well. And of course, I can find my
uh custom business events as well.
Uh if I go
to tables and navigate to tables, I will
see my virtual virtual tables that are
exposed inside the environment.
Or if I navigate here to my apps,
I will find Business Central
configuration model-driven app.
Okay, where I can see as well uh all
available tables. So, the same screen as
I have in Business Central, I can also
uh
attack from from uh
from the Dataverse.
If I have some synthetic relationships,
I will find them here as well.
Configuration.
So, if I click on the configuration, I
can see what is my configuration. So,
same screen as in BC.
And of course, I have my companies here
as well.
Good. If I go back to configuration and
Business Central, you will find out here
uh
refresh business event action, which
will if you don't see your business
events or you did some modifications on
them, you will need to refresh this to
fetch new
uh new new business events changes.
And that was about,
uh
virtual tables demystified. And now,
Milan, Thanks, I will switch to you.
Uh
So, yeah. Now, let me explain how
virtual tables actually work. And before
I go to Visual Studio Code, it is really
simple what we need to do. Basically, we
will just create custom API pages. So,
idea is now to
connect this loan header and loan lines
that we have into our custom solution to
Dataverse. So, I will just quickly go to
my code and show you how I did it.
So,
I will just go to
my code here. And since we have header
and lines tables, what we will do,
basically, as I said, I will just create
a simple API page. I mean, this is
again, it is not that hard. We just need
to define all the parameters
when we
need it for API page, and then we will
export the fields that we need for our
solution later. So, basically, I
exported contact informations and also
some status and start date and end date.
The same thing I did also for loan
lines. So, basically, I created the same
thing for the loan line table.
Uh I also did uh
some I was just playing with with
virtual tables. So, what I did, I
created a
API page,
which is said loan orders. So,
basically, it is consists of loan header
and then loan lines. So, basically, what
I have, I have all of the data from
header, and then I just embedded my loan
lines at the end.
So, basically, maybe we won't need two
tables with maybe we can can have
everything with one table. Yeah, how we
just know
we will see in in the real case scenario
that this doesn't make sense because
if we have multiple lines,
system will not know how to create this
record in that in that table. So, if I
just move back to my data verse
and if I just search
loan order.
This is the one that I told you.
So, basically, what will system do? It
will just ignore all of the lines part
and it will just use the loan header.
And this is really good example why all
of the not all of the API pages are good
idea for virtual tables. So, because of
that, Microsoft by default disabled all
APIs and then if you need any of these
as virtual tables, you will just enable
it as Renato showed.
So, basically,
uh now when I showed you
uh loan
line or loan header, if I come for
example to
Business Central and go to my loan
order.
And if I change
I don't know any data, let's say.
What what will happen
here if I will just
go back
to
loan
and if I open the loan header,
you will notice that
data will be changed. And the reason is
what happened in the background,
basically, this virtual table app from
AppSource that Renato display
explain basically send the request from
data verse to get the all of the
data or all of the new data from
Business Central.
So, if I just switch,
right, you will see that end date is
changed. If I move it back to the I
don't know, 19,
and if I go back,
you will notice here that if I open it
again,
it is 19.
Because API pages are
APIs doing the changes in the
background.
And that was it from my part of the API
and virtual tables. Now Renato will be
able to play a bit with synthetic
relationship, a new feature from
Microsoft.
Okay.
Yes, so now we have two demos to go. One
is the synthetic relationship and then
second one is the how we can build some
Power Apps applications based on the
virtual tables.
And as I said, to start playing with
synthetic relationships,
we go to Dataverse connection setup.
And here under the synthetic relations,
I will see that I already created one
relationship between
my
vehicle table and Dataverse Dataverse
table.
If I want to create a new one, I'll
click new.
I'll click native Dataverse table. So,
this is the table that exists inside the
Dataverse that uh
uh that I want to use.
So, let's say that let's try if account
will work or contact. And the virtual
table is the one that is representing
that is virtual table inside the
Dataverse.
And this doesn't need to be your contact
table. It can be any table that is
connected somehow with your contacts.
Uh in our case, we have on loan header,
we have information about uh about
uh contact, and I will click then next.
Okay, on how many fields you want to
connect? So, I will say one field.
And then okay, please choose the CRM
table.
And now uh the thing is that you need to
connect uh your uh
uh number from from your field from the
CRM table with our Dataverse with field
uh from BC. And we see that here we
don't have a field NO that is usually
used uh
uh to map. So, I will just cancel and uh
return back and I will try to show you
our connection
that I already built.
So, here I can see that I have my native
entity, which is my master data in this
case, vehicle.
Uh
okay, sorry. Uh I have my loan order
line.
So, this is the virtual entity. And I
see that I have a field from my vehicle
table, number, and vehicle number is in
my lines.
So, this is the very easy and simple
synthetic relationship between vehicle
and loan order line.
Okay. Uh what this means now when when
it's uh available, if I go back to uh
Power Apps,
and if I click on apps,
I'll create a new app.
Let me see here.
And then,
vehicles.
Wherever it is.
Uh tables.
Uh vehicle.
Okay. I will open my table.
I'll create a new application.
Uh BC Tech Days
24.
In a few seconds, I will get my
Dataverse table uh Dataverse uh
mobile-driven uh model model-driven
application based on my uh
table vehicle, which is normal table
inside the
dataverse.
Okay.
Let's see the data soon.
Okay, if I go back here.
Okay.
If I now play with it,
if I run the that application,
okay, I see my my vehicles.
And for example, if I go to this one, I
see information about my vehicle.
But here in the related, you will now
see that I have data from my loan order
lines. So, this is my synthetic
relationship.
And if I click on a loan order line,
I will see that I have
all
I will see that I have my loan
information from my loan document. If I
click If I open it,
again,
I can see that I have my details about
my order lines. So, because my vehicle
is part of my loan lines.
And then I hear I can have here whatever
I can I want. I can play. I can edit
data and and so on.
So, that is the synthetic relationship.
And
yeah, we have our application that is
built on top of real dataverse table.
But now I will go back and build one
application that is on top of virtual
table.
And I will go back to my tables all and
then I find loan.
Loan order line.
Okay, and I will create an app
immediately.
Uh
Wait.
Done. For example,
because I want to register when someone
is returning my car uh car from the from
the rental car that uh what is the
mileage and and so on.
Uh okay. If I play,
I will see my uh loan order lines.
Uh I have this one where I have my car
uh Peugeot. And then I see that I have
some start mileage that uh that is now
uh that was uh brought from my master
data. And then I for example can enter
here uh some number. For example,
if I what I
told you before, if I try to save this,
I will see and I receive an error.
Meaning that uh Business Central and
Dataverse and uh model-driven app will
respect what is going on uh with
business logic inside the Business
Central.
This is also applicable for uh
drop-downs or uh look-up fields. So, if
you try to
for example, in fixed asset, you have a
responsible person as a as a person. If
you try to assign some fixed asset to
person that doesn't exist inside the
Business Central, you'll as well receive
an error an error inside the inside the
model-driven app.
But, if I put something uh normal, so 19
thousand
and I save and close,
uh things should work. And now if I
navigate to my BC,
uh loan orders,
this one.
Yeah, it's automatically updated.
So, that is the application based on the
virtual tables.
And now we'll continue with
business events.
Uh
thanks, Renato. And I usually say about
business events that they are webhooks
on steroids. So, how many of you
actually worked with webhooks in
Business Central?
Few hands I see only. Okay, then it will
be fun to see to tell a few more things
about webhooks. So, just for you to get
a feeling what they are and how why the
business events are more powerful than
webhooks.
So, basically, if you go a bit even
further
in the past,
the time when we don't have
when we didn't have webhooks and we
wanted to connect two systems. So, for
example, we have Business Central and we
have external system and we wanted to
sync data, for example. So, external
system will need to every now and then
to send a request to Business Central
asking, "Did data change? Did data
change? Did data change?" And then,
after some time, Business Central will
actually reply, "Okay, this record is
changed." Or data changed. And then
again, it will go again and again and
again.
And you can see this is not very
efficient, especially if we have a
multiple external system picking our our
system.
Then, with webhooks, what actually
happened, basically, this is a mechanism
for
in Business Central or in any other
solution to notify external system about
some data changes. So, basically, that
means instead of polling the Business
Central, Business Central will just send
a push notification to external system.
So, basically, it will just come and
say, "This data is changed."
And also, this is very scalable. So, if
multiple systems want to connect to
Business Central, Business Central will
just send notification everywhere.
So, in order to see how these webhooks
actually working, basically, they are
based on subscription. So, that means
that external system need to subscribe
on specific resource in Business Central
to get notification about. When I said
specific research, that means specific
web
specific API page.
And when we send this subscription
request, what will happen basically,
Business Central will try to achieve
handshake mechanism. That means it will
try to reply back to the external system
with a new
request
passing by validation token and
expecting it to get it back. Why it is
working like that? Basically, Business
Central just wanted to ensure that
external system actually listening for
the changes.
And also what is also important here to
know is that
once we establish subscription, it will
last for 3 days.
That means that every 3 days we need to
refresh our subscription. In other
words, this external system needs to
have some solution, whether it will be
some cron jobs or whatever, that will
every 3 days ping and send the request
to refresh the subscription.
And as you can see, this uh
business webhooks are based on every
data change. So, that means that once
data is changed, we will just notify the
external system. If we go a bit deep
down to see how this is actually
working inside the Business Central,
once the Business Central establish
external system establish subscription
with Business Central, what will happen
basically in the system table API
webhook subscription record will be
created.
That means that
similar as a change log functionality,
it will watch for any on insert, on
modify, on delete global triggers
changes. And once any change occurs,
system will adjust uh
record it in in inside the another
system table called API webhook
notification, which will then fire the
background
job. Basically, the task scheduler will
be created a task to
uh dispatch this notification to
external system. And this is this
standard uh
code unit respond responsible for that.
So, now I will just go into my uh
code and I will try try to show you how
web hooks works actually in in real
example.
So, as I said, uh this external system
that doesn't mean to be Dataverse that
that can be any system. So, basically,
it can be Azure function, uh web
application, or whatever. In our case, I
just created a simple Azure function
that I deployed and it will act as
external system which will listen for
any changes in Business Central.
So, basically, if I go to my Visual
Studio,
what this Azure function do, basically,
nothing special.
Uh what I have first, as I said, I need
I need to be able to perform handshake
mechanism. So, if Business Central send
me validation token, I will just return
back this validation token
um saying, "Okay, I make sure you're
listening."
And then, when any change occurs, I will
not do any special anything special, I
will just log that information just to
see that something changed.
Okay. Now, once we have our uh external
system, which is our
Azure function, I will just go quickly
to
uh my Azure portal
and I will open the
log stream here.
Okay.
I'm connected. So,
now
I will just go in the Postman and from
Postman, I will try to um subscribe to
specific uh web hook and then I will try
to check track changes.
If as I said
it works similar as change log, meaning
every change that happens it will notify
the system. But what if example external
system is not not interested in changes
about all changes, it is interested for
example if sales order is released. So
basically they want to know any
only when sales order is released. So
let's create then this example. So what
I will do
I will create a post request to
my subscriptions. And this is basically
a p call for creating a subscription.
What I need to put inside my body it is
basically pretty simple. I need to
define notification URL. This is
basically my Azure function, and I need
to define which resource I want to
connect to.
Also, there is additional thing that can
be sent here, and this is called a
client state. Basically client state is
a
I would say I would
like shared secret. Basically since this
Azure function or any other external
system accept anonymous calls, so
basically anyone can send a request
there. With client state we are somehow
ensuring that we will accept only the
these
calls with these. So basically if I
define the
let's say BC Tech Days
uh client state here, then in my Azure
function I can add a logic is saying if
client state is different, I will just
not accept this is someone trying else
trying to send me notification.
Uh in my demo I I will create it without
client state, and I will just post the
request.
Once I did this, basically I got my uh
response that uh web hook subscription
is created and what you can notice here
that
uh
expiration date time is a three three
days from now. It is 16th of June.
Uh this time is basically this is UTC
time zone.
Once I created this uh subscription to
sales order and let's say
users come to the
sales orders
and they want to change something there.
I don't know.
They want to change
reference for example and I will put
here reference to be busy text this
again.
You see, we are not interested in this.
We are only interested whether sales
order is released or not.
But still somehow web I mean webhooks
are not that smart so we cannot decide
what we want to what changes we want to
check. Basically it will check all the
changes. So if
I come back to the
logs, now I need to wait at least I
would say a half of minute to get the
notifications to so Business Central to
process this webhook. So I can just
wait for it. You can see here this was
our initial subscription subscription
request and now we got our
uh
notification.
If I use this notification, I will just
copy it
and put it here into this
JSON
pretty file tool. So basically you can
notice that
I didn't get any notification what field
was changed. I only get re- resource
that was changed basically saying,
"Okay, this resource was changed." And I
get the change type. So that means that
external system still needs to send the
request to the Business Central tracking
what was actually changed.
Now,
if we move uh
back to
Business Central
or presentation,
uh and if we move to business events,
basically business events are not
tracking any change that are occurring
in Business Central. They are just
mechanism of notifying external system
when some specific actions are occurred.
So, basically, I don't know,
this uh demo for releasing the order was
example uh when Business Events are
really good to use because
what will happen uh after the
transaction is done in Business Central,
we will just notify the external system,
okay, order is actually released, and we
will not care about any other changes.
Because
all of these business case that we
talked today was connecting Business
Central with Dataverse. And of course,
we can connect the business events with
Dataverse as well. Renato will show
later in Power Automate how how you can
create flows there. But what also also
we can do, we can create uh connect
Business Central with any other external
system through business events.
How business events
look like, so basically, they are also
based on subscription model like
webhooks. The only difference here is
that
subscription will not expire. So, that
means we don't need to every 3 days to
refresh the subscription, and also no
handshake is needed. So, basically, once
we subscribe, external system don't need
to worry about performing handshake.
And as I said, uh this uh business
events are really good tool for
processing notification.
Uh
when we talk about standard business
events, Microsoft introduced this uh two
two versions ago. It's a part of AL app
extension repository where basically
what they did uh
they created a custom external events
app. You will notice in the system that
Microsoft wasn't consistent here. So, in
one place they are calling it external
events, on other another place it
calling it calls it uh
business events and somewhere they also
call it external business events. So,
we'll just call it business events here.
And
they group all of these standard
business events into five different
categories. So, basically
I will show later in the code. You will
see this is nothing else but just the
different inner values. And basically we
have different events in account
payable, accounts receivable, sales,
purchasing, and for opportunities. So,
basically we don't need to create our
custom business event for sales order
releasing. We just can connect to
standard one.
And now I will just quickly show you how
we can extend the and create our custom
business events and how also we can
connect those to external systems.
So,
what I will do firstly, I will go just
in my code and I will show you
our case. So, basically in our loan
orders we have two actions. We can loan
our loan loan order can go into loan
state or after someone returns the
vehicles, we will just put it into
return state. So, what we are
interested, we just wanted to have
business events when order is loan and
when order is basically returned. So,
how we create a business events?
It is very simple as that. First, what
we need to do is we need to extend the
event category
uh enum where we will add our own
category and we will call it loan.
Then
into
business event, as I said, we will
create vehicle return and vehicle loan
business event. It is pretty simple. As
I said, Microsoft is not consistent, so
here it's called external business
event.
And we will say what is the name, what
is the display name of this business
event, and in which category they is.
And also we will define the version.
Idea is that
we shouldn't change the business event
if we want to
I I I don't know, create additional
parameter. Idea is to just obsolete the
standard
existing one and to add a new version or
or new version of the business event.
Because we don't want to break existing
integrations.
In In our case,
um we wanted just to send as much
information as needed for the layout, so
later then he don't need to get get
again the records from Business Central.
All the information that we need we will
just send to him.
So as any other event,
those two events are simple used like
that. And then into our subscribers, we
just
subscribe to on after return and on
after loan vehicle.
What is important to know with business
event, so basically they are sent
once transaction is done. So basically
if there are five events
fired inside one transaction, they will
be just
put together and sent as one
notification to external system. And you
will see that also in
in the code.
Now, once I have uh
business event, let's create a
subscription.
So I will go again back in the
Postman.
At what I will do basically
I will
first
there is
I will show you that there is available
business events. So basically we have a
endpoint where we can get all of the
external business events that are
available.
So if I
send this request
you will notice all of these standard
ones and also our custom business
events. What is important to know
you will see when we are say creating
subscription for business events, we
also need to pass this parameter app ID
of
where
business event is actually created. So
this app ID is important for us and also
in payload we can see all of the
parameters, all of data that will
business events throw to us.
So if I go to my post business event
subscription in the body as I said we
need to put
app ID, we need to put uh
sales order released in this case and we
need to put notification URL.
As um
this azure function that I created for
webhook it will also act as our external
system that we are connecting to. But
instead of using sales order released I
will connect to loan order so
for basically for vehicle loan. So what
I need to copy I need to copy vehicle
loan
and I need to copy app ID.
I will just here
put it.
And I will send the request.
And you will see that our
uh subscription is created.
So that means that every time when we
actually go to our loan orders, I'll go
now.
And let's say we have this loan
which has
two vehicles here. So basically in our
code basically two business events will
be fired. But that won't be two
different
events sent to notification URL, it will
be only one bundle together. And this is
how system works. And we have to show
you later in Power Automate. I'm not
sure whether it is by design or it is
bug in Power Automate, but Power
Automate flow will be triggered twice in
this scenario. And that is not basically
the thing that we looked for.
So if I come here and if I put my status
to loan
and if I go back to the
Azure function logs,
we should be able to see business event
here.
Sometimes and
in in last few days
once we tested these business events,
sometimes they they occurred to not be
that stable. They are still in preview,
so they usually works good, but
sometimes it could happen that they are
not not that stable.
Okay.
So
for some reason
business event wasn't fired. I will just
check.
Okay, I see.
There is additional step that we need to
create. Basically
this event version that I said, if you
don't specify them, it will by default
put the empty event version. And the
event that I created in my code, it is
basically with even even version one.
And the one that I created subscription
is empty. So, what I need to create
here,
I need to basically create a
subscription to
event event version
one.
Type event.
Uh okay. Thanks.
So, yeah, you can see we created a
new new event subscription with a
correct version. So, now if I go
making business central also, and if
I will just
reopen
and loan again.
And now if I go back,
you see there is the business event was
fired. So, now as I said, it is fired
once, not two times. And basically, if I
copy this again here,
you will notice that I have two lines
actually changed. And you can see with a
business event, I can pass by as much
information as I want. So, basically in
my payload, I send document
contact information, also what is
vehicle number, name, and document ID.
And this is really
the real power of these business events.
What is also
interesting, if you are interested
about subscriptions in business events,
so out of the box, you can see here
in the inside the business central those
standard pages. So, basically, I will
create a
I will open just business event
subscription.
And you can see here all of the systems
that are connected to something. So,
basically, all of these systems are
connected to vehicle loan here. Also,
you can notice here activity log,
basically stating whether subscription
was created or here if in this case, you
can see
that
successfully sent notification. And we
have it two times because we have two
lines, but it is bundled as S1.
And with that, I will pass by pass uh
back to Renato. He will continue and
show you how you can use these business
events in Power Automate. Okay.
Thank you, Milan.
Uh very nice and very powerful,
actually. I really like those
uh new business events inside the
Business Central because it also opens a
lot of uh possibility for for me as a
consultant to build some powerful
automation.
Uh as it says, so business events will
enable us to have outbound integration
with Power Platform
and to trigger Power Automate flow
uh based on the Business Central
connector, or I can utilize as well uh
Dataverse connector and uh trigger that
is called when an action is performed.
So, there I will also find my business
events from the Business Central.
Uh once I have data inside the
Power Automate flow, I can do whatever I
want uh with it. And it's very important
that you agree with your colleagues
developer what kind of data he wants to
uh give to you and what kind of data you
need uh for that so you don't need, for
example, to once the business event is
triggered,
that you need again to go call another
API to get data from the Business
Central database.
Uh as I said, we have two triggers. One
is uh a Business Central connection and
connector, which is still in preview, so
when a when a business event occur,
uh and another one that is not in
preview is Dataverse standard Dataverse
connector uh when an action is
performed.
And now, uh I would like to show you
this, how this works on a several demos
uh which I prepared for
this presentation.
Uh
okay. So, if I go to Power Automate
flow,
uh
I will go here first. We have some
standard Milan said that we have some
standard business events.
And I will open one of the flows that I
built earlier.
Okay, and what this flow is doing, he's
listening my business events, then
getting adaptive card from the Business
Central, and posting that card into
Microsoft Teams for channel.
Okay, what I have here. So, I need to
specify my environment.
What is my event? So, what is my
business event?
Like this. So, I see some standard when
customer is blocked. So, Microsoft think
that this is very useful.
Or I can see also
when vehicle is loaned or when vehicle
is returned. Business events that Milan
developed for our business case.
Uh
okay, I have them here. I used purchase
order released. So, when purchase order
receives status released, either after
approval or if you don't use approval,
we want to post some message.
Uh
okay, I'm getting adaptive card
from that
uh
from that, and then I'm posting this
into my Teams. So, very simple very
simple flow that that will work. Uh
okay, so this is something based on the
standard.
Uh but, if I have my custom
Uh I have it here. This is my first
example.
What I want to do and what I want to
achieve, we said, "Okay, when we loaning
our or issuing our card to contact, we
want to also have some notification
inside the Teams in this case. So, I'm
using again my vehicle loan
business event.
Okay, and then if I go here, I need to
specify to get URL of my
of my uh
record. I need to specify what is my
page of
for that
loan. And of course, I need to specify
document ID.
Uh for which I'm getting. If I take a
look, I will see all the fields here
that Milan developed
inside the business event. So, document
number, contact number, and so on. So,
you can combine in one business event
data from header and from the lines.
Okay, I have this get URL and then I'm
posting some adaptive card inside the
uh channel that I created.
So, uh
this adaptive card JSON is something
that I uh created manually here in
adaptive card designer. So, where you
can select Microsoft Teams, what is the
target version, and then you can
uh design your adaptive card for your
needs.
Uh okay, so I passed information from my
from my trigger. So, this is my trigger
here, all the data about trigger and as
well here.
Okay, what is now happening
if I turn this on?
Uh I will turn on
my flow. Okay.
And let's now go to Business Central.
And I have loan orders, and I have this
one, right?
Okay, and if I say okay, I want to loan
it.
Okay.
We have status has been changed.
And let's see if our flow will run
successfully.
Okay,
3 seconds ago, yeah, it succeed. Okay,
Uh if I navigate to my teams, demo test,
I will see my
uh information from my Business Central
and data that was passed from my
uh from my uh
business event.
Uh of course, I can now click here on
view.
And it will open as well as any other
adaptive card that you can use with uh
Business Central data.
So, very easily you can uh track uh
statuses of your documents and and so
on.
Uh another example that I would like to
show you and how you can combine Power
Automate with whole uh Business Central
uh scenario is uh
returns. So, we said in our business
case that once we return our vehicle, we
want to say send a thank you thank you
note uh to our to our customer.
Uh so, I have this loan order.
And I have one Power Automate return
vehicle.
What I have here
if I open it.
Here, I'm using something different and
some another trigger. Uh so, which is
manual trigger. So, when uh first
selected record inside the Business
Central.
Then, I'm getting
uh information about my record that is
selected inside the Business Central. In
this case, it is the loan order
uh page table. And I'm getting the
information about system ID.
I'm sending an email to my contact,
which is contact email, which I have on
my header.
And then, I'm running some action inside
the
uh
inside the Business Central using Power
Automate.
So, and I will run the action return
vehicle.
Uh
okay. If I turn this on again.
Okay.
Come on.
Turn on.
Okay, it is on. Perfect. And now, if I
go to my loan orders,
and I click on this
document,
and I click actions, automate,
in a few seconds, you will see here
return order power automate.
Uh okay, I will just click
click on it.
Again, in a few seconds, I will get a
side pane
uh for my uh flow. Here, I can also add
some inputs. So, for example, I will
attach uh invoice and I all I will
attach some uh some another documents
for that I was going to send to my user,
uh to my contact. When I click run, it
will succeed and in a few seconds,
I should get an email. Hopefully, here,
yes.
In my case, uh yeah, thank you for
working with us and details about my
from my action that uh me and creator.
Okay, uh I was also
uh
I have possibility also to achieve this
with business events, right? So, what
I'm going to do in this case, I will
just listen when my loan order is
changed status to returned, trigger
trigger uh business event inside the
power automate.
Uh
okay.
Uh this is uh
those are the business events with power
automate and now we are going to switch
to
telemetry.
Thanks, Renato.
And of course, everyone is talking about
telemetry and last few years at every
conference, there is at least one top
one session about telemetry. So, I won't
talk much in general about telemetry. I
will assume that all of you already
knows what that is and that you are
using it much. So, I will just focus on
telemetry for business events. So, if we
talk about telemetry for business
events, we basically have four different
event IDs that we can check. So,
basically, we can check whether business
event subscription is created,
whether this subscription is deleted,
and then we also can check did event
trigger success- successfully or not,
whether it is failed to send.
And now, I will just quickly go, since
we are running out of time, I will just
quickly go to the
our application insights, and I will try
to run each of these event IDs, so for
you just to see what information we can
get there.
So,
I will switch to my
application insights here, and I will
just run
traces
where our custom dimension, okay, this
custom dimension's
event ID is
equal, let's say, firstly,
40.
So, basically, this is all of the
subscriptions that are created
successfully in last 24 hours.
If we open any of these,
inside the custom dimensions, we will
see a
interesting data, actually, useful data.
I don't know
Okay, I think you can see it.
Uh
I'll do like this. So, what we can see
inside the custom dimensions, what is
relevant, we can see what event name,
basically, what is the business event
that someone subscribed to, what is the
version of the event, and the
the most useful information, what is
basically this external system that is
subscribing to our business event.
Similar, we can check
for business events
that are cancelled subscription.
So, as I said, uh here subscription will
not be automatically cancelled. It will
not expire after 3 days. So, if you are
not interested anymore in this business
event, you need to do it manually. So,
again, here you can see all of these
similar information. Again, we can see
business event name and we can see which
external system was uh
the
unsubscribed from it.
And the the one which should be useful
and it turns that it is not that much is
basically which business events are
triggered. So, here we can see every
occurrence of these triggered business
events, but there there aren't any
actual much of the information needed
here. So, what we only can see here, we
can see what is the business event that
occurred, but we don't have idea to
which external system a basically data
is sent.
And with this, I will
stop with telemetry. I will say that if
you are maybe interested in telemetry
for virtual tables, you can maybe see
API calls that are sent, web service
calls that are sent from the Business
Central. So, you can check what what
Business Central um virtual tables are
used. Or also, if you are using
synthetic relationship, this is a new
feature from Microsoft. For that feature
is enabled feature telemetry, so you can
also check check it inside the
telemetry.
And before we finish for today, I will
just
will just say a few key takeaways.
So,
yeah.
Okay, so yeah,
uh
we we came at the to the end of the hard
session.
And yeah, the key takeaways uh so, we
have several possibility to integrate
Business Central and Dataverse.
And it all depends on the business case
that you want to that you have and then
how you want to build it. Uh we have
data sync that replicates data from the
Business Central to the Dataverse. It
works via batch jobs. So uh this is a
those are the details about data sync.
Virtual tables on another hand, they
work through APIs and they are querying
your
uh Business Central. They are not
storing data inside the Dataverse. And
as well they are Oh, sorry. Uh
respecting the business logic that was
uh that was built inside the Business
Central. Yeah. And if you are you are
connecting uh checking for changes
inside the Business Central, there are
two ways, either through web hooks or
through business events. What is really
important to know about web hooks, it
will check any change that happens and
you will not get actually information
what has changed. You need to send
additional request. When we are talking
about business events, they are
basically system for notifying some
process changes. And of course, you can
use telemetry to check how the systems
are performing on all of these uh
features.
And with this
we are open for your questions now and
the fun part starts because I want to
try to throw it. Okay.
Interesting session but and I have
multiple questions here. May- maybe I
ask one. Yeah, okay.
Okay, is there any security issues you
have to consider when using the virtual
tables and the and the connectors?
Do you have to protect the data and how
how GDPR is taken into account and When
we are connecting with Sorry, I didn't
hear the complete
Is there any security issues you have to
Security issues with connecting to
Dataverse, for example. And how do you
protect your data?
So basically, since this is all of on
cloud on Microsoft cloud, this is
basically responsibility from Microsoft
and we are believing that they will
protect everything. And it's in the same
subscription that the
the Business Central is in. So for
example, if I'm in North Europe and then
in Okay, so that way you have this
client state that I said basically with
client state you can create this shared
secret I would say and with this you
will protect that not anyone can send
the request to you. It will be only the
one who know the client state. Okay. So
I think you I will ask the rest of the
questions.
Yeah, yeah, of course. We will be here
until tomorrow.
Uh maybe you can pass it.
Uh
Um you show Hello. You show that we can
use web hooks to uh
So from events from Business Central, is
there any way uh to do this the other
way around?
Like if So Business Central, yeah, of
course. The Business Central can we can
implement some integration like with the
APIs with web service where we'll just
Yeah.
be the one
listening. But we cannot subscribe like
to web hooks or something or or what how
would you do this?
So if we have web hook, so you want I
have an external system and I don't want
to
uh pull from the system constantly like
we would have to do without web hooks,
but I want to be able to get a
notification and then process this in
Business Central. Okay, so in other way
around that that means that we can
expose the system and just someone can
send us the request in Business Central.
You so we can expose the API and if
something is changed, someone can just
call us and say, "Okay, this has
changed."
If I correct you.
We have one there, I think so. No, or is
this for you?
Yeah.
Hello, it's such a moment.
Great great presentation. Thank you
Renato and Milan. Uh
today um
we see
um many services and integrations, uh
but uh what about the license uh Example
of business events,
do you need extra license for this part?
That is matter for licenses, but in part
from the Business Central perspective,
you don't need any extra licenses. Only
maybe if you are connected with Power
Automate, but I also think it comes
Maybe Power Automate license.
Yeah. Okay. Okay, thank you. Uh maybe
you can pass it.
You know, pass it.
Last one.
What I'm wondering here uh we're going
to do a lot with APIs
in the future, aren't we running into
limits?
in in the number of API requests we can
do?
Yeah, it depends if you're talking about
the there are some limits and on
Business Central and Microsoft keeps
just
putting these limits to be more and
more. So, basically, these limits are
currently pretty high, so if
I don't know
in the in from my head, but I know that
they move from environment to user
perspective of limits, so they are
limiting how many requests you can send
by intra app, not on complete
environment. So, I think these limits
are pretty high currently.
So, okay, can you
And this is
Sorry.
Uh okay, I have one question. Uh so, you
showed how when we use virtual tables
and we put some data in uh
um Power App,
the the triggers from Business Central
are executed.
Uh is it the same case if if we use
integration tables?
So, if we integrate two tables,
one in Dataverse and one in Business
Central, if we start
populating the data in Power App,
Okay. does it execute the for For on
validate or on insert Yes, it will in
But you will get this information in
Business Central. You will not get it in
the power in the Power App.
Uh, sorry? You will get this information
about failed synchronization inside the
Business Central.
Aha. Yes.
So,
I will be able to create, for example,
vehicle in Dataverse, but it will be not
synced with the vehicle in
Business Central.
Exactly. Okay, thanks.
Thanks.
Okay.
I have two questions. First, you.
Yeah. Um, is it possible to in business
event send complicated
types like XML document, JSON object, or
record? No, basically,
you have limitation. You can you can
maybe deserialize JSON object and send
this like a text, but you cannot send a
record or some
more complex data types.
Thanks.
Yeah.
You are so far away. I will not show it.
Thank you. My question is Oh, sorry.
Sorry.
Okay, my question is regarding the data
synchronization with data
happen. Is how reliable is it when we
use transactional data like sales
invoices transaction couple per minute
on the Power Apps and we need to
ship it directly to Business Central.
Can we use it with this level of of
data? Yeah, you can use it, but it again
it depends how often this data
will change, how many data will be
there. So, I will definitely maybe
propose to use better virtual tables for
that instead of
data sync and then use data sync maybe
for master data. Also, with virtual
tables you will have data in one place.
It won't be duplicated, I would say. I
think it's job queue based, right?
Yeah, yeah, it's job queue So,
basically, job queues are in the
background.
Thanks.
More questions?
Um one one more question.
you don't have any shirts. You got only
one, so we don't have a second one. No,
no, it's okay.
But
one more question about the
localizations. You said that
you can get the data for the option
fields and stuff like that. And what
happens if you have have your Power Apps
English and your Business Central is
Finnish? Okay, so basically you can map
those options. So there there is a way
we didn't show it, but you can map. So
basically you know
to to to map it to correct one. So
basically if you
if on English is yes, on Spanish is see,
you you can
map it or define how to between those
two. If you're asking me like But you
have to you have to translate them
yourself.
There's no loose coupling. Aha, but
options are I'm talking about options
values.
Basically option values will be some
integers in the background. So you will
just need to sync integers to be synced.
Okay. So you don't need to worry about
translation.
In in Power Apps option, it's called
choice.
Uh you need to define external external
uh
external number that will then represent
in Business Central and then you will
sync option set, right? Items. And then
you will write your
translations inside Power Apps.
Yeah.
So my question is uh related with uh
field mapping. So I have a situation
where uh
I am upgrading our code from C/AL to AL.
And the old version is BC 14. So we have
a few fields in
under the 50,000 range. And I am moving
the fields from 50,000
from to the 50,000 range because of that
is allowed. So when I am mapping the
fields, so I'm not able to synchronize
the field because so in the legacy
system old system the field ID is
different and in the new system I added
the fields in 50,000 range. Okay.
In that case, how can I map the fields
with the new Yeah, you can you you can
map. So, basically
so basically you can
define
the No, in BC 24 is available, but in
the previous
Yeah, yeah, I know it is not available
in the
Yeah, yeah,
this is only for from BC So,
BC 23 or the previous version You will
need to do it basically in the code. If
you want to extend the functionality,
you cannot do it manually in the in the
client. So, but from the code you you
will be able to extend.
Uh
Do we have
questions?
Okay, if there is no more questions, we
will be here today and tomorrow. So,
just stop by and ask.
Thanks.
