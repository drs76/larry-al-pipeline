# BC TechDays 2022 - Above and beyond - When BC is not enough

- **Source:** https://www.youtube.com/watch?v=6lq7mMa6l7U
- **Video ID:** 6lq7mMa6l7U
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 85m32s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

[Music]
ladies and Gentlemen please welcome toia
Fenster and bird for
[Applause]
[Music]
bake hello and welcome to this session
BC and Beyond uh what can you do if BC
is not enough for your
requirements first of all I want to
introduce ourselves uh first myself my
name is Tobias fener I'm one of the
managing Partners at 4ps in Germany I'm
also a Microsoft Regional director and
an MVP for aure and for business
applications and if you want to follow
along what I'm doing what I'm talking
about then you find my um Twitter handle
my LinkedIn handle and the URL to my
blog and I'm very happy that I don't
have to do this topic today on my own
but instead my colleague B has agreed to
also yeah I'm b b uh working for 10
years for FS Netherlands and right now
in the current solution of um techn
solution architect and also you can
follow me on on Twitter and Linkedin and
I've got also a Blog uh.
NL great so what will be talking about
um the introduction we're already in the
middle of it then we're going to talk
about options when you have um
additional data needs this is when we
look into Azure data Lake we're also
going to look into what happens if you
have some code some functionality that
you can't put into business Central
itself or you don't want to put it into
itself then uh we can take a look at
aure functions and then we also have the
question what happens if you need to
integrate with other systems especially
in the Microsoft ecosystem and there we
will look into Data verse and of course
question and answers in the end but the
first topic will be about data will be
the aure data Lake and for that I'll
hand it over to Bel
y okay F first topic indeed as your dat
Lake and when we prepared this session
tobius told me okay just tell people in
a non-technical way what is an a DAT L
and I think it's quite odd because we
are on BC Tech date but okay I I listen
always to TOS uh but IM mention what I
say also to our account manager to our
functional Consultants it's just a big
lake and and in that Lake there is a lot
of data in it and not gigabytes uh but
just pedabytes and trillions of objects
so it is designs and it's very rough if
we take a little bit further what it is
is uh on the Azure
platform um well the Azure data lake is
built on the uh blob storage on aure
that's very uh familiar by
anybody and it is designed for very big
Enterprise data analytics so it is fast
and it is
growing and especially here and I come
up in that later in my
presentation it is very low on costs if
you uh imagine it is and the the numbers
I've got here it is almost two three
months ago so I'm not sure if it's
exactly the same right now but had the
storage if you look at it it's quite
quite low per gigabyte uh and then again
yeah you have to pay the read and the
write with if you don't do that it is
also quite
low and of course and that's especially
uh very nice is in hierarchical uh name
space here it's so it's a directory
structure so you can name and uh find
your FS very easily so that's that's
also quite good um but then how how it
will be integrated with uh B Central and
this is a very high over uh uh picture
and we are going to deep uh and take a
deep dive later in the presentation but
first what we have to do do is that this
centr will export your data to the data
Lake and those are the
Deltas then we are try we are using as a
synapse uh to conate the data that's
already in data in the data Lake and
combine it with the news deltas and
maybe someone know ask what is as
synapse and um as synapse is just an
analytics had to to bring several
sources of data and uh transform it into
one data source so you can ingest uh to
another and you can filter and and sort
like
that um and then again what we do uh
next is now we read it directly in an a
powerbi dash board and that's because
the powerbi hasn't standard connector
with the S dat L Gen 2
version um but first if we look in uh
are you going to in the details um there
is one thing you must know um there is
an a file structure uh that you can um
save on your data L it is CSV file I
think that's the most common uh on our
people that you know and that's just a
row based and this just like in Excel uh
you have rows and columns um but also
you have paret fs and that is column
based and that's how you see right now
in the picture the the structure it is
sorted by columns so if you remove one
column or change it it is quite fast but
then again have which one would you
choose and uh this is a research uh by
by by some guy I thought I had the link
in my PowerPoint but I think the table
is over eared um but he's done an
experiment with elf uh FS with in total
28 million rows and that will be
inserted in in p and you can see here
the CSV file and the p f and the CSV F
in F size is quite large than in the
with paret Val it's only
755 megabyte but then again when you
read data the CSV f is faster so uh the
the conclusion is it depends if you want
to store it uh with less data just use
bucket uh if you want to read it and
this is the Total Line so if you choose
columns in in your PBI several columns
and not the wool row uh maybe the P will
be in favor of the CSV fil so you have
to choose
there um but then how it will it helps
how it helps your Solutions uh the
integration with the a data
L well if you see at the cost we have
say seen the cost uh couple of slides
ago that the business Central database
is quite costly and you probably all
already know uh you can EX stand it at
80 gab per user per license you get two
or uh three uh gigabytes but then have
for every gigabyt you uh have to pay 10
EUR per
month um and
also with smaller database the
performance is better in this
Central um and then okay have can you
say can say there are apis on it in that
indeed that's true um but the API has
some limitation on it um it doesn't work
with very large data sets
uh you can do it in batches uh and stuff
like that but with quite large data data
sets and you want to export it into Data
Lake uh it has its limitation and one
another question is yeah how will you
handle the deleted data in this Central
you can have subscribe to an API but the
limit is only 200 so if you want to
export 300 tables uh how you will de
deal with that so uh that is one uh
issue on the API
extensions um if you look we are going
to look at Deep uh further in the
solution is um have and we are going to
look right now in the upper corner uh
part is how you want to use it in this
Central we are looking from how to set
up it how to export it to storage and
also have how will the uh dat Lake
extension uh
uh handle the deleted records so if I go
to my B Central
environment I've gotten um side page
export to a DAT Lake storage maybe one
side step um there is an extension uh
that is Microsoft have published that's
the bc28 extension that's what we are
going to use in this uh demo and there
is is you can update that uh on
that um so if you go to the ex data Lake
what you have to do is you have to set
up your uh container your tant ID
account name and your app registrations
and then uh what kind of format do you
want to export is it paret or CSV format
in this case we are you using the pet
format and then you can easily add your
tables in there and if you add a
table uh you can select which Fields you
can export and you can only uh export
the normal Fields flow filters and flow
Fields aren't
exported um and then just a simple
export and it will export it to the a
data Lake and also you can Shadle the
export um so that that's is quite simple
uh how you can uh set it up in in B
Central if we look at um how we can
handle the deleted items um there there
is a subscriber in the code unit this a
code Unit A execution and um there is a
trigger the on after on database delete
so if a record is deleted in the
database it will this and it will uh
record and and doesn't insert on the an
extra table on the ad extension but
then what if you don't want uh to delete
also the record in your data Lake yeah
because uh there you want to keep track
of your history uh but you don't have to
uh have that record anymore in your B
Central database that's quite easy
easily and there there is already an
example in
here if it's in this case the GL entries
um then just do an exit and you can name
all those
tables um so that this how it will
handle the the deleted
records if you uh look at the uh uh data
L uh structure is this is the the
structure we have gotten follow the dat
we're coming up later the Deltas the
staging and the ad jent fs and the jent
fs these those are very uh important so
we have got an A Delta Jon and in that
Delta Jon
um you can see this which table we want
to choose and also what we see is uh
there is
an uh in this case the customer table uh
in here the JL says okay which fields
are exported in that and also uh on top
of it um is also indeed the par
format
it's should be there but uh sorry it's
in the Delta Fs in this one and in the
later one we see the par FS um if we do
an an a meta change here if you want to
delete an an an field or what what kind
of else things you want to delete you
must update also this record and you
must update the r set um that is the
first
part
and then we are going to look at the
second part H it is uh deleted uh sorry
exported in the uh Del F that's already
what uh I've shown it's in the uh Delta
fils and in also in the Delta folder
um if you look in the Delta
folder you can see that is also also the
naming uh structure in the customer and
there you can see that's right now in
CSV fil but later on it will transfer
into an pet fil there you can see all
the records where that I have listed and
my Deltas in
it uh
um then the second
part and that is the uh transfer so in
this part we are using uh as synapse to
transfer the Deltas and combine it with
the already data that is existing in the
data l so you have got one set of tables
uh and then we have also a slightly
change on it uh you can also uh change
that uh C pipelines to filter the the
old records so if you want to save your
records only for seven years the rest of
the data uh you can remove very easily
so if you can't do see the uh AC
pipelines
and here it is and it's just a very yeah
nice view and the flows so what we are
going
to see here is on the top um it it will
pick up the data and it will combine
with my data files and in this case I
have selected the the filter old records
if we going to see what is then the
filter old
record that is my current data in my uh
data Lake but then scroll it down there
is an filter I apply an filter on this
so um in this case the
records uh older than a year I don't
want it removed in my uh data
L then it removes also the uh deleted uh
Records um it filters some empty rows it
will be sorted and then and
that's nice
part which file format I have Cho chosen
this is the parare of the CSV and in
this case we have chosen the parare fils
so it will stay it will ingest my uh a
Del leg with the uh B FS so that's in
very short uh how will our synapse
transform your de Deltas combine it with
your
data and then
if you look also um there is also a
folder data in it we already uh seen
there um there's also one F that's the
data manifest
pation it's also very important to know
because that is the schema for the
data um and I've got it here in my f
Studio
code you can see here okay what kind of
tables are there and what what is the
export
format so it it will be transferred and
then if I look in my data Lake and in my
folder
data you can see also here the the right
directory
namespaces u in this case the customer
and here are all the fils that are uh in
there in my data leg and each file
contains just one
row so it will expand a lot if you got
um a lot of customers in in in the this
case but it doesn't matter for the
performance and then and that's the last
step
is um now you can read it into PBI H we
have got our dat datas and uh data
combined it and now we can read it in my
PBI dashboard so if I open open my PBI
desktop and I'm not going to set up the
wol connection but because that's takes
quite uh some time uh I've already set
it up here and of course with PBI you
can do some a nice dashboard then if I
click here on my uh tables and I hope it
is a little bit visible I cannot zoom in
with my powerbi you can see on the the
right which tables I have selected and
if I open the customer you can see also
all the columns that there are in there
and also the fils and the records in
there so then I can very easily do it in
my powerbi with the data that's coming
from B Central into my data Lake and now
it's in my PBI
desktop so that's that's that's quite
quite easily um if you want to set up
your p
uh uh connection there a standard
connection that's the a DAT L Gen 2 uh
connection you must change your URL uh
if you copy it from the S dat L it's
standard with The Blob uh in there you
have to change that to DFS and then uh
you can do it with your also with your
common
data
model um then yeah there there are some
concerns and that's also the support
it's it's just an open source uh project
uh it's initialized by Microsoft
but who wants to support it and that's
that's the community so I will say he uh
also support for this one if there are
errors in it but then if you got
customers that want to try this
extension are you going to support it
Microsoft says it's an open source
project so it is done by the community
so that's maybe an a tough discussion
that you have with your customer um and
also one concern and that's also what uh
we are looking at from upgrading it is
uh with very large data vals data sets
well the pipelines can run for a lot of
time so if you got data especially for
GL entries there are quite a lot and
it's growing over the year the pipelines
will run longer and longer so that's uh
because need change uh the uh remove the
deleted items and stuff like that so
that's also an improvement uh that we
have to made and that's uh the first
part of the our presentations and now
Tobias will tell us about the wonderful
things of ense absolutely thanks P so
yeah we talked about um how we can
extract data to make our database
smaller to have um Advanced reporting
needs or whatever but the other side of
of um business Central of course is not
only the data but also code and if we
maybe run into situation where we want
to do something in code that is not
directly possible in business Central or
is very complicated very cumbersome to
do in um in um business Central it could
be an option to use an Azure function so
first of all what is an Azure function
Azure functions are a fully serverless
way to run your of course non- business
Central code the idea is that you write
your code you have great tooling for
deploying it you have great tooling for
getting it up and running and the
service basically does all the rest for
you so you only need to worry about your
code and of course the deployment but
the rest is handled which means is that
you get a runtime infrastructure so you
don't need to worry about where is this
running how is it accessible and so on
it worries about scaling um and it can
automatically scale of course as always
if you scale there's cost that occurs so
there are different plans for that
called consumption premium and dedicated
so so I don't want to go into the
details here just to let you know um
scaling is handled automatically but you
still have control and can you can um
kind of forecast how much money you will
pay for it it does listen for incoming
calls um for triggers for example by
other Azure services but also third
party providers and it can also um be
timer based so if you have some piece of
code that always needs to run at night
at 2 a. then this is also something that
an Azure function um can do but probably
the most common usage is to use either
an incoming HTTP call which we will do
in a second or um be triggered by some
other Azure
service it also integrates very well
with other Azure Services um so for
example you automatically will get
monitoring through Azure application
insights and we will also take a look at
that um and you can do what is called an
output binding so you not only have the
inputs that are triggering um your
functionality but you can also easily
bring outputs into Azure SQL into a
table storage into a blob storage
use send grid to send a message to
someone or whatever so um yeah it's
really very well integrated into the
whole Microsoft platform and then you
also get automated cicd including
staging so if you just have your source
code somewhere in a um G repository for
example in GitHub or in Azure
repositories then you can extremely
easily set up the whole cicd thing so
that it um for example automatically
publishes a new version into a um
staging environment whenever ever you do
a commit um in your main branch or
something like
this so Azure function really helps you
to only worry about your code and all
the rest is is handled for
you now how are we integrating it with
business Central fortunately with
business Central 21 there is a very
simplified integration as you can see
here and we will do this again in a demo
in a few seconds um but I just wanted to
show you that even with I hope a fairly
large font size you can still put it on
one slide so it's really extremely easy
to use the integration in Azure
functions um has vastly improved in the
past of course you could do it manually
but that would have been a lot more code
not as readable so I think really a
great new feature that Microsoft has um
provided or will provide with business
Central
21 so what again are the problems that
we're trying to solve with this
basically the assumption is that you
have some code in C in Powershell
JavaScript F Java python whatever as
functions are really very very open on
that or you at least know how to build
it and now the question is how and where
do I want to run this in a secure and
scalable way because imagine you're
running um your application in um you're
putting it on appsource so overnight
this is the huge hit every business
Central customer decides that they want
to use your extension and now um for
example you run this on an on-prem
environment but it's not five customers
who are calling it's 5,000 customers so
what happens how do you scale that is it
secure enough and that's exactly the
kind of questions that you need to face
if you're um going into an appsource and
online world and again AER functions can
very much help with
that examples could be that um you might
want to merge a PDF you might want to
create a barcode and the standard
functionality in business Central is not
enough you might want to convert data um
or an image file from one format to
another and there is this nice C library
or python library or whatever do exactly
does what you need but unfortunately you
need in business Central so how can we
make that accessible or um in the past I
don't know if if you're in the same boat
but the companies that I worked before
used to have more or less extensive C
libraries and now we're moving into the
cloud so we can't use our C libraries
directly anymore um we have to move them
to net standard but we also can't
directly use them anymore so what can we
do how can we solve this and that is
exactly the example that I want to show
you how can we bring our own sh Library
into the business Central online World
by using an Azure function so let's
imagine we have our custom dll that
contains our code we create an Azure
function that uses this dll to provide
the code and we will have business
Central that is doing an HTTP call to
our aure function uses the dll and
returns some data and by the way this is
exactly the cloud ready architecture
that was mentioned um yesterday in the
keynote so this is exactly the setup
that um Vincent was talking about here
and um yeah we will now walk through
that
scenario now that we've talked about the
serverless back end that is all very
very nice because we will have a
serverless production environment we're
very happy we don't need to care about
that this will all work but
unfortunately we still have our local
development tools and I know that this
is a discussion that you can fully um
validly answer with yes I want to have
my um development tools locally but I
think there is also a good point in
making that you want to have your
development environments also in a
serverless way so you don't need to
worry about setting anything up locally
you just want to open a browser and
start coding and that is the other thing
that I want to show you today how we can
do serverless development with code
spaces so we will create our um coding
environment in a browser and we will use
that without using any local tools again
this is not the Silver Bullet that that
solves everything and it's not
applicable to all scenarios but I think
for some of the scenarios this is a
really very interesting alternative
because we are not relying on any local
potentially different environments
between different people in our team we
have all the dependencies all the tools
including the versions defined in a
config file directly in the repository
so we always know what Tex stack we are
using um what tooling stack we're using
for creating our solution and it's
extremely fast to set up it's extremely
fast to onboard new people people
because they just have to open the
browser point at the right URL and they
are up and running and it's also
extremely easy to switch between
projects because again you don't need to
install locally or uninstall something
that is blocking you or something like
this how are we going to do this one of
the options is GitHub code spaces and
that is what I will show you today we
are basically getting a containerized
configurable development environment um
we can use it via Visual Studio code in
a browser again this is what we're going
to do today but I can also say open in
vs code which means that I will get my
local vs code installation that talks to
the code space in the back end this
brings me more or less the fall fun full
functionality of Visual Studio code
including all the extensions that I
might want to use of course if I'm
running in the browser and I have some
local I don't know device connected via
USB that's not going to be available so
anything locally um will be an issue but
everything else Works in in GitHub code
spaces
and just to give you an idea of how well
this is usable and how well it scales
the majority of GitHub is actually
developed in GitHub code spaces so this
was a decision that GitHub made a couple
of months ago and um there's actually a
very interesting blog post by GitHub how
they made that move what the challenges
were how they solved it and so on um but
I would say if if the GitHub
organization can develop GitHub in code
spaces then it's pretty production
ready what is the architecture
again um as I said you can use your
Visual Studio code desktop on your local
installation as so to speak a client or
SD code editor but you can also use
Visual Studio code in a browser um you
can also see Safari here so this also
works on your iPad if you were inclined
to code on your iPad um probably not the
most attractive alternative but just to
mention it's possible um and then we of
course have the backend side so you use
the editor how you um use the code but
then we need to have the back end also
and the back end is a container that is
running on a virtual machine it's worth
mentioning that this is only um on Linux
for now and to be honest I haven't heard
any talk about supporting windows so
that is an um a restriction to keep in
mind and of course this is running
somewhere in Azure but as always
serverless is basically a lie of course
there are servers it's just not your
service anymore and in this case it's
Azure
service what you get in that in that
container is um of course your source
code you have the language and you have
the tooling so basically everything that
is running everything that is needed for
you to do the coding is running in that
container that is running somewhere and
it's automatically provided for you and
when you make changes of course that
becomes visible in your um in your own
editor so this is the whole setup of the
codes spaces and again just to make it
clear you don't have to develop Azure
functions in GitHub codes spaces it's
it's just a nice and convenient way that
I want to share with you
today so that means that the development
of the Azure function will happen in a
code
space now finally let's go to the demo
the first thing that I want to show you
is my extremely complicated library that
we want to um bring into the business
Central online world you can see here it
has exactly one um one function here it
gets the rating for a Tech conference we
hand in the name of the conference and
if it's BC Tech days then of course it's
awesome if it's anything else then it's
not as awesome um so certainly something
that I would have no chance in
implementing in business Central let's
try to um bring this to the
cloud
um when we have this when I uh when we
set this
up there are a couple of things that
take a second or two and because of that
I have pre recorded this demo but you
will see when I am fast forwarding you
will see where I'm cheating a bit so
basically what I do is I go to GitHub
and say I want to create a new
repository I give it a name BC Tech days
Azure function demo I think
exactly I just initialize it with a
readme and then I say create repository
and because it's GitHub it's extremely
fast so here is my repository and now I
can click on code and say create codes
space so this is now um kicking off the
creation of the container of the
development tooling that is in there by
default and you can see here it's
connecting it has the image um the
container has automatically been built
because this is just the default and it
says connecting here and depending on
the day and the time this can take a
couple of seconds or it can take longer
but in this case it was um very very
fast so now I'm in my development
environment but of course this is just a
standard it doesn't know anything about
Azure functions so what I can now do
when it has um finished loading is that
I can say add development container
configuration files this is also a
standard here I can get a lot of
definitions and I'm searching for the
Azure function definition and I'll use C
with net 6 just select the default here
and now I'm basically turning my blank
code space into an Azure function. net 6
codespace and the tooling recognizes
this and tells me to re build the file
the dev container Chason file we will
look into a second so now it's
rebuilding and this is a step that takes
a bit longer so here is one of the
occasions where I'm cheating a bit by
fast
forwarding and then um we will be in the
system again so you can see here fast
forwarding still in that um View and now
we're connecting and we have the aure
functions development
environment but still the code is
basically blank so what we need to do is
um we need to create the Azure function
and as I said the um extensions are
available so now we have the aure
function extension also there we can say
create
function yes this is not yet a function
project so I want to initialize it I
want to use
C I will want to use doet 6 and I will
um be ask for a trigger we want to call
it via HTTP so this is the trigger that
we will use and you can see the list
here there are a lot of other options I
give it the same name that I have in my
uh complicated C library so it's get BC
Tech conference
rating and then it asks me for a
namespace of course we are Tech days so
this will be BC Tech days now I can also
select how I want to um authenticate and
for that I use the function scope we
will see later how that works so with
that now um the the basics of the Azure
function have been created and um we
there we can start to use the code we
need to do a restore as always in C but
that also works
automatically and with that we shouldn't
have any error messages anymore so now
we have the basics in
place um and I'll commit this here
because in a minute we will do our demo
then I will set up exactly in this
initial
stage and sync the
changes okay um with that we have our
function code and we will um add more to
that in a second but we also need to
create what is called an Azure function
app so for that I'm signing into Azure
and then I create what you can imagine
as the um as the folder where my Azure
function is stored in or the the
application and this is called an Azure
function app again I'm using an
extension in my codespace I'm creating a
new function app in Azure again I need
to give it a globally unique name
so I use kind of the same naming
convention that I've used before it's
just the BC Tech days 2020 Azure
function
demo the runtime stack isight 6 which it
knows because that's the local version
and I can select the um Azure region
that I want to use and I'll use North
Europe in this case and now this is the
second um Step that takes a bit longer
so I'm fast forwarding again and it says
it has now successfully created the
function
so now we are ready to do uh more coding
and we're ready to do the actual
deployment okay uh that's the next demo
that I've pre-recorded let's stop that
and go back into Visual Studio code or
actually into the
browser so what you can see here now is
basically the state of the Azure
function as I have initially created it
so this is the end result of the demo
that you've seen now of course we need
to bring in our library so the first
thing that I want to do is grab my
dll and use drag and drop to bring it in
again this is a codes space running in
the cloud but I can still easily
interact with
that so we have uploaded the library of
course we also need to use the library
and for that I have created a snippet
which I call dll reference so you can
see here all I need to do is pointed at
the library that I want to use and now
um it's ready to use in my C
project the other thing is of course
that we need to change the code of the
Azure function so you can see
here um that the default is just um
looking for a um yeah for a parameter
and is answering please pass in a
parameter or if not if a a parameter was
um put in then it says hello that's not
the functionality that we want
so we need to change the
code and I hope that I still remember
what my snippet looked
like
nope okay this is better so now we have
more or less the same function but now
we are looking for a conference name
parameter if the parameter is not set so
if it's null or empty then we let the
user know that we want to pass in a
conference name and if we get a
conference name in then we return that
the conference rating for this specific
conference is whatever our library and
there you get BC teag conference rating
um function returns so basic basically
this is the way how we integrate with
the dll that we have now shown and all
it does is call that one function and
then in the end as you can see here
return um the response that we got from
here now we need to deploy this to the
function app again we can use the
extension for that let's select the
subscription select the function app and
now the deployment is running it tells
me that it will overwrite anything that
has previously happened there um there
is nothing so we can easily accept that
in this manual step and now it's running
the deployment task while it runs I want
to quickly show you just to give you an
idea what the dev container Json file
looks like
so make this a bit bigger you can see
here that it has a name of course it has
a list of the extensions that we want to
use in our code space as we've now seen
multiple times we're using um the aure
function extension and we're using C so
that's the extensions that we're using
here and for the rest basically um it's
all just the defaults so there's not a
lot of configuration that you need to do
and as you've seen you can create all of
this from templates so it's actually not
very complicated to get up and
running while the Azure function still
deploys or actually it has been deployed
but still I want to show you the um the
business Central side of things
oh here you can see I just ran algo to
get a Hello World example um then I
created an extremely easy table so I
just want to enter conference names I
have a page that shows basically just
the table and then we have an action
that calls a function send get
request and you can see here that we get
the conference as a record and then you
basically see the same code that you've
seen before on the slides a couple of
variables then we need to create the
authentication and we will change that
in a second um of course this is not a
way to do it in production please don't
codee hard don't hard code secrets and
if possible use or off because um yeah
that's a secure way to go but for this
demo I'm using um just the code then we
hand in the parameter as you can see
here we send the get request and store
the response and if the response is
successful we just um get the result and
show the text and if it's not successful
then we show the error message so as
easy as it gets again really a great new
addition into business Central 21 for
integrating with your um Azure
functions so we've seen that the Azure
function has actually deployed and I
am missing the Azure extension here it
is so let's go into the function app by
the way you can see there are no icons I
don't know why but this sometimes
happens in code spaces um typically it
is enough to restart and then they
appear so we have our BC Tech days Azure
function demo and as a function this is
the function that we just deployed so I
can do a right click and say copy
function URL open it in the browser and
call it and now you can see okay this
has been executed successfully but we
didn't um put in a conference name so if
I pass in
a
conference
name BC Tech
days then we're getting an
authentication error that's interesting
try
again ah yeah thanks it's the second
parameter so it shouldn't be a question
mark but instead an end thank you um so
the rating of course is awesome for Tech
days and if we do anything
else
any else yeah okay uh excuse my typing
skills um then the the the answer is not
great
as I've shown you before um we're using
the code in here so you can see the code
uh that is stored and I want to do this
for this demo as well so I will just
grab the code from
here and put it into
my business Central Al code and with
that it should be up and running so if I
just hit F5 for
publishing into my demo environment
it should
hopefully publish yes and open the
business Central
environment need to grab the password
from the cosmo alpaka extension but that
would be different for you
probably so put in the username and the
password and now we are logged in we are
on the conference page I'll add to
conferences and then we can
see in the actions that we have a get
rating it's calling the back end it's
getting the result and showing it in the
message and just to show you of course
for anyone else we're getting a
different rating so again a very very
quick and easy way how we can set up our
development environment I didn't exactly
check but I think it took me like 10
minutes to set it up and I did some fast
forwarding so let's add five minutes but
in 15 minutes I was up and running with
the aure function of course your code is
probably more complicated in the asure
function and you need to set up cicd and
all that but still I wanted to show you
it's not like the huge step that you
need to take and two weeks of you know
learning until you get can get up and
running but it really is a very
approachable technology that you can
easily use to go into um Azure functions
and get them up and running and with the
great new integration that we have in
business Central 21 it's also extremely
easy um to call it from business
Central so this is my demo um but of
course when we creating code we also
should autotest it that's that's a given
and for the functional testing it's
basically the same story as for everyone
else do unit tests do integration tests
but as I mentioned before if you're
going into appsource and um your
extension is calling your aure function
then you also might run into unex
expected scaling issues because
unfortunately your um from a technical
standpoint your application is now
extremely successful and you have a lot
more load that you expected so it
absolutely makes sense to also have
performance testing on your Azure
function unfortunately that is also
something that we can very easily do
using Azure load testing and I want to
show you again how that works
also this is something where we need to
wait for a couple of seconds here and
there so I have I've also pre-recorded
this demo and you will see where I'm
fast forwarding so I'm in the eure
portal here now you can see the
resources that um were created for the
Azure function and I'm just creating a
Azure low test now and this is currently
in preview as you can see but it
actually works quite well the only thing
to mention um I created this recording
uh and for the first five tries it just
said unknown error and failed so um I
guess it's still in Pre as I mentioned
um but if you run into the unknown error
um maybe it's enough to be patient and
try the next day as I did got a bit
scared um for my demo today but um I was
very happy that I decided to
pre-record anyway um we're going to
start it here again we will give it a
name in this case again I'm using BCT
Tech days 22 and now it's the Azure
function load test I'm using the same
location north Europe but of course you
could also spread it across the globe
through Azure if you want this is now
creating um
the deployment and then we say create
and the deployment is starting and this
is the moment where I will do a bit of
fast forwarding
again so you can see it's in
progress and fast forward to the moment
where the deployment is finishing here
we are the deployment is complete this
typically takes like 3 to 5
minutes now I go to the resource and you
can see here that I have an option to
create create a quick test and this
quick test is meant for when you just
want to call an HTTP URL which is
exactly what I want to do because I have
that I will first try it with five users
120 seconds without a ramp up so now I
can just say run test that's it not very
complicated you can see here on the
status on the top right that this says
provisioning and if you reload after a
couple of seconds it says configuring
and then when you're reloading once
again you will um see that it changes
status again and says executing but
still still the test run will start
shortly again I'm fast forwarding for a
bit this again takes typically between
60 and 90 seconds and then um the test
run is actually starting and now you can
see a couple of metrics on the left side
you see the users and um on the right
side the response time you can see how
many requests per second it has started
and you can see the
errors um on the top right where you see
the response time you you can see that
the very first call is slower and then
it gets extremely fast because we are
basically just doing computation in
memory so nothing um to make it slower
at the same time if I now on the right
take a look at the um application
insights that have automatically been
created with my Azure function I can
also take a look at the live metric
those are already um starting because
our test case is now creating traffic
against our Azure function so you can
see here I can also o see the incoming
requests which are of course
corresponding to the outgoing requests
from our aure function um we are not
creating any outgoing requests in our
asure function so there's nothing here
and we can take a look at the overall
health there you can see how much CPU we
are using how much memory we using or if
there are any exceptions so basically I
can take a look at it from the client
side and I can also watch at the same
time on the server side what is
happening and I had um two minutes so
I'm fast forwarding again and now you
can see how the graphs are all going
down so my test case has
ended okay so for five users it works
but what happens if I add a lot more
usage for that I can easily just go back
into my test and then change that test
run select configure I want to configure
this particular test um I can also
download the jmx which is the technology
behind it but for now what I want to do
is I want to change the parameters
I don't want to use five users but
instead let's try with 500 users and
make sure that we're really stressing
the service so let's do this in 30
seconds again um very very easy to
change I just apply it's updated and now
I can choose to run it again what that I
need to open um and then say run again
and then it's the the same steps I can
give it a description if I want but I'll
just run it for now and then um the same
thing happens as before it goes through
through the different stages until the
test is running and now we should see um
our test case that starts you can see on
the right that the first requests are
already coming in that the CPU is
kicking in and on the left for the load
testing it takes a second until um it it
appears you can also again see that the
request duration on the right is
slightly higher in the beginning and
then goes down and again and I can take
a look into um how many requests it's
sending you can see here that we now
have a th000 requests now 2,000 requests
per second so this is really a lot that
is happening um fortunately we still
have no errors at all because those two
lines of C code even I am able to to
create without an error um but we can
also see that the backend scales for
this kind of load of course it might be
different for your specific word load it
also depends on how you configure the
asure function but this allows me um to
very easily check if my environment is
ready to scale if it um gives me the
right performance that I need for for a
load and I can even do a prediction
let's say I have a seasonal requirements
on Christmas I expect a lot more load
than I can run that load test before and
figure out if this is something that
works for
me this is it for Azure functions um now
we have handled the data part we have
handled the code part and now we want to
also look into a great new integration
with the ecosystem um with dataor
yeah inde need uh data first what toas
also said we are going can export it
with data L doing functions with s
functions and we have course also data
first we have C also apis to share um
records between systems but there is
also standard integration with datae um
but F first what what is database and
yeah database is just what also
Microsoft says is just a database in a
cloud
nothing more nothing less um it's really
easy to match and you can also
understand it quite well because it's an
low code platform but yes you can do a
lot of more coding uh in there what we
are not going to do in this uh
session and mostly what you see is uh
that it data will put in in the middle
between two systems to to share your
records uh and also what Microsoft is
promoting is the common data model so
there is already a couple of tables in
there especially for the accounts that
you can share your data um with uh fno
uh bu B Central Microsoft uh marketing
and uh sales um and that's the common uh
data model and you can as an IV as a
partner can uh add to that
if we come to Deep dive in that uh
that's a little bit more about uh the
Microsoft data first to tell and not
going to explain the whole picture but
you can imagine what I said is just had
the data phase uh has very good apis
with power automate power apps uh but it
also have an very good security uh layer
on that um also had the data you can do
with uh business uh rules um the storage
uh is there and the export s is also in
this case to your uh data lake so you
can combine your data first B Central
and all kind of data in your data lake
so it is a lot more on that and it's
growing and
growing um if you look at the B Central
integration there are two integration
inside this Central
and that is the sync methods and the
virtual entities um and especially
virtual entities uh is only available on
this Central
online if we take a little bit closer on
the high level design of the sync and in
the red that is my V Central uh database
in the green that is my uh data first
database and in the middle there is an
integration table and that integration
tables um you can share your records
from B Central to your data data uh
database and to do that for performance
reasons Microsoft has said okay we do it
with the job queue so we can shedule the
records through the integration table to
the uh data verse table and that's just
a native uh database table in data ver
and then of course you connect that with
your power automate power apps and other
things if we look at the virtual
entities virtual tables sorry it's
renamed uh high level design yeah also
on red we have got our B Central
database and uh in green M data
database and here you can see is that is
it's coming from the API Pages we
already know so your data is going from
the O data lay here to the virtual
entity uh plugin that's Microsoft Is
providing to a virtual table so in this
case when I'm in an power app or power
automate and I uh going to use an ver
table this the data doesn't live in data
first but it's just
calling is doing a lookup to my this
Central uh database through the API
pages so that's that's the difference
and in two last release you can join
also in a d data ver a virtual table and
an a native table or you can combine
that um but then how does it help our
integration in this part that we want to
share my B Central data data with my
data first and and other solution uh in
B Central there is an standard B Central
uh data first in the rtion and that is
from bc70 plus general
available um so that is our base layer
and we don't have to do anything about
that then we can share very easily
records to other environments what I
also told for example and that's also
what we are seeing in the construction
uh industry uh customers vender and
items uh you want to share to an other
database
because
um very big uh companies have multiple
Central databases in their environment
so there's not one production database
but there are two three or more
so what is the scenario what we are
going to do with the data
first uh on my left hand I've got my
central company in that Central company
database I will uh enter all my data
in this case M items um so I've entered
there m item x with yob Q it's going to
send the data to my data first uh table
and then also how with the
sync uh with my B central two database
that's my D Central company um there
will be had the the item from the data
ver into my B Central database
and in that database I cannot change it
so if I must change something I must
change it in my central
company but then have what kind of
development is needed for this uh and I
will show it uh in a couple of seconds
uh but first we need to create a table
in my datae uh
database
then also in my uh recentral database in
my extension I have to create an um
integration table that's what we see on
High level design that's the U shared
table from data ver and B
Central um also have we have to create
some integration go code so that the uh
fields are the same and the data uh the
tables are uh linked to each
other then H we have to import the
solution in my central company and in my
decentral
company and uh also we have to create a
setup
so how I am going to do that so first
have we need uh to do to create that um
integrate sorry in the table in
dataverse so if I'm going to
datae and uh this is I'm going to use
the make Power
apps.com in my left side I've got my
data first and there are my tables and
then my tables are listened I've created
here a table item and you can see that's
just an item name um but it has an
prefix and that's just an generic prefix
because this is in my data first and
every data first has another prefix if I
put it in a solution I can create my own
prefix so if you want to share this
solution to other partners please do it
in the solution and you can uh have your
own
prefix in this
table uh I have added some columns and
I've added with the uh poix in this case
BC I've created an base unit of measures
that I want to sync uh my description I
want to think my number and my type is
it in surface or just in general item
and there you can see also have that
this be Central uh database
has some own data types have an option
and description and and a look up so
after that you use that very carefully
because that must match my pental
database um if I've created that there
is also in my in code extension
an uh executable that's the alttp
generation and um I must use that to
create that in gration table there is
some par parameters in
there what is my project uh where I can
find my packages what is all of course
my data first
environment what kind of entities I want
to create an integration table in this I
I've created my own item table but then
I have to add some system use table and
a team user table uh because there is
some look up to it in my item table in
this case I've said okay my base ID is
uh
2500 and the table type CDs and that is
the former name of the data first that
is the common data service two years ago
mic transferred it to data ver so that
is what I have to run and if I have run
it I must authent authenticate and it
will create just a table
go up just table in my B Central
extension only in this case it is not um
a nor normal table it is the table type
is CDS so here you can see all the
fields that are in my data table are
also in my uh B Central database so if I
scroll down there are my B Central uh
table
with with my name uh number description
and type and that's all what I have to
do to create an uh integration
table
um so I've created an in database table
a b Central database but then I have to
link it to each other and that's quite
some complicated that there is a nice
walk through uh on the Microsoft site um
but I've already prepared it and you can
see this this just one code unit and
only for have one uh table there is
already some quite a lot of coding there
um but then what what the most important
one is and that's one what I want to
show is um how you can link the databas
table with your V Central table and
there's an um
uh a function that's insert integration
table mapping and this
one it is uh says okay I will link M
item with mine uh data ver sorry my data
first item table that's the integration
table and then I have to say
Okay how must I link my Fields H my my
number will be with my number uh BC uh
databas table and what kind of
directions I must do um if I've done
that and um I've uploaded my extension
to my databases then if I go to in this
case my B Central
database my integration table mapping
you can see here that there is coming an
a special line for you with your item
integration in have I click on mapping
on fields you can see also the link
between them and in this case the
direction is also to my integration
table this is my central
company um and that is I've said in the
code
um if in in inventory setup is Central
company yes or no then it's deciding the
integration is from my integration table
or is to my integ ation
table so that's what I need to set up
and uh do so when I've done all that um
have and then I will
show
PowerPoint uh then I can do my scenario
so I've set it up in my central company
uh run the job queue put record in my
data first table and then uh with the
job Q it will returning to my D Central
company so if I go to
my uh B Central
database
here I go to my item and I will just
create a new
item from sorry for the Dutch language
an
article and then this
B Tech days 22 and the base unit of Mage
is pieces in this case um that's all
what I have to enter and then for this
case I will trigger the
synchronization uh right away so we
don't have to wait I go to my
integration table select an item and say
okay in this case I want to run an full
integration so right right now what is
happening it will integrate I sorry it
will share my record my central record
to my data first table so if I go to my
databas table and
going to my list and just edited so I
have got the full list and I hope on the
bottom there is just one uh record that
is the same as my central company data
that's the BC Tech days 22
item uh so that's in my central company
and now it's in my dat company but then
um in my de Central company I must uh
inserted also in this case I've created
a little piece of of code and uh that's
also what I can show is I've cre created
an function you get data first uh
function
and in this case um it will get all my
uh newly record that isn't
coupled it doesn't find first it will
get it and then it will create a new
record otherwise it does
nothing um
so when I go to my decentral company to
my item
list and I select the get data from from
the data
ver and now it's processing also the the
job queue and when it's done you can see
also here an extra line with the uh new
item the BC Tech days 22 and in this
case I also said okay you cannot change
anything so I have to change all my data
in my central company so in that this
case it's quite easy to share my records
between databases have from my B Central
Central company to my uh D Central
company and because it's in in data ver
the data I can attach also U Dynamic
Sals and other
things
then uh when that is ready there are
some
things sorry for that uh things uh to
note well how we have seen that there is
an an a sync with the job queue but it
isn't real table in there so you can use
just the insert trigger the delete
trigger and a modify trigger um if you
do an insert directly to the DAT uh
integration table you must also set up
the coupling so when you modify it it
does know that it it is the same article
but you can do it just directly and
without the job
queue in uh bc21 the release of
October in there will be an uh a new API
um available that it will can um start
up the job queue so you don't have to
wait five minutes or 10 minutes how long
you setting up the job queue but then in
this with this example in power automat
you can say okay is there is a record
change with that user
uh I want to uh kick off my job queue
immediately so in this case you have
gotten real near time uh sync so that's
that's quite helpful and then again uh
you can also extend existing entities so
Microsoft has some eight default tables
for example accounts you've added on
your own solution a couple of Records um
you can extend it just an a table extend
extension uh with the type CDs and name
your fields and it's coming with him
with the integration so that's that's
quite quite helpful but then H one
concern about this yes it is a lot of
code to make
the uh uh integration working the base
layer is there but there there is a lot
of cod coding in there you can see that
also So within my Cod unit and hopefully
it will be more
easily okay that's it we've taken a look
at uh how we can extract data we have
taken a look how we can extract code and
how we can integrate um that's the scope
for today and I can see a couple of
raised hands so people are interested in
shirts let's
see hi I have a question regarding the
code spaces do you know if there are any
requirements for example to have a
GitHub paid account or how the cost are
of this Cod space stuff that's an
interesting question because I've been
in the preview and there it was free but
I think now it's a public preview and it
costs some Euros so I think you need to
somehow link it into a paid account and
then you can use
them and um yeah maybe also to mention
the cost depends on the size of the
codes space so you can have a 4 core 8
GB uh code space which is cheaper than
the 32 core 64 GB Cod space so basically
the same story as everywhere if you want
to use resources you have to pay for
them uh I have a question uh related to
business Central and data Lake
integration uh so um if I change uh
table structure so should I care about
the structure in data link and how can I
handle it uh if if there you've exported
already with the same structure and you
want to change it you must delete the
structure in your uh dat data Lake um if
you remove that and you do an export
again it will create the Json fils again
and update the the data and the Delta
Json and then you have got that new
field or deleted Fields already in there
but you must do in full
data okay thanks
I have a few questions so the first one
is about code spaces again so is it
possible to use code spaces for I
development uh not at the moment because
we don't have a Linux version of the AL
extension but um I I Tred to get this um
a couple of times and now I heard that
they actively working on it so I hope
that this should very soon appear but at
the moment you can't because um it's
only um compatible with Mac and windows
so you can't use the Linux codespace and
of course Linux is the only option at
the moment but again I hope that this
will appear very soon okay uh another
question uh when there was uh the demo
we generated uh integration tables uh
the type of the field was option so is
it possible to use a NES or only options
are are used when generating tables yeah
in this case it it was an option but you
can use enops and then in the data first
must choose uh Choice and then create
the
old and then the final question so uh
aure functions and um let's say we need
to do a lot of file processing for
example uh we need to put uh passwords
on every zip file that we send to the
client let's say and we do that let's
say a lot of uh a lot of for allot of
clients we generate uh business Central
reports then put them into a zip file
and then we want to put a password on it
so well the Nave solution is basically
create a asure function where we where
we send the full file and put password
send it back to business Central and
then it sends the so is is there a
better solution for
that without sending the full files
or sounds like a reasonable approach to
me to be honest because well when there
is a lot of file processing it in fact
Works a little slower than client
expects yeah that's that's right you you
could try to uh fully extract it into
the Azure function instead of doing it
in business Central if that is a a
possibility but of course if it's a
complicated report layout then business
Central is the right place to do it I
would say okay thank you so can you hand
it over
thanks hi um um two questions one for
code spaces is it possible that multiple
users can work on the same code space no
you um you have your own code space if I
remember correctly if another user um or
if you just open another browser window
then the first one will recognize it and
will stop it um but what you can of
course do is that another user is using
also a different code space so you have
the full setup in the configuration file
you have the code and so on so it's not
like it's limited to just one instance
but instead on the same GitHub repo you
could have 100 code spaces it's just one
is used for one user and one is used for
another user okay thanks and the other
question for be um on the central uh
business Central site uh we created the
integration table there and I think then
we have to synchronize all yeah all the
time from item table to the integration
table and then from integration table to
data verse and so on um why are we in
that case not using the virtual table
that directly data verse points to an
API of business Central and gets the
data from there just without doing
synchronization stuff that we have to
code well it is also about performance
uh things with the fal entities uh you
have to call the API and it's goes
through the NST and also do you read
only but have your
NST doesn't uh must take in that that
requirements uh so that that's why I I
always say oh if you uh do very large
stable chars DL entries do it indeed
with the virtual entities but all the
master data you can do it with with the
sync methods because um in this case you
want to share your uh Records with other
systems then uh the the bental database
will don't be uh used anymore but only
the data database that's why uh I will
all say Choose Wisely and bring the M
data to the data first and FAL entities
uh with the yeah uh yeah the GL entries
customer entries and stuff like that
okay thank
you any other questions here we
go I have one one question about um
Integrations to um so say we have a
customer that has a B server that is
doing the data conversions and
connections the between multiple
different uh environment so uh well how
do you suggest that we should replace
this when we go to the on sasce en
environments is the is the data verse
and U and
maybe um a event grids and as functions
the correct way how to do it in the
future I mean uh it's a long time since
since I last took looked at bis talk but
I know that bis talk can do a lot of
things that are probably not directly
available in dataor so um I would say it
depends if you have um a more or less
simple integration that you have on on
bis talk then this could be aaable a
viable approach if you have a quite
complicated bis talk solution then it
becomes more interesting and you should
Pro would probably need to do a bit
more okay
yeah
thanks I have a question regarding
performance testing of azure functions
we usually have some parameters there
does this performance testing uh
initialize this parameters with some
random values or it just doesn't send
any parameters in this case um when I
pasted in the URL I had hardcoded the
parameter so if it's only one like for
example the authentication code that I
used then you can put it in if you want
to have different um parameters for
different cases then the Quick Test
functionality in Azure loow test is not
uh the right option you maybe have seen
there's another option where you can um
yeah do more advanced stuff it's using J
meter and D jmx file format in the back
end and there you can do really
complicated load testing as well but
then you can't use the quick test and
you have to do a bit more setup and it's
a bit more complicated but it's
absolutely possible you can use that
service for that as well and one quick
question I don't know if I saw it right
but it looked like during this big
performance test that CPU was going
above 100% yeah what does it mean then
um it means that uh there are multiple
cores in the back end and if you use
more than one core it can go above
100%
okay any other
questions oh that's going to be a long
throw but let's
try yay
nice um so a question for for the data
Lakes as I saw you set up that per per
company right yeah uh and you were
saying that the pipelines can can take
quite quite a long time what are what
are some like real world um times we
would be looking at especially if we
would have multiple companies actually
piping all all the data together yeah
right now the solution is that you must
export it per company so first uh the
first company then if that is done the
second company so you must time it
exactly um somea from Microsoft is uh
developing a solution that you can
export it multi company so then you have
just one time for all the companies
exported your Deltas to your uh data
Lake um but then again indeed you must
run just run the uh AER Sy
pipelines for all and in indeed if it's
yeah take longer in in time with a a lot
of Records uh your pipelines will will
run mostly what I've seen is with 10,000
records it will take s six uh minutes
okay thank
you thanks other questions
yeah good that I moved
up so this might be a multiple questions
in one but I have uh I've been working
on integrating dataverse for a year now
and if I remember correctly the CRM
integration record was Mark to be
deprecated is that not the case anymore
or is there something else coming did
you ever see this I haven't seen that I
I haven't seen that also uh that is
deated because
um this is The Way Way Forward what what
Microsoft also knows um the only what
they see also is what I told also there
is a lot of code in there so instead of
uh I fought in 200 18 had with the shm
integration you can click it's it's
confirmable uh that isn't anymore um but
Mar want to go uh is looking into that
okay and um with in the table extensions
for the integration table could you add
fields that are part of
the the base table that were not put in
the integration
table you you can have if you
um in a day data table you you can
extend that also with with your own
Fields uh in there um if you do an uh
gen generate the table you can just
delete the existing records you can
extend it to the original integration
table for example
account and and then add some code then
you can uh syn your also your own fails
in there I meant um let's say for
customers or sales L I think maybe
descript let's say description two is
not part of the integration table but
it's part of the base Microsoft table
can I add this field to the integration
table in the table EXT you must extend
that also in extended the table okay and
it's going to recognize it cool so you
need to add it then manually because the
generation is scoped on your extension
but you can add it manually in that case
you well it's not configurable inside B
you can't add anything manually you need
to extend the table in the code right
yeah exactly in the code that's what I
meant the generation won't work so you
need to do it manually okay yeah Co
thank okay any other questions no I am
up here
so no no okay so thanks a lot thanks to
B for sharing the stage and thanks for
listening yeah thanks toas
