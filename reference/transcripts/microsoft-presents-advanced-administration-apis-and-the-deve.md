# Microsoft Presents: Advanced administration APIs and the developer experience

- **Source:** https://www.youtube.com/watch?v=2dCB8VBrLiQ
- **Video ID:** 2dCB8VBrLiQ
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 37m10s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

[Music]
hello wow it's amazing to see so many
people awesome welcome my name is Roman
I am the engineering manager of the
control plane team and we're part of the
business Central platform and
responsible for among many other things
for environment management and
administration so in this session I want
to show you how you can use the
administration API someo a tools and um
automate some of your developer
scenarios or maybe simply give you some
ideas how you can be more productive
with
automation so I'll start in the admin
Center so in the admin Center you can
see the list of environments in your
tenant and you can do all these
different Administration operations from
here uh you get to the admin Center
through the URL business central.
dynamics.com and then SL the tenant id/
admin and who can access so uh it's for
internal administrators and delegated
administrators with the role of either
Global administrator Dynamics 365
administrator or and this is new from
from this year we have introduced a new
role that is specific for administering
business Central environments so it's a
Dynamics 365 business Central
administrator and that one gives you
only access to administering business
Central environments and not to the rest
of the Dynamics
365 um uh you need to know that behind
the API uh behind the UI we have um
API and um I put the link here with the
um documentation uh for more details and
and um this is what we're going to use
the the backing
API so if we want to call our admin API
we need to set up a service to service
connection and and for that you need to
register a entra application in your in
your tenant so I would refer to this one
as the the partner
tenant and make this one multi-tenant so
that it can connect um uh to your
customer tenants and give
that application these permissions to
access the admin Center read write
all um and then we need to take that
that app and authorize it in our
customer tenant so the the destination
the tenant that we want to call and
because these permissions require admin
consent we also need to Grant this admin
consent
so I have created an
App this is my my admin app and uh what
is important to know here is the the
application ID or client ID this is the
ID that we will use later to make the
calls if we look at
permissions we see that this is the API
read write all permission that we need
to get
okay so you can you can find these
permissions um when you when you add
them under Dynamics business Central you
select it
here and then we need to authorize this
one so let's get back to the admin
Center and here you can go to Microsoft
entro apps where we list the apps that
are allowed to
call the apis for the tenant so I have
done this already
uh you would just add here um enter your
your app
ID and um then we need to Grant
consent so it looks like this when you
add the app you click on on that link
and you will get a a ground consent pop
up like this um in this case it's it's
just a test app so it shows unverified
but um I put also a link in s them
documentation how you can verify and so
that it looks nice and so as an
administrator then we will grant the
access you can see here that we
specifically want these admin Center API
permissions we say
accept and then it will also show up on
the registered Enterprise applications
in our customer tenant on the Azure
portal with the permissions that we
requested and it will say yes and
administrator has given
consent and once that is done it will
look like
this
okay so let's call the API see if it
works and for this I'm going to use some
po shell
magic
um
so I'm I'm using the
msal Powershell wrapper module here it's
a really convenient way to to use the
authentication library from Powershell
it will give access to these different
uh libraries uh that we will need to to
get the token and uh make these
calls so you will recognize again our
application ID uh we need to say which
tenant we want to connect to so this is
my customer tenant and then we need to
say which resources we want to
access and then um so this is
a conf confidential client um because
it it will know or we need to give it a
a secret to to
authenticate so how how does that work
so we want to make this automated right
without user interaction so we need to
use a server to server communication
flow without any user interaction and
and for this we can use the client
credentials flow
and this one relies on the client
knowing some some credential some secret
to to
authenticate I also put a link here uh
with the documentation it's quite well
documented and um so if we
look look at my app I go back to the
portal and you can see uh certificates
and secrets on the app and I have I have
created this one already U but so you
would you just say here new client
secret and it will generate it and then
it's important to to copy the value put
it into a safe place because once you've
done that it will um blur it out like
this so I have done that so we have the
client
secret and we have the code to make the
calls let's give it a try
y that worked no error message so far um
and then let's see if we can use the
token because that's that's another step
that's important so for this we can do a
simple call to our admin API to give me
the list of all the invironments in
tenant so this is endpoint API business
central.com
admin the version and then now we say
all applications all
environments and I want to see this in a
in a nice uh
table let's call that yes and we can see
the list of
environments uh you you get all the
different properties of the environments
here with the the response um so the
name type and also the status so you can
see some of them are soft deleted and we
have three active environments which
is also what we see
here all right so we have the app we
have it authorized we have retrieved a
token for the tenant we have done a test
call retrieve the
environments and let's add some some
automation right right we want to do
some automation um and the scenario that
I was thinking about here is whenever
there's a new business Central update
available for my production environment
um so like a minor or major update then
I want to take a copy of that production
environment into a
Sandbox
and schedule the update for my
production environment in 2 weeks so I
put the date in 2 weeks then I have
enough time to to test with the sandbox
if the update goes well and then at the
same time these copied sandbox I'll
schedule it to update
immediately and I'm going to check that
the update is successful and then in the
end it should send me a little message
on team
saying yes update is successful or
scheduled okay how do we do that so we
have already the admin API
I want to use application insights also
because this is a really good source for
different Telemetry events that are
happening um in business Central in your
environment and I want to listen or
react to some of these events I want to
use teams to integrate with teams and
then tie all of this together with a
logic
app so before we start um make sure to
set your your application insights
connection string and enable Telemetry
on on your
environment so how do we do
that so I have an application insights
instance here and what we need is the
connection string we can copy the
connection
string and we go to the admin Center and
then we set it on on the environments so
you go to the environments detail page
and here you can see Telemetry we say we
want to enable Telemetry and you put
your connection string so that means um
after a restart of the environment which
we need to do to register that um after
that we will emit all these different
tety signals to your app insights
instance and I just want to show you um
the different available Telemetry that
we're emitting it's it's really very
Broad and very useful
um different things that happen in the
environment or related to the um
environment Administration and
management and so what we're interested
in now is environment life cycle so
information about updates um or hot
fixes app updates and so on so if we
click you can see
um some examples and then some some more
details on what properties are
emitted so we can have a look I'll show
you an
example so we go to logs
here and I have a a few um queries that
I can show you so for example
um I have a few interesting environment
life cycle events that I picked out here
and if we run
that I can make it a bit
bigger so you can see um information
about uh scheduled updates or
environment updates available extensions
being updated
um synchronized and this is also a
really good way to see what happens
during an update so if you're
environment is updated and maybe there's
some issues with some extensions you can
get more details here in the
Telemetry okay so now let's try to put
some pieces together
so this is my app I called it the
environment
tracker we go to the
designer and so your your your logic app
needs some trigger and it can be um
triggered from a request or run on a on
a periodic schedule uh for this example
I've just set it up to run once a day at
5:00 that's my trigger but you could
also run it like every hour or whatever
um I'll need some variable because we
have some long running operations that
we need to check the status I'll get
back to that and then let's start with
the query of the Telemetry and what is
really nice I think with the um logic
app is that there's a lot of connectors
that you can use out of the
box um and and here um it's it's very
easy to to connect it so what we need if
I go back actually to my up insights
instance we need to give access API
access to to our application insights so
the connection string is a way to
feed um events into that instance and
the
application um key uh here is a way to
to read from it
so go
back so under configure um we can say
API access and we want to give API
access to this application insights
instance and similar to the S2s app so
you have again an application ID and a
secret
that uh you you can generate by creating
API key and then you use that in your um
logic app
to make that
connection so the query I want to run
now is to see if there are updates
available for my
environment
okay so for this we query the the traces
um I pick the event ID and I say
um uh give me the tenant ID environment
name type and so on so the properties
that I will use later in my logic
app so here you can see there's actually
two
environments that have available updates
okay so this query runs get the signal
that there's an update available and
then if an update is available I'll I'll
Branch out and do the copy and so for
the copy now we will have a call to our
admin API from the logic app so using
that same authentication flow that I
used from the pow shell API
call so in this case we want to call the
environments endpoint for my production
environment and say
copy and uh in the body you need to pass
the destination environment name and
what type of environment you want to
copy to and again I would refer to the
API documentation for details on on
these different parameters on the
different API
endpoints and in terms of authentication
we basically need to do the same thing
so we pass the destination tenant our um
audience that we want to get the the
token for our client ID and the
secret and in parallel we do an update
of the scheduled update date for for the
production environment and I think what
is also really nice here there's a lot
of functions that you can use out of the
box um so here I'm just going to
schedule it for 14 days in the future
and I will also say um we do want to run
this with within the the update
window
okay should we run this let's see what
happens
so if you want to see uh what's what's
going on uh there's the Run history and
we can look at this run that was just
triggered and see what's what's going on
where are the actions what what is it
doing so it went through our trigger
initialized the variable we quered app
insides yes there are updates
available we triggered the copy set the
update dat to the
Future and now you can see uh we're
waiting here on the copy
operation so the copy operation usually
takes a few minutes so I I built a loop
here to
say check so after triggering the the
copy wait a minute and then check the
status of the
operation and I think what is also
really useful and and Powerful here is
that you can refer to Output of previous
actions to
um to
run uh subsequent
actions good so let's have a look
um can go back to the API and see what
what's happening
so for this we have the operations end
point and if I call this one so this is
for my production environment I want to
see all operations that are
ongoing so you can see there's quite a
few and there's a running copy operation
here
yes okay this is
what what we have triggered here so
um while this is running let's go back
to the admin Center I want to show you
the operations log um
you can also see here yeah there's a new
environment that's being prepared that's
the one we're copying and I want to show
you here the operations because I think
it's really cool so this is a list of
all the different operations and actions
that that happen on the environment um
from from Administration point of
view uh it's a bit like a not an audit
uh Trace but it's it's kind of a log
really to see what what happened and and
who did what so for example what we can
see now
we have an operation a copy operation
that is created by this this good here
and this is the ID of the app that I
have used to call the API to trigger
this right and this is running and you
can see other operations that I have
triggered as a user and then it will
show my my username
here so this is
running good okay so this is running
let's continue I'll go back back to the
designer okay so the copy operation here
um um as I said it's a long running
operation um it will return status code
202 accepted and then pass me the
operation ID with which I can then later
on check the status so this is I I do
this here and here you can see this is
using a parameter from the result from
the response of the previous copy
operation Okay so
um I have I've set this up now in in a
way that um if I run this again um and
the environment the destination
environment exists already this is just
for um for demonstration purposes I
think it's easier to show like this um
so
that next time we get here um
the request to see if there's an update
available for the copied sandbox um will
will come here in this branch
and then do the schedule of that update
to run
immediately
okay let's have a quick look what's the
status
here okay this is running all right so
what we want to get so we want to get
the upgrade status of the of this the
sandbox
copy and use that information to
schedule it to run
immediately um and here now we can say
run on UTC now immediately and ignore
the update window so this means it will
run as soon as possible usually there's
a maybe a small one 2 minutes delay and
then it will be picked up and and
executed the
update and then because I like teams I
like to get these little
notifications um I I have here now as a
as a the final step um a message that
the the flow bot will send me and say
update of the environment has been
scheduled and here also this is a
built-in connector that you can just
connect to your account and it it will
send you a message
okay this is still running all right so
there's a a few more possibilities that
I I want to kind of show you that you
could also do so now in this example I'm
reacting to an environment update that's
available from from
Telemetry um what you could also do is
you could if you have a set of apps that
you're responsible for that you're
developing you could install these apps
on the
sandbox before you run the update and
then make sure that the update of your
app is successful with the update of the
environment you can also check if
there's app updates available so for
example if
you um if you're again responsible for
for a bunch of apps and you want to make
sure that those get installed on
environments of your of your customers
for example you can check if there's
updates available and then install them
in all the tenant in um that that you
would want to do that so automate that
roll
out and then kind of to to close the
loop uh I don't have that in the example
but it's basically the same thing so we
could listen to the environment updated
signal to get the result of the update
um and that could look like
this so let's see if the cop is
done yes so we have our copy of the
environment the
sandbox and we can already see uh it's
it already shows me there's an update
available so if I look
here yeah
so this is still running
probably
until the copy operation is complete um
let's have a quick look at that
[Music]
mhm
yes so now I want to try the the other
Branch right so we want to schedule the
update now to run
immediately let's run it again
okay so this is
running and we can see that our copy
request did not succeed
um and we can also see then why um in
the in the output here so in this case I
reached the number of environments that
I have
um but this is now intentional so I
wanted to go into the other Branch so
query the update information on the
environment and we have seen already
there is an update
available for the
sandbox yeah so you can see
um we're on 24.0 there's 24.1 available
and I can select the date
uh haven't selected it yet so this is
this flag here and uh yeah it's
scheduled but we want to run it
immediately
right so we have done this
call and it's also
successful let's go back
here and I can see yes the environment
has been triggered to to update and you
can see it's already updating we we see
the the changing status and it is
updating
okay all right if I look in my my chat
guess my team spot has also informed me
the update has been
scheduled and um yeah I think this is
nice um I actually think this this is a
a pretty cool feature I like that um
having kind of this idea that there's
some some b or some automation taking
care of of these processes and at the
end it just sends me a little message on
teams saying you know I'm done it's it's
done your update has scheduled and you
could hook this up for example also with
checking the the success um of of the
update but that would now take too long
for for this session today we use it
also for for other flows other Purp
purposes um like requesting pool pool
request comments
or
um I also use it for for the the wine
club if there's a new event from the
wine club available I get a message from
from my bot and say uh you know there's
an event and I will I will make sure to
sign up quickly because those fill up
very very
fast all
right I have a little bit of bonus
content also for you um some new
features that we
have just shipped or will ship soon so
first thing is a a new self-service
capability in the admin Center that you
can transfer environments from one
Microsoft ENT tenant to
another and I have some time so I'm
going to just show you how this
works so from from from the admin Center
and and this is one of the operations
that you cannot do through API um just
for security reasons we need
a um internal administrator that has the
the um the administration permissions to
do that on the sending tenant and on the
receiving tenant so this is a new button
here new feature and with this you you
can say I want to transfer an
environment
you select the environment and you you
put your
destination tenant ID and so this is
useful for example if you imagine you um
you you have a you you're preparing demo
environments or you you're setting up
some
um uh some environments for for somebody
for a customer you can do that um and
once you're done just transfer it to
that customer
tenant and uh what the receiving um
tenant then has to do also you need an
internal administrator log in here and
say receive environments you specify the
source where the environments are coming
from and then there's an an approval
step um which basically make sure we
have it
handshake um and then the the transfer
will run and you can schedule at what
time it it should
run also some of you maybe have faced
this um we had or yeah we had a a cache
cach delay so whenever there's a new app
version that you upload through
appsource and it makes its way through
the validation steps and it comes to our
services there was a delay that could
take up to half an hour until it was a
available to update on the tenants so we
have eliminated this this cache um it's
much faster now um almost instant um as
soon as it re reaches our our services
the new version so that should make make
you also a bit more productive and you
don't need to wait that that time and
then I want to announce
um uh some something more uh something
we have planned for later this year
which will also make that
API um
scenarios uh easier for you so we want
to have the ability to give you kind of
a discovery endpoint where you can see
which um environments you can manage
with your S2s app so the as a partner
now you can call this new endpoint and
you will see which tenants you can
manage that should make these
multi-tenant scenarios much
easier yeah and I see I have still a few
few minutes for for
questions
um
yes
yeah yes there's um think I can pass
this test
yeah thank that new um role that we now
have yeah will that give us enough
privileges to uh Grant use the grant
functionality of the intra apps in
the in the admin Center or does it
require higher privilege roles uh to
yeah no to to Grant the admin consent no
no it will not yeah no okay yeah thanks
I think there's a special role um yes as
an app administrator yes I think Cloud
app administrator that's a different or
yeah okay
thanks
mhm I'll give you a t-shirt because
you're the first person asking a
question
nobody that's
okay yeah anyway um if if you don't have
other questions oh there's one more
otherwise I'll be I'll be around still
um you can reach out I'll be happy to
answer is there a way to pre
preauthorize uh your application for for
all your
customers so make it some automatic way
so in order that I don't need to Grant
consent in each ah yeah no so that's
that's still a requirement that you need
to Grant the admin consent in each of
the tenants each of your customer
tenants that you want to
call so we we try to make it easier just
by having that link directly on the page
you just click the the link um but
that's just part of it's by Design
basically that you want that customer
administrator to give That explicit
comment because it's a very powerful um
permission yeah maybe I was wrong the
ground should be done by the customer
yes but the uh this initial part when
we associate or uh the authorized part
like add it mhm yeah
um no you need to do that also yeah yeah
you need to do that also yeah that's
kind of the first connection step that's
needed yeah
mhm all right
um I'll give you also a
t-shirt here you
go okay um yeah as I said I'll be around
feel free to to reach out and then with
this I will
hand you over to my my colleagues
Christian and Rainer there will be a few
short minutes break um until they're
ready and then i' say just thank you
[Applause]
