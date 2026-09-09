# NAV TechDays 2017: PowerApps, Common Data Services and Common Data Model

- **Source:** https://www.youtube.com/watch?v=T8o-Eq2XzcA
- **Video ID:** T8o-Eq2XzcA
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 86m10s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

good morning everybody and thanks for
being here you are very brave people
yesterday I learned two things if you
drink beer you have to eat as well and
if you present at 9:00 a.m. you have to
bring your laptop back to the hotel room
so fortunately Belgian people key can be
trusted
so my laptop was still here when I when
I arrived here this morning so we are
going to talk about you actually learn
something
he never learns so we are going to talk
about power apps common data model and
commonly the services but most of all
today we're going to talk about
connectivity because we live in a world
which is constantly changing and
everything that has a power plug also
gets an internet connection and in order
to handle all that connectivity I think
we have to change our mindset so today
we'll talk about how power apps common
data service and common data model fit
into that model and also where nav fits
fits into that so Michael you want to
introduce yourself yeah so I'm back on
States I used to do the keynotes old all
the time together with Luke in the old
days my previous job was Microsoft but
since two years ago I started from F and
I'm back to coding again so we actually
see me code on States so you can be the
judge if this is successful or not but
at least that's I'm backward to my roots
back with you in the crowd so yeah and
Microsoft
also invented CL a long long time ago
right so I know I did so a mark and I've
been doing an AV since it was still
called Navision started in 1997 and I'm
actually going to use the version that
I've been implementing or buying back
then for the photo presentation today so
if we look at the agenda we're going to
talk to start with
a quick introduction about the building
blocks and the concepts then I'll going
to do a power reps demo then michael is
going to show common data model and
common data services and then we'll have
some examples of how to use auditor for
in combination with C sharp and Al and
then we have Q&A
the idea is to spend 50 minutes on 115
on 2 and 30 minutes on 3 and then
something like that so we actually have
some time left for Q&A we have the
t-shirts to give away the Antwerp
t-shirts but I also have a whole bunch
of nav skills t-shirts that if you come
here back down on the stage after the
session you can actually grab your nav
skills t-shirt out of the box if you
want I'm not going to bring them back
home so today no marketing demos no
licensing we actually don't know
anything about licensing so please don't
ask us what all of this stuff cost we're
just going to try to focus on technology
and make make make try to make you
understand how all of this works so most
of us have been with anythi for a long
time and we all think that in the center
of the world we have a seaside we are
all experts in Seaside and we've been
using it for a long time when we have to
solve something we solve it in Seaside
with with CEO and most of all most of us
think that seaside is this like big
hammer that can solve everything
some of us even think of of seaside like
this right it's a really powerful super
mega tool but in fact if you really look
at seaside it's basically like a rubber
hammer Microsoft is restricting us from
making a lot of mistakes and it's really
trying to guide us from from from
preventing making mistakes right so we
have to start expanding our horizon in
this in this changing world we have to
get out of our comfort zone our comfort
zone would be typically that we have
seaside
in the middle of our comfort zone this
is what we have been using for a long
time and we have to start learning we
have a lot of things that we need to
learn one of them of course is Visual
Studio code but we also have to learn
power apps and we have to learn how
Microsoft flow works right for example
right now if we send an email where it's
nav we all use code unit 397 but if you
use power ups and flow that cochin it
can actually be discontinued it can
actually send the email using flow right
the same goes with with EBI
we always all have tools that download
stuff from FTP and SFTP and we do that
with dotnet Interop in Seaside but you
can necessarily do the same with flow
right so all these objects can actually
be replaced by by other technology that
you don't have to maintain then we have
the the danger zone this is where
Michael gets in this is where asp.net
core is this is where angular is this is
where all the frameworks are that young
people are are using right and this is
where all of this technology gets
together and you can actually leverage C
D s and C DM
in order to get this connectivity to to
work so life begins at the end of your
comfort zone for me it was a very steep
learning curve Michael said oh let's do
a session about C D s yeah okay let's do
that so I actually had to learn all of
this stuff from scratch during the last
last couple of weeks and I'm just going
to explain to you guys what I learned
from from all of this so we all put nav
in the middle let's actually replace it
with something more modern so we put an
IV in the middle and then we start
connecting an AV to all kinds of devices
but we always use an AV as the central
point of everything and then we start
connecting and everything ends up in the
nav sequel database using web services
and everything is connected
but I think we should change this this
idea I think we should move a navy to be
just one of the other apps and I think
if you really want to connect everything
all these devices will start talking to
each other all these all these devices
will have Web Services and instead of
having a navy in the middle we should
start thinking and were considering to
have CVS and and power apps and and flow
in the middle of all of this so the way
Microsoft explains this this platform
it's a business application platform and
it consists of of three pillars and a
couple of different levels we have power
users and power users are what we in the
Navision world would typically consider
consultants who know how to do a little
bit of programming people who know how
to make changes to the UI or maybe even
a consultant that I can actually connect
to code Judas together and remove the
confirmation dialog in between and then
you have the the pro developers and
those are the architects those are the
people who actually make posting
routines and fit everything together so
it actually becomes a workable
application on on the bottom of that you
have a common data service and go and
connect this in gateways and for the
power users we have power bi power apps
and and Microsoft flow actually I think
I heard somebody actually yesterday say
power flow that would actually make it
right so power bi power apps power flow
and for the IT pros we have pro bi Pro -
with Visual Studio and improve
integration with logic apps right so
today we're not going to cover power bi
Steven covered that last year if I
remember correctly we are going to talk
about power apps going to show you a
little bit of that so power apps can be
considered like the pages that we have
right now it's the new UI that's built
on top of all of this connectivity
Microsoft flow is like workflow
it's allow
you to connect stuff together so if
something happens then something else
should happen and all of these
applications that use flow have the same
type of connectors so everything
understands each other and then you have
the pro def which can be considered like
okay that's what we call code units I
had a hard time mapping logic apps to
something so I said invoke maybe that's
processing reports but it's also where
you do coding and then a common data
service is where your data is right this
is where you would compare it to two
tables and then a common data way
gateway is its Web Services so
everything starts with Widow data if
your application understands Oh data
then you can connect it to all of these
good stuff then we have a vicious video
code that you can use to create your
business logic or you can use the full
visual studio if you want to if you
prefer to use that and then you add
html5 to the front-end all business
applications these days have html5 user
interfaces and that should make
everybody everybody happy you can code
in any programming language that you
like you can go to in C sharp or
typescript or in nal but basically the
programming language is not important
anymore and you can connect different
applications with different programming
languages you can just use whatever you
want to whatever you want to use and
then you have earth overthrew and that's
basically the security glue that fits
everything fits everything together so
let me start with with with the demo how
do you demo something like this right I
watched a lot of YouTube videos on power
apps and flow and there are a lot of
demos that you can find on how to
connect things together on how to
connect the name x265 to to power apps
but I figured well all of you guys can
actually look that up on YouTube
yourself and you can actually do that
and I think it's my job
to make motivate you guys to actually
start doing that so say okay what can I
actually show these guys that I will
probably not find on on YouTube right so
I decided to connect Novation financials
version to the version of Navision that
I bought in 1997 and see if we can
actually connect that to power apps and
how that would how that would work
right
so this is Nevisian financials who has
worked with this version a lot of hands
we love it right so actually the the
benefit of Navision financials version 2
is that it actually runs on Windows 10
you don't have to do a technical upgrade
to a new platform in order to actually
make it make it run but for this demo
what I actually did is I took a native
backup from my database and actually
restored it in an AV 2009 r2 on sequel
server and the reason for that is that I
had to somehow expose an audio web
service from this write power apps and
and flow expect a no data connection so
I'm going to show you how I actually did
that and there's did several options I
just picked an option that I could get
to work so the thing that I actually
decided to do is in in sequel server I
have created a view on the table
I have create a new table and Ivy Tech
days attendees and I expose the data
from this table as a few the reason I've
created the view is that I have to
remove the timestamp fields which nav
automatically adds the timestamp field
at least from what I experimented with
if I try to wrap that in an audio a web
service it doesn't really like it so
actually the the data is showing without
the the timestamp field and the next
thing that I that I do is I go into
inter visual studio this is the danger
zone right so in visual studio I
actually create a new project and as a
project type I am choosing a visual
c-sharp web and I'm going to pick
asp.net web web application
let's call it an even take days
real so this is for real and I would ask
me what kind of app do I want and effect
the azure Web API because what I'm going
to do is I'm going to use edger and
Azure is going to create an API for me
that I can call from any device anywhere
right so now it's going to create all of
the plumbing for me and the next thing I
do is I have to add a model I'm going to
create a new item and now I'm actually
going to connect to my sequel server
database using an ad Oh dotnet
connection call it nav tech this DB ad
and I'm going to generate the code
automatically from the database so I'm
going to tell which database I'm going
to use and this is where you have to
tell a sure which machine you're going
to look at this is where in my first
attempt I put in localhost but then if
you publish it to Azure I sure cannot
find it right yes it actually connected
to your a sure machine so in this case
I'm going to use the IP address of the
azure machine by using sequel server
authentication
that's connection connection successful
all right so it's going to use this
connection from asier into my database I
also had to open port number 14 333 in
Azure so that as you can actually
connect to sequel server it doesn't have
to be 14 333 you can actually use
another port as well if you if you
prefer and now I can select my nav tech
days database this is just a demo so
security is not something that we're
going to worry about today maybe this is
not smart to do this for your for your
real customer but in this case we're
just going to do that and now I'm going
to pick the nav tech days power
apps database and it's going to generate
some some c-sharp code this is way
outside of my comfort zone but I could
going to show you what it's it actually
did you can see here in the in the error
message in the warnings that it said I'm
using a sequel server view and I can
read from a sequel server view so I
actually can get data but with a sequel
server view I cannot actually put and
post that batch data right I could make
that work but that's not for the scope
of today's demo and it automatically
creates a class based on my view and
it's going to use that that class to
expose the data so the next step is I
have to add a controller and we're going
to do that with a scaffolded item no
idea what the difference is do you know
the difference between an item and the
scaffolded item no idea so we're going
to use that we're going to use web api
to controller and now i made a mistake
because i actually have to build my
solution first building the solution
will actually build some metadata that
actually this guy depends on
builder succeeded now I can actually add
careful the item Web API to controller
going to use the this one this one just
call it nav tech days controller use
async so now it's going to build more
code for me until now I have not
actually written any code myself the
only thing I have to do now is
electrically have to search in my code
for something called swagger we're going
to create a swagger API and swagger is a
language definition for for building
OData API so I want to search for that
and what I can do here is can actually
enable the swagger UI and now if I do
that and I actually test my solution and
the demo gods are nice to me today I
hope they are
so now I have to add the swagger end
point and what I have now is a a no data
end point to my sequel server view I can
actually click on my nav tech days and
now I can actually use the get statement
try it out and now I actually get the
results from my division financials
database in my API so now the next step
would be to to make this public right
now it only works on my on my machine
now I actually have to connect it to a
sure and a zero is going to make sure
that from anywhere in the world can
actually can connect to this API and
then Azure is going to go to my sequel
server machine in order to do that I
have to I have to build it and publish
it so I can actually publish this and I
can actually connect it to my Microsoft
Azure app service I'm not going to do it
right now because we're actually trying
to be efficient on time so I actually
prepared this already so here we have my
measure account and in my account I have
published my API and you can see here I
have my Novation financials web and this
is actually the endpoint that Asscher is
published for me and that I can now
start querying from every machine
anywhere right so let me go from my
virtual machine to my local machine I
actually wanted to start this
presentation with the Fellowship of the
Ring but Michael didn't think it was a
good idea I hate it it's like it's in
the Shire and everything is green and
everyone is lies and we have seaside and
bla bla bla bla bla and then the ring
gets out right one ring to rule them all
and then everything just turns upside
down that that's what this guy is doing
to us as well so here we have Navision
financials web dot as your web sites the
net and then swagger UI and here we have
the same swagger but now it's not going
into my local machine but now it's going
through Asia to the azure VM and now I
actually have the same data in on my
local machine right so now the next step
is to see if we can actually use this in
a power bi so let's see if we can do
that so let's go to our apps and I'm
first going to show you the result and
then I'm going to explain how I got
there
so we have the nav tech days power app
app and I'm not using any of the fancy
uy that you can do with with with power
apps I really hope that when you get
back home that you actually go and watch
these cool YouTube videos that all of
the cool stuff that you can do with with
power apps but if you have been with
Nevisian for a long time and you still
feel that with the role to the client
you are limited because Microsoft only
gives you five colors and you're not in
control of where you can put your data
right power apps is solving that with
power apps you can put data everywhere
you have all the colors and it's really
it feels like you are back in the
Navision client so here we have the
power app and we actually have the the
data from Novation financials
so let's actually add another attendee
we'll go to new vision I will just add
someone else I know that my daughter is
in a room here so I'll add him and he
works for from Dyk from Holland now
let's refresh the power apps and cross
the fingers
everyone please cross the fingers and
he's in powers right cool
so let's close the app and actually what
I did
I had to create a custom connector the
custom connector allows you to import
the definition from your swagger API if
I go to my swagger UI I have a special
URL which is called swagger sled-dogs /
v1 this is a JSON file you can copy this
JSON file to notepad and then import
that into power apps and that gives
power reps the definition officially you
have to clean it up because this wagon Y
also contains put patch and delete and
the sequel view doesn't support that so
you have to clean it up a little bit
before you actually do that and then
after you have done that so here I can
actually edit the connection and then
test the connection test operation and
now we get started 200 then we get the
same data let's look at the app yes
that's okay if you take this edit
this is where I should sing and dance or
tell a joke
please mark - here we have the the table
which is my control and you can see that
this table is connected to navigate
financials web which is my custom API
and it actually is using the the get
statement on the on a swagger API so I
hope that you agreed with me that this
is a cool demo right connecting
something from 1997 to technology that
nobody could ever dream of back then
don't try this at home
I forgot one very important thing which
is security and the main reason for that
is my edger account is connected to my
outlook comm account which doesn't have
Azure Active Directory and my power apps
is connected to my nav skills account
which doesn't have an azure
subscription right so I actually forgot
that so every one of you could actually
query that endpoint right now and get
these six attendees back from the web
service right so let's wrap up and then
we'll give the stage to Michael and it
will show CDM and CTS Microsoft flow and
power apps it's a new suite of
development tools it's designed in the
cloud it's born in a cloud solution and
you can actually start connecting all of
these Internet of Things devices if as
long as they use all data
everything can be connected its workflow
and event-driven based on old data and
both using a common data model and
services like Michael will show you in
in a minute
you can code using Azure functions but
you can actually code using anything as
long as it goes into
a connection using using all data so I
made a very quick comparison to between
power-ups and the nav web client when
should you use the web client or the
phone client and want you to use power
apps power apps has a way more flexible
controls yeah the web client and the
role to edit Lyon still try to force us
into like this structure that Microsoft
thinks works for everybody so you really
have a WYSIWYG design native modern data
items it has way more controls and nav
is doing you can connect it to an
endless amount of apps it's it's
designed to be connected
it has offline capabilities but I have
been told that that is still in the like
playing a round stage but there's a
hyperlink on the slide if you can click
on it you actually go to a website that
explains it and the community I mean I
love you guys and the Novation community
and we are great together but the the
community for c-sharp and and power apps
and azure is even just way way bigger
than the nav community with the web
client you have the UI which is bound to
the database the advantage is that you
have native office integration right in
a vision just natively connects to excel
and word it's only online but it has
transaction integrity to a section
integrity is hard with web services and
the web client of nav is accessible
outside of your Active Directory with
power apps as as far as I know the
information I have you still need to be
part of the Active Directory right so
you cannot use it
for people who don't work for your
company unless you want everybody to be
in your ad key takeaways it's easy to
get up and start it it's connected to
flow it's definitely not a replacement
for ERP it's it's something new for
solving new challenges I think it's
something that every nav developer
should know and should be aware of and
it's not limited to nav 20:18 customers
right with Azure and c-sharp and swagger
you can create an endpoint
I used a view on my sequel server
database
but you can also use a CSV file or an
excel file or you can convert a soap web
service to a no data web service
anything as long as you you convert it
right so timing is perfect and test
again yeah so what did your soul was not
just a bunch of technologies but you
also saw a guy mark who lived his whole
life in Seaside actually now within a
couple of days long long days actually
pull it off and created all this new
technology so I think mark is one of the
smarter intervie developers or maybe
these modest but it also shows that
everybody can take this journey into the
new world so should we gave mark and
applause so let's look at the common
data model and also the this common data
services platform that sort of the thing
around is always Microsoft is fantastic
at doing these marketing slides and when
I first saw it I asked my friends at
Microsoft oh this is Project Green and
say got this anchor loop notes not and
those of you who remember back was that
Fairy Queen was about creating this
common data model and creating a
framework on top of it and I was part of
that and we spend a lot of money and it
burnt down it was closed but this is
something different than you so hope
it's successful this time but it's if
people remember back it's sort of the
same thing sorry for for saying that so
also with something like this it's not
funny at all so cause 2 billion dollars
the promise here and promise always hard
to keep so let's dig into a couple of
these to see how this actually works but
leave something that that works is that
it's extremely easy to provision so we
should try to sign up on power apps it
takes you maybe 20 seconds to get in and
get a database you can even put a
database on your onedrive so and if you
ever try to pull up a full interview
solution untrimmed with C was ever
anything you
I put that on the cloud afterwards it
will take your day mo but also even
though this is fantastic I also saw that
the if some of you have probably looked
at the expensive that nav has done for
office and that's actually faster so you
can deploy deploy a Asia nav solution
now in seconds so actually any be
speeding this promise up then the other
promise is a common data model I'll look
into that and and also there's a data
access layer that's a search to the SDK
and I'm going to also give you a glimpse
of how that works and how to work with
it so let's look at the common data
model and looking and these models
always sort of Archaeology because the
people who create these models always
come from some where in the world and if
you look at these entities you you can
see ah this is from CI m and this is
from a X and paste it as some foundation
classes which is great because I always
wished I was this kind of class in in
Seaside's where you have an address
object and account IDs can't thing but
it doesn't exist and it's still not
there but those kind of things exist in
egg from day one and also in cm things
like customer service of course come
from cm and then somebody aspect the egg
seemed did a sort of rock structure a
push where they quit or structure for
sort of embracing companies with
hundreds thousands of employees and that
ended up in hand CDM as well so that's
basically the you get the full meal for
lesson and then there's the sales and
marketing and things that come from cm
as well that's that's rather lightweight
but still really powerful to do these
kind of things so so you see the
heritage of this if you look into them
and you'll feel right at home
the problem here is however if you come
from a navy there's nothing the nav guy
was not in the room so they left you out
mark sorry but of course like any other
framework you need to have custom fields
and custom tables and you can add this
in using power-ups and it's it's really
good simple to do this as Mark said
YouTube's vision it's really powerful to
do this so it's it's a really great
experience in empower I have to to set
this in but let's I promise you to look
at some code
so please switch marking yeah I'm wrong
right one so directly what always beats
MSDN is to open visual studio and
actually look at what's in there because
that's that's the perfect truth and MSDN
is sort of the handle last year's true
so but let's like take a look at this
and this is the whole sales or entity in
there it's it's really simple so it's
back to where anyway was many many years
ago in terms of complexity so they left
transfer stuff out that we have an enemy
today but that's good because that's not
the paper that you have to have
something that symbol that also can be
used across all the applications and you
have know things like addresses in here
I can click into this so my mouse left
the building
and I have a nice address in here I also
have things like coins in here again
something that's I would love have seen
in interview many years ago where you
have the amount and the county code in
here and this can never be blank that's
my hate thing and interview today that's
why I understood we construct the the
concert code should be blank 25 years
ago but that's what people you have to
live with today but that's not occasion
here so these things are pretty good but
that's it actually other systems like
Salesforce they they're using the enemy
model where you don't have optics
because having optics in West based web
services gives a lot of heifers because
you don't want to have these and these
classes and you want to have a flash
talk so if you look at the the financial
force API they have exactly the same as
nav so everything is completely flat so
so they also going back to basic and
always could be that time Browns now so
seems like he learned something from
from being at seem so but also these
models have issues we have talked to the
serum team but they have not listened
that greatly so far and actually we try
to create an invoice report on top of
this but the problem is that you cannot
sell to somebody and ship it to somebody
else because there's only one name down
here so it has to be a sort of the the
same company different addresses but you
cannot do the thing you usually do today
while you're actually shifting to
somebody and send the bill to somebody
else that that cannot be done also if we
do down into payment terms so in a nav
of course everybody knows that payment
terms is determined by a adders
expression and then you get sort of a
data out of it so what do I have in here
is sort of I think this must come to
come from cm that you basically are
stuck with these options in here so and
this sort of gives it a
you have a pretty hard time of mapping
your beautiful nav ex-patient into into
this and there's no way around it so I
hope this will be changed in a future
model so but otherwise this is entity so
you also have the lines down here which
is also pretty good and you can you can
work with this and get sort of a fully
industry but this is again and we caught
up on this so if you saw the OData fall
or the the API session yesterday with
honest last and other people nav is just
in par with this already and you can do
beautiful things for this so let's move
on to the impact to the slight market oh
wait a second so so and sorry about that
so just wanted to show you what I made
with the organization I just put this in
to get a hook into this so I can go to
the definition and basically the the arc
stalks and here's something that's
taking out of X so you have parent
organization and you have several
networks where you can select between
Twitter you have its stock ticker and
all sorts of things so this this is this
can do anything so compared to this azor
Ahai which is really simple this can
sort of do any correlations in the full
world's and that's what it was created
for so but I'll come back to what the
issue is here so thank you so you know
there's a lot of cool things that
there's some issues that hope will be
fixed in the future so there's this
abstract level difficulties between the
arc structure and and other entities so
the instance come home see em are pretty
simple and easy to understand where
something like the or structure is sort
of out of program out of the league in
this world so and also the the enum
saying you saw the payment terms but
this is actually for a lot of things
also freight and
and other insole in that it's edom it's
just not cutting it to to do dates
so that's another thing that's broken
then there's the thing I miss about the
missing names that for the addresses
which is also something of course you
can do a custom feel in there and I'll
show you how to do this but sort of it's
not part of the tomorrow and then of
course that's the whole idea that's just
like CI m integration that you you want
to sync your data in this model with
enemy for those of you who ever worked
for synchronization you you you know
that first of all it's bad career move
to work in these kind of things because
it no matter what you do you you will
fail I promise you that so that's an
advice but having two masters and
two-way synchronization is asking for
trouble it will never ever work no
matter how many books you read and I
think we we try that with any video over
there so again it's a bad fit for the
Naveed tailor more because things are
just not fitting together very nicely
and then also there's a nice security
model and envy where you find people
from reading things and and and doing a
lot of things that's perfect that's
perfect over many years when you're in
true CDM it has its own security model
and whatever you synchronize over there
you have to set up security over again
and it's not doing the same as nav is
doing so okay but it's very easy to
download to see them their own data
models also I'm immersed in if you don't
want to go into vicious duty so I
encourage you to go and look at it
because even though it's not done it's
it's going to be the future but let's go
into look at the common diseases SDK and
see how that looks so can we switch back
max thank you so actually before taking
I'm going to sort of show you and easily
how easy it is to create an array der
Hooven so in a week just to compare the
two worlds so in this case I'm going to
to start with use to you 2015
because unfolded this requires a bit
more plumbing in 2017 we don't have the
time for that but it's so easy in 2015
that's anybody can can do this so so
create a new project in here it's
console implication I don't care what
it's called this time so fantastic
activity log so I think I'm alive so
good then what I need is that I need to
go into enemy what I got and just get
the orator you will for anything in here
to to get hold of biking web service sir
then I'm going through the references
and add a service reference in here
it's Aguila just got in here and I need
to get rid of in everything back to the
OData thing please go now it basically
goes to nav and it gets the schema
definition for everything I'm going to
call this table okay
and now behind the scenes Visual Studio
is creating the net classes for all
these enemies things inside in and outs
done so if I go into the programs yes I
can hopefully start coding
this was not supposed to have himself
yeah
mark says restart that always works I
was over the new video about this song
damodhar
the demo gods
Oh fantastic okay
so i'ma have my table maybe and they're
not going to to the you you you you I
I'm going to need my you will again
including the company name
this is so happy
No
you of course then I'm need to set the
Corinthos or ADA darts okay
then choose ecosystem that's done it dot
with them some cash dot d for instance
so now I'm ready to talk enroll so now I
can do basically already starts sales
order
at first
console over reach okay no sorry's I'm
ready to go in here
what to set the big point so
of course already - cannot you cannot do
right back into this so it has some
limitation police this is a very very
easy way to to get your entities and of
course if you want to get more the other
thing you need to do is say you eat that
Oh take it out saves over a touch where
and even though this can look weird from
half the beginning it's actually pretty
easy - huh - dot kids you know I'm Rita
so this basic course I would eat and get
a number of Records back and then the
only thing you need to do is while alert
you did a mode of Munich so so this is
beta iterating over everything's wrong
Morrow ego-c dot can't sew can't hold it
so so basically this basically iterates
over the the roast at your age so so you
can create filters and you can access
any of the fields in in your sales order
and go party on those so this is how it
works with the OData - Oh even though I
did some typos you can do this in less
than a minute so let's look at how this
actually works with creating the EDC DSF
so in this case I'm going to start with
studio 2017 because all the SDK works
with was post 2015 and 16 new solution
check these 2017 see yes
okay create it and then now there's some
really important things that you need to
setup so first of all I need to go to
the framework type it only works for the
four or five - so you have to do this
otherwise nothing will work in here and
you have to do though so so once you
have started this you need a first I
need to go and get a new good package
with the SDK so go to then you get
packet mention I get the console and now
I need to go to notepad because actually
this new good packet does not exist on a
new goods so it's hidden so you need to
know what it's called
but this is actually the name of it okay
so we can package including the all the
data model fits in here so depending on
the speed of the network we should get
it in
or selecting I'm going to change my app
config and actually there's two ways of
getting to the into the hey CGS system
one is to create a NASA function that
you that you call into another one is
just to put it into a config field for
one sake of time I'm going to to put it
into the config file here that takes
enough time so I'm going to put this in
here and now you can see there's a bunch
of value in here that says replays and I
need to cut out and fits to to get it to
work so I'm going to go into my favorite
portal in here the yes you're poor and
I'm going to the ad and here first I
need is the directory ID in here so and
if you're doing it for Cosmo usually
this is something that they don't want
to give out because it's sort of the
person want but you need this otherwise
you you're chose from the start on so
I'll put this into HAART in here then
the next thing I need to do is to go to
to power ups and you can see up here
there's also a quit it's the environment
ID that you also need and you can see up
here I can set my power cell environment
and if I use default you'll get nothing
so I've spent the day on trying to get
things out of default but nothing
happening is you have to have something
else but let's do that and saver they
cost me so you just create another
environment and use it instead so so go
back in here and I thought you'd get the
environment ID so far so good
I hope then we go back into so a shady
and our
here and now we need to go and register
a new web always didn't had copper
chests in here so why we do a new one
take 17 and now this is really important
again if you don't want to spend hours
you have to select native otherwise you
get sort of a weird error message and I
need a redirect API disk and this can be
any URL in here so I'll just use
localhost
it just needs well it's insulated to us
or LED you well it doesn't have to
connect or anything so said quick mark I
think so looks good good okay fire so
now I've got my application here and go
selected so then the next thing I need
to do is to to go and set permissions
for on it to to available to access from
from the outside
actually I what I'm going to do first I
need the application ID for my country
for normal just click here to copy go
back to visual studio so these complete
this so so this is my 80 application ID
I know so now the config file is is
completed so to get this to work I need
to set up the permission so I'm going to
look at the list in here
I need to write it otherwise nothing
will happen to him down here and ETS
your service management I a P I I select
this I need to delegate that and select
that so one down one to go
and then the next one requires a little
bit of tweaking because now I need to
delegate the phases for the year the
common data service in here so as you
can probably see it's not in here so I
tried to say is common nothing happened
then I tried to do CGS and then after
spending a lot of time I I was desperate
so now I worked perhaps ah here is just
need to know where how much you get it
ok so now my app is there and of course
if if you're creating an app that has to
to work with different cosmos out there
you Basin he to call them to a can you
please give me your your directory ID
and then I need to go to to create a new
app and set up these permissions and
then send the these strange-looking
values back to me then I promise I'll
get things to work for you trust me but
actually we we now can write some code
again so I'm going to cheat a bit more
because I'm using all of mark time so
I'm going to just like before I create a
demo with the sales order so now I got a
program starts yes this time so that's
good
okay and what you see is the the CDSA is
the key and for some reason I don't
understand still on tenth day they
decided to quaint the old version of the
the link syntax in here so you see that
you have things like select fields in
here instead of the where clause and if
you once more feel you have to sort of
continue this so in order you sort of
have the the select star thing but that
doesn't exist insidious because of
performance reasons so we don't want
people to select all the fields in the
database and I returned that that
goodness but it sort of gives a very
clunky to insects while you maybe have
to add 50 of these select field
statements in here and in order to get
the lines I need also true to this to
this beautiful clothes and here include
related and then sales order and product
related and now I'm back to getting the
selects field from I I say it's all
aligned in here so lets me just set a
breakpoint here and see what we got
so far so good I can log-in sannin
except
Oh fantastic
so now I should be able to get my cold
out here you can see I got 20 rows back
with my sails over I can dig into the
first one and ask for a description and
some other stuff so these fields are
filled out but the other ones are not in
here and I should also be able to go
down to the the order line Scizor that's
two of those I asked to get a park named
out of that in my cruiser so you see
again same result as with the OData just
a little more work to to get things in
here also in in the SDK you can do
updates of value in here in this case I
I basically look if the description is
wood - and if let I remove it and
otherwise I'd put it back this was not
to blow up my database doing this too
many times so so I can go to to all of
these in here and and to this updating
and then what I do the execute payment
down here this basically - a callback to
the SDK and doing all the updates this
is all code s but now we are near P so
this is logic you would ask do I have
not enough of this item in the inventory
and then if I do that I can actually
sell it to this customer and you you
basically remove the item from inventory
and then put it on on the on the order
and that happens in one transaction but
CDs does not support some sections just
within one call just like normal or ADA
so you can ask if there's something on
the inventory and then you can give it
away but then somebody else might have
taking it before you actually go to the
end so that's so honestly this is sort
of useless for transaction use unless
you want to upgrade
description are on a cosmonaut II really
useful for her for doing bookkeeping or
any of the stuff you hope you'll find in
a V so let's move back to the dislikes
take the last one so so as as you saw
the issues in here that this
confirmation of corneal cost was to get
the the three values from ad is not
really scalable you have to specify
these for all the channels that you want
to to get through in your code and then
all the quizzes so they they have to
reasoning in code and they are static so
you have no select star and for the
people who playing around whether you
can actually do cogeneration to to do
this query and using the Ross and
framework in Visual Studio but also and
when you try that you also know that
whenever you create a type in Internet
it stays in memory forever
until the process is killed so if you do
this on a service you wouldn't in
running out of memory because your tap
will just eat up everything you have so
in order to get this to work you you
have to do this an Esso function all you
have to do use the old trick of
restarting your service when it's
necessary but that's not that fun so
and for some reason also why on earth
didn't they use the OData way of doing
it
state they create their own if you are
the muslim be some reasons but it's sort
of a new way to learn where the host
whole rest of the world is moving to or
ADA this is something new where I was
created for some reason that I don't
understand so but that's probably a good
reason for it and also in ohrid whatever
constant feels you have put on your your
service that will also be reflected by
the dotnet classes you get in your
projects that's not the case in NCDs so
you have to do the things where you use
reference by name to get this value this
works but it's so it's not optimal when
you're used to working with the data or
data now of course as it's very
something that's sort of also various
port
by reading stuff and simple things this
is doing the trick and I hope they will
create a version too because the the
ideas are great it's it's not just done
for for beta business yet so so at least
we're waiting until version 2 comes out
so yep but that'll be next year Hannover
Linux ok thanks barking so this session
is about connectivity everything is
connected you can connect to anything as
long as it has an endpoint sharing
solutions has never been easier than it
is today people are creating extensions
and I know that when Microsoft came out
with extensions version 1 I was a little
bit loud about not being too happy about
all the all the pitfalls but I think
with the extensions version 2 they
actually got it they got it right you
could also see on on app source
solutions are popping up everywhere so
repeating the same modification over and
over again and then collect the money
from the customer that's that's history
people can actually click try and buy
apps and there's a star rating system
and everything starts to be connected
why did we event ERP what was the reason
to create ERP solutions right in the
1970s and 1980s connecting data was hard
and ERP was invented because people were
tired of the sales department creating a
customer and then it would go to the AP
or a our department and they would
create the same customer and that's the
reason why we created earpiece solutions
so everything is in one database but if
connectivity is so easy why do you still
need to put everything in one database
it's much easier to put everything into
distributed systems because we are all
aware of upgrade issues and I'm pretty
sure that extensions will solve part of
the upgrade problem but I know that some
of the nav customers out there they use
nav and they have one database for
entire Europe
right and then they want to upgrade and
how do you upgrade entire Europe over
one weekend and it's just much easier to
have distributed system and then connect
all these pieces together and then if
the sales part sales department wants to
go to a new version of their app they
can go to a new version of their app
without interfering everybody else right
so we're going without from that
perspective to a new era of connectivity
so yesterday you if you went to the
session about api's Microsoft has
connected nav to Microsoft graph if you
run a navy in the cloud like Dynamics
265 you can actually go to Microsoft
graph and and read all of your nav data
but you can also do the same if you
install a navy 20:18 at at a customer
then you can actually read the data from
the API that Microsoft provides which is
pretty cool so let's actually see if we
can actually make that work and I think
you already did the c-sharp demo right
during the CVS demo you showed how to
connect yeah yeah yeah
so now I'll go back to the rubber hammer
right so Microsoft gave us a new rubber
hammer in in Visual Studio code they
moved our precious beloved AL
programming language to 2 vs code so
what I'm going to show you now is let's
say that you have a couple of customers
using an AV or one customer using an AV
in different countries and let's say
that you want to connect those countries
together right so rather than having one
big sequel database and then everybody's
connecting to the same database we have
one and AV database in Holland one in
Belgium one in Germany and Germany wants
to read some data from the database in
in Holland right we can use the rubber
hammer for that let's first go into the
API endpoints this is the
the API endpoint on nav 2018 this is
running on
I think CTP 16 or CTP 17 you have to
enable the endpoint like Anders
described yesterday by default the API
is not enabled because Microsoft doesn't
want by accident to be to expose all of
this data and you can see that we have
all of these wonderful entities that you
can query and one of the entities is
accounts so let's see what accounts look
like this is my accounts API and here I
have a couple of accounts we have food a
savings account these are all of my
chart of account records so let's see if
we can actually read that into into a
nav and I'm going to do that using the
new data types that Microsoft has
provided in Visual Studio code and I'm
going to use a framework that Erin John
has provided and Gunnar and I made a few
small improvements to it but you can
actually download this framework from
from our engines github and then if I go
into a visual studio code I have the
code unit that will actually run from in
this case I have decided to just run it
from the customer cart so I have a
customer record extension where actually
go into calling the web service then I
call the web service and basically what
what are in John did is he created an
argument stable and that arguments table
is basically a wrapper to consume the
web service in in in vs code the first
thing we have to do is we have to
initialize the the arguments table and
in this case I'm doing that by giving it
the base URL which is the URL of my
local system then I'm adding the
accounts endpoint and I'm including
which company I want to
read from then I'm telling the system I
want to use the the get method and I'm
going to use a username and a secret
password then I'm going to call the web
service which is also part of the of the
argument table I won't go into that you
can actually download that from from the
github and then we can go into the into
the save result and this is where my
arguments table gets back with my web
results and this is where gunner did his
magic
we're actually reading the result into a
JSON object and every OData endpoint
that you work with always has a values
class and the values class contains the
data that you can actually read from the
Oh data endpoint you can see that in the
nav web service here I have the value
right it always starts with value that's
probably something that they discussed
and they said let's use that word I also
in my in my swagger API I also have the
values right so that's probably
something that these guys actually
always agreed on to be a good idea and
then we have just a simple loop we are
looping over the the result using the
for each in in a L actually the funny
thing is that I actually showed this to
to Michael yesterday in the speaker room
he says but but when are you going to
show me al
yeah but this is nothing sharp this is
al right it doesn't look so clunky
anymore as it did in in Seaside but it's
the wrong key be careful this is a
roomful of nav developers so let's
execute this
goes into the web client tries to fire
it up
and then I run the web service and now I
get the the result right this also works
in the in the good old windows client in
the good old windows Lyon technical so
go to a customer card and I can run the
web service and they get the same
results Michael just showed that in in
c-sharp you can connect to the end point
and then c-sharp will generate all the
classes for you that have all the all
the all the types you can do the strong
typing and c-sharp against all these
classes let's start a community project
project I'm going to start a github and
I think what we should do is this is our
OData API endpoint and this contains all
the metadata and let's create something
that generates a whole bunch of tables
that we can use as temporary tables and
then we'll move the data from jason with
likely F and filter into those temporary
tables right I wanted to do this as a
demo today but I actually spend three or
four Sundays and a whole bunch of
evenings getting the freaking power app
stuff to work so actually did not
succeed in doing that right
so hope you like that allows you to to
read data from a navy database to
another nav database just like Michael
did with which C sharp it's everything
is about connectivity there's a whole
bunch of tools out there the trick is to
use the correct tool for the job try to
get out of your comfort zone and try to
learn new things learning curve is
always high but once the penny drops
it's it's so much fun to start working
with if you don't get all of this don't
worry there's probably going to be a
hundred thousand of Asian customers on
seaside forever
and you can always work for those
customers right questions thank you I
know you do a lot of work with
connecting nav to other apps for your
customers how has this changed what how
you are going to do that can you give
some some real-world examples so how is
this changing how I decide to solve
problems if a customer approaches me
with connecting stuff right now I would
say I would still put a navy in the
middle because c.d.s is not there yet
but this is something that I will
definitely keep an eye on not everything
in the real world is yet ready for OData
you would be surprised how many
companies have a software package and
then you ask them how do I connect to it
and they still are so proud of their
soap end point it's like come on guys
this soap is like 1995 wake up and go to
AU data so this is I think this is
future but it the real world has to
catch up with that that's my opinion no
no if you so
so as you all know L has this limitation
so you don't have dictionaries and stuff
you don't have optics there's a lot of
thing you cannot do it's really powerful
from not getting hurt and you have the
Robo hammer but that also has the
limitations so if you use Ojeda together
with a sharpie now have the fool that
needs power underneath you where you can
do fantastic things and do it in two
lines and really clean code so in some
case it's good to break out of the box
and to to visual studio and do these
things because it's so much easier then
it is a nail but al is grated was this
dosh today to write business logic and
turn it it's good for something else but
now you have the possibility to do both
very easy and you can see that's if you
fasten a keyboard you can actually cut
something over running within a minute
so it's not like the old days where you
had to do so stuff that's integrity and
you have to have a piece in rocket
science so this is for everybody oh yeah
I've been working with soap endpoints
which were in Dutch and then all the key
words were in Dutch and then you try to
code in in English and then you have
some programmers from Ukraine trying to
help you and you actually have to
translate all the keywords and and the
advantage of voda of course is that it's
structured it's it's it's an API that
everybody agreed on with get boot and
stuff like that a lot of questions
for you mark when you were talking about
the power app you said that you could
not have the time stem field that means
that the the normal Oh data is not
working with the power I pour water from
data is working with a field that they
call eat egg and did you go to the API
session yesterday yeah so Oh data has an
e-tag and each egg is basically the same
as the time stamp if you write back
after you read it the e-text should be
the same and if the eat egg is the same
it's basically that you get the same
error message or she should get the same
error message as in any V another user
has modified a record after you read it
from the database right so you have to
implement every table as view if you
want to sorry
so if you want it to work from the
powerup you have to implement every
table at of you if you want to work with
power apps and you want to expose an AV
data to power apps you can use the API
that Microsoft ships with an every 2018
but if you have your own vertical
solution you have to create your own API
as well you can probably create an API
with vector F and field ref I think that
is what jet reports is doing then you
just get everything okay
I'm not going to throw it at you so you
know how fast Microsoft is going to
implement the proxy generation for data
for in Visual Studio 2017 or in which
code it's not yet there so can you so
the proxy generation in c-sharp for
example yeah from OData imports yeah for
imported from importing the web service
is not yet working it's not yet there
and also I want to you know have any
ideas one when it's up to come so I'm
the second question is is will it exist
for for visual code also don't think
it's exist for for Villa's code yeah
there are tools online if you like
Google on Oh data conversion to c-sharp
classes or to type trade classes you can
actually paste in euro data JSON file
and it will generate the c-sharp classes
for you okay and you can paste it into
your code but it is actually weird that
Michael actually did it in 2015 and it
worked in only seventeen its own yeah
that's so on so reason why I didn't and
2015 is that you can go and just go and
add a service or F instead has been
removed from 2017 and also already for
does not work that way
but that's a that's a client innovating
API that you are component that you it's
a new good packet that you install that
that can create the things for 2015 but
I haven't gotten it to work with 17 yet
so there's something missing with the
year with with the item types that you
you want to add so but if the
documentation said it should work but
nothing shows up when I try so might
just be me but instead that's a
component need to install and you have
to mess with the TT file and these kind
of things that said vs so it's more
manual than
but there's documentation on the image
the end that shows you step-by-step what
to do so it's not that bad just more
work I actually have a project going on
which is connecting Odetta 4 to asp.net
website and we read the OData manually
and when then we used a Jason convert to
map it into a c-sharp class ok I'm sorry
it works I showed it to Michael and he
said we're not going to show that to
this audience I can live with that I
think we have we had we had bowling on
Tuesday and my knee still hurts you
mentioned before that you are able to
extend the common data model by
ourselves
it's quite complex can we do it in
Visual Studio or how would be the way to
extend the model so right now you have
to go to power ups so there's that whole
tool English theorems which is fantastic
but it's not Visual Studio so you do it
through that that's also a way you
create your own entities but it's still
maintained by Microsoft and also
extended by Microsoft with new updates
so yeah so you might have to take care
that we get a prefix or something that
it's not exactly upgraded but I've seen
during this prototype phase that you get
clunky erases that you are half frame
without thinking ok but also what proves
that actually this is not really a
facility I actually try to buy a
power-up subscription but that link does
not work and it hasn't worked for months
so so I guess nobody bought it yet we
have one more shirt and then we have a
whole box of don't forget it I don't
want to take them back home yeah
I have a general question on perhaps
because the
find it very very interesting but it
sounds to me that it's only for viewing
data and not to do more complex reading
between nav is that right is it
something that is going to come in the
future or so so did the whole
architecture behind power-ups right now
is that it works on its own database so
they didn't want to have sort of a link
to other database you can do that
Marc showed that but sort of the the
core data sets in NCDs underneath the
system - may also make it faster and
that that works beautiful and if you
look at the apps in that it can do great
things so you can do a data entry
application in in an hour that's oh and
it's a moving target you know what what
doesn't work today may work in a month
but problem however if you want to
synchronize data for many we into this
model this well you get all this
clunkiness where where the pieces simply
does not fit together but that's as you
Microsoft will fix that's moving on
because otherwise it's nothing to me
it's great replacements for access and
these kind of of tools back in the old
days but it's not sort of access access
programmers and SharePoint guys love
this stuff yeah that gives them things
that they never had before because they
don't know the legend right and also
there's no there's no code in in power
up so it's find users so code you need
to create into Azure function that's a
completely different story so you can do
basic logic like in Excel adding stuff
and if everything else but that's kind
of it
you said that you cannot use power-ups
for use outside Active Directory so is
it the way that I'm not able to provide
perhaps to the users outside Active
Directory really or is there any other
way
as a Marine you can build as a Marine
happen it uses the same technology you
connect you can connect as a Marine app
to CBS as well or - Oh data it's not
power anymore
okay any other questions just to ask so
we cannot post we cannot post or make
change in the database from power up we
can just see the lake as far as I know
it should be possible to also call the
post I just finished this demo last
Sunday and I was so insanely happy that
I got into work that I didn't want to
touch it anymore but it should be
possible to do it so soon the power FC
API you can of course write back what
you put into the system and also using
CTS you can like I showed you and change
data and write it back or create new
entities but you cannot do translation
like you have encode your lady and then
reach today where you do a party
together and you roll back everything
that's not part of solution yet so it's
sort of a fire-and-forget thing where
you do one thing at a time and then it's
over
but there's no rollback
everything is committed at once or not
any other questions okay well coffee
time
Coffee time thank you thank you
[Applause]
