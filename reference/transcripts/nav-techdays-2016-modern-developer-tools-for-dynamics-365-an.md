# NAV TechDays 2016: Modern Developer Tools for Dynamics 365 and on premise NAV

- **Source:** https://www.youtube.com/watch?v=nqrPaTMF8N0
- **Video ID:** nqrPaTMF8N0
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 83m41s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

good afternoon um I'm Michael Hammond
I'm the lead for the team that works on
extensions yes and I'm ESP
Christopherson I'm an architect on the
team who works on compilers and
developer experience and today we're
going to talk about both of those topics
um in some depth and uh look at what
we're doing going forward as well so
today we want to understand extensions a
little bit this is something that we've
talked about a lot I think most people
are starting to understand it but we
want to reinforce just a little bit why
we're doing extensions um where to use
them and how to start using them today
also we want to talk to some of the
enhancements that we've done in nav 2017
the new features we've added to make
them more robust uh we want to take a
long look at the new developer
experience um understand the ways this
can be used uh the ways to reference
code that does not come from extensions
and then we want to get everybody
excited about the opportunities that are
coming down the line the new tools the
way that these can be leveraged uh in
business cases and start talking about
how to move forward on
that so like I said the first thing we
want to dive in is talk a little bit
about okay we've done things the same
way for 20 something years and now we
have extensions how does that fit in
what's the difference when should I use
both and the first thing we'll talk
about is when we talk about
customizations that's the source code
modification that you've done in the
past you can go in you can modify the
objects you can still create your new
objects it's basically what you've been
doing and if you're when you're doing
this model again is going in and
makinging changes to the existing
objects everybody on the system has the
same thing if you're running in a
multi-tenant environment when you're
doing this upgrades depending on the
patterns you're using can be a little
more complex um and there're but you
customized this to be a lot of cases for
the specific customer you're looking at
when we start talking about extensions
we're talking about adding new objects
that modify the behavior of the existing
objects and being able to put these on
very easily being able to install them
upgrade them as part of the process
minimizing the cost and time it takes to
do an upgrade uh simplifying that the
new Concepts we've added such as events
where you no longer need your code in
the uh page or table or code unit you
can write code separate from that and
still influence the behavior of the
application um you can think of these as
modules that you can put in place you
can put multiple modules in place on the
same system they should work well
together we've tried to Define um a tool
set in patterns that support that and
again I talked about the upgrade when V2
of the base comes out your extension um
as long as we haven't changed in the
apis that you're using should be able to
move across and slide in and continue
functioning uh as they were so the next
thing I want to talk about I'm not going
to spend a lot of time on this slide
there's a lot of information here but
one of the questions we got especially
when we release now of 2016 we got a lot
of comments some very positive some were
I like what you're thinking but
Microsoft has a history of starting and
not finishing some of that's a nice toy
you got there it's fun to look at but
what what I really want to emphasize
here is yes in nav 2016 we laid the
foundation we put a lot of support in
the platform for the very very basics of
what you need to do that I talked about
that install that upgrade the very basic
functionality that you can use and know
it wasn't everything that everybody
needed but when you look at what we've
added in 2017 we've really rounded out
the feature functionality of now we have
support for all the objects at least as
new objects we've added things like net
addins ways to work with data um support
for translation and some upgrades to
some of the apis that we had to make
some of the problems that we were seeing
some of the things that were complex
much easier and I'll talk a little bit
about that more soon but then also the
Future Vision we're we're invested in
this we're continuing to invest to this
in this and hopefully by the time we're
done you'll see a road map here that we
have that we're set out and that we're
committed to what we're doing um and
some of the things here that I really
want to call out in the Future Vision on
this slide because I don't talk about
them elsewhere but if you look at the
platform improvements things like
support for per tenant profiles um
ability to remove setup records on
uninstall the reason I want to call
these out is not necessarily because
they're huge but these are feedback that
you've given us these are the scenarios
that you're having difficulty with today
and we know we need to take those and
make them better make them easier make
them work uh more fully so so as we're
going through this and we've had a lot
of discussions and this doesn't mean you
get everything you ask for this is not a
blank check but we are listening to
feedback and trying to understand what
the scenarios are and what the proper
ways are to address them so we've gotten
a lot of good feedback please keep that
coming in and we will continue to listen
on
that so I want to dive in now to the
things we've added in nav 2017 um and
just go through this list quick talk
briefly about all of them so one of the
scenarios we had was I have a lot of dat
in my application how do I get that into
the running system how do I manage that
and the way it was done in na 2016 was
you have code units go write your code
unit and push all the data in which is
not a great way to do it it works but
there's better ways that can be done so
the way we've supported this today is in
if you add a non-company table so
something that goes across the tenant
you can fill that up with the data you
want through either the UI whatever tool
you want and then we've added a new
commandlet to export that data into a
file the export Nava table data and what
happens then when you get that file is
you put that in the folder of your
sources like you do your um objects that
you're adding that gets added to the
extension package and once that's in the
extension package on install there's a
new function that um you can call it's
the nav app. load package data passing
the ID of the table and we will go push
all that data into the that table and
again that's a per tenant table not a
per company table and the first question
we get is why did you do that well there
the main reason we did that is there are
scenarios that you need to think about
when you're using this of what happens
when a new company gets created what
happens if you're doing something else
in those companies and by putting it in
the pendant table if it's shared data
that can be leveraged it can be
referenced across there that's great
otherwise you the developer is
responsible for getting it into the
correct abl in the system that they
want the second uh feature is custom
report layouts again these are very
similarly used um you create your report
layout put it in the source folder and
it then becomes available in the
application um again you can see the
command L up there that we have for
dealing with that so this gives you an
opportunity to provide new layouts on
top of existing
reports the next one on this slide is
language files one of the problems with
the initial was it works great if you
want English or if you want the default
language or if you're in one local how
do we deal with stuff where we need the
different uh translations so we took a
look at um the way nav is doing
translations and we now allow the
language files to be packaged and
extensions as well um the other thing of
note at the bottom is we have with the
translation files typically you replace
all the strings that are in that file
and sometimes you want to add a new
translation to the system and with that
you don't want to overwrite existing
systems so we changed this to work on
not the whole file but on a Delta basis
like we've done a lot of other things so
we added the compare uh nav app or nav
application object language commandlet
and that allows you then to change only
the strings that you need to if you're
adding a new language you can add just
that language and multiple extensions
can add different languages without
overwriting each
other perant web services like we did
permission sets in 2016 in 2017 we've
added the ability to publish web
services with as part of the package so
if you are adding new forms um new
queries code units that you want to
publish as web services every time your
extension is installed you're now able
to do that and web services can also be
published on a per tenant basis you no
longer have to publish them for
everybody on the system um again if
these are in your package or your
extension package on the install they
will be published
automatically net add support um there's
a couple of different ways to do net
addins and that's caused a little bit
bit of confusion about this feature if
you are currently pushing stuff to the
gak um that's not the way that this is
going to work so there is some
documentation about how to package your
add-ins in zip files um that's on msdn
if you can find that information that's
the way you need to package your addins
we do support the servers side.net uh
clientside JavaScript and client side
win forms all all of them are supported
but you need to get them in that zip
file and again put that zip file in your
Source folder and it will be used the
other thing I want to talk about when I
talk about net addins is if you're doing
an on-prem deployment or if you are
doing your hosting you can use net as
you see fit or as you and your customer
or the partner that's doing the hosting
agreed to if you're are going to push
code to Dynamics
365 at some point we will not be
supporting net um we realize today that
there are some things that you can only
do with net um for example the uh client
side JavaScript add-ins need a net
interface um for now to talk to um
service accessibility is mostly done
through net today that we don't have a
good mechanism for that these are apis
that we will be adding over time uh so
you no longer need the net but if you're
putting things like business logic
inside of net that will uh fail your
validation when you try to submit to
Dynamics 365 we do scrutinize very
carefully what goes into the net
assemblies because of the security risk
it
poses um debugging we've added better
support for so the the debugger now
finds extension code you're able to
debug it uh set break points um it works
with the profiler so we've done some
work to improve the tools there to make
uh developing a better
experience and the last thing is when we
started out with ex exensions everything
was a commandlet we had lots of
commandlets and some people that was
okay they meant they could script
everything they loved it other people it
it was difficult to deal with one of the
common scenarios though is when a
customer needs to install an extension
it's a difficult scenario for them to
get uh access to Powershell number one
they may not have it depending on their
environment and number two it's the
average customer doesn't always
understand uh what they need to do in
Powershell to make this work so we've
added the new extension management page
inside the application uh as you've seen
earlier this uses the images uh that
were added so there's some information
now in extensions as well for uh images
and this is where that information gets
displayed so uh excuse me friendly for
the users here and they can go in see
what's installed and also choose to
install new extensions if you're on
Dynamics 365 this page functions a
little bit differently it only shows the
ones that are currently installed in the
tenant and appsource is the mechanism
that's used to go find and install new
extensions which is available from the
extension management
page so uh kind of wrapping up here
extensions in general they are the only
way to publish code to Dynamics 365 to
our SAS service so if you some people
have kind of pushed off looking at
extension saying I don't need that I
don't care about it if you want to be on
Dynamics 365 it has to be in the form of
an extension
um
appsource some of the benefits of using
that is free advertising uh this is
where a lot of mic most of Microsoft's
business products are going to be
available where the um extensions are
going to be available so this is a place
that businesses will hopefully come to
see as the place to go to find out
what's available so if customers are out
there already it's a good opportunity to
have your product out there as well
something that they can search for
something that they can find and use and
and part of this too is if we look at
the model historically for nav where you
we talked about the sales funnel in the
keynote where you're going to find those
customers spending a lot of time this is
one of those places where customers are
going to be they can go all the way
through the pipeline themselves and you
can have a customer up and running your
stuff that you had zero touch with and
start collecting Revenue off of that
customer
um so we talked about upgrade uh we are
how extensions are meant to be easily
upgraded able there have been some
concerns about performance especially
with large data we are currently uh
looking at ways to make that better and
I'll talk about that a little bit later
on in more
detail um when we talk about appsource
the only people that ever see the
extension package are you and Microsoft
that have any access to that at all so
one of the concerns has been IP not just
around extensions but um nav code in
general so this is one way where you no
longer have to ship out your code to a
whole bunch of customers customers other
partners that need to work with it it's
available in that one location and they
never actually get to download the
extension
file
um es yeah um and now to something
completely different um it's no secret
that we over the years have spent a lot
of time internally talking about the
audience for our developer tools we have
been wanting to I mean have a broader
appeal to the younger developers and we
have as Marco peric mentioned at the
keynote at directions he was talking
about the coffee shop developers young
people sitting with their fruity
flavored laptops at coffee shops
Starbucks coding in PHP go or some other
cool modern language and and we have had
the feeling that that Seaside as such
was not really cool and attract itive
enough for that and and so we have had
many and long discussions around that
over the years and
and one of the things we have noticed is
that I mean even though that that we as
Microsoft think that that the app that
we delivers out of the box is fine
finished and perfect you always seem to
have something you want to fix change or
because we did it wrong so we know that
that good developer tools are important
so even though that we have been talking
about these coffee shop developers we
also think that this new tooling are
meant for you and as a big
upgrade um and that's really important
to stress that this is not only to
attract new developers it's certainly
also to make sure that you all have a
better tool set than than what you have
today um to try to talk you through the
process that we have been through um
this one yes over the years and we start
with this and I mean everyone loves a
classic right and that's I mean that's
probably why they became classic at the
beginning um it was affordable everyone
loved the
Simplicity and and I mean even using air
pressure to to to to drive the uh
windshield washer fluid seemed like a
good idea back then so did the F5
intelligence bed into Seaside
um over the years we we added a number
of improvements we added a new editor
this one got a rim new rims and a paint
job something else we also added new
reporting I mean not all of the
improvements were equally successful but
we have
improved but at some stage I mean even
Classics they're getting old it's not
Thrill Is Gone it's it's not the same
and you start thinking about I
mean what should the new one look like I
mean how can I get a new classic um all
the new ones they are more intelligent
they are
faster
and so you begin begin wondering about I
mean how should it look like what is a
good next iteration and clearly I mean
you could get go with something same
color same shape but I
mean it's it's probably not going to be
a classic even even if we fixed all the
small annoyances like I mean the if if
if the date is in another format you can
import the text files if 12 is not
working all the places even if you fixed
all that I'm not sure that this is
actually what we would like to end up
with um so we did some more things
I mean maybe it's time for a real change
and maybe something pointing more
towards the future right we could keep
the collar but I mean get the latest
Technologies and update it over the air
stuff like that so maybe there's another
way and actually I
mean I have this pictures here is
running inside this new year because
it's actually within Visual Studio code
which is our new development tool but
that this is running and um I have used
the markdown language which it
supports internally let me just go here
and as you can see we actually
have some some toolbar on the on the
left side here and down here there's a
one called extensions and you can see
it's actually it's prompting me I don't
know if I can make it
larger zoom in bit yeah
one
more there is at the at the left side
there's a notification saying it's
actually ready to be updated over there
in this case it's the C extension I have
installed but even more important on top
of that there's a new extension in there
which is the a language which is the one
that we are going to
use so let
me jump away from this presentation
one and pick a small
demo
and
just
oops away
with
there one of the things one of the big
pains with Seaside over the years has
always been the way it handled any
character and any character not included
between a and C so I actually took the
opportunity here to show that that with
the new environment we are fully
supporting Unicode you can write I mean
your text files with all the different
languages you can canop and I actually
chose to do hello world and since my
own language skills are are limited to
to English and danish I used Bing
translator to get a few all the examples
here and and you can see it's handled
gracefully so let me add some code
here let me add my own favorite here at
the
bottom and do like this and as you can
see as soon as I start tying typing I
get I immediately get instant
feedback from the compiler which is
running in the background so I can type
along here and this see while I'm
typing error me messages are
changing
Danish patter like
this and all the red ones are are gone
so let me scroll up a bit here and as
you can see it's it's I mean we have
preserved the important part the a
language itself we have had to make some
changes to the source files because
frankly the the current text files are
not really useful for writing anything
just on
a just by hand I mean there's a lot of
wides space um Reliance and stuff like
that we have gotten rid of that and if
you want to you can actually write a
code unit on a single line I will not
recommend it but it's
possible so let us compile this and I'll
do this by doing control shift B
and as you see a couple of things are
now happening on the top I get the
information that a default manifest file
has been created for me and down at the
bottom there's an output window and what
goes there is actually the output from
the new command line compiler which is
the true command line compiler you
compile source files into a package
which can be
deployed and if we look over here file
explorer you see I got the app. Json
file here and I got another
file which has the extension nav M for
now that is the compil
output
um and if we look at
the app. Json file here you will notice
that there's a lot of similarities with
the uh with the Manifest file that
you're using for the current extensions
so but let's just correct this a
bit call it hello
world this one should Microsoft like
that and we can build
again and it create creates another one
actually with a new name I
suggested then you notice here there's
another icon out here who got a number
two on it which is actually the built-in
git integration because I added a new
file here and I made some changes to the
other one I actually automatically get
this I
mean listed as changes in in because I
put this in git um very nice and very
convenient so but let's close this one
here and create a
new code
unit do it like
this create h world.
sorry and as you can see what you get
here is just I mean basically a blank
piece of paper and to make it a bit more
easy to get going we have added some
Snippets so if I type CC I get a
suggestion here example code unit with
one run trigger I like that
one fortunately we still have the IDS
but we are working on
it give it a name hello world like that
and then I actually want to do a message
box calling the um methods from the
other code unit so I'll add a variable
here notice no
dialogues do it like this
greetings code
unic and now it actually loads All the
known code units from W1 which are the
one I'm building on here but right now
I'm just interested in the greetings
management the other one I have in my
project
here and then I'll do the message box so
I can start typing and actually we got
intelligence here as well suggesting all
the buildin methods I can type a couple
more do it like
this and I get some useful information
about how it works but what I want to do
is actually use the variable here
greetings call the random get random
greeting like
that
boom that's it let us compile that
again fine it works
compiles but if you're not really
building the compiler it's probably not
that fun at this stage because I have
just compiled some files and Stu it into
another file so I think we should try to
deploy it that will probably make more
fun out of it
and we I mean I know Thomas at the
keynote talked about how complex it were
previously when
you did extensions and had to do a lot
of steps so we boiled it down to one
take your finger press A5
here and just need to have
F like
that runs the compiler and then it up
here the first time tells me I need to
select an environment what I'm actually
picking is the debuging support for
dynamic 365 for
financials that gives me a launch
configuration file think about it as
where should I deploy this
to um so I'll go in
here it's a Json file luckily I have
some intelligence in here so if I do
server fine I'm deploying to local
host I need to specify server
instance domain mine called and one more
thing because it's local I need to
specify I'm using Windows
authentication like that do a five
again it's compiling it packaging it and
now it's publishing to my local server
what I actually should have
done I'll do that show it to you
later should have showed you before that
this picture was actually empty before I
deployed
it
um but that actually installed the
extension but hey wait I mean code two
code units no one is calling them so
let's let's try to wire them up to the
existing application instead and what we
can do is actually to go back in here
and use one of the new extension objects
we have added namely a page
extension so I will add one called
customer card
extension like
this again I will use a snippet to get
started and give it an
ID one
customer
card
extension this one here should extend
the customer
card like
that now I have two different sections I
have one which is called layout which is
all about the
controls groups and all that but in this
case I'm going to add an action instead
so I'll go down to the other one here
the action
section
and what we we have added here is the
ability to very very
specifically to to to specify what you
exactly want to do in this case I want
to add an action first within a
group and I will actually add it just
pick the first one the customer group
here and
I then oops add the action here I will
call it say hello
like
that just again if we go
here and then I will do and as you can
see again I have intelligence here I
will do run
object on code
unit this case the hello world one I did
before so I will also like to put an
image on
it and I will pick m because it looks
like
world let's also
just put it in a promoted
category let's pick
eight now I got some information here
down here saying
that I can only use promoted if I
promote a category if I said promoted to
true so I'll do that
like
this and
again I will
build and
deploy like that let's go back
here go to the customer
card one here and actually you can see
up here we have this say hello action
and if I click it I get hello
world I think we are back to
yeah so what did we just see here I mean
we saw Dynamic 365 for financials or
actually it was the on Prime version we
call Dynamics nav Visual Studio code and
we saw the nav extension we have built
for visual studio code with intelligence
background comp compilation syntax
highlighting Auto completion
Snippets navigation Unicode and Source
all the good stuff that you would expect
from a modern
development we saw an extension object
the new pce
extension and we saw how easy it
actually is to build build package and
run an
integration so a little bit more about
Visual Studio code first of all it's
free I mean who doesn't like that it's
not Visual Studio but recently the
visual studio code group become a part
of the visual studio group internally in
Microsoft it's optimized for code and
there's also a debugger integration
which we haven't it's not ready yet but
we'll get
there and there's building native kit
support I showed you that it's so nice I
mean I have been running my demos out of
a small git repository locally and I can
just revert them back whenever I'm done
with my
demo it's updated monthly if you're
using the normal one or if you want to
be more adventurous there's also um
nightly
build um it runs on Windows and Mac and
Linux
platforms it supports a ton of
extensions I mean there's more than 1600
the last time I looked and there's a
huge Community around it it's it's open
sourced on GitHub and and I mean there's
lots of people um basically coming with
suggestions and then they are very good
at
fixing un unwanted features stuff like
that and add add new improvements so
it's a great
tool so we've talked a lot about Visual
Studio code and it's very much a tool
targeted at um what we call the pro
developer somebody that likes to get in
get their hands dirty knows what they're
doing very very much and the slide is
called two sides of the same coin which
I don't think is quite right really
because really you have a spectrum of
developers you have people who show me
the source code everything else gets in
my way that's that's all I want you have
developers that yeah I know source code
I can go in and work with it but I'd
really prefer some kind of visual
designer and all the way along that
Spectrum until you get to the far end of
the Spectrum which is the minute I see
code I'm out I'm done at that point and
those are people that we don't typically
think of as developers but often times
there there people in a company that
want to do simple modifications how do I
change the layout of stuff how do I add
a new field to store some extra data I
don't need any business logic tied to it
I just need something simple and one of
the things that talking to those
companies if they have to call somebody
and get a pay a large check every time
they need something simple done it's a
real turnoff to the way or to their view
of the application it becomes an
impediment to them doing their business
which is really what they care about not
the
software
so the next thing that we've got that
we're going to show and we've seen this
uh already this morning
is the in client designer
and we had some new updates that
unfortunately I don't have um them in my
environment they were done uh earlier
this week and but I was unfortunately on
a plane at that point already and I was
afraid to take them this morning just
because I know how things like that go
but talking about the in client designer
so if I navigate to the customer page
which is one we talk about quite a bit
and as you saw this morning when you get
here you can do the simple things I can
if I partner code doesn't matter to me
as much I can move it down to the bottom
out of the way
I should be able
to
so we'll try
again so I now hopefully nope that one's
not going to work for me we'll hope the
rest of this stuff goes I can do simple
things like um change the titles um so I
can change it from General Dom main I
can do those simple types of
customizations we will have support for
changing uh field captions as well soon
I can do other things like adding new
fields to the page fingers crossed so I
can drag name two
on okay so um moving along we won't be
that be that one but I can come in and
uh create new Fields as well so if I
want to create a Loyalty Rewards
program do something simple come in and
say the um values that I want it's gold
silver bronze and the initial should
always be
bronze go ahead and finish that when I
come into my new Fields now I can
search and I can see loyalty and I'm
sure this is going to go the same as the
others but we'll try it anyway yep okay
so take my word for it it works it just
apparently something I did here so um
we've showed a lot of this already but
these are the types of things that as we
talk about that far opposite end of the
spectrum these are what those users are
um want to do and it being right in the
app gives they don't have to go download
a separate tool they don't have to go
learn something else it's just natively
available to them in the tool that
hopefully they're becoming familiar with
so what else can we do here in the
designer um if I go to stop designing
one of the things we're looking at so is
eventually being able to use these
because there's simple UI customizations
in a lot of cases a lot of it can be
done for personalization as well so
we're investing a lot into the designer
that we're creating here and there's not
a great personalization story yet for
the web client it would make a lot of
sense to use this for both
personalization and uh the role based
customer um profiles as well so being
able to make the changes here and save
those out now there will be some
restrictions on that um obviously if you
add a field to a table that happens for
everybody in the company so you can't do
that add a custom field just for
yourself but as much as we can we want
to leverage uh the investment for all
these scenarios and again that goes back
to let's keep it simple for theend end
user let's give them a consistent
experience on what's
happening if we look at um one or some
of the I guess the other thing here then
is save for everybody that's the build
an extension and make it available for
your tenant right away publish the store
if I've done something that is useful
maybe I've customized it at least in
verbage and such for a vertical I might
want to make that available to other
people so they can use it as well so
pushing that up to
appsource the um so that's what we have
there
I'm going to try something else here and
see how it works is I I I don't have
this UI all finished out there's
actually uh this should be available
soon for us internally and then will be
available in December I hope um but we
started a new page setup dialogue and if
you you probably can't read oh maybe you
can read the description down there a
little bit but basically with the
description is saying the the checkbox
is card details I want to create a card
page but
in nav you very rarely create just a
card page there's other things involved
with that you create navigation that
goes to a list page then from the list
page you hook that up to the card page
and you share fields and data source
between this so the goal here that we're
going after with this design is that we
make it as simple as possible to not
only create the object you want but to
create the scenario that you want if I'm
I realize we have customers in there but
because it's one we're all familiar with
if we want to create a customer card we
typically want the customer list that
navigates to the customer card they
share fields and also hooked up to the
navigation so by clicking this on here
we're actually creating multiple Pages
hooking all that background Plumbing up
that will again make it simpler for that
end user to do that um and then looking
at other experiences such as if I've
customized some data on the card can we
extract enough information to put maybe
not perfectly but a pretty good guess of
what goes on the list page as well so
that they don't have to do everything
once once realize they need to navigate
somewhere else and do it all again can
we at least get them pretty
close the final thing I want to talk
about with the in client designer is
underneath the covers this is creating
an extension and this is one of the
scenarios that the new compiler that
we're investing in allows us to do with
Seaside it was a standalone application
we had to push all the objects into
Seaside do a compile we did that off in
a separate environment because we didn't
want to corrupt the environment that the
customer was currently running in with
the new compiler we can
do take the file basically generate the
files here through an API around the
compiler take those files compile them
on the command line they're all filebase
now so we don't have to touch the
database we don't have to worry about
setting up a shadow database to do our
work in and then once that's done we can
build it up as an extension and do the
publish on the Fly because all that
tooling is there
now um so the the next next thing I want
to talk about is Espen showed briefly an
extension object in this case a page
extension and we've done it to ourselves
again we've created verbage that is
going to get confusing we now have
extensions which are the package and we
have extension objects which is
something that modifies another object
in the system so the two that we have
right now are page extensions and table
extensions and starting with the
developer process of this I'm sure
everybody's favorite thing to do right
now is to create the snapshot out of the
database that you're starting with make
your changes to the object create export
the result of that then compute the
Deltas then roll everything back to the
original database that you can build the
extension and test what you're doing oh
you made a mistake so take the extension
off start that process over again it's a
lot of work it's air prone it's not a
great experience so getting rid of that
now from a development perspective you
never have if you want to modify the
customer page you never change the code
on the customer card again you now write
an extension to the customer card and
you author with intent exactly the
changes you need to make and that with
intent is another phrase that we want to
talk about because today when you modify
the customer card you're basically
saying as you're doing your development
this is what I want the customer card to
look like when I'm done the problem is
then you go ahead and compute those
Deltas maybe the underlying customer
card changes maybe another extension
comes in it never actually looks like or
may never look like what you actually
off authored it to look like here now
you're describing what the changes you
want are and it it's a little easier to
understand exactly what you're getting
or again what your intent is in your
authoring as opposed to doing those
modifications um the way it had been
and the last point about the development
experience around this because we have
the new compiler because these extension
objects are first class citizens in the
compiler the compiler understands what
you're doing with Seaside you could go
add code to a page and I know I've heard
this from a lot of people the first
thing they do is they go in and they
change a key on it change the primary
key on a table go in and add code to a
page or a table they spend sometimes
weeks developing what they think is the
perfect extension and they never build
the extension at that point they're
focused on development which makes a lot
of sense that's what your intent is is
do the development and then you get to
that first time you go build the
extension and the first thing you get is
you can't do 50% of what you've just
done go back and start over and try
again thanks for playing that that's
it's obviously not the experience we
want so now that the compiler
understands these as you saw from the
syntax the red squiggly lines it knows
exactly what is allowed when you're
authoring it which again should improve
that experience
greatly so moving on to what this
changes in the platform is again we
talked about them being first class
citizens and what do we gain by this so
right now when we do the publish and a
customer installs the extension we end
up with multiple copies of the customer
card on the platform we have one that's
the base object we have one that has
extension a put into place we have one
that has extension B put into place we
have a third one that has extensions A
and B put into place depending on what
customers are using so we end up with a
lot of copies of the customer card and
and this has some inefficiencies with it
by moving two extension objects and
making them first class in the platform
as well we can have one copy of the
customer card metadata that's shared
between everybody we can then have the
extensions objects one copy that's
shared between everybody and as a users
come in we figure out what combination
of those we need to put together to get
the right information to the client but
we get some efficiencies in the
platform U so that goes to the Not
Duplicate objects as well the next one
um we have a we've talked to Partners
that today say please just write me let
let me write a little bit of code on the
page so let me write a little bit of
code on the table there's something that
I need to do that I just can't today um
I think Set uh filter record I think is
the API that's only available on Cur
page so I can have an event that I get
called when get called when the event
fires that I care about but I don't have
access to the apis or the information
inside the page that I need to to do
what I want to do with that with these
being new objects now all the reasons
that we've said we're not going to allow
code those now go away because this is a
new object we can expose certain aspects
of the page to a page exension extension
uh some of those apis um and things one
of the other scenarios was if you add an
action to an existing page you weren't
able to write code to that it was fine
if you wanted to um just call run object
on something if you again if you didn't
need the actual data from the page you
were okay but there were uh apis that
sometimes you wanted to call in order to
set up the new page that you were going
to launch and that wasn't available this
will give you the opportunity to add
code in those places
so going
into demo here or very short of what we
have here I have a a very simple
customization here and I'm going to look
at two objects so the first is a table
extension and here you can see what
we're talking about is I I've added a
new field to the customer table and I I
didn't have to go in and modify the
customer table itself I I I said exactly
what I want to do I have a new field
also you can see the trigger there for
onvalidate I can handle that and I can
write my code in there and uh do things
I need I can add new uh functions as
well and have those called from inside
and outside uh either which makes sense
so this will work very similar today as
of right now if you're modifying the
customer table but again you get you
understand exactly what you're doing as
you're writing it there's no more going
into the uh customer table and saying
what parts did I add what parts were
there before did I do something I wasn't
allowed it's very straightforward
here and now then with the page
extension you can see the same thing we
talked about the layout we talked about
um being able to do ad last and I can
take the field that I added from my
table extension and add it to the
customer card page through a page
extension uh can as Espen showed we can
go add actions we can add code behind
that um we can start hooking things up
that way and make it uh impactful that
way the way we need to so um and just to
show us working here I I launched this
or installed this one earlier so let's
stop
designing and on the customer card you
can see here I have my shoe size with um
with its value um so this is kind of
what we're moving towards trying to make
it a little bit more obvious what you're
doing during development make the tools
work better for you during development
and take out a lot of the overhead steps
that have been there because we were
trying to use uh the tools we had
available to us at the time
the next thing I want to talk about that
we're doing for an improvement is we're
changing the way that data is stored
when used by
extensions um today as you may know we
actually if you modify the customer
table we actually change the schema of
the customer table the approach that
we're taking moving forward will be that
we store the data in Separate Tables so
so if you author a table extension it
will get its own table in
SQL now there's a couple of things that
that means but um one of the things is
to to note about this is you don't have
to reference it as a separate table the
table record apis will take care of
getting all that data in place for you
take care of where the data gets stored
which tables they need to write to doing
it in single transactions that sort of
stuff so the usage of this is very
simple but that storage is separate so
the question isn't why would we take the
effort to do that uh if the API is the
same or going to be very close to the
same a couple of problems we've been
listening to is naming conflicts if you
extend the customer table and you put a
shoe size field on it and then Microsoft
extend or changes the customer table to
put a shoe size on it your extension is
broken it it it doesn't function anymore
because when you try to install it again
after the changes there's two fields in
SQL with shoe size it it SQL can't
handle that so so this will give us the
ability to have avoid name conflicts and
especially now if two um Partners add
the field shoe size they can both live
in there and we don't have to worry
about all the referencing because the
compiler knows that when you are
referencing shoe size you probably care
about the one that you added not the one
that somebody else added that you didn't
know about at the
time one of the other concerns that
we've addressed or that this helps with
is the upgrade process today with
today's upgrade model we have two
separate upgrade models one for
extensions and one for the core
application and the core application if
you upgrade that with extensions in
place there are mechanisms that need to
know the entire exact schema of of the
table to work and when those happen with
an extension in place that has new
Fields it doesn't know about the data
that the extensions added and the result
of that is if you do it with the
extension in place it will lose that
data as part of the upgrade which is why
we our guid today is always roll your
extensions off upgrade the Bas
application always put your extensions
back on because this data from a SQL
side is now stored in Separate Tables we
can mitigate some of those uh concerns
and work on ways around
that
um and then also we talked about
hyperscale I think a little bit this
morning but what the hyperscale is is we
want to push more um or make available
the ability to share schema between
tenants so if you have some very
lightweight scenarios customers that use
a little bit of data infrequently it
doesn't always make sense to spin up a
whole database for them um the overhead
of creating all the schema the little
bit of data they have uh you can gain
some cogs and efficiencies by if they
could share a database by uh the
extensions having their own tables now
part of the problem with putting them
into the same database is or one of the
problems is that if two tenants have
different versions of the customer table
how do they share that schema at that
point but if the table extension data is
stored in a separate table again the
everybody shares the same customer table
at that point if people are using my
extension everybody shares that schema
as well if only five people are using
espen's extension those five people can
share that piece of the schema but not
everybody else um is driven by that so
the companion table here that we've
talked about again has some efficiencies
that way and is something that we intend
to leverage going forward more the last
thing I want to say about upgrade I I
talked briefly here about some of the
things that will allow us to do and I'm
talking some about what it will allow us
to do because we're working on changes
to the upgrade process overall right now
to try and make that a smoother process
instead of having two hopefully we can
get down to one upgrade process for
everything um so more will be coming on
that in the future
yeah um what I'll show you now is a
more more a deeper demo of what you can
actually do it's it's it's a small
extension we had our one of our
application developers do but um what I
forgot to do before was basically to
show you like the magician there's only
the hello world in
here so
I will go back now and and add a bit to
this extension um and then deploy it but
first I will tell you a bit about it
it's it's it's an extension that
actually is is targeting the UK market
and what is special about the UK Market
is that their post codes are
actually um describing very very small
areas so if you have a post code you can
get a list of 10 20 addresses to pick
from so actually the post code is often
the main entry field on an address so so
if you enter the post code you will get
a suggested list of of of addresses um
more precisely so what it actually does
is it utiliz an external web service
where you can send out the the post code
and get it back the list of
addresses we have added that
and and there's a couple of I mean I
just need to find my mouse
here in here there's a Code unit that
does most of the heavy lifting and if
you see here we have added some
additional intelligence here or symbol
look up so you can actually navigate
through the symbols within the code unit
here we have an even broader one which
allows you to search for any symbol
let's try on there's a couple of things
that has On in
It
ums we have a data layer with some
tables and as you can see the table here
we have changed the layout slightly to
make it more easy to work within an
editor
it's there's a service connection
setup and then there is a couple of
pages
what I want to do first is actually I
will I will make a small change to the
customer card because since the post
code is now the preferred entry field I
would actually like to move it in front
so again what we need is a page
extension so I will do another custom
card
extension
to again I would use the SN
feature custom card
extension custom
card this time I will go into the layout
section and what I want to do is
actually to move
the post
code as the
first um as the first entry in the
address details group so I'll select
that and then I need the post code like
that and as Michael mentioned this is
very M very much about stating your
intent I mean my intent is move the post
code field first in the address section
it's not designing the entire page it's
just this specific action and and that's
all I need here so let's do this five
build it and deploy
it so now it has been published to the
server let's go back in
here and do the refresh and as you can
see I got another extension
installed and if we go in here into
the service connection
page see what we have here we actually
have this address
setup which contains the service URL and
a key to allow me to actually go out and
fetch the the addresses for a post code
so let's go out of this go back into
oops let's create a new
one create a new
customer like
that my
customer and as you can see down here
the post code field is actually now the
first field in the address and contact
group and just by adding that single
line so what I actually how it works is
I do like
this I know one that should work and as
you can see we have utilized the
notification feature here I actually I'm
being asked now whether I want to look
for addresses for this post code onion
yes please I would like that looks it up
and I get a nice list of addresses I can
pick from I select one and it actually
fills out the other
fields this is an example of how to what
you can actually do already with the
tool set we have Pages we have tables we
have code units page extensions tables
extensions and it's actually possible to
to build I mean real
extensions yeah
um up there yeah so list of syntax
changes and as I mentioned before they
they we have try to keep most of the
existing text file format as is we
haven't changed the a we have the same
methods we have the same
layout but but all the surroundings the
metadata definitions like how do you
defined Fields it's it's it's changed
but it's changed to make it possible to
add comments wherever you like with wack
whack you can do it next to the option
strings defined in the
field um and you can write it on one
line do not do it um but it's all about
making the layout more writable and
readable
um and I think we have some page
extension and Page syntax see changed
slightly rather than having the flat
list in the current page um format where
the controls are basically the the
hierarchy are specified by a an integer
specifying the indentation we have
chosen a hierarchical structure here
with some names which lit up or are more
visible when you actually look at it
because syntax highlight and kicks in um
and then we have tried to create a page
extension for format which
are similar as as much as possible to
the to the layout for the actual
page
um sure okay so talked a little bit in
the beginning about net interrup and
we've had a lot of questions about this
can I is net interrupt going to be
available is it available now in
extensions is it going to be available
on new stuff we're doing and as I
alluded to earlier it is available now
we support the net add-ins we realize
that that's a critical piece to people's
business right now that taking that away
would um stop a lot of people from
building
extensions in the first place going
forward one of the things we've said is
our intent is to get rid of net now
that's that's probably a little harsh um
but we want to prep people for what we
decide to do going forward so uh right
now in the stuff we have there is no
access to net
our goal is in um Dynamics 365 that you
will not be able to use net longterm
going forward as we talked about this
means that there needs to be an
alternative though and we're not going
to take away net support until we have a
good
alternative um so couple of options
right now there
are um Al objects that expose some net
wrappers or expose some net objects
those are one mechanism that we have
that we could potentially uh allow
things to go forward the other thing is
we would like to create or talked about
creating some new objects for the common
scenarios and the first thing that goes
through people's minds when we have this
discussion is you're getting rid of net
you can't do that it'll never work and
then you say okay what do you use net
for what what are you doing with net
today that you can't do otherwise and
there are typically six things when we
talk to people and if I try to list them
off I'll probably get four of them but
there are six things that people almost
almost always always say these are what
I'm doing it's I want to call web
services once I call web services I need
to get to the data which means you need
XML and Json apis because I need to send
that across through the services and I
need to parse that coming back um string
manipulation is another one collections
are another one and as you see so far
these are things that we could add to
the AL language with without a lot of
difficulty and the last one we get is um
uh JavaScript add-ins or add-ins in
general but especially the JavaScript
the interface is defined as a net
interface but if you look at that list
that list isn't huge that list is not
unachievable um there are obviously some
others that people use just because
nobody's ex there's always something
that there's a unique case but 95% of
the people we talk to is within that
list so we realize that net is important
for what people are doing today and we
realize there needs to be a solution for
what people are using it for today um um
the Azure functions do you want to talk
about that one a little bit Yeah Azure
functions is I mean since we are
planning to add the ability to to call
externally to the air language I mean
ashure functions is is a is a feature in
Asher where you can write a piece of C
code which is exposed as
a as a as a web service that you can
call using a rist API and and our plan
is to support that so it's an easy thing
to work with if you have some critical.
net code which are probably should do a
a a larger piece of work and not just I
mean trying to flip a flag on an Excel
spreadsheet something like that um but
but it's a way to isolate and
park.net code which is then callable
from within a without compromising the
security of the uh our service
um so we we've talked some about things
that we're doing going forward a lot of
these are near-term we're not too far
off so we have a pretty good handle on
those obviously everything is subject to
change what I'm about to talk about now
though is things that either we've
started planning on or um one of them is
something that Marco mentioned in a blog
so it's obviously completely defined
because he mentioned it publicly um but
these things are very much subject to
change please take everything as a this
is the direction we're going rather than
these are the specifics of what we're
doing especially from this point
on so we talked about solution apps
briefly this morning and if you look at
the diagram here we have
um an example of the way we'd like to
start layering the application and when
I say layers that has a lot of
connotation for some people it's not
that just we'll get to it in a minute
but if you think about the way things
are done today or were done let's say
three years ago in an on-prem world you
had
the ball of everything in it you put the
AL code on the platform and that was it
and you went and modified the AL code if
you needed something and there was no
separation of what was going on in nav
2016 and we've enhanced in 2017 we had
extensions which is that top layer where
now we can start to put modules side by
side um on top of the solution you could
still do code customization that was
still available but now you can put
these extensions on in place you can put
them on take them off upgrade them
independently they can work side by side
they don't have to know everything
that's going on inside the application
to function so the next step we've
started to look at is solution apps and
the first thing that we talk primarily
about is that second green box the one
that says isv solution app and what
we're looking for here is extensions are
great for functionality that has limited
scope most often it's where they really
hit their sweet spot but what they um
what that allows them to what we're
looking for a solution apps is I need
deeper customizations I I need to change
the business logic not just react to
what's happening within the system and
again we're starting our design on this
so all subjects change but we're looking
at things like how do we give you the
ability to change the functionality
right now we've got the two ends of the
spectrum that we have we've got I can go
in and modify code and I can go respond
to events problem with events is there's
not enough of them how do how do I hook
up to somewhere that's nonevent we've
talked about well do we add pre and post
on functions the the thing that we get
there then is always well what if what I
need to change is between line four and
line five of the function I need to add
a new conditional or I need to add an
error message if there's a new case for
my logic so before and after doesn't
work um so we're looking at ways
potentially to allow you to take control
of a function and this is something that
we're able to do in a solution app world
because at that point in the application
there is one extension that knows about
everything that's below it in the
application and this is where we start
talking about stacking in the layers
there's no explicit layers like you I'm
at layer 75 whatever it's at that point
in time I'm building on top of another
stack whether that's just the platform
whether that's W1 whether that's um us
or uh Denmark Danish for example I I can
control everything there so if I take
ownership of a function I know what
needs to happen in the rest of the
application to go make that work and I
know that nobody else is going to come
in and say we're not going to compete
for who's
overriding um one of the things that
we've looked at here is we talk a lot
about one solution app but once you get
those principles in place they also
apply to a stack of solution apps which
means that if a big vertical creates a
solution app um and again takes that
ownership and they know what they're
controlling they they have that
additional control over the solution
then what's to prevent somebody else
from putting another solution app on top
of that I want to customize that for my
customer I want to take um the big
vertical they did and Target it to a
very Niche uh vertical something more
specific or a certain Lo localization or
region they should be able to do that at
that point because again at that point
even if the um bottom solution app did
the customization they took ownership of
functions I can choose to override
theirs as
well so now if we've established the
stack what's to prevent us from doing
localizations this way what's to prevent
us from doing the W1 the very base of
the application this way and we're
starting to look at maybe how this plays
into a stack and that's part of why we
have the boxes around um W1 and
localizations that covers both what isvs
and Microsoft can do is Microsoft has a
set of localizations I think the count
is 24 right now and if we build ours
this way and create a model for doing
this this gives isvs an opportunity to
go and create localizations that we
don't currently support to get into new
markets um so at this point again it's
solution apps we're looking at ways to
give them more control to do things that
normal extensions can't uh they're a
little more isolated um and we are
working on that right now and doing
planning so hopefully soon we'll have
more information on
that the next slide that I'm going to
talk about has very little
information called customer apps and
mostly I'm going to talk about the
problem and that we're starting to think
about it right now everything that we've
done with extensions right now has been
targeted a lot towards Mass cell
everything you put in app Source you
should be able to get to as many
customers as possible make it widely
available solution apps you're going to
make your money probably not by creating
it for one but by being able to
redistribute it and have a customized
something customized for a vertical or a
localization and if you go to all that
work for one customer you're probably
not getting your return on investment
that you want but there is still a need
for if I have everything else in place
that a customer will have some specific
needs they will have something unique to
their business that needs to be taken
care of and if the outof thebox
offerings don't work they'll probably
hire somebody to do customization for
them for their uh specific uh cases so
what you can think of this is this would
be applied on top of everything else but
would probably have control more similar
to solution apps um when we start
talking about Dynamics 365 and app
Source this would be something that you
wouldn't have to publish to appsource
available for everybody we need to find
a way to make this available to the
specific customer that you're working
with so the last thing that I want to
talk about today is we provided you with
a lot of information so the question we
get is what do I do with all this and
what we would love to say is go change
your code into extensions and mass sell
it that that that would be ideal but
that's not always realistic yet that
doesn't always work and this takes time
and there's steps that you can get to be
ready uh for this even if you can't get
all the way there yet the first one is
start refactoring your code there's a
lot of good practices out there the one
I call out here is the hook pattern
where you start to isolate the number of
objects you're modifying and whether you
go to extensions or not this is a good
thing to do um it makes your upgrades
easier uh helps you when you're
upgrading your customers because you're
not as integrated into the Microsoft
code base and as we turn our objects
you're less affected by that and it's
you can get up and going on the new
version faster so using the hook pattern
is good where you put a single line of
code in that calls out to your
functionality basically minimal
modification Star Source better would be
if you can use events to do the thing
the things you need to do start moving
in that direction and even if you can't
get 100% of the way there getting 80% of
the way there then you're well down that
path to being set up to uh follow along
with us as we continue to evolve the
second thing I would say is talking with
a lot of Partners when we released
extensions in now
2016 we got a lot of feedback from
Partners um especially ones that as we
directions and people were seeing it for
the first time that it's great but it'll
never work for me I'm my solution's too
complex it'll never happen and but then
we started talking with some of the very
very large partners that have huge
Solutions and they started doing some
things that we realized can work for a
lot of people um the first is take a
look at how much code is reuse between
your customers if you've got 60% of the
code that's common across all of your
customers customers take that 60% and
make it extensions do the other 40% in
source code modifications if you have to
having that portion in an extension
gives you a head start and gives you a
leg out and then when you go to do or go
to approach a new customer um I've heard
stories of where now that they've got
where Partners have done that move their
code to extensions for as much of it as
they can when they go to do a prototype
for a new customer that they're um
trying to sell to they can take that and
put it in and then do a little bit of
customization and they can have a
prototype up and running that very
closely matches what the customer wants
in hours instead of days it it cuts down
that time because it's dropping the
extension in is a trivial piece of work
the second thing that we've seen
especially with the huge Solutions is
yep I've got a an enormous vertical and
there's no way that makes sense to do as
an extension but when I look at what's
in that vertical I've got things like
address verification as a part of of it
credit card processing is a part of it
things that can be broken out and
isolated so rather than trying to create
one huge extension can I take my big
source code customization that I drop on
every customer and turn it into eight
different extensions and again even if
that's only 2third of my code becomes
those eight extensions now I have those
eight extensions that I can rapidly
deploy uh turn on and off depending on
what the customer's needs are and put
those eight in app source for an
additional source of Revenue
the and the last one like we said start
to build extensions where possible it
it's not always possible sometimes
there's a a piece of functionality or
something really unique to your Solution
that's just not going to work but if you
can break out those pieces and start
building them you'll be ahead of the
game and um ready for us with the
journey that we're going
on and one more thing yes one more thing
before we go to Q&A which we will still
have time for as I mentioned before
Visual Studio code is also available on
Mac and on Linux and I actually brought
one of those fancy things with me um and
um we have actually made the extension
you saw before also work on Mac maybe
also on Linux someday but
but for now we have it working on Mac
and you'll get the same Sly lines
whatever you would expect have
build the only thing we haven't gotten
to yet is deployment but that will be
there um
so we are now on multiple platforms for
the development
tools and I think that's will leave us
with Q&A yes for 15
minutes any questions
are you telling us to do all development
as
extensions so the qu um right now I'm
not telling you to that you have to do
everything as
extensions so far we haven't taken away
any of the existing tools you have
everything you've ever done is still
doable we haven't removed anything uh if
you're targeting Dynamics 365 that has
to be extensions right now but you can
see the way we've talked about some of
the platform potentially extensions may
be everything thing someday that's the
direction we're going um when how long
it takes us to get there you know I I
have no crystal ball to see when exactly
that is yet but that is the direction
that we're moving so it's very possible
that someday that is the only way to do
development but again there there are
tools that you need in place and we
don't have all those tools
today uh in terms of upgrading will
there be tools for upgrading extensions
that we created already in 2016 2017
for the new environment and how about
handling all the uh uh translations and
and all the other parts that are part of
extensions in in 2017 yes um so we will
have uh we're working on a tool to
create existing extensions over to work
on the new platform um that won't be
available for the December preview but
once we're ready to formally release it
we expect that tool to be available it
may not be a 100% all the way over but
we should be able to get you know 80 to
90% of the way there so you just have to
go tweak a few things rather than
rewrite from scratch and we would expect
then that the upgrade story if you have
say version three of your extension was
built in Seaside and version four is
built in uh visual studio uh code that
you would be able then to upgrade that
seamlessly at that point in
time about the translation oh
translation uh was supported in 2017 you
can add translation files already
today was well what currently available
and we're looking at changing the way we
do that to make it a little more similar
to resource files if you've Ed net
language to make that process a little
simpler than it is today but we'll still
be supported going
forward less power shell yes
absolutely hi um what's what is the
business model uh in the app source so
how how do I sell my extensions how do
you make money in appsource today I have
a bad answer for you right now appsource
doesn't support Commerce yet
So currently you have to add uh whatever
mechanism to your extension that you
want in order to enforce that it's being
paid for what appsource does do is when
somebody downloads it you get a lead
notification in your CRM system and you
can direct contact that customer um but
any checks any billing currently is up
to you we are working with the appsource
team telling them repeatedly that this
is something that they need to provide
there needs to be one way for customers
to get build and ideally they get one
bill every month instead of one from us
and one from every extension that they
have so it's something we're working on
but we don't have it
yet hi uh you briefly mentioned the
debugging in Visual Studio code is that
some way you are going to move there are
you going to debug in Visual Studio
code uh yes we are visual studio code
and uh also has a model for for um
for extending uh the debugging story and
we are going to use that as well to
support debugging from within Visual
Studio code it will not be there for the
preview but we know we can do it and we
know how to do it but um the work is not
done
yet I have a question when we are
upgrading A customer from an earlier
version and they have some customized
fields in their tables and we're going
to use the extensions to do the new
Fields how do we do with the upgrade
process to get the new data or the old
data into the new fields in the
extension
package so we don't have any um tooling
to support this currently my
recommendation would be if you know you
have customers in this scenario to when
you do the base application upgrade to
split the fields that were custom uh to
a new table a separate table and then on
install the extension check to see if
that table is there and move that data
into the extension table and then once
once you do the next upgrade you can
drop that table because it should be
empty at that point um so that's it's a
little bit clunky right now there's not
a great uh tooling story around it but
that would be my
recommendation we started uh trying to
work with extensions and to divide our
solution into several extensions and we
notice that the different parts of
extension can't see or communicate with
each other is
it so the fields within extension one
can't be seen from extension two
although both extensions are in the same
uh database we can see both fields in
the SQL server but not from nav so could
the customer for example see these new
fields in his own lists or something
like that yes so right now we support uh
the concept of dependent extensions and
it's again one of these processes that
today is difficult to work with instead
of your Baseline being W1 or your
localization that you're working with
your Baseline would be the code with the
um first extension in place and if you
use that as your Baseline then when you
build the nav or the navx file the
extension package one of the flags on
the commandlet is for dependencies and
you can point that to the other
extension file that you're dependent on
and then that'll set up that dependency
which will do things like um making sure
that it's installed or published when
you you try to publish the one that has
the dependency making sure that excuse
me if you know you're trying to install
the one with the dependency that the
dependent extension gets installed um so
if you have a pure dependency that that
is supported today the the problem there
like I said is you have to have the
source code for the dependent extension
in place while you're developing the
second one going forward with a new
tooling uh because we will have access
to metadata and symbols you won't have
to have that Source in place and it will
be a much easier story going forward
I would like to add on that because as
as you saw in the demos we were able to
reference um things from W1 uh the
customer card for instance although I
have no database access I do not have
the customer card as a part of my
solution here and we do that by having I
mean files containing symbolic
information and basically the lavim
files also contain that kind of
information so what you will be able to
do is to reference the other extension
from in the the app. Json and now
suddenly the symbols are visible Fields
added other code units so you it's
basically a reference model like I mean
net references so one final thought on
that is we we've talked about how we do
this in Dynamics 365 where if you're
using an extension out there and you
want to extend that that you can
download just the symbol information
right from there you never have to get
the full package in order to be able to
do that
one question over here um to develop and
deploy with Visual Studio code will you
still need access to a developer
license that's so oh I I I believe um so
remember when I said all things subject
to change in the future I'll guaranteed
promise is uh free or your money back um
so uh what we are trying to do is you
will probably have to sign up for a
developer program you will get a tenant
much like you do if you do a trial today
and you will be able to develop directly
against that tenant um in Dynamics 365
for Dynamics nav I I don't know how the
licensing model will change going
forward um you saw on Espin that we've
gotten rid of a lot of IDs already we'd
like to get rid of all IDs at least from
the um source file perspective that
obviously changes what's going to happen
with licensing I I don't know how that's
going to change going forward but
especially on Dynamics 365 we want to
keep the barrier to entry as low as
possible um free would obviously be as
low as possible I don't know if we can
get there but that's you know we're
trying to keep it down as much as we can
