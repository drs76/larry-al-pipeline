# NAV TechDays 2018 - Practical approaches for upgrading your NAV database and moving to extensions

- **Source:** https://www.youtube.com/watch?v=1andDm5gMaU
- **Video ID:** 1andDm5gMaU
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 93m31s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

[Music]
Prince of Eternia and defender of the
secrets of Castle Grayskull this is
Cringer my fearless friend
fabulous secret powers were revealed to
me the day I held aloft my magic sword
and said
[Music]
[Applause]
[Music]
Cringer became the mighty battle cat and
I became he-man the most powerful man in
the universe
welcome being born in 1976 I am a
product of the 1980s it's when I had my
teenage years and if you go to my office
at home my office is full of vintage
LEGO Technic Transformers he-man masks
all of that stuff I love collecting it
and I think great things started in the
1980s and it was also in the 1980s that
my vision got started and it was also in
the 1980s 1990s that we got seaside and
we started hacking away in in Seaside
what I want to do today together with
Mike is we're going to take you through
some of our own experiences the last
year in migrating customers to
extensions the things that worked things
that failed and I want you to change
from Granger into the battle cat and
let's see if we can find your magic
swords and that hopefully after the
session you can say I have the power and
I can move to vs code and I can write
proper clean code so my name is Mark and
I've been doing the vision for as long
as I remember more than 20 years and
actually the last 12 months of my life I
scoped and I said okay I'm not going to
talk about these aren't patterns and
we're going to teach anymore I'm going
to do this I'm going to go to customers
I'm going to go and work with an ISV and
I'm going to make extensions and see how
that actually worked and that works
really nice because a year ago also my
wife said we are pregnant again so you
have to stay home right so Murphy was
nice to me for a change so that's me
now floor is to pike introduce yourself
and then take us through the agenda yes
I will hello my name is pike peg honest
when Mark was 6 years old
I participated in the beta test of the
first version of nav which was not
called nav it wasn't even called
navigator it was called PC plus ever
since that I have destroyed solutions
around the world and now I do have a
customer in future customers and have
teaching what we're going to do here is
we're going to go through a couple of
the examples and I'm going to start out
by how to prepare for the upgrade what I
did last a year was I decided to become
a front runner and front runner is
always hard because you get all the
problems that there is and of course at
some point it gets better and better and
of course it helped with the sea use
that kept coming so it got easier at the
end so first thing that we we saw all
right we need to discuss do we need to
go to it you're on premise that we need
to go to the cloud and there are pros
and cons on both of them so most of our
customers have have already an
on-premise solution and therefore it's
it's usually the customer that says
alright we want to stay on premise
unless there's some some other reasons
for for for going to the cloud then we
need to decide do we want to move all
our extensions or do we want to go
hybrid well there's a lot of discussions
about should it be a hybrid solution or
should we go 100% sometimes it's not
possible to go 100% to extensions so
therefore sometimes you have to go this
way now the dotnet support came in in
see you what for or something like that
and therefore see you at the dotnet in
extension wasn't possible before that
now still not every dotnet that is
possible in in
in extensions but then you can utilize
the azure functions or or yeah use some
of the new functionality that has been
been built into the year to the Al
editor so now we also have to discuss do
we want to go the whole way from the
beginning meaning do we want to take all
our changes and make it into an
extension or do we want to go one-to-one
conversion from from our customized
solution up to a new customized solution
on a business central and then slowly
take the the customizations and move it
into extension one by one now that's not
always possible because I mean there
might be some dependencies you might
whenever you move a table then you also
have to move all the relevant pages and
reports and and all that so but you can
take chumps chunks of the the different
customizations and move them one by one
also one of the issues that we saw is we
didn't have all the localizations
available and we didn't also not have
the the add-ons that we needed now also
when you look at the the cloud solution
we need to see which apps do we have
available and other apps that actually
can substitute some of the
customizations that were made previously
now there's a lot of different parties
involved in a nav solution first of all
we we have our our w1 version then you
have the Microsoft built-in extensions
you might have some localizations that
comes on top of this and they can also
be hybrid the Danish solution right now
is consists of four extensions but there
are still some code directly in
the base application then you have the
ions and do the errands function as a an
extension or is it still in installed in
the base application and then you have
apps on top of that and then the red one
up here is the user customizations
because that's also possible so all of
these things are a part of the solution
that we need to handle later on now when
we prepared for this the first thing
that we need to do was we need to do the
actual conversion and the actual
conversion acting we found out that that
took a lot longer than we expected
normally you just take your your new
development environment you will click
on to the database and it says do you
want to upgrade yeah I want to upgrade
and that's it that it wasn't like that
let me just say that first of all we
need to have a database as a single user
we need to have our license file updated
to 2a
Dynamis 365 BC we couldn't have any
locked objects we could not have objects
not included in the license file so that
means that lazy-eye is vs who has
discontinued some of some objects and
they are still in the object package but
they are not in the in the license no
can do also whatever you have of your
own small testing objects out what we
also found out that if you have
reminiscence of other localizations we
had the situations where we had multiple
countries where we had put localizations
from one to the other that wasn't
possible either so we needed to remove
the localizations that didn't didn't
work and some strange stuff debugger
breakpoints you cannot have any records
in there and you cannot have any records
in the in the server instance table but
the worst part was actually that we
needed to have a developer's license
that covered all of the the
Aran's and the localizations and in in
some cases we did we did have it and in
some cases we didn't we tried to use the
the customer license to to convert but
then we found out that at the end after
half an hour thank you very much then it
came out and said that it needed access
to to modify the GL entry table
yikes so therefore we needed a
developer's license and the next thing
was they we need to go through all the
different steps so we if we have a 2009
then we need to go first to 2013 to do
the first conversion we need to go from
13 to 15 and that was actually a version
wasn't there of nav where you could
convert directly from 2013 r2 as far as
I remember directly up to 2018 but you
cannot do that anymore so this is the
the steps that you need to take now if
this had been a cloud solution the only
way to do it was to go through rapid
start now if any of you have tried to go
to search for rapid start in the in the
cloud solution it says it doesn't it
doesn't exist but it does exist it's
there somewhere but the functions are
there you just need to call the
configuration packages or whatever now
this is not my own experience but one I
my my partners that I were working with
they had a one chair about 2009 database
and they did a test conversion just from
2009 to 2013 and just all the dimension
conversion it took one week great also
another thing when you start doing
extensions you need to have a prefix or
suffix and every partner can apply to
have a prefix or a suffix and it's a
minimum three-letter suffix or prefix
maybe some of you have heard it before
maybe some of you have not heard it
before
and the three-letter they will be
quickly gone so you need to be quite
fast I mean my company name is this big
Anderson consult if I had to prefix
every object with that an object can
maximum be 30 characters and then I
would have 11 characters left to to to
give my object a name
so therefore apply now and in some of
the courses I have in extension in
building extensions some of my delegates
have actually applied during the course
and got the answer during the course I
applied for these until I actually
looked at the middle one I thought no no
no I'm not taking the bacon one no so I
but I got mine so you just need to be
fast if you want a a prefix that is
actually writable and that says
something about your your company now
the big question we have here is a do we
want to make one large extension for
each customer do we want to make
multiple extensions with dependencies
all we could make multiple extensions
without dependencies okay the
dependencies well if we for example have
the Danish version the Danish
localization consists of four extensions
if I want to utilize some of the fields
there are in the for example if I want
to make a and sales invoice with an fi K
number which is something Danish then
you actually need to to make an
extension so therefore you cannot get
around the dependencies but let me just
tell you that these dependencies is
something that you would need to be
really really careful about because that
can make a total chaos as you can see we
have a number of different elements
built into our solution in the future
and
whenever we built a solution an
extension that we make for ourselves
then it will be dependent on maybe the
add-ons that we have and the solution
maybe the localization and all of these
dependencies are going to make a kind of
a spec ad network so that you cannot
move a remove an underlying extension
before you have removed all the other
extensions so I'm not going to say that
I actually melt it down a database
yesterday am I good also when we want to
make a development environment because
we might want to have a testing
environment or development environment
for for our customers well in them in
on-premise it's easy I mean we go and we
make a sequel server back up now we as
we saw in the keynote in the cloud it's
even easier it's just going into the
path to Center and then just click on
the create assign box and then you will
get a exact copy good mark
that's which so one of the companies
that I work for is a company called for
Neff you probably heard of it we've been
a platinum sponsor of a Navy take days
for quite a few years now and with
foreign have we started our journey to
AB source and to extensions in the last
twelve to eighteen months and I just
want to share a couple of things that we
ran into during that process and I also
want to share I want to give you a
couple of gifts right we run into some
problems we solved the problems and I'm
going to share my experiences but we're
also going to share the tools that we
use to to fix it spike said one of the
first things that you need to do before
starting on the whole app source journey
as you have to register for a prefix the
prefix or a suffix is a workaround for
the problem that we still have IDs in
the end objects eventually I've been
told by Microsoft that IDs will go away
but before the IDs go away a lot of
stuff needs to to happen and the only
way that Microsoft can guarantee that if
you run multiple extensions in app
source that they don't crash is that
everybody actually suffixes or prefixes
the the object so not a big surprise we
reserved for which makes our lives a lot
easier
we cheated a little bit because the life
cycle of our product only started two
three years ago so when I started
working on this solution I already knew
a lot of stuff that was going on but we
actually also prefixed everything in
Seaside right you can actually already
do a lot of stuff in Seaside before you
actually think about going into the F
journey in ab source everything is about
simplicity everything has to work
intuitively and basically what a
customer can do in an ab source is they
can create a sandbox based on their life
database and in that sandbox they can
deploy your extension and they can start
playing around with it so as an ISV you
are no longer in charge of installing
the software it's no longer that you
make an appointment of a consultant and
the consultant shows up with a briefcase
in the briefcase he opens it up and he
puts a diskette and it has the fob and
the license file but the customer is
actually going to do that experience
themselves so what we did in NC side is
we added notifications so if you install
the extension or the for the first time
you run the software it actually checks
if the setup table is populated if the
setup table is empty it will give you a
notification said okay well you
installed the foreigners product but you
want to set it up and as soon as you
click yes I mean you can click no you
can actually say I don't want to see it
again but then it starts a wizard and
the wizard it's kind of the wizard used
to be dead right in the classic client
making Wizards was very hard you had to
make this form and you had to move all
of the Expos and the Expos and the stuff
overlapping each other but with the app
source Wizards are now back and wizards
are meant for your customers to be able
to install your extension pretty quickly
you can add those Wizards in Al but you
can also do it in in Seaside another
thing which is mandatory is translations
I'll show you in a minute that if you
create an extension if you go to xox
apps worse you have to create these
excel files somebody here loves Excel
files raise your hand if you love them
there's the door
please leave the room now they solve the
problem they solve a problem that we had
I mean it's not nice to have
translations in your objects but come on
guys give us a better solution than this
and tooltips tooltips are not mandatory
it's not mandatory to have tooltips in
app source but it is highly recommended
and as you saw in the keynote this
morning even the search is optimized to
show a tooltip right if you search for
something and the search finds an action
with a tooltip the search will show the
tooltip and it will make support of your
extension a lot easier if customers
don't have to pick up the phone and call
you or actually throw your extension
away because they don't understand how
to how to use it another thing is
writing tests if you want to go on AB
source you need to have 90% test
coverage it is actually very easy to get
90% test coverage right it's what you do
with the results I mean I can run all my
code and I'll have 100% test coverage so
I'm not really sure how serious this is
if they actually look at the results but
you can already start writing tests in
in suicide and if you create your
extension you can create a second
extension with your tests your second
extension will take a dependency on the
first extension and then if you publish
it you can run the tests using the test
tool page and of course write clean code
right if you started five years ago or
ten years ago with creating your own
code units your own hooks if you've been
nice to a navy in the last five or ten
years then your journey to extensions
will be a lot easier in the second demo
that I'm going to show you is I'm going
to show you an extension with two
thousand objects and it actually works
right
one of the challenges that we have that
we run into is that as an ISV solution
we have to span across multiple versions
with four nav we go back to 2013 2013 r2
and I don't want to create folks for
each Seaside version and extensions for
each business central version so this is
basically what we do we code everything
in business central in Seaside in
business central and then we downgrade
and upgrade right and we have one code
base that we work from I hope this is
big enough I always have a hard time
figuring out here and if we take this
how small you can make the font before
people start complaining that they can't
read it anymore so the development
process looks like this we start in in
Seaside where we have the the report
pack and we have all the tools that we
have this is where we have the test and
in Seaside I use a very simple trick the
good thing about extensions is
extensions force you to think about
decoupling and I'll get back to that in
the second demo but in Seaside you can
also decoupled right and what I do is I
use the version list to decouple I have
different tags in my version list and by
filtering on the version list I know
that I get a subset of objects and that
subset of objects does not have overlap
with anything else so that subset of
objects can be an extension by itself
right that's how I separate my my test
and my ship and some of my development
tools so then we go to Seaside from
Seaside to see signs that might sound a
bit strange but we actually do some
cleaning up before we before we ship and
then my colleague Jakob he wrote a
couple of c-sharp lines of code with
regular expressions and basically what
he did is if we want to deploy our
report back to nav 20 when did
notifications come in was at 17 or 16
right 70 so in 2016 you cannot have
notifications right so what Jakob stool
is doing is if somebody wants to use our
report back in nav 2016 we actually
delete the code units that have the
notification that of course means that
your notifications have to be isolated
right if you raise a notification inside
of an object that you need then you
cannot just automatically remove that
notification if you want to downgrade
right then we go to Business Central and
I'll show you in a minute how we do that
but we basically create an extension
from the seaside objects and we have two
flavors we have a flavor with dotnet
those of you who have experience with
our tool you know that we depend on a
dotnet DLL that resides in the service
to your folder and we decided for now
that if we want to run on Prem we're
going to keep on running on those dll's
in app source we have a service which is
running on on Azure we don't use Azure
functions
Jakob in our team is the guy who is
doing Escher and Jakob found out that if
you want to do GDI manipulation which
you need for PDF crunching that as a
function actually blows up so he is
using Azure service connections or
something like that and that actually
worked worked for us but of course if
you want to run on on Azure you have to
you have to pay if you want to go with
with business central you have to come
up with a new way of of charging your
customers because now we are in the
situation that if a customer runs a big
report then we are actually paying the
bill right because all of the report
crunching goes through the Azure
function or the Azure service whatever
it's called let's call it asha functions
so that's one of the reasons why on Prem
we decided to keep using dotnet but then
we're not quite there yet because if you
want to create an extension you need to
create a couple of additional elements
one of them is you need to have an
installation code unit Microsoft
introduced
a new type of code units which is called
an installation code units and in that
installation code unit we don't do a lot
of stuff we just I think we publish a
web service and we don't do much in the
installation process because our add-on
is designed for simplicity but you also
need to provide an XML file with
permissions and we decided to use the
replace report functionality so we have
a chart of accounts we have a trial
balance we have a customer aging report
and we would actually like if you use
business central and you use for an F
that actually if you click on the trial
balance that actually goes into the into
our report so we basically created a
couple of al files and each time that we
that we create the extension we have to
add those al files into the extension so
how we do how do we do that what is the
what is the magic sort that makes my
life easy right for downgrades there's a
couple of things that you need to be
careful with don't use images in actions
that didn't exist in older versions
sometimes Microsoft comes up with new
images and they didn't use in older
versions put notifications in separate
code units I already talked about that
be careful with properties that did not
exist in older versions like application
area and now we have this new gdpr
property that did not exist in older
versions sometimes microsoft does not
protect you from mistakes so you can
actually read a fob into an old version
and it actually blows up because it
can't find that command that property
but like I said we use an internal tool
it's just a bunch of regular expressions
and if you are an ISV and you want to
know how this works just go to my
colleague Jakob and he is the C sharp
guy in our team and he will tell you
exactly how he is yanking out all of
these properties that didn't work in the
in the old versions going up if you
touch base nav you have to create table
and page Delta files and if n subscribe
a code units I'll get back to
in the next demo because with the four
and a half extension we don't touch base
objects but then you have to run txt to
Al and this is where an AV 2018 is
mandatory you cannot run txt to Al on a
2017 or 2016 database because a
requirement for the text - AL - is that
it requires you to run the export to new
syntax and we use it in the beginning
but we we found it a little bit hard to
work with and also Microsoft introduced
new properties like when they they said
ok we're going to introduce this new
search feature they introduced a new
property that allows you to connect your
page or your report to the search and we
basically found out that if your page or
your report was in an old menu suite you
actually can reuse the properties from
the menu suite in your objects but the
textual tool is not taking care of that
so let me show you how we make that work
how is it with timing timing is good ok
so this is our extension skeleton we
have the app files which are downloaded
from the database of course we have the
net packages where we have the DLL that
we depend on when we run on Prem and for
anything else it's currently empty I
only have my my permission set I can
zoom up that must be the 8 different
spike so look you said you wanted to
have a bigger cinema you also need
bigger screens
[Music]
so here we have the converter we already
had a lot of plumbing in place because
the converter that we have in our
product is capable of converting a
classic report into our own format so we
already had some some tooling available
so basically what we did is we wrapped
our converter around the Microsoft tools
so the text to a l XC file depends on a
text to a l dll file and Michael Neilson
seems to be handy with c-sharp a little
bit so we actually reverse engineered
the whole thing and it said I can do
this and I can do that and you can Det
know so we actually wrapped around the
txt to Al and basically what we can do
is we can take a text export you can go
into Seaside and you can filter on all
of your objects which are modified and
you can simply say file export and just
use the normal export file it doesn't
require export to new syntax so you can
actually take a Navy 2015 database or
2016 database and export all of the
customer objects to to a text file and
then without PowerShell or dos or
whatever you can just convert it into an
extension we have a little flag here the
flag is saying convert Excel files if
you run with extensions on-premise
you don't need Excel files Microsoft is
still supporting the caption and ml and
I think for now until we get proper
tooling around Excel files I think on
Prem with customer specific extensions
caption ml is just easier right extra
files is not easy to work with
it's a solution of separating captions
from code but that's about all it does
so I don't select this option so I'm not
going to generate excel files
I'm just going to run a converter and
hope that the demo gods today are nice
to me and now envious code the objects
should appear so now we have all the
objects in vs code compiler starts
immediately the compiler sees that we
have new files in vs code it gives me a
warning if there is anyone in the room
except gunner no no you can you can do
the contest as well but if there's
anyone in a room that that knows how to
get this warning out you get a t-shirt
this warning is actually warning me that
I could i cannot sort on a flow field
come on that was the best feature of nav
2013 r2 right don't warn me for those
great features and now I can simply
build my extension and I'm good to go
right so I can keep all of my daily work
in Seaside I can serve all my existing
customers and I can upgrade to
extensions without having to do a lot of
work if you like PowerShell yeah okay
cool
then come out I'll reserve your shirt
it's not going to go away and then
you're going to tell me how to disable
this warning
so this tool is free of charge you can
just download it from our website as of
next week it's not there yet
but as of next week you can download it
and play around with it let us know what
you think of it we are open for ideas
the easier we can make it for you
the better and in the next demo I'm
going to show you how I'm going to
create an extension of more than 2000
objects
another challenge that you will probably
run into if you start working with
extensions is that you lose overview I'm
not saying Seaside is perfect but one
thing that Seaside is very nice with is
that seaside acts as an excel sheet for
us to manage our objects right and if
you start working with extensions you
will start feeling that you're losing
control of object IDs and names and
what's going on in your system and if
you deploy an extension Microsoft does
not allow you to see the objects in the
object table but Microsoft's introduced
a new table and in that new table you
can you are actually allowed to see
which objects you have in the database
so Michael actually dusted off his
Seaside skills and Michael created a
page that you can also download from the
website it's the modern object Explorer
and if you download that you get page
number 1000 and if you get me drunk I'll
tell you how to create page number 1000
it's actually not that hard anymore and
Microsoft now gives away licenses to do
that but in the past you had to hack
your way around that but this is page
number 1000 so it actually runs in a
customer license as well all customers
can run page number 1000 and this will
show you an object designer that shows
all the objects from an extension you
can see if the extension is installed
you can see actually the version list
of the extension and it gives you a
little bit of feeling around control of
the objects that you can that you can
use it's also available as an extension
so you have an extension to control
extensions and then it shows up in the
search and from the search you can run
object designer from the web lines
that's cool alright so back to you Mike
yes so well when we go out to our
customers what do we do mostly we sell
hot air don't we we go to them and would
promise him that there we are going to
do and make their life easier and they
are going to get a new system that can
do everything in half the time and at
half the cost something like that isn't
that what sales people usually say now
we are selling changes now I have a lot
of partners that that I go to and make
upgrade courses for them and I can see
that we are not very good at adapting to
changes ourselves so we would like I
heard in the beginning when the Windows
client came for the for the role
tailored version a lot of a consultant
said well we don't like the role tailor
trine could we just please have the
search bar in the classic client then
we'll stay a stay with that and and
that's the problem so we need to somehow
adapt to the changes we need to to to
get one step further the problem is that
maybe people come on a course like mine
and learn how to create extensions and
and everything is fantastic and they
think well this is great and then they
come back to the customer and they are
still running 360 or 370 and then you
have to code in the maybe even in the
native database with their with the
previous development
we see that all the time but there also
some that that embraces the changes and
they're all right we'll do that
and and we want to adapt to all the new
stuff and we want to go to the cloud and
so on fine but when we get out to the
customers they are typically they don't
give their about what system they are
running what which version there right
there the guy at the warehouse well he
has a barcode scanner and he doesn't
care if if the system is called nav or
365 or whatever whenever he scans a
barcode he wanted to do some stuff and
hopefully should do the same stuff and
as it did last week and the same with
everybody else
so therefore when we upgrade to two
extensions and this is not only our
creating two extensions but upgrade
anything we need to make the
functionality to be backwards compatible
we need to make sure that all the new
functionality weeper we implement is
actually a setup where you can add it on
and not where they get some new stuff
and say oh we didn't ask for this could
you please take it away again
so so we need to keep the processes we
need to chew to not piss the users off
and now one of the now I'm not talking
about pissing customers off this is one
of my customers and what the first of
the experiences that that I had and in
this case this was a Danish production
company they have production in multiple
countries they are they have an
on-premise solution and they were
actually having an 2017 a solution so we
decided that all right let's let's take
a look how far can we get right now if
we want to move it first of all to to
2018 the business central had not come
at that time we had a few add-ons that
we
to handle somehow there was some
document output there was some payment
management and some shop floor and the
problem at the customer was that they
had had multiple nav partners previously
and they had had it was kind of
spaghetti code let's just say that so we
said all right there it's an on premise
solution they have we want to start up a
hybrid implementation so what we did was
we had all the objects in a one-to-one
conversion from from the 2017 to 2018
and then we started picking and picking
out small extensions and we made a plan
and that plan is that we were in a year
we have moved everything from the the
customizations in in the in the base
application to extension the problem
with moving our functionality is very
often that we as nav developers we have
been spoiled for so many years why
because first of all we have access to
all the source code maybe we cannot
change it but we have access to all the
source code if somebody changes the
source code we have access to that as
well
so basically what we need to do now is
we need to find out first of all if it's
made as an extension we might have to
think differently we might have to say
make sure that there that we cannot go
into the sales line and make that change
that we made in the old system we had to
make a Don functionality in some way and
that's the one thing also in business
central or in nav 2018 that might be
functionality where you say all right we
can settle with the standard
functionality in the new application
instead of using the functionality that
we had before let's say something like
document output if you have a document
output well as an add-on maybe the new
solution in nav 2018 is enough for that
so another situation we had was
a test conversion it was one of my
customers who said all right we have we
have 10 countries we have a 2013
database that has a lot of add-ons we
have a lot of customizations in it and
you can see this is just the list of the
add-ons that we we have in it we have a
master data replication and we have
intercompany flow and scribes ascribe
CRM integration and so on so on so on so
this is actually a massive task to to
upgrade we have different databases we
have localizations from Denmark Germany
Norway and UK that we need to handle
somehow so our aim was to try to analyze
what is the kind of work that will it'll
take to convert this and the first thing
that that we did was we said alright
let's just convert the database but one
day later we had just converted the
database and that was because some of
the limitations I told before we have a
developer's license that was necessary
because it needed to modify the GL
entries the problem was that in that
database
we had add-ons from German partners that
was not a part of the Danish partners
[Music]
developers isin and so what did we do
all right we needed to go to the sequel
server take all the data out of the and
this was a shop floor module take all
the data out of the shop floor module
delete the objects and then do the
conversion and then then take all the
data back in to to the converted
solution and that was fully possible
that was not a problem so it ended up
taking a whole day just making a
conversion of a database and normally
it's just click yes get on with it
also we had objects that were left in
the solution and
does this little trick that if you if
you go to the DC side and you mark all
objects and you lock them then it will
only lock the objects that you actually
have in your license so therefore you
can just you can just export those but I
mean it's really really tedious that it
has to be that way so problems yeah the
add-ons were not available yet the some
of the add-ons was discontinued so what
shall we do then then we need to find an
alternative solution can we convert from
from the previous solution to the next
solution and so on so on so on this
considered add-ons yes only a few
localizations were at that moment ready
for us so so therefore we decided that
maybe we should just wait until next
year and see what happens here good then
there I have I also try to be a
front-runner in my own company so
therefore I decided to take my own
company and take my own medicine
and see what happens if I operate to the
to 2018 I am going to move as much as I
can to extensions and then I'll try to
make periodic upgrades I was a really
optimistic in the beginning and thinking
all right how about if we upgrade every
month now no good but I started with the
the see you too that was their nap 2018
see you too which was the first version
that didn't delete all my data yeah
thank you
then I moved everything to extensions
but there was something I couldn't move
into extensions and that was all my dog
net so I had to rewrite all my net code
units and put it into one single code
unit rewrite it so it could be called
from the extension and return with the
values to the
extension and and that was more or less
its so it's a nice small solution
there's not a lot of changes as you can
see in the numbers so so my key problems
here that was that of first of all the
RTM to see you one was not usable well
yes that net was not available there was
still some errors in the standard code I
mean when I took the co2 and installed
totally standard strangely enough you
couldn't post a sales order where you
had an item line and a general ledger
line you couldn't had to post them both
so therefore I had to make some some
some very small changes in the standard
code also I found out very quickly that
this was a moving target
I had there maneuvered into a meaning
that whenever I thought now I found out
how this works then and you update him
and now it was not not like that anymore
so also the undocumented functionality
changes in the standard code that was I
was not very lucky and we had is in the
cu3 and cu6 and cu9 that I actually
upgraded to later on in the co 3 I think
the sales line introduced started to
disappear when I when I entered some
data into the line so then you had to
press a5 and it came back again and you
thought oh how did that happen and then
I we started getting another user has
changed the the sales line because well
with the extensions the extension on the
extension on the extension there are so
many parties that are involved in in
this sales line that's sometimes you
will get these errors and that's one of
the things that we need to consider when
we start making extensions as I usually
say we are not alone and anymore I mean
we have the the base triggers and the
base properties but we also
have the the properties and the triggers
of all the extensions that we need to
handle then later on when I try to to
change some of my primary keys that was
no good because you cannot change a
primary key in an extension because that
is a schema change so right now I have a
number of tables in my extension which
is not usable anymore I had to make a
copy of the table and put it into a a
new object in order to get my my new
primary key hopefully this will be a
result at some point but right now it
just looks a little bit strange in my my
database so how did it go well actually
it went well it's a nice small solution
I have a webshop I have some
subscription I have some some but it's
it's fine I have a right now two objects
in the five thousand range actually one
of them has disappeared again because
the query for charts in the cu3 I think
it was you couldn't have a query and use
it in a chart that was fixed later so
that has been disappeared now but my
code unit went on it
yes I need that still now there's been
some changes so therefore I'm going to
change this into using the new HTTP
requests and response and then I'm going
to connect to a API instead of using the
old net functionality I can use the new
functionality in the extensions now
there's also some customization in the
standard objects I don't know if anyone
has tried to make a sales order in the
2018 from cu6 and forward well if you go
to a sales line and you type a deal
account and then you in
the account number then you insert the
description if you have a an ATL account
with that description somewhere else it
will switch to that account without
telling you
yeah that's a nice one
so this actually same in the in the in
the purchase line so I had to fix that
also in my my transfer course that's
also a little so but that's some of the
small yeah
things that you you you see when you
when when you go to the newest version
so one of the tools that I used and as
you can see I have put them on my
website so you can just download them
these are some PowerShell scripts that
I've been using and they now mark has
has provided you with a conversion but
this nice little PowerShell script was
my sword during the conversion because
whenever you need to convert from a a
customized table up to a a extension
table then you need to do a number of
things first of all you need to enable
the side by side development now the
only way to see the new objects is if
you activate one extra setting in your
service tier and you need to start up
your your development environment with a
new parameter that's called general it
generates simple reference equals yes
and then it will whenever you compile
your objects then they will be included
in the symbol file that will be sent to
your extension took me a while to find
out that one because in the beginning
when I downloaded the symbols and then I
just went into to see all my existing I
couldn't see all my existing customized
tables so second thing I've had a
problem with what's the naming that has
been solved since because in the
beginning there was no talk about
prefixes so therefore I didn't pre
takes my table names so instead what I
did was I exported all my my tables were
using this script and then I renamed all
my tables in Seaside to something else
and then I converted my my objects into
Al and imported them into the solution
now during that now you said something
about install code units
I made a quite a big install code unit
then whenever you press install on your
extension then it will fire the install
code unit and that code unit then
carried all my data from my customized
table and there into my extension so so
this was the first of them and it's a
nice little one I know that Waldo is
happy he saw that I was going to to have
a PowerShell script here so that was a
happy Waldo good secondly handling the
apps well in in nav 2018 and in business
central on-premise you cannot upload
your extensions to the cloud or to to
the to the database so therefore you
have to either use your a your Visual
Studio code editor in order to to
publish the extension to the database or
you have to use a PowerShell script so
what I did is this PowerShell script
will show you the whole the whole
lifecycle of an app so in you can see in
the in the top I think I will start out
by publishing it then you install it
afterwards into the tenant yeah you
uninstall this action from my course
that I had yesterday and the strange
thing and that was a little surprise for
me when you install an app first you
publish it then you install it to the
tenant and then you start using it
that's
then you decide man I don't want no good
well I'll take it away again so you
start out by by uninstalling it and then
you go into the database and the
everything is still there the tables are
still there the data is still there
then you unpublish it the data is still
there and the tables are still there so
what do we do then
well if you look at the last line down
here it's not until you run the sync
command with the mode clean that it
actually removes the the the actual
table in the sequel server and that was
a little bit a surprise for me also
because that means that if we don't
watch out in the future we'll have a
hell of a cleaning up to do later on
now the third tool I used was when I
started doing these upgrades from one
CEC you to another one because then I
found out ok it's not enough to upgrade
your your database and your base
application you need also to upgrade all
your your extensions and this is
actually a nice little script where you
can see that the videos here that that
is just redundant but you uninstall the
extension and that is the old version of
the extension then you publish the new
version so that you have both versions
side by side then you have this
synchronization and then you start and
upgrade and the upgrade is the upgrade
code unit in the extension don't confuse
the upgrade code units with the one in
the in sea side because they have to be
executed separately now I I'm not quite
sure what they're going to do in
business central would the upgrade
because I asked a few Microsoft people
yesterday but I didn't get a clear
answer on when they upgrade code units I
actually fired when you upgrade I upload
them to to business central so we'll see
they said that they would run it
directly but I don't know so and this
has to be done for all your extensions
so therefore my script at home is this
long I didn't want to bother you with
the whole script so I just gave you this
tiny little script and it's actually
based on the Danish localization the one
called payment and Reconciliation
formats DK but I'm sure that you can
probably change that into something else
okay then after a while and actually
luckily a week after I had made my
upgrade then the cu3 came around and
there so whenever I I get a new see you
it's the same procedure every time I
uninstalled the whole application and
then I installed the new application
next to it then I connect my my
development environment to my database
upgrade the database load the upgrade
code units run those and that's more or
less it and then of course I take the
new objects there are and put them
directly in and since I don't have any
changes in the standard application
except for a few error Corrections that
I have that I've made there then a one
and a half hour for a whole upgrade from
for both the the base application for
the code for everything one and a half
hour
now the cu9 was a bit a little bit
different because i thought i could jump
directly to that i'm is 365 business
central but that did work so i had to
roll back so therefore it took a little
longer so my issues are here that i need
everything to be backward compatible i
cannot introduce something where i
remove fields in the middle of a in a
table and something about you had set it
to be marked for deletion later on but
that doesn't delete the actual field so
there are the other thing I saw is that
in in the different sea use you get
functionality chains and some of those
are maybe not even wanted one of the the
surprising ones came in the cu6 and that
was the one I told you about with the
with the sales line and well right until
now I can still go into Seaside and I
can still go in and and say alright it
will just remark all this code and then
I'm still running but we won't be able
to do to do that in V in the future so I
would really like to see that the
quality of the see you maybe is a little
bit better or maybe that's a little
harsh said but maybe that that a new
functionality is based on setups instead
of being forced to the users so mr. mark
we are actually doing great on timing it
says here in the notes 30 minutes mark
starts so we have to wait 12 seconds
until I can start okay if you want to
steal code within our community it's
always been good to get inspired by a
code from someone else
yeah if you go to the github repository
of for nav you can go into the beta
repository and here you can download all
of the code that I've created for 4f but
I also got inspired by one of my good
friends Gunnar if you go to Gunnar's
github you actually have to search a
little bit but then you can download his
GL source names extension the story
behind that extension is a little bit
funny because I was in Iceland doing
some consulting for quite a large is V
there who wanted to get his first steps
on extensions and then Gunnar and I came
up with the idea like let's let's see if
we can blog about what it would make
take to get your extension into into AB
source and then I said oh my god I'm not
going to do that it's my free time dude
that's a lot of work but he actually
took the challenge and gunner actually
blogged about how to get into AB source
and I still think that his blog is the
best resource to get inspiration on how
to go to to AB source so the back to the
user cases another story that I want to
tell you is what we did at my largest
customer this customer is so close to me
that it's even strange to call it a
customer I've been working with these
guys for 14 years now and internally at
that company
I am the IT manager and the lead
developer and we have a nav team of four
guys and I have a really close
relationship with with this customer the
existing situation that we have today is
that we are running nav 2017 and 2018
our main database is on 2018 but we
started with no vision three-point 70s
what we went live on 14 years ago and
every time a new version of nav came out
we evaluated and we decided if we wanted
to upgrade or not we have about 80 users
in five different offices in different
countries in in Europe we have a base
and AV installation with nine companies
and we have two add-ons which are CFM D
that we use as a base to code against
and then we have added 1,800 objects
that's a lot
those 1,800 objects did not just show up
like that it's an add-on that I wrote 20
years ago when I started my division
career it's a trucking company and the
add-on is for for managing
transportation companies and slowly but
surely organically over time this
solution grew and I'll show you a couple
of slides of situations that we run into
when we converted
a page to an extension that was
converted from a form to a page right so
it's conversion on conversion on
conversion we also customized some stuff
in a navy and based on a V we I think we
touched about hundred objects and we
have power bi and we have direct sequel
access I'm heavily against hacking into
sequel directly but our CFO came to me
and said yeah we are using ing Bank and
ing
promised me that I have this great tool
where I can analyze the payment of my of
my customers and they are going to
install that and install their tool on
our innovation database so the guy comes
with his briefcase but in the briefcase
there was no fob in the briefcase there
was a sequel statement so I and G is
actually hacking on our database
directly and you just can't say no to
the house bank right and then we have
databases in Romania Lithuania and
Germany they are actually the ones
running on 2017 partially and they are
based Neph they have no modifications
and I'll tell you how we integrated them
because we actually used extensions to
integrate those databases together this
is a fun company to work for my commute
is 22 minutes over countryroads right
and my daily driver is a Land Rover
Defender and I have an American Ford
pickup truck for fun right so I cherish
this customer a lot no traffic
what is our long term goal we basically
want to migrate to a business central
right both financial and operations we
want to have tenants for each country
that we work with we want to have small
extensions with customizations we want
to be always current and of course we
want to be compliant with with GDP are
we have a lot of modules
I'm not going to deeply go into all the
modules but we added a lot of
functionality to an AV and you can
easily divide all of those
things into modules everything is
related to to trucking of course and
wouldn't it be nice if all of those
modules could be their own extensions
right yeah we talked about that we have
about 75 interfaces we heavily rely on
dotnet we have 25 custom net DLL files
the.net was actually the one that
prevented us from completely going to
extensions with an AV 2018 and we have
added those eighteen hundred objects to
to NAV the good news is that we have no
dependency or almost no dependency
whatsoever on base knife right but we do
have a heavy dependency on net so start
small right
don't start big start small so the first
try the first extension that we did is I
upgraded our database and I said this is
going to be the last merge ever after
this upgrade I never have to merge code
again we are running hybrid so that
means that we have small extensions on
top of our sis ID system and all of the
fields that we added to tables are added
to see side because from vs code you can
code against seaside but from Seaside
it's very hard to code against an
extension but we what we did do is we
converted all of our changes to pages to
page extensions right so that was my
first experience with extensions in real
life so I created page Delta files based
with with PowerShell and I converted
those pages to page extensions with with
the txt to L converter that was way
before we had the the four and a half
conversion tool another extension that
all I'll show you in a minute is we have
the financial systems in Romania and
Lithuania and Germany
our operations are run from the
Netherlands and we have to do invoicing
in Romania and what we did is we used
the new API that Microsoft shipped last
year in business central but also in nav
2018 there is a generic API that allows
you to synchronize customers vendors and
create sales invoices and purchase
invoices and what we did is we created
an extension in our 2018 database that
was calling the API in a Romanian
database and then in a romanian database
we added an extension that would do some
juggling with the data that we thought
was necessary after the after the
interface and we also said everything
that we are going to do from today
forward we're going to try to do as an
extension it didn't mean that in the
last 12 months I didn't touch the side
we still had a lot of little projects
that had to be done in in Seaside but we
actually I think we are currently
working with about 12 extensions right
so all the small stuff that we could
make as an extension we we did right so
let's see how that works
I'm going to go live into the customer
system the first thing I wanted to show
you was the option that spike told you
about if you want to zoom it up again do
you think this audience is so you have
to start up the fin sequel deck see with
the general symbol reference set - yes
and this will actually generate if you
make a change to one of the code units
it will actually generate the symbols at
at the backend actually the way that
Microsoft is generating symbols is
pretty smart you know that for each
object that you have in Seaside
Microsoft generates a c-sharp file which
is basically the real code that is
executed and besides the c-sharp file
they also generate behind the scenes a
dot al file and what happens in Visio is
envious code if you download symbols
basically what it
it concatenates all the dot al files
that are stored in your database and it
rubs that into one big al file and it
throws that into your extension as a
simple reference actually the app file
which is the symbol reference is a zip
file you cannot open it with Windows but
if you download 7-zip you can actually
open it and then you'll find a JSON file
which is actually a humongous JSON file
that contains all of the fields tables
pages and function names in your in your
database this is the extension that we
have created to communicate between the
Romanian database and the Dutch database
it uses the new options with the with
with with adjacent objects I think they
are very powerful it makes communicating
with Web Services a lot easier this
extension is not published on github
because it's a real project it's a real
customer so we took a bunch of shortcuts
but if you are interested in this code
don't hesitate and just send me an email
I don't want to publish it on github but
if you want to see it just send me an
email no secrets
then we have the page extensions here
you can also see that I was juggling
around a little bit with how do I call
my objects I've been fighting Microsoft
a little bit over the licensing the
situation we have today is with a
customer license you can run any page
extension number for free but with that
customer license you cannot publish a
page extension unless you have that page
ID in your license with the page
designer right fortunately I also work
for a partner so I have a partner
license that helps me publish the
extension right but
even though the customer has application
builder and even though the customers
runtime allows them to run any page
extension I still couldn't publish this
with whether with a customer customer
license and just to quickly illustrate
to you how small an extension can be we
are a trucking company and we still rely
on phones we do a lot of subcontracting
a lot of subcontractors are small single
truck companies freelancers and we just
call them up and say do you have time
for some Freight tomorrow and all the
planners don't have those numbers in
their head so they had the numbers of
the of the of those subcontractors in in
a phone in the phone system and that
phone system died so we got a new voice
over IP system and with that VoIP system
we could actually create an interface
between nav and that VoIP system and
this is the interface right super
complicated interface right you just
install a tool on the terminal server
and then it works if you ask the guys
what was the best improvement that we
made to Navision in the last 12 months
everybody unanimously say oh that we can
call from the vision right that was just
the best thing you did last year right
but this is how small an extension can
be because now I can go to another
customer and do this extension again and
again and again and I don't have to say
which customer did I do that for and
which objects the way I have to filter
on and filled export it to a fog file
and it's just get get get lumber so
right next step business central that's
the next step we want to do we want to
do 100% extensions on-premises with
dotnet after that we want to go to Azure
functions but let's take small steps at
a time some general tips use an excel
sheet for object numbers we actually
have an excel sheet can show the excel
sheet right here this is just a simple
excel sheet that tells me which
objects are in which extension use the
dates in your versioning this is also a
nice trick but in your object version if
I go to my extension I can actually see
the last date that I've been working on
this extension right even though I have
git integration this is very easy to to
have in your versioning I'm using
PowerShell to to deploy because at the
trucking company we still use the
windows client the windows debugger
still works fine with the windows
debugger you can actually debug
extensions but you have to turn on the
show my code property right by default
Microsoft switches off to show my code
which means that if you publish your
extension the source code is not there
and then if you have to debug a problem
in life or in a yesterday database you
cannot run the debugger so how did we
convert we run the phone half converter
and we exported all of our objects from
Seaside and voila we have an extension
with table extension space extensions
etc after the conversion I went back and
I fixed stupid errors and let me go
through the slides what do you think is
wrong with this code right
this code compiles just fine in Seaside
but after the conversion to an extension
this showed up this is hard to see for
the human eye right there's two case
statements being catched and of course
only the first one will will win and as
long as none of the users are
complaining then this just works what's
wrong with this code the from address
Depot used to be an option field and I
changed it to a boolean that's what you
can do if you code for one customer
right extensions don't like that right
extensions think that this should not
compile even though it works just fine
in in Seaside
format address in extensions you cannot
add functions to this code unit anymore
so instead of adding functions to the
code unit you have to add a function to
the table and in your table you can run
the format address function the same
with dimension management I've added a
couple of functions for for doing funky
stuff with dimensions and I've created
my own dimension management code unit
this is the example that I talked about
with the form two page transformation
tool we have a whole bunch of forms that
we just converted to a page does it look
well yeah it looks well ok let's just go
live right I'm not going to check four
or five 600 pages so after the
conversion we run into code like this
that in the first version of the rotated
lion there was no own after get career
record so the form transformation tool
would actually generate this on off the
get career record and then in in vs code
you would get the the warning right
table extensions and local variables if
you get your table extension it doesn't
necessarily compile if you have a
function in a table extension and that
function depends on a global variable
the global variable is dead right the
global variable doesn't work anymore so
sometimes you have to refactor some code
in order for the for the function to
work again I actually try to fix all of
this in Seaside and then run the
conversion again but in some cases you
end up creating local variables and
global variables with the same name and
then just relying on the fact that
Seaside knows that the local variable is
more important than than the global
variable because that's what table
extensions do as well
when we created the add-on 20 years ago
we didn't have service items so we
created our own types in the sales line
you cannot add types in the sales line
with extensions
even though Microsoft introduced the
enum type they did not implement the
enum in the sales line so you still
cannot add types to the sales line so we
just decided to convert back to service
items right that didn't exist to in the
year
ago and we said okay let's just throw
away our own service items and let's use
Microsoft once we are running short on
time and I want to give you guys an
opportunity to ask questions but I just
want to quickly show you the monolith
extension with 2000 objects right it
works I have an extension with 2000
objects if I start Visual Studio code it
takes about 90 seconds and after 90
seconds it actually figures out that my
extension has 164 warnings if I now
start typing it'll take a while for
Visual Studio code compiler to catch up
with my typing because the compiler has
to constantly look at all of the objects
in my extension if I build it and let's
force the demo gods it should build in
about 30 seconds and then I can deploy
it why am I telling you this
I think it's important still even if
this works to break your extensions up
into smaller modules right seaside had
runtime compiling right in Seaside you
could throw away a function and then at
runtime you would figure out that that
function did not exist any more in
Visual Studio code you can't do it any
more in Visual Studio code if you delete
a function the compiler will immediately
start searching where that function is
used and it's just a lot easier if you
start refactoring your code and work
with smaller extensions make sure that
your smallest extensions that everything
else depends on doesn't change very
often because if you change an extension
that other extensions depend on you have
to uninstall all of your depending
extensions right you don't want to spend
every Sunday hours and hours of doing
PowerShell scripts in order to make that
work
this is proof that it works it's ugly
but it works breaking up your extension
we rely on unveil and 4nf which are now
extensions and our yeah I need to speed
up I know I know I know I know you know
yeah so Keith key take away stay away of
basecoat start cleaning up in Seaside
try to delete objects see what happens
take incremental steps but real steps
and it's just fun to do really I mean it
it works be careful with these guys I
mean we are lucky that we don't touch
base Neff but these are still
application areas that you have to be
careful with what happens if you delete
fixed assets right in Seaside you can
filter on all of the fixed asset objects
and say ok I want to delete them but
then code unit 80 doesn't compile
anymore so I'm not jealous at the guys
of Microsoft who are going to break the
the base up into multiple modules corner
F is not decoupled we still think it was
great and a lot of code that we write is
still not decoupled right before we go
into Q&A I want to give sent you away
with a thought what if we had C side
like this three years ago whatever table
extension and the page extension were an
object type in Seaside my guess would be
that the adoption rate of his stations
would have been higher
because then we could create extensions
in an environment that we are familiar
with and then from the familiar
environment then go to vs code right
questions yeah
I was told to tell you that the black
part is actually the part that you have
to talk into what is about money sweet
what is about the menu switch so the
menu sweet does not exist anymore which
is not necessarily a bad thing the menu
sweet is replaced with a new property
called uses category called usage
category and you cannot make groups in
the in the menu suite anymore you can
only make categories that's why the name
is like that catch
any other questions yeah this is where
the users category goes and basically
what we do with the four nav converter
is we look at the menu suite and if the
report was in a menu suite we
automatically generate this property
right so that makes life easier and this
is only for four pages and it's for
reports that you can put the users
category next one almost what are your
experiences with upgrading an existing
extension but in a live database I am
taking shortcuts right so this is a
one-off customer and these extensions
are not in app stores so if I upgrade an
extension are right sequel scripts
I don't create upgrade code units I
create code units yeah it doesn't work
yeah yeah okay like item data entries
for example does it take a long time
does have everybody to stop working and
every for every extension or just the
ones using that extra life extension so
we don't use item ledger entries we all
track a company we don't have inventory
so that's why we are on the happy path
right I can tell you what does not work
but that would be very boring 90 minutes
I wanted to tell you what works and what
actually was happy but we do have one
table that has 2.3 million rows which is
our shipment table it contains all of
the shipments from the last 14 years and
we added table extensions to those
tables and the performance of adding
those table extensions is the same as
adding it using seaside it's exactly the
same and we didn't see any drawbacks of
the companion tables the companion
tables I mean if I look at our sequel
server the sequel server that we have
spend twice as much time writing as
reading and our service tier has 100
gigs of RAM
and if I look at all of our data is in
we have a 200 gig database and all of
our data is in memory right so our
sequel server is basically eating out of
its nose all the time so catch you can
give it to your from a personal
perspective if you have to choice to
start the snuff 2018 with air or hybrid
or Society what you do first of all if
you there are still scenarios that won't
work right if you are doing heavy
crunching on reservation entries it
doesn't work right but if you have a
scenario where you can run with
extensions I would run with extensions
and maybe do something in in in Seaside
to make it to make it work so like what
what bike basically did is create one
code unit with dotnet because that is
not supported but what we do in the in
in in at the trucking company is with
each request we say ok which route do we
take and extension system preferred
route one of the things that makes me
worried personally is that the promise
that Microsoft did is we will never
break your extensions and the first
freaking release they remove code unit 1
and everything is broken right and now
they are going to say that they're going
to reflect his base nav so that's
something that I'm worried about so what
will happen in the future releases and
how much al do I have to refactor but
will that be better if I stay in Seaside
definitely not all right so we have
another question over here
you really want to happy never mind
upgrading from 2013 to 2018 do we have
to go through 2018 see you four because
only there we had this upgrade code
units in the later there is missing that
you have to go to the I would go to the
latest version of Tara of 2018 the code
unit from the 2018 co 4 thank you I just
wanted to give a shout out to Microsoft
because at the trucking company we are
working with 2018
RTM and we have not implemented a single
cumulative update everything that we did
with extensions was on 2018 RTM right it
was a very stable release form our
perspective
you said you couldn't no comment great
extension because it didn't have the ID
in the customer license but can't you
create a runtime package and then
install it with the customer license yes
you can create a runtime package but
generating the runtime package requires
the partner license it's a catch-22
story it's horrible yeah right I think
we have one minute left so let's just
continue I've been told that the the
tool that Microsoft has created for the
intelligent cloud that's going to be the
future tool that you are going to use to
convert your customers to business
central so if you have an on-prem
database and in business central the
schemas are identical you can use that
tool to convert
an on-prem nav system or an on-prem GP
system okay so I have a question over
here I had in the public okay I have no
idea where you are yeah that's okay I
just talked my question is what is the
best way to create Exley FRA file for
extension you want to take that bike
yeah you can you can do it two ways
either you can have it generator
automatically you can there is a
conversion tool where you can export the
module from a seaside into this export
translation and then there is a
conversion from the text file to the
excel file or you can just use the the
export to new syntax that will include
the extra file automatically if it is a
new extension which is built on al it's
not it's not in here no okay then that's
only hard work okay thanks
what can I say we are on spare time so
thank you for attending and see you home
early next year
[Applause]
