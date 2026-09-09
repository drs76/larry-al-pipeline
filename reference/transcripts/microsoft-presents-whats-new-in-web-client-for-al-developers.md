# Microsoft Presents: What's new in Web Client for AL developers

- **Source:** https://www.youtube.com/watch?v=cteMH9MUNRU
- **Video ID:** cteMH9MUNRU
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 42m11s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

Ladies and gentlemen, welcome to today's
afternoon session. Please welcome on
stage our next speakers Thomas Herrerida
and Vasil.
[Music]
Thank you. Welcome everyone to what's
new in web client for AL developer
session. I'm Thomas Gublauskas. I'm
engineering manager at business central
client team responsible for web and
mobile clients. And here today I have
with me Arita.
My name is Arita. I'm a software
engineer in Thomas's team. Yes. Uh what
we're going to talk today is a bit of
product productivity updates in the web
client specifically. Uh that's the part
where from the AL developers
perspective, you don't have to do
anything. You just get them for free. Uh
but it's always good to know how to use
these features, how to present them, uh
and educate your users how to get uh
best use of them. Then we're going to
step into a part where we do have some
new AL concepts. uh and where we're
going to show how to utilize them from
code. And lastly, we'll talk a bit about
partner telemetry, what's new in there,
and we'll also be have the usual uh a
bit of from the lab section. Uh it's so
secret that it's not even on the agenda
now. Uh so yeah, let's start with
productivity updates. That's the part
where you don't have to do anything and
you get all the goodies for free and
Arita will show them.
Nice. Let's get started. Uh our first
productivity update is in roll explorer
and report explorer. As you know role
explorer and report explorer is the best
place to go to if you want to explore
pages and reports that are available in
business central not just for your role
but also for different departments and
different profiles.
So we know that when you look at that
big overview sometimes it can get a bit
overwhelming and throughout different uh
past releases we have edit features that
make that a bit easier for you such as
allowing you to find things in in RO
explorer and also filter according to uh
usage category or department. But we
know there's still improvement to be
done and that's what our most recent
update is about where we have added new
rich tool tips in role explorer and
report explorer and these are based on
your pages about title and about text as
you have defined them in AL as you see
in the picture on the right. Um when you
have such information available as soon
as you hover over one of these uh links
to a page or report uh you will see this
info icon showing up and when clicking
on it this information will be available
with the about title and about text.
Also keep in mind that uh this tool tip
supports markdown. So sometimes uh in
your description you might have a link
to another related page or report. So
that's supported as well. something else
which is available in this tool tip as
you see this um icon over here but also
for the pages that don't have these
properties um supplied provided uh we
have the opportunity to open things in
the new window and why that's relevant
is because of course you're looking
through roll explorer report explorer
sometimes maybe even the tool tip isn't
enough to understand what the page is
about and you just want to open it and
figure it out so what would What
happened before is you click on a page
and then you find out it's the wrong
one. Maybe not what you're looking for.
So when you go back, you're no longer on
roll explorer because it has just closed
up behind you. Now if you're just
looking around trying to figure out what
page you want to see, you can just click
this open a new window icon and you
remain in the context that you were in
while exploring all these pages and
reports and you also get to see this
page or report um that you were curious
about.
Nice. The other one is new page sizes
for modern screens. So, as telemetry
tells us, as we also see, we are using
bigger and wider monitors. And a guy in
my team even has a monitor big enough
that we all call it a TV. So, it
literally is a TV. It is a TV. Um, so we
need to make the most out of it. And
truly, we weren't really in business
central especially when you open pages
in slim mode. um you had to compromise
between either showing a page with two
columns of data or opening the fact box
and seeing just one column of the data
and then the margins on the side that
are unusable would be huge. So we know
that's not the optimal um choice and we
have delivered improvements to that. As
you can see in here, this is the new
slim mode. it has become wider uh and
you're now able to even in slim mode
look at anything that's in your fact box
all the relevant information that you
have in there while also having a great
overview of all the fields in the page
next to it. Um some other changes that
we've done in here are also changing a
bit and improving the ratio between how
much space the uh caption of a field
takes versus the value so that you can
read more of the caption before it gets
truncated.
So my laptop here is quite narrow on the
screen and I just wanted to show you
this before and after uh of what it
looks like. So you can see on top um the
previous size for the slim mode where we
have a lot of space on the side and then
with the new those margins have become
smaller. But I think where this feature
really shines is the second screenshot
over here where we go um from this very
slim page with a factbox opened to a
wider page that allows you to view more
data at the same time while also having
the factbox open.
Related to making the most out of your
screen estate, uh we've also enabled
factbox resizing in a previous release
and in this one we also enabled keyboard
keyboard support for resizing. So you
can just shift F10 to do the same thing.
What keyboard uh what factbox resizing
allows you to do is that you get to
choose how big your fagbox is on the
page. Sometimes you have as I have in
here in the case of the uh payables
agent where we have a dis um the PDF
previewed on the side next to the lines
and you want to see them side by side.
If you make the fact box wide enough,
you can truly read anything in your
preview and just compare it over there
without needing to open the uh PDF.
Also, you might have some very valuable
control add-ins with information that
you want to see while you're using the
page. So, this is also great for that.
Uh what happens in here is that as you
choose this preference of how big the
fact box should be on a page, we
memorize that and it's memorized uh
separately for the slim mode and for the
wide mode. So wherever you leave it,
that's what you come back to. And the
factbox is just as you prefer.
Um just to note, it's being stored in
the local storage in a browser. So it's
not part of your profile or
customization. Uh so this data would be
cleared if you open a new uh for example
in incognito session. So if I log in
from Thomas's computer I won't get my
preferences anymore but I can make new
ones. Y um yeah and it's also important
to note that this is available just as
you open the page and you see it. You
don't need to start personalizing or
designing to resize which is also great.
So let's go ahead and see all of these
in action inside the product. Starting
as we said from RO explorer or report
explorer uh you have these new icons
available here but they as we said
they're very valuable when you go and
look at what's available for all of the
roles and as I said once you start
hovering over these links you'll see
this info icon that's showing up and you
can show more information about these
reports and you can learn what they're
about and even for those um pages that
don't have those uh about title and
about text defined you can just open
them in a new window. So, while that
loads, you're still able to use Roll
Explorer in here. Go around, maybe open
another page and the page that you went
to was just loading in the background
and it's ready. Once you're done, just
close it. Go ahead. You don't have to
worry about losing your context in all
the searching that you were doing. Uh
then for example if I open the vendors
list we're able to see those changes
with the uh slim mode and how much space
it is giving me allowing me to work
with. So this is the slim mode right and
I can even if I open one of these vendor
cards I can see that uh if I go in the
slim mode the page is still quite wide.
I have resized previously the fact box.
So it opened exactly where I left it
off. But if I want I can just make some
more space for my fields. And when I go
back to that wide layout view, um the
preference of the fact box would be just
as I left it over there. Um and my
preferences are saved. So let's go to
the next one. Thomas, yes, you can just
advance. Uh a new shortcut. Uh this
actually has a long story. It's almost a
year-long story for this shortcut. Uh
not the time it took to implement, but
where it started. This was actually an
idea from you the community. Uh last
time we were in BC Tech days. I really
would like to remember the person's name
who suggested this to me. Uh I cannot.
Sorry for that. But if you are in the
conference, I can find a t-shirt for
you. Uh so the idea was that it's really
painful to copy values from read only
lists because by default what happens in
a list is that I'll just zoom a little
bit and if I am on a row and I click
Ctrl C to copy uh entire row is copied
and most of the time that's what you
want. Uh but in some data entry
scenarios you actually want just the
cell value and well technically it is
possible to do that. you will need to do
a bit of a mouse ninja and you can
select the text uh in in the cell and
then uh click Ctrl + C and you'll get
the value copied. Uh but that's painful
uh especially if you look using a
trackpad like I I do today. Uh so now
instead we have a new shortcut which if
I focus the cell value and I clear
control shift C, it's going to tell me
that I copied the cell value and now
it's a lot easier to transfer values
outside of BC face. them in emails in
teams. So, thank you community for this
great idea.
Uh yes, I can help. Guess you can
advance in slides. Um another thing that
we built on top of is KTIPS. Uh we heard
loud and clear through feedback that
shipping kips only in English was very
limiting and there's plenty of beautiful
languages in Europe and abroad uh and
beyond that uh that could really benefit
from KTIPS. Uh so we have extended ketip
support into many other languages. We
started just looking at telemetry and
looking at the most used languages and
we started from there. Uh so languages
like uh German, French, uh Spanish, uh
Scandinavian languages, Danish,
Norwegian is now supported. Uh it's not
just flipping a flag for us. We actually
do spend a lot of time figuring out do
these do the does the system we created
for generating these key tips make sense
uh because you can understand that
changing it afterwards once it's shipped
is very painful. We really know how uh
how important it is to have stability in
the system. So all the productivity
shortcuts tips you you your users have
learned it stays consistent between
versions. So that's why we are rolling
kind of slowly. Next thing that we're
gonna most look uh likely look into is
just by default enabling all Latin
character based languages. U and I'll be
very happy because on the list somehow
lifer and my native language is not
there. I probably missed a meeting about
that. Uh and this was also something
that was asked in BC Tech days when we
presented key tips. So we deliver. You
ask and we deliver. Yes. So be sure to
ask questions after the session because
we listen. Uh yes. Next, modern search.
I actually also had conversations about
that in the last BC tech days. Uh it's
not only our team's uh contribution to
this. We work together with server team.
Uh but we have finally found a way to
introduce more modern search that
doesn't have the same performance issues
when we are dealing with really big data
sets. Uh because we basically would run
into cases where there would not be no
no mitigations. The the only thing was
add filters. Don't use uh the search in
in the list page otherwise your tenant
might be busy for for a while. Uh so
modern search is smarter. It's free text
uh based. It's also uh optin. Uh you do
need to first of all enable this
feature. It's still in preview. Uh it's
scheduled to be uh GA in 27. Uh that's
still a bit of a question. uh we're
still looking for feedback and like to
hear uh how you're using this feature.
Uh because I actually asked a poll uh on
the session and I'm seeing last time I
checked was 20 responses and half half
people are have this enabled and half
are not. Uh so I probably would be
interested to to hear after that from
both sides people who are using it and
from people uh for what the reasons are
of not using it yet. Uh
right. Uh if so the way uh the opt-in
works can advance to the next one. Optin
works is that by default we tagged bunch
of fields in our uh application with uh
with new property that includes fields
into the index for this feature to be
enabled. If users ends up on a fe on a
page where uh this is not tagged, it
simply falls back to the old behavior.
Uh so this is opt-in. Um and you can
also uh use that from code. That's the
bottom example here. So you can use the
new modern search example from code as
well. So let's look quickly how that
looks
in the product. Yes, you can see my
screen. First feature management. Of
course, I need to have the feature
enabled. You should be very familiar
with this page. Trying all the latest
goodies from us. uh search
and yes it's enabled for all users for
me so that's very good and I'm going to
just show one typical example of I'm a
new user in Business Central I have my
items list I have bunch of items in our
demo data that's uh furniture and I see
I have some chairs but I specifically
would like to find a green chair
huh I don't have any green chairs
But is that true? I think I have green
shares.
Well, with modern search,
I do have green shares. Uh because the
search is a lot smarter and it's trying
to match uh onwards. Doesn't matter in
their order. Um and it's not the same as
it was. I can also see which fields have
been included in the in the search.
That's a little bit of tip. Uh a new
thing that we added along the way is we
are showing uh like a search mag
magnifying glass to show which uh fields
are participating in the search. And of
course if you have some uh some
behaviors that you have from old uh
behav from the old search, you can
always just quickly switch back to the
Lego search and it's going to work the
same way uh as it was before.
Cool. It's been released last October. I
just want to resurface it again. Please
start using it. Give us feedback. Uh
this is the way to make this faster and
solve the performance issues that we see
from time to time in in production.
Yes,
the next slide. Yes. Perfect. Uh new
things. This is going to be just a a a
quick uh sneak peek because there was uh
it was shown in a in a keynote and there
will be a dedicated session that I will
uh plug after this. But we also are
adding a lot of productivity features
using copilot. trying to find unique
ways how copilot could be providing
value for users entering data and
autofill is the first really awesome
example of that uh where co-pilot is
working together with a user and is
helping them to fill in data quickly uh
we are able to track uh patterns of how
user center data um what most commonly
values values are set in the company and
copilot is able to provide really smart
defaults and fill out entire forms uh a
lot more efficiently
That's one of the features. Uh the other
one is summarize. Uh again with copilot
we are able to provide a summary of the
entire page content and hopefully
highlight the most important bits that
users should be aware or should act on
on a page. To learn more about that uh
tomorrow there's an awesome session uh
from Monica and LIL who going to really
dive deep how that works. uh for now
there's no development story so all
everyone gets that for free but that's
still something we also thinking about
how these features could interact with
your IP as well. Cool. Um so now let's
dive into a section where we you do have
to do something to get the value out of
the features we're building. So let's
talk about all the new AL APIs that we
have added or changed.
Good. Let's get started. One thing that
you've already seen in the keynote uh is
that we've added the ability to preview
PDFs within Business Central where you
don't need to any longer download them
and then check them out. We know it can
be very tedious in processes where you
need to do this very often to look at
PDFs and then the old flow would be you
need to download the PDF, have a look at
it uh in your computer and then next
time you come to the same record and
have to view that PDF again. Well, you
either download it again or you have to
go and uh look into your file system
which takes time. So now you're able to
just uh add the opportunity the
capability of uh previewing PDFs just
within Business Central and it's proven
very useful to us for both of our
agents. We've used it quite a lot and
you can do it too anywhere you want with
this code snippet. So we have two
different procedures that we've added
for this one for BC onrem where you can
uh use the file view from stream
procedure uh and then just apply the
instream the file name and in BC online
environments you can use a very similar
procedure called file view where you
define from what file uh you are looking
to view this from and I have a snippet
on the right that shows uh shortly how
you can view a PDF for your of your top
10 customers report. And all you need to
do essentially is just uh create an
outstream uh save a report from your
customers top 10 list into uh the PDF
format into your outstream and then just
create the instream view it uh the file
from the stream using this new procedure
that we mentioned. What's important here
is just that one line where you call
this file uh view from stream. I'm not
running any code now, but as I said,
we're all already using it quite
extensively uh with all of our agent
stories. So, if I just go, for example,
into the sales order agent, um you can
see email from Alicia. No, that one I
didn't care about. Um in the email
that's going to Diane, I can show the
attachments. It's a sales quote PDF.
Just click on it and then you can see it
directly in Business Central. And of
course, we support uh many of the tools
that are available for other pre uh PDF
previewers as well, such as uh
navigating between pages, zooming in,
fitting it to the width of your window,
to the height of your window, moving it
around um if it's zoomed in, and then
downloading and saving and printing and
so on. So, it's quite useful. We're
using it. I suggest you start using it
as well.
Uh the next thing that we have for the
AL changes that you can uptake is
changes and updates in our barcode
scanner. So we already supported quite a
lot of barcode uh formats. Um and you
can see a list on the left side of the
screen. But what we also did is we added
support for specifying what format you
actually want to scan in AL. And this
was also from a partner story. uh
partner reached out saying they were
trying to uh scan a specific barcode. It
was working great on iOS and it was
picking up the right format and just
getting the rights code. But when they
tried on Android, for some reason, it
thought it was another format and it was
just doing it wrong. So, we added this
new procedure where you can specify what
barcode format you're looking to scan
and then you just make sure that we're
focusing on the right one that you need.
And you can see it right here. It's just
request barcode async and you specify
the barcode formats as the first
parameter. Um a little code snippet of
how you do that. Again, the most
important part in this one is that in
your page that you're adding this um
control addin, you define this user
control with the camera barcode scanner
provider addin and it's just a trigger.
When your addin is ready, you just need
to call the barcode control request
barcode async. And you will see in this
example for example I've provided two
formats uh the QR code and the data
matrix and that should be it really a
very simple change that we hope um
really helps you succeed in all your
scenarios.
Next up yes a new page type. So we don't
do that uh that often. Introducing a new
page type is usually a big step for us
because whatever we add it has to stay
there for a long time. Uh but we think
that control addins has finally matured
to having their own page type. uh
because so far we have been relying on
having all kinds of semi-hidden I mean
documented in documentation but not so
straightforward for AL developers to
discover patterns uh how to display
client add-ins for example there was a
pattern and still is uh if you have a
card page and the only control is the
client addin or user host control uh
then client addin is going to show as a
full control on that page uh but then
there would still be a lot of unuseful
crust on the page that would not
contribute to the usefulness of the
page. Uh so we finally thought that this
is the time uh we have a really
important use cases on our end as well
to uh make this a precedent. Uh so we
introduced a user control host page
type. The pattern is very similar. Uh
still only one control that can be on
this page is client addin. And by having
this client page uh type first we can
start uh not relying on
documented but not maybe well-known uh
hidden patterns how to display client
add-ins. Next we can also uh since we
have a dedicated display target we can
start optimizing the page for displaying
the client addin. Uh so we can removing
unnecessary like top header UI like a
new action uh edit and different modes
in that as well. Uh yes for now this
page type is still a bit locked down. Uh
you cannot extend it uh you cannot add
actions to it. Um but as we are uh
playing around with this new page type
and also hearing from you how you're
using it uh we'll be uh opening up some
of the things and maybe adding more
things specific to client addins uh to
this to this page type. Uh so we are uh
really looking for your feedback uh how
you using it. Uh for example I think the
first thing that someone asked was well
could you make it really full screen? Uh
that's a good idea. Uh maybe that's
something we need to consider. Uh yes.
So the first
use of this was embedded PowerBI
reports. This all of this experience is
built uh on the new user host uh page
type. Uh and I'm going to show you how
that looks. I'm on mine.
Yep. As you can see, there's nothing in
the header. Uh there's very limited
actions on the side as well. You can
bookmark the page, you can pop it out,
you can make it wider. In this case,
it's not going to help just because of
my resolution. Uh there's page title, uh
subtitle, and everything else is left uh
for the report to fill in. Uh so we're
using it internally. Um at least for
now, it serves our purpose. But of
course we would like to hear uh what
kind of scenarios you have uh what
you're missing, what you would like to
have uh see in this new page type.
Yes.
Let's go next.
Yes. Telemetry.
Thank you. Uh something new in our
telemetry uh also related to client
add-ins is we added a new event called
CL00005.
Uh
what it means is we are finally
surfacing exceptions from client addins
uh to partner telemetry. So it's easier
for you to monitor how your client
addins are behaving in production. Uh
you also can get a signal if some of the
client addins importer from different
partner extensions are also misbehaving
in your tenant. uh you get a mostly for
I guess for AL developers not familiar
but for JavaScript developers familiar
uh exception stacks uh that you can
analyze and it's we hope is going to
help uh you to discover uh what is
happening in client add-ins uh because
sometimes they might be the source of
some of the performance problems uh or
maybe pages being stuck uh and it was so
far not visible because it would not
show for example in AL errors uh If
JavaScript is is misbehaving in a client
addin
uh yes uh other point
[Music]
right uh client addin exceptions uh I
thought I had some some really good
point about that maybe not talk about it
in the end just talk about it so now the
hidden part uh of our section from the
lab exciting session I think it's become
a tradition now that we show you a few
things that we're working on always
under the disclaimer that things can
change. They may be shipped differently,
but it's still fun to have a look at
what we're doing. So, first thing that
we wanted to show you from the lab is
actually the um capability to collapse
panes um in business central. This is
relevant and actually this started
because uh as you know we do a lot of
accessibility work trying to keep uh
business central everywhere accessible
and we also have to support users that
are uh zooming in for example to 400%
and they have a very small window and
they need to be able to use everything
in business central so the item card and
the help but also any one of us when
you're trying to use business central uh
side by side with some document maybe a
word excel um whatever you need then the
window becomes quite small and as you
are working with the these panes
alongside uh data entry or anything else
you might be doing the space that you
get left over for the main page is
actually quite small. So what this
brought us to is just adding the
capability to collapse any pane not any
pain these three panes that I mentioned
and probably in the future also the
other ones. Uh so we've added this uh
button that you see right next to the um
close uh button which is the button that
collapses the pane and then what happens
is from taking up all the space the pane
actually just switches to this very
narrow ribbon on the side. It's not
closed. It's still there. All of the
context whatever you were searching for
in help is still there. It's just not
taking up that space anymore. And
anytime you need to get back to it, you
just click on that uh question mark to
reopen the help pane. And as I said,
this is also available for a couple
other panes such as page scripting. Same
thing again, the same button, the same
scenario. You just have it uh on the
side. Finish anything you need to do in
the main page. Whenever you need to
actually do something in the pane, just
go back and open it. Similar thing with
our co-pilot pane with the tasks. We
have a lot of scenarios in there as well
where you need to look at uh the tasks
side by side with um the page that
they're related to. That might be your
sales quote, your sales order, your
purchase invoice, whatever it is. And if
your window is narrow enough, you think
you don't get enough space. Again, just
collapse that pane, get back to it
whenever you need it, it will be right
as you left off.
Another thing is we just showed you the
ability to preview PDFs within Business
Central. But the thing is when we first
added that feature, we didn't really add
support for password protected PDFs. So
you'd have to do that same old thing
again where you download things and then
you go looking for them or you
redownload them, which is not fun,
right? If you can preview PDFs in
Business Central, why not preview all of
them? So now we've added uh support for
that and we just show you this native
dialogue where you can type in your
password and if your password is correct
you just PD uh preview that PDF as any
other within business central and we can
see that right here. Uh so I did add a
very secret password protected uh PDF to
this uh customer and I can see it here
listed in my attachments. So, if I click
on it, I'll get this enter password uh
dialogue. And if I type random things in
there, it won't let me see it. Of
course, we're not playing with security
over here. But if I do know what the
password is, hoping I do remember. I try
again and it works. And the secret is
that the PDF is password protected.
So, yeah, that's it. When you're done,
of course, you can close it. Anytime you
try to open it again, you need to type
the password again. We're not playing
with security. And that's it for PDFs.
What else do we have from the lab? Yeah.
And just about a PDF, it's a feature of
a PDF. So it's not something added on
top or from AL or business central side.
This you have to do that at the
generation of PDF time. Uh it's inbuilt
feature of PDFs. Uh yes. What else? For
all the demos we do, it might look that
only thing we do is copala that copala
this uh but actually there's a lot other
things that are very important to us as
well uh to improve security of course
being uh number one priority for
Microsoft. Uh but we're also seriously
looking at performance and trying to
make our minimum bar is to make it
faster each version than it was before.
Um, and from from for the client team,
we also have some work to do. And we're
continuously trying to uh
make the client cleaner to make it
smaller. Uh, because we definitely see
that it's an issue for uh slower
machines or users using slower network
speeds. Uh, because also every time
there's a hot fix, all the scripts are
new again. So, every time you open your
laptop on Monday, well, you need to get
all the new bits. uh it doesn't
necessarily happen on a Monday. Uh but
every time there's a new version, you
have to download them again. They cached
with your browser and subsequent open is
better. Uh but still that initial hit is
just a lot of unnecessary work that we
would like to minimize. Uh so in our
journey, one of the things we really
wanted to do first was to get rid of
jQuery. Uh a bit of backstory in mostly
web development is jQuery was the one
tool the one dependency that everyone
had in that their web pages because it
was doing a lot of awesome synthetic and
sometimes implementation sugar or over
very immature web APIs but over time web
became a lot uh smarter more powerful
and now we running full uh ERP software
and SMB software in in the browser
that's how far we went but we kept Jack
jQuery along the way with us with the in
the journey. But finally, we figured out
that now is the time actually we have
mostly everything we need uh in the
standard browser APIs and we don't need
jQuery anymore. It's just another
library that we're taking dependency on
and from security perspective that's one
just broadens our attack surface. Um
every time there's vulnerability
reporting in jQuery, well we need to
ship we need to produce new on-rem uh
builds as well so everyone can update
it. Um, so it's a it's a tax to pay. Uh,
so now we don't have jQuery anymore.
Yay.
What that means for Yes. What that means
for end users uh is a smaller bundle
size. There was a lot of code that was
not used anyway. Uh, so now that's just
simply cut from the bundle. Uh, that's
top of my mind maybe 200 kilobytes off
from the bundle size and it on slower
networks it really matters. Uh another
thing is uh we in general try to reduce
uh client bundle size. We're trying to
figure out different ways how to
modularize our code better uh so we can
on demand import code as we need. For
example, one of the examples of that
would be uh designer and personalization
experience. So actually if users are not
using it, it's completely unloaded and
not active in in the web client. the
moment you click on it. Uh, of course
the downside of that is the moment you
click on it, then we need to get all the
scripts for that experience and that
initial entering that experience is a
bit slower. Uh, but that actually
happens a lot less than everyone else
paying that tax every single time they
opening web client. U so that's our way
to reduce client bundle size trying to
be a lot smarter distributing it. I
would like to be able to show some
numbers but it's just a continuous
process and we usually can take
snapshots at end of the releases and now
we're kind of in the middle of it. Uh
then as well for the next wave we have a
goal was kind of continuous goal to
always try to see what is the next 20%
we can cut in page running times as
well. Uh what we can make it how can we
make it more efficient. Uh because again
for fast devices it almost doesn't
matter. uh if you have the latest
hardware, it's so fast that all any
efficiencies are just covered by by the
hardware doing all the hard work. Uh but
accountants is probably not running on
gamer PCs or even uh latest uh I know
surface books. Uh and we need to
acknowledge that and that's why we
always keep uh looking for opportunities
to make uh rendering faster. Uh yes. And
lastly, we're also looking again at the
network. uh we're trying to see how we
can do more with less network requests
because every time we need to go back
and forth even though we are using
websockets that we don't need to open
HTTP uh connection every time uh still
we can be a lot more efficient uh so we
have made some improvements of how many
initial rows we have ready on the page
so we don't need to fetch it and do this
dynamic loading uh and it's helping our
telemetry showing that all of this is
slowly trying to build build by build uh
making everything faster. So yeah, and
that's it. Thank you all for listening.
This was a big uh overview of all the
new things in web client for rail
developers. Thank you. Thank you.
[Applause]
We do have some time left over. So if
anyone has a question and they have
questions, I don't think I'm the good
right person to throw. Uh actually, do
we have t-shirts? We have been promised
three t-shirts. Promised t-shirts. I
I'll start throwing. And then we'll
figure out t-shirts.
Yes. Uh users, they like the new key
tips or keyboard shortcuts.
Uh but they are annoyed when they're not
the same. For instance, in uh a
worksheet page, you can use the Windows
uh shortcut shift delete for deleting a
row. But in a an editable list page this
the shortcut is alt cd.
Why is that different
every time? So we have an algorithm and
arita knows a lot about how it was
implemented. Uh but the design goal of
it was that it is adaptable. It's we try
to thank you. Uh we tried to make it as
persistent as we could along the pages.
But if the layout of the page meaning
the controls on a page that are active
is different, it's going to there's a
chance that the generation will be
different. If you really want to lock it
down, application keyboard shortcut is
the way to go. Then it's not going to be
changed. It's going to be stay uh the
same way all the time. But we have tried
to create some consistency throughout
pages. So there's a lot of that dynamic
determination of what the key tip will
be that is determined for everything. We
typically try to prioritize everything
that comes first because those are uh
centerm first and foremost but we have
tried things uh like on every page that
you open creating a new uh record should
have the same shortcut and I believe
deleting should also have the sh same
shortcut so if you just come by and let
me take a note maybe it's something that
we can fix and make that the same in all
different pages I know we have done that
for a few things because as Thomas said
once people get used to it and you
create the habit we really don't want to
break it for you So for those things
that are used quite a lot uh we we do
support having the same um access key in
different pages.
Thanks. Let's try
uh let's try that.
Yeah. Uh one question you have mentioned
that you will be we will be able
basically to preview PDF files but in
future would be an opportunity to
preview any other different types of
files for example word Excel maybe
pictures whatever else to preview mode
that's an idea we just need some votes
on that and then we can see how we can
prioritize the the f file types
technically yes uh that could definitely
be possible to do uh but currently is
this new function that is customiz
ization. Is it like limited to PDF files
only or we can try to send there
something different? No, just PDF files.
I think this one is limited to PDF.
Okay, thanks. Let's trade.
Oh, next up.
So, here
Oh, sorry that was a headsh shot.
Um, I have a question about the new PDF
preview. Um if I update the report
layout um does this affect um existing
previews or need they to be reloaded?
I don't think that's related like we
just displaying PDF as it is. Uh okay
but it was attached as a file or and is
this created every time I open um a
page? No, because if a report layout
event the hot fix is made in a layout
and in the preview for the customer the
hot fix is
still not shown or does this get updated
when the report layout is updated. Uh so
the way the API is that you always
streaming data the new data so I guess
it's up to you. We could discuss the
scenario a bit bit further but we always
show the up-to-date version that you
provided through streaming through the
API. Uh so whatever is the view in the
data that that's what we're going to
display.
Okay
let's discuss
next question. Hands up. Yeah. being
blinded by the light. So, excuse me.
Can you get it a bit closer
and now? Yes. Okay. So, also question to
this PDF thing. Uh so I'm wondering
maybe if it is possible or it will be
possible in the future to print PDF
directly
like not to open preview and print just
to call some command from code and to
print it to some printer that's already
possible through different APIs uh
through cloud printing that would be the
way uh to go
okay on premise
yeah don't have comments for
Thanks.
So, I think we have three more minutes
to our next session. Maybe we take just
a couple more Yeah. questions and then
we switch.
Um, are there any plans to for the
future to improve the tell me search for
example adding a fuzzy search to it or
search history?
That's uh something we could have
included in from the lab. Yes, we are
very actively looking into that.
I think we need to stop here because we
need to set up for the next session. Uh
but now you you see you know our faces,
our names. Please find us somewhere in
the conference or in the Microsoft
booth. We're going to answer more
questions. Thank you. Or just write them
on the Hoova session. We can also have a
look there. Thank you. I can help.
