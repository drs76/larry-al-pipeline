# BC TechDays 2023 - Experiments for BC - Wasm? Codespaces? Linux? Wtf!

- **Source:** https://www.youtube.com/watch?v=gZyAREvm4Q0
- **Video ID:** gZyAREvm4Q0
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 88m45s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

Welcome to our session we're gonna talk
today about webassembly about Linux
about code spaces about Dev containers
so we really felt like we need to do
something different this year
um you know AI is nice but I'm not too
keen on the 115th AI demo to be honest
um and maybe we've seen enough Power
Platform as well so we felt like let's
do something completely different I was
a bit worried that we would be sitting
in front of 10 people because no one
would get the idea but I'm very happy to
see that all of you have joined even on
nine on the second day so thanks a lot
for coming
um with that I also want to say thank
you to Stefan for joining the stage
today but yeah please Stefan and
introduce yourself yeah as you can read
my name is Stefan Merle
um currently I'm a freelance PC
developer and you might have heard some
of my projects so I'm I was the creator
of the code history repository on GitHub
as well as the linter cup
um
and well feel free to reach out to me on
Twitter LinkedIn GitHub anywhere if you
have any questions afterwards and I'm
going to show you later another vs code
extension I created
perfect
um thanks so to introduce myself to BS
fencer on the business side I'm a
managing partner at 4ps in Germany on
the community side I'm an MVP a regional
director and a Docker captain and if you
want to reach me um you can find my
social handles my blog my podcast and so
on so yeah always happy to have
discussions on BC Tech around BC with BC
whatever so please please feel free to
reach out
but with that let's Dive Right into our
topic um I first want to let you know
that a lot of the things that we're
showing today are more or less
experimental or are relying on
implementation details that we figured
out by looking at code that might change
tomorrow so I sincerely hope that all of
our demos work so I can prove to you
that it works today but it might not
work anymore tomorrow so if you want to
use the things that we're showing today
um especially the stuff that Stefan will
be showing he's using on a day-to-day
basis so we're pretty sure that it's
it's quite stable on the other side
there there might be changes coming up
soon so yeah if you want to use it feel
absolutely free but be aware that this
is stuff that might break without
further notice but I hope it's fun and
could give you an idea of what will
happen in the future in our ecosystem
and if you don't know who that guy is
then that shows that I'm pretty old and
you're probably younger and if you start
googling
it's three movies first is great second
is okay the third don't even bother if
you haven't seen it
okay so let's go into the actual topic
what are we going to talk about first
part will be about webassembly or wasm
what is it where does it come from why
does it matter in general why does it
matter for us in the BC
um ecosystem and of course we're going
to take a look at a couple of demos and
then in the second part we're gonna take
a look at Linux Dev containers and code
spaces again why would you bother to
implement or to use Al on Linux and how
does it work Dev containers and code
spaces again why does it matter how does
it work and let's see a couple of demos
in the end depending on how much time we
have and how much questions you guys
have we're going to take a look at the
AL language Linux Patcher which you
probably don't know yet but
um we'll get to know during the session
so let's see if we have time for that
and if not then Stefan will find a way
to share then
so what is webassembly or wasm in short
um basically it's a safe and portable
low level code format the idea of
webassembly is that you can get with
something that is actually platform
agnostic near native performance in a
sandbox environment that means that the
code that you create that you compile
into a wasm is running in a secure
environment that is completely
independent of the hardware of the
platform of the language and so on so
we're going to be using a couple of
different languages programming
languages today but it all will be
awesome in the first part
it gives you a very small and
efficiently executable file that you can
use to stream and parallelize so you
don't have to have all the code to start
executing you actually can have small
parts first start executing and then
later download the rest of it and it's a
modular in a binary format which means
that you can plug in different modules
collected from different places they can
talk to each other
it's an open standard I've put the link
here if you really want to you know if
you have trouble falling asleep then the
standard is always a good idea so you
might want to take a look at that
um the first implementation of browsers
and we'll we'll also start there in a
second have been in browsers because of
course you have a safe way to execute
code without accessing something outside
of your code it's portable it's small
it's efficient it's streamable I think
it's pretty clear that this is something
that makes a ton of sense in a browser
in web applications but we'll also take
a look at different implementations
and the example and that's where I want
to start first is banana bread
so this is actually
a webassembly implementation
and I'm extremely bad at it
so there will be a guy soon
who will hurt me
let's see where
I can jump
shoot I can run
and there he is and I will have a
problem because I'm extremely bad and I
don't even have a mouse
but anyway
um
let's stop that one right here point is
this was a webassembly application built
in 2012
um I was actually surprised when I
started to dig into the origins of of
webassembly how soon it started and how
much you could already do in 2012 at
that time of course gaming is always an
interesting application because it has
its complexities it has performance
requirements but there are other
implementation you might have seen in
the past couple of years things like
Photoshop figma AutoCAD really have big
requirements
um Graphics requirements suddenly run in
the web and the reason for that is
webassembly same is true for Google
Earth so whether you know it or not you
have probably been using webassembly
quite some times in the past
um how do you actually create something
that could run as a wasm thing as a
vasel module well it depends on where
you're coming from where you want to
create your code we have first system
programming languages like C C plus plus
rust and go and they have always been
used to compiling into different formats
because they needed to Target Linux they
needed to Target Windows they needed to
Target different architectures like arm
and so on so for those kind of languages
it was relatively easy to create support
for bosom because they just needed to
compile in a different format so they
already had things in place that made it
quite easy for them and then therefore
they were faster
then white code languages like Java or
c-sharp for them it was more more
difficult because they yes they were
already compiling into their own
intermediate languages but they weren't
used to compiling into different
um targets basically so that made it
more complicated for them took a bit
longer and you still see languages
picking up support for wasm mostly it's
still experimental early days and so on
but you can use those languages to
create awesome components already and
then for scripting languages like python
or JavaScript they just have a
interpreter because you just write the
script and then it's interpreted on the
Fly and what they are typically doing is
that they are porting The Interpreter to
vasum so you still have your scripts the
interpreters running on wasm now and
yeah the the scripts are interpreted
from a support standpoint it can run in
all major browsers but you can also run
them natively in on Linux on Windows or
whatever you need but because the wasn't
module itself doesn't know what to do
it's just the instructions basically you
need a runtime the runtime could be a
browser or it could be something that is
running on your on your machine
somewhere in the cloud whatever and
that's where the webassembly system
interface called Wazi comes in because
it allows a webassembly component to
have access to the system to have access
to networking to files and so on
that's it for the theory I thought about
how much Theory do I want to do and I
decided to keep it short
um I hope you can still follow along but
let's Dive Right into our first demo
because we want to create something that
is a awesome module what you're going to
do is we're going to use rust as
programming language we're going to
create a hello world because yeah that's
what you do in development when you do
the first demo
um and then we I'll show you how the
security sandbox works and I'll show you
how portable it is
and because we have code spaces as our
second topic of course I'm using a code
space for development
and I need a bit more space here
actually
is that still big enough
oh okay so what we're gonna do
um you can see here Visual Studio code
as I said it's a it's a code space but
you won't notice the difference for
today and what we're gonna do is first
create a demo project
and I would have had to delete the demo
try again
okay that's better
so we have our brand new demo project it
has very easy code
it says hello world and of course we're
going to change that to hello BC Tech
days
and that's basically all so the the most
simple
implementation that you can think of
let's go into the demo folder and now
we're gonna do the build as you can see
here
and it has a Target that says which
means it's compiling of other module
that wants to Target the um the system
interface so vasi and now we already
have our module and it's in here
Target
we have a awesome file so this is a
binary file we can't take a look but
this is the module that I can take and
run basically everywhere
so to show you
we're gonna use the
avasm time implementation of the Wazi
and there you can see okay we have a
Hello BC Tech days so exactly as we
expect and as I said it's completely
independent so if I download this to my
local machine
in the demos folder and overwrite the
existing file
yes then I can open my local machine and
do a vasam Time
of awesome and it still works hello PC
tech days so that's basically the the
idea and one of the big benefits of
vasum you run it or you create it in any
language that you need that has support
for volume and then you can just
distribute it to anywhere and it will
have a way to run
now to make it a bit more interesting
and also show you the concepts of the
security sandbox
and because I'm bad at typing I've
prepared it so you can see here in Rust
that we want to use the environment we
want to use the file system we don't
want to use read write access
second step is to create a
little function that takes a file as you
can see here reads the file
creates another file and writes the
content of the first file into the
second file so we're basically just
copying two files
and then we need a
we need a main as well and that one is
just taking the arguments that it's
giving it
um running the program and executing the
copy
so again let's compile
try to run and that says okay you need
to do give me the file that you want to
copy and the target file so let's first
create the file
so we have our first file and now we can
say
um
and put it into another file
like this
and it says there's an error and that's
what I wanted to show you because that
is the sandboxing thing so I can't just
access a file because I have the code I
have the required libraries I'm running
in this sandbox and that doesn't allow
me to do any networking and do any file
access it's completely secure I can of
course give it access
if I do something like this
it works so if we now take a look at our
file you can see we have copied from one
file to the other file it has worked and
I could now copy this over to windows
again do the same thing on Windows it
would just work but for the sake of time
let's not go there but just to give you
an idea this is how you create the
applications how you run the
applications we will also see later how
it works in a browser but in general you
create the vasel module module that
module has a starting point has
functions like you used to in
programming and you can access them and
do things with it
let me check that I forget something
that I wanted to show you no this looks
good
okay so this was the first demo um why
why does this actually matter why does
it make sense to look into wasm you can
already see with the examples that I
gave you that it's used widely all over
the place to put all kinds of near
native code near native performance into
a browser so that that for a very long
time has been the main application of
webassembly that you want to run
something that is actually native that
you want to distribute in a different
way and that needs almost native
performance into a browser
because it's so small it's secure it's
portable it's also very interesting for
iot and Edge devices because they
typically have very small resources you
need to be able to run something that's
very small very efficiently and again
that is something that webassembly can
do
it also allows you to to use the right
tool for the job because as I said in
the beginning wasn't tools can easily
interact with each other so if you have
something that you actually want to
create in let's say C sharp but it would
like to use a go library and a python
library then this is something that with
webassembly is relatively easy to
implement
and what we've seen recently is that a
lot of cloud service providers have
started to support webassembly or new
cloud service surprise
cloud service providers have been
created solely on the purpose of
creating webassembly support where you
get a framework where you get an
environment that you can just throw your
webassembly module at and they take care
of the rest it's completely serverless
runtimes with great performance again
because of the benefits of of
webassembly
why does it matter for us in the
business Central world I think there are
two clear scenarios with maybe less
clear applications that that's where the
experimental part comes in but the
things that you can do in general is
either you use it on the client side so
that means you have your um your web
client open you you want to do something
in there and you use a awesome module
for that that's going to be the first
thing I'm going to show you and then of
course we have the server side
um it's extremely fast secure and
scalable and maybe it can do things that
PC is just not ideally equipped because
of the way that Al works and you just
want to use whatever language whatever
Library you need and you can address it
from business Central which basically
means the
um
serviced here would call a webassembly
application and as I said we're gonna do
a demo of both parts now
so the client-side demo is the the idea
that we have the nice little pictures of
customers on the customer card and what
I want to do is I want to use a go
library to change that picture so live
in the browser we're going to use
JavaScript to address the the
webassembly module written in go and
that will get the picture we'll change
the picture and show it again
so let's take a look if we can make that
happen
my second code space
here
so what we have is our go application
first
it has
a bit of code here
so it's using a library to adjust the
image
we can do
Integrations with JavaScript so you can
see here that we have a brightness
callback so if we later change the
brightness on the image that's the code
that will be called it gets a number
which is the amount that we want to
change to brightness it uses the image
library that you can see here to set the
brightness and then it sends the updated
image back into our browser and again
we're going to use JavaScript to make
sure it works
then we have the same for contrast we
have the same for you we have the same
for saturation so that's basically the
core of it that actually does the
changes to the image
then we have some code that loads the
actual image so it takes the bytes of
the image puts them into a buffer it
resets the sliders so this gives you an
idea how we can also from our go module
in webassembly talk with the browser to
through JavaScript so we have a
brightness slider we have a contrast
slider and so on and we can reset them
and the last part is to put it all
together so we have our main method and
when it starts it sets up the brightness
callback on our brightness slider it
sets up the contrast callback and so on
and in the end it says hello from Boston
go and we will see that message in a
second as well
so that's basically the Go part and as
we seen before we need to compile it
and
now we should see here it's the Shimmer
basm so this is um the the awesome
module that we've generated and of
course now we want to use it in Al we
want to use it in business Central
so for that we're going to use a control
add-in that you can see here it uses the
images as a workaround to get the
awesome module into the browser it has a
startup script it has something that
helps us to execute the vasel module
that's a standard script that just comes
with go in this case and we have an
additional script here to give you an
idea the startup just creates a bunch of
HTML code again we have our brightness
slider we have our contrast slider and
so on WE inject it into the Java into
the HTML code we have a status field
that first says initializing it loads
the vasel module as you can see here
maybe I should enable
word wrap
um yeah you can see here how we get the
Vasa module then we instantiate it
we use our status field to say when the
initialization is done and we create a
connection through this memory bytes
array between the go world and the
JavaScript world so we can pass the
image back and forth
in the additional JS you can see that we
first
have a connect image function that
fetches the picture so by looking at the
area labels I can figure out what the
picture of the customer is where it is
and then we just fetch it into a byte
array and call the load image function
that you've seen a second ago and then
on the other side when it is changed we
have the display image function that
again takes the area label to identify
the customer picture and shows the
changed image
and then on the page
extremely simple again we just add the
image adjust control that you've seen
and we have a action that runs the
connect image function
so let's see if we can publish
and this is one of the drawbacks of
running in a oh no of running in a
code space we need to re-authenticate
all the time
but that should do the trick
publishing
and we're getting business Central
but that that last demo code L and code
spaces yes absolutely
and in a second we will see why that
actually works
so we have our customer picture here
slightly adjusted from the standard and
now I can
um you see here the hello from Buzz and
go so we know that the implementation
has worked this is actually go code that
has created that message now I can
connect the image it says ready for
operations and now I can adjust the
brightness
I can adjust the U
so yeah absolutely business critical
application I know
um
but still it was fun to create
um if I move over here I can again
connect the image
and just the U
adjust the saturation and now we have a
beautiful black and white image so again
um I know it doesn't absolutely make
sense but it shows you that there is a
way how you can use a completely
different programming language a
completely different approach to create
another module connect it to your
business Central code al control add-in
and use that to make whatever you might
need to make in your in your application
so this is basically
um the client side when we actually run
the Vasa module in the client but as I
said there's also an application on the
server side
the idea here would be that we have a
backend service on open page so whenever
a page is opened we call a backend
service and because of awesome is so
incredibly fast and scalable it doesn't
take a lot of time now this is certainly
not something you should do a lot
because it will make opening your page a
bit slower but I hope that you will see
in a second that it's actually quite
fast
what we will use is one of those
serverless providers that I talked about
called Fermi and spin they provide a
framework for building and running
microservice applications with
webassembly and I'll show you in a
second how that works basically they
just give you a framework that you can
use to create your version applications
and be a runtime so we can just publish
into their backend and it works easily
we will see how we can create a module
we can see how the performance is and
then in the end we will take a look at
the pre-built example with the BC
integration
again let's
switch to
a code space
and
get a terminal
let's say Spin U which is the way how we
create a new spin module
it will be an HTTP go implementation the
name will be easy Tech days demo
no description just accept the defaults
and with that we have our BC Tech days
demo application you see here now we
switch to go
we have a Handler that just takes a
request and answers with hello fermian
and of course we're going to change that
to hello BC Tech days
and that's basically all it does the
main function is empty
so when we now do a spin build and that
takes a second so I also want to show
you the second important file which is
the spin tomorrow there you can see that
for all of those different components
and we are now creating the main wasm
file so that's that's where we're
running I can say which HTTP host for
example are allowed to I'm allowed to
reach out so another example of the
security sandbox I need to explicitly
state which backend URLs I want to
access so if my version module wants to
reach out that needs to be in that list
here as well
so we are done building let's do a spin
up
which means that the application is
running
and we can connect to it yay
let's see if it works locally
we are not getting an answer why not
let's try again
I think I've run into an issue in GitHub
by the curl again okay what I actually
wanted to show you is that it initially
works
but maybe
last attempt to show you
if we just create the
get request here
we get a response of not found
ah
did I run it in the right folder
no I didn't okay sorry
our demo is PC tech days demo and if I
do a
spin up here
I need to First compile it because I
also did that in the wrong folder
so that's
um
oh I did it in a completely wrong folder
now I see
okay sorry for that
so let's move it into the right place
okay let's see if it works here
it's been built again
I knew one of the demos was gonna break
but I thought it would break because
they changed something in the back end
but this is clearly my own stupidity
that breaks it so sorry for that
uh spin up again
try to access it hey hello BC Tech days
um so that has worked the request here
also works hello BC Tech days okay
that's what I actually wanted to show
you and the other thing I wanted to show
you is the performance for that I'm
going to use a little
um tool called hey that can just fire
off requests so what we're now doing is
that we're running 50 concurrent clients
with 10 000 iterations so what we've now
done is that we ran 10 000 requests
against my little application here which
took two and a half seconds the slowest
was 0.5
0.05 so basically 50 milliseconds and
the slowest was
um 12 milliseconds and you can see here
that is just extremely fast granted it
doesn't do anything but it shows you
that the whole wasm runtime around it
doesn't take anything from the
performance it's actually near native
still although it's it's not native
application it's wasn't but it gets
performance that is really great on a
near native level so even if we extend
this and say
let's say 250 and 50 000 requests it
will take a bit longer
but still we should say I should see
comparable
um comparable performance so that means
if you have an application that is
triggered a lot of the time you don't
really know might there be Peaks that
are really high you don't really know
how much concurrent requests you get
then webassembly is something that will
help you because
um it has amazing performance again you
can see here now it's gotten a bit
slower but we have 200 concurrent
requests now or 250 what do they do yeah
250 concurrent requests
um 50 000 times and still we are
extremely fast so you can see that the
the infrastructure the whole setup is is
really amazingly fast
um but let's actually remove that one
again
and
show you what I have for the store back
end so um the the predefined example
that I have is just something that uses
a key value store that's been also
provides and it just has a an easy
Handler here that accepts a where is it
a post request so if you run a post it
just stores the information if we run a
get as you can see here it gets the
value from the back end and we can run a
delete to delete something so again it's
just the webassembly application that
allows me to store some arbitrary value
and what I want to do is show you how we
can integrate this with the customer
um
with the customer page in business
Central again so
my Al code looks like this
um
we have on the customer card and action
that just sends a post to my backend you
can see here how an application that is
running server side on fermion actually
looks like
and it um yeah we'll just send a post
that means that the customer is
registered it just creates a record
there and then on after get record of
the customer card we're gonna do a get
that basically checks whether the
customer is already registered in our
backend or not and if we
if you don't get an okay then we get a
message that the customer is not
registered
let's see what this looks like
okay
and we are publishing again and because
we're running in a code space we have to
re-authenticate
yes
so here we are in business Central we
open the customer card
says the customer is not registered of
course we didn't send the post request
before so I'll run my register customer
and if I now go back
it shows me that it um
it has registered it if I change of
course I'm getting the not registered
again this might be maybe more relevant
for something like license checking
um but whatever what I mainly want to
show you is that if we take a look at
the performance of loading you can see
my server side of awesome implementation
that has 712 milliseconds actually
that's because we ran it twice
let's go out and back in here
now we're getting closer to 350
sometimes 300 now it's 400 milliseconds
so we're doing a full back-end trip
we're requesting something from the back
end the awesome application is taking a
look at a key Value Store returning the
value and all of that only takes 400
milliseconds again should you do that a
lot of the time in all of your own open
pages definitely not but if you have a
requirement that says I need to call
something in the back end it needs to be
extremely fast it needs to respond very
well it needs to scale very well then
this could be exactly the kind of
application that helps you to to
implement things
okay that was my server side demo um and
the whole overview about wasm again I
wanted to show you what it was and where
is it coming from the roots in the
browser now also moving to the server
side moving into iot and Edge what are
the main applications and hopefully give
you an idea of why it matters for us in
the business Central world as well
so that's it for the first part
um now let's switch into the second part
which is Al on Linux Dev containers and
code spaces
um
why would you even want to do this
the idea of running Linux is that you
have something that is completely under
your control you have full transparency
you have full configurability I used to
use a Linux laptop until I moved into
the the nav world and the thing that
annoyed me most was that suddenly
Windows was doing things and I didn't
know what and it showed me the system
process was using 90 of my CPU and I was
yeah kind of annoyed with it so that
really from my personal perspective is
the big benefit on Linux you always know
what is happening if you really want to
you can dig down into the source code
and figure out what happens
it has a huge developer-centric open
source ecosystem so I think if you're
going to give it a try after maybe some
initial struggles you will feel right at
home it's definitely less demanding on
your Hardware or if you stay on the same
Hardware you get better performance it
typically has no license cost and it's
yeah to be honest just fun you can just
change it in any way that you want and
Stefan will show you in a second how
different it can look
why would you use Al on Linux well if
you're used to the benefits of Linux if
you want to run a Linux laptop or a
Linux machine then why not use Al if
that's the only thing that is blocking
you then we will give you an idea how
you can do that of course there's also
drawbacks um sometimes Hardware
components are not fully supported
actually that's also a benefit because
it's not coming pre-reloaded pre-loaded
with all the drivers for all the
components out there actually you need
to do a bit of your own setup and then
you can typically make it work it comes
with only very few pre-installed options
so it's not as easy as with Windows to
just go into a shop or whatever and say
I want a Linux laptop
um you're you're a bit more limited here
and not everything that you might need
for your job will probably work so
things like Microsoft Office the report
designer of course Windows containers
Seaside if you still have to use that
the BC server although I heard there's a
different session that shows you how
that might work and of course the AL
extension but we will give you a fix for
that and if you're into gaming there are
also less options for that but the most
important thing is Linux has acute acute
logo so it's a penguin who doesn't love
penguins a lot better than just the four
squares of windows so that that might be
a very good reason to switch to Linux as
well
um why doesn't it work out of the box of
course
um Stefan took a look at it and what
also helped a lot here was the migration
to.net core so actually the thing that
is running the code that is running
already is
um independent but uh the the extension
directly used a pre-compiled Windows
binary instead we need to call the
generic dll that is also contained by
using.net directly and then there were
also some small cosmetics in the Json
data types that are different between
Windows and Linux that needed to make
that that you needed to make happen and
the fixing of course is done with an
extension which is the AL language Linux
Patcher that has very recently appeared
on the visual studio code Marketplace so
if you just want to use it you can find
it um in the search
and with that I'll hand it over to
Stefan for the first demo thank you so
let's get the screen switch first
um
don't be afraid I'm going to explain
everything it might look different but
it works
all right so this is my terminal I'm
going to launch a vs code profile I
create
um so that should feel a little bit more
home already
um as you can see we don't have any
extensions installed now so I'm gonna do
this live for you
first we need to have of course the a
language extension
and while that installs oh it already
finished
um the Linux Patcher as well so now only
two extensions to make it nice and
simple
and what we can do now without patching
anything for now we can do air go we can
we have a few comments to open the home
I don't think it worked I don't want it
right now but
um all the other comments like download
symbols debug publish all of that not
there so let's do I'll go first
and just call it BC Tech base
latest platform
and
the generation Works syntax highlighting
works
um so far so good but you didn't see the
message pop up that the language server
is loading the the workspace and
everything and as I said we can't
download symbols so there is no no way
we can compile this actually it doesn't
figure out what build task should be
used so all that doesn't work
um that's where the petrol comes into
play
um and I try to very hard to explain
everything you need to do if you want to
try this on your own so precondition is
that you have.net 6 installed on your
machine I included the comments how to
do that on a on a fresh install and also
how you can find where your net
installation ended up it should add up
in the bin.net folder and that's the
default setting if it doesn't end it up
there then you can change the setting of
the extension so it will patch it
correctly
all right so let's add
run the patch
and what happens it um
it just search and replaces basically
inside the a language extension in the
typescript code and then executes the
window reload so you uh yeah reload all
the extensions again and as you can see
it already asked me to choose the server
which didn't happen before and I
prepared a launch lesson otherwise so I
can delete this
and if I now execute download symbols
which gets available I can authenticate
and I have my symbols
almost not yet
and I know that might not look very
impressive since you can all do this on
Windows out of the box right away
um but yeah now you can also do this on
Linux so we can compile without any
problem just Ctrl shift b as you used to
and we can also
publish
yep I trust the domain
and there we go hello hello World
published everything works
so now a few things that don't work
maybe as good
um
there are still a few things that are
not not quite there yet
well it works on on the native machines
I can actually show that so I'm
debugging
works as well I can I get the full debug
um
experience here the debugger experience
so I hope this is big enough yeah it is
um
so
yeah I think
did I want to show something else
oh I think that's that was it for the
first demo
exactly so we what we basically now see
just to put it into perspective again a
leading Souls native relearning learning
Visual Studio code because that just
works and how we can patch the a
language through Stefan's extension to
make sure that we can actually compile
we can publish and we can debug as
you've seen can you switch back to mine
okay thanks so um that's the starting
point the second idea is now that we
have Linux support that opens up a whole
another world for us now we can suddenly
start using Dev containers in code
spaces but again why would you even
bother why would you want to use Dev
containers in code spaces well if we
take a look at production environments
we are now a sauce ready so we have all
that that automation we don't need to
worry about the whole infrastructure of
our production environment but when it
comes to installing our Dev site then
it's probably still manual if you're
lucky then you're working for a company
that has kind of a description what you
need to do or you might even have a
collection of EXT tensions in vs code
that get rolled out or something like
this but actually it's still a very
manual process of setting up your
development environment and if you're
not only doing BC but maybe different
things as well different programming
languages different Frameworks and so on
that becomes even more complicated and
and you probably need to do some manual
stuff as well so the idea is that we run
our development environments in a
container and this time I'm not talking
about the container with business
Central and SQL that you probably all
know and and use
um so that's not the thing I want to
talk about but actually we're going to
put Visual Studio code into a container
the AL language into a container c-sharp
PHP whatever you want to use whatever
you want to need or whatever you might
need for your job all of that the
development side of it can run in a
container as well
that gives you cleanly separated
development systems because you don't
have any version conflicts anymore if
you want to develop and for whatever
reason you have to develop with a
specific Al language extension version
that can be configured directly in the
container if you have to use a specific
c-sharp version that can be configured
in the container if you need to switch
into a different project with a
different version you just spin up a new
container that has a different
configuration they both don't interact
with each other they both have side
effects so it's very easy to have
different setups for your development in
those containers
and I don't know how it is for you but
at least it is for me um at some point
of time my development environment will
start to feel slower where things will
appear they're still yeah then you know
that you have to reinstall or start from
scratch again and if you have it
containerized again that is extremely
easy because you just throw away the
container create a new one it takes
literally like 30 seconds and then
you're up and running again with a
completely clean with a completely safe
development environment
we have all the dependencies all the
tools the versions
um the the other stuff the settings the
visual studio code extensions that you
might want to use all of that is
described in the dev container Json that
I show you in a second so we have kind
of an infrastructure as code approach
for development environments it's
completely defined in a Json file and we
can put it into Version Control so you
know that your developers are all using
the same configurations they're all
using the same setup if you want to
update to a newer version you just make
a change like you would change your
source code through a pull request put
it into Main and then roll it out to all
of your developers so you know they are
running on the latest and greatest
version again
and it's an extremely fast setup so if
you need to onboard new developers if
you need to switch between projects if
you have that requirement in your
company it will also help tremendously
because you don't need to set up things
manually you just use the tooling um the
configuration files and it's done
how can we do this Visual Studio code
comes with development containers or Dev
containers so they are exactly what we
need containerized configurable local
development environments we can connect
with Visual Studio code so from a
tooling perspective from an IDE
perspective it works exactly the same as
if you're working natively and it gives
you the full functionality including
extensions access to local resources
offline support so all of that works as
you would need it and really at least in
my opinion it only has benefits with the
only drawback that it doesn't work
Windows based so yeah welcome to the
pretty new world where Microsoft is
creating tools that only work on Linux
and this is one of the reasons why van
Stefan told me that he had made the AL
language extension available for Linux I
immediately thought well that's nice for
people running on Linux but it actually
has bigger implications and that is that
we can finally use Dev containers almost
so the other thing is that it's an idea
starting point for GitHub code spaces
because codes bases are behind the
scenes using the same technology and we
will see that in a second as well
the basic idea of a Dev container is
that you have your your local
environment so what we're seeing here is
the container that would be your Dev
container and you still have on your
laptop Visual Studio code running so
that doesn't change Visual Studio code
is still running on your laptop and if
you have something like a theme or a UI
extension as you can see here that is
also running on your laptop but if you
have a workspace extension and the a
language extension is an example of that
then it's actually running in a
component that is called vs code server
and that is running in the container so
the actual things like a terminal
process like an application like the
debugger all of that is actually running
in the container which means that we
have complete separation it's not
interacting with my with my processes on
my host machine and so on the only thing
that is typically integrated through
what is called a volume Mount is the
source code so that I'm sure that when
the container goes away I still have the
source code on my host machine so I'm
not losing any work and that's that's
the general setup how a Dev container
works so a spin up the container vs code
server is running inside of that I have
Visual Studio code running regularly on
my laptop and it's connecting through
the server component to get development
running
and again we're going to take a look at
how that works
all right let's switch back
this is where we left off before so what
I'm going to do is now to our two
extensions we installed before I'm going
to install the remote extensions
there is actually a extension pack with
four extensions coming bundled so this
is the windows subsystem for Linux which
we'll see hopefully in a minute the dev
containers
and maybe just let me yeah that's maybe
better the dev containers SSH into
remote environments and remote tunnels
so there is plenty of stuff
so
let's get this installed
and what we can do now is
create
where is it at Dev container
configuration files and that will guide
you through through wizard kind of
approach
you first need to choose the template
there are there are a few templates you
can start with there are wnd Dev
containers their Docker and Docker
containers because that works on Linux
um Gilbert needs and and all sort of
things
um
but what we need to do because we need
to use.net6 we can use a pre-built
container which has.net6
um that would be a c-sharp container but
we don't we don't really care
um and there we can now it asks us to
select which.net version we want to use
so it will be.net6 so we don't need to
install anything anymore
if you would need for any sort of things
additional features installed directly
on container creation you can you can
choose them here and that's a pretty
extensive list as you can see
and those also offer you to select the
version afterwards after you selected
the modules
well we don't need any for now so that
leaves you with
um with a Dev container Json and that's
added inside the dev container folder so
it's committed as that was mentioned
already inside the git repository so it
it gets shipped to every developer who
clones the directory so they can start
directly right away with the
configuration you create
all right so the image is is there
already you can give it a fancy name if
you want to
and
um
you can if you're familiar or just good
with Json type you can just type it down
here but you can also
um change the configuration through the
UI so what I'm going to do is Select my
extensions which I want to have added to
the dev container
um to add it to the Json automatically
and you can see it gets updated on the
Fly so we need the a language extension
and we need the Linux picture
and as I mentioned before there is one
setting we need
in-depth containers the
the net Parts is not the same like the
default setting I created
so
it's not pin.net it's in the user
directory
so that's the only change I need to do
here for the settings part and now I'm
ready to go and create my Dev container
already so
I can just click on this remote icon
here down below and say reopen in
container that will reopen my current
repository or workspace I'm I'm in or
photo whatever
just spin up the container clone
everything in there amount the photo
structure and reopen vs code
when you created the first time it needs
to clone all the images download them
um and build up the whole Docker image
and everything I prepared that already
so we don't get stuck too long
um and if you just recreate it from the
same image that's how fast it is
and you can see in the in the corner
down below that it indicates that you're
connected to a remote container
and now it's the same story again like
we we did before
um I don't have
any Al commands like the normal ones
um
I I mean I I have the full instruction
everything but I can't execute anything
so I need to run the patch again because
it will now patch inside the dev
container although we have a patched
version of the a language extension
already on the host
so it really reinstalls everything in
the container as you created so also
worth noting that's another benefit of
having Dev containers if you're doing
experimental stuff like Stefan is
showing here you're not breaking your
host machine you're just breaking it in
the container yeah it's breaking
anything but in case it happens oh I am
all right um
since I already got the symbols I can
compile right away
um
and I can also
publish
from within here the credential skirt is
not shared so I need to need to type in
my credentials again
and that's a fun
um
clear okay maybe I just typed it wrong
better anyway all right published from
within the dev container
and now to the debugging part of things
um
I mentioned earlier that there are some
problems still so I'm gonna show you
first
um
what works and then what doesn't work
if I go to the on open page trigger of
the customer card and set a breakpoint
here now start the debugger
you can see that works that's the part
that works
um let me continue and I will set a
breakpoint in my custom code
and debug again
that breakpoint still works that
breakpoint doesn't work
so what happens is
at least it's a little bit of my
assumption what happens that
um now the vs code extension the a
language extension tries to open up that
file but doesn't look for the file
inside the dev container but outside and
outside at the path it's searching for
select workspace BC Tech days that that
path doesn't exist so we we could create
a file but that would just we would need
to create all the files basically
but there is a workaround
for that
and if we have the time I'm gonna show
that
um
so if I let me just close that again
close remote connection
and
let me copy that over because it's not
that easy to type from the top of my
mind
BC Tech days
Dev container and I'm gonna explain this
as well so
um what this setting does is basically
just telling the remote container that
um where to mount my workspace folder so
instead of mounting it in the default
location which is slash workspace slash
uh whatever it was
um
it will now pull use a a variable from
from vs code which Returns the
um the local workspace folder I have on
my host machine and tells the container
to mount and copy everything over in the
exact same location which which will
result in the files having the same path
on host and and guest
so let me just recreate
three
build rebuild a rebuilt okay rebuilt
without cache three
build
and reopening container
so now
let's see there do we have the
oh probably I need to patch again since
I rebuilt everything
try one more time
now the debugging works
but there is a huge but to this
workaround it only works if your host is
Linux as well because otherwise the path
layout is different on Windows and then
this just
doesn't work
and by the way that's a great example
for the Linux World you've probably now
seen how Snappy how fast how responsive
Stefan's machine is I'm pretty envious
coming from a Windows world but then
you're happy that debugging in Al works
it's it's kind of the um the differences
of running on Linux you have clear
benefits and sometimes you're very happy
about things that are just very obvious
but in the end you're happy so who cares
all right so do you want to show the
same stuff absolutely Windows yeah then
let me just
um
you're pushing the code to GitHub so I
can use it on my machine on my Windows
machine and show you um how far we can
get there
and I did this
from inside the dev container of course
so you just take it takes a minute and
then we should
there we go
it's published okay great so let's
switch back to my machine thanks now if
you remember I told you it doesn't work
for Windows containers and that's true
you can't have a Windows Dev container
but what you can do actually is still
run it on a Windows host because
fortunately there is the windows
subsystem for Linux which means that you
can run Linux application on Windows by
now it's easiest to install with Docker
desktop but if you don't want to use
Docker desktop you can also do it by
hand and get to the same point
what's interesting here is that I think
some of you remember this nice guy who
said Linux is a cancer
but fortunately Microsoft has absolutely
changed Direction here you probably also
know that guy and they decided Well
actually Linux makes a ton of sense
um I don't know the current numbers but
until very recently the amount of
workload on Azure for example was
dominantly Linux based so it was almost
50 50 but actually there were more Linux
workloads running on Azure then windows
and I think that kind of gave a push
into the direction that maybe it makes
sense to invest more on Linux as well
and one of the things that we can see on
the client side is the windows windows
subsystem for Linux that we can use to
get that done
how does that look like
and now this is the demo that I'm
actually scared of because
just before we started Docker desktop
had an update
and I don't want to comment on any way
and what that means but we might have an
issue let's see
so the first step is a git clone
from GitHub
and we have
France B
Tech days
and that should be it right yes take
this so let's clone this
here
and it's hopefully cloning
yes
and I absolutely want to open the cloud
Repository
and now we you can see we have the same
Dev container Json
with the same configuration that
mustafan showed us before
those settings don't work so I'll
remove them
and visual studio code immediately
recognized well you have a def container
configuration file you might want to
develop in a container and you also have
the windows subsystem for Linux so it
actually might work
and now we are restarting we are
starting the dev container
and it actually might work
and I'm only surprised because it was
the docker desktop update um
otherwise I would fully expect it yes
indeed um you can now see that we have
the
full configuration set up
let's do
this
to show you that it's coming from a
different back end of course this is now
my Dev container so I also need to patch
and as you can also see here the a
language Linux Patcher is already
installed
actually a bit surprised why the a
language isn't but sometimes because
it's a little bit bigger that extension
it just takes a moment so sometimes the
reload Windows I experienced this before
sometimes a really old window just did
the trick Okay so
and anyway now we should have it
in the dev container yes I run
the Linux Patcher on my Windows host
and it restarts
and we should hopefully
see it loading
I have the impression it was a little
bit faster on my machine now I see
that's just because you're left over so
much stress yeah probably
so we have it up and running
and let's see if the extension works
it's loading the workspace that looks
good
and when it's done let's try to
debug
and what we have seen before when Toby
has shot his first demos where he would
need to authenticate all the time there
seems to be some kind of issue with the
with the caching with for the device
authentication so what we did for those
demos was actually to use an alpaca
container where we can use user username
and password authentication because that
gets saved correctly so we would need to
re-authenticate all the time
okay so here we have it and just to
reiterate this is now a Linux staff
container running on my Windows host
with the patch Al extension and I can
use it to do deployment so actually the
whole Dev container story if you felt
like man that sounds interesting uh but
unfortunately I'm stuck on my on my
Windows laptop you're not really stuck
you can just give it a try using the a
language picture you need to have the
windows subsystem for Linux and then it
should immediately work for you as well
okay so this is Dev containers now um
what is GitHub code spaces as I said
that's basically the logical next step
if you are already on dev containers if
you started with that then um using Code
spaces totally makes sense and the
reason for that is that it's basically
doing the same thing so if you remember
the picture of before we had a container
with a clone of the repository with the
workspace extensions with the tooling
and so on so basically the green thing
in the middle is exactly the same thing
as we've seen before it's a Linux based
Dev container the only difference is
that this is now running in a virtual
machine that is running on Azure so this
is no longer on your laptop no longer on
your virtual machine or wherever you're
running this but this is just a fully
managed service provided by GitHub that
is running somewhere in Azure and then
you can connect to it same as we've seen
before using vs code desktop but you can
also use it in a browser that is where I
did my my awesome demos you've seen it
all in the browser that's basically
GitHub code spaces
um so that is what we've used here and
if you're into jetbrains or want to use
a command line that also works but again
it's the same concept it's the same
basic idea that you um that you have
there it's just that the container is
running somewhere else and not on your
machine
to give you an idea of how well this
works GitHub has completely switched
their own development into code spaces I
think one and a half years ago so
basically GitHub is completely developed
in GitHub code spaces so it's absolutely
a very scalable very performant
um very
um yeah highly available environment
that you can use for your development
with the shortcomings that we've seen in
the a language extension but for non-al
or if you can live with the restrictions
that we've seen then it's it's a really
great way to work
um and not be reliant on your local
hardware anymore
but how does it look like demo time
again
there we go all right so I pulled up
that repository on GitHub and
um
since code spaces make use of the same
configuration we use for Dev containers
before
we can just start right away and click
on code and instead of cloning it
locally to my my machine I will just
select the code space section and click
create a new one
and it will create the same
the same Docker container basically the
same images will do will pull in the
same settings
um
sometimes it needs to read full images
and we're lucky enough that we can now
watch downloading container image layers
but fortunately the base image is quite
small so if I keep talking for maybe 10
more seconds then we should be done but
you can definitely now see it's the same
base technology it's creating the
container like you would create locally
just hopefully a bit faster and now I'm
done speaking
all right there we are
I hear that it's better to demo on light
layout so let me just switch to
something more bright
um
and I'll say same same
configuration in here
um
the extensions are
installing
so we need to give that a little bit
more time but those those code space Dev
containers they are not recreated every
time so you can actually reuse them that
will speed up things a little bit if you
need to hop between repositories a lot
um and it's it's on demand pricing as
always in the cloud so while it runs you
pay for it I think they have something
like 50 hours for free every month and
then has an auto time also if you're not
doing anything for half an hour then
your code space is automatically stopped
yep all right so need to patch again
and since good practice I committed all
the symbols and everything into the
repository I can build right away
and there are different kind of sizes
for those code spaces I'm probably
running on the smallest one possible so
that's why it's a little bit slower
right now I think it's a two core
machine or something with two gigabytes
of of ram so uh yeah but as you can see
it does work and I can
publish from here as well
of course
I don't want to save that
and there we go
um same limitations for debugging
unfortunately so
although I have that fix still in place
it only works if I'm running
um
on my machine on my Dev container so if
I'm running in the browser and with code
spaces it unfortunately doesn't work it
doesn't fix the debugging
as you can see it's not fixed that's
interesting wait a second I switched
Demos in between
no I I switched back to my local vs code
that's why it works
um
I mean that would have been a fast
response time for Microsoft yeah um it
would have been very impressive actually
so let me let me just debug from here
again one more time
but it's I mean I did notice you didn't
notice we could have gone away
all right so here that's the error I
wanted to show you
um
pretty cryptic but it just tells you
that the file isn't found because it
just doesn't search inside the container
but outside so yeah that's it but I
think the use cases uh isn't really
doing much of like real time or all all
your daily development in a code space
right so um rather than just um
if you need to do a quick fix on a pull
request or anything you can just spin up
that that code space do the fix because
you have language support you can
publish this
um you just can't debug but um yeah for
for quick things because the the vs code
inside the browser when you just switch
the domain to want from github.com to
github.dev
um there the language the a language
extension does not work because it needs
to have the language server components
under the hood and everything so
code spaces the way to go there it works
absolutely and I personally started with
code spaces with the same mindset yeah
I'm probably not going to do all my
coding there I'll just use it for maybe
a pull request review or taking a look
at a park or whatever and by now I'm
happily using Code spaces for a lot of
scenarios where I don't want to worry
about stuff locally typically things
that I don't need every day but maybe
once in a week or once in a month I just
have a code space configuration when I
need it I go there code codespace
started wait for a minute and then I'm
up and running and for that I find it
very very
um easy to use and I've yeah done
development for full days in code spaces
that that absolutely works as well
but just to mention it once more all
those drawbacks and all those things
that don't work are limited to code
spaces or Dev containers if you're
running native on Linux it does work I
work like this for several months now
and apart from few extensions extensions
which are not yet supported
um the a language extension works so I
can I'm working like this does work so
perfect
so let's switch back to the presentation
please thanks
um
yeah so that's what we've seen the
GitHub code space is set up but maybe
the question you have is well I'm
actually still running on Azure devops
repos and I personally don't plan on
Switching we all know they're great
options for CI CD on on GitHub as well
um but if you have invested there on on
Azure DeVos with Al Ops or alpaca or
your own homegrown solution whatever you
might still want to stay there so does
that as work work as well can I use my
Azure devops repository
um inside of a code space and the answer
fortunately is yes the only thing we
need is a Dev container feature and
that's an interesting mechanism that I
also wanted to show you this is
basically an excerpt of the same
configuration file that we've seen
before where Stefan did the changes and
there you can do something like features
which just adds something pre-configured
into your Dev container and we have a
specific feature here called external
repository the background of that is
that there was someone in a Microsoft
team that absolutely wanted to use Steph
containers as well but was stuck on
Azure DeVos repository and that guy
created that that feature here so what
it does is you give it a clone URL and
you can see here that it's coming from
an Azure DeVos repository it needs a
secret actually the guy told me that it
doesn't need it but I haven't figured
out how that works and then I have a
folder that tells me where it should
clone it
and you can find the repository here and
as we have a bit more time I'll also
show you so again we're now in GitHub as
you can see the repository only contains
a Dev container configuration but if I
do go into my Dev container that is
connected here
I do get completely different code
I have a customer list extension page
I have again my
pre-patched extension
so it's loading the workspace
and I can work on it and just to show
you
if I go into the remotes here you can
see there's an Azure devops remote in my
Dev container so I have my Azure devops
demo demo code spaces repository with my
customer list extension with the hello
world and now I can work with it like I
would used to
so let's do a BC Tech days again
do a commit here
push it yes
and if we go in here in Azure devops you
can see the change that we expect so as
you can see here using that
configuration setting I can also use
code spaces connected to an Azure
Devil's repository you have that
somewhat weird in-between repository on
GitHub that you need to create that
knows which Azure devops repository is
connected so the setup isn't as easy as
Stefan has shown you you need to create
the dev container file and put in the
right configuration options but if I
find the time maybe in the train back
I'll also try to create an Visual Studio
code extension that does this for you so
then you would be able to very easily
spin up your code space connected to an
Azure DeVos Repository
okay
um
that brings us into q a so thanks a lot
for listening any questions from your
side
ah yeah
yeah can we scale up and scale down the
code spaces as we want to show or show
you
um
go back into the code spaces if I go to
manage code spaces then I can see here
that it's now a two core machine
and then I can say
change machine type and that gives me
additional options I can click on it
wait for typically half a minute and
then I have the new resources on my
codespace
further questions hello hi so a question
about wasm
a couple years back he did some
experimentation on publishing the vasm
into business Central and run into a
problem where DC server would refuse to
publish the wasm file if it was under
dot wasn't right so I was wondering if
since obviously in your demo you did
exactly that so I was wondering if that
is something that was recently changed
if that is just a server configuration
issue to be honest I've been playing
around with wasm only on the server side
and only for this presentation did I try
the client-side PC integration so the
first time I tried this was like half a
year ago when I handed in the session
and wanted to be sure that it actually
has a chance of working so I can't
comment on anything before half a year
ago I can only tell you that it seems to
work by now I see thank you okay
further questions
yeah up there
let's see
yay
yeah I had a question regarding
departure it's actually two small one
first is it butcher open source one so
can we see what kind of magic you're
doing and a second one
um is there an option to have this
patching as a step when you generate in
your depth container so why should we
have a kind of separate patching
yep good idea
um
well it is open source it is on GitHub
um I prepared I already open it up
because if there wouldn't be any
questions I would have shown all the
details
um but you can you can look it up
yourself it's on my GitHub
um
it's linked within vs code so you can
you can open it up directly and the
reason why I did this with an action was
basically because it was like a a a
workaround or or a quick thing just to
to get me started around
um but if you if you want to feel free
to do pull requests change it around so
it happens automatically would help me
would help others so
um would be possible I think yeah in in
Dev containers you have a configuration
that is called I think on post create
command so after it's created you can
run some code that would be very easy to
patch the
um the LA extension there but that then
again only works in Dev containers if
you're running natively on Linux as
Stefan is then you would need a
different solution but yeah certainly do
a little
for me it was the easiest way to get
around possible situations where the a
language exchange is not yet loaded
correctly I can issue the reload
afterwards and it's just one click so
was easiest easy solution for me
for the questions over there
full disclosure no more shirts so only
ask the question if you're really
interested yeah
you use the alpaca containers for your
demos here does it also work with if you
have yours
the PC running in a local container
absolutely
yeah the the interesting thing if you're
running in a code space is
um that it can also
um access local resources because your
vs code might be local so depending on
what exactly you need that could be
possible
um if if the server side process needs
to publish then the container needs to
be available publicly so if if it's
basically the AL code that's running
somewhere on Azure it won't have a
direct way to access your local
container so you might have to think
about the networking but otherwise no no
technical limitations
other questions
down there
thanks for the presentation did you try
other flavors of you mentioned like
Windows and Linux but I'm wondering
about Android or iOS or trying this out
on a tablet or no I did not try I mean
I'm I'm pretty confident that all of the
Linux flavors work
um but the part beyond that I I don't
know I
and code spaces is just browser so I've
used that on my Android phone and I'm
pretty sure it works on an iPad or an
iPhone as well yeah
okay
other questions
I don't think so there at the top at the
clock oh
letting an old man run
can you raise your hand again please ah
over there
thanks
regarding the branches so Asia git
repositories can be somehow download
multiple of them because we have a
dependencies of apps you know it's
possible to just set them up there in
futures or can we maybe run some power
shell stuff that would I think there's
no setting to have multiple repositories
but you could easily run a Powershell
script
um to pull them as well and the source
code of the extension or of the feature
actually is
surprisingly easy and and trivial so if
you need that I think it would not be a
lot of work to just extend it yeah thank
you
further questions
no it doesn't look like how are we on
time Stephen
six more minutes six more minutes do you
want to show the Linux Patcher internals
who wants to see the Linux Factory
Insurance okay so go ahead all right
um so as I said already this is on
GitHub you can have a look yourself as
well you can do pull requests if you
feel like this missing anything or if
you would like to see some other
features
um but what it comes down to is
basically just one one command which get
executed and I added some code comments
here and I hope this is big enough it's
a lot of code a lot of path because what
I'm what I'm doing is I I'm reading
basically I'm getting the
um
the AL language
extension based path
where do I get it there
um so I pull I I track if there is the
MS Dynamics a smbal accent with which is
the language the a language extension if
that's installed I get the path so it's
independent where you're where you're
running this it works for for vs code
um
configurations if you if you have
different different path it all works
um and then I inside there I open up the
extension.js file and just do search
replace of of those two things so there
um there you can see that what Microsoft
does is
let me just see if I can find it it gets
the server path from it from from
another function which will return the
path to the actual executable the dot
Exe on Windows and to make it work on on
Linux I need to change that so first
parameter needs to be
um let me see
maybe you want to open vs code.f so can
you can switch to light
I try to highlight what I'm talking
about good so you can see so what I'm
what I'm doing is I'm I'm inserting the
net executable on on Linux and then at
the first parameter I set the path not
to the exe but more to the dll of the
editor Services host so that will
basically run instead of the Exe on
Windows it will run the dll because
of.net core
um
with help of yeah that configuration and
that needs to happen in two places and
I'm
um I try to make it as dynamic as
possible so the
so the uh the.net path is um is a
setting and the path where where to find
those dlls and where to replace that
that's that's read uh live on runtime
and then just some Cosmetics there are a
few two Json files the alc runtime Json
and the according Json file from
from the service host which just need
need a few a few settings it says
included Frameworks and I need to change
it to framework and that's that's all
all that happens
so those files get patched those three
files and then I issue a Reload window
and that message I tried to display it
doesn't get through because of the
reload window unfortunately so um yeah
and
I hope that those lines I read the
search will replace don't change too
much so I don't need to need to update
my code but as I said I'm working with
this on a daily basis so I'm probably
the first one who noticed and I will I
will probably update it if it breaks
um
but yeah that's that's all there is to
show so it's not that complicated
perfect so again thanks a lot for
joining enjoy the rest of the conference
[Applause]
