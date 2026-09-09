# BC TechDays 2023 - Connecting to Dataverse: do's, don'ts, and how not to make all your data publ ...

- **Source:** https://www.youtube.com/watch?v=MkkQpQWH51U
- **Video ID:** MkkQpQWH51U
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 88m58s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

um welcome so I hope this is the session
you chose because otherwise you're in
the wrong room
um my name is Helen rickmans um I work
for cubics as a solution architect Cubix
is a Microsoft cloud consultancy based
out of Antwerp
um we do everything except for business
Central funny right so we do Microsoft
365 we do a dynamic CRM and customer
service and stuff like that we do Azure
things we do Power Platform we don't do
any Erp business Central
yet I'm here I'm a business applications
MVP and M365 development MVP I blog on
blog.com
remember the URL it's not for the blog
post because that has been sailed that
um has been a while since I blog but you
can find all my social profiles there um
and I tweet uh regularly so you can find
my Twitter as well
now on to maths I'm Matt I work with knk
um we are a business Central partner
actually and I started my career with
business Central and I'm especially
excited to be here because the First
Tech conference I've ever went to was
actually enough Tech days back then so
I'm very happy to be back here
um I moved to Power Platform Dynamics
CRM a while back um I'm MVP in business
application so my daily life are doing
mostly Power Platform but since knk most
of our customers using business Central
so we have a lot of Integrations and
scenarios with business sample we have a
few uh like isv Solutions on that so I'm
especially happy um with Yannick
together to present today a bit about
how to bring that together uh similar
Scenic I also have a Blog similar again
it's a bit in sleep mode at the moment
but that will change and if you find me
on Twitter LinkedIn please feel to it
feel free to reach out we will have a q
a in the end but we're always happy if
you connect with us with if seals
running around or even after the event
connect with us if you have any
questions back then let's get in contact
um yeah we're really happy to be here
and meet more of the business central
people
so I would say let's get right into it
let's get to it yeah and if you're
taking pictures it's also a good thing
like you you most likely are taking
pictures of the slide because they're
super interesting but if you happen to
take pictures of us on this big stage we
like to get them on our Twitter as well
so it's always good to have some
memories afterwards so we have an agenda
and some session goals so first of all I
don't know how many people have
experience with Power Platform in this
room so let's do first of all a raise of
hands so that's more than I expected
I've been at days of knowledge for the
last couple of months like three of
those events and people show up there
with no knowledge of Power Platform so
we will do some quick quick introduction
and then we move over into
authentication authorization because
that's the bulk of it how you connect to
dataverse how you authenticate how you
do properly we show you the pro code
connectivity and we introduce a little
bit of business Central connectivity
because I think we have something cool
to show that hopefully you have never
seen before and we will do lots and lots
of Demos in between
if there are questions shout because I
can't really see you
um we have this sketch box you have seen
it before I will throw it very hard at
you and you have to catch it and then
you can ask a question good
good yeah okay let's move on Power
Platform you have probably seen
something similar like this before it
consists out of five
um
products five types of applications that
will do something in Power Platform all
of that uh bound together by dataverse
which is essentially the database where
all your data is stored
looking at those
all Fiverr on here will quickly move
through them first of all we've got
powerapps which is according to
Microsoft the world's most complete low
code platform it's not world's best low
code platform it's the most complete
local platform it covers the most things
it gives you the ability to build
cameras apps which are mobile
applications where you can control all
of your look and feel yourself your UI
it's yours to control or the other end
is you build model driven applications
which are a bit more like business
Central not as nice looking but they're
very quickly to generate and build on
top of your data that you have
um
they scale really well because it's a
cloud right it's always a marketing talk
about it and they scale really
um fast as well so you can put a lot of
data in there so that's pretty
interesting in terms of low code
connectivity we're moving on to power
automate is essentially the automation
platform it's where you go to automate
your business processes and the thing is
that it's way more than most likely you
have seen in this conference
um because the Microsoft people from
business Central
usually only talk about the cloud flows
in power automate essentially the
resilient API driven automation the
thing that runs that calls the apis and
does some automations on it but there's
also a robot process automation inside
Power Platform where you can automate
processes that do not have apis
um as well as if the slide moves on you
can do business process automation it's
essentially in your mobile driven app if
you have several steps to take in your
business process it will force you to
follow the steps to input the right data
to do some validations on it and that
will give you the ability to move your
client through their business process
and in the meantime get all the data
that you need for it
um and then one of the new things
Microsoft bought a year ago one half
years ago a company that does advanced
process mining so you can run some
process mining on your database and on
your data and then see what data is
inputted and how uh the process goes so
you can optimize there as well if you'd
like to
we move to power bi
the product that takes your data and
gives you the ability to visualize it
and most likely none of your dashboards
look as nice as this one
um because it's not as easy to get them
to look nice but at least you get a lot
of
insights in your data you can build
dashboards on them and then you can
export them and embed them as you can
see in many of the applications that are
available within the Microsoft cloud
platform as well as outside of the
Microsoft's cloud
our virtual agents with all the hype on
co-pilot and chatbots and generative AI
power virtual agents is now a bit of a
letdown
they're improving it I don't know how I
should
would frame it better much you're joking
you're laughing but it's the thing where
you build an intelligent virtual agent
and you have to build like your topics
and you can ask it questions and it
gives answers back
um the integration with copilot is still
um coming so it's now a bit more simple
than what you're seeing from Microsoft's
current demos on what AI could do for
you but at least this gives you the
ability in the low code way to build
your own chatbots because otherwise you
have to move into Azure again and full
on develop
which maybe for this crowd isn't that
bad but it takes a while and then the
last product is power pages and power
pages is the tool that will bring uh or
will allow you to build portals public
websites on top of your dataverse data
and it allows you to either create it or
have access anonymously or put some
access on access control on it either
for inside your company with Azure
active directory or for outside of your
company with Azure active directory b2c
so it gives you the opportunity to take
your data and expose it to the outside
world in a controlled manner within the
building blocks of a low code
website builder essentially
bringing all of them together you've got
them again you've seen this slide before
most likely because all of the products
are supported by dataverse in the middle
of course for all the data as well as
some other functionalities the data
connectors they are available within
power automate powerapps and power bi to
connect to outside apis
as well as AI Builder which is a low
code no code way of doing AI
[Music]
generation or machine learning on it
like the pizza no pizza type of thing
you throw images at it and it figures
out if it's what data is on there it
does form scanning and form completion
so if you scan documents in it so you
can get all the data out of it managed
environments I'll let that behind us for
governance reasons mostly but powerfx is
our Excel like programming language in
Power Platform it's a weird language it
looks the same way as
Excel functions look but it's not the
same as Excel functions so you'll have
to relearn it again but most likely
you're aware of that or you're used to
that because algo or Al is not the
nicest simplest most documented language
available either so we have a weird
document language you have your real
document language you'll fit right in in
the Power Platform
um
from Microsoft right it's all Microsoft
let's come up again it would be so
simple if everything would be C sharp
right
well we will get that
um the reason when you saw it on a lot
of slides the data was Yannick mentioned
that right that's the reason that's why
we focused this session a lot on the
database because that's really in my
mind kind of like the center of it all
that's kind of like connecting the
different things and there's new stuff
from Microsoft coming all the time the
data was and it's more and more in the
middle of it and I was happy in other
sessions here especially with Microsoft
and they were presenting and there was a
lot of power apps and they were also
talking about virtual tables for example
which we later talk about so Microsoft's
really working on getting a story across
all the different products of bringing
database in there so we figured we will
take the session a bit talk about what
is data was what you can you do with
that and I like this slide a lot because
it shows uh database it's not just a
database right even if the name kind of
suggested but it's a lot more in there
um a big thing we're talking today about
will be the security part so see
database then we call it's an API you
interact with apis but really at the
core of the API is a very secure way of
handling your data very sophisticated
permissions you can set up there we will
go into that a bit later and what you
get as well on top of that and that's
again I would say a bit similar maybe if
you used to work with business Central
so you get the logic on top of it so you
get a lot of ways how you can handle
data
um for example like triggers in business
center right so something happening with
data there should be a business process
being triggered by that and we can use
power automatic of course for that but
data was in itself also has capability
to do that so it's quite powerful to do
that Microsoft is working a lot of
bringing power of X the weird language
so again I called it more into it so
it's getting also more low code to
develop for dataverse
um obviously there's a lot of data in
there I want to show a bit about data
especially with the storage part because
um this is something where I can I feel
like database can offer something to you
if you have business Central already in
place but the sample is a relational
database right so there's a SQL Server
somewhere even within a cloud you can't
really reach it anymore but it's still
there so it's for relational data mainly
and then
that's there's also a SQL database in
the back end we can't reaches as well
but they also have different kinds of
storages we will talk about that so
basically you don't have just the
relational storage but you also have a
blob storage for files if you have
images if you have some kind of
documents and want to store that with
your relational database you can do that
in dataverse and the nice thing there is
because well with the move to the cloud
I think we all got a lot more aware of
the price of storage right I don't know
exactly what they charge per gigabyte
for business Central but it's not that
cheap and data was either and because
there is a lot behind it Microsoft is
managing a lot of it but you don't want
to store everything in relational
databases so it's very nice that we have
the option here to have the file storage
with there because it's just a
percentage of the price compared to the
relational database and it is quite
transparent so you don't have to think
about where to store it dataverse will
do it for you if you throw files to it
it will in the background move it to a
blob storage and make it more cheap for
you which is always a thing right so
developer basically have the API and
there's one field called the image field
and you don't see that it's a different
field or what happens in the back end
data versus will take care of that and
then obviously the integration layer
we'll talk about that a lot we will do
the demos with that how to interact with
dataverse and Microsoft is using a lot
of these capabilities as well in
connecting business Central and data
errors so um maybe a quick thing um
because that's what I said I like the um
the idea of having like these different
starches so what is the data worth you
intact with an API so everything you see
here this is not something you can
control this is fully managed by
Microsoft which I'm personally a big fan
I like the whole Cloud idea I don't want
to work on some server virtual machine
install the patch or something that's
Microsoft jobs and they're doing a good
job at that so we have this virtual
machine like load balancing they're
doing a good job
mostly doing a good job okay better than
I would do managing virtual machines
and basically this is what it looks like
behind on the virtual machines that's
like into processing logic
um and it kind of as we said before you
give a record in there and the record
has a lot of normal Fields like text
integer that kind of stuff but also
maybe an image on a file field and then
it's determined okay which of these
storages are we going to use is that
going to the SQL pool is that going to
the file storage Cosmos DB is also in
here that's used a lot for lock
storageers and will be more and more
used Cosmos will be a nosql database and
this is all brought together
um in here and also with the data Lake
the one data Lake Microsoft is pushing a
lot with Microsoft fabric
database has I would say a kind of long
history of integrating with the database
and it's only getting stronger so yeah
exciting stuff you can do with database
we could probably fill 90 minutes just
going into that but as we said we would
today we want to focus a bit more about
kind of like the do's and don'ts on with
the authentication with the security
part and also of course going in the
integration part because that goes hand
in hand
and with that I would say let's do the
first part yarnick will show you a bit
of the we call the low code connectivity
related kind of like how do you code for
half the group that already built
something on Power Platform this is uh
Basics so essentially you you start with
your uh Cloud flow you have the
dataverse connector
um but I do want to show it because
there is a tiny little bit that's not
super clear about this
um you find the dataverse connector it's
one of the out-of-the-box connectors
that are available I think Microsoft
says that there are more than a thousand
now
um and this gives you all of the actions
to interact with dataverse essentially
if you do this
um and you get list rows you will need
to make a connectivity to your dataverse
now um by default Microsoft will and
then you get the list of tables so you
can list all of your accounts and you
can do multiple Advanced options on it
like select specific columns filter row
sort by all of that that's in there
those are the connectors that's the
default way that this happens the
default way that Microsoft does this is
that you when you get a connector a
connection it will do this based on the
logged in user so the first time that
you store the power automate Cloud flow
the connection to dataverse will be
created with the user that is signed in
into Power Platform which essentially
means the maker the developer that's
building the cloud flow
their account will be used to access
dataverse now if you're building system
flows and
um
Standalone automations that might not be
the best thing to do and then you can
add a new connection that's the one
thing that I wanted to show and then you
get the big blue button which you're
very tempted to click but essentially
what you would like to do is connect
with the service principle so you can
use an application registration to
connect to dataverse I'm showing it here
mods will talk lots more about that
functionality but you need this in this
connector just
because basically this is the first
don't or we would if you can avoid it
don't use a user for these kinds of
things because usually you will move it
to a different environment the
environment might be in completely
different tenant that's where the
application URLs come in and yeah make
more sense
um same goes uh in the uh power up as
well on the canvas app you get the
ability to connect to a data source and
dataverse is in there by default so you
can just select the tables in there and
it will get all the data for you the
difference between power automate and
canvas app in this sense is that with
power automate you get all the different
actions you get get a row by ID list
rows all of that when you do it in a
camera app you get the table like you
get the full data set and it's up to you
to filter it to sort it to everything by
using the uh weird programming language
power effects which is Excel like to
sort your table that's just the a little
bit of a difference and the last one
that I wanted to show show you but I did
not open up yet is that is a model
driven app
um so I will quickly run that one so
model from apps as young except before
that's very similar to the business
Central app so you can't like in canvas
Pixel Perfect Define where controllers
basically you say this view should have
the following columns in the following
order and sort by that and then it will
generate the app for you so when I
switched from nav to Dynamic Specter and
powerapps this was actually a full query
at home because I thought oh I know this
I if I can build kind of like a business
sample I can build a model to a map
exactly so you get the view you saw and
this is a form you can put multiple
fields on there you can modify it but
you can only drag and drop fields on it
this is what we call a model driven app
things like Dynamics 36 365 sales is a
model driven app customer service is a
model driven app Dynamic 365 marketing
is a model driven app they are just
provided by Microsoft their first party
model driven apps you can build your own
if you want to
um
was there anything else I was supposed
to show well um I think we saw it
quickly or you see it here on the screen
right the virtual tables um maybe just
to mention that because we reference
again so he was showing the customer
table there and that was and I think
Microsoft has had some sessions on that
right and or who has worked with virtual
tables with business Central do we have
that
well if you've got a few cool cool cool
um we'll cover it a bit more but
essentially this is the way of bringing
your business Central data this is one
way of bringing your business Central
data into dataverse so you can work with
it I can open this here make the change
in dataverse back to this thing and then
it will be updated directly into
um business Central as well so and it
will follow all of your business logic
and anything so this means that you can
get your data and dataverse and you can
build multiple applications on top of it
um which might be easier than building
those applications right inside business
Central
then I guess we go back to the slides
yes because we mentioned the
connectivity
um and you already mentioned like you
can do it like as a user connect with
your user account or you mentioned a
service account service principle so we
want to talk a bit about what's the
authentication authorization what's
behind that and what different options
do you have when you connect to database
so you get your data and database how do
you get it out how can you work with
that and
um first of all the authentication
authorization which can be a very
abstract concept so I like to think
about the kind of think about it like
layers the first layer the
authentication is basically we need to
tell the system who are you if the
system needs to figure out who are you
because we don't want to make our data
public it's business data so we don't
want to give everybody access so we need
to know who is trying to access the data
that can be a user but it could also be
an application and a system so for
Integrations scenarios for example once
we know who is that user who is trying
to access the data the next is the
authorization what is this user this
application allowed to do is it allowed
to do that because it could be that
Yannick is trying to access my database
but I don't want the anik to access it
so I still need to know it's Yannick to
tell him no
oh I say oil yeah Yannick is allowed and
then the next step and that's a bit so
authorization for me comes in two
flavors the first one is the more
technical yes Yannick has access the
second one is what does he have access
to the permissions
um think about it at um in business
Central when you create a user right you
create a user record and then you give
it the permission sets to say this user
has access to the following data and
this kind of flavor
um yes I were flying in yesterday and I
was living at the airport if you imagine
airport it basically follows the same
steps so you get at the airport you go
to the check encounter with your
passport the passport they will check
are you the person with the passport so
who are you and then okay it's mutts
here's your boarding pass okay with the
boarding pass I go to security
the check is a developed bordering pass
that's the authorization step so I'm
allowed in a secure area of the airport
I'm allowed to take a flight and then
with the boarding pass it kind of like
Get permissions can I go to the lounge
connect to what gate can I do and what
seat am I allowed to allocate too I
don't know if that helps but uh I
figured it might
um but yeah well with your history it's
surprising you're allowed to fly so just
saying well
but it was going to the forces right yes
so it works out
um just very quickly so there's a lot
kind of like technology behind it when
we talk with
um dataverse um basically with Microsoft
365 in total authentication is done by
open ID connect which is kind of like a
framework a protocol how to authenticate
people and the authorization part is
doing with oauth oauth2 at the moment I
mean gets developed and developed
um and again open ID connect who are you
who are you could be a user could be a
machine an application authorization
what is that user allowed that app
allowed to do and then every application
I mentioned the permission sets in
business Central we have something
similar in dataverse you have to do like
this permission set when you know who it
is and you gave them access you want to
control what exactly are they allowed to
do technology wise in the end it's oauth
so even in business sample if you use
the permission sets on the API level you
set up the oauth permissions what the
user has to do that
and the whole behind that I mentioned a
few times the Azure active directory
that's basically the brain of every
Microsoft tenant every application
Microsoft has every login you use it
will go to this Azure active directory
um yeah so if you ever use your Office
365 account if you ever use your Outlook
account any other account
every request will be going to Azure
active directory will be I think it's
one of the biggest application and it's
it's immense like the amount of traffic
they have in these and it's working
quite well well without identity nothing
happens in Microsoft 365 for Azure or
Dynamics or Power Platform so it's the
brains of it all yes and that's a good
thing because we want to have a secure
Cloud environment otherwise we wouldn't
do any business applications in the
cloud if we can't trust that it's a
secure platform Azure active directory
is giving us that
um so just quickly I had to put it in
there so we have all our users so every
user and any Microsoft tenant is in
there
um but if a user for example you log
into your business Central online
in the end it's not just the user you
need because every time you will need an
application an application Azure
directory is basically telling the
system like which app is it in that case
business Central and how can I log into
that so in the end in the back end
there's always an app and the app has
either access
um like similar to you when you set up
with your user account right exactly so
basically you gave power automate
because he wasn't a power automate maker
right so he gave power automate the
permission to log in as his user as
Yannick that's so it's not the user
logging in directly but the power
automate application connecting to
whatever connector he has with his
permissions so that's you have always an
application in the back end and that's I
think maybe one of the points if you
take something from the session well I
hope you take a few more points but this
is definitely one so if you work with
Azure active directory it's in the end
always about the applications and the
service principle behind that it's kind
of like the implementation of the
application in your tenant
there are a few flavors to that and we
will do that in the demo later so the
first one is so if you want to interact
with your data works with Microsoft and
anything else you need an application
and when you register an application
Azure directory it will ask you what
type of application do you want to have
the first one and that's the most well
if you do some kind of integration but
it's like the default option right it's
the single tenant meaning it has to
happen in your same tenant the Microsoft
tenant Azure directory usually kind of
like this ad for me it's at KK for
example at cubics that's the tenant and
it says this application is only valid
within the borders of this one tenant so
which means something custom that only
users with an account where the
application is registered can access
that application and that's the
important part there that's a single
tenant application and this is for most
internal applications this is the case
because then Azure that we will make
sure that nobody from outside can access
so they for the authentication they at
least at least need to have an account
in your tenant security device otherwise
they can't access it so it's a bit more
kind of like a wall around it and for a
lot of cases that's what you want
because obviously there are also other
cases multi-organization apps
um multi-organization apps for example
um if I have an ISP solution or I have a
software as a service solution and I
want you all to access that I'm selling
you all subscription to that and you
want to log in there's like this one
application for my software as a service
and I'm virtual serving in your tenant
saying this tenant can access this
service application then because you
don't want to create an account in my
Azure active directory you want to log
in with your account so basically we
need to make a connection between these
tenants and saying well you can use that
so in the end um it's also an
application as you see maybe in the
picture it's basically living then in
two tenants and kind of like linking
Easter tenants and this is also
something you have to be very careful
about because you have to set up which
tenants are allowed to access It or Not
by default I think it's for all tenants
for all so if you make an app app
registration
um multi-tenant essentially as soon as
anyone finds the public URL for your
website app or anything they can sign in
with their own credentials to it
so that's the definition of a
multi-tenant application I don't know if
you remember back in February there was
this big leak where you could log in
into a Microsoft application with your
own credentials and you could find Bing
search results and you could promote
them so that they would be on top of the
bank results page and it would show up
instantly
um so that's because they didn't do
their multi-tenant application properly
it's the developer's responsibility in a
multi-tenant application to validate the
tenant IDs that are
allowed to access the application and
there's another special thing here
because naming within Microsoft is super
complex if you talk about the home
tenant this is where you register your
application this is where you go to
application registration in that
screenshot that Matt showed
app registrations that is the app that
you register every app also gets a
service principle
the service principle is the one that
shows up in Enterprise applications
for a single tenant application it makes
no difference they are both in there the
app registration defines the well if
we're talking
um
development it's the class it's the
framework it's the characteristics of
everything the Enterprise application is
the instance of it so in my SS
application so I have the app ID
basically yeah and if you would kind of
like install that get access that in
your tenant there would be a service
principle yeah of that app and it would
only show up in Enterprise applications
so if you ever wondered why in
Enterprise applications there are more
things than in your app registrations is
because of that
um so if I register it in my home tenant
and you access my SAS application or
mods SAS application because he's a way
better developer than I am um and you
access it access it then you will get
the service principle or within
Enterprise applications in your Azure ID
you will not get an app registration so
that's a big difference
good yeah very good and again it don't
or do I would say I do so if you do this
and there are a lot of cases where it
makes sense and it's the perfect way to
do it be aware so don't just follow any
tutorial and copy paste be aware what
you're doing there because otherwise you
will have it's a bing example kind of
like opening up your app to a lot of
cases where you don't want access to so
I said it's a secure cloud and it is but
I mean this is a powerful thing so you
can open the door so be aware what
you're doing there it's secure by
default unless you do stupid things
um so it's up to you to make sure that
it stays secure right
yes permissions and consent lots of fun
there
um the the first of all delegated
permissions this is essentially where um
so you can set up your authentication in
two ways your application can do
authentication to dataverse or to any
data source in two ways first of all
delegated permissions this is
essentially where I log in into an
application and that application will
use my credentials to access the data
source like your ultimate flow like my
power automate flow it will access the
data on my behalf and get back the data
that I have access to
essentially when you do that you get the
pop-up like everyone has seen the pop-up
like um do you allow this application to
access this and this and this data these
Scopes you've seen that Twitter has it
Facebook has it Azure active directory
has it um at that point your app is
unable to act on behalf of me over on
behalf of the user
um but it's very important to note that
you do not Grant apps permissions you
grant the app the ability to act on your
behalf the app does not get
more permissions than the user that's
accessing the application and that's the
important thing to remember with
delegated permissions if I access it
access it as a global administrator
of course the application can fetch way
more data than if it's just a user in
there now if you're looking at
application permissions this is all used
for apps that run without the sign-in
user present
um Service uh things that need to run
Windows services that need to run Azure
run books everything that does not have
or does not allow you to go through any
sign-in flow
when you grant an application permission
granting can only be done by a global
administrator with some permission level
within Azure active directory and you
don't Grant it permissions for a user on
behalf of a user you granted specific
Scopes and in most cases this means you
granted full read or full write access
so it's a way broader scope and gives
way more access
so you the client application in that
case gets that permission to run
directly on its own without a user
present to the data source in terms of
dataverse there's a second step and that
step is very similar to business Central
you still need to create an application
user user in the dataverse environment
that maps to your app registration
because you have to give it
oh yeah security rules I will show that
in a minute there's a screenshot there
is it here no it's not there yet
um so I will show that so it's a it's
very similar there
um for connection credentials
you essentially have two options uh you
could use user or service account that's
your user account your named account it
shows Yannick does something but when
you access this or you use this this
also requires username and password it's
a very bad choice for automated
non-interactive applications
um because it also gets impacted service
accounts also get impacted by
conditional access and MFA flows which
means
for example in power automate if you
ever wondered why a power automate floor
that was connecting and running for
months without any problems has turned
off and run as never run before
potentially one of your administrators
has made a change to MFA which forced
the log out of every logged in
credential and the invalidation of every
refresh token which means all your power
automate flows stop conditional access
policy is the same thing if you say you
can only use this credential in the
browser well that's out of luck you
can't do power automate flows anymore
we're really really problematic and also
it uses licenses so if you use a service
account or a user to connect to
dataverse that user account that
connects to dataverse needs licenses
um which also means that if you need to
separate do separation of concern you
need multiple service accounts because
not every service account for every
application should potentially access
the same type of data which also means
that every service account needs a
license
yeah that's fun and you see your bill go
up Microsoft is making enough money so
we don't need to do that we don't use
them we can optimize right 3.4 billion
last quarter or something it's okay they
have enough
um and also user accounts have
um lower API limits so essentially
um especially with high impact
applications if you use service accounts
there it gives a bit of um of a
there are lower limits there for
accessing the dataverse apis
if you go to service principles or
application users in the end because
they can also be managed identities they
run as a system account essentially you
use client ID and client secret to
authenticate
um you still have to monitor the
lifetime of the secret because you set
up the secret Lifetime by default it
suggests 180 days I think six months
less and you can increase it to up to
two years maximum I like the secret
without it it doesn't work and after a
maximum two years which is not
recommended to do it will need a new
secret and you need to re-authenticate
everywhere yeah so you will need to
update the secret in all your
applications
um but the important part there is they
have a higher API limit
and you don't require any licenses for
those application users they are
included in the platform
um the biggest difference between the
two is that especially within Power
Platform connectivity low code
connectivity there's limited connector
support for these like most of the
connectors support username password
authentication only the dataverse
connector and the Azure key Vault
connector I think maybe a couple more
support application users
and this is my statement I know people
have different opinions on it but I'll
I'm on stage so I get to share my
opinions right
um so managed identities in my view are
way better than service principles
um manage identity threat that's kind of
like the service principle but Microsoft
is doing a lot of management right so
you don't have to manage your own secret
so a managed identity gives you a
service principle but the secret is
managed and rotated and changed by
Microsoft so you don't have to remember
it you don't have to do any secret
Management on it so I managed identity
in my opinion is better than the service
principle or slash application User it's
kind of the same thing which is in turn
better than a service account to use
which is in turn better than a user or a
named account to use for any of your
Integrations
it's my opinion we can have hour-long
conversations about it I did two days
ago with people so it is possible but
this is my recommendation if you can
connect to dataverse to your data
sources with managed identities this is
the way to go
then we get security roles everything
that accesses dataverse needs a security
role in the security role basically
defines what permissions a user has
within dataverse it's the same as your
permission set within business Central
so you see this is the new one the
screenshot is not super great for people
that have been working with dataverse a
little bit longer it's just updated to
this new UI finally the previous one was
really ugly and you remember the the
little circles that you had to click
four times and then they fill up quite
quite nicely yeah super difficult to use
but we have got new ones so security
role and every application user or user
needs a security role to actually access
anything within the environment
and this is your concept comparison but
since I know nothing about business
Central I think this is better left too
much yeah basically as we said before
what um think about security walls like
the permissions and if you look at when
you register an application user in
business Central this is what the screen
looks like in the current business
Central online and you have the name for
it
um you have the ID and that's the Azure
active directory ID you have there and
basically this is the authentication
part right you tell business Central
this is an app you can trust this is an
app which should be allowed to access my
business sample and it should be allowed
to access the following data it gets the
following permissions and only those
permissions if you don't set up the
permission part then you don't have the
authorization so even if you the
business sample knows that app it
doesn't know what it's allowed to do and
you won't get any data out of business
Central and basically the same thing on
the right hand side with database so
that's why we talk to screenshot you
also have the name there you have the ID
below that and then you have the
security roles it's basically calling
what is allowed and yeah I would suggest
I showed a bit how to set that up
quickly
thanks a lot so uh yeah my playground
Azure active directory isn't that your
production environment no no
so don't don't make any photos of any
ideas
um no so this is in here um as I said
here we have for example our users
virtual just users in there but we
especially also have our app versus
relations and this was Yannick said
right the average situation is if I want
to register a new app like I want to do
an integration I want to have some kind
of connectivity which is not for example
done by power automate I go here for the
application to quickly show you the
Enterprise applications because as the
only mentioned there is a lot more so if
I remove all the filters here you see I
have 467 applications in here and if you
look at the names you will see there's a
lot of kind of like Microsoft products
already in here and that's what I meant
there is always an app in the back end
so if some kind of data has access
within Microsoft there will be an
application
um let's for this one create going back
to my app registrations let's do for one
integration
see integration I give it the name this
is kind of like for me to remember what
is it and here we have the types of the
app registration this is what we
mentioned before so the default is the
single tenant meaning only accounts
which are in my tenant here can access
that I can also choose the multi-tenant
one here just again again from every
tenant people could potentially access
this application I can't control that
and by default people with Microsoft
with Office Accounts you see
um recently or it's been used there was
also that personal Microsoft accounts
can access that
um you could not say I only want to have
personal Microsoft accounts for this
case let's create the singer tenant and
if you want to access dataverse you
don't need to care about the redirect
Uris here um
shows you watch a study application and
what you get is you get an app ID so I
have an app ID here in the end because
it's an Azure active directory
everything also has an object ID be
aware those are different and usually
you will need the app ID but the I love
how it says usually is it always it's
probably always right it's a Google it
should be unique
and what's the same is your tenant ID so
this is the tenant ID which is kind of
like controlling if it's single tenant
only other applications from that tenant
can access it if it's multi-tenant also
other tenants can access that here and
and now you have basically two options
if you want to really use that delegated
so it's the Unix said if you want to
create an application where the user has
to sign in and then the application has
working on that user's behalf with that
permissions what you need to do is you
need to allow this app to access the
database you do that here with API
permissions by default it has the
Microsoft graph user read so for the
user which is logged in it can get
information for that user for example if
you want to access dataverse what you
need to do here you need to add the
request API permissions and yeah we
mentioned naming is sometimes difficult
with Microsoft dataverse back then was
Dynamics CRM called so you still find it
in here as Dynamic cim we ask them
something and apparently changing this
name here would break a lot of things so
they still couldn't do that you see if
you click here then we have here another
thing the user impersonation for the
common data service common data service
was the name after Dynamics CRM for
dataverse so it's one name impact it's
still not a code name but this would be
dataverse API permissions
yeah don't ask us why it's still there
and access common data service means you
can access your database and for a tiny
small three-week window the thing was
called dataflex I believe oh yeah and
then there was a trademark infringement
so that's why it's now a date of birth
exactly okay this is what will be for
the user um apple troll date demo later
where we build some kind of integration
so I don't want the user process in here
so what I want to do is being able to
register like um it will be an Azure
function in the end something which is
running on a schedule so I don't want
the user so I don't give any API
permissions
so I have set up kind of like the
authentication part now I need to tell
my dataverse okay this app has the
following permissions because I'm not
using user permissions I'm not having a
delegated access so what I will do and
this is what we saw the screenshot
before this is comparable comparable to
when you set up an application user in
business sample or um
yeah that's I think the best comparison
there so I'm go to my Power Platform
admin Center and I have my CXC that's my
environment name I have here and with
users and permissions
what I have here is application users
and if I go to application users this is
basically where I tell database which
application users are allowed to access
my database and you'll see there are
always some in there and for example
Microsoft products also use this way of
accessing data for example Microsoft
forms Pro there's not something I set up
in this environment it's by default
already there and there will be new
stuff added by Microsoft all the time
yeah and it's also not named forms Pro
anymore it's currently customer voice
so also true yeah what I want to do I
want to get my application in there
because that's the application I want to
use later on to authenticate with
database so what I will do I will create
a new app user and the nice thing here
in the UI is basically gives me kind of
like a wizard to show me okay what uh
what's available in your active
directory and here we see this BC
integration has just created with the
app ID and I can select add so now kind
of thing this app but remember we also
this is the authentication now I need to
tell which permission does it have
um
dataverse has a concept called business
unit without going into it too much it's
a bit like companies
um business sample it's not completely
but kind of not that important at this
moment
um and you see by default there's only
one business unit in there and
um next to the business unit I need to
assign the security walls and this is
the permission sets you have there and
you see there are a lot of different
sets in here and we can look into one
how they look like there's Auto one and
this is a don't there's the system
administrator this is I think this is a
super is that still available in
business stand for kind of like giving
permissions for everything this is
system administrator and dataverse and I
see it a lot of times
um when people say well I don't exactly
know what permissions so best to give
them like all permissions then I can't
get an error that's a don't like do not
do this because at the end also said if
you give all permissions then everything
can happen especially if new stuff will
be added in the future the app will
automatically also get access there that
can be quite dangerous so don't use this
one and
um I for now um
I created some custom roles here
um I called it for example I have a
Content part of the demo later on I want
to do and I have an event part and I
want my application to only read data I
don't want it to write data back so I'm
selecting the content read and the event
read permission set security rule here I
add that and with this the app is a
registers and database and database
knows okay if somebody is authenticating
as this application against database the
following permissions are applied to
that the following things are loud let
me quickly because the screenshot I
think was a bit small let's go to the
security rules here and let's check
so because you saw well I just picked
the name I think it's the same in
Business Center nowadays right you have
this permission set name but you don't
see directly what's behind it similar
here with the um security rules for
example if I get to my content read
and by default it's showing me only the
assigned tables
and if I
well it's a bit new
oh that worked out quite nice yeah maybe
you should zoom out a little bit
this looks a bit better
so there are always some kind of default
things which are always assigned but
basically for my custom table it only
gots the con it gets the content content
table and you see it as non-create
permissions it has read permissions
organization means for all business
units when these business units are
meant so basically for all business
units if I have multiple ones and I
can't read I can't delete and database
has a few special security walls um
yeah which we don't go into too much but
you as I said it's quite sophisticated
what you can do with the security model
there usually think about create read
write delete the usual ones and um yeah
here we see I can only read my content
data but I can't right back to it
okay okay
so now that we have authentication
settled and we can access our dataverse
now we have to see how we do that and
what code we use so first of all working
with data and dataverse using Code there
are many options and most of them are
pretty confusing if you Google it
because there is a lot of history
um I heard someone say in a session
today that Alm in Power Platform was not
really great like two years ago but
essentially it's all built on top of the
fundamentals of dynamic CRM from back in
2008 2009 so there is a lot of history
in date of Earth
because dataverse is essentially the
thing that got taken out of fundamentals
underneath Dynamic CRM so you see lots
of old code and lots of old suggestions
for you when you Google
um so that's something that we want to
help you with at this point so first of
all
you can find anything like this
um saying if you need to do web service
authentication to get your data
this is the organization data service
um
this is what Microsoft talks about it's
using odata V2 and it's deprecated at
the moment so any
example on the internet that uses the
xrm services 2011 organization data
service is deprecated it's old you
should not be using that we've got the
API data V 9.2 endpoint which is the web
API and it uses odata V4 and this is
essentially the future of it so this is
it's already there right well it is
there no so and it's here now but this
is where the you should be doing your
code if you have code in your
organization for some reason from other
developers because you would never do
that of course that uses organization
data service you should be changing this
very very quickly Microsoft has extended
the
deprecation date like it's deprecated
but the removal date out of the platform
five times already and probably they
will do more but that doesn't mean that
you still should be using that endpoint
you should switch to the web API
um the other thing that you will find is
the CRM service client also known as the
organization service
remember the first one was organization
data service this one is organization
service and it uses the soap endpoint
it's an undocumented soap endpoint that
they internally use so you shouldn't be
using soap yourself
and it's the CRM service client is an
SDK for NET Framework and in the
background it uses a soap endpoint so it
isn't going to the organization data
service it's their own endpoint it is
um only for.net framework currently 4.6
point
two I think 247 but 47 framework it's
super super old it's in the sandbox
still so if you build plugins for
dataverse it has to be using the CRM
service client but currently it's being
superseded by the data for service
client or service client is what the um
the the class name is in in.net which is
confusingly enough also called the
organization service
um so just so you know if you Google you
find lots and lots of stuff this is the
SDK for net core and net six and like
all the future.net because it's
cross-platform this is where all the
development happens this is the one
thing that you should be using
um
anything special I should mention there
oh yeah the fun part about the service
client the new one is that it internally
uses a combination currently of the soap
endpoint as well as the web API as well
as the
um a bit of organization data service
but the end result of Microsoft is their
goal is that in at some point in time
transparently without that you noticing
it in your application the whole SDK
should move to web API it's not there
yet as far as I know but they're very
um
tight-lipped about that because well who
wants to admit that they're still using
soap somewhere I think it's is it still
possible in business Central oh okay but
yeah you're still using soap who dares
to race his hand or their hand oh no oh
I yeah I feel for you with your soap
envelopes and your XML sorry
um
yeah not really
um so when you use the service client
sdks and there's the thing when you
start googling this you have two options
with the service client because one
option will be too simple you have late
bound code which means you don't have
any generated classes you only have
runtime validation of your code and you
have limited intellisense and it looks a
little bit like this I don't know if you
can see it but essentially when you want
to create an account let me see if I can
get this too
you do new entity and you specify it
with a string and every field that you
need to fill up it's a string that you
have to know because there's no tele
sense it doesn't tell you anything it's
super
frustrating to program that way luckily
we also have early bound code the
downside of early bound code is that you
need to generate the classes the object
classes for your environment
on the Fly for every one of your
projects for every one of your
organizations for every one of your
environments which means you have to use
a tool you have to generate it you get
lots of files you get and then you get
compile time validation and you get
intellisense which is cool but then some
developer goes in and your environment
changes the fields deletes a field and
then your code still compiles because
the classes are still there and then you
still have runtime failures because you
have to rebuild the classes at the time
when you make changes in dataverse
it looks like that
I hope you can read that but you get at
least the Clause there you get all the
properties on it so you get intellisense
there so that's a way of you for you to
get your early Bond code done this is
I think the way that most applications
are built currently except for my demo
later on
the difference yeah
um
there's some helpful tooling there that
I want to call out uh first of all for
early bound to generate your classes
Microsoft has the CRM
svcutil.exe that's provided somewhere on
the internet
um or you could use the early bound
generator in xram toolbox
um I'll get to XM toolbox I think you
will demo it right or you can use the
pack model builder we get the new Power
Platform CLI which has a new mobile
Builder new early bound generator and in
XM toolbox it exists as early Barn
generator V2 for dataverse queries which
is the thing that's interesting if you
want to figure out without building your
application without doing all the
queries you could use fetch XML builder
in the dataverse res Builder to quickly
build up your rest queries or your fetch
XML queries which is essentially
something like a SQL query to your
database but it tells you the result set
up front so you're sure that what you're
putting in your code will give that
result it's a very quick way of figuring
out if your search queries or your
select queries or
um working and with xrm toolbox which is
a an open source Community Driven tool
it exists already for how many years
long 20 I guess or something long and
it's plugin based so essentially there
are new add-ons in the store for xrm
toolbox basically every week people that
find something interesting to build to
automate it's in there if you're working
with dataverse and you're thinking this
is stupid this is taking so much time
this is not very efficient most likely
there is a plug in an XM toolbox that
can do this way faster for you
yeah I'll do business Central
um
with business Central
um now we've talked a lot about
dataverse but if you want your your
business Central data there as well or
you want to connect your business
Central data as well as connecting to
dataverse you have a couple of options
and I I assume I hope that the First on
two on the left you know better than I
do remember I don't work with business
Central
um so there you've got the data
synchronization to get your data into
dataverse tables because you're
synchronizing all the data into
dataverse tables the accessing of the
data is not different than accessing
dataverse you can use the same
methods of accessing it
and it only requires you to have or the
user that's accessing dataverse to have
permissions on that dataverse table that
could mean that mods has no access on
business Central
customers table but since you're
synchronizing customers into dataverse
if he has access on the dataverse table
of customers he can still see all the
data synchronization you have virtual
tables too which uses the API to connect
to dataverse which essentially means
that mods who connects to that table in
dataverse with the same methods because
virtual tables can be accessed api-wise
connectivity wise in the same way but if
he accesses it through dataverse it will
use delegated permissions his
credentials will be passed on into
business Central and he has to have
business Central Access or he will not
get any data out of business Central
and the last thing is you use apis
I know all of you know your apis better
than I do but your user and your service
principal name needs permissions on the
business Central site you access your
apis now the one thing that I hate I
don't know if you hate it but I hate it
is the fact that there are no sdks made
available by Microsoft if you want to
access the business Central apis you are
building HTTP client requests
step by step and manually now I decided
that I did not want to do that in my
project so I
tried something new that I wanted to
show and it starts all with
the blog post from Waldo
you know Waldo right
it's a question well
um Waldo is my co-worker essentially
we're working the same company and he
figured out that business Central the
API of business Central has the metadata
endpoint it's required for an odata V4
endpoint it's a metadata endpoint that
gives you all of the methods in your API
now it gives it a little bit
in a weird way in an EDM X you can't use
anything with it but there is a thing
called the open api.net odata thing
which transforms that metadata endpoint
into an open API spec file or a Swagger
file with that Swagger file
I can use something that's called kyoda
kyoda is provided by Microsoft
and it's tooling that Microsoft uses to
take open API endpoints and generate
sdks for it
so you throw your open API
um Swagger file to it and it generates
for you
an SDK
see and that's when all the phones go up
that's fun
um I I knew this would be interesting
um so I will not show you how to
transform your endpoint into an open API
file because I had Waldo do that for me
he was nice enough to show me or to give
me the yaml file so you see
the yaml file that describes your
business Central endpoints and if you
then go into the command line and you
have kyoda installed
can you read that
making it smaller always nice
you use coyote generate you tell them
which language you want an SDK for it
supports multiple languages not just
c-sharp it's also does typescript
JavaScript uh whatever I forgot you give
it a name for your client for the
business Central client in which
namespace it should exist which is your
open APL yaml file and in which folder
the client should be stored if you run
it it will generate all the classes
which I will not do because it takes a
bit of time but then you get this you
get folders for all of your endpoints on
the left
and you get
request builders for everything
now the way that you use it in your
program file you do
first have to connect to it
like you'd have to do authentication in
my case I'm doing a client ID client
Secret
but I also can do device code credential
which means username password but
through the browser
um
and it uses the Azure identity library
for it which is a standard identity
authentication library that Microsoft
provides so it's again super standard
and you will see that in the database
demo later on that's kind of like when
we show because it's both Azure active
directory right so we can use the same
framework actually to authenticate and
followers with database and business
Central when we're coming from the focal
perspective exactly
so you get your business Central client
where you give your adapter which you
give your authentication provider and as
soon as you've got that super simple you
use your client and you do and you get
all your
endpoints that you have in your business
Central API in this case I want it
um companies with ID because I want to
get the company the specific company
then I want to get the customers out of
it and I get uh do a get request on it
so it's a fluent API type of SDK as a
result I get I just count all the
customers that I get right
um I also fetch a specific customer for
a specific ID super simple again dot
customers with ID specific customer ID
get async now you see it's not the
perfect generation it sets says
customers with id1 because it can't have
multiple uh methods with the same name
stuff like that but still this helped me
tremendously when accessing um
this uh your business Central SD case
because now I get intellisense again on
an environment that I do not know
now when you run this
okay
when you run this it's not super
impressive it just
fetches the data and prints it out
hopefully if the internet connection is
working
maybe you mentioned that you
authenticate with Azure ID right Azure
identity the framework and you're using
the airport station for that I'm
currently using the app registration for
it in this code
here with the client ID client secret so
I have an app registration in my
environment and if I show you in
business Central
or not
um it
um I have that registered and I have
given it a permission set so it finished
execution I have only five customers in
my environment because it's a demo
environment and I retrieved one specific
customer but this way you can access
your business Central data in a way more
interesting way
um or easier way at least for people
that do not know the business Central
apis much as probably you do but I liked
it so this was my generation of a an SDK
and you can regenerate the classes if
you add more API endpoints to it you can
also integrate your custom API endpoints
to it so it's way easier that way to
integrate in your custom applications
and build
your applications or access your data in
a somewhat similar way than you also do
in
um for data versus or any other thing so
um especially like the early bound tool
for like the early Barn too exactly you
can see here that my app registration is
in here
um as well and I gave it basic
permissions because again I do not
understand permission sets but it gave
me access to customers this is all what
I want I think the important part is so
he what he gave in his Azure the C sharp
code you saw he had the application ID
and the application secret to the
authentication so this application can
authenticate with business Central and
then the business sample comes in and
says okay the following permissions
apply and you are actually allowed to
read the data there yeah if I run it
again it's the same result if I run it
again with device code authentication
you will see many of you will probably
have seen this before that it will tell
you to go to microsoft.com forward slash
device login and you have to enter the
device code and then you can so you can
go here
you have to enter the device code that's
in there and then you have to pick the
uh
pick the account that you want to
authenticate with
so there's that but it's the same result
so let's move on because mods is anxious
of getting here it's his full demo done
yes uh we bought one more demo of us and
um basically the case now I'm registered
already kind of I showed you okay
there's like the content event table I
have and I will go there so basically my
use cases I want to build a website I
want my users to access the data and I
don't want them to log in somewhere
um if you if you listen to the Power
Platform overview there might have been
one tool which does the similar things
do you remember if you want to do
externally build something and give my
data out externally
well that would be power pages so that's
something from Microsoft or Microsoft
stack
um we had a customer project where we
didn't want to use that for various
reasons there's on one hand licensing
costs but also a bit architectural stuff
so what we use as a so-called static
site generator aesthetic side generator
is I think an interesting concept
because it takes basically a layout and
it takes input data and on the push of a
button it will generate a website for
you a static website and with that
static website um the thing is because
you can create it really quickly
um it's a static website you just need a
web Hoster so basically it's just HTML
and JavaScript files you just need to
host it somewhere you can put it on
Azure blob storage make it publicly
available and you have your website up
and this is for example how I host my
blog my blog is a static site generator
and there are a lot of Frameworks for
that um so if you want to look into that
a lot of different things I will work
with Hugo in this example it's also what
I use for my blog it's a very fast one
and
um basically what I would say the
advantages it's very very fast so you
can create very faster things it's very
cheap it's almost free and there are a
lot of hosters where you can host it for
free and it's very safe it has very few
dependencies and this is why we picked
it for this use case at our customers
because for various requirements we were
not allowed to have a live connection
from the website to our Erp system and I
think that's in a lot of cases it's an
Erp system right so I don't want to give
too many people access there I don't
want have like a public endpoint which
does communication there and also
because data is not not all data is
changing all the time so it doesn't make
sense if I for example this event portal
my event data is not changing that often
so if 100 people are looking at my event
data I don't want to have hundreds calls
at my database to retrieve the data I
basically want to Cache it and that's
what static site generators can do for
you it's open source so it's very easy
to extend to work on that um you can run
it locally on the cloud and if you use
the white Frameworks does it put it in
there it's very very fast so I really
hate when it blocks and there's some
like really old WordPress
implementations and you click on it and
then as you see okay it's doing it the
database request and five seconds later
it's loaded I don't think that's it
shouldn't be like that anymore nowadays
there are a lot better tools and I want
to have it now on a click and this
static side channels because they don't
have a database connections they are
really really fast and when will you
reach 100 in performance mods you're
only at 99 I think that's disappointing
I think it's because it was above like
five milliseconds or something
and if you want to host that there are
different options um there's for some
natalify like third-party options
Microsoft nowadays with Azure static web
apps also as a way to host it so
basically you check in your code to
GitHub and get up with actions it's
running and it's producing the website
and we the running and producing I will
show that it's like a few seconds and
then you have the updated static content
with all that there but before to talk
more about it in theory I think it's
best if I show you maybe one more slide
yeah
I call it the power CMS CMS content
management system right so the data is
in my database environment I'm using in
the middle in Azure I'm using my static
site generator and I want to have the
Azure database data so what do I do I
use my Azure function to authenticate
with dataverse and I will show you two
different ways how to do that we will
use the application users again we set
up and basically that then generates my
static web page and I make that static
web page available for external users
the nice thing is external users don't
have access to my database because
there's a block in between and I also
don't have to share my application IDs
with a website because that's all done
in Azure itself
okay
let's
switch over here
very good thanks maybe I'll first show
you what it looks like so what I have
here my event Hub that's my model with
map so this is the app on top of
dataverse and here I kind of like have a
list of all different events with with
descriptions um I have the BC tactics in
here
um I have to start date the end date and
what I create with that what I have here
is and you see at the moment it's
locally hosted by the same Works online
basically I want to generate a page of
that so if you're a PC tag base the BC
tag is here and for example now say oh
well this description it's the same so
let's change something there so I go in
my database
a USBC tactless here and and I'm also
passionate about
our platform
we're doing white and left demos and
data works
in there
we saved us and what I'll do now is I
want to this to be reflected here I want
to update my static site generator what
I do and basically it's running here on
my computer
and I'm using Hugo so Hugo server and I
will show you later on how that works in
backend just quickly what's the result
it regenerates the page and basically
this was the whole process right so
maybe two seconds oh no 700 milliseconds
and if I now go here and refresh my page
you see it got the data so it access
database might just change the
description now is reflected here in my
web page
so let's uh let's take a look how that's
done
um basically my hero I have here my
power CMS demo it's in GitHub and you
have like a lot of stuff there um
important is the layout here Hugo works
like this so if we go to layout I have
an index HTML so usually when you have
some kind of web page you have some kind
of index HTML index.html basically says
it works with this is Hugo so not
important but just connect to understand
it it works with partials basically like
modules one module is the banner
the banner in my example is this part
here this is the banner part this is
kind of like a fixed HTML part and then
it's using the partial items Dynamic and
with the following data let's quickly
look into that
there we see how the magic happens
go into items Dynamics so here you see
okay this is generating HTML
and this is what most static side
generous let's do right they generate
HTML in JavaScript but you can make it
Dynamic so in here it's always with
these curly brackets kind of like
commands so to speak and one of my
commands is actually here we get data so
what I'm doing here I'm doing a get Json
this is a Hugo call to say please go to
this API and get data
um I'm not accessing data was directly
here because I don't want to do the
authentication in here what I do is I'm
accessing an Azure function and as Azure
service which I won't then use which I
want to use to authenticate with one
dataverse and what I get is the range
like uh like a result set and per item
in that result set it will create this
following HTML code and it will use
the name and the description and this is
why when I change the description of the
event in my database the next time I run
this code the next time I generate the
HTML it will call this page here
it will get the results back and use the
name and description field of my result
in order to create the HTML
okay and this is what creates it there
um let's take a look at the Azure
function because that's basically doing
the heavy lifting here right the Azure
function and I have two other functions
here and I want to show both
um let's start in Visual Studio code in
Visual Studio here what I have is
a little bit bigger
when I use the query this is basically
the function which got called and what I
do is I use the dataverse client this is
the SDK janit was telling you about so
this is the SDK for Microsoft and use an
initialize here I go into the initialize
function the service client that's the
Base Class of the SDK and in order to
authenticate I'm using a connection
string data wash connection string
the database connection string and I can
show you in the Azure function so this
is the code the project will develop if
I want to upload it to Azure I can
easily do that here and go to publish
and it will publish that to my Azure
account I've already done that
in here I have my
yeah called friend zone at friends right
click publish right
short demo yeah you do it in your devops
pipeline yeah
um if we go here to configuration this
is where I store basically my settings
and because again I have to tell my
Azure function with app ID which app
secret to use and um I do this here in
configuration and this is basically the
um yeah we would call it the application
the service principle we could do that
so if my data was connection string
three
well you do yeah well it's a bit but
small well connection swing basically
here we see it ah yeah so what's in
there is my URLs in there and I have my
client secret my client ID all this
stored in here so basically this is the
app ID the app secret connected and my
application is using that to
authenticate so this is not using a user
account remember Unix slide which is
better which is not to use so it's not
using user account but it's still
storing here in Azure function the app
ID and the app secret and be very aware
where you store app ID's app secret
because that's basically the key right
so if you set up this application that
it can access dataverse data and
somebody else gets your app ID in app
secret they can access your data so be
really aware to do that so this
basically I just want to show it don't
do it like this because
well it's better than if you use a user
but it's still not good right so if
you're and if you're doing it like this
please put your secret in the key vault
in Azure key Vault not in the app
settings of your function app but we're
like
you know showing what not to do in this
case to show you how it's done better
right so what I also did here
um let's go back here right you see here
the service client um that's the
simplest Constructor in c-sharp if you
want to I need this connection string
with app ID and secret I also have one
initialize function here called
initialize manage identity and manage
identity in your next slide that's kind
of like the top level right this is the
best way to do that and I will show you
why it's the best way because in here
um I still need to store the URL the URL
in my environment so that's still needed
um but basically how the managed
identity Works
um here in the code I don't have any app
ID or secret stored and if I look into
my function and this is the
data managed here again I'm going here
to configuration
and in this case I don't need to store
anything here so this is all the default
ones and I just have the URL stored here
but compared to the other case I don't
have any secret any app ID in here but
how does now the function app is
communicating with the database and this
is a nice thing about Azure functions um
so definitely if you haven't tried other
functions try them out really great
stuff and because they have something
here identity
and if I turn this on what Azure will do
it's basically it will register my
function as an own Apple situation so
basically this app now is known to um
the Azure active directory let's take a
look so I will copy the object idea here
ID here and if we go back to my
my Azure active directory and I go to
all applications let's search for this
ID
here we see the app is here found so
this is the same way as if I would have
done it manually but this time it's
managed by Azure so Azure is kind of
like owning this apple where the
situation here I do get an application
ID I do get an object ID and as soon as
I have an application ID I can use this
application ID if I go back to my
environment here
zoom in a bit more
I go to my application users here
and here I have already added it
check if that's the same one yes to it
so here I have added it the same way I
did before
it's the same way as I added the
application and I've given it security
walls
so it only has the content read event
read this is why now my Azure function
here if it's using the managed identity
Azure knows that this my Azure function
is authentication as this application
and there's no secret here right you see
in the screen there's no way for me to
get a secret I can't get a secret
because that's managed by Microsoft so
the only thing I have to store in here
is the URL and I have to turn it on
basically giving an identity to my Azure
function and then telling my database
this as a function is allowed to do the
following things and the additional
security with that is that the code in
the Azure function is the only one that
can act as that identity that's
associated with the Azure function so
it's a one-on-one connection yeah so
this is really the most secure way to
access that and if you work and that's
kind of like why I wanted to highlight
when Yannick was doing his demo when he
was working with the business Central
API
um in C sharp you're using here the
Azure identity so this is not something
specific to dataverse but you can use
the same way if you want to authenticate
with the business Central API because in
the Unix example he had the client ID in
there right again if we put do this
production code wise we would not use
this code but instead use the same code
AS here and say please do the manage
Identity or authentication do not use or
do not store an ID on a secret somewhere
use the manage identity
so kind to wrap it up because I think we
want to leave some time for question
what
um it do definitely is use the manage
identities and if you do that you don't
have to worry actually a lot about
authentication in your app if you use
with Azure functions here because a lot
of the heavy lifting identity is done by
Azure and as we said before identity is
a complex thing and if you do it wrong
they're kind of like the implications
are big so if you do it wrong
potentially you leave a lot of your data
open or a lot of your data are
compromised so the more you can do let
let be done by Azure I would say the
better because I don't have to worry as
much about authentication and
authorization if I go this way exactly
when preparing for this session we found
some blog posts from the business
Central Community on how to do
authentication going directly to the
login.microsoftonline.com endpoint and
stuff like that which gets you an access
token and a refresh token but in that
sense you're responsible yourself to
store the access token to store the
refresh token to use it at the right
time whereas the sdks the identity sdks
either Microsoft authentication library
or the azure.identity library which
gives you a bit more options but it's
built on top of the Microsoft
authentication library and manage all of
this for you so you don't have to do any
of that work
okay yes which brings us to the do the
do's
um essentially
um this is wrapping up our session these
are the things that we feel that you
should take away here basically
um when you do uh delegated
authentication or you should do
delegated authentication for users if
you need a user to land directly on the
data so they can only fetch the data
that they have access to it's supposed
to be delegated authentication if you
need need app-only authentication
managed identities or better than
service principles which are better than
service accounts which are better than
named users which didn't even make this
light
um
this with the permissions right only
assign the permissions which are
actually needed to do the job and if you
also con architectural wise think about
do you actually need a live connection
or can you be like similar to the static
site generator right because this is
what's done server side
there's no connection and it only has
read permissions so the the risk of my
web page being kind of like an entry
door for a malicious actors is zero
because they can't access it so this was
the least privileges the one of course
on permission side but also think a Tech
head to architectural wise if you can
set it up in a way to make it secure to
access the data and what access you
actually want to give
exactly and if you want to access your
dataverse data through the API use the
web API for odata Access if you want to
do it directly for example in JavaScript
code or stuff like that use the web API
to go there
if you need it with net core please use
the new service client with early bound
code your life will be so much simpler
and your code will look so much better
and use the helper tools that are
available in xram toolbox we only
highlighted two of them better are about
100 well there are hundreds available
that will be another 90 minute session
but take a look there if you started
playing around with dataverse take a
look at some toolbox and I think that's
basically kind of like the last sentence
we want to leave you on one more please
do use database
as I said before as we mentioned it's a
very cool thing and Microsoft is really
pushing there and it's offering a lot of
it's not going to replace of course
business Central but it's offering an
additional way of accessing data a
definite way of maybe have different
data in there and as we saw before kind
of also microsame for some use cases for
example power app is a lot better to use
so start looking at that there's a lot
of opportunity there so I don't like
want to put it as a threat but think
about like a big opportunity to use and
I hope we could show you a bit that is
actually not that different like from a
from Pro code perspective if you want to
integrate with it it's not that much
different conceptual wise or also from
technology than Business Center yeah and
we learned that Microsoft is heavily
investing on it in terms of integrating
it or making it useful for business
Central and it's not going away we were
in in Dublin this week and Charles
lamanna said that data version Power
Platform have 33 million monthly active
users so it's big and um most likely
will only be bigger there so
please enjoy the same things that we
enjoy it's so much fun and on our side
and with that
um
I have to say thank you first and then
there's still five minutes and a half
left for Q a
um three people that ask questions get a
t-shirt I saw one two three okay so
that's already done you were first I
think you have to talk in the black
thingy it doesn't work okay so my
question goes for the static generator
example I saw that you manually
triggered the generation of the HTML but
in production how would you trigger that
to be you know to do it manually very
good question
um so because how to trigger it is um we
do it either way like with an event so
if something changes in my dataverse I
could for example use power automate to
do that do that we have other use cases
on a schedule where we say like once per
hour just because it's running for one
second it's not that important to be in
real real time we just do it on a
scheduler but in most cases really if
the event is happening trigger the build
Creator equation
cool
you want an extra large or a large large
thank you next one here and
so
um question about the security ID and
authentication D and the third one was
um object ID I think so if I could
understood that I understand that you
told that object ID will be used uh in
the list so we will use the object ID
and find the application and then we
connect with to the c-sharp but um
that's basically object ideas kind of
like think about the internal ID of it
um I only used it to find it in the UI
quickly usually you would work with the
app ID and a lot of your uis you can
search directly with the app ID and you
won't find anything
object ID I think in one case sometimes
it takes a bit to I think kind of like
publish so to speak so that's why I was
searching by object ID to find the app
ID yeah for most of your use cases and
code it's the client ID the app ID that
you should be using okay it's about a
managers at ID yes yeah okay
um you had this one slide where it said
what you can do with a business Central
license and whatnot in dataverse
um does it make a difference if you have
a team member license or a full license
like can you do stuff with the team
member license or do you always need a
full user I would say if you want to
really work with dataverse you need the
database license I think additionally
um I'm not a licensing expert for
business Central but I think it gives
you the seated capabilities for
powerapps basically saying the
non-premium stuff you can use so I think
if you really want to use dataverse you
need to have a separate license as well
but I might be wrong since um yeah you
get seated licensing with business
Central which means that
um you get limited use cases you can use
power automate and I think you can
there's a there's the gray Zone can you
use the the
um the the premium capacity or not I do
not know but at least it's only uh that
license only covers the use cases
um when it's running in context of
business Central so it's only when
you're doing things that are related to
business Central that's what it covers
if you want to do all the fun stuff that
mods did and build your own portal and
want to interact with it that would mean
that you need to buy premium capacity
because also with the seated licenses of
business Central you do not get any
dataverse capabilities you do not get
any dataverse storage with it for that
you do need a full license so you can
use for example the business Central
connector directly in your power app but
you can't store data and dataverse and
then use it there
but it's only I don't know it starts at
4 84 pages of Licensing guides to read
and then you'll figure it out and well
and the thing what I was really
surprised about when I started this
coming from Business Center as well the
per user license is a lot cheaper if you
want to have power apps with dataverse
in there it starts at four euro per
month per user and there are different
tiers to that but it starts it's not
compared to business Central license
it's not a bigger license it's a smart
small license and talk to your Microsoft
account representative they might have
something
thank you
any more questions any more people have
to throw this thing to
because I'm ready for it no
okay so I guess that's the end thank you
very much for attending it was fun for
us so I hope it was fun for you too
[Applause]
