# Microsoft Presents: New flexibility/capabilities when updating/administering BC online environments

- **Source:** https://www.youtube.com/watch?v=fv19P2fIMkk
- **Video ID:** fv19P2fIMkk
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 48m23s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

All right. Hello everybody. Let's shift
gears and we go to administration.
My name is Roman. I'm the engineering
manager of the control plane team and we
are part of the business central
platform responsible for environment
management and administration and many
other things. And with me today I have
my colleague. Hi everyone. My name is
Vessa. I'm a software engineer in the
control plane team uh working together
with Roman. It's my first time here at
BC Tech Days and I'm very excited to be
here. Yes.
Um so in in this session, we're going to
build on top of what I showed last year.
Um if you have attended the session last
year, I hope it gave you some ideas and
inspiration how you can automate your
admin flows. if you haven't attended it
or if you want to look again in a bit
more detail of how to do the setup that
we're going to show um you can actually
check that recording out. It's on
YouTube. Um but we'll start with a
little recap.
Um and for this I'll just start right
away in the admin center. And um now
when you when you open it you see the
list of environments.
And if we want to do automation, um the
first thing that you need to do, it's
very important. You create an app like
an entra app in your partner tenant and
you give it permission to access the
business central admin API
and then you register it in the admin
center on your customer tenants.
And finally uh need to grant consent and
then that app can call the admin
endpoint. You can see here this is my
app my application client ID. I'm going
to use that one later.
The second thing I want to point out and
Tobin also mentioned it. It's the
telemetry side of things. So it's really
useful to get insights into what's
happening in your environment. like you
can do troubleshooting um you can query
like some of the examples to open showed
but it's also super useful for example
um to get information about environment
life cycle events.
So you need to create an application
insights instance in your subscription
and then take your instrumentation key
and register that on the environment of
your customer tenant. So basically if
you register your app insights on all
your customer environments you can get
all the environment life cycle events
for these environments and for example
react to events or do the
troubleshooting and analysis. So we have
done that here. I set the key and
because we uh want to do automation
um
I have put that uh together
in a logic app. I really like logic
apps. I think they're super flexible and
easy to build and you can do a lot of
things.
So the idea here
is that we have some periodic trigger
can be like a daily trigger or hourly
and we need some some variables here to
to manage the responses.
Um but then the first thing is we will
query our application insights and look
for
uh for updates if there's any update
available in any of the environments
that that we we are monitoring.
Um what is important here is the event
ID. You can you can see here um we have
extensive documentation of all the
different events uh their properties uh
when they get emitted what they're for
and so now in this case I query our
application insights instance for this
particular event ID which means there's
an update available
and then what I want to do if there's
any update available I want to um
make a copy
of my production environment. And the
idea here is so I copy that production
environment
into a sandbox and then I
update the sandbox to the new version
and see you know if the new version is
good, everything works fine and then
afterwards I can update my production
environment as well.
So to do that I have two steps um in
parallel. So one we set our production
update into the future. Um that's a call
to our admin API um for the environment
and then I can say run on I put the date
now
and here uh we have a a property it's
called ignore upgrade window.
Um so what you need to know is this
update window is set on every
environment. We have a default based on
in which country the environment is on
and we will run the updates inside that
update window. And the idea is here that
it should run outside of the business
hours. Right?
Then we trigger our copy. So we make a
copy of our production environment into
a sandbox. So we call the pro production
environment
um
and make a sandbox.
And now for long running operations
like a copy so that can run for a couple
of minutes
um we check if the operation is accepted
and then do a little loop here. So uh
check every minute check the status of
the operation. So every longunning
operation that you trigger from the um
API you will get like an operation ID
and then later on you can check on the
status of the operation ID to see when
it's done.
Yeah. So once the copy is done, so we
check on the status of the operation
and then we query for the information on
the copied environment like the sandbox,
right? So we go to our production copy,
check if there's an update available.
If we find that
then I'll schedule that sandbox to
update immediately. And now the
difference here is I put the run on date
as immediately now and say ignore the
update window.
So one of the things maybe we also
notice sometimes is that um uh if it's a
longunning update for example um and
it's running inside the update window we
cancel it before it reaches the end of
the update window so that we avoid
having the environment unavailable then
during business hours. If you say ignore
here, we will ignore that um as well.
And it will just run as long um until
it's done.
And then I I like teams. So um I have
set this up here to just send me a
message in um in in the chat um saying,
"Yeah, your
sandbox environment has been scheduled
uh for for update." And uh yeah uh the
idea here is that this is running in the
background automatically making the copy
uh scheduling my
um my environment uh update and then
just when it's done it it tells me hey
this is done.
Yeah. So I think this is a very
convenient way of automating such a
scenario using a logic app. uh but the
flow that we see here it is running only
for one customer tenant and we are
passing the entra tenant ID for that
customer with every HTTP request. Uh
what if we wanted to have the flow run
for all the customer tenants where the
app is registered? Yes, excellent
question. Right. So for this actually uh
we have a new endpoint. We call it the
discovery endpoint. And this will give
you the list of all the
uh tenants that your app um is allowed
to administer. So the ones that are
manageable by your your app, meaning
they were granted um access and they're
registered
in the admin center like you have seen
uh before.
We have the documentation for that in
the um behind that link on the Microsoft
learn page. And essentially this is is a
new endpoint here. Um u there's also a
new version. So it comes with uh version
2.24. Um it's the authorized AD apps
manageable tenants endpoint. And
um you pass the token of your um
um app from one of the customer tenants
um to authorize
and uh then it will return you the list
of all the tenants. So we can have a
look. I have a little script here
um how to do that.
So, first I have connected here my Azure
account. I I ran this already. Then I'm
using the MSEL.ps
module. That's actually a really nice
encapsulation of the Microsoft
authentication libraries. Really easy to
use then from from PowerShell.
Um I have my client application ID. So
that's the one that I have registered
and authorized in my tenant. And then I
um want to get a token for the admin API
for the API. So if I run this,
yeah, looks good.
Now
I have put
the secret that I need to get the token
on behalf of the app. I put that into a
key vault. So keep your secrets secret.
Um,
and I use the a key volt module to read
the um secret from the key volt here.
And let's try that.
Yeah,
looks good. And then let's get a token.
So
that's the service to service scenario.
We use a confidential client application
builder. Um, request
that token
also looks good. Then I'll put it into
the header here.
And I'll make a request to get the list
of environments.
So, and now I should see the same list
of environments that we also get in the
admin center.
Yeah.
Uh one thing also to note all the
actions operations information you see
in the admin center is backed by this
admin API
and you can
use the API also all the operations you
can query you can run operations um all
of that is possible to automate um and
like now we see the different properties
and um yeah we can we can work with that
so we can build now automation ition on
on top of this.
So if I go back to my logic app
and so I have just put it here into a
separate branch uh just for demo
purposes to see how it looks like.
Um
yeah so here I again I read the secret
from key volt using a managed identity
that is assigned to the logic app and we
call the new endpoint.
So that's the new endpoint manageable
tenants
and then I think it's also very easy and
nice we can parse the response. Um so
here we want to extract
um the list of entra tenant ids
and then do a loop over that.
So for each of the entertain ids that we
get I'll get the list of environments
we parse that um so we extract the
properties like we have seen um and now
in this case I want to get all the
sandboxes
so do a check if the type of the
environment is a sandbox
and then we
um query here uh for available updates.
So if I want to run this from
from my script from PowerShell
um we can do that.
So yeah we get the response. So in this
case I have registered my app in two
different tenants. So my partner app now
is is registered in those two customer
tenants and I can um more easily
basically like we've seen in the
automation
process all the different entra tenants
go through the environments and then do
whatever operations I I want to do. So
for example, yesterday I got a question
um if it's possible to
um update an app in an environment or a
list of apps in a at a particular point
in time. So this would be possible and
let's say you have an app maybe a list
of apps some dependent apps you could
make an automation that
u goes through all the entra tenants
that you have and then you have the list
of apps you want to update
and you can call that programmatically
and and update the apps for example at a
certain point in time um if you set your
trigger here for example uh at a
particular um
uh particular point in time Yeah. Yeah.
So you don't really need to maintain a
manual list of tenants or worrying
whether it's up to date. Uh so the with
the discovery endpoint you will always
have real time and accurate data which
will make your automations more scalable
and reliable. Yes. Exactly right. So
normally you would now have a list of
your entire
and then you need to process that
somehow. But in this way now it's it's
more built in and you can build the
automation based on that. Yeah. So we
talked about updates. Um
and that brings me to
the second uh big part here of of this
uh talk. Um it's the new flexible update
management
and what what is behind that? So the
idea is we want to give you our partners
and customers more flexibility when it
comes to updating environments
and concretely that means longer update
period. So we extending the update
period to five months and also we give
the possibility to skip minor updates.
And why do we do that? And what's the
idea behind? Um,
we know like we get the feedback some
customers run like a 247 business or for
whatever reasons um cannot or don't want
to update as frequently. Um, so with
this we want to address these these
needs of of customers that are somewhat
more update averse. And the second is
also we know that sometimes it gets very
busy uh for our partners for you um
around the major update cycle and
there's a lot of environments that need
to go through the update. Um so we want
to give you a bit more um time to go
through all the um the updates and
basically spread out um that that
workload. That's the idea. And so if we
look at the
update cycle, so the major update cycle
um we will still have a preview period.
So 30 days before the release of the new
major version uh you can create a new
sandbox on the on the preview version
and try out the new
uh release.
then we will get into the update period
and now this one is five months but we
want to have a fixed end date right so
we we often get requests for exceptions
or extensions um but with this we want
to give more time so with five months we
really uh believe that that should be
enough time to update and then that date
should should really be fixed Um
but if for for whatever reason um an
environment hasn't been updated yet um
at the end of the update period um then
we get into the grace period and here we
will try to do weekly updates on the
environment um and you cannot postpone
the update further. But for example, if
you fix the problem that prevented the
update, uh then you can say schedule now
or update now and it will go through.
But then for those environments that
still haven't updated, um
at the end of the grace period, then we
get into the enforced update period. And
here we will uninstall incompatible
apps.
So that um could be a per tenant
extension or or or some app that is not
compatible blocking the update and we
will uninstall that one. Um the data is
still going to be there. So if the app
is fixed, you can reinstall it. We
continue as it um was before it will
work. Um but we need to do that to move
with the updates forward.
So for minor updates uh we will still do
the monthly cycle like ship ship um on a
on a monthly basis every month and the
default scheduling is not changing.
So if you follow the the the default
schedule your environments will still
update every month. Uh but you can opt
out of that automatic scheduling and you
do that by selecting a target version
for the update. We're going to show you
how that looks like, how you do that.
And then finally also you can create
environments on any supported version.
That's also new.
So if we put that on a timeline,
um so now uh all environments should
have been updated to version 25 by now.
And we're in the middle of the update
period of the 26 release.
So there's two important dates now to
remember. Uh there's September 1st and
March 1st because these are the the days
when the update period ends and the
grace period starts. So September 1st,
March 1st
and then for the fall release version 27
that will be released um in October, we
will have a preview period again 30 days
before the release and then we will
start the updates.
Yeah. So with this you will have five
months to go to the next major release.
How this will look like we'll go through
some examples in a moment. Um and this
is available as of version 25.5.
So if you have environments still on
lower versions, you need to go through
the miners until 25.5.
And from there on you will have the
extended
um update periods.
This also comes with some API changes.
Um there's a new endpoint um a new
version. I'll show you one of them in a
in a moment. And also I referred to the
documentation on Microsoft learn. We
have documented the the API, the calls,
the responses and um
yeah also on the UI we have released the
changes just just a few weeks ago and so
let's let's have a look visa. Yeah,
let's do that. I'm just going to switch
here.
Right. Uh so this is the environments
page in TAC and as you can see I have a
few environments and they are all on
different versions.
The first thing I want to point out is
that we have streamlined the information
that we show here. So in the current
version you will see the version being
displayed as major dominor
and then in the column here you will be
able to see which version the update is
targeting and when is the update
scheduled for. So I'm going to select
the sandbox here which is currently on
version 25.2 too. And as Roman just
mentioned, uh this version uh we don't
have the flexible update management
changes uh so we are only able to go
from 25.2 to the very next version which
is 25.3
and I already have an update scheduled
for version 25.3.
We can also see here the start of the
grace period or the date the September
1st 2025.
And if I click on modify
and click on the target versions,
there's only one version that's
available. So that's the one that we are
already targeting. That's the one that's
scheduled.
And I can still change the update date.
So I can select from the dates available
and schedule the update to run.
If I switch back to the environments
page and then we look at the production
environment.
So my production environment is on
version 25.5
which means I can make use of the
flexible update management changes. And
you can see here that the latest
available version is the 26.1
version and I also have an update
schedule to version 26.1. So I am
skipping version 26.0 and going straight
to version 26.1.
If I click on modify and expand the list
of target versions, then there's a lot
more versions that I can pick from. And
I can pick any of the versions up to the
4 minor of the next major which for this
environment that is version 26.4.
So here uh for the versions that are
already available uh they will show up
as available and the one that you have
already selected or the one that you are
targeting that one will show up as
scheduled.
All the other versions that are the
unavailable versions will show up as
planned and then you can also see the
month and the year for when they are
plan to be released.
If I pick any of these so one of the
planned versions uh then I am not able
to pick an update date as of now as we
have this uh box here that also displays
this information. So once the update is
made available, we will automatically
schedule the update for the environment
within uh two weeks and you will also
receive a notification for that. So once
the update is available, then you can go
to TAC or through the API you can change
the date for the environment.
So for this environment uh the grace
period is also starting on September 1st
2025 because it's also on major on
version uh major version 25
and my last environment here is the
sandbox environment. So this uh
environment is already on the very
latest available version that is version
26.1
and for this one I have picked uh
version 27.0
as the target version. So I cannot pick
a date for it yet. But if I expand the
list of target versions then I can see
all the versions up to version 27.4 for
that I can pick for this environment.
And of course uh with the environment
being on version 26, we also have the
grace period starting on March 1st,
2026.
So as we mentioned, these changes are
available for environments on version
25.5 and higher, but they're also
backwards compatible and they are
optional. So if you don't want to change
the schedule the update schedule for
your environments then we will just
continue scheduling the updates
automatically with every minor and major
release. So your environments will
continue to be updated to the latest
version as always. Do you want to add
something to this part? Yeah. So um um
maybe to to recap uh the
the difference is now that there's not
just one update available for an
environment but um there are many
basically um they can be scheduled they
can be planned they can be available um
so that that's a change that's also a
change in the API
um so let's let's show you that um
so if I go back to my my script Um
I requested the list of environments. Um
got the list of tenants and now I can do
a query against that new update
endpoint. So this is the new one here
from version 26 2.26.
Um and this is like you query for the
application family. So, business central
and then um we actually want to do a
loop over
um all the environments that that we got
in the previous call and then for each
environment I want to get the list of
updates
and then write that out write that out
in a in a nice format if there's any uh
update available for for each of of the
environments.
So yeah, you can see the response is
different um for the environment that's
on 26.1. Now we see a whole list in the
same way as we saw in the UI and we can
see that Vista has selected the 27.0. So
this sandbox
will update will be scheduled to update
once the 27.0 is available.
Um for the other one the 25.5
um we have
um selected the 26.1 but you can see
that 26.0 and 26.1 are both available.
So the way essentially to opt out of the
automatic scheduling is that you pick a
version in the future.
Uh you can see a bit more information
here on the on the dates on the time
frame when these are available and when
they can be scheduled. Um yeah and the
last example here is that our um sandbox
that's behind on the
uh older 25.2 two. Um, it needs to go
through the miners until 25.5.
Right. Um,
yeah. But um, we have some more things.
Yes. To show, right? There is, uh, one
more thing that I want to show you in
SAG. Uh, because a couple of months ago,
we released some updates to the, uh,
apps page in Tenant Admin Center. So now
for just need to refresh my session.
I'll go back to the sandbox.
Right. So now in the apps page uh you
can see all installed apps. So you can
see the global apps. Uh I'm able to pick
the dev extensions and you'll be able to
see those as well as the per tenant
extensions.
Uh we have also made available the
uninstall action directly from TAC. So
you can now uninstall dev extensions,
PTEES and global apps and you can just
do that by clicking on uninstall and you
get some information about the app that
you want to uninstall.
uh if there are any dependent apps for
the app that you want to uninstall then
you will get uh these uninstall
requirements because it's important that
the dependent apps are uninstalled
together with the root app in order to
avoid any breaking changes.
So you have all of that information here
and then same as uh you have the option
in the extension management page you can
also delete the application data you can
choose to delete the application data
together with the uninstall request. So
once you click on uninstall uh you will
just have a confirmation dialogue
together with the two acknowledgement
statements and once you select those you
can just click yes and you would proceed
with uninstalling the app.
So for the PTE uh right now the
uninstall action is the only action that
we have available in TAC. So the install
and the update functionality is still
only the in the extension management
page from inside the product but we are
working on uh designing a way so that we
can bring the uninstall and the update
uh for PTS to talk as well.
Uh that is all I wanted to show you
today. Is there anything uh I might have
missed? Yeah, we have um some bonus
content um
as well. So yeah, because you guys are
here, we want to show you some uh
insights uh behind the scenes um things
that we are working on. So I cannot
actually show you the features yet, but
I want to tell you that this is stuff
that we want to do that we have in our
plans. Um first is a connector for um
for the admin API like a power automate
connector. So that will make the
building of logic apps much easier. So
then you don't have to use HTTP requests
build them yourself. Um but the actions
will be native inside the connector and
it will also allow you to use for
example uh Copilot Studio.
Um, also we know um sometimes
app uh app apps don't compile on a new
version and so we run these app
validation runs against the next um
release versions of PC but we don't
surface that yet in the admin center.
So, we are also planning on on bringing
that in so that when you're in the admin
center and you want to schedule an
update, you can see right away if
there's any extensions that are not
compatible.
And uh finally, um the uh preview
period, right, the 30 days before the
new major release. Currently, you can
only create a new sandbox on that new
preview version, but we want
to enable the
possibility that you can take your own
sandbox and update that to the preview
version and try out with that. Um, and
together with that, we're also looking
at longer preview periods to have more
um more versions actually available to
um to preview.
Yeah.
So, that will bring us uh to the end of
the session. Um, so there's a couple of
takeaways I want to leave you with here.
So, the new flexibility, use it when you
need it. Um, ideally we would like to
have all environments on the latest
version all the time, but we recognize
that for different reasons it's not
always possible. Um, so we want to give
you that flexibility. Um,
but yeah, use it when needed. Um,
otherwise the default schedule um will
make sure that we'll keep your
environments up to date. Use the new
discovery endpoint.
Um, we hope it's useful and uh give us
feedback. Um, so we're really happy to
hear feedback both positive and
uh new requests or or or things that
don't work for you. So give us feedback
and um the the best way to do that is is
Yammer. Um so check out
aka.msbc
yammer. Um but we will also stick around
after the session and we'll be at the
booth if you have any other questions or
just reach out to us um
directly.
Yeah, with that actually we can do a
little Q&A and I see some hands up.
Awesome. Um here yes.
So why don't one question if I um
install the entra app in the beginning
on the tenant of the client. Yeah. So I
have to do it in the
client Azure for each client I have to
install this or can I have it if I have
an admin relationship only make it
globally for all my clients? Yes. So
it's a security uh requirement and also
by design that you actually in fact need
to go and register it for each and every
um tenant and your customer. So an admin
in the customer tenant need need to
grant the consent so that you can access
their their data and their APIs so that
you can act on behalf of their every 180
days I have to
update the secret no no no you don't
need to um uh no you don't need to
rotate or change any secret um yeah so
the
um the the best way to to use the um for
example the logic app is to have a
managed identity um and give that
permission to authenticate as your app
and then you don't need to work with a
secret the secret I used it here only
for for that script that local script
yeah do you want a t-shirt I have
already you have one all right here
if you go from 25.5 to 26.4 for instance
be significantly longer than if you go
from 25.5 to 26.0 or is it would it be
roughly the same? Oh, this is a
difficult question. So if the update
time would be different.
Yes. So the update has to be made
available for you to be able to schedule
it and we released the five minor that
collides with the start of the grace
period depending on which version you
are. So I don't think there's like a big
change if you want to go from 25.5 to
26.5
uh because the version needs to be
available already. Yeah. But did you
mean the execution time? Yeah. How long
will the will the environment be
unavailable for? Would that change? I
think this is really hard to to answer.
I will need to experiment. Then the the
changes are cumulative. So let's say you
update to 25.3.
So that version will include all the
changes from 25.2,
25.0, any like previous version, the in
between versions, they will be included.
So potentially it's longer, but
probably not significantly. Yeah.
Do you want a t-shirt? Yes. Okay.
Yeah.
Oh, there's a question in the back. Oh,
all the way in the back also. Oh, are
you just stretching?
You have a question. Okay, but I'll I'll
go here first.
Thank you. Uh it's more like a feature
request. Uh when copying environments,
will it be possible to um select a
security security group in advance
instead of waiting the full copy?
Okay.
[Music]
So if we like you copy the environment
and you want to have the security group
carry it over. Yes. Um for customer we
create different security group for the
production and development environments.
So it will be nice to to be able to
react in advance. Okay. Instead of
waiting because it take 10 minutes
sometimes. Yes. Yes. And you do that
through API? No. No. Okay. But you could
then if you do it programmatically you
could call it afterwards. So when it's
done and and set that okay group. with
API. Okay. That would be one way. Yeah.
Yeah. But okay, we'll take that. Yes.
Thank you.
All right.
Hi, I have a question. Um, in case an
update failed, um, is the process
different
um, or we still get an email with the
error stack and that's the only
um, or is this part of this process
improved in any case? Okay. So, you mean
the new flexible update management, how
that impacts if um, if an update fails.
So fundamentally there's no no change in
that. Will there any improvements or
better overview of of of this? Uh as far
as uh I know we only get an email from
from from the yeah from the system and
you get only the errors error st. But is
there a plan for more
uh information? Okay. Will help us to
fix this? Okay. error. Okay, I get it.
Um, yes. So, if you go in the admin
center, we didn't show that, but there's
an operations page and for each update
there's um
uh there's an entry there and and there
you will also see some more details on
on the update operation and the error
message. Um and then also telemetry the
application insights telemetry can give
you some more insights into what
happened in the environment. Yes. So
those two places
I I would look in addition to what you
get in the email. Yeah. So especially
the telemetry should should be more
helpful.
Just a tiny curiosity. Currently, for
example, if a mistake happens and a
company gets deleted from within an
environment, the only option that I've
got is to restore the environment. Are
we thinking of maybe getting something
in place? So instead of doing the whole
restoration to get back to restore just
the company within the environment.
Okay. So
if one company gets deleted, how how to
restore that? Yeah. So we currently only
have that on the entire environment
level. Um so you would need to restore
point in time restore the entire
environment.
Um and then Yeah.
Yes. Yes. Yeah. What we have seen
sometimes is that um
uh people do a restore and then take
that copy that restored environment and
only take the data that got lost um for
whatever reason and copy that back into
the production environment.
But that's maybe a bit more difficult
depending on what happened. Um yeah, but
that we have seen that as a as a way to
work around this. Um so because the
point in time restore creates a a second
environment like a copy and then you can
extract whatever you need from that. Um
yeah, good. Do we have another t-shirt
to give away?
Yes,
I can go. Okay.
Was there any other question?
I think we're otherwise out of time.
Well, yes.
Hi, thank you. um in the admin center
under um capacity we have that ratio
from one production environment to three
sandboxes. Yes. Is that something that's
going to be
can we change that somehow instead of
just having to buy an additional
production environment to get three more
sandboxes?
Often times we have a sandbox for some
we do for some troubleshooting then we
need to do problematically some update
test and then we can quickly run out of
sandboxes. Yeah. So you you
good question. Yes. Really good. Yeah.
So you can buy additional environments.
Um
they're not cheap, you know. Um
Yeah. And we we we do get these
questions and we we get that feedback.
But I mean currently I I can't tell
anything about that that we are changing
that. Um um but that's a question for
our licensing
uh folks. Yeah. Yeah. Yeah.
Yeah. But you can also get this partner
sandbox if you are um if you are a
partner. So those are cheaper, right? So
that could be a way if you need more
more sandboxes to use that part.
Yeah. Yes. The question is is it
possible sometimes to is it possible to
buy additional sandboxes not additional
environments with three sandboxes and
one productive system? This was the
question. Yeah, I'll pass that feedback
back. Um Yes. Yeah. Yeah. But yeah,
currently you would have to buy and I I
can't share any plans that any changes
are are done to that.
Yeah. All right, we're out of time, but
one more question and then that's the
last question.
Here you go.
Um is it possible if you have an uh
authorized app in the admin center uh of
a tenant that is no longer available to
login to remove that um app
registration.
So we we have for uh some experiments uh
added and a demo uh tenants the app
registration right now the demo tenant
is no longer available but we see
the uh app registration is still
available and we cannot delete it
because you need to have uh you need to
sign in as a user to remove it. Mhm. Do
you see that in the in the API in the
disc the manageable tenants? Yes. Okay.
Yeah,
I am not sure but it might be possible
to do it through the Azure portal. Uh
have you checked that? Yeah, the the
tenant is removed. So I don't think it's
uh existing anymore from your side. So
from the partner tenant if you can see
whether uh so on which customer tenants
it has been granted access to and
whether you can remove it from there.
Yeah, but we we don't have access access
to the tenant anymore.
Uh so if we get a list of the manageable
tenants, it's still present, but the
tenant does not exist anymore. Mhm.
Okay, we'll have a look at that. Yes.
Yeah. Mhm.
Is the question clear? Yes. H is the
question clear? Yes. Yes. Yes. Yes.
Yeah. Thank you. So we'll we'll we'll
have a look at that. Yes. Yeah. Mhm.
All right. Yes. So that's it. Um, thank
you very much. Enjoy the rest of the
conference.
[Applause]
