# NAV TechDays 2015:  NAV 2016 - Phone client  Webclient enhancements  Windows 10

- **Source:** https://www.youtube.com/watch?v=ZzXwA0bHDYQ
- **Video ID:** ZzXwA0bHDYQ
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 95m24s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

so uh Welcome to our
session um we hope you had some coffee
this morning and you're ready to listen
to our session well not me you know I'm
Italian but it's like coffee totally I'm
just I honestly don't know how he
manages but okay so should we introduce
ourselves let is first yes my name is
Hina I am the engineering lead of the
nav client team and my name is Andrea
I'm a software developer also in the en
client team yes so um it has been a very
busy year for us and uh we have a lot of
cool things to show you today uh
actually When I Was preparing for this
session I went through the questions and
the feedback we have gotten last year in
this forum at NAC Days 2014 and I was
very proud to see that we have addressed
all uh all these requests not all but
some most of them uh so we really hope
you're going going to enjoy our session
um but before we go into today's agenda
uh we will start with a little quiz
because we have some T-shirts to give
away let's see let's see yeah so uh who
can guess uh the uh total number of
unique downloads of uh our tablet app I
know he knows but uh is there anybody
who
volunteers um is between 20,000 and
40,000 pretty close but a bit
less okay 30,500 I think you but I guess
it deserves one because you were the
closest who was
it
congratulations okay so um yeah let's go
through to today's
agenda so we will start with uh what's
new in uh uh Dynamics nav 2016
clients after that we will give you a
tour of our brand new NV Universal
app um then it is time for a roller
coaster tour uh of the enhancements we
have done for the desktop web client and
um last but not least we will um uh go
walk you through some of the
considerations you need to make when
you're implementing Your solution for
the universal app so by the end of this
session we hope you will walk away with
a general understanding of the NV
Universal app a good overview of uh the
enhancements for the desktop web client
and um we will also try to demystify the
process of um implementing and
customizing your solution to to run
across
devices so with that let's uh go into
what's new let's start yeah so what's
new well you know a year ago we have
released Dynamics nv4 tablet um which is
an app for your iPad for your uh Android
tablet or for your Windows tablet uh
actually how many of you are using our
tablet
app okay I see some hands that that's
good so um in in this release we have um
uh introduce the next evolutionary step
of this app bringing Dynamics NV to to a
broader uh set of devices so the
Dynamics nav Universal app runs today on
your smartphone on your tablet and even
on your desktop
PCS so um unlike the web client and the
windows client which are in designed for
mouse and keyboard interaction the N
Universal app knows how to adapt to the
screen size of your device and also to
the input method of your device mean
being touch or mouse and
keyboard so of course the first question
in your mind probably is where do I get
the app from uh and it is uh available
on all stores uh it is available on uh
on the Google Play on the iOS store on
the Windows
store um so then of course what about
backward
compatibility so um the if you'll be
using the our tablet app version one one
uh you will get automatically updated to
version two and you can still continue
to connect to the nav server
2015 if the server has been upgraded to
version 2016 then you need to have the
version two of the app uh and also for
the users of the app on desktop and uh
on um smartphones then they will also
use uh NV server
2016 and uh one more thing we would like
to say about the NF Universal app is
that it also use makes use of uh uh
device capabilities so you can uh
develop uh application scenarios that uh
use camera on location Isn't that cool
it's very
cool yeah but how uh how did it all
start it with with the NV Universal app
um so in NV we really love Windows 10 so
we got uh inspired by uh by Terry
Myerson words about Windows 10 we're not
talking about one user interface to rule
them all but we're talking about uh what
Pro product family with a tailored
experience for each device and this is
what we have done as well with uh nav
2016 we have built a product that
delivers the right experience on the
right device at the right time as a
result the Dynamics na user interface is
in intentionally different across
devices and uh the message we want to
convey with the universal app is that
nav flexes and enables uh our customers
to perform their daily tasks uh anywhere
basically whether they are at the office
whether they are outside the office or
on the go just holding a tablet or a
smartphone in their
hands so um how does it all come
together right how how how do you get
the universal up right to build so of
course it all starts as usual with uh
you defining your your pages and uh your
data
model after that uh you can Define the
profiles the RO tailoring basically and
the
configuration uh then the user
personalization and after that the NV
platform takes over and it uses a set of
layout
Builders which are not customizable uh
and these layout Builders they are
basically rendering the controls on the
screen so um the layout Builders take a
lot of decisions based on the screen
size of your device on the type of
device on the page type and so
on um and if we look at uh at these
three user interfaces the tablet
interface the phone phone interface and
the desktop interface we can say one
thing they are same but they're
different so they are same because the
nav clients are built on the same
framework but they are different because
the user interface is intentionally
different so um with that maybe we
should try to go into demos and let's
hope yeah it's going I think you can
start showing them the real thing so
let start the um let's switch and see if
we can do
that no don't
start should be
fine cuz you're standing oh
okay it here awesome yeah let's make it
full screen yeah I will
try all right okay so you probably
already saw this in the previous
sessions but so what do you have there
actually oh yeah you're right so this is
first of all my Windows phone and it's
running Windows 8.1 here I have my
Universal app installed and I just
started it and this is the r Center it
looks like you probably saw this already
but in this session we are going to go a
little bit more into details on this so
we start here we have our tiles we have
our familiar experience we with the RO
Center our activities and uh we can get
a general overview of our business but
we have the RO Center what about our
parts so since we are on a phone it's
well we have less space and a bit lack
of real estate so we have to play a
little with this so your parts now are
showing us tabs so just by using the tip
of your finger finger swipe left and
right in order to access the different
parts here I am in the navigation
menu then again on my
tiles moving forth to my
chart again my favorite customers trial
balance report inbox usual experience
and well it's very Snappy and smooth
experience on the phone and here we have
an addin so Vincent yesterday already me
mentioned that in order not to break
this extremely cool swiping experience
we should not let your adience uh
interact with you otherwise you will not
be able to swap as easily as I'm doing
so if you want to interact with or Adin
just tap on it and you will be brought
inside your Adin in Zoom mode and there
you can start interacting with your Adin
and the nice thing is that this is your
JavaScript Adin
there is nothing new there is nothing
you need to do to have your addings run
in a phone client they just work fine
exactly as in tablet and in your web
client so have my head in Arena I guess
I will I will start drilling down so let
me click on one cor area and get to the
customer
page perfect and here's the customer
page how it looks like on my phone and
I'm in edit at the moment just because I
was drilling down from the chart so let
me use the edit view toggle button on
the app bar you can see the blue bar
just at the bottom and I'm brought to
view mode and did you see something
changing yeah we are brought to a
different display mode we have a two
column layout so like this you have a
broader view of your information these
cards can get pretty crowded we know
that so that's why we restructure the
layout accordingly
so again tip of your finger scroll
down scroll up and you can get access to
the different parts of your
page and uh the experience is very
smooth because the type of interaction
we have is is such so let me go back to
edit
mode and uh let me just edit the contact
name for this C customer so I want to
put myself on it Andrea you want to be
the contact person for this customer
yeah I want to experience this thing so
I I easily edited the contact name for
this customer and now I'm ready to to go
back so notice that the Windows phone
has a physical back button so I press it
uh I tap on it in order to dismiss the
keyboard and then back again to go back
to uh where I was before my adding by
the way the value was
saved I'm back to my ading which is
still in Zoom mode so I'm still able to
interact with it but I want to get back
to R
Center back again using always my
physical back button and swipe back and
I'm back to my tiles back to your Arena
okay so let's switch to my
phone see if it all works yep so uh here
I have an iPhone 6 so um what we would
like to show you now is that uh the uh
phone client has the same look and feel
across all platforms so notice that on R
Center you see the same UI concept that
Andrea just
showed uh but now I would like to have
an overview of my
customers so I'm just going to navigate
to the customer list so uh in the in the
phone client we have completely
redesigned the list in order to optimize
for the uh available space and the
readability of the data so we are you
for rendering data in the grid we are
using A New Concept called The Brick
View and I will uh talk a little bit
more in detail later about the brick
view concept uh another thing to notice
is that we have added continue scrolling
on the list so notice how smoothly I can
Traverse now to the record loading data
on the
command at the bottom of the screen we
have uh we have the app bar just as you
saw it on the Windows phone uh but
because the iPhone does not have a
physical back button we have um added a
software back button uh and that is used
for navigating between action Pane and
pages and also between Pages if you
would open customer card you can
navigate back to customer list and so
on another thing to you uh see in on the
Upp part is the magnifier glass uh here
we have um uh that this magnify glass
indicates the Pres presence of the
search so you can actually search
through the records in your lists uh so
let's stop on that and the search text
box appears so uh let's see if I can
find the customer that Andra just
modified because we are actually
connected to the same server and um You
probably noticed that this is a cross
column search since he has added edited
the contact name and not one of the
primary
keys so let's view this
customer so by default in uh in Leist
when you navigate from Leist to cards
the cards will get open in in View mode
um notice the same y components on the
card just as Andrea showed them but what
I would like to do now I would like to
uh create a sales invoice for my
customer so let's go to the sales
invoice so notice how of CAS right now
we have the customer information prefill
so all I need to do is uh I just want to
add a line so I'm going to uh tap on the
plus so unlike the uh desktop web client
and the tablet client where the editing
in the grid was done in line uh in the
phone client and we have autogenerated
an editing card uh and that is done
because we want because of the lack of
realate uh on the on the phone right so
um this card is generated based on the
same metadata as the lines uh grid so
there is no C intervention you need to
kind of set turn this on turn it on and
the editing uh you can do it just as you
would be doing it in line
so I will show you that I
can type a
th in the item number and then I'm going
to quantity
one and now uh you can see the NV
business lodging in action also on the
phone because I I I shouldn't probably
uh create the sales invoice so I will
press yes and there it is my my line is
uh complete so I can uh go back now um
to to the S form and notice that now we
are taken back to a to a autogenerated
list place for the
lines um we it is sort of a zoom in
functionality similar with the one we
have added for the for the charts uh in
order to cater for the lake of real
estate um so basically in this uh lines
list place which is built on the same
data as a sub form uh you can uh you can
um do your you know you can operate with
the with the line sub form so you can uh
open the action Pane and invoke the
actions that are associated to the page
uh you can create lines or delete lines
or or edit
lines and then when we navigate back uh
we are taken to to the sales
invoice so that's it I am done with
creating the sales
invoice so um one uh one scenario I
would like to show now is uh on the
phone is how quickly you can uh we can
use the S Excel
functionality so uh if you go to the U
open in
Excel and then
we start up the
Exel here it is we have the the list of
our customers and the data is filtered
because I um search for particularly the
customer that Andrea created uh
modified and yeah you can do anything
you want with this file you can save it
on your uh device or or send it as an
attachment and so on and now I will be
navigating back to to the customer
list so that uh brings me to to our U
last demo on the
phone um which is a scenario you have uh
seen before actually I think probably in
also in keynote and also in maybe a
workflow session for the guys for those
of you who attended that uh so uh
basically the scenario is I am holding a
receipt in my hand and I am taking a
picture of the receipt and then I am
sending that picture to nav and na will
uh create an incoming document which
will have this uh uh picture
attached um so let let's see how this
works so Andrea agreed to be my receipt
for today I think I can be touch go for
it and say use
Photo uploading it yes and now um the
number
of incoming documents should uh
increase and let's uh just to show you
that is the same picture to believe us
I don't know if you see this before but
okay we love this scenario
so yeah you know iPhone is a bit slow oh
yeah I don't think it's the iPhone
actually but okay the
network probably probably I think yeah
okay so let's uh if I try to search the
I see you have the same picture I have
taken nice pretty cool
okay so so that uh that concludes our
demos on the phone uh and uh just to say
uh some takeaways from from the phone
client as I said the uh look and feel
for the client for the phone client is
uh uh the same across all platforms and
we have done that in order to uh keep
the uh familiarity uh across different
Dev different devices when when you are
uh using the phone cloud client and also
we have designed the phone client uh uh
for uh the end users that want to
perform their daily tasks on the go so
some most of the um you know most of
most of our UI is reacting to to
gestures and it is designed for you
holding the uh phone in in the hand
right y so we have one more device to
show you today let's see if Andrea can
bring it up yeah I'll try not to
disconect otherwise going to be a mess
so here we have uh our surface tree
running Windows 10 you can probably
recognize the operating system from the
picture just behind me and uh of course
we have uh our Universal app installed
on it so I think I'll just bring it up
Arina ready let's see if I can succeed
in this yeah hey
Cortana start Dynamics nav
yes the funny thing about this that it
always shows a different search string
so people think ah it's not going to
work but it does so uh oh yes it's
working now let's wait for it to connect
yeah so if the network allows it we
should be brought to our Ro Center in
our tablet app and by the way was it
just last year we released it yes that
is true so this is our Universal app and
uh on the tablet right now and what we
would like to uh we would like to show
you now is the na Universal app knows
how to adapt to the mode of your device
so it can easily switch between the
tablet mode to the desktop mode just as
the surface can switch between tablet
and a into a fully functional PC so we
are taching the keyboard now and na
reacts to this mode change and when you
press yes then it will switch to desktop
mode so the same app it is now optimized
for mouse and keyboard interaction for
precision clicking and it makes the
users feel comfortable performing their
tasks uh on the
desktops but uh how do you think that
was possible to do this desktop mode
well uh this year we introduced a lot of
enhancements and we worked hard on the
web client as well yeah so actually we
have uh uh done a lot of enhancement to
our desktop web CLI uh around 65
actually um so but and that is going to
bring us to the next next step on our
journey today uh but before we uh we
move to that uh let's uh wrap up the
universal app so um basically why do we
call it Universal because it tailor
three experiences in in one up and
because it also adapts your experience
uh to your to your uh activity to your
display to your device to the mode of
your device and the input of the device
be it touch or mouse and keyboard so
with that let's uh talk about the web
plant
enhancement right yep okay so um in uh
NV
2016 we have started our journey of
redesigning the web client so it becomes
a first class desktop experience client
and what does it mean a first class
desktop experience client it means for
us uh three key words uh Simplicity
productivity and performance so one of
our main goals has been to deliver a
simple user interface uh which is uh for
both for all users actually be it new
users or Advanced
users and uh we have also invested in
productivity improvements for the users
that um operates with a large data set
um so for example navigation scrolling
uh freeze pain are just some of the
examples of that we have for features
that improve
productivity and uh performance yes has
been definitely a focus area for us
uh we have improved the startup time of
the web client and we have also um I
think V vincon actually mentioned in the
in the key notes about us moving to a
single page
architecture um so um so that helped us
a lot with delivering a lot snappier
UI yes so the message we want to to give
here about the web CLI is that with all
this 65 enhancements we have done this
year we believe that all users all your
user roles operating on desktop will
have a great experience using web lant
and it is a lot easier for you as a
partner to um deliver a similar
experience to our Windows client
users right so with that let's uh start
showing the
enhancements yeah
so let's we need to get out of the and
then start the desktop app right
absolutely try
to this one yeah uh we are extending yes
let's switch back to yeah one screen
yeah I guess it's better so allow us
just a little trick so we can mirror our
display yeah I want to keep this
changes perfect I don't need you
anymore and
uh let's
go to our
Universal let's wait just a bit yes okay
or you're good to go okay so our first
enhancement I'm going to so first of all
of course we don't have time to show all
the 65 enhancements we have done uh we
have just Cherry Picked some of them um
so um I think we will probably show some
10 enhancement instead of 65 but okay so
um the first enhancement is about uh
simpler deployment um as you have
probably noticed from the previous
releases we have always um uh kept a
strong resemblance to the office product
in order to make our users feel
comfortable when they are working across
uh web client and Office 365 uh in the
browser so inspired by the office family
we have uh introduced in na a Brand New
Concept uh called my
settings so what is my settings my
settings is um place where the users can
make personal choices about systemwide
parameters and the first uh one that um
comes to our eyes even though not on the
top is the change company so the users
can now see the least of available
companies and they can choose which
company they would like to work
on and uh this is a feature that existed
for a very very long time in Windows
client and we have gotten a lot of
requests of having it in web client and
here here it is um we have
also um added uh language or the ability
to change language for example and you
can also adjust uh
your time zone and you can also adjust
the work
date and um basically this this feature
my settings is available also on tablet
uh client and on phone client which
means that these settings are actually
portable across
devices and um also what's even more
cool about my settings is that is fully
customizable because U it is implemented
as an application page so any partner
can add their own per uh systemwide
parameters that the users can choose to
personalize
later and this is how we achieved a
simpler deployment for web CLI because
the administrators do not need right now
to install multiple web server instances
for multi language support or for
multiple companies now the users can
self-sufficiently choose uh these
settings while they are connected to
only one web server
instance okay uh so that was the first
that we wanted to show and now we have
uh some enhancements we want to show for
the lists so let's navigate to uh the
item
list so one um one enhancement is about
responsiveness in lists so in 2016 the
lists Al for the desktop web client they
also have undergone some significant
redesign um in order to address the core
usability issues we had uh meaning you
know you couldn't see all the data uh
you had to you had two buttons page up
page down and see only 20 rows at a time
so now we have um uh added continue
scrolling notice how uh fast and fluid
mostly I Travers through through the
records and if I can and draw your
attention to the um bottom of the screen
you will see fing more rows which means
that data is uh loaded on demand in
order to keep the list uh being
performant so we're not preloading all
the roads and then just having a scroll
bar we're actually loading data whilst
the user is
scrolling also uh the GDs have uh become
a little bit more
adaptive so um if you are showing the
web client on a wide screen then uh the
grid will stretch and take the space and
it will also uh load enough data so it
fills out the available space so you can
really make use of some of your brand
new wide screens so many announcements
on uh vertical scrolling but what can
you tell me about horizontal scrolling
Arena yes so horizontal scrolling has
also undergone uh significant redesign
in in the in the web CLI as you probably
know some uh the uh web client was not
uh interpreting the free pan column
property from the metadata but now it
does so when I uh scroll horizontally to
the right take a look how the leftmost
columns they stay in View and how
smoothly The Columns animate in and out
uh um making sure that you can always
have the full value in view so we uh so
we don't really kind of start not
showing the value one step at a
time and um this feature is as a bonus
uh it's also working in tablet clients
so
um we in tablet client we have taken
away the uh uh adaptive layout that we
had in uh in the last release where the
you could only see a certain number of
columns based on the uh screen size now
free span is available there as well and
we have added gesture to it so you can
actually scroll left and right by uh by
by doing
swiping and yeah so one more thing to
say about the free pan is that um in the
web client if the page does not have uh
free span column defined by default we
uh chose the First Column to be the free
pain column and uh it has this uh this
has a little bit of a drawback in the
sense that you cannot customize the free
span col like you would be doing in the
in the in the Rolla client in the
windows Cent sorry um but uh I mean it
is U we'll think about it to introduce
in the next
releases yes yeah so I guess now you can
talk a bit about our columns there is
something new yes so there's also
something new we have added so um the
ability to personalize which columns
you're actually seeing in the grid so we
have added in the context menu of the
columns we have added two
actions uh one is height column which
simply takes away uh the column from The
View and uh we have also add this choose
columns which basically shows you all
the possible columns and then you can uh
make your choices and uh uh after that
the grid will beautifully readjust to
the new column structure so um we notice
that here we have not rendered the page
and we have not reloaded it or refresh
it basically we have just uh uh change
the HTML structure to to fit the new
column so it is pretty uh implemented
pretty
efficiently and that gives us to our
last demo about the least right which is
the search right so notice that uh in
the list we have the magnifier uh glass
icon and while if I click on it then uh
the search text box uh animates in and
we can start typing and notice how
whilst we're typing the data is
filtered and this is also a cross column
search uh as you must have noticed
uh we can also pause and then refine our
search and we have we can also use the
um wild cards that you are familiar with
from the quick filter so you can uh use
uh um star for example or or yeah what
other sorry denish
keyboard
okay and as a bonus we could say that uh
this uh cross column search is actually
not available in Windows client so it's
only available in the web okay but uh
now uh Andrea is going to show you what
improvements we have done to the
cards yep so I would say away from the
Magic World of lists and let's go to the
Magic World Of Cards You' probably seen
these in some of the previous sessions
uh probably a
glimpse uh but in our cards now we have
uh fully functional fast tabs so so far
we have been having fast tabs fully
working on the Windows client there you
could do everything you could collapse
them expand them but the web client was
a bit stiff now we've brought this
experience in the web client as well so
we have fast tabs we did this because
it's very cool feature and allows you to
to group your fields and uh just focus
on what you're really interested in so
by of course by click on the caption on
a tab in the web client you can collapse
the tab by clicking again you can expand
it and uh of course as soon as the tab
is collapsed the summary section will
appear uh but before going there uh
please notice that uh the first time you
get in a page the first two tabs will be
expanded the rest will be collapsed so
that's just our guess um
for your for the most important
information in the card but of course
you will be able to expand and collapse
the other tabs to adjust to your own um
what you like the most and uh as soon as
you collapse one tab the summary section
will appear and uh in that section you
will be able to um to see the fields uh
some Fields depending and according to
the importance property you set on Cil
so you know you can set this property as
standard um additional or promoted in
case you marked one field as promoted
then it will show in the summary section
if it is additional it will not show in
the in the tab body also when you expand
the tab you will have to drill down a
bit more using show more in order to
have it
appear and uh you know we brought this
because we know that these are very cool
feature something important for you to
have and here it is and um another very
cool thing about fast UPS is the fact
that their state is persisted so when
you leave the page to go somewhere else
and then you go back to it the tabs uh
their state will be preserved so what
you left collapsed will still be
collapsed what you left expanded will
still be
expanded again when we first the when we
show the the page first first time we
show the first two Tabs are guas then
you just change the configuration of
your tabs expanding collapsing them and
we keep
that so pretty cool right yes and
actually we have that for other parts of
our uh the nice thing about uh fast tabs
is that they are also available in in
the tablet
client
okay so what do we have next Arena so I
think next we should uh show uh lookups
oh yeah uh uh well talking about
greasing cards so um all right we've
also brought in the web client the very
cool experience we have for lookups this
has been something again available only
in the windows client it's very cool
feature we we received a lot of requests
and you know here it is now so um inline
lookups looka
Fields you can bring up the the lookup
byli clicking on the lookup field as
soon as you click on the lookup field
the on the lookup button the lookup will
be brought up for you and you can
interact with it it's a grid you have
all the familiar Concepts you're used to
in grids you have vertical scrolling and
with vertical scrolling you have loading
rolls on demand as as Arena just showed
you a bit time before so you you have
continous scrolling and horizontal
scrolling as well is available with a
free Spain available in lookups but
controlling the lookup uh is not
something you can do only with your
mouse your keyboard is also capable of
doing this so focus on the field and hit
alt arrow down by doing that you will
bring up the lookup and do not leave the
keyboard stay on that stick with that
and use Arrow up and arrow down to move
across the different rows in the loot
cup uh and as soon as you are ready for
making your selection just hit enter and
that's
it pretty cool Arena what do you think
yes we love inline lookups yeah we love
it and uh we have something more about
lookups Arena yes so I think we should
show search as I type in lookups yeah so
before you were showing us uh the search
experience in greets well the same
search experience now is available on
lookups as well so get in the lookup
field and start typing as soon as you
pose the lookup will be brought for you
automatically by the system yeah
this Y and
um the the search criteria will be
applied so you are setting a filter the
filter is applied and then you can still
keep using your keyboard as before and
move up and down using Arrow up arrow
down and then hit enter the moment
you're ready to make your selection so
very
fast and uh pretty simple and as a last
thing to show you always about inline
lookups is the fact that the search
experience is also cross colume in lcaps
so same search experience you can also
use wild cards here and it is cross
Calum this is different from the windows
client in the windows client you know
better than me uh you need to select the
colum here you don't need that so it's
very fast you start typing cross column
search so it the the your filter will be
applied across all string based columns
and this is pretty amazing right yes yes
so that uh was um our last uh demo on
the on the uh web CLI on the desktop web
PL and uh so I think we should switch to
um back to the presentation right
okay just let me once you do that then I
will try to wrap up so basically what we
want you guys to remember is that uh we
have done a lot of enhancements and we
believe that the uh uh user roles
operating on desktop they will have a
great experience and it should be a lot
easier to uh have uh the windows client
users switch to using web client so this
is one have been one of our uh
investment
this
release yes so what do we have next on
the agenda it is about developing for
the universal LA right yeah okay so um
when
um when it comes to developing for for
for all devices you probably think uh or
fear maybe new tools new languages new
devices new development environment but
actually you wanted any of those in
order to quickly build a reach tailored
uh uh application that should run across
all devices so there is almost no
learning curve because you will still be
using the same tools you you have until
now the uh development environment and
you could use the CL language for uh you
can use the CL language even for
accessing uh uh device capabilities as
we will show later
you can also reuse your components your
business logic your pages and your
customizations um of course there are
some small tws we need to do uh in order
uh because of the different form factors
um but it's not like you will have to
rewrite your your
Solutions and there's low cost in the
development because you will not need to
buy a new set of devices uh with the
latest version of Android or uh or other
operating system but um you can develop
and test your uh app just using your uh
your browser and your
desktop and we consider it low
maintenance because with Dynamics NV you
build your up once and then it will run
across uh your tablet as your SM
smartphone and your
desktop so now I will just walk you
through some of the uh suggestions
considerations we have uh about uh uh
developing for for across
devices so developing for St for the
phone client is uh almost the same as
for the uh tablet
client um but you have to be aware of
the fact that as the screen size uh is
gets smaller then uh the user experience
has to be much simpler and also a bit
more limiting and um our suggest is
suggestion is that you should not design
your pages um with the Assumption of a
certain screen size so in this case for
example you um you have two groups right
and that will probably look good maybe
on a tablet on a on a landscape mode
right uh but if we do that show that on
the phone yes we will try to adapt the
layout but you probably won't get the
best experience so you could what you
could do for example instead of you
deciding the the the structure of the
groups you could let our layout flow the
parts and uh it will take care of uh of
rendering nicely for for
you and uh so so yes our advice is don't
Tie Your Design to a certain
device and the next thing is about
bricks layout so actually I promised I
will uh come back to to this so is this
as I said we have redesigned the uh the
list in the phone client in order to uh
optimize the available space and the
readability of the data so this uh brick
view concept is actually compressing uh
um more columns actually in total you
can compress up to six columns in in the
brick view structure and uh how do you
implement that in the uh metadata
basically you add these fields to the
field Group property uh on the
table and uh the bricks have up to six
layouts uh depending on how with the
number of columns you are choosing to to
have in the
brick we also have um some
limitations um to the to the brick list
meaning we do not have the concept of
the current row and we do not have the
concept of uh multi selection and uh we
also do not support the um um shows3 for
example right I think show3 is quite
complex for showing it on a
phone and uh another thing to remember
when you're dealing with lists uh on a
phone is that uh uh you could make use
of the scr scope property on the actions
so if you would like that your actions
appear on the action pane in the editing
card that I I just saw uh on the phone
on the iPhone uh you should set the
scope property to be repeater uh in that
way you're indicating to na that my
action is actually interacting with the
rle and it's not interacting with the
page and of course if you set the action
on the page then it will be shown in the
the action pane Associated to the sub
form and the next one is about
card
pages so card Pages they are normally
very busy they render a lot of data a
lot of fields and uh of course you won't
have space for that even with this two
column layout that we have introduced so
we suggest that you use uh the
importance property on the fields uh
that Andrea actually talked about in the
fasts um like um if you set it on
important then uh on promoted then it
will will uh uh show on the summary if
you show it on additional then it we
will take it away from from the fast
apps um yeah so that's about the the
card pages and now the last thing we
want to talk about is the device
capabilities so we said before that the
uh nfv Universal app um can um um
support the use of camera and location
so this feature is only available for
the Universal app um the API for
accessing the camera and location is uh
uh Cil API um it is available in the
client extensions
assembly and the API uh follows the
event based asynchronous pattern the
reason being that uh when you when you
are interacting with the location
requesting the location or you're
starting up the camera it can take up it
can take some
time uh depending on the device so we
will not want that our app is uh blocked
waiting uh for for the GPS for example
to to kick in so um so that is why um
and now before we uh go into the demos
of how to use the the this device
capabilities let's talk a little bit
about just briefly about the
architecture right so um the camera API
and location API I said they are uh uh
in Cal right there CL exposing C is part
of net assembly and uh the server will
send a request to the client uh to uh
interact with with the device um and for
uh reaching out to the device native
capabilities we have we're using Cordova
plugins which offers a uh common
interface uh for for accessing for
example camera and
location so uh with that uh Andrea is
going to show you how to use this API
for device
capabilities sure
thing so now we dis miss the
presentation and we
again mirror our screens instead of
standing it
oh
okay you can see it perfect yes all
right we talked about it we chat about
it you saw it now it's moment to develop
it so we're going to implement a few
scenarios for device for developing
device capabilities and uh they're going
to be uh simple but straightforward for
you to see how easy it is to develop for
device capabilities so are you ready
Arena yes I am all
right so we let's use the small business
profile and the mini customer card so
one thing you need to know about me is
that I'm not a cal developer so so he
doesn't know make
mistakes I tried this a lot let's
see but that's okay Andre that shows how
easy it is to use the API right yeah but
you know how easy a developer like me
can screw it up
all right so this scenario we are going
to implement is fairly simple in the
customer card we are going to create an
action an action to get your location so
our first demo our first coding session
is about that developing for the
location API we're going to create an
action the user will be able to click on
it and this will bring up a message with
his current coordinates it will tell us
where we
are so the start point and this is valid
every time you need to develop for
device capabilities you need to define
the objects you're going to use in in
this case the object needed for
interacting with Device
capabilities so and we Define them as
globals so as I told you I'm not a cal
anymore so I don't know the shortcut
keys forgive
me so yes we are going to need need two
variables one variable we call it
location
available so location available is a
Boolean and it is a Boolean Guard we're
going to use to be sure that device that
we can have access to location think
about it every time an app wants to
access your location capabilities your
GPS your G localization you get a little
nice message telling you do you want to
allow this user this app to use your to
access your location and you can say yes
and no if you say no then you will not
have access to these capabilities we
need to keep that into account that's
why we need this variable and it's going
to be up much Clear uh in in a few
minutes the next variable we call it
location and it is a
net type and being a net we need to
specify which type orena told you before
that when you develop for device
capabilities everything you need is
inside the client extensions assembly so
we need to reference this
assembly let's get
it so should be somewhere
here here it is Cent
extensions we go okay and we are soon
brought to a view where we can see what
types we can play with so you can you
can recognize something there is camera
there is location some options so looks
like a fun place so in our case we are
going to need location
provider so location provider is the
type we need and we set it location
provider is uh our entry point for the
location API as the name implies is the
provider for location so we request to
these object locations we're going soon
we're soon going to tell it hey please
give me my location so that's our object
and we're not done yet when we need to
Define our provider and that's valid for
all the providers in general because we
still need to set a few things so we
bring up the
properties and so can you see these two
little ones random client and with
events yes we can so you need to set
them to yes okay
otherwise it will not
work why that so run on
client uh these apis are running on our
client we need to grant them access uh
to run on nav and with events is because
as Arena probably mentioned before these
uh API are
asynchronous it means that the moment we
will request our location we will not
get it immediately so we will get it
after an event is raised so we need to
allow these events to be recognized in
nav and that's why we need to set yes
what do you want okay just some update
all
right now we're done we can save we can
compile okay so far so good and the
first step is done we have defined our
objects so do you know what's next Arena
think we need initialize the object
right all right so now we yeah now we
need to give them some values so we go
to our C code for this page and we
locate the onop page
trigger here we can add our logic to
initialize our variables so what do we
do the first thing we want to do is
checking that we have access to the
location so we can ask to our location
provider
is available so do we have location do
we have access to location did the user
say
yes in
case what we do is initializing
location so which keyboard is this okay
you can switch it no no I'm fine looks
like it's not the Danish is the US one
good no this to
English and we use
create in order to create the location
provider object so now here we are
creating the location provider and after
we create it don't forget that we have a
guard
so we set location
available to
true and that's
it we do not need anything more at the
moment
so as soon as I get to the page I create
my object so it's going to be available
throughout all the lifetime of my page
so I can access it very
easily um well now we have the we have
the finer objects initialize them we can
create the action so we go back to our
card and we show the page
actions instead there we can create an
action so well I guess this this is fine
uh we can create our action here and I'm
going to call it get
location yes and I'm going to set some
properties on this
action and the first thing I'm going to
set this is pretty important the
visibility so guess what
we don't want to see that when the
location is not available yeah so if the
user said no we don't display the action
at all so we will not bother him he will
he will not know there is the ability to
access location because we don't have
location and we can use our Global
variable to to flip the visibility of
our action and just a few more minor
things just let me set this thing as
promoted
and I think all the other action here
are on category
four that's and promoted big this action
is nice so I want it to be
big
uh okay so we have defined our
action we have defined our action and uh
I guess we can now add logic to it so
let's add some some logic and let's show
the C code
and here we have the on action
trigger here we are going to request
location so we use our location
provider which is we we call it location
and here we are request location
async so this is the place when we start
requesting for location as you can
see where is my location
am I does this thing me something uh
where do I save it it's not here so
again it is the asynchronous pattern it
means that you will not get access to
the uh the real location there because
you just requesting location you need to
wait for the device to be ready to give
those information back to you but
meanwhile while you're waiting for uh
for the device to do his magic you're
not blocked the user can still do
whatever he wants he can interact with
the device do whatever he likes because
we're not blocking you that's the magic
of the asynchronous pattern and once
it's ready you're going to be able to
fetch
location
here so this function was automatically
generated by our extremely nice
development environment the moment you
created the location uh global variable
and here we can add the logic to to
receive our coordinates and do whatever
you want with them so what do we do the
first thing is checking
that our
request was
successful why that so I don't know your
user might be a spy or whatever it can
be in a bunker so he might want to
request location there and of course he
will not have access to the satellite so
your request might not be successful
every time keep that in mind so ask
status and check if it is zero zero
means fine you get your coordinates so
if we have our
coordinates then we
display those
coordinates
so you are here
and we just put a few Place
holders
and no this is our
Architect no no how can I dismiss it
ignore go
away um yes where are our coordinates
they are
here coordinate you forgot I forgot to
shut down
Skype sorry about that and I didn't mean
to screw your demo yeah
so location coordinate do
longitude they are there and we display
them in a message and if we do not have
them well we just display a pretty set
message and we can make a bit
funer that's it looks fine okay so so if
I didn't make any mistake I should
compile I did something so you're
missing the H wait a moment okay else of
course of course that's that's your
fault it was the moment Skype po it up
and I lost my
cool I'm sorry you're going to pay for
this Arena and she's my
manager okay you can try it out so let's
uh try out let's see if we can switch to
the
iPhone so uh that was on the customer
card right yeah
M
yes um isn't that that actually that
happens automatically now as far as I
know so um but in any case let's
see yep there it is so it is the a
location oh thank
you my first C demo worked I feel
proud right okay so you experience the
how to develop uh for location
API and uh I think we have time also for
yeah we have we have time to show also
the camera perfect I mean the API is uh
pretty similar uh but um it's just a a
different way of getting the data
getting the pictures so we can also show
that so next scenario next scenario we
move from the location to the camera and
with the camera we just have a picture
here uh in order to make the thing a
little bit different we're going to play
with uh something called camera options
so when you create a provider you um uh
you know we just created our provider
and we called request location assing
without passing anything so there
we can actually set some options but we
left them with their default values but
with the camera we're going to show you
how you can pass some uh more
information to your API in order to get
uh different kinds of information in our
case what we want to do is being able to
take to take a normal quality picture
and a high quality picture the way to do
this is by means of the camera options
object so
I will not be detailed as before in the
first part so allow me to speed it up a
little so who remembers the first step I
do I don't care so anybody remembers
what we need to
do yes give me a shirt this guy deserves
a shirt okay
yes who are you
sir oh you already have one that's not
that's not nice
he wants he wants another one
yeah but exactly we need to Define
variables so we get to globals and we
are going we stay on the same page we
Lu oh yeah sorry sorry sorry that's your
fault ARA again
that's yes all right sorry yes here we
are sorry for that uh perfect defining
variables let's do this
so well out of fantasy I'm going to
create location
available this is going to be camera
available sorry camera
available uh it's pretty repetitive
pattern and uh we now
create the camera provider object so
again this is a net type we need to
specify which type and remember
everything cool is in our assembly
client
extensions we will reference it and here
we get to camera provider this time we
select it and fine so who remembers now
the little trick we need to
use are we done with defining this
variable
again yes the variable the events and
the random class
find all right here we have a shirt
where are you
sir there you
go
okay
precisely so we bring up the properties
and we set them to
yes
perfect we just save because I feel
safer and uh so for this demo I was
mentioning that we will go a bit further
so we need camera options as well but
before that since uh we're going to
handle a file in this demo we need a
file object so we call it incoming file
and this is a file so once we
get not
now um our
encryptor uh once we get our image we
need to play with it and since it is a
file we need a file variable file typed
variable and here now we get to the
camera
options this is a net
type leing in
our name space uh sorry in our assembly
Cent
extensions and this time it is called
camera options so we select
it and that's it uh for this guy you do
not need to set run on client and with
events of course only the
providers and because providers are
those who are using the as synchronous
pattern yes I I think we are done here
with defining
globals and the next step is
initializing these things so C
code on open page okay here we have our
nice logic of before and you know what
it's going to look pretty much the
same do we check we check whether the
user granted us permission to use
camera and in
case we
can
initialize our
object by invoking
create and do not forget
our guard which is pretty
important yes and this is
done all right so we we also initialized
the logic so a bit fast forward and we
now go to the page actions and in the
page actions we add a new
action we add a new action and you will
probably guess get
picture get picture and we set a few
properties
here visible we flip visibility thanks
to
camera
available and just a few more tuning I
want it promoted in the same category as
the other actions in this group and big
fine and now we need to add some logic
to this variable not this but yes this
um right see code and here we are and
well you can probably guess
it it is
just the
same request picture
assing in this specific case so again
using the synchronous pattern we can
request for a
picture and uh again as before you don't
get the picture here you will get the
picture in an Handler function which was
created and generated automatically the
moment you created the camera object the
camera provider object and here we can
play with it
um yeah we're going to use our incoming
file and
open the location so picture five
part and after we do this we can well
display a a very simple
message with the size which is important
because I want you to realize that the
quality is changing when you will take a
picture with with a normal quality
picture and you take a high quality
picture
so and incoming file
do after that it is very important that
you properly dispose the your your file
so the moment you you request a picture
you you will see this orena will will
play with it um you will take this
picture the picture will be uploaded to
the server on a temporary folder and it
is a temporary folder where you need to
deal with your stuff so it's there play
with your image play with your file we
don't care about it but after that be
sure to clean it it's your
responsibility so here we close
it
and
sorry yes
we properly
cleaning picture file path should be
successful yes and this is for no wait
orena we have the other action so this
was the simple action so the few the the
only New Concept here is for the the new
important concept uh is the fact that
being it a file for the for the camera
IPI you need to properly dispose it here
in the Handler and now let's play with
the camera options I promised you we
would have cre created two
actions so the other one is
get picture
high
so here we are going to get a high
quality picture how by playing with the
camera
options same as before this is an action
which is which has some point only if
the camera apis are available so
we use our Global guard it is
promoted same category as the others and
big we save it fine and
now we do our magic
here so how to do this very simple you
remember camera options yes so we are
are going to initialize
it uh I probably choose a bad name
because this is the way you do
this if I had chosen a different name
would have been better than this camera
options equals camera options. camera
options my fault but the important thing
is that here you can set
quality to 100 quality is uh is a value
spanning from ranging from 0er to 100
um 100 simply means the um the picture
is going to have uh the full resolution
allowed by the device if you set 80 it's
80% of this full resolution by default
the value is
50 and
then we can
request our picture and we pass
camera options in
here yes of course I had to do this
mistake that's okay now you can play
with it Arena okay so arena is going to
show you the two options let's see if
I'm ready uh
okay so which one should start get
picture yeah
smile this is how you see from up here
okay let's keep note of the
size okay
fairly light I'm
sorry and now let's use the other action
for taking a high quality
picture this iPhone well should be a
high
resolution so we expect it to be bigger
yeah yeah it definitely okay and that's
it that was pretty cool it's pretty
simple to use well even I could do that
so you can do this for sure and uh let's
switch back to the presentation because
I have a
little bit more things
to CH about so let's extend
it Chang yes and
okay yeah
starting all right where is the thing
yeah there you go
okay so you could see that developing
for uh device capabilities is fairly
easy uh um and uh again we didn't use
anything different from everything
you've been using today until today so
it's the it's our development
environment all the tools everything we
are familiar with the experience is
exactly the same orena already told you
that no new tools no new languages
that's what you have been using in the
Box always so that's what we want to
remark again uh let me uh underline one
thing
there are a few limitations that you
should take into
consideration because because now the
experience on a on a device such as a
phone is different you have you have
less space things are different so
you're going to have some limitations
design your Solutions accordingly so in
the first place let's consider a feature
like multi selection multiple selection
is something you have available only in
the web client you do not have that
available in the tablet client or in the
phone client so design your pages
accordingly to that again activity
buttons something you have in the web
client not in the tablet not in the
phone client worksheet Pages yet another
example uh but this time they're not
available on phone but available in
tablet and web
client I would like to bring another
example which are lists you could see
that on a phone a list looks totally
different from a from how it looks like
in the web client or in the ttle client
because we we lack real estate we have
smaller screens things are a bit tougher
so we had to use bricks to showly out in
a different way and try to display all
the required
information but there for example you
will not be able to display a fact box
on a list on a phone it's just
impossible it means that you should give
up on on those facts absolutely not you
can work around on this so if uh in this
in this specific example you can find a
solution to this little problem by
simply uh ensuring that that fact box is
also displayed in the in the card page
in the card page you will have those
facts available so we have
limitations we know that you can walk
around on this you you can play with it
and it's not like you're alone out there
we are here and the all these limitation
are fully documented on our msdn uh site
so go there check them and develop your
Solutions and let us
know uh as well as new challenges
so developing solutions for multiple
devices is pretty amazing experience but
sometimes you might want to display
information differently depending on on
our client type so you might want for
example to display information in the in
the RO Center as cues in the tablet
client in the phone client and as card
Pages or card Parts in other clients in
order to do that you have the ability to
use current client type variable in C so
with this you can um you can Define
different layouts depending on the
client you can differentiate the
experience across our clients and that's
something we advise you to do
and the other thing we want you to
to uh to always be aware of is the fact
that on the phone rigid layouts the
rigid structures uh do not flow well try
to avoid using them when you're
developing AC cross devices because they
will you will have problems with these
structures in the phone so try to use uh
flex flexible layouts try avoiding grid
layouts and fix the layouts if possible
and if you really need to use them then
again use current client type
variable in order to differentiate the
experience across across
devices there is one last thing I would
like you to to keep in mind and it's the
fact
that testing your solutions for multiple
devices can be tough you know we've been
through this and uh well Vincent showed
yesterday this big picture with the
Android market and all the different
display sizes it's just crazy you cannot
go there and test on different devices
each of your page it can take time and
be cumbersome so we have added something
for you and those are our as Pages you
you're already aware of that we have
default ASP we have tablet as PS and now
we have also phone as PS so just let me
show you
these again I need
to yeah but I need to can I just move it
instead of EX stand oh you're right
yes uh so this
is wait a moment I need to adjust the
size so this is phone.
ASX let me resume
it and by using pH SPS
in a browser you can uh actually see how
your page looks like you don't need a
device for that use your browser and uh
and play with it so here in a browser of
course you will not have the same
experience as in a device we cannot
swipe here we need to to use the old
fashionate scrollbar but fine maybe we
don't really need this uh swiping if we
don't really need to test it
just if you want to to see how our Pages
looks like look like so use these pages
to test your applications it's not
difficult you
can it gets easier just need to realize
that you have the tools for doing
this and uh we hope that you go out
there and build your pages your
Solutions we are really eager to see
them so go ahead and have fun yeah okay
yep thank you Andrea for uh for your
demo so um I think we are um pretty much
at the end of our session and but before
uh we start into questions we have
actually put up some uh some of the
questions that you know that we know
that uh probably they are in your minds
so um let's go through them so does uh
does NV work offline and U uh the answer
is currently no
uh how Universal app how Universal is
our Universal app right uh so when you
talk when we talk about when we think
about Windows 10 and what universal mean
for means for Windows 10 that means a
lot of uh type of devices from internet
of things from um uh tablets from
smartphones from Xbox um and so on right
does NA actually run on all of this uh
and the answer is know uh we are
primarily working on smartphone and
tablet and
desktop uh what about the new wave of
platform versions like uh new version of
iOS or Windows 10 sure yes definitely we
are going to support that we have a
three months period to adjust to to some
of the these new platforms so we'll
probably issue some updates if
necessarily uh do we support uh barcod
scanning and the answer is no uh you can
uh take a picture with the with the
barcode uh but that could be quite
cumbersome when you're are working in an
a warehouse and you're doing this
exercise pretty frequently right but
there are also some uh barcode scanners
that uh could uh introduce the text
directly into into the text box so we
recommend you guys use
that and the last question should I
avoid building native apps
so the answer is not really it all
depends on the scenario so um if your
scenario is about completing a daily
task using uh nav uh and nav business
logic uh then our solution is the best
but if you are thinking about a very
tight integration with your
device uh or a very specific type of UI
then uh we do recommend that that you
build your native app using the uh NV
web
services yeah that was uh all we had so
um we could move into
questions y y
so can anybody help with the mic or um
hello go ahead um I need to know if the
web client is as reliable as the windows
client and it's
more faster than the windows climent and
of course I need to know if it works on
aspet sorry it works on HPS ASP net ah
okay so let's repeat the question so
your question was whether the uh uh web
client is reliable just as reliable as
Windows client yes and if it's faster
than Windows client and it is faster
than Windows client okay
um so if if it is reli as of course it
is as reliable as the windows client
this is what the message we are trying
to convey here today um in terms of
performance uh uh I think so I actually
we have done a lot of uh improvements to
our web plan performance um I mean of
course optimizing field for performance
is an ongoing tasks that you know we
always have our minds in any of our
releases so um so I think so to answer
your question I didn't really get the
last part
with but okay we
can if we using aspnet or uh no if the
web client uses ASP net yes it
does very little though we are moving to
browser side components
yeah I wanted to
ask if um how worksheets are different
and why they are not supported in home
client so I think um main reason is uh
because worksheets are meant for inline
uh inline editing of your data and uh
and you know we really wanted to uh if
we would be enabling worksheet we really
wanted to offer the users a great
experience and we're not sure you know
using this editing in card might be a
great
experience um but on I mean we will have
this in
mind any other
questions hello yeah so yesterday we
have seen that we can totally change the
visual of the RTC so is it possible also
uh in the P client as well to make some
here to make some addins yeah uh yeah we
are supporting the the JavaScript addins
the client extensibility framework is uh
um also is basically available in web
client and actually if you are using uh
the JavaScript addins you can write your
code once using JavaScript and it will
run both on the web client and all the
windows
clients hi bit puzzled about the
uh location and the camera net type
class that you're using because you're
running a d climent but you cannot Run
net on iOS or non Windows device so how
does that
work about uh you mean you're referring
to the net interoperability or what yeah
you s net class run on client but it
doesn't run on on on a non- Windows
client it doesn't run on iOS so how can
you select run on client and still uh
use the camera
um because we are relying on Cordova so
basically uh on your device we are
relying on Cordova to have the same um
to have an abstraction of the of the all
the inner logic which happens below the
stack basically so Cordova will abstract
this on both I on all all platforms
supported so iOS Windows and Android so
that's why you can do that
any any more
questions there's one
here hello good morning um just got a
question about the minimum bandwidth
requirements yes I do not recall that I
don't I but we I we can look it up
um what we have done is we have done a
lot of investments in uh in um offering
the user a great reconnect
uh scenario so basically if you are in
um in places where there is a low
bandwidth then uh and we you lose your
connection uh then the um the client
will try to
reconnect um and uh it will actually
take you back to at least we will try I
mean of course if you have a lot of
model dialogues open and so on it might
not be possible but in general we'll try
to bring you back to the same context uh
before the before the connection was
lost
yeah um in 2015 you did the setup for
the mobile client and web client in the
RTC in the windows client so that the
mobile client uses sees only those
fields and and rows is this still the
same for 2016 and new versions so that
you do the user and rooll setup in the
windows client and after that the the
web client looks like the same yeah we
still support configuration for web
client that is true okay also for the
fixed rows because you told us that the
first row is always the fixed
Row the F pain the first Pan the the
First Column the First Column yes um for
the freeze pan or yeah in in in 2015 you
can set it up in the windows client and
it's also applied in the uh no it wasn't
available there no it was not available
so that's why I'm a bit confused so but
yes I mean you can customize the freeze
Spain column uh in the RO tailer client
uh and then web client will uh will will
take this in consideration okay thank
you so you can customize it it's just it
would be nice to have it to customize it
directly in the web client right
yeah okay I think I think that is all
okay but we up thank you very much
