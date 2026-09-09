# NAV TechDays 2019 - Development Methodologies for the future

- **Source:** https://www.youtube.com/watch?v=j4WiWv1BGE4
- **Video ID:** j4WiWv1BGE4
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 87m17s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

let me do a test first did anyone of you
attend one of my previous session at
enough 30 days no the ones that were
clapping dead were the real ones that
actually attended my session so let me
do that test again whoever attended my
session in half day days okay okay not
good no we tried that again clap once
whoever at the end of my session yes
okay so that's a deal
whenever I ask a question you clap once
if you actually agree with whatever I'm
asking if you do not agree you can clap
would be a little bit of a ridiculous
okay um good this morning actually I
need to present myself like Who am I and
this morning somebody met me I said hey
you're Waldo you were renaming my files
I was like I didn't get it at first I
must be honest but at a later point oh
come on this thing is not working I'm
going to remove this I'm going to fix
this for once and forever with my own
tools
I hope look at that so it must have been
this right yes I am that guy that
developed a little bit of a side project
that became downloaded about 130,000
times
and yes I'm renaming your files the
thing can do a little bit more I can see
so lets you can try to find out what it
can do anyway yes that's me I'm a
community guy I develop tools and what I
would like to introduce use this as
introduction to is why this tool is
actually the left one the the air
language extension why that actually
came is I was actually looking for an
internal tool to help my developers to
force some good practices in terms of
filename conventions and all these kinds
of things to make them their life a
little bit easier
yes I like the force stuff I do that but
I would like to do that when it makes
sense so that kind of like makes me I
introduce me as yes I'm responsible for
a development and team eight a de facto
and Belgian partner basically that's
what I like to do another question did
you ever try or actually did you ever
have to explain to your parents what you
do all day did you succeed yeah I have I
have a solution for that I invited my
parents actually here so my parents are
here in this session and now they will
finally know what I do all day anyway
when we drill down a little bit and do
this future the development
methodologies for the future what does
that look like because yes I've been
talking about that a few times on other
occasions I've been actually having the
same title of a session when when I was
at directions but this is going to be
completely different
is anyone did anyone attend that session
at directions okay so you will see new
things here and a directions I basically
did three I prepare three topics this
what I will cover today is one of the
topics you did not choose don't worry
it's going to be interesting I hope but
when you look at develop methodologies
sorry that you didn't see that well it's
actually just a matter of applying some
simple rules applying of or make your
developers think the same way and we
have a few rules that we really would
like to hold onto the don't net rule and
you probably have you might remember
from last year in my session with
vehicle where we talked actually a
little bit about that and we still hold
onto that like for a full year we have
not used one single
don't net interoperability in and one of
our solutions it is perfectly possible
to do whatever you want without all net
and drop really you can don't that next
embracing dependencies somewhat
controversial but dependencies is
something new what I see in the
community quite a lot is that people try
to avoid them I see even design patterns
implementing dependencies without
actually in implementing dependencies
like this sorry the common crazy but
crazy code units to make and come to
avoid actually a compatible dependency
interface code units no embrace them
organize yourself to embrace
dependencies this is actually going to
be one of the main topics of today I'm
strict guidelines absolutely strict you
need you know this the the code and that
was this rules that now come with the
compiler
okay well the warnings are not enough
they should be rarest in my opinion I
mean why is it a warning when it's a
guideline which is good practice it
should be an error any kind of code you
write should comply to all the rules
that is what we apply in our company
testability so important and it was
actually stressed this morning at Unity
keynote as well I agree I fully agree
with that testability is actually the
only tool that you will have they call
it your your insurance Microsoft this
day for the future I totally agree with
that
just imagine you will be writing
software right yeah you will be writing
software but that software now all of a
sudden you will not have in your or
under control when whatever you apply
that software to when it will upgrade so
all of a sudden yours
we'll run on a new version of whatever
software you bye-bye to your customers
on-prem will even expect that at least
my customers on purim also expect to
have an easy upgrade easy and upgrade in
one sentence you know what I mean
testability is something that can be
applied quite easily use the Force Luke
extendable patterns remember testability
right extendable patterns will help you
implement testability if I have time
today I will go into that what I mean
with that but obviously any kind of
coding patterns you need to think a
little bit further I think in the future
as what you what we have been doing with
CIL before it's not just helping the
customer its solution we expect from
Microsoft that their base application is
extendable the amount of complaints that
they have gotten like hey there are just
not enough events we expect more events
there are about 6,000 events now so they
listened I guess our partners or anyone
who wants to extend our software we need
to implement our defense as well you
know don't forget to make your software
as extendable as we expect from the
software that we extend ok and there's
also possible it's perfectly possible
there are some nice simple patterns that
out of the box just make that possible
avoiding breaking changes yeah it will
dive a little bit into that later on I
have a very simple thing about that this
force rule that we have for sync that we
can do well we cannot force in the cloud
so nerve breaking changes is still quite
evil so you need to do whatever you can
to avoid them you cannot break to your
customers the Karstens will not really
appreciate it losing data ok or maybe
your customers will at least mine
customers
don't really appreciate that I have that
firsthand um when it's hard in al it
doesn't belong in Al's just actually a
simple guideline if if it's really hard
to do probably al is it meant to be done
with if that's the sentence at all okay
so that is actually simple rules yes we
have more but we like to apply them to
do yeah simple guidelines to keep the in
the back of our minds well what I would
like to do today is dive a little bit
more into these dependencies things
dependencies things when moving to Al
well when you look at it
moving to Al you have experience in see
al right so all these products that you
have these customers that you have
hopefully you are considering and a good
strategy to move those things too well
okay well I see four possibilities first
of all this is going to be difficult for
me to explain or not explain to say even
migrate to coast code customized al so
nobody finds this ridiculous I okay Mike
ready to customize al means you migrate
see Al as to Al and you end up with
actually a base application that is
customized no extensions at all
still not ridiculous enough okay let me
try again
just think a breathability
how are you going to do that in the old
days all today's C al had powershell
scripts we were able to create Delta's
we were able basically to create a
script that automatically with between a
lot of quotes could turn our CI L
version X to version y in one go
no scripts in al we are back to the
Stone Age interim
of upgradability in that case things
support your consultancies are going to
have to support code customized al
I honestly very passionately do not see
this happening in any efficient way for
me this is the purest dark force and I
know that about 50/50 of people because
I did that poll actually once like hey
what are we going to do or you want me
to code customized or not and about
50/50 people said yeah that's customized
there are reasons probably I don't see
them I only see problems with them if
you are able to organize your around
code customized solutions and code
customized customers fine
you're better organized than me I'm okay
with that we internally will not do that
we have a very simple rules was not on
the list
it's either 100% CL or 100% extensions
next migrate to a monolith extension I
see quite actually not that bad right
it's a gradable because it's an
extension we will be able to maintain
that quite well and very similar rebuild
so we don't migrate to the next ng we
wipe everything again but again a
monolith pretty good but I hope you feel
the disturbance in the force
because yeah you're not really taking
advantage of what we get extra in terms
of extensions we are able to now
implement dependencies so why not
rebuild and in the same time rebuild it
with a set of dependencies that actually
makes sense okay
alright dependencies this has been for
some reason and also an actually I
understand the reason because it ii-i've
been avoiding
different dependencies quite as well
like a few years agos like Oh what is
this extra complexity Oh No let's let's
not do that let's just create one
extension and that's the only one that I
need to to maintain we all know what we
do with the product we all know how big
the product is that big product we put
it in a big extension it's going to be
again big to maintain so maybe we can
make ourselves a little bit easier now
what and why would we do that
well it helps especially it helps
structure more complex deployment
scenarios more more complex products and
I'm hope I'm going to convince you of
that today you can sell them
independently that's not the only reason
I see a lot of that this is the only
reason to those split dependencies but
that's definitely not the only reason we
the next one reason that we actually
quite do a lot is it's viewers the code
a little bit not a little bit actually
quite a lot so I can have a separate
team on a very complicated extension
secure that and its own code base DevOps
whatever how do you do that and let them
develop an understandable interface
layer for other teams to use that
functionality it's like a DLL and many
people think when you say DLL DLL hell
well yeah you can obviously get into a
dependency hell as well you really need
to make sure that you do not exaggerate
with this how do you do extensions I
think we all know it's basically just
defined in the app Jason and we define
whatever extension a is depend depending
on extension B if you do if you would
put that in in schema form what I will
show you is a base application let's
call it the library app where we have
these library functions based stuff
report helpers these kind of things that
helps us do our functionality a little
bit better our functionality could be a
fin of
financials up which would be dependent
from the base up in reality obviously
both apps will depend on the system up
and on the base up indicating that we
actually already have three dependencies
in the fin up and to any base up here
that's it let's look at an example so if
you look at in code quite easy I have
this base and fin up and you can already
see I hope this is clear should I let me
zoom in a little bit because the screen
is a little bit small isn't it yeah so
to pace up and finna we have two ups
here you can already see actually am i
we try to structure it every up as a
desktop oh yeah because we want to do
testability right so the base up did not
have any dependencies or yes actually it
does because it by default has the two
dependencies to the system application
and the base application our fin app
this one introduces next trying
dependency to our pace up now you see
here the way I'm working is pretty good
and it's not pretty code is actually
pretty handy useful how you say it
efficient I actually open all my apps
and a multi route workspace meaning that
I can work on all the apps at the same
time let me quickly maybe there is
someone that doesn't know yet that if
you would for instance delete the the
symbol file from the app that is
dependent from the base up if I would
compile watch this one here would
compile the base up it's automatically
going to put the symbol up there this
was actually quite inconvenient in the
previous version it is actually very
convenient when you build a multitude of
dependencies yeah multi route workspaces
any case
as you see here as well for any kind of
app we should also have a test app
because we are building testability or
at least we are implementing test-driven
development and for every single line of
code of every single pull request or any
change that we do in the product needs
to be accompanied with the test because
if there is no test that shouldn't have
been a change it's a simple rule but
that also in terms of dependencies
obviously implicates that the test app
needs to depend from the actual app that
it's going to test and the reason why we
will not implement in testability or
test code units in the app itself is
because the test framework needs these
dependencies and quite a lot of them the
library assert is apparently a separate
up the any app I still need to figure
out what that exactly is then we have
this system application test library
test liar test test libraries the test
test libraries can only assume that
these are libraries to test the test
libraries and the test run in any case I
need them to be able to write my own
tests because I need that test run and
so on and so on yeah so a big set and me
just having to implement test-driven
development is me having to take care of
all these dependencies just for the
default test framework of a certain
version of a certain business central a
certain business center of business
central so what we have seen here is not
just it actually this simple two-way
dependency is actually this these were
two apps within an analysis dependency
analysis on our monolith of a CIL
product this is actually the the apps
that we are creating at this moment we
are actually in the final stage last few
weeks for our product it's not just two
apps it's
which means 20 apps at minimum yeah so
that brings challenges now before you
think to dive into dependencies and to
figure out what dependencies you want
and how your product will be structured
please
think things through make a plan because
if you do not do that the structure and
the building or the code might be there
but it might just not work at the end
and some things are easy to fix
I think I I can fix these easily and I
all of a sudden of this whoo but
obviously this water thing was not that
easy to fix
hmm so how do you I think things true in
case when I'm moving from Al or to Al
and all I have is that monolith well I
would like to introduce what I call
dependency analysis Wow so creative that
term and dependency analysis is coming
from CL okay well as a start point you
might remember if you join my session
last year with vehicle
besides the ugly piano part I also
talked a little bit on a tool that made
us analyze or at the possibility to
analyze CL in a structured way basically
building it when object model from CL
well we can use that tool because that
object model that's an analysis and
that's actually exactly we want to do we
want to analyze our CL but now we want
to put that in two kinds of dependency
map so we came up with a methodology
that's called development methodology
look at the title and our starting point
was this big monolith the big codebase
our endpoint needed to be some
collection of apps of apps now this
model doc tools
I'm not going to spend too much time in
there is a YouTube video I heard this is
actually building an object model and
makes that available in PowerShell it
just gives us a way to a to actually
loop objects in a structured way what we
had in the old days called CL I think I
can give you some examples as well so I
actually already read the text file so
what I will be doing is reading this
text file this T modified which is
actually only at three or four thousand
objects this is actually our product the
new objects and all the changed ones
okay I built one text file of it
and I just read that as an object model
this is actually what you get from this
model the tools thing the the powershell
which is basically just a wrapper that
uses the default Microsoft Dynamics dot
F dot model the tools thingy
in any case we build an object model and
now we can do stuff how do I know that I
have so many objects it's not four
thousand three thousand you see here I
can basically just query the objects
County objects is three thousand sixteen
objects and you see what I can do right
I can get to coach unit ATL in this case
by simple filter in PowerShell I can get
to the full name of code unit 80 this is
how we try to make a unique name for any
kind of control or object or symbol
let's say in CL we can count two
procedures in encoding 280 332 so you
see what I'm getting at right I can get
to details in a structured way in the
scripting language ok next part would be
to very used I don't have to just know
what my object is and how many
procedures it tests that's not the kind
of analysis I want to do I want to do
dependency analysis
where is this object used because these
used objects of use by objects are the
ones is depending on this one you can
see what I'm getting it and want to see
which object is dependent on which
object and well there is also used by
information service publisher
information obviously when I would
subscribe to an event of another object
I'm also dependent on that object so I
can simply see in this with the use by
statement is also just part of the model
that we create where this 1380 is being
used okay having this information makes
it actually possible to put this in a
flow to do some kind of dependency
analysis i've actually yesterday evening
i figured out that this is a little bit
of a detour i think we could make it
shorter but i will just show you the
florida that we that we did first of all
we created an app an app in business
central because we need something to
store and to work with and to analyze
and to see and to change let me do
whatever so i'm not going to execute
this powershell all the time no i'm
going to execute power cells stored
somewhere and see what i can do so the
first thing and i wanted to do is store
all the objects objects that i had so
these three thousand and sixteen objects
i have a script for that so upload
objects you see that I'm actually just
using sorry if using the model here to
model and I'm looping the model and I'm
actually running this function which is
simply going to invoke a rest call into
that app that I created on business
central actually just uploading my
objects into a table it's nothing more
than that I have that here let's refresh
let's login
so this is just a local docker container
where half that running so all my
objects are here but in the same time
for every single object that I create I
need to give it a meaning I need to give
it an intent why did I create an object
why did I change that object what is
this object why is it here that's the
intent let's call it the module
I learned this this morning that
actually Microsoft also calls it a
module part of your app the reason why
you created an object okay I have here
an example coated on to automate that a
little bit yeah sorry wrong so while
inserting this record by record it's
going to figure out about named number
the follower elsewhere and so so
everything is in the base up is the base
app anything that ends with hook and not
in the in the default range is actually
a hook in our product a hook was
basically something that we created for
one object to be able to minimize
footprint and such that's like that so
these are actually in our product
objects that yes and a lot of meaning
with no meaning at all I mean I did not
create that for a certain module for
certain intent right then I have
function library so you see by applying
some naming conventions I could figure
out already an automated object name if
you see here that's pretty cool actually
what we did in our product and this code
you would be able to change however you
create your product depends a little bit
on your your develop methodology at that
point but we always prefixed our objects
or at least most of the times so
whenever I could find a prefix which was
all uppercase I took that prefix as B
the intent the module that I created at
the object for so the idea was not just
uploading all my objects would also give
it that intent you see here that the
default objects are all days up and if I
would filter on all that is not base up
you will see that I get my function
libraries my hooks vm f which is
validation messaging framework the
report helper supplements journal
template selectively so these are
actually all our modules yes we already
prefix them if you didn't that's not
that's okay then you have a little bit
more work to do because basically what
the idea was is automatically do already
that module or that intent kind of thing
but if not I can always start edit this
is why I wanted to upload this to a
table that I can edit this is why I
upload this to an app a business central
yeah this is actually my step two this
is the table to manually correcting all
these modules very important every
single object that was in that table
needed to have that correct module next
obviously is now we have not only just
three thousand objects we actually have
a limited set of modules so while
importing them I have been actually also
creating a list of modules right it's
easy on insert if module does not exist
create the module so I have now a list
of all my modules and in the background
all the objects that are linked to them
I just imagine per object we can get to
the used by so instead of object used by
we can see modules used by and that was
actually what we wanted to do so that is
going to be our next script here you're
not here
actually quite simple
where we going to watch I get old used
by from the objects I will make that in
a little bit more of an understandable
yeah object like I wanted to have the
source and use by in in a single object
and then I will loop all these objects
that I just created there's actually no
reason if you're happy with that bit
more complicated object model yeah that
just a shortcut not a shortcut to detour
that took just made it a little bit
easier to understand what what links a
time I was getting actually and and then
again I'm just again using that API that
I created extra for uploading all these
links and while I was uploading all
these links that's these ones I
obviously linked an object to an object
now because I have an object to an
object I also have knob module to a
module so in the meantime I was
uploading these on insert I was filling
this table that is actually going to
store all the links of all these modules
yeah and that is actually giving us an
overview of all the dependencies which
is about 797 so yeah I couldn't remove
the logo by the way that's why I'm
moving it down a little bit now we need
to visualize that 797 dependencies it's
not really nice to visualize that I
don't know I know that Camille knows web
graphics or at least graph is there is a
website that you can easily I create
graphical overviews of dependencies
actually this this web graph is and what
you can easily do is if a depends on B
you get a graphical picture of that so
you can already see like I got these
seven hundred and some dependencies so
why
not great a loop and create a dependency
model why did we want to do that because
we need to figure out that we do not
have circular dependencies I don't know
if you know that what our circle of
dependencies this is actually one of the
main pain points in dependency in any
pain dependency model
well the circle dependency is actually
when a is dependent on B but also B is
dependent on a this cannot happen in
business central you cannot do that how
on earth are you going to install your
extension it's not gonna happens
there is no chicken or egg in that place
but this is simple this is less simple a
depends on BB on CC on a I got 797
dependencies not 5 like we have here
right so in our case we had a problem
visualizing this was easy was looping
that table and throwing that error
arrows and you could visualize this and
we had a problem when I first saw this I
was actually quite mad and I was
thinking hmm we will not get there but
when you really closely look at it
actually the problem only is in a few
areas I didn't realize that before but
if you see this link here a lot of
arrows goes in there if you see this
link here a lot of arrows comes in there
the one is you can't read it is each eh
which is the event helper which is
actually just a framework that we
implemented to help us with events you
know the event the fact that events are
not raised in a certain order you can
see so we wanted to help us a little bit
of I now to order stuff right that's a
he vent helper and the other one is the
framework helper just a simple stupid
message to consultants to help them what
this framework could do to them is
actually just a message you can already
see if we would remove these
modules if you would just decide to not
do them that this picture would already
be a lot less complicated another one
here is our function library that is
quite normal that lots of modules uses
the function library that is kind of
like a library module but in any case
yeah I have some work to do I guess now
so we need to figure out how we can
solve these these circular dependencies
so we needed to be able to figure out
for a certain module what is a certain
not what is the circular dependency so
what you see here the entity which is
the number two text again a very stupid
piece of functionality but any case
number the text is dependent from a
framework help is dependant from the
event how but it's dependent from the
database help but it is dependent from
CSF whatever that is is dependent from
function library and that's a point
where I realized like oh this function
library which should be a low-level
module that modules actually also
dependent on another module that
shouldn't be the case right so you can
already see you see actually that your
own design flaws this was our own design
flaw that we implemented and you visual
and you can visualize that so what we
could do during that's not my intention
to do actually I was here so what we
needed to do is starting to change our
design right we needed to figure out
like a K for this entity we need to be
able to change that so first of all this
graphic is actually just a loop that we
do in the module link table we just
create that as a message this is all we
do if we paste it here done we have that
message right it's quite easy
now next do they be able to solve that
yeah we need to delete some stuff
because we realize like this event
however we probably don't need anymore
so let's not implement that anymore so
let's ignore that I didn't want to
delete the module I only want to ignore
that because I need to track the changes
I need to do at this point I need to
create a task in my dev ops to take this
into account in the development of the
new version of our product
okay same for the framework helper I
want to ignore that and that one module
link from the Frank library function
where actually I saw that the func the
opie was used by the this this phone
clip that should not be the case we
should have we should redesign that so
again a new task in dev ops and ignore
this link yeah so now I can again
analyze the entity show my graph is and
now it looks a little bit less
complicated and you see this is actually
what we have been doing for a couple of
days trying to figure out how we can
minimize these circular dependencies all
these red arrows that you saw those were
actually part of the circular dependency
this.d need they need to move okay
so then obviously I'm not going to
create 99 apps I'm still not crazy or
not that crazy so these were modules and
let's now create that a player we need
now a layer that is going to combine all
these modules in certain apps thing is
that is actually quite easy because we
just created a new table here
and in our of not objects in our modules
we are going to just assign them to a
certain app and since we solved all
these circular dependencies we thought
we are there we have our apps well we
were not there because simple reasoning
if you have a non person or non circular
dependency in your modules and you
divide them the wrong way in apps you
again have circle dependencies so
basically the same what we did or now on
a multi layer we needed to do an up
layer we need to solve those three
circles dependencies by either splitting
modules or combining modules in apps and
as a result from this monster of a
monolith but because that's actually a
monolith the design of a monolith we
came up with this analysis and I
strongly believe let me look at the time
I strongly believe this is what thinking
things through means do you agree
okay would you like to - okay every
single thing that you have seen is
available online the app is available
online it's on the github the lowest one
our dependency analysis the scripts are
in there as well to upload yeah all in
that API stuff it's tested is the proof
I'm basically using that exact same
library at this point web graph is links
and also obviously the dll that you need
so I hope this is going to help you a
little bit now this is dependency stuff
coming from CIL let's let's now drive a
little bit into dependency stuff when
there's no CL as actually how do we
think about dependency is moving forward
just imagine you are a partner can you
imagine you want a partner 92% I think
was partners so I think a lot of us can
take in your partners
now we have our own
challenges right we need Phineas time
sheets we need to do support we need to
support hopefully more than one
customers so yeah we have customers
customers we have developers and we have
consultants and we have sales those very
very different types of people correct
we have planning we need to plan
developers plan consumes and I need to
work together hopefully we have support
tools customers that send mail and
automatically stuff happens or stuff
doesn't happen we have work trackers
issue tracker systems and you probably
have that as well there are partners
that do everything in business central
we don't we actually have different
kinds of software to track different
kinds of challenges now just imagine
that you need to invoice your just
imagine you the invoice your customers
hopefully that's not difficult to
imagine then probably stuff needs to
happen in support tool in Montes we have
Montes which I called mantis ad for to
be able to invoice business central need
data from these tools to be able to
invoice the customers just to imagine
you need to do support at that point the
data flow is a little bit different but
the tools are may be the same you need
to do remote support so we need some RDP
information now I talked about that last
year so I'm not going to do that this
year but in a way again some kind of
flow is going on here to get to the
customers to do that support on customer
level just imagine you actually need to
sell your product
just imagine sometimes demo would be
easy
yeah this is central is not making it
easy on us all these monstrosities of
apps these multitude of dependencies how
we're going to build a devil in demo
environment to show our customers what
our hatch can do well maybe we need yet
some more services docker vehicle easy
maybe we need a library of apps
maybe we need docker with apps that's
available from the outside from outside
and let's say cloud yeah that last
picture so this one that's actually the
picture of H a proxy I don't know if you
know that is actually a routing software
so that's kind of like an ability to get
your daugher container outside of your
company meaning I can access it at the
customer side so I can give a demo at
the customer side in that way there is
also a data flow the consultant the
develop it creates apps obviously and
the consultant or the pre-sales need to
be able to get to some kind of container
that he can use to demo their stuff at
the customer side I see this business
central thing as a central thing but I
also see that quite a lot of challenges
would be interesting as well to connect
this is central with so how do you
architect that and I just want to give
you ideas and I'm not going to give you
lines of code or all these kind of
things I just want to give you the idea
on how to think dependencies because I
could perfectly do this I open my
monolith of a monster monster of a
business central internal app and I just
start coding talker here H I proxy their
apps everywhere and you know that's that
I don't think that's a good architecture
so I think you just need to break down
into separate apps just think you need
to be able to read from your issue
tracker developer number one do that he
resisted racket make
then I can read data and I can sync data
from my mantis second same for Ian which
is a planning tool same for topdesk
which is the support s2 same for
business central no not same for this
central basically what I need now to be
able to do is get that data in business
central because I need to be able to
invoice yeah so I might be interested in
some kind of functionality and business
angle which could be yet another app and
what you see here actually is our actual
apps that we created all with its own
functionality so the inside app that I'm
talking about that's the lowest level or
actually the highest level I'm just
going to combine all these
functionalities that I need from the
other ones so the other ones like mantis
even on top desk it's very stupid apps
the only thing that I know is how the
connected mantis or how to connect with
Ian nothing more than that but on top of
that create some kind of layer for other
obstacles against events just imagine I
create a new issue event there was a new
issue so this inside app can connect not
anymore no dependencies yeah yeah so
this inside app he can connect all these
things just imagine that from the moment
I create a time sheet that's conflicting
with planning and it's conflicting me
with whatever customer damn logging in
at that moment it could create alerts
and notifications and mails and whatever
so you have all these tools you have the
implementation or the connection with
all these tools the synchronization with
all these tools the API calls with all
these tools and also the events that you
decide would be interesting on plan on
open RDP connection on whatever and now
you can connect all these data and so on
to make actually quite a simple but very
strong functionality
this is what we did not going to show
you this a little bit to internal I
guess but this is actually just also
insights in the role center of the
insights app that gives us actually an
overview of the customers where we are
able to log into the RDP connection of
the customers where we are able to get
to issues which are automatically linked
to customers and so on there are all
different systems actually it is just a
multitude of connected apps another one
for another example is that this this
demo thing like how can I set up demo
environment for consumes or pre-sales
well software needs to be existing where
people I can actually request such an
environment then I need to solve the
docker layer how can I create a daughter
from business central or at least call a
docker host to create some kind of
environment in some kind of way how can
I get that to the cloud and how can I
add apps into this environment because
doesn't make any sense to just demo
vanilla based in central so I need these
apps as well well you can already see
this is kind of I the same structure you
just solve the lowest layers to dr. part
the rooting part the apps part and then
you connect them with some kind of
connection app interface up call it
however you want
so how would it look in the app well let
me first show you how it looks look in
yep
I have this environment here this is our
actual live internal environment and
what we have for scene is this how doc
part right that is the part I was
talking about here the one that connects
all these bits and pieces we have set up
just a functionality to set up templates
a template could be a certain version of
a docker container
like you see here and a set of apps
right
you see I'm connecting stuff with this
the apps with docker containers and
obviously when I set this up it needs to
be available a be available from the
cloud oh sorry the result would be if I
say here action great request I'm not
going to do that takes a few minutes but
I prepared one I'm just creating this
record basically and it's going to call
the necessary bits and pieces where we
will dive into a little bit in a minute
as a result when the status is ready I
will have a web point I will have
launched up Jason I will have the
ability to restart and all that docker
stuff that it needs to be necessary so
you know what I'm getting at this is
actually just a framework not just to be
able to facilitate for our developers
but also for anyone that needs any kind
of environment at that point how does it
look in code well I'm just going to show
you a few screenshots the doctor part
docker app is actually very easy doctor
comes with an API and all we do is call
that ABI nothing more than that it's
actually the app and business central
just a wrapper about a bunch of API
calls d.h a proxy I don't know how that
works I'm not an infrastructure guy but
the H a proxy has got an API as well so
every single thing every single comment
that we need to do for setting up our
docker container routing that to the
cloud it's actually just a bunch of API
calls yet again this time not to dr.
obviously but to our our route is H a
proxy to combine all that I just have a
few screenshots here hot dog is all
obviously going to use the docker part
to create a container or to pull the
image in this case
Update license you see docker container
upload file but the file is not a docker
thing the file is actually something
that is being managed by the hard rock
part hot dog comes from haha proxy and
docker and it's more funny in Belgium
than anyone else because of the hard
thing anyway
then we have the start container the the
setup hf proxy where we basically set up
our container for for the cloud let's
say and you're just an an example of how
to set up the docker container itself
okay this is just an example that this
is a docker API and docker API also lets
you execute power shell in the docker
container so by embedded code very embed
power shell and even sequel into an API
call we can simply actually just do
whatever you want in the docker
container so this is just an example on
how it would take backup of the database
or restore backups obviously also
possible this app catalog yet another
very simple stupid app that we created
with the table of apps nothing more than
that so at some point this catalog here
is just a table with blobs more than one
table with blobs because we store every
single version that we create of every
single app in our business central and
in that way we can basically just take
it and drop it in any kind of docker
container that we needed so again we
want to facilitate anyone choosing to
set up a docker container how they would
like to do that so we just created a new
possibility in our DevOps where we can
call this API from our environment ok
so this is where we end up with now you
already saw me using this web graphic
stuff well graph is is actually let's
call it the language modeling kind of
thing do to create graph and we've also
found actually an API for that so we
were thinking like a cave now since we
have all these apps in our system maybe
we can draw this dependency model as
well you can already guess that we are
not there yet but
oh you dare yet we can draw it I mean
this is just calling a simple API call
but now we want to combine that with if
we would draw off if we would set up a
dependency that was not intended that we
can alert create events and in any case
act upon that from wherever maybe send a
mail notification whatever we want to do
from this environment this is actually
yet another app that we created and I
prepared one single picture let's create
it again
oh not create show so there is actually
an up-to-date picture of the apps that
we are creating you saw the analysis
previously this is actually very at
where we are at today okay and just a
bunch of code so all these is actually
just a bunch of connect apps apps where
we connect to a certain API of a certain
piece of software not all of them the
alause part is actually yeah we should
have called it differently actually it's
just an app catalog where we can push
apps to yeah so that does not have this
dependency you see already fan I already
said like hey yeah you do not want
dependencies in these up because these
are low level of they need and don't
need appendices there's one dependency
that I really like and that is this
best app arrest app over simplifies your
life actually that much if if I give a
course it's for me
difficult to explain how to call a web
service cop because I have been spoiled
with a very simple app that made my rest
calls actually very easy to do but yeah
this is just yet another indication on
how you could use the rest app to call
an API call but tomorrow there is a
session on connect apps some point by
these two actually gentleman and we will
dive into API calls quite heavily so I
don't want to bore you today with that
so remember all what you have seen is
without a single single table net
interoperability call it's all just
service based very simple al code that
everyone can do ok don't forget please
don't forget that in the future
on-premises will follow the cloud rules
this is not a statement by me this is
named by Microsoft whatever you do with
dotnet interpret bility it will not be
supported at a certain point in time
even on Prem that's what I get out of it
some other more hands-on development
methodologies I have no idea when I
started an hour in the session ok so
more so more and more hands-on develop
methodologies I think these are really
important the question of all times
where do I put business logic I always
tell my developers if you want to choose
where to put business logic please start
your own company you don't find it funny
ok they always laugh if I say that the
thing is I'm not joking at that point
but I do try to convince them of a good
methodology on just not having to think
on where to put business logic remember
what I said you need always not
just implement your business logic but
also think about the fact that it needs
to be a lot more than just work
yeah so I actually make it very easy if
you think about where to put business
logic put it in a medal coat yet yeah
and this is actually a pattern that that
I didn't come up with that but I'm very
grateful of Gary winter who came up with
that and we have been implementing this
that insanely hard and it has done us
really well so what is it code unit well
it's a code you know the type of pattern
that is going to facilitate much more
than just business logic it will
facilitate the fact that I will be able
to decouple at any point by any app
think extensibility and extensibility
also means handle disable decouple yeah
this far handle or pattern you you
probably all know well that is actually
decoupling that is you deciding that a
certain piece of code should not be
executed
yeah extendable you encapsulation
obviously by deciding that every single
method is one coating that you
encapsulate the responsibility of that
piece of business logic
okay now that single code unit can be
and should always be called from it's
what we call class not really class this
is not I know
but either from let's call it the class
code units or it's table I like the
calls from a table I like to be able to
say sales Heather dot post instead of
crazy code like code unit don't run
sales post comma wreck come on that's
crazy no sales added up post that's a
matter that's a method call yeah
obviously that's where we call our
business logic from you see the errors
not going from I think the laser did
work
the arrows are not going from a base to
the method code or the code unit of the
medical unit or any kind of other place
where you want to call your method no
they always call your method from the
implementation from the table or the
class code it depends a little bit on
how you structure it okay thinking the
couple ability thinking extensibility
I'm talking here one app obviously one
coaching can only be in one app but if
we have another app another extension
they would have that class coaching at
that table to code against right this is
how they can call their method and if it
is necessary that they would be couple
or create their own implementation of
the business logic they would be able to
subscribe to the method decouple the
method let me show you in practice
somewhere yeah so I created this simple
code unit the simplest simple Scott
unist that you probably will never
create it is a block customer method but
this employee implements that design
better so without even thinking don't
think when you code that's probably when
you mess up yeah so without even
thinking I create a file I start coding
either a method without UI or a method
with you why I give it an ID I give it a
name block customer whatever block
customer cursed customer done this is a
compatible code unit that already
implemented all the things the
extensibility the critical ability why
because I have my own before on after
event at any point and this on before
event has got a hand with pattern
so anyone that calls
this event subscribes to this event and
sets handler to true this cogent will
not execute anymore which is exactly
what I want if I would like to tick
couple a code unit and maybe implement
my own version of this business logic if
for me blocking a customer is something
different than the intentional or the
initial Cochin is a version of the code
unit I can at least implement my own
version at the customer side on top of
our own product or maybe when I'm
implementing an IV product and I
implemented this kind of yeah if you
look at our product which is somewhere
you will see you see with this a little
bit bigger you have this is just base up
one of these ten ups by the way if I
would search format we have quite a lot
of medical units and all of them
implement the own before on after event
this is without you why you would be
able to implement with UI as well oh
where is that here so this one was with
Yahoo UI and that basically just means
if you would like to confirm like are
you sure you want to block the customer
and all in the end
hey you successfully blocked the
customer usually I do not wrap my
function or my methods in that so in
eighteen ninety percent of the time we
simply use this without you why another
thing is one app one repository yet
another rule that we try to implement
there are opinions about this and I'm
sure you do not share or you might not
share this opinion but what we try to do
is let every app dependencies or nor
dependencies let every app be as
dependent as at all possible which would
mean if in this case let me just show
you in DevOps I have this
bass and fill up that we thought but an
hour ago I think yeah that they are
independent but dependent not clear
right anyway if I would change a
breaking change in the base up that is
not the problem of the base up that's
kind of like what I would try to say
that's the problem of the fin up
obviously the thing up needs to know
right the finna needs to all to know
that there is now a breaking change in
the base up but it's not the base ups
problem I need to be able to deploy my
base up to any customer that this does
not have the fin up yeah that is again
this is an opinion if you would like to
have all your app synchronized and at
all times being compatible let's say
okay then you can implement DevOps that
way as well how would I set up is the
built of the base is basically just as
independent as can all be but if I have
a successful build of the base up the
fin up has a trigger in there very
simple that on the successful build of
the base up to build completion of the
page up it starts building the fin up
yeah so from the moment I have a new
change in my base up the fin up is going
to know a few minutes later like look
there is a problem okay you might want
to revise your code and that is how I
like to think of the setting up
dependencies on DevOps level test-driven
development
yeah quite important we implement very
simply like if there is no test in our
Pro request in DevOps we I'm not even
going to look at your code we do manual
code review every single pull request is
being reviewed not only by me locally by
a team of developers and one of the
simple things that we look at is test
another thing is like no settings should
should be changed like AB Jason should
be not change the settings or Goten
shouldn't be unchanged test-driven
development is actually quite easy look
in the pool request if there are tests
and if there are tests okay you can look
further if there are no tests don't look
at it but that also means to set it up
what we actually do in this case you
don't see it really well because I am I
opened actually four workspaces for
every app is a single workspace but the
base app is one repository yeah and the
fin up is another repository you could
see it here where I have actually the
base repository and the fin repository
there are actually no changes in the fin
one but there is one change the method
code unit I just created in the base
repository and I think that's a good way
to set that up and Bev ops it looks a
little bit like this where you have here
the fin up the base app looks very
similar where you always have two apps
that obviously belong to each other
I need my tests in the same repository
because those needs to be updated
together with a bit of source code I
update as well yeah and also for
test-driven development it's actually
quite easy to do just tell them that I
need to do it do know that the tests
that come with the I can do it with this
the tests that come with the app that's
what we call in our case unit tests it's
not enough to have just unit tests I
hope you agree with that it's the
combination of your apps that's going to
make sure that they are combined the
right way that I will will work together
the right way so that is what we have or
implement also in our company and let me
try to show you that this is what I see
as unit tests I test to unit which means
without any
influence of other apps if I would
execute the test ability that the
running of the tests and dr. in the in
the in the release of sorry in the bill
pipeline no other apps are there only my
app and these are the unit tests of my
app as a second one I need integration
test as well I need to be able to make
sure that the integration works as well
and I didn't open that so what we did or
doing actually is not here but here we
have a repository test and this is going
to be our integration test so this
obviously is going to depend on all
single apps that we all the apps that we
that we have yeah and are going to run
the integration now what I think needs
to be done not only I'm going to run my
defined integration test whatever that
means I'm also going to run the unit
tests I need to know which unit tests
will fail if I combine them with other
apps and if there are unit tests that
fail then I would like to know about
them and make them work in this
situation that I should work just
imagine a simple thing if I would in a
posting process add a message in the fin
app the base app is not having that
message in a posting process a simple
test that tests the posting process does
not expect the message the fin app will
have a message testing the base test
together with the fin app will fail just
because of the message yeah to make it
work is adding a simple handler but I
cannot do that from a dependent
extension so what I would do is copy the
unit test and make it work in my
integration test app yeah the
integration test that's something we run
every day the unit test is run a speed
runs every single build
yeah we saw that very good explanation
on anything that has to do with
automated testing is this book I
literally are not joking literally the
rate is in 12 hours one day filled
non-stop I'll read this I loved it and I
bought five other copies we have more
available but they don't read all these
books at the same time but yeah this
mandatory for me this is mandatory
knowledge and there was not one letter
too much in this book in my opinion
breaking changes I actually already
mentioned that in a way there is no
force when you need it that's the simple
truth I actually had this comment on
Twitter which which I actually loved
when I was asking like what is your main
development methodology to look for well
I mean Microsoft did implement a force
for sync but that only works on Prem and
that only works if you first uninstall
apps in the deployment model you don't
want to start uninstalling apps it needs
to be just an online kind of thing
uninstalling for me it's not done yeah
and at this point still how the status
is today breaking changes is not done
yeah so again DevOps can help you to
make sure simple tip there is make sure
you first publish in your build pipeline
first publish the previous version of
your app then compile the next version
of your app and publish it that one and
then you make sure you will never do
breaking changes okay it's just one or
two and extra entries in the build
pipeline number series they're almost at
the end don't worry stay there yeah
still something you need to take into
account I'm supposed you develop in team
right yeah
that will that means multiple developers
in one project yeah come on if two
developers create a table they will have
the same number if you use the automatic
number so it's not gonna work you need
to manage number theory what we did
simply yet create another business
central app with simple table that per
project that developers can not create a
number but reserve a number for the
module they are working on we only plan
one developer on one module so that
works pretty well yeah another thing for
number series never use numbers in code
please never use numbers in code I know
a lot of dinosaur developers are out
there knowing all the numbers of all
tables and pages and all that don't use
that you can you should not never very
bad practice so instead of doing that
use the actual name of the object okay
that's also something I look at in code
review if I see an ID anywhere in code I
I'm not reading further I'm declining
but even saying anything anymore I get
really pissed off about that sorry
translations last but not least I hear a
lot of disturbance in the force about
that thing is translations is now actual
it does now actually make sense in
extension um but don't try to do it the
way you're used to do it developers know
languages but it's programming language
we are no translators we never have been
we needed to be because how see site was
working and now finally we have an
industry standard on how translation is
done let's do it like that yeah and what
I would suggest don't translate every
single PO request don't do that it's not
feasible it's it it creates a lot of
inefficiencies translate at the end of
the development cycle every week every
month whatever
your release cycle is translate at the
end of it in bulk in batch and as
automatic as adult possible we are using
lifecycle services pretty good pretty
well I have seen other people using
other services you find your own
services whatever works for you but do
not do every single PO request that's
just as inefficient as anyone could be I
don't think that would be a good
development methodology okay so to end I
think I covered a few of these in time
so if you have any questions I'm all
ears I do have three t-shirts not more
and I hit a little present in them that
I won't say I will just not throw these
my okay I'm going to throw this and VA
go almost killed someone with it few
years ago
oh wait wait
do you in yarn development he is events
that you have your other programmers in
years as so to keep carried other tables
put in a code unit that if the pattern
that I just showed would always call the
method code unit from the table or the
class code unit that I was talking about
right but would never put business logic
in a table the business logic the real
business logic is actually always on on
on cogent level I won't throw that yes
like a question about testicle innings
actually how do you test XML ports or
whatever is being importing where you
were in it file to import we don't I'm
on steer we don't we don't test XML
possibly don't test anything that
connects to something else or downloads
the file or or or something like that or
local resources these kind of things we
do as we if we have like api's we try to
mock the API call we do not do the API
call but we mock the response that
that's basically what we do and you get
water can I draw yes close do you have a
tip for connection between business
central and Asia to F ups so for example
you had some extension mate for business
central to get more productive and do
you have a connection where you can say
ok you have a task in business central
and connect the idea to Asia DevOps
tasks for example I didn't do it the app
catalog that you have seen could have
been done the other way around that we
basically just read DevOps and then got
the apps from an artifact store or
whatever we didn't do that we basically
push from dev ops to our business
central but I know DevOps comes with its
own api's so basically what you could do
is create the DevOps app like we did
with all the other piece of software ok
so you did it the other way around
the reason is because we have yeah
there's not a good reason by the way the
reason is because we push from multiple
repositories multiple organizations
multiple collections so we will just
wanted to push through one end point
which is our business central this is an
in-house reason if I would ever do it
like for out house purposes that makes
more sense obviously that you could
build like it DevOps extension within
within business Central and then talk
from that from wherever
ok so it's more a try actually all
prototyping to me arrested it comes from
prototyping what can we how far can we
go okay what yeah I need to give that
t-shirt to him so you're not gay
where do you do the builds in Azure
platform or in your own hosting servers
and you have you noticed some kind of
latency in Azure due to pulling of new
containers wait a minute
so the you mean the other parts of the
building the containers that's around
the building of apps which should the
built in DevOps yeah that's all our own
bare metal we do not use Azure machines
to build that's crazy expensive and the
reason is just expensive part oh yeah
and slow never do that I mean an agent
is very something very simple and it you
can set it up like in minutes
so it doesn't work set up another one on
another machine right in as you know I
know this is fanciful and yeah I have a
question okay no it's okay listen you
were speaking about multiple but if I'm
going to extend a table I don't expect
that every app will add some field to
that table because when I'm going to
insert something in that table I have to
insert the practically in multiple table
extension that physically our table in
SQL should we consider this issue
absolutely you need to consider the fact
that if you would have like we do 15
apps and every single app would extend
the same table and it happens to be the
ledger entry table I would reconsider
that I don't think that's a good idea
absolutely you need to think before you
would create that on the other side I
see other people that just create a
table extension and all the table
changes is done in that table extension
yeah that's a little bit too hard for me
I want to
look at that case-by-case basically yeah
if that makes sense as an answer yeah
it's complicated practically to decide
romanian state usually on these big
tables consider it okay what
implications could have let's see two
more minutes I believe very back yeah
the question about upgrades and
upgrading to apps would you ever
implement test-driven development and
not scenario in what and operating get
to apps if you're upgrading from an ax
from an earlier version you're gonna
sort of package everything as apps from
in the new you're all you do test over
test-driven development oh yeah yeah oh
yeah okay absolutely
okay thanks okay last question let me
throw this oh yeah be careful hey I
played basketball sorry you didn't talk
about it but when has it been where has
it been too hard to do it in al and what
did you do about it we try to sit down
together and find the solution usually
the answer the answer is surface based
architectures so create a web api I
remember one case where we needed to
read data from sequel table that's quite
hard to nail these days not I heart you
can do it on that intro what we decided
to do is read it through a web api or
at least we created an API to be able to
call from Al that does the read creates
an object from it and I basically got an
object by that I could easily use
adjacent response so yeah if there is no
API we create API that's kind of like
the simple answer to that one
at that point and on the NST so where we
would have the web client hosted the
same same part that's what we did that
that was already basically the thing
that we need okay yeah oh okay thank you
very much I really appreciate it that
you came to my session I hope you liked
it I liked it thank you
