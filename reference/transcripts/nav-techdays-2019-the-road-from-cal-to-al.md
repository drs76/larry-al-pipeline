# NAV TechDays 2019 - The road from C/AL to AL

- **Source:** https://www.youtube.com/watch?v=bRphFZEirMw
- **Video ID:** bRphFZEirMw
- **Channel:** mibuso.com
- **Published:** 2019-11-27
- **Duration:** 90m35s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

and in this session we're actually going
to dive down into a few of these topics
uh to a larger extent
than we present in the keynote but
before we do so
let's quickly take a look at today's
presenters in no particular order
yeah that's me
can you hear me my name is espenous
christopherson i'm an architect on the
compiler and tools team
in copenhagen
oh yeah that's me my name is weil uh i'm
on the application teams uh and i'm also
part of the security team in business
central
my name is alex soder i am the lead of
the team that is developing the air
language and
development tools and i've been working
with espen on
paving this road to al
yeah and i saved the best for last
that's me
my name is jesper i'm also an senior
engineering manager
on a team working on the system
application so that's what i'm going to
be talking a little bit more about later
so the road from cal to al now what does
that look like
well for some in this room the road
might look a little something like that
it's very well hidden under massive
amounts of lava glowing hot
it's hard to see like where to go
so mothers of you might be a little bit
more advanced you might sort of kind of
know you know how to get out of this
mess getting there
but where we really want this to go is
obviously this
straight road to paradise
now make no mistakes there are obviously
a few rocks that we need to clear out of
the way and that's why we're here today
we're trying to address some of these
rocks you know to pave the way into the
the new world of al
because as you say difficult roads often
lead to beautiful destinations
but it takes a little bit of effort
so a little bit more serious view on the
road from clt is probably something like
that
most of us start out with a code
customized solution in cil
that we all have in common
we also had that point of origin half a
year ago
and there are multiple ways obviously to
get to al the one that we're not going
to cover today is the one where you
completely re-implement everything from
scratch and just discard your old
solution that is an option but it takes
some heavy lifting and some investment
the more likely way that you're gonna
you know get to al is more like this
um where you start out by preparing um
yourself
for the move to al
now that al is in your language um vs
code is a new editor um the entire
extensibility model is something that
you need to kind of you know
slowly get into
so what we recommend is instead of you
know taking it all the way from the
beginning
is to start out strapping out a few
add-on extensions one by one trying to
submit a few event requests trying to
see how all of this works you know just
to get warm with the with the new editor
and the new entire development stack
however we're not going to focus so much
on that in this session because there is
plenty of good material out there
already there are some recordings from
previous tech days um and there's also a
lot of good learning material written by
some of you guys
um so if you are completely new to this
try to check out the net you'll find
lots of good material where we're going
to start is
how do you convert your cl solution to
al
so the big bulky thing that is left that
is now in cal how do you get that into
al
then up next we'll take a look at this
infamous system application that you
have heard a little bit about in the
keynote already
so what is the system application and
how will you uptake it
and then we're going to take a look at
now that you are in this new
paradise world of al like
how do you secure your apps
and and what other benefits can you read
when you when you actually made the
conversion so what's the benefit of this
entire uh
road
um before like i will start with uh
mentioning one related session
because what this session covers
is the move from seaside to cal
ncal sorry to vs code and al
and the change from the monolith
application architecture into a
modularized and extension
architecture and we're going to talk
about the latest additions to al what
we're not covering
is the actual code conversion and the
upgrade process
for that later today you'll have a
session called using docker and the
container helper to convert your cl
solution to an al solution which will be
by uh freddie and nicola
so that's later today at four o'clock
and i highly recommend going to the
session if you're more interested in the
actual lifting and how you go about
making this transition
i've been told there are whales and
crocodiles and mountains and stuff in
that session so it's probably a very
good one
so that sums up the agenda
i think we've spoken enough about that
without further ado
let's jump into the first one and now
we're going to ease on on the ease up on
the pink part for a little bit here for
a while so if it's like you know too
pinkish
he went from a white theme
so in the next 20 minutes
you will learn how to convert your
solution from cl to ale how to avoid the
common pitfalls and how to handle
typical errors that might arise during
the conversion
and
most of you will be coming from a
solution that is running on f 2018 and
uh earlier uh before you can start the
actual conversion process the first
thing you want to do is to perform a
technical upgrade and get your solution
running on the latest
business central uh platform from the
latest ceo of the spring release we
recommend that you do this step because
the tools that you need to convert your
solution will be getting regular updates
with each cu
these two seaside and txt 2 l will only
be available from this
in this
release
we also recommend that at this point you
perform an application upgrade and you
merge
the latest application available in this
eu and with
into your code base this has two
advantages first you'll be able to use
the
merge tools with which you are familiar
familiar for merging cl code and you
will also
decrease the difference between your
solution and the solution that we
released fully on ale
this fall
but before you we start with the actual
code conversion we should uh
make sure we're prepared then we bring
our other artifacts around along for the
right if you have a trans uh an
application that
is available in multiple languages you
probably have translations uh
for it
if
you have been using multi-language
properties in cl code such as caption ml
tooltip ml these will be extracted
automatically to translation files to
excel files and you will not have to
worry about them
if you have been using
non-utf8 translations or translation
files that are compatible with seaside
and which you can import you should
import them at this this point in time
using the standard tools translate
import command and make sure you compile
your solution before starting the
conversion process
this will ensure that
your translations will again be
automatically converted
when you convert the code
if you have utf-8 translations
that are used in
external txt files you'll want to do an
additional step here to
create some
helper data for the conversion process
you do this by calling the create
language command in thin sql which will
generate placeholders that we will use
later to convert your external external
txt files
once we're done with preparing our
translations we can start and
export our solution
while developing the conversion process
we've tried to
do two things first we wanted to
generate code that follows the all
coding guidelines
and second we wanted to make sure that
constructs that were not valid in al
were
properly commented out and
were
taken out of your
your way
on this the first step to conversion is
exporting to the to the new syntax and
you do this by either invoking the
export to new syntax command using finn
sql or by using the export nav
application object with the export to
new syntax switch this will produce a
txt format that is very similar to the
one you know
from seaside but has some additional
benefits that will help us along with
the conversion process so date and time
literals are in a culture in variant
form and not a culture aware format like
in seaside uh object references are
by name not by id so the code will be
more human readable and your your
developers won't have to know the 6000
objects by heart by id
yes and no literals will be converted to
true and false to match the new language
and we will also be converting keywords
and
method names to
have the proper casing so that your
your the resulting code will follow the
l coding guidelines
another thing that
will
the this step does is inject additional
information in the txt files to to help
us
better process controls and controls on
pages uh so one of these extra bits of
information is the type of the source
expression of a control this is
sometimes used to filter out to comment
out properties that we know made no
sense and i will
come back to that later when we talk
about typical errors
and probably one of the
the big changes that this step does is
assign names to controls and actions
uh in cl ids were the main point of
reference so developers sometimes uh
skipped giving meaningful names to
controls and actions on a page but in al
everything has to have a name
and
we use seaside as uh
we asked seaside for a bit of help to
get there
by generating unique names for all the
actions and controls on a page
and preventing
unwanted conflicts
and probably the last big important
piece
of transformation that happens here is
that all the identifiers in the code
get get coded
we so this is done here so that
the next tool can
more easily process the information
seaside already had the information
about all the identifiers it had and all
the properties so we're using it to to
push us along
once you're done with that you
everything that you have to do is called
txt2al and this will take the
you to use this tool you only have to
specify a source and a target folder the
source folder will have to contain the
txt files you have just exported and the
target folder will contain the resulting
al files
uh most of the defaults for this tool
are set up to to do a seamless
conversion but you can also optionally
specify a runtime
to better find to to fine-tune the al
that will be
emitted so that it matches your target
runtime now this runtime version here
matches the runtime property in app.json
and it's relative to the first release
of business central as a product so that
means that if you want to map back and
forth between the this version and
the version that you see sometimes in
the information page you add 11.
um
versioning is hard as you probably know
but
there are some things that you might
want to pay attention
uh to that are happening during this
conversion phase so the first important
thing is
going from donet declarations in the old
style in cl to the ale type of donna
declarations in cl for every variable
you had to specify the full
type name qualified with the assembly
name version and everything and we could
not
we did not want to do that in al so in
ale you define your references in a
single place where you specify what
assembly you're using what type you're
using and give it an alias and then
you're in your code you can reference it
by that
more human readable name
the txt to l2 goes over your txt files
and whenever it encounters a new type it
keeps it keeps track of it and generates
uh
will generate an entry in the resulting
l files
but
if you import other modules like for
example up taking the system application
those modules can also bring their don
and declarations and you might want to
avoid conflicts between the donut
declarations you're importing and the
ones that are generated in this step to
do that you can use the donna type
prefix
option
to prefix all the donut aliases that are
generated during conversions to avoid
any conflicts with imports from other
modules
so if we use that option we see that the
alias is now my xml document and
wherever this is used it will be my xml
document
um
this is important because xml document
for for your solution might not be the
same xml document that is
brought in by some other solution and
the compiler will give you a an error
and it's better to just avoid it
as i mentioned in the beginning uh
multi-language properties are
automatically converted uh to single
language properties so from caption ml
and tooltip ml we go to caption and
tooltip
and the
actual values are extracted to
accompanying excellent files
now if you have the external
utf-8 translations and you've run the
create language command you will want to
also
enrich the
emitted x-ray files with information
about
the
ids of these translations that were used
in seaside
and the ids that are used in the new
world this is just to make mapping these
resource resource files easier so if you
use ad legacy translation info
what will happen is that the produced
xlip files will contain an additional
note containing the id of the caption in
csi and you can take this id
and
you can use your existing
txt
translation files and create a map and
produce new
translation files that contain
information from both sources
another
tricky
part of code to convert
is the one is usages of control add-ins
control add-ins were basically stored as
data they didn't did not have a type in
cl and there is not enough information
in the cl code to do a proper conversion
the fields that were
used control add-ins only had a key that
was used to look up the information in a
table when converted to a l these become
user controls with the name and a
reference to the
the type mentioned there but the
compiler will complain that it does not
know what microsoft dynamics nav client
web page viewer is and it cannot find
the control admin with that name
to help with this you need to provide
the compiler with the txt2al tool with
information about what
actual donut type this add-in represents
to do that you can use the dot net
add-ins package
switch to specify a path to an af file
containing the declarations of your
donut types that represent custom
control add-ins
for example for the web page viewer we
would have a declaration such as this
one
where we specify the assembly microsoft
dynamics nav client webpage viewer and
the specific type and you can see that
the actual type that implements the
control add-in is called iwebpageviewer
and for the alias of the type we use the
one that we have already used as a
lookup in
in cell and of course we need to specify
that this is a control add-in
now
that's pretty much it you can now create
an app json add it to the root of your
project make sure to configure the l
package cache path to point to a
directory containing the system
and i i want to emphasize one thing here
this is the system app not the system
application app and as you all know
naming is hard and we
really
could not come up with a better name
here
said
um
once you do once you do that you should
also keep in mind to configure the al
assembly probing paths these are this is
a setting that tells the compiler where
where to look on your machine for the
dot net assemblies that your project is
using
that's pretty much it and now you can
compile
and if you do you'll probably see
something like this a few thousand
warnings and a few
hundred hundred errors
um
and you but you should not panic
the vs code offers help to navigate
through these and you can use the
built-in uh
built-in
filter to filter out the errors that
you
the compiler has detected
and you or you can use the command line
compiler and say
specify the error log switch and i'll
put all these errors to a json file that
you can use to
better divide and conquer the problems
in your uh
in your project
now
you might be asking yourself why are you
getting errors your solution has been
working for so many years why now
well
seaside was quite lenient and it allowed
you to write
a lot of sloppy code with al we tried to
enforce
rules that helped you write better code
cleaner code and
hopefully code that runs on the first
try and with no
surprises at runtime
what type of errors
could you might you get
well most of the time the l compiler is
trying to is trying to save you from
runtime exceptions
for example the al compiler will detect
if you have a case statement with
duplicate case lines and
we've all used copy paste
liberally and this is one of the the
side effects this was allowed in seaside
but what it did was just execute the
first case statement it found and
ignored the rest and we this allowed us
to find a few bugs in our application
while performing the conversion
the ale compiler ale compiler will also
tell you about
references to missing objects so in this
case we had an action that was
referencing a page that no longer
existed seaside would allow this it
would compile and then it would fail
at runtime in a new and mysterious way
another instance where we see
references to missing objects was in the
permissions property where where people
gave
permissions on tables that were not no
longer part of the application
the compiler will warn you about will
give you an error and the solution is to
go and just remove the the invalid
references
now you might be asking why are we not
doing this
during the conversion process where it
would require
full knowledge of your solution and any
references
that you might have and that would
require building another compiler just
for the
purpose of converting but we haven't
seen that many errors but it's good to
know how to react when you see them
another big improvement we've made while
switching from cal to l was the type
safety we provide when interrupting with
donet
we try to maintain backwards
compatibility while enhancing
the checks around type conversions
typecasting whenever you uh pass the
donut value to another and we've seen a
few instances in our application where
the type of a variable or parameter did
not match at all the type of the value
that it was passed in
the l compiler will warn you about this
and the solution is to figure out what
are the proper types in some cases this
code worked only because
both types had one common method and
that was the only one that was called on
that code path but if somebody else
tried to touch the code it would have
thrown a runtime exception and people
would have been left scratching their
heads
probably one of the
big changes we've done with
in the air language and which we hope
will uh help us evolve the base library
and the the system
the built-in
collection of methods was how
symbols are resolved so whenever you
reference
a method
or a field in al
the compiler will start
searching for it from the innermost
scope going
steadily out
in this case we were
referencing the evaluate method and
because there's another evaluate method
in this object it tried to resolve to
that and the real compiler would say
that it could not find it could not
resolve this method
now
seaside on the other hand has some
random luca patterns for for symbols it
might look at the global scope it might
look a local scope you really have to
spend a few years of figuring out all
its secrets we try to be explicit
and
we think that this will help us extend
the base library so for example if you
have a method called foo in your code
and
in cal we would have introduced a method
called call fool in the system we would
have broken your code but no longer now
your foo will be used uh independent of
whatever we do
another great uh feature that seaside
had was around donna types with events
whenever you set the with events
property on uh on a variable of type.net
stubs were created for all the events
and
you could code it and then if you set
the property back to false the code was
not deleted the code was left in the
background because maybe it was just a
mistake and you did not want to lose
your code now this means that during the
conversion process this code comes along
for the right and their compiler will
tell you that there's no uh the that the
variable being referenced doesn't have
the with events attribute
the solution is in this case is to
simply clean up the the code and make
sure that you you're not losing any ip
now another great great feature that of
seaside that what has been causing a few
problems during the conversion process
was its great copy paste functionality
you could take a field and
copy paste it all over the page
now properties that made sense in the
initial context when for example the
field was of type option
did not do not make sense in the new
context when the field type has changed
or some other properties have changed
dell compiler tries to make sure that
all the properties that you're using
make sense and will lead to good runtime
behavior so if you try to use an option
caption on a very on a field of type
text it will tell you that that's not
possible and the solution in this case
is to just delete uh the property ins in
certain instances we by using the
implicit type that we've seen earlier we
can
try to remove some of these properties
but that's not always possible because
the txt2al
tool needs to work with pure txt files
and does not have all the
possible information
and decimal places was another property
that was often left be behind them you
will have to remove
another
important check that the compiler does
is ensuring that the signature of
subscribers and publisher must match
exactly this is done to make sure that
the code that you've written in a
subscriber actually reflects what the
publisher will be communicating to you
and that the developer just that is just
looking at the subscriber does not get
the wrong impression of what that might
might do
we're also checking that
methods annotated with special
attributes such as hyperlink handler
have a signature that matches what the
runtime actually exposes seaside was a
bit lenient there and it could allow you
to have variables that were
of slightly different type
and this could result in unexpected
unexpected runtime behavior
i think we only found one instance of
this but it's good to to know sometimes
seaside inserted special conver
conversions in place you would
at least expect so for example the data
caption expression is of type text
but uh it was possible to assign the
to assign a value of type date
or of a different type and seaside would
insert a magical two-string conversion
behind the scenes we think that this
behavior should be explicit and you
should be aware of what's happening
there
now one of the smaller issues that you
might encounter is attributes that
should be used in tesco in test code
used outside of a test test context
the solution here is simple just remove
the offending attributes
another
interesting check that the compiler does
is verify that the all the handlers that
you specify in the handler functions
attribute are present within uh within
the object this ensures that you do not
get runtime uh exceptions or that your
tests do not fail because a handler was
not found or
was not executed
and now for
errors that were a bit more subtle
in certain cases for reaper columns the
the compiler will generate
additional entries in your data set so
for example if you had a column of type
uh
decimal i believe
it would generate another
column in the data set called format
with the name of the column followed by
format and this could lead to unexpected
behavior during runtime the al compiler
will warn you will give you an error at
compile time and it will instruct you to
change the name because the name is
reserved
and i don't know how how many of you are
familiar with this uh this special trick
do you know if we're referencing a value
an integer or a string there it's
so what's happening is that the the
option type allows you to use the column
colon syntax to reference a numerical
value within uh codes so you would think
that this is an identifier but in a in
it was actually an in integer value
we think that this will lead to
confusing codes so we do not support
this in al and you will have to
validate to verify your code and you
should not be having numerical values
anyway
one of the
the limitations that we've introduced in
al while looking towards the future was
a limit on the length of identifiers all
identifiers need to be at most 120
characters we enforce this limit because
we want to expose these elements through
refl through reflection reflection by
the means of virtual tables with which
you might be familiar though
familiar with
uh now seaside automatically generated
certain names based on content so if you
had a label it would take the whole
label text which if it was a paragraph
of law could be quite lengthy and
converted that to a label name the
solution in this case is just to give it
a more human-friendly and also
compiler-friendly name
and
going back to our our our path of
conversion we i have our cl solution
running on uh
business the latest business central
spring platform
we have converted it to l we have an al
solution
we try to compile it and we'll get
compilation errors
now what we recommend here is that you
go back and fix it in cl
this will ensure that your existing
customers will benefit from the
errors that the l compiler has
discovered and it will also help
help you maintain that solution for
longer
now of course at some point you
will convert to ale
you will get the real solution you will
compile and success you will have
a solution running on the latest
platform from
wave 2.
now back to translations because we said
we had some additional information that
we want to bring along for the right
multi-language properties are converted
not new tfa translations are converted
and now for utf-8 translations that we
could not introduce into seaside we just
have to run a script on the txt files
and the xle files that the txt2l tool
has produced and you will get
them merged into a xliff file that
contains all the information needed to
get up and running
now
you might also want to consider
converting your profiles and
you should really think uh
how much of them you should convert
and especially looking at
existing profiles it might be difficult
to understand from them
what they actually did and i think it's
one of the examples that xml is not
really a human readable format
but thankfully in al profiles are
first-class citizens so no more fiddling
with xml no more pain pains during
upgrades everything will be compile time
checked
and with the wave to release the profile
object has received new properties
uh well the description property was
already there but now it's explicitly
just a developer comment like it was for
all the other objects
you now have a caption and a caption ml
the caption can be used with extra files
caption ml can be used directly in the
code and this allows you to translate
the string that appears for your profile
a profile description can
also be translated and it shows up in
the profile
window that we've seen in the keynote
and you can also decide if the profile
should be enabled or disabled by default
these properties are overwritten in the
background whenever you switch the
in the web client you if you switch the
profile from enabled to disabled it will
create
some mail code on top that will override
this property
and you also have a property called
promoted that will
make sure that the profile is visible in
the
in the
role center explorer
now
we get this question a lot and
to understand why this is
so
we have to go back to the time when
seaside was created when your
workstations look like this
and half of our developer team look like
this
and uh
you need we need to understand the
changes that have happened to compilers
since then and now
compilers have gone from simple programs
that to which you give a simple file and
they give you gave you back a cryptic
diagnostic you spent another half an
hour trying to fix that
uh two
complex pieces of software that
um
complex pieces of software that sport
intellisense go to reference final
references and much more
to support all that we need to keep uh
dale compiler as well as the c-sharp
compiler keep an in-memory state of
your solution and constantly update it
so you are paying for all the features
that you get
now if you want to
trade some of these features for more
performance or more responsiveness on
your machine you can disable some of
them such as code analysis
code lens
code actions and or you can enable
incremental build which will reuse some
of that in memory state and of course
you can use red for
faster development
and that's pretty much it
all right
if you could get your machine to work
again that would be cool
yeah so that was a little information to
take in um
let's switch gears a little bit slower
here
and look at the system application
we're back to the pink theme by the way
so the uptake of the system application
now how do you get started well really
that's one small step for a developer
all you need to do is to add that
dependency
and then that's a giant leap for
oh hang in there
when you do that you will be broken
so a natural first reaction to like
being broken is of course why would you
do that
some others in this room might ask
dustin
again others ask
you i know
or some other languages that i will not
try to
even get started with
and
allow me to apologize for that in the
beginning
of course we know the uh it's it's
always a hassle to get broken
and we do recognize the pain that we're
inflicting you um
when we break you
but there's actually a good reason for
why we did it in this release and i will
try to get back to that and explain a
little bit in more detail
what these reasons are
so really um the system application
builds upon this quote or one of the of
these like you can't build a great uh
building on a weak foundation you must
have a solid foundation if you're going
to have a strong superstructure
so really what we're trying is to
reinvent or like recreate a foundation
upon which you can develop the business
applications of the future
now why would we be doing that now why
did we think this is a good time to
start embarking on that mission
well in order to explain that um i'll
like
try to
explain a little story here
so we'll turn back the time to the year
2016.
um
when everything was an on-premise
business there was no cloud on the sky
if you get that one so
nav was running on local boxes you guys
would go in you would code customize it
to fit the the customer's needs and
everyone would be happy
now that was all perfect
until that spring day in 2016 when these
clouds came along
[Music]
so this was not just a disruption you
know for
business central but for the entire
industry microsoft of course also had to
react to this new trend with cloud
computing which is why we came along
with the cloud first mobility first
mantra
now that really meant that you know
things were about to change
we had to take dynamics nav and push it
into the cloud
now our first attempt was how should we
put that
interesting
as nav in the way that it used to be
wasn't really capable of running in the
cloud
so first of all nav building being built
on a code customization model
was really really hard to build upon
being in the cloud you need to have
similar code you can't have every single
cluster running some code customized
solution so what you need to do is you
need to switch from a code customization
model to a code extensibility model
right
um and then you need to build on top of
the the solution that that we are
developing now that was kind of hard
still is a little bit challenging
it was also rather hard to evolve
the product as a
you know we didn't have the right
language constructs with the seaside and
with cal it was very hard to to extend
the language to actually
evolve the product into being a true
cloud solution
so that's also not so good
then also switching to the cloud means
also switching the maintenance model so
we will be going from a model where you
guys would go out and help the customer
and fix every eventualities to a model
where actually microsoft themselves have
to we have to go in and and operate in a
devops model where we operate the
solution ourselves
again nav not the strongest suit and
last but certainly at least nav has
always been an expert product um
it was built by experts and then
explained to people that become experts
which is not really the cloud story and
clouds it's often you want people to
just walk up to the solution fall in
love with it and then you know live
happily ever after
it's not really what a navy
was the strong suit of navy
so that's why we had to change
to become business central
and now this release is really a
milestone in this journey going from nav
to business central
um
one reason obviously
that we are now only have one client you
no longer need to think like how does
this work on the wincline how does this
work on the web client there is only one
client to develop for and that is the
experience that you strive to make
excellent
also
there's no longer
different languages different
development environments it's all al
it's all visual studio code
so that obviously provides a much poorer
platform
to develop for the cloud for
and also all of this now enables us to
start componentizing to start extending
which in the end is
what why we decided that this is now the
right time to start rebuilding
the application from the bottom up
trying to separate the business logic
from
the system logic
by separating these functionalities out
into small modules which then will make
up the system application
now with all that talk about modules
what is a module i'd like to
add a few words to that
so basically
a module is just a set of objects
so there's nothing fancy about that
the difference though being that these
uh the functionality within a module is
functionally coherent so the base app is
like one big mess of all kinds of
functionality right it's hard to
describe the purpose of the base app
that's different for a module a module
has one purpose and one purpose only
so the first thing the first property of
a module then is
that it's coherent
so how do you reach this coherence well
really you just take the subset of
objects out of the base app
put in an extension of its own and there
you have it
so why didn't we just call it an
extension well because it's not really
extending anything um it's kind of like
the bottom layer it's like small cute
modules and also there are other
properties to a module than just being
an extension
for instance
modules encapsulate complexity so that
means
you will not be able to access the
internal implementation of a module we
do that by using the new access
modifiers so the implementation will be
marked as access internal
so if you're in a different module or in
the base app or in whatever solution you
will not be able to call the modules
that are inside
so that of course
you know gives us flexibility going
forward because now you can go into that
module and change the underlying
implementation or maybe move it into the
platform or do whatever you want with
your internal internal implementation
to your likings
but then how do you get access to the
module well obviously
we need a facade on top of it the facade
is the public api that's the one that
you guys will be calling
and that's the one thing that we cannot
change
and now that facade in order to make it
you know easy to understand will be well
documented you'll find xml code
documentation in the facade
um which then allows you to understand
what a module does
and you don't have to go into inside the
module actually read the code as it was
before
in in cil
so quick deterrent to access modifiers
as these are quite crucial to the
concept of modules
you just specify axis internal
the definition is that the axis property
is an access modifier which allows
controlling the accessibility level of
methods and objects
all right
you can set those on object level
public being the default which is as it
always has been but now you can also
make an object internal meaning it is
only accessible within a module
extension
you can also set it on the field
function level so you can declare a
function to be internal meaning it is
only
again only accessible within the module
it can be local only within the the
object or it can be protected which
means
that it can only be
referenced within the module
or in the x
in the table extensions page extensions
so these are the new um access modifiers
use them wisely
then there's one more property i'd like
to point your attention to which is also
new it's the extensible property it's
pretty much self-explanatory it tells
you whether you can extend a table slash
page or not
now when you're creating new modules or
extensions you need to think
extensibility into the design
so while anyway doing the effort of
ripping things apart
try to pay attention that you know
should this thing be extensible or not
every once in a while it might actually
be a good idea not to make it extensible
it's not always that you want people to
go in and fiddle with the internals of
your
of your implementation
but if you make it extensible then try
to think it all the way through do
provide the right events do provide the
right interface um yeah interfaces
and that property has a set works on
tables pages and now also enums
so the advantage of modules we already
touched upon in the keynote but i'm
going to sum them up here again they
separate concerns
they have stable well-documented apis
and they encapsulate complexity
also they have a smaller attack surface
meaning it's much easier to do security
analysis on these little modules rather
than having a big wide open bulky
app
they're faster to compile which is very
very nice so actually the entire system
application with its 50 modules
takes a couple of seconds to compile and
publish so the development experience is
a very different one than if you're
trying to compile
the base application
also this is extremely important
their clear size and purpose allows for
code contribution model so every single
module that we're creating is going onto
github
you can go in you can create pull
requests we will happily accept them
and as it was announced in the keynote
you can now also go in and create
completely new modules i'll talk a
little bit more about that in a minute
but everything that we do we're trying
to do as open as we possibly can so that
you can chip in with with
with your needs
they're also easier to performance
monitor and they allow for individual
versioning
so
um that with these modules in place now
we could start um
creating the system application
basically what we've been doing is we've
been extracting one functionality after
another out of the base application and
then made the base application depend on
that module
all these modules together is what we're
calling or referring to as the system
application
so the idea basically behind the system
application is we are trying to get out
of your business
so
the the place where you make your money
is uh with the ip in the business
application maybe not so much in the in
the in the things that make the system
work so by getting out of your business
we won't be stepping on each other's
toes which is the idea here and that we
will
continue to do
so um that was the introduction
now let me jump into github to show you
what's out there
all right that's big enough i guess
so basically on github let me zoom out
just a little bit
you'll right now find two folders it's
the add-on folder where you'll find all
our add-on extensions
and then you will find the modules
folder
now in the modules folder
no surprise you'll find our modules
there are again some folders a little
bit of a folder structure here
every single folder ideally has a readme
which describes the context that you're
in in that folder so for instance now
that you're in the modules folder you'll
find the properties of modules down here
in the readme
if we now go into the system folder this
is where the system application resides
at the bottom
you'll find a diagram of how these
little modules individually
reference each other and what the
purpose of the system application is
on top of that you will then find all of
the modules that we've released so far
those are updated regularly we try to
to make them like as current as possible
so let me try to go into
into one of these modules just to
describe or to show you what that looks
like so for instance going to
cryptographic management
um
this one holds well here we go
here you have the readme well this
module provides helper functions for
encryption and hashing
and so on and so forth
so first there's usually a little
description of what the module is for if
you just want to quickly understand what
it does and then further down you'll
find the api documentation
so for instance
the cryptography management code unit
has a function called encrypt that one
returns plain text as an encryption
encrypted value and this is the syntax
so this you'll find for all the public
apis in the modules so you no longer
have to go in and
look into the gory details of every
module you can just read this and you
would understand what a module does
now going forward of course we will also
at some point have this in vs code so
that you when you hover over a function
you will see you know these descriptions
but we're not quite there yet
but it's in the making
so if we take a little closer look at
the source code in here
um
let's take a look for instance at so so
usually you'll find
two flavors of code units one is
suffixed with impulse that's the
implementation now the reason why we
call this implementation is because
these are hidden inside the module and
you will never reference them so those
didn't need to have the pretty name
whereas the ones that are in the facade
are the ones that you guys will be
referencing so those got the nice names
so if we take a look at the cryptography
management code unit here
i can zoom in here you can see that this
one has public access because this is
our facade
and then all it does is kind of
reference into the implementation
with a nice documented public api
so that's what a facade looks like and
that you which you will find in just
about
every module that we have out there
if we take a quick look at the
implementation code unit
this looks a little bit more something
like what ux what you are used to see
like a lot of code undocumented uh
yeah
goodness like you like you probably have
seen it before
um but this again i mean of course if
you want to understand the internals
then you can read about that but else
you don't have to anymore
now interesting about this module is
actually that we've received the first
pull request um by one of mp's gonna so
he said like i need this raindale
cryptography functionality as well so he
made a pull request for us
where he added this facade where now you
can have a render provider and do all
the encryption there
so again if you guys have similar
missing capabilities in our modules
please do feel free um
just submit a pr and we'll be looking at
it and and you'll probably see that in
your in in the product in a
within a couple of months
there's one more thing um we are going
to retire the cl open library as it's
not so it kind of competes with this so
if you want to going forward have.net
wrappers
you can just create them as modules
i will be blogging about that very soon
i haven't gotten around to it yet but i
have for instance made the first
little module that is basically just a
wrapper
this is the math module so if we take a
look at the facade here
so basically all it does is that it
forwards the call to some dot net
because in the system application
obviously we have dotnet access in the
higher layers of the application we
don't so if you need some net stuff
and you would like to you know have it
added to the product feel free to feel
free to create a module um
and reference that
um
so one last thing while we are here on
github
there is a breaking changes document
that i would like to point your
attention to
now when you've uptaken the system
application as i said
we've made some some
some changes which will break you
some of them might be as simple as that
we've renamed some code units
um i'll explain why we did things like
that but you know the fact is that there
are some there are some some breaks um
but you can go into this breaking
changes document and just search for the
error and you will find uh the solution
so for instance if you stumble over an
error saying assisted setup is
inaccessible due to its protection level
well that's because it was made internal
um
then the solution is use the appropriate
api methods in this code unit instead
and so on so forth the list is quite
long as you can see well it's actually
very long and it's getting longer by the
day because every like this is again on
github it's an open document so if you
stumble over something that isn't
documented in here by all means please
make a pull request and add because then
you will help the entire community
you know resolve these breaking changes
yeah so that was on github
so speaking of breaking changes
why did we not do like why did we not
do non-breaking changes like we promised
in the keynote today and like we will do
going forward why we did not do it like
this in this release
well that is because ensuring backwards
compatibility through deprecation is
costly in slow stein progress
considerably now that as such is no
no problem i think some of you might
actually really would like to see us
slowing down a little and
you know take a little bit easy
but in this case it was a problem uh
because the system application needed a
critical mass to establish itself itself
if we'd come with like three modules and
say like hey look at that that's our
system application you've got three
modules
um nobody would care i would probably
not be standing here talking about it
and chance's other system application
would just die a silent death so we
needed to somehow you know establish
this thing and say like this is where we
want this to to go and you know
and then this thing will become a
self-runner
it's also the new model um that we will
have to work under with these side by
side implementation so we retire some
old functionality in the base app and
then we create a new module which
competes with the functionality
um
it's quite complex and also we need i
think a few more uh
language support a little bit more
language support to make this happen
properly
um
so this is why we kind of you know now
going forward we will be able to add
these because now we're in al and we can
evolve the language much quicker
um
but that will then allow us to do this
side-by-side implementation this is
rather hard at the moment i would say
and then also of course we wanted the
modules to be clean proper examples for
you to follow
[Music]
so yeah that's why for instance
sometimes you know when a name in an old
code unit was camel cased we actually
did rename it and it's annoying for you
because now you have to go into your
code and you have to rename that code
unit you know to be not camel case but
there is a meaning behind the madness we
really wanted these to be shining
examples of how our modules are in the
future
so how do you participate or request
change really there are only two ways
left
you can go to github microsoft a lab
extensions and then you can submit your
pull request you can ask questions
whatever you like will be listening
there
and you can go to bc ideas if you don't
want to do it yourself this is a little
bit slower progress um you can you know
put an idea up there then you can have
your friends voted up
and maybe at some point we will pick it
up for you
but it is important that you let us know
what we should focus on next because we
will no longer just for the sake of you
know architecture we will no longer
extract modules it will be customer and
partner value driven
so we need to know from you what should
be the next thing that we extract as
modules
we won't be doing it for the fun of it
that completes the
system application
all right
does my microphone work okay cool so uh
now that you're going to be writing
extensions from now on
uh i want to talk to you about uh
some tips that will actually help make
your extension more secure and we
absolutely follow these steps when we're
building extension internally in
microsoft all right so
let's start with the first thing
data so where do you store your data
obviously in a database in tables right
that's
all right if you are dealing with
non-sensitive data and the reason why
is
if you are building extension a
and basically you access your database
you access the tables you know set
delete get whatever for for for records
um and that worked great right but you
have to understand that if someone else
is writing extension b they also have
the same access
so
what if you have let's say some
sensitive customer data so your
extension will collect some sensitive
data for example just an example some
social security number or credit cards
and now you would prefer if you can
isolate this data and only your
extension will access it right so
theoretically it's going to be something
like that so only your extension can
isolate can i can access this data
so how can you do that
luckily
we have a feature in business central
called isolated storage and that will do
that exactly it will offer total data
isolation between extensions right
so how can you actually use it so first
how many know about isolated storage
great
after this all of you gonna know about
it right so it's really simple to use as
you can see you have setter and getter
and you can even set
the value as encrypted
and you can check if the secret exists
or not right
and if you can see in the function call
we have something called data scope
so what is data scope basically
you can add on top of the
extension isolation
to make sure that
you have extra scoping so for example if
you set the scope to a user it will mean
that
when you when you store the secret and
isolated storage or sorry your data in
isolated storage only the current user
will be able to retrieve it right and if
it's a company then only the current
company will be able to retrieve it and
you can even merge and have it like this
company and sorry this user in that
company would be able to retrieve that
data right
and bear in mind no matter what scope we
use the data is also is
specifically isolated to your extension
all right
okay so now what about secrets what if
you have your own secrets
so where can you store that
so
i will definitely say you need to use
some secret store like azure key vault
so i'm building extension a and now i
want to connect azure key vault
i will need to use some credential for
my let's say i created the service
principle and i would need to connect to
that so i have the credential how can i
do that
so
would you hard coded in an extension
i recommend against that so don't hurt
code secrets in the extension and we can
talk about that after the session as
long as you want
so
where would you store it so the first
time you're setting up a tenant or that
extension in a tenant
you can manually add the data and then
have
a page like let's say a setup page will
go and store that in isolated storage
which means that this secret is going to
only be accessible to your extension
right so
now i wanted to build like a small
prototype to see how would that look
like
so
let me switch
so
i will show you first
what i did and then we can take a quick
look at the code
so if i go to custom
so i created a demo page
and in that demo page
i had two actions
first one will open a setup page
and if i open my setup page you will see
i have
information i would need to connect to
azure key vault including the key vault
name and the service principal crits
right
obviously i'm not going to enter this in
front of you so i did it before the
session
so let's go back
and i had another button that will
basically go fetch a secret from azure
key vault and if i click
you can see the secret one all right so
for people that have trust issues i have
my azure key vault right here and i have
my example
secret so let's update it now
so
[Music]
come right now all right
so if i write the value here you're not
gonna see it so i'll just write it here
and and paste it there okay so let's say
now
take days
okay
so before it was secret one or test
secret one so if i paste it here
great
now let's me let me fetch the same
secret again
and that's actually like using azure key
vault in that scenario is a great way
for you if you want to rotate secret
update secret for external service it's
always great because if you can have
like let's say 100 tenant that are you
know fetching data from the key vault
you only need to change the data in the
key vault right
and let's take a quick look at the code
so basically this is a page that has two
test actions
or sample actions
and i had this is my setup page and one
great tip when you have a setup page
is that you don't want to store the data
in any tables i would totally recommend
that you don't use you don't base it on
a table so just have some variables
and have the field point to a variable
so client id for example is just a text
variable that you can see down there
right
and
it's really simple because i was using
rest api to connect with azure key vault
so all i needed is to get a token using
my credentials and then just basically
get the secret right i will publish the
coding github so you can have the sample
code if you want to use azure keyword
from now on
and yeah and i have the sample code
units for using isolated storage that i
showed you before right
okay
let's go back
so you are in a prototype or design
phase it's really highly recommended
that you will do a threat model before
you go and finish your extension
so why would you do let's let's talk
first how can you do a straight model
so
you would try to gather your team
and people that have some
knowledge in security
and you will try first you will build a
data flow diagram for whatever feature
or extension you're building right
and then you gather as a team and you
try to look in in that
data flow and see
if you have any risk or threat that
might might might happen when you have
this extension in production
and then later on you will try to
mitigate it and try to validate the fix
so why would you do that yeah
you will potentially fix all the threat
and risk before actually going to
production so that would be great and
you will increase the risk awareness and
understanding in your team
so
uh in order to give you a quick example
i was trying to build the threat model
for what we just did for that prototype
so that's me
i wanted to build an extension
and i have
my service principal creds
and of course i'm not going to hard code
them so i created a setup page the setup
page will go store them nicely with
storage
and then
later on i want to get that secret
uh so i get the secret for myself
storage i
try to create some functions that will
basically go get
the secret from azure keyboard and then
now that i have the secret i will use it
to do whatever i want right
so
bear hold on
so
i want to just give you one tip that
vincent talked about earlier and also
esper
basically procedure scope or access
modifiers
uh
you have to know that in and by default
in al procedure are external which mean
any other extension that will take
dependency in your extension
can actually call that
so
you have to mark any any any extensions
that deal with sensitive data or secrets
as internal so if i go back to the
threat model that i just did and now i'm
in with like with my team and someone
will point out hey you have a git secret
function and if i build an extension b i
can actually go and get your secret
and this is not safe
so what would i do
i will go back and i would add to my all
like all the sensitive function the
internal scope as you can see on the
right
all right
moving on so now that you have your
extension you're happy with what you
build
and you know you want to submit that you
have to understand to protect your ip
there's a magical property in app.json
called show my code true sorry show my
code all right how many of you know
about it
great all of you should know about this
one
because by default it is false
and if you set it to true this would
mean that any other extensions that will
take dependency in your extension can
load the symbol and can lock through
your code
or while debugging they can actually
debug into your code right
and if you're fine with that that's
great that's fine right
uh also you need to know when you
compile the extension you create a dot a
file and that dot a file
contain your actual code it's an archive
file so anybody can open it with any is
any like you know 7z or whatever
so if you want to distribute an
extension
you need to make sure
and you don't want anybody to look into
your extension so you need to create a
runtime package and if you're my if you
have show my code as false it's not
going to include any al code it's going
to be runtime code right
and you it's just like one liner which
basically you just invoke
you can try it on your docker machine
and yeah this is the link for how you
can do it
so
my last tip for you
if you decide for some reason to mark
show my couch you're feeling the open
source energy and you want to share your
code with everyone else
but you still deal with some secret or
some sensitive data
there is a decoration for any function
or a variable
that called non-debuggable which means
that when someone is track is trying to
debug on a sandbox they cannot look
inside your
view extension secret right so that part
of of whatever you mark would be skipped
during debugging right
okay all right thank you
so
after the move i mean i'm so glad that
we actually are here now because i've
been working towards a complete
al stack for the last four and a half
years
and one of the reasons
why this has been so important for me
and for a lot of other people in
microsoft
is that we will it will allow us to
evolve the language to provide better
extensibility in the base app
and
some of the things was actually what
winston showed in the keynote
so
first of all don't be afraid it's not
turned on and even if it were i would
probably not be able to find a place
where i can could get any picture
developed from it anymore
and actually that's
this camera here is most likely an
evolution over a number of previous
iterations
and you can continue to do that for a
while but at some point you need to take
a major leap to move forward
and the major leap year for us has been
to move the entire stack into ale it
allows us to
be more efficient in evolving the
language providing new constructs
without seaside holding us back we have
had the feeling internally for the last
couple of years when we are trying to
make the base up more
extensible
it has been holding us back caesar has
prevented us from
from moving forward as fast as we would
like to do
so
this is basically the example that
vincent showed
and
there's a number of very important
points around this
is interfaces which in itself provides a
new
excellent way of
adding more extensibility for us in the
base app and for you in your code bases
but it also
is coupled with the enum extensibility
which is also something that we have a
ton of requests on and we have been
dragging our feeds a bit
in actually uptaking that in the base
app and one of the reasons is actually
that we have a ton of code which is
basically
if enum is full then do something and
then if not anything else just throw an
error
and we will have to go through all that
for each of those enums that which our
options will change into enums and make
sure that all of this is extensible
but how would we ensure that we
first of all get all of them and make
sure that it's easy to extend upon
because if we just
used i mean the one tool we actually had
in the toolbox which is an event we
would have to free genome probably spray
a huge number of events
all over the base app you will have to
just to subscribe to all of them and be
sure that you get
everyone
and if we add a new one in some place
where we use that option in the base app
would also have to know about that
this is something we have tried to solve
with this combination of interfaces and
enums
first of all using an interface it gives
a semantic name to all the places where
we would use it for a test
one example is the has launch access i
mean rather than having a
if loyalty equals gold we would actually
have this specific
if statement is all about whether the
member
would have launched access
another important part of it is that
when you actually extend it
you will have to supply
implementations for the places
and we can tell you about it if you add
an
enum extension and you don't
actually implement an interface and
supply it we can tell you
this is not going to work because we
rely on you to reply this as well
so it's
we think this is a very good way
to evolve our extensibility story i have
another example here
which is basically an imaginary shipping
provider we don't have anything like
this yet in the base app but this is
some way we could actually imagine us to
implement it
i would start by creating an interface
it would have a method that could be
configure allow me to configure this
specific shipping provider
this configured basically
how i set it up or not
and then then a number of other methods
that relates to this particular
piece of code
i will then create an enum
a shipping provider enum
and the one we may provide if we don't
provide any other implementation that
base would be like this
it will contain a non
value basically saying
select one and if there's no one present
you can select from well this is it
and it's extensible
so
our implementation would probably look
something like this configure
throw an error is configured false
and then empty implementations it's not
going to do anything
the beauty about this is i mean the
setup part of it for a default shipping
provider that could be something like
this
a simple table two fields
basically and not used primary key
and then just a default shipping
provider which is of this enum type
so
whenever i use it i can basically uh
look up my configuration i can cast my
default shipping provider enum field
into an interface and i can start using
my default provider
so the configuration page could look
something like this basically
showing only one simple field default
shipping provider
persisted
good to go
so
and then
if you or
someone who actually have a shipping
provider service this care my in this
case my imaginary land c and air
shipping service
will come along
will create an enum extension adding a
value for my specific provider
and i will point to an input in
interface implementation which will be
the lsa shipping provider interface
or implementation of the i shipping
interface and in there i will have the
ability to provide configuration i can
figure out myself how to persist it and
i will probably
end up having some implementations of
which calling are calling my external
web service
so
this is
one
of the ideas of how it can be used
there's probably many others i think we
will see a lot of
new ways of doing extensibility using
the interface
i'm super excited about that
i think it will be a great addition to
what we're already doing
so
obsoleting objects
vincent talked about it
i think he just also mentioned that a
bit so
this is basically a way of us to
warn about
changes we're going to do and give you
good time to
react to it and
adapt to an improved base app
we have added obsolete to
to all the
all the objects and
all the extensible
object elements
and we have also it's also an attribute
on procedures and variables so you can
mark them
still
we're not removing fields yet from the
sql they're removed from the schema so
we don't care about them anymore but
they are still in the database but we
plan to
fix that hopefully for the next release
so
demo
i will switch over here
so
this is visual studio code you know that
and i have already opened my demo
workspace here
and i'm not going to say a lot about
workspaces projects and dependencies
except for it's actually mo works as you
would expect almost all the time which
is super great
and and what i can see here is and i
actually have a code unit here that has
mirrors in
so i can quickly navigate to that
and i can see in here i have a bubble
sort method and we all know
it's not the most efficient one
but apparently i like some variables
here
let me just
that
it's an integer i have json
hold on wait a minute this this looks
silly
let's see if we could do it like this
instead
so
oops
this looks better
so
small nice addition it for me it
compared competes a little bit with
interfaces because i have loved to do
this for a long time
so but actually bubble sold
it's not the most efficient one so let's
get rid of that
so i want to obsolete it
obsolete
that
and
here and this is where i say it works
most of the time
there's more delay
actually
without deploying and getting new
symbols
my sword app which consumes the bubble
sword immediately gets the uh bubble
sword is marked for removal
and i think i would say use
quicksort
instead
so
you can see how it works the project
dependency part it's super nice to work
with
and a part of it is actually also that
we can deploy
multiple extensions at the same
time and it will uninstall and reinstall
again if you deploy a base and you have
something on top
super nice and saves a lot of time
so
let's
look at another demo here i will just
close this and this
i have created my better customer list
report here
and
created a layout for it
and i would actually like to
substitute
the
built-in
customer list with my version which of
course is way better
and i
remember last year alex presented a new
event
that allowed you to substitute a report
and
even though i was actually presenting
with him at the same session i cannot
really remember what it was called and i
can definitely not remember which object
it was in
so
instead of going through all the base i
can figure that out being an engineer we
decided to do it and do it in another
way so we have added a way to pick enums
so there's a new shortcut
saying shift alt e
which gives you a list
of all the enums defined in all my in my
current module and all the references
and i what i remember from the session
yeah last year was something about
substitute
let me see
it's this guy here
so let me pick that one
and it inserts the
subscriber for me so i can just fill it
out
super easy
this and i can substitute it with my
better customer list report
this is
the demo part
let's go back here
so just a reminder
we have created some stickers we have
noticed that a lot of people put
stickers on their laptops and rather
than fighting it we have tried to
embrace it so we have brought
a lot of stickers they will be in the
booth
down there and if you for some reason
have a
laptop from a competitor or something
like that i mean get a logo slap it on
right center
and remind everyone that you are proud
al developer
who builds business software that
actually helping real businesses to
thrive
and
there's a session tomorrow
just a little bit of advertising because
i mean it i have brought a lego robot
and then i'll try to convince it to
dance on the command of business central
so if you're interested in that join
that session
and i think we have a few minutes left
for q a
so
if
anyone has questions
now it's time
first one to ask with a t-shirt
goodie
which one first the mic or the t-shirt
so this is working yeah it's working so
i was wondering do you plan to extend
the feature of the interfaces for
some kind of i can pass in generic
object
we plan to evolve it
right now
we
use it as a
foundation for
the enum extensibility
we will evolve it
but right now we focus on
a plain simple interface put on code
units for methods
i
think
just one question
sorry one
interface
uh so one code unit can implement one
interface only
correct implement multiple
because all the examples currently that
have been shown is
one code unit one interface one code in
one interface yes but you can implement
as a list so you can implement more than
one so then there's no question because
my question was about so what about
licensing so do i have to create
buy additional license just to implement
every single interface oh it's a
licensing question
oh yes related to the code units yes you
can implement
more interfaces with the same code unit
so thank you
anybody else
i think
one in the back first i think
oh i think she was first so she can have
first one
um yeah i was wondering before you
showed um how great it is to convert
excel files but do you plan on tooling
to maintain them because once you have
them and start developing and
especially when you have an add-on you
develop in the
seaside then you develop in the al and
want to bring this stuff together and
right now it's quite
tricky to merge those fights again
no
can you hear me no okay i'll try this
one
so
it's a good question right now there's
tooling available uh
open source tooling and also tooling
provided by microsoft for managing your
excellent files
we are planning on improving the
experience of working with these files
but we what our current recommendation
is to take out these files from your
development process
when you're doing development you should
care only about the code
and once you're done
build your project generate the extra
file send it off to translation
and only include the translated files
when you're ready to ship so that you
don't spend your time merging xml files
also these resource files are quite
difficult to maintain and get
you you should not be spending your time
around that but we will follow up with
the with the blog post on how how to use
the current tooling and open source
tooling available
available out there and i know there are
currently a few
languages in the vs code marketplace
that offers some nice commands for
working with them but we will follow up
with the blog post
oh sorry
all right so my question is
you mentioned that we can
create pull requests now for
for next time when we want an event
request
can we do the same instead of creating
an issue or it's only available for the
system app
yeah so for the system definitely you
can create pull requests so if you need
something anything in the in the system
app go ahead do podcast the base app we
can't open source quite yet the problem
being the second we would open source
the base application it would get ripped
into thousand different directions and
we probably would not be able to deal
with the with the incoming amount of for
requests because i mean also let's face
it not every pull request is maybe you
know the right way to do it so we
actually need some people to look at you
know the actual content of the pull
request so this is why we're still
working uh and i would be very
interested in talking to you guys like
catch me somewhere out there like how
can we move forward with the with the
base application and and the project of
kind of open sourcing that and then you
know enable a closer collaboration on
the base application
but for now you'll have to settle with
all the extensions that we ripped out of
it as a true open source model
it might also be
a good idea to
before you send out the pull request and
you start writing code open an issue
there and start discussing it you don't
want to start writing code and go in a
totally wrong direction it's good to
start a discussion early before you
you've already written code
anybody else
sorry i can't see
thank you
it's about the interfaces again
um
you told about that it's planned for the
extensibility of the enums a nice
feature would be some kind of dependency
injection for testing or for
making the code more flexible
we have to put those ideas that they
will be the next step you take or are
you planning those steps already
[Music]
first of all we need to finish the
feature it's in the making
i hope and that's probably more for
yesbo and i know he is very excited
about it um that the app will uptake
this for
at least probably in the beginning
because otherwise it will be breaking
new extensibility
areas
in the base app
which will allow you to
provide interfaces
but again we will have to make sure that
we are not breaking you while adding
this
so
but yes we are going to use it
so i don't think i can
pinpoint more exactly where we will end
up using it
um interfaces only
contain the definitions of the functions
typically are there any plans to allow
it to actually have
code to execute within it or maybe then
down the line is there going to be
inheritance perhaps
there's no plans for adding code to the
interfaces
maybe down the line we will have
inheritance
and
maybe not
necessarily on top of the existing
objects
we have no specific plans for right for
that right now
but in the case of i think the code on
the interface
i think that goes a little bit
i
assume the background for that question
something about defaulting
in the case of the enums there is
actually a way of on the enum itself to
provide a default implementation for the
interfaces so unless you specify a
specific interface for a value you will
hit the default one
does that make sense
all right
i think we're out of time yeah
thanks for listening in
[Applause]
