# BC TechDays 2022 - Customizing the developer experience

- **Source:** https://www.youtube.com/watch?v=DGup5JV3EtY
- **Video ID:** DGup5JV3EtY
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 45m54s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

ladies and Gentlemen please welcome
kelman and Nikolai
[Music]
good afternoon everyone welcome to this
session about customizing the developer
experience yeah I'm Carmen he's Nikolai
we are from the team who is bringing you
the
AI development environment
so our agenda for today we are going to
talk wait we don't see this or we see
the screen yeah
we're going to talk today about some of
the non-obvious AR settings
that are there but probably nobody knows
that they are there then we are going to
have a brief introduction into
workspaces
and project to project reference
resolution then we are going to talk
about dependency publishing and I'm
going to touch briefly at the end on red
rapid application development that said
I give the word to Nikolai
so hello everyone welcome I hope you had
a nice session so far and this one will
be good also so let's start so L
settings
okay I believe most of the people here
should be our developers and as air
Developers
you have three vital configuration files
while you're developing your extensions
you have your app.json file where you
specify the identity of your app
dependencies version publisher and more
some other configurations also you have
your launch.json where you specify the
configurations to connect to your
business Central server
uh and then you have
one of the today's topics AO settings
so let's take a look at Neo settings how
you can configure them where you can
modify your settings
so first up uh so code
user or Global AO settings
uh these you can find when you open the
settings you know graphical interface in
videos to the code you can either find
the extension the AO extension and
modify them using the graphical
interface or you can actually open the
the settings by pressing Ctrl and comma
and then pressing on that
small button on the top right corner
there you find the Json editor for your
settings and you can add AO settings
over there AO settings they start with
the prefix AO Dot
okay where else
you have your workspace settings
so that's actually your workspace file
where you add all of your folders
different projects
single projects and then you can specify
settings which will override the global
ones
and they will be taken into account for
the current workspace
other than that if you don't have a
workspace
but you still want to override the
global ones you can open a folder or
so-called a single project and you can
still override the settings there you
can specify different settings up here
and have in mind that that settings or
Json file does usually doesn't come by
default you have to create it yourself
manually and it needs to be placed under
the dot vs code folder where your
launch.json and the right.json is which
come when we talk about
okay so we looked where we can set our
air settings
and let's take a look at some of the AO
settings that can boost your performance
can make your life as a Neo developer
easier
okay here is a table I'm not gonna
basically read what is written over
there but I'll talk briefly about them
the first one which is incremental build
I need to give you a little bit of a
back story about it so when you open a
document and you start typing your AO uh
what we do is on every keystroke we
perform these so-called background
completions
so why are they needed so they're needed
because every time when you type
something we check if what you have
typed is correct and we provide you the
necessary and the accurate Diagnostics
so you can see diagnostic messages down
in the in the bottom of your Visual
Studio code current project so that's
why we have the background completion so
what happens if you specify incremental
build so incremental build comes by
default with true you can set it to
false
and when you press Ctrl shift and B we
are not going to use these background
compilation so that's actually I already
pre-compiled uh state which we by
default use to speed up your Full
Compilation of your project
if you set it to false you'll get
Behavior similar to using our Powershell
client and I believe many of you you do
that in your Pipelines okay we have the
second one editor service log level
uh this is something we recommend or we
actually ask for a lot in our GitHub
when you have issue and we need a little
bit more verbose logging we ask you to
go and modify that file you need to
remember though after you set you know
the state to to more verbose because
that's an inum option you need to get it
back to normal because as common likes
to say AO is very chatty language and
that file size can grow exponentially
the last two browser and Incognito
straightforward they complement your
launch.json when you actually
for example open a debugger or you
publish your Dev extension to your
server you can specify in which browser
you want that one to be open and if you
want to be open in an incognito session
have in mind that Incognito won't work
if the browser hasn't been changed if
you're using the system default which is
the default one coming then Incognito is
not going to be taken into account
next one
we have compilation options
so these are specific options which will
increase or boost your performance when
you're trying to build compile your
extensions
we have generate report layout
straightforward do you want the one to
be generated or you don't want to
we have the next two which are related
to the compilation if you want to use
parallel compilation so you can decide
if you really want to use or you don't
want to on our servers we go with
parallel so we have better performance
you can also specify the max number of
parallel
processes that can be executed and we
advise you to use the number of virtual
cores you have on your machine
these options parallel and marks degree
of parallelism they come by default
from.net so if you want to blame us
about something just go and blaine.net
I want to demo these two
so I'll switch here
and I want to show you what kind okay
you see good
what difference it will make so I'll
open our base app that's do you see
should i z Zoom a little bit
let me Zoom a little bit
okay good
not good you don't see it different oh
no you do okay so that's our Benchmark
for a big project it has probably over 7
000 uh application objects and I want to
show you the difference between the
parallel compilation and non-parallel
compilation so there are few uh options
I want to highlight here so the
incremental build set to false we want
to start a compilation from scratch and
then the completion options are parallel
also set to force so I've already
pre-built that one because if you take
time we don't have that much time in the
session today
and you want to see we want to to take a
look at when the compilation has started
it has started at what is that almost
quarter past two
so that's late 13 minute and it has
finished at 18 past two so that's what
15 minutes approx five minutes
approximately to compile and then I'll
switch to another uh project open again
base app here incremental build of
course set to foes but compilation
options set to true and the number of
Max degree of parallelism is set to 16
that's the number of virtual cores I
have on that machine
so the compilation started at 23 minutes
fast almost 23 minutes past and it
finished at early 27 so you gain almost
a factor of two performance if you set
the
excuse me the the parallel to true
let's get back to the presentation
finish with the less the next two
oops
we move fast good
uh slideshow
current
and next one
good so delay after last
document change and delay after last
project change so that's always related
to the background compilation I talked
about so if you have a big project again
example with our beta and you don't want
to get these
um
you know the Diagnostics are often
because you know that when you modify a
big project that will trigger a
compilation it will take time it might
slow uh your development if you have you
know slower machine if you don't have
that that big of
Hardware resources it will take time it
will consume your memory you can specify
these two settings
according to your needs you can see the
default values up here
um have in mind that you know after last
project chain has to be always uh bigger
than after last document change and then
the last one continue build an error
that was introduced by a request uh by
you guys by the community in GitHub
it is related to how we actually compile
projects
whoever is familiar with with compilers
you know that we need to First parse the
file and then move to other stages and I
remember the exact request was uh that
you weren't getting all the errors so if
you open the project in in Visual Studio
code then we we are able to parse for
example on multiple stages and then
you'll get more Diagnostics but in your
pipelines you get less because what we
used to do is if we fail at parsing then
we don't continue
so that one if you specify that
parameter we will try to continue
building so we can give you as many
errors as possible but you have to also
bear in mind that if you specify that
one to true and that's also only a
Powershell
um flag if you specify that one to true
we cannot ensure you if the Diagnostics
will be accurate because after wrongly
parsed file we don't really know what
will happen
and having said that I'll pass to Carmen
and he'll talk to you about workspaces
yes so
what are workspaces so what is an Al
workspace because we are talking about
an AI workspace
so simply Define an AI workspace is just
a collection of one or more AR projects
and then so what is an ER project so an
AR project is a collection of files
mostly alphys Json files XML files that
produces a single output an alap file
and here project is defined by the
app.json file
a workspace you know can be Standalone
or it can be a multi-root workspace
and why why is this important so the
biggest Advantage as I see it of a
workspace is that it allows you to work
on multiple projects within one vs code
instance
but there are other advantages so let's
take the next
so in a workspace
you can Define projects and these
projects can be set
in a dependency relationship so what
does that mean so that means that
interdependencies entry in your abdog
Json you can specify
a project another project in this
workspace
and then this project will be a project
reference
if you work with Visual Studio
you have similar Notions so you know
workspace is sort of similar to a
solution and then you have projects in
visual studio and you have project
references so in Al these are very
similar con uh
terminologies
so there is no distinction between a
so-called project reference and an app
reference so the distinction is made by
Logic so if if a project exists in your
workspace with these these names then
they are project references if not they
are app references the important thing
with projects and project references is
that once we see a project reference
every resolution symbol resolution will
happen from the project we are not even
going to load the app even though it's
in your package cash path so we're going
to ignore it completely this is a new
thing uh since uh
I think yeah January this year or
February this year
so when you work in a workspace and you
have multiple projects there is always
one active project and why is this
important
and what is the active project so the
active project is basically the project
that's in in your view
so you know the for example if you have
an AR file open then your active project
is the project where this AR file has
been defined for or if the app.json then
it's that project then why is this
important it is important because all
operations or commands they happen in
the context of the active project
so the active project can be seen on the
bottom toolbar it's it's there
so you always know in which contacts you
are
now if you have a workspace with
multiple projects
loading them is a bit yeah as you
probably know and we got a few
complaints about
there are some rules okay so let me
explain these rules for you so let's
assume that I have a relationship like
this so I have a my leaf up that has a
project reference to a my system app and
then Miley fob also depends on my base
app and then there is also an external
app here which is not a project
reference
so
what happens if I load my days up
so what happens if I load my base up
that will first load my system app
then it will load my base app
and then
my leaf up will not get loaded that will
stay unloaded and it's marked with a
letter N is not loaded
so I was talking about
project to project references and
resolving symbols and I will repeat this
thing again because this is important if
you have a project reference that is the
resolver even though you have an app F5
for it you're not going to use that
so let's talk about building a little
bit building projects with project
references so you always build the
active project
yes but if the project references have
so-called red change or change you know
red change means that you change an
application object file
then we are going to uh
so-called Building forward topological
order which means that we are going to
build a project reference first and then
we are going to move backward but only
if those projects have been dirted
and I have here a hint for you so do
wield often on large projects but
because at the end of each control shift
we built we are going to do a GC collect
and that is supposed to you know release
your memory
so let's just look at all these things
that I've been talking about
this is not visible
my screen is not visible I don't know
why
thank you
I have to watch
that one yeah I know the other one
doesn't matter but you know I can go
okay
yeah I don't see my screen here but I
see mine but I don't see it reflected on
um
okay
can I get some technical help from the
technical FIFA
get this
try that one p and see what's green yeah
nothing
yep sorry
so
yeah where were we so we were at we
wanted to demo some of the workspace
things which you probably you know I
think how many of you are using
workspaces like okay
yeah good a lot so let's do these
scenario that I was talking about so you
know I have here these projects and they
are in this relationship so what you can
see here is a workspace in my life as my
base of my system app and then an
external app which is not in this
project yeah so I have only these three
and then let's reload the project but
let me reload like
you know let's start with my system at
what happens here if I reload this one
and I reload window
then the message box should appear that
the project is loading
so here down this is something new we
added like half a year or a year ago
and then what happened is that only my
system app was loaded my leaf up and my
base up hasn't been loaded I mean you
load my leaf up by just clicking any any
of the files then that will load so now
let's do this control Shield B that I
was talking about so again
in this scenario myleafar has a project
reference to my system app yes so if I
just build it Ctrl shift B
let me toggle the screen that you can
see which
Ctrl shift B
then
you know so I said that the project
reference should be but it hasn't been
built only my leaf app has built and why
is that the because I haven't dirted so
I haven't worked with my my system app
so if I just you know add some lines
here
yes the command Maybe
and then
if I rebuild my leaf app that should
build my system F2
yeah so you see if I do it in my system
then even though I build mylifab that
will build
forward topological order for my system
and my defend
Okay so
this was about
building and
let's see the next step you do in Visual
Studio code is publishing
and for that Nikola is going to talk
about dependency publishing
okay we move to dependency publishing
so we get to know how workspaces work
you have a workspace in Visual Studio
code
and that's actually a brand new feature
we got very positive feedback during the
workshops about it so let's see what
will happen just imagine a scenario
your AO developer you have fresh and
tidy workspace
sandbox note workspace sandbox
environment sorry and then you have your
workspace with number of projects uh
let's imagine a a complex dependency
graph I mean that's how I imagine a
complex dependency graph
I mean always it can get complicated
always but I needed to show something
right so let's imagine that dependency
graph
so you have all these projects and you
want to publish to a fresh
sandbox completely empty only our
standard apps are published over there
so what would you do so back in the days
what would you do is if you want to
publish an app yeah I need to
sorry for for showing my back but I need
to to point a little bit let's let's
pick up 11. if you want to publish P11
what you had to do back in the days is
in order to resolve the dependencies in
the server to go and publish first P2
and P3 I mean that order doesn't matter
Basics and p8 and you also have to be
aware of
the topological order of your
dependencies beforehand so you know how
to publish them
we hope that we may mitigated that for
you so what we will do from now on is
you just open one of the projects part
of your workspace
then we'll ask comments should build
that active project of yours with all
these dependencies and we introduced a
new option where you can publish all of
its dependencies and that project
included to your fresh sandbox
let me Demo it for you so I'll pick
project 13 and you can see its
dependencies on the right hand it is
right yeah on the right hand uh side of
the screen
so I jump to visual studio code
and fingers crossed that demo would work
because I literally cleaned my
environment two seconds before Carmen
finished his
we have the workspace here all the
projects in the same order as in the
previous picture I've opened P11 and you
can see P11 is our active project down
on the left corner
uh what I would do is I'll go Ctrl shift
and P I'm not going to show the the
toggle screen mode it's not necessary
and then I'll select publish full
dependency tree for active project
uh then I'll switch to Output just
ignore these errors that's for another
project we're not touching it and then
I'll go to Output yes so let's see what
happens in output
so first we say
okay somewhere in the top yes
first we compile locally in the
topological order all its dependencies
so that's where we we compile
then we say prepare to publish 11
projects and these are the 11 projects
we are going to publish
we have sorted them in topological order
so you can see which one will be
published first second third and so on
until the last one and then we start
publishing
so then we publish one by one
until we get to the end
and yeah the demo worked so we can see
done publishing project 11 of 11 and
that bad projects is B13
okay ah
actually you should be excited here I
hope you are
yes thank you
uh let me prove it for you if you go to
extension management page
I'm going to use some of these
extensions later so you'll see but yeah
they are published all of them are here
okay
so let me talk more about the feature
and
[Music]
what what it does and what are the
current limitations I might repeat some
of the uh the the the slides or what is
written on the slide but let me say okay
so we currently compile the current
active project and we reuse its
launch.json it's actually on the roadmap
to introduce loud launch.json or launch
configurations for your workspace so
then you'll be able to have one
configuration for your whole workspace
and use that one instead
okay what happens if some of the
projects fail to compile locally fail to
compile on the server when we published
them or anything else happens
we just failed a whole operation and
then it's up to you to sort it out what
has happened I guess we'll give you
accurate you know Diagnostics to figure
it out easily
then
that feature and the best for that
feature is that it's only V6
implementation so it lives only in the
the visual studio code extension so you
can use it with older environments no
matter if you have to anyone out 20 21
19 whatever you can use the latest
extension in Marketplace
and then publish to other environments
good do I forget something
yeah you you check it out from the
slides
okay let me move forward
so we are back to the uh complex graph
and you have published uh
your project and all of its dependencies
and then you continue developing
so what you would do is I guess you get
one project you publish it you modify it
you debug it everything that is usually
in your normal day-to-day work
so in order to demo what will happen if
you have a dependency publishing not the
whole workspace but just few
dependencies I'll pick cherry pick some
of the projects for Simplicity I'll pick
a level 13 11 and 12 and I'll open a new
smaller workspace
so here it is
so P11 and p8 are part of my workspace
P11 p8 and p12 this time are part of the
dependencies available on the server
and now I want to talk to you about
dependency publishing and what actually
happens on the server when you publish
some of the so-called dirty projects in
your workspace
so we move forward
we do not hear with Asterix the the
dirty projects as common said in a
workspace dirty project means that you
need to modify some of the source code
uh or Abdul Json right
yes
so let's pick the first scenario
you have
dirtied both P11 and p8 and P11 depends
on p8
and then what we would do is we want to
publish p8
then we'll create that uh that file with
extension depth.app
and what we'll do is we'll publish that
one to the server
will before actually publishing or
actually compiling on the from the
server side p8 will uninstall all of its
dependencies b11 and p12
then we'll compile publish compile p8
and then we will install all of them in
the right order
another scenario if we want to publish
b11 which depends on p8 and both of them
are dirted you saw that in the workspace
if you're dirty both of them and you
compile
the dependent one it will actually
compile the base one also so that will
happen in the server as well so if you
want to publish P11
we will publish P11 with that Dev app
file what we'll do is we'll uninstall
the whole graph
we will publish
both p8 and P11 in the right order p8
first P11 compile them and then install
B12 back
why is that needed so you can get all
the data updated
more
since it's the topic of today's session
is customizing that assumes that you
have the flexibility to change that
behavior you can go to your launch.json
file
you find dependency publishing option
parameter over there which is synonym
and you can change that behavior why
would you want to change that behavior
again we take as an example our base app
our Benchmark for big application as I
said
you you might want to actually ignore
publishing p8
if p8 is big and you know that your
changes to the app that extends p8 or it
depends on p8 are not breaking changes
so you're still able to work with the
older version of it
then you might want to skip publishing
and recompiling sending to the server.ph
if it's that big and if if its
compilation takes time so then you can
specify ignore
strict is actually only about the
workspaces but you cannot go here
to the our official documentation page
and see more about these options
let's take a look before rapid
application development let's take a
look at demo for these stuff
so now you have to bear in mind because
I didn't have the time to switch right
and I need to switch
we switch to another workspace
that's the graph just as a reminder
and we have P eight uh P11 and p12
all of them are published what we have
here is one base page and we have an
extension and that base Pages 50
8 and let's open 508 and see what it
does
we already published it with the
workspace publishing so there are some
uh there are some messaging from here
the first one comes from p8 and then the
second one comes from p12
and then it also prints a variable which
is part of p8 hello again coming from p8
and then P11
that should be enabled that is old
so let me show you now what we will do
is we'll dirty both of them we'll change
that variable let's say coming again X2
and let's change hello to high
good
and also dirty
P11
as I said okay
coming from here should be updated let's
remove should be updated
that's part of the testing before and
let's change that one also to high
so what should happen because we'll
reinstall
p12 is p12's message should take into
account the change of that protected
variable
and the rest is it's obvious also P11
and pH should do that so we published
P11 right
we go Ctrl shift B then we say publish
say without debugging that's fine
no workspace folder good
even better let's try to reload the
window so now you're seeing
troubleshooting live
yeah I was concerned for the previous
one not for that one for the previous
demo
good
let's try to publish again
okay now everything's fine
we're publishing
and now we got to p8
the first message coming from p8 that
one we didn't modify it second one
coming from p12 we can see that the
protected variable has been updated
because we reinstalled p12 and then from
P11 again we can see the updated message
X2 high and then coming again and then
here we removed whatever it was I don't
remember
good
so with that said
we move to rat rapid application
developer development in common we talk
about it yeah so let's briefly talk
about red
you know I will try in like three slides
explain what's going on beneath
so what is rapid application development
this feature set has been introduced
like I think four years ago or even more
and what it serves it's a fast
incremental compilation and deployment
step in one word
so all these things are happening on the
server so this is all a server thingy
and not a visual studio code thingy so
in order to I I will try to explain what
is red so you will see that it's
probably worse using it so let's in
order to understand how red Works let's
just go back a step and I will try to
explain on this diagram what happens if
you say Ctrl F5 on an app so let's
assume that you have this base app which
has three application objects stability
PJ and code Unity then you say control
F5
and this app file is sent to a business
center server so our services
and then with the control F5 phone
within Visual Studio code the at least
these three things happen so it will be
a compilation there will be a thing and
there will be a run yes when the browser
comes out
so let's go what does it mean
compilation so on the server this app
that you already compiled we are going
to recompile that it's not that we don't
trust that compilation is because at
this point on the server we are going to
compile it a little bit more it's not
just we are going to create abstract
syntax with them bind things together we
are going to emit things we are going to
emit two constructs we are going to emit
something called the metadata
and we are going to emit c-sharp code
and this metadata this is an overuse
term in our case metadata means an XML
file and for example for a table this
XML file it will Define how it should be
created on secure server
for a page it defines how it will
interact with the web client
so when this thing happens then from
this metadata you know we are going to
create the physical table
and then when you run and this is where
the interesting thing happens you know
using this metadata part the XMR things
and the C sharp chord we are going to
generate dotnet DLS we are going to load
these.net dlls in the running Business
Center process address space so
basically at the end
you are running dotnet DLS
okay so let's move to red
so the important part here was that
compilation will produce metadata and
c-sharp
so if we go back and we take
this scenario that
you had a base up then you published it
on the server then we compiled on the
server and we created a metadata out of
it yes in the table called application
object metadata table which is
an app table it's not a tenant here but
it's an app table so assume that we do
the following thing we modify table a
yeah like you know we add the method and
we had a completely new table e
and then we publish again with now with
the red publishing
so what will happen is on the NSD on the
server
is that we are going to only take table
a and table e as files
there even though they may reference
other symbols from their own project
we don't care about them we will treat
them as symbols so we are going to
create some sort of artificial symbol
file in order not to parse and bind too
much
and then basically we are going to do a
div in the application object meta data
table and we are going to
update table a and insert table e the
important part here is that
if red works if you have 7 000
application objects and you do a red
publishing and you modified only two the
time it takes it should be
similar as you would have only changed
two files and that's the difference
okay so that's
how red Works in
yeah that's how it was designed at least
so let's try
and
let's do a demo okay
so here you know this is a daring demo
I'm telling I'm telling you why this is
our base app I took it you know like
two o'clock I took it from our
repository so here you have 7 000
something application objects so
everything is here this is the customer
list
and I already published it you know at
two o'clock
and it is Ctrl F5 on my machine which is
a medium powerful machine my machine
with I think I have 64 gigs and but yeah
it's three years old machine it took
like four and a half minutes to publish
which is not a bad time
but let's see what happens if I do red
so let me add a new chord unit here
and let's use a snippet
let's give it an ID I don't know
yeah so let's save this one
and then let's do a riot publishing
which is you know let's use the command
so let's publish it without debugging we
don't want to debug this
so I click this one
it will do a pub it will do a full build
and until it finishes let's just
continue with the slide
so the shortcuts for red are Ctrl alt F5
in Visual Studio code if you just want
to publish without debugging or ielt F5
if you want to do it you can you want to
do red publish with debugging now
there are a few things uh you should be
aware when you are doing rat publishing
so red publishing requires a Baseline
because it's an incremental publishing
so you need to have something that it
increments
manifest changes we don't support that
are not supported for it there is an
unfortunate side effect of red that if
it fails you cannot re-read until it's
successfully publishes you have to do a
new Baseline
and we don't really support this kind of
big rename refactoring so you know
that's not good for that so if you if
you if you do uh
change an application object ID
refactoring that's not gonna get
supported
and you know translation permission
layout and web service definition if you
change these ones they don't participate
in red only
ar5s participate in red
okay so let's see if this publishing has
finished
yeah so previously it was and don't
forget that you know whenever I'm
sharing something you know the DVM
process style Desktop Windows Manager
process starts running in the background
that also eats a lot
so you know this was 1728 and it
finished like like a minute
yeah but it was five and it's almost
five minutes before so you gain things
yes normally should be 20 seconds you
know publishing base up
at least my experience says if you don't
do huge amount of changes
okay
so well I think our time is up
but if you have questions you know just
ask them on the on the app and then we
will try to answer them yes I think it
depends uh or if you cannot I mean if
the organizers don't kick us out it's
the last session well I'm staying here
you can come by and you know you can ask
questions like for five ten minutes I
will stay here if you want
okay but that ends our presentation
thank you very much
