# BC TechDays 2022 - Empower citizen and pro AL developers to do more with Power Platform

- **Source:** https://www.youtube.com/watch?v=4Rz2hbuTqXM
- **Video ID:** 4Rz2hbuTqXM
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 27m11s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

hello everyone
um so my name is Enrico chimitan and
with my colleague Edison Mercy we're
going to present the last part of this
demo it's going to be empowers it is
well you know the title it's basically
the part about Native connector and the
web client integration with Power
Platform
so how my presentation is going to start
is with some connector capabilities so I
have some introduction on like something
that you probably might or might not
know some announcements and then I'll go
with some demo on how our connector
works and which capabilities it has
let's start with the elephant in the
room that's a question we always get
does this work with on-premise so all
new features and everything that me and
my colleague are going to present are
only for business Central online we
still have the on-premise connector
which we still support of course but
that's still in preview and the new
features are not going to hit that
connector
another question we get very often is
what about license well the business
Central connector has requires you to
have a premium license for database or
powerapps for automate the good news is
whenever you have a business Central
paid license you also get the database
license included so that's good if you
need a trial or demo so you don't have a
business Central paid license you can
still have a trial
and that should be enough for your for
your demos now as you might know a few
months ago we actually removed the
preview flag from the Native connector
so now it's officially GA that means we
fully support it and we're going to
continue investments in the connector
um I'll jump to My Demo
and now I'm gonna show you some
capabilities
for our connector so I want to start
about for um like to talk about the
approvals so you might know that we have
the capability of connecting to the
approval system in business Central
so what's going to happen is for example
in a purchase order you know you have a
request approval buttons here and what
you can do is you can create a new power
automate flow the moment you save it
this button is going to become enabled
in business Central so you can start a
workflow in business Central that calls
into Power automate and then goes back
into business Central to approve the
item
um so I'll show you the first floor
which I already made in interest of time
so this is based on a template we have
templates for approvals for like limited
set of records at the moment for
business Central so for example purchase
orders or customers or vendors and
similar
um and they all start with a trigger
that is called when a asterisk approval
is requested in my case it's a purchase
document so you can see here I have all
my filters on of course the environment
and Company
and then I'm going to get the record and
I want to focus your attention on this
step you might know it already it's a
start and approval this starts on
approval on the dataverse side what does
it mean it means there's going to be an
approval which you like your users can
reach from all kinds of different
products within Microsoft for example
they can approve from here you see
there's an approval section in power
automate but they can also reach the
approvals from within teams so if they
install the approvals up they can just
go into that and just do the approval
immediately from within teams it's very
well integrated with most Microsoft
products and again the moment you create
this flow it's going to integrate well
with business Central as well so that's
the first type of flow you can create
the second type is an automated flow
that runs whenever a record is created
or modified or deleted in business
Central so the moment you use one of our
triggers when a record is created
modified or deleted then we are gonna
basically create a webhook subscription
in business Central that is going to
call back to Power automate and start
this flow then you need to get the full
record because then you get the latest
version of whichever data you need and
you can use it for one of the 600 plus
connectors so last time I demoed
anything regarding Power Platform it was
like 400 plus now it's 600 plus so
you're getting more and more integrated
like first party Microsoft products and
also external products that you can
connect to your flows in my example I'm
going to do the boring demo thing so I'm
just going to send an email to the
customer email that I'm getting from the
previous step
in my example just welcome to contoso
please confirm your data but of course
you can use everything coming from the
previous steps and from any other
connector you can use I'm not going to
show you this working in the interest of
time because we are running a bit over
time and we need to leave some space for
Q a
um yeah so I want to mention by now um
you you've seen a lot of triggers and
such so you might ask yourselves where
can I find documentation for all of
these we have actually two types of
documentation so if you search here in
the connector section in power automate
you'll find the first documentation
and this is basically a list of all the
capabilities all the actions and
triggers we have for our connector and
the second part is within the business
Central documentation instead so you can
go to aka.ms slash BC automate I'm going
to have that to install it later as well
so that it's recorded whenever this
recording gets out and there you'll find
actually the explanation of how it
integrates with business Central and
what you can do with business Central
Empire automate combined
I want to focus your attention for the
last bit of my demo on one action in
particular which we have improved and we
are going to improve as well in the
future that's defined Records action I
would say it's the most powerful one we
have because it allows you to set a
whole lot of different like capabilities
that are basically or data capabilities
so you can set for example the order by
whenever you get in my case the list of
sales invoices so you can get them
ordered by posting date or whatever else
you need and you can also have a top and
Skip so if you're familiar with the data
this means basically you get only the
first 10 records and then you I don't
know first skip the first record because
you know already what it is for I don't
know what you're like implementation
might be but you have the full power of
data like order top and Skip and also
the full power of a data filter query so
here for example in in my example flow
every Monday I'm getting all the
invoices posted in the last week and
these you can achieve by using a data
filter so the connector supports
basically every filter that business
Central supports you might know that
there is there are some weird
limitations if you do cross-column
filters in the NST we have the same
limitation on the connector of course
but other than that you can just use the
full power of filter queries for
business Central so in my example I'm
just getting all these sales invoices
and then posting a message on teams but
of course you might integrate with some
other product or service
so for the filter query we don't have
any help in how you fill in the query so
of course if you want to see the
available Fields you just jump into the
business Central documentation from API
V2 and then you find all the fields you
can use all of these is of course
supported also for custom apis so here
you see that I chose API category V 2.0
but I have a few contoso apis that I
published to my tenant if you have a
custom API you can use it
uh and if you want to create a custom
API we have docs on that as well so you
can find them on the business Central
Docs
last thing I want to show you
still regarding the find Records action
is that we added a few so first of all
we added a new capability which is what
we call paging so until today you will
see here it says maximum a thousand
records that was true until like these
days we've actually relaxed that I need
to change the documentation in the
coming weeks but now you can get more
records you just need to go to the
settings here
and then you can activate pagination so
that means basically we are going to
follow the links in the business Central
data and get as many records as you need
so until today it was up to a thousand
today you can go to 100 000. the reason
you cannot do more is not business
Central it's just because power automate
doesn't want to do too many calls so at
that point it gives you a hard stop of
uh 10 100 0001.
so um so that's regarding the pagination
and the other thing I want to show you
is that
um we a question we get very often is
okay but here I have to specify my
environment name and Company like
statically can I do that dynamically the
answer is in short yes you can and the
way you do it is you need to create your
flow first for one environment and
Company and then you can just have a
custom value here and just like get some
output from your previous steps or have
it Dynamic the reason you need to set up
the flow for one of them first is
because we need to download the metadata
so we need to know like which apis to
use and which which metadata which
environment the method comes from
um the other gotcha is that you need to
use the company do it because behind the
scenes we resolve the company using the
good but if you do that then you can
have it working and very last thing the
other thing you can do using the find
Records action is you can get related
records so in my example I can get all
the sales invoice lines for example for
an invoice and you can do that using the
filter query
uh so here I'm filtering on the document
ID and then I'm getting all the lines
and again I want to show you these
working just because I want to
jump to the Q a and have some time for
that
um good so that's the end of my demo I
want to leave you with some teasers what
are we cooking for the coming months so
we are already working on supporting
images and attachments for powerapps and
power automate so that's coming very
soon right now that's one of the hard
limitations we have it just doesn't work
if you try and the other thing is that I
showed you we have support for related
records in power automate by using the
find Records action that's a bit
unintuitive because of course you need
to know like what to filter on to get
the related record and all of that we
plan to have a better story for that
coming very soon
as I mentioned earlier more information
in aka.ms BC automate in the power
automate docs for the connector or you
can jump to ak.ms BC Yammer if you're
already on Yammer you might know that's
a community of of Partners working with
the power automate and powerapps
connectors and there's a lot of like
questions and answers and basically you
can talk to your peers and figure out so
I'll pass to Earthen and you can go with
your demo
cool uh yeah so Enrico showed us some
fantastic improvements on the Power
Platform side but now it's time to talk
about bringing that into business
Central right so uh you may remember
that in may we shipped the power
automate uh instant actions
functionality so I'm just going to go
over there and do a quick recap of of
this uh for those who haven't seen it so
if I go to for example
the customers list and I look in the
Overflow menu then I should see this new
context menu this automate right so I
can see in here I have to schedule a
meeting flow so I can click this one and
if I click this flow
then it should open up the power
automate Wizard and within this wizard I
can uh I can run the power ultimate flow
right so if I was to step through all of
these steps then uh it would complete
this process so we'll take a look at how
one of those is implemented so if I go
to uh this one this
go open these tabs in the meantime
foreign
so
um the example that we're going to look
at is uh about notifying a customer
about an invoice that they need to to
send a reminder for so we saw a more
complicated example yesterday with the
AI Builder and of course you can build
more complex Integrations with Power
Platform
um but we're just going to keep it
simple for this demo
if it shows up
okay yeah so uh the flows that Enrico
showed were all based on some of our
existing triggers for example when a
record is modified or created and those
flows all run automatically but the
difference with the instant flows is
that they're triggered manually by a
user so in order to get your flows to
show up in the automate menu in business
Central then you need to use this for a
selected record trigger and in this case
I've said for a selected record from
this table the sales invoice header then
what I would like to do is get some more
information about this record first and
foremost so I can take some of the
dynamic content from this trigger for
example the environment I did the
customer is in and the company ID that
they were in and also the idea of the
selected record retrieve some
information and then
craft an email about this using some
information about that record right and
then if I go to business Central select
an invoice and invoke this flow then it
will execute this flow and then send an
email so just a couple things to
remember about this is that of course
you can use the filters to limit where
this is shown to a specific context so
if I want that flow to show on the sales
invoice page for example I can use the
page and table filter or I can limit it
to specific company so if I'm working on
my flow I can filter it to the sandbox
and keep it there so that users can't
see it
uh yeah you prevent your users from
running your flow against something
unintended like running a sales invoice
flow against a warehouse or uh you know
meet an invite with a document right and
then you need to take advantage of
dynamic content as well so you can use
the environment name sorry you can use
the web client URL that we provide and
the page ID to link to the context that
the user was in when they executed the
flow so you can share a link to the page
that the user was on you can get some
additional record information with the
system ID of the selected record and of
course you can build your flows in a
more generic way as Enrico was
discussing before as well using the
environment name and Company ID in the
the first two fields uh so now I'm going
to talk about some new stuff in 21. so
if you've used this feature and you have
gone into the personalization then maybe
you've noticed that uh that like if you
try to personalize an action you see the
personalization UI but then when you go
to the ultimate menu nothing shows up
right so we've made some major
improvements in this area in the next
update and now I'm just going to give a
quick demonstration of the
personalization stuff so um
we're back in business Central and we're
on the sales invoice page so what I'm
going to do is uh activate the
personalization mode and when I hover
over this do you see the UI shows up on
these actions and now when you go into
the automate menu the designer UI shows
up there too so I can take this send a
reminder flow for example and I can drag
it to the root level of the command bar
and now instead of being buried in the
automate menu that flow is placed in a
more prominent location that uh you know
now as a user I have more access to this
right and of course if we support the
personalization then we also support
customization so I'm just going to look
quickly in the uh this posting group
then here is a flow this notify when
posted that I customized and we're going
to come back to this in a quick second
uh so just a couple tips on this
personalization so you can take action
from the automate menu and you can drop
it any way that you can drop a standard
action so for example in the promoted
area or on the right hand side or the
repository area on the left hand side
the only place that you can't drop it is
in the automate menu because this menu
is generated automatically from Power
Platform data and if you move an action
to the repository then it's just going
to create the action of the place that
you dropped it if you move it to the
promoted area then it's going to create
a base action under the actions group
and then an action reference which
refers to this base action and of course
that means that if you blew a lot of
personalization you're going to create a
lot of Base actions in the actions menu
and maybe you know it's unintentional
maybe you end up with a lot of stuff
that you don't want there but don't
worry if you made a mess then of course
you can clean it up with clear
personalization or via the customization
personalization management pages
uh and maybe you're thinking my promoted
section okay I understand the word
promoted but repository action reference
what is he talking about right then I
have a fantastic recommendation for you
in about 40 minutes in room five
there'll be a talk what's new in
business Central for Al developers uh by
Quentin and ego and they'll be talking
all about the new action bar model where
they'll explain all of these terms right
so don't miss that so I was saying
before I've customized this um this
action on the sales invoice this notify
when posted right so if I'm able to do
these personalizations and
customizations then you know this must
be represented and stored somewhere
right so how is this stored well uh I
can export the customization and produce
the uh like for customizations file zip
folder and in particular I have this one
the sales invoice list configuration
that I did earlier so if we look at that
file in vs code
then you can see I have this page
customization and in the posting group
I've added this custom action object and
we'll come back to that in a quick
second and then I obviously have an
action reference because I promoted this
action right
um so okay custom action what is the
custom action uh We've introduced this
New Concept in v21 and custom action is
an action which uh is handled by the
platform right so you can execute an
instant flow for example maybe we'll
introduce some more types down the line
right now this is the only one uh you
can leverage these custom actions in url
extensions to take advantage of platform
Integrations so uh this is what our
custom action looks like and how it's
built right obviously you need to say uh
build me a new custom action and the
implicit type is uh flow right and we
infer this from the other data that you
use so you know if you start writing a
flow action you don't need to write this
but it's important to know that it's
there
uh and then the main thing that we need
to put is the flow ID right so we need
to tell the platform which power
automate flow it should run and it's
represented by a good which you can get
from Power Platform itself and we can
stop there if we want this is the
minimal custom action this is all you
need to start running your power
automate flows from Al actions but of
course there's more flexibility with the
system that you would want to take
advantage of so if you're in a situation
where you have multiple Power Platform
environments then you can specify the
Power Platform environment ID of the
flow and then you know you can have flow
actions which run from different
environments
um but in most cases like if you only
have one environment you want to Target
then you can just omit that it's an
optional parameter and then you can set
a default caption right so the flows may
not necessarily be accessible to all of
your users so you can provide a default
caption in case we can't retrieve the
data or that flow is not available to
the user at the moment and you can set
Dynamic visible and enable properties to
determine whether the action is going to
show up and of course you can set things
like a shortcut key like standard Action
Properties
so how does it work right with the
standard action object uh it produces
some UI in the platform and then when
you user clicks this UI then we call
back into your on action trigger in Al
right but I mean you can't write an
email to trigger these power automate
flows manually so what we do instead is
we have these custom actions and they
produce this UI in their platform and we
merge the metadata from Al with the
properties from Power Platform so for
example the caption and whether the flow
is enabled and we'll tie all that
together and produce an action for you
and then when the user clicks it we
invoke that directly in uh Power
Platform so there's no need for you to
write any Al code to implement a
behavior all you need to do is tell us
which floats are run and then we will
take away with the rest uh so where can
you add these custom actions of course
you can add them in pages and also in
page extensions and in any place that
you can add a custom action you can add
a reference to it so that you can have
copies of that action particularly in
the promoted section so just one tip
here uh the caption property will be
overridden with data from Power automate
so the caption of your flow is what
we'll show in business Central but the
caption will be shown when the flow
isn't available for example if that
particular user doesn't have access to
the flow so make sure that you define
something so that it doesn't show the
the control name and
since the actions rely on power ultimate
and also the users have a couple of
options as to how they can access this
feature it's possible that the user
won't have access to a particular action
so it's important to know whether the
action is going to be disabled and
remain in the UI or we're going to hide
it entirely right so the action will be
disabled if you set the enable property
to default I know property to false of
course but if the user does not have
access to the flow it'll also be
disabled if the trigger filters exclude
the flow from this page you put an
action on the wrong page it'll be
disabled or if the flow is turned off in
power automate altogether then we'll
also disable it there too they actually
be hidden entirely if you say visible to
false if you hidden it via the incline
designer so you cross out the action to
to move it around but also to hide it uh
the user or admin is disagreed with the
Privacy analysis or if the user doesn't
have permissions to access this feature
and we'll just come back to this at the
end of the demo
um so now you're thinking if I can write
these custom actions how do I tie this
into my Al extension how do I ship this
via appsource right it's all good being
able to customize this on an individual
tenant but how do I deliver this at
scale so
you need to produce two parts to this
right normally what you would do is you
take your Al extension and ship it via
appsource but now you can also put
together a Power Platform solution
containing things like power automate
flows and connectors to enable those
flows package those into a solution and
you need to ship both of those so the
first thing you would do is develop this
Power Platform solution and then you can
export that solution into a zip file
which contains some information about
the objects in this solution so then you
look inside the solution inspect it and
find the ideas of your flows to
reference and now you can start writing
custom actions that refer to those flows
so then you publish to appsource and the
customer installs your extension and
then separately you also need to deliver
the Power Platform solution to the
customer's environment so you know this
is like a nice diagram of how this works
but it would be good to see in action
how that looks right so we know where to
find all these things so I'm going to do
a quick demo of this where I walk
through uh just producing a small
solution and a small extension so um
if I go back to the browser then the
first thing that I want to point out is
on the left hand side in power automate
you see the solutions at the bottom
right so this is where all of this power
automate solution stuff is going to
happen
um so here I have my list of solutions
and this my business Central solution is
the one that I created for this demo so
if I look inside this one I can see that
I have a bunch of different uh
flows for example I have this Notifier
when posted and also schedule a meeting
and then what I want to do now is I want
to export this and produce this ZIP file
right so if I take one step up to the
overview of this solution then I have
this export action and if I click this
then after some time power Power
Platform is going to provide me a link
to download the zip file for this but I
prepared this earlier so we'll just skip
ahead for time uh if I go back to this
folder then look inside the platform
solution this is the output right so
there's a lot of metadata here about the
solution and the caption and ID and
things like that but what you really
want to look at to build your IL
extension is this customizations.xml so
if I look in this file
then I can see that I have an XML object
for every flow that I'm looking at so
for example I have this one workflow
here to schedule a meeting and I have
this workflow ID and this is the one
that I need to use to refer to this
power automate flow so I'm just going to
copy this and now I'm going to start
writing my Al extension so what I can do
is I can write a page extension
and what I want to do is add a custom
action into the processing area just
into the actions menu so now I'm going
to write a custom action and I need to
give it a name so we'll call it a
schedule meeting
and then we need to give it a default
caption so we'll say schedule meeting
and now I need to type in the flow ID so
if I publish this then I would get an
action in the actions menu which runs
this power ultimate flow right but it
would be nice if I promoted this as well
so maybe what I should do is add a
action reference
and point it to this action so we'll say
uh schedule meeting promoted
and then point that to this schedule
meeting
this is it it's as simple as that I just
need to take the IDS from the solution
and put them into the AL extension so if
I publish this and you know again we'll
skip that just to cut down some time
here and I take a look at the customers
list then you can see that the scheduler
median has been added to the promoted
area and then if I look inside the
actions menu
and because it was promoted it's been
put into this little overflow menu here
I also have the base action that it
refers to schedule a meeting and now if
I click this
oh no
I think I clicked it too fast
okay
yeah so if I click this action
then it's going to run the power
automate wizard
and you can see that it's running the
scheduler meeting flow from the solution
so uh yeah just one particular tip for
Distributing by appsource is that you
can leave this flow environment ID blank
right so if you're building these things
in your own environment then you're
probably going to start hardcoding
things like the environment ID and the
flow ID but that would point the flow to
your own environment so if you leave
this blank then the client's going to
search for the flow in the user's
environment so once you've imported the
solution to their environment we'll
search there instead using the
particular flow ID in the in the default
environment last thing that I want to
talk about is privacy and permissions so
as of v21 this feature is now generally
available and that means that we have
removed the feature key and as a result
of that the feature is enabled for all
tenants right the users now need to
agree to a privacy notice to use this
feature but you can get started much
quicker if the admin goes in and accepts
on behalf of all the users and I'll just
quickly show this too so if I head to uh
a new company that I created
I have this my company this is a company
where I've never used this power
automate feature before right so I'm a
brand new user to this and uh you can
see the extension that I published
before this action is disabled because I
haven't accepted to notice yet so if I
look inside the automate menu there's
some new UI this gets started with power
automate we don't make any requests to
get your Flows at this point we just
show you this and if I I'm intrigued by
this feature so I'm going to click this
and now I'm presented with a nice little
marketing page with some information
about this power automate feature and if
I click next then I'll be prompted with
the option to agree or disagree to this
privacy notice and we built this in the
same way that any partner could uh you
know you can just hook into the Privacy
notice module and provide a custom
wizard we just did the same thing
um so the other thing is that we've
added a new permission this allow action
automate so if you assign this
permission to users then they will be
able to use the power ultimate feature
the UI will show up if you remove this
permission then the UI will be hidden
for them so you can hide the menu for
people that aren't supposed to be able
to run in these flows to avoid the
clutter in the UI but you should
remember that this doesn't prevent the
user from running any flows it just
prevents the UI from showing up in
business Central if you want to prevent
the user from running the flows you need
to use uh like roles in Power Platform
so if you want to opt out of this
feature then the users can of course
move or hide the actions via
personalization decline the Privacy
analysis the developers can use
customization to move actions or hide
them or you can write Al code in a hide
them across a page extensions
and administrators can assign
permissions to remove the feature for
particular users or decline the Privacy
notice on behalf of everyone to disable
it globally so just a quick summary uh
Power ultimate action is a ga so you
build these powerful Integrations like
we saw at the keynote yesterday without
writing a single line of code we now
support personalization customization of
the designer so you can make these
actions more prominent for your users to
access and of course you can write these
in your own appsource extensions using
custom actions and now we've provided
some new methods for you to opt out uh
yeah I think we would sort of running
very sure we actually out of that time
so um thank you all for listening and uh
me eriton and on at Georgie and Lucas
are going to be here so if you want to
ask any question please come down here
and find us thank you thank you
