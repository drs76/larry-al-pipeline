# NAV TechDays 2019 - Control Add in development supercharged

- **Source:** https://www.youtube.com/watch?v=_IjppPvkmgE
- **Video ID:** _IjppPvkmgE
- **Channel:** mibuso.com
- **Published:** 2019-11-27
- **Duration:** 92m27s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

[Music]
thank you almost got my name that's good
so thank you for coming to my session
called controlled in supercharged my
name is vicoslavic
people usually know me as vieko and i've
been speaking at tech days for quite a
while now
i would like to start just like waldo
did
i will ask you how many of you have been
to my sessions before
no no no don't clap you
you you clap at waldo sessions at my
sessions you raise hands so it's so okay
good wow look at you
so well this is relaxing for me at least
um
so uh
this session is going to be about
control of this what a surprise and
take
seats and relax this is there is no
better time to sleep than just right
right after lunch so
um yeah
something is wrong with this i think
it's they have technical issues oh no no
no it's not so um
when we are developing control of things
or at least uh the way we were mostly
developing control of this or at least
the way i saw most controllings out
there being developed it sometimes feels
like this and what i want to do in this
session i want to take us all from this
kind of tooling to this kind of tooling
when it comes to control it in so let's
see how far we can get
um
what is this session going to be about
it's going to be about making control of
this uh development work and you may say
yes my controller didn't development
works thank you very much but remember
the x so uh we are going to talk about
real uh real real stuff here so uh we
are going to talk about practices that
work practices that don't and why they
work and why they don't we're also going
to
try to do development web development
like web developers do not like the
accountants do
you know
when i speak to my mvp colleagues like
from those um you know superior
technologies like c sharp and azure and
stuff they kind of joke with me like
what do you do at those business central
and nav conferences you get together and
what both journals and
so
well uh this is their perception of us
and you know
our development sometimes looks to them
just like that so what i want to do here
is i want to make you or actually show
you how to develop for web not like an
accountant at least okay so speaking
about practices that don't work one that
absolutely does not work is trying to do
36 demos in one session so
i'm going to try to cut it down a little
bit but let's see how far we will
we will actually
succeed so building controller things is
easy in ale have you tried that let me
see
so perfect because you have an amazing
all in all in one environment where you
can do just about everything you define
what you used to define as interface
earlier in net you define the manifest
that you would normally develop in xml
then you put it all together you put
stuff anywhere you want you have a free
folder structure you have the language
that you know the type system that you
know and everything is beautiful so
let's take a look at an amazingly simple
controller din
that i have developed for
this
particular occasion i have too many
windows open i hope you don't mind if i
close
down a few of them so um
it will just be simpler for me to to
navigate through this uh mess off
everything so
vs code yeah i will actually switch this
i've been
i actually prefer dark team
i'm on the dark side you know of the
force
um
so this is a very simple controller then
so it doesn't do anything
i call it simpler payment registration
so if you ever done payment registration
during your journal posting career
then you might know that it's not the
most user-friendly piece of
functionality in there so i decided to
simplify a little bit i have a page
that invokes a code unit and that code
unit prepares some data pushes that data
into the controller then which has
actually this is the script this is just
some dependency that i have to nicely
format numbers this is my script so
let's take a look at this script
this simpler script is yeah this
it does everything it it builds the
controller in interface
it handles the state it handles
calculations
it handles html events state absolutely
everything so all is in one place and
when i run that
since everything is so simple
it will get published
i need to sign in who would say
and there it is so this is my simpler
payment management i can go here i can
click around and then you know i can
select
stuff in various currencies and then
when i'm done i click post and then i'm
done
so
that was simple right
and it was easy but yeah this really
doesn't work easy is
tricky
because
you might like this like it's all nice
easy simple in one single place we can
do a lot of things with that but there
are a lot of problems with it the first
problem that i find with it is the what
all web developers call global scope
pollution we're just putting everything
in one script which runs in global scope
so it's a mess that we can break
by introducing any other script or we
can easily break any other script we
introduce because we're just not paying
attention that's something that we all
often fall victims of
the second problem that we have is
performance it might not be immediately
obvious but
it does not render too fast because i'm
really rendering everything procedurally
i'm re-rendering entire interface every
single time i there is a smallest change
it just goes and renders everything this
might look amazing on your newest i9
9th generation
you know
processor but when you have like some
small machine at the customer's office
then maybe it's not going to work that
nice
the other problem that we have is
debugging if you have tried debugging
this stuff then well most likely you've
been doing it using the browser debugger
tools which are not the friendliest
especially if you like f5 to continue
and then you're in chrome and you press
f5 and it reloads everything so
we'll see what we can do about that as
well and
there is also browser compatibility
issue if i try to load this and i will
have to say trust me this time
trust me doesn't work in internet
explorer it just doesn't because it's
not compatible with it there are there
are issues it will break it will not
work and you know this picture if it's
not obvious why it's there it's
because of this the picture was taken
this morning in the speaker's
uh room
uh the other problem we have is also i
it's separation of concerns there is
absolutely none this is not the picture
from the speaker's room this morning
this is waldo's garage no
it's not so uh these are the problems
that we will try to solve in this
session so we will try to find a better
way to do all of those things
another practice that does not work is
developing in one file so i have one
nice javascript file which is one big
fat spaghetti monster
which is just going to be more difficult
to untangle the more we go so something
that's good for browser which is this is
not good for you so uh you have to uh
try to not have thirty thousand lines in
in one file uh we will address this
issue a little bit later so uh
actually you know we can do much better
so
let's
do better
um
the next thing that i will do is
is i'm going to address the fact that
this is all one file because that's a
bad practice
so web developers don't develop in one
file imagine you putting all your al
objects just in one file that's
pretty much the same thing so you don't
do that and what i've done here i have
split it up so i have a number of
files i have my start script i did have
that one earlier so it's nothing new in
here i have this constant script which
just have has constants and if i need
more i will just put them there then i
have this ui script which is in charge
of building ui and it's in essence just
uh dom manipulation code then i have uh
this
interface script uh sorry state script
which is handling state but it's not the
most beautiful script ever you know see
this is not just handling state it's
handling events it's handling also a
little bit of dom and kind of i wasn't
sure what to do with that one so how to
properly handle it and then i have
interface which is you know also not the
cleanest one um so i'm sending data from
business central uh oh actually this is
where i receive data and then i send the
data to controller then it's also you
know i'm not too happy with it it
doesn't belong there but i wasn't sure
where does it belong should i put it in
a separate file and ui file and state
file yeah
so
yes it works it's exactly the same so
i'm not going to run this demo trust me
it works
it's exactly the same stuff just split
up a little bit more so that we can uh
we can manage our development better and
then i'll control it in
is looking like this
i have i've declared every single
controller in there sorry script file in
there but there is a big problem with
this
if i continue doing like that
then you know at some point i will have
150 scripts and then you know i will
have 150 declarations out there and
that's not going to work you know uh
i have to handle that somewhat better
but
you know the first thing that i want to
address is i want to address this fact
that i have
this thing here and
i have also
that thing here and also if i look at ui
oh my god like do you really handle ui
like that when you're web developing for
web
normally not normally you're using a
framework
so uh
let's try to improve this let's actually
go to another branch which i called
framework
and here i have this everything is the
same except i have this extra file which
i call framework so let's take a look at
what i have inside
so
um
i don't know if you can read this but if
you cannot then it says the last thing
the world needs at this point is another
javascript framework from you so
and let's actually stop for a second
here
and let's talk about frameworks
javascript is notorious about frameworks
because
all the time new frameworks arrive and
you know there is so many front-end
frameworks they are popping up like
mushrooms and it's very difficult to to
choose which one to go for and you know
the problem is it's not that there are
so many frameworks it's why are they
coming and what problems they're trying
to solve you know
12 years ago everybody was doing
everything with jquery i'm pretty sure
half of you here are using jquery on
daily basis when you're developing if
you're developing control events but
then newer frameworks have come because
they wanted to solve issues that
framework sorry jquery introduced and
they introduced some more problems and
then some other frameworks came that
solved those problems and then
introduced some other and yes
frameworks happen so often in javascript
world that there is even a website a
funny website like just mocking all that
which is called days since last
javascript framework.com and you know it
just shows you this number so
since i started talking about frameworks
there have been probably three new
somewhere on github so
one thing that does not work one
practice that i please ask you do not do
do not develop another one because
you will quickly figure out that it
wasn't the smartest investment that you
would have possibly done so we will not
be doing a new framework
and
let's actually forget about framework
for a while um
let's talk bundles so i started
talking about how bad it is to have one
big fat script like 30 000 lines
but uh that's actually what we want to
have in the end
um the thing is when you're developing
in al when compiler compiles everything
it puts everything in one object you
know it compiles stuff like when you
write in c sharp it develo it compiles
everything in one dll not 75 000 dls if
you have 75 000 files and the same we
want to have with javascript when we
develop
we want to be able to write in separate
files because we want to separate
concerns separate topics and everything
areas but
once we want to deploy that to browsers
we want to bundle that together so it's
actually a good thing to have everything
one file it's just bad to develop in
that one file
javascript bundles are good thing so
they group separate files together they
are actually improving performance in
the browser they also reduce http
traffic and it is actually your goal to
end up having a bundle
it makes things more difficult for you
in certain way but it's actually very
good and let's take a look how we can do
bundles let me introduce our first tool
in our toolkit today which is called
gulp
uh what is gulp
gulp is
well they call themselves as the
streaming
build system so well let's not try to
explain what exactly that means
their their primary task is to enable us
to bundle files that's number one thing
that gulp does
and it in fact is a task system it
allows you to write custom tasks which
automate things like and those things
are typically shuffling files like
reading some bunch of files doing
something to those files and then
spitting them out as either a bundle or
some some other files so that's what
gulp does and beautiful thing about gulp
is that it taps beautifully into visual
studio code so let's take a look at that
i will open my first gulp branch which
is called gulp hello world
yes framework is deleted i don't need
that one but what i need is this gulp
file i will not show you how to install
gulp well
you have instructions on on gulp website
all installations here are npm install
then the name of the add-in that you
install and then save or save dev in
this case it's safe dev anyway i'm not
going to show those things i'm just
going to show you what gulp does and how
it works so this is a gulp file gulp
file is necessary because gulp uses gold
file when it needs to do automations and
when you have a gulp file something like
this then you can use gulp to automate
and how can we automate well we can
always go to the terminal we can say
gulp
tasks
and see which tasks are available
we we see that hello task is available
which means we could also say gulp
hello and then it will run the hello
world task and it will print this hello
world on screen another thing we can do
with tasks is we can go to uh the
command palette and we can say run task
and then we can choose gulp hello
because visual studio code recognizes
that there is a task in the gulp system
and we can run that ask let's for now
forget about that so i'm going to
continue without scanning the task
output that's if you have some linters
it can be useful but since i'm not using
any right now i'm not using that either
so here vs code has just executed my
gulp task to automate this hello world
so
um
doesn't look too uh useful yet but let's
take a look at what else can we do with
gulp
so in fact before i
get to show
what can it be used for well just about
anything
there are more than twelve thousand
plugins for
actually gulp related downloads or
packages on npm more than four thousand
golf plugins
uh also
you can use it for bundling for
automating
you know transpilation for example
minification beautification
ugly uglification whatever they want to
call themselves these days uh you can
lint you can annotate you can document
you can do anything zip ship anything so
let's try to make something useful with
gulp so i'm here going to skip a few
demos out of those 36 so two down
and i'm going to jump into this gulp
debug so my gulp file is you know it has
grown
and let's start by saying gulp i'm sorry
just gulp tasks to see what i have
yeah enter that's good to press
occasionally so i have two top level
tasks
one of them is called build one of them
is called watch so the build task is
also as you can see hierarchy of tasks
which does a lot of smaller things so
let's take a look at what what i do
inside build task i build javascript i
build css
both are actually split up so i have
like nice
split up system
i'm also
inside this bundle.js i'm reading all
javascript files except for start js
file which i don't want in the bundle
then i'm initializing source maps that's
another plugin we will see what that is
for
then i am concatenating all files into a
single file which is bundle.js file name
it's going to be this simpler min dot js
then i'm uglifying that uglification or
minification or whatever you want to
call is the process of reducing the size
of your file by changing the variable
names to the shortest ones possible and
also by removing any unnecessary syntax
constructs and also simplifying syntax
constructs so they take the least amount
possible
and then we write the source map and
then we write the file itself so this is
what my build js does and if i run
gulp
build
it will build my
simpler min js yep git has detected that
there is a change i can take a look at
this so it has really uglified my
javascript code it doesn't look anything
like my
uh my original code it has code up there
and it has a source map down there what
is a source map well it's a nice tool
that allows me to debug my code my
javascript code regardless of where it
comes from from which file and
regardless of how it looks in the end in
this uglified bundle file i can still
debug it using visual studio code and
that's exactly what i'm going to do
at this stage i'm going to
first run this
so i'm running this project it's
deploying it to business central
i can um
sorry i will close this one
and then i'm going to set a breakpoint
in my
state
script
here entry click you can see that it's
actually red ah sorry i apologize yes
no no no i would have to say trust me it
works and then you would laugh and i
don't want to afford you that pleasure
so i'm going to launch chrome uh we will
we will address this a little bit later
so uh
i'm launching chrome because i'm now
going to use this session to debug my
business central
so i'm again inside here
and yes i can see that this is still red
which means if i click here my debugger
kicks in
regardless of the fact that you know
it's somewhere very very ugly in that
uglified minified single bundle file
my source map tells my debugger where
exactly to look for the source line of
whatever line it's currently executing
that's beautiful so this is for example
something that gold can do for you
another very nice thing that gulp can do
for you
is
it can watch so i have this gulp watch
task so i can say gulp
watch
and then it starts watching the changes
so if i do something like alert
clicked
what do you know
save you see
it bundled up everything together so
when i deploy this now to business
central
i don't need to do anything it's just
yeah it's just there so i don't have to
do any manual deployment zipping or
whatever so um all of that is fully
automated by gulp so this is
what
gulp can do for us pretty pretty cool
i would like to introduce another tool
now that we've seen gulp which is the
first toolkit that you will probably
want to introduce into your toolkit
the second one is called babel what is
babel well babel says for them this
babel is a javascript compiler wow
so
yes every browser has a javascript
compiler all javascript code ever is
compiled inside browsers so why do we
need javascript compiler
well
let me show you
so i'll go into jsfiddle i don't know if
you know jsfiddle
you can play with javascript here see if
something works like for example you can
say
alert hello or what blah i'm doing typos
you run that it shows you
when you execute it shows you the output
so imagine that you go on let's say
stack overflow and i find a nice chunk
of code
that you just
want to make work for yourself
and then you are copy you copy that into
stack overflow sorry into into jsfiddle
and then
you want to try to make it work
and then you run it and then it
doesn't work
so um why doesn't it work can you read
this even
so
yeah so
it's you know for me it's very difficult
to figure out why does not this work
because it you know it looks like
perfectly
valid piece of javascript code to me so
what's the problem
and then i realized oh this is edge it
might be that it's not fully browser
compatible so let's copy that and paste
it into chrome actually this is edge
just chrome acting as edge
so i run it in a more modern browser and
i run this and it tells me oh the echo
is the best
cool so uh
where is the problem well i'm using a
few syntactical elements here which are
not known to edge
or god forbid internet explorer whoever
uses it still so
i'm going to copy this
and take it over to babel the javascript
compiler for compilation and then i'm
going to try it out
i'm going to click here and i'm going to
wait
how's life ah it's awake
i'm going to paste this here and
when babel compiles this
it actually didn't run that code it run
the code on the right side so
it's this
so see
this is browser compatible code for this
here so you know javascript is a little
bit like your wife when she tells you
this what she really means is
[Laughter]
that stuff over there i'll have to try
babel next time at home so
let's actually see if this does work so
i'm going to copy this
over into edge
and i'm going to run this now and see if
this really is
working so
yes vehicle is the best of course he is
because he only needs you know one line
to write all the junk
so
back to
sorry back to our original
code
if you followed what i was typing you
might wonder what happened to waldo
in this line so let's see what happened
to waldo
so i'm going to remove this part and i'm
going to inspect
what happened to aldo so
waldo
and then i run that
while the who
okay uh well
come to mind one world recession
tomorrow we we are at far better terms
that my session would make you believe
so
babel
mabel is a javascript compiler it makes
your
funny space
star wars uh level uh jedi javascript it
turns it into something that common
browsers can
uh execute on and process
uh it transpiles the syntax into the
common syntax and you can choose what
common syntax means it can you can
choose the browser target that you want
to target you can choose a lot of
options
it also polyfills missing features so if
you're using a functionality such as
let's say promises that all the browsers
do not know about then it will polyfill
them so that you can use promises so
overall it will turn any javascript code
into javascript code that runs without
issues it will optimize code it will do
more and of course you can integrate
babel with gold so let's do that
at this stage
i'm actually going to run internet
explorer
and i'm going to run
i'm sorry i'm going to
yeah i'm not going to run anything yet
i'm going to first run my
simpler demo
so when when i get in
i'm copying the url i'm pasting that to
internet explorer
and when i sign in
nothing happens because it cannot
because if i look in the console it's
full of red stuff because yeah it's full
of syntax that internet explorer just
cannot process
good let's put babel to work here so i'm
going to
remove all things that i changed and i'm
going to go into my
babel demo
and the only thing that has changed here
is that in my gulp file
i now have
babel plug-in
and i put this babel plug-in to work
just after concatenating all the files
and just before uglifying
so my babel will take care of
transpiling all my code into something
that will work in all browsers
and then uglification will make it small
as small as possible and when i run this
this is now
chrome and i'm
or actually edge acting as chrome or
chromatic z whatever you want to call it
and i'm going to internet explorer
pasting the url again
and
trust me it works stuff or
let's take a look
yeah it might be that i didn't run gulp
that's true so
in any case let's close this and
let's go back i will just
save
a script file
because
my watch task should be running internet
explorer is playful
so yes it's now bundling
and now i'm going to run it again
and let's try
no
what's going on this this explorer is
just it's not doing anything in fact i'm
not sure it's even gulp it's that it's
it's blocked so
it's not responding to two things and
yeah
it's not there
i will just once more i will just try to
manually build because it might be that
something is uh wrong with this i will
stop everything and i'm going to do
gulp
build
because it didn't close i should close
and restart because i have watch
configured as a startup task so that it
starts up automatically who knows maybe
things have gone wrong i'm just going to
run once again
before i fall back to trust me it works
because it does work
yeah
you you know me it's now a tradition
so i'm going to retry internet explorer
there so yeah
thank you
so this is what golf can do for you well
i don't know why you would want to care
about internet explorer in the first
place
there is still 0.0 something
people in the world who are using it so
yeah why why actually annoy them
so by the way all
uh business central sort dynamics nav
users who are using the old version of
the universal client
actually use
internet explorer another reason why you
might want to care about internet
explorer is that the windows client for
those who still use it when they embed
a web controller then they also use
internet explorer so it might be
worthwhile to tap pop babel into your
tool chain to actually uh let it take
care of these things so this is what
babel does
it's a pretty amazing piece of tool what
else can gulp do
for example for us in the al world well
things that i have put it to use is
when i'm building control of things for
earlier versions of nav and well
it's stupid to say like earlier versions
of business central because i'm talking
about nav so um of course i do bundle i
zip control it in files i'm deploying
stuff through powershell like when
you're developing control of this you
have to do all these acrobatics with
zipping files creating controller in
records uploading the resource file etc
so i automate all that through gulp i
just press f5 in vs code and it ships
everything through gulp into business
center sorry dynamics nav
also it can build documentation for
example from your al source files it can
extract the controller then resource
file from the app file like i build it
for business central then extract and
reuse for
dynamics nav and probably you know a lot
more but you got the idea
and
unfortunately
the story about gulp and al and stuff it
stops here
because uh
the the more astute from you might have
noticed that
when i'm using gulp
actually yeah
i will just have to sorry restart
my
vs code
you might have noticed this folder node
modules
who knows what node modules is
good
so do you think it belongs here
well microsoft also agrees with you so
that folder does not belong there why is
that what is node modules well when you
install
uh gulp babel anything uh
npm
which is the node system package manager
something like nougat for javascript and
you know visual studio code is node it's
running on node.js so when you install
an npm package the node modules folder
gets generated for you it it contains
dependencies dependencies that you will
use either for development like gulp
here or dependencies that you will use
for runtime as we will probably want to
do a little bit later when we take it to
an even higher level so um the problem
with and with node modules is that it
now sits right in the middle of how our
al workspace and if you don't know it
you should
when you compile al what happens well al
compiler looks through every single file
in there to see if it's a nail file and
then it compiles that file and it will
look through your node modules folder
and try try to find any al files in
there and it shouldn't be doing that so
if i actually take
an example where
where is it here
i have
installed some funky al
sorry npm module and if i try to package
that i will see that it fails
so compilation started and then it will
just
it will start showing me these errors
because there are al files out there
somewhere deep in
node modules hierarchy which are guess
what not al files there are some binary
files containing audio
and yes that will not be compiled so uh
that's that's the end of the road for
for us in ale trying to integrate
all these funky beautiful tools into our
workspaces so
what do we do
well first
one of the practices that does not work
is to keep
nodejs inside ale workspace
unfortunately you know in my opinion
microsoft should have done a better job
at making al play nicely with the
environment in which it lives which is
node.js environment it actually just
completely ignores that fact
and uh we have to live with that maybe
they fix it at some point but until they
do we have to actually use multi-route
workspaces and i don't know if you tried
multi-route workspaces i'm just going to
show you how to actually use them
multi-root workspaces are a feature of
vs code that allows you to have
multiple workspaces loaded at the same
time so
they can belong in the same subfolder or
they can be from multiple different
subfolders is up to you but if you put
like one parent folder and then all
related workspaces as subfolders of that
and then you get in it in the parent
folder you will have a very beautiful
git controlled
master workspace which controls all of
your interdependent uh workspaces like
in our case maybe we can put al in one
and gulp and all automation tasks or all
web control add-in development tasks
into the other workspaces so let's take
a look at that
this will be a quick demo i will not run
anything so just open this
split up simpler workspace where i have
al in here
web in there
and you know this is where gulp lives
with node modules and all this is where
air lives without node modules or any
pollution from the tools that it doesn't
play nicely with and you know all of my
tasks are configured here so uh all of
automation is configured here when i
compile when i save a file the watch
task will bundle it
it will actually ship files across into
the al folder so i can i can check that
i can open i can first make sure that
watch task is running it's not because i
didn't restart the entire this code i
will just do
gulp i'm sorry not from this folder this
is al folder
and then i will go into
web
and i will do gulp watch
so this will run
the watch task and then if i just go
here and just change
a line of code
you will see that it has actually
updated
two files so one file is out there and
well
and this file simpler min is in my al
workspace so
this is now beautiful because al is
concerned with ale
gulp is and you know you as a
controlled developer in web department
is are concerned with something else and
it all plays nicely together not
because
al still doesn't live nicely with multi
uh root workspaces there are a number of
things that al does like for example it
hijacks f5
and one of the beautiful things with
multi-root workspace is that you can
create compound debug configurations
where you could say when i press f5 i
want to launch
like uh i want to launch webpack here
with node.js web server and i want to
launch a chrome debugger on top of that
and i also want to launch the attach to
next process configuration of al and
then all three come up together and each
debugger is attached to whatever that's
not unfortunately possible
uh in vs code at this point i tried
crazy things to try to make it work to
present it here it would be really cool
but you cannot do that that's why i will
for the for this session and until that
this gets gets fixed i will have to
actually always run al and then run
chrome as a parallel debugging session
when i want to debug web stuff or
control it in stuff that's how it is and
maybe that gets fixed maybe not we will
see also al will put some ale artifacts
into you into other workspaces like for
example this rad.json it will always get
injected if you accidentally press or
invoke any or try to access any al
feature from within your workspace uh
web workspace which is going to be
difficult not to like for example you
will accidentally press f5 and there you
go al will immediately try to run your
web workspace and will fail it will put
red jason in there so yeah you you need
to take care of that you you get used to
that and then that's it
good
remember frameworks
this jungle of
different frameworks that i said like
let's talk about them later
there is
vast uh ocean of these things and
i've put
the reason why i don't have more here is
that you know there is no more room also
i needed to get ready for the session
otherwise i would have to spend like
entire career putting logos of some
obscure frameworks out there
however in that jungle of frameworks
three frameworks have kind of bubbled up
as the leaders
i call them big three it's not only me
who calls them the big three and what
are the big three the first one is
angular when it appeared first it called
themselves super heroic javascript model
view whatever framework
it's from google and it's funny
google did it on typescript which is
microsoft's back at time when steve
ballmer was like the chief google hater
officer of microsoft and they were
really fighting each other so that's
that was a very very nice symbiosis of
of google and microsoft technologies so
that's angular it has advanced quite a
lot since then and it's one of top
frameworks these days the next one that
appeared like three years after was
react by facebook so they have uh first
developed their own user interface then
they released it
into open source and now it's one of the
most popular frameworks it's all they
are pretty unpretentious they say about
themselves a javascript framework for
building user interfaces full stop so
they are not super heroic or something
like that and then finally a curious one
happened by a single developer called
ivan yu
which is called view
which is just you know popped out of the
blue like in early 2015 and just gained
quite some traction and is extremely
popular these days i know that here in
this audience there are people who are
using vue right
okay good so um it's
something that disproves my point when i
said like don't build another framework
you
actually that guy did and he succeeded
but it's you know one in
million um
good uh let's talk about these
frameworks what do they have in common
the first thing that these frameworks
have in common is if you want to use the
full power of them you cannot just write
something in them and then put that into
a browser and then you know expect that
it will run it will not so all of them
will require some kind of preprocessing
transpilation beybling whatever you want
to call it that will translate that
framework into usable javascript code so
we will have to use some kind of tool
chain to translate whichever one you
choose into something that you can
actually use inside browser
they all have huge developer base which
means there is a vast knowledge base out
there when you google or bing i don't
know if you bing
any question or if you look at stack
overflow or anywhere there will be tons
and tons of stuff done of issues and
solutions
and they all have great support in vs
code actually vs code is number one
development environment for all three so
it's just it just took over uh web
development world
just as it did business central or nav
development world um also
there is a difficult question we're
trying to choose because you know if you
choose a wrong framework
you will suffer from it ever after and
then refactoring between different
frameworks is not just about changing
user interface because you also make
data and model and different kinds of
choices architectural choices around the
framework that you choose so which one
should you go for well
all three will work with business
central in fact every single framework
you can make work with business central
there is none that you cannot at least
with gulp or with babel or with other
tools which are available and you will
see some of them you can take any
framework out there and make it work so
that's not a question all will work
i would say choose whichever one
suits your development style but also
take a look at numbers
if you take a look at stack overflow
they did this most loved most dreaded
and most wanted framework uh survey and
react is number one with 74 percent of
web developers actually loving react
angular is somewhat low at 50 like
people who are using it like half of
them like it the other half is kind of
ah
just like seaside you know probably
um
about dreaded well angular leads it's
the most dreaded framework like people
who are using it they mostly are afraid
they're scared shitless of it whereas
you know react nearly nobody is scared
so um this is what is on the dreaded end
wanted end is of course react is again
the first one
and then uh it's view and then it's
angular so that's what stack overload
overflow says
google says a different story so google
says that react is uh the most commonly
searched term then it's followed by
angular and then followed by vue and if
you want statistics of how used how
often they are used well you look at mpm
which is the site that ships them as
dependency then you know react is really
on the top and
it's gaining traction it's actually
coming up whereas these two are kind off
you know
honestly i don't expect view to to win
it it's popular it's nice and
and all but yeah which one did i choose
well obviously not few uh view is
beautiful by the way but i don't quite
like it and so which one did i choose
and why did i choose it
well i choose react
and let's take a look at why i choose
react
well react is very straightforward very
simple
it is also not template or
you know it it's not template based
which means it doesn't have some
declarative syntax to build user
interface if you take a look at
business central and seaside if you want
building page object is declarative it's
template-based you can do those seven
kinds of controls that you can do and
nothing else that's why we are here
sitting in this session because we want
to do something else with user interface
uh declarative languages tell you this
is you know this is the framework you
can use that framework and nothing else
is possible sorry next version go there
and make a git issue if you want react
says nothing like that they have their
language and this is fully under control
javascript you can run whatever you want
you can build with everyone very very
simple it's imperative as opposed to
declarative and it makes it really easy
to use you will see quickly about it
it's also very flexible about
architecture it's completely
unopinionated about a lot of things
nearly about every single thing it lets
you choose whatever
way of doing work you prefer and it also
in my experience fits best with how al
and javascript work together
and of course numbers do matter when i
have a problem react something problem
enter and i get a solution nearly
instantly whereas you know with others
its numbers tell me that i would expect
to get less of that
um how do we get started with react
obviously you cannot just start you know
notepad start writing react because you
need to have a tool tool chain
configured there are a number of
available options like for example if
you have ever built a control sorry
an extension for vs code i know that at
least one or two people in the audience
have built sitting over there maybe some
are sitting out there you have used the
almond which is you know
building up you know project structure
creating like starter points with
putting boilerplate plate code together
and stuff like that there is create
react app
which is also a command line interface
utility which can get help get you
started there is this manually from
scratch
kind of guide which i actually prefer i
prefer doing it from scratch because it
only takes two minutes it's very easy
and it gives me complete control over
everything and it doesn't push any
decision on me it doesn't choose which
package manager should i use it doesn't
choose for me what version of what
dependency i want to use it doesn't tell
me which test framework i want to use
etc so i
just start off from scratch and uh can
do anything
i want also it gives me minimum
dependencies installed which means it
will keep my bundle files smaller
good the first thing that you will set
up when doing this from manual workflow
or which any of those automated code
builders will do for you is install web
back so what is web pack
webpack is a static module bundler and
it's very very very different than gulp
so gulp is also module bundler but gulp
is kind of stupid about it it takes your
files
one two three four five then it glues
them all together
chunks out turns out this
bundle file and there we go webpack is a
little bit smarter about that so it will
still generate the bundle file but it
will do a lot of optimizations and it's
also heavily configurable you have a lot
of different plugins that you can tap
into that process
which will make that optimization even
better
the number one optimization
that webpack will do is on this output
bundle that it will make sure
that this output bundle contains only
what it needs to contain and it will do
that by building a dependency graph and
then when it has this dependency graph
it will do an optimization which it
calls tree shaking i will show what that
is and then it will come up with
something that is very small and
contains just what you need it to
contain and it's not only limited to
javascript it will do that the same for
style sheets for images and any other
kinds of assets so what is this
tree shaking optimization well every
webpack
bundle starts with one entry point
that's one module one file which says
okay start here and then this module
probably depends on two other modules
and this module b depends on two other
and d depends on these two and e depends
on this one c depends on e and f and f
depends on only j so this is like an
example of a tree that has been built
after webpack started optimizing and
then it runs dead code detection which
goes through the code and tries to see
which top level function from which
module is or is not used and when it
detects that it will actually mark those
and when it marks those these are that
branches it shakes the three those fall
off and what remains is the bundle which
is optimal size contains only what it
needs to contain and will guarantee to
be the smallest possible and
will cause least amount of traffic or
complications for the browser when you
have npm managing your modules and
dependencies this is important because
those modules when you install whichever
module you want they will install
thousands of others and that happens
constantly so you really need a good
optimizer to make sure that you only use
stuff that is necessary
good
webpack with react works pretty nicely
it use react user specific javascript
dialect called jsx this jsx
looks at first view it actually looks
very ugly because it's mixing up
javascript and
html and you don't really see the
boundary between the two it looks really
kind of a mishmash of those things
well webpack uses babel to transpile
this jsx into actual javascript code and
then it includes all all dependencies
and uh it all it results in a single
bundle file so
let's actually try to see a react hello
world example this is
an example of a component which just
prints hello world on screen and let's
take a look at that in practice so i'm
going to open another workspace
so
here is my
react control control or component with
just results in hello world
i will run that
oops
yeah
i didn't start
web back because
my browser was
uh sorry my vs code was running already
so we'll run it again
let me take a look f
it's not running so we'll run it
manually
i normally configure my workspaces to do
this automatically on open folder and
most of them are like this i don't know
why this branch isn't so
now it's
running i
i will run it in chrome and here we go
with my hello world so
as you can see this is just the typical
javascript class
it uses it has random method
it uses return syntax and then it
returns
a chunk of html so this is what jsx is
it
simply this html gets translated into
javascript object representation
and then if i want to use this app
i can use it like this
i simply return the app tag this is how
react does that so pretty simple pretty
straightforward even though at first it
may look a little bit ugly and
unmanageable it is absolutely not
let's try to do this simpler in react so
we want first to start by creating
necessary components so we will have one
data container one summary container
data container will have data entries
this will have summary details which
will have summary entries on top of that
i will have a view which controls all of
that and then when i see this as a tree
structure this is what i have view
contains these two those two contain
something else and it is a nice
hierarchy on top of that i'm going to
add data so my data that come
that comes from business central as a
json array will just be fed to view view
will distribute that as properties onto
the data container data container will
distribute that as properties onto
individual data entries on the right
hand side where i have summaries i have
those question marks because i don't
know yet exactly what that will be i
will get to that point a little bit
later something else that i will do is
when i click
this data entry i want it to turn
uh tl
so when i click it
uh it will turn tl that is something
that is managed through state as we will
see so uh this is the first step of my
state management where i will actually
turn the caller and the second one is
i will actually notify the view that i
have now selected this and view will
distribute information to the right hand
side where it will feed information
about selected entries and then summary
container will actually take care of
that so this is
the simplest
possible structure in react i'm just
going to show the structure i'm not
going to run that
so
what i have here is this al
sorry simpler with data in react where i
have these components i have my data
container which is this jsx file i have
my data entry which is this jsx file you
can see it is mostly writing html
and then just
doing some data binding which is not in
fact data binding it looks like template
language from from view or from from
angular but it is not this is actually
just writing out an actual value of a
javascript value so this
curly braces in react doesn't mean like
template syntax for variables it's
actually just saying from now on just do
javascript that's inside i can write
functions i can call
um like
interesting array functions from there
anything at all so this is my basic
structure my view component
that i have here
will receive
data as a property
so that data will come into the view
component view will then assign that
data to my data container my data
container will read that data it will
use data map to actually run for each
and then create a data entry component
of each data entry that's how simple
that is in react and you know when you
get used it's pretty readable and much
much better than where we started off
like at the beginning of this session
one more thing that i want to do is when
i'm developing in react i do not want to
have any extra steps when i want to make
this component available to business
central what i want to do
i apologize
they normally serve water here and i'm
now out of water so
yeah
anyway uh what i want to do is uh i
won't yeah throw me a bottle
i will throw mike at you later on
so um
thank you very much
thanks
apologize for this but
thanks
so i want to make sure that every code i
write will will run in my development
environment right now in my uh chrome
but when i just
gulp it over to business central i want
to just run there without me having to
do anything to it i'm going to build
this bundle and this bundle has to work
from business central without me having
to do absolutely anything as compared to
what i'm now developing in my web
workspace so
that is something i'm going to show you
so i have a very very very very simple
sorry
al mock system
where
my view is still
i apologize um it is still receiving
some properties
however uh what it does is it changes
properties to state we will see soon
about state what that is
and then um it makes sure that
in essence
yeah i have more components here
i don't want to go into deep details
about all of these i will blog about all
of these this is now ready i just need
to to push it out
the rendering part is exactly as it was
what is the important part here is if i
want to take a look at my app it is now
running view without setting properties
as you can see it's not setting data
property anymore on my view so my view
is completely detached from data it is
just a holder for other components and
my data is actually if sorry if i look
at my index it's also not just running
this
react render it is actually
i exposed a global function called
initialize react
which i run from my startup script and
my startup script is not in my folder
here my startup script is in my
controller then folder there
in my node.js web site where i simulate
everything so this start script is the
same start script that i will use inside
my controller then and i have a mock
piece of code where i have i'm mocking a
current page
so this is just
it
is the simplest way possible i have this
simpler send data which is exactly what
i would write in c sharp sorry al
corpage.simpler.senddata and then i'm
passing this data which is now a json
file containing all that data so it's
here so this is my
json data also i have microsoft dynamics
nav moc which is mocking the the
framework where i have invoke
extensibility method where i have this
on control ready method i'm notifying my
al
that
front end is now ready for communication
and then back end we'll call this
current page simpler send data to send
this chunk of json so when i build all
that
when i actually run
gulp build
oops yeah i'm in the wrong folder
so um
yeah i'm sorry yeah yeah i don't have
nav yet sorry business central i will
get there i forgot so i apologize uh i
don't have any business central but if i
just put business central and i build
this bundle over there and send
start sending files it will just work
and if i run this you know
whoever is developing this now whatever
they do will just work with business
central um yeah my
uh i've stopped my
npm sorry node web server
so now if i run
it's happening as if
this was run from a controlled
environment inside business central so i
can still click and it still works
exactly the same except that
i don't have to change anything i have a
bundle file which i simply copy over i
can do it manually if i want i just copy
it over to business central uh
controlled in development workspace and
it will work we will see that a little
bit later when i put these things all
together
so yes we can make react work with
business central very easily there are
no problems we will use webpack for that
we'll use all the tools that we have
seen so far
now having seen react we you can you may
ask yourself what architecture is react
because you know we suffer from patterns
and architectures and those you know is
it mvc is it mvp
is it mvvm you know all of these i've
heard these days here attack days uh is
it also maybe model view whatever
react does not care
so react used to say react is v in mvc
so it actually lets you choose so react
can be put to work with any kind of
architecture but you know it will be
very difficult to draw lines to say like
okay this is model this is view this is
controller etc it's just not possible
with react it has its own architectural
approach
and in react it all starts with state
state is at heart of it so um here we
will
clicked too fast
i want to
start showing you what state is in react
so i'm going to open another
folder
pretty sure it's this one
nope
apologize
yep
it's this one so i'm going to collapse
all unnecessary stuff i have even al
here
so
let me run this
workspace and let's see what we have
oh we still have this
must have selected
the wrong workspace well
yeah this is the one sorry
i have a simple counter component
what i want to do is when i click plus
and when i click minus i want
up this counter to go up or down
the problem is
that i have actually done it in a very
very amateurish way if i take a look at
my
counter component
yep it returns the counter
value and it has this on click event
where it increases this counter or
decreases this counter so i have state
in my component this state contains one
single property which is called counter
and then i expect when i click plus or
minus that it will just go up or down
magically well it will not
uh the reason why it will not is because
react doesn't do what vue or uh or
angular do it does not bind directly to
state
it actually detaches the state and the
view part completely and it has
different ways of accessing that so the
first thing that we have learned is that
yeah this state object contains
component state
and also we have learned that we cannot
manipulate that state directly by
assigning values there directly we do
not achieve anything so let's try to get
it make it better
so i'm going to
show you that in fact that statement
wasn't completely true i still have the
same stuff here i still have this state
i still have this plus plus minus minus
but i have another thing every five
seconds i'm going to refresh my view
so
i can go here
and i can start pressing plus
c
and now it will refresh and it will be
this and then i will go and click it
more see if i can get below zero and yes
i succeeded good so uh
what we learned so far is that we should
not
manipulate that state directly because
we can hit unexpected results so what
should we do then well let's fix this
once for all and let's make it the way
it
should be done incorrect in react so in
react there is this function this dot
set state where i'm saying which part of
state i'm modifying and then when i
modify that part of state react runtime
will make sure to update that part of
user interface which is bound to that
state so since this component is bound
to this state it will be
refresh entirely
so when i now start clicking this plus
or minus it actually executes that
um at
that moment so it refreshes
automatically so what we have learned is
that we should manipulate state through
this set state method however this is
not the cleanest stuff possible let's
improve this architecture so let's get
it to a more correct
state so instead of me just doing uh
like increasing by one or decreasing by
one i'm i have created a method called
increase which receives a number and
then if number is zero it doesn't do
anything and if number is not zero then
it actually increases by that number and
then of course if i run that it will
do the same you might have noticed that
i don't have to refresh anything
webpack does that for me automatically
so when as soon as i save something
webpack rebuilds everything and
refreshes it automatically in the
browser it's called hot loading so i
don't really have to change a single
thing while developing in react um that
is also true of you and angular if you
if you want so um
but this is not good yet so uh what i
dislike is that i can pass five to this
and maybe that's not good according to
my business logic rules so what i want
to do is i want to do it even more
correct way so i create a method called
increase which accepts no parameters and
decrease which receives no parameters so
i can only go up by one or down by one
and then when i click click one
plus i get increase when i click down i
get decrease and now i have these
methods taking care of specific business
rules which is increased by one decrease
by one so when i run this i still have
the same result but i have a much better
architecture
so what we have learned is that react
refreshes ui automatically and states
change and it is good to manipulate
state through dedicated methods
the methods which are designed to
perform a very specific well-defined
state change
good
but
what do we have at this point we have a
wall in one component where we could say
model is state we could say view is this
jsx and we could say controller is these
you know on click logic and you know
these two functions that i've created
but it's not the best can we do better
well yes we can so let's try to separate
the concerns here let's try to move the
state out of this component and let's
try to move the controller out of that
component and here
we get the help from redux have you
heard of redux have you used redux well
everybody who has heard and is not using
reader's shame on you because it's the
most beautiful framework ever
so what is redux it's they say that they
are a predictable state container for
javascript apps and what does that mean
well
here's the link it's the library for
managing application state it's
extremely popular it has a ton of
plugins i don't know why 12 000 is kind
of a magic number for everything
javascript like everything has 12 000
things out there on npm
um it's actually the only correct way to
manage state in react and it's not only
built for react you can use it with any
javascript framework you can even use it
with angular i've seen people using it
with vue even though it's kind of
i'm not sure
but yeah it can be done
let's take a look at what redux does
this is a simple
extremely simple
redux refactoring where i'm going to
start with a very very simple thing
called store this store will now move
state out of my component and let's take
a look at the simplest possible shape of
store so i have a store which has state
just a number zero and i have an action
called increment action called decrement
this one returns state plus one this one
returns state by minus one and if
anybody calls this function with
anything else but any of these two i
return state whatever it was before and
then i create this store and then i can
bind my component to that store so this
is where redux would start
what are the redux principles first is
the state is centralized there is one
single central state store for the
entire application one and only one
this state is immutable you cannot make
changes to it this is
true about any react state you don't
mutate
this dot state dot counter plus plus
that's bad we know that already and
redux just builds on top of that
state changes are only possible through
functions called reducers let's not go
into why they are called that way there
is a reason
and
another strict principle is that data
flow is strictly unidirectional it
cannot flow in both directions like it
does with vue which is something that i
don't like one of the reasons why i'm
not too happy with it but anyway
let's take a look at
some terminology state is application
data store is the state container store
simply contains state reducers are
functions which manipulate that data and
actions are functions that indicate
intent to change
data or to invoke some kind of state
change and this is this
unidirectionality state defines user
interface actually user interface is
built from state user interface will
trigger actions actions will
invoke reducers reducers will update the
state and state will then refresh in
sorry reducers will up to this store
store will update the state and it will
it is one circle which always goes in
this one direction
um this is the actual flow uh we have
this user interface and then the user
clicks a button and then what happens
you know it triggers an action creator
which
dispatches an action in a store and then
that store sends that action to a
reducer and then reducer executes its
logic returns the new state back to the
store and then store updates the ui if
necessary
good
let's take a look inside of every redux
action
let's imagine that we have a payload
every action has a payload this is
something that we send into the action
like for example to do sleep we send
this to an action creator which turns
that into an actual action so this
action will receive this type which is
the critical component and it will have
this payload action creator can modify
the payload it can add more more things
like default state maybe if it's not
passed into it and then when we have
this action it sends this action into
the store and store then dispatches it
to all reducers
inside of each reducer
store will send actual state
and action
and then reducer will first have to
check is this action for me at all
and if the action is not for that
reducer then it just returns the state
the original state and if this action is
actually intended for me then i
do manipulation
and i return a new state
and this state must not be mutated
directly from the original one if let's
say original state was to do i cannot
say like state dot to do and then set
something else it has to be a new
instance of an object which is typically
a copy of the original state with some
manipulation done on top of that
reducers must be pure functions they
cannot have any side effects they cannot
mutate anything they can only operate on
state they receive and they must return
some state uh some new state or the
original state that is true of redux in
its originally intended for there are
variations of redux which allow
something that looks like direct state
manipulation but it's not and that's why
i dislike it
actually
what happens then
once reducer has completed its job it
returns the result which is either new
state or old state over to the store
store runs the comparison did the state
actually change if the chain is if state
all state equals result it means nothing
change then we do nothing if state
changed which means result is different
from known state then it simply triggers
bindings which in the end results in the
ui being updated so um let's take a look
at that i'm just quickly going to run
through a couple of demos before i jump
to our
simpler demo with with redux
so i'm going to
wire up this counter with redux so here
i have my reducer function it receives
state which is default zero it receives
action action can be any of these two
and then if this one then plus if that
one then minus otherwise state that's it
it doesn't mutate well it's difficult to
mutate an integer or actually a number
value directly but if it gets more
complicated we will see see it soon we
will not be doing any state mutations
and then my counter
actually is not just my counter
component you can see it does not have
any state anymore i have taken all that
out it doesn't belong here this is just
let's say view if you really want talk
mvc or mvp
it is just the view part and what i have
here is binding
where i'm binding
my component
to the counter state and for that
binding i'm using this map state to
props which is the function which says
when it receives state whatever current
application state is it exposes it as a
property called counter on whichever
object is bound to this piece of state
so when i go back to my
counter component it will have property
called this props counter
also when i click plus or minus it will
call props increase or props decrease
which is nothing but actions
so i will have action increase action
decrease with this map dispatch to props
i'm mapping these two
into
um into props object of whichever
component binds them and this is my
action creators they receive no
arguments
and they simply dispatch
the increase action increase action
sends this payload or actually action
over to every reducer this will trigger
my reducer function reducer function
will check if it's for them or not and
will execute its logic so when i refresh
that it is still
the same stuff just very very nice
completely detached concerns completely
separated
i can do that not only with single state
i can combine multiple different
reducers so what i can do is i can have
situations such as this where i have to
do's
stop talking
start closing the session
down
drink
beer
later and then i can you know click this
and this and then it updates uh that
summary so
these leave as two separate states
and
they actually live as two separate state
objects i have counter state
here i have counter reducer i have to do
state and to do reducer
and each of them handles a separate
chunk of my overall application state
and then i have store which actually
combines these two
into a single reducer so i have a
hierarchy of reducers which allows me to
have reducers every reducer function be
concerned only of the subset of state
and my store will then be able to notify
only the necessary reducer
when a
change happens on a subset of a store
and it knows that based on actions it
knows which one to call and when and it
also knows which subsets of state to map
to each of those reducers so
i also have a more optimal version of
that where i'm binding really smallest
tiniest possible chunks of user
interface to smallest possible chunks of
space to get the most optimum possible
rendering and for that i have actually
my
um
sorry i'm going to
open my debug console and then i'm going
to clear my debug console and i'm going
to refresh this and you can see that
okay now everything rendered so all of
them just indicated that they rendered
themselves but if i click this plus
only the counter label has re-rendered i
didn't re-render the entire component
which contains quite a lot of dom
i just updated this single
component and again just that one when i
added to do like
or 12 it has updated three of them
but now if i tick that off as completed
it has updated just this entry to
indicate that it's crossed over and it
has updated this
one
of one not both of them not the entire
label just one single small
part this is how far you can get with
redux to optimize the
what kind of ui updates you get from
what kinds of
state changes this is really amazingly
beautiful and now let's take
a look at how we can put it together at
work with simpler with our demo so we
have our component tree in into which we
will inject
the store and reducer we will have only
one reducer because we only have one
kind of state and
this store will then dispatch or
actually map specific parts of substate
to each specific component so the
hierarchy doesn't matter anymore the
hierarchy is just ui hierarchy so that i
know where
something is rendered from but which
component refreshes does not depend on
that harkey it actually depends on the
state and the actual state that is bound
to actual component by redux at runtime
also when i click data entry
i will i will
mark this selection i will dispatch a
specific action to the reducer reducer
will that then update the store and
store will then update the necessary
components only those that really need
to be notified of that change so i can
go and take a look at
that just before i do i forgot to to
show you one very interesting thing
um
and allow me that please uh why i
absolutely love redux is because of
redux development tools so let's just do
this like this and then let's add to do
stop now
12 minutes to go
and then i will click this one and this
one and then this one again and then i
will go to redux tools
and then i will say okay i want to see
those changes as they happened in the
past
so it can replay
it can time travel
it actually notices every single change
implementing undo is like
15 seconds in redux
it's just beautiful you can save this
state out as json you can load status
json you can ship the state over to
debug department or
imagine like your customer happens to
have a problem like you detect the
problem you take the redux stage just
ship that together with everything to
your developer he can get the same state
that the user have at the pullman moment
of error beautiful so this is something
that redux gives you just out of the box
let's take a look at how we combine this
with our component
so here i have
one workspace which is react
one workspace which is al i'm going to
go into my redux folder i'm going to go
into reducer function and i'm going to
set breakpoint on state change
and then of course i'm going to run my
uh
i have to open
an al file if i want to run al
so i'm now
deploying the component over to bc
then i have to go to debug i have to
start
so i don't care about this one i care
about chrome bc so i'm attaching chrome
to running bc instance
i get this
i sign in
i will click
here
and then see
my breakpoint hits i'm in my reducer i
can inspect everything i can really
debug through all my original javascript
code regardless of the fact that i have
very uglified bundle running out there
in business central
so that's uh
that's how easy it is to to bind these
things together with all the tools that
i have presented and then one last final
touch i'm going to do and present
a way to mock this entire business
central web client so that your
developers
and sometimes like i know companies that
have web department who is in charge of
developing for web and then you know
they always have difficulties talking to
al department which is in charge of fail
code so it's always difficult to know
exactly what will they ship how do you
really bind it up and wire it up all
together with the controller then so
let's take a look at what i've done here
so i have
a folder
which i call bc mock and this also goes
on my blog
it's actually already in github just my
private repository as soon as i you know
document it up together that i'm happy
that it's in in good shape it goes out
here i have this mock folder where i'm
mocking business central and i'm mocking
absolutely everything i'm mocking al
compiler i'm mocking page runtime i'm
mocking the microsoft dynamics nav
framework
components in in javascript absolutely
everything
because i want to have exactly the same
experience i even have busy state change
mock so that you can see how the
component will see that state has
changed absolutely everything and i even
mock the look and feel so when i run
this
of course i first have to deploy this to
business central
actually i didn't have to i can just go
to react
and i can re run this part and then your
web developers will see
yeah wake up wakey wakey
come on
let's stop
um let's go to this let's compile so
whatever
this should work now
okay i will just run i will close
this i will run it again
okay my tasks are wiring up
when web back is up and running i will
stop
actually i will skip over to okay
everything should be fine the bug
console is empty so let's see
it should work
yeah
so it looks like a page in business
central as much as necessary and yes you
can just keep developing
so
everything that a web developer does
will behave exactly the same way with
business central they can even mock the
latency of the network to see what it
would look like on a slower network so
this is like a
free gift for me to community this year
just something that i've been playing
with recently so um
i hope you will like it when when it's
out there published on github
and
yes
that's it
uh tomorrow do not miss waldos in my
session
uh we will be talking not about control
of this but there will be quite some
react there
there will be uh integrations with uh
with apis in in business central so uh
this session is going to be tomorrow at
11 a.m absolutely do not miss and we
will have a killer demo there really a
killer demo so that's it
thank you
now we have
the traditional t-shirt giveaway and mic
throwaway
stage so i have to throw this to you
okay
works works awesome works thank you for
the session first of all and
apart from that how do you see
testability when it comes to ci cd
processors how do you get these things
aligned
i see it like pretty nicely
[Laughter]
so thing is i actually wanted to show
that here
and i couldn't i actually wanted to show
view i wanted to show angular and then
when i went you know my original ideas
changed so um
testability taps nicely into that redux
is highly testable react is highly
testable there are frameworks for
javascript testing that you can tap into
uh ci cd like devops
ci cd just as you can tap
business central or
extension deployments through through
devops so
anything you can imagine any kind of the
stability it will it will just be nice
what will be a problem is how do you
really make sure that uh
you are testing the actual integration
when stuff is coming from business
central to javascript and what goes back
well you can you can use the mock so
this mock can be used for tests that's
one of the reasons why i developed it so
you can put it in there it will actually
simulate the entire working of
the
nsd and web service and al
infrastructure so yep perfect deserve
this shirt thank you you're welcome
anybody else don't be too far
thank you for another nice session thank
you um in the past you also used uh
control add-ins to uh
enter to enrich the
ui okay with components and you can also
use
local resources like serial
communication and stuff to
integrate the
local resources into the ui
there are various cloud solutions and in
the cloud you have to but is there also
is a way to
connect local resources in your
ui
fully on-premise so you don't need any
services one word and it's a crucial
word i didn't catch integrate what
sources local resources like resources
yeah like a serial report or something
okay that kind of stuff
well
you can do that it's possible like um
you could you could
yeah there are there are things you
could do with uh
what are they called
the name is escaping me yeah web
oh crap
not not web services uh
web something
yeah the name is just escaping me you
can call tcp from web to talk directly
to uh to processes which are running on
on your machine so if it's the same
source
then browsers today will allow you to
actually place those kinds of calls so
they are similar to rest they are just
not rest so they are different layers
separately they don't go through course
rules which are limiting your
possibilities they're actually allowing
you to access any kind of locally
running service that you have on your
machine so you could do that you could
expose a service which runs as a like an
application in windows that exposes a
tcp port which will listen to
invocations which are exactly the same
as rest so it will accept accept rest
calls it's not called web hooks it's
web sockets crap yes web sockets thank
you thank you
so websockets can can do that for you
okay thank you
come on
we have two more minutes
okay there's a question
careful i almost killed the person two
years ago sir
uh have you tried some uh azure builds
for
azure uh i mean uh in pipelines yeah of
course you can yes you can use azure
pipelines you can integrate devops with
this do you have something uh
i myself do not so
my problem is you know i see devops as
infrastructure
and i try to let other people's handle
other people handle infrastructure so i
myself you know i will prepare test
stuff and code but i will not set up
pipelines so
i know that it can be done it's just not
i'm not the person who can tell you
exactly what and how to do that i let
infrastructure people handle that so
yeah but yes a good question
and
give me my mic back
yep
i'm a geek i'm a developer you know i
just don't want to set up
those kinds of tasks anything else come
on one more minute yeah
oops sorry peter uh
when do detach uh this
web app from business center element to
integrate into business central let's
say for warehousing i don't know yeah uh
that's a good question in my view
everything that can be detached should
be detached so you shouldn't really be
putting too much into control again if
you can build a separate interface that
talks using api with business central
then that's a preferable way to handle
it come to our session tomorrow we'll
talk about that so
you know
when you want to be inside business
central
i would say
these are the situations when you
actually want to have full access to
business central flow like for example
click a button and it runs a lookup
page with items and then you want to
select an item and return it back over
to your controller then immediately so
that's something which is more
complicated when you completely detach
and it's much easier if it's integrated
together with within a controller then
that talks directly to business central
rather than through api but i i should
say like uh it all depends on your
scenarios both are possible both are
viable i have shown one approach here
i'll show another approach tomorrow or
waldo and i thank you
molly
one more question yeah we have 22
seconds i will give you more
they stole time for me in the beginning
have you talked to
the microsoft ao people about making the
product compiler more friendly and aware
of
non-al code and vs
code
well so the very theoretical question i
think well i mean have you talked to
them about that because i mean you yeah
you said it basically they tried to
compile all the als yeah well you know i
can complain about that i can actually
raise issues on git
but i cannot tell you when they will fix
that i do have complaint right no i have
complained in the past they listened
they didn't listen so yeah and i will
complain in the future and they will
listen and they will not listen so it's
you know they listen it's not that they
don't they actually listen very much
it's just you know they have their
budgets and scopes and customers to
support so yeah you know ale compiler
and how nicely it plays with nodes it's
not really you get you learn how to to
live with that and yeah so
look at this
waiting for you come on
no
really
okay go
thank you very much once again and see
you around
you
