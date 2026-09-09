# NAV TechDays 2016: The Power of Power BI and Dynamics NAV

- **Source:** https://www.youtube.com/watch?v=srGwTDIp7Hc
- **Video ID:** srGwTDIp7Hc
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 94m43s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

Hello and welcome this Friday afternoon
on this last session about uh PowerBI.
Uh and look when Luke asked me to uh
prepare for this session he told me
actually PowerBI is a whole topic we
should do something about that and I got
started to think well what should I tell
actually about PowerBI because there was
so much to tell. So I had the idea that
okay let's go over the tool set
together. Let's see which tools we have
available out there how we can use them
and hopefully after the session you
should have a good idea on which tool
might be the best uh for for you or for
your
company. So let's get started with an
overview. And if you look at powerbi.com
if you go to the website we talk about
the selfservice revolution. It means
that you can make use of the PowerBI
tool set for everybody in your
organization without having to be a
rocket scientist uh to get started. And
that's a very big shift between how it
was in the past and how it is right now.
In the past, we need to create these
expensive data warehouses and cubes and
it took years before they were ready.
Then if you needed to make a change, it
took even longer. Now with the PowerBI
tool stack, we are ready to do it all
ourself. We have a rich set of reports,
a tool set that we can use. We can
distribute them along in the
organization. You can access them via
web browser. You can access them on your
mobile uh
device. So, okay, if you get started,
you might be interested to connect to a
number of data sources and I try to
collect a couple of them here on uh on
the slide and about every month, new
data sources are being added to the
PowerBI tool stack. So, if you use one
of the products, these are actually data
sources you can use. you can connect to
directly uh if your data source isn't on
here. Of course, you can also create a
different kind of of a connection. So
you can connect to whatever matters to
you. We can do this with the PowerBI
tool stack, but of course also Power
Apps and and and
Flow. So the self-service revolution
means that you will create PowerBI
reports or reports. You can start for
example using the PowerBI desktop. You
can start from Excel where you develop
your reports and then to distribute them
to your users and you can make use of
the PowerBI service which is actually
PowerBI.com the website where you can
upload uh your uh reports. Certain
reports require a connection to a
database which might be on premise. It
might be for example an AV database on
SQL server. It might be a cube might be
something else. And to be able to
harvest that data you can install and
configure the gateway. There are two
versions of of the gateway. One is
actually meant for PowerBI and the other
one is also meant so you can access the
same data sources using Power Apps and
and Flow. If you have time enough today,
I might also demo on how to get that
working. So once we have all reports in
the cloud, we can access them. We can
share them depending on depending on uh
the accounts you have on PowerBI.com,
the free the free version, the paying
version, you can store more or less
data. You can refresh more or less
frequently. Now this is the architecture
at the moment but in the future it might
also become an extra possibility it
might become available to do everything
uh on premise. Uh I have heard and read
that with the next release of SQL server
or one of the upcoming service packs it
might also become possible to host and
execute our PowerBI reports instead on
the PowerBI service within reporting
services for example in the uh report
manager. So then we will also have a
complete onremise
solution. So we have a lot of tools and
that we can we can use. We have our data
might be on premise. It might be in the
cloud. We need to start to build a data
model. Then we need to analyze and order
our data model. And then we need to
figure out a way and how to deliver all
of that information and how to consume
it. You have a lot of of
possibilities. Now first let me start
with a question. The one I always start
with when I also deliver PowerBI or
reporting or any kind of BI training. A
question is always what is BI? BI means
something else depending on on who you
are and actually BI is an umbrella term.
It means that we should implement some
kind of software or practice that should
lead to better insights and decisions.
That's actually the most important
should know what you do and how you do
it uh and how to create it. And the idea
is to visualize facts to our end users.
Facts coming from our enterprise
applications. We can make use of data
warehouses cubes. Typically in the past
the cube was where the single version of
the truth was was held but in real life
actually users prefer to work with
Excel. So in the past we had kind of a
contradiction between the very
intelligent IT people partners
developers creating these warehouses and
users wanting to make use of them in in
Excel. Well PowerBI know we have a
solution uh that can actually satisfy
both types of
usages. So when you will start to build
your own we reports hopefully after this
session what you are going to do is go
in circles you'll start by connecting uh
what matters to you can connect
information from one or multiple data
sources I will show you a couple of
examples the sky is the limit using our
powerbi tools we can bring your reports
to life we have a solution for the whole
organization and we can visualize and
analyze and even predict the future with
every new version of PowerBI, new
features have been added and in the
latest version of the PowerBI desktop
tool and we can even uh do some
predictive analysis based on the data
sets that we provide to certain
visuals. Now can be a difficult uh road
to travel in or if you travel in the
PowerBI forest you will notice lots of
trees and the first choice you will need
to make is what am I going to use and I
try to divide all the different trees or
tools on two slides. On the first slide,
we will see power query, power private,
power review, and power map, which are
the tools that you can use if you are a
user who works in Excel. You would like
to work in Excel, you would like to
continue to work in Excel, but also
harvest the power of PowerBI, but then
we have these tools available. If you're
not really limited to Excel, but you're
open to use other tools or you don't
have, for example, this uh version, this
this licensed version of Excel that
allows you to use the tools, you can
switch over to the PowerBI desktop
application. PowerBI desktop also
includes a way to query a data, power
query. It also includes a way to
visualize a data and to shape and model
uh the information. So you have
everything in one tool which is
completely uh free. When you use a
PowerBI desktop, you can upload your
reports to the servers online. In the
future, you'll be able to host them on
premise and reporting uh services. We
have a mobile solutions and since the
release of the latest version of NAV, we
can make use of the PowerBI API to embed
all reports in uh NAV. I also
demonstrate that
later. So, when you would like to get
started, the first thing that you need
to do is think before you begin. Cannot
repeat this this enough. The tools that
we have out there are such very amazing.
They look very attractive. You can
create very stunning reports. But to get
them right, you need to start to think
about your data model. And even though
we're not we not creating a data
warehouse. And even though you might not
be creating cubes, you still need to
think in the star shea. Which means that
the information you would like to
analyze, you will gather that in a
table. Let's call it a table which is in
the center. And we'll call that the
facts. And that table contain uh
contains measures. surrounding that
table we'll drop our other tables for
examples customers or products uh a
timeline which we call dimension tables
it don't need to be nav dimensions can
be actually attributes that you would
like to use to slice and dice the data
and whatever tool that you use this
actually a very interesting and
performant way uh to create a data model
which you can then use to present or
visualize that information. Now all of
the tools that we use uh also have
different programming languages uh that
that the tools actually use. So you can
be a user without any technical
knowledge that goes and uses the tools
to create a report. But if you would
like to go a little bit deeper then you
might need to start to learn SQL M ducks
MDX R and whatever letter is next in the
alphabet that might become available in
the PowerBI uh tool stack. So what are
the these languages meant for? Let's
start with a small introduction. SQL or
TSQL is actually the language that you
use to go to a database. You can
generate it and you can also use that in
the context of PowerBI reports. You
execute that before data is is important
to prefilter to join tables to make use
of maybe views store procedures and so
on to build a little bit of logic in our
queries and to make them a little bit
more uh performance. SQL is not so
difficult uh to learn. Most of it can be
generated. Of course, if you create it
yourself, it might be uh might be
better. After SQL, we have M. M is
actually our uh power query language
that we use and you will use M during
the import of the data. And M has a lot
of uh functionalities. It's actually a
programming language which which will
transform, clean up, uh create custom
columns. Actually, it's a very very very
rich uh language. It contains lots of uh
definitions. It's generated
automatically if you use a power query
editor in Power Query or in PowerBI
desktop. But it can become a little bit
difficult. So, it will need some some
practice to be able to get good at at M
because the language behaves different
than other languages. It's actually a
step-by-step language as I as I name it
myself. After M, we have DAX. And Dex is
actually where the added value is of of
PowerBI where you will spend most of
your time. We will use DAX or DAX
expressions like you can create formulas
in in Excel to enrich our data model.
Now you can create DAX for example to
create custom columns to create measures
or KPIs. Uh we'll think about how to
create the data model which DAX formulas
that we will create and then we will use
uh a number of DAX patterns and we'll
also come back about that that later.
DAX is not so difficult. It's like
creating a formula uh in in Excel. But
one very important thing to understand
about DAX expressions is context. You
can create a very simple expression
calculate the sum of the quantity in the
sales effect table and if you drop that
for example in a matrix the sum will be
recalculated depending on the context of
the row and the column and so on and the
kind of calculation you perform in your
ducks formula will make it sensitive or
insens insensitive to certain types of
context. Now it's quite abstract. We'll
come back about that uh later. Then we
also have MDX or MDX is the language
that you use for example in in cubes or
analysis as services. I find that
relatively difficult although when you
create cubes for example there are
number of tools out there that can
generate them for you automatically. You
can use MDX to pre-filter to to query
data. MDX is a little bit like like DEX.
can also use that for example to create
KPIs and measures in your
multi-dimensional analysis services
databases and so on. So that's M MDX. We
can also use that of course in the
PowerBI
context. And then we have um R the new
programming language or actually a new
uh programming language in our PowerBI
stack. But R uh actually is a language
that has been used by scientists all
over the world to to perform actually
some very powerful uh calculations. R
was introduced in the PowerBI tool
stack. to be able to create uh visuals
in a in a program uh or via program or
function that that you create. But R can
actually also be used before during and
after uh data import. They can be very
short. You can use R for everything in
PowerBI. It's a fullyfledged programming
language but I've rated it difficulty
for it's one of the most difficult uh
languages. But like for example when you
start with PowerShell and sounds also
very uh difficult in the beginning but
if you build a little bit of of
knowledge and experience in that it will
it will grow okay but R personally you
should see that as your last resort. If
you cannot do it with any of the other
tools we have at our disposal okay then
we go to R and we can make use of its of
its
functionality. So these are the
languages that we will encounter in our
journey in all of the PowerBI products.
Let's get started with power query and
power query is something that uh we will
use automatically or we will create
scripts in power query using our M uh
language. Now how we will use power
query? Power query is actually the
engine which will transform the data. We
can have it access multiple data
sources. It goes to the power query
engine and it comes out for example as a
private table in Excel. Power query
started in Excel and to generate uh
tables. We can transform data. Power
query is actually uh somewhere in the
ribbon in Excel. If you open it, you
have lots of buttons that you can use to
do data transformations. Uh try to paste
a couple of these buttons here on on the
slide, but there are many more. And if
you look a little bit at power query and
if it's completely new to you but you
have a little bit of experience for
example in integration services ETL
extract transform and load then p power
query will be more and more familiar and
that's actually how you use it to
extract data transform it when you're
loading it in uh your data uh model. We
can do it right here in Excel but we can
also do that for example in PowerBI
desktop. So we have some buttons that we
can play with to load the data to
transform the data and then at the end
we'll click on the load in our Excel
file uh button or load load and data
model which will then create a private
uh table on which we can uh we can
work. We can start from different data
sources. We can also for example start
here uh from an export to Excel use the
power query engine to transform it or to
unpivot uh data. You have some other
examples multiple files multiple files
here which we can then convert into uh
one file. The result if you if we use
power query in Excel will be a new
table. The advantage of using power
query or the the business case is more
in the fact that for example you might
have already users at this moment who
are using Excel uh and linking tables
using uh very uh exotic VLOOKUP
statements which are very difficult to
maintain and to to understand. Well,
Power Query might be a much better
alternative. Behind the scenes, Power
Query will generate some kind of
language and it will do everything. This
is an example of the M syntax. It can be
generated, you can create it yourself.
You can modify it and you can also
customize this using a parameters to
make it dynamic. So, you have a lot of
uh possibilities here in uh in M.
Everything that you do in PowerQuery
when you start in Excel or when you use
the PowerBI desktop tools will be saved
in steps. So all of the modifications
that you're doing, you're importing
data, you are changing data types, uh
you're multiplying by this and
transforming this and so on and so on is
saved in uh different steps that you can
also rename since one of the latest
versions of of PowerBI. So you can see
what happens. You can go back back and
certain steps you can also edit uh them.
So that's a a very uh advantage. If you
look at uh the power query tools in in
Excel, that's the best way to remember
how to use them. Power query will
prepare your cookies. Power private pore
uh or or tables will bake the cookies
the data model and then you can use
power view, power map or Excel to
present and share uh your cookies. So
PowerBI is as easy as baking cookies
especially when you work in Excel.
Okay, so it's time for a small
demo. So let's have a look at what we
can do with Power Query. I just have a
couple of of
examples. So let's have a look here on
my
machine. I prepared a couple of demos.
And the first one is just actually uh
here in
Excel. Let's wait for a moment to see if
it
opens. Oh, it's a little bit too slow.
Well, I'll do that locally then.
should have that here
too. One
second. Apparently, my machine decided
this afternoon right before the
presentation to become a little bit
slower. Voila. So, I'm here in um an
Excel. And if you have a look here at
our top, I need to go to uh insert
normally or data. Where is it again?
Query. No, here I am. Sorry, I was a
little bit confused. So we start in
Excel. What we have created right here
is a possibility for a user to end or to
enter an a starting date and an ending
date. And then actually by clicking on
the refresh button which should be here
in the the data part, a table will be
generated which is a date table which
you can then add in your data model. If
you have a look here, if I just go back
to
[Music]
home then to the query. No, I need to
start from here.
Voila. So if you have a look here in
Excel 2016, you will find power query
here in uh the ribbon. If you come from
a previous version of Excel, there was
actually a top with the name power
query. So it was very easy to find back.
If you go to Excel, it's a little bit
more difficult otherwise it would be too
easy to find back. If you click here on
show queries, uh you will uh display the
queries that we are currently uh using.
And what you notice is that I have a
table which is generated based on the
input and I created also a small
function in here. So let's have a look
at this function. I will just go to edit
and the system will open uh power query.
What you notice is that we see a
function which can have an input uh or
two input parameters. You can invoke the
function and it will create a date uh
table. If I go and have a look here in
the advanced editor, that's where the
magic happens. Here we can actually see
the the power query script which will
generate a table. Now this query editor
isn't really the nicest one although it
will detect syntax errors if something
goes wrong. H you can try to figure out
for a long time how to how to fix it. So
what I have done is
here let's have a look in notepad++ I've
actually pasted the same query and there
for example you can also have some some
color recognition available. So what we
have here is a let function. It will
create a table based on an input date.
Uh two dates actually start date end
date. This is how you create a function
with parameters. Uh I will based on the
information I will first create a list
of months. I will find the number of
days between start date and ending date
by simply subtracting uh them. Using
that information number of dates and
duration I will create a date list. And
from that date list I will create a
small table. Let me just drop down a
little uh here. And once we have the
table, I will start to do a number of
transformations. Change data type,
figure out um uh month uh day of month,
month number, year, day of week number
and so on. Actually behind the scenes
some variables will be generated and all
of that in the end will actually be be
saved here when I call this uh this
function. This function is stored here
in my uh power query.
uh it's actually in my data model. What
I then did actually is I created a new
table by invoking the function. If I go
here uh behind that table and then to
the advanced editor. Where is the
button? V. Here it is. Then basically
you notice that I can zoom in here. No,
that I'm actually looking at the
information in my Excel workbook. So I
will fetch start dates. Here it is the
start date. here is the uh the end date
from the Excel file, transform it, pass
it along to the function and it will
create a date table. So it's something I
I can do in Excel and then the user
doesn't have to do that him or herself
anymore. We can make it even more
flexible if you want to. It's just a
silly example. Now if we are here in
Excel working with Parker, we can
actually do the same thing if you use
PowerBI desktop. PowerBI desktop is a
free tool you can download and and
install. What I've created here is
actually a PowerBI or a PBIT file which
is a PowerBI desktop template file. And
it's a new option that has become
available uh last month. And if I open
this here, you notice it also asks me
for a start date and or end date. I can
uh load and basically what happens then
is that the query is re-executed. Takes
a couple of seconds and it will create a
dimension table also here in PowerBI
desktop. And then as a user I can
continue to load extra information or
the other tables I would like to use and
then later on to create my uh data
model. So creating a data mention is not
is is can be kind of difficult but you
can make it very easy for example by
making use of a power uh query function.
If I just go uh into the advanced editor
here in PowerBI desktop you also notice
that I can work with a function. and I
will create my table and in PowerBI
desktop uh since a couple of months we
can also use uh parameters to make it
even uh more dynamic. When in this case
when when I launch my file he asks me
for a start date and ending dates
doesn't really make much sense. If you
start the 1 of January maybe in the
1980s and you end in 2050 I think that
should cover most of your BI needs but
just just an example on what you can do.
So these are some examples of of power
query. There are many more but there are
also some other tools I need to uh cover
uh today. One of them is then power
private. Power private is actually also
a plugin in Excel in Excel 2016. It's
automatically in there and other
versions you might need to activate it.
And with power private what we will
actually do is we will create uh our
data uh model. And according to Mr.
Excel. Bill Jalen, founder of Mr. Excel.
Boro private is actually the best thing
that happened to Excel in 20 20 years.
And I actually agree when Bor Private
was introduced in Excel. It's actually a
very powerful tool and it still has a
lot of advantages. Although nowadays I'm
more eager to start to use PowerBI
desktop. I don't know if you can see the
difference here between the two tables
in Excel. The one on the left is
actually a normal private table. One on
the right is a power private table and
there isn't actually much difference
between the two and how a user uses them
but there is much more power behind this
table than there is behind uh the other
table. That's the power of power private
the data model and that you will create
and the meta data will provide in the
data uh model. So using power private we
can make use of a lot of intelligent uh
functions smart functions to be able to
assist the user to create a data model.
uh we basically can u u have a virtual
limitless data capacity. So actually
porop pirate is actually a mini analysis
services which will run in Excel which
will be able to slice and dice your data
should be able to work on millions of of
rows. Of course also depending a little
bit on the hardware of the machine you
are running it on but it should be a
very powerful tool without all of these
limitations we have in Excel being for
example 65,000 rows 1 million rows and
so on depending on your uh version. So
using power private you can start with
your row data then you go to power query
you import the data you transform the
data and with power private you will
create a data model a very enriched data
model which you can then attack for
example as a user in excel uh by
creating charts or or private tables or
what you're used to to do you can use
power view to visualize the information
uh you can send it up to Q&A for example
in in shareepoint or on powerbi.com and
you can also use power map I would go
into those tools tools in a few moments.
So let me do a small demo again this
time on power private. So I will go
again here to my
file demo. Let's have a look here. Power
privates. So I have actually an an Excel
file in which I imported some data. If
you have por private enabled, it's
available in the ribbon in in Excel. I
will just open it. Takes a couple of of
seconds. And I imported data from NAV
make making use of O data web services.
And if you have a look here at the data
model in my Excel file, it should
resemble a little bit a star sheima
where in the middle we basically have
our fact table surrounded by other
tables uh to uh be able to slice and
dice for example invoices or or or uh
posted invoices by customer by product
on a timeline and by salesperson. And to
create this kind of data model import
private, it's very easy to get started.
You can import your data from different
types of uh of services. Of course, your
data might be a very interesting one to
use because you can create your query
objects in in NAV. Query objects in NAV
can access data from multiple tables.
They're very fast when they load and
execute. You can publish them as an O
data web service and very simply access
them from uh within Power Pirates. We
can also combine the
information with information coming from
somewhere else. Now I don't have all
afternoon or two or three days to talk
about uh uh power private but basically
what what you can do is you can build
your data model. So you import the data
as different tables. Then you need to
verify if the data type has been
recognized correctly. For example, an
item number is not something that we
would like to add uh in in a report. So
we need to make sure it's recognized as
text. So then he will not propose these
silly aggregations of of data. So we
provide them here in the data model.
Then there is also some extra
information that you can do. You can
create calculated columns. You can
create new tables. We can use all of DAX
expressions to enrich our our data
model. And there is some extra metadata
table properties that we can also uh
provide. So once we have created our uh
data model here in pore private, we can
then simply close power private and the
user will have access to it in Excel
when they start to create a private uh
table. Now just to give you a small
example of of a DAX expression. Let me
just go back here to my home tab and the
data. As you notice here, I'm importing
some invoices from NAV which actually
come from the invoice lines that I uh
published. Okay, let's just continue.
That can happen sometime in in Excel.
So, I've just imported some uh some
invoices. And what you notice here is
that I have the number of the sales
invoice line, the type on the sales
invoice line, which I'm just importing
from from NAV. Then I would like to be
able, for example, to link this fact
table to an item table and a resource
table to use them as attributes. The
problem is that if you try to do this
here with the number, it won't work. So
we need to split out these numbers
depending on the type and that's for
example a reason to use a DEX expression
to create two new columns which I have
right uh
here. New columns or columns which are
calculated are shown here uh in with a
black uh color and this is the very
complex DAX expression that I am using.
So let me just click on the column to
see it. Well if the type is item then
take the invoice uh number. So it's a
very simple query language that you can
use and a very simple example. Once I
have these two fields in the data model,
I can then use them for example uh to
link the invoices here to uh the
resources. Okay. So we'll spend some
time in uh power private creating our uh
data model. Let me just close this
again. Once it's closed, we can we can
attack it actually from uh from within
Excel. I can start to create a private
table and I can access my uh my data.
Now creating a date table can be
complex. So what you can also do for
example if you have some data in Excel
and if it's a table in Excel what you
can do is if you put your mouse in there
should be a button here in the power
pivot for this table to also add it into
a data model. So what you can also do
for example if you have this row of
dates in here in Excel add it to the
data model go back to power pivots and
then what you can do is if you have a
look here back again at the data
mentioned table this is the date coming
in from from Excel you can calculate uh
here the years that's really annoying
today so I will calculate the year from
my date the month the day the week day
the month name and so on using these
expressions here make use for example of
a of a switch uh statement. I can also
use that to generate my dates uh
table. Okay, let me just close that
again. The idea of using our uh power
private tool is to create a data model.
It's one uh one thing that we can do.
Now if you for example have a number of
power query tables in Excel and you have
a poor private data model, you can't
really combine them. So you will have to
choose between one or or the other.
Okay.
The idea of creating a data model is to
be able to create uh a presentation of
the data. For that we can make use of
PowerView. Powerview is also a plug-in
that we can use in in Excel. Um might
not be the best tool at this moment
anymore. PowerBI desktop is actually uh
more interesting. Powerview can be found
in the ribbon. If you're not working in
Excel 2016, but in the previous version,
you will find it in the ribbon. the
insert you can click on it. In Excel
2016 the tool has been hidden in the
ribbon because Microsoft prefers you to
use uh PowerBI desktop. Why? Well, Power
View has been developed based upon
Silver Light. PowerBI desktop is using
visualizations which are based on HTML
5. Using power view, we can then create
these enriched visual interactive
dashboards in uh in Excel. But let's
have a look at how that uh that works.
So let me just go over again
here poor view and I have actually an
Excel file which is the same Excel file
that I used
before which has a which has a poor
private data model that I'm now using
here to leverage in a poor review sheets
and if it loads it can take a couple of
seconds depending on the data then need
to enable the content what we notice is
that fab I know I have a dashboard here
in Excel uh where I can see my customers
here from NAV. If I click on one of the
charts, it should be very interactive.
If I have a look here uh at where they
are coming from, I can also see some
some information. I can add some some
filters. How does it work? Well, what
you need to do is just go and then in
your insert menu, if you're not in Excel
2016, in the insert menu, you should see
power uh view. If you're in a later
version, you need to customize the
ribbon and add the button again
somewhere. you will end up in power
view. Here on the right side is where
you will see your data model and so the
data model from before in power p is
available here on the right side and I
can start to create dashboards. For
example, I will select the amount you
notice here in the fields uh that some
of them can be aggregated. Some of them
are calculated using a ducks expression
and if you select the fields they are
added here uh in a kind of a table
layout. So if I select amount from the
invoices and then city uh from customer
I can see the information in table
layout and then the idea is to go here
in the design uh menu and then for
example transform
this into a table a column a chart to
use a map to visualize the uh
information and depending on the visual
that you select you get some other
possibilities and once you have selected
the visual here on top there is also an
extra tab which will appear imagy can
also provide some extra meta data
So I can transform this into a map. The
first time he will ask you for
permission to connect with the Bing
services, but it works quite quickly.
And to give some extra context here, uh
let's do uh let's just take a field and
drop it here in the property. So the the
tool itself is actually was inspired I
think by reporting services but meant
for nontechnical people. So instead of
creating expressions, we will drag and
drop fields into properties of of
visuals. When we create this, if you
spend a little little bit more time in
there, we can create a rich interactive
dashboard in uh uh
Excel. And that's a couple of
uh brief words how we can use actually
power uh view. It's it's available in
Excel. It's still available in Excel. If
you enable it, you can create uh more
interactive reports. But I think the
added value at this moment is more in
the other tools that we use in PowerBI
desktop. Before I go over to PowerBI
desktop, there is also a kind of a
strange duck in the list of tools that
we have available in in
Excel which is Power Map. Power map is
also a plug-in that we can use in uh in
Excel and it's actually not really a
PowerBI tool or a reporting tool. Power
map is actually a tool uh that you can
use as an alternative for uh PowerPoint.
It's a presentation tool. If you have
geographical data which you would like
to present uh for example over uh time
then we can use uh power map as a plugin
in in Excel. In the past it was named
power map. In the latest version of
Excel it's actually been renamed into 3D
uh tours. If you create a power map what
you will create is actually a tour. A
tool can consist of one of multiple
scenes. A scene is actually something
you would like to display on a map. So a
scene is a map and it can contain one or
more layers and a layer is actually the
way you would like to look at your uh
data, how you will visualize it and for
example also how you would like to play
it using a dates that you have in your
data
model. So we have a couple of of of
examples of how you might use power map
here on the left side. I've used the
power map with just a custom bit map to
present information. It can be a picture
you take of of your warehouse or your
store uh or whatever you would like to
visualize. All that you need are the
coordinates uh on uh on your image and
then map them to some other data and you
can make use of them in power map. On
the right side, I'm using the standard
uh power map to visualize information on
on an app coming from a Kronis database.
Now, I'm using a simple Kronis database,
so I don't have that much demo data.
That's why uh it's relatively uh empty,
sort of speak. Now, how do we get
started with Power Map? Let me also
demonstrate uh
that. So I will go back to porum mapap.
I have an excel file which I will open.
It can use the same data model than the
excel file I used before with the por
py. It can be any data in in excel. And
to be able to make use of power map we
need to go here into the insert menu and
open or 3D maps or uh uh use the power
map button as it was in the previous
version of uh of Excel. Takes a couple
of seconds to uh uh open. Now what we
will create with power map is not a
report. The idea of working in power map
is to create a visual representation of
the data that we can play. Now if you
start with an empty chart or with an
existing one, what he will start to show
is the list of fields that you have
available from your data model. They
will pop up in here. So you can drag and
drop them or you can uh just select them
if you want to. The first thing that you
need to do when you start with power map
is explain to the globe or the visual
that you are using where your
coordinates are coming from uh in your
data set. So in this example what I have
selected is the city fields from my
customer table which I would like to
link to one of the fields I have
available here in in power uh map. I
think behind the scenes the system is
using Bing maps uh to present the uh the
information the if I link city from my
customers what I also noticed is that
power map was able to map 80% of of the
data you can click to go and have a look
at some more details to see why certain
mappings didn't work and then correct
the data or add some extra information
in your data set. Okay, that's how we
get started. We need a location field.
It can be one or multiple fields. Then
we need to define what will uh be used
to visualize the height of for example
here the graphs that we have on our map.
So in this case I'm using the quantity
from the invoices. I can also use any
other field from uh my data set which I
can use to create uh an aggregate if I
want. I can also categorize these fields
for example by salesperson, by country,
by something else. And then very
interesting is I can also provide uh a
date from my data set to be able to play
uh the data. And once we have that we
can start to play around a little bit,
zoom in, zoom out. You can change the
pen uh depending on how you would like
to have a look at uh the data. Here on
top in the ribbon uh you can select a
number of themes. You can add some
shapes. You can even add some extra
charts, legends, some text boxes to
fine-tune. Right now I'm working in uh
two uh scenes. Scene one I have here.
Scene two I have I have here. The
difference is actually the same data but
visualized a little bit uh more or
differently. Um just to be able also to
show that if you for example like to use
certain visualizations of the data it
might have uh certain um let's say
requirements on what you feed to uh to
power up. Just to give you an example,
if I would like to present this uh
information using this visual, for
example, by country, then I need uh uh
some information to indicate where that
country uh is. So, I don't have a
country data set selected at this
moment. In location, I have city. That's
why he refuses. So, I just created two
data sets. Once once we have your your
two uh tours in here, we can still go to
the properties. Where are they again? Um
let me just try to open them. Nope, it's
not. Here it is. No, we have some
general properties. Ah, sorry. They're
here at the bottom. So, we have some
extra uh visualization options that we
can choose from. And then here at the
top, we have some extra scene options
that I can select from. For example, we
can work with some some effects. And
here you will see why we are using a
power map because we can select for
example how the camera needs to move
when we will render the visualization.
So let's have a look. If I play the
tour, this is actually what I will I
will see. The camera uses some kind of
perspective to uh to display the
information and I can see data coming in
from uh from NAV, whether they invoice
by region, by uh by country and I can
have a have a look. Of course, it will
work uh more nicely the more data that
uh that you have
uh to be able to present them in a
geographical uh way. So we can test how
the map looks like and if we like that
we can create uh the tour. We can uh
decide how you would like it to be uh uh
displayed and to make it completely
complete. You can also include a
soundtrack. So it's not a a reporting
tool. It's a presentation tool and that
you can uh use and it's a part of of
Excel. It works best with large amounts
of uh data
sets. Okay.
That's power uh map. A little bit the
strange duck in the list of tools but
might be interesting to uh to use. And
remember you can use a custom image
which you can upload. So you can
completely customize it. You could for
example uh show your warehouse, show uh
where your stores are located or
whatever is of interest uh to
you. And then we have um some new tool
that we can use PowerBI desktop. It has
been not around for for not so long. I
think maybe one one year, one year and a
half, two years, but it's a very very
very very exciting tool, especially
because every month there is a new
version and we get lots of new goodies
from from Microsoft and Microsoft is
really investing enormously in uh in the
tool. I can pretty confidently say that
if there is something you don't like
about the tool posted on the forum, uh
if it's something other people also
don't like or would like to have in the
next version, chances are very high that
you will get uh that. I think it has a
very big priority within uh Microsoft
and PowerBI desktop is actually a tool
that you can download for free from the
powerbi.com website. You can just go
there, download it, install it and it
has everything uh that I have also shown
you in Excel but uh bit better. And we
have a power query in there to be able
to get the data from the database. We
can visualize the data. We can create
very interactive reports. The visuals
are based on HTML uh 5. They're very
interactive and I will demonstrate that
also by using or showing some some
examples. Okay. Now with PowerBI desktop
what we will do is we'll connect to data
sources. So you start the tool, you open
it, you connect to the data data source
of your uh
choice. Uh we have a number of options
available. The screenshot here is from
some time ago. In the meantime, you have
many more uh options that have become
available and Dynamics NAV or Dynamics
is also in here since the latest uh
updates. Uh so we can also connect to uh
to that
directly. If you want to, you can also
even connect to uh to Facebook to create
a dashboard on the latest likes that you
received. Uh we can go to a Twitter and
maybe in the future we'll also get uh
LinkedIn. That might be uh might be
possible would seem logic. Okay. Okay,
once you connect to a data source, you
can then choose to import the data
directly and then modify it afterwards
or you click on the edit button, you
will go into the power query editor
where you can use your M language to do
some uh transformations. You load, you
edit or you load first and you add it
later. PowerBI will import your data and
then actually in the tool itself you can
also determine uh how your data might
need to be transformed. So you can click
here on the edit queries button to open
uh your query. Have a look actually at
how it was imported. And here at the
right side you will notice that we're
using a power query visualized a little
bit differently. So we fetched
information from a source. We
navigateavigated and we change the data
type of a number of uh of columns. We
can make many more transformations if
you want to using the the tool. So we
have a number of uh uh transformations
we can perform on the data type. That's
the very first thing I always recommend
you to do. So all of the columns which
have been imported for example from an O
data web service verify the data type is
okay which means that things that should
not be numeric make them text things
that should be numeric make them then
numeric or or decimal have a look at the
dates for example which come from an NAV
database usually they have the uh the
year the month the days in there but
also the hours the minutes and the
seconds so you can change the format uh
so it looks a little bit uh nicer. So we
transform the data using PowerBI
desktop. Uh we can see all of the steps
and since the latest release, we can
also rename uh steps. We can also drag
your steps around uh if you if you like
to. So it's a little bit workflow style
changing and transforming of the data
that we are or
importing. We can then of course close
and load the data go back to PowerBI
desktop. The changes will be applied to
the data which was already uh imported.
and then we can uh like create our
report. So as you notice I also have
prepared a number of small demos on
PowerBI uh desktop. So let's get started
with with an
example. I have a number of reports in
here. Let's take the first
one which is a report that fetches
information from an NAV database.
And if I remember correctly and so let's
have a look how it how it
works. So what I see right here is an
overview of my stock for a number of of
items uh coming from our corners
database. I can see the quantity for
example in the item ledger entry table
and I also have the accumulated quantity
which is also calculated. So depending
on on what happens, the committed
quantity also updates. So at any moment
in time on the timeline, I should be
able to see how much is in uh in stock.
I have some kind of date visualization.
I can filter on the item or items that
are selected and then the visual will
recalculate and and update. It's just a
simple example. Information can be v
visualized in in different ways using
different types of of graphs. The choice
is is up to
you. It's still rendering at the moment.
But here I selected a different type of
of charts. Okay, let's wait. Let's don't
wait too long. What you notice is that I
have a very simple data model in here.
So I'm I have a table item transactions
where the information is coming from uh
from NAV and then a table uh date to be
able to do slicing and dicing on on a
timeline. What I get from NAV is the
item number, deposing data quantity and
based on that I can then also calculate
a number of different
fields. If you get started with PowerBI
desktop, the first thing that you need
to do is a get data. In the case of NAV,
you might be able you might do a get
data feed. For example, you can go
directly to SQL server to have a look at
how this data here was uh was imported.
So I only get item number, posting, date
and
quantity. I can open the queries again.
uh and uh let's have a look at what
happens. So if I go here to the uh
source, what you notice is that if I
open
it, I'm basically going to my database
directly on SQL server. So that's one
way of fetching the data. I will go
directly to SQL server. If you go to SQL
server, what you can then do is you can
for
example execute a query. You can see a
list of all of the the queries of the
tables here in in your database. And
then we can say okay I would like to
fetch some information from SQL. So in
this example if I open the advanced
editor you will notice that we are
fetching information here from the item
ledger entry table just some columns
from
there. At the end in the last step what
I'm doing is I am just uh removing all
of the other columns I'm not interested
in. So you notice that here on top you
have a number of buttons that you can
use to filter out columns, filter out
rows uh to only end up with the
information that you would like to to
have. That's the information which is
coming in. Let me just close the query
editor and just do some pretty basic uh
things in there. Then actually the
interesting part here are a number of
calculations that I have performed. So
what I'm actually doing right here is I
have my my table which I import from
from a database. I have my date table.
of the relation between the two and then
I will just create here a formula which
will calculate uh the accumulated
quantity from the item ledger entry
table and so you can see I'm using a
calculate function to have the sum of
the quantity in the item transactions uh
table calculated and then I'm allowing
that to be filtered uh with information
from the date table and every time I do
a calculation of my accumulated quantity
uh calculate the sum of the quantities
until the date that I am looking So
everything until and before that uh date
and that's an interesting or a du
expression that you can use for that.
I'm using it right here to get a
cumulative quantity. You could also use
that for example if you go to your uh
general ledger entry table and you would
like to see
um information or sums of quantities or
amounts on on your accounts. It's
actually something that we use quite a
lot in in
BI. Once I have those those fields, they
will actually enrich my data model here
of the item transactions table and then
I can start to use them in in in
visuals. So basically if you have a look
here it is loaded. What you notice is
that we have a number of panes here on
the left side and import desktop.
Typically we start here to import the
data. Second step will then be to create
a table relations and third step will be
to create our uh reports.
If you create a report, what you will
notice here on the right side is the the
data of the tables that you have. And to
create a visualization, you can just
click one of the fields or drag them
here on the canvas and then select one
of the visuals that we have available
here on on the right top. And they are
actually connected because there was a
link in the uh data model. So this is
actually a simple example uh of simple
du expression that I'm uh using. Next
example which I will show is the the
sales uh dashboard from uh SQL which is
using uh also information from the SQL
database but with with a little bit more
uh intelligence. Let me just open
that.
Okay. So what we are looking at right
here is also information from our NAV
database. I can see our
salespersons. Excuse me. I'm using the
the Belgium database. I have two
companies in there. Konis Bell here and
Konis Belgic. I'm just displaying some
uh some
information. How do I get the
information? Well, if you have a look
here at our uh data model, you notice
it's a very simple star. I have my
invoices uh minus the credit memos
linked to uh some sales information,
some customers, some sales people. I
also here have some tables which come
into the data model which which I hide
from the report view because I needed
them to import the data and to create
new tables. So what am I doing right
here? Let me just show how it works.
What I basically have in my uh database
which is hosted on a specific server on
a specific database is I created a
number of views. So if I go here to uh
sales, what you notice if I just open
the advanced
editor is that I'm I'm querying a number
of views which I've created on SQL
server. A view for customers, a view for
uh sales headers and and and and credit
memos, a view for this, a view for that.
I'm very simply querying that. Why do I
use a view? Well, just to be able to get
back information from all of the
companies in my uh database. What you
might notice is that
here I also included an extra column in
each of the views indicating from which
company is this information uh coming.
So in my view I'm just doing a union of
all of the information over the
different
tables. I fetch that information here in
PowerBI desktop and then what I can also
do for example is go here and create a
filter. So I can put a tax filter for
example on this company which I did to
filter out the information from other
companies. And once we have a filter in
here we can make that also dynamic by
working with parameters. So what I did
here in my data model is if I go to my
parameters here is there are a number of
parameters and one of them is a company
parameter which I am using. You can give
it a name. You can give it a number of
values. for example, the values of the
names of the companies in my database.
Default value, current value, and it's
also something the user might select if
they open and run the report. From which
company would I like to be able to see
this uh data? So, you can create uh your
reports, your dashboards with
information coming from multiple
companies and the company is displayed
here. You can go back to manage uh
parameters, change a value uh of your uh
parameter to see the information from
the different company. Just one example
of something that we can do. Is it the
best solution? I don't think so. Just an
example. We can work with these
parameters in PowerBI desktop. That's a
very nice feature was added quite
recently. But I would also like to warn
you, we can't use these uh parameters if
you will uh upload your report to
PowerBI.com. So there your report will
be uploaded as is. Once it's uploaded,
you can't change the value of these
parameters anymore. So you might might
want to upload it multiple uh times to
powerbi.com. It's a feature which is
probably in development which will
probably arrive in one of the next
versions but it's not yet
there. Okay. Another example which I
have prepared here number three. Let's
have a look. That one I will run on my
virtual
machine because it's connecting to a
database which I have right here.
What we see at this moment is another
example of of dashboard that that we can
use. I'm just looking at the number of
customers by salesperson which I'm
fetching from uh the customer table the
salesperson table also having a look at
what these customers did the latest
years and I'm trying to to figure out
for example which
are number of active customers by year
the number of new customers by year and
by salesperson just to see returning
customers. Yes or no? What's what's
going on? To be able to create this
dashboard, there are better ways. What
did I do right here? It's just
visualization of the data that comes in
the data model. In my data model, I only
have one table. This one table contains
a number of fields. Agent year, month,
number of new customers, number of
active customers, and so
on. Based on that information, I'm just
using the visuals. And how did I find
this information in the database? So
let's have a small look here in the
advanced editor and what we notice is
that the data is coming
in by executing a store
procedure. So I'm just running a store
procedure on my SQL server database find
the number of customers by agent it
returns me this data set which I can
then consume in uh PowerBI desktop.
Another example of what you can do if
you don't like to work with SQL queries,
you don't like to work with fuse, you
might create one or multiple store
procedures, you can also access them to
harvest that information. Is it the best
way? I don't know. It's just a
possibility uh that uh that you have and
you can create your reports based on uh
that and your visualizations. I can also
upload this information to pbear.com
have it refresh behind the scenes making
use of the gateway. I will show how that
works also in a few moments.
So this is here a dashboard because I
have some uh time line information. I
might also be able here to zoom in and
because I'm using a time dimension.
Okay, that was another demonstration. So
let's close this one for the moment. I
have some more demos here. I have
another kind of dashboard which is a
sales uh dashboard. And this one is
actually a bit more interesting. This
actually the way that I would recommend
you to uh to work. Now you don't really
have to make a choice depending on the
rights you have on your database. You
can combine all of these methodologies
but this way I prefer to work and what I
have right here is actually a data model
which comes from NAV which resembles a
little bit what we had in power private
in Excel. So basically I did the same
thing. You can do that in two ways. You
can do a get data. You can go for
example to an O data uh feed. uh in here
you can just paste the URL that you
would like to use in the next window.
You just need to authenticate uh to your
service tier and the data will come in.
I recommend you to work with query uh uh
objects. You import the data in here.
Once you do that, just go over your
tables uh quickly. Let me just wait a
couple of seconds till I have my data in
here. Voila. And then what you need to
do
is in each of the fields that you
imported, make sure the data type is is
okay. Okay, once the data type is okay,
you can do some transformations and when
all of the information is
imported here, you can then create your
data model. That was not the button to
click. Let me just go here
again. This was the
one. So, I'm using my O data web
services. What's the advantage of using
OATA web services? Well, you don't need
to manage security in in SQL. If you
like to use any of the other examples,
SQL query, SQL view, SQL store
procedures, you need some kind of user
which is allowed to go to SQL server and
execute these store procedures and you
need to manage that in in SQL itself.
That might not be something you want to
do. If you you go the O data way, then
you can use O data web services which
are managed by the service tier. You can
set up a separate service tier. You can
manage the performance of that and you
can also manage all of the security of
that in uh NAV. uh itself. What I have
right here is actually a dashboard which
I created and I was a little bit
inspired by the information that we
actually have on powerbi.com when you
create the content uh puck. It's
basically a number of web services uh
which I published in
NAV which I linked and then used to
create uh a dashboard uh in here. The
dashboard is not the most spectacular.
It's just the way that you create the
data uh model. Even though we go to NAV
and we import uh information from tables
that might already be related in NAV, we
still need to recreate these relations
in the data model. So that that's uh
important. So we have a number of
choices that we can we can uh we can
make. You can go to a SQL
database. You can go uh import
information from any kind of database.
There are some advantages, there are
some disadvantages. Something I would
like to show you is also the following.
If I just launch a new uh PowerBI
desktop in
here is that there are a number of
advantages. For example, going to
SQL. If you go directly to our NAV uh
database using SQL fuse, using SQL
tables or SQL store procedures or or
data web services, you always have to
recreate your data model in PowerBI
desktop. If you use PowerBI
desktop uh that can be a little bit time
consuming. Now what you can for example
also do is you can say well I will go to
uh SQL and then in that case of course
you need to know the name of
your SQL server. Let me just click on uh
okay. I wait a couple of seconds. I can
see my databases that I have available
in here. Uh let's go there. And if I go
to an NAV uh database, then the list of
tables pops up. You can select the
table, filter it. You can also use a SQL
query and so on. That's not really super
super interesting. If you go for example
on the other way here to a data
warehouse or a database on SQL server
where you already have created your
table relations, you can make use of of
them. So let me demonstrate that. I will
go here for example is also select a
finance uh table in an Excel uh
database. Let me just wait two
seconds. Still
evaluating. Okay. And then what we can
do is we can also click on the button
select related tables. Then the system
will actually go and have a look at all
of your foreign keys in your database.
Also select all of those tables. Right.
So they should pop up any second.
Oh, once that happens, you can also
click here on the load button and data
will be imported. Uh, and the table
collections will also already have been
uh set. Now, this is taking a little bit
too long, but don't worry, I can very
quickly also do that
here. Uh, normally should be able.
Okay. So here I have Porbii
desktop. So locally it should go a
little bit faster. So let me show how
that works. I'll try to lose too much
time. So okay I go here to my SQL
server. Don't have a database name. By
the way, if you go to SQL Server, you
can choose to import your data or you
can also do a direct query on direct
query on the database. What I have right
here is a data warehouse locally. So,
let's also select here the fact table.
Click on select related tables. And you
notice that all of the other tables are
also selected because we have table
relations or foreign keys in the SQL
database. I can now click on okay. Wait
a couple of seconds. the table uh or
tables are
imported and the data model will
normally also be
created. Okay, apparently I have a
little bit of data in uh in my local
data warehouse. It's the let's say the
advancure works database from SQL which
is like the chronis from uh from NAV. It
can take a couple of seconds for the
data to to import. Once it's important
what you will notice is that and that's
the real edit value you can go for
example here to the relations they will
already have been created. So typically
what you can do for example is that you
can prepare a data warehouse a SQL
database in which you import data from
uh one or multiple sources how how you
would like to import it whenever you
would like to to import it and users can
access that uh information. uh they all
need to know the name of your database
and your sheima will be generated. I
might even already also have some
calculated fields in there. Everything
is done and as a user I only need to
take care of inventing a greatl looking
uh report and playing with with the
visuals. That's also another example of
what we can uh do with PowerBI
desktop. Okay, let's have a look at
another example here. So I have I think
that was already
open. Voila. And what I have in here is
actually uh maybe the best way to uh to
go. If you use PowerBI desktop, what we
will do is we will connect it to a data
source using all of the different types
of of of data sources that we have and
ways to import data. But the emphasis is
actually on importing uh data. Like I
said, if you use direct query on a SQL
database, you will import the data from
your data source. Every time you click
on refresh, all of the data will be
reimpported again. There is no
incremental load yet in PowerBI desktop.
I heard it's coming. I I noticed I saw
that on uh the on on the website where
you can vote for new features in coming
releases. It might be coming in the
future, but it's not yet here. So
imagine that you would like to take
ledger entry tables, value entry tables,
import them into power by desktop and
create a great looking dashboard and
report. Well, then you might encounter
some performance uh issues. What I have
right here is an example on working uh
with data warehouse which has already
been created uh thanks thanks to BI for
dynamics in in my case I was able to use
their software to create a cube. I'm not
a cube expert. the basics about data
warehousing. But using a wizard, I was
able to create a cube based on my NAV
database. It generated uh data
warehouse. It generated the cube with
some calculations. And using the PowerBI
desktop tool, I can also very easily
connect to uh that. So what what you
actually need to do is you just need to
connect to analysis services. Let's wait
a couple of seconds. Give the name of
your analysis services server. And let's
just show that using an example.
Where is the query editor? Here it
is. So what I'm actually have fetched
here is information from my sales
analysis cube. And if I for example here
click on add columns, what you'll notice
is that when you make a connection to a
cube, you might have multiple dimensions
in there. You might have multiple
measures in there. Everything is already
pre-calculated, contains data. You
select what you would like to uh select.
Click on okay. Uh columns are imported
and the advantage is that uh all of the
data is in the cube. You can still
import that and load that here uh in
PowerBI desktop or PowerBI desktop can
just connect to the cube and present the
information but you can do an interment
incremental refresh behind uh the
scenes. That's a big advantage of this
of this tool. Now in this dashboard I
also did a couple of other things
because if you have a look here at the
dashboard itself I'm showing here where
my customers are uh coming from and if I
zoom in a little bit you can see for
example uh the the sales in this city
for that customer also has a certain
value. I have a breakdown here of my
customers at the right top. I can see
their sales information, credit
information, debit information and then
for example depending on the sales
information of my customer, I might want
to send a salesperson uh there uh and
that salesperson might be interested to
have a look for example well I might
need to go to Germany uh today what is
the chance that it will rain for example
just a a crazy example just to explain
that besides the information coming here
from uh the cube you can also access uh
other kinds of of informations. I can
for example fetch information from the
web or any other web service which might
be of interest to me. So what did I do
here in my data set? I have a weather
service which I am currently using which
for a number of cities is providing me
information about percentage of rain,
wind speeds and so on. Where did I find
that information? Uh well basically uh
where is the advanced editor? I will
show you. I'm going here uh to a website
erpmagazines.com which you should check
out. It's from a very nice person
Alexander Totovich who was going to
present with me today but wasn't able to
uh to come and he created this web
service for me which I can just access
and it's it contains a table uh that it
uh just gives back and I can just access
that web service and the PowerBI desktop
tool recognizes this information as a
table and can import it. So it's a very
simple example actually I could go to
any website is able to go to a website
recognize the tables and the data on
there import and transform it so can
also make use of web services there are
lots of use
cases so I'm using this to enrich my
data
model and I'm also importing information
here from another web service that I'm
using so for example it's a no data feed
that comes from uh somewhere else or
some other kind of nav database which in
this case contains some extra financial
information about my uh customers and
here I can see for example the EBITDA
data the revenue of my customer and so
on which is in another database. So just
to give you an example that depending on
the type of report that you want to
create you can harvest actually uh
enormous amount of of data sources just
create your data model enrich your data
model create your calculations and then
uh your uh report itself.
Okay, another small example of what we
can do here is this
one.
Okay, so what I have right here is a
dashboard which is
opening hopefully quite quickly which is
actually a a dashboard that categorizes
your items depending on their uh sales.
So we are getting a little bit deeper
now into uh DAX expressions. What we can
see here for example is I have three
types of products. A products, B
products and C types of products. If I
click here on A, I can see okay uh these
are the uh the part of the bicycle that
I sell most frequently at my Cronis
company or who are actually providing
most of the profits in my organization.
If I click on on the B products, I can
see my B products. If I click on the C
products, I can see all of the other
ones. So, it's not by amount by by
number of products. It's actually by
percentage in the revenue that I'm
categorizing which type of product that
I have. I'm applying these on products.
Could also be customers or whatever
information that you have in uh in your
data model. What do we actually need? We
need some uh sales
information. So, what did they sell on
what date for which product? And we need
some product information. the the name
of the product, the some pricing
information, some quantities. What I
will actually create here is a measure
of sales amount. So let's have a small
look at how this works. If I have a look
here at my sales table, I can see the
data coming in from NAV posting date
quantity by item number and this amount
field is one uh which I calculate very
easily. I fetch the quantity from the
sales uh table which I multiply from the
price information uh from the product
table and because I have a table
relation in my uh uh data relations I
can also use the related function here
in a DAX expression to make use of uh of
that it's the power of uh of DAX. If I
have a look here in my product table
making use of the information I now have
in my sales uh table I can also
calculate a number of uh fields. For
example, I have a product sales which I
calculate as being the sum of the uh
sales amount field in the sales table in
this case by product. I have the
cumulated product sales which we also
calculating. For example, I will
calculate here the sum of my product
sales in the product table for all
products where the sales is before a
certain uh date. So there's the
accumulated sales which I'm calculating.
Depending on the cumulated sales, it's
not so difficult to also calculate the
cumulated sales percentage of the total
sales. And once we have that, then this
column is basically then where the magic
happens depending on if it's more or
less than 70 or 90% of the of the sales
in total. I attribute an A, a B or a C
to this type of to this to this product.
This then generates the new column here
in my data set. And once you have the
columns here in the data set, all that's
left to do is to create and visualize
the uh the information uh using a matrix
and using different types of of visuals.
We have a lot of of possibilities right
here. So ABC
categorization. Last but not least, I
also wanted to
show the 07 one. That one I don't have
on my HyperV. That one I have locally.
No, it's quite a lot of demos of PowerBI
desktop but I just want to introduce you
to the different elements of PowerBI
desktop what we can do with it and if
all of this is not enough uh then we can
also make use of of a number of new
features that recently became available.
One of them is R and the other thing is
forecasting. You might have noticed that
in the smartness session of NAV, I
presume forecasting was a was a topic.
Well, forecasting is also something we
can do in PowerBI desktop. What you can
have a look at here on the right side
are two things. So, I have some some
data uh coming from a data source
presented here in a line chart and I'm
using forecast functionality to predict
basically what will happen in the coming
uh year or the coming uh months. Now
this forecasting relies on a number of
algorithms which are quite statistical.
So depending on you need to have enough
data to be able to do goods or to make
good predictions. What you see right
here is a difference between PowerBI's
forecasting system the built-in one
which you can just enable in a property
of PowerBI and the forecasting which you
might access via R. And R is actually a
programming language that you can use
for example to also access machine
learning experiments on uh on Microsoft
uh Azure.
Now, how does this work? Uh, two things.
If you like to make use of the in
embedded PowerBI forecasting
functionality in the latest version of
the PowerBI desktop, you will need to go
into your options and it's a preview
feature that you need to activate. So,
if I just go here to preview uh features
there, this where you just need to
enable uh forecasting. Once you have
enabled that
property, then certain visuals will
support it. Just select your visual go
here. I think on the right side where is
it flap on the last options top
completely at the bottom you will have a
look here at uh forecasting you can in
or insert one or multiple forecasts
decide how they need to be uh visualized
and then they will be added here in the
visual the other one that I'm using is
using similar information but here
basically I'm using my R to enhance my
data model or my uh reports if you use
an R visual. What you basically need to
do uh is then program a little bit of R
which visualizes your data set. Now R
isn't the easiest language to get
started with. What you can do if you
want to is you can also have an
completely R development environment uh
that you can install on your uh machine
which I've already downloaded. It's a R
studio which you can then also connect
to from within uh PowerBI desktop. So I
just export that script here into R
studio and we can have a have a look. I
will not go over over the all of the
details but basically I have some
information in this case in an Excel
file which I'm importing and having a
look at this information in the Excel
file and then using a number of
functions from R I will try to predict
uh some uh information which I will also
then add in my data set and visualize
here in uh the
end. uh so the data or the functions I
use in are aren't uh the easiest ones to
to understand very small words so very
little documentation but they are
extremely uh powerful and the script
that if I then execute it basically also
uh visualizes the uh information here
and then the last part is also able to
do a forecasting making use of a machine
learning experiment. So just to give you
an example of what you can do with with
R. You can also add that in your data
set. Could show you many more examples
but we only have a limited amount of
time of course. So PowerBI desktop is a
very interesting tool to uh use and I
also demonstrated a number of uh
patterns and design patterns aren't only
important in the NAV context. patterns
are also important in a PowerBI uh
context. So that's actually where you
should spend most of your uh time.
There's a very interesting website where
you can go through it's ducks
patterns.com uh created by very two very
very very very intelligent people who go
all over the globe think Marusu and
Alberto Ferrari who are actually the
Ducks gurus worldwide. So I really
strongly recommend you to have a look on
their website. And you can find some
examples of patterns that you can also
apply very easily on NAV data. Each of
these patterns is explained in details
uh with how you can create and most of
them are explained in the Excel context
but they're not so difficult to
transform into PowerBI uh desktop and
you can make use of all these kinds of
uh of patterns. Just have a look
dexpatterns.com. And by the way, they
also have a ducks form tool that you can
uh you can use and if you get the
possibility to attend one of their
sessions, that's really something I uh
recommend. Okay, so we have been
creating a number of reports until now
using the different tools that we have
have available. Now it's time to make
use of them in the PowerBI service.
Which means for example, I can go to
PowerBI.com and create a dashboard. the
different ways and how we can get these
dashboards created. We can make use of
the existing dashboards or we can just
upload our own and then we can uh do
that once we have our dashboards
online. We can even do a little bit uh
more. Now let me just quickly
demonstrate what we can do. So I should
have my browser open in here. What you
should be able to do is just go to
powerbi.com and then you can do a get
data. You can decide on power.com once
you have a free account where you would
like your information to come from. It
can come from a file from a database
directly from your organization. Someone
might have prepared that for you or from
a service. If you go to from a service,
there are a number of services in here
and also some very interesting ones like
NAV. can connect very easily to NAV uh
by using this get function. All you need
to provide is the the link to the URL of
your service tier and then how to
authenticate should work without a
gateway to can also work with a gateway.
Once you have that you can follow the
wizard and this dashboard will be
created for you. So that's one way of
getting data on here. Another way of
getting data on here is for example when
you have worked with PowerBI desktop. Do
I still have one open in here? Let's
have a look. I'll just open one again.
So I can start from learn PowerBI
desktop and
publish. There should be a publish
button available at the right
top. Just take a couple of seconds here.
Publish. It will ask you for your
account on power.com. Your report will
be uh published. Uh or I can just from
pub.com import uh such a file.
Everything that you create for example
in Excel can also be imported into
PowerBI desktop. So your power private
data model, your power view reports can
be converted into a PowerBI desktop
file. Once you have them available in
here, you can create your uh dashboards.
If you like if you are a person who has
created a dashboard and you'd like to
share that with someone else, you can
very easily do that by making use of the
uh share uh button. uh you can use an
email address of uh someone that you
might know in your uh organization and
just share your report with that person.
Sometimes depending on your own user
rights, you can also decide if that
person can only view or update uh what
you are sharing. This you can do with
the free version of uh PowerBI. Of
course, in the PowerBI service, you can
also upgrade to PowerBI Pro, which gives
you some extra uh storage capabilities.
Instead of 1 gigabyte per user, I think
it's 10 gigabyte per user online. If you
use the gateway and you go to the pro
version, you can synchronize one time
per hour, 1 million rows per hour. With
the free version, it's one time a day. I
think it's 100,000 rows per uh per hour
if I'm not not
mistaken. But with the pro version, you
also get the possibility, for example,
uh to view or create content packs. And
that's a little bit more interesting.
You can give a content pack a name. You
can share it with someone with a group
of users or with everybody in your
organization and you just decide which
dashboards, which reports, which data
sets you would like to share. And if
they also have the right to reshare, yes
or no, you can make that a template and
continue to work with that also in uh in
the
future. And then people will see this
reports uh popping uh popping up. So
that's very short, very briefly the
PowerBI service. You can upload your
reports on there so to speak. Once your
reports are on there, you can also have
PowerBI generate some insights.
Depending on the data in your data set,
the amount of data, the insights might
or might not be uh interesting. If you
do it, for example, on the standard
corners database, then the system is
intelligent intelligent enough to
discover that you sell actually more
pieces than boxes. But if you have uh uh
more data in there, it can really uh uh
detect some very interesting uh insights
and you can learn on your data and
discover insights which actually is what
the tool is is meant for. What you can
also do once you have uploaded your file
on porb.com is ask questions. So
depending on the names of your tables
and the synonyms that you have provided
you can go on the let's say the Bing of
powerbi.com just start typing in a
question you can say for example I would
like to see in this scale the sales or
show me the amount where the entry type
is sales sorted by customer or just show
me amount by customer the system will do
a search in or on your metadata and it
will present you the information how you
like to see presented it's actually
based on synonyms you can also provide
right on your PowerBI desktop file. And
then what what you actually have right
here is the red room of any manager.
When they ask you to create a report and
you ask them when when would you want
this report? They they always say
yesterday. Well, you can just say well
just go to the Bing of PowerBI tap in
the report you would like to have and it
will be generated for you automatically.
So that's one interesting feature to
have a look at. So the PowerBI service
is is online. And I just demonstrated uh
that. What I also want to mention is
that we also have the PowerBI mobile
application. Can't really de demo that
right now. It's also free. You can
download that on any device. Works on
Windows phone, Apple phone, Android, and
so on. And you can consult your reports
depending on uh your phone. You might
also be able to share to pin dashboard
to make some modifications, annotations
uh and so on. very interesting also to
have that besides the NAV uh uh mobile
application. So just some screenshots on
what you can do with the mobile device.
But and that's actually more interesting
uh once you have all of these bells and
whistles on.com and these very
interesting looking uh reports we can
also embed them in uh in NAV. So we can
go back and embed them into the
application and that's embedded PowerBI.
I also have some slides in a demo but I
think with embedded PowerBI it's more
interesting to start with a small
demonstration. So what we can do for
example is let me just go open my web
browser and go to NAV. So what I have
right here is a web browser is
connecting to uh an virtual machine on
uh on Azure and this is my data coming
from my database. Let's have a look here
at my uh sales uh people and my sales
people are actually interested to see
what's going on with uh certain
customers. So if I go here to the
salesperson purchasers, this is the list
actually in view modes. What I can have
a look at here is a
report which is uh being displayed and
let's say this is not really the report
I would like to see. I can click on
selected uh reports posted sales and
this might be of more interest to my uh
salespeople. I can have a look here at
my or PowerBI report coming from the
PowerBI service and I can see uh my uh
customers. I can see them by
country. I can click on them. I get all
of the interactivity that I see in here
and I can see for example the customers
of this salesperson are presented in an
aquarium who are the big fish the the
small sharks and so on. So all these
visuals are now also available and I
know also have them here in uh the
application. I can also do an expand of
this uh report and look at it in more uh
detail. I might not even be the one or
the person who created this report. All
we need is someone who publish it
publishes the report on PowerBI.com
shares it with me and then it can become
available here in uh in the application
and you can enrich uh your application
that's actually embedded PowerBI. Now
how does that actually uh work? What you
will notice is
that if you go here uh on your uh RO
center you might get uh uh depending on
the RO center that you are using your
PowerBI parts in the beginning it will
be empty and no reports have been
enabled with you what you actually need
to do is you need to follow a wizard and
when you follow actually that wizard
that should have that here on the slides
let's have a small overview you can get
PowerBI embedded to work so you go to
the assisted setup in the application
And there what you actually need to do
is set up an Azure Active Directory uh
account. So it works via Azure Active
Directory. If you do that a wizard
launches you can launch that starting
from the assisted setup or you can
launch it from the PowerBI part if you
have never done that. You have the the
welcome screen which we uh never read.
We click on the next button and then
actually to be able to get PowerBI
embedded working and up and running what
you need are two things. you need uh uh
an application ID and a key and that
application ID and key you need to uh
get that from Azure Active Directory. So
what you actually need to do is you need
to go to your uh Azure Active Directory
portal as an administrator. You need to
have the rights to be able to do that
and you need to create an application.
Now the procedure on how to do this in
the meantime has also been documented on
the new MSDN website which contains all
of documentation for now
2017 but it's not so let's say straight
uh forward to uh to do um I think in
this case if you go to the Azure portal
uh the procedure works the easiest in
the new version of the Azure portal for
example if you would like to get the
Excel addin up and running something
else which is new and the latest release
then the old classic portal might be
better. Anyway, you just need to go into
the portal, create a new application and
just search for your app registrations.
Click on add. You give your application
uh a new name and for example, Nav
2017 application type will be web API
because we will link that to our uh web
application or the web uh client. And
the sign on URL, all you need to provide
is a URL uh to your uh web client. At
the end, you need to append out landing.
uh HTML. Uh if that works then your
application will be created on Azure
portal. You can just click on it. Uh go
to the properties of the
application. Go to permissions. In
permissions we need to give PowerBI
access to the application that we are
creating. So unrequired permissions
click on the add button. Uh go to the
API give the rights to the PowerBI
service. All that PowerBI needs is view
reports. If you follow the wizard, it
will also show a bunch of other
permissions that you might want to to
append. Once that that is done, then you
will arrive actually in a blade uh keys
where the key is actually visualized.
You need to copy that key. It will only
be visible once. If you close the blade,
then you need to recreate the key uh for
it uh to become visible. So you copy the
key. Then you go back to the properties.
Application ID is the other one that you
need to uh copy from there. So now we
have a key. We have the application ID
of the application we created in Azure
Active Directory. And using these two,
we can then actually continue. Let me
just go back a couple of
slides and one next to enter them uh in
here. Once that is done, we only need to
do that one time. And if he can make
connection with PowerBI when the user
logs in with their Office 365 email
address and and password they will be
able using to use that that that adden
to fetch and connect to reports that
they can view on PowerBI.com. And the
advantage is that you don't need to
teach every user to be able to work with
the PowerBI service or PowerBI.com. No,
we can have a few persons creating very
interesting looking reports, assign them
to users and then they can just go into
the application and use that part on any
page and just fetch the report and show
it combined with the other data in uh
NAV. And to show how that works, it has
been plugged in to a couple of uh
pages. There's actually a page that you
can have a look at 9006 the sales order
processor ro center. You'll notice
there's a part in there and basically
it's a PowerBI spinner part. uh which
you can have a look at. You can maybe
even o also open the code to see how it
works in in detail. But that little part
is something you can also plug in in uh
any uh other uh uh page uh for example
like it did here with with the
salesersons. Once the tool is is up and
running it's very easy uh to uh to to
get started. Okay. See I'm running out
of time so I will not demo that. Okay.
So I tried to demonstrate a number of
different uh tools that we have in the
PowerBI tool stack. Um only had one and
a half hour to do that. We had seen a
lot of tools and the choice now is a
little bit up to you on how do I get
started but I still have some tips and
tricks and actually uh the tools look
very nice and are very nice to to
present and have a look at but it's not
the most important
thing. The most important thing is to
know how to get started. How do I get
started with PowerBI or any uh reporting
tool uh or reporting uh u uh project so
to speak? Well, we need to interview the
business users because in most cases the
person who creates the report is usually
not capable uh to really really
understand what needs to be uh shown.
Secondly, we need to understand what
information is uh is required uh and
interview the business users. So you
need to talk to the person for which
you're creating uh the report. Sounds
obvious but in in real life that's not
always uh happening. Okay. Once you have
that we need to try to figure out which
are the core numbers that you want to uh
display. Uh for example the overall
revenue number of units sold uh this
kind of calculation. What numbers need
do we need to have available in our data
model? Then for example do we need to
compare this with budget? Do we need to
compare that with targets? Yes and no.
Where they come from to be able to also
predict on short but also on long-term
uh in in the data set and the reports
that we will create. We need to try to
figure that uh that out. Then which
fields do I need to calculate? So which
fields can I get out of a data set?
Which ones do I need to calculate? How
do I need to calculate them? How do I
need to present uh these uh fields?
Where can I find the information? and
typical uh questions that you need to
ask yourself. Try to create an inventory
of all of that uh information. Try to
see if you also need to compare and so
on. So it's a process that you will need
to go uh
through. The most important part of any
reporting project, any dashboard that
you will create will be thinking about
and creating your data model. Your data
model is the basis for everything which
will come on top and on top of that
you'll have your reports and the reports
that you will create will contain a
number of components and these
components will end up in dashboards
that you will uh make but the most
important part is the data model getting
the data out of your data source data
sources into uh your BI solution and
then also think about how would I
refresh that uh that
information The best practice in my
personal opinion uh might still be to
work with some kind of data warehouse or
or cube that you use. You don't always
have to go for the on-remise solutions.
Microsoft is also coming with a SQL
server uh data warehouse which is
actually multi-dimensional database
which you can host on Microsoft or on
SQL Azure which is also very powerful
and the whole PowerBI tool stack is has
actually some capabilities built in to
very easily connect to uh that I
personally don't have much experience
with it but I know it's available uh uh
and it might be very interesting to have
have a look
at now what is it eventually The power
of PowerBI, I think the power of PowerBI
is that we have a tool set in which we
can find elements for everybody. If you
look at the business user and they will
be able to import their data wherever
it's coming from and then they can work
with that data in the organization. The
business analyst has a tool set at their
disposal to reshape to model the data to
do things that are difficult to do in
Excel with VLOOKUP and much easier in
the tool stack of of PowerBI or PowerBI
desktop. They can create stunning
visualizations and they can share the
information in in content uh packs. Uh
the BI professional is able for example
to connect to on-remise data sources uh
to uh actually have have a multitude of
data sources they can work with to
empower everybody within uh the
organization. And as a developer, there
are also some very interesting languages
to work with, but also some APIs that we
can use for example to integrate with
NAV or with other applications that we
are developing uh ourselves. We can
create real time live uh dashboard. So I
think there is something uh for
everybody in uh in PowerBI. whatever
that you will do actually or whatever
your role is in the organization, I
think PowerBI is the one tool which uh
is has the capability built in to bring
all data uh
together. Well, that was what I wanted
to uh present. I hope it wasn't uh too
much or too little on certain subjects
or you can always contact me if you're
interested in more uh information. So
let's see if there are any questions at
or any any not too difficult
