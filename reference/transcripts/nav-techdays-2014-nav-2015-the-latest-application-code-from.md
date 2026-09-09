# NAV TechDays 2014 - NAV 2015 The Latest Application Code from a Design Patterns Perspective

- **Source:** https://www.youtube.com/watch?v=wG_uzqPt9yA
- **Video ID:** wG_uzqPt9yA
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 91m17s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

late ladies and gentlemen good afternoon
had hope you had a nice lunch break
we're starting off here in room five
with the next speakers please welcome
bogdana Mustafa and unders hi everyone
so how is your conference so far good ok
i am bogdana betezh i'm here with my
colleagues mostafa ballot and an
assassin and we are going to talk about
design patterns from the latest
antivirus and not only talking about CL
design patterns isn't this a little bit
of a contradiction if you think of cl is
a programming language you know that it
is not even object-oriented it has no
inheritance it has no polymorphism no
proper encapsulation no interfaces so
how in the world can we have design
patterns on something like that but I
get back to it for now I want to ask you
how many of you here are or have been CL
developers Wow okay this is this is
exactly what it should be in this
session so if you are a CL developer
this might be your day at work not in
the weekend hopefully if you don't like
your day then you get to work on new
features if it's not your lucky day then
you might need to do upgrade and by now
you are all aware that Microsoft is
giving you monthly cumulative updates
which you want to install if you want to
be on the latest bit if you're not doing
new features of upgrades then maybe you
get to fix some bugs from the older code
that already exists so what if working
on new features wouldn't it be awesome
if creating a new feature would be quick
and
easy and clean thing and if somebody
else has had the same challenge before
they would have documented it explained
it somewhere with diagrams and with code
examples so you can figure it out and
not have to reinvent it all over again
what if working of upgrade Microsoft
developers wouldn't ruin your solution
each time we ship a new cumulative
update every month so your upgrade was
actually easy and fast what if in God
maintenance you could look at the legacy
code and understand its intention from
the first moment without having to do
reverse engineering and detective work
to figure out what's there which would
make maintenance quite fast and painless
so this is all a nice dream slide and
the question here is what can we do to
get a little bit closer to this goal and
it is something that comes after you
have figured out what your
specifications are after you think you
know what the customer wants implemented
but before you start to write the first
line of your code so let's talk about
code design and this is the time when I
am searching for a t-shirt there at
mostafa I want to ask you if anybody
here has read this book okay so there is
one person there uh and if he gets a
t-shirt wait for the rest of you it's a
pls doesn't count on this one for the
rest of you I'm going to tell you what
it is about so this book is written by
Donald Norman and it's called the design
of everyday things and it is the 101 of
good user interface design so if you are
into creating an awesome experience for
your users I really really highly
recommend it but this book is not
talking at all about software it talks
about doors and door handles and how to
design them so
you use it use them correctly without
thinking and it talks about electrical
stores and about teapots and whatnot
that you interact with in your everyday
life yet when I was reading this book I
figure out that it is has everything to
do with software because today in
today's world from the moment you wake
up in the morning and you click on your
phone to turn off your alarm clock until
the moment you go and click on your
coffee machine to select one coffee
until you read the morning news or check
out the wetter our life has become
everything about software and we
interact with it with almost every step
that we take so I took this nice picture
that donal normal has drawn and I
changed it a little bit so now I have a
question for you we have tea pot number
one and tea pot number two so imagine
you have this deep what's in front of
you and it contains really really hot
tea and you want to pour this tea into a
tea cup which one would rather use to
okay so that is correct and the point of
this slide which is obvious by the way
the point of this slide is how many
times have you done this to nav how many
times did we build a solution that has
all the correct elements that looks ok
but yet something is really really off
and if the human race has been into
doing design for tea pots for so much
time already why not use the current
design and be performance and use our
effort into something new ok enough
storytelling this is what you are going
to hear about today I'm going to talk
very shortly about what is a design
pattern why use design patterns and then
we get into the interesting part where
you actually get to see some of the
patterns and the first of them are in
from our work from the latest year so
from the last release and each one of
them is mapped on one attribute that you
can make better in your code so they are
like this that would help you make your
code a little bit more extensible more
upgradable more configurable adaptable
and more user friendly when we're done
with that we have added also some
implementation patterns that are very
very close to the code so we call them
cookbook recipes and they are the
following how to do care to web service
calls how to do a copy document how to
do select distinct with queries we can
do that traditionally we using temporary
tables and if you search the net you can
find the solution but now we have
queries so it's a bit more easy and then
at the end we have added a few of cl
guidelines that we are using internally
inside Microsoft when we develop new
code our intention is to publish them
very soon we have an automated tool that
is checking those so actually cannot
check in if we are not respecting those
so there will be a few examples for you
here we'll end it up by telling you who
is part of this project and what's next
so what is a design pattern probably
many of you especially have been to the
PRS session or sessions over the years
you have heard about the Ganga for if
you didn't they are not some Italian
mafia they are for developers who made
up while ago about 20 years ago and they
wrote a book about design patterns they
took the term from architecture and this
book was about object-oriented languages
which can be used to implement design
patterns since then it's been very
widely adopted by the software community
however when we talk about object
oriented and pad
us because they are used together so
much we tend to think that design or
good design cannot be used outside of
object-oriented and this quote here is
by from the beginning of Martin Fowler's
book this is the guy who invented the
factoring by the way and it says I quote
when the Ganga for was writing design
patterns we knew that there were lots of
software patterns other than
object-oriented design patterns and this
actually it is a book about ERP patterns
so if we look at design patterns this is
how it started while ago and then the
community added more object-oriented
design patterns to the ones that were
already in the Ganga for book and then
people like Martin Fowler and many
others have added non object oriented
design patterns so wherever there is
software and there is a problem to solve
you can think of it in terms of design
so why we are here with this project is
to add something that was missing well
actually it started to exist but was not
named like design pattern and those are
nav design patterns we work with nav so
the problems that we solve our nav
specifics of the design patterns that
resolve our nav specific and it's
intentional that those areas overlap
because we do have patterns like
singleton and facade that have been used
in object-oriented or not object
oriented languages but we have also our
own that are really nav how this is a
short definition for a design pattern it
is and I will read this for you a
pattern is an idea that has been useful
in one practical context and will
probably be useful in others this being
said why patterns that's why so if you
think of the Navy with all its cold in
my
it is like a watch a complex watch with
a lot of mechanisms inside and if you
look it a bit closer to it then you can
and pay attention can figure out that
some of those elements inside our big
mechanism repeat each other like we have
posting for example it's part of a navy
in many areas or like we have the set up
tables which are very specific actually
they have just one record they have the
key that is empty and then you can do
get and get this record and it's the
same all over nav so those mechanism
that repeat are there already and they
are the wheel that we it is there for us
to take and read about and just using
our solutions why is enough patterns we
have done some research and with our
developers trying to figure out what are
they spending time on and if you ask a
developer hey what have you done today
and he or she will say I've peeps I've
been coding but if you take a look of
the actual at the actual process you
will figure out that in order to add new
code they will have to open the existing
code up and try to figure out what is
there and where to plug it and how it
makes sense to plug it so this means
that the more readable is your legacy
existing code the easier and faster will
be for you to add new stuff and this is
a nice comment that one of my colleague
colleagues has done he says avoid MC
Hammer code so do you know what MC
Hammer code can be yeah exactly it's the
call that success really can't touch
this it's like this big chunk of code
that just works and it's all interleaved
and you don't know exactly why it's like
that and you don't want to touch it
because you're afraid to break it
somewhere else so it just stays there
forever and becomes this big dinosaurs
okay so let's get to the patterns
pattern number one for extensibility is
called the argument table and yesterday
at the end of PRS session somebody has
asked
knowing that we cannot do function
overloads in nav how do we solve this
needs in a nice and elegant way there is
a pattern for that it's called argument
table it does a bit more but it's dead
delete also solve partial this problem
so the problem that this pattern is
trying to solve is using too many
arguments in a function and it's a big
religious discussion of how many
arguments are too many some people say
that three are two many assume that five
or whatever but the point here is that
at some point they begin to be too many
which makes it hard for you to change
the function signature because oh it's
easy to change the function signature
but then you have to change everywhere
where it's called so you do something
that martin fowler in his refactoring
book called shotgun surgery like okay
change it here and change there and then
maybe there's one place at least in this
case the compiler will help you and tell
you where you didn't change it so you
will not make a bug there is no function
overloading in Seattle so if you want to
add one more argument you have to change
the signature and you have to change
what it's called and if you're lucky to
use an option type and that option type
definition is changed by adding one more
option for example you have to change
your function signature again so how to
fix this it's in the title just group
together your argument and put them in a
table and pass that able to function
like this so this is an intentionally
exaggerating example but it's not
something that I haven't seen so this is
a function that was to fill in some data
into those wires in order to use it
later to fill in ova t return and it has
some vit declaration ID line ID and a
lot of cold verse and then it has a few
boards and so on and so on so when you
get to call this function you have to
kind of remember okay the first is easy
contours Bin's by the time you get to
the end you might just put through where
it's supposed to be false and reverse
this and it's just a bug waiting to
happen so how to make it better first
you get to make a new table and here
it's called the vit return data then the
function signature will be much simpler
it just gets this table bonus before
calling this function you can now assign
default values into the fields of the
table for example I want the number of
copies for this v80 to be by default one
and upload it is false anyways but
that's an example and then you get to
call the function simply by using the
table name so this time when you want to
add a new field you just started to the
table function stays unchanged except
for the implementation where maybe you
want to use this value but the function
call stays unchanged and functions
signature stays unchanged a second
example is from upgrade so if you want
to move your data well do upgrade then
you have to specify the old table ID the
upgrade table ID and the upgrade mode
which is an option field if this option
field changes for example now we have
chip copy move and for us if you want to
add a fifth then you have to add and
change the function signature as we're a
better way to do this is to group them
together in a table one thing that we
wanted to do with the design patterns is
to not only say why they are good but
also why they are bad or when not to use
them so here's the overview you get
fewer arguments it's a clear intention
of what the code does because now in
this table the field names are telling
you what they mean so you don't have to
remember that parameter number seven was
through something like that you can
assign the files value default values
and then you also can get validation
logic inside your
table it's easy to extend because there
is no upgrade problematic new fields one
note is that if you use this table then
the see the type of the table should be
temporary because it's not something to
persist in the database is just a
vehicle for your data through the
application at runtime what's not so
good about it is that you get to use
more objects and there is only so much
that you can do with putting stuff in
the table you can't put a table inside
the table okay pattern number two this
is a really nice example of why
community project is better than the sum
of the parts and this pattern comes from
one of our partners from waldo AK Eric
Walters who is part of partner ID
software and he said I facto so the
problem that while do is trying to solve
here is merge conflict during upgrade
and the more upgrade you get to do and
you have the chance now to upgrade every
month the more you want to solve this
thing that is going to become a
repetitive part of your process how to
make your product more upgradable
solution is just try to minimize your
footprint so if you think of the nav
standard code the one that Microsoft is
shipping think of it as a minefield the
more you step into it the more chances
you have that will refactor something
and it will just blow up in conflicts
next time we give you a cumulative
update and there is the other side of
this story so on the other side there
are Microsoft employees and I know that
each time somebody comes somebody new
comes in my team they look at the code
and say why aren't we write refactoring
this I mean it's so obvious what we
should do and we have three screens of
this function and a few hundred lines
and no we don't refactor it because we
don't want to cause you a lot of pain at
upgrade so then it's like we are keeping
this old code we know it's so easy to
make it better but we refrain from it
okay I have like three ideas in my mind
Stella but if you minimize your
footprint inside the code then you give
us the freedom to refactor it and then
you give yourself the freedom to have
fast upgrades and work on something more
interesting so there are two steps to do
this try to find the places inside our
application code where you want to hook
in your customization and write your
application code outside and just hook
it into minimally from the standard code
and here is an example on the left side
you can see enough code is called unit
80 and on the right hand side you can
see Waldo's code which will be plugged
into the code unit 80 so there is a
really nice discipline to this hook
pattern and part of it is that if you
name if you prefix your code unit your
hoop coordinates with one hook then it's
going to become obvious what is your
code that it is a hook and even if you
get to have a merge conflict it's really
easy to solve it because you don't have
to try to understand what was there and
you can read more about this pattern and
all the others on our wiki side but you
don't need to remember this because this
presentation and all the others will be
on me boo so at the end of the
conference okay so what is the result of
applying the hook and this is from a
while ago he was one who was trying to
upgrade from enough 2013 to nav 2013 are
too and he estimated that after running
the merge and it will take him two weeks
to solve the conflicts in the whole
product code with the hook implemented
by the book and i quote insanely meaning
that he really respected this pattern
the upgrade in terms of fixing multi
conflicts took 15 minutes and here is a
nice coat that i'm going to read for you
it's
upgrading from 2013 12 2013 are two
there was a change in quad unit 80 yet
that's a strength refactor where a piece
of code moved to a function and there
were lots of reactions from the
community like Microsoft please don't do
that now my code would merge anymore but
I only had to move online to that
function so if there is one pattern that
you can start to find where you get
merge conflicts and apply the hook there
first and see how much easier it gets
and then maybe you'll be convinced to
use it everywhere else okay this being
said I will handle my presentation to my
colleague mostafa who will take you
through the next patterns thanks for
dinner hello everyone so but with what
Bogdana has explained we had
successfully made our product extensible
upgradeable and we want to improve it
even more so now is the chance for us to
make it configurable in many cases we
have a bunch of code that we have to
extend or actually improve the behavior
this good is doing however we come
across a very complicated code that is
not easy to extend because the logic
itself is hard-coded so what we really
want to do is to make as many minimal
changes as possible when we are adding
new behavior or extending existing
behaviors so that it's easy to maintain
the code later if we want to also just
imagine now with multi-tenancy that we
have so many tenants on our product and
we want to implement the same change
over and over for them so that means
including their customizations that they
need we have to repeat that hundred
times thousand times just counted so how
can we address that and instead of
changing have the code itself is
implemented which basically means the
algorithm itself why don't we change how
they could behaves using some data we
configure the code behavior through data
and if we change that we change how it
behaves
they just look at an example over here
speaking of bank reconciliation where
you have some bank account from which
you can get a bank statement file and
you already have recorded do
transactions within a navy as ledger
entries if you want to reconcile the
recorded statement clients again it's
the ledger entries that means you need
to figure out which legend entry is the
one you want to match agonist the
statement files already have some
information like the cosmonium the
amount the document number the date and
so forth based on these different values
which will be your criteria you will be
able just to match the statement line
against the ledger entry if we want to
implement this in code how can we do
that the first option we may ever have
and don't recommend it of course is that
we just tried all the combinations for
mixing and matching these statement
files statement filed lines again it's
the ledger entries that will actually
give us a lot of if statements that we
refer to as forest of ifs it has as many
f statements as a first could have trees
but that is very complicated and will
just expand across so many pages if we
just keep displaying that on the screen
a slightly better example even though
it's still not that good is that we
combine each of the logical criteria
into one group and each of them will
just become an AC statement that's
easier to look at slightly easier but
it's not that good to maintain or extend
later just imagine one of these criteria
is supposed to change at one point of
time you would have to revisit all these
statements and all of that is going to
expand across three more screens if we
just implement this then that just
brings us the same idea about using data
to control the behavior of an algorithm
if it is generic enough so let's try to
use a bin and and a piece of paper to
write down this criteria each of our
criteria just a column on this drawing
and each of the values combined on a
single row will just be one rule if we
have this
and we will mend it at a table in nav
and it will become easier if I have my
statement filed line and my ledger entry
and then try to think what kind of
values I need to calculate to figure out
the right rule and eventually decide if
this is a good match or not so as we
look at the example we have today here I
know that I know that I have the
customer number in the statement line
and it also exists in my ledger entry
check I actually don't have the document
number in hand so I don't have that one
and I know that I should find a single a
journal entry that also check so I have
two things to match on and one that I am
missing using these three values if I
just use this against the table have
just constructed using filtering then it
will be easy to figure out which you
roll it is and eventually i define I can
actually determine the confidence level
from my match easy and clean how can we
ever movement this in code so for each
of the criteria we had come up with each
of them will require a calculating
function so one function bear criteria
and that is an atomic function that one
has one responsibility to take care of
and it's easy to write and after
calculating these different values I
will actually be able to just apply some
filters and using these filters I will
figure out my confidence level on the
match I'm doing so one two three the
table the calculating function the
filters done what if I want to add more
rules as we as we described a role in
this case will be a row on my table and
that means because it's an nav table I
can just add as many rows as I want it's
easy if I do that as long as he still
makes sense as a rule and not duplicated
because well location won't help you but
if I add one more criteria that means I
need an extra column and a column in
this case will be added to the table so
for example if we want to add the
criteria for G for finding those matches
that all over do you then I add a column
to the table and just add a few things
to the code the first thing we add to
the code is we need to add a calculating
function just to figure out the value if
it is a yes or a No as we have seen in
the past the slide and also i need to
add the filters that will just run
against the rules stable they have
already defined so that is sample where
else did we use that we had the data
exchange framework introduced 2013 or
two and that helps you create
definitions for files that you export
and fold you import any kind of files
but mainly we use that for banking and
stuff like that but still you can export
any data or input in data as you need
what you do is you describe the format
and after that the framework we'll just
act on your behalf the heavy lifting is
done you just define it the same
approach has been done for every star
templates and configuration templates
you just describe what you want to do
using data and eventually it just works
so what was good about that first it's
easy to extend the code is easy to read
and because it's extensible and readable
you will spend less time maintaining
that when it comes to upgrade and merges
your code has minimal footprint back
then I was referring to so it will be
easy to merge your code for and bring it
forward if you are going to deploy this
across tenants guess what the changes is
if they share the same application data
you do the change once and you're free
if they actually have this already
deployed we can still go ahead and
customize the rules we have after you
implement that for them just by adding
more rows if you want to add more
criteria it's one column to add and one
function type what could be a little bit
tricky if you have a table full of data
so as long as you maintain them to make
more sense then it's good but if we grow
beyond that they won't just be good they
will not be understandable never product
is in good shape is configurable as well
as
full and upgradable let's just make it
adaptable to the user needs so what we
see in many situations is we have a
product that has a lot of data but users
are different so you want to present the
data to the users according to what they
need so for example if we if we have the
data is stored in a master table and you
want to present this in a different way
using the same table itself and binding
it to a page will just result in a lot
of data so we actually suggest that you
can use something as a representation
layer or an interpretation layer and
that one would be basically temporary
tables that we will see in an end exam
after a while as you make a temporary
table you you basically make this off
the main table and you have the mental
validation triggers but not all of them
will apply when you're going to present
the data so you should remove as many of
as many of them as you need as you don't
need because you don't apply in this
case and as we all know our result of it
should be free of the business logic you
should have it factored out and good
units and tables according to good
design practices how can we do that we
should ever be described create the
table of the main table and use that in
temporary case so the the idea basically
here is your main table is the model and
you have the view that the user to X
with this is one hand and the other had
the view so the layer in between will
just take care of offering a subset of
the data getting bound to the bed and
represented if we carry the same analogy
jav their model in this case is a table
already stored in nav nav database it
against which you can insert update
delete all the kind of actions you want
to do and the view in this case is a
page with asians and fields and so forth
the layer in between is a temporary
table that
a subset of the actual data it's
temporary it's shared in memory it can
be used and freed later so how did we
use that in 2015 for the bank
reconciliation feature we keep going
with that feature because it's a
feature-rich we had some local
implementation and that one was offering
a good value for the users but the
universal mutation we have been w one
has evolved over time to cover the same
features and on top of this it even
offers integration with importing bank
statements and automatic as we described
in the previous slide so with this in
mind now the users have the choice
should she continue with the local one
so should we move to the universal one
we give them the chance to decide on
their own the business should be go
should continue to grow and go on and
whenever they feel that they can move
now they just make the chance the choice
how did we do this we decided to offer
the users a single point to start from
and from that one if they stick to the
locale all data they still can use it
from the same place if they decide to
move on and migrate their functionality
again is the universal w1 implementation
they have the chance and as the user all
centers all the statistics showing up on
the road centers will reflect the right
can't numbers depending on their choice
and the choice is easily made through
the general ledger setup so basically
the users will be sorting from a list
page and that will be the access
point to what whichever cards we need to
interact with and these cars will be
will will be the bin been amended on
their choice the in local feature or the
universal w1 feature the table bound to
the list weight itself is a temporary
table and that table holds the subset of
the data they are supposed to interact
with depending on what kind of frequency
use the temporary table will just
reflect the subset out of the devil you
on table or the local legacy one with
that in mind we can just look at the
graph / hate understand how it works
so the moment the user has the list page
open and they start trying to access
whatever function as if you want through
the beige there will be that question
which one are you using and that depends
on the choice you have already done they
have the ready-made and mapping of the
data into the temporary table will be
done based on that if it is the W on
data then it's clone mapping if it is
the old legacy data then it's a custom
my link and we will see that in goods
excerpts later based on these users do
that actions as it plays and whenever
they are done the data is updated inter
permanent cables and everything is in
place as we expect seamless experience
it works well and they just made the
choice you need so how does it work the
subset the temporary table it's built of
the main table by finding the proper
records users are using and then we just
make cloned copy but if we are using the
locales table then we actually find the
fields there the records are interacting
with and based on that we do a custom
mapping as you are able to see over here
feel to feel as required then the
temporary table gets bound to the bed so
the there are different actions on the
bed is for kidding new records for
anything listing records or deleting
them and all of these are just dependent
on some functions we have already
implemented in a code in it and that
could unit hostess the functionality
will require so the trick is we open the
page cards that the users will deal with
and just hand off the record debate
should act on and that one depends on
the user's choice speak the local one or
the old one and the data set the
temporary data set that we are acting
against it shared between the card and
the list and if one of them doesn't
action the other is informed and the
data is refreshed
so after this the user gets to you the
page what is good about it the you can
using this pattern make sure that you
resent the right data to the right user
bending on their scenario you don't need
to offer the whole thing you can just
offer what they are concerned about or
interested in and one other example that
comes to mind is the customer card the
the actual customer card is so detailed
and full of full of fields and actions
for good but if I'm a very infirm a
small business running very small very
basic scenarios I would rather use the
many AB and use the mini card which
offers me a subset based on templates
and the best of all is you are moved
trying to encourage your users to move
on to new features which will offer them
more more capabilities so you still give
them the choice when to do that because
if they are running their business on
some kind of feature you have already
done some investment and do moving
forward should be done when they are
feel free of that what could be tricky
is that should be used whenever you are
going to present the data that means
using your user interface but if you
want the functionality of a view in
terms of a scale that means you should
be using a query our product now is
successful extensible configurable and
adaptable this make it even more
user-friendly we tend to use dotnet
classes different look Nick classes
because they offer us some features that
we don't necessarily have today in ncl
but if something goes wrong with using
one of the classes we get an exception
back exceptions are very detailed when
it comes to error messages and you're
ugly and then no users then we need to
handle that but we don't have the luxury
of using a try-catch in CL yet then how
can we handle the exceptions so here's
an example let's imagine that we have a
hypothetical feature that is supposed to
own a catch a foil cash and if the file
is not there
there will be something to be done and
if the file is there it will be just
used so the code in this case that will
check the file existence and use it
laser is revved in a good unit if it
succeeds we are we're good to go if it
doesn't we have an exception to collect
so you following the same bored I'm as
exception handling and C sharp we have
catchy statements using a case statement
using that one we should be able to
figure out which type of error has
happened using the gate dogma type
serial key word and that one helps us
discriminate between the different
possibilities so how did we use that or
where did we use that we had the need to
integrate nav features and extended
through other web services available
outside so we came up with a web service
management could unit that helps you and
you should be building on top of that to
integrate with external web services so
when you need to do this you have a web
request in hand that you send it off to
the service if everything is fine it's
good if not if something goes wrong you
get an exception back and when that
happens you need to find out which issue
it is and just display an error to the
user in a friendly way we use that with
the bank data conversion where we had
some files to change across different
formats we had a method from at that the
web service is accepting we send it off
so we get back a file that could be used
for bimota export or bank statement on
board and we even had a service to
integrate with for bank name lookup so
that web that good unit web service
management should offer you the chance
to integrate nav with in service
oriented architecture deployments and
integrate with services and have even
more features added to your nav so
keeping up with the same example about
bank data conversion we send the file
the man in the master from at the web
service is going to accept and we get
back foil in a bank specific format if
we get the file we downloaded to the
client and the user is a free to use it
otherwise we have an exception that we
need to handle and from the exception we
get error and displayed in my speed so
where is the magic basically we have
good unit that will interact with the
rebbe of the functionality to for eating
these files and that means we built the
web request and run our food service
management code unit we make it back on
the on run trigger to actually return
understand back at true or a false if it
succeeds and return is true everything
is fine we should proceed on if your
turn is false that means an exception is
thrown and this is the moment when we
actually collect the the exception and
start analyzing it after we collected we
have to figure out which type it is
using goodness my good get dotnet type
it's that's very long to use anyways we
collect that and we understand what type
it is and as soon as we have it from the
for the type we expect in this case it's
a web exception otherwise we just throw
it a game and pop what's up we get the
response out of it and then get the
message out of it which is according to
what how the web servers behaves will be
just an examination of something is
missing something needs to be changed
currency is not classic code is not
compatible stuff like this so where is
the trick here we have one more key word
to remember today which is get Lester
object that one helps collect the last
exception that was thrown and we use the
dotnet function for getting the root
cause get base exception because usually
when you get an exception back from my
Navy service it's trapped into inner
exceptions a long chain of exception so
you have to find out which one is the
root cause why is that good and helpful
because it's as it looks here it just
easier to customize you have your sail
code in line with your dotnet code and
you you know both both of them so it
will be easier for you and all the
to change and you carry this on across
different versions and deploy that to
your customers using text files or folks
as you are so used to already and when
it comes to migration across releases it
would be easier to upgrade you don't
have any evidence or a external control
that you depend on it's your CL code and
your net good to move on and best of all
you do what you do best right feel good
but there is a catch the catch is if you
have a well chained invocation of good
units so a good unit you are running it
and there's that good unit is running
one more konyen underneath if an
exception happens then it you won't be
able to catch catch it properly which
means our recommendation is reb of the
code that will that is expected to throw
an exception within one code unit that
you're on just look at web service
management good unit as an example in
this case our code is good our product
is fine and I'm hungry so it's it's time
to actually do some cooking who likes
cooking so time for recipes they were
next one to speak about is web services
let's imagine we have a web service and
that will offer us some data and that
data is supposed to be up to date to
some extent so the choices we have it or
the first one is to continue to be
connected to the web service so the data
is always up to date that's good but we
may encounter network latency service
downtime all these sorts of things the
other choice is let's just make a copy
of our data back into a table in nav and
at the moment we do this the data is
already old it's out of sync we don't we
have to maintain it somehow and that is
expensive and what could be the
alternative choice we can actually get
the data both the data out of the
service cash it and reuse it and then we
refresh it periodically according to
have the business requires this so if
you are going to do it this way
there is one example we have in mind
about bank names these bank names we use
to communicate with that another web
service to figure out which format we're
going to change the file to if we have
the data already cached and it's not
outdated we just get to use that one
otherwise we will have to figure out
which country code the bank belongs to
and based on this we ask the service to
give us the proper bank names for that
one and that is a subset of the overall
list the service can offer us so the
footprint we download here is very
minimal and also only when needed and
being outdated so the data is stored in
a table and nav like any other table and
it's it is time-stamped so it's easy to
figure out if it is outdated or fresh
and it gets a display to the user
through beige a list page that lists
page works in a regular mode like all
other less pages or in look up mode when
they need to use that from bank account
card the beige is going to offer the
chance to refresh the date at the moment
it detects that the data is outdated
otherwise the user is always going to
have the option to refresh the data the
moment they need to where did we use
that we used it for payment export
feature we will generate a bank specific
file formats so we need the bank name to
communicate it to the web service that
dot the conversion and from this one we
we get the right file and give it out to
the user this is how the page looks like
where each of the bank names is already
time-stamped and associated with a
country code and the user has this
action to decide if we want to refresh
it at some point of time how does it
work the moment the page is approached
by the user and open it tries to figure
out which country code we are going to
use in this case because bank name banks
are going to be tied to a country and if
there is no data at all it just goes and
go ahead and fetches the data from there
service otherwise it tries to figure out
if the data review we really have now is
outdated or not if it is it just go
ahead and which is the date again and
now we need to figure out what's good
about it so there is no need to worry
about time out or the web service being
down or no network connections and as we
as we embrace the cloudforest mobile
first world we work across different
devices in different contexts and we may
or may not have a proper connection so
if we get the data cached then it's
relatively fresh enough according to
what the business defines what could be
tricky is we depend on external services
the more we integrate with external
services the more we depend on them and
the value of the code at the value of
the data in this case it as good as the
services up and running so with this in
mind I get the chance to hand this off
to a nurse Tarson I almost have Jeff
hello oh no I'm on oh so now to
something a bit older copied argument
that's an old function that we have in
our application so as a developer I
cannot live without copy paste and if
you have to do with a document structure
the user will expect that you will be
able to copy from Juan structures who
are nada or within the same structure as
well and the only way to do that and see
al is to create a co tuning code unit
for mapping the fields something like
this
if you just take a very simple flow
diagram here the user create a document
hater run the report there I sorry
invoke the copy document and we have
this little function that do the magic
looks pretty simple if we look at it
from a component perspective it looks
again very simple that we have a
wrapping code units arriving report
sorry for for calling the coach unit and
actually we are utilizing the fact that
we have that request page so you can key
in paramètres for free and that just
call this quote copy document management
code unit that's an awful long name that
do the trick of copying from the source
to the destination but some of the
problems you have then you have curtains
like this that it we didn't have we had
we have a lot of implicit implementation
patterns if you look there are at least
two in this code unit is by the way a
huge code unit it's the first slot is
code unit we have in our base app that
by itself making a bit terrifying to
look into the validation order on our
document line we assume that we have a
certain order that we will after we have
created a document line we validated by
time number on the invocation very end
unit of measure and then we fill in
quality and amount unit price in that
case here
so that is actually even though it looks
like we have D cobbled the document from
the copy document we have that we depend
on there's a validation order over here
another implicit implementation pattern
is that we need to implement fields in
table consistently to get transfer order
to work it is used widely in both copy
document and also in posting of document
so Dom bar data type and length must fit
otherwise a last word around copy
documents inside have that high class
coupling it is actually one of the
object we have the highest his coverage
for an hour bass amp so the more you
Kabul code to bail on you more code
coverage you need to have select
distinct it will be nice to have a
select distinct out of the box in the
older days not that many years ago you
will use say trains find last remove
some field that's fine next or whatever
or feel it into a buffer table now we
have the crabby for doing that configure
some parameters in a query and have a
total column to trigger that grouping
the majority of the audience here are
from Europe so you know we have this v80
thing here in Europe the majority of our
document will say the footprint in here
some will say it even more if there are
more VHT types on our on a document and
then if you want to have a select
distinct in this table based on document
number one line per document number you
can configure that by using type
document type
and document number and the query simple
query look like this for those of you
who remember the old reporting stag you
will also remember that the reports back
then was actually also very good at
doing select distinct so when we moved
our reports tag from the classic to our
DLC there were a few issues reported in
many one of the issues was around the
vet year's report where we when people
should import the interest at or the VA
T we fetch all the VA T entries and sent
them to the report layer and let that
let reported it to the magic it went
very well on on sassyxx tag but
unfortunately on our dlc it could crash
so that's why we also implemented that
pattern here in the report 19 using that
query there and of course we also have
related pattern like a user Tim table or
buffer table CL guidelines when I was a
bit younger than now start developing
making nav solutions I was pretty part
of myself to begin with then I show my
code to a colleague he gave me honest
and candid feedback it looked like
then a few days later I took up my ass
myself together to ask him and you
didn't like it and he said and us first
off you're not following any card line I
said at all I cannot read that quote you
have wrong indentation or wrong spacing
you use wrong variable name its foo foo
and then back then in the old days there
was actually DVD cvd where there was the
guideline visible and then we were
supposed to follow them and we did that
also
when I joined Microsoft 11 or 12 years
ago we also got those guidelines handed
out by paper but you know put it in
that's not so nice so 78 years we get a
gating so every code which we touch or
change should follow the rules that we
had agreed on to follow and I hope it
have increased the quality it have least
increased the readability of the code
that we are producing I will not go to
all the CL guidelines here there's a
bunch some of the Matthias space in
entation whatever I will go back to
where you can find them later on but
let's take a few of them here to rules
about paramètres something with the wide
scope I love wit scope sorry and then
this little buzzword cyclomatic
complexity how many know you how many of
you know that word good you will learn
something new then parameter says that
these two rules of parameters you know
you can declare a string and you can put
in % 1 % 2 and so on placeholders there
and we will actually like to have a
match when you call that string that the
number of parameter should match the
number of placeholders an obvious one
this example is a bit of course bit
simplified so to be able to check into
the product it should look like this
another one
and i think is a bit more important that
is calling by reference when you look at
a piece of code or procedure i will at
least look at what is called by
reference and expect that that will be
change in the procedure we have a rule
that if you call by reference it is not
for fun you must use it
another one this is a tricky one the
width how many of you use with a lot oh
so the problem with width is if you use
with together with auto variables then
you must know exactly what fields are in
that table in this example here of
course you all know nav so will that you
know that service contract here I have a
feel where it is called contract type
and it is actually if you Deepak and let
often happen when you have to do with
with that you actually need to debug and
debug is time-consuming in this example
here of course if you change the the
calling parameter is to be something
that is not within the scope of the
width then it goes more gracefully
and I actually often if you use with
that is because you have a long list of
field try at least if you use with to
isolate that into a procedure and have
only that little finger there this one
cc it is supposed according to
literature and browsing to the net
should be commonly widely used it is an
attribute you can use to describe your
code like you don't have to tell young
developers that they write shitty code
they have to high cyclomatic complexity
or they have too many lines in the
procedure so it gets something that you
can discuss so how to calculate
cyclomatic complexity its numbers of
decision in the code plus one so
whenever I comes to a new decision and
if for case I just increment the CC for
that trigger hmm so here yes in CL we
consider if and case s decisions you
know you actually see if an if then I
start to think and the same goes with
the case actually when I was researching
here the other day for preparing I
realized that for and while also
decisions so we might look into that
rule laid on so now we have a number for
the crew that we are riding some
consider 20 to be the absolute maximum
others concealer 30 to be the absolute
maximum of high highs cyclomatic it also
took me a month or two to learn to
pronounce that how high that ma numba
must be we having a magic number in will
bake let's call 25 and it is actually
zoom magical that it have disappeared
from this fight sorry
but 25 is the key number so now since
none of you know what it is or very few
there is an opportunity for even a
t-shirt here remember most of her
shoulder piece of code Hugh middle come
on no lower 1138 close 12 to 12 we have
yes Suber the funny thing is actually
when when when before I know anything
about cyclomatic complexity that did
curl here look a bit torchy just for the
fact of the many lines and also I know
that this is only a sniff of that quote
one little additional comment I said we
had the rule that you are not allowed to
check in new code or modification of
existing code if you exceed 25 we have
that little exception because some of
you know some code unit 80 90 if case
blah blah Papa and not to completely
ruin your world by changing that all the
time we have that little exception
unless you only increment with one but
otherwise that will actually have forced
us to whenever somebody Turner the trots
quoting the 80 to do a refactoring there
we do incremental refactoring on the dot
G code unit from time to time and we
will keep on doing that but only
incremental we don't have a huge
refactoring project going on or at that
plant yet but I must have made also MC
Hammer is close to cochin 8080 from time
to time this is a high risk function to
change but hopefully over time we will
have something more simple than that all
of our code base now this aren't pattern
male pattern cookbooks coming up soon or
the CL guideline who is a part of this
is an open project we are some from
Microsoft and some from the partner
colonel could those of you who are
present and active here or named here
peace raise up stand up mussafah up
thank you say hi
you can try to search for an app design
pattern on various media sand places
please if you read something anywhere
any day around the Sun pattern he was
some feedback is it good what we are
written a writing or bad or yeah and if
you feel inspired to join or contribute
to it would either an idea of a
suggestion please feel free we have the
bigger place where we poppies all our
patterns where there also is a contact
person back there now I can see if you
want to join so what are we planning to
do in the upcoming time a new pattern
per month don't take that literary
understand that as a 12 to 15 over a
year soon all the guidelines that we are
using in will pick for gading will be
poppies at this VG hopefully laid on
some chillin all some but to begin with
to have some visibility around what we
consider as important to you and then
also since is a vegan you can also give
us feedback unless you disagree have
strong opinion or have suggestions for
good guidelines to to have so think
laughs in design 10 are there any
questions
yes cyclomatic complexity cyclo cyclo
cyclomatic yes yes yes f4 is a decision
and we are missing that and so a while
yes I totally agree yes that was a good
one actually that was completely correct
in the example that was 13 because i
forgot the +1 or did I for gods who in
it my very able or yes it was it further
yeah that was because we caught off the
coast of Appeal yeah oh yeah yes one
more hey 14 that is why we have
automated that gating I don't count that
precisely so said 13 okay unfortunate
row is there a smart way was not pattern
to avoid the field validation order
dependency if what if eyeing if there's
a pattern to avoid field validation and
no right here yeah yeah there is a
problem if you change validation
procedure you might break validation
ordering some other procedures so are
there any recommendations about that are
talking about the argument table or
generally generally when you copy copy
documents until some of the implicit
pattern I hope that we will be able to
document them better either at the vig
aside or other sides
and and then in an ideal world you
shouldn't have that dependency that the
class need to be validated in a certain
order you should have called that class
with the parameters and let's one place
take care of the validation in yes yes
when I look at something cooties or
wherever I i take my we are there we are
and we need to move on to something
better I agree we have a lot of death
and inherent that that we cannot fix
overnight we also have to add new
features to keep the product alive but
yes this is something that we are where
we will address that by both documenting
that and do incremental refactoring
actually the incremental refactoring is
the best way of doing refactoring so you
refactor the surrounding code when
you're touching something instead of
rewriting all of it yes in in the hooks
better is there any plans for in
Microsoft to extend the hooks pattern
also using the argument table so you can
configure your hooks yay we might do
that that is something about having pre
and post event more sorry the question
was are we from Microsoft looking into
to extending they are to enable you to
an easy way to do the hoop patterns and
we might consider some event of pre and
post event I don't know when it's going
to happen but we are looking into that I
don't know we're for doodling corfu
timeframe or later but it is something
that is nice to have hello would you
consider documenting in the code units
the preferable positions to put hooks in
order to get a nice flow data if we will
document the document is the code fluor
on the table we have to get a nice flow
oh so understandable it would be
interesting to encode 84 for any
beginner to know where to put the hooks
in order to get the data to the right
places I think the question is if we are
going to show from before I where to put
the hooks that's right well that partly
depends on your implementation so and I
think we don't have any plans for for
showing who couple places as well so
don't know how we are going to change
the code in the future
is it a new design pattern to use a
speaking name for text constants because
there were some enough 2013 speaking
names for these constants oh yes yes and
that is for readability that we will
like message to be prefixed with MSG
arrows with er are that is to improve
the readability that's part of our
guidelines not one that we showed today
but we're going to put it on to Vicky
that's a good catch but it's not the
pattern was more like a cutlet it's an
implementation having your character in
star card yes next question here hello
in visual studio there are several tools
to to check your coat so what's what
kind of tools are you using and is there
anything planned for innovation
internally we are using a tool called
pre care that is a component building
g-sharp it have you feed it with a
reference file the latest baseline plus
the Delta that you are gonna proceed I
don't know what kind of tool will be
able to offer you moving on but if
nothing else we will try to see if we
can release the internal precalc to with
some direction on how to use it but
generally to have a professional
communities working on god there's would
be nice to have this tool however there
is no plan now we'll see what happens
web service was it yes
hello bud question about see who design
pattern we are using in since version 5
and I like to ask if it's a possibility
to get current coat unit in a court unit
so then I can pass the instance of my
current court unit to another coat unit
to work with this which helped us a lot
to make better hooks for Courtney 12 and
something like this that's a good
suggestion we don't have it right now
but we will hand it over for sure
actually it's not the first time I hear
this question so it turns up like this
repetitive wish coming for this to
happen but again it's not in the plan
now I did I really agree that is
something to have it would help a lot so
the more times you ask chance it it is
still happen when you were talking about
cyclomatic complexity it ran me over a
limitation we encountered a while ago
when a colleague of mine wrote some very
very well a huge piece of code we'd
encountered a limit that the number of
parameters plus the depth the how do you
call it the complexity depth of your
code as a limit I don't remember exactly
which we consider like five years ago or
more but if you had a lot of parameters
in your function and your function had a
lot of ifs that went very very deep
there it wouldn't run or compile even is
that still present at limitation I hope
so if you have a lot of pair meters and
a long list of coach I agree it is not
supposed to do that but but another
while talking about cyclomatic
complexity we also have a restriction
that you're not
to allowed to have more than hundred
lines in a procedure for good reason and
that should be sure if you ask me I also
have to little feature requests that
that I think will make life easier for
the developer one is an obvious one
that's been touched upon try-catch is it
plant in some form foreseeable future
two versions ahead or something we don't
actually have any plans concrete plans
for a try-catch clothes at the moment
because currently the code unit run like
you said has a limitation in nesting and
or multiple right of during right
transactions you can't try to use it
that is true we know we are aware of
these limitations and we are trying to
see what options we may have but no
concrete plans are in place for the
moment but at least as it looked like as
we describe it you still will be able to
catch the exceptions because we have
this in a life implementation with the
web service integration we have talked
about today so it is possible to follow
the same approach as it is today I hope
we can improve it further for the sake
of everyone and the last just went off
sorry the last one was smaller I think
on after insert straight on there on
tables so you can update totals depend
depending on after the insert make it
easier to read these are this is a good
idea that I think that Thomas in the
keynote has mentioned that we are
thinking about event driven development
as well so hopefully that will happen in
sometime somewhere time we just hope for
that now okay so actually one of the
nice rims of people who are writing
patterns is to see some of these
patterns retired meaning that they have
been replaced by platform features so we
don't have to do the pattern workaround
but yeah the first step is to find a way
to do it
then if they will be retired will be the
first ones to celebrate hello about
pattern testing and artistic try-catch
about dotnet inanition you use and if
coach onon run construct why you do this
why cause it does a commit I have to
commit my data when I use a coat unit
run if you do if coding done run it who
you are handling the arrow that that
code unisys room so if there's an error
within that code you know you ignore
that yeah well then matter if not every
time when I use the dotnet variable in a
vision I want to commit my coat that is
true it's a limitation we're aware of so
well in the invitation we have shown
today with we don't have a single line
of that is going to commit the whole
process is going to happen and whenever
it is done it's committed if something
goes wrong we have the exception in hand
there is a this is a very correct
limitation you have just mentioned and
we have encountered this way we will
trying to develop scenarios in which we
had to run the good unit throughout the
right transaction but this is what we
have for for the moment and we want to
improve that we are looking into how we
can improve that so hopefully in the
future as we improve it it will be
possible to not to require commit if we
actually have a different approach so
it's something we are aware of it yeah
thanks for the good question Frank we
have Otis one hi hello so I had two
questions actually one way the is about
this if coding is run so for in your
example the whole concept of if
coordinate run was too
an exception and present in a human
readable way but basically I have to
commit before that so if i have like
asking a web service after something
happened I still want introduction to
roll back it depends on where when you
call that and it's not called Ron modal
so you don't need to commit before you
do a coating it up but if you do call if
code unit run this just will if you in
the middle of transaction so basically
just writing something into my database
and then confirming with the web server
that actually it's correct and I want a
human readable error on my screen so
it's more not more of a question but
more of a suggestion that to have a
command and nav to actually roll back
but keep in mind one idea if you ever f
you have a right transaction in progress
and you want to run a good unit that
actually well we have two concerns two
responsibilities here that we are
concerned about so just to make this to
the example we had today we were
actually pulling data from the service
and if the data is in place we will try
to use it later but if I if I have a
right transaction in progress that means
they have some functionality that acted
on existing data I should take care of
this one first and whenever it is done I
should just interact with the service
because the service should be active
acting on the data I have already on the
database so I I don't see a huge issue
if if I actually well divide the
responsibilities across different so I
think it can be redesigned a little bit
yeah i agree that so basically we can
use the temporary table down in the
famous we had shown over here for
processing the payment export files and
bank statement files we take the whole
thing in memory and we just go through
one transaction if it succeeds you have
the data you have the file you're done
if it never succeeds nothing happens I
mean nothing gets committed to the
database so it depends on how you
approach it I think you just need to
just look at the design once more to
separate the concerns first and if you
do that you will not have the issue of
committing before you proceed even
during our testing scenarios automated
tests
scenarios we had to create it and
proceed with that so we with proper
design we were able to we were still
able to proceed with with that approach
even though we were running a good unit
okay Mike signs thank you very much one
more question then about the argument
table pattern it all sounds great
including them using it myself sometimes
when I have like very complex functions
around but the challenge em coming
across is actually in this case if I add
a new parameter and they really want
this perimeter to be populated I cannot
catch the exception before the run time
because the compiler will just say oh
you pass a record it's fine not like for
example have ten places calling this
function and I really want this
parameter to work fine for all my
previous code so what you're saying is
that if you add a new parameter will add
it to the table and it's not used by the
function that should use it so for
example if I do that the classic way
adding it to the function just compiling
all the objects will give me the
basically it's gorgeous yeah so I have
just two exporters in two tags and then
just find that were used as rainy better
way well there is a trade-off between
the flexibility and the compile time
error messages and detection of issues
but so either you opt for this the
flexibility or you opt for as many
parameters as our colleague was
mentioning when you'll hit the
limitation and then anyways but I think
there is a trade-off if you have three
or two parameters maybe it doesn't make
sense to have that but if you have if
you expect your design to grow over time
and you better of opt for the
flexibility well it will reduce your
maintenance costs along the road anyways
so it's a trade-off you have to decide
on it's a trade-off but also is a good
request for for further improvement to
see where I have used my table yes
especially as a parameter okay thank you
very much thank you
I see no more razor still one over there
yes perhaps more a remark and not a
question about the hooks and wouldn't it
be nice to define the code unit or the
function as a hook so we can identify
where hooks are used and when we try to
upgrade the code so that we can ignore
those parts automatically so we can
identify this this line is calling a
hook so we don't have to to bother with
that so the platform doesn't help you
now with this the only thing that you
can do is to post fix it so fix it with
the hook but it would be nice to have it
of course that would help
hi regarding the functions and the
parameters you have when the way you you
change the parameters to a table
wouldn't it makes sense to use a dotnet
functionality to have for example a key
value pair with in.net class and then
set those values before running the
function and just give this dotnet
variable as an parameter and get the
values inside the function afterwards so
you can work with arrays and address the
information within your co dot net class
so that would be an alternative
implementation yeah so but this way
would help to reduce tables and
functionality inside in a nav to blow up
those values who just want to over take
in the function yeah it depends on how
much you want to hook into dotnet code
or how much you want to keep it CL and
of course the tables are it matters for
you if you create new tables so then
that's it but I think the point of the
pattern is to gather your data
encapsulated into something and pass it
to the function okay that's a good point
we have one more pin
hello you said you want to get rid off
the buyer efforts parameters when you
don't return a value wasn't it the
function parameters you want to get rid
of the by reference if you don't return
a value oh isn't it's not that you get
rid of it but you're encouraging not to
pass a valuable as a parent an argument
by reference if you are not going to
change it inside the function yes but
for for equity standard use by happens
because you don't copy the data then
open the whole table table records but
you're going to change them but behind
the scenes the server takes care of
managing memory on your behalf so when
you best buy value by reference you are
just instructing the server I'm not
going to change the value if a change
happens give me an error but the server
behind the scenes is actually using C
sharp good and these kind of things and
it takes clear of memory management on
your behalf you need not worry about
that you just need to worry about what
I'm doing is going to change or not to
change so you in the standard vision or
the table parameters are not by
reference anymore we haven't modified we
have and you will see that when we
reveal all the guidelines that you will
be able to find violation of those
guidelines because it is only when we
change the code we we implement the
guidelines also okay thank you
last question otherwise feel free to
come down afterwards okay thank you
thank you good question
