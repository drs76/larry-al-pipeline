# NAV TechDays 2018 - Evolution of a titan: a look at the development of NAV from an MVP angle

- **Source:** https://www.youtube.com/watch?v=KnUomsA_4Jk
- **Video ID:** KnUomsA_4Jk
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 95m44s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

good afternoon wow that was a good start
how are you enjoying enough take days
alright hopefully really good cool so
welcome to our session one of the most
unclear titles I guess that you could
think of I'm Eric Walters from Belgium
this is a vehicles of Babbage and
actually we are not that we are all the
wimpy echo so what we will be doing so
excuse me
Walden vehicle but it says VA Cohen
Waldo yeah why do you have to be first
like it it doesn't make any sense that
you are first so yeah let me introduce
this session because my name is first on
the slide so welcome to this session
called evolution of a Titan a look at
the development of nav at from an MVP
angle so what we are going to talk about
today has so V a go yep what's this year
I don't have a clue piano yeah looks
like I can press keys come on yeah look
cool come on didn't do something
[Music]
better
[Music]
well obviously we can still do a little
bit of that so as you might have guessed
I need that thing over there we are we
are too old and grumpy guys that will
just take a funny look from the balcony
yet what has happened over the past 15
years and where it has led us to and
then where we will go so you might know
these two guys they are Waldorf and
Statler from a pet show and that's it
should at least be well fine with me
then okay no no no that guy's dead ler
that's dead ler but that's not all just
continue on no one cares
okay well good let's get let's cut the
crap so let me start with this if you
don't have a problem you don't need a
solution so all of the development of
nav or business central or if you want
that has happened in the past has been a
reaction to some kind of a problem so
when it all started 25 years ago these
are 25 35 years Wow 35 years ago this is
what it looked like and the problem that
this thing tried to solve is let me
handle my business processes as a single
person and then as soon as that problem
was solved another problem came along so
how to get more people in the system and
then in 1987 navigator came along and
then as that system came along there
were more problems how to get even more
people to the system how to integrate
with other system how to provide better
performance how to allow web services
there was a number and number of
problems and as we went along more
problems came along and we had to solve
more problems so out of all the things
that happened in past 35 years and
especially in the past 15 years where
things really kicked off after Microsoft
took over I would like to bring these
kind of holy grails
to our attention there were things like
for example how to provide
world-class scalability that was
something that was but that was a
barrier hardly to be broken for years
Microsoft was trying to kind of get more
people to the system
remember all those days when you know
pushing more than 50 people really hurt
anybody who hadn't hundred people it was
like wow a crazy implementation there
was stories told about implementations
with 250 people and stuff like that
today nobody asks that question anymore
you don't think
can I put like this number of people on
the system or not architecture just
scales well when you think of cloud you
don't ask like what kind of cloud
architecture do I have to have in fact
so if we take a look at architectural II
what happened
overall all this time we started with a
single tier then we went to two tier
where we had a client and the database
from that we went to a three tier
architecture but today barely anyone is
talking about architectures because what
we have on one end is clients and then
on another end we have this big cloud of
things that is just connecting all of
that together and this is our
architecture so it's not a real
architecture it's really clients
connecting to a cloud of different kinds
of services exactly and oh a cloud of
things is a nice way to put it
I call it technologies and we've got a
lot of technologies actually that we can
think of that actually connects with our
environment our life as developer so we
are not going to bore you these 90
minutes we're talking about all of them
so we picked what we think influences
our life as a developer in this time
future let's say so going forward it's a
good way to look into the roadmap let's
say so if we look in the roadmap and we
look in the future I think I just want
to focus on one thing for now that's
this thing modern clients what does that
mean I mean we have clients
they are quite modern even new clients
so modern clients in 2020 where does
that mean well actually from all the
collection of quite nice looking cool
clients that we have been using in in in
the past only the modern clients will
survive the modern phone client modern
type enquire into modern sorry but if I
just may interrupt again again modern
modern what does it even mean motor if
you think of any of those client that we
have seen all of them have been
considered modern nobody was releasing a
new release of an old-fashioned client
was just you know here's a new modern
client so modern let me show you what
morning so I just want to show you what
I think is a modern client so I'm going
to connect my local instance to a modern
client wow this is pretty modern as far
as I so let me try to see like what my
customer list oh I see I clicked on
orders well let me let me try to what
was that yeah I want to go to sales
source and then maybe click on this one
and try to post that one or yeah so you
know if you ask me why doesn't it work I
need to post if you ask me very nice
very nice but I have no clue how well
how I did that it's JavaScript obviously
so but still this is cool to show yep
but on the other hand is this function I
don't think so do you have anything
function that you can do with it
something really useful when you think
of modern clients and we are all afraid
of going to Monica line through one
simple thing I think it being shortcuts
we are not able to use shortcuts anymore
come on come on
so shortcuts shortcuts like for example
post post so sales orders this is
obviously the real modem client so I'm
opening a sales order here and what is
this posting right now this is what I'm
going to press f9 on my keyboard and is
that what you're looking for that's what
I'm good really good nice so just like
that cancel that and then let me let me
try to see what f8 does nothing let's
make f8 do something shall we good so
here I have a little solution where I
have show shortcut listener and then in
this page I will subscribe f8 to an
event and then let my JavaScript take
care of the rest room publishing this
and with this published
I'm closing the browser I want to do I
can do it from the browser too but I
want to show that it works in the client
so I'm going to sales orders and I'm
going to and sorry
this is the universal plan yeah so what
I bound my action to is these shipments
in here and then I'm going to press f8
to run that shipments page so is that
useful is that useful good I think so ok
good so yep before you get too excited
about this you will get a source code of
that I I did a little cheating not much
just a little bit and Microsoft would
hate me for what I'm about to say but I
did I wouldn't have to do any cheating
at all in this demo if the
architecture of the AL code was correct
so unfortunately all of that code that
runs when you press f9 or f8 or click
those actions is on action triggers in
pages where Microsoft is saying do not
put your code in pages and yet they put
their code in pages when that code is
off pages then we will be able to just
do not no tricks here until then this
works with just you know little bit of
tricks so let's talk a little bit about
JavaScript my obviously my suggestion
would be that if you want to invest in
one single piece of technology or one
language new language that can really
boost your development then you should
go with yeah I'll try to stay here so
powerful javascript is a powerful
language it really allows us a lot of
things you have seen that using
javascript i have been able to hijack
the entire client i have full control of
the user interface i can really do
anything that i imagined when we think
of control agents which is where
javascript lives then we typically think
think of things like this so for example
i will go to yeah even escape doesn't
work there i'll fix that remind me to
fix the scape ok so I will go to
customers and here I have my customer
list and I want to rate my customers
with stars so this customer is obviously
a great customer and but it's lousy at
payments and then this what is happening
this is happening yeah yeah so let me
rate this customer like that and then
let me prove that it's really yeah it
does remember so this is an example of a
controller then that people have in mind
when talking control things in
JavaScript but obviously it doesn't have
to be that it can be a lot lot more
however you know javascript is not a
language that we are all used to it's
vastly different from from most
languages that we have seen so let me
just
quickly prove that I have my node.js
environment here and let me just do some
simple tests like for example any
language would pass that test right one
equals one that's obviously true right
but in JavaScript for some reason this
is also true well it makes sense
obviously yeah one those quotation mark
whatever but what if I try that yeah
that's true for most C based languages
that will be true but what if I do this
will that be true
well that's true as well so that means
that I should be able to do this as well
well that's obviously false does it make
sense right so sometimes not all things
in life make sense that's not all let me
show a little bit more about JavaScript
so obviously we know that now we know
that this is true so it means that if I
do if I sorry that this is false if I do
true then I print true obviously if I
put false in there then this will not
print but if I print sorry if I print
that true which we know is not equal to
true that will still be true so let's
take a look at a little more so I
absolutely love this one so Waldo I put
you in and erase it's fine with you yeah
fine good this is true but if I put
Waldo in to erase this is obviously
false right it just makes sense right
well in JavaScript we have this concept
of truthy and falsy and you just have to
live with that this is just one of the
quirks of the language eventually get
used to that
but even though it's a very crazy
language it's also a very powerful
language so let's just take a look at
what else can we do with that language
so I'm going back to my real modern
client unfortunately this one and I've
always but
always wondered why in the web client we
have this user icon in the upper right
corner if we cannot change that so I
just decided to make it possible to
click that icon and then on click of
this icon it starts a webcam and then
takes a picture of me so I for example I
will now take a picture it didn't
succeed so because you pushed me so let
me know yeah so I will take a picture of
me and so that's just an example of how
I would like this to work so yeah well I
will cancel that now I have my picture
already and to prove that there no you
know smoke and mirrors I will just
restart the session and it shows picture
out there so these are things that
JavaScript as a language can really do
for you so I would there saying that
after al JavaScript or addition of
JavaScript to nav technology stack is
the number one thing that has happened
to us because if anything can open up
horizons it's JavaScript and this work I
also have some you know dreams like what
I would love to see in the future
unfortunately currently when we are
working with the universal client on
Windows we are using Internet Explorer
down there so Microsoft has given up on
Internet Explorer how many six years ago
something like that and yet we are
confined to that thing I know why is
that like that but I hope that
eventually we get rid of that so we can
get access to for example ACMA script 6
also what I would like to have is I
would like to have callbacks that when
JavaScript completes the work that al
gets a call back that JavaScript is done
that will allow us a lot of different
things and one thing that I would
definitely love to have is a permanent
JavaScript layer so a piece of
JavaScript layer that we can always call
from al rather than having to put our
crazy controller needs in there to be
able to communicate why why do I think
it's good
because if you think of if you think of
crazy people like for example me I do
these crazy things like color the client
in pink colors and put the icons of
Muppet Show
because if customer asks for that and if
that's possible we will make it possible
we will make it work we'll break all the
barriers we will break the rules just to
achieve that thing and wouldn't it be
better that if we we have a nice piece
of architecture behind that allows us to
do that without having to pull the
entries this is what I'm calling for and
what I'm hoping for
so you did now quite some rambling on
your baby
I got a baby as well you get baby yeah
Power Cell power show come on power
partial power shall ever done for us you
cannot mean that it did some
simplifications on installation
installation okay installation for merge
and comparison like object merge and
yeah okay but I don't care the developer
like administration part I've ministry
okay I give you that but that's what
Marshall is for administration that's my
point okay but for deployment like
deploying your objects your don't pay
okay well good deployment fine
security security okay but apart from
installation comparison and merge
administration deployment and security
what has powerful PowerShell over 10
times real PowerShell does a lot for us
except from these and backups and
upgrades it does crapload for us a lot
more as the boxes that you see here I
did nothing
some of them are fake but a lot of them
are not fake and PowerShell does a lot
for us in terms of nav development so if
we go back for a minute in time a tune
of 20 13 enough 2013 gave us quite some
possibilities with PowerShell this was
actually our first baby steps baby steps
into PowerShell and the connection with
we had some administration parts but it
could be good update settings from the
server and stuff like that we could even
publish web service we can still do that
we could do stuff with companies the
worrying about oh but now uses that are
not used is from nav we'll be able to
yeah that's all possible enough 2013
Microsoft put time in to merge tools we
were able to upgrade automate upgrades
with PowerShell and I hope a lot of you
are using that possibility because it
immensely immense help in the upgrade
process and obviously also language
management it was thanks thanks to
powershell that i came to the conclusion
that i need to translate about 12,000
captions in my solutions anyway on top
of that but what do we do
currently i think a lot more still now
we have docker we have yeah obviously
the entire upgrade process and we have
look at that source code analysis
interesting how can we do source code
analysis with with powershell well i
would like to go a little bit deeper in
that to be honest so i don't know if you
know it but there is a dll somewhere in
the client folder
it's called Microsoft Dynamics NAV top
model table tools don't do well actually
on the slide again it's a fake so what
does this do well actually this is what
Microsoft created it builds actually an
object model from the text files that
you are exporting from CEO to be able to
merge so this is actually the merge to
the bird the binaries let's say of the
merge tool that we are using in
PowerShell yeah so I got this clever
developer in in my company and he said
so what he did it applied some magic he
did actually wrap around this dll
because what Microsoft already does we
don't
to do anymore if we can build already an
object model from the text file maybe we
can build our own object model from
whatever text is in the text file being
the code right because that's Microsoft
doesn't do Microsoft does not build an
object model from from the code itself
so he did that and basically now we are
able to make that available in
PowerShell to make actually code
analysis available in PowerShell which
is useful in build scripts just imagine
that you upload your code in in source
control you could check the code so let
me try to I even have it showing it I
will going to show something that's my
PC so let me show you a few bits and
pieces that is PowerShell I see I
personally do not use PowerShell IC
anymore you can see that the reason why
I still use it is I wanted to show you
this progress bar this is something that
Fiasco doesn't show what I'm doing now
I'm actually using it DLL that we
created which is that wrapper around
this model dot tools and this is the DLL
that is just using this import of the
text file building ad object model
that's actually the first two bars and
the second and third bar is actually the
where use that's something that we built
on top of that object model actually
going to use and map the references and
in the background we are filling this
variable it's quite a variable let me
show you memory at this moment
PowerShell is using two gigabyte over
130 megabyte file so it is quite a model
in the background I must say in memory
but the thing is all references are
there so from code the variable encoded
the variable amusing in code refers to
some kind of type refers to - yes let's
say the customer table which is used in
code anywhere else or all these
references in the entire path
can be tracked in thanks to this model
let's see if we can have some examples I
have a few you see so this model
variable here the nice thing is now that
is something you can really understand
so you see here for instance there are
nav objective laboratory in text cool
and in this text files I maybe can count
the amount of variables sorry objects
five thousand eight hundred and seven is
the screen big enough so five times
eight hundred objects in this text file
what the tool also does is going to make
this an understandable object model so
that you can actually read it and refer
to it by key so this film name is
actually a key a key to a specific
symbol within the text file and you see
we've got some symbols let's just take
Coach unit eighty here I simply going to
filter on object type object ID and in
that case my variable C u8e should be
only one code I can check that and yes
code unit sales so this is kind of an a
key I can refer to I can work with to
refer to whatever I can't count the
number of procedures about three hundred
functions in code unit eighty and I'm
already doing some kind of analysis
we're ten Alice's counting procedure
still the code unit with 300 procedures
something you should question have
questions with in my opinion the
variables there are 144 variables no
there are 144 global variables again a
question you should ask yourself the
code and I'm checking in here do I want
this right so this is why I want this in
PowerShell check the code and check it
if I want this in my
my products so I'm going to skip a few
because VA goes really
so you see here from the 20th procedure
I can go into the local variables and
this is cyclomatic complexity so during
this code analysis obviously a nice
thing to see is how complex is Michael's
not a way to measure that is the the
quantities of yeah and ifs and repeats
and cases you are building so number of
apes if you have five ifs
I'm bad at ifs yeah it is quite complex
so the complexity is added by one and
basically you just count the number of
waves cases repeats with these kind of
statements right and that's also what we
did so by this this dll I know that
there are two hundred and ninety four
that's not very interesting but an
average of a complexity of two point
seven and you can measure that now you
can measure your two complexity of your
code and have a threshold and if a
certain procedure on a certain code unit
is too complex you can refuse that this
code analysis is done by code model this
so this is the part that is new and that
is actually done quite simply by not
simple I shouldn't say that because I
didn't do that it was that magic
developed that is that but it's going to
take every word out of that and map it
and if it's not able to map it well then
another problem so we kept on building
on top of that so that we could map
every single word in in a code line and
a map it can be a statement and mapping
can be a variable or any kind of
something that it already know so if you
see here here you see that we have
spaces new lines and stuff all
characters and words are being mapped
including the if so if you going to
measure that you see that there are two
ifs or repeats in this
piece of code of the first procedure and
that's how we basically am building to
complexity where we can add on top of
that so if the base model is there you
see here that we do other stuff by the
way like publishers and missing elements
so is if the base stuff is there we can
create scripts in PowerShell obviously
to build yet another information kind of
thing that that shows us let me quickly
run this shows us an analysis of command
of code complexity in this case of the
first 1000 objects so you see here right
away my most complex functions not my
most complex for instance these are
Microsoft's most complex complex
functions in in the first 1000 objects
right you can see here from 1000 objects
an average of 1 which is quite fine so
the average is really good and so on
commit another thing that you might want
to analyze I want to have commits yeah
because you like to cut the fingers of
your so this is a kind of analysis i i i
tend to like and let me zoom in that for
a bit so just to go over them there are
one more than 1,000 commits in
microsoft's code spread over more than
almost 900 functions 14 of them are in
comment and 22 have a comment
so they explain 22 commits like don't
explain all the then type ok you might
wonder why do we have this we are
talking about evolution we're talking
about going forward the future and
you're talking about CL okay point taken
my point to myself this is an example
where we use the model to go forward to
try to build tables
that are in Elle but don't have any
coach makes a lot of sense believe you
mean this is a good opportunity this al
conversion do not convert but to
refactor and one good way to refactor is
to rewrite your code thing is rewriting
code shouldn't be rewriting your tables
right so in a way it should be nice that
you could export your tables without
code and then convert them to two al
so what we did is do it the other way
around he analyzed our code we built
some kind of function print nav table
which is going to produce al files this
is the function that produces the AL
files based on tables so what I will do
here is I will take tables that start
with cost which is the customer ledger
entries right so if I execute this here
is that was not fake I can redo this
back today I do don't fake I don't do
fake so you see that it's just actually
printing to Texas is completely off but
we don't care obviously because we have
this Auto formatting thing for us so
empty table this is this table is full
of code or might be full of code I don't
I don't know I just take the pieces that
I want and put that into a new elf I'll
take the properties that I wanted even
convert the caption ml to caption and
basically go from there and now I have
my basic tables already I can start
pulling the code one by one in that I
alright
what is this back so that was code
analysis there was another one on this
slide that is darker darker I hope you
heard of dog
well I know that you were not an
infrastructure guy but actually when we
talk about talker we talk about
infrastructure and in a lot of cases we
as developers are confronted with
infrastructure we need to build up
development environments and the way
that via KHOU does it well he does a lot
of manual things I'm a coder right so I
have seen him work I've even seen him
sweat one hour before this session
sweating wait can I tell that sweating
with vm vm his personal vm on this pc
and he just showed that demo from my
daugher free yeah
be proud of that not actually his
livestock shut up so he spins up a new
docker or a new vm a new entirely new vm
installs nav and start coding money he
needs a new version the same thing and
this is not this doesn't take two
minutes just take 10 minutes a lot of
manual clicking now I simplified myself
a little bit I can simplify myself so
what I did
you know what the problem is
what's my problem I talk too high talk
install nap
so I had a script here so I have a
script here that basically helps me
install math and this is just a quiet
install of over DVD so I was in back in
the days still very relying on the DVDs
that that we got and downloaded yeah the
download takes time and you all you know
the pain the pain that Shaco still goes
through every single what are you
thinking because at these days we have
dollar doaker simplify stuff now let's
dive a little bit in a little bit into
docker docker is a VM not a VM we have
just a part of a VM it's going to start
an isolated whatever p.m. it's called
him but it's going to use your kernel of
your host so it's going to reuse stuff
which we'd use size which basically
increases in boost performance so
basically meaning dog is fast and
efficient it is isolated
I like isolated I mean I was working
with VMs because of the isolation so I
like the isolation part and now we can
isolate in a more efficient way
thanks to dr. so it is actually your
solution for having multiple versions of
nav simply installed next to your
development environment yeah so this is
definitely a solution for developers you
can focus on writing code you just need
to dive into how to work with docker
no need to worry about that we have
enough people in the community that can
help us with that I have one referral to
for DevOps for instance DevOps is this
is built we will talk a little bit on
DevOps later on in this session but
automating your your your bills
that's my machine and obviously this is
for ministry now I just wanted to show
you one thing what I'm using docker for
and how I'm using talker now this is my
daughter environment I've got three
environments
obviously I yeah obviously because I'm
using docker on a VM basically combining
two because I still do not install
docker on Windows 10 because we
understand at this point I think it's
going to improve I heard in in the
future so I might and not do that
anymore but at this point Windows 10 is
not that good with dog yet or at least
not with the contain is that Microsoft
built for us so so I want to use Windows
2016 and I can do that on my Windows 10
with the VM but that brings some
complexity because it and I want to
execute something on my docker container
I need to execute that on my Windows 10
which basically going to remote executed
on my VM which basically is going to
remote execute that on the container and
when there's feedback I or a file that
is written that I want to get back to my
laptop I need to get the entire thing
back to my laptop so there is some
complexity part of the complexity is
solved by Microsoft Freddie has created
some nice scripts factored into the nav
container help but that lives on my host
my talker host that doesn't live on my
laptop so I should still remote into my
docker host and then I would be able to
execute ready script so what I did I
build some more scripts on my laptop
that remotes at acute that - enough
container level which going to read not
execute that and I can actually simply
show you that if I switch
again that's the guy so this environment
actually this is a set of scripts that
I'm using to that I used actually for
this environment for these demos that I
will be doing on the client so I needed
to build an environment this environment
is built in docker this docker lives
somewhere on German server because
German servers are a lot cheaper than
hazard so on an urban server somewhere
in in any Kenney way that means a german
server somewhere that s windows 16 has i
need to be able to contact that talker
to be able to remote i'm working on my
laptop so i simply set up some settings
to connect to that german server which
is this one and yeah I have this one
function here that I actually execute
you see quite a lot of parameters
because in the background and also going
to set up some routing so that I can
actually access it as well but just one
instruction I can rebuild that contain
f5 five minutes this helps me a lot in
my and I can really focus on okay
so as I said there was one guy that is
going to talk a lot about docker I can
only advise to go there it's going to be
tomorrow at 1:30 p.m. and again it's
useful did I convince you well you
definitely convinced me that you can
talk but I'll try this thing docker but
still you know you use a virtual machine
and docker inside why not dr. inside
docker
well that guy can talk to so can I
dotnet seven years ago at this stage I
was preaching dotnet I was explaining to
the world how beautiful dotnet is how
beautiful our life is with dotnet I made
my career out of dotnet since then
because there was not a single session
at Tech days that I didn't mention or
use or show anything or something from
dotnet three years or two years ago when
Freddy told me we are getting rid of
dotnet from what it wasn't you called
business central back then but from nav
I said like our crazy really like you
cannot do that to us you give this
beautiful access to the beautiful
framework to us and now you're getting
taking that as taking it better away
from us and all the time what I realized
is that yeah Microsoft was really right
with taking this away so unfortunately
for for me I'm here now standing in
front of you and saying that it's time
for dotnet to be garbage collected so so
why did we even need dotnet in nav well
the first thing is we had to call
outside now
so we could not just live inside of the
CL code we needed to get out of it but
yes we did have tools for that we had
automation automation allowed allowed us
to go for those things but yes just like
that guy automation was you know slow it
was outdated it was it it came with a
lot of problems it was obvious that in a
short while it will go
out of support and we will just not be
able to use it properly especially in
64-bit scenarios and and finally when
thinking of dotnet dotnet is a part of
Windows
so whatever Windows can do dotnet can do
so it made all the sense in the world
that we just simply have access to that
environment that allows us to do
whatever we can imagine to do
and finally nav itself has been running
on dotnet anyway so we had this
beautiful access to this beautiful
powerful framework that allowed us to do
just about anything that we could
imagine so in a way it could have felt
just like sorry yeah I forgot to say
when you give access to developers to do
this beautiful environment what happens
what happens when you can use dotnet
well you use dotnet that's just obvious
so you use it because you can but it
might not be the smartest idea out there
so when talking about dotnet we have two
flavors of dotnet so the first flavor of
dotnet is c-sharp where or it can be
vb.net or f-sharp if you really hate
yourself you could really write a piece
of code in Visual Studio in language of
choice compile it into an assembly
deploy it somewhere we'll talk about
that somewhere and then consume it from
CL very good thing about that was that
there were no limitations so you could
imagine anything in dotnet you could do
it in dotnet even though there are
things which kind of don't work like
multi-threading for example it doesn't
quite work well with with CL but still
you could wrap all of that inside of
your C sharp or F sharp or vb.net
project in such a way that it works with
CL so you just did not have any
limitations you could do whatever you
could imagine however you had some
problems we'll talk about them later but
it was just
powerful the other framework sorry
flavor is what I used to call CL dotnet
because it allowed us to do whatever we
could imagine from dotnet just from CL
without having to call to any external
assemblies so we could use really just
pure CL to do anything with all of
dotnet couple of years ago I've
demonstrated here how you can have a
piece of CL code which contains c-sharp
coding string which compiles that
c-sharp loads the assembly dynamically
and then uses that assembly s dotnet
from the code so things like that were
possible so the biggest benefit of that
approach was that all code was contained
in your CL so when you take your fo bead
deploy it in another machine it was
there on that machine we didn't have to
deploy anything else so when thinking of
these two flavors and and things that
you could do when choosing what which
which approach to take it might have
felt like choosing between using a magic
wand or a lightsaber however that's not
what the real choice was between the
real choice was like would you prefer
having your fingers tucked in every door
that you close or just falling down
every staircase that you ever come
across why do I say that well let's take
a look at a little bit of code so what
I've done is in Visual Studio well I
should have opened it earlier but yeah
thankfully these days it doesn't take so
this is my performance test I just want
to test how fast this dotnet really is
and I have a very simple test I have a
for each loop can i zoom it that's a
good question this is Visual Studio not
Visual Studio code I don't know short
for that yeah glasses anyway so this is
this is my
performance test what I do here is I
create a dictionary of integer and day
time and then I have two stopwatches
I have a loop which does 5,000 things
and inside of those 5,000 things it adds
an element or or or a key value pair to
the dictionary and measures that part
using one stopwatch and then does some
complex operation and then measures the
entire loop of 5,000 these things and
this complex operation is really complex
because it's exponential it was
exponential leap slower because it for
each key in there it actually multiplies
so if you have one one if you have two
you'll have two more and there's some
calculation based on those keys it
accesses their values it accesses their
keys and everything so it doesn't do
anything useful but it allows me to
measure the speed so if I run that on my
PC here if I run a five to two tests
that it will show me that it will show
me some results it may show it will show
me that adding five five thousand
elements to the dictionary took ten
milliseconds and it took 964
milliseconds to do all of those complex
operations five thousand times I'm now
going to my virtual machine in here this
is just there because I want to
demonstrate how net behaves badly and
anyway what I have here is I have this
test c-sharp from here I'm going to
invoke this very assembly that runs this
test and prints out the result of this
perform operation just before that I
will run this perform operation from my
debug folder I will double click this
user test perform exit it will tell me
that it took three milliseconds to
process dictionary and 683 milliseconds
to process everything else and once
again this is roughly what we get three
seconds 600 milliseconds good let's try
to see what happens if I run that in my
role table client I'm going to start
that so that it's not offsetting or any
of these measurements it shouldn't but
still it's better it's up there and
running and then I will just run this
code unit I will run this each test
c-sharp to see how fast it happens here
so it took one millisecond in 500 and
some and they'll write once again just
to see and to prove that these numbers
are really roughly there so this
performance when using a dotnet assembly
from CL is roughly the same as when I'm
using it directly so those differences
can be attributed to what is what else
is happening on my machine but this is
what you get let's now try to rewrite
that all of that in CL using CL dotnet
so this is what I have I have this test
dotnet and here I will do exactly the
same thing just CL so and you know just
to be on the safe side I'm not doing it
5,000 times I'm doing it 1,000 time
times so I will run this now and let's
take a look at how much time it takes so
it took nine milliseconds to process
that the action Airy which is depending
on which measurement you take between
nine and infinitely times slower than
what it was in net and the other took
seven full seven seconds let's try to
say okay since this is exponentially
slower if I make it one and a half
thousand so just 500 more and then run
this piece of code it will take a lot
more so it will take closer to twenty
seconds I will get back to that screen
and then Google we will see how much
time it took in the meanwhile let's try
to see why is this happening so why is
CL so much slower
then c-sharp when doing exactly the same
thing
well the problem is twofold the first
one is reflection and the second one is
boxing so reflection is how when you
compile a CL code into c-sharp how that
c-sharp tyr is accessing your dotnet
variables it is not accessing them
directly it accesses them to reflection
so every single time you set a property
you invoke a method it has to get a
reference to that method from the type
then has to dynamically invoke it all of
that takes extra time and if you do it a
lot it accumulates the second one is
boxing I've used intentionally
dictionary of type integer and date/time
because that's how you do that in
c-sharp in CL you cannot do that you can
always ever declare a dictionary of type
object object which means whatever you
put in there will have to be boxed and
then unboxed so accessing any of the
information there again takes extra time
this has been a little bit improved in
al so al does not do reflection L truly
wraps that and if I ran that in Al it
would be slightly faster but it would
still suffer from this boxing problem
because it still when using dotnet
variables it uses exactly the same
principle it allows you to create just
objects instead of actual types so in
the meanwhile let me just take a look
how much time it took it took 13 seconds
or is it 13 yeah it would have taken
three minutes for 5000 I measure that I
just don't want to bother you with that
so obviously obviously we cannot do it
this way so the way to go with dotnet
obviously is to put stuff in c-sharp if
you really want to retain that
performance however when we are doing it
in c-sharp we have another problem we
have to deploy that assembly to all of
the machines that will use that and then
how can we do that well we can deploy it
physically on the server or we can put
it in the database which is simpler to
perform because when you put it on a
server when you need to you need to stop
the service tier who have to deploy
there in the
then you have to restart the service
here every single time that you do a
small exchange so when you put it in the
database if you update you just deploy a
new resource dot zip into into database
and it works except that it is not
really like that
so let's actually take a look at this
database deployment so in here I'm first
going to stop my service here so it's
now dead and then I will take rid of my
assembly from here yep now it's gone
so my service here is restart it stopped
I will start it again
I should have restarted it I don't know
why I didn't and then when it starts I
will start my RTC my modern client not
and then I will first prove that the DLL
was not there that I'm not accessing
that there are no smoke and mirrors and
then I'm just going to deploy to the
database because that's the way to go
that's at least what Microsoft says is
the way to go so let me let my modern
client come back to life
because I will have to do two more
restarts prove my point
that's because of docker we trust you it
works it works yeah okay so first when
my client is up I will run this again
sorry not this I will run that thing
again c-sharp just to prove that my
assembly is not there it will fail okay
did I just start another client session
would be I will run this once again
there it says that it cannot create an
instance because it doesn't have access
to the assembly so I'm now going to
deploy this assembly to the database so
just so that I can run that piece of
code so I will do I will go to control
it ends I will create a new entry called
perf test it has versions one zero zero
two and it's not net interrupt time and
here I will just import that resource
that's it I will take this one so I'm
sorry
the zip and then I will just run my test
to make sure that this is running fine
and there we go it has just been
consumed from the database it has run
its test and everything is fine in
hunky-dory until I need to do a change
I've noticed that this measurement has a
bug so I want to fix that bug and since
I'm not breaking any signatures I'm not
doing any breaking changes I'm simply
fixing a bug I'm not increasing the
assembly version I'm increasing the file
version because that's the best practice
in the dotnet world and unless you're
doing a breaking change unless you are
touching signatures or the number of
objects available you don't change the
assembly version you change the file
version so let me just prove you that
that the best best practice here I have
my original
project I now just want to update this
earth test DLL which is version C which
is version assembly version one zero
zero two
but file version one zero zero three so
sorry file version also one zero zero
two I will replace it with file version
one zero zero three
so I'm going to my sorry
it's in here but I just did not create a
shortcut so I'm taking my file version
one zero zero three which is still
assembly version zero zero two so
obviously this is zero zero three I'm
taking it and just patching my piece of
software with a new version of the
assembly since I didn't break anything
since I didn't change the assembly
version it can still run this one that
depends on that assembly however I can
see here that it's version zero zero
three responding so let me now deploy
this one zero zero three to the database
so that I can use it from the database
good so since the assembly version
didn't change I will just go in here and
I will use this one so I will just go
and I will import version one zero zero
three and then let me restart my test to
see that it's still the old version
responding there is no version tag in
there good
then obviously I need to restart the
service tier so let me restart the
service tier so we start the service
tier ok my session is dead so it's now
running again let me run my client again
hopefully it takes a little more time to
wake up this time
actually let me just cut to the chase
let me just simply tell you what will
happen because we are shortly running on
time and for some reason my daugher is
not working well that's a good joke
thank you what will happen is that
nothing will happen I will still have
the old version responding because
Microsoft has decided that file versions
don't matter that the only version you
can ever deploy an assembly with is the
Assembly version and they tell you well
increase your Assembly version that's
fine I will increase my Assembly version
but then I have to recompile all of my
CL code and redeploy all of my CL code
because updating Assembly version is a
breaking change but I will do it however
what if I for some reason just like you
Microsoft use JSON dotnet which follows
the best practice in the dotnet world
and does not touch the Assembly version
not to introduce bracing breaking
changes they simply update the file
version where they want to fix a bug
what if I want to use their assembly how
do I get their assembly to deploy on NST
the answer is there is no way so once
you deploy a file with a single assembly
version you are cemented not pertinent
but per machine not very nasty but per
machine you can have multiple NST
instances you can have multiple tenants
all of them will be condemned to use one
single version without the possibility
to upgrade in any possible way but
hacking you will have to stop everything
then you would have to go to some system
folders to clean up files manually and
then if you have multiple entities using
multiple different versions of the same
assembly you are doomed so some of them
will work correctly some of them will
not so it's a bad idea to use dotnet so
why is it a bad idea to to still use
dotnet well if we're using c-sharp we
are introducing all of these
dependencies which we can we cannot
properly handle we cannot really handle
those dependencies by deploying them to
the database because we will hit a wall
or we cannot really use those
dependencies physically on the server
because we might not have access
to the server to put those assemblies
out there so whatever approach you
choose you are doomed plus business
central will not let you run any dll's
well then CL obviously well it's so much
slower it can be so much more painful
and of course you just cannot do
everything also you cannot migrate that
to Azure functions what would be a good
choice to do and it's also very
difficult to refactor to anything else
so it's really a bad idea so then what
can we do if we cannot use dotnet or
should not use domain what can we do
well the first obvious choice is inside
of a L we have a lot of Al api's like
calling web service is handling JSON
handling XML handling text streams etc
so things like that work beautifully in
Al and are getting improved with every
single release there is something new in
there in that arena where we can use
more features to do more stuff for what
we would have used dotnet earlier if
that doesn't get the job done if there
are things that it you cannot do with
that then you can offload your stuff to
Azure functions and if you don't like
ESRI functions then you have a range of
dotnet underscore code units which are
supported also in Business Central which
are tested by Microsoft which are
approved to be working by Microsoft and
that allow you to do other things with
dotnet using.net but just to a wrapper
rather than directly and if you don't
have a code unit that can do something
specific for you well you can create
your own and then you go to this github
and you simply submit that and then
Microsoft will simply take a look if
they deem that good enough and
reasonably enough they will just include
that in the stack and next service pack
or cumulative update or next release of
the product will have and include that
code unit which you can then use
directly so that's how you approach that
was serious long story
obviously if anyone is a bit lost in the
story like me
let me just read
phrase this in only one slide don't net
good one and I can I want to actually
talk about a small example not really a
small example quite an example on where
we achieved actually one of our I'd say
biggest solution that relied completely
under net and put net interoperability
and our own dll's and so on you touch my
machine sorry sorry oh sorry this is too
soon this is called this is called
enough management now this is an
internal solution I just want to show
you what is possible going from this net
world that we were living in and
following vehicles rules to dont net
yeah
so this enough management is actually a
partner solution is our internal
solution that we monitor our craft
customer service the typical part of
problems being able to remotely log into
customers monitor their nav solution
self-healing services cryptid ask could
not cryptid scripted installations like
if we want to set up a customer we
basically do it through this do looks
like this not in the modern client this
is basically the previous version but
you can see a little bit yeah on the
infrastructure part there is the fellow
fully automated install our connection
to our customers these kind of things so
an infrastructure solution software
solutions to an infrastructure problem
yeah we want to approach our customers
as being cloud customers but they are
still on Prem that is basically the idea
thing is business central and via KHOU
is actually moving us into an on net
solution so we needed to move this in
yeah and into another solution in not
being that dependent from our dealers
and this deployment issues and all that
so we completely rebuilt or are
rebuilding the
and this is the architecture that we are
trying to so we have business central we
haven't completely outside our P and a
web application which is going to do our
funky funky stuff this funky stuff
we used to be in these dll's okay and in
the.net intro and all these kind of
things now we won't move that out so
this is very comparable with Azure
functions for instance but we didn't do
it as your functions we want to be
completely free from s your functions
and build our own web app on the right
part you see an agent an agent which is
basically pushing the buttons at the
customer side and we are able to
remotely connect to that agent let me
try sorry the communication between
business central and and all the
external services is pure rest cost pure
web service calls nothing else nothing
at all
okay so let's see that in practice and
now I can switch to this one this is how
it looks like in the modern client so
this is just to start definitely less as
you have seen in the screenshot the
screenshot is more but this is an
environment that is building up we re
factoring this solution into removing
that part and moving to this happy
approach what I would like to show is
one functionality which is a remote
desktop functionality being able to
remotely connect to any kind of server
we need to be able to monitor or
administer at the customer side on Prem
yeah so obviously this is a test
environment or a demo environment so I
just set up some connections to two of
my servers and one of a co service you
can see here I've been helping vehicles
in
yeah probably setting up I can see
connection details yeah echo has no clue
how to work with docker so we can not
only solve this yeah let me say it
another way customers always want us
want to know when we log in in their
environments and why well there's a law
in behind the scenes so we log who
logged in when how long with what
credentials
yeah and also these credentials is GDP
are related
quite quite sensitive we do not
distribute credentials to our developers
develop do not know any credential for
the customer type still then need to be
able to login yeah so that's all things
that we safe here
and basically we have we set up the
connection and let me just simply
connect or reconnect to via Coast
machine this is one of your demo
machines just customer via KHOU his
agent is this development machine with
the up mint account on which is fee a
map in which you should and they
reconnect now there is this funky thing
going on so this is central connects to
the RP the article next to the agent the
agent asks for details
sets up oh come on come on yeah you need
to close you need to close your browser
yeah man anyway I might have set that up
really yeah that looks like you but in
any case I've taken over his environment
and logged it as well you see here the
URL by the way that actually does the
magic in the background I'm actually
this is a URL to the RP and I will
switch back here to the RP I need to
show this first anyway I will show this
first so this is the
in the background we are rebuilding this
as an app as an al up and if you look
closely you will see that it is a real
extension there is no net going on in
the background I am NOT able to use dog
net in this this this application so
this is the story that I wanted to do so
what business central does it creates a
connection ask token from from the IP
the web app gets it back it calls this
URL with that token in that case it up
is going to connect to the agent the
agent get some details of the service
bus and I didn't redo my slide here
serve this Ebers opens in the channel at
that case in that scenario and then
opens the connection which I don't have
open anymore but I just want to show you
one more thing if I redo that it's not a
direct connection this is a connection
through the service bus and this
connection or this channel is basically
garbage collected let's say from the
moment we closed very safe how it should
be all possible without not a single
don't
this is just a piece of code that is
actually creating the connection if you
look for instance at the last line that
is the hyperlink with the token that
opens the connection basically to the
arm okay yeah sure yeah all this is
obviously possible with Azure Ezzor is
an important part of technology stack
and when talking about Asia let's first
try to get a look at the story of 2002
2011 back in 2011 when Asher came along
the number one question was wow this is
really cool is there anything we can do
with Azure we the nav people and the
answer was not much really so back in
2011 we could have used virtual machines
if we wanted and then people tried using
those virtual machines to deploy any be
to Azure until a couple of years later
it was suddenly possible to use Azure
simple databases then it was possible of
course to use Azure Active Directory and
as time went on Asher grew so the the
Azure landscape today looks something
like that with all of different services
that we have inside Asher and those blue
ones are those that we have seen from
from nav these days using nav without
dotnet we can connect in this or that
way to all of these that I've marked
blue probably it's due to some others
just couldn't bother so the entire ESRI
landscape has has really changed a lot
so if we go back to that question of
2011 can I do something with Azure the
question of 2018 is can I do anything
without a sure
because that's what we what is currently
possible like we can really just take
any of those services as you will be
able to see soon and and do something
crazy that was even unimaginable so back
to this slide of course we cannot talk
about all of these blue ones I've just
picked three most prominent ones we will
actually show only two not only just
because
we're running out of time one of them we
have showed Doralee last year so we can
really watch the session on YouTube so
Waldo do I really cannot talk anymore so
can you just take over machine-learning
yeah when we talk about machine learning
one of the most new topics I guess I
connected to NIV well I'm not going to
talk too much about that either because
there are too many services really a lot
of them are very interesting for
connecting to an AOP development like
business central but a lot of them are
not I wouldn't know why I would like to
do text analysis or or translation maybe
in any case today there was a session
already that handle quite some machine
learning part that is a very important
topic and you should look into it
building your own models Microsoft
already introduced you to a few
functionalities where they implemented
machine learning like like what cash
flow forecasting for instance now I said
I'm not going to bother you with that
people already bothered you with that
and if you haven't seen that go and
watch YouTube but from all these
services there is another one that might
be interesting and Microsoft is actually
already using you must have seen demos
of for instance Marco did it I think on
some keynotes that the imported of
pictures are from himself on contact and
all of a sudden some machine learning or
AI technologies recognized that he was a
30 or 40 year old man the thing is that
Microsoft built is built is on top of a
service in Azure computer vision you can
build on top of that and let me show
that in a small demo so this is the
smallest demo of their demos
to save this so this is an example where
I have a code unit wait
actually this is the magic we're
actually reusing code units from
Microsoft do do my own vision analysis
right and you can build on top of that
you don't have to do any magic just
reuse what Microsoft is already using
what I did is I put that here in the
cloud on my German server and what you
can do is here well this is just a list
where I can import pictures and then
it's going to recognize a little bit
more than just the gender and what is it
eh I want to tag basically everything
that it can tag so in this case a toy
doll dressed and and so on and in my
case 39 year old males and was lucky so
and it should do that still maybe with
Viejo's picture here very very old
picture is actually from five years ago
and five years ago it was a 45 year old
karate man Wow that's quite some machine
obviously this is not really hocus-pocus
that was also the idea is that is this
is not hocus-pocus is this what you can
already do by simply reusing what
Microsoft is already putting its work in
it's it's already a big framework to do
facial not facial recognition but at
least cognitive services recognizing
properties from picture 45 you know when
you look this good at 50 talk to me
I also would like to refer to the
session and we put that one of the last
slides because this session is going on
at this very moment and we didn't want
you to move out of this session so which
or doing crazy things with other
services on passion last but not least
is the azure dev ops part another
service from azure actually this is is
this really a service of let's call it
the service from either because they
renamed it from visual studio via steam
services which is now called agile
devops now can I ask who is source
controlling their CIL customers oh yeah
maybe clap because I don't think ok so
that was not a lot so can I reverse that
question who is not source controlling
their CIL customers that should be
anywhere else right what other option
was available the question is why not
and I will tell you why not and you know
why not because CIL didn't really make
that really accessible so what control
was was quite a challenge going one step
further is continuous integration and
continuous delivery this is a hot topic
these days but what is that well let me
talk about continuous integration we
talk about continuously integrating code
from developers continuously merging
just imagine when you're doing al
development not see al but al
development all these files are locally
on your PC at certain point I need to be
merged we are going to merge the bejesus
out of ourselves yeah continuously so
best practice is that something
automatic will do that for us
not only that at a certain point we will
have to deliver the code to environments
like our test environment like a lively
point
yeah so basically we are talking about
source control on steroids basically we
talk about working in tea just imagining
- all these files are spread on your
PC's and but you're still working in
team on one app continuously merging
continuously testing if everything still
works because I might be developing one
feature the other one is developing on
feature and the third one is developing
speech at the certain point he says yeah
merge it but does that still work in my
code because we never touched each
charge code yeah you're not evolving in
one database anymore so this is the
concept that is yeah quite new for our
world I've got 6 minutes and 48 seconds
so to show you that thanks do you just
talk a little bit about the challenges
just imagine you're doing an app for app
source this app for app source is
probably for multiple countries so just
the database that you're developing and
it's not enough to actually developing
in 15 databases because it needs to be
able to run in 50 nopales Asians yeah
are we going to set that up well you're
developing in one environment you're
building and all the others yeah I'm not
going to spend all or all the challenges
here or dependency challenges like
automated test challenge how we going to
test in all these 15 environments and
then a test environment does this
comes later but everything is tested and
built and compiled how do you get that
to an environment that your consultant
can check that is actually that's it
what what it asked for it compiles a No
but is this what I asked for and if you
do a rebuilt and you deliver again to
this QA environment is it still what I
asked for and where it's my data that I
just set up previously it gives you a
lot of challenges challenges that you
can solve with the combination DevOps or
as a DevOps or build automation and all
these kind of things and
and powershell now that's too soon
there's good news the good news is vs
col vs coat gums natively with good
support so source control it's gonna be
hard to not do source control alright so
next year everyone as it develops helps
you setting up this continuous
integration continuous deployment yeah
and last but not least Freddie is there
to help you as well
he has got lots of scripts that helps
you setting up this build
setting up this this delivery yeah just
go to that block I have four minutes I
shouldn't be doing this but I'm still
gonna do this just to simply show you
and not I'm not going to do the complete
demo but show you how this DevOps could
look like so I got here my enough take
days 20 18 project with a repository of
my simple image analyzer now whenever I
push a change to a certain branch and I
have two branches here I as a developer
need to mark this development as close
like I can push multiple things to this
branch which from from the moment I say
yeah ready then I can create a pull
request I can request my master
I can ask him to pull my code and that's
very create all the question you'll see
here that I have a few completed pull
requests already and that results into
some kind of built this is where
actually our DevOps or our continuous
integration comes into play in school
it's going to test if everything still
works and you can see here what is it
going to test right it's going to
compile my code against the current
master it's going or against multiple
versions is going to run the test
application and it's going to even
capture the results of of the test I can
even see here what it did for tests and
I hopefully 100% of my one test failed
succeed I only have one test and 100%
six yield nice thing is from the moment
I have a bill from the moment the
application DevOps decides yes you did a
good job I could build you an
application I've got you an app file I
can also automatically deploy this and
this is basically release pipeline
release pipeline - in my opinion in my
case to this online environment on this
journey server this is again where
docker and my remoting docker comes into
play because I want to move this app
file up to my remote environment
installed there the app for that either
just built with meaning from the moment
I create a pull request let's say seven
minutes later it's deployed on a test
environment and I don't have to do it
try that with Caesar
so tomorrow at 11 a.m.
these three fellows are going to show
you a lot more recording continuous
integration you have anything to say
nothing more to say man you can talk you
know mr. Bligh I love this session why
because it's over so we said all we had
to say so your turn now we have 1 minute
37 seconds go if the question is good
you can earn a t-shirt and keep that
away from me I kill people with that I
know if you if you can't okay if you
can't use net functionality directly is
it possible to use it via JavaScript for
example and if the answer is yes
are there any limitations or
disadvantages sorry I must admit I
wasn't paying really attention because
Waldo was taking over and I was just in
them I was just roaming in the Miken and
my question was if you can't use net
functionality directly yep is it
possibility to use it via JavaScript for
example and if it's a scrip what do you
mean by JavaScript well JavaScript
doesn't have access to dotnet directly
anyway so you would if you would want to
do something like that theoretically you
would theoretically you can do that but
the implications that you have are just
huge so for example how I would imagine
that that you would have some kind of a
service sitting on a local machine where
JavaScript can talk to that but then
that local service would have to run on
HTTP not on HTTP because otherwise you
would not be able to consume that from
the client and if it's running on HTTP
it has to have a certificate which you
need to update because otherwise the
browser would
trust it or if it's self signed you
would have to somehow establish that
trust on every machine so it would be
painful so yes you could call your
functions as well okay when are you
planning to go on Europe with your music
[Laughter]
is it like enough called something
different from the moment basically you
you commit right and you push your
changes it starts doing that so you have
triggers in that they hope that that can
automatically be triggered from the moon
you do something so what I did is from
the moment there is a pull request it
starts building up so there are agents
somewhere from DevOps agents on servers
so we saw these two Volvo service I
opened Shaco server because I something
to show but I hope these this Volvo
service or actually these agents from
their verbs that are constantly waiting
from the moment that that magic devil
says okay I've got job for someone it
finds an agent and finds an agent and it
starts doing that so obviously I need to
install stuff on that agent like docker
like there is a part that is going to be
yeah downloading an image and
compounding my code at that point so
it's a combination between an agent from
that DevOps
PowerShell and and yeah docker okay so
there is no Python called auto merge and
this point there is no edge DevOps
template that you can use you Echo's
first funky demo with nodejs
was that driving the client to was a
client calling the nodejs
my node.js demo involved only node.js
but what I the only thing I showed in
nodejs was those crazy true default C
JavaScript boolean logic my first demo
was the client so I did some JavaScript
hacking it was hacking so that Muppet
client was modern client was hacking it
I could yeah I would have done it all
using controller then except that I
couldn't show the splash screen using
control in so for the purpose of the
splash screen I added I did some hacking
but other than the splash screen
everything else it can just be done with
the controller in just pure simple
controller in JavaScript clean and neat
[Music]
you mean like themes and stuff yeah
absolutely do you want to map a team I
can do Star Wars theme next time
lightsaber man you don't want to use how
do you want to access like local
resources like ports
like service bus is one of the options
Waldo has just shown that so he was
accessing a VM he can access some other
local resources then that question that
I explained is another way like you
could have a local service running on
your local machine that you could do
yeah I know without having something
running locally which is either a
service that responds to either your
JavaScript or something in the service
bus or without building the entire
client wrapper yourself you cannot come
on ask that guys something about
PowerShell over time you need the stuff
doctor Walker Walker last question
let's contain you don't get the shirt
can you play something for the end of
this session we didn't plan to well
let's play that theme again okay do you
want that well we have less stage fear
[Music]
I love the song thank you thank you
