# NAV TechDays 2015 - Deploying and Managing Microsoft Dynamics NAV 2016 with Azure SQL Database

- **Source:** https://www.youtube.com/watch?v=uv6aicyk_nI
- **Video ID:** uv6aicyk_nI
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 99m25s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

Hello and welcome to this session about
deploying and managing Microsoft
Dynamics NAV 2016 on Azure SQL database.
It is too long
topic. My name is Alexander Totovich and
this is my first time to speak on Nav
Tech
days. I am in NAV more than 10
years. Currently I'm working as ERP
consulting director in NPS
uh one of the leading Serbian NAV
partners. In the same time I am
editor-inchief in ERP magazine. I am MVP
for Microsnamics NAV. In the last two
years I made a lot of how do I courses
uh video videos and few official NAV
courses and this is in short about me. I
write blogs. You can find my URL of my
tot blog and if you need my contacts,
this is my mail. You can write me I will
answer
uh not maybe immediately but I will for
sure answer you. Of course, you can find
my Twitter account and I call you if you
need something about this topic or some
other topics, you're free to ask
me. Today's agenda is short is
uh some basics and uh historical about
NAV on edge architecture. After that uh
I will present how uh we can manually
how we can uh deploy manually NAV on
Azure using Azure
SQL. After that how to prepare our
server tire and clients uh for using
Azure
SQL. how we can scale Azure SQL database
and on the end deploying using NAV on
Azure using management service portal
because this is something new and we can
make comparison in what situation we can
use manually deployment and in what
situation we can use uh management
service portal.
First short introduction NAV on Azure
architecture. First time actually we uh
when we get possibility to put NAV on
Azure was on NAV
2013 and we can be situation to use one
virtual machine to put NAV server web
server SQL or database server for
example as test environment. Okay. Uh we
can use this environment also for
production but this is not seriously.
This is only one virtual machine and
this is commonly used for testing envir
testing purpose. If you if you want
production environment we used two
virtual machines one for NAV server and
second for SQL server and NAV database.
This is something we used until last
version to NAV 2015 and it
works. Uh we had to know how to deploy
this using PowerShell it was not so easy
but uh we could use it but with uh NAV
2016 we got new
feature. Now we can use SQL as service
on Azure.
I think this is a really good feature.
Uh this is
uh we can uh save some money. Uh we can
uh get some better experience and I will
show why and
how. First why to use as I said it is
easier for using easier when we use uh
Azure as platform.
We have better price and less initial
costs. Pay only for what you use. And in
this situation, we don't need SQL server
uh to put on Azure. And we don't need to
pay virtual machine for SQL. We can
start with uh NAV on Azure. And when we
get first client we can run only this
one SQL service for this one client for
second client for third client we don't
need to use big virtual machine with uh
bigger
costs. Okay. If we use Azure uh with
Azure SQL server we have better
scalability and of course I will show it
as well. We have some another specific
features and we will speak about
it. First about
cost. I made one small
comparison and you can see this is uh so
uh price for a database S. So it is only
50 $15 per month.
This is for one small
client. This is not some big some uh
serious database. But we can use this
for some small client and it cost only
$15
US. In the same time, if you want to
prepare virtual machine for few
databases, we must invest $300 for this
virtual machines virtual machine. And of
course we must invest in SQL
license. I made one example. If we start
with NAV on Azure and each month for
example we have four new clients and
after five five months this is 20
clients and we can we can compare this
is about the same price three
$300. But when we make a monthly compare
and total cost it is not.
So you can see green is uh using Azure
SQL and blue is when we use SQL on
virtual machine on Azure. first four
months it is much less
cost and when we made total cost total
cost of using Azure SQL server is about
$900 but in the same time when we use
Azure on virtual machine sorry SQL on
virtual machine it is almost
$,500 and plus SQL license this is not
exactly uh uh cost compare but this is
uh some example with some typical
clients. We can see that uh it is much
better to start using Azure SQL if you
want to use NAV on on
Azure. You can make your own calculation
because I said this is not exact exactly
this is not so precisely I made some uh
example you can use this uh URL I will
show
you you have price calculator and you
can use it for to
calculate any kind of SQL database on
Azure just need to change what uh kind
of SQL database want to use for virtual
machine. You can
change again and you can choose a lot of
different services on Azure. You can
make your uh real calculation and after
that decide what is better for
you. Let's back
Uh this is not important only about uh
license pricing. Uh we still have some
another comparing.
For example, when we use SQL as on
premise, we have oblig we as partner or
client, we have obligation to
administrate all services for
application, database, SQL, server,
middleware, networking, storage,
everything is our obligation and this is
cost as well. When we decide to use SQL
on virtual machine on
Azure, our obligation is uh thinking
about application database but still
about SQL middleware and so on. But
Microsoft have obligation to manage
virtualization, server, storage and
networking.
But when we migrate to SQL on Azure as
platform, our obligation is to take care
only about application and database.
Nothing else. Everything other is
Microsoft and Azure team obligation.
Everything about SQL, middleware,
virtualization, networking, everything
is Microsoft obligation. And this is
pretty less cost. you have to uh to have
your own administrator for first and for
second uh variant and this is not
so this this is pretty
expensive in third
situation this is almost uh nothing
about about system administration almost
all IT people can work with
this and Now I will start with uh
operative
work. I will show how you can manually
deploy and manage NAV on Azure using of
course Azure SQL. First we need to
create Azure SQL
server. To do this we need to use your
our own manage uh Windows Aure portal.
If you uh all partners has um situ has
possibility to use this portal. I think
$150 or something like that per month
and you can make your uh test
environment your own test environment
and if you decide you can put your
production. You need create Azure SQL
server and after that we have to make uh
some specific configuration. we need to
add uh IP address for our computer to
the database firewall because uh of
security reason uh SQL on Azure must to
know that you have possibility to use
this
database and then when you get uh data
server on SQL server name you need to
prepare full create full database name
this is plus.database.windows.net
And in the f future you will use only
this name. And after that you can start
with deploy
database. To do this I already saw you
you must to
use window uh manage windows aure
portal.
You can find SQL databases here. I
already have some
databases and
choose
servers. I have my two SQL servers and
we can create one
new create and say add.
You must to choose your login
name and
password and must choose your region. I
usually use North
Europe. In my case, this is the best
performance, but I suppose in in
Belgium, this is the best choice.
And we need to wait few
minutes. You can see that database is
creating. Uh in the meantime, I will
prepare for my other databases.
I already say that we need to add our IP
address. Uh because this is my first
time to manage my Azure SQL for this IP
address. I need to add this IP address
for all my
servers.
And you need to go to database find
configure tab and you will get current
client IP address
automatically and just need to press on
add to the allow IP address. You can see
this is lot of IP address. I use it for
my company for my home and just need to
press and I can use this SQL server from
this. Sorry, we need to save
it. I will do it for my
second
server.
Okay. And I think yes, I already create
my SQL my new SQL server
measure. And you can see this is
very weird name D50 SD4 RR Y or MI I
don't see very well. Uh I didn't find
way how to change it. And we must use
this. You just need to go to
dashboard and you can find dashboard
name of this
database.
Copy to your
file and add
database.windows.net and
This is our
new Azure SQL
server. Okay, I will save it because we
need it
later.
And now I will open SQL Management
Studio.
And I will try to log to this SQL server
and this will not be
successful because I didn't
add I didn't add IP address my IP
address to this SQL server.
Now I will do
it
also. You can see this is empty and this
is first IP
address. And
now just a
moment. It depends of
internet speed. You can see we have our
our Azure SQL on our management studio.
Now we can um manage uh most of this
database through our management studio.
When we finish with SQL create SQL
server, We already finished it. Now we
can uh deploy our
database and we can use it on manually
on two different ways. I will show first
using wizard to deploy completely
database and after that I will show
another way when we use backpack file.
To use wizard we must use
uh our management Microsoft SQL
management
studio. We need to find s database
source. We we must to uh choose what
database want to deploy on Azure
SQL. After that we need to delete or all
Windows users for the this
database. This is very important.
Then we can start deploy
database wizard. We need to connect to
our Azure SQL
server set some specific parameters and
after
that I think 10 15 minutes I'm not sure
I will run it and after 15 20 minutes I
don't know we will check if this is
finished. We can check it in management
studio and Azure portal as well. But
before uh I
continue uh I prepare one potential
database uh deployment
issue. If you you have situation that
you can select only obsoles on Azure SQL
database web and business with the
maximum database with 150 GB and uh in
situation that that is uh there is no
option to select new service tires uh
basis standard premium this is big
possibility to find uh this issue you
just need to update your SQL 2014 14
with cumulative update
five. This is first uh cumulative update
could solve uh this issue. After that
everything will work
fine. Okay. Now we have connection to
our Azure SQL and we also need to create
connection to local
SQL
and find what database is our source. I
have only one database here and this is
Kronos database
NAV. You need right click task and find
deploy database to Windows Azure SQL
database.
This is
wizard. You just need to connect to
Azure
SQL. This is our name. We already
used connect. We can change our database
name on Azure if you want. and issue uh
I talking about was on
displays. You can see we can choose
basic standard and premium. This is uh
there are new tires on uh Azure SQ Azure
SQL but old was web or uh business. Yes,
web or business and you didn't be
possibility to choose one of them. I
will choose standard and after that you
need
to choose service objective. I will use
S1. S O is enough but I will choose S1
in this situation. And what is maximum
database in gigabyte
uh S as standard u enable maximum 250
GB. I think 100 is enough.
And you can
see this is wizard but system will make
backpack file.
system will run with deployment and make
uh backpack file temporary and this
backpack file will be deploy on Azure
SQL and but this is something we don't
see
and system will
work I hope it will finish until end of
session
We will
continue.
Now we need to create Azure virtual
machine for our NAV
server. To do this again we need to use
Microsoft Azure portal. We need to
create new virtual machine with only
Windows server. Okay. We we can have
more than only Windows server. can have
SQL server. This is no problem. But we
don't need it. We need only Windows
server on this virtual
machine. And after that we need to copy
our uh NAV DVD installation DVD to this
virtual machine. Install only NAV server
tire. Again as minimum we can install
more or you can use uh from gallery
micros dynamics and 2016 image if you
prefer it. You have everything installed
on this
image. I don't uh I don't want
to create now virtual machine because
this is really long time. I already have
a few virtual machines prepared and I
will show
you after we create virtual machines and
finish everything uh them. We need to
open client service port on uh our uh as
endpoint on our virtual
machine for external login to this
server and
I I create this virtual machines.
For example, you need to
choose end points and just
create new
And this is everything. You don't need
to make nothing
else. After minute or two, end point
will be opened.
Uh yes, if we you want to have
connection to Azure SQL uh with some
external computer not from your
computer. If you want to enable some
external computers to login, you have uh
to manually add computer name and IP
address to management
portal.
And I will show
how for example I
want to add for
this computer
And this is my IP
address. Now I need to go to SQL
database. Find my server. This is new
our new
server. Go to
configure. And now
You need
to put your computer name and IP
address. And now if you have SQL server
on this computer, we can also be
connected to Azure SQL.
Now I want to show how to configure
server and client configuration. To
configure NAV server tire, we need to
login on this virtual machine using
remote desktop connection. After that we
need to run PowerShell IC as
administrator and we need to use
PowerShell script. you can modify but
Microsoft published this par this uh
PowerShell scripts on their own
blog and we need to change some
parameters in this script to
work and just run
script after that we can check
results I will do it on one of my
virtual machines
run IC as administrator.
I will open my all my
scripts.
Okay. Sorry.
I said we need to change some
configuration in this script. For
example, we need to add our
username, our password. This is only
temporary
password and this is not some secret. Uh
you can put a path for your license file
here. This is standard part file when
you have from installation DVD.
You must find uh folder from your
computer, your installation
DVD. You can
see this is
my folder for
uh for installation DVD. Then import
module for
commandlets. After that again we need to
change server instance. We need to put
our database
name of our uh database sorry server
name name for our database and you can
see very similar data about username,
password, credentials uh and SQL server
and SQL SQL
database and I will run first to
import our
NAV command.
Then install Windows
feature. And now we need to make
encryption. To make encryption, we need
to uh make one uh folder where we uh put
our encryption
key. If we run this uh script without I
currently don't have this folder.
If you get
error just to
wait few
seconds and to see
maybe we finish with
What
is now we need to wait a few seconds.
Sorry, it was pretty fast. I'm going to
try few times.
I
know I already told that we need to
delete our Windows users but I forget.
uh problem was that I was already
deleted all Windows users but I prepare
new Windows user for this demo and I
forget it.
You need to open you need to check all
users in
property. If there are windows user this
is Windows user. Okay. We need to delete
it. I know anti
authority
is Windows user as well and I will
delete. Of course, you need to check all
users and delete all Windows
users. And now we can
standard
S1 and I
hope finished.
I expected something like this. And I
have another virtual machine.
Everything is perfect.
This is so slow.
Okay, I have this temp file temp folder
here and I want to show how it look like
when we have
not then when we
run we get of course error
message and we need to
create folder or create path where we
put this dynamic
skill. Okay, I
delete
and I did it.
And
now okay now we
have and I have already I think I have
already created this database but I will
try this we need to import we created
this NAV encryption
uh uh key we created
And we add our password and everything
we need. And now we import this encrypt
key to our survey instance to our N SQL
server with our credential to our SQL
database with all necessary
information just to see if
this I
don't of course we can continue
this we need to set any server
configuration to put our
credentials. Now we need to put database
name key and key value as key value as
our SQL Azure database.
Now we need to add database
name insert NAV server
configuration and on the end to enable
SQL connect
encryption we already
created. Of course we need
to restart our service.
Okay. And import our
license.
License. This is part of our of our
license. And we just need to import
And now we need to check results. To
check results we we need to
uh we need to check it in database name
in database server. Uh other database
credentials uh if we encrypted uh on SQL
server connections and so on.
And we can do
it any
administration. This is very
hard. I need fast internet.
Okay, this is our server
service
and we can see on database. This is our
Kronos database NAV 900. And this is our
server we
used
LIJ WDC and so on. Of course, we we have
enabled encryption on this SQL
connection, enable SQL parameters, and
now we have everything we need for
this
tire.
And if uh if we have u if we use
database we already used on our uh
computer. We after install NV client we
need to run trunket user personalization
user property access control and
user and after that we can run our
Windows client.
This is not so
fast. I want to
show I don't have SQL on this virtual
machine, but we need to wait.
We finished 92% on this
computer. It's still working. No
errors. I choose the minimum uh
requirement for this u virtual machines
because I have $150 per month and I I
cannot put uh a few uh CPUs and so many
RAM
and this is slow possible because of
that but this is
our client
Now how to configure web client? Okay.
Um this is Windows client only virtual
machine. Of course if we want to run
Windows client from our computer we need
to change u uh to NAV password from our
uh in config file. You must to prepare
certificate but after that it will work.
But for web client it is easier and we
have enough time to configure web
client. We already have web server
component installed. If we have not okay
we need to run installation DVD and
install them. We need to create
endpoints to web client again. As we
already put endpoints for ser for client
service, we need to put endpoint for our
web
client lo and login with different user
because uh I have domain user from my
computer and this domain is not on this
virtual machine. You can use
administration username you already
create use it to deploy this database
and create virtual machines or create
the same uh local user on your computer
as you have uh already create users on
this virtual
machine. After that you need to type
http your virt uh virtual machine name
and cloud
app.net at8 dynamics nav and so on. You
know what is bad for the
client. We need to go to virtual
machine. I use virtual machine too.
And we need to add new end
point
HTTP. I use AT80.
Okay, we need to
wait few seconds.
It still
work. Okay.
Now I can put
my
and already said I use my username I
already used to create this virtual
machine
and this is on nav tech server
to virtual machine I already used and of
course I want
to after that to show one
possible issue.
uh when you create when you open
endpoint for example at80 you can still
have problem that you cannot open web
client you if uh you have this situation
you have to go to your virtual machine
open control panel and in Windows
firewall open inbound rules and check if
we have Microsoft Dynamics NAV 2016 web
client with open port you need to check
local port if You if you have not if you
cannot open with web client this is
reason if you have uh just uh different
um port you can open properties and
change if you uh don't have uh this
service you need to create new
role I hope it is
open. Yes, this is our web client. But
as already said, if we have this kind of
problem, you just need to open Windows
Firewall.
Go to advanced
settings inbound
rule
and find microdynamics
nad.client you if you have but with
different
with different local port. You need to
open properties and change it. If you
don't have uh this rule, just need to
create new
[Music]
rule. Choose
port.
Next, put your AT80 port. I don't want
to continue. Give the name you want to
use.
Okay, we already finished with uh SE
tire and uh clients configuration but uh
I already said we have two ways to
create uh to to deploy uh NAV on Azure
SQL. I show one. Now I want to show you
another way using directly backpack
file. Again you need to use uh
management uh
studio. Again find nav data. If you
don't have backpack file first you need
to create to create you need to find
your database as source
and again delete all windows user. I
must to say this for me because I forget
it. After that extract data tire as
backpack
file connect and now this is preparation
for backpack file. Now we want to deploy
we need to connect to Azure SQL server
import data tire as backpack file and
again check result when we finish it.
just to see if this is finished. This is
not finished. And I
hope I will be situation to
do both of them in the same time. I
hope. Okay, I already have created
backpack file but just to show you need
to do it. You need to choose
task. Add extract data tire
application. Go
next. Choose name and after that finish
creation. Now I want to import this and
I will choose on my new SQL server
measure import data tile application.
import from local
disk. I will
use app database for my multi-tenant
environment. In the same time, this is
answer if uh because I I got a few
questions my blog if this is possible to
use uh Azure SQL in multi-tenant
environment. Yes, it is possible. It is
not problem.
And okay, we need to connect. We we
already have connection. We need to
choose database name. Okay.
Standard
S1
100. We need to check all data and say
finish. And now we can wait to finish
both of these.
In the
meantime, I will
continue when we finish with uh
deployment. Never mind uh what way again
we need to go to our virtual machine and
run everything
to to use our
database. Uh I already
have just to show to see what virtual
machine I forget.
I want to uh mount NAV app data. I I
will deploy on uh different uh SQL
server but I already have one deployed.
again to deploy. This is
uh basic uh the same uh PowerShell
script as you already used but with some
modification. And again we need to
import module and add our credentials.
Now in import nav encryption I already
have encryption because I created uh few
few minutes ago and I don't need to
create
again but I need to create new seven
instance I don't have
and I need to
Okay.
Everything is so slow.
Okay, I have one new instance and now I
will add encryption key to
this service.
I'm not sure what Okay.
credentials.
I tried it few
times. Sorry.
Hello
sir, we have recreated this new enough
service. Maybe you still not have set up
the
database on the
service in your PowerShell script. You
would like to yes configure the
application database name 19 app.
Isn't
it with the import encryption key? Yes.
But um it's still not configured in the
service in the multi 90
service. You've set up it with the
mouse. Yes, I set up it.
But this script need to add this
encryption to Okay. Sorry, just because
I need to add this
file. Sorry, I
didn't. Yes.
the same encryption key.
Okay. I I create again
uh yes I create again second but this is
not uh connected with this because
encryption key is just for this
database.
Okay, I will continue and on the end I
will I I will came back to show the
tenant because we have 20 minutes I will
try to make it on the end of session. uh
we need to uh to try how we can scale
Azure
SQL and to scale Azure SQL database we
can use service tire as or as basic
standard or
premium we can change performance level
and maximum size as we already you
already saw I use the performance level
SO1 S2 we can use premium or some
another and we can change maximum size
of all these
database. Uh if you use uh single
databases uh as service tires we can
choose basic and as standard we can use
SOS S1, S2, S3 and we have few premium
data uh premium service tiles P1, P2 and
so on.
The maximum of um database size for
basic is 2 GB and this is only for a
really small
databases. Uh for NAV you usually need
to use standard or maybe some big
project premium but standard is
uh well enough. In standard we can use
250 GB uh for databases.
If you think uh that NAV on Azure SQL is
for standard repeatability model
for pretty easy and small companies,
this is enough for
them. But if you want to have uh more
complex database, we need to we can use
elastic database pool. And in this
situation we don't need to manually uh
make scaling from S1 to S2 for example
or or or to S3. We can uh configure
datab elastic database pool and system
will automatically change uh service
tire. If system need more than S2 system
will automatically start with
S3. When we make some price comparation,
what is basic, standard and premium? You
can see that uh basic as already said
yes this is not so expensive but this is
only for small uh
databases standard is something
we generally need to use for NAV and you
can
see 200 and some dollars 400 and so on
per per
month. Okay, we can use premium but this
is I I think this is not uh necessary
for any
databases to scaling uh Azure SQL
database. We need to understand this
use. This is database transaction unit
and exactly mean this unit of measure in
SQL database that represent the relative
power database based on real world
measure. The database assaction of
course we have some unit of measure.
This is not based on standard
transaction and we can add uh some
number of dus to our databases. It
depend of them of this what we uh tire
use. If we use single
databases you can see we if we choose
for example S1 we can use 20 DT use. If
you use S2 50 DT use and this is single
model but if we use elastic model system
will automatically if system recognize
it uh needs more DT use system
automatically will change and use more
when you create database uh SQL server
on Azure you will get I think uh 15,000
DT use for completing server and after
that every time when you create uh
database you spend 50 100 or some use
for this
database to make your own calculation
you can use this uh URL you can put
your CPU's memory or ATC and make your
calculation what you really need to use
needs
And if you want to change this manually,
if we don't use uh elastic module
because elastic model is more expensive,
this is more comfortable but this is
more expensive and if you want to use uh
for less price uh model, this is better
solution to use single databases.
And for
example, if we choose one
database, you can go to scout tab and
okay, you can choose basic, standard,
premium. But by default, this is this is
standard. When we deploy, we use
standard. But
now we can, for example,
choose to put only S1 because we don't
need S2 for this database and we can say
this is
not 250 I need just 50 GB or something
like that every time when you do
something like that you need to click
save and
after few seconds you already finished
with the scaling this is not so complex
job
I think uh if you have not hundreds of
databases this is uh this is not complex
you can do it manually but if you have
hundreds more thousand databases okay
elastic databases it is a better
solution by default you
have just
When you create the databases system
automatically create
backups and you don't need to take care
about this but just to open
We finished with this
deployment. Everything is
okay. And of course with this another
I will show how how to check if
everything okay. But first you can see
all backups for your databases. Every
time if you want to restore you can
choose and run
restore. Choose what you exactly want
and continue. I don't want in this
moment to put
it just to open
our find our server. Okay.
Databases. This
is our
new and this
is yes this is another. We have two
databases created on
our new SQL server. You can also find
them when we refresh.
Yes, you can see Kronos databases and
NAV 90
app. Uh if you want to make copy of some
of your
databases, you can do
it. Of
course you can just choose what database
want to copy and choose
copy. By default you you will get copy
name. You can change name if you want
and find on what server you want to make
copy. Now you can have 10 servers and
find the database on one server and make
copy on some another. I will choose our
new server.
and system will
create. You can
see this is creating process of copy NAV
native
app. Now we talked about uh manual
deployment of U SQL databases on Azure
SQL. But we have new tool
uh management service portal for using
NAV on
Azure and this is a really good tool for
partners. uh partners are enabled to
manage all databases for our for their
clients but with some conditions. Uh
this portal can you can be used only in
multi-tenant environment not in single
tenant environment and you can you can
make your environment that you can uh
prepare your database and after that
uh not automatically but really really
very easy um deploy your your
application to your portal uh your
tenants your health file and manage on a
really easy way without any
administration work. You don't need to
know PowerShell. You don't need to know
some administration task. You just need
to uh use portal very similar as web
client on NV.
This is
portal very similar as I already said
web
client
everything can be used with mouse and
really easy. If you want to make new
service, you
can choose. You can say I want new
application
service and give
name. You can put your description.
You can change your description name and
you can put here your login screen
image, splash screen image and split
screen image narrow. You can choose your
brand and all clients uh who log in on
using this application service. You will
see your uh your brand on splash screen
and some
other. Then you can choose to put a
legal link, feedback link, privacy link,
community link, sign in help link. All
these links will be automatically showed
uh when client try to log in in NAV
using uh web
client
and it will be helpful and you can put
your license here just need to click
browse and find your license and
upload. If you want to use Office 365
authentication, you just need to
register just I cannot to
prepare
and I don't
want I don't want to save
it because I cannot prepare a lot of uh
services. If you want to see how to uh
deploy your application, you just need
to go to
applications and you can say
new
and everything. We need to new
add. I think I cannot make
more. When you
create you need to add
versions and in each version you can
using business logic you can add your
backpack file.
every time it is easy. Just need to
browse, find your backpack
and
upload. The same is for tenant data.
When you say when I say tenant data, I
need I think on tenant template because
we can uh upload tenant template and use
this template for creating u every new
uh tenant for new
customers and of course help
data. When we have everything
created and we want to add just new
tenant, we can say okay of course I want
new tenant.
to choose what
country you can put some
tags. You can add users for this
tenant and everything you need and after
that just uh use uh template uh for
upload and nothing else. This is really
really easy and almost
people can work on this don't need
administration
knowledge okay it uh it have more
additional features but this is just a
basic because I know uh you already has
had session about this management portal
I just want to show when you compare
manually work and using management
portal what is difference but
uh when We want to
compare this
uh manually and manually deployment and
management portal using when we use
manually deployment we can use it for
multi-tenant and single tenant
environment. When we use management
portal only multi-tenant
environment and when we use manually we
have only database as service everything
another is virtual machine this is not
really a service but when you use
management portal this is really
everything is service and this is much
easier for administration.
uh when we again when we want to use um
manually less we have a less initial
cost and we have a management portal we
have some initial cost and minimum 10
clients per year and I said uh initial
cost uh I'm not 100% sure about prices
but I think uh 300 something euros is uh
application service and you have 10
databases included in this uh price. But
this is something you must to
invest. When you have only one client or
two client, this is not so
cheap and you have obligation to
implement 10 clients in first year. This
is maybe
not so comfortable but this is a really
good tool and I will every time I will
choose them because when we uh compare
managing uh okay we need to pay
this,300 euros but this is a really easy
managing we don't need administrator
work we don't need uh one new one new
guy to work with uh this tool
But on other side when we want to work
manually I think we need some people to
work with uh Azure portal we need to
administrate to administrate uh any ser
database and application but when we use
portal we don't we need to administrate
only
application and
uh by my opinion when is better to use
manually manually is better when you
want to use single tenant We have some
specific client and this is not for
multi-enants, some specific development
and this is better situation to use
single tenant environment and maybe in
beginning when you have only one two
three clients to save some money because
it have less initial cost. But if you
have a repeatable repeatable solution
and you you have uh really easy clients
for implement multi-tenant environment I
every time I think that uh portal is
only one solution and easy managing is a
really really big
benefit. Again I made one comparison in
money because everything is money. And
you can see green is uh again this is
not exactly cost. This is some my my
some uh
calculation based you can see on five
clients, 10 clients, 15 20 so clients in
and all of these client has uh
by five users in the same time. Uh
really small clients and this is just
for calculation.
When we use management portal, we have
some initial cost. Uh I calculate cost
for u all all cost for virtual machine
for portal for everything for NAV
subscription license everything for this
for five user per client. This is maybe
this is not the same in all country but
this is uh pretty the same. Okay, we
have some initial
costs in this situation. And this is not
all about 100 euros when we don't have
uh new customers. But you can
see about here this cost is the same
after that
uh using manually is more expensive and
I didn't calculate
administrator guy cost. This is only
license uh and cost of Azure
subscription and about this I didn't use
user cost of
people and I think this is uh when we
calculate completely cost this is not
the this point I think maybe after five
six clients it is uh cheaper to use
management portal
and okay sorry
uh just to make wrap up what we talking
in this session we made small
introduction in NAV as Azure creating
new Azure SQL
server we deploy
completely NAV
2016 database on Azure using wizard and
extract uh data tire as backpack
file. Um I show some issues in
deployment process. Create Azure virtual
machine open client service port on
Azure virtual machine. How to register
IP address on server virtual machine on
Azure SQL server. How to configure NAV
NAV serretire Windows client a web
client. How to scale uh Azure SQL
database. Understanding the use and
using of management portal service
management service
portal.
Um all scripts I use but I first uh must
to see what is problem with multi-tenant
will be on my blog and
uh every everything you need. Okay, you
can ask me now but okay you you you can
send me a mail a question by
mail but now you can ask me any question
and I will I will again try to to see
what is the problem
with okay thank
you first
okay
for database. How do we do that for
maintenance?
for the SQL Asure
database. How can we implement uh the
maintenance on it? Rebuild index def
integity check update
statistics. As far as I understood when
I checked SQL Asia database, there was
nothing like SQL server agent.
you
know uh everything is managed by
Microsoft Azure team. You can uh use
dashboard to to see if you need to
change some tire and give more more DTUS
or something like that. But everything
other is managed by Azure.
when you were um connecting the
um the nav virtual machine in Azure to
the SQL server um you enter the IP
address of the Azure VM but you can't
guarantee that that's going to remain.
So what's your recommendations there?
The because um your virtual IP address
can change
uh IP address can change uh you think
when you add the IP in firewall. So when
you put the IP address
into sorry when you put the um IP
address on your SQL side your Azure SQL
side of the client um which was your
Azure VM with your nav service
running that IP address of that virtual
machine can change. Okay you you need to
change this again portal so you'd have
to monitor all the time but you you
don't need you don't need to add the IP
address for regular work only if you
want to uh connect from this virtual
machine on SQL server if if you have SQL
management studio for example on this
virtual machine and you want to to
enable connection for this virtual
machine to this database in this case
you need to add uh this IP address if
you don't need this requirement you
don't need to do it okay
Um, how do you know how to scale the
Azure SQL server? So, do you start by SO
and work your way up or what do you
recommend? I re uh um first everything
depends of client type. But if we think
the about Azure SQL and NAV that this is
for standard
implementation really really
repeatability model with 99% of the same
objects. This is pretty the uh the small
uh clients. I every time recommend SO
and you need to monitor if everything
works fine okay you you don't need to
spend more money but S or S1 is enough
by by my opinion for for
uh in in start so after that S1 when
when you when you see in dashboard but
so is enough
um at the
We saw the price for the SQL server on
Azure and the um full virtual machine on
Azure. So, but at the price for the SQL
server on Azure, I think
there's there's an additional price for
the VMware for the N
service or it's included.
No. Uh you asked for a license and not
the license. We saw the the initial
price for the SQL server on Azure was
$15 a month or something like that. But
um the good machine for the service
that's additional or not. Yes, this is
um price I think for A3 model. I I
didn't use the the most cheap variant
because uh it can work only on one or
two uh databases. But you can use
calculation
later and uh and see what is uh for your
example. If you have only maybe two
databases, okay, you don't need 300
dollars in virtual machines, but uh if
you need if you need 10 databases, you
you will need it for for sure. Thank
you.
Uh I have one technical question about
uh
SQL on Azure limitations. Uh let's say
it's from my
company experience right now we have
come some customers which have uh some
external uh integrations which been done
on the SQL server directly. Uh but for
this reason some uh let's say external
ports should be opened. Is it possible
to uh manage uh SQL server on Azure
because when all those ports which I saw
you are opening it's uh on the client
let's say side and
aes SQL ser is based on on some
additional layer
somewhere behind addition
firewalls. Is it possible to
it it it has some limitations but
uh when if we want to make standard
development we can use standard uh Azure
SQL for development this is no problem
but for some integration direct SQL
it has some limitation. It is better to
use web services if you can but it has
some limitation but um again as SQL
uh by my opinion I cannot speak in
Microsoft name is u the first place for
small
companies really for I I speak currently
okay for two or three years I don't know
uh it's possible it will totally
different situation but currently this
is for small companies
uh for small price and not for some uh
comp not only big for some complex
company complex business processes for
integration. This is not for this uh
business. This is just my opinion. Thank
you.
here.
Um, is it possible to use um the the
client's existing uh active directory
domain to authenticate against on Azure
SQL active directory uh standard active
directory? No, I didn't try to use Azure
Active Directory. I know it can be used
but I didn't try but standard active
directory it cannot be used
the database size that you set what
happens when you hit the size limit does
it does the database stop functioning or
do you get a a warning saying it's
reached its limit so you set originally
set what's 100 gab say database got to
100 g does the database stop function
you you can use for example 100
gigabytes and change 100 GB. Sorry, what
happens when it hits that limit? You can
change to 150. Uh if you get a warning,
if you use uh standard, you can uh scale
from uh I think 20 gigabytes to 20 to
250. If you and you can scale um and uh
make bigger or less, this is not
problem. But if you need more than 250
gigabytes, you need to change to premium
or packet.
But do you get do you get a
warning like on the management?
You you just you just need to open
management portal and change it and
save. This is only uh in in standard uh
environment. This is only few minutes
job. You just need to to change uh size
and press save and nothing
else.
Excuse me. I want to know if you have
any experience with the other things in
SQL server like store procedures.
Can we uh like upload them through this
backpack files and then make them
automatic through the portal or they are
completely manual?
Uh you if you want uh ask me if we can
automatically uh deploy. Uh my question
is that I do not have a good impression
of these backpack files. I don't know
what they take out of database. Do they
also move a store procedures and views
and
uh I don't know if this is possible as I
know only with back file you can use
visa but again this is backfac file if
you use management portal again this is
backpack
file as I know only backpack file maybe
f future but currently
Um, you set up when you set up the SQL
on Azure, you also added the service to
your IP, but um, can I also assign it
then to when I have a my own network on
Azure? It still an island where I always
have to open it the security or can it
also be part of my SQL as a network that
every uh I I have in my in my company I
have p private network when I add uh IP
system will add uh external IP address
not internal and you don't need to give
IP address from your for your computer
just for your company external my
business. But if I have an does this
mean I always have to leave my Azure
network and access the SQL from outside
so that it's a dedicated island let's
say like this. If you want to uh use
outside your company you just need to
add new address and after that when you
finish you can delete this and this is
no problem.
Yeah. So right now you set it up that I
always have to go over the internet but
can I have it inside my
when you have uh inside but you still
have to use some virtual machine measure
when you have a yeah in my network in
aure
I don't know I don't know uh I will
remember it and I will I will try to
give answer on my book this is good
question I I don't
know. Thank you. I will I will try to
make this multi-enant and I will put
this video on my blog. Sorry.
