# NAV TechDays 2016: JavaScript Architecture - Turning Pain into Gain

- **Source:** https://www.youtube.com/watch?v=_uWDgD8D22c
- **Video ID:** _uWDgD8D22c
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 87m01s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

good
morning morning morning come on yeah
wake me up wake me up
please uh thank you for joining this
session called JavaScript architecture
turning pain into gain uh my name is
Vios babich also known as Vio um I've
been active in this community for quite
a long time this is my sixth time at
Tech days and I'm really glad that this
time my session is not called uh black
belt session so far all of my sessions
or nearly all of them have been called
Black Belt this or that however me being
a black belt guy um I couldn't just you
know not do a black belt thing so there
will be you know even the session is not
really black belt I will have to uh do
some crazy things okay calm down okay
good um you know those numbers session
numbers 2 3 400
who does okay so um this session has um
actually was originally planned to be
level 300 which means Technical and then
uh discussing with look and everything
um we decided to make it level 400 and
then since I'm at level 400
already what does it take to get it to
level
404 so this means that uh I'm probably
going to lose you somewhere along the
way actually I'm probably going to lose
myself
so let's try to see how far we get
without going crazy
um you know if we would have to make a
comparison between Cal as a language and
JavaScript as a language this would be
Cal you know very serious very official
very few things it can do and it doesn't
ever do anything that it wasn't supposed
to do and JavaScript will be this a
crazy guy like doing whatever you wanted
to do so it will turn around do
absolutely anything and will not
complain mostly so um that's the guy
that we need to live with you know these
two guys do not cohabitate well you can
imagine that they're they kind of do not
really like each other but since we have
to do control edin then I believe we
need to find a way to somehow reconcile
them um I assume that all of you here
are really because of control Adin
right that the reason that you are here
is not because this session sucks but
the other sucks more so let us be
here okay hopefully it's not that so let
me see who does control a
dance okay good so there there will be
fewer of You by the end of the session
okay so um the session is called
architecture why architecture
like what does it even mean architecture
when we talk about control edins this is
a controled in right like a small piece
of screen where you put something like a
colored field or a button or whatever
what is architecture what does
architecture have to do with it well if
you think of this then absolutely
nothing then you're good to go you can
leave and just join s session um however
if your
users spend their day in something that
looks like this or maybe like this or
this or this or this or this or any of
those zillion things which consume
entire screen and do many more things
than just um showing couple of values in
different
colors uh and if for your users doing
their work in this or that doesn't make
much sense then we absolutely do have to
talk about architectures
because with JavaScript uh architectures
are intrinsically very difficult when
communicating uh communicating with a
language which is as rigid as
Cal and we will see uh what kind of
problems we can encounter and how how we
can uh solve those problems because if
we do not pay attention on architectures
then our JavaScript code and our CL code
that talks to it will probably look
something like that so I assume this is
not the kind of architecture you would
like to have in your solution trust me
most of JavaScript things I've seen look
like
that um imagine for a second that your
users do have to spend their day in a
full screen thing that consumes entire
attention of them and entire screen or
better part of it and provide some
different user experience to them rather
than lists and pages and you know role
centers that they are used to so uh can
you imagine that did you okay what do we
need to achieve that we need two
things right first thing is a page
obviously yeah a page object uh and it
shouldn't be more complicated than that
actually you know this is as complicated
as it will probably get and the second
thing we need is code actually we need a
lot of code more yeah we need heck load
of code uh the problem
is you know these two guys the left and
the right guy do not really coexist well
either code should not live in Pages
code has nothing to do in Pages perhaps
something like this does belong in a
page um okay I'm overreacting you know
um this is not uh the only thing you
would ever want to put in in the page
the kind of code that should belong in
pages is is user interface code that you
cannot possibly put anywhere else
because it wouldn't work
anymore or some infrastructure code
which helps connect page UI logic with
the business logic but business logic
itself has nothing to do inside of pages
and this is the first obstacle that we
will find there are many many more
obstacles JavaScript as a language is
completely isolated from uh Cal when you
make a call to JavaScript it's
asynchronous from the perspective of Cal
and the opposite is also true when you
call from JavaScript into cal cal seems
to be asynchronous even though both of
them are perfectly synchronous
JavaScript is synchronous as well even
though it doesn't look that way uh both
of them perceive each other as
completely asynchronous which means you
cannot make blocking calls from one to
another it means you can only do ping
pong like send a request and then wait
for response which influences how you
write your code tremendously because
your code cannot be done the old way if
you attempt to do the old school code
the way you have been doing Cal only
inside of especially classic client and
then of course also roll tailor client
it will be just huge mess of spaghetti
that will be very very difficult to
disentangle so I will be showing a lot
of examples here I will be using visual
studio and uh all of the demos that I
will show will be done using the
template which you can download from my
blog the template simplifies building of
control Adin so it builds the control
Adin Zips the resource file creates the
controller in inside of nav um uploads
the resource file and if you have
multiple different control Tings it will
do the same for all of them it will also
create the folder structure and the
Manifest file for you so it's a very
useful thing if I don't see 600
downloads by the end of the day I will
be disappointed so go um there will be
two parts I will be optimizing two
things I will be optimizing the
framework which is a fancy word I will
explain what I mean by framework and
second thing is I will be optimizing the
back end so let's talk a little bit
about optimizing the
framework uh
click let's start with a problem
statement
controll
adents tend to get heavy and tend to
cause performance issues maybe not big
performance issues maybe tiny
performance issues but the slower the
internet or the slower the device that
you run that on you will perceive them
more they are also rigid because you
have to write a CP interface or visual
basic.net interface that defines the
functionality and Cal is tightly bound
to that that definition which means if
you change anything in the definition
like you come up with maybe a new event
from JavaScript to publish in clal or a
new method in JavaScript that CL can
call into then you will have to change
this assembly and then deploy it to
development environment then refresh it
which means losing all of the event code
which is
painful and um I like to avoid those
things but first let's let me prove this
with I've just said even the simplest
control at ins can be fat and ugly so
let's take a look at the first demo of
today I will just go here into my uh
Universal client I will click this Tech
days 16 icon and here it is that's my
controller then very fancy right
um does nothing right the only thing it
does it shows two pictures it prints
some text text uh let's take a look at
the code actually so here I have my
script I have jQuery of course most of
control Ence will use jQuery Microsoft
uses jQuery so it makes sense and here I
have some very simple code so I append
some HTML when the document is ready and
blah blah blah so not much but if you
take a look into the folder if I open it
and take a look at this this resource
file is 374 kiloby big
uh why does this matter it matters for
several reasons first every single time
the control is loaded even if it's done
multiple times per one page it will be
copied from the server to the client
extracted from the server on the client
actually client being asp.net and then
loaded in a separate instance of an
iframe so it's a lot of infrastructure
work every time that you use a controler
in it refreshes them all the time so
even if if you don't change it it will
send it again and 374 kiloby might not
seem that much but trust me in the world
of Internet it is and especially if you
want to do some uh fast showing or
opening like popups or something like
that depending on what exactly this
controler in does it may take quite some
time uh I've uh fought with a solution
once which actually spent 1 second and
you know maybe one one and a half every
time it needs to open up and it didn't
seem that much in the beginning but
turned out to be extremely slow in the
end and was annoying the customer so
things like that get annoying so what I
want to do first is I want to reduce the
size of this controler in because you'd
see it does nothing absolutely nothing
and still it can it it is 300 kiloby in
size which is 300 kiloby larger than it
should
be um my first step will be to turn this
controll it in into a framework the
biggest problem with this controller and
it has specific methods we can take a
look at that if I go into my controled
in definition here and open this um I
controled in file I will see that I have
some methods and some events inside and
if I think of some other method or or or
some other event I would have to put it
there recompile redeploy refresh the
page lose all the code put all the code
back it will be too much time too much
hassle for nothing so so what I want to
do is I want
to fix that I want to enable myself to
have more generic thing also I want to
move the code from the page to the code
unit let's take a look at the page so
this is my
page um this
one
no this
one oops was
it apparently not so I will I will just
show this one it has quite some code in
there let's uh I'm I'm losing time so
let me not fiddle too much I want to
move all the code from the page into the
code unit actually uh yeah we'll see
that later also what I want to do is I
want to enable event-based communication
because it's much better it it is more
efficient than tightly bound
communication and also I want to move
scripts and styles and images away from
my controller I don't want to have that
in there so let me try to make a generic
control Ed in um first thing I will uh
go into my demo here and I will delete
all the contents of my controller
in and I will just copy demo one uh
sorry demo
two and let's take a look so I will
first rebuild this solution and then
take a look at the
size what's going
on yeah it's now 31 kilobytes so it's
much smaller than it used to be why is
it 30 31 kiloby because okay it doesn't
have images embedded I don't need them
then uh my scripts are still in there my
stylesheets are still in there but at
least I've dropped images uh also if I
open this code now I have some HTML code
I have some more uh logic inside and if
I go to my
page let's take a look at what I have in
there I have a tightly coupled code
inside of uh if my in my page object but
it's at least lean because the entire
architecture of this control it in is
imagine that I only have control ready
event to let me know when the control is
ready I have control event which is any
kind of event that control passes on to
me and I have these two events that I
will explain later on so I have added
them as I went on and then uh this what
happens is when you run this page
control and in will do something on its
own and then it will fire this start
event let me see how does it fire this
start event simply here inside of uh
this
code um sorry not start event it was the
control ready event when my document
loads it will fire the control ready
event then my page will do whatever
preparation it needs to do it will call
the start code unit which does some
initialization and calls method start it
is a generic way of calling any kind of
method inside JavaScript and then my
JavaScript has this switch statement
which uh receives whichever arguments I
want to pass to it and handles that this
is just the first step in the
optimization I hate this but I have to
show it so that we can easily build up
uh a more robust solution so um when
this start hits what happens is that
this jQuery that produced this HTML will
be appended to the page actually and I
will bind an event so that when I click
an event something happens and another
event is fired in nav and the event that
will be fired NV is submit event and
when I go back to nav there is only one
event control event and here I check
what was the event that was
fired if I have an architecture such as
that I can easily change just the
JavaScript and remember JavaScript can
come from internet you can easily deploy
a new version and new version can have
new functionality in there and that new
functionality can call into Cal and cl
can accept that new functionality
without you ever having to touch the
interface or the CL structure of the
object so the events are the same which
is what is important so let's run this
uh simple
page so I will go to Internet Explorer I
will run demo 2 and here's my page this
is what uh the jQuery does so I will
just put V page and then send to navv
what happens in nav is that it tells me
data from JavaScript first name last
name and this is in fact the results of
this function here so I have received
data as Json I have I have this
interesting Json management code unit uh
which I use
to parse Json for me and construct Json
for me so that I when I need to pass
data back and forth I uh don't need to
spend too much time on that so this is a
very simple Improvement which now keeps
a solid structure of my control in that
I never ever will want to to change so
structurally speaking this is the last
version of control edin at least not CL
code not JavaScript code but the
interface that sits in
between okay um however as I said this
is of course not the last version this
uh what's happening here oh this
is trying to find the
slide there is another problem here
there is business logic which is Blended
with the UI logic this submit method
that was passed it was handled directly
in the
page uh and this is something that I do
not like I want my business logic to
stay somewhere outside also
infrastructure Logic the Json management
thing like receiving Json parsing Json
and all it's also Blended together with
uh the user uh interface code and the
business logic code I would also like to
separate that part and move it elsewhere
so I I I I like my te to be clean so
maybe events could help if I introduce
events and start publishing events from
my page rather than just stuffing
everything inside uh I could solve the
problem so let's take a look at um what
kind of events we have we have Dynamic
events we have static events uh sorry
Dynamic static and manual Dynamic static
events are events which are invoked
automatically you don't need to do
anything you just say that this code
unit is or has an events of subcriber
and if you do nothing else it will just
fire and every time it fires an event it
always fires the new instance of that
code unit and there is no State
preserved between separate calls into it
manual subscriber code unit will not
fire any events unless you call bind
subscription function and it will stop
firing events the moment you call uh
unbind
subscription so these two functions will
change the behavior of that uh code unit
however important thing is every time
you fire an event inside of a manually
bound code unit it is the same instance
that responds which means you are able
to preserve state which is very
important if you think of this if my
business logic is going to leave in the
events somewhere outside of the
page one thing that Paige could do and
that pige is very good at is retaining
State you know as long as user is inside
the same page the state remains in there
however if you move the business logic
out of the page object into a code unit
your state is gone so if you have
Dynamic static code units then every
event that it calls into code unit you
will also have to pass all possible
state which is a bad thing why would you
be passing all of possible State into
something that is intrinsic part of uh
of the page object just separated
because of clean design so personally I
prefer manual um manual events however
they come at a price let's take a look
at how we can decouple this thing with
events so um I'm going to delete uh
actually no demo 3 is the same
JavaScript it is just going to be
different clal so let's go into
CL uh
here my clal looks different now so I
still have a control ready event however
it doesn't just call start it also calls
buy subscription on this JavaScript code
unit let's take a look at this guy so uh
JavaScript code unit so here I have this
initialized method which receives an
instance of JavaScript add in this is my
interface that I've defined in C you can
in 2016 and 2017 pass that as a variable
out of the page and now you can talk
directly to JavaScript from outside of
the page object from code units so this
is what I do I create an instance of a
code unit I give my JavaScript interface
to it so that it can talk to JavaScript
directly and I bind its events so that
when the page fars events this code unit
will will respond so here I have this
control event this is my business logic
so inside of this business logic I now
handle this case and check okay which
method was called this one so what do I
need to do that thing and that's all so
also when I close page I unbind
subscription so that uh my event
subscriber doesn't remain alive after
the page is closed that would be a bad
thing because you know you start another
page the same event is fired and then uh
my dead actually Undead code unit starts
responding or keeps responding to things
which would be bad thing so that's why
unbi I unbind subscription so let's
start this demo
3 it will look exactly the same so you
will not perceive any difference I will
just do something here like that and
send to nav and that's uh that's
interesting because it does exactly the
same thing just in a different
architecture so when event arrives from
nav what happens in here is control
event is fired and then it simply calls
on control event which is an integration
event see I've made an integration event
Microsoft doesn't do that because they
are not sure that they will never want
to change the signature I'm pretty sure
I will never want to change signature of
this one it only needs this Json which
contains all the context I need for
business logic to execute um okay so
that's how decoupled page uh with the
control in looks
like there is one problem with that I
haven't demonstrated yet I will just
demonstrate in a second that's um that
depending on how you exactly navigate to
the page or from from the
page this onclose page trigger might not
fire if you do not trust me then let me
just go back to the
browser and let me just refresh I will
just click this again and then I will do
vco send to nav one two okay I'll
refresh once
again Donald
Trump one two 3 and if I keep going it
will be more and more and more every
time I refresh I get a fresh instance
subscribed but my on close page trigger
never
fired okay uh you are looking at the
page not at this and this is a problem
why does it happen well honestly I do
not know but thing is it does happen the
only situation when it does not happen
is if you open the page as a card page
from a list page from a role
Center and then navigate using the
navigate button but if you open the page
directly which you can do then this
Behavior will happen so the end result
is that we have multiple subscriber
instances uh subscribers remain
subscribed we have no possibility to
unsubscribe and we actually have orphan
code unit instances living out there
happily firing events with out uh a page
to talk to that will cause bugs you can
imagine because JavaScript instance that
it attempts to talk to is gone it's not
on screen so I'm not sure it will crash
the the session but it will it will look
ugly anyway so we need to take care of
that um so how do I do that how do I
solve that problem well I will just
delete this uh content of My Demo 3 and
I will go into demo
four so I'll copy the content of demo 4
and then let's take a look at
JavaScript uh because Cal is still
mostly the same there are subtle changes
in there the most important changes
happen in here so let's take a look at
my script now it's this script
so I have this this little part this
little bit piece of code what does it do
here I subscribe to the on before unload
event of the parent
window this is the event which will
fire no matter what you do so no matter
how you navigate way this JavaScript
event will fire so I capture that event
and so this is how I capture I assign
this function to it and then I I also
have to make sure that I do not unload
twice because that could cause issues so
I memorize if I have unloaded it and if
I didn't then I simply call this close
requested event in Cal so back in my Cal
if I take a look at demo 4 There is
close
requested and from here I finalize so
I've moved some code into this finalize
which means I've unsubscribed from here
rather than directly from on close page
and then I call close page again
directly so that I make sure that the
page does go
away and then uh this page close might
again trigger this finalize and it might
again trigger this uh the same thing the
reason why I have it twice is because uh
if you navigate away using standard
behavior of nav then it will be quicker
to do that so I just uh I just save one
extra event uh unnecessarily so this is
uh how I do that and then let me just uh
compile and build this um solution
here and the moment it's completed I
will load
Lo demo 4
here actually is it demo 4
or Y and then I will try the same thing
John
do once and then I will load it
again and I will do
Jane do send to nav one and only one and
if I try it again trust me it will be
one and only one ever since so this is
how to take care of this
problem honestly I believe this is a
platform issue it is a probably a bug
and I hope Microsoft fixes this so we
don't have to do this ugly workaround
every year I present an ugly work around
here and then next year it gets fixed
last year I wasn't able to show how to
transfer control edin out of the page
into a code unit because that was
pressing the the client now it's fixed
so maybe uh maybe this gets fixed at at
a point I hope so still we have problems
this is still not good
enough the problem is scripts you've
seen that in my control edin it's now 34
kiloby but I want it to be even smaller
because I want to eliminate any kind of
duplication that I have in the script
what kind of duplication do I have well
first of all this jQuery that I use
Microsoft also uses jQuery so there is
jQuery download from the internet loaded
into the browser so browser has it
cached locally and now I want to supply
another copy of it why why not just
using the same copy that the browser is
already using that's just one example of
why I would want to separate the scripts
from my controled in my controlin
ultimately I want it to be just
infrastructure so that everything is
comes from somewhere else so the first
step that I want to do is reduce script
loading and multiplic application by
loading things only once and reusing the
browser cache as much as I can because
this will improve performance especially
at those small devices like like phones
and also I want to optimize any kind of
dependencies uh scripts stylesheets
images anything so let's take a look at
how I can take care of this
now so I will just delete demo
for see how easy it is to change the
entire code just press F6 and everything
is deployed to na so if you didn't
download that template now is the time
while I'm fumbling here with these small
icons on the screen do you see the code
okay so uh here is my demo 6 let me
first rebuild demo 6 and then let me
take a look at the size of the resulting
okay it was 30 something now it's 2
kiloby in size so it doesn't doesn't
really have much in there so let's take
a look at what it has it has this
stylesheet it has this script here demo
5 control JS which now has some more
code
okay it has this piece of code let's
take a look at what it does it retrieves
the scripts that are loaded in the
parent window which is the nav web
client and then it does a 4 each through
them and is looking for
jQuery and when it finds jQuery it
creates a new script element uses the
same URL and injects it into my if frame
where control it in lives and then only
after this script is loaded and
executed I
fire my ready event in Cal so exactly
the same thing happens only much fter
faster with a much smaller controller in
that just takes like a nanc to tr
transfer to the wire much less time to
unzip and do everything so um if I yes I
have already rebuilt it let's take a
look at my uh page
six page six six is still exactly the
same copy of page five so if I run my
demo
6 even
though um sorry demo 5 I'm at demo 5 I
will click this and it's here so exact
the same behavior from a control which
is only 2 kilobytes in size so what I've
done here is I have saved a little time
by reusing code that Microsoft has
already deployed so that I don't have to
spend extra time on processing that you
know JavaScript takes a little while to
execute and specialist scripts such as
jQuery which are 100 and plus like 180
Kil I think this this specific instance
is minified which means it's quite a lot
of code it needs to compile it every
single time why would you do that so
just reuse exactly same Source browser
is smart enough to know if it comes from
the same Source it is already compiled
so um this is how we optimize both the
infrastructure Behavior and the
performance of this script so again it
will do exactly the same thing Behavior
has not changed and if I refresh that
and do it twice it will still be only
one um
okay so we are nearly there not
quite there is a problem I don't know if
anyone of you thought of that the moment
I showed how I collect my jQuery the
problem is this works only in the web
browser because if I go into the RTC
client there is no parent
window my ey frame is the only thing
there is actually of course there is a a
browser window on top of that but there
is no jQuery loaded into it so I need to
put everything into the script that I
want to have inside of my um frame so if
I try to run this page from the windows
client let's try that this is page five
I run
that uh what okay this was
sleeping this morning unlike me
so that's my page nothing in there
because it didn't load jQuery it didn't
have anywhere to load it from and it's
not a part of my control it in so I have
to handle that
somehow um so what am I going to do here
what I want to do now is provide a
different way of loading uh script and
other kinds of dependencies as I said I
do not want them to be a part of my
controler in because that is not the
most efficient thing but obviously I
cannot just reuse them from the browser
because the browser might not even be
there so I have to handle that through
my infrastructure code so I will have to
create a framework for loading those
dependencies and welcome the require Al
guy who knows of
requirejs
okay two people three four five six okay
this is normal because why would a CL
developer be concerned with required JS
it's a module order so if you run some
JavaScript in the browser in the app on
nodejs or like in uh if you want in
Visual Studio code then requirejs takes
care of loading dependencies so you just
say at the beginning or anywhere inside
of your JavaScript I require jQuery and
then it loads jQuery you don't need to
know where from it just loads it it
knows where it is so I was thinking why
not doing require Al so when I need a
script inside of my controller then I
cannot unfortunately use requirejs or
perhaps I could I just didn't uh push
hard enough so I came up with this
require a so inside of my JavaScript I
say I require this or I require that and
then it collects it in the most
efficient way that it can be so how
would it do first um it would take a
look at the web client if it's in the
web client it would just collect the
script from the top window if it can if
it cannot find it there then it would
fall back and fire an event in the back
end in Cal and ask CL okay can you
supply this script to me and then CL
might Supply it because it might have it
in the setup table that I will show or
CL can say sorry I don't know of this
script and then third thing happens is
it just downloads it from internet so
you get your script in the most
efficient way always it's just that
sometimes it will be a little bit slower
because it's a different kind of client
that it cannot handle so we keep our
control as lean as possible we load our
scripts in the most efficient way as
possible we have a fallback mechanism so
that we can make sure that script is
always loaded and we can still make
changes to the behavior of JavaScript
and change anything without ever having
to worry um about upgrading the existing
framework existing interface or the the
the footprint that the interface has on
the Cal code so let's take a look at uh
require
Al I will delete these
uh objects from demo
5 and I will go to demo
six so I will copy them
here so let's take a
look
inside
here H I'm I'm not sure what's exactly
happening but I I might uh apparently my
demo files are not in the shape I hope
them to be so I might at the end of this
demo do a little fumbling maybe it
doesn't succeed so I usually rehearse
all my demos but this is probably going
to be one that might fail but for now
let's take a look at this let's take a
look at this require Al
script so there is this big function at
the beginning I would just collapse it
to start with and here I have two blocks
I have a config block of course they do
not have to sit together this is just so
it is easier for you to see what happens
and how it works here I have this config
block where I Define that I have two
objects two scripts that I might need I
may Define angular or whatever else like
knockoutjs or whatever um and then if
any script that will be loaded through
my framework ever needs it
then require Al will know how to collect
that so I have uh each of them is named
and it has um the the regular expression
pattern by which um JavaScript will
attempt to find it in the scripts that
are loaded in the parent window if that
fails it will ask nav for jQuery script
from the setup and if that fails then it
will simply load this from this URL so
jQuery will apparently be loaded from
the URL and um this one will uh will not
jQuery UI I don't have it at the URL
because jQuery UI is something that you
need to configure according to your
specific needs otherwise it's just too
big uh to download so I don't have a URL
I will have to have it inside of my na
let's go back to NV and let's take a
look at this setup so uh I will go to
um to my pages and there is this uh
controled in
resources so here when I run this I see
see that I have some javascripts some
images um and that apparently I have
some configuration there is this jQuery
UI here which uh I can load and run as
um instead of my uh jQuery which would
normally be embedded also uh yeah I
don't have jQuery apparently here so it
means it will always fall back to
downloading it from the internet that's
intentional so that you can see that
even though I don't have it in the setup
and even though I might not be able to
access it through uh the the parent
browser I will still be able to use it
so this is my uh page uh six and let me
rebuild it
here of course here I have also said to
my framework that I want to use both of
them so again this does not need to be
here it can be somewhere else wherever
you it makes most sense for you to put
it so uh I will just run it from there
so
let's load demo
6 oh what do you know there's the chess
so let's try to play chess with
na let's see if actually it can detect
stupid
mistakes okay I'm I'm not going to
embarrass myself in front of you but
this is something that has happened
because uh I have decided to show a
different demo for for a change I've
been showing this C C me and send me uh
so this is a different kind of thing
like just to show that you can put
whatever you want inside of your
um uh of your page so how did this get
loaded let's take a
look so apart from having this
requirejs I also
have this new event that I've created
which is called on request
UI
so all of my code unit that I will be
able to now abstract my business logic
into and this page 606 accidentally
works with the code unit
66 if I go into code unit
60006 I will see that in there I have
some methods that send scripts and send
Styles and send images and send HTML and
they respond to require event to send
something else if needed and here I have
some
functionality my control event is still
here and I even have some stylesheets
embedded into the code I have some HTML
embedded in the code so I can have it in
the code I can have it in the setup
table whichever way I want to and then
this uh request
UI uh event it will be received as a
subscriber here and then it will just
get HTML from this code P pass it onto
the page get JavaScript get images get
stylesheets and pass all of that into
the uh into the front end and front end
will then execute that and even though I
don't have all of the dependencies
loaded if I run this inside of my
windows client it also runs pretty well
you know so it is also fairly yeah it
doesn't make me uh doesn't let me be
stupider than I already am so okay this
is how to um how to separate those
concerns of UI of scripts of classes uh
sorry stylesheets even further than we
have done so far but this is still not
good enough so far we have managed to
get uh to a fairly lean state of the
solution we have a very lean very thin 2
kiloby thin control it in which can
handle all scripts which can handle all
stylesheets dynamically as needed and
and will load them in the most efficient
way and it also separates the business
logic from the UI so far so good however
this is not um not all so we are again
at a part one apparently that's copy
paste bad habit so I've changed the
title I just forgot to change the uh the
number so this is part two optimizing
back end so JavaScript is as optimal as
it can possibly get perhaps you will
when you download these things from my
blog you will find more ways to optimize
that and that's fair I will now go and
try to optimize another thing because I
have only 45 minutes left and quite a
lot of work to
do what is the problem why do I want to
keep optimizing well code is still
tightly bound there is still um well
logic is removed from Pages as much as
possible but uh UI Logic the
infrastructure logic and business logic
are are still tightly bound inside of
that code unit if you remember this
chess code unit there was all sort of
crap inside there was HTML there was
responses to events there was UI events
there were click events all stuff in one
code unit just dumped yeah we don't have
it in the page good job but we have it
in another pile which is equally as ugly
and you know if you ask me if you have
your code in piles it's better to have
them in one pile rather than two piles
so if you want to separate then separate
the correct way not this way so let me
fix
that apparently I will have to apply
some design patterns here so far this
was no design patterns and I don't know
if you hate the term design pattern I
don't but I will have to introduce a
few let's talk a little bit about
polymorphism so you know what
polymorphism
is it's when a dolphin jumps and you see
it as a
cow that's when an object can change
shapes at run time and uh one moment be
something and one moment be something
else polymorphism is an extremely
important Concept in objectoriented
development uh and not just
objectoriented development because it
allows something that's called loose
coupling and sad truth about
polymorphism in Cal is that there is no
such thing as polymorphism in
C so we are kind of in front of a wall
so let's try to see what we can do
there are many polymorphic patterns just
not in Cal so uh if you take a look at
Java at C at python Ruby whatever you
will see a dozen a dime of polymorphic
patterns which which attempt to solve
the same problem in a slightly different
way or maybe a variation of a problem in
a different way when we talk about most
common or gang of four uh design
patterns then we have these five Factory
Service locator dependency injection
strategy Etc so all of these are called
inversion of control because they do
something very very nice they help us
really decouple our code separate
concerns as much as possible uh how does
inversion of control approach the
problem let's think of this imagine that
you have some consumer object that that
uses a dependency which means it uses
another object which has logic which is
not in intrinsically this object's logic
so let's talk about event logging
imagine that consumer object is sales
order page and dependency one is event
logging so namely you are logging events
into a file so when you release a sales
order there is a flag in the file which
says this user at that moment has
released and when you reopen it says
another line and this user at that time
has reopened so this is how we would
normally write it in CL we would put
event logging into one code unit then
reference it from the sales order page
or maybe sales order release code unit
but we would still have a tight link
between the consumer and the dependency
and then what happens you decide to
change this
dependency with um SQL Server logging so
what do you need to do you need to go
and recompile so you change the link you
change the consumer to use another
dependency but what happens with this
one it loses the link so it forgets
about it what if you want to use this
one or that one well then you would have
to go inside and write if this then that
and it becomes a very ugly piece of code
so inversion of control approaches the
problem like this obviously this is a
bad practice so how it does inversion of
control it just inverts it so
dependencies work work in the opposite
direction and they're not really
dependency they are Loosely bound so we
have a consumer object which needs a
dependency so it needs a
behavior and then it has some kind of
dependency resolver let's say a factory
and it says to the
factory I need an event
logger and it doesn't care if it's a
file system or Windows Event log or SQL
server or some kind of web service or
Twitter or whatever it just says give me
an event logger and then this dependency
resolver based on some setup or whatever
makes a decision and says okay here's
your Twitter event logger and then my
consumer object consumes whichever
dependency came into it without having
to know what exactly it does all that my
sales order page needs to know is that I
can log events with this thing how
exactly not my concern okay so that's
inversion of control it solves this
problem of lightly coupling
dependencies um what happened I was
clicking too
far there is one pattern in particular
in CL which seems to solve that problem
if you take a look at the diagram it is
almost identical so here we have a
consumer object uh since you know it's
extremely difficult to have
real dependency injection or inversion
of control or factory or any kind of
similar pattern inside of
C uh we have to call events in place so
instead of consumer object knowing or
actually just asking handled uh this uh
dependency resolver for a dependency it
fires an event it says I need this uh
logging thing to happen Okay and then
this facade which sits in between which
has this event log method
it simplifies an event and then allows
any of the subscribers to subscribe to
it so if you want to have um let's say
Twitter logging then this handle facade
will fire Twitter logging if you need uh
file system logging it will fire file
system logging how does it work it has
two components it has the publisher
component which is the interface so if I
need to log an event I log I call the
publisher I say I want to log an event
and I don't care how exactly it's what
publisher also doesn't care so publisher
finds the subscriber code unit and then
it calls the event and then at the end
it makes sure that the event was handled
at the same time subscriber checks if
the event was already handled am I the
Right subscriber to handle that and if
these checks pass then I go on and
execute the logic and then set the
handled parameter to through so that
publisher knows that it was successfully
executed this is what it looks like in
the code so we have this piece of code
where I have log event this is uh my
interface here I first retrieve a
Handler based on some kind of setup and
then I call on log event and then make
sure that event was handled if not
handled then error good and then I have
two
subscribers both of them do this check
at the beginning they check if this is
an event for me if so was this event
already handled if not then it executes
the logic otherwise it goes out and at
the end it sets handled to true and all
hunky dory but it's not really hunky
dory there are things which are not that
that good first subscriber
identification it is handled at two
places so
my interface needs to be aware of the of
possible subscribers this is not a bad
thing it anyway anyhow any inversion of
control has to be aware of possible um
possible consu sorry uh dependencies so
this is not such a big problem problem
but um this is duplicated see inside of
my event handler I also have to do this
check and this is a failure point I may
make a mistake
there the second problem is there can be
multiple active subscribers nobody can
prevent me to subscribe to the same
event without following the rules of the
infrastructure without checking is this
event for me I don't care was it handled
don't give a you know
and I also do not set handle so I just
want to confuse the framework so that's
you know a gentleman's agreement pattern
if you ask me
so then cross call State preservation in
the handle pattern you have to have
static uh code
units so um you will have problems with
State preservation every call will just
you know uh go into new instance then
infrastructure separation what you see
in all of them is this you have
infrastructure code then some business
logic then again some infrastructure
code all in the same place personally I
dislike that so this is not the best
thing and then infrastructure fragility
as I said who prevents me to do things
like that like I check I make a wrong
check or I forgot or forget to set
handle to true and I break the whole
thing or like inject some malicious code
or whatever so let's think of how to
handle those
pitfalls um obviously I will have to do
something with manual
subscribers but the moment I introduce
manual subscribers I complicate things
you will see why exactly however if I
manage to put manual subscribers in the
game then I solve these two problems if
I have manual subscribers then since my
interface subscribes manually each of uh
possible event handlers then at least it
can make sure that that there are no
multiple subscribers and it also can
make sure that there is cross call State
preservation so that whenever an event
fires it is in the same instance which
was subscribed which may be important
depending on what this logic is that you
are
performing uh there is another event
pattern which can help here this is
called Discovery event pattern if you
don't know of this then follow this link
and learn about it it is uh it has been
put to use in 2016
and also 2017 even more it is a standard
pattern that Microsoft is applying and I
will also demonstrate how you can apply
it in a very similar way so what is
event Discovery pattern this is a
pattern which is in charge of finding
what kind of things exist in the system
so you can use it for whatever you want
here I'm using uh it for identifying
interfaces and for identifying possible
dependencies to handle those interfaces
how how does it work first we have a
discoverer some entity in charge of
finding out who is out there like for
example who can handle event logging so
it fires a discovery event and says
please identify ourselves and then
subscribers who subscribe to event
logging will say me and me and me and
will identify themselves in some way so
that Discoverer knows who they are okay
and then we have a list of discovered
modules and that's all so it doesn't do
much more it just identifies things for
us but it's extremely powerful even
though it's it looks simple because it
doesn't does doesn't do anything it just
gets the list of things that are there
we can put it to very very good use as
you will also see in standard code how
Microsoft does it so let's see this
discovery event
pattern I've said that I have things
called interfaces think of interfaces if
you know C and you know what an
interface is this is similar here I have
interface code units they do have some
business logic inside because we don't
really have interface code units in Cal
uh but they perform or achieve exactly
the same thing so let's take a look at
these
interfaces here I have one page
interface setup apparently I will have
also interface setup table what I want
to make sure is that this table is empty
so I run it it's
empty and then I want to see what kind
of interfaces I have which means what
kind of possible behaviors that somebody
might need in the application so I will
run my
page and when I run the page oh there
are four so there is address format
there is currency exchange there is
event logging and there is Tech days
2016 demo interface what do you know so
they came from somewhere where did they
come from well let's take a look what
happens in this page because if I go now
into my table and run the table the
table will have some values inside well
let me delete that I really do not want
them to to be
here let me go back to the page so let's
take a look at the page at the beginning
of the page page fires this unregister
interface what is this unregister
interface it is an event on the table
called interface setup
so when this event fires let's take a
look at the signature it says it's
interface setup record so it passes this
table as itself to whoever cares to
subscribe itself or actually identify
itself then let's take a look at an
interface interface is a code unit so
I've said I have a currency exchanger uh
format Twitter something or other or
whatever um let's take a
look I have
this let me start with this event log
interface so I go there the interface
has a method event
log it has an event on log event and it
has okay it does some subscription for
whatever reason it doesn't really matter
at this stage but it has this on
register interface so it subscribes to
this discovery event and tells to the
system here I am I'm inside I can handle
event logging or if I go into uh address
format interface it is very similar it
has less business logic and it also
registers itself so if you have a
functionality like an a new
functionality that you want to introduce
into the application just the way I have
introduced this um control addin
interface which is in fact Tech days
demo interface you can just create a new
code unit which subscribes to this known
event and suddenly your your
functionality is available to whoever
needs to call into it uh so this is how
Discovery event Works let's go back into
this page so interface setup I run this
interface setup let's edit this list and
let's try to configure this for each
interface it asks me which module
handles it so I look up here I have no
modules for event logging I have well I
have this Windows Event log let me use
Windows Event log and then when I sorry
uh apologize let me use Windows File
system event log when this setting is
done here I can click setup and then I
can configure this module okay I can
specify where's the path to which I want
to log events what happened here you
know what happened another Discovery
event so when I looked up from here
another Discovery event F which asked
okay where are the modules which can
handle this interface so here I have for
event loging I have three modules I can
log it the whatever way I want or for my
tech days 2016 demo let's take a look I
have two modules I have Twitter demo and
I have this uh arbo chess demo that I uh
constructed from some public uh open
source libraries so this is how
Discovery event works it fires an event
it asks who's there and then either
stores it permanently or temporarily and
allows you to configure the behavior of
the application in a Loosely coupled way
you can imagine that now that I have
this interface setup my infrastructure
can use this setup to identify which
module will respond when I need to log
events or which module will respond when
I run my tech days demo next time okay
so let's go and let's take a look at how
it responds to these event logs so I
will uh go into my RO tailor client into
sales
orders
um and then I will find a sales order
which is released like this one and then
I will go to this file this temporary
location I will delete this log file
from here let me move it over there and
let me
reopen so when I reopen there is my log
here which says this sales order has
just been reopened I will release it and
this updates with sales order has just
been released good I don't need this guy
anymore let me close this
page and then let me reconfigure my
interface let me say that instead of
file system event logger I actually want
to have Twitter event log okay there is
some setup behind Twitter which is a
different page this is what my Twitter
module said this is page that you use to
configure me so every module can publish
that using the same Discovery event
pattern and here I have some Twitter
configuration how to log into Twitter
and I will close this page go back
and then open the same or actually let
me use another
one what where's the fun if I always
demo from exactly the same so I will
reopen that and then I will go to my
Twitter page so here I will refresh my
tweets and it says sales order has just
been reopened so I will release
it
and when I refresh this page it will
post another
tweet so I didn't even have to close the
application exit do anything whatever
just live I have Loosely bound one other
module just by changing a piece of
configuration so this is how Discovery
event works so that's the discovery
event pattern extremely extremely
powerful so whoever tells you that this
is not the the real pattern has no clue
what they're talking about this is as
good as a pattern as patterns get so
after discovery event this is what we
have we have solved subscriber
identification because right now nobody
can cheat me anymore that you are who
you tell you are because I have
identified you I know that you exist and
I know how to call you
specifically so that's how we have
solved the biggest problem of handled
pattern we have more to go so here I
propose my own pattern which I called
module binder pattern so what I want to
do here is take care of these two
remaining blocks infrastructure
separation because I really love to have
clean code and infrastructure fragility
I want to make sure that nobody can
really mess up with my behavior so uh I
combine these two patterns I combine
Discovery pattern and handle pattern in
such a way that I achieve logic and
infrastructure separation so that my
business logic leaves in the business
logic code unit and infrastructure
leaves completely in the infrastructure
part of the system or or or the setup
and that way you have very very clean
solution that you can also apply to
JavaScript as as we will see so so far
this part is not about JavaScript it's
just generally architecture what does
this module binder pattern look like
like this so if it looks like this to
you it's not accidental so it it seems
to be a lot of components in there that
you know do this or that but in fact
this is what it is it has four
individual large blocks of code this
consumer is the smallest one it you can
just ignore it this is my sales order
page that consumes this
functionality my sales order page talks
to the interface this is you know
remember that those interfaces that I
had like event logger address format or
whatever so my page is aware of those
and it doesn't have to be tightly aware
it can be aware through events and
through extensions I can actually create
a code unit which is an extension which
is aware of my interface and which now
binds the page to be able to talk to the
interface so it's Loosely coupled so uh
this interface publishes the business
logic event so when I need to log
something I call interface and interface
fires on event log to whomever wants to
listen however my consumer does one more
thing
before it starts consuming events it
talks to infrastructure and it says
please load this module for me so if
I've said that for event logging I want
to use Twitter at this stage my sales
order page talks to the infrastructure
and says please load whichever module is
responsible for event logging interface
and infrastructure goes into the setup
and checks who is responsible for uh
event logging Twitter and then it binds
it calls bind subscription on the
Twitter code unit so that it is the only
code unit that actually responds to
events okay and then when I call this on
log event my interface fires the event
the module which was bound manually
using buy subscription response and
performs its logic and that's all that's
all there is to it so this is what
interface looks like very simple thing
just one simple method and one simple
event so you are kind of tght tightly
bound to the method you say like log the
event but that's where it ends from that
moment everything is Loosely coupled and
this is how all loose coupled pattern
there there has to be tight binding at
some position like you need to know what
you are calling so when you fire this
event what happens is that the module
kicks in module is a two code unit Block
it's not one code unit anymore because
it cannot be um it has one code unit
which handles infrastructure and one
code unit which handles business logic
so how does it handle that uh like this
this is the business logic code unit it
just has an event subscriber so it has
this event subscriber log event and it
performs in this example the Windows
File system event
logging this is the binder this is
infrastructure part the infrastructure
part find the module and runs bind
subscription on that module and when you
unbind the module then you unbind
subscription so how did I bind those how
did I actually invoke module binder for
my code I will show all of this or
actually not not exactly all but most so
here uh I have this event log
customization code unit this is just
full of events so here when I open sales
order card I bind my interface and when
I close the sales order C card I unbind
the interface so that's how I bind I say
like okay please bind for me whichever
code unit is in charge for handling
event logging or whichever code unit is
in charge of handling my uh Tech days
demo so this is how I bind to this
binder so it binds and unbinds
modules it discovers modules for me
which modules exist for a specific
interface and we have one more component
which is module manager which handles
discovery of interfaces and modules so
it's kind of on top of everything we
will see a little more of that
um we still have some
challenges still uh there are certain
things which do not work just as
expected so first call
multiplication we can it can still
happen that we have call multiplication
uh it can still happen that we have
explicit subscriptions like all
infrastructure aside if I follow the
gentleman agreement that I have in place
I can still create a code unit which
statically subscribes to event log and
anytime that there is an event log my
code unit also Firs nobody knows that
right how do you know you don't so
that's a problem then I can have these
Rogue subscribers just jumping in
subscribing to whichever event just to
to mess up with the system or just to
steal some information or whatever
or I can still have single subscribers
so let's take a look at the solution to
these challenges first uh I have I have
invoked the help of event subscription
virtual table this is virtual table
which keeps on the NST in memory the
list of all Publishers and all
subscribers and it's extremely fast
because that's exactly the same thing
that NST is using when choosing whom to
invoke when an event fires so you can
use this virtual table to actually check
to perform two very important checks
first is you can verify that for your
module there are only manual
subscribers and if there are not manual
subscri actually if there are
subscribers which are not manual you can
throw an error and say sorry I do not
let you
in and that will just prevent you from
messing up with the entire pattern
because nobody will be able to just put
their code unit which subscribes to our
event because if it's manual uh sorry if
it's static it will be rejected by this
event here and uh sorry not event but
but function and if you want to
subscribe that to actually be
legitimately responding to events then
what do you need to do you have to
create a module and you have to have the
user configure that module to respond to
that specific event so it's pretty safe
and then you you have another one you
actually verify that there are active
subscribers before calling with this you
mitigate this last one that there is
only a single subscriber okay so uh
before you make the call to event log
you again check into the event
subscriber table to verify that there is
one and only one or in this example more
than one because I've just decided to
allow more subscribers for specific kind
of event but here you can do checks
whichever you want whichever makes sense
for your business logic if it's more
then you can check for more if it's only
one you can check for exactly one
subscriber and see if there are uh or
there are not so this is the solution
and with that we have actually handled
all of the problems so uh with the
module binder pattern in place we
actually solve the uh the entire
infrastructure and uh UI and business
logic separation so let's take a look at
this binder pattern inside how did all
these Twitter and event log things
happen so here I will go into event log
binder
Twitter inside here I have the bind
module subscriber which checks if the
module name that my infrastructure is
asking for matches my
name or if interface name is different
then I just go out what does it mean if
since this is statically subscribed all
of these will always fire and this is
the tiny layer on top of everything
which is still kind of Gentleman's
Agreement because this is the entry
point if you want to inject something of
yours you could do it theoretically here
but uh since uh the system is resilient
on another ends on other ends it would
not break it so you could attempt but it
would fail uh so here I do two checks
first I check is this module handling
this interface which means if I'm
loading uh Tech days demo interface and
here I have Twitter event logger module
responding it will just go out because
it's not for the same interface but when
the system asks okay who is handling
event logging then this guy will check
okay this is event logging that's me but
is this also loading Twitter event log
or SQL Server event log then it will do
another check and depending on what it
finds it will either Exit or clear the
instance of the business logic this is
this module thing okay and then it will
bind its
subscription since this guy is single
instance it can retain State
okay um there is a way and I will blog
about that uh how to it would just be
too complicated for this session how to
make it multi instance still to allow
you to have multiple subscribers at the
same time the reason why I'm not showing
it would just be acrobay it wouldn't
help anything because inside web client
you are onepage only thing so there are
very few and far between situations that
you would actually want to have multiple
subscribers to the same interface at the
same time that's very unlikely uh but
still it it is possible so here I bind
subscription and then I specify that yes
subscription is bound and that's all
when I close the page for example the
the sales order page I'm unbinding the
interface so what again do the same
check I check is this for me if yes then
I check am I bound actually or not
because it can be that I'm not actually
bound so then I unbind subscription from
this module and I clear the variable
once again and set this bound to false
that's all that my infrastructure part
of logic does and then let's take a look
at event log Twitter business logic
that's it so it subscribes to event log
event
and then it checks some Twitter setup to
see is Twitter actually configured if it
is it calls Twitter
API it creates an instance of this class
and then just calls tweet method by
passing the context into it to perform
the actual and these there are two
helper functions which just do some
formatting uh to help me with that and
then if I take a look at this
customization here I can see that I have
actually when sales order page was
opened I have bound the interface and
when the page was closed I have Unbound
the interface and I've done that for
sales order list and sales
orders and then here in sales order
released event I have actually called
I've created event arguments because
again I'm using another pattern here
arguments table pattern and then I'm
populating this event arguments and then
I'm logging them into event logger
whoever that is Twitter file system
whatever and that's it and then when
it's reopened exactly the same thing and
here's my helper that just creates my
arguments table for me so that I can log
that let's take a look at that in
another example which is my demo example
here so I'm going to my tech days
2016 so here since I have a specific
page which runs My Demo I'm doing this
module binding inside of the page so um
here I will actually have a load module
method where I will first check if this
was already initialized because it all
depends on events which are firing uh
first then I just uh then I initialize
or if I have already been initialized I
just go on and then I call this bind
interface and I'm binding this Tech days
2016 demo interface whatever that is so
that's just something that my control
add in needs at this stage and then
again when the page closes there is this
finalize method which is safe because of
this require close requested it actually
finalizes it unbinds the interface so
that it doesn't respond to events
anymore it de initializes it also
unbinds this JavaScript code unit which
was responding to JavaScript user
interface things which are not business
logic they are just user interface
things so I've separated user interface
into separate code unit business logic
into separate code unit and
infrastructure into separate code unit
and then everything else happens just
like it happened earlier so if I take a
look at the
configuration uh interface setup right
now it says that I have this Garbo chess
that's handling my
uh my business logic so let me run this
from the windows client there it there
it is so it actually works let me not
play chess even though I have 11 more
minutes just enough time for me to lose
badly and if I go into this inter
interace setup and change this
into
Twitter and close this and then I can
run it from
here there is some Twitter or I can run
it from here which one do you want me to
use so that you can tell me that I
didn't
cheat this
one okay so I just attended the most
amazing session ever
ever okay let's
check I bet it will be
here there it is so if you do not
retweet this every single last one of
you I will be very annoyed come on go on
I know you have been tweeting earlier so
what's stopping you now okay so that's
the module binder pattern in action with
control
addins resulting in very very lean
control Adin veran business logic code
units ver lean infrastructure code units
everyone handling just whatever they
need to be concerned with and
finally oh yeah uh I have jumped a
little bit ahead sorry
um I've explained that slide earlier so
I will just not re explain the same
thing what the the last thing that I
want to give to you is if I didn't lose
you so far here's where I lose you
because right now I'm going to do
something so crazy that you will either
go like this guy is an
idiot or you will say like
wow yeah I know that you knew so
um when events came along I had a chat
with a colleague who said we should not
be subscribing to our own events from
within our own application it makes no
sense and I strongly disagree to that
and of course you you do want to
subscribe to your own events I've just
shown why and Microsoft does that and
you probably do that as well there is a
million reasons why you would want to do
that
however what I did is I wrote a code
unit which publishes an event and then
it sub cribes itself to its own
event how would you like
that do you think it's
crazy let me see who actually thinks
it's crazy because when I who whoever I
told it was is like wow you you are nuts
so okay let me explain why I'm doing
that think of this I have separated all
concerns all over the place so there are
code units at work which do not
necessarily know of my control it
in for me to be able to talk to
JavaScript whenever I need to pass
something into JavaScript I need to be
able to get access to that instance that
I have originally passed from my page
into my infrastructure code unit or
actually UI infrastructure code unit
JavaScript hand manager code unit so
this code unit is now an interface for
doing the talk to the web
client however since there are those Lo
modules that are loaded all over the
place they do not necessarily know of
this instance so my page has an instance
of this code unage which holds an
instance of my controled in but my
module which responds to events which
needs to talk to controled in does not
have an instance of this code unit
available because it does not even know
which code unit that is or might be
so to avoid writing a zillion control Ed
sorry if this then that if this then
that or switch or whatever what I've
done is that this code unit which is in
charge of talking to the controller in
let's take a look at it it's this
one JavaScript
Gateway it actually has a method for
example this send script when I want to
send a script rpt from my setup into the
JavaScript so what does it do it sets
this Json something or other and then
calls this method call and this method
call checks if my JavaScript is null
this JavaScript that's actually if you
take a look at this that's my addin my
control edin my interface class sorry
type so I check if this is available it
should be available because initialize
has received it and this is the instance
that holds it so as long as I'm talking
to this instance which holds this
reference all is
fine
however my page knows of this
instance and this instance knows of that
instance but nobody else does especially
my module does not or any other module
that might want to talk to my controller
in maybe a table trigger somewhere would
want to talk to it I would hate that but
still anybody might want to talk to this
control addin and they don't hold the
reference so they cannot call send
script or show dialogue I I had it I
deleted it for stupid me so uh if you
want to talk to JavaScript you have a
whole because you call this sandscript
on an instance which actually doesn't
hold the reference then this instance
goes to Method call this method call
checks do I know of reference of
JavaScript controller in no so what do I
do I fire an event on this code unit
okay this is the on get JavaScript event
and guess
what this get JavaScript is a function
event subscriber on the same code unit
which responds to that event and since I
have manually bound this infrastructure
code unit uh to events there will be
only one of them alive and that will be
the one that holds the reference so
since that one responds to event it
passes the reference out as by reference
variable so that after that my code
which was called from whoever knows
where from has the same reference to the
controlin that the original in instance
of the code unit has so this is I don't
know if we should call it pattern or
whatever but this can always help you
obtain the state of any code unit from
within this the another instance of the
same kind of code unit for whichever
other purpose you need that because this
is something that people often had
problems with in earli versions before
we had events so if you ever had a
situation that you had a code unit which
inside of itself had a variable of the
code unit of the same type then this is
exactly the same situation just with
events so do you still think I'm a nut
case because I did this or is this um a
valid thing to
do so yeah
uh that's uh I don't know what this
slide means so it's that's all I have to
show thank you very much I hope this
was worth the Applause thank
you
