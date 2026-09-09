# BC TechDays 2022 - Universal Code – Target must be cloud

- **Source:** https://www.youtube.com/watch?v=im0doFu6tzM
- **Video ID:** im0doFu6tzM
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 41m44s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

um my name is Christopherson I'm an
architect on the developer tools and the
compiler in Microsoft and with me today
I have brought Michael Nelson
from phone f and we're going to talk
about universal code
how many of you have heard about
universal code
my hands oh great deal good fantastic
it's a good starting point
so it's a technical presentation but I
got a few slides from Kurt who's sitting
somewhere here so if it comes to final
details on the program itself it's Curt
not us
so
but
the idea around the program is
to help us Microsoft and help you
you may not feel that way all the time
but that's the whole idea
so we want new customers to business
Central to be able to find the apps they
need in appsource
and we also want existing customers
to see a path forward from where they
are on premise a path into the cloud
where we want everyone to be
and being Cloud first that's also a way
of limited limited limited time that you
spend and we spend on upgrading
customers giving more time in the
channel for you to focus on adding value
adding good solutions for everyone
and the isolation between
our code and your code that happens when
you are creating cloud ready Solutions
also allows us to innovate more in the
base
rather than you relying on everything in
the page now you're relying only on the
surface that we provide on the base
application and the rest of our apps
and
this is probably more something you
should talk about it replace a number of
Legacy programs
and what is universal code essentially
it is cloud optimized extensions
extensions with the target set to Cloud
meaning that there's a lot of capability
in the a language and in the platform
that you won't allow to use
but the benefit of this is that they can
be implemented everywhere I mean both
on-prem in the cloud they are not tied
to a single place
so
what is the universal code initiative
it's us starting to enforce universal
code
in the platform both for on-premise and
also in the cloud words or where there's
always been like that you need to have
Target Eagles cloud and you cannot
modify the base application
we are now
starting to enforce the same
on premise
going forward
and you will be able to license the
right to use base App application and
modify and and modify the base
application and use on-prem Target
this was the
bison part and the more marketing
part of a part of slides and now we're
going into the more technical details
but first a short disclaimer
there's no one easy fix and we know it
it's hard many years of on-prem coding
have tied your two a lot of things on
premise
and you will probably encounter many
different obstacles non-prompt solution
that makes it hard to move them
and this will only hope this will only
be some possible solutions to some
problems that we'll present here
so how are we getting there
so in order to get ready
start by checking the target setting in
after Json
if it's true fine all done you can leave
at lunch whatever you want or you can
stick around and hear some ideas to what
you can do or maybe improve what you
already have done
so
I needed the demo app for this something
I could modify and change into this so I
chose a
your organizer if I happen to have a
number of beer pictures lying around for
some reason
so on this marvelous app is able to keep
a collection of pictures of beers and
you can rate them so very useful
has a number of features
first of all it's an extension
it has a gallery of peers
and if any of you now have a headache
due to last night you are feel free to
close your eyes and just I mean listen
um
you can actually import
s pictures appears into this
with a feature called Brew first batch
and you can rate them for stars which
will put a
number of stars on the picture
so
like this
so one of the first problems is that the
on-prem version I first created was
actually accessing local files to
to read in pictures
in journalists a number of local
resources which you can now not access
when you do universal code it's files it
networks it's local hardware I mean many
many solutions in the real world they
are actually talking to local hardware
it can be a scale that you waste on
something on it can be a printer it can
be a machine Real World objects
but if you're in the cloud you need to
do something else
so in this case this
app has a feature called Brew first
batch I mean it's a little bit like when
you first start on the social media like
LinkedIn you want everyone to think you
have a great big Network and have some
experience
it's the same here you don't want an
empty list of business
looks like you don't know what it is so
it has a feature you can pull in a
number of pictures and have a populated
list
in the on-prem version
it looked like this
basically using a get server directory
files list from file managing management
code unit in
in the system system application which
reach files from your local drive on the
server clearly something we will not
allow or we are not allowing in the
cloud
and if you flip the target to Cloud
you get a bunch of errors all saying
that this is not supported
in the cloud
so I had to come up with something else
and I think a Natural Choice here was
actually
to use Azure block storage
so I I created a small repository in the
Asian plot storage uploaded a bunch of
pictures and then I used the
the recent module in system application
to access Azure block storage and
reading the files and and write them
into my
image list table and actually the code
became cleaner more simple and it's
actually usable for both on-prem and SAS
and feels like a good solution
that was my solution in this case to get
around local files
um there are other
ways of doing it this is one
last time I was here in this conference
three years ago
I did a demo with a robot Lego robot
which were attached to a local computer
it's a 10 year old Lego robot which over
USB could be communicating with a
computer
and I showed how that could be done
through the cloud
what I did was
actually I using one laptop over here
oops
me sitting there
um bad picture
that's here and everything maybe it's
even a helmet so I picked another one
so I was using one computer
with a web client talking to an Azure
cloud service
and in that cloud service I used Azure
Service Plus relay to talk to another
computer with a local agent running that
way I could actually work with a local
resource through the cloud
the problem is essentially this
you have a web browser and web browsers
are shielded from accessing local
resources that's the whole purpose and
if it breaks down people tends to go and
panic
so I was using the web browser with our
lovely business Central client working
with the backend service
and I wanted to access some on-premise
Hardware
in this case I was in the same room but
I didn't have to be
by using Azure service bus relay this is
possible and the way it works is that
the on-prem service runs a local agent
that adds or creates a listener to an
endpoint in Azure service bus really
and then the cloud service in this case
business Central with some Al code can
talk to the
service bus relay and call into
on-premise even though it's behind a
firewall
the flow in this example I used it's the
demo for this is available on the PC
tech repo there's a link to it later
so essentially from
oops
I'm gonna use this
from over here
I had a supports a number of different
extensions that can handle different
areas of functionality locally
going through business Central and
calling through the using the HTTP
client into
service bus relay will
command or something
down to a local agent running as a
service or any piece of code running
locally
that had a plug-in model
and that problem all could access local
fires could write to a printer could
whatever you do with c-sharp code
and send replies all the way back
through service bus relay into business
Central and back to my El code that way
I could browse the local file system
there's that's actually a part of the
code lying around there
this is a solution for
in those cases where you want something
in the cloud to talk to local hardware
there are many cases out there where
this makes a lot of sense
so a number of different different
solutions here the last one
which are called dual service pattern I
will get back to in a second
on-prem apis the on-prem apis which are
all the ones in the base app
there's no way around those you will
have to find
another solution for those
some of them will be covered by the ones
representing files or other local
resources but there may be other things
before security reasons have locked down
on-premise
and there's probably another single
answer to those so
you will need to refactor your way
around it
then there's the good old.netic feature
many years ago in Al we gave you a
very very sharp tool and you have used
it a lot all over the place and we know
that
unfortunately there's no way that we can
support the net running in our SAS
Solutions so you have to move it
somewhere else
in my
sample program here I am using a.net
library to manipulate the pictures I
mean potentially it could be done in Al
but it will probably be very hard and
take a very long time so nothing not
something I would like to do
and the problem is essentially this I
have an extension
Target is on-prem should be Cloud they
had some cloud incompatible.net
shouldn't be there at all
and
the business Central installation that
should be anywhere
so how can we get to that first of all
we need to extract
that.net somewhere else outside
and that would allow us to make
the extension Target equals equals cloud
and also now we can install it anywhere
so now we have an external service here
with some
incompatible.net
ideally or the Dual service pattern here
actually is a way of having it in both
worlds
two different ways in the cloud in this
case I'm using an Azure function and
on-prem I'll use a local service
they are both having a reference to the
same small library that allows me to
manipulate a image
in my El code
I do this
I have an interface describing the
things I want to do
with this service
in this case there's only a ad rating
method but that could be plenty of
methods in this describing my service
interaction
then I have a single instance code unit
which is the one I use whenever I want
to interact with my service and on the
first I have this
instance procedure and I use the ability
to learn to return a complex type in
this case the interface to n
implementation
and the first time I call it I
initialize it
and in this case I do it depending on
whether I am SAS or on premise
then I have two different
implementations
one
for on-prem and one for says and in this
case they are calling conventions with a
local service are slightly different so
they are actually
not exactly the same but they're close
they're both talking both talking to a
web service endpoint
the Azure function for one and the local
Service as the other one
this means that the consumption code
becomes very clean
in this case it's
here see
service.instance add rating add get
images
page 64.
and completely hidden from all the
consuming code
another benefit of this is that this
pattern also makes it very easy to mock
out the service when you are creating
tests which you of course should
so you can create a mock service that
have a
simple mock implementation of what the
service call is doing
so let's try to run it
any preferences for cloud or on-prem
personally I prefer Cloud but
should we do that so
this is a cloud sandbox with the
upgraded solution in
oh sorry
that
there you go
I have the solution here
and it shows up first
it should be a gallery and notice the
new action bar that have unfolded my
rating actions
and I have a preferge first batch which
is talking to in this case an Azure
function
on sorry to Azure blob storage loading
in images and populating the uh the list
here
and if I change this
we can even get the PS and I can vote
for one of my favorite ones
yeah
like this using an as a function and if
I ran it on on premise
I would get the same functionality
probably spinning up my Azure function
somewhere now
and I got some stars there
and with this pattern you can extract
the.net
somewhere else and still have a
cloud ready solution
so
if this not gets if this doesn't get you
all the way we have a number of SV
Development Centers that can also help
you going further or maybe you can get
some inspiration from Michael who will
explain what they did
and this list of
further reading
so what would you Michael
thank you
okay
so when
deleting top was introduced in nav 2013.
is that correct when we did that Aspen
so it sounds right it was extremely
popular because remember back in the old
Seaside Library a string copy was the
sort of the most complex function you
had in there and that.net really gave
you the capability of getting out to do
a lot more so you could call graphical
epic libraries out there you could also
do integration so it it was sort of the
way out of there
but a lot of things have happened since
2013 and also the
dot net will start to have some cracks
and that's also being replaced by.net
core now
so a lot of things have happened
universal code is just one thing that's
pushing you away from.net which is sort
of from the old on-prem world into what
we we're doing our Cloud these days
so I'm going to uh to talk about the uh
the chances we had with using dealers in
the past with for that but also back in
the Microsoft days and also where we are
going uh and and the road to that
so um what I don't think you mentioned
but actually uh
businesses is moving to the dotted core
because that's more efficient to run on
service yes
so PC is moving away from internet
framework because you cannot run them
side by side
so no matter if you want to go universal
code or not you'll be pushed to move
away from.net framework
and it's going to be soon in my slides
which was from swing it said long term
but I Ruled that it's it's now yes that
was what Vincent also told you yesterday
also even though
you might be able to upgrade your The
NET Framework libraries to to that net
core maybe the developer that's
probably likely oh the vendor went out
of business or for some other reason you
cannot get there and also there's a huge
class of dot NET Framework libraries
which cannot be ported
so.net was based on when 32 and Dot net
Graphics in there
and that doesn't mix with the net core
at all you cannot move those elaborate
so if you're doing anything with PDFs or
order of that kind of stuff you are
you're choked in this world you cannot
use that anymore you need to move to
something else
and also universal code which
is modified code down here
so that has both a stick and a card so
the code is that customer who are sort
of reading news they can tell that okay
they want to move long term to the
clouds so that's the code the stick is
if they don't read the news Koto send
them an invoice to pay for dll support
so they'll they'll know sooner and later
that the the hard way or the the good
way so
so customers will know this and put you
guys in this room under a lot of
pressure to move away from this
also working
with dlls outside Microsoft I found out
that it's not just plug and play and
copy you have versioned conflicts all
over the place so we ever
had a dll with a reference to open XML
then is in some new version would change
to a new dll and your solution would
blow up depending on if he was the
fastest so low to his his version of
open XML or it was us so you end up
having angry Cosmos saying it doesn't
work because it cannot load oh XML and
that's because of the the conflicts
so if you do a dll today you have to do
fourth loading of types in your system
and do all sort of Hoops to get this to
work so it's not just x copy and it'll
work that's that was the story 20 years
ago but not anymore
and also once you install a new version
of your deal and you need to restart the
service here and no customer wants her
to have a restart of service here so you
have to wake
wait until late at night and restart it
and it's never a good good thing and
nobody wants to restart so that's a
reason alone too
to stay with it
so of course
we as an isv and also everybody else to
move to a way or are basically or stay
on pc14 that a lot of people are doing
that but I won't recommend that because
that's sort of your your Solutions did
uh in the water if you do that
okay
um so when eston told me you just create
a window so without I was scared setlist
because I looked at back in the late 90s
to create a Windows service you took a C
plus plus compiler and then you wrote
stuff that nobody could understand it
and it would never work it would break
down so I said no no no no it's but
actually it's it's quite easy today so
so.net has made it extremely easy to
create a service and you're guided
through this so the journey there was
not that long the actually the biggest
effort of doing this is to create an
installer that actually installed the
service but that's another story I'm not
going to cover this today
so let me run to you through the steps
so in Visual Studio you simply go in
there's a project type called Windows
service so that's easy enough so you
start there
and then you you basically add your old
donate delay code to to the solution so
for now we already had an asset function
but we use for the cloud version of of
that that was fairly easy so we just
added it and also as it's been talked
about the interface in our case is
basically we we sent over the wire that
we need a data sets with the data that
people need in the report then we have
the layout
and then we have what output you want if
you want to have Excel or PDF on and
then we have the license information so
we can judge people for for our products
so that that's basically it and and back
we get a PDF or Excel or whatever so
that's fairly easy and very suitable for
this kind of solution I'll get back to
other scenarios where it's not obvious
and you have to do something else
but it's pretty pretty forward what what
you need to do
then you add some plumbing code to uh to
state service code that you get from the
the template with your dll code
and that's basically it
so let me just bring up our solution
which is actually what we have achieving
today
and I can show the code
so what what we use will create for you
is as service based class that you'll
hear from and that has on start and on
stop down here and basically if you ever
play around with the windows service you
know that and you restart the PC server
all the time you know that you can start
or restart or start but so this these
are basically the base has been called
in here that that does that
what you also need to do or I definitely
recommend you to do is also to add
call to the wedlock so you actually
write down what you're doing so if the
service doesn't work there's no UI
remember you can actually go to the
event lock or somebody can go and say it
it stopped because of some weird error
in here
but that that's basically it next thing
you do is to to basically call The
Constructor on
on The Listener code and also what has
been talked about
and basically that's a fantastic HP
listener in it.net you can use uh so you
basically go in and spin up the
number of connections you want to use so
uh so we use 100 in here which is far
enough to for our purpose
and then you basically start listening
so now this is listening to ATP calls
that comes in and now when somebody
something comes in basically calls this
process request async and then you can
you can basically read out the the data
that was sent over the wire and do what
it with what you want to do and then
send the payload back and it's it's it's
pretty easy to do this if you already
have the pieces
[Music]
um
together in here
so we check the license information and
then render the the report and then
we send stuff back and basically we have
again the same interface inside the L
code
on our Cloud version also on this
universal code solution we have so
there's there's no difference so the ale
part of solution that we have an app
source and also on on-prem thing until
it gives up and puts on payment
appsource as well
foreign
[Laughter]
so the code is the same it's just the
delivery mechanism is is different in
here so
so extremely easy to do
um so this is sort of The Listener side
in here and if I have just one more
slide in here I can show you the
um the service and that's basically just
a PP call so you you basically can can
call your local service in here
so we have we had cheated a little
because if you want to use atps it
becomes a little more challenging
because running a
a listener on the HBS is uh I I'm not
clever enough to figure it out so I
stopped this but you can also do this of
course but we we took it to use HPS so
it has to run on the same machine as the
as a PC server but for our purpose
that's that's probably okay
so basic call it an HP call to to this
listener and it executes your call and
comes back with the results so that's
basically basically just the replacement
of the dealer
um
so just to recap on the the pros and
cons of this so
you get good happy and he doesn't send
you an invoice so it's compliant with
with your difficult
it doesn't require the restart of the
NST all the time you don't get the type
conflicts that you inevitably end up
having if you use old mix Mill of
anything that conflicts with BC or any
other lives in there
um you don't need to rewrite all your
code to go to.net core you can stay in
in The NET Framework you can also go to
core of course but the code you have
already will work in this solution and
also uh really really uh great reason
for not doing this and also what is
talked about the cloud you cannot
you cannot kill the the service if you
have a
a DL warning in in Prague with your
service here it's a dangerous thing
because it can bring down everything to
stop and you have no clue what what went
on then the customer is down and uh you
you have no idea what what caused this
so
um drawback of course there's also
drawbacks is that it works best if it's
stateless because that's sort of the the
whole idea of having these things so
keeping State requires some work on on
the server size you need to have a
window installer which is probably the
biggest part of this and also if you
have
uh a lot of calls with very little data
and it marshalling can be really
expensive because it has to go over the
wire all the time
but actually in the case of the finale
we see that our our reports were in the
faster with this solution than before I
have no idea why but it's it's around
double the the speed for uh running in
this solution even though it goes over
the wire on the same machine compared to
running in prop so
go home do this and do it now before
it's too late
thank you Michael
so I think we are ready for our
questions
any questions
we scared people away sorry or they are
just eager to get home and fix it yeah
quickly
oh that's the light sorry
thank you
with the the universal code
we have to implement our code with the
cloud Target
but the control on the the check with
the license of with our client customer
license
in which way
is made because I know that if a license
was migrated before April if I don't get
wrong
uh there will be no additional cost to
run on-prem code
but after may you have to use the target
target the on cloud Target
and but the check with the license in
which way is made
because if I add a version 19 or a 20
I don't know if the check with the
universal code
is valid
of the furthest occurred
hey so um
the check that we're going to do is in
the platform so the moment that you're
going to download the latest version of
the upcoming versions and all the
supported versions you will see that the
platform will check whether you have
loaded
um
no extensions or code customizations or
whether you have loads non-universal
code so Cloud node targeting cloud and
at that moment in time you will an arrow
will be thrown and that I will basically
tell you that you will have to license
these non-universal code modules so
that's how we're going to
all supported versions in the on-prem
version
I think we are competing with launches
so
we have more t-shirts if
I'm not sure whether you're covered it
or not but why do you use a Windows
service another web service
for the replacement of the dll
it's a small web service
and we didn't want to use uh is because
that gives a whole array of other
problems
uh because it it has this
big pudding around it which we tend to
see so it's really it's not it's really
low low footprint and very efficient
solution
and also in a lot of installations uh
the admins doesn't want to allow is
um but this always works and it's part
of windows so
thank you
more questions
first
one small question maybe what's
Microsoft effort in having like the base
app also
cloud ready let's say universal code
ready because once happened that we copy
pasted code from the base app from the
Belgium version and
when we put the target to Cloud did not
compile so maybe in general what's their
effort to
provide the same as we do
okay that's a good question
um
first of all
we are we are also trying to clean up
our
base app oh I have but we also have
parts of it where we same way as we on
the platform can do stuff which that we
couldn't allow you to do because we
after all trust ourselves more
not that we don't trust you but but
that's the reason why it is like that
but we are also trying to separate but
it's
it will be a longer process also because
whenever we make bigger changes to the
base app you tend not to like us because
then you have to change your code around
it
so we it's it's it's a long process but
we are also
trying to be clean
foreign
thanks so since pc19 we had the
possibility to integrate with the Azure
blob storage so it's part of the base
app or system map now yeah
um but one of the things that was not
introduced was basically some kind of
setup table for configuring the the
connections to The Blob storage
have any changes been made in bc21 or
the upcoming release in real life in
regards to having you know a generic
setup place where you can configure the
different accounts
I don't think so but but I think the
reason is also if if at least without
any knowing about this but my guess
would be that
if multiple extensions are using Azure
blob starts they may not want to Target
the same Azure block storage it can be
one extension actually access
some account and another will uses
another it doesn't have to be the same
no no I was interested in a kind of a
list where you could configure your
different connection endpoints so that I
can say that when I want to do
some custom file integration use this
account and instead of having each
partner each app building a custom
configuration for handling that it would
be nice and it was part of the base app
yeah
so it may be there I may not I I don't
know I have enough
where uh compiler questions
okay
more questions
so the windows service that was shown
while it was said it was universal code
compliant
as I understand it that would only work
for an on-premise solution because you
said you had to install it on the same
machine as the as BC was installed
is it would it be possible to kind of
like take the same approach that you
wrap the dll and then it somehow it
becomes like an Azure function or
something that then you could call and
from the cloud as well
does that make sense yeah I think I mean
the in the peer manager that was exactly
what I did and I think that's also what
um Michael did they have an Azure
function serving SAS customers
and an on-prem service for on-prem
installations
okay okay
I forgot to tell so one of the reasons
for having the on-prem services that uh
especially
German Cosmos don't want the data to
leave
the building and also in some some
courses the internet is really bad so
you want to have the service running on
your own machine and not in the cloud
because that's not possible
so around here it's fantastic but not in
all parts of the world and also privacy
is is a big part you don't want the data
to be out there because
after a lot of reasons
I also think if using the the pattern I
showed with the interface you could also
for individual if you have multiple
Services you can let the customer choose
where you will want the cloud one or an
on-prem installation I mean you
both is
possible
okay
thank you for thank you for joining
[Applause]
[Music]
