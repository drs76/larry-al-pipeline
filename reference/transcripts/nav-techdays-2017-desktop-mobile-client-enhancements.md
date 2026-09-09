# NAV TechDays 2017: Desktop & Mobile Client Enhancements

- **Source:** https://www.youtube.com/watch?v=5lNX7RnsuJY
- **Video ID:** 5lNX7RnsuJY
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 95m52s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

my name is Haruna I am the engineer lead
for the nav client team and I'm here
with two of my awesome colleagues yeah
my name is Andrea third time here if you
remember me glad to be back I'm also a
software engineer okay so we won't want
to start by saying that it's really
great to be back here in Antwerp once
again and we look forward to show you
all the features we have been building
since we were last year on this state
and that was it was a nice experience
actually
but Thomas that's your first year here
right that is true yeah so let's see who
can allottee we have a t-shirt for you
where are you some words in the top well
who was the first one all right
great okay so during the keynote you've
probably have seen glimpse of the of our
work during this year of the client
enhancements and now it is time to
actually show you in detail how you can
enable these new features for your
customers in your solution so let's like
let's start with the session objectives
for today so bringing nav to two devices
everywhere and anywhere has been a
continuous goal in our strategy and that
is why we will be starting at the high
level recapping again the overview of
our client technology where we are and
where we are heading towards from user
experience point of view after that of
course we will go through the nice
features and we'll talk about the latest
features and updates that are available
in to this year's release and we hope
that at the end of the session you will
walk away with a good understanding of
how you can
label these features and create new
scenarios for your customers and then we
will also take a peek under the hood at
the architecture and platform
improvements that we have done during
this year and there are quite a lot our
focus has been as you have also seen in
the keynote on providing a great
experience for our end users in the
cloud and as usual we will be rounding
up with with a Q&A yep it's it's a
pretty big agenda right yeah so would
you start from yes so let's start with
our overview of the client technology so
at a high level we will be going where
our users are going which is basically
devices and office 365 and interestingly
enough the devices have introduced new
scenarios for us and the reason for it
is because they bring the computation
and information to be available anywhere
and today it is expected that any user
can perform any task on any device at
any time and securely and with comfort
and also supporting all sorts of type of
interactions like a visual touch gesture
voice mouse keyboard and so on and
basically and basically the desktop
client right it's still here with us
users are very fond of it and it's not
gonna go away anytime soon but one thing
is for sure and that is that there is no
more one single entry point for the
users that we as system providers and
developers can optimize and build their
application for so we also have looking
at the enough clients right we have the
desktop clients which are designed for
intensive use for concurrent tasks right
and also we have the tablet on phone and
these are basically optimized for touch
and enables our users to perform their
tasks anywhere basically and recently we
also have a small addition and which is
that the nav universal app can run on
hololens we did not have time to
optimize fully for the heroine scenarios
but
you should go ahead and try it out at
least we had fun trying it out right
Karina that's all the I was really
actually doing work at my desk when I
was playing with hololens didn't look
like that this is my I was just waving
hands all over the place I think it was
the first time Tomas was happy about
testing his features yeah so now that we
have a good overview of our clients and
and where are we going let's talk a
little bit about how an AV user
interface comes to life and it is
important to note one thing that the
enof user interface has not been
optimized for one single neural task
basically it is a fully feature up at is
flexible customizable on row centric so
it all starts with the table data and
paid objects basically with the
application functionality and the
business logic and after that we define
the profiles and then we start applying
the configuration and personalization
layers and those two layers basically
allow us to customize the user interface
and the difference between configuration
and personalization is that the
configuration changes are applied to all
users in a certain role wise the
personalization they are specific to to
one user and after that the nav platform
takes over and uses a set of layout
builders to render the controls on the
screen so these little builders are
actually not customizable and that's
intentional right because they make
decisions based on the form factor and
device type and one and one common
misconception about the user
personalization that has been that the
user personalization is intended to
render the UI differently between
desktop tablet and phone but actually
that's not the intention of user
personalization the intention of the
user personalization is to provide the
exact view of the data that the user
needs to perform their daily tasks and
this is how basically the
and Ave user interface comes to life
meaning we have even though it's one
user interface actually has three three
displays three three user interfaces and
they're all based on the same common up
and on the same come on client platform
yeah it's always nice to have a recap or
architecture but you promised us
something right yes okay so let's talk
about what is new right and let's talk
about one of our recent features and
that is user personalization so the
recently we have introduced for our end
users the ability to customize their
workspace in the web client directly in
the browser so what does this mean this
means that the users can of the web plan
can also now optimize for efficiency
meaning they can for example take the
fields that they use the most and move
it on the top of the page or they can
simply hide away the data that day or
their organization don't need and it has
been our goal to provide an intuitive
experience meaning that the users will
simply get immersed into a and not
really need any help for for doing these
changes so they can just do it
themselves so let's let's take a look at
how hot personalization actually works
oh very sweet let's make a switch okay
so I am currently signing into a dynamic
c-65 financing operation in the business
manager role center and what do I find
the personalized action I find I did
under the settings cog wheel in the
dynamics 365 shell and notice that when
I click the personalized action then the
personalization toolbar appears and I
can start right there customizing my
role center without any additional setup
so what is it that I can do with the row
center for example I can drag the tiles
inside the activities part so let's
assume that I you
invoices a lot or orders and then I
would like to have it to be the first
style so I can just drag it in front of
the orders and also I can hide ties that
I don't necessarily need for example I
have been knowing a navy for quite some
time so I don't really need the replay
getting started tile so now that I am
done customizing my role Center I can
move on to the items list and also
customize my view there as well so when
I actually move to the item list you can
see in the in the rows view that the
number column is at all times in view
and that is because the number column is
set out to be a free spin column but now
I would like to also keep the
description field in view whenever I
scroll on to the right so how would I do
that
I set the free spine to be the
description column I notice how the UI
simply adjusts to my changes so I do
this this change is directly in line and
then the screen simply adapts to my
changes and I can do a lot of other
things like for example I can move the
columns around let's pick one let's pick
B for example base unit of measure and
move it before quantity on hand and I
can also hide some columns let's assume
I don't need the assembly bomb for
instance and that's it basically this is
how I get to the exact view of my data
and now that I am happy with how the
grid looks I can also start looking on
the on the right side where we have the
fat box pane and since I love a lot the
item attributes features then I would
like to see it on top of the power bi
reports which are not set up so I can
just move it on top
great and now I can go even further and
customize my view on the item card and I
can do almost the same things I have
done on the list but at a Fields level
so for instance I can take the quantity
on hand and move it on the first stop
because maybe I'm using this field a lot
or I can for example rearrange the
fields inside the first stop let's just
pick one and move it around and also I
can hide the fields that I don't
necessarily need so that's it that is
how simply I can how simple I can get to
to the exact view that I want so I can
see only that data that I care about and
in the preferred sequence rearranging
content on the page is very nice up I
have to say I was expecting a bit more
than that so that we also have more
capabilities in the in the
personalization toolbar so if you click
more you will see that there is also the
option to add a field so add a field
with sliding a pain in there in the
right-hand side and you can basically
this pane contains the fields that you
don't have added yet on the page and by
dragging it on directly onto the canvas
this will be added to the item card and
this is how I'm performing all the
changes directly in line right and now
for example I think maybe I'm not
satisfied with all the changes that I
have made and I would like to present
clear personalization after all this
work that will not go so clear
personalization does not revert all the
changes you have done so far basically
it only reverse the changes that the
user is currently on right so you will
only lose the item card changes okay
that that's better
so should we know so actually I'm
satisfied with my view so I just want to
press down you sure yes okay so that is
how basically now I exited
personalization and what happens behind
the scenes is that those changes will
get applied to me and only to
and there is no more additional changes
in the UI because of all the adjustments
had already been done
why is customizing and also I can use
the product in the same time so that
that concludes our demo on
personalization I think so now we should
switch back to the slide and talk about
the personalization summary what is it
that we we need to remember right so
basically with personalization you can
only show the users how can optimize now
for refresh efficiency and they
basically can show only the data they
care about and in the prefer the data
sequence also the the UI interactions
are based on on drag and drop which you
provide provides an in context the
inverse directly in client experience
and also we can talk a little bit about
the depersonalization in terms of what
technology this is based on I know that
but the question is do you know anybody
know what's behind the personalization
I know Microsoft is an existing
technology is something that we ship in
a European 12 machine images few months
ago let me give you a hint there is
another session about that at the same
time with us yeah close close close was
designer tool right it's basically say
it's basically based on the designer top
button okay how much you have a bad yeah
where are you yeah so basically yes the
personalization has has implemented that
has been implemented based on the
designer tool so behind the scenes yes
there is a special extension called page
extension you won't be able to see that
into the extension management so don't
try that but basically this means that
we can basically continue in reaching DD
personalization capabilities even
or you know since it is based on a new
technology so designer is in general a
platform for for great innovation so
we're looking forward to actually work
more on personalization so but it was
every great feature right way it also
has a small fine print and of course you
all know that personalization is
available in Windows client today and
when we have implemented the
personalization in web we have been
actually looking at the Windows client
as a reference point however but right
now we don't have yet full parity with
with the Windows client in terms of what
we can do and there is documentation
available on on what are the gaps but
basically we're actively working on
uncovering those gaps as well also it is
important to understand now that you
know how the personalization in web is
which technology is based on that
basically the Windows client
personalization and the web client
personalization are based on two
different technologies that are not able
to talk to each other just yet and that
is why we have not yet provided a tool
that can migrate the personalization
from the Windows client to the
personalization on web but it's also
something that we it is top of mind for
us so also we are currently missing the
ability to to configure profiles that is
also something that that we're currently
working on the other the other two parts
are that are left in terms of fine print
they are regarding the personalization
experience so you will not have a
personalization experience on the mobile
devices and outlook so what does that
mean that means that the personalization
toolbar you have just saw so you just
saw on the on the web client is actually
not available on mobile devices and
outlook but basically if the user
applies the changes on customizing the
row center or the least
on the on the web client those changes
will also be available on on mobile
devices and in Outlook right so we don't
have the exact customization experience
available yet on devices and one last
two thing basically we don't support
form factor personalization that means
you won't be able to track independently
the personalization on on desktop versus
personalization on on tablet and phone
so as I mentioned before if you
customize your workspace those changes
will be available on all HTML clients so
that concludes my my talk on on
personalization and now I think that now
that you have seen you know how you can
instantly customize your your workspace
you can thomas is going to show how to
instantly change company and profile yes
so Verena just showed how we enabling
the user to adapt his environment or
user interface to best fit his needs and
I would like to build on this topic and
show how users are now in control of
their settings by showing the new
instance my settings page we have
introduced my settings page in 2016 we
were inspired by office products to
create one central place for the user to
manage their system-wide settings like
company name profile language and others
switching company and profile is really
important for small and medium
businesses because employees in these
companies usually fill multiple roles
and they have to switch between them
multiple times during the day and
speaking about roles accountants is
especially interesting because they
usually work with multiple companies
throughout the day so previously using
my settings was not a great experience
users had to sign out and sign in again
for the settings to take effect and it
also limited some of the use cases like
working with multiple companies side by
side and we heard constant feedback from
community that this is not a great
experience and we agree so we have
active and
active opponent on it and tried to
improve the experience and without
further ado I want to show you the new
instant my settings page let's jump to a
demo and for this demo I'm gonna assume
a role of a business manager a business
private business owner who's doing his
own accounting and also doing accounting
offering accounting services for other
companies soul and in my business
manager role Center where I spend most
of my time but now I would like to
switch to accountants profile and do
some accounting for my own company so
I'm gonna go to my settings the my
settings page is still in the same place
it's under settings and it looks exactly
the same all the changes we did were
internal and it's just now gonna work as
you just would expect it so Andre let's
select accountant profile it works
exactly the same and just before hitting
ok so before user would be presented
with information dialog saying that o B
be warned you have to sign out and sign
in again for your settings to take
effect
well that's no longer the case let's see
it ok so now a web client immediately
refreshes and when it's done we land
into accountant role Center and I can
just do my tasks right away here your
accountant now today Andrea we're gonna
create a purchase invoice but there's
one catch we're gonna do it only using
keyboard you know you're not allowed to
use Mouse it's gonna work so we'll start
with navigation pane and we will use tab
button to select purchase invoices and a
navigation pane and you'll hit enter to
open the page purchase invoices list
page will open and you will be
immediately focused into the first row
of the list but we want to create a new
invoice so we're gonna use shift tab to
navigate backwards to a new action yeah
let's say I were to open the card page
and here again the first input field is
automatically focused and
we'll use alt arrow down to expand the
lookup and let's select the first vendor
I think that's great and then Andrea is
gonna use tab again to reach the first
focusable element in the grid and so far
the experience was pretty standard this
is how anybody works today but now
Andrea is actually able to navigate in
the grid columns using arrow keys
because we have adopted a focus group
pattern inspired by office products so
you'll be very familiar how it works
basically we divide our UI into focus
groups or components which make sense
together and you can navigate between
those groups using tab but inside of
those groups you can use arrow keys
so now you can immediately skip the grid
columns and jump straight into the first
row of the grid by using tab tab yes
yeah and since input fields focus groups
because they are important parts of the
application you navigate between them
using tab so let's let's pick an item
number again using old arrow you expand
the lookup and Andrea knows which item
to pick is the artwork yes
conference table last thing to do let's
fill in quantity and again Andrea is
gonna use tab to focus input quantity
field and the last touch on drea let's
press control enter so that immediately
allows us to jump out of the grid and
jump to the next focusable field below
the grid in the form and this is great
for accessibility and productivity at
the same time Andrea I think we are done
here but now I would like to check out
check on other company I'm doing
accounting for which is not my company
so Andrea is going to open a new tab and
I'm just going to explain how this
experience would look previously so
previously I would either sign out and
sign in again and work with one company
at the time or I could possibly create
open two different browsers and sign in
at the same time onto two different
browsers or use in private mode but
that's just not a great experience what
we can do now using my instant my
settings we can go to my settings again
when the page opens we're gonna do same
selection as with it with profile we're
gonna select a new company and it's
gonna be my awesome company of course
you're gonna select my awesome company
and hit like ok again you'll see the
same experience the change is instant
the client is gonna refresh yeah it was
just ok finds refreshes and I'm like I
will land in my awesome company just
like that and I think all the vitals of
my company looks great so we don't have
to take an action here but let's look
back at the previous tab I can still
work with my previous company if I
choose so it's not lost so now I can
using new my my settings instant feature
I can easily work side by side with
multiple companies and by the way
exactly the same experience is available
on mobile let's let's see how how it was
possible so profiles right so we can
approach with profiles as well you can
put work with multiple profiles Immelt
honestly having side-by-side tabs in the
same browser windows exactly all
settings in my settings page work the
same way yeah so let's look how it was
possible before session settings and
session was very tightly coupled so we
needed to introduce a new complex al
type to decouple the session settings
from actual session so have a new type
which holds all the basic session
information like company profile ID
language ID local ID timezone and it is
easy to use this type as initializing
setting well you want to change and
requesting for a session update it's
better reflected in code so let's jump
to code example and here you can see
session settings type and it is complex
type in a sense of computer science but
it's definitely not complex to use here
I tried to try to find the simplest use
of
session settings type so we created a
new variable which is called my settings
and only thing you have to do is to
initialize it this will load stored
session information setting the
information from the personalization
table and fill it this type of this
information then you're gonna set the
value you want to change in this case
again I want to switch to my awesome
company and then you will request for
session update and here you have two
options you can call it with true which
is going to save these new settings the
personalization table and that means
that these settings are going to apply
to all future sessions so it will be a
persistent change or you can call this
method with false and you'll get an one
off session with these settings without
actually changing user settings so this
opens a new interesting area for
creating new user experiences yeah let's
let's summarize so we introduce the new
session settings type it enables to
instantly change session settings right
now from my settings page it works in
all HTML clients just one note it is not
recommended to run code after call and
request session update because server
actually doesn't know when the session
change will occur so there's no
guarantee when or if the code is going
to execute after this call also session
settings tab is available in extensions
so you can also integrate that in your
solutions or extensions for SAS for SAS
offering also session setting sessions
update is ignored in OData and soap web
service calls because it simply does not
apply there and also it's important to
always call in it before changing or
requesting for a new session just to
make sure that you're not overriding the
sessions you did not intend overwrite so
don't do not be discouraged by these
best practices because it's a cool new
type which opens a lot of new
possibilities and we are really looking
forward to seeing what the developer
community is built on using this now I
want to show you another thing so we
talked a lot about how users can adapt
their
why how how they are in control of their
settings now I would like to focus to
one specific workflow which we work hard
to improve and that's report preview and
print you viewing and printing reports
is very important part of entering
business interactions
there's nothing worse in terms of
productivity when you have to switch
between different apps just to preview a
PDF document while you're working on
some important flow and it just breaks
your focus and it's not a great user
experience most of you probably are
familiar how report to you works today
in Windows client so in every request
page has a print and preview button and
and they open a new window where we have
basic controls for navigating the PDF
and also printing so the same same
functionality but in less a much lesser
extent was also able on web client but
previously it's only worked with
Internet Explorer because of selection
of some specialized components here in
NAB client theme we strive to embrace
the open web standards and we want to
provide the same great experience on all
modern browsers so this year we worked
hard to create a new PDF report preview
control which offers uncompromised
experience on all supported platforms by
nav so let's see how that works in
action yep
so I'll and into sales order processor
roll sensor and I give a and I will give
a quick tour of some of the reports
showing off the report capability
reports preview capabilities and rayless
let's expand the ribbon and in the
customer reports lets select item
customer item statistics and while the
while we yeah so now we get a request
page where we have two familiar actions
from windows client that's printing and
proving a report in this case let's
select preview and now server is gonna
prepare generate a PDF document and is
going to serve the document to the
client so the rendering is gonna be
performed fully
the client is all client based and here
we have very familiar experience full
screen we have PDF document in the
center we try to use the space available
in the most optimal way and we also have
familiar controls which you probably see
in another PDF your apps so andre let's
try some of them for example let's zoom
in yeah and here you can see that
rendering is really crisp there's no
distortion you can clearly read the text
and you can also let's try to fit back
to the page yeah and it's very instant
it's just as you would expect that's
that's what we wanted to provide and
aundrea let's try to hit print and see
how does that work Wow yeah and we just
get the native printing experience from
the browser and if you already set it up
a printer you can immediately hit print
and it's gonna be printed but this time
you know gonna do that you know we we
are we care about the world right yeah
so we would rather download and send a
file through email let's close this
report and let's look another customer
report I actually want to check my top
10 customers so it's again in the ribbon
in customer reports and this time we're
gonna skip the preview and it will jump
straight to the print so that works the
flow is the same as the miniguns client
so you can save time if you are
comfortable with every port and you know
how it's going to look you can hit print
and you'll be presented with the same
native browser page where you can
preview the PDF and here please note
that the PDF is very rich so we support
custom fonts we support images and we
can see that the graph is also rendered
just perfectly and again if you have all
this printer setup ready in a browser
it just works in all pages and it work
also works in nav yeah well again we're
not gonna print the document so let's
close now let's open page search and
we're going to search for one
interesting report
which is
[Music]
detail trial yeah
and again let's just preview the report
and this report is interesting because
it's very big and you can see here
server we are waiting for server to
prepare the PDF document but once it's
ready and it hits the client it's gonna
be it's gonna be very fast how many
pages do we have in here I have no idea
I should scroll yeah let's just scroll a
bit that's a lot and here you can see
the experience is really good because we
try to optimize how you render the page
which we employ some really smart
strategies of a partial rendering how
many pages do we render Andre let's try
to assume that also should work just as
smoothly as before and I will try a
control which we didn't try before let's
try to select text so Andre is gonna
pick a text selection tool and yeah he
can just decide on on a text he wants to
select and it just works as expected you
can copy and paste also we support links
so if a PDF document contains links you
can just press on them and I gonna open
in a new tab and it's just an experience
you would expect in your modern browser
yeah and I think I think this looks good
I know Andre I can also pan the document
using the other tool which is the hand
tool again just as in any PDF preview
yeah let's close close the report and
let's recap a bit on the new PDF control
so the new control supports ldl-c and
world layout report layout what does
that mean for you well you don't have to
change anything if you have reports
already available they're gonna just
render fine on the web client also the
new control is fullscreen and responsive
so we try to utilize the maximum amount
of space available
also we scale in any reasonable
or form factor we also support different
page sizes and pictures and custom fonts
so not limited we don't want to limit
your creativity when you create PDFs or
reports one note we have not done any
changes on windows client so windows
client is still using the old control
and the new control is available on web
client and mobile and that's right it's
also available on mobile the same great
experience is also available mobile we
created a new control which works on the
web client and in the mobile you will
get on mobile you will get the smooth
rendering same smooth rendering
performance and also intuitive touch
controls like pinch to zoom panning text
yeah and so on and so you can have an
uncompromised experience while we're
gonna go in the office anywhere it just
works ok so let's see how this works on
in practice on an iPhone so again I land
into a role center I will pick a report
which we already seen just to show you a
comparison between web and mobile so
I'll pick top 10 customer report and I'm
gonna hit preview and again you'll see
the same flow server prepares the PDF
document and we're gonna see it up here
on the mobile client and you can see
here it's just as beautiful ideas as was
on web you can see the same richness I
can pinch to zoom and it's as crisp as
it was on mobile the graph looks fine
it's colors colored this line alteration
everything I can also pan if I would
have more pages I would flick to scroll
and since it's this is a mobile
experience users expect a bit more than
we had on a web and we are tapping into
native possibility native API which
allows us to tap into the native iOS
sharing
Payne where you can either send this PDF
to your friend or co-worker over email
you can send it on Facebook Messenger or
you can maybe using slack or Microsoft
teams you can also print it if you have
already set it up a printer on your
iPhone again enough it just works
because it's it's tries to coexist in
the platform and use the best
capabilities we can yeah let's jump back
to the slides and summarize so the new
PDF control the report preview and print
control is available everywhere so it is
exactly the same in the web client and
in the mobile you'll get very similar
experience it is embedded in meaning
that you don't have to install any extra
apps or plugins to use this
functionality it just it is inside of
nav and you can immediately use it it is
interactive so we adapt to the platform
via I in and try to use the most
capabilities we can so on a desktop you
will be able to use keyboard shortcuts
or a mouse on a mobile device you'll be
able to use all the touch touch touch
gestures and also modern this it was a
great start but we have some ideas how
we could build on top of this control
and enable even more capabilities so now
we have seen a new thing from about
platform but that's not the only thing
and now let's switch focus to Andrea and
he's gonna show us the new contacts API
you're going right yep thanks Thomas so
Mike's what that I'm seein if he tries
to provide the same experience
regardless of the display target you're
in it means that stuff tablet or phone
you're gonna say you're gonna get the
same functionalities that our objective
here
our motto you have seen a lot of great
stuff in my stop and Serena and on phone
as well thanks to Thomas and I would
like to stick with the phone in order to
show you some another cool functionality
we just evolved made available for you
and there is one scenario that we
decided to enhance
and that scenario is filling in the
details of a new customer it is a very
common scenario and it can take just a
bit of time it's one of those things
that you don't really like to do because
it might take 1 1 1/2 minute but still
you just need to fill in the name the
email some numbers can we just make it
faster the answer is yes especially
considering the fact that those
information most of the time are already
in your phone inside one of your
contacts sometimes actually many times
the customer you're trying to create all
the information for the customers are
already in your contact list so many
times what we see is that customers try
to fill in the information for a new
customer and they they need to switch up
on the phone to get the contact and copy
something copy the email address or copy
the phone number and then paste it
inside a Microsoft Dynamics NAV which is
a bit wrong so we can sure announce this
and that's what we did so let's have a
look at that so let's switch to the
phone and let's bring Microsoft Dynamics
NAV so oh here's your awesome report but
I don't need that what I need to do as I
said is I need to create a new customer
so let's navigate to the customers list
and let's add a new customer just place
the developer of these of these
application created an action for me in
that action is as you can see import
contact as soon as I click on the action
the Microsoft Dynamics NAV is able to
actually talk to the device and use it
the capabilities of the device is able
to bring up the context the contact list
so I can just pick one of the contacts
yes then let's add Stan and Stan is
there now so I'm just importing the name
in here but basically what you can do is
in CIL you have the ability to get
all the information from the contact so
all the data all the fields from your
contact from your device are made
available in CL so you can basically
transfer all of them inside the fields
of your page and that is pretty easy
actually and I'm well I'll show you that
but first let's just go back to the
light and try to understand what is the
pattern behind it how we make these
possible and in my opinion that is the
best part
nothing really new for you to learn
because it is the same product we are
just handling we're just dealing with
device capabilities it is the same
development paralog that you are used to
do you remember two years ago on this
stage together with me you coded we
coded together the the the camera API we
use the camera we interacted together
with the camera and the geolocalization
as well so it is still the same paradigm
because this is available as a client
extension so nothing really new for you
to learn nothing new to learn it's just
very fast and since I want to prove that
to you we're gonna do that again
together so as it happened two years ago
I'll try to do some CL together so here
I am now I am a CIL developer no more a
user I am a developer and I want to to
actually have this functionality in my
application so what I do I just get get
my customer card and I design it perfect
I want to create a new action so I don't
know all the shorter shortcut keys
unfortunately so please be patient all
right
let's create a new action interaction is
of course import contact
and there we go
since I'm working on a phone I want to
make sure that the action is visible
there in the action pane so what I need
to make sure is that these action is
actually promoted so I may get promoted
with a category spine and I make it be
so I make sure that I make sure that
that action is going to be visible in
the action pane perfect next let's start
writing some code alright our awesome
environment is ready who remembers what
is the same thing we need to do what
what's the thing we need to do here now
remember same paradigm what do we need
again code unit wait that's too
complicated I couldn't unit dot map what
do you mean precisely sure yes thank you
good so exactly as your colleague was
saying we it's the same part agamous
before you need an entry point and that
entry point is just available there's
gonna be a dotnet type and subtype
clinic sanctions so let's let's do that
so I remember some shortcut keys here
yes so I can create a variable and I'm
going to call it the rise contact
provider yes it's a dotnet variable and
I need to make sure that this variable
is actually a client extension so let's
pick up the assembly so I'm going to get
the list of the assemblies available for
me and I need to make sure to select the
client extensions so where are you
Microsoft Dynamics NAV client extensions
if you see that just up in here yes
thank you all right
there we go of course as soon as I
select the Assemblies I get all the
objects available where and the one I
need the entry point that I need is the
device contact provider I click okay my
variable is ready so I have my entry
point perfectly I got my entry point so
I can skip it I can move on I mean and
the next thing I can start using it so
the first thing I want to do is I mean I
want to to start using my object and I
can just go and call the API right well
is there anything else I would like to
do first check it what check check what
if I run a phone not really
that's not what I need to check no not
client type
precisely thank you so you need to make
sure that where are you oh thank you so
it is correct of course you might want
to track your own phone map you do that
by making the action visible and and
acting only visible property what what I
wanted to stress on is the fact that you
need to check that you have permission
to access the contacts because a user
the first time you didn't see that on
the demo because it was not my first
time to access the contact list but
you're going to be prompted the first
time the user is going to be prompted
whether he wants her now to give
permission to match the Dynamics NAV to
use your contacts and it makes perfect
sense it makes perfect sense they might
say no so you need to talk accordingly
so the first thing you want to do is
check in these yes I will close it don't
forget it alright so now I'm sure that I
live in the code only if the user
provided I mean gave me a green light
basically so now I can really use the
object and I love intelligence the first
thing I do of course is creating a new
instance of the device contact provider
so I can use it as soon as I have it I
can request a device contact
perfect am I done
no because as the name implies this one
is in a synchronous API right so there
is a second phase and the second phase
means that there is I am an event
handler some work and who can tell me
what mistake I made because this isn't
handler I will not be able to find it
why yes so yes we have many shirts where
are you okay
basketball yes when I was creating the
variable so let's bring that up again I
keep forgetting this I keep forgetting
this yeah I need to set run on client
yes and I also need to actually enable
events that is very important perfect
now I'm really fine because at the
bottom I will see that seaside has
created a placeholder for me where I can
react when the user is done and has
picked up a contact so perfect it means
the device contact that the argument
past that function is going to method is
going to contain all the information
about the contact no it's not really
always the case we need to check we need
to check the status
because the user can actually give you
permission to to have access to his own
contact list but it might decide not to
pick up anything or I mean something
else can go wrong actually so that's
what we need to check the status if it
is different from zero it means that the
user probably didn't select anything or
or hit cancel in the case the Vice
contact is no it's not going to provide
you anything no information because no
contact was picked up and in the case
you need to react for us it means that
we basically exit gracefully but you can
call something else you can show up a
message or do whatever you want when we
are done now at this point if we if we
continue then it means that the Vice
contact actually has some information
for us and what do you do you just
basically copy the information device
contacts into the fields of your page so
guess what I'm lazy so I already had
that in my clipboard because it's not
really rocket science here you need to
copy a string and that string nothing is
nothing more than as I told you the
fields inside the contacts provided you
in device contact so preferred name and
prefer email in this case it's just a
very simple a very simple example
I'm just copying the name and the email
and that's it I'm transferring the
information from the contact into the
fields of my page and of course if I
want these to show in the client I need
to call update and that's it
nothing else so as I promised it was the
same as two years ago we did the camera
together and we did the geolocalization
same part AG simple synchronous API
there and I think that concludes my demo
for these so we can continue
yes all right so so far you have seen a
lot of cool features and we have more to
come but actually what has happened
behind the scenes is that we have during
this time we have also reacted we
architected the web client stack in
order to provide a great experience for
our end users in the cloud so let's take
a peek under the hood the architecture
and platform improvements we have been
working on during this year so if we
think about the architecture journey
that the web plan had so far right the
when we have introduced the device
clients our main focus was on
responsiveness and that is why we have
shifted to a single page architecture so
what does that mean
that means the HTML CSS and JavaScript
are retrieved doing one single page load
and there is no other page load during
the whole lifetime of this session and
that was the fundament for building
modern responsive web apps later on when
we have in 2016 we have started our
journey of transforming the web plan
into a provision that desktop client and
we have done around 1600 right and along
with that we have also rewritten the
rendering engine to run on the browser
side and that has helped us a lot with
the scalability of the web server and
also it improved the performance of our
mobile apps on a high latency networks
and this year the focus has been as I
said the cloud experience and also
vinson has touched that during the
keynote so we have been shifting to a
micro services like architecture so what
does this mean for web that means that
the web client now runs on asp.net core
stack in an azure service fabric cluster
so let's take a look at let's take a
peek at how our start looks in the cloud
today this is a bit similar with what
you seen in the keynote but let's not
vary between in detail rights
notice that on the right hand side of
the screen you have the service fabric
cluster and in there we have the three
micro services the web client the nav
server and the monitoring agent and
let's understand what do we gain from
the micro services architecture
basically when we have shifted to cloud
right we have not only changed our
mindset but also it has also changed the
way we design and we architect the
components and also how we deploy them
in the cloud and parameters like ability
to scale on-demand availability of the
service has become more important than
ever and this is where the micro
services approach it helps us because it
it takes a monolithic application like
ours and splitted into finely grained
loosely coupled service components and
those service components can now be
upgraded and scaled independently so it
improve it improves a lot the efficiency
of our service and along with that we
have also improved the security of our
service and we have done that by
introducing the application gateway
basically it maybe sounds very technical
and but what it does really it is a web
dedicated application firewall so that
means that our our web plan endpoints
are protected in the cloud against
security vulnerabilities and and exploit
even more and our end users don't
interact directly with the web client
endpoints but now that we have you know
an understanding of how our stack
looking looks in the cloud today let's
talk a little bit about the service
fabric and what we actually gain from
from running on a suicide cluster so as
I said fabric the intention music is
that is a platform that simplifies a lot
the process of building and deploying
micro services and it does that because
it takes care of the inter-service
communication and also the the earth
handling right and it is important to
note that addresses have brick powers
today many of the Microsoft online
services Benson also mentioned basically
as us equal DB Skype for business power
bi
curtain IP and so on but what it was
important for us was primarily the
automated upgrade process so that means
that our platform today gets upgraded in
around four minutes to a new version and
during this upgrade there will be no
downtime that our users will experience
so this has been a great feature for us
because it gives us the ability to roll
out new versions and new hot fixes a lot
faster also we have a great also as a
fabric has a great failure recovery
mechanism and a load resource
distribution mechanism but coming back
to the web client and why is it that we
have moved to a nice without net core
stack the primary reason was that the
web client on the asp.net would not was
not able to run on a service object
cluster so that is that was what our
main driver for for being on the on the
asp.net core but besides that we also
have gotten a lot of benefits are out of
moving to to the new stack and let's
talk a little bit about those so as we
turn that core just in a couple of words
right it's it's a web web development
platform and what it does it actually
allows the web developer to to write the
application once and then it can deploy
it seamlessly either in cloud or
on-premise on docker images and whatnot
and by using and by doing that that we
have achieved a seamless transition of
our web app between on-premise and cloud
also the current SP dotnet core platform
supports multiple hosting types so what
does it mean it means it has to support
for a couple of web servers so we have a
Windows dedicated web server web called
web listener and this is what we are
actually running on in the azure service
table cluster then it also has a
cross-platform web server called castrum
and it also supports
the good old ayahs which we'll still see
on the on-premise installations with the
new stack and another another thing to
remember is that this video net core has
really good performance bench benchmarks
you can go ahead on the internet and
uncheck but basically I can handle
million of requests per second and also
another interesting aspect is that it's
a cross-platform right so that means
that this opens the door for us to be
able to potentially run the web server
on a Mac OS or on Linux of course we are
not there just yet there is still a lot
of work but at least now we are on first
platform stack getting closer yes I know
you would love to have on my clothes
right yep ok so now let's talk a little
bit about what are you going to
experience when you install the new web
server components on premise
so the web config file is still their
bodies in its very light so right now
the settings are actually stored in a
JSON file called nav settings that JSON
you will also see no more SPX pages so
if you would like to access as
previously be the phone and tablet
client in the browser you instead of
saying slash phone experience you just a
slash phone / tablet also we have done
enhancement to our partial scripts the
most notable one is actually that now
the the web server can be deployed as a
route side so what does that mean that
means that that now you can have a
simpler URLs for your customers
previously you're tied up in a certain
structure like NCP dynamics now what not
now you can choose to have your your web
your novel web server installation at
HTTP localhost if you choose so and the
new bits are going to be available of
course in the nav 2018 and they were
also available in the city beautiful for
some of you too to try them early on and
give us feedback ok
so that concludes the under-the-hood
talk and now as usual we also provide
you with a glimpse of what's coming
which is the most maybe interesting part
the best part yeah Peters or what's nice
I don't know it's hard to choose what's
that supposed max yes so at a high level
what are our intentions our intentions
is to of course continue on the
Microsoft services journey so we plan to
take advantage more and more of the of
the actual capabilities and we have
actually currently working we're
currently what can you remember the
three micro services we're also
introducing a new one which you will
basically search the HTML CSS and
JavaScript independently of the web
server we will also be optimizing the
clouds and are useful for end-users so
for those of you who actually tried out
the dynamics you simplify for finance
and operations how many of you okay I
see some hands so you know that the
tenant URLs are our DNS based right so
you have to all the time book more than
one remember them what we will be doing
we will be introducing a single URL to
sign in for every user so you don't need
to bookmark those URLs anymore you'll
have just one single URL to access your
your finance and operation solution and
of course along along with the cloud it
also comes the investment you know in
the powerful user experiences so what
are we what are our plans there right so
we plan to and reach the personalization
even more you you notice that there are
some gaps and we plan to cover down
those we will also be focusing on on
accessibility and productivity features
features like like keyboarding we have
seen a games of the hour get more
improvement but there are more to come
and we also plan to focus on
accessibility we will of course
continuing or integration with office
365 of course we can go ahead go ahead
and watch tomorrow the office
five session with your Kenny and lastly
we will also be focusing on updating the
look and feel because we want our client
not only to be at the island and perform
well in in cloud but also look modern
hey you say no more that's my part don't
spoil okay
so UX refresh let's start from one basic
fact and that is users every year expect
more and more from applications great
visuals more productivity more
simplicity and with these in mind we
decided to start an effort in the client
team to restyle our UI for our HTML
clients this is this is very important
I'm quite excited about that because
it's basically about changing the look
and feel of our application and the
desktop client tunnel client phone
client are going to be impacted
we call this effort UX refresh and I
think in a keynote you already heard a
little bit about about that but the
point is that in this session as the
last demo for you we want to enter a bit
more in details about your X refresh
especially in the consideration that we
are going to offer something very cool
which is steaming yes the ability to
define your own color palette in
Dynamics NAV why that because it is
important for you to make Microsoft
Dynamics NAV closer to your solution you
want max with a nice nav to look more
like you and with that in mind we
decided to start supporting theming and
guess what UX refresh
the new layout is all based on theming
so what we are doing the effort we are
trying to put on is act on our controls
our set of controls and parametrize all
UI related parameters color thumbs and
the style so that you will be able
to change them we have taken the first
steps towards these final destinations
so it's not like today you're gonna get
that we're gonna get there slowly and it
is a big effort so let's start by
looking at some visuals here the Ross
center one of the basic principles we
have in mind as we are rearranging the
layout he's making space for what's
important and you can see already a few
changes here we put focus on what is
important in the page and we make less
prominent what is not so important in
that context in that in the context of
that particular page type and also
device and also display target because
the effort is spanning across desktop
tablet and phone so you see bigger
numbers because that's where you want
the user to draw his attention actions
were armed actions there they've been
moved so we have moved them in a
contextual area we have a new paradigm
and your common bar on top so they're
still there they didn't disappear they
just differently reachable and there is
another thing you might notice here the
navigation pane the navigation pane is
no more basically because we saw that
dedicating the side area to the
navigation wasn't really correct
let's make space for data in content
which is the most important thing the
rest will flow so we have a new paradigm
for navigation which is the new
navigation bar on top we are still
working on that as we are designing the
new navigation product but it's it's
it's tough work but it's very nice is
when I come up beautifully and we are
also using input from you yes let's have
a look at a list page these pages have
the same principal layout the centroid
and you might see another
changing here where our boxes again
taking a whole side area just for
boxes seemed a bit wrong importance
space to content and data the rest of
law so we have taken out boxes from
their usual side area and we put them in
a different area in these places in
these pages which is in contextual areas
now you will be able to bring up
boxes by using the context menu on each
single row in lease pages card pages
let's stay on boxes because you see
that boxes in here are displayed
there no more on the side as before but
they're on top we have created a new
header section for fact boxes are
actually for card pages and in there you
will see a summary of your entity can be
an item it can be a customer but you
have the key matrix and some the key
numbers that provide a good summary of
your entity and then box is
actually useful so we move them from the
side and we decided to put them on top
while the rest of the layout is pretty
much the same even though we still have
some different paradigm in here where is
the ribbon if there is no more ribbon we
are working on that so you will be able
to place your actions in a different in
a different area which is the command
bar still working on that but that is
where we're headed and the best thing
which is what I want to stress on is
that everything is much of this is based
on theming so the new colors new new
fonts the new style most of them are
FEMA ball so later on when we will be
able to roll this out for you you will
be able to take your own color palette
and apply that to Microsoft Dynamics NAV
and I'm not joking on this we are we
already started our effort for that and
we have started gradually not rolling it
and I have a little treat for you guys
so I can just provide you with a little
take peek of how the new UX refresh
looks like and the seeming looks like so
we can bring up arena the the colors as
they are now and you will see the new
colors for the eggs no no that's wrong
now that is my personal theme that's my
personal theme that's not you extra
fresh that's Andre Tino's personal thing
well you see that's my theme so I define
my own colors it's pretty pinkish but
that's fine to me so you see Charles is
different new colors are on Tyler's you
will be able to define your own in ten
colors and apply them to the UI but
that's not really what I wanted to show
so let's bring a new colors the real
colors for you extra fresh okay so
that's how we're gradually rolling it
out so at the moment you see that many
of the paradigms that I introduced are
not there
navigation is still there ribbon is
still there because we are working on it
we are gradually changing all of these
and gradually with the updates as well
they're going to be made available for
you to try and to experience so I really
hope you enjoy you will enjoy this and
I'm really sure you will and I'm looking
forward to see how Michael Ranson IV
will look like in your own specific
solutions so looking forward to that and
that basically concludes my demo here so
we have now 15 minutes for your question
a bit more than that for your questions
[Music]
I questioned about the UI there's been a
lot of questions about it already but
the possibility to drag and drop the
width of the column our clients what
width of the column Jeff yes where we're
working on it yes no no
sorry no promises yet no no I mean in
the short term yes you can just throw it
out hello you showed us the personalized
personalization of the of the user will
they also be able to personalize the
profile the web client so today in the
indian after thousand 18 you are not
going to be able to personalize the to
have profile configuration okay through
the new technology right but if you
create the configuration profiles in the
Windows client those will be applied to
the web as well okay didn't see it quite
as well but did you just drag a field
from the invoicing register to the
general register in during the
configuration of the page yes because I
think that it wasn't possible in the
last versions so this is a new feature
between the registers between the first
absorb yeah yes yes okay this will also
work for the VINs client no experience
is primarily on the Windows client right
so we have not touched the
personalization on Windows right okay
and when a personalized my Windows
client will the changes be affected on
the on the web client no so the thing is
the moment the moment you start
personalizing the web right then then
windows and web would be to separate
personalization right because they are
based on two different technologies so
you'll be able to run with them parallel
okay and the last question is it's just
a new preview of the after after
printing and printing in the Windows
client you can have a dynamic sorting
you can change the sorting of the rows
as this is a PDF I think in the web
client yes you are right it's not going
to be available you know directly in the
report for you but that is also because
we believe that the sorting the ad hoc
sorting can also be done to other tools
like Barbie or Excel for instance right
you can always export Excel under the
sorting okay mm-hmm good thank you
maybe it's just a definition question
but I'm wondering is the desktop client
the same thing as a Windows client was a
desktop actually the wet line so the
desktop for us is is is both actually
and primarily the web client right and
the Windows client it's basically as I
mentioned in my in my you know overview
of client technologies right we are
aware that users are still very fond of
it and it's probably going to be for a
while but but actually we intend to you
know have all the features being
available in web plant as well because I
can remember I think it was two years
ago Android actually had this Windows
client actually dropping off the
PowerPoint sheet at some point in time
no no it was year or one of the other
colleagues but there was quite
forcefully stated that the Windows
client would disappear some point in
time and now I actually got the feeling
that it's got to be there for some years
to come yet it's basically it's going to
be there but it's not going to be the
client where we were going to invest
with the new features because it's a
different technology the Windows client
and the web client are based on two
different technologies and the HTML
clients are you know the future from
from our from from our technology from
our engineering point of view and our
customers actually because you won't go
on devices with the Windows client so so
that is where we will be inviting the
the Windows client will still be there
because as I as I as I said you know the
users are still fond of it right okay
one last question because there might be
a lot of other ones to ask questions of
course the pic card that I saw in the
key presentation and you showed again so
that's on the list so that's the new UX
experience and then the picker which you
have a list page and you just show some
sort of a sack box is that gonna be
populated with like for example the
promoter field sorry yeah if you in the
you action refresh the list page and now
you have this this small I thought it
was called a pic card I don't know for
sure but a pic card pick card
yeah like the car black box was was
showing up on
the lines in the list page yes are those
gonna be populated with the promoted
fields or working on that it's still a
work in progress but the idea is that in
the context menu on lines we will show
fact boxes for the actions we're still
working on that because it's about
rearranging a lot of elements so a bit
of working progress there cannot really
tell at the moment thanks over that high
grade work on the refresh I'll see
whether client I have a question
regarding the filtering what is still
some kind of hassle in the web client
right now because you can't do the some
filtering totals yeah yeah and you
cannot filter on columns that aren't
shown in the list mm-hmm and that's
somehow that's the main reason that
stops my co-workers from working this
web client although it's great but
that's some some some kind of a big deal
I don't I don't think yes so so yes
definitely the the advanced filter it's
an experience that we will have to
provide also in web right and whether
that's going to be that we will think
about how how how to render the
delimiter tulsi in the new UX refresh or
it's gonna come later we haven't decided
yet right but coming back to you to -
you're saying to your your statement
that you currently blocked to my
knowledge the limit totals can be
applied also from the application
filters rights you can always have an
application action that applies ditalini
Toto's i know that that's not good but
but at least you know until you and
block your scenarios and
actually finally get to the advanced
filters okay it would it would be great
if there were some some method to reset
all the filters because when I said some
filters from the code and I want to
remove these things that just can do
this without hitting or making another
action this feedback in mind I think
also the mind and the interesting thing
I mean I don't know about you guys but I
mean well you know I was in a Navy
actually when we roll out the digital
Taylor client right in in 2009 and also
the advanced filter in Windows kind was
also not sought to be ideal at those at
those times in 2009 so I think right now
what we're trying to do we're trying to
find a way to provide a good experience
for for the filtering as well it in
terms of you know being because I think
the complaints when we had the advanced
filter for the Windows client that was
that people were users were used to
sucide which which was a very table
approach and then we moved to this
control which was hard to use and not
very friendly right it's a big control
so we for sure don't want that kind of
experience in the web client so that is
why we are not writing and just saying
okay let's let's have the advanced
filters right now right so we need to
think about how the experience would
look to satisfy both the you know
simplicity needs and also the
proficiency okay thank you okay so it
looks like that box is not working he'll
go back to you when we said that we
could change the profile on the fly so a
user could say which profile they wanted
to to select is their only protection
around which profiles they can see to
select is there any permissions around
that in the my settings page yeah you
only see the profiles which you can pick
so is that a list of all profiles is
that sorry it's not in my settings it
doesn't show all the profiles that shows
the profiles you can select okay and
do you control sorry which ones you can
select is that permission-based okay
hello regarding the report viewer PDF
report viewer does it use printer
selection I mean this configuration for
user so the configuration is done on the
client side in the native side so if you
have a printer configured in your
browser that's that's how it would work
or on a phone so user has to configure
the printer in the browser in the native
browser experience so it works like in
any other page when you want to print
the page right so the user has to go
into browser settings and set up a
printer yeah
an IL code they said we're not
supporting dotnet so the exact examples
she showed us on getting the camera
providers is that still going to work
the way you coded it was that going to
be different in il code sir again the
content not the camera alright the car
basically used a dotnet you get the
camera but we were told may all code
they're not supporting darknet anymore
so does that apply to that those
functions or first gonna have to be done
differently so you're talking about the
new modern dev modern dev experience
right yeah I mean there were there is
some discussions today about how the net
objects will you know be replaced and
and we don't have right now and answer I
think the team is still working on so
for now that that's sure supported so
you can use that so when the the new
experience for developing is going to be
rolled out we will say because I think
the AL is ready gonna be available with
the new release for doing extensions
also you are wondering if this is we're
going to be possible to be
in an extension right right yeah not
currently but we're working on it yes
the the accessibility API like Cameron
TPS will will be available I got a
customer here all the way up here the
action images will we be allowed to
choose our own or are we still limited
to the ones about that UX refresh no
it's Ted Thank You layout no it's just
about the action images if I have a have
an action I'll put an image on the
action and push it and I can see what
action it is but I'll be able to use
another image for my actions like apart
from those available in the list in
Seaside right yes yeah no no but we know
that that's also a feature that that our
partners wants okay question for the PDF
functionality is it possible to use to
preview PDF but as taught in blob field
start with status PDF function in the
blob so that I can use the new functions
and browser to preview the PDF would you
like to change the PDF after it get
generated to the server like archive
just do some operations on the PDF or so
I stopped the PDF in the block that's an
archive and now I want to view the PDF
in the browser okay No so basically
we're talking whether the PDF view or it
works only for reports or you can also
use it for PDF documents not currently
so it is primarily based on the under
report data okay hello I'm here just a
quick opinion about UX refresh and
removing the boxes from the right
pane and move it to the contextual money
so it's a one more click for the user to
reach the data maybe yeah maybe it is it
is one step backwards because when you
have it on the right pane you can click
with down key on the list but depends
from the point of view so how are you
exiting we we investigate on what users
what actions users do the most in the
context of certain UA areas when it
comes to least what we noticed actually
by by seeing users using the product is
that they spend more time they want more
space for rows yes so and that's the
thing also we collect that every time
you also in the cloud where when you
actually collapse the fact box so we see
how many times users collapse and leave
the fact box collapse all right so we
have this data and we could be we could
see that users were spending more time
on the content so we know that it's
actually more important for them to get
the content rather than the fact box so
we decided to move the boxes into
the conceptual area it was also the fact
that we sometimes have different types
of hot boxes right sometimes we have
four boxes that reflect the overview of
your list and sometimes you have four
boxes that reflect the data on the row
right so it could be that we will go
with two different approaches where the
ones that you will see in the context
money are the ones per row and the
overview will still be able to see it
somehow somewhere else right right so
we'll have we'll have this in mind yes
believe me we'll have it okay thank you
okay I've got a question so you say okay
we remove all the facts books so the
customer has more space to see fields
but then my question is okay do you see
really more fields because when you are
adding a field the maximum is two fields
on one line all you need to make let's
say make three or four but is it a not
not easier to say okay if we want more
space just change the length or put it
where you can as like in the classic
again our UX team has done research on
these so we have data that indicates us
what the best approach was so we could
we could see that users were spending in
lists so I see that you are referring
more on lease right yeah also on cords
because now I don't card you didn't lose
the fact box if they're on top now
actually were there where you have a
header so you can have a better summary
of your entity but but now the problem
is with end customers you need always to
scroll down to see the information on
the fields of the fields that are
available but if you let's say if you
have 10 lines with two times no five
times two fields is that not possible to
put four fields against each other I'm
sorry you need to repeat the question
because how are we going to optimize for
the space for the vertical space okay so
now okay let's say you have 10 fields on
your own a card so it means it's always
five lines so okay you be removing the
fact box okay so you're making your
creating more space but you don't create
more space it's just the language of the
fields and it's growing so what is the
benefit to remove the fact boxes I don't
see the benefit to be honest
because the visibility of the customer
stays the same when you open it it
doesn't see the fact box okay it's
bigger but yeah that's true for this is
specific for card pages right mm-hmm
yeah so in the new layout for card pages
we have decided to create a different
section for the summary of the of the
entity and that's where we thought that
fact boxes were more useful also again
by making some research we could see
that users spend some time in those
areas or not but with the specific case
of card pages we have created two
different logical areas because we
wanted to separate the data of the
entity from the summary and we wanted to
create this horizontal separation and
that's why you see them now in the in
the header area so the my comment about
in this case for more space to data is
actually to be applied to lists yes
that's true on car pages you get fields
with a width which are a bit more
expanded now fair enough
but not least only spade use it really
pays off what I mean general we will be
actually running usability study quietly
and that is why you know your difference
will take some time it's not like you
will just you know roll it out so we'll
have all of these considerations in mind
also what we will have in mind for the
UX refresh is it's not changing too much
the metadata or not changing you know
our goal is basically to you know for
you to get this new experience without
having to change the application code it
could be that maybe for getting some of
the optimized feature you will have to
add new properties or use new properties
but in general we won't be for example
asking you to do you think you know the
metadata on the ribbon or on the on an
application paint and so on if it is it
or not not oh not at the same question
as the others are mentioned can it not
be possible that we define the length
instead that that a system is doing
creating this the length himself these
are yeah so this this is all in terms
usability so the layout that we have
today is based on the research and the
data we have now and keep in mind that
we are still working on that so we will
see basically this is all what's next
remember right it's not coming you know
just not okay we're running out of time
but do you we can take your question I
think down there but here yeah if you
can I have a question oh okay sorry okay
so it was on the saved
well actually the advanced filtering and
I was thinking about the save views that
you could create in the past or you can
create in the old style windows client
wouldn't it be possible to bring back
views as a way to create advanced
filtering so that's more of an
experience saying I want to create this
view with an advanced filter save it as
a view yes so definitely we will be
addressing the side views right the
functionality we are aware that two
together with the advanced filter the
side view is also you know on our minds
right and I think that the way we look
at the save use is also we look at it in
the regards of of having the new
navigation pane component in the UX
refresh so we'll probably have this in
mind when we are designing the new
navigation component for for us refresh
thank you hey they were a quick question
up here in the middle you talked about
the use of personalization and
configuration is a correct understood
that the configuration mode can only be
handled in the windows client and you
know the user configuration can only be
handled in the web client so the new
functionality about moving feels between
fast apps will only be available in the
web client right so
you can personalize today in Windows
client right so the personalization in
Windows client has actually quite quite
a rich set of features today that we're
trying to reach parity with it's just
that the drag-and-drop paradigm and new
technology is only available in web
right excellent
and just another question about the
shortcuts in the web client at the
moment and understand the Willis clan
may die at some point which is fair
enough
but you sure control-enter for doing one
shortcut in the Windows client and it's
another in the web client and just
general shortcuts the question about
this are you going to be able to apply
this and web client into the point I
think of account into a constantly oh
yes so so definitely we are working on
on keyboard shortcuts right we have an
hour and actually our or first approach
actually is to look at the keyboard
keyboarding Ingrid's today I think the
web client does not have you know all
the goodies that the Windows client has
in terms of control home control and
shift control home shift control and
this is this is something we're
currently working on so it's it's
definitely something we're going to
support thank you yes okay
thank you very much for attending
