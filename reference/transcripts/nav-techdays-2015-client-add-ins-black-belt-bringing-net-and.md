# NAV TechDays 2015: Client Add ins Black Belt bringing  NET and JavaScript together

- **Source:** https://www.youtube.com/watch?v=UCNdJJzI2kw
- **Video ID:** UCNdJJzI2kw
- **Channel:** mibuso.com - Videos
- **Published:** unknown
- **Duration:** 92m15s
- **Ingested:** 2026-07-26
- **Source of text:** YouTube caption track (auto-generated captions are unreliable for API/identifier names — verify against Microsoft Learn or the compiler before trusting a signature).

---

uh hello and welcome to this session
which has a funny name it's called
client addings black belt and I'm going
to talk about bringing net and
JavaScript together so the reason why
this session is called black belt is
because at least once during this
session you will definitely have to go
what the this guy doing or talking about
so uh it's going to be full of um deep
level code uh complicated code so um I
hope I don't lose you I will also have
to run because I have a lot of demos a
lot of slides to cover so it's really
going to be a lot of topics um let me
first introduce myself uh my name is Vos
slabic I come from Croatia I'm an MVP
for nav I've been an MVP for past six
years I think yeah and um I've been
speaking here at Tech days regularly
since First Tech days I've been talking
about JavaScript a little bit I've been
talking about net I've been talking
about client Ed now I'm going to take a
completely different angle at that so if
anybody here was at any of previous
sessions from me either Tech days or
directions this is not going to be the
same content so this is going to be
mostly new stuff um you can also follow
my blog uh I blog fairly regularly and
most of the content uh from this
presentation will also be blogged about
probably all of the demos will be up on
my blog today and everything else like
explanations and stuff as as I find time
so so um let's let's take a look a
little bit at uh at the CL as a language
CL is the language that we all use every
day and if I would take a picture to
represent CL I would choose this it's a
very rigid language very strict you know
somber and official uh you you can do
the stuff that the language allows you
to do but not really much more than that
if we take a look at the JavaScript as a
language it's completely different so
it's uh
it does funny things so uh it not only
does funny things it's usually fairly
difficult to look at so typical piece of
JavaScript code looks like if you take a
transcript of a couple fighting at Ikea
and then make random edits to it until
it compiles without errors so uh this is
the language that we now have to know if
we want to develop really powerful user
interfaces in um
nav 3 years ago or four I don't know uh
I had a session here in probably This
Very Room uh which was
about net NCL that was the time when net
interrupt was introduced and back then
the session was titled Beauty and the
Beast and I compared Cal and C to Beauty
and the Beast so I'll let you choose
whichever you want but in if you ask me
c is the Beast so um at the core of what
we do today will also be C there will be
quite some of it even though we are
doing only client side um controll
thingss that work in all clients so you
might think like what does c have to do
with that because we know C doesn't run
on the client it doesn't but it runs
runs in the back end so if we take a
look at this C Beast and then combine it
with JavaScript we will end up with
something like this and of course since
there is Cal around this is probably
more like what we are going to see
today okay so let me now do some
gymnastics here let's let's see how many
of you have developed more than one
control Ence in your career okay more
than
two more than
three five okay more than 10 control
EDS okay okay still some hands in the
air pretty good uh now a question for
you how many control edings do you
really need like how many of them do you
think you need to solve all your
problems how many exactly we only need
one so you don't need more than one
control Ed in so um in this session
today I'm going to deliver that one
control Ed in that you can use to
actually solve all uh of the problems
that we are uh ever going to encounter
before I get to anything I think I will
just demo that one control to rule them
all so here in front of me I
have a screen of a POS thing so I will
just now go back and I'm touching this
screen and going going back to nav and
then from nav uh sorry I'm actually
going to um touch screen for uh sale
application POS application so I'm going
to log in in there and then do some I
don't know
um some sale transaction like that and
then give some discount uh
like 25% on the last line so that is uh
one interesting controled in this is
really controlled in this is not a web
application that runs with NV this is NV
so all that you have seen is pages that
I have completely taken ownership off
and uh done strange things to them and
you might ask like okay do we really all
need POS as our only control Ed in that
we are ever ever going to use the answer
is no it's not about the POS it's that
this control here is really a framework
that can do anything so it can do these
interfaces or it can do do any other
interface so what I'm going to show
today is going to be subset of that
essentially that part which allows you
to really have one single controler in
and then use it for absolutely every
client side needs why only one so you
may ask that question because deployment
is a pain whenever you have to deploy a
control addin you will have issues let
me see who has ever had issues with
deploying control addins okay so let me
see keep your hands up okay so who of
you has uh developed more than two
controlin okay keep yeah okay so
essentially all of you who have who are
regularly developing control in are
experiencing problems so let's just have
one single controller in so that we
never ever have to deploy anything so
when we come up with new ideas with new
functional
we can just keep using that one single
control in so what are we going to talk
about there are going to be six groups
of topics um all packed with Theory and
demos so first topic will be Crossing
page boundaries we'll actually will not
talk too much about topics right now
when we go into them I will explain what
I really mean the second topic will be
Json the third topic will be deployment
uh then in the fourth topic I'll talk
about resolving assemblies in the fifth
top topic I will talk about user
interface in general and how to handle
user interface and then finally in the
last topic I'm going to talk about call
synchronization which is extremely
important Concept in um JavaScript and
cl combination so let's take a look at
the first part crossing the page
boundaries so uh when I say crossing the
page boundaries what I really mean is
talking between different objects and
the page that host the controller in let
me make a brave claim at the very
beginning so code does not belong to
Pages let me see who agrees with me okay
let me see who doesn't
really okay so most people still are
undecided but actually there was nobody
who said yes code belongs there because
it doesn't code belongs in code units or
elsewhere but not in Pages we should
have minimum of code in
pages so that we can handle stuff that
is happening like events and similar but
the real logic belongs elsewhere however
if code belongs to does not belong to
Pages then we have a very simple issue
so let's take a look at this example
here so imagine that I have a page on
which I have a control so what I want to
do is I want to take that
control which is declared as a net
object inside of an assembly take that
net object and pass it let's say to a
code unit so that code unit can actually
make calls to that object which would
end in a page something like that was
perfectly possible using um
net control ents so if anybody has ever
developed net control ents you have
probably done something like that taken
the reference of of the controlin which
is regular net interoperability object
and then passed it around and accessed
it from Pages sorry from code units from
tables from wherever needed however it
doesn't really work like that in
JavaScript so let's take a look at why
it doesn't really work so um I'm going
to my first first demo and I'm going to
open the page which has this one single
controller in and then let's take a look
at what this page does so here it has a
control Ed in ready event I will not
explain the basics I assume that most of
you just know uh the basics of control
Ed the basics of of good architecture of
control Ed so I will just just have to
start with that assumption so here in my
control add and ready event what I'm
doing is I'm calling my code unit so
let's take a look at this my code unit
it has set control edin which receives
the control edin as a parameter so what
does it really receive it receives this
one v.com controled in template do I
controled in so let me go back to my
visual studio and let me find that
control definition so here I have that
so it's this interface so what I'm
really passing is this interface which
is also declared as my controller in and
if I go back to page I can verify that
this is this my control edin so this is
this object so what I do from the page I
call this set controled
in function I pass it over here then I
store it in a global variable in my page
sorry in my code unit which is of the
same type and then I call say hello say
hello is a method on this interface as
you can verify here I have this say
hello and then it say says say hello
hello world so let's run this page to
see what
happens oh uh I don't know is this big
enough probably not let me just increase
it a little bit this is what I get an
error which says a net variable has not
been
instantiated if I debug I would find out
that this doesn't happen on assignment
it happens actually when I call the
variable which was stored in the global
variable actually Direct reference which
is stored uh over there so apparently we
have an
issue so and okay my client even crashes
so good let's start the client
again it makes sense if you think of
that it makes sense that is it that it
doesn't work and that it doesn't crash
why because my control is declared as an
interface and you cannot have an
instance of an interface it just doesn't
exist so you can have an object that
implements the interface and then you
can do stuff with that object but we
never declared any object we just have
the interface so what nav extensibility
framework does in the background it
doesn't even instantiate an object on
your behalf it simply mimics that there
is an object but there isn't one so this
is what's happening so let's try to make
uh oops uh I think I think I've I was
talking about this slide so as you can
see there is this interface up there so
uh let's take a look
at actually um I think
that I want to show some more here yeah
exactly let me let me show what's really
happening with this interface so first
here I have situation that I don't call
any code unit that I have all the code
in my page so here I simply directly
call say hello so when I run this
page it will just say hello world that's
what I want it to say so this works not
because there is an object which hosts
this interface it works because nav
extensibility framework knows that there
is a function somewhere which is called
say hello and it simply forwards the
call to that function so there is no
object involved to prove that there is
no object involved I have another
combination so let's investigate bit
what is really happening so here I still
have a code unit a different one so
first thing is I'm going to see what is
the get. net type which is going to
return system. type of this control edin
so what is this control edin in the page
so that's the first thing I will get the
second is I will store the reference to
that and then I will take a look
at um this is nonsense actually
assignment will pass nicely and let me
just exit here for a second and let me
run that so there is this message which
says this is Microsoft Dynamics nav
runtime n.net so it's not interface type
and when I click okay assignment passes
nicely
however if I try to
see this
which
is the get. net type of control addin
let's take a look at that so I run
this and this is I controller then so
this is my variable so I I should have
inside of this variable essentially this
object which I should be able to talk to
however if I do not exit if I call this
controller and say hello and let me save
and run if I call this first message
second message and then nothing uh okay
this is cached version let me save wait
for a couple of seconds and then run it
again okay okay and then error the same
one so you cannot assign this object to
variable you just cannot do that so
let's comment this line let's pass this
into actually let me just call say hello
so if I do
that and exit this will work so let me
just comment those above because we know
that they work so if I hide those
messages if I run the page will call say
hello this of course has to
work however the next thing will fail so
here I set the controller in so let's
take a look inside of this function so
here I set this controller in
in and I say hello on this code unit so
this is the demo that we have seen
earlier this will surely fail so just to
save time I will comment that and move
on
however if I run that so here I have set
control in addin that works and I call
it and from from here I call it on the
variable that was received into the
event trigger when I run that so save
this and run it still works okay so uh
and then it fails on the next line
so here the last one is if I want to
inspect what it really is let's take a
look inside so I'm trying to see is it
null and what is the get. net type so
let me actually uh
run
that so it would tell me that it is this
type still the same net type which we
seen we have seen earlier but it is not
null so it is it has a reference and
still when I attempt to access that
reference it
fails
so what I have shown here is the fact
that you don't do not really separate
the responsibility of a page
and logic and put logic somewhere else
because the only way you can really talk
to this controled in is to call a code
unit by passing the reference and then
working directly on that reference from
within that function which makes no
sense it makes sense for initialization
maybe that code unit initializes it but
for everything else it just doesn't make
sense so if you want to have any runtime
work on that reference you canot because
there is no reference so how do we solve
this problem well we will have to invent
an intermediate object so imagine this
situation we have a page and then we
have a code unit uh inside that page we
have this object which I will call event
marshaler because it has one duty it is
to Marshall events into the page so
events which come from elsewhere it will
simply raise them in the page so this
event Marshal will be a net
interoperability object which will have
with events set to yes so that it fires
events in the page because it is created
defined declared and instantiated in the
page so when I pass something to the
code unit I don't pass the reference to
my control it in I pass the reference to
my marshaler and then when code unit
needs to do something it calls
marshaller and says to Marshall please
do that and then Marshall Aires an event
in the page which then talks to the
controller then so this is the concept
that I will introduce so let's take a
look at this communication through the
martial art
so I will just quickly show this Marshal
class it's extremely simple so it has
one event which is Marshall uh Marshall
event handler this Marshall event
handler has one single argument which is
of Marshall event arguments and this
Marshall event arguments is a class
which is not that simple but we will see
why so I for now I will I will close
that class and I will go back back to my
marshaler it also has a method called
Marshall and only thing this method does
it invokes this Marshall event if it's
declared so that's all uh let's go back
to Cal and let's take a look at Cal what
we have inside so first thing that we
have inside is this marshaler object
which is declared from my uh uh event
Marshal
class and then I have my control edin
still the same control edin and then
when the page initializes which is
essentially when control says I'm ready
uh marshaler is instantiated and then I
pass this marshaler to the code unit so
I pass the instance of this marshaler
into this code unit the code unit stores
the reference to the marshaler and then
I call the code unit which says do stuff
so this do stuff is whichever business
logic you need let's take a look at what
business logic I have inside I have some
message I'm doing some stuff and then I
have some confirmation do you want me to
Now call into the page and then when you
say yes you essentially call marshaler
and you say Marshall Marshall do
Marshall and then you create an instance
of string request this string request is
a class so let's take a look at
this um sorry it's over here so it's
called string request it has one single
property which is called string and it
is instantiated with this string as
parameter
so what I do here I simply say to
Marshall please send an event to the
page and tell the page to do something
so the page will know what to do with it
okay so let's go back to the page here I
have Marshall event event and here what
I do is I call control it in and I send
request and what I do I call the two
request method on my event arguments so
now I will go back to my event arguments
class just to to show you what this is
so here I have some information so this
class really carries information about
uh what um what the Marshall will do
this request uh sorry two request method
converts the the content of the class
the the event arguments class into a
request class we will see that class a
little bit later so when I pass this to
request it sends this to JavaScript we
will see what exactly this to request is
a little bit later so let me run this
page before I do that I will just Mark
in my controller in that I want to run
demo to and I will rebuild my
solution okay so I will run this page
and then it says I'm doing my stuff uh
now may I now do call a page method I
say yes and it says CL has invoked a
method in JavaScript so where does this
come from it comes from JavaScript so
when I go to my JavaScript here I will
have demo 2 this send request what it
does is it says CL has invoked a method
in JavaScript so my request has ended
inside JavaScript and JavaScript has
executed it okay this is not exactly how
you execute JavaScript we will see it
later this is just the demo to see how
to actually call into the page into
JavaScript from a code unit which
normally doesn't have access to all that
okay so that's how communication through
marshaler really
works and here I end my uh communic uh
my my talk about the event Marshal this
event Marshal is going to be in the
background of everything I do today
actually not everything a little bit
more um so uh in the second part of
today today's presentation I talk about
Jason I hope you know what Jason is not
not that guy maybe you know that guy as
well but this is not what we talk about
so Json stands for JavaScript object
notation it is a representational
language it is used to represent objects
in their state it's used to describe
data content and stuff it's very similar
to XML in its purpose and functionality
um except that it's way simpler it's
much more human readable so um on the
right hand side you can see an example
of a Json object so with Json inside
JavaScript we describe we Define objects
so JavaScript natively handles Json so
it can use Json to convert an object to
string when the object will become a
string which looks fairly like that then
it can also take Json string and convert
that to an object or as you have in this
example it can instantiate an object
directly from Json so this is what Json
is um how does Cal talk to JavaScript
let's take a look at this part so first
on one end we have CL on other end we
have JavaScript and normally if you call
a method in JavaScript then you simply
imagine you pass a string you simply
pass the string and string seemingly
goes directly to that method so you you
call a method which receives string you
pass a string and string ends in
JavaScript also when JavaScript calls an
event inside of C it does very similar
things so this event accepts a string as
an argument and then JavaScript passes
that string as an argument into the
event so this is what seemingly happens
but this is not what is happening
because CL does not really talk directly
to JavaScript in between we have the nav
extensibility framework so this nav
extensibility framework has some
functionality which I definitely do not
know exact name of because it's hidden
somewhere deep in in the stuff that
Microsoft has created so I have given my
own names to to to those components so I
will call them proxy methods so when you
call a method in inside of an interface
what you really call is this proxy
method which lives in the framework and
what you do to this proxy method you
pass a string and then seemingly this
proxy method also passes the string onto
the method and the same happens in the
opposite
direction however it's not that simple
uh what we have really is we can pass
anything to this proxy method and then
imagine that we pass objects so we pass
an object object which is a net object
this proxy method will retrieve this
object it will serialize it into Json
and then calls the method with the Json
as parameter in fact on the opposite
direction we have JavaScript which is
passing an object again its own object
JavaScript is object based not object
oriented it passes the object onto this
serializer inside of the framework
serializer receives object convert it to
Json and then we have that Json which is
passed onto the deserializer which
deserializes that into a net instance of
an object which is then passed onto nav
so this is what's happening so maybe you
haven't uh tried that yet or certainly
Microsoft's demos do not explain that
but you are totally able to pass objects
from one language tier to another
language tier so how does that really
work the object first must be
serializable no no objects is Ser no
objects are serializable by default so
we have to make them serializable if
it's a serializable type then the
framework will convert that to
JavaScript sorry to Json whenever it's
passing it onto onto JavaScript so this
nav runtime handle synchronization on
the left hand side we have an example of
a C class and an an example of how we
instantiate that class in in JavaScript
we don't have class definition we just
have Json so it's instantiated directly
we don't have to have a blueprint uh for
a class in JavaScript so we have this
object as a Json object so these are
equivalent so if you pass this Json onto
C meth event which expects person nav
extensibility framework will deserialize
that into this person class and if you
pass this person class to JavaScript the
same framework will serialize that into
Json and then JavaScript will receive it
as Json and handle it as
Json so for example here if we take a
look at my um one controled in to rule
them all we really have one event
handler which has message as parameter
so this message apparently is an object
it's not a simple data type and the same
thing on the other end when we call
JavaScript we have a method called send
request which passes a request and as
you have seen this request is a very
very alive class it has content it has
method it has properties it can do many
different things so but I can still pass
that on and all of all of these objects
together with their content will be
happily transferred around so let's take
a look at how can how we can transfer
objects back and forth so I will switch
on my demo number
three so um doing this and then
rebuilding so what's going to happen
with demo number three
again I have exactly the same page it
just loads slightly different JavaScript
so I run the same page so it still says
I'm doing my stuff asking me can I call
JavaScript I say Yes And now when it
call JavaScript it it says hello world
where does this hello world come from so
uh okay I will explain this one uh in a
minute so inside of my demo specific
logic I have
this actually over here I have this send
request method so this send request
method receives an object so it's
represented as R this is pretty good
name for JavaScript you know in CL it's
not but in JavaScript it's pretty good
uh and then what I do with this I pass
it to my own object which is request
Handler to Method handle so this method
handle does some funky stuff so let's
take a
look so it okay I will explain in
details in fact what it does it it
locates the prop a proper request
Handler here so I have string request
the trick is the method should match the
the class name so if I'm instantiating a
string request inside of Cl in this
instance here so if I go back to my code
units and show that here I have string
request so I'm instantiating a new
string request then I will just have to
have a string request function inside of
my request Handler and as you can see
here I have many more request types like
CSS Handler HTML Handler JavaScript
Handler all of them are supported as
independent functions inside of my
request Handler so this handle function
will locate the correct Handler function
and then it will load it by passing the
content that it has inside of the Json
and it has it inside
of sorry type and then it has content so
it passes the request content onto my
method so this content in this case is
something that I will show on screen
inside of this alert so content is this
s but it has this string so where does
this string come from it comes from here
it is this string property that I've
assigned inside of my
Constructor so let me just wrap it up so
I instantiate an object assign a
property to that object object pass it
on to JavaScript as Json JavaScript now
sees it as a full Json object and then
handles it using its own logic and has
access to everything that I wanted to
serialize okay so this is how to pass an
object to JavaScript also I have got a
response so I have got JavaScript
responding to my request so let's take a
look at that so I'm going back into my
controlin so my Handler after it
successfully executes my function that
it retrieves then it calls message event
so this message
event calls
raise message and then passes a Json
object and then this raise calls
Microsoft Dynamics and a invoke a
sensibility method by passing message as
event name so let's take a look at what
this is it's this one okay it receives
this message as parameter okay and it
will end up in my
Cal in my page inside of my message
event and then I have net object which
is javascript. message where I have
message. type which is a member of that
class so in essence I have my JavaScript
instantiate an object on the Fly this
one and pass it onto C so it says type
is T let me build
that
sorry and rerun
again
so I'm doing my stuff can I call yes
hello world and now I have event it says
I have not just received message from
JavaScript which is string request so
I've got the content back from
JavaScript okay so this is how to pass
very simp simple object data between the
tiers however we are not limited to just
that we can get even crazier what about
dictionaries have you used dictionaries
let me see who has used dictionary okay
good so if you take a dictionary and if
you think of what a dictionary is it's a
catalog of unique Keys plus values okay
so this is exactly what objects are they
are cataloges of properties where each
property has a unique name and
JavaScript uh actually an nav framework
does very nice thing because it
serializes a dictionary directly into
JavaScript where every key becomes
property name and every value becomes
property value
so one dictionary becomes one object and
it can really be like whatever key and
whatever value actually key should be
string but value can really be an object
so it will still be properly serialized
as long as that object is serializable
so you can do that as as well and you
can even do the opposite direction as
well as long as you know what you're
doing because um when you're serializing
add ditioner into JavaScript serializing
an object into Json is simple because
you just take a look at properties you
copy the properties into into values uh
string representation of those values
and that's all but in the opposite
direction the Ser this serializer must
know okay what is the type that you
expect if it doesn't know it cannot
deserialize so you could manually
deserialize that or you can receive J
object which is essentially what
framework returns to you whenever it's
unable to deserialize so then you can
handle the serialization
manually okay let's take a look at how
we map dictionary to Json so for that I
will just un I will just switch on my
demo number four and then run exactly
the same
object and before I do I will just
explain why because I'm still running
the same code just with a little bit
different logic so here instead of
running that Handler I will just show
that I've received an object and I will
show Json representation of this request
so let me run the same page
again I will click okay yes and it tells
me I have received the following object
let me actually zoom into it a bit more
so take a look at this
content content is another object okay
and if I take a look at my definition of
my request
object which is here this content is
really
dictionary so I'm passing a dictionary
onto JavaScript and JavaScript receives
it as an object and then from then on I
can treat it as an object inside of
JavaScript okay let me click okay here
and that's all uh when I receive it back
it's exactly the same thing because I
have received a class which also
contains a diction AR so um you have
seen it earlier so this message class
also has dictionary called content I
will use it later on so I don't have to
prove that I also deserialize this
dictionary properly using net okay so
that much about Json uh let's talk about
deployment let's see uh how to handle
deployment issues um we
have we are all very familiar with
manual deployment so we know what it
takes to deploy uh a control Ed in
especially We Know What It Takes when
you make a change to an existing control
in to actually deploy that it it it can
be several manual steps and there is an
ancient wisdom which says that anything
that should be automated should be uh
anything that can be automated should be
automated I don't know really if it's
Chinese or Indian but it's it's very old
and very smart so let's see how we could
uh if we could automate that my stance
is is that all of uh steps in the
deployment process can be automated
which means they also should be
automated so if you think like okay what
do we need to do we need to zip content
of a resource can we do that somehow
automatically yes uh we need to inspect
and find the public key token can we do
that automatically yes we need to import
this control it into na can we do that
automatically yes so to every question
we'll get finally the answer that says
yes so let's do that let's actually
automate so how do we um how can we
automatically uh deploy assemblies first
uh to deploy an assembly we need to
first load and I'm talking about Powers
shell here we need to load all of
satellite assemblies which means all
dependent assemblies from my assembly
into memory I will explain why we need
that then I need to search for all types
inside of my assembly so during build
progr says I know what my assembly is
just let me stop for a second uh you
have all seen that I have been deploying
new version of my controller than just
by pressing F6 in Visual Studio because
Visual Studio was doing all that on my
behalf so when I run it from Visual
Studio Visual Studio knows which is my
assembly because it has just built it
and then it passes that assembly to to
to Powershell and it inspects it so it
loads all types from my assembly and
looks for the type which exports the
attribute which is sorry
this
one so controller in export and when it
finds such a class or sorry type which
can be class or an interface it knows
that it needs to do something if it's a
class it doesn't need to do anything
special if it's an interface then it
needs to create a resource folder
structure so if I don't have a resource
folder already in my project then the
project will build it from a template
and then suddenly I will get this
resource project sorry folder here which
which will have a subfolder for my
control edin and inside of it it will
have a standard structure for a control
edin resource file built automatically
by Visual
Studio then next step is it needs to
read the public key from ID easy peasy
so it simply opens the the the file and
inspects for the public key then I need
to zip the resource file again very
simple I just say like okay this is
directory take all content and pack it
into zip folder then I need to copy the
files to client and server if necessary
at that stage if I can't copy I have to
restart NST so I restart NST all of that
can be done through uh through
Powershell and then finally I call
Powershell command l in 2016 to import
them into uh into nav I've also posted
uh on my blog about how to do that in
earlier versions so you just need a code
unit but you you still can automate all
of those steps and get control at in
inside so I will not really do much I
will just show this Powershell script
here so uh it's over here so it has
some quite some code I will not explain
it because I've just explained what this
piece of code
does uh I will just prove that I'm not
doing any tricks here
alert hello Tech
days and press
F6 and then run a random page okay hello
Tech days
so let me take this away because I don't
need it
anymore that's how to deploy from visual
studio and that's all I can say about
deployment so now we have our controler
in inside of Visual Studio we can do uh
smart things we can really start
properly
developing another big problem is
automatically resolving net
interoperability assembly dependencies
so what am I really talking about here
in this title you have seen that I have
a control addin which is client side
thing living in JavaScript but I have
also been using some net and this net is
not client side it's server s side
because you cannot have client site
inside of an asp.net page which is what
web clients are all of this stuff that I
have done already I have been showing it
from the windows client but all of this
really works from the web client so let
me actually go to this demo
66011 and then let me run that from my
tablet client so I will just
say page is this one and it runs hello
Tech days I'm doing my stuff okay may I
now call Page method yes and then I got
that so all of this is working in in in
all clients it's not just um it's not
client side stuff it's all net here is
server side since I have a server side
assembly I still have to deploy it
correct and deployment of server side
assemblies is also a pain not as big a
pain as it is to deploy client side
assemblies but it's still is a pain uh
and it's especially pain if we need to
move between different environments so
what I would really like to do is I
would like
to uh actually before I before before I
say uh what I would like to do let's
take a look at how we normally can
deploy
assemblies uh we can deploy assemblies
to either addins folder of service tier
or client tier or we can deploy them to
gak Global assembly cache both have pros
and cons I won't discuss them uh
so what whichever option you choose you
might encounter problems especially in
development when you are developing with
multiple versions and then when you
suddenly code doesn't compile because it
references an older version and you have
accidentally overwritten the file
because you didn't think of that etc etc
etc so
um what I would like to do is I would
like to automate that so um the thing is
if we automate deployment to gak or
service service tier or client tier add
in folder we do it per environment when
you move to different environment you
have to automate again again like you
have your development environment
everything is automatic then you move to
testing environment and everything is
okay then you move to staging
environment see it takes a lot of
working to actually get to production
and then maybe there you know there may
be multiple tenants etc etc So to avoid
all of those
issues
uh yeah I'm I'm jumping ahead a little
bit I apologize So to avoid those issues
uh I would I would like to have some
different approach uh let's take a look
at client side there are two types of
deployments client side and server side
so when we talk about client side
deployment that's something that 2015
and newer versions can automate so uh if
you have an assembly which is required
by client side so you can only put it
into server side edin folder and then
server will push it to the client if
client needs that assembly okay that's
simple so if the assembly is not present
in the there and if assembly is not
present in gak and if the assembly
hasn't been pushed already it will push
it and install it in a temporary place
and keep it there until you change the
version if you don't change the version
you can deploy the new file onto the
service theer it will never update the
client so you might have an
issue uh in 2016 we allegedly have
client and server side deployment so
Microsoft says it works I wasn't able to
make it work myself but I trust
Microsoft so um at least it's designed
to work and if it's not working probably
I've just encountered a couple of bugs
it will be fixed over the next couple of
cumulative updates so what I'm talking
about here will work maybe it doesn't
work for all situations right now but it
certainly will so what it does you have
this addins table which used to be
called client addins so uh in this table
you can upload
net interoperability dll so when service
tier does not have a dll which it needs
inside of its edins folder it can
extract it from a database and load
actually copy it to a temporary place on
the server and then load it from there
from that moment on and again we have
the same issue uh we have the issue that
if you want to deploy new version you
really have to version up if you don't
version up then your file will never be
updated so if you don't have version
practice inside of uh Visual Studio
development you will have issues another
problem is that this whole process
ignores the fact that assembly is not
identified the way how Microsoft is
identifying it inside of client at in
stable it is identified using fully
qualified name yes Microsoft has taken
fully qualified name apart but they have
also made a bug back in 2009 sp1 which
is pushed forward because of forward
compatibility which is ignoring the
version tag so that's maybe why I wasn't
able to actually make it work but this
version tag will actually cause problems
so in theory you should ZIP the assembly
into zip file imported into to control
it in and then it would just should
automatically run but it doesn't really
work like that so what I've done is I've
reinvented the wheel I've come up with a
better wheel so uh first I had SE
several goals I want to have full
backward compatibility back to 2013 I
wanted to go back to 20 2009 R2 but it
it would be it it wouldn't work because
of limitations in 9 I want this to apply
to both server and client side I want to
redeploy assemblies even if version does
not change so if you have if you have
built a new dll you just deploy it into
the database and also it must have zero
footprint because I do not want to ever
deploy anything to my service deers this
might have to do especially with future
uh with man Services by Microsoft I I
don't want to put any assemblies there I
just want to run everything from the
database so
so how do I do that there is an event
inside of NET Framework which is called
assembly resolve and what happens when
net application is trying to load an
assembly that it doesn't know where it
is
so net is like collection of assemblies
whichever application you have talks to
15 20 different DLS all over so how does
Net know which dll to load from where it
knows because there are two places where
it must look first first place where it
looks is local folder so is the assembly
available in the local folder if it is
it is loaded from there it looks into
Global assembly cache if it's there it
will be loaded from there however if it
can't find it in either of those two
places then it needs to look elsewhere
but NET Framework does not want to look
all over the dis and and try to locate
your assembly it simplif fires this
assembly resolve event and lets your
application choose the location so
this is how nav locates your control
Ence your net interoperability DLS that
you deploy to service tier folder what
it does it fires this event inside of
nav service tier or client tier and then
the client or service application looks
into the addins and further into any
subfolder that it finds over there what
I want to do is I want to tap to the
same thing I want to expose this event
into my Cal so that my Cal code can
actually respond to that
and I can resolve uh my assembly from C
from C how should that work uh the the
output of assembly resolve event is the
assembly it's loaded assembly and net
doesn't really care for most practical
practical purposes it doesn't care
whether you have loaded from a disk or
from a database or compiled it on the
fly it doesn't care so it just requires
an assembly um there is a problem sorry
there is a problem in CL I cannot use
this event directly
because this event returns a value and
cl does not support such events so I
have to have a wrapper class that will
support that event and fire a compatible
event inside of Cl however if I do that
if I have a wrapper class then it's not
zero footprint anymore because I have to
deploy that assembly which hosts that
wrapper class that talks to CL so what
I'm actually going to do in the end uh
I'm going to compile that assembly
resolver class on the Fly uh in memory
so uh let me quickly show that I will
just have to hurry up because time is
running and I'm not so let me quickly
just show this assembly resolver while
I'm showing it what I will do here is I
will first
run
this net assemblies
page and I have two assemblies inside I
will delete all of them so I don't need
this I don't need that I will close my
client and I will restart my service
deer okay so now it's really zero
footprint I will also go to my service
tier
folder
sorry addins and okay I will not go into
every single folder but there is no
assembly resolver in there so I will
quickly prove that there isn't one so
what I will do here is I will run my
client again
and immediately
thereafter I will run this net
assemblies page
again oh I have an assembly in there
what is this I'll I'll explain in a
minute so how did it come there it came
there from code unit one this code unit
one has called my assembly resol
resolver code unit so let's go to this
assembly resolver code unit so it has
quite a lot of
methods the core of this method is this
get source so uh it starts
here what I do here is I have a source
code for
C uh assembly that contains this
assembly resolver class it's minified
just to consume space and to scare
people off no uh so I will close that so
how do I use that I have this compile
resolver assembly so I load this source
and then I load it into assembly
compilation infrastructure inside of net
and what I end up with is an assembly so
this is compiled to a location on disk
so this is path to assembly I simply
pass do uh that uh result into install
resolver assembly this install resolver
assembly is a function which takes that
assembly takes its bytes and essentially
serializes it into my blob field in the
database so and then funny thing is it
also subscribes itself essentially the
assembly which was compiled in memory
subscribes itself to an event which was
uh which exists in the page so it's kind
of scary but it works so it the logic is
if there isn't this assembly resolver
assembly then it will build one install
it so that it never needs to build it
again so it can always use it from the
database so in the future what we have
here is this unresolve assembly this
unresolve assembly calls this resolve
assembly server side which analyzes what
is this assembly that you need then it
will take a look into this assembly
table and if it finds one it loads it
from The Blob field and streams it in
actually loads it into assembly and
passes it on to Net Framework which is
running behind uh nstd so this is how I
resolve assembly so now I have this
assembly resolver let me let me prove
that there is no black magic in the
background I will just run
my sorry my demo number two for example
I'll run this page so it says hello Tech
days and then it fails why does it fail
it fails because it cannot load an
instance of the following NET Framework
object so I don't have this v.com
controlled in template assembly so
I don't have it on my service tier and I
do not want to have it on my service
tier what I want to do instead is I want
to install it into my assemblies so I
will simply click import assembly I will
select that and click open and then I
will run this
page and Page runs so you don't have to
deploy anything anywhere so the only
thing you need to do simply import
assemblies that you need into this table
and then whenever net sorry CL needs
them it will extract them and pass them
to net environment which will then be
able to run them so you only need
assemblies in development environment
everything else suddenly is available
and then when you take a backup of the
database move it elsewhere or take a
tenant and move it move it elsewhere all
of that is already there so you never
ever have to actually deploy anything
anymore not to clients not to
servers
okay so um this closes my uh topic of
assembly U resolution so how nav
resolves assemblies so with this
infrastructure so far what we have is we
have one control which so far doesn't
look fairly uh flexible we have
infrastructure which allows us to easily
deploy stuff for development and also
easily deploy stuff for runtime so I
never have to deploy anything to my uh
server tier anymore so let's actually
Focus now on user interface so let's see
how to actually create that kind of POS
solution for example using a framework
as simple as this so you really do not
need much more code to have that POS
running uh essentially you you can just
keep using the same exactly the same uh
scaffolding classes if you want uh from
C and the same JavaScript library as is
so we don't really need to to make
anything bigger than
that what they teach us in school is to
create user
interface and now we are talking about
control it in for JavaScript inside of
nav we need to create Dom manually so
you really need to create all content
manually by manipulating Dom using
JavaScript directly so you cannot just
pass
HTML uh they also teach us to embed
stylesheets into the resource and they
also teach us to embed images into
resource and also if we want to have any
client side logic which we do that's
JavaScript then we need to embed scripts
into the resource or we need to to to
reference an external scripts which run
somewhere else so this is how Theory
goes and this is what we can read in
help files and all of the examples what
they don't teach us in school is that
nothing at all needs to be embedded in
the resource okay couple of things you
still need manifest you still need one
very lightweight script so script such
as uh one that you have seen it can even
be simplified so let's take a look at uh
this demo number number seven which is
going to be fairly comprehensive where
we're going to see how we can actually
handle HTML dynamically CSS dynamically
and even JavaScript
dynamically so let's take a look at demo
number seven I will close this page then
I will prepare my demo uh just a second
I will go
to my visual studio I will say that I'm
now inside demo number seven I will
rebuild my visual stud does all that
stuff that we've seen so far it deploys
this assembly into uh into uh
n and then let's take a look
at demo number seven page HTML at the
core of
this is HTML request so what is this
HTML request again it's a class which
has very simple Constructor actually it
has several overloaded Constructors it
has three proper
it has HTML which is text then it has
Target selector this is the parent so
where do I want to append this HTML and
then finally boole and clear do I want
to clear the content of that something
before I put my stuff
inside and then I can instantiate this
HTML request with that HTML or any
combination of those um those
properties so from here I create this a
HTML request and then I do this div
hello world then some input type button
with value click me and when it's
clicked it says it does alert I'm
clicked so I will save that and I will
run this page so hello world and there
is this click me button when I click the
click me button it says I clicked okay
so I will uh I'll do okay and then I
will close this
page so so this is a very simple demo
let's take a look at how did we render
this HTML what how did we handle this
HTML request so I'm going back to my
uh sorry I'm locate JavaScript so you
already know that I should have a method
sorry function which is called HTML
request so there it is so what does it
do it locates using jQuery uh sorry it
first checks do I have specified this uh
Target loc uh Target selector if I don't
I assign control it in this is the
default um ID of a control where you
should put all your all your stuff when
you create controls and then I select
this element using jQuery and then if
clear is specified then I empty that uh
element first and then I simply append
this HTML so with this approach I have
just passed some random HTML into
JavaScript and JavaScript has rendered
it and it even has um JavaScript fun
functionality I can click the button and
actually do something with that button
okay let's take a look at the second
instance we have HTML plus CSS so I'm
not embedding any CSS inside of my uh
resource file so here I'm making an HTML
request again it's the same uh HTML
however I'm adding a little bit of CSS
so I have CSS request CSS request is
different so I have two properties
selector and value and inside of
JavaScript
what I have is just a second let me
close
unnecessary
files inside JavaScript I will find my
CSS request so it will locate the head
element then it will append style and
then selector plus value using valid CSS
syntax so that you don't have to worry
about that and then when I run this page
I will apply font size and some color
and some font family so it really looks
different and I can still click this
button it says I'm clicked okay the next
thing that I have
is
sorry is C is actually HTML plus call
back so apart from um just plain HTML
plus CSS I have a call back so let's
take a look at what this button does so
it it still says click me but on click
it calls this class dollar dollar event
message so we have seen that class
already it is part of my framework and
then it calls message with button click
message and passes the ID of the button
so I know which button was clicked and
then here in this message Handler I'm
checking okay what is the type that I've
received it's button click I could have
made it strong type if I wanted I could
have even compiled it using this
assembly resolver but I just didn't have
time you know this is just a
presentation so um so here I check this
button click and then I essentially do a
CSS request what do I do with CSS I
first hide the button which was clicked
and then second I change the color of
any uh any element which has style uh
sorry class hello so let me run this
page says click me I click and it hides
the B button and changes the color to
Green so I have uh even called back from
my dynamically generated HTML plus
dynamically generated JavaScript I call
back into
nav uh of course we could make it even a
lot different so as I said you just need
one control to solve all problems I've
been showing very simple user interfaces
but you can really use this the same
infrastructure to create something
fairly uh fairly easy which is not
supported by itself on the JavaScript
framework like timer in a page so have
you tried that so let's try to just
create a timer out using C so I'm going
into this JavaScript page and I have 22
minutes I don't know know if I have
enough so here I have JavaScript request
here I have one constant I will just
copy that into memory so just if I
fumble too much and I don't manage to
create that uh directly I will uh I will
copy I will paste it back so let me just
pass JavaScript so what I will do here
is set
interval and then I will do
function and then I will call it every
second
okay
then what I will do inside here is
Microsoft Dynamics nav invoke
X
cility method and then it's going to be
message and then I'm just going to
Mass sorry
uh this happens sometimes with this
keyboard here so uh I have
to copy this
character it always happens during demos
I've spent I don't know how much
time preparing this demo and it never
happened so and I'll just pass a blank
object so let me save that what is there
yeah message J yeah yeah yeah thank you
thank you so uh you have saved a little
bit of hair from scratching so uh what
happens when message fires I have this
timer event sorry uh it should
be here I should say type
is timer okay
and content is blank I think that's
correct let's see if it doesn't work I
will just paste the one which is
essentially the same just without bugs
which I might have introduced so let me
run this
page okay it doesn't work so let me just
uh put this constant in
here
text time is if time is running out so
what what did they so it's still called
set interval yeah type timer yeah I've
I've messed up a bit of the structure
but doesn't really matter so I will
run and ping and ping and ping and ping
so let me close that then let me take
this ID and go to web
browser and then paste it in here and
ping and ping and ping and ping let I'll
I'll let it ping as long as it wants so
this is example how you can really just
think of something that works in
JavaScript and HTML and CSS and just
make make it happen without ever
changing your control ENT I didn't have
to change my control ENT for
this okay um so let's take a look at
further things so let's actually own the
playground we do own the whole
playground when I say playground I mean
mean the whole environment the whole
client Everything Is Ours not just this
tiny div inside of an ey frame inside of
a div inside of a largest structure
where and be puts our control we own
everything so let's take a look at this
demo where I will first take the whole
page and then I will just use Angular JS
which I will also load dynamically I
will I will not embedded into my
resource so I don't have Angular JS
inside of my resource I can prove that
here so there is no angular I just have
jQuery so what I will do here
is inside of this
sorry this
demo is I will instantiate an HTML
request which is going to download
angular from Google then it is going to
call this full screen function inside of
my framework let me just quickly show it
so this full screen
function does some hacking around we'll
see that later on then I change CSS I
essentially apply font and then I make
an HTML request where I inject some HTML
code which has some angular syntax
inside are you familiar with Angular JS
let me see okay so this is an extremely
simple example but you can I mean it's
here just to prove that angular can be
used this way from from within um nav
without ever having to really develop
and P all together and deploy all
together so I will run this and okay I
have
hello and then I have this name here
which actually updates as I'm typing so
this is a simple angular model which is
going to which is updated automatically
let me show that from uh JS this guy is
still
pinging which okay 29
sorry okay so I have it in full page now
so how did I get full page out of
something that really is nav because you
can see here that
this H my developer tools have stopped
working never mind trust me this
actually I I
should I will need developer tools so
let me close this now and then let me
restart my edge
browser okay so let me prove that this
really is inside of Na as you can see
this is just this tiny part which is
consuming full screen so it has hidden
everything else so I have hidden
everything else by using J uh sorry J
query to get to the content of the upper
window and actually hiding stuff that I
don't need and consuming all available
space for myself and then again angular
works as advertised so this is just a
simple example of angularjs and some uh
like crazy thing like what you can do
with a client what Microsoft doesn't
really tell you that you can do okay
good and now for crazier things so what
I'm going to show here is really stuff
that might Microsoft does not want you
to do so in all of my interactions with
Microsoft Microsoft was saying you
shouldn't be doing that and my response
to them is I actually learned about this
from you because you have posted a
knowledge based article or a blog post
something like that which explains how
to do that you know Microsoft wasn't
really showing stuff that I will show
but they have shown the concept which
I'm just applying exactly the same thing
just to achieve different things so
let's take a look at what I'm talking
about so let me own a little bit more of
this playground by editing asp.net files
so the whole client is nothing but
asp.net so we can inject our asp.net
stuff or sorry our JavaScript or HTML or
CSR or or whatever else we want so here
I have
one useful demo like I have done slight
tiny changes like here what you can see
is I have those alternating colors in my
grid so if if I uh sorry if I open for
example a customer
list you can see that I have alternating
colors in the grid okay I have something
more when I click new it actually shows
mandatory Fields as yellow but also when
I try to do something stupid like
deleting a
customer it hides the yes button for
five seconds to force me to actually
read the message before I accidentally
click yes so oh there is yes button so
yes let me delete that now okay I can't
I cannot so this is something that you
can do so this is not something that you
achieve using controled in this is
something that you really achieve using
U injected JavaScript okay so you can go
and really become crazier
so let
me show another demo like why not doing
something like
that okay I hate the color but it's here
just to make a statement you can make it
as ugly as you want
or as beautiful as you want so it's
really up to you so there is nothing in
the client that you cannot take
ownership off all the elements icon sets
fonts colors whatever positioning if you
want everything is at your disposal so
that was um the last crazy demo I won't
do that again so Microsoft will tell you
don't do that I will tell you please do
why not not there is nothing to lose so
you have asp.net files if you simply
injecting your scripts in there you will
not break anything the only thing you
will break is when a new version comes
and deploys new aspx files you will just
have to apply the same settings which is
just adding a line of code so all of
those changes are nothing but an extra
line of code inside of ASX files and
that's it so some ideas that I can give
you now that I've shown how to really
handle user interface from from
JavaScript
um do not store HTML CSS or or images or
anything in resource files store them in
the database like in Blob Fields load
them on demand and pass them as
necessary construct HTML construct CSS
programmatically construct JavaScript
programmatically write code that
generates JavaScript I have even done
that I'm just not going to show so I
have an object model which is
essentially just a set of screen
elements something like Dom which I
create inside of Cal which generates
JavaScript to respond to events inside
of that Dom so all of that can be done
so you really do not need to put
anything into your resource everything
can be pure Cal and deploying clal is
not a problem deploying clal can be done
using extensions all of this what you
have seen today can be an
extension okay
so you own the show you have seen it so
be creative try to see things uh like
what else you can do okay I do not end
here I have sixth part to go so the most
important one synchronizing calls
between JavaScript and cl what is this
about so when CL calls JavaScript this
is what happens I don't know if you can
read the yeah it's pretty readable so
when Cal calls JavaScript they start
executing
simultaneously okay and either might end
sooner than the other okay you never
know the thing is that c will stop
executing while JavaScript might still
be going on you you just have no way of
knowing if JavaScript is still alive
okay when we call Cal from JavaScript
then JavaScript is going making a call
to Cal at one point and then both of
them go on however Cal let's say it
still does something while JavaScript
has completed the call JavaScript does
something in the end what it does is it
goes and chck
is CL still busy and if yes then it
shows those dots that run across the
screen and then repeats the loop so is
nav busy is it busy actually it doesn't
do the loop it's a bit bit SM smarter
than that but in the end when suddenly
CL stops being busy JavaScript also
completes and yields the control back to
user so first the question why the
difference why do we have that
difference between JavaScript and cl why
JavaScript is waiting for cl to complete
and not the opposite way
around locking no okay think for it if
you want a little bit later I will just
give you my explanation because
JavaScript is running all the time you
know JavaScript is not like C there can
be events like Dom events users clicking
like there can be Pages loading
automatically depending on what is
loaded in there so it's a live animal so
it might never stop like this ping thing
JavaScript is pinging all the time so CL
cannot wait for JavaScript to complete
doesn't make any sense JavaScript is
just it has a life of its own whereas
Cal just like in the windows client you
cannot have control while CL is running
so only when CL stops running you get
control back so this is the
reason this has both negative and
positive consequences negative are and
these are pretty obvious you cannot have
return values on any end you cannot call
JavaScript to say give me the answer of
something back
okay so let me just give you an example
of that so here I
have one
simple I hope it's sorry it's this demo
yeah I will run this and then there is
this assist edit button when I click it
it shows me some uh touchpad where I can
enter PIN and click enter and then it
says pin entered is this okay how does
this this code work it works like this
so this is obviously controlled in this
is a Windows controlled in so this is
what it does message pin entered and
then it retrieves the pin and shows it
very simple but it is a typical pattern
it can be hundreds of line of code
happening after that okay and we you
know when we write clal code we actually
do write hundreds of lines we write
so-called God functions functions that
attempt to do everything in a single go
just like code function in code unit 80
which has
1,274 lines so that's a big one so the
first good aspect is that that cannot
happen with the code because you cannot
do that with JavaScript you cannot call
JavaScript and say okay give me the pin
because you can just say show the pin
dialogue and then somewhere else I will
listen to an event that says okay pin
dialogue is now closed this is the value
okay so you have to restructure the code
so negative consequences CL is not aware
if JavaScript is busy also you might
have performance issues you might have
even crashes if you don't handle
synchronization properly however your
code becomes more modular your
architecture becomes cleaner and you
also separate UI from business logic
much better because everything is event
driven okay so let me just give you one
more demo like what kind of issues we
can have due to synchronization
so let me go back to demo number 10
which is already known to us so this is
this ping okay I have
ping
however let me switch on this demo
number
10 and rebuild this demo number 10 has
some specifics so what does it do
specifically actually nothing uh except
that
here I making a sleep of 1 second and
I'm running this timer every 200
milliseconds so try to think of that
JavaScript JavaScript is pinging Cal
five times per second and every call in
CL actually takes a full second to
complete so there will be five pings
from JavaScript into Cal until actually
CL gets a chance to to respond because
it's or doing something else okay so let
me save this page and then let me run
this so there are no specifics here and
then let's observe so I have ping ping
then ping then
ping
H okay let let me close that let me just
go here into web
client okay not
you okay are you see see those dots
running and then ping and then
nothing and then four of
them if I leave it running long enough
it will crash you know because CL will
become clogged I cannot do that I must
not do that I have to take care of that
okay now see it says that it's taking
like unexpectedly long time to actually
process that okay good um let me uh let
me stop that quickly okay I will I will
just probably have to restart let me fix
that by actually doing a synchronization
attempt so while it's running in the
background let me explain how I can
synchronize there are two ways actually
no two two two areas where I can
synchronize calls first is there is this
environment object which keeps track of
busy property and on busy changed event
so you can always see from JavaScript if
CL is busy and when this busy States uh
stat changes and also when you invoke an
extensibility method which means invoke
an event in Cal you can skip if busy so
if if JavaScript sorry if CL is busy you
just omit that and then you have call
back which tells you okay now the call
has been completed by CL so let's take a
look at
this sorry demo number 11 and 12
actually so uh the slide has a bug so
here I will just switch on demo number
11 so let's take a look at specifics for
demo number
11 in essence it says true it says skip
if busy okay and then I will run the
same page again so I load that and then
let's observe okay now I will probably
have to restart my service tier because
it's you know as I said it's going to do
crazy things over time it will even
crash it
so it's restarted I go back
and when it
loads if it
loads it's not running did I just stop
it or
what okay so let's do it
again okay and ping and ping and ping
you see it executes every second because
it skips all four of the others let's
take at the more complicated version of
this so this is demo number 12 and here
I have full synchronization framework it
has quite some specifics in here so let
me just quickly explain the theory what
it does what it does is is that it first
if it's busy it will cue the event it
will put it into um an array of events
and then when it calls extensibility
method when it gets back it tries to
process the next event from the queue so
if there is an event in the queue it
takes it from the queue and pushes that
onto na unless na is still busy with
something and it keeps doing that okay
so uh and also at every moment it knows
what was the last event received so in
case you receive exactly the same event
with exactly the same arguments it
rejects it otherwise it would just you
know this array could grow it would go
you could get stack Overflow because
because you could just get far too much
information inside of that stack pretty
quickly so um let me not explain that
you will be able to to to read that uh
all of that on my blog so let me just
rebuild this
one make sure that I have switched demo
number 12 and then here I will switch to
my console view my console view doesn't
really show anything in this stage but
here as you might see it has a lot of
console information it is logging what
it's actually doing at each step so that
you can really see what's happening so
I'll refresh the page it will nicely
refresh because it's not stopping
anything on the service tier and I will
still have the same behavior ping ping
ping Etc but here you can see what's
going on so it's rejecting events
because that duplicate it's deqing them
it's queuing them etc etc so it's nicely
handling that queue and synchronizing
all the calls for
you okay so couple of takeaways for you
as you have seen web clients allow you
to own the whole playground completely
everything is at your dispos second
hopefully is you will not create
hardcoded control EDS that have
everything crammed into them so that you
have to deploy them every single time
when something changes you will
construct everything on the Fly and then
finally I hope you have seen how to
combine the power of net with
flexibility of JavaScript to achieve
really anything that you can think of
and some more takeaways uh all of this
will be on my blog tonight so you will
be able to download all of these
examples all of this code visual studio
will be on GitHub so I hope you you get
there and and use those uh bits to to
learn something or to see like in detail
how the stuff was done here during this
presentation thank you and now let thank
[Applause]
you we have 1 minute and 6 seconds left
for
questions I hope we can steal a couple
more minut yes we have a question over
there oh one but then
yeah so if the question is good you get
a
shirt I go
there you just edited the ASX files to
modify the layout of the the web client
why not build just an addin that breaks
out of the iframe and inserts SS
directly into the browser uh because
there are situations when you cannot do
everything sometimes security model of
the page will not let you access certain
things like one simple example is I want
to change the url like I want to
navigate from my full screen controlled
in back to uh role Center and I cannot
do that because I cannot from within if
frame I cannot change I have to call a
function which resides in the main page
already that's just a very simple
example but there may be more so just
one okay good question so short for you
uh uh is that correct that uh the
JavaScript code only ons on
clients uh in this examp all these
examples yes it runs only on client
there is service side JavaScript just
not here not in
na uh thank you yeah you're
welcome uh remind me if there are not
enough questions you will get a shirt so
one is possibly reserved but I will keep
it from probably a better question if we
have no the question was good it was
just way way too simple so uh we have
okay we have a question over
there yeah hi there one of the
challenges we've had in developing our
add-ins is one of styling and you you've
shown there how you can you can use the
manipulate the the own the CSS provided
by Microsoft to your effect but is there
a way to use Microsoft CSS for our
Styles so all of the fonts and spacings
and margins and everything look
consistent with what else is in the web
client yes it is so what you can do
since you have access to the page you
can just load the same links so what you
can do you can enumerate through all of
links that belong to the master page
using jQuery and then simply take them
and copy them into your HTML and also
look for all style blocks and copy them
and put them into your it's you know
it's two lines of jQuery code for that
okay I will uh I will award a shirt for
that one
yeah so no that that's not a
question you're welcome thank you
uh hello um I made the experience that
um in
the the client web client is pretty slow
on rendering 3D objects with JavaScript
I made the same in normal web client and
normal website and it's pretty fast and
and when I put it in the web Cent it's
pretty slow have I you know it's very
specific question I cannot answer that
because it can be due to many different
things as you have seen like that POS
thing it runs fast and it runs fast on
all devices and all clients so I would
dare saying it's something in the code
that you put in there I don't know what
your code does so I cannot answer like
why is it slower in IE than some other
browsers but this is really something
that is not due to framework so the
framework performs pretty well so it
might be something that that IE does
differently so maybe you're using some
features where iie is slow maybe you're
listening to certain Dom events which
are slower in iie or propagating
differently than they do in other
browsers I really don't know so I would
have to take a look at the code to
actually tell you
uh another reserved
shirt
okay any okay one more question why the
windows client do not react on this
synchronization call and you switch to
web client because previous deos runs in
both web client and windows client but
this synchronization when you had timer
y uh with uh the timer runs every uh 200
milliseconds and in Windows client
doesn't work this actually it it was it
seemed to be pretty synchronous in the
windows client so I cannot really say
why I can I can only make an educated
guess here so uh what Windows client
normally does with with events when they
are happening it's trying to Marshall
them in such a way that if they cannot
be passed onto the onto the um UI thread
they are actually queued and fired l
so this is what the framework does
because of asynchronous events in net
because all events in net can be
asynchronous and then you cannot fire
anything asynchronous in CL because CL
is strictly single threaded so what is
happening with the with Windows client
that it's marshalling those events in
such a way that they do not fire outside
of the main thread whereas JavaScript
allows that JavaScript is not
multi-threaded it's also single-threaded
but allows code to be injected and it
really switch is between different calls
and handles them in seemingly multi
traded way which it which is not so I
can just guess that this is the reason
but if you talk to somebody from
Microsoft there might be something else
okay um good question so let me give you
a
shirt and do we have more questions
you're welcome thank you for the
question yeah we have a question here in
the front row
y let's wait for M yes you have shown us
the zero footprint uh uh method of uh
instantiating uh uh new um uh assemblies
will you have a performance penalty for
that when restarting the the client not
at all so it it runs fast blazing fast
so it's something that net does at all
times so if your code is correct it it
compiles like probably takes like half a
millisecond to compile that so no
performance problem not at all no draw
bre spot no no really you know that's
something that net just natively does so
it's it's not really black magic it
seems so from CL perspective like we
were never able to do stuff like that
but in net it's something fairly common
and fairly easy
so yeah thank you you're
welcome somebody loses the
shirt this was a better question sorry I
only have five shirts I have to
distribute it
somehow okay if if that's all then thank
you very much for attending enjoy the
rest of the conference and see you
around in the cloud and elsewhere thank
you
