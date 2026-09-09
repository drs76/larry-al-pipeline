# BC TechDays 2022 - Build collaborative apps for Business Central with Microsoft 365 and Teams

- **Source:** https://www.youtube.com/watch?v=RUCaTfNJxDo
- **Video ID:** RUCaTfNJxDo
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 41m11s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

[Music]
ladies and gentlemen welcome to in this
afternoon session please welcome monica
sam and jeff gainey
[Music]
hello everyone welcome to the session um
monika evgeny sam here we are going to
talk about
how to create extend and use
business central integrations with
multiple different microsoft 365
collaboration apps
so
let's just assume that we work for an
organization that is responsible to give
loyalty rewards to the business central
customers and how do we do that we have
an extension for it so let me show you
the extension quickly
so
we have a reward entity a table for
reward which has the reward id and it
has the minimum purchase amount criteria
uh that you need to meet if you want to
reach to a certain reward we currently
provide three reward levels um prone
silver and gold
and uh
once you meet the reward level then a
certain discount percentage can be
applied to that reward
as you can see we have also extended
some customer entities here so we can
store which customers and current is at
currently what reward level
so we are now going to show you
the scenario for a case that we got to
explore what is the reward level for
customers
and
we are going to show you how we can
sorry
uh we're going to show you how we can
analyze the
reward level for a customer so let me
first see
to go to customers and see what is the
reward level for the support case that
we got so we are going to go to editing
corporation and we see that currently
the reward level for this customer is
silver however the total sales do look
too high so they must have met the
criteria let me collaborate with my team
to see
what is the issue here and any
collaboration starts with share so i'm
gonna
click on share to teams
this is the new feature that we have uh
where i can just go ahead and select the
team channel and see the link for the
entity that i want to share but now we
can also see the preview of that entity
before actually sharing it and you can
see that you have the
reward id for
the customer in the customer card itself
so let me go up and actually type the
message to ask help from the team
so i'm gonna just say
hey
we have a case for below customer
[Music]
can someone help
and i'm gonna just go ahead and click
share on it
so now
we have shared the entity let's just go
ahead and go to teams and see what
happened so we are in teams now we can
clearly see the entity has been shared
i'll just go ahead and click on details
uh
to see how the entity look in teams with
the almost full screen experience this
is what we call a stage view layout and
it's also another feature that is
currently available on in all the
business central production environments
i'll just now go ahead and pin the
entity so that i can bring my entire
team on the common view so they know
that we have a support case to work on
this is a feature that's going to come
soon in upcoming business central
versions
so we have tabbed the pin and i'm
expecting now
our expert evgeny who can analyze what's
the issue with this report
thank you monica
okay so back to teams saw a message from
monica i'm just going to reply that yes
i'm on it so she feels
she feels good about it
and how do you start an analysis well in
my case i'll start with the data i have
a go to the customer sales list report
i'll just preview it and see quickly if
that report have enough data
where i can make my analysis
and that looks okay it had a customers
sales
and so on so forth
what i'm going to do now i'm going to
send it to excel
excel document data only because i want
to work on a data set which empowers
that report and when the report is
loaded and excel file is opened
which usually takes
a couple of clicks now i have a data so
i can probably you know take it make
after refill
select couple of records
every analysis will start with a pivot
table these days so i can go to
insert like a recommended pivot table
start with some default suggestion
so i have like a geography and a sale
sum of sales i can also bring the
customers and obviously i can use maybe
insert some more advanced utilizations
to pitch my point that yes that customer
maybe deserves
uh to be promoted to the next level
now i obviously can build very extended
visualization to support my case and
let's say i just did that
so to save a time you prepare a file
which have exactly the same data set or
a simple one and then you can build much
more advanced visuals for me as a user
to complete my tasks so i have advanced
filtering and i can you know look on the
sales data from different angles
now i want to go to business central go
back to my report and that's a new
feature come in this release that i can
go ahead and write my schedule report i
can choose a layout i want to use
primary port or create a new one
so i'll press a new button
give a new name and for my layout like
customer sales list better you can do
better
you press a button
you select a layout or file we just
created
and
obviously
in real life he'll probably schedule
your report so i can send it to my
report inbox
and now business central will process
bc data
based on the layouts we just created
okay
so at some point of time
if i go back to my reporting box i can
open the document in a onedrive
see the final results
open first and then to see a final
results
and this way also maybe invite more of
my colleagues on collaboration the hey
here is my data set come from business
central and all my visualizations
obviously are now live
so i can conclude my task and say yes
this customer has to be upgraded to them
to the gold level
so that was a scenario where i run a
report and make some analysis using
excel layouts to get some conclusions
but sometimes you don't have that or
maybe you don't necessarily have
the data same sample you start with
so let's see what else can you do
sometimes you start with a you know data
you have on a screen so in this case i
just go on a list and open my list in
excel basically getting the same columns
to my excel file which i see in a screen
just one click away from me
okay
i can again
after how to fit all the
columns and let's just select couple of
columns for now like maybe
number name
balance and sales
because i want to analyze again this
data
will just copy them to another tab
pass it here
format
as a table
it's just kind of very natural step for
me to do
okay i'm going to use a feature which my
organization powered me in excel
i'm going to data
and select the organizational type which
allow me to bring
live data from business center write to
my excel file
so i'm going to
click organizational type and selected
columns
and excel will bring a live data from
business central right
to me and if i'll move it a little bit
here
so it's happening we're able to
recognize that 10 000 is a customer
number bring data from erp back to my
screen i can scroll a bit okay i can
maybe bring rewards
id's on the screen so i can clearly see
that yes that customer is silver high
sales let's put them to more i can bring
more data maybe like a geography
to continue doing my analysis
so
just another way for me to conclude the
same task and now again i'm in excel and
onedrive
i can maybe
leave a comment to my colleague monica
hey
you know all good here's a document here
is like data to
conclude we need to upgrade a customer
to the next level
uh please take a look if you agree with
that or not
i can go ahead and create a task which
is super easy and convenient for me
right from excel
and obviously because in a onedrive i
can go ahead and share the document with
my colleagues
and she'll be notified and you can
continue from here
so i just got a notification on outlook
let's see what's that about
so um i can see that if guinea has sent
me a task
let me go to the comment
and he says oh please upgrade the
customer to reward level gold so good we
did the analysis and the data looks good
so let me just go to teams and click on
i can either update the level from
details or from tab so i'm going to
click on tab
and then update the level
let me go to the edit mode and i'm going
to change from silver to gold
and that's how easy it was
because now we all know we are working
on this entity so i can just use the tab
option
so let me also go to excel and mark the
task as completed that was assigned to
me
and i'm gonna follow back on the chat we
were having so i'm gonna say um thank
you i have
updated the reward level
and also i want to say to sam that
please make sure that the customer gets
the new welcome level for gold
so
he should send the welcome letter over
to you sam
alright thanks monica
yes so i go over to teams and i see i've
received
a
notification from monica um so i'll go
ahead and give it a like so i'll start
working on
um so i can use the details action here
to open up business central and then i
can double check what the reward level
what the latest reward level of this
customer is so i can see it's gold and
then from here i can peek and then go to
the gold record and we have some
attachments in the document attachment
fact box here
which includes the kind of welcome
brochure we have to the the gold reward
level
so i'll go ahead and click share and
what this will do is take this document
in the attached documents factbox and
upload it to my onedrive and then
present me with the common share
dialogue that you're probably familiar
with from other microsoft 365 products
and then from there once that pops up
i can go ahead and click outlook and
that will
open up the compose
editor in outlook
and i can go ahead and let robert towns
who's the contact for this customer
know that they've reached the gold
reward level and write some kind of
quick
introduction
email so i'll say like welcome to the
gold reward
level
and i'll i'll try and type quickly
so hi uh we would like to and you know
you get all the autocomplete suggestions
and stuff uh from outlook it's like just
the full editor
and then
just say that they can see the uh
the document here
now i'll just
quickly sign this off
and hit send
yes so now that's been sent to um to
robert and i've kind of let them know
that they're part of the gold rewards
tier so i can now close the stage view
as well and then reply to monika back in
teams that i've kind of updated
everything
so
that's kind of the task done
um so i'll go ahead
and uh yeah so this is kind of the whole
collaboration scenario we've been trying
to demonstrate here and i'll hand over
now to monica who can hopefully tell us
a bit more about the collaboration in
teams specifically and how we can adapt
these uh extend these adaptive cards
sorry thanks sam let's take a pause over
here so what did we see we saw a lot of
experience across multiple uh microsoft
365 apps but what are we going to talk
about now we're going to talk about that
how you as an al developer can create
and extend these
experiences
so let's start with developer
extensibility for a teams card
you as an al developer can extend
adaptive cards for both existing
entities but also your custom entities
you as an air developer has a full
control on what will be the final fields
that will be shown on a team's car how
can you do that you can do that by using
by having two options first option is
using brick field metadata group
and second option is using al events
let's just switch to first options demo
how are we going to use brick field
group for custom and base entities i'm
going to switch the screen
and
here you have seen this before
we have the reward table as we are
working for a company that provides
rewards to the loyal customers
and i want to bring
the reward custom entity into teams
how do i do that i just go to the source
table and go to field groups and quickly
just add the brick field group a big
brick field group is the group that
basically has a set of fields that
specify the record and can
can summarize and identify the record in
a glance so choose the fields
accordingly
we also suggest to use the second field
in the group something like name or
description because this is the same
field
that is
projected as bored in web and mobile
client so now brickfield will also be
used to project the second field in
bold in teams
so we get a consistent experience across
all business central clients
and
let me just go ahead and publish this
extension
i can just
publish
and while this is publishing
we can just uh
go to teams
and see in business central client if
the extension is published
yep looks good
okay
let it load
so we can just go to the same
sorry we can just search for rewards
because this is what we
added the brick field group to
i can just go to a gold level reward
and let's copy the link for it go to
teams just start a new conversation
and paste the link here to see the
preview of that card
and you can see that it was so easy to
bring your custom entity into teams card
just padding the brick view group but
this was about the custom entity how can
we extend the existing entity so we
already saw that the customer
card can be extended to have the reward
id in the initial demo so i'm just
quickly going to show how to do that so
we have a table extension for customer
here
and
in the field groups instead of just
adding the brick you actually add
addlast to the existing brink that is
defined in base app
and you can add the fields that you want
we only added reward id but you can just
choose any fields that you want
so that was the demo for
extending using brick field group
it's come on
let's see the second option extending
using al events uh business central
offers three different al events uh so
that you can choose
full control of fields on the car on the
team's car
you can read about this in the
documentation as well without going into
details i just want to mention that
these events are part of the system
application in the page summary provider
module and i'm gonna just demo one of
them let's choose on after get summary
fields
so
[Music]
um
we are gonna this is the base card that
we have without any customization or
extensions so it has name number balance
and many details and let's go to the
visual studio code to see how we can
extend on after get summary fields it
provides page id record id and field
list as the parameters
fields is the one where you can add and
remove fields and the order that you add
and remove fields in this will be the
same order that the fields will be
presented in the teams card
so we can use the page id to select
which card we want to customize in this
case we'll just use customer card and
then we remove balance details add
reward id and add city phone number and
publish
so now that it's being published
we can just go to the customer record
and copy the link again to see how the
card looks
so
let's go to teams
i will click a new conversation
and here is the modified card
let me paste the link
now you can see
immediately that in the preview the
balance fields are removed the reward id
is added and all the fields that we were
interested in are added so this was just
one example but you can just use other
events according to your need to extend
the existing entities
so let's summarize
what did we see for teams today we saw
that pin a t pin pin a tab in teams is
coming soon
you as an al developer had full control
in the final fields of teams card and in
most cases metadata is enough actually
we do recommend you to use brickfield
group
for consistent experience across all
business central clients and any
external data that you want to bring to
teams can be just brought easily by
custom entities
uh all these features are available only
for business central online so we
suggest developer testing in sandbox uh
and not in docker
and as an partner or as an admin if you
want to just get started on teams we
suggest to use the centralized
deployment so that all of your users can
get the app by default and as a
developer if you want to know more you
can refer to the documentation here
so now we learned about how to do
extension on teams
switching over to evgeny to learn about
how to do excel excel creations
how many of you tried excel layouts
really
james have you seen how many hands we
had
no okay so excel layouts is awesome it's
really like a great feature very easy to
build you export a data set you bring it
back to the product with the powerful
utilization
like just go ahead and use it
when you run a report we give you a new
feature you can go ahead and change the
layout on a fly so you need to go
somewhere and pretty you know predefined
which is default you can just change it
as you go
and it's just just easy to use as a
developer
you can go ahead and bring your layouts
together with your reports
you can also go ahead and define that
excel will be your default layout for
all reports going forward uh
just you know easier better easy to
build easy to maintain looks beautiful
like all the benefits you get from that
we have a number of samples as vincent
advertised today on our github
github.com microsoft bc tech you can go
ahead and download and see how it works
and i have a number of excellent
community blog posts on this topic so
just you know bring it to google it
and learn how to use excel
layouts
now
let's talk about organizational type
i don't know if you pay attention but
it's like a magical feature i'm in excel
i'm working with the data and i can
build bring the data from my erp backend
and i'm not even know where it's coming
from it goes against level of
abstraction from apis i can enrich my
reports take a decision and it just
works
as a developer you need to build custom
apis which provide your data everything
starts with the data obviously
i'm going to show you quickly how you
can leverage power bi to bring this
excel experience
it's really really straightforward you
can share organizational types with your
organization and it's easy to get
started
if you're in a power bi desktop you want
to
get the data for api you want to connect
to our online service
we're online service it's like business
central and while you're connecting
we'll try to detect all the api
available endpoints and we'll go for our
demo sandbox and we'll retrieve
api build to get sales rewards data
which you just seen i was using a couple
of minutes ago
okay i have nothing special like a sales
cost no number sales number like a
customer data
we're going to load the data with power
bi
not so many records
you can see a schema
where is it forward to you and the data
set how it looks like
now
you need to go ahead now and put the
switch feature table mark this table as
a feature table and when you do it
that's where the magic happens so you
say i want to mark this table as a sales
data with rewards i want to provide a
label
let's say customer number i'm going to
provide the primary key column so excel
know how to resolve
an entity by that value when you save it
just go ahead and publish your power bi
report to your organization
and we recommend you use organization
you use like a
yeah teams workspaces meaning we can you
know i can invite monica and sam and
collaborate with them
so when you publish your report and your
table
you go back to power bi online
which has nothing but when you refresh
or when we refresh
you'll be able to see that those assets
get published and once it's done we can
start to use them
for real
all right so when you have it deployed
we can just
start our excel story
refresh excel file
go to data
and our organizational type becomes
instantly available for those users
so you can see we have organizational
type called customer rewards data and
now if you have a value like 10 000
which mean nothing for any decent human
being but we know that it's a customer
number so you can press a button create
a type
and bring all the advanced information
from erp right to your reporting and
again i don't even need to know where
it's coming from i can go ahead and
start my
reporting job right from here bring my
column and so on so forth
this is a pretty cool compatible
advantages i don't know if other
products can do it
but
yeah
really awesome
a short summary
how many of you tried to use
organizational data types with excel
before
okay uh please spend time to learn about
that as this is a feature powered by
power bi
it's required to have power bi pro
license because power bi will maintain a
layer
which will hold your data so excel talk
to power bi power bi will talk you know
periodically to business central you're
not going to put a lot of queries to a
back-end super powerful feature great
for pre-sales great for developers great
for all of us it will work with excel
on-premises and excel in the cloud
so because many people use just excel on
their box and this will just work great
with that
finally you have seen all the demos 3d
today work with the files which is
stored in onedrive when i open file link
excel edit and excel uh look on the
reports they went all the way into the
onedrive
and with that we'll ask them to tell us
how it's possible and how is a developer
and can build solution to work with a
onedrive
yep sounds good thanks
um so yes uh we've brought the share
experience to business central and it
should be the same experience they're
used to in all the other like m365
products
uh but something kind of a bit different
that business central does is it takes
the file
from business central and it will upload
it to your onedrive for business
before showing the share options or
opening the document in the onedrive
preview
from the share menu itself you're then
able to like email a link like we did in
the demo or copy a link or if it's
already been shared you can actually
just adjust the link settings from
inside business central
and we've tried to organize how we
upload these documents a little bit so
it will be written into a business
central folder inside your onedrive and
then we'll also split split it based on
your company name so it's a yeah a
little bit organized
but i'm sure you all know how share
works so i will dive more into the
developer experience so how can you
extend your scenarios with
the share and open actions
so i've built my own extension on top of
the rewards extension
which adds my own open and share actions
because actually with these welcome
packs quite often i want to share
multiple documents and in the attachment
um
box
we can only share one document at a time
so what my extension does is adds a new
page and it will zip up all the files
together and then um with one click i
can kind of share or open them in
onedrive and share it with the contact
um so i won't go into the details of how
i do all the zipping and stuff but
i wanted to point out kind of the
actions we have so we have like the open
in onedrive action and the share with
onedrive action and they both have these
captions and tool tips and images that
we try to keep consistent throughout the
product so if you're adding your own
please use these same properties
we also have this visible property
and that should be set to a helper that
we have in a system app that will
make sure we hide the actions if
onedrive integration has been disabled
or if it's been enabled then obviously
it should be visible
and finally in the trigger um we have
this yeah document sharing code unit in
system application and then there's the
share method that takes essentially the
file name you want to pass in
um the file extension
and then
the stream of data that you would like
to share
and then there's this intent enum that
kind of says whether or not you want it
to open or share there's actually a
third one as well which is prompt so
that will give like a little string menu
to the end user to decide what they want
to do
so i can go ahead and hit publish
and then
hopefully the wi-fi is good
so i'll just
upload this extension
yes
so i'll pop over to business central and
go over to the rewards list
and over here now you see this open
welcome pack action that opens this new
page i can go over to gold
click open and i put some like
information just to make it a bit easier
but then i can go ahead and click open
that will then
zip up all these files for me start the
upload process to onedrive and then once
that's completed
it will
invoke the
preview one drive preview
any design yes good
so yes here you see the previewer knows
how to kind of deal with zip files so i
can see the contents inside the zip and
that's all the attachments
so that's nice
we have a few design considerations we'd
like you all to be aware of
when implementing these for your own
features
um so we have this like share open
download concept that we've brought
everywhere in the base application uh so
if you're also extending your download
scenarios it'd be cool to keep download
as well uh just so like you know end
users have all the options
and we recommend looking in base app as
well for how we've implemented these
actions and then you can just copy paste
because the boilerplate's essentially
the same
and yeah pretty much any data stream can
be uploaded
it just depends on the file type and
whether the onedrive previewer will
handle it so most open formats will
support but if it's like some
proprietary ones it may struggle a
little bit
and the next question you may have is
how do you administrate this feature
so we've added a new onedrive setup
wizard for this release
uh this allows admins to manage the file
handling
within business central
and it applies across the whole
environment so it is cross company
and essentially you get two toggles
one is for app features and one is for
system features
app features are effectively these open
share actions that are invoked through
al and you can think of the system
features as more platform-based ones so
like opening excel in excel and all the
reporting
the setup itself is managed by
permissions so you can gate who can
change these features quite easily and
if you anyone here has been using the
legacy sharepoint onedrive stuff
um there'll be a little migration step
as well that will show you what may or
may not be changing when running this
setup
then on the other side sharepoint also
has an admin center and this will allow
you to manage how the file sharing is
managed across all of m365
as well as business central and it lets
you set policies on whether or not you
know you can share your files outside
your organization or how long links can
be valid for
and like bunch of other stuff
and um yeah this policy is just shared
across the entire tenant
so in summary i would love you all to
extend your um download scenarios with
these open and share actions
and also to run the
onedrive wizard
on your environment so that you get the
latest and greatest integrations um so
like the main one i think is edit in
excel in this wave will work with
onedrive
so i hope you all found that useful
hopefully this enables you to increase
your collaboration with other tools with
the business central and you can take
this all to your ip as well
thank you
yeah
you got any questions
long day
yeah you can just shout out your
question no problem
yeah the question was you can control
where the file goes directory the
program programmatically or dynamically
at the moment not really um so they will
go into this company directory
but in the path you pass in i guess you
could add a child directory as well
and then it will just get put under
there
can you show some how to get to the
folder from business central and how
it's stored maybe yeah so we have a few
ways actually um
so we have one in in my settings uh we
have this cloud storage uh
label now so you can click click this
sorry
oh
all right well i can go back maybe i
don't know i don't have control
it's good yes so yeah i go to my
settings and then here um you can see
your cloud storage kind of thing uh so
you click this and then it will kind of
also discover how
like if you have your business central
folder and your company folder and then
it will drop everything in and you can
see this is the
welcome pack i just uh
uploaded
and obviously you can also go through
the waffle in the top left but that will
just take you to the root directory
so whatever is whatever way you prefer
any other questions
it's hard to see
yeah
i can take this question so the question
was i have approvals in business central
you can obviously send it to teams but
how would the people person approve any
teams does that go to business central
press a button is that the question
yeah it's
yeah so actually if we go to business
central maybe we can also damage right
now i'm gonna take it
uh if you go to power so the short
answer you can
in business central we have out of box
67 available approval templates and it
deploys this template as a flow we
create has the different steps and we're
going to use microsoft teams approval
app which allowed to notify the user
have an approval and you can take an
action from teams like approve or
decline
and then we'll call
uh it'll call on the back end our web
services to confirm or deny approval so
you can do it today
one more time you can create approval
flow go to teams go to your phone you
press the button on your phone it's get
approval business central
and that you can do it right now we also
have a number of plans to improve the
story in the future like for next
release to make it better obviously in
business central you don't have a like
maybe ux pattern that is an approval you
don't get notified as a user necessarily
that your order was approved and so on
and so forth but the basic scenario
described is possible right now with
business central and to show you that
if you just go to
power automate
maybe same you can type with your
credentials
on your keyboard
we can show it quickly yeah no i haven't
used it on this user but we can try just
sign in
so i hope it's time with you i just want
to show you how it's how is how it's
done
okay so we don't really have anything
yeah
okay
actually we have a session tomorrow
about power automates improvements and
we can also show you the demo of the
session our colleagues can do it so
please come by it's an awesome question
i think it's 9 a.m tomorrow
good time
i just want to add that just from the
team's card perspective the only control
l developer has us on the list of fields
not actually on the actions
uh so uh
power power platform is the uh answer to
your question
yeah you can figure that
yes sir
so if they can get the question i'll rip
the question so the question is
is essentially does it work with outlook
desktop
yes so um
yeah
let me just quickly
share some other document
um
so yeah this has put the file on
onedrive
and uh yeah so there's this action here
and that action will always open the
outlook web app
um but you can also just enter contacts
from like here so for example i can type
moniker
and this will then if i click send that
will also send an email directly or you
can of course just copy a link and then
go to outlook desktop but we don't
there's no like one click to outlook
desktop
yeah
sorry
teams desktop yeah that all works right
yeah
but i guess that's fair to say that all
the integration try to build the work in
the cloud that's where we try to deliver
value and from there we try to drive
on-premises if we can but sometimes you
have technology limitations which it's
just hard for us to address yeah like
also like the demo is into the arena
where you can take a file send to ii
builder get pdf convert to real document
those assets work in the cloud
more questions
i don't see any
great thank you for your time we have
five minutes for our next presenters
[Applause]
