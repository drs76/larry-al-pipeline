# BC TechDays 2022 - Improve the quality and readability of your code using tools from Microsoft ...

- **Source:** https://www.youtube.com/watch?v=n3Hj673X3DQ
- **Video ID:** n3Hj673X3DQ
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 95m13s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

foreign
[Music]
foreign
ladies and gentlemen welcome to the
second day of our BC Tech days your
first speaker for today is NJ
good morning it's nice to see you all I
hope that you have a nice evening
yesterday
yeah probably a very long one
and I
I unfortunately have to prepare so yeah
welcome to my session
about quality and readability of the
code so before I start let's just
introduce myself
so my name is Andres rashkovsky very
hard to pronounce in some countries I'm
working on currently as a development
standard leads and enough people
um before I was working in that company
in the product Department
and yeah probably if you are seeing this
slide you are thinking that company is
not very good in choosing names you know
choosing the name that follows the
product that's not a good idea but
that's just the name we're using
marketing we have another proper name
that is completely immune to Microsoft
ideas of changing product names it's
very big limited yeah so if they only
haven't moved
so yeah that's what I work I'm a
developer I develop in a few different
languages a bit of c-sharp a bit of
power sometimes and I yell and sometimes
I'm also doing some JavaScript
typescript development
I'm the author of the azl dev tools
extension for vs code so if you are
using that's great if not try it
I have a Twitter account if you want to
just look here maybe not too many many
posts but yeah I try and I'm trying
sometimes to post something here and I
have a Blog that one was update very
long time ago because you know if I have
to choose if I want to write in C sharp
or IL or in English then well I'm going
for C4 and
scripts or Al usually so yeah so that's
me
oh
the subject
that was probably a bit bad choice for a
very long subject
and
uh
what I wanted to
do today I wanted to talk about
extensions that
people are creating in our community
extensions for vs code that can help us
develop
[Music]
but I didn't want to talk about
every extensions and every function
because it would probably be very boring
for for all of you so I wanted to choose
a subject and then try to find the
functions in those different extensions
that could fit into the subject so talk
about about
readability or maintain ability of our
our extensions and if there is something
interesting in one extension then I can
I would like to point you to that that
one and not on extensions yeah something
that to things that that Microsoft is
doing or what people in the community
are doing so mainly mainly extensions
[Music]
um
you know so uh
so that's what I wanted to do I know
that some of the subjects may seem
obvious but not all people know those
things so
I wanted to to talk talk about those
those things you don't have different
cases different situations so maybe
there will be something that that you
will learn or maybe maybe you have no
time to follow the rules but maybe you
will find a tool that that can help you
to do that
okay so uh
quality and readability
why I wanted to talk about it
first the the code is not only something
that we're giving to our customers that
will do something for them that's also
something for us for our other
developers in our team that they will
need to modify the extension they will
need to go inside change the code so
let's let's make it easier for other
people or for ourselves in month or
three months to read and and be able to
modify it and also we have to remember
that usually we are reading code more
than really writing in the usual we're
analyzing thinking so also this reading
to writing right here is greater than
ten to one so let's make our life easier
and also we are part of the team so
let's
try to help our friends in the office
work
efficiently and make their life easier
yeah another thing I feel that here if
anybody should be able to fix or extend
our code it's important to have
something less less perfect less optimal
but
easy to read so it's not you that is
constantly things your own code but you
can pass it to somebody else and you can
focus on on other on other things
and we have to remember that
but code can slow us down so at the
beginning we don't have much code we are
working fast everything is great uh
and and in time when our code base grows
we have realized that any change is
taking longer and longer and longer
because we have
a lot of things to consider we are
afraid that we break something
so it's better to have something
readable easy to easy to easy to modify
um
okay so what
what really can
can help us with with our
your development jobs
first we should be using Source control
probably a very obvious thing
that's a tool but uh
what we are doing we sometimes have a
customers that have their own developers
and they would like to together with
upgrading the
my system from Cal to Al They
they need to learn how to develop
because they have one two developers
doing maybe reports maybe some very
simple modifications and sometimes with
customers which is two hours and earlier
they have contractors and when we talk
with them they were not using Source
control they they have no idea what it
is so yeah so I'm mentioning it here if
there is anybody that is not using it
then yeah maybe it's time to switch and
we should educate also our customers if
they have developers of somebody that
Source control is something that you
need because it helps you also with
readability of your code
uh
another thing that
really
can help us which is not an extension is
the development guidelines and patterns
website that's something that is
important because if we know the
patterns then
if if you know if you know the pattern
then it's
it's easy to understand the code you
look at the code ah okay I I know the
pattern I know what it is I don't need
explanation what somebody is doing it
and also if you need to to implement
something you're not
you're not Reinventing the wheel you go
to the pattern you apply it everybody
understands it or should understand it
and call this code is better so so L
guidelines dot def that's the website
that you should go let's come we need to
run and Microsoft endorsed that's what
is on this website uh go there read the
patterns and use them
so that's that's a tool outside of
of this code but we also have other
stuff directly in in vs code we have
code analyzers those few
colonizers from Microsoft that help us
analyze the code and see if something is
not right but we also have
Community
colonizer made by Stefan Maloy that's a
fantastic tool you can also install it
that vs code extension you can find the
marketplace install it and it asks a few
additional additional checks
and if you need another one probably
it's easier to create a pull request on
on the on the Stefan GitHub
and
maybe he will be faster yeah Microsoft
has a lot of things to do that might not
be the priority to other colonizers but
here this one is
just a community created one and maybe
you want to create a pull request maybe
you want to add something yourself to
this code analyzer and then you will get
get faster result you know faster
analyzer that could help you inside your
component to
uh to have better code
and then we have vs code extensions that
are extending the functionality of vs
code so you can have the Snippets we can
have some commands that can do something
about code we can have code actions that
will make our development faster and
also we can have some additional panels
displaying some information helping us
to analyze the code so so when you want
to analyze what is happening here you
just download a new repository as the
first time you're seeing it you would
like to to check what is going on some
of the extensions can also help you to
to analyze what what's that
so those are all the things that that we
can have
but now
time to start talking about about code
what we can do
first before I go into any any examples
I want to talk about the setup
because I found interesting case when I
was looking at one of the repositories
some time ago so
in in vs code we have two types of
of settings or two places where we have
called Store settings the user settings
that are kept inside the user folder and
we have workspace settings and obviously
everybody has some preferences about
colors how the how they prefer they
develop an environment look and feel
that's probably setting that's probably
the the place for those settings is your
user setting is just for you but if you
have settings related to your
to your project to your solution then
they should travel together with your
with your code because to make sure that
every developer that will open that
project they will be working in the same
environment the result of the work will
be the same
because you may have rules for file
naming you may have some rules for
running some actions when you save files
and you don't want to have a mess
because some developers have different
settings and other developers have
different and then it's really you know
getting messy so that's the place for
this
for those settings is the most workspace
settings which are inside this dot vs
code folder in the settings Json file
and yeah and the last Point here is keep
workspace setting in the source control
that's what I found and I found the
project where a developer
header settings but put
settings Json into git ignore so he
probably missed the point you know
that's not the place where that's not
what it should be doing if you don't if
you don't want to share your settings
it's not the place where you keep them
so remember about it
okay so that's about about settings yeah
some simple things just remember why why
each of those exists
next one that's yeah very simple subject
magic numbers
magic number what is magic number this
is something that I hate magic number is
value of unexplained meaning so you open
the code you see numbers here there and
you have no idea what they mean and and
Robert Robert Martin or Uncle Bob in his
clean code book said that it breaks one
of the oldest rules for of programming
so please don't break the all this rule
of programming that's
not right
and and it's for example when you use
enums when you you should be using
genome so if you're not using them if
you're using numbers like in this
example here uh where I have a function
I have some
uh
and some numbers in the case just
probably develop and develop that was
using this Str menu function and get cut
integers from it and then decide okay
let's move code to the function but the
functions goes you know free code unit
is deeper then at that level we don't
know what it is and in a month somebody
will find the function that's a nice
function I will use it for something
else and then we start calling it with
the number I'll call the problem
somewhere and then you have no idea
what's going on there so
magic numbers are not very good and
Magic numbers are
sometimes in the project everywhere yeah
and we have those magic numbers in code
but sometimes we have also our magic
numbers in emails like somebody send us
email with just task number from a
project management system but
that's not something that we can do with
vs code but that's also another example
that's annoying magic numbers
okay next thing about magic numbers
hard-coded object like this that's bad
you're looking at the code and what's
going on here what that person was
calling I said do not hard code object
IDs just assign that ID and forget about
it and just I don't want you to remember
I remember the discussion a long long
time ago when we started working with il
and we have a meeting and one of the
developers I want to see numbers because
people in my project knows objects by
the IDS
want you to know that forget about it I
don't want you to see it anywhere so
yeah use
to use the the system menu types like
database or report
[Music]
instead of of those like integers and
you can also detect those problems if
you want and you can run it the Stefan
in in his business Central intercom
there is a rule that will check that you
know that's the number so so you can you
can enable it
and then you will see how many problems
you have
and I was like I have a problem what I
can do about it yeah and probably it
takes time to fix it so we will have to
stay with it because we have a budget we
don't have time but no we don't have to
yeah in in my extension there is there
is a function convert object IDs to
names you can run it it's probably five
seconds it can go through all your
project for through every file and it in
the places where it can detect that
that's that's integer here that's the
parameter that's that's object object ID
here so it will replace it with the
proper database report or page and the
name of it so your code will be more
table then you will be able to renumber
it if you want
and in the next version of business
Central if you take a look at what's new
what will be new Microsoft problem is
that we'll be finally able to use the
those items also in the properties uh on
on the object so the last place that
currently is stopping us completely from
from using IDs all the properties or
maybe
links between Pages where now we still
have to hard code object ID if we have a
table with object ID field it will be
gone we'll be able to
uh
to finally have proper very nice names
and the last thing here
as I said do not
forget about ideas so do not preserve
them yourself manually do not take the
first one that is free don't don't
do it just use any solution that is
available for reserving those ideas you
might have your own maybe you already
developed one maybe maybe you want
something very special you can do that
but if you don't have time if you want
something that works go for Al object ID
ninja from vehicle you just install it
and it works yeah so 10 seconds and
you're ready to go go for it you don't
anything install it that's the way to go
and
last thing here
had killed it object IDs in the using
object IDs in the file names don't do
that
don't do that we had a discussion
as I said at the beginning you know
years ago and
half of the team at that time coming
from Cars we want object IDs in fine
names because we are reserving them this
way and we can see those ideas people
understand
people remember object by number say no
you won't get it and as a compromise at
the end what we did we put the object ID
at the end of the name so they were not
able to order those files by ID but yeah
you have their you have your IDs and
that team that was shouting that they
want like this was the first one that
switched to Microsoft
ways of naming because they'd learned
that you know you were right we don't
need those numbers anywhere so
and then we switched to Microsoft tools
because yeah finally we can and nobody
nobody wants to have those numbers uh
and how to do it use filed extension
thank you Aldo
use the
um use the use those settings there is
also a command you can just open your
project type configure best practice
file naming it will add the settings and
you're ready to go remember it should go
to workspace settings and it should go
to your Source control so everybody will
have those names because the default one
is not this one and you don't want it
so yeah so do it
and now
next slide demo demo about object IDs
uh so let me switch to the
other screen
and time for some demo so I have empty
project here without anything uh
first thing what I would like to do I
want to make sure that I have proper
naming before I create any object
so I have that settings opened let's go
here and
um commands
[Music]
and I have a configure best practice
file naming I press enter and it should
start and should ask me about oh sorry
once again
best practice for naming first question
if I want to use a Works user or
workspace settings definitely workspace
maybe we should hide the user
so I will press enter and if I go to the
settings I have it
yeah I have those settings in the file
uh I also have the on-site file action
to reorganize you can have to organize
and rename there is a discussion what is
the best choice
[Music]
people that are against reorganized
don't like the fact that it creates
folder per object type
[Music]
and if you look at the Microsoft code
they are keeping objects grouped with
functionality
in the folders
but if you have a lot of people a lot of
developers working on this project and
you're afraid that each of them will
have different ideas how to group files
together
then instead of
having long discussions violent
discussions how it should be done maybe
you can just switch to reorganize and
forget about the problem yeah maybe it
won't be the perfect solution but it
will work
so that's the setting and now the second
thing that I want to do I want to create
a new code you need and
or any object and show you how the
vehicle vehicle ID ninja work so I will
just create a new file
[Music]
BC
code unit
yeah
and let you snip it
T code you need yeah first
I will press Ctrl space here now it
tries to connect to uh
to the internet to get the ID
hmm
that's interesting
I should see it and it was working
before
no no what's going on
CE again
control space yes
okay so again what I have here
I have two IDs I have one from
first one is from Al object like the
ninja second one is for Microsoft
extensions but I want to use the first
one generated by vehicle extension and
uh
keep the and his extensions keeps the
mappings somewhere in the cloud so
everybody in the team can use it so I'll
go for this one I will also
um
I will also rename the code you need
and
maybe not the best time that doesn't
matter and I will save it
and sorry too much typing
and I will save it yeah saved and as you
can see
the file name has changed and it follows
Microsoft best practice
so so that's how you can
make sure that you have proper names and
that you are reserving the IDS and if
you want to know more just install if
you don't if you're not using vehicle
extensions but you want to have
something install this one take a look
at it it's great uh so that's the first
example that I have but also have I also
have another one
I want to show you fixing the problems
so that's the um
that's the piece of code that I have
very bad one uh with numbers everywhere
I have
a coordinate right here I have
number here
I was surprised when I first time saw it
I don't believe that it can be done but
yes you can specify numbers next to next
to data types that was surprised for me
how people can be creative
yeah so here and also I have report run
and
I selected something that I have no idea
what it is it exists but I'm looking at
this code and okay 80 I can okay I know
what it is people remember but but this
one no so so I would like to fix it I
would like to make sure that
I know what is happening here so I will
go to the commands
and I will run the
um
command that will convert object IDs to
names
um so I have two versions of this
command one is just for a current editor
second one is for the whole project so
if you have a project that you want to
upgrade in value very bad
usage of those numbers and run the one
for the project but I will run just the
one for the editor just to show you what
happens inside the single file so
let me run it
it runs and that's the result yeah so I
no longer have those numbers I have
proper
size post code unit here I have here the
the number the record the record item I
have and now I finally know what I'm
calling here yeah it's return order
confirmation okay fine somebody somebody
put it here
so yeah so that's
um
that's what that's what that's what you
can do with with your
with your with your object object like
this yeah and one thing I just reverted
the change because I forgot to show you
that that I can see warnings
below each of those numbers here I can
see this yellow
yellow lines below and here I take a
look here I have a warning with
lc005 here so those are the warnings
coming from uh from the linter cup from
Stefan's uh kernelizer I enable it here
in the settings uh
and it shows me what is wrong with with
this code
so yeah so that's
that's the demo
let's switch back to the presentation
next thing
procedures
so what about procedures
they the rule that you're probably saw
everybody's procedure should be small
yes they should and and they should be
doing one thing and the question is what
that one thing means and different
people have different opinions what that
single thing not that one thing one
thing means
but one interesting opinion was from
Robert C Martin that for him the one
thing means that you cannot extract
another procedure from the existing
procedure
and here we have
interesting solution
from David fieldhof in his Al code
actions extension because he implemented
extract procedure so we have it now I
think David if he's here
now we have something that
help us follow the rules obviously you
know I would probably apply a bit of
common sense and I would not start
splitting four lines of code into
procedures just
maybe that will be too much too extreme
but there will if you can extract if a a
sub procedure from a procedure that
might be a good idea to do it
and also another rule about what
procedures is that the name should
explain the functionality of this thing
you should be looking at the names and
you know what is happening and if you
start extracting procedures then you
will have some high level procedure
explaining the process and inside you
have a call calls to maybe three maybe
four maybe five procedures but they will
really explain what is happening
different and if you're analyzing the
code you don't have to go so deep maybe
you will finish analysis of of that code
with trying to understand what is
happening here at much higher level
instead of going line by line and trying
to understand what this half of screen
is doing or what those three three
screens of code are doing
um and don't be afraid of renaming
procedures you can press f2 in vs code
on the procedure or on the variable type
a new name and it goes through whole
solution and renames it everywhere where
the procedure is referenced so don't be
afraid because AI sauce I hire some
people it's hard to rename because then
I have to go through whole code and do
it no F2 and it will do it for you
okay so quick demo extract
extract procedure
so let me first switch to
vs code
and open
my example
here
I have very simple very simple piece of
code
probably will think yeah that's enough
but as a it'll be good as an example to
show you what we can do
so
what is doing it's increasing prices on
on the order yeah so it applies a filter
and then goes in the loop and then on
every line changes the changes the unit
price but we could extract the procedure
because if you look at this filter go
through the records and then for every
record to do something so
let's just select the first part which
is click the ring and I can click on
this bulb after I select the code and I
can choose extract procedure now I can
type a new name of the procedure so I
will put the
filter
lines
and I press enter now I have just a
single line here and and a new lockout
procedure yeah Lookout is important here
then I have a second part now I should
follow it because if you leave it at
this stage
let's look a bit uh
uncomfortable for me because I have
coded to different levels here you know
so let's let's try to keep all the calls
on in this procedure at the same the
same level so I will filtering and then
I will be processing all records
not filter and then I'm going deeper
just next to it so another extract
procedure and then I will call it
process all lines
and I will press enter
so now it goes through through all lines
and if you notice first before I had a
variable here which is gone and now has
been moved here because
there's no reference to this variable in
the original function so we don't want
to have unused variables in code so
another great thing of this
functionality it picks the
variables and moves them to to those
lower levels yeah so that's what I have
and I still may think maybe maybe I will
still extract it because it's not doing
to one thing here it's
going through the records and then
processing a single one so again let's
select that one and go again for extract
procedure and I will call it
process single
line I press enter sorry
uh
yeah I press one key and
exit but yeah but in general that that's
that's the one actually I can press f2
and I can rename it quickly
Center here you see
it has been changed here and also here
so a second and
it's fine so that's how
that's how you can quickly extract
procedure Without Really copy code
moving it and be careful uh to not
trying to break anything
okay so that was the demo
next slide
here and the next one
so you started extract procedure and you
have a lot of them
but there may be a problem
if you do it manually there is a problem
there is something if you've browse the
internet you might think something some
articles about High room slow and what
it is and just it he he wrote that with
a sufficient number of users of an API
it doesn't matter what you promise in
the contract all observable behaviors
behaviors of your system will be
depended on by somebody and that's the
here's the URL where you can find it and
also he want if somebody is quoting it
he wanted also to put that that picture
yeah changes to version 10 17. the CPU
no longer overheats when you hold down
spice bar and they issue somebody with
logged in the update broke my workflow
my control key is hard to reach so I
hold space but instead I configure a Max
to interpret that a rapid temperature
rise as control
well not what happens here whatever you
I mean this logo is a deeper than making
something public and then not being able
to refactor code because somebody
somebody depends on that but that shows
that you should be careful yeah but just
not make publics too much stuff public
so when you are refactoring make those
methods local if you
if you want to create event Publishers
also be careful yeah that's what I have
on next slide yeah so use local
procedures
um maybe think about facade patterns to
hide your implementation
to be able to easily modify it later and
to avoid situation no you cannot change
it because we have a lot of references
to that maybe you should consider using
interfaces uh
um you can use interface wizard from my
extension or there is a code action
create interface there so you can kind
of have a code you need with public
methods you can use it and you create
the interface which you can use later
instead of that and
when you are designing your event
publishers
be careful yeah don't create too many of
them or you can create as many as you
want but maybe think
if it's better to create event publisher
that uh
the idea of Publishers comes from the
process not from implementation don't
don't create
event Publishers for every procedure
because you want those procedures to be
extendable
well it's
because you have pop you have private
procedure you don't want anybody to see
it and you are and then you are creating
different Publishers like on beginner at
the end from this local one and yes now
it's kind of public maybe nobody can
call it directly but there is publisher
that tells everybody there is such a
procedure and if you have a new
requirement from the customer you want
to change your code
that procedure no longer makes any sense
but somebody subscribed to it and then
you have a problem
so be careful with
[Music]
that
and one more interesting thing about
power of this conference
I said consider using interface and
mention interface Wizard and create
interface when I was sitting yesterday
in this room when David was showing the
create interface
he showed a create interface called
actions and I look at it and
didn't know about that
so yeah I learned something that I
created
okay
so yeah
actual demo
so let me switch quickly to vs code
I still have the same
um
the same code that I showed we just
before and now I said okay let's make
interface quickly that will Implement
public methods from this code you need
or not that will have public methods
from this code you need
so then I will then ever will use the
interface to hide completely the
implementation to separate it so the
option that I learned yesterday from
David is that I can use my own
actions from here and there is a great
interface and it will create an
interface that's what she was showing
yesterday but there's also another
option I can just right click somewhere
here I can use new Wizard and I can
choose interface
um
and
I will
select the
phase line update code unit that I
created just few minutes ago
and I can press finish and yeah I have
the interface with just that single
public method the rest is not visible so
that's how you can extract if you have
an idea that that single accounting is
great with those functions but you would
like to create another one from
something completely different uh so
let's create the interface and then we
Implement completely different versions
of our logic in another code you need
Implement exactly the same functions so
that's how you can quickly
quickly get to get those code those
interfaces created
okay
back to the demo
next thing avoid duplication yeah to
avoid duplicated code the
most duplicated code to a single
procedure create the procedure that you
call because procedure is something that
we should be calling but I saw people
that were treating procedures as a place
as a big bin from which you take a code
and put it somewhere else
so some people were working this way so
procedure single procedure with the same
code you call it from different places
so then you will have one place with box
not 20 and we'll be fixing it then we'll
be fixing the pack everywhere for
everybody for every code calling this
procedure not just in a single place
yeah so if you have procedures that are
related obviously group them in the code
you need
um
and what about this duplication because
if you open big projects you look at the
code and you don't know how many
duplicated procedures you have so can we
do something about it can we can we find
it I mean yes you can so again
some time ago I'll create this find
duplicate Al code command in my
extension because I was curious how much
that kind of code we have in our some of
our projects so this procedure this this
command cite just for exactly the same
code not similar one because if I start
searching for something similar it will
be slow but searching for something
that's exactly comment common statement
to statement the same is something that
we can do really quickly in a really
efficient way
unfortunately Al is that kind of
language that sometimes we have
duplicated code because variable type is
different but maybe the name is the same
so sometimes you want to do the same on
parties and say size so then the code
can look very similar and that's
something that unfortunately we cannot
avoid but
but if somebody but you can detect with
with this command if somebody just copy
the functions from another code you need
in this code or if somebody copied 20
lines of code and now we have it into
places
so a demo
quick demo about duplicated code
um
let's switch
The View and open
open the code that has duplicates
so I have extension I had a bit of
duplicated duplicated code here in a few
in a few places
now how I can detect that I can run a
comment so again let's go to the
commands palette and
it will be
um
find duplicated Al code let's run it
it asks it just asks just one question
how many the same statement you want to
find that's the minimum number that you
want to analyze that default is free but
you may want to start for for example 10
yeah because
the problem is that you will find a lot
of set filters or set ranges in many
places yeah set range on if everywhere
in your system you will have size header
dot reset size header that set range are
built to customer number or sell to
customer number so
um
so maybe you don't want to find it maybe
maybe you want to skip that so let's but
let's go with free so run it and I have
it not a very not very big solution so
it's it's very quick but it should also
be quickly with the with the bigger
bigger project so I have I have two
two duplicates
one is the whole method
and the second one is just a bit of code
um yeah so first one has the same
methods with seven statements inside
second have some state that six
statements being exactly the same let's
take a look at it I can click on the
first one and it will
it will open the file and select the
same code so you see it's it's the whole
procedure
and if I click on the second one is I'm
going to another code you need I have
exactly the same procedure so now I can
start asking the questions why
this procedure has been copied to
multiple places maybe if it was in some
specialized code unit maybe you need to
create another one and just move that
procedure to that one and use it in both
places yeah
[Music]
and the second case it's just a bit of
code and yeah it shows
a bit of
maybe not a problem but this is this is
by Design and that was my my decision to
make it fast it's actually if you take a
look at this code
actually the same code you could say
that it's almost the same procedure yeah
this code below is also the same the
difference is this line here but here I
have just two statements not three so it
has not been found and
yeah if I implemented something that
finds similar code then result should be
probably
hold this piece of code but it will be
slow yeah
it should say you know this whole piece
of code is something like 99 the same
maybe you should take a look at it but
just because of efficiency I decided for
something simple it still should should
give you some result it still should
allow you to to find those places when
people were
preferring to use copy and paste instead
of calling calling the code or making it
more generic
Okay so uh
that's the demo about finding duplicates
let's go back to the
to the slides
the next one next subject that I have
here is
a variable about variable names so again
first line here it's obvious variables
names should reveal the intention
when you are looking at the code you
should be able to from the variable nine
understand why somebody somebody is
using it it's not always the case I saw
a database a customer database where
uh the developer was using proper names
of the tables but then was using ID of
tables in the variable names so it was
variable t21 and so on that that was
completely unreadable yeah so it should
really tell you what uh the variable
name should really tell you what it is
and why do you do you want it but there
is also another thing you should avoid
name instead names that look similar if
you like to create very long names but
there is no one letter difference
between them then it's very easy to
start using the wrong one especially for
example if you use
if you like to use that Hungarian
notation and you will have pieces header
as a parameter and inside the function
you will have L says header as a local
one then it's very easy to start you
know
using using one of those and then send
the only one suddenly have one line that
is using another one just make that
difference bigger
and again you have F2 key that you can
use to rename the variable if you think
that there is there is a better better
name
[Music]
also we have code cop from Microsoft
that can detect problems that suggests
that you should use different naming
that the name should follow the uh
the variable names it probably can be a
problem if you have very long tables it
can be annoying that you have to type
all those uh
um all those long variable names and you
may not remember the names yeah and Al
is not very good language in this area
because you first type the valuable name
and then you will have suggestion of the
type in languages like cfap for example
you first type in data type so you can
have intellisense and then based on the
data type that you've selected it can
suggest you the name of the variable
well here you have to properly type it
without any mistake because that's the
first thing that you're doing so that's
unfortunately problem with with the
language but it's not the only one the
same is with SQL you're writing SQL
query and then first you have to select
fields and then use typing from which
table if you want to run create a query
that gets something from BC tables
that's hard here we have very long names
with spaces and very long table names of
spaces
so the question is is there anything
that can help us in in this area just
anything
and yes there is uh so there are a few
uh
um
there are a few extensions that can help
you there is uh add variable code
actions in Al Navigator uh there is very
nice snippet in Al variable helper
and also there is something that I have
in my extension but it's not public yet
when I Was preparing to this
presentations I was playing with
something thinking how we can make our
eye life easier when we need to uh
type the variable name and we would like
to follow Microsoft rules
so
that's that's something that I will
I will release after the conference
because I don't want to break anybody's
presentation
and when I'm ready after after the last
session or maybe tomorrow morning I
would release that new version of the
extension with the last thing that I
have here on this slide
um but let's go for a demo and take a
look at it
so creating variables
let's see what we can
what we can do how we can
um
[Music]
how we can use all those
those extensions so yeah there is
another project in vs code just let's
wait a moment until the io language
extension starts then we try to do
something with those variables
um
okay so I have
a cold unit of some functions so first
first thing first case or first
extension that we can use we can use AO
Navigator so how does it work it
it expects you that you just start
typing your call in your code you will
start using variable names so I can
stand I have a function called process
sales order so probably I would like to
do something with size headers so I can
start typing
and probably I said that would be the
first thing that I want to do now I
don't have a variable I have an error
here but I can click on it
and in this bulb I have a few code
actions coming from IL Navigator I can
add a local variable Global or a
parameter and let's go for local
and what will happen
uh
it needs to start is it working or is it
not working let me save the file
and try again maybe I click run
correctly ah the local variable
and
probably still
come on
do I need to save something what about
global
yeah Global World so I have a global
variable here uh
so what has happened uh the function uh
like the command
analyze the name of the variable and was
able to find a
was able to find the table the the
object that has this name
and then based on that it suggests that
okay that should be probably that that's
what you probably mean and created
created the record variable so that's
one of the options that that you can use
um
there is another one there is a
a snippet it was the record
and that's the AL variable helper so if
I select this one first first it creates
a snippet and goes first stops at the
place where I'm selecting the data type
so I can
type says and then I have in collisions
so I can select it
then I can just remove temporary and
then I can go it goes to when I press
stop it goes to the to the beginning and
then when I press Ctrl space I can free
options I can use full name short name
or just tag and tag with just first
letters from from the data type but
let's go for full and I have says header
so that's something that also help you
first selecting from the list then then
it would suggest suggest variable type
but now let's just also take a look at
those experiments that are doing during
the weekends trying to find a way if we
can make it make it even
easier so
I have a setting
um
L outline completion providers
those are the you can select a few
providers that will
that would suggest you code in a few
situations uh it's not ready yet so I
can select
and currently if I press Ctrl space I
have three available I can
have some completions for the variable
data type or for variable names the last
one are exactly the same with just a bit
different Behavior so we can only select
one of those and I can choose let's go
for data types because that's something
separate and there is variable names
with data type so I will select those
ones because I'm not sure which one is
better and maybe you don't want them at
all that's why it's in the setting and
by default it will be off or maybe maybe
you know maybe if I have a positive
feedback maybe I will some of those
default so yeah so currently data types
and variable name move type and let's go
here
and now
I can select far and I can start typing
sales and I have sales header with data
type yeah
because it tries to it suggests all
possible variable names for based on all
all available object types and that's
what I can select so if I'm only if I
only want to have one single size header
variable in this function that probably
does the best name because Microsoft
code analyzer will expect exactly the
same name so I can just press enter and
I have it yeah it's ready I can also
thank you
I can start typing
time says header and I have temporary
record less typing
yeah so
I said it'll be available in a few days
but also but I cannot suggest everything
so I can type like
says header sorry
face header buffer and now I don't have
employee sense and now there is this
second provided I selected the data type
provider so I can start typing
record
and I have one here again size header so
I can press enter and again I have it
yeah so so that's one that's that's
those are the options and the thing that
I'm not sure which is the better the
best one is here
so there is another option just variable
name
which changes a bit the behavior so now
uh
I still have size header but I don't
have the data type so I can select this
one
but I still can use the second one
so still the same result but
it's up to you which one you prefer if
you want just to suggest variable names
and then do the rest yourself because
there may be a case for this one
I guess Alexa press enter and that
buffer and so if you want to have some
more complex names that that have inside
that starts with the object name then
this option probably will be better for
you
and now
I can still go for records I said that
and I have the variable
so yeah so that's what I was trying to
do to make
make our life
easier
okay go back to the demo
comments
another subject I have two quotes from
uh Kevin Henny
from his
presentation about seven in affecting
coding habits of money programmers and
from his Twitter the first one is with
he said on this on this on this YouTube
on this video my experience yeah that's
what he said he said suggest that other
human beings don't read comments and
compiler don't read comments so
so who are you writing them for that's
what he said yeah that nobody reads
comments compiler definitely not doesn't
care what is there and other developers
first go to code trying to understand
what is going what is going on inside
and later they are if that everything
fails then look at the comment maybe it
will suggest what it is doing but
comment may be a bit old from you know
free comics before
and also the second tweet from a tweet
from him was a common fallacy is to
assume authors of incomprehensible code
will somehow be able to express
themselves lucidly and clearly in
comments and so we're expecting that
people that can that write completely
unreadable code very messy and with very
Twisted Logic the explanation will be
different but probably will be the same
it will be just in English another
language it won't help
uh so yeah so the question is it looks
like developers don't like comments and
if you watch read about it everybody no
no comments are bad well they're not
it's just we should use them properly uh
but but watch this video there is very
interesting thing about that fits into
this session uh into the subject of this
session uh
but I don't want to start a new war here
because he said which identity style is
a wrong one
and his selection fits into it and it
has something to do with F2 key when you
want to rename procedure very
interesting
I don't want to do it here because
that's one of the subjects that could
trigger very violent discussion the same
like begin and around single statement
let's not go there
okay so the comments
Well everybody's saying cult should
explain itself you don't need a comment
still need the comments if it adds a
value
and also too much comments are the noise
and it's very hard to read code we have
a lot of noise and that's where we
coming to the one of the first slide
that I said you should be using Source
control because your code is not the
place for putting your for example Jiva
task numbers that should go into the
commit and in a code you should talk
about the code about functionality not
about the time when that change happened
but rather
what this code is doing you should find
it in your task management software and
maybe in a comment and you should not
leave comment in that code that's not
what commandants are for don't keep the
metadata or old code inside your current
code your Source control and also it's
common should add a value
this one
not really yeah
find item price final and then price
yeah
I mean I know that I'm probably not
sounding very convincing if you think
about the functionality of adding
tooltips to pages in my extension
because they are doing the same sorry
for that but yeah teach the comments
should add some some value
so what
could we do what how we can use comments
one thing that comments can be helpful
we have XML documentation now in Al you
type free slashes and it generates XML
that you can populate with some
explanation of your function and then
you can generate using Al XML
documentation extension you can generate
MD documentation from it that you can
give to somebody
or when you are typing using that
functions you can see in the suggestion
intellisense you can see those
explanation
but be careful yeah
this this extension can can generate
this documentation but the first thing
I'm doing I'm turning it off because it
shows complete complaints that every
function in my solution should have XML
documentation
but on a previous slide I said that
comments to that value
so
if the explanation documentation for the
function is obvious doesn't make any
sense then you don't need XML comments
[Music]
and I have to say that I made this this
mistake in the past and the XML comments
has been introduced to c-sharp in 2005.
when I saw it first time now I will show
you how to write documentation and I
made every mistake possible I was never
updating them because they are not
updated so if I add that parameter to
function well back some of the comments
that I made was staying old
never did that because you know it's
easy to generate it but it's very hard
to modify it yeah there's really no
suggestion it's no generous one you have
to retype everything at that node
manually very bad one
I never generate any documentation never
and nobody asked for it so
if you're on isv if you think that it
will help other partners to understand
your code if you want to have nice
documentation to get generated or you
think that other partners extending Your
solution will benefit from this thing
that's a good idea to go but if nobody
will be reading it don't build this huge
decorators of your code that are in the
different color when you're scrolling
through it just because you like the
different you know seven lines of
different cult above every of your
procedures
not going to help anybody it would just
make harder to read and a bigger code
so those are XML comments second thing
are to do comments there is extension
two to three and this extension can find
all to do comments
and you can see them
somewhere on the panel which is a very
good one
but you know if you have to do that
stays in your code longer than probably
a week or two or maybe a month maybe we
should this up it should disappear from
the code and go as a task that you have
to do in your system okay to do probably
should be something that I need to fix
that code quickly before I create pull
requests before I push the solution back
if it's something for longer then
it's better to keep all things that we
need to do in a single place and
probably some have some project
management solution where it should go
yeah and I had a chat with with Stefan
modeling maybe we need a code analyzer
that will detect to those which will be
disabled by default because messages
from code analyzers are very unstable
but if you have a pipeline you can
enable it and if somebody is creating
pull requests it can go through it and
see huh there's a there's a to-do that
probably should not go to this to the
main branch because you haven't finished
your work and if you want to keep that
to do because that's something for later
move it to maybe to to the to the
product management stuff and our code
will be without and introduce that's
something that maybe we'll do in phase
two of this project
and the last thing that I have here is
mandatory comment next to comment that's
what Stefan has in this his least
lintercope
it can it will show me a warning that
you have a comment inside the code but
there's no comment why
which is a good idea our our guys from
the performance team love that they said
okay if you want to put a comment maybe
first think about it and explain it
maybe when you will be thinking about it
we'll listen no I don't need it
uh that can help so that's the first
third thing that
good example where you really can use
commit and they can very very very
useful
so short demo about
uh
about comments let me quickly
uh
open my comments and go here
don't save this project and
I have a bit of code so quickly
I have one
one to do comment here
um
let me just close this file
and here I have 2-3
and I can see this to do here so you
have a lot of to-do's a lot of tasks
still to do
you can find them here and as I said I
was playing with cold analyzer that was
showing the to-do's other warnings but
it was a very unstable list and it was
hiding some more important warnings
because there is a limit of those walls
I can have so code analyzer in this
situation will be very bad but this
extension is a great thing as
something that can quickly tell us on
the technical level you still yeah we
are putting some notes this code is not
the best one I need refactor because
before I finish so that's how I would
use those those to Do's so that's that's
the first thing yeah this one
second one
I have a comment here I already have a
comment but let me delete that
and save that I have the linter cup
running so now I have a boarding here
Comet needs a comment to justify the
existent either uh leading or a trailing
comment so you have to put comments here
um
and it should be proper explanation so
it's not the right one
that's not how you make it silent
but I just wanted to show you that you
can make it silent by adding a comment
don't do it this way yeah not I need it
it's why I need it
uh and the last quick thing is those XML
comments
so
I can press free slashes and press enter
and it creates it
as as you can see it's a summary when I
can type the description of the function
and I have the parameter I said the
problem with it is that if I add a
second parameter it won't be added here
automatically so you usually I will do
it later and it later is never
that's why that's what I was doing and
so I stopped using those comments
because it wasn't working like I said
yeah but
let's do a bad example so
that's a part example and also
that's not adding value but I can show
you the example how does it work let's
just save it and now if I go here and I
start typing
processes
face orders
and it's not showing it
yeah but if I hover over it in the
uh here I have this protest size ordered
comment here and uh
and over the first parameter
it should
come on
it should start showing me
but it should
it happens so that's that's how you can
create those those
comment that can help help other
developers and what they can do I can
also uh
enable the uh
um when I have it acceptable
documentation I can enable it
and now I should have uh
command will be
next
I have aldoc export documentation I can
expose PDF or I can export as MD file I
can I can select it and it will it will
run and it will
it will it will create the uh the the
dock folder
um
so export documentation it runs and it
created documentation folder and if I
preview
I have some
have a documentation for for those code
units and
it also took the descriptions.i
I put indexable comments here so it
combines the
uh the comments together with with the
object description
okay so that's how we can use it but as
I said it makes sense if if you're going
to add a value if if you're just going
to be uh
if your idea is just to
have a comment separator doesn't make
doesn't make any sense
okay
um
so yeah a few
last things before we
finish a bit about formatting so
when we are writing code we are writing
not only code that we run but something
that other people will be reading and
our brain works in a way that
one part reads the text and another
tries to graphically understand the
structure
fortunately in il we have automatic
indentation automatic formatting but so
that's no longer the problem but still
you can have a lot of noise yeah a lot
of
too much comments and a lot of empty
spaces maybe wrong casing of the names
so so it would be good also to to make
sure that it's
it's a bit nicer you know it's easier to
read we don't have this situation where
half of our brains
have that reads the text thinks that it
works this way and that part of our
brain that analyzed the overview of it
from a big distance things that
something completely different because
then you have to focus to really
understand what's happening if those
both things are suggesting the same it's
much easier might result much easier to
read it
so what we can do uh one of the things
is that you can
you can solve the variables maybe you
want to solve procedures I don't I don't
think that's a good idea
but you can if you prefer you can sort
properties that's probably fine with
procedure I will be careful because I
prefer to have to go down we have
the most generic procedure at the top
and the procedures that that one calls
at the bottom yes so you cannot sort
them by name it's rather I can start
reading from the top the the code you
need and then I can stop at some level
because I don't have to go deeper uh
uh so I think it really helps you uh you
can think about religions but the
regions is something some people
complain about regions that it helps
create God objects because you are
hiding complexity you just can fold
everything and yes you have code in it
that has 500 screens but all of them are
folded
and group together maybe if you're doing
that maybe we should have code unit but
each of those regions uh
so Microsoft code cop can detect sorting
issues with with variables so it is
it has a rule that can go and and then
you know would be you should be sorted
by data type if you like it that's fine
if you don't like it turn it off it's up
to you and I have a few comments and
unsafe actions that can for example sort
variables when you're saving your file
so you don't have to care about it you
don't have to run anything you may get
the default settings for everybody in
the project then when they are saving it
the result is exactly the same that's
why I said earlier that put the settings
together keep them together with project
so everybody when they are saving the
result is the same not that different
people are saving the same file and it's
constantly completely different because
they are sorting differently
and I have a few commands that you can
run also that will remove empty lines or
remove empty triggers or empty
subscribers and also there is a comment
that can help fix the the case of
of the um
casing of of the of the command so of of
the statement so let's just quickly
quickly go to the demo
[Music]
and open a folder
just go to formatting quickly
and quick formatting examples
so
quick example I can have
you know a lot of spaces for example
yeah
sometimes people are putting a lot of
that stuff and then you're seeing it and
it's hard to eat it's hard to see what's
what's there so
um
so what's what I can do I can run a
command
oh sorry not the overview I can learn a
comment
empty lines yeah
just from the current editor and it's a
bit better
I can also if I have a trigger like here
or if I have subscribers but without any
code
I can also run another command
remove empty empty triggers and it also
removes empty empty subscribers from
from the active editor
um sorry I need to save it
and let's run it again
and
of amp the triggers from the active
editor and it asks me if I want to
remove triggers if I want to remove
subscribers and if I want to ignore
comments inside because sometimes you
may have something that is completely
empty but there is a comment inside but
there was post that there was a case
where
system BC was behaving differently if
you had empty subscriber and if you had
no subscribers I don't remember the case
so just David filter mentioned to me so
that shouldn't be here
so that's
that's what that's what you can do so
let's let's just just
to remove it
empty triggers from the
uh
and let's run it it's gone yeah so we
don't
uh
we don't have a trigger is gone
and the last thing for this subject is a
bad looking code you need to answer but
casing
with this size header uppercase
so I can I can run a comment and I can
fix
identifiers and keyword case in this
editor I can run it and
it runs and now I don't longer have
uppercase I have proper size header and
here are the names it clears it
so that's
that's the uh
that's the formatting there also if you
want to use something unsafe you can go
to the uh
to the settings and
and in the site there is a command L
called actions on Save and you can for
example have sort Properties or sort
variables and each time you save it it
will reorder your your variables
or all the properties in in this case
okay
so
let's go quickly here
and one of the last things here
something about code analyzers last few
minutes
all right so we have a colonizers from
Microsoft we have the community
colonizers from Stefan with a central
intercope that's the vs code extensions
that install another colonizer
if you want to create your own because
maybe you have some special rules in the
company you can take a look at my blog
there is an example how to end and post
how to do it yeah the old one but still
valid uh and don't enable code analyzers
if you don't want to fix the warnings
because you will just populate your
problems tap in vs code with a lot of
things and then something that is
important you may not notice that and
then you will leave leave some bugs
inside the code
and if you don't want if you want to
know what type of rules you have you can
use a command from my extension show to
analyze the rules that will display you
every available rule maybe you want to
maybe you maybe you know maybe you have
a discussion inside the company which
rules we want to disable so you can go
there create a list and then talk and
decide okay this one will go
uh
and also how we can disable
some warnings
there are a few ways
the worst one in my opinion is suppress
warnings in app Json and in my opinion
is wrong one because
there is suppress warning reasons
property where you specify comma
separated list of codes of those
exceptions but there is no place to
explain why
and because I'm talking today about
readability that's not readable yeah you
open it and you're thinking why they did
that yeah what was the reason I have no
idea so that's probably not the place
yeah
so there are also advised which are
better
because there is justification property
and you can expect you know disable this
rule so no now now I know why and now we
can have a discussion I can take a look
at it I don't think that okay you put
you explain why but I don't think that
that's enough yeah maybe maybe I don't
agree on maybe yeah that's fine uh and
you can use pragma warning disable or
restore uh
if
uh if you want to have just one
exception in a single file you may want
to follow the rule but sometimes there
are special cases so we can do it this
way uh there is a code action from L
toolbox done you know you have a
warnings you can then use surround with
pragma and it will add disable and
enable around the warning quickly you
don't have to type it yourself
and I was also trying to do some
improvements again last weekend when I
was thinking because the problem is you
see pragma you see the code
and you don't know what it is so again
you see they disable something but this
is aa00 or something what is that so I
just added the hover functionality uh to
be able to see the code and description
of the rule and also find all references
on the rule ID because you might be
interested okay what are other places
where they disable this rule
and the last thing avoid overriding
safeties if you're developing for SAS
and you know that functionality will be
disabled in six months you don't want to
use it so and in rule sets you can
disable compiler warnings and that is a
compiler warning that this functionality
is marked for removal maybe that's the
moment when you should know about it and
talk with your project manager or
Consultants you know you're suggesting
functionality will be gone in a half
half a year we should not go this way uh
so be careful with that one I mean if
there is explanation that there is a
valid business reason fine but it should
be in the rule set it's not we disable
it because that's too much to work that
doesn't explain why and it's very
dangerous
show demo
we still have 9 minutes and 30 seconds
social demo and then I will ask for
questions so
quick demo
um
cold analyzers
um
I don't want to save it
I'm here so quickly we have linter cup
it's installed I have it installed here
the nice thing about it let's wait until
it activates uh
so
there is a button from the winter cup
which allows the quickly to turn on and
off analyzer so all standard ones and
business Central intercope is also here
it adds itself automatically
if you if you tick this box and it's in
the settings
and it shows some some warnings so
so what we can we can do I have a I have
a wardening that uh
um
variable size header is used in on
increased prices
function and I have a bulb here coming
from IL toolbox
and I can select
sell out this error this warning with
pragma I can click it
and you see it's surrounded so it should
disappear but there is another problem
so it has a few more yeah
so now but this rule is gone yeah this
aa137 is gone it still complains about
uh about something else doesn't matter
uh
what I can do I can hover and now I know
what it is do not declare variables that
are unused yeah so without it I don't
know what is happening here
um
yeah that will be all there
[Music]
so yeah so another another wording uh so
yeah so so that's that that's the thing
that the pragma that can also right
click here and and just go to final
references and I can see where it's in
every file when this single rule is an
Amazon organized if people are not using
disabling this rule too much too
frequently in the solution uh
and uh and what what else you can do I
just want to show you that we have
obviously app Json and we have
suppressed warning so I can do the
lc00150
here
and obviously I have no idea
what it is yeah and I have no idea why
so I added also I was trying to do some
experiments and I added hover during the
weekend here so at least I can see what
they disabled
and and the last thing where you can do
it is the rule set so
which is
there is a snippet
yeah and
I have the
I can have a rule so I can do again
ai0021
if I don't have justification again when
I was doing experiments during the
weekend
which will be released soon I also added
the hover here I just need to save it is
it working
not really let's look listening
don't let that select any other one
and no no
okay
doesn't like me but it should be old I
will be hover also here so you can
um
you can you can you can do it this way
okay you can check what is there and
check the justification uh
so yeah so that's the uh
[Music]
those are the
the colonizers that's what you can do
with it uh
last thing one third is last 30 seconds
uh
there are some commands that you can use
to clean your extension some of them I
was showing like removing empty lines
sorting all the Sorting procedures
sorting variables there is also called
cleanup command that you can use when
you can specify in the settings which
which comments you would like to run to
clean the code
and you can run it at the end of
development
and that's it
I'm not going to do it here is a list of
extensions that I was showing
and the last five minute questions
okay
and a shirt
okay the first
yeah
so you showed the function to find
duplicates yeah you have a parameter
that finds by lines
uh do have this that so it finds
duplicates for the code unit or fines
and duplicates for exact function or it
only runs just a function and JavaScript
piece of code it's not it's not
searching for the whole code unit just
on a function level it's not going
higher
okay but but does it search for the
function that you defined or is it
searching for the whole project and it
finds every duplicate that there is it
starts everywhere for whole project okay
okay thanks
any other okay
let me check this one
yeah this is actually no question I
think the reason why the local variable
creation failed was that you didn't have
the VAR section in the procedure
but
shirt and then
so you had you had to proceed your uh
but you didn't have the borrow section
up below it
so it so the wizard didn't find the bar
so it couldn't add the variable to the
procedure in the duplicate no no no the
creation of the local variable yeah
yeah I probably that was that was
probably the case okay
another one you showed a lot of tools
for visual studio for Al uh do you know
um if there is something the same but
for cl extensions for visual studio but
for sale
uh not really I was doing some
experiments with Cil in the past for
for all
for a bit newer Dynamic snuff the one
that has a visual studio editor when
Microsoft took it they took they took
also part of Visual Studio editor
extensibility so there is a possibility
to extend into the code level you can
get access for example to the local or
Global variables
but there's nothing like it I mean you
can you can go to my GitHub there is an
example small dll that you can project
compile dll you put it into into the
folder inside the RTC client and it adds
a it adds in Snippets to intellisense a
few things but if you want something you
can take that source code and develop
something yourself but it's only for
code it's only sits there nothing else
you cannot integrate with the with any
other functionality of classic Dev
environment okay okay yeah thank you
you can develop something yourself if
you want anybody
is there a reason why you are disabling
the Mal 72
um that variable names should be
suffixed with types
because um your extension is
um when you show the example the sales
header is called sales header not sales
header rack
and
it's fine for me I prefer the full-size
header I'm not putting Greg it's just
just a name but it's a code cop rule I
think that he was not checking 72 what
yeah
it's still information yeah so okay
thank you
anybody else
nope
okay thank you yeah
oh one more question
[Applause]
it's probably went too far
you know there are lights that you it's
just straight into our faces so it's
hard to so while we're talking about
Cold clean
um you know since I'm wondering what do
you think about passing a record to a
procedure when you need only a couple of
fields because in Microsoft code there
sometimes they pass only the fields they
need sometimes the records and when is
it
better one or the other do you have any
opinioners I don't have opinion here
it's it's up to you what you prefer and
see if you pass the record the list of
each shorter is one of this of the
patterns that that the record you should
you should create a record and put some
uh with multiple fields that you will
pass together but if you prefer to Fast
Five parameters
fine yeah I mean if you want to plus 20
I probably will look very bad so I would
put some limit and start thinking what
to do if I have more in other languages
yeah we can create a class hide
everything inside but here you can only
use record which you are limited to the
size of the field in the record so
sometimes I don't want to use record
because I have longer strings uh but it
it's up to you yeah I would okay yeah
but that's the pattern so
suggested to use to use record
somewhere in il I think that it's still
in the LL guidelines but we'll have to
check thank you
okay
so yeah nobody else no
they care about
[Music]
foreign
[Music]
