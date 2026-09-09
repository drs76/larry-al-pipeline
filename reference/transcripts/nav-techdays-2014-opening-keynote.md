# NAV TechDays 2014 - Opening Keynote

- **Source:** https://www.youtube.com/watch?v=xrq83fFNsA0
- **Video ID:** xrq83fFNsA0
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 101m55s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

whenever thomas and i arrive here
at tech days we enjoy reading the uh
the movie quotes outside uh
and the most famous one of is of course
i'll be back
but we wait for it that we are back all
of us
and the the other one is make my day by
clint eastwood
but you already made our day because we
have 800 people here
sharing where we are going to share with
you the uh the latest bits of of nav
but also i think it's an incredible
effort that luke managed to gather as
much people as many people here
every year and
the venue keeps growing and growing
so first of all let's give luke a great
applause to
make sure he does this again
[Applause]
those of you who have been been here
before knows that we usually have this
long agenda and will not make sure half
of it so
this year we are going to cheat a bit
and uh throw up the topics that we are
going to look at so we are going to look
as seaside improvements as always
a new reporting story uh something about
the client architecture
where we start of course
a new big thing about upgrade on the
system and also the the roadmap for
moving forward
and then
as usual we're going to show you some
stuff that might make it into the
product and might not but it's it's
really interesting
uh we're going to share this it's uh in
sort of whiteboard form right now but
it's a it's a big thing that we want to
explore
okay
so let's go right through it
so
let's go into seaside
so during the
2015 release we we basically took the
whole team uh out for two months to do
test automation of the local versions
because as you know we now have these
cumulative updates every month and in
order to
accomplish
testosterone that we put the whole team
on writing cl tests
for two months
and by doing that we found some areas
from improvement in seaside
because there's
some cumbersome things that you all know
exist in caesar right now and basically
been there for for 20 years since we
wrote it back in
in 1994
but let's look at some of them
so it's not random i selected this
report and i'll show you
why
the deal is that
in seaside it's very cumbersome if if
you have a
page and a subpage
and you're on the sub page and you want
to
update the main page
it's very cumbersome to figure out how
to do that without having sort of an in
this loop or not updating the main page
so what we did was to
introduce a new property called update
propagation down here
and this you can update the subpart as
usual but you can also
go to the parents and update that as
well
and the reason why i'm showing you
especially this form at this page is
that
this feature came in relation late in
2015 so we only made it to put it into
this one
but it's up up to you to use it all over
the place
another thing you can see in here is
that uh
all the properties that changed in here
they are bolded and the ones are not are
not bolted of course
which makes it easier to overview what's
changed and what's not changed in here
another thing that
you you need all the time is
if you select something
of course five years ago we made the
invitation where you press tab and then
of course back
that works but what if you want to
comment something
then you just press ctrl shift
k and
oh to get it back so
[Applause]
we're not done yet
so let's go to
the global menu in here so
let's do
something in here so
you can see i put the name to the right
instead of having in front so
the deal is if if i
use record in here and i want customer
oops
it's quite cumbersome to have to repeat
the name again
so it autofills the the name of the the
of the record to be the same as the
table name
uh as default of course if you need
customer two you go in and edit that but
that also saves a lot of time especially
if you have some of these
german table names with all the uh
periods and and what have you in this uh
so this also is a particular game that's
that's in there
also if you go in a new function
we now have
local as yes
because in the old days
local was no and you had all this
function that didn't make any sense to
see in the
simple menu
that's all now hidden because
every time you create a new one you
forget to set this flag to
yes and then it's all over the place so
again
it makes the system more visible
to to work in
[Music]
so yes we uh we spent two months in
seaside all of us
yes still want to update to notepad on
the editor yeah we'll get there thomas
okay
but that's not all so let's move back to
the slides so
so beyond that we we actually started
using xml port internally
for real production code
and some annoying thing is that you
sometimes need the corn path in there
and of course you can create that
yourself using ale but
but now there's a function to to get
that at
your hands to uh
to write your code
[Music]
another thing is that we
when we did this dynamics online
payment services
we made an encryption library in in
there
and we also
saved the password and database
and that's really not handy because if
you take a back off of your database
then you also take a backup of the
password and
it's somewhere that you cannot control
yep
i think we put it on automatic shift but
okay
and since we did the mca integration amc
integration for
can you fix this thomas while i speak so
i told you you you ruined my flags when
you started so you do this every year
um
anything else you want me to fix
we'll we'll get to that so
thanks
so instead of of doing the same mistake
over again and uh and creating a new uh
way of doing that uh in in the app we
created a
encryption library uh and basically
there's a set of function where you can
create an encryption key and that's
basically creates a key and put that in
in the folder on your server
of course you can delete it again
and also you want to be able to export
it because you want to have a backup if
something happens to the server
and you want to import it again
then when you want to use your unit you
use the encryption able to enable it and
then you can also ask if the
key exists
and that's very useful if if you run
multi-tenancy uh the deal is that you
basically have to run this on every
server
right now in 2015. we're trying to fix
that in a future version but right now
you have to run it on every server
there's some control mechanism in there
if you uh by mistake create
different keys on two different servers
you
uh of course you cannot use encryption
it will it will block you
and if you just have uh encryption key
on one server and not the other it will
also block you from using it
but this is to get you going and then of
course
the caveat you can now go in and use the
encrypt and decrypt functions
to uh do what you want to do
but go into the sample menu and play
with these there's also quite some good
documentation of this
and it's going to build out and be built
on future versions
oh you you're on yours so no no
all right so what do we do now so
i want to talk about something else on
seaside
thomas
sorry this i still want to talk about it
but that's fine that was my mistake this
time so
you can put
it's not only me
can we please lock this
okay
we also have something upcoming and if
possible we'll backport it into the cu
that's coming out so one thing
that's needed to uh again work real life
with the xml port is you need namespaces
and then for those of you who've worked
with the
enables collections and from.net it's
really really cumbersome to uh do
something comparable to for each
so actually we put that into the
language and there's a phrase and a
break
but the
thing that is a big
in there
prevent us from back porting it because
it's a braking change
but we'll see if we can work around that
because that's really useful
you also have runtime access to metadata
lookup
you url generation and there'll be a
operate tool for manipulating percentage
report layout
then
along with changes that will have sql
timestamp support for
on records so you can actually see when
if you do synchronization or something
of that kind
where did i get to the last time and
also
you can do a lot of
really nice things with this that you
couldn't do before
all right thomas thank you
now i want to talk about something else
in seaside um
our clients you probably noticed that in
2015 we released a
tablet client which is uh
you know whenever i see that in action i
get thrilled whenever i see the web
client in action i get thrilled these
two things can combine you know show how
we modernize our our clients how we
uh you know utilize the the architecture
behind that and how it was built many
years ago we prepared for this and
finally we are getting here and it's
just so so big a thing you know to see
all this and what i want to show you
today i want to you know go a little bit
behind the the scenes and see show you
some of the things that that goes on
there i'm not going to demo the tablet
client you've probably seen that you
know uh a thousand times
so
let's just step into this and then the
question here is you know how do we
build these clients because we are asked
constantly you know isn't that a big
maintenance task to have these all these
clients you know and maintain and so
forth and and
the real reason is we basically cheated
because we did not build
so many different client view we only
built basically one
and they share a lot of things and even
though as you can see in the bottom of
the screen here they look very
differently what goes on inside the
server what goes on on the logical
client layer and what goes on in the
javascript and so forth is more or less
the same that's very very few uh
differences here
and you know
the three tablet clients and i call it
the three tablet clients because it
appears to be three separate clients are
basically only one we use a framework an
open source framework called cordova and
these guys have built a native app which
runs on ios runs on windows runs on
windows you know on android and inside
that they host a web controller inside
the web control there's some apis and
eventually end up being html5 and
javascript so what we build is only
only because it's quite difficult
actually
html5 javascript client that then can
run inside these shims which are three
different shims but they are built by by
the cordova framework so we end up
having basically a a single client
running across
three platforms which is pretty cool and
then the the inner working of that is
then mixed in with the web client so we
only again only because it is really
difficult you know have to do one
essentially when when we are at the at
the bottom of this
so let's let's go see this so the first
one i'm going to open up is
the the windows
version of the the nav client
so this one again this is the shim we
are seeing here the
cordova app and they're hosting a web
controller inside that web control
you'll see our html5 and javascript app
running
so far we're seeing a logo but we should
see it running at some point
there we go so this is the the tablet
client is running on my my windows pc
here but it's basically the same thing
that we're seeing
i love the way that when you go into two
screens just take the
stage or quote whatever when you
navigate here the animations between the
screens and so forth the use that you
can use here also of course support
touch which is one of the the biggest
thing for the
tablet and so forth everything you see
here is basically the same thing as our
web client it's just you know presented
differently using the css and cascaded
style sheets and so forth okay so having
seen that one let's close out this one
and let's do the
the web client
and if we just watch it the
oh if we just watched the web client
here
so what we see here is something that
looks again looks very differently but
the controls are the same the metadata
is the same the application running
behind it is the same and so forth we
have a ribbon up here
which is navigation model is different
and so forth but behind the scenes is
the same thing and one of the cool thing
here is just to show you this this is a
browser but the shimmed app we saw
before is also a browser inside the gym
you can actually go change here the url
and just add actually i want the tablet
dot aspx and if i do that
inside my browser i now get the tablet
app just to show that this is actually a
html5
browser app that we are watching here so
this is not i'm not even using the shim
now i'm just navigating directly into
the
window that that can host the tablet app
all right
let's look a little bit about what's
what goes on inside
the client here
so the tablet client actually are
different from the web client in in
certain areas and the the biggest one
here is the navigation model between
uh the pages we we changed that in the
2015 release when we did the the tablet
app so we stay within the same page we
would love to do that with the
web client as well and there are several
good reasons to do that and that is that
all the contacts you load up into the
page when you kind of go from the the
role sender to the sales orders and so
forth all the javascript standard
libraries all the things we have in play
here when you change the url after page
and navigate to a different page all
context is lost completely so you have
to reload everything from the server and
that takes time and so forth so we want
to get away from that and therefore we
will in the next release probably change
the web client to navigate and use the
same single page um application so we
are faking it by changing the entire
contents on the page but staying on the
same earl here it also allows us to do
nice animations and and and other things
now another thing
that we did was we
greatly reduced the html structure
when doing the tablet client uh has been
an enormous effort done by our client
team in in making this uh reduced and
the reason for that is of course that
then with the amount of data needs to be
loaded from the server into the client
is less performance goes up and all the
goodness about having things being
simplified and what i want to show you
here is just
the number of levels and complexity of
showing this
tile here this is how it was before and
if you see at the bottom of this long
list there you actually have the number
of of sales orders text
and you have all these layers in between
and and that has been optimized to to
less than half there are very good
reasons for these being structured that
they are it's not like we could remove
all of them but getting to less than
half is a fabulous thing and we can see
in our performance measurements we can
see in the ui responsiveness that the
tablet client is is way more responsive
than the previous client and we'll keep
working on on getting there
another thing that we've done is we
organize the cascading style sheets
which is you know and very important
feature of doing these clients this is
where all the the magic happens which is
that is what differs the the tablet
client from the web client essentially
this cascading styles you that define
how things are looking so basically data
and and controls and all that kind of
are the same but how they are looking is
is different here
and we started out with a with a
strategy aligning our css to to
sharepoint which forces into
working with these in a manner that kind
of didn't suit nab that well so what
we're doing now is we're moving away
from that and then going into uh our
that's called our own way of doing it
which which is more modelized and and
actually we're saving a lot of
repetitions and and so forth it's it's
again to improve the the performance and
so forth
that's a little bit about what happens
in the in the client we have lots of
things to cover here uh michael is now
going to talk about some document
reporting and uh i'll be back in a
second
okay and i turned off the used timing
that you put in my presentation oh did i
screw up your presentation again
oh wait now we're talking about
reporting so i thought cloud stonestuff
just woke up
yes
okay so this is about document report on
to stay in the movie terminology here
the the the good the bad and the ugly
and it's up to you to
figure out which is which
so if if you just install a 2015 plano
dealer
and start look
for
world reporting
you have to look uh very long to to find
it
and you actually have to go into uh to
seaside and and find these four reports
say what the hell is this just it so all
this marketing fluff about world
reporting and it's not even there and
these four silly reports
are the only things that's actually in
there
but basically there's a bit more
so underneath there's the all the
railroad tracks to to create the uh the
world reporting uh
and compared to the old days where we
basically sandbox everything into
seaside and you could not change it
everything is opened uh because it's a
application just like
like gl and nav and you can modify the
the experience also what it does
pretty extensive
but what it does is to
the big thing is that end user can now
do uh customization of reports
with the of course code with the rdl but
it was a bit more difficult
also we provided some new document
reports and you would say oh there's
only four but what we also did behind
the scenes is to
to clean up the reports and
in the old days we had 20 versions of
the rdc reports if you look at the world
reports and also the new artillery
equivalents there's only three different
versions
and that's the u.s version that's
because of sales tax and there's a
spanish version
because they have two types of two types
of tax that they need and then the rest
so if you work across multiple countries
it's much easier for you to go and
modify them
we also had a scheduling and did a lot
of cleanup data sets not only in these
four guys but also
in other places and a lot of other new
functionality
you all know this
especially listening to klaus who's now
with us again
so with rdc reports of course the the
biggest thing is that it's it's very
cost to do this compared to the old
reports uh of course if you're close you
can do it really fast but most people
find it a bit more clunky
also it's a
it's a precision layout and it's very
difficult to do font changes because you
you basically have to go and modify
every field in there
and also it's it can be real really
complex to
to imagine what comes out of reports if
you have something really complex
um
also you need to uh
to be skilled to use this and it's not
exactly busy week and it's really not
suited for end user customization
but also there's some limitation of with
reporting so you're not getting the
the magic silver bullet here but uh a
combination
so basically what word is is that it's a
notepad with some extra formatting and
then there's
basically three controls that you can
use
so there's a text
text control and a picture control and
that's a repeater that's all you have
there's no grouping or totals no
conditionals no
no nothing to
control visibility
and number forwarding normal forwarding
is because it's only text fields we are
doing that in
in the server
so you cannot control that in word
but that said we really decided it
should be simple so uh so
delivery we didn't want to get parasite
between world and rdlc so idle c is for
when you want to create something
complex whereas the if you want to
create a simple
document layout you you probably would
want to use
to use word
and also
to make up for the missing grouping and
total capabilities in uh
in words you can do that in data set
instead and i can't i'm going to use you
show you how to do this so
and also
you would expect microsoft to basically
be able to
[Music]
to convert a word document to pdf but we
have no such technology currently in
microsoft so somebody is apparently
working on it
to ship in five years from now so we had
to go out and buy a component
uh but you know word is very complex and
a lot of things can happen in the
rendering of of world and between
versions they ran the difference
and pdf is the same so this is sort of
translating swahili to uh
to french
in all dialogues at the same time
so something will not simply look the
same if you uh try to enter it but
that's it it's it's pretty damn close
what you get out of it
what our llc are we going to discontinue
this of course not at all because it's
still a good foundation for report
design and still our strategy we have
improved a lot of the rdz reports in
and it can do a lot of things that's
what it's not good for
and we also ship the versions of the
docker reports and rdlc to
showcase what you can do
if you have the right data set
underneath
also multisensor gives a new challenge
for this because
if you have a lot of tins they they
might want to have different layouts so
we also enable this
for rdlc reports as well as word reports
[Music]
and
so again this is optional to use word or
rdlc but if you have a lot of small
tenants
small customers running nav as a tenant
you might want to go for the word
options to uh
to make sure that they can do
customization of themselves otherwise it
would be too expensive for them to
to pay pay for so
also i said the the sort of the plumbing
for our railroad tracks for world
reporting is is open for you to go and
modify
so one example is that
when you want to run reports it calls a
function called has custom laid out in
coding one
and if if you get word out of that you
basically when you
want to print out the document calls the
merge document
and there you have to cover everything
you have to have
to merge the
xml data you get out
from data set with the word layout and
and print it it has to be done all of it
but the benefit of course is that you
can go in and replace this and you don't
even have to use word you can render to
whatever you want or call a web service
or
go down to the basement and find your
work layout down there do whatever you
want to do in there it's all up to you
same thing with the custom layout if
it's idle c uh so basically this is
loaded before the report is run and
there's
nothing you can do to control that
afterwards but uh but still you can
again get the rdlc for from somewhere
else and not
just necessary in the nav database
adjust a little bit of drill down into
what happens with the word report design
runtime
so basically from the data set designer
you get an xml description
and with that you can go in and create a
new word document
with nav fields or edit an existing one
and then at runtime it basically uses
this using the xml merger to create the
document so it's it's pretty simple
and once you get ahead of it it's uh
it's very easy to create these documents
also compared to llc
okay so
let's go in here
so
now i'm going to show you a known crash
so you just have to
okay
is
okay so uh
our dpm marco he says and when
when you are a male and and you owe 50
you start making these sounds when you
sit down so i thought just was part of
being past 50 is that quick
i was thinking about how it was my fault
that you and mike screwed up
i'll i'll think more about it
okay please do thomas so
okay um
so let's look into
report selection
um
so by default we haven't set up the the
system to use the new world reports and
the reason for that is that we want to
provide seamless upgrades
to from
any of the newer versions into 2015 and
also moving forward so if if we just
landed the new reports on top of the
cosmos cosmos rdlc reports they would
probably not be that happy
so we we decided to keep it
it's separate
um so just go to one of these
can i get a spill take a next time
thomas
yeah
so in here you can see i have the old
report
206 and the new report is called 1306.
and that's basically all i have to do to
run the new report
but let's go a bit deeper so
into the
report layout selection which is brand
new
so i have to
filter up here to get this one
to get the invoice down here and i can
go in and see my custom layout so
so there's of course nothing here
because it's brand new
so i'll select a new one
and here i can select if i want to have
a weight layer word layout to modify or
the rdlc so
so i'll select this one
and now i can go and edit the
layout
okay so
i want to
just get rid of this guy
and let's go and
find something useful out there so huh
don't have to take days
oh
how can it oh it says that
there's some copyright thing here so
so luke are you going to
call for your lawyer or am i going to
do this oh i'll do it anyway so
let's get this logo in here
also i want
so i'm probably from bavaria or
something so i want a nicer fondant here
so
also with uh
if you go to the develop tab
of or if you haven't installed that yet
you you go to the options down here
and customize ribbons and then you can
go in and enable it here but once you
have it you can go into the developer
and look at the xml mapping pane
and you go down and choose the microsoft
dynamics in here
and under here you can see all the
fields you can use and since again the
there's no
total concept in words
we basically created all that in the
data set so if you go down
here you have the
total lines and the totals and you can
use that as your waste in the report so
so this is a point where i will try to
unhook the network because now it will
probably crash
we'll move on to thomas
it worked
[Laughter]
sometimes michael i find you a bit
scared
okay
i'm amazed so
[Music]
oh great so
nice looking
so now we know the workaround is that
you just
unhook the network and then
continue
we'll look into this when we get back
home
right tom
thanks
okay so once we are we're done here we
can go back and now i tested this and i
can go and say i want to have the
customer layout
i can choose the one i just created and
now you're ready to go and your users
will be able to use this
but again it's uh it's up to you to
extend this as much as you like and use
in all different flavors that's
suitable for for your use and
so just go ahead
okay
back to you thomas okay thank you
i'm scared about this guy sometimes
really you know it worked huh amazing
amazing you know
all right well
it wasn't even your code no no no
no the other thing you know what michael
was saying before with the the the thing
that marcus said that that he said it to
me at lunch and what he said was the
following do you know
when you're getting old and i kind of
know because i don't feel i'm getting
old at all
that is kind of when you sit down and
you go
and then i start noticing i do that all
the time it's freaking annoying right
and and try to figure that out yourself
then you know when you're getting old
because you probably are doing it we had
dinner with jackpot yesterday and he was
ah
[Laughter]
there you go i think i don't know
whether you're getting even older if you
do it when you get up but that's that's
another story
anyway uh
i'm gonna talk a little bit now about
you know it's called a rapid start
upgrade here but what really i think is
the most
interesting thing about the move that we
are doing within the the product and in
in microsoft general moving to the cloud
moving to volume is all about automation
how do we
automate things so whenever you have
something that needs to be done a
thousand times in the cloud either
because you have multiple tenants or you
have multiple repeatable installations
of the same thing or whatever how do you
automate it earlier times you know
demanded you to go do it one at a time
and and we really need to get away from
that and and start automating way more
and this is what what this is going to
be about
so first of all
you know why do we do the rapid start
upgrade this is going to be about
ribostat upgrade code i'm going to cover
the data in a second
and first of all because we are going to
change the release cadence we already
did that you probably noticed that we
are releasing every a year a new major
release but what will happen over time
as we start you know moving into the
cloud you'll see things like you know
office 365 being continuously updated
and so forth and i'm pretty sure that
with nav we'll get there at some point
as well where you don't have these major
releases but you'll have you know
incremental upgrades we're doing that
with the cumulative updates and so forth
and doing that you need to be able to
automate the entire upgrade process
otherwise it would be too expensive to
to uptake these
and that's this what is what it's all
about it's about being able to uptake
the updates without much hassle
now unfortunately there there's
something which is which is blocking
this for for us first of all we do not
have many automation tools at at all
um
and when we are using source code
modifications which really is a super
benefit quickly you get to the goal on
the other hand you pay the price when
you get to the upgrade we all felt that
pain
and and so forth so we also need to to
to work on that but merges when you're
doing source code modification is just a
pain and and and we are working on that
and i know other partners and peer and
his merch tools are also working on the
same thing and and it it is possible to
do something about it uh and and we are
definitely gonna join that that game
so
there's another reason
this is the most important one right we
feel the pain ourselves
because even though
might think that it's easy for microsoft
we do not have these operating thing and
maybe you see the picture as as this we
have a release this is just a nav 2013
r2 we have release we rtm it we get some
hotfix requests we find bugs ourselves
we do some servicing we end up doing a
cumulative update we release that and we
do the next one and so forth it's very
easy for us because we do not have any
upgrades whatsoever do we
and the picture is yes we do because
inside microsoft we have the trouble of
having a w1 version and then we have all
the country versions where we do the
localization and all the controversies
is not that different from any you know
vertical solution or any horizontal
solution being added on top of the of
the product itself so whenever we do
something we find an error in the polish
version now we need to fix it there or
we need to back put it into w1 we need
to move it do we also need to backport
into earlier versions of the product and
so forth same thing with regulatory
features that i implemented in a given
country release where we put it w1 in
the country release move back and forth
and so forth we have all these troubles
ourselves
and the picture of course get even worse
if we add in you guys because now we
just have the you know more dimensions
on on on this
this full picture here and it's not that
easy to take all these cumulative
updates so what we need to do is we need
to focus on trying to solve what i call
the the square problem here if we can
move within one square and and fix
having two dimensions microsoft doing a
vertical uh our horizontal chains
partners do a
vertical change and then get to to the
to the corner piece automatically then
we can just repeat that pattern over and
over again and this is what we are we're
trying to address here
so let's let's look at an example here
assuming we have a table i'm doing it
very simple because then i can
understand it that's the main reason
here
we have a table here 888 and it contains
a phone number and and two or name
fields and let's assume that we
microsoft decide in in some cumulative
update or the next release to remove the
first and last name field and merge them
into a name field that's a very simple
change but it's a simple example here
at the same time however a partner
solution decided to add an email field
to to the same table
and if you try to do a three-way merge
on this you you'll end up with a
conflict because the position of the
email field is unknown and you see
changes in the textual format of of the
files here being the same place and so
forth
there are tools addressing this but the
tools need to address knowing the model
knowing to know about fields and then
and so forth not just the text file of
of the exported application object
so
what do you do
we need to operate with with deltas
instead of looking at text file and
comparing text files to text file what
we need to do is we need to
figure out what is the difference really
here and what we do then is we look at
either direction it doesn't matter
whether you do the microsoft change or
the partner change you should hopefully
end up with the same thing
but in this example we kind of analyze
the difference between the
rtm version and then the partner version
and that delta we extract that out into
an object by itself and then we move
that delta to the other side and apply
that to the new version and the delta
here should of course read we we added
the email field and eventually we are
then able to calculate the resulting
version here which is whatever was there
plus added email field and we will end
up with with this at least in theory
this is doable and this is what we would
like to to do and actually i spoke about
this in the in the lab section uh last
year we were working with some
techniques and trying to see if we get
to this and now actually we have uh this
in in the product
now
i'm going to demo a little bit of this
and we do have sessions on this as well
but before i do so we need to have the
naming straight because we have so many
you know text files and and versions in
place here so the first one we
we call the original and the names i'm
using here is also the names being used
by the commandlets that that allows us
to to do all this so there's the
original version that's that's kind of
easy and then there's the modified
version
and modified version basically means the
the partner version there's been some
modification to the original version
and if you think about the the delta
that's easy that's the difference
between
the two versions and then you have what
we call the target version that is the
target to which the delta should be
applied and eventually we will end up
with the
result version here so having these
names in our mind when we're talking
about these things is as important so
let us see a little bit about this so
what i did
to
make it a little bit easy here
was i made a bitmap of these
pictures here so there it is so i'll
just keep this open and then i'll open
the commandlet prompt here
which is the
development shell
so in there we have all the the
commandlets being able to do these
things a good thing is always to use the
help function go help and then nav that
will
list all the commands that have
something nav
in it which basically means the the nav
command here and you can see there's a
compile objects import objects export
objects compare objects in here you'll
find all the commandlets that you need
to do this operation of
in an automated fashion export stuff
import stuff compare stuff merge stuff
differentiate stuff and and and so forth
now
if you look at what we got here
very simple um i have in the rtm version
the original version i have my tap 888
dot text so
i have a blank file wait a second
wrong place so here you'll see it with
the with the phone number uh first name
and last name that's kind of the
original version in the unchanged format
and let's just look at the the the added
one the modified version um so if i go
modify version and tab in here lies the
modified version where you can see we
have phone number first name last name
and and this time we have an email what
i can do now is i can run the command
list to do a compare between these two
so i go compare
nav application object and there are
some defaults here where i can put in
the first one is the original the next
one is and so forth but i can also put
in the the parameters which i prefer to
do so everybody including myself know
what i'm what i'm doing here so the
original path of this one was
um
backlash original backlash tab 888.text
the modified path
was backslash
modified
and then where do i want to put the the
delta so i have a delta path i want to
put that in delta
and then i put a fourth parameter
meaning if anything is in the delta just
overwrite it down look here so this is a
very simple way of doing a compare
operation as you see here it analyzed
the situation and figured out there's
one changed object which is not that
surprising and i can now type the
delta and see what's what's in here it
produces a delta file and what you'll
see is a file that that looks very much
like the the
normal
nav
file
just scroll so you can see it here
you see the the format is the same thing
but we are talking now about
a modification
to the file and here we're talking about
an insertion which which sits just
around here
and then there's insert after and
there's a changed element and and so
forth so the textual file is still
readable but here we have in essence the
delta and now i can go on now and apply
the delta to the to the target version
and so forth we will demonstrate that in
the session uh we'll also have one that
does all of it take the original
computer apply and write the results so
you'll end up with with one version
during the entire thing
i'm just trying to get to some of the
the building pieces uh
here
now
of course
during the code merge there's also in
the session by the way all handling of
conflicts and so forth so so you will
definitely see how to how to do that
but but doing the code merge and the
metadata changes is only half the
equation we also need to take care of
automating
the data upgrade
and in there you you probably all
experience having for instance multiple
companies inside
you know a database and you have to
apply the
the upgrade have to run the upgrade tool
you have to do this one company at a
time it's it's hard without the
automation and again everything now has
been automated and and put into um to
commandlets
so
fast and automation is of course a must
when we when we uh move to the cloud
that's again
a given given the situation that that we
are in
so
what we need to do is we need to make
sure that we are
independent
on on seaside seaside can no longer be
the the master of doing the upgrade
because if you're operating something on
the cloud if you have a repeatable
solution if you have something which you
need to multiply a hundred times it'll
be extremely tedious to do it so there
needs to be a way to do that using
uh a command list needs to be
you know you need to be no need to be
there unmanned needs to be scriptable
and and and so forth so let us uh
look uh a little bit on
on the premises here basically nothing
changed i mean the the way you do data
upgrade
is is the same thing as always you
figure out what the prerequisites here
you need to save data that's been
overwritten if you if you do changes to
two field structures and so forth so you
have a
you know
what are the prerequisites you have a
runway preserved data you have you know
the the of what we used to call buffer
tables and then you copy from the buffer
tables into the real tables and and all
these things no change as such the only
change here or the biggest changes we
automated the the entire thing
and let's use the example from before
even though it's a very simple example i
have the table 888
and what i want to do here is i want to
you know merge first name last name into
a name field and now we should imagine
this is a change i need to apply to my
500 customer installations each having
multiple companies in the databases or
or whatever so
what we need to do first is we need to
create
a new
code unit
in the code you need to have two
methods in here and we need to create a
copy table of the data where we preserve
the first and last name during the
upgrade to to eventually merge it into
the name field what it's going to look
like is
something like this
and the automation here kicks in because
you can see we attributed these methods
first of all we put the entire thing
into an upgrade code unit so what
happens now is when we start up the
server the server will go look for all
the code units that are attributed with
the upgrade like we have test code unit
today we introduced a new type called an
upgrade code unit
again inside there we attributed the
method here called get table sync setup
with uh i'm
a table sync setup method meaning
whenever somebody tries to do something
to a table that has destructive uh
consequences like deleting the first
list and last name fields it will go
search for a method somewhere describing
how should i handle this thing and what
we basically do here is we encode tell
it whenever that happens please do a
copy of the entire table 888
deliberately i use the numbers here to
table 889
so that's a copy operation so that means
when i deploy this code unit in a fob
file to a customer site the system when
it detects the difference in metadata
will automatically go look for this
method and in here lies the recipe for
how to handle this situation
and you need to handle it by you know do
a copy into 889
now at the same time then we apply a new
method here which is attributed upgrade
that then says when you do the upgrade
here's the code to run and as you can
see in the code here we're basically
enumerating the old
uh table what used to be known as the
buffer table the 889 table here looking
looping through all the records and for
each record we look up the 888 record
and then populate the name field with
the first name plus space plus last name
the logic here could probably be
improved if there's a blank first name
you'll end up with something starting
with space but whatever that's not the
case here
so the the interesting thing here is the
aspect of automation
having this code unit in place allows
you to go to the customer side with the
fob file and just shove it in there and
run a data upgrade the platform will
then automatically load up this code
unit in here lies the answer for oh i'm
doing destructive changes what should
happen you should do a copy into table
889 okay i'll do that and then when you
run the the data upgrade the same code
unit will have the the code to be able
to actually move things in there and
then the platform will automatically
move to the next company and do the
entire thing
um everything here will be run in in
parallel so we introduce parallelism so
we can update multiple companies at the
same time and the the improvement is
phenomenal in in upgrade times when we
run the and use this this framework
everything is resumable if there should
be an error and so forth we will flag
how far we went with which company with
which uh installation and so forth and
we are able to to pick up from where we
where we went
we're a little bit short of time so i'm
not going to show this to you but
basically you have the the building
blocks here it's all about attributing a
code unit with being an upgrade code
unit flagging this method being the
table sync setup method and the upgrade
method and from there on it should be
more or less self-explanatory
over to michael okay thanks
is this cool or not
it is cool
okay on simplification
so
back from the old days of nav one of the
models of the product was the beauty of
simplicity
but what we found out
three years ago was that it wasn't as
simple as it used to be because just as
three grows the uh so there's a ribbon
of energy for every release each team
had the fingerprint on the ribbon and
put on new stuff
and it just uh
exploded and also putting
new fast tabs and new fields on for
every new release and everything had to
be visible
so we've been through a
number of applications that went through
2013 r2 and now 2015 and that's an
ongoing effort
but for this release we made a number of
changes that's uh
also been a wish for a lot of people for
many years so one of them is mandatory
fields which is not really mandatory but
i'll get it back to that
it's the old autofill of the number
field
to have totals and documents that and
you don't have to go into
other pages you see that
getting rid of all the stuff that you
don't need and also the new enhanced
cues that we put in
and overall the the new mini app or
simplified ux that we're providing
also for the tablets
but instead of
going through a lot of slides let's go
into the
product and see
this for real
good thomas
so let's go into the uh
management console for once uh and here
in here we put in the ui elements
removal
and you can basically there's three
choices so you can do nothing you can
adhere to the what you're allowed to do
based on license file or you can also
you use a look at the user permission
and just a warning in rtm there's
there's a performance block that's if
you use the
both the license file and the permission
then things are getting really slow but
in the co one that's released this is
fixed and it runs optimal
but this enables you to control how much
the user can see so
if if you're not running jobs or cm or
whatever you will not see it in the
ribbon or
having the fields in there
so that's one thing the other thing we
introduced is this small business
role center
and basically it came out that of that
we also had a product in denmark called
c5 and we wanted to
update it to run on the nav code base
and c5 is for really small customers
single users and these are craftsmen
often who
sit in the van doing it so we create
this role center for
the rtc in the web but also a special
one for the tablet so
because if you're on minivan and you
have your ipad in there you want to use
that to run your business
and actually if you visit pier monson
who is here as well he he actually runs
his business on his phone
uh
using the
the small business role center
but as you can see here compared to the
old days the the ribbon has really been
cleaned up up here
we dragged all the
things necessary for a small business
owner to uh
to run his business in here so we have
the k
key performance indicators and we have
the trial banners on here
am i bankrupt or not that's sort of the
question you
you get answered in here
also uh
instead of having these queues where
it's sort of is
168 000 is that good or bad
i don't know
but let's
go and look at the setup to
figure out so so basically for for the
cues you get the possibility to go in
and
define a low range or threshold
one and two and
what's beneath here you have different
sentiments
you can have none and
you can say this is uh good or this is
bad or i don't know or
subordinate so that's just gray or i
don't give a
whatever you like so
but but this basically gives you just a
hint of is this good or bad or
do i have to care at all
and do i have to push this bottom to get
down here
um
let's get a bit deeper in here so
if i go into the sales invoice
you can see there's the the star in here
and the star indicates this is a
mandatory field so uh so we also
considered that you always had to fill
in these fields
but what if you hide these or you don't
have permissions to to see this then
you're sort of stuck
so we started to have a middle ground
where you just get the things that you
need to fill this out but we'll let you
go if
you don't do it
so let's get and go and sell something
to sportsmail
and you can also see that the uh the
the number was not filled up from the
start and now it's up there so
so the
if you have a number series and only one
and you cannot do manual numbers in
there
we basically decide for you that you
don't have to see the uh
the invoice number in here
so we remove it because it's sort of
redundant
to to see that uh
also if we expand the lines you can see
we put the tools in here because of
course you want to see the tools
and this this was also back from the
beauty of simplicity days that this was
actually in in the beginning from
in one
other reason
it got lost over time but now we put it
back
let's go in
let's buy some
set some front wheels
and the two
yes and now we can see the sums are
updated down here
so again simple simple symbol and we are
continuing the effort to
to remove more and then newer versions
and really emphasize what's important
for the end user to to work on
so very short about certification now
back to something really
complex and nasty thomas
i'm not complex and nasty oh but the
topic is
all right the the next thing we are we
are going to talk a bit about is is
office 365 integration and
again this is going to be more about
how you do stuff and and
some of the building blocks available to
to achieve what what you want to do with
the with this integration
at this time there should be no doubt
that microsoft is heavily you know
betting on office 365 it's our fastest
growing
business within microsoft and definitely
as nav being the division we are you
know we want to be on that wagon as well
so we are going to continue our
investment into
uh the cloud into office 365 and and so
forth
now
the interesting thing here is there
there are a couple of scenarios we have
right now in in nav
the first one is because this open in
excel that sits
at the far right here in the ribbon
and when you run that one
strange things happens sometimes you get
an error that's that's happened often to
me
sometimes it opens in your on-prem excel
but what happens if you have an online
web client sitting there and you want to
be able to open it in the online excel
now what how do you set that up how does
that work and what happens behind the
scenes
so basically what is this
how does it work and and you know what
is required to to make it work
so if we're talking about these
scenarios the two things i i want to
cover today the first one is you know
get the send to excel
to work from a online web client to the
online version of excel what is required
to to make that work and the list is
here this is actually quite simple the
first thing you need to do is you need
to have a office 365 subscription to
make this work
the reason for that is that basically
it's it's very simple whenever you do
this export to excel what we do behind
the scene is we actually save the
whatever list you're having to a file
and we need a place to save that file
and right now the only thing that we
support is saving it on a skydrive
pro or skydrive for business or
essentially a sharepoint site
and whenever we save it there
then we can open up the online excel and
have online excel pick it up from from
that location that is essentially what
what what goes on and this is what is
needed to to make that happen i'll demo
that in a second
the other one that's that's really
promising is the entire story about
single sign-on to your to your office
account so you link your your id on in
the cloud to your nav user id and have
them being the same thing there's a
tremendous amount of advantage by doing
that
but it seems to be something that that's
complex to set up complex enough for us
to actually have done a commandlet that
does everything
and and of course of course you can use
that one but what i'm going to show you
today is actually the bits and pieces
involved in in doing it if you want to
do it manually
so again this is all about having an
azure subscription and this one is
actually for free it's interesting
because inside the azure cloud live
something called the aad the azure
active directory it's basically an at a
cloud hosted super hoover domain
controller where you get your own node
and this service of using that one as
part of the azure services is for free
so you can you can go and create an an
azure subscription you need uh as usual
on those things to to give you your
payment info but it's for free nothing
will will happen as long as you're just
using
aad
and then you need to configure the
client not to ask for for nav username
password and you need to configure the
the server
so let's go uh
look at this so the first thing was the
um the
active directory thing so i've set up
something here i have a remote into a
machine this isn't
a machine in the cloud i created a nav
td
2014 domain
which which is you know just a free
office 365 uh subscription
and and at this point i'm i'm ready to
to go try these things so the first
thing i'm going to do i'm going to use
the web client
opening up my
first i'm going to sign in just to show
you this i'm going to sign into office
365 using my my credentials here
so my credentials on my
trial office 365 account was thomas at
nab
td 2014
on
mike
it's hard to spell to microsoft
come
and
like this okay so this is
simple enough now i signed in here is my
office 365 as you can see it's a it's a
trial version and that gives me the
sharepoint site so now i have my
location to be able to set up where the
web client the online hosted web client
should be able to save
my excel when i do with the the x
products yourself so i'm just showing
you
the the sign-in process here closing the
browser make sure we forget everything
open again i'll do the
this time the nav
and as you'll see the i'll be asked for
my nav user password here um that's a
standard uh installation here that i
haven't created anything special except
this user account
so this entire thing is running on on
an azure machine in the cloud if i go to
to any list take the customer list
[Music]
and then of course i have the the open
in excel
now if
click this one i get this error which is
you know a little bit strange it it has
to do with my browser setting does not
allow me to to download files or
something but you might expect other
areas like you do not have excel
installed locally so how should i open
this xls file or or whatever what i
really wanted to do was to have the
online version of
excel open up the file
and to do that i need a few things i
need to go into the online
document storage
configuration
and again this search feature is also
present in the web client you've
probably all grown used to it in the rtc
client today it's it's super it's also
in the web client and then you can
quickly navigate to two pages
anyway
i go in here and i need to create a
service
basically a way or
what i'm doing here is basically telling
the system where should you store stuff
when you try to to export in the cloud i
can give it an id i can give it a
description it really doesn't matter
what's important is is out here where's
the location this should be stored and
that just sit on my domain
http
and then i need to type in my my
domain name and that was the nav
td
sharepoint
dot com
one could imagine in the future that we
are going to support things like you
know uh our one drive and and so forth
but currently we only support the
sharepoint for for this
then i need to designate a folder and
that's essentially just you do a folder
here and whatever is getting transferred
using this send to excel mechanism ends
up in this folder not to destroy your
your other things on your sharepoint
site so i can call it whatever it will
be order created
if it's not there and i need to
tell it within which document repository
on the sharepoint sites this sits you
know when you open a sharepoint site you
also have these documents and you have
team stuff and so forth the most easy
thing is just to do the documents
then you're in the document folder
and then what i need to fill in here is
the user credentials that have access to
the sharepoint site that the the web
client can actually use to to store the
the document and that's my my account
from the sign in before so i'm going to
do the thomas at nav td
2014.
on
microsoft.com
and then i need to set the password
for this account and i do that in here
and i put my password here
and it asked me whether i want to change
my password not really but well strange
anyway and then there's a test
connection or test button so i can click
this one just to make sure that
everything works
and if i'm lucky it'll tell me it works
the connection validate correctly so
everything works here and then i can
close it up
and then i have my customer list and
when i press the open in excel now it
will end up saving the the the order
generated file on a sharepoint site it
will open up the online excel
and and get it in here now what you see
here is this is one of the reasons for
this single sign-on being interesting
right now i'm asked when i jump to the
online excel to type in my credentials
of course i could put the they keep me
signed in here but i'm not doing that to
to demonstrate to you how the single
sign-on is nice when you have it i don't
have it right now anyway i sign in here
thomas
2014.
come um come on this is too shoot i'm
dot com
right
there we go
and i end up in the online excel
hopefully with the list so it is not
that hard to set up you just need to
know exactly what what to do
well that was part one um the other part
is actually you know starting to to look
at the
the single sign-on if i go back to the
slide again for for a second and and
just you know to to show you what what
was needed here
again and as a subscription
having the right side now i do have that
one created already and then i need to
go into the manage portal of azure and
telling azure about nav because this
active directory that sits in the azure
cloud needs to know about nav being an
application and i'll get back to to to
that in a second
and then i need to create a a user on
the nav side that accepts the
credentials coming from office 365 and
eventually i need to change the
way the client and the server
authenticate so we're not using the the
nav username password anymore these are
the five things i need to do and again
it's all about knowing this
and of course this has been written down
numerous times but i'm going to show you
how how easy this essentially is to do
so the first thing i'm going to do i'm
going to open up a browser
and i go into the
azure management portal
again i'm asked to to sign in here i'm
getting a little bit tired of typing all
this
thomas
is that also a part of getting old
thomas yes
right
so this brings me to my ashes
subscription and this is a again a free
trial account i i've set up here
on azure i have the capabilities to
create virtual machines and all that
kind but that cost money what i'm
interested in is actually the free thing
here and that is the usage of the active
directory it sits at the bottom here
so i can scroll all the way down here
uh and you'll see there's an active
directory that's the only thing this
this account has all the other things
are zero the zero vm serial connections
here whatever but there's an active
directory which is needed
so what i do in here
i go into the active directory and then
i can look about the
i can
configure here i can see users groups
applications and there's applications
i'm interested in here the applications
that i want
to give the permission to use this
active directory and active directory
should know about the applications i
create in here basically these
applications should participate in the
single sign-on process so i need to
create a new application i'll do that
here
what is the kind of application this one
for the gallery or is this one i'm
developing myself i'll go full manual
here so i'll do the the one i'm
developing myself okay what's the name
of it well we can use the name to have
td 2014 keep the
the naming here
okay
and then here comes what is the sign on
url
and and the reason for that i'll get
back to that in a second is that the
azure active directory needs to know how
to redirect request back and forth when
you type things into your browser you
probably already
experienced as you go into something it
needs you a live id or your office id or
whatever and you kind of go this click
click click browser goes back and forth
and kind of what is it doing and i'll
get back to that in a second but
basically what we're doing here is we
are telling it if you need to navigate
to this application
this would be the the uh all you need to
put in to navigate to the application
and the easiest place to get that is
actually just to go to the nav client um
the nav web client and just steal the
the uh they're all here because this is
the the design on uh earlier you're
gonna use we can strip some of the
the uh
detail part here uh and just go with the
with the web client that is enough
so i'll copy this one
go back to my active directory and say
this was my sign in
url
the next one i'm going to put in is an
app id
and
it is just basically an identifier being
used several places um but it needs to
be in earl format i really don't know
why but well it requires it to be so
i'll put it in here
uh http
and there will be nav
td 2014.
i just decide to to use that as my earl
it's not really an earlier navigating
too it's more like an identifier of the
the application that's it
that is what i need to set up and now i
told the active directory about nav
being an application
in the cloud i can go and look at this
if i if i so want to
there's a dashboard i can see what goes
on i can go into the configure and add
additional details
and i can just show you something in
here that might be a little bit
interesting here you'll find the sign on
earl the name the things i entered
before
but you have one thing here
which is the reply url
and this is part of the security of the
active directory meaning whenever active
directory send keys and tokens and
whatever back to somebody requesting
info for this application it will never
ever send anything to something which is
not either this specific earl or a sub
domain off of that earl so to make
things secure here instead of having it
all the way to the web client you can
basically go say i'm just going to be
happy with anything being sent to
my domain
so if i change this that means that
azure directory will will send whatever
as long as the the url kind of starts
with with the info we have here another
thing worth noting is the permissions
down here where you can decide uh which
permissions have access uh or which
which applications have access to what
so when a user comes in this user have
access to do this and this and that and
and so forth by default it's set up in a
manner where it's usable meaning that
there's a delegation so whenever you
come in that particular user can read i
really i delegate to that user to be
able to read the the the active
directory itself and there's a sign-in
permission
okay that's enough i'll save this one
and and that's it now i told the azure
active directory about nav as an
application next thing i need to do
is i need to go into the nav and create
a user here
so i'll do that
log in
create a new user
and do a new one
and call in th
error full name
thomas h
now expiry date and then leave
everything as is in here
except the authentication email this
user authenticates by using the office
365 authentication so i need to put in
the email here
again that's thomas
today 2014.com
and then i get the
activation status is inactive meaning
this user hasn't logged on yet so we
don't know uh about him yet but i'm
creating the user here and i just need
to assign some
permissions and i'll do the
super too myself here that's essentially
it at this point i created this user
i'll close it and now i'm ready to
i closed i didn't save it that was not
on purpose
um
it is safe okay um
oh there it is okay so
now i need to reconfigure this the the
server and the client to use the new
authentication method instead of using
the the nav username password and while
doing that i lock out my nav user user
which is why i need to create a new user
first otherwise i'm kind of toast i need
to to reconfigure back again i'll close
this one and what i did is i prepared
two shortcuts here we'll navigate to the
location of the server and client
configuration files see on timing i need
to hurry up a little bit here so i'll do
it a little bit fast but what i need to
do is i need to go into the
configuration file here the normal one
you see has a lot of text into it i
removed that and isolated what we're
going to look at here these two keys are
everything that we need to change
today
they identify that you're you're using
nav username passwords and
there's another key that's blank because
it's not relevant for an app username
password what i need to put in instead
is i want to use the access control
service and then i need to put the
location of the federation service
basically meaning where do you go for
tickets ids and privileges and and so
forth and this is the entire path that i
get which points up to
my azure
active directory you'll see in the in
the help file you actually have
everything sitting here log in windows
net and then add your own tenant id here
and that's the only thing i did i put in
nav td 2014 microsoft.com and that's it
so i'll just replace these two lines
with the other lines
i'll zap these two and put them into the
comment
and i'll take the other two take out of
the comment and and put here and that's
it i'll save this one and i'll do the
same thing for the
client configuration
and the web config file and essentially
we have the same thing here down here we
have again two keys that needs to be
changed
again it's credential type same thing as
before we need to have you know tell it
to use the azure active directory and
then where do you go
the active directory ui where do you go
to get the entire cyan going and so
forth
i'll do these two keys zap them put them
here take the other two keys
zap them and put them to be used and
i'll save this one
the last thing i need to do is to
restart the server
to be able to do the new of course all
this can be done through commandlets but
old habits die hard right so
i'm going to restart the server
and after having done that
i should be good to go with the single
sign-on experience using my
th account
there we go
so i'll open this one and i'll go to the
roll center as before if everything
works now we should not see the nav user
sign on dialog instead we should see an
office 365 and that's exactly what what
came up here and i go okay i use this
account
i need to type my password
and now i can use to keep me signed in
and all the things that we we used to
have and so forth and now exactly i get
absolutely nothing okay i mistyped
something along the way i'm sorry
but that's the you know live demos and
so forth
normally when you get in here everything
is then set up and you will have the the
sign-on experience working on um
nav and the office components and you
can all do these you know export import
and you'll keep using your same
credentials there when you do sign off
of nav you will also sign off off of all
the the other services because this the
sign up process is common to all the the
products here
so going back
to this
um
one last thing to talk about here is how
this how this works essentially and what
we have here is um it's all about
exchanging tokens and trusting tokens so
essentially we decide to trust the
active directory it could have been live
id it could have been other forms of of
ids and we do that by putting that into
the configuration file of the server we
trust this guy up here okay that that's
fine and then they send us a token when
you do the login of on in the in the
cloud we end up getting a token from
from that service and we can see inside
the token your your
mail address is there and so forth and
we can match that to a to a nav user at
the same time certificates make sure
that it isn't tampered with and we can
check both the
authentication and and so forth on these
uh
on these tokens
um what really goes on let me just click
through this is this is what goes on
when you try to to to do a login there's
a lot of pinging hanging back and forth
between the
the web browser and the active directory
or another identity provider and
eventually you have you know you get
your first page this is what's happening
when you see things where you kind of go
click click click and the browser keeps
reloading and
if you do this keep me signed in you
kind of skip these two steps where the
ui is presented
meaning the entire thing will go on
every time you do a navigation to one of
these pages but you'll skip these steps
showing the
ui
all right
thank you
so this looks fairly easy if you just
able to
type in your password yes
absolutely
okay
so we have two topics left so let's move
very fast to the roadmap because i want
thomas to show some of the
new stuff
and get your reaction that so
you all know nav started back in 87 with
version one of the text-based version
[Music]
and then 2000 of course we had this
franken platform where we had the
classic and the new stuff in the same
same platform uh
2009 r2 we we added
cm integration and some visualizations
but the real big things happened in 2013
where
basically most of the server was
rewritten and also we made a lot of
exchanges to the clients
to
extend it from just having a web client
to also support other clients
and that's basically the foundation that
we're building on and you'll see that we
we are now able to move much faster than
the old world where it took three years
to create something because we had to
deal with all the old nazi receivers
plus code and now we have a modern
three-tier platform
it also runs on asia
of course in in our two we created
multitenancy and also we went very much
into the cloud
and enabled that
also based on what we did before and
building on the
investment that we did
and and also we are moving into very
much the tooling side of running a
large-scale operation or navy and
not just
doing inside seaside
of course the last but not least the in
2015 you also these but also a lot of
great app features on cash management
and simplification that we put in
to enable that
but
moving forward to
to the future uh
so previously we we had a slide that's
where everything ended in i think 2015
and people said oh
they're going to discontinue the product
so uh but we are not we're going to
continue off that so we in a new slide
that now we continue so
that should solve that part of it
but just as a previous release we have a
code name that's the greek island called
kofu
nice island
and we probably are running out of time
i think we're running out of islands yes
and
but since we are very much running agile
now everything is is not planned to
every detail when we start the release
this is pretty much work in progress
so right now we have this
one-year release cadence but you should
expect to see shorter release cadence in
the future as well
because if you look at windows windows
10 is the last version there'll we know
windows 11
is just going to be windows 10 going on
and nobody cares about office 65 what
that what version that is it's just
office 665 so
so maybe something in that line would
happen to nfv as well
but right now some of the themes that
we're working for is working on this
workflow
that's been
longstanding wish to have some
foundation work in there
also on docker management and
ocr
also on the
on having a better connection to
[Music]
electronic trades and
handling the the mapping between
documents out there
that's another
wish that we had for a long time and
beyond that we're going to continue work
on the client so thomas talked about the
new chapter client and how that improved
the uh the single page concept
and also what also dropped off on the
web clients we're going to continue this
world and work and and try to get a
single code base across all the
the web webbies clients including
tablets for
for the clients to make sure that they
have a single code base in there and we
can
flourish on all the uh
all the progress across all of these
clients
especially uh you know the web client
was sort of the theme back when we drew
that this was for large users
so it's not really a replacement for the
rtc or companion for the rtc we're going
to fix that so we'll have a web client
that's as good or better than the rtc in
the next release
but don't expect us to come out with a
full-fledged workflow or document
management solution this these are
foundations and we're also looking for
partnership with corn solutions out
there
to make a good solution but this is
basically
putting in the railroad tracks and the
architecture too
to build on it for the future
very fast on the roadmap because we need
to go to the lab
yes
this is this is the the favorite part of
of of this show this is where we kind of
get to do the free form let's just
discuss what what what we are thinking
about notice the front page here
microsoft dynamics and then nobody knows
because what we have here is really what
michael and i are thinking about when
when nobody is watching right when we
have our our discussions are where where
do we want to take this product from a
technical angle what comes your
perspectives and so forth and we have
lots of things
there will be no mythbusters this year
unfortunately we do not have time we
will come up with other things like at
the equity show next year i think where
we'll have categories like
how come michael's still here and you
know
okay you know
i'll i'll do how come michael's still
here for 300. that's for sure yeah
that's a good question
absolutely
there's also we don't need no stinking
architects but that category is kind of
well anyways especially the stinking
part so
again disclaimer everything you see here
is just ideas there's no promises of
this showing up in the product next
month or even five years from now or
even at all but we are going to share
some some of the ideas here
the first thing we really would like to
do something about is as i said before
in the the merge section we would like
to introduce some kind of event-driven
customizations i would say this is
probably the one that has a highly
highest likelihood of making it in in
some time soon
[Music]
and the idea here is basically that you
are
being able to hook any method without
the method itself knows that it's being
hooked
and that's a big difference because that
means that you from a subscriber
standpoint tell the system i want to
hook onto this method and here's what i
need i need these two parameters this
local variable this global verbal and
you need to call me before the method
and i'll take it from here
that allows us the freedom from the the
guy being hooked he can actually change
the parameters add additional parameters
add additional local variables and so
forth as long as the thing i subscribe
to is still there
then this one won't break and you can
keep having this subscription hook being
there
it will be able to daisy chain them you
can call bass and have the original
functionality being executed you can
fiddle with the return value before it
returns and and so forth all these
things is something that we kind of see
as being part of an event-driven
customization and then of course if we
do something new we're going to take
care of worsening dependency tracking
and all these things to make absolutely
sure we generate something which which
lasts uh
way into to the future
again the purpose of all this is again
to make a more seamless you know upgrade
and and and that entire experience there
now the
the big difference about such a
customization would of course still be
al still be something you install on the
server you still need to compile stuff
and and so forth but there are other
scenarios where you would like to to be
able to do other kinds of customization
i'll get back to that in a second
another one
interesting is
subscriptions
one of the services that lies in in the
azure cloud is something called azure
subscriptions or the the
service bus
essentially if you think about it the
service bus is just an advanced queuing
mechanism meaning you can subscribe to
tell me whenever
there are red balls put into this queue
whatever
and then you can go to sleep and
somebody else can put the red balls into
the queue and when you wake up and the
day after you reboot your machine and so
forth you can ask for all the red balls
i was put into the queue it's a curing
mechanism uh in its essence there's a
lot of you know for niceness to this and
and details but in essence it's a
queuing mechanism now imagine a world
where you could tell nav to put red
balls on the queue whenever a sales
order was posted with a with a
you know amount greater than this or
that or whenever a customer was created
and so forth you could generate all
kinds of interesting synchronization or
corporations corporation scenarios
between the cloud even if you were
offline and this is the
the the great part about this the azure
service bus is always online so you can
count of that being there so you can
always deliver your red balls
but then the consumers can be offline
and come online and pick them up at at
any time and of course the reverse is
also interesting uh where you have a
situation where you from ale wants to
subscribe to somebody putting blue balls
in another queue whenever that happens i
want to know because then i need to
print an invoice or whatever it could be
a production system running all night
whenever something happens leave a trace
in in the
azure service bus and then have your
application pick up those traces when
you come online and and and so forth
that's one idea
i think it's really cool what do you
think
oh okay
we haven't made it yet we're just
thinking about it you know so
anyway we need to make more of these
things yes yes
now
another thing is as i
talked a little bit about before about
these having the applications being
something written in al and you need to
to recompile and so forth
um again if you're running something
multi-tenant where you have you know one
server serves hundreds or maybe even
thousands of customers and then you
wanna do something for a single tenant
you want to do some some special things
here
the problem is going to your host or
going to your own machine saying this
tenant here wants this special
customization and by the way install
these eight dlls and stuff like that you
would never risk that i mean that's
simply too dangerous if you're getting
things hosted in out in in in city as
part of a big multi-tenant system in the
cloud you probably cannot provide your
host or to to go and put in
special things for you because he's
sharing the entire thing across
multiple instances
thousands or hundreds of customers so
what we're looking at here is something
where you have the capability of
installing add-ons which is
which are non-intrusive so and that is
the the most important thing here so i
put in something here we call it an mxd
but it could be called whatever don't
take the naming here but i put in some
extra piece of metadata the system will
let it run time read the standard
application definition of a given page
but then figure out that there's an
extra thing here so it's not in truth it
doesn't destroy what was there it just
add an extra control to that page let's
say a link button to do your sign in on
office 365 or something silly so
whenever you the user of that particular
tenant or or whatever takes out his page
that button will be present but for
other users it will not
it doesn't ruin the the application it
can be removed again at any point you
can just simply remove this
add-on thing and the entire thing will
be you know
away and you're back to the original you
do not change the application on the
server there's no recombination
retesting re-certification nothing of
all that because you do not change the
application that is the most important
thing about this idea it's non-intrusive
and nothing has changed
you can of course build on that and say
what about the
the even more intrusive one which is
still in a non-intrusive fashion i want
to add a field but i really want to add
a field without ruining in the the
normal application
so this is a situation where
this particular customer wants to have a
single field added to his his customer
record we do not touch the customer
record itself we just tell the system
whenever you you read customer records
before you send them to the client to be
shown
go and then see if you have a foreign
key
to this bulk database where extra fields
are stored and then merge everything
seamlessly into the data sets and into
the ui on the client so all the clients
will work and and nobody will know that
this field has been has been added the
good thing is however if you don't like
it you can just remove that feature
again because you haven't changed the
original application everything here is
is unchanged
um
another thing you could you could see
well another thing is on the mxd you can
see here is that we
we would really like to you know have
dependency tracking have this this one
being showed as
something that is only shown for a given
role or given tenant or give it a
logical condition it really doesn't
matter since it's something you can add
and remove at any point you can also
have it come and go and on even and odd
minutes if you so choose a silly thing
but but that's something you definitely
could be able to do
non-intrusive code now it gets even more
interesting
if we cannot change the application on
the server which we can't because then
the hoster or the the other customers
would be angry if we crash something
what about what about having extra code
being being run let's say i want to do a
automated currency lookup thing why
can't that happen at the client why
can't i have a button sitting on the
client and when i press that button it
will go to an external service look up
the currency code come back and fill in
my field in my screen for that that's a
pure client thing if if such a feature
you could have other features zip code
look up or whatever there's tons of of
these scenarios and basically starting
here to think about something which we
when we think about it is this an is
this nav apps is this kind of an app
model where you download something as a
user even you install it proof it works
it enhances your experience in the ui by
being able to run javascript on the ui
and that javascript can do anything the
user can do
it it's not like you get any special
privileges and go mess with the
application no but you get an automated
fashion of doing things with the ui
on screen which is kind of interesting
there's definitely ideas here so you
could call external services or you
could call into apis on the server and
these apis are public that could be web
services that could be whatever it's not
like as i'm saying you're not ruining
with the application nobody you know is
getting special privileges
now
that's it that's some of the ideas that
we have been you know thinking about
some of the things that that might show
up in the product
we are 39 seconds from uh
being at the next break i think both
michael and i would really like to thank
especially look for giving us the
opportunity of of being here to talk
about the product that we we all love
it's fabulous to see so many people here
i don't know what nick is going to do
when we break the record next year with
even more people because it seems to be
pretty full in here
but probably he will have an idea
thank you very much for attending and
have a really good show
thank you
