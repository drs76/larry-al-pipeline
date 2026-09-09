# Microsoft Presents: What's new in Business Central clients for AL developers

- **Source:** https://www.youtube.com/watch?v=mr7WEzzxEnI
- **Video ID:** mr7WEzzxEnI
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 43m43s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

right so welcome to our session it's
called what's new in business Central
for
clients uh clients for Al developers um
I'm Thomas gasas I'm engineering manager
for business Central client team that is
responsible for web and mobile clients
and with me today I have my colleague
clao uh he's engineer in our team very
busy right now setting up things uh
great and he's going to provide that a
bit of technical backing as in the last
session we had a a PM here I'm a manager
and I have a backup engineer as well
always come into to always have your
co-pilot pun intended uh okay so what do
we have for you in this session we're
going to cover a lot of new things that
are uh have been released in mobile app
uh we're going to cover at least uh one
and a half releases so the 24 and 23
that we added and then enhanced so
that's Barcode Scanner worksheet Pages
uh some support uh enhancements to
mobile app as well and then we're going
to take a look at the general platform
improvements uh that we have done in the
web mostly web uh clients it's going to
be a bit of overlap what just Stefan
showed but we're try going to take a
different perspective we we're not going
to focus so much on Al code we're going
to take a look at the ux perspective and
what considerations you should take when
designing and making different uh
decisions how you use those properties
okay so cloudia you ready yeah okay
maybe before we start it would be nice
to know how many people actually using
the mobile
app well okay not that many but uh yeah
the beginning of this session is going
to be about that so uh previously at the
the previous BC days conference last
year we introduced for the first time
the barcode the scanning capabilities in
business Central and since then we've
been doing a bit more work on that so
now we support native barcod scanning
capabilities in the app and in it works
on all supported phones tablets and
camera via camera it uses the native
mobile OS capabilities to detect these
barcodes and decode them and we also
provide an integration with dedicated
Android Barcode Scanner devices and of
course we build these features in such a
way that you as partners can extend and
make them
extensible yeah cloud is it mobile only
for now yes uh it works only on mobile
and tablet of course for the camera but
maybe in the future we're also going to
add a possibility to have this
capability on the desktop client as well
yeah I could imagine I could use my
Surface camera maybe
yeah go you want to switch no just
perfect in terms of the supported
barcode types out of the box we support
most of the wellknown
1D uh and 2D barcode formats um so we
have kind of two types of uh barcod
functionality one is through the camera
so both IOS and Android they have as you
see in The Matrix they support some
certain barcode types and then when it
comes to the L dedicated bar Barcode
Scanner that's something that maybe you
should check with your
manufacturer what about is there any
setup I see a pretty long list of Barco
scanners is there any configuration no
there's no configuration out of the box
you just have to call a method in Al and
then uh yeah we're going to take care of
everything for you so it's simple as
that
nice good um in terms of the
capabilities we divis them in three
scenarios one we make it so easy for you
to just add an action to a field which
can instruct the mobile client to just
uh yeah start the camera functionality
and SC scan a barcode so that's scen
scenario number one for scenario number
two it's based on the same functionality
as the previous one s number one uh but
we made it so that it's extensible so
therefore when you actually get a value
from the barcode functionality then you
can actually process it in inl and then
SC number three it is uh about the
integration with dedicated barcode
scanners okay so let's talk about
scenario number one as I said it's very
easy to add an existing page or a new
page um all you have to do is annotate
the field of type code and text with a
new property extended data type equals
barcode and then uh this will instruct
the mobile client to just show the bar
code scanning Button as you can see in
the image uh on the slide um yeah and
it's going to be rendered with whether
uh your device supports this capability
can we actually go now in the
demo perfect so just let me show you I
have created a page hopefully this works
nice I've created a page a very simple
page which has this
capability um sorry just need to go back
scan but and then I have two fields on a
list page and as you can see both of the
fields support this scanning action so
if I'm clicking on of one of these or
tapping on one of these action
then the camera functionality is just
going to pop up and I can just scan this
QR code and yeah well he detected
already that data exchange and if I want
to update it you can see there's a
barcode value that has been added to the
associated field on which the action uh
was uh annotate if we go to the visual
studio to see how the the page looks
like this one it's pretty simple as I
said all you have to do is just annotate
a field in this case
barcode field one with the extended data
Tye data type barcode and then this is
going to instruct the client to just
show the specific action so just to
understand how does this work so you the
field but how does it work behind the
scenes it's just text input to the it is
just it is just a text input that comes
from the camera but if you want to do
some more advanced scenarios when you
want to actually process uh the barcode
and maybe find items in your database or
something like that then we can go to
scenar number two uh maybe just perfect
nice thank you uh so scenario number two
invokes the same capability that you've
seen previously is just that we made it
that it's extensible and you have to
code specific Al code for that it can be
started from a roll center queue an
action a button a link or some automated
Logic for example when a page is open
and then when you scan something it will
return the scanned barcode value to Al
for for the processing and also have a
demo for that I'm just going to go back
to my mobile go back to my page let me
just full
screen so I created another page camera
bod SC sample and then in this case I
don't have any field uh which has the
extended data data type property on it
but I have created simple action that
triggers the barcode
scanner and then as soon as I press that
action
then yeah the camera functionality is
turned on and now I can just scan
another bar code again and in this case
in the demo that I'm doing I'm just uh
updating the field with uh yeah the
incoming value from the barcode scanner
then if I'm just going to Al I can show
you how that works in order to uptake
this functionality you have to declare
on your page a user control and the user
control stes uh yeah a camera barcod
scanner provider addin this is something
that we added in releas
24 uh the addin has three triers or
actually Four triggers um one of them is
controlled in ready that is when the
page is embedded or the control is
embedded on your page then we are going
to call from the client this method uh
and you you'll be able to assess whether
or not the camera Barcode Scanner is
available on your device then in order
to call the
the the camera functionality all you
have to do in this section for example
I'm just calling request barcodes asnc
on that specific um user control that
you just declared and then if once that
happens then the functionality is just
going to well be triggered and if
there's a s successful barod scan then
the following trigger is going to be
called barcode available which has two
arguments barcode and format the first
one being the value of the barcode and
the second one being the format of the
barcode that has just been
scanned uh in the case whereas there's a
barcode failure then we are going to be
calling this uh method the barcode
failure method with the reason of the
failure yeah so in this scenario you're
really putting Al developer in control
like from start of setting up the
barcode scanner calling uh to initiate
the scanning and also then you're hand
fully handling what to do with the value
I guess I could imagine one extension of
this scenario is that in Warehouse I'm
scanning one code but I immediately need
to scan second code and third code is
there any way to support this scenario
in this full developer enabled mode yeah
so actually just add a comment for death
um for example if one of well some of
you had watched the BCL event uh the
previous two ones actually we already
support uh in the in the base app this
capability where uh depending on of
course how many items you want to put in
an in an order then the camera
functionality is just going to kind of
keep on popping up until all the the
items in the order is going to be well
added to to the order so you have you
can do this kind of continuing scanning
as soon as you get a successful scan
back from the the functionality so the
way you would do it you would just call
scan in a loop until certain condition
is met and then you can break the loop
yes that's correct yeah okay perfect
manager gets it
let's go to the next
one and now let's talk about SC number
three this is different from uh what
we've seen before this is an integration
with dedicated barcode scanners and
actually it hasn't really been showcase
last year at uh at BCT Tech days but
we're showcasing it now um it requires
configuration at the device level since
these are well third party devices it
supports continuous scanning while L
processes the incoming codes so you can
actually kind of think that already that
this uh capability could be used it's
really handy in Warehouse scenarios uh
the developers need to explicitly start
listening for incoming barcodes and uh
the way that is done is VI L extensions
similar to what we've seen in the
previous scenario uh where we had a page
with a user control and so on the setup
is done per page uh meaning that
multiple providers can be registered
however there's a small caveat and that
is only the current page or topmost page
will receive the incoming barcode um and
I have a d for that as well
actually
good and go back I have uh create
another page simple page which doesn't
really have any actions on it or
anything like that and then I'm just
going to use hopefully this works nice
I'm just going to use the laser bco
scanner which you can see I'm just
pressing a button here and then as soon
as I scan something you can here that it
was successful successful scan and then
uh you can see that the value of the
input field has changed and I also have
a count to Showcase The Continuous uh
kind of nature of the device and I can
just keep on scanning for example and
then just keep getting updated and so on
so this increases massively the
productivity of your Warehouse
users uh in terms of the AL
code the API looks similar to the
previous one you're going to have to um
declare user control that takes a barcod
scanner provider adding on your page uh
similar as in the previous one we uh you
need to declare whether you need to
declare the trigger controled in is
ready and then we are going to assess
whether or not your device supports this
capability then uh you're going to have
to call the method reest Barcode Scanner
async and in this case I'm calling with
with four arguments and actually I can
show you what exactly those four four
arguments mean if I'm going back to my
phone then I'm just going to go to this
so usually the way these parode scanners
work and the way we integrated with them
we are doing it through uh through
intense to broadcast intense and that's
something that Android support Android
OS supports
natively so first of all in order to
enable it you need to set up the intent
delivery to broadcast intent and then
you can can uh declare uh some conf you
need to declare some configuration
strings by default we need to have four
strings uh declared in the
application that's the way it works this
uh yeah this broadcast broadcast intent
functionality however my device does
does not really allow me to change all
of these four configuration strings it
only allows me to do to change two of
them and that is the intent action and
the intent category and then we actually
request if you see here in the code we
request also the data string and the
data type but uh since I'm not able to
change them then what I have to do is
check with the manufacturer of this
device and make sure that yeah I'm able
to retrieve this this content uh
constants and then when I'm calling this
method I need to declare the
configuration strings that you've seen
previously there is the intent action
the category which I just said and then
the constant ones for the data string
and data type
um similarly if your device actually
supports to change all four of those
then all you have to do you can just
call this method without any parameters
and it's just going to work and we
actually provide uh a documentation in
the documentation the four configuration
strings that you need to to change on
your device for uh integration with
business
Central okay I guess we can go to the
next one right so one question uh
Claudio I'm mostly iOS user so I have
many questions about Android so you're
saying there is certain hardcoded
communication protocol on on this
Android devices um is there any way like
I'm a business owner I'm trying to or a
partner who who's trying to recommend uh
a business to what devices to purchase
is there any decision tree I should use
when deciding what Hardware to buy what
it should support yeah you should make
sure that the devices that you support
support sending data to other apps
through broadcast intent and yeah it
allows you to configure the
configuration strings otherwise we are
not really able or you're not really
able to integrate with business Central
but most those devices would use this
way exactly most of the modern devices
they use they we yeah and I think it's
always fair to just I know request a
sample try it out see if it works with
integration and only then order
thousands of those
devices uh yeah okay good I'm going back
next
one okay so now uh probably you've seen
um for the ones for a few of ones
already that implemented the barcod
scanning functionality last year we
initially um added the functionality
using the client accessibility adds that
maybe you are used to and the way they
they used to be implemented was via the
do in name space and so on however due
to some technical limitations we are not
able to make those
available for SS
tenants therefore in the previous
release or actually the curent release
release 24 we introduced a new uh way of
updating this updating this
functionality and that is via uh a new
controlled in API as you've seen in my
examples this controlled in API is a
close system meaning is meaning that you
cannot really declare them it's us who
are declaring them for you in the system
app and currently uh we only provide the
control edins only for barcode camera
barcode scanning and barcode provider to
integrate with the
device um it is compared to the user
controls that maybe that you are used to
it is uess meaning there's no if frame
therefore the styling properties are not
applied and no additional scripts can be
provided it is really important to
mention that the net based API is still
supported so hopefully you are not
breaking uh any functionality that
you've built already uh but uh the truth
is that we plan to migrate allnet based
apis to the new control Adin and
probably with the upcoming releases we
are just going to keep on releasing
releasing new uh addings therefore we
strongly encourage you if you are to
take any uh new barcod scanning
functionality to use the new control
edin
API great so let me where a developer
head for a second is there any action
for me right now uh yes if you want to
well have any bar coing functionality uh
in your tenants then uh you should yeah
upgrade your your extensions but maybe
you can actually actually see an example
of how uh or comparison between the two
addings so for example here uh on the
left left side yeah go left yeah great
um you have an example of how the baros
scanner provider could be integrated
with the previous way of doing it via
the daret object it's more or less if
you can uh if you look at the code it
looks pretty much the same in terms of
the API but then looking on the right
side pane uh this is the new way to yeah
update the functionality using the
control addin and it's pretty simple
yeah didn't really change anything it's
just a different way of uh of doing it
and the nice part about it is that uh
you can use this functionality in s
something that you couldn't really do
before so
yeah awesome yeah thank you
let's perfect so now let's uh switch
gears we've been talking quite a lot
about Baron scanning um in the current
list we are also bringing you uh
worksheet pages on phones they represent
a simplified version of uh worksheet
pages that they're used to on tablet and
desktop they have a shorter header
section uh they display all the
worksheet lines they also include a pH
summary section and of course to Ed the
dat data one has to Simply tap on the
desired area and we are just going to
slide in another pane displaying the
data associated with the line uh it's
also really important to mention that we
haven't done any change to tablets so
therefore yeah they are still fully
supported and now um I'm just going to
Showcase how will they look like perfect
I'm just going to go to my
application I'm just going to open the
item journal page you can see already
the that uh in the header section it
displays the batch name field if there
were multiple Fields then you would
actually get an action like the one that
we have in the fura which uh when you
would tap on it it would just slide in
another another view where you could see
all your Fields then we have uh the
lines associated with this uh worksheet
page and then down below here we have a
full summ summary section and when we
press on that we can see the item
description associated with the page and
some fact box data which we don't have
any data but this is pretty much how the
UI looks like for worksheet pages on
mobile yeah one question is there
anything for me to do as an Al developer
um not really out of the box it should
just work the worksheet pages that you
already have in your application should
just work on a phone however we do
advise for you to check if the UI
suffices your needs and maybe you want
to look into Q groups to make sure that
uh yeah they look exactly as as you
would like them to look yeah field
groups because it's most likely that
those pages have not been exposed to
mobile before and mobile phone heavily
relies on field groups to promote the
right fields to the UI so you might
revisit the field uh the pages to see if
the optimal values are surfaced to the
end user on mobile probably that would
be the only tweak uh you need to do yeah
thank
you and last lastly for the mobile we
are also bringing you the help and
support page that maybe you already know
from the desktop experience uh so now we
actually enable access to help and
support page on mobile devices that is
tablet and phone and uh mainly um kind
of the main scenario that we are going
to use it for is for troubleshooting and
probably you as a developers are going
to be using it for the AL profiler and
if I'm just going to go and going to
show you how it looks like
it leaves in the well in the help and
support on your mobile under learn and
then I'm just going to click on the
action help and support and the help and
support page is just going to slide in
where more of the most of the
information that you already have on
desktop is presented here it's just in a
compressed format something that looks
good on
mobile and you can uh you can uh yeah
just uh click on different uh on
different uh actions like for example to
analyze the performance uh you could
start for example an an Provider by just
uh clicking on the start action I'm not
going to do that right now and also it's
important which maybe makes our life
easier for uh yeah helping your customer
when you report a problem through the
ICM portal for example um now they
actually we are doing and we're hoping
that more and more users are going to
use the mobile and tablet
applications um when there's an issue or
something uh usually we require some IDs
and S IDs and what not to troubleshoot
the problem associated with your user so
therefore we made it in a simple way for
uh for you to just copy the text below
by clicking uh by clicking uh the
information and then just share it with
us uh in the support ticket which is
going to make our life easier to help
you well faster uh and unblock your
client so let's say I am a person who is
about to create a support ticket and
you're the person on the other side
who's handle who's going to handle that
ticket what should I provide in that
ticket should I copy the details take
screenshots what do you prefer you
should uh preferably both actually would
be great if we had all the details
associated with that uh session and so
on and then also some screenshots of or
a video actually of what is happening so
we would be able to troubleshoot much
easier and much faster way and therefore
yeah just unblock your customer yeah as
always privacy first so we don't really
need any of your like company
information in the screenshots try to
blur it out uh if will really make our
life easy not to make sure to destroy
that data in the screenshots uh not in
the database in the
screenshots uh okay
so next let's talk about client platform
and what's new uh so we have talked
quite a lot actually across entire
conference right now about new things
we're adding but it's always good to
talk also about screen cleaning and what
we removing U because it makes our
platform less cluttered some things
maybe have D purpose or there's better
ways to do things and definitely there
is a better way uh to do things with
Legacy list views maybe it would be
interesting to know if anybody knows
about what legy views are and how did
they used to work like that would be a
good quiz before I explain what Legacy
views are could I could have show of
hands who know how list use used to work
we have one two
3 very
good then it's more likely that you will
also not notice that they're gone
uh so but just for sake of completeness
so how they worked um we used to have
this magical platform Behavior where
would would take a look at your Ro role
Center specifically into nav ation
actions and Q tiles and we would see if
you have uh many pages that are running
well we have run object pointing to the
same page then but you have different
run page views meaning basically you
have different filters um so once user
would click on that uh navigation node
action or a que we would open an
embedded list page and we would kind of
create these views on a side based on
the uh run page view filters you had
defined in R Center
I know it's a it's a it's a handful and
there were many problems with that
because uh if you would open the same
list page not in embedded mode they
would be gone and immediately there's
user question like where's My Views uh
that already creates a confusion um and
we had even bigger story of redefining
and redesigning Views and we basically
have completely a new view model and
that's what we want to encourage
everyone to move uh it have many many
advantages you can Define sorting you
can Define filtering you can Define
custom not custom but specific layouts
for those views on pages uh they also
work with design and personalization
subsystem so they are extendable as well
or customizable um and users can also
create custom views that was not
previously uh possible so just a small
recap this is from couple or three
releases before but on on the list Pages
there's Now new section called views and
there you can create uh view definitions
uh they can the simplest view is
probably caption and a filter uh they
can also have shared or non-shared
layouts there's a lot of details that
you can look up in the documentation uh
but even with such a small change we
took it really slow We monitored the
usage in production for probably two
releases uh you may have noticed a kind
of nagging message popping up when you
would open these Legacy views in the
previous release so we were trying to um
slowly nudge users towards the new model
and lastly with this release we noticed
that finally the usage dropped the
global SAS usage dropped uh below 5% and
we then felt confident that okay now is
the time we can decate them so I think
that was a good story of being slow and
just taking it easy and not introducing
any uh unnecessary
fuz cool uh let's go next to more new
things we adding so so uh Stefan showed
us how we can use the new instructional
um text property I want to go from a bit
different direction and explain some of
the design
considerations uh so in essence uh we're
trying to avoid data entry uh errors
data entry errors happen when there's a
mismatch between what user's mental
model is what he's going to enter and
what how the system is going to behave
and on the other side the developer
mental model what he expects the input
to be and the placeorder text is uh so
the general term more broad term is
placeorder text we call it instructional
text instructional text is an
opportunity to bridge that Gap and avoid
that error um there's multiple ways to
tackle data ENT errors of course you can
show a validation message but this is
already too late all user already made a
mistake uh he feels bad because system
is trying to correct him it's a lot
better to give him a hint what kind of
uh text or value format you expect uh
maybe some internal usage that is
specific to your implementation anything
that can help
user uh but it's not a replacement for a
tool tip uh they have different purposes
tool tip is more explaining internal
business details of what this field is
about and instructional text should be
more just about the shape of the data
being entered it's really just a guide
to the user um because there is an
important uh point about this
uh you should uh ideally provide both
the tool tip and the placeorder because
Place placeholder or instructional text
alone is not accessible so for example
imagine you have a person who is uh
blind he's primarily uh relying on text
reader uh to enter data in business
Central uh so play holder text in
instructional text will not be uh
revealed to him in the screen reader
because it's simply a value that is in a
field but is not really really in a
field so it's mostly a visual guide uh
to the end user so in order to be fully
uh inclusive and creating access
accessible Solutions uh you need to
provide both ideally uh field uh caption
uh field tool tip and optionally
instructional text that's mostly for uh
visually guided users who are able to
read and see the text and that will help
uh
them um yeah um I I will skip I will not
show again how you can do it in Al uh
it's it's one uh field uh that you can
add on on uh on page Fields so but
there's more properties that uh you can
set on on discretional text first you
can set lock to equals through that
means uh you don't want any translations
on this field uh practical scenario
would be the field purely describes just
the shape of the data imagine maybe even
semi sample value or some pseudo regular
expression in there uh it has no
language attachment so it would be
ideally fine not to translate this value
uh but if you do if it this part of
translation process it's it's really
great idea to provide a comment for your
translation team uh and help to make
sure that that intent of the
instructional text Carri us into a
different language uh max length again
it's a guide how long should be the uh
instructional text because it really
starts losing value if it doesn't fit in
the field because if you cannot see it
it's not helping you it has to be
concise it has to be short to the point
uh that's again why it's not a tool tip
it's very short and concise it's mostly
about the shape of the data uh some
limitations um so first uh in
documentation you're going to see that
you could set the field this field on
more uh in more places in Al but really
what we are going to render in client
currently is just PID page fields of of
type text Big text GD uh and code we're
kind of reserving a bit of space to
uh create more solutions in the future
that might be more flexible and based on
the same uh
concept uh right
so uh Stefan also showed that it also is
possible to use it in uh uh promp dialog
pages and there it serves a lot of value
because we actually are missing both
label and the tool tip uh in the prompt
input field so it's mostly visual Guide
to the users what they should do with
that field um and the story behind it
actually carries that we went many years
back and forth should we have the
instructional text but I think the promt
dialogue was the the breaking straw that
flipped the argument and said yes we
actually see enough value to have this
extra property on the field uh that's
how it came to be and then we realized
well actually it could be a good General
platform capability and we expand it to
all of the fields so that's a backstory
uh okay so multifile upload um you saw
this the code how to implement it uh
it's really also continuation of some
good Investments we made where we we saw
a lot of excitement uh that started with
supporting drag and drop first just with
single file upload uh we saw a lot of uh
Community uh feedback about that um and
it was really the next step to how we
could further improve the user
experience so what comes next after drag
and drop well actually I want to just
select and drag multiple files uh we see
in in the field uh of partner extensions
there's many extensions that actually
have this single purpose custom code
client add didn't implemented just to
support this uh multifile uploading so
hopefully this will alleviate some of
the implementation burden of uh
achieving this quite common scenario
especially when period of copal you
could imagine uh let's say you have a a
company or a user who does uh data entry
for items from catalog descriptions in
PDFs you could imagine person just
selects all PDFs drags them over to
business Central co- pilot takes care of
sorting out which data should go to the
which field uh that would be pretty cool
um scenario if doesn't already exist um
also some a bit of client behind the
scenes details uh the the upload happens
in parallel so it's a bit more efficient
uh than just single uh file upload on
top of that that you're also saving a
lot of clicks because otherwise you
would need to uh click an action upload
the file click an action upload the file
now drag and drop uh uh upload happens
in parallel but user is still blocked
until all of the files are uploaded and
processed by L uh also all the previous
uh size limits apply per file uh So
currently in SAS if I'm not mistaken
it's 350 megabytes yeah let's talk we we
hear quite often that it should be a lot
higher uh but it's also the reasoning
for us is really trying to be fair of
everyone's resources uh
uh in in Cloud as well um okay U mile
upload a bit of Al code uh Stefan showed
it I'm not going to repeat it uh it's
pretty straightforward it's actually
very familiar if you ever implemented
the file upload action it's just an
extra property to say that it's
multifile upload and of course it has a
list of files to
upload uh next calend control uh this
one is pretty fun uh because uh uh this
is helping us to align more with a
bigger Microsoft fluence UI design
language uh our calendar control was
pretty dat uh so we completely flipped
it around it supports exactly same
shortcuts same behaviors it just looks a
lot nicer um and if user is using uh
office U Outlook uh Excel he's going to
be very familiar how that control
interacts and it's just a small uh
reduction of uh just learning a new
control no upti needed from your side
whatsoever out of curiosity I've seen
actually an idea on the BCS website uh
does the calendar actually support the
week numbers in your calendar very good
point we took a note of that feedback
and I we think it's a pretty good idea
we're just trying to figure out uh
because it's not only showing weak
numbers there the problem is more
complex as always nothing is as easy as
weak numbers like there's different ways
of how you count apparently there's
different uh ways how you count weak
numbers uh so that's probably something
probably would like to configure based
on your uh country local uh whatever so
that that's something we're trying to
assess and yeah I hope maybe in near
medium future we could provide something
like
that uh okay we're good on time we're
going to have time for questions but
lastly so wiet has the tradition of
showing something from the lab and we
also are following this trend so far
quite well and we want to show something
that uh we're thinking about uh we
cannot commit to deadline we have plenty
of uh problems and edge cases to figure
out but I still want to inspire you of
something that uh we are looking
into so let's see let's launch a
video so we are exploring to enable uh
fact boox
[Applause]
resizing so immediately What
complications we're dealing with um the
primary reason why this is really useful
would be for example client add-ins that
are living in boxes that needs more
estate to display their data uh but of
course they're living in an if frame we
need to figure out how the resizing
would work uh we also need to make sure
that our flexible design system is hand
handling it not in only in this list
page scenario but also in every single
other combination that is possible and
that's usually our challenge we're
trying to design a very uh broad system
that works for everyone and sometimes it
doesn't work for very The Edge case uh
and we usually try to make sure that uh
we still can address it in some or other
way so we need to at least think about
it uh and that's what we're doing we're
doing a lot of thinking but I hope uh we
can make some progress on
this that is all thank you thank you
right so we have time for questions and
we have some T-shirts to do I saw one
hand there yeah okay can you pass it
on yeah I'm
just and also a
t-shirt can you just throw it there
okay um yes I got a a question about the
mobile app
um I saw you you when you open the page
the cursor was blinking in the first
empty field how how did you manage to do
that because uh I
can't okay it's actually no specific
code to do that you should just be by
default uh yeah so not really sure
exactly but but I know what you're
hinting to uh we don't have any API to
control the field input and we know that
feedback item we we need more thinking
about it there's some also complications
of what would that open up not just for
that uh scenario where it would be super
useful if you have one field and it
immediately is
focused
yeah
okay we have one more t-shirt I guess
that's our t-shirt to give away I can I
can do regarding the instructional test
a text um uh you mentioned that it will
be subject to some improvements would
you consider to uh possibility to change
it
dynamically uh that's a good input we
would like to hear a bit more maybe a
concrete scenario and that's something
we can then uh yeah take into
account but come come to me or either
after the session or in the tag Boot and
let's
discuss hi uh why there is no search bar
in uh work worksheet type uh page and is
it possible to to be added
uh there is no currently uh yes there is
no but what would be the scenario do you
mean the filter pan or just list no just
the search bar so the the shortcut uh F3
so if when user inputs like 300 lines
into the general journal so it's easy to
to to filter it and search for for
that's something we're going to take a
note of fine yeah
thanks any more questions
there's one in the
middle I'm going
to spot
on um the instructional Tex
so uh is that for the will that be
possible on table Fields as
well that's like the tool
tips yeah I'm trying to think uh is it
generalizable or not I guess that would
be the discussion can it be generalized
for the table field the will be the same
we need to discuss with
Stefan uh which kind of license do I
need for mobile
client do I need full full user license
or limited or device user
license uh I would usually redirect all
the licensing questions to the licensing
experts but there is device license type
that is true okay but can I okay you
don't know it okay not t-shirt
okay oh there's a question over
there we have a lot of questions hi um I
have another question related to
worksheet Pages um have you thought
about also saving having um saving views
as a possibility on worksheet
Pages use
uh openly speaking uh no but again it
would be subject to the scenario we
would like to understand uh the exact
business case of like how that would be
used yeah so come to me let's
talk um I have a question regarding uh
JavaScript uh add in layout uh you
mentioned that it will be not possible
to make uh I
frame uh and we have Solutions based on
that yeah but we are not deprecating
those Solutions uh these are just the
two controllin that are not supporting
that so these are specific for client
and sensibilities uh the addins such as
the camera Barcode Scanner and the
barcode scanner provider but we are not
breaking any existing functionality of
the current user control in so they
would just work exactly as you are used
to them so specific to like for example
camera provider uh location provider uh
what else uh contact picker those were
all Native platform capabilities that
has been exposed through net interface
uh so that's what's changing okay thank
you
uh do we have one more
or no okay well I think we're good um
thank you all thank you
