# Microsoft Presents: What's new in Developer Tools

- **Source:** https://www.youtube.com/watch?v=5Pk6NYcObi0
- **Video ID:** 5Pk6NYcObi0
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 46m32s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

thank you and uh welcome to this first
session in the combined Microsoft uh
slot this afternoon um this first part
is what's new in the developer tools uh
you might already know me some of you at
least my name is Peter and I'm actually
a product manager right I think I'm the
first one on stage at Tech day so that's
a huge honor don't tell Luke right but
with me on stage I have real developers
I have Stefan he's the engineering
manager on the dev tools team and I have
Espen he's the architect on adep to team
and uh today we're going to talk uh
mostly about uh sort of the news in the
last release but also a little bit of uh
news in the prior release but just to
understand the audience a little bit
better so how many here are by raise of
hands
developers yes great that's awesome um
how many of you have seen the launch
event video or record recording on
YouTube on what's new in developer
tools so that's less so that's going to
be a huge overlap right it's a but for
the rest of you you can watch this or
you can watch the recording on launch
event afterwards if you want to see the
details of that there's going to be a
recording anyway on on this as well
anyway on the agenda today uh we're
going to talk about um additions to the
language so we have the ability to have
um object extensions in the same app uh
as the the base object uh we also have a
number of improvements to the language
itself I'm going to talk about system
application debug some appsource
functionality uh as well as some
additional features from the previous uh
release but let's start with you thank
you
Peter so let's talk about having object
extensions and the app in the same as
same in same as the base so what is this
all about it's
quite simple it allows you to put
extensions one or more in the same app
as the base object you can have for
instance a couple of table extensions in
the same app as the table they are
extending you can also just have a
number of extensions in the same app and
then extend something in another
app why would you do that and one one of
the reasons why you would do that and
that's actually what we are using it for
internally now it allows us to structure
our code around refactoring we can keep
different parts of the application
together and that may not necessarily be
the same as the base table for instance
the sales order contains a number of
fields which are actually related to
other areas now it allows us to
gradually separate them into their own
folders in our case their own namespaces
and by that giving us a better design
and
maintenance so why have we done that
until now because it's something we have
wanted to do for many years and actually
all our tests when we test the compiler
actually does this there's a couple of
reasons why we didn't do it the first
and primary reason why we haven't done
this before is because of table EXT
and this drawing here shows how we
actually structure an app couple of
table extensions in their own app and
the result of that would be that you
would actually end up with three tables
in
SQL and this is how everything
worked up until last
release or actually the release before
last fall
um and this is how we started out from
the beginning with tables and table
extensions the problem with that is that
whenever you querry a table you will get
a
join and we have from the beginning
thought that if we allowed you to easily
create table extensions and tables in
the same app you will actually have an
excellent opportunity to shoot yourself
in both feet at the same time and we
would end up have a lot of performance
problems
then last Rel least there was a change
rather than having a a companion table
for each of the table extensions we
actually combined all table
extensions into the same SQL table so
you end up having two there was a huge
Improvement and we were actually at the
same time working on this change to
allow you to have them in the same uh
table table extensions and tables in the
same app but decided to wait because
these two features were sort of
competing so in the way One release this
year we added the
ability to have them in the same and we
did it a little bit smarter because if
you put the table and the table
extensions in the same app we actually
collapse it into one table so there's no
performance penalty by doing this now
if you add a table extension in another
app you will go back to having the
companion table but if you only have
table of table extensions in the same
app you will have a single table and
seeq this is not just for tables you can
do it for all objects that is extendable
they can now
have base and extension in the same app
and in all the
combinations so let me show this
together
with appsource cup because this is one
of the things we need to make sure also
works because if we in this case try to
delete a table field
here this is the small example is hooked
up with appsource cup and the previous
release of this app and as soon as I do
this I now now get an error from ABS cup
saying I
actually have removed the field which
was in the previous
version but as you can see here I can
take this table extension down here that
adds the field as a table extension in
the same map and
immediately it actually fixes the
problem so I can start refactoring
inside my app without breaking uh
dependences and the same goes for
tables and now Pages here and enums I
can come this out and
again I would expect expect an error
here
ah no I have deleted something here
same for pages and if I now add the same
action down
here solves the
problem and as you can see here we have
already started doing this ourself
inside the base app this is actually the
business Foundation where we have moved
number Series in and we have a table
extension in
here you see number series number series
obsolete it actually one extends the
other
oh this is in the same map and we are
going to do this more and more as a part
of our
refactoring thank you ESP thank you
really nice y so now I'll walk you
through some of the changes to the
language that we've introduced over the
last year
um I'm not going to talk about extending
interfaces is and as and this just so
you know that's not part of this talk
and I decided not to show any slides so
I'm going to go straight
to
code it's much better right everybody
loves this and has the Dark theme
right okay so first thing to talk about
is nam spaces we talked about it last
year so I'm not going to say anything
else but go to the session tomorrow if
you want to have some answers and if you
want to have the opportunity to ask some
questions about Nam spaces so moving on
the next thing I want to talk about is
tool tips on tables you now have the
option to Define tool tips on tables by
doing so the tool tip can be reused
across all pages that has this field on
it this makes it much easier to maintain
and the likelihood for two tool tips to
be different on two different pages is
going to be reduced signif
signicantly if you do have tool tips on
a page then there is actually still an
option that you can overwrite tool tip
and if you don't want to do that you can
also just move it to the table with a
new code
action I can do it for this specific
control and of course as you would
expect for the entire document and for
all in the project and if I click this
one it magically disappears and it
should go up here somewhere there it is
easy peasy right okay moving on to the
next thing let's
see we have a new action type that you
can use it's called the file upload
action it's a new action specifically
designed for uploading files and you can
specify of course as you would expect
the low extensions whether or not you
allow multiple files in one upload or
not
you get a new trigger as part of this
which has the first argument here as a
list of file upload this work introduced
a lot of other goodies with it so now we
support list of interfaces as you saw in
the keynote but also our file upload and
in outst streams so really nice to see
where this will go in the future also
maybe there's more to come in list of
something yeah
right now in this version here you have
to specify the file encoding if you're
uh getting the stream for the file that
you've been uploading uh in the next
version we will default as you would
expect but right now you need to put the
encoding here and as you would expect
you can also inspect the the the file
name that has been uploaded to figure
out which one it is is it a PDF is it a
document where do you want to put it and
so forth and then you can do whatever
you need to do with the files that have
been
uploaded pretty simple easy to work with
okay let's look at something more
interesting here all right prompt
dialogues you've all seen them and I
guess a lot of you have already tried to
do prompt dialogues we saw them on the
keynote a good way of describing how the
UI should look for standard UI in a
co-pilot experience where you want to
generate some data so this is the new
page type we call it prompt dialogue it
comes with some restrictions and
limitations one of of them being that it
has to be
non-extendable this kind of makes sense
if you think about it you're writing a
prompt some kind of generating content
or something how would you support
somebody else extending that that
requires a bit of extra work so you
cannot extend it to begin with at least
you can put a a source table on it but
it has to be temporary again we want to
be secure in the way we generate content
so we recommend that users go and access
accept the generated content and then
you can copy it to the real
database the P prompt dialog has three
major layout sections there's the prompt
section this is the place where you put
in the data that needs to be a part of
the prompt it could be a fre text like
it is here but it could also be the the
values of uh like Dimensions or whatever
you need in order to generate the prompt
that will create content for you you
have the prompt options area here we saw
in the keynote there was a nice way to
get quick access to some good prompts uh
to be inspired or maybe to do the same
task again and again and again here you
can add your
own oh sorry I actually this one is
wrong okay I'm going to scratch that
we'll get to that a little bit later
prompt options is ability to add
additional options to your prompt in
this case here I'm adding error so in
which uh period of time you want to
generate content for um it will be
options on the the list here I'll show
you in a second we'll get to the the the
other prompt suggestions in a second
okay going to the last section here the
content that's the produ content we have
the the produce content here in this car
situation here I want to produce some
content that describes a car and it it's
going to describe the make model year
and the description of a car so all of
that from my prompt
okay so that was the content area then
we have the actions first off is the
system actions and here you have now the
ability to override or create the
function that will generate content you
can also choose to implement regenerate
then you get the regenerate button okay
and cancel and attach for attaching
files to your prompt and now we get to
it this was the prompt guide I was
talking about before so this is the
guides to give users quick access to
easy prompts in this case here is a easy
prompt for uh getting content for 7s
cars uh it's a nice V8 engine here I
want to put in I'm a k guy I don't
know okay uh so here you can add all the
the things that people have to repeat
every now and then you could put in
templates where they only need to change
like a few parameters and making it
super easy for people to generate
content uh from your uh suggestions it
can be a full suggestion it could be be
a partial suggestion you could also have
combinations where users can choose one
or two or three and then you'll get an
even better prompt from the user okay so
how does this
look let's have a look see so this is my
prompt dialog
here this is the content
area and I've only implemented the
generate function here the error was
what I was talking about with the
options here I've added a an option of
70s 80s and 90s cars if that's something
you want to put in you can put whatever
you need and I have my prompt guide here
so I can easily select it okay so far so
good let's move
on
so here we go you saw the nice button in
the center of the screen also saw in the
keynote that that's what uh Ida and
Vincent were presenting
that is this nice button
here these are actually copile actions
that are in this menu up here and the
first one is the one that gets shown on
the middle of the page it only works for
some pages so it doesn't work for cart
Pages at the moment but it works for
list list parts and standard dialogue
and worksheets and you can add whatever
prompting actions you want in this case
I'm going to add this nice little one
here and it's just going to run my
prompt dialog
I can use this action to collect some
more data and put it into the prompt
dialogue in this case it's just going to
run it and then hopefully something will
come out of it in the other
end okay you might also have noticed
this one so we got the opportunity to
add instructional text to
controls the instructional text Will
populate the grade out text in the
background of the control so you can
give users instructions on what to put
into the control itself of course this
works for text not for
numbers but uh in this case I can show
it here so I have here if I want to do a
new one you can see here I'll get it in
the
list what I should put in as soon as I
click
something I can start typing and when I
type it disappears so it's not data it's
just a hint to the user you also saw it
in the the dialogue here as a hint to
the user on what to do with this control
that's pretty nice it's not tool tip
it's right there you don't have to hover
for
it
okay some unrelated features that we
added so for those of you who are
working with number sequence you will
now find that there is a restart method
on number sequence allowing you to
quickly restart a
sequence you can of course only do also
do it from a specific point in the
restart or in the in the series and for
specific companies if you need to but
new functionality to add or to restart
number series you also have
functionality to reserve a range of
numbers in the number Series this is
quite useful when you do bulk inserts or
bulk
Creations so you reserve a range and
then you go through it as you would
expect pretty
nice another unrelated here to
co-pilot for the secret text that we
introduced few releases back how many
knows about secret
text oh I'm so glad to hear that yeah so
secret text is a way for you to hide
data from whomever is debugging it as
long as you keep the data within
business Central nobody can inspect the
data as if you send it outside obviously
the people you're sending it to will get
the data that you're using what we added
in this past releases is that we added
the support for isolated storage so now
you can get a secret text from isolated
storage you can also set a value in
isolated storage using secret text you
have to be aware that once you've set a
value with the secret text as the
parameter then you can only get that
value using a secret text so there's no
way you can get it as a plain text
anymore that's also
good for HTTP client we added a few
optimizations primarily around the
cookie manage mement so we now have a
new type in the language called cookie
allows you to create cookies and you can
see here it's fairly simple a new
variable you set the name and the value
there you go you have a cookie you can
use the cookies on requests you can also
set it directly for on a request without
a cookie variable if you want to and of
course you can get the cookie value from
the request itself into a cookie
variable and you can Loop through all
the cookies that are in the request and
and get the cookies out of that request
if you need
to of course the same there's also a new
property on the client called use
response cookies this allows you to have
an ongoing session uh where you keep
using the the response cookies on the
next request as long as the client is
alive and as you would expect you can
also do it from the response itself you
can get the cookies from
there very very nice okay last
thing new obsolete States pending move
moved if you didn't attend the session
this morning then uh watch the
recording I'm not going to talk more
about it uh it's just a way for us to
move data without actually doing
breaking
changes um between
applications final word from me is going
to be debugging
so we've had to make some make some
changes in the the visual studio code
extension that now means that we cannot
support you debugging on all the
versions in the latest version of the vs
code extension if you need to do this
you need to install a previous version
that is compatible with that version of
your installation and the screenshot
shows it but let me just show it here
also while I'm at
it so you go here
and you might think if you go here you
can find it somewhere here but no that's
not where it is it is over here right
click on this one and install another
version now which version to
choose so this is an ongoing discussion
I guess um so um 14 is
25 right so minus 11 that's the trick
it's easy it's easy yeah minus 11 you
know it now you know
that's how to pick that's it for me
thank you thank you so talking about uh
debugging so another feature that
Partners have asked for has been the
ability to debug the system
application and uh I don't know if you
missed that but we got a lot of feedback
uh on that and now you finally can so
that means that if you're either
debugging your own code and it calls
into the system application then you can
step into that uh also
um we still respect in the system app uh
if there's any non- debuggable or secure
text uh uses basically right so there's
still areas of the system app that you
will not be able to reach but by and
large most of the uh code you can debug
and uh the major benefits uh of doing
that is uh as I said you can develop and
troubleshoot your own code that calls
into system app but we also um take a
pool requests for the system map from
you guys as part of Open Source and when
you're working with that of course you
would like to be able to debug and
troubleshoot that as well right so that
it is enabled by that how many are doing
contributions to open source in the
audience not a lot so that is a big uh
big opportunity uh you know we we see
more and more contributions uh luckily
now the reason we haven't uh enabled
this before is that H we actually needed
uh secure text in the in the system
application ourselves right so we needed
to launch that platform feature and tiet
in the system
application okay let's uh switch gear
and talk a little bit about some of the
investments in uh app Source how many in
the audience are you know isvs having
appsource
apps Ah that's nice that's about 50% of
the audience so um the first investment
that we have is the ability now to have
appsource apps in a preview state so
that's actually a functionality that
appsource Marketplace have supported for
you know a long time but we have not
supported that and so the way this works
is that when you now submit an app to
the
marketplace it actually ends up uh
inside a partner Center as part of the
submit process it will end up if it
passes validation being in preview
State and um that means uh that you can
share that preview state with a select
set of customers or yourself for testing
out functionality before uh you go live
right so that's a a nice way to ensure
that everything works before you go live
and then in partner Center you can then
say go live with the
application um and that you know ensures
Prime Time Readiness uh for for the app
now uh any customers who opt in uh to
this will be able to install the app uh
and test that in their environments but
we for now only support
sandboxes right and then they can
provide feedback to the isv that
everything works this is actually
something that we backported as well so
it is supported in version 23 and
higher now the way works is that when
you are in partner Center and you have
to do this before you submit right
because the preview key needs to be
defined before you submit but in partner
Center there is a place where under
preview audience you can Define um you
know we call it a private key you will
also see it being called uh hide key or
a flight key for that matter but it's
basically like a secret that if you know
that you will get access to install the
app right and you can use whatever you
want you can also use the um pre
generated string that is in partner
Center and then uh you can take and to
install the app to allow customers to
install it you can then share an install
link that's actually something we
support already today which is how many
in the audience were aware that you can
install an app apps app by
link a little fewer so uh that's
something you can do already today um
but uh what you then do is that you
create a link where you then include the
tenant ID of the customer the app ID
that needs to be installed and the
preview key and you share that with the
customer the customer admin can run that
and it will be installed in their
environment right
um now the installation process itself
is business as usual the only thing is
during installation you will or the the
user performing this action will be told
that this is a preview app uh and if you
try to install it in production it will
fail as it is
currently H so there's a couple of
things that is good to know if you are
an appsource publisher an isv then we
only support previews for versions that
are higher or newer than the most recent
public version right so your basically
previews are thought of as the next
version of something which is is already
uh public and uh as I as I mentioned uh
you have to set the preview key and you
have to do that before you actually
submit uh your
app H we support multiple different
previews at the same time you can have
different preview keys and you can have
them out uh at the same time it will
install the version but in partner
Center you will always only be able to
see the last sort of preview that
doesn't support any kind of multi
tendency but as long as you have the
link and the right preview key uh than
it then it will
work um yeah talked about that that that
um we actually uh you know understand
that the purpose of the preview is that
you want to find issues and fix them
that also means that when uh a preview
app is installed we allow installing a
new preview app version of that with
breaking changes right so it's actually
allowed to do that between the version
of the preview um but but uh uh and and
the way we do that is that we actually
perform a for sync between these right
this doesn't apply to normal sort of
public apps right but for preview apps
uh this is supported now you can include
preview versions of dependencies as well
if they're part of sort of the preview
uh package and then it's important to
understand that this is not intended to
make sort of one C you know One customer
off solutions for the isvs this is just
just for testing out
functionality if we then look at the on
the admin administrator side of this
again we support sandboxes uh only uh by
definition we could do this in
production as well but we limited that
for now that also means that if you have
a Sandbox where there is a preview app
installed uh then it cannot be copied to
or restored to a production environment
so if you have that then you would have
to uh you know either update the app to
the public version and install that if
there is such a public later version or
uninstall the preview before doing those
operations um yeah and then if there's
already a preview version on the
customer uh sandbox tenant they can
upgrade to a newer version or to the
public version right and actually if
they try to install the preview version
but you submitted a newer version to go
public we will install the latest public
version right so we'll always strive for
that so public trumps uh over preview
apps uh the same uh on upgrading you
know if we follow the uh app update
Cadence set for the environments you
know once that happens and there's an
upgrade uh um happening if there's a
newer version we will install that newer
version the public version as well and
not just the preview
version now the installation of previews
are track in Telemetry just far like for
normal apps um you know but we we don't
uh
um track them in in extension management
and the admin sensor so there a couple
of signals here that you can see if you
want to know more about this there's a
couple of links here to the fact we have
a little video on this available on
YouTube as well we talk about it at the
lunch event as
well okay then another thing that we
changed uh with appsource is that uh a
couple of releases ago we added the
ability for you to hot fix an appsource
app and as part of that when you
released uh an a hot fix for a um an
older version than your latest public
version um then we actually did
validation against the latest version to
make sure that there's an upgrade path
for customers installing that hfix to
the latest appsource version but when we
did the validation we would validate
against the first major version or the
first version on the next major version
um but the problem you know there is
that uh that had limitations and we got
feedback from Partners so now we
actually changed validation so that we
uh validate against the latest appsource
version on the next version and that
actually allows Partners to backport
functionality just like we're doing as
part of their hot fix and there's still
an upgrade path uh to the newer version
for the appsource
app uh I put in another link here if you
want to read more about how we handle
those versions you will get the deck
here later as
well uh okay then um we have a an
embedded experience inside of the web
client for browsing and installing
appsource apps um directly within the
the client itself and um that experience
has been deprecated by the appsource
team and instead been replaced by a set
of apis and so given its widespread use
we have actually um built a new
experience inside of the client and we
call that the Microsoft appsource apps
uh page and so it looks like this and
it's you know we understand this is the
first version you know we got some
feedback on this but um but please just
you know give us ideas give us feedback
in the usual channels what it does is
that it lists all of the available apps
just like in the old experience uh here
you have um maybe a little bit more
information in the list you know you can
have the name the publisher name uh the
the install State the last modified date
reviews Etc in a little more easy to
view um scenario plus you get the normal
uh functionality for filtering list
pages in BC right so now you can
actually filter e down to a certain
publisher see all of their apps or you
know just a little bit more uh powerful
experience um from the list page itself
uh you have links that you can select
well actually you have one link where
you can just go to appsource Marketplace
and open that in a browser but there's
also another link where you have a
selection uh like uh is it Shopify I
think I selected and then you can go in
and to the Online Marketplace just for
that app itself but you can also stay
here in the client and you can open the
cart uh again now for the uh for the
appsource um apps
Shopify um
and again from the card you can go to
the appsource marketplace so you can
install from within here if uh if the
app is free or have a plan if it's a
contact me you actually have to go to
appsource and that's where you use this
link that I highlighted on the page here
or from the list
itself again give us feedback on this as
with any other list Pages you can
actually use analytics or analysis mode
on this and so that's another way that
you can slice and dice and sort of see
by vendors Etc
okay we have a little bit more uh first
of all uh we have uh how many of the
appsource isvs um have heard about the
transact
functionality Yeah so basically if
you're an isv and you want to sell
licenses you need to make money of that
so you have to build your own license
management uh appsource has a
functionality for selling a licenses or
you know for customers purchasing
licenses through the appsource
marketplace we have support bought for
transact ability via credit cards for
about a year now with the use of
entitlements you can go and and find
videos that we made on that but in April
this year we actually added support also
that these apps can be sold through csps
so isvs can decide that they would like
to extend the sale of their apps through
csps with a margin share with the
partners that are then the resellers I'm
not going to talk good I'm not going to
talk about this but you can go read more
on ak. mspc transact there's
also yeah it's not out yet but we
actually Kur yans and myself did a video
on that uh from the launch event and
that should hit Youtube and not too far
a distant uh from
now then uh I think most of you saw the
keynote this morning uh where Vincent
showed the page scripting tool you know
that's a tool to allow customers and
Consultants to easily record user
acceptance test
and replay them right for for ensuring
um a much better experience in uats
basically and we released that as a
preview uh in this release and again
there's a launch event video for this if
you want to see more on this on YouTube
we'll get back to that
later IA talked about the big
Investments we done in
docs um she covered the list uh that the
nice thing about this investment is that
that actually helps in co-pilot
experiences for developers as well so
when we have examples and more coverage
in Ducks copilot in vs code becomes
better at suggesting something in these
areas so that's why we continue or I
will be continuing to investing in docs
also because we've been told by you guys
that they're not good enough right and
especially they need more examples but
this is a first
start then there's even more uh from the
previous release how many of you heard
of the open or explore in vs
code where were you in the
keynote because it was shown in the
keynote so you should all raise the
hands right but if you haven't heard
about you know you might not know it by
name but but maybe by function but um
I'll show I'll show more about that I'll
show a little demo as well but you
really go home and play with this you
you might think you what's in it for me
as a developer it's also a good thing
for Consultants but uh but let's have a
look so you know imagine that want to
investigate how a certain functionality
Works maybe Stephan made
something I wasn't part of that but I
you know I would like to understand that
you know where where is his source code
you know how do I provision that uh
integrate to GitHub whatever pull the
latest I need to talk to him Etc that's
a little bit tedious right but that
could be one scenario that I wanted to
do another scenaria could be that I
would like to troubleshoot why something
is not working again to be able to debug
I need to set up uh vs code Etc and so
um you know that requires a manual work
you have to open vs code you have to
create a project you have to find the
details on the environment you have to
uh you know figure out what is the
session ID that is there if you want to
attach to a user you have to create a
launch configuration for the environment
and figure out the authentication to
that right you have to maybe create an
appj Json and create the symbols Etc
download
them probably a scenario that most of
you every day and it takes time right
and so imagine that you could automate
that so you could increase the developer
productivity more of the Consultants
could do you know even if they don't are
not familiar with Visual Studio code
maybe they still want to see how a field
validation is being done to understand
when the customer calls and there's a
problem with the field you know is that
a bug or is that just because there's
some functionality that needs to be
straightened out um and that could even
be used by by support as well to
troubleshoot this for lower time to
mitigate
and so let's let's have a quick look and
as I said it was actually shown in um
the
keynote let me just see did I select the
wrong one
uh shouldn't it be just PC screen only
we did should we take
duplicate okay oh it worked I'm so so
much going to forget to extend back when
I have to do presentation let's see two
developers to help 1 p.m. no no no by
the way you guys promised to go down so
I had the stage for myself
right yes but then you were would have
been stuck now yeah yeah maybe maybe I'm
stuck now so uh let's go to uh the
customer card right and let's say that
we want to investigate something so um
how many are familiar with the page
inspector Good Very yeah but it's still
only 60% that's another exercise for you
guys when you get home uh control Al F1
to open the PTI inspection for those of
you who never tried it it's a way to get
contextual information about the page
which is open so I have my page here uh
I can see the page uh you know uh page
21 is the one that is being used to
drive this customer card I have a link
here to explore that page in vs code I'm
not going to use that but that's
basically the same scenario that I'm
going to show in a moment but it just
goes to the
page right then you have information
about the table and what object that is
you can actually view table if you don't
know that that's the old run table so
you can see all of the data that is in
the table if you want to understand what
data is beneath there I'm not going to
use that but what I am going to do is
let's say that I have a my phone number
right and so I search for phone I click
the phone and it will sync to where it
is in the UI and I'm blocking it but
it's down in the corner um let's say
that I have a problem with that and I
want to investigate that and so I can
pick in the three dots to explore field
in vs code and this is where as a PM I
of course hope everything
works uh so um and I did not close the
vs before but that should be okay so if
I had VSS open already it will ask if I
want to reuse that or create a new but
I'm going to create a
new idea was actually to not have it
open but never mind so now it's going to
close the project I had it's going to
create a new Mt project it's going to
set up the launch
configuration it's going to connect to
that environment it's going to
authenticate against that it's going to
download the symbols that are present
for that page not all symbols but the
ones that are used for the page and it's
going to ask if you want to do snapshot
debugging which you can do in production
or regular debugging which you can do in
sandbox or no debugging I'll just do
regular debugging for now so that's
going to set up so now it's attached to
that session and I'll go back to my
session
um and I'm going to do edit here and
it's a phone number right but I can do
Tech days
2024 and um that is not going to work so
it's going to uh you know trigger my
debug I got an got an error and so you
see that I landed now on the validate uh
uh functionality here right and I'm in
debug right and I could do a phone
number here we have intelligence and it
says Tech days 2024 and I can you know
browse that and understand that super
super fast to set that up I hope you can
see that um if I was a consultant just
to stop this uh debugging now maybe I
want to understand what this piece of
code is doing I don't know what this
validation code is doing and there we
have our friend in the in the in the
co-pilot chat in vs code I'm going to do
uh an explain of the highlighted
code um
and it's a sharp observation that it
looks to be written in Al so it gives a
introduction I hope you can read this
can you see that all the way up
there right so it kind of tries to
explain here that I'm trying to Loop
through each character and the phone
number and it's checking for letters in
that and it checks for changes in it and
it obviously does something else
right super quick going from the client
going into to understand what are these
things doing on tables of fields that's
what we're supporting right
now yeah uh just to go back to my
presentation yeah you don't you think
you can use that for something you know
I I love it but I'm a
PM so just a quick overview you know I
talked to this you can open the page you
can open the field
one thing I didn't show was that if you
just want to attach to a session you
know to to debug something you can in
the help and support there's an attach
option uh and when you pick that it's
going to do the same right uh you need
to have permission to troubleshoot and
you need to have you know the page
inspector permissions here now um we're
at the end so as usual we have a lot of
resources you can go to yamama LinkedIn
we have the aka. msbc all which is the
landing page for everything so that's a
good starting point uh YouTube as I said
we got YouTube a year ago where we have
as many videos that we record we put
there that's a super good place to go
sometimes we have office hours on
specific topics this is the YouTube
channel
aka. bcbe how many have been to the
YouTube
channel not enough the rest of you go
home and watch this Friday
night um no you can do it another time
yeah and that's the launch event it's
just you know can go there H we have uh
one minute two minutes left so we'll
take one question 30 seconds 30 seconds
we had 30 seconds should we take one
question because we have a t-shirt that
we can give away anybody out for a
question can I uh somehow hide the code
uh of my app uh to prevent to see this
using this yeah oh so that's a good so
in the last demo that I did yeah so um
for good and bad we respect the uh the
IP policy so that means that if you are
an isv and you locked down your source
code we will not show The Source Code
just as usual uh so we we respect that
so that means that this open in vs code
which looks flawlessly now because you
could see the code if the isv or the
owner of the source decided that that
should not be possible it will be
blocked um so I I hope everybody thinks
that's a good idea uh for those of you
who don't Know It uh two years ago we
actually added the ability where you as
an isv dynamically can uh add access or
Grant access to a reseller or any intra
ID so basically if you have an IV
solution and one of your partners have a
problem and they need to troubleshoot
you could grant them access through the
keyb basically add the entry ID for the
partner there and then they will be able
to debug for the amount of time that
that uh inra ID is in the key for that
isvs app look up resource protection
policies yeah re yeah resource exposure
resource protection policies
okay
good thank you for coming you want the
last one
okay yeah so maybe we should no come on
we don't want to steal your time over
time so we are out in the Expo area so
you're more than welcome to come and uh
and ask us questions afterwards
[Applause]
