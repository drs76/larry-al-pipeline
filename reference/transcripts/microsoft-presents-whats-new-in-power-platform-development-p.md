# Microsoft Presents: What's new in Power Platform development: Power Automate and workflows

- **Source:** https://www.youtube.com/watch?v=pkqMT-BXK_k
- **Video ID:** pkqMT-BXK_k
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 45m44s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

okay second day of tech days when ready
uh hello and welcome everyone my name is
Monica alja and I'm a senior software
engineer at Microsoft uh team in
Copenhagen Denmark and today I'm going
to talk about uh what's new in Power
Platform specifically focusing on power
automate and
workflows this is going to be a demo
packed session and I want to show you as
many demos as possible so uh we'll be
doing the Q&A together at the end of the
second session following this which I'll
be presenting with I geny uh where we'll
be talking about how to develop co-pilot
experiences using Power Platform so
let's get
started uh since we talk about Power
Platform uh let's do a quick refresher
what is Microsoft Power Platform uh it's
the world's most complete set of
integrated low code development tools we
have co-pilot Studio we where you can
create your own co-pilots using power
platform we have power apps where you
can create apps both the modern driven
and the canvas apps uh we have power
automate which we're going to listen
about in the next 45 minutes uh we have
powerbi where uh you can use the
business and analytics uh uh and and use
reporting and all
that and then finally we also have power
Pages where you can host external
websites uh and all these are together
uh connected through Microsoft dataor uh
and it also has integration with AI
Builder which we're going to talk about
a lot in the uh next few minutes and uh
of course the core of it is
connectors um with all these products
there's one thing that is common and
that is data and the data comes from
these
connectors I have done this presentation
uh these presentation since few years
and every time the number of these SL
number on these slides keep increasing
there are 1,400 plus ways to bring data
to Power Platform and of course business
Central is one of them we have
connectors for both business centrer
online and Business Center on
Prem but let's talk about what we have
done with Power Platform and business
Central recently
we have provided support for power Pages
via data virtual tables so now with
business Central data that is exposed
through virtual tables you can create
external websites using power
Pages we're going to talk more in detail
about what improvements we have done
with power automate but overall we have
added many actions and many improvements
in the
connector we have improved the approval
experience using power automate and we
we have done many many many new
templates including the templates which
use GPT actions and AI
Builder we have delivered power app
samples in GitHub where you can get
started with power apps uh and use those
samples as they are or build on top of
them and last but not the least in
powerbi we have embedded support for
scorecards as well so so that's all we
have delivered recently with P platform
and Business
Center let's talk in detail about what
we are here for which is power automate
business Central and power automate
provides basically the way we see it as
three ways of integrating with power
automate uh we have approval
flows we have automated flows the flows
basically that are created using a
trigger a trigger is an event
that happens uh that tells something has
happened and you can do some actions
based on that events and those are
automated flows so you can automate when
something
happens and then we have custom actions
based on instant flows or manual flows
which is basically you want your user to
manually click something and then
automate the process and we provide
integration of these Flows In Business
Central uh but we also provide lot of
templates templates are basically uh
some predefined set of flows that you
can use as it is again or build on top
of
them so what we have done recently is we
have created a single group in every
page inside business Central where you
can get started easily with how to
create these flows with these three
integration points so you'll have a
power automate group in every page in
business Central and you can access
these three actions where you can create
flows based on templates so first and
foremost approval request flow this is a
special action this is not actually
available on every page this available
on pages where Al developers you define
it um using custom
action and the scenario could be you
want approvals for sales order and send
emails or teams
notification second is automated
background flow um this is this is
basically the flows that you create
using triggers and now we are also
supporting flows with business events
that we're going to talk about more in
detail and imagine a scenario when an
email is arrived you want to create a
sales order
automatically and then the F final
integration point which is the create
actions based on instant flows this will
be creating actions using templates uh
that will show up on the pages that you
want and when you when the user clicks
on them you can run the flows behind the
scenes and last thing no more feature
management needed anymore this will be
the default experience now for all new
and updated
environments talking about templates
because that's the three buttons do they
lead you to template experience we have
added more than I don't know 40
templates I think there are in total 70
templates now we have added templates
for approvals where we support not only
the First Response where one approval is
enough uh multiple responses where you
need to say I need approval from three
people or four uh or custom you can say
I want approval from first this one and
then later we support templates for all
of those and we support templates for
both Outlook scenarios and team
scenarios with the automated category we
now support templates for every built-in
business event that comes out of the box
from Business Center so you can just get
get started with one of these templates
and you have it uh you can just run the
flow and then with instant actions we
have added more scenarios to help you
guide how you can go ahead and customize
with more scenarios
and we are going to create more
templates that will be coming soon that
will be using the AI Builder GPT actions
I'm going to show some demos for this
later talking about GPT actions let's
see how we have infused AI with power
automate so we have done it in multiple
ways the first way is as I said we will
be
using business Central flows with AI
Builder GPT
action and now you can automate your
business processes with generative Ai
and power automate together in business
Central we'll be creating new templates
in all the three categories and these
will be coming later in the
wave let's see the demo
okay here I am inside purchase invoice
in business Central and as I said every
page in business Central will now have a
automate group with the Consolidated
View and you can just go ahead and click
uh on any of
these but let's go to the demo that I
want to show uh which is in sales
orders and not only I have the ways to
to create flows but now I also have a
new action here which is the action that
I created because I use the manual
instant
flow and let's go ahead and see what
this action does so imagine a scenario
where um you realize that there is a
sales order that is supposed to be
delivered today but it can't because
it's raining heavily and you want to
change uh this the delivery date but you
also want to send a no ification to the
End customer saying hey I apologize and
uh how to do that so let's see how we
are using GPT action in this
scenario so I'm just going to go ahead
and run the
flow and what it will do behind the
scenes it will open the power automate
uh experience to actually run the flow
that was created behind the
action and it asked me what is the
reason of the delay of the order I'm
going to
say bad
weather and then it's going to okay then
what's the new delivery date I'm going
to say it's going to be delivered on
Monday now you saw a few things here
already you saw that I actually didn't
write any Al code and these inputs are
coming from Power automate flow we'll
see
how so I run the
flow and let's see how the flow looks
like so this is the this is how the flow
looks like it starts with the manual
trigger called for a selected record in
this case the selected record was sales
order and you could see the input fields
that you saw are coming from these two
Fields reason and
date and I'm specifying that the table
is 36 which is the sales order table
then getting the record initializing
some variables but this is the thing
that I want to show here we are now
using the new action called create text
with GPT what it does is it takes a
prompt and the prompt could have been
the built-in prompts which is AI reply
summarize sentiment extract you could do
that but you could also create the
custom prompt like we did and let's see
how it looks like so in this case it
looks like please craft these are the
data of the sales order that I'm passing
to you and please craft an email saying
we apologize for the delay and what's
the
reason and then we actually send all
that
input and then what is important is to
involve human in the loop you do not
want to rely completely on the AI to
send the email to the customer you want
to first see how the email looks like
from the AI so let's see that
so in approvals I have got a request for
approval about the email that AI model
created for
me and you can see this is the this is
how the email looks like so it figured
out the customer name from the input and
then it says I hope this message finds
you well I'm writing to you that the
delivery has been late and it also took
into consideration the inputs that we
provided on why it is late and explains
this to the End customer I don't have to
write the email manually anymore tpd
does that for me so let I I actually
like it I couldn't write it better uh
than this so I am just going to say
approve
and then the flow
continues and it actually changes the
date uh to the
right reason let's see if it
did WR
dat yes you can see it's on Monday and
it also notifies me on teams
that this was the suggested email you
can just copy paste and send the email
to the customer I could have also
automated that in my flow if I needed
to okay that was the demo with GPT
actions let's switch
back so you saw one way of how we are
infusing AI with power automate let's
let's see another way we're going to
create a way for you in business Central
to describe your scenario in natural
language and let co-pilot build the
steps for you in the power automate you
might have seen this experience already
in power automate if you if you have
ever logged in there but now this
experience will also be integrated
inside business Central this will be the
preview of this will be coming later in
this
year let's see how this looks like I've
recorded the demo for this
so let me show you how it
works so imagine uh you have a new
action called create a flow with
co-pilot and this is how it will look
like and it will open an experience for
you where you have an input box to
actually provide your scenario in
English in natural language
uh right now it only supports English
you could also choose from the examples
that are
predefined so I'm just going to go ahead
and say when an item is and a when a
product is created and right right when
I start typing it is already suggesting
me so I suggest go and say when a
product is created create a flow for me
create an item for me in SharePoint and
now it suggested the steps for those
what for the scenario that I'm
describing so when I click next it
realizes what are the connections that I
need for each of these
steps uh and I can just say yeah this
looks fine and in the next window I
could just F fulfill the parameters that
are needed by these which are not
already defined most of them will be
already defined but in some cases
because I wasn't explicit in my prompt I
have to fulfill the parameters so in
this case I'll say I want this list in
SharePoint and then the flow will be
created
let's give a title to the
list and the workflow has been added
successfully I can also go ahead and see
this flow in power automate on how it
looks like and you can see that it
created a flow with two steps where it's
saying when a record is created which
means when an item is created duplicate
that item in SharePoint so create an
item in SharePoint I could also use scop
pilot to edit this or
um add more steps to this flow if I if
needed isn't it
cool
okay so that was all about how we are
infusing AI with power automate but
that's not the only thing we have done
with this recent releases we've also
improved the approval experience overall
we've done many changes to the templates
so you could use the approval experience
right from the template without doing uh
without needing to do a lot of
customizations what have we done uh we
don't require anymore for users to uh uh
add environment and Company when you
create flows from the template we have
added more detail s in for requester
we're also now supporting the cancel
approval request inside
templates and we have added the approver
information from business central inside
the template so you don't need to
provide this details when you are
actually creating the flow from the
template it will be automatically
retrieved in business
Central I see the demo
okay this time I'm actually going to
show you the experience of creating the
flow from the template so I went go to
the single entry point for purchase
invoice and I click on create approval
flow
and here I
see filtered templates for purchase
invoice for approval scenarios that are
supported by default let me just go
ahead and select the first response one
I'm going to say
it uh demo
two it automatically determines what are
the uh connections that are needed for
the template
steps to create the flow and here you
can already start seeing some of the
improvements so it doesn't ask me which
environment and Company it is
intelligent enough to determine what I'm
using uh from from the
browser it doesn't even ask you which
approval you want it's just asking do
you want to change the title of the mail
that will be sent to the approval so
let's just
say
requesting approval
and then you go ahead and create the
flow
and it just creates the
flow I want to show you where the
approval details are coming from so we
have this approval user setup
table and this is where you define who
is the approver for whom you can also
Define um the extra condition
but right now we aren't supporting that
in power automate this is only for First
Response direct approval scenarios where
we are supporting to fetch approver from
business Central to power automate so uh
in this case Mayan's approver is admin
and I'm signed in as a admin user so let
me just go
to my flows and see if the flow has been
created and yes the flow has been
created
let's see how it looks in edit
experience I just want to show you how
templates are useful so I'm going to
zoom out and show you this is a very
complex flow but because you because
these templates are available you can
just build on top of them and that makes
life a bit easier for
makers so it start with the trigger that
is special for approvals in this this
case since we said purchase invoice it
starts with the purchase document
approval is requested this you might
have seen in already before but what I
want to show you is the get direct
approval action which is the new action
that we have added which fetches the
data from the approval user setup table
and sends it to the approval engine in
Power Platform this is the approval
engines action and here we have also
done some minor improvements we we
weren't adding requester in the email
and things like that so we have now more
details about the requestor so approver
can use
it and furthermore we have we were only
supporting in templates the approval and
reject scenario and now we are also
supporting the cancel scenario so if the
requestor decides to cancel then
business Central is also informed about
that with this
template let me just sign in as Megan
and uh show you how it works end to
end okay so since the flow is um enabled
oh this is the document I already used
for so let's just uh choose another one
yes for this document the status is open
so hopefully the button is also
enabled um and I can just go ahead and
say send approval
request and what it does the first step
is it changes the status so now it's
pending approval so you cannot uh do uh
to edit and post actions should be
restricted until somebody approves or
rejects or or the requester cancels
himself okay
so Megan has sent an approval to admin
so if we go to
admin we should be able to see this
approval now there are multiple ways to
see this approval
request um the first one is we could go
to approvals here and then see that we
have received an request but also my
flow allows for a request uh in the mail
so I could see that we have the same
engine and teams so you could also so
wherever you are working you should be
able to receive a notification that
Megan has asked uh for an
approval and yeah it all looks good so
let's just go ahead and approve and then
what will happen behind the scene is it
will inform business Central that the
status has been approved and you can go
ahead and release this or uh do whatever
action you wanted to do okay but let's
say Megan realized oh she want to do
something before the approval obsess so
she wants to cancel this
request um so she could
also go to Power
automate and in the sent request
she could say
cancel and now what this will do
automatically for admin it will remove
these notifications and for the email
status it will actually say this is now
cancelled so admin don't have to do any
action so this is the new thing that we
are supporting in the templates since
last
year cool that was the approval
improvements are you guys saw with me
still
Yes okay we talked about Ai and you saw
action based
flows we talked about approval
experience and you saw improved
experience now we are going to talk
about automated integration
flows and one of the ways uh we support
already a lot of triggers for automa
flows when a record is created when a
record is modified deleted but recently
we start also
supporting business events what are
business events what are external
business events these are basically
events that happen in business Central
and are exposed to the external world so
those are called external business
events and now power automate also
supports these events how by adding an
action called when a business event URS
and that action can now find all the
business events that has been exposed
not only the built-in one but also the
custom action events that we can expose
through Al extensions I'll show a demo
for that but before I go there I want to
say now we have for all the buil-in temp
uh for all the buil-in business events
we also provide some templates uh so you
could build on top of that so let's see
the demo on how we can do custom
business
events
so I have the rewards extension which is
a custom extension this same extension
that you might have seen in the keynote
uh and what it does is basically creates
rewards entities for loyal customer
customers and depending on how much
sales they are giving to business
Central it gives you different reward
levels gold silver bronze and give
depending on that the level customers
get specific discounts
simple um in the re in this extension
now I added a code unit where I'm
exposing an external business event
called on customer gets gold reward
level and this happens when somebody's
uh so loyal that it reach to the final
level of
discounts uh and this event is
triggered in a subscriber of another
integration event
called uh on customer reached goal level
so one of them is an external business
event and one of them is an in sub
integration event
here uh and I'm subscribed to that
integration event to expose a external
business
event let's see where this integration
event is
raised so I'm raising
this here whenever the level of the
customer is changed and if that level is
gold then I'm raising that integration
event and in the subscriber for this
integration event I'm raising the
external event so let's see how it looks
from Power automate
site so I have a flow that starts with
the trigger when a business event occurs
and
here uh I can see that in my sandbox
environment where I published my
extension I also have the built-in
events but I also have the custom events
the custom event that we just
saw so I can choose that and then go
ahead with my flow in this case um it's
getting the URL for that customer and
sending it to the Post uh posting a
message to the team saying this customer
has reached goal level go ahead and send
them welcome instructions for this new
level and maybe terms and conditions
depending on the new
level let's see how it
works so for this I have to switch to
sandbox
and let's go to the
customers and here you can see the
reward ID is uh not assigned
gra it should have been gradual from
bronze to silver to gold but let's just
say that this uh gu is now eligible for
gold
level and now since I changed the level
to
Gold uh hopefully the trigger should
have fired it should have informed power
automate that this this event has
happened and power automate will listen
to this event and do the steps that they
need to do for automating the proc
process so
hopefully here I have received the flow
uh output which is my customer has been
promoted please go ahead and send the
welcome
instructions or in this case I also
automated send a welcome
instructions so far so
good yes
cool okay
so this was about automated flows using
business
events but that's not it all you saw is
now how was the different ways of
integrating with power automate but that
is possible through Power automate
connector and connector is something
basically that sits between business
Central and power automat platform and
connects data and that component is also
crucial for you guys to know so you can
understand how to create flows better
and we have now added new capabilities
with that flow uh with that component
first capability we've added a new
action called get list of companies all
the
actions uh in the connector ask for an
environment and most of them also ask
for a company
there was feedback from you all that we
want to enable scenarios
for flowing data across companies and
this is the tool for
you uh this one accesses the company's
API and list all the apis uh list all
the companies through this
API and you can use this action
basically to flow data from one company
to another
company that's first action
another action is a need for find one
record action in the connector we had um
an uh an action called find
records which was the way to find
multiple records uh but we never had an
action to find one single record where
you you might need it for multiple
scenarios and the workaround was to use
find multiple uh records and then apply
the loop and then go for the one record
where you find the condition and do that
instead of doing all this and a complex
Loop complex steps in the flow we are
now providing you one single action for
find
record finding one
record this how it looks
like it allows you basically
to get one record based on the condition
that you are specifying in the
filters or you can also specify the
order on how the filter should be
applied but otherwise if you haven't
specified anything it gets you the first
record of that table
okay improvements in connector we have
added new
actions but we're also
making makers life
easy
previously uh we didn't had support for
dynamic companies what do I mean by that
uh if you go to an action in power
automate uh you would not be able
to uh get data for your create record
metadata uh like what are the fields
without specifying the
company that's fine no problem still
there you can just specify the company
and go ahead but now imagine this with
big flows where you have 20 actions and
you want to change the company you have
to do it in 20
actions maybe you can do it still fine
now imagine this was 200 actions and now
it's get okay it's too much I I don't
want to do it I just want to make make
this flow work for another company or I
want to change the company this should
be possible and now it's possible
because we are providing this
support because we did this there were
some uh other improvements that we
wanted to do the same for
environment
and the way to do it for environments is
to use data verse environment variables
it's just a technique to Define a
variable for the entire data was
environment and and that variable then
can be used to choose provide business
Central environment and then it can be
used across the flows so now you have
basically support
for getting environments and companies
updated easily if you want to change
them for multiple of
them what
else we have done some small
improvements by default now the API
category will be defaulted to v2.0 which
is the most used uh
apis from our
Telemetry all the triggers will be also
enabled in the new Power automate
designer for example the hybrid trigger
uh for a selected record wasn't uh
enabled before and now it will
be and we're also doing some
improvements for collection
records what are those so imagine a
scenario where you are changing multiple
records in Excel
and uh you have automated a flow saying
when a record is modified do something
now we had a limit before that if you
modify more than 100 records in a short
span of seconds then um the flow will
not trigger because the max limit is 100
but it's very easy to modify lot of
Records in Excel it could be more than
th000 records in less than 30 seconds so
then the flow will not trigger
so we have changed this limit now
depending on the Telemetry that we saw
and now this limit is
to, so there will be triggers thousand
times and you can run the flow for
collection
record
um finally this is actually my favorite
slide which is there are no more we2
actions
in the connector there will be only
updated actions the recent version so
you don't have to handle what does that
mean for you if you have flows that use
V2 actions already it won't break now
but it will be deprecated soon so start
moving to V3 actions as early as
possible um some Partners got this
confused when we announced it with V28
apis please this has nothing to do with
V2 apis V2 apis will be supported and
that that is how power automate will
work it's about we2 actions in the
connector okay we have 6 minutes left
and I want to do some final
bits so we learned a lot about power
automate uh in this session but I want
to wind up with how to get started if
you haven't yet and the simple thing is
that now this power automate group will
be available in all the pages in
business Central all you have to do is
make sure these two things
first all your users need to agree to
the Privacy notice if you have an admin
user then they can agree on behalf of
all the users and second
you need to make sure that the users
have the appropriate permission to see
that power automate group that's it
that's that's the simple thing to get
started with power automated inside
Business
Center optionally if you are using
multiple power automate
environments then you can also go to
assisted
setup and
select which power automate environment
should be the default environment for
business
Central this was already possible
but
soon we will be introducing this
capability for admins to do it in
business Central admin
Center so you can link your power
automate environment to business Central
using the admin Center as an admin and
then by default all the flows that you
have configured will be taken from that
environment okay we have four more
minutes
um and uh these are the resources that
you need to know for power automate it
will be aka.ms /bc automate but if
you're like like me where you don't have
a very good memory you only need to
remember one link aka.ms /bc all and you
can get to all of these
links okay we have 3 minutes so let's do
some
questions yes okay um I will throw
actually I will ask if Genny to throw
this for you because I can only throw
exceptions not
this okay back joke
sorry yes like this okay yes looks like
uh one easy question I saw copilot to
help you generate power to my workflow
uh does it come with the license should
I have another license to of this very
good question I have a slide for this
wrong
PC sorry answer to
this not this
dech okay ah here found it cool
yes yes this is
the licensing uh for Power Platform and
let me spend a few minutes since we have
some time um so with business Central
Essentials and premium you pretty much
have access to all the Power Platform
products with limited usage rights what
does that mean it
means you get to use these products for
business Central data
okay when you buy business Central
essential or business Central premium
license to answer your question copilot
studio and AI Builder does not come uh
with by default business Central
licenses you have to additionally buy
these
license with business Central team
members you have access to some of them
as you can see there okay thanks and
just one other quick question um I see
that you guys are adding more and more
workflows uh for approval within power
Tate but we already have existing things
within business Central and standard
ones what's your vision uh everything in
power toate tomorrow or are we keeping
both ways to do approbations were it's a
good it's a good question so uh I I
would like to rephrase the question uh
we also have workflow engine inside
business Central that is not dependent
on power automate and that also supports
for a lot of scenarios uh including
approvals and uh long term we have the
vision of at least going completely
independent of the existing workflow
engine
uh for approval
scenario long term uh and of course it
will follow the right process we'll let
you know when we'll get there so we'll
deprecate so no need to panic um if you
have flows
already uh but to deprecate
entirely the existing engine maybe not
right now because as I said the existing
business Central engine not only does
approvals but it can be used to automate
more processes as well can you talk
about
onr yes um we are keeping the existing
engine also for on Prem purposes right
now uh because the Integrations with
Power Platform is
mostly uh business Central online or it
is kept up to date with business Central
online uh there's also a platform on
Prem connector but the recent uh
improvements are only done with online
collector okay uh that would be it now
it's time for the next session where you
get to learn how to build co-pilots
using Power Platform
[Applause]
