# BC TechDays 2023 - What's new in Power Platform development: Power Automate and workflows

- **Source:** https://www.youtube.com/watch?v=1tZhuX-uLx8
- **Video ID:** 1tZhuX-uLx8
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 43m30s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

pretty cool yep
nice okay so by now you're very familiar
with evgeny but I'm Elton and if you
remember me from the last tech days we
had a session about Power Platform power
automate and the improvements that we
had made there regarding uh bringing
instant flops to business Central so we
have continued to invest in this area
and today we're going to talk some more
about that so we're going to talk about
the improvements that we've made to
approval workflows we're going to talk
about some quality of life changes that
we've made in the power ultimate
connector on the power automate side and
within business Central client as well
we've introduced external business
events which are going to allow you to
notify your external systems about
things that happened in business Central
and finally we've introduced some new
power ultimate actions that let you
integrate with these events and uh use
some functionality within teams so I'm
going to hand it over to organifirst
who's going to talk about the new
approval workflows
yeah so the first question you always
get asked like a year ago one half year
ago can I approve Samsung on the phone
can I get my invoice approval uh
whatever can you do it on the phone and
Community said yeah maybe yes we don't
know and the truth is you could back in
the day you can do now and hopefully we
don't get this conversation going
forward so it's like yes you can and yes
you should
um
this is how world looks six months ago
so we give you capability to create
workflows and approvals but it's a
little bit like a messy or maybe not
that it was like a functional but not
desirable you had to create very
complicated flows you had to pass like
some content like man kick copy
environment and Company through all the
blocks it was functional but maybe not
that usable so to speak or enjoyable
so this release we hope we did a better
job to give you a number of templates
something you can discover click
configure and basically it just work out
of the box so next time I have a
discussion can I approve on a phone for
the you know your client's answer is yes
you can let me show you and just
basically get it done with no time
let's see it's an action
so with that we're going to move to
will change we can have a role the play
a bit so I want to show you how you can
configure a purchase order approvals so
I go to push sorters
like anyone really
then you need to find
actions
approve request approvals power automate
and then you have like a create power
automate approval flow it's a bit of
hidden
you'll do better job to promote it but
that's where it is
and you can do it for all obviously
document types not necessarily purchase
orders now when I run this UI it gives
me there's like a just pleasure to my
eyes place to start to select my
templates if you do work with Microsoft
teams for example create automation it's
exactly the same usability and I have
here multiple templates not one all
three is better than zero and we're
going to build your more and more as you
go I can say I want to have a template
if someone requests for approval project
purchase order I can be notified and
maybe I need one respond one upload
approver maybe multiple people have to
be part of the process and so on so
forth so I just create the first one
because it's the easiest to demo and the
easiest to show
that workflow process involves couple of
components business Central obviously
Microsoft team approval apps obviously
and some notification that things can
happen it's a template meaning we give
you initial structure you can go ahead
and modify it yourself or actually your
customers even without calling you you
need to define or select a bit
like which company you're talking about
where are you and then who needs to be
part of that approval process
you do yes you are the approver yeah it
makes sense I'm kind of a manager I'm
saying every time someone asks for
approval I want to be in charge I guess
like
doesn't work in a real life but we can
we can we can take it for example
so now we have an approval running and I
can continue to do my job and just maybe
forgot about that step and now we're
going back to Arthur yeah so it's very
fortunate that evgeny has created an
approval workflow because I have created
a purchase order that I need him to sign
off on so I'm just going to send him an
approval request
and I can see that the status of the
purchase order has changed to pending
approval and now on afghanist side
hopefully he's received an approval
request
yeah I got notified actually I can get
notified on my phone on a go I'll review
it say yes but for a
scientifical purposes where in the web I
get an approval I can get a lot of
custom information you can configure all
that who is involved why is happening
what is the business reason I can look
on attachment and documents and so on so
forth and at some point of time I can
say yes okay and I'll always use this
opportunity to remind you that we're in
the modern days and you press approval
button so basically I approved continue
with my day and now we go back to artem
yes so now that Afghani has approved my
purchase order I should receive an email
say under the purchase order was
approved there you go so if you've used
the workflow approvals before then maybe
you've received this email and it just
says you know your approval was approved
congrats right but we've made some
improvements here too so now that we're
able to support both single and
multi-approver flows flows where you
require everybody to approve who's
listed in the the approvers list we show
you a table of everybody who signed off
and the comments that they left and what
their response was so if you need to
follow up with someone who rejected your
request and you know exactly who they
are and you can go and facilitate a
conversation and we also provide you a
link to this record so if you were in
the middle of working on it and you
switched contacts now you can quickly
get back to this record without having
to look it up yourself we give you the
URL to the web client and if I click
this it's going to take me straight back
to this document it doesn't remove
capabilities to get your standard
apparel process in business Central yes
you go to UI find a button or proof
reject but if you use themes which many
of your customers use we know that and
we are you can give them just a better
tools to do the same job
now we can go back to presentation
yeah uh quickly summary we give you
different templates template means you
click it to configure it runs but you
can go ahead and customize and you have
a choice for different situations you
can always go ahead to more advanced
mode and do more stuff if you will if
you wish we don't recommend but you can
uh we took an opportunity to look on all
the approval templates we had and make
it better we also add like a purchase
code document so now out of the box you
can configure approvals for all this in
a couple of clicks so we hope you don't
have this conversation anymore can I
approve because answer is yes you can
absolutely and actually we also show you
how you can make it for a custom
entities just in a second not only what
Microsoft give you out of box
more power automate in business Central
I showed in the keynote
um briefly and let's do it again very
quickly because it will help us to
demonstrate point in the future
the same idea of a or maybe you should
say the same concept of giving you
templates to start build automations can
also apply for what we call internally
custom actions so every time I want to
build flow for that entity
I should be able to start not with the
emptiness
which is kind of lovely but not that
helpful but start with a number of
templates so something I can choose
yeah and go through from it
in this case you have one template one
is better than zero again we'll get you
more and the system plate it's very
simple template how you can basically
have a flow which will
allow you to block your customer
yeah externally yeah you need to Define
who can be responsible for that I'll
just say
again very easy to create automations in
a product without leaving a product our
platform has thousand connectors one
more time one zero zero zero so you can
really build impressive stuff Beyond
like this primitive demos we are showing
you right now however the question
arrives is always where would those
flows be safe and start
it's like a question number one yes you
create a flow but how do we manage it
where it stored what does it mean and so
on so forth
in this release we give you an ability
to select configure and Define where
your flows will be stored we're also
giving you a powerful Dev tools to build
your power pattern solution with il code
we'll show you the tomorrow we'll show
you briefly in the keynote but for now
just you can always Define and configure
where your flows will be stored and
those will have like a short demo about
it
so now we're going to demonstrate more
more power ultimate in business Central
so if I switch to my laptop then as
Afghani says you can now configure which
Power Platform environment your business
Central environment connects to and if I
look back to the last tech days I
remember that the probably most popular
even only question that I was asked was
how do I actually use this in my setup
where I have multiple Power Platform
environments maybe for different
departments in the company or just
because we don't want to use the default
one so if you see on the screen right
now I'm not in the contoso default
environment I'm in my own custom
environment that I set up for this demo
and I have an instant flow that is
called I'm in the BC Tech days 2023
environment so if I switch back to
business Central and I open up the
automate menu then I can see this flow
even though it belongs to a non-default
environment right so maybe you're
wondering how did I configure this so if
we go to the assisted setup
list
and find the power automate environment
wizard
then I mean I've already set this up
because you can see these flaws in my
environment but if I Just Step through
all of the instructions then I can see a
list of all of the Power Platform
environments that are available to me
and now I have the option to choose
which environment I am connected to but
I can also choose on behalf of the
organization because I'm a system
administrator so if you have a single
environment needs to be the default for
everyone you can apply that first and
then you can choose on individual user
bases if you need some special setup for
particular users
um so you know like I hope that this
satisfies uh everybody with that kind of
setup and that this is a big quality of
life Improvement for you we've also made
some improvements on the power ultimate
connector itself so if you've set up an
approval workflow before then you may
remember this screen because usually
when you click the template it takes you
to the flowchart instead and what would
happen is that you would open this up
and in every single trigger and action
you would need to enter the environment
and company that this should run against
and if you pick the wrong one then your
flow doesn't work right so so now what
we've done is we've taken the
environment and company that is
configured in the trigger and we output
that at every stage from every action
and trigger in the connector you can now
see which environment and Company
they're supposed to be from and
configure it to use the same one right
there's only one caveat to this which is
uh in order to see the intellisense you
do need to actually pick an environment
first as of now as of now we're working
into a way to work around this but at
the moment if I want to see the inteller
sensor and I need to pick the
um environment and Company and then when
I look in here I can see all the API
endpoints that are available to me
because we need to know what extensions
you've got installed in order to
surfaces information right but once
you've built your flow you can then go
back and replace these values with the
environment and Company Dynamic values
and then your flows become portable
between environments so if you are a
partner who is trying to deliver power
ultimate solutions to your customers and
you'll find that you're having to
configure these values and all the flows
or you just can't shape business Central
flows because you need to go to the
customer's environment and change these
values now you can build them in a
generic portable way
um in order to build this and I think
that is that
yeah great so the next thing that I want
to talk about is new custom action types
that we've introduced so looking back to
the
um request approval example that we did
before yeah I'm going to change back to
my um just quickly
yeah so going back to the example before
Afghani you said uh this action could be
more prominent in the page and it can be
because this is a custom action and it
can be personalized with the designer
and moved somewhere else right so if I
wanted to take this action and drag and
drop it into this group then I should be
able to do that
um so the type of this action is a um
template Gallery action so what we'll do
is open up the template UI
and show
the templates in a particular category
right so I mean you can see the template
your eyes opened up so I'll just switch
back to my slides
um yeah so there's two different types
of action and one action is this flow
template which opens up a specific
template directly to the editor so if
you have a template that you know you
want to invoke you can just go straight
there otherwise if you have a group of
templates for example you want people to
work with approvals or notifications
things like that then you can specify a
category instead and allow users to
choose for themselves
um so how do you write these custom
actions so if I switch over to vs code
then all I need to do is add a custom
action the way that you regularly would
I need to define the custom action type
and I have these of the flow which is
run an instant flow or flow template
which is uh open up a template in the
template UI so now I have two options
for how to configure this so I can pass
the flow caption which is the caption
that will be used by default when you
open up the template editor so I can
just say like my new flow right and then
the next option that I need to configure
is the template that should open so I
say float simpler ID and I can get this
template ID
from
power automate so for example if I
wanted to surface this create an item in
SharePoint when a record is created in
business Central template then I can go
to this floor template ID and just enter
the Google there and now when I publish
this and I click this action then this
is going to open up the template UI
directly to this template and what if I
want to use the template Gallery instead
well I can just change it to flow
template gallery and now the flow
template ID is obviously invalid because
I'm not showing a specific template I'm
showing a category of templates so
instead I need to choose a category name
and there's all the basic ones like
approval notification things like that
and they're available just in power
ultimate by default or we also provided
some custom categories which you can
find on our own actions in base app so
for example we have like d365 BC
approval item and that shows you all the
item approval templates or purchase
order or general journal Etc or d365 BC
instant will show you the instant flows
that appear in the automate menu this is
the same one that we use so I know that
the next question question that I will
get is
how do I create my own power automate
templates and unfortunately if you want
your templates to appear in this
template Gallery they need to be in the
Public Power automate Gallery which
means that you need to coordinate this
with the power automate team right so
unfortunately we're a little bit Limited
at the moment it's only if you have your
own external integration that you plan
to ship templates for then you'll be
able to surface those in business
Central but you need to coordinate that
with them and they have documentation
for this which is available in the
slides as of now as of now we're
investigating options for you to bring
your own templates outside of the public
Gallery but this is still work in
progress we don't have an ETA on this so
just bear with us while we figure this
out
so that was it for power automate for
now and now we're going to switch topics
a little bit to external business events
so what is an external business event
well you can notify external systems
when an event happens in business
Central so for example our power
ultimate connector is an external
service which we want to notify when an
item is created approval is requested
things like that right that's the kind
of systems that you can notify you can
discover And subscribe to these events
via our outdated apis you can get
notified via HTC post to a URL that you
provide to us and we provide some events
that you can subscribe to out of the
boxes examples but also just for
functionality right
uh and you can create your own events as
well in your Al extensions using the
external business event attribute
so these are the custom events that are
available out of the box I'm not going
to go through all of them but it's a lot
related to purchases sales uh quotes and
you know sales opportunities so we
expect to deliver more of these we're
going to roll them out as time goes on
but this feature is in preview so we're
still thinking of ways that we need to
expose parts of essential behavior for
you to hook into
how do these differ from regular a
elephants so I mean most of you are
probably familiar with traditional aele
events like integration events business
events and they are subscribed to using
an Al procedure with this event
subscriber attribute and they're
handling Al so you define the behavior
of the event in Al you call the event in
Al everything happens in the AL runtime
um we've got external business events uh
discovered and subscribed to Via old
data instead you're not using event
subscriber you implement the behavior in
your own service and your notified via
web hooks right so you handle these on
your side
so the way that this works is you define
sorry this is extremely small but you
define the event in Al and then the
external service can discover that the
event is there business Central response
with the list of events that are
available and then you can add a
subscription to this event and Business
Center will confirm that the
subscription is created so now your
users start using the products and
events occur in Al and at some point
after these events happen we're going to
notify you via a post request that these
events have occurred so this is the the
overall process we're going to step
through now so the way that you define
an external business event is very
similar to traditional business events
uh so they're defined an Al using this
external business event attribute you
raise it by calling the procedure just
as a regular event and subscribers
receive the parameters of the procedure
as a payload in the post body that you
receive so for example here's my
business event the name of this that I
need to refer to it as is my business
event you provide a display name that
will be used in for example power
ultimate or your own Services when you
you surface these and a description of
how this works so it's not only for you
but also for users if you would like to
use it for that and then you need to
provide a category for filtering as well
so on the power automate side we uh you
know if we showed you every single event
that was available the list would go on
for Miles so you need to provide
filtering categories so that users can
easily find your events either through
the API or through UI light power
automate and then finally you just
Define your procedure so I say my
business event and now I need to specify
uh data that I want to send to the
external subscriber so we don't allow
you to pass a whole record the entire
mention of this is not for you to pass
the entire sales invoice right you just
need to pass enough information that the
subscribers can request more and perform
simple operations with that so I mean
here I just have some sample parameters
with primitive data types and then there
is no event body because this is handled
externally right
so this is example from base app that is
present today we have the sales order
released event that admits a sales order
ID the one that was posted uh and the
URL of that in the API so that you can
make a request for more data and how do
you raise this well we already have the
internal event subscriber for when the
sales order is released so you can just
call the external business event so now
every time a sales order is released
then uh webhooks notifications will be
sent out to all the subscribers of this
event as well
how do you protect this data right so if
you look at the previous slide you can
see that this is only exposing the sales
order ID and URL but you might want to
expose things like the customer that is
involved in this or the total sales
value things like that so how do you
make sure that internal subscribers
can't see data that they don't have
permissions to read so so external
business events can expose this data and
you should Define permissions that are
required to create the subscription
right these are permissions that apply
to the subscriber when they create the
subscription not to the user who
triggered the event so for example if
Afghani doesn't have permission to read
certain tables and and he triggers an
event
it doesn't matter that he doesn't have
the permission the important part is
that I have the permission to read this
data right as the subscriber so
um if you need to Define permissions
then all you need to do is add another
attribute required permissions and then
you just say you know what object type
and uh additional parameters you need to
provide here I'm saying the subscriber
needs to be able to read the sales
header table and you can Define as many
required permissions as you like just
line after line after line and you know
the subscriber must have all of these
permissions in order to subscribe to
this event
so now how do you discover events we've
created our events we published our
extension how do I actually find these
and start creating these subscriptions
and get notified so the events are
exposed via odata API every odata API
has the extension endpoint external
business event definitions and if you
make a get request to this then we'll
just give you back all of the events
right but it's a no data API so you can
apply filters so that you can narrow
this down to the events that you're
looking for so for example here is one
event that was returned this is uh again
the sales order released event and we
give you the name in the description but
we also tell you what kind of data you
can expect to receive when you receive a
notification of this event so this comes
in a serialized Json format that I
deserialized it for you and you can see
here that it tells you the order that
these parameters will appear in and also
the data types that you can expect to
receive and even though this is an old
data API the notifications come via
webhook so these are nav data types
which means that you need to be able to
handle those on your own external system
you to build interpret these and figure
out what type you should expect to
receive in whatever language your
service is implemented in
um so how do I subscribe to events well
very similar these subscriptions are
also managed by our auditor API all the
auditor apis have the endpoint external
event subscriptions you can subscribe
via post to any of the apis and this is
what that request looks like right so my
subscription type is webhook I think
this is optional but then I need to say
which Al extension via app ID and event
name do I want to subscribe to right so
here this is the sales order release
from base app which company do I want to
subscribe to this and this is optional
you don't need to Define it you can
alternatively give the company name but
you can subscribe to events on an
environment-wide basis so you don't need
to filter company if you don't want to
this is just for your own purposes then
you need to provide the URL of your
service that we should send the post
notification to so here I've just said I
have a single endpoint that I would like
you to notify me and is this
um and then you can additionally provide
some more information so here we have
this client state right right so this is
any data that you want to be returned to
you when this notification is fired to
for example indicate what type of
subscription or what the purpose of this
subscription is what action it should
invoke on your service so in our power
ultimate connector we do exactly the
same so subscribe to this and in the
client State we placed the uh like ID of
the flow that should run when this event
is fired right
um so to get notified business Central
is going to send a post to the
notification URL that you provided and
you will receive a list of events that
occur since the last time you were
notified so events can be bundled up uh
like if there's a long transaction that
has many operations to trigger many
events then you'll receive a list of
events
um
and the payload for each event includes
the client state from the subscription
that it came from so they're bundled by
notification URL not by subscription not
by event so I might receive many events
from many different subscriptions all in
the same uh notification so if you
provided the same endpoint all the time
then your main routine endpoint needs to
uh be able to handle these different
events or you can provide a different
notification endpoint for every
subscriber is up to you so this is what
this looks like and you know I'm going
to get the uh the identifier of the
event that was fired the time that it
occurred the aad user ID of the user who
triggered it so then you can do a lookup
in graph to find out more information
about them and correlate that with the
business Central user uh the company
name we always provide this even if you
didn't specify a filter we will always
give you the company that this occurred
in and then the information that came
from the business event the sales order
ID and URL in this case and the client
state that you received so now I'm just
going to do a quick demo of how this
works
um yeah exactly right
so I need to first in my extension add
some business events so the scenario
here is that because also Electronics
has decided to go into the production of
widgets and I need a approval process
for this because this is a custom data
type we don't provide any templates out
of the box
um so I need to provide some business
events that enable to me response to
this action this send approval request
so I'm going to go into my extension and
create a new business event
so all I need to do here is exactly as
we saw in the slides
um create a new business event and we'll
just call it a widget approval requested
and now the event name is the same uh
which approval
requested and in the interest of time
I'm just going to put a
name description right and the
categories so in order to define a
category you need to extend the event
category enum with your own category
there you can add as many as you like
and now I can Surface my event in this
particular category so this is widgets
and finally I need to Define some
parameters so I would like the
subscriber to receive not only the idea
of the record but I would also like them
to receive for example the name the
display name of the widget so we'll say
I have a name and I also have a
description
um which is
some more text
so now in this event that I have created
I am exposing some data about this
widget right I'm giving the name in the
description so I want to make sure that
anyone who subscribes to this can't read
this data unless they have the
permission so all I need to do now is
add a required permission to the widgets
table
and the permission level is read right
right and now anyone who subscribes will
be rejected unless they have this
permission
um so finally I need to actually trigger
this so I have the send approval request
action and all I need to do
here is
um
just call my function which approval
requested and it's with the system ID
yeah give it the system ID and also give
it the name and the description
so I'm not going to publish this now
because I actually published this to my
production environment using algo for
GitHub so we're just going to skip
straight to uh using the web Hooks and
subscriber and using the business event
sorry so if I go to the API V2 external
business event definitions and send this
request then I will get back a list of
other credentials and not
let me just sign in
nice so
if I send a request to this API then
I'll receive a list of every business
event that is in the product right so
you can see even though
um like I've just added this single
event I'm actually getting all the
events like customer blocked uh customer
unblocked sales invoice released Etc so
now if I go to my own API this is the
API that I've provided to work with
these widgets and I send the same
request then I'm going to receive
exactly the same response I can still
see like customer blocked
um customer unblocked so we've just
mirrored the API between all the
endpoints so that you don't need to
manage several endpoints but if you want
to limit this to events that are
relevant to you then you can use the old
data filters right so for example here I
applied the filter contains the name
widget so if I send this now I'm only
going to see
events that have the name widget for
example this widget approval requested
that we just added and now I can
subscribe to this so I need to subscribe
to the event I've already populated my
my app ID and the event I'd like to
subscribe to is a widget approval
requested
um the notification URL is acting as my
service I'm going to use this
application webhook.site where I can
easily test the web hook notifications
so I want to notify this URL and when I
send an approval I should see the output
appear here
so I'm going to press this URL
and the clients today I'm just going to
say hi from PC tech days you can put
anything that you like here up to 2048
characters so if I send this then I get
the response back 201 created so now my
subscription is there and if we look
here I haven't received any events yet
so what I'm going to do is send an
approval request with this widget Now
using my action
and what I should find in a second is
that my
subscriber was notified you can see the
client State there hyphen BC Tech days
here is the widget ID and now I can do
more operations in the API to request
more information about this and take
some action on it so uh going back to
this just a reminder that this is in
preview uh external business events are
still being developed by us and many
other aspects of this are subject to
change so please try them out and give
us your feedback but our expected GA for
this is a 2024 wave one so there's still
a lot of work to be done a lot of
improvements to be made you join the
discussions on Yammer about this if you
would like to join the conversation and
you can learn more about how to use
business events even though they're in
preview at our documentation
um and finally we're going to talk about
some of the new actions and triggers
that we've introduced to power ultimate
and up to again
yeah so I can show you that we build
technology you can integrate that
through any kind of custom development
code through all data very standard in a
secure way you can expose your payloads
all good if you don't want to pay
attention to all this complexity maybe
you don't want to you can use power
automate to basically say in a very
simple way as I show you hey if business
event rise please act which is obviously
more I guess like enjoyable story for
like a Norco developer like me so it's
really easy to go ahead and build those
flows you can probably
skip this even demo for now it's super
super important that you can Define the
payload so you can say if my order is
delayed you can send dates home to
notify or a number and you'll be able to
discover that information and act with
that very naturally which is cool cool
stuff
we talked a lot about how do you notify
every automation you do need to notify
you know something has been approved
something has been delayed just for your
information and it's usually you have a
call for Action like you receive your
notification like how do you act with
that we give you more tools for this
release which allow you to notify users
where to go what to do
we have more let's say like a Lego
blocks which allow you to retrieve URLs
for entity create adaptive cards
something you can post to gym channel so
people can basically act and know what's
going on why it's important because
we can expose much more users to
business Central to organizations again
Auto limited telling us almost all your
customers
most of your customers are Microsoft
clients out of 100 people Organization
three has busy license 97 don't even
know what that's really exists never
heard about it kind of not my stuff
and when people need to collaborate in
the real world you know different
offices different locations they use
teams for collaboration like I put my
guys on a project from different
locations over the world the same you do
to resolve your customers issues so now
with the teams you can create a channel
like like you can get your all people
talk about delayed orders as an errantly
part of conversation and we don't have
those artificial barriers what to do so
the easiest way to demonstrate that if
you project to the PC so I have created
an approval flow for this widget type
right it's time for us to implement the
approval flow
um now that I've set up all of my events
that I can subscribe to so I've used the
new when a business event occurs trigger
and I've said in the production
environment I want to subscribe to the
event from my extension this approval is
requested for a widget and the company
is in Coronas but this is just optional
for us and now I need to actually send
the approval so I get some information
about this I post some choice of options
to the approver which in this case is
going to be Afghani and if evgeny signs
off then first off I'm just going to
call my API to set the approval State
and now I'm going to use the get URL and
get adaptive card actions to send an
Adaptive card to notify the production
team that this widget has been approved
so to get the URL I can just use the
environment and Company Dynamic content
from before I didn't need to specify all
of this again and then say I want a link
to the web client to this page using
this widget ID and then I would like to
generate an Adaptive card for this and
all I need to do is take the web client
URL that I just generated and pass it to
this action and say I would like you to
format this for teams please and finally
I would like to post a message in our
production nurse announcement channel so
congratulations it's been approved for
production and reply to that message
with the Adaptive card so this is like a
flow for a customer approval for a
customer entity and then you want to
notify people to teams or through
Outlook and then obviously I can go
ahead and take an action and do that so
let's do it right so I'm going to send
an approval request for this we can see
that the state has changed on mine to
open approval and now if I switch to
Afghani
then you should receive a message
you receive a message in the chat in the
chat yeah so there's different ways how
you get notified right now we use like a
board so basically something talking to
me that's why I guess it's like a pop-up
but there is different ways how you can
arrange approvals it can be part of a
child conversation you can have people
can look somewhere time to time and then
basically reply by time allows a lot of
combination same idea exposed two
buttons and I can say approve
looks good
and the ready to roll yep so now that
afghanist approved this hopefully my
adaptive card is going to be sent to
teams so in this scenario now I am Sam
who works for our organization but he
doesn't have a license for business
Central who he works in our production
department and he needs to know that he
needs to start working on this so as Sam
I can see that the beaver has been
approved for production and I can click
details on this adaptive card and when I
click this it's going to open up
business Central in read-only mode on
this record uh because I have an M365
license right so here you can see I
can't take any action but I can still
see information about it so we just
enable Sam
to get data from business Central he can
open it maybe control C control with
some key fields and get going and back
in the day he'll probably call me a
local Excel Samsung data super
unofficial and
it's just great yeah
yep
so
uh that was that so I guess that wraps
up everything that we have to demo today
and I guess we've got a little bit of
time to take some questions and then I
have a little summary to do so
yeah if you can see hands if anybody has
any questions then we'll throw you the
uh box we have some T-shirts to hand out
for anybody who does ask us a question
so uh looks like somebody wants one all
right
there you go
so for the team user that reads the card
does the user need to have a user
defined in business Central to have so
the user is defined for you
automatically so sorry the question I
don't know how loud this microphone is
so the question was does Sam need to
already exist as a user do I need to set
him up as a user in order to see this
data and the answer is no if you have an
M365 license and you try to open one of
these adaptive cards then the user is
created for you automatically
and the permissions are for all the
business Central objects that you send
to teams
so your question was how do you
configure setup so external people who
has no quality business plan will
somehow get access to the data which is
unheard of obviously we don't do it just
because you can I'll take two minutes if
you share my screen for a second how you
could uh how it's basically configured
let's see if
you have an environment yeah so you have
first of all it's a as an admin you need
to enable those capabilities so if you
go to admin Center admin Center to our
you have like a enable access with
Microsoft 365 and by default you'll get
no because
we don't want to expose business data
outside of organization like a horrible
situation to be we don't want that so
you're in control to enable that to say
yes I would like to do it after that you
can also Define Security Group like
control which people like your
organization your employees maybe even
your external vendors should be able to
be part of that then we're giving you to
the product where you define which
permission set should be associated with
this like newcomer we recommend
d65 read meaning they can read cannot
act but you can Define yourself and
finally there is so much documentations
written on that how to do it in a secure
way
so basically you go hide and read and
you enable it in production so we have a
level so we have a number of
administrative steps to enable this
feature it's very controlled process and
we don't expose any data yeah just just
thought never came to us by the way in
the first place so it's a we recommend
you go enable to your customers in a
controlled way show them how it works
build trust with that and go to adopt
because what's happening now you can
have a read-only view you can say hey
why does he or she can I cannot suddenly
just get a nice license and another
license and another license and that
just that's how it grows
thanks uh yeah I mean I think we have
time for one more maybe
yeah great okay well then let me just
wrap up and chill for some more
Microsoft talks so obviously if you have
any questions for us maybe you don't
want to ask us right now but if you have
any questions about our platform what
are the questions oh there's a question
okay let's take it where are we going I
can't Secret Life yeah
it just yeah you're in the spot
invisible spot for us
yeah so my question is how the
authentication works for the external
business events so what what kind of
permissions the the others the software
on the other side needs to be able to
subscribe for the external business
events it's all data
yeah yeah so at least in this case the
way that I set this up let me just
switch back to my
to me so the way that I've set this up
is I have an Azure ad application that I
I set up in my environment that I have
like given authorization credentials to
right so I set that up as an application
in business Central and then I use the
client ID and secret to exchange for a
token and that's how I'm communicating
with the auditor API and the Azure ID
application I think I can show that in
business Central
um so if I go to yeah Azure ID
applications and the tech days 2023 is
the one that I created and when you set
this up you need to provide your client
ID and secret and then you also need to
apply some permissions to this right so
I just gave myself everything because
it's just with the demo but you can
choose which permissions you want to um
to to set and then that application is
only going to be able to subscribe to
events that it has permissions for so
this comes back to the required
permissions from before uh if I only had
permission like let's say I didn't have
permission for this table this I didn't
have the super permissions I didn't have
permission for this then my subscription
will be rejected so it's just not
possible for me to subscribe to this and
I think we check it on the way out as
well so if your permission has changed
then we're not going to notify you right
yeah
um
yeah thank you cool
external business events are in a
preview preview as of now which is
awesome uh probably on the pass2ga
soon maybe fall we'll see so give us a
feedback if you need to improve
something like settings configuration
we hope it just works for you great
you do
we have like let's take two more
questions if you have
um oh there's one up there yeah so I'm
going to run up with the Box
good luck with that yeah
all right
where was I going over there
all right hang on let's do first all
right
nice all right with the power automate
um is there a way of passing through
like instead of creating a flow for a
specific email address can you pass in
parameters to the power automate because
if you've got a big company and they've
got hundreds of people you'd want to
pass in the email as opposed to setting
up different flows and the second part
of the question is can you also pass in
like attachments so if it's a purchase
invoice coming in someone might want to
see the attachment as well from the
customer so as yes two questions the
first is like how can you pass the
parameters and the second is going to be
patch attachments as well so when you
create an automated flow then that's not
triggered by the user it's triggered
automatically when an event occurs right
it's not necessarily like a direct
one-to-one you click this button this
happens so with those it's not possible
for you to pass parameters but it is
possible to pass parameters to an
instant flow so let's say that instead
of using these approval triggers you
said for a selected record for this
purchase invoice then you you start your
approval flow in that case you can
Define parameters in the trigger that
when the power automate panel opens you
invoke your instant flow the panel opens
and then you're presented with
parameters that we've asked you for but
also parameters that you defined
yourself right and in that case you can
have an email field that is then
referred to later right right yeah and I
mean if you like we're going to be down
at the Expo Booth immediately after this
so if you want you can come down and
I'll show you exactly how to do that
right
um and then the second question was
attachments so there's two ways to do
this I think there is like a file input
in the you have an option of like text
email
um file input and some other types of
parameters and I think you can use those
data types to put in there but if you
have like at like a zip file or
something needs to go in then we have an
action in power automate that is get a
document attachment so if you have for
example a document or anything like a
customer with a picture attack or
something like that you can retrieve
attachments using this
um attachments action and you know like
if the attachment is on this record in
business Central then you can retrieve
that attachment and then do things with
it in the power ultimate flow so there
are ways to set that up but it's just
something we didn't demonstrate today
yeah so just so you can get access to
all documents basically saying from BC
give me my PDF of invoice then you can
send it to some scanning solution get
results back some stuff like that so we
give you access to get documents images
attachments we even built a new
endpoints with the previous release to
allow you that so yes you can that's how
I built this power app we show you some
images and then brings those photos back
just by using those apis so absolutely
yeah it's not something you couldn't do
six months ago or 12 months ago
something absolutely can do right now
and it doesn't require any magic it just
just out of the box
how are we doing for time we have like
one minute 30 seconds 29. you take one
more yeah I'll take one more question
and then we'll just go for lunch
together yeah yeah and a follow-up to
the last question can you use approval
flow of business Central in your power
ultimate approvals the power was made
like approval well so I mean today if
you use these um templates then it's
going to create an approval workflow in
business Central right and your approval
uh hello in power automate is linked to
a business Central workflow
um but then I mean if you create your
own custom flow then it's all on you
right then you need to you can create an
approval in the approvals app but then
you need to set up your own API to set
the state and things like that we're
looking into approvals for custom data
types as well with the built-in triggers
but then again this is another thing
that we're working on in the in the
future right thank you
