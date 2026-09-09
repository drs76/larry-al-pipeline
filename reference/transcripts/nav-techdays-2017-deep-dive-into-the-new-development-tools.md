# NAV TechDays 2017: Deep dive into the new development tools

- **Source:** https://www.youtube.com/watch?v=SVw3Hh1B0zo
- **Video ID:** SVw3Hh1B0zo
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 86m06s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

welcome everyone to our session about
new development tools
my name is stanislaw stampin in english
it's just stan
i'm the engineering lead for what we
call internally modern depth
to steam
modern development tools
and we have a lot of content for you
here today we will start with some
basics
this might not all of you might have
seen vs code before so just to get
everybody on the same page
and then we'll move into more advanced
topics
so i'm very happy to see a very full
room
probably even the second room
and i hope you'll enjoy the session
thank you
my name is espen christopherson
i'm the architect on the modern
development team and
yeah it has been a fantastic couple of
years working on this project so we are
so happy to be here and presented
yeah hi everybody so i'm especially
sweater and opposed to stan and
espen i'm not part of the modern dev
team instead i'm an application
developer so i'm kind of on the same
side as you guys are a consumer of this
new awesome technology
so about 14 months ago i first
encountered this new development tool
set
and i've just lost it loved it ever
since
um so a lot has happened since then
actually it's amazing how quickly
this develops
um and so today i'm gonna try to dim a
handful of the latest innovations for
you here on stage
okay
since you have had plenty of time to
read the disclaimer i will immediately
get past that one and start out with a
picture of a good old seaside
and i promise you this will be the last
time that i'll start a presentation with
a picture of seaside because we are
moving everything to vs code
so but a small
walk down memory lane around history i
mean
seaside it's getting old and
while we move the platform all the way
from two-tier to three-tier move the
client from
from web to devices
and the architecture from on-prem to
hosted to cloud we really didn't give a
lot of love to seaside
we added color coding and we were
everyone was yeah yes we got it
10 15 years later than all the other
products
and we added a new editor but
even so when we introduced extensions it
was clear that i mean seaside started to
show at age we couldn't really make csi
do the things what we needed to do in
order to make a good extension
development
experience
so
we
compiled a list and we
god knows we had many years to actually
think about this i'm still sitting with
seaside
so we
created a list of stuff that we actually
wanted to achieve with the new
development experience we wanted it to
be state of the art we want a better
development story for extensions which
was one of the primary drivers
and we of course also wanted to protect
all the investments you have made into
seaside al and nav
and we wanna be we want it to be file
based we want to get out of the database
and allow you to use all standard tools
for doing whatever
things you want to do
and we wanted to be able to
add features more quickly than we have
ever been with c side
we want faster compile time components
since compiler so that we can use it in
a lot of places you want to do that when
you have a compiler
we want to be able to modularize
something that we have never been able
to achieve with seaside
and we want support for cloud deployment
and lastly we actually also would really
like to have a more
broader appeal to modern developers
so
luckily at the same time actually
another group microsoft
started out a project called visual
studio code
and it's a simple but very powerful and
extensible editor they have a really
really great extensibility model that we
have plugged into
and i actually know that some of the
attendees here have already created
their own
extensions into visual studio code
and it has a huge marketplace where a
lot of people have created extensions
themes
and other stuff it's like really it's a
huge community it's open source it's on
github
and even better it's actually free so
just download it
after the session
so
enough about that
now i'll turn
to esper
all right let's get started
there we go
so
basically all you need to do is to start
visual studio code
that was the wrong one this one the blue
one they change color every once in a
while it's a bit confusing
so
then you end up in this empty view
now in order for visual studio code to
understand al you need to install an
extension first
where you can get that where you can get
the latest version will be a part of
later in the demo or in the presentation
but i've heard already installed for
sake of convenience and when you click
on it you can get a few details you can
also get a list of all the new commands
that it adds all the new capabilities
this adds to visual studio code now one
of the most important ones being algo
that will get you started right away so
let's jump into it
by hitting
f1 for instance
you can just type algo
then you have to choose the directory
where you want to put your new extension
in my case i'm going to put in detective
and that should
get you started so what it does now it
asks you where your server is you can
either choose the cloud sandbox
or any other configuration that you
might have now for this demo i have it
locally on my box so i'm going to choose
this configuration
and it generates a launch json for you
which then we'll explain in a minute and
an app.json
and basically the first page extension
for you to get you started
and you up and running
so this might be a lot to take in for
someone who saw vs code for the first
time and the al extension for the first
time
so let's take it step by step
so what you can see here
in the left top corner
you have a list of
all the files that are in your folder
and you might have noticed that we we
don't actually open a project in vs code
we just open a folder so in that case we
just created a new folder and this is a
philosophy behind vs code where it
doesn't operate on project files it
operates on folders
and then each extension can decide what
the folder really means
so in our case
we decided that if a folder contains a
file called app.json it means that this
a language
package extension or project
and this file contains the name of your
extension
the publisher name version and all the
details necessary to publish
to appsource
it doesn't contain a list of files
the list of files is simply
what is in the folder
then we have a couple of other json
files
[Music]
as you can see they are placed under vs
code folder
and that means they are
system files related to vs code
and launch json contains
all the connection details necessary to
connect to the server
so this is what you saw yes per
selecting from the drop down
depending on which option you select
you'll get different content in that
file
and depending on how do you do your
development you should not be adding
this file to source control because you
might be developing as different servers
and then
there is no point in sharing the
connection details
and lastly we have the settings json
file
and here is where you store vs code
specific settings and any settings
specific to a language extension or any
other extensions that you have
installed
this is also a file that you should
you might check it in if you have
settings for the project but it might
also contain
settings specific to your user
so there's a lot of json files
and
if you're not familiar with json
we have a formal
notation for json
and it fits on one page so this is
probably the simplest spec we have
for any open standard
file format
and it's very simple so actually json
contains of dictionaries of
names and values
and it also can have a list so in a
square bracket you see a
basically ordered array and and that's
really it
and on the value type you can have
string type
boolean type
or a nested dictionary so it's a very
simple type very readable
and it's used all over visual studio
code and we also try to leverage as much
as possible
so now back to jasper and we'll continue
all right so let's continue where we
left off
so in the
in the conference guidelines it kind of
states that onstage coding is a really
bad idea so that's what i'm going to try
to do
um
first of all let me give you a little
bit of context and set the stage here so
in our normal nav product
um we already have integrated a
functionality
which is called translations which is
basically
just a place where you can add
translations for
the product description
now this is very very manual and you'll
very quickly hit the wall when you don't
speak a language so but for danish i
could
i could fill it out of course sort
canelo
but then if i wanted to do it in flemish
or something else well then i would
have to go into another product
so as vincent quickly touched upon we
have this
in the keynote we have this lovely
microsoft translator service so i'm
going to try to make a lightweight
implementation
where we actually consume this microsoft
translator the translator text api with
an nav
to translate the description
um so let's get to it
first of all let's create a new folder
that's just good style source
and then we move our source code into
that folder
i'm going to scrap this one so i'm going
to do some snippet coding today in order
not to make too many typos
but first of all
we need a item translation extension
also we should probably rename our file
no that was wrong
that one
so the naming convention is usually that
we
write then the id of the page that we're
extending then we write the idea of the
page of the actual extension and then
the name now the name is not chosen very
wisely here
so but this is just for the sake of this
demo to keep it easy
all right so once we have our
our extension
we can
add the action that we'd like to so in
the action section i'm going to add s
first in the processing section
the translate now action
this is the caption of the action i want
to show it in these application areas
might also choose all
i want it to be promoted
and big obviously i need a nice icon for
it
yeah so that's about it
now we need to hook it some logic for
this to be fun
so i'll add the trigger
the on action trigger
and then here for now for this stage i'm
only adding the description translation
logic is missing onto the
um
so let's try to publish this one
let's see where that takes us
so when i go into translations
i have my lovely little button
which i can hit and it says translation
logic is missing
so that was that
yeah
so what did we just see here we saw
visual studio code for the new al
language extension
we saw an app being deployed to a
dynamic 365 that could be in azure that
could be on-prem
in this case it was on-prem
and a simple page extension
the page extension is one of the new
objects that we added that allows you to
describe a difference to an existing
page add some code
and and in that way augment an an
existing page with new functionality
without disturbing other
changes to that page
so
how does that this all works first of
all vs code is no longer it's not like
csun is not connected to the database
it's connected to
a service
so
what happens when you press ctrl f5
is actually
that we do a
packaging
and and a compile step
inside vs code and the compiler locally
and when we have done that wrapped it in
a nice
package
we send it over
to the service
the service then unpacks it
and compiles it again
now actually creates some binary
artifacts
and then gets stored in the database
and now it's actually ready to be run
from the clients
so for deployment options you saw them
before
happens immediately after yes but he
actually created the go project
you are asked where to
which service should i connect to
and you have two options you have the
microsoft cloud sandbox
which is
a sandbox managed by microsoft
and basically the other one could be
named all other configurations because
if you are connecting to a server that
you are managing
either if you have put it in a cloud on
a in a container or you have it locally
it's the other option
and it's
just also mentioned it's controlled by
the launch.json file
so
what does it give you you cannot see the
database you cannot see all the other
objects you cannot see the customer
table the customer card item whatever
from your extension
because you do not see the database like
seaside did
so to get around that
we added a way of
conveying symbolic information
for our service
to the client
so actually when you see this
this info or warning up here is that
vs code is not aware of the symbols for
your service please download it so it
contacts the
contact the service that you specified
in launch.json and actually pulls down
the symbols
for the
platform
and and
[Music]
the the app that you actually have
specified
puts it down
puts it locally and now the compiler can
certainly
see all the tables all the pages
all the methods that you have created in
your code units
and give you first of all compile
against that but also provide
nice rich intelligence about all this
so
the way it looks right now is that we
have at the lowest level
called the platform level
we have a package called system that one
today contains all the system tables
which is
covered to the platform
so it's it's
all the various tables the user tables
things like that and on top of that we
have the application
and today it's w1 it's us it's
gb whatever
and on top of all that we have the apps
and the apps can depend on the
platform
at the application
but they can also depend on another
module i mean if you as you as i
mentioned before you can module modulize
your code so you can have apps that
depends on other apps or modules
a lot of terms for the same thing
and this is how we see it right now
but imagine
in the future
coming soon
we will have the ability to have many
more modules that you can have reference
i mean today we have some parts of the
application which actually have bigger
affinity to the platform than to the
application think about user management
today it's actually pages that come to
the platform no that comes with the
application but it should belong with a
platform so we want to make this
distinction
and longer term could imagine that we
actually modulized the app
and made it easier to pick i only need
finance
that's the only thing i depend on for my
application
so
this is how we see the future going for
this modulization it will take a while
but
this is the
direction we're heading in
so now let's go back to the
actual code and
recap of what we've seen on the stat on
the screen
so a few words about the syntax
as you can see we tried to keep the
syntax very similar to cal
so as has been mentioned we are trying
to protect your existing investments
make it as easy as possible to migrate
the code to the new development tools so
even though the language is new the
compiler is new
we try to make it very easy to migrate
existing code
so anything you see between begin and
end block
this is pretty much the same as you've
seen in in seaside
there are a few small differences we try
to make it look a little bit more modern
so all the keywords are lowercase
and
method calls are pascal cased instead of
uppercasing everything so this is not
enforced but this is the convention that
we'll be uh
sticking to in our internal code and
we'll be presenting also coding
guidelines externally
then another difference you might notice
is that
now all the variables are actually
visible right above the procedure so
it's very easy to see
what is the list of
variables and
what is your current working set
the procedure declaration pretty much
didn't change we also made a little bit
cosmetic alignments and the spacing will
be different and the formatter that we
ship will be different
formatting is slightly differently than
seaside
so this is code now what about metadata
in seaside
we had a lot of grid-based views
which were used to present the metadata
like properties fields table fields
now that we are fully code based we had
to find some way to present it
in a consistent and readable way
so the metadata was already present in
the txt files which we export the file
from
object from seaside you would get the
txt format but it was never optimized
for readability
but it also contained all the necessary
details so we took that format
and we changed it to be more readable
and human editable
so this is
this is an example of a code unit this
is the simplest object in terms of
metadata
and you can see that on top we have the
object properties
then followed by variables triggers and
methods and this ordering will be
enforced by the compiler and this will
be consistent across all objects so you
will see this in pages tables
reports it's always properties first
then object specific section and then
the code
so for example this is another object
type this is
table
it's hard to see on this screen
so
table has
fields and keys
and this is the table specific section
but it's all structured in the same way
and it all
looks like a list even though it's code
so here are a few other objects
as you can see the same pattern
but we don't follow the same approach
only for objects also for sub-elements
so here you can see a
page field and it also follows the same
pattern that we have properties first
and then the triggers
but okay
you might
still not be convinced seaside had a lot
of designers
so where are my designers now
so seaside had a table designer page
designer
another page designer for actions
they're not really that different but
they were very convenient
so we are aware that
the approach changes now from
very visual approach to pretty much
starting with a blank screen
and it can be pretty scary at the
beginning how do i even get started and
how do
people very familiar with seaside get
started with a blank page so we are
aware of this and we did a lot of
improvements or took advantage of a lot
of features in vs code to make it very
easy to get started
so first of all we made we made sure the
layout resembles a grid layout so it's
still a familiar view it's not that
different
but then
we made sure it's very easy actually to
know what you can type in which context
so we added the structural
keyword intellisense and that means that
in every place in the object so wherever
you put your cursor and press ctrl space
which triggers intellisense
you will always get the list of keywords
that are possible in that context so
that makes it very easy to know
am i in the right place to start writing
variables or this is is this a place for
table keys
this list will always always be filtered
to what is allowed in the given context
so you can do what's called the
programming by intellisense pretty much
keep pressing ctrl space select the
option that fits and then fill out the
data part
another feature is
signature help
in visual studio and c-sharp this is
used only for providing help for methods
but we took advantage of this feature
in vs code to also
help you write the structural things
like fields on tables keys field groups
so you'll get help
on exactly what is expected after typing
the field keyword or after selecting the
field keyword from intellisense
then another thing is that
even though we don't have a property
sheet right now
you will see the full list of properties
also after pressing ctrl space
and that list will be filtered down only
to the properties that haven't been
populated yet so
it will keep shrinking the more
properties you select
and lastly
this is to get you started from a
completely blank
slate we added a lot of snippets
and these snippets can they will create
the completely new object from scratch
and let you just fill out the details
so we have snippets for pages tables
we have snippets also for sub elements
so you can
create the table key just by writing t
key enter and then again fill out the
details
in many cases using intellisense
so now we can there is
another part that we haven't mentioned
is that
even though
most things are done in code there are
some things that
we know require visual designer
so if you've seen in the keynote we have
a
one designer for now that we will demo
and a nicely integrated flow
yes so back to our little extension here
so the microsoft translation service
requires a two letter language code now
unfortunately we only have three letter
language codes so what we need to do is
that we need to extend our table here
or our
page with a two-letter language code
so let's go back to visual studio code
and we create
a table extension
which extends the language table
and then we add
our two letter code field which is a
code two and that basically does it
um so now
if i hit f6 i will launch
let me just try yeah here i will launch
the client in designer mode already
so let's go to the page that we wanted
to add the field to
under translations
and select from full list
and now this is the page so now we go
into more
and we say we want to add a field here
and as you can see now our two letter
code that we just added is present so we
can now drag it into the column where we
would like it to be for instance here
uh and then we can also quickly do the
do the check if it looks all right and
all the other client types that doesn't
pollute our phone client for instance
so when we're done we say stop designing
and we save it
and we go back into visual studio code
and by hitting f7
our page extension shows up
so i'm just going to move it into the
right folder
i'm going to give it the right name
like that and then also we can because
the formatting is not always correct we
can use the autoformatting function
lamp there we go
and that way you can form it back and
forth or transfer the
code back and forth
so a little bit more details on what
happened here so as you saw the designer
is integrated with vs code
but how does it know that this is
this specific set of objects to
download back to the extension
so that happens through
extension context so
right now there might be a lot of
shortcut keys to remember but we deploy
with control f5
and then if you press f6 it also deploys
but now it deploys in the extension
context and opens the designer so we
pass the additional parameter
the extension grid
and that opens the designer link that
specific
package
i'll put it
away
and that opens the designer
in a mode linked to this extension
and it knows that all changes that are
made on the server should be saved
within that exact package
and then we press f7 in vs code and then
again it passes the same parameter to
the server and knows to download only
changes from that extension
so it's good to remember what happens
exactly there because there is a there
is a chance that
you might have changes in both places so
you need to be careful when you press f7
as thus overrides the changes from the
server
we'll have
15 minutes at the end
so
next topic is a bit about developing for
the cloud first of all you're not alone
in the cloud
and even though that sounds comforting
it's not without challenges
in the cloud the resources are shared
which means that one tenant with
a lot of traffic or maybe even fully
written code
can't disturb other tenants
so what we need to make sure that this
is not happening is resource governance
requires us to have a good chance of
actually
monitoring what's what is going on and
and another thing that we need to ensure
in the cloud is that data is not shared
and that's
and and for that we need to be able to
sandbox each tenant so they cannot touch
each other's data and that's
sort of
what is needed
that
unfortunately for the development side
of it requires us to add some
restrictions when you are deploying to a
to a cloud service
so we took away
some of the platform apis
and and we know you have all noticed all
of those
all of you who have tried to work with
vs code notice that for extensions
there's certain things which are not
allowed
for instance the file apis we had to
take them away because
the file system on the service
is a is a place where you can actually
bring down the server so those
we had to take away
we are considering how to introduce them
in another form but for now they are
blocked
and similar there's parts of the
application which is
merely wrapping
dot net interrupt for instance
and some of those
code units are potentially unsafe so we
had to block those as well
and
our first attempt were probably a lot on
the cautious side and
as all of you who had followed us on
github we are taking requests for
opening up for some of those blocks
blocked apis
but for now some of them are blocked and
won't
keep keep being blocked
and the last thing is that we do not
support the net interrupt in the cloud
we will bring back the feature
but not for the cloud
so what did we do to help you because we
know we gave you this
great tool the net interrupt a number of
years ago and you have used it for so
many things
but
luckily there was a huge overlap we
looked in our own code base and noticed
that i mean more than eighty percent of
the usages of the net was actually
coincidentally the same as the eighty
percent most usages when we asked you
so we took that list and say okay
we'll fix those we will add them to the
a language so they become native
to the language
so on that list is
we needed json support we needed xml
and now i'll skip a bit ahead and
mention the http client support we added
because those go hand in hand
in order to call external services
you need a combination of those
the text builder is also something that
many have asked for and and
i shall be the first to admit that
string manipulation within
ale has never been that fast
or that rich
but we added text builder as a native
type
and then we have added list addition
areas in a generic form
not everything can be used as the
generic
part of it
but the basic types everything you can
return from a function can be used and
then we add
some additional string functions
and that that
helps in all the 80 cases
so there's still some length left
and one of the solution is to take those
and move those the pieces of the net
code
into azure functions where they can be
sandboxed and then use the json.xml http
client and combination to actually
invoke the methods over there
and the last option
for now
is that you can submit a pull request to
the opencl library on github
and as long as we can provide it in the
safe form the functionality you need
we will try to build that into the base
app
and allow you to call it
through the
through a base api
so
i'll take a chance and use this one
so for json
this is a small sample of some json i
would like to create
and if we look at the code how it looked
like in c side
and i even abbreviated a bit because
some of the lines were very long
lots of code to create this small sample
if we look at the similar code using new
native methods it's more condensed
and way shorter looks better
similar story
for xml almost the same sample
lots of code that was even worse
to create that
if we look at how it looks now
a lot smaller a lot nicer
so this
clearly some goodness in this
for the text builder
i created a small sample here
try to build up a big string using
the text type
or using big text
or even uh
and using text builder at the end and i
ran that on a on a surface pro
and this one took 25 seconds
slightly faster to use big text i'm not
sure why it's even that slow but not
impressive
with a text builder it took 72
milliseconds
so huge performance gains
and for the text functions
these are basically now
using fluent syntax you can
do text dot contains rather than call a
static method
and there's a list here and there's some
additional ones i won't go through all
of them
and lastly we have the generic types so
dictionaries and lists
just put them up here so you know they
are there and you can find documentation
about it and use them
so
now i'll hand it over to esport again
and we'll
do some demos yes and we're back
um so now let's put these awesome new
types to work um
so as i mentioned the microsoft
translator service is a rest api which
conveniently enough gives us the
opportunity to use the http type
and also that service returns its
results in xml which is also one of the
new types so let me show you how to
actually hook up our little extension
to this
translator service
so first of all we need a new code unit
to hold all our logic
now this code unit i call translation
management
it has a function translate which takes
an input text and then language code
to letter and return something
translated
this token management you can disregard
this is just for
for some
security that we need here
so first of all
let's construct the url
for that we will need or we will use the
text builder that has been just demoed
for sure
so first we take the uri of the
microsoft translator service
and then we append
the input text as parameter one
for this demo the
from language is hard-coded to english
and the language code is whatever we put
into this function
[Music]
so next we should probably go over and
actually hook this function into
into our
call so where before we had the
translation logic is missing
now we can actually go over
and add this code unit
also we need the language because we
need to retrieve the language we need
the item because we need a description
from it
yes i've also added these two variables
and this part we will replace
with the actual call to the translate
function now if i hover over it you can
see again the parameter list that we
need
and we're going to input the item
description and the two letter code so
this should hook it up nicely
so we can go back here
next we actually need to call this url
so for that we need the new http
client
type
also we need the http response message
which is the response we're getting back
and then eventually we will put the
contents of this into a stream
so code wise this looks a little
something like
this
first we need to add a request header
which is the authentication part
next
again if you hover over it you can see
what the what parameters it accepts so
it needs the path where it uses a where
it can get the
call the get request
and then it will get a put a result into
the response
now from this
response we can read the content into
the content in stream
now as i said this content in stream now
contains an xml document so if you want
to get our translation out of that we
need the xml type
we both have the xml document and the
node which contains our information
so let's try to get our
oops
like this
oops sorry about that
so by calling a simple document read
from
we can pass in an in-stream and we'll
convert it into a xml document
out of this xml document we can retrieve
our child notes in this case we know
that i know that the first actually the
first note contains our translation so
we're going to extract the first note
now we have our note and out of that
note we can retrieve the inner text
which actually is the translation itself
so that should actually do it let's try
hitting f5
and we're back to our black moped
so if i now first of all of course i
need to provide the
the two letter language code
so i quickly need to add that if we
actually
let's take dutch belgian i believe the
two letter code for that is nl
so now if we hit translate now
it says vader broomfields
which i think is the right
translation
so yeah that's about that
yeah
and of course even i mean yes we use
snippets so of course it's completely
flawless but but when you are doing
developments sometimes those nasty
little pesky things get in there which
are called box
and um
i know that we we once tried to ship a
version without a debugger and um we are
not going to make that mistake again
so
we have actually created a debugger for
you and
espo will now demonstrate that
yes so personally of course i never use
the debugger because i write bugle's
code but for the rest of you
actually it is very much like debuggers
that you know from other products um so
for the sake of this demo
let me add one more little
little call
so i'm using here the permission manager
code unit which is actually in the base
app
and then
if it is a sandbox configuration i do
not want to waste my precious
translation
thingies so i will exit out of it
so let's go into our action and actually
place a break point here in the very
beginning of our action trigger
and hit f5
so again quickly i need to add
this one language code i cannot set it
up here for the sake
um
for danish sda
okay
and if i now hit translate now
you can see it starts flashing down here
so i can go into my debugger
it has now halted on our first
breakpoint i can go into the debug view
here
and i can see my global variables in all
the fields and whatnot i can add watches
i can see my local variables
and as i single step my way through my
code you can see the value is changing
i can also step into my methods or
procedures by hitting f11
and now actually when i step into a
function that is not part of my
extension
it
did something weird
sorry i just didn't hit the button i
guess
um
so here we are in actually the code unit
from the base app where you can now also
single step your way through
and exit false
and we're back into our extension
so yeah that's a pretty powerful tool in
case you ever write a book
so what have we just seen here so
the debugger uses the same endpoint as
the deployment mechanism so what that
means is that we use http connection
also for debugging
and that's another case where
vs code is such a great platform for us
because we just implemented the
debugging protocol that vs code offers
out of the box so we didn't have to
spend time implementing any of the ui
any of the controls stepping into
stepping through we had to implement the
protocol and make sure the server
returns the right data
and populates all the data structures
and provides the control flow
so what happens with debugging is that
we create a unique debugging context
every time you press f5
that's also a grid
and then on the server we start a
session and place all the breakpoints
within the debugging context and this
communication happens over http
and it establishes a
bi-directional signalr connection
so it's based on web sockets and means
the server can transmit messages back to
our vs code client
and at that set time at the same time we
start the web client with the same
debugging context
and this is how the web client then
knows or the server knows that it has to
connect this particular web client
session with this particular debugging
session so the breakpoints are matched
only in the context of this one session
so with seaside you could only debug one
session for the whole server
and obviously this won't work for cloud
sandboxes where you might have multiple
people debugging at the same time
so this is how we
make sure that it's only debugging
within a unique session
so the benefits of this approach are
that first of all you can do many
debugging sessions on the same server
which we want to enable on the cloud
sandboxes
but it also means is that you can do
remote debugging so you don't have to do
any additional work to actually do
remote debugging against a different
machine it doesn't have to be a local
setup it's all http based
and all based on the same protocol
so you can have all kinds of setup where
you just can connect to your colleagues
box and debug their deployment
so if you remember the symbols and
modules diagram that has been shown
there was
a talk about module dependencies
and we can actually already do that now
so it's technically possible to
break down your app into separate
modules
and this will be a natural step when you
when your app becomes bigger
yes you can build and debug and test a
single module but over time you'll have
some reusable pieces that
also just within your extension you want
to break out
so you can already do this now
by using the dependencies section in up
json
you simply point to another extension so
you have to have the grid of another
extension
and you add it as a dependency to your
final extension
it's also supported in appsource so you
can submit library extensions that are
then reused by many other extensions
and it all works base
it based it works on the same mechanism
as
coding against the base up
each extension generates symbols
so
as soon as you compile your extension it
generates inside the package
a symbol description for everything that
is in this package
that means it can be consumed by other
extensions
it's very similar to dlls
so it's you can treat apps as assemblies
and have other things take dependency on
it
so
one good thing of what you might want to
put in a dependency or in this library
is a control added and as ben will show
an example of that
controller in our client add-ins
as
any of you who have tried to actually
create one of those
knows that it's a three-page description
how to do it
you first write a an interface into
sharp describing the protocol between
the control uh then and and and
see side and you compile it
sign it make sure that seaside can
actually see this assembly so you now
get some
intellisense or
at least some compile validation against
that controller then
and then you can start writing your
javascript code in
another place
and at the end you will have to take all
this and package it together and zip it
and copy it around a bit it's a very
long description so we thought we could
do a bit better
can i get the this one yeah
and um
probably forgot to mention in the
beginning that the
vs code is a cross-platform and we are
working on the cross-platform
implementation of the
el compiler we have it running it's not
shipped
but we are getting very close and close
enough to use it
so
this is a small example where i have a
submarine code here describing a
controller then
this is the new
object type the new syntax for creating
a controller again it's it's a
combination of the interface you used to
create in c sharp
and the manifest that you have to create
along with it
and as you can see we have reused the
mechanism that we have already we have
properties in the beginning describing
the scripts that you need to include
any style sheets that you want to have
include images some other properties
and then you have the ability to
describe
procedures that you can call if you want
to call
something inside javascript
and callbacks which are
the ability for
javascript to call back into ale
so
and the way you use it
is like this
i modify in this case the customer card
and i and after the blocked field a user
control
has to have a name
and then i refer to my
add-in that i just created
and in this case what what it actually
gives you is validation so if i
change the name here it actually
tells me now that the
callback
without the k is not found
in the target
so let me
quickly add this one back
so
as you can see a way better integration
between the
interface and the
and the code you write around it
but together in the same folder
structure here i actually also have my
style sheet
so i can go in here i get all the nice
benefits of
obvious code there's a nice color editor
here it's a bit
create a blue background instead
so
and also here i have an image i would
like to include
and i have some javascript code here
and actually
then interesting thing is that
we have intellisense in here because vs
code knows that this is a javascript
file so it actually provides
intellisense
so
you remember the long list of all the
stuff you need to do on a line to make
it run in a client what i need to do
here is basically
just to do control f5
i'll build it
deploy it
this case to azure
i can log in and here i have my add-in i
just created and you can see the file
color i picked was sort of purplish
and
down here i can call this button that
one will call back into
ale
get some values back
presented
or i can actually also go
here to the actions and i can call the
javascript and that means i get some
values put back here
it's a way nicer experience than one
than the one we had before so i'm pretty
sure you're going to like it
so now for for completeness we want to
mention there's a lot of other embedded
resources that you can include in
extensions v2
and this is also now
easier in the in the new tooling
essentially we support all the same
things that you could do in v1 so you
can include permission sets
you can include translation files
extension table data so you can
pre-package some setup data
configuration data or demo data
and you can have web service definitions
and custom report layouts
so we kept the way to obtain these
things work the same as in v1
so most of most of the
resources are achieved through
powershell
so you connect to your normal
development server
run the powershell commands and the
files you get you can put them in the
same format as you did in v1 just drop
them in the folder in your vs code
project
and they will be automatically
recognized by the compiler and packaged
deployed to the server so you don't have
to do any additional configuration any
additional plumbing just simply drop
these files next to
anywhere in your project folder
and as you can see on the screenshot
here we have
danish localization txt permissions.xml
then web services xml and some service
setup data
but as you can see for cs for
translations it's not a powershell
commandlet it's still a seaside command
so how does that fit into the new
development tools it really doesn't and
the re the only reason we have to use
seaside is that
translations are part of the source code
in the base application
so can we solve that actually in
extensions v2
yes we can so we have new approach to
translations
which is no longer translations are no
longer part of source code
and we also introduced a new syntax in a
language to handle the new captions
so you'll be able to use both
but you won't be able to mix them in the
same object
but this is the new way to use
translations
it's very similar to the previous
approach but you can add more metadata
to it in a nice structured way with
intellisense support
so as you can see caption is just a text
and this will be text
this is text for developers so this is
not translated in any language this is
what
you should put there to understand what
the caption should be about and this is
the text used in development
you can also include a comment
now in a structured way not not as a
curly brace
interjection
and you can add now maximum length
and actually why do we have maximum
length now this is because
the output
that we generate based on this on the
new syntax is an excellent file
which means that
whenever you compile your extension now
we'll generate an xliff file and what is
an xliff file
so xle file is a most commonly used
translation format it's an open standard
it has around we could find at least 50
tools supporting the standard so now we
are getting questions of which tool is
the recommended one by microsoft
there is definitely a lot to choose from
and this approach lets you now decouple
your translations completely from source
code so
you can send the files to translation
vendor you can use open source tooling
to do the translations yourself
and again it works in a very
intuitive simple way that the files get
generated by the compiler and then
automatically recognize and include it
back
so this also solves a problem where
source code was oem encoded and you
couldn't really import translations in
different code
code pages into the same
source code
so yes pronoun will show actually how
easy it is to do these translations
how it works in the
practice
that's actually going to be my shortest
demo because it's really really easy you
open the app.json file
and you add a little parameter in here
which is called
features translation file now if i save
this one and i rebuild my extension
it will create a translation folder with
an excel file in it
this excel file is now the file that we
actually need for translation so in this
case i would like to create for instance
a danish translation file
the source language is english i then
need to specify the
target language in here
i can also of course do that through the
tools as stan mentioned but me being a
hardcore developer i'll just do it right
in here in the xml file
so if that would be denmark it would be
jdk i guess
and then you can see here my my little
extension only has two captions it has
the translate now caption for the button
and it has the two letter code from the
from the table
so now if i wanted to to add a
translation all i would have to do in
here
is to do
target and then the danish translation
i was hit new
and finish it
and now when i compile it this
translation file is included in my
extension and it will then speak danish
and of course as
dan mentioned we could also go in and
use one of the online tools
some of them are free some of them cost
money they some of them want to use you
as an advertisement
thingy whether you want your twitter
account and facebook and whatnot and
so be a little bit cautious when
choosing it
but basically they all are about the
same you open the the xlr file and you
say start translating and you then
get the
the captions and then you add your
translations in here and then you
generate your new excel file with the
translations
so yeah that's what's that
yep
next thing up is mini suites
the menu suite object
is
as it is going away
i mean it was built to support a
navigation structure that i believe was
introduced without look xp or something
back in the 90s so it doesn't really fit
the cloud and new navigation modules
so
we haven't defined exactly how we want
to do this
for web so
for now we are have staged this into
phases
we still
know that there is a need to able to be
able to add and that was one of the
things that the menu suite did you want
to add to search so you can search a
page and find it
and
basically we want to enable that pages
and report can light up in search
so you can find them and the way you do
it is actually a couple of new
properties
that you add to the page or to the
report that you want to show
you want to have shown up in search so
there's a huge
usage category
already there in the corresponding mini
suite item
and then there's the ability to restrict
when it's seen
and then there's an application area all
those are the same properties that you
found in the
[Music]
in the mini suite by doing this
and compile the page
it will show up in search
another new thing thomas mentioned that
as well in the keynote
is the install experience
so we have added a new subtype to code
units called install which gives you two
new
triggers
uninstall app per company and uninstall
app per database
and in there you have and now a number
of options to actually test against
the app version the data version and
test dependencies
and make conditional
behavior based on that
and that is something that jasper now
will demonstrate
yes
so this will be my final demo let's
extend our extension with an installer
and some settings so first of all i will
create a little folder here to
group my things a little
and then i will go ahead and create a
settings table
[Music]
like
this
so my settings table basically only
holds the the url because if previously
either hard coded whatever change it
would make sense to have it in a setup
table right
and then we also
that was wrong
then we also need a page to show this
so this page that i just created has the
translation settings as the source table
it's a card page and it shows our url
now if i compile and launch this
then apparently it did not work right
now let me try again
all right sorry about that not sure
what's going on here
i will just call it something else
apparently there's still a little
leftover from another demo
translation settings too
i'm going to do the same over here
oh i of course also need to update the
reference well actually this would have
been a splendid opportunity for me to
use the renaming functionality
actually if you want to rename variable
you can use the f2 button let me try to
go back and see if it actually still can
do that
you can mark your
variable and then you can do an n f2
and then do the renaming and it will
actually update
all the references well automatically
for you which is quite powerful
so let's see if that does it please
sweet
[Applause]
so right now if i look for
translation settings
there's nothing in there
so let's add those properties that espn
talked about
so by saying that this is an
administration type
and we define the application area
it will now
be visible in our menu suite
translation settings here we are
so but it will be very convenient if we
actually would have some default values
in there so that we don't have to type
the url every time so let's try to
create one of these uh lovely
installation code units
so for that i'll create uh
this code i should probably give it
another id
[Music]
sorry that was the wrong one
so now create a code unit
did i
that onstage coding actually is
challenging
all right here we go um
so
the subtype install actually makes this
code unit an installer code unit
and now we have
certain triggers at our disposal one is
the uninstalled app per company one is
uninstall public database so in this
case i'm going to use per company
because the other table that i want to
populate is a per company table
begin end
and then i would like
to update my settings
so i have the translation settings which
is now called translation settings 2
which are in it i set the url and i
insert the value
and then also i would like to add a few
languages these two ledger language
codes that i don't always have to go and
manually set them so i'm going to add
the
flemish and german in this case
so now in this uninstall app company
trigger we should
we should call these two functions that
we just created
update languages
and update our translation settings
and then last but not least
for completeness we should also
hook in the new settings page
um
yeah that was probably this one so the
translation settings which are again
called translation settings two in this
case
and then instead of actually using the
hard-coded one
we will use oops
a bit too many snippets here
like that so we translate the
translating settings and then we set it
over here so let's try to run this
and see what happens
so now if i go into my
translation settings page
it's pre-populated
and therefore now i would go in and say
i want to create a german translation
because now the two-letter language code
should already have been pre-populated
it says
movehead schwarz
so yeah that completes this little
extension now we have automated
translation capability
back to slides
so
once we have a new compiler what can you
do with it
so there are many things we could do
for example build new objects and this
is exactly what we did
and we built a profile object
so i was advised against using
animations but they like this just too
much so enter profile object
uh
this is a new completely new concept
well now the concept but completely new
object in the al language it doesn't
exist in cio
and it replaces the xml based profile
approach
with a strongly typed object with
intellisense
and all the editor candy that supports
editing in vs code
so what the profile object does is it is
it links the role center and the set of
page customizations
uh
to a given persona to a given role so
you can set it up
uh the benefit of having this in as
profile objects is also that you can add
them to source control and
add it treat treated as code
so as you might notice we have a page
customization object
and before we saw page extension so why
do we have a different object there
the reason is that
there are a couple of reasons so first
reason is that we don't allow any code
any triggers any variables on page
customizations this is purely for
customizing the ui and adjusting
based on the user that views the page
how the page looks like
and you can the nice thing is now this
is code this is no longer configuration
files this is actual part of your
extension
so you install the extension that
contains the profile
and that links all the page
customization objects with that specific
profile and you will only see the
changes to the page
if you actually
connect the user with the specific
profile
and you get all the benefits from the
extension technology meaning that it's
also
a declarative approach intention-based
approach
and you can
you can use
not not right now in the future we'll be
able to use designer to also design the
individual customizations what you can
do today is you can create a page
extension object and just change it to a
page customization link it to a profile
so it's it's based all on the same
underlying technology and makes it very
easy to manage the customizations and
profiles
so you might be thinking that this is
all nice
but
you are working with cal with seaside
and all your code
currently is on on the
old syntax so how are these new things
relevant
and actually it is very relevant because
we provide a set of tools
to easily convert your existing
solutions to the new world
so there are two important things here
one is that
as you have seen there were
even though there were not that many
syntax changes there are some important
syntax changes that only seaside can
make
because they are based actually on on
symbolic information so we added a new
command to thin sql
and you start by exporting your existing
sources so just log into seaside as
usual export your sources
using the new command
and that gives you a
slightly modified export format where we
fix dates where they are no longer
locale specific they are following iso
format
we fix all the quoting
so one important thing to learn in the
new language or in the new flavor of the
language is that
uh
single quotes are string literals and
identifiers always have to be double
quoted even in properties so that was
not visible in seaside it auto-corrected
so
you never had to pay attention to it
and then the next step is you run the
txt to al conversion tool and that tool
it will take all your base objects
so pages tables code units but it will
also handle delta files and actually
generate page extension and table
extension objects so you can start with
customized base and it would generate to
the degree possible page extensions and
table extensions from it and get you as
close to
an extension as possible
so of course what the tool won't do is
it won't
rewrite net integer interrupt code into
the new types this is something you have
to do yourself
and also it won't
change the architecture to event based
so this is also something that has to be
done manually before actually becoming a
full extension
and we have certain recommendations that
that you can do
[Music]
to make sure that as much as much code
as possible is actually automatic
convertible
and then treat the rest manually
[Music]
whenever you need to convert
so essentially you should take all
the.net interrupt code and try to put it
in a separate code unit and only
call it from the remaining code that
means that you can then
auto convert all the all the remaining
code and maintain two copies of the dot
net interrupt code one is in the
v2 syntax using the new types and one in
the old syntax using the dotnet interop
so once you move the code
we also give you a possibility to
upgrade the data
[Music]
so we this is this is a set of
uh
both a new upgrade code unit with with
upgrade triggers
uh but as you can see it actually uses
the old or the v1 nav app apis
so you can load data in your new
extension
from the existing tables v1 tables
and migrate them to the new data sources
and
this this is important also for appstore
so if you have v1 appsource apps you can
use this approach to upgrade the data to
v2 app
on premise if you're migrating tables
on-premise you would have to do
basically manually
transfer the data to the new data
structures
so there's another aspect to this
one is migrating your code to the new
technology
but you might also be thinking that
okay what does it have to do with
on-prem development since this is all
about extensions and apps how is this
relevant
if i'm working only with on-prem
customers
and we have very good news here you
might have heard already but all the
modern devtools are shipping with now
so exactly everything that you see in
the dev preview and the latest updates
will be shipping in enough 2018
and to that effect we started making
installer changes so you'll see a new
new component popping up in this store
which is modern development environment
and that will
this will install the extension on disk
and then you can just install it in vs
code
and the rest will be set up for you
so there are some new configuration
options
of all you the installer will now open
the dev services port
and the on-premise instances
and this is defaulted to false on
production installations but if you
select developer option this will be
defaulted to true
so there's no more configuration
required other than
selecting developer option in this in
the installer
and then you have a set of
this is actually this tab is all the new
settings we've added over the last year
to the server
you might notice a setting here called
allowed extension target level
and this is set to internal and what
does it mean is that
if you're developing for on-prem you're
actually not bound by any limitations
that are applied to the cloud so so you
can use file apis you can use
all the restricted code units
and once dotnet interrupt is there you
can actually also use dotnet interrupt
another setting is
enable loading application symbol
references at server start
that's a quite a long name
but what it means is that
you can use
symbols from seaside
for
v2 development for modern dev
development
and let me show you what what this
enables
so here is
can you see
so i'm in seaside i'm connected to nav
2018 server
and i want to
add a new event to the customer card
because maybe as part of your
refactoring to v2 you need to add a new
event
so here let's see
if i can
subscribe to this event
so here you can also see how
intellisense helps
with discovering events
so these are the currently available
events on page 21 on the page that i
want to
modify in seaside
and right now i don't see
the new event that i'm about to add
but then in seaside simply
go to the object go to the code for the
object
and we add my new event
publisher
then
make a publisher
and then finally the defaults
then i simply save the object and
compile the object
and i go back to vs code
find the command for downloading symbols
and without having
okay
sorry about that i'm running a docker
and it seems like
the dns name
expired
okay seems like i cannot use my domain
credentials here so in this case what
would happen if i could connect to the
server
is that
a new event would show up on this list
and the way it happens is that
first of all you enable the new setting
on the server for loading symbols at
startup
and then you have to run seaside with a
new switch
generate symbol references set to yes
and that means that every time you
compile an object in c site it actually
generates
symbols only for the specific file and
refreshes the the whole package that
that's downloaded from vs code so that
means you can use we can do seamless
side-by-side development between seaside
and vs code
from back to asman yeah
so
it's stability
we are not all
all of us as perfect as jasper so we
make mistakes and
when we do we write we like to write a
test so we make sure that we do not make
them again
and we have of course still
testability both test code unit and page
testability available
for the modern development and you can
now write your tests in other modules
which is a nice separation from your
actual production code
and we are still
working on
improving the actual
execution of tests
so
we would like to give you a more
integrated experience of running tests
so you immediately in the code can run a
test and get feedback on it
and this and this is not the only thing
clearly we are not done even though we
are releasing now we have more stuff we
would like to provide in the future
so
what is next
of course we need to add but net
interrupt we know that
and we want to improve the testability
experience
we would also like to provide you with
even more
editor features
vs code recently
added a a multi-project feature which
you would like to update so you can
actually have
within the same vs code instance have
multiple modules available
so clearly we have a lot of stuff we
still want to
provide you in the future
so
i have a
demo this is the last one
showing off some of the stuff that
we will add in the future
um
and if i can get out of this here
so
what i have here it's a very very small
code unit and i have a calculator code
unit that has the add method
so and if i use f12 just to get into the
add method
i would like to add some more
functionality here what if i would like
to actually add three numbers and have
the same method
so let's throw in a couple of other add
functions in the same code unit
we have a version with
which takes three integers
and we have another one which actually
adds text to text
um let me just use the refile reformat
functionality to get it a nice look
if we go back and first of all you can
see only one of them is actually
referenced using the code lens
if i go back to the use here
now instead say i wanna
wrong place there at 40
and still i have
another version of the
add function that which one which is now
the one i
hit so this is method overloading we
have had that sort of in the platform
functions for a while
but we are now going to support it as
well for user defined functions
and
back to
stan
i think new developer tools was that's a
big undertaking it's we are talking
about
pretty much bringing back the
functionality written over
several years now in a matter of
couple of years two years
but we took this challenge as not only a
technical change we wanted to change
more than just that
and the main thing is we wanted to
change the way we work and the way we
engage the community
so in december last year we as a product
team made an important decision to ship
a preview of developer tools
and even though we knew it's an early
stage and it's not complete we decided
we want to
release it
and get feedback
and really engage with you on an open
forum
and that that turned out to be a great
decision
so thank you all for being part of the
community
we can
with clear conscious say that we had a
new member of the team for this last
year
plus and
we are really overwhelmed by the
great feedback we got from all the
channels since we released the preview
and as you might have seen the the main
forum that we chose is github
we we decided that we want a completely
open
forum where the
not only we can respond to issues open
by you but we saw a lot of cases where
developers are helping each other out
and solving issues as a community
but also providing lots of suggestions
for us so this was a great source of
deciding what is the next most important
feature that we'll work on
so we would definitely like to encourage
you to continue that engagement
and we have a
few places where you can contribute and
be part of shaping the future of modern
dev
the main forum is github
we have
snippets and samples there so we can
contribute
more of your code of samples and
any snippets that you find useful i
think we we've had a couple of
contributions already
uh you can also
suggest new events there as this is as
we see a key part of moving to
extensions is having enough events in
the base application
so this is also a forum where these
events are eventually suggestions are
very quickly processed and added to the
base up on a monthly basis
and then lastly
we we went out with a cl open library
and it started as an initiative to give
away to replace
net
at a faster pace than we can produce new
types in il
and so far this this has been quite
successful we've had
close to
10 different contributions that were
accepted reviewed updated by esper and
included in the base app
and actually now in the latest developer
preview update in november we are
shipping uh all the contributions from
the open library so this is the first
month where these become actually
available and part of the base app
so this is really
a point in time where we have really
open source contributions as part of our
base application
so once again thank you all for
contributing and we hope we'll have even
more
contribution points in the future and
we'll be able to
engage you even better
thank you
[Applause]
