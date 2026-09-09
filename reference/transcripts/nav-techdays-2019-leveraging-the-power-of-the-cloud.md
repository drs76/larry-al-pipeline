# NAV TechDays 2019 - Leveraging the power of the cloud

- **Source:** https://www.youtube.com/watch?v=xHE7Axg6Onc
- **Video ID:** xHE7Axg6Onc
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 90m07s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

good morning good morning everybody are
you still alive
okay we're gonna do a quick test
if you're alive raise your hand
and there was a few people who didn't
raise their hand i'm a little bit
worried here okay
welcome to uh leveraging the power of
the cloud station
um
what we wanted to do with this session
is do something something fun and show
you some cool demos we've been you know
playing around with
and
you know technology
technology is something that
move along and changes and evolves like
you know this technology it was great at
some stage but then you know it evolved
into something else
and sometimes you have to lift leave it
behind and and you know move along with
with the new things and that's also what
we've done with business central with
nav
we've moving along following you know
where technology is taking us
and the cloud is certainly one of the
big things that happened for
you know um our industry in the last in
the last 10 years or so
getting to the cloud also and getting to
you know to this new technology also
opens up a whole new world of
possibilities and what we wanted to do
with this session is give you a
you know a sample a tour of some of
these things obviously you know there's
a lot more things you can do but
hopefully you'll you'll find it
inspiring and and go out and and um
you know check all the all the goodies
there is on azure and and in the cloud
and by the way
most of the thing we're going to show
here is not only for the cloud but also
can be you know used
if you have an on-prem system
before we jump into it
uh i'd like to
have a few words around the code we're
going to show you here everything will
be or is available on github so you'll
you can download it and use it as you
want
integrate it in your solution there's no
ip problem it's all free to use
but but it is prototype quality it's
it's code we've you know been writing
most of the time you know outside office
hours
and um and it's not production quality
so if you want to use it in a
professional environment you you'll need
to bring this code to production quality
and uh with that you know let's uh let's
jump right into it and aspen
over to you thank you
clicker clicker thank you
first of all before we are going to talk
a lot about azure services and how you
can integrate with them
and a one of the key concepts
with many of them is that they allow you
to access access them using rest and
http
and a very common authorization
mechanism is actually shared key access
so i thought it would start just by
explaining how it works because it's
actually fairly simple and a smart and
clever way of doing it when you have
sort of a service to service type of
author authorization
so
the key principles is basically that you
have a service that exposes a rest api
and a client
and
in most of these samples the client is
actually business central
and the service is a service in azure
the idea around it is that these two
services are sharing a key hence the
name chat key
and they use the shared key to sign
some information from the request that
can be verified on the server side
so
it's not it uses the key to sign the
in the case of a rest which is actually
the uri is an important part of it
often
or always i think the uri is included
and then it it
adds in
at least a
time stamp a time to live how long is
this request valid so even if you
intercept the request you can only
actually replay the same request
so
the idea is to use
public private key to
i mean to sign the request
on the with the hash on the
client side
send it off to the server and the server
as part of the request the name of the
key is actually in the request so we
know where to look it up and say okay
this is the
listener key or the center key if you
have multiple different key types
and it actually then can verify that the
request is signed with a valid key
one of the services we're talking about
today is the azure service bus it does
it in one way
azure blob storage has a slightly
different way of doing it
but the principle is actually the same
so for the azure service bars it
actually it signs the
um the uri
it signed signs
and includes the resource and all of
that goes into a header which is
the authorization header that says
shared access signature contains the
signed parameters and then the
inco or the assigned value at the end
and then that is then used by the server
to verify it
it's
even though it sounds a bit
actually sounds very simple it's a bit
tricky to do it in ale so i mean
some of these samples that we have
published includes this functionality so
it's easy to get started with it
so let's jump into the first one
which is
about files and storage
a common problem that many of you are
probably facing is that if you have done
a lot of on-prem integrations
you have you've been using the file
object which we took away in the cloud
and
the file type
is
doesn't really really mean a lot in the
cloud i mean after all i mean
it relates
to c drives and files on a network share
but in the cloud it's a bit different
a file is basically just a a um
a stream of bytes
which we have organized in some shape or
form and when we normally think about it
we're saying we tend to think about it
in the context of context of
classic dos
directory structure
which is just a
representation on top of storage
most of you are probably
all using onedrive or dropbox or one of
the other providers to have a backup of
your files in the cloud
and
even though it looks like they just have
a c drive in the cloud with your data
it's not actually the case because it's
not that efficient in a cloud service to
do that
so
when we start moving our ip to the cloud
we should start thinking about how what
are the data on that we are storing and
how would you actually like them to be
organized maybe a director is not the
right
way to view them in the cloud
maybe they should be shared in the
context of other objects which is not
necessarily direct directory organized
so
let's
jump into the demo
and i will switch
to this one
so this is
business central running in the cloud in
our data center so it's not connected to
anything local here apart from my pc
and
let's
jump into this i will see if i can
make it bigger
so
this is actually azure blob storage
underneath it's not it's not the blobs
in
sql azure it's not blobs
or files shared on on my c drive it's
it's it's actually a peek into my azure
storage account
and what i've built here on top is a
couple of
i have a small problem on mouse here um
it's basically a
directory
browsing similar experience
but it's actually just built on top of
blob storage
so i can pick files i can take this one
and download it
and it will actually download from azure
blob storage through business central to
in this case
my c drive
and it's a picture of a car
so let's
go back
here
so
how's this done
basically it's using the rest api of
azure blob storage with shared key
access
in in the samples that we have published
i have added a list of
of supported operations here which is a
subset of what you can actually do with
blob storage but it's a
good way to get started because some of
most of the underlying mechanics are
actually included
and actually the
last one
delete blobs
is actually a contribution from
bad fanbeak down here
front row i have a t-shirt for you after
and it's the first contribution to our
github repo with
some code that you have added in this
case bart and i hope if any of you start
using this and find i don't know box
improvements i mean
feel free to contribute and
at some point it may even find the way
into the base of the product and be
fully productized but for now it's a
sample but feel free to help us improve
it
the samples here
to make it easy to get started will are
all set up using the normal service
connection setup and there is a for
reference in this i'm not going to go in
details here basically it has a setup
dialog you
read the slides and you can see where
you should put the various parameters to
get started it's very easy to try the
samples out yourself
this is how you upload a file basically
use the built-in upload to stream
and then the azure blob storage code
unit
wraps all the functionality so basically
put blob into my containment this is the
name
here's the in stream
and it calls i get content type from
file name which says if it's a pdf it
gives us the right
mime
file type and uploads it with that
so
one of the other things that you are
missing and we know it because we have
heard it many times
the use of net interrupt and external
functionality
fos
service reliability and security reasons
we cannot allow you to bring any
arbitrary component into the cloud
so one of the options for this is
basically to externalize some of that
functionality and a very very good way
of doing that is to use azure functions
they are designed for that it's
serverless computing you write a simple
function
and it's fairly powerful
so
by the way this picture i accidentally
took when directions asia was in kuala
lumpur this spring and i was standing on
a rooftop and took a picture and
lightning struck and since we normally
use lightning to
as an icon for
functions i chose to put it in i think
it's a great picture in my
personal opinion
so
let's do a demo of what we can do here
for as a demo of what you can do in an
azure function i have chosen to put in
the functionality to make a picture
monochrome i just before i downloaded
from azure blobstorage the picture of a
car it had a collar but i can actually
if you navigate to the same file again
come on
here
i've actually added that option here to
download more chrome and what it
actually does is that it pulls the
picture of azure blob storage sends it
off into an azure function
which do the heavy lifting of the
monochrome conversion it's probably not
something you would write in ale
bring it back
and then download it
so let's try that
if i
yeah
and while
this short period of time i actually
read it from azure blob storage send it
off to a service and i actually think
there are different data centers
and
made a monochrome copy and downloaded it
into my pc here
so it's a very
efficient way and also fairly easy to
wrap the code
if we go back here
so this is the azure function i used
as you can see it's the actual part of
it is 8 10 lines the rest is just some
boilerplate code
and i'm using an external library so
that i can do upload that
sorry
and when i call it from ale it looks
like this there's a bit of preparing
arguments i'm converting it to base64
before i shouldn't send it off
then there's the call
and the return and the conversion back
again
so
this were two examples of some of the
challenges that you will be facing in
when you are trying to convert
integrations to
work with a
cloud
even though we are trying to move a lot
into the cloud
we all know that there is a lot of
integrations and systems which are still
firmly rooted in the ground
i mean
some examples here
barcode scanners
it has to be in the
store
payment terminals a scale for instance
heavy machinery on a factory floor all
of that is not going to end up in the
cloud
maybe at some point in time some of
these will be
integrated
into the cloud
with for instance iot which
gear is going to talk about but right
now the reality a lot of this is not in
the cloud
so
what what can we do about that is there
a way that we can bridge between the
cloud and on-premise
i mean essentially this is the problem
we have a cloud service and we have
something on premise
and that something is always behind the
firewall if it's not probably don't want
to talk to it anyway
and
early on we had this nice little
insider
we could rely on i mean we could send
something to the rtc client with the
run-on client and you could actually
execute the net locally
but with the removal of that we are left
with a web browser which for many good
reasons are running in the sandbox and
cannot do anything
locally so that's not really helping us
a lot
so
let's see if we can find a good solution
for it
and
let me first
do a demonstration here
and talk about what i did after that
so
i have put here
okay
five browser
and this is
actually
my local c drive which i'm
navigating through
from the cloud
and
go into folders
so
and you can see
it's actually
actually fairly fast
but i'm actually accessing local
resources so
how am i doing that
so again this is the problem
so how do we get around this
we introduce service bus relay which is
an azure service that allows you to
create connections between
separate networks
azure service bars is a
umbrella for a number of services they
share a lot of common technology but the
service bus relay is basically a way of
having a
one service that is a listener and
another one that's a sender and they
will be able to communicate
using a
functionality which is very close to
http request
so
look like this
what we have done is that we have built
a framework
which we have put on github and that
framework
takes away a lot of the complexity
around doing this kind of communication
it allows you to write a plugin into
sharp or actually any net language which
will be picked up by a local agent that
you run
on premise
and that local agent then exposes
functionality
that you can connect to from the cloud
in a secure way
and the idea is that you then write and
matching extension in this case i wrote
one which i wrote a plugin which is the
one that actually allows me to ask
locally give me the files in the
directory
and
a an
extension that actually wraps that
functionality and and adds a sample code
with a browser and some pages on top
so the flow is here i have a plugin
and the plugin starts to create a
listener using again a key from azure
saying i want to listen to this endpoint
and then
an extension in this case my browser
extension initiates the communication
through business central with some
framework code there
which is actually also an extension all
of this you can download and play with
yourself from github
and then they send the request into
azure service bus relay
and as your service bus relay says okay
i have a listener for lists and forwards
the request down
into the local agent
down there on premise
and that one
is actually responsible for forwarding
into the correct extension
of the correct plugin the plugin picks
it up
does it work in this case it could be a
give me a file
request
sends the information back
all the way
after service bus relay back to business
central
and back into the
as a reply to the original call
so
the way it's built up is this duality we
have plugins we have extensions
you can see on the left side this is a
sample of a small calculator plot plugin
probably not that interesting but it's a
nice sample here
basically exposes an add and a subtract
function and the right side is the
corresponding extension that wraps those
two calls
so it's easy to access basically you can
the
consumption of this is basically
add a reference to a code unit and you
can do calculator.add
and all the magic happens behind
there's these matching things there's
the agent plugin in the uh the shop code
which basically says this is the
relative endpoint that you are wrong
that you are connected to
and
on the right side is basically a part of
the
request
it says that it's a get call it uses the
get method in the code unit helper
and parameters i actually
put on the url
and the framework automatically unpacks
that converts it
and sends it into the
to the c sharp method that can return a
value
all this is built into framework so it's
very easy to add new plugins
and again the configuration made easy
you can read that yourself
and
again
there's a
local part of it of course that's a
local agent agent is either in this case
i run it as command line there's also a
symbol where it's
set up as a service you can try out
and again
number of parameters that has to go to
the command line to it for it to work
but that's it
so
and to to to do a final demo i actually
tried to get this guy here and i wanted
it to drive around on mars
i think that's the last known location
and do a giant pc logo unfortunately
it's very slow and no one really knows
where it is right now so i had to do
something else
and i wanted to have some old technology
so i ran around in my basement and
found
this little guy
actually it was not built when i found
it i asked my son to do it for me say i
need this so go build
this is a prime example of some of the
old technology that you will face out
there this is from 2009 it's an old api
it's actually bluetooth connected to my
surface here
i had to dig
deep to find some old documentation of
how it worked
but it actually i have i have actually
integrated this using the same
same mechanism i use the service bus
relay and the local agent to connect to
it
so let me
see if we can bring it alive
first of all i want to show you the
local agent it's here
it's basically just the command line and
you can see it currently locks
whatever i
do on it as the from before the get
drives get directory items that's what
the caller needed to
get the direction directory before
so
if i do this next brick control
it should
query it and you can see that got got a
couple of new entries here get firmware
version protocol version battery level
you can see here
some data from it
and i added some
additional um
calls to it here first of all i can ask
my
helper here to
young assistant yeah assistant
partner he will help me
and i have prepared some questions for
it so
can i ask it to tell us about business
central
[Music]
you can try again
oops
it's complaining now
[Music]
so
and as a final
experiment i will try to make it dance
um i will not do it up here because it
will definitely commit suicide if i try
it from
this one so let's see if it works better
there
so
while this is
fun and i was definitely fun doing it
it's a very good example of what
you can actually do with this piece of
code
it's not completely trained yet
thank you
and i will hand it over to gert
yeah so
what you
what what aspen showed you is you know
how you
you um connect some technology and some
some hardware
to the cloud and interact with it
through the cloud
but it's
it it's mostly meant at uh
being used with
all technology that this one which
doesn't have basically an internet
connection so things like the robot
or um
you know scales and backward scanners
some of these all hardware they don't
connect to the internet so you don't
have the you know you have to do
something you need to run an agent like
like aspen showed you
on some pc to connect with it locally
and you can use uh
the
azure
relay for that
now i'm sure you have heard of internet
of things you it's kind of a buzz word
you hear it all the time
internet of things is
basically allow you to do the same thing
you connect hardware to uh to the cloud
but it's for hardware which does have
the ability to connect and it's for
things that that are a little more
modern you know typically you know
sensors thermostats this kind of this
kind of thing and that's what get is
going to talk about
thank you
doesn't work yeah
so um to show you some stuff about
internet of things i built a connected
cookie jar
which we had running in the office for a
little bit so you can see it here
um in the in the base the in the tin is
actually uh this stuff that you can see
up here which is rather small
it's a it's a scale so
it measures the weight of the cookies
and when the cookie jar is nearly empty
uh it connects to the cloud it
connects to business central and creates
purchase order which is sent out for
approval and when it's approved
you can get more cookies so
as you can see we
we did run this in the office and people
enjoyed their cookies
so
for
people who like arduino it's a it's not
an arduino device but it's it's based on
arduino and you can you can code it with
arduino
so this is the wiring diagram
it's a it's a small device it connects
to the wi-fi
and
on the bottom right that's the scale
part and i
on the bottom left you can see i have
temperature and humidity as well just to
get get some more data
so
i'll show you so to connect it to the
cloud i used iot central so azure iot
central is a service that makes it
really really easy to connect devices to
the cloud they handle all of the the
infrastructure bits in azure for you so
you really don't have to know what's
going on
behind the scenes
so here's a little diagram
before i show you so on the bottom left
you see the iot device which is
connected to wi-fi
that one sends telemetry to iot central
it central connects to iit hub iit
device registration all of those
infrastructure services so we don't have
to worry about them
and you can set up rules in iot central
when the rule fires i you know you can
do many things but i had it trigger a
logic app and the logic app
does some authentication magic it
connects to key vault to get some
secrets
and then it triggers a custom api in
business central
which will run a workflow to create a
purchase order and send it for approval
so
now
just
before i show you how all that works if
i can get my trackpad to work
so the people at iot central
they they published repo on
on github where they have sample code
for
all sorts of devices so the one i'm
using is the the third one on the list
esp8266
but if you have a different kind of
device you can still connect it
you know using this sample code and you
really don't have to worry too much
about
the secrets behind it you can just copy
paste it and run it it's very easy
so to show you iot central if i can get
the mouse to work
that doesn't work either okay
so
iot central when you
create
an application it will look like this
and
what you have to do is you have to
create a device template
so in my case i create a template for
cookie jars
and um
i
configured it to have
some telemetry so humidity temperature
and weight and you can see
the data coming in here so this is a
graph of the last 10 minutes so not much
going on
and if you're wondering i think this is
temperature i don't know if it shows no
it's not showing how much
so
other things you can set up you can set
up settings so this is settings for the
device so in my case
i wanted to be able to control how
frequently telemetry is emitted so in
this case every 10 seconds it will send
data from the device to iot central
i also defined some properties this is
usually um just
properties about the device like serial
number
location those kind of things in my case
it's whether or not an
order is is pending so that i don't
create you know orders over and over and
over again
you can also set up commands that you
can send up back to the device so in my
case resetting the scale to zero that's
very useful because when it's all hidden
away you can't can't access the device
so it's nice to be able to do it from
the cloud
and of course
some rules so i have one simple rule
when i'm low on cookies
so that's when i'm not waiting for a
refill and the weight is less than 125
grams
i will kick off this rule
so
as actions i know it's a little yeah
so you can set up email so you can just
get an email you can call a url call a
web hook you can call an azure function
you can call logic apps which is what i
used or you can use flow or you can
connect it to
azure monitor action groups you can do
all of those things
so
once you've set up your template you can
set up an actual device so in my case i
have a cookie jar squiggy jar one
and
when you need to
connect this is all you need to do is go
to this
little page
and it will give you all the information
you need that you can plug into the
sample code and once you so the scope id
is basically the application you want to
connect to so in my case it's my cookie
jar app the device id so that we know
which device it is and
a key
you copy paste those into the arduino
code and it will
start emitting telemetry so
the samples are really super easy
so
from here i can also control the
settings and i think it's
i know
i do this correctly
so right now i have it connected to my
pc as well so i can see
what's going on in the device normally
it wouldn't have this connection but we
can monitor it through the serial bus
and so if i wanted to
have my data more frequently so if i set
this to
update every two seconds
you should see that the device
receives this event and now it starts
emitting you know telemetry every two
seconds
so it's two-way connection which is very
nice
so
you know this this screen looks
very much like the
like the template so there's there's
really not that much magic you can send
commands you can reset the scale
so
when
my rule triggers i kick off a logic app
so i can show you the uh the logic cap
that i have here it's not very
complicated
so when a rule is fired this is the iot
central pla connector
you it's very easy to configure you
don't need to know anything about
authentication it just works
so when i'm low on cookies
i get the device by device id so that
i can read its information
and if pending refill is true i do
absolutely nothing
but when it's false
what i do is i call another logic app to
get an access token for business central
so that's where the authentication magic
happens
and then with that token i can call my
business central api
which you can see here
and i pass along all the information
that i want and when that returns
successfully which means a purchase
order was sent for approval
i update the cookie jar
and set pending refill to yes
so i can show you the
other logic apps so this is the one that
does the authentication magic which is
reusable so
it's one logic app but i can use it for
any connection to business central not
just the cookie jar
so the first
logic app will send an http request and
this logic app will receive that request
when it does
it connects to azure key vault where it
retrieves a refresh token that i set up
manually before
it
parses all that data it get also gets
the client secret from azure key
vault and with that data it will do an
http post request to get a new access
token and the new refresh token
then i connect back to
azure key vault to
store the new refresh token so it's
ready for next time
and the reply back is
just the the access token and the token
type so that
my other logic app can connect
so
obviously we want to be secure at all
times so you know exposing these secrets
is not
something you want to do so you can see
on some of these
there's a little uh lock and what this
does is it it hides the
input or output
of the action so that
you can't see what happened so i can
show you that if on one of these
runs so if we try and see what the
refresh token in azure key vault was
like
it's hidden so you can give certain
people in your organization
access to editing the
the logic app obviously they can they
can see
the outputs because they can change the
logic app but you can give access to
other people
who can see the history but they can't
edit and so they will never see your
secrets so that's that's quite nice
so when the logic app
calls the custom api
we get into business central and in
business central i created the some
extensions
which add
some workflow capability so in this case
i have two workflows the first one
is this one
which is uh when a measurement is
received
then create a purchase order
based on some setup that i created so i
know which vendor and which cookies to
buy
and it will uh send that order for
approval
and
when it's sent for approval the
second one that's just
standard purchase approval workflow
that that ships with the system it's in
danish because i have a danish tenant
so
that's
kind of
how the whole thing works
we can do some more things so
over here i can see
i i have a device so this happens to be
my cookie jar
we can
using http requests we can connect to
the iot hub back end
and ask you know details about the
device so in this case i parsed out just
the set settings
and now i should
go back here
so from business central we can do the
same thing so if every two seconds is a
bit too much you can change it back to
five seconds
and you should see the device gets the
event and now
it starts emitting every five seconds
so
i think that was that part of the
so
that's not the right slide
is it yes it is
so this is again the diagram that i just
showed you so the the device connects to
iot central
which kicks off some logic apps and then
controls a
custom api in business central
so
iot central has some other features that
are very nice so one is
continuous export
so i can show you the diagram for that
one the device connecting to iot central
that's that's the same but now from iot
central it will export data to service
bus
and
i'll have a logic app
that receives messages from the service
bus and then does the same connection to
business central
so what would you use that for
so if i go into
if i go into iot central and i want it
to create some new devices so i can show
you how to
how easy it is to create a new template
in this case i'll choose custom so i get
a blank template but you can pick one of
the others that come predefined
so
let's give that a name
so once we have our template we can add
some telemetry i'll uh
let's add weight as a
some telemetry
you just fill in some of these details
weight would be in grams
let's go zero
and one kilo
and
no decimal places
so i can save that
so
this is just the template so nothing's
really happening yet
in settings
maybe we want to display a message on
the device if it had
a screen
and we can do that
and we can say
hello worlds
and save that
so now i have a new device template when
i now go to devices i can see my new
template
and automatically it will set up a
simulated device for you so even if you
have no hardware you can still try this
out
this simulated device is right now it's
being set up so
oh it's already done so we have some
data this will iot central will create
random
data for you not entirely random but
it's demo data
so that you can try out all your
integrations you can you know make sure
everything works
so
if i now go to business central
and refresh this page
i should
now i already see that i have two
devices
and
there's my nav tech day simulated device
so
what happened is that in iot central i
set up a data export
and
you can
pick where you want to export this to so
you can export to blob storage event
hubs or service bus i chose service bus
and i chose to export all my device data
so
here you can see you can you can export
all the measurements device templates
but i just wanted the devices so that i
can push my setup to business central
and i don't have to set up anything
manually
this
is this data gets pushed to
the service bus
and it gets picked up by a logic app
that's not what i wanted
this one
so it's pretty simple logic app it works
kind of like before when a message is
received in my queue
i get an access token that's the same
logic app from before to get an access
token
and once i have the token i call a
custom api for my devices
and i send over the data
and i don't have to worry anymore about
setting up my devices in business
central
so that was
what i just showed the same diagram iot
central service bus
back to logic apps
so this is a fun scenario but
iot and erp there's you know there's a
lot of scenarios you can use it for some
common ones
are
automating time registration using smart
devices you can have fingerprint
scanners facial recognition to know who
you know who was working at what time at
which station
you can track your shipments in real
time like if you order a pizza you want
to know when the guy is going to come
you know that's all iot devices
inventory management
real-time inventory no more you know
counting all your stock every week or
every month
you can track consumption of production
processes how much scrap you produce
you can use in a warehouse to automate
pick lists using rfid tags
and
a big one as well is in service
management so
modern equipment is typically full of
sensors that emit data so
if you detect anomalies you can detect
problems before they occur and send out
service people before the machine breaks
down and your customer can't work
anymore
so with that
that you get over to you thank you get
so
what get showed you and aspen is
how you can leverage some of the
services in azure and it's was a lot
about connectivity and and interacting
you know with on-prem and
this kind of thing and now we're gonna
move we're going to move into a
different type of
services which are
you know the you know the cool one based
on machine learning and and artificial
intelligence
no yes yes you can good
so yes we'll take a look at cognitive
services and in particular vision and
even vision is a big thing
so
cognitive services is actually a subpart
of the bigger azure ai and machine
learning
family and as you can see
that has a lot of
different things in there
and even cognitive services
is a lot
so you can
see it as vision and language and
so forth uh bing integration if you want
to
do
a search within your app
so
we'll focus specifically on
computer vision
and
more specifically on
recognizing handwritten and printed text
in a picture
so by the way
analyze images
is one thing you can do face recognition
and so on
moderate content will be to protect your
kids from
naughty
pictures and uh
ocr of printer text that's an oldie but
it's also up there
so but we'll take a look at a combined
example
i threw in a picture
i won't go into details but
i grabbed a picture from imdb
from a movie
and put it into the program and as you
can see it
is actually able to find some of the
words you can actually see in the
picture up there
before i continue the presentation i'll
just show you something that the team
the computer vision team did
so they created this guide
and they actually created a very cool
tool that you can use so you can
there's a lot of c-sharp examples and
good thing is that somewhere here
there are instructions on
github or how to download this from
github and
run the program which i did
so i tried to throw in a couple of
pictures
so this is a program you would get if
you compile the guitar project
so i don't know if you can read it up
there but it says that this is a
cake that looks like a face
maybe
i don't know but it tries to
analyze it
and adult content no it's this is not
dirty
um
[Music]
the racy content i had to figure out
what that meant
raising means almost dirty it's kind of
piquant i think you would say in some
languages
if you
try to take something else like a face
emmett
here
right
i don't know if you noticed but
it did made a call to azure
and it he's
he's certainly not sexy
absolutely not but you can see here
actually since he's a
known person he can detect that this is
christopher lloyd wearing a white shirt
and then apparently find something else
just to show and
there's a lot of different settings and
so on you can try out here and you have
the c
c sharp codes and which is not that
difficult to translate into al if you
want to
so i'll go back to
presentation for
a couple of slides
this is actually the same program
this is one of my kids playing football
and i just try to use different settings
so in the first one
i
used describe settings
and you can see that it can figure out
that this is a young
boy playing football on a field
this is pretty good right
and the other one where i said recognize
text it's actually able to detect some
of the um
things that are on this
right this is alex peterson and
stadium
right
kind of kind of cool i think
now this is obviously fun and i don't
know maybe this can be used for
i don't know
so
how do we weave this into
our world with accountants and so on
salespeople
so
in
business central we have uh our contacts
pro
card and
in the context card we have
a small
profile questionnaire
at the bottom i don't know if you're
familiar with this feature but we have
and these questionnaires you can set
them up but there are some standard out
of the box and you can print this
actually report where you can print a
questionnaire handout
so
this
thought of example i'm working on
here is we take this
example print it in number of copies and
then hand it out at a conference or
classroom or something or some event
and then you might imagine that people
will
fill it in
and
luckily two people did in this case
some people we know
this team
so they ticked off
you know
it's com completely ran
a coincidence that the handwriting is
the same here
so and they ticked off some crosses
there
names and
this is this is not nice writing right
and you have this
event conference and
but i mean what are we going to do with
all these things are we going to type
them in manually
and no we are not
so there's a recipe to do this but
before i do the recipe i'll just show
you in
what you can do in here
and i'll go over here
and remove christopher
i hope this didn't time out
so i have
two responses here that so i created
this small app it's basically a card
with an attached picture just like an
item
i loaded in
and the other one from the other
respondent so go back to geared
and i hope all connection is okay
click process picture
voila
so you can see that
apparently it didn't quite get the n
right right i mean
[Music]
this should be an n
and there's a space there but otherwise
it's kind of good right
and the way it
finds that
the number of employees and
what else he ticked off is that
in the scanned
result we also get the x's these appear
as the text x
so we just need to find the
question
that has an x
after
to the right of it
it's not perfect because if i scan the
other one apparently i i was
the respondent was
not as good with the crosses or the x's
right it didn't recognize those
but
so it's not perfect but
i think it's due to the boxes are out
there but anyways
overall this works and you just remove
those or make those boxes bigger or
instruct people to do it so how do we do
this
yeah we there's a short recipe so
one is to obtain a subscription
where
and by the way
there are free subscriptions i mean
free samples right you can
so you get the key and end point and the
end point is dependent on
which region you are i mean you probably
want this
region near you
then you post the request and this is
pretty similar to what esmen and those
showed so
you
at the end
then post the request
then you get a value but since since the
processing can take some time you
actually don't get the picture you just
get
a link to the result
so therefore we need to wait for it
so down here we wait for the result
to appear
and then we read the json result
and by the way the nice thing is all
these
are just
regular al types no
net or anything
and this is how
snippet of the
json result looks so i have a bigger
picture of it
and i deleted some of the surrounding
stuff just to get down to it
so you can see
once you get into it it's pretty
straightforward so you see some text
so you have the text string which is
then broken into
atoms
and one name that's broken into atoms
and then you have geared robins and
individual words
and you can see that it's it's not quite
sure that it's geared but apparently
very sure that it's robbins
and the same with
email not sure it's microsoft
but this is how you can
analyze it or you get the analysis of
the text
and
as you would know the rounding boxes are
bounding box rather
they just point to
where it is
and it actually has the full set of
coordinates because
it's intelligent enough to
have a skewed i mean now this is pretty
straight but
even if the text is angled
it will actually give you
a angled box
and this is just what i just showed you
the other thing i want to briefly show
which is something i
that is very recent on
the cognitive services or envision
so they have created something that they
call a form recognizer and this is in
preview and only in us obviously
but
this is very close to what we would like
for
what they call key pair valuing so if
you scan in something like this i mean
you can't upload but you can take their
examples
you can see that it finds invoice for
someone address
invoice number invoice date
so i i think this is certain something
we should take a look at so there are
some examples here you can click
here maybe
here this is not always responding
anyways
sometimes it does sometimes it doesn't i
think they have a very small server at
the back end
so i think this
is one of the coolest thing that is
going to come
i think that kind of concludes
the
yeah this is also
this is another example i actually took
so even a receipt like that
it's actually
able to pretty well figure out what it
is
i think that concludes sure thank you
guys
so
your question lots of application
obviously in in erp scenarios with with
this type of services
now
um
get mentioned a few times
uh telemetry and um
when he showed you the the iot
and i'm i'm going to talk a little bit
about telemetry
uh because when you when you are in the
cloud telemetry is really important so
you know the robot here
if you um
you know imagine that you want to you
know know what's going on you obviously
need to send a lot of data a lot of
information in order to figure out
what's going on monitor it and debug it
if you look at the definition of
telemetry in wikipedia it says that it's
a
the collection of measurements
or all the data at remote
or inaccessible points and their
automatic transmission to receiving
equipment for monitoring so that the the
the robot on mars is a is a good example
of that is obviously very remote
but if you think about it
um even so if you put your your software
in the cloud if you run this in the
cloud this is also an inaccessible
area you can't get to it so you need you
need telemetry but even you know even if
you are still
have on-prem installations
if you want to debug it you you you know
if your customer is 100 kilometers from
where you are you probably have to jump
in your car and drive out there and and
figure out what's going on if you don't
have any telemetry so that's why
telemetry is important
um
usually telemetry conceptually is
divided into uh several categories
and these categories are
monitoring and alerting diagnostic and
troubleshooting and usage
so monitoring and alerting
is about finding out what's going on
right now it's about monitoring the
system and being alerted if something
goes wrong
diagnostic and troubleshooting is
finding out what happened so look
looking back you know what happened if
you had a failure in the system finding
out what what uh you know what went
wrong
and usage is more about
what features
um are used you know from a usage
standpoint
by your customer or by the users of the
system and how they're using it uh how
often you know discover this kind of
information so it's not so much about
troubleshooting and monitoring it's more
about you know how the product
is used
another thing you can do with telemetry
which
you know you can you all the data i
mentioned before for monitoring and
troubleshoot you you could imagine you
could do that
in an on-prem world by logging uh
messages into a file and then you could
go and look at that file and try to
figure out what happens
but and and that you know that that
might give you the kind of you know
equivalent uh capability to do
monitoring and diagnostic
but
what you can do with telemetry which you
cannot do
in the old-fashioned way is to aggregate
across tenants so if you have a solution
installed
at many customers at many sites with
telemetry you can aggregate all these
data into one place and do correlation
between the different systems
so how to do that i
i'm going to talk a little bit about
application insights which is an azure
service
meant for telemetry and it's it has a
really really a lot of
a lot of functionality i'm only going to
scratch the surface
and show you a little bit of
what it does so how does it work you
have your extension the ids you from
your extension you you emit events to
application insights and from there
you can
look at some metrics
create some alerts get notified
something goes wrong you can do some
analytics and even do some
cool power bi
dashboard if you if you want to do that
so
the type of emissions you can do to app
insights
there are basically five five types and
the
name of it in the blue box is actually
the name of the function you call in the
sdk
so the first one is called track page
view
this is meant to be used to
track which page are shown in your
application
track trace just to log a diagnostic
message text message
track event is
a little bit like track trace but you
can also track a with track event you
would log a message but also uh you can
add some metrics to it like some numbers
and an app inside will allow you to draw
some graphs based on this metrics so if
you monitor some value
in you know for example in the cookie
jar example you could you could uh you
could use that
track exception obviously is to to track
error and there are situations
and the two last events i won't talk too
much about it because um they are more
you know for tracking certain metrics
which are not performance related for
example the size of a queue or something
that runs in the background and track
dependency is
for um
tracking if you call an external system
on external service
you can
use it in app insights to uh
differentiate from what's going on in
your own application and what's going on
in in external services so i'll focus on
the on the four on the four uh
first ones and
on github again we'll give you some
pointers at the end of the presentation
we have a small sdk that implements
these four
type of emissions for el
so let me do a quick demo
of application insights
i hope
my internet connection
is with me
let me refresh that screen
okay just give me a second so
so this is application design this is
how it looks like in the azure portal
and you can
look here at
the events that have been emitted to to
this particular service
so if i go there and look at um
all the data i haven't
emitted any data in the last 24 hours
but if i look at the last seven days i
should get hopefully some results see i
have some different type of events here
i've been emitting to to the service so
we have some page views about
um
1 600 of them various exceptions it's
artificial data generated but you get
the id right so for example if i want to
see
i can filter on
[Music]
on custom events
here
and for example i have telemetry here
that at that particular time
i run the background job i can look at
it and get the information of that
particular telemetry mission so
this background drum was called
synchronized with office 365 so that's
something you know some information i
send from
from my extension
you can also look at crashes you know if
you have any exception you can figure
out you know try to figure out what
happened
and you can also create alerts
um
so
alerts are pretty cool because they will
you know you can create notifications
let me
figure out where they are here they are
so the way it works
it's pretty simple you
create a new alert rule so you indicate
here which
which resource you want to
listen to so in that in that instance
that's my application inside service you
can have more than one
and then you create a condition
so that could be something from for
example like
if i receive this error more than 10
times or if this particular metric falls
below
a certain value
then the the rule triggers
my connection is a little bit slower
here but you get the idea so
you define the signal type could be for
example
in gets example could be when the cookie
jar
gets below a certain value
and then
when
you've defined the rule
you select an action
and that action could be
send me a text message or
or send me an email when that rule is
triggered
so
that allows you to have monitoring and
alerting on your on your system
so how how do you do that
um
let me see let me get back to the right
machine here
here we
go so let's look at how an emission to
application insight
works
basically you go and create the service
in in azure in the azure portal
and you get a you get a key
and to emit telemetry you need to post a
request to http post to that url
with a json
adjacent object containing the
information you you want to
you want to emit and this json
has a pretty self-explanatory format
for track page rooks look like this
track trace you have a similar format
but it has
some
message and
some properties
track events resemble tractors except
that you have another section
here that
contains a matrix and finally track
exceptions
you have
obviously an error message so that's how
the json you have to send looks like
so the recipe
very simple create an application inside
service
in al create the json object with
telemetry data
we have a json api l to do that
invoke the application inside rest api
doing a post request
and then you can go from there and
create dashboard dashboards and alerts
in in application insights and monitor
extension
so the code looks like this
um you have a bunch of variable
a client to uh to do post requests and
some json json objects
you create the json object so in that
example
this this particular code emits a track
pageview event
so you create the the json object that
respect the format that application site
expects
and
you just do a post request
and that's it
and it's very fast it's very small
payload uh you don't really you don't
you don't really need the response
basically it's just respond okay when
you send when you send a post request
like this so you you don't need to pass
any any result or anything so it's very
quick
so this is how you emit uh telemetry
from from your application from your
extension
uh i mentioned that in the keynote
we from from the version from version 15
of business central and above we will
allow you to bring your own application
inside key into business central and
configure it into the tenant admin
center
and we'll tell will send you a telemetry
about long-running queries
in the first in the first version sorry
for from 15x and
in the future we'll add some more
telemetry about re report execution time
and about oh data usage and we'll keep
heading
to to this so that what it means is that
if you if you create an application
inside service
use it to emit your own telemetry from
your extension
and you take that same key and bring it
to um to the tenant admin center we will
emit into that same
application inside service which will
allow you to correlate whatever happens
you know if you have a long-running
query
you will be able to correlate with your
own telemetry and find out you know is
there some relation if i have some
performance degradation for example in
the system
then you find out you know what page
have been viewed at the same time so
that you can imagine that opens up for a
lot of you know great scenarios for
troubleshooting
all right
so that was about telemetry now we're
going to get back to
cognitive services so baldur
um
talked about vision and talked about
recognizing handwriting
i'm going to talk about another area of
of cognitive services which is
translation
so obviously translation is important if
you need to
translate your extension
and from
a couple of releases ago i believe
we introduced the xliff files which is
the way
we recommend for translating extensions
and i'll show you how that works
so i have a
i have an extension here
it's very simple one which just contain
one single page and it has a
bunch of fields
like you know custom name some caption
balance
and i have some labels here just for the
sake of the demonstration and obviously
if if you want to go international and
publish your extensions in more than one
country you will need to translate your
pages
so the first thing to do is to go to the
app.json file in your extension and add
the
feature
keyword
with the translation file entry just
like that
and what happens here
when i'm going to build the extension
and take a look at the uh at the
workspace here
when i'm building you'll see that
it creates a new folder
called translation and in that folder i
have a generated xml file that looks
like this
which is a excellent file so xliff is
the international
xml standard
for translation if you talk to a
professional
translator they will know about this
format they use tools which understand
this format
and it's a pretty simple format it
contains some translation unit
like this
and there's a source
tag here that contains the original
string in the original language and when
you need to do to translate your
extension you just add a tag underneath
called target which contain
the
translated string
in the language in the target language
which we indicate here
and when you do that so if that's that's
if you translate manually
we will and you when you deploy your
extension all the magic in business
central will happen if you switch the
language in business network we will
show the translated strings that comes
from that file so all you need to do is
to
get into that generate that file which
is done by the compiler here
and add all the targets for the
translations but translating manually is
not fun
so
we want to talk we want to use the
cognitive services and and use the
automatic translation
so to do that
we have another
option which is using the translator
text which is the
azure service
and it works like like the other
services you create you create the
service and you get again a key which is
an api key you and that's all you need
to start doing translation
the api is very simple you post a
request again you know same same pattern
here you post a request to this url
indicating the source language from
which you translate to the target
language to which you want to translate
and in the body of the request you have
a json
adjacent
package with all your um your strings
and what you get back is a json result
with all the translated string in the
language you you want to translate to
so
recipe again
create a translator service translate
text service
generate the xle file
by adding this entry the features
translation file in the app.json
extract extract you need to need to pass
the file and extract it from the xliff
file
invoke the translated text api
send the json package with all of your
your strings pass the result back and
put it back in the in the in the xd file
so that's the way to perform the
automatic translation
so to do that
i have created a small extension which
is not
a business central extension
it's a visual studio code extension not
to be confused with the business central
extension so it's a
it's an extension written in in
typescript and the code is available
again on github and it but basically
what it does it implements the recipe i
just showed you before on the slide and
i'll show it to you in action
so
let's say let's pick a language here
let's say i want to translate to
[Music]
german then i invoke so this is this
command comes from i've installed this
this visual studio extension here on on
my version of visual studio code here
and this command actually invokes the
azure service and you can see the magic
happen here i have the targets
added to the file
with the translation in german for for
this text
let's pick another language let's pick
for example
french
and again
after translation that now i get the
translation in french and you can also
have like
more exotic languages like japanese
and you get translation in japanese
it supports really a lot of languages
so
when when you use the translator text
as i did here in my example when you
just create the service
you will get a pretty generic machine
translation meaning
the quality of the translation is
as good as it gets when you do generic
translation meaning the the neural
network that is behind this
doesn't know about erp so it it's not as
good
as as a human translation most likely
especially in the erp because uh erp
has certain terms and a certain semantic
that that
that needs to be
specific to uh to um
to to the to the language right
but what you can do is you can actually
create a uh a service so instead of
using the one out of the box you can
create a model and train it if you
already have translation
in your domain area whether it's
shipping or warehousing or whatever
and train with translation you already
have and you'll see that by doing that
you'll create a
so the recipe works the same way but
you'll you'll have another service you
can call with a trained model based on
some
high quality translation and you will
get a very uh very high quality of
translation out of it doesn't take a lot
of training to improve
the translation in a significant way
all right
so that was machine translation so how
much that you know we showed you a
a whole bunch of services here in azure
and you might be wondering how much does
this all cost because everything nothing
is for free actually a lot of it is for
free
there are some price indications here uh
application insights for example cost
it's free for up to five gigabytes of
data and you saw you know the payload of
the json uh it's pretty much the json uh
packages you send they're not very big
so far five gigabyte you can emit really
a lot of telemetry
translation uh you can translate up to
two million characters per month
and that's quite a lot uh that's also
for free the the um the train model i
was talking about before a little more
expensive
but if you have if you go over to two
million you know it only cost like uh
eight euro per per additional million of
characters
ocr um a text recognition that bado
showed you also you know
one to two euro
for a thousand transaction
iot central is five device for free you
know one euro per device per two euro
you know by device per month
you have some prices for logic cap and
keyboards service boss you know service
bus
very very cheap you know 0.0 43 euro per
million operations right
and and blob storage and service
possibly so you can do a lot of these
things for
almost for free and so these prices are
only you know an indication on how it
costs just to tell you you know how low
the prices of the services are
it's a little bit complicated to give
the exact price so if you if you're
interested in calculate exactly how much
it costs you can go to this url which is
the azure price calculator and you can
enter the exact parameters of the
services you want to use in which
regions and so on and it will give you
the exact price
of of these services
finally uh a couple of resources uh
again you know all these all the code
source code for for what we showed you
today is available on github
address so uh github microsoft bc tech
we uh we have an intention of keeping
adding to that repo i mean feel free to
download the code and contribute to it
ask questions there if you have any any
doubt and any uh any
questions about how to use it
and we plan on you know all these small
experiments and small prototypes and and
and cool stuff we do on the side we plan
on adding them uh to this ripple and and
hopefully you know we will have it
growing with more and more examples of
that
of that nature
we also have a blog post where we have
poster
articles which explain basically what we
what we showed to you so if you want to
go back to
some of these some of this stuff and and
and look it up in a in a blog post
format that that's the place ak dot ms
slash bc tech
that was what we had for today thank you
very much uh we have i can see we have
eight minutes left so if you guys have
some questions we'll be happy to uh to
take some questions now
yeah just
a second i'll i have a
swing box
that was you all man
wow good catch
um i wanted to ask you about the
telemetry it will be available inside
business center business center
some
logging of errors that happened i mean
like uh missing setups or such things
with the
tracing behind
so yeah so the plan so right now we have
you know as i mentioned right now the
only thing we emit is about
uh long long running queries right but
we'll keep we'll keep adding
to this and if you have you know if you
have some suggestions or something in
particular you would like to see
us emailing you know go to akrms
id that's the url right
and submit an id here and that's what we
use to prioritize uh requests right as
if people vote for it we'll uh we'll put
it in
right
there's another question here
pom-pom hi hi
talked yesterday uh but uh my question
would be about the business central
agent that you show that allows you to
connect to the
client the end user which is not
available currently when using web
client
so is this product uh produced by
microsoft and is shipped with the
product or is just a repository with the
code where we can uh where we take the
code and build the application and
publish and
not sure about the maintenance of it so
the agent i mean yeah local agent that's
so it's it's on github uh it's not a
it's not productized again it's it's a
prototype you can just grab the code
as it is and
make it your own
yeah but any any if maybe in the future
can it be
produced and shipped by microsoft and
can we trust on this or we don't we
don't have plan to ship it as a product
version of it but you know go and look
go and look it up it's very it's very
simple there's not a lot of magic
happening in there so you know you can
just as well take it make it your own
this i i don't think you will need a lot
of maintenance you know i've got to be
honest uh
i mean it's it's a few line of codes we
don't have we don't have plan on
productizing at that stage all right
okay thanks yeah but i think that i mean
another option is also to go to ak
dot ms slash bc ideas
put it as an idea and hope that enough
of all of you
upload it
it will be considered more actively yeah
right now it's just a sample
um
yeah we had an issue recently about
files and other code pages coming in um
the files which you get are not always
unicode
especially when they're from asia
they're still using lots of um
legacy code pages
and my question is can we expect any
sort of integrated function to convert
code pages to unicode
in
the future
because the japanese which you show
japanese here but if you get filed from
a japanese bank they they are likely to
be in shift gis or something
which was
they're still using that because utf-8
is not very efficient coding for asian
because they take up to three bytes
um so they are still using these code
page formats and if you get these files
you have to do something with them and
since we can't use net conversion
anymore directly
and will there be azure functions
available to do this
so you can definitely do you can
definitely write your own as a function
i think so what you're talking about is
when you have to import
files or you know payment from
from japanese banks or something yeah
yeah so we we don't have
this capability in the product today
right guys
uh
but uh yeah azure function is
is your friend
that or or actually
add a pull request as jasper is
explained yesterday and at least the
session i attended or are part of
on the
our
other github review yeah the system
application i mean this sounds like a
functionality that
could fit in there
that's something that somebody would
have in the in the in the system app and
it's on github so you know you could
write your own and do a pull request
here
all right thank you i have a question
yeah okay yeah that was a question i
have a question so about telemetry uh is
it subject to
gdpr yes yes thank you
do we need to care about privacy can we
harvest any information from the
customer yes thank you for reminding me
uh i
we agreed i was going to mention that
representative so obviously you know
when you emit
information to telemetry you need you
need to respect gdpr and be compliant
with gpr meaning
you know it's it's a pretty complicated
area but in a sense you shouldn't be
emitting any information
which is can be tracked back to um
to uh individuals things like names
addresses
email addresses
and you know the list is is is long but
to be careful with that you make sure
when you use telemetry
you're compliant with gdpr
yeah thank you for reminding me
there was a question over there hey
thanks for brilliant demos and
my question is about demo when you
send files to storage account and to
error service bus relay uh as i saw in
variables you had
some management code units either
standard code units from base app or you
created some own behind the scenes
those are
put on the github repo there's an actual
azure
blob storage library
code unit or actually extension that
wraps the functionality that was needed
to do these samples okay i think it will
be a good idea to include it in base up
thank you
any other question
over there
a question to the bc agent
would it be possible to
connect to local printers or something
like that yes yes absolutely and i mean
it's basically it's basically breaching
towards a local running component so if
you can write it in
language or connect to anything locally
from there you can do it
okay thank you
another question over there
um i have a question regarding document
previewing uh is there any plans on any
cr integrating any components uh like
from office uh to better
preview documents because we've seen
attachments coming in and stuff like
that but
we never really get an integrated
preview
so you mean for uh
things like pdf documents or yeah well
like with office there's a lot of
capabilities that you have
with microsoft right so i'm wondering
why
not better integrate yeah well you know
aka dms slash pcids okay that's uh but
is there any plans yeah
no that's not that i know off okay but
uh if you get enough votes
that's definitely relevant scenario for
sure
yeah we might no
thank you thank you
all right thank you very much
for attending this session
and
go and have fun with asia
