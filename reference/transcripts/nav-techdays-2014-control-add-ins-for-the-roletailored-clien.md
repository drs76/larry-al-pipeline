# NAV TechDays 2014 - Control Add ins for the RoleTailored Client in NAV 2013 R2

- **Source:** https://www.youtube.com/watch?v=NWn2f-8Tlww
- **Video ID:** NWn2f-8Tlww
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 87m06s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

and welcome to this presentation my name
is Becca Slovak I'm an MVP for a Navy
from Croatia and today I'm going to
present a session about control events
for the role table client in Nov 2013
our - the reason why this is our - is
because at the time when this session
was announced - look we didn't know the
date when 2015 would be shipped or if it
would be shipped in time but most of the
things if not really everything from
what I'm going to show today will be
presented extra everything new book to
present it on 2015 but most of it or
everything if it just works on 2013 r2
so essentially all of this is compatible
so what are we going to do today
actually we're going to talk about the
cross client control that is essentially
the the controller things which work in
both the windows and the web client when
I say the web client it of course
includes the web client and the tablet
fund so we are going to first see how to
create a Windows client control them
because you need to understand that
process before you can develop
JavaScript or actually the cost time
controlling we're not going to spend too
much time there we're going to see the
or actually discuss about the
extensibility framework in general we
are going to see which functions it has
how it actually operates then we're
going to create a crossed line control
it in from scratch actually it's a
simple process so you will see how to do
it from the beginning and then as we go
I'm going to give you tips and tricks
and some best practices - to learn how
to actually use different controller
names let me see who has written control
events okay
quite quite a lot of you actually who
has written JavaScript control things
okay fewer hands in the air I assume
that I don't have to explain why we need
the controller days but before I do that
you know I was really surprised here
because everybody was talking about
anyway 2015 and nobody mentioned the new
page type that we have
the it's the semi-transparent borderless
draggable style full thinner dialogue
have you heard of that page type No
so here I'm going to the RTC client and
then I'm going to click this set
password and this thing which opens is
essentially a form actually a page so I
can drag it around semi-transparent as
you can see and to prove that it is a 4
sorry a page control I can open this a
very fancy page here I can add a new
control to it user name I'll save it and
then I'll run it from here
and there it is so this is actually not
a page type obviously so we're not
talking about a new page type what this
thing is essentially control it in it's
essentially a Windows forms controlling
which allows you to style your pages
which are in fact windows forms as you
want so maybe it didn't cross your mind
but every page in nav is standard
windows form and you can do whatever you
want with it
so this session is not going to be about
that this is just to tease you a little
bit to show what kinds of things are
possible and of course you'll find the
code for this on my blog I will publish
it this afternoon I don't think that I
could I need to explain the reason why
we have control things I will rather
just show couple of advanced control
audience interactive control things
which work in both windows client and
both of the web clients so let's take a
look at a couple of advanced
extensibility demos I'll start with my
customer list this is probably showing
so many time already but still I'm
opening my customer cart page and here I
have this how to find the effect box
which is a shame essentially up a Bing
Maps control of course if I run it in a
tablet client I just couldn't make the
tab the real tablet client work off my
machine yesterday they spent like three
hours and
it's funny it's about the certificate so
I'm showing it from the browser not from
the from the client so here I'm going to
customers and then I'm opening a
customer page and here of course this is
the same controller in another
controller then that I've showcased so
many times already so maybe I'll bore
you to death this time but it's this
drag-and-drop controlling so here I have
some bicycle images and I'm just going
to drag this bicycle into here and it's
automatically saved in the database and
then I can take a touring bicycle which
is a little bit more advanced thing or I
can select for example front wheel and
drag it and drop it here so and this of
course works also from the web client
let me actually prove it
so if I go to the web client and then go
to items and then go to for example
spokes and then take those spokes and
drag them and drop them here
it works in there now available of
course this time I cannot show this from
the tablet client who knows why there is
no drag-and-drop very simple so and
again I'm not going to show how these
things were developed all these examples
are already on my blog and what I'm what
I will do here today is actually just go
and explain the process explain the
concepts and give some tips and tricks
and best practices as we go so how do we
develop a controller then it's a a thing
that you require visual studio for so
you will need to learn at least a little
bit of c-sharp if you want to write
control ins and if you want to write
first-line control things you will have
to learn quite some I would dare say
JavaScript CSS and HTML essentially the
web technologies these steps that we
have here are the steps that are
necessary for all control events so
first thing is we need to create an
assembly in visual studio then we need
to sign that assembly it is a
prerequisite then we need to deploy this
assembly it's the same process as with
regular dotnet controls or actually
dotnet assemblies you just copy them you
must put them in the Eden's folder for
the client remember one thing
control engines only work from the
client headings folder you can deploy
them to the server
technically they should be all to deploy
to the client then but you cannot deploy
them to global assembly cache that's
something that just will not work so you
have to put them in the in the end
add-ins folder so it's essentially the
three-step process
you copy the assembly to headings then
you have to define and Eddings
definition inside nav and then you have
to assign the controller then property
on the page where you want to use
so let's take a look how to develop a
very simple control it in so I'm going
to do Visual Studio I'm going to start
with a new project
don't worry about these messages I have
paths which are just too long so it's
complaining about path line so I will
start with simple control
so it's a class library here I have one
class before I can use that class I need
to reference some external assemblies
essentially need to reference the
extensibility assembly from Microsoft
Dynamics NAV so I'm going to add
reference and then I'm going to browse
and then I can click this browse button
and look for Microsoft Dynamics dot
framework dot u i dot extensibility dot
DL now remember that this DLL is version
specific so if you want to develop
controller Dean's for 2013 you have to
go to 7-0 folder and then select that
for 2013 are - it's seven one folder and
here in 2015 you have to go to a zero
folder and select essentially if you
want to have your control and to work
with all three versions even though all
the code is compatible you would have to
recompile it three times or actually
somehow reference all three it would be
a tricky thing to do and then
essentially select the right one like
you conversion your controller means if
you want inside it your assembly so I'm
selecting the one from eight zero I can
go to add and then I will just click OK
so this makes my class able to talk to
any V so I can prove that immediately
because what I want to do with this
class I want to export it to nav so I
will decorate the class with the control
add in export attribute it automatically
uses my Microsoft name extreme of UI
extensibility namespace so here I will
add a name this can be anything I'll
just call it tech days live demo it is
any string but this is the string that
you will use to identify the control
from within nav so it's important that
it matches whatever you configure in NIV
it has to be here as well so this class
one the name doesn't really matter so
I'm not changing in here what matters is
that I inherited from something I have
to inherit it from one of the available
control item types so I'm usually
starting to them with strain control
add-in
so this is the base class for all
controls that accept string as the data
source so the control that I create will
be automatically bound to a page sorry
to a source expression so if I bind this
control to data field in a table it will
automatically billing so when I change
it in my controller automatically
changed in database just like any
regular field control in in nad so my
compiler is complaining so I need to
actually add one method which is create
control method which returns an instance
of a system windows forms control you
see that it's again complaining there is
one more assembly that I need to
reference I need to reference the system
that windows dot forms assembly because
this is a system that windows that forms
application so again I go to references
add reference assemblies and then I look
for system dot Windows sorry system
windows forms I select that assembly
click OK and now this is OK I'll take it
from here and just add it here
so using system that windows conference
so what I need to do here is simply
return a new control so I'm not doing
any fancy time I'm just returning a
simple text box which is going to be
colored differently so we can really see
that it's a different thing being shown
in the page so we'll just say return new
text box and then I will say back color
is okay here to be able to color this I
need yet another assembly which is
system start drawing so I'm going to
okay and here I will just say color
light sky visible so at this stage
essentially I have all the code I need
and it's going to be data bound next
step is I have to sign this control so
it's the same process that you might
have seen yesterday if you have been at
the dotnet presentation so I'm going to
select properties signing sign the
assembly I'll create a new file you can
reuse an existing file if you have it so
it's going to be control add in no
password and that's this part so I will
rebuild this solution I have some bugs
make sure no flux syntax errors
yeah so at this stage I have my DLL and
I'm ready to deploy it so I'm going to
my folder in file explorer bin-debug and
then I have simple control dot DLL I'm
copying that and I'm pasting that into
add-ins
client so it's here my next step is to
register the control it add-in in nav so
I'm searching for the control add-ins
page and here I'll click new so I need
to specify the name of the control it is
this string that I've used in the
control and export attribute so it's
tech days live demo I'm putting it here
I need the public key token now this is
a trickier thing I'm copying my path
here I'm going to my developer command
prompt and I will just
get there and then say SN minus capital
T and then simple control dot DLL and
here I have my public key token so I
will not copy that public key token
and paste it here that's all and now I'm
ready to use this on a page let me go to
vendor card
and let's bind this to the address field
so I'm selecting the address field and
then in the controller in property I
will select Dec days live demo I'll save
this I will run the window vendor page
and here I can see that my address text
box is actually blue I can change the
value in there going go to previous
sorry next and then previous and verify
that it really is accepting and
interacting with mine with my controller
in definition so
that was essentially all you need to do
to create a simple control in everything
else is nothing but your knowledge or
your proficiency with system dot windows
that forms anything that you could do in
dotnet you could obviously do here as
you've seen in the beginning of the
presentation with that fancy fancy
looking page there is one best practice
that I can give to you which is to
include an add-in ready event at all
times in your control at him it's very
important because you need to know when
your page is ready to interact with the
control at him for example you might add
some methods or properties or even
events to your control it in and
actually events are another problem but
you might want to call a method like for
example set color to something and if
you call a method or set a property on a
control which hasn't yet been
instantiated then you will see an error
so that's why we need to have a control
at in ready event or something of the
sort to notify CL that we are now ready
to talk to to the control so let me see
why is it bad to have do not have a
control it is ready event so I'm going
here I will close my development
environment and my artistic line because
I need to redeploy then I will just open
them both again and I'm going back to my
visual studio here I will add a new
property so I will add public Bull
important and then get
returned and then actually I need an
instance of my control so we'll just
store it here private text box text box
I'm changing my create control into text
box is new text box and then return text
box so here I will return text box not
color equals color not red and set
text box back color equals value and
then color red color light sky-blue so
what I did is essentially I'm assigning
a color if I set this property to true
the color will be red if I set it to
false it will light sky-blue and to be
able to access that property from CL I
need to decorate it with the application
visible attribute so I'm adding this
application visible attribute I'm
rebuilding the solution so it has
succeeded
I will now redeploy my controller in so
I'm just going back to my folder copying
the DLL pasting it back here
and now I'm ready to actually try to set
this property from within CL so let's
start with an open page trigger I will
go to my curb page controls and then
find the address control actually it
needs to have a name so I will add I'll
call it address control it in I'm going
back to my on open page trigger and then
I will access this important property I
will start with setting it to true okay
let's see if it works so I will go to my
action from here so if I take a look I'm
getting an error so it tells me control
it in on controlling page has not been
instantiated so before I can talk to
this control I must do something
I must must let my page know it is now
okay to set properties in there so this
is this is what you need to do
now how to how to raise this controller
in red it's easy to add this event but
how do we call this at an event let me
actually first declare the event and
then show the problems with it so here I
could easily say that I need to have an
event I'll call this event so a public
event method in poker control add in
ready and of course I need to make it
application visible so this makes it
visible to CL let me again restart my
clients I will rebuild the solution okay
it's now rebuilt okay this event is
never used so nevermind so far if I do
this if control add in ready
and then actually fire that event what
is the problem can you see the problem
there are actually two problems first I
didn't yet return this text box so I'm
firing an event before I've even got the
instance so if I get this controller in
ready event in my page and write any
code in it to talk to the control the
control isn't there yet it's being
instantiated so technically I could try
to do a funny thing like try and then
finally and then this but don't we'll
just break things so don't do this you
need to keep in mind that events
actually everything in nav should be
single threaded
let's try final thing kind of changes
the execution flow of your code it
technically it would work in your
application but it might break anyway so
don't do that you need to be smarter
than this so essentially you need to
fire this event somewhere else so I'm
going to clean this up
like where I was so to properly fire
this event I need to attach my event to
some other event which happens there are
several candidates one typical candidate
is on parent change event so you
instantiate the control it doesn't have
a parent yet you are just passing it
onto the framework when the framework
puts it into the page you get this
parent changed event and that's the
situation when the control is both
instantiated and it is in the page
already the second one is handle created
event where you actually have it happens
when this is placed for the first time
into the page the reason why I suggest I
should not my trick I have to give full
credit to iron gun Kaufmann for this if
the handle created an event this event
fires only once when the control has
been first placed on a container so it
doesn't exist only memory it actually is
present on the page so if you attach
your controller in ready to this event
handler then you are guaranteed to
receive it when it's really ready to
talk to and when the control and it's
your going to receive it only once the
parent changed event might occasionally
fire multiple times so you don't want
that one you actually want to attach it
to the one that will fire surely far and
far only once so let's do that here I
will do actually after my textbox is
instantiated I will do text box and then
handle created and then declare lambda
and just here put my if controlling
ready is no no then I'm invoking it so
essentially this will fire as soon as as
the control is ready I'm going to show
another trick here I'm just going to set
a breakpoint on there and then I'm going
to rebuild this solution redeploy the
DLL
okay starting my development environment
here when you change the definition of
the control you don't immediately see
the events inside so here I don't see
the event what I need to do is
essentially rebind the control so I'm
going to the control against property
I'm taking it out and then I'm putting
it back so here I have my control adding
ready event and here I can essentially
put this important is true I'll save
that let me run my point for Windows
then let me attach my debugger to the
client so I'm going to debug attach the
process and then Microsoft Dynamics
actually I will put one more breakpoint
in here so the control is not yet loaded
but it doesn't mean it will not be so
I'm running the page okay I get my
debugger here so I can debug over my CL
code so this is now executing this is
executing but I'm not getting into this
event because it's a lambda essentially
an anonymous method bound through this
lambda to this trigger so I can run and
then at one point I will get a
breakpoint here I will just take a look
at this control isn't ready essentially
I've forgot to show what I intended to
so here it is obviously read let me
restart this page and do just one more
thing so here if you take a look if I
run this and go there this control I
didn't ready it's no it has not yet been
assigned and that's why you wouldn't
even be able to fire that so and when I
run it again here controller and ready
is not now anymore and it's obviously
firing inside CL so that's just one
important thing to remember always use
it otherwise you will never be able to
know when exactly we're ready to talk to
it let's take a look a little bit at the
controlling framework history so at this
stage I will stop talking about Windows
controls and we are immediately shifting
into the controller dens for the for the
JavaScript so in 2009 sp1 there was the
first extensibility framework so as
early as that version you could write
extensibility controls there was some
actually a lot of limitations with that
framework but it was a fairly good proof
of concept and Microsoft has delivered
some pretty advanced control agents
which used that specific framework in
2013 we have got an updated framework
which allowed us to actually expose
methods and properties and events
from our control didn't actually respond
by the events to the control in etc but
the biggest problem was in 2013 we have
the windows line and the web client and
obviously if you write a Windows forms
control add-in it cannot work in the web
client just no way to make it work so in
2013 our to what Microsoft has delivered
is a new framework which is essentially
an extension of the existing one which
allows you to write JavaScript code
essentially don't have a Windows forms
container where Windows forms controls
are placed instead you get in the
Windows client you get a browser control
which loads an HTML document which loads
your control and runs it as an HTML and
you have a framework which allows nav to
talk to that browser document which is
loaded in that browser control whereas
on the web client and the tablet client
you get an iframe control which again
loads the docq the same document and
technically does the same thing as the
windows windows so in essence you have
got you have one framework which targets
all the clients you just need to write
everything in javascript and HTML so
this accessibility in 2013 is based
fully on javascript and HTML and many
people ask is it html5 yes it is so it's
fully html5 there are no limitations it
is supporting all clients the the best
benefit of this is that it's fully
self-contained so essentially you need
to develop it initially in the visual
studio because you need to provide a DLL
with a structure of your controller then
and this structure is actually not a
class it's an interface and it's the
only purpose it serves is to actually
allow CL to know what exactly is the
content of my controller in so which
methods which events know properties in
JavaScript so you don't need this DLL
you don't need to deploy the DLL
essentially everything you have is a
bunch of JavaScript files CSS files
maybe HTML files and one XML file you
put them together in a zip file and just
upload them to the database and then
when when the control needs to run what
happens is that service tier checks if
the client already has it if not it
sends this zip unzip sit there and
creates an HTML document on the fly and
loads your stuff into that document and
runs it so no deployment required and as
I said windows forms is fully supported
on the windows client but also this
framework is fully supported on the
windows client so this was this is the
content of the cross client control it
in we need to have a dotnet interface it
as I said it needs to explain to CL
which methods and which events are there
so that's the first thing then we need
an XML manifest file this manifest file
describes the controller then it tells
the the framework which scripts you are
using which CSS files you are using
which images you are using it allows you
to put some script code directly in
there into the manifest and it declares
the size and like the flexibility of
that size of the client area that the
controller is going to consume so
essentially that's the manifest file
then you have JavaScript code we have
different ways of putting JavaScript
code into the controller then and then
optionally we may have images we can put
embed images into the resource and then
on demand
they are extracted from the zip and
loaded onto the control and also style
sheets if you want to style your
controls you will need a style sheet you
can also put it into the actually
somehow into the manifest or actually
into the JavaScript code which
instantiate your control so it's up to
you there these two are really optional
so after you develop the first stage of
across client control it in which is
essentially the same thing as what we
have seen so far
you start with the visual studio you
create an interface you create this
controller and export attribute you add
any methods and any events you decorate
them with the application visible you
sign it you deploy to the client just
for CL to be able to see it and then
after that you have four more steps
first you have to create the manifest
then you have to add the resource is
necessary you need to zip those
manifests and resources into this zip
file of which has a specific structure
and then you need to import this
resource file into the controller in one
tip that I'm going to give to you and
actually this is going to be a template
that you can download from my blog
create a visual studio project template
which has all that already in place and
then you really don't need to do
anything you just start a new project
from that template and it immediately
has all of this content inside and
another one is run Visual Studio as
administrator because then you will be
able to auto deploy from Visual Studio
to do Microsoft MX nav client so let's
take a look I'm going to develop a
simple java script control in using this
simple template that I've prepared so
I'm closing Visual Studio and I will
start it as administrator
I'll click new project and here in my
visual c-sharp templates at the bottom I
have some custom templates that I've
developed so here I have this Microsoft
Dynamics NAV 2015 simple extensibility
control the name which makes me it
through this error message because it's
just too long to be a path so I have to
shorten the name of my project I'll just
call it Dec days simple okay so when I
click OK
what I have here is this I simple
extensibility control interface I
already have all the references I need
to the extensibility framework here and
in this interface I have some methods
and events so first I have own
controller and ready even though with
JavaScript controls it's a little
different still you need something like
that you need to inform CL when you're
when it's ready to talk to JavaScript
then I have one method send data to
control when nav needs to send something
to control it can use this method and
then this event data on data received
from control which is when JavaScript
needs to send something to the client I
will explain those two things a bit
later and here I have this control at an
export I will just call it tech days
simple template demo so you put your
name there and you're almost good to go
here I have resources I have my manifest
let me see the manifest so manifest
references this script control Jas which
is essentially where you need to put
your custom code so you open this script
folder and then control J yes this is
where you put the control okay
then manifest also reference is a
default style sheet so here is a default
style sheet which just makes the font
family Segoe UI and font size 9 PT
so you can actually use this default CSS
to add your CSS code into it then in the
manifest I have this script URLs block
here I can load external scripts so here
I'm loading jQuery and jQuery UI from
Microsoft CDN so this is URL which is
guaranteed to work Microsoft is never
going to change it or at least that's
what they say so you you can download
those scripts from the internet
alternatively you can download them and
put them into your scripts folder and
reference them from there in that case
they are not loaded from the internet
they are loaded from the resource it
will perform better especially in the
situations where your
your users are not expected to be
connected to the internet okay I don't
see too many of those but still this
might be a requirement so you can really
download them and put them as scripts in
there then I have my script block here
this script block essentially attaches a
function to the document ready event in
jQuery where I call initialized control
function it is in my control J s so here
I take a reference to this control at
end this is the container control the
iframe control that hosts actually it's
not nice Ram it's actually a div within
the item iframe so it is the container
for where we need to put our stuff and
then I use jQuery here to append some
nav control so here is some blank
template what I'm going to do here is
put input type equals button well click
me on click equals alert
let me see that I just take this on
click out
so don't click those in here
nice to them I'm sorry it's it's adding
too many of those I'm just going to make
it simple I'm just going to add input
type is button and then well is flick me
and then just close it I don't have too
much time it's really a simple name so
here I will just save this control JS so
let's go back to manifest after it
initializes the control it inserts this
HTML into the page it calls
Microsoft Dynamics NAV invoke
extensibility method it essentially
raises an event trigger in nav by name
so here I say on control adding ready it
is going to be this event here ok so
that's the last thing that happens in
the manifest and then here I have
requested height 200 requested width 200
vertical stretch false horizontal
stretch false this is going to consume
200 by 200 block which is not going to
be resizable you will not be able to
make it bigger or smaller for that
matter so this is that's it so I will
now build this solution it will deploy
it to my two nav it will print the
public key token here so I can start
immediately with just declaring it as a
controller in in nav so I go back to nav
control
I'm creating a new one
I didn't copy it obviously so he copy
and then paste then let me use this
public key token from here I'm putting
it there and last step is to actually
create a resource file so I'm going to
this resource and then I'll select open
folder in File Explorer I will select
all the files inside and add them to
resource that's it and then back in my
control ideas page
I'm clicking this import button action
sword and then I'm going to this folder
selecting resource that's it and click
open so the control gene has been
imported so if I go back into my nav and
create a new control and bind this
control it in Dec days simple template
demo okay I can see that it has those
two events controller and ready and data
on data received so on controller and
ready I will just do message I am all
ready now click me five thousand five
days okay let me run this page so here
it tells me that it's ready click me and
here I have this HTML button click so
this is how you can inject your HTML
code into this control add in div and
essentially whatever HTML you are able
to develop you're going to put in there
and everything else is just again your
knowledge of JavaScript HTML and CSS
just like with the windows forms so I'm
not going to talk today about how to
develop HTML how to develop jace
JavaScript how to develop CSS I'm going
to stay in the nav backyard so we're
going to talk about interesting things
of the framework itself and those
advanced demos tutors can download later
on one thing which is important not good
to know but important to know you cannot
bind the JavaScript control to source
expression or in fact you can but it
will not do anything in 2013
r2 it might crash the client in 2015 it
won't crash the client but won't work
either so the reason for that is that
javascript and nav client are running in
two different applications they are
really two different applications so
even if it's the web client
you still have an iframe which loads
another document so it's not the same
application and to make the application
stock
the easiest or actually the the most
stable way to do that is asynchronous so
you have a synchronous communication
between nav and the JavaScript control
and the effect of that is that you don't
have actually since nav cannot respond
to asynchronous events it has to stay
single threaded when you call JavaScript
you never get any return value back so
if you send something to JavaScript it's
a one-way road so you essentially if you
want to send let's say source expression
to JavaScript you call it but you cannot
expect a return value from JavaScript it
it's not allowed you cannot have a
function to return a value from
JavaScript to you
also when JavaScript calls an event in
nav it's also a single way street so
when the event fires you can't have any
by reference parameters you cannot pass
anything back so it means when I call
JavaScript and I expect something back
then whichever method I'm called should
call me back and give me any so-called
return value and the same way the
opposite way around so if javascript
needs something from nav it needs to
notify nav i need this and then nav
needs to call a method in javascript so
essentially this is what you need to do
when you need to pass from CL to
javascript you call a method when you
need to pass something from CL sorry
from JavaScript or CL you invoke an
event so let's take a look at how we can
do that I will close my
development environment and my world
talent and I'm going to open develop
environment again so let me change this
here let me change this from input type
button click me to input type text and
then value is not going to be click me I
don't need any value but I need
unchanged is and then I will invoke a
method so I will say call actually send
data to nav sorry yeah on change and I
don't if I didn't even call the function
so I need to actually call the function
so it wouldn't work anyway yeah thank
you to see it better than I do so
function send data to nav so here let me
just call Microsoft Dynamics actually
copied I never remember it by heart we
invoke extensibility method
and then
it's called scent sorry on data received
from control and I need to pass
arguments which are defined by this data
event handler so let's take a look at
this here I'm passing object data which
means anything whatever so I will just
pass a value since it can be many
parameters I have to put them in an
array so I will just pass a string I
will call it hello world at this stage
so I will build my control
and also let me do something here alert
and then data
this is send data to control this is the
method that nav invokes so here I will
say C al says and then whatever it says
so written let me redeploy that and let
me go back to nav I will modify this and
here I have own data received from nav
here I'll say message JavaScript says
and then data and then I will
immediately call it back so I have to
assign the name here control so I will
go to her page for send data to control
okay
so that should do if I run this page now
yep that's true Thanks so I need to
upload a new resource so I'll delete
this resource from here we'll address
this issue later but I have a trick for
that so I'm going to control it ends
and then selecting this simple template
demo import now it tells me there is a
resource inside already you need to do
something about it so like yes I'm okay
to override it
I'm clicking resource and then I will
run the page so let's take a look I'll
enter something send data to map is
undefined so I will not run splits on
page anymore obviously I made a typo
somewhere yes its function name it's
here it's lowercase and it has to be
JavaScript there's also case sensitive
so I will just redeploy the resource
join again
so I'll change something here and here I
have CL says okay I've got it and then I
have JavaScript says hello world so
that's how to exchange data it it might
hurt a little because it's not the way
we used to so you want to have data
bound controls there will be a lot of
communication actually one-way
communication so we'll have to have some
triggers and events sorry methods and
events that you will have to call but
that's the only way to do that and now a
typical question that I hear often is
about this control here see it's kind of
ugly because it has those eighteen
hundred's
tip tooltip popping up and if we run
that in the web client okay so it has
expired but I will restore it
okay so here it's different it looks
kind of 20 at least like 2010 so the
question is can I do that with my
controls because obviously this is a
Windows forms control and JavaScript
control in one single control so the
question is can you do that and the
answer is no so Microsoft has hard-coded
it actually so instead of allowing us to
do the same thing maybe they do that in
the future but for now it's essentially
just a trick that they can do but you
cannot so maybe if you would D compile
their assembly and see how they have
done it you could do the same thing
that's that might work but there are no
clean ways to do that so so far we have
seen basic interaction between the
control and and your page and we have
seen that we need to write some
JavaScript and we have seen different
ways of adding job javascript so we have
three ways first one is to put them in
the manifest block the second is to load
and URL from manifest just like I've
loaded jQuery for example and the last
one is to load from resource that's it
so all of these have their pros and cons
however there are interesting things
that you could do if you do not just put
your JavaScript code into the control
imagine like for example if you want to
automatically update like you want to
deploy the new release of your control
to all of your customers or like whoever
uses your control if you have to deploy
the resource and then depend on
everybody loading the resource it will
be kind of not the best way so why not
for example putting it let's say on your
web page and then essentially having
your customers automatically update the
resource actually the resource downloads
the script every time it runs so that
could be one way so how about that how
about another thing how about loading
the whole JavaScript the name
how about like for example loading HTML
code dynamically like not even having to
deploy anything to your your customers
but actually having for example CL code
inject JavaScript or HTML code or CSS
code javascript is an extremely flexible
language it's probably the most
beautiful language there is right now it
allows you crazy things so and
essentially we could have CL pass on the
full content of your control so why
would you have to put anything in the
resource in the first place because then
you have the updates problem why
wouldn't you just control everything
from CL or why would you have to deploy
15 different control events why wouldn't
you just have one and then supply your
code into it at the runtime depending on
certain circumstances or not so these
are all the possibilities so what I'm
going to present here is an advanced
controller in template that I've
developed for this presentation and also
it's going to be available for you to
download it we cannot really see can you
see those so I'll start with this bottom
at nav so when nav loads the control it
will call the initialize control method
in the framework then this initialize
control will call an another method
called create control it's an internal
JavaScript thing only so essentially you
override this create control by
supplying your HTML code there and that
HTML code can come from an ad if you
want then this create control fires the
unready to receive control definition
this happens in nav so nav has
essentially a chance to supply HTML and
CSS and if it wants to supply something
at this stage it calls the send Control
definition to JavaScript and it sends
the HTML and the CSS okay so at that
stage essentially this end control
definition
puts whatever you pass into it directly
into
Paige and then it calls the on control
control control rendered it tells your
CL okay now I've done my job now you're
ready to talk to me that's the initiator
initialization stage the next stage is
the user interaction stage so user
enters data into into the control or
essentially this would be the trigger
like you read something from the
database and then you need to pass that
on to the control so you call this send
data to control and then it does
whatever it needs to do and then users
user enters something in the control or
changes the context in the control then
it calls this unchanged data event this
is very similar to the concept that we
have seen and we have one more stage
which is essentially dynamic execution
stage so imagine that CSS the CL wants
to update the CSS so for example I want
to change the style of something on the
fly I just call this update CSS and then
it updates the CSS in the page and then
we have possibility to execute code on
demand so I call from CL I call execute
JavaScript code I pass a string into it
and JavaScript executes that string and
returns the value to me by calling the
on JavaScript code executed event so
that's the advanced control it in
template that I'm going to present right
now which will also simplify this
development process
so I will just start with this file new
project and then again the length thing
I'm going to select advanced control it
in and then I will just give it a name
tech days advanced template I'm out of
space Dec days advanced let's take a
look at the content here so still
still I have resource I have sprits and
I have style sheets however I have two
scripts I have this extensibility
framework which does all that stuff that
I've shown here and it has this control
jeaious which is essentially where you
need to put your code so you need to
extend this one it has the create
control so here you can put some code
into the control if you want this is
invoked from the initialization here so
it essentially inserts this div and then
calls your create control thing which
then essentially passes some HTML that
you want into the page and you have the
data received from CEO also here when it
initializes the control it raises the CL
event it's essentially just a friendly a
name that then Microsoft Dynamics NAV
dot invoke extensibility control which
is so simple that Microsoft has even
made a typo in the first release that it
wasn't called invoke extensibility it
was called extensibility so to make it
simpler you have this raised CL event
which kind of is friendlier so this
raised CL event essentially calls this
extensibility so
here we have this data received from CL
essentially when we deploy this control
I'm just not going to spend too much
time developing from scratch but I will
just show this page which already uses
it so here the control does nothing by
itself it's just a framework where CL
does everything so here the first thing
that happens is on ready to receive
control definition here I'm passing two
things I'm passing some HTML and I'm
passing some CSS so essentially when
JavaScript tells me I'm ready to receive
something from you
I'm calling this scent control
definition to JavaScript so it has two
variables HTML and CSS let's take a look
at this same control definition method
here so send control definition to
JavaScript receives HTML and CSS so it
appends the HTML to your control and
then it calls the update CSS method this
update CSS inject CSS to the body
element at the end which makes sure that
it overrides any existing CSS that's a
nice thing about users you can override
existing CSS as long as you want so this
update CSS is also the function that you
can call directly from from CL if you
want to change and then when it has done
that it raises the event called
on control rendered and then I get this
on control rendered event I can do
whatever I want from there essentially
this is the own controller in ready it
tells me everything is a stage is now
done you are ok to talk to me and then
let's take a look what kind of content
I've passed into it here I have some
span which which is called ID has ID
caption and obviously I'm using that ID
here to style it in color red and then
the caption says enter some data
then I have some input text where I put
the unchanged event which is send data
to CL
okay this send data to CL is essentially
this method here so I'm calling it and
I'm passing the content of my control so
I call my control dot Val it's again
jQuery function which returns the value
of my input box and essentially send
data to CL is going to call this
function here it will raise an event
called unchanged data and here I get the
unchanged data event so what I will do
here I will update CSS I will color it
to red and that will also execute
JavaScript code it has ID of 1 so I can
know exactly which because there can be
many different invocations of JavaScript
code this is just a tag it is completely
arbitrary and here is the JavaScript
code I say alert hello world and then
return some value called test okay then
let's take a look at what this executes
JavaScript called method does so here is
the method it essentially creates a
function out of your code and then it
invokes the CL event it passes the ID
back and executes the function which
returns whichever value it should return
back to CL and at that stage I get this
on JavaScript code executed and it tells
me JavaScript execution completed it
tells me which ID it was because you can
call it from many different places and
it says it has the result this is what
it has received from JavaScript
basically the result of the execution so
I run this page up sorry no not this but
this this is my enter some data I will
put hello Dec days 2014 and I exit from
here it says hello world so essentially
it's this unchanged data thing this is
the alert hello world
okay and here I can say okay it tells me
JavaScript execution completed ID equals
one result equals test I can change it
now without redeploying the control so
here imagine that I don't want I'm just
going to make it simple I will not say
hello world I will say you know this
demo and let's change this not green but
to blue and I we can start off not with
red that way yellow run that and here is
my yellow and it turns to blue and I get
this
so essentially you can fully control the
content and the execution of your
JavaScript purely from CL don't need any
any redeployment or anything and your
fully flexible like you can really
develop whatever you want without having
to redeploy stuff occasionally now where
you where it takes this HTML and
JavaScript that it executes and CSS is
completely up to you
you can put it into the blob you can
download it from somewhere you can just
hard code it in C al if you want you
wouldn't do that I see you like that yes
that you wouldn't do that you would
probably store it somewhere but it
essentially sky's the limit so some
framework like that can really help you
achieve a lot now final I think final
tip for this session is how to handle
the situation so you have seen me I've
always had to create this control I had
registered as this control so instead of
that how about actually auto registering
the control so you have company open
trigger in code unit one it can call
your code unit which is called register
controls which inserts the control
definition which is name and public key
token into the client add-ins system
table
and it also downloads the control @n
definition resource from your website
and streams it into the resource blob in
the time so and of course it does that
only if it needs to so actually let me
let me demonstrate sorry let me
demonstrate this last tip how I would
develop that so I'm going to my code
unit register control at ends
sorry register custom controls so I'll
start off with control add-ins okay so
here I will actually delete this
advanced extensibility controlled the
control demo I think that's the one let
me just make sure this way to make sure
is to just check the page
so I'll just delete this one I'll just
click delete okay so the control is not
there if I attempt to run it it should
not work okay now it has it cached on
the client-side I would have to close
the client so let me demonstrate that I
will essentially go to this and here on
run I will just exit immediately then I
would close this page I run my page from
here that's the page so it should fail
okay it tells me that it cannot load the
control because it does not exist I'm
closing it again I'm going back to my
code unit and I'm deleting this exit so
here I have register control what I do
here is I call this local method
I passed the name of the control the
public key token these are defined by
you so you can just hard code them in
here version description they are
arbitrary and here you have the the
resource file which comes from Internet
okay so it's a resource demo from my
blog so I passed that on to register
controlling if the client add-in exists
it doesn't execute this so if there is
if the client exists doesn't client that
it does not exist it actually first
inserts sorry let me increase the size
because I'm not sure if you can really
see that from
so it first inserts yeah I'm not used to
that magnifier but I've seen Microsoft
do that in their presentations at school
I have to practice more so it first
inserts the control it in and then if
you supply the resource download URL it
calls this download control and now this
download control is also smart so first
it checks ok if we have if we don't have
this control at in then it just exits
because it cannot import a resource for
a non-existent control then if it has
value okay it exits so I don't want to
download every time so if I have a value
in there I'm keeping that ok but if I
don't have a value in there then I
essentially do the trick from
yesterday's presentation I instantiate
an instance of web client on the server
side I define the URI out of my down
download URL I download it into memory
stream then I create an out stream in my
resource field i copy my memory stream
which contains my zip file into this out
stream and i modify the client ID so
essentially this is all you need to do
so I'll save this and I'm going to run
the page you remember it didn't run last
time so I'm running it it should fail
because I don't have the control
and why is it taking so much time to
point
is it resource download and there is no
internet or what did I do they click run
at all no I didn't like that for ages
let me just click run okay I could have
waited you know and there it is so and
now you know if I go into control it
ends and find my control and just click
remove so I'm removing the resource okay
the next time I run it will download
because there is no resource so it
indicates okay you need to get the new
one the latest version from the URL and
you get it in here and essentially
that's same thing so that was all I had
to show I think I was a little bit too
fast we have 20 minutes left but it just
gives us enough time for Q&A so for more
information follow my blog I have
blogged quite a lot about about control
events and there will be more all of
this stuff everything that I've shown
here today is going to be on my blog in
a couple of hours and then you can take
it play with it and abuse it to like
your to the maximum extent allowed under
international copyright laws and I give
it to open source too so let's talk
about your questions yeah
can somebody if this if the question is
smart you get a shirt if not I keep the
shirt
right yeah okay but there were two
questions up there I would like to
address them yeah
let's get this one first do we have
enough time so everybody positioning and
sizing of the controls inside the page
so that's a very good question if we
talk about controls in Windows forms yes
yes windows forms if you have seen my
trick at the beginning this how I called
it semi transparent borderless draggable
something whatever with tricks such as
that you essentially can access anything
on the windows form and resize change
styles change color you're sure so
essentially you can use that to to do
fancy stuff with windows forms with
JavaScript you're very limited because
you cannot access the the parent of the
JavaScript if you're in the Windows
client and you host the JavaScript
control there is no way JavaScript could
talk to Windows forms and do something
about it so really no way you would have
to have another control and then from
JavaScript call that control but it'll
kind of violate the reason why I have
JavaScript in the first place and if
you're in the web browser then you have
a security issue because you have an
iframe and again security rules will not
set it will not allow you to talk to the
parent page so you're very limited you
can define the size so you can say I
need 200 by 100 frame and I want it to
be resizable for example like I want
horizontal stretch yes or no or vertical
stretch yes or no but that's it
so no positioning no no precise
positioning if you really need precise
positioning for whatever reason then
maybe the best thing is to simply
consume all the space available with
your control not put any nav controls
and then just do everything in
JavaScript but that would kind of be
okay we had two questions up there oh
yeah in the middle oh yeah okay I was
just wondering moment you can take
control a didn't turn over Peter didn't
catch yes that's true so you cannot add
a control at into the repeater I was
just wondering is that something that
might change or is so honestly I would
not expect Microsoft to change that
because it's not that it would be
technically even difficult not
impossible but it would kind of allow
you to break the repeater itself because
then you could just put anything inside
of it and then you know repeater kind of
could get like all scrambled on on the
page
however again since it is Windows forms
control you can access it once you place
your windows forms control in there it
can talk to any other control on the
page
repeater included it's essentially
nothing but a data grid or not really
data grid it inherits few levels from
the data grid but then you can get that
control you can really find it by name
because you can see all the names of the
controls inside the page and then you
could play with it yourself like you
could see like find the cells that you
need to put something of your own inside
like the background color for example or
something like that that would be
possible yes but it's I I'm pretty sure
Microsoft would kind of frown upon the
stuff that I've shown at the beginning
of this presentation and this thing that
I've just explained but it is possible
yeah
okay I would I would really like there
is a gentleman in the in the last row
here I would like him to be the next oh
okay yes we have a questioning okay let
me ask you I apologize actually whoever
has asked a question gathered the shirt
later in here okay I count on your
honesty okay records you cannot send
records but that's not because
JavaScript will be unable to handle them
it's because nav doesn't allow you to so
you can't you cannot assign record
variable or any nav built-in complex
data type to anything outside the CL
domain so you cannot set records but
other than that I could say just about
anything you have seen that I've been
dragging images from my folder on to the
JavaScript control which has somehow
stored them in the database so it is
really anything
it's whatever nav received receives a
system that object it's some kind of
serialized whatever probably some binary
data that you have but really anything
the JavaScript can handle in memory it
can pass on to to anything so really
really anything there was a question
here in the last road like that on next
so the short question is about the
manifest
so manifest contains information about
the within the size of the window to
consume for the controlling either any
way to retrieve this information from
nav that's that's a good question I'd
anticipated this one it's actually not
that I know of so as far as I know there
is no possibility of you two retrieving
the size what you could do is you could
call JavaScript and then call those
measurements functions inside jQuery to
tell you the size of the client that it
consumes that's something that you could
do but what you cannot do is you cannot
influence that I know so maybe you know
it doesn't mean it's not possible maybe
it isn't maybe it's even simple I never
try that I I know that you cannot
dynamically let's say inject something
into the manifest so that thing you
cannot do but if there is some fun fancy
JavaScript framework which allows you to
kind of precise those controls with the
parents in respect to them which I don't
think so because it is really an iframe
I wouldn't expect that to be possible
but yes I just say I don't know thank
you very much is there a small way to
debug the llaman script or browsers tend
to interpret the Yahveh script
differently so yes there is a smart way
to debug it just you I don't know of a
way to debug it live so you would have
to have a test project and then
essentially it would have to have your
HTML page which essentially hosts your
control and then you debug it using
Internet Explorer
development tools or whichever Chrome or
Firefox development tools so you could
do that and then when you debug and test
it you actually deploy it but live
debugging I don't know how to do that
again not to say it's not possible just
I don't know sorry
there we go so you could use the web
client really thanks yeah
smart smart trick this deserves a shirt
out right so we had a question here in
front of control from the Neph time as I
think yes you know I'm really not a
JavaScript guy
I don't know it inside out I I think yes
as far as I know there are many events
exposed to jQuery so you could respond
to too many fancy events does anybody
know the question was do we have key
events like on key press onmousedown
yeah there we go
I won't have that many shirts you know
therefore the client add-ins windows
forms we have the ability to use big
text and stream and external port into
the ad and I can put the record to my
control is the report ability to do the
same trick with jQuery yes there is I
would just not
I wouldn't use with jQuery you're better
off with using JSON so you would have to
stream it somehow into JSON basically
turn your XML into Jason that shouldn't
be difficult now absolutely you can load
let's say kendo UI grid or like whatever
grid in JavaScript show it on your page
and then load whichever kind of data it
expects you could pass it from nav I'm
pretty sure could even do that with XML
and directly it's just that you know
again it depends on the control that you
are using but yes it's possible
sorry we have ten minutes left so just
let's let's do it
this seems to be an interesting topic
right I want to ask and then you put a
new event that's a big problem actually
so if your interface definition changes
so you define it once and the purpose of
that interface is twofold first is to
explain to JavaScript what is inside but
not not really for that primarily it
explains to CL which let's say events
are in there because it means to add
events events are automatic so if you
change the interface add a new event you
have to go unbind the control which
kills the event triggers that you have
and then rebind the control which just
gives you the empty triggers so it's
that's why it's the best thing to do is
just follow the PRS principle slide do
not put any code into those triggers
just call simple functions from there so
in the worst case you would add
functions to the page and put your code
there and then just call like if you
have ondatareceived trigger
you wouldn't code this in the
ondatareceived you would put that in the
own data receive method and then from
own data received you would call own
data receive and then it's easier
because then you just put that code back
but this is painful so yes this is a big
problem maybe they fix that somehow with
like developing environment tools
refresh interface for controls or
whatever that would be perfect but right
now you have to do it manually
and I was happy to hear that
Microsoft's also deploy the add-ins but
yesterday I heard they are not that's
not always and now i've the question how
to make sure that all you have the same
version of the client and so there would
be there would be ways to detect if
everybody has the same version because
your control it in is nothing but a
dotnet thing if we're talking about
windows controls because the problem
that you just put is not a problem for
javascript because everybody has the
same version because it comes from the
resource you cannot have an older
version unless you have you keep your
world able client open for millions of
years in which case it would but with
Windows forms controls what you could do
since all of them are really just
nothing but dotnet controls not net
classes each of them have a type and
they are already signed with strong name
what you could do is do can load type
and test whichever type you need so you
can test if everybody has this version
for type so you would have to use
versioning so we would have to attach a
version tank your assemblies but when
you do that you could easily say like if
can load type and then you put the
latest one then you do your stuff and
then whoever doesn't have the latest
stuff you throw an error you say like
sorry don't contact your administrator
or whoever so that would be a trick
we had more questions we don't have any
more questions come on lunch will wait
okay
and the event trigger in NAV seems to
offer in general only one parameter is
there a way to extend that yes using the
data you can put as many as you want so
I've used I've actually used to in my
demo here so when I was I was sending
this on JavaScript executed it had two
parameters so you can put as many as you
want
yeah okay yeah no you just need to
define your your delegate so you need to
define your delegates for your events
first you declare a delegate method
which is a template for the event and
then you create an event from that
delegate so if you if you needed it like
an event with five parameters you create
a delegate which has five parameters of
specific types and then you SM simply
just create an event from that delegate
so it's simple it's take a look at the
code when you download it and you will
see how it's done here anything else
more questions okay
thank you very much and have
