# NAV TechDays 2019 - {Connect app}²

- **Source:** https://www.youtube.com/watch?v=9yg-8tLNjzg
- **Video ID:** 9yg-8tLNjzg
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 102m55s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

or let's just say Waldo in vehicle Waldo
vehicle although let me ask you a
question who did attend our last our
session from previous year no I want to
see Ken's no no I want to see Clara okay
okay I have an idea you clap one hand
and raise it without like this this okay
so I'm gonna ask you another quick light
your neighbor
everyone can you not please okay ask you
another question did you all turn off
your phone oh then leave it on we want
you to have your phone on absolutely
because only liquor it's all sound
everything maybe if I switch to my PC we
want you to do our demo today because
yeah we both had a session where em for
a minute and yeah they basically fed up
to doing demo so you need to do our
demos deal meaning you are going to hack
your phone just click it from here
because apparently I'm not able to do
that take out your phone and start
downloading the Econoline yeah the
export point that's just if you don't
know that's not some malware or
something we're not stealing your credit
card we're actually giving our password
out to you later
this is just react native development
test client that was the easiest way to
share our app with you today we want you
to test our app for us and then we
release it and make money and rich and
like we never come ready to speak at
Tech days again but we will obviously
not spend too much time showing this
slide because we need to take did you
all did you all did you all did you all
download the app like let me hear let me
hear it
you see clapping is bad and nobody's
raising then but is clapping or is it
afraid of us now this app or not this
app this session is going to be about
connect app square that was kind of I
the intention of the title it's not just
connect up to its connect up squared
basically meaning we will diving in the
bits and pieces and with extensive demo
on how to connect stuff stuff with
business central now maybe diving in a
little bit into what connect up is well
basically anything from outside of
business central connect into inside of
business central and third-party app
that wants to access data execute
business logic whatever the technology
that we will use or that we have at hand
is rest web hooks and all these kind of
things the technologies that the third
party has to use is basically whatever
he wants or she wants okay so we have
done demo for you that is going to be a
nth timesheet and payroll system you
like that topic boring that's what
Microsoft wants you to think of when
they are speaking about connect apps
they're all payroll all expense
management and time sheets and stuff we
have something better so we have built a
killer app for you so let me demonstrate
that so
no nobody will nobody will kill anybody
so something is yeah which how do I
switch to this press this okay
so I'm on a my own nope so what do you
know so yeah I mean mirror my screen
yeah come on please work just stop first
and then thanks yeah I click that I will
yeah okay I mean I mean cool so there is
the killer app wall to ask me if I can
make a killer app for for our session so
I made a killer app I have this see this
killer you can see the no really it's
delayed okay so we have a fallback
solution for that so switch to one okay
I see it
[Laughter]
okay no I don't need to mirror yeah so
connected devices is this is not a
session about connect devices about
connect apps this is about apps
so I saw this let's let's try again
let's let's try this again
so I'm going to try the app switch let
me just connect this yeah
so you like it like it so far this is
very killer app yeah
well I'll try this but I don't guarantee
this will work so we had two problems
five minutes ago one was this we got it
to work it doesn't work again the
problem is the network just does not
connect the other problem was with our
business central tenant was offline okay
I mean so I hope that means now I mean I
make a good your end so Walter asked me
to build the killer app so I built the
killer app you'll still don't see any
[Laughter]
issues a broader piano I connected this
so this should be number number one over
there I'm not I'm not sending wirelessly
no it's off screen your ring is off now
yes I can take it out you brought
another one another adapter
okay now I'm on perfect good so I have a
killer app so I hope my demos go better
yeah so the killer app as you can see
the killer you can see like the name you
can see a vehicle but this was not
really what I had in mind honestly but
this is a killer app this is an app
about killers that's you should be more
specific next time about asking yeah
didn't you build anything else please
I know let's try to switch to number
three yes so yeah we did build something
else obviously and something serious
yeah and somewhat less serious we will
not tell you too much about that just
yet but we'll just tell you that you
know we couldn't make Apple accept this
app Siri
into apps or app store that's why we
have to share it using Expo there is a
user ID and password now to sign-in with
this user ID and password yeah well we
will give you a minute yeah good did you
sign in how can I make people hate me
advanced okay five four three two one
everyone okay you will see the password
again the username and password will be
them okay yeah so just a little bit of
an introduction what our custom API is
actually quite easy something that can
be developed by partner that is included
in add-on apps and can be accessed using
specific end points basically what you
can easily do is open the door to
whatever business functionality that you
have it is very easy nuts that's also
why this part of the demo is my part of
the demo building custom API and
considerations you obviously are
responsible for whatever door that you
are opening to your product it needs to
be as consistent as at all possible
Microsoft does all its best to make
their api's consistent you are basically
responsible for your own api's meaning
you must not break if you have an
upgrade of your app if you have a next
version of your app please make sure to
not break anything that third-party
applications might be integrating with
just imagine that your app is an app
source ten thousand people are using it
integrating with it and you break it
people will not be happy with that part
of your app I imagine so any kind of
rating change is basically just an app
versioning of your API is very easy to
do but please stay that two into
account it needs to act like an actual
API so include system ID to identify any
kind of record to identify any kind of
specific record include last date
modified you can already imagine that
not just any kind of table can be put or
can be let's say exposed as an API you
need to do some plumbing a little bit to
make that act as an actual API also the
camel casing which is typical and the
consistent behavior renaming for for
instance renaming a record needs to be
possible but if you're working with the
system ID yeah system ID is always going
to be that system ID and identifying
certain record but still renaming needs
to be possible if I would rename a
certain primary key of a table I need to
make sure that is will be working same
for any kind of insert a modification
behavior and table relationship and all
these kind of things okay considerations
that you need to take into account now
let's dive a little bit into how to
develop an API
well quite simple there is now an API
page that you can do is basically quite
the same as an or data web service you
now are able to create an API let me
simply show you that hopefully I already
open it yes so I have here just an
example I will zoom in a little bit I
always turn on screen costs or you know
what buttons I am pressing very simply
set an API I always put it in a separate
folder I have here a crime API and yeah
that's all I need to do create a page
page API and we'll go into these
properties a little bit later and
proceed the fields that we want to see
in the API okay
the properties I was talking about quite
important
they will define your end point later on
so first of all we have the API publish
a group and the version the version is
already there to do your app versioning
this is where you will keep your API as
consistent and and working for all the
versions stuff like that that you do not
introduce breaking changes but these
properties will identify the end point
now that will be as well it will use the
publisher group and version in the URL
and will tell well that that is
basically going to identify your end
points on top of that you have your and
the data model properties as well which
is entity name an empty set name and
this will sorry I need to show you this
because it's just very nice animation
this obviously will yet identified D and
D data now you can already see how the
URL is building up obviously when I want
to access some data in business central
I need to provide a company name so
usually a few calls need to be made to
get to the company ID because everything
is accessed through IDs then go to a
specific entity yeah I can just advance
I said probably you will have to do some
plumbing just not any table is ready to
be put our ready to be put out there as
an API first of all consider the fact
that you have the system ID now it's a
good bit you don't have to create that
actually in the earlier versions you
actually need to create a good field I
think by default was filled 8,000 or
something like that that you need to
make sure that it acts like an actual
identification of the record he needs to
be created from the moment you insert
the record and all that that's quite
some let's say yeah
Abigail called boilerplate code that you
need to copy all of the place to be able
to make that work now we have
out-of-the-box system ID and surrogate
key
that basically identifies any record and
the nice thing about this key it will
never change if you would rename your
record the kill the system ID will
remain the same it's an actual surrogate
key it's a very nice addition
it makes yeah it a lot easier to
facilitate api's you need to add the
last modified date time as well this
actually has some boilerplate code where
you need to make sure that you update it
needs to act like it's actual last date
time of this certain record primary key
consideration systematic can be the
primary key
although European this one is more
durable where I did not put that second
thing it's more durable as I already
said it's not going to be overwritten
when you would change the primary key
now if you probably know the record ID
the record I did was always changing
when you would rename a record right
that's why record ID actually is very
cumbersome to use to identify a certain
record a field consideration yeah but it
table should be a table and business
central so do not start naming your
fields as camelcase no just make it
normal case just words or whatever
what is default done in business central
later on we will we will identify or
create the API page that's where we can
yeah
identify the field name for the API to
show this a little bit I created two
branches so I've got my killer table
here actually your kill of table right
where this is basically just a normal
table with the caption and all that so
nothing special but and I have the same
for crimes so not really something
special a typical table relation if I
would introduce api's I need to do some
plumbing so you can see already here
that I added a last made modified
date/time just a normal field
in the table but I obviously also need
to update that from the moment I insert
the record I need it's lost point of
fact and so on and so on on top of that
for my killer part I introduced this
crime ID because yeah
dev Relations needs to be on terms of
IDs as well so instead of just having a
table relation with my crime code I
basically need an API level at a
relation with with an ID so I can work
with IDs within any kind of rest call
and if I update any of these I need to
make sure that the ID crime ID or the
crime code has been updated as well for
my api's but I think I need to show this
first when I will create my page my API
page the field names need to be camel
cased yeah that is you don't have to set
the application area actually I think in
the previous version application area
was necessary to set doesn't make any
sense obviously depending on what
licensing the customer has certain API
would show up so actually you need to
set all the application areas to also to
make sure that your API would act always
the same in any case in this case not
really necessary anymore so that's also
why my API pages here or pretty clean I
you I usually do it like this no
properties at all instead I accept of
the editable property if I do not or do
want to have the field editable you see
you're also no caption it's also not
necessary the caption has no influence
whatsoever on the field name in your API
call modify behavior yeah I already
showed you that you need to make sure
that whatever that you can work with
with IDs and on top of that I didn't
[Music]
yeah
it's what what happens when you turn on
your phone right yeah yeah yeah now I'm
going to switch it off okay not yet what
was I saying
oh yeah the rename part I didn't show
that again or not yet I actually don't
remember where I put it yes so I need to
make sure if I would overwrite my coat
in this k the crime code I need to make
sure that yeah the crime code is
actually a primary key but the primary
key from our API is it's my system ID so
it's going to see that maybe as a modify
so I need to make sure that the crime
code if this the same then I can just
modify my record but it's not the same I
need to make sure that I rename my
record rename behavior it needs to be
the same as well so there are a few it's
just a basic small short introduction on
API calls or to create api's some useful
resources here and maybe also a little
bit of an introduction on which tools
might be interesting to use what I use a
lot personally is a rest point you know
the rest client come on make up your
mind that makes me a yes
so the rest client is actually an vs
code extension and I actually already
have some examples here a vs code
extension that you can install obviously
in vs code and that makes you actually
able to easily create rest calls to
whatever kind of REST API that you might
have so I created this killer connection
the skill or API kind of things so maybe
I can show you the crime part and you
see already here that I can maybe zoom a
little bit more
I don't know what is it vehicle came
zoom a little bit less I mean just okay
yeah you can see here you can set up
some parameters yes you have now the
password for the web service call I
don't care this is not going to last for
long this this talent I actually rarely
didn't last up till our session yes yeah
I must say literally five minutes before
our session this tenant was completely
gone so I don't know if this click is
going to work but anyway so you set up
some parameters I basically want to
compile some kind of URL to my API and
you can already see how that your URL is
kind of like the same as I was showing
on slides now I can sub set up a get
method to my URL with write
authorization and I simply get this sent
request and I basically can test it
works the tenant is still online
so this is just to get you an overview
obviously I would probably want to
execute one of my api's being either the
killers or the crimes in this case the
crimes for that remember I need to have
my company ID so what I would be able to
do in the rest client for instance I can
get all my companies that is just to get
for my companies and in this case I'm
actually going to fill the response into
this variable which is the company's
variable what I do next I will get a
certain value the ID of a certain
company out of this company's variable
this has certain paths in Jason reply
and basically now this company ID
variables is a certain ID if I hover
over it up here I see that ID okay I can
use this ID now to get to the crimes of
my of this company basically so let me
see if I have any crimes I
get a reply but I do not get any
failures at this point that table is
completely empty you can already guess
with the rest client you can basically
test any kind of call I did some get
methods here but let's now create a
certain crime in that case I will do a
post call and now I need to provide some
kind of headers so in this case using ax
is a crime do you agree with that yeah
let's see let's see if I can make it
actually in the table yes so now it has
been adding a record if I would now
check that table here with getting the
crimes I should get one value cool ax
doesn't exist anymore
so let's rename a X into F and Oh in
that case I need basically I need to
update a record in this case there is
obviously something that's called
optimistic concurrency or at least
concurrency I need to make sure that the
ID and from the moment I read a certain
value from my table moment when I update
it the concurrency levels is actually
maintained in meantime somebody else
shouldn't have updated that record so
what you can do is using these attacks
for that so what I would do here is I
get that into my crimes at that point
you get always an attack I can copy that
and I make that part of the fetch method
to update this particular record in
using ethanol instead of using ax again
the request and now you see the response
says using ethanol is an actual crime I
would be able to also delete obviously
this is an actual crime so I'm not going
to delete this record and yeah that is
basically what yeah the rest client can
do for you the nice thing on top I I
don't know if you're using postman
probably a lot of you are using postman
personally I never did so I cannot tell
a lot
about that the nice thing about this
restaurant part is that you can save
your files as part of a project as part
of a workspace as part of a multi root
workspace however you do it as part of a
repository in their house I mean it's
very easy to just include this into the
rest of the code of your project and put
it into get for example yeah and that's
not for example actually I use postman I
converted after I saw although using
this Wow
have I been an inspiration to yes you
have what do you know you never told me
that
let me show you power $7.00 I'll show
you that later on sir okay so power cell
absolutely also is a tool that you can
use to test not only test use your API
calls I actually might not be surprised
but I use it a lot really a lot that it
is really easy to use I to invoke rest
methods with with PowerShell and
obviously with PowerShell you can
automate right let me show you in simple
example for that vehicle and the
sessions yesterday I showed you the
downside of using multi route workspaces
in together with al with PowerShell you
basically suffer from the same the fact
that al hacks the f5 method basically
makes in a multi route workspace like
this the f5 for executing my PowerShell
scripts not possible so that's why I
need to turn to yet separate workspace
this is actually the very same as this
one but anyway yeah this is just a
PowerShell script I'm will be uploading
you can already see a list or a
dictionary of of three crimes this case
and obviously now CRM is part of that as
well of anyone who did not attend a
session that's like Tobias is in the
concurrent session by the way and you
can upload like killer so I've here a
list with killers that I can simply
browse through or loop through now this
this but this is what I'm typically
doing to set up some test data
just imagine imagine and you don't have
to manage too far because Microsoft
actually kills your business central
sandboxes in a major upgrade that
actually also happened to me from the
moment we were upgrading from 14 to 15
all my sin boxes were gone luckily I had
for some demos DS this kind of scripts
where it was actually quite easy to set
up some demo data again and you'll see
later on when we talk about the killer
app that I have exactly the same script
there just to set up around our
environment yes the it is just nice to
have that just as the I do usually I
would use like a CSV file or anything
like that that I just loop through and
then I can upload my data again in my
new environment whatever
yesterday I use that for in my session
for uploading the objects and the link
says stuff like that
okay so let's execute this one this is
simply going to loop an info rest call
post message to the same kind of IDs and
you can clearly see also all the
response message that you get back from
this PowerShell statement it's actually
very nice to use I use this actually
equal to to the rest client and
obviously again this is all just code
you can upload that again with the same
project everyone can use that that
contributes to do that workspace last
tool that did help me quite a lot to
identify some problems if you have
problems sometimes whatever requests you
send from whatever language that you're
using PowerShell but also al sometimes
it's nice to just find out what is the
actual requests that you sent right how
did it look like did I actually follow
the guidelines that was actually online
or whatever request bin actually I was
using request catcher and then you
actually
who wants me to use a request pin with
action we was working yeah it's actually
a very good tool and you know it's
actually very easy to use you just sign
in actually don't have to you can just
go with the public one if you don't care
anybody else seeing your requests about
that so you just copy a certain URL and
instead of calling I think I have that
here the request bin instead of actual
calling the actual URL you just call the
request bin URL and it will just catch
the request and show you this is what
you actually were sending to this do I
have an example where I use this
variable I need to get my company's
first and then this one's will use the
request print of one so it says it
basically just has a response it is true
but I know then that here
I can see the actual request now for
this for a get it's not really
interesting if I would do like a post I
guess I can see the post message and the
actual data that I sent and I can
basically already I tend to fight the
problem here I did not include an idea I
included some kind of string that was
trying to get to an ID or especially
headers like yeah there so typically
where you fail especially from Al that
you feel but that's why I have you write
my help code and I had a lot of stuff
yes
can I you can please thank you
so we've now seen Waldo talking to these
api's and you might have asked yourself
how is he getting through because how
this how does he authenticated we saw
his username and password and you might
ask is this the correct way to
authenticate and what happened am I
still on oppressed mine I pressed yours
yeah yeah sorry have to get used to that
so let's talk about correct ways to
authenticate when talking to api's and
let me introduce the topic of auth let
me see who knows about OAuth I really
just slap whatever yell cheer as you
cheered in in in looks oh so we have two
types of authentication which are
supported with business central the
first kind of authentication is basil
indication and based authentication like
click the button and maybe it works yeah
have to be too far away unfortunately so
in basic authentication you're sending
actual credentials you're sending the
username and password
actually with business central you are
not sending the actual password you're
not using the actual user's password
you're using the web access key from the
users card which cannot be used for
anything else but accessing through web
services which is either soap or all
data or API but still you are using
direct credentials user ID and kind of a
password it does perform actual
authentication so you are when you're
connecting to the service you're
connecting directly to the service and
you are directly authenticating this the
service impersonates you at that point
it provides lower security so there are
dangers that you know if anybody catches
that information they can do anything
they want with your business central
instance app in essence they can do
whatever is available through through
API endpoints there are other risks that
I'm not personally aware of that but
Microsoft is very keen on having us not
used based authentication they know
other ways how malicious users could
actually exploit that so they say that
we should not really be using that in
production they say that we should be
using this only on Prem
or in sandboxes or during development
but for production grade access we
should use a stronger protocol which is
off authentication in all authentication
we are not using user credentials
directly and we are not really
impersonating the user what happens
there is that we delegate authentication
to a third party that we trust both we
as users and them as business central
who needs to authenticate us it provides
higher security because whatever gets
exposed is very short-lived it is based
on tokens it is not based on actual user
name and password and those tokens
typically have an expiration date or
actual expiration time rather than date
because they normally expire in an hour
it works in all environments of business
central cloud business central it also
works in all in my environments on Prem
if you are using Azure Active Directory
if you're not using Azure Active
Directory then well you well I don't
know what you could do probably probably
not much
so Azure Active Directory is
prerequisite also it is mandatory for
all clouds production environments so I
apologize yeah you don't want me to take
over this you talked you talked enough
yeah sit down yeah so what is all it's a
protocol with it's an open protocol it's
not invented by Microsoft it's used by
just about any big player out there
Microsoft Google Facebook Twitter github
all of them have off protocols all of
them actually have altought indication
they allow you to use their credentials
so this delegation allows applications
to access resources without actually
exposing user credentials to those
applications so it works through
delegation user access is just delegated
to an application no user
nation will take place at the end point
user credentials are exchanged only
between the user and the platform that
manages credentials which is a sure
active directory so since you are the
one who owns those credentials in Active
Directory Azure Active Directory it's
not unsafe to exchange the credentials
there but business central never gets
your credentials so if anybody captures
your token while you're talking to
business central your communication will
be exposed or actually anything would be
exposed only for the duration of the
token it is all token based I mentioned
token several times the application that
is connecting will receive a token from
Azure Active Directory and then it will
pass that token onwards with every
single call so if you paid attention in
world of scripts the the rest scripts
you could see that sometimes they have
authorization basic because he was
demonstrating basic with authorization
but some of them also had authorization
bear which is in fact you pass the
bearer token which is in fact the token
that you receive from Azure Active
Directory so this bearer token
authorization is what happens with auth
to zero it's also web-based protocol so
to be able to authenticate the user you
have to first play several rest calls
and depending on which of the indication
flow you employ this will be a different
flow with different requests and two
different endpoints but in the end it is
just a series of rest calls it is not
applicable if you cannot use HTTP then
you cannot use you cannot use all and
all communication happens exclusively
through HTTP but it is not a single
thing in all to zero we actually have
six different flows which define
different scenarios under which you
obtain the token in different way the
most common one is authorization code
grant and this is typically used when
you have third-party web or native apps
I will use terms third party and first
party in
when I'm talking about OAuth first party
is us a first party app is for example
an Internet app that we built for our
instance and that only we ourselves are
using inside that Internet so it will
not be publicly available on for example
App Store for anybody to just download
it we control everything we control
absolutely every single resource that's
the first party thing third party app is
when somebody builds an app like we
built the kinder app that you guys will
be using and then you will be using that
app with your own tenant that we know
nothing about that's a third party app
we know nothing about you or your tenant
or anything but you can still use our
app to access your data in your tenant
that's third party so and this is where
typically use authorization code print
the second one is implicit grant this is
typical for single page browser apps the
difference between third-party app and
single page browser app is in security
primarily single page browser apps can
only access any service from the browser
not from the backend whereas third-party
apps which are typical web apps they can
have or they typically have a back-end
and the communication with the service
happens from the backend to business
central here we are completely in the
front-end and that's the browser front
and an browser has cross-origin
restrictions browsers prevent you to
just pass random calls to random
endpoints out there and this is why
implicit grant kicks in it actually
takes care of not circumventing the
cross-origin restrictions but making it
all work nicely without violating them
the another another flow that is also
typical is the on behalf flow and this
is a pass-through flow so you have an
app that talks to an app and that app
talks to business central so you have to
authenticate is the user from this app
all the way through business central
bypassing through another app then you
have this on behalf flow we have client
potentials grant this is the typical
low for service to service communication
when you have a back-end that needs to
talk to another back-end in this case
business central then we have device
authorization grant this is for smart
devices like for example you have
anything like a dishwasher that connects
to Internet and you want to connect that
to business central or any other or
endpoint I'm making it up usually in
that case yeah maybe I don't know you
want to start like you post a journal
you want to start a dishwasher so that
is when you know you cannot there is no
keyboard on the dishwasher you cannot
really authenticate there then you use
another device so this device
authorization flow utilizes a different
device device that can really authorize
that user to use that other device to
access and then finally we have the
resource owner password credential grant
a mouthful of a grant which is used for
first typically for first party apps
with high level of trust why is that
well because this is the only one in all
of these flows that actually uses the
username and password but still it only
uses them to obtain the token not to
actually communicate to the final
service in this case business central
and the obvious next question that you
may have is which one will actually I
have a question why doesn't this work so
which flows are supported by business
central and here yeah it's a little bit
a complicated answer the first thing to
know is that it's not business central
that actually supports or does not
support OAuth is a part of Azure Active
Directory
it's a functionality that Azure Active
Directory supports or does not support
so azure active directory supports all
these six loaves and you can obtain
tokens with credentials that work with
Azure with business central through all
of these six flows however you will not
be able to use those tokens for business
central for all the flows because
Microsoft is not going to be able to
validate certain flows and you know the
problem is actually licensing they
cannot count the money they can't count
how many users
which user actually is accessing and
they say like we do not officially
support service to service if you want
to use service to service then what you
have to do you have to use either either
off user flows where user authenticates
obtains a token you put that token in
the back end and then you use the
Refresh token flow where automatically
your service has to refresh a token
every hour if that fails your back end
fails you have to go to the like front
end again obtain the token again put the
token in the back end and then restart
the service not the nicest thing however
don't let anybody you can use the
resource owner password credential grant
that works quite nice and actually Waldo
has been using this in his demo so this
is a flow where you will put your
username and password in the first
original request to the token endpoint
and you will say I want a password for
this actually say like I'm providing a
password and then extra Active Directory
gives you a token and you can use that
token with business central why is that
well business central will want to map
the token to an actual user so when
business central validates the token
against Azure Active Directory yellin
you will see what that is then as your
Active Directory will say this token
belongs to this user ID and then PC can
map that and say yeah fine we can trust
this guy the biggest problem is if they
cannot identify you as a user by user
name the flow will not work again
because they want to count the licenses
I'm not too happy as you can see with
the fact that we cannot use the most
secure service to service flows because
you know API is mostly service to
service it will be mostly service to
service I'm kind of disappointed but I
know that the guys are actually working
on that honestly they are trying to make
it work the best possible way you always
have lawyers on top that decide these
things for you so it's lawyer design
architecture call it licensing yeah
let's go with licensing yeah so you can
use this one let's talk about how
normally without thinking of business
central how would you normally choose
which grant type to use the first
question that you have to ask is who is
going to own the token and I'm not
talking about who is going to access or
etc it's just like who is going to own
that token like who receives the token
and owns the token and if the answer
actually the but the answer which grant
type you use depends on the answer to
that first question the first
possibility is that the machine will own
the token so we have a service to
service stock then the machine will
receive a token machine will consume
that token and machine will probably
refresh the token and generally manage
the lifecycle of that token in that case
we have a simple answer the correct
grant type is client credentials doesn't
work with business central maybe at some
point you know the technical guys you
know outshout the lawyers and finally
yeah
well--that's lawyers there's lawyers and
accountants even worse then if the user
owns the token if an actual user will be
will be managing the lifecycle the user
will be obtaining the token through some
kind of signing process and the users
app will be refreshing their token then
we have another question that we have to
ask what is the kind of app that is
going to be used by that user if it's a
native app which means a native app
running natively on the hardware like
our pillar app is or kinder app is or
like for example a twitter or facebook
native app not a web app something that
runs natively built compiled for that
platform then the then you have to ask
is it the first party or a third party
app if it's a first party app then
password credentials is the simplest way
to go if it's not the first party you
cannot expose credentials because if you
would expose credentials anybody could
capture them so you should go with
authorization code friend if it's user
and it's a web app then the answer is
plain it's just authorization code brand
no questions asked and finally if it's a
browser app again if it's the first
party app you could go with resource as
resource owner password credential grant
which is the simplest to implement
or if not if it's a third-party app then
you go with implicit grant which is
probably most complicated to implement
out of all these grants and then let's
talk about this authorization called
grant flow because that's the one that
will be used the most and if you really
want to follow Microsoft guidelines like
really to the letter then you should use
this one for all flows for all scenarios
so let's take a look at what this grant
is and how it actually works you are
actually very familiar with this flow
you are using it nearly every day who
has signed into let's say office 365
today asier
yeah ok Facebook using an app yep you
have used this kind of grant it's all
over the place everybody is using it
everywhere so let's take a look at
parties who participates in this flow
the first party is the resource owner so
this is typically the application that
that will provide the resources to which
you want to gain access through an API
call the second party is authorization
server this is the party who actually
owns credentials if you are in business
central your credentials are owned
maintained managed by a sure Active
Directory so this is the authorization
server in our our case and then you have
the end-user application which is going
to provide functionality to the end-user
and through that functionality you
should be able to access the resources
run by resource owner and secured by the
authorization server in our case it's
the kinder app where did we take
inspiration what was the app so this is
the flow we have a user who wants to
access business central in this case or
actually business central api's through
kinder app by using the app when the app
realizes it cannot access the resource
it will first redirect the user it will
open the browser view for that user and
will redirect the user to a web page run
by Azure Active
it's the authorization and page in that
authorization page or authorization
endpoint this is playing HTTP protocol
in happening in the browser
it simply redirects it presents the
sign-in page the page that you have seen
every time that you sign into Azure Auto
office365 using browser so this is the
azure own page that users can recognize
and trust and they see okay I'm
providing my credentials to Azure so
users are not providing credentials to
the app or to anybody else they are
merely putting them into Azure sign-in
form so when the user provides
credentials Azure Active Directory
authorization endpoint will redirect the
response not to the user but to the app
and at that point the app has to capture
those credentials and this is a tricky
part if you are in the web it's easy
because authorization endpoint or
authorization service needs an redirect
address so it needs to redirect you to a
web page to which it will provide your
authorization token so it must be a both
accessible by that server and it must be
captured by your app at the same time if
it's a web app you simply provide a URL
that will be contacted with this
authorization token but if you're
building a native app it's a little bit
tricky and then you have various ways
you will see that when I demonstrate
this in the code how this flow goes you
will see what your options are so in any
case you get redirected you capture that
authorization token which was provided
to you and then the app talks to another
endpoint which is the token endpoint and
says okay this is the authorization I
got from authorization endpoint now
please validate that and then token
endpoint will check if this is a valid
authorization code if it is it will
respond with the token and now the app
receives a token through which it can
actually talk to business central so it
sends a request an API request it
provides this bearer token to it and
then when it when business central
receives that token it still does not
know who that user is can I trust this
user is it develop token whatever so
business central will actually call the
token endpoint
we'll say okay is this token valid as
your Active Directory will say yes it's
valid token or no it's not and then
business central will be able to perform
everything else and it will pass the
data or error back to the app so looks
very efficient actually yeah there's no
performance loss whatsoever yeah
at least you know when business central
a measure on the same intranet which
they usually are all use raise it that's
just one arrows yeah no it's not it's
not it's more less errors than this but
still some errors errors good so how do
we implement this to implement this
authorization flow we have to do a few
things the first thing is when you first
access an endpoint you need to see if
you have a valid token or not so if your
app knows that it does not have a valid
token it has to redirect immediately to
the authorization endpoint then it needs
to listen to response that comes from
that either through a URL which is in
the same application domain so that the
application knows okay I've sent this
user there and now I'm receiving this
stuff back for that user or a native
Apple will simply have to listen to
whatever comes back to that browser
window and then it would have to
intercept it somehow
that's official it's not hacking and
Microsoft actually gives you some URLs
that you can use so there are two ways
how you can use it I will show that
Microsoft will give you a URL that they
suggest you use which is fake URL just
if you expose accidentally anything
through that URL it won't be exposed to
a third party just to measure and your
app so it's fairly safe and when you
receive that response then you capture
the authorization code you pass it on to
the next token the next endpoint which
is the token endpoint which will then be
used to obtain the token to send to
business central good
let me now show that in my
implementation that I've done in react
native so this is my kinder app mmm I
need to start here I mean I need to
start it up first I use it oh yeah it's
on screen so I will start I hope they
didn't change my IP address in the
meantime so so I'm starting my react
native development environment so I can
actually debug through the code I will
actually be bug step by step through
everything that's happening during this
off authorization flow and then I'm
going to attach my Visual Studio code to
my running instance of node.js and Expo
and here when my debugger attaches which
I hope it did let me see why do I not
see that
yeah it's there so I'm not going to use
my mobile phone to connect to this
instance and maybe we can just switch to
one so we can see what I'm doing I'm
going here I see that I have my kinder
app available so when I tap on that it
will open the app sorry what it's
opening the app it's now actually
compiling it's we can see what's going
on at this stage so my debugger is now
attached and I can see that I'm
compiling the bundle you have heard
about bundles yesterday it's the same
stuff so we get a bundle which is sent
to my client and yes in my app I'm now
presented with this screen where does
this come from well at the beginning my
app will see okay I don't have a valid
token so I better redirect the user to
this authentication screen inside of my
authentication screen I have this yeah
thank you inside of my authentication
screen I have this elf
sorry Azeroth screen which is a
component I developed that will handle
the browser stuff for me and to that
component I'm going to pass this
constant and this constant simply
contains the information I have obtained
from measure so I've obtained the
authorization URL from my Azure Active
Directory every tenant has their own
authorization URL per app so we have to
go to Ezzor to configure that per app
then you have a token URL per app so
this is these are my - azure endpoints
that I will have used have to use to
validate or actually to obtain my token
then I have my resource URL this is
where I'm going to this is actually what
I need to pass to authorization endpoint
and later - token endpoint to say what
is this that I'm trying to obtain access
to because if this is not embedded in
the token then business central will
simply reject the token and say this is
not a token for me this is token for
some other resource
and then I'm providing the client ID
this is my app and then there is this
client secret every app has a secret
which is something that is known only to
Azure and the app and it can change
reserve copy that secret do not
absolutely no nois you will obtain
access to our as your demo tenant which
My Account and then I have some redirect
URLs here so what i'm doing here is i'm
i use this to capture the response and
the response can either come on HTTP and
this is one that microsoft says if you
don't have any other means of capturing
response from authorization then use
this one so it's a fake address
it does exist actually so it will not
fail but it will do nothing so it's
under their control they don't listen to
it they don't care so this will just
intercept authorization token and they
say if you can intercept it otherwise
you should and actually specifications
for all of when you're implementing them
on native platforms tell you you should
actually come up with your own URL
scheme in this case kinder scheme so I
provide my own kinder scheme which I
have to register with the OS and I'm
using this only in production so if I'm
in production with my app I will be
using specific scheme so that only I
receive the token it's it doesn't go
anywhere else and in development I'm
actually going to use Microsoft's end
point that's it so now I'm going back to
my mobile screen and I'm actually going
to sorry before I go there I will just
go to this as you're all out component
this measure or all component it
actually renders the webview which loads
the authorization URL and then when I
get response
I will call my unload finished function
and then from here I'm going to extract
the token using a regular expression and
then I have a couple of debuggers this
is an async function it's a pain to
debug async functions in react or react
native so unless you put the bugger
statement explicitly you might not get
an endpoint there but in the bundle so
let's go back into iOS view
and I'm going to sign in with this user
so I'm going to type the password you
ten age please why okay and I'm clicking
sign in and I've got a breakpoint so at
this stage I have received the response
from authorization URL and I have it
here so this is my match I can also
check that inside that match I have this
match groups code this is how I
structured my reg ex and this is my
authorization token this is the token
that authorization endpoint passed to me
said okay you are a valid user I trust
you now go and obtain a token to
actually talk to that service you want
to talk to so that's what I'm going to
do I'm actually going to the token
endpoint and I'm going to pass this
authorization token so I press a5 I've
got see how slow that was really and
then I got response this is my response
it's not ready yet I need to parse the
JSON out of it so I do another a wait
and I receive JSON
so this JSON now contains this access
token I can see it here and this is the
token that I now need to pass on to all
API calls that I will be doing through
this app and then yes of course I will
just press a five here and switch back
to my app and my app now talks to
business central it took you four
minutes and 30 seconds to authenticate
okay yes okay let's now I think it's
about time we said something about ready
for demos hinder kinder app so switch
your phones on actually yeah this if you
didn't authenticate the ethic in the
expo client please do let me see who has
sorry you cannot we were some of you are
in there so who is in there let me see
okay good
amazing now you cannot use the demo yet
why is that well because I didn't switch
it on
I'm using a piece of architecture for
that as well i'm using an azure function
and i'm actually going to turn the demo
on for everybody now so i'm just going
to send a natural function request okay
it should have refreshed good so you
know the drill so we actually need to
swipe if we like or dislike so we are
building a toy store and then our goal
is to use this kinder app so that we can
gain information from our customers what
kind of toys they like and what kind of
toys they dislike and then when we put
more toys into sale we will use that
info to suggest toys that they might
like using Azure and sorry machine
learning services in that you'll see all
that so what come on yeah I like like
hey oh what a beautiful train right
amazing train good tree nice tree oh
come on
look at this cool this oh look at this
one course yeah no this is no okay so
okay good I'm done too so cool so now
that we have swiped through this and
maybe you too maybe you too
yeah if you didn't you can still try
unfortunately we didn't have any other
way to actually share this if you have
Android though if you had a yeah we
cannot do anything yeah we should have
put that one down spring actually if you
have no you cannot do anything good
let's take a look at architecture what
do we have here first of all of course
we have business central and this
business central talks to custom vision
every single item that we upload in
business central will publish a picture
into Azure sorry and Ezra custom vision
in there we have the images and then we
have kinder app which will go through
the so to reauthorize ation it's not
using obviously this one for simplicity
purposes we are using basic
authentication for your demo but we can
use all for our demo so
it reads all information about images
from business central so every image
every item with description and image
and everything it comes from business
central API and then when you when you
swipe that you like an image it Maps
that it actually sends a tag to to a
custom vision and it says this user
likes that image and that's something
that machine learning will use later to
learn from your likes what kind of items
you like and then it will suggest to you
if it's good or if something is
interesting for you or not then the app
will also subscribe to notifications to
business central we say ok I want to
subscribe to these notifications but
notifications don't work that way in
api's we will see that so we will have
something else also when new items are
coming we're using all those scripts we
will upload a bunch of items using
PowerShell they will go into business
central we will request like predictions
from the model in in the custom vision
and then the app will use a middleware
as your function f to fetch those
notifications that's the only way you
can get notifications from business
central you need to have an HTTP
endpoint in this case as your functions
and then we send predictions back to
kinder app and then it will say oh we
have something you might like
and that's it so maybe I could switch
over to to Waldo to say come on that was
faking the demo man I was actually
surprised so this is this is your like
sexual yes so this is the items and
every one of you has his or her own
random random tag and then for each tag
you can actually see how many how many
likes you have so this person likes cars
and some trains and then you can see
that this person here likes something
like cars and then whatever so we will
use this information to actually predict
when we upload more images what you like
or what you not like okay so you can you
can close this stop
making a demo well I must say I noticed
that there are quite I've noticed - yeah
they want to go from here no because I
need to control ents yeah we have a bug
in our app that is the problem so he was
fixing it done okay
um some architectural considerations in
Al you haven't seen much in Al just yet
well if you attended my session
yesterday you might already have figured
that I didn't do this in one app I
actually implant implemented this in
three apps where I have this rest
component where I basically just want to
solve the rest part I have discussed a
vision component where I basically only
want to solve the cost custom vision
part and obviously the kinder business
logic that needs this custom vision to
implement all this okay for the rest
part well why is this interesting I
think is because it only contains cares
about anything that you would do with
rest calls now just imagine I I will
show you the code in in a minute
but calling rest api's for some
including me something quite difficult
or complicated to do a nail so what we
intended for this rest apap to do is to
have some helpers on yet any kind of
rest call or any kind of json
representation so some json helpers and
some rest
helpers you will see what i mean in a
minute since this isn't a separate app
it can introduce some logging as well so
why not just log any kind of rest call
that we would do if there are problems
at some point you see me using this
request bin you will see me using you
have to request minutes actually the
only thing that you see me using then
you may be it's interesting that if
there is a problem to see what actually
of what I have sent at that point or
what the customer has sent at that point
so so why not introduce logging since
this is a separate app where we can
introduce these kind of things introduce
events
it is an app so I can introduce events
like on before sent on after sent do ya
catch and maybe change the header or
whatever if that is actual necessary for
a very special whatever call that I
would need it for so how this kind of
like looks I've got my multi route
workspace here you see you built all
three apps and this is nothing more than
some coaching it's not more than that
health precautions for rest calls and
you see here some some typical things is
you ever set content type or needed to
change the content type probably the
first time you did that took you more
than two minutes in any case these are
all things I just take care of once in a
code unit and done also the sent
introduces timing and logging so I
always know for each and every call what
was the duration of that call and I will
be logging that to some kind of table
and this is basically just what the rest
app can do for me it also has got this
Jason how about the typical Jason
functions that I can now always refer to
because I probably need that if I would
like to yeah read that response that I
would get back okay so yeah this is
again if you ever did that without any
kind of help this is actually how the
code looked like to do a custom vision
call and to upload an image to send an
image right this is basically has got
the basics the for image in there and
has a response with the image ID that
you get back with the rest up it looks
like this very simple just initialize a
certain method at request headers if
necessary and so on this is also a
downside because me explaining how to do
actual HTTP calls and stuff like that
I'm spoiled with this kind of app and
basically just three to three lines of
code is usually what I need to do a rest
call
the custom vision part is kind of like
the same you just encapsulate the all
that's necessary to do the custom vision
calls in this case I need to be able to
set up custom vision so I basically just
created a custom vision set up nothing
more than that and it has all the yeah
ideas that I need to access my custom
vision which I closed I need to reopen
that don't copy these ideas so actually
the the API representation so the idea
of the custom vision app is do be able
to do all this and understand all this
am I still sewing yes so the the thing
that I wanted to do is upload images
upload images that vehicle could read in
his app and that vehicle could basically
tag these images with your tag to which
which ones you like that was the idea so
Wow
that's why I implemented a few methods
from this I didn't implement the entire
framework that would have taken me a
little bit too long and also objects we
will talk about this to make working
with custom vision app a little bit
easier from the Kindle app because
Kindle app is going to want to like I
have got a picture here can you can you
please upload that to a custom vision
and so on so it needs to be able to do
that easily but I will go into that so
in here I have my custom vision and my
custom vision is obviously using the
rest up and all that I'm just going to
quickly show you one part where I will
show you might remember this method
pattern that I showed yesterday but this
is where it will call the rest client
very easily to in this case do that call
to custom vision and obviously a
Christian vision knows it's your URLs
right so this is why it is in the custom
vision app my other hands the Kindle app
does
care about what URLs or API endpoints or
whatever syntax that I need to do
whatever I want to do in custom fishing
that's basically a Kindle app just
implements the business logic that that
I want to implement so when the Kindred
app I just created some tables where I
want to store items and pictures nothing
more than that
but obviously I'm going to call some
business logic in custom vision to be
able to send my images and do whatever I
want to do there oh this is an example
of sending the image to custom vision
and you see here that I am using just
the current vision in this case coach
unit to set a name set the content with
the basics the for representation of my
image and just send the image done five
lines of code and I'm able to send
something to go to custom vision that
makes it structured very nice overview
if anything would happen on a custom
vision and the only thing that I need to
change or update is the kerstin vision
app and I'm basically and up and running
again but the idea at least okay so I
would like to also talk a little bit on
what is totally not an official name
which is a objectification usually a bad
thing but I think it is what I mean with
that I addressed that already a little
bit I need to make it as simple as at
all possible for the Kindle part to send
my images or use anything in the custom
vision part now you might have seen it
here this this actual API call I need to
do needs a certain JSON structure and
has a certain JSON structure that it
responds now I myself need this know
what did I need the ID because this ID
identifies the custom vision
representation of my image
and the kinder app so I need to be able
to get that idea from the response and
save that together with my image on top
of that I need to be able to compile
this kind of request to be able to
actually send my image to our custom
vision now you can already see this
should not be a responsibility or part
of the Kindle app the Kindle app needs
to be able to just create this very
easily so what we try to do is for every
JSON representation build some kind of
that's why I called objectification
because I have no name for it but some
kind of code unit that wraps this
implementation yeah of the Chasen what
you see here I have a collection of
images and within the collection of
images I basically have one image so
this is basically a call one one object
in mind my collection and on top of that
I might have tag IDs as well now to be
able to build this for again Kindle app
shouldn't care so what we do we do in
the kinder app on the top-level part
actually the top-level part should
simply be able to say hey build me an
image and where do I do that it's here
so what I have is an image cogent and
this code unit is going to help me to
build that JSON representation is I
would drill down in this coach and the
set name part for instance is just a
method within my coaching it and the
global variable yes in this case I'm
using global variables would anyone ever
attended my workshop I hate global
variables anyway I have my global main
object kind of representation this is
it's my image okay and the idea is that
this is going to be the Jason that I
will send with my request this is the
singular image I also have a coach in
its plural which is going to combine
multiple image this is my array of
images and the idea is and again by the
way in my custom vision I have that the
question of the custom vision have has
got these class Kotian as these objects
that I can
news from anywhere else to simply create
an object and simply call a method that
will obviously use the right
representation of that adjacent
representation so at when I would send
this image is obviously going to call
that code unit which uses that main
object sorry that it's this one and will
reply with that response object again to
coach unit this time not the image that
I'm sending but the information that I'm
getting back as a response the response
basically looks like this the only thing
that I needed was the ID so that's a
human thing I put in there and again
this this this this path is actually
just something that obviously only the
the the custom vision app should known
that's also why I have this object in
the custom vision part of my application
okay that's what I try to do split
responsibilities Custer vision only
knows piston vision but make it as easy
as at all possible for any other app
that uses these yeah yeah API apps let's
say to do whatever you want to do so
this is just again what I explained so
let's keep a little bit through it
because eh I spent like 50 years on off
you did luckily this was not after lines
you know okay people still fell asleep
again this is actually it's just in
slide form what I just showed you from
from the app where I'm using these code
units to pass as a parameter being
basically just direction that I want as
a response or sent as as requests here
I'm using that response by the way to
just simply save the image idea that
needed that comes from Kirstin vision as
part of an identification of my Lego
item in this case you said that ID he
needs to be able to tag it with your
like
okay ah notifications yeah
what do you know so let's talk about
notifications just wait wait wait I have
to get to that slide yeah I'm here so
why to make these notifications you've
seen earlier that we can we actually
want to receive notifications we want to
push notifications to you so that when
there are new items in the database your
application tells you look at this you
might like this one so we have that
functionality embedded in business
central API layer microsoft says don't
call us we will call you so we don't
need to Paul business central to check
for new items and then do some choices
you simply say I'm interested in changes
on this API endpoint and if the data
change occurs that would trigger a
change if you place another request to
that endpoint they will simply push a
notification to you so how does this
layer works well this is a web hooks API
for business central API any interested
party who actually correctly authorizes
them themselves against the
subscriptions endpoint can subscribe to
data changes so it means any user with
valid credentials can subscribe and then
business central will push out those
notifications when any changes occur
both standard API and custom API is
provide this there is the subscriptions
endpoint which you can use to do any
operations that manage subscriptions we
will see shortly what these operations
are and down there you can see an
example endpoint so you have a typical
endpoint to access your api's like those
EDM level API so if you add slash
subscriptions instead then you are
accessing the subscriptions endpoint
that you can use to manage any
subscriptions so what can we post sorry
send to that endpoint we can we can use
these for HTTP operations or methods the
first one is get method we are using
this one to retrieve the list of
existing subscriptions this will
these are the subscriptions that are
currently active and through that list
you can see who are not actually who
will be notified you cannot really see
that but you can see that there will be
notifications sent out when changes
occur on specified endpoints you can
create new subscriptions by sending a
post request to that endpoint in the
post request you will have to specify
what you are subscribed subscribing to
we'll look deeper into that one you can
modify a subscription which is typically
you want to request a renewal every
subscription will expire in three days
so you actually have to make sure that
as the fusion doesn't expire so if you
are still interested in receiving
notifications then you need to reset
send a page request and you can of
course switch off a subscription you can
say you can send a delete request and
you would get rid of a subscription so
you would not be receiving any
subscriptions anymore which parties are
involved well obviously business central
and the end-user application however
there needs to be somebody in between if
you are building a native app such as
our kinder app is if it is not a web app
then subscriptions are a little bit more
complicated so you have to have a
middleman a middleware where you would
have to kind of handle those
descriptions I call it notification
dispatcher that's not an official name
you may call this component whatever you
want Microsoft doesn't care your app
doesn't care I don't care so it's just
something that will receive
notifications and make sure that whoever
needs to get them finally gets them so
let's take a look at how these parties
actually collaborate first let's say
let's see how we create a new
subscription so we need to send a post
request this is an example of a post
request that I send to subscribe to Lego
items so if there is any Lego item at
this endpoint it doesn't matter where
the change comes from it can be from a
user interface or it can be from from an
API I would want to get a notification I
also pass the notification sorry I
started I started from the resource
resources
what I want to get this is the resource
that I'm interested in receiving
notifications and notification URL is
the URL that business central will call
to actually notify me that there is
something business central does not send
any other kind of notifications but HTTP
notifications to this endpoint at this
stage there is a handshake happening so
business central will first call this
notification URL so it calls it to
verify is this a valid URL and it will
pass this client state this is a random
string that you can specify whatever you
want in there like your name or
something that is specific to this
specific subscription when business
central will echo that string to this
endpoint and say okay I'm trying to
subscribe you is this valid then if this
is valid your endpoint which in my case
is a natural function would respond with
yes it's okay and it would echo back the
validation token that was passed to it
from business central at that moment
business central says okay I've done a
ping I've got a pong and my subscription
is active and then you can start using
it so how do we receive notifications
whenever there is a change business
central will send out a request a post
request against the endpoint that you
specified it's the same one that was
used for handshake it will simply just
say okay there is a change on this
endpoint and these changes are not sent
out immediately they're actually
accumulated over some 30-second
intervals Microsoft doesn't officially
say how many that is we count it it's
always 30 seconds but it doesn't have to
be maybe it's maybe they change maybe
they kind of try to make it smarter I
don't really know yeah they're they're
whispering from the front row yeah okay
in any case it's not immediate that's
the point you will have to wait a little
bit as you will see shortly
so after this time after first change
occurs all changes are aggregated over
that time window when the time window
elapses they're back together and sent
out to the endpoint and this is a
notification payload it will tell you
what kind of change happened on which
endpoint it doesn't contain any data it
simply says
this endpoint creation has occurred in
this specific example and then if you
really want to see what happened you
need to call this URL to obtain the
record that was created in this case so
this is what happens business central
sensor notification payload and then
this endpoint has to somehow dispatch
this notification it can
I don't know use signal R or use
whatever other technology to actually
push that notification out and that's
it's time to switch on our demos and I
actually cheat a little bit and I have
switched it off but I'm going to switch
it on now for you
so yes the app should be on and Waldo
will now push new items into the
database yeah obviously with powers and
yes obviously with PowerShell I'm also
going to start using the app if I manage
to connect we need to open the app I
open the app we're not using signal are
we were just too lazy you know so much
stuff to build for this demo this you
you don't want to see the to-do list
what remains and will this work I have
no idea if it doesn't work I will just
say trust me it works
switch your volume on we want to hear it
so the changes are being accumulated and
now you know
oh my app is gone rap is gone come on
work yeah yeah yeah we don't we have one
minute and 30 seconds so everything is
fine let me actually check if I've got
anything from this is
yeah there should be some notifications
to some of you at least well keep the
phone on maybe they will come later so I
think I would have to say trust me it
works at this stage it's just like you
wouldn't believe how many times we
tested this last night and this morning
and it's just like wow yeah it's maybe
it's because we try to cheat with expo
we redistributed one account to all of
you and we don't know really like sorry
we just have 45 seconds to go we really
have to close off really closed off
we'll hike oh yeah yeah oh you had one
say a slide that you need to create and
you just forgot that to create that
slide but you said you would do this one
no no no you you were going to do that
one it was your job actually anyway
thank you so much do you have any
questions we have 3d shirts and 22
seconds left so be quick and we have two
jokes to crack by the way you come up
with them anybody yeah yeah we're okay
so everybody else just doctor I almost I
nearly killed somebody
two years ago experience oh okay um you
said there was a time axis to time down
at a certain a certain final time what
what is the lifetime of an access token
and this is possible to change it
okay so the timeout for excess tokens
typically in Azure is one hour I'm not
sure if that's for all tokens they say
yes Microsoft says yes so it's one hour
and then depending on which flow you use
if you use the flow that I demonstrated
which is authorization code flow then
you will receive a refresh token so
before the time elapses you can send
Refresh token to the token URL to
retrieve a new token that will be valid
for another hour
so but not like with a resource owner
password credential request you cannot
do that that one will not send you a
refresh token so it depends on the flow
I was seeing somebody here saying this
when I was saying how business central
validates the token did they say
something wrong okay yeah yep oh sorry
it's more a question of performance when
we talk about an API the new API and
good old odana or soap are there any
issues there is the API faster or
microsoft says I have to be going to be
faster we we did not benchmark they are
fast they're very fast okay so like you
have we all been using this app here and
I'm pretty sure that it was not slow so
it was showing you images pretty fast
and also all the api's I ever did
they were just fast so you will not
experience many performance issues
unless you of course write slow mail
code in there
of course that's up to you can I get a
t-shirt without making a question no
question told me no no yes got two left
hands okay if there is no other question
the t-shirt is yours could you get the
man have this t-shirt I will throw a
split split in half oh okay yes where
okay I'm just going to give that to you
guys it's quite complex application show
today and thinking for this demo and
just a white question how much it takes
to develop it
what part yeah okay if you can
distribute it by parts because well well
the business central part if you know
I'm not going to say a few hours it was
a few days but then the most difficult
part was finding out how to communicate
with with Kirsten vision basically and
how to get I never sent a picture for
instance so so that was basically for me
some figuring out to do a few days yeah
okay and then a vacation handler for
example in Azure that was the longest I
think it has the largest number of lines
of code it has a grand total of 22 lines
of code to handle all that so it's as
your functions are pretty efficient so
yeah the react native stuff took yeah
about today to do so it's yeah so
something like that okay take three days
for the hold okay so okay the proof of
concept we got in on in under a day and
then also took me you know it I spent
quite some time with all but not because
all this complicated it's just that in
react native getting a decent component
to handle that is nearly impossible
because they recently upgraded things
and then export grated things and then I
had to build my own so that's that's why
but I didn't like it's not really too
complicated API said not too complicated
to consume it's like yeah plus we will
put all of this stuff yeah on github all
of this will be publicly available so
you will be able to go to streets you
will see it's not really that much code
already is probably fine yeah oh is it
okay well I didn't know that you should
have told me I need to take this
offensive logo yeah it's quite
interesting because right now it was the
subscription for API which are published
inside of
Business Central and is there any way
how you can manage who is subscribed on
your IPS well if you have access to
business central you will be able to
subscribe and now you have you know you
have security rules you are a user with
its own role and then your data access
will define what you can read and if you
can read an API then you can subscribe
to that API and that's it I don't think
that you have specific permissions that
control that I can read something but I
cannot subscribe to that is it possible
that's what I said in essence what I
what I explained so you need to have
users credentials to set up this
connection and then business central
merely validate who you are it will
check your permissions your role and
then it will apply those rules to
subscriptions just like to anything else
yeah by I mean that from the inside
let's assume that I am like
administrator of business central and
then I am able to check who is subscribe
to my advice ok I see where you're
aiming
so in this was a very very simple
example so how I implemented it I have
an azure function which exposes an
endpoint it receives a during handshake
it receives and it simply just pings
back whatever it receives and then later
on when it receives an actual payload it
simply forwards it into a blob actually
sorry into a cue and then that cue goes
into a blob and then I have a blob that
contains there all the changes and then
the app is pinging that to see okay let
me see if there is something for me when
you are subscribing you actually can
control absolutely everything this
client state thing is something that the
app should actually use to identify who
is subscribing because it is not just
any random string that client state
remains active throughout the lifecycle
of subscription so if I subscribe with
client state of let's say hello then
every single subscription that comes for
that will say hello in the notification
because if I have and I try that if I
have five active subscriptions with five
different client states on the same
point I will receive them so business
central that's what this line state is
for it is for you to control what to do
with the subscription otherwise yeah
business center will send some
subscription out yeah there is a change
and then you don't know whom you need to
dispatch this - okay so there is a page
there is a page that contains all
subscriptions that you can use to manage
to delete if you want or something like
that we can build an app to manage
subscriptions it's all through API it's
easy okay so me me me oh that was
anybody else okay there is a question
over there I like to throw sorry no
problem
especially over people's heads you were
talking about the tokens that you did
you get from the azure ad do they
contain like an expiration date oh yeah
so the token itself I'm not sure exactly
if the token contents about the the
payload that received you receive when
you obtain the token tells you
expiration date and time so it's it's a
JSON payload so it has number of fields
one of them is access token one of them
is expiration date one of them may be
Refresh token that you will use to refer
so you have all you have the date when
it was issued you have the date that it
expires actual date time it's yeah but
when you send the bearer for example you
just simply take that content whatever
so it's it's called
access underscore token you get that
property out that's a string and you
simply every time you pass a request you
create a header authorization content is
bearer space and content of the token
string and then it simply does all the
stuff the tax planet for three days
subscriptions available for three days
and after damages after that you can
extend them you can use a patch so you
can just patch an existing one and then
they would expect extend it by three
days okay
and the information that you lost
between the days yes that's something
you've just lost yeah so if you didn't
get notified it will not be Reno defied
yeah because and then you know you need
to be careful because those notification
payloads can contain not just delete
create update they can contain
collections they can say like okay a
number of changes happen that are too
many for us to send individuals so they
just tell you they give you a URL with a
filter that includes all of the records
that were and then you need to kind
sometimes it's difficult to figure out
exactly what happened from that but
that's the task of your application
that's a different one that's something
that api s-- must contain by actually by
convention that's what Microsoft is all
should contain no no it changed them so
why do you do with that so basically
this is the thing that we haven't told
you and this is for all of you guys that
are still here we are planning to add
the last modified to date time the same
as we did for the system ID to be out
included in every record thank our that
would be and that is going to be also
it's going to happen I'm not sure one
but definitely it's on the backlog and
the reason why we have it the last
modified date time is because you are
following really strict guidelines for
graph appears so these guidelines for
the graph a POS they're extremely strict
if you take a look at the automation
api's we don't have lost data modified
on them because it's not used it's not
needed right because you need only the
last date time modified if you use it or
if you're filtering right and graph get
additional requirements so they required
us to include it on every entity right
but but if you build your own custom API
think about if it is needed and there is
a slight risk that you will have a field
obsolete in the future okay but now it's
rather unusual that presenter ask a
question to the audience
here's the paperwork didn't tell you the
stuff because we expect you to expect
the unexpected right why do you still
have application area and captions in
your api's is there any trick push that
we are not aware of because you
shouldn't have application area and
api's that I don't think that the only
reason for that one and you can
double-check that one is the Stalcup
check but it's not which right it's not
know we tried we got got rid of them and
it just passes nicely it's a thing so
it's not using them right no no so I
think the only reason why we have them
is because of the Stalcup Chuck
okay it was easier to add them than to
update based on romance but right didn't
really think about what I would
recommend to set the application areas
because they might it be used in the
future it but allocation areas an API so
dangerous yes an API like you have two
users calling the same one and there is
a field missing or something well I
don't they don't want that yeah you
shouldn't that that was a good feedback
I think when I go back to the team we
are going to discuss about removing it
yeah because you are implicitly breaking
in an API which should not be breakable
by the drugs' and if you flip the
application area the metadata is going
to update and there should be no you
just make version dynamic and there you
go
[Laughter]
