# NAV TechDays 2018 - Designing for extensibility: Learn straight from the Application Architects

- **Source:** https://www.youtube.com/watch?v=-TdaINyhrTs
- **Video ID:** -TdaINyhrTs
- **Channel:** mibuso.com
- **Published:** 2018-11-27
- **Duration:** 87m48s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

good morning so we're going to talk
about designing for extensibility today
I'm Michael Hammond I'm an architect on
the business central team I've worked a
lot with extensions and extensibility in
the past few years and I'm Barbara
Goodson I'm an application architect and
I are doing basically the same as you
guys
I do the same thing in
application architect and lately focused
on extensibility and how to get there
okay so real quickly or agenda we're
gonna talk a little bit about background
what we've been doing how we gotten to
the point where we're at right now with
business central then we're going to
talk a little bit about the current
state of where we're at give some
examples on how to extend and finally
we'll talk a little bit about some
upgrade considerations when you're
dealing with extensions
so starting off with the background
apparently when you Bing for extensions
the first image that comes up is hair
extensions and if you let your colleague
make your transition slide it ends up on
your transition slide
so we've talked if you've been paying
attention the last few years we've
talked a lot about a couple things
extensibility and extensibility so how
did we get to a point to where we're so
focused on this and that's what we talk
about all the time
so going back if you remember nap 2015
it wasn't an issue it was all source
code modification we Microsoft would
work for a couple years create a big
ball of code throw it over the fence to
you and you would change it to do
whatever you wanted and that we'd do
that regularly and you'd have to figure
out how to merge it and we worked great
for us you guys figure it out but
there's a better way so in NAB 2016 we
introduced extensions and the first
round was admittedly rough and we got
some great feedback like that's a nice
toy you have there and that'll never
work I don't know what you guys are
trying but we did get some very valuable
feedback as well and we went forward so
now 2017 we completed all of the basic
object types we had most of the platform
support we needed in place but the
development experience was still very
rough so in 2018 we introduced BS code
in the al language
and this is where people really started
to say okay I get it I see the vision
and I can see that you're committed to
this and during all this time when we
talked about extensibility the message
was that
Microsoft builds extensible code that's
something that we need to do and we
teach people how to consume it and it
was exactly what we were doing at the
time it was exactly the state of where
we were at but in April and again the
small we released business central and
updates to it and now we have is be
embed solutions where is vs can add a
vertical deep into the system that can
be deployed on business central as
extensions and we also have pretendin
extensions so you don't have to publish
everything through Apps source you can
do a one-off extension for a customer
that they need as a bar or the customer
themself and they can create modify the
system kind of that last step to get to
where they need to be for them as a
customer
so now what we're here partially to say
today is that we're in a world where yes
Microsoft still needs to be world
worried about extensibility but partners
also need to worry about building
extensible code for others to consume
and I say this not as something you need
to do but if you look at a modified
version of the slide you saw in the
keynote we have these different layers
of partner customizations and these are
all in place today some of the other
layers that we that were talked about
are still coming but all these partner
layers are already there which means
that even if you're not intending for
people to build on top of your code if
you're in
Microsoft hosted Business Central it's
very likely quite possible that somebody
has already built a customization on top
of your code and hearing that was that
easy for that person to do on top of
your code do you think maybe it was
maybe not but some examples so we have
one embed is be live and two more by end
of the year even though this program is
just some pilot we have partner
localizations live for ten countries we
have about 150 app source extensions and
within the last 60 days alone we've
received approximately 100 new ideas
that partners are starting to build and
we have almost 15 hundred unique per
tenant extensions that have been used
within the last 60 days
so when we talk about people are already
building on top of your code these are
the numbers we're talking about
real briefly if you haven't seen pretend
in extensions yet so in the extension
management page there is a new option
called upload extensions and if you
click on that you can point to the dot
app file that you've built and upload it
for that extension it doesn't go through
app source and is only available to that
tenant that you're working with
the second reason that we talked a lot
about extensibility is
we want to create a development
experience that's fast and easy to
maintain
with source code modification it was
very powerful but we ended up with
something that looked a lot more like
spaghetti code was inner woven you could
still have some practices that would
separate things but because of the tools
that you had available to you there was
always some level of the spaghetti in
there and going forward we're trying to
get people to build in thinking about
building blocks as a style and I've
talked with one partner a couple of
times as an example who they made this
change a couple years ago and started
building everything as extensions rather
than source code modification and you
said at first their consultants hated it
they were used to being able to go in
tweak any line do whatever they want
really easily and said admittedly they
have some trouble right away they didn't
know how to build extensible code they
didn't know what extension points they
needed but shortly after they got it
going they said the consultants came
back and said you were right this is
what we need to be doing and they loved
it when they could go to a customer in a
presale environment start learning about
the customer and what they needed and
they could people come in and start
gathering information and they could
come back or sit down with a customer
and say okay you want this and we'll
throw a couple of extensions in oh and
you want that functionality we'll throw
a couple more in and some combination of
I think at their time it was 37
extensions they had they would throw a
combination of those in in the meeting
with the customer and say so this is
basically what you want basically right
there they had pretty much set up the
system at least with the functionality
that was needed and then they could do
that last mile to an sit on top of that
so with that in mind I'm going to turn
it over to Garrett
thank you
so are we there yet that's the key
question I guess so when we talk about
application extensibility there are some
questions we can ask so how extensible
is the application how much of the app
is extensible how are we progressing on
extensibility and finally where do we go
from here so some future aspirations so
how extensible is the application so I'm
only going to talk about w1 the same
thing holds for every country version
so you can add new objects you can
extend objects you can call save
procedures you could subscribe to events
you can use the next and enums and
there's a bunch more you've probably
learned here in the past few days
but that doesn't really say much about
how extensible the application is so how
much of the application is extensible
so some numbers this is the fall release
latest one
2,760 something integration events
sounds like long eleven thousand
external procedures that are safe to
call in a SAS environment but our
application is big so we have five
thousand eight hundred something objects
you can see how they're distributed
across the types we have thirty fourth
something thousand procedures we have
five hundred and twenty six thousand
lines of code
so and by the way it's getting bigger
every year it's pretty linear actually
so does this tell us how extensible the
application is maybe not so
78% of objects have platform events so
this is really great 80% you can you
know have credit ends on insert one
after all those things integration
events those 2,700 events are only in
664 objects which is roughly 12% of
objects so doesn't look so good now
and 50% of our code is either local or
internal which means you can't access it
if you you can slice it by by object so
50% of objects have nothing you can
access and in terms of code lines half
of the code lines you can't access
so how are we progressing on making the
application more extensible so we're
adding events every release we add more
events we have a nice curve
327 events in the next cumulative update
but external methods were almost done so
in the next update will add 2,200 more
and you can see there's not much left so
external events is the yellow the the
blue bit right so we had none in October
2016 and now there's almost no
global non external methods left
so then when will the application be
extensible enough will it ever be
extensible enough should we add more
events should we have events in more
objects cover the entire application
would you be able to navigate the tens
of thousands of events methods and
objects that we'll get if we continue on
this path is it the right path will we
ever get a fully extensible application
this way
we think there's a better way
so as you saw in the keynote this is our
kind of end goal where we want to get to
so highly componentized sensible of our
partners high quality open source where
components can be extended they can be
replaced they can be removed little star
there they can be added
the Stars because you can't remove a
component that somebody else depends on
but
so in the end everything will be an
extension
something about component izing the
application code the application was not
designed to be code customized so it was
designed to be code customized not to be
extended you guys all know that so by
component izing it will forces to
redesign for extensibility and
the interface to a component should be a
versioned contract
that can be accessed from inside and
outside business central we we don't
just want people to use business central
from within business central we want to
be able to connect to business central
from the outside it should define how
you use extend or replace the component
it's pretty obvious and
what about the components themselves so
we have some thoughts around that they
can't be code customized those days are
gone you can't have circular
dependencies because that would break
they have to be extensible by design
because otherwise they wouldn't be able
to depend on each other because there's
no more code customization they should
be replaceable they don't have to be but
they should be and
we think they should be small and
manageable but they should be big enough
to provide value and
we'll put all the source code on github
for partners to contribute so we don't
want to do all this by ourselves so
now a dose of realism right sounds like
a fancy picture this is the start of a
very long journey this will take many
years and yes we will break your
solutions along the way and
extensibility will not be automatic and
it will not be free we will have to
design our components with extensibility
in mind and yes we will make mistakes
and hopefully we will learn and then
we'll move on so where do we start so
another slide from the keynote
on how to component eyes so component
eyes from the bottom we're starting with
the system layer
so what's what is the system layer right
it's basically the interface between the
application and the platform it's a lot
of the things you know as code unit 1
which hopefully you know is gone
it should hold all the platform ish
functionality so here's a short list
this is to be decided we don't yet know
all the things we'll put in there it'll
be a pretty long and
this is the place where we're going to
access all the unsafe bits and we're
going to wrap it in a safe way so that
you can use it and
the system layer can't be replaced and
that's exactly because it will do all
the things that are unsafe in a cloud
world
but we will open source it and you will
be able to contribute to it if in case
we missed something
and then what
so here's a rough timeline of what we're
planning to do so
separating app from platform that's been
done that's basically when we removed
code unit 1
creating a system layer that's in
progress we're actively working on this
we're planning in planning stages for
creating the app foundation layer which
will be all the horizontal features that
everybody will need and want to use and
after that the plan is but it's very
fluffy to start pulling out the the
financials module and at some point
we'll componentize everything
so now over tomorrow for some examples
yes you can so that's another thing that
comes up when you look for extensions
we'll take a look back in time as well
so for instance back in time we want to
allow users or partners to substitute
our reports with others also sort of an
extension we had the report selections
pay-table that most of you know
which has a usage and this is how the
option string looks today I don't know
how if you have a love-hate relation to
this one
[Music]
so this is something we should fix I
guess yeah
that's exactly how we feel about it
so yeah I said used for selecting which
report so the thing about an option
field is that it provides programmatic
validation when you compile right that's
important because
but it's also difficult to extend
so can we fix it
first of all there's the upgrades issue
if we fix it so should we move it to an
integer or to code
should we hard code specific values or
do we want and then you know a lookup
table that that defines the usage if you
made these
considerations yourself
[Music]
or should we just wait for modern L
hope some of you were to be presentation
yesterday on the modern ale
because there we define
the values in this way and this is kind
of nice and programmatic and the same if
you extend it you
seem to write the new values right so
maybe
this is just what we should do wait for
it
we leave it as is for now and wait for
more an ale so I think that's our plan
for now
another thing that we made some years
ago was the dimensions functionality so
that was also intended to be as
extendable as we could think of back
then it's generic user-defined I mean
you can define these anything should be
easy for the partners to extend
the caption class functionality that
some of you may or may not have used was
actually introduced at the same time for
this very specific purpose
in case you don't know the dimension
system so this is an item
this is the default dimensions for that
item and it relates with
a
table ID and the key for the main entity
and this is a pattern we then use for
customers and vendors and what have you
and
for transaction so this is a sales line
it has
a dimension set enter that points to a
dimension set and when you post it the
posted entry also points to the same
so for the ledger
and that's
this is how they relate
and we as well have library functions
and which it also with what I didn't
show there was we actually also at that
time release documentation on how to do
it for you developers
the caption class
this is an example from I think it's a
sales line or customer whatever it is
so you see up
there one point two point one and if we
look here in code unit 4 to caption
class management
the one relates to the area which is
dimensions to which group so this would
be shortcut and number one is
number one
which then points to shortcut dimension
number one which again points to
department where we
define code caption or field caption
depending on which
field you want to show
and as you can see here nicely price
department code as specified there and
the same with the other ones and
if you want to use it in your
solutions
this is how you could do it either you
can hard code something there or you can
make a function that may makes it
dynamic so in this example we just show
a random singing so it feels like a
lottery every time you look up a
customer 41 here at the
time when this was picture was taken
another less understood feature is
out of format expression for amounts
so a balance you see we have type 11
which is custom and then again a
function could also be a constant value
II but I could just write
and then you write something so hey
something and which then it means that
the number will be
format like that
maybe not as use useful but
it could be used for drawing attention
to
the number or as we do several places we
use it for adding the current design
so item charge this is actually one of
the first things we designed it for the
new way to extend
code
so when you want to when you have an
item charge and you want to distribute
that on among one or more don't dispute
to one but distribute among several
sales lines
you click that thing suggest I didn't
charge the Simon and then it suggests
you different types or different methods
of
distribution equally paramount or weight
or volume but
it could be that you have a fifth or
maybe want to exclude one of these maybe
you want to change this option so how
would you do this without modifying our
code
so if you look at the code that does
this so first of all we have the
assume you know about you know string
menu so here we construct the string
menu with different
options
and
you're suggesting just before we show it
we call an event
where we pass everything in including
the
string
so then in you or amend subscriber can
either add to the string or remove from
it or do whatever and
then we shall show the string to the
user and then
we
call this function which bring passes on
what user actually selected
and
so this is our code I mean I delete it
so much there but then we say
if the user selected you know one of
ours then we do what we decided or
we pass it on to your event so this is
in a minute that you would then
subscribe to so if the user chose option
number seven you would handle option
number seven and do whatever you need to
do with distributing the
yeah there
so that that's a general pattern we will
you know we aspire to to do
[Music]
Michael talked about building blocks
also talked about component component
and then ties in the
application so we have a lot of features
or building blocks that are horizontal I
mean they're kind of generic we have
some some there are more vertical in
their nature like manufacturing and
distribution as such
so how would we go about designing a new
thing here
so one thing we have heard over and over
from customers is
subscriptions or recurring invoicing or
whatever we call it
so as you can see there are
many many examples where you use
recurring invoices I mean if I look at
my bank account I
don't know 70 or 80 percent of what goes
out goes to some sort of recurring
payment rent insurance stuff
so
this is what your customers want or our
customers but what should we do
Microsoft so if we extract what's
generic from that I mean it's something
about managing subscriptions like
generically something about being able
to create periodic invoices
something about changing the price up or
down
something about being able to mail or
send email make some sort of
notification to the customer that we are
changing either price or conditions
some sort of tire debit because if you
have many subscriptions you would
probably sign up with no credit card or
some sort of automatic bank transfer
so if you look at how such subscription
system I mean from our point of view
could look like so let's say that the
end goal is that we want as it's a sales
invoice so that's what we want and how
do you then get there so we have a
customer and
we have some sorts of subscriptions
here right so this guy can select from
it some of these so I
added Jim basic there
and then you can sign up for it means
that he gets assigned
Jim subscription
and then we have a batch job that can
generate
periodically an invoice from that
so this is basically what you already
have or almost
with the so called recurring sales lines
and standard sales lines if you are
familiar with it
but we need more right so we need some
sort of
recurrence so what I drew up there is
maybe it's difficult to see from your
where you are but this is the recurrence
you can select in outlooks recurrence
when you
want to set up a meeting right there you
can see do it daily weekly
every other week last Thursday of the
month
whatever and we actually I
have this in words I mean in lab
to do something similar for now because
it has been a frequent ask for job job
queue for instance to have a recurrence
even sent that is more meaningful than
just minutes
so that's something we should be able to
connect the recurrence object to
custom subscription
we also want
conditions so terms conditions it could
be a symbol as a word document you know
just some attachment that
can be generic to the subscription and
then it's passed on to the customer
because it could be that the customer
gets a
different condition than default one
we also want to be able to adjust prices
both our I mean the announced prices or
the price list view or the individual
customers and
this is probably something that would be
heavily extended because
I mean like prepayments so if their
prepaid do you pro pills need to adjust
the prepaid amount there are a lot of
difficult things there
we also want to be able to send
the letter to the customer to advise
them
before we send out the noises
we probably also want to be able to
verify that the totals right we want to
be able to
you know run reports
ensuring that we are
collecting the exact correct money we
want to so don't over charge or under
challenge and
also some sort of payment integration
so what it just showed is what we aspire
to do but your customer I mean our you
eat more so
as I said
this is a table right and you'll be able
to extend with code and fields and
whatever
same on the customer
subscription because if you subscribe to
an insurance there might be all sorts of
insurance specific things when versus a
gym or something else
you
would certainly want to adjust our
change how we calculate prices
you certainly also want to change how we
collect or generate the invoices and
how we which report to run they could be
as simple as report selection so we can
add yet an option to the string from
before
maybe two options even
we can use customer layouts which is an
existing way of extending
or
you can substitute as I said not only
extend our stuff but substitute our
stuff so that's what this would be you
can in this example I said I imagined
that maybe you don't want to go through
sales documents and then posting new
sales documents I mean if you have a
simple thing like a gym membership or a
music subscription then why would you go
through creating a sales invoice and
post a sales invoice which is expensive
maybe you want to go directly to
customer kill the Gentry's
just do a journal posting
so that's how we imagine creating the
subscriptions I mean this is something
we are working on as we speak
so example one
another thing that we talked about as
well was
separating out I
mean we start from bottom layers who
will separate the GL from the rest and
to do that
we need first we need to remove
dependencies
so if you look at the general ledger
table or GL entry table we have things
like production order I mean why do we
do that fixed asset stuff
and some system things
there are also the hidden dependencies I
mean why would a customer ledger entry
inherit its entry number from GL entry
number that makes it difficult to
make what make what we had in the
previous example maybe you want to
create an um a lot of custom Ilic
entries and then collapse them all into
one set of G lenses
so in your account you wouldn't say you
know membership for customer a customer
be but just
December months membership fees
so again
the general journal
it needs to be general right today is
not real general you can't post items
with it right
but also you already today you can post
to things that you know if you look at
the bottom layer of the general ledger
that if you only look at the bottom
layer you wouldn't know about items or
customers or
fixed assets or whatever so we need to
be able to extend it to any sub ledger
and
so assume think of a general ledger as a
true general ledger or journal that can
take any type and extendable to any type
then when you post such a thing with
whatever types it has think of this
patch as a bag
property Bank if you're
thinking programming terms or just a bag
of things and then you pass it on to
each subsystem like inventory
capital creditor
insurance
leasing whatever system you might have
and then each sub ledger could you know
handle their records or their journal
lines in that patch and replaced with
either you know Gil or if it's further
up in the chain like if it's some
manufacturing it will probably know
about items and so it could
substitute
its journal lines with item journals and
then
eventually
you know it would only contain GL
journal lines then it will be posted to
the finance
so I mean this is what we aspire to so
it's hot air on till now right
yeah so then I think this concludes the
examples of
from the applications
then
great
Michael boo yes so we'll so once we
started building a system where we have
many extensions and the extensions are
all interacting we need to figure out
how to upgrade all these pieces together
we obviously want if you've got
something working when you go to the
next version we wanted to keep working
and there's some patterns that we've
seen or some things that we think people
might not be aware of yet that we want
to call out here to help start this
journey
so I'm gonna start out with showing
what's available in upgrade code units
and extensions so we have six functions
there's per database and per company
copies of three different triggers and
the I'll start with the middle one on
upgrade per database that is where your
upgrade cone goes that one's pretty
straightforward people understand how to
use that one it's the other two where we
get a little bit of questions and some
confusion about what their intent is so
the first one on check preconditions
this is something where and I'll talk
about this a little bit more in the next
couple slides but you're able to check
before you start a lengthy upgrade
process if you have a lot of data can
take quite a bit of time you don't want
to get to the last record of five
million records and fail on something
that could have been detected in
milliseconds for a couple of seconds
right away if there's a way to detect
early some condition that you know is
true do that right away find out if it's
going to be a problem before you start
going through expensive upgrade
operations
fail-fast
allow somebody to fix the data and then
try the upgrade again
the last one on validate upgrade if in
the context of upgrading a single
extension is probably not really useful
again I'm going to talk a little bit
more about upgrading multiple pieces at
one time but when that happens you may
want to make sure that something that
happened during an upgrade you were
involved in still holds true once all
the pieces finished upgrading if there
are conditions like that that you need
to check things that you're worried
about this is where you put that logic
and all these triggers all three of them
operate within a single transaction so
if you find something that's wrong you
can throw an error it will roll the
whole transaction back again again
that's part of why we want to try to
find easily identifiable problems up
front in the check preconditions so that
we can fail quick we don't have to keep
that long transaction open it doesn't
take all that time we don't have to
spend the rollback time it's a lot
easier on the system and a lot more
effective for users to deal with
so now that we've talked about
components how do we upgrade these
components together so the way it's
typically done right now and in the
examples I'm giving right now the today
the base application is written in CL C
side but as we talked eventually this
could become one extension multiple
extensions it really doesn't matter for
these examples but I'm just want to call
that out so what we do today is we tend
to upgrade each piece when it succeeds
then we go on to the next one we can
still do these in one process through
set of calls but we're essentially doing
one at a time so go through the base do
is check preconditions do its upgrade do
its validate then take the first
extension and run all of its pieces
the way that we are moving towards
internally and we want to promote more
externally is that these processes can
actually be inter woven as long as you
not don't have too big of a transaction
with your upgrade code that it'll
refills the transaction buffer you can
run all of these in one single
transaction that means that we call all
the check preconditions first
so we'll call the Chuck preconditions
for base for your extension for my
extension for Garrett's extension and if
any one of those finds an upfront air it
stops if no errors are found we go on to
the upgrade step and we'll call the
upgrade code for all of these extensions
so that we run them all and you can
start to get to see why the Chuck
preconditions is valuable up front if
I'm the seventieth extension in line in
a single upgrade process and I don't
accept blanks or defaults in a certain
column I need something specific for the
upgrade logic I have if I check that
right away I haven't run through the
first 69 extensions then at that point
before my extension fails its upgrade we
can again fail-fast find right away and
then with those multiple pieces that we
talked about we may have some logic that
we need to validate when it's done did
another extension touch say maybe I'm
integrating to a base table if I'm
integrating the customer and I'm
changing some of the data and customers
that it works with my application I want
to make sure that another extension
didn't come along and reset the values
or change it to values that are no
longer valid
so then we start to get into scenarios
where how do I know what's actually
happening how do I know if I'm upgrading
if somebody else is upgrading I've got
events that I've hooked up through all
the system if I'm subscribed to an event
on the customer table when the customer
fires is it because a user's in the
system or because somebody's upgrading
the customer table I may not care during
upgrade I may go back and fix it later I
may just want to wait until the whole
upgrade is done so I can fix everything
once instead of constantly interacting
on every record slowing things down
doing a lot of extra logic and
processing so the first piece we have is
the execution context API
the execution context is an option
filled with normal install and upgrade
pretty straightforward and we have a
couple of different usages available you
can call into session dot execution
context that will tell you what's going
on in the system as a whole if any
extension is installing or anybody's
doing an upgrade those will be set
appropriately if none of that's happen
happening execution will be normal
then the next one is what's happening
with my extension so I can use the get
current module extension context
execution context and find out if the
execution context is upgrade yeah my
actually upgrading or as somebody else
upgrading where am I in relation to this
and on the previous slide where I showed
how these are all happening at the same
time we're within that step this will be
the one who's upgrade is currently being
executed so you can be queued for an
upgrade in that set but the execution
context will tell you which
extension or base is currently doing the
upgrade and then if you have
dependencies and you want to know is
your dependency upgrading or is another
extension that I'm aware of upgrading
doing an install you can look up a
specific one by calling the get module
execution context and passing in the
module ID that's the app ID in the app
dot JSON file pass that in to get the
context of a specific extension that you
want to know about
the second piece this is the module API
so there's a couple of pieces to this
but this basically allows you to get
information about an extension so again
get current module info will get
information about your extension the one
that your code is authored in or you can
look up information for a another
specific extension this will give you
the ID the name the publisher things
that you said in the app JSON the
versions and any dependencies that you
have or the module has so the probably
the most common way this gets used is
with the app version and data version
both on install and upgrade so on
install if it's installed for the first
time it's never been on the system the
data version will be zero because
there's no data there if the app has
been uninstalled and then you install
the same version again the data version
will match the app version because
you're putting on the same version of
what's already there so you can use that
in your install code as well on an
upgrade then you can tell which version
you're coming from if you're going to
version 6 scene of your extension and
the data version is too maybe you don't
support an upgrade path there that's
something that you can check and find
out is this something some data that I
actually can upgrade something I know
about do you have different upgrade
logic depending on which version you're
coming from I already converted
something going from three to four so if
I'm going from four to five I don't need
to convert that data a second time but
if I'm coming from three to five that
data hasn't been had that first round of
conversion yet so I need to handle that
case as well
so a quick example of checking the
context basically I talked about so
we've got two variables of execution
context I'm just calling first of all
get the execution context that's the one
for the entire system
and then I'm getting my local context
that's for my current extension and then
just a quick check to see if the system
is in an upgrade but my extension is not
upgrading then in this example I'm just
gonna exit this is not logic that I need
to worry about when somebody else is
running in an upgrade and if I'm not in
an upgrade or it is my extension that's
doing the upgrade then I have some code
that I want to execute here so pretty
basic example we've also talked about
being able to attribute event
subscribers something we'd like to add
so that you don't have to write all this
boilerplate code but we haven't plugged
this into everything yet because there's
different situations depending on what
your code is doing depending on what's
happening in the system right now is
something that you will need to actually
write the code to go do but hopefully we
can make this a little bit easier going
forward
so a couple of other considerations and
these are things that people get tripped
up a little bit on so sometimes I talked
a little bit about versions don't need
to be applied in sequence so you can
upgrade from one to two to three but I
can also upgrade from one to three and
that's up to the extension to do those
checks for is it a version path that you
support in your extension
obviously going from one to three is a
lot easier for the user they don't need
multiple steps it just means that your
code has to account for that situation
and at some point you'll probably get to
a point to where your several versions
back and maybe it's not worth
maintaining that upgrade going forward
all your users are off of that version
extensions can be uninstalled prior to
an upgrade being invoked I talked about
uninstalling and then reinstalling it in
my previous example I can also uninstall
v1 maybe there's a breaking change that
we Microsoft introduced when something
came out and it's a non-critical
extension it was useful helpful um have
some nice functionality but you want the
user upgraded and you can go without the
extension for a little while so you
uninstall that extension and then once
you've had time to modify the code to
work with that breaking change you want
to put the new upgraded version back on
the system so an upgrade gets invoked
and that's where you're going from 1 to
in both install and upgrade cases if the
extension was on the system previously
if you have table extension objects with
the companion tables we make sure that
there's default values in the companion
table for every record in the base table
so if defaults are ok there's nothing
specifically that you need to do but if
you need more than that if you're
getting either reinstalled or upgraded
from not install you might need to check
some of those values again to make sure
that they're valid because the system
ran for a while with your extension not
present so there may be some data it
needs to be cleaned up
when I talked about those serial
upgrades before and in general in
extensions commit is ignored we don't
want somebody to end up in a situation
where an upgrade fails it rolls half
back and then they can either work with
a new extension because the upgrade
failed but they can't work with the old
extension because the a
partially completed committed some of
its data so maybe that data no longer
works with the previous version so if
you write a commit during an upgrade we
will ignore that
um also we recommend avoiding external
calls during upgrade we recommend
handling these after the upgrade
because you don't want to be start
making external web service calls during
your upgrade have a network connectivity
spike not be able to complete and it
rolls your entire upgrade back
basically just try to do the minimum you
need to in your upgrade and clean up the
rest
in a post upgrade step obviously you
want to do the upgrade of the data do
that but try to avoid things like
external calls if you can help it
a couple things to know about schema
this is the modifications to tables once
you've added a table currently we only
allow additive changes we don't support
destructive changes so this means you
can't remove fields or keys you cannot
rename fields or keys and you cannot
change data types this is pretty
restrictive and it's a change that takes
some getting used to but it's a pattern
that we're working with internally and
we've kind of learned to deal with it
and it makes you think a little more
upfront about what you're gonna change
going forward so once you can't do this
you run into all kinds of problems right
away how do you start to work around
this and the way we do that is with the
obsolete state property this allows you
to signal that fields are going to be
removed going forward and there's three
values for this normal pending and I
forget the last one but basically it
said it's no longer able to be used so
what we recommend is set it if you're
the example we use to demonstrate usage
of this a lot is I started out with a
name field in my table and I want to
change from name to first-name lastname
but how do I do that if I can't get rid
of the name field so we recommend um
turning name into or setting the
obsolete state pending first of all and
then adding the first name and last name
fields to the table and the new logic
should work there you probably hide name
from the UI but name is still present in
that table it can still be read from it
can still be written to and then you'll
want to handle any rights to name just
split name into first and last name as
they're being written and try to
maintain both of those fields for a
period of time we recommend at least one
major update is what we try to do
internally so that people have time to
react if they've built on top of that
it's there's nothing worse than coming
into work one day and finding out oh
everything is broken it doesn't work
anymore giving people a little bit of
leeway with that helps everybody out in
the long run and then once you no longer
once you've given them a window you can
change the obsolete state to hide the
field and remove it and even though that
still exists in the table it cannot be
written to the platform blocks out it
can only be read from an upgrade code so
that you can still move values out of it
if you need to and then going forward we
are working away on a way to enable the
actual scheming removal this is not
something we have yet this is something
that's impacting us as well Microsoft
this applies to all extensions it's on
our backlog coming soon with a way of
how to actually then remove the field
from the object and from the sequel
schema
so finally what have we talked about
here
and we titled this join us on our
journey intentionally this is not
something that we want to force on
everybody for change sake but we believe
that extensibility is important it's
going to be more important we've been
saying this for a few years now and
wants you to be involved with this as we
talked about at the beginning people are
building on top of your code as well
it's no longer that Microsoft's code
isn't extensible we realize we've still
got work to do but you're going to start
building on other partners code people
are going to start building on your code
so come along with us we'll share things
that we're learning please share things
that you're learning so when you're
writing your code start thinking about
how other people extend my code where
are they going to tie into it what
functionality might types of
functionality might they add to it and
start you know if you know of people
that are building on your code go to
them for feedback what are they doing
with your code today what are they going
to want to do once your code is in
extensions and then start writing
extensible code where you can things
like bar durscher showed with when you
have a switch statement the default was
to call an event the default was no
longer to throw an error because if
you're throwing an error in a switch
statement there's no way anybody can get
in there to add a new case that they
want that wasn't in your initial design
um practice writing safe upgrade code be
aware that there's other extensions on
the system that other code is executing
in the same upgrade transaction with you
unfortunately as said prepare to be
broken this is going to be a transition
our goal is to do this once and do it
right so it will be a little bit painful
at times as we go through this we'll try
to minimize it and keep it as easy as we
can but there will be times where we
will break your code
um and last of all most importantly we
believe give us feedback when we started
extensions a couple years ago like I
said the initial response was not
overwhelmingly positive people some
people saw where we were going and we're
excited but a lot of people weren't real
on board with what we delivered in that
first release but we got a lot of
feedback and we took that into the new
development tools we've gotten a lot of
feedback there we've changed the way we
solicit feedback for that and that
iterative approach has helped us develop
something better develop something you
use and as we're changing the way we
interact with the community we can
deliver changes faster this is also a
unique time in this product a lot of the
changes that have come down in the past
have been worked on for three years then
delivered and then you were stuck with
it we can make little changes but there
wasn't a lot of things we could do we're
starting on this journey we've obviously
had extensions for a little while but
the application refactoring is just
starting so if you have feedback if
you're actively involved as we're going
through this getting the early builds if
you've seen some of the other sessions
about where to get the docker drops that
are coming as you're getting that stuff
try them out provide feedback let us
know this is an opportunity for you to
be involved and get something that works
best for it to the community for
everybody for the product longevity
going forward 10 years from now it's
gonna be hard to go back and change what
we do on the system layer and then
contribute to the github repositories so
the last slide there's a bunch of
resources but you'll notice several
these are github repositories so the
first one is the development tools on
the open CIL library where you can
interact with net on that it once we
prove that that will go into the base
application ale application extensions
we're starting to share our extension
code publicly both so you can see them
and see what we're doing and also say
you can contribute back to them
and then so those are the places that we
recommend right now to get involved with
seeing what we're doing
we're very active on those sites so if
you're active there you should get
feedback in it within a couple of days
generally
extension requirements
you can go there to see what what it
takes to build an extension to put on
business central and the Microsoft cloud
and they're ready to go program is
another place to go look at some of the
documentation get started find out what
you need to do for building extensions
so I don't know how we are for time
hopefully we're okay but I think we're
so that question is but strictly tied to
extensions but something we are
working on so whether we get it for
spring or not it's not a promise but we
are working
Thanks
you can hear
so the moment when you deploy extensions
to the Sun box the same checks aren't
carried out as when you deploy them to
production it's not intentional
so
is code and it was happy use the upload
extension I get an error because
someone's missed the application area or
something so are you talking about when
you're deploying it to production are
you deploying it from app source or as I
pretend an extension
okay so the reason we do that is you can
develop both app source and pretend
extensions in the sandbox so we've
basically taken the least restrictive
set to put on there so when you deploy
pretend there's a couple other things we
check if you mean BS code there's now
code analysis that you can run and you
can use the pertinent cop will give you
locally when you build all same checks
that would do when you deploy it to
production
a small suggestion on the ordering or
the triggers on the app the upgrade code
units could you add one that it also
validates after a single extension I can
understand that you want to check
everything that it doesn't roll back
halfway all of a sudden but if you're
only going to validate at the bottom of
everything I think there could be some
checks in front of that preventing to
roll back after my extension is wrong
already yep yeah I think you could do
that you could also do that in the
upgrade so we could add that
even though it's just tricky what's the
question
it's broken
so the question was when you have
multiple extensions upgrading do they
always upgrade in the same order and I
believe the answer is yes that your next
question is gonna be what order do they
upgrade in and we don't guarantee an
order and so I believe it there is an
order but we reserve the right to change
how that order is calculated and
we do respect dependency order though so
if you have a dependency on another
extension and they're upgrading at the
same time your one that you have a
dependency on will do its upgrade before
your upgrade happens
yeah so the question is the suggestions
for github whether it's only for w1 or
all countries or all versions and
obviously it's for all versions and
we'll actually those encourage you to do
so because it's typically the same I
don't know five ten people who are
active there which is not much so I
would I mean there are hundreds in here
so please do
report extensions report extensions
report extensions is something we've
talked about haven't done yet so right
now you can replace the layout but we
would like to make it so that you can
extend the dataset would be the part
that we would allow on a report
extension so it's something that's on
our radar
we just haven't implemented it yet
Thanks
[Music]
yesterday
your colleagues they told us that the
requirements in order to upload an
extension to observe and you
thought you showed the link where we can
check those extensions
the thing that I want to ask is
one of the requirements is that we have
translation so we have actually file but
I think that they said that the extra
file includes only the captions what
about the text constants and the other
things so
the ex lip file is just for translations
right so I don't I don't know exactly
how the format is but you put your
normal captions in using the label tag
right in the axle if you get a reference
to the label and then that's
good I'll go with the microphone over
there it's okay
hi
as interested in the
roadmap for extension izing the
application we've got
a vertical which integrates the
inventory module heavily but we find it
very difficult to make this vertical
work without modifying the source code
of the inventory module and in certain
cases just a lot to do with reservations
we're on the roadmap is a rework of the
inventory module and at what point will
the source code be locked down so that
we can't actually
correct the issues that we find with it
it's a very good question it's on the
bit of the broke map we haven't looked
at yet
it's it's too far ahead in the future to
to say anything about that
so
the way we're doing it is so we're we're
taking things out of basically the
bottom layers right and those those were
building them as separate components
extensions and then refactoring the base
app to use those new components and so
we'll go up through the stack but at the
same time I think you know you can you
can continue with what you're doing
today until you know the inventory
module probably multiple modules get
pulled out and then give us feedback
obviously but the idea is that that by
then decision the system should you
should be able to take the component
which is open source
change its code and republish it as your
own so in that sense you will still be
able to code customize but if you do
then you take responsibility for the
entire component so that's kind of the
plan but when when will this happen
you know one year two years five years
I've no idea
you hear me okay you were saying that we
should
expect potentially breaking changes
every six months so what is your concept
to prepare partners would I see
solutions are there going to be early
bills that we can check our solutions on
or what what's your concept on this
so as far as I know it's it's the same
as we have today so we have docker
images
every every build every day at least I
think it's
least every week I think every day so
you can go see the latest
now okay so those are not the official
bills yet so we have more or less an
early build we can check our stuff on
and then it's going to push to the real
customers eventually
okay
see what we're doing take a darker build
every day or every week
with regard to amending indexes
so in this indicated you can't change
indexes which is an issue because the
indexes have some index fields they have
to maintain
sift index maintain not maintain the
sequel index so and the ability to add
indexes
so you can add new indexes okay that's
the reason we don't allow you to change
indexes is because
internal backings of what we do when we
host we can actually host multiple
tenants in the same data database and
they could have different versions of
the same extension installed so if you
have v2 and v3 of your extension
installed in different tenants but on
the same database then if they have
different indexes we can no longer keep
that table together if all the indexes
maintain the same and that's why we
don't delete fields right now currently
as well is because it's basically the
common denominator of what's there is
what's actually in sequel
different tenants just see different
portions of the table based on what they
have installed and that's where why if
you change an index then we can keep
that table together anymore
and change this from the based
application like an example being
content entry into the warehouse ledger
entry is turned off by default which is
a big performance in a warehouse so that
needs to be able to be changed by an
extension and cannot be or you can ask
us to do that by default right well turn
them all on and all by default and give
me the ability to in a separate way to
turn them off because we do index tuning
okay the the product breadth is wide and
so therefore the maintenance of those
some indexes by some clients is
unnecessary in their hot tables yep
maybe it's a question for my it will be
possible to make pertinent indexing well
so
in in Microsoft host so this is probably
not something you'll be able to do we
talked about ways to do it on Prem and
if you're on Prem right now the easiest
way to do it if it's in the base
application is just go change in the
base application right now
yep yep exactly so this is a problem
we're aware of we know about we're
working on it but that's what I would do
in the short term until we have a
solution to just go do in the base app
if you're on Prem right now okay so do
you think that this would be addressed
by the spring release I honestly don't
know if it's on that team's spring
release or not
yep completely agree that is important
so I just I can't commit to it because I
don't know we're back
in 25 countries and none of those
countries is available at the moment on
the business central so these are more
exotic countries I would say do you
think that with this approach we are
going to see viable localizations in our
lifetime um yes
so I'll say two things about that number
one we've been increasing our number of
localizations that Microsoft provides
out-of-the-box as I said in one of my
slides we also have ten partner based
localizations that have come online I
think all of them within the last six
months so if if you want to build a
localization or talk to Microsoft
the one link that I had
get started with apps I believe has a
link for building a localization apps
was required who to contact so you can
go there and find out more information
if there's one you're looking for
specifically or one that you want to
build and provide thank you I
have a question also you said it would
be possible to replace your components
but if we do that good other extensions
still be able to use our new component
just as if it was yours
so
there's
very interesting things that go on when
you start thinking about replacement so
I'll just go off in dreamland for a
little bit right so
so currently you can't replace any
component because if you have a
dependency it's hard link to some good
and if it's different good even if it's
in code broken so number one fix that
if you think about you know replacing a
little bit more extensively so imagine
so the bad example but it's a it's an
easy one right so locations locations
today it's a code field right and then
there's a bunch of stuff behind it
imagine I wanted my locations to be
longitude and latitude
what do I do I can I had extra fields
and then wherever I go I can go use
those two fields and have some table
relation to all sorts of magic but if in
my component I could decide
what I think a location is is LAN
student launched in latitude and when
you put that on a cart page you show map
and if you put it on this page your
coordinates and if you used here do that
and so that's all defined within the
component
and anybody who depends on me doesn't
say here's how they just say I want to
use location they don't say how to use
it they don't say what do they just go
put location here when I go in and I
about the location and I put in my new
you know latitude and longitude location
everything should just light up
everywhere that's kind of like the
really long-term dream so that requires
every component to define a very strong
contract say exactly here's what I allow
you to do if you want to extend me here
are the things you are allowed to do if
you want to replace me here are the
things you have to provide that other
people have used right and so if we have
that and it's probably you know we'll
never find probably be new object type
type of contract well
then we could start to do you know very
interesting thing with with replacement
as I said far into the future but it is
being discussed and thought about you
know the same as in dotnet or is it C
sharp that you would have to implement
an interface right
so got a question there
hello I was just wondering are there any
special memory considerations when
you're working with extensions
so if you have more extensions you would
need more memory
slightly it's not significant because
it's basically similar to creating
objects in Seaside right now creating an
object and one of the other once it gets
to the platform at runtime they're
indistinguishable from each other where
they came from
obviously if you create a lot of
extension objects it will be more memory
but it's not significant compared to
actually running the system with the
data just the amount of data that's
there and being cached so it's pretty
negligible
so we should say right now we do have a
couple issues currently with if you
build very large extensions and by very
large you'll start to see some
performance on when you have five four
vs code I think when you get up to two
to four thousand somewhere in that range
and if you get to tens or hundreds of
thousands of objects in your extension I
don't know why you put a hundred
thousand objects in one extension but
you might want to
then you get into some real issues but
we're working on that right now fixes
available in the spring hopefully for
that so but that's simply just deploying
the extension with layers had a hundred
thousand objects
once it's running it's the same as
creating objects in Seaside
yeah you talked about Kotov can be
triggered during installation or
upgrades but not during an installation
is there a specific reason why it's not
possible to trigger code at that point
or am a missional possibility no we
actually get that a lot and there's a
couple of reasons we don't do that
number one is would you want your code
triggered before or after your extension
is uninstall and if you say after
because you want to make sure that the
uninstall I should have completed how do
we run your uninstall code after your
code has been removed
that's the bakery or one of the big
reasons that's the technical reason the
second reason is we don't want
people when you try to understand
extension to put in no my extensions
really good you really want it error you
can't get rid of my extension I mean
that's obviously a path that probably
won't happen but if you have a bug
nobody writes bugs but if you have a bug
that throws an error then you can't get
rid of the insects rid of the extension
so how do you fix it from now point so
until we have satisfactory answers to
both of those we don't have uninstall
code
we're here
one more question about replacing
components I know it's far in the future
but what is your idea do you expect
people to rebuild everything from
scratch or use your al code and do kind
of like code modifications and then
replace your component so what is your
idea or your expectation on that both I
guess I mean one thing is you could the
case of location you can completely
change it or you can take whatever we
have and do your tweaks and then put it
back I mean so you
the idea is to look into both directions
sorry yeah the idea is to look into both
directions you should be able to enhance
the example you should be able to both
enhance location or if it's completely
not what you want you want something
completely different you should be able
to put in a new component
similar to interface isn't on that if
you have an implementation of the
interface I can take out that
implementation put in a new one and use
that instead okay
I
hope you would consider you know going
to get help changing the code during
pull requests getting it accepted
helping everybody else before you decide
nope my things so special nobody else
can see what I'm doing but
we should
I was just wondering if there was a
timeframe on the removing fields
other work because right now the the
problems of leaving are there for now
are that you have extra schema sitting
around that nobody actually uses never
gets queried and you have it
unfortunately in your al code but other
than that there's no impact the system
so it's when we look at some of the
other situations where we got things
that are a little more pressing it's I
don't want to say it's pushed off the
radar but it's a little bit lower than
some of the other things we have going
on right now so
what how do you can you unable
effectively the field is what was game
yep so if you don't want anybody to be
able to use it you set the
I'm setting obsolete state I think too
so and once you've done that the only
place that field can be
read or written to is an upgrade code
and that doesn't affect the records
locally the object size right so if you
look at if you get a record of that
table then in your normal code the field
isn't there so it can't be accessed
are you going to provide a payment model
for the app source
so you can
so we don't have to do that ourselves
with the customers we are trying to get
the App Store's team to implement that
and it seems like every time we ask them
it's six months out and we've been
asking them for three years now and it's
always six months out so I would like to
tell you that yes it will be here
immediately we're unfortunately that's
the team that we don't own control
they know we want it we keep telling
them we want it it's just a matter of
when they'll actually give it to us and
I know that's not the answer you want
but unfortunately that's the best answer
I can give
you if you want to do an customization
to another partners app how can you see
the extension that they have installed
the the source code that they made it
will have a opportunity to export the
the extension that they made so this
leads into my favorite question is
for 3-4 years now when I've been talking
about extensions it's died down a little
bit but the first question I usually get
is how do I look into another variation
how do I look into somebody else's code
so I can debug it build on it not
something like that the second question
we get is how do I keep people from
seeing my code I'm not sure how to
resolve but I'll tell you what we've
done and you can tell me if it's good
enough so you can always build on top of
another partners extension in the app
that JSON there's a dependencies array
just put the app there the good for
their app ID in there and then when you
download symbols like you download our
platform symbols in vs code it will
download the symbols for their extension
as well if it's installed to an
environment you have once you have that
you always get access to their metadata
so you can see their tables and fields
you can see their their pages and the
controls that are on them you can see
their code units and stuff that's global
there you don't necessarily get access
to see their code though there's a value
in the app JSON called show my code and
that's up to you as a developer whether
you set that to true or false if it's
true then like we've you've probably
seen some of the other sessions like
when you use f12 or you're debugging
through code and you can go into the
base application Microsoft code if show
my code is set to true you can see their
code in all those places as well if they
set that to false you'll basically go to
the definition and it will step over
their code you won't be able to see the
code but you'll still be able to see the
procedure declaration or whatever you're
going into okay but if you
get a new client and they have
extensions from another partner yep then
then the client is blindsided because
they don't have the extension from the
previous partner right so you can build
on top of that but you can't
get that extension now it also depends
hopefully the customer had either the
code for that or otherwise
it's the same thing if they had a
that's up to the purchase agreement that
they had with the previous partner
whether or not they got the code for it
and that's something that's really
between customers and partners and we
can step in until
you what you have to do with your code
or how you have to sell it
so the show mind code dilemma I think
he's one we've all faced up to one of
the best suggestions I heard was
actually to move it so it's a property
on the object okay so effectively you
could hide if you have a licensing code
unit you could hide the code within that
and protect it but actually I'd like to
publish the majority of my code so other
people can work with it in a friendly
manner but having it at the extension
level is just too black and white why
can't we move that down into tables code
units yep no I don't think we would move
it I think we would add it there as well
so you could set a global on and then
set on a project that's a good idea
there's a question up here
and I had the possibility to developing
an extension with different communities
update for example I am I develop in
Maschine and I wish you 10 and my custom
I have a co 5
in on-premise installation
ok so you're trying to develop for a
different update than what you have code
for yes
so
to create shoe extension yep to version
of the same distinction okay no two
versions okay so if you actually need
two versions then if there's differences
between the C use that you're coding
against
you would need to create the two
specific ones coding against those
different environments based on the
changes that are there if you
can write one set of code to work
against both the contracts haven't
changed that you're coding against you
can code against the lowest one and then
it will still work on the later one as
long as it were no breaking changes also
I think we changed modern day it was
hard coding before against the app and
platform version and we relaxed that to
just be the major minor portion of it so
you in that case you'd actually be able
to code against the Cu ten and deploy it
against Cu five again as long as there
were no breaking changes
okay
very good question one
reason why we cannot republish actually
install an application a tenant
application on the BC live
because we have a customer on BC online
and we install the version of extension
uninstall it when try to insult again
and asked us to absortion it
so if it's the same package it's not
there were no changes to it made um it
should be able to be reinstalled done um
so let's talk afterwards I'll get your
information and we'll figure out why
that's not working that should work
they are expansions and I want to build
a condom and I gave
in the
configuration file all those extensions
is it possible to instantly extensions
if
one of the
all of the
extensions actually present
so to actually write the code if you
look at how es code is working when you
download symbols there's a dot vs code
folder and I believe that's where all
the simple packages get placed if you
have just the symbols you can manually
deploy that there and you can write the
code once you go to deploy the code
though you will need that deploy it on
the system because it will compile the
package again once this deployed to make
sure that everything it needs is there
and if it's not it will throw compilers
at that point
compile if I can copy the
conditional dependencies is something we
want it's not something we have
currently
in the ways
unfortunately okay I think there's one
more there and
if you try to look in the crystal ball
do you have an idea and
when the idea of your transformation
will be finished ten years something
else
so I think everybody has a different
opinion on that I think ten ten years is
good okay thanks
you're a nice you gave a date my answer
would have been yes I have an idea
okay thank you very much everybody
[Applause]
