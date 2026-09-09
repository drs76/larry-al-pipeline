# BC TechDays 2023 - Lessons learned from migrating to .NET Core

- **Source:** https://www.youtube.com/watch?v=hQq89iLuwKc
- **Video ID:** hQq89iLuwKc
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 27m30s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

[Applause]
hello everyone we're going to talk now
about something different
so our session is about the lesson that
we have learned about
migration to the dotted core so my name
is vladisoft nagorni I have been working
with Microsoft for around six years and
in business Central for three and a half
years
I work in a platform team yeah mostly
with the back end stuff
so I've been working also on Microsoft
for six years yeah we match uh yeah so I
work in the application team but I wear
many hats in business Central so I also
work on security so I manage business
Central Security for you so just to make
you safe and yeah today we work we're
going to talk about our.net core
migration Journey yeah
so
the the short plan of our session so
we're going to cover what is the Totten
core and why did we actually need to
migrate and why why do you need to
migrate to it and then how would you
plan with the would you go with planning
the migration and uh certain migration
techniques that we have used and also
discuss some common challenges and
solutions to to the problems that we
have met and how we went with handling
the components which was not which was
not possible to migrate to doten core
and also what were the end results and
and the benefits that we have found on
during the migration
um so what is.net core
first of all the the core idea of the
dotted core is that it is modular it was
built from the ground up
and it's it's very small
um it's much smaller than the classic
legacy.net framework where you have all
the all the base types and all the
framework
in in a big number of the assemblies so
the size is much much larger and that's
not modern it's a monolithic
um the second very important aspect of
Dot and core is performance it was built
with the performance from the beginning
in the mindset
so there are actually dramatic
performance improvements and I'm going
to talk about how it affected us after
the migration
the next point is that it is
cross-platform so it's not only for the
windows but you can also run it on on
Linux and Macos
there is a possibility for the flexible
deployment strategies so it can be the
self-contained or it can use the runtime
which is installed in the system
it opens up for certain
different maintenance
strategies it has a simpler and also
more powerful build tools so there is a
new CLI and you can actually do
everything through the command line
interface now
unlike in with classic.net
it is open source so it means that it is
driven by the community so Microsoft of
course does a lot of changes but
Microsoft accepts a lot of changes from
the community
to make to make the improvements and you
can also see it transparently at the
how.net is evolving and you can follow
all the developments
and
the last bit is that it is also so the
fact that it is modular and
cross-platform and that there are
flexible deployment capabilities it
opens up for a possibility to to run on
containers especially in Linux and
windows Nana servers so you can run it's
perfect for the for the kubernetes for
example for the Azure kubernetes service
so
now that we have talked about what
is.net core and why would you need to
migrate it so how do you go with
migration
so first of all
if we look at how dotnet's framework
Compares to.net core
so there are
basically two large parts or three parts
let's say so there is application models
for example in dotnet framework there is
WPF aspenet the WCF winforms some others
and then in dotnet core there is for
example core WCF asp.core Maui also
there is WPF
and then there is also a base libraries
um then there is also a thing called.net
standard so it was created to basically
Define why one standard API of the base
libraries across.net framework and
dot-in core which which basically
unifies the the interface between them
and this was primarily made to simplify
the migration.n core without doing the
big back change to allow the the gradual
migration
um another thing that's I'd like to
cover is that.net migration guide it's
uh something that we have used and you
can also use it
to look through basically what is what
what can be the different steps during
the migration what are the different
caveats that that you might meet and
what are the different tools that you
might use
and one of the great tools is the dotnet
Upgrade Assistant
so it's uh it's actually the easiest way
to start
with the migration and and possibly it
might be the the only step that you
actually need to to perform
if only
yeah and it
um it actually exists as a common line
utility but also as a visual studio
extension and then in the visual studio
you can choose basically it from the
um
menu of the project and then you will be
offered
basically choose your way of migrating
whether it's in place or side by side
and then choose the target framework and
then look at the results
and
basically in most of the cases it can
actually convert your your project
however in in a lot of cases it's not as
simple
for example if you're using the WCF or
or some complex aspin at apis
so how will you go with the
what to do
first of all you need to list all the
incompatible functionality and
components and establish the dependency
between them
you need to define the migration
strategy for each of the components
and then start execution so this is the
simple overview of the plan
and
let's talk about how to choose the
target technology
so first of all we need to understand is
the functionality
which doesn't exist or which wasn't
possible to be converted during uh with
a with a.net upgrade advisor so is is
there an alternative functionality uh
existing and dotted core
then is there a functionality that
exists in uh in some nuget package which
is other than the you know one of your
own packages or the dotnet core
framework packages
and
also maybe you need to consider so
whether the component has has actually
been planned for refactoring or
deprecation for example if you are using
basic authentication and then this type
of authentication does not supported in
the library that you are using in Dothan
core maybe you need to consider to
switch into to the all of
um in other parts
or another technique to consider is
whether to go with the in place or side
by side project migration
so the in place is perfect for the small
isolated components
like when you just need to change the
nougat package from one to another or
yeah when the change for example takes
one day or a couple of days to migrate
and then the side by side is where you
create a new project and then do the
gradual migration of the components one
by one
for example if you have a complex web
API infrastructure
um
and then you have a lot of Integrations
or a lot of middlewares controllers some
custom Builders so you would you would
normally start with defining the new uh
project with a new host and then migrate
the controllers middlewares one by one
and then also adjust the clients if
needed gradually
um So speaking about the asp.net for us
it was actually one of the biggest tasks
to perform we had 11 endpoints of the
different sizes
especially the audit and API endpoints
that are extremely complicated to
migrate they have a lot of history
obviously
um
before we have been using the Owen which
is basically a set of interfaces which
extends the aspin app web API and
it is actually quite similar to the
expanded core so in case you are using
the oven and an aspinal cord
for you it will it will be rather
straightforward to buy great list it
will be a lot of mechanical work and
there are some nuances of course despite
the similarities
and also the good part about the
asp.core is that before version 2.2 if
this or actually before the version 3.0
it is supported by the dotnet framework
so you can start my migration in place
in the same in the same solution without
having to migrate to a different
executable or a different web host
project
and then also small parts about the
signalr in case you are using it so the
signalr core is a is a better newer
version but it also has a different
protocol it has changed so this is also
something you need to consider and
you'll see later that it's going to have
a huge Improvement on debugging but yeah
um also during the migration of aspl to
the Aspen core we found out that
by default they started to use the
system check Json it's the new
serialization component in the button
core which is more performant than
Newtons of Json which was a standard
before that
um however you might also want to
consider keeping mutants of Json as it
supports a little bit more than system
text Json for example if you are using
the data contract
serializer attributes or if you are
using the Newtons of Json tributes in a
certain way or recognition it might be
easier to start with Newtons of Json and
then consider migration to system text
Json separately
both of them they are supported in dot
not Corsa it's it's just a choice that
you need to make
another also large task that we had to
go through is WCF so it's a
pretty powerful framework that has been
introduced several years ago and even
though there is a
kind of where it may replacement in.net
core calls core wshf which has been
released last year as a first version
it's still not fully implemented the the
WCF so certain things like 90 CB binding
will not work as as expected
what's up there are certain ways that
you can consider for example the core
WCF also you might want to migrate or
you might want to consider whether you
want to move to the plane rest
controllers and then just forget about
the WCF
and if you care about the high
performance maybe the the good idea will
be to
use the grpc with weapons sockets and
also in certain scenarios you might want
to to consider to write your own custom
middleware
um
yeah so it's a lot of possibilities
another interesting aspect is whether
you want to keep the holes
or classic application configuration
format for versus to switch to the app
settings Json
basically both of them they are
supported in.net core certain settings
they are not supported so they are using
either causing the Earth or they are
silently ignored in the button core
so it's up to you it can be that you may
start with up config and then eventually
move to the app settings Json
um if you are an LL developer and you
are updating your app editing to
well if you're if your Al application
has the botnet aliens and you are
migrating them to.net core
you need to make sure to update the
assembly probing paths to remove the old
dotnet for gag and switch it to them
.net6 or dotnet core
um assembly assembly locations
make sure that if you support
if you plan on supporting both the
version 22 and the 21 and and before you
need to consider switching the settings
between the workspaces because the the
one on the left
it is supported by version 21 and before
but if you want to Target
version 22 and above you need to use the
dotnet core assembly paths
yum yep all right so
so far let's recap so far we have tried
to find alternative functionality in.net
core for whatever we had that we
couldn't just migrate
we try to basically find maybe we have
the same functionality just in sir
parking nougat
and we also we even try to see if we can
refactor the component in some cases we
even with the decompile the package take
the source codes that we need that is
that will actually work
and we will take it and make sure it
works so we tried all of this right and
it has been a long journey to get here
but are we done
sadly no business Central is a huge
product with so many components so we
still had leftovers and the next
Technique we try to address that is
compatibility mode so before we talk
about compatibility mode
let's talk about tie forwarding so tie
forwarding is a really cool feature that
allow you to do stuff cool stuff without
breaking changes so let's have an
example so let's assume you created your
dll for Tech days 22. and in that you
have created a class awesome demo but
now we're in 23 you came here you want
to update that to your new library right
take days23 and you want to use the same
class so what do you do and how do you
do it without a breaking change so you
move the code you move awesome demo to
your new library you build it it's there
perfect now you want everyone who's
using Tech days 22 to reference it
without a breaking change and still
initialize an object of awesome demo so
how do you do that tie forwarding so you
say in in that take days22 library that
hey this class has been moved to this
library and you create a type forward to
that new assembly
and simply work at that and now this is
fully supported in the AL compiler
so if you recall a while ago Vlad said
that.net standard was meant to ease the
migration to the Technic core and the
way they did it was again thanks to Tire
forwarding because most of the packages
in in.net standard are actually tied
forward to other libraries mostly MS
corlib
so now that we have Tire forwarding we
can actually explain what compatibility
mode is so compatibility mode is
basically it allows you to reference.net
framework libraries
from.netstandard and net core projects
but if we can do that so
this is again it's possible because type
forwarding but now you might be asking
the question so if we are doing this or
if we can do that why are we here in
this session in the first place or why
are we not using this compatibility mode
to reference all of our.net framework
libraries and we're done
so the thing is if you do that you will
find you will find out that compilation
would work just fine
and you will quickly figure out that it
does not cover all the dotnet framework
apis
only what is whatever was supported
in.net standard
and you're not going to get compilation
error but you're going to get runtime
error
so this actually happened to us as well
in our OneDrive integration and once we
figure that we had to actually switch
from basic authentication to OS right
and now if you upgraded to 22 and you
are writing your own application add-ins
you need to make sure that they will be
loaded in compatibility mode right which
means it's not going to have compilation
error but you might have runtime error
so
try to invest in in migration to.net
core if not
all right so again as I was saying it's
a big product huge product many
components so how do we handle the
stress of migrating to huge products
so
this is me and Vlad trying to sleep at
night while we're working on on this.net
migration
yeah we keep dreaming about the does not
migration is it going to break you once
we release 22 are you gonna come
screaming at us and say everything is
not working it's all on fire
and we wake up scared every night
but we always remember that we have good
disc coverage in our application and
platform Rebels right and that helped us
a lot
to go back to sleep safely so
the basically advice from us invest in
test automation
and we actually wanted to join the hive
of AI because everybody have including
AIS in in their slides so we would try
to generate an image using AI
for test Automation and that's what we
got so just saying
okay so let's go back to what we've done
right so we tried all that before now we
have compatibility mode but it doesn't
answer all of our questions or it
doesn't cover all of what we have left
so we have one trick left to do is to
move to whatever we couldn't move or
whatever we couldn't migrate we're going
to move to our microservice
so how business Central looks like in
22. on-prem you will find that NST have
two micro service next to it the porting
service and application proxy service
so application proxy service contains
some application add-ins that we had for
some of the local countries in Mexico
and Netherlands and it contains this
feature in there because we couldn't
move them
we also have dataverse 9.1 integration
and this is how it looks on-prem
it looks a little bit bit different on
SAS because we didn't want to so we were
in this situation where we wanted to
think
when our partners try to do the same
migration
what do you do when we ask you to join
tests to come bring your solution into
SAS and you have some.net solutions that
you need to introduce so we always say
ah just move it to an Azure function and
we thought maybe we should do the same
right so that's what we did we moved the
application proxy service into an Azure
function and really really quickly we
figured out it takes a lot of lines in L
to connect to an Azure function which is
why we decided hey let's just write an
Azure function system module and instead
of writing if you ever tried it
if it's actually was released last last
wave in 21 and if you ever tried it
instead of writing about like 20 30
lines of code just to connect to Azure
function it takes you like two three
lines
all right so at this point we're finally
done but we have some things that we
noticed so there are some let's say
breaking changes or we call it
interesting changes so the encoding
in.net
Is Now by default set to utf-8
if you have been using default encoding
before 22 you will notice that it will
default to your system settings right so
if your system settings is set to
something different than utf-8 utf-16 it
will be that right
but
here we have actually a recommendation
for you whenever you need to use
encoding
explicitly specify the encoding that you
need to use right do not depend on
default encoding because it can cause a
lot of issues and it's really hard to
troubleshoot until you figure out yeah
it was encoding issue at an end
what else this is interesting for you if
you're writing
C sharp code and and you're writing test
automation for that so debug assert
in.net core will actually crash the
process right because it's going to
throw an error
and read-only Fields in.net core cannot
be modified using reflection so if you
you're hacking your way into writing
this this way yeah it's not going to
work
all right now
the moment of truth so we spend a lot of
time doing this migration this span this
effort spanned over many release that we
had so many people have contributed to
this one and now it's time to see the
results the benefits we got from that
migration
so obviously the main benefits is
performance
so in general we actually found this
consistent computational performance
Improvement across all areas
and some of the application scenarios
you will see it was up to 30 faster
Administration task some of them got
even more than 50 percent faster
sometimes even 55.
so this is a chart from our internal
performance lab
and this is basically where we measure
some of the scenarios common scenarios
that we're using like creating a
customer posting an invoice
many scenarios that we identify right
and we use that to help or to maintain
uh performance and make sure we don't
have any regression and once we switch
to 22 once we have the.net6 uptake you
can see the graph is big for itself
huge Improvement
so
let's have that in numbers because
sometimes graphs and doesn't tell you
much
so
building our internal binaries for for
the platform we have seen about more
than 20 Improvement
and
you want to go to the next one yeah sure
so for example to start a new tenant so
a different Administration tasks like
starting a new tenant or adding new NST
nodes in our SAS environment restarting
honesty so they all got in average
around 30 to 50 percent so you can see
the difference here
um so this will affect the operations
mostly over the admins or when the
environment is under the load and needs
to scale scale out yeah so there are
some improvements yeah so hopefully when
you come to us with tickets and our
customer support is helping yeah these
process are a bit faster now yeah next
is a little bit interesting stuff for
ale right so
computational on Al
uh so if we put the you know SQL
transaction aside just pure
computational in ale and we calculated
that using hashing the best way you can
make that kind of computation you can
see that we had significant Improvement
it's like 38 and later on was like more
computational you see that we get better
Improvement the more load what we put in
on the NST so it teaches up to even more
than 40 percent
and then the last bit is again thanks to
Signal our core we got this actually
Improvement for free so our when you are
now debugging especially across the
ocean so basically you let's say you're
debugging a production environment uh on
a different region I don't know you're
on a trip you're on a business trip and
you have to troubleshoot that issue for
the customer
now that we're loading a dynamic Al file
the files that you download when you're
debugging well basically went down from
17 to 3 seconds which in some some
timing on a test machine but the
percentage is a more important part here
is that it's 80 faster
right
and with that
we actually try to have a lot of free
time at the end so maybe you want to ask
us questions maybe you have maybe you
are in this process of migrating and you
have some questions
let us know so any questions
anyone migrating maybe maybe we can ask
you some questions
anyone writing C sharp code.net code
yeah
dotnet framework
maybe the mic yeah
nice
so we had a
um dotnet component which
set up a connection to the Microsoft
message queue which is not anymore
supported with a toilet core yeah yeah
and that's just an
experimental version
have you got any recommendation
what we should or could do to connect to
the message Q on-prem even in the future
you should take a look at the core WCF
because they have just announced that
they're going to support the msmq
I think it's going to be version 1.4 or
1.5 it's already in preview I believe
good to know thank you
all right any more questions
all right if not all right yeah thanks a
lot thank you
