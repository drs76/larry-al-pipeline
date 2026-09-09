# NAV TechDays 2016: Building cool experiences with NAV everywhere

- **Source:** https://www.youtube.com/watch?v=pbv4dhlYBWo
- **Video ID:** pbv4dhlYBWo
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 84m00s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

Good morning everyone. Welcome to our
session. How are you doing so far? Did
you enjoy the keynote? It was very cool
actually. Okay. Uh so let's introduce
ourselves. My name is Horina. I am the
engineering lead for the NAV client team
and I'm here with these two gentlemen.
So my name is Andrea. I was here last
year. So I hope you remember. I also
work in the Dynamics NV client team and
I'm a software developer.
Okay. And uh my name is Ego Kawani. I
also work in the NAV client team. I'm a
developer as well. Okay. So we are very
um privileged to uh be here today uh and
share with you dear Nav developer all
the cool things we have been building in
Microsoft Dynamics NAV 2017 and Dynamics
365 for financials.
So it has been a very busy year for us
at Microsoft and what you will see um
throughout the sessions today and
tomorrow is that NAV is truly everywhere
and it is not only on desktop and all
major mobile platforms but also uh
deeply integrated into
office. So uh with that let's uh take a
look at our session objectives.
So our so the message we would like to
convey today with this session is that
with NAV you have all the building
blocks that are needed for building new
modern experiences
everywhere. And today we will walk you
through the list of the client
enhancements uh available in this
release. And you will see that some of
them just simply light up by upgrading
to Microsoft Dynamics 2017 while others
they will just need a little bit of your
developers touch to uh enable new
experiences for your
customers. So
uh let's get started. So the first uh
thing on our agenda is to show you the
building blocks available in the toolbox
for building these new modern
experiences.
The next thing we'll we'll show you
what's new in our mobile
apps. After that we will talk about
simplicity and productivity
enough and at the end we will do
something we normally try to not to do
but this time we will change it a little
bit. So we'll actually uh share some
thoughts with you about how we see
Microsoft Dynamic Nav clients evolving
in the upcoming releases. Well, pretty
busy agenda, right? Yes. Where do we
start from? We start with all new
experiences. So what are the ingredients
that uh you need for enabling new
experiences in
NAV? The first one is the bricks and you
can say the bricks uh is actually a
concept that is not new to NAV. It has
introduced it has been introduced in
Microsoft Dynamics NAV 2016 phone client
in order to um um optimize the available
space and the readability of the data.
But what it's interesting about bricks
is that they're not only just an
alternative way to render the old
classic rows in the lists. They actually
flow naturally and beautifully into the
UI and uh give you at a glance all the
information you need for uh performing a
business uh process or making a business
decision. And that is why we decided it
was quite important to actually enhance
the lists in a tablet and desktop with
bricks. The next thing is media. So what
is media all about? Media is all about
bringing color and modern experiences
into NAV. So what I said previously was
that bricks were like a compact
representation of a record. But what
better way to to actually represent a
record than a picture, right? So, uh
imagine you want to order an item and
instead of reading all these description
fields or you can, you know, you see you
see a picture and say this is what I
want. This is what I want to order. And
that is why we have introduced these two
new media types. The media media set
that actually ago is going to tell you
all about it. And of course you can say
the pictures were available previously
as blog fields and why didn't we stay
with that is because they don't scale
enough for our ambitions to deliver
modern experiences in the HTML
clients and the next building block that
is wizard. So as we build more and more
repeatable solutions in the cloud, it
becomes quite important that the end
users are able to perform their daily
tasks uh without a lot of friction and a
lot without a lot of cost to us as
solution
implementers. And this is where wizards
actually come into play. They're a great
concept for um set up for guiding users
to set up on configuration tasks or for
guiding users through complex tasks or
uh basically building welcome and
introduction tools for the novice users
right and behind users be behind wizards
is actually a concept that is uh uh not
new to enough that is navigate page and
what we have done in this release is not
only that we have extended the support
to uh all platforms but we have also
brought the uh user experience to a
whole new level and you'll see a bit
later and then the last thing uh that
we're going to touch from the old modern
experiences that is contextual
notification. So what is a notification?
Notification is a message that appear at
the top of the page and it is meant to
guide the user to perform a certain
action and you will see that the user
can directly interact into the into the
message bar uh invoking actions. And if
you think about the wizard for example
then we can see that contextual
notifications together with wizard are
actually a very powerful combo for
building uh welcome and introduction
experience for for novice users.
And these are kind of the main concepts
that we have in our modern experiences.
And we will show you uh a demo right now
on how we have combined this uh on the
desktop client.
I guess we're ready. All right. So we
have here the Microsoft Dynamics NF 2017
web client.
And whilst we're preparing for this
session, we wondering what would be the
best way to to show you how to combine
these uh these tools available uh in our
toolbox. And we decided maybe the best
way is to actually build a mini welcome
uh tour for u uh registering NAVC days
attendees. So let's see it in action. So
in a welcome tour, it is very often that
you would like to start with a video to
to either because you want to distract
the user from all the configuration and
setup tasks or because you simply want
to introd introduce your product to the
user, give him give them an overview of
what is it that uh you have as
functionality in the product. And that
is why we have decided to um basically
embed also videos in the wizard and AGO
is going to present a lot about it. And
of course it was very much discussed
which video should we put in this in
this w in this welcome tour. We spend a
lot a lot of time but because both all
three of us are very big fans of uh
surface studio we decided to show you
this introduction. So I'm expecting next
year to have some of these cool devices
on our desk. always need devices to
test. That is correct. I see nav on all
devices,
right? So let's see what's next on our
welcome tour. So another uh common
pattern in the uh welcome tours is
basically show a cover image to the user
associate the information that is
provided to the user with with a cover
image. And actually we in uh this
release we have also introduced this
cover image concept in wizards and you
will see a bit later how how this is
done.
And now it is time to register someone
to the NAV tech days.
Register Andrea. Yeah. So let's type in
my
name. Um well who remembers where I'm
from?
Oh yeah, you can get a t-shirt.
Where are you?
Thank you. Perfect. But Andrea has been
so long time in Denmark that actually
he's considering me to be a Viking. So
yeah, it's also written on my badge. So
I'm Yes, I'll I'll put Denmark. Okay.
And well, we need a t-shirt size. Why do
we need a t-shirt size in our welcome
tour? Well, because we are going to give
t-shirts. We are going to ask questions
to you and uh well if you answer
correctly you'll get a t-shirt so we
need to know your size and in my case
I'm medium medium or medium. Medium.
Okay.
Well, and then what is your favorite
session or the session you want to
attend? Well, I'm already attending the
best session which is our session,
right? Of course. Great. Great. So, we
can move on. Yep.
Then finishing with my
address. And of course, we all
love Nav Tech days.
Okay, looks like I'm done. Andrea is
registered to the NAV Tech days and now
we can continue showing him all the uh
cool features we have built in NAV 2017.
So whilst we press continue the welcome
tour navigates us to the customer list
and what we see there at at the first
site is basically how we did we combine
the media and bricks together uh in
showing images in lists. So if you have
for example a field in in your table
that is a media and that is part of the
brick property group then we render
images uh in the lists and of course
this this brickview concept you know
switching between brick views is is a
concept that is uh uh familiar in all
multimedia apps in Windows in SharePoint
and just uh we have implemented a
similar experience in nav. So you can
actually switch between these modes, you
can also re go back to the classic rows
view. Maybe not. Yeah, it could be
boring, right? No color. And also if the
uh list has media with thumbnailing,
then we also introduce a third mode
which we call tall
bricks. So Nav Nav also remembers the um
uh view mode that the user has chosen
last. Um so basically if you choose one
of these modes then uh next time you
open the customer list you will uh get
precisely that mode and also um the NAV
is able to intelligently determine the
view that the list should open. So if
you have no if you have defined the
media field but there is no images
uploaded into the database we actually
start in the classic
mode. Also the other thing to notice is
how fast and fluid the scrolling is. Uh
and that is because we don't load all
these pictures at once. We load them on
demand. And the browser also has
mechanism for loading the pictures as
synchronously which helps us to uh
provide this fast and fluid experience.
So now um you can also do search um you
know in the bricks meaning you know you
can type the uh name or or or a keyword
and you find the um specific customers.
Unfortunately we don't support yet uh uh
sorting and filtering in in brick
brickview modes but if you go to the
classic mode and you sort do sorting and
filtering and you come back to the
bricks you will respect this uh these
options. There is also not yet a
developer API for actually specifying uh
directly in the which brick mode you
would like the list to open.
So now let's uh drill down into the uh
one of the
customers and here you can see uh I mean
you can see that the um um pictures the
media fields can also be embedded in
fbox boxes and for here here we actually
have defined actions for importing and
exporting the picture and ego is going
to uh show you how that was
done. So this is how we actually uh
build this uh this experience by
combining the media and bricks together.
But besides that, besides this uh you
know big major improvements, we have
also done a a bunch of smaller
improvements. So for example, if you
take a look at the ribbon, I don't know
if you noticed, but it opened expanded
and the reason for this is that if you
have a promoted action, the ribbon was
now automatically open expanded. This is
an improvement we have done based on a
lot of feedback we have received. So I
hope you find it
useful. Then also in order to reduce the
clutter in the ribbon, we have also
collapsed the uh view and edit action
into one single toggle
button. So uh this is how andrea likes
to play this with this a lot. Yeah,
maybe I should stop doing that. Yes, you
should stop doing that.
Um another area of improvement a small
improvement we have done is actually
related to shortcuts. So we have added
escape for as a shortcut for closing the
the the list the pages in general right.
So um and coming back to the ro center
another uh shortcut uh behavior we have
changed that is F5. So F5 before was the
browser F5 and if you are pressing that
then the whole page will be will be
rebuilding. But what we have done in
this release is that we have connected
F5 with the actual data loading. So when
you press F5 we you know the page is
still built but we're just reloading the
data and we're not we're doing that for
each of the parts. Uh and that is
including the parts with the
extensibility controls and um what we
have done in order to enable that we
have extended the our adin framework
with a new event uh a refresh event. So
when you press F5 basically this uh
event will be raised in your addins and
you can implement your code for for
loading data and we strongly actually
suggest to you that if you have existing
addins to actually uptake this uh this
event and that is a a kind of a small
summary of what we have available right
now on the desktop and now Ago is going
to show you how a wizard media is is all
working together. Okay, thanks Raina. I
hope you're all excited for the features
we just saw. So I'm going to start with
the wizard because this is probably my
favorite page type we have in
NV. Um as Hina just explained, wizard is
actually not a new concept. It uses the
existing page type uh the navigate page.
Uh this has existed in the Windows
client for for quite some time but we
received a lot of fever from you to add
support for this in the HTML clients. So
in Microsoft Dynamics NAV 2017, we are
we're finally adding this for you and
you can already start using this in HTML
clients and the upgrade should be a
trial process and there are no actions
required to start using this and that
means you can reuse the existing pages
and they are enabled in all the clients.
So that means even the touch clients
like tablet and phone and there are also
many examples in the product where you
can take a look if you're wondering how
we built some of these cool wizards. So
uh but we didn't just stop there. Uh we
added a new feature for the uh
specifically for the HTML clients and we
called this cover image. Uh what this
means is that you can use a media field
or control addin to embed uh some
visuals or videos to a step. So in
Hina's demo uh we had a YouTube video
embedded in the step in the wizard and
that was done using uh a new addin we
have uh introduced in 2017. We have the
web page viewer control addin. Uh we
have a session for that tomorrow. Uh we
use that to host an YouTube video and
the second page of the wizard uh we had
a media field showing the logo of detect
this. Um but there are several things to
remember if you're using this media
field that cover image the image will
will get the gray background. I don't
think it was that clear in on the uh
screen here, but you do get the gray
background and the image will be left
aligned. And if you using it, you don't
have to. It's an optional, but you get
one per
page. All right. So, let's get into the
more details about how to construct
these pages. So, here you see at the top
uh there it's a very typical wizard with
two steps and to define a step uh we use
the top level groups like you see here.
There are two groups at the top level
directly under the container. But that's
not the only thing. You also need to set
the visible property of these groups to
be dynamic. So that means you need to
assign a variable. So in this case we
have a variable called current step
which is set to these properties and
you'll be uh incrementing or
decrementing this or maybe setting to
true or false to control which step gets
shown. So that's pretty simple and we
also put the picture of the uh wizard we
saw in the demo just now. And maybe
maybe I can go through how this page was
constructed. And at the top we have the
check icon and this is uh using the
cover image feature I just described.
And to get that effect um you need to
define a media or control addin field as
the very first item inside the group
which represents a step. So at the top
you see there's a field and has a source
expression variable bound to uh some
field in the table and that's actually a
media field. I get into how to actually
start using this or more about what the
media field is about. But here just uh
remember that uh you have the media
field at the very first group. You can
swap this with a control addin and
that's how you create a cover image. And
there's another tip uh that you to
remember. There's a group underneath. If
you look at it um using these subgroups
are a great way to organize or create
like sections or paragraphs with
emphasized title. So for example in the
picture below you see the text says
that's it and that's actually done using
a subgroup and using a caption property
set to that's it and the text below
comes from the instructional text
property of that subgroup and we use
this in several wizards we have built
and it's a great way to organize text.
So you can probably start using it. And
uh next uh once you have the steps the
the next important thing you need to do
is to define actions so that user can
navigate between steps. Right? So uh I
can explain how this works. It's pretty
simple. So at the bottom uh right corner
we have the three buttons. This is the
just a screenshot of what we saw in hus
demo. Uh we have the back next and
continue. So there are two properties
that are important to remember. One is
the info bar property. So if you set
that to yes, the action will show up at
the bottom of the wizard. And if you
don't do that, they will not appear
because if you noticed a wizard does not
have a ribbon and that's because we
wanted to promote simplicity inside the
wizard because it's meant for guiding
users through some complex tasks. Um we
don't want to use that for like
presenting a data for example. So we
remove the actions from ribbon and um
hope that you don't I mean I guess you
can if you want to but maybe do not put
too many actions so the user can focus
on what's important. Um but so that's
one thing info about property and the
next one is the image property. So uh we
support using three different images
here to
uh to uh define uh which button is
treated as the back next or finish. So
if you use the image set to previous
record then that would be uh rendered as
the back button and next record for the
next uh button and finish or continue
button is done using the approve uh
image. So on the desktop client you just
get these three text boxes and some of
them get highlighted depending on which
buttons enabled but on phone clients and
also on tablet clients we uh render
icons instead. So if you want that kind
of effect u make sure to set the image
property. So that's all we have for
actions. I think it's pretty simple and
I hope you all familiar with the navig
page already. So please use start using
NAV. I think it's really cool. Um yeah.
So next um I want to go through the
media fields. So this is um new field we
added in 2017. Um this is pretty much
about the image fields. So we have the
image field. Um maybe I want to ask you
some questions. So does anybody know how
we store the image field currently in
NAV?
No, like image field. The not the media
before the media.
Yes. I don't know who said it first. Got
it. Choose one. Choose one. Oh, no. But
I think there's someone over there.
Someone over there. Andrea, who was it?
There was someone over here. I heard
Andrea. What? Someone over here. Oh,
yes. But yeah, that's right. We used the
blog field to store binary data directly
into the HTML SQL table. Um but we
noticed that that's not what we really
wanted to achieve um the uh level that
we wanted to get especially for the SAS
environment. Um so we wanted to scale it
well to the level that's really is fast
and fluid. But for example if you are
using a mobile phone with a slow
internet it was very important for us
that the experience is smooth. If you
are scrolling scrolling through a list
of bricks with images it was important
that you you don't have to you know load
the images and to wait. And so yeah, we
spend some time thinking about how to
solve this and uh we that's why we have
this media field introduced and what
this does is that when you store an
image, the image gets um stored in a
system table and we reference them using
uh ID. So we don't really interact with
the blob data directly. So that's what's
actually the media field is about. But
there also some more uh advantages that
it gives you over the uh good old image
field. is so the probably the biggest
one we have is the thumbnail link. Uh so
what this means is when you store a
media field uh we generate uh thumbnails
of the image of different sizes and we
figure out which size is the best to use
depending on what device you're using or
what component you are using for example
it doesn't really make sense to download
a big image on if you're using a phone
client because you all you want is just
a smaller image right so um that's what
the thumb lending is used for it's also
happens in desktop client if you're
using um brick field in the So client or
the fat box we figure out the best image
you to use there. And next uh we have
the caching. So caching is something we
do in the HTML client. So we cache the
image on the IIS server once the user
access it. So the second time we can
eliminate or reduce the uh round trip to
SD server. So that's another neat thing
we did and we have the on demand
loading. So I think H touched this a
little bit but uh when image loaded we
do it asynchronously. So we don't have
to block the user and so it's it gives
you it helps us to gives us um very
smooth scrolling experience and of
course we support all the common image
formats like JPEG and GIF that's so you
can start using that and next uh it says
that the client only shows the first
picture so let me just explain what this
means so we have the media field and we
actually have another one called media
set and this is used um if you want to
store several images into one field. For
example, if you have want to store
images of item from different angles.
For example, if you go to Amazon, you
have uh images of the product for
different images, right? So, media sets
can allow you to do that. But we
currently have a limitation that the NAV
that uh shows only the first picture,
meaning you can't choose which one you
want to show. But we'll be working on
this. But uh it's great. Maybe you
should uh remember that you can show
this in the reports. If you have media
field inside a uh list for example, the
image will show up in the report. Um but
yeah, so this is still a work in
progress. Um uh we have we show this in
c parts and the wizard when uses the
cover image, but we don't we do not show
that in other places. For example, if
you want to use this in the c page, they
will not show
up. Okay. So let's get into more details
to how to actually use media. Um so the
primary example of using media will
probably be bricks. So we have a picture
of brick over here right now and I'm
pretty sure you are familiar with the
bricks or played around play around with
the bricks at least once. Um it's pretty
easy to define that. But first if you
want to use the media and brick u go to
the table and define a field whose type
is media. So we have a field called
portrait and it has the media. And you
might be wondering why we have the
extended data type set to person. So
this is something we new we added. So if
you set that to person, what we do is
you get a circular image like you see
here. And in the item list, we have a
square image. But if you set the person,
that's the default one. But if you go to
person, we have the circular image. So
once you have this um all you need to do
is go to uh define uh field group and
set the name of the group to be bricks.
And just you have to add the media field
as one of these views you want to show
and it will show up as like
this. And there's one last thing I want
to go through for the media. Uh it says
that you must code your own CRUD if
using HTML clients. So this means uh we
do not yet uh NV doesn't support uh give
you a way to natively update or create
know create update export delete media
fields uh yet but we'll be working on
that. So what this means is if you want
to let users import or export or delete
pictures you have to code this using CL
right now and so I put the snippet of
code how you can import a file. So it
uses the file management code unit to
upload a file and you can import a file
into the field and stuff like that. So
in this um uh in the hoous demo we had
we had a customer card and we had a
picture in the factbox and there was
some actions in there says import and
export like you see here. So these are
all done using the CL code. Yeah. So
that's all I have for the bricks right
now. Sorry, the media. Um I think we're
going to just switch to gear to the
Andrea if you're correct. So the next
the next topic in our agenda is uh what
is new in our mobile apps and uh you
will also get a chance to see there the
uh media uh and bricks in action. So uh
let's switch to to our phone app.
So uh I have here the Microsnamics NV
2017 phone client and the first thing we
see is uh that the navigation bar has
moved at the bottom of the screen. We
have uh done this change in order to
make it more accessible for the users
while uh holding the phone in their
hands. And also on the navigation bar we
have added the swipe uh uh that so you
basically can swipe between parts just
uh swiping on the bar and let's stop
while swiping through the parts. Let's
stop on the item list. Um so here we see
yet again the media and bricks together
in action and also you have a chance to
see how scrolling actually works on the
device. the the same fast and fluid
experience. We have also for the uh for
the list parts available on the
homepage. We have also promoted uh two
important actions meaning the uh the new
action and the search. So uh you can
have uh you can interact with the list
um much much faster
quicker and uh but all of these are sort
of you know uh tiny a bit improvements
but the biggest thing is actually that
we have introduced gestures in in our
mobile apps. So let's uh let's assume
that I am in a warehouse and I'm doing
stock keeping every month and uh you
know I'm sitting between a lot of boxes
and uh I have the uh phone in my hand
with the NAV phone client and what I
want to do is I want to go through these
items and I just want to adjust the
inventory amount on these items and I
know for example that the Amsterd
Amsterdam lamp that I have returned one
of them so I don't have 268 items. So I
would like to adjust the amount. So all
I need to do is swipe from the right and
take a peek at the existing actions. So
here you can find the uh actions that
are connected with the swipe gesture. So
in my case I would like to subtract. So
let's just swipe all the way to the end
and then the notice that the quantity
gets updated. And the same thing with uh
others like for example the Tokyo lamps
that is Andrea's favorite the Tokyo
chair sorry that is Andrea's favorite
chair. So he said he would like to have
one more. So I'm going to order one
more. So uh I will just adjust the
inventory amount uh by swiping from the
from the left. So here we see the add
action.
Right. And this is how the inventory
amount gets updated. So I can continue
all day and updating this uh this uh uh
items in my item list. But once I'm done
then I would like to uh create a sales
quote for my
customers. And let's assume that I would
like to create a a quote for the uh
progressive home furnished. So um if I
tap and hold on that particular record
the context menu appears and I could
just uh with the tip of my finger in
invoke the uh new code
action and the information gets
prepopulated uh so about the information
about the customer gets prepopulated. So
now all I need to do is basically add um
add a line, right? So let's um add a
line. Let's assume I'm still in love
with the Amsterdam
lamps and I want quantity
one and and I have my line uh created.
But now I'm thinking, okay, uh maybe
not. So I I think I would like to have
two lamps, right? I would like to create
S code for for two lamps. So then I all
I need to do is just swipe on that
record and and increase the quantity. So
there is the the gestures are available
basically on on parts in the in the in
the RO center also on the uh sub forms
and uh on lists and um you can just go
creative and and create all sorts of uh
crazy apps, you know, like uh I don't
know, Tinder apps or whatever, right?
Yeah.
All right. So now I will give it to Ago
to talk about gestures. Yes. So I'll
start with the swipe action. So I'm sure
you already saw this in the keynote and
everything, but I'm just going to get
you to more details. So you can define a
record level swipe. So what this means
is that action you define will be bound
to the specific role that user is
interacting. Uh like we saw we created a
sales invoice for that user. So that's
what swipe action can do. And this works
in list parts and list pages but they
work on the phone client right now. Um
and they are driven by the scope
property and the gesture property. So
I'll show you how you can actually do
that and talk about how you do it. And
another one is that you can have single
or multiple actions and you can have up
to three actions in per direction. So
that means you can have up to three on
the left side and you can have another
three on the right. But if you have more
than three for example then we but we
just cut it and show it three actions
there and the order of actions that we
create is implicit and it's actually
what you see in the designer and I I'll
show you what they mean. So yeah and
next I'm going to describe more about
the tap and hold. So this is the little
menu that appears if you tap and hold
your finger in the row. And this also
works in lists and list pages list part
sorry and they work in tablet and phone
and these are driven by the scope
property. So swipe action and tap and
hold they work uh very similarly. So tap
and hold uses only the scope but the
swipe uses the extra one the gesture. So
I'll show you how this actually works in
action.
Right. Okay. So, I've created a list
already. You have a have a item list
here. Yep. And if I go to
actions. So, here I have uh several
actions that I could uh change it to a
swipe action. Um so, it's pretty easy as
you saw in the keynote already. You can
uh first thing you need to do is to set
the scope property to repeater. So what
this means is that um this action will
be bound to a row instead of the page.
And once you uh once you did that uh set
the gesture property to left or right
swipe. So if you do a left swipe they
will show up on the left side of the
brick and right otherwise if you do
that. So you can do that on all the
actions. Yeah. But make sure to set the
promoted property to yes because it's a
phone client. Um so here we have to left
swipe first and then left swipe too
under the group. So you you'll get the
uh the auto action will be you get the
left swipe as the rightmost action if if
you swipe from the left and the swipe
two will appear after the swipe uh left
swipe one and the same story goes for
the right swipe one and right swipe two.
Um so that's how you do the swipe
action. It's pretty simple but if you
want to do tap and hold uh all you have
to do is just to go to the same okay
let's just use this as example but just
do not specify the gesture property and
it will show up in the tap and hold
actions. So let's say you have five
swipe actions like as I said before you
have you'll get only three actions but
if you open the tap and hold all the
actions will appear there. So that's the
one neat thing to
remember. Okay. Um so should we uh
switch gear to Andrea? I think he has
something to show us about the mobile
platforms. Yes. So, so far uh you ego
and Arena, you have shown us a lot of
very cool new features in the product
and I probably one of the questions
you're asking yourself at the moment is
is it going to be available everywhere?
Uh will my customers be able to get it?
The answer is as always yes. Um, even
though some of the features we've just
shown, like for example, gestures, the
swipe action or uh the tap and hold
action are only available for a specific
display target. Um, you will get that
feature on all platforms namely Windows,
iOS and Android. So, and maybe
everywhere. But how about the app stores
in the operation operating system that
we support? Yeah. Well, uh our app is
available on all on all the stores and
uh we keep updating it uh as soon as new
updates are pushed on these stores. Um
for example, lately we've introduced u
support for iOS 10 and we have also
introduced support um in Microsoft
Dynamics NV 2017 for the iPad Pro. So
now dynamics can also be uh run on the
iPad Pro and the experience is is very
nice. It's amazing actually. I've tried
it and I love it.
Well, I think that now it's time for me
to uh switch topic and start talking
about uh NAV and uh first-time users.
Mhm. Um, in this release, we decided to
put a lot of focus on uh on first-time
users and simplifying the user
experience. Uh, why is that? NV is a
pretty powerful tool. You probably know
that. Um, and it should be from the very
first time a user approaches NAV. So,
we've decided to put a lot of focus on
uh on all these users that are not
really familiar with NAV concepts. We're
talking about users that um see the
product for the first time. So we want
them to be very
productive and in order to do so we have
worked on on different features in uh in
the product in order to make the
experience from the very first time uh
amazing and we have started working on
improving some of our existing features.
Uh one of them is the tool tips. Um I'm
not talking about uh something new. You
can define tool tips. the developer can
define tool tips on different fields via
the tool tip ML property and uh and the
tool tip will surface in the product.
This also pretty powerful because it's
localizable but we have restyled the
tool tip and we have changed the way it
behaves so that um it is more
interactive and we have also decided to
join two experiences the tool tip
experience and the help experience. So
you will see now in my next demo that uh
both of them are actually connected
together so that the user is always
provided uh with the necessary amount of
help he needs for carrying on the
business operations he need to
perform. So I guess we can switch to the
demo and uh here's a little story about
me. Uh when I started working in
Dynamics NAV uh 3 years ago, I didn't
know anything about ERP uh sales
invoices, sales quotes, uh sales orders,
something I've never really played with.
So think about me uh three years ago now
approaching Dynamics 10V 2017
uh and I want to create a new sales
invoice. That's my task. But remember
that's the first time I see Microsoft
Dynamics NAV and this is the first time
for me to create a sales invoice. Where
do I start from? Uh, I'm in the RO
center and I can see in the ribbon there
is an action for creating a new sales
invoice. Probably I should go from
there. And looks like that's the correct
place. A new page opens and uh it is the
new sales invoice page. Fine. But yet uh
that's the first time for me to fill in
a sales invoice. I don't know anything
about it. But I see a red mark over
there. And that red mark tells me
probably to start from there.
So, a customer field is probably the
first field I need to fill in. Uh, why
do I need to have a customer for a sales
invoice? I can click on the customer
caption and the new tool tip uh shows
up. So, as you as you can see, uh the
look and feel is different. Uh the way
you bring up the tool tip is different.
It's no more on hover, now it's on
click. uh so that you are not disrupted
while actually uh scrolling on the page.
But there is something more there is a
learn more action. If you click on that
the user if the user clicks on that the
user will be brought automatically on a
new tab to the help page and this is the
contextual help page. So um the user is
working and uh there is something he
doesn't understand it he's immediately
brought to the help contextual to that
specific topic. So now that the two
experiences are connected together uh
the overall experience feels much
better. So now I can start from here and
I can pick up a
customer
and well is also very nice because it
fills all the other fields for me. Uh I
I want to uh point out another thing
very important. Tool tips are available
on all page types. It means also on
lists. Um when I want to bring up a tool
tip in a le on a list. Uh I can go there
um by using uh the column header. So as
soon as the user clicks on the header a
new action is available. What's this?
And as soon as you click on that the the
tool tip is shown up as before. So tool
tips are available everywhere on all
clients actually. So not just the web
client, it's the tablet client as well
and the phone client. The experience is
different because there is on tap but
tool tips are everywhere. The user is
never really never left alone.
Pretty cool. Yeah. Uh actually very
useful. Mhm. So my next
you'd like to talk us about what is
behind the tool tips, right?
Um yes. Um actually the the whole story
uh on tool tips is over. So we can move
on on notifications I think. Okay. which
is the other very cool uh feature that
uh we worked on in this release. Uh we
fight over a lot on the things that we
like the most. So ego has his own
favorites. I have my own favorite which
is notifications. Um so the best way to
introduce notifications is probably by
asking ourselves a question and that is
how many ways does a developer have
today for interacting with the user with
the user. If you think about it there is
one tool that we have today and that's
the dialogue. Uh two things about the
dialogue very important. Uh first of all
dialogues are prominent and when I say
prominent I really mean prominent. So
they appear at the center of the screen.
They hide the rest of the UI and uh and
the user is basically distracted and now
his attention is caught up there on the
dialogue. Second, the other most the
other very magical characteristic is
that dialogues are blocking. It means
that whatever business process the user
was carrying on now uh he cannot
continue anymore because he's blocked.
the dialogue is dragging his attention
on something
else. From another angle, from another
perspective, you can say that the tool
tip is also the sorry that the the
dialogue is actually forcing the user to
take a decision, to take action on
something. All these three
characteristics, do we really want them
always when interacting with the user?
The answer is no. There are some
situations where a dialogue is good. We
want to interrupt the user. It's a very
critical operation to do. So the user
should be blocked. But in other cases,
and it turns out to be most of the
cases, we just want to inform the user
about something that happened. We don't
really want to block him. We don't want
to distract him. The user must be able
to continue to to go on on his task if
he decides to do so. So far, it wasn't
possible. But now in the Microsoft
Dynamics NV 2017, it is thanks to
notifications. Notifications are a
different paralleling for interacting
with the user. Uh they are not
prominent. Uh they appear in a very
subtle way at the top of the page. Uh
also they do not block the user at all
when a notification is shown up. Uh the
user can still continue carrying on
whatever operation he's doing without
be. And that's exactly what we want to
have. So um I guess enough talking and
uh I can start demoing that and showing
that to
you. So now that I can create sales
invoice, I I promise I'm going to create
thousands of them. So let's create again
a new sales invoice and I will I'll just
pick up my favorite customer. And uh
this customer asked me
uh a lot of chairs. So he wants 200 of
them. So, I fill in my says invoice and
I put inside uh 200 of them. As soon as
I do that, I leave the field and a
notification is showing up. Now, the
point is that I don't care because this
is my second in sales invoice. It's very
important to me. I I want to finish
filling in the sales invoice. So, I
create my second line because the sales
invoice is not over yet. So I keep
filling my lines and when I'm done with
it then I can raise my head and see that
there is a notification and I can start
acting on it. But I'm deciding to act on
it now. So there was an action uh that
gives me an option and uh that's just a
review of the item that I'm running out
of basically. And as soon as I'm done
with that, I can close the page. And as
soon as I do that, the action that was
defined in the notification, the action
uh the CL code inside there is done. And
uh the notification is
dismissed. And that's the other
important characteristics of
notifications. Whatever action you
define on a notification uh when uh
invoked by the user will automatically
trigger an automat a dismissal of the
notification because once an action is
invoked, the user has made a choice. So
the notification is not going to be
needed
anymore. Well, pretty powerful, right?
It's a simple but powerful API indeed.
And uh I can actually show you how to do
that.
the the whole uh experience for
developing notifications is very
simple. So let's
close the objects that ego
had. Yes. And uh well notifications can
be uh sent from every part of the code
really. But I would like to keep things
simple here. So, I will just create I I
will just send a notification when
opening a
page. So, I'll get the the customer
card. I think that's that's a good page.
And uh so when the page opens, where
should I put the code?
Sorry.
Run record. Huh?
Yes. On open page. Yes. On open page.
That's much better, right? That's Thank
you. That is true.
Yes.
So, let's go to the
trigger and
let's bring up the
code. Perfect. Um, well, you attended
the keynote, right? So, and you saw a
little bit of the code of the
notification. Uh, I need a notification
object as the first thing. And uh
well I'll just call it my notification.
Uh do you remember that the name of the
new type that we have?
Yeah, it was
simple but in Yeah, you deserve a
t-shirt. It was you
right. Thank you.
So our new
type is
here. I can go out of the my locals and
I can start using the
object and as soon as I bring up my
amazing experience for uh all the new
features in our coding environment, I
can see how the API basically looks
like. But this is going to be a very
simple notification. So let me just set
a
message and uh well let me just greet
myself and after that remember what I
told you
we send
notifications and that's it. Two lines
of
code and I'm done. So back in the
product in the list and I open the
page and my notification is there and uh
well thank you for g greeting me and I'm
done.
So you could see that notifications are
very simple to send and the API uh looks
very simple as well but it can be much
much richer than that.
uh there is a whole session devoted to
the notification API. uh so I'm not
going to go into details on that today.
Uh I will encourage you to attend uh
tomorrow's session by our colleagues
Klaus and Yasper. You will learn all
about notifications there. But let me
just give you a little sneak peek u
around the notification API by
introducing you two um two features of
the API which are very very useful and
they are all about interacting with
notifications already existing on the
page. Uh what's the main scenario here?
The main scenario is that you send a
notification. You're the developer. You
send a
notification. But remember when you send
a notification you have no guarantee
that that notification is going to be uh
actioned uh immediately by the user. The
user decides it now. It's up to the
user. So theoretically uh that
notification uh might stay on on the
page for a really long time. So let's
consider our user uh interacting with
our solution and we send a notification
but the user doesn't care about it. It
keeps interacting with our solution and
uh now that the business process is at a
certain state the notification that we
sent has expired namely because of the
new state of the application that
notification is not needed anymore. What
do we do? uh should we wait for the for
the user to dismiss it but that
notification is not needed anymore. So
from the code we can use the recall API
in order to remove the notification from
the page from the
code. And the second feature is about
updating notific existing notifications.
And the scenario is slightly little
different. Namely again you send a
notification but the notification is not
im immediately actioned by the user. And
uh as the user keeps interacting with
your solution, the business process is
carried on and at a certain point the
state is such for which the notification
you sent is no more uh valid meaning
that the information which is which are
providing the notifications uh are not
good enough. So you need to update this
notification. The notification has
become uh outdated. You can use the
update API in order to change the
notification. You do not need to recall
the notification and send a new one
though you can do that but we discourage
you from doing that because there are
two operations. You can just do the same
with only one call uh which is using the
update
API. So indeed very powerful API
extremely useful they can change the way
you interact with your users. Uh I
encourage you to start changing from
using dialogues to notifications where
it is required. Uh I really hope you're
going to love them. Mhm. And the most
important that they are available across
all platforms. Oh yes, Windows client,
the web client, tablet and phone
everywhere.
Okay. So let's switch to the next item
on our
agenda. Yeah. So uh we have reached the
productivity in uh in outlook. So if you
remember in the beginning of the session
I uh mentioned that uh NAV is truly
everywhere uh in and deeply integrated
into office and how have we done that?
So we have taken the business process,
we have automated them and we have uh
integrating them from NAV into uh
Outlook productivity tools like Outlook
and Excel providing uh an immersive user
experiences uh AC across all these
product families office 365 and and
NAV. So uh now let's uh let's take a
look at uh the Outlook
addin. Uh let's assume I am a business
owner and I have uh Office 365
subscription. I am at my desk and I read
my mails and uh I can see in my inbox I
have two unread emails. One from Andrea,
one from Ago.
So this week I had a meeting with Andrea
and I have presented him some uh Athens
chairs and all the wonderful features
that an Athen chair has and he was
really happy and uh when I came back to
my desk Andrea sent me an email and said
wow Hina that was a great presentation I
would like you to send me a quote for
these Athens
chairs and here I am in my mail and
whilst I'm reading it I see that I have
Dynamics NAV uh tab available and um
basically the Dynamics NAV addin is able
to uh give me to recognize the context
and give me uh customer information and
not only just uh you know what's the
address and details about that that
particular customer but also financial
information like what are the history of
my transactions and so on and now I uh I
would like to send a code so I go to the
uh new action, new uh context menu and
choose new
quote. Notice how the information is
prefilled already in the quote as as
always. And now I just go and create a
line. How many chairs did you wanted the
quote for? 10. Thank you. 10. Okay,
let's put
10. And that's it. I have my quote. Now
I would like to send an email to Andrea
with this quote. So we have an action
available and we click on it and what
happens behind the scene is that NAV is
generating uh a PDF version of the quad
and is attaching this this as a as a
document in the in the draft mail
prefilling also the um uh information
and all I need to do right now is just
press send.
That's my one of my first for tasks in
the day already done. So now I am
looking at the second mail. So um we has
with ego I had a meeting long time ago.
I have sent him a quote and he replied
back uh saying okay Horina yes I'm happy
for that quote but actually I would like
to increase the quantity in the quote.
And whilst I'm reading the mail uh I can
see that uh uh the dynamics and addin is
able to recognize the um sales quote
keyword and is uh is giving me a context
about that particular quote.
So what I do now I all I need to do is
basically just go and change the
quantity and then send the
email with the updated
code and again all the information is
prefilled and uh NAV generates the PDF
version of the of that
quote. Let's press. We can send it.
Let's press send. Yes. Yeah. So, these
are the two of my um task for for today.
But then uh after I done reading my
mails, I go to my
calendar. And here I can see that for
today I have a meeting again with AO who
works at Fairway Sound, right? And I'm
thinking, okay, why don't I prepare a
quote for him? I know he's interested in
the Amsterdam lamps. and I say, "Okay,
maybe he can uh review it while we're at
the meeting and say, "Yeah, that looks
okay or not." So, uh let's uh open the
Dynamics NAV addin. And notice in this
calendar view, the the space that the
addin has is fairly limited. So, what I
can do is actually I can pop out the the
addin into the browser window. And here
I can do all the operations I would do
normally in a desktop in browser, right?
So um let's create a quote for for
AGO and I uh I am have again the
information filled in for for the for
the AGOS for customer information. And
all we need to do is just fill out the
line. And how many chairs you want or
lamps? How many lamps did you want?
Maybe I'll get five. Okay. Yeah. Okay.
So now the source code is done. All I
need to do right now is to actually
press send an email right and this time
the uh send email is actually uh inside
nav right. So um uh we have also
generating again a preview version of
the quote and uh you can u send this
email uh to ago now
right. So this is how you can uh uh
interact from um from Outlook directly
into NAV. The whole idea is that you
don't need to switch apps between
between Outlook and and NAV to perform
certain tasks,
right? Then of course the next question
probably in your mind is okay where
where do I get this addin? Uh and you
know how do do I deploy it? And uh the
answer is very simple. You can deploy
the Outlook addin directly from
NAV. So if we go back to the web
client and we search for the office
admin management
page. So there we have our two uh
addins. So we have the we have the
document view that is the addin that
when I was reading the email from Ago is
able to recognize the sales quote and
give me the particular information about
that sales quote. And then the second
one is the contact insights. That is uh
uh the one that you open in the mail
from Andrea where you can see the
information about the customer and you
can interact uh directly in there to
create new codes or uh or or um perform
business other business
tasks. And of course let's draw our
attention to the ribbon and there you
find some interesting actions right so
we have deploy addin and uh so but that
will deploy basically the addin that you
are currently selected then then you
have also deploy all addins that will
basically take the office addins and
deploy them and everything happens you
know enough so you don't really need to
do other than basically specifying which
mailbox you need to to install this
addin
on and the Another thing to notice there
are two action that is um uh rel related
to the manifest file that is uh upload
and and download manifest. Of course the
next question would be what is uh what
is a manifest file for the for the
outlook addin. So the manifest file uh
is a sort of a metadata definition file
uh for for the outlook addin and it's
part of the um you know regular
extensibility framework that outlook
provides. So it's it's not basically
this manifest is not a an AV concept per
se, right? We are using the Outlook
extensibility framework here and um
basically you can define the metadata,
the name and description of the addin in
there and also you can define the
endpoints that the addin integrates with
um and also define keywords, regular
expressions um and and so on. And what
happens is when you what happens when
you actually install the addin basically
the manifest file will actually get
stored uh in the mailbox for that
particular uh user or for the whole
organization. And when the addin uh
actually when the outlook actually
starts it actually parses this this
manifest file and uh starts up the uh
addin and also sets up all the endpoints
that the addin interacts with and also
the behavior inside the mail. How the
does the addin surface in the mail? Is
it a context menu or is it just a tab
and so on? That is um that is how the
deployment and integration with the
outlook
works. Then other important thing to
remember about the outlook headin is
that if you are connecting it with with
the web client then you need the
connection to the web client is to be
secure with tl
tlssl also the supported authentication
types here we support azure active
directory and nav username password
uh basically you um you first with the
first sign in you need to perform that
operation on the desktop top. Um the one
other thing to actually keep in mind is
that the there's no magic uh behind the
Outlook addin as such right besides this
manifest file uh you you have all in in
CL pages. Um so um the way to you don't
need to learn your programming languages
for for for customizing the the addins,
right? you just take a look at the CL
and extend those
objects and u yeah that is that is
pretty powerful so um we hope you're
going to to play around with it and and
give us uh feedback right absolutely mhm
and uh well I guess that wraps up your
final demo today yes yes that does so um
basically the message we want to convey
with the outlook addin is that we have
uh we have provided this immersive exper
experience and you don't need to switch
between different apps for performing
your daily tasks, right? Yeah. You just
perform three different tasks involving
NAV inside Outlook in different places
from Outlook and we just without
switching. Yes. Uh you were always
there. Yes. In Outlook was amazing. Mhm.
And I can say this is my coolest
feature. So Ago has wizards and Andrea
is in love with notifications but auto
is my favorite. Yes.
So how do we conclude? So I think we uh
we should talk about what's next, right?
The next item is what's next, right?
Yeah. Uh we have a big disclaimer here
actually, right? Yes. Because we
normally don't talk so much about what
come what comes into our uh future
versions and this is more just some
thoughts right that we have. So um in
NAV 2016 we have begun our journey of
transforming the web client into a
firstass desktop experience client and
what we want to assure you is that we
are committed to continuing uh this
journey because our goal is that we want
to provide a great user experience for
both simple and advanced users. So in
the future we will experience a desktop
client that is simple for for new users
and powerful for um advanced proficient
users when needed. Right? And if we look
for example in NAV 2016 we we have
introduced a couple of shortcuts and we
have also invested a lot in productivity
for users that operate with large data
sets. Um and in NIV 2017 we have focused
also a lot on simplicity. We have
introduced um uh a couple of shortcuts
that I mentioned like F5, control F5,
escape and so on. But looking ahead uh
we see uh that you know we need to
invest also in in uh productivity for
proficient users right like uh
introducing keyboard shortcuts for um
for proficient users for navigation in
lists uh copy paste all of these are are
feature that uh uh we see it as uh as as
missing and coming right and um also the
Other uh important part is about
personalization. With regards to
personalization, it's not only that we
think about okay what can it be done in
Windows client and you know transfer
that to to our HTML uh clients or web
client, right? It's mainly we actually
want to bring the experience to to a
whole new level basically you know in
integrate modern experience with the
process of customizing what the user
actually sees. So um we want for example
to introduce uh um like drag and drop
and show hide together combined right?
So I I drag and drop different fields
and there you go my UI is customized and
and saved right all of these we want to
customization with the tip of your
finger. This is this is how we would
like to to have a personalization uh
coming right. Absolutely. Yes. And that
is uh we got kind of through all our the
items in our agenda. So I think we are
done. Yeah. I have to say that the
outlook interaction was so easy to do
that it was even faster than we thought.
So here we have uh plenty of time for
your questions
now. So yep.
Yeah. Um where's the box? Where is the
box? Oh.
Sorry. Can you see that?
We should have a microphone coming.
Oh, yeah. She's coming. Okay. Where is
the question?
Here. Over there. Okay.
Okay. Thank
you. I love this
thing. So, we're Here you go. Catch it.
Just speak inside it. Just speak. Sure.
Yes, that's cool. Right. Um, one of the
downsides I found from at least 2016
still in the web client is that there's
you're not able to resize a column in
list view. Has that been improved
already? No, we haven't gotten to that
into this release. the to the resizing
of the column. Yes. So it's not it's not
not done but it will be or
we I mean it is it is top of mind for us
but of course there are no guarantees.
Right. Okay. Right. But we know it's
missing. We know we have received a lot
of feedback about that. Yes.
Next one. Okay. You can Oh no. I want
the
cube. There you go.
Uh the other question that I have is for
notifications. Um could you just forward
the notification to different users?
[Music]
What do you mean? Like uh for example, a
sales guy is making an order. He found
that the item is running short of
inventory and he thinks okay I want to
send this notification to my warehouse
guy so that he could Yeah. procure the
goods. Yeah. Uh so at the moment the
notification uh will uh are so uh you
will see that you can set a property in
the notification which is called scope.
Uh uh you can set it to two values at
the moment uh local and global. At the
moment we do not support global
notifications. Uh we only support uh
local notification or contextual
notifications. So they will appear only
on the page where the user is actually
uh working on. So if you send a
notification from uh um from the
customer page it will be shown there and
uh at the moment that's how the API uh
those are the possibilities that the API
is giving to you later we can evaluate
more improvements but at the moment it
it's pretty young API powerful uh but
more features will be will come next for
sure. Okay, thanks.
Uh, why was the decision made to put the
images into a system table and not have
hyperlinks or something like that?
Right. So, if you're using the image
field, we still use the blob, but if you
use the media field, that's where we do
the uh system table. So, we we have two
fields. We are keeping the image field
now. We still have that. We didn't take
that away, but we have a new field
called media. So once you store or you
upload image into it and that's where
everything happens. We generate the
thumbnails and then we store in the
system table. You might have all those
images somewhere else in in existence
that you could reuse rather than
generate them in the database.
Oh yes. Yeah. Basically supporting links
like being able to to specify a link
where the image could be downloaded.
Yeah, we had that in mind but we haven't
reached to that uh functionality right
that that could swell the database quite
a lot couldn't it if you had lots of yes
but normally also it comes to with
different downsides you know like where
is the image stores what's the security
involved and all of this so we have it
in we had it in mind but we just didn't
get to you know complete the story right
I think we also had authentication
problems with that no y
I guess over there.
Okay. Um, will the Windows client become
a legacy client in the near f future
because all the great Sorry. Sorry.
Okay. Can I bring my PMS? Will the other
clients just be greater? I think
I'll um because all the new features you
showed us like the Thank you. the brick
brick for instance it's the first
feature that is not in the Windows
client and this is is this a tipping
point or is this some sign
so yes we I mean it's not that we
basically we will be investing in the in
the web client right I mean if we look
at dynamics 365 for financials right we
we are actually improving the web client
uh and you have web client primarily
there um we will also uh we will also
make to make sure that some of the
features you know like related like
notifications for example some of the uh
CL API right will actually work across
all platforms but in terms of all these
you know modern experiences um we will
probably focus more on the web client
that is for sure right okay great thank
you uh there is there are couple of
hands over there or over there as well
yeah throw it
Oh, I don't know if you should try. What
if it breaks? Wow, we are very good at
throwing this thing.
Another question about uh image or media
uploading because it's generates this
these thumbnails um on the fly. I assume
that it's not possible to upload this on
the SQL level. It has to be done through
the nav code.
You asking about the sizes of the
thumbnails like could you repeat the
question again? But normally you have a
blob field and the blob field is stored
as a SQL image field. So you can upload
the stuff or clear the stuff uh into it
using the some SQL functionality. with
media. uh you said that there is a uh
extra data generated when you upload it
like thumbnailing um and generating many
uh images which will be selected by the
system on on request and because of that
I assume that there will be no
possibility to manipulate load the data
on the SQL level anymore
right but media is actually a blob at
the end because we just store in
different place it's a media table at
the end right it is a blob but it
doesn't store the data as you load it
has something extra added to it on the
load process. Mhm.
You are because I'm loading the image
and you said the system
generates thumbnails and these
thumbnails are selected many thumbnails
and and then proper image is selected on
the depending on what device is
displaying the data. Yeah. Yeah, that is
correct.
Okay. Uh and you uh and the question is
about having access to those. Yeah. So
it's it's already thrown off. So I can't
really do any SQL access to manipulate
upload them or or do some mass action on
the I think the point is that we also so
these images right this image size are
also driven from the from the devices
and the web client itself right so they
are actually predefined sizes. So uh
actually if you if you would even have
this option of changing the thumbnail
you you know the platform still will
decide based on device uh from the for
on the based on the form factor of the
device which uh sizes to actually load.
So, uh I'm not sure how useful that
would be for you to actually generate
the thumbnails yourself, right? Unless
you want to provide some completely
different, you know, thumbnail, but but
I mean we can talk about it later. If
you want to reach us, please do so.
Okay, very good. Box, I have question
about notification. Yeah. Uh can I just
somehow convert the notification to the
error
within life cycle of notification?
Sorry, can you repeat that again? Can I
just convert the notification? Yeah. To
the error within life cycle of
notification.
So you send a notification and you want
it to be converted into an error. Yeah.
in some some stage of uh usage. Well,
what you can do is uh you can send a
notification and when at a certain point
you think it's not necessary anymore,
you can recall it. So the notification
will be removed and you can then uh well
trigger a validation or an error. Yeah,
that's what you can do. Thanks. No
problem. Next. Okay. I I have a question
regarding uh the tool tips. So they in
my experience they are very seldom used
because it's hard to manage them. May
may you have five fields that would get
all the same tool tip and um it's very
hard to
synchronize. So um have you ever think
or thought about changing it from a
property to something else? Well uh so
we we didn't get into that at the moment
and I don't think we have a story for uh
um for working at that level. Uh the
point is that at the moment what you can
do yes you can specify different taxes
on different fields and uh if you
believe it uh you are uh making the
information redundant
uh maybe you you can restructure the p
the page in a different way but um I
don't think we will invest so much in
our next release maybe uh changing this
story uh what we were focusing in this
release was uh to change the way these
these tool tips behave at a at a client
level. So we didn't go deep into the
architecture but let's talk about it. So
let's see what scenarios you have in
mind and what can what what type of um
usefulness we can get out of it. So
yeah. Yeah. Okay.
There are some of the Oh, you will need
a good throw. Oh wow. Oh wow.
Okay. I have seen that you have
implemented something like um email
editor inside NAV
uh when sending an email quote or
something like that. Yes, that was that
is a CL page. Did you consider at least
for future versions uh implementing HTML
editor also or
um so no but I mean theoretically for
the HTML editors you can also build an
extensibility control right? Yeah that's
the situation at the moment. But can you
Oh, you okay? Can you can you edit the
the text in this editor at the moment?
Sorry. Can we edit the body section at
the moment or uh you mean the email
editor? Yes. No, I don't think so. Okay.
Behind
you. Hi. Um in the reports are they used
um the thumbnails of the pictures or
they you can use it print optimized so
that you run a report with 10 or 100
etiquats with the picture that you can
use use it directly on the printer
that's the print optimized the pictures
no I don't I don't think we have a
specific size for using media in the
reports we I believe we are reusing the
uh uh size we used with brick type so it
would be not too big but it would be
bigger enough to be able to see. So
they're only thumbnails you see. So a
screen optimized. Yeah. Okay.
I have two questions. The first one is
regarding the tool tips. Um um as we
have known before the brick view is not
available for the Windows client, but
I've checked uh the tool tip new
functionality is also not available for
the Windows client. It's still a Hoover
functionality there. Will this be
available for the Windows client? So we
decided to improve the the tool tips in
our HTML clients for the Windows client.
Uh we need to see um our um so uh with
our new uh offering for financials uh we
really wanted users to uh u to have a
much better first time experience with
NAV. So that was our main focus and
that's the reason why we really improved
them in the HTML clients for the Windows
client. Let let's see let's see how much
feedback we collect how much this is
needed and we can talk about that. Okay.
And will you fix the the Windows help as
well? Because in the in your
presentation you you showed up that if
you press F1 and the the Windows help
goes on and the the the web help. And I
think in the last two two versions 216
and 217 it didn't really work really
good that the right in the Windows
client. Sorry in the in the Windows
client that the the the correct help
page opens and the user really gets
help. The you mean the contextual help?
Yeah the contextual help. Yeah. Okay.
Okay. So I think one one uh one strategy
that we have gotten from uh from our uh
actually UA team is that uh when when we
when we look in future we uh see a lot
more help available in in tool tips
rather than have you know this
contextual page where you just open one
page and you see everything about all
the fields right so we're moving away to
this strategy so I'm not sure how much
we'll actually invest into this into
into the Windows client Okay, my other
question is regarding notification. You
you told us that you can recall
notification if it's not anywhere of
use. Um if you um have a look at the
sales um um document and sales order and
if you create a line with let's say
10,000 pieces, you get a notification
that they're not on inventory. If you
remove the the quantity to one uh again,
then the notification will stay. So are
you going to improve that logic
yourself? Yeah. So as we moved a lot of
our logic from using dialog to
notification, it's possible that we
missed something. So yes, we will
improve that because I don't think
that's any recall at the moment because
it's the same for the credit limit. Uh
check. Okay. Yeah, maybe an tip.
Feedback taken. Thanks. Okay, next one.
Okay, one last question.
Hello.
One. Cool. Um hi there. I I actually
have a question um for both
notifications and tool tips. Okay. Or uh
maybe a suggestion.
Uh could we hope at some point to have a
cross breed of the both of them like u
being able to uh add a bit of code into
the tool tips rather than at the top of
the window?
Uh so uh it's a formatting
uh like a like a markup question related
right? Um so you would like to display
some code in the web. Yes. Yeah. So uh
again we uh you should uh be aware of
the fact that tool tips should provide
kind of an immediate help and a
description. They were not really
designed to uh uh to display very
complex content. For that you can
probably move that to the help pages so
that the user can reach that from the
from the learn more action. But do not
overload tool tips with too much
information or too long text. They are
meant to be uh uh first glance help uh
just a very fast uh guidance for the
user. If more is needed then you can
move that to the help page. So it's
going to stay. So yeah I I don't think
we're going to invest too much on that.
Okay. Thank you. And the other the other
one you had two questions. No, no, no. I
it was, you know, because I was like
moving the code from notification into a
tool tip or vice versa. Okay. All right.
Uh I don't know if we actually I think
we're out. Thank you. Yep. Thank you
very much. Thank you very much. Thanks a
lot.
