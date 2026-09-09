# NAV TechDays 2018 - What’s new in Developing for Business Central

- **Source:** https://www.youtube.com/watch?v=7jNByP3kFPk
- **Video ID:** 7jNByP3kFPk
- **Channel:** mibuso.com
- **Published:** 2018-11-27
- **Duration:** 89m04s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

thank you and welcome all of you it's
impressive to see so many people who are
coming here to be
informed about what we have done over
the last year in the development tools
unless it's just because you only have
two sessions to choose from but
at least you're here
my name is espinous christopherson i
have been an architect on the new
toolset and the new compiler over the
last three four years and with me today
i have alex
my my name is alex strader and i've been
with the modern development team uh
since the start almost
and since my start at microsoft and it's
been an amazing experience and as you
will see in the following
hour
it only gets better
so we have divided this presentation
today into three main topics we have a
section where we talk about what we have
done to improve extensibility
as you heard in the keynote we are very
focused on making a an extensible app
which allows you to extend it in all the
right places
and make it even better
and we have a section where we talk
about what improvements we have done to
the language to al what new things you
can do
and
least we have a section around
improvements we have made to the tooling
so what you can do in visual studioku we
should study code how we integrate with
that and make an even better development
experience
but first of all i'll talk a little bit
about extensibility this is one of the
things we have focused very much upon
from the beginning with a new
compiler and the new development
environment
we want you to be able to extend in as
many places as possible
and we want that for several reasons
reasons first of all when we're in the
cloud as also mentioned in the keynote
we are pushing out new updates
every month
and we want that to be a smooth process
otherwise we cannot be in the cloud
and in order to do that we need to have
a better separations between your code
and our code
and the ability to easily update the
platform
and the application underneath
to do that
we have had many internal discussions we
have many talks have had many talks with
you about how this would work how it
should work and we tried to capture
the essence of that into a single
sentence which is easily for us to
remember whenever we need some guidance
in what we are doing
so what we cannot come up came up with
this to enable partners to efficiently
develop maintainable solutions on top of
our application while still allowing
microsoft to evolve the application
and there's a couple of
highlighted voids in there efficiently
means it should be a
top of the class experience for you to
develop it should be far you should be
easy to
do all the tasks you need to do to
complete
your job
and it should be a maintainable solution
and what we mean about that is it should
be easy to
come with new updates add new
functionality
on top of what we built
but at the same time still allowing us
to continue to evolve our base
application and as boxy showed you we're
going to do a lot in that area so we
need to have a
system
language tooling that allows us to do
that in a good way
one of the feedbacks we have had
on what kind of extensibility we already
implemented and what we still lacked
was the case of
enums
you have all asked for
the ability to extend an enum what we
today call an option string
which is basically just a set of name
constants
in cl we chose to
list those options or those constants in
the option
string in al we chose to call it option
members because we thought it was a
little bit clearer
but
having that information captured in a
single property made it very hard for us
to come to anything which is extendable
and another
um problem with that construct was also
and whenever you define an option in cl
you have to repeat it all over the place
so
if you had red green blue you will have
to type that in tons of times
so what we chose to do was basically to
create a new top level type which we
called an enum lag of imagination we
stole the name from c sharp
it's a similar concept but just an al
and with a twist
so it basically lists
possible
outcomes values
all the values have an ordinal value
it's actually they say exactly the same
as what you have with an option this is
the one we use for persistence
you can put captions on it you also have
that with options
and
by the way it can be used instead of
options and long term we imagine this is
going to replace the optin type
completely
so how do we define a new enum
basically
simple syntax we have followed the
syntax
layout we have reused for all the other
objects
enum
we have an id sorry for that still
needed
and and the name after that there's a
section of properties in this case
there's only one extensible or not
default is not
and you have the list of values and all
of those values can have a caption
that's
the property you can put those right now
so
the use of the neon
that is sort of you now deserve to find
it you want to use it
use it the same way as many of our other
types
you use the word enum and then the name
in this case i use it first as a field
on a table and i can also use it as a
parameter and a variable same as option
and whenever you refer to a member on
that enum you do it by the old colon
colon and then the member name
so
let's
switch to a demo
this
everyone can see i hope
i have created a
small enum here it's basically a loyalty
enum
and
i have
i can get my mouse working
i've created a table extension where i
add the loyalty
enum as a loyalty
field on my customer card
and
a small confession here i'm a platform
developer there's many parts of the app
i don't understand any of
so i really prefer the customer cards i
can remember the id and the name
so most of my demos is centered around
the customer card
i also added
the loyalty as the
with a page extension to the customer
card so i can view it somewhere
and that's basically enough so i can now
go and deploy it
and here you can see my
loyalty
and if i
change it into edit mode
you can also see i get my
outcomes here
so
and this is a backup slide
so the extensibility part because i mean
this was actually why we needed it in
the first place
you need to be able to extend an enum
you need to be able to supply your own
outcomes to the enum
and we chose the same kind of syntax
that we have for page extensions and
table extensions
now we have an enum extension so you can
create a new
enum extension that extends the next 16
one
and in this case i basically extend the
loyalty genome i created before i add
another value to it which is the diamond
level
and i supply
my
the the ordinal value in this case i
take it from my
my own range it's an id it will be
persisted so it should be within your
own range so you don't clash with any
others
and if i
create this and deploy it
i will be able to get a
another
outcome listed
automatically in all the places where i
have a drop down on the xenon
so this still
leaves something behind because
actually all the enums that you you want
to have
made extensible
they live in seaside still
although we are on the track to remove
seaside we still have it we still have
our base app in seaside
so we need to find a way to make the
enums and seaside extensible so you
could actually
be able to extend those
so what we did was that on a
table field option an option placed on
the table field we added a couple of
additional attributes
and
yeah it's visible you have a button here
you can mark it as extensible
and you have to give it an id should be
in you should be in your range actually
it should be in our range because we are
the one who will do it
and
provide it with the name
for the enum
and
by doing that it will end up in the
simple files that you get into al as an
enum that you can now extend
so let's try that
and
go back
to this one
i have
first let's take a look inside our old
tool here c side
i have marked the application method
enum on the customer as extensible
i've been given that an id
and i
and a name
and because i have compiled the
application in this case running locally
on my own machine
with the generate simple options i
actually generate my own symbols now
which allows me to be able to extend the
application method enum
so if we'll take a look here
i actually
have intelligence here because this is
the only enum i have available for
extensibility right now in these symbols
so
this is by the way the only thing in
this project so i can now deploy it
and go to the custom account
if i remember
and the application method
as you can see now i have added my own
method
from an extension to this
so
why don't we just enable all the enums
in the base app mark them as extensible
and then we're good and you can go party
on them
there's a small problem with that
and it's
highlighted in this couple of lines of
code
basically we have
many places in the application where we
assume that we know
the number of outcomes from the enum
so whenever you and your solutions have
gone in
added
something to an option string somewhere
you have come through the application
and added your own code in all those
places
but you can't do that anymore so
if we mark an enum as extensible we need
to go through all these places in the
code and make sure that you have a way
of
get a saying
add an event so you will be called
saying
this this happened do something because
we don't know what this
case line should be
so so the way we are going to do that is
that we are going to accept requests on
enum extensibility and we will add them
and prioritize to add those
and over time
we will have
all the right enums marked as extensible
there's a small small other twist to the
enum compared to the option first of all
they are not assignable to anything like
the option basically the option type
today you can assign it to integers to
the bytes to the
decimal doesn't matter any numeric value
will go
we have
tightened that a bit actually you can
only assign an enum to an enum of the
same type
and there is no implicit conversion to
and from integer
right now we support implicit conversion
to an option type
we need that in the cases where the base
app is actually exposing something as an
option where you may have marked the
table field or we have marked the table
field as an enum then that shows up
as an enum we need to be able to call
the old method which takes an option so
right now that's supported and that's
actually the only conversion method
right now is to assign it into an option
and utilize that
we will be adding real conversion
methods for enums in the future
in future update we haven't done it yet
but we will
another thing which is also
missing
is the ability to
um
to to extend a split relation
the sample code before
was on the sales line type which is
actually a split relation to find us a
split relation we cannot do that yet but
we will add that functionality so you
can point it to another table if you
if we extend that enum
enough about enums we have added some
more extensibility for you
one of those we have added also
often requested is field grouped
extensibility
so
in the first iteration we didn't support
any kind of changes to field group but
what we heard a lot was that
oh i need to have
this and this in the drop down field
group so it shows up all my customers
want that
so what we have added is the ability to
add last to a field group
this will not solve all scenarios but it
will solve the most common one and we
will add more over time
so you can add to the drop down
field group for instance a new field you
added or just one of those that we
didn't think anyone would use
and
let's jump to the
demo for that
by the way this is a good reminder here
i'm prompted here to update to the
latest visual studio code
1.29
unfortunately
and this is the
problem with living in the cloud we have
a small issue with that version which we
are looking at
um
which means that right now you should be
using 1.28 with the al extension because
when you deploy
we fail to lock the deployment steps
in the lock it actually
contacts the server it deploys but you
cannot see it
um
they have made a protocol change and we
need to
adapt to it
and
we
unfortunately have got have gotten a
couple of those surprises over the
last couple of years but
for now i will dismiss this
i have a
small field group
extension here
i will extend the customer table
on all the customers i will actually add
the
sales
for that customer
and
for the items
i will add description too it's also a
very often requested
field to add to the drop down now you
can do it yourself if we
forget to
so
let's just
deploy that one as well
and
let's look at the sales order which is
probably the one with
most
drop downs
in the app
so we can look at the customer here
all the way to the right
we have the sales
local currency and if we go to the item
here
it must be chrome
try again one last time
okay
you will have to believe me it's out
there to the right
and pass the backup slides
another thing we have added
and i mean the problem was that you
could add a bunch of new objects but the
help was actually in the cloud just
pointing to our help server
so we have added the ability to add help
links on objects and those help links
are the ones that will be invoked
whenever you
ask for help and you can point it to
your own external help server if you
want to
what we have also added is the
is a local um
[Music]
replaceable part of that url in this
case it's the
curly bracket
zero curly bracket end
and that will be replaced with with the
with the local information and that
local information
you can limit in the app.json you can
specify which locales you actually
support
and if you are
running the users and running with one
which is not supported it will pick the
one the first one from that list and put
that into the help
url um
will have to do that for all your
objects we are
looking at
if we can implement a feature where you
basically specify a base url and then we
will automatically request
move all requests to that but we haven't
done that yet
another thing
we added
as mentioned in the keynote we have
added a lot of integration events
almost 3 000 over the last couple of
years
and
it's
very complex to find out what to extend
and
since my
manager stole my
most of my demo here i knew about it i'm
not going to demo it basically we have
added the event recorder
which is a nice way of being able to see
what events are fired when you execute
a action
post sales order you will get i don't
know several hundreds i think
um
but then it will give you an idea of
where you actually
want to
stick in the knife and add your own code
so
and
what it didn't show
was actually we have proved the improved
the
intellisense for events
so compared to seaside whenever you did
an event subscription you just got a
a procedure with all the
parameters which are actually available
for that event
which is not necessarily very efficient
and it also meant that you will
now take a dependency on all that if all
those parameters even though you only
used one or two of them
so
we went in another direction
with a
and one of the reason of course is that
is a completely different way of doing
development with a source file rather
than the more prescriptive seaside way
of doing it
so we rely heavily on intelligence in
all in all places and what we have added
now is actually that when you have a
subscription which in this case i could
have
dog out using the event recorder pasted
that in i create my method
and now i need to
figure out
what parameters i can actually use for
this event
so we have added the intellisense here
that says that oh there's a report id
fine i need that
one more
and i will also pick the wrong mode
so it's an easy way to get that
information surfaced as intellisense
and
i think that's actually
your q alex
so in the last year
their language its base library and its
runtime have been extended and improved
with two big goals in mind
one to make you more productive than
you've ever been before in seaside and
two
to support the seamless conversion of
your existing cl solutions
in the next few minutes i will talk
about the improvements we've made to
reporting
how donate interoperability works in ale
about all data bound actions and
isolated storage
reporting
is the one of the areas that has
received the most improvements in the
last year when reports were first
introduced
in al it was fairly difficult to create
a new report
with the new layout if you for example
you wanted to create a new word layout
you had to create your report publish it
go to the client
create the word layout from there
download it add it to your project
make some modifications then republish
it and then go through these steps every
time you wanted to do modifications to
the dataset
starting with the
spring release of business central
we have improved this process a lot
so far that it only takes a few seconds
to create a new layout for a report
as i will show now by creating
by creating a better customer list
so i already have my report
can you see it
no sorry
now
so i have my better customer list here
and
it has a customer table as the data
source because as lisbon said we really
like the customer table
the number and three columns
the number the name and the address
and now i'll
add a word layout
and i'll specify the path to
a local word document that will contain
the layout so
better
customer list docx because it needs to
be a word document
right and i will set the default layout
to be word because i i don't want to
deal with our dlc during a live
presentation
now we're set and as you can see there's
no better customer list oops
there's no better customer list document
here but if i press ctrl shift b and
build
the document is created
and if i click open externally it will
open in word
and let's it's an empty layout
but if i go to the xml mapping pane
i can see that our data set is here so
if i click on this i see the custom with
the all the three columns
and every time you make the change to
the data set in the report the changes
will be reflected in the data set in the
layout and this works for both word and
our dlc
so let's go ahead and just create our
much better customer list
and
let's just make
use a table for the customer list
and had add the three
table headers name
and address
and three simple plain text controls for
each of the columns
and also we need to make sure that we
have one row for each customer so we're
going to select this row
and make it
a repeater
good and we save
and that's the layout and now if i
publish
and search for best better
customer list
shows up here and let's just preview it
quickly
and we can see the
newly created uh word layout that took
only a few seconds to build of course we
know that a lot of you have spent more
than a few seconds on creating layouts
for your customers and creating reports
and that you would like
your customers to use these instead of
the ones that come with business central
so starting with business central fall
we have added the
ability to globally substitute
reports
so this means that instead of having to
go to every place where a report is
run and make the replacement you can do
it in one place globally by using an
event subscriber
so i already have
my code unit that will do the
substitution so all you need to do is to
subscribe to the report management code
unit to the on after substitute report
it's a funny name but
that's the
the paradigm
and this
event publisher has offers you two
parameters
report id which is the id of the report
that is being run and a new report id
which can be used to set the report that
should run instead so what i'm doing
here is just checking if the report id
is the id of the customer list
and
if that is true just substituting it
with a better customer list before i
deploy this
let's just go back to our
client and search for the customer list
and
if you give it a few seconds we see the
customers that ships with business
central which i find inferior to mine
because i created it and of course it's
better
so let's
publish our extension
and now if we search for the the
customer list
and we run it
we see that starting from the request
page we already have the better customer
list right so the substitution happens
before anything else has to that has to
do with the report happens
and if we press preview
we of course get our customer list
let's go back
the slides
so one small detail that you have to
take into consideration is that
substitution only happens when a report
is run through
as a result of a user activating an
action that has the run object set as
the report or
when it is run
for one of the static methods on the
report class reports cannot be
substituted when executed from a
variable so if you have full report
customer list and food.run that will
always run
the customer list not the better
customer list
in this case
so let's skip
through these
to improve reporting even more we've
added
more information to we've exposed more
information about reports and request
pages
we have added the two new virtual tables
all control fields and report data items
the all control fields table contains
information about all the page controls
on normal pages and request pages on
reports and xml ports
and the report data items
table contains information about
the individual data items on a report
so using these new tables you can
extract information about a specific
report
and send it off to a third party system
which
can constru can present an alternative
ui to
the user or
get input through some other mechanism
and send back
the request page parameters xml
essentially what this allows you to do
is to
separate the execution of the request
page from the execution of the report
and gives you more flexibility in how
you interact with external systems
we have all in the slides we also have
the schema of these new tables for
reference but
you can look at these after the
presentation and we also have code
that
can help you get started with this new
scenario you can find it in the slides
and also in online in our
in our documentation
and
finally after two years of people asking
when this is coming back
we have done it interoperability but
only for on-premise
so again only for on-premise because
this is the most important thing in the
cloud we we suggest you use uh
alternatives such as azure functions
and all the other goodies offered by the
azure cloud or even
other parties
um
i think the easiest way to show how dawn
net works is to
start with uh to go to go through a demo
and if you remember how darn it worked
in the seaside is that every time you
had to add the variable
uh you had to go through a series of
dialogues
until you selected the
the the type so you first have to select
the assembly and then you have to go
through a long list to select the type
and you have to do this for every time
you wanted to add a new variable to your
code
but with
with in al we wanted to streamline this
experience
but before i start with the demo we have
to
make sure we are targeting on-prem
so i need to specify that
i am the target is internal in my
app.json
and because the compiler runs separately
from the server so you have a version of
the compiler in vs code with the
language extension you also need to tell
this compiler where to look for assembly
for assemblies or donate assemblies
and you can do this by going to your
settings panel and
setting the
assembly probing paths
to paths where you have assembly so in
this case i set it to see windows
assembly which is the location of the
global assembly cache
and another folder that contains
assemblies from the from the server on
my machine
and now if we go back to
here we have a simple.net
container
so you should only you only need to
declare
the types that you are using once and
you do this in a dotnet container where
you specify a list of assemblies that
you will be using by using the assembly
name
and of course you can specify other
characteristics of the assembly assembly
as properties culture culture version
and so on
and then you go on to specify the types
and you do this by uh specifying the
fully qualified type name
followed by an optional alias this alias
is used in code so that you don't have
to say system.datetime every time you
can say my daytime
if you do not specify an alias the
compiler will generate one for for you
for example just using the class name in
32.
so that's how you declare the fact that
you want to use donet
and when it comes to usage
let's go back to our favorite
page
and extend it
so i want to
add two new fields to the page or my
daytime text where the user can enter a
text in his locale
and
my day time that will show the the
result of parsing this this text and i'm
going to use the donet
daytime type to do the parsing
so
if i have the
to declare that i'm using a donut
variable i need to use the donet keyword
followed by the type and as you see you
get the
intellisense
and i just need to use my date time
and
that's
and you see even though i'm using the
same name which is a bad practice i do
not get conflicts right so i can say my
date time is vt parse
and my the time text
one improvement we've made to done it in
al versus cl is that now you can
chain methods and also get
autocompletion for this
so now i can because parse returns a
date i can call uh methods on date and
for example let's i can add a few days
to the date and you see i get a full
signature in doneta and i have full
information about the type
so i can add five days to this just to
and now if i build
and publish
yes
ah
yes um
let's remove this
that's probably because i messed with
the demo before
good so i have
my two fields on the customer card and
if i enter some goblin
i will get an error
from the system daytime first and if i
enter a
date in my locale
december 13 you see because i added five
hours
it parses it
i added five days it uh parses it as uh
it parses it as as december 13 and
that's five days so the date is 18 of
december
but uh
working with donald types is not enough
because
in cl you also could use
events from donet
and
in order to use events
you had to one second
so to use events in in
seaside you had to go go to a select a
global variable open its properties
window and
set the with events attribute to true
and seaside would generate stops for all
the events that you had on that
that type
in al we don't want to generate a
necessary boilerplate
so we rely on intellisense for helping
with events
first i need to specify the with events
attribute on the
on the variable to tell the compiler
that i'm going to use events from this
and then when i want to subscribe i'm
going to use triggers because
so i start by using the trigger keyword
followed by the name of the variable and
then i get auto completion for the
events that are available on
on this type
and if i just say elapsed
i get the full
signature of the event and you see that
the compiler is complaining a bit
because
it's
it says that it doesn't know about this
type so if i go back to donet i see that
i have defined an alias for this so i'm
just going to use the alias because i
like it more than the predefined
type that's an area for improvement
and let's just print a message
when this event is triggered so
let's print the signal time
and also make sure to stop our timer
because it might get annoying
so now if i publish this
at some point
i'm impatient so
i get prompted about the about the event
in the previous case the page loaded
slower than the timeout i said so the
timer was stopped before i could
see the the message
and
one other piece of donet
interoperability that is widely used in
cl is for interacting with javascript
and download address
moving forward we recommend that you
migrate these add-ins to native al
add-ins but we realize that you might
not want to do this right now
so for the time being you can continue
using your existing.net
add-ins
so
if you convert the cl code to al
you'll probably get
something similar to this and the
compiler complaining that it cannot find
the control add-in
microsoft dynamics nav client ping-pong
we can we can solve this by going to
our.net container
and
declaring
a type that corresponds to the donet
add-in and specifying that it is a
control add-in
so here i have the full fully qualified
name of the type in donet followed by
the alias that is
used
in the code
and that's it that's everything you need
to do to
convert your
existing cl
usages donet usages in cl to al
most of this is done automatically by
the by the compiler the only step that
you need to do if you have custom
add-ins is to specify the
the add-ins that you use when running
the txt-2al converter
so let's
move on
backup slides
and the
[Music]
next major improvement we've made is
isolated storage we've received a lot of
questions from from you around how to
store values in such a way that other
extensions cannot access them most of
the questions came from developers
uh that wanted to store values necessary
for interacting with external systems or
building their own
licensing systems
the answer to all these questions is
isolated storage in essence it allows
you to store key value pairs in such a
way that only the application that
stored them can also retrieve them
the values are stored in a new
non-company table called isolated
storage and it's left up to you to
decide if you want to store them
encrypted or in plain text
furthermore you can
re specify the scope of the data by
default all the data is stored at the
module level so the data is accessible
to the application independent of the
user or the company in which it is used
if you specif you can use the data scope
system option to restrict this
and for example if you specify data
scope user you can restrict this to the
user level so only the user that store
the data can also retrieve it
the fourth area of improvement is all
data bound actions in ale
all data for those of you that might not
be familiar is a protocol that is a
standard that defines best practices for
creating and consuming
restful
services
this standard is well supported by
business central
and
it allows you to interact with entities
defined in the application over http a
bound action is nothing more than a
procedure that is exposed
through the data protocol
until now it was not possible to create
bound actions
in
al uh mostly because the mechanism for
which the runtime interacted with the
data protocol relied on a few donut
types and donet is still not
is not allowed uh in the cloud
to solve this we have added the web
service action context and web service
action result code data types that allow
you to
migrate or write
procedures that can be exposed as bound
actions
uh in uh al and in the cloud
the
only prerequisite to exposing uh
a
procedure as a bond action is to have
the service enabled attribute
one small limitation that we currently
have
is that you cannot add
bound actions via page extensions so if
you want to create the new bound actions
you need to create a new page or query
and
all the innovation in the last two years
has
been greatly helped by
visual studio code it is a great
platform to
develop for and it has allowed us to add
better tooling at a faster pace
i encourage you to
explore the marketplace and if you find
an extension
that
is useful use it freely or if not
feel free to develop your own extensions
that complement their language extension
and make them available talk to the
community
with
we've had
a lot of
feedback from you
regarding their language extension and
our team has worked diligently to fix as
many as or address as many of the issues
that you've reported on github
by default these issues get fixed in the
master branch of our repository which
targets the next major version of
business central what this meant is that
back porting some of the intelligence
improvements or minor bug fixes
was
a labor intensive task and because each
version of business central shipped with
its own version of the extension the
the effort grew as time went by
starting with business central fall
we are shipping only one version of
their language extension that can be
used with all versions of business
central
so
you do not have to wait for the next
major release to benefit from the fixes
that we do
of course different versions of business
central
um have different slightly different
capabilities
and we want the compiler to let you know
if you're using a feature that is not
available in your current version of
business central
to help with this we've added the
runtime property in the app app.json
and this can be used to specify the
version of the of business central that
you are targeting we associ associate
version 1.0 with the spring release
2.0 with the full release and we
increment by one for each major release
of the product
all this work has been done
for the benefit of you as the consumer
of their language extension internally
this meant that we had to version all
the bits that make up the language
the syntax the properties the library
and so on
um but we believe it was worth the
effort because
now you can uh use you can benefit from
for from all the fixes we do
shortly after they go into the master
branch
so
as you can see doughnut
was one of the things we we versioned
first
and to see how this works
let's go back to our donut demo
and open our app.json so right now the
i'm targeting runtime 2.0 which
corresponds to the full release of
business central
if i if i downgrade to 1.0
i will immediately get
warnings saying that donate interrupt is
not available in this runtime
and you will get this for all the
features thereby enabling you to get
feedback faster
and
i think that's it from my side
this one yeah
thank you
[Applause]
so
yeah it's already up there and i
probably need to
wake my computer up
yeah
some of the improvements we have made
is to the debar
they were still lagging behind the old
wind client debugger
you have known for some years
and
we have
added some more functionality to close
that gap
and
some of the options we have
what we have added in this release is
the ability to
now break an error which means that
whenever an error occur you will be
placed on the
offending line
and we have also added the break break
on record write which is basically
insert modify delete on any record the
system
the way you specify that is in the
launch.json file which is the one that
tells you or
tells how to launch the debugger or that
when when when you do a deployment from
visual studio code
and another thing we have added is also
the ability to set breakpoints in
external code
which is a
a change from before
and
what is actually
enabling that is the ability to browse
into
old code cl code
and in this case if i place
my mouse or cursor on top of the
customer record here
i can actually do f12 and now i navigate
into
the source files
for that object
it's a little bit the source files in
this case are a little bit different as
you can see up there they have the
extension dl which is
short for debugging al
but we have
inserted all the code from the um
from the original object
in this case it's the same it's the same
format as you used to see in the in the
old debugger
but actually down at the end here
we have the the rest of the object
information
so you can see this is the field groups
this is actually the keys and all the
fields on the customer table
all the properties are not there there
and this is but this is an interim
solution until we are all on a l because
then you will be able to go to exactly
the
original source
file so
let's go back here
and this is the
brow cl code base app code from visual
studio code i just showed
another thing another benefit from using
visual studio code is actually they are
very great at adding new functionality
new innovations and one of the things
that they have added is the outline view
this is a this is a tree view that is
added or available inside visual studio
code
and you can use that to surface elements
in a file and in this case those
elements are actually our symbolic
information
we had
some of it already available for it but
we have now
tweaked it a little bit to fit the
outline view even better
so
let's
try to take a look at that
and
find this small project here
which is called w1
um
as you can see here this is actually a
converted w1 application i have loaded
into visual studio code
and
if i pick the sales order page which is
huge
oops
i can try to pull up here
maybe i cannot make it any bigger
down here there's the outline view
and in here you can actually see the
structure of the file there's a layout
session
area content there's even something
which is green
which is
which disappeared
it was actually the group itself
and the green color is because there is
a
warning on it so you can actually from
the outlook from the outline view here
spot areas in the file which there's
something that you that should
point your attention to it will be red
if it's an error in this case it's just
a warning but i can actually use this as
a
quick way to find
navigate to places in the file i can
even do search if i want to search for
something with customer in it it will
filter down
and show me all the areas which contains
customer and i can navigate to that
so very very
efficient way of navigating around if
you can control your mouse better than i
can
another improvement way we have made
this release is that we have improved
some of the institutions
we have added direct helpline links from
the intellisense so if you click the get
help it will actually
open the our
our online documentation where you can
read about those properties
that online documentation today is
actually hosted on
[Music]
so you can so you can add suggestions if
you find that this service is is not
containing containing enough information
or can you maybe explain this better
and our
ua writers will actually
see this pick it up and
maybe ask some developers to help
improve on it or maybe do
write some more themselves
another thing we improved is actually i
mean it's a bit hard to choose an icon
from a named list so we actually
utilize the ability to to to add images
to the help
in intellisense so actually when you
look at the image property on an actions
for instance when you scroll down you
can actually see the icon which is
associated with the name so you have a
better chance of choosing the right one
launching the browser we have heard that
complaint
a lot of times i mean why do we open the
new instance of the browser every time
you deploy
now you can change that behavior
there's a new launch pro browser
property in the launch.json that you can
set to false if you do that we will just
deploy without opening the browser
by default is true but you are free to
change it
as you like
id ranges
we
all love to hate ids but
we are not able to
remove them right now or
anytime soon we have
it's unfortunately the truth we
we have a licensing system that still
sits on top of them and our entire
runtime platform is actually
very much utilizing the fact that we
have
an integer that represents all our
objects
from a development perspective
as a developer i really love to get rid
of them but then
it will take some time
so but in order to help you not
entering ids which are without outside
your own range we added the id range
property to the app.json file
in in the first release
but a lot of you have actually told us
that it's not really good enough because
your id range are often fragmented
so you've got some ids someone else got
the next ones and you got some ids in
another place
so we have added a new
id ranges property that you can use
instead this is available in the
for from the full release of the
compiler
and that allows you to specify multiple
ranges that you can work in
so
another thing we optimized in the
tooling
is
how to generate permission sets in order
to submit an app to appsource you need
to provide a permission set with
permissions for all the tables that you
add
we
haven't been that good at actually
telling you exactly what you needed to
do and and how it should be formatted
we added a number of
snippets that we thought would help you
maybe it did but it was definitely not
enough
so we have added a new command which is
called generate permission set and what
it actually does is that it takes your
extension
and looks for all the tables and
generates a default permission set for
you
so let's
try to do that and i'm
not going to do it on top of w1
let me
i actually think i need to create a
table
so
let's do that quickly
that
feels in here
i now have a table and if i try to
submit this to appsource apart from the
fact that it's completely useless it
will not be accepted because i didn't
include a permission set for it
so what i can do is that i can use ctrl
shift
b to get to the command palette
and say i wanted to generate permission
set
and that one actually
creates a file for me
will
with the permission set in it containing
my
objects
and
unfortunately here i'm running on a
not ship version with a bargain so i
generate a too many
permission sets
um
but it will generate a a permission for
each of the tables included in your
extension so you can go you have a
template form setting the permissions
that you want for those tables
it's amazing we saw that this box at
directions i have fixed it and i even
though i did that i managed to get a
version down here with that one fixed
and
so but it should have just generated a
permission for the only table i had in
the extension
one of the new things we have added as
well is analyzers they have actually
been in there for a while
but we haven't really not
said a lot about it and we have
wanted to spend some more time improving
the actual analyzers
the analyzer is a separate assembly
that
is called by the compiler
and it's possible to add rules in there
so it can validate
syntax
semantic validations
whatever rules in there
[Music]
the results are shown together with the
compiler output if you run it from the
command line it will be some of the
compiler output on the command line if
you run it within visual studio code it
will show up in the same window as the
rest of the errors from the compiler
and you can use rules from rule sets to
control the severity of of um
of errors or warnings you can make
warnings into errors if you said this is
actually
something which is so bad that it should
be treated as an error in our case
so
as boxes showed
at the keynote
these are the list of what we have today
i want to talk more about that
i'll talk about how to enable them
there's two properties that control this
in the settings file
there's
enable code analysis ta-da now they're
enabled
and there's the code
analyzers which is a list of analyzers
which should be enabled in this case
i've enabled the code cop and the
appsource cop analyzer
the rule sets
we have
it's basically a file that specifies
how how individual errors or warnings
should be treated
it's writing it's it's
it lives together with a project
and and we have added a cover of
snippets to help you
add
new rules to those in this case
it's elevating a warning into an error
or actually everything into an error
um
and
another config file is also worth
mentioning is actually um the absolute
json file the absolute cop is the one
you need to run
and have a clean run on before you
submit to appsource
and one of the things that one actually
validates is that you haven't deleted
any fields any tables or anything
which will cause a schema or update and
the only thing that can it can validate
that is actually
to
point to the previous version of your
shipped uh app
the way you specify that is that in the
in in the
appsource.json file you have the version
number name and pop name and publisher
for the previous one
which you type in there
and then when the analyzer analyzer is
running it will actually validate that
for each table you have
that you haven't deleted any fields you
haven't modified any changed any types
that will require schema change
and and help you
not breaking any of those rules
and you can also add uh
prefix or suffix
um
for and and have them analyze the
checking that you are actually using
your
prefix or suffix that you are using for
your
solution
and then the mac os version i have
actually demoed it down here last year
but we haven't been able to ship it
until recently
so in the
marketplace
v6 file
is actually both
a windows version and also a mac os
version
there is some limitations in
functionality but it's actually
only almost only around
reports and report editing specifically
because
there is no idlc editor
or rdl layout editing on mac os we have
no tooling for that
and the xml pane that alex showed before
is not available in the
in the word for mac
sort of a bit out of our hands but
that's unfortunately the truth
but you can still compile and and change
data sets so you can work with project
that contains
reports you can just not edit the layout
and also net is also
not supported
so
and last i think translations
we added
xliff as our translation format
we have heard a lot of requests for
separating
the translations from the source files
so they are actually different artifacts
and internally for us it made a lot of
sense and we think this is a good plan
we stick with a
a standardized format which is a cliff
everyone is happy
it turned out not so much because as
some of you pointed out in the cases of
patented extensions and in other
situations
it's a bit cumbersome to actually have
the x-leaf and if you don't have a
separate translation team or maybe even
a translation agency and just do it
yourself it's actually far easier to
still have them in the source files
so we
sort of
reverted our previous
planned decision about obsoleting
caption ml
are actually sticking with it but you
can only choose one you cannot use both
at the same time
so we will allow you to use
caption emails still just not for absorb
submissions if you are submitting an app
for app source
you will have to use a cliff-based
translations
and if you are actually using xliff
based translations we have made that a
bit easier because
we in the generated xl format we have
this transunit id
and it's hard to read
because it's actually hashed of table
names and and field names and property
names and the reason for that is that
there is a boundary to the length of
that id that we had to obey to so we
could not just concatenate all the names
unfortunately
but what we did instead is actually to
add the real names into the
into an annotation inside the
trans unit
so you can see that this was actually
the shipping rates table and there was
the name field in this case the caption
this should make it make it easier to
identify where gl element it came from
this was the last slide so
let's open up for questions
one here and i don't have to throw that
far
so uh
about the debugging
is it possible i know it's not possible
right now is it technologically possible
and are you planning to let us debug
javascript especially in control
headings
um
right now we do not support it
i
don't know
what
if
how we can make it work actually
we know the scenario and and it's
definitely
something we would like to do i think
you can do something if you run to
we just do your code side by side
but i'm actually not sure about it
other questions
i have actually two questions uh one
about keys
as i know we are not allowed to add keys
in our table extension for the fields
which are used in actual table
will we be allowed to do it somehow
um
it's it's one of the most
requested features uh
we would like to support it but there is
also some complications with it that we
need to solve first because
because of the way we are doing it i
mean the table extension ends up in a
companion table which means that in
order to add
fields from the
base table we actually need to replicate
those tables into the into the companion
table in order to do it
[Music]
we are
thinking about it i don't have any
timeline for it it's definitely
something we hear a lot
and another one about query object it's
now really limited
uh are they are playing to do it's a bit
better
we don't have any immediate plans but i
mean please let us know what you are
lacking or
how we
what you think is missing um
more questions
wonder
regarding the enumerate extension thing
if your app extends for example table
39's
line type
how would you recommend you solve it if
you have to remove that but the customer
is not going to use it anymore
and you have the records dependent on it
it will
yeah i mean
if you just remove it which you can but
now you will have left i mean
outcomes will with
unknown ids basically and and it it
nothing
breaks actually it will leave them with
with the id that you gave them and that
will actually show up in the ui
um i think the
i mean
you probably need to do some kind of
data cleanup and in some cases i i think
it's different
difficult
to say exactly what you need to do
because it depends on what it was that
that outcome meant
if it's crucial for
some of your accounting that you
actually had this special flavor of
something
maybe
it's actually not really an option to
remove it
because maybe that information should
stay in there
otherwise you will have to
write code that basically enumerates all
your
objects and change it into whatever then
makes sense because for some reason you
chose that outcome at some point and
what does it mean to remove it
yeah it was just an extreme example but
yeah
but i mean you can do it
hang out the extension and and
it will keep running but now you'll just
see the ordinal value
thank you
more questions on the front rows oh
that's one up there
yeah so i actually have two questions so
the first one
is um if the al language extension is
planned to be backwards compatible with
nav 2018
and if not are we going to be able to
have two separate extensions
um
are you talking about the extensions you
develop in a yellow or about the
that's one thing that i forgot to
mention
uh you can use the language extension
from the marketplace with any version of
business central
so for nav 2018 you should use the
extension that ships with the product
and if you if there are any bugs in that
one you need to
make requests for
fixes
and but
it should be
compatible in the sense that anything
that worked in 2018 should work in the
latest version
yeah and uh
continuing in this
will we be able to have those two
extensions installed at the same time
uh
no you will have to
they can be installed but you have to
disable one or the other otherwise they
will compete on giving you
compiler feedback
and there's one more important thing
that you should remember whenever you
update the a language extension it only
updates uh the compiler that is used by
visual studio code and the extension
right so the compiler that is running on
your server and that compiles your
extension when you when you publish is
still the one that was shipped with the
server right
okay so the next question is about
translation pulse
for now the
only if i update something in
functionality translation file the base
file gets updated
and uh the other
children files
don't so is there any plans to make it
so they do update
yeah we we know we can do better in that
area yes i cannot give you a timeline
for it but yes it's not optimal no
thank you
there was one up there
please sit on the front row the next
time
my question is
you said that
if we have dot net adding develop for
seaside
if we want to use
this
in business central on cloud
we need to
migrate it to
al.net control in how what does this
mean to move it to azure functions or
i i will clarify that a bit
so
you can use your existing.net add-ins
on-prem everything related to donet is
on-prem that includes javascript add-ins
uh if you want to use an add-in
in the cloud you can use the ones that
ship with business central so we already
have the business chart been
included
but if you want to add your own address
they need to be native al control
add-ins so this is a specific type that
allows you to
package javascript and
css as an add-in and deploy it with your
extension
hi uh regarding dependencies so
currently when you're doing a
personalization on the pages it adds
dependencies to every single
extension that's been installed uh that
is i understand getting changed pretty
soon yes so do we have a timeline for
that
and
[Music]
it will soon we have we're working on it
it will be in spring i don't know if we
will
move it to
the
updates i'm
not sure about that thank you
here's what
is that up here
um with the field groups you use the
command at last to set it at the end
can
you set a field anywhere in the
already existing field group
no um
not not right now we
know that this is not solving all issues
uh
and and we may add more functionality in
the future but right now we i mean you
can you can move it around personalize
it around but you cannot
as a part of the extension tell it to be
the first
okay thank you
um
you showed us
up here
but yeah
um you showed us using the f12 to look
up to a
you know declared a variable
we could then look up to the code behind
it yeah yes um the dal files
uh you can't go any deeper than that can
you once you've seen something in that
dal file you won't think i need to look
at that function
move on
no no unfortunately not um
and the reason for that is that i mean
we do not have
all that symbolic information for the uh
for the stuff that comes out of cl
okay and the other thing was
in the old seaside it was useful to be
able to browse through
existing objects
and
look for things in there go i need to do
something how does nav do it
are we going to be able to look at
and do that sort of browsing
browsing of of the of the source code in
general
[Music]
i mean we're not we're not closing uh
the source code it will still be open
you'll still be able to see today the
browser is seaside
in the future it will still be available
and we know that the entire
discoverability of
existing al code is an important part of
development for you
so you'll add it into the s code at some
point
i mean at some point it will be i mean
one full extension
sitting on a github repo that you can
grab and and work with yeah
any other questions
it was uh basically uh similar to the
keys and the issue with the companion
tables
what about if you want to add
an extra key and not
not using the companion table
so like the fields are already in say
like table says 17 say
are you thinking that are you thinking
of that at all
i don't think we have any immediate
plans for that
and but i'm actually not sure
adjusting the performance as much as
anything yeah
um i i'm sorry i don't have an answer
for that all right okay
i know why it's a problem
um i also have two questions my first
one is you've shown us the way to add a
field to a field group but is there a
way to add a new field group to an
existing page
or
table yeah you can add new field groups
the problem is that if i mean
some of those some some of the field
groups the drop down and the brick
has special meanings and you cannot add
a new one because if they're already
there
i've seen i've seen several uh tables
without field without the drop down
field group so can we add those yes okay
and the second question is and you've
shown us the debugger or the new
debugger features um but is there a way
to attach a debugger to an existing
tenant because now we have to publish an
app to debug but we also have to debug
without publishing an app yeah
unfortunately not yet um we
want to add that feature but it didn't
make it for fall
we i mean it's of course it should be
like that but we just haven't
had time yet
maybe
so there's one question up here
hi this is regarding translations you
said that the ml properties will still
be available for customizations
is this just for a longer time or
forever is a lot but but i mean we are
basically we
i mean we are not removing the support
for them because we acknowledge that
it's a this is an easy easy way to
provide translations for
pertaining extensions or smaller
extensions
the only limitation is that if you want
to submit to appsource we will require
to use xliff
hello uh you show us this uh extension
to replace the report with another
report yes yeah
and it is uh
then we don't have to change the report
selection
yes
but how about the printer selection will
it work
either we need to
put the new report in the printer's
election
what will it print to the standard
printer
i think it should work in in general
because
as long as the report is invoked for one
of the entry points that i i've
showed shown in the slides
the the substitution will happen happen
before anything so if it's printed
it the report you select will be used
thank you
anybody else
it's about the same as your report
replacement
this is global for example very customer
list but if you want to make it
dependent on the data
is this possible or in the future
by the data what kind of data because
for example you have a sales invoice and
you make it want to make it dependent on
certain customers each customer has
another
sales invoice report
not at the moment okay but if you have a
specific scenario feel free to open an
issue on github and we can discuss it
there okay
in regards to multiple events on the
same
act or activity is there any
news or update or upcoming changes in
the order in which they're fired if you
can manipulate that for instance if you
one of two
two modules have an on after modify
event on a specific field so far it's
forced which is where which happens
first and second is there anything new
in regards to that
um
we have no immediate plans but i mean we
are considering well that could be
something which could be changed in a
potent extension because then someone
will have the final saying in what is
right or wrong
um
we're not exactly sure how we would
design it but i mean it would probably
be something like that if we do it
all right thank you
there
that would continue the question about
the order of events being executed in
conjunction with the report substitution
so let's say we have 10 apps that
subscribe that event and they try to
substitute
with their own report what will happen
last one wins i guess actually probably
first one
no actually last one so you can
all the extensions will be notified
about this event right
and
they can each set the new id
but you can check if some other
extension before you already set it
right if the new report id is not
minus one and it's different than the
report i did and somebody already
replaced it so you should be a good
citizen and leave it be
exactly like you do with other event
subscribers with a handled
pattern
anybody else
okay
i think also almost out of time so
thank you
forum thank you for coming here
